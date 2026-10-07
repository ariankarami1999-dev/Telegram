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
<img src="https://cdn4.telesco.pe/file/ngRiI43z79T5slZA7coKcTX33-02lPZQaZzaDwAGESXqsIPfccW2UIz5i75jg_Z1h8zdh6Rj5RSnzMSXhLuTKC1XP-FTcSAd-st7jmniAz26nmYvjt9agHTSWn146UtFrvT8nE7Mc4LrnEYdPlMCxduwcH4TdOJ-T8-w6EUqtedMnWIfyjjWopwvgYPhdVBwqtyRbxCrRHGdH8IS31hLd_82jD7f-5Pf3VTPbme11RrHtKpVgibvQOBFGngZhABPVK6khmcL959uMRYkeHQRbnVQRPSp87ffHCUCToHXnR6EhYZnrImm1YSDI4ZxEFN80E7KUFiLc8PpSxLuUZeZ2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-72907">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=n07azNhjZaff3C1EfVFBEPty2P0pP2xbervo_Z-aiQk32X-IHjPBPKKa8tYNNF0TzeXp1wOgPUjwN5J-j4iXnaPpS_Ydhecc0w9HKDoJbE3VejnIAiucXXzvERdY-qWgtbkPd1UrUnYeY9GMYruVuA2bt36DGiwiFGM7gieYNgpo6ohg2_6D_J0cwTYOc4Ce_8WJ9KWNc7sue0ehkDX2Bs87_W2XcbKu-hP5cKAfn1y-B50vfl_XvK4DCSySSN9o1ApXDR2CRn--76iujOYTzhjdnQ4jRNIWCXfJEznPfd_iopT4L9Gadwy-STl6KOgYL-pAqmdusCxpP1LGEZHP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=n07azNhjZaff3C1EfVFBEPty2P0pP2xbervo_Z-aiQk32X-IHjPBPKKa8tYNNF0TzeXp1wOgPUjwN5J-j4iXnaPpS_Ydhecc0w9HKDoJbE3VejnIAiucXXzvERdY-qWgtbkPd1UrUnYeY9GMYruVuA2bt36DGiwiFGM7gieYNgpo6ohg2_6D_J0cwTYOc4Ce_8WJ9KWNc7sue0ehkDX2Bs87_W2XcbKu-hP5cKAfn1y-B50vfl_XvK4DCSySSN9o1ApXDR2CRn--76iujOYTzhjdnQ4jRNIWCXfJEznPfd_iopT4L9Gadwy-STl6KOgYL-pAqmdusCxpP1LGEZHP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجایی که مشاهده میکنید تگزاس نیست، کوهدشت لرستانه که یه چند نفر با همدیگه به مشکل خورده بودن و تصمیم گرفتن با کلاشینکف حلش کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/news_hut/72907" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72906">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXlXro9wdaigkDFBr4v_co9MQiSgXZCg25eJnf1Pf5E0GQcYUH3roQp5sX8DX7ZMx2LplyE2sq7aC0QHtRlWCFT70wTUVT_DDD0NVXYEG-xVNr6IxoHyOLT_ya0Z36dFuwd5CYIQ30UVch9q714i7q5wapzlK7HPPm8DuVCi-WNqvQWK6ZE1Cn3E7kas5zrVnv6J3PjRmHLRhzXtYC4y0zIpy913FtPXdviXiyy8FQBjIZzYcoAp5Mg3c8iHTdQjYgdcs7FIv3SbN3sXhsGd62YrLfSP-fQKhsWPyNSoDjBho3r1CO-jh313ADFR1lNjBNRKMgNrBI67feHy8DqdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه
!!!
طبق گفته منابع رویترز، قرار شده به هر خانواده ۳ هزار دلار پرداخت بشه.
حدود ۵۰ هزار خانواده که خونه‌هاشون تخریب شده یا از روستاهاشون امکان رفت‌وآمد وجود نداره، در اولویت قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/news_hut/72906" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72905">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=JkQyy7GJvPTobNXNY2Hjb5LGpu7iYVr-4NRb9cNS4iVxe2pWktwS614EvLJ745yelJRgN7RPiowmj2DNK409-hw-9iJ3iFMAcTwfB6HJpl9ueSZb55iUvjfLW9XQH6oslQk6h5qfLWNvK98kuXgDtgSr2HaTis-QqqnWnPAX_646XTCHUDVtoKDRvAndos54ojy9FOylfek0N6uy5wfSFwgavD6kioML5aW3m8rSs8iawbx-zsmY6qHN93M1fyVcnlCYcvXmVsZo25zlj7yXd_wwsHCI3cPtF3CCIrSX3PrS9g5tjysXZKJd6zTKXVJvgMP8Ri7R1l9c4Ad3zpB6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=JkQyy7GJvPTobNXNY2Hjb5LGpu7iYVr-4NRb9cNS4iVxe2pWktwS614EvLJ745yelJRgN7RPiowmj2DNK409-hw-9iJ3iFMAcTwfB6HJpl9ueSZb55iUvjfLW9XQH6oslQk6h5qfLWNvK98kuXgDtgSr2HaTis-QqqnWnPAX_646XTCHUDVtoKDRvAndos54ojy9FOylfek0N6uy5wfSFwgavD6kioML5aW3m8rSs8iawbx-zsmY6qHN93M1fyVcnlCYcvXmVsZo25zlj7yXd_wwsHCI3cPtF3CCIrSX3PrS9g5tjysXZKJd6zTKXVJvgMP8Ri7R1l9c4Ad3zpB6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/news_hut/72905" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72904">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=VgclEwo3KsolDYjH3FjKMuGCCOnZ-g8LjNbtnAHZIjiSEHcLPDTTevEBFNZn3qVw6rxM6376xPH_Vapg8R7HA-tDTacZg7XNZ9nvThb3Xqy7mn5JNagxtJCtwrxp2hww1tldOL_Dkh6QRsv0bwh6fxr3CBfvCey4JoT9-sTH_di7VU4B3WvNx1BOEjYaeMnbbUcjbOPr2WzLKUcsHP4deK3WIAa_kb34QlXu8GDXzfuYXFH0j9bqjyeu4zFrUg7QpfOTLBd5rwmtu0dfkP-86jaGbxvZalZxNBAUyKagO-nWAXUidiKQw72oEYIrie9Z-9EuoX94lPpsHFF43xvs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=VgclEwo3KsolDYjH3FjKMuGCCOnZ-g8LjNbtnAHZIjiSEHcLPDTTevEBFNZn3qVw6rxM6376xPH_Vapg8R7HA-tDTacZg7XNZ9nvThb3Xqy7mn5JNagxtJCtwrxp2hww1tldOL_Dkh6QRsv0bwh6fxr3CBfvCey4JoT9-sTH_di7VU4B3WvNx1BOEjYaeMnbbUcjbOPr2WzLKUcsHP4deK3WIAa_kb34QlXu8GDXzfuYXFH0j9bqjyeu4zFrUg7QpfOTLBd5rwmtu0dfkP-86jaGbxvZalZxNBAUyKagO-nWAXUidiKQw72oEYIrie9Z-9EuoX94lPpsHFF43xvs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
مجری: «شما در سازمان ملل گفتید: «یک روز، که شاید این روز چندان هم دور نباشه، مردم ایران آزاد خواهند شد.» منظورتون از این حرف چی بود؟
نتانیاهو: «مردم ایران خودشون می‌دونن چه زمانی و در چه شرایطی باید کاری انجام بدن. وقتی زمان و شرایط مناسب فرا برسه، اون‌ها به پا خواهند خاست و این حکومت سقوط خواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/news_hut/72904" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72903">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/news_hut/72903" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72902">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3tnzkPZTU41i8Il0x8yZFj9z9slzoa0_mQMl131aSd4jhPwmrmQQwE40KyVrBedVpXSjQDsGMSATypM4-24iSPc0rlxmgfxKlYaNKTZTfkrLrk3AxjwGvS_7_nvFU8Qx3zjBCMUUtzfE5L5UHSb1ZXfYWnsaPsViEoiK5GB12a8i5pQrCjfZMwOKYcPeyvjsCm_lgTypKlOdm5-oaDF-fAh3VCiYVdk-NWMg3k4aekdOu4NkGQPGLQLeZPpUn5q-W14kAuXp0JGtj-DwyYpj8ULBaQJQVVBz700dh_CAzWXGNQGesgnnPcUeJXcMsRVP-8vk7vg4_oweMqGdxxWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/news_hut/72902" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=C18I7yR7tqU0dMtUO4byQ4XqW251nY5ubY6MsihK_LWhnxtS_iJjqAGBiVogeqwVYRu8zhrU75cKPnxOpYGsEHG5m3f7uDEQZf2WoppixY-QONJc_dhjtPGtlvu_mmVCFdKVCTG3IgdNiQx9wvB_iVpHdWut2VSdSQtbj-Q0tSrwCYQ5XH80kRm5S1tLu2AXi0YeaxVunu3BRMddiZhYkIij16XlPzrJwT-lz49_zLyR47acbTyl9gRJOfy-vRhMI81Esww8wri0ia_hrkEtXlJ426cr8fR6IOWJBfwkXh7_hKFUx4Nj2kQxrR-XmTZYZ08Ey-E1QI2GghsgUof_iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=C18I7yR7tqU0dMtUO4byQ4XqW251nY5ubY6MsihK_LWhnxtS_iJjqAGBiVogeqwVYRu8zhrU75cKPnxOpYGsEHG5m3f7uDEQZf2WoppixY-QONJc_dhjtPGtlvu_mmVCFdKVCTG3IgdNiQx9wvB_iVpHdWut2VSdSQtbj-Q0tSrwCYQ5XH80kRm5S1tLu2AXi0YeaxVunu3BRMddiZhYkIij16XlPzrJwT-lz49_zLyR47acbTyl9gRJOfy-vRhMI81Esww8wri0ia_hrkEtXlJ426cr8fR6IOWJBfwkXh7_hKFUx4Nj2kQxrR-XmTZYZ08Ey-E1QI2GghsgUof_iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تریلر Gta نیست، ایران خودمونه!
چند روز پیش توی بازار آهن تهران، یه نفر با ماشین میزنه به یه موتوری و فراری میشه، پلیس هم میفته دنبالش.
چند تا تیر میزنن به چرخاش و در نهایت گیر میفته و حسابی کتک میزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/72901" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=Whi8RWH_kDQq55IhMuPK_Yf9As6xXhiXfS6rwCmeFhYpJOicciDEc3uyRhKR5kc81WqpBeUa_Sxhof3_KZjiLplm9f0c4EIGFmAk5FFrmHtLWzhput2yx_HyBKFJ1rb8EAfXXv1e6w-07Qsuo9T31teXg3TAbRFUWpAhjb8L0PKjS9unJUQjuPAYUymbL0qlJXUJjt_eLxQtEs5WoEL20rPSeLO2aYcSO9aVrRBFAUuhURRHkyZ5BgcQo1I3WqOFZLfZNDN-H5P7CC-Lm65bkA2cXOqtzchv4L36m7v6acXmJnXNcl5wriyu8Poq9SKbnqSpq8HJaxQbiiJWcy9OIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=Whi8RWH_kDQq55IhMuPK_Yf9As6xXhiXfS6rwCmeFhYpJOicciDEc3uyRhKR5kc81WqpBeUa_Sxhof3_KZjiLplm9f0c4EIGFmAk5FFrmHtLWzhput2yx_HyBKFJ1rb8EAfXXv1e6w-07Qsuo9T31teXg3TAbRFUWpAhjb8L0PKjS9unJUQjuPAYUymbL0qlJXUJjt_eLxQtEs5WoEL20rPSeLO2aYcSO9aVrRBFAUuhURRHkyZ5BgcQo1I3WqOFZLfZNDN-H5P7CC-Lm65bkA2cXOqtzchv4L36m7v6acXmJnXNcl5wriyu8Poq9SKbnqSpq8HJaxQbiiJWcy9OIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم در جستجوی کار:
بعد دیدن یه آگهی منشی مطب با حقوق ۱۵ میلیون تومن رفتم مطب اقای دکتر
خیلی همه چی هم شیک و با کلاس بود؛
وقتی گفتم برای کار اومدم اقای دکتر(آلت متحرک) بهم گفت اون ۱۵ میلیون حقوقی که نوشتیم فقط ۶ تومنش برای کار تو مطبه و اگه ۹ تومن بقیشو میخوای باید به خودم خدمات جنسی بدی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/72900" target="_blank">📅 17:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=JdETC5TZxkteGvyyOJWZwIMAqPqY-XaLlh0i5lKFWCJKawTLfwcaQ8W43XHnjmWZDgoAJAV9g5QVPUg00kFMUBhzgMcEXnNCn2g3Zg12euThtTKDcZf6DtClhglhEiIUETLclG05eUn_OgXTpvsEMp5TqBqGdhs_VQ4kpqZ5leg9teE3qJy_kNp5YbUiGJKlhkorxmr1HBkNTX5k4UsbJURnNfgKQMb0WfTc6SdjYDSAz_whdXExJEr3Js5eC70wnv0oYMvJuM5NsdT6EPCmNq_71FEXma0ePM3DaCHgS_1Q8tuAOQsCXdngUBS-kKH4oGHxZuX4F1PleS1669OFhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=JdETC5TZxkteGvyyOJWZwIMAqPqY-XaLlh0i5lKFWCJKawTLfwcaQ8W43XHnjmWZDgoAJAV9g5QVPUg00kFMUBhzgMcEXnNCn2g3Zg12euThtTKDcZf6DtClhglhEiIUETLclG05eUn_OgXTpvsEMp5TqBqGdhs_VQ4kpqZ5leg9teE3qJy_kNp5YbUiGJKlhkorxmr1HBkNTX5k4UsbJURnNfgKQMb0WfTc6SdjYDSAz_whdXExJEr3Js5eC70wnv0oYMvJuM5NsdT6EPCmNq_71FEXma0ePM3DaCHgS_1Q8tuAOQsCXdngUBS-kKH4oGHxZuX4F1PleS1669OFhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی از اینستاگرام پکیج پولدار شدن خریدی و خیال میکنی دیگه کار تمومه...:
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/72899" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=u45ry_UeSiRvKPUaQ4tQXg_FjfZQcjUb2M4PDFZ0SD-_ogC5mMOrisdQ8YTrgeGs3Mcr7LBD6qYgvEVca8R2ckHVR5CQAwmUqj04kfiYYKV7nXXg4sxiJh3bdiZAwh8KFkNQ2dWz4Gww2GWmb62yq331_w6fXkN-YPghVoQyn84DzGKlUkFeL02kzlPLaSRXaQnxosBvs0_dVhWuibHcXHgKoymOPEbZBwUHUv7-PQihil5QFDgfoCqZmTOH2LRbmNQB55llLRWJM18f5A2VYD18gxDOilmbjQ5GcTvgL5opUw10IsJbwh1J0CzakGvzC6jXs5E7xVZpxVLLMuwqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=u45ry_UeSiRvKPUaQ4tQXg_FjfZQcjUb2M4PDFZ0SD-_ogC5mMOrisdQ8YTrgeGs3Mcr7LBD6qYgvEVca8R2ckHVR5CQAwmUqj04kfiYYKV7nXXg4sxiJh3bdiZAwh8KFkNQ2dWz4Gww2GWmb62yq331_w6fXkN-YPghVoQyn84DzGKlUkFeL02kzlPLaSRXaQnxosBvs0_dVhWuibHcXHgKoymOPEbZBwUHUv7-PQihil5QFDgfoCqZmTOH2LRbmNQB55llLRWJM18f5A2VYD18gxDOilmbjQ5GcTvgL5opUw10IsJbwh1J0CzakGvzC6jXs5E7xVZpxVLLMuwqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از سورپرایز تولد علیرضا توسط مامانش. دخترا اگه نصف عشوه علیرضا رو داشتن سر خونه بخت بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/72898" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72893">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLE2g-fCSryCzljLb-D-HjZCTaNo16suZbGg8Yc6pTBOdTMzp4iolk7iocZq_6ovX39Pyv7xhVpjOlMZQy4WZN9R0C6WzmkEf4dmyC4GD4wnfKPU4jMcCtrmy8RB3HW-qhLCH_oLHh3UXtjjNb5Oz-ZoI3vECEKmo7EvfgRt7gbmaDc5kQSDHzl3RaeaJB2YYYu2eIP2jwaOkcDgFx_4aT55vRH0Io0Vh06W29l5E4X0woTReBq4zeT1yEp4gFHS0Ft12jcfR-wohF-93Vyo9Qwvl66VOXCdLZA48kKShmAsWS1rlBBKQsXjY7JM9VuJ0esZKZXuuXezJk6uEM_mfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFJIlIi5iDnsHQCbn8MkqgTOXZujakpes54ZR_GJqwtdD0UYp6pKH-_dAQoZSkZFRUfJWy8xcMgpeb3MypDBfq5KNVutyXmfTU1rrK0jhk-rW6TPmFAB_qLLVfYvpMord6D8tkSAm1EEqhEGX7yq98xB3qcDpnnkP35xUVwqs52NfAExhQ2ktAUapiW1lNXtc4MwqJ5M4udNA-8pBCAdQIvwc_bFw37_Z5OffiFPV_lsWEMMxQiya5_q12n71kEhjLUPPEDnqKm0VqugsjhycV0R-iOZ2GzgsNy6iuEnR12fbvbq0EjOkhjWXM2XrFsoxz09H2P_GMieMLa0mVTIIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=Mhr_vNGotDc0vZk-bTBZCGaHi20bhd1QDhs8BPG6YxCzggzUsOGCSNtJUMzZKPVVvK1zJyLLsljcNM0VksvbU3y0idjG8Ojueh806wBGJEZJRa5jPVuf_CNSG_g6rGf86jWlwjdVW-bFDKp-ctTTrMaM_0rBz0FsVEvtnjOfjNT_N0XStCHqbTsxUNpM6L9aAKwzm0X94O1M3A2gm9Kzll-YLGmjzhs8nlLusyW4ZQmoGkHj2M9ytuiSyEMACYH5aGq3WIYckVNCTCh9rYOLDnShOJLHmq6NPFFUnIoOAoL-8NlLYtrnC4VYo_RjpgS9Df1hLaUB973gS-NGWo4zhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=Mhr_vNGotDc0vZk-bTBZCGaHi20bhd1QDhs8BPG6YxCzggzUsOGCSNtJUMzZKPVVvK1zJyLLsljcNM0VksvbU3y0idjG8Ojueh806wBGJEZJRa5jPVuf_CNSG_g6rGf86jWlwjdVW-bFDKp-ctTTrMaM_0rBz0FsVEvtnjOfjNT_N0XStCHqbTsxUNpM6L9aAKwzm0X94O1M3A2gm9Kzll-YLGmjzhs8nlLusyW4ZQmoGkHj2M9ytuiSyEMACYH5aGq3WIYckVNCTCh9rYOLDnShOJLHmq6NPFFUnIoOAoL-8NlLYtrnC4VYo_RjpgS9Df1hLaUB973gS-NGWo4zhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۷ اکتبر، سومین سالگرد «طوفان‌الاقصی»؛ حمله‌ای غافلگیرکننده که سال ۲۰۲۳ توسط حماس و گروه‌های مسلح فلسطینی انجام شد و حدود ۱۲۰۰ نفر در اسرائیل کشته و ۲۵۱ نفر هم به گروگان گرفته شدند.
بعدش اما ورق برگشت؛ جنگی شروع شد که نتیجه‌اش ویرانی بخش بزرگی از غزه و کشته‌شدن ده‌ها هزار فلسطینی بود. اسرائیل هم از همون اول گفت قرار نیست ماجرا رو همین‌جا تموم کنه و دنبال کسانی می‌ره که در حمله ۷ اکتبر نقش داشتن.
و این وسط، فهرست ترورهای اسرائیل هم کم‌کم بلندتر شد؛ از فرماندهان حماس و حزب‌الله گرفته تا چهره‌های ارشد نظامی و امنیتی جمهوری اسلامی؛ یعنی جنگی که قرار بود با «یک حمله» شروع و تمام شود، سه سال بعد هنوز کلی حساب باز و بسته‌نشده پشت سر خودش گذاشته.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72893" target="_blank">📅 15:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72892">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR2jb0RuNOjz1-_ZYXBl6sZKOFCTzDi8QMjUhauOGZFkUwJ7mZdT8lY7ZuykMmT-ThCl1qsiHG_rqSjVYX2eS5-ULYdSiqfZdpvqC3vC5v9s562P43WuJUiP3kSNI_sijWDqLx5ydYVRXBajNWU5WiQSO8TZFOvmflXfliwce0cPl9jFNM_5ndKee0BAtlhvKkiBP6YWmENELrZMdnc1hqwk-nS_udw1qUkc_4La4vM5iij-XTztRtfAL7tCtRdHLcOAf0g5IQHGVYjEeoQID_DYKekpIyevsI78235XEpRDG-w06JdqD-Hn3AP0kQ-YI-I-fo8FEt0sMrygx_7-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه‌های برتری که مدرسه فرهنگ (وابسته به حدادعادل) تو کنکور امسال داده :
زرین، پسرِ بادیگاردِ علی خامنه‌ای : 16 انسانی
محمدباقر، پسرِ مجتبی خامنه‌ای : 106 انسانی
محمد‌امین، پسرِ بذرپاش (وزیر راه سابق) : 173 انسانی
محمد، نوه حداد عادل : 910 انسانی
محمد، نوه محسن رضایی : 1700 انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72892" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72891">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=aasnGNbaRotuOW44E2To3YAUFx_vH_L2HvCKsM4gD-cAlQ4KAgauzIdlol10AL8u3IefgeCEKe4ANqZVINpXtXU6XHhObGuH4i4BTofgMvca1O30PXHvM3rd8VUZYBzb4gZxOUyqglNERvuBaNufzGHHHz3OkIU-QGk6-NX5wy8OcyNvom6KwAFagT5BpozuDzFwU727j_au6TJBpDykK8mm_RXSnrZ618jbP9_5uBzQSXjBOjs4x7vGk75-xm7wh5zcPfPOLTosBw-_ExXexee3oAG14AQBvvBvIh8LymmtmvVXkDG1r5xN5utH1eoNTS9AU7U4LguFU44c9ecn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=aasnGNbaRotuOW44E2To3YAUFx_vH_L2HvCKsM4gD-cAlQ4KAgauzIdlol10AL8u3IefgeCEKe4ANqZVINpXtXU6XHhObGuH4i4BTofgMvca1O30PXHvM3rd8VUZYBzb4gZxOUyqglNERvuBaNufzGHHHz3OkIU-QGk6-NX5wy8OcyNvom6KwAFagT5BpozuDzFwU727j_au6TJBpDykK8mm_RXSnrZ618jbP9_5uBzQSXjBOjs4x7vGk75-xm7wh5zcPfPOLTosBw-_ExXexee3oAG14AQBvvBvIh8LymmtmvVXkDG1r5xN5utH1eoNTS9AU7U4LguFU44c9ecn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوچک زاده نماینده مجلس:
به یوسف پزشکیان بگید یه بچه دبستانی از پدر تو بیشتر میفهمه!
حرفایی که تو میزنی باید امریکا بزنه نه پسر رئیس جمهور ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72891" target="_blank">📅 14:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72890">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=HLkdJtZqdfNapA6vRXoXXk18Mcw1ua3VgJHjL0pBoGU_OoTDBkakh_hS1MJpN6eSi5p6Ppjo2-qYr_YJUZnRUQ8CxwHpT9GZvQCY3hVVWdisSg-fTAYm2e3X3aw8IowAoMqg3N_NfiPkGGjuipzs4lhyPdinZr8YCXsGQ_KdVUP54rX7Zzwa3CIcZD475N3Im_6EfeUL_rjytjmw3EJNojrGyR9aFaE3WLUhTdrjEh6T12giN6gAUfF36s5PxprU2glH3KpIob2iASklTonG8Ii--g-h-tym1WYTNu3HhqVKzDx-WZdSAiZCqs5FO_XrZEwZlUjWmELff6Sliy_SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=HLkdJtZqdfNapA6vRXoXXk18Mcw1ua3VgJHjL0pBoGU_OoTDBkakh_hS1MJpN6eSi5p6Ppjo2-qYr_YJUZnRUQ8CxwHpT9GZvQCY3hVVWdisSg-fTAYm2e3X3aw8IowAoMqg3N_NfiPkGGjuipzs4lhyPdinZr8YCXsGQ_KdVUP54rX7Zzwa3CIcZD475N3Im_6EfeUL_rjytjmw3EJNojrGyR9aFaE3WLUhTdrjEh6T12giN6gAUfF36s5PxprU2glH3KpIob2iASklTonG8Ii--g-h-tym1WYTNu3HhqVKzDx-WZdSAiZCqs5FO_XrZEwZlUjWmELff6Sliy_SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو درباره ایران:
«کشورهایی که حتی به ما حمله می‌کنن، یواشکی و در خفا می‌گن: اینا باید سقوط کنن؛ دارن همه‌مون رو خفه می‌کنن.
ما مطمئن می‌شیم که سقوط کنن. سقوط می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72890" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72889">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=phHyGLfo7boLqpEnbRwGSOMEWyh3F8lpSrw0o18lYuzh3x9tAoj7N7y3jBsoRdS4ztj17C8miMIBOLNOXwEJ4W3LK_eLR4epIKgAeF91ljtBa_mNantSWo0hMGKLc0HYGRCWorYE8SUxy6-EvlvHRY97gc7VzWP0Ekw0Unw0A9s19eBBwUInKBBVWUnNigcly3mBa18xCwKjIk-fPFYH19Hg4JwdRec5SYlwVQCPK89ypdjZJXh-8xDgDjPaFQfnT8FeGW8SSiNxE0gauraQWVESoOlR5LChEgtedTSmKHIT7q9mpSBbIDRb1rIoxILTLk4ZB6ZRFlJZAnxx7AaxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=phHyGLfo7boLqpEnbRwGSOMEWyh3F8lpSrw0o18lYuzh3x9tAoj7N7y3jBsoRdS4ztj17C8miMIBOLNOXwEJ4W3LK_eLR4epIKgAeF91ljtBa_mNantSWo0hMGKLc0HYGRCWorYE8SUxy6-EvlvHRY97gc7VzWP0Ekw0Unw0A9s19eBBwUInKBBVWUnNigcly3mBa18xCwKjIk-fPFYH19Hg4JwdRec5SYlwVQCPK89ypdjZJXh-8xDgDjPaFQfnT8FeGW8SSiNxE0gauraQWVESoOlR5LChEgtedTSmKHIT7q9mpSBbIDRb1rIoxILTLk4ZB6ZRFlJZAnxx7AaxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هر دلار و هر سنتی که این حکومت به دست میاره، خرج جاده و پل یا بهتر کردن زندگی مردم ایران نمی‌کنه.
این پول رو خرج حزب‌الله و حماس و شبه‌نظامی‌هایی می‌کنن که از داخل عراق موشک شلیک می‌کنن، و همین‌طور حوثی‌ها.
باید پولشون رو برای مردم خودشون خرج می‌کردن، اما به‌جاش پول رو صرف تروریسم و تسلیحات می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72889" target="_blank">📅 13:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72888">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=QHlUPIci89FlXS9P4xcSa75ZMoG7MVuHiutsZvtMSa1dM8o88_17ohHKRNWoJCYqTDZ58mQI1jGH_QQqoDTPJB9-0hX5SJklyW5mf3Z8hdCusUQ1QmU4EJ65mJqubAgY-pFqAZil7gjkvlqhRA3_icV841kaIc7KiaHHACCikOpgU6Zzj6Oqx-ZEbYCkyd74n7PmEQ09n5jDGTQFNkq0ivO_GI8BlJMY6lo7efN3pkVWACNtXV4efYVtqaNnRCmhMFx4OuTkzJnZ0JlE95hp597CnLUoCVSkzHeYPKDD40I1i3uzOwfoMZEU7jnNF3xurFfZqCfUgJJuILIdWByZmzX4Qi9qB90QWFyzU_xviOKWGegqS9kTxIyfPFuEmDrtEHJOCnCuvi3YM2vCDjlC4QexBRGGSkZN43P0uEJWeAwniyY0Pp2L6U7bbnmiYoMguN9AfjT50ZUaXtPJV9LCBFdJhT0SZ174_0VItm_J-C4fkDNr5ZpwzzuY9CupIi463TSk1CUYZMKctMl8yDHeouv1HwYmkheqcl_fheuhGIkUGwlI0uFh-idSPSbfJ-w-V32JRCo9u-Foin650G7Ody-UCv_TYktmekZ6hofBOPOtjOpns2AehhUzBpoc3K0NriG-HXLb-fpZws25ajWRA0REP83u2aPlWavMDpjYc7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=QHlUPIci89FlXS9P4xcSa75ZMoG7MVuHiutsZvtMSa1dM8o88_17ohHKRNWoJCYqTDZ58mQI1jGH_QQqoDTPJB9-0hX5SJklyW5mf3Z8hdCusUQ1QmU4EJ65mJqubAgY-pFqAZil7gjkvlqhRA3_icV841kaIc7KiaHHACCikOpgU6Zzj6Oqx-ZEbYCkyd74n7PmEQ09n5jDGTQFNkq0ivO_GI8BlJMY6lo7efN3pkVWACNtXV4efYVtqaNnRCmhMFx4OuTkzJnZ0JlE95hp597CnLUoCVSkzHeYPKDD40I1i3uzOwfoMZEU7jnNF3xurFfZqCfUgJJuILIdWByZmzX4Qi9qB90QWFyzU_xviOKWGegqS9kTxIyfPFuEmDrtEHJOCnCuvi3YM2vCDjlC4QexBRGGSkZN43P0uEJWeAwniyY0Pp2L6U7bbnmiYoMguN9AfjT50ZUaXtPJV9LCBFdJhT0SZ174_0VItm_J-C4fkDNr5ZpwzzuY9CupIi463TSk1CUYZMKctMl8yDHeouv1HwYmkheqcl_fheuhGIkUGwlI0uFh-idSPSbfJ-w-V32JRCo9u-Foin650G7Ody-UCv_TYktmekZ6hofBOPOtjOpns2AehhUzBpoc3K0NriG-HXLb-fpZws25ajWRA0REP83u2aPlWavMDpjYc7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
«اقتصاد ایران داره به نقطه‌ای می‌رسه که از نظر شدت وخامت، فقط تعداد کمی از کشورهای دنیا چنین وضعیتی رو تجربه کردن.
و تمام این وضعیت تقصیر روحانیون شیعه افراطی‌ایه که توی اون کشور تصمیم‌گیری می‌کنن.
همین‌ها هستن که مردم بیچاره ایران رو به این شرایطی که الان توش قرار دارن، رسوندن.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72888" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGLcb464ywRpQ0kW5v8hsDBeFNVIhKhRHRGPgApLW3X2cNy2fKY9BGfjKjYZXyfI3fCVILVOLhrhXJF4PdVeYkCL-AplaGwdXOFdUvx-J5KEczu_nTAf992H2xITq5x5-Xr-HswcyflH4wyn42fhuFalA4vG0PtLusuRpwU1FuH5UpFV9YQPyguCkLkKQLpy3H898-GzKtTihLldIu8Fc8714Qo4lJxSi6uns22NTnmW9vbIm0WakcIw1QkCU-c61rnADhFjxBAb-Bqq_oGE1CpKwnewST2tBRO9C8Ph3m22Mh11rGDfpKMbwYNJHUS3HkhKsoaoY4XEA9LPkaBRhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، به رویترز گفته آمریکا هنوز دقیقاً نمی‌دونه بعد از کشته‌شدن علی خامنه‌ای، چه کسی در نهایت تصمیم‌های اصلی ایران رو می‌گیره.
ونس گفته آمریکا در حال مذاکره با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه است، اما مشخص نیست این دو نفر در ساختار فعلی قدرت ایران چقدر اختیار و قدرت تصمیم‌گیری دارند.
او گفته یکی از چیزهایی که آمریکا متوجه شده اینه که «کاملاً مشخص نیست ایران چطور تصمیم‌گیری می‌کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72887" target="_blank">📅 12:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPTszGaq7T4Yts_QniOHvnxrKIAej2Oj7-SS3e7M4lQnAq7JwTZS5VLHJHKaVO7RnuvPNXYWZaA_MNvvJBOEkMg8430fvZOXfSh6Hm2MlSpn2wnY7vfk-U7l6HaqSiJn56ML2YHtnzLBPn0f6yWmG_tYYHAJAIsZZdWQARINosld7h2R4c4b8dDI8MK0lF_m-AuKLHE92vHxFmEKQSYuJt57RTs87J9nGtoEyED72Tft8yZIeQk7nJy4Oaxn6ffZtesMdsj32dk7dr-vPr10PPWdYlR8K3_2INuZtpAU0Fd7TGZU92eMoYftP03Y96Ha_m4vyQ2TkYeNu0AgTNHMGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، معاون ترامپ، به رویترز گفته اگه ایران بخواد به توافق برسه و جنگ ۷ ماهه با آمریکا تموم بشه، باید ظرفیت غنی‌سازی اورانیومش رو به‌طور قابل‌توجهی کاهش بده.
ونس گفته آمریکا دیگه به وعده و قول برای محدودیت‌های آینده اکتفا نمی‌کنه و باید اقدام واقعی و قابل لمس از طرف ایران ببینه.
اون همچنین پرسیده: اگه ایران واقعاً دنبال ساخت سلاح هسته‌ای نیست، پس چرا باید اورانیوم ۶۰ درصد غنی‌شده داشته باشه؟
با این حال، ونس گفته آمریکا همچنان برای توافق آمادگی داره، اما امتیاز هسته‌ای واقعی از ایران می‌خواد و تأکید کرده: «قرار نیست حرف رو با عمل عوض کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72886" target="_blank">📅 11:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72885">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=TJHEpADlCMe5Gh6ahuAGshAw_d7RDn2koglXQEhqIw9YbjYZjzkUtrVqO4LQcrXnRS43T2GrU4YvNf2uvUrttxFZR446SOBi7fcBt1PPGJs-Oq9wG6pUFs-TWHQdXte3lno4JYQNXOnAr6hNs73SAT4QPYOayxv90P4c0gGPmHLEsjnR_A1xpAOuI4jL6D0MT-xktyg0RMeMHXztXGIYt96iJbQaLRuBpLfrT9Za_aKMPaToT6YJp467Z5yPZIIjWJukBtYIeMFg29fCHJoztBFTJ46jaIPEjxOgn45xRaTaOCAaOR3x8qC1mpO5gMqwhdv_eyyrjHDLpUNGtEuT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=TJHEpADlCMe5Gh6ahuAGshAw_d7RDn2koglXQEhqIw9YbjYZjzkUtrVqO4LQcrXnRS43T2GrU4YvNf2uvUrttxFZR446SOBi7fcBt1PPGJs-Oq9wG6pUFs-TWHQdXte3lno4JYQNXOnAr6hNs73SAT4QPYOayxv90P4c0gGPmHLEsjnR_A1xpAOuI4jL6D0MT-xktyg0RMeMHXztXGIYt96iJbQaLRuBpLfrT9Za_aKMPaToT6YJp467Z5yPZIIjWJukBtYIeMFg29fCHJoztBFTJ46jaIPEjxOgn45xRaTaOCAaOR3x8qC1mpO5gMqwhdv_eyyrjHDLpUNGtEuT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72885" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72884">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94194705f4.mp4?token=pT3DAyoE8UCMfYAMDzFkJ3O_4Zq00_sR6h6REEihCS2u_l-LcOFIds47fl9e1sDHdbeBzZcJuYcaTBRAtUu2Y3AGRfdQtQvUEVd9UjS2uRM6i-F_WejMhFJj_bQqc0EEB7U0R9HT4nKCyrU8wnOSKdLovcuM_9DdD1BSAMG_jFfliBKMWDYtIFny4H-AmQ0dpBzV1NvCd85YIvfRsZmy5gGxbXxJvIRPjKUTnnh3ZAZjoKIoRixdjN4ASZ15_55q50SlY4Liq0wxVpnrQylEyGshK2T2tp2fMtLrE9q9dEhoPsaP6sWoj8PqmfJF7bMeoQnWGwFZTGzspn7ZPugc2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94194705f4.mp4?token=pT3DAyoE8UCMfYAMDzFkJ3O_4Zq00_sR6h6REEihCS2u_l-LcOFIds47fl9e1sDHdbeBzZcJuYcaTBRAtUu2Y3AGRfdQtQvUEVd9UjS2uRM6i-F_WejMhFJj_bQqc0EEB7U0R9HT4nKCyrU8wnOSKdLovcuM_9DdD1BSAMG_jFfliBKMWDYtIFny4H-AmQ0dpBzV1NvCd85YIvfRsZmy5gGxbXxJvIRPjKUTnnh3ZAZjoKIoRixdjN4ASZ15_55q50SlY4Liq0wxVpnrQylEyGshK2T2tp2fMtLrE9q9dEhoPsaP6sWoj8PqmfJF7bMeoQnWGwFZTGzspn7ZPugc2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم زیبای و ویژه برای وداع با مسی با نمایش پهبادی در آسمان!
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72884" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72883">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72883" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdidU8RdJxpe8ePdxbY-Hm7f2UDMjU1O54GqmJqYom01tLZbLMFiOOVoHC0QbKfThD99iGLeYmPLJfmx1_XQtKFH8OjuGA-vetoK_qles8jSmeEJrRPK7UVkpyPvHiu3KLI9Q-Kzyf1mGdaiSHd3Zr4jt3xMggYV-0gUVibGwHnSk7wj4M1tp_JPZEHRnGKcxCXmIwSuMBNQdOvii51nUV-n9IVKLpYVMl9ovhS0JZa84tPZ40HtmrHGX4IgOfxpUsLMgiTNtp5-lQaOV8hMBOPJOTX5oWTjSdrBQzfTcMJv-QRNvrUcD6g2YoU5hySPs5wEgRWmNQH__P-sh5uxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72882" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72878">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=pUxSx0esFbjIOQtirTO3cywl8pRmDbpx4qnj6PTZF4GqV48cLY_aShP2GbXJUMQUfk_FYVwoZy2x1Uik1UDf7035F4GFdFjHjOhhfrqEw9hKGpfgDPuuf_vrDdVSFfmVywrNu2Z5NqAkShxNJznLCQVIwl8KttdENnMbDIK6dmO6bE3y_WycULnVF0jrAwzmjyoYzu3liA99K62zK0pAuq_oXvDU8QN5ln3UzS1Csm3EtPB_u_s6P0iz_CEgTM5b2ViEocUE631Ewt-mQes1NbZQ4sO-rZw2rDCEaSU_h039ut-z6dMzkj9EKK3ZgWMQ06g9KKcj-MH29-R0XF33MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=pUxSx0esFbjIOQtirTO3cywl8pRmDbpx4qnj6PTZF4GqV48cLY_aShP2GbXJUMQUfk_FYVwoZy2x1Uik1UDf7035F4GFdFjHjOhhfrqEw9hKGpfgDPuuf_vrDdVSFfmVywrNu2Z5NqAkShxNJznLCQVIwl8KttdENnMbDIK6dmO6bE3y_WycULnVF0jrAwzmjyoYzu3liA99K62zK0pAuq_oXvDU8QN5ln3UzS1Csm3EtPB_u_s6P0iz_CEgTM5b2ViEocUE631Ewt-mQes1NbZQ4sO-rZw2rDCEaSU_h039ut-z6dMzkj9EKK3ZgWMQ06g9KKcj-MH29-R0XF33MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسیدیم به اون لحظه‌ای که عاشقان فوتبال تحمل دیدنشو ندارن...
لیونل مسی، اسطوره ۳۹ ساله فوتبال، سه‌شنبه ۶ اکتبر ۲۰۲۶ برای آخرین بار پیراهن آرژانتین رو پوشید؛ این بار در ورزشگاه مومنتال بوئنوس‌آیرس و مقابل بنین.
مسی بعد از سال‌ها افتخار، جام‌ها، اشک‌ها و لحظه‌هایی که برای آرژانتین ساخت، جلوی چشم هوادارانی که برای خداحافظی باهاش ورزشگاه رو پر کرده بودن، رسماً از تیم ملی خداحافظی کرد.
از این به بعد دیگه مسی رو با پیراهن آرژانتین نمی‌بینیم؛ پرونده یکی از باشکوه‌ترین دوران‌های ملی تاریخ فوتبال هم اینجا بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72878" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72875">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=B7eqWB2NhZRsBjhEG8ltoO7U5KqVH6MvSpz5V_fiMaw8ePmAM3bzRc7RVgtZu8-52cobMjAC_PaWQgRyPOBc4SEcpIjjTOIcE5WT642d_Z4V_YgNxO8ag8q-S6b4SP8_4-oxHtGGze3Rtq5anmWIPOG98xswaby9gHbAiJO06wpZPabH-glpsV_MbQiTxFTLcIXihddibfKrBr3bibad4Dvb2RH8QDNbSApbL7ycXZjyh7McEhC7zvYs2kgRLc3KfIZur2s_Ugn-QebRtT7YXVs9MVoHRbBnzWo5geezJut1sOmS05Edti5W7fJnGhrQULKhxw8mCw8JK__eDwx9FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=B7eqWB2NhZRsBjhEG8ltoO7U5KqVH6MvSpz5V_fiMaw8ePmAM3bzRc7RVgtZu8-52cobMjAC_PaWQgRyPOBc4SEcpIjjTOIcE5WT642d_Z4V_YgNxO8ag8q-S6b4SP8_4-oxHtGGze3Rtq5anmWIPOG98xswaby9gHbAiJO06wpZPabH-glpsV_MbQiTxFTLcIXihddibfKrBr3bibad4Dvb2RH8QDNbSApbL7ycXZjyh7McEhC7zvYs2kgRLc3KfIZur2s_Ugn-QebRtT7YXVs9MVoHRbBnzWo5geezJut1sOmS05Edti5W7fJnGhrQULKhxw8mCw8JK__eDwx9FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ایتا و روبیکا تصاویری از یه سلاح ایرانی تو مرز ایران و عراق منتشر کردن که حتی خودشونم نمیدونن دقیقاً چیه :
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72875" target="_blank">📅 10:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72874">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=g1Uyy9w6zra8uwdOG5fjYVhdWmtGhDQzW0Sco1fsBQhYcPwNVCwLihPzoV7BVILNkKo670qufAwJQWdaUi8rLNFYaZV4E3kZIOUgZNPOtx0XrzMWmpJIt222oXASqv4K8rVNw_Ak1onDBVZXh0Wjr0koJ4njFvK5Ef7-LP8iN9NLrxrdjrPuiHvxWWLs-5OAskejkS5qgt5NyXXGvUWCtpAgS9vHhLP9dcvWr2FkhNESS0MQQRDPrdnYU4PNmQjwPO5X-NYcPaFIQYkPyO9csh-tThnWo5cp98gyQEKmQLiQjS0mSR2ccP2pVsQZCYhUXOjV7td9KUGkTK-Ngwscmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=g1Uyy9w6zra8uwdOG5fjYVhdWmtGhDQzW0Sco1fsBQhYcPwNVCwLihPzoV7BVILNkKo670qufAwJQWdaUi8rLNFYaZV4E3kZIOUgZNPOtx0XrzMWmpJIt222oXASqv4K8rVNw_Ak1onDBVZXh0Wjr0koJ4njFvK5Ef7-LP8iN9NLrxrdjrPuiHvxWWLs-5OAskejkS5qgt5NyXXGvUWCtpAgS9vHhLP9dcvWr2FkhNESS0MQQRDPrdnYU4PNmQjwPO5X-NYcPaFIQYkPyO9csh-tThnWo5cp98gyQEKmQLiQjS0mSR2ccP2pVsQZCYhUXOjV7td9KUGkTK-Ngwscmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72874" target="_blank">📅 10:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72873">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=KmihdcQ0zY89gzzXigpeeNlD5ZwVoFN-3D8w8iHcLaPHcYmRwokdrQYYxhuOkKqBPu19RxvIczrMNtKV1FyANzwLr4prIv2qdimwRc4Onw9YLfHpuNZSvAz66Ia-Q33bFnRH5ad5lX4E794di5uYYoKyqvjR4dQlqoy-KUYlEZYNVqBTtbfGIOXLR_u7MHoLg9qkWN6U4kclLoJWEhp9F_zFVyRrQ8gRG5cZ_X8_UvQ8Mj-caPK7zsa8FeCV_GlbY7El6yOlNge0_rGPQIoPeb-73wKcmQ_tXP3RZTR6Re4pDSO1Gplb5HE1TxnCXAxckAOjo20wjynO_bIIgNQv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=KmihdcQ0zY89gzzXigpeeNlD5ZwVoFN-3D8w8iHcLaPHcYmRwokdrQYYxhuOkKqBPu19RxvIczrMNtKV1FyANzwLr4prIv2qdimwRc4Onw9YLfHpuNZSvAz66Ia-Q33bFnRH5ad5lX4E794di5uYYoKyqvjR4dQlqoy-KUYlEZYNVqBTtbfGIOXLR_u7MHoLg9qkWN6U4kclLoJWEhp9F_zFVyRrQ8gRG5cZ_X8_UvQ8Mj-caPK7zsa8FeCV_GlbY7El6yOlNge0_rGPQIoPeb-73wKcmQ_tXP3RZTR6Re4pDSO1Gplb5HE1TxnCXAxckAOjo20wjynO_bIIgNQv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شک این یکی از عجیب‌ترین پرونده های فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72873" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72872">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=riWx5dYOqO7ffAuvGFkfOH1ZCSmBq3F-NdgdwvACeN8hFi1bb6r5S_PczM3nPBay2b9dMxL_r4pZB6YBeSz_nXy4mw5t3uftI7hBBqeTtKWt7UrTQM8prinC5FfpIxpH3Spghmlpfkk2STZR4stHkw27O_YQtB1JPKZrUIJj9fJv-S9S3XS3XyM1cnl9qcXRbduePCt2Uxm3Jpqe8BSMTxm4VPdZ6ilnstMuwptHcdnGwnyq5ruEhmEI7a9tsm2bFo6akv6NyQglP3eEAjnaCkWjx_H1U7Lg2I8ElSpq7di0jctrG7BNGY9IRm_3ojw5ZGheCOEc3e4UbvfiTxFWpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=riWx5dYOqO7ffAuvGFkfOH1ZCSmBq3F-NdgdwvACeN8hFi1bb6r5S_PczM3nPBay2b9dMxL_r4pZB6YBeSz_nXy4mw5t3uftI7hBBqeTtKWt7UrTQM8prinC5FfpIxpH3Spghmlpfkk2STZR4stHkw27O_YQtB1JPKZrUIJj9fJv-S9S3XS3XyM1cnl9qcXRbduePCt2Uxm3Jpqe8BSMTxm4VPdZ6ilnstMuwptHcdnGwnyq5ruEhmEI7a9tsm2bFo6akv6NyQglP3eEAjnaCkWjx_H1U7Lg2I8ElSpq7di0jctrG7BNGY9IRm_3ojw5ZGheCOEc3e4UbvfiTxFWpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
حداقل شش ماه اول امسال، عمده کارهایی که کردیم این بود که دو تا موضوع مهم رو به نتیجه برسونیم؛
یکی کنترل تورم، چون به‌خاطر رشد نقدینگی و فشارهای ناشی از دو جنگ پشت سر هم، نقدینگی شتاب بیشتری گرفته بود.
دوم هم اینکه توی این شرایط بتونیم کالاهای اساسی، دارو، معیشت مردم و مواد اولیه کارخونه‌ها رو تأمین کنیم.
این دوتا استراتژی اصلی بانک مرکزی بوده و خوشبختانه بخشی از اقداماتمون هم به نتیجه رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72872" target="_blank">📅 09:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72871">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را #رایگان کردیم برای 100 نفر اول
👇
꧁༒VIP CHANEL  GOLD༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72871" target="_blank">📅 01:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را
#رایگان
کردیم برای 100 نفر اول
👇
꧁༒
VIP CHANEL  GOLD
༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید
لطفا رعایت کنید تا حق خودتون ضایع نشه
🙏
چون عضویت فقط برای 100 نفر بازه
هرکس سود کرد دخترم و همسرم رو دعا کنه
❤️
🙏</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72869" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72868" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y18vNF4cd04jBs1E2QP_3Pn-bgJpEnHQDrjZ64G3LrcP_expCYAt_-DVH1ri5Wv1DNmRLWkXl8678jBzg6fNpsPLpJ608jJOL__B8h8253ziUIPq7t5kvURrjcULoryIyG9X71Bsu77RXWSe8IgMA6Jkgoiww30ygF19WJIKzxlu2GSfZhdZZkJSYXT2E_u0s223j4ar83XQBlvlraDvqSXaDVrTU85dfKG1zCeDQ_Ciexpll7pkYXsU_Nu9Af5uuQTJy1acEYDLlwhYJ6ddduLqwT38GmSWTRlSoa6vf1lOUkZE1bAp_uQsuoIBM_xsiMiu_tdYQj7nsqZWdz2e2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72867" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koj7pgyb2gYugguRfMiAfm25Jp8L05RfaZYyQRrXmwQZC-emZ3DvJr-eOw654OJfUm4CQKeg6g38nDz3uRslk6d7zduC5HHPy76TIWbsIKBrAE0fBSQx4r2cvxzaT4COYaOoLzYTaxPIElJQ_aLK2Kyjmn9oOULBpNxo-lK76GP8n6d1W-5kmSLUWOg_5FIZRDDKiGJP3dZugXmdO62P2AmrQGAISMCedERvzeKEvx8e9cQqyZNQImdbmuNy6GOP1OEdfLs8-XUU0LWILg2AOYyr_gWAH_myyp_iymgczC7N1QAgZGKaCcwqgyEC0huGr5FdWujOjiXDulZWnIhTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا:
«ایران یه وزیر نفت جدید داره.
با توجه به اینکه ایران از ۲۵ اوت حتی یه بشکه نفت خام هم روی هیچ کشتی‌ای بارگیری نکرده، این وزیر نفت دقیقاً قراره چی رو مدیریت کنه؟»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72866" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=lB6P4LFvhYbP4EH6rmYlUxAbRAxlpyBb5inb98HdREMCsstjUVfNpCxwr5b3RYcyk0RW-RiPk7AnQ1nJOjWBOZweslM4M0jjq8KC7EdS2ipX5jTeAEVdEttmMgiplcjy9E1QTpjguRXtNJhBnPU4szhiM0pkS2R5imgFiwVKOb3RIUKWTZhx0VNuiSa_KxKQ4z0ALPvfFfpdTy4GopcCVPGzbSD1D2HPxOyhJSc1Oas5WYwWQhOEyZ7vMr0eCKhumVC5To2mqBIvmb3sBYvew49Hj6zZKi9lCi56zuzUrDOOE-VjSdptcSafpyf2ley9FaE3xNrXvzTZtY6dyrLEEzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=lB6P4LFvhYbP4EH6rmYlUxAbRAxlpyBb5inb98HdREMCsstjUVfNpCxwr5b3RYcyk0RW-RiPk7AnQ1nJOjWBOZweslM4M0jjq8KC7EdS2ipX5jTeAEVdEttmMgiplcjy9E1QTpjguRXtNJhBnPU4szhiM0pkS2R5imgFiwVKOb3RIUKWTZhx0VNuiSa_KxKQ4z0ALPvfFfpdTy4GopcCVPGzbSD1D2HPxOyhJSc1Oas5WYwWQhOEyZ7vMr0eCKhumVC5To2mqBIvmb3sBYvew49Hj6zZKi9lCi56zuzUrDOOE-VjSdptcSafpyf2ley9FaE3xNrXvzTZtY6dyrLEEzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره طاعون در روسیه، با پوتین صحبت کردید؟
ترامپ: «به‌زودی یه تماس باهاش دارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72865" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=N3xj-nv19jf_r1Az8oz0GuJAf5f2Mji4Y7qQAngKGzPu299EIpRtz2SE2WcEuxl1KmW1-P0w545QVUH5AqQuJKhLfdj2nc5Cy2udEnoNum69be_-Me53FX8B3TXesOO16_KGK7-6GZVA7foDkV9e6OawMr8XbdSdLIYvDGg1DY1YNqqEfNowUnI59iV57Iwg-h-smyXmanfHJNU_mwvXE3RvGS7MZut7IY97VI6hoIrKQDvsmU-2e60a4RCt914CK8CpWfn-szlI5CadKdm2NDNz1X_8yRM6huKU2hz4XqW8zPHNipeKce8X0JBvkOP0am9hrzWXE45mX6mMO5GFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=N3xj-nv19jf_r1Az8oz0GuJAf5f2Mji4Y7qQAngKGzPu299EIpRtz2SE2WcEuxl1KmW1-P0w545QVUH5AqQuJKhLfdj2nc5Cy2udEnoNum69be_-Me53FX8B3TXesOO16_KGK7-6GZVA7foDkV9e6OawMr8XbdSdLIYvDGg1DY1YNqqEfNowUnI59iV57Iwg-h-smyXmanfHJNU_mwvXE3RvGS7MZut7IY97VI6hoIrKQDvsmU-2e60a4RCt914CK8CpWfn-szlI5CadKdm2NDNz1X_8yRM6huKU2hz4XqW8zPHNipeKce8X0JBvkOP0am9hrzWXE45mX6mMO5GFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌گن: اوه، ما شش ماهه که درگیر ایرانیم!
ما عملاً همون لحظه‌ای که بمب‌افکن‌های B-2 حمله کردن، کار رو تموم کردیم؛ چون با اون حمله، برنامه هسته‌ای‌شون دیگه تموم شد و ۹۵ درصد دلیل این کار همین بود؛ شاید حتی ۱۰۰ درصدش.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72864" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=Oc1NkokTWh2s82YLCYOh6D8BKBWPJ9RBOSzrl62f3E6dLox6s9gOtAdDukvKDdCL1UwjrHnfDOOO6WXxMSgwejh9-0PgT8aguCOtDnn1_fxNjRko9RhJMZpEnuAmYgDWeC5gtCXdlehW0kKBrrpJrK2wknU3a31fLqyWwlDsMZnpQqRigSJLTZBFu3xTXlDieC0LQb3hloYhTXUboEwLhwbS-Khn6OQu84jUymxQZwT5k6wj85SgPnS5nuykFMYaqcqld4_dtvklIVNH8Vu7gU80X9R58ghD33fopFPB9BireQvgCCx0epeJkVeq97vewBEMLTgOsYT_eKO-piPhR72DMeVK5bbO_lWDRvCrgSBu7bMcumuNuWRavSjlTPuKMeDt7aaZTqEv5Srfak7Uf5aT8nC__ptaXMa7qU0D6zX5U8w1WkBx3e0scR_gke55KmM8JFdR123p2XsEyQOOZlrh3Y9kl4zIGdbjUSfb4wpZRaO5LMtFlLiV-tkyjJtuoOhk5Q_Q_Cc3qOU5eRaqZExrHGqtgIPJmC3XhjCUF7VlBGapYPfkJRdhUwDj8XtSICTvW_hysjwjr3KOCWbJvth4t1tpXJe-XZfuLayp4w-cLWsk4G9syystBdfFLLseMWORkBwEXD_nCCK_MREG1qjwzytYqa69zjpUgHExvpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=Oc1NkokTWh2s82YLCYOh6D8BKBWPJ9RBOSzrl62f3E6dLox6s9gOtAdDukvKDdCL1UwjrHnfDOOO6WXxMSgwejh9-0PgT8aguCOtDnn1_fxNjRko9RhJMZpEnuAmYgDWeC5gtCXdlehW0kKBrrpJrK2wknU3a31fLqyWwlDsMZnpQqRigSJLTZBFu3xTXlDieC0LQb3hloYhTXUboEwLhwbS-Khn6OQu84jUymxQZwT5k6wj85SgPnS5nuykFMYaqcqld4_dtvklIVNH8Vu7gU80X9R58ghD33fopFPB9BireQvgCCx0epeJkVeq97vewBEMLTgOsYT_eKO-piPhR72DMeVK5bbO_lWDRvCrgSBu7bMcumuNuWRavSjlTPuKMeDt7aaZTqEv5Srfak7Uf5aT8nC__ptaXMa7qU0D6zX5U8w1WkBx3e0scR_gke55KmM8JFdR123p2XsEyQOOZlrh3Y9kl4zIGdbjUSfb4wpZRaO5LMtFlLiV-tkyjJtuoOhk5Q_Q_Cc3qOU5eRaqZExrHGqtgIPJmC3XhjCUF7VlBGapYPfkJRdhUwDj8XtSICTvW_hysjwjr3KOCWbJvth4t1tpXJe-XZfuLayp4w-cLWsk4G9syystBdfFLLseMWORkBwEXD_nCCK_MREG1qjwzytYqa69zjpUgHExvpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«نیروی دریایی آمریکا یکی از مؤثرترین و نفوذناپذیرترین محاصره‌های دریایی تاریخ رو اجرا کرده. هیچ‌کس تا حالا همچین محاصره‌ای ندیده؛ حتی یه کشتی هم نمی‌تونه وارد بشه.
اگه کشتی نفت داشته باشه، به کابینش یا سکانش می‌زنیم؛ اگه هم نفت نداشته باشه، کلاً غرقش می‌کنیم.
الان محموله‌های نفتی که از خارج ایران ارسال می‌شن، تقریباً دوباره به بالاترین سطح خودشون برگشتن.
یعنی به زبان ساده، تنگه هرمز متعلق به نیروی دریایی آمریکا و ایالات متحده‌ست؛ جای واقعی تنگه هرمز هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72863" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72862">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU673yDClfMJBV5Q8OvYzFB36hwM48ZO9fpNt59PLnLsC3hCEeaiJG6hrH15KzWWVw56FXfmekX8fQ_Pmp2ojFgv_-UpjT9ey1ZL8y8hOXbeRxGkaQitF7EA7KZzEZfKM0W3KXMXGcrwwd4X-Nste4RWMjzp7xL8QWWP7XDz5kq8WckpcYTvAPe3hgWXgNUsR-vYhxOxGzRUoEZzO8T8vA9Z0sK4h_MFwlgMhKiJDKOIY25EP9PAn4TIBNfOiWPZyW6w22Hwt-6W4sKT0d_v8Pozkx1Q5SUtpPjxfVnXrCc7XdEpo0uvwoYhL6fEa_wkyyRqN_kpfF9RXyUkLW2aIGsOGbc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU673yDClfMJBV5Q8OvYzFB36hwM48ZO9fpNt59PLnLsC3hCEeaiJG6hrH15KzWWVw56FXfmekX8fQ_Pmp2ojFgv_-UpjT9ey1ZL8y8hOXbeRxGkaQitF7EA7KZzEZfKM0W3KXMXGcrwwd4X-Nste4RWMjzp7xL8QWWP7XDz5kq8WckpcYTvAPe3hgWXgNUsR-vYhxOxGzRUoEZzO8T8vA9Z0sK4h_MFwlgMhKiJDKOIY25EP9PAn4TIBNfOiWPZyW6w22Hwt-6W4sKT0d_v8Pozkx1Q5SUtpPjxfVnXrCc7XdEpo0uvwoYhL6fEa_wkyyRqN_kpfF9RXyUkLW2aIGsOGbc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«من مدام از رهبران کشورهای مختلف دنیا تماس می‌گیرم که بابت جنگ ایران ازم تشکر می‌کنن.
منم بهشون گفتم: خب، خوبه! کی قراره پولش رو بدید؟
ما داریم بارِ کل دنیا رو روی دوشمون می‌کشیم. اتفاقاً از این کار هم خوشحالیم، چون خودمون قوی‌تر شدیم و بقیه ضعیف‌تر.
اونا دیگه ضعیف شدن؛ دیگه کارایی سابق رو ندارن. ما داریم کارهایی می‌کنیم که هیچ کشور دیگه‌ای از پسش برنمی‌اومد.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72862" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72861">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ درباره ایران:
«ایران یه کشور شکست‌خورده‌ست. همه دارن کنار می‌کشن و می‌رن. اقتصادشون هم عملاً به خاک سیاه نشسته.
وزیر نفت ایران هم گفته: «من دارم می‌رم، چون کشورمون دیگه تمومه.» خودش دقیقاً همینو گفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72861" target="_blank">📅 00:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72860">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=uU8kIlIeYJDU9bb2cb7qYX_cyI-e-3E4uz2wgMyPBU9dl42ZcyhRbqHnKGusfoZL156ZdzLjnPDeMg3Mj7Z8GDCL3_z5_QQTswuXQxv18b6laSqize2q0VcRinaAduvpPpQAx9rnOEVhMlPadmc4z5i7bxnOXAHgBq98o2JYFp1Ez4Dpqa-_p6wUr8MMi1V-rhd-C1gTfsXrY4dHQxhJ9-Xiu9VIW4bB85oi_GKwWi5-cb3GmN-UI-F5Lv2P14RtEz7DFv5VUKWBZpBvEWkdHwrv4MoHWs72Mm72ha1HzTgUT2oTNDHPy6Jo7_WcbBdq_clp9_iFwS8KHiV54dyarU8r6zSdiJlKtWtVCCDrX5fxuOwxe6a4RhmtuU4Is7NpzaitypIZMp0ZffXOsEBR2gfSxMiipPtGoXYj8o90NrV9FFa1I5CIQOOvVjgZXsKafbFzpAP4ZkPeRAUglKxmAgcAYB2dFiz3IBw9lctZCvZDqEHyNxa7bvJOHZSe3w-9F9WPvTAsLHoHzXcJP8SQ04MKT5YGuHxFl93uSgT2q46zsBagAb8LuHWWUC5ruSPS1mIF3QwucuCCv44CZp583363Eqs0fmZuX3DEKCqJ4QJZ2bvWmFKMi_HMNgvoxC9nu2C9dTCq6yW0qNebrNN6GPzrNQANs5slsMQANEaWtsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=uU8kIlIeYJDU9bb2cb7qYX_cyI-e-3E4uz2wgMyPBU9dl42ZcyhRbqHnKGusfoZL156ZdzLjnPDeMg3Mj7Z8GDCL3_z5_QQTswuXQxv18b6laSqize2q0VcRinaAduvpPpQAx9rnOEVhMlPadmc4z5i7bxnOXAHgBq98o2JYFp1Ez4Dpqa-_p6wUr8MMi1V-rhd-C1gTfsXrY4dHQxhJ9-Xiu9VIW4bB85oi_GKwWi5-cb3GmN-UI-F5Lv2P14RtEz7DFv5VUKWBZpBvEWkdHwrv4MoHWs72Mm72ha1HzTgUT2oTNDHPy6Jo7_WcbBdq_clp9_iFwS8KHiV54dyarU8r6zSdiJlKtWtVCCDrX5fxuOwxe6a4RhmtuU4Is7NpzaitypIZMp0ZffXOsEBR2gfSxMiipPtGoXYj8o90NrV9FFa1I5CIQOOvVjgZXsKafbFzpAP4ZkPeRAUglKxmAgcAYB2dFiz3IBw9lctZCvZDqEHyNxa7bvJOHZSe3w-9F9WPvTAsLHoHzXcJP8SQ04MKT5YGuHxFl93uSgT2q46zsBagAb8LuHWWUC5ruSPS1mIF3QwucuCCv44CZp583363Eqs0fmZuX3DEKCqJ4QJZ2bvWmFKMi_HMNgvoxC9nu2C9dTCq6yW0qNebrNN6GPzrNQANs5slsMQANEaWtsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
«ما توی جمهوری اسلامی ایران داریم خیلی خوب پیش می‌ریم. کل اونجا دیگه داغون شده.
باید کار رو تموم کنیم؛ فقط مونده تصمیم بگیریم چطوری تمومش کنیم: با راه خوب و دوستانه، یا یه راه نه‌چندان خوب!
خیلی زود می‌فهمید قراره کدوم راه رو انتخاب کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72860" target="_blank">📅 00:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72859">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423715c427.mp4?token=gvuEx56cQepHOEFvsMkoJbpdyL5dYaJgUcOErAMpR3REwc0kUw5PpSTQep1d8szCbOsFD0mDf2nosNPm48CZK635GquhOQdDKK0OMSaa1UXeiZZnWsJxIozRxb5DJLUcjcrtR3VjHXXY4QVd2A0NuA97JNANW-_yMuQECILQRaU4H1fYwtuuOgS09EaHrE5NmBLDOslGOBEkcABWOW1Y26QAfJHtuT6qxS09J2vZnRx8gII39owPwjPaYAm7ZNtEktLbtuFfPLR2giZjb6Pv8qH4sLgj3VLnrQ1vICuQ7I-bPCJ5kWE--YIqCXOCLfzOqwGie8Y5zj-PZaP22idkMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423715c427.mp4?token=gvuEx56cQepHOEFvsMkoJbpdyL5dYaJgUcOErAMpR3REwc0kUw5PpSTQep1d8szCbOsFD0mDf2nosNPm48CZK635GquhOQdDKK0OMSaa1UXeiZZnWsJxIozRxb5DJLUcjcrtR3VjHXXY4QVd2A0NuA97JNANW-_yMuQECILQRaU4H1fYwtuuOgS09EaHrE5NmBLDOslGOBEkcABWOW1Y26QAfJHtuT6qxS09J2vZnRx8gII39owPwjPaYAm7ZNtEktLbtuFfPLR2giZjb6Pv8qH4sLgj3VLnrQ1vICuQ7I-bPCJ5kWE--YIqCXOCLfzOqwGie8Y5zj-PZaP22idkMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«یادتونه خمینی رو؟ همه‌شون دیگه نیستن؛ همشون رفتن.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72859" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72858">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=GboM1lCSDtcjTojloI8kqsa_DXvErsBm4i9GNUIt9caPAY9R4MQdFdqmGZLAGfGJMC0q2jKIbSRUcEgm1iFUf5cxEcaGSY6fn8VagoZCNZmjB-fxXmeckQt16PKbDoL9y9AszYRW0SVYgmK6LVq8F77vVU64suhvhQf4sbkCwux92x79J52kTPPfgToVm9mBZDkRhSydHoqSjyb-ML-x3x5XlBTMiQmC7sG58qCNTUbqpAYCH79s0KkofS0nj3gT1qW7X-2BeAOODwAzJjp9J6lf34MMyRl81hx5lonRvtT3IKkuN_gbvtJL5JeC3yiNNa_Agyary1VvjqLTqGAN5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=GboM1lCSDtcjTojloI8kqsa_DXvErsBm4i9GNUIt9caPAY9R4MQdFdqmGZLAGfGJMC0q2jKIbSRUcEgm1iFUf5cxEcaGSY6fn8VagoZCNZmjB-fxXmeckQt16PKbDoL9y9AszYRW0SVYgmK6LVq8F77vVU64suhvhQf4sbkCwux92x79J52kTPPfgToVm9mBZDkRhSydHoqSjyb-ML-x3x5XlBTMiQmC7sG58qCNTUbqpAYCH79s0KkofS0nj3gT1qW7X-2BeAOODwAzJjp9J6lf34MMyRl81hx5lonRvtT3IKkuN_gbvtJL5JeC3yiNNa_Agyary1VvjqLTqGAN5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:
«ده‌ها نفر از سران تروریستی ایران رو از هستی ساقط کردن و مستقیم فرستادن اون‌ور، پشت دروازه‌های جهنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72858" target="_blank">📅 00:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72857">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=MOhKu4O65USm_mWsa6_8GJNCErgE_e2LjD9hFORmwYeMc03QWlEC_Zq52zPIMM6gvIDuP6_bP6T_cKydMSx8sdzycbG-PuPZdZE2wTEP4gd8TiTEKwpVcHvNcdEgvy4e8CnpCZNAK9Ew4G0Vnrs1NZBlx3lhWmhMpneqJSfZne5IULOBbQ4A-DL_cvY6helpOtR6Ruq40Wv8hM46ERL8S_JJmmgWuL_H1nzFrnPu9597V-InkqEsaXMuBaQ7DBe6Gf-VZYgq58MHpcjhN21F76uzAPT9tTo9EBjvYBDqZTVGxH91y3VDx27t0wfaOOLalMbf1PM_9I5rsSw4lxjSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=MOhKu4O65USm_mWsa6_8GJNCErgE_e2LjD9hFORmwYeMc03QWlEC_Zq52zPIMM6gvIDuP6_bP6T_cKydMSx8sdzycbG-PuPZdZE2wTEP4gd8TiTEKwpVcHvNcdEgvy4e8CnpCZNAK9Ew4G0Vnrs1NZBlx3lhWmhMpneqJSfZne5IULOBbQ4A-DL_cvY6helpOtR6Ruq40Wv8hM46ERL8S_JJmmgWuL_H1nzFrnPu9597V-InkqEsaXMuBaQ7DBe6Gf-VZYgq58MHpcjhN21F76uzAPT9tTo9EBjvYBDqZTVGxH91y3VDx27t0wfaOOLalMbf1PM_9I5rsSw4lxjSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.  @News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72857" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72852">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/news_hut/72852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72852" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72848">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uM4PePzMF9hJKj74o30uqACS-EjP-DXeMjRTKVdEyHOsW52VlxoJQBkz3dsBArWw1FUtDjLEzD6p4IH5XhYGB4csYjqZif_XRx2IDi7-TlbwxA5jdryuARST-L_6N1vV_M3NfySAjBoB904IcH33ytQankWJxayZPvjS1Y5uYLPhPeSoMTftXb1agGWAtqe6YQSn7upMghZu4RpOFswIK-PZ_U4y5lPSGOAs3dEVMBC7TzwSu9TOYWbq3KMNeczf4fVqbLhmWmtS5_u2HZFaqtpmXak1WLb5tvdk0nULziXW3o5DDFfpoOJ39NT2TA009yQWXDghhIYibRU2zowoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OSn3vI5idKAisSxDiC1SS4rsY81rcT7uDHP2ypSQPZ_azCrTFAG9wweJGOdQgJUXHjReDUbguGV0r9dzR_HKA2BF7h8lNMhusyCy6ce4I--y57ZQcHtjA6SEpc0y78VVkg__FMexO_scC8_T4GH0b1awgv84n3IQ_FdrRAalBWqGMfWi3ceHnb6CKO9G_v3EiLORxgqFOr7SGOPOeRxjt1U3ZpCp5kDtvx_Z4bSaEhwxANLxpmLx2OSqaODGuRe16wXF4w5nFI2Hme6e5wdDwJskf_rEpmPLRoUkeIR9Bdlk5ncp-pBbJyiPA9r3YuBAP1ASS4zHQFqhAu6a-dWNpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=LF1Er7taii48527pUjg-PKYMli7G6c3bzlE70ArD6GBBAOv1wl406Z-4A77q_43DdUDeAMz1THzLKelL5wkjfzvunLAOobCJ5QvBGgc1phkZvtDFu6We-qyliE8KxsCmZFsWCvyR_YeiM1l-GfBQlEsiVTYHj1L7bQjGA_eGMXp4tfIcUMGctPqjUuXUtaK3cR64gyTejYDypE42kUlR6DumwXJTrQg5Da9lLoriZznIZcKhJ6JyFy9S53i7S03kSkKsnqtaOcdFmHKgK7DrjhNlw6rxWrO9J7nF9cKgl1HKruoUWDLc2CZyrVH8i1qFDZLtOAJuC2EzNiJLOS-Jng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=LF1Er7taii48527pUjg-PKYMli7G6c3bzlE70ArD6GBBAOv1wl406Z-4A77q_43DdUDeAMz1THzLKelL5wkjfzvunLAOobCJ5QvBGgc1phkZvtDFu6We-qyliE8KxsCmZFsWCvyR_YeiM1l-GfBQlEsiVTYHj1L7bQjGA_eGMXp4tfIcUMGctPqjUuXUtaK3cR64gyTejYDypE42kUlR6DumwXJTrQg5Da9lLoriZznIZcKhJ6JyFy9S53i7S03kSkKsnqtaOcdFmHKgK7DrjhNlw6rxWrO9J7nF9cKgl1HKruoUWDLc2CZyrVH8i1qFDZLtOAJuC2EzNiJLOS-Jng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا صرافی ایرانیه «omp finix» که دارای امتیاز رسمی و تایید شده هم هست، پول مردم رو بالا کشید و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده.
مردم هم مقابل قوه قضائیه دست به اعتراضات زدن و خواستار تعیین تکلیف و پرداخت پولشون شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72848" target="_blank">📅 23:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72847">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=DaczE-zgdcVGCtTyTyKWw88hl7lJE_j1CCxnCg0rJK3M68eAY9q9nEk77bDkIHzINAByJr_VoBK2HocNT5-Kz508sJXodlZYIPJEu_h3fWR_gv_aN4UcubtuoMabZKJxVccgSLc7rq61bgic8RH0TNk5xTXz-gnS5YwseorUIrM-wtm9B3kfIZRfQwh2k3ji6rob0jKBrCIeh-GUV-PdNe5-s3j-w7NDerm4muA9bHu--Z0zzM4wgM2Np567hdjRwB23npYiwqdXSu-hgHflZM6TbodT-zRd3t1liJQcJ6L1duydgu8UY3kGVfB-K34-5v_6-mr0WtgIh9UjMFPuVq17UoMxwxcivWwJmn6cM4qX8qTV89qbTYs0FHw_xFdpIVf983UwyDKbhV6PmGFkRdzKcHJd1ONsZhty4bRySaQ-JW9DEZJMT-fdEasW1X3C9aGFvS0k74Udgns69YUaCamT-_GXedIzhTz_P0RyCjem2Xz1NN7qA8fTT_YWbdtVCrQMqPSfvgJw_Am8oJVbbx_MNRh0GBxOWDnDSET_5tU1qlx50liQAuUIqkG8ZNXBLIVc7la6zj3ju7XAwksJPFsT5pE1hHcf5XfQZC7axnjnTl1pDJ44j-Q0rHXiZDVyvow29bqwP8UKhfhOj1XCpb2xkTpX6CUqDGLm8oFFfSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=DaczE-zgdcVGCtTyTyKWw88hl7lJE_j1CCxnCg0rJK3M68eAY9q9nEk77bDkIHzINAByJr_VoBK2HocNT5-Kz508sJXodlZYIPJEu_h3fWR_gv_aN4UcubtuoMabZKJxVccgSLc7rq61bgic8RH0TNk5xTXz-gnS5YwseorUIrM-wtm9B3kfIZRfQwh2k3ji6rob0jKBrCIeh-GUV-PdNe5-s3j-w7NDerm4muA9bHu--Z0zzM4wgM2Np567hdjRwB23npYiwqdXSu-hgHflZM6TbodT-zRd3t1liJQcJ6L1duydgu8UY3kGVfB-K34-5v_6-mr0WtgIh9UjMFPuVq17UoMxwxcivWwJmn6cM4qX8qTV89qbTYs0FHw_xFdpIVf983UwyDKbhV6PmGFkRdzKcHJd1ONsZhty4bRySaQ-JW9DEZJMT-fdEasW1X3C9aGFvS0k74Udgns69YUaCamT-_GXedIzhTz_P0RyCjem2Xz1NN7qA8fTT_YWbdtVCrQMqPSfvgJw_Am8oJVbbx_MNRh0GBxOWDnDSET_5tU1qlx50liQAuUIqkG8ZNXBLIVc7la6zj3ju7XAwksJPFsT5pE1hHcf5XfQZC7axnjnTl1pDJ44j-Q0rHXiZDVyvow29bqwP8UKhfhOj1XCpb2xkTpX6CUqDGLm8oFFfSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار رحیمی: از امروز اگه یک سایت یا رسانه قیمت ارز (مثل دلار و یورو) رو منتشر کنه با اون سایت برخورد قانونی میشه.
جدی‌جدی اینا فکر می‌کنن با پاک کردن صورت مسئله، اصل مسئله هم پاک می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72847" target="_blank">📅 23:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72844">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=EXN8Yqw3jXMxGoCge1fwFg4XK3haR1DYshq8tnCJ-icUWRshG1X3fUgfCdaALZL_dYazfvHlq3rJ_QpnVVzDwM3oNFb8lVE2NMaO0NU2EDEmQAcpkLrXRgldQApxWO4QSIvmcDS5XdR8EjwCDBZhb4lHGUelHWof8br43kSEuxJDNf73cQWNpqdynNtFuK0uTVis_ztBuWO11CCdY0sgjQjgwK6uXG30dKMLzpP2ne0qYegf_IdNUNIW4jSgJJUMme-m8el9B18TAqGtcrd54JmyMDphc4ZFsa7GoDKZ2aRZxITrq5WqB8fQvivvB1iUiKaaovQ7-md8siHQ91cYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=EXN8Yqw3jXMxGoCge1fwFg4XK3haR1DYshq8tnCJ-icUWRshG1X3fUgfCdaALZL_dYazfvHlq3rJ_QpnVVzDwM3oNFb8lVE2NMaO0NU2EDEmQAcpkLrXRgldQApxWO4QSIvmcDS5XdR8EjwCDBZhb4lHGUelHWof8br43kSEuxJDNf73cQWNpqdynNtFuK0uTVis_ztBuWO11CCdY0sgjQjgwK6uXG30dKMLzpP2ne0qYegf_IdNUNIW4jSgJJUMme-m8el9B18TAqGtcrd54JmyMDphc4ZFsa7GoDKZ2aRZxITrq5WqB8fQvivvB1iUiKaaovQ7-md8siHQ91cYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ توی آب‌های نزدیک سوچی
امشب یه آتش‌سوزی گسترده توی آب‌های نزدیک سوچی روسیه راه افتاده؛
توی ویدئوها یه خط طولانی از آتیش و یه ستون خیلی بزرگ دود سیاه دیده می‌شه که از نقاط مختلف شهر هم قابل مشاهده‌ست.
حساب‌های نزدیک به اوکراین مدعی شدن این نفتکش هدف قرار گرفته، اما منابع روسی فقط گفتن یه شناور نزدیک بندر آتیش گرفته و فعلاً علت حادثه مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72844" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72843">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72843" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72842">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ایران در اعتراض به برخورد دولت فرانسه با اعتراضات دانشجویی و چیزی که «نقض آشکار حقوق بشر» عنوان کرده، سفیر فرانسه در تهران رو احضار کرد!
وزارت خارجه ایران هم از فرانسه خواسته به تعهداتش در زمینه حقوق بشر پایبند باشه و آزادی‌های اساسی، به‌خصوص حق تجمع مسالمت‌آمیز، رو رعایت کنه.
جالبه رژیم جمهوری اسلامی که بویی از حقوق بشر و برخورد مسالمت‌آمیز نبرده میاد به بقیه کشورا برخورد مسالمت آمیز و رعایت حقوق بشر توصیه میکنه!
یه نکته دیگه هم که هست اینه که تا امروز هیچ گزارشی مبنی بر اینکه معترضی در فرانسه کشته شده وجود نداره و گزارش های رسمی که وجود داره نشون میده فقط بیش‌ از ۲۱۵نفر دانش‌آموز و ۸۵کادر آموزشی زخمی شدن.
از نیروهای دولتی هم حدود ۷۱۵ نفر نیروی پلیس و ژاندارم در جریان اعتراضات زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72842" target="_blank">📅 20:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72841">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEQqZm5TVeHPfH-aDoyMidj5LQ2X-m9ebiRllIeapCuQqi-nbHbkH07t1ZkeyWo5lVX5RQIekqCRhvEvql6ThBbRKLnn_qdoAZbWfQN1PTiZlQv0RYjTnoEnkAaCVkkIpzwF0T-9-ZSZn9qdi_0tvNzdqVDh-yBSm2DsHfcYxgjbHVXWoXayfe_AVi9mqQcM6KMLT1RqPZIS9cjSmMHSK3ZyqD6-FFO4BbUXdRCcqPojkU2VolIOQXCar8PmyYbSfPuj2rCXWwm82jNIgHrzGzHiAyuWdvVDfVnqPo5Xbh4leAlUqswD8v2WMTiFprJi7TFIVhPeUwgcBEyXwhuCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72841" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72840">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#فوری
؛رایتل رسماً به مزایده گذاشته شد؛ شستا ۱۰۰ درصد سهام این اپراتور را با قیمت پایه ۱۳۰ هزار میلیارد تومان (۱۳۰ همت) برای فروش عرضه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72840" target="_blank">📅 18:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه مرد ۲۲ ساله بریتانیایی به اتهام مشکوک بودن به آماده‌سازی اقدامات تروریستی، در ارتباط با پرونده مشکوک پایگاه هوایی RAF Fairford بازداشت شده.
پلیس ضدتروریسم انگلیس گفته این فرد امروز توی وست‌مینستر لندن دستگیر شده و هفتمین نفریه که توی ارتباط با این پرونده بازداشت می‌شه؛ البته تا الان برای هیچ‌کدومشون اتهامی ثبت نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72839" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=OkfE0rzvRiEfcj5w41AYbZL4-SUlKw3XH6EUmTiGRBcbN9hOpA_KDeQuPLGWP2piMAopMSdeta2vgSgT5s8ql6H59QNJfSpFrV_gf4Ld3g5S7sL9ClbdTBAeT-xWzPxv1ZSx6ijZkxreGHuqscrc2cm42SsoDFBDtJRZprDODM1uvf3Yc1A3GcKfd7S2yHOd3O6w-W4DT21MntuY5fuu0AkkpAFVK9_IKq7r8QTiDdGeVKebiwloS0C9CjyNEQE-5-XdmuyPAt3afQd7_UZvjDpXXye1TciDAQHto3UBdfEMW2VtuRzOBk0uYrx8mMObtEImJ5VBRPwbxNSvqaawMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=OkfE0rzvRiEfcj5w41AYbZL4-SUlKw3XH6EUmTiGRBcbN9hOpA_KDeQuPLGWP2piMAopMSdeta2vgSgT5s8ql6H59QNJfSpFrV_gf4Ld3g5S7sL9ClbdTBAeT-xWzPxv1ZSx6ijZkxreGHuqscrc2cm42SsoDFBDtJRZprDODM1uvf3Yc1A3GcKfd7S2yHOd3O6w-W4DT21MntuY5fuu0AkkpAFVK9_IKq7r8QTiDdGeVKebiwloS0C9CjyNEQE-5-XdmuyPAt3afQd7_UZvjDpXXye1TciDAQHto3UBdfEMW2VtuRzOBk0uYrx8mMObtEImJ5VBRPwbxNSvqaawMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون شاهد نخستین شلیک آزمایشی موشک بالستیک جدید M51.3 فرانسه از زیردریایی هسته‌ای «لو ویژیلا» بود.
مکرون:
این آزمایش، اعتبار و قدرت بازدارندگی هسته‌ای فرانسه رو نشون می‌ده:
«برای اینکه آزاد باشی، باید ازت بترسن؛ و برای اینکه ازت بترسن، باید قدرتمند باشی.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72838" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=So3NJiNIJxxtj_mJpop4jj2bVK4GjL7c96pGAMhjYT5ogkWE_sd6KdihNhB8NnqRmUnV3Akub0QCxJIsC3V50gG685DH-rrWkXjvIP1Gzmna6vGICJelDRE0zAqgkrpbXn0yAWpJfDtAljH2NZ3Y4Gaz6OAA9EjGZwUb_SpJXaTStP0yXfuIGhYYMFybw95V6gy-PPRiBLyGp5nJd5er0jYx0KnLNmU0B0VW7_pQwfwBhpMC365iNcxLrLBPKQxD82UXzD0vYHtSVH8fcCmrmeYdaG2z3__OkWHUjZFWFX1TVyYHya8VBAV4V97_pves_1YjEI4xdzg5BuqmHqQU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=So3NJiNIJxxtj_mJpop4jj2bVK4GjL7c96pGAMhjYT5ogkWE_sd6KdihNhB8NnqRmUnV3Akub0QCxJIsC3V50gG685DH-rrWkXjvIP1Gzmna6vGICJelDRE0zAqgkrpbXn0yAWpJfDtAljH2NZ3Y4Gaz6OAA9EjGZwUb_SpJXaTStP0yXfuIGhYYMFybw95V6gy-PPRiBLyGp5nJd5er0jYx0KnLNmU0B0VW7_pQwfwBhpMC365iNcxLrLBPKQxD82UXzD0vYHtSVH8fcCmrmeYdaG2z3__OkWHUjZFWFX1TVyYHya8VBAV4V97_pves_1YjEI4xdzg5BuqmHqQU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل: هر موقع میرفتم خونه و می‌دیدم کفشای لِه و درب و داغون پشت دره، می‌فهمیدم مجتبی خامنه‌ای اومده :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72837" target="_blank">📅 18:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72836">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72836" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72835">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-rpgSKIPODyoAxViPrKr8T1P65BaxyuZYwDh5nJ-QlUoYmdo4cx0TQreKMUn0dzcMG7FrJzYgIuHQyrA6GbHM_JVOAyTPOEweAiGDyuvoi-rwmZl6kwEns5YLhrlWgBERgx015fmgcFWfrz1chuV8lzmIZIw9dZA4_PIQVkNjQGLPtj2qNED5_EOQQPJiJtCzN60BD9iKqVGTSh4GdYyGPfkTR_jHgKe5dx54zgqNsLRPcRWPXdngsLiEiBpAtNY3HcSYOrjqV1kvesYH03ysNUk6fkoWrnhEZvrabfNaxGgibapobQnwMyCJP1VZcr-gVqfdVKKbR3NxIWqFeN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72835" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مارکو روبیو درباره مورد مشکوک طاعون در روسیه:
«فکر می‌کنم روسیه باید اطلاعات بیشتری رو در اختیار دنیا بذاره. کاری که باید انجام بدن همینه و امیدواریم همین کار رو بکنن.
ما هم داریم موضوع رو خیلی دقیق زیر نظر می‌گیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72834" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=TojQcZivarES6wVXaYcDB85v-EfD03dTLPlho5bZ-HGxWf21ciF3QtemIFkjc_9gAdaMez0NwFWm6V9NLgPiQBa7fLA5U4oylZe4rWFyRc7c87m55Dp9as0yha4t7F1vDhsoO8qwQtomCyQi5Xew9r8Rnl2CgM8qPZJiWhCjoWTygLvEPfjclXV6Di6EcC1D0jN2IeQDOnwUv_S-toUnDa-IxFsxu7nvYqZDHaO9lcSl0ZMAvriXdJ_yEJtckSR8gLb2XBfrZp-guLnVzf2IdOWoEq7g1LQtQdFMuvfSYbBN-_nzDngNSeWplwixWFvbRqHXCY6PeFxlHS84KuwJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=TojQcZivarES6wVXaYcDB85v-EfD03dTLPlho5bZ-HGxWf21ciF3QtemIFkjc_9gAdaMez0NwFWm6V9NLgPiQBa7fLA5U4oylZe4rWFyRc7c87m55Dp9as0yha4t7F1vDhsoO8qwQtomCyQi5Xew9r8Rnl2CgM8qPZJiWhCjoWTygLvEPfjclXV6Di6EcC1D0jN2IeQDOnwUv_S-toUnDa-IxFsxu7nvYqZDHaO9lcSl0ZMAvriXdJ_yEJtckSR8gLb2XBfrZp-guLnVzf2IdOWoEq7g1LQtQdFMuvfSYbBN-_nzDngNSeWplwixWFvbRqHXCY6PeFxlHS84KuwJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی : مردم ایران در دنیای واقعی خیلی خوشحال و شاد هستن ، واکنش ها تو فضای مجازی دروغ هس و حقیقت نداره
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72833" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=sBFmsHbM69K4pJnmB-7n_mkb0L7W1PrordgR8UhQTEGKvyIn-tTZ2cKe5Ac-z9WRtETiHcQK0nctLI5O67Fg9uEgoZaEw8yenrhTQojmnl9yN1deijjpQLTXZG1Ei2MiVUOFBFM9YKzId4FbDVb9jkja3_tTOw7MzvZzTAi2BMwZV-hmSSWj2QXeOPimDpJi81iktISFTkSwO0STKZDr9jurolA7tE1JpwALuZ_HMqKQA3qeo8rUX07-I1SnQ0ILXO35x9mzQLLlWwBHZd79dw7NbJzQ2c_81tLusFXMh4PelP_EvorplFyO4mysxfJpCWeFSRL_Pcl5ktAAAtw0j4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=sBFmsHbM69K4pJnmB-7n_mkb0L7W1PrordgR8UhQTEGKvyIn-tTZ2cKe5Ac-z9WRtETiHcQK0nctLI5O67Fg9uEgoZaEw8yenrhTQojmnl9yN1deijjpQLTXZG1Ei2MiVUOFBFM9YKzId4FbDVb9jkja3_tTOw7MzvZzTAi2BMwZV-hmSSWj2QXeOPimDpJi81iktISFTkSwO0STKZDr9jurolA7tE1JpwALuZ_HMqKQA3qeo8rUX07-I1SnQ0ILXO35x9mzQLLlWwBHZd79dw7NbJzQ2c_81tLusFXMh4PelP_EvorplFyO4mysxfJpCWeFSRL_Pcl5ktAAAtw0j4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش چشم بازم تحلیل کرد و گفت جنگ در پیشه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72832" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=MCUUIQyni-iYpo4EHt2qCfFdxkTLYn4zTAZRaG9aKsaQdiPbYW-TQvqt1uLU3OKeeAeAuFA-6VxAr8jvMmJx5z8b2EyC6K8QgDyZ-B0_AoODcvtf0J83lM8tUnKHagCUSk8gbSc5xojLaOxzPUme-KOwgONmYOAtqL3jnvyvmW--fO8G0cX4wZxi9SCkHs3LXDIl0osLGs3dTchjeMalwqjdM0ZWpWE5SX3MaG2zHLfVBmgHTyK5Tw6jCFX5HdGWUGYmVRsC2Puss65JGoYHu2MwgYsEkSS1G_sovpmlizn3nQ0iBxMKLt9WBQHGeQM_H-nvx86PWqSokwDWrvryiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=MCUUIQyni-iYpo4EHt2qCfFdxkTLYn4zTAZRaG9aKsaQdiPbYW-TQvqt1uLU3OKeeAeAuFA-6VxAr8jvMmJx5z8b2EyC6K8QgDyZ-B0_AoODcvtf0J83lM8tUnKHagCUSk8gbSc5xojLaOxzPUme-KOwgONmYOAtqL3jnvyvmW--fO8G0cX4wZxi9SCkHs3LXDIl0osLGs3dTchjeMalwqjdM0ZWpWE5SX3MaG2zHLfVBmgHTyK5Tw6jCFX5HdGWUGYmVRsC2Puss65JGoYHu2MwgYsEkSS1G_sovpmlizn3nQ0iBxMKLt9WBQHGeQM_H-nvx86PWqSokwDWrvryiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید.
خبرنگار: همتی هم گفت از شما سوال بپرسیم.
مدنی دلقک: نه دروغ میگه از خودش بپرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72831" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72830">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=Lz8tqKsr6n_3KdJP-z6arxpy9QzATh30EsK_H0449TDsMO9nkClgCodSVxTrh0ZsIRi8Ndn2wt8QdgsrTAKsFp88duPWukF60jWnUgVmWKqhf8BnmOKu0AEWCoBrRlpl-mDGamJO-gpzjoQTuNp5QSXOfxT6IMdqVqgBN6QC1wfg2mZ4I_kQ_tHpad1WBObJUDn9yjk_5Htf7KpK1AVoyaKzcd_sO7byrymiesmVJJsNdHT8UY9mvVkgFWzD0DmehQz8pNRz_5S_IuFdxMbm-n9XdNwWZcftYRzIzYGVIAwfdMLIqkDtrRi6Qaq5xtI_tyEDK-HgDs4TAEW6BtOqFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=Lz8tqKsr6n_3KdJP-z6arxpy9QzATh30EsK_H0449TDsMO9nkClgCodSVxTrh0ZsIRi8Ndn2wt8QdgsrTAKsFp88duPWukF60jWnUgVmWKqhf8BnmOKu0AEWCoBrRlpl-mDGamJO-gpzjoQTuNp5QSXOfxT6IMdqVqgBN6QC1wfg2mZ4I_kQ_tHpad1WBObJUDn9yjk_5Htf7KpK1AVoyaKzcd_sO7byrymiesmVJJsNdHT8UY9mvVkgFWzD0DmehQz8pNRz_5S_IuFdxMbm-n9XdNwWZcftYRzIzYGVIAwfdMLIqkDtrRi6Qaq5xtI_tyEDK-HgDs4TAEW6BtOqFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
اسرائیل توی ۱۴ ماه گذشته اسم ۱۴ تا خیابون و بزرگراه توی تهران رو عوض کرده! اونی که عملاً داره اسم خیابون‌های تهران رو تغییر می‌ده، اسرائیله؛ اسرائیل همین‌جوری مقام‌ها و فرمانده‌های سپاه رو می‌زنه، بعد شورای شهر میاد اسم همون‌ها رو می‌ذاره روی خیابون‌ها!
دفعه قبل هم بعد از جنگ ۱۲روزه، اسم چند تا خیابون و بزرگراه رو گذاشتن به اسم حاجی‌زاده، سلامی، باقری، رشید و شادمانی؛ یعنی اسرائیل اینا رو می‌کشه، شورای شهر هم جلسه می‌ذاره که خب حالا اسم کدوم خیابون رو بذاریم به اسمشون!
در واقع اونی که داره اسم خیابونای تهران رو عوض می‌کنه، نتانیاهو و موساد و نیروی هوایی اسرائیله؛ شورای شهر فقط می‌مونه و تابلو رو عوض می‌کنه!
با این حساب، اگه همین روند ادامه پیدا کنه، باید منتظر باشیم هر بار اسرائیل یه مقام دیگه رو هدف قرار می‌ده، تهران هم یه خیابون دیگه به اسمش دربیاره!
یعنی خلاصه تقسیم کار اینه: یکی می‌زنه، یکی تابلو می‌زنه:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72830" target="_blank">📅 15:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72829">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmV3n3v5LJ311NaJGqu53zicozo2NnflivjDoV4RTjmS9pDO4sRAMdc6XQJ0wplf9XxcXF6SQ802g6e2gNHybGWFiSkiSlw596VgIFqrl1XHkT2xLsaDtTaOrJq2M4bxXk7IZDfRtnnsLUL_F59m9WyS8kzl7rSgav47oXoBiOMX7b7HUE5SHcnvTE2Rgjc7G7hsS_P5bR0211EY6i53P87Blgz8297Q2NHKEgamrwdOzVLmFRWkrSGk0-IZI9PpX1DLcBwJmSA24zNUwzmyuUDPKBLW8fB8RjBXLqLOmJC3gRBFz5rRCxa5mtoQvjJaXcrrM4mmejXxzjLgjjXaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه از تاثیر سهمیه! توی کنکور امسال یه نفر رتبه‌اش ۸۱ هزار شده بوده،
که با سهمیه ۲۵ درصد، رتبه‌اش ۲۸۳ شده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72829" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=Vl5WEi-TfrisNoqhU5Ij9R1awk-FEpQOIjBQhlp9RmEN1KWsSFShzYmg1KEkuzzML3gZaGRxdofHrh3g9LOzBHUBoJx1E6AzzegeyKlOHv2i3jNoujUOI7SJ6G-DCeaIdE0BQuzt29F42C8zdTGqJLxPnt9w3Q5IX_5bsu2xNTOqUL3RfXPIOJJrM9f29pl-OHjxDzEIetf8azAfPdZqDUvcRxxczI0nY6oDdSRGGaR5YiKfA5tgsmrHWxnejeqIsyRJ9jY01sv8kqb2ucn4t2eyOjAnTD3T3JRwCnhwk-xq3h43eFKGqf58Um5CSulXBwtmQjTjkQ1BE5gPWRVjbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=Vl5WEi-TfrisNoqhU5Ij9R1awk-FEpQOIjBQhlp9RmEN1KWsSFShzYmg1KEkuzzML3gZaGRxdofHrh3g9LOzBHUBoJx1E6AzzegeyKlOHv2i3jNoujUOI7SJ6G-DCeaIdE0BQuzt29F42C8zdTGqJLxPnt9w3Q5IX_5bsu2xNTOqUL3RfXPIOJJrM9f29pl-OHjxDzEIetf8azAfPdZqDUvcRxxczI0nY6oDdSRGGaR5YiKfA5tgsmrHWxnejeqIsyRJ9jY01sv8kqb2ucn4t2eyOjAnTD3T3JRwCnhwk-xq3h43eFKGqf58Um5CSulXBwtmQjTjkQ1BE5gPWRVjbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشور چین واقعا عجیبه، روی یه شهرک یه شهرک دیگه هم ساخته شده. شبیه فیلم inception شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72828" target="_blank">📅 14:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72825">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1Ml8GtVii-_np5FYAHh9xU3HKSEpPuInydzAlpOdnL3Tfq9S3WXXWcXdxlNyvdRNjfFvToesUrMLNLxVXi7g6In_Ok9Wjw8N2Le8t2ftb0ZTae_d9gBM1_P16HWQhVG9pGK_rV4i40St6glzrlzVNAeKexnuE3QYsw1bpGn93biuSmsgy6KYhNuYqOCc3icR2wmnfgpdIWNcXamuUMkH6uo6glsy_wqeo4G0fVLIQ21izoxnyouB84aoaMlZc3Sy01yxlg57A8PtxW0fPmRCd6P34oYIKMmalh4dWxjrPiFD74-YFiOt0tBYCM4TSc95CqgyDifODX2yb9kXRTJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQqWjCqg6Ph4UoFifp1ScUVQDIESSyJ-liiCn4U298ewSMw_45xr9-OHG_a36-_rrjobV1po-w5Hvf0Hqf_tf7QWAxZOXX2Qe9ggFh-5X8nPL3E6j0T4X2S8EXtUVC_tK9rbkYog0xm5GQshByJWvnEZHo9iG4DJj1qtja80jvTLg1DOAWAwwRZODJqPzax5CE1CpgnxVFN7HqqeuFTYJoinsOQ6A98WuxgIPQVVhxAu5aun27hGthK1PUQunr-Yq4jxAdpoVB3HC84_AXHZwwUmVkVCPECxdPln2FoNutM35gXs2V7kfIfdIieYxgDUB7n1PIKo8hZnfkT-s5U-6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=ANeIj_9NgDKn9nQXBEkShG1KvipSsUxDBRfke0ZWMY5zwmlkvImEXNOnWTPTMVnkHelSOOjLp5ZTiW1_f1WGeorsYirjhlVkKqPqtkQXTWYAxL2yyXbCXwFohqjwNa0OS8sTk9K2tHNggf8V0_xGNOyXV3uO5LgwJwwwC-p9PvzrDOIy312-FbQAg1v85EC-EUvtAqOH6kQ6_JqixV_LYF4XEq0N7yVMDwIu9AQG0n68FI2UUGO5hxiZYammY56OGSBKi05owqpzN-VeKJdYFf7djGEXZkyUSe55GJhYHLYQrih_MoIef2dmHMYxop1a6cSSrjnm3GJ5YagkhOrUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=ANeIj_9NgDKn9nQXBEkShG1KvipSsUxDBRfke0ZWMY5zwmlkvImEXNOnWTPTMVnkHelSOOjLp5ZTiW1_f1WGeorsYirjhlVkKqPqtkQXTWYAxL2yyXbCXwFohqjwNa0OS8sTk9K2tHNggf8V0_xGNOyXV3uO5LgwJwwwC-p9PvzrDOIy312-FbQAg1v85EC-EUvtAqOH6kQ6_JqixV_LYF4XEq0N7yVMDwIu9AQG0n68FI2UUGO5hxiZYammY56OGSBKi05owqpzN-VeKJdYFf7djGEXZkyUSe55GJhYHLYQrih_MoIef2dmHMYxop1a6cSSrjnm3GJ5YagkhOrUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یکی از همون ناوهای آمریکاییه(USS Delbert D. Black (DDG 119)) که سپاه تو بیانیه‌ها گفته بود موشک بالستیک خورده و «خسارت قابل‌توجهی» بهش وارد شده. ولی خب، به نظر من برای ناویی که موشک بالستیک خورده و خسارت قابل‌توجه دیده، زیادی سرحال و سالمه!
الانم برای استراحت چند روزه خدمه، وارد پوکت تایلند شده و بعد از تمیزکاری جلبک ها مثل روز اولش می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72825" target="_blank">📅 13:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72824">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=t2SjqZqSTu63dyEPWDds8enKv5eHznvDyP2vo4StkOicpUN22CywfOD0hXqxMQ7CujCADZj2uVtpfpysoOeauGUfi8jah7V7AjdoNdWCJGlTTAq6oCSjOTNpYEyYzUnx0t5D4hFshvsUs4mQ_2iKNV6FtfVYBAdA85_SdXqiEYHWw_JWbmETWvQo5l0olJGB0QWbP1RsWmlk03eB-XNQ7i4aqDY9pawHlCMYtzzqscOt41rE9osDWz_dL1W3ifN0118SHAbPj8jqfIvNc5yrfuFLpAByL17SnrW0zjPN1_k2-OSkJEQrFTQVxOoj-9mGM3z4pfQ6ORSHWJ2a3D_yOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=t2SjqZqSTu63dyEPWDds8enKv5eHznvDyP2vo4StkOicpUN22CywfOD0hXqxMQ7CujCADZj2uVtpfpysoOeauGUfi8jah7V7AjdoNdWCJGlTTAq6oCSjOTNpYEyYzUnx0t5D4hFshvsUs4mQ_2iKNV6FtfVYBAdA85_SdXqiEYHWw_JWbmETWvQo5l0olJGB0QWbP1RsWmlk03eB-XNQ7i4aqDY9pawHlCMYtzzqscOt41rE9osDWz_dL1W3ifN0118SHAbPj8jqfIvNc5yrfuFLpAByL17SnrW0zjPN1_k2-OSkJEQrFTQVxOoj-9mGM3z4pfQ6ORSHWJ2a3D_yOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم طرفدار حکومت:به پسر نوجوانم گفتم اصلاً نگران نباش!
خواستی سیگار بکشی، بگو خودم برات می‌خرم؛
خواستی قلیون امتحان کنی، با بابات می‌بریمت سفره‌خونه؛
فیلم مثبت۱۸(پورن) هم خواستی ببینی، بیا با هم ببینیم! این‌طوری دیگه خیالم راحته که همه‌چی کاملاً تحت کنترله!»
@News_Hut
😐</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72824" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72823">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=OWu0BdCX_zpSeqmJmCXe-mU6BJ__hIud03776ce_N-kEBf7UmmHpoTgSUBjR88KH0T2AOGOrrZDCw_ZIApDPcqxuBHYBHkqv4Ihzgid5ZpS2DVHHbSwV-rxuGM73AV1qfuNAzkGWo-21NT-8oYpKybDP2-yH6b2nlxB23OK9CrWUsJ9u1I3dmJ5oIbSjtETWrtaeQzuqIeuLLHs4cyT11L0QFQham--eBOyh6Qhy1rPGcIkahyIyTIhbI03EtU_yreh3zQZadHuFbjCrX78KvTFeBudt2eRSAr7Eqk-njNCB5w-vvNseTCqXFtYVLNy0WQYPwfMl6kC8ApkPuTwqwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=OWu0BdCX_zpSeqmJmCXe-mU6BJ__hIud03776ce_N-kEBf7UmmHpoTgSUBjR88KH0T2AOGOrrZDCw_ZIApDPcqxuBHYBHkqv4Ihzgid5ZpS2DVHHbSwV-rxuGM73AV1qfuNAzkGWo-21NT-8oYpKybDP2-yH6b2nlxB23OK9CrWUsJ9u1I3dmJ5oIbSjtETWrtaeQzuqIeuLLHs4cyT11L0QFQham--eBOyh6Qhy1rPGcIkahyIyTIhbI03EtU_yreh3zQZadHuFbjCrX78KvTFeBudt2eRSAr7Eqk-njNCB5w-vvNseTCqXFtYVLNy0WQYPwfMl6kC8ApkPuTwqwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سال 2023 یه میم به نام Opium Bird خیلی وایرال شد که یه موجود بزرگ و پرنده‌مانند تو کوه‌های برفی رو نشون می‌داد و سازنده‌اش گفته بود که سال 2027 (۲ ماه و ۲۶ روز دیگه) می‌فهمید یعنی چی؛
حالا شباهت Opium Bird و طاعون
👺
و همچنین لوکیشن برفی اون میم و آب و هوای روسیه، دوباره همه رو داره به این فکر فرو می‌بره که نکنه داریم وارد یه سیزن جدید می‌شیم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72823" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72822">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=NjO55sMDggk1muuy3THXVgXoyhNqHHjpCa1eNGMFwwBlbDrKb_yVTzmPGT2vJV9jaSVam3sqPUvZsljoXbWatnuhPex9DJl2MU96xJi7GbKsS8dkkNXm-3hYTS_56I5H9JDoLcSSe3vAjZAERlc6TNsKQ3wYKjRn_LIyhiC7WcRgmkarlSqmIFjSiLVZs15cp7ZfzxoO53tjqx7H-BlXRALR-Aujg86E16SgF2RxUn_h9HR8QJP-x1mTxRh_zbTzC_bxvEQ6BStq4MOYJcmAtXS1GH7Q3ygOq_6Kg9uKI01GHsOFxB0X5CNxQGwPwWSkAeQPxJhIhRpLy7gGx0iw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=NjO55sMDggk1muuy3THXVgXoyhNqHHjpCa1eNGMFwwBlbDrKb_yVTzmPGT2vJV9jaSVam3sqPUvZsljoXbWatnuhPex9DJl2MU96xJi7GbKsS8dkkNXm-3hYTS_56I5H9JDoLcSSe3vAjZAERlc6TNsKQ3wYKjRn_LIyhiC7WcRgmkarlSqmIFjSiLVZs15cp7ZfzxoO53tjqx7H-BlXRALR-Aujg86E16SgF2RxUn_h9HR8QJP-x1mTxRh_zbTzC_bxvEQ6BStq4MOYJcmAtXS1GH7Q3ygOq_6Kg9uKI01GHsOFxB0X5CNxQGwPwWSkAeQPxJhIhRpLy7gGx0iw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«همه دارن می‌گن من GOAT ـم، یعنی بهترینِ تاریخ.
من می‌گم: «پس واشنگتن و لینکلن چی؟» اونا هم می‌گن: «شما از اونا هم بهتری، آقا!»»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72822" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72821">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=Ugixmp81CLRxBTxu3yyp7j3LWbDpPhEibJW_z0GbTMmpnCzXkrfBAmo4tiLTKxjBFmNcZMPiAWOxEMl75MWOVUUmoDUylslf76O1_MRQA51mbcvlcVhKIIiVg3glSME0lI9lmz21IxbnDucSX2z_LUHTbOJQ-eY3hZ94SvU_xr05YtqcbsY6EM1auD5U0qkL3Bad7yw9D9XyD1YMuHaNhZY-U64AItJWSLOnRGQfK-TBUFN1clh5yMwbiHFOl3rhKPubKRTNFC2BkiTWE2HuTXTkABXK2JxlUssJg2oEaJqwU0xrFS_lLXG3Y5HZV_xn3iLC7cveAECF06CaL2IR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=Ugixmp81CLRxBTxu3yyp7j3LWbDpPhEibJW_z0GbTMmpnCzXkrfBAmo4tiLTKxjBFmNcZMPiAWOxEMl75MWOVUUmoDUylslf76O1_MRQA51mbcvlcVhKIIiVg3glSME0lI9lmz21IxbnDucSX2z_LUHTbOJQ-eY3hZ94SvU_xr05YtqcbsY6EM1auD5U0qkL3Bad7yw9D9XyD1YMuHaNhZY-U64AItJWSLOnRGQfK-TBUFN1clh5yMwbiHFOl3rhKPubKRTNFC2BkiTWE2HuTXTkABXK2JxlUssJg2oEaJqwU0xrFS_lLXG3Y5HZV_xn3iLC7cveAECF06CaL2IR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«این جنگ خیلی زود تموم می‌شه و قیمت‌ها هم قراره حسابی بیاد پایین. شاید حتی خودتون بگید: «خواهش می‌کنم آقا، این‌قدر سریع ارزون نشه!»
😂
خودتون ببینید تو یه مدت کوتاه قراره چه اتفاقی بیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72821" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72820">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=QLJLKwjNFBfHAPNVPgiJZj1bsITFC40NAfA7PIfwFDhUxQA2lagUTYAs2yxRSRY0AQPTlYH5rQBYDer7L-BydIFb4TNeSzwwQbxSsu22mSrdkpsIqVo9u7YHSIns6x-cvjhVRZyLG4kr0MEvy7SJEhuFPiBZNVyI4wcATRSGWkMvj3oxnP1siqfzRkcrZU1Nrc5c4Fa1l9SgY2BD1BXdYvRolJVWeCCdLDn0ZEEpniG5DAxutGbZLU5uK7i_5R_r4aMCQwZF9MI0CYywIfF10fCEqCmJQC1wfGjpJHk1qbqUUVfTZ6_y7DKwkU1VBrFRvXiiaN421aPa-6MRqAHWfxCe-Ctd04ruZzwqB_MMoNhtXgJPGINJ7QE9Vtkd5jzGH8dt89tyhGpLuYPY1unxBmc0B4ujyog3oE0bm_H8B0uFX9opw8ycytQQ3Ek1Pk65GJhOjp4TlD6GUJ4nV_lNkrIhKqHF92QbTxNDKFosASl6-ggB41OcdbgMGOKlLPnYAzeE_Dr0nAmUgsbdAp_uAce_upY_TltmW3NOGF_GA4qolbxX7Mbf0bZTHo1oUxydb2QhZqSQ8YL_UHN2uzjYXZc1xj0ZZGFfdtaQIzq3WV6Ydlozt-0MQZBw5yTN8cuP-BQ0i0UnSOuzjcgr2d8UHvJFuB2sezUvgH4L2_5hens" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=QLJLKwjNFBfHAPNVPgiJZj1bsITFC40NAfA7PIfwFDhUxQA2lagUTYAs2yxRSRY0AQPTlYH5rQBYDer7L-BydIFb4TNeSzwwQbxSsu22mSrdkpsIqVo9u7YHSIns6x-cvjhVRZyLG4kr0MEvy7SJEhuFPiBZNVyI4wcATRSGWkMvj3oxnP1siqfzRkcrZU1Nrc5c4Fa1l9SgY2BD1BXdYvRolJVWeCCdLDn0ZEEpniG5DAxutGbZLU5uK7i_5R_r4aMCQwZF9MI0CYywIfF10fCEqCmJQC1wfGjpJHk1qbqUUVfTZ6_y7DKwkU1VBrFRvXiiaN421aPa-6MRqAHWfxCe-Ctd04ruZzwqB_MMoNhtXgJPGINJ7QE9Vtkd5jzGH8dt89tyhGpLuYPY1unxBmc0B4ujyog3oE0bm_H8B0uFX9opw8ycytQQ3Ek1Pk65GJhOjp4TlD6GUJ4nV_lNkrIhKqHF92QbTxNDKFosASl6-ggB41OcdbgMGOKlLPnYAzeE_Dr0nAmUgsbdAp_uAce_upY_TltmW3NOGF_GA4qolbxX7Mbf0bZTHo1oUxydb2QhZqSQ8YL_UHN2uzjYXZc1xj0ZZGFfdtaQIzq3WV6Ydlozt-0MQZBw5yTN8cuP-BQ0i0UnSOuzjcgr2d8UHvJFuB2sezUvgH4L2_5hens" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«یادتون باشه، این جنگ یه چیز مصنوعیه؛ یه مقدار هزینه‌ها بالا رفته، ولی خب برای اینکه دنیا امن بمونه، قیمت زیادی نیست.
اگه اونا بتونن یه شهر رو بزنن، بذار لس‌آنجلس یا سن‌دیگو رو بزنن؛ این در برابر حفظ امنیت دنیا، قیمت خیلی کوچیکیه.
در واقع، این ماجرا تقریباً دیگه تموم شده.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72820" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72819">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=FzIGjR5ZcVj4-fSPTXfqUsR2Uzd_9_V6bchVLnf8s6BsKdo4JzZ82wvYlteTUVih-ewwtSDdY-VCyTe0qjJjMTbMkLmUteeg_rec-LD6zRUnFtFwFuINMUb98jKmgn8r_Bv2xUbXMqvBtYWVM8Ke1rv0qZP4yJOPQLDWDAkYwyo9GwgJm_nSJEqUbRIeQr_sZd-0vH0KFwIkNRUOnCyayrih63GbTb6xO25tEBtyG0M6Xkf-x6k_q5mhV02LDpCncB1TFbv3j-CHrkOGxHxhofBreROrT9k7-GHknGN9YlFKv1idCfJKHBoShFYHigoDnZlVbi4C1FyZcVl5tguIHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=FzIGjR5ZcVj4-fSPTXfqUsR2Uzd_9_V6bchVLnf8s6BsKdo4JzZ82wvYlteTUVih-ewwtSDdY-VCyTe0qjJjMTbMkLmUteeg_rec-LD6zRUnFtFwFuINMUb98jKmgn8r_Bv2xUbXMqvBtYWVM8Ke1rv0qZP4yJOPQLDWDAkYwyo9GwgJm_nSJEqUbRIeQr_sZd-0vH0KFwIkNRUOnCyayrih63GbTb6xO25tEBtyG0M6Xkf-x6k_q5mhV02LDpCncB1TFbv3j-CHrkOGxHxhofBreROrT9k7-GHknGN9YlFKv1idCfJKHBoShFYHigoDnZlVbi4C1FyZcVl5tguIHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگی که علیه ایران راه انداختیم برای «
نجات دنیا
»ست!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72819" target="_blank">📅 11:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72818">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225b755540.mp4?token=Om5VZWNb5TJab02nIOlkIfibnLmFGfq5_fxOVpy9aoIADaq8RfKDlvI8GKPvSkRe-lyOJJP9qLQOg50J57r-YM2CXm4gng7jvvj1zAH6GxmV4e_sCTkRtZTrdqN8FNzO4cnV9NhXGQcLXTXFyMYjOglQe3UvaladcbwPezGJeZs-eAi_E3WxQPm0s4gnuliBmtbEaFMzCMxtj0bizkmMH_XdkH_2Ha_9NBEVEQX_NVZYHHQiBqZi1eD-n6i70jOA1Ce-EtozsYaVAaCAJFBmdmUWvIeinsmm4RTd5iH2r83mVsUclEgGsuMZD65XDiDAi1K5PTsHU1nQDvvUVi9_roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225b755540.mp4?token=Om5VZWNb5TJab02nIOlkIfibnLmFGfq5_fxOVpy9aoIADaq8RfKDlvI8GKPvSkRe-lyOJJP9qLQOg50J57r-YM2CXm4gng7jvvj1zAH6GxmV4e_sCTkRtZTrdqN8FNzO4cnV9NhXGQcLXTXFyMYjOglQe3UvaladcbwPezGJeZs-eAi_E3WxQPm0s4gnuliBmtbEaFMzCMxtj0bizkmMH_XdkH_2Ha_9NBEVEQX_NVZYHHQiBqZi1eD-n6i70jOA1Ce-EtozsYaVAaCAJFBmdmUWvIeinsmm4RTd5iH2r83mVsUclEgGsuMZD65XDiDAi1K5PTsHU1nQDvvUVi9_roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«راستی، داریم حسابی ایران رو می‌کوبیم، اینو که می‌دونید دیگه؟!
در هر صورت، این داستان خیلی زود جمع می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72818" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72817">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72817" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72817" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72816">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6dcySwT5UQ6rfnLqSLuwE8_FAd1rGxFZDCtlzvdxSsJaHjW6Tx5bbN_le0CpKoR9lwB-qC-XFWtqisjwEhy1EuOkboEP3lTithSFthTYPlGSfikRAxdkRzWiD2q0h9ZKwN5SDTGA6oNLPPvrNafxonihxexaPot58mQfcHtggO8D7hjzRXQsJs8GroJeTgJ72_mNGasnxyWNfRlH9nNjDUam_mqLOHrdg620WRP79ujRXVVQer6csAmKwofTEYWRzNHVe4tPNadnyZGzPXBvzzGvbDOzCd8-J1z7TY7AHiszy7oqGsYIxquLOLKKEsa2mYrVB1C6zNkKLr3GrwsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72816" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72815">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=nXzWZwhwCuonwIKmJBtCKRnIwLSOe77__-YEfOGvU6yixF5X1UT6f7-YUlEPe3bWPE2ebUlIEWRLIcJBB57a_o3hNXu2gv6-LFZRAO-UMGMC9XWrjjh6lQAwzv_zzF2X1vinMSM8Qq8IdYb4wiHDFMA2dadZLRzBkIUxtJ-lAI98V8KsKVqTno8geNKMfzOan1Hsmn5sjqpFqwbdoexL7ELWhaWEkLVftP8GmMRWTj-5y_y5B-Nw2aTMrA846fM8q-tfSWSZzuahPfg_G_-QNI_DUM_8PAXruX74OVUbEaNybL-4vsbXlQrEVGFOERPMw4CWK1u11hwwaOH1bWrHdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=nXzWZwhwCuonwIKmJBtCKRnIwLSOe77__-YEfOGvU6yixF5X1UT6f7-YUlEPe3bWPE2ebUlIEWRLIcJBB57a_o3hNXu2gv6-LFZRAO-UMGMC9XWrjjh6lQAwzv_zzF2X1vinMSM8Qq8IdYb4wiHDFMA2dadZLRzBkIUxtJ-lAI98V8KsKVqTno8geNKMfzOan1Hsmn5sjqpFqwbdoexL7ELWhaWEkLVftP8GmMRWTj-5y_y5B-Nw2aTMrA846fM8q-tfSWSZzuahPfg_G_-QNI_DUM_8PAXruX74OVUbEaNybL-4vsbXlQrEVGFOERPMw4CWK1u11hwwaOH1bWrHdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش چشم: اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72815" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72814">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=RUX1Y12ZPGAMnl1EKhaekgvpfHX0ReSVfBXyoFtwrp2YlVJxnHIMqeF0cpPBHrxcHGkmlBgd26kBctO84Kl4_owgGATZb53anyQLjren64mZTsoZWOBy0jm5gW-f0sw37iYZxaMu5dFeE6aZ001GnWeVvesus32O7BH3IeeBCikNnQPoIzuTaUNM8HlRS1eQXGCksVtbtp8OJYj-JHakDmd48HJwPrfQXil01OFB5ducJPZFx2OXZFpITObkHUjBsKd3zF0esEb-MqRF0Aif1vOIErLg6A4xZj_2yD9PZCpGvVMwpgDwovRiuB6-d11tFzsikGdJiH6lV1fu95UPPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=RUX1Y12ZPGAMnl1EKhaekgvpfHX0ReSVfBXyoFtwrp2YlVJxnHIMqeF0cpPBHrxcHGkmlBgd26kBctO84Kl4_owgGATZb53anyQLjren64mZTsoZWOBy0jm5gW-f0sw37iYZxaMu5dFeE6aZ001GnWeVvesus32O7BH3IeeBCikNnQPoIzuTaUNM8HlRS1eQXGCksVtbtp8OJYj-JHakDmd48HJwPrfQXil01OFB5ducJPZFx2OXZFpITObkHUjBsKd3zF0esEb-MqRF0Aif1vOIErLg6A4xZj_2yD9PZCpGvVMwpgDwovRiuB6-d11tFzsikGdJiH6lV1fu95UPPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز ترسناک‌تر میشه، یه پدر برای اینکه پسر 3 ساله‌اش رو تنبیه کنه، یه بسته مداد رنگی 24 تایی رو فرو کرده توی باسنش!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72814" target="_blank">📅 10:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72813">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=iBwSzykFVZFUbDhUCB6YYZmZY_9B-Dii5nRT1LGmlaXHsRKrso6rWCpZOnIIhngrHVZc3A6Sx1OT7rJl_GpTdhLhIPZLz0zM4BWP78Ir-S3dZH9oL4YB8kvFadZxJHjAS-RRZGx-5rUy9Udbt6hh8QmcPQ3BBuSTnGyjiPLqrQm0iF-AbXMFaRQs2pPH8bSLYipDEyndADekj0dko2CwW4enHuaoXfFLDWVuhZYFfYvj7_LUw2hdaGwnSyVZ_KiRIQ_J79c5tgW9IHFLC_REQDQ3wKj6ySocDSiTZb5dyTb6g9QW1vIC7lC0b-ZuS20rkvt2YEBtt2tFCKqsK7JnPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=iBwSzykFVZFUbDhUCB6YYZmZY_9B-Dii5nRT1LGmlaXHsRKrso6rWCpZOnIIhngrHVZc3A6Sx1OT7rJl_GpTdhLhIPZLz0zM4BWP78Ir-S3dZH9oL4YB8kvFadZxJHjAS-RRZGx-5rUy9Udbt6hh8QmcPQ3BBuSTnGyjiPLqrQm0iF-AbXMFaRQs2pPH8bSLYipDEyndADekj0dko2CwW4enHuaoXfFLDWVuhZYFfYvj7_LUw2hdaGwnSyVZ_KiRIQ_J79c5tgW9IHFLC_REQDQ3wKj6ySocDSiTZb5dyTb6g9QW1vIC7lC0b-ZuS20rkvt2YEBtt2tFCKqsK7JnPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا از لوکس ترین مدارس بالا شهر تهران که شهریه شون یک میلیارد تومنه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72813" target="_blank">📅 10:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72812">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=WXanNG_u_7h5304IG5EMHOR5T63FyG22oD_dESfCBD_Pg1N4CVNlS_N1e8rUPchA68CD4QD2D-WZ9Se3YMLub736081U3UUH2sUjff7IDrLj0avaLGIOt2XE2VAVcT86BtQl-RmXkeyiL0xNS3-EZqZ-8kPLn9xgyU-PH6iNVzjh7Fzki25HFWjlA857ld1REq_Q-v3I_VigbUdzQpKg5bwp2HpeU6Iwgz0Zz45P4WmaFYAQLsQs_wH0wzMnUU85rfMbmO6WfqrGfe9XrRvuxZK5XkUYTAr58Y6Ih4IuefdVzeN1-qL1XLz1Wk_1Ux0aD8JlO4jq7yV_Fag1-UkY7ApVDFXrRxQVvgFfof3UI-evwVIy_qSzFW09zyxhpd_EGwcwntNmohAdDqe63k45pkljogASZx_eiHAVksRrr1dD7Zkxo22mJY2irTEnU1xQ7XBzNWO5z7mlgXJt-QoPERv9XtzDpO4LQHY5Yp0xApC8vjCwVCzczt6boMQPXeOeHnWL3V2C4nbIso012RB4LnzFLrqmDEQt-B49AGJbS3cTCU0XjGnEF8wAqiNASpgZ44Jmt1ZE6op2A1o1mwZmdUvLSMmVQcUc75BnXnMifSjD_54RxoF8lyOoM2CNAFn_tbtuyyYJnjJ5bj6goLmUQfK3RrobGr9mgyhgvINgLGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=WXanNG_u_7h5304IG5EMHOR5T63FyG22oD_dESfCBD_Pg1N4CVNlS_N1e8rUPchA68CD4QD2D-WZ9Se3YMLub736081U3UUH2sUjff7IDrLj0avaLGIOt2XE2VAVcT86BtQl-RmXkeyiL0xNS3-EZqZ-8kPLn9xgyU-PH6iNVzjh7Fzki25HFWjlA857ld1REq_Q-v3I_VigbUdzQpKg5bwp2HpeU6Iwgz0Zz45P4WmaFYAQLsQs_wH0wzMnUU85rfMbmO6WfqrGfe9XrRvuxZK5XkUYTAr58Y6Ih4IuefdVzeN1-qL1XLz1Wk_1Ux0aD8JlO4jq7yV_Fag1-UkY7ApVDFXrRxQVvgFfof3UI-evwVIy_qSzFW09zyxhpd_EGwcwntNmohAdDqe63k45pkljogASZx_eiHAVksRrr1dD7Zkxo22mJY2irTEnU1xQ7XBzNWO5z7mlgXJt-QoPERv9XtzDpO4LQHY5Yp0xApC8vjCwVCzczt6boMQPXeOeHnWL3V2C4nbIso012RB4LnzFLrqmDEQt-B49AGJbS3cTCU0XjGnEF8wAqiNASpgZ44Jmt1ZE6op2A1o1mwZmdUvLSMmVQcUc75BnXnMifSjD_54RxoF8lyOoM2CNAFn_tbtuyyYJnjJ5bj6goLmUQfK3RrobGr9mgyhgvINgLGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: خبر داری دلار شده ۲۷٠ تومن؟
یه خانم تو تجمعات: اره ولی ما بخاطر وطنمون اومدیم، اگه ما نبودیم دلار حتی گرون ترم میشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72812" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72811">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=h5YRHKdmFdWLojZzhZK82gSu6C7arFwTfMF7jAQbReGweShm_Qshnglyy3yKoJq42YbEdPuucqCu_8REQeIeD4rfiEKdFIAcAo-Ma37XczF6gyBE2c_VXHu-rEWpoI5UlG8b8cRHs_szTMNeEjJDtl_mm9rLpuUN3jqHZKRSBMJ9K9QuERsarO9iWIqKINEKfFauu2CpdQokV_Ne63iaZihSL9R9dvvGEgYuSh41GG3cc7YJXPHcaxpyY76JofU0OO4U8tV6vbKlWiUz1gVqQB9VNTJq3byr-mY2sHeduep1mVRTy5fAT7PbqEXRdiHuWESEt2aNpFErbUDfpXD6Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=h5YRHKdmFdWLojZzhZK82gSu6C7arFwTfMF7jAQbReGweShm_Qshnglyy3yKoJq42YbEdPuucqCu_8REQeIeD4rfiEKdFIAcAo-Ma37XczF6gyBE2c_VXHu-rEWpoI5UlG8b8cRHs_szTMNeEjJDtl_mm9rLpuUN3jqHZKRSBMJ9K9QuERsarO9iWIqKINEKfFauu2CpdQokV_Ne63iaZihSL9R9dvvGEgYuSh41GG3cc7YJXPHcaxpyY76JofU0OO4U8tV6vbKlWiUz1gVqQB9VNTJq3byr-mY2sHeduep1mVRTy5fAT7PbqEXRdiHuWESEt2aNpFErbUDfpXD6Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آجرلو عضو تیم مذاکره‌کننده:
بابا بالاخره یه جایی باید قبول کنیم یه‌سری از این تحلیل‌ها اشتباه از آب دراومده!
هرکی نظر متفاوتی داشت رو «خائن» و «وا داده» خطاب نکنید؛ وقتی می‌گفتید ادامه جنگ این‌طور میشه، اسنپ‌بک هیچ اثر اقتصادی نداره، نفت میره روی ۱۵۰ دلار یا با شکست ترامپ در انتخابات کنگره همه‌چیز تغییر می‌کنه، باید امروز جواب همون تحلیل‌ها رو بدید.
اینکه بگیم «ترامپ انتخابات کنگره رو ببازه، دموکرات‌ها جلوشو می‌گیرن» هم خیلی ساده‌انگارانه‌ست.
بین انتخابات تا شروع کنگره جدید چند ماه فاصله هست و رئیس‌جمهور آمریکا هم قدرت زیادی داره و می‌تونه سیاست‌هاشو دنبال کنه.
خلاصه اینکه تحلیل غلط، تحلیل غلطه؛ فرقی هم نمی‌کنه از طرف چه کسی گفته شده باشه. به‌جای توجیه و فحش دادن به بقیه، بهتره بعضی‌ها یک‌بار هم بابت پیش‌بینی‌های اشتباهشون پاسخگو باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72811" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72810">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72810" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72809">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObRW0i_JpImxEe_9RNr0X57PSMNK3ZF9QeiQBU4-GEUvmkKLSPgCjVyvk2F0HMv7v7XAdQvxyCtLTijbOj15rYfdeNC7ESkzH4x0cEaTbGnSnnFs6w0aMM9XVMlorO0CFv-lDg3F-gpAW-96zaF7_xK8B2iIFXMrvOLNum84sIunLFjgyf7fknag07NYv5dClJWQ6PVp2K0hHStCy5rsprV7kN94owjS8rFiVJunA0c58IVt6PZXIxCi6Q7NpicMohOMOuatOpAIIt-6T3rz6ftqCPwZg1LlZPKjZMF4VrtpA3ysDWxG5WbsWhZDNDO58KaF9lErhgoPm9ZWxFtVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72809" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72808">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=F3rdfB4LIkJ6iy4eKTTyS6Yegt45XoJsMmb-15zF0nUoOlhyTAz4VlV4WAOIL0-3Tph0-Pr9-aQqSc-FxxtMh2RZOrX_FSnyHiSfDmU_TkiTpYwCuXgJ5_ag-dGAcsk0D_Ejk-bHEmpjm8nTNXEnmdPMNu_ohumSlTCHybJGTZ0jKtDaa41dsl3xPCwCGMmGe1Y1Sgd63qWBt8sqSizcMxeZL5senQj6lHmA-r6CNVD5wULrWEmVT4B8UYwdzJx2497mdrfGzeOgSATtxzdgjRsoW7Gxj4Z9xQ9LC9Vyhn4keua5_t0Z5C2S0TcktJkfgeGHv7Q-RB-GXKzVbHE0KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=F3rdfB4LIkJ6iy4eKTTyS6Yegt45XoJsMmb-15zF0nUoOlhyTAz4VlV4WAOIL0-3Tph0-Pr9-aQqSc-FxxtMh2RZOrX_FSnyHiSfDmU_TkiTpYwCuXgJ5_ag-dGAcsk0D_Ejk-bHEmpjm8nTNXEnmdPMNu_ohumSlTCHybJGTZ0jKtDaa41dsl3xPCwCGMmGe1Y1Sgd63qWBt8sqSizcMxeZL5senQj6lHmA-r6CNVD5wULrWEmVT4B8UYwdzJx2497mdrfGzeOgSATtxzdgjRsoW7Gxj4Z9xQ9LC9Vyhn4keua5_t0Z5C2S0TcktJkfgeGHv7Q-RB-GXKzVbHE0KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئوها از شهر طاعون زده شلخوف در روسیه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72808" target="_blank">📅 01:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72807">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=qgSlUycjX1B2B6dVfE98wjr_dXFEC25jTKiTfEWUaMoDZv6X2gjZ8o4Utcj_cDbRNjboSNNlMyqqXnv_fKKL1hiNDYDZE_oCkH5j4-J5etMkPHbYLTRmxOfuA4faJpcDmpDMn_aHtg6dmG2l9ggWwT41p1W-Nq2oKzYqUFGUkWKqYkzoDXgqSK9aG6x7LRS_qQxa4KgsuWVIJPB9u9y0cT8LSwSJlCnlExg-wt60tDZyt6k0NvhZ7Cr4d6JldkxLOcQcQHnuqt9_03s8uk0nWihAQb6ivBhNABv0HfRDZ9fjSvDwuDjsgMZXTcZ4nmmHsrelyQ2vYa1TmL9RVFE9ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=qgSlUycjX1B2B6dVfE98wjr_dXFEC25jTKiTfEWUaMoDZv6X2gjZ8o4Utcj_cDbRNjboSNNlMyqqXnv_fKKL1hiNDYDZE_oCkH5j4-J5etMkPHbYLTRmxOfuA4faJpcDmpDMn_aHtg6dmG2l9ggWwT41p1W-Nq2oKzYqUFGUkWKqYkzoDXgqSK9aG6x7LRS_qQxa4KgsuWVIJPB9u9y0cT8LSwSJlCnlExg-wt60tDZyt6k0NvhZ7Cr4d6JldkxLOcQcQHnuqt9_03s8uk0nWihAQb6ivBhNABv0HfRDZ9fjSvDwuDjsgMZXTcZ4nmmHsrelyQ2vYa1TmL9RVFE9ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پشم ریزونی که ارتش یمن منتشر کرده که دارن با ماشین، حوثی‌هایی رو که در کنار ساحل گرفتار شدن و در حال مقاومتن رو زیر میگیرن و له میکنن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72807" target="_blank">📅 01:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72806">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e493def7.mp4?token=BdewcSgxVDp7xVc_7kxwbxVDYfH_UbbSWFC49GN5ZSEIMrkFqb03pVHOC7BZtBqma2QPvyMw89CcOZ5xs8eyovAnmsFg7tk9XPE3J-qk9hhH84tTbM0x8fC2B3iQPFBFUq31flD7ajp3cpGMHnBPXX49hQhnnS-NpzXVz9aZ_VijvH8LaukIKst1ZuexBoBLwfHYt2-gms0VDri-Q72s3Tx_-PCQoD9ZDD4YTT7Z_o-SBjB639SdWNL76fDtfWz1XDy7h_jK4sq4cSQ8_S0P46Ea9urKBAhsTy8QY9UMJftkWq-g_VJDxm_mQxLXnb2t_wuwUmb1x6uExuQgDw1yyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e493def7.mp4?token=BdewcSgxVDp7xVc_7kxwbxVDYfH_UbbSWFC49GN5ZSEIMrkFqb03pVHOC7BZtBqma2QPvyMw89CcOZ5xs8eyovAnmsFg7tk9XPE3J-qk9hhH84tTbM0x8fC2B3iQPFBFUq31flD7ajp3cpGMHnBPXX49hQhnnS-NpzXVz9aZ_VijvH8LaukIKst1ZuexBoBLwfHYt2-gms0VDri-Q72s3Tx_-PCQoD9ZDD4YTT7Z_o-SBjB639SdWNL76fDtfWz1XDy7h_jK4sq4cSQ8_S0P46Ea9urKBAhsTy8QY9UMJftkWq-g_VJDxm_mQxLXnb2t_wuwUmb1x6uExuQgDw1yyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان سخنرانی حسین رحیمی، رییس پلیس امنیت اقتصادی، درباره افزایش قیمت دلار، برق محل برگزاری سخنرانی قطع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72806" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72805">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-t1HwpGxWNON-VRAXfqbXp3n6wd--9Jji_g3BSjUVyN9shZm5sk3ocJrNLWRk1qW6pEGDclPT8Nbj7GFLNg9LiogYOpmbRqGQ_d96Ih0FkLuBqmduOG55gyZwcVnPEZmKVSvwIdZ5YepMg_A-RWYKcdJwe1ioRSRPGbl1JQi4q0ZDqmBlE67OzP_p-vci82hzi_MMW0MRSr2xgO1MvPjz5EzfP7Kj2AiNJlJxwNmXpEoLPYPSX3LSu-VibnQS_BEjv9Gg4nk_33HbYRBqStuqNt-WdmASEzU1WTvYcsY0DnvxH7KoK-QJGmc_lQMINy2oQ0py5WolDtVyG9RZ-lnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت درباره ایران:
«عملیات طرد اقتصادی» نتیجه داده؛ ارزش ریال به پایین‌ترین سطح تاریخی رسیده، ایران ماه گذشته هیچ نفت خامی برای بارگیری روی نفتکش‌ها نداشته و حتی یکی از مقام‌های ارشد امنیتی ایران هم گفته کشور در یکی از سخت‌ترین دوره‌های تاریخش قرار گرفته.
حکومت ایران در حالی مردم خودش را تحت فشار و رنج قرار می‌دهد که منابعش را صرف حمایت از تروریسم می‌کند و عملیات طرد اقتصادی تا زمانی که جمهوری اسلامی از تأمین مالی تروریسم و ساخت سلاح هسته‌ای دست نکشد، متوقف نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72805" target="_blank">📅 00:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72804">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=d7nHpcsHWYDgeyDJ1A8iEnfKznSEXl8SdtOPaD4vQfHF-Ip1alnuk9pS4F92sBZAyA5Un7GqE88xchWv-6DYlPcwLhiX-hy0VoSYi7D1ZfLqlqNQjmcU7HZDDz6Hmqxsgqq227RMByBm48YAHtqAe3wyOJStkVMm5epR5sPSrrnw5u6xtzOQwahHn3vY9NdPAi3rPzEsnA8RDr8NaYgNi_2MpzQlgkX_63BBSo0xSqU7MilFkqxqaSoeLAP1WT2WOlqnB_K4s_dr_CAWyjBMP8XtBpRPBIus6PoQuBhuzlij9oPbxRyQzhwvXw_Z-ktlrBLI0GO2EsdU6nC7Uo2rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=d7nHpcsHWYDgeyDJ1A8iEnfKznSEXl8SdtOPaD4vQfHF-Ip1alnuk9pS4F92sBZAyA5Un7GqE88xchWv-6DYlPcwLhiX-hy0VoSYi7D1ZfLqlqNQjmcU7HZDDz6Hmqxsgqq227RMByBm48YAHtqAe3wyOJStkVMm5epR5sPSrrnw5u6xtzOQwahHn3vY9NdPAi3rPzEsnA8RDr8NaYgNi_2MpzQlgkX_63BBSo0xSqU7MilFkqxqaSoeLAP1WT2WOlqnB_K4s_dr_CAWyjBMP8XtBpRPBIus6PoQuBhuzlij9oPbxRyQzhwvXw_Z-ktlrBLI0GO2EsdU6nC7Uo2rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ:من فکر میکنم ایران مسئول حمله به هواپیمای «فلای دبی»است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72804" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72803">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:
ما مقادیر بی‌سابقه‌ای نفت از تنگه هرمز خارج می‌کنیم. یکی از مشکلاتی که داریم این است که پالایشگاه‌های روسیه به‌شدت هدف حمله قرار می‌گیرند.
این یک مشکل است، اما اوضاع به‌خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72803" target="_blank">📅 23:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72802">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سؤال: آیا نگران شیوع طاعون در روسیه هستید؟
ترامپ: این بیماری‌ای است که قبلاً قادر به مهار آن بودیم؛ اما به نحوی، آن میکروب‌ها قوی‌تر و هوشمندتر شده‌اند. آن‌ها مثل یک ارتش هستند. ما به روسیه کمک خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72802" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72801">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=PhdFcj6zOg2GwXReCLTFr6R_PZrBeoPTdryu5Lx50tzrTyjNTyqzv6WglzDff94xk_EtXtpW7N8QRcHTCUSt7hBRA2jpiFNYqhs09FG9yQl7OUvsr2nbHSy56BPu67hI_zYZaW5m9r3ZcV_plb-o4UlQHh5WvZ633sg0Ks54NPxUgQca662iNAXVS3gon_c-o0DC0qA6VqMcPUwKzkQ2l0ObPBQWAkqmYcDWy-IQ3Zqm_-TayPQIlVK-NFpDbGBk3sg7eXx6BibZ-qH7GL4aYHXhur1JLGhaVmMrdWRZy5x_zvah9BJdIsfoCNf9801jkR0jvrbLWlCLNuiss9V8SlzGthofHp97-F3rGfKqMO9uPnSMoOAv1IQk-nf4QGAlEb21JOO62eqhRjNQdajdjoe2G45N5tSXeT7K2Z1wHp-1NLaCSVJVkvLz6_MegPz1ZJn9035m-bgBFkX8RLH_e2Vtvfqp2AfoyDUbD3AmEdVz9Kw4DxjrnClVOOO7dLWDZzImFeTzwEnk0kX-zSCfcaj1NWF0W5GyFGJU3oalQlipcsyjvQhdrjE60XjTsJP5WBZ9s3ELhWzbYfQ05Ih5jwIZNoeDD9_9_nalfxkaPwcu3Zwek5ZpzbMqVAJpO2ZxFLfEvWm7pIy3A2lmCXD-85SxduED_Lel7iIZ-y2c_M4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=PhdFcj6zOg2GwXReCLTFr6R_PZrBeoPTdryu5Lx50tzrTyjNTyqzv6WglzDff94xk_EtXtpW7N8QRcHTCUSt7hBRA2jpiFNYqhs09FG9yQl7OUvsr2nbHSy56BPu67hI_zYZaW5m9r3ZcV_plb-o4UlQHh5WvZ633sg0Ks54NPxUgQca662iNAXVS3gon_c-o0DC0qA6VqMcPUwKzkQ2l0ObPBQWAkqmYcDWy-IQ3Zqm_-TayPQIlVK-NFpDbGBk3sg7eXx6BibZ-qH7GL4aYHXhur1JLGhaVmMrdWRZy5x_zvah9BJdIsfoCNf9801jkR0jvrbLWlCLNuiss9V8SlzGthofHp97-F3rGfKqMO9uPnSMoOAv1IQk-nf4QGAlEb21JOO62eqhRjNQdajdjoe2G45N5tSXeT7K2Z1wHp-1NLaCSVJVkvLz6_MegPz1ZJn9035m-bgBFkX8RLH_e2Vtvfqp2AfoyDUbD3AmEdVz9Kw4DxjrnClVOOO7dLWDZzImFeTzwEnk0kX-zSCfcaj1NWF0W5GyFGJU3oalQlipcsyjvQhdrjE60XjTsJP5WBZ9s3ELhWzbYfQ05Ih5jwIZNoeDD9_9_nalfxkaPwcu3Zwek5ZpzbMqVAJpO2ZxFLfEvWm7pIy3A2lmCXD-85SxduED_Lel7iIZ-y2c_M4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آن چه تهدیدی بود که باعث شد آن هواپیماها را از بریتانیا خارج کنید؟
ترامپ: احتمال وجود تهدیدی را می‌دادیم؛ خب چرا باید آن‌ها را آنجا نگه می‌داشتم؟ با تهدیدی مواجه بودیم. ما کسانی را که آن تهدید را مطرح کردند، می‌شناسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72801" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72800">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=FSnOzS-KXGgl-Jzfp2OI14E98WUyJClk-jOYKcg8s1QMl9xgNJWYq0gkXyGC1JikL_RmJ31E21-p1uP41yXQX7LyImFCh44wrNBAV5e0x4f0WI2hOJgV7ClWJMIxsLqNZ-Tlj2a96zAp9ZK2964nY2vqsMHit8G_mFKXosOfzXodPFOouq-Ym80OqgdsBztI5G84d2Q2zD1-KHwgTU7zjae56Gu0-IfrBGBTe-xvw5uYr0NG5NL5dOMmQe9Z0qbxZqPH0lGABx4OvzfllwQvSJyFaYj-I-HFpuqgLJQ-SgOUwCGS8et5Y2TZRufCGB732vhIFsJmymw8lpLEFx2LVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=FSnOzS-KXGgl-Jzfp2OI14E98WUyJClk-jOYKcg8s1QMl9xgNJWYq0gkXyGC1JikL_RmJ31E21-p1uP41yXQX7LyImFCh44wrNBAV5e0x4f0WI2hOJgV7ClWJMIxsLqNZ-Tlj2a96zAp9ZK2964nY2vqsMHit8G_mFKXosOfzXodPFOouq-Ym80OqgdsBztI5G84d2Q2zD1-KHwgTU7zjae56Gu0-IfrBGBTe-xvw5uYr0NG5NL5dOMmQe9Z0qbxZqPH0lGABx4OvzfllwQvSJyFaYj-I-HFpuqgLJQ-SgOUwCGS8et5Y2TZRufCGB732vhIFsJmymw8lpLEFx2LVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا فکر می‌کنید این خطر وجود دارد که ایران پهپادهای رزمی وارد بریتانیا کرده باشد؟
ترامپ: نمی‌توانم چنین چیزی به شما بگویم. اگر دست به چنین کاری زده باشند، بهای سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72800" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=Abb4u3Otj8e8pDU6aX4ToYC0g3oPA0B1sGONczHmABeKIE3oRg9bxCuXtIsWBTFRVjAjkAgyZg5bC4bSHt4vfb5BOX3JmobvQ0Xm07nfdGdw9bnjcKIo6i1STqMspDOFATBYt3qpzIdqB1NkVMTe8mDLV-_3pGLpcab-9Ku2Y268tcNIZoBDyGS3g-I-d4dMBudgS5V_DOdoB_tc07TgdBWGOc39Xf_5gtHdbFLnHw9o8kdUvEM-aOJ-bXPN_KqAE8-nyv7k5k5BKHz1_Qe1JYIK-dvD3xASlPuQIKDZEVmVwnUJ58vGXgW_E_stCCJ2LDYcAsmKuQwBKdblN-B2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=Abb4u3Otj8e8pDU6aX4ToYC0g3oPA0B1sGONczHmABeKIE3oRg9bxCuXtIsWBTFRVjAjkAgyZg5bC4bSHt4vfb5BOX3JmobvQ0Xm07nfdGdw9bnjcKIo6i1STqMspDOFATBYt3qpzIdqB1NkVMTe8mDLV-_3pGLpcab-9Ku2Y268tcNIZoBDyGS3g-I-d4dMBudgS5V_DOdoB_tc07TgdBWGOc39Xf_5gtHdbFLnHw9o8kdUvEM-aOJ-bXPN_KqAE8-nyv7k5k5BKHz1_Qe1JYIK-dvD3xASlPuQIKDZEVmVwnUJ58vGXgW_E_stCCJ2LDYcAsmKuQwBKdblN-B2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:نظر شما درباره ضدحمله عربستان و یمن علیه حوثی‌ها چیست؟
ترامپ: همه چیز به خوبی پیش خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72799" target="_blank">📅 23:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=isT0PfL1A7L_zdebOGCN19o2lQeOf8zPTySWYzxj0Xj1LcJj7e7uh6529RxX6cyr5aLsY-v22G2r4e4-iG1JFenXp-YZ1L75-yLFERdxAVTZ9CNm9rPaMMBt9f7jvoMBiM-NECUsIGU6wbhkTHODLeQYSYTSMaPO4GB23GmTYsVwAm4OVsmZwFrNQVrB7g3yitAptf1r6ectwiefrC-PiurxWLm0JgUfn_obyduL5mleh3KcGGW5LsBK_4cTiQGlOXeldg7n8BSWOzQq2E132YUA3ygnHbYlLKelL0eI6kw2OiSKpTtjbCt2UjboBB6vYFkqsut-xJCDyWRM9Fc6TDPPY_a8WOvgA_TdQ6L4-hJMpb31otzlp9W0eQBKzHrZAvb1zt2OtrWC60mn-sb6OH8mbGLBM0vlGDd6RZrPUwQyRrMnWvwUFH9G0i31FYsVFP8teoBhyCE8FCXDdGaPTyNdQgcSTfUE0up4TmODiPjj7WvqqXPEYQon_o_LTvQhFcNt05g7dE3hmTgIKGvZhuJoUHyyVbdjKENf2y5hWCMmmRvM4SDX-F3d1Fv67cfPZDyleY7lQt1TNuu5WllCQd-KZg1d_uOkgp9t_Q4l_33FzvWX3OaoZy1DVbo8jracC6gahRuJCV0mqEOuyFoSQtLP2aLHQiHxh3tECO3W3Fc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=isT0PfL1A7L_zdebOGCN19o2lQeOf8zPTySWYzxj0Xj1LcJj7e7uh6529RxX6cyr5aLsY-v22G2r4e4-iG1JFenXp-YZ1L75-yLFERdxAVTZ9CNm9rPaMMBt9f7jvoMBiM-NECUsIGU6wbhkTHODLeQYSYTSMaPO4GB23GmTYsVwAm4OVsmZwFrNQVrB7g3yitAptf1r6ectwiefrC-PiurxWLm0JgUfn_obyduL5mleh3KcGGW5LsBK_4cTiQGlOXeldg7n8BSWOzQq2E132YUA3ygnHbYlLKelL0eI6kw2OiSKpTtjbCt2UjboBB6vYFkqsut-xJCDyWRM9Fc6TDPPY_a8WOvgA_TdQ6L4-hJMpb31otzlp9W0eQBKzHrZAvb1zt2OtrWC60mn-sb6OH8mbGLBM0vlGDd6RZrPUwQyRrMnWvwUFH9G0i31FYsVFP8teoBhyCE8FCXDdGaPTyNdQgcSTfUE0up4TmODiPjj7WvqqXPEYQon_o_LTvQhFcNt05g7dE3hmTgIKGvZhuJoUHyyVbdjKENf2y5hWCMmmRvM4SDX-F3d1Fv67cfPZDyleY7lQt1TNuu5WllCQd-KZg1d_uOkgp9t_Q4l_33FzvWX3OaoZy1DVbo8jracC6gahRuJCV0mqEOuyFoSQtLP2aLHQiHxh3tECO3W3Fc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا تهدید خاصی وجود داشت که باعث شد آن بمب‌افکن‌ها را از بریتانیا فراخوانید؟
ترامپ: بله، فکر می‌کنم بتوان چنین گفت. پرواز آن‌ها تصادفی نبود؛ تهدیدهایی در کار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72798" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72797">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449cc78904.mp4?token=vSR6BJa6ReeXCfgMIkQXnjK-xvXk6i4naMMDLCrQ_GjFfA9WpgUapld0P-X0M__4XpU0_nfTX6ZXHwSVm_HOJ28A6N9CQ2F54-D63M5qX8JLLN-IPcA_tpjYwlJGlYulCtvQNhqBFAwOh56lsYn5WnumYPgCZjfPHx7Y084MYZmqzRorHQNDv7KZxaOir0VU9r8J4TCSqSaLGhTlOby_5df7S4JwFnoZ0eBo71bhQn9aleXOjglv8y8uZLdWl_ujJ2Y3T5tzXBJYp7qfFCJ3ybqI8aLc98Ao67y2mmEFhcrXHPFrltXDJCqgDz4CyftXdfBbX5YRO9J58DFXsDRhZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449cc78904.mp4?token=vSR6BJa6ReeXCfgMIkQXnjK-xvXk6i4naMMDLCrQ_GjFfA9WpgUapld0P-X0M__4XpU0_nfTX6ZXHwSVm_HOJ28A6N9CQ2F54-D63M5qX8JLLN-IPcA_tpjYwlJGlYulCtvQNhqBFAwOh56lsYn5WnumYPgCZjfPHx7Y084MYZmqzRorHQNDv7KZxaOir0VU9r8J4TCSqSaLGhTlOby_5df7S4JwFnoZ0eBo71bhQn9aleXOjglv8y8uZLdWl_ujJ2Y3T5tzXBJYp7qfFCJ3ybqI8aLc98Ao67y2mmEFhcrXHPFrltXDJCqgDz4CyftXdfBbX5YRO9J58DFXsDRhZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در میدان آزادی (میان اقبال) سنندج از این کوماندو‌ها رونمایی کردن برای مردم! امیدوارم این فیلم رو هیچ وقت ترامپ نبینه چون بعدش قراره دیگه شبا آرامش نداشته باشه
😂
یه ساختمون چند طبقه رو ۱ دقیقه طول کشید تا برسن پایینش! از پله‌ها میومدن زودتر می‌رسیدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72797" target="_blank">📅 23:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72796">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=FZkg1tcA-TCRNS-g7APHlNiU82DLO_8AdXGDNQvFMUd4AQx03bQmLwZYoQF8J8TCvf_MtE0m-AEWFbuyE3Xg09YcaEYxU81shIs0MAkbgtCJPKJU5gQZFJ9ESQO202_fSV5QN4hA4IGPtlHP1CGf7MPj_2KVmYM4ajK5yfUuSEzJsZrgf77UBoGfmRG1jDeQWDpd46bjnhgYR-eD07CYyxc1NmhQ5_5_Kg-cgIhpxRrGJcfwuz7RCFGBtaJIsZcU4tXa7qj36onWjAExihqztS--llrwHOEtATp-n6Cb9S9apwRQsrA5zN0FayDZwspQX-0iurt1AN5AfqwkAX2sGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=FZkg1tcA-TCRNS-g7APHlNiU82DLO_8AdXGDNQvFMUd4AQx03bQmLwZYoQF8J8TCvf_MtE0m-AEWFbuyE3Xg09YcaEYxU81shIs0MAkbgtCJPKJU5gQZFJ9ESQO202_fSV5QN4hA4IGPtlHP1CGf7MPj_2KVmYM4ajK5yfUuSEzJsZrgf77UBoGfmRG1jDeQWDpd46bjnhgYR-eD07CYyxc1NmhQ5_5_Kg-cgIhpxRrGJcfwuz7RCFGBtaJIsZcU4tXa7qj36onWjAExihqztS--llrwHOEtATp-n6Cb9S9apwRQsrA5zN0FayDZwspQX-0iurt1AN5AfqwkAX2sGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شامگاه شنبه ۱۱مهر۱۴۰۵؛لحظه برخورد صاعقه با برج میلاد:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72796" target="_blank">📅 22:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72795">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=DON5oESfCyNtg67O3VdtkeN-kEKIvEU6go4X4Wo4SJ46JiiDQC7kkJQzoXButapngE01KFveRAa5FANXrW-wiPQza0h8ZcPLJqlceOBj3b0HzFFhAvIbW7WVhlWt-Vqxm6EyJKSOZCpNAdinBVOU8ERXD2kSRjrjjiwzSmd1m3UqGTc3NMkVcxM243FLTc8w8yfpA-miE_Xboo4yTmDgTllRa7qy3-9qvkEJF4rpBeq1WL6OSdtYdmUdf6t5sMG4I9Ss-WZ2mjfyhJXqOoIiwY91VW6ZAjzwoPxDY6IUXgnRgTzONlS-G6hrAGstJPGXU_beJggwUdo5zFUWyJ0Q7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=DON5oESfCyNtg67O3VdtkeN-kEKIvEU6go4X4Wo4SJ46JiiDQC7kkJQzoXButapngE01KFveRAa5FANXrW-wiPQza0h8ZcPLJqlceOBj3b0HzFFhAvIbW7WVhlWt-Vqxm6EyJKSOZCpNAdinBVOU8ERXD2kSRjrjjiwzSmd1m3UqGTc3NMkVcxM243FLTc8w8yfpA-miE_Xboo4yTmDgTllRa7qy3-9qvkEJF4rpBeq1WL6OSdtYdmUdf6t5sMG4I9Ss-WZ2mjfyhJXqOoIiwY91VW6ZAjzwoPxDY6IUXgnRgTzONlS-G6hrAGstJPGXU_beJggwUdo5zFUWyJ0Q7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: اخراج ما از آمریکا مثل اخراج تیم برنده از المپیکه!
پس خبر درست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72795" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=Y_2Rh7lQWMQG72-dEvwaDfvpgy3QdO3BhL-KQAeYzzI4AYIv2MsL02LTk8LhFieuIr6Ldh6uZ0rdQvEuHx4qbzjtUAVLMyu0f8P_CPcFW_HesM-Rf4uSeGWkNEud7ThtM0A-Ry7Iydg-Ng2YEFB66A6nA91uT5MLZLvHQhzQvkaOxQ3Rd_3uQnpKZnpI-Beelnoqbi_KRcQyuoS1SwHEzqgXDSJGrlmrg_wcMqvnAaKgnIR-2JCB_OpbhZxo3SmT7PfCwag6XUFicr5YAB5HOf_xcE708vJH3GD-GF6VSoxFdlC3Me1dhf7Ax4ijoBbcq6JnL6QZ2BsNurg3rh00dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=Y_2Rh7lQWMQG72-dEvwaDfvpgy3QdO3BhL-KQAeYzzI4AYIv2MsL02LTk8LhFieuIr6Ldh6uZ0rdQvEuHx4qbzjtUAVLMyu0f8P_CPcFW_HesM-Rf4uSeGWkNEud7ThtM0A-Ry7Iydg-Ng2YEFB66A6nA91uT5MLZLvHQhzQvkaOxQ3Rd_3uQnpKZnpI-Beelnoqbi_KRcQyuoS1SwHEzqgXDSJGrlmrg_wcMqvnAaKgnIR-2JCB_OpbhZxo3SmT7PfCwag6XUFicr5YAB5HOf_xcE708vJH3GD-GF6VSoxFdlC3Me1dhf7Ax4ijoBbcq6JnL6QZ2BsNurg3rh00dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آقای آتش‌نشان در مورد ساخت پلاک مشخصات برای دانش آموزان:
امروز رفتم یه دبیرستان دخترانه برای کنترل مسائل امنیتی بین حرفامون با مسئولین مدرسه متوجه شدم که دارن برای دانش آموزان پلاک مشخصات فردی درست میکنن مثل همونایی که زمان جنگ استفاده میشد؛
از این پلاک‌ها که زمان جنگ سربازها مینداختن دور گردنشون که اگه بر اثر بمب و موشک چهره‌شون دیگه قابل شناسایی نبود، از رو پلاک شخص رو تشخیص بدن..
وقتی پرسیدم برای چیه؟ گفتن نمیدونیم فقط از بالا دستور گرفتیم و مشخصات فردی دانش آموز رو دادیم تا براشون درست کنن!!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72794" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpnJDPVgeQKtCDYsldAgRO04bHUqzOsvv7NHuc34pMj_kOU8uui-sn-cnQT0wUwl3KIXvoG6l97XScojLnQ4HLg5iuFrNRp-Codltlueu_H5nmXfDMXP4rT8h4fsXAVPQfpqQY72rJq1WR_pNwp3wrZMJmqh7d6x-gftsf57K6q-xvzIlvIg6MgwfrikCNMyyxoMQQJNlvLBaAWeDGUzsmHlOKS4H6VYhmJ2TEfN5d8ByHdd0BLsbC6hO2V04AbzuPIm3Tgyug9zHbV6iM_FwWmedVCPtcKRXQW0g7wXD0m46mFEA918OKGSjtTjsWlUd2gHr2kP6uYGaYXHr4Ghjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
آنچه باعث افزایش قیمت بنزین می‌شود دیگر تنگه هرمز نیست — چرا که اکنون حجم بی‌سابقه‌ای از نفت (بشکه) تقریباً به‌صورت روزانه(از تنگه هرمز)عرضه می‌شود
.
بلکه مسئله «پالایشگاه‌ها»ست؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط «دموکرات‌های احمق» تعطیل می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72793" target="_blank">📅 20:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902f67b684.mp4?token=G1BVsI13vDnOiUODLmD_f3Lf9XOvYQ9Fko8sqLOdnXl8D14PS0WpkspcCSmq6DPFnMByjb3747KkVSVzKgI-6Swwrw0_7i1D3et_ayxTuN1-cm6yA6VTjeoEdrOyfvx927EjI8BFbpSlVNTRFuN2k4bZleH-K-Ue0b7xIkFjoTowQxB_EGar3pt9we7-wpbR8MaDXDuBiTnacAZtgTDDMLalLxK0mR5ryq8XATJrvwK34hoE3E9xFQq6AXxSLeTbAM_dtRFKlv5fvPU93uio2PS1RJf1mgXTZw_323T12lI2qmaTpI0dOHsSoyYOf7Bbojv1fdZ2NQgx0BxoEcxMTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902f67b684.mp4?token=G1BVsI13vDnOiUODLmD_f3Lf9XOvYQ9Fko8sqLOdnXl8D14PS0WpkspcCSmq6DPFnMByjb3747KkVSVzKgI-6Swwrw0_7i1D3et_ayxTuN1-cm6yA6VTjeoEdrOyfvx927EjI8BFbpSlVNTRFuN2k4bZleH-K-Ue0b7xIkFjoTowQxB_EGar3pt9we7-wpbR8MaDXDuBiTnacAZtgTDDMLalLxK0mR5ryq8XATJrvwK34hoE3E9xFQq6AXxSLeTbAM_dtRFKlv5fvPU93uio2PS1RJf1mgXTZw_323T12lI2qmaTpI0dOHsSoyYOf7Bbojv1fdZ2NQgx0BxoEcxMTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا توانایی خودشو توی بسکتبال هم نشون داد و تقریبا همه توپاشو سه امتیازی وارد سبد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72792" target="_blank">📅 20:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=j0bjkcf44jSRyiKN_A46O0C8pEaMITaQ3-0G1NBIYnfrFwY7yXDhYB4Xna9XbQTp7P1HfzEvLoxgiXkMRGWtDfXeBgcJT7b38w2Cxdd_uMBfcZw49qcgO8WlvZYZ6ZvJ491KCKubIzgUobGOOdgId057tAB3Spyg7LrlBzwKISs9Pkij9PB5lOxQsnR7sqyScV0i4GIroL_LcFXFyMzfNuURmTySb3wFnytWA2PUhc6IlEbarJReZINN325-udtdQDQYgG36LHyfPJulsOm99Tv_wkSHnx4Bs1OI2L7uJ1z6I_nPQqe0PbAln_uCsCpz9hEe0atNRmKQz73-E85g24h1cCkJhCb-O5E8_OYXRHafJCtmPCx3ljcVO_SvdEktLMx6Yr2m8fcsZ_8B04WVoEi0Jl11WF1tUEZlDM5UgBWVnwBUfnRK36I1jgM1HS5B7fAN1JY1PQeXaXk2kz_lgG7c5VFI2pShozG8szFV8AMZO2TkzPhQik64xdtfNy2LlmCXCtnIDyAZp4LWVj2x-lp_sOT6-UKigAhgyq7xfxFv32-G70jXcg7BxzTEkwdOTSBSOJ5Mptwf7TiAlS3zGT_dwonqzXqIDVtuGjsP1rOUKmZitcKzKziVdH-mrSXVqIEYVCMBR7eojb1W615QK9Qhvp3bk-7BHwX-0DsEmJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=j0bjkcf44jSRyiKN_A46O0C8pEaMITaQ3-0G1NBIYnfrFwY7yXDhYB4Xna9XbQTp7P1HfzEvLoxgiXkMRGWtDfXeBgcJT7b38w2Cxdd_uMBfcZw49qcgO8WlvZYZ6ZvJ491KCKubIzgUobGOOdgId057tAB3Spyg7LrlBzwKISs9Pkij9PB5lOxQsnR7sqyScV0i4GIroL_LcFXFyMzfNuURmTySb3wFnytWA2PUhc6IlEbarJReZINN325-udtdQDQYgG36LHyfPJulsOm99Tv_wkSHnx4Bs1OI2L7uJ1z6I_nPQqe0PbAln_uCsCpz9hEe0atNRmKQz73-E85g24h1cCkJhCb-O5E8_OYXRHafJCtmPCx3ljcVO_SvdEktLMx6Yr2m8fcsZ_8B04WVoEi0Jl11WF1tUEZlDM5UgBWVnwBUfnRK36I1jgM1HS5B7fAN1JY1PQeXaXk2kz_lgG7c5VFI2pShozG8szFV8AMZO2TkzPhQik64xdtfNy2LlmCXCtnIDyAZp4LWVj2x-lp_sOT6-UKigAhgyq7xfxFv32-G70jXcg7BxzTEkwdOTSBSOJ5Mptwf7TiAlS3zGT_dwonqzXqIDVtuGjsP1rOUKmZitcKzKziVdH-mrSXVqIEYVCMBR7eojb1W615QK9Qhvp3bk-7BHwX-0DsEmJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره خروج هر ۱۲ فروند بمب‌افکن «بی-۱» (B-1) از پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford):
آنچه در آنجا شاهد بودید، اقدام وزیر دفاع برای محافظت از نیروهای ما بر مبنای احتیاطی مضاعف بود.
ما با اطمینان نسبی معتقدیم که ایرانی‌ها در پی انجام همان کاری هستند که حکومت ایران طی ۴۹ سال گذشته انجام داده است؛ یعنی ارتکاب اقدامات تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر.
ما نهایت احتیاط را به خرج می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72791" target="_blank">📅 19:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_jUPP1iCHOdNUkWP11JfjSPmPpJCyrTHweaRUhk-v2fir81KEyKTNGN1w60nTG7C8byoYmjaDDMNQO6Ln-gMvEFzQu42hyf47qHNMWLz9W11gAuRjQFX7JVXQ7Rz66ZAJABO0lnYHQTFWxq5ymyhjkslrBhifA4RiEobWxgp4POKcXYZm78lUCqBpxJXdmMUbhi6_AHF73QCE3rnsAw7JZznpIsZoROP39UEs03P-M7fc7RILIz4rw-tU5Qa5q3xWtQxxmZhZkJ8qmlfpTi-jBPaxc5xgSCM-NlJH59nmZ__pRSA9GeZZ9ttH4ZYHveavUZEWZQhICnVurpFuoVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.
پوکت نخستین بندری است که این ناو از زمان ترک ایالات متحده در ماه مارس در آن پهلو می‌گیرد؛ قرار است کارکنان آن از ۴ تا ۹ اکتبر برای گشت‌وگذار، فعالیت‌های فرهنگی و برگزاری یک مسابقه فوتبال میان آمریکا و تایلند، در خشکی حضور یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72790" target="_blank">📅 19:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=oYmY4of1JIO5GM914_gZX7IBx-u7aNb8q9PMxru62ZZfysR7_pTJjiwBwbCKmVSmOPksGjNU_chZ3hHyhnW--KY4qJZAi1LU_-hwqj1hDl1ph3TANH2qtXuIo7JjL8NAYm2xAHSxF5f6K1P_EfMgUw6WGu0deIXSrEplKMsSjqyxrfVEteBWdyNF15X74xGGfkP-kYYw22XyjdvQ13D6qWWqSm78JHR9FWMO8nnF30Snh4NQhU8zhMSVNMQACzr-A2dkviejloEDuqU8dVVYAKFmE6mSs7E6Ksy9uJqzUDNdNR0GQx61wh8NCDiGZuKR5TdP1e1TnStEa4kdE5qL4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=oYmY4of1JIO5GM914_gZX7IBx-u7aNb8q9PMxru62ZZfysR7_pTJjiwBwbCKmVSmOPksGjNU_chZ3hHyhnW--KY4qJZAi1LU_-hwqj1hDl1ph3TANH2qtXuIo7JjL8NAYm2xAHSxF5f6K1P_EfMgUw6WGu0deIXSrEplKMsSjqyxrfVEteBWdyNF15X74xGGfkP-kYYw22XyjdvQ13D6qWWqSm78JHR9FWMO8nnF30Snh4NQhU8zhMSVNMQACzr-A2dkviejloEDuqU8dVVYAKFmE6mSs7E6Ksy9uJqzUDNdNR0GQx61wh8NCDiGZuKR5TdP1e1TnStEa4kdE5qL4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)  تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72789" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)
تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون از دست می‌ره (کنترل شهر مهم تعز همچنان به دست حوثی‌هاست)
#hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72788" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حوثی ها دو موشک را به سمت منطقه ای که تحت کنترل نیروهای دولتی یمن بود شلیک کردند.
در همین حال خبرنگار شبکه العربیه در حال آماده‌سازی برای پخش زنده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72787" target="_blank">📅 18:28 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
