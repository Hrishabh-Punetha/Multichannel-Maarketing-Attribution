# Multichannel-Marketing-Attribution
Multichannel Marketing Attribution (MMA) (also known as multi-touch marketing attribution) is a phrase used to describe one of several models used to assign value, or credit, to different marketing channels users interact with before deciding to purchase. Companies spend money on multiple channels (online platforms) to drive customers towards their goals. Using these attribution models helps marketers understand the customer journey. 

The purpose of this project is to implement the same, it focuses on analyzing the importance of various marketing channels that are involved in the process of making a conversion. Also, this project focuses on optimizing the advertising spend so that maximum ROI (Return on Investment) can be yielded and profits continue to grow. We use various algorithms to solve the purpose as the goals of different organization vary and a single generalized approach would not simply work out for all the goals.  


## Multichannel-Marketing-Attribution-Models 
## First-Touch Model  
1. Marketers often use this model to measure marketing efforts intended to drive awareness by reaching new consumers for the first time. 
2. With first-touch attribution, the first time that a customer interacts with your company is deemed to be the single most important reason they ended up purchasing from you. 
3. It assigns all the credit to the first touch or the first channel visited.
4. Great at attracting more prospects and increasing brand awareness. 

## Last-Touch Model   
1. Due to its history as the default marketing measurement methodology, marketers often use this model as a baseline for comparing other multi-touch attribution models. 
2. The last-touch model also makes a lot of sense. No matter how many interactions a lead had with your company, they didn’t convert until the last touchpoint. 
3. It assigns all the credit to the last touch or the last channel visited.
4. Therefore, it’s logical to assume this must have been the most important reason as to why they became a customer. 
5. Great at increasing your conversion rates.

## Linear-Touch Model 
1. The true benefit of using a linear attribution model is that it take all touchpoints into account. 
2. Adopting a linear attribution model is a great way to get started if you’re looking to gain a macro-level grasp of your overall marketing strategy. 
3. let, a channel be (i). 
4. v[c]=value of channel (i). 
5. n=number of times channel (i) occurred for that user/chain. 
6. N=total number of touchpoints. 

## Markov Chain Model
1. Markov chains is a process which maps the movement and gives a probability distribution, for moving from one state to another state. 
2. A Markov Chain is defined by three properties: 
  1. State space – set of all the states in which process could potentially exist 
  2. Transition operator –the probability of moving from one state to other state 
  3. Current state probability distribution – probability distribution of being in any one of the states at the start of the process. 
3. Which can be interpreted by the heat map generated or transition matrix. 
4. Removal effect principle says that if we want to find the contribution of each channel in the customer journey, 
5. We can do so by removing each channel and see how many conversions are happening without that channel being in place. 
6. To calculate contribution of channel c1. 
7. v[t]=total conversions with all channels intact. 
8. v[r]=total conversion after removal of channel c1. 
9. removal effect[c1]=removal effect of channel c1.

### Removal effect for optimization 
1. Removal effect principle demonstrates that the contribution of each channel in the customer journey is determined by removing each channel and seeing how many conversions occur without that channel being in place. 
2. In other words, it gives you an idea about: 
  1. how much does a given channel affect the probability of conversion 
  2. which touch points are the most important in the customer journey 
3. Removal effect can take into account either conversion or revenue, depending on the outcome you want to track. 
4. Hence, removal effect becomes very handy while analyzing and optimizing the ROI (return on investment)

