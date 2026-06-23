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
<img src="https://cdn4.telesco.pe/file/jEVfE9TVkbI1P9uPkkDDb1LS0R0JVmcuABZnqPSmMbGaGrPZDYWye6DlkKmSAvTTonTPUTiHyjd2QnyR6y7ilTC_OZt8TFRPTKzOk6f0a3Kpk6hn4R5YYkaLA2z10YUq34Fdht9M01ByMduqwVtWacInfYt0h3OK7oCCZ24yc3X8Iaaik1K5oho41tN9Mxaoe32JAP6jjsiVYbVFmt-pZfHdpEwQ5eXbgJRmUYuP8j7pV899kHn4QBDvj1o7qqeOYvk_QuZxQAZ9opAvCfcclKoW5Yq5U9mrbmsKmrMeAfCzo6T7nyvLCpvdjYd0-K8Lp5hiZR0ED1RTUrgL7gEwxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 11:54:03</div>
<hr>

<div class="tg-post" id="msg-662563">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
بقایی: ظرف ۳٠ روز از توافق نهایی نیروهای آمریکایی باید از منطقه پیرامونی ایران خارج شوند
🔹
جزئیات این گزاره باید در حین مذاکرات مورد بحث قرار گیرد.
🔹
یک تعهد دیگر این است که آمریکا در حین مذاکرات به نیروهای خود در منطقه اضافه نکند
🔹
ما این موضوع را به طور…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/662563" target="_blank">📅 11:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662562">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بقایی: مطلقا موضوع توانمندی دفاعی و موشکی ایران به هیچ عنوان نه بخشی از گفتگوهای ما بوده و نه هیچگاه موضوع مذاکره با هیچ طرفی خواهد بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/akhbarefori/662562" target="_blank">📅 11:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662561">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: پس‌از تهدیدهای ترامپ مذاکرات را ادامه ندادیم
🔹
در وقفهٔ بین مذاکره با تهدیدهای موهن مقامات آمریکایی مواجه شدیم و پس‌از آن نشست چهارجانبه تشکیل نشد. ادامهٔ بحث‌ها فقط تبادل پیام از طریق میانجی‌ها بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/662561" target="_blank">📅 11:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662560">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بقایی: توضیحات بقایی درباره خروج خبرنگاران از سالن اجلاس چهارجانبه: ما برای کار رسانه‌ای و تبلیغاتی به سوئیس نرفته بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662560" target="_blank">📅 11:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662559">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=PHZ9wtiylzCxUAFxlhKQIde09J9IYn6dIVIM4Ek2h1F-5J53ae1z1kyH7VkMfcsTs2UIFNmET83kz6eQL9ZqSPXU3VrAaA0Ns3seTSnwA9EB0lifla0CDGpThKlSzXhlhfyl5nT-Sv_vSkNyS3XRVIlrcTBhexKjNWd8kNl6dyfL6w0Mu7iW0NNRqpCaCUzBpp1Mog_XkWLDdqdZwkiOjb41VU4QmjQqB9lxz12AH1MuinLSTdo3j6yVGC04V1XWQFAJt4kUyG7YV6IvQH79X3Lt8KYPydrBHPgmyrkXkKdL_8URItJHRh3XESACxsGlHMm51pGrWcKon1oW2bqb-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=PHZ9wtiylzCxUAFxlhKQIde09J9IYn6dIVIM4Ek2h1F-5J53ae1z1kyH7VkMfcsTs2UIFNmET83kz6eQL9ZqSPXU3VrAaA0Ns3seTSnwA9EB0lifla0CDGpThKlSzXhlhfyl5nT-Sv_vSkNyS3XRVIlrcTBhexKjNWd8kNl6dyfL6w0Mu7iW0NNRqpCaCUzBpp1Mog_XkWLDdqdZwkiOjb41VU4QmjQqB9lxz12AH1MuinLSTdo3j6yVGC04V1XWQFAJt4kUyG7YV6IvQH79X3Lt8KYPydrBHPgmyrkXkKdL_8URItJHRh3XESACxsGlHMm51pGrWcKon1oW2bqb-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: توضیحات بقایی درباره خروج خبرنگاران از سالن اجلاس چهارجانبه: ما برای کار رسانه‌ای و تبلیغاتی به سوئیس نرفته بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/662559" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662558">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e39941421.mp4?token=bfLdBJ4hRuw8YhY-8qWZYbBp-aW9hmyAPEAo3Id3YhEpK4dHLx3SD3PvShwlEaWbztozZsuyrO6Q90xE60Xfvs92WWyxRGm5sMNagdI4U4mJDrwhpjnPxuMK3sOXRfOy4PznEaeSl1I0A4TaIAxTtvDI9mDEEho79glGAxDF8L5f6qCVFLOckW-c4SVp8McRxovKeSCx87jud8QewqWcoiYwsrQJJ0VXJA_SMvKCzjrbJ8Ciw2dKAA_FyDB2eeA_LnobxsoDTHO3AldI5miEGirOYFx9cWidnw-UWKb1Mgsc2ngSed-j0tKt3V3blAMmBt5WVQnYdKzFosxMWn5tkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e39941421.mp4?token=bfLdBJ4hRuw8YhY-8qWZYbBp-aW9hmyAPEAo3Id3YhEpK4dHLx3SD3PvShwlEaWbztozZsuyrO6Q90xE60Xfvs92WWyxRGm5sMNagdI4U4mJDrwhpjnPxuMK3sOXRfOy4PznEaeSl1I0A4TaIAxTtvDI9mDEEho79glGAxDF8L5f6qCVFLOckW-c4SVp8McRxovKeSCx87jud8QewqWcoiYwsrQJJ0VXJA_SMvKCzjrbJ8Ciw2dKAA_FyDB2eeA_LnobxsoDTHO3AldI5miEGirOYFx9cWidnw-UWKb1Mgsc2ngSed-j0tKt3V3blAMmBt5WVQnYdKzFosxMWn5tkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلفظ درست ماه‌های میلادی و مصادف تاریخ شمسی آن‌ها را یاد بگیریم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/662558" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662557">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800218067c.mp4?token=RZ3V7TwRa4IZKrFo60f8rJiiciec7QNBr6kVbp7jEPeb7duompxW6Th1JNKEcOmQZQNwWt0qABeaYpPGzBIOo-bm9RCx4K7D9exJFaSYpQryQ9QRtp1HftUbJHlTQTl7aoZ-8tX5r5oczW3oOASYm6JwIA9RhidPrcs4q8GnMJfIb9QbHQbmxClQVM9rHV9D3vw4wMYTu_PO36fIWeEhr66H-ey6X5msCxjOkZFueQixZ5cD1jpDi4-RBm6oRNzsr1l3Z7WQ-WjSNJoEXlZrreZTEEqrgrVNI-2bxM95pWeCBVH8W0YudL_RYafuvSniMtrkyTl6RTCy2A_PUXOZxyt-mdG7YL0n93REpeTd8YRgS2dE6XPZUzmpLT3HjUHlU1YAcFCroht0XNP6s87uYXj_ixfme5v-OEyFaa58WQs_mBuvz7LzCQiADu9I1FBTDbR_fi0T0cPrNDi-n5ElyfuahGMqj3aciGojYuXxBrs_zqn0LDrrIW4n7kGME1n1H_gmKPL-hUa7sKDN-XvtiIhnfrnkG5_dRXCoc910-wgLJqiLzrmM68ooxrbgwissdv0eniW0F1A7jWghZa0P0Bd4Pw4Vuy5BNapPSSLMSqN-8CLubDKLgjGCIfUBuWIa21dXjcPk8QNcmaRiEhOEo78LOZ6hdDXzO1YFqktGYCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800218067c.mp4?token=RZ3V7TwRa4IZKrFo60f8rJiiciec7QNBr6kVbp7jEPeb7duompxW6Th1JNKEcOmQZQNwWt0qABeaYpPGzBIOo-bm9RCx4K7D9exJFaSYpQryQ9QRtp1HftUbJHlTQTl7aoZ-8tX5r5oczW3oOASYm6JwIA9RhidPrcs4q8GnMJfIb9QbHQbmxClQVM9rHV9D3vw4wMYTu_PO36fIWeEhr66H-ey6X5msCxjOkZFueQixZ5cD1jpDi4-RBm6oRNzsr1l3Z7WQ-WjSNJoEXlZrreZTEEqrgrVNI-2bxM95pWeCBVH8W0YudL_RYafuvSniMtrkyTl6RTCy2A_PUXOZxyt-mdG7YL0n93REpeTd8YRgS2dE6XPZUzmpLT3HjUHlU1YAcFCroht0XNP6s87uYXj_ixfme5v-OEyFaa58WQs_mBuvz7LzCQiADu9I1FBTDbR_fi0T0cPrNDi-n5ElyfuahGMqj3aciGojYuXxBrs_zqn0LDrrIW4n7kGME1n1H_gmKPL-hUa7sKDN-XvtiIhnfrnkG5_dRXCoc910-wgLJqiLzrmM68ooxrbgwissdv0eniW0F1A7jWghZa0P0Bd4Pw4Vuy5BNapPSSLMSqN-8CLubDKLgjGCIfUBuWIa21dXjcPk8QNcmaRiEhOEo78LOZ6hdDXzO1YFqktGYCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مجوز فروش نفت و محصولات پتروشیمی دیروز صادر شد و از همان زمان قابلیت اجرا دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/662557" target="_blank">📅 11:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662556">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
بقایی تکذیب کرد: نه دیداری با گروسی داشتیم و نه برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای آسیب‌دیده ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/662556" target="_blank">📅 11:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662555">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3207303375.mp4?token=NkmWgukWo6eKuaiIQiUtOM_m9gIQio0onNy37lpOewB5nHOUJXDJJkicfXf4vqLGMnG5XYDsa5OvJKy_QvLJLodT-ox5VI4UMhYrwgdqs5W-y-HnGkInSfKYawu--ukpHx6Yg-ZET0F0rXrxSXoeAWpXNbW7W0PP7lpFSFTo0OffoZ7KDzdeJqxdcfaLKypk5QJC6Age9W354ldWd_pra05W8Kp5OFYEe5M1KQ0hCa_kzFgPXHgQzdj6a1We2k4e7ufskvBRWon4WtLclYHW9nf2QKQokLtxx0uhqYXxPoe00hn8NDVC079BFBgFPTpLGpxrF15cNPhEu6GfOzjWCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3207303375.mp4?token=NkmWgukWo6eKuaiIQiUtOM_m9gIQio0onNy37lpOewB5nHOUJXDJJkicfXf4vqLGMnG5XYDsa5OvJKy_QvLJLodT-ox5VI4UMhYrwgdqs5W-y-HnGkInSfKYawu--ukpHx6Yg-ZET0F0rXrxSXoeAWpXNbW7W0PP7lpFSFTo0OffoZ7KDzdeJqxdcfaLKypk5QJC6Age9W354ldWd_pra05W8Kp5OFYEe5M1KQ0hCa_kzFgPXHgQzdj6a1We2k4e7ufskvBRWon4WtLclYHW9nf2QKQokLtxx0uhqYXxPoe00hn8NDVC079BFBgFPTpLGpxrF15cNPhEu6GfOzjWCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاخ سفید درباره ایران: این فرض که ترامپ هرگز قراردادی را امضا کند که به هر نحوی با توافق فاجعه‌بار برجام که باراک حسین اوباما امضا کرد، قابل مقایسه باشد، مضحک است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/662555" target="_blank">📅 11:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662554">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72b824858.mp4?token=tcrEtVzCJvkdCPtQQGZpZu0Nw7D_89e8GI1wyZHJB9C39mOq1Tw36inSXXRW9SYQmkCbi_bwv_09lO7aH21eF6S5W1EQnmp_n_jpIeCqu1avheHhO_e5H2fdQWVT9piPBaTFjeGp3Qo43F4CKhtiZp0Fy_8XCurJvSoYuDCgTSgWL8ZCIE4bvBxYIk2mafUSj4EJJVNQ0ZxtbXdfhcvJy0vIw92HiRZ1HSYNYVB-DC7I3X7TAJlG8bUc_r80dgWrYozyNm045n_5QKXpGqI3j68rXNYe2ECzXuPgQt8o4IBGh84iujt2gnNJ24OCC5KsIWVw7lgHKQx98LbXyJrdoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72b824858.mp4?token=tcrEtVzCJvkdCPtQQGZpZu0Nw7D_89e8GI1wyZHJB9C39mOq1Tw36inSXXRW9SYQmkCbi_bwv_09lO7aH21eF6S5W1EQnmp_n_jpIeCqu1avheHhO_e5H2fdQWVT9piPBaTFjeGp3Qo43F4CKhtiZp0Fy_8XCurJvSoYuDCgTSgWL8ZCIE4bvBxYIk2mafUSj4EJJVNQ0ZxtbXdfhcvJy0vIw92HiRZ1HSYNYVB-DC7I3X7TAJlG8bUc_r80dgWrYozyNm045n_5QKXpGqI3j68rXNYe2ECzXuPgQt8o4IBGh84iujt2gnNJ24OCC5KsIWVw7lgHKQx98LbXyJrdoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی تکذیب کرد: نه دیداری با گروسی داشتیم و نه برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای آسیب‌دیده ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/662554" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662553">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcZnFRdbJs77H_ThyX9aWewehxcD2mXC1YSxyk7DFZyWsoS9tN0qoNu1_9OT1HdlzElcOOVw1aH-5GGMie6OSWe2TeQrN9HPnPkY6C27o0q38eCXilscmzURJDnG2FTF_knN_95RGWNp7Tk7LSqzQuy4osmEl_7mEGaemXmUB7J0I2oThcDDy2wekUCcp4ovvZclbkY7DDVeKIfIuSE6L9r2xaFcxaR6FNUoTSou95xyzLPyS-46Ny8KbmIi3v0VYmTpZI0FC92Uk4BYrjhRmY8-rMXU6YH7P8XaHNjW_9Mr6XGqbBBnVLjLShxFCyQODg0Y52UsaC4MjnTvIclh8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدافع مصر ضربه مغزی شد/ غایب بزرگ مقابل ایران
🔹
حسام عبدالمجید، مدافع میانی تیم ملی مصر که در دیدار مقابل نیوزیلند دچار آسیب‌دیدگی از ناحیه سر شد و طبق پروتکل پزشکی فیفا از زمین خارج شد، به‌دلیل ضربه مغزی حدود یک هفته دوران نقاهت دارد و به‌طور قطعی در دیدار برابر ایران غایب خواهد بود.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/662553" target="_blank">📅 11:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662550">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqe7ET5xnn-XFH9m6yi5xQX7_6imni4jcGoh7zmPNoKflTGVi9tKl_HOSR3rBCWX9nYRNzE5P08T-h1Sr4oe5UotWn5CxtYWp38VpGByqaxujsTCqbw-XvPl-_H95qO1ThYWS5s0OHi59G80gMIlfrzetE6uAAlvvInkxyBheHY-TAn20CAjcNJYb_1gH5vw_HuF_-Kt-ujKxT-3Q2umTnE6j145QYR_CjI1eybJsajRUlsMxxnAsCPMzF5DgvfWFTsuHHgpYoFMpcpYICuTmcI5pQIw6BXM9MWIt0kghVKk5PRlKgRCj_1lRjw87gx_2poG9UeXXQzusI4ASaoRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ob-RcHQoOWMtn1E2hMBec9MKiLrzYoHHWur2RwRIs31Vxe9xoAIJMw-LdFVs6YXx8WiAFTBfUOzbJGjuhmFjJ0eEzvGhJyQHoFdHp8BAYtE_IpM4wrJWVhtAEDchmnbefDBuGK5nOR_5aPUt5v06E39SsJ5uRFoiWTdE_VtPpXaV8jyDeSzF4VkRnr6fsd1fzDCYx0IWVMMO_l3V051IVlOfcrL_Nib8-aXjNpOcaM7cYDYWw22GFV4uxVj08oRDLuHkKCNlwSo3kZ30FnlOfa1y_Qswpy-895GrTH84sP7abta-rQcQ-RMz6ksyPNC8ogsO3wdv8lDypLIpRiC_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXBznDzr70clRnMRARUw_FpA8jqDln9vF0PfbsDaAwnuGTyOZAGsoR-vu-1_uqdRdiZM-IFhZG_ynD5x579X2fPYViZKNdv_wj-OoJ2C8VrtKCLrJ60td9kG-VsJ1gh4tGm0lrtkAh4DabzjF7Aet8VgphA4Z_Xkzgp8jo6MwuxMtBqhSQuGOffTzp8vqlWYtVCW1ZVrnAahNxbk9h8w0xhQsPsPqCRdhnTmn5XuN4k-VonpH_9vOAJcnShfomgtKz06_ypEDXx906z8k5sugIbrBx7AP-Wrs-0a96XP9uIs60NtLldjOBGEqJBTLfUhGXys72xSXD1lk_V6VWptNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بازی دیشب فرانسه - عراق؛ زیر بارش شدید باران
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/662550" target="_blank">📅 11:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662549">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
مسیرهای مراسم تشییع رهبر انقلاب مشابه مسیر راهپیمایی ۲۲ بهمن است
معاون فرهنگی شهرداری تهران:
🔹
مسیرهای مراسم نیز مشابه مسیر راهپیمایی ۲۲ بهمن خواهد بود.
🔹
بیشترین حجم تردد ورودی تهران از محورهای غربی و جنوبی است.
🔹
تهران دارای ۱۴ ورودی اصلی است که بیشترین حجم ورود از محورهای تهران ـ قم و تهران ـ کرج است.
🔹
در روز مراسم، برخی ایستگاه‌های اتوبوس فعال و برخی دیگر غیرفعال خواهند شد.
🔹
فاصله حرکت قطارهای مترو حدود ۱۰ دقیقه در نظر گرفته شده و خدمات‌رسانی ۲۴ ساعته انجام میشود.
🔹
از پنجشنبه هفته آینده تجهیزات اطلاع‌رسانی در بزرگراه‌های شهر تهران فعال می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/662549" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662548">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0158a349e0.mp4?token=iE6kHPCGZU6XmTWDEP7S-WfjWRl6UDzb7_IBxoQ1BPPedvfQQ6Au5mxpdQnoMkjwZu974uZoRx9R9aRVYpi3HzbOk3eQ-N3qItWH1zxqu8xiziWKLUPN3VVe61TEfSwNP8F_NFazPN2yff_Z2k0koZYCSU51lDTXacIjJo9c7cOvnpQgXDPK9iT_6AWhRZJzL6te9Fdbr7De-mJSSncEO9vRAh_iOtIF4ZRgpFlPO8ONErLsoOJNricsminFR4JIRO_bO4cAuRdzlUh2C4ukSBRB4q7LHwqUKnCEZay6JhQFnH4iGrCWVHVVY0_YomVOc2gGvClK7kwGE9NvMb2HDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0158a349e0.mp4?token=iE6kHPCGZU6XmTWDEP7S-WfjWRl6UDzb7_IBxoQ1BPPedvfQQ6Au5mxpdQnoMkjwZu974uZoRx9R9aRVYpi3HzbOk3eQ-N3qItWH1zxqu8xiziWKLUPN3VVe61TEfSwNP8F_NFazPN2yff_Z2k0koZYCSU51lDTXacIjJo9c7cOvnpQgXDPK9iT_6AWhRZJzL6te9Fdbr7De-mJSSncEO9vRAh_iOtIF4ZRgpFlPO8ONErLsoOJNricsminFR4JIRO_bO4cAuRdzlUh2C4ukSBRB4q7LHwqUKnCEZay6JhQFnH4iGrCWVHVVY0_YomVOc2gGvClK7kwGE9NvMb2HDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشگل‌ترین انرژی بار دنیا رو اینجوری میتونی درست کنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/662548" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662547">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd57389c4d.mp4?token=SWTITfuiWNvz1jkRmBvbp4r1wAvGBJO0ehV7zDXzf9cx1MUVNluU5ISsymyYRSPMNbtobvve3xHsBKyPE9liyNY4K9livFOGC2-8MKmUzAhmibw4TA8RP8vn0tqLaix6akNMvi8u4KwRfUb8iGcrJNhP1dxtIKhqqXWOrpULnfxJ-tYSBmwy9bX_3HjRxqGEVicYFMF19sKuhnuztQOBxqu-WjSgnW6WwFvrwjXMzqM8pzMU-dJhFCc815sEMG3xzQl4VBwFu2OE0eMFfPGdv_fmlgsMdQSzpzC6pfa-OxCxt-MWCnGwRRjbOmX9WeKQDlUIJ3aCKGXuRK-Mi1AbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd57389c4d.mp4?token=SWTITfuiWNvz1jkRmBvbp4r1wAvGBJO0ehV7zDXzf9cx1MUVNluU5ISsymyYRSPMNbtobvve3xHsBKyPE9liyNY4K9livFOGC2-8MKmUzAhmibw4TA8RP8vn0tqLaix6akNMvi8u4KwRfUb8iGcrJNhP1dxtIKhqqXWOrpULnfxJ-tYSBmwy9bX_3HjRxqGEVicYFMF19sKuhnuztQOBxqu-WjSgnW6WwFvrwjXMzqM8pzMU-dJhFCc815sEMG3xzQl4VBwFu2OE0eMFfPGdv_fmlgsMdQSzpzC6pfa-OxCxt-MWCnGwRRjbOmX9WeKQDlUIJ3aCKGXuRK-Mi1AbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار رییس اتحادیه نمایشگاه‌داران و فروشندگان خودرو: مراقب کلاهبرداران باشید و پول را فقط به حساب شرکت‌ها واریز کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/662547" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662546">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
رؤیابافی رادیو ارتش اسرائیل: تا نابودی کامل حزب‌الله در لبنان می‌مانیم
🔹
در حالیکه طبق تعهد آمریکا در تفاهمنامه، جنگ در تمامی جبهه‌ها می‌بایست پایان یابد، رادیو ارتش اشغالگر بار دیگر بر ادامه حضور در جنوب لبنان تأکید کرد.
🔹
به ادعای این رسانه، ارتش صهیونیستی تا منطقه الشقیف، در خاک لبنان باقی خواهد ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662546" target="_blank">📅 11:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662545">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgNUH8yboXBmP5ZSAzAc0kqrDcmII6M99L4jO5rLKOsApJpxP7f6Edu0dnnPEkg0ZC10Q3fa7F6ZoKDJR0CLCEFRhD931UI2bIDFajI_1LUZTtNrnJYnRm9-ZIfLXI3VwVBon3XfYE_w_nasZ1qVvVfaGf59o9Ogo19m4b4TdRf79pTtIFAb3-tocnGSP54KzoE_fdypmwiml5RZd9p4J__ncX44Rl3xIzPuiwys2kq_p4Nhyr2EJiXbJQmO-E5ycbFhz6I9b-ti8MnDTBwUd803d__s-bslWicOArTBiDWMFDaSujyGM-RhPUZxDt1k5u0MHyZBYGXpV-YGYZe4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امن‌ترین کشورهای جهان در سال ۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662545" target="_blank">📅 10:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662544">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروایت فتح</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b93cb9ff5.mp4?token=jvqL9IdapR3Al7P7POn6PgpHmVOl3GvziSDqIKrsbWznWCFxSZtcqTQSUFm1-KR43MAyz892uGbrkBdi-OSI-uKicyXnGG8sEWxjUiP5aG8Rh667f1AXGWkxh_LoQhc7ue5Y3WThy_z3tX3lQcni1sXmBfW33jbSOd8ccRluIkKRXp1l7L5Oe9J-pCbcxPNChMXINoRr6vus8ADBZvfXf-47EajHeX6R3VHD47F7_wsi8MbsDGN4la7jQdkqNxnwSHvIrYOwW1IvH8SH5izZ8N2GeQ49TYhKPe7bE_9OoUHUJhbDsNdQLQbE3LhAh3qpPqAxZXQNfFmb6zhlA_xouYepZ92dB46JhJ0UkE0j9bUAlssLjXTu0J3APx66OIp9mPRTH89QlSo01AFgqxMaXr6vhyYIod50nwnIHRYY31h7schNrAhSk-1tNIhUcNh_6R5B9fFd4-SAn9Cyh9e1bkeLi1FtfezalIQ1Cgbstnn_HqZzXSNpb-LtQekfGf6vhXzFxl1R2rKROlFvP4T192dHKrMgbPHb8OGKf2JPFlU8HsdwT_JNtYEvMyqs1Kaj8F460Hy2xqGdJUd-KP4L-yJnYG3bqBT9WwT600Vr0crJms9ywsUXWmw6vyJQp2dGlwYauv8Xllys1_uCnOkKGZfbhuOM0ZZe3hnonDHQ7do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b93cb9ff5.mp4?token=jvqL9IdapR3Al7P7POn6PgpHmVOl3GvziSDqIKrsbWznWCFxSZtcqTQSUFm1-KR43MAyz892uGbrkBdi-OSI-uKicyXnGG8sEWxjUiP5aG8Rh667f1AXGWkxh_LoQhc7ue5Y3WThy_z3tX3lQcni1sXmBfW33jbSOd8ccRluIkKRXp1l7L5Oe9J-pCbcxPNChMXINoRr6vus8ADBZvfXf-47EajHeX6R3VHD47F7_wsi8MbsDGN4la7jQdkqNxnwSHvIrYOwW1IvH8SH5izZ8N2GeQ49TYhKPe7bE_9OoUHUJhbDsNdQLQbE3LhAh3qpPqAxZXQNfFmb6zhlA_xouYepZ92dB46JhJ0UkE0j9bUAlssLjXTu0J3APx66OIp9mPRTH89QlSo01AFgqxMaXr6vhyYIod50nwnIHRYY31h7schNrAhSk-1tNIhUcNh_6R5B9fFd4-SAn9Cyh9e1bkeLi1FtfezalIQ1Cgbstnn_HqZzXSNpb-LtQekfGf6vhXzFxl1R2rKROlFvP4T192dHKrMgbPHb8OGKf2JPFlU8HsdwT_JNtYEvMyqs1Kaj8F460Hy2xqGdJUd-KP4L-yJnYG3bqBT9WwT600Vr0crJms9ywsUXWmw6vyJQp2dGlwYauv8Xllys1_uCnOkKGZfbhuOM0ZZe3hnonDHQ7do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آب ندارند، اما دست از کمک به دیگران نکشیده‌اند
روستای کنارجوی سیریک؛ جایی که مردمش با وجود محرومیت‌ها و کمبودها، از روزهای اول جنگ پای کار بودند.
#روایت_فتح
@revayatefath3</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/662544" target="_blank">📅 10:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662543">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889d4f5a02.mp4?token=ihH4miD11UCPQiN9ymUga9edm2a3bii9h_BcTEvcTHkjHDmv9Tr11f9QrEDxj9wQU7nUyWBg8Wrhk8tzLYGwEGF10F2lqoMb3jos64P0k3wEy3RVCFbla5IzDtGhkMdGp8FPNPqkpk238x5oHYMaVwBGLbcPdMzsm5e0vwWY0VuO6U3tD1ikxbkJ-NwcoBknPCOCXaSr6CjwyHXyYGwubanUkO3_AvBh0R-Lt1ZdF6poMa6ujAg5NUTFVoXkzvVvh4reOFmqTxCmF_eo4uvzGsY5qpbrb6J3qgjhUCi1UhkGNeF0y_bI8PUWsQ1TiX2WsT_HbmJrD3Qzm6j606QAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889d4f5a02.mp4?token=ihH4miD11UCPQiN9ymUga9edm2a3bii9h_BcTEvcTHkjHDmv9Tr11f9QrEDxj9wQU7nUyWBg8Wrhk8tzLYGwEGF10F2lqoMb3jos64P0k3wEy3RVCFbla5IzDtGhkMdGp8FPNPqkpk238x5oHYMaVwBGLbcPdMzsm5e0vwWY0VuO6U3tD1ikxbkJ-NwcoBknPCOCXaSr6CjwyHXyYGwubanUkO3_AvBh0R-Lt1ZdF6poMa6ujAg5NUTFVoXkzvVvh4reOFmqTxCmF_eo4uvzGsY5qpbrb6J3qgjhUCi1UhkGNeF0y_bI8PUWsQ1TiX2WsT_HbmJrD3Qzm6j606QAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو خودروی لکوس ‌ال‌ایکس ۵٧٠ با یک پلاک!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662543" target="_blank">📅 10:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662542">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
بنای دولت پیگیری حقوق ملت ایران و تقویت صلح و امنیت منطقه‌ای است
پزشکیان:
🔹
سفر به پاکستان با هدف قدردانی از تلاش‌هایی انجام می‌شود که دولت این کشور برای نهایی شدن تفاهم‌نامه انجام داده است.
🔹
ما به دنبال اجرای کامل بندهایی هستیم که در چارچوب قوانین بین‌المللی و حقوق ملت ایران به امضا رسیده و در صورت تحقق این مهم، بسیاری از مشکلات منطقه کاهش یافته و دست متجاوزان و تجاوزکاران کوتاه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662542" target="_blank">📅 10:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662541">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان راهی پاکستان شد.
🔹
دانیال نوریان از پرسنل مرزبانی شهرستان مریوان در حین ماموریت به درجه رفیع شهادت نائل آمد.
🔹
سازمان ملل: برای نخستین بار از مارس هیچ حمله هوایی در لبنان ثبت نشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662541" target="_blank">📅 10:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662540">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfFIRcuB3qmVZ1u8wHNBaCZ2wLCvyWMgtU3qAXlIUAsTF_EMOoorWPfPKbVafUJhVv2grL6Dx3prseb4dI3Vy-hqumzaXXZj5KtEe3-2Du5zGnLyfvVnENkc7wDKN5j2JGn-CPhuFUU2vCu2pSFNdBHtEelXit40tQsyExhRRL7im89mFALw1eLt2KDprwwmaZyb4JGBHVcZXxwuWAl1hyiab8C3rPEPkm1AjfidQrZfbkrGnB1IBzfHdxQSwhIgHRkPfVzpoz86Xwt00Ze1n1hdwYifL-Inlrn6goPfb6dzMNo22GqlgSs_bMugMtyGZG_HkT7odGyDxGYP05W9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ نکته عجیب درباره ارث که همه باید بدانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662540" target="_blank">📅 10:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662535">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rW9LnK5YTcZQhIM67gWbMufNRqBlFyu7PB0P3ymUG6uswoUo3X6jD46xncTt9yaq6078a4WwWcab709NxvrjI69QSmqNz7raY95XyRPuGdZq42357eWlnpHyNz5rHEov6CL0a6QzdbnoOyF_6N2eUPdouCXeCkoXXhnzZJ5KfZHnSrPXhyhvm_zbP72yzRU4QpqAanUb7R0o5WgRQMBFqmSAZuFa_z8kP568ZoemnIBRC0t1_hj_BLUaVlBR5OEmfWrqli881zdsT9EM5J_-p810c4us0Giedy9pda-4V8A8suLl2mfpGy7MwYnyl-yHlj-jxJQIerQEGnm7nWKPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJGPj7pkczBBanFx9xU5BcndyFf8OufQ_058cOnE2MMvHWzxUBFAN788cBPAHRfBKdisBGaIH3GiJvLNZNfyDbV7wJYDpH22EqQSi9tJtvG75S_Vh2bc1FoB0ATqytOpoKzYL2HZFhJLs9uxwQq6pcQ5fSZgzRcJhqPa1Z0DUMaE_25WZwcIrQwDMnCBM6tHST64KxbbkpZ9XmVOoxpWRsue5QhIvkNylnf7fqO3xHDh8FqAyS4IP1jmlbXaTFm9bAGYOojmCwG9lnY-7LnbKZhtX-qc_oghoD_h8z1d4aTVUeuJGHUR25KxWqXYYjLm6NJ6OvxvUnqEGe62pryGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pp8FG3tlhE251Ds9KPKbwEIwGMKngbbR4_jiq_49B38SB4MpMk8N7aroGNuoHQem4Gqf3HOiwhKA9YNhW176T_9Pe5dQvEQ6MBTpXpyzn1Lw_PncMjOEnrBTcq0bhLIxfak9vQg1X3fpNKXeIePgVHl8sLLyFDgxna3bDc-fMioxA3QszeaVHGeGZjVkWolwS-z1N7QCtpDBFfscbcAfXpyfKQc3sLVpGcHlg9BrjWuK96_RxDNbddpmQFfgSNWo4RmVUdKRwB1gd9m-SKr6WnnF1AHGNXJqxowWSC8YU20To4ktRJ1VKbGajCPt3JF21xHg-4clzRzKCbOsXqt23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VT6ydpfFx9sirotNS4tuGBiaTxgU-sYJbbZtaT3eEUQEyQnqD3JxBy41d0TOc8Cli-y20MURKQ14BrDWtotqnhgTLL-gWBjE8yMxbWAks09qqCPAkWjWPEdc_u-6uS-0mZMYV3FYsUKoYwwaBNecHX84YfcxdtAqcqFb3sKNhKRRafOzAzms83F_5ijGLvCl4OHR6fqRBv8hAsY9rQSHz3eZBps4CTnfCcxhazhDzgw6eLSZlpvJSKIUfO7Wz1dw2Uv4WWOvA9DcurB3yJdQQwzkq_FdmHjjFHLPXVZmnsCED2U7xsPH0YL7Ll-fR0T8jFNQydJpgo3_dsvyR1eJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lX-A4JYi_lU7CdJdRfNswMZixbHz6QvxVKxqB8D2nYoAVFIv4a4HlTBQgJvOVSt2kHhrABQm5pEufE30V8qh3fGLJ4h_w-763KbdSftY1t7tPzCt9LWDlgfnEdd2jy98aieJw6mQ5m0mrTheHcI3VEgVP26QYSwgox3IoHJBVQTzskrmPHPDzSppl6mrpBPan_Fz8X5TiAmGF1fAAcQr7M68QIbuTVdnn7eTzrP1rcbNcCdW7ANeEG4Ym-lUGApsMzykdLVpPM-mNNUsKPhgraqR53dzkKc80jyXB9Kczw7J5TKq_GPAtw2NqT8GLj2Qr0aei6MPYUvzXJ-ZrlDwFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ازسرگیری واردات خودرو از عمان - جزیره قشم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662535" target="_blank">📅 10:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oY17U3i53UQBXLnnCO2GD7xmSW7CE8K-CnM3qCTAkRdKZV4yXoUdg5TUgQmYMiFId7kgZE2-_cByrqMCW_zgEWMpnMRYoq9K0gc5JUvhufJg6YwrsdtHfrx3CwTOFgO07tKl1mNA8GXnSCc4HKBU_qjF7GGYNNqMRysorWCNbPoMpQWZvVxiSTJgWod6Iuo18EJCgxV8kWxarTUf6YNe4tUdgeEHM91T_AD07nGzdLhVvX9hc3vmss4ELe6ELiH5_VCEm76ACm52XhS_GJboUgDrYYQ-hh1XMuSSGe5pfZvqTNwl-cnkp5hV31NE5jpEFpv4dqUTZ94SgjqeYQRNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbgIOooX1o7QK1vb_GFY9p5iZmUdmCdpFNIo2IhXh99Kfob_EwKHs1Zrm-DK_d5s2SPW4OEhSSg8rK-UcQ_ytYe4EQ0bn0i-QNfXpq43YDfo2MO7gxXM9LVdS_hYaI30Pz-ikTFlyn2goG3LQ2ZKo2n_r8bw3L2WcNcVO4JM0VyxSCEg13bb1YgfgLgvVBea6LwRxEusgKYYu3fw4iifh48nkZPD3UaQ13qrwcWlfeQ23DeL_QTeH08BSbDKTUQ9sFm_bZLVvWbaBm4cePJi6UcxLYSnARRHhY7RnGetfMLV5PV7Ersu3Ii7E4VSh9urtDdNFOAmypOEn-XFnpqq2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اطلاعیهٔ جدید آموزش‌وپرورش: برنامهٔ برگزاری امتحانات نهایی بدون هیچ‌گونه تغییر اجرا می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662532" target="_blank">📅 10:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
الجزیره: بند مربوط به لبنان در تفاهمات جدید ایران و آمریکا باعث نگرانی اسرائیل شده و گفته می‌شود نتانیاهو را سردرگم کرده است
🔹
مقامات رژیم صهیونیستی با وجود این نگرانی‌ها تأکید کردند که حضور نظامی خود را در جنوب لبنان حفظ خواهند کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662531" target="_blank">📅 10:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068235bd6e.mp4?token=tECC3eBY5p4w50P2XQFPkUUQQPKkp8Jy7hSUkdk12XG0ZkKQNnBn2KfTcSC7luGbUQEhzIbismKhmkIG8CE9KFae665Jic76d_kfNO7RlssmiSkRkJFIukKGYG4B0W5Yr2ATltF4FTnbgzYp-oSJb8ijftXOwFTGMWl4M6NUjvHidaHfqOIHzh564gwhx8-vuFnju-SWr82JSKOFOtPH6cPWsN0Of6ud3jt1ytAJ00wIPkZpBnI0X-PyUmYmS2WkGxBm7M_C48KfYbvSscyL6WJYR-FYRVq-utcTIxtJFmDSTkHjaT3zOKrEzipmttoM0hYlDFCgLYkrcB98nS6sUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068235bd6e.mp4?token=tECC3eBY5p4w50P2XQFPkUUQQPKkp8Jy7hSUkdk12XG0ZkKQNnBn2KfTcSC7luGbUQEhzIbismKhmkIG8CE9KFae665Jic76d_kfNO7RlssmiSkRkJFIukKGYG4B0W5Yr2ATltF4FTnbgzYp-oSJb8ijftXOwFTGMWl4M6NUjvHidaHfqOIHzh564gwhx8-vuFnju-SWr82JSKOFOtPH6cPWsN0Of6ud3jt1ytAJ00wIPkZpBnI0X-PyUmYmS2WkGxBm7M_C48KfYbvSscyL6WJYR-FYRVq-utcTIxtJFmDSTkHjaT3zOKrEzipmttoM0hYlDFCgLYkrcB98nS6sUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین تیم ملی فوتبال ایران یک روز پس از بازگشت از لس آنجلس
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662530" target="_blank">📅 10:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQnVFfRJpaAYmlDRqx6nEeuSUbOAjzc19fzJ2hdAa4jR54jwcW-EjJBgp2n6WYovWrLEaXRwB8WCRkWzXOaebiXuJ_lVIPEd0PNsns2G_6M0nFj_-lkhQHWhTb57pHOS_Xgxeq4CJhDO63GLKMhSvq-OfGLPi0hoBXUPBGrcI6gXz2ndml0lMxbxpIH3TQ17ICAPkbJFvF9S4ty5MwiiTXq131-6mbkcbZJrhzPO4lq3McL0HPOLtQgI3-aEQpQV816MMKqlNFtJ48vbz5h2XLC9Ipr52wrJ7fE0IJhuyZORkXB4EF-njfIPCx3smvixk9dbUTRpv__P8jgu7PHVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
دکتر فتحعلی در مراسم روز ملی اصناف مطرح کرد:
🔰
بانک مهر ایران در مسیر تبدیل شدن به بانک عامل اصناف کشور
🔸
با حضور دکتر «مسعود پزشکیان» رئیس‌جمهور، دکتر «سید محمد اتابک» وزیر صنعت، معدن و تجارت، دکتر «امین‌حسین رحیمی» وزیر دادگستری، رئیس اتاق اصناف ایران، رئیس اتاق بازرگانی، جمعی از نمایندگان مجلس و مدیران دولتی و دکتر «غلامرضا فتحعلی» مدیرعامل بانک قرض‌الحسنه مهر ایران، آیین گرامیداشت روز ملی اصناف در سالن اجلاس سران برگزار شد.
🔸
مدیرعامل بانک قرض‌الحسنه مهر ایران در این مراسم، گفت: این بانک با خدمات خود در تلاش است به بانک عامل اصناف کشور تبدیل شود.
🔸
فتحعلی با بیان اینکه پایین بودن نرخ تمام شده پول مهم‌ترین مزیت بانک است، گفت: در حال حاضر بیش از یک میلیون و ۳۰۰ هزار صنف، مشتری بانک هستند؛ همچنین یک میلیون دستگاه کارتخوان بانک در این حوزه فعال است.
🔸
وی افزود: بانک مهر ایران علاوه بر خدمات بانکی، در حوزه پرداخت‌های ارزی، صدور ضمانت‌نامه، صدور کارت رفاهی متصل به اوراق گام و همچنین فروش کالا و خدمت در بازارگاه کیومارت می‌تواند در کنار اصناف سراسر کشور باشد.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662529" target="_blank">📅 10:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb45e6f68.mp4?token=a72RS8Muao4XBkt8VWVY18nuuivErGmPJEa5ujrtmH5bEXg8UsKdyWMm3ONe36OWSVwkd8mt23yTxZ7OfX6ZL3q3PI8QCB77xHlT2zPzAKWB_VwQpXAwk-9Alxc1-IJR_uEc4KpQaT0NynzMhGruvRuX7jUzgyJ_doI-Tq0JaWqwEzojsnXewHl1-jOWAQsDCTxSypkxw2sEcJtnaNxNuxVyGxnx9g0Zx-kyZaQ7-lxragb8JR-jDG_0cL8-vQ0emyHvwbm2uFcbQrCkXGmFS5YQYL4VkD-9IN7UOEY-peR9ubn3r5vmlBz_Etpwpy7R59npYmh5nOXFAVH2oztegw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb45e6f68.mp4?token=a72RS8Muao4XBkt8VWVY18nuuivErGmPJEa5ujrtmH5bEXg8UsKdyWMm3ONe36OWSVwkd8mt23yTxZ7OfX6ZL3q3PI8QCB77xHlT2zPzAKWB_VwQpXAwk-9Alxc1-IJR_uEc4KpQaT0NynzMhGruvRuX7jUzgyJ_doI-Tq0JaWqwEzojsnXewHl1-jOWAQsDCTxSypkxw2sEcJtnaNxNuxVyGxnx9g0Zx-kyZaQ7-lxragb8JR-jDG_0cL8-vQ0emyHvwbm2uFcbQrCkXGmFS5YQYL4VkD-9IN7UOEY-peR9ubn3r5vmlBz_Etpwpy7R59npYmh5nOXFAVH2oztegw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض کمدین آمریکایی به ویزای یک روزه بازیکنان ایران: این چه وضع برگزاری جام جهانی در آمریکا است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/662528" target="_blank">📅 10:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662526">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7795093980.mp4?token=A2iBmGZQDFpiU1TzF_vsw6TLfQTCj9iPAGnTY4Xjh5ANNqiKgVQPtgiiAbDEDPZUGtqK9Ud6pnX5bGMlsGWmPbH-rhc13tkBm7-0e8aPpYRuW4rHYY6BC-IKWgOZAcS-K3rkHxv-EdkyK5rJrx23rFN27l_N4lk76-51qXoQ6mTj9OzvKDxZ93AeivDpJ9_7hCbQKXkoLucpQIDcmN1kpuiX7uXELMpm6X70DTGCxGT9VzvcViJhW7EGMA3PRAUcY7War-BNMzkUsTySl5F_6HsULOFWOT_oQFhh3kSDeUr0Ycz8uRKDk-KOcz2JK_CRNp8XbhhaRpWiyho_efeKjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7795093980.mp4?token=A2iBmGZQDFpiU1TzF_vsw6TLfQTCj9iPAGnTY4Xjh5ANNqiKgVQPtgiiAbDEDPZUGtqK9Ud6pnX5bGMlsGWmPbH-rhc13tkBm7-0e8aPpYRuW4rHYY6BC-IKWgOZAcS-K3rkHxv-EdkyK5rJrx23rFN27l_N4lk76-51qXoQ6mTj9OzvKDxZ93AeivDpJ9_7hCbQKXkoLucpQIDcmN1kpuiX7uXELMpm6X70DTGCxGT9VzvcViJhW7EGMA3PRAUcY7War-BNMzkUsTySl5F_6HsULOFWOT_oQFhh3kSDeUr0Ycz8uRKDk-KOcz2JK_CRNp8XbhhaRpWiyho_efeKjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقدام عجیب راننده پراید برای فروش ماشین که باعث چپ شدن ماشین شد !
🔹
راننده قصد داشت برای معرفی ماشین، یه دستی بکشه و از خودرو پیاده بشه تا فیلم جذاب‌تری برای آگهی فروش بگیره؛ اما این حرکت نمایشی آن‌طور که انتظار داشت پیش نرفت و در نهایت خودرو چپ کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662526" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662524">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
معاون وزیر صمت در واکنش به افزایش قیمت خودرو:خودروسازان به حرف ما گوش کرده و قیمت را عادلانه می کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/662524" target="_blank">📅 10:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662523">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4p6UIkhcqfohnwo65NPK_QcXGfoU_XStoWCudRRWbxGfTbp2ZqaTg-KDGFHSPs2RtkPac5sGecYsLpxsOpShho_A4ktozJ5KZxwoeh-8nJpEZ4cIZIC_b5QZdbJmV8bQxITwTLHRo-Ui5KGd3I3hsEyOr5hQhe_KhsOHuOS7IHy9R4JOBplCQ7RysKLAIwWApTdCpZFuAubvOZGE2jmy4AoPEM27t2_ErFWTS8YKhNArDXAuy9llsGyLEFfTQt1F4maxuvBSRp-RUUzx2wsDVUHz2GutU5QaDwTVtdICbiHNvOZJveRN5XALVr6Uc51y5uvQlPmjkVbxxba7BHA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت یک کاربر بلژیکی: ما نتوانستیم ایران را شکست دهیم اما حداقل 300 میلیارد دلار هزینه نکردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/662523" target="_blank">📅 10:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662522">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_EnzKVd4H_4NL6LKyOMuRjmcrH4UgA8mlqXbCrNaKjnxJWRh7lNIaXWxi3K3G2RdzsANSsd8VT4KjK4c41eL8qvlniU_0lZBwsaxrLzPaFEa1Cl8yr1YFmePubNMeAooChM6daKwO06zjV4O7hL72xbivZsK2XKfLLBWTH_5VFzEXglphPWhnk62TbvGZsRf9H-Q5oWznIFIUDmoBiZS3WQH20CinMmUWwJrgdNcaOUr-Gdhb-Q3jyG4-zOrY6HzY7K_33KEermU7l_G6EkLoS1fic43KgLAGo3dhyp2k85onvuey45rDEhXlxmIomWDrTGytKlCqj0q8sgnVp7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه مسابقات روز سیزدهم دور گروهی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662522" target="_blank">📅 10:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662512">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0R6WAMKUV-a1Hkd6He_5P6lf4quEF8Rzccxc20iTCWPZFeXr6B3qpjqj_diyLNgdDt6z4P3eVUh7fTjCbCcZJ4E_bcrmhjprQK_emO5LV45QpqEBMv5puOgPpLr_3xQ2RUeO1d-D8Pmg0KTdpuKjRcVs_9xEOKA5YpNftPtKk86872u_zC5HZ4XYCEg2cM7yeebG6U_VY1xgcNcMgyw-XfElhvYAlLmhYbYF8w43q_ZCWhUFcJvJA_MIfXarWiMr_N54KNrztEEoql4myW3TaOTJOHA_6J_ba5daHCRgtWbYgD77wwMw_JGyq65W5jv-wuwjd1qpvpQtwuCGIBvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyZKvsN_9REeEodfWNwltz9nFz3C6PW76kXm0JeDAAewZ7eosXDKRG3j1IJlk972gK9jCBJhoOw5m36wn2AlPcI2ELUfeYXXH-di43MyTzQZ3ZnxvuJ1QRyesOgNCVtQP_bosKFW2Olag_MjZ1vl8HHmI_JvzW9EajrWW8GaKnXQuJuij45xRe-GWYETiWAjb8-X-PIlUSLucxQQrHXj_dah_AwE7EPg3FwNnsK4gyQUOmkZ3QWB5kabPN2qzsKrFWfQxixWbmYffLMLnddQauGd2M0JCnIC0byX8QzGX9YY1cuF6EBQ7M7rwo-0Ro_Ow7ZLuft91dt_kRCv-svdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj2r3crgQx8tL6HldWcEthR13RGSps62WOYF31F88OanrMGI-SVWVj1StamuLInAKtYl-RYThruEpreLfi5x-WrGJT4Tz-OiX7rtw9iJ2Yr2gfdVRwcFZqcqGUwO0m7nHXgSLAlrNyM2pafDsbwSqhxdAbmafvH8Pws4fuUpTYjFjHlCNQEiLIlmosGsmxSmId9vowDrussKiBdrCXOMXv1kv3ADisomU1smg7cGJEMm4acze4p_fSIC1w63ppwY_mxssOzSL11AaJOQPBJ_lSGVzq5jkK6kxrFgcN44qAzfX4olcRQc_J6Ew9r8r45BDnXPCRFrFQtSUCp8ekJ1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK4uRJsMUc6SgECySv8QBBi7UaUhjhqFBuuI6H-a3EobVM8NPlTdqwohwu8-lbJJJHdACaAlnjpCf8UD0rLAW4esFWdS-bN6DE1AbUZ8f-A7MeuQ9jzlVNPl0tEXEWTbydWVjOxYqvHGkt4y5CKHLvfBCGMcDyALAMJ9jflztJRpIYVJxv38P-YGLrGMmkLCiYhau2A4UtPUIceA8G8H9n2wPZa_BdmZaFMn4aTQPvr6kROc9faE_bFwCCPh-tg7UNEmQi-Zd0yTWOqVFW9LAepKyzrtNzcwzDuIAyocZb8D8w0aUqu_FB1TjAhWycRNc8mL38GpE79XwgC9W2ORrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4tj-JuGjgQ_3VmIXourwfAspncqdo31_knMkdtc9p9nGhLqqymUvQA8fx4B77Szh6pI9xl_RB9P2iarmSMiy3AJ5fyhuJnHBsoBb8RZ3CYLGpLgiBIiu31OEjuicwWNaugHePpXIhQrFccjVeZPm7YWFwHpm-Pf7wRRbDd4DAScr5qewm-_pGlYQM-pY3-U2ezVlO3jQJ4wsvtRO8VhjjwRKGFwWGWnEPlSSePWGrQto0l5qNWjFx1_fMOxmAyNbXK9MLap3Fc_xSnKID1QGJQ7XV9gnNF8CCScR9IvGUui1lgArsHi02BSFF-4MOf9VGYWAXgYGf-EStp9QILQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKhUqyobHpnRKPuNFYXv1sn9ElcT2e-xAlsRNIwmAQ-aPsVB1e4kiSz2lSdE5l3fJ24r5iq_eJ-HjSUEKu1WhgDbHWyJVpBajlSg-7WDqzxhjMfw8TS52bkPMR9UjGiHZ-ZMZA-D-11h7jdIR4PNvZCHfa--8yQXxkwh6EtkYkJo08tGbTqlcJh8ULo-L6F3pb0rJSiQFieERtlvPXON0xK-vbRRrtTLF_bc7pU34Mta9oUBMW5l1E4dbiUcz5MGjSvxjBQAYA83ABHzxQUHcGVqRl7--xHrFIw5vKQ766RasPIEk8_Vubn9wEQiV7LsikLTUIqlWome3MSyA5huAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvjB4jJkdEZX8Mzi7fuBsGT91n-BlOZMUgSvRdV15qe0YPrBZYoWrPCcUIuLDYy84hKwRF_iLhRQVF9cICPQ9HUsCHLNZaLRV0X9tIZcs0fCPAE3_dwR6w9OlkmSZdqaBG9jGfXpeQZ4k6PEfjSNnpYANdAmTTeIg-3di1x2Aieoc6rLTGzs5s3oikitk1w8UvdUdw3GB5mXLfEZ2kvuE2IZgI3uuPgXqLuNf828CnS0zEm5ww_aCAVofS-TmtKq1wBCWLHIIvO31rDP_gyXLaEYt_hzRo4ZkzH0bv4LLji-PMGzBr_uswmMQPH229bi2plzPq-kUheLTamUqF1M4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRxlY6nbaY79HIx-FGGWM1HapFwIveCzaJzb1LCeS8svI9xrwdGRfPSVd7QnOBST0WFtZw4DBWM89ERloFt3kBOBCsUbAZkyVrZOCTsEyPJxfFcF-8WoxCOmd7_JPhPDZegRdQnrKliTupz3X24xSIYIv5oBaMMsPps748Nn7kuYRhUiRLeV28gMXuayesTsqbam1ngaumwCiA-v2fhIMACFm82XXopoUKGmhrlAfUXPAwItr78OkJxpqx2dZ4At1zQaXdwgut5DDS5YFtott6Y1vdp-MBrUImCAOix2mgNA1zb8gZsF3AUizOxbLQjmm37C7sI1hdICt-7ZaY9Uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8LKiSgA5Qm9emS_n4BsyBnTvOC6AQsHpzRZcktcmcw1RKxnLpfOYaJqcL03TuBI7i7XhPKKZx4sKVTsWhTa_XLvrGt4Z683fin9dFaXVe0G9YIlNyuYLNrcvfxAjDuinuHZDcm2WREB7wkQBNmB7_hs1wnsg0qTz1riVnUOOSMCJzr378KTZes1DjffXET9N-OM1FmLEKQG5E8d2dFJR0qUzBkvVlD1zJtNaHMTn1S7DlpibmF_BN944A7HOIwx81-NbjjYlrM2aK0A8HTQtv_6LXyeAIBfKwQs0bZ9VsaRNIZhltAROn5d9_GP2htoFH5bRZ3XpxAwLnztdhrsBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ نشانه که میگه سلامت‌ روان شما در حال فرسوده شدنه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/662512" target="_blank">📅 10:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662511">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش: امتحانات نهایی پایه یازدهم از ۲۰ تیر ۱۴۰۵ و پایه دوازدهم از ۲۱ تیر ۱۴۰۵ طبق برنامه اعلام‌شده برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662511" target="_blank">📅 09:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662510">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3727fe8.mp4?token=idLJ1JNn1h8eJQkKj25o22weD5oOKZIah5HFrVCrbOPCesYbZHkXR6LdtM2KH725-oBoEx1d4T-sRBGdVX6usknyeDVfpuLYqciu1MQ98pH0PU2Du28lVDoCoSodciqhqxxJkiTRsdNlG9_uMTYy0G-gc1s37fQe2aJi9iyMBLkpXL-VFuVXSFBnzm6LwIOPTUVWMnu4rzz586ptNH29weV0E3JqF0Z52y2nZOtKje82Mbwq-j5BeUWY7RN2LXwhavyF8du6W5e8XnaqDkaMhvE32YdODROAEIgRi-Tp0vNCGXdqnvD5TxzquYoLJUsAUOt-OMoAJ50BcZhgZ45Csg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3727fe8.mp4?token=idLJ1JNn1h8eJQkKj25o22weD5oOKZIah5HFrVCrbOPCesYbZHkXR6LdtM2KH725-oBoEx1d4T-sRBGdVX6usknyeDVfpuLYqciu1MQ98pH0PU2Du28lVDoCoSodciqhqxxJkiTRsdNlG9_uMTYy0G-gc1s37fQe2aJi9iyMBLkpXL-VFuVXSFBnzm6LwIOPTUVWMnu4rzz586ptNH29weV0E3JqF0Z52y2nZOtKje82Mbwq-j5BeUWY7RN2LXwhavyF8du6W5e8XnaqDkaMhvE32YdODROAEIgRi-Tp0vNCGXdqnvD5TxzquYoLJUsAUOt-OMoAJ50BcZhgZ45Csg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی منتشرشده توسط ناسا پرواز کاوشگر این آژانس فضایی را در کنار قمر سیاره نپتون به نمایش می‌گذارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662510" target="_blank">📅 09:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662509">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
پزشکیان:اثربخشی مذاکرات به پایبندی کامل به تعهدات مورد توافق بستگی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662509" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662508">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051b7d322c.mp4?token=QGYLUFmjte_sixQ0SeZ4OT02EQOdzDZIxq2ummtTL1kTE1wCTn_u8PQK8JZIszXDtWqkaFeMgX6fzrwxNRiy1car63yFspxk9OZEe0cjoZSN48TmJWgYMLASebjwN4KVtcMGP5r3DOQTPgZHO5rcZQL-Fh76rgktzfIcRTec_X_G88Bv_sqnXXEoiaxO1SSJEJOHdMTAGMsJZU8aMWf3p9ZPEo7Zrgy0jlSGbuSphiNufhNbeLiigWIUO-wI2ZUThBIjcYUDA_wwcB-fBmZ_xf3CJZgP0iu3RWxYp5iafqDzQ302XxbTX4RuLhBD0O5oGPEkAYWEu4q7HT7geI8MkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051b7d322c.mp4?token=QGYLUFmjte_sixQ0SeZ4OT02EQOdzDZIxq2ummtTL1kTE1wCTn_u8PQK8JZIszXDtWqkaFeMgX6fzrwxNRiy1car63yFspxk9OZEe0cjoZSN48TmJWgYMLASebjwN4KVtcMGP5r3DOQTPgZHO5rcZQL-Fh76rgktzfIcRTec_X_G88Bv_sqnXXEoiaxO1SSJEJOHdMTAGMsJZU8aMWf3p9ZPEo7Zrgy0jlSGbuSphiNufhNbeLiigWIUO-wI2ZUThBIjcYUDA_wwcB-fBmZ_xf3CJZgP0iu3RWxYp5iafqDzQ302XxbTX4RuLhBD0O5oGPEkAYWEu4q7HT7geI8MkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امانی سفیر سابق ایران در لبنان: رژیم صهیونیستی در جنگ ایران و لبنان و غزه برای استفاده از بمب‌های خاص با موافقت آمریکا بمباران و جنایت می کند
🔹
آمریکایی‌ها به دلیل فشار ترامپ می‌خواهند توافق را به هر قیمتی اجرا کنند، هرچند در چارچوب شرایط خودشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662508" target="_blank">📅 09:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662507">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c3b2ec0.mp4?token=WfR8r_4MFIHvZS0U52Gs7iOvm_tlSCh72omYDN1SVXydbAFWOwbbpTCgq52bMy1t1Ddq3UXbpqNv5tqUY4K_ZiDI_JrP8iWGtSyys5tZiS901mRbckU-ht96w6aBgjyogUfa6sxTKzDiSPuKq4HogfcHjhrzkHmFIBhYIABSslVFcOY_HqPS9vUQYLaelr4eZARlm22Wxg1IKKsi56Ao1jrVBLNquRKHrThBHFLJpPe1jy_hXpPDsc84qAPFh1KxaNB83r5zIp-zxsdoTY6QUN3-dm2re6NSs6AFe_IeXlBssa0lZTP6xWy6VT_k26_SJluPL7JEC82p2YOboZ8mmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c3b2ec0.mp4?token=WfR8r_4MFIHvZS0U52Gs7iOvm_tlSCh72omYDN1SVXydbAFWOwbbpTCgq52bMy1t1Ddq3UXbpqNv5tqUY4K_ZiDI_JrP8iWGtSyys5tZiS901mRbckU-ht96w6aBgjyogUfa6sxTKzDiSPuKq4HogfcHjhrzkHmFIBhYIABSslVFcOY_HqPS9vUQYLaelr4eZARlm22Wxg1IKKsi56Ao1jrVBLNquRKHrThBHFLJpPe1jy_hXpPDsc84qAPFh1KxaNB83r5zIp-zxsdoTY6QUN3-dm2re6NSs6AFe_IeXlBssa0lZTP6xWy6VT_k26_SJluPL7JEC82p2YOboZ8mmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار قالیباف و هیئت همراه با سلطان عمان/ تنگه هرمز؛ محور گفتگوها
🔹
کمیته‌های تخصصی در سوئیس به ریاست غریب‌آبادی درباره چگونگی اجرای یادداشت تفاهم در حال رایزنی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662507" target="_blank">📅 09:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662506">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjQs48vkfRMjieU115NVwE_VrC7TOam8bHQ4j96aZEa0Viq9IATn0B9F__I9mXtH8VxaDJzPd4FoRqTCFObBtBsL6rR5VOhXeixIHGO5b7e0yoWTYz9MGfn-_skituT-ASRyzQTzLxdCvHgOvADkEZ9kT_Gh2UnwmGFpG0MtZgfBZRsKXerWctGPJwJ15zAn63nX9hcs7I29MVWBFonc8_H8tKFHNkQVz-VXn3XDnWPtVa2MKvwQHortnvZzTTKct4Az_4kzkAm8wXyUAI5qLVFt2JXOKqz-sU05Nca3xPDu74ZyLToDOkOWIPN7dya92uRY_HlzNH3aof_W_VjDGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ اعلام کرد خودروسازان آمریکایی کارخانه‌های خود را برای تولید سلاح‌هایی مثل پاتریوت و تاماهاک تغییر کاربری می‌دهند
🔹
این تصمیم در پی گزارش‌هایی گرفته شده که می‌گوید درگیری با ایران، حدود نیمی از ذخایر پاتریوت و ۳۰٪ تاماهاک آمریکا را تمام کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662506" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662505">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دوم،قسمت چهارم</div>
  <div class="tg-doc-extra">بزرگمهر بختگان</div>
</div>
<a href="https://t.me/akhbarefori/662505" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
♦️
کریم‌خان زند (وکیلِ مردم)
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «برندینگ معکوس»، «مدیریتِ ریسکِ آینده» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/662505" target="_blank">📅 09:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662504">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194817b2c6.mp4?token=ErrVCnxLGvUlo62Huk1bDZdzZW0RVIGUNXFsKptr_UpJoqimHRYZwqhTrT15I_pWIXie1Fy3ksds4aFIwopU-DCGx-x0sWzLjgHXICvgRGrm3Wp19OdZ1XN7QUbEKkvcxrYdK6e7tSL5w6NugbofMFDru3cfpmsjkWuDVXtFCeC6_cSXNPduTaLuIDAQQeBD03Am5DEnGFYOGbiLqbW4pTcfj9tTKm4HwTBU4Fgnnf75Jj42JNSNlnYojQWXs2ggwJmQjy-5DRXnOf73H-JsU2CY9udT0fe5hGvqftPO6gL0Mn9u-v2nCXLeZ1SAYmwINe9fBZYkNVFOPBJjbQPR3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194817b2c6.mp4?token=ErrVCnxLGvUlo62Huk1bDZdzZW0RVIGUNXFsKptr_UpJoqimHRYZwqhTrT15I_pWIXie1Fy3ksds4aFIwopU-DCGx-x0sWzLjgHXICvgRGrm3Wp19OdZ1XN7QUbEKkvcxrYdK6e7tSL5w6NugbofMFDru3cfpmsjkWuDVXtFCeC6_cSXNPduTaLuIDAQQeBD03Am5DEnGFYOGbiLqbW4pTcfj9tTKm4HwTBU4Fgnnf75Jj42JNSNlnYojQWXs2ggwJmQjy-5DRXnOf73H-JsU2CY9udT0fe5hGvqftPO6gL0Mn9u-v2nCXLeZ1SAYmwINe9fBZYkNVFOPBJjbQPR3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریم‌خان زند و برندسازیِ معکوس
#پادکست_کافئین
| فصل‌دو،قسمت‌چهار
☕️
🔹
رهبری که در عصرِ اشباعِ ادعاها و دیکتاتورهایِ خون‌ریز، تاجِ شاهی را کنار گذاشت، روی فرشِ کهنه نشست و نامِ خودش را گذاشت «وکیلِ مردم».
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
🔹
از اینجا ببینید و بشنوید
👇
https://youtu.be/8Hfg6_MHS8Q?si=ZwwAKvamjOCObRCN
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/662504" target="_blank">📅 09:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW73Z4TelxKccW_gaLEknjfULoEJEUQm7URRoEHN15v5CltK3tVMOh8cuunK3FxjTpUVjEajXTjZo6BKOE1YPiNFRluXzQaAcHAVxkaOz9FZdp3T0mNxsjR7Hc6Z9MaEXSTbQP7lGmKymGb8D6LTBUCAkXda4tGI06aaNdW1AJ8M6odxiKCMJRDHjIkVOOGFm_OZZ5VFpsjBGF6Gj5NW4_SrjLv5zJSl6xFG4GGlSL00iVWTbKh8wfQprvFBJCp4DuSVuaQBHVmyLMRBC9qAXj9tKAe936BorxEjhyEYJPw53Tea3JmOBxa7WF4OxOH0RlahACkLJPOGXO2t-hpzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در آخرین روز کاری هفته ۱۰۴ هزار واحد مثبت شد و به تراز ۵ میلیون و ۱۷۷ هزار واحد دست یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/662503" target="_blank">📅 09:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1b8581e9.mp4?token=nG12lK_UizauY0wDHABbCeKElzgAeWTU3TYpVvr1-xE934seCxeMES3VMFUu-bwMn8ReZZO85ZImAjpBboQdz-XbWRaUnu4mK-30R5jzw1cn8Ncezm92nwGqRk3FmynTtCIlRsKgAlTlmNX75F-KnhbtS-ZRDn9cju1E3tgdmRPkIt6ShVn0OIrRy5-f2-j2FU0iw8IEh9E9NF1KH3Tn3oEk1LBsEgzih3p2uBQfc99kSdz3Ds4oBbowcsYdFxrT7xoyAlNbPWPUgP97L7Kygy9XZs1Dfc29uKIqgMxecdf7-lbOtyyrNkXEdkMQQNmPgl6N2TsTYWT8eamI2iw4fkUAKKRBQxEReF2H60ih4zwEwrEx2LcbuxqOT1FPSf-APchBvO9g9S-5OwY41OsBE8mVzlvQ0QvyL5Bp-TO31efjItfcoiLM2NZfxAK0l8PdMMn2wMQqTihZY3jyprwUkMPXim3yn4KP8yIMbqw7hpmNwqKFj8O2opxWX3jhW_fTlwSW612BB3HYiAkAGh0iEJH1iDMIT74J-dnYRRinD9Jw-pmK55XMIu66utzj0ZyY0Xwmv6Hg1i7GY7M-P9eT8k9Oxf2fAF048OQFkG2mU9LpD3be_zANI5t8WsWQR4jLNj1n6_04SSpa-kYuh9poa_Iw_ZPJ45vPkK3Zmk9gx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1b8581e9.mp4?token=nG12lK_UizauY0wDHABbCeKElzgAeWTU3TYpVvr1-xE934seCxeMES3VMFUu-bwMn8ReZZO85ZImAjpBboQdz-XbWRaUnu4mK-30R5jzw1cn8Ncezm92nwGqRk3FmynTtCIlRsKgAlTlmNX75F-KnhbtS-ZRDn9cju1E3tgdmRPkIt6ShVn0OIrRy5-f2-j2FU0iw8IEh9E9NF1KH3Tn3oEk1LBsEgzih3p2uBQfc99kSdz3Ds4oBbowcsYdFxrT7xoyAlNbPWPUgP97L7Kygy9XZs1Dfc29uKIqgMxecdf7-lbOtyyrNkXEdkMQQNmPgl6N2TsTYWT8eamI2iw4fkUAKKRBQxEReF2H60ih4zwEwrEx2LcbuxqOT1FPSf-APchBvO9g9S-5OwY41OsBE8mVzlvQ0QvyL5Bp-TO31efjItfcoiLM2NZfxAK0l8PdMMn2wMQqTihZY3jyprwUkMPXim3yn4KP8yIMbqw7hpmNwqKFj8O2opxWX3jhW_fTlwSW612BB3HYiAkAGh0iEJH1iDMIT74J-dnYRRinD9Jw-pmK55XMIu66utzj0ZyY0Xwmv6Hg1i7GY7M-P9eT8k9Oxf2fAF048OQFkG2mU9LpD3be_zANI5t8WsWQR4jLNj1n6_04SSpa-kYuh9poa_Iw_ZPJ45vPkK3Zmk9gx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در آمریکا؛ ستون‌های عظیم دود آسمان شهر هیوستون را فرا گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662502" target="_blank">📅 09:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سازمان هواپیمایی کشوری: به مناسبت تشییع رهبر شهید، پروازها در فرودگاههای تهران (مهرآباد و امام) در ۱۲ تیر ممنوع و تا ۱۶ تیر با محدودیت همراه است
🔹
همچنین محدودیتهای مشابهی در قم (۱۶-۱۷ تیر) و مشهد (۱۷-۱۸ تیر) اعمال میشود و در برخی روزها جابهجایی مسافر کاملاً متوقف خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662501" target="_blank">📅 09:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای
وزیر دفاع پاکستان: حصول توافق میان ایران و آمریکا ممکن است به بازداشت نتانیاهو منجر شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662500" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
روزنامه معاریو: ترکیه با برخورداری از دومین ارتش بزرگ ناتو و خودکفایی ۸۰ درصدی در صنایع دفاعی، تهدیدی بزرگ‌تر از ایران برای اسرائیل محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662499" target="_blank">📅 09:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662498">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHZYJLO4Yxbgrcj8YJZUFMVgRYGON_AT3w-KQ4mwDbHv3WDDu1FVcPLqofv1cySrHtFVmxpf3Ab8UIiv8ettyWZZCVtKBKtBC3r5OEI4KACg3jtZbRl3YC8MEkAdhvE5CNIjIUl5ef-nki5SlHq8clrjB7Ypj4TYZkqaq0vS-jTjttlCr217OV1AAZG6TcKlnH_r72A5rU3l2bn0B3L_z8jNJdz8yM_C4twBWvd0hSw9rzJ3sLONG8g2Bl8bHTRaR9JGCiHuy4Vao8PZ77fhcoc3X5kVV1cUPiDgz8_IUnOrO37O4Jow1RVgxNQnvge1EjqFYYNVgsv0dnEoG3HQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌هایی که حذفشان از ادامه جام جهانی قطعی شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662498" target="_blank">📅 09:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1f0a815b.mp4?token=D-rpk4C3mZFtuP5uGy0aazt7dZCjobSigYkYWXGXHOB_hFboVd5tTINRoHRDXI7Zez8OJyXBH_J6HEz6W9qT2P4z6x4cTO9BMd43wAAuY1-XKZdqVOGP3rhsWeTRX8Ybs8i___Q7qILP1HTaFSF10B-P_Q-0-4Hiwsjnn8ZnRU-x7npLjOs8B7VIwaTq1Wrq_jkJCqOgZrhIoaQdJP29cxNTdo4bf67CuN72OXWiUmJaw7ca-JDAZxO4ZJjtRS7dCVVH5-JZmI0tMlJuOAdKaPAnrS-WL5MXc2_NhspvI8dPnlTmX6Mq55Gi_osmO8uueJbC7RtmhOxJzdexEW_TBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1f0a815b.mp4?token=D-rpk4C3mZFtuP5uGy0aazt7dZCjobSigYkYWXGXHOB_hFboVd5tTINRoHRDXI7Zez8OJyXBH_J6HEz6W9qT2P4z6x4cTO9BMd43wAAuY1-XKZdqVOGP3rhsWeTRX8Ybs8i___Q7qILP1HTaFSF10B-P_Q-0-4Hiwsjnn8ZnRU-x7npLjOs8B7VIwaTq1Wrq_jkJCqOgZrhIoaQdJP29cxNTdo4bf67CuN72OXWiUmJaw7ca-JDAZxO4ZJjtRS7dCVVH5-JZmI0tMlJuOAdKaPAnrS-WL5MXc2_NhspvI8dPnlTmX6Mq55Gi_osmO8uueJbC7RtmhOxJzdexEW_TBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سریع‌ترین راه برای پر کردن گونی!
با یه کم خلاقیت میتونی به راه‌حل‌های جالبی برسی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662497" target="_blank">📅 09:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGkWnRSHoePBIuSQE3Dn5FNruMVZhFmK2Nrtibe23_v9a4sfjzTvojs8qM-jBuRhxST92TJ2oD-Sh4P-RxnEIl_OJbxjT4ucbNEGUp4cPSOJdIsqXUseEvvcLtOFR1Q4b36URn2oTOxHtzVDNWZYyMFpceL4PZIOq0qxUhE-NIWWWmfRePsMNKO4wLjtXGg5huCNbd0ASq34cDWl4qFUxbzXdaU2PYjrf-dpSM8YBGGKDoDo_Jk0iUqgT5k7Ce1m4MjtoptvhDCAUEpWZmh64mECZkg0qTYbwBEjxBr0nVqi_CUhgAhcVQM2pnLu8XkbnJ2UUhyYy3PNV0RlEDth6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما با شما پدرکشتگی داریم!
سیدمحمد مرندی از تعجب دار و دسته‌ی ونس نسبت به رفتار سرد هیئت ایرانی:
🔹
"بمب‌های ترامپ فرزندان و رهبر ما را کشت. با این حال، ونس و گروه مطبوعاتی‌اش از اینکه مذاکره‌کنندگان ما دوستانه رفتار نمی‌کنند، شگفت‌زده شدند."
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662496" target="_blank">📅 09:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ثبت‌نام ایجاد و ترمیم سابقه تحصیلی آزمون‌های نهایی از امروز (۲ تیر) آغاز شد و به مدت ۶ روز ادامه دارد
🔹
متقاضیان می‌توانند برای ثبت‌نام به سامانه‌های
my.sanjesh.org
و
my.medu.ir
مراجعه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662495" target="_blank">📅 09:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnzN-vvL0q-gGsu8ZHQ4GlETmnF0g-DVan_mFcUdFz2C-yJJLJlSRO4u_MNYLVOmnhg8SNZgqMsBYzEkxD-ly2SUsBAuutRZjGRN6ZTjtJkgBFXX2zt6P2x8Ak1ONMcdP9K903Mc7rd8UYbEKdn2JEeO3mc8249zumdsOXvbY4yW-sXqS1reW4gKvpHpoRopyeYC7Ud15rEfASSmRPA3mh6_caNFCWVbsUenOeieIPlfP1CJ24sTQ1Oa4-ZphqVyjDwCYLq4Nu9cY5R4yp6w_w4Syc_bYJBNCQ6VrXnheMbOVSZb8p95vElJ09krZdunsxP2_KdXWj3sUf9JU2_wCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت کاهش یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662494" target="_blank">📅 09:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5630b934c.mp4?token=L1jjb3Ew6DQqapBwT4TnRGYKDzU1l1bhfF4ewDvfdz_VNMPffJAMu92KBbqtOi9l88Mum5UjhGAiNillWTB4dieWaAzE8Dbn7L2WbB_xpZa6Ny3EHDElWnYYnVHBW7iSK1wG0l4bZEsxJWmcaQuR8yTUTvmWiciWGDJJqAPj0BiwDQV0XPTpq5kAMqmgPi8HA8SMAipZ0DwSVFfsRmlOtFNm9DkHUGSE6pTOPrXNqFlXFxkRKN6QqSxBft0kMXKC-9Qa63vFyu7G1ZQB2HI-xnLN3csZbsxG0zz0fim0QK8Md-tWqXLOqjf8VyVGI4hHJk7B7CmG0BzhyQ8S6vTnGqDYas9ywHKZiXOk-fwoMRb8yU4yEX956PWX7VfKPM0OQft0jKnXZBdCRB9JLPij0Vey50FkiE5xfDO6V0uoUGAhDuuNjV5EBEbGmtEAk9sYZ0wwNf79baaX-iKw-Uzu3UyIFt44MaCJwg4Q4doyES2EgmDAy1mLJuIJ8m1gZt6_vw93Al9wV-G5xZZ2JSc-Tl8tuzXZ0TuBvEjpzwyHp16yCoY8SEcNSRBS2uhHSIIcMc8rnCqu7vMFG3TegmcZeLucg89CsRu2D37QNp_JpdxzKlpTY4SPeYwB93HQrpoiSz8GsZU3umx4-IIWVNg9eQkq-_UhjmSwh9wG1ZkwRIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5630b934c.mp4?token=L1jjb3Ew6DQqapBwT4TnRGYKDzU1l1bhfF4ewDvfdz_VNMPffJAMu92KBbqtOi9l88Mum5UjhGAiNillWTB4dieWaAzE8Dbn7L2WbB_xpZa6Ny3EHDElWnYYnVHBW7iSK1wG0l4bZEsxJWmcaQuR8yTUTvmWiciWGDJJqAPj0BiwDQV0XPTpq5kAMqmgPi8HA8SMAipZ0DwSVFfsRmlOtFNm9DkHUGSE6pTOPrXNqFlXFxkRKN6QqSxBft0kMXKC-9Qa63vFyu7G1ZQB2HI-xnLN3csZbsxG0zz0fim0QK8Md-tWqXLOqjf8VyVGI4hHJk7B7CmG0BzhyQ8S6vTnGqDYas9ywHKZiXOk-fwoMRb8yU4yEX956PWX7VfKPM0OQft0jKnXZBdCRB9JLPij0Vey50FkiE5xfDO6V0uoUGAhDuuNjV5EBEbGmtEAk9sYZ0wwNf79baaX-iKw-Uzu3UyIFt44MaCJwg4Q4doyES2EgmDAy1mLJuIJ8m1gZt6_vw93Al9wV-G5xZZ2JSc-Tl8tuzXZ0TuBvEjpzwyHp16yCoY8SEcNSRBS2uhHSIIcMc8rnCqu7vMFG3TegmcZeLucg89CsRu2D37QNp_JpdxzKlpTY4SPeYwB93HQrpoiSz8GsZU3umx4-IIWVNg9eQkq-_UhjmSwh9wG1ZkwRIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیبایی‌های بی‌پایان جام؛ شادی وایکینگی بازیکنان و هواداران نروژ پس از صعود
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662493" target="_blank">📅 08:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6fk_osMWkLlF4FbvaHkAVnv60NYm8w879V6AvX_Up6bfXLG3LLlQH2ed0_yX4GhW6UgPlmqMvPhJQDQJNCiB77YyTtUnNLp_C-MCVFWmT94CEesY3ZWKY0FKBAaKzhxUZ0ymx-aUURAULyLh1GM2GV-DSOsgfD-sVj3c2ohQ7bYAkMOShqp0a-P8kwgewBcDfbnY3gaQe-NnDY431Y43ss9Z1yYtPZol2PQZMBu-74CAih1RNj79KbSziyWamer6hxqul0yNtH5TXqdRL_F41-MYjhhuzqeAfELAlMEr3t5MjAzGi5Cw2QbIR0Dn45t9gwMWvLio7r7kjqzhiUvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسی به رکورد علی دایی هم رحم نکرد!
🔹
فوق‌ستاره آرژانتینی با ۲ گل مقابل اتریش، تعداد گل‌های ملی خود پس از ۳۰ سالگی را به ۶۴ رساند و از رکورد ۶۲ گل علی دایی عبور کرد.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/662492" target="_blank">📅 08:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تست سامانه‌های پدافندی و دفاعی در محدوده نیروگاه اتمی بوشهر امروز از ساعت ۹ تا ۱۰ صبح انجام می‌شود و صداهای شنیده‌شده از پیش برنامه‌ریزی شده است؛ جای نگرانی نیست
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/662491" target="_blank">📅 08:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662490">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4ZuGVLT8ph8VdIT4QFJtiJIyZdFJdRBInuoY87EAo98jgmZ61cDk0Py3L9jSlYVvMsHP35IBnmmf7r0nQ16xaR27AnpvSU5u1iXhMSKY4YIAbVRgyzeas5pADSKse0UZ9bGpTeimam_Kkhx303U-zE6yX8Tro9yWK1Inn48vYoFRkQYpHe7I-BC2akxhY8XpBWXLxFlqjJGmMzFPoAiRd89nafryT7vLFJ9h7Ze08p36miBe8ISmUBquf2wDyWb9QY4i-7ByqGELqM_30jykh-4-djNOaT0u84iA1zjCKnPt57tKsFyMRcpqphurp86sS07KZNkG85Tjex249SGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده مجلس:  یکشنبه آتی، صحن مجلس، کار خود را آغاز می کند/ احتمالا با موضوع بررسی روند اجرای تفاهم نامه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/662490" target="_blank">📅 08:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662489">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1fc12711f.mp4?token=cWNiuyKoUK2wWMpcMFn3zHQfssNzwLDm7eklx8G63siTln8jD6I-5DPfHSb2pRV_o9mbHhlImxPlYuosZ1rngyY2KI3RwMzVBJ4IaeheEeFYyLiD4_LD3SnIgbC4BbHThzsB1L8Rn0tJA-n7LTSRdSxxYLwfZsLfYFWRhEpMJijPYx07kqcMNxZkU8th9BTodUajz9GkxvumFSWeZmqlIr4IHtaFTJ8R0Jr_oBS248Aot0cczG7aICByfZvlJdO1kI8BHKdCrMVTS8qUXqMJj-BFLWDWmlCUNjE7Z-QsmzoxKJjBH8_brZHUz_1EVGEdnT18584DFIbt4kXByFISQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1fc12711f.mp4?token=cWNiuyKoUK2wWMpcMFn3zHQfssNzwLDm7eklx8G63siTln8jD6I-5DPfHSb2pRV_o9mbHhlImxPlYuosZ1rngyY2KI3RwMzVBJ4IaeheEeFYyLiD4_LD3SnIgbC4BbHThzsB1L8Rn0tJA-n7LTSRdSxxYLwfZsLfYFWRhEpMJijPYx07kqcMNxZkU8th9BTodUajz9GkxvumFSWeZmqlIr4IHtaFTJ8R0Jr_oBS248Aot0cczG7aICByfZvlJdO1kI8BHKdCrMVTS8qUXqMJj-BFLWDWmlCUNjE7Z-QsmzoxKJjBH8_brZHUz_1EVGEdnT18584DFIbt4kXByFISQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاخ سفید: ترامپ توافقی که به نفع آمریکا نباشد امضا نمی‌کند
کارولین لویت در مصاحبه با شبکه «فاکس‌نیوز»:
🔹
آنها به مذاکرات ادامه خواهند داد و اطمینان حاصل خواهند کرد که در نهایت به توافقی دست پیدا کنیم که نیازها و منافع مردم آمریکا و کشور ما را تأمین کند. ترامپ همواره اصل «اول آمریکا» را در نظر دارد و منافع آمریکا را در اولویت قرار می‌دهد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/662489" target="_blank">📅 08:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662488">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc9bfa8f1.mp4?token=Vqo22u8YKXqTG4ita1giVdnGpsDS75S_5YcmMAwdeN4sJ6hvTwyqGoh4vsFi2zQiXTL_C2uMJQq6LUpE9emPMeAHg2KVZW-315Phdxq4ER7jBTSu84xszOMK4J-skKil4h832sBXud58sgByCXF4m2uyTJyBgddG2drP80wN2D9zKKEyp2-xW-B0dlB0tEYzZvpC9OvJ1Ss1AcWWVLNOLrblcAk2qasv46Xasqta2K_5_0SA3uOuZJqmJ18yeCKnepUEDkbfMjIA36J5Lz0m4Nkn5vW42IIpWRnAsEy1Ary_Bw4zkMXM-1YP4RdCiFfp_ZM_-TQLJ6edalLuGvDGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc9bfa8f1.mp4?token=Vqo22u8YKXqTG4ita1giVdnGpsDS75S_5YcmMAwdeN4sJ6hvTwyqGoh4vsFi2zQiXTL_C2uMJQq6LUpE9emPMeAHg2KVZW-315Phdxq4ER7jBTSu84xszOMK4J-skKil4h832sBXud58sgByCXF4m2uyTJyBgddG2drP80wN2D9zKKEyp2-xW-B0dlB0tEYzZvpC9OvJ1Ss1AcWWVLNOLrblcAk2qasv46Xasqta2K_5_0SA3uOuZJqmJ18yeCKnepUEDkbfMjIA36J5Lz0m4Nkn5vW42IIpWRnAsEy1Ary_Bw4zkMXM-1YP4RdCiFfp_ZM_-TQLJ6edalLuGvDGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتارهای شرم‌آور صهیونیست‌ها ادامه دارد
🔹
انتشار تصاویری از آزار و اذیت و رفتار زننده سربازان اسرائیلی با مسیحیان فلسطینی و جلوگیری از برگزاری مراسم مذهبی، خشم مخالفان و صهیونیست‌ها را برانگیخته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/662488" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662487">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
علت پریدن آنتن گوشی‌ها چیست؟
🔹
بررسی‌ها نشان می‌دهد علت ضعیف شدن آنتن گوشی به عواملی مانند کاهش قدرت سیگنال، نقص فیزیکی آنتن، تداخل الکترومغناطیسی، فاصله از ایستگاه های تلفن همراه، موانع فیزیکی، مشکلات رجیستری موبایل، مشکلات نرم افزاری مربوط می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662487" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GeE39aeYBOqqO7dpdQwpo5xA8WXiDK-c_8DI2491Br_7zFF2SrmaNQFUUbQJ_ZsJn_dGwvpLlWRvTxiXZ-UtDFYLtLHTC4VZO2x0XrqIr8-Th6CzUIWcGXWGvgY91QfvJ6Nqwq0Jc6vEUB3cxxZ7-fGtjF_VnIbBbn0OzoE7oZZF-nWM_bXIiOd0CmIOX6xzfFelQChanYVKwHsWiGiUwQ19-Cckj9hY62-oKoJXtZ5xFgnr2Iih5gVKotx7nDU6x4xsM3MJggb3qhJrpL60HHrMoVspSvmDwUG7js14JsJlkBt5uozSei15lN2MJkwKNK0bi9JVGCQV5Sw79VazOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌هایی که تاکنون صعودشان به مرحله حذفی قطعی شده است
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/662486" target="_blank">📅 08:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662485">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941cbbdf87.mp4?token=NeJtQWbsrA1Uw0J-HJclM9meEDYhenNWPIyef0l6DBzoAwQd80c7y6dNLyehNYIA-Jr7fQ5zbBZqyHgF2KCg84T6s9cLHSv1XDf35jHyuaVSSk6fAad3yg-yYd6QxnqaxhoBZekMHGIKWI6BAl6ZJwN0E-ryTZ1gAWcsNB0crcdcUa-2yYlkPuCB4mV28au8MkQDNu20fQODgtL061wPm_YplmUzjdLGMrwEi3jUjsl07Y2JmTQq5aUaFeWzGpSBK8fwl-cHU1bs-CrmyJsH9z6Me_z7ivpz8-0XI_t_gwfKQSyNe0CVSQ6etmiSwZRPOwYv0au-69wpflTyeYaXpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941cbbdf87.mp4?token=NeJtQWbsrA1Uw0J-HJclM9meEDYhenNWPIyef0l6DBzoAwQd80c7y6dNLyehNYIA-Jr7fQ5zbBZqyHgF2KCg84T6s9cLHSv1XDf35jHyuaVSSk6fAad3yg-yYd6QxnqaxhoBZekMHGIKWI6BAl6ZJwN0E-ryTZ1gAWcsNB0crcdcUa-2yYlkPuCB4mV28au8MkQDNu20fQODgtL061wPm_YplmUzjdLGMrwEi3jUjsl07Y2JmTQq5aUaFeWzGpSBK8fwl-cHU1bs-CrmyJsH9z6Me_z7ivpz8-0XI_t_gwfKQSyNe0CVSQ6etmiSwZRPOwYv0au-69wpflTyeYaXpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیل‌گر آمریکایی: چطور ممکن است از حزبی [جمهوری‌خواه] حمایت کنم که به آمریکا وفادار نیست؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/662485" target="_blank">📅 08:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662484">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0c191c12.mp4?token=F53q-PC47Mx-4yaGgTMsjOKO5khpNrHBUzKj1hho40L3sdwHmzWtvCScjLYxDZZIQ1sy9rIuiScWG4lLsF1rQVDfgmKAddS6h6UDjrIjoKTE6VVYL3qG835kehtDfzq-waKsS1CEOC17srzXA4A4XFZsS0V-EwDxqG8XmkPZ11A2sXz3beVgQamAPljVSpSN3jhP6533DorSKQ63M3S-tcZPk3qHi7d_Djxdtw5YYLkYZKDmMs_D0W3myx3fVpIWGLCO7QelwN5VRMbYECuswq1K1m39mXB0B67QWj51LcQDtthBTSsme1yKcyYEvjRYIsZMfrS0g5364GKaEfwTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0c191c12.mp4?token=F53q-PC47Mx-4yaGgTMsjOKO5khpNrHBUzKj1hho40L3sdwHmzWtvCScjLYxDZZIQ1sy9rIuiScWG4lLsF1rQVDfgmKAddS6h6UDjrIjoKTE6VVYL3qG835kehtDfzq-waKsS1CEOC17srzXA4A4XFZsS0V-EwDxqG8XmkPZ11A2sXz3beVgQamAPljVSpSN3jhP6533DorSKQ63M3S-tcZPk3qHi7d_Djxdtw5YYLkYZKDmMs_D0W3myx3fVpIWGLCO7QelwN5VRMbYECuswq1K1m39mXB0B67QWj51LcQDtthBTSsme1yKcyYEvjRYIsZMfrS0g5364GKaEfwTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گردباد هولناک در روسیه برق ۵ هزار خانه را قطع، و ۱۵ نفر را زخمی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/662484" target="_blank">📅 08:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662483">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9750278c52.mp4?token=myBcHsBeqDaE4cLQnhJ1Zg6RbldcIqivqEz2h0sL80CwKqRMrVAW20v6CyXeVjQ5EF2JACIqGI9ICyhzV9shGkHBMd89tPI6gegyCFi0jtr9Rh49er-5QIp8RlcG1e-_ubF8_jjcOiLsP9ZEOULtGYUJoVO_QjgArmhOMH72K_HUYu0pIGegrRdhrmHoH7ROHHiL8_vgjsfURf1o-zRgSFTKL5a6AN9qKR2ZELCNP5GXv3KWv3U_CUDZR1SrKIv5GmSNfVvjvYpP1aV7PJGcgT21kY0SJhLIIVgfP5JduzIp9eJ_L1AN6Mg18tBzP0uLfmg7oQf5QrZrTj28QRsxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9750278c52.mp4?token=myBcHsBeqDaE4cLQnhJ1Zg6RbldcIqivqEz2h0sL80CwKqRMrVAW20v6CyXeVjQ5EF2JACIqGI9ICyhzV9shGkHBMd89tPI6gegyCFi0jtr9Rh49er-5QIp8RlcG1e-_ubF8_jjcOiLsP9ZEOULtGYUJoVO_QjgArmhOMH72K_HUYu0pIGegrRdhrmHoH7ROHHiL8_vgjsfURf1o-zRgSFTKL5a6AN9qKR2ZELCNP5GXv3KWv3U_CUDZR1SrKIv5GmSNfVvjvYpP1aV7PJGcgT21kY0SJhLIIVgfP5JduzIp9eJ_L1AN6Mg18tBzP0uLfmg7oQf5QrZrTj28QRsxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم فرانسه به عراق توسط دمبله
⬛️
🇮🇶
0️⃣
🏆
3️⃣
🇫🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/662483" target="_blank">📅 08:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662482">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/464379724c.mp4?token=I1CaD2xsQYpApEavJ5MT7cAL_zZoKcB4strzlNU6GyUeVqt6CG_PEQ6OboW1MKyDqKmiBILi9PgWuqM0fgtlL_3x6HJTOUlBbJaZWkGaYF7yD4riyb1uAPl7He2ZzLsypZdpF2k1lovPcJntwcXQaeVosHXpDiwsc2EUgVwxGm1OGoF6sDd16Uj6d1_HC8aHDcGvECg7lu4ZlF2pnpkDyGccZb3USWLBqPtXZL26dRvG33ZpfW_vdN3yMeiwG9NIzGktTOEgV98ZzI7mrmP1Bt-wwOQuYMBLflx5FbGlLqM2wbFMzscWYuJPIIjSB9CbBIunUjGmceP0AqA8MGU4_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/464379724c.mp4?token=I1CaD2xsQYpApEavJ5MT7cAL_zZoKcB4strzlNU6GyUeVqt6CG_PEQ6OboW1MKyDqKmiBILi9PgWuqM0fgtlL_3x6HJTOUlBbJaZWkGaYF7yD4riyb1uAPl7He2ZzLsypZdpF2k1lovPcJntwcXQaeVosHXpDiwsc2EUgVwxGm1OGoF6sDd16Uj6d1_HC8aHDcGvECg7lu4ZlF2pnpkDyGccZb3USWLBqPtXZL26dRvG33ZpfW_vdN3yMeiwG9NIzGktTOEgV98ZzI7mrmP1Bt-wwOQuYMBLflx5FbGlLqM2wbFMzscWYuJPIIjSB9CbBIunUjGmceP0AqA8MGU4_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیل مرشایمر درباره علت عصبانیت ترامپ از ایران و تهدیدات او درباره تنگه هرمز: او امروز فقط حرف‌های تند و توخالی می‌زند، این ناشی از سرخوردگی او از وضعیتی است که اسرائیل برایش ایجاد کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/662482" target="_blank">📅 07:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662481">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0phWgQxgQRrDDxOAUDbt0YP3gDm7g8YKMzjN8p2frcR67gPUp_uV061IXLwj4hpBnRp6VMLeX9cBRxyq5jeV-yZQ5EBHC1RauJZ1MvydvnmHN7Jbk5ME71sYbBbqSzr-Zu5bsYMK48gXMNOFq13q92SYWz47FoYHO2naxvfHhgQXsyI_TTd32JV8KYGDSCLuhhmhT3ngMthz2jEVAjJ10oyFteuFChj1GXQJlEoMNlTehgvKs2XNmgsj_UBArKPwq_gQcNG9kWtiQ0BZl2SFuPjSd0Bqdw98d8MNjlZfoB6_zYyGZB9yoNXJYGj3QjPZRnEHo9ntemXfm7Ktc2feA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: امارات برای خرید موشک مافوق‌صوت «براهموس» و سامانه پدافندی «آکاش‌تیر» با هند وارد مذاکره شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/662481" target="_blank">📅 07:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662480">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab56180ae.mp4?token=elVF9D1oKJX16OrHdGRxcIfKBBFh_wgniM0NKC6Gaub4X1ifyZo7obLpu7ibLQDx5rBAchZ4tc6KXMbFJVNYRlS3hqrt0RSb0q-YjO3opw8ubfUFxdI1hK2WbyiMk4wEeSvqD7LSHbQ4mNNbjMz5MTWJvqBkponFXgACxoKL2-b6-rmVps5OLTGH7qrhD4nYVPKlIpJWgwPbmv0guKDrNdyV9TeEaSU0OLzVpJC2_jDdGTC7sxnMgTBjQH3rpkUuKx0BiSmmiIpoPFb_qRXKA3Y899T7CYcJBjiWAWOA0mbmn3WUrfZQBtm4g1desR3y4JyfRCpirah-7t7IdXvzVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab56180ae.mp4?token=elVF9D1oKJX16OrHdGRxcIfKBBFh_wgniM0NKC6Gaub4X1ifyZo7obLpu7ibLQDx5rBAchZ4tc6KXMbFJVNYRlS3hqrt0RSb0q-YjO3opw8ubfUFxdI1hK2WbyiMk4wEeSvqD7LSHbQ4mNNbjMz5MTWJvqBkponFXgACxoKL2-b6-rmVps5OLTGH7qrhD4nYVPKlIpJWgwPbmv0guKDrNdyV9TeEaSU0OLzVpJC2_jDdGTC7sxnMgTBjQH3rpkUuKx0BiSmmiIpoPFb_qRXKA3Y899T7CYcJBjiWAWOA0mbmn3WUrfZQBtm4g1desR3y4JyfRCpirah-7t7IdXvzVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشتباه عجیب مدافع عراق، گل دوم فرانسه را رقم زد
⬛️
🇮🇶
0️⃣
🏆
2️⃣
🇫🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/662480" target="_blank">📅 07:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662478">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
نان در تهران گران شد
طبق اعلام کارگروه آردونان اتاق اصناف ایران، قیمت جدید انواع نان در استان تهران به شرح زیر است:
🔹
نان لواش: ۲ هزار و ۷۰۰ تومان
🔹
نان بربری: ۱۰ هزار تومان
🔹
نان سنگک: ۱۵ هزار و ۵۰۰ تومان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/662478" target="_blank">📅 07:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662477">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
خبر خوش برای دانشجویان دانشگاه آزاد
🔹
دانشگاه آزاد برای کاهش هزینه‌ها و جلوگیری از سفرهای بین‌شهری دانشجویان، امکان برگزاری امتحانات پایان‌ترم دانشجویان غیرپزشکی در واحدهای دانشگاهی محل سکونت را فراهم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/662477" target="_blank">📅 07:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662476">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82a913bcf2.mp4?token=bsmNIoG97Xt4vEgNd_EVWu0dEwjxmS_8Pc53ZyWbl9dJgKwyS-70MdcKBfhD5zZpslZCyfhTCPvN3DzhV7Rr_aneQPCibwMldcgwPHCXdKfKSFzQU-CV8BuEnLKW7WfmwsnPlggGzlBmF_HeUxZtzXq13O6K5tLUaIoIgfG49PTS2mVBhQeME0tmnHaU_GDxQt_Hzqe-Cd6gnYvTB-9M5jDtZkvubgXCm5iGsLqUxK5dRAbFI8XooRz_OrJIZHDVQdMxguOpMg4dyl9H5gJWgf2CwX2XNUEosTbEHQk9XY0jwMAgbnzNZCb4hUGs_uuFJ1oD1BE_woKe76-z-JjvHWimnYfvoBIvdVVE8_pN7WUHg2m40cJpJ8fDSrIkMgLef43veBVCrObs8UUeTX7bqTMWZOpAx0tRzigkIaPto_CwDqdJ6fU_9AlRHnhlFlnp6pkR7yj8sOdNX6DYCc1ZCI4IG2UFjkHlg-JO5enw0satvU8kh8SGDaZPbeKzvqRnb9S7OYmINDm_rehTj9sLBPOWKDGi6vO1KaMSJaswZzVsdT-TKpjXwSzng0Zy29GesGWaL1cSt3KiRtG_neZ3CUtSMBQT5x0wl50AL3qXm7q3onFPtOdwdiwfL5u28AliQ3CnsES8FQv5CmQPwUuWCZCLjM-qZimdGLtVOHECQX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82a913bcf2.mp4?token=bsmNIoG97Xt4vEgNd_EVWu0dEwjxmS_8Pc53ZyWbl9dJgKwyS-70MdcKBfhD5zZpslZCyfhTCPvN3DzhV7Rr_aneQPCibwMldcgwPHCXdKfKSFzQU-CV8BuEnLKW7WfmwsnPlggGzlBmF_HeUxZtzXq13O6K5tLUaIoIgfG49PTS2mVBhQeME0tmnHaU_GDxQt_Hzqe-Cd6gnYvTB-9M5jDtZkvubgXCm5iGsLqUxK5dRAbFI8XooRz_OrJIZHDVQdMxguOpMg4dyl9H5gJWgf2CwX2XNUEosTbEHQk9XY0jwMAgbnzNZCb4hUGs_uuFJ1oD1BE_woKe76-z-JjvHWimnYfvoBIvdVVE8_pN7WUHg2m40cJpJ8fDSrIkMgLef43veBVCrObs8UUeTX7bqTMWZOpAx0tRzigkIaPto_CwDqdJ6fU_9AlRHnhlFlnp6pkR7yj8sOdNX6DYCc1ZCI4IG2UFjkHlg-JO5enw0satvU8kh8SGDaZPbeKzvqRnb9S7OYmINDm_rehTj9sLBPOWKDGi6vO1KaMSJaswZzVsdT-TKpjXwSzng0Zy29GesGWaL1cSt3KiRtG_neZ3CUtSMBQT5x0wl50AL3qXm7q3onFPtOdwdiwfL5u28AliQ3CnsES8FQv5CmQPwUuWCZCLjM-qZimdGLtVOHECQX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده سابق کنست رژیم: ما با ملّت ایران دشمن هستیم و با آن‌ها در حال جنگیم؛ باید مردم ایران را بمباران کرد و به آن‌ها گرسنگی داد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/662476" target="_blank">📅 07:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662475">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آغاز اجرای توافقات جدید؛ آزادسازی ۱۲ میلیارد دلار از دارایی‌های ایران
🔹
غریب‌آبادی از نهایی شدن سازوکار مذاکرات آینده با تشکیل چهار کارگروه تخصصی خبر داد و اعلام کرد مجوز فروش نفت، محصولات پتروشیمی و فرآورده‌های نفتی ایران صادر شده است.
🔹
همچنین آزادسازی ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران وارد مرحله اجرایی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662475" target="_blank">📅 07:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662474">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حفظ امنیت منطقه و ایمنی کشتیرانی در تنگه هرمز، محور رایزنی‌های هیات ایران در مسقط
🔹
خبرگزاری رسمی عمان گزارش داد مقام‌های عمان و جمهوری اسلامی ایران در دیداری در مسقط بر استفاده از فرصت دیپلماتیک کنونی برای حمایت از تلاش‌های صلح و تقویت ثبات منطقه تأکید…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/662474" target="_blank">📅 07:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662473">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfrP2pFWlgrR6Ph8W41AdTTyp8q1ntsfXvVHHbA-ipRHkMIKdjiWB4D9WkaNQgA0tju_Vd-VitLJhIWXQTedYdnCeutvSQh61HH2_rZ0Cl4emAxgGdULtd3tpST-VQPWQPQR1ZowaEs6Wc7qB-2wlGEVRF2KomwRkf5M0OANnbTrqNp_nqWscX7CWGs3ZBz2XPJTFZnhJMIKxEjjI1mi1TKJwYuJ6pmBW8nI-bRezdC2H3adlQ3gss5e8Fsepmo2TKJUhwlttms0tB4YVXNfjBf1VP7067wbd1RLIXnkAaMxfN__lf-H00nHHptA1ljfZgXYjUeM6QJS5OBiq0McEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲ تیر ماه
۸ محرم ‌۱۴۴۸
۲۳ ژوئن ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/662473" target="_blank">📅 07:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662472">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری مذاکره | مذاکرات ایران امریکا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOAwSYxRYLvedoKpcnPNHx-qSKFRQXxPG-TAQFny9aALrsVAPYmuJZ_8J8KhO29r2w09zpIHApCgKjoq0ABdi3I5f6cq2Yaflj5WU0jHKcOxLtzYJ5Fu5mITLGHsFnsrA6q31aiujIqzKldOKC5Zoteao6069mleMnxvtc4-mOYufxldOR7U9ge6dA2FalG7GGU1pyLH510n66_BqJVMLev2Y2X3_ZlEtJEn4eVsuoBfR9uFm7rhTsLpk4zMEyNCKHfE2_4USypozJ83Jgdjp7p-nA03w4Vqz8ggMVU8ubKwtz9bfw2heh3N4crOvvb36rPenmrdbgLkM31xSkJDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/662472" target="_blank">📅 01:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662471">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b825fce2.mp4?token=qol-bsAb05Qp3_dAlhCKfIlccXrTy89YXYHODcezIRxoGMK8yJzONlGYaPXrOiAZ44iuKZGUIYSRv4EWjquQ5C-f6W-Jp6ANhUlF5V7ViR0rr6cRIHz17VJIvhFpvzw19LCs4DTNx2x76JfEMbcmoTOIt8p5-wIPpdyTTsWK-H4zSOtLGKZun3n72X0ow_F6MonYBKR_ViTx2KL071sWvW8OJeo96aYEdamOJK7rREZ5HcROxbYu-9D6yy32TxVKkBEQjuXmuFY2KsuaSPWlvid4ktUo0iQ6tZ2S6r6jGBDzUV0Qvtz2qOplndI_xOWuscsYnEJm5uoDDUao3egizA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b825fce2.mp4?token=qol-bsAb05Qp3_dAlhCKfIlccXrTy89YXYHODcezIRxoGMK8yJzONlGYaPXrOiAZ44iuKZGUIYSRv4EWjquQ5C-f6W-Jp6ANhUlF5V7ViR0rr6cRIHz17VJIvhFpvzw19LCs4DTNx2x76JfEMbcmoTOIt8p5-wIPpdyTTsWK-H4zSOtLGKZun3n72X0ow_F6MonYBKR_ViTx2KL071sWvW8OJeo96aYEdamOJK7rREZ5HcROxbYu-9D6yy32TxVKkBEQjuXmuFY2KsuaSPWlvid4ktUo0iQ6tZ2S6r6jGBDzUV0Qvtz2qOplndI_xOWuscsYnEJm5uoDDUao3egizA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با وجود سرکوب، مردم شیعه بحرین امشب عزاداری باشکوهی برای شب هفتم محرم برگزار کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/662471" target="_blank">📅 00:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662470">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c4668205.mp4?token=HO4DR4XaSGFOA5P1c737oRru0SiVtexM4v06mZnV01bKqxLXUDDyAqAciZHPHaaRTkB4VlDUehZbUzsyHHnjfb8X-e72VksBHQs_70tSsG23cbcyTow7BR6bSoS_Mab5MghpSr_-evz8uWRaaYTtrUX62t-nF9aPHRLM0QyyxFTE6wpeJmZUliWUKGWyqrnat0HjzbYBiFrIZ-HrDU0v7TXTrTNmfIxc2uIG_PEQLqVpDyD5rDmjaMMDgyjVY7dYDjPM6PMRtVpBPseqkAi0Dc5iu0vuxEXJw1RkRGalIaU5WjgCRro601ojOlzdm2C3yfY9TaOB4_FPOkcU-Q57AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c4668205.mp4?token=HO4DR4XaSGFOA5P1c737oRru0SiVtexM4v06mZnV01bKqxLXUDDyAqAciZHPHaaRTkB4VlDUehZbUzsyHHnjfb8X-e72VksBHQs_70tSsG23cbcyTow7BR6bSoS_Mab5MghpSr_-evz8uWRaaYTtrUX62t-nF9aPHRLM0QyyxFTE6wpeJmZUliWUKGWyqrnat0HjzbYBiFrIZ-HrDU0v7TXTrTNmfIxc2uIG_PEQLqVpDyD5rDmjaMMDgyjVY7dYDjPM6PMRtVpBPseqkAi0Dc5iu0vuxEXJw1RkRGalIaU5WjgCRro601ojOlzdm2C3yfY9TaOB4_FPOkcU-Q57AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: اگر به ایران حمله نمی‌کردیم، اسرائیل وجود نداشت
🔹
رئیس جمهور آمریکا با ادعای اینکه «عملیات چکش نیمه‌شب» موفق‌ترین حمله یک بمب‌افکن است، مدعی شد: «اگر ما این کار را نمی‌کردیم، الان اسرائیلی وجود نداشت».
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/662470" target="_blank">📅 00:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662469">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7607a8c682.mp4?token=uOFbgbm9yCp5rNucYKPPvak6-6XUoYvDZhWMAYk2-86yIOAJ7QnR3BurpXDeYEKNS8gCCK5lv5MUpm5WSjPWy4i0z5Coy1HuEbmipDvOu6WLMt0PQ51ZBlcYk9zkvnl8-FfED1bTEA4CYEPM9NmPPRW4KVbD_RAJJRLh3V9MIjtiOaaXTVR9E3auZfl5R9uDsIKmwr4ACABGZVwvlCu5BZI1V9pPUd9-Uhqj5J2ydLTASHxWorchxU0D2jPfk9w-C5xCcg3Lu-n26IO7ya7hGAD9k7MGz8we9ZNTsokkEcOYKoY062dCH0SLyMuz5M1Z7WDlMNT2BdyYaRHAqG0aMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7607a8c682.mp4?token=uOFbgbm9yCp5rNucYKPPvak6-6XUoYvDZhWMAYk2-86yIOAJ7QnR3BurpXDeYEKNS8gCCK5lv5MUpm5WSjPWy4i0z5Coy1HuEbmipDvOu6WLMt0PQ51ZBlcYk9zkvnl8-FfED1bTEA4CYEPM9NmPPRW4KVbD_RAJJRLh3V9MIjtiOaaXTVR9E3auZfl5R9uDsIKmwr4ACABGZVwvlCu5BZI1V9pPUd9-Uhqj5J2ydLTASHxWorchxU0D2jPfk9w-C5xCcg3Lu-n26IO7ya7hGAD9k7MGz8we9ZNTsokkEcOYKoY062dCH0SLyMuz5M1Z7WDlMNT2BdyYaRHAqG0aMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به عراق رو موشک کیلیان امباپه
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/662469" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662467">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
عبدالناصر همتی، رئیس کل بانک مرکزی: ما سالانه نیاز به خرید میلیاردها دلار کالای اساسی و دارو داریم و برای ما فرقی نمی‌کند پول خرید کالاهای اساسی را از چه منبعی پرداخت کنیم
🔹
اگر از منابع مسدودی بانک مرکزی بتوانیم این خریدها را انجام بدهیم، درعوض درامدهای…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/662467" target="_blank">📅 00:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
همتی: اگر نرخ و کیفیت نهاده‌های آمریکایی در مقایسه با سایر کشورها مناسب‌تر باشد، مانعی برای خرید از آن کشور نداریم
🔹
اصولاً طی سال‌های اخیر خریدهای جهاد کشاورزی از طریق شرکت‌های بزرگ آمریکایی و اروپایی بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/662465" target="_blank">📅 00:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662463">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c7a1ff2a.mp4?token=avalT9vbXhsoASI-xGxXb1_R_dqNVnQ8zaGhckPvjlt8IHehauGAeVWObJofFhRHGgoksV0aTZQVuLBRfXv2eedDOIANq-QK5Y3o7LrS5-8F9iv4DDqX8SzsCHVj0Pi22mEf9DIUMbJR51y1iQFG2sSBG8oYPZFMXeVz7lM0kXYC6C2fioq08dfjBYSivgaSTJgKsnRtjcpDZQ5SO29sahqpC1wDGAyBssZG3RFt5GcUD6pQQHaDa5ux0ITUderj4JpZVXjcVwduboI5g_LFsDQrgRRWSHlQH1di_yhcBtc2DwqlZyelsd4bWNbieDv-2eN-QSoX31CKG0J850ZreHy2iyspO2kpE3q5WUg7PU5SUKG1Eba10PL1dJqKcafKxUN6Zwso_qJR-4NPXAyOvgY-AC32QGKeWPUun_VrFkBlFPvAF5ye12RhBCBM0oyEVkWVzq4iVlLaIZYCntCyI4p51mKNXj_eFi8VgHSuEsJnQ3irrT5C9KALOhF6fCmJsWD7eHfWeHhAllViGaURsMyAm-plWNjPPxFPQiaUTqClFh328bgGyIh1jkFm6hpkdn-pGM0zRpJ2WjPScBnOHAABZ7JjCKbUSdbFydujnIvTY9S07o4SjArWCUYH0ARO-Eg2mpVXYEQbd_tbdgz8-Rhetx5AYOAIZOP3HYnfMYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c7a1ff2a.mp4?token=avalT9vbXhsoASI-xGxXb1_R_dqNVnQ8zaGhckPvjlt8IHehauGAeVWObJofFhRHGgoksV0aTZQVuLBRfXv2eedDOIANq-QK5Y3o7LrS5-8F9iv4DDqX8SzsCHVj0Pi22mEf9DIUMbJR51y1iQFG2sSBG8oYPZFMXeVz7lM0kXYC6C2fioq08dfjBYSivgaSTJgKsnRtjcpDZQ5SO29sahqpC1wDGAyBssZG3RFt5GcUD6pQQHaDa5ux0ITUderj4JpZVXjcVwduboI5g_LFsDQrgRRWSHlQH1di_yhcBtc2DwqlZyelsd4bWNbieDv-2eN-QSoX31CKG0J850ZreHy2iyspO2kpE3q5WUg7PU5SUKG1Eba10PL1dJqKcafKxUN6Zwso_qJR-4NPXAyOvgY-AC32QGKeWPUun_VrFkBlFPvAF5ye12RhBCBM0oyEVkWVzq4iVlLaIZYCntCyI4p51mKNXj_eFi8VgHSuEsJnQ3irrT5C9KALOhF6fCmJsWD7eHfWeHhAllViGaURsMyAm-plWNjPPxFPQiaUTqClFh328bgGyIh1jkFm6hpkdn-pGM0zRpJ2WjPScBnOHAABZ7JjCKbUSdbFydujnIvTY9S07o4SjArWCUYH0ARO-Eg2mpVXYEQbd_tbdgz8-Rhetx5AYOAIZOP3HYnfMYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل بدون آمریکا هیچ است و ایران قادر است آن را بکوبد
لری جانسون، تحلیلگر سیاسی و افسر سابق سازمان (CIA):
🔹
مسئولیت حفظ تمامیت ارضی لبنان بر عهده ایران و آمریکا دانسته شده و در مقابل، اسرائیل به‌عنوان ناقض این تمامیت ارضی معرفی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/662463" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662460">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
همتی رئیس کل بانک مرکزی: هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/662460" target="_blank">📅 00:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxOLoajVv1mJl_CqTz6dWZtFWrovjuz9FeJ-qmt1cxW-8zfS5SGS0Xr6vjLGXCbL172yrpyPWivECNh6GTM3YdVQLTkxIy3pYj9LlAne2urNbW6djLtLBT8S5BAtvTVcvLxY_gyKQzBBLck5iMYeauc5s_eyF1FZkJ_piW_nj3kko26I3ffFrXr2m5h8G1rGCiXDEaXBuCvh90ocW_WU3ib8V9K3gwzKEgdyF6UNnBKl806bdM5asmT-pRsFZ4-kYZkirZb-efc8kr9JtWoP9mq_bXIUynN9pN8GqHnbHwqiaQnYG9fYjXlBW8u-BX_F6DTHwFeqfT1JKLM_lcwBOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیرانوند: موقع گرفتن موقعیت گل بلژیک انگار یک انرژی عجیبی پشت دستم بود
🔹
من آن لحظه نه دست خودم را می‌دیدم نه توپ را؛ فقط دست خودم را انداختم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/662459" target="_blank">📅 00:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
همتی رئیس کل بانک مرکزی: هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/662458" target="_blank">📅 00:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e168bac7.mp4?token=bm6GBYdO9EXDvBnKfLm9cgVRXxbaLMab1ROkI4-heGNUAJl7f3mNJVusLGR2FEENl9OQLg5bGMOGQ61HvR0NUuyzVa_-ONsUxWvuZeu9tZ4wOK0YqYbsLfaQXy-TtlZt4E8HEWldBjJrPOG7Th3ipvlTK1H_M3rQsVeDf3qu7caUIxViSMGKxIwwH8PqbXHUOmutliMT9fDD5Lv2u13HZ6w-tB-hRUdo4z9MgHpKkZMr-9RJZ6Cf1Axha5tlnzoyVttOzC2ex-jT1PaZ2fR-JUod2oM6ll2O58Terhc6cY1syM6snDs1GraV4lKmbm4FZnaaacrNKcf8g5jupMZGrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e168bac7.mp4?token=bm6GBYdO9EXDvBnKfLm9cgVRXxbaLMab1ROkI4-heGNUAJl7f3mNJVusLGR2FEENl9OQLg5bGMOGQ61HvR0NUuyzVa_-ONsUxWvuZeu9tZ4wOK0YqYbsLfaQXy-TtlZt4E8HEWldBjJrPOG7Th3ipvlTK1H_M3rQsVeDf3qu7caUIxViSMGKxIwwH8PqbXHUOmutliMT9fDD5Lv2u13HZ6w-tB-hRUdo4z9MgHpKkZMr-9RJZ6Cf1Axha5tlnzoyVttOzC2ex-jT1PaZ2fR-JUod2oM6ll2O58Terhc6cY1syM6snDs1GraV4lKmbm4FZnaaacrNKcf8g5jupMZGrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله دوباره ترامپ به اعضای ناتو: ما دیگر در ناتو هزینه نخواهیم کرد / استارمر گفت اگر پیروز بشوید به کمک شما می آییم، هیچ یک از اعضای اروپا به کمک ما در جنگ ایران نیامدند! #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/662457" target="_blank">📅 00:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff99eb275.mp4?token=SDiwSpxygg82w5YTMudvYhUCBW2OLqVrv95AySjDDiLf36x4Ormt_C5ePdmOP--wsICBVaNfP3oCHOBydGXD4gVPG4Sv7nnmN3rJJzMpFI_2j0Rs5eTSTrzpUMuU9iMTdK8HxAV4PEm5sFVor-Ga1F4bEq2bBHn61Yjv3_w97P_YglK_AraMBx9SOl3miRV4RQvViZW62f5StGcbhs6TdVMhPCvGaFxsGkX8et3Zmb1VoLEeMycdh5rVz09q8drpXy0cSYgjqEaFfVhoLDJdr72y4GL3vVL5oWLPKB2gRbwLZQ2IlolPtV2UND7ZP14cRuasC1SJ4Qw4P9G3AatZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff99eb275.mp4?token=SDiwSpxygg82w5YTMudvYhUCBW2OLqVrv95AySjDDiLf36x4Ormt_C5ePdmOP--wsICBVaNfP3oCHOBydGXD4gVPG4Sv7nnmN3rJJzMpFI_2j0Rs5eTSTrzpUMuU9iMTdK8HxAV4PEm5sFVor-Ga1F4bEq2bBHn61Yjv3_w97P_YglK_AraMBx9SOl3miRV4RQvViZW62f5StGcbhs6TdVMhPCvGaFxsGkX8et3Zmb1VoLEeMycdh5rVz09q8drpXy0cSYgjqEaFfVhoLDJdr72y4GL3vVL5oWLPKB2gRbwLZQ2IlolPtV2UND7ZP14cRuasC1SJ4Qw4P9G3AatZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات خصمانه ترامپ: ایرانی ها تا زمانی که به ما احترام بگذارند لازم نیست نگران چیزی باشند / محاصره دریایی ایران از بمباران تاثیر بیشتری داشت / با یک تماس تلفنی میتوانم محاصره را برگردانم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/662454" target="_blank">📅 00:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
قالیباف، رئیس هیأت مذاکره‌کننده ایران: انتقاد و آگاهی، حق همه مردم است
🔹
البته چون در جنگ هستیم، اگر بخواهیم همه‌چیز را بگوییم تا مردم آگاه شوند، به همان میزان دشمن نیز از اسرار ما آگاه می‌شود. بنابراین ناگزیریم، نه از سر بی‌اعتمادی به مردم، بلکه به‌خاطر…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/662453" target="_blank">📅 00:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR-bOT-Wi2GNqtZEnzF1wMyrqS7GNEYMfW6OVYJDJmO9zNZP6Q77uHdVNIe7DhLW8dqTeQKZESYdANkOgi7NNEejP18lqyr9LxF9EfXQVU2dxCY2mqIPm0jBWa7rFrMb5yS4AE-aN8ZFNSbvtvC9GPK9QdVoMJJln9RwmPCOILsoRVpobcfPjmD8o9Px5z5wtzYo0OzlH_zkPRO6goBSVftCNaZoJxaxDAsfn2ZmD6Y21K916KumgD0Kezk0v7YhXlLTSMBf5Zopo-xZ1eiv_XVWojsqdXtv_P_SgnvonKKMb6UgBFgillHo4VQpJhv41bmrmSBRYvvv4Y0DFS3fLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/662451" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662448">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
قالیباف، رئیس هیأت مذاکره‌کننده ایران: دیدم در [یک] برنامه [صداوسیما] اعلام شد که کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، مسلمانان و شیعیان لبنان کشته می‌شدن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/662448" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662446">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d098b42cd0.mp4?token=e8eevo3icBeoQnjH6NOWvkdN-ICDFjKAEd7x-KFRkqdJuBgWUKHsRGNOP9xp0Dq6DZATpIvAthD0PdxxpyrtJlkPC9_93a_Cn-RYe_XMi0IbvjZiwM1VmasyV-Oh6y_f47JqZvYECzuBus-zbN9BGMM4rLaPdCEK8dJPCb_ju9zF_ZmUwotFl2iqR5JNCDjN0fm-2Ni6MLZRBR1ZHWMdvNGpGAtB9GzdbVHetD7wnAYSYOE6zawv4ssuJP6Usucl-3vxesr6oAGFYHdnaczLz1q-bJuEe_ucAXeUM3RcRq35PYsxPVs0Y_KWf2afA-1W4b1bWCQDtAwjxXNyqGEgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d098b42cd0.mp4?token=e8eevo3icBeoQnjH6NOWvkdN-ICDFjKAEd7x-KFRkqdJuBgWUKHsRGNOP9xp0Dq6DZATpIvAthD0PdxxpyrtJlkPC9_93a_Cn-RYe_XMi0IbvjZiwM1VmasyV-Oh6y_f47JqZvYECzuBus-zbN9BGMM4rLaPdCEK8dJPCb_ju9zF_ZmUwotFl2iqR5JNCDjN0fm-2Ni6MLZRBR1ZHWMdvNGpGAtB9GzdbVHetD7wnAYSYOE6zawv4ssuJP6Usucl-3vxesr6oAGFYHdnaczLz1q-bJuEe_ucAXeUM3RcRq35PYsxPVs0Y_KWf2afA-1W4b1bWCQDtAwjxXNyqGEgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات خصمانه ترامپ: ایرانی ها تا زمانی که به ما احترام بگذارند لازم نیست نگران چیزی باشند / محاصره دریایی ایران از بمباران تاثیر بیشتری داشت / با یک تماس تلفنی میتوانم محاصره را برگردانم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/662446" target="_blank">📅 23:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662445">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaft1-KbGu1PjIgyviMXv9XHxGSOIRMwVjz-d-7S5tcL2Rgq_OiPCWwvk5mJMEe6tRg8ADerpeTBLmKcjhXKw3GeL3h2dmAV67esvFbyZPC2LFKpHt1__aXM5NmRWj7xYGDnoV5JwmHEK52Bp2ss3ECtBdtaTJxcu1h5Rm4LaVT_ObmQVx3YFTQGatCB_y5IRAAkZ9gEQd3xOtL7CzxKx6vgLwhuEVkGouvHwIC1HLk2jS6dTIvvETpZRD97gp57FbyCIWks208zMIYXIp2zHspfKvuf8Kn00uf7HOpLA9G1paFSm5_cJMYiTXO5Hyx_UekFXY5HKKDCh_RU1oQ0TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ‏«إنّ للحسین فی قلوب المؤمنین حرارة لا تبرد أبداً»
🔹
هر کجا می‌نگرم رنگ رخش جلوه‌گر است
هر کجا می‌گذرم جلوه مستانه اوست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/662445" target="_blank">📅 23:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662444">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b2c57e7a.mp4?token=XvUXM_1s5iMBfBRUQZSSGmIzElLnJghiuP_Q2xoptrCGVgfoNHL_RkhsBQw3wWAjtMCVTw7rUrqCNg2Dl1KDceh-CWLzUHsUzUy8vHNCB0kxCZoNphjIst6p5lUTSPBz-_DE1kSSUThSRrwr-NZcA6ZcIkQf7r-IJrQmBV31iFAQCQ-WaaF1AEQZTIQtvom3nGZdZudJiGFsAiBmteoRrIIgDM-It6tfLYg2d-MJIUh-MhoQxCM_vmS86voLc3CeQwF774njAOwHkrmP3l0iG5bHu3qcCemiAvEcPQ5HiJW6Q0zolWyFwgcM12s2nlJC-8eBfvVEU-6Ec06MOE2SMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b2c57e7a.mp4?token=XvUXM_1s5iMBfBRUQZSSGmIzElLnJghiuP_Q2xoptrCGVgfoNHL_RkhsBQw3wWAjtMCVTw7rUrqCNg2Dl1KDceh-CWLzUHsUzUy8vHNCB0kxCZoNphjIst6p5lUTSPBz-_DE1kSSUThSRrwr-NZcA6ZcIkQf7r-IJrQmBV31iFAQCQ-WaaF1AEQZTIQtvom3nGZdZudJiGFsAiBmteoRrIIgDM-It6tfLYg2d-MJIUh-MhoQxCM_vmS86voLc3CeQwF774njAOwHkrmP3l0iG5bHu3qcCemiAvEcPQ5HiJW6Q0zolWyFwgcM12s2nlJC-8eBfvVEU-6Ec06MOE2SMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اراجیف ترامپ درباره ایران: در لایه سوم مسئولین ایران؛ هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران باشد
🔹
آنها ۹۱ میلیون نفر جمعیت دارند؛ نمی‌توانند آنها را تغذیه کنند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/662444" target="_blank">📅 23:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662443">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
خبرنگار: وزارت خزانه‌داری تحریم‌ها را از نفت ایران برداشت  ترامپ:
🔹
من باید دقیقاً وضعیت را بفهمم، اما اگر تحریم‌ها برداشته شوند، پول به این کشور وارد خواهد شد. تمام آن پول بازمی‌گردد. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/662443" target="_blank">📅 23:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662442">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
خبرنگار: وزارت خزانه‌داری تحریم‌ها را از نفت ایران برداشت
ترامپ:
🔹
من باید دقیقاً وضعیت را بفهمم، اما اگر تحریم‌ها برداشته شوند، پول به این کشور وارد خواهد شد. تمام آن پول بازمی‌گردد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/662442" target="_blank">📅 23:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662441">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای ترامپ: مذاکرات با ایران خوب پیشرفت / پول‌های ایران از بلوکه شدن آزاد شد و فقط می‌توانند از کشاورزهای آمریکایی خرید کنند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/662441" target="_blank">📅 23:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
قالیباف: باید حول محور ولایت وحدت داشته باشیم/باید بدانیم فصل‌الخطاب، کلام و دستور رهبری است
🔹
آزادسازی پول‌های بلوکه شده و رفع تحریم های نفتی در سفر سوئیس نهایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/662438" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a752b4180f.mp4?token=ZHmgGjWF3IY7gFEDogTRw8bHRgI5iUXSkQCMWaefqd7SoYpUQ3ogKL-WSaIbjEDjT7Bv_ogDdyZpxNtrQfWv1Ms0kzQ_CEa6n5xDWg6e6gvcoo2txGiyJGbsQUE9u1_BTedDZlD_N6S4os5d_XxKpZtyE_hVq9x5bbMJbA9gNu0pTosrWfv_rFqoAw30g0vbHbgxDPCOurZt7sv73sc4618REjyiJuqCb8B0otKWYqdiYh9WORqhRhKUi8hCUvzBeGahbuRyQkBWWxJSg_sxzH0WsN8iJaNwiyihIr5CaZUstOklcLR_kOVr3bTfFrLziQpDsa5tfPJuR-z5ouL8bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a752b4180f.mp4?token=ZHmgGjWF3IY7gFEDogTRw8bHRgI5iUXSkQCMWaefqd7SoYpUQ3ogKL-WSaIbjEDjT7Bv_ogDdyZpxNtrQfWv1Ms0kzQ_CEa6n5xDWg6e6gvcoo2txGiyJGbsQUE9u1_BTedDZlD_N6S4os5d_XxKpZtyE_hVq9x5bbMJbA9gNu0pTosrWfv_rFqoAw30g0vbHbgxDPCOurZt7sv73sc4618REjyiJuqCb8B0otKWYqdiYh9WORqhRhKUi8hCUvzBeGahbuRyQkBWWxJSg_sxzH0WsN8iJaNwiyihIr5CaZUstOklcLR_kOVr3bTfFrLziQpDsa5tfPJuR-z5ouL8bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف
:
باید حول محور ولایت وحدت داشته باشیم
/
باید بدانیم فصل‌الخطاب، کلام و دستور رهبری است
🔹
آزادسازی پول‌های بلوکه شده و رفع تحریم های نفتی در سفر سوئیس نهایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/662437" target="_blank">📅 23:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q03Y9LeHpKrv5Y-6-UjfDAL0k6a8MpYDqsn74ETS4vKmXxC5J9KCrElWkJwTJDMVnReoT6dkgOdOApzj0L0cV0RViNreTmF5xBwrsQMBRpDI68iw_C0n_IlM5OqSoMWlFRyfryYNHpw5Ze9HaPrZluSbM9ZpXkIJshjnI8j7VYO6Nb4NTsDWfBEPvwifenO24ajf1mVgdJ7iWmohJXqnx2zW5nmo4AO_JkVg25eCvunLrX2DmVCV2b3mngC_mdH9l2gs4YpgWOvKZNMrYtrqEMIIAHbWZsmH6zwU_wrx6uP81YUxwkqA-TPgYiXbFqwgXMvCBfIgtUqPwv27HlNveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بالای یک قوطی فلفل سیاه در یکی از سایت های خرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/662436" target="_blank">📅 23:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c41e0981.mp4?token=KDVzTPkP7c00Snfa5Ax7dvpH0vQjILoGKIT0RPB-6M71WB28FLALjRsJCwTcbzVMlziD6YF6Whq4anqHNkrsD3MTMu30i9B7aLdDTS2S-w9QCaPWIuFuZfA8pcPxt7ygMOrZ8R6_m9L6n0xwrHENLXCP-rtyBj1RSuN6uzmGHCkaAGNa2JEtmH71BLcoJvFz7RYuJLlvVPniEbACH8LX5aNwBqktV-LqbK_5ciibaZRoujrE25uZydCUz3dH6h0mJfubAazTB_ZtdzXIGVqGRlY2zxN6eTDSKyiU8t48o5NLUbv12aLMNzGWinH1TgJSA4_NQFiWsOQVDNT9_EZj3ThvHnCr2mhutavD5UPebMZBXOrygGwS5vumZTszedg-V4iullnHtFqVdfY8DjdF-s5nZtl-xLSgsEmcahavkl8hyyG_vPWGdAtRdVpXPFSQE5lDT94_xruz-sDnOJfqL78Dstj12Zo1vDvdlY0iTN8XvT8HVSBUdxXLUDe16R4pkBF-YcBaDg_yBlVt67ftS8EvZzmIJaRZ4QSa67huB2Hn3Mna4T3XRuG4NMzzpAIxWrPZ_F7O1vs7HFgwQl3W41DhoVnXCLLdqqCDCNQIx7Ai54zfxxchkZ2K2HJegKG-RDjmyAdThVEwVp8D7EGOCYav4smm65h7myEy7wi4_XM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c41e0981.mp4?token=KDVzTPkP7c00Snfa5Ax7dvpH0vQjILoGKIT0RPB-6M71WB28FLALjRsJCwTcbzVMlziD6YF6Whq4anqHNkrsD3MTMu30i9B7aLdDTS2S-w9QCaPWIuFuZfA8pcPxt7ygMOrZ8R6_m9L6n0xwrHENLXCP-rtyBj1RSuN6uzmGHCkaAGNa2JEtmH71BLcoJvFz7RYuJLlvVPniEbACH8LX5aNwBqktV-LqbK_5ciibaZRoujrE25uZydCUz3dH6h0mJfubAazTB_ZtdzXIGVqGRlY2zxN6eTDSKyiU8t48o5NLUbv12aLMNzGWinH1TgJSA4_NQFiWsOQVDNT9_EZj3ThvHnCr2mhutavD5UPebMZBXOrygGwS5vumZTszedg-V4iullnHtFqVdfY8DjdF-s5nZtl-xLSgsEmcahavkl8hyyG_vPWGdAtRdVpXPFSQE5lDT94_xruz-sDnOJfqL78Dstj12Zo1vDvdlY0iTN8XvT8HVSBUdxXLUDe16R4pkBF-YcBaDg_yBlVt67ftS8EvZzmIJaRZ4QSa67huB2Hn3Mna4T3XRuG4NMzzpAIxWrPZ_F7O1vs7HFgwQl3W41DhoVnXCLLdqqCDCNQIx7Ai54zfxxchkZ2K2HJegKG-RDjmyAdThVEwVp8D7EGOCYav4smm65h7myEy7wi4_XM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس هیأت مذاکره‌کننده ایران
:
ماجرای حاضر نشدن تیم ایرانی در یک قاب با طرف آمریکایی و خروج از نشست مذاکرات پس از تهدیدات ترامپ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/662435" target="_blank">📅 23:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قالیباف: سفر به سوئیس برای مذاکرات چهارجانبه، دقیقاً در امتداد میدان نظامی بود  قالیباف، رئیس هیأت مذاکره‌کننده ایران در پرواز بازگشت از مذاکرات چهارجانبه سوئیس:
🔹
نیروهای مسلح ما با افتخار، قدرت و شجاعت، این پیروزی بزرگ را به دست آوردند. در مقطع آتش‌بس…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/662434" target="_blank">📅 23:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
فوت دختر ۱۲ ساله در یکی از پارک های آبی مشهد
حسینی، فرماندار مشهد:
🔹
متوفی دختری ۱۲ ساله از استان گلستان بوده که به همراه مادر و خواهرش به مشهد آمده بودند.
🔹
این نوجوان در حوالی ساعت ۱۷ بعدازظهر روز گذشته چند دقیقه پس از استفاده از سرسره آبی، در محوطه داخلی یکی از پارک‌های آبی دچار مشکل شد و متاسفانه اقدامات امدادی و عملیات احیا برای ایشان موثر واقع نشده است.
🔹
خانواده متوفی شکایتی از این مجموعه آبی نکرده‌اند و علت دقیق فوت و جزئیات حادثه از سوی پزشکی قانونی در دست بررسی است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/662433" target="_blank">📅 23:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662432">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
قالیباف:
سفر به سوئیس برای مذاکرات چهارجانبه، دقیقاً در امتداد میدان نظامی بود
قالیباف، رئیس هیأت مذاکره‌کننده ایران در پرواز بازگشت از مذاکرات چهارجانبه سوئیس:
🔹
نیروهای مسلح ما با افتخار، قدرت و شجاعت، این پیروزی بزرگ را به دست آوردند. در مقطع آتش‌بس و پایان جنگ، این بخش را با مذاکره پیش بردیم. اگر در اجرای آن اشکالاتی پیش بیاید، در پاسخ می‌توانیم هم با موشک پاسخ دهیم و هم با مذاکره آن را حل کنیم.
🔹
طبیعتاً همه ما، چه نیروهای مسلح و چه دستگاه دیپلماسی، مرتب با یکدیگر در ارتباط هستیم.
بنده نیز دیپلمات نیستم؛ یک رزمنده‌ام.
🔹
دیپلماسی را دنبال کردیم و دیدید که پایان جنگ و رفع محاصره را با گفت‌وگو، به روش مبارزه و با اتکا به قدرت میدان نهایی کردیم. عرصه دیپلماسی و میدان، مکمل یکدیگر هستند.
🔹
در بحث لبنان، از وقتی وارد مذاکرات سوئیس شدیم، دیدیم که آتش دشمن علیه لبنان قطع شده و بخش عمده‌ای از مردم به خانه‌های خود بازگشته‌اند.
ان‌شاءالله با تصمیمی که در سوئیس گرفته شد، تمامیت ارضی و حاکمیت ملی لبنان را در این گفت‌وگوها به نتیجه می‌رسانیم
و تا رسیدن به نتیجه، آن را رها نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/662432" target="_blank">📅 23:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662431">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
اژه‌ای: ۶.۵ میلیارد دلار سرمایه ملی در حوزه ارزهای صادراتی و تراستی‌ها به کشور بازگشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/662431" target="_blank">📅 23:33 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
