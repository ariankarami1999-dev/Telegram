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
<img src="https://cdn5.telesco.pe/file/RAaJayT3WAfGucXPGu6W27Rmzumka1DVmQSoP9lgUJYjALrZS4GfSNlPUHLHXpITbMjY9m18xzJckvYHsI7va3qxO7uWNnlVmYUgh_tnlJtC5ZuzgpeeR4VvqczBdX0jpme5yxbJrtVvY5yfsAwG4UBuBjShXd6JfcTbSF7dSKfU0Pi6IIsYx-AZxgB0V4ZWVKBRKN4SdK_5cGJJZj4Txrp_JWpCGmwJ1QaH_ml6pYJGrESnIkwotdpvWdH48eHG3g_uAF_NaYi4PWK3dJYfEpmOmWKriMukHkf60qtBkbKBnMDgR5UFsmfkQARiJgRSOd2sgpEhSpTR_V_Tmx-2uQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 395K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-107640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753494da36.mp4?token=nOee6PDD_0OlJglGfNDxDDeuWordDTp8yx16Z8LpIlgg2SDjwZxiorqCkVk70SQMiRkAjldgbspHEXa9P-u9Vg_6Sy6djvl2zUJE0Pq4F6229_vf0zp0GskW1aeOGgEeeTVWXl__0PNQa4Nz1TmUKQ9Y_ehT_3DveMtK72zd8HirRL1EgJrTqXMnvKMjrVCuyV6aTO7lNQS_XLnGsQPVg5tSyDcHVq2slHDxdoe2ScMqHkLHpaxtiqAUngVtM-iLnismodG76nsOFxxMe5-1WJEszvqdKor7hPQ6shBR-pSVaRe-Hhidl-miBRpJv6sY-Wm_NcnHWBVf-FCrUeKZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753494da36.mp4?token=nOee6PDD_0OlJglGfNDxDDeuWordDTp8yx16Z8LpIlgg2SDjwZxiorqCkVk70SQMiRkAjldgbspHEXa9P-u9Vg_6Sy6djvl2zUJE0Pq4F6229_vf0zp0GskW1aeOGgEeeTVWXl__0PNQa4Nz1TmUKQ9Y_ehT_3DveMtK72zd8HirRL1EgJrTqXMnvKMjrVCuyV6aTO7lNQS_XLnGsQPVg5tSyDcHVq2slHDxdoe2ScMqHkLHpaxtiqAUngVtM-iLnismodG76nsOFxxMe5-1WJEszvqdKor7hPQ6shBR-pSVaRe-Hhidl-miBRpJv6sY-Wm_NcnHWBVf-FCrUeKZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به دانمارک توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/107640" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95be3e3e74.mp4?token=HVrxJ_DwnXk98WNwKiqGYbtKBqeTPXd2yVqo0J4XzSvuAhqalwlvw2ws4SUVPl3iIdJ9FwlSvYx5I9d8-GnFwCALnUvU-3k9qQaxV9DH-EOt-PNOvqukc4kMNCCGIyuEHfTOtSv37G4ctTJbwGECn2XGBCXa5pIqal-nxJt_P7112GYQb_p6ZiTV1IuW38I4gu2QVoqu3Fs0uU__5cmVbIhcnccc_Fw8v_jY-txTnxCvtT3VlX_X_VDzo2OWnQI_73ksovtSRk0RoEWrfF9uh35_2-Db9DRrAxnqnbRPJF82673Wba02aLygsOq1X2yTBMZzYt5PnMWmqj6Jy37O1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95be3e3e74.mp4?token=HVrxJ_DwnXk98WNwKiqGYbtKBqeTPXd2yVqo0J4XzSvuAhqalwlvw2ws4SUVPl3iIdJ9FwlSvYx5I9d8-GnFwCALnUvU-3k9qQaxV9DH-EOt-PNOvqukc4kMNCCGIyuEHfTOtSv37G4ctTJbwGECn2XGBCXa5pIqal-nxJt_P7112GYQb_p6ZiTV1IuW38I4gu2QVoqu3Fs0uU__5cmVbIhcnccc_Fw8v_jY-txTnxCvtT3VlX_X_VDzo2OWnQI_73ksovtSRk0RoEWrfF9uh35_2-Db9DRrAxnqnbRPJF82673Wba02aLygsOq1X2yTBMZzYt5PnMWmqj6Jy37O1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برونو فرناندزی که خیالش از بابت کاپیتانی پرتغال راحت شد و به خیال خودش از شر رونالدو خلاص شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/107639" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ژائو کانسلووووو</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/107638" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پرتغال زد</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/107637" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گگلگلگلگ</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/107636" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یونان یکی به هلند زد که آفساید شد</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/107635" target="_blank">📅 22:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp1YTIDtGsjJ_RfT5urIoGdcZHE2h0NWlsANjSI0MtHiAiQitkhKeFahjfvZPB4mjB4iFDgIE2olJY8fIlWxdwJqIa0zbekXEi04brioF0YVxBloueHD9AbPEJYHkfLKjyiHIeuR0wq-GC2cFBJJN4-BFq_UWNeAkniyTOc_GGKFWtfzPXpK2CnARbmD1HvJaVbU1ASLsO3N5EXmBHwZNTIO0AaTQX8gMkmhPSgF5QERrIwG76IRv7lELd_kPK2xShzOy-TFzn-kPiYASt9Z7JLHSIhxqnka_XMqMZUprpXv0xeEAEXyoaZd--u1kawVdwkOsPAKa1n8XjrbItTMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
شبکه رسمی رئال مادرید:
🔻
کارنامه آقای گواردیولا، آقای ژاوی و آقای مسی، همگی زیر ذره‌بین و در حال بررسی هستند
🔻
تمام جام‌هایی که بارسلونا بین سال‌های ۲۰۰۱ تا ۲۰۱۸ به دست آورده، زیر سوال رفته و تحت بررسی قرار گرفته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/107634" target="_blank">📅 22:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfqfJe8B63x6HbiNLWp5pJB0gVZa9Ka7umKdeMidA7HolLqsbM1ZdgU6phbMq7WasZums479Fn6ct9Y4Oqs8jzgSvuUpRi4WHeLWnvsOx7AG-0TfSHfUXyXH-056omAfqEB1knBT5ECveghZaU2uTpH2t6UcWshZsSedrnMv5ip_qzVzuCu2iwwtwlXgMgdECbFp_oz8EVwvS5jVOopvYZURsztvBBfXb6IheO-9We-J1YbKks4Rw2tWE_QkWlKzYUFQIb5MFwtiJLwtttPB_XDfXnErk53axNojhXu0xZMQmSsHg3q2ZemFilOQca3rZjcTstmt5GUrcWO7iHAAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
باسکال فِری، رئیس سابق تحریریه‌ مجله فرانس فوتبال و مسئول سابق جایزه بالون دور:
‏
🔻
در حال حاضر، و با صراحت، من از لامین یامال کمی تحت تاثیر قرار گرفته‌ام. و شخصاً، جایزه بالون دور را به بازیکنی اهدا خواهم کرد که قهرمان لیگ قهرمانان یا جام جهانی شود. این دیدگاه من است.
🔻
یک نامزد، کمپین‌های انتخاباتی را در تمام روزنامه‌ها و به زبان‌های مختلف انجام می‌دهد، فقط برای اینکه بر رای‌دهندگان تأثیر بگذارد. اما من با روزنامه‌نگاران و رای‌دهندگان صحبت کردم و آنها تأیید کردند که این موضوع اصلاً به آنها خوش نیامده است.
🔻
این بازیکنی که من به آن اشاره می‌کنم، خودش را به عنوان "انتخاب شده" معرفی کرده است و من فکر نمی‌کنم که او این جایزه را ببرد. و اگر برنده شود، با وجود اینکه من این را باور ندارم، این موضوع برای آینده این جایزه خطرناک است و باعث هرج و مرج خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/107633" target="_blank">📅 21:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a570eeee2d.mp4?token=kHw7vRlIKg02t8JaxuEvuMUAT5yat2ctzZp83pi-85K0mBXhhkvdn7dQymfMFnhMyEUbEcWML0uNwFRrZagC78js1I6WExp1sl9qcJXzc5Lh7ZAVqtXxGVycPQ_J6NkwMewCOYf5xPddnUpnmKYKC-m3V8mgyHmHmKyobDgBJ6JcwioftzkKvmuH2jql7v6bLlkXsaInRoZfnoHXOnlEC2gM4F9Qgrprn-OcIUZqd3Dg83EJLtNBB-5xDZ3bi7XwPQxXQuRPLogn16cl7LM57zcDlADdG9JvS-70FEvY5Gut3zE9eH7EfYOOJAB_J9Y0y3UqST2sGBxBwfMm8k7CkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a570eeee2d.mp4?token=kHw7vRlIKg02t8JaxuEvuMUAT5yat2ctzZp83pi-85K0mBXhhkvdn7dQymfMFnhMyEUbEcWML0uNwFRrZagC78js1I6WExp1sl9qcJXzc5Lh7ZAVqtXxGVycPQ_J6NkwMewCOYf5xPddnUpnmKYKC-m3V8mgyHmHmKyobDgBJ6JcwioftzkKvmuH2jql7v6bLlkXsaInRoZfnoHXOnlEC2gM4F9Qgrprn-OcIUZqd3Dg83EJLtNBB-5xDZ3bi7XwPQxXQuRPLogn16cl7LM57zcDlADdG9JvS-70FEvY5Gut3zE9eH7EfYOOJAB_J9Y0y3UqST2sGBxBwfMm8k7CkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
میلی گلد این فیلمو از طلاهاش منتشر کرد و گفت دزد نیستیم و پول مردم رو نمیخوریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/Futball180TV/107632" target="_blank">📅 21:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puY72KJz_sIQ-FrtHpPCtIcZzR-1z00qrz7MWsyQDV1rsvA-4CCwfbvdjK3YHNBD0wJcFM2Rp29sU1kZzEhiGKNcLTw04Hq4MG38Eivf6R7txFZ3K4nwF5TL2O_3JIiVT2VKE-60pMAy79RMKFvzbcS1yShSb5j7dUB3sCVV8BeCQXLUGxdIY1ZomCs-pUu7Gc0c2miWy5aMjYiqbISg9IfhuzPtdBeYsgM0NKFNknBen87OfNxXApRCGjU336BwqsItvJ1lMSvHVKBEitr7e8aCe0f82fosbvxLm66IANx4MSJhYBDR2TojuyIXB_CD9vCDGoYFyYV9Hs5azPAjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ترکیب آلمان برای دیدار با صربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/107631" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107630">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇵🇹
ترکیب تیم‌ملی پرتغال مقابل دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/107630" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107629">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ot25-ZCpXiA_-xvY0yK80v72yipxMe25nXsFSa6KDrqsjHHNrK054CBcbakhZVX1CT45R533IkWpVd92dLO20IsRaFbqJnBloD4vnTmX-4-LDn01zqA9JhnUmuILUw81bRNNeozNZ-OuAMGhQCxru5O5U47aXjhbtnT6Zznbe2LOf-xNTIM47Gw0CBIRYx69V3SyxcmWtztUaPAuCLZveq923KPeeyPeLapqeECL4So19oa0uujpNqmbjHX53_iJ_pjhII4tnzCL6UD7N9MgYomAAK-bueQkrm2nLTnGofG2VsEY5UKJ-MGg3RQ1Ys4heVYMEiJQqNByuBMMQJijvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب تیم‌ملی پرتغال مقابل دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/Futball180TV/107629" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107628">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehB5DJ4pQr0n4RajUxj1xdbyAzx9D7_gYRmX_Zt76KM6e19zQsmyJQ1Rs1-9VY6LTNsKqfpiF-7fBeqUASIevcEujimP5kVCIGbONo2ZcK5Ko8qZT7taJEDs30Llbl3jImv1KBPIAqrnKFH9ZpVQKYBsGtzjnwQ1Lyu8uJ-a4bNgmtPLQB2TEYl7yP84z6YF-WuSYMetQGf74vLQjV_WWuv0TxpRy94u5XiuudGxxDQgYeyO_eYxhJXo08kaamV3CNO5AwyN7SCfRn035vPVjNPunqYa_1ukaLqxYMmdi4qH4-t1fK5xZQL4dY2gxEps83pQJ8v4ZfaAL9oFHhB3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیونل مسی، مالک جدید باشگاه اسپانیایی سی‌دی الدنسه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/107628" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107627">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b37d3dc9.mp4?token=d4KjpVJ-1xey2Krxbm_g0rHINFOq5EnENEchhHneyt2WQOs0a6_Fh-CB8_LeXy3y77U4jb4foj4z8PKj6Be0Md8m9NxeynUuC4_4AS3Sc3AmVRiJzTEkIWaI369jBlWzesM3vuVOAgyhyLJ6RjkF4bijaHSaxj2rICJayVf7UoRnDHNbjVVnoZEHmqWgf4El_jkpFqHShYs1H1dS3rZXxHX_08oJH_ii7C6F_ftFMNaszB6as8TltYBpLHbJz9LBK-zayxbaoZKOrnd5p11U_I2NwasSIBRiy6z_VB1dXcxFiVIRuZKaHjdeBSino7UY3rSTrLp0ajnPoc0bLwJNag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b37d3dc9.mp4?token=d4KjpVJ-1xey2Krxbm_g0rHINFOq5EnENEchhHneyt2WQOs0a6_Fh-CB8_LeXy3y77U4jb4foj4z8PKj6Be0Md8m9NxeynUuC4_4AS3Sc3AmVRiJzTEkIWaI369jBlWzesM3vuVOAgyhyLJ6RjkF4bijaHSaxj2rICJayVf7UoRnDHNbjVVnoZEHmqWgf4El_jkpFqHShYs1H1dS3rZXxHX_08oJH_ii7C6F_ftFMNaszB6as8TltYBpLHbJz9LBK-zayxbaoZKOrnd5p11U_I2NwasSIBRiy6z_VB1dXcxFiVIRuZKaHjdeBSino7UY3rSTrLp0ajnPoc0bLwJNag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوضاع فوتبال ایران با این آدمای لجن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/107627" target="_blank">📅 20:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107626">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d318c00047.mp4?token=gDSvvQf2QPtwQIqxmHz3Wihni54zKRIv-8Qinqv12beHLKX4vvsxpQp9w2lgzBmVK5JNKlCtqcOA-W95UWGyk_f1-siBS9c0NtnGlq_8ve6x0BAIrAMDrsYt2Z3zCrlM_muVDH_S6NMUh-tkrapOOKajel0HRqRlduZrx-zI6CMC8KeEGHnmm7SpUxzGPXhTvVNlWP_MD2LpFYz57lf9fqd0Yt6oDEHECIu4_a5R6MjTtIZ7AwRIFRJN_ySYFw1I1QD1we9Lb86oy1HwuiHSOMGx_jXqVCF76qfvCPU2bx8ZxCsOyrj9VsxxuELZtpbgVY8TfamOO8jNI937AwSeeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d318c00047.mp4?token=gDSvvQf2QPtwQIqxmHz3Wihni54zKRIv-8Qinqv12beHLKX4vvsxpQp9w2lgzBmVK5JNKlCtqcOA-W95UWGyk_f1-siBS9c0NtnGlq_8ve6x0BAIrAMDrsYt2Z3zCrlM_muVDH_S6NMUh-tkrapOOKajel0HRqRlduZrx-zI6CMC8KeEGHnmm7SpUxzGPXhTvVNlWP_MD2LpFYz57lf9fqd0Yt6oDEHECIu4_a5R6MjTtIZ7AwRIFRJN_ySYFw1I1QD1we9Lb86oy1HwuiHSOMGx_jXqVCF76qfvCPU2bx8ZxCsOyrj9VsxxuELZtpbgVY8TfamOO8jNI937AwSeeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🇷🇺
پوتین:
اگر حمله‌ای مستقیم توسط ناتو به روسیه صورت بگیرد، از تمامی تسلیحات متعارف و غیرمتعارف (بمب اتم) علیه آن‌ها استفاده خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107626" target="_blank">📅 20:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107625">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8054bb57.mp4?token=Hjwt_r5N8s9V5-AcmpBfhQcBSNyZZexWxagB4KCjUANHReQVcF1x8BmRz4hRhRIYFFT2ebsgJ2WP-yaqTqhVpa1_vgvW5FM2WWxd1VnGvV2LFsbV5iuwyMTiDuzQhMWrL3fO8lZ7m-_kLGtGlpA63cLtK3mW8OFbxf9ZY4WsgwLee_6zEyokZtmEjy7SlZli4FmNDZSRsX6jZyuZtgA1Jpq_BwSvQe4W5RGIQAXbpJ378xkruJX7XP6Tcwyjp9RajeRoajJex22G5XlpFiJVvOFy0WZxje7GYaDMTi1vlOrnoesmoXQcLKj2lIe3_PHPZUH4yEnx1_Emt68wteOlVwHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8054bb57.mp4?token=Hjwt_r5N8s9V5-AcmpBfhQcBSNyZZexWxagB4KCjUANHReQVcF1x8BmRz4hRhRIYFFT2ebsgJ2WP-yaqTqhVpa1_vgvW5FM2WWxd1VnGvV2LFsbV5iuwyMTiDuzQhMWrL3fO8lZ7m-_kLGtGlpA63cLtK3mW8OFbxf9ZY4WsgwLee_6zEyokZtmEjy7SlZli4FmNDZSRsX6jZyuZtgA1Jpq_BwSvQe4W5RGIQAXbpJ378xkruJX7XP6Tcwyjp9RajeRoajJex22G5XlpFiJVvOFy0WZxje7GYaDMTi1vlOrnoesmoXQcLKj2lIe3_PHPZUH4yEnx1_Emt68wteOlVwHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتایج بیلدآپ کردن امیرخان در تیم‌ملی
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107625" target="_blank">📅 19:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107624">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce141f49b.mp4?token=WP_xWQpaDiDtlKyflesm-MshGAmZnIjyY5tergXzcfHPHJmolbnZ3tJIqMJvxcGu0AKfZpVcMnwUZ-zLruEQWqE21DBABSnPda8GDiJWhmAKL2CwjrnzXPKOUb1IVyKIGMMQm3r3ThdqBtyouqtwIuUSgcW8f4nn5e7WNmBPmvOAyl7q7_Y1MREEj4yLrF4U2vPCKlPLdF60hGX2_FQCN9f6vXKGubqQ9eGWmzKSDMcpU4jJ0Xs4LwVbxoov7N67js5f967Mhw-Df_PTvVsL7awFa9kkB4K_A2sad84Re4tWGKI05u42VjMuxuEdbfM8CrFr-kIvZqN2cLRIKRUvZzpFZFB20D9cM3LPyfEkmn_Eu_dBBNqN7KJ_4Ihzafs09UNa0wo8a-PVRBA-7vidB189jG9fWEE2I9AWlfyJ5NdJuj55ByyJoqOh2-gOHkfQI9wmYyRUXBiQYRPA378L7-QA1EMZUYDZch4TU3SR7v2xksyCYBsAP0d_9tdyPtSl-mViI-x8CXZRpd_lfO7NIS9Nkwh0UaZDus-8sZCFThM8L1g-u2qJDg8bu3VCmSA3mK2qdU6skuD3loltiiFJz__jHJO2x7JxTLazJB0w-gVV-vf1T8RfUAul_6TyUGGI4-hBXNATsoIkD2kpZf2ICNHacuk9hLT9MDZ94CtswUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce141f49b.mp4?token=WP_xWQpaDiDtlKyflesm-MshGAmZnIjyY5tergXzcfHPHJmolbnZ3tJIqMJvxcGu0AKfZpVcMnwUZ-zLruEQWqE21DBABSnPda8GDiJWhmAKL2CwjrnzXPKOUb1IVyKIGMMQm3r3ThdqBtyouqtwIuUSgcW8f4nn5e7WNmBPmvOAyl7q7_Y1MREEj4yLrF4U2vPCKlPLdF60hGX2_FQCN9f6vXKGubqQ9eGWmzKSDMcpU4jJ0Xs4LwVbxoov7N67js5f967Mhw-Df_PTvVsL7awFa9kkB4K_A2sad84Re4tWGKI05u42VjMuxuEdbfM8CrFr-kIvZqN2cLRIKRUvZzpFZFB20D9cM3LPyfEkmn_Eu_dBBNqN7KJ_4Ihzafs09UNa0wo8a-PVRBA-7vidB189jG9fWEE2I9AWlfyJ5NdJuj55ByyJoqOh2-gOHkfQI9wmYyRUXBiQYRPA378L7-QA1EMZUYDZch4TU3SR7v2xksyCYBsAP0d_9tdyPtSl-mViI-x8CXZRpd_lfO7NIS9Nkwh0UaZDus-8sZCFThM8L1g-u2qJDg8bu3VCmSA3mK2qdU6skuD3loltiiFJz__jHJO2x7JxTLazJB0w-gVV-vf1T8RfUAul_6TyUGGI4-hBXNATsoIkD2kpZf2ICNHacuk9hLT9MDZ94CtswUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین کم مونده بود اینو بلندش کنن ببرن ترکیه با سرآشپز معروف ترک‌ها ویدیو بگیره
‼️
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107624" target="_blank">📅 19:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107623">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seJhjbVmc9_rHRdSLR-nTssEllamebVXqWN87wQe_R5T_lboRjzXxs8Pf4v53rsntIeelJ7cf2OGWT6DndKpIeeSAyv-pjjOlgY3av893l56Y9OOxSCmxDB0_0mUFb-EEp_Azl89-jWKwn32LCBy19y4TlcLm2F861BLUDEf_jPzuTDST_pKPn4Ru9ieNzQQi89HyuOumPt8j_btN7P4vFHpOKoI56z5GYufTFISEUttMc3oXoV0P94oww2OfCOz496XfH487K7-qZhM8cPWnVaWTdTZULXSFT9AnEUZIWyLxk1TVvM_jru2tuc9HeCOm2fnce7HjZAoT7DhzXsQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اسپورت:
🔻
باشگاه بارسلونا تاکید کرده که یوفا فقط شکایت رئال مادرید را دریافت کرده. برخلاف آنچه در رسانه‌های مادرید مطرح می‌شود، یوفا اصلا از آغاز یک پرونده تحقیقاتی صحبت نکرده.
❌
یوفا همچنین تاکید کرده که پیش از صدور حکم از سوی دستگاه قضایی اسپانیا، اقدامی در این رابطه انجام نخواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107623" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a15cb946b.mp4?token=ER4JCsEeS-W69FqnhPbLXMjcggYiY1F5oeYQX46x83M8bS9V9nu4N44qHmCUMfPWClMGRiDgA4KQZIywfCf9-hhbehON-T9W9tPoYIdCDjhhBd3PaDB_fDPieWgb6bDBTWGFlpUmWu9THVBP6npYtoK4i_15rObsVT87dRmBy-9hzi-wW_2-ilC6_EfR2_Yg_4aL8rfG-tTg1UmPcgY2fuYfkU_P8n4cYJ4upmXbSHPV5p_zM2AuSXJl6IySGpPvly94b58CG--hC3gHP2_r-VQ_TMFGcyH-VmFupi1lgd7B_9-89lQrrP00tTM2mHHUJgM-epEh4BpqstJGXe6eLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a15cb946b.mp4?token=ER4JCsEeS-W69FqnhPbLXMjcggYiY1F5oeYQX46x83M8bS9V9nu4N44qHmCUMfPWClMGRiDgA4KQZIywfCf9-hhbehON-T9W9tPoYIdCDjhhBd3PaDB_fDPieWgb6bDBTWGFlpUmWu9THVBP6npYtoK4i_15rObsVT87dRmBy-9hzi-wW_2-ilC6_EfR2_Yg_4aL8rfG-tTg1UmPcgY2fuYfkU_P8n4cYJ4upmXbSHPV5p_zM2AuSXJl6IySGpPvly94b58CG--hC3gHP2_r-VQ_TMFGcyH-VmFupi1lgd7B_9-89lQrrP00tTM2mHHUJgM-epEh4BpqstJGXe6eLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری پشم‌ریزون حسن‌روشن پیشکسوت استقلال: فصل‌قبل که استقلال در کیش اردو زده بود، ساپینتو هرشب تو هتل دختر میاورد و وقتی تهران هم بودن داخل سعادت‌آباد بساط دختر بازی راه انداخته بود و هرشب با یه نفر می‌خوابید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107622" target="_blank">📅 18:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107621" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107621" target="_blank">📅 18:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po1A8T1Vu7z6TGdMbOoh9SQ8CaTgddz6x-H6BIlLAZs4NAASnQ3aw0cH6j24lk-Skg0dpQFTOy0iUnrb6cyxANK7X9oNQvSdaNLco29Z-Re79Z5NxEcLvlPnaq2utx_VnXaqXeqynSj4Atv8SJE4u8brzccKDlMw57qxv9-Omtb1pE98_wLTDCOqsEBH73ostmN6HbnFqBJkFZCxkx0zkfnKZtbTgLrJHy89qVoS52dyHxitUe3cZ-qJPpZqsbxwOZr7FPbyUjbQAY0pKakHJgzu_EypDz1HnUOJHVDkk4mxWEZRcNr-d5sORv9a9Vf6TUJOeTyhLSMcwuflER7-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز پرتغال
🆚
دانمارک را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۵ گل زده
دانمارک: ۲ برد، ۲ تساوی، ۱ شکست و ۱۰ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107620" target="_blank">📅 18:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107618">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
❌
🇪🇸
🇪🇸
فلورنتینو پرز به اعضای تیمش قول داده که در آخرین دوره ریاست خود باید تمامی جام‌های کسب شده بارسلونا در قرن بیست‌ویکم را پس بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107618" target="_blank">📅 18:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107617">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3ymfZy8hx_qH8d5udXMDUoVz7NpiQRXjzc2fpogrrVyycUxNRhOYbMyNAW4WJDyuTopz9YrnioFLRFKXGTnyIwJnty-pztDxQ9R6HQUKrFHyUA69vORom-ZZHZNZ1eG7OV22tc59mwck_8ywtMGIVRPUWXfkpkIsqD3LUm2_qvARhmYWwTOqQ11dIL2ACAsqJt5b4qJK2UfHiIGtOauVVybQLWuNGxRKHHgcw5UKWmtm1plSz98F5rtnU7srBME6YwFiqizNAg5sHncXVuIvwerbPLRmkUy_jZJFiZbUERZkNe9fA0xz-2ewqTvSG8KvjQGChK_Y8o2Dwajcap8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!  محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107617" target="_blank">📅 18:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107616">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgf_nVfIPLOgVDTztqXTDp204BRydraw1s6XGkOerbAnORX8wZzk8cX7HF6Wh-HwYKbyTGBqunmseHZZj-kk6f-jJm82a7BDoxQd41EVqeWwCaS6M-nk9Npa2jpLeEYPDJp_aoaQWPZy-5pz-359-zSp9sfWZWlMqqV7qOR3QvlbyQWTqWA3uEGn21ZZQdKbyqrO7YBoU8izZY9uos1GO_2p_IkL5NMZjgU3ArspgQ_DMsrqxALk9XAtll-c5uAi89U4LH1jdLEumZegs24HGkbw0GjnVDgA5hkrs21hPaM1fCEfwO_Iohq1fKKN7kgCKx66hXS10H2Hx6vfdwF-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🇪🇸
آاس: رئال‌مادرید بیش از ۵۰ هزار صفحه مدرک علیه بارسلونا در پرونده نگریرا به یوفا ارائه داده که برای حد فاصل سال‌های ۲۰۰۱ تا ۲۰۱۸ است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107616" target="_blank">📅 18:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haCSLmnv361j2c3EnF8tMpznJeNKWukzMqBtXLaETTWvAu-Ssm-UMvqk93_aQBf7Zeidf8baZQH-TDJIaQPbqMJFUA562C5YUXePf5rBk_pr34erAOxM_2AOS6vXZDm7sdtFvuow6c05TwsVNzAF6p2eXdq3bXIL62c-MeDWQpa5zOvTNDG-DXyprgSl7TD9za3YmUizqp1i5efYAkXGN2cPmv4LSvYxjCq7XHNT8zgUVNO4srmrXBrCc9td35PyHDvks5vBdLX2lPocWsGvN2uE9NXDn6aaPdxZVb-CZo8N7J_YEqd9RwnqbHKjGEpDsE_aHXE3_o_H6W15zZ95YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
یوفا اعلام کرد که حجم قابل‌توجهی از اسناد مربوط به پرونده نگریرا را از باشگاه رئال مادرید دریافت کرده.
🔻
این اسناد در اختیار بازرسان اخلاق و انضباطی یوفا قرار گرفته و در چارچوب بررسی‌های جاری پرونده مورد ارزیابی قرار خواهند گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107615" target="_blank">📅 18:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107614">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Empd0Z7FttfU3_35rEtceYe5giyA9Zr3L1LDIsiPy7H7nFR39zRWXLrW64O_Bk6BpXsytjG8ORrp0XTR61hGHRT0k1SFNLqDNylJ8YLjE5rGioi-zoCxOda8dPGhjVfQ0efvfhKCmn3QHG3_o-3u4LDGs1QhCrM9wby1vrvLR-Bwhsb732x00cfk0-_061L6yg25rIRWm7XwZ6a0vj1IKhDJCGZClhYOFXnVFFSaTUXebv7JRZvWODGe8dNV76o9zGfNkOVQhbyLmoC67asBJbU6oI2pJ6DIx_VVSESOz2DBG-of2VabdUMhqkLv0QsKPsT8hgsGbEo9Ctr_4U2g2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
یوفا اعلام کرد که حجم قابل‌توجهی از اسناد مربوط به پرونده نگریرا را از باشگاه رئال مادرید دریافت کرده.
🔻
این اسناد در اختیار بازرسان اخلاق و انضباطی یوفا قرار گرفته و در چارچوب بررسی‌های جاری پرونده مورد ارزیابی قرار خواهند گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107614" target="_blank">📅 18:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107613">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015e854338.mp4?token=iHiprSvX1hJAT-DuIMVjlky7l4fuAIbTNi4pZm4D2pUJ2t6nuszlEOj89PC7U26kiE_Lh8oPpwrlrMFNVkzJwWbP-lQQwG9V5Na4h4y52NlZpbvDZuyAB--uengqDcieZzSFfyWF-63VUzF5Tw6VVkc_YZAr1G9mY0gVUPBAPlCeL8wufWypZWng2MDO9ERDM-4Ba9OB3nNoz3nAAjxP92qwHC6jnC8ptwwVW4FsRDKtowRmsYT-I4-xkvSCPbiino4795GkPi2T7JpCS6Duz8o_o-KNBj0XQj2eZtk-kB8L7vzTry5FMh3W_wns8XGgK7POp9f7TKjCa7jKEGXdxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015e854338.mp4?token=iHiprSvX1hJAT-DuIMVjlky7l4fuAIbTNi4pZm4D2pUJ2t6nuszlEOj89PC7U26kiE_Lh8oPpwrlrMFNVkzJwWbP-lQQwG9V5Na4h4y52NlZpbvDZuyAB--uengqDcieZzSFfyWF-63VUzF5Tw6VVkc_YZAr1G9mY0gVUPBAPlCeL8wufWypZWng2MDO9ERDM-4Ba9OB3nNoz3nAAjxP92qwHC6jnC8ptwwVW4FsRDKtowRmsYT-I4-xkvSCPbiino4795GkPi2T7JpCS6Duz8o_o-KNBj0XQj2eZtk-kB8L7vzTry5FMh3W_wns8XGgK7POp9f7TKjCa7jKEGXdxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اصطلاحات مثلا تخصصی الهویی که باعث بگا رفتن تیم‌ملی و قلعه‌نویی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107613" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107612">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2985c6ba3.mp4?token=DstI9fEOQRwClyPWCuV2wpyGupmTGhazpRYvR19O7c0LmghwRdmjnjZCd2yU9fFRfekbRUAcfBkqxVsE_zcdc4wcj4goN3ArCT7jvzm2hYsocB3fFt5FbVm27L2GvKwkdL35jiDoio1t-WxHSdHitvBwBFj6-f-4cC_TX-3O6vBLUoSATh3VN15se3HJxOO15ljfe_r7xiQXip2a-dGscWpWDHfAn9So8Oew3cn7KYu6GxulnEyCGT0fa3R-5bXpfMr0eRCHAUXSSoVDtjrwnc_I3Ukx581JHSug6noLhk-yHmx44-K9NdW4txpbnyR44gXv9Zlzm9tYdwaZwvAhbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2985c6ba3.mp4?token=DstI9fEOQRwClyPWCuV2wpyGupmTGhazpRYvR19O7c0LmghwRdmjnjZCd2yU9fFRfekbRUAcfBkqxVsE_zcdc4wcj4goN3ArCT7jvzm2hYsocB3fFt5FbVm27L2GvKwkdL35jiDoio1t-WxHSdHitvBwBFj6-f-4cC_TX-3O6vBLUoSATh3VN15se3HJxOO15ljfe_r7xiQXip2a-dGscWpWDHfAn9So8Oew3cn7KYu6GxulnEyCGT0fa3R-5bXpfMr0eRCHAUXSSoVDtjrwnc_I3Ukx581JHSug6noLhk-yHmx44-K9NdW4txpbnyR44gXv9Zlzm9tYdwaZwvAhbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🥈
اولین تصویر از رضا علیپور پس از کسب مدال نقره بازی های آسیایی: پارتی من خداست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107612" target="_blank">📅 17:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107611">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e174f30bb3.mp4?token=KfmZm8_BjPM3K_vvPsNduHOZlOPn_HHZEEs10MmvuDZ5P9dSqOzMSSCcedQKUGClLAnYT5cqRWszVFyKS5wcIfjVoxju9VwnATJeggcCkmoE1dEjNKitIWCw3NoWZm3vk48d3-_wx5BniI9DnbQWoW3dsUqQaDVp0LeAdHpsASKdLaVhuE7jckgq0HFnRJRYvwaAfuFH_Bew8OVLKPk-4aEtY7_F-raOWPjM7I9ukLs97Opnc5iZmbtzoIRXdfVCazT7E68NdJ1jcbhh4iX8GTMPkmYLRb4LKnyAHui9s-Oq0NdY-1HSM-6A3IoALCIUQEWe3xEaP2-KiG-iivS7tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e174f30bb3.mp4?token=KfmZm8_BjPM3K_vvPsNduHOZlOPn_HHZEEs10MmvuDZ5P9dSqOzMSSCcedQKUGClLAnYT5cqRWszVFyKS5wcIfjVoxju9VwnATJeggcCkmoE1dEjNKitIWCw3NoWZm3vk48d3-_wx5BniI9DnbQWoW3dsUqQaDVp0LeAdHpsASKdLaVhuE7jckgq0HFnRJRYvwaAfuFH_Bew8OVLKPk-4aEtY7_F-raOWPjM7I9ukLs97Opnc5iZmbtzoIRXdfVCazT7E68NdJ1jcbhh4iX8GTMPkmYLRb4LKnyAHui9s-Oq0NdY-1HSM-6A3IoALCIUQEWe3xEaP2-KiG-iivS7tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیو جدید لامین‌یامال و زیدش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107611" target="_blank">📅 17:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107610">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خلاصه مقاله جاناتان لیو‌ در گاردین در مورد ابعاد ژئوپولیتیک پرونده منچسترسیتی
🔻
برشی از متن: شما به جای ابوظبی(مالک‌ سیتی) و عربستان سعودی(مالک نیوکاسل)، به راحتی می‌توانید جف بزوس، عضوی از کنسرسیومی که اکنون تقریباً ۴۰٪ از سهام باشگاه فوتبال لیورپول را در اختیار دارد یا متا یا ایلان ماسک یا بنیامین نتانیاهو یا دونالد ترامپ را بگذارید:
یک طبقه کامل از مردانی که هیچ مرجعی فراتر از خودشان را نمی‌شناسند، کسانی که به سیاست و تجارت و ورزش و فرهنگ همیشه به یک شکل نگاه می کنند: بازی‌ است که رقیب باید به هر وسیله ممکن به زانو درآید.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107610" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20411da1e7.mp4?token=fATn8rqdh1-s4GkByFtIwjrXKytrHY6y1uC_KcFead5jaZuat9H_GgX14Nx-8ZFXZuQVRv0TOghic9IAJzKUlLQTbSoZuwxakbomY7cH2-vGFtRR3rZ6Uj7hUgLVmvbZOWTlwr1bsMwjYMeFGhSwX0muo1UneJUT07-QP8LDbhUfPa19tXFQiQPjlQm36L__JvlHXdT8yME0b44UpOl3injkiVd9sVR8YTKuuupqwrssx-QucwQC6zceGLzNYdbsEpPkxyy7-v9BQmmeIiPI3sJFGNHflYXociJNn6aVv3OEln3dR8390rv8hkONYu46ztSwmJ18ypHHEwDCwKQIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20411da1e7.mp4?token=fATn8rqdh1-s4GkByFtIwjrXKytrHY6y1uC_KcFead5jaZuat9H_GgX14Nx-8ZFXZuQVRv0TOghic9IAJzKUlLQTbSoZuwxakbomY7cH2-vGFtRR3rZ6Uj7hUgLVmvbZOWTlwr1bsMwjYMeFGhSwX0muo1UneJUT07-QP8LDbhUfPa19tXFQiQPjlQm36L__JvlHXdT8yME0b44UpOl3injkiVd9sVR8YTKuuupqwrssx-QucwQC6zceGLzNYdbsEpPkxyy7-v9BQmmeIiPI3sJFGNHflYXociJNn6aVv3OEln3dR8390rv8hkONYu46ztSwmJ18ypHHEwDCwKQIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
دور دور بیژن‌مرتضوی و زنش در تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107609" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107608">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a1969c57.mp4?token=ONzQLy-uQoNbgGzpmgFSR2qS0UX8t0Z3c_IV_AiBzYEFNCkZVDsRtNEQoXLHRsk-cEbEGqi3F_cL6NaXbEvf-eAunQNZFGLCRokgkknZxJKhmtdNbaHL8FDDE-QI5Aqk_MlwIBdJyhyIuBdXDqGYAdhGqewxYzwfcU-mFCT-kpn5zIWgX-oa6CmMbpA7LEvCpptf9IqRKugBpnlr9mrb4JJzKdn6T7mmlm2ys1tCGynF4IuKjJODGViHEAcguAYJf3eiWOYIZZwiWQ714P_udWe-SBhd87FJNmnCTV_LFumBOOGxQJG_WnTO0iYovqOQmFJ1Kou0XQDmmBxN5oSvbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a1969c57.mp4?token=ONzQLy-uQoNbgGzpmgFSR2qS0UX8t0Z3c_IV_AiBzYEFNCkZVDsRtNEQoXLHRsk-cEbEGqi3F_cL6NaXbEvf-eAunQNZFGLCRokgkknZxJKhmtdNbaHL8FDDE-QI5Aqk_MlwIBdJyhyIuBdXDqGYAdhGqewxYzwfcU-mFCT-kpn5zIWgX-oa6CmMbpA7LEvCpptf9IqRKugBpnlr9mrb4JJzKdn6T7mmlm2ys1tCGynF4IuKjJODGViHEAcguAYJf3eiWOYIZZwiWQ714P_udWe-SBhd87FJNmnCTV_LFumBOOGxQJG_WnTO0iYovqOQmFJ1Kou0XQDmmBxN5oSvbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
حنیف عمران‌زاده مدافع سابق استقلال:
من توی دربی که چهارتا خوردیم هم بودم.
آرش رو گذاشتن وینگر که فکر نمی‌کنم اصلا اون‌جا بازی کرده بود. حالا دلیلشون چی بود؟ این‌که رامین رضاییان هی نفوذ می‌کنه از آرش بترسه و جلوی نفوذ رامین رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107608" target="_blank">📅 16:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107607">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e980239cb3.mp4?token=LY0DM09-JxmscmmHKyg_l9_esk4EUBCsUwu6nLvDh6IQnrfmzSzLxIV4hOyvCIQ0ySq9STH1kVjmnq0W2Y7eh2ycpIX07abVJr6EMYadamHAYtE-5lnKjxRpzwvAeXiGoQFzqQvN097F3HrnUAEACuXGZPS33CJmqDRtLYmJuUGcqGdZdlFFSdl5Xe9rYCQyP4ewKJx6lzYqWb13OhCViFLN4z2ZpmNw-EVQ-AZRidoqz5QePelh9v5UxqUuzw8ZwiS5nCQCG6C9EkzrTqaJtJDGe1ZTvtV5iA2DTzlu44YteRzTT2u_MR4Iy7cey5K4j4DmF99Db8Ev4JSFzCET5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e980239cb3.mp4?token=LY0DM09-JxmscmmHKyg_l9_esk4EUBCsUwu6nLvDh6IQnrfmzSzLxIV4hOyvCIQ0ySq9STH1kVjmnq0W2Y7eh2ycpIX07abVJr6EMYadamHAYtE-5lnKjxRpzwvAeXiGoQFzqQvN097F3HrnUAEACuXGZPS33CJmqDRtLYmJuUGcqGdZdlFFSdl5Xe9rYCQyP4ewKJx6lzYqWb13OhCViFLN4z2ZpmNw-EVQ-AZRidoqz5QePelh9v5UxqUuzw8ZwiS5nCQCG6C9EkzrTqaJtJDGe1ZTvtV5iA2DTzlu44YteRzTT2u_MR4Iy7cey5K4j4DmF99Db8Ev4JSFzCET5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
صحبت‌های شنیدنی و جالب احمدزاده درباره اسطوره ملوان مرحوم سیروس قایقران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107607" target="_blank">📅 15:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107606">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBgVzbkqrld-4jtezHizBLqTsml2uUINC995P79Dv-rhy4jFJqpJ4JrDxEXGZWuGtIUNy-VoYsCgHJ7x7PbV6cxT0GtrYbzMM4chyqkncfYRUlSEzlbdDH0pxZyQ5tIXi-0J5s46AKcN7UEsZNBUea3SLmyTyumj_GB4y-36R5HJHgMsL6wqqwuaec7l9hhTiPeFDkcCJd8-uBps7nIzUD6o8kmQt08hvmpCF6BOTnhtpJzgOiYjovMaHLoIUEga9k5o8sosF0dslimEqsn7XhcElPr1ylspwNiONuAZBmGLOxeBR6QfPAP2Rdqa9aM8jqNUaRjuf3r9S35jMop8pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس دیاز: کادرفنی رئال‌مادرید تصمیم گرفته که کیلیان امباپه مقابل ویارئال به میدان نره تا با آمادگی کامل به استقبال الکلاسیکو بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107606" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107605">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5204393f.mp4?token=HZSAaozttveWV5qx1OLU-cZklZyVO4jV9Rpzw9VF_GMRWu4U58XgFlcictjvh2IJQlWUXn68-rXuj2G-40fmoFtclF3dFGk1w1zFrnwC8-eWrdxO273U0FriNUgJwW88pQZ-uBa994Jf8UI1dnb1JrvBmg5CICLC5XDCvAJhVfyKM9pjcv2JHYPHkChcaYixjjsUoGxK_5eH4NMLDqv1oWkSVJZQDkkDYqJI9DPE6Qvl2vVSq17-Uxtfp9mN0cDwljzOHORzqm2ORBlvXBs1hxhbD0CQllUZrInpYXaoTCIwUsAUuKCCfFW72M-vZlTovQZg2WQyUjv5U5uqQxG6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5204393f.mp4?token=HZSAaozttveWV5qx1OLU-cZklZyVO4jV9Rpzw9VF_GMRWu4U58XgFlcictjvh2IJQlWUXn68-rXuj2G-40fmoFtclF3dFGk1w1zFrnwC8-eWrdxO273U0FriNUgJwW88pQZ-uBa994Jf8UI1dnb1JrvBmg5CICLC5XDCvAJhVfyKM9pjcv2JHYPHkChcaYixjjsUoGxK_5eH4NMLDqv1oWkSVJZQDkkDYqJI9DPE6Qvl2vVSq17-Uxtfp9mN0cDwljzOHORzqm2ORBlvXBs1hxhbD0CQllUZrInpYXaoTCIwUsAUuKCCfFW72M-vZlTovQZg2WQyUjv5U5uqQxG6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
استقبال خانواده بیژن مرتضوی از بازگشت این نوازنده در ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107605" target="_blank">📅 15:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107604">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/297bb4ba61.mp4?token=VDcPwXzMRw7Sts8eSg8_SHLSpr-26yDL5rEIbObADTwr6hN1sj2IzWaX3-m4m5NhUCSFt61FZzXQT5mKCti5FfPXsRETHoo5WsjvVIH529qL8d9_Bl4EiDoNZ2anecb0DFEXDo7foGgf22dprURx8evFBpjNUamF-bU2tMzluY1QY9IoIDXTh-CTwco7qdb3GsdnMtD1_dSRvPPl4S0Wr-gBUVLFxzze3EXhQMHAgT1_WsMkE7TsZ0I3LuzYdQVPAsnV5sbVYC5P8EtuiJWu3hoTyYxxiceZqqrQTXfNDnVMW8r62AOE0QK5K5VXXbShxlzLEBkPfLVF_dQ3OW5wdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/297bb4ba61.mp4?token=VDcPwXzMRw7Sts8eSg8_SHLSpr-26yDL5rEIbObADTwr6hN1sj2IzWaX3-m4m5NhUCSFt61FZzXQT5mKCti5FfPXsRETHoo5WsjvVIH529qL8d9_Bl4EiDoNZ2anecb0DFEXDo7foGgf22dprURx8evFBpjNUamF-bU2tMzluY1QY9IoIDXTh-CTwco7qdb3GsdnMtD1_dSRvPPl4S0Wr-gBUVLFxzze3EXhQMHAgT1_WsMkE7TsZ0I3LuzYdQVPAsnV5sbVYC5P8EtuiJWu3hoTyYxxiceZqqrQTXfNDnVMW8r62AOE0QK5K5VXXbShxlzLEBkPfLVF_dQ3OW5wdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
✔️
🎙
مهم‌نیست در چه‌تیمی فوتبال بازی میکنی؛ مهم اون انسانیت هست که یاسر‌آسانی به خوبی در ایران به نمایش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107604" target="_blank">📅 14:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107603">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc7d01e79.mp4?token=EGVvlolCYMCXkgHTFxX055Tvsm6jgXAQetGH5K34ITLGDPM6_83kopFuoVQL9SzaDuxZBH4xYZxCNf22OqhVqdDRL3_k21X89SNwmoNPjXrJ7TrSebDavxn0RN5rFHwobr4VdxIMBWuQx4CdTvHFi-L0iCyV1bFphH7BZYAE0Rf1FjScTwydb0W1ppNFtOklDeOfgL0OzhBfrTbaVo22AFANx06MjQoJ3NRbtzVk_Qsl938ZJSQfy719mMXlkSr1G_gof6QsyJ9-aTR03OyWs0jSPzZuZXvIk-rYi-MaNgMSQZtJbEhM7s_H0hxB3JFopENSYv67nZFYa7gujzsdfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc7d01e79.mp4?token=EGVvlolCYMCXkgHTFxX055Tvsm6jgXAQetGH5K34ITLGDPM6_83kopFuoVQL9SzaDuxZBH4xYZxCNf22OqhVqdDRL3_k21X89SNwmoNPjXrJ7TrSebDavxn0RN5rFHwobr4VdxIMBWuQx4CdTvHFi-L0iCyV1bFphH7BZYAE0Rf1FjScTwydb0W1ppNFtOklDeOfgL0OzhBfrTbaVo22AFANx06MjQoJ3NRbtzVk_Qsl938ZJSQfy719mMXlkSr1G_gof6QsyJ9-aTR03OyWs0jSPzZuZXvIk-rYi-MaNgMSQZtJbEhM7s_H0hxB3JFopENSYv67nZFYa7gujzsdfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🇵🇹
‼️
ژسوس درباره ماجرای رونالدو گفت: هیچ بازیکنی، حتی کریستیانو رونالدو، نمی‌تواند ایده‌ها و تصمیمات من به‌عنوان سرمربی را تعیین کند. نه او و نه هیچ فرد دیگری.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107603" target="_blank">📅 14:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107602">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBNf-kMLOYiYN-u97szQQMolcbA-zCLYcVTY1W8SqKaIQYuHHEG_qivVDOcdqIh-0EKjYIy4TPRHLzbEvoOoJgwFnkeP6ES-hayYtz1Ef9Wf0iiktvTJSEO7d5NfAPx2qF_evVshVldFwlsQc68lemnz-lOy1TMzx4vREhxQ3-D0aMNUgir3i_Av_c-55dqPpjG5pCB1FESAky2dBL_rVROWG-UCztMMYgfsPQPEy1zLzv8zYnjmoRsCXzhEJitofoVZ_0yFYZBrOmK13sDaWPE4kpvkraIPw7jUWFePVCsbfAr-euXPaWHFYoMRNO2khh8J8RiSqPTVBC3ZJY_pkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
‼️
فکت
:
هر ریال ایران حدود ۰.۰۰۰۰۰۰۳۹ دلار ارزش داره، در حالی که قیمت هر واحد همستر کامبت حدود ۰.۰۰۰۱۷۱۹ دلاره
یعنی ارزش یک همستر کامبت تقریباً ۴۴۰ برابر یک ریاله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107602" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107601">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df216dbd92.mp4?token=cyPWi6L_emuI7ltyEr2Oik1CCeGi97KTS6fOsK5rziiNLHsnYjAw-i1JhBHBHPeHin4ay5QVlclhCr-XfZcR6Y-KnnB691g_KNELvyAkZYJ9tYHorAw83zYyD_4camP89Z8FkERYmosrkTN1Vt_wTXEN4Dh7qTbvRxm7Xb3o5h27m9MWqpM8J1AKr1HYN0MShjbSKjBiP017zzomvkle6e2On1us8_f3ibpayf5NMzIao66rXYR5t4J31DhX3mH40doknrW-I97PWiUnUxyYrpLOL2nxwcPfVdEcH4CJtFNQCAFaqs9saJ53pyUlx-f0eamiqoX1D9kwZN-XMaQ57Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df216dbd92.mp4?token=cyPWi6L_emuI7ltyEr2Oik1CCeGi97KTS6fOsK5rziiNLHsnYjAw-i1JhBHBHPeHin4ay5QVlclhCr-XfZcR6Y-KnnB691g_KNELvyAkZYJ9tYHorAw83zYyD_4camP89Z8FkERYmosrkTN1Vt_wTXEN4Dh7qTbvRxm7Xb3o5h27m9MWqpM8J1AKr1HYN0MShjbSKjBiP017zzomvkle6e2On1us8_f3ibpayf5NMzIao66rXYR5t4J31DhX3mH40doknrW-I97PWiUnUxyYrpLOL2nxwcPfVdEcH4CJtFNQCAFaqs9saJ53pyUlx-f0eamiqoX1D9kwZN-XMaQ57Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
بعد نتایج درخشان قلعه‌نویی بد نیست از این مصاحبه طنز ساکت‌الهامی یه یادی کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107601" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107600">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc_dMgUBt_YEWvAAXwc_X05NeKDIg3AWTOIRvLBAx2hgMa8apt8clPSHUd77ucQ1BZ1JfIFkB-Hw9GnCHrWqtEShulh4EMcMIkCtGFrVaE8ljdssW3WdwDnCaV7iBta9x3pfrTgjK9IojE2qdIVbKTcxlwhil9EvANA_epf4j_CBOyThxzsq_EFiH_y5sUHPSzW3438rpDkKJz1qwfeQcVp5inMHvXJIq-YNn_nDplIKjbh-xT2Gc9RPY6y5sJ2gyQ2ueWqalWg018CywY2thmrNUANvQu1VDkQ1hf9a6N08lYCUQJ21TKF63JyBlYQQs8gkxhfwVboBWj1GxpqYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇵🇹
⚽️
ادو آگیری، نزدیک کریستیانو:
🔻
«ژسوس در جلسه خصوصی بابت توهین (گرم کردن ۳۰ دقیقه‌ای و عدم استفاده) از کریستیانو عذرخواهی و وعده عذرخواهی علنی داد. اما ژسوس در کنفرانس مطبوعاتی دروغ گفت و وعده‌اش را نقض کرد؛ این خیانت باعث خشم شدید کریستیانو شد.»
⚽️
…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107600" target="_blank">📅 13:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107599">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972dc1e1fc.mp4?token=crjFhU-KZljewF9z8irZyB-LCwsHGweBwj4re7utGzjnXHuMAYRsrvziLmFDW3t0ujia1uI3vHpC45t9ypLVjmARTxFGcyM2JAdDSeF25BoJhg0hmnuniVRL6n4eBFQmP6B6TyBezbq-3VnrT4Y6y69Jj4xP9lsvwiHa8y_tRznGiiC-imusLhL0VTLHl14MC6DSaUq-sorJ0J5yEgVy3TYul2aFyFzdT7PLleLPC1QbA6r38Pdl8iKqenm3onWoOH6Ir2n7nOjG8jPQASJWE-wl4l3Do0gj8AQ_88ozcIYrxDI-ya4t3ask_yJJEM16RZksdcmIguZqxY7P1duXMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972dc1e1fc.mp4?token=crjFhU-KZljewF9z8irZyB-LCwsHGweBwj4re7utGzjnXHuMAYRsrvziLmFDW3t0ujia1uI3vHpC45t9ypLVjmARTxFGcyM2JAdDSeF25BoJhg0hmnuniVRL6n4eBFQmP6B6TyBezbq-3VnrT4Y6y69Jj4xP9lsvwiHa8y_tRznGiiC-imusLhL0VTLHl14MC6DSaUq-sorJ0J5yEgVy3TYul2aFyFzdT7PLleLPC1QbA6r38Pdl8iKqenm3onWoOH6Ir2n7nOjG8jPQASJWE-wl4l3Do0gj8AQ_88ozcIYrxDI-ya4t3ask_yJJEM16RZksdcmIguZqxY7P1duXMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عدم پاسخگویی مدیر اجرایی منچسترسیتی به اتهامات وارد شده در پرونده فساد مالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107599" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107598">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1tTE-U0aBnHftSls8MBwMOLh00GySGhWC8tumzdC5GC1W6r0Poij1a2qrSNnd1FHjms6-4gky1ErV8lonTe8mOcchQlMOdY5nXgPGtDcbWvkFbxAml2sSES8wbJRvLQMIIO8DG0BVJww6DOQYpSZxZlRBH437hQdLMMvjy0BB-STKLn1oCPGVmdjIJKhczJzVeDcvZ6yHWBfie8VkUhGu3HdOjmcZ_1mk6eer7P8ikhzxy6IUvR2-l2PkdfrwVM1Qz62AoohS_NgNGfdaD-zcaciY45cDQTb01K8GototYGXUhsXkSHcfHyk38431Xu3TPK_WEinMTzTr8kJH9aLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتایج اخیر قلعه‌نویی با حقوق ۱۵ میلیارد تومانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107598" target="_blank">📅 13:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107597">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb2nGF92raTHFuvqW-GkJfQPf0KFDFjeXNvdoZIpuuV-vloKZ41X4UWpymdfbFY3LSvdzUrlU3dDhBOXBJT6vqC7kEK4gbCE-qzDABSd0vng2VlVdLqIQJcwj5Xo-1UBBWDLi1k4a6eNBrL2n60QrWIL1nInTJzyKU80dbFta9sATCEogIaLT5c8D9cEFkDE_Zz1_zJ2IdfKTp01yprbrvBRcVNbEiO7A8vrr-hJvuVLI2npRTPCXwUiZV9hQtcEDvkncP-53PTKNScQTMUCVw2tzL7CYxNZaBtpYfTKI48zMhOP6GI46bUPfS_h_Niru9_Y4DIn0EHzpcUt_fJKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
#فوری
؛ رافائل لیائو وارث شماره 7 تیم‌ملی پرتغال پس از کریس‌رونالدو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107597" target="_blank">📅 12:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107596">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f7d3031e.mp4?token=ONzfnSM_JeTqjoTNAPhG3VyBhi7egng0Qd1ExlmglRtnTya36-7VKlFU8xujFtxN5oChw0YfGeOO2jCEnO9_XhU_lqyL-9eaW0SJDx2KnL_YBLwzhv3-xn6QaEJwLCYg8mP-aq2fM1-AA-0JS1ixnE8K2KmZTaIlTj5VgVZSnyW9EXYFlmD5N_HB8sqEODUlGxJk3xAl2upmtCcKyVfg0YYbc-eK17f0snbXAj3BxahHMcwnx-_KG4fa36e6rXQVKpfPI-tpf3qNCMDUyCHpODZoPJKiAB-jIiTxAWCP2nfvyZtZvd-Z2iI5afmv68duuMbc5qzVEEz65gZZOse10Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f7d3031e.mp4?token=ONzfnSM_JeTqjoTNAPhG3VyBhi7egng0Qd1ExlmglRtnTya36-7VKlFU8xujFtxN5oChw0YfGeOO2jCEnO9_XhU_lqyL-9eaW0SJDx2KnL_YBLwzhv3-xn6QaEJwLCYg8mP-aq2fM1-AA-0JS1ixnE8K2KmZTaIlTj5VgVZSnyW9EXYFlmD5N_HB8sqEODUlGxJk3xAl2upmtCcKyVfg0YYbc-eK17f0snbXAj3BxahHMcwnx-_KG4fa36e6rXQVKpfPI-tpf3qNCMDUyCHpODZoPJKiAB-jIiTxAWCP2nfvyZtZvd-Z2iI5afmv68duuMbc5qzVEEz65gZZOse10Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه تند حسن روشن پیشکسوت استقلال به امیر قلعه‌نویی: رئیس مافیا سرمربی تیم ملی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107596" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107595">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107595" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107594">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afj4uNrnt27vH3h4O4kpP0kB5o66glWlvPlExOIj3MeZqHFQAFNFktWmRpf75hHNg6XLg2-6aiI4VFTuBywnlGqqQgJArUHf--sl8RaRNOJ_NC0nXAVbzShoxEE4Q2lZeyKphzutdqPZSYAEhc9k8sN17V_TP09wF7KUTkh0jHQUBId9yqm_a8tZyL0RpNU8BpJIHVpKb97PiBuowguFyxFLIfjQIpigv8jArHHkyF5ncUtBc2ztTQylKNqMWdiMFjAH1s54phfVZe_CrPnV0aglKCy2wg4dXmF7lb5vI_0ygSV1fqUrtT5UdJ7lIlgXvkOcoYB65DOtFxQFlOUIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
صربستان
🆚
آلمان
هلند
🆚
یونان
پرتغال
🆚
دانمارک
نروژ
🆚
ولز
بولیوی
🆚
آرژانتین
اکوادور
🆚
ژاپن
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107594" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luSzNAZzpw5yRrEjOqyR-cWMsfV_srgRzIxh8CCTU_4u087o0x7G4PiOWjyqaW4Hn8x1VAiG7FSJ60Yq4TksZzSiT-04mwoDZVCIHqiOPQzyr7fUhnj0okcY7xPXWxawuJV5_W6UTObxRRhzBbqOuzlO6mbRLIQFUpEogmtnfd1bbSOL2PyiJAw0nEU_saCjef_lOuw8BVpvFA6x3y7_SePx6EY_va4v8PZC0UjJeVgvHAW6RhTgFnuYdFM6T5yCf0XViMK72YFNcdRdKyOiBfMkqXjtzXfGW8DTgL0ZSkSrycckggxo5khFMK8ukvwkxsncFf6RHLUPmLpiRsrIuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
چندین واسطه به علی‌تاجرنیا پیشنهاد داده‌اند که استقلال در نیم‌فصل با دنیس‌درگاهی قرارداد امضا کند که تا این لحظه مورد موافقت سهراب بختیاری‌زاده قرار نگرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107592" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d48b3887.mp4?token=DTR-Cp8YWQhznB0lWLm1OC5HwdVxLDhcVTgtyYgg9A0vAZHekGF-jVvKCpstEPteaw_2gYmpjvb3QA6jYibrL3RvVKt8Mth89L5piatHIBeigYsl9eIeiZzW0NmzmWTYpIP2F8WtiWJwoX4AUQqPO8gmZMfTuMc2RVs1N8BRLs7JCxiEBQYaax3zVe3JCh6f7vYHzd-KNeTVa89vJBlprdDIURJ-1dMnjbLO1hJPPOaqC_qiZptIRo_yY9v0pEAVcdnFYNLGdFbBFqow9-ajjvMyppfNMXRgbkwIPKOSLT7363bOz_rJoFFaODpBkxsLkGWiweOG-KJAvSpGJNO-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d48b3887.mp4?token=DTR-Cp8YWQhznB0lWLm1OC5HwdVxLDhcVTgtyYgg9A0vAZHekGF-jVvKCpstEPteaw_2gYmpjvb3QA6jYibrL3RvVKt8Mth89L5piatHIBeigYsl9eIeiZzW0NmzmWTYpIP2F8WtiWJwoX4AUQqPO8gmZMfTuMc2RVs1N8BRLs7JCxiEBQYaax3zVe3JCh6f7vYHzd-KNeTVa89vJBlprdDIURJ-1dMnjbLO1hJPPOaqC_qiZptIRo_yY9v0pEAVcdnFYNLGdFbBFqow9-ajjvMyppfNMXRgbkwIPKOSLT7363bOz_rJoFFaODpBkxsLkGWiweOG-KJAvSpGJNO-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
همچنان رقابت نفس‌گیر برای توپ‌طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107591" target="_blank">📅 12:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
❌
⚪️
#فوری
؛ بدلیل تحریم‌های خطوط هوایی ایران، سومین بازی تدارکاتی تیم‌ملی قلعه‌نویی مقابل گینه‌بیسائو در هفته‌آینده لغو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107590" target="_blank">📅 11:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0FOz7CQ9Nr_2NN-2TZN6dJpnlDQxtWw641zMbkKJbxAkobN-LQev62Z6m2pvhSKdpnJlKqKvynS5mWocW737j_c58VXg8zvTlZds1PccLRh0AnO4HBsphp4BK5I4s_w7dYaS8IOoc6drN7lKt2dI1CKS5NKRpdRMRgHm237HSvVZn4FXfF_QY3iWFWEnVp6MGbu5335cjJU9mQzWSa0Alu2jXS9QtaMWA_Ycp8SfT7euMfO6IPJF1jkOn8DKGeJqiIfaz2cGzRXY4nSMBqzzB3Nbb-6a2brZqHfAA8nr9J4FUX3SBpzpmEd8T22U4aERSYjJe_PdB3Zx-zUz2ycBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
میگل‌سانز خبرنگار اسپورت: خورخه مندز ایجنت ژائو فلیکس به بارسلونا اطلاع داده که این بازیکن در پایان‌فصل قراردادش با النصر به پایان می‌رسد و قصد دارد به صورت رایگان به بارسلونا بازگردد. تصمیم نهایی درباره این بازیکن با هانسی‌فلیک است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107589" target="_blank">📅 11:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0340a7da43.mp4?token=XaQJdpMnFtW1QzrQAYGpuXSGME_Bz0PjbuH7aGo5WsTqVJX5jiy7otWlu5YtmaLocNeSQ3gjAj6gWpmZBYp8UpYGxbx3S3umr_ktaVV-dzw-YgBbyqx-NvA45C34DRbQwUpzW6Rr0d-VKduLfB3saGD4LHAVK4fdjkvuLnoMWMDoKNyFM1ny0uer-lDw5Mms8z9L3AYGeq2zHg41WUNEI8GcB3H0hMl4kHgD-NU0qyUtoaJE3nusTbKSWFOBYsHNmnAF4glL5xzujGgug5OTtm8Nqk7Pnoy9wdfvI71H7EYIvKk_pJgLGM7JWsXU3z7Seas3jZ0Dtsc99wg0Xbi0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0340a7da43.mp4?token=XaQJdpMnFtW1QzrQAYGpuXSGME_Bz0PjbuH7aGo5WsTqVJX5jiy7otWlu5YtmaLocNeSQ3gjAj6gWpmZBYp8UpYGxbx3S3umr_ktaVV-dzw-YgBbyqx-NvA45C34DRbQwUpzW6Rr0d-VKduLfB3saGD4LHAVK4fdjkvuLnoMWMDoKNyFM1ny0uer-lDw5Mms8z9L3AYGeq2zHg41WUNEI8GcB3H0hMl4kHgD-NU0qyUtoaJE3nusTbKSWFOBYsHNmnAF4glL5xzujGgug5OTtm8Nqk7Pnoy9wdfvI71H7EYIvKk_pJgLGM7JWsXU3z7Seas3jZ0Dtsc99wg0Xbi0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇵🇹
⚽️
ادو آگیری، نزدیک کریستیانو:
🔻
«ژسوس در جلسه خصوصی بابت توهین (گرم کردن ۳۰ دقیقه‌ای و عدم استفاده) از کریستیانو عذرخواهی و وعده عذرخواهی علنی داد. اما ژسوس در کنفرانس مطبوعاتی دروغ گفت و وعده‌اش را نقض کرد؛ این خیانت باعث خشم شدید کریستیانو شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107588" target="_blank">📅 11:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7be9b354c.mp4?token=fsktxxa4fpvLO8D4-hWFwyBiX-Kw9LC_qz78Cu_8bQv3V7QlIhNfi990xeysLbzUQulLs4XjJq5WawXV402A1-iEF9RC6GgY_gQozgwWvwgyBMvyyxBIh9Wp4zRBpKDDqCl5n1zuMK-zQNnWds-iOYQAwrr5aZeA3JcXdwWBtpcpGLufxl47k4_FF58xYeihMx656DuON8PvHwmvagXM96PwP39B7pXNhvAIntCh-tFAFI2YdxaNh1qQtgQ8w5UAco_UCe3Xtaa3ZgU1MAaUXZn7pI3CS6bmY-1Rv8A1NrVTRfW-AeMX0ovV28ce-YpZNC5oBqlPmoBBM6XdpakUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7be9b354c.mp4?token=fsktxxa4fpvLO8D4-hWFwyBiX-Kw9LC_qz78Cu_8bQv3V7QlIhNfi990xeysLbzUQulLs4XjJq5WawXV402A1-iEF9RC6GgY_gQozgwWvwgyBMvyyxBIh9Wp4zRBpKDDqCl5n1zuMK-zQNnWds-iOYQAwrr5aZeA3JcXdwWBtpcpGLufxl47k4_FF58xYeihMx656DuON8PvHwmvagXM96PwP39B7pXNhvAIntCh-tFAFI2YdxaNh1qQtgQ8w5UAco_UCe3Xtaa3ZgU1MAaUXZn7pI3CS6bmY-1Rv8A1NrVTRfW-AeMX0ovV28ce-YpZNC5oBqlPmoBBM6XdpakUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سقوط امیر قلعه‌نویی با انتخابات و انتصابات شائبه‌دار و پر حرف و حدیث!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107587" target="_blank">📅 11:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">▶️
🇮🇷
ویدیو باشگاه پرسپولیس برای یازدهمین سالگرد درگذشت هادی‌نوروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107586" target="_blank">📅 11:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTeKqD2hj3tuIQ68T404SSommajOnv-hAdTHxPzmNbyUaJRbvTDigjwvySGp3G6Rz7n_zzbEQgMLnJKgBV87EyVzt_QwFxRWwCTn9k2-WvFTAuhe84jYxf1E6cyyV92LMcKYPi-CMoZVfSnoY5X9fLKk3gIMqbinE-tSiX7WgMuQAclDio39-X7AErpSL6MmafM8GE-ilI8pp5qpsFzIyCJxLZMpmy_C5tivcNTDw3NIGR5yU7JILKPKezEzSddSTcXg94c-mBC6Ht23zkYcRgMrmJse1mYHNzIBA2xLmKrUQ7-vZvPZVK2k2uoEQCl4LhQiFPP9ZgTg6MlLDU8EdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مهاجمان بارسلونا در این فصل تا به امروز:
لامین یامال: 11 گل، 7 پاس گل
رافینیا: 15 گل، 4 پاس گل
آنتونی گوردون: 2 گل، 4 پاس گل
کریم آدیمی: 3 گل، 3 پاس گل
گابریل ژسوس: 2 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107585" target="_blank">📅 11:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d3c9c064.mp4?token=kK9t2vUcubs7YflBVXs5b56lz9NEZmyhHr0XazYPjDnDXmg57HZ7lp91Tpi7_apV3Vq3JcsrGcFwE8XWqZHjkW2XZ0kfhXxX75s7JlVV9bkatYaRguMFQTQ_nvy7j40eL1PEu7syvOZzvk9vsFrJ3M3I3iJsv1ALuZK53nULmqAr0KpOKvASrr_shWOSnoB-OV82ln4HOcm6aY2Ie7rWZ0NoignjPWq_8E9kd2CWx7FbH2rr7VIAG6ac0w8CYn-bb9FuOYdU3gT_sF6zpCYPVeKVjKrhcXg2pGJ1SljsnAXOEE5zbFdECnwAJ4UVUewf1f6tXJuBD7OF7w4eMIdz9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d3c9c064.mp4?token=kK9t2vUcubs7YflBVXs5b56lz9NEZmyhHr0XazYPjDnDXmg57HZ7lp91Tpi7_apV3Vq3JcsrGcFwE8XWqZHjkW2XZ0kfhXxX75s7JlVV9bkatYaRguMFQTQ_nvy7j40eL1PEu7syvOZzvk9vsFrJ3M3I3iJsv1ALuZK53nULmqAr0KpOKvASrr_shWOSnoB-OV82ln4HOcm6aY2Ie7rWZ0NoignjPWq_8E9kd2CWx7FbH2rr7VIAG6ac0w8CYn-bb9FuOYdU3gT_sF6zpCYPVeKVjKrhcXg2pGJ1SljsnAXOEE5zbFdECnwAJ4UVUewf1f6tXJuBD7OF7w4eMIdz9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حسن‌روشن: یه روزی چند ماه پیش بیرانوند بهم زنگ زد گفت اجازه میدی برم استقلال و بهش گفتم اگه اینکارو بکنی میام جرت میدم. واقعا سر در باشگاه رو باید گِل گرفت اگه دنبال جذب چنین بازیکنی باشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107584" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800d85114f.mp4?token=Ur5mrYboOU3a3vzWHdFenovN8VhLKKlGwJrv52P5ShH1vOEJ44K3QI2X-TbLHXNplxNIog-hSOkjg28Sr69sTntu775_pdC8Gp57n5RUCJPDQYmdEcrRobO883uVjunOzi-k0KECIp-mYuBH-mVnCNT3EJNRo7IlCnGt1mzybLTyk--tYewTTc5nALh-fRbt9NSSTOQfIuWLMQRkyGmlSBU8Pz3eYa2szgJ_ih7Z0L67UGU7CWX3pvinwoXMr5Ewh_kOcr0LX8TKv5CGNok_4oKGAiyQq_nVMMck6CpR_EmxLUwGf63DkYeLsmGifdrRwpX62WiDRujIqkwRaFRuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800d85114f.mp4?token=Ur5mrYboOU3a3vzWHdFenovN8VhLKKlGwJrv52P5ShH1vOEJ44K3QI2X-TbLHXNplxNIog-hSOkjg28Sr69sTntu775_pdC8Gp57n5RUCJPDQYmdEcrRobO883uVjunOzi-k0KECIp-mYuBH-mVnCNT3EJNRo7IlCnGt1mzybLTyk--tYewTTc5nALh-fRbt9NSSTOQfIuWLMQRkyGmlSBU8Pz3eYa2szgJ_ih7Z0L67UGU7CWX3pvinwoXMr5Ewh_kOcr0LX8TKv5CGNok_4oKGAiyQq_nVMMck6CpR_EmxLUwGf63DkYeLsmGifdrRwpX62WiDRujIqkwRaFRuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های رسول‌مجیدی پیرامون وضعیت تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107583" target="_blank">📅 10:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09df2fee06.mp4?token=ZN79Z_ct4wqNtuUyCOB2TqTFNTzGcb1rigpLxeEHsGvbVgDdzDDz8yfBT_pcsa1OAQeJH_UV-Xx7J2cmqSwQmz-TDsQp_IqMb1eFczJtNy1-C5kkcTBGAMAXAcpPrgoNUCdtpo0FohLJtqa-6FY-QQlrHFTMX-L5A5I4PZy4SlOUZuepWnICJxfmuOCLV0LGX7ZSWJeuWml86oAJfP8et8nRp71rXyvMEMRqMdQwFI6dBHEQd2ZdIhCZ2a50_ePQEVxeveXA27Ubob4PD6CNYL4Dy8KqSNAamKUp3lLZmiW3fz5clzCoUIknSOxW648QhuKtcRWopAgUxgJZTwxJFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09df2fee06.mp4?token=ZN79Z_ct4wqNtuUyCOB2TqTFNTzGcb1rigpLxeEHsGvbVgDdzDDz8yfBT_pcsa1OAQeJH_UV-Xx7J2cmqSwQmz-TDsQp_IqMb1eFczJtNy1-C5kkcTBGAMAXAcpPrgoNUCdtpo0FohLJtqa-6FY-QQlrHFTMX-L5A5I4PZy4SlOUZuepWnICJxfmuOCLV0LGX7ZSWJeuWml86oAJfP8et8nRp71rXyvMEMRqMdQwFI6dBHEQd2ZdIhCZ2a50_ePQEVxeveXA27Ubob4PD6CNYL4Dy8KqSNAamKUp3lLZmiW3fz5clzCoUIknSOxW648QhuKtcRWopAgUxgJZTwxJFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
⚪️
از مفت بری تا رو مخی ترین فیفا دی
وقتی منتقدان تیم ملی در جام جهانی انتقاد کردند، جوابشان شد «مفت‌بر» و «جا خالی»؛ اما امروز یک شکست در بازی تدارکاتی، می‌شود «رومخی‌ترین فیفادی» و دلیل برای زیر سؤال بردن بازی‌های ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107582" target="_blank">📅 09:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107581">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2ebca248f.mp4?token=f9MAjXdocdu7Zq5DoXsiKw0vybYfDvKeGIFWpqezfVU-dNz7KAZ2nkvhBKNWqRtYD6Op47zf0EteXPKaNocKq0j1puwM08IIP9qLCuWX_cFeBuZHNxu_O5TK74bQ07P-XzgVXpa1ctmTqi1qAf9I_8IHpwL0V7nIx79QTca8e3MP0A4zPH1YGuH23Qa_Mtdqb-YlRE4A0WGoxLwVLjWHjZ44R36oCmnuTuxbcoVCGz6ueaWm4Z3q0BFScszsvtWQxJd6N12xa-xCww3amOJS0WD6VaiuQTXiI4tR7wxYueJuiE_wlQmuwB8rpO-cag-6LQcHMe0m7XGY9y2dmR9RpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2ebca248f.mp4?token=f9MAjXdocdu7Zq5DoXsiKw0vybYfDvKeGIFWpqezfVU-dNz7KAZ2nkvhBKNWqRtYD6Op47zf0EteXPKaNocKq0j1puwM08IIP9qLCuWX_cFeBuZHNxu_O5TK74bQ07P-XzgVXpa1ctmTqi1qAf9I_8IHpwL0V7nIx79QTca8e3MP0A4zPH1YGuH23Qa_Mtdqb-YlRE4A0WGoxLwVLjWHjZ44R36oCmnuTuxbcoVCGz6ueaWm4Z3q0BFScszsvtWQxJd6N12xa-xCww3amOJS0WD6VaiuQTXiI4tR7wxYueJuiE_wlQmuwB8rpO-cag-6LQcHMe0m7XGY9y2dmR9RpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
صحبت‌های کنایه‌های مجری صداوسیما به سعید الهویی دستیار پرادعا و بی‌خاصیت قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107581" target="_blank">📅 09:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107580">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH2Q5DHCCyj-nFIhvnwzpJdlpRdCccWYmFNALp2O8byKNdEqHLWTUrLIsR3S5T_ctkCLhD1Pw0atx036lD1UvJUP5uocbDHzXjh56mT6ZCGW8YZKcnYC3lXWdMBWp_p9SRBnAOLY5P5MiyeAR_X1YiO0D04GsSNIo8yfZQeAOhceaBWztDfruYjZRqd7-4yEUPULr0sls3y2m6sLAhmsb96mbdQEFULWVTwyEvNdhPvmTHQugzM4PWC2FHdxAaBo9n0IdIGULi1FQPIwp4wwvht3IfWlg3RR_CgZtZyXz0e1XM7zB-JzXLid1PCtLK-nbAhKLrxlWPyaaJ5lpD4lvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
⚽️
فدراسیون فوتبال پرتغال بدلیل بی‌انضباطی در ترک اردو از سمت رونالدو میخواد این بازیکن رو جریمه مالی کنه و اگر رونالدو از میادین خداحافظی نکنه، ۶ ماه حق حضور در تیم‌ملی رو نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107580" target="_blank">📅 09:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgphBUbvqRfSZSSwmOjx76NWqW0ajlZn7h68fCnA0w-bzrC5EtTy-TB86-iaK_JgEwpkQ--V7XDKdbjnUVKXAYoqeN4R11IVMLDPetfxgWyCT1QT0cghhX8soXlJ9zQmEy1hQeJnKdtbOuSXqRqXKWywhN26jfU6o-_q0j0u_HmhzWGkT4yCve5eJfNfyUo5LL-J1hX_VaNVcQ1eGTnHUr3AyDHkSstwAmtvUgclIfxyyHY2hnIWVgoR6QbCchVyBrPvV79j3NJzfNDiKSo6lMugrh8P_DaG-e7BApLvsK9Akp_Z_Qqt1iwnNVMkRpasQEprUnJRYMg2g2iW8agoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🎙
تیبو کورتوا گلر رئال‌مادرید: بنظرم جایزه توپ طلا باید به بهترین بازیکن فعلی جهان یعنی کیلیان امباپه واگذار بشه نه کسی که صرفا جام‌های بیشتر برده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107579" target="_blank">📅 08:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107578" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/107577" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107576" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6Ssbm51Y3YRmtNLHtdq0IcXPBq-dlxO3IEjveKc10kor6yQmBGy_gKeqXuqBRbymMzhuS_0PaWARknBcA4ySjOPnNn9X9FW8rIT6D15co_GuHjwBT1Nyf8CvrtO9nRdi5IHai5GZ_ALHjOWqtGJa91ii6awJL4247Agvvh8sb8S7t-45pLmakEBBFwcH4qaix4RPXJQFOU67uxUhTrZKiiLrqN5mbKoM81sz-WZv3FwOCSLawwWf-wO37bK7l8t4aW0Zmelvrd8SBbuuAo5SxKK44_JyCPmkq0aw42eZETCBk4Nt8Bl9Fx_DekEJo66zW9GYq-tQ_eFReFgP9DOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇦🇷
ترکیب تیم‌ملی آرژانتین مقابل بولیوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107575" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7236f39a.mp4?token=l_LrAC0weHI81ZW4mbD0q2-a5-tYJvuxQR0CtjTu3qRvViB2ivY88QMAKTBDZp5Z0PFoIK8U5UylsV1-u89GArsQbeGjQcrkUwze2bRIOIeVMEXDwzTMeSw8-tpXTT28ALqJiHBXWIwKldEMQ4RFbXyCu2XuJ-nVpFVA8eyOlfreYILJdu4qesIMwzVMJ1u1ZaKepF98Zo31w-dlhg-iLXcmtJiZp_1-YrXqI7SVLZpXVP8V7y0HsEGWy64MPkqqWt7pb085q8NJC-znfmpAXsGlsIBEFCu3IU4zrKdn1TDyfA2owcDfPZuFmpMW8Ydp892mm2a4lCd2lIaMh0eHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7236f39a.mp4?token=l_LrAC0weHI81ZW4mbD0q2-a5-tYJvuxQR0CtjTu3qRvViB2ivY88QMAKTBDZp5Z0PFoIK8U5UylsV1-u89GArsQbeGjQcrkUwze2bRIOIeVMEXDwzTMeSw8-tpXTT28ALqJiHBXWIwKldEMQ4RFbXyCu2XuJ-nVpFVA8eyOlfreYILJdu4qesIMwzVMJ1u1ZaKepF98Zo31w-dlhg-iLXcmtJiZp_1-YrXqI7SVLZpXVP8V7y0HsEGWy64MPkqqWt7pb085q8NJC-znfmpAXsGlsIBEFCu3IU4zrKdn1TDyfA2owcDfPZuFmpMW8Ydp892mm2a4lCd2lIaMh0eHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🇮🇷
محمد خلیفه گلر فعلی آلومینیوم: قراردادم با استقلال امضا شده و نیم فصل به این تیم می‌روم. خودم هم دوست دارم در استقلال بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107574" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45c62d9ed.mp4?token=pIVTtTngqDAi45JbmP0UmnEcMkHHv30uIYwFuL2FEPoFdm4GJ-g_Qot_elxYhkxUgJbPXrjwHCIaM7MLGSz9A8vqrNtS8QMW21fkGYAVAOZ3MLMqyTRWSvuMOKfby-0Hwris0l_r-BO0MzdlcwRinDpHTiJkEqv0QoTsrWVra0McE543i1C6__vMBknK15g6OiVymc1NV3jC1gaXouCbnQdx70eXeCS5gXkk2QMeQzVtRNGE-H0P68VtOWhW-Fq43nO_ljYDAiM8eS8Y1F4NgnIbGW9a0ZNVmPSpr0Ov0sS6cU0lkrOLRldcuh3qgLU_Oi5PE3uoYsYltwhKduwLUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45c62d9ed.mp4?token=pIVTtTngqDAi45JbmP0UmnEcMkHHv30uIYwFuL2FEPoFdm4GJ-g_Qot_elxYhkxUgJbPXrjwHCIaM7MLGSz9A8vqrNtS8QMW21fkGYAVAOZ3MLMqyTRWSvuMOKfby-0Hwris0l_r-BO0MzdlcwRinDpHTiJkEqv0QoTsrWVra0McE543i1C6__vMBknK15g6OiVymc1NV3jC1gaXouCbnQdx70eXeCS5gXkk2QMeQzVtRNGE-H0P68VtOWhW-Fq43nO_ljYDAiM8eS8Y1F4NgnIbGW9a0ZNVmPSpr0Ov0sS6cU0lkrOLRldcuh3qgLU_Oi5PE3uoYsYltwhKduwLUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکت‌جالب بیژن‌مرتضوی در بدو‌ ورود به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107573" target="_blank">📅 00:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnEo4q7wSFQ_6N-mhybJVC6oNh1S38T5n0bWgXPc5RVjvwCG-WUSTix9Y1mXpkKk1H-gfYVI4SMp9ukvlFTJ2H7gffPoV2nX_hKebC3kHJDWBFoRwIT0WTd4P-AiUBSNFyj-2qITZots0cN4g470eDEwqtT0ebxtYv-Q63Ip5dvyVipdLHexNZAVsc03m0_7kSaNffctHdLvZgfExuDEqSk06PFooPDElwjhXsWrWpayFZMFQwnqkQXjcLP_hNc_V1t8xkRFIovY_f3EOG3INShKnPVkBvZYptXVhN8F6ZWQJW35kyWBSOlrkIg4-p5DKibefK6xy4HVUSS5fAg8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
👤
رامین‌رضاییان از ناحیه عضله زیر شکم دچار مصدومیت شده و احتمالا برای مدتی از میادین دور خواهد بود.‌ وضعیت نهایی این بازیکن تا فردا مشخص می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107572" target="_blank">📅 00:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db10a352e4.mp4?token=P5KZya4fbBbOLxqG3qcgSFZIYZNX2PFFsYOuqd2afD6n6XPVig2BgGflhgxPJHbyVA7hOGOZdg0korKcO6SJzb-yD4QvqIo5qnDCRLDJ44GX7xeTgOAN9aaPDVPcH1Wb6SxLFRUkPdT-SvyMIJX3O0UKWW2z3HGoMBwfLLknbNhQGh9l72WuCkVmhFel90hsMjJFLrm7Zckj5uiLd8uW8g0URVZi5BSaatImhfp4nldcStJ0iX2J_xcMFDxgcMXN-oTN0S3GIdrSkhx_0V-aL_XRFR8OZR-e5avWvhSWtO_LjJ_AhXI_TK8sxGG3teU96soP7D4CHrOqerlthni3Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db10a352e4.mp4?token=P5KZya4fbBbOLxqG3qcgSFZIYZNX2PFFsYOuqd2afD6n6XPVig2BgGflhgxPJHbyVA7hOGOZdg0korKcO6SJzb-yD4QvqIo5qnDCRLDJ44GX7xeTgOAN9aaPDVPcH1Wb6SxLFRUkPdT-SvyMIJX3O0UKWW2z3HGoMBwfLLknbNhQGh9l72WuCkVmhFel90hsMjJFLrm7Zckj5uiLd8uW8g0URVZi5BSaatImhfp4nldcStJ0iX2J_xcMFDxgcMXN-oTN0S3GIdrSkhx_0V-aL_XRFR8OZR-e5avWvhSWtO_LjJ_AhXI_TK8sxGG3teU96soP7D4CHrOqerlthni3Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آهنگ جدید محمدرضا گلزار منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107571" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHZBdLsWJWHkhYak2IqgdUUAWsKOZiUQCnQ_aTxVE_tofA1XFJhJaRwjlhHK0WyXWUqq20J94wl4HKX4TAEepE1RFEhhOMdDAt1MFThZb7CG4VwN46oFmDPZ9o76w8WNkSmGzEqx2BnsNSeAmd6wCYOYVRBVAxT0YfkIY_gEu1wN6O4ukLYF-L8CMAsmbNGlRo5OiW655lBSOpSCH5BBkKzUN2aeIBtUQ_UmdYxW08lBz1hwdhBtrc4jlwszCDFYB1WiF4DUKfZAYPCWj8OjJUN_-j9suVueVweao5lWRarQ2hflx1zURsgFSLnvwU-1SZW8Enswhujc04wcB-CKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوری از آبولا پرتغال: تا زمان حضور ژسوس روی نیمکت، بازگشت رونالدو به تیم‌ملی غیرممکنه و باید بزودی شاهد مراسم خداحافظی برای این اسطوره باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107570" target="_blank">📅 23:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw7UXuXnO48FKJ5NB_oB6AYyTmRzWsVdLthtO1TDF8lvUBxeBVrbvK5w-shHUtcNHvTeijBl5-j4bBQvzNCP0YfF-3OWkTEooBOinQxRe2k1tZYHY8UpydbCCf_mFe-q5zAkNiiM0MvpgbC4nHua4fHvnSVnii5YawVWtKqqnB5Xnz7AmuHySL8ws0ONuOqlCsccGjrcFw5G7ZoGV6Q3GSIEOLzFPczLvycGHdFgOPILDzWqNvrpgZs6jtPBMhEwbVPp4vLTUBM4F4oxBHwB6eZ-NNBoaNjoZ5Mmt-2zzgbcrfMtQ6OJyJMmN6SCra1H21M70WzdpPDsIjJR6fJ0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: اشتباهات اخیر خود را میپذیرم اما از مردم میخواهم فرصت بدهند و مطمئن باشید که تیم‌ملی را دوباره پرقدرت خواهم ساخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/107569" target="_blank">📅 23:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6l2dm-zQiZIC5hPNsKyZGeqDYHBsJ7uU1mnuVDcp3Fa0YrBDNMeXtSqxmcoaNvAHB7DUg2HRI_F4EmApWQ6eXNqk9ssWm3yWRzX95WyHJ3V92KXw0dIU1IK9SbMlL_vFtDpYsswwK5BpfAJP6QkrjO9vLO6NXn1zO0DWQ7Pyl-RavBZgUuaFjIy_yC-SV0Kf5n_ZPKlKKBkYWpVFJdaIUNJXf_UEsppPrKQeaxVgH5yr2hlikKwqfUpfly7FL41tI7R4Wr5jte4zgH4fMoGPSDEaOOC67X0XiZNG2Xg396_CnzByVWbujBk2Ei9IHpmPPK-4ul06Xj_eUxX39b6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوری از آبولا پرتغال: تا زمان حضور ژسوس روی نیمکت، بازگشت رونالدو به تیم‌ملی غیرممکنه و باید بزودی شاهد مراسم خداحافظی برای این اسطوره باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/107568" target="_blank">📅 22:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjTOHcNFoOIMqrs0jaT6Fpc7S6p9QIqN174ZuOdMHze37SIzS9GUhkWChAa2yzOJtHhltNb-rkHVdP8LxokeXIRMo-fXRKeGvKgP-ZNfV3NAbY5hvzOxp9blWwawR-mjRUYk6L1h26KrXHpscm1l2G-VGkSX5xUWduRtzHT9w_ttCLlEZ0kXW79XTZYKxniUkFy9sX16LFUkWFjsij3lzIsYmjQ5AFAFw6dLnq5wcz7rWdcz49S6fan_Jlw8CDTaMk2mmfeXBBvcnsl9w0vFB5lKWa-38DeC8Gl6dR-1p414LruQmwZGLuOXvh2JCDKS9dXgtuV4lqKJ8Nv5KyBXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💣
رونالدو اعلام کرد که کمپ تیم ملی پرتغال رو ترک کرده:  بعد از کنفرانس مطبوعاتی سرمربی تیم ملی و متعاقب گفتگو با رئیس فدراسیون فوتبال پرتغال، تصمیم گرفتم کمپ تمرینی تیم ملی رو ترک کنم.  در زمان مقتضی، حقیقت رو درباره دلایلی که منجر به جدایی من از تیم ملی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107567" target="_blank">📅 22:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ9TvFLBFbY8mGrS5Y8iWpE5zlR7SBRr6rLo6k05JyHYyjI9BZ4YZIJCfh-Fkosvq0srPwV0B6mbeFjAlJCMc2cSAKm1WbnfHa9MTat6SwMUMACTnUmcaoB01BH3W_mHhgsu6OGd_FfuOaUKMdEvN9EL6Y522raGk5r9tlpT7w3RQF2NofagKGuR5fy24RJ4VUaj0HJH43yawlsLTL2tQN6fX3VQZ39r9fDxuaPhjvVcQk6u9SnNGch7C9E3_TOJTQYDvWD7oM8W942eb77xnR5uodm8HbM-tjRY3bPPJsPcaBIR4txabsL8ftRF42L6NTOLx8JdeyAHq0KFZOZ2PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💣
رونالدو اعلام کرد که کمپ تیم ملی پرتغال رو ترک کرده:
بعد از کنفرانس مطبوعاتی سرمربی تیم ملی و متعاقب گفتگو با رئیس فدراسیون فوتبال پرتغال، تصمیم گرفتم کمپ تمرینی تیم ملی رو ترک کنم.
در زمان مقتضی، حقیقت رو درباره دلایلی که منجر به جدایی من از تیم ملی شد، تیمی که همیشه خودم رو وقف اون کرده بودم به همه مردم پرتغال خواهم گفت.
اکنون زمان اینه که برای پرتغال و تمام هم‌تیمی‌هام آرزوی موفقیت کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/107566" target="_blank">📅 22:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQQYZj1UeQS-YXpgtlW1063H8-z76EarkTpJj6Ghx_wPOiNuAeLVcK65kgJuROmFd9Q31kCXzof9g51esQc-k4GgN6q4jkd8q5Nmd0o7u9KPGqmZypPD0MfgroX0hytTqhKHFQD3dGRWwhuiRSAM5vDXJkuCr3yU3Dc2npx5i4R84egikJ17Ckmjx0L7X18vtltppqNspaDLmx97stZrmykT5jYPhwEIvmun1jF7xc1WglKAO9-Ef2f5MJ4NamjD1WtTvLtf3itmET9Onx5tbZsg5hkFpwqgyiU2VrN2z2gVHu0ELvnsRVs8_za9StbYwxykBt2dmVs42vyZjSY8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
فرانس فوتبال اعلام کرد که عملکرد ابتدای این فصل در ارزیابی توپ طلا  محاسبه نخواهد شد:
🔸
دوره ارزیابی رسمی از 3 آگوست 2025 تا 19 جولای 2026 است.
🔻
هرگونه عملکردی پس از 19 جولای 2026 خارج از دوره رای‌گیری خواهد بود و برای ۲۰۲۷ اثر گذار است
👀
به عبارتی درخشش‌های ابتدای فصل یامال و هری‌کین و ... تاثیری در نتایج امسال نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107565" target="_blank">📅 21:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0mpeZccsiaLWJrmsqKqtjBwirgk_4kcksurrqAcEC627fve8F58gWiUjZ5O64edZnCH1YiejcYxH747GR0K5HphUQhM2X9l7F-US0AwJn37U0QEusPLvljg_Lvc9EMJpFaf298PSlSlSmipp64E9Kh_P1SNjARcdVw3T9k0jzdcTty29oW0HGLaQsOhsKfcMpT1fVVQjMtSuav-3g21e-cYQaqpg9EiE4NtKE-K7qCZj6TwM6TerSp0rDw3aH_YaryhMqs05owYJKP9ofp90lyY8caZKK5n0kmsIsBwW05TuI7s0cUNArJvs1NmoiANKe653_RRkFgisyzw18AwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107564" target="_blank">📅 21:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81558f0c75.mp4?token=f95TmZiXMdLSlEEtRuYxajL3dbLKWGvZfh4KUqPtNV6Nvrh1Ac2x6KWxUX_zq_ls0nv8v2rV89cmd3L7wAAYoOG1ToVaYqS-yQJcfukobltXTv7huoU3v0QTnv9T0zKp3rBwSPCER7cYbe-1FmNZKl66j9wgDy5PXVAyPDCCF3vr1_IZhBnVNzbxp-zhn5s6-Y5pFHgQSRh9XMFkhskNuJj0Phj49zNTE8qDEoIn41Vw-QzSTzTYTU8Ohck9pKRs7SBVZDsxRINrPfJUszpQ0VnUwped-SYbiNuRS2XpZ1g2paSUJZFKubbEuuUk3uhBDfRZZYLDQ9WjALuefEtVQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81558f0c75.mp4?token=f95TmZiXMdLSlEEtRuYxajL3dbLKWGvZfh4KUqPtNV6Nvrh1Ac2x6KWxUX_zq_ls0nv8v2rV89cmd3L7wAAYoOG1ToVaYqS-yQJcfukobltXTv7huoU3v0QTnv9T0zKp3rBwSPCER7cYbe-1FmNZKl66j9wgDy5PXVAyPDCCF3vr1_IZhBnVNzbxp-zhn5s6-Y5pFHgQSRh9XMFkhskNuJj0Phj49zNTE8qDEoIn41Vw-QzSTzTYTU8Ohck9pKRs7SBVZDsxRINrPfJUszpQ0VnUwped-SYbiNuRS2XpZ1g2paSUJZFKubbEuuUk3uhBDfRZZYLDQ9WjALuefEtVQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رنگ عوض کردن سردار آزمون؛ حین جام‌جهانی خایه‌مالی عادل رو می‌کرد و الان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/107563" target="_blank">📅 20:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=Fcf4wQoEPxf2iRDkYjrXp99TwxeJqWPeW5joyK77E2DEodRFmF_Z-wJ7Shxq9IJG2287p9HHo7eyNDnCPnK9TdHq0wz6Vzkp91xHuRvf9B38pPyyE0pWkvVAEtzQlKYyZl5-FjtagJfurZ1rAPRYfWGnPAfX5pjQA5d0qI1yvn9uJ6jMkb8c29vwbpJ8vb0MegS_SoEgxxRt0bCU0g2rzCRATF7SG1z9cMSLiM_YHBa36BDMySwHSZ4AZz_N7zCfKDFdhaAkVWgeFecN28SMk2lGaBWsUN5RCsJ5IhDk0EHIDq4d1ii9M3cCSrWNAAd3CiJ8SitaGxvYtBzf7ITGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=Fcf4wQoEPxf2iRDkYjrXp99TwxeJqWPeW5joyK77E2DEodRFmF_Z-wJ7Shxq9IJG2287p9HHo7eyNDnCPnK9TdHq0wz6Vzkp91xHuRvf9B38pPyyE0pWkvVAEtzQlKYyZl5-FjtagJfurZ1rAPRYfWGnPAfX5pjQA5d0qI1yvn9uJ6jMkb8c29vwbpJ8vb0MegS_SoEgxxRt0bCU0g2rzCRATF7SG1z9cMSLiM_YHBa36BDMySwHSZ4AZz_N7zCfKDFdhaAkVWgeFecN28SMk2lGaBWsUN5RCsJ5IhDk0EHIDq4d1ii9M3cCSrWNAAd3CiJ8SitaGxvYtBzf7ITGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس ژوله به قائدی و قیاسی؛ ژوله وسط برنامه زنگ زد به قیاسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107562" target="_blank">📅 19:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXZ1e7Kj6vmsAvDHhJ8PbkJ3F2JUFpSR0SQWteHRBcDkmbQssAJ7vGBiVTaLpOjKB6XrZJWxuoLqF1LUshmOXZBJjFHnTFNGVOLAf627p32c6QP76DmFA-okiKYQZTKSUR0nruNitW21U9mC1XHV8077FjuNOb36TCCUZ1SO2QUH496Dxi6kb92EUDFEkWDjv72zKI6DjukVicvQu1BDntV4wHho0K6RTaIhKfUYL_p8iuStgaBRf1qvP3ynKuQA6BXgTy_ew2y10oPqw_06a0kWQMnPCloXOW5adhOOsfXVJx3ZiWA-RN7RMO9EJADXv8hibZUeRu4s5alQc2ZumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107561" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=cC1joWZGEZbmfIfV7o7DKamRm8lvZXOcxSFGaWmbXznjoTKofVfFJJIYDGIreeJbKlMORSGKpXBQslU_R-2Wk8zRHnsp7_iHF6IvsBNADUB181QDT7nDAMihxs_1R7vEiLO8tY_z_JkPSeI7UZU0RCbYipSa0Kw7cdFZrPCa4gMzCKiT4pusMd6AmOZHWEJmW-7d8AA2mydHZ-kleVY_tTkmVFrFZrAklMDMAxaeodKNM1XI5ypwiNKtD8IeoQieb5mn36c_YEiYyiQ3ZawHJU0yF82eO408ERFz4PI1KHg6TRE71bB18U_vx1LdmyXypy_n-_SDt4jKKREg1jVB-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=cC1joWZGEZbmfIfV7o7DKamRm8lvZXOcxSFGaWmbXznjoTKofVfFJJIYDGIreeJbKlMORSGKpXBQslU_R-2Wk8zRHnsp7_iHF6IvsBNADUB181QDT7nDAMihxs_1R7vEiLO8tY_z_JkPSeI7UZU0RCbYipSa0Kw7cdFZrPCa4gMzCKiT4pusMd6AmOZHWEJmW-7d8AA2mydHZ-kleVY_tTkmVFrFZrAklMDMAxaeodKNM1XI5ypwiNKtD8IeoQieb5mn36c_YEiYyiQ3ZawHJU0yF82eO408ERFz4PI1KHg6TRE71bB18U_vx1LdmyXypy_n-_SDt4jKKREg1jVB-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های ژوله‌درباره جنجالی هوش‌مصنوعی در ارتباط با سربازی علیرضا بیرانوند
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107560" target="_blank">📅 19:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=ija3cFY1WCf7XMbxknDjH1xCZ_gWQgCOWJWteU-4ppR0VAwROU6FJR1aWeCvt9lht13WYKX1gyvOMiD2_PxmlEigFs2AqMWg8qq2-AMaho8eIZlBTx5-wNQIHuU4jMpNIyu1k6gv2aMZhXNv_4Ir3Uk3HNMxBP3sxSZsUySu7bYtqFcwaR4msAhVAzNFM8bGix-naZZ_3ENir6LWS7b0ZMCGwVFmBZZkKmQLP0-xKXnVDF03SZe9LuvSy-oYecLb7kvFTFZYwmhVVw7kmsmE1OSwia4GSrtohhwfB9TYMB3VXR5f6KXnu2eBU4mAZ8GrMqZ_Th8Gvk9mULelSE31dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=ija3cFY1WCf7XMbxknDjH1xCZ_gWQgCOWJWteU-4ppR0VAwROU6FJR1aWeCvt9lht13WYKX1gyvOMiD2_PxmlEigFs2AqMWg8qq2-AMaho8eIZlBTx5-wNQIHuU4jMpNIyu1k6gv2aMZhXNv_4Ir3Uk3HNMxBP3sxSZsUySu7bYtqFcwaR4msAhVAzNFM8bGix-naZZ_3ENir6LWS7b0ZMCGwVFmBZZkKmQLP0-xKXnVDF03SZe9LuvSy-oYecLb7kvFTFZYwmhVVw7kmsmE1OSwia4GSrtohhwfB9TYMB3VXR5f6KXnu2eBU4mAZ8GrMqZ_Th8Gvk9mULelSE31dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
شهریار مغانلو بازیکن تراکتور: زندگی کردن خیلی سخته؛ مردم نمی‌تونن خرید کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107559" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107558" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107558" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107557">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWCIQdDEN3SM9n1UWT2jjDRzCyadt4K6Yf-3iSQeN4wkkcC4_aD5MNbw6OKpwqgt6ZmVZGn4Pzk9PI7lJPJb2Y44Hb8J4Urlz9PvxZHOGDMnoVUQ-K5DPq8ZqEZfIOY-zDuigtdNAXVMOEy_wiTEccG2YxUf8489F788JmowjTE3HQB80N1-RZ0SMr4FxAYXYZq7Iwf4N-Ej5nYqX6skfNH_A7KCBbVzmziodFF_mEqG82fXwx8y5dgcxSNoLDz0x_er1OURtQofwO291v5pylo-Uvp822ySnc3ZvJH7xVLbDUNL8qUt-Qo6JB-wQ2OSXRmabTDspuT2anZeiMNQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107557" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
آخرین وضعیت ورزشگاه مخروبه آزادی تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107556" target="_blank">📅 17:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=MiyKuS2L3dxkrZBpNN6K03p4C_HdWcg69hX8GUfm0kACDLORjL2WJh_JeZioPcwr-c9py412JlUGr2rl3APqOAC1oqrfNcmrEKhObl2cIBRnT7-hImrsBkG5gpHWiwdSjRGpm3ZZ2l8n2Pk06si4NaEhX-8DnsuxiGyIaXeK5IwkPrDUpejXJuAnx48AB0XlvisHSqTWPuYyJ1CzAA8cVomv3N0QIggawjWWjAk0WOFEtRm1Ol64o0-vgT6b4SJRbY9rdLxUugL8BL1Aoxj142m-7TaYG_K6lpacyvNzDWAseP-SXtPFPamu1_5JZKN9J3CgkLhf6IlWxGkLLklyqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=MiyKuS2L3dxkrZBpNN6K03p4C_HdWcg69hX8GUfm0kACDLORjL2WJh_JeZioPcwr-c9py412JlUGr2rl3APqOAC1oqrfNcmrEKhObl2cIBRnT7-hImrsBkG5gpHWiwdSjRGpm3ZZ2l8n2Pk06si4NaEhX-8DnsuxiGyIaXeK5IwkPrDUpejXJuAnx48AB0XlvisHSqTWPuYyJ1CzAA8cVomv3N0QIggawjWWjAk0WOFEtRm1Ol64o0-vgT6b4SJRbY9rdLxUugL8BL1Aoxj142m-7TaYG_K6lpacyvNzDWAseP-SXtPFPamu1_5JZKN9J3CgkLhf6IlWxGkLLklyqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دیس‌سنگین ژوله به حرکت کنعانی‌زادگان روی گردن عارف‌آقاسی در بازی دربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107555" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107554">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=hTiRsxW__Z7JFVDCh43MJY8qDRHiD8RIZ6VoSovr5EiDWcBpIu50VjAfW8Z2yqI3jVpfmPo5Al7zB-e9gKPAt4Bk3o1g__aFY2vSx0LtfenmV9ruYhXfpsiN0CmBkxW4vuZ3PAGumd-xfIDotlYFFZATUM6k-kmHrWqvOG3cfj7X3mRav6vvJj5zARArV14goGWCHrCgA_Uw9g-eikjcrj14uXrLqKUJQHPqX6dGeJGLH2YLlK0EjtkRE5R_gNJjME7hzWU07tqkw8_Qzkk9mCVb5ra33fJF8cLM6Dn6M0Hi0PDtB81rFfy65p9pckOamxDZ8JXgZX5_QKWhxQJ49A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=hTiRsxW__Z7JFVDCh43MJY8qDRHiD8RIZ6VoSovr5EiDWcBpIu50VjAfW8Z2yqI3jVpfmPo5Al7zB-e9gKPAt4Bk3o1g__aFY2vSx0LtfenmV9ruYhXfpsiN0CmBkxW4vuZ3PAGumd-xfIDotlYFFZATUM6k-kmHrWqvOG3cfj7X3mRav6vvJj5zARArV14goGWCHrCgA_Uw9g-eikjcrj14uXrLqKUJQHPqX6dGeJGLH2YLlK0EjtkRE5R_gNJjME7hzWU07tqkw8_Qzkk9mCVb5ra33fJF8cLM6Dn6M0Hi0PDtB81rFfy65p9pckOamxDZ8JXgZX5_QKWhxQJ49A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش‌ ابوطالب به صحبت‌های مسخره حسین عبدی پس از شکست ایران مقابل کره‌شمالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107554" target="_blank">📅 16:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107553">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=ayXzRWNm9OxJ5yipHeePmFTjks-NbA1Js-IPYpQoEw2fxTSbCPEmLLUqD5JJg5ixwf3WkaxDryZAxxPPTKILGAGVluwUVjSwT5mCl51jMedZDIl9mTSaqfAf4c1tm5sOcKh6L8JstWkkG7muEBzE2ONjOjcJdeqRqld68JBlcDELwuSkf5YfhCj5bBGQeQMiGC9y9Meg22EkALrUEwcw7cs3TZ21rXFjfDIuXy5GiLLSNbpaQI6J-QXD1DUNmL4bdQijHSSJb3qixrrQeyrp75hQXIy25T_wdOORpaP-oiGgEaWsHvbSefQJ1G37EwnqUVQepD4evxYEhbwLbPAkJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=ayXzRWNm9OxJ5yipHeePmFTjks-NbA1Js-IPYpQoEw2fxTSbCPEmLLUqD5JJg5ixwf3WkaxDryZAxxPPTKILGAGVluwUVjSwT5mCl51jMedZDIl9mTSaqfAf4c1tm5sOcKh6L8JstWkkG7muEBzE2ONjOjcJdeqRqld68JBlcDELwuSkf5YfhCj5bBGQeQMiGC9y9Meg22EkALrUEwcw7cs3TZ21rXFjfDIuXy5GiLLSNbpaQI6J-QXD1DUNmL4bdQijHSSJb3qixrrQeyrp75hQXIy25T_wdOORpaP-oiGgEaWsHvbSefQJ1G37EwnqUVQepD4evxYEhbwLbPAkJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
همسر بیژن مرتضوی خبر از بازگشت این شخص به ایران را دقایقی‌پیش اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107553" target="_blank">📅 16:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107552">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=V4qfUjyKESi_IJkZCRAZfQNLea1PyK34Lf0R-7USnhdPrth2F8zyeiR_QiX_Nrg6gRoFniQP7TPuXGcrQ3f3r0e7eOh63DJXQMXOOls1q8LwAzI_3N2e-fR9odALiMrEbcUljc_a1wq9hcN0RCTZ58h7fD-DP5eJtxOqJfMkuXR48Nwt1cpbR9EvHboJWq6SIgyILP7RZBePFbxta_m0GAsC-8BAexAO-uk-GRIleLRvZznJRWhE2cQxxxdd8NUf7AZXfxYBIAziUVV0ce0BbgG3qHTw9-YaGhI9-nFbWc0yQGb0hfgknyxk4TG4PnxkS8vRAlPeo5i_b3une32JPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=V4qfUjyKESi_IJkZCRAZfQNLea1PyK34Lf0R-7USnhdPrth2F8zyeiR_QiX_Nrg6gRoFniQP7TPuXGcrQ3f3r0e7eOh63DJXQMXOOls1q8LwAzI_3N2e-fR9odALiMrEbcUljc_a1wq9hcN0RCTZ58h7fD-DP5eJtxOqJfMkuXR48Nwt1cpbR9EvHboJWq6SIgyILP7RZBePFbxta_m0GAsC-8BAexAO-uk-GRIleLRvZznJRWhE2cQxxxdd8NUf7AZXfxYBIAziUVV0ce0BbgG3qHTw9-YaGhI9-nFbWc0yQGb0hfgknyxk4TG4PnxkS8vRAlPeo5i_b3une32JPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
قلعه‌نویی میدونه ترند چیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107552" target="_blank">📅 16:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107551">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN71arI02wHi4Mk88KSvZ4Jkh2yP8Zz_pgS9OKBNGKfaL6FliJlJaheABnmaV2-eUEuLd24KktW95Uuamc0uCwrKHpOOD3Glso27CIwR8hR-FgPOy5WQCweVjF4DPsW3t5OlT3v1UkGn_vRfSnhRrNzNOSyfo5EFZm2bNqyDSatsuh6p0ZNeqoAyqovSvfOnm_9GbCPQzE-e5JVh8LiC_6uV_zy4bGcIcyrrIHpp2qA_4vjPXHRNhqrAW3e-amMBijEbnDfAH2vI48sFxwxJhokHt5RK8tS_AYoc1gZH28MCn9KI5mcKWT0u1StDWBDOucU9zWmVymDKfdSzbrwd-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
⚽️
برای اولین بار از زمان رقابت‌های یورو 2008، کریستیانو رونالدو در تمام طول یک مسابقه، نیمکت نشین بود و حتی یک دقیقه هم برای پرتغال بازی نکرد.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107551" target="_blank">📅 15:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107550">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=QlF3uUdOwqwdeWSi46gtAWhZNQ_inYda1mBRnNpL4s_x8ElOO72jHfAoJAIviV7cYfstAY5MopBhLrlcDHFPmr9MPFnVIgarhYpYCIJGlwZ86Jm1HJgDbNBacI7TidfzRzkd4sDuU5A2O3lBv9DXzmQX364MbpnITQZbtGNN5W83YShc-5q9c0uKA19Cn7dUAQyBqRPydg1waiphyRuqIjtODZgbTNBKIh6ee7_sDyZ6lzn2FdL9PMlXOkP0fdHvtSgIGjvxdstWLr0RrSmPI1yBJ-dC7D9_qA5VMkau97YSIf_PbG8Z1L_fFhkah7GzGYnyHwVY6Mz9Fpk3D84MMQXAfr3xA8w3zMgmxJFZZR1oan64Yvp78O1G3Pajp0lPUM5vOJcdyNeBmvrjXWbFTn4AsTuibUO21XW7ofj33lWWuYd6ctY-1Dg5Tp0Uv023MMBNluZK4QbgLQFphCMCD7zSBEHhuf6NrY11e0NZuKrcAWSkq13nPDvEI5_YyWn_Tg_BaSwO4GELyYSqdqvL5T7obIHz6mg-C9Y98h5bYm0kfyeKLPfTOfZ1E9wEppwR9P4exiQyFIC9Ivi4Nr2fpItPFgP0dfZvVGzDslnsymwMADL4652F22iDmkfFZGofR-xMS90VTTLi_lfss2PK8_XYAOhMcRGPG7kb4Yy6q1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=QlF3uUdOwqwdeWSi46gtAWhZNQ_inYda1mBRnNpL4s_x8ElOO72jHfAoJAIviV7cYfstAY5MopBhLrlcDHFPmr9MPFnVIgarhYpYCIJGlwZ86Jm1HJgDbNBacI7TidfzRzkd4sDuU5A2O3lBv9DXzmQX364MbpnITQZbtGNN5W83YShc-5q9c0uKA19Cn7dUAQyBqRPydg1waiphyRuqIjtODZgbTNBKIh6ee7_sDyZ6lzn2FdL9PMlXOkP0fdHvtSgIGjvxdstWLr0RrSmPI1yBJ-dC7D9_qA5VMkau97YSIf_PbG8Z1L_fFhkah7GzGYnyHwVY6Mz9Fpk3D84MMQXAfr3xA8w3zMgmxJFZZR1oan64Yvp78O1G3Pajp0lPUM5vOJcdyNeBmvrjXWbFTn4AsTuibUO21XW7ofj33lWWuYd6ctY-1Dg5Tp0Uv023MMBNluZK4QbgLQFphCMCD7zSBEHhuf6NrY11e0NZuKrcAWSkq13nPDvEI5_YyWn_Tg_BaSwO4GELyYSqdqvL5T7obIHz6mg-C9Y98h5bYm0kfyeKLPfTOfZ1E9wEppwR9P4exiQyFIC9Ivi4Nr2fpItPFgP0dfZvVGzDslnsymwMADL4652F22iDmkfFZGofR-xMS90VTTLi_lfss2PK8_XYAOhMcRGPG7kb4Yy6q1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
دیس امیرمهدی ژوله به جنجال خداداد عزیزی نسبت به پاهای پرانتزی امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107550" target="_blank">📅 15:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107549">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=VrvyPSlhpEsxTYA9bghE156V2BfLimCezKMpK2Z7ZriOV4n4iZEJA9ZmbLDkC68gAQkqgVl8QMDdWR8UrFkDq5h_sAkExkojxbg23gZiYYananrFA-aBWtwe18XFDjQU2YZOZBpXR_sAOUcKAVk0vrshWZYw68hbYZz7u7_V7Uej20_Sxm4VohJrLlYj4bcBXO8_qkko2yinKDLn2-9wczMD2e3ua6wAB4EvrliiqI5-h3Un2o5JQBUJr3o3qXBPA7_Ahh9FRs-nSt6nC9VqvxswwKV-zMC6Y8hUCKjY9FDVkQ1NcQE0e1ameBYDP-1nnp4n9xGGAczfbiL3Du_tQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=VrvyPSlhpEsxTYA9bghE156V2BfLimCezKMpK2Z7ZriOV4n4iZEJA9ZmbLDkC68gAQkqgVl8QMDdWR8UrFkDq5h_sAkExkojxbg23gZiYYananrFA-aBWtwe18XFDjQU2YZOZBpXR_sAOUcKAVk0vrshWZYw68hbYZz7u7_V7Uej20_Sxm4VohJrLlYj4bcBXO8_qkko2yinKDLn2-9wczMD2e3ua6wAB4EvrliiqI5-h3Un2o5JQBUJr3o3qXBPA7_Ahh9FRs-nSt6nC9VqvxswwKV-zMC6Y8hUCKjY9FDVkQ1NcQE0e1ameBYDP-1nnp4n9xGGAczfbiL3Du_tQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
جام جهانیه یا مسابقه‌ی انتخاب کراش جهانی؟ کنایه ابوطالب به لیست نفرات قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107549" target="_blank">📅 14:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107548">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=XR4sYzwvCLs5IETBNAE62qRHrQuhmklCMS-AHeFwDymsxqS0k3g7E9s4KdgeyirewDCusmxrMshMCrLUSdYGfgxCx84YOiKlUkaOpNR0RbmZloBEH_nUuysHA6e_alDjdDnVufpnS9TAglWkHckOw58rSWJZdgBQPUWI7iX5_FPJJ3EgTC6irvTc_Po7iOjfWqx9QppoXnaqMS3_OTm-cEOfF5jPvCUqKZluc0OXnetozQhiC4VGxXTBWtVJgsVvVCyCpuKQf35SpN1ApnMZPcbLw2r3CP-uSOq6-oneq4KW_dvw2RbLSNqN5IA9HhFTPWza8oE0Z4LhiemfuKhoQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=XR4sYzwvCLs5IETBNAE62qRHrQuhmklCMS-AHeFwDymsxqS0k3g7E9s4KdgeyirewDCusmxrMshMCrLUSdYGfgxCx84YOiKlUkaOpNR0RbmZloBEH_nUuysHA6e_alDjdDnVufpnS9TAglWkHckOw58rSWJZdgBQPUWI7iX5_FPJJ3EgTC6irvTc_Po7iOjfWqx9QppoXnaqMS3_OTm-cEOfF5jPvCUqKZluc0OXnetozQhiC4VGxXTBWtVJgsVvVCyCpuKQf35SpN1ApnMZPcbLw2r3CP-uSOq6-oneq4KW_dvw2RbLSNqN5IA9HhFTPWza8oE0Z4LhiemfuKhoQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پاسخ ابوطالب به انتقادها از برنامه‌فان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107548" target="_blank">📅 14:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107547">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=abOfxnklF0sYAyC9Fyvb86F4xZyZHm6R_IC__kBowvFgk7ecAtOaaKdbwxObHA0dv4M9broyjTtP7DOdvsgPP4hNHmdyqAhW-1TzMLXLuaxoE0g9kx0uHBKKZRpetBg05pEL9iXry2iTOLy2TUQDNjEpmv6qlyoQPG8vRwsCHTRA_EC8rtrahCEVhW2Uo90dIU4rIqAnAas79g1JlAQcQWvmuFYf1CPoWSdbfQfO1cC0VzWWQbMd1130X254kqUbQiVEqi_uJVKWxkmk009hBaU3tHnLkE7EUFQF3egAXcPBJbiHEiWGyNRNzsNvYK87FFsnuIXp9Lct2myEZJouULlVEoDke-VbR1jYHB2Yxnsy9MHuVG0qJy7mCQ-Dq1LYkQdlFiQjrHLvyH0TtndhnNgvDJGeoOnD_cqAoYt1OLoII_AvTnL0PzuGe2CUrnI4IaW0428bDevRZ4X4gmTApJxT1nJ0BRzxnI_FSEqF5BkDxtlNpPYo-EYLHQuMy7DWEIr1duoOPVAfXL6-N9C3gbEWlIEDmJrD7b-ICZcYb1Q-0YsVtPnU940jUB3Ii44FMWHpwLZPPvNJA-UPoa5ylUskOGX6vPUBdUvhA3yIKWNedkgVQyNIpphfWLYCLEniUGCpOHHdd3_KYUVcYe8LuMO6Zpn5SYSNx42SrtXhgso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=abOfxnklF0sYAyC9Fyvb86F4xZyZHm6R_IC__kBowvFgk7ecAtOaaKdbwxObHA0dv4M9broyjTtP7DOdvsgPP4hNHmdyqAhW-1TzMLXLuaxoE0g9kx0uHBKKZRpetBg05pEL9iXry2iTOLy2TUQDNjEpmv6qlyoQPG8vRwsCHTRA_EC8rtrahCEVhW2Uo90dIU4rIqAnAas79g1JlAQcQWvmuFYf1CPoWSdbfQfO1cC0VzWWQbMd1130X254kqUbQiVEqi_uJVKWxkmk009hBaU3tHnLkE7EUFQF3egAXcPBJbiHEiWGyNRNzsNvYK87FFsnuIXp9Lct2myEZJouULlVEoDke-VbR1jYHB2Yxnsy9MHuVG0qJy7mCQ-Dq1LYkQdlFiQjrHLvyH0TtndhnNgvDJGeoOnD_cqAoYt1OLoII_AvTnL0PzuGe2CUrnI4IaW0428bDevRZ4X4gmTApJxT1nJ0BRzxnI_FSEqF5BkDxtlNpPYo-EYLHQuMy7DWEIr1duoOPVAfXL6-N9C3gbEWlIEDmJrD7b-ICZcYb1Q-0YsVtPnU940jUB3Ii44FMWHpwLZPPvNJA-UPoa5ylUskOGX6vPUBdUvhA3yIKWNedkgVQyNIpphfWLYCLEniUGCpOHHdd3_KYUVcYe8LuMO6Zpn5SYSNx42SrtXhgso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز بازی انگلیس مقابل اسپانیا که حاوی نکات بسیار دیدنی برای علاقه‌مندان به فوتباله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107547" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
رونمایی فدراسیون از معیارهای تعیین رده‌بندی و قهرمان در صورت لغو فصل:
🔻
۱-در صورت برگزاری حداقل 75 درصد مسابقات رده بندی بر اساس جدول موجود.
🔻
۲- در صورت برگزاری کمتر از 75 درصد رده بندی بر اساس میانگین امتیاز در هر مسابقه.
🔻
۳- در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
🔹
تبصره: سازمان لیگ می‌تواند با تصویب هیئت رئیسه روش عادلانه‌تری را جایگزین کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107546" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=QMwSs2G8HGdZ2Tq5AM0t29k4fJR4MYQJ9wtE8Glf5vezv3zS5p0VoLub_Cj1P_Ai_zKWTspuySd1pkWoUc4_Q64xnWit3C9AEQBSXtq52QGM34Yw_Z_SlbyVsCKh_CGuPN0jsxncRAWrlcjDewbRAL8aL96aK7OlPGgiHrHowgkAEZM9AuKK1pihuClGH37t3i5ELnINNdocRHqs2iZdHNA7PuLHPHDz7sKGZdORg9m7QBdqPxDF-vttsV8l2fTXrl7_tx30iJolhyHOgA-Xctwtgze8L0CcZpYi2SBPJmPuJtdRkrjmoFuZTgZCYnH5QeU0r09HMDV-KKAJ70DIhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=QMwSs2G8HGdZ2Tq5AM0t29k4fJR4MYQJ9wtE8Glf5vezv3zS5p0VoLub_Cj1P_Ai_zKWTspuySd1pkWoUc4_Q64xnWit3C9AEQBSXtq52QGM34Yw_Z_SlbyVsCKh_CGuPN0jsxncRAWrlcjDewbRAL8aL96aK7OlPGgiHrHowgkAEZM9AuKK1pihuClGH37t3i5ELnINNdocRHqs2iZdHNA7PuLHPHDz7sKGZdORg9m7QBdqPxDF-vttsV8l2fTXrl7_tx30iJolhyHOgA-Xctwtgze8L0CcZpYi2SBPJmPuJtdRkrjmoFuZTgZCYnH5QeU0r09HMDV-KKAJ70DIhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تصاویری از علیرضا بیرانوند با لباس سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107545" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107544">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=GPKqY8kVoKd9-Co4QSmx4g-ldyT6eb-Io7mJCsHNNJrMFUtUC0xNLbOIjzJzkMGS1eBj0RverNQRZElq-Y9JZWSmCRGpxqNeb0wZP24nAEuJ9RM0FsHcNnPqLNB4YBxqxkuJVyvgUPnv4Gm8tfOQ2vV-kP9PStXraZX6CeTtWkxNPRbjgKkGyTbYXykb7BgPJpC7t-JFg5YNqBIxJeMpWQAeCBUgG0JyDQCVtkAPS8F6X2XXWcJpUd0HIEZZuqorokYBzkKU3BIden8UqTkdyn2LvaqIUd6efssx5bBAUIfK4mDFp5yrdgwNj6RqMSupkRbh21FTEVDQ5QrzxjBuVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=GPKqY8kVoKd9-Co4QSmx4g-ldyT6eb-Io7mJCsHNNJrMFUtUC0xNLbOIjzJzkMGS1eBj0RverNQRZElq-Y9JZWSmCRGpxqNeb0wZP24nAEuJ9RM0FsHcNnPqLNB4YBxqxkuJVyvgUPnv4Gm8tfOQ2vV-kP9PStXraZX6CeTtWkxNPRbjgKkGyTbYXykb7BgPJpC7t-JFg5YNqBIxJeMpWQAeCBUgG0JyDQCVtkAPS8F6X2XXWcJpUd0HIEZZuqorokYBzkKU3BIden8UqTkdyn2LvaqIUd6efssx5bBAUIfK4mDFp5yrdgwNj6RqMSupkRbh21FTEVDQ5QrzxjBuVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚽️
توصیف امیرحسین قیاسی از امیر قلعه‌نویی: جوان‌گرایی و تاکتیک مناسب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107544" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107543">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=v_oQeqvYFnFcMgH_95-BwlGX1pVxtYpta1onMV4ysW4T3JGfPZiutxntZOHFR3y2daD8xF3qOZDjwuxTNfarCrZLudwwKC1hBFvjPfvg3lNacHyWGQGMtZIVvbFVk8QaznDoopnUSpBSrvxGtdMSVYJxrCCybgpoMEICbuAbAtTUxJ3N0zI1RBBG1Mq2JOJdbL9Yg7S3GBemAdVwSCzjLgkmRWedHOWGoNiHMAJ7zldzTndqMzkzc9KqqgiVEemnfsy9kzxs8rZ6y3br67PgZQMRoghNnP6rJioRHq3zKMzDfLdojKAwUVF7MKBYWktk48u79CBstjUvOF0gX-qwqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=v_oQeqvYFnFcMgH_95-BwlGX1pVxtYpta1onMV4ysW4T3JGfPZiutxntZOHFR3y2daD8xF3qOZDjwuxTNfarCrZLudwwKC1hBFvjPfvg3lNacHyWGQGMtZIVvbFVk8QaznDoopnUSpBSrvxGtdMSVYJxrCCybgpoMEICbuAbAtTUxJ3N0zI1RBBG1Mq2JOJdbL9Yg7S3GBemAdVwSCzjLgkmRWedHOWGoNiHMAJ7zldzTndqMzkzc9KqqgiVEemnfsy9kzxs8rZ6y3br67PgZQMRoghNnP6rJioRHq3zKMzDfLdojKAwUVF7MKBYWktk48u79CBstjUvOF0gX-qwqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین‌قیاسی درباره سفارش غذا ۶۰ میلیون تومانی برای مهران‌مدیری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107543" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107542">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=gfLmz1whFs7HlVcFrWjcD-99RZI2AnIEngHP-x7ZOsEDkF-_r_Eeduja6h4pbizAVMevyJPtvKTkha1I5HC8p_qbkFZywW2EOj5pkIoRn4o8_ZlayDlQJsVR4KoakAW8q9S3j9SBjS_bAeGKPwPabi7c4a7PEil81DpclgVvEMutpHvpj0505NyHkj_PhPLPuzVLqZvg2sgvtBoRZ3i6frXP2esoKE529DvOEG6S5O37rvAT5wSjC9aE6xDXl0qBdc6_BZXfVxZqNsEvyDV0D63nXArpqJXNABTZ7L8dTgVmELGrdRggm7ismJM7rSm4Zv-J3clfS_PNbR3BX-y9UpvJusJGaOJPot96ECLiiGp2RSH-LK2lIwQ_83vZsumFSoLWtRHS3nsbEabwaI1z8uGREBBgPrJyYytyp5lVp76uH6N1zP-8RC5CRXEhYYeghrw_n1EMdj5tOIsYkhu2iPgepN1fcbNVNd5Rl0GIpn5pw9VNvjLx5GMZyuqIfEgEBQiGIPra-ae4duKQYPw1HmOYBkWdyytnZMcT4fhLIJuKADE6i8MY_fPTO80N0AbxZjePCkCAH5Py3unv7FwhzgSoCugNLGo0ORqgDJkIdy-ekWTFsAiY61YoQE4RXK58PiZA4OJuCjkDCLAlrpvZnWbTv54mrbRsJ4cqW4DoDME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=gfLmz1whFs7HlVcFrWjcD-99RZI2AnIEngHP-x7ZOsEDkF-_r_Eeduja6h4pbizAVMevyJPtvKTkha1I5HC8p_qbkFZywW2EOj5pkIoRn4o8_ZlayDlQJsVR4KoakAW8q9S3j9SBjS_bAeGKPwPabi7c4a7PEil81DpclgVvEMutpHvpj0505NyHkj_PhPLPuzVLqZvg2sgvtBoRZ3i6frXP2esoKE529DvOEG6S5O37rvAT5wSjC9aE6xDXl0qBdc6_BZXfVxZqNsEvyDV0D63nXArpqJXNABTZ7L8dTgVmELGrdRggm7ismJM7rSm4Zv-J3clfS_PNbR3BX-y9UpvJusJGaOJPot96ECLiiGp2RSH-LK2lIwQ_83vZsumFSoLWtRHS3nsbEabwaI1z8uGREBBgPrJyYytyp5lVp76uH6N1zP-8RC5CRXEhYYeghrw_n1EMdj5tOIsYkhu2iPgepN1fcbNVNd5Rl0GIpn5pw9VNvjLx5GMZyuqIfEgEBQiGIPra-ae4duKQYPw1HmOYBkWdyytnZMcT4fhLIJuKADE6i8MY_fPTO80N0AbxZjePCkCAH5Py3unv7FwhzgSoCugNLGo0ORqgDJkIdy-ekWTFsAiY61YoQE4RXK58PiZA4OJuCjkDCLAlrpvZnWbTv54mrbRsJ4cqW4DoDME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مارادونا: ۴۰ تا بازیکن از تیمای مختلف ایتالیا روی هم،  به اندازه یه توتی نمیشن!⁣
اسطوره رم ۵۰ ساله شد.
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107542" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107541">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4869197932.mp4?token=iqbi-fYjYMcI1fnCZl9RIoVw1VG3zi5P62P1PLzf30MijXd4o0MhtYv9kd1idGAA5k4cpRIfngQQlROxtHA81WCWhJMyAHaS21pTU3gOErknUsOVn7MgRdQSi4PrG_pa-ctJZgtd0VQFHiMVbJ-YqfN6RDgTpTLBWoF4BqGnyRh5oJJt6HsYUM8a6jdkIlzNTZYEdOkdfwSVmE-pt2HZe9KEz49g_GU2qDjeJ1u8YzkdxM2ucLMYj8aDeMLhveYQTHaeMWQi8pCNiPz8kOxbPANzm3EAv9sooqv_oxxzMIVz7AuZEIHAkiIjMzgRDisQNzwiA2tm4pe7sUgyA2HiYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4869197932.mp4?token=iqbi-fYjYMcI1fnCZl9RIoVw1VG3zi5P62P1PLzf30MijXd4o0MhtYv9kd1idGAA5k4cpRIfngQQlROxtHA81WCWhJMyAHaS21pTU3gOErknUsOVn7MgRdQSi4PrG_pa-ctJZgtd0VQFHiMVbJ-YqfN6RDgTpTLBWoF4BqGnyRh5oJJt6HsYUM8a6jdkIlzNTZYEdOkdfwSVmE-pt2HZe9KEz49g_GU2qDjeJ1u8YzkdxM2ucLMYj8aDeMLhveYQTHaeMWQi8pCNiPz8kOxbPANzm3EAv9sooqv_oxxzMIVz7AuZEIHAkiIjMzgRDisQNzwiA2tm4pe7sUgyA2HiYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🇳🇱
یک‌ماجرای جالب از فوتبال هلندی - بلژیکی!
خانواده آقای فن‌بومل، خودش، پسراش، زنش و البته پدرزنش⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107541" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107540">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=nIXKBlRevdN0q1Cjzt8HmC8tnr2xLwDGmVnBhumfW71M8o1KxAmBRXAOMKq-_jTEAmM5sLUcEsHAgCIwmUWj2OpVLDFJkYkDo8RX3xj-WZquw_Bcqn3kAclzG1tST_sIw7BPMRJN_kTujDlJui4o6aUS4m1maeCh4lbGfrZPaee_VusFMJh5Q_3Y2Tkv2xiSd7xJMR80uvsaxkH_dhrKoKD7-j-jwqqOcEGjHqmaluizuLUZfHGqkKZkuJ_SjqQkkVV33yO2N0ZnvqgZCNZ7UsHrZea7dK4v59h3hSBMtcstb5dESmnR4a11O-fgYCS3khq3Wvy89Soc4tMdriwqfQlleC5QyD1gd7dCaP2Ymza5Y5eSErF5WSo0QE_L47DLknLlnxFnfrhpL9SuYsekbqEzv1epPhVOjOqE0oeB2wbLo-o-usI7bvlqyEtjoqduaPv8nbNDaixVkYhHgPnh-XPA4fbhgTJq3yvOEVzFQ4yfAICrL-DySge4vvbp9sruJYTxq43_PV-Pd32OJ_Ld17gQnmF_Wu7PSt3uX5bHhHkgbWx-eHLbyUS35fpYSpngh1d9cCxEsHSqjCoCjS0VIoBBBbn-yxwksHGYLABYo_hdPKq2NZlq6Bk7FuPuAngc7bn-0BhV557QkbqLRBsDWwiV1hhk6K2FgmmSlhdfGXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=nIXKBlRevdN0q1Cjzt8HmC8tnr2xLwDGmVnBhumfW71M8o1KxAmBRXAOMKq-_jTEAmM5sLUcEsHAgCIwmUWj2OpVLDFJkYkDo8RX3xj-WZquw_Bcqn3kAclzG1tST_sIw7BPMRJN_kTujDlJui4o6aUS4m1maeCh4lbGfrZPaee_VusFMJh5Q_3Y2Tkv2xiSd7xJMR80uvsaxkH_dhrKoKD7-j-jwqqOcEGjHqmaluizuLUZfHGqkKZkuJ_SjqQkkVV33yO2N0ZnvqgZCNZ7UsHrZea7dK4v59h3hSBMtcstb5dESmnR4a11O-fgYCS3khq3Wvy89Soc4tMdriwqfQlleC5QyD1gd7dCaP2Ymza5Y5eSErF5WSo0QE_L47DLknLlnxFnfrhpL9SuYsekbqEzv1epPhVOjOqE0oeB2wbLo-o-usI7bvlqyEtjoqduaPv8nbNDaixVkYhHgPnh-XPA4fbhgTJq3yvOEVzFQ4yfAICrL-DySge4vvbp9sruJYTxq43_PV-Pd32OJ_Ld17gQnmF_Wu7PSt3uX5bHhHkgbWx-eHLbyUS35fpYSpngh1d9cCxEsHSqjCoCjS0VIoBBBbn-yxwksHGYLABYo_hdPKq2NZlq6Bk7FuPuAngc7bn-0BhV557QkbqLRBsDWwiV1hhk6K2FgmmSlhdfGXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
روایت عجیب و غریب میثاقی از معافیت پزشکی برخی از فوتبالیست‌های مشهور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107540" target="_blank">📅 11:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107539">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=sswRtplAQsB1_RL0ZjCao2NGSUqikkdaYW7db41AoNg8SHma3FOWFBMYBSU70vc5ztQsTEJNMe1ITcue78Wk5Q0IrU-AlRxQA5I6O0n_rtfEuXSQO3ugFb8OyaS7ATN7xzfyq_EpmIQKOjQ2tN97hysAlrKY708GKzPl1Ks5EHyhcbOOU9zR4l3FF98sZe4idO0rjyGOq60RNO6YxdnEf2NDHv6Z0EXkQcB5sn_v3voRuKGV_Nr2L6LD9RY7t-zyWN46q3Y2XNHv6wAfCBvB0lauTzCG2o0ubAdRTALqSDnKru1YRFJStZ-3dTgC8032KVxerUdAUh7jddU82FHjsHhCMVjwFkeeY6_eEl4UJ3hHnaSUnvX8FSxFoeqFaTP6a_dUKKQNXCaqz98kP0j_qCfQP4iq1H1S3Rvoi70atkoBIUm2YIkslNdDjTT1Nmcuvl5w6mTrfICDsyjhDCs6nIO9AWVvSLtPjigw4ETRyW_1wDERL52E-iPPWDDr08C2JRTQmxKmQPXqkzoZZAw9d0Sf24jPG3xsiV7GN-18WZpopdX0i193Nqv4du3x9ltfm7Iy0E8WVxZgQBWBkS9u5IPvW5oKq1FDTLIjFDQLGR9C14ymo4B_3WYEhvYtnzJnRaGQnKlQldwGOhECKiRQ-V_PyUxQ23Y3Tr_BOUf_Fmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=sswRtplAQsB1_RL0ZjCao2NGSUqikkdaYW7db41AoNg8SHma3FOWFBMYBSU70vc5ztQsTEJNMe1ITcue78Wk5Q0IrU-AlRxQA5I6O0n_rtfEuXSQO3ugFb8OyaS7ATN7xzfyq_EpmIQKOjQ2tN97hysAlrKY708GKzPl1Ks5EHyhcbOOU9zR4l3FF98sZe4idO0rjyGOq60RNO6YxdnEf2NDHv6Z0EXkQcB5sn_v3voRuKGV_Nr2L6LD9RY7t-zyWN46q3Y2XNHv6wAfCBvB0lauTzCG2o0ubAdRTALqSDnKru1YRFJStZ-3dTgC8032KVxerUdAUh7jddU82FHjsHhCMVjwFkeeY6_eEl4UJ3hHnaSUnvX8FSxFoeqFaTP6a_dUKKQNXCaqz98kP0j_qCfQP4iq1H1S3Rvoi70atkoBIUm2YIkslNdDjTT1Nmcuvl5w6mTrfICDsyjhDCs6nIO9AWVvSLtPjigw4ETRyW_1wDERL52E-iPPWDDr08C2JRTQmxKmQPXqkzoZZAw9d0Sf24jPG3xsiV7GN-18WZpopdX0i193Nqv4du3x9ltfm7Iy0E8WVxZgQBWBkS9u5IPvW5oKq1FDTLIjFDQLGR9C14ymo4B_3WYEhvYtnzJnRaGQnKlQldwGOhECKiRQ-V_PyUxQ23Y3Tr_BOUf_Fmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
‼️
سه‌ سال و نیم بدون رشد و تغییر در ترکیب نفرات دعوت شده توسط قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107539" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
