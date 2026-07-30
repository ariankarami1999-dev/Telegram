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
<img src="https://cdn4.telesco.pe/file/MruG6VfXXKXN0vG0PKWya-0nhOpeCxgj2sXwYKm1pBksL6wc2hZ1naB2eQEhqBNn5zZj-1u313WjFkmNn1ndW_QaNYXUbsYd5di-LNAF6IJy56BS-IfO0hlYCb_WMP9Lp1tvpdmxHtd9yz63BULUsRSYS3KxvD4QNQwy7rc3XH8xH0mmYJ3yod9KfVFzVYnqwlCDDSUYgX3fk_pCxnIvoXWD1TqsCY-v161r4UfcIF3PblaVp0NKbtXdCLOX1BYd2o5MqxwIsbKWlqrQa3ojjMPOqT5vTy7Datw9GG9KMF9pa7P20s-U20OfOjrvA9QUS--8MBrf2zb7BkriMVB2Iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 434K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-20084">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری رویترز در گزارشی ادعا کرد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل طرحی را شامل پیشنهاد ترور هدفمند فرماندهان ارشد سپاه پاسداران و ارتش جمهوری اسلامی ایران به دونالد ترامپ ارائه کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/20084" target="_blank">📅 12:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20083">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی:
آخرین خواسته امیرحسین صفری از مادرش پیش از اجرای حکم اعدام این بود که به همه بگه ویدیویی که جمهوری اسلامی از اون منتشر کرده، اعتراف اجباری بوده و اون کسی رو نکشته.
@WarRoom</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/20083" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20082">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری رژیم : نتانیاهو به ترامپ پیشنهاد داده یه لایه دیگه از رهبران و‌ فرماندهان جمهوری اسلامی رو بزنند.
@WarRoom</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/20082" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20081">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx9mhQEwrIDg00-pK0sJF9e80OQX3HnkgGbMmu0-L67_s5ZMl381PcPpAMhO-WPssPta2_Z1D-HUOzZsvbx3GkA2CrRAR5EF_dyrWDge36-r8gBglml98zuOAoo8Np068DWuEvGWPqEtLXBPm8fyHBbSCGoRvdZEMNWKUHfzOc2YSc1MYZ3Leftq7px47nq12shMA6gYl1VpODcEDzyy-XyZgGrg8pWx1ckgr_4ugUHiUkCFPJjuTikYEocjojii9vl0wxdiFhu-ZkcN29eMV-XhF61Df88QfO_hkls2H_9G8U-CJ2SPwd7YYbfF8XLBhsfyjjyNxhqaNeJ7e3D1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۳ تا از کثافتهای رسما گی حشدالشعبی که در حمله عربستان کشته شدند (عکس رسمی)
همین افراد دی ماه در ایران قتلعام کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/20081" target="_blank">📅 11:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20080">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو به شبکه ABC:
حماس باید منحل شود و غزه باید از سلاح‌ها پاکسازی شود.
@WarRoom</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/20080" target="_blank">📅 11:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20079">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سپاه: متجاوز همین امروز تنبیه خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/20079" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20078">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت دفاع کویت : یک ساختمان متعلق به یک شرکت چینی در شمال کویت مورد حمله موشکی ایران قرار گرفته و منجر به کشته شدن یک کارگر و وارد شدن خسارات قابل توجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/20078" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20077">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سنتکام : در ساعت ۵:۳۰ صبح پنج‌شنبه ۳۰ ژوئیه به وقت تهران، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) با موفقیت یک موج سنگین از حملات را علیه ایران، در پاسخ به تلاش روز گذشته برای حمله موشکی به نیروهای آمریکایی، به پایان رساندند. دارایی‌ها و تجهیزات سنتکام…</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/20077" target="_blank">📅 10:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20076">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتانیاهو به ای‌بی‌سی: «رژیم ایران همیشه دروغ می‌گوید، تقلب می‌کند و با زمان بازی می‌کند»
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20076" target="_blank">📅 10:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20075">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5647d258de.mp4?token=V9CIRCM_SjxHOrDmyns3Ge1UXXzcEMYvepNjuwHrpTA8i_VrwHCZ9VcI547-3VtS4htJImmpfOU0t_w02CncnDLGojnv6M-XnROx5BcoIXeFxYenMEq1SGpVX8Z1VXNzQmUFWkVjjfAzNxQnrgv-OmaxIvG6rEtHJRWIsaGETF6Rrwf_OznsKzjYwm_s3fpE1g4gq4vti5yb4nitEIurNoq83-YDDWGJsP-DbB8z7nFKlUc_DdQbg72p3zrd_VL-8IYYwFRsjn6ol4x2HS9ZEy5xk62zE8hpEK3TK0Zz1HuFFG9jarBRRQBPi7Fwrh8lqICI1AiuWLDWbdTz3elmBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5647d258de.mp4?token=V9CIRCM_SjxHOrDmyns3Ge1UXXzcEMYvepNjuwHrpTA8i_VrwHCZ9VcI547-3VtS4htJImmpfOU0t_w02CncnDLGojnv6M-XnROx5BcoIXeFxYenMEq1SGpVX8Z1VXNzQmUFWkVjjfAzNxQnrgv-OmaxIvG6rEtHJRWIsaGETF6Rrwf_OznsKzjYwm_s3fpE1g4gq4vti5yb4nitEIurNoq83-YDDWGJsP-DbB8z7nFKlUc_DdQbg72p3zrd_VL-8IYYwFRsjn6ol4x2HS9ZEy5xk62zE8hpEK3TK0Zz1HuFFG9jarBRRQBPi7Fwrh8lqICI1AiuWLDWbdTz3elmBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به ای بی سی: بعد از پایان این جنگ، فکر نمی‌کنم تنگه هرمز اهرم قدرتمندی باشد، زیرا خطوط لوله انرژی را از تنگه به ​​دریای سرخ و از آنجا به اسرائیل و مدیترانه منتقل خواهند کرد.
ما می‌توانیم این گلوگاه را باز کنیم و این کار را خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20075" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3061f41fa2.mp4?token=tqBLxAuGaSabQBjdEcO741Y6aLO-7T2svYqFTwyx4IBF_0sVH2TCNuJxUHOy0asFmWX7lw_m9TZNswPHW3MVcY3QrH0SrNo4PprrADVdFbqb8PkjiMg1nLFCBA2pRaSBPGZzLNFwF3Cqs3zv_spDcSVO8937bniUog3uwnH7ctfXv-jG1pSUI95mH_X-OzlEOByQHr4nuQ3eirM00GRwB7p-OF3-uy00KpdsqWFum2THNO4DrpyXC36ah1dDGo9DDxIQncpn2deiGryXwIJG0DqWUDXi9tDtNSMer9ZP-81TCj7rkwyQcj1NcSVr5xcMBpIh5UqLyMkVYfdB3n1ZjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3061f41fa2.mp4?token=tqBLxAuGaSabQBjdEcO741Y6aLO-7T2svYqFTwyx4IBF_0sVH2TCNuJxUHOy0asFmWX7lw_m9TZNswPHW3MVcY3QrH0SrNo4PprrADVdFbqb8PkjiMg1nLFCBA2pRaSBPGZzLNFwF3Cqs3zv_spDcSVO8937bniUog3uwnH7ctfXv-jG1pSUI95mH_X-OzlEOByQHr4nuQ3eirM00GRwB7p-OF3-uy00KpdsqWFum2THNO4DrpyXC36ah1dDGo9DDxIQncpn2deiGryXwIJG0DqWUDXi9tDtNSMer9ZP-81TCj7rkwyQcj1NcSVr5xcMBpIh5UqLyMkVYfdB3n1ZjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری ای‌بی‌سی نیوز: وقتی در کاخ سفید با ترامپ ملاقات کردید، آیا سعی کردید او را متقاعد کنید که حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک کاریکاتور یا تصویر کارتونی است. این درست نیست.
ما در واقع هر سه احتمال را بررسی کردیم و فکر می‌کنم این کار را به صورت علنی بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/20074" target="_blank">📅 10:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20073">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDnpRloS4Iqbqda4tgVA-wM3XM0B8oCm6s6R-r0Dhlwtd8eELQnZYkvfLyUaoKI-aL2MWrJA1t_tiEelWfFR9ROiY9_va1XPUz7rqs0yBuy4Bvz2MdOGDAIBxud8zAsUAKE3107FGOX5idVK2b9lGwkCOP-Lff9QOAP4qchh4q2dmT2kDWjLKRswmji0eNkQ9nSA_mNYwxL_89_eY1Ecb8KgUOZgxI8t-gYkSHbi1SHBr7zie8sSLyHJ7pw1EJFMUGPwT0_quVJ7MEZMqnsQEqbCP8NkETtm9hkdrosEO5sNzt2u-sgEdyuJaFnEPMEiQIYdUMgDbHTlhfUfzb5kIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه حملات بامداد ۵شنبه ۸ مرداد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20073" target="_blank">📅 09:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20072">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند
و داخلش کنترل پهپاد انجام میدن...
هیچکدام از مردم روستا اطلاع ندارن که خونه بغلیشون چه خبره فقط میبینن تردد میشه در صورتیکه داخلش سیستم‌های کنترل پهپاد قرار داره
لطفا اگر هم قراره اطلاع رسانی بشه
فوروارد مستقیم نکن یاشار جان
آیدیم به فنا نره
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20072" target="_blank">📅 09:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20071">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاون سیاسی امنیتی و اجتماعی استاندار بوشهر از حمله هوایی به اطراف شهرهای بوشهر، جم و خورموج در شب گذشته خبر داد.
در این خصوص تلفات جانی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20071" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20070">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe63b4dfd0.mp4?token=BKYmREcCcjQcVjpqGeNgTvE1giC9Urro7ZnF4fu--UFm6jDd41D9AQgPbyKON8LdOVF2n5vPB0B4MD--iDjSm9EjYeWi1G4b7kYGza58Gk-HXp12QID4j42eO6Xfp_Mpnx6s2ggq5QfVsEuLbfBww1K-y8VkadMetU7BXCU3vPVyjdzZ8BA-sTEK2tM_tvv5JL6uLBxWNb_k-oLynUQ3xhaQ6E2TXCucUh_TXkYb3Ep2sYGmIgpwOkC6pWPl1NEonoLCOC_gCwLPY2u3usOQdz6aTmYoHFjR91qGnTY_8aro8HvksxgKpNgnbqp8F85jOX8ADHyUaVT4xZ3Xydf4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe63b4dfd0.mp4?token=BKYmREcCcjQcVjpqGeNgTvE1giC9Urro7ZnF4fu--UFm6jDd41D9AQgPbyKON8LdOVF2n5vPB0B4MD--iDjSm9EjYeWi1G4b7kYGza58Gk-HXp12QID4j42eO6Xfp_Mpnx6s2ggq5QfVsEuLbfBww1K-y8VkadMetU7BXCU3vPVyjdzZ8BA-sTEK2tM_tvv5JL6uLBxWNb_k-oLynUQ3xhaQ6E2TXCucUh_TXkYb3Ep2sYGmIgpwOkC6pWPl1NEonoLCOC_gCwLPY2u3usOQdz6aTmYoHFjR91qGnTY_8aro8HvksxgKpNgnbqp8F85jOX8ADHyUaVT4xZ3Xydf4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خمین
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20070" target="_blank">📅 07:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GztC7bPfib2MLvshS0RuJrd4MqGZ2U25S0IOKwbkH-6HEAXqQOmPscjy4E2bnWWu1XDNf7UCV7_Er6wnoBbP7o-GAgaprUgAnmi6GchEOzDtGB8hz6FK-5QsQIpJmB7CDrYRRvCYR9bJS19WVxB4TDBIID8ELCrrM-9GYPO3lL4k6UtiqtCeIQAkukNBmDZ0xv-ZvbORzHjBNBpUd_20Th2mq3FwdR1_XU4lYJhAWie_Przfvc-7KU5F39Mo2-qCBaSrdLowgsQXdpLFHvs6XyQzyazclnOlyNv5f_ysnZSq0fwQLVjk5-W51nn96ggHNiV4ZAOjad-YjKdZBU3wDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-QnTzhp5WftTStjucpU-4heNWWJkX2gnL4pqCpWrCiwDxjlCz_HjfXiO_qZbOCvsknsioOpnfvXaLC5gQdcZK1jI938OFXIxPOBwxdRgDjVknqDk-HS9KQ3p0cskjqdtteEQJzPkz7rqdxQDOhJoxchljAge7B9XKybv-g9ji29Y4OqGxy3anO0OmiexXBtXQZ5HaEq3Z3vqJA_GGPUJzkFU8WgpZLMCtmNRKqaoFYJUY9WZ-6C0vd_PAVoC8cXbjxwUMc7qUGgZ9RUCsy8M33XiZ3nZctLqjK7Fk9SYHnic_7XLZPkxtSfE0YCY2qWi8ZUm2J-j1nbMtWArBXVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tg_4-c2f_1fLuvwjp0OokiF-QFU4G-e76mvrg4fOUVGqr6VNwQvuoMj5fTmEQYcB5T8XIMe1FgSG7YfQwTsXFkejRY0TnlelikVsfavolkpeVbYNA-vBdD8nAQVX05vUt9nDbOAMUzkWj6ENHhFcWUjrRmiHOFgY3QP6NlIEFbw6LHaf7uvlO2S8838X9jA-W5Zsrw2s_0ddat505I7Qntgz8D-vYRO2epa2775QklAbz7rJkQHwFDiH4KsglSsE6wWPWZs3FV-Qdb-HlAPqE8IiKZTwJN4KFlth7dtIY3Cguw2eNB_gY9UB8-Wwcdky_Or9vARHNgpbcltioLsPaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قشم ( از پارچه های یا حسین به نظر میاد یک پایگاه بوده )
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20067" target="_blank">📅 07:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739655b0d2.mp4?token=Q1FKVpYgV3H0Rr8TK1KRFTMvCdBZYe19q8RgQqoyzSYdOUiAIg7AOp1jpMFGbLRAzr8ERaNqQZsy-lZsKd6E9mZFEsdCnKQncfxqE0xEwyyUSQ4MrYp5ZOyS6H67lZrLs73y0OGei6yVLAh1HUwDYf6Cmbpm2Qkh5SLozCBuhscthAIo_GVdzZnWit5VcoOeJgNS9SwPZxCY5-mRj6D6ydzfi5S2hN4X6fO2ua7oZEPzExXe7-9cLpsoGrYAZA1PBGki-BMg_PdJSnknFLQJtssUY0NcX-_O9QTNwZg021GxYV_ojf06oSoKVUT4rwpYAt9Sg6ckbsFjQZ0GAVRK6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739655b0d2.mp4?token=Q1FKVpYgV3H0Rr8TK1KRFTMvCdBZYe19q8RgQqoyzSYdOUiAIg7AOp1jpMFGbLRAzr8ERaNqQZsy-lZsKd6E9mZFEsdCnKQncfxqE0xEwyyUSQ4MrYp5ZOyS6H67lZrLs73y0OGei6yVLAh1HUwDYf6Cmbpm2Qkh5SLozCBuhscthAIo_GVdzZnWit5VcoOeJgNS9SwPZxCY5-mRj6D6ydzfi5S2hN4X6fO2ua7oZEPzExXe7-9cLpsoGrYAZA1PBGki-BMg_PdJSnknFLQJtssUY0NcX-_O9QTNwZg021GxYV_ojf06oSoKVUT4rwpYAt9Sg6ckbsFjQZ0GAVRK6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20066" target="_blank">📅 07:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20062">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sqok3UdWnwFpk-W32QCvUOgrsuonZd7fX2YoM38T4OiX59crEBVaJR39zB4VuwlHuvaD1ZFEeXIbp1BHDT7AELW0jrhsKLhwQQSIX0JhM2rFqeSuUlikTmXRALQ_H5V_wYBzLQQ6WUc5Lx5_aSyxNz8rYxD8wxE2xuBxWfurRw0Tew6XbMvWQLbik-Y0iEavQtGnRpKgQvaLZXOwwctZwD8orKPby-9LEqp0dlSaraiV1-sF7gLpPGQLqjHhStH4D4pPCABPVyOOOZl4HORFiQKS4ESqfzxuMpxhy8Aaso32BlJ1xW2cQ8MC1tnbYfYrGLrr6GS9NqrNl6caVobdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuU7W3BvcqVSCCk6imaId_muvgDCqTokHzuGqRDpSvyAanfpY5DxJ1E4FfiuIUKHCBM6BKD6ChpyA2KbnCFsmt2yDl9a6rbeeda_6fYJZgCFP56opCvtmLfGvEhnpKdi9ci3hutQBpb3LwshV4jpacZjXeR-CeS3hNH2rgWpZqrYvC8ZI9OfrqkqV34b1gbbl6Ht2nI4eUkyujxgUvJeaC7PN4VSVVFz-L8Tl9UDQM6I8aR15CVvuU6OvXgF_XFQX-DBd1RDoXNTrIiEslBK3m-yfqBOh3zmBlh3oddtJj3PbUqXoO_TQbGA6gHpM7XsTt8H-yGjxFVjg6iITuu2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_BS190uWczjeCdVBFPoQuAMpucN6k7FXsI8WFJktgQv_oWtCEP3gNTJ7uk_a95TEq6UWby-Sv_5fTDTbzZF74BTE-22p7WouL-cWWnJumJoA1Wpqts-396mw3Nv8X29KCaltbXo1cGI2QkOy_psLXihzbFIrkVbFrDfhM0Gx8vqCogzq3IZGy88X__yxoDws4EljuMBwzubTFFz60A3RoYcjcjVliD0wWlmzhjTSo2CBaWjmvow6HNuk1kpPFY27wM_FZlrCMPeEZWVnMZMsDSKC3OGfXFx8TnYa4fY5lx7DhM2c_Gum0nu2W-1z6x0g1_13XCt2BB7aJme7PcpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXszVk36zJnRbe2M7b1_BnLzY3arkoEQuSYXiuK5a_mt1S6T6bwgy2bBsJT5r6ak74vx4tgkl623Isw8Tnrdf0TvDhhOKSf7Kxu5SKBcbpDtPL0FkX-R4Lq9WXyqnL8-CNi8UVV2Zv1-eLS4oEfQXJpdsGIidVAG3WMUR9NsJflmAiqwO3J1esp5hEKIv8vWVt9F4Y8fSXGKo5hnDDLuozNn_VSx2rnALe7oNExk4KAhAb5wTxl-s02E-fh06jNiXRmMLA786eP_83bS4v22upzTC4TmmJ-c6rWUmUkkp7amCcu95en3uHZbnkMYl2dlxyu8khF53TM2j_wpf784aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از یزد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20062" target="_blank">📅 07:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20061">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c918aabbfc.mp4?token=sYGWgtce7uAxSq-D95DelzITvhdMw4mxH6SV_wDaY3hgBS1YwuKIZ-6JtUDzQL3qQDCLWr6g0OFLQ95ZqikQ5pI0BtI2fWMZ-JUigwEKUXSEET3r92ShnRHWB0uWDJzD9adaG6x_FxfXTxgBAA2TDWB0ZqdK_fYXxwHlsQY9YnRlCwAHD9kYCAHrTnYQbYWzXNd4s_00T1c88Ca5rku1MGiohyu7Zz0ZBcZG_HCdeOOBz0RK7ucM1xyVdbNt0JZqHF19yRbnFMcjXrpAZgdJxa8ulPxTE_0q088emG01boCB0pePYJfVUeL0OI2_I_fNwy-GWw7qnB-elpDDCobdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c918aabbfc.mp4?token=sYGWgtce7uAxSq-D95DelzITvhdMw4mxH6SV_wDaY3hgBS1YwuKIZ-6JtUDzQL3qQDCLWr6g0OFLQ95ZqikQ5pI0BtI2fWMZ-JUigwEKUXSEET3r92ShnRHWB0uWDJzD9adaG6x_FxfXTxgBAA2TDWB0ZqdK_fYXxwHlsQY9YnRlCwAHD9kYCAHrTnYQbYWzXNd4s_00T1c88Ca5rku1MGiohyu7Zz0ZBcZG_HCdeOOBz0RK7ucM1xyVdbNt0JZqHF19yRbnFMcjXrpAZgdJxa8ulPxTE_0q088emG01boCB0pePYJfVUeL0OI2_I_fNwy-GWw7qnB-elpDDCobdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریز شبستر دو تا موشک رفت
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20061" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20060">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2NCNA-OqmLnO1vjoJNzYuGszANjHQTijIIcoA6P3UQqEaD2XZq-an_TZ9gtfZfo4IUrirqQ5MrT0F2nVA4bix8IBfOeR8huw3qITk4OWLkVKwkPnWyjLw55zzu-tAnjrNOmNddnMaSzCu6Gq72aTX_CwifhWBHbrAo2_FOQF-SaYCykbHDzFPHpHbWJWhV8WSDQzSCU49nwUJdv3bMqZI3vi0Q2Q908sy8hwfglwKIXcnSoXG1e5Mv_Si4UMAJhr-FA0GvZCQNwJXC_z8aP2vi-8VC0PN-iTag3SGy0qX2NKt60f2DVsqVtVIwxHYo_JWD_J2vuhSBIhmFdnCSU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان پرتاب موشک از خمین
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20060" target="_blank">📅 07:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20059">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a4989fd2.mp4?token=R-wm9zMEb1d0NHMBX9I3Act5vowzqWCD0gSK1jMYZZa4pWV6wn84S-pCc43kf-MnptvskP-xLTHdbtil6XDe4y7Qv3zCRynucVfOFWqdkio_xxnNshPcBRRIseiGChOe42xgxMEX8IlQEGucycWbxmCpBFf5RF3ibihQ0mrhQcOuKzUcXMbxGmOmvYiVgOgA8CauajnQRMyhaf1REy1KOVNwgClmvDbrhPYGPB4dzjm4SEy_EFpJkElciEaQDNDGm1jeGGBCENB_y-jfQDeAH47Bp3vuKWK-et6bLWVDXgfhum2BcjTO6hRswVT314PHaJywKnEHMQPELSgug6YosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a4989fd2.mp4?token=R-wm9zMEb1d0NHMBX9I3Act5vowzqWCD0gSK1jMYZZa4pWV6wn84S-pCc43kf-MnptvskP-xLTHdbtil6XDe4y7Qv3zCRynucVfOFWqdkio_xxnNshPcBRRIseiGChOe42xgxMEX8IlQEGucycWbxmCpBFf5RF3ibihQ0mrhQcOuKzUcXMbxGmOmvYiVgOgA8CauajnQRMyhaf1REy1KOVNwgClmvDbrhPYGPB4dzjm4SEy_EFpJkElciEaQDNDGm1jeGGBCENB_y-jfQDeAH47Bp3vuKWK-et6bLWVDXgfhum2BcjTO6hRswVT314PHaJywKnEHMQPELSgug6YosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز حدود ۴ صبح
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20059" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7049e361.mp4?token=cznPpT5Ejtqwee--F4Qi4aUr4sT9OOv3bXnmMIh66cqpdCJ18AyEBcukb_1b7MW0OXpNwfZCH0XHCLLNcg6UsscjoSFG5zxOoFKE8njVfRmnjI2Aw887I4-Z2OEKmWqqZHFTaJg3iQTljfYF3bRFwm5jkGbMdbNtPo15MHwpKhCHn6qZDw31ygvxk7iki_xAMphsxirsbLJq0sp6ZEzFBadtmPzZCxEDhz6AioaGPrdRWvrvXbZETH2xLHaAjJ03zvOKAak_Fw27o3B_ia2W7dYHbl_fQNtSpipxzXmIWHu4VK2TC2to5BSvlbPVb8wS1lPCivOIK_m91IYtDq1Sag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7049e361.mp4?token=cznPpT5Ejtqwee--F4Qi4aUr4sT9OOv3bXnmMIh66cqpdCJ18AyEBcukb_1b7MW0OXpNwfZCH0XHCLLNcg6UsscjoSFG5zxOoFKE8njVfRmnjI2Aw887I4-Z2OEKmWqqZHFTaJg3iQTljfYF3bRFwm5jkGbMdbNtPo15MHwpKhCHn6qZDw31ygvxk7iki_xAMphsxirsbLJq0sp6ZEzFBadtmPzZCxEDhz6AioaGPrdRWvrvXbZETH2xLHaAjJ03zvOKAak_Fw27o3B_ia2W7dYHbl_fQNtSpipxzXmIWHu4VK2TC2to5BSvlbPVb8wS1lPCivOIK_m91IYtDq1Sag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس ۳:۴۵ بامداد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20058" target="_blank">📅 07:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b11a9cf.mp4?token=Tay46GBXChgMKh0lCEkU0IlxgnWo-kC5kww8qpOaFKU4k4jLPOs5LK4ZnETD5eYi5lqyUTQ0ArcCPdhZa33CMz6Xv1wVQlI16fX-HagPJCLEA_nky5ICLChcOqJbnydLPVEqFptJlWLYmztnA9mrZ3MJyO0-RZbYHLP8q5ktbv7nn2GUVXf1bEz404_1mJ-6qOk26pK9il6D0poIh2ElC0QGknkGYPTq9K9TZD_JzRVOckF_JTt-zB1zCDFC59Qc_QlQ1wY93hfDAHfu9uFK1ZTFRNXGuz02M1Ma-aGSzSqvX41GXNY-nc5ZZZ1Y7BKW6v8GFDrHqFd2H4Ux2SRNxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b11a9cf.mp4?token=Tay46GBXChgMKh0lCEkU0IlxgnWo-kC5kww8qpOaFKU4k4jLPOs5LK4ZnETD5eYi5lqyUTQ0ArcCPdhZa33CMz6Xv1wVQlI16fX-HagPJCLEA_nky5ICLChcOqJbnydLPVEqFptJlWLYmztnA9mrZ3MJyO0-RZbYHLP8q5ktbv7nn2GUVXf1bEz404_1mJ-6qOk26pK9il6D0poIh2ElC0QGknkGYPTq9K9TZD_JzRVOckF_JTt-zB1zCDFC59Qc_QlQ1wY93hfDAHfu9uFK1ZTFRNXGuz02M1Ma-aGSzSqvX41GXNY-nc5ZZZ1Y7BKW6v8GFDrHqFd2H4Ux2SRNxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">4 صبح آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20057" target="_blank">📅 07:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فاکس نیوز : هدف سفر نتانیاهو به امریکا تکرار 9 اسفند و بمباران تمام سایت های هسته ای و موشکی و نیروگاه های رژیم تروریست اسلامی ایران بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20056" target="_blank">📅 06:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNKFrWbGJ8x03mb4deIxYYED0auOLAIJVn_WLaFW0v8s2wfhe8h2CdECEX9svY4HhXBDuyJC8FxIUMSn-TWn5SuZhuSSMJ2L10jwmv8u2NB7C9i2ZdCoEV8QnlxrMAAHbJx-fZ1lpNyi6YljpVowZry94xxcKH9gCXZ4mhEaBxRprWkjBUUH3CuCpVXBfTlQe4TX7eTpLIYU5_44C9s3A4yD0KFHWQCJ7q76w3f5LiqDHxedXGkVCjNvmzldL6C_poIWV7FhiBaOchYnEAisiwj9CaSgjf0xQEz0gzP7acAT4IbIlDo5xsajiUrjo-ue6v-N2zHHGfesp6NhZZ2ZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : ده‌ها موشک ATACMS برد بلند آمریکا از کویت به سمت تأسیسات نظامی در داخل ایران شلیک شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20055" target="_blank">📅 06:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20054">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc88dc378.mp4?token=eF7ucFDlgHaMP484QRo1A1PZpThl4JCjfR3GDj_uapcqK47TbIEbB1nnmMsME1Qz7qm62IwkytrTfInz2rxcbMXDcFsJK0apZr1wcMXS5Ef6yjPAyMLz8VdCtdII6Ty70NnIt70xHQL7zbwAN0uQYhD6wfepRLKG4QXNwOQi44ehjA1LNEPUoErBiCFp6Nob6dolaxDQ1Z9qDuIt4IhDcjG_LBTUvsa7fRFEXBvSt4u9rK0aD2ooYXQu-lnaFUpw2fvINgWl2yDsTtiVZ4ZkRKGGNRXfxi6B-YKKB8x5yZAFP-x-CoHmUz90xNDKlKizlr60ALO59APe3TGuz_BaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc88dc378.mp4?token=eF7ucFDlgHaMP484QRo1A1PZpThl4JCjfR3GDj_uapcqK47TbIEbB1nnmMsME1Qz7qm62IwkytrTfInz2rxcbMXDcFsJK0apZr1wcMXS5Ef6yjPAyMLz8VdCtdII6Ty70NnIt70xHQL7zbwAN0uQYhD6wfepRLKG4QXNwOQi44ehjA1LNEPUoErBiCFp6Nob6dolaxDQ1Z9qDuIt4IhDcjG_LBTUvsa7fRFEXBvSt4u9rK0aD2ooYXQu-lnaFUpw2fvINgWl2yDsTtiVZ4ZkRKGGNRXfxi6B-YKKB8x5yZAFP-x-CoHmUz90xNDKlKizlr60ALO59APe3TGuz_BaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اطلاعات سپاه گلستان اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20054" target="_blank">📅 06:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aabd75843.mp4?token=Y64RUoWxCzYQv_Y5yBTHS8PgpSvdmSbzRw92E0gayJiTrlzRAsR3yF6mQqVUUo9p7Li_Gfykc_ytljKB1G3S1LXktn4e6tQkAzQBVTIn1b43_hiu70GQyHAXbCOhhaWgo1WT1eIVyxH5vRI6gj1upLnfMCvAYJGg2X--0u9vDilPBp7cCKQYlekgd57MxnppFHqDsmNftD7-3VUYNov5z4HQDiGPn0tWxBvRMfk3NGvoG-IAbmJYToMxxA1sJZFb6gtZLMCVnlWcmcSgF-kUxXzaxDm2QxCImXLWypIwkE_Zmr1hLSpsHsHJXTzEzNd1occTTmoHeNi6QszUIG5x3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aabd75843.mp4?token=Y64RUoWxCzYQv_Y5yBTHS8PgpSvdmSbzRw92E0gayJiTrlzRAsR3yF6mQqVUUo9p7Li_Gfykc_ytljKB1G3S1LXktn4e6tQkAzQBVTIn1b43_hiu70GQyHAXbCOhhaWgo1WT1eIVyxH5vRI6gj1upLnfMCvAYJGg2X--0u9vDilPBp7cCKQYlekgd57MxnppFHqDsmNftD7-3VUYNov5z4HQDiGPn0tWxBvRMfk3NGvoG-IAbmJYToMxxA1sJZFb6gtZLMCVnlWcmcSgF-kUxXzaxDm2QxCImXLWypIwkE_Zmr1hLSpsHsHJXTzEzNd1occTTmoHeNi6QszUIG5x3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در
ساعت ۵:۳۰ صبح پنج‌شنبه ۳۰ ژوئیه به وقت تهران
، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) با موفقیت یک موج سنگین از حملات را علیه ایران، در پاسخ به تلاش روز گذشته برای حمله موشکی به نیروهای آمریکایی، به پایان رساندند.
دارایی‌ها و تجهیزات سنتکام ده‌ها هدف متعلق به سپاه را در ایران هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، سایت‌های دیده‌بانی و دفاع ساحلی، و توانمندی‌های دریایی. هدف از این حملات، کاهش بیشتر تهدیدهای ناشی از ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حوزه خلیج فارس عنوان شده است
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20053" target="_blank">📅 06:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس به نقل از مقام ارشد آمریکایی :
آمریکا هم اکنون در حال انجام حملاتی در ایران هست.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20052" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بوست کم شده داریم لول میایم پایین یه کمک کنیدد بریم بالا استیکر شاه برگرده به دوستاتون که پرکیوم دارن هم بگین
https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20051" target="_blank">📅 02:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش‌ها از شنیده شدن چند انفجار سنگین در نورآباد ممسنی فارس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20050" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، در ماه فوریه تخمین زده بود که کمپین علیه ایران برای دستیابی به اهدافش ممکن است شش هفته یا بیشتر زمان نیاز داشته باشد.
کوپر در ۳۱ مارس ارزیابی کرد که هنوز حدود ۲۰ روز دیگر برای تکمیل عملیات نیاز دارد.
با این حال، سرنگونی یک فروند جنگنده F-15E Strike Eagle آمریکایی در ۳ آوریل بر فراز جنوب غربی ایران، علیرغم نجات موفقیت‌آمیز هر دو خدمه در تصمیم ترامپ برای پیگیری آتش‌بس تنها در چند روز بعد نقش داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20049" target="_blank">📅 02:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش صدای انفجار سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20048" target="_blank">📅 02:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رویترز: انفجارهای شدید و پیاپی، کیف پایتخت اوکراین را به لرزه درآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20047" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به گفته روزنامه وال‌استریت ژورنال ، ارتش ایالات متحده قراردادی به ارزش ۵۸.۶ میلیارد دلار با شرکت لاکهید مارتین برای افزایش تولید موشک‌های دفاع هوایی پاتریوت امضا کرده است؛ بزرگ‌ترین قرارداد تاریخ برای موشک‌های پاتریوت.
این قرارداد بر تولید موشک‌های پیشرفته
PAC-3 MSE
تمرکز دارد؛ موشک‌هایی که برای رهگیری موشک‌های بالستیک، موشک‌های کروز، هواپیماها و پهپادها استفاده می‌شوند. هدف این برنامه، افزایش ذخایر موشکی آمریکا و متحدانش و بالا بردن ظرفیت مقابله با حملات گسترده موشکی پس از تجربه جنگ اوکراین و افزایش تهدیدهای موشکی در جهان است
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20046" target="_blank">📅 01:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آسوشیتدپرس : ایالات متحده تمام مذاکرات را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20045" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b45ec100a.mp4?token=Lf8bgrhDQvyMBZ6uVd1H3vBHjwra1tSY7tuXAaLZMSGsQQbtnng1JxD_gTIdktfhEnBGF25Mo9MDiDVeS74aPR1gWN6RUTcaLnZJUIDiKMEEi4ZCCSH0PTKZgbx1aSWtasyVKaO0aDIqlnj2NcoMsjbKVLM8FN5XKu2QzOt7SEf5vnM19rrkmJbd7FVGt2Em-XrCpsnhQu2gigr5aeMAp8Oh93bCw-EdwfIhfX-R5v5dzrBA2pDd2FWuwsJqvNjjVfap24abpyJthC9iEQqqDn9IzAlHGTaCUiK-Zk_IhP_mNsncnHSW7PtRBxJ0UjXTF_0ywxF7cc-cocY2IZ4VLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b45ec100a.mp4?token=Lf8bgrhDQvyMBZ6uVd1H3vBHjwra1tSY7tuXAaLZMSGsQQbtnng1JxD_gTIdktfhEnBGF25Mo9MDiDVeS74aPR1gWN6RUTcaLnZJUIDiKMEEi4ZCCSH0PTKZgbx1aSWtasyVKaO0aDIqlnj2NcoMsjbKVLM8FN5XKu2QzOt7SEf5vnM19rrkmJbd7FVGt2Em-XrCpsnhQu2gigr5aeMAp8Oh93bCw-EdwfIhfX-R5v5dzrBA2pDd2FWuwsJqvNjjVfap24abpyJthC9iEQqqDn9IzAlHGTaCUiK-Zk_IhP_mNsncnHSW7PtRBxJ0UjXTF_0ywxF7cc-cocY2IZ4VLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش خوردن عنبه
😁
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20044" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20039" target="_blank">📅 01:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار در تبریز و بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20038" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20037">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرگزاری صدا و سیما : شنیده‌شدن صدای انفجار در پایتخت عربستان
منابع عربی می‌گویند لحظاتی پیش صدای ۲ انفجار نامشخص، به وضوح در ریاض شنیده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20037" target="_blank">📅 01:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20036">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تیک تاک ، تیک تاک ، تیک تاک
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20036" target="_blank">📅 01:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20035">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">همان طور که دیروز گفتم، اینستاگرام و چنل تلگرام رو میخوام پرایوت کنم. این آخرین فرصت برای کسایی هست که ممکنه دیروز این پیام رو ندیده باشن !سریع عضو بشین تا پشت در پیش عرزشیه ها نمونین
🌐
instagram.com/yashar
🌐
t.me/WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20035" target="_blank">📅 00:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20034">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هم‌اکنون ۵ هواپیمای سوخت‌رسان از اسرائیل و ۵ هواپیمای سوخت‌رسان از عربستان سعودی، به سمت خلیج فارس بلند شدند، دو سوخت‌رسان هم‌ در آسمان خلیج فارس با فرستنده روشن مشغول عملیات هستند. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20034" target="_blank">📅 00:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgkrZENOK-s2WLeNLhf_UxaHU_EsEcjZlV1b8iKTu77UqBwhiPHo4ueVe9FJQLMxVTE7ahxATqmp6wYVNgXpZcZtKIg9E4lWRCoaHvhn06lqXABJg58arsPc7sBnKNZFj_xa8Dgwz1Uxy3hpItxBHcPQ6zTgu1yXC7aJQqj9UCKsn2S_2MSC_in65AlScAtr15GBy3VCOA4P0A3vF_tKzz77Dm5NMiuvDg0BMfvQ8jQHVWOpHphocdlpARJOZgX3RZEPXQyJWbu36QNYsQf4zjUCxgju6wNn-7LScu-2sGi7inq8FDhNkjAfm-PzZDNfD8Fg2FfguBOiipKJf0zLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون ۵ هواپیمای سوخت‌رسان از اسرائیل و ۵ هواپیمای سوخت‌رسان از عربستان سعودی، به سمت خلیج فارس بلند شدند، دو سوخت‌رسان هم‌ در آسمان خلیج فارس با فرستنده روشن مشغول عملیات هستند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20033" target="_blank">📅 00:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20032">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وال استریت جورنال:
ترامپ با وعده انتقام از ایران، از یک دور جدید از حملات "بسیار شدید" خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20032" target="_blank">📅 00:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20031">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20031" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20030">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش شلیک موشک بالستیک از ایران
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20030" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تا آخر گوش کن</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20029" target="_blank">📅 00:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از دایرکت مشخصه امشب هیجان به اوج رسیده</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20028" target="_blank">📅 00:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مقام ارشد اسرائیلی به الجزیره : پاسخ گسترده آمریکا به ایران محتمل‌تر از فقط یک حمله تلافی‌جویانه است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20027" target="_blank">📅 23:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20025">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ در مورد ایران:
من دوست دارم تعرفه‌هایی علیه ایران اعمال شود.
لیندسی این را می‌خواست.
خبرنگار: آیا می‌خواهید مجلس نمایندگان قبل از ۳۱ آگوست برای بررسی لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: راستش را بخواهید، نباید لازم باشد، اما اگر لازم باشد، دوست دارم ایران را به عنوان تعرفه اضافه کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20025" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4981a0c73.mp4?token=uma6w4tzcZvBsiybspTSYE0RP-At42wwsbKClAsnT__lhgXYPtm9uXf83_6wZ59C6CdnHPd2qa_9CPDWjhxIBh7R1KSUsr5K4dJ0XQ_mLuDt0NMZKFzacVPTK_dvuGZHm71gG8Vsuu50aL1NRETeutJQvnUPZYWa3uZE9RAemwVGLKYDgNn_qZR9FJ1ruZTW-9VG9Rjxq2SsIfXRnd4-oMt-ySmlGMpr81n4CaKxaj6LJTVyk1Sp_9hxKTrxhD8Uf4vEygmXXBlXzhfy4iw3x_YDfueR4vNKzQ6ZUEKmNtOBZuhV6Zeiw_9HW-3UdVJxqjBib4Md-9xFiDQxpCikEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4981a0c73.mp4?token=uma6w4tzcZvBsiybspTSYE0RP-At42wwsbKClAsnT__lhgXYPtm9uXf83_6wZ59C6CdnHPd2qa_9CPDWjhxIBh7R1KSUsr5K4dJ0XQ_mLuDt0NMZKFzacVPTK_dvuGZHm71gG8Vsuu50aL1NRETeutJQvnUPZYWa3uZE9RAemwVGLKYDgNn_qZR9FJ1ruZTW-9VG9Rjxq2SsIfXRnd4-oMt-ySmlGMpr81n4CaKxaj6LJTVyk1Sp_9hxKTrxhD8Uf4vEygmXXBlXzhfy4iw3x_YDfueR4vNKzQ6ZUEKmNtOBZuhV6Zeiw_9HW-3UdVJxqjBib4Md-9xFiDQxpCikEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد حملات ایران:
این گروه با گروهی که ما با آن سر و کار داریم متفاوت بود.
آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، ما باید کمی آنها را تنبیه کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20024" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20023">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364b88f4c7.mp4?token=VTcCX9U2nrmbWPnpH49kf7j1CYyig1DCBa5Bs3JEyg8LgEN_-qJM6vCGTmgnaHj7tHJwoxKNFesYiEUTZuihGIoXquBMiPIbmGYMi67zV-pfjxUqZlkgYlDoFvmMSckyCa4SWj_Lm9_4Bn1Lsbu7DfVHRWrzsEc6uh81_c-GlSPBhkH0vqsGJ52Cv6O__rA584iVqvWxuKOXBO6GoC-6atQRIRRxtic91nsY-C4DywMDLJLXIQB2DyE0ZV9l-J3tBey0rFdNUhngLO5RXzLldd0af-AcGTbuvuheHDa84kz4XfvGNQIkKfkxI-p80LD8SEvDRXsqPT4Mhf4gslGKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364b88f4c7.mp4?token=VTcCX9U2nrmbWPnpH49kf7j1CYyig1DCBa5Bs3JEyg8LgEN_-qJM6vCGTmgnaHj7tHJwoxKNFesYiEUTZuihGIoXquBMiPIbmGYMi67zV-pfjxUqZlkgYlDoFvmMSckyCa4SWj_Lm9_4Bn1Lsbu7DfVHRWrzsEc6uh81_c-GlSPBhkH0vqsGJ52Cv6O__rA584iVqvWxuKOXBO6GoC-6atQRIRRxtic91nsY-C4DywMDLJLXIQB2DyE0ZV9l-J3tBey0rFdNUhngLO5RXzLldd0af-AcGTbuvuheHDa84kz4XfvGNQIkKfkxI-p80LD8SEvDRXsqPT4Mhf4gslGKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: چه چیزی می‌توانید درباره حمله به نفتکش در مصر به ما بگویید؟ آیا این موضوع به ایران مربوط است؟
ترامپ: من در جریان قرار گرفته‌ام. این کمی بیشتر از همان چیزهای تکراری است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20023" target="_blank">📅 23:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b410c8b1ad.mp4?token=i3_xKIF9n2dZ3emfbHEC90mlch7hio20VGsLc06cYwWGv23MLR5g-ITK5bDqGLaLBq8X1vaNZio-_Z1pwXY8TYmxzSISVahjthyzAh1S4-NRzvdNtBrfsuz_YgB0xF_hutOk4mX2qJTxfjJYIo3SjycbsT506QamDySXi8cVQvR7_bVCIdJ6CvH0TUa-PK0nmYLYZ5jYRugxP69HSSbFEymheFS6dtiJx_7ndCZ3-BFM3CgW6qrgSKnoddc1Fz7qAHEs5G0RnhU9OjVFM7wVL3fwE6zs3oOmkiwZ47nj0CQWS23oWVxBnpUYbchxEcqmgfUUxPC5QkCpKCHmpZNZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b410c8b1ad.mp4?token=i3_xKIF9n2dZ3emfbHEC90mlch7hio20VGsLc06cYwWGv23MLR5g-ITK5bDqGLaLBq8X1vaNZio-_Z1pwXY8TYmxzSISVahjthyzAh1S4-NRzvdNtBrfsuz_YgB0xF_hutOk4mX2qJTxfjJYIo3SjycbsT506QamDySXi8cVQvR7_bVCIdJ6CvH0TUa-PK0nmYLYZ5jYRugxP69HSSbFEymheFS6dtiJx_7ndCZ3-BFM3CgW6qrgSKnoddc1Fz7qAHEs5G0RnhU9OjVFM7wVL3fwE6zs3oOmkiwZ47nj0CQWS23oWVxBnpUYbchxEcqmgfUUxPC5QkCpKCHmpZNZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:ما می‌خواهیم آن‌ها را بسیار سخت بزنیم زیرا نوبت ماست که آن‌ها را بزنیم.
آن‌ها می‌دانند که این در راه است. آن‌ها از ما می‌خواهند که این کار را نکنیم.
آن‌ها دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20022" target="_blank">📅 23:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اکسیوس دربار دیدار ترامپ و نتانیاهو :
نتانیاهو در دیدار با ترامپ نسبت به احتمال دستیابی به توافق با ایران ابراز تردید کرد و گفت‌وگوی ۹۰ دقیقه‌ای دو طرف عمدتاً بر ایران متمرکز بود. به گفته یک مقام اسرائیلی، سه گزینه برای ادامه مسیر بررسی شد: دستیابی به توافق با ایران، ادامه محاصره دریایی و تشدید فشار اقتصادی، یا ازسرگیری و گسترش حملات نظامی. این مقام گفت ترامپ درباره پیامدهای جنگ بر بازار انرژی و اقتصاد جهانی ابراز نگرانی کرد، اما نتانیاهو تأکید داشت جمهوری اسلامی در تلاش است با استفاده از تنگه هرمز آمریکا را وادار به امتیازدهی کند و باید فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی افزایش یابد. او همچنین مدعی شد ایران با کمبود سوخت، صف‌های طولانی بنزین، کمبود گازوئیل و نارضایتی عمومی روبه‌رو است و حکومت از احتمال گسترش اعتراضات مردمی نگران است. این مقام اسرائیلی همچنین ادعا کرد که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری
و بسیار شدید خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20021" target="_blank">📅 22:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آسوشیتدپرس : ۶ نیروی مشاور سپاه قدس در حمله مشترک آمریکا و عربستان سعودی کشته شدند. @WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20020" target="_blank">📅 21:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارشات از‌ پرتاب موشک از شازند اراک  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20019" target="_blank">📅 21:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارشات از‌ پرتاب موشک از شازند اراک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20018" target="_blank">📅 21:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به گزارش واشنگتن تایمز، وزارت خزانه‌داری آمریکا اعلام کرد دو نهادی را که به گفته این وزارتخانه از سوی ایران برای کنترل تردد در تنگه هرمز مورد استفاده قرار می‌گیرند، تحریم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20017" target="_blank">📅 20:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به گزارش وای نت عبری به نقل از یک منبع ارشد سیاسی، گفت‌وگوی میان بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و دونالد ترامپ، رئیس‌جمهور آمریکا، عمدتاً بر موضوع جمهوری اسلامی متمرکز بوده و به عنوان «یک رایزنی واقعی و تبادل نظر» توصیف شده است.
این منبع اعلام کرد که رئیس‌جمهور آمریکا با سه گزینه راهبردی روبه‌رو است:  دستیابی به یک توافق، ادامه محاصره دریایی، یا «از سرگیری و تشدید حملات». همچنین تأیید کرد که مجتبی خامنه‌ای، زنده است و افزود: با اطمینان این را می‌گویم
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20016" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارشات اولیه: صدای انفجارهای شدیدی در اردن شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20015" target="_blank">📅 20:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee18be9c.mp4?token=ff-GQLxSifofdua7SDA3-qvDFnuBX1V1xC8CNaMW5_cGrDHwFX1uGYWcaQ-kceSJ_oHMCJAWYjicAIh16SrwjYrA-6zea3ttK7-HhbrhlO5hyqDHtMqrVB0rio2-9hvxNqUlmvNPvkuMtD-fKVUAU5b_wWEwywq3w6skqGhsqbbJOTTCmVsiyw3spyckNVVZ1Ydl8bUsQUJgmLErh7eeFqjVtaNI4Xu0Io84OJ3rryHyGjfpPE4oIhuzf-tT4vx_XyXCi-iPsW5La3ZBwHjPRt1iiH09vsQrRt0NhoPqQXrxh7yd9OG4KUs4qG6tD2tiwN3m419mvjfV1wH04EfXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee18be9c.mp4?token=ff-GQLxSifofdua7SDA3-qvDFnuBX1V1xC8CNaMW5_cGrDHwFX1uGYWcaQ-kceSJ_oHMCJAWYjicAIh16SrwjYrA-6zea3ttK7-HhbrhlO5hyqDHtMqrVB0rio2-9hvxNqUlmvNPvkuMtD-fKVUAU5b_wWEwywq3w6skqGhsqbbJOTTCmVsiyw3spyckNVVZ1Ydl8bUsQUJgmLErh7eeFqjVtaNI4Xu0Io84OJ3rryHyGjfpPE4oIhuzf-tT4vx_XyXCi-iPsW5La3ZBwHjPRt1iiH09vsQrRt0NhoPqQXrxh7yd9OG4KUs4qG6tD2tiwN3m419mvjfV1wH04EfXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:من همین الان گفتگویی را با وزیر دفاع، پیت هگست، به پایان رساندم.
او چیز جالبی به من گفت. او به من گفت: "ما به جهان نگاه می‌کنیم، کشورهایی هستند که اراده جنگیدن در کنار ایالات متحده را دارند، اما فاقد توانایی هستند. و کشورهایی هستند که توانایی دارند، اما اراده ندارند."
او گفت: "فقط در اسرائیل است که هم اراده و هم توانایی را می‌بینیم."
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20014" target="_blank">📅 20:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الجزیره: شرکت امنیت دریایی امبری گفت که حداقل یک حمله پهپادی به یک تأسیسات ذخیره‌سازی گاز طبیعی مایع ایالات متحده در دمیاط، مصر اتفاق افتاد
تأسیسات ذخیره‌سازی شناور مورد هدف قرار گرفته متعلق به یک شرکت آمریکایی در دمیاط مصر است و توسط آن اداره می‌شود.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20013" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سنتکام : تنگه هرمز یک آبراه بین‌المللی است.  سپاه پاسداران انقلاب اسلامی هیچ اختیاری برای تعیین مسیرهای تردد برای جریان آزاد و باز ندارد. کشتی‌های تجاری همچنان از این تنگه با حمایت نظامی ایالات متحده استفاده می‌کنند.  از اوایل ماه مه، نیروهای سنتکام به عبور تقریباً ۱۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20012" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آسوشیتدپرس : ۶ نیروی مشاور سپاه قدس در حمله مشترک آمریکا و عربستان سعودی کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20011" target="_blank">📅 19:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=GcG-_bW8gUsM56LOVBy0vKsdcCXfn-hIPupcgVPn9gfYfYAcPhF7DFQcIpiwZMbtJzffvbJxTxu123dwkEp7UK4HQ89yiU94-WX04jGPYrWzKXtF9gERUspZgSpceyDaH4uavhdE1GkTs1fZN2sFXwLyJ65wjUEFi3dw3fMltEPWKt7lUjbugkBbRzChb3oTIQtzikp_lQyGMvaovxwPxIfOusmQtmERFy0NfCwwNZVorb1QZYIArmRrsPclQwN7gsYWUAxS6H2vnoLn1fa71BPrcGcnVmMFG8vXTtw-NNasdzk8yMNBWQDq1aWhdD1YWWm30Lc4MXk6sqx0CMao6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=GcG-_bW8gUsM56LOVBy0vKsdcCXfn-hIPupcgVPn9gfYfYAcPhF7DFQcIpiwZMbtJzffvbJxTxu123dwkEp7UK4HQ89yiU94-WX04jGPYrWzKXtF9gERUspZgSpceyDaH4uavhdE1GkTs1fZN2sFXwLyJ65wjUEFi3dw3fMltEPWKt7lUjbugkBbRzChb3oTIQtzikp_lQyGMvaovxwPxIfOusmQtmERFy0NfCwwNZVorb1QZYIArmRrsPclQwN7gsYWUAxS6H2vnoLn1fa71BPrcGcnVmMFG8vXTtw-NNasdzk8yMNBWQDq1aWhdD1YWWm30Lc4MXk6sqx0CMao6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیتر هگست، وزیر جنگ، در واشنگتن دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20010" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو : جمهوری اسلامی، فرایند غنی‌سازی اورانیوم را در کوه کلنگ اصفهان آغاز کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20009" target="_blank">📅 18:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=a7oE5c5TTFln7Gn-YMghTiWoWU01_5m-W0yQHv9Ook_mJIPqmz656tR1jKDLO788xHcLgmKjJs7ZIggygYxG0F3px_M1ks51aoQ2vVj_sbExHFn1FSjULGmkE5sPx3CecfnBI21pBo8kped058zMYia0RA4JKBjnaYcFr9PxBtFmW0314pLZXxwMrbA5RT3UtRETsNugNJtPUJ-yxliK9khR5-ykJOuCS1zl4VoMatuB_oBANn9N9xYjScuK-nPD9uVEJX-TNI8anJ8oFXZXXjpI1sxU6PLjfoIbO1zNhnhUX-Pnh1XQGZDcB4VGMi6RotpDc9m0eR3W7K-B8NiuFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=a7oE5c5TTFln7Gn-YMghTiWoWU01_5m-W0yQHv9Ook_mJIPqmz656tR1jKDLO788xHcLgmKjJs7ZIggygYxG0F3px_M1ks51aoQ2vVj_sbExHFn1FSjULGmkE5sPx3CecfnBI21pBo8kped058zMYia0RA4JKBjnaYcFr9PxBtFmW0314pLZXxwMrbA5RT3UtRETsNugNJtPUJ-yxliK9khR5-ykJOuCS1zl4VoMatuB_oBANn9N9xYjScuK-nPD9uVEJX-TNI8anJ8oFXZXXjpI1sxU6PLjfoIbO1zNhnhUX-Pnh1XQGZDcB4VGMi6RotpDc9m0eR3W7K-B8NiuFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20008" target="_blank">📅 18:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">زلنسکی:از ترامپ درخواست کردم که یک «بسته اضطراری زمستانی»، شامل ۳۰۰ موشک رهگیر پاتریوت را در اختیار اوکراین قرار دهد
اگر مشکل کمبود این موشک‌ها برطرف نشود، حملات روسیه نیروگاه‌های برق ما را نابود و یک بحران انسانی ایجاد می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20007" target="_blank">📅 18:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رسانه‌های حقوق بشری: اجرای حکم علیرضا سپاهی(فرد سوم در اصفهان)بعد از سکته قلبی متوقف شد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20006" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پس از تهدید ترامپ علیه ایران: قیمت نفت هم اکنون به 90 دلار به ازای هر بشکه افزایش یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20005" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد نیروهای این کشور در جریان عملیات در روستای حداثا، واقع در منطقه حائل جنوب لبنان، تونلی به طول ۵۵ متر را کشف و نابود کردند که زیر یک کارخانه تولید مصالح ساختمانی و در نزدیکی یکی از مواضع نیروهای حافظ صلح سازمان ملل (یونیفل) در جنوب لبنان ساخته شده بود به گفته ارتش این تونل شامل سه اتاق بوده و حزب‌الله از آن به عنوان مرکز فرماندهی استفاده می‌کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20004" target="_blank">📅 16:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20003">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانال ۱۴ : ترامپ درباره حمله ایران:  «قراره به باسن‌شان لگد بزنیم»
رئیس‌جمهور ترامپ پس از آنکه ایران موشک‌های بالستیک به سوی اردن شلیک کرد، وعده داد که پاسخی گسترده و سخت خواهد داد. این در حالی است که ایالات متحده و عربستان سعودی، در پی بیش از ۳۰ حمله پهپادی به نیروهای آمریکایی و تأسیسات نفتی عربستان، حملات مشترکی را علیه شبه‌نظامیان مورد حمایت ایران در عراق آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20003" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانال ۱۴ : ترامپ درباره حمله ایران:  «قراره به باسن‌شان لگد بزنیم»
رئیس‌جمهور ترامپ پس از آنکه ایران موشک‌های بالستیک به سوی اردن شلیک کرد، وعده داد که پاسخی گسترده و سخت خواهد داد. این در حالی است که ایالات متحده و عربستان سعودی، در پی بیش از ۳۰ حمله پهپادی به نیروهای آمریکایی و تأسیسات نفتی عربستان، حملات مشترکی را علیه شبه‌نظامیان مورد حمایت ایران در عراق آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20002" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20001">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دونالد ترامپ اعلام کرد حملات علیه مواضع شبه‌نظامیان وابسته به ایران با هماهنگی دولت عراق صورت گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20001" target="_blank">📅 16:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20000">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو شامگاه گذشته در اقامتگاه بلر هاوس با معاون رئیس‌جمهور آمریکا، ونس، دیدار کرد همچنین نخست‌وزیر نتانیاهو امروز با وزیر جنگ آمریکا، هگست، دیدار خواهد کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20000" target="_blank">📅 16:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19999">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک سرطان جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نفوذی جمهوری اسلامی هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19999" target="_blank">📅 16:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19998">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ درباره ایران :
ما به آنها اجازه می‌دهیم که به وراجی ادامه بدهند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19998" target="_blank">📅 16:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19997">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره ملاقاتش با نتانیاهو:
این یک ملاقات عالی بود. او اکنون متوجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19997" target="_blank">📅 16:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19996">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e251708c59.mp4?token=csGPLvq3POHFJ9ImkCBGAOGreBIQRPA9dG6vSfaLwhPHU9bPI-grEqVnyvwwzq5H7rYFkjfYuro9nxd2tsk932Vq8X1NL0RdDhokr3CAQqNlX6sGV3XRxKdZ1u9j1tT8-mhSDKAG3Ooio7ru3lRAxQBU-ipoaw2koL8YLFEEgQtlnsPYw95RPcGhnFRfl1RcwDriM8N_AEUx0iJ6WZiJoV3L2yIc5ZRgXX9G210WU82AaqZnacVonJ7hp02HQjKu9e_3XT955q60B1pRv3sB6vy0DaBaKk88HJ8Jib-XDEqJ9HSIaEiq4hpbKscisqg-algK39xIUgaUnuQICwaatx7FH_kI-HxuvU3dmgA3HD34XjKb42-zPPJ8vy4L-9Imoh5uywwvH_Wf4YtAutVY_uWB76UezE9HyHxNlS-i_3bwdOgKx9fl6MQ5BoXesuFpq-YJti0mdfBwJfzklq_58EsH4TJTSQX8ZJIL6e8pPRUSDiuZ8qPqonSevS4D7hFF7575NFboy8JySmlXPx0Zghf55yLPpQOCHfxfGLdzq1SaKFAeYrPd-byrmm3fskEmWy3CU2zFcv7vZPsCIfM2BZ7KrwY_CPSSeXXRLuG8qYSqPOaWeKgNE_NH0UkAHaT6NVAIWBI3EmhR-6tT-IAztg0uvaojdtp31fyy45Bg2yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e251708c59.mp4?token=csGPLvq3POHFJ9ImkCBGAOGreBIQRPA9dG6vSfaLwhPHU9bPI-grEqVnyvwwzq5H7rYFkjfYuro9nxd2tsk932Vq8X1NL0RdDhokr3CAQqNlX6sGV3XRxKdZ1u9j1tT8-mhSDKAG3Ooio7ru3lRAxQBU-ipoaw2koL8YLFEEgQtlnsPYw95RPcGhnFRfl1RcwDriM8N_AEUx0iJ6WZiJoV3L2yIc5ZRgXX9G210WU82AaqZnacVonJ7hp02HQjKu9e_3XT955q60B1pRv3sB6vy0DaBaKk88HJ8Jib-XDEqJ9HSIaEiq4hpbKscisqg-algK39xIUgaUnuQICwaatx7FH_kI-HxuvU3dmgA3HD34XjKb42-zPPJ8vy4L-9Imoh5uywwvH_Wf4YtAutVY_uWB76UezE9HyHxNlS-i_3bwdOgKx9fl6MQ5BoXesuFpq-YJti0mdfBwJfzklq_58EsH4TJTSQX8ZJIL6e8pPRUSDiuZ8qPqonSevS4D7hFF7575NFboy8JySmlXPx0Zghf55yLPpQOCHfxfGLdzq1SaKFAeYrPd-byrmm3fskEmWy3CU2zFcv7vZPsCIfM2BZ7KrwY_CPSSeXXRLuG8qYSqPOaWeKgNE_NH0UkAHaT6NVAIWBI3EmhR-6tT-IAztg0uvaojdtp31fyy45Bg2yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : بعد از حملات غافلگیرانه به نیروهای آمریکا در اردن، حسابی جوابشون رو می‌دیم
محکم بهشون ضربه می‌زنیم، حسابی تنبیه می‌شن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19996" target="_blank">📅 15:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19995">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">amme kojai(IG @yashar)</div>
  <div class="tg-doc-extra">TaTaloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/19995" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19995" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19994">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:
حملاتی علیه ایران انجام خواهد شد و ما با قدرت به آنها ضربه خواهیم زد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19994" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19993">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19993" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19992">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسپانیا پخش اذان از بلندگو رو در بعضی از شهرها مجاز اعلام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19992" target="_blank">📅 15:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19991">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری رژیم فارس: تنگه هرمز بسته بسته است، دیگه از این بسته‌تر نمیشه.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19991" target="_blank">📅 14:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19990">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هم اکنون هشدار های حمله موشکی/پهپادی در تلفن های شهروندان اردن نمایش داده می شود
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19990" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19989">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز: فرماندهان سنتکام در حال بررسی امکان توقیف تلفن همراه سربازان آمریکایی جهت عدم انتشار تصاویر خسارات ها هستند
ژنرال براد کوپر، فرمانده ستاد مرکزی فرماندهی ایالات متحده (CENTCOM)، به نیروهای آمریکایی مستقر در خاورمیانه هشدار داده است که ویدیوهای ضبط شده با تلفن همراه و منتشر شده در اینترنت، به ایران کمک می‌کند تا میزان اثربخشی حملات خود را ارزیابی کرده و موقعیت‌های نظامی آمریکا را شناسایی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19989" target="_blank">📅 14:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ed6y7I2P-gSsrdPShtHAQBmB3aZbfD4t1ET_3ubcVh_PUcceUHpiydK_KBLdJAJ26j4z90lqklcEEhmZktLw6HyMOWBMxyf73QPbPF7l23zZ-AqKMlhJtT0s46_0-D6cfiAQLkXEgiNZYOOFgU8svAE7qY_RVVrmyL5qdcEoHvbQIZ-2nXSzIFj1Cjdj9bdrqUqs-9WqK3xh97m8ZYr6C7-D6saW0PZ-3ZeA2RW7U-n6_QL_WdeVd-iQ4B5cGcvVxkamKa2RJCoYS3Ek5abtIk9cDg2hPSl7-q3caIJ5LFE4fxYtrYxgnIrf-J0-G_s6XTBytV--ZAyDvLx9o1yhhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEy09gHfvO0PC0_mQ2Jz7DX0SdMJeu8Mmj3-uSw3udO_3YgeO2moHG2OHGLLgNV_jAx81hPiDGrEZJZaEAhQAqsG3wXQqhZnYfIYGzEjGtZBPLA9gaVDc4eiZskVXt3Puka3TNdkNK1-AVT_7JESp8tUVGdq1haPThdF4IR-kEx_lM_OF-PRA1dk3rokapprPh8LQbWOzcj0rtLosGukHIDckUyyqigPgzX4j42C53jFVng2MUfFZML4RQOtZj0l4y0e_dVx5jfVcszLYN42AhdaWJorSzivCJxnNyA4tH-VFRpw44IFY6DTvPvXYack_5xaT2_DeP7tnEs-UuKqkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمله به شمال ایران ساحل خزر شهر
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19987" target="_blank">📅 14:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش های تایید نشده رسانه های بومی و مردمی در خصوص حمله هوای به نوار مرزی پیرانشهر در ایران  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19986" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تصمیم‌گیری در مورد ایران
کاخ سفید اعلام کرد که ترامپ امروز ساعت 18:30 به وقت تهران یک جلسه اطلاعاتی مهم خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19985" target="_blank">📅 14:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زلنسکی به اکسیوس :  رابطه‌ام با ترامپ خیلی بهتر و سازنده‌تره ، مثل قبل دیگه این‌قدر احساسی نیست
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19984" target="_blank">📅 13:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش های تایید نشده رسانه های بومی و مردمی در خصوص حمله هوای به نوار مرزی پیرانشهر در ایران
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19983" target="_blank">📅 13:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش انفجار در عراق و اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19982" target="_blank">📅 13:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش‌ تایید نشده شنیده شدن صدای پرتاب موشک از ‌کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19981" target="_blank">📅 13:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مشاور ارشد ترامپ: "ایران می‌خواهد حزب‌الله در لبنان فعال بماند، ما اجازه این کار را نخواهیم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19980" target="_blank">📅 13:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3Tcnp0PjdPB85e5f1-7UdZouDewiTE3zAPQ1UFZx8z8CjrtJxXGrV49909BIewHjUO74SV0qX9PTGnestxHEpe1XiwRuFPHWfvhdFVqf5ebhkpB5Rg3vBfEZWSocQI6Wm90yZRqy80ndaD67IeVhyLzR-l8ElyYv5d3nAnqXMtdRbCQny1KyhmlS1ZZEs1gVwAJU-XtG1biU2uS1vVH3eSv4Bts-2kx2EW1oLQ9KqQpbUe-cWn2Q35oi2rvmVgWE4Z8GksPA7eXt0B2Fh6tpZLfdYlHXqJ6cPphEbmsccLNjFq-b_9bHIVeEIi8xDAfkh3dOKVFoprdOaZGsrmDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این عکس نوشت : شاهزاده رضا پهلوی، ولیعهد ایران، با شرکت در مراسم یادبود سناتور لیندسی گراهام، به نمایندگی از ده‌ها میلیون ایرانی که برای آینده‌ای آزاد و دموکراتیک مبارزه می‌کنند، ادای احترام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19979" target="_blank">📅 13:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOcbN0lLV_Ilr5iUswFfoPlubZ6rfsKAll0Cz5MjvlKVvUQuoY-FFpWtmHZQm1jxO1Ct0tEwS3OBBPkqXb1TX02hBTkzWunuGm538zPRTcrOi4TFl5Kxbd4I8E54dwPRRVE0ztT-ri10nuDCByE-V4ujVbrk_suvjYhvRKICqwSJ3tb-P5oEUfSmmfbEmP-oDaOAbaio6-Fdo0Eon5yT0TGhY4dRK9BKwBmpQ4tV9vYm6UrI4Q_NXVdbLRqafp57DDDbfyW0_Zypj-6pQYW5qVuXxI5rIKH0bOnt5s8cHTCs66n1OAJMbCslOLlyjAKSZfduj3rONpeWfvrfGCXlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ حضور شاهنشاه آریامهر، ریچارد نیکسون، شارل دوگل و بودوئن، پادشاه بلژیک، در مراسم خاکسپاری رئیس‌جمهور ایالات متحده، دوایت آیزنهاور، که در تاریخ ۳۱ مارس ۱۹۶۹ در کلیسای جامع ملی واشنگتن برگزار شد…
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19978" target="_blank">📅 13:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏استیو استکلو، خبرنگار ارشد رویترز و برنده سه جایزه معتبر پولیتزر در گفتگو با شاهزاده رضا پهلوی و گفتگو دیگر تکمیلی او با بی بی سی فارسی @WarRoom وی در این مصاحبه به نکات بسیار ریزی اشاره و خودش همچنان اذعان میکند که شاهزاده را به چالش کشیده و وی خیلی مسلط…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19977" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏استیو استکلو، خبرنگار ارشد رویترز و برنده سه جایزه معتبر پولیتزر در گفتگو با شاهزاده رضا پهلوی و گفتگو دیگر تکمیلی او با بی بی سی فارسی
@WarRoom
وی در این مصاحبه به نکات بسیار ریزی اشاره و خودش همچنان اذعان میکند که شاهزاده را به چالش کشیده و وی خیلی مسلط و با تجربه به او پاسخ داده.</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19975" target="_blank">📅 12:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الحشد الشعبی: بر اساس آمار اولیه، دست کم ۲۰ مجاهد کشته و ۳۲ نفر دیگر زخمی شدند. این آمار مربوط به حملاتی است که توسط ائتلاف آمریکا و عربستان سعودی انجام شد و تعدادی از مقر‌های رسمی الحشد الشعبی را در چندین استان عراق هدف قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19974" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19973">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش‌ تایید نشده شنیده شدن صدای پرتاب موشک از ‌کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19973" target="_blank">📅 11:15 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
