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
<img src="https://cdn4.telesco.pe/file/h3vM_fUKgUKpaYxbpR4uK3RHcnHD6gfZFd0MdUIGVbVKyiPCU1QOIJlRPfwDa3Cl7pSzNGw7e4-PTuGx6moAxfaKLlhxqipOaMScn6vU6ci-B_ievdr3zyha1HTl3bVWxaEUB7Vi_Nk_2G7z4YtzgvvfDPpuOYAdio9ff4uhIxYUGszKBNcB2nDbOhNzhnzdfZCocpZCenho0Qyo6We8gONAvMo2IXwbRopfcQK7MOr1CCTLD1xAZSKwKK9wLOeo2LevY_38PzUKankYA9mZpkigkaf_MqpWTxfwT46w7HCx32jfqMA8h06ZtwTCe6xal9Qy00a5E_8ypvGCStsQzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 07:27:51</div>
<hr>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jhADblqcx_-IfzWpUPgHlIimFk6IHNkcn1YrdwHBMoxw_lCSZeF4Mrw6xc-AYBdXvSp5uwBYJ2W12BS11mQcpW5ZFO_gKMe3CaYScdXprfMbgmwzMZLy-sd--V36zMpkRqnRjLWGY4IBeULOz0iLCO6Urpw2wrjZOhacK5fba_KUv2JAXt5-gkm2yjnEED63ECkv6vkhvmGRjmC3Fcqjy8OachSz_FbWjq0kp_uak6Fq61qzrb0AiD2fOjYiHYIh-z78R8THOIDd3ZS3tHOi_AoRf1gMt-1AwcIl46EcNFvUYpSGp3xVa2lkvGUsL_aOEdTMG-OLOlB2CPpfhCjqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=skB2kOB7AN2gK18uLzFBUQaqIm2ZhjZPhVSziydyV3DI-21rK1nOEUovzTcOU6j96qmei3T6tnt218qnKsUsBmnWpp5kpDxRLKzOxp1tTvCvYKS_I6eNPwwyr54rVghvo8GLRk15y5vGvhGrUKRdA11U14DjJs2sHiDvwPbEWS_EGb3O2umVCeBwrsJ5dpfsmxY81tQCT_dz0Mga9jJBkWk2lekHlPY6r_vvCLSf07SXqh4rKO2xSVFfF8z354PEnYUpIF7Qmg-sdV-l3rRI5n06C51KW7dXyCfjVJZfBGTV7BUGl2BWdqpOT5p9nHu3LWWy00PA1HZGv-w4mwOBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=skB2kOB7AN2gK18uLzFBUQaqIm2ZhjZPhVSziydyV3DI-21rK1nOEUovzTcOU6j96qmei3T6tnt218qnKsUsBmnWpp5kpDxRLKzOxp1tTvCvYKS_I6eNPwwyr54rVghvo8GLRk15y5vGvhGrUKRdA11U14DjJs2sHiDvwPbEWS_EGb3O2umVCeBwrsJ5dpfsmxY81tQCT_dz0Mga9jJBkWk2lekHlPY6r_vvCLSf07SXqh4rKO2xSVFfF8z354PEnYUpIF7Qmg-sdV-l3rRI5n06C51KW7dXyCfjVJZfBGTV7BUGl2BWdqpOT5p9nHu3LWWy00PA1HZGv-w4mwOBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=pOmV6pv9zT2f4uK8rPAqPwElMW8SAXR3ZB3zdJlRpA_Yk-fNqOmAvsQ9wgve_1yRhDQLOVyPJA15ey6Tb1Yv4V27B-sp-OKoH5yvwi9hqMkM3HWZ6nXbdpOKJ6k7xePUO_0uJ2vsNDR3GxDdWa4ZEqojXR33XJzadBEd6Ngo5hbr8YAX2028sbR5i6WaeA-AWqx16RG7HkJ7zismdU-5RHfYGaqZtWI9G7mwhDQ_iVdtm_vE1h-lLEYN2uQrHXabaztRppFYGjayA6b9Pb6aaH_nDvZEmj2lBigQJKs9mMF7B1T69GMiUhk8In65rq5XuDU62A_5G_eM7MOUHBiMtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=pOmV6pv9zT2f4uK8rPAqPwElMW8SAXR3ZB3zdJlRpA_Yk-fNqOmAvsQ9wgve_1yRhDQLOVyPJA15ey6Tb1Yv4V27B-sp-OKoH5yvwi9hqMkM3HWZ6nXbdpOKJ6k7xePUO_0uJ2vsNDR3GxDdWa4ZEqojXR33XJzadBEd6Ngo5hbr8YAX2028sbR5i6WaeA-AWqx16RG7HkJ7zismdU-5RHfYGaqZtWI9G7mwhDQ_iVdtm_vE1h-lLEYN2uQrHXabaztRppFYGjayA6b9Pb6aaH_nDvZEmj2lBigQJKs9mMF7B1T69GMiUhk8In65rq5XuDU62A_5G_eM7MOUHBiMtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=V0GAlOEIq9jq-SEJiXwIGSy99YC-37u4jDgL64fTIrEOFDX8qfM04qqd-89gx7Zds6G-dacLDMqzejIiRnnvSinrm0iEOF61fbRie8h4K8Enix46xjReMGOygEQ4By5v6bgzNZSLXT08ezooJk5XI6gio6U4AhkJr6vS5MoFzHWs-wUz9hsgpJ3-I7G-QPdGWoSAjv_4oFlqAkYpeJkJkY4zyF_-yo6LIqNhnh9zD2HUUVgR60NF6ijYIQp_2LfVWrTUqYgSq4TTVBJcr2t7HjMXLc9nbqwk3Y3gQS4Hm0CVKGnjYLFWfBRtkRCKoaWLFw6HA8W7KYHGhjB_UBwGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=V0GAlOEIq9jq-SEJiXwIGSy99YC-37u4jDgL64fTIrEOFDX8qfM04qqd-89gx7Zds6G-dacLDMqzejIiRnnvSinrm0iEOF61fbRie8h4K8Enix46xjReMGOygEQ4By5v6bgzNZSLXT08ezooJk5XI6gio6U4AhkJr6vS5MoFzHWs-wUz9hsgpJ3-I7G-QPdGWoSAjv_4oFlqAkYpeJkJkY4zyF_-yo6LIqNhnh9zD2HUUVgR60NF6ijYIQp_2LfVWrTUqYgSq4TTVBJcr2t7HjMXLc9nbqwk3Y3gQS4Hm0CVKGnjYLFWfBRtkRCKoaWLFw6HA8W7KYHGhjB_UBwGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=enpSl44m1ZaFIt0n5K5rEm7JQ0tWY99TNlCqghFjt1XBVmSRZWwJFkwAvFrz26_iPkwpyPqO7wl5Lkr-YdNpK9lnIBkJWAVkcsIbkm1yUtJ1-d_v31pPvGtUVd3Y8ADHIWO9ptLwrMzQnA4_9zxFNkuUruHRU5j8NwaVzW80fyAAgt-SgHIIRr5xrh9s-7TfeIdeQeepb4_Qc3AKQMpAsF8EVneApAr5jc3PjpG8KfrVEOzbo6IekGW4dXj4ttcPrLskobAO9Ut4VdCIiCGEo8h04EUwHpY8jCvrF2CdQcuXAurMH7bRhCqukoLG66H9jkV6-RkxayVM251VB-PSYB7BW4uuTsDt-KEHZrntFA7KdmRnaWsNZWGqfNeRvVJoSVxbZg0KvtWNEShbZ8uZ7xCEevT3g59ZaOxSH7tx__9nSKT-PpEQZOPTK6SgN_l3eO88zqp5fSKWiRk62KJf0k6WTbRSpkhxNZo1JNINdsgMKn92OrIn51tFzAQUPHF7QWG3HhBZLBF1dqLQsi7RKnPxrx2hnMp57_gU9Ix4yTNBg1Cwgf41BKdby3OOsgBObblxCWsNR-iGFMeW2SyzaELwsjXAhZc8vUqHGe-8p_ivZsO9SjsriHqlk66331RAk1gtYI1Tn2UU9P74D_qwo47-3xewyrhA47DqhRp4KfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=enpSl44m1ZaFIt0n5K5rEm7JQ0tWY99TNlCqghFjt1XBVmSRZWwJFkwAvFrz26_iPkwpyPqO7wl5Lkr-YdNpK9lnIBkJWAVkcsIbkm1yUtJ1-d_v31pPvGtUVd3Y8ADHIWO9ptLwrMzQnA4_9zxFNkuUruHRU5j8NwaVzW80fyAAgt-SgHIIRr5xrh9s-7TfeIdeQeepb4_Qc3AKQMpAsF8EVneApAr5jc3PjpG8KfrVEOzbo6IekGW4dXj4ttcPrLskobAO9Ut4VdCIiCGEo8h04EUwHpY8jCvrF2CdQcuXAurMH7bRhCqukoLG66H9jkV6-RkxayVM251VB-PSYB7BW4uuTsDt-KEHZrntFA7KdmRnaWsNZWGqfNeRvVJoSVxbZg0KvtWNEShbZ8uZ7xCEevT3g59ZaOxSH7tx__9nSKT-PpEQZOPTK6SgN_l3eO88zqp5fSKWiRk62KJf0k6WTbRSpkhxNZo1JNINdsgMKn92OrIn51tFzAQUPHF7QWG3HhBZLBF1dqLQsi7RKnPxrx2hnMp57_gU9Ix4yTNBg1Cwgf41BKdby3OOsgBObblxCWsNR-iGFMeW2SyzaELwsjXAhZc8vUqHGe-8p_ivZsO9SjsriHqlk66331RAk1gtYI1Tn2UU9P74D_qwo47-3xewyrhA47DqhRp4KfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7AvCv_PpXyOpZ1OhHftVcAqTR2gGUOFk5ok1UlFF_3b0woVLToo2gd6XH_CZVVh9MnxSIIqncx68J1rcLpRisTidybVj5Rb-mPeBJJzY2fVmiDhn-7OesWyecFheN5vBCTGDLye0oF_plGIU2cTIc6ZHXKtPtpB1sJTcHvnNwYIl1nzFlTaQtSOhs9HVeIu0XPLxMNcqEweInJUVj-gr1MeFY-63DWgb-pOSre0GIguPG8YSgyhnPAcf0LGcZEZlC6a1G5zd7i0mc4kTehAcr2S16i8ZP-uvkxrEwYDzigS7upM-mWGiSHSFjCNN1qJc4H1y2YQBRQv3ducR8_wzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IRgMS3NMtSBAkJeRBFZUlzZx_IE53OIZ4cOCYWYlHpI5oNKiom6VwWr6hUrjyAme8rDOjz_hx6vyuwgy5w3pCmcxE4DTEES8zuYf9uraAy6MP_PGJ9VgxHg7sA5m9pKdbxutXQc0kvbUEjasDiu0NWC9iG8gqSBQCvC82LD89uh53X8vUP24kZkqkF1WLGG8_COdzplBGp8rbIJD8Fiko2LyRBAb3hBmEOBp6iJexwiSlFfmEI39rNbYKZwSoki_16yscuZgNUE_UP4_FenjEWSe-K4m16IMPnsu404abrNBRhMa9Mj7tFyzZc0Q3RIY25MqMgYmfbcShbE_mY8rdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=m4xis0tNkJH4KtG6lTcVjEf5602uOUyW7GZ-WTJPyH9MgpiUFrv6_syNKnOnkh3enamdnNLd6XzMvNMR8Jkya3gPcrON6cI6Xp-b_nmsoggSqXkrzAYtkwPu943_pgLIVyE9JJrQkzpcinzqitg4TnRdncUq6o13VPSoOTRj3vxaTDyZzXuYL839GrLFQmvVPRG3bKQel4JwD6BER-az3UlcmnIzgH_y4A7AFk9RELJLf4NSu6jcwmYUMDJhPBzjf31_4iVA6Nm7w8VzxGhZvdNmMPWtBlbRJ5yG18_154SuHi81QYwlXlHp1vhcqDG1QA72rqbgOXPcdCwoJfy7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=m4xis0tNkJH4KtG6lTcVjEf5602uOUyW7GZ-WTJPyH9MgpiUFrv6_syNKnOnkh3enamdnNLd6XzMvNMR8Jkya3gPcrON6cI6Xp-b_nmsoggSqXkrzAYtkwPu943_pgLIVyE9JJrQkzpcinzqitg4TnRdncUq6o13VPSoOTRj3vxaTDyZzXuYL839GrLFQmvVPRG3bKQel4JwD6BER-az3UlcmnIzgH_y4A7AFk9RELJLf4NSu6jcwmYUMDJhPBzjf31_4iVA6Nm7w8VzxGhZvdNmMPWtBlbRJ5yG18_154SuHi81QYwlXlHp1vhcqDG1QA72rqbgOXPcdCwoJfy7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=Pwxb3rhip5iRBX2OqYsBNyavQqLhTnNlRteSjnrxPmllCHJxbg3W568rPvhNr0jsqXkAwsMULadhHSj-rZGtkxFZj_X98PSYisDdBsPs7DYvidzg_0MZhVE0kzH7S1JAHtXjt4YX03qKDMDkwHokhd2sCyl5eUo_ejZKJewh9hT654fbiQ9OuD14H3znSuVRI7D5MTPGqNSs4TFxRM0DwSSpZ9t7yOkmUVU61nVgnatfOfgesBvM1pWLMKPD_0_hI4Lme3E-0Wx26NrrjkelWvI9wmXntDgzc4lCTni1RF4rPnm5yCIlyuKx9Q_gQvEJybwM9AnSv5KcAfSFy0wUPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=Pwxb3rhip5iRBX2OqYsBNyavQqLhTnNlRteSjnrxPmllCHJxbg3W568rPvhNr0jsqXkAwsMULadhHSj-rZGtkxFZj_X98PSYisDdBsPs7DYvidzg_0MZhVE0kzH7S1JAHtXjt4YX03qKDMDkwHokhd2sCyl5eUo_ejZKJewh9hT654fbiQ9OuD14H3znSuVRI7D5MTPGqNSs4TFxRM0DwSSpZ9t7yOkmUVU61nVgnatfOfgesBvM1pWLMKPD_0_hI4Lme3E-0Wx26NrrjkelWvI9wmXntDgzc4lCTni1RF4rPnm5yCIlyuKx9Q_gQvEJybwM9AnSv5KcAfSFy0wUPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=A2aVlhA8ss566fOqZQV6NrVdQZNcxDOsgfN7i00hs9lIZdCGKNc3ZqNbGcxu1UadwDqUioclkfY0FLXYj9G0T3CC_NA1DkAOOULpZ8mxhkP6FmlO1s1bGtc-RUIrtMbqpJGnkR-isFn5v5cr0QmOYuubJ37QLXR4zjVXTnKuUqqbipHJFcKnT67RhrQGcRGYjR0PBRCNCPr3x2_ZaIcErj5aYRPZl-kZlgYo0-Kl8zLIwEM1a1da91aTRq3UM_MwRoV_KbLKrxsuRhdg981Z3T95MYQy-piUwNOmgqz3bk0_Gle6hsddDos62fGAFXqE-hXpCvWoH_viPxwbR3rg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=A2aVlhA8ss566fOqZQV6NrVdQZNcxDOsgfN7i00hs9lIZdCGKNc3ZqNbGcxu1UadwDqUioclkfY0FLXYj9G0T3CC_NA1DkAOOULpZ8mxhkP6FmlO1s1bGtc-RUIrtMbqpJGnkR-isFn5v5cr0QmOYuubJ37QLXR4zjVXTnKuUqqbipHJFcKnT67RhrQGcRGYjR0PBRCNCPr3x2_ZaIcErj5aYRPZl-kZlgYo0-Kl8zLIwEM1a1da91aTRq3UM_MwRoV_KbLKrxsuRhdg981Z3T95MYQy-piUwNOmgqz3bk0_Gle6hsddDos62fGAFXqE-hXpCvWoH_viPxwbR3rg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=bxzKzsw6Bj4ewXknONmVFsMLsP8a9jiqai2jB0hQLnz0eLWXBafN7HGbH_eijs-0qAQife1sSGTdAHU1z-a2ERdI7Qnu5SpynfjYZcHFyJliKfJZ_bEypMws-b4QQqD_55aXtylicwmZnHiOIt3X_hvctkX5RR3Yf0xztE-28XgqupHOHnG22cHfwGSLhXA8tXSVTNlYgAkSv1JdOUEfd7ODxJf0Bup_R2CahPw9q7QOlnP3CjkcnxSwyJrbOIk7SV5XZ1_58LtjdTjVgmfY5qO5u9tamK58Hn8pH-wOdZ2dXoTt1jhILPeX2NLauKpMq_eJQODh6ef5BfsyScpqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=bxzKzsw6Bj4ewXknONmVFsMLsP8a9jiqai2jB0hQLnz0eLWXBafN7HGbH_eijs-0qAQife1sSGTdAHU1z-a2ERdI7Qnu5SpynfjYZcHFyJliKfJZ_bEypMws-b4QQqD_55aXtylicwmZnHiOIt3X_hvctkX5RR3Yf0xztE-28XgqupHOHnG22cHfwGSLhXA8tXSVTNlYgAkSv1JdOUEfd7ODxJf0Bup_R2CahPw9q7QOlnP3CjkcnxSwyJrbOIk7SV5XZ1_58LtjdTjVgmfY5qO5u9tamK58Hn8pH-wOdZ2dXoTt1jhILPeX2NLauKpMq_eJQODh6ef5BfsyScpqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf83llMcxzFzCG1JUl28AxVsqfDU6LsnH5QzxyykXH6Za9oDc7f35TmVF1dL2VDcmRg7TyTlj2b_VjROmy7_dBTiyPTHoUTUKBq7-Q_TLSDjExVKNX3uPRJfyPKZwzd5A7kud1Lo6Qj8SekGSjyNyskjlBocDL_eVBo7BTXLLAn4FPnpjLDbcgW_r9uc3m5bEUmohilHLBDTD6GgFlr-jT7aQ8xbC43cvg-nPI4Zr7iWDjlBK_DxBuMyJzArzVoQWSr0tsVZS035zYnpMPnTarzApSwunbhysEbKnspwF3ent2jrzcNIaNUAJ-5vIiUpzHpc0PYBZLXFdTFm1FLtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=ILYYpWdax5JWwEHwoxSlcNlrsoOWAVLPbjE2CcTM3LsAohSsor2TgxuuNFH7ywdbu3lrUzG18DG7PS_ZPN6JrrfkK5G9QboHkzZRmWb4hwKiA1NGwpCAvkCq4n7vqlOlltZdSThnP5xVXjk87_a_2xUafz-Tu_vQ9yeznyiuyADx-j5ltttMfB0T8BfP1LOQWR8tbQw2X_DjzosVxergnMg1ARG8G6N1TEvNvFW-ip_1vrD6KudExelaOl_Y3mL8K23TNKGWcmu8lNyM1qNU-D0ZlWDNZhZ_qItSNK0Jw47OPxUxbShK7pq4884wD0aDN6yDs6NlbEBfKomWEclclg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=ILYYpWdax5JWwEHwoxSlcNlrsoOWAVLPbjE2CcTM3LsAohSsor2TgxuuNFH7ywdbu3lrUzG18DG7PS_ZPN6JrrfkK5G9QboHkzZRmWb4hwKiA1NGwpCAvkCq4n7vqlOlltZdSThnP5xVXjk87_a_2xUafz-Tu_vQ9yeznyiuyADx-j5ltttMfB0T8BfP1LOQWR8tbQw2X_DjzosVxergnMg1ARG8G6N1TEvNvFW-ip_1vrD6KudExelaOl_Y3mL8K23TNKGWcmu8lNyM1qNU-D0ZlWDNZhZ_qItSNK0Jw47OPxUxbShK7pq4884wD0aDN6yDs6NlbEBfKomWEclclg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=XxKrqCvFtvcHdz5NmPtPR8KWYEQMq2jQtEqhQw67M6GsfGrHFsIlAv-9qa59n1uMeBQuw0qYAfUJUQ3JbE-j5oE7mzcI5-Q607X8r-6mx4NAveNeNHEEp8aB65QOdFHM2T3wN6L7vKEHHEavzHBVDeJAkT4ly3lRwUvV6EeYwjnDnOcAXPc1CXs3p83LoQm3AE6x-rgltr2Meoj2ha-RoBBk_UA8cxDoHuNIgBxw3qLTMHEGbYyzN8jOx8Wgs_FupEZLP3eXadH92pfWv2At9cuCpnftYVUEiojyAwq3ywNzBDASP-MNN0Z_53RFQ58A8UDZImQ4cNxc_Qk38slaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=XxKrqCvFtvcHdz5NmPtPR8KWYEQMq2jQtEqhQw67M6GsfGrHFsIlAv-9qa59n1uMeBQuw0qYAfUJUQ3JbE-j5oE7mzcI5-Q607X8r-6mx4NAveNeNHEEp8aB65QOdFHM2T3wN6L7vKEHHEavzHBVDeJAkT4ly3lRwUvV6EeYwjnDnOcAXPc1CXs3p83LoQm3AE6x-rgltr2Meoj2ha-RoBBk_UA8cxDoHuNIgBxw3qLTMHEGbYyzN8jOx8Wgs_FupEZLP3eXadH92pfWv2At9cuCpnftYVUEiojyAwq3ywNzBDASP-MNN0Z_53RFQ58A8UDZImQ4cNxc_Qk38slaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=fsnHCGPqu-ufAhM3lAs0fAuRU390l5uGskFeMMxNXI8vuaBv5LNc77bmxIkMUCZA60qSPJpXnNimVGjqzsgEOLYa-8vVOTtlW7MoSS8O8ubWiPwGzP33b8TzYA4MER-fYaEO8pa7X_I8WeFUfT4buANHgQIRJ0pvIk7K8apo16hfeT3edZlZSo3XQ0I49wdrOBLEOiz77VGCVievlfCoPWeDv1L1nQcwFMwLnHroLrRESm3JracDWs7r5N0RL1CTgnKN4cu7E5IAuZfWaP1Z2yAq41XpDwEPYl70Xxc6J83x3GBdUlNl_9cYbLyQZIq_PXG-SyaU3OJ6NL_1wK50TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=fsnHCGPqu-ufAhM3lAs0fAuRU390l5uGskFeMMxNXI8vuaBv5LNc77bmxIkMUCZA60qSPJpXnNimVGjqzsgEOLYa-8vVOTtlW7MoSS8O8ubWiPwGzP33b8TzYA4MER-fYaEO8pa7X_I8WeFUfT4buANHgQIRJ0pvIk7K8apo16hfeT3edZlZSo3XQ0I49wdrOBLEOiz77VGCVievlfCoPWeDv1L1nQcwFMwLnHroLrRESm3JracDWs7r5N0RL1CTgnKN4cu7E5IAuZfWaP1Z2yAq41XpDwEPYl70Xxc6J83x3GBdUlNl_9cYbLyQZIq_PXG-SyaU3OJ6NL_1wK50TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Wn2vAI8zT-A4J_ecncluU4NSs5gu7FIxXkGaNv3ZXR76uOGtYzGKG5WURI_JPjvBHixl3YhqQ9O79jpt1eoKFodYWj9EAM-vX-Tge0Lg5DCQqbGaKcODic8HtxsGT4RwU_Zn4BAcBG-YpKMzxeVIKCcqOFtnLqBBrRBMYUOROhHyasOyohN6lW1WpmI84XNVZKBAtkrrbwtVgbnRaTcBunvXTRplp2Unbq2-7Vn9LdSRSs6w41DrpfPJ0TC2nxuwL2Gmw-dp1OdAd_iHDEyalZsRWXsYRrZTDDpsR14kTbfU0tdF8XlHtrwcQmQeWv48DLjmbiG_2qU_iEhUpn2hOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Wn2vAI8zT-A4J_ecncluU4NSs5gu7FIxXkGaNv3ZXR76uOGtYzGKG5WURI_JPjvBHixl3YhqQ9O79jpt1eoKFodYWj9EAM-vX-Tge0Lg5DCQqbGaKcODic8HtxsGT4RwU_Zn4BAcBG-YpKMzxeVIKCcqOFtnLqBBrRBMYUOROhHyasOyohN6lW1WpmI84XNVZKBAtkrrbwtVgbnRaTcBunvXTRplp2Unbq2-7Vn9LdSRSs6w41DrpfPJ0TC2nxuwL2Gmw-dp1OdAd_iHDEyalZsRWXsYRrZTDDpsR14kTbfU0tdF8XlHtrwcQmQeWv48DLjmbiG_2qU_iEhUpn2hOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caCvNyyKFqsy76GYzl04zVFmewxcsaej-Bg7Incf45UhzepV-Riz2cAHXpQALWmg7sGeH8DnZbzztcAPlKLWEyB56RDO6uo6OndGVhpHe75kbf0aGiaGd9eLoHhIgjdy3pQZdarP8NUHydkQKqoPR_mEXkGWWG3CqJWaXmSi4Tv6umqsEqZq8JicmxTGTvJhXUAAE-FhRn4tNyE6WxljnVSDSXy0mqMN7mrZqNCqGofxzyUQAsi82iLATCZ0Z8rZfFWDL1HD4kWWQoFaMacymgJeNwiLFYbcMAao6maDcX7e-A9TzUs3701dSpir1g-hcfx74ILCr-_daOb4vc_pTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do2hMvulqIdUaDQY9EXOPIqMEvqmk_yHohOAjHYmeYR2lxk7NU-QWWJtMKK4wrHR7r-9ooiehceB3NlTsvsdvjjqtDZk0o54OdbtK0j3s3BkxevdnWnYB8khkMjWpv66P_3Eq1jr6mscPdTTdnthScLZ5qf2R1gm91UJ5GNRKBAY7WrFbVqaMu3BdEsSX2eAgOKktEWYuzvAbuxAKLg7v1ZS9ZjZ9pA3pwASsoHMsPpqsVyvdx0DZ3A4Zrsoelrww8xzBzzUxE_YH2RxvUs429vPp4OTGkUH7j8qmjdTSYUmWSGzRXuYexV3j_uKKi9VUGTVpNcPoVxIH3xMLe0rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTN8lp9HAn4rgKtG_kdqimJETHVUzWGje00fVLmwunaek8yMPZinYpqBlzqydPJqXJ9uc3KZP5GihvyAlCLZF2nl6iV5YZ_mNm7nIkLHyRdePfXA0S7A6K5lC08Xk0klgwTl8AA03b6HJGbFKgUuQODcicrepMmsmBLhlMAT-vdBHzXspnKGJaNi2bp03oy7N4a1UQ8aUYV6Qg9o8q0pnyBysP4YLj4fbtLEXPB-CWtH-3FaRgEPQ021T_eMdO3d64WitWuVmqHLF7SYVLxTZ1pxwmZERY1Y_P0J_DEFd_BhE2IVIP63sT519-a2xPnTm3goNRmUD_eWOBZ-g9iyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=accH_xErJr1oezP-sKHkfgdZr4SrBnkvBy2JTMalEuvP4aSYAZcrL7F4jUVVD5XlIGego3PqSpa6Ga-4Oi9rtw2THbxaXK70abbWnxeitftisQ4zUWOLi7EAMXQZFSD7B6wTHc_1pkqO1m6Luj7zqC7evg7aBw0gO2jjw4xjaMf_4EO8TAx-oLOFjyaQQnU6OsKj_rVdkHaqMtVWnQ16fi62tjdvjsi5fFf4CzR7yzk9sLpYVo4N2rSUqfX0eDtzHfMyZJqqkzVCHrcc7Q1x32qj4YZ2MRI_4OtDslNtmK4SZ9NAx_Z_Tr1dVW7VSZyABqSlXPA3anSYRxm1nEdakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=accH_xErJr1oezP-sKHkfgdZr4SrBnkvBy2JTMalEuvP4aSYAZcrL7F4jUVVD5XlIGego3PqSpa6Ga-4Oi9rtw2THbxaXK70abbWnxeitftisQ4zUWOLi7EAMXQZFSD7B6wTHc_1pkqO1m6Luj7zqC7evg7aBw0gO2jjw4xjaMf_4EO8TAx-oLOFjyaQQnU6OsKj_rVdkHaqMtVWnQ16fi62tjdvjsi5fFf4CzR7yzk9sLpYVo4N2rSUqfX0eDtzHfMyZJqqkzVCHrcc7Q1x32qj4YZ2MRI_4OtDslNtmK4SZ9NAx_Z_Tr1dVW7VSZyABqSlXPA3anSYRxm1nEdakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn-x7ttPWc_9zpRzCeH1oxNGFxad5rfy02hrc284azN-7SblDg0agTWBm9k9jns41yhlM1erbER8NWCLsNk5s3zGluQNJKbhQ9lYdTElJiT5YQkrJH_x6VpBlq7e-uBTUSJi5ymGk0LcVBM_daBQHQUioALnUjQvXvM8ivGsRkcxo_k0guNhjphZa_iNoU3EfM-LAqDv-TlxAZKfjPI8F2yEsMSRod4SSxWfQEHjEgzq1uvvzwkcPU2ZU1FuYwuHcUrXClE277uyw78451gjtpKDNxA-QwqT7LiXwBlcSBE15YV_00F6DcL-ZJOJZ-Bxs4jcFlcAOUlJm_egl8XyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BflolI967nIQzh_rIdc1T9NSeTeAkRqNdfuopfLs4Id7tlsKomDEcKDTc4LDFK_0Pxn8s4MXwoD2vgYzV_MIMg10YAiuHXkNYJbqASSkr1V6o3sA7Iq_m-YnHJ_6hcqLG7cEV1HblggCG54WecF8bC9rfW5p27dV3RC0g7JINGVWa-ll9SHt3_irK9fZ6yTVetnttgTD3XLDfwvl-W-3i3NbE5ZvJcMhbd7IXBFa909QusL8qVRJTbc_n1gzznDclid4HHZssEk6qCHVl2B2ljDOV5aUxqGshdbyDnA7ST0xODEcWnkKPfwgSXAsby8aOFidrGHzPtn5rhTb_Pj4Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BflolI967nIQzh_rIdc1T9NSeTeAkRqNdfuopfLs4Id7tlsKomDEcKDTc4LDFK_0Pxn8s4MXwoD2vgYzV_MIMg10YAiuHXkNYJbqASSkr1V6o3sA7Iq_m-YnHJ_6hcqLG7cEV1HblggCG54WecF8bC9rfW5p27dV3RC0g7JINGVWa-ll9SHt3_irK9fZ6yTVetnttgTD3XLDfwvl-W-3i3NbE5ZvJcMhbd7IXBFa909QusL8qVRJTbc_n1gzznDclid4HHZssEk6qCHVl2B2ljDOV5aUxqGshdbyDnA7ST0xODEcWnkKPfwgSXAsby8aOFidrGHzPtn5rhTb_Pj4Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=cHQw80rxd1LdbuYfApsV7rQPle6d9cI5quEoBlmMTTUeoo7fP6IZkZVfu1lfzUWr3gqeCNNkrFj8epkJVx_apjxw7Sad-Rmz2qF90RKh-e02IMO-_K8F9zZZWqgfhTG-1hLGX9yQZAgtP_9V4xsVATvB4csCdw1bF8XbjZ_388nowcDyDOvyFJiXWQKXirIuvtnDtsr5wyyHJFsNnEz7NwwimTSbk2qDNM6PZW6q_UWmODZhtzRjM7vSxpkFmzx_JXmHaYaLm-WwWMjSAFYicRdZJtOQuXX_7bYalAUrWpzapB91FxLHDwo8FaqV1YPDadd661HrDZPTNU7dzGEo0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=cHQw80rxd1LdbuYfApsV7rQPle6d9cI5quEoBlmMTTUeoo7fP6IZkZVfu1lfzUWr3gqeCNNkrFj8epkJVx_apjxw7Sad-Rmz2qF90RKh-e02IMO-_K8F9zZZWqgfhTG-1hLGX9yQZAgtP_9V4xsVATvB4csCdw1bF8XbjZ_388nowcDyDOvyFJiXWQKXirIuvtnDtsr5wyyHJFsNnEz7NwwimTSbk2qDNM6PZW6q_UWmODZhtzRjM7vSxpkFmzx_JXmHaYaLm-WwWMjSAFYicRdZJtOQuXX_7bYalAUrWpzapB91FxLHDwo8FaqV1YPDadd661HrDZPTNU7dzGEo0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=E9IuapouxA0JTYPsz15wEvyKLvDVZKQOtIipiqRzibgOiSrcbHt47VPeW3CW-c1yOk2BKuKlLMQ9bmAFEbgFid2cl-FbEWQuQye3WbJ9mdtAGBD5fvQeDT7-z3WAfbSqJtNeZQKcIuxt9ZcfFkqn9AMx4kDLPss71XSY5i5wF-LG_p-jhypayhCmNQPS7sLCcABKmASeEc7ou-3tIH376ttnjm67GAAM9waGNZ82WJn5lAiU8QGJYieGZDVdBoB9KgcMbPVGNBbpzP4Occ47FtPSSRHRJNcBg7KWmfdOpqoHqQsTUvUEhjxhna8GNvzXLAHb6iscXUbfshQHE4b7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=E9IuapouxA0JTYPsz15wEvyKLvDVZKQOtIipiqRzibgOiSrcbHt47VPeW3CW-c1yOk2BKuKlLMQ9bmAFEbgFid2cl-FbEWQuQye3WbJ9mdtAGBD5fvQeDT7-z3WAfbSqJtNeZQKcIuxt9ZcfFkqn9AMx4kDLPss71XSY5i5wF-LG_p-jhypayhCmNQPS7sLCcABKmASeEc7ou-3tIH376ttnjm67GAAM9waGNZ82WJn5lAiU8QGJYieGZDVdBoB9KgcMbPVGNBbpzP4Occ47FtPSSRHRJNcBg7KWmfdOpqoHqQsTUvUEhjxhna8GNvzXLAHb6iscXUbfshQHE4b7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=fRKENXmgk54rUn1F9qcWTbDZF5IvArXEsRfd7X4xAGM_Prsdqy9Inuc6AF4J5NnXbcrvv0dwOUo35VkX0wcbyuO5w18sO4GRWy4rl4ACGsPSgqzT1G_Q--TSyRwmeYlL8Sq_2MF1kv5G_KYmN-h-tFZ4JuH0xEreBMQLOqWZNWQdzlQJd_Y4MxIa4GUsy--RcMh7TGp2wEh0oR7fqinDclV0Iy-J6Cc9sxJfCjNxVm26pFpG0-7_9uGvnaKgpKy3EmsL6xFmXRGNfYvt5TvjPVNvywXiIEAtMRiT35CyQompUL28tVAp2cEfxQbUT7g2uATnBuE-_QDwOGfyIopDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=fRKENXmgk54rUn1F9qcWTbDZF5IvArXEsRfd7X4xAGM_Prsdqy9Inuc6AF4J5NnXbcrvv0dwOUo35VkX0wcbyuO5w18sO4GRWy4rl4ACGsPSgqzT1G_Q--TSyRwmeYlL8Sq_2MF1kv5G_KYmN-h-tFZ4JuH0xEreBMQLOqWZNWQdzlQJd_Y4MxIa4GUsy--RcMh7TGp2wEh0oR7fqinDclV0Iy-J6Cc9sxJfCjNxVm26pFpG0-7_9uGvnaKgpKy3EmsL6xFmXRGNfYvt5TvjPVNvywXiIEAtMRiT35CyQompUL28tVAp2cEfxQbUT7g2uATnBuE-_QDwOGfyIopDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=V8OFxeh42cQhjainkNwMnyd2-Qx8NcBeBmk22MrQ_rXAUAFvgbcyTHOVRJiVA-UNs4f-b7IX72tmjljIm6yMk0Dk-irARmoEpIPqNQuz10qrPrlMuOdMAYZmxmw-RHxaYhFRfvqmOvRopzIIzOw6uCM-5UHxHtOGW4wPCy-rT8sUVrF9S9vqEeAfTLr88yoAHpXm_gGEV0qVJoydCGhxiYkrd9hzrELWbwYnDwSe5VMQ10D4oQb4eZ1-u4xbVwwkmuula7znGfzV_ExfFAauVjMr3VCGPbT8xud9QbHDVUmX7ZJ5BMxnO7-X0hQF_z0AUaHifUmVU53SPiKoVROEO76NLfrU-pSzrOY2Z3DLXxkpDksBjcLzDoeVga4_HC52qnfnsEn4b5PLCnOXwXeTJ85PuFZsNm2SNbFlmhAcUNT6kN4J7n6DCuPme8qopM5NYkuuBcRZKKOIxxjMS-_ODG2I13WXt038iEiAbMTY2o3hNzciWTGatygejWs3-p5JEYKmowYGw5a0jwLBbDJbY4ck9_waLXiWJf2DCFGmqVyJYS0iTW6boZ7IleO4ke433_4QwrLNEU8CPYjpoeVdoO14rhDS_zUJvpEiyy8fGVSKJ8gG1fWyQM1rTnpAuAu7lVgUWerY9zAZ51g44yZ0EPiSQveV56tS753mf_w8CaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=V8OFxeh42cQhjainkNwMnyd2-Qx8NcBeBmk22MrQ_rXAUAFvgbcyTHOVRJiVA-UNs4f-b7IX72tmjljIm6yMk0Dk-irARmoEpIPqNQuz10qrPrlMuOdMAYZmxmw-RHxaYhFRfvqmOvRopzIIzOw6uCM-5UHxHtOGW4wPCy-rT8sUVrF9S9vqEeAfTLr88yoAHpXm_gGEV0qVJoydCGhxiYkrd9hzrELWbwYnDwSe5VMQ10D4oQb4eZ1-u4xbVwwkmuula7znGfzV_ExfFAauVjMr3VCGPbT8xud9QbHDVUmX7ZJ5BMxnO7-X0hQF_z0AUaHifUmVU53SPiKoVROEO76NLfrU-pSzrOY2Z3DLXxkpDksBjcLzDoeVga4_HC52qnfnsEn4b5PLCnOXwXeTJ85PuFZsNm2SNbFlmhAcUNT6kN4J7n6DCuPme8qopM5NYkuuBcRZKKOIxxjMS-_ODG2I13WXt038iEiAbMTY2o3hNzciWTGatygejWs3-p5JEYKmowYGw5a0jwLBbDJbY4ck9_waLXiWJf2DCFGmqVyJYS0iTW6boZ7IleO4ke433_4QwrLNEU8CPYjpoeVdoO14rhDS_zUJvpEiyy8fGVSKJ8gG1fWyQM1rTnpAuAu7lVgUWerY9zAZ51g44yZ0EPiSQveV56tS753mf_w8CaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=gajycXfOgEzNIffoD_v3hSCP2uehV9vfNQuQw3HJVVtu6Q7EuPyAwR79HI3KFCsoqJRx_Q0VKP6_H-JrQtRTrR8yyKj0QPpBBSD54dOKGtJtTOzIQVRx2Zpfyvaz5MuTF4KKWOyleg6DQM3uvMURnGZgB8_AWf_s9D9xuIm2qx2tEYOlVQyssF6_izhTrJKpbeNBQpb0TKRs-CaTdcarAMh0SL_ou1iwVUengEJwnh062RBQ0Ce6qncK2TiOONoRG7YhWEm565kdaqOj9oIxXtRYLtZhBnFhW7izhu-5fxAkIa6_KtEQe7X15b_fSU9MRE5MN7oDb8n09nvP6JrvZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=gajycXfOgEzNIffoD_v3hSCP2uehV9vfNQuQw3HJVVtu6Q7EuPyAwR79HI3KFCsoqJRx_Q0VKP6_H-JrQtRTrR8yyKj0QPpBBSD54dOKGtJtTOzIQVRx2Zpfyvaz5MuTF4KKWOyleg6DQM3uvMURnGZgB8_AWf_s9D9xuIm2qx2tEYOlVQyssF6_izhTrJKpbeNBQpb0TKRs-CaTdcarAMh0SL_ou1iwVUengEJwnh062RBQ0Ce6qncK2TiOONoRG7YhWEm565kdaqOj9oIxXtRYLtZhBnFhW7izhu-5fxAkIa6_KtEQe7X15b_fSU9MRE5MN7oDb8n09nvP6JrvZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=Kn3DO2pA3ve2WcAIINnjM6eGVGPlwmAvfUjtS8tUyXjzs2R-KqcaVUW99H8zgvuYinfaA_xeow7pJEOsrnqOY4WL4o0aamK5xVkZG07nnQzu2a4Xj7eW3xjzIdQjhkyYWVOSwXOnMplzO7IS_sRZK957XY4-kuTWldIYSLk_vigsIAouLK-RQgnPVwjbqU59ghJ9iFsotjVsWnkqUhZVFLSKu8CLq1gjDoU4o-4xyIikIM0JNiQHijPoVamB497qGSlMj2ubgyD0w6fPuvThUTF74jIItNy2S5tbdXKQzZL81HwFqdDkx0wrdugqkqfHyKvrEKgLi_vI15r1YjcwKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=Kn3DO2pA3ve2WcAIINnjM6eGVGPlwmAvfUjtS8tUyXjzs2R-KqcaVUW99H8zgvuYinfaA_xeow7pJEOsrnqOY4WL4o0aamK5xVkZG07nnQzu2a4Xj7eW3xjzIdQjhkyYWVOSwXOnMplzO7IS_sRZK957XY4-kuTWldIYSLk_vigsIAouLK-RQgnPVwjbqU59ghJ9iFsotjVsWnkqUhZVFLSKu8CLq1gjDoU4o-4xyIikIM0JNiQHijPoVamB497qGSlMj2ubgyD0w6fPuvThUTF74jIItNy2S5tbdXKQzZL81HwFqdDkx0wrdugqkqfHyKvrEKgLi_vI15r1YjcwKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=k-xH3gUsnBoYRaPYKymTlbLW5KEQBcf7a2UVFHoXgtY5Ve5TxE-yBgM287F1M6-6H9YFmGCHLJFseazkUsRIpqDQGRMs9BIK4HNl6_qF3KEeSkFRRF-yuL4_YzTql6Fx6fP3FP3QWA5tUGFKOakYM9-xcJRFhZY_aIAyg90zCywp36yRRlUCTV6c4KR4EtMxi_v-s6JUsoIjIx2FFfKig50QaJBKdXQVJL25Of44kWu-NlciPx8Yegmg4GQ1GFnKyb2eqYjmmnZODyEhQzjgKU5EUDNJmRQe6uYfqQX36VCcRNeBamEmT95HuLvo0-lu8P-ILDRq6p1XClHREOUkJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=k-xH3gUsnBoYRaPYKymTlbLW5KEQBcf7a2UVFHoXgtY5Ve5TxE-yBgM287F1M6-6H9YFmGCHLJFseazkUsRIpqDQGRMs9BIK4HNl6_qF3KEeSkFRRF-yuL4_YzTql6Fx6fP3FP3QWA5tUGFKOakYM9-xcJRFhZY_aIAyg90zCywp36yRRlUCTV6c4KR4EtMxi_v-s6JUsoIjIx2FFfKig50QaJBKdXQVJL25Of44kWu-NlciPx8Yegmg4GQ1GFnKyb2eqYjmmnZODyEhQzjgKU5EUDNJmRQe6uYfqQX36VCcRNeBamEmT95HuLvo0-lu8P-ILDRq6p1XClHREOUkJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pWC8tVNL1QbL3OWpsyFatW1Wellno3JBNiCONWZ8B9U_MuxGemDE-41gd8meBTwGOVpzuzIESByrDoTjQ4dmuUYKX6LgaxSiMNC-to1YWe5Z8ykQFO4RmXTZrA0jMVr4KIOnFfYIgLh4f7cIdhpal5P7AGINbEolhsKCG_bioTY7tKxLLJg_Axstc5RAVYaMeWH7BMNs3lsnUAPrOLg0rWVekYZ_Hwqz5S03kQflRSOK6rNuLzUMMMpCG0BQ5wE1p7d9gmE4kMAVMtCTxfbb07JDLAc6dGCK253bzPN4y8ukaE34ov1zrHlAy3_3kU6nB-hzHFaouQTymOo_AQNNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=YrjGr30u2ar_90UrgGUi_Zq5ooMTHDVqyK6FHeg88tY2CscRk2IlzRk2FhrrS_UMSe3QqjNAIlVZA2BvfX2AwVoFlYMKlbha7rN1ip9WIWVwqnW2StTsSJ9Mn-Hkfd4JeFbk6hHR1DJ2nfxdBeRdywoPK13cWhbO1Kghl7QXNWBs9rzmryijcNNCSCsjNagb4_biPv-Ji7CNXONcbZTMdlU7Q-KdHNDCG0fEJBXXc_VlR8pQHsySP7fCghN8cgno0mGg07dmut1SK5hl1hrLX8w_O82HYX0I10buFhPrehQe3B2YutTuvjtSgaY7z3YxXVTAubQ537wI_Ai2G_qKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=YrjGr30u2ar_90UrgGUi_Zq5ooMTHDVqyK6FHeg88tY2CscRk2IlzRk2FhrrS_UMSe3QqjNAIlVZA2BvfX2AwVoFlYMKlbha7rN1ip9WIWVwqnW2StTsSJ9Mn-Hkfd4JeFbk6hHR1DJ2nfxdBeRdywoPK13cWhbO1Kghl7QXNWBs9rzmryijcNNCSCsjNagb4_biPv-Ji7CNXONcbZTMdlU7Q-KdHNDCG0fEJBXXc_VlR8pQHsySP7fCghN8cgno0mGg07dmut1SK5hl1hrLX8w_O82HYX0I10buFhPrehQe3B2YutTuvjtSgaY7z3YxXVTAubQ537wI_Ai2G_qKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=VLqnSlsVs7Q20ya86LfrUuuKlFh1dGhiXgfEG6Nhqo_tOZNOCwoo1010r2s17RuxNlgFZv2BXsUbG8QJKlxuLrOyh1ONC_qUl1s0OwJaOfiugZ2vYn-w_uiJI3yeoMsjXqbJwYSHUFbgOFo0xIhjOGh15UAobbXdnSXfAqslEkA4o16z7hst6NAbPZJzoOUeEsH14-cahMEtol8BkGrXkpS_n975annGGkt2cfthckz6BVvbHzci4-Zyr9yLjfHS7Jk4DyozRQWLjwVjTmbVzMreQp_Zk_6fIzI2Dk3-YD57yr8eY9-mRVOhXnUqSnfeykSeihUJsHBwv3wp0O4EgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=VLqnSlsVs7Q20ya86LfrUuuKlFh1dGhiXgfEG6Nhqo_tOZNOCwoo1010r2s17RuxNlgFZv2BXsUbG8QJKlxuLrOyh1ONC_qUl1s0OwJaOfiugZ2vYn-w_uiJI3yeoMsjXqbJwYSHUFbgOFo0xIhjOGh15UAobbXdnSXfAqslEkA4o16z7hst6NAbPZJzoOUeEsH14-cahMEtol8BkGrXkpS_n975annGGkt2cfthckz6BVvbHzci4-Zyr9yLjfHS7Jk4DyozRQWLjwVjTmbVzMreQp_Zk_6fIzI2Dk3-YD57yr8eY9-mRVOhXnUqSnfeykSeihUJsHBwv3wp0O4EgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=vj0TFoPajHqyCxZ1ZIVd3X-BgdrSj9970kjVC7O-5YEpU8MLrZZdXjGIYXRrCPjKIBhOIKoJQeUFL9ynEnb4sLJBDbHcrUi9_76Y-aQ_Xurbi9X-ThdgT1fTlQHWXL2YS7cEvpH9k4hLVvp17Q3ADQsCiij-s4h8Cfu-r7-JMC1-Nbqn2q6X4E7VZ4RU70aTi-RnyYqEfX5t5sLHOY7aXHOBSTMUvK_1FlMRDyp4HqeVA-284EcU3fFgo__3Mh-9hhqzWktUUxsAxX7czP_Ec5_1lbGlbhMvoZNga9XPNzeGLG-_gPwNAUPvGeAcLEMDL2Qm3fKN9ahSnk3PXmc6oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=vj0TFoPajHqyCxZ1ZIVd3X-BgdrSj9970kjVC7O-5YEpU8MLrZZdXjGIYXRrCPjKIBhOIKoJQeUFL9ynEnb4sLJBDbHcrUi9_76Y-aQ_Xurbi9X-ThdgT1fTlQHWXL2YS7cEvpH9k4hLVvp17Q3ADQsCiij-s4h8Cfu-r7-JMC1-Nbqn2q6X4E7VZ4RU70aTi-RnyYqEfX5t5sLHOY7aXHOBSTMUvK_1FlMRDyp4HqeVA-284EcU3fFgo__3Mh-9hhqzWktUUxsAxX7czP_Ec5_1lbGlbhMvoZNga9XPNzeGLG-_gPwNAUPvGeAcLEMDL2Qm3fKN9ahSnk3PXmc6oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=Q0DM90p2bo6wCBh3Z4tuVrNcvvUr1Lt4GK-kQsR0OJlEvPGbHmYRXjHapR2crspksNgmnCDBezEYl4EYdoXt4qBiriBiAtFMeKssCMKoqPE_cJmxQ3yfCl7dtdhSAStVNaSk8LjtxdsGF1x0TdACSZeKpPWqAGiFFJinpskO6DkjLOyw2TR-7Wxsnx9wa5w8DSRmgMqIgu_1SBSat6myYBUiiS8jJcje1xunYaqw6VyagN5Jztt0Ym9YRkoIyoSaZhRfm2ZyifgM_ktToFTCkKDS3t2V-PpAcy_lqVkowQOl791h3WrSqj_SaMmEMBc1Txs5rvFHkXMToyryk2hRGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=Q0DM90p2bo6wCBh3Z4tuVrNcvvUr1Lt4GK-kQsR0OJlEvPGbHmYRXjHapR2crspksNgmnCDBezEYl4EYdoXt4qBiriBiAtFMeKssCMKoqPE_cJmxQ3yfCl7dtdhSAStVNaSk8LjtxdsGF1x0TdACSZeKpPWqAGiFFJinpskO6DkjLOyw2TR-7Wxsnx9wa5w8DSRmgMqIgu_1SBSat6myYBUiiS8jJcje1xunYaqw6VyagN5Jztt0Ym9YRkoIyoSaZhRfm2ZyifgM_ktToFTCkKDS3t2V-PpAcy_lqVkowQOl791h3WrSqj_SaMmEMBc1Txs5rvFHkXMToyryk2hRGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=aiIB1dzEGQS5L61d0haJhAkcsZOVXH8bchBFhUTnWL5T13dHK8jJG3nhm6tNApqBees5BHAaGbCmzvU-OhVYzOISpZ-lmpI7Kbwnbnh-P-KqIGxayLRp1ciVyccZItnUw46X0Vokt15fMLOYXS8Nbdrjohllv-duodlvn_eYt_uP_xqy2yr47xfI-ttgeKPX-9IZ4Hqib3-snhO26K69VgN1DHrsa9OM8TzDv76RJPzSd9W-Df3BPTGZVMd_nBlV2a2IK2isu1XgpY6ZZx0bwuQMaMWruosxR0PNOJcavV20--CXntYIMxWpbTARvjMDm1yGtBRtwvEPU5HwqMt2cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=aiIB1dzEGQS5L61d0haJhAkcsZOVXH8bchBFhUTnWL5T13dHK8jJG3nhm6tNApqBees5BHAaGbCmzvU-OhVYzOISpZ-lmpI7Kbwnbnh-P-KqIGxayLRp1ciVyccZItnUw46X0Vokt15fMLOYXS8Nbdrjohllv-duodlvn_eYt_uP_xqy2yr47xfI-ttgeKPX-9IZ4Hqib3-snhO26K69VgN1DHrsa9OM8TzDv76RJPzSd9W-Df3BPTGZVMd_nBlV2a2IK2isu1XgpY6ZZx0bwuQMaMWruosxR0PNOJcavV20--CXntYIMxWpbTARvjMDm1yGtBRtwvEPU5HwqMt2cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=kBppxhsdJilPqr_-z4tRHHi71RXMclDdguXosVLybuCpitP919mjeCPj3Qsv5bH6sktquGSZKopOg498JLatOZqa4Sx1ESRmsQ_PCxghAzepPUVd2GaRRTgKygFKDfa5CMtLn1bz9m-lORr1DWNoZaC44PICloggYrFKJkwSep8r2GT7h0S02PExbUMQAz_Frgkue_tRYUlDoAFTOHA1YUc5UPWrDDJG5wF1ZPVuWKkpzzEu_MTATHSEaygdODQuY7WIDryuKe7quKAxGSG8oyHGTjUV3gzdwG-6OmFzXuU2SJByTSE4ZmR4HDO1JoHuhuj2aUMDOVK00xACdY0hWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=kBppxhsdJilPqr_-z4tRHHi71RXMclDdguXosVLybuCpitP919mjeCPj3Qsv5bH6sktquGSZKopOg498JLatOZqa4Sx1ESRmsQ_PCxghAzepPUVd2GaRRTgKygFKDfa5CMtLn1bz9m-lORr1DWNoZaC44PICloggYrFKJkwSep8r2GT7h0S02PExbUMQAz_Frgkue_tRYUlDoAFTOHA1YUc5UPWrDDJG5wF1ZPVuWKkpzzEu_MTATHSEaygdODQuY7WIDryuKe7quKAxGSG8oyHGTjUV3gzdwG-6OmFzXuU2SJByTSE4ZmR4HDO1JoHuhuj2aUMDOVK00xACdY0hWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=cjVQ93l7CDZpPvzD2NPSC30lgTrhKeVCCxVvCTbfr_SzPbC08GGuz2bhoXWtK8IxsnhuWk8lO1t0vBCkQoqEgEV8v80-6yUpwK0dBeDK9vMHMwzn09wAr75NyJWfV0Ux6ewvUTReahFdGShPoy_Zl0Pl1WH9xgX7s1YwWK7bC4Vbx9T8ZZlUaMMpiprLBVGvDr3YvynTmCYDSMgf_mj6pJ_B56nBurV10rapicAsQLBVAeatfsjNbDlR8Hy-bEg4c7dunH5vvXc3LQfV75hF2wPqlOiPyGOVQwHYwEsLtFqnjG8XaHwBtcVmoagUQgAuoH83WR0nD5qVUaelnpI4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=cjVQ93l7CDZpPvzD2NPSC30lgTrhKeVCCxVvCTbfr_SzPbC08GGuz2bhoXWtK8IxsnhuWk8lO1t0vBCkQoqEgEV8v80-6yUpwK0dBeDK9vMHMwzn09wAr75NyJWfV0Ux6ewvUTReahFdGShPoy_Zl0Pl1WH9xgX7s1YwWK7bC4Vbx9T8ZZlUaMMpiprLBVGvDr3YvynTmCYDSMgf_mj6pJ_B56nBurV10rapicAsQLBVAeatfsjNbDlR8Hy-bEg4c7dunH5vvXc3LQfV75hF2wPqlOiPyGOVQwHYwEsLtFqnjG8XaHwBtcVmoagUQgAuoH83WR0nD5qVUaelnpI4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=eXTsbnJsX13Rt3oSmvyCp4zKWS1-F5KDVPoP2Ujn49Sz2LWQyyDpZpnAR410oUwQTTVgl1pHVWHM7Uz8yp0l1ErYYtsZYRLHwrDuOLYvhXIXvD4BbyztNsFJHZtyreHSsERNsnwPLI5X03dCkdplhQCi9jITPg3tIsLlLjvRUvS2mvNqW7VTNgqtfDA3L6tWThafKI40BLRUGDitzrKxahjbFZOJCENSmAZ-vmpSCtfYsGysatq_gv4BSJVSha7gC5soFNPf3qBoms3tHxCbUc4f69HhipzoLeSULoQzFh4r2mIKXSZb3KtG8LwNuu1ikkG2hjEa7eOkGFL9gJEVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=eXTsbnJsX13Rt3oSmvyCp4zKWS1-F5KDVPoP2Ujn49Sz2LWQyyDpZpnAR410oUwQTTVgl1pHVWHM7Uz8yp0l1ErYYtsZYRLHwrDuOLYvhXIXvD4BbyztNsFJHZtyreHSsERNsnwPLI5X03dCkdplhQCi9jITPg3tIsLlLjvRUvS2mvNqW7VTNgqtfDA3L6tWThafKI40BLRUGDitzrKxahjbFZOJCENSmAZ-vmpSCtfYsGysatq_gv4BSJVSha7gC5soFNPf3qBoms3tHxCbUc4f69HhipzoLeSULoQzFh4r2mIKXSZb3KtG8LwNuu1ikkG2hjEa7eOkGFL9gJEVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=dabTK4un7rh9muPVFVk5IO0HV2P-xUTUL3eR_qFBy7rlfUfaWyNBgRiNVuj3UfG9Jjh5AD_j9zZTCw3G3H8ATFoRrVDsTEL3gsrpHk7PfjXJB9D1d13ft0etwnxgHnG1Ww6c_oBttkKUHNtiBnFM2UDz96lsnEA-UFK15qwU142mT1DimKbMmvYs_2Ate6m3MQ7e_UNS59QxFdszFjZuog27l-LMcvLKV3RkA29fYyfPRlzB277HZYFeQaGyE8HBzEB6xPvuXoQbNqFgDP0cie0q2-8agbvaT83CQ0QA7v7ENWxPGJtSzGH8SmULaQlyvb7MKBF7ndL2QP3bKCtRIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=dabTK4un7rh9muPVFVk5IO0HV2P-xUTUL3eR_qFBy7rlfUfaWyNBgRiNVuj3UfG9Jjh5AD_j9zZTCw3G3H8ATFoRrVDsTEL3gsrpHk7PfjXJB9D1d13ft0etwnxgHnG1Ww6c_oBttkKUHNtiBnFM2UDz96lsnEA-UFK15qwU142mT1DimKbMmvYs_2Ate6m3MQ7e_UNS59QxFdszFjZuog27l-LMcvLKV3RkA29fYyfPRlzB277HZYFeQaGyE8HBzEB6xPvuXoQbNqFgDP0cie0q2-8agbvaT83CQ0QA7v7ENWxPGJtSzGH8SmULaQlyvb7MKBF7ndL2QP3bKCtRIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=ENayKoDmYKVdrC_SzTErAybYB7gBWTB2UiCXhqq7CJH-7TKvTjJfnXHjdKxiT4-zzkdEyTK6RKg_h1gAk0mrLhUAWmUHywBF0QPSJAVJWXhUX2Mg1izAnC8nJWZBsVTGa_qMwF_9d0IV9uYZ0LCdglAtNrwKKT0wwrce7P4pXPReD40lYDzYC7vVtpD1VjSyjuox664xZT3yFUpX4FTw8qqFKUwqYY5LVNfxKsh33uU8bL_r3ozAylQW5L9WIZYfiYbUI1x9uHBVjUlr3ZvE7LyoYkqXqGJ32LWLbTBH2t7FTO7wn4rU2W4b7rxIC8VJ4Q-DfyYJocMPlyiPUS0Bcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=ENayKoDmYKVdrC_SzTErAybYB7gBWTB2UiCXhqq7CJH-7TKvTjJfnXHjdKxiT4-zzkdEyTK6RKg_h1gAk0mrLhUAWmUHywBF0QPSJAVJWXhUX2Mg1izAnC8nJWZBsVTGa_qMwF_9d0IV9uYZ0LCdglAtNrwKKT0wwrce7P4pXPReD40lYDzYC7vVtpD1VjSyjuox664xZT3yFUpX4FTw8qqFKUwqYY5LVNfxKsh33uU8bL_r3ozAylQW5L9WIZYfiYbUI1x9uHBVjUlr3ZvE7LyoYkqXqGJ32LWLbTBH2t7FTO7wn4rU2W4b7rxIC8VJ4Q-DfyYJocMPlyiPUS0Bcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=WrRhd7nhB01hzetxngxWLLiGSLR83NwsGIM2IM7qU_dbc9J99KN-HdZT3Mb0D14WxcbuwpwE4orpwAEk8H8H3Zqx26Di1IukgWME0DeIs1Ej4xAmapWY5kLt9JjfQXUpTxkV0CVOcGpxUWvzmf_nq30prXmBbdxG8ZbFoM6uUsv1fHwOdQBknZgkwXvaqKmPduYyNAmt8hgMPJ5Gd3obCUBs9wCYVEFkSd285Ltj4LJ6h55ZVrsCPfg0f6kv2BH6XBOyzGjKqnIxCXQ8aIoDSANBq81uYjZynm0xe7Fnb5UCpWNri6KcnpuDsVwpCcr1nhq8KXykEllTkRR-_ZIvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=WrRhd7nhB01hzetxngxWLLiGSLR83NwsGIM2IM7qU_dbc9J99KN-HdZT3Mb0D14WxcbuwpwE4orpwAEk8H8H3Zqx26Di1IukgWME0DeIs1Ej4xAmapWY5kLt9JjfQXUpTxkV0CVOcGpxUWvzmf_nq30prXmBbdxG8ZbFoM6uUsv1fHwOdQBknZgkwXvaqKmPduYyNAmt8hgMPJ5Gd3obCUBs9wCYVEFkSd285Ltj4LJ6h55ZVrsCPfg0f6kv2BH6XBOyzGjKqnIxCXQ8aIoDSANBq81uYjZynm0xe7Fnb5UCpWNri6KcnpuDsVwpCcr1nhq8KXykEllTkRR-_ZIvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpTK051RLu7nSpaZiQVB4HnlCx2f9l0BjbInTxD1A5hlHizfRNwHzyeeai4Q7hLZiO8gg7CdZKFL9Rsso8uJGuJJ1PPGKBsHaHHefsUBaItEkVNiBPbtO6TRoM1Sm-4n1IfG3nTstK2zP2jvz5OzFCfIl_6bUnMLXJHWV3MNaqRtPNwt7YdU8y5I_bVcyRHcQYuTPFKaAfsLgv5N8cpgoe_L3SKZ1yxieqcftpjgvihxvvxs_L7TBJLN7dgS7kY868oeYEzgXsS3FIhHHBOyNyQ88Bg3ikbwQxNmPQ_y_d4rOZP_Ffo8JzSB5bpmEozVPnMmg7BRv4ttqUdP-ZG-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_hSKcBo_sBoDZODdTyQDWnB2fUXE73ER_3ckDnDzKqcw41uvFlEdd2O38VTm9t0-QWPjffoWwBTG5D0U0flqNZRgnb3MRHUzjOL76-RaJ8GOgQfp8P67lHtYGB4qE7iCNa0RcjrIA1hPjKXgicz5Y-TIynKE-XpUcE0TtvmeBIQC_77b1J8j7vtpnma1qaolJ0Obijwbug0ziAnZmylTl3MyHrio3KTRs0lhIrkUTOuY8S7SrLfAyPB1YY5dJ2i19SRPILKVG7yCURiUBydJYrEfATunqMP7Q-Gz9VrP5B-_CyD4MjxaEkKiU3pdH-l1xoT0iwTEe5CAYG1LvEkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=qv5pG0cpoqT3Lz4ybGtPmywPfsbdopJuuRYstv2IV8i17ajtfl0wYxXK70nEpS-NTt32eVlwuw7z96JrkgxW_iTJRcjN9VNuk8TvJLitgSZoGyCHd4YOv86uaimD8OMFABstM8Wp3qsvjryjvvsJfner-D4WBUuDXDnyLF5k_yj0DGPR_Tqdxtokt217fnYeVd82WCJftWixq1VEdABTQPxxpdShYlEydAMkuDLmc3K0bqtCv2f1o1YEQRmz-2jhmXUnPnJd93eR5edumdOe_nxjKAXev_RfE0w-Hd_irVXQEqlQLsw2GG379CHXY-8tU11t0xAmvDXLtrJpp79_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=qv5pG0cpoqT3Lz4ybGtPmywPfsbdopJuuRYstv2IV8i17ajtfl0wYxXK70nEpS-NTt32eVlwuw7z96JrkgxW_iTJRcjN9VNuk8TvJLitgSZoGyCHd4YOv86uaimD8OMFABstM8Wp3qsvjryjvvsJfner-D4WBUuDXDnyLF5k_yj0DGPR_Tqdxtokt217fnYeVd82WCJftWixq1VEdABTQPxxpdShYlEydAMkuDLmc3K0bqtCv2f1o1YEQRmz-2jhmXUnPnJd93eR5edumdOe_nxjKAXev_RfE0w-Hd_irVXQEqlQLsw2GG379CHXY-8tU11t0xAmvDXLtrJpp79_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=UHPbTKrzI2CFz7_PP0AiZwiCB53omQgdakKNxaAABI0N4cNojokaWINEcy5228du_7qfkJI7CeJs6Fztu_vkgnOVCT2hRwJlveNcjk5V2Z3gAIJ0S_OIIhyEU0RV184Rsue4jpxjvanXMHoNNeC2XQCjmKRA9ywIUm3SUBCMHa-NxKl2U0kn0GafXZ1r3FJZUFILtSaSpdQRzzEhs0P1i98uBamxMWPWC2f8Cb_mTwZ8uP1UCDPMfDzZcU8y3mJeEHudPb3wB0ap4CpF_IuEvMVOoMPAbgC3qDHVXt1NDixP1yDJoIgUTEtKVeVFlJzhIEggrRd9I_SOsQcgEw6G7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=UHPbTKrzI2CFz7_PP0AiZwiCB53omQgdakKNxaAABI0N4cNojokaWINEcy5228du_7qfkJI7CeJs6Fztu_vkgnOVCT2hRwJlveNcjk5V2Z3gAIJ0S_OIIhyEU0RV184Rsue4jpxjvanXMHoNNeC2XQCjmKRA9ywIUm3SUBCMHa-NxKl2U0kn0GafXZ1r3FJZUFILtSaSpdQRzzEhs0P1i98uBamxMWPWC2f8Cb_mTwZ8uP1UCDPMfDzZcU8y3mJeEHudPb3wB0ap4CpF_IuEvMVOoMPAbgC3qDHVXt1NDixP1yDJoIgUTEtKVeVFlJzhIEggrRd9I_SOsQcgEw6G7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=HfkneOBwCUhN-FEm-P-yoVZG6RhbNuVJcduy3VgX-4mZ886ZTDjKHMA582FKWAXCnpMN74TBw4OPoohkgdAlBtFG6YY2YB5x3eMVV57k0BdS62_aJ-P0uE2TpDwZ1wGzNv1JMVmGQNitQaRJcVOe0nV7qIP9--FlNr61m-1O1-LPSpyp1hgsXEubFuTOMVgxboCazVWsRIaSKknD077t4RlrJdB1MQV9Mba0T1Dud8c5KDOZ5E-sITzfjNb-Lz4qkGqd4AqW1BP1SLcKSWGtey4T68EosMEHbHN1kPSMATUPy1L0TZLfjR_TJkQO0_R0M9ZXJmolKsjhbNDTzwDmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=HfkneOBwCUhN-FEm-P-yoVZG6RhbNuVJcduy3VgX-4mZ886ZTDjKHMA582FKWAXCnpMN74TBw4OPoohkgdAlBtFG6YY2YB5x3eMVV57k0BdS62_aJ-P0uE2TpDwZ1wGzNv1JMVmGQNitQaRJcVOe0nV7qIP9--FlNr61m-1O1-LPSpyp1hgsXEubFuTOMVgxboCazVWsRIaSKknD077t4RlrJdB1MQV9Mba0T1Dud8c5KDOZ5E-sITzfjNb-Lz4qkGqd4AqW1BP1SLcKSWGtey4T68EosMEHbHN1kPSMATUPy1L0TZLfjR_TJkQO0_R0M9ZXJmolKsjhbNDTzwDmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=dtbPAeQC_04MnQ14U3F0irhknaLc-z3P7ysmm91p-6e1XcwYES9geGj7LpaZC2vq2f3mpJREf_BOe1v8MN2Mu2ECQldIEL3kHNFyP8wDwZ4Cf-Yx_cc0snTc-l1Wo7iDBPEsZu1pn20NULADnCQ9BoCbA6UNXWivjs8J7fxbzZP2Q-6_zixm_WQZtGeiYWxjEhzVQF7zJgDAny4to1XyVqAh9C_VTkRXuAhrtue0odfU_fF6EwqoB9gsRYiRZ0cZVjT2mehYvysMOb4RVPSfS0K8cCTPyObrJ-OvRVUQsCfJDXRXd_4KL1c7wseSaEoSV_hW894gdSTII2KJNv4F9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=dtbPAeQC_04MnQ14U3F0irhknaLc-z3P7ysmm91p-6e1XcwYES9geGj7LpaZC2vq2f3mpJREf_BOe1v8MN2Mu2ECQldIEL3kHNFyP8wDwZ4Cf-Yx_cc0snTc-l1Wo7iDBPEsZu1pn20NULADnCQ9BoCbA6UNXWivjs8J7fxbzZP2Q-6_zixm_WQZtGeiYWxjEhzVQF7zJgDAny4to1XyVqAh9C_VTkRXuAhrtue0odfU_fF6EwqoB9gsRYiRZ0cZVjT2mehYvysMOb4RVPSfS0K8cCTPyObrJ-OvRVUQsCfJDXRXd_4KL1c7wseSaEoSV_hW894gdSTII2KJNv4F9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAGPxe0Lz7DymmUjQ4VHIYIK5n-EA_pXauTm34_0HHuThjSqkpb_4AOOB6KN_5JTeWWM-6fDT5zA0JGuWYoJPQclC2QiPTujT4zXGe6oeIQwyY_BlS8F2rJW8DefmeMOtiPB4uPL_TLZSWpIohZxRd3K_4Vv-rnKW65xdKVXJ9xLedeWCCf4SssttX6Cl3aACmW3Ei0erCX8URoY4ladrnynlKvg3dY8xF8HveMtq_gSwV0ZwoV_jrIeNm1PflLb06yIohXwibFu1qh4G3bUrL1kw3jpZ63wvGrnHFcoxr-_5zpck005UPJhB8R2qKSojfWJy_Q5Y9OeS5WWl49EjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDYHc_elET8KhQlXNyVjo7lBtzAJ6WVHFlH1GWcj96c9k-uuGgzUpNcO1-6fKETdg8Vm-zNHGNvTdwN8hFFFySmW_Q17GTx36PdyZEE6YpFemw0W7kxDyh5d2ZTnqqRJ-ETjTh-LvER9L9SWPJdPMooCQNT7H503NugESvboXIbB3kOAVYZxNrPfC3HBN7y1dKdrgMiXChQRB4Lp93A9pRApDJTXrqX2PLh7v73KCb5ZCflFl-yNwQTdc3m23PIlWJTfkfPCLmeIsEAvtGgrHytCrM65cxzAqOJmn_naHeLYTeD83hFG2QiLLjYfDYlmnFTaw13qaN_FyKt2LeK5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2VYcICbSGLKFgU3TRe2q6fAatxhYvesePVLHGHL9kYYpueIzH14DJrLIGr0fTnZvwqKCB4PUAzeA-utO08oUs6qCyFEessBpnsWcRv34apHSWIAzcFivYzUHjdJEXSi8stGiiXUNEj-loFoH4zDO_i39QO1bbyw638uH3kOGbpTkLSUadWmyq6YrPGIA7pFl-B-WOTyou9crQBqkua5NQN4fSw7fOmY8QhSBLhswVSNgPehiqjZS5oMf9lAaA4_02c3qBZBsmNyzmxmEmClo0t_f3P_2RqNWUNZGNQwlNvNBD9Fs4X6uTTZZQyhk7h5JKxiENTxCckvCyL4V0brMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=i6HWATCe7v2ZtvaKAWPj7lH1Z3lw0fvrubCfBybDGNtMJGtJCsAskc2J4ikhbPVNM7ZmaliuYtDuSsfsaIuEw6eV4zWaKiyqD84F4VD6aY0NF7gfxyHcWG1VXCHFBlB9t0W5kGAVA6O2R8V2T3vP28vNhxbx1rQUL_ECMrn8ZEZFF9fiVfDNPSj5CzidJg1NT-SINNJVHJD0Bd5ZsAYrNiFd1Ao6UgNWNKocTAIx0dg75ZLTDOnjUHG8SCBK3f0djgrVyRvu9JdsFpdQLiXvF-lziHjyOqVMzxOlva2V770GnOfYwIXRvFnvRJHKJvilkTOrfETz_GE1l5s-WZtJQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=i6HWATCe7v2ZtvaKAWPj7lH1Z3lw0fvrubCfBybDGNtMJGtJCsAskc2J4ikhbPVNM7ZmaliuYtDuSsfsaIuEw6eV4zWaKiyqD84F4VD6aY0NF7gfxyHcWG1VXCHFBlB9t0W5kGAVA6O2R8V2T3vP28vNhxbx1rQUL_ECMrn8ZEZFF9fiVfDNPSj5CzidJg1NT-SINNJVHJD0Bd5ZsAYrNiFd1Ao6UgNWNKocTAIx0dg75ZLTDOnjUHG8SCBK3f0djgrVyRvu9JdsFpdQLiXvF-lziHjyOqVMzxOlva2V770GnOfYwIXRvFnvRJHKJvilkTOrfETz_GE1l5s-WZtJQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=Q2CINVGY09Ppsf0hEytWTvSo02VwH2Y7IZ7jHeYUeP9VA9Ln3H3nRwhKWUNw6Lz9Ms3qhSIb7Vcah58hLISSBlP9rXhHe7tErjVBJPiDMCd53vhaHFCKn0PZhPMtucfGrvgV0rcOwIgKlz37OMtatN6dJZYcTwWgZpxuxQflPnTOxsvmS8U8cePkFSAaq8j-hXSFeaSJ7_xwJf5h9785Y-KCYUaQh5YJt44hpoJnABQEYyUzpYvTZ9zUzbG6u2TX2yIWeM6tTTrJWbcq091eYvvMqKTY2nLg4O7ixT7I-XZ-q2jVBDTpgMwuYN_qa5rfJkINyDpuNGA__wpTNUTHew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=Q2CINVGY09Ppsf0hEytWTvSo02VwH2Y7IZ7jHeYUeP9VA9Ln3H3nRwhKWUNw6Lz9Ms3qhSIb7Vcah58hLISSBlP9rXhHe7tErjVBJPiDMCd53vhaHFCKn0PZhPMtucfGrvgV0rcOwIgKlz37OMtatN6dJZYcTwWgZpxuxQflPnTOxsvmS8U8cePkFSAaq8j-hXSFeaSJ7_xwJf5h9785Y-KCYUaQh5YJt44hpoJnABQEYyUzpYvTZ9zUzbG6u2TX2yIWeM6tTTrJWbcq091eYvvMqKTY2nLg4O7ixT7I-XZ-q2jVBDTpgMwuYN_qa5rfJkINyDpuNGA__wpTNUTHew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsQVdzASoA2BTFkLBci2BCg84s9usD2M8VA7EYfrVt0cB3h7j5dZJPR8HLaufjNnsBMhvhBGBtZmHU-ob2jzy_q-IIAJmSeTrTCUeaAJACVWcuMmbmSKZPJB48ZVRxufS4lZjZHyOZlBuXmOyoutDF4v4UReaVNT1dxOWOJP3UVdva95HvHbyB2Q39mEjDAM2f0jYJ9PbaDkZb-jC6U94A6VjxCIOYeZiHUm_jn6qGnWjWccd-2SzHySO-AkP2I0RQuHV1m9kDBk-E0jdeSbNRO3pIa6DNVdkgR-mtF3_DySfZ7-FY3KmbSAPHtl1lQ_yKpdXht2-4k_AGeVVWw9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=XbJnMXAGZJMybFD_hc4CyCzT8GaxxXSBg3MGkyz5UEymNA5ErjbxYxih7E9QuSiVDuX6mZKt__Gq2WUuQvyd4dkFc9mGxtsTCETznzVRpYeOgHUtL4Y9dxw2Qh8WGTgadgm98BPo03ZgwlAizb-Z8w0Wqa-SDPfXmbK1-B1eIUsXSqvR5oG2HqvXF5wJi_XqO-_MJbdynvaeFo3peLG4XnGs7lEevhWWaYG6TWpxm9IDdVGu0PxSsKZLIWNu3zJIHWQZy5mDKgQOr0buO9MIES1s4-LCcReJUxy-JOHkcaMX-P8jNsqGjafQ8QukHWtMKUqPaWvHyGZdORZSV7KDI5ZORbZCgESqBjU1qoJeN_Phlr1t9vhS_jCk7mXAYBoPGA-ObPFXdMiSEaAT85oL0-Wr0kl_Cx0AzQ7ygEVGROlgKJ02cgqLwa4t_R7y9DIq1tOBUcEH3snTouH7mYqLYnOaCUPMFKfkAtRuzGFRjXjnOQHNqpE7Eg6n-FB6SHssD8Mm3qTamM-mOWBajXWfwsdhcQPNATSxpsPPlrO6ZXTyccF4g2Ak09u27MZ6S4UVA8JLdFAjNPufgEOQPpNFFAdkjESw8ocmqWZ7JApwl2BSkwSFymytP2eMGTCu9z_CRHp3UYnZhjE34e3qh4DizxJ4YfmW2UrAquomlga9ulU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=XbJnMXAGZJMybFD_hc4CyCzT8GaxxXSBg3MGkyz5UEymNA5ErjbxYxih7E9QuSiVDuX6mZKt__Gq2WUuQvyd4dkFc9mGxtsTCETznzVRpYeOgHUtL4Y9dxw2Qh8WGTgadgm98BPo03ZgwlAizb-Z8w0Wqa-SDPfXmbK1-B1eIUsXSqvR5oG2HqvXF5wJi_XqO-_MJbdynvaeFo3peLG4XnGs7lEevhWWaYG6TWpxm9IDdVGu0PxSsKZLIWNu3zJIHWQZy5mDKgQOr0buO9MIES1s4-LCcReJUxy-JOHkcaMX-P8jNsqGjafQ8QukHWtMKUqPaWvHyGZdORZSV7KDI5ZORbZCgESqBjU1qoJeN_Phlr1t9vhS_jCk7mXAYBoPGA-ObPFXdMiSEaAT85oL0-Wr0kl_Cx0AzQ7ygEVGROlgKJ02cgqLwa4t_R7y9DIq1tOBUcEH3snTouH7mYqLYnOaCUPMFKfkAtRuzGFRjXjnOQHNqpE7Eg6n-FB6SHssD8Mm3qTamM-mOWBajXWfwsdhcQPNATSxpsPPlrO6ZXTyccF4g2Ak09u27MZ6S4UVA8JLdFAjNPufgEOQPpNFFAdkjESw8ocmqWZ7JApwl2BSkwSFymytP2eMGTCu9z_CRHp3UYnZhjE34e3qh4DizxJ4YfmW2UrAquomlga9ulU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=tciMSDAkamx_U6fNyJspadBFpZtdNiJlEV2RTyuoj0Z37VSg_ejFXf3Of8rijsh36dvMb4OS_QiOzQtiWO_R4W9H3hB4nmUGVcVm5JVRKbYM-4eqWbkfr1vmyvwM6mEASHbIkMRPflSbSxmtpgOW8BrRW8LQwA5kkZKwUsMuvDJYb_kBWYI9UvGcIQhawm7R4dO7cEt41FE3ic238ZthMp9eGwR19iG8fgMnwUFOzl4qGT-m55VsEY9SgPo541DRsvkqv2hnX__WLkYKUaRZYOBX-kPj-EjjAyNYNM6P1u1c19XL-ONnNv2PckaDcbMKb__SvYsAkxAgwvp9ill4qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=tciMSDAkamx_U6fNyJspadBFpZtdNiJlEV2RTyuoj0Z37VSg_ejFXf3Of8rijsh36dvMb4OS_QiOzQtiWO_R4W9H3hB4nmUGVcVm5JVRKbYM-4eqWbkfr1vmyvwM6mEASHbIkMRPflSbSxmtpgOW8BrRW8LQwA5kkZKwUsMuvDJYb_kBWYI9UvGcIQhawm7R4dO7cEt41FE3ic238ZthMp9eGwR19iG8fgMnwUFOzl4qGT-m55VsEY9SgPo541DRsvkqv2hnX__WLkYKUaRZYOBX-kPj-EjjAyNYNM6P1u1c19XL-ONnNv2PckaDcbMKb__SvYsAkxAgwvp9ill4qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=QcQYrPhCTCijQkM49cVnDCQYfAYtsOwlkMHU03LpatQ2dUe4FWUTn3cbqpKea3r1J8GLdHZJ2fGQt83Mne-niV9_9HvyUsubUkfhNCrCZSET3xU3XeL9VQcQhNqetUvOZfzO-YyzGEfFc4tCtRgKqLCFTN4noNiJz-y17ArYzGm-Go7RTYy_q9WJhrtJr3bJWGxsx7JIDdZul8UDRb22jB8nI_4N_ycP1rtD-4VYv3ifHirdPoytjCX2v34oUSYnUdt0LXMABYk71FlHVxbgZNbzJSzYxW1zKVRTEp0HJWrEKiPgCRFyro45mXv_OrQBR0NJHBGakQ5-2pz0XfzLsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=QcQYrPhCTCijQkM49cVnDCQYfAYtsOwlkMHU03LpatQ2dUe4FWUTn3cbqpKea3r1J8GLdHZJ2fGQt83Mne-niV9_9HvyUsubUkfhNCrCZSET3xU3XeL9VQcQhNqetUvOZfzO-YyzGEfFc4tCtRgKqLCFTN4noNiJz-y17ArYzGm-Go7RTYy_q9WJhrtJr3bJWGxsx7JIDdZul8UDRb22jB8nI_4N_ycP1rtD-4VYv3ifHirdPoytjCX2v34oUSYnUdt0LXMABYk71FlHVxbgZNbzJSzYxW1zKVRTEp0HJWrEKiPgCRFyro45mXv_OrQBR0NJHBGakQ5-2pz0XfzLsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=BBI7PXS3dBvzvi-zDIVv2_AoAXT_kp-lzzi4eKrzHXQ3Jb2ySt0nE9Jh97889U7xvtqBrkAJYDluGcsb7NqCaH0kUMi4yjRlVIj1XUrQriiQ9p7kqT2p9UTqmMbr14RzK4W2X2wBUo0yh1zvwUk2Q4uxFKl2RhaZd2yCgSXB1wYXa9XYXQDRUeJJq1pEOqQH-Hi7OFdCr386OM0lWzfCFEH7PYJuM6KRmwb4bN0VeUbx32CPBMnBdGm9dHsZuotyKMuQcnr2Qhred_vofgZjVnjdpTcfdKhXyZN-g0X8ONuf74fVvRWDjsPiG0YbhjSY2aCy-3MuKb8rP0s_eIkFgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=BBI7PXS3dBvzvi-zDIVv2_AoAXT_kp-lzzi4eKrzHXQ3Jb2ySt0nE9Jh97889U7xvtqBrkAJYDluGcsb7NqCaH0kUMi4yjRlVIj1XUrQriiQ9p7kqT2p9UTqmMbr14RzK4W2X2wBUo0yh1zvwUk2Q4uxFKl2RhaZd2yCgSXB1wYXa9XYXQDRUeJJq1pEOqQH-Hi7OFdCr386OM0lWzfCFEH7PYJuM6KRmwb4bN0VeUbx32CPBMnBdGm9dHsZuotyKMuQcnr2Qhred_vofgZjVnjdpTcfdKhXyZN-g0X8ONuf74fVvRWDjsPiG0YbhjSY2aCy-3MuKb8rP0s_eIkFgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=uYv2XTHf0-hDX3kn5N-BLLwHRIGebH76cxdSQ9Rv_7_JokrfCIO7b6P5vZWm3ifpHOWOH03VoftN9AghefDZl9rlIT4NcZGvyfFS-98ZE3steq9FyTsvTGyIeyEpPy42JERWLNYBBkrBlb02B8sXntjzMWZ3etLyABoJj9NJBuQhySuE6wsLkMvGAiv4efrOYYUBUL_r9jWzWRPCEkyUJZdwlcXqyDhTKEnPUzNB_3eI5nMUplDr8nEq8cyJ66ROidq1lrJf-qt1huEX8q-8ffUVVLcVJZb0n3YVauIq-OmPtPhBwbMn85prmuyp-peQwTB5FJOU1SOgaKJ_aFROmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=uYv2XTHf0-hDX3kn5N-BLLwHRIGebH76cxdSQ9Rv_7_JokrfCIO7b6P5vZWm3ifpHOWOH03VoftN9AghefDZl9rlIT4NcZGvyfFS-98ZE3steq9FyTsvTGyIeyEpPy42JERWLNYBBkrBlb02B8sXntjzMWZ3etLyABoJj9NJBuQhySuE6wsLkMvGAiv4efrOYYUBUL_r9jWzWRPCEkyUJZdwlcXqyDhTKEnPUzNB_3eI5nMUplDr8nEq8cyJ66ROidq1lrJf-qt1huEX8q-8ffUVVLcVJZb0n3YVauIq-OmPtPhBwbMn85prmuyp-peQwTB5FJOU1SOgaKJ_aFROmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=AoOmitAG6aR1R4GW0azZcj-4qm01CRZQgueFfC5PdmOK-0t4914j2g_W1L6WKLeiV-61pW4eb6ZA-ZOxf34BqAc5Hz9kfpI8A43HDtoJuVjslIBXe_n1lPjlXOqfCBl3FxM0RE472pLgGynt4ldGgpt-omufeaFFMmwvVEhmz5n8atxmOiceDi33JQEf3YvnuvXYX1Kn_eBw4hsz6qOXMeFvFFhxf1uSnbgajOAjqv7lICliAuCVWXDB6tss26I-oTwrPALTgu7wrMXx2u649XStgjWSJU5rVeNgxf19DMqyic4FV_IRx6ZOA07GghKYmKnAvcose-jOz3obKPPNPRdIqnj-VsmsRQq0pU98hTPT1FSUS8hPP9XcNUki8S0kPAtO8iL-hIVWRnQ3l6BFHeIiFzU5_bIkAwzGzJH1zoPQQq5Kez-Z2PKyfKDmD8m2Le8hlOAgwaPb5jkBWUel0CN6Kr61iYYkwyWJbV8NZ9bsDw1psiT0ioJe0PTolhsT9L19sQjVezSxlUORP0eTulwf_BVjIfFIZ4SxWCeuoUL0rY9Vb97yaVPEnmrDKTYOONB0kGy7brsxnHzvir6POy35ArKVlf7iWHououhT3iPY7iP73hkqpMkakk7w9sJjjJNgkqPoL7Q4x4NPpLtn5CYAQtteqBSvcdm9slBi_Gk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=AoOmitAG6aR1R4GW0azZcj-4qm01CRZQgueFfC5PdmOK-0t4914j2g_W1L6WKLeiV-61pW4eb6ZA-ZOxf34BqAc5Hz9kfpI8A43HDtoJuVjslIBXe_n1lPjlXOqfCBl3FxM0RE472pLgGynt4ldGgpt-omufeaFFMmwvVEhmz5n8atxmOiceDi33JQEf3YvnuvXYX1Kn_eBw4hsz6qOXMeFvFFhxf1uSnbgajOAjqv7lICliAuCVWXDB6tss26I-oTwrPALTgu7wrMXx2u649XStgjWSJU5rVeNgxf19DMqyic4FV_IRx6ZOA07GghKYmKnAvcose-jOz3obKPPNPRdIqnj-VsmsRQq0pU98hTPT1FSUS8hPP9XcNUki8S0kPAtO8iL-hIVWRnQ3l6BFHeIiFzU5_bIkAwzGzJH1zoPQQq5Kez-Z2PKyfKDmD8m2Le8hlOAgwaPb5jkBWUel0CN6Kr61iYYkwyWJbV8NZ9bsDw1psiT0ioJe0PTolhsT9L19sQjVezSxlUORP0eTulwf_BVjIfFIZ4SxWCeuoUL0rY9Vb97yaVPEnmrDKTYOONB0kGy7brsxnHzvir6POy35ArKVlf7iWHououhT3iPY7iP73hkqpMkakk7w9sJjjJNgkqPoL7Q4x4NPpLtn5CYAQtteqBSvcdm9slBi_Gk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=caG1be7lYqxMmP0IUuY_-XILqhvbaTiSae09mjWLlSN56ilg6pIndkHR7OdINbblNGKWif_HDuwTrSeXMz2dtoqtfMYrXYjpA5nSW1YPd5cEnLwNTJAopPLeyCXCMSQlktQLALAxJRylDOUw3yLg2B3VJgbDew68TCor2t2jXyUbz1HEeVy0477Vyhn5K1nXOPlwCwKkFl2F7LlP3cyiiCpOUrzY7F-c0cr59L4rn0DI6PnLE56Ss0Rv0TO32k9HFKNGBOnP9XClo-Y5-C0tzvxRYleUInddPx_81RVpqkvf3iFQ4ohxywplp6L2GpCAw2CBumZebN5EoAlTHbIieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=caG1be7lYqxMmP0IUuY_-XILqhvbaTiSae09mjWLlSN56ilg6pIndkHR7OdINbblNGKWif_HDuwTrSeXMz2dtoqtfMYrXYjpA5nSW1YPd5cEnLwNTJAopPLeyCXCMSQlktQLALAxJRylDOUw3yLg2B3VJgbDew68TCor2t2jXyUbz1HEeVy0477Vyhn5K1nXOPlwCwKkFl2F7LlP3cyiiCpOUrzY7F-c0cr59L4rn0DI6PnLE56Ss0Rv0TO32k9HFKNGBOnP9XClo-Y5-C0tzvxRYleUInddPx_81RVpqkvf3iFQ4ohxywplp6L2GpCAw2CBumZebN5EoAlTHbIieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=mRJAVzelAR9SdAg-GbUKRb0bLiD2ZynPu2WzwjR7boVQeT0B04nYW3By77YiawJuCnO71yAazk1bmL5Coh1t26vuHXtlOKQFv5Tn0ZoBJlUSSXYVFZrm3E44BLBjcD2JAOmxs3MKJ5ryiVd97LtLpL_jYSyCaCWg1QCEeDIjhbdvqHMYbSoaIfyGr-B82KsAr4bZwPGmDQppxvW9ET-uJ6QVlDFBK05IXfxotBBHQTPPsxTsFzeKl2MabCXyAwHYbav9qLoG0YP9ndRY0tWww6KsjWN4tNlm05QJkRkt0iUm2WeSziJu_bcrsWkda2Vs0LeA8HepmeSiJqsFJHEo3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=mRJAVzelAR9SdAg-GbUKRb0bLiD2ZynPu2WzwjR7boVQeT0B04nYW3By77YiawJuCnO71yAazk1bmL5Coh1t26vuHXtlOKQFv5Tn0ZoBJlUSSXYVFZrm3E44BLBjcD2JAOmxs3MKJ5ryiVd97LtLpL_jYSyCaCWg1QCEeDIjhbdvqHMYbSoaIfyGr-B82KsAr4bZwPGmDQppxvW9ET-uJ6QVlDFBK05IXfxotBBHQTPPsxTsFzeKl2MabCXyAwHYbav9qLoG0YP9ndRY0tWww6KsjWN4tNlm05QJkRkt0iUm2WeSziJu_bcrsWkda2Vs0LeA8HepmeSiJqsFJHEo3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ALfPFmV4oPV-J8uDNzv7YZiUOBSBpBzryjsKFnqoepa7spLsK-MmRP3YjLH5mL7PPbopkLU-eNiFZ7ohyukWik4bYOiK3kE7Yg4g1Wp1smN0weYgXtwIVzKlGc_QyBwb9ZBeE4x7yKqjnH0FM8kZwa0jbSGR4-abzIT-pHtD-Ak__7qxxo0LQCdVEVf-qsE3AwwpU_cfCxGaCucW1-SOIlrldv-7kj4BhGNku54BhimvJOd--RwHiszXg1hiwx4o4MnNw_mI8kWqIToda6s1CFcoJ3vhd2HZK5gEL_-FS6FUduIBW73DTMBKfv6CARcQlkSd948q6O0aV6zOP3alpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=YLMAEVEanJlRmvAPgHBaKORcgG7324uNl4E_BqZEypGreGtb1E41qLfa4B4hbbG-NxgRzVAxNs4bYoPkDDGhj4bwCc7t9ePx90tNPHH0pAeCMgXFYNVAi40QXRGSZpCVPBUghAfmlnBlpqtMH9EDF3bl9uig8gz6xp_o3zAflGEhnmKiUj2J5bjR7jQhHA8e-h1JAajBGTKJWYLRXTTvJOuSsx-Wfw8k5iZQ1XkNQjsV4FU6BgZD3LPNMMtUil918prsXH30VRSWJrXdDCT5o44FPQHVAbRO_v6TD-wwlXRB06BhAnsYPYD91vssRoWE8YtXDQq6VsQwV2WyzxJTOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=YLMAEVEanJlRmvAPgHBaKORcgG7324uNl4E_BqZEypGreGtb1E41qLfa4B4hbbG-NxgRzVAxNs4bYoPkDDGhj4bwCc7t9ePx90tNPHH0pAeCMgXFYNVAi40QXRGSZpCVPBUghAfmlnBlpqtMH9EDF3bl9uig8gz6xp_o3zAflGEhnmKiUj2J5bjR7jQhHA8e-h1JAajBGTKJWYLRXTTvJOuSsx-Wfw8k5iZQ1XkNQjsV4FU6BgZD3LPNMMtUil918prsXH30VRSWJrXdDCT5o44FPQHVAbRO_v6TD-wwlXRB06BhAnsYPYD91vssRoWE8YtXDQq6VsQwV2WyzxJTOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=pqOSXYSrTYABXZDUw7wFZnniZkeREHE14_Z3nRkSXwv61vXVPc5fQFItSlJn_sFyb-Rl1QiGSBZPv0mjlgqI36IGB3-sGYA6eIscpNW3KogfP5VmLU2DKhutOHvBOu4IIAK2kwz_KuZ5MqC7oBJaHRInUh5aUv_RELXfHtdOCgjPLRIoRO8A83ATTcb7V6EQJcvzHCIZB_q_nSlhI1lXaMJDuSEAnp4BRJWsYRb9eQ4LfaLvkYeXK0ie5IY0P7gYTeqFTJYzpMdMqRqLbe6zi8ZJSk3Yupvvuopaqf1KjmJCcK1gqO_bf5YPrmrfVrkEWYIk15O2oRDCCiGFeQR8Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=pqOSXYSrTYABXZDUw7wFZnniZkeREHE14_Z3nRkSXwv61vXVPc5fQFItSlJn_sFyb-Rl1QiGSBZPv0mjlgqI36IGB3-sGYA6eIscpNW3KogfP5VmLU2DKhutOHvBOu4IIAK2kwz_KuZ5MqC7oBJaHRInUh5aUv_RELXfHtdOCgjPLRIoRO8A83ATTcb7V6EQJcvzHCIZB_q_nSlhI1lXaMJDuSEAnp4BRJWsYRb9eQ4LfaLvkYeXK0ie5IY0P7gYTeqFTJYzpMdMqRqLbe6zi8ZJSk3Yupvvuopaqf1KjmJCcK1gqO_bf5YPrmrfVrkEWYIk15O2oRDCCiGFeQR8Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aATFHvOQ2rgCGydgnlKt7mjDIB7cAVglebN4bFX6-u3Em4cezWL2QfucSWb56_0yiY0w1fJpb2t43MIrQGsqQxuZm_6EGSIuncFSKbLufHL6PWQGX8tquuqF6bXFQarJp9NiAzR0a9Fi45MWcjtbrJYe9phkgV6zy7qbm248NwtZzcI8k-bT95SLCyzqaYm67DStr3sZk95gChMtHaU-C9iGIi2RWdEeLqPgWT4xwrLW3Sa4DthNrOB1WSsjioOVKDq4i32pxvaG0zWOFpgSkFJeOaQEMxpSWRTTWzliejRkO7KxdUrNcmVlz_OA34mYPNcfPEXRLd18_YuaRTLI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=eW9_vrHlElM9WnH-7tYi34b-G0kLndRrGEp5anOoC13_MpWmwi8sXjKoHvTnPq5H-P_sV_9fjBoxmZuoGp2PPgVdn5UXt7ginYrtGhBq1ha2JskA4jo22W0wmMjopsBFEaRDfL0KCtyUH4PGlh8hY7RTGYsQFmA-9MvIrbt4EPMhC5qhiLoIEDpEyg_OxWcpya9Rs__kqjxFgu3aVH_Bzgm9AWRFmImRjUFenZjQ6e9xZbTKmcVC_IEGI7Iz6lqyVtBIpVjbU7dDHA5ClOje4OFomm8ei9iDXgHyjP86CCXxPBQrz5zVp6_vzTiMMGOv5YFLlnlRkg9eg_hjjBO_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=eW9_vrHlElM9WnH-7tYi34b-G0kLndRrGEp5anOoC13_MpWmwi8sXjKoHvTnPq5H-P_sV_9fjBoxmZuoGp2PPgVdn5UXt7ginYrtGhBq1ha2JskA4jo22W0wmMjopsBFEaRDfL0KCtyUH4PGlh8hY7RTGYsQFmA-9MvIrbt4EPMhC5qhiLoIEDpEyg_OxWcpya9Rs__kqjxFgu3aVH_Bzgm9AWRFmImRjUFenZjQ6e9xZbTKmcVC_IEGI7Iz6lqyVtBIpVjbU7dDHA5ClOje4OFomm8ei9iDXgHyjP86CCXxPBQrz5zVp6_vzTiMMGOv5YFLlnlRkg9eg_hjjBO_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=RSSdoBkqd8XJ5RpJFwr0L4NErpJTdItJBn8LaPZZxd1tkuH_LQoc-7FE5AuoVVg5yU-sJ-pM752JzMEzXu6HslNXSDnFQvrKZy9tgrHeq3RERBHScGvM3MvA1gVEjG4Ce7Y3j15wmzpmvvyLmlKDDuFgBfwsvSkddMR0gsgm4G9hg4Ir8WO9WFMuB_L9eeQ5YE6zIJgT5q-LQOY38lBFWgNCoButOwJg1gfeUobwjdeX0JhiyNaEsCHdmnlz-wPJg5YtxmvhxhyFigkx0JjydtPxptzCmfIP0Xv53pr_OZWPKM2nGb9CnD8Evu_Ow87goYV3bQ-3hAJqBpfiiYxLMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=RSSdoBkqd8XJ5RpJFwr0L4NErpJTdItJBn8LaPZZxd1tkuH_LQoc-7FE5AuoVVg5yU-sJ-pM752JzMEzXu6HslNXSDnFQvrKZy9tgrHeq3RERBHScGvM3MvA1gVEjG4Ce7Y3j15wmzpmvvyLmlKDDuFgBfwsvSkddMR0gsgm4G9hg4Ir8WO9WFMuB_L9eeQ5YE6zIJgT5q-LQOY38lBFWgNCoButOwJg1gfeUobwjdeX0JhiyNaEsCHdmnlz-wPJg5YtxmvhxhyFigkx0JjydtPxptzCmfIP0Xv53pr_OZWPKM2nGb9CnD8Evu_Ow87goYV3bQ-3hAJqBpfiiYxLMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=BHSHNvLSuHbB5JoCW5BMVtB5yGIt1bNinJbGdWA1lJBS_5MfPQ1Msem5gIvdQbHEAo8BGR5nvXPB2Qq6BEDvA47ZfuHytorKIP2nrFuLNFfCk7gNBrcLtIMwU3b3RNf4_HrgCgiovHSiEGwWc2u7AnbCxKOQaLMkb97h6hjOMAOueju92QcT3RrKM1fo7OQAMlG9tbFrZWlwvfeWfQ7ghxYGgi5KKhZn3Ndcvn2hKGkO8rEzISUrE59VaajED1c5w6QyfCbHoaj3A2N538iQoWzndmgbwjPt8rntl4ip2fpeJS2A1B90vh_-Mtn6FMwTBmg61ql-WOm8JAHwgHXl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=BHSHNvLSuHbB5JoCW5BMVtB5yGIt1bNinJbGdWA1lJBS_5MfPQ1Msem5gIvdQbHEAo8BGR5nvXPB2Qq6BEDvA47ZfuHytorKIP2nrFuLNFfCk7gNBrcLtIMwU3b3RNf4_HrgCgiovHSiEGwWc2u7AnbCxKOQaLMkb97h6hjOMAOueju92QcT3RrKM1fo7OQAMlG9tbFrZWlwvfeWfQ7ghxYGgi5KKhZn3Ndcvn2hKGkO8rEzISUrE59VaajED1c5w6QyfCbHoaj3A2N538iQoWzndmgbwjPt8rntl4ip2fpeJS2A1B90vh_-Mtn6FMwTBmg61ql-WOm8JAHwgHXl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=p47XpbnCwi-UhO4shArH2QAkL0kejIclbkXX1t2tYTEADZOK9oWajbNbV8vSZe-xh6oVugvbFXqUllEbgLg-VuI9OeJzghkO9dMPa64CKeMjUbOqKMFNg-cmjHIPVkIMhtYTUYY9AlSb2BdgDbO3-r1S1E4QjEYnWRSWCcFe8P1dX3ymPw9oF6Qst4MK5gaAB_-Ip16TRTqo3agba7mrKZptgzzRe8-Oxc6gktAkEckkgIQpmoTGHNWOS8ZnCfVPR6e6F6UOmY8dFi388dFxTTc4q_p5_OzRYd7sPxn6gZextoIL_wk1FOrxzou28Z7-Qo6ttRHwqrT8qcUWl0NIeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=p47XpbnCwi-UhO4shArH2QAkL0kejIclbkXX1t2tYTEADZOK9oWajbNbV8vSZe-xh6oVugvbFXqUllEbgLg-VuI9OeJzghkO9dMPa64CKeMjUbOqKMFNg-cmjHIPVkIMhtYTUYY9AlSb2BdgDbO3-r1S1E4QjEYnWRSWCcFe8P1dX3ymPw9oF6Qst4MK5gaAB_-Ip16TRTqo3agba7mrKZptgzzRe8-Oxc6gktAkEckkgIQpmoTGHNWOS8ZnCfVPR6e6F6UOmY8dFi388dFxTTc4q_p5_OzRYd7sPxn6gZextoIL_wk1FOrxzou28Z7-Qo6ttRHwqrT8qcUWl0NIeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=L9K0Hq69pDmwiIT6FS77kcJ4tAJ4QAXNXwgh7NcYuNbvuSBZAACM_4lsPxGZO9sOrgeX6ZRoXEqlDeOaq09iKTD1n3Mwl7A1TG_SVjpmmWPL94ih7Bw-TnD7q1eS9bSbkfKS8N-Yv_C8jONREYXSwPm2-Zn6wYINppWfWM9HIEWXqq3T6_qEmpTbxOT4oxFgeyKkLjHvlR9uJPIjyK_e-e5Rg-qyqyfR7TvVybyP6NF0zxWL58oUs0DKnNfXEK8QHjEIY_V4jJhX4OJb6xHk8DWlInDMNKg73BhrOVG_gKb_anv6er3xKa2-BRtUly_z-0qkW6M6cMj0hIWTLg3WWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=L9K0Hq69pDmwiIT6FS77kcJ4tAJ4QAXNXwgh7NcYuNbvuSBZAACM_4lsPxGZO9sOrgeX6ZRoXEqlDeOaq09iKTD1n3Mwl7A1TG_SVjpmmWPL94ih7Bw-TnD7q1eS9bSbkfKS8N-Yv_C8jONREYXSwPm2-Zn6wYINppWfWM9HIEWXqq3T6_qEmpTbxOT4oxFgeyKkLjHvlR9uJPIjyK_e-e5Rg-qyqyfR7TvVybyP6NF0zxWL58oUs0DKnNfXEK8QHjEIY_V4jJhX4OJb6xHk8DWlInDMNKg73BhrOVG_gKb_anv6er3xKa2-BRtUly_z-0qkW6M6cMj0hIWTLg3WWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1ghNxJE6cMQJ0rje4qUTuozpl2-7IUSaIUFvxwo5BO4p1ogkdqHJjqPWuzfThRKJB5-bRHV_sCCWyLDcROQx95fUBrOZCQe-RidNfH6wzK07yl896Sxk-oLOnel1DY2ISlQHBeGUwsMG4XzRUXvAEiqh7PdjeZlKiwch6LnWHaHDP25a7XZjlUSJFZmFcLoTRN15J8KgPJfkg7inNibDAcrfPvcHwJBVxp3TDOyjS4NOKmHVLHSZQKz4Y9_P270Ce8K7A4AsmunQYmsUJvV0NHWJlyIlc5sd68l_g6chjsMH4y9HNDasFfeNMraz_TdTq0MHa3J5avSAtfYBGXHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq4Y2rZohQc67KpqJRv9kyd_mFYr1iVSCpjC6sONLE7lzvJx1HJ6Bzsfk-VCqRREDxZaUUQalimTTWHQgk_H_Ir-dlu4m-4xA3hVP2GLbe-SOdXsopwoljFT0K-hNwInK1rOSliwaB4N4Vhe69lDDzasJ5tZ5vnViyvtZGAtYcq67lE45wZ-JtaCLg-PB17_ozOH7Vvyzv8Y1RP_3sF4f8rK_wakQR03qtyzY-nHmPUhyxrDuieGWor3iZ98PvfRlEjVNlLMgPIKUCHYDINr8Po1NMlRoNWd1F_nOINmOKfGfSazHlWlKYx5ofg6Y9fCpnt7AMpVlB-Ks1SldxF6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c588jOSAlSi4Xjyzbp8AwrK_38-FeoDQqpypLKdFAOSuQ8Jwu8KxJL754viMC2nEJacqllnUGJUwIB5EAgxfSPZsLE0A12CISltOqPdM37q-h4WLPdEzHW_k-Dg_pALN8PPZ3-eBJuRjYJKVt1P3oNADH0NpQyefwt3d84eoBzbbr5BYmoq13Rt5fCKgPkxMDoh1YMMbHHPBkndbipAxq68xyqzVsd7pO1LocVYd0kfHZkctbrt4UyM6XxTJtJ6-SJF9eBUtI96y5YdBCzllRpDbXWRU4ppiyAPGPHRkuHjcOacC0k7FHHbYC5KXvCNIIQHrtrfYkLVd5gncq4UwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp5wOktku1bpIuqz1SZsv1EVF5_rWMxxezYgM-gZvXo_zVrnl7DeycdiJtieeFgdmQeLc_6bBpP1z0Pcg4GKnluX3cXAu6LniL8_mvEssImkbU1PWexHWbJ8nvJHB6fUH-XpLs0UMh-B_v1aAwIjvuzMmCJlpA0wZYlFS1WnJX2vjiQjEoFxSka5Agz4fym_OVlg_dgb4BWxG6CFb7WjImxv9w17amx1x9-JvWy6iX6OxcgUkKhL42y5Qjy-eTWB4JKqlmRP5LA9hz_wkZ1A6m1rEboiClB55Dxoa30n6ml7n8u1h97GPR9W9oYB9Enfv0XGlnp34l1beO59OmF5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwwRC8HxEeaU2JN8XtJmjUq-F9DJ9GhLmvtSx9NLiOpcYb9y3uzYeuvpd4-_mk6hJ8j-Dydl1c-V5kvInwOVOPvDLMz8QOYzwPGQLqTGDGyQAnZkXUm846WCycWBjboZAyPXIHnMsyw5M-y8gKnIWDLJ3lVrEhsCnWZ8PAs9fcxL1q1ncD7tfB-ek2OF4jz6iDe_p5gZzxnwqqGsVdRSsUyqx5gGJZeK-6xGtLQBdA5IxhBwgQrziuuINdMs5PqYXBj0jH_WL9EiJhB2oNkCMM9lfSKvt9Xh09PdVMR96ZS-bkyUd_e_t-gJxzJcF9gyWJA9tNwXDWntXjFMgVpgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMoMMY-VqRMq5pFMHqrNIUV3NkrRoG9gim0YV_qkXgMM64JcPQ-NlSXP3J9so8wIl6QwOlLYgtlkEPuF2MzBqqzVr_X-XcnXBIQDN0pJoL-J9AU7UCyu-tZkru3SUw0V3RlF3LHi4YY4KaEeNAM2WrHkZYxb3AeSedFn_7i87ui8bApywTNCM0WeAUrB3mSL865YJPRumpX3kS1k4RHdnWQURkhDxQThivRPU879Ec48HubaO86EfTYJuM1P-cUN4AoTplREyhLeQ-_m-U0dDZkVB3cbx9WhSmDN32vMCoETiBL6uzWrAMKKnHsZEMbVDyCn6vfAj0gywzWVyuVp8Cfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMoMMY-VqRMq5pFMHqrNIUV3NkrRoG9gim0YV_qkXgMM64JcPQ-NlSXP3J9so8wIl6QwOlLYgtlkEPuF2MzBqqzVr_X-XcnXBIQDN0pJoL-J9AU7UCyu-tZkru3SUw0V3RlF3LHi4YY4KaEeNAM2WrHkZYxb3AeSedFn_7i87ui8bApywTNCM0WeAUrB3mSL865YJPRumpX3kS1k4RHdnWQURkhDxQThivRPU879Ec48HubaO86EfTYJuM1P-cUN4AoTplREyhLeQ-_m-U0dDZkVB3cbx9WhSmDN32vMCoETiBL6uzWrAMKKnHsZEMbVDyCn6vfAj0gywzWVyuVp8Cfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=OOZNje_JDS6vqStzdqogHVAY04b-THKEfJiKcdw-LrOD0F2kD9sGyn_wIwG3Wzw1zpME11EpHgM3aDClz2x4p_G0uxPV7ILcXxQB-act1Xi-x6Ye0Xb7HuFyaIA-nWownIV8RUlWqPOAdjsMp-dbwjwBm2EswBILPcYDCy_QjYAIH_whhudXlUSayzZkG89_3t2rhx7ooVCUaZcdnhgN78wIX5Y7l-dpS1iIUzvkjA8qBcdmHmkqAnYKa-_cyIldCuNeID_n7V9tRxqLMgYq2meF6UIh5UqV1jw8tYyylHWtEdrC5XBs6NVd_LwTVNi5V27yuYIh-kN1XwsFFg02Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=OOZNje_JDS6vqStzdqogHVAY04b-THKEfJiKcdw-LrOD0F2kD9sGyn_wIwG3Wzw1zpME11EpHgM3aDClz2x4p_G0uxPV7ILcXxQB-act1Xi-x6Ye0Xb7HuFyaIA-nWownIV8RUlWqPOAdjsMp-dbwjwBm2EswBILPcYDCy_QjYAIH_whhudXlUSayzZkG89_3t2rhx7ooVCUaZcdnhgN78wIX5Y7l-dpS1iIUzvkjA8qBcdmHmkqAnYKa-_cyIldCuNeID_n7V9tRxqLMgYq2meF6UIh5UqV1jw8tYyylHWtEdrC5XBs6NVd_LwTVNi5V27yuYIh-kN1XwsFFg02Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=Nf5N2ZggNMn6unnubITSk8wr03D79KzUFbBSDoVTyxY3VKPcA0ERSaRHQ6MHG2nWzZOTqQgyXKpvFFY2TObOq38_CbJU-HN5VWIus6OaLWgSCnMiy4vWi8lLj24zPDRmoWHpnUCJZu9iT5iT4uFPzgzeHrF10pdaKuXo9sPQ_sd3vNnlOTYn3KL1k_tkG_QCz1xoyuQfPt0ptbhzCVXdtdvjUNu_VbiYqa_SlO7H7TmhlUFeJVfMt3mf2Fz9OJhEVpsJhK7pbeoUoJ1Zwil_QxbVrAaGGLBaiZ9EEcbC-H6QlVC2zupWkJFz2ebZ0Ajz9UcVwa75EbRbLW3WPKeHozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=Nf5N2ZggNMn6unnubITSk8wr03D79KzUFbBSDoVTyxY3VKPcA0ERSaRHQ6MHG2nWzZOTqQgyXKpvFFY2TObOq38_CbJU-HN5VWIus6OaLWgSCnMiy4vWi8lLj24zPDRmoWHpnUCJZu9iT5iT4uFPzgzeHrF10pdaKuXo9sPQ_sd3vNnlOTYn3KL1k_tkG_QCz1xoyuQfPt0ptbhzCVXdtdvjUNu_VbiYqa_SlO7H7TmhlUFeJVfMt3mf2Fz9OJhEVpsJhK7pbeoUoJ1Zwil_QxbVrAaGGLBaiZ9EEcbC-H6QlVC2zupWkJFz2ebZ0Ajz9UcVwa75EbRbLW3WPKeHozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=eUaYQ52la9B4xkJ4WRR2RaBRwzOXHca9TEOWpCR3FKrTfNsD7HbJ1pCkff6dKWlmgtZ56LIO391pRwwC6zVelOFaBe6tNs7tBmeIoTDh-8O7r9gNnNvG6I9r-S8G6vDQZPH5j2kscJhrxeK65lCrr8FnvDYFXotPvHGVxqW8RZn374QaeAC9zc834UegjiPt5K2NJU_-7Bq0p6M9FDQazeEoemZySu4R6eppOcx9LiNccXBWC8qT1odHYdEW-ob-5IA7sS5CWDne81Mc3OR7mCKOBlclfOU7SY-bs1WC5GRysMter9s9Kn1Z6Kac2nX8KiSTBcrUuRQPgwRdtc0H-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=eUaYQ52la9B4xkJ4WRR2RaBRwzOXHca9TEOWpCR3FKrTfNsD7HbJ1pCkff6dKWlmgtZ56LIO391pRwwC6zVelOFaBe6tNs7tBmeIoTDh-8O7r9gNnNvG6I9r-S8G6vDQZPH5j2kscJhrxeK65lCrr8FnvDYFXotPvHGVxqW8RZn374QaeAC9zc834UegjiPt5K2NJU_-7Bq0p6M9FDQazeEoemZySu4R6eppOcx9LiNccXBWC8qT1odHYdEW-ob-5IA7sS5CWDne81Mc3OR7mCKOBlclfOU7SY-bs1WC5GRysMter9s9Kn1Z6Kac2nX8KiSTBcrUuRQPgwRdtc0H-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdmD366BtN6aAwywA0J-ZxWf-5hxi85sFAxP2tBaU81G1wNro-tMKle0f2VRaYTraPv5783OJ60qmsl46FJkdlDRyAtFeK38f4xsvHhgJ6GozpiiU62FOihAp3K3CMK7BjPOB0tKq1XCS9w8G2jlAtLTGAX7cHU1yXXZ31XWWC6ozP0nNklNmOu80Zt3WagbuPEyocD8jVxfGBZvN3gV4iNJXhxTtLB5MoU51_5JTaw7mpIgcnWVxCqsXTNxMWqeAS6Go3wjZ7u1aWtoos3Cx4G2dCBPU4t-W5DFRHsNfGLVThMe8psoouGPWmQDBXhxVvE9tgl0m_QbDXfKtU7D8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
