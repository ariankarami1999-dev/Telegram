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
<img src="https://cdn4.telesco.pe/file/fbIiqgv3pg1s4j9uWSr-UFKnstlmQ3nlvj6AUWjMygjYexED5GJwlY6nRr5in-gFmaFyBZUaJyRAAjRCcHLVcrA_aw-Uk0iRMNGNK-GRYvMKxb7zk8z6yCmiWldVHbAQZZgEPYX7DZ2Vk4Q1g4tMYYAJaKrXah1EDNHIiZB7EJ2NJZyWI1LlcBdfF6vEvPR-howDOMlHMRgYNNn9x_IVLlF-J_fPqj5zZBZjdVuBpLNZFTJ4U4HMbdUmb3CK_qK0UQwCz43dSktXKePaS_G-e7vXZLCCJxJP0MNQnvFQXqa7gqevXKXM3CnQWmKwfaowB-knrD8BA4RhQSp_tJcBkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 19:05:01</div>
<hr>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EifKuCTpulCT_OFZUREqD3ESfwlMzcXjU6VZy4p0oPHFb9pUSQ8Al2ieOxiT7EUr7emJ0u0_VsspBkcDTR5uGCk0ppGBrbsXGxEMG23-HtMAHVh5L_WsiTLzy-5wRT6lVvUFjudduAaef9kGeAxoXqHF02XnlKgXTsCKdXK_DXCm0QukG7Qwx7FtPr-c-YT18gHmOZvJWOfdHUJBA3xvW4rBC3UhBKeJjBVE6B-xccGUwCqlLm-lYmNE_GmtWqae5ogqbzVsTJ-8YiIzXU_fOTbJOqkYjs8CRUpDMNI-9Uawlwj6FV81ZloTVxm6v7C2frbJjSaaqjfmgH0x3j2SdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf2ze1vR_vgLrIsaAeU6BGjbceIx_2osoh4kYx9PNzeEXniSEY5a7oBsrCBNFGJG1V1X4JogfSdrv8aNiOz3Knku-3ty8C4f9xgCH9W2LHGJwTbOFMIDUn7IhjATJCE3ZYNjsG6Dkdt_VFI_dxCRRAqLn2zv_pgfw1gCkI6gynmrg9IATZ2hTQOaKWNmgKFfvsIMav8JhsA5oQo--PzFG6hGp27zPgldHYHL_HswS3ZRWtUx8p0BFvBmf7RlXt0n39GMjmsNx44nefVzMhgxP06L7jkvJxqFLNLpUIinGl94egTYFwd-QH7IFVjTaZRjuOlyDKlEnHfEq196zokKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHG79sJfk1HrKHU4l7ii6713U9t5HhqYmsyezxN74VrrS_0Wfk4AODeESUxvBlXCAxfdgL34C6m48QO1y8W4MOTUwuyugrHXriYc8mgORpq_NwTqLW0fc0wlHSTlSyT9cd_hDht5CUQuksOQP8yUtTbPHtHjlDH0zrdXqthLAG3wuEJV9-AiQdkh4Y-fwqYrAS_0TRX8WJubKM96rkSVYskRn_-U-1F13hbS_ydJv57JuvA7goB6HpEdK5i6viK9W4Y38GlpNYX7kBmYP_igM4O5f_GMjAnjF7Mu-A38A8eoDGkCreDvYqtTrxVterCxt3IscOX9ERQlQaa5L7ovQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRenryfa2oG2KZlxHJuw8UXZjm_Nj9EMBcaWqm2TXhMJ_MqgyMofWueYuIbi5LIHFxz3HNzUObmJBK-5b_wPZ11Ldr1CTOGEddN2avyvsGr2WbhYmDKP3WTpvQJ-97BDr0g8RE1BJTMkXLdaUBVj3MegXmV4drogOFR40s45S2AdsF2OmflcWFhE2xxkzpLX7nxiKQPYCcrOso1geNWq4jMXH6NF7HadDV-c0qVUpG2jm58eHAC99kfujr4cchoTdjwTBCeoQG7_HUMkqi-cCybASQXzcsEHxL79GyPWbD5kTa1xhcoB-h8MfR2sp2vEILfi6jd_I62tOlwEgA1e7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUt-cL8RVIYSXGymqenW4r4nRgsCxoGW-79_wktf6DfSRe5Lxm2TS1P2XTnwDVtUU9JZSJttsqEeydmviaa_6V7wUUVL8oNwNCI3CMsydnNdFMmrR1lE6AZ5cWXCN4EgxdkbA25bfstfUAAM6fmb7y9xSb5_0BsJdsza7VoqgWnHlXHxXStjKVrepZzcswLIVtZupfhl-NlAxz0nEt5kMT761-SxMSwwCBUQZLBOrWcs09vrR5rfZd4OQ7FP4_TZ0MqsqVAG0kXRhnLMLi6t8ndI25GTcSq8CWj4BtF7qU5JBXA5L9rX-fcnEVCkPM8y5-6fHkUXQhU0hYUrh9TYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df1C1__G8fN99ec4J187IBtQKmX6CK_xNVDSNa8JXuHMCZKpWEBiWPcKgl4-OnYTs2o8jLYs9j9pwqnFnfohl0CnAHq1q-5we_Kphb3tvMU7R4282dG870pHJcrnu3LFQvZf5SYlWrOg8M4C6dzXZCopGpa5NUsmWhk9sdQ7na9XBWrp3uZ8y-CPSayqyRjFJ5m3qfVmZerXtLxPtAq6Tq478AfkzfFUZX6fHGNipgWDQ3ETWRlm9NORAQL9MD-gwVMVfZk2G-KZimfZe3glUFXfKKseH-2q_XBpVQRfQAOQ0dLGVJifDmH8aGdeQ2e5wLNbZ1rYvkkXdqYSMdBoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDqbOYiJYXCh8Yae38LV3ZmE0EyBLt5cM9ii2SARa5TpampEXW3iXGsadIrY7JCcTNPPDaY95X2EICgZummecTXQQ_7YvDQKsLGogT2mZYLpPeg4Jx0K1PK3XClORSk-cqktJEbuKDT3lx7wCe4hke4ctdNmLoJD6PDv6Oog-RE6Medww2LJlunJxlWDoy7A6mM4VkAcbmuozPV_MzJkewOLrdg1930w-ptaByqU92-EtBHLdRrCpZUCrH0lswdodZklta1xgmv27BKqgHISaLmJpNghtGUJ47dVtozuSPM-7SLnQmqWzFYnrjDxwys3STTo7JSSmL0zvjLZM8TV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR80kl-ehPDj7T_Z_P3rCPuxYS5Lt40K4u-zSO4b_6s616jiYU4lrzGpIgI--_QHuCGUudwvzXMIAJL8xnEXr00GghyUJIshpv592u369HfiEV6M_ZczqWex_5dVOCG9yEyJQmtsQTKAZOGNxVek5vYO94ONJrR7MQhGAypu8YhSn5J7YAal2bs8rZAFz2EoPwBZ-mft4QqkxOTDgEsG3hKjEOs0ByjJk2tplvU9vR9CHVxiTns4J9Ycmn76FSHzFovEw5bn1fViIv1-MTjDLZfluRUt7-CVrey-FequiskSg1oXFCwT-VfsHMbJ1-BT_ERP0E7Quda4TVdxp3b88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANNRkG3p4dH8Xk7aL86TclRYXwj-3GN0TF5Q3WuRz6qR8iKhvTMfMySVz1MBvwJUf2bVWxj1Vgcf1KW2h8ElBrBKAJsJDEn1EPSWHI6QUMsQnKhd78uvVs1bueLtthhiesPPAQvkA4Le6-s_nOpMgKVWP9C_X5_MFcbirNGuR--yEvKZmBQxxg5hTJDuClXwUKO6dpl78dipDR8oOZA8eZRxFrt4yicetIwHMHwbHp0hn-NRSMmkGUJyo0HQPHgQ141vydSPK4024-C6i5IzGmvKEBtGDl3e3GwGDzd0soTEffSSaFR92fe7xjUH1Vr6mJnju5cBZK8xh3_l4iCMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xta_htQ33m12TeqtZXOM07H964tNvvfGQ0KAT_J0Tv0pxtjTLbegR78EBQbdU41qSRdTiwjcjTRF3tn41FYgGPnH6RyBUArktoL6NS4tgnHzoMxr2iCKv-SpMPLrda7JKcrmzbskSzckvUD-hTFyBLqrZ4xiezKmd3kUvDspxKObrCh0Izchc8LN1F8tuXH5-ydO0hDfUk7mUG_ovsyzjSshzSxdCpWcwCvpOnPRWMxj5eBbywCmrKcUIFyY5F930auXBruep4pqDQHWKyf_7vICRklvc-RRDphTC7nHzGEkDhMEt5yjSen3CLe9uZZisRK7NmVKPth2FJA7qqDqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqfKRlv2BOeE9q4D5rRs1gsu32nkNwRRJ8E5cmO03m7t0Z8aCjy4oMjZd3sh-SBggCrC-0qkRcLPnDnNaZXxs0jfUP3K6x1I-KkStPmRFGzLs8vh6_qit-y_Z6Q3dwXzHo9g5ftoyLNumy29QXMS5JPfFzBflT77zDvw5I4mMmSzJDk9Ui3x8jXzdO1MmkB4w_z1us3V_H3Q9c6SB3a6d6IbYktn05LWO279uXm4h1A9G55P4u0clMwH_HgwO6ZqyWvcY_sOPVta1iCUbkXsPr-7iupv9NdCucknyyAbvy3yfN4fECa72AWBRix3sV_hLjbO7iCQ5JSaHK8p2ivLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e18V3Bg-Uy-bo9ikhRI0ztV_Z2nDVyHXyMnW9nG6K0TxMznHD0rcUCZKC8bpW91Wi7oUyLfbE4b7zZzvjQ1CBgGdhjWfeqPDznc5DxCHNy7wC_TvNVSbzahUQhl0RqLJiIn8ijtw2v2X7YxwWwHc2abfIGvwqxd51n3CsFGqO6znkVEkSQgkry0GMCPli_rSy4PBCdSjCwluqoWE8gUA2xoaQx43eMagC36ef0x2bL45tycuf06HG6581-ZHGiFjpxgDuFgeBeE_Azeb9lQLoaHlykgHNtYlZJgjVmD0Qag3-ZYkTtnzC6cYoEsnQKYn7X7FzkvPg-g44o5Ir-1t6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct7ma52ttEcB1SPI1sXDrLV0ImmVQwbFIscb0v8r7ImER-Sl-ZQU6he43rN67jPMWxTMHGevUmsZAqIweLUunPqlRP5B843UzpeWHVjT-kSdYOombDc2Ns0rwhLygOrzNYFZCUzS3wmk2gXr2nZq3YsW00LVUts7qfj_jJfhgUDrnWeeDDP-iwyfkiBcMcoI27uUBA7bJCxmiaRyrUt_8C0qdo6r4HORUm3l9iaZH44CDq9MZGyKAkjAIGspmmKFGiUWabZu8CBlOkjAnAm2hrCUKT4mhOKIbF1Oz64EO50x5zy_pRt2v8wXqAj5QVjvahRASo4jkdkQjjfEJt4edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcHrcZwJ3QjDmpcqSCYCA6Hwu2XC2rG9CoiCFaFGiMLDqW0Jl5GYIgOItzigcbbG8X9PcQCfkoDybWXPv_5FzGcW3Ka6rT5T2bV6CyEqD0vn9gTDx4eu6RWwoMz3TBZGIor3ZeGc39thl-PgEinmxXvkKdoypD-l608DFqJQOnRnkuNCBj-z9jJShgSGx-GqdGDZ1kqVceOoTxyPY8EbwrGeIesVmW3QZFSqw_zb_kgZFUI7mD4FP0_LyVYN4eNLf8uzW4TG3cKIuGrdtzGmzvWSRqJFJvetbBMmRwA7ENDC32Ggflt-Z1FTe9GkCT4IzxpTkL7up7aad-uy4KSYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=m76Me_b3qC6orRKw8pQV_Z8AVxH0M5X2c1WCCl_Aez5P8oDogCd0JQxwBAYAjTxzTsd8XBAN2nB_030CYTk1tssaQrh5UMhWt6I9zW4F6_k_rIpja-y3d5BWeYWAxNZcP3OzNG6dJ-lIKI3edopur4spffv_yOR3H90FXUWq1hBUabpLk73_IEB7QhC9zRL6g2pz6U4g-WsSLSCYFktNE5vnJ3FD_FNKxCGR_Ak5BYRDAqmBcJgfqbAPc0jo3M_ZnAR5VJnSEnNjKiUFWD_F_PBEhWsbKwp0w2hfnDkqYHYYt1NYmRwhRJDzQdjRYruq0oGhq0XVb1BSJY9wps_G1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=m76Me_b3qC6orRKw8pQV_Z8AVxH0M5X2c1WCCl_Aez5P8oDogCd0JQxwBAYAjTxzTsd8XBAN2nB_030CYTk1tssaQrh5UMhWt6I9zW4F6_k_rIpja-y3d5BWeYWAxNZcP3OzNG6dJ-lIKI3edopur4spffv_yOR3H90FXUWq1hBUabpLk73_IEB7QhC9zRL6g2pz6U4g-WsSLSCYFktNE5vnJ3FD_FNKxCGR_Ak5BYRDAqmBcJgfqbAPc0jo3M_ZnAR5VJnSEnNjKiUFWD_F_PBEhWsbKwp0w2hfnDkqYHYYt1NYmRwhRJDzQdjRYruq0oGhq0XVb1BSJY9wps_G1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rie3AQP4dmNq1HVw1llkQzRxdNmR1Y3dFfJw0LD_2_mZR7Uenv1IHplnKxMPkzHBUtdCDzC_PJ6xoeZ_b5keL8lyEqfOAqFtc06P4WNufx8Hd9oHq9IOHNOIL8ALlixE_kyvXX4pmRSsoUuJSvkAp9FkZkm0UDoETCcp3x8fOrGNgRSE6ZaMcrQuhZXhFexJrYXkarR6pzvm0O5NH0KNaJRheqhC2oF6z2XCgJV7UDX2eMeHXFho4EK1JmOa0lUxqvBZVoVDL3lJmDkae46WxQz3faYY1FaoiBXzLntBscRAJrGBqGFp2eJnrNTmyyinDldq6RF4D4NUBaS_8dYVPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_MYiELFmaCuRW4K5t0iXHsssd2nPiMseMwen1dgWTGx0m971qi-AcVBeISstXpS2AyhnVfeeXj43LZfC1a-n6iEhO1pLR5J8AjQeVBRIDzE0hoTO035zhwm40ORszerLXQ3R1EB7bdLoaPRi7z1gEHLYz1yPvQOeylFMUoWTsNdB-Wyj9WO6Lh_cKCtDskntTuSWGzhc64DTBaWW5NU6x0JofnTmwFHfCG8oI5v8NHEnW_23l3seiHCmfb9pwqZPsieW01qN7cWJ0SZVmNsxn58HBGoo7_XYd6Evpn52kw2uv84qYS14b1-kwxyfc2KIq2ogzrCXocJdHYsfBoUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg-Q3oMjNfneqGUWi4Z_1_MstfPfS4pGtLE4XIZUqBTrmlAEex5yamJ31WsLEbXUrJ-nvHulM5RyQayp6mY86zJcCG1upFCSb73SL8oMMmL_gudu__Yp3pqb3B-yyyfSCmrvmyP7wh-qerG7BMWcpRj2OHKl5Bl4g4bsa4IWs-nctM8EAgN2_DzbmkRtxe55kTQHaNeGyFet8H4R_GH-ka5iV0CRe3tuFntWAMvdDR5i1Ye3vByc9Wpgy4pUzgAuQbvLIIIZLZLOLofizDGc1LpDMGi1iOGo4m_gAvYvCBrrG8cOKcwv39kS_9hwyAh1KTughUDl2IpdIsjU-XK8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqO-Ys6gM-aP5jJ39DyrDfIOz_WvT__lYsUOOfNVDjCafVBWPxNBVKEcinUVULN8b0pPCRt8ObUDfCnBnApslp8GWPTmLU4q5AwZNkPAn9pJAHRUVQE-RNB6fUBQoZO5eYPT9vnzINL10TcNQIrBTurHdh4GJ1TLHpLIdABKD67WzlHsNnOxWFDgsIXgdapNtfS0QmF9BkqvTdf2sFtv-SzHHjczl54HLu6holMnn2xgi70kgeuwf1CFHDXGwe2EfUoczZ3PSKeGT6mgOvrX222s9ejiWoOQOBICNMJHy-CIi6lDEIAFb7uPtRfkgi7GyGELP1yO-6_1j22DKY-AfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-73ak1rf6cE9XU2Rxhe6foWf9IfvhvYyNTPdLsO9GOK9kawPzMSjU_DFHy0VFhlgymYTNNmxBHntyZlwzsajr-Kg06xHTCT0QqjT8ExMFPAnidUQhKpv06U2A7Wy3n4x3kE-HuZdQL4PrJS0qwWiYByuQomvNaN70SIrcGxZTgFeni563eQvllKobegXUvtTVq6_DZR2EDXYyEA8w7CN2V30H5BAdEcemNhCxoDBDStYo-_oWecl7lhL0X56KOlsJ5PcJ8Gh8NB0Kp-D6B24PgoLabisOx7ZsuzpMPKTqMab52Ckthnv-0wOAE0RGSkmX7MzrmXkpm2eLgIvldjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZWXiG9Pm2zdfjszEwuYn5iU5V_EP7mO1aAFznmjNvBb4vK53U9R-oc_LyVwBBrHhHuR-sBwCy_jc0Nea476C6z8iHttZJMPGlvQDHTrIYkiCVt8S2P-rH09MTF1o4g2cIp_jW7QQ5Vq0oKEl-WaohwfhDfBBVgP1uPt5CvybKOE3aKnxLp7jEBWCjbfLFsUoHaxeC5rgQ9eNgdhv8wSn6CO7_muNTtjWMvoU5HWziOdqHYqVW_g34aNwrjnYbmYRYGEoaLV4e-cpxhzDxThA1KlocF6jW-Rle3XzG_ji0cCRQd4_grYiy2z9D3A7SqjvHvn3ptLnRPiI_30yogJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_IqMKFX8OgRbLEyw8rO2mEHMGLx_WmMsGQDl1n5_3kN3eSCTlCD11f1NHr7rnYvypYaGN1AXY05fm56NvWd9FF5Q-49tQZLNAnxGKdOArZKot470ndZRggLwjgbOmeEom13tvgoCpOC6eqMoPNrLYoPrijUXuqcUdC8jo1RMpKR_YDklvUL7PlFaxj0_QsnMKXaaieAk-juF6zrsUhy24-t9KH0iWUrPnGtQ5uIuXBX1B9iFrtbAqaqULCopqrLPROUPcbSSqaq4EoapGn8D2s4_Hd2ZXbzNYR8C7y67bUAF3aysWc_-uNoGDmPO-1MlT9Zbpko4JymG84l7IQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD9ZlWx9cVj_jEsUeEeF9DP-nqMt96Gk8HGEqi6InLVrmhwyynXOv_qwSC-_FVZpUnpmUo-ZPu1FAn-AKLFayMq8iKJZ5Cmc83tEyHdKuEkUNCFLBi96XJw08YimuBBP1jtuuqLIsdUO3ZrxfyL4Mi9lk5aMG4iHq8lci_vhP8LXmdUinvQ0XCcplh8IBVVbfAUGOKKSZkVHi5EWJ_EpzBR2M3uPk5Mzt9vpxumB9kwiLfPL9Di6Fy42sBQlR4IZzSmpXGtD9YkKePEUYXmnQmVrhcOBUISAk75ruzcbcMhrTgI9kIIACX6WmfzOvm2b8QZsObCSyGA0qw5ENngmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=GH-voRMiAQVI5Y1lxhUPgVol7OMha4y-eRHnKBtGU0velpyDlh8qhhHs6a8RhjZk1dOxRqZwmSelZ_iHnQ8H_fTCdKvF7wX6UHLszpxo2fzSazSsezyxJ6sPHBEJ93xiZjgCk_C6356fBq8nsYJmlRyO6zEvruK0Bo7uPGhFeatc4zwAVSuPi7haizCOylhnRraYG-3Fod6tty7bdKoO3zdFzLb8x4jbCU0t_-LSlx_KVjlCDgzLRrZD89SA9mKMGhL2bWnhfaOpgwGXI4UcHfFPtyGx6r0hHvumrErUBFqmFInvCF13WBBGdMNwh6TGJxXoKk8tBQRkb0WiD5JtAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=GH-voRMiAQVI5Y1lxhUPgVol7OMha4y-eRHnKBtGU0velpyDlh8qhhHs6a8RhjZk1dOxRqZwmSelZ_iHnQ8H_fTCdKvF7wX6UHLszpxo2fzSazSsezyxJ6sPHBEJ93xiZjgCk_C6356fBq8nsYJmlRyO6zEvruK0Bo7uPGhFeatc4zwAVSuPi7haizCOylhnRraYG-3Fod6tty7bdKoO3zdFzLb8x4jbCU0t_-LSlx_KVjlCDgzLRrZD89SA9mKMGhL2bWnhfaOpgwGXI4UcHfFPtyGx6r0hHvumrErUBFqmFInvCF13WBBGdMNwh6TGJxXoKk8tBQRkb0WiD5JtAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7fDL6bxIU34f_GyoTklJmMTaS_INm3JGCmWbWbLs8OtQY05_w0tNo6JE7Vvz5-cDikSIbUe6TWfUzfFVLmcJ-oD4ePKQ2Tqvo7fY1n76MyHAxrSFheYBgVYKPwy_jzuSVl58hzUpJlKT-p-B7_FxvHRbWMo3EHJlVo11FheLpxgIHZCsjQGWq797unfzDkAnDZfw_6EgDNWGlOORmANQhAgZsb72iBh73uulLyCPM2B-PWV9PGQ5FGFJPYmsCg-KySsaG1Qumw9-qIjioPOonieI2ZTCR9atTTVUmgXFDKhjtrUWHqJGy3sQ5yeg9qmJOwy38_2TQkSR8p8gerX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWUGkrs15ZjWk5J8BftqzGL2DMdUbU0Mm63HGSRmdBRgOui3zbfc51MMFwfK5o1dMi-uD3rZZENLqItLn9q0KbAeAUdXNZFioDxzAafnY2G0hu3Eh_ZblJfSm_NkaBx1rG2V1skLoLsumEg9OYnP3SfZiqkEp6tBSdhbHFqgv6wi3a5RGa8UEuD_V8kovNB5DTEvGb3TZDjCzbFJ1Qg7Z42jsv9Fw7lP7rmuTK3-t1CFf77cW8-SdTnhzq9JwUyfTyzj5ZwLhcWdtA9irDtORzVa8RlwdDiSxJ4vQlzoRamIRCkPjJfqh6QetonBrHSEZnb_6GLg1BDsaHaDjJH9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be3cpTqWGYzvikbvguIaNwDHOdmp1MECqKlg8cyZpYzpVnsUASWVMJoHUMtIQWD1Pf_EM6re5nmYjVYUyLavveSkY-7toIL2ks_qhDzK3g32l2hHSUou-j9Qh6jn2D7yvaECrVXVcDGSbXIMCn-RvPLGrW2rCbO1RHI3ebTvA67YY0FSyZRLGP5im_tKxV1I7Sw0acdOD9iSv3TE56Km_nZSbrUYMBakGce_6Hy4d2IgiLSxEUyAbljy1NtOaOBZOh3aM4kQtnjgq4K9Ya20EEy41t2jjno7d3Mjaw5HYEi2-x24Z4H63MOMM8RtDqN1iW7zEnm6NMAbSUAfEs9umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVjeJYtqErrHXaFCPqEf6FMTIvmkfRi4UuJcAm89VIYgNzXgBbycfDJe90rhtuycn5YIx7mY0pUq0lNhzAO1SzOGFEfInu0qXmm-2kekhfTOAIWURvIsUR7Rmh4TgBo4zYNZ4DzEV_FL8kRQuSFXN1TuTBNSGgdyvtOaDdZ_2oMW_F--baxuAHPZTAwtcjA8fiQcdBHkQP3rBRYvtb7K9t1ftJA1kMJmPzpvS0kFlw5p2p_Exh2DHI-dA71T-6eShK2yULZ08s9nH4zLU56_GwcbDejAeKxNCjCJbV9SoHD09HQIe06pcViXqHr1s4S92y_As7WsFuoyNtcgzrxqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIxgXCS3nkDfswr-Qqs8xtENfHaGZTH95dgiagCmBM7KPacsiS3Ws6ZMPH-YjoeYzaCiNdUS9ZNiy6btDeEemrUuG-Gm4Ch57QMz6bEP4PwoE5rZP_l4njZzhENabcBe91dcPiwnF4TEdso4W5MpUvsLvtlRZZbSEjGuFKH0pFC6GBmZXdz2h267k6YRDvOr5IpNSqC6mgxIqfnDHZPQbwGWhP4ioOmQ6IkFkjpsIsOcIBcSG9Sxmo9_7S2CZcotrxEPW7U9WF-QX9WXoxS9R-GEF4hcaOtHW5mabtPnqA3zbFABr6WPZRIMBE0X1XdkJsbsoFqLQevv0Y7OZF7AaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss5LsYsSu1bTIb2UxXMd3N9qkH5zx22In_lszP513GGWkQaaaJJZ_Fmym-A_BHX0srIwHm8db2shPuvTVgvLfJCZwxokozeRNnSa3toSS8-2P0Knx5_QnSJPdBdcX2XAiZijT_I6G05RcwAqBuWfSyyExSBX5zzwGWYwguXHVRQndZaDynooC6zlo8PLC_xojC5Nk4Buwdpd-8cw__VSYhmvSXlIFGq5X80iocmT-fA4wsgZdoY2PwTZ9iQGnil0Keu1gPFDiLOWwN4Z_kC4DVkwd4js8Cc1ms85wHe1bFcRm9bnM0UvalOKySJyYhKD7CL2rkFmPNEgwkgaSU5Few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW3GqkA_yUw4ZJ97Hniq7n8b7VY8gqwn48WozSD7BqYIdsRSSpphKzfvIFc7S46V3dybYUJcpIP41qqDdMol--i6s0PbeA6c1m1WF97JrpaqYRZq2B4nEgvbhhxkfJwkMQAZc1_fMTK3maKAVsM3fxWV_10g8m-f0gPEGz59tOkAaqa67BCaBu79NNqvrFg1yamaWyZDeKSjpb-s2sveUsE4ASK9ML0jwDN5pvHeXaiMxCviYd652yecRdQdIbEjRjI8J4RallO47rsSageC8jzbBDO2Yerb9JzIVSoRYNIsILxSQpO8Cn9AiM1DUn3d26Ev96Ow8iiPCuu0F0Ylxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=FhOhUo5bBtLvMeDpMbcUjVy5yqepq48lzC62-XaAoy4HIlXLtZ6RiB_5RqxvRrH4DIfF8SaR9pIqW2JohlCiTiWMfA_0axCX3x79bzNw1SjLB1XEumFifhzOJS3ftknACiSPiuJvuMUAMffi0JCwKGMfzjE_keBhuFKDzWcnXNleVWv5GVuC22ZqNj73cPWjog3MT2nYYVjGemrYRkOv03hrKPVebETwzbel1CS-GqTttYPK18Z-TYiHzIXGwQBiE8cIASzCbhWKDny3dpFBwMPqy0N8yC4XmvkXcGJpHgX9oFFq0XhxwxRTkW3uH4a1qqFG9sj2xRpz_0j9WoxeO0Ae0LARODCKxQ3SPQCDzYMCPaiH5HRap4YoInacmi5jUri47ylk2FoaDqUeUCL5IUewO3_p4qHxSEhFt64rWz8gw2R6PJ6uXaaHg2OcYu5jjOPIxClm-je8IlCmGK24_Szi3G76Tfq_hO4qZok1sbLkOQfRoG_CWlWVPiQ3_ggHV_Cl9hQzHQ8d0WFgTr2ctsEGzRybCig98y6w-oOkxTkwzPVCijkzGDweCgdhAGm2su56XAC0tyUVIJtjT6ef54aN-pOmRM-NJUEWVLeJW2KV05owUVOHH3jAWpZgv9EVF-Z7sVX6atiMBgNxFCp2_wefcGd_1Rqa_gWwlPul7fo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=FhOhUo5bBtLvMeDpMbcUjVy5yqepq48lzC62-XaAoy4HIlXLtZ6RiB_5RqxvRrH4DIfF8SaR9pIqW2JohlCiTiWMfA_0axCX3x79bzNw1SjLB1XEumFifhzOJS3ftknACiSPiuJvuMUAMffi0JCwKGMfzjE_keBhuFKDzWcnXNleVWv5GVuC22ZqNj73cPWjog3MT2nYYVjGemrYRkOv03hrKPVebETwzbel1CS-GqTttYPK18Z-TYiHzIXGwQBiE8cIASzCbhWKDny3dpFBwMPqy0N8yC4XmvkXcGJpHgX9oFFq0XhxwxRTkW3uH4a1qqFG9sj2xRpz_0j9WoxeO0Ae0LARODCKxQ3SPQCDzYMCPaiH5HRap4YoInacmi5jUri47ylk2FoaDqUeUCL5IUewO3_p4qHxSEhFt64rWz8gw2R6PJ6uXaaHg2OcYu5jjOPIxClm-je8IlCmGK24_Szi3G76Tfq_hO4qZok1sbLkOQfRoG_CWlWVPiQ3_ggHV_Cl9hQzHQ8d0WFgTr2ctsEGzRybCig98y6w-oOkxTkwzPVCijkzGDweCgdhAGm2su56XAC0tyUVIJtjT6ef54aN-pOmRM-NJUEWVLeJW2KV05owUVOHH3jAWpZgv9EVF-Z7sVX6atiMBgNxFCp2_wefcGd_1Rqa_gWwlPul7fo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=KgNeNI2JElr1uHnpOMdzzNy64mlohQE9u3tbD7lm2QG8WtQxRnbjpvJg4bmTnYUUAEl9LHAdEzOeifSo_TLd1TUHA1yu_uuvvRnrquKDKpUNpL-oJSc8El3ejfPSBtAWwkbWVH-KHuI7NkZ0wcqJf8mwtp_WOu5--JlrBEDUBNeu5Wj7-jeH9ZoYB0UquMH7_fTLWhK4t0NpR32JsUqO9Eno3JhPIAK81KHUO0jCuc_-sJQBIqP7NDCqv6fafbcdVQO8FvLX8SY2bJlZXZ0OWgqVK5AoOElyc6VrhHhWnDtuBs8VD8Zl_ZzoSjRYXBcLH1lKdJ06O0xbFB_MXnmJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=KgNeNI2JElr1uHnpOMdzzNy64mlohQE9u3tbD7lm2QG8WtQxRnbjpvJg4bmTnYUUAEl9LHAdEzOeifSo_TLd1TUHA1yu_uuvvRnrquKDKpUNpL-oJSc8El3ejfPSBtAWwkbWVH-KHuI7NkZ0wcqJf8mwtp_WOu5--JlrBEDUBNeu5Wj7-jeH9ZoYB0UquMH7_fTLWhK4t0NpR32JsUqO9Eno3JhPIAK81KHUO0jCuc_-sJQBIqP7NDCqv6fafbcdVQO8FvLX8SY2bJlZXZ0OWgqVK5AoOElyc6VrhHhWnDtuBs8VD8Zl_ZzoSjRYXBcLH1lKdJ06O0xbFB_MXnmJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub7H5bICdkFtgUF1Zm997D52JP6VKJeGC9_mPNPi1em-hWyuW5uV27QY0UjSXeCfmpU_4gEF3beztRUVBVTj8uiRDopdLnPmdyJUtUrFf2GB9ZOo51F0iYZ_eqe26wjZ8BywmhedRBvpmDm8Jf39rovjTCwKiKCxM-C3H7UxLsjuuMmDlIIttjvwSZpRuqxg7Ia0pmQfZ48vsNOTj1TzGElFayOGQerw2Ep5hezysotI8pgknoS1iS6HdOZ2C6yP8kiR5vM-xrC9d0rUQ6xYW3es8zVNyJKf8Q1zm2vJyKKHDxeLmurwQYFvFiC5oh_2qHcymUB4QQGiyH6gGJ93dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec6hG93SenMVLeC3FBwfKHNS7H4DR6xjwfANHDFKe4B83n_lH0kELHQN4akE3OkdlQCAqpnqmboljADQN4tySbXC2rWxD4VKPBov_QT4AswTkVcwoZgVxrPfbjFUxtrc8JEo4Nsd78Kgj1c9lAyY2WMkHrGBCEEFt-4AnSwKx4FlCY4T4RSWcRYk-9XkIpRZHNuYd2eNg25IOG2wbRIIAAIIcPxb60_8sBzV5p-waHSUhWHNxrozrkubdnHYfRqrTkJKFI5DEEoIu2Fgdq1pW9cpWkqO_vL7RYhqd7sPP1TacdmymtltsN5ktpHtxvcp6gYv8MzHZR_A086Fgl-veA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=sFkUJViOxGQGjoC9AQC1HeWHuHm70ukdr49C20B_xJfjUh7JdnECTiTDdULr5SsWIcfgd1RWHSvU-XDCNmNILIIvFDrPr11qgr1bXUWShf4mTH9EK6BJq1Yh1HIcEV4xlxJDuHV9o0kpKDcjELm7A8sQ9g5_Ay2mVSIDw2_ZHsBrowLqnCml7Twk3AHtocIVtAAxSJAbYuuueCvOgRkDIv5kS1ccmSot4eVSytAh0wxHSFe6B7Igu7gpmf3WZ8HiC9eAFbXUFTTFkFaO8wXKAUvBajEclieEDq3e-wUr6ryEpGIVXx0Qe_ATZKnHlq0DG_QZK9Ktoit0YKEae9GyTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=sFkUJViOxGQGjoC9AQC1HeWHuHm70ukdr49C20B_xJfjUh7JdnECTiTDdULr5SsWIcfgd1RWHSvU-XDCNmNILIIvFDrPr11qgr1bXUWShf4mTH9EK6BJq1Yh1HIcEV4xlxJDuHV9o0kpKDcjELm7A8sQ9g5_Ay2mVSIDw2_ZHsBrowLqnCml7Twk3AHtocIVtAAxSJAbYuuueCvOgRkDIv5kS1ccmSot4eVSytAh0wxHSFe6B7Igu7gpmf3WZ8HiC9eAFbXUFTTFkFaO8wXKAUvBajEclieEDq3e-wUr6ryEpGIVXx0Qe_ATZKnHlq0DG_QZK9Ktoit0YKEae9GyTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJoUjNgQ-7CKFEnASY32Ja2LIJzZT5rs576gLmH-ExqwKY1m_n1pZnvDGczyFH2KLc6TE6detZ5XlaJGqueO4PYgim0GqBGVK2BX2gmG0TN4YQxWTL9r7Gqckg1uTS2E-dGYk96VW30Jiu8SJYp4c7AO4q6VNohYaBCGHD97mbkU_vVXwef2Ldfoqj_OXScY2lQUp9utgrkBKJAX9VYNemrVwcMWR1sJPblB2krNiPWg93W6CmLAq84FDnc3vWzuaaQtlRkM8GkguVnmIw156rmzf-2cB49iRPRZQ2FuNjsA3V9Llwx5jfytd1XWg2R-pD0_m-IQZI6bUGIXrREpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5xTzUdku9Sowb9S8KDLZ6FzIeFkGyVHS25iEPfVS6Dy54x2gO-PzDZIPPuPNz52FQJohF9Xlc4XPgspqI5ExqxSGPnwAYn_y1obfvgANYS6rqzvdf7-65l7c8AfzhraFnCi7FFcc7-TLUDcNVKmxDHt4IFkXOrdwed1AzDozQ3MlNm6pe25VlEuYlMPbd3d_M6ZJlgM8k5mG0_VHYlC2vMVWBP-7kNCckGfZnWCjNziZ_c6WWkSFqNoK4jQBTUVlFvtHBdPxcnLIN-AxfywGfDKD56Gk8CSxG4kQR5TlSaQFsMypClPP3mjgrGlnX3ayxtN5xDjg971MuWbGHoPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8jRAKPd303j_rXAgXEekpSidjPB1L3aOOBlsTRt7HKKd7y4QhUSSv4E91JFD6APDWyOhAx7WkcFyP2XPRxluWasBgIizZbwVAdsVQ4l1p7RZ2vcvXCKIrWr5wCJLe-vfS_oewppbM9D1LL7aSCX_-afprKYcYWaERPNkO5QiuM2PHI1_xtCnUBJnC0fPAL70b30yczJY_sWBXd-CTGoJ5l1UQ0MxKDy20l6lktn4HnlTl7-kmH6QLsHDnvbtigsgX4SNaQEsOu1kdXqoF8TBJ1u2M5vWpkvjCo66ourDqGS_ZOxRAqKbfT8nJMq582ziCPI9ORraEobVQJcFTgHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZ6HH9kWnb4cdmaIsUxAiaGGEK9hOUlb9aWsDgZQUQe5zdaztr886wtff8Yk-EOIJAOcfiNWigoePb9gL9VB7GR_rZloLLoFoR1WLjh6qbrDwjTErl8OLKgzF4XLx5H8j7mp6cIwUKFGQ9l-AzRPEAhq4CChZZl8BCjMYfAiu7rJp2NOyciRxtXxGt4p5xfnNCwif-0jMpfFvfQpDGEJaRTQeRoD_xvUTQCgLC9Pd9seqqmMhkBA-TqcnwFzdQXsA-8yh2y6ARMTPCV_ipZMxm4Bg3W89dxJG-WT7aXBIyZ0n5zT6i5KtXl1QdPPgStx8f-Wfa8QnmK3AhGbkDTQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdcL2MFNDb3E-KqfDYvPG7adiR9_kwW82jQNZ7I9a_jXpDXGSmHZZE5vZezzKixP3i8d9AJ6i0k_d4svuo0a41MaLQ7scf8ym6kbkvIUNIAX4HQhwCpI2W-1Lr8G7Bza3yjRSef4OO2kZbgzTX0F9wInn5tNgN5UaO_c5yvKeJgLdZuZ4K72sDRE6TBKOqKDDZ5Bcu4t49C08fVqNzUZkoKILFZBXXM-I5Zwhaf0aAc5U5v-tU7IBNo3ZmpoOtq97_5UvN1xDD25KebEQeia-3UVrmKI9-RYrK8iczRc1FdQwBfstP4CU0QTBzA6mkMDSel3bmhfMaO2pPSkjGaLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJZUDCOawVaMRn6jSfPhZGA4lftqgPw6fnY9Zq_yhqYN0cLsNiAjWomha0_UgUJgZg9yzswFImpZ9CKHxCaMJR8P98JOtbOoM8GkPiXv-9ljIBMX5D3JEdT-ApCckBHTHUty2qpmV5BvUSfKJr9RpaV7T_Ow3vd9ZUuTIwUcJBkxDlkfln-9zBl3rY1ZbbLnF6wMmT_SWGWFKq9P7vFFSWaO8MwqAqxX6cR_G897boHwVrQsmGRGiNYZZzFcqPZLLjjsVwoNLOe0UFZCjsPdgobBBvwxqHcnDsxcT7eSLwV8DLdP0suacuTqiHalJmzjo22ogMtm4RxPCiqyOvt0Zc1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJZUDCOawVaMRn6jSfPhZGA4lftqgPw6fnY9Zq_yhqYN0cLsNiAjWomha0_UgUJgZg9yzswFImpZ9CKHxCaMJR8P98JOtbOoM8GkPiXv-9ljIBMX5D3JEdT-ApCckBHTHUty2qpmV5BvUSfKJr9RpaV7T_Ow3vd9ZUuTIwUcJBkxDlkfln-9zBl3rY1ZbbLnF6wMmT_SWGWFKq9P7vFFSWaO8MwqAqxX6cR_G897boHwVrQsmGRGiNYZZzFcqPZLLjjsVwoNLOe0UFZCjsPdgobBBvwxqHcnDsxcT7eSLwV8DLdP0suacuTqiHalJmzjo22ogMtm4RxPCiqyOvt0Zc1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnI-Eu-oYm7fDAnIlZm9wl5OaBDNjEZyH8gxlC2NRJI6-3-aRRm_t9X1K4WcBxhMUkFlfjDOeWCCOzdQGTgaWcufRd_DxtLSY_iHtc1aAOZZJAgp43KkboW9XgsDdQseP6zwQASlyOgEoS_kRQvEwUq2l6uD7Xl1TvcKAwV13o7HX9Z7Yo-gz7ynCuxChKvAUGo24PG1rCcSnLGz8cy_6i-8GJxutAhqPr5muN-AoLOXLmn-mhBtUMNFX19FdA0ftwtrV7MCSrOrwrzrGTUocJG-F1klVxMcbv5-VwSQNB9W_QHEus5sysCT2ATBQaBgcHx0WEAfqL1OlcUJkJGroYnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnI-Eu-oYm7fDAnIlZm9wl5OaBDNjEZyH8gxlC2NRJI6-3-aRRm_t9X1K4WcBxhMUkFlfjDOeWCCOzdQGTgaWcufRd_DxtLSY_iHtc1aAOZZJAgp43KkboW9XgsDdQseP6zwQASlyOgEoS_kRQvEwUq2l6uD7Xl1TvcKAwV13o7HX9Z7Yo-gz7ynCuxChKvAUGo24PG1rCcSnLGz8cy_6i-8GJxutAhqPr5muN-AoLOXLmn-mhBtUMNFX19FdA0ftwtrV7MCSrOrwrzrGTUocJG-F1klVxMcbv5-VwSQNB9W_QHEus5sysCT2ATBQaBgcHx0WEAfqL1OlcUJkJGroYnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=NMj62a2I3M-VQ-kEDh4gEvlUsmxTdywgkwd_ifvh_ew9Yo6Q58_tpeY7lDucaCweHWh2_175g_1Sn2YakbkPeV9ijWfB_RqRpTzGGZ3IZB-gd0bbuav0EoGnfYYB7TVlCsPUe7t80Eq1CKY91mBUnCxYbG4FR6vEtcgIvjJx5JdKIg1B82iiNJWTOdsLvCcvlDbA0lP3P7sLrjq7lmiCoUmjx1ygpTJE3q1gdH44AYqOQzMo692G86dgP1-CVzVw_gjGeAjcQKAHlNUmYUO8DQC6SwZwxuWI-I9IVNUNLlZoTfVPUyWkN6Zruh-kcXPDwk0goYP2YHhCnl44MgNF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=NMj62a2I3M-VQ-kEDh4gEvlUsmxTdywgkwd_ifvh_ew9Yo6Q58_tpeY7lDucaCweHWh2_175g_1Sn2YakbkPeV9ijWfB_RqRpTzGGZ3IZB-gd0bbuav0EoGnfYYB7TVlCsPUe7t80Eq1CKY91mBUnCxYbG4FR6vEtcgIvjJx5JdKIg1B82iiNJWTOdsLvCcvlDbA0lP3P7sLrjq7lmiCoUmjx1ygpTJE3q1gdH44AYqOQzMo692G86dgP1-CVzVw_gjGeAjcQKAHlNUmYUO8DQC6SwZwxuWI-I9IVNUNLlZoTfVPUyWkN6Zruh-kcXPDwk0goYP2YHhCnl44MgNF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipLB6t2XbEWtNbexuA74Y15sQYj86eDIsuaNp3djZe5c9zfWG4JRKnfpl_auqmng2gQ1_Vlqjqk48dI3duLKZ7ojonQy70N85-w4rewF6J2gmHl9qhXeltnbRiJV9ekQ3JOr-0FL8KXKHxFct0WfMXuFBakmX8Ro98J6m1sSEFcWQWqRCr5FP9Ts_Cjr15SLeCfzXchGllcnIJ3AHIPKf6TUFgjJFIKHiv7bVm0t5Vo2-I2HtoimxYxqej66MivPxO5iCGF5X40bOvU_l8qQfThkWpKCk82TtTHqYN8FFGODHpt4KE7gYKpRKFlEhUZyLzhGdhhWac7FQnl_5BoL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrZJ_IvEYMTSBmhMYxz-yUiTelJoXSro8LRbMdpwKtTR9uDZPeG55ewS9KYALHBsgWjdjRoUlA0662Jf8zqzpVZUaYT_-wiJG-d6MSHXIaDaKlrFnExjV25NFtXP526mfkyZJnoC4z9HNpzyBEupRw4yOy1nOF4Y2UdKcZf5-M5_Kwd37wXZzwR8ULv1ubiJJh5fqnbiBzDwqtbXWwuDaKmiu2Uy-8B5RcVf1wAB1_XlhBg4Mz2nKdjVYqblwxcXMegX6xI0nlDBPZweGgvJXYDc5DA5goIfUpoYUU68kFRNZhuuUVCpLC8T67p9XotKH2kvPn_LQidr9RrkPU9ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=KnOUuqlwXs---oGyVgKob0lwrltKg6VvdD0LZUhPIkEYp_JTsBdBbu_xYIuRxRoUs7XD51gyDCrRPMJpjpL6-F6RqcZJeUKzxSb3wQQExosI8_FuE57ZIM21bU4JtKasDFNjuHDNo2kyUPxDoaq_RcxJedLzvayw3qKoT85LvmOSUJzVTEkxUFacosxNWRb5wMCQSDg4X3IbtEwMB0FoQEJaIA0atCtzUZLSVMTuEUE2ODCsF8yZ0jc-UGCbK7-FJnfaQYjHgsibNLaN7MMhQQ8XkhWLAXfP1OcV2lkXSK85f941wvZID-5WlQLi83SjhqH6AbrU8rn4zO4hO6SJDQ-a2uUw_KyevF7TVGjdys65UducZZ0qghVf-NpoAOH9CKmUdR_MEtGTJVzwQH30eRl8gB0mdwhmDvSAmGw_g2N_PHkHVLsK1SkWofkczOB4DmJOBTM4AaFNegdAQP5xHrhWmxf-19_XF6oeDe10GvkOd_QIkmxyNwemN9p7e__krgeFiHH2rze6lV0HwVQWtBiJY8liWc5UZK9yeUHidoxe-zMiGlPEKB17nbk7dJOcxl-G4RITeTfjt0W8yrlxiBgVYSV720H-ZziLKjbuJp1JI5XYknNAa1bKmTmvnkQKnr1R5FLiqJsoeAVa1EqglDjRkhMaujBZFDVwfNUsk5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=KnOUuqlwXs---oGyVgKob0lwrltKg6VvdD0LZUhPIkEYp_JTsBdBbu_xYIuRxRoUs7XD51gyDCrRPMJpjpL6-F6RqcZJeUKzxSb3wQQExosI8_FuE57ZIM21bU4JtKasDFNjuHDNo2kyUPxDoaq_RcxJedLzvayw3qKoT85LvmOSUJzVTEkxUFacosxNWRb5wMCQSDg4X3IbtEwMB0FoQEJaIA0atCtzUZLSVMTuEUE2ODCsF8yZ0jc-UGCbK7-FJnfaQYjHgsibNLaN7MMhQQ8XkhWLAXfP1OcV2lkXSK85f941wvZID-5WlQLi83SjhqH6AbrU8rn4zO4hO6SJDQ-a2uUw_KyevF7TVGjdys65UducZZ0qghVf-NpoAOH9CKmUdR_MEtGTJVzwQH30eRl8gB0mdwhmDvSAmGw_g2N_PHkHVLsK1SkWofkczOB4DmJOBTM4AaFNegdAQP5xHrhWmxf-19_XF6oeDe10GvkOd_QIkmxyNwemN9p7e__krgeFiHH2rze6lV0HwVQWtBiJY8liWc5UZK9yeUHidoxe-zMiGlPEKB17nbk7dJOcxl-G4RITeTfjt0W8yrlxiBgVYSV720H-ZziLKjbuJp1JI5XYknNAa1bKmTmvnkQKnr1R5FLiqJsoeAVa1EqglDjRkhMaujBZFDVwfNUsk5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=OOvu_ahyxf9rkqQ_2MxrOY3atM4GJWxVgpE0IUWn2HYbb3Z4IK9jtJ_Zv6KZsDuZiCDKbSCMThwnGT2K5Cpi0hjwhNYGe0wCQBLWgcvA0sEcXHM-wJYNCkGiDc-qGvrqQ3AF0Q4prJ_N0l9ADSXIHkdC5khBxbfTuLeOhX4m3G33tU0FVCRTssM6xJkW5S15JSKaeDVuByGC5J1T_QhBNTNQELElq0C0j-f6Ll2LJzfPacRSobLfTwhcin5pEGrPChCMUwY4YuUe_ZHKFbaOnK7-4_xiuj6v_hO909fo1ciSZaaaN0j1vZGgc5XZcYMtYDnWkBTDqqWPlBtxNm1Cvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=OOvu_ahyxf9rkqQ_2MxrOY3atM4GJWxVgpE0IUWn2HYbb3Z4IK9jtJ_Zv6KZsDuZiCDKbSCMThwnGT2K5Cpi0hjwhNYGe0wCQBLWgcvA0sEcXHM-wJYNCkGiDc-qGvrqQ3AF0Q4prJ_N0l9ADSXIHkdC5khBxbfTuLeOhX4m3G33tU0FVCRTssM6xJkW5S15JSKaeDVuByGC5J1T_QhBNTNQELElq0C0j-f6Ll2LJzfPacRSobLfTwhcin5pEGrPChCMUwY4YuUe_ZHKFbaOnK7-4_xiuj6v_hO909fo1ciSZaaaN0j1vZGgc5XZcYMtYDnWkBTDqqWPlBtxNm1Cvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MphR6szCuLaccVEnUYOnSyffcBSDp_hCaDQ6--Bsjzn3Kg9wOhtBxtXMRzEJkYE9ZlHEXz1kXGgRnPZ2GTy4pOHRxTwIMFXIjlTC5DV35ze2ggcBQ9_fGDOR825HE1TUOnqDlkFTW9sw5gq2yP_wsYFi6u3J6LYxK8GKzUO8-hINuI5PpHNKpot6u7CQwKPUx7z6fzLt0T-fNQi-t0HJTAWktVfjx4aHpcoueT20sWwPPTbuXEWWYp7kT4Q07_71OSmzKUA1ebwusV5FZHLdXyKr_elgBmLwJjX-qkBAfhrWUqG22ZL18k-JzGgOHvOxsawfP7z2vGUFU6x14wXlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5pGbsMN8vPlNGibuUenrG7CfB7R7mBXNXCBSmzQLrrFDqLKsBh9YMfl30s5gVn3_k6OvDpRR_q2wEpXQ4yx516ITAMrJrldYL-u0ipcy1IkoguelhsxNSPPrTwoETtVqfN2pPxV2zlQsk2bs5c4sFanxYrd0ULhJE7LimCm2q6pW0SwjEvk22vKWeGPjtmU_2g5AnS5ouoNW9Q6bxSV3TWIOag3q_QFHxhTgNNj2NyxN3E3-Wz-r81jt-RtG1-WUCuabJV074a64-J0ms0Zxiv6TgHe1X2Eunj-ZmQAqhrtZB0i072dWoJMO1I12dWxhpXeNWbD8S8JKF9lF9aeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOzxn5iVc1RDLvVYOQKc3gBj6bP2tsjDdH-uFMpAXbbHbTHWyeSfrxl-2CGDF_gpfTsOvJPk-W-RvlicirEyP4_Xl0D-yLPPW-AxE8DHCphvJuxX9pcC3B65EvgB2PhchQoemt1FcAVc4GLoHz0RQb-kgr2TFuucvJ7xVrj1D8T3FXUAOJv6SIM0igjxvZFXo0dd9NCUeVxexVOULZRyoKgMAiUYCKa-UzX5XAD1_sUJZ5N3sBsLbVmYdII3HhkjioOEPW3qtme9o45sVZJ_dBjmQHPq6F5rNgCdpfdwp5yzlzF6tWB8dXf8qQE3zmLvnPmge_EtUtb0YlE_aI3t-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=pKTloBQeG467LVY4zzJwzPinYi3OAFtUcNuwa4shAWDw80m5VuifvY_0iPqlOL7IvC_FSEgvRD4RkvZcQmxLO_sEVWBAyyMGG5gPtDvXIlz1TFdsuxrjLFmkVnWv4MSQoTNqN6PnGfm6IWECwxPXMEmzEo0ZEm5yb27eEQQy6AJjtfBs5uJdU__2yI8jP21fIG8_93ClAnduVUvbDjxe3FCebVdWdU5CP4S49Z53oggcvHbmACefzjlsvhuK21pW8M3E_ZlrQZLOggBBeh73vzB4UMVNPJxo1t0Z64Jlqd7FXy43pqBHqGSYZUEVlwFiRlEMkOucxKbT-eKov6CZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=pKTloBQeG467LVY4zzJwzPinYi3OAFtUcNuwa4shAWDw80m5VuifvY_0iPqlOL7IvC_FSEgvRD4RkvZcQmxLO_sEVWBAyyMGG5gPtDvXIlz1TFdsuxrjLFmkVnWv4MSQoTNqN6PnGfm6IWECwxPXMEmzEo0ZEm5yb27eEQQy6AJjtfBs5uJdU__2yI8jP21fIG8_93ClAnduVUvbDjxe3FCebVdWdU5CP4S49Z53oggcvHbmACefzjlsvhuK21pW8M3E_ZlrQZLOggBBeh73vzB4UMVNPJxo1t0Z64Jlqd7FXy43pqBHqGSYZUEVlwFiRlEMkOucxKbT-eKov6CZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=v9WxFKSrLWvrX9boZgbEdp_yt3sDNJ4rrjzZ5nZ2DsmVc7EToZ0_qdNRT8QhGzJXbUWAu9WPAzUpyFhZ07B2FNLPyGMi1TYemDTSnQKAR_Y5MVsoDTcqfLxSkRc6E3ZIyPPo3C09AX0WcdAaomwwRAehdCQa_n-j0aWU6bq9l1cacm7zPkkN3R70JqJAKrqeSJHnTrFVFej6G7qy9bbAFW09jIqg-ZKd788y3-__4hTrjsyMljZDXdz8kUYfVpZB9YOunDSfb4jl-HsRTb5yZ9fll2zQYEafVUTwuOSLuMGlGfN4ugTQ7mkTZguAmovAEmlWaxPl38cbMkxIfH4xg0gWBf5-krI-Eli3svx7c0gnP-rsnHN9rKGL_s5uVEP6OCoF0ZU8sCXY1V5LLq2EFNTo6uaNTcyhXfJdDt27wcyxoVHnVU9jjoWBTJYIHlexs4Fgn7lhn7JW6Bp9PBeX30dpffQ7AX2xflx9Sa0DeHUN9nwUsbjniD9mWcuscFkxxUAVVcWiat4Ss-BpBqyVJOdub_PK4Zynu5r8C0uT5dx3lh0VLXAEEkSNih4vfc2HsmL5w3OgYwFOgoF-S-xH4t9GT_7w8MGgxTVBU8lA630d6tJP4sO_em-MK21rM5fBz8RgT5-4TToxHGoIG1giFAqbPiPj57sc2fyIJLrAtHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=v9WxFKSrLWvrX9boZgbEdp_yt3sDNJ4rrjzZ5nZ2DsmVc7EToZ0_qdNRT8QhGzJXbUWAu9WPAzUpyFhZ07B2FNLPyGMi1TYemDTSnQKAR_Y5MVsoDTcqfLxSkRc6E3ZIyPPo3C09AX0WcdAaomwwRAehdCQa_n-j0aWU6bq9l1cacm7zPkkN3R70JqJAKrqeSJHnTrFVFej6G7qy9bbAFW09jIqg-ZKd788y3-__4hTrjsyMljZDXdz8kUYfVpZB9YOunDSfb4jl-HsRTb5yZ9fll2zQYEafVUTwuOSLuMGlGfN4ugTQ7mkTZguAmovAEmlWaxPl38cbMkxIfH4xg0gWBf5-krI-Eli3svx7c0gnP-rsnHN9rKGL_s5uVEP6OCoF0ZU8sCXY1V5LLq2EFNTo6uaNTcyhXfJdDt27wcyxoVHnVU9jjoWBTJYIHlexs4Fgn7lhn7JW6Bp9PBeX30dpffQ7AX2xflx9Sa0DeHUN9nwUsbjniD9mWcuscFkxxUAVVcWiat4Ss-BpBqyVJOdub_PK4Zynu5r8C0uT5dx3lh0VLXAEEkSNih4vfc2HsmL5w3OgYwFOgoF-S-xH4t9GT_7w8MGgxTVBU8lA630d6tJP4sO_em-MK21rM5fBz8RgT5-4TToxHGoIG1giFAqbPiPj57sc2fyIJLrAtHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxHl7oV_PahXnoGnswOMW7VlHKhRYp5cIOJ4qJRTtMuhcwhTgW-vp08GOxxghyIXpv31R-_3l7MWoRHB0j1rcTs8Efjzg2Zo5BCt1A_MERaqqoTQ6ySRiYjeNkqD1-X67Pig4LhSfETbKV2xcfva7myfcOE-9qCJ8p7WEt8TnD1m_EU-uYxdHLVEd5qAhwJdvJ7eJ8XOFf_u31i5c7CzHY0bTv1R0wh06ROoBQYnEd_cWAAnuj-ydB6U-JbPBmyFqFCFKFiAcvuNqYcMwaaDo30c3o6XgeYB6-9CxwK_WLsbqKGFhz6MKMqd6oZ8b3QEQb2a5EDv4gViuC7-A-eCTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTdq-XPJeJkZZIkDEx2nuqFLv_0TGExOQ8TMYZNlglS62kGpECnkAeohGi6CdgF1JSVM_PmIXIw--MDTBIe1r5J-3eDIxMRFCxFdYk3lRO8T6mFhryTVUAN-e_45MoQ3Q52cnbzB1hdXH-GKwwUO0MO9i1YzdLdH1z4-PbUhtd9oZAfF1TrS-wZZxEzrGxcym6cqvqpgP3M76vLNuaiZ5vAX1vzXod2wuI0srkzeZKqx4Lj0SIhDBE35ccddcazqOXT5J3Iv1Yk3rK4NDEIsmRD-wpUlNE6nwImDjj-xybYre8edDaapGDHSS_kdPrnLcnw2vlRs2GxPNPdxv2GEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=P7JVjVGvqUKq_p9V4hvEumXuFj_4-dOmSYogBfAh7NLzw9UjyS5541Vb6_9fT98joHULpK1HseMF5PXqCLiL2FwWyTC_d06gexFUNGShcdEqzFFW8icFZC9xpJ3LIRhD_z3jhZ8uiZHrSD2u3yGl3hoIDejV4uaFZ4La6hgV8R5-R_VB0_tapyvh1hlk5M2sK9381Mrurpvz-rhAWNZ3Y1S_Uijfo8iDLMX5EtVO4t-c7RWyil1F8y7n3u4n8-4r0oEazwP0wLCGdAPx3lr_w8EFDMtEXbEEFRUlfsCZ7CwRPNZY-O6G7-7btZBzJZrGm2iPLYrdHnCBJlR1h6fDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=P7JVjVGvqUKq_p9V4hvEumXuFj_4-dOmSYogBfAh7NLzw9UjyS5541Vb6_9fT98joHULpK1HseMF5PXqCLiL2FwWyTC_d06gexFUNGShcdEqzFFW8icFZC9xpJ3LIRhD_z3jhZ8uiZHrSD2u3yGl3hoIDejV4uaFZ4La6hgV8R5-R_VB0_tapyvh1hlk5M2sK9381Mrurpvz-rhAWNZ3Y1S_Uijfo8iDLMX5EtVO4t-c7RWyil1F8y7n3u4n8-4r0oEazwP0wLCGdAPx3lr_w8EFDMtEXbEEFRUlfsCZ7CwRPNZY-O6G7-7btZBzJZrGm2iPLYrdHnCBJlR1h6fDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZd0xj0IkzvVnXFB4pMf7cjiltY5omDzL9HxVy6zlRnjeeoVxTNWzTU-kOVBRY-0YSZnEGzFQZrsZSm4F9WCeIVfiRLaUGkNYHc_3GKzhecIDMRpNWo0LXF8uvx8l8HAUFWTsA_XjLR-ngXTA_McdIbyKuHkHFxrGkFrOe8DfO-MkiZRxOeyMgoPLu4JUbVAH12wUQFtPbMeCpB9ZEpj4bT94zWxAcVwqGf3-2EM-mZSzVdf4JL4sy75-R6NPKLUI9EHW-WbuGloY_PNqq2zjPiSFC2GVxktExZM0GKY3dyWqzzDHxmAF00KRFajLLSyzZxB89RQKq8xYsA7Tfie-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRxpSpx0K7NXN3NHPYgh2aIXeLiQu_ZwqE9zCtBA-qDP77bXXUyvya1lucTVct1lHhFuF6OR9_MArIsZQXoP8bLrmHQfMuJBX7o-cIi1lVPXbnp-HlN_nYO_KqHepVg4lKA_Yu4RZkjT8POifq1FheEIBCRkpGoR8pnWBbXh6UDomEDfnuK-6ekEhLUv3BKpUpVAka03T1q4c_3So1d9uIMWnR2qLtFZblQF8JGD5W4XEqLvyUzL9I-L95sXoDIXUzOXDx1MjNsNEbxgJiTG-_Jx2ms5qbl3KTWnopOu4N4ntMTVG7b-DGRjb1gqS-y_Yhs_cgQjiNgaWyfdgUrT_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZdgNbPXun01YEOP2mXMiIgrec8wOBcRIH0MiKFdxw-r22C5nNUUzO-vwyAmQGIuQOVfI9k7P5tl2P1haURoB8EI_46twz5mlUzvBG32C3pca3ITTMQCCoeDDZ03soIJWjXqqQ3Cv4bMo_4PIAymEoewldounK5Asylr8byPUzC1aTbBUp5vXsFH6e--zOZCXJjtP37BT6zWcZPcRqFJZ5QX7icOpgVGF6pwuMaClErkzR9SjaMt4hGSwg62ARCm_IAGS9hwO-Dr79-4zCgSACotbDE3DzO2yoCReP0RtoSVkRbv_ToFtKtEAF-0zldGItDZSYDv4CBAm0IblfpfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I1LEH_p6kLuLko1PaGY6SqSTkHA3GVtVIpRETiTXgkpShsop4UogSULLvSvP5iu7yaNANsy0vgqinmFpTD0APPyrQP7IICk8i9--T6gv291loBlkoLx5Ju55ZR_gEfXiSdqoSf3KcUq8Btm-0i-JgaeonUNQ3mgeDe0uhVC7F6A8ctJwCvDGPNlS0c8CYnkCtZZxJH53Z5SWJCT5KdW6A89L_kCXYa7o5zdON0ZVKUjxFVkESVROoz9OiJyjr1Rwey7xypD_C8qjSnQul4WD_g7CjhoP1mvpebz_wt0ZOTOcB2cv-9-7vpzneilqJO6iJZJjCVcLQOykqsOuTsoF9ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I1LEH_p6kLuLko1PaGY6SqSTkHA3GVtVIpRETiTXgkpShsop4UogSULLvSvP5iu7yaNANsy0vgqinmFpTD0APPyrQP7IICk8i9--T6gv291loBlkoLx5Ju55ZR_gEfXiSdqoSf3KcUq8Btm-0i-JgaeonUNQ3mgeDe0uhVC7F6A8ctJwCvDGPNlS0c8CYnkCtZZxJH53Z5SWJCT5KdW6A89L_kCXYa7o5zdON0ZVKUjxFVkESVROoz9OiJyjr1Rwey7xypD_C8qjSnQul4WD_g7CjhoP1mvpebz_wt0ZOTOcB2cv-9-7vpzneilqJO6iJZJjCVcLQOykqsOuTsoF9ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSkn7vxS_dZkczGNW88tXKECS23BDqzFXhECrI72xUyWrRqsSTYLBlOQvqJmuC0ASjjpno0lGtS-20x4FpBftz_9RPSDAOJVSF0NXnHc4JzY2y2H8UO1rnhApR6BwoEAOXVaRUlgP05LR4M7UEzWD6h0yxAdI-q6M8OVJYvfDt0RmGyBKCc9Gs0Q0j5b22Qg9EBGBEZVluC0ipLKeOiMhXIIoznV91oArPNIukIAPXd6ugpAb7onWKN1mVlhF0jJuw6m1-ftOo8UM3bjwsAvsAKGtYI47XK1Jv-oZinh12N5aGyYS3SWqQxNbENCnyFZySKSGUJbM5MmsflTl-YyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHlhZ4ar5GgFoY6I0xIkUmLw9Stb2-KyrXIBWiRcOXOWzK8xtWPnrnLxxrl0x9W4n4EivpuTmnL3SixBKh58rac4nYCXPAuXagHPdtoQSbcUZaF4sXNBTO-l53VcEfzJ_xMlMnAcFpjIYKBf4ueyEf1RqGbGe8ql7VUT3SW1J-mTPsK3zFr3B_Wv6gE8TkTD3Tk_6FSAW9eVTghWTbnummQSkbhPcyxOui388ugPqyeGr1aRCUFoHxvmvKyWlBjl-DeLVVKgqK3uqAg3FNEJJEI7s4RsIAqP-JZenK6cFIXt7fOX23abqG3W-BMYuAioZg38TNFoy9yAettBouDEvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=PkuoUvAQA6ML_KQ35iSkLANBsdiDIOxzevalxXXHBGV86Ae1UbC3SIq0tCs5prqYtOb-iQX5NmussrrE-BabMuzvy8YyDwU2UVjVfZRycMGY4WuktjvmctACpPutcnXcwFjW7vVDGNdQpc45HEE_9d-hLZ2zIlN6xbA4lE44XcGFGCau3gD34Kwq5MRFwn0zUHhZsR9ikr-M6kkhpo8kFsuiDft8n4enSjDbfXJw0WSm_la6ApDiQyGdmCeiPTsYnwmMXZYImDtlWcyu9PRCQFmirT2WbepwtRCTsYvJL3V8DdM58JKurIgBtTYTRrCnBRVwkXhkSzD0WRCVaEEsMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=PkuoUvAQA6ML_KQ35iSkLANBsdiDIOxzevalxXXHBGV86Ae1UbC3SIq0tCs5prqYtOb-iQX5NmussrrE-BabMuzvy8YyDwU2UVjVfZRycMGY4WuktjvmctACpPutcnXcwFjW7vVDGNdQpc45HEE_9d-hLZ2zIlN6xbA4lE44XcGFGCau3gD34Kwq5MRFwn0zUHhZsR9ikr-M6kkhpo8kFsuiDft8n4enSjDbfXJw0WSm_la6ApDiQyGdmCeiPTsYnwmMXZYImDtlWcyu9PRCQFmirT2WbepwtRCTsYvJL3V8DdM58JKurIgBtTYTRrCnBRVwkXhkSzD0WRCVaEEsMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=qyDtJ4WXVrRqQTercl2zMnf1684-diRHfAHMX9iNmn-dAmQTtPz5KjHEuPArA1ZAvwSXc41_v1nRwdrE90mTNynyiaupoXGLD1MYS-tbAUbgE64xIaBXFXpkvkZ7M9gKRJEmK_tpef7pmPiOmseGG9ui3P1HtiZG6yFPiutRQ4Iyw7dSiBJAyUYrBBobyvCLsf770TMorV9iRX4DeRXTzqYGXjTViiKjq84kFChaXcodS9-CrCOMF4HbgKiNBNy2Hu_eVZoj2nIfU0KEWYHeLSDyS3ppvQqWlYv0TjHQnV8JgbhgssJut1szCpQ6eqSkVfU9pAkvn_TEn34VJ_cprg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=qyDtJ4WXVrRqQTercl2zMnf1684-diRHfAHMX9iNmn-dAmQTtPz5KjHEuPArA1ZAvwSXc41_v1nRwdrE90mTNynyiaupoXGLD1MYS-tbAUbgE64xIaBXFXpkvkZ7M9gKRJEmK_tpef7pmPiOmseGG9ui3P1HtiZG6yFPiutRQ4Iyw7dSiBJAyUYrBBobyvCLsf770TMorV9iRX4DeRXTzqYGXjTViiKjq84kFChaXcodS9-CrCOMF4HbgKiNBNy2Hu_eVZoj2nIfU0KEWYHeLSDyS3ppvQqWlYv0TjHQnV8JgbhgssJut1szCpQ6eqSkVfU9pAkvn_TEn34VJ_cprg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koa0YfM9FyUO6G6iiIqe3EZYuNd2fZ5L6WYaq-Bi6ByMcytKrbTqrgMTZfL0zoQv89kk_7AyXCNz70W3dYEPiThCkMhiaHX7q-LLXm_O1wYgkrbCP5pXlx8NzZghA-0MFwWRMjUHUeXhySW2ed2vn3j9qnZWAlFPpQeFVJ1e_tLG-Nrt13SRB0zkkh39aIL8YMT04YMIHLdc-0WJVgtU0XmM8lU_Zi8HqdL28JTQt0OOdGdxzMx8aTFFqv3GJgOSk83Rcckav3Kdi7Mxrw2Rk01XRl0sZat43IE7BeWawjD33I1F795KfSsUzUay2YSPxh6MBf6LHil6GHhWhyXZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlBa2sTV0tStFj2Apgmgr6SkSE-Gz7vQU5IXWg0sNLWYBDt0JKRPjiO_AsGW6oA6NgiHnnrmig2voR2XiHZY6oShaDuCuf7bAzoFtcN7HGDcMnUwOAX5RYiVD6qcP1c49TTAnk7KSpi6NykHhQST_-t_RwzFwquNRsmbF_z4nReQ10ePKbDBsZKps6SK1hjzsD0BRmZBTANy2zw0QHXnusnzgHDpWOP8FnGbTpw_-M3ghI9keHn1ZMx-8z3sCcma2wmiwLpIYTA3DNJDA8v4S5yT2T4wnlAwJ-1EbeQZXJlWcAfWbb92c-U4BqPnFWN-VWK--mHRq-l1-TiT-oNfCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=ehRQXWHAxM9FmAer4iIXOMnw-tCFAxLyKDXaXg9ALT3Td3wp_aKwyab-_38a8zLicivQCGLEcBk4kGwGiMV7_QCk_Npbx06a0G6ZXIHGDSUrXJHofpQYiDLDrmNnZ5-wjNcmP95OeQY_7kHl-hBm1F1SgdBWck78gmEqT0hPTvy8DCEPwVNR4yNrLZzq02rU-TK7eZB2YszbsZ5dMnpsn9AaacK5vjZ0hB3mbJToIUZhvu6dimbIz5TfTghzwq2564m4t8wNoEMshIb5qnYVIZwLBRTjnfAf-a7iLewRo1HZRQd3UaYh0qzgyUu0ATLkg42DlrCCLttYoInG4H2C6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=ehRQXWHAxM9FmAer4iIXOMnw-tCFAxLyKDXaXg9ALT3Td3wp_aKwyab-_38a8zLicivQCGLEcBk4kGwGiMV7_QCk_Npbx06a0G6ZXIHGDSUrXJHofpQYiDLDrmNnZ5-wjNcmP95OeQY_7kHl-hBm1F1SgdBWck78gmEqT0hPTvy8DCEPwVNR4yNrLZzq02rU-TK7eZB2YszbsZ5dMnpsn9AaacK5vjZ0hB3mbJToIUZhvu6dimbIz5TfTghzwq2564m4t8wNoEMshIb5qnYVIZwLBRTjnfAf-a7iLewRo1HZRQd3UaYh0qzgyUu0ATLkg42DlrCCLttYoInG4H2C6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=dVX2MLkCaKHd7jsLUwijbBEDzAHuMilZoTBU-OZOYfBngM3I_zTKM7D9fiCE8ECMzERA71LgONuo68c5f9DXQS3MwlcBrTyA4voqBudiXvQ6VDH06CvN0SThzQ9M0EaAuJI1pQm3sQLrcfZ5qnW983IcQhEiWapphKt4EZhAQsEdIdTE-3Jk9IDxBkdMVmReE7NI_6aOxmvJy2JxgjHmmSfcUHkFWYpaKpm4Z13k7rb5fqMP-QdYKb5lLjTFRLoFh2o5LvPIDVgtkhv_Fam3XlsCKVKWMmaMnrKnC9RbLR1svMxA4DSrNnNR9t4xEMX_q8b8nF2C77HzfbLmus65vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=dVX2MLkCaKHd7jsLUwijbBEDzAHuMilZoTBU-OZOYfBngM3I_zTKM7D9fiCE8ECMzERA71LgONuo68c5f9DXQS3MwlcBrTyA4voqBudiXvQ6VDH06CvN0SThzQ9M0EaAuJI1pQm3sQLrcfZ5qnW983IcQhEiWapphKt4EZhAQsEdIdTE-3Jk9IDxBkdMVmReE7NI_6aOxmvJy2JxgjHmmSfcUHkFWYpaKpm4Z13k7rb5fqMP-QdYKb5lLjTFRLoFh2o5LvPIDVgtkhv_Fam3XlsCKVKWMmaMnrKnC9RbLR1svMxA4DSrNnNR9t4xEMX_q8b8nF2C77HzfbLmus65vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6EgBT-1spyJxgvg0071eBSUIOePzYOv_x2pcyRLgsBRU4EVwgfYFuDg6jb3BoBlTLznoD-eRdJTAKkw0-ApwrHmyhUmCtT0buXypW6JnrLgzZFsB_ICdUlF-fVLLAxDvfztj3PC2p8Z0JwDQ5fJDcbXeYAQr5E9aldnDOMSUcR0tRcOG1eN3rifZcHwGxr76SgvRAuSn2SgH6Mi7po3Iw3aXbt_ThULjSk3HvGDdCNreY0E3ZxWCjFBJNGXzaRs73ZPSGZy4bNROx9LsXKq0nOHKISD2fbqQSRMym6RQgQSLS5NHXy_NEcT65MKret2MzQjhssMUYwhQMTqqbB_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMjIyRyNab3VOicmp0wF8WragFlhQ_6AXCV3ssVcmH8IJxw6mFfWnWpwKaub42PfNBY5plfX5PP7ifoaHP_1f84YSfvCIjKIaGf4M5Qan2ADee7_Wn2hQA6nXLuu9_2CsWYT7iLepSEZraKTDycd8HCWD4Qf7LdElB5BFJSumEzQHA_c1UHeMeOIvrgw929CY_E42mOznG5wzxRKDZRklDLv96NjOg17fZqA_A5LGIP0_7txtfkJu3vn3znArZ0Oea4VIQJa85JjnjJKt79KaLj6KHZLcUE27gz3vg0ToSfj_DlFDdzPj-PSzEQoF5elMSGLLIuaTI2RKY0gqrHuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIMZ_zWaFL8eI42RUdi4oF2t382e8LlK_pILyNcFuO0GgqPn_wu8vGwIkQqEu93z9w-rocQ2HAvduQtFwnH8xCMLx9_EWKOYc_ZkUt3IuThptJDPjoQHM0W4yHMe4q3_jvDvxj-vDpJ-faUZQDQzpMWp5UHcNEtfVd_eFFMAnaNGU5afx5bcoqD6GDHkJYAwBM0Z6nexmWT3107IUJOGDzrFAEQan7VjacAJJ0tuwYVwCEe2IJEIX3XRyEVMu_UrUctGEvtWsomcoBe8RpQTFZSINgaGgbAEbsZ57lXUSp-fTR1cNkn2z8UahrqnjluEwnYDZRgTfHU9G_HJ_ihbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grlY77W1GackKxE_PkoUAt3RkQr0wBroGNS9QGCTraoYpAe0Rxsw6GwpansqT0eWZScp1GJgWARwLjcjb_z1RXrmolH7goIa0Jzd0mAjOU9Fndz8lqYaphfrdB5jgFC3_VhzHC_7uCXGNw3iZws9Zioptu5LiTISsv4yMXEinCIbtHM4cmLK7JuHy4kgGq3EmvlcPHf7YqbLwebiTgKnEiIyMN7fmTD9jTesJlParS6ilemh-L_jnD0ZoTWz9Bxm35KgwpIBpKwjmsKEIig1HDbmRMiv2Y0pLb4v4nsKz__5_1ys2RcKZBrnruvlEQTC1_PpsXwrycP-_GWBSdbkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YBhN9Tz9nrm9tVpAzy9gCHMYMwuEfm6F6tYh7D1cAt384K7T1VS3DYMkaixmhKuSwIFAF92_1ojgsZKnBlJWWyJ4yhRbHRqMAMonlDe66Kc0pbOMa48UmccSEyy99Gz75aim-HItsO3-0gRa1jWsN_v5wExhSlrz0RBno2ej2nTq0ZaZ1n6ycBVWhydrRgaI7JHFBKUQTqHR-JdMkRGVgk8kYKPuElEnc7a3v7OJ-_4oEAzeLIFDZnjqJ8CFVofKu_eNnBfrsYTQ_OAMjg07KF9PVECZD6L6vgqhBhSorF8RvVeDBVwzPAcVYFXXgVbzHqmToo14AYk7xxNG7RJRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2DKyVZk92HF39J-8bxcWdu0zla0EQadouZhavJCZxPWPcsXnC5WQE9jcpBT_ycHvwR2TzzRmOs5MnFDREBO9tDv2UMfKzrpa5l1xIhlPDEt9WgkcYVUA3db-c9BuWqNh3a4FGNaI0M4sri_OnmPlXA973EqONwOixJFZ4VXHLYjWQJMUXgxh7VxznFiso_yHnyQNCKBuYBrld7klmflxIHWGXP2oPMk4WjX1mjYB_nlm51yoAv6Zo4VPy5ZhHQYdY_O_xmWEEYfMMX-NVzgig0ES3yeJFK61Q9hg7jlk5uxqBE50h8s0-t91Pf-45NRanZUTy_IZ8ylDg_ih3MZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5TB2mbhmY2uhH21UOteZwwzruVm78KzkAyht5UjVWQD-Y1HnBs1ByqMRKfBUrA6DyUGRJPj1h5P3JEUxZ05IowFC8iMG6olpzvZAF8RdQsXuyGBo9G6PmVQMTQvqmP1efJc2YVLieUP_pxu_xpDlJGSnWOXqG78GZYUW8DS5ZQ3mDBl6QLuEzOlR4BY3UGL0E-g2HweiODrYdA-gQ4Xrwzqp2Dz2JGfXckUqBS4XSMFs6uFTlG0VUJFRcLsPqTDJ1UyB8QeyabBZDBXOzbX-6VHO4ItohNvYSyva72BN9z4c6bMymn8sO3Mw3dd0JceFsuqcR62FtvZesLYlKKC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1OHQShcRVpqFWU0qPoNhSrD4spMBp25W9s3CMLyLzsK2ePuF5NPwa1dbNZ92_5SCH51XVzS_rXkPNwgWc_7AZUvNArPRIbcEDL2S18IIlLBcG8zAqAanU7MOc358MkVg__RoR-TIMlOKRBei-xu56YSa8oOBSOoiN2oS17WBA-yOvFBf9sqreudHiUi0HzyWjk7hufmo-fmhMpGVuUH8XE1tnosU0LL4mGyWhB_xlyWhfPSqDFMD8HlFB0wj-ofJjvy1qeliiFlGXHjo6lMsm43SlPUYf8Kk7ARY572NCUxyXbRk6sXKIH6YaTYQ2MmeLxvU4i7cVU72t2oqiUWGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOEjIMtmfkdAr4u6pgHduJh0gmCT1hTcoiOE1lQP5XlnjrDluq4OjoMBlSyMEbXssoOtTyggCjc4LlU_Fe3IXzihCg9lPjtU0gt__nf_GLzkB9TkRO7EEWxEuat7ZU9TsaP5lbRcOtGyKGEv8Dv63QDwcP2FZYAqFlz500y2TpOjpjRlqZbfI5TNH1eBfOdo5hIxtVDY0H29TE01GH6NGCZhjsannhnkubRkNwQejsXhmdMC-G-lQ95gY4ZZeKbbtRqGCfo_C-AMD8oJBch8KPS6j8-BBUnwidvPNRWvfI8eYjD71IMOIeD3JNQFbTC8sKFjt-Mc6PPYlk_GYXI5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9fhn6uUcgFQRYpYAivyuuc645FXVgyhh3mxzRt5RddttM7V_AMenjY2EbF27e-AYBCAq8FVmOZ4Q0oyFny40YLhJ6S6buDtV0BprqLUXNaBRH_K_RG0DleIaoUyU8mombJbo4xwD0d3isyULi9xBBEMK2ZRxkJ5yS6rE0T832LgKoXXhh7BSvRBbzxMx1USZ6SyRBbaZIlL45-QAZ2b14FkkB6CLJYGlOJe0RrTzy3n6_xRWBz9QBAn99YWEFmn33WR8ja-NHbQ_K9k0OQTwq5J14OeZ7rdybwJ5IJDF9_yyG6a0ifTEOk6JRlbQ-Y8YbKvD1MYPHHv0wobYIY0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=tph32EqA1hfdDNTKItQhYVts6_yF3mmpCmhcXsSuM2qKFHFKA6RFyjVxkUPScA-Svz4S4oVS7DqW5AjsFtPN0QwdqlSY8yMMYiDhfZONrXSBRsNe2p7DCHHJKJECOBG2ftty94EpSON8LOMvnwP7FDMDjqAerLbUIjcPm7zvkPZwSmWXsCwL8bzbUwYxJk8SLq-N1jzAhZPsazN6TAfgO5aMRyLTdrp7RuCRZzlbaJgeXykZ2Gwq6ETV2ATHiTIjABC8vyHEGTTfk89VDcv-S_hoiAgsQMNvoaVZWGUvc1Ir0an0GfzANlN4SxrAjkzzT6q_5myHgQ9e3BvX4ovDsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=tph32EqA1hfdDNTKItQhYVts6_yF3mmpCmhcXsSuM2qKFHFKA6RFyjVxkUPScA-Svz4S4oVS7DqW5AjsFtPN0QwdqlSY8yMMYiDhfZONrXSBRsNe2p7DCHHJKJECOBG2ftty94EpSON8LOMvnwP7FDMDjqAerLbUIjcPm7zvkPZwSmWXsCwL8bzbUwYxJk8SLq-N1jzAhZPsazN6TAfgO5aMRyLTdrp7RuCRZzlbaJgeXykZ2Gwq6ETV2ATHiTIjABC8vyHEGTTfk89VDcv-S_hoiAgsQMNvoaVZWGUvc1Ir0an0GfzANlN4SxrAjkzzT6q_5myHgQ9e3BvX4ovDsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=TeKSBVX6Czytc4LP8DhQyCJuYaANaY21Zfq4EfXJh1gAcxz6erJbWXLNIk4EJc_hSiwQ877wYH6vPcQs--V9w6dY1gjZq9pEIhwOwYu8WlxqSwldaNz4y0ILjvQbBlVT77evkQEq76IsFwJilQi3uSsJvkSSWlPZ15bo-e8Wj_XyMZ3BvoTzslQIK86-saBSIP5i2EpkxcCVNpKr3nespGevBjwHkPzXs3l4DOM3LdQedx_nzbLBqvJLR3Tk-np2xAZFLXVmq0M8ZB9r06lgRgrinVzgHGccdu1n06zQ9bQma-X0KgmRhjLkLtiRTx_uHKzCAk7FtCIGoZuSTs07Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=TeKSBVX6Czytc4LP8DhQyCJuYaANaY21Zfq4EfXJh1gAcxz6erJbWXLNIk4EJc_hSiwQ877wYH6vPcQs--V9w6dY1gjZq9pEIhwOwYu8WlxqSwldaNz4y0ILjvQbBlVT77evkQEq76IsFwJilQi3uSsJvkSSWlPZ15bo-e8Wj_XyMZ3BvoTzslQIK86-saBSIP5i2EpkxcCVNpKr3nespGevBjwHkPzXs3l4DOM3LdQedx_nzbLBqvJLR3Tk-np2xAZFLXVmq0M8ZB9r06lgRgrinVzgHGccdu1n06zQ9bQma-X0KgmRhjLkLtiRTx_uHKzCAk7FtCIGoZuSTs07Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=Jgj2F8AkPkHhmIOcBmdMrJd6vuBPGEkl-8tcXuNfRdysshb1Q9a_uapOfnbzgv28i37EPkA1HkrDXmfAjgiiCEmiWW2RZp5_cqFDpYcynQMV5Pr-dZfwuDan2k0Rg503vzwJ8hDzlDK5Te2pAuwh7p-sSkA73sCGAp2auBkWaKMYhNrxmW_wkc5wbFlom2FbmJZnZavRsiPh8eXlORSmfl7It_KIAvA7ZwTBu3L5yQqp9BRgtWnGVui-FPvaSb1oFBNmQ9jX1GA5Tq--AwE_Z0sY_HzkDaEavGqedgspToBxy8g129azBcCUvtXA2PvA1S4Famr5svqlzhlJ77bwaSVl31MXC8JcEM9wh17WGMzjgjrJtNGB6JxutRHVBSn-TCriCrecJObEuL07g8Wl8pk0x1pzuXgxCa_mnYsTVp3Uah2vGKH1xRxgMrXnuKwSVTaMthFlmsQ19dhKOb11tgSPIM7WdXSKXLXMSPOj4kWf7DR8cTV3h7SyVbtfo2rBdrpSxEumd6oB5ddda57nlqfGrd5agW5GK7LCnzvXXrhml9373kH-FVaqHPfl0ik2B2S3OyLpGu2-VRw2S3jBhGDwElf_c62j-xxdLNRzvXey01duk3FZbqqC2rfCDaiQ985obW--hyX5sLe8EMEFSvVsDmgOIVNXDe77vPy-h-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=Jgj2F8AkPkHhmIOcBmdMrJd6vuBPGEkl-8tcXuNfRdysshb1Q9a_uapOfnbzgv28i37EPkA1HkrDXmfAjgiiCEmiWW2RZp5_cqFDpYcynQMV5Pr-dZfwuDan2k0Rg503vzwJ8hDzlDK5Te2pAuwh7p-sSkA73sCGAp2auBkWaKMYhNrxmW_wkc5wbFlom2FbmJZnZavRsiPh8eXlORSmfl7It_KIAvA7ZwTBu3L5yQqp9BRgtWnGVui-FPvaSb1oFBNmQ9jX1GA5Tq--AwE_Z0sY_HzkDaEavGqedgspToBxy8g129azBcCUvtXA2PvA1S4Famr5svqlzhlJ77bwaSVl31MXC8JcEM9wh17WGMzjgjrJtNGB6JxutRHVBSn-TCriCrecJObEuL07g8Wl8pk0x1pzuXgxCa_mnYsTVp3Uah2vGKH1xRxgMrXnuKwSVTaMthFlmsQ19dhKOb11tgSPIM7WdXSKXLXMSPOj4kWf7DR8cTV3h7SyVbtfo2rBdrpSxEumd6oB5ddda57nlqfGrd5agW5GK7LCnzvXXrhml9373kH-FVaqHPfl0ik2B2S3OyLpGu2-VRw2S3jBhGDwElf_c62j-xxdLNRzvXey01duk3FZbqqC2rfCDaiQ985obW--hyX5sLe8EMEFSvVsDmgOIVNXDe77vPy-h-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
