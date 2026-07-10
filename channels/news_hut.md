<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/KGnE1t2xKdokcPy29rEPDZdGCJn6q0-XFabDxpFG2aC6HQqM3vCFGSXfwkza5tbNNxQG2nRFEcFscpWwkNqWVc7w1YPbb3xseiIZfsjCaxXwOJCc_BCg_7ozW62QhibYWMm7eR9HmjX6odoOA_oGagmTV4P_qVO3PJf5s2cVmxzqP6vokwDtfhauWvDVSMV_ePJQ40nbuPnVotSTYS1kMJpXl--OjAs4E6T3PXuqByGqKfy1dD9dbI8_75UZQUwSxHAeib8S29UpBcxnr0yljHEOezaEusCaDT1uUGFreSd78QuA1o7lfeZNeKEQd8p8eZhHVFp8G6wF_h6y_-53nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 187K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 20:46:25</div>
<hr>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS_TQaagjmgZ74AAKxBmXwXBOY_B9XsQSxFT-UjW4FPtLHToOLfKZFewi-1ZCEuHfpR0UHhFeAb9CJ-Hp8GLUGin_Wibbtqy1Tl6euJhzXNnDUV2vJ_YBpdENhXkXO8MES0W1E9Y89z0ocipwMHelmy77xBBs2xzxFcy3hP33m8SRyoaALyoSZE9hQsxINzar551KJafFvz9PwHVSkGjiGqDNxtzG9pqOcLXbeaIWc-zE_888v_jQbCV8fr7GGErTVbuaUc_6w5yhDcGVle4K76hQxShcpEn1mhoRO4Ltun92_VIjP7mWxdJKs30dpM0sfDXOOkvHJJF8TEOxeopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdFEqDwNTxZs2Ii58BzB9q8svz6SgVxULERrn4RA2OTpE8kVst5OljdjfBTAKBu2e1dRED9lLpX27iJDZNH1JpZUCn-KrhTVpr2dR-eJ-zTk9gPDwcJeBPWgelB2PPE_syc2Nmp2gkLcAhVeff212XLJguME0kiao6Xy53Na7pmBGBEziwBdkgCR5z40HY_qbskEFpSon698QroammssZv9ukNCIm50_pEuaX5BRchBEeY7smvDTHf7MasjPyVcYLrotSZGa3QwEU4tccN7y-B1HvB00k_8akO6Hf05xSY_dFbyL2YTBlOt5HfWnuznBMkEPgrdUhh1YskUfvdox6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=ZpuYXEKszUxizkN-WWYbzHue7hbIX2lXU3GAQmpu2IQMiPOlSf1442tKMsmS3ZA6GJS1F0HYzw2DE31D5j6ynCTkRdS8HqojREnCJHNuLjAik7-j1eQysAbdvz_tZRZ1DP6HyxNzEYRZ3XkTY0GTfpRn2xUx9Q-znnmSl7iEDfuegT1m6nwoNgS9tzUeGnjNjlHZkEInVCPDtn5RZL_pBTmc_eQSgcHNjvcO-wCn4grwaPNvSSVQygjqzefZoBi9ndwUoNdA76s_I20vCxrkElsArwdERISnTCNNPSSycOufcHRY8QWRwp5angQblej-y5gDqc4NN7EGxNk8X12brg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=ZpuYXEKszUxizkN-WWYbzHue7hbIX2lXU3GAQmpu2IQMiPOlSf1442tKMsmS3ZA6GJS1F0HYzw2DE31D5j6ynCTkRdS8HqojREnCJHNuLjAik7-j1eQysAbdvz_tZRZ1DP6HyxNzEYRZ3XkTY0GTfpRn2xUx9Q-znnmSl7iEDfuegT1m6nwoNgS9tzUeGnjNjlHZkEInVCPDtn5RZL_pBTmc_eQSgcHNjvcO-wCn4grwaPNvSSVQygjqzefZoBi9ndwUoNdA76s_I20vCxrkElsArwdERISnTCNNPSSycOufcHRY8QWRwp5angQblej-y5gDqc4NN7EGxNk8X12brg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHU0bQPTXx84WC3vxRpgMZHTs6woLF85PuswU3Hxo4pF-IFY9AcyPPQHaqfMU6HckEGoKHKS5VsRfwvhl-Vf81agxvmuUdAoGeKvOqqFn5FXwHV5wrVj8luNBFt7nxEMBzTlHsiDmhPMaEsvM4eebYL7NO1twLcM1lHV9Q3t_NDARYDBymOrxNlX4E9Ez0-tlf_n5ghRPzwUvwwNcHtBfqORvSn5iX0ZXQp5iVGZIa4CvfKWQ3RmCjcIGV2gGX0Ne98h9NncHOec9H1EbCYE_kByY2eridc_HxjW3oLATs5zHnSMkl30rARMlowxYFprStnX1FIrzaVFcIu27BKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUsjWXQG5QPbV5o-yPfic5CkmmhYvqUjOvvNramn5dh6wnzC0nLbrvfysb6qPv3lqXdyStrCgIz0FwR2fHRSnl3H399iTYbmD9LaIuMeM3o8PvGrB9Fz6DuLVE-XujUpeUGZMAFuJ8ZjB64M0IKXf_HoyFUTCrv2Zloe1SvVWK0w24aee3yCCK5-gBD17SqmOL6NFMp37YzZ0i2tOo4C9tkg1slQvA1F0uV2Mv8Eu5y_yplWWHVdmbyPyaSeLXlNJKyQBjj55yChmRdhAe-PRTy_wMXCgyoeKXR2NQg5wo4InipSJadSGnzfUC2l_fUpcVbxukxcFth-hjLDE_CSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=hFngk352zfmB2YNVoROthRcEMGbEoWLxBO6lxyCv3JCKWHoO3lfpSZ_VCyb6wuq7SJAgdooHay15MC-Jf9K8HriygFT1yhlx-OEVAEFU_ZqFLTMgs3fwDrTrkj8hf8EwhI7ge5rrE9DVphHug2Im_GTSGLbwBoh3rPqSez29jScZJbkw-NRMFQTKggNnWrbuEzFVry3EwJTcpF66zf3mULUs2UDGnxJ5Y0yRnUcJcEGPJdBphkI58JMGU0t-e5MTozVO9eTRjK22FdCzq_YM1qOwEjpfWUOn5gfThX9DvW99_mkAClzRBJuL9Djxj35guBeIquSGXcLGJyUPAp77RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=hFngk352zfmB2YNVoROthRcEMGbEoWLxBO6lxyCv3JCKWHoO3lfpSZ_VCyb6wuq7SJAgdooHay15MC-Jf9K8HriygFT1yhlx-OEVAEFU_ZqFLTMgs3fwDrTrkj8hf8EwhI7ge5rrE9DVphHug2Im_GTSGLbwBoh3rPqSez29jScZJbkw-NRMFQTKggNnWrbuEzFVry3EwJTcpF66zf3mULUs2UDGnxJ5Y0yRnUcJcEGPJdBphkI58JMGU0t-e5MTozVO9eTRjK22FdCzq_YM1qOwEjpfWUOn5gfThX9DvW99_mkAClzRBJuL9Djxj35guBeIquSGXcLGJyUPAp77RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arjnpsJ5xnsaeMh8VZUga0qPWjna1lZNgCGA3KteIt383c0K0UIJ468YE6bjuCi1sxV8-wuhe-W3IJRSSZTuJl8WDExrcaY7UKQf7W4vkzzyFW1PUsg3z3kQvGjxDd5hjvzDwLkHbgzH3uDvkQO8DIgnCithsrwpjxtDQFfW0R9YxpHw8AZRKcERDYm-pJmnVZQktNmF_Pgt7wOReHdPCZxplea_ppnICoSUYWQICK_DYCt3CLz750uNc0kkDgWnm6ckugaSxhDsgDWLAe7NJjKtJBQ7EmtIb9FcZS87aGVxpGC3VkW9VFj3q5SrjHsA9FkTWYQTizxlrcLuV_AjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU9Sctj167KWL5BeATIl-nk7KxxONOc1wIu5Oev-J3wArbgw7XHrar8bg4kzNYUhKFRV5onWtVYYJcfMlAx-CZiHdA3ty9P_rsZKU2rq8sUbA1wUPzg-TN66JvCOCfnyhIXq4Hwby9Bcnf9S6Jg1-PTZVn9yWa3LF1k7Cac94n8kmuEv4YxX6E8uRN1DfhaJyFkMcKnrGO_lH98agkztuaZ1FvXMconYlpgYLAAnfkmzUnEIabPM3eKTEU0h6wvKRAGwd3wPfqPCyjlFg2SPz3gqaUfARiTnkXfB8z3QoH7v3IncCX8vtvyD9TlYbH2tBGB4yISCul1ayCwzmY_oQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=kEv1J_Iq_XvCiUvR9CWkN4JEXvbkxCZo7LgICvKLa-DEZ3BdhiLupYDSkEavvQ77HjPEKXbnhzIE6arKHOIRzuZyE5RPQiUG8V2VLApgiOgWLvpoVXgPeEuICvp9WWdcSp0sZBMyJYMN8kzLVkgs8yA55v59V_R87yFt6OKHSjr0gKnDkTcUjbHBfqMrhaOPqUNYLVhe22Nm57dzzbTa33rAq10WtpB2HAY2xkriRX9aM37X3rCK_zgnbbhRAHejTlvqCw_CJMTf2t8J_3tzV1Hwx9xerm0qnSk7zT0wilOOq-kBCO-zmnULhkbynrSr7ihLiSfy0VTRiGI_uesRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=kEv1J_Iq_XvCiUvR9CWkN4JEXvbkxCZo7LgICvKLa-DEZ3BdhiLupYDSkEavvQ77HjPEKXbnhzIE6arKHOIRzuZyE5RPQiUG8V2VLApgiOgWLvpoVXgPeEuICvp9WWdcSp0sZBMyJYMN8kzLVkgs8yA55v59V_R87yFt6OKHSjr0gKnDkTcUjbHBfqMrhaOPqUNYLVhe22Nm57dzzbTa33rAq10WtpB2HAY2xkriRX9aM37X3rCK_zgnbbhRAHejTlvqCw_CJMTf2t8J_3tzV1Hwx9xerm0qnSk7zT0wilOOq-kBCO-zmnULhkbynrSr7ihLiSfy0VTRiGI_uesRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LobtDc_3YShnkjUz0Zp-1Hz_gxTikobKfg8bpdfkdlkzwhHaBF-2S7SlU0Ci8Xbjmld_PzsFTSVmewOXBBqsoTtHulgZrMQwmJEzdbau8VHuYC-Nx0-KOeEfvWdOJZ8tZtJ6CT2ybk3tPNh92pVl-eWLaaBeem9V8NbpyzeJHPIUa7Jyedj0keEesKNd3Obxg8Kj3If5jDjwhiC6JM88GQqnJ4pr-boWAqBwMcI5hBL5MqdliBcW82sbkuTTmhFOnxbn03amBg4iVQq5Pv-eTphJY5PSUG6tZearYQjaV3IE8pmAhi9ZMiKKBR0gH6EIHmcLLmjj-rryi589k4ArKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cIYW5qFJ7vC-F0n3c9Tx12DobABqlS2B-LctiiH_TY2Ls-3J_i2qA2N73-BDwro92DHCuMOEAl_oHQRKfkyBAR-g2K3bb5j5VkRKAXgxcRQIyzjWF80jNc8OUrO740Eh-mPUkAOzL_Ym18o0WOZrQvu7IYGtx28eOFsZzdUIZSv_qxW0C17shGSdBbxqX2gQpRA5URubh_HdYrp8D4jPNOXygHZMBwTeZt2FKwTfSQt76rKuv60x-h7ddFvXUXqEc1n7nOwhVFfr7OEaEWQMxqoBdWAFnq189OceT_g63c3YV7FPRVN67JIEARMCvJPVKN8XpM4lqNK6rWZVC7Gmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cIYW5qFJ7vC-F0n3c9Tx12DobABqlS2B-LctiiH_TY2Ls-3J_i2qA2N73-BDwro92DHCuMOEAl_oHQRKfkyBAR-g2K3bb5j5VkRKAXgxcRQIyzjWF80jNc8OUrO740Eh-mPUkAOzL_Ym18o0WOZrQvu7IYGtx28eOFsZzdUIZSv_qxW0C17shGSdBbxqX2gQpRA5URubh_HdYrp8D4jPNOXygHZMBwTeZt2FKwTfSQt76rKuv60x-h7ddFvXUXqEc1n7nOwhVFfr7OEaEWQMxqoBdWAFnq189OceT_g63c3YV7FPRVN67JIEARMCvJPVKN8XpM4lqNK6rWZVC7Gmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiFDIx6SIWVbqqTWdPlEuWDK1EgV9eIIKw5LqkDp1l4UoE0vmb06414c4JIwNcqYOzEu0IEtEiZKyISeI0Ti6qwoDzlI7XhN6Hh_UfrHmGofkqYsVcHdCtSjfAl1fVGZNZ1vxq88BKbDiXhPOmoOfStHm2TIILRtvYOB3GVD7dQuVcfknJf6DoCrZJQ7jFOauv9dfuTFlX6ktm-9nA8QecvsVzVHn9ywBmpZIsRw3ryjUH8ZFlncEG01Hh3JMyvP5fR8G2RVFhryBqtrpe4o7iihLeCjKFOsNuFcUVPGKBNxhPEgHo-a7qVy6f9GczmB5CGuiMQu1dHgX36v63GHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY1i3-zYKbvImSsuNGFBGq8AKs_W3ir6QzGRuRbBdHImZghylSoat-5jMd7IIb7sRnOeqK5nt5sy7MiJjpnYHHEZt5NuvHDkoqpo7Y-7EDSgsMzzn478Pq2VQzv-Uc4soIIvRPuNtxg55Jcag5z4bWtBzu1uaKbgHGdtJ7-h5AR0KBV4XRFWL6H5DhSgBbB1XGvbldcKLNoXEZa-daIueYZf-XJa_c1iwh7hAcD_hgLotEXMsJgg-SDTsrShKBIcEICbNICejQo1ad2hVi3AIcEo587kNv9hxoZm3X8VAWmOD7X4NwFI8BGnFQ6A50i3muXQungJKNB3vcsmkJpBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4niFslqZE0AoBZJ-dmltWAWiO_SCAmrBELRcjebG9bGaF0oA6OXrYPFo-CNaN78SNNUV8c84axNMDp8PdUqqIlUpaq8INLezNLXwJBFw_ohvxcsTnpeaq6l2ptEIG-ZbSrZR73fovMYw0TDb-GdIFxLbqSwgCbhhmAsgVqglFUT6790J0kwhS7nakj9QQRevpdvLWmogh4_W-q3xJ4A6w-ztFWjF6_wXWv72lcE4Vcf15UfRetSzPWYzfXMFGGyq46nRXJL2CRNxgyxv6-1o-L5LPE-v0CcmASgrQfFaRTihQ2NK36FSRRW6SJ9tBCNyCrsOBxqew5BX8wrwnWzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSINzXHWjiXBv9HILfg3vtgiwshkCcL90_R-gn5gS-vQije_M05oDf8vW25PoIQh-CyVJS709L-rusGHbyKOmdeKI3ttAyv8245QQ9LH52NR7DewseTjEf81RP1Qw3TbVMMR1uLlpwT0QEBn2SgqXDXhtocFQVPvOQ1exNWiNc7IbpeE0OnJCGjVJJgRnGKcRONjyhQD_5DB-0zgI_X19Exwe7cMlBM0_BdIC7OKZU4wE6Wr2BP62ZsAaU_3ZHR9-eZj4HqVOFeIUNDAnZB6yrdVky7pr3dNNRDHXO9I4j3_r96yhrhx08u01a51JazoueI4-MVfMwdnbW7n1LffDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwga0J5qoQpDy7fdgNWSFyD6jtgsob4p1o6RLRVe_bbKM2Yv986DG5qn9jPz61nvjgCrHM93CyIQx2qqrhFeA3kHuDdkVgCzoq6W_P4PoIdkr3IDxS2oEf9C1_Qvtl04ut-OvLpHEztSWGRp5B4Z-aGQ1nO_GOh8VSWOARsj-j-qQ4m3YKHAX-w4x56IOvL4Z32lxOjEuWvW5y4SlGng_3C52VGaUc2oNK7pmtaqkiRFqNGTKUfGL6o8bZ1U9WEcXUYlgJReQgjS_RNNMcz0OnVd7i8tF-3dtDgT-glPY03ouPHyzYp-dYH0JNPHU-vDfGBpsOsNnj_BKk5DW-GtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=eo6EHCRmN1aCW6hrHQuwpwe5PQGgLnZt1qedw3S7oT0ojz5kq7zhprrW1HLRQ1oF2Xa_tvWNF5BnKInO-MMqTiwChd3PKyHlJBApW6sJ9QZ02LEctNPRpFI6QoXrZKXZsG3oXJJK90OnVZvcuArkXQgiOPhcNtJajaUAkymVYFOSPkOTDeMef0YLAG3agRhCUm5mQZKdfkgHvLtqkmhbWYRXcjPXNKQqht_vO_2zlTNO1eWodMe0rZ4xrOgIWTFYbU_FFMfQNDnu9pFuq5W6wIb6m9S7hBoYCvLkqGZXwHx6glWlVEdVlvrTHHithv0znOBoVE0ZpztRmbVnY-AJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=eo6EHCRmN1aCW6hrHQuwpwe5PQGgLnZt1qedw3S7oT0ojz5kq7zhprrW1HLRQ1oF2Xa_tvWNF5BnKInO-MMqTiwChd3PKyHlJBApW6sJ9QZ02LEctNPRpFI6QoXrZKXZsG3oXJJK90OnVZvcuArkXQgiOPhcNtJajaUAkymVYFOSPkOTDeMef0YLAG3agRhCUm5mQZKdfkgHvLtqkmhbWYRXcjPXNKQqht_vO_2zlTNO1eWodMe0rZ4xrOgIWTFYbU_FFMfQNDnu9pFuq5W6wIb6m9S7hBoYCvLkqGZXwHx6glWlVEdVlvrTHHithv0znOBoVE0ZpztRmbVnY-AJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vzdzr8sRVwlcSF8HYwFVUM4stRC4_RCE30KFv3NU5NVMIUKZNuK5r-cgCxqtiJCveXaiLpMio9vFtrKAgNnV5Ci0uMR_CtGmI4aUQd3ugDFvosRELLnFddWa1oC_ilIckBmdoX6nEhP_8dpi3Oq2xZ88TGMpPkUT3ClaVlnZMHU6P4gyFvq40yw7Lm7syXkElPolv7LSY8sfgOwrX3DnTJ_KXJfhvbruhD9-61FPGIAMlU8tbEgo-Hynd3xhAcLKPzfzcUfuHWzz0Va4BfwJJ0LH1se7uTfTPDREco8NfwrGDQdKT00gn1mT0JLyAq5-M78aWmLgIcMMVzfnri8TwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSj0rpA15e5FcoNij0jBAhiJOXdVHIXbl03npxCPtAJXD0Vmw69Yte4OgjB0SiQ398eboqsKzemDo_EdZ1CI_KU9WGCz1_KjH6LVkt5OnlfyMGGiMQ4SqILe0ZGsr1nqkmt5DgzsNqGHwMbQktIdK2jILZExRwDCFRkV-mlRIeHMLquqgzQlqp7JqVcmFo3O54udV5JzcD5eRtvzYR3xUI9-pNWD5BBd16Rsh8z5bNrIsoVfesdZAwcYwRikFX-3zA3xzXYKWYbNApYcmanLUq2O0U6rxLK4-HuMJL2BkMphAXpdIq5_IvW3pXeXmk1La0IRKxf1tOjSaErllhtldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YqeaKF7yeLgmIRwApMdWdkDTitcAqJT-TOhvrnNYk6J9i1Mkw_T9LCNrK9_RVLG86JynKmewXklDJlOL4QBcCyYeWQfSoR7lqLyYu48zzEoGfjNkkMQg8U9P0qST_DlSiupbd-WskNAOi3pm7jTxd4mSlpc1tLQvFW6FQ01BwyHrzzDzE-ZEaHXWDX4qWbWxfYxBWY4Xb-pB0wkxxooE_oiQDrGlnu2UEUot8qeREIlsZQifXk5k2wiv3u_DOXbLJhoRhiDDZ92PlXa9PW13p9RdxS50fr2wdHmjkRZyBNZl-JNWyhx1EbjGo4_EjYnFXOxpknCHK8brAYyZR4oUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz-HJF3Kat5cPYpmEV_D_NluR2fPVXwoIz-LJwAnFonKNcj9287vITLZLZifKju0w3IESroWTYQg9hYLbK0OWTbBzfhCywsE9Js6B_pQ_RSw50UAdZSSqjiX7rSdxbXKqubvguwzecLOiOtA6XfgwvQxQS5rdOpydwZpJrB5QPEufeL9rZT_FtixihP9VE0br2GObbvekIvU9hg97ATCE4UTCWYKIbfuSKHSulApLYeCXOvKwYIyF8vDn-tLKXEm4NU8qRR-bcEWi46hyRmN4ngy3RfYbQmJgAAyMpinO02CvtIcoBYXcFjIZkGKOXfQvWoIZJpwGWGobTaPB03bcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-ldibvukZZb1IBL7kkGHX8f8PNuqJafnYBWbk88edfnKCcjAv0fYfU0VIdjVgk_bR4Qe-sE7htvk-YuuMATAaHcRVBKTIWMb0VImqBObyo1dKHYPxiWEZYVC2xY3lKvfqdZH3hsQnpD7pRowQMxhjsI0PrIuKTQlYoKOGb_ddB7JFpUgOyi7fova_RyYAFhOjJeAq9hiDc9njl6fY0LgNKLzTDtPb9_F_u9aAUmB_K0ruzbScONMhzmDxHFKGsS-ys97UixDI46S_dWAxRpuIbpq2BYzgjwIyAovsluiO60s8P0liAmQnvMi7oaOZoeOyrP7BfY63kNaTE4tsBSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjQi4XzsILSDPcYHIosOT2_nRdDJ9TN255bcsqCNOXmrxxIDssipjYjaOCxIlvcJpUywJaNk7PCrLaGShndM3fc8htRAun9wunNn1-CuRD-XFSnSpO9UdTEn272HalQ1uTR_3eBFpYqVNsHbA2GA5MEKRkBTTP1CbVC84UxUcNI8LcJu4syjJTFRjeiYqV9SIcGCmF9uu9kaq3akfHt-JD5mBFw04Fmf9CJ54es1-oHIO5p7N5xlaafYcUns6_53S7hzKmTPRAX8tDdLh6mj91ybES0kb9GqcypNb7aoDKw7hNuqRsA8IiAjnsRQoB3cwu1AgzN6IpyTkv56MriQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=dChs0xs-0oKV6pO_3BTbxH3Y6-kb9BtmUt-EL2UR-_XnbskP9PcTEKUOH5BZjJdoyl5mAiv_Gr9iGQw0oeOAsD53708HfdRqxwXZAVCUPp6um-Gy_pvizb1Ijj8hPifIvw3EE2l8bgcAK9VT5g_2eAOKAH2PcsrKOI8JYd39u_mOFZnkUff2OpMj5XdjjKU0MtDkRYIeotvX51z-ec8wIO56rMBK-7LhTQxHxO0BoGscZBgxdsLBj_FJW_v3VD19hYTXP-od14bqXr38vqYmsXsKbjHXm3TBo0bzRueDYzTNvFtcgRpAQO7Bj9766Fs3mLt8u0V53aUuZenJ1tOYtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=dChs0xs-0oKV6pO_3BTbxH3Y6-kb9BtmUt-EL2UR-_XnbskP9PcTEKUOH5BZjJdoyl5mAiv_Gr9iGQw0oeOAsD53708HfdRqxwXZAVCUPp6um-Gy_pvizb1Ijj8hPifIvw3EE2l8bgcAK9VT5g_2eAOKAH2PcsrKOI8JYd39u_mOFZnkUff2OpMj5XdjjKU0MtDkRYIeotvX51z-ec8wIO56rMBK-7LhTQxHxO0BoGscZBgxdsLBj_FJW_v3VD19hYTXP-od14bqXr38vqYmsXsKbjHXm3TBo0bzRueDYzTNvFtcgRpAQO7Bj9766Fs3mLt8u0V53aUuZenJ1tOYtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQTq5tYL-a3oGIPcWJ-oCMsFoMyd7xGtruYeGynO4f2tplQKfSKQj3lHxbrE9aR_e9l1aGRYKBYDjjHeYBbAEj1uOqYtVoWkMKicJrgIavTuiEfjo5ytYmOndC57FLgVedU0D1kT5Pj9yWR83a7pm-ouG3nZvxOMhBoHzx7jZYUudKPSHjw_HEOmOVj0BE5-MnxPtVwW0OjN7i-sxab9l7YM0aSMGtvLoyP4MMThOLHq-ftuoiUBTZQzHe68yMIey-uEYQSnY6I3GPvkrz_SgMdigz7BfpRG35xFOm-di1QtU5t1jW8R1teSfS1jIh6qceqD5UefeZN8ZqbDh2A-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxSBiR4IIq0byXh1tj9AMYujx8qqdnMVCMDTkBxqCSw2YB_zOnR2mCG1dhg2rSbuTHEqzHbXbFEMpvT4SLf8ZatMTafdDOMU2_lDM2QzB06LAU4cDjVqpjfAeC_f6gju_2UAvoxb_QjD9ysai-HqgCb5oMELymg2m3EvgO0pQ43HPsRv3Y_QQHcwhfRpTEMWGnhT9ZZwuBIoOCDv7UrL56my3Mo2qFMpLSPzaydfxef8x3XsMN2HH0sC0a6W2rDOGC2yDgy33BEg55H51tXnPWhx6G3amlK5wFlUCAeq7mN1xk1twZzTEx-QrdEySWHieQDHgAxLgP95lU6Ve7jOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js3ABVY-oPONw5U58dXW_YY8g9V-mv4Qm-JKSZLVveEyX4Y3O0sSaC0t81sLhCVT4LgCLeceB4BSVIqiznCA3mDZH7Ro3qFXHABsUunAvN4XNVarTXEQ4oP0p9lAS0kWQWDUK2bLZOMT1xCEQDkGCzvCvsviKoZybTQF2B8vZJaULOqmDhkO26Rsp34Ono0HD-2ifdzR8vCYXmIs1HcDXVudaFKU31ynVz0VMRNCOB9W274OpgeJqpXs_QLiH-4ZFWZMFJUkY5tobUOHYUjR6-yNcEAHCP73U2y_IJ5Z6nlGcH4fGYEYCrlAl0Nus2AycAXfKA-curtdA1NOTe_VTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a59E0lTpLxQMTji4Q-W5AVByNlg7jo_o95W8tZjVyEkbOP6ksSUj1uU2Ql-psyijCNMyUx8V-NAbXjsCPZwooI4jio7L9sRromr3qSQ1rxBeAAEGrqC3MVU_KvD1mr2s5HppjJWOz4sOCfFORaRz_SeIPLm-42PMWLc7Fxo5W1pYSzvp8fICY_dbqZhYtzeucDWU-Euk_-kLU4jWCmbdn-dkKAHIBThJV5GaUeMc_4x259ZF8vjqsVwCBz38jd-C2ct-o6AXJIbAJUeJroNEMWDglk_AEymQFcIws4sBiIeifSoy5CvCF7YcDeQo4VlHspA_ZdxIpUuSKT4DaeAtkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=eAJ82KqWkA66Z9OsHRx-IPe3AAlLBcSt-tbJgNDD4MDpW01ZeKl9lQIrPu-5ua0xh46yiFe1rbIjluRBBQNwZlSRpX9MDCGqpo28ck4xyq84lzSHv6vFCNqFIJpaOlj9MdztZ6SFYcheqBXNdf2nS0iBHzyEbRxAMMEBuNONMHbcWq9LsTOAio3gtxxrJS0KhK3qIwL6V0oZPm9-mLGGu25M8a4dKLO1YU53u1TTfKlILkWYNQyUzKhv4ZIR_O_2FCtO5bh1q48i5Zg4SiogNS9b8_NuwjQl00fQB4NIzDEpaFz3xhdvTFEXkOOBKy4giqbtvO2k4HnNgJXnN8NHwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=eAJ82KqWkA66Z9OsHRx-IPe3AAlLBcSt-tbJgNDD4MDpW01ZeKl9lQIrPu-5ua0xh46yiFe1rbIjluRBBQNwZlSRpX9MDCGqpo28ck4xyq84lzSHv6vFCNqFIJpaOlj9MdztZ6SFYcheqBXNdf2nS0iBHzyEbRxAMMEBuNONMHbcWq9LsTOAio3gtxxrJS0KhK3qIwL6V0oZPm9-mLGGu25M8a4dKLO1YU53u1TTfKlILkWYNQyUzKhv4ZIR_O_2FCtO5bh1q48i5Zg4SiogNS9b8_NuwjQl00fQB4NIzDEpaFz3xhdvTFEXkOOBKy4giqbtvO2k4HnNgJXnN8NHwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=Sc20lifCbGwPi36GUuvTX2BiMLQ0KzQtMWlRcJoW7a9ELtHCtqqpWJ91GzkcHtYXAlYfocWpnNWIDZv_VTY1GWmDPNZ0qbhGfCV7MNoii8rM-E8SCXu2xim-fEiwfpwsy-e4uTWCWNQq_5n33ECgDR6cKiL2gADtdu6E8Navzea_5iaFz4jXn7Vd-o4uy0uLjiaYTInme99pSuhTkI__PBhqtew2ZtSi2IGHogwyBDeuGqgdcz97DDHL5fdAVB4ioJpIqYm2D6aY7PxNdZcxlz8TzryrJGHdi8Ju21NRRRU80B5P7OXMwq9Ov-7lA7kSD1w6nTJ8HPdA-H3ZRpVilw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=Sc20lifCbGwPi36GUuvTX2BiMLQ0KzQtMWlRcJoW7a9ELtHCtqqpWJ91GzkcHtYXAlYfocWpnNWIDZv_VTY1GWmDPNZ0qbhGfCV7MNoii8rM-E8SCXu2xim-fEiwfpwsy-e4uTWCWNQq_5n33ECgDR6cKiL2gADtdu6E8Navzea_5iaFz4jXn7Vd-o4uy0uLjiaYTInme99pSuhTkI__PBhqtew2ZtSi2IGHogwyBDeuGqgdcz97DDHL5fdAVB4ioJpIqYm2D6aY7PxNdZcxlz8TzryrJGHdi8Ju21NRRRU80B5P7OXMwq9Ov-7lA7kSD1w6nTJ8HPdA-H3ZRpVilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=iPUQ1etVtispVnk707STgJDT4aUZekxVhE8L95FhMvHGxReT-16Wh8UeyB3X3CbPSfQRcLT_wSjPhlKEXAdUdNToJ4k3bSydgDPc6FfJeZ6W8oiBYDtm9ToGxq5R5wnTEGrVNYahQtS5g31j1BgaiFKpI2CW3MrY-yNoqVxdJgZlSD5rImnFv2rKHEgApvvPngnFBh-oKaDSRGKKRtlyvgUNaJOVJHCjlrDa0Cv92oHBMlxmBk0CE5hk0S688MJNIvHKw2eo9EGvhtXJiWu73Oace5LgYWaqfBV77QoB260wk4-DnPz-4QsPijszKMG9wX0Z1Ja7MuM-TLn671UIow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=iPUQ1etVtispVnk707STgJDT4aUZekxVhE8L95FhMvHGxReT-16Wh8UeyB3X3CbPSfQRcLT_wSjPhlKEXAdUdNToJ4k3bSydgDPc6FfJeZ6W8oiBYDtm9ToGxq5R5wnTEGrVNYahQtS5g31j1BgaiFKpI2CW3MrY-yNoqVxdJgZlSD5rImnFv2rKHEgApvvPngnFBh-oKaDSRGKKRtlyvgUNaJOVJHCjlrDa0Cv92oHBMlxmBk0CE5hk0S688MJNIvHKw2eo9EGvhtXJiWu73Oace5LgYWaqfBV77QoB260wk4-DnPz-4QsPijszKMG9wX0Z1Ja7MuM-TLn671UIow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ups3jeUS71Aj9f56UosWfE1dhWwUa2hdBBSZKG9FVvJPh-yZyY3W6F3Te-aKfWcUmJHbI1XD4MDhHK2Ooan6EQmGFwsapICtBT01Q0RSYAMAgEDOvbvQHoegjsrRlVtBDDeWWp2aJd_A1DdGuV5fESRBScddqQrgcei9o8WM6GiEtVvN9rYsVzj6d5PYoERIPMaKlBUjwFqlbtsdHhyFNKrN9jI3HDDPH5I1ovFvvgfdUkUKwRiW4CzQDROqJs5-KX9BxG5Kaf6oEbqBX4tMwOfcEPKOJGrJ2SMPcy-knot63Ql60hJZC-gQ9D952sihFtUsSpYIsOMgQZcjrrGOyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcDlGsdz5KDEaORS-CeLClx7N7RQrCsmy-rE6x9RzipJP5LqyCnzcWTdA-QAyEzfU12lRPg4TZG0xkidIGXumX10kZKQ514nc7-7oXEVv5dogNS50lUA-7NAR91bzIrqG7Tp8KnwTR5nfDtLEzwQIdmyI9m6P0Xf_4VMBidXBAvgRgd8RwMQly4D5KcremzYxpBSUtmze7BmUpTXHr-Okb2-KQsuvk7JYjw3v-ahpBde5acqak3eFzkZIVwk1y4ppjTWFWi3sbhuH5m6iSBCImteTdYlenhwgq5MfOJLdQj9q3TrdODsadi69qsM1PqgrLBPtHlBDY-zqxVt4U0W9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=kXm1fdWxgCBVNBrTOYtAWlvWJ2_w04jJoENR4CNoTVFS7wKD0g6vA6H29jvflQGyw7KxgJokVgRzQ-gMs8sHD32uY63HURggyNicGI3cQ_1Fy-cNEFaPqoBngPXpMIFxWHlJx8KxOvbik76GRcD8sq9D236hSVxvUGxWmaFojRtSVJacE8PzRADpHQMkl9DdUmCsC0-D1nnCGG0Kh1Q0aSXP6JbPSvxkFWI3Htclfy-ndqqR4QXRp__zArrDBD5j6bCRtLP8LNhjgkmaC3z0XKW-tL1VPVpM_SaBrmWe9H_IZsqBvK2SEUzGiHGaQJHOMFb7xi0uZO889o0cRmLD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=kXm1fdWxgCBVNBrTOYtAWlvWJ2_w04jJoENR4CNoTVFS7wKD0g6vA6H29jvflQGyw7KxgJokVgRzQ-gMs8sHD32uY63HURggyNicGI3cQ_1Fy-cNEFaPqoBngPXpMIFxWHlJx8KxOvbik76GRcD8sq9D236hSVxvUGxWmaFojRtSVJacE8PzRADpHQMkl9DdUmCsC0-D1nnCGG0Kh1Q0aSXP6JbPSvxkFWI3Htclfy-ndqqR4QXRp__zArrDBD5j6bCRtLP8LNhjgkmaC3z0XKW-tL1VPVpM_SaBrmWe9H_IZsqBvK2SEUzGiHGaQJHOMFb7xi0uZO889o0cRmLD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=SFzw1wM8D-gaOk_FhXzObGRZZ8dGGAy1El_p9Ec_cCJryjCChLT-OsHjf4AiNCu4uP7AHniQpFir3RdiFLys9EGs_ExlYWLyM7rsB2oU6rFLic9v7_WKth_z9vdmAQF_QUtivKfpKweqjNCo6bRWBuRYbO04UUdmi2439Swh-hpJb-agO2xFDDfXdJf0F0wGeWgo3a-JT_orRJk49w-3S7ixoab48UmzdqdCeSZuQL-S8FUD-_ldt3fYNXCJD7QvTnfroaQmINW11eOKmQ-hCNRx764D_61KaunQ8yjrwFJcUjfHoQzImpYfDk1Q9IEkEJQsro_xALG157m62iImaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=SFzw1wM8D-gaOk_FhXzObGRZZ8dGGAy1El_p9Ec_cCJryjCChLT-OsHjf4AiNCu4uP7AHniQpFir3RdiFLys9EGs_ExlYWLyM7rsB2oU6rFLic9v7_WKth_z9vdmAQF_QUtivKfpKweqjNCo6bRWBuRYbO04UUdmi2439Swh-hpJb-agO2xFDDfXdJf0F0wGeWgo3a-JT_orRJk49w-3S7ixoab48UmzdqdCeSZuQL-S8FUD-_ldt3fYNXCJD7QvTnfroaQmINW11eOKmQ-hCNRx764D_61KaunQ8yjrwFJcUjfHoQzImpYfDk1Q9IEkEJQsro_xALG157m62iImaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFH-dC2mdp-NSH18BBJaSKM-5070HNvcxsqJCg1CtmlW9YYYX40tJdPUugCvYkWJY-h2o-MIzFRijE-sMeBqdT2r_CkP1frelqM56-ZS2oQIj0S3F2ALaBSIyvB6BoZmzZUrcjdewBXXvf6qJFASn4D7kR3ylfSZNK_ehibDYy65xjbhvIKRSfWn-dNbZ4gsNncOb0OvqsaKy_6G_fdFUBPwGsL5Rl3Iwpzogfs4ZG7hfTAPY2joe9_aED87ejNnsV-UGclbKxzs3dIJ-2MSbv31zDRk-gRHPGBSaouHgaIL8_5Yqrq8pfotXuLhrwCtcJ2o9jMPQqITGil8cEW2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMibz0Z59cKBBDn8eJWfRwlll_mPl3LhWsvrZFwiEU7al81H7QIllinY_Nig-DR5kx1kz11_Xh6lF9UgGfvTZZQFrp6dwH4gc27nh2-nuawaieISdKcHpyPRzDvQyhIpVigymDP37aIj01n3mK5auqWnIcjXG3RaqZqLJMMEq-JHty4lxdPSAy4OE84R6z2X06RngCwLD3Bn2Ix6iRkQF1uZdYXslRseerMh6fSaKkL19NwP2owiz_1p8mTlfTplBxPLYcxbJbUa5t1K2lH0VZsMUI-lHFUqdi5glIydHQDK0AXVELe6I8xqs1psWF-lg969UZTN_OmQ0L86Ran6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvUApNFec9Pb8vvBZ5v2G_mlGXVNx4cpkMzS9yUUnKdiP3tjNfPNFdPQrhN8Mhfyt6NsjHq_x2prUWpRqLSS9npz8UbKTKer_9KAtFrWWxL5TsIUC8Hg7vkw5Odkoe36Rdbru3r2WBHSZsK-W7yuQscKks-cbiAUbUBIh5vDouVZRDTIx8sYuzmSeo4RHcNESgvhhKjCAlBcfZbTOINtTvA9vKGMOuOYs0D0TZtJ6gtYeFvxGiSqdS8wXIWqTnn1xbwoL0GatoNgVWtRC5nVTXGUQoIs4_xsXM-v5Wf0xwOnGjYLUeOUgnpSfjb7nk5t7q6iAlZWAZi2mkcMezrtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=AmsYTH0n5o-TEYDweGcHc98mpYKIlyYzGRz2bo0d2TU4yVoWLwJO5872hG3zUc1Lxhz28luzK9sUMHAYwyH6E3vOuZniqHbK2xV63oGoB2WPwatSX2F2bpeQdmnMi9KsfB8C3paWo9aseyKwn-3kN4VZOnyA1LS1rVkTZ820N9_l0yyt9XQB4Zk1ISLN4lxJgaa2LJaGS5NZLlHMiW42P6d5ksTBysJ_ZjfE3zIqRRNpDJe-XOmv3HUDmag1-tFNjTwMLoCf_GBQ3NE6VK-48UKn1lyv7RLri7_b48_8xpINY96UH4uHUziz74STqPbxdQhhswKCdY2fN83ksEgI-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=AmsYTH0n5o-TEYDweGcHc98mpYKIlyYzGRz2bo0d2TU4yVoWLwJO5872hG3zUc1Lxhz28luzK9sUMHAYwyH6E3vOuZniqHbK2xV63oGoB2WPwatSX2F2bpeQdmnMi9KsfB8C3paWo9aseyKwn-3kN4VZOnyA1LS1rVkTZ820N9_l0yyt9XQB4Zk1ISLN4lxJgaa2LJaGS5NZLlHMiW42P6d5ksTBysJ_ZjfE3zIqRRNpDJe-XOmv3HUDmag1-tFNjTwMLoCf_GBQ3NE6VK-48UKn1lyv7RLri7_b48_8xpINY96UH4uHUziz74STqPbxdQhhswKCdY2fN83ksEgI-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=oR5R55z0A7QdVGHZy1RKfccx5WvjsYrgmA15VeuYwL6eZQ7xwSHksj-gnFR_64RUXv4LDo-K8GuxrRJXZAev4Nl-TstNZO1gYa85tTh4Vz2VZtlOouBYl2te0_lU0cnlZpQUr6z178oFYjLUAD6IP3R9sCy0THrO09fMKaYhUUojQsUONDmOOf2C-2ZF6YDERuq4oaQ8DOlQ3UtQXB2tPEVfT_DiErNlGxgTi-Ii-W-trofISsXbdDZJc1i4BUQk4eiUKga176hCOZRY3KwMtotW5xzVdBVx2C6KSebcS968N5_CWnJJ2HBHEWGFsFs02fz_yigoss9FlqS40I4lOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=oR5R55z0A7QdVGHZy1RKfccx5WvjsYrgmA15VeuYwL6eZQ7xwSHksj-gnFR_64RUXv4LDo-K8GuxrRJXZAev4Nl-TstNZO1gYa85tTh4Vz2VZtlOouBYl2te0_lU0cnlZpQUr6z178oFYjLUAD6IP3R9sCy0THrO09fMKaYhUUojQsUONDmOOf2C-2ZF6YDERuq4oaQ8DOlQ3UtQXB2tPEVfT_DiErNlGxgTi-Ii-W-trofISsXbdDZJc1i4BUQk4eiUKga176hCOZRY3KwMtotW5xzVdBVx2C6KSebcS968N5_CWnJJ2HBHEWGFsFs02fz_yigoss9FlqS40I4lOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=TA-UBGcc9Un08YXpAnECPhnXIPPZU108LjuBUCJDAOUx-MhLZ4r3bDUYFvgxR_AuC-f90OQH5OFskKsTJm_G_hCNG86WMfr3oAxRU3nOhDu3jI3wDX8CIllHnDlJT0Uhbvt_g3USUaRXii-9t75-sIBUVkYgQC-Ky9wrcQzDfZbdXFWVhayV2B909O1_3pQxez98RSMbbE8mA-L6RkcojyYQjBsz--jKuoBmF2iXBVuK_PkpmBc2yMVZzm4aqnijWmi00d3gJ_UZ6-aKbWj4KKQ0XdM6sio9xMDuzXbTlMsBAR0X18OuLl47koVQ31_3gLV5KHT2ZIJRrDnMohPcjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=TA-UBGcc9Un08YXpAnECPhnXIPPZU108LjuBUCJDAOUx-MhLZ4r3bDUYFvgxR_AuC-f90OQH5OFskKsTJm_G_hCNG86WMfr3oAxRU3nOhDu3jI3wDX8CIllHnDlJT0Uhbvt_g3USUaRXii-9t75-sIBUVkYgQC-Ky9wrcQzDfZbdXFWVhayV2B909O1_3pQxez98RSMbbE8mA-L6RkcojyYQjBsz--jKuoBmF2iXBVuK_PkpmBc2yMVZzm4aqnijWmi00d3gJ_UZ6-aKbWj4KKQ0XdM6sio9xMDuzXbTlMsBAR0X18OuLl47koVQ31_3gLV5KHT2ZIJRrDnMohPcjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=WYJ6FwVPOnHqmjXJGPmcvH6L5TCt_1IsncwtzPjhWNxIRwFqWScOKJRD4pazZZFO6q1hRmwjd4NQYe55tocdohN2145lcP9pKN-l0cDJkOl0TE9NnbHFQ3pbC8wOHTZaEG75Qp7TuR2jvQXQgwXZ8QyGKEIPPJKgHqhvvPn5WtMmJIJIoQk90bayNeKT8fxcR1YglOzS9uukkS85l1noVbqrnr0NdgH7YfB_FOGIjuijEr-DzXSG0JO9oh_u2_bo_EcwRaYfAfL7_Z8f8U3Dze_RDecWiDr00-tXR1Oz822eAnG8R07iNdF8Pyqd9ZgBZxbwtCN40pYu5U4MR2bsTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=WYJ6FwVPOnHqmjXJGPmcvH6L5TCt_1IsncwtzPjhWNxIRwFqWScOKJRD4pazZZFO6q1hRmwjd4NQYe55tocdohN2145lcP9pKN-l0cDJkOl0TE9NnbHFQ3pbC8wOHTZaEG75Qp7TuR2jvQXQgwXZ8QyGKEIPPJKgHqhvvPn5WtMmJIJIoQk90bayNeKT8fxcR1YglOzS9uukkS85l1noVbqrnr0NdgH7YfB_FOGIjuijEr-DzXSG0JO9oh_u2_bo_EcwRaYfAfL7_Z8f8U3Dze_RDecWiDr00-tXR1Oz822eAnG8R07iNdF8Pyqd9ZgBZxbwtCN40pYu5U4MR2bsTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1512ymNhttVPtkrIMeUuRBjnMbqGn9iKBm9qzrQU2-KdQjWi5TlJqXReof48TEQAScQCCsMsJ0yznTUJ8McZoS527TQHnBHs0TYWXgSDrtVHrq7F0DAXRHYEKBDTRPQ8Uqbnw8hqPhhbe6lmxU0cHXl-OISiGhhTxB3foHkPlgGVvgtAFE-pY64aPT8cKwWmjN_18X1r4VpQZooJ1ue8mjlMmjYTw2wJMrFChpw_T-7Obd-vc8ODXMz_ziju58I0-fJX1EfrCZn5pkn_CNYJzYvAl8AbtF1uMeKjc6sx6mqXssbW82bwiNNOd8VzBrleASUyo_4wPy2SXP33AQ9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=BMI8ErC1GjBeO4dRN9WTFctF8Gs8AkhQUNPayie3fzfh0tldE4wjGvteig8TzUrmBpGiNJaoH5qyWofixxYv_EaI3f6l15hN7G62SnoSjtT-QXx38rtoSZKytLIkAODsLedXUHC6XDHrGDO3fXIgLFAk4LVTnNzFBzUBl_X2GnBdHtMtyEMC7Z5_q3JBIjqBpdbb6LiFcdilKcH3GDNUjVVcvZNE2ZNANMTIGTEK_xdFJJ7FtD9S_sMWrAi4FkCalE_hqut6othN-itH568dcvwTH_k5f51OOq2Z2Zx4l6sj4niKraf85pTT8CZOqTgpBgoAu8HEQt-HrCmKNlxUjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=BMI8ErC1GjBeO4dRN9WTFctF8Gs8AkhQUNPayie3fzfh0tldE4wjGvteig8TzUrmBpGiNJaoH5qyWofixxYv_EaI3f6l15hN7G62SnoSjtT-QXx38rtoSZKytLIkAODsLedXUHC6XDHrGDO3fXIgLFAk4LVTnNzFBzUBl_X2GnBdHtMtyEMC7Z5_q3JBIjqBpdbb6LiFcdilKcH3GDNUjVVcvZNE2ZNANMTIGTEK_xdFJJ7FtD9S_sMWrAi4FkCalE_hqut6othN-itH568dcvwTH_k5f51OOq2Z2Zx4l6sj4niKraf85pTT8CZOqTgpBgoAu8HEQt-HrCmKNlxUjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vH3TRemxtoms-aUFifMFiJSGszjmIEeypu7CtHrTuWzfWyV6la3p3FgExgmKQ9rwL1iovhGUr-z9OvOTG4cXjt-QZmgJS14o9DbLtgnt3V83gZacNePJYWUWvP9PAcfOfZ_oUF4nZi-Eh_a-1BEUMCCsxSdV5u0JfuSqjJRVvja415Z0v62IstygWGUXlQ_ptYScoXOgLl4f5J8ByI2mYhDkONCXkF5WSfftH6gMOe_sX1yQWr6jdxCAk_ljk9OmE5B935oQO-aYm-mYfZ31FkmzGer81uZBYwMh51iBUCofIMCIGkI4-N58h0rzjl8uMr8xAPQDOy3xtoBdwd2sAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIdzs4CQQ-Lq2QAMjWuxiFY3SFOulHaC8glTRos0FoD4ZZZfG0-hDS0B0b3aL4b4heN9suW6Or7mnRH9orjh4G8DC7OE970BrY3WlTc5dcjUIVyAOkUTqaOwNuBfXW6wQHZjpqkTEPzz94TRZLJv0057csdlwwyYzeGfPxLj-_TdSP-B1k7VmhfErr0Ag9CERkuSpg1VSb9W_g4OSLvGihtLF0PxUK20TOugfsqvpoBLVt4V8F-wytUie_9r4LNdl6XsEMGOJHG-wfqZwn-CM4Q9K9BCqOXL1J0aNwI0kwO6BwVhouPPd73Nyo87DejMLuKdPFgwAk7e8NmTafdURQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP6p6lckst4SmISk_ce6doi7qxdsC3UBxFrUsfZKs2FdTqpehqFGdb4yTRtu3ipDDno0t9jmoe8xSwGN7zPpGTyxbZXibu4MkxqNxMnPnAXbfRpmsrh-T99nlPR10e3vSGIzOvloHsmQrjkhDMeaLwovJDGnckNHEu7C3ye7wg8oyv4i7a19QNRJfIN73YAvX4kE7Iz3hlRn6ByOVladHvVECgTVVZPEw8ItuFeBM98v4UpbtYZZ4Hg-xRirA45N3f5mV0eBKN4C6jr6XYXPv-xqG3PrT3j5-NH-XStZa3zfcm5KD35E8TRQ3gVmAsJzKWdrVjxVN1JVN2Xs6rMvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIR2aTi1y2wicR1w6isGEo6jesmUCBYF_FeZo9vybV93BKzPpeMIXnu6_v9gtOqI17VnIAMenA9KS_xQV4RX9WA5cyu6u5NCfYBOFRaPWC-nz8jbaXkX_1VtLbNjiN-SLXsTJ56lCtJiW8Cp2DChNvBBbCnqd53nBakgsgoBC7daqThWVmYQtM_h44Sstuu7ik2tcvxe7kDf1BhUtkLD6qecNzKPkZrxFTOECmZDtSDIRPz-K1xULSJk1ha_QEnjGpH5qusqKBFbtw3r-gkXXFqxCWSD7QjXlTu6p-GT761nljNgoWyVQgQOojHaC5l4n4dU0TwH5WLswltK4CVOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=nl0mykkAtZT4dacvLy7lfTDSFiQFZxpFNqZjBboOExLbOqMQ0wvDMDLn3W3JmOGr-0sopw0hhApa7TJdim-0r9IENtqu51llHI7AObwoSIihH1LFF3923OGo2fyVCi_4ao1oF_XxWpK8vMGh4M-2_sBisi0jhbGuwfwJPxY6B5OgRD3K2pFQGr9xvMLmoteyCiZqaKCvyg0A0B0OP_heVm1cO9KevCevXMHEYB6O7WM_-BJa5tkgSuK-pAGu-pVXWA72gdBCZBhCc3zxm4RPfHoNO-sZoUS5VS6DOwZvGeXMPCN921yWI64s6vszsm-5rFK4BvQ8b2nsGdjZ-NpNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=nl0mykkAtZT4dacvLy7lfTDSFiQFZxpFNqZjBboOExLbOqMQ0wvDMDLn3W3JmOGr-0sopw0hhApa7TJdim-0r9IENtqu51llHI7AObwoSIihH1LFF3923OGo2fyVCi_4ao1oF_XxWpK8vMGh4M-2_sBisi0jhbGuwfwJPxY6B5OgRD3K2pFQGr9xvMLmoteyCiZqaKCvyg0A0B0OP_heVm1cO9KevCevXMHEYB6O7WM_-BJa5tkgSuK-pAGu-pVXWA72gdBCZBhCc3zxm4RPfHoNO-sZoUS5VS6DOwZvGeXMPCN921yWI64s6vszsm-5rFK4BvQ8b2nsGdjZ-NpNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=JdjJFl23TOCHAfcCGzcjvEFv1kcWdos9mnH2Yunpmn4KFWUb3Cc-vfPZw1NLu3iX2OxqLlUdZQeyo7MjFMlOwXWUvAFQh_hc2Tq7l7FWulLMdVMckozmYesdQtK8oAI515Tbn7mefymlUaVJJPwtDXkx2WUNC7K64STZ4H3tynASn05mR3v__2CLY8MDomYOEo6kDeIU5Ex_ipKNJ3hA7CIHohUhZKgs25jCqLvmN3P3S2vszSn_m1jiMne9Wbq1BAwLNcHoNRHrWqSZzXE0FERvsLYDzXLtGqhAWZM10bXzcR38RcXmM9-AYcSEYyEiy1X33gv-Na-Jdbt8SXvKG3yr_CEuY2lvjp3paeOEXTDM1b2qY6iHjoI-IJZHzOhNL3NSy2945iYe_ok50rSc7qCU-zMnfYOBLOaLO1CR9yHhdcAFMcAVWpLGAUcPDAQotM7LMPK5pu0HEpuFpR0HzID-a80oSqlSfl2CFr1CzqO31TbbjlC8_HJdG5FihoHMLXyTpIG9n_l_N4JNJImRI2zhSvyDpMjL8VMyBGGkSr0HC4g1q5d9rJT549KkHagWK7LBoZIaR2tRe4Dlqbm_X4H4RLznL3mkL2JAPx10ZOvWr9u8aar-l2mOgMXIne3s6n4-q81a9o6Swewhw9JrLJJZZ3vrKnYLuozrVhiT7TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=JdjJFl23TOCHAfcCGzcjvEFv1kcWdos9mnH2Yunpmn4KFWUb3Cc-vfPZw1NLu3iX2OxqLlUdZQeyo7MjFMlOwXWUvAFQh_hc2Tq7l7FWulLMdVMckozmYesdQtK8oAI515Tbn7mefymlUaVJJPwtDXkx2WUNC7K64STZ4H3tynASn05mR3v__2CLY8MDomYOEo6kDeIU5Ex_ipKNJ3hA7CIHohUhZKgs25jCqLvmN3P3S2vszSn_m1jiMne9Wbq1BAwLNcHoNRHrWqSZzXE0FERvsLYDzXLtGqhAWZM10bXzcR38RcXmM9-AYcSEYyEiy1X33gv-Na-Jdbt8SXvKG3yr_CEuY2lvjp3paeOEXTDM1b2qY6iHjoI-IJZHzOhNL3NSy2945iYe_ok50rSc7qCU-zMnfYOBLOaLO1CR9yHhdcAFMcAVWpLGAUcPDAQotM7LMPK5pu0HEpuFpR0HzID-a80oSqlSfl2CFr1CzqO31TbbjlC8_HJdG5FihoHMLXyTpIG9n_l_N4JNJImRI2zhSvyDpMjL8VMyBGGkSr0HC4g1q5d9rJT549KkHagWK7LBoZIaR2tRe4Dlqbm_X4H4RLznL3mkL2JAPx10ZOvWr9u8aar-l2mOgMXIne3s6n4-q81a9o6Swewhw9JrLJJZZ3vrKnYLuozrVhiT7TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=ROPsGKTcCzDqP2bMYJOUuYwNSZsEHpZuwPumLggKWTNFZVJ2TlMbZhqsf6ugoFqBrtEZhw4qDDGHrP-fNhYnrkWbRVjgTGyTM3-gRbTUNk74q0fecLcuBG8jnOrqY9sUlZOUjJUBZkvJcXuIsGpM2x_3ZxShTj_BSr53GM3_r6irUoX7XX9HT4R4t0TFUuSi25Tknhq8pnb3DN577ld1xB3DTFeMQMEUg1EGrmp6f6dxyG0zU2ec5kgbUduAPiuVP6kgPvApurhsV4BvO_ecw9-HUkTSlq6b8xqOmETWJvnoeWQBFEJoiz7WbP2dtIeeyFmkaOaBSM_pi_jk7FwC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=ROPsGKTcCzDqP2bMYJOUuYwNSZsEHpZuwPumLggKWTNFZVJ2TlMbZhqsf6ugoFqBrtEZhw4qDDGHrP-fNhYnrkWbRVjgTGyTM3-gRbTUNk74q0fecLcuBG8jnOrqY9sUlZOUjJUBZkvJcXuIsGpM2x_3ZxShTj_BSr53GM3_r6irUoX7XX9HT4R4t0TFUuSi25Tknhq8pnb3DN577ld1xB3DTFeMQMEUg1EGrmp6f6dxyG0zU2ec5kgbUduAPiuVP6kgPvApurhsV4BvO_ecw9-HUkTSlq6b8xqOmETWJvnoeWQBFEJoiz7WbP2dtIeeyFmkaOaBSM_pi_jk7FwC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=Xnlxw8Q9X8CEsultiEHS3j1WVTWKEgo2GsAtkHsSDtIl-c5wpqcVsmOuK195Lt8__0ihwNQjdZjGbr26Ixvp-bnqgTMuY7uVE_JnwHB2gzsLycdPNLD-4KK8ie7zT13GeU9UwVd_S_Cjp0s8O6b3ZvI1pof7FIgoVBYv2HHVXEsmqKX3rkGBYbI5aYQi_osU2Uo5JHArOqNRNYJjy-IYrl8ghYKE4A_QZbqcGYBrgophNlWz_bfa_Al0iR6qva07jgSmhINQCIJGwHFA5d5KVF35jw663AnxyO9HTEAl-5rOZXryxcN784BYhm4vEKJkiHAbtZirJz0BN4IEObICtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=Xnlxw8Q9X8CEsultiEHS3j1WVTWKEgo2GsAtkHsSDtIl-c5wpqcVsmOuK195Lt8__0ihwNQjdZjGbr26Ixvp-bnqgTMuY7uVE_JnwHB2gzsLycdPNLD-4KK8ie7zT13GeU9UwVd_S_Cjp0s8O6b3ZvI1pof7FIgoVBYv2HHVXEsmqKX3rkGBYbI5aYQi_osU2Uo5JHArOqNRNYJjy-IYrl8ghYKE4A_QZbqcGYBrgophNlWz_bfa_Al0iR6qva07jgSmhINQCIJGwHFA5d5KVF35jw663AnxyO9HTEAl-5rOZXryxcN784BYhm4vEKJkiHAbtZirJz0BN4IEObICtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VH8y_h_FyjCZ31bWc-ECilFRNyn43zNvrE5vJaO1B06N990t6kjmdsN4WUcfjQooZ8AieGrfxpuL875MBD403sqBHwHBS3Wm55a4W8Gzoz0QA3_NDvmZsyV2Euw29e6LOsOz1n3W6ey7c3ijvFfgmLdzlzxUWhWN2Seqv0LuvbizC4yXHtas3XfpuydSYTE9o4717ByVV4r1gAjMqOc6JfYdjH8nx6z7eQgupn4Xcyz3aNWdTH3iXckS1WuVT1uh7vHUJThbfGj6w-9TvUVvA8VGyw4wWKXpU-WJfKOcQYTFkQe0hhZldWRqtYcEIFpd_EkxrDlnqgeKwOaFS337og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQtnKYlrPWn0L9FFm-lgzIlwiEWIW2VT1UeLPYBr0Bbvq5fVRb8H_azpWsttE6HeU94RSzgG65NOMEiQjA5c9h-dv_9aM3d2J_0FReY6TW9vo2PDMN6InIoT_ohlId6J3DQDRkO3eiPf-HBV1QAlz44nt5bMxcnsG6oDmPHRf5hoLOuYwGBX3ZmH66He9dLPEt5w2CJwoFCbMmal1loHEzwagQCeZPhqB-uscHlLnzPwxoyJsc2l8qawd7yI_Yx2ECAjJLu1B4kinQFm3oU0Bdb8hcPApUloNdA1Ifa_Qyvz_BBXEI6y14dk_z4x06vrTDvChG1kOM2tV0rxX4akzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_JrT68t4CFFq3NVLKcFv3hOPYGE5_aEheQBox81TOPbhXSY5x2wfUBlj5Mm7pQiFwDu8DDaVnGevp6RdEzuJy9dEFiqWRr7-ZBvb07AYgTsMeKKl8K3ApU9D_HOygTKXbNP98LAMZlnJCHdRmK1x1B3giKhZeg8bREzxJqBt4-VEViDWIaXNbAGfJAlKa3ywLu8gLBfjjGEpI2W3BP8dNNjr0xU3dmhqFCQEvEuZ5hZQ-wsCnrcxAJYSCVZqettuG_XYpnqNAhCeJfyjWZw6Moc2SQjpDfyAAiGiuO0iktJleW3K-1dFk1oTZwVP5IhlocVv5JBP4O0E9jaEqb_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ms1pNphb-gubAXL6kIMf7npKYVuGPXZ_6IchkktLFobl-NTC-G25Y_vrge4UEHs58Le_tjTscb6xuILY6Xw9lqWm7lvoNJX1oJ4t1GNhnE2kF61mJDV2YVa9TGS3dKciYcUmbPEq0GEYJaldVblRNMZQf-WL6ogQyyAPHjtRLIBWABFlssO1BXsqHglD7BTVJOK3Wnq4KFUZD6yZq7CikwE07MCld6U7uz39kpJfVqVlZPV3hbqG7Yc5p4IKBDqnTJ-TALZVni2EQpYf5YuraqXsXmcXDiyHDPPGmYWu7pTYahc5c7O0X2EZp9e4bCeuDyP7Nls7R9ueeqQj5dxLuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZIHzGLbuLfXwmCIFGNILPB45ZUd6cwv7yTacnsgqragP67DDobZR684uyn7wzojxDqvBd3Hh9nGteUpxTvXnLNwFYZvTsT5U9fI858nQrzFP8s0Oe5qNv5GCcBi65b3LOhLSQVtYbVWrRA7Ly1gm6GIz3NP2JMyKKzSC3SeIFr0Nmcezaadyj0ECU0mPVN7mAcUmHvBL5uZ1Jtkq7Ank1yPMql77IbrSWAr7dgW85T6Gu_K2mAklAEINtFGzQwdJ_O3DfJHPjT1Efmb9pKc09Nfbv8615mn1xNysSkO6dVMPDV4QdirNMcewK3kFuTs8rhmvyobHe8uoj3ij27pIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqiOOmvtbcK26p5z6rrfT8SQDaAy6jtey-GehHWWWuYCsLBQWxLT4rMWRezuTZVnikjGQeNGWzNX6K25flNlH5I3FTwU4dr52WZsFiw1fdpwSaZFvxCdz42zSnjtWP4iy9wJd8eMJpZnewVIGE_EPaOIWy9DDTKomzZbJOdSHtXblCEhXpdjFjRTa2I1SQQ-eLoMmUQduGDIMKqPQeiFxC6w0ckPSc-yzS2WxB4xWGbEt1gbFSWsb7EEIJdZkF9PACwDDACKaNJBJIjaPw4dtDlou3avrkTJAE4JGmKD7O_7l6pfF29ehciaqA-V9BUZMAzyjyisDruBvoahsRvRtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhVqD2_tFyLIDsaJCxVwhOgfsjJ8KWOXZOMuEsLOg6CuWKaVwUwp28uey9W2ydrn6W68dGrJn9x2NAUm4iVFrCPh0aFYEw2WxPloQJS-AmEhD40ozxPJF4P1G1XaOv7MnJTmpNwiyVknh3UrihHiO2aXrSKb0ysn407X2VZ4ycTtRMX4vpKUw63AZ6kfs2S3lRloMVdrNmzgYhV8Xm_bfkBM7cfjmUU-2A3UqaWmM-g3JODMUSu8xwjl0IVMm1um4JLqCt5cU7SGSypQY6sR7npbSmsSt8HpL6gGyxraR9Zxx241erlbJqLzdfclgueS7mji8SwkxLc-yrlSYylS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcOJCtsxlwIZnuD0uV89IVjDANrSDjDotcYOmAMVUZhhKSSbygq7Gmi7Ak2e3iwEtGffUPw5Pl8__fchHmBrhvYDkCGDxQbqrcCu49P1xNSHw68MaYqhiqeVoTt-hAf1Fo0xdo5tmAYntohuoBTs-yemi6LgCJegKmGFYiVMFX1eGl3hjfrrrpLuBUq_e80gHWWfO__cPBxWpB-c1ExJHzwLUgRa5nctuqSpG1Xjp2HdE37w1xBiXTS81C5ze1PoKy-70w13i5am087q4_XxQZ-KaN1DRdYdjTKi7xYjOF26ifsyH7ragZwvSwymgvVvRlJ_0bjKv5WmBVSIWNPMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=Jtz5sXrsTdh561jFSK8Fos_3vjNWr1H5RcBmeMDKnqeyAVN2rVGwsuKHa7GMF71sVGvW6ChWQBz5RXqNGjUT_XcRXALBQ3P4ePm1lM-yed9Cy-Dsf78kgQaml54kgft2bPbXXD0ydBNS3CCezvmoMuMkqfQ_DDWLzZl7ZkagYbAACxTV2ET9GbiYUD7-itMH4BDMDT_2suT5mSkV77EjbHgsrz1UQKN6kJpHKRaRnlXUSz_eafK34jR-GUyqE9hUY1R52qNGKavhNJYnaKR2W7EMuEz2wvab5338CKjjjC6FZr42gXou-E02DqlvZLcG7KKyNA5KF0EbXiNpXJLiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=Jtz5sXrsTdh561jFSK8Fos_3vjNWr1H5RcBmeMDKnqeyAVN2rVGwsuKHa7GMF71sVGvW6ChWQBz5RXqNGjUT_XcRXALBQ3P4ePm1lM-yed9Cy-Dsf78kgQaml54kgft2bPbXXD0ydBNS3CCezvmoMuMkqfQ_DDWLzZl7ZkagYbAACxTV2ET9GbiYUD7-itMH4BDMDT_2suT5mSkV77EjbHgsrz1UQKN6kJpHKRaRnlXUSz_eafK34jR-GUyqE9hUY1R52qNGKavhNJYnaKR2W7EMuEz2wvab5338CKjjjC6FZr42gXou-E02DqlvZLcG7KKyNA5KF0EbXiNpXJLiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=MnlKDWs7yU0jRb97mj3jEQZkwiyXbsdgKR2c_-KfP8cJVMNe1-0WZIK3-IujxOk9Xfut5b0goDyuxCHFE5SeEfTVSqXUW1DSLzV_-EZ-Ef-_N6YdnaEoCHxz5opzIvNV19KHMiPNusz6tzb3jxCCTRH4JGtLRhgzH7oMcM1_loUA9GV46wjFv8GyZFJBe48xyIdz3x_mmm2X5q6yjONxLJhruCu1cxGtZ9SAs8V6Vt7xDw3_JY5GrCZE_uMuif-Xt7GnqzCMuEBld715nzREU_L4_MguLwdfvGIBeOyDj2gra2p4-F2TqgXC2yUk3TRhopOrLFgjPKTxabtIR9SbCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=MnlKDWs7yU0jRb97mj3jEQZkwiyXbsdgKR2c_-KfP8cJVMNe1-0WZIK3-IujxOk9Xfut5b0goDyuxCHFE5SeEfTVSqXUW1DSLzV_-EZ-Ef-_N6YdnaEoCHxz5opzIvNV19KHMiPNusz6tzb3jxCCTRH4JGtLRhgzH7oMcM1_loUA9GV46wjFv8GyZFJBe48xyIdz3x_mmm2X5q6yjONxLJhruCu1cxGtZ9SAs8V6Vt7xDw3_JY5GrCZE_uMuif-Xt7GnqzCMuEBld715nzREU_L4_MguLwdfvGIBeOyDj2gra2p4-F2TqgXC2yUk3TRhopOrLFgjPKTxabtIR9SbCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyrSNvKo9NsXBxjfjvbuptYej0dsO3olBv0Zh1KQbNrd9_fUNykxyYBsDV9rFIExNeU-YPRQ2EmRQXzH6CsVRycXqRzS_oATcjpBI4e4DmiGeLaLI_un0Vx6FnkooZGW9VCjrMxNew8NlRVgeGCpjbnrv768JZo3Y3pzQl8-vG8nZtdqyLzV-Q-dTMduf7YQLmF98Y2G251fpEA9JMkaia1MayhpWK0h8b_9vHcD0sUjgc6fGSZ_OJCTbbJo7uIg89lMIf7s7MMVwvGhy_MtR9eSj2PeW_5gLB4db9aRcPEBh87dYHHsOMz-RozPqfcNwkDdqY5otDeEXCJpj9MOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=QFhJimGq93Ef5NYDR4bKAIn1fYKLbzFWZkRY6NWGNR1YuoHmbIH-Y1juKYu9fXqC3WrBeZ-UxHO2q3dduHFaoSRG4NVbMCs0LwGMcs1DNG6pEXIKHEPwUIK35gqZjqGNNtfNlupNN7m631GTLNiUuUZ3OvVVzqzOaachDndPfHFtEtY0HjiRV5byMjSOtTiwm_nMInCsqmZ72lx4eETtofMo0s7JI3GhGIyCL7b0KocBrH2ruQam2GUd-sB-tr6SDkBWnbQajiBbbPkgqZG79Loh3x9a7c8ssyqUZYvOj1k5KwwSF14I9CRTMUhWHPnN-nf2xr95eSMIEDsLSkJVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=QFhJimGq93Ef5NYDR4bKAIn1fYKLbzFWZkRY6NWGNR1YuoHmbIH-Y1juKYu9fXqC3WrBeZ-UxHO2q3dduHFaoSRG4NVbMCs0LwGMcs1DNG6pEXIKHEPwUIK35gqZjqGNNtfNlupNN7m631GTLNiUuUZ3OvVVzqzOaachDndPfHFtEtY0HjiRV5byMjSOtTiwm_nMInCsqmZ72lx4eETtofMo0s7JI3GhGIyCL7b0KocBrH2ruQam2GUd-sB-tr6SDkBWnbQajiBbbPkgqZG79Loh3x9a7c8ssyqUZYvOj1k5KwwSF14I9CRTMUhWHPnN-nf2xr95eSMIEDsLSkJVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
