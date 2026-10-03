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
<img src="https://cdn4.telesco.pe/file/CTVfq0lPhVwc7XBGgMfy5ttbF_jA3hbT5CTEDLEFwy27SsAl1-QE-5PjVo_wW5O9B9WCBXA4UwfKDpqLjFKzNIK2ZJss7Q2PNYkZAZQZm-foi-VK0kKljP-Qukk38hdT6HU-EWe4WA2V0c3MIqOYRunDx-ULgISg4dPHJ_g3_tAZkai_01H3xY0_amUbpBeIzWH87vzv6SDsVPPnTdYnPARTcVc6Li0muDe6ivMRJ9GSAyZUqX9YXg2I5o6y74-0mgLVVbKpgEHsCku8eaOFMKF4ekhOim-4s7jHTC9VHlKqPM2XnfZxpgTXwRuoogOYJGIgckA6IFx4ztCHJ8-wWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-695206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3Fi8paFAvdsO1-gew5hvu8A1jTAvDWCizcAghAHcAGlSgYsTZEDZK0CcwxH40OA5EwVWapaFNM3iyxvcXVasSfpYGAm3wUiIVMTID4UF-Wyskb4My_VhK9pp1uKlrdGNhwa20qMZ3ieBkwj0EQDgQd6EBJuX5KyCsnD9kHPPLz1657seTjSDCxLMiEckWXeKcRvsey1IaaE1iDsrEXIanBg7W3FlxGTEseJ3zDBNd3VdG7q98S3ZT7kNftjlUfh8pe1WbKtbCMPq69UV0RScPu6-uNSSBmRmDdopqHApbG_jSbOEPCfI7CpTAHEXtIKhsMAIzw508T3o4_d4PolnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhZcK86UdwijkyYQp1Z_B9DKScTdvycDDbgo53AU0-muS1rTUP4qwa35YvonQachhTLsNYP5x-_zrLkgHFDyITfcBs9gM223q1oqHtyiHY6tO4ByOaWyEE1UBEEQsHRYX72kWMoOs2mVwFj2hubQBw3Hsm1EximupOaXrX9VS_iZdtVzmgJ3anEsM5zRFgFaUrWvgDNnYUxvjgL8BLx26OJs0eSEuabg06Vs1nfh6KiU-2x4FAyxdLDl19lpaypjx1IA2fjJ_viX18KCWaCUDUx3TdAXrB0c1GrwFSY9O6UsMOWR3nIpcXv2pbbimTbsqThX9Hj4SlVeyuWl5D1Inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z24DcGz6W8D9FiXKQ4sTRNUVNcb1cN5CU5mSic1sKx5ZT3TQKQB4OdBV1rWVqf6yYsVNXLwNLZ1qlDzIyr3pkDc5x_tIBPIWymvqXUF3ef-cKjiz9hkHak0JTuJgWM2Y7EKoh-tk3JKwrzx-AC5pNzHyFjzOOnECoBKBzE5ySEos8Ez_v5w4sFMAD8uVCOHAMsSXLF2H6R3W5cNIFYXXml-6STWpjuM9ca1hv6laXvNHyzc1sSb-B_AZ9HD4E_6tMZB8gi30TL4HaeFUmsLQtiSuqAbdI5dSsKiH47M1noZlSlwpLyRa17yYKNBy7RUlzzkH3Kd7NEnxfnqVlwZS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwamAH_XJSDGIJ65OwG_H7SH5IQdYwAjebclcbLmtaNnFEjilB0av1hgejwHm-rhwTCpoXV2yNMJFl7P50cIyIvVb39U9MjUnc8c-vA93u5ABLBmOvCHjbhLxKSzNuXzcX6jErpT9iWWMZIDLADwK20jp5xNaFcsSATWrNgVoGTs804GBt03VwreT1LmBGl8V8ZAhaszWe-OVGuCqgoMaVuDuwSyXvi0vATA6pDQ6EU5SA0HXdv9emO5h6_gCgzH1lK_01l4QIMJUPf8afNXnHMGmnYoWtooEk8lqJpgsvLw8i6c8PXfkafCZfEbyCUPr_Q2N8tkjyt9k4ZNfcqWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdnTlN5_blgqNBvJ8GoK-osli190yeXE-xR4z1KLKwBKw2_AxYtsFC8Tdd2Q1KQZYNgyJPWD_bJMA1zVhsi4ZzF7kC4XqiTXW2KmMiEvEdtrKiNwk2wiZQ9Qjj0suKLYtEgKttH1gTwTNiT1vaqrksx8k_aDbwidtMHhmV5S87ksdSAx7gF5DpR0JLrytreGeZA5C373VqvN94ApQxnKIBNf--LBaUUPBemm6xfdi3BcEZY8GD1BigUAo-RutGje1jwx9zo5k4h7N1aFL4jbl24MwyVZbMXTpoBg6z58oIax5PfvtyvjFsWONfUMmBLMieZIyU-n5UGjCINO5B6S9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/paeLZv1_09a_ET7PgXqRP1KgBorqyI_3iHofSkA6oY_DeuFlv3DN3EAdEH8TaIFjDpUbHwjU-qC6c21anrAXg2LUKrhjdKQezDuXICekP0DT5MAEYbwpdKNdGjt0RZc0PYVJgLHe4HpT1vofKMmPM6u2Nv5cxEc958caahvb2ctg6QqRr85GIZ4vhs489a-AyeqAtq7qOAtDZEu8m_eaqRe8gRzHEWdM1dPIc8i7CKyaICiknsDCUWuVu1F4thHrxHHyebfA5VrM-eLo42T1j251flWFw0Q7y6nlIuT0nDhykv158CBYDWGV18fEzBmvhCqF2HfDKQt-CAYbwWtoZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چطور محتوای هوش مصنوعی را کشف کنیم؟
🔹
فکر می‌کنید اگه واترمارک رو حذف کنین، فایل رو فشرده کنید یا متن خروجی هوش‌مصنوعی رو بازنویسی کنید، واقعا می‌‌تونید تمام ردپاهای هوش مصنوعی رو پاک کنید؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/695206" target="_blank">📅 17:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حساب صرافی‌های رمزارزی در آستانۀ مسدودی
🔹
بانک مرکزی قصد دارد حساب‌ها و درگاه‌های ریالی برخی صرافی‌های رمزارزی را به‌دلیل سفارش‌گذاری‌های مصنوعی در بازار تتر و ایجاد اختلال در قیمت‌گذاری تتر و بازار ارز مسدود کند.
🔹
پیش از این نیز در دی ۱۴۰۳ درگاه‌های ورودی ریالی صرافی‌های رمزارزی مسدود شده بود.
🔹
شدت برخورد این‌بار بیشتر خواهد بود، اما یک طرف حساب صرافی‌ها برای تسویۀ وجوه کاربران باز می‌ماند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/695205" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
دومین نفتکش امروز در تنگه هرمز منفجر شد؛ در ۵ روز گذشته ۸ نفتکش در مسیر جنوبی تنگه هدف گرفته شده‌اند/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/695204" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c86f2a125.mp4?token=sJaXn0w_KSXOnhJwXOiYyx7ZWZKuwTT3MVHTQ4_KLWqn_Opj2ll_MnKvkykjn2lYNpTwK44FFUXn-F04DjlGUOEfhg2RjPjveVMV_d_CmsGCT2nZRzjou7sxnlCzmqm8O7mB5D3KAoU9w_aOaEyu8ac2D7RQKZsrslETkYAO583cL1vnt861_W6A-1lL5qAug83_GJrUmsHUegbb1eLW_9s9nrmSbjLPdnL9SPshZoL-HOqHFCpKoR4fzl1UP91Ob_XaUFzvk86QM9Vu6P5QvDik-TNtJOwwhQoF3RJalZ5aWaDz5TVsQ7TKraW7YdkmHCjkdBfnE1p-U0tycoajkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c86f2a125.mp4?token=sJaXn0w_KSXOnhJwXOiYyx7ZWZKuwTT3MVHTQ4_KLWqn_Opj2ll_MnKvkykjn2lYNpTwK44FFUXn-F04DjlGUOEfhg2RjPjveVMV_d_CmsGCT2nZRzjou7sxnlCzmqm8O7mB5D3KAoU9w_aOaEyu8ac2D7RQKZsrslETkYAO583cL1vnt861_W6A-1lL5qAug83_GJrUmsHUegbb1eLW_9s9nrmSbjLPdnL9SPshZoL-HOqHFCpKoR4fzl1UP91Ob_XaUFzvk86QM9Vu6P5QvDik-TNtJOwwhQoF3RJalZ5aWaDz5TVsQ7TKraW7YdkmHCjkdBfnE1p-U0tycoajkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعی برق در اثر طوفان شدید در قم  #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/695203" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33998a3453.mp4?token=JKoA5S28q4fZK5PhA-3kinSu7GgHXWER4xTAwlMkbAOoGBRt_rwHhsOMltGOwVoM5gvXw0LXn78a1PMaz9c1UvTKRBQNqhCYsbHliv9lDE3J54L3OC78byeHN1J3mT8gUz23qJmI-CesNebNq7OsVo5L-IjY2anW_SGVNYUSE3bJkv9MyXfGTTLxPGmD7Nhrv9C7rQFvHY_Ae6GhjPt_Eg0N8FyurbvvmHhqcfxzx_ymuPd0awwCAMeOTdCMouwqlYeLheZDkWtClbgwrLPhS0ycUdbM82YLNf2QqPUmBsgUxmpFKuRchOiNgXkufeNoZKery-V_xJI1-poBCiDOlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33998a3453.mp4?token=JKoA5S28q4fZK5PhA-3kinSu7GgHXWER4xTAwlMkbAOoGBRt_rwHhsOMltGOwVoM5gvXw0LXn78a1PMaz9c1UvTKRBQNqhCYsbHliv9lDE3J54L3OC78byeHN1J3mT8gUz23qJmI-CesNebNq7OsVo5L-IjY2anW_SGVNYUSE3bJkv9MyXfGTTLxPGmD7Nhrv9C7rQFvHY_Ae6GhjPt_Eg0N8FyurbvvmHhqcfxzx_ymuPd0awwCAMeOTdCMouwqlYeLheZDkWtClbgwrLPhS0ycUdbM82YLNf2QqPUmBsgUxmpFKuRchOiNgXkufeNoZKery-V_xJI1-poBCiDOlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان خرگوش و لاک‌پشت در دنیای واقعی هم ثابت شد
🐢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/695202" target="_blank">📅 17:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شهرداران کلان‌شهرها از پزشکیان چه خواستند؟
🔹
مومنی وزیر کشور خطاب به رییس جمهور: مولد سازی را به شهرداران بسپارید نتیجه اش بهتر از الان است
🔹
نصرتی معاون عمران وزیر و رییس سازمان شهرداری ها و دهیاری ها: شهرداری ها برنامه عرضه مایحتاج مردم تا ۳۰ درصد پایین تر از بازار را  دارند.
🔹
درخواست صریح یک آتش‌نشان از رییس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/695201" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WebNIOd3ScNz-OwpUhQsmKnBSvRXkTIoO1hniP9RUdJtHQBfcJkvhkSlC-sB2b3bi5PdVdzu1hguiLqgkZyvxoz29WyvF6m5WifPMYxBGK6oMpE_0-MwbJ4pd-VDdB9UHBuFi_0eI6yhPQB_kBwfA0jWAIoyYIN90LTRo8OADJ9vYpH5SMbzspR7rVZ06lBWD9-Vh57Vac_8PgUouui2icLQHCs1muDR-bqH6X9YFu4pgGBTmxlM2K9woyE8T3b2M1Bfazpxpaxl_-kQvPgV8rzUo_iJly91Jmvp2wBMGqdNU4xoXL7-6E9KHSnWMhtP8_SB9moCfIv4yZx6AhT10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست امروز گلشیفته فراهانی در اینستاگرام: سال‌ها پیش تهران
🔹
این پست گمانه‌زنی‌ها در مورد احتمال بازگشت گلشیفته فراهانی به ایران را افزایش داده. پیش از این خبرگزاری تابناک از احتمال سفر فراهانی به ایران خبر داده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/695200" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=MdDjZHoipvQONmwuXMbBaJmiO21Ty2O6brOCE03GRbbjVjYHkHTl5QAPSJzwW7tPR8Rinz1YCdaFAQ8pgwrkcLplU9DdxArsSnQp1-Zm6b43AFOd977nB_NqqRvyTjuNI5yIg6WsUU3ztKgB7qt57JbF6qGcdfjViqJg1XGOKOCHO623A5NIW0VPT49qY4vrtbooO7JVfbyRHh5kRdFY1d9Gcr7gEHngh9i7Au3WWwG4goIB779bjuG7VRGBa-rRg15BPI_Py7KVJGCbnUYOEy6kGuHN_VxWuILz-PUDqFvo43-JVNgavxGqMiAhnz_UIrOIU6CVlfvVEg48oFfGWIB3PmWMVWYxdXwGrJ1AZJb_gRPAVdn4bRQqScU9Itt1H5MpAyslCoXBp413sp4rt90ZfIt7BfAOwI61lCKBsH61xhs6Uq__ILGAp06dZfVL4is9Ttfb8d6H237jPsYtDOei1_JcKyJcOHY7SbO8cAqxCeaKDOomv16jBkmd8dqFV73Q_0Nhl6reO0BTVMRnTm2H_dONraXaodqvuZT69a18wUGnJLrCjSMWeeU_PvvBV-RwIeJn6VdtQvoQGKsXejKS2xOWzWWam1wVCHwZ0JXOdQh4Yj7kCCcfWB-DXI1pMlBiyAupqFm4WFPA6Ghmtb5Pi-DE3vthZ-LUE99CWNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=MdDjZHoipvQONmwuXMbBaJmiO21Ty2O6brOCE03GRbbjVjYHkHTl5QAPSJzwW7tPR8Rinz1YCdaFAQ8pgwrkcLplU9DdxArsSnQp1-Zm6b43AFOd977nB_NqqRvyTjuNI5yIg6WsUU3ztKgB7qt57JbF6qGcdfjViqJg1XGOKOCHO623A5NIW0VPT49qY4vrtbooO7JVfbyRHh5kRdFY1d9Gcr7gEHngh9i7Au3WWwG4goIB779bjuG7VRGBa-rRg15BPI_Py7KVJGCbnUYOEy6kGuHN_VxWuILz-PUDqFvo43-JVNgavxGqMiAhnz_UIrOIU6CVlfvVEg48oFfGWIB3PmWMVWYxdXwGrJ1AZJb_gRPAVdn4bRQqScU9Itt1H5MpAyslCoXBp413sp4rt90ZfIt7BfAOwI61lCKBsH61xhs6Uq__ILGAp06dZfVL4is9Ttfb8d6H237jPsYtDOei1_JcKyJcOHY7SbO8cAqxCeaKDOomv16jBkmd8dqFV73Q_0Nhl6reO0BTVMRnTm2H_dONraXaodqvuZT69a18wUGnJLrCjSMWeeU_PvvBV-RwIeJn6VdtQvoQGKsXejKS2xOWzWWam1wVCHwZ0JXOdQh4Yj7kCCcfWB-DXI1pMlBiyAupqFm4WFPA6Ghmtb5Pi-DE3vthZ-LUE99CWNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ بارش شدید باران در برخی مناطق تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/695199" target="_blank">📅 17:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4lq2mx_yU4ydw07Eyqt_NC7mr2T_sToaSedOm4TuyruqBk_-Fk9jJ2NnU7gUSVPVeIJuJJ7y0V6jOrz7NUFmsDQEmku2NELZUBQgBOZvgX9zIgxrSBN8oviqGDasVdvxlzKlHEbp_FQ-VNvQfDtTtODt4AtgugXj4WGqcHlvuTbXH-RJ_CCIsihwUHF1Gk2m82ZEW65I8E2Jck8pywfrPU1frbzW55JzgPoKdNtnbsWsYt-bGwqtkAASscD4AizJsOEDyVx_p1492kGb8ifL6Bt4W4xQxCE4mTIiXyhUdBM6tx8nVNVZaRNCVeg-Qwz56an9yVYPC67bwwN3-rVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
المیادین: ارتش یمن کنترل رشته‌کوه راهبردی راسن در استان تعز را به دست گرفت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/695198" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7WZ45rrHA1RARDXWx2y0_sxWh9uNFsXwY646viLpT_wmQvIOI5TzNMOyE6-h2Hc_gXFDCjr5GPi7AvEY2ayJo4BWyEYKmS3dHvAiD-Sek4S1Ll8hgw3dw51mFdK4ZfpKJP_-Ui0T2x62BfrOk4bQE6vnFS_-7pb2r-V9J64GKWCxsxft-7rWYK9d-DV3ulLw_u8AjaOsEFMZPk6K5t0embGGpet6LjWGm49eIvKyMd0n-5ZUyaK_21CshFC7ca5TytAs9llqPsmhEZYq0IM8EnW8dVpwNlAgOvET5Jq0UcU5DVaSdAzj4BUWlelAR_kjKINu1ugKO7EFD8tluBqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۶ نشانه در بدنتان که نباید نادیده گرفته‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/695197" target="_blank">📅 17:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPAW7toiZ3RMa5RSiOtBF-2HFjmao1qmv_GgWCYolyntJCgMudhQ8duHBbVnhFWiwoAbj5RTXcQfF9o9PULLnz11DCuAK1zIcBO3i4moXcmjjTyjueuK9zVow8RNHDo9h3ufslyiL4_k3DpiZCvdAMAjlIPv7iKKesiXSBI-NNgJIxU4WFnv0GDx9GIgL2VLqxW-4bypBoPRZp1q89DcfcS-DMVMEOO0g4rZCmPTCx2LFgkiY3HXUiRxI-ZbwHlZzgj0DUyUVVnNyGvsKcVec7CFoDU_9W7wf4sN1hi0kJmRyP8nIIvsiQAuq_KT__NzRDmzwF6CnTnNZxlPfDXGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مدیرعامل بانک کشاورزی تشریح کرد:
ثبت سود عملیاتی ۵.۳ همتی؛ بانک کشاورزی در مسیر تثبیت سودآوری پایدار
🔻
مدیرعامل بانک کشاورزی با تشریح مهم‌ترین دستاوردهای این بانک در سال گذشته، از ثبت ۵.۳ همت سود عملیاتی، کاهش ۴۸ درصدی هزینه‌های مالی، رشد ۳۵ درصدی درآمدها و صفر شدن اضافه‌برداشت بانک خبر داد و تأکید کرد: تداوم این مسیر، مستلزم توجه جدی به جزئیات، توسعه بازار و سودآوری پایدار است.
🔻
وهب متقی‌نیا با قدردانی از تلاش مدیران و کارکنان این بانک در سراسر کشور، دستاوردهای حاصل‌شده را محصول کار تیمی در شعب، مدیریت‌های استانی، ستاد و هیات ‌مدیره بانک دانست و اظهار داشت: ثبت سود ۵.۳ همتی، با وجود تعدیلات  اعمال‌شده در فرآیند بررسی صورت‌های مالی، از محل عملیات بانک محقق شده و این موضوع در شرایط کنونی نظام بانکی، دستاوردی بزرگ و کم‌سابقه است.
🔗
مشروح‌خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/695196" target="_blank">📅 17:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695195">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b985326ea.mp4?token=vZp244s4oRp9NmnXdqEUM21GVpxd_TWmAbKIaAV44TV9HZd8QzH43I5kZfl9FzAwwSlIwvO7Yn2YONJNs8BYDCNu4IrTKJ9zlacHJknSR7MADYlgvYjLZJKOjkH36C93zWAj7w2hRUqx9JPvHc7eWoiSDf1WCaagorxhAq5quTmpWkcjcGdi6cjrBruv0mbcLFwkS00mNizbFtZk_7HVBrZJnySnw0gsALJWgCwcH9TErWFKBQq9jxx_gTUeTd-9gVRuREEuuganLi_1QIZ0NycBfqRO9FNtlSFi_tvUpGw3mJj5WjnCKuO3GjV9e1_8EGKY5dAeL9nRw_vtGd2Xnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b985326ea.mp4?token=vZp244s4oRp9NmnXdqEUM21GVpxd_TWmAbKIaAV44TV9HZd8QzH43I5kZfl9FzAwwSlIwvO7Yn2YONJNs8BYDCNu4IrTKJ9zlacHJknSR7MADYlgvYjLZJKOjkH36C93zWAj7w2hRUqx9JPvHc7eWoiSDf1WCaagorxhAq5quTmpWkcjcGdi6cjrBruv0mbcLFwkS00mNizbFtZk_7HVBrZJnySnw0gsALJWgCwcH9TErWFKBQq9jxx_gTUeTd-9gVRuREEuuganLi_1QIZ0NycBfqRO9FNtlSFi_tvUpGw3mJj5WjnCKuO3GjV9e1_8EGKY5dAeL9nRw_vtGd2Xnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری‌ها در فرانسه همچنان در حال گسترش است؛ از تنش و درگیری با نیروهای پلیس و افراد لباس‌شخصی تا حمله به خودروی پلیس و غارت یک فروشگاه پوشاک
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/695195" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695194">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای الجزیره: دمشق و تهران در حال نزدیک شدن به یکدیگر هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/695194" target="_blank">📅 17:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695193">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb250b2e7d.mp4?token=Q7TmHh7vQYt0YAgKZ4fwFLvGU81kcj_0t7LpNiBF_QeMtJB81jA7EZF_rLsoooXK2KCB6bj5B22b15GpzdbqSMUfi2h6WSIU9svpWLCZe6dTgGpN8b95PnzWcetma8DqM8WSYbuq0Sf41xohDnHdvVWlhz0yfzwrtjptXuelpEVfUc_16rRhPfC_w6N0QfsNbXu4_RHwUPAdtHgiv6v1o5IwBh5KIEtcDOc6tcA7eX3wz-CL6v0Aw0ZvhvWpmQ7x-7o8-cEu9dcvTU1EB8KVaurRQ1mlumYRpd95WkqFifw9dJvK51S8Gxh3SxRIvstZ_3vFg5VsDHTC9mgtq2cHYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb250b2e7d.mp4?token=Q7TmHh7vQYt0YAgKZ4fwFLvGU81kcj_0t7LpNiBF_QeMtJB81jA7EZF_rLsoooXK2KCB6bj5B22b15GpzdbqSMUfi2h6WSIU9svpWLCZe6dTgGpN8b95PnzWcetma8DqM8WSYbuq0Sf41xohDnHdvVWlhz0yfzwrtjptXuelpEVfUc_16rRhPfC_w6N0QfsNbXu4_RHwUPAdtHgiv6v1o5IwBh5KIEtcDOc6tcA7eX3wz-CL6v0Aw0ZvhvWpmQ7x-7o8-cEu9dcvTU1EB8KVaurRQ1mlumYRpd95WkqFifw9dJvK51S8Gxh3SxRIvstZ_3vFg5VsDHTC9mgtq2cHYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش متفاوت و خلاقانه برای الک کردن آرد؛ ساده، سریع و کاربردی
🍞
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/695193" target="_blank">📅 17:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695192">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
عصر شنبه صدای انفجارهایی از جزیره قشم شنیده شد؛ بررسی‌ها نشان می‌دهد هیچ حادثه یا اصابتی در جزیره رخ نداده و صداها احتمالاً مربوط به اقدامات نظامی در پهنه آبی خلیج فارس و تنگه هرمز بوده است./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/695192" target="_blank">📅 17:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695191">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ترامپ قمارباز: معمولاً در انتخابات میان‌دوره‌ای عملکرد خوبی ندارید و نمی‌دانم چرا #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/695191" target="_blank">📅 17:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695190">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ترامپ قمارباز: معمولاً در انتخابات میان‌دوره‌ای عملکرد خوبی ندارید و نمی‌دانم چرا
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/695190" target="_blank">📅 17:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695189">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWskiHFRK1wwHmKvT74tNFA-gozIrYdJMlKsQkM7Fw1_gRJXXRknOJk2edrRNpEL9gZeGzoA42D6fo_wj6jMZjvbbtoeubpoHu8hShiI8twtay2ehEnsR2NHSEkw7HGGvmvMeIqhWE5Q95LRwIduKCkaKqji2XZgLPsnCjgEk4kAywaCztHfzWHexHkEy_Rm8uVrsLQMzYSTWtYYua0GOsq333GaQ7yWRn2Fcv7wxGZMaERMF1ejFRcN3O2IwIfe13HNjFJgYSCi2zFHAPN26n5DVdZ0LpmFbJ30iDZZj34ryo98bju2PZ00VNIEdrOmd16SdQb70L9AMQOuyK6vjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ها از سرنگونی یک پهپاد متخاصم در نزدیکی سواحل ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/695189" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695188">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93aeff917.mp4?token=RGRJ0F_PoFcOSsrLzYABmCNETg4a6y1sAvsoZQ1UmLUDFmtxB584YFAbDrMMeeeUC2QBCg_CVWovn3p8amUDrs4oyZZ_NeOQhKPEa72EczOIOrxFRnTkHgA0PMc1vJpDGojcvprV8YRr_lBoB0VAh9lsESgwJFwY5NQZsbVqaNNrTdO0y1etXY63xKy9if9KLoNACCGIyrplRiyuWRScP34oLhm0a2d0_fMCGnkJ9XWhBlSaXOGc-MbDsIhHpajauaq3UBcrmcKYcJLd0NLmbYa7B6Vr3Crqkh_4oDm4h9zv4rkq2sbejfig0_W5ot49j1WcQ8jLoOOXayO1VZOReT8bbr1VBPE4vkeQ5y-MQ55Mx8j0jHKx3w6sV5SrA9VFzhxoGUZFJCndnEfqZDzPWUIgTCmzKNdciWcszA0WE3qOwTfNm-eVreDTSLkr6fkpGD9E9DSZyoOb6pBTUEidEwZUp0gbrvW_BO8tHgt7-eUUGa02HA9V4qkyxl-lErZ_b3j86unxTeOUtt40LVZA9QNh-ugNSf1wYsb_9WO-XlOUpAbjYOorPrxbnwBvkCr04c9VgsbRf-7mkkINEl8jg-B4Iewh1Nq4j0GfD2SpijuzVItXxCal_rTIPmJ-uBb8PWwXNkMGuBEekmv-8VwZGzGVDpxVW0PoPPRF31N9H0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93aeff917.mp4?token=RGRJ0F_PoFcOSsrLzYABmCNETg4a6y1sAvsoZQ1UmLUDFmtxB584YFAbDrMMeeeUC2QBCg_CVWovn3p8amUDrs4oyZZ_NeOQhKPEa72EczOIOrxFRnTkHgA0PMc1vJpDGojcvprV8YRr_lBoB0VAh9lsESgwJFwY5NQZsbVqaNNrTdO0y1etXY63xKy9if9KLoNACCGIyrplRiyuWRScP34oLhm0a2d0_fMCGnkJ9XWhBlSaXOGc-MbDsIhHpajauaq3UBcrmcKYcJLd0NLmbYa7B6Vr3Crqkh_4oDm4h9zv4rkq2sbejfig0_W5ot49j1WcQ8jLoOOXayO1VZOReT8bbr1VBPE4vkeQ5y-MQ55Mx8j0jHKx3w6sV5SrA9VFzhxoGUZFJCndnEfqZDzPWUIgTCmzKNdciWcszA0WE3qOwTfNm-eVreDTSLkr6fkpGD9E9DSZyoOb6pBTUEidEwZUp0gbrvW_BO8tHgt7-eUUGa02HA9V4qkyxl-lErZ_b3j86unxTeOUtt40LVZA9QNh-ugNSf1wYsb_9WO-XlOUpAbjYOorPrxbnwBvkCr04c9VgsbRf-7mkkINEl8jg-B4Iewh1Nq4j0GfD2SpijuzVItXxCal_rTIPmJ-uBb8PWwXNkMGuBEekmv-8VwZGzGVDpxVW0PoPPRF31N9H0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای سرمایه گذاری، طلا بهتره یا نقره؟
🔹
اگر طلا دارید و فکر می‌کنید نقره هم، همون کار رو براتون انجام می‌ده، صبر کنید! یک بررسی 40 ساله، یک تفاوت خیلی مهم بین طلا و نقره رو نشون میده.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/695188" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695186">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
بلومبرگ: ایران می‌خواهد فشار را تحمل کند تا آمریکا کم بیاورد
بلومبرگ:
🔹
محاسبه در تهران این است که فشار داخلی را تاب بیاورد و منتظر فرسوده‌شدن حضور آمریکا بماند؛ مقام سابق شورای اطلاعات ملی آمریکا نیز می‌گوید ادامه این راهبرد در بلندمدت فشار «واقعی» بر نیروی دریایی آمریکا وارد می‌کند. نفت ۱۰۰ دلاری و انتخابات میان‌دوره‌ای هم ترامپ را تحت فشار گذاشته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/695186" target="_blank">📅 16:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695185">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
قطعی برق در اثر طوفان شدید در قم
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/695185" target="_blank">📅 16:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695184">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P36d6z9wEPoZtjgG9ds615Ik1Sr0-A-WQsv-96TBIssYywpHrgOe_NwlDHa4BWgPTKx3lFQFxCEJAJydonw7xMDTSg5toHzUVSyciwRkxKuXONRAgStGL-kymDtQzh2h2Nee-Id6qVzaI2Fja909O7vBogeg7n6v9x6guARkNFsWEq0sEb3qEaUVCPJtxNFzVSrn4xYmlbDAwudqx9w6B4QB7mDYgF2gsnuRxEw5RpLwts2fXWUGqEkbu8WFhcMI3LZtVJHIIUXJhFD5smUFIXyJhEVQZUOftGu0VKzhrT9DWiLRrEbxkgInQyndSBwOzCVgzwMorjf-aOgDZzlIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این مواد غذایی رو جایگزین کن؛ لاغر شو!
🥗
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/695184" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695183">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9ff93120.mp4?token=dlI7tEgBGusvrfOrBghd3a7aP229Y0loPLuk46myAULzZ1JxXA1c2Zuc92TUDnSXFATmpszjuxnbB_27lgw0iiDlkxnxnWVYxfcESLmDiCPrn_BQ8aaT02T6grOuBrT9MhIeEYKuAlx47OpU0ActGZEVBZUFhwcjYfVUU8BCitJun-28mm7CP7tbrIyH4XAYG6YCm82MjL2fbktrWCf6VtIEIMRBu59yk5G3bdqArjN7pcixDD5agNhvEXYlVn7COyO6nT8WxlPCdkCLLDAgs5o07aQcrCH_4GWj_Mig2jX1Pmg_M7EN2ZIPTL-DjPb4uW0Zqty_rx4T7QyJl6hG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9ff93120.mp4?token=dlI7tEgBGusvrfOrBghd3a7aP229Y0loPLuk46myAULzZ1JxXA1c2Zuc92TUDnSXFATmpszjuxnbB_27lgw0iiDlkxnxnWVYxfcESLmDiCPrn_BQ8aaT02T6grOuBrT9MhIeEYKuAlx47OpU0ActGZEVBZUFhwcjYfVUU8BCitJun-28mm7CP7tbrIyH4XAYG6YCm82MjL2fbktrWCf6VtIEIMRBu59yk5G3bdqArjN7pcixDD5agNhvEXYlVn7COyO6nT8WxlPCdkCLLDAgs5o07aQcrCH_4GWj_Mig2jX1Pmg_M7EN2ZIPTL-DjPb4uW0Zqty_rx4T7QyJl6hG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی وحید یامین‌پور با حاج حسین یکتا در منزل شهید لبنانی در روستای عرب صالیم در منطقه نبطیه جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/695183" target="_blank">📅 16:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=TWE7ECamM_bG_eWiFtkZRbyw-_AK7y2q4bSFX1E722SsHRi_xpTrEm70Iefo1rix5k-jc1WCOUsdOvWB2rjKtd_m9cnxg3394NOMMz60Dd-wUcsBgBaOl2q0OxZtU_MsU9Rr69NDRx9oBukXaQULJy8erUCkJtIqfPlx_k19npKJ9iSUf5iX_jp1Q48QJokSmLcay1v0Dh0X_ATeMD9ETa6oZwn6DZ-EBDptAj0utfsfXCBkzHQYr_sBKpPYhn0ROd8BQ13WxoFVfmCyJevK6sXIiwwhK0jNBeppUBlegq_GOvfj_O94DH4p8BtjWqJ2KvgB4TQDgzt4VSishSRa1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=TWE7ECamM_bG_eWiFtkZRbyw-_AK7y2q4bSFX1E722SsHRi_xpTrEm70Iefo1rix5k-jc1WCOUsdOvWB2rjKtd_m9cnxg3394NOMMz60Dd-wUcsBgBaOl2q0OxZtU_MsU9Rr69NDRx9oBukXaQULJy8erUCkJtIqfPlx_k19npKJ9iSUf5iX_jp1Q48QJokSmLcay1v0Dh0X_ATeMD9ETa6oZwn6DZ-EBDptAj0utfsfXCBkzHQYr_sBKpPYhn0ROd8BQ13WxoFVfmCyJevK6sXIiwwhK0jNBeppUBlegq_GOvfj_O94DH4p8BtjWqJ2KvgB4TQDgzt4VSishSRa1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های مادریگراس اسپانیا رودخانه شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/695180" target="_blank">📅 16:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3782ee87.mp4?token=D7CwjPOXrt-M2_6_3XOCRWm1E8xwVQvhNQI_0a4VyGW6BCC3MvG0ckqRnL9r0cgBKcKtB4yfjEnI160LBihs2DJAqxGwd3RyMpd2lJ9X_09lnvloderdMESuV6oBHaPjaNcwdwHl5WWXMh7AJFJJQpyF1PkQr26VyUVPTL2P0iS1TkCa3qWoW2HqchJypOLvHy5HDg9YRrLwW7hnRwPMfeEL_MiFNTmKBS1YF1r6Qa27dnihzRFb5NWh1mjmWZ39RREbMxoQoZWPoqKAtkZJBUDU5yzHy3oI-miD9BWuLDxWKSpuki0NHgnIWDQEbGjHPMenvrQ4LzaovXuFJqMjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3782ee87.mp4?token=D7CwjPOXrt-M2_6_3XOCRWm1E8xwVQvhNQI_0a4VyGW6BCC3MvG0ckqRnL9r0cgBKcKtB4yfjEnI160LBihs2DJAqxGwd3RyMpd2lJ9X_09lnvloderdMESuV6oBHaPjaNcwdwHl5WWXMh7AJFJJQpyF1PkQr26VyUVPTL2P0iS1TkCa3qWoW2HqchJypOLvHy5HDg9YRrLwW7hnRwPMfeEL_MiFNTmKBS1YF1r6Qa27dnihzRFb5NWh1mjmWZ39RREbMxoQoZWPoqKAtkZJBUDU5yzHy3oI-miD9BWuLDxWKSpuki0NHgnIWDQEbGjHPMenvrQ4LzaovXuFJqMjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار جدی؛ زودپز را با آب سرد خنک نکنید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/695179" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFnqHTNeKqVIpwdMC_SF1GK4hcRoSMki5yOvWuU9uIrSTHVt_vlbt3EBEHhEhYIbhCHP7oeI30amiDsfr2dD-n42dbXxY8WG0OuHbd0MauiL28W6Q1Se-GV77ExLO-zk5Scjy4tO4ccYoBg6vOej_xlV8YMuxs7dhc_vfKqDlvRfGqC-REB5NV6Oy8s5dGVdrri44MS8rAN7h_d9xVPXxXCqlnV9WVgrhR3kneWgBarsEOYG7ahFJygxtReb3vRSFwXVfXx3U4ZrcVUwofooMIPgduabxrkFUu-7JX4iEnfNHoGO8q7Kp7LPlZD2YNr_N85cnOha3FDWAzauRe9WNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم چه رفتارهای اجتماعی را بیشتر می‌پسندند؟
🔸
در این نظرسنجی بیش از ۳۲ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۶، بله حدود ۲۸ و تلگرام ۱۶ درصد بوده است.
🔸
حدود ۴۰ درصد شرکت‌کنندگان رعایت قانون و بیش از ۲۳ درصد رعایت حقوق دیگران را به عنوان یک رفتار اجتماعی که تمایل دارند بیشتر در جامعه دیده شود، معرفی کرده‌اند.
🔸
رعایت قانون و حقوق دیگران می‌تواند به تقویت اعتماد متقابل، کاهش تعارضات روزمره و بهبود کیفیت روابط اجتماعی کمک کند.
@amarfact</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/695178" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTSTnwH1W8CT-pc0s7--j7-Gup_9nHq4zfocbc0or1kv8DbHwpByOelIS00qcGvv6pGUjThoLUJxEn-4sCUA6VastLZqHKQyGpDSXwAwPTzjMEg9UcbG8RgRAJi_rbxc8xK-86wAU5YXOvcNEodRXz8eUbqL7T8sXB2K0OGjqYPQy7f9GyzP2nU_UwYCJwp9Ivkn1lLVhQqxyfVu0bx9nfmKo43I642mAnVnlJRY0Uqll92xCDmsBPo-AyiTHATwA_RqvsBkt-kcqBlH1PmW6Z9B0p84LbJaa__H-i6Ykso_l0_hYDYu9MMu2YNwl7zvjxQDdMSBgU4CuHS7Ji1giQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استایل عجیب و جدید مرجانه گلچین بازیگر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/695176" target="_blank">📅 16:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUO75KmiNdvvXux18gCzpZ65WB1JqPWybvj5UDt2bBi1YtRz_48-e8KZy-6RjoiLdxdWvs30dFyy1IqBg0WejjdfyTMT_WQyFuQtlMXY-QA7oSdtDcoYzIE4A3MWu5yN4FcK8h4rtQmSTJm1FfBe_m_nZzZVUb_zJ3FRDfGQ3gQwVi6HC9WiayP28NKK6zykkieiO8FWrvdGpnGM4KeT4RYBwYCtbaJxExA_D606Ppe5UI35Fu0utwunF83ohXPYvwxm8wvlzOGrY_ubc_AbBHIWKB37rcZVgf7tzasmtXaBpGDtxD7s2BFK9LB0wEDzSsULQirA1jsKPxC0B9K5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKRojCoYUexXccg0HdkdsnrYC8qN9tHC0BcRgQ9rZSaiIhwyOkoB63eqpt0gwlu55Pj0wqW8AeUuns8Nb0Z0LD7DqDlS5ADUN121TzGiLFtE5IS7xlQh2AAFIXhzIGRAjf0_0aTeV6oF0nMAI0VpKCKM9gMFg_2QuPuvcfINnyebNNpMXL1F4Bo72UM053vn2VxOPO1NcjpgVoAjJ4CZqZ6br-rcPK02PS9VImEWjxt0bj4PWdsMKwKL-oyI8QocrN8fLy1Wztky2ka75l0VXANg9-yFpPo8Kdil9EjNzOulbA-HPX1KoGudCd9RbHnlOWKD4u5chAGwuuYdMimqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlD3bgyuOcWk-6fI_O701klNLNzE_FqIav6GIMufc8HlO4yS7brCE6Z2H3fx-oJbG22REMRRrWD_7hJsPoOafJwxDgH6tdtxtYxoI4pH43y1RqlZm3mLgXTox08Ct2IXoThErgUKNYB-nZN6Ur16o9WCL1KRoVkDpqK6oINcCeyprWB7wd5krfYNQu_zX2fGDB9bCYVH5tFycnWfoFS2WBOa2PX2-yYp036vhoDiznEEW6o1YAYAVMfZaw8RSBDSgglZUMGXSrfEQ7U1srsrXR8FRhCRb3U0Gj44KU7M3yJHJG1CincA1QRl-urLk6V7u8uzfD-1HGmVfVnSUOOs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS1_-jIEtWi9JgOQxxWSQlpHQGvsu13kBks5_f1Z-GYxRf2d4sI_s3h63okOBac9LdgRpB3tQqPVFupEXrjpSp8mbI1w96qRi5C1YMMqeU2g76VXNmZqoa13KqRb0HDAeILnGRgrllOfgTkDzQVLrVT2ItL6MekDxPK49lNJFlxOjUWb1eWR14rraEABu0wfNDASxf7vgb_m6Cl_cQPzx8W5OaubHkkR7zl4qouk9DwTq6jM-1dLKEBf5gpYolMVlGopaDHBEUdK0_xW_t7f4NhMwgCC2vKoPxBj2WtKunEv67ncdRCnWjfM0jrfZs0GYUGJ8wu0D6HIj-xHisSpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uI__oWPrH2oKJroNkCThkfKmaObEao5Gv4B2-2E7Sg9OvQGxjNJlWNrgTUdxTXb2RMaIOGr0nZeyVq2hAWYObL_YgwYTxcScFiKjc09DPQBc8Ju_gSgJk4HHtkSpCEbamCq8D-1CEoUKwX7XenqkfrWmb2xDVrIQoj6xgX_3-s-hYvRsEKLp2kX5UIPXFPh0k0wQUkgkCnZnk5TliVLCZKUGNefzMIAZY0sFJ8sVAJ7kre2W1PfyGyG9Txoo4rd7vn__DvzvHqSOei2UiyYXZLVRl72Zgcknncp65je6FrsWBo_qYJ-Lk491JRWWUmXlRi5SsaZZq3luQHudBMC_IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از خرید میوه، این نکات رو ببینید؛ انتخاب بهتر، خرید بهتر!
🍎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/695171" target="_blank">📅 16:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش قیمت ۲۰۰ درصدی ترند این روزهای اینستاگرام، ۵ شاخه لیلیوم نزدیک به ۵ میلیون تومان!
اکبر شاهرخی، بازرس هیئت‌مدیره اتحادیه گلفروشان در
#گفتگو
با خبرفوری:
🔹
بازار گل با کاهش ۳۰ تا ۴۰ درصدی مواجه شده و گل از سبد خرید خانوار حذف شده است.
🔹
محاصره دریایی و هوایی موجب افزایش قیمت پیاز گل شده و گل‌های وارداتی نیز تحت تأثیر افزایش قیمت دلار، گران شده‌اند، اما گل‌های داخلی افزایش قیمت چندانی نداشته‌اند.
🔹
قیمت ۵ شاخه لیلیوم از ۵۰۰ هزار تومان به ۴.۵ میلیون تومان رسیده و قیمت لیلیوم و ارکیده حدود ۲۰۰ درصد افزایش یافته است.
🔹
از ابتدای سال، قیمت اسفنج گل‌آرایی حدود ۳ برابر و قیمت کاغذ تزئینی گل و ربان ۱۰۰ درصد افزایش یافته است.
🔹
قیمت هر برگ کاغذ تزئینی از ۷ تا ۸ هزار تومان به ۲۵ هزار تومان و قیمت باکس گل نیز حدود ۱۰۰ تا ۱۵۰ درصد افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/695170" target="_blank">📅 16:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695169">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f512f4a2d.mp4?token=BSQAHrmG2g65bvOyske7JZJQ2OL7GSHsHVeicGSoNdIjiBcfXeUMsI6UW9yleyUX8mqHC-zW99KNcH36SdnxgjEml4i5nz6GNED_lVptsBodj7Q5AAwkrE5ixIRpy6XhMBv8wbGuxT6r_MSnOUfB7_pInsSLrFqUNAh602U4dxKSlvQDOesEOpGZqnhkAe7DLLuguJTlz6DWCo3TmssQliZ9MSHlFKeCE2HRiF8LCbBKW7N21kwamdRZCNmNPuAv-TsmGduMkuzXQWkP3qNRTV9dpss6fByp6aopvoVjj4mWbBfABgEV5Paj4vXyJTnKxI1UeVx7IB0DTTs36RnnAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f512f4a2d.mp4?token=BSQAHrmG2g65bvOyske7JZJQ2OL7GSHsHVeicGSoNdIjiBcfXeUMsI6UW9yleyUX8mqHC-zW99KNcH36SdnxgjEml4i5nz6GNED_lVptsBodj7Q5AAwkrE5ixIRpy6XhMBv8wbGuxT6r_MSnOUfB7_pInsSLrFqUNAh602U4dxKSlvQDOesEOpGZqnhkAe7DLLuguJTlz6DWCo3TmssQliZ9MSHlFKeCE2HRiF8LCbBKW7N21kwamdRZCNmNPuAv-TsmGduMkuzXQWkP3qNRTV9dpss6fByp6aopvoVjj4mWbBfABgEV5Paj4vXyJTnKxI1UeVx7IB0DTTs36RnnAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: ایران این هفته نفتی برای فروش نخواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/695169" target="_blank">📅 16:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695168">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYDA_2hEgV92MvVi8c8cZyhTB4vEe1jBGwx-XRU4L8m5Wi9Ys_AVdiNuEJpL4vazgvw5eDPpcxXr7g59RD0boKU9dzrMIn5RMiNoCXOoijPia_Eh-deUd8exOzWkP62_1GOHbuC2wdAOoiXjCLG9gTGtPPpVez_O9RUk5y5hDuWHcrYW12VaOcreLq0QX74NHGrfC4-B5iFfQR9dBnvwi0i4RqLnNVm09RzXiTD8QSESnp_TTq6ydYsY_4x-nMiNY6jFkhQ_poNjV8vfeUEAvUZk0qOQkr9KBOrimLwWW9ERT7V1f8VC7xZaFNuwDiZpdosd1o309-jTPgZvzRoCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کهن‌ترین درخت گردوی ایران ثبت ملی شد
مدیرکل میراث فرهنگی لرستان:
🔹
کهن‌ترین درخت گردوی کشور با قدمتی حدود هزار سال در منطقه کهمان شهرستان سلسله لرستان، در فهرست میراث طبیعی ملی ثبت شد.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/695168" target="_blank">📅 15:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695167">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرفوری
pinned «
♦️
فوری/ نتایج کنکور ۱۴۰۵ اعلام شد
🇮🇷
✊
@AkhbareFori | Link
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/695167" target="_blank">📅 15:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695166">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbYor4fV6uEFPMjBs7-To0NYcWvfAbw-Gfsc38C34Jz3BxO5N4uYHKW2kmmhaleBRSfIYFyzPCAwwaH05CCCTuxg9iWSyAq2reD_0lUyy0N8DNBxUMqNhxQvRUjoeSFja3n0AIMhgoPInaecDQS57ysmcuAqxCgg4lKIgu6rMoqoWH_O57s8_27IUV7_MxDzY_MlD9bTxSId1Bip0-eds6EpuSAtjdzJGP-m2NCc8dC2EiPoSE2P_xrEGgVxn-dV19IezRuh7vOwQT5C9kuTKAD5BqBpT2cx9K0sBI-I8wAUfeF1ADF0W8nuYW29WjfVC0pRom1J0oTgvkkGm0puyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر جدید از تداوم آتش سوزی در پالایشگاه «آرامکو» در ریاض
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/695166" target="_blank">📅 15:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695162">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcLydsBVFWDDZ5RiZhkVKhnmdS2zqyOIXXZvITybpbqoJPO8GE7A1AcsdcFbQYbLmLwID7DMMJYRjfRCRWwacto0NhL6Zls6hQ3Lm13UaOQMdWefOUA2aQMmLrwHRp2uHgRiy20eNVeQpN5fs1b3qHFXtX8z0_I9LhVHrq0A7ytNsa67jIp4lXFvqQfg1W8Jv0_I4gEli1v-P5NVJkvlmiKs_z9CQvt7BLVMVOznASFI4gfZBt1lRvQBsOvkzYwIrhQocGM10UJ-veFaYfx4VZjjRAOCsYiFdIMSL5Tz-i1Lz2mqXOkXO1_fB0iHSg8DGoKhvI7QXVhuMTvCxyIozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEQe2eesYxFhTOgbFPPmxeicfWHjpkDEtkB2gTSDq6KBgHrSsf-vQgWOxOuzsI9ZVu3waKXHfAQLIPqLp8Sof-VTyXcS-slWtE2_lqhY78rYtVHt74yDyedPqsgjPYj9EA4aojHrwTcirSlmiXT68pzhH0TZk8XTmafUQwq-l7S1Y-MimKqq5IE6Ac7zzRdCng78wagIIc-ALS11UGhZFMIx4hnmVoTHQBa92UQkuHNBAo_mF4so4mMYlLNpWoPffX26ZvE-FRss8YWyUabtlCg4Em-nuz8JOAQ-voNEaObKzYDJ9g9Ibra61D2_a61uU5Z_05C5jzP71CENe5XeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akG1tuyBtK6zpYPSSDsYNB6869s_Fq_vft7R1K3LlvKD-bceQHpDUoYsjN6FZMQ-wVzbE9891O7des6uZ5bIok42-W4t-o0t2o2w1VksPXqWT2kEhBnPoWVAH7i1oLfTjva2uyY_X_ipRwJk9LypE410R3_NKgQSQ5cCPad8TzkN1lDHaJrl8wcjHZ0dyJ_Va__af_FY54a5dfs1zoe2nzejdlYkanlX2uOV8izgmDiTf9OJyc_tS1UtPbzVVF_IXr8sr-930qixefWNDf3iaPgrAEQ1feUTA71_C0FAa2rF8LD0YlQq_vryjbQtLJ46RMfug8KYe5V2LYQ4fVBGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFDqE0hAyg7FU1tY0n3dHPj73uP-Y9XZlUdQ7o7H4D5_Y_WHxjAi01XKtoTuvFOab-U2LDMmSyua6pQnw4FRRa-txA3rGLWhMhG8NgD4BNwQlLahiK9e7fDVByPeQoEwEXjsPkkt0h99JtGFaPXuRvAwId8NSymfO5yRV1Xf0nmldg0Q1c1BYZ9NNk5dolS0mX_uGROm3aid_2HWreiJ39buWjaUrYw90yB3DLy7X0FgvnoJRB-XuUjQg3_3ZwMV4S95WTrjQzsncIV15I1ysJYw16qLGN2S6U62uhAKs89aNUDO4Focj4GOp4pH-gXqH8mm8qJjbTKxJRVsTmRdYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پایان موفق پروژه «پل چارگون» با ۴۳ تیم
🔹
پروژه پل چارگون با مشارکت ۴۳ تیم و ترکیبی از تخصص‌های مختلف برای بازنگری در محصولات و فرایندهای سازمانی به ایستگاه پایانی مرحله حضوری رسید.
🔹
این رویداد فراتر از هوش مصنوعی، بر تقویت آینده‌نگری سازمانی و هم‌افزایی تخصص‌ها تمرکز داشت و ایده‌ها در قالب‌هایی نظیر مدل کسب‌وکار و نمونه اولیه (PoC) ارائه شدند.
🔹
شاهین طبری، رئیس هیئت‌مدیره گفت هدفشان صرفا پیدا کردن یک ایده طلایی نبوده و به دنبال تمرین کردن توان دیدن آینده و همکاری در سراسر سازمان بوده‌اند.
🔹
‌این پروژه همچنان ادامه دارد؛ تیم‌های منتخب ۶۰ تا ۷۰ روز فرصت دارند تا دستاوردهای خود را تکمیل و در روز نمایش پل عرضه کنند.
مشروح خبر در لینک زیر
👇
khabarfoori.com/fa/tiny/news-3249563
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/695162" target="_blank">📅 15:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695161">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b29b502f2.mp4?token=T4AFYJJvcHgPjxFLCA1A2yj3B1PsqlQd56R7HuoiqQlofemjyEdp1lnCe4QU85vxEDHZguWpysSBmizqwKX568TVniWaILh2l0F2kcQNENzJGcEvyTlDs_fwqbIE6F4Wc0CSAiJkmjfK52ll4E8DKzN8DSRgtzcLpLlFaAOisBVQ2FQFOvn8zJ3F9yPcsdJWEfAtjnNXZZ1vraDaI8oswYHK7mCGQmwZ6ywtQHijJObcjny873RyjsBnZjNAdn9IuQtIixc9-8wmjyGTSTCpWK9PG_ATVqBs-i5jrGjGy8aWp5ZiDugAWiVSPQOyVK8BU7rkfwXGt3b-kYtnY-wVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b29b502f2.mp4?token=T4AFYJJvcHgPjxFLCA1A2yj3B1PsqlQd56R7HuoiqQlofemjyEdp1lnCe4QU85vxEDHZguWpysSBmizqwKX568TVniWaILh2l0F2kcQNENzJGcEvyTlDs_fwqbIE6F4Wc0CSAiJkmjfK52ll4E8DKzN8DSRgtzcLpLlFaAOisBVQ2FQFOvn8zJ3F9yPcsdJWEfAtjnNXZZ1vraDaI8oswYHK7mCGQmwZ6ywtQHijJObcjny873RyjsBnZjNAdn9IuQtIixc9-8wmjyGTSTCpWK9PG_ATVqBs-i5jrGjGy8aWp5ZiDugAWiVSPQOyVK8BU7rkfwXGt3b-kYtnY-wVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جالبی از شباهت شگفت‌انگیز طبیعت با اجزای بدن انسان؛ گویی طبیعت آینه‌ ماست
🌿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/695161" target="_blank">📅 15:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695156">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
فوری/ نتایج کنکور ۱۴۰۵ اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/695156" target="_blank">📅 15:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JobJ8z1NR3gKtTlx4-A6rCWR_6EhKrispB0v7WhRobuJEjyu5jBlnNHk5THo_ODzl0mJZ14lTOLIjJlBelEcZ1p_T8Z_1Q6SrOALJHH0hro4O5yK6VgK1Ai9vg2vOKLK9CgY6j7UUSeZyI0az9xuOaSWyJmVkCZtsXDpXUcbIGiUya5wujJoA2G0iphu9eBpebZ3DbkH9lX1-sYNMeHHAEz38aPN9IqRgw7IUjlvi0CgRi518EKmvvtJTvIA2Bo77OmEmkYk2X65toWBe_mgCRnLWyfg8N6cgPmu7jPO8WDuMmNePpmeCFzfEM-8y3ejP8UoHHl94oul0QEtWgFMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWkC3PGr34j0WCP-YqooE7NEFlSDl0xKBRkMOsvshUdwPe6LGuYzSXOLqNxjNNKTh9XZ7ycXJagt9nksEbZqIT7LmAX-7khQSVqS-mp_HyiAJuEhUN7GpyjF0Ul1xFAjtmtErhmDNEz0E7C2K0PCtgmmkyoO1BEZ8JlLr1cPmE-mQDbGokJcjEoo3BzOl0a9QH25PtrZYT3MjIrVhnGHXuFpV4hIUp0arrSB8z0LEJ-gRXeODaQl8-xY_g8PcbisVSV7nJgh2i-JGB4kMSzc3XW5CACNEU7D77BCEFvneX_WRQ1AiKqdBDl0jESvZgglyO1xnkK8kqaCHv934-5EMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bo2hoRzYn04gYIhdCLf5XiqIIGDyQ-i5AqPip8NH1BqQqmKmU5y7jX7g1L2uzcGplTZ4qwcftVGD1-OuIr_yKEuqJeJ_DzwZ2KopNDolWEKWLAIRdNH9lts2AVozeAXc41TdGt2VUKCSoP6IfXmzeNOzBj7kICFKUSt3xP6hBYQk3rZOQ4f5Fbq_KHdTZu-RDVdidd8y8nlDbgRBszvVyYUpXbo0djusnHD0TnVP2-p7idljf9E5nPZiEgpUH4lzg9Q9jwjsnolkDEPyIIXKK_t7LK5c06ke7ELzvK9DknO8_aXXL-v5jH_94dGWuJebTH7OSrq1LVjnQ2ECh5Wupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpYxlidK0DjAAMAc8KATiSLBiikutKOX0WfXNwei-MJOkrZweNQR_7P3YQApn5Gb1qF5dvL_faUGXS8s-REDQjDlR1PtXqV1I2V16yPn1a8MNgd2iAOZrrqWITEXzfzXMvw06qkYx9pUSVBbvc6NguBs-DLFrt4b7Bfkk572_hZAwa-bSstSohq8Fx4D3pifn3qiIlb-KkXIsvovbV9qCy3Qr8phsqHs9xmPli1NVYt_FAzR_ccS_VmaIONdTFpr5bMvbcQFEExy3QzX-f7McC9gheqkY__g0dKX2wVqPchHzsASmdX39W0hoglFbOt_CL_uRh5UdZCOYf1J1Fc4Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نرخ کارمزدهای بانکی در سال ۱۴۰۵
🔹
از انتقال وجه و خدمات کارت تا پیامک تراکنش و اعلام مانده کارت؛ نرخ هر کارمزد چقدر است؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/695152" target="_blank">📅 15:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7ArkEB9RadcQ3n27rdarP8Sh2Mn-Ti_-j6wOdJBrNccwTCNB5i2iolnVMIpg0qomVueUGibWQxryWfdaGI3Y6PAVSrZE-NNMmB7kfgCojcmlVUHddeU0sBNefjSHkUSDWhrVkxvgTwdgmxTNpafIYVsa_CmtUdMJRX9h8j4-4DJvVKmnBBmoXWQZmYlH_8_FB7v1_Sx9g0oSouMgT0QaU6CWpve38-U65pHdBA_rJryLElq-QBtKAQETr6EAwngHmIEdD9TSQ67NtpkhRYanM3C-i-TKC9AoxRb8Ltaqg8zOgOxJe7NihNVV_Qs8QNwcOmK42nDy72pasHf7n6Sgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smXYFoavvw_xYM64S-wjDGpFqG8Ew-wmVRmxgHJ2_ezoLbIab3jq46YNNV8z02SO21Y84uAhYSIufMSgcnSU683MlAMeH21WlnOe6ABiSMq0_XZLvNxi0764Bu2crjfdhdv9JEh0mhrFkcgmWfyP7tjX1PthK2x8LnK3Oyek4kIw6f42EVJBoh6UhbCKZ-vG8UggPkhySTx0kvj0Og6CFSUaJX-FZGqYdmF9qA56JASoJ2x_p_9wVDURFUo1tDn9_iKUi8POMt9K7g07qh2LiLZHJQ0rcvn0LdDoqrx8UXTR-yWJr6w4KOfg2HDra87UP68h7P0RExhzJg1fIUi0kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مکلمور، خواننده آمریکایی و برنده گرمی، پس از کنار گذاشته‌شدن از تور اد شیرن به دلیل حمایت از فلسطین، تور اروپایی خود با عنوان «موسیقی مقاومت» را برگزار کرد؛ تمامی بلیت‌ها در ساعات اولیه به فروش رفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695150" target="_blank">📅 15:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQsS8ftDogb0zxwDvm7BIogrnhAKux4l_B54wocSL7-o0FrSgnn_pZsmJlOC0HAZtc3CxlLExgYnpnRAfcBnUuYtxmQYOB8JhKiigY8yDJMfSHMM8CAW_UFXmqDXmwrRCczsBJ86xaU6cmICYYxOEin_xy8vTz_sqRscshXTBqwXaryQXAH2WxO3sFFBiyBSR28cxD4kXLbHmkD8KOGwZ0O9klPpZE_0kk2bMVvDYBfGY_P7KUEsQw7uwAp6jwCMnp_EM_fgFa-c-h48bGGTpY4MOz3VTu1D2O6CbmptEvalJ2XRnf-jAEA89-DfcCHxtVzLKo49NvrU3VkIlo8WSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشکان کریمی، رتبه یک کنکور ریاضی ۱۴۰۵؛ مادر و پدرش، هر دو پزشک هستند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/695149" target="_blank">📅 15:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695147">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/di_SRZSKlY3-iuxI4xXibyT8654w2dVU63akbTIyXID9PakjGS4yZ-nK_yRwInLmOlUUsgncDz8mnLE09IWye1MZIsAKiwUTWfGvvBGmx-4VZ41QiVgLXKNXSzKuzL1HOQU-Ag1Wr3jXdxPPCVVoohtDjAXzJlacXvDrWSqsr5vab_5l9OqpQW0CJJiaAXIPK8VZgAQjdB4pTowR1kjgwNpcwNi-TMaCf9iqoGjWGZX27XFg2lmQVrL9k51sLOD6BvZQUc0c8kPGYRjfk8RJxeH9mgO3QPQE9dddz79M_LPCdHDI_JvIj1_DVTLpnKrFMygi5oSBwSebPtddVXU3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOLzdOHkqVDJLcx_HE-GGxE9yypJQZPDERJ4BG6l31ndHLa1ECbKzOarufpKBHmd27YhoGGcGvkctOeDo-hePkHz-MeFafTSBpNKBGgslh5ZawDDexve-xv3inilCQ2bSyNcegC4QDvesm56B-wO9I4i8za8jVkA87285IyghefiPJA7jQ1OaGxnqfmuBTt238lyvPQxr0mceT1ZNBwxKu6NqjK3gqEZrHdzKh2BO8YOu8VgY4VH7rVGwBzFnDYIIxP16vvk2h00VdmbPVFCQnWiMpjcZ4e6KscMKsLPhCseZpmDrWiciB4tKJw5uXCt27p9qXyQcy5POhg7BmF3_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نامه مدیران عامل شرکت‌های هواپیمایی به رئیس‌جمهور
🔹
در این نامه، مدیران عامل برخی از ایرلاین‌ها ازجمله زاگرس، چابهار، کیش‌ایر، ایران ایرتور و آتا، ضمن اظهار گلایه درباره اقدام اخیر سازمان هواپیمایی کشوری در ممنوعیت پرواز برخی از هواپیماهای MD، نسبت به پیامدهای این تصمیم برای صنعت هوانوردی هشدار داده‌اند.
🔹
کاهش پروازها، افزایش قیمت بلیط، فشار مضاعف بر ایرلاین‌ها و تهدید اشتغال و معیشت خانوارهای مشاغل وابسته به صنعت هوانوردی ازجمله مواردی‌است که در این نامه به آن اشاره شده است.
🔹
طبق آمار غیررسمی بر اثر پیامدهای ناشی از این تصمیم، موقعیت شغلی بیش از ۶ هزار نفر بصورت مستقیم تحت‌الشعاع قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695147" target="_blank">📅 15:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99155c9708.mp4?token=Gsdc0_YPB8YsQ2ZrA5XnVj6gUNjRZs5oRmzVvoMlGzYHhtEFcyhf5BnG8rceEoHbAb3tO4bs5XCHr6Wh7bbU8d35ekiEN9-PhpOfr2g5tURBpJgyJCR3IkG86QhLgs0mZaQ6zvLdMPuOC51cS0xSrTrOC8jkALkivHAb7T8xSYG1krnTXYXFVs8jIG106txwoPszEHOvG5gYGZhB3C9FfVXUHX4uIZVwclFp9njKVp54KqS3nmlZYzSoWuro2hyyBCtzXgU5_r9Q9TLjVF8u4TK3leZASAJHQqts4tB2g1Ah9YKFdCl5-Z0o_1U8pvxNNitBDKYVjH4TKbQpW1vLZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99155c9708.mp4?token=Gsdc0_YPB8YsQ2ZrA5XnVj6gUNjRZs5oRmzVvoMlGzYHhtEFcyhf5BnG8rceEoHbAb3tO4bs5XCHr6Wh7bbU8d35ekiEN9-PhpOfr2g5tURBpJgyJCR3IkG86QhLgs0mZaQ6zvLdMPuOC51cS0xSrTrOC8jkALkivHAb7T8xSYG1krnTXYXFVs8jIG106txwoPszEHOvG5gYGZhB3C9FfVXUHX4uIZVwclFp9njKVp54KqS3nmlZYzSoWuro2hyyBCtzXgU5_r9Q9TLjVF8u4TK3leZASAJHQqts4tB2g1Ah9YKFdCl5-Z0o_1U8pvxNNitBDKYVjH4TKbQpW1vLZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون، سیلاب شدید در اوز ؛جنوب استان فارس
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/695144" target="_blank">📅 15:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای جدید ترامپ: به نظر می‌رسد ایران در حادثه فرفورد دخیل بوده است
🔹
ترامپ: ممکن است از اروپایی‌ها بخواهم ذخایر اضطراری گازوئیل خود را آزاد کنند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/695143" target="_blank">📅 15:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695139">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LisVHhjHey6HQLflLl92B-gnMN7JMud9NBNItc-Zcv7X-_zlUUrK7pazhY2CN5SF8PP8mnReD59JcaT_g7WzEfMzfTp1XWqF0ltJY_1B5LeLKWwPXIcBpldHdJesQ0twC_Je13xwYWuWe3f_UdUT0eZDx7A-yO6KVOC4bUEC-1BESTP5Ky6NCIWZX9-bdLA_fvVtbI74Oi6u_-aIrCa6hbcCY1oTFTveJdRhCkBA52L5CgK2LAQm-nBx-QCgu7W3RMrSWysiS7JM6eIxe0Ue-4PnbDbqw6WaCWYP3VrTWfwNhe0a-fglA66vzgGAXWMSSTuq5mXSa6hHdLHR9gZJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/go_0ROyFpEf5iBervbKm9T-EWV3MH5V5qpuyGk08G0vtt_473-pWWnfXWDGPJYTS3ufzRRs_EblrK_kNeanhDDP3ZTbBNN83k_JgimABhdFmmXkxxiD9e4eVkOph76hhfiI01dHlNmCGfX5M2UFtDuZL3e-OE-dtftRLz_qhJoCvN66_yQNm-D5thtZ5pzuV01XMWGVp7sSKywCBHlNmPxBkTP_gILoNOD3QWI-7gk-EXaybhZEkhXoUkgOjhiHrhVlsyhLPNwfbK76eV6cSwqz6Lkr0SNzlItYPSfgQcRZGDffRZq6zICWivKXh3xzE7QXCRSqC1E9myzPjqv7XXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wdk32eSZ7IkUWZ8C7kXDn-fg0BUuepxZy9T_rWaz7E9-1dmGjcjZZ9Z-ltHahIbic0-o_VVf44BD_YrOdXpK1uPFDuad89HrATODTt0f5bgfZg2K7NX89DiODkmVtOngbKgvi9BN4fuYPO6C8Bp0D5N677GhnxF-mmaRgiKIrPJ40SPWos2buomGqHeFX6iQIRmf6cySgxDx2eN2aZRHUgNGpeMCJcJ69cR4FijGoM75P5gPGlVYMCWa8xMu8qxXPPhvf4_0cqOUNAUmIfkCxtP2G0lni0k-KbGX2dg14jp08aWokX0AJavZFtR97kuwvro0CcpgR364HWvABWuS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBK2qFGUyzo1cQfkmK_DDtnb0pj5D_uZVDZQTMJNMLDaZU2Q8XVkCS7AtJmwen1G0YPV2BP3zZuH-J1V65FJy3I8UiIQl0fHch2Jem6aQUiCF8kh2q7T2ogtjWhye7Vth1n0lEtF7bikxqeBZ8pRs69mj27Bzn2ZOHsKPXApMiXXYHY8Y9y8LHnNCypkazBCaPEoJpcHVxDV_b_T1B8r35yaaVAdazAF01Flnc-uzfntcpnpY0OXcCZs36kbO56lKf-ViWDj17qTEkjdul-adKM6SuriojhEWwl3utWSBSRr7xyQK_Ie7NSPFme-52k2WAQC5neXavB3SeC1Sovahg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بهترین‌های عکاسی طنز از حیات‌وحش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/695139" target="_blank">📅 15:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695138">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزرای کار و جهاد کشاورزی در صف اول استیضاح
مهرداد بائوج لاهوتی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در حال‌حاضر شرایط استیضاح وزیر کار و وزیر جهاد کشاورزی مهیاست و یکی از  علت‌های استیضاح این دو وزیر، عملکرد ضعیف آن‌ها در ایام جنگ است.
🔹
خبر استیضاح وزیر ورزش نیز مطرح شده، اما فعلاً اقبال بیشتری برای استیضاح وزیر کار و وزیر جهاد کشاورزی وجود دارد.
🔹
استیضاح وزیر نیرو از سال گذشته مطرح بود، اما هیئت رئیسه هنوز آن را اعلام وصول نکرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695138" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695137">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نرخ اجاره‌ مسکن استیجاری برای دهک‌ یک تا ۶ اعلام شد
معاون مسکن و ساختمان وزیر راه:
🔹
در طرح مسکن استیجاری، اجاره‌بها بر اساس درصدی از نرخ کارشناسی روز تعیین می‌شود؛ دهک‌های ۱ و ۲: ۳۵٪، دهک‌های ۳ و ۴: ۴۵٪ و دهک‌های ۵ و ۶: ۵۵٪
🔹
قراردادها ۵ ساله است و شرایط مستأجران سالانه بررسی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695137" target="_blank">📅 15:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695136">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed0a925d5.mp4?token=KE_XlTCsGLWqjvBuBLzkILO8fsMUKOe5HBSsjQ8vs7r7NoC2zVITkctjhAz7IsjyeuTnVIQitmVcM0U9Vx3Hg0PSX7_bKnAyLIQVTE6VtfzJQ3_O8Whg_FDBvMnjAwogtQo0lR_PypMW53i-bMpa_dksUuhccXOf2SMVFz2_KsYjV7gwAVrKomIWSJd3XVUyplMMCCOiH9TX-yuRy81ofUe-VRuyuC1Hlq_BvzmPUjxQG9ty_ONUjcaDff2bflDziD40ytIyMJT6N2cpst9DVEreb3HlHgyI2yCEhFNrC7iXGQAhgqWvuhMMhgyoPy1lKxF7K-SKxcqwdTwekhp4Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed0a925d5.mp4?token=KE_XlTCsGLWqjvBuBLzkILO8fsMUKOe5HBSsjQ8vs7r7NoC2zVITkctjhAz7IsjyeuTnVIQitmVcM0U9Vx3Hg0PSX7_bKnAyLIQVTE6VtfzJQ3_O8Whg_FDBvMnjAwogtQo0lR_PypMW53i-bMpa_dksUuhccXOf2SMVFz2_KsYjV7gwAVrKomIWSJd3XVUyplMMCCOiH9TX-yuRy81ofUe-VRuyuC1Hlq_BvzmPUjxQG9ty_ONUjcaDff2bflDziD40ytIyMJT6N2cpst9DVEreb3HlHgyI2yCEhFNrC7iXGQAhgqWvuhMMhgyoPy1lKxF7K-SKxcqwdTwekhp4Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالن ۱۲ هزار نفری آزادی؛ حدود ۶ ماه پس از حمله، همچنان عملیات آواربرداری آغاز نشده است
🔹
ادعای حضور نیروهای امنیتی در این محل، با وضعیت فعلی سالن در تعارض است و این پرسش را مطرح می‌کند که هدف از حمله، تخریب زیرساخت ورزشی کشور بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/695136" target="_blank">📅 15:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695135">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156650fa8d.mp4?token=RfZYq5MCOdHR7Au1YcRAyKAL7IC4SuAo-qMIxkJarnzAmTOAOrczhrI1Uo31kIbCX2bS-1Ipd-OCIEDwJbgQkUu_1UjnzZlumhhvs8yvghHC-09ZQX_u6gntX4H4Q8193-XQap7OdQoP7uiTs6wJ4BW75q187mHqT1jFz539A9L6L1ASBr35Y45RjIDLclUkDrken91ZO82f0hA4dUGNbJVycfixs3CCjTcZBQcm4gbptHwXjDCbRO64sBqzRptFmdAFt-VzHplRP5BtTX7p7-421zpWk_QwNRpYOQ6RNfrKFL7FdqaTXE6ZjudXII0g6ei3ABhZwVg7KzRZ8KPkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156650fa8d.mp4?token=RfZYq5MCOdHR7Au1YcRAyKAL7IC4SuAo-qMIxkJarnzAmTOAOrczhrI1Uo31kIbCX2bS-1Ipd-OCIEDwJbgQkUu_1UjnzZlumhhvs8yvghHC-09ZQX_u6gntX4H4Q8193-XQap7OdQoP7uiTs6wJ4BW75q187mHqT1jFz539A9L6L1ASBr35Y45RjIDLclUkDrken91ZO82f0hA4dUGNbJVycfixs3CCjTcZBQcm4gbptHwXjDCbRO64sBqzRptFmdAFt-VzHplRP5BtTX7p7-421zpWk_QwNRpYOQ6RNfrKFL7FdqaTXE6ZjudXII0g6ei3ABhZwVg7KzRZ8KPkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برس‌های کنار پله برقی واقعا برای تمیز کردن کفشه؟ #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/695135" target="_blank">📅 15:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695134">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74b3a8c5e.mp4?token=vX46PCwMmjTVYH9ddbe72LyV1J3Dk_TJHsRKl1uEGuNgXjkEXRcH3n5zyfwx5Aazo3YHEVv4p1vP1vO8j7SUv7zf2X_pYOP_ApZDAs1_xEdVbU58spF8v3jgAjlWHrJtxif1fxIqsMxyDmzddTuoyr-HJnDS0DMcC_Y5nfLAbvUuBQwECsD1JW6hdtpRSaujRfpTYP87_IqEp8Rvu4XC9R4CbhBT5sLQGydhiav9qGlPcjdPc8LtE12XGfIY3xI9bs1vUJNlLIrkup2yr2edaVfQ3RWUET0lx3oda1a8WK9SoVccgvbctIJOjKdRX3KINQ5t1x2h8Sa2pHIehSdvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74b3a8c5e.mp4?token=vX46PCwMmjTVYH9ddbe72LyV1J3Dk_TJHsRKl1uEGuNgXjkEXRcH3n5zyfwx5Aazo3YHEVv4p1vP1vO8j7SUv7zf2X_pYOP_ApZDAs1_xEdVbU58spF8v3jgAjlWHrJtxif1fxIqsMxyDmzddTuoyr-HJnDS0DMcC_Y5nfLAbvUuBQwECsD1JW6hdtpRSaujRfpTYP87_IqEp8Rvu4XC9R4CbhBT5sLQGydhiav9qGlPcjdPc8LtE12XGfIY3xI9bs1vUJNlLIrkup2yr2edaVfQ3RWUET0lx3oda1a8WK9SoVccgvbctIJOjKdRX3KINQ5t1x2h8Sa2pHIehSdvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میکروفون باز، کار دست گزارشگر داد
🔹
بعد از پیروزی امیرعلی آذرپیرا مقابل آرش یوشیدا، صحبت‌های پشت صحنه و خارج از گزارش روی آنتن زنده، یک حاشیه بزرگ برای کشتی ایران ساخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/695134" target="_blank">📅 14:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695133">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc9614cf2.mp4?token=DbLfkSrxKWX5Gmy1FBp8Ll7WB0dLFCEi-HZUBkcV4cFc5_QvJOS2fvO7DqjDP3O1a8qtLY4gcv_JNU7SJsjVIw7VUEl2AGbKIrakcREaHkgL7pNJo4dZQbfQ-M387NA0-ywYCUMJ_Rigps1I5AmxvUjvmrd9cBhfsUVHWUmwXTEfJ_qz6mom2fBQ8SQuF7FvZ2U00GYrYOihHPyUqnABRvszVwdMFKWh4kmXLRMP954RzGLlkMRgD0-0j1a-nH8LQwaVabS8egJXR9wpOLNF8F82kqxLEB-Gau30L11nKgT2uw1_rdDb2ruA9aGHthb-cROU8O4LlTcyoGl-ftWx1BthhiROeAyFMtWhjrNU_Co6lFfQTUKOnQsyleM5pXR_dKm-3H09aqjLMZsICrX32OsMiM6VBDkEk_9y4WZrvb3gSKoDTNGSEeOwtv2kYfsL4gYL0AGy86ZlwRAbv-IJFNNUYAdYDgu7U4yxX4w2Jha2qIcrYuK_SJUn2nHTpythyKxRQTRq9BuMcvzv8yNHqcvr7Le42UX32xsLb3kn7lirvSDI4Hh9FEGXgsVsoG2XIrtFOvGMzM9xj_Hvl5JyZe5Ouj5BcHuzSfHz9JOZeYx6sq-rX56BPI4pVYsF1WtQQw_jTvSP-LJALkzQ9ZLhummV_KCyhL-C_uQML40gDqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc9614cf2.mp4?token=DbLfkSrxKWX5Gmy1FBp8Ll7WB0dLFCEi-HZUBkcV4cFc5_QvJOS2fvO7DqjDP3O1a8qtLY4gcv_JNU7SJsjVIw7VUEl2AGbKIrakcREaHkgL7pNJo4dZQbfQ-M387NA0-ywYCUMJ_Rigps1I5AmxvUjvmrd9cBhfsUVHWUmwXTEfJ_qz6mom2fBQ8SQuF7FvZ2U00GYrYOihHPyUqnABRvszVwdMFKWh4kmXLRMP954RzGLlkMRgD0-0j1a-nH8LQwaVabS8egJXR9wpOLNF8F82kqxLEB-Gau30L11nKgT2uw1_rdDb2ruA9aGHthb-cROU8O4LlTcyoGl-ftWx1BthhiROeAyFMtWhjrNU_Co6lFfQTUKOnQsyleM5pXR_dKm-3H09aqjLMZsICrX32OsMiM6VBDkEk_9y4WZrvb3gSKoDTNGSEeOwtv2kYfsL4gYL0AGy86ZlwRAbv-IJFNNUYAdYDgu7U4yxX4w2Jha2qIcrYuK_SJUn2nHTpythyKxRQTRq9BuMcvzv8yNHqcvr7Le42UX32xsLb3kn7lirvSDI4Hh9FEGXgsVsoG2XIrtFOvGMzM9xj_Hvl5JyZe5Ouj5BcHuzSfHz9JOZeYx6sq-rX56BPI4pVYsF1WtQQw_jTvSP-LJALkzQ9ZLhummV_KCyhL-C_uQML40gDqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا نگه‌داشتن پول در اقتصاد تورمی خطرناک است؟
🔹
اگر ۱۰۰ میلیون تومان داشته‌باشید و تا یک سال بعد به آن دست نزنید، فکر می‌کنید تا یک سال بعد هنوز همان ۱۰۰ میلیون تومان رو دارید؟
🔹
پاسخ را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/695133" target="_blank">📅 14:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695132">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
رویترز با استناد به گزارشی از نیویورک‌تایمز: مذاکرات میان روسیه و آمریکا اکنون شامل یک قرارداد نفتی چندمیلیارددلاری مرتبط با دونالد ترامپ است
🔹
بر اساس این گزارش، این قرارداد نفتی مجموعه گسترده‌ای از میادین نفتی، پالایشگاه‌ها و جایگاه‌های سوخت در سراسر جهان را که متعلق به شرکت لوک‌اویل است، دربرمی‌گیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/695132" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695131">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879dc234df.mp4?token=vlFID89NQTyRPWLj_ltnWux81TNoH7m-xuwpoCEMEkwwG6Udn7SYFj0Zkbts0k4IfhC4Wwta3XM0ksiUIR2CLj2bL4vw7HtPMygBpailh3q58IkW2Nb1cRZOZulWHN6fynggpeRhCw1z1i7UzJcQciuQ7mip6va0fl6HRoAtV9X5K2koKGHSZIhj1YJqr635cqvEPZiDrEm1RXStEA93PVr-zvcsM971JR7jc-EiKtVPfcjFQGNcpvIzcHYs3f4CNMfJhoT_4eUTyHnrPYw35GsBfiqYXZTCXAjzc1yYRYNy3E1sxQ9Zgv0ObVb-Vja0sddhbJf8bu8f2gk8WFmMeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879dc234df.mp4?token=vlFID89NQTyRPWLj_ltnWux81TNoH7m-xuwpoCEMEkwwG6Udn7SYFj0Zkbts0k4IfhC4Wwta3XM0ksiUIR2CLj2bL4vw7HtPMygBpailh3q58IkW2Nb1cRZOZulWHN6fynggpeRhCw1z1i7UzJcQciuQ7mip6va0fl6HRoAtV9X5K2koKGHSZIhj1YJqr635cqvEPZiDrEm1RXStEA93PVr-zvcsM971JR7jc-EiKtVPfcjFQGNcpvIzcHYs3f4CNMfJhoT_4eUTyHnrPYw35GsBfiqYXZTCXAjzc1yYRYNy3E1sxQ9Zgv0ObVb-Vja0sddhbJf8bu8f2gk8WFmMeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هرگز به قوطی نوشیدنی لب نزنید!
🥤
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/695131" target="_blank">📅 14:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695129">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb590f9f8.mp4?token=tYp7nrqgMbaBT5r_FiLAGX4d91hA8lkB5qXxFANl4-VYVbJ3mX28Z4o92YC2WRhdjg48t0mGrlUvR1b1A0lrH-YuyWRPRkCfBGKGF-cRxSwLsIWTFukOnig49yO1sNg0lLezj8WZ2YPP5XtXzv7JvRG3qhgtXIPZToJM2iAbAtXt9SqYNjcq_GmoOxfthL_Qd2SN-DRmf8jMKE0yLnuDADeMGHbL1Az6Gt55cv5CeK2SHF-643GbNkYK80BW6kZBMDgoXTUrsby_RBa_SjDRe3zigdWWizd3z4CU9BDCk3sjMkdYbbQfG5HnnYgLHn1ILlgHPhhJRS3eoXrolHDdHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb590f9f8.mp4?token=tYp7nrqgMbaBT5r_FiLAGX4d91hA8lkB5qXxFANl4-VYVbJ3mX28Z4o92YC2WRhdjg48t0mGrlUvR1b1A0lrH-YuyWRPRkCfBGKGF-cRxSwLsIWTFukOnig49yO1sNg0lLezj8WZ2YPP5XtXzv7JvRG3qhgtXIPZToJM2iAbAtXt9SqYNjcq_GmoOxfthL_Qd2SN-DRmf8jMKE0yLnuDADeMGHbL1Az6Gt55cv5CeK2SHF-643GbNkYK80BW6kZBMDgoXTUrsby_RBa_SjDRe3zigdWWizd3z4CU9BDCk3sjMkdYbbQfG5HnnYgLHn1ILlgHPhhJRS3eoXrolHDdHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج اعتراضات دانش‌آموزی به دانشگاه‌های فرانسه هم رسید/ رنگ‌وبوی حمایت از فلسطین و مخالفت با صهیونیسم در تجمعات
🔹
اعتراضات سراسری جوانان در فرانسه با گسترش به دانشگاه‌ها، به تعطیلی چندین پردیس دانشگاهی و لغو فعالیت‌های آموزشی انجامیده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/695129" target="_blank">📅 14:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695128">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-5cWQ3XyhScsDBADTJVsVotzJ862yoMsJGrRTTfZwJwjQCae7Jk2EF1HKACWKypKvq0pl86ZtnyHcDXVr9oNTOF-2hYKIUQDw5tcRoAjUkDZRlMQEZaD2I__8cYOTtWIMBwOCOJvwi_JC4nvuXDDHd6BxcewU7oR8YTxc-fz5SVjKl9QricpEMDZ1ieyZqwMyEAH4NsCzHXdmpuokRViQrmCWo118QJsxTdBAftoD5ZFBSm1nqFGJsCgu7gI_HSDTWm60_PLFjNiJmoYfuj6A9Fw6COudM78BBnYjuvwot3r1_qgKqC_PbvZdB9H2aFkITluNmASkIaKlATQmBGgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پسرها صدرنشین رتبه‌های برتر کنکور ۱۴۰۵ شدند
🔹
بررسی اسامی ۴۰ رتبه برتر کنکور ۱۴۰۵ نشان می‌دهد پسرها با ۲۳ رتبه، سهم بیشتری از رتبه‌های برتر دارند و تهران نیز ۲۱ نماینده در این جمع دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/695128" target="_blank">📅 14:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695127">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رهبر جریان حکمت ملی عراق: در کنار ایران و ملت این کشور در برابر فشارهای اقتصادی ایستاده‌ایم/خواستار بازگشایی تمام فرودگاه‌ها برای پروازهای میان ایران و عراق هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/695127" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695126">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d92aee257.mp4?token=pYGzAQTRMA7IQI70gCaWvj_2MuZyHTILDwsEELEG4_Za-3NI6edHvzMnieehyj_P7R5cslwLz8g5gQxO_uxBfiW8kclW_V5mG2roEUvppEolCtC2I8dzuoSnuoTpvp7nKGJzPEsXCerGd4CZb9TaV_k7whh_DofCfJY8BMpRuvDArqsRojoJm2t5nIy_XWD1pJ7ecpeX-h-DGU6tlBWgkHf2K2JYMqXTdIW6YGEj86TcUlY0HR5IycKmPzbATACI_ejdToKAyBZrYR8-3EpkWKdlrAiRcJrLy9u0sXLOKsGvk_NBqDYvJcA5fWgrXNGEhYEfDtOghV6rrj-7NYrmRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d92aee257.mp4?token=pYGzAQTRMA7IQI70gCaWvj_2MuZyHTILDwsEELEG4_Za-3NI6edHvzMnieehyj_P7R5cslwLz8g5gQxO_uxBfiW8kclW_V5mG2roEUvppEolCtC2I8dzuoSnuoTpvp7nKGJzPEsXCerGd4CZb9TaV_k7whh_DofCfJY8BMpRuvDArqsRojoJm2t5nIy_XWD1pJ7ecpeX-h-DGU6tlBWgkHf2K2JYMqXTdIW6YGEj86TcUlY0HR5IycKmPzbATACI_ejdToKAyBZrYR8-3EpkWKdlrAiRcJrLy9u0sXLOKsGvk_NBqDYvJcA5fWgrXNGEhYEfDtOghV6rrj-7NYrmRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت «تلما» و دو توله‌اش به "توران"  مدیرکل حفاظت محیط زیست استان سمنان:
🔹
محیط‌بانان تلاشگر مجموعه حفاظتی توران موفق شدند «تلما»، یوزپلنگ آسیایی ماده، را به همراه دو توله امسالی مشاهده و تصاویر این خانواده یوز را روز جمعه ۲۷ شهریورماه ثبت کنند.  #اخبار_سمنان…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/695126" target="_blank">📅 14:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695122">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfFkkerQsFdUytluZSYD1dM47UfiVdudB_WL5VsdQpXybzUlY2wKHdeJ6JNMl_evB_0ahJyiQ2vHzv5H_vWF5XNwyNmfAg-pVkijZwhLwP0zNYIJPZYf2XpwpsRPjn9TVdDVzzOHtnmRgI9SI5ThkzXKPKa0VrLjr2esRpSECeQfh3nz5DGJt8mEIVS7571sdx_VTCYZ8PizaWhD5uUQkHDYjnYR880tMWaiWVwVoURQUb3EpxfE2bo0yBhjo2yg2-jpY08YQtsYngfdK5yfEbQJnROGmA_EZ8lmOmmU7gMlO2RGuSNelAk23TD5S7Zn0rxX-FLpnGWAOKb-cNUQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTC4IjUPJNOrRVhZprC1MmHwvNcTvh5KOKHhMbQNZV5B0NZoekYSOy-2HGs_m0cdr91btWyr3G-k7mzQ0qHudTfeh8RkIO7amgMdgeiEyGxdB9Z289iW6LSUnENFA_wjNoq51AfbZx4BcnW8uCiuGzf0JXWGriBX4yq8n7s2YQCeAZ3-u5gyhpQQUuUuXv7U1TT1YvQmlSybWBgCKoS9b73sjFyxiI_Jd3STvL7WjYz8b_gbYfID8G-rxFJp0OafufUFbOUuo3pa_laWY3fwLA8bSGUmMlOGFyBVe0FcZYU3EC-9_sqvVtMxxIcWMKG035h4nWkE4Mc2grTIcYXZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuSYnrP2NGxO9S2tuwdbKAddSPt3UpfotF_WUKYgZr9b__zu4EgcadxJkIylHuW6DgHVVnrUHPXlEsOfaPncenmFn72de5cMoekFcZersl2YmO9MJgkmJstdAQ9PLoTcl3CDLaBjf27ZoiH1sTeCeA7QYVLsQxXT6qCUct_93DDEMBEqQ3wG4qXjx7wQ7j4krmb_zsAgotC3osjSy6kHlECIxYbnisEaDIH-Zcewu1Z32UmF0h7keWZohWv0MxFPEECKQ29Rcb00cW5evHG-kd0ViiQN2EUJWzqAdo2Trhwd6NBTlJsOa_6AmpzQGuHJtZ0ySZBCf10zfi75y9_aIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvIkecKplXZJVzfbMtCJn0Wj9IV9KO8-FjkSGV1RgH-eZ4xz5uilQMW-i9WOvl76K9D2A3v2gDg0EoYONsmrDfTWfvE8nCo-xZIPD73wj3LmdzU9q0Zi3vwy8VOyHDWgUYeWasWFBsh39jK9ZRIg2G0Q8qYK9r15xt9zq4-i9KUe4N2OJr1FioWD2plSSlwUUbfAvXtITGAQJsQbmI7zSjJeP2MoYmpH3R2IWWfZvMV0TFaxiHW8ZaDd7ieXTEmrUv2Q0s4eCvoXczoCjmZ3DY_ihUMICU8httxIoRT9eOj2LIJi338TSJUQA_Rt2vxqypnUBKmPUW9peE0Lhpkozg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
باورت می‌شه با این ۲۰ آیتمی که احتمالا در کمدت پیدا می‌شه، می‌تونی ۶۲۵ استایل شیک داشته باشی؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/695122" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695121">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رتبه ۱ رشته تجربی کنکور ۱۴۰۵
🏆
آرش محمدی
🎓
تبریک به آرش عزیز
خیلی خوشحالیم که نتیجه زحماتش رو گرفت
پشت هر رتبه‌ی برتر کنکور، یه عالمه انتخاب، تلاش و ماجراهای شنیدنیه!
✨
این بار آرش محمدی از مسیرش برامون گفته؛
از روزهایی که آسون نبوده ...!
📚
از کتاب‌هاش، آزموناش، کلاس‌هاش تا تجربه‌ی روز کنکور و همه چیزهایی که کمکش کردن یا نکردن تا به این رتبه برسه...!
📝
خودمونی ترین مصاحبه رتبه‌های برتر کنکور ۱۴۰۵، به صورت اختصاصی در کانال خیلی سبز
👇
@kheilisabz360</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/695121" target="_blank">📅 14:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HTbT8Gljwixp6cnmjB1aXW_OtD5u-REExl_FT25p1ko4hkfGKiqp0YCFwA30-BUHKwPnpQSSs99WtkTigwclGq9KE2DaKceGtXdn4lzN1En1IN7rfUwGvch94FjNOovzaRxcxtmuu3s8AFCjgW4Oa6xrW5pgcarlANKkua1XK6gIqHOWSASiJzu49MpJX-qXScFJx8NzAFgg7EKOENyZ65mUoNSB0Qb9S1IDV4E-ooGERHalJEgsdLVLuMK-q0BPRRi6T6TT6mmkC6wQ3IbZVmJ55DOKOFfdMXXuB_J2wNoSu10a8OtzsFm9fT2GHdy2DA_VkgvU8avGCkx1qR3jQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J07HRkTIp7OdoDccQiNHuI44NXF1Z8SwxVMUunu_KsS3nJmisUKClVIoaUbB7NaPAFtHm6CWKDEVNqXTqHORwxGQRiPGRpIIpPyNDsj2XHxlZ7o3kibu6fsz7oz9mqua5Hzvc2TIe1UI4XnyklnESR4fXTwjU4Mr7pPVB1OtOjjPU15sUbfw1rDIFntvftPdfcNlktbQV7OIrwO2Ty06iL-1T6EaXDp0oINmBr8_bNK0m7Cl6DkbiFk4QzFrZZY5o5JYRHOaxJSqhjEDmlg6kZOtw45k3LxuFwINDflKgfQwX963ReaC8rboaDVgvJ5NWzpw4BBmtX3VLtsVYK0BXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جان شیپتون، پدر جولیان آسانژ، در نمایشگاه «بمب برای صلح» در ملبورن استرالیا با سنجاق سینه میناب ۱۶۸
🔹
جولیان آسانژ، بنیان‌گذار ویکی‌لیکس و افشاگر اسناد محرمانه آمریکا است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/695119" target="_blank">📅 13:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c347e84fa2.mp4?token=i4NOSUP5ucgUNEJnyrrvnjixpv86B4u3Gu3FpkPe8iyexO1e1Fd0YMzlqBWhptNb7yT33lvrCnE3c9eqCPdezH0u39IgE6Q8MMjyoo1pvQuI5ZXBQditEzLPbMVrfcUnrTG6XStc3GIrdClbzrXKedyBatq34v4kh4bSNQRelPjgTGyYj8EpXIiuwz-RYcaGAjV_pWvRUO2NKtdMt_CPmjbUE0biaCHAWZhQMObICzVtZS2DFEFiH4SNph2uKruK_0ToKls888lSakleBq7vq7hVcHuvgvhvT2WFzI873W9V6Abeu0TxQ9To1wWAp1MkLCOVMB_qPd9eVwg3dj-8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c347e84fa2.mp4?token=i4NOSUP5ucgUNEJnyrrvnjixpv86B4u3Gu3FpkPe8iyexO1e1Fd0YMzlqBWhptNb7yT33lvrCnE3c9eqCPdezH0u39IgE6Q8MMjyoo1pvQuI5ZXBQditEzLPbMVrfcUnrTG6XStc3GIrdClbzrXKedyBatq34v4kh4bSNQRelPjgTGyYj8EpXIiuwz-RYcaGAjV_pWvRUO2NKtdMt_CPmjbUE0biaCHAWZhQMObICzVtZS2DFEFiH4SNph2uKruK_0ToKls888lSakleBq7vq7hVcHuvgvhvT2WFzI873W9V6Abeu0TxQ9To1wWAp1MkLCOVMB_qPd9eVwg3dj-8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حقیقت تاریک پشت لوگوی اپل از زبان شاون ریان کارآفرین و مجری آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/695118" target="_blank">📅 13:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سخنگوی ارتش: در جنگ ۴۰ روزه، نیروی زمینی ارتش با استقرار نیروهای زبده و تیپ‌ها در مرزها، فرصت تجاوز زمینی را از آمریکا گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/695117" target="_blank">📅 13:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a49fad02.mp4?token=YF2bLD77_RZCra62nfIyROQCxtT74BjcDXoYIGUutPsnW6Ajg-klCo19PLzunPvrzpSsI3ChkjkKSgcUmepmEQoVXkmWDOeyndKTtX7HUlBVAiUjZBlOKmHVerUn_TYSfEwnVoC-PneCgCMt7ZQMXaIP_asaqC7g8nt8eXrpk1Tk-yJc4_5ASaN1t4B7ho4-5SX5NJofOPewLcGD-pRodBF1FpqgTsb_ZYKLXSNZJ1VVYbAV7p1UX93WBx19nylZVd7IAi7TNTg2-3aw2PYuF0INqF0TNf0xBROUJRS51s3i-s8mPw_p86FGo-0v9RLHO35mPO_L7yCBlcHoJ9VfwiGmzVGUUvkRQ-SCZSAJGOqkokOV7nQ9Ja7r2J8lPikFOTTtGccC5y2otQ1Ch3F6SNdvbd3XjfdVVwcj3B1oigfI5Gh3RXDhrVbOhSXzbnWaj_i99-u9QQ7DqNYk-SwGNHfynW73KCKJSHaJoCk98eTKp3X8EvSAbIWO3cS_aMdceDtf196lSDqMl5HPV0ZL409p2MERzFBlOD9unLitp7obnT_I89wiHINiYkvQK9YRtzcf-scdv5KSg-nVe2O-8iZxXl-WUQNmCVTaS9u-w6zg582qRRk4bIuVwr-jvMyyXzd3O2e0V4xrX7lbN_FJRbFiEVJ-CxLocG0DZQru2hE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a49fad02.mp4?token=YF2bLD77_RZCra62nfIyROQCxtT74BjcDXoYIGUutPsnW6Ajg-klCo19PLzunPvrzpSsI3ChkjkKSgcUmepmEQoVXkmWDOeyndKTtX7HUlBVAiUjZBlOKmHVerUn_TYSfEwnVoC-PneCgCMt7ZQMXaIP_asaqC7g8nt8eXrpk1Tk-yJc4_5ASaN1t4B7ho4-5SX5NJofOPewLcGD-pRodBF1FpqgTsb_ZYKLXSNZJ1VVYbAV7p1UX93WBx19nylZVd7IAi7TNTg2-3aw2PYuF0INqF0TNf0xBROUJRS51s3i-s8mPw_p86FGo-0v9RLHO35mPO_L7yCBlcHoJ9VfwiGmzVGUUvkRQ-SCZSAJGOqkokOV7nQ9Ja7r2J8lPikFOTTtGccC5y2otQ1Ch3F6SNdvbd3XjfdVVwcj3B1oigfI5Gh3RXDhrVbOhSXzbnWaj_i99-u9QQ7DqNYk-SwGNHfynW73KCKJSHaJoCk98eTKp3X8EvSAbIWO3cS_aMdceDtf196lSDqMl5HPV0ZL409p2MERzFBlOD9unLitp7obnT_I89wiHINiYkvQK9YRtzcf-scdv5KSg-nVe2O-8iZxXl-WUQNmCVTaS9u-w6zg582qRRk4bIuVwr-jvMyyXzd3O2e0V4xrX7lbN_FJRbFiEVJ-CxLocG0DZQru2hE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جانی به آمریکایی‌ها: گرانی را تحمل کنید؛ این در برابر هسته‌ای شدن ایران ناچیز است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/695116" target="_blank">📅 13:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d3092203.mp4?token=JS4pPF75flUBX3YdK48te9NnM4NBnd5D8Q9BMsTeKwY_ztZ6mwBZNzn_hvwm303SVLvFrN9LaqqT5dDT4AqG802bXJUSb71qc9d5vxSHWVmHeAHEHaX-m_JznefxzAU25_H2blHxeeCDRfwIfkhK5pKkSgKjY1hGiZYO25ldkCo0FAzeMNjyv9XJss5xo8fqr7OSRB4rRHSA-c4NB1JUsLTY4ztHYwpjEXsn3uF_qDl7iXXzKX70epXyi7bq1pEvOTgy5AHQhd6sEEclgWNcUABEukDRN293iMbiOG_cx0Kz0IppfkReVvhYWUDoOTP0dqA7MPU5j7Rkw4OG8wMDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d3092203.mp4?token=JS4pPF75flUBX3YdK48te9NnM4NBnd5D8Q9BMsTeKwY_ztZ6mwBZNzn_hvwm303SVLvFrN9LaqqT5dDT4AqG802bXJUSb71qc9d5vxSHWVmHeAHEHaX-m_JznefxzAU25_H2blHxeeCDRfwIfkhK5pKkSgKjY1hGiZYO25ldkCo0FAzeMNjyv9XJss5xo8fqr7OSRB4rRHSA-c4NB1JUsLTY4ztHYwpjEXsn3uF_qDl7iXXzKX70epXyi7bq1pEvOTgy5AHQhd6sEEclgWNcUABEukDRN293iMbiOG_cx0Kz0IppfkReVvhYWUDoOTP0dqA7MPU5j7Rkw4OG8wMDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طبیعت‌گردا حتما این ویدیو رو ببینند| عقرب مرگ!
🔹
چون تزریق این عقرب زیر جلدی و زیر پوستی هست فرد گزیده شده دردی رو احساس نمیکنه برای همین متوجه گزش نمیشه و در نتیجه به بیمارستان مراجعه نمیکنه؛ برای همین درصدر مرگ گزش این گونه عقرب بسیار بالاست!
🔹
پراکندگی این عقرب بیشتر در نواحی جنوبی، جنوب غربی ، غرب و برخی نواحی مرکزی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/695115" target="_blank">📅 13:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیشگامان توسعه ارتباطات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSx_uDsDNgJHwjsoXfNF13vUu0cBPSvc4PRwHdwyIkiVbhu5ppOWCtWmafTj7-DC5FMnFJBVJetfFwK0fNVy4GcLrud5JGCR3ef0HvPlWCf2QISSqEz2Cyten3_uWf6b3Z9JfWMhsQkkJbAA693K_KUXUCWJGtnK_0p_1EMmaGhQPp33urTyu3m1XX_GWPE6mZXAWVfGX2ajo6Zg39AE9D_4pDHLHUETCupn_-J9LSUFEwSCq0kUlh_bcAzeuvwj9vc76ps87joqh3YvGTQTet5k2uTJ1xkNUcpgQxGOzbk7wUYsULvhJV6p-OAPIje_fyTFnhmOkpKQnsrTSBvw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاییز امسال
🍁
با مودم‌های LTE پیشگامان
🚀
اینترنت پرسرعت رو با شرایط ویژه جشنواره به خونه یا محل کارت بیار!
🧡
خرید ۴ قسطه بدون ضامن
با ترب‌پی و اسنپ‌پی
🍊
ارسال رایگان به‌همراه سیم‌کارت هدیه
👈
بدون نیاز به خط تلفن ثابت
🔥
تا 600,000 تومان تخفیف ویژه
🎯
ثبت نام سریع:
https://pte.ir/a1tza
☎️
تلفن سراسری: ۱۵۷۷
🆔
کانال پیشگامان |
@pishgaman_official</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/695114" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJuNQtX9czswL6uOd59vWFR6ik-FDhYv69K1E7XLbiLt1MHQRuE_rimSZCTfzduYcF6pzrGcdd3dRyWjYgGjAO-xQdoCLlOeTUby6cWB7Z2sHKK6XjTLoqInXK33uq34iBIe-0873yL3it56nNaps7PH8oo_3gcaX3T932TwAih-DMJqTjNqbu2Ah9-YrwosoOjD7AmBh0HhE6IcPE0YTt6I0z0AZQgZV5vQWrKOM_ZmfjF-ypYjx6sIvod85HNfMZpEMeygV-f0lxAXBlpdJRtAJnUINqnBHrr2SBE7X1bhdSayESbp7Ad2Fm0CXfIGwoj6V9e-DLEvq1XHpkLYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسایش در سفرهای جاده‌ای با آروباس
💛
با اتوبوس‌های جدید وارداتی، تهویه مطبوع و شارژر اختصاصی، سفر جاده‌ای راحت‌تری را تجربه کنید.
🚌
🎁
کد تخفیف ویژه مهرماه: MHR405
💳
امکان پرداخت اقساطی با اسنپ‌پی
برای دیدن مسیرها، تخفیف‌ها و خبرهای جدید، به کانال آروباس بپیوندید
👇🏾
@Arobus_ir
رزرو بلیط :
https://jryn.me/7qlJR1</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/695113" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
خبرگزاری رسمی اسرائیل به نقل از یک مقام امنیتی گزارش داد: ارتش اسرائیل دیشب علی العمودی، رهبر حماس را در غزه هدف حمله هوایی قرار داد./ الجزیره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/695112" target="_blank">📅 13:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ca7e8e9e2.mp4?token=nTOPHvCzcaywaH-46PRpgI7APNmXN30r2GnzgSwszgoanCOF_JNJ6VC1eqQBqu1P9pzDk0_wxoOJOTlwzWG68QXGRrnL5JlprQUl6QMx8tzMCcmMdWbEeQW0y4zGDQyfwbaWLXMCUpUzbC20RABVK6bGx6yRh5yU5hS5sARlHJOAXXZtpqILQ4HAHciZYUrb0MII1MykH0zvfrS0EY-FVwe5MBJF1HTFFZ-C-StAywIFZQt91IRubfDhqHPeRzfp1tnZntTpU51l9koX4oAYVRmY7DdtEIcXihQCC3sJVizb2v-ff_jAeMzSGOea094qvYeAFn1PQnI-t48H2qSnYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ca7e8e9e2.mp4?token=nTOPHvCzcaywaH-46PRpgI7APNmXN30r2GnzgSwszgoanCOF_JNJ6VC1eqQBqu1P9pzDk0_wxoOJOTlwzWG68QXGRrnL5JlprQUl6QMx8tzMCcmMdWbEeQW0y4zGDQyfwbaWLXMCUpUzbC20RABVK6bGx6yRh5yU5hS5sARlHJOAXXZtpqILQ4HAHciZYUrb0MII1MykH0zvfrS0EY-FVwe5MBJF1HTFFZ-C-StAywIFZQt91IRubfDhqHPeRzfp1tnZntTpU51l9koX4oAYVRmY7DdtEIcXihQCC3sJVizb2v-ff_jAeMzSGOea094qvYeAFn1PQnI-t48H2qSnYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو جنایتکار: اسلام‌گرایان و چپ‌گرایان باید به‌طور طبیعی در مقابل یکدیگر قرار داشته باشند
/
اسلام‌گرایان همجنس‌گرایان را اعدام می‌کنند و زنان را از هرگونه حقوقی محروم می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/695111" target="_blank">📅 13:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شادی امیرعلی راوندی بعد از اعلام رتبه ۶ تجربی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/695110" target="_blank">📅 13:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695109">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
وزارت اطلاعات: انهدام ۴ شبکه خرابکاری در سیرجان
🔹
وزارت اطلاعات از شناسایی و بازداشت ۳۱ نفر از اعضای چهار شبکه سازمان‌یافته در سیرجان خبر داد.
🔹
به گفته این وزارتخانه، اعضای این شبکه‌ها برای ایجاد ناآرامی، ساخت کوکتل مولوتف و تخریب دوربین‌های شهری آماده شده بودند.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/695109" target="_blank">📅 13:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695108">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb49d47e2a.mp4?token=jEVY9Mz3U_OYBzEI-xHlGxJ2bQ-Igzg_XKX0Xi63bhvLNrizF9a5h-gYuQQOtX31Emr812CnGPoiyN-CRQ5XxHxxWEj0oxADZ0hyheXXGnTgsHoYmwXkS5MhPbtR2jntN5zdFdNfR_5pylgoa_rmIUHWEQma_eFm1hWP1o2qJ50BW4ux_o7LPJDFIWxSUXhL7xAmiWnOUeBHFPXlURbsDwslAUPmwyvu47xZz2_rOuGPS4POH3ATSRtvKK5Bm76Wma34pnG9gd83-GVBiTx-fAPgCobBXUxsD1klY1lGwG5ONKruqeEHcjNo4kN98m0TIrjbNb3C-cncBXOOvx8Puw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb49d47e2a.mp4?token=jEVY9Mz3U_OYBzEI-xHlGxJ2bQ-Igzg_XKX0Xi63bhvLNrizF9a5h-gYuQQOtX31Emr812CnGPoiyN-CRQ5XxHxxWEj0oxADZ0hyheXXGnTgsHoYmwXkS5MhPbtR2jntN5zdFdNfR_5pylgoa_rmIUHWEQma_eFm1hWP1o2qJ50BW4ux_o7LPJDFIWxSUXhL7xAmiWnOUeBHFPXlURbsDwslAUPmwyvu47xZz2_rOuGPS4POH3ATSRtvKK5Bm76Wma34pnG9gd83-GVBiTx-fAPgCobBXUxsD1klY1lGwG5ONKruqeEHcjNo4kN98m0TIrjbNb3C-cncBXOOvx8Puw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخت‌های هیرکانی، بخشی از میراث طبیعی ایران هستن، مراقبشون باشیم
🌳
🌲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/695108" target="_blank">📅 12:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695104">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjCdshWLapkLRupYbXLSL-xs0vaYmMOJwEU4N15znhFfm2b_DTrsuOu47SrxQ2_TI1mvOR2sK6_8P5aKK9UahydwKHH55uvihzufgPgcnOcIbWR39C-_-HGdOl1y9ueOO1ZFFNtXLj_h7ATRbZ3rhvhKBvHrjvKYmbXuTYTG-j_jb63I2WbqV6prwVH_HbQ0GiFj___HRBKZTXmCIXtA-i3lWrChTTmyOuDsXvOgGA6-0ItijYrT4t_opS12u2WijEiyRvxJDkXYDu740LaLJoluVpoG-W2Y6Ob0zMhU2GQe3muOUDO0k5PjzxUg8mwTuUCao6FW_JKO_MCiz9w5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_RUKAsfoA48XquzOW2m-CqSYCkppaCL59fu5tWgLy6PeeuSeSHJ6UwTa3U16POah-Fmo5xD7aE66LP4RxMYQht8piZBdnVu-N_T4Q7XIJmFqLlndzHRvKe4oK0epkdJBdbHZfOCim-NlR9TsSdS_i53UjT82n7sOgJ44DY2Lajcum0vTOIs-zeqCroLsrVm7DuxIJiGnlaKq8Y6sM_zF6sMow6Bnzk1yrJfNiILSG7HHH4TnUdHZWyPlZH-p4Tb00RLVRUMmzwJ9SnNMYe3ya_OM4BXm9uHXhmSM9CY-ip6UWBGidJ5IWqhck0jmeS9hcvd1jBJ_Cj3W-czwQIZuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86287d76d.mp4?token=I_z7MtEqz1Q0tEZBDmOkMgqErBideRW7DklcD1GuL-sou7-fFvLeQiCBBmTqsxcKgJp-WNNXhH0Tk0SvJiHKvLBoOoCPLkXd6B_fNmvRZ-2tC45ryWLqzdTlqIzjhwL9594FV9cYW8FRrNITs1q19V6BPu3cNkoMQw9qcY7K4lY66G-mDBLn7cg4kX1zaNkvRiyxdM-o7Udhx7K7BYKgaVrwN28jQjqDTrQPYenOSpN-yCo2NxXFlrDDksXbQm5CpRGz1jzi0NYH9_rVY0ajtq1aClzO5akPqAXDiT1_0iPfr65hMBTlZPQr9izMaJdKxfO3lAkARLHaLCkofBVrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86287d76d.mp4?token=I_z7MtEqz1Q0tEZBDmOkMgqErBideRW7DklcD1GuL-sou7-fFvLeQiCBBmTqsxcKgJp-WNNXhH0Tk0SvJiHKvLBoOoCPLkXd6B_fNmvRZ-2tC45ryWLqzdTlqIzjhwL9594FV9cYW8FRrNITs1q19V6BPu3cNkoMQw9qcY7K4lY66G-mDBLn7cg4kX1zaNkvRiyxdM-o7Udhx7K7BYKgaVrwN28jQjqDTrQPYenOSpN-yCo2NxXFlrDDksXbQm5CpRGz1jzi0NYH9_rVY0ajtq1aClzO5akPqAXDiT1_0iPfr65hMBTlZPQr9izMaJdKxfO3lAkARLHaLCkofBVrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استوری‌های راحله امینیان از وضعیت مدارس لبنان و تنها خواسته مردم لبنان؛ «فقط سلام ما را به مردم ایران برسانید»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/695104" target="_blank">📅 12:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77d54ad32.mp4?token=WPKjqafiZvAecRVsn57etoJ6IXOfOS91A4EC8A4SxCEir7MBV1lPXIQweMGBBcaYmH_bF8kfJ9WwuFUG_cCkeZCmUBYeeaks1AVlHB2Ix_iswPgIhW4hiPqNPaZVHF9nDFeZXNcnn57LUgZKFyFVU3GBtukan88oR9TLxOepuQLFv8D_OYgpUOJ9kZ7DRoFEH6ofciXHOW4Q77Kc2NZSc-VnQRC3I6iRMYC_GorYcncmvl5W47cbGjm_nxFjEbs95G0aNHD3RMy44JRqrnlx04FZCvwLJshJGG1cr-89xLJqzw1nd2CT8TU8U0o48bR5gH8bny9AGWRho0Xgd81NNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77d54ad32.mp4?token=WPKjqafiZvAecRVsn57etoJ6IXOfOS91A4EC8A4SxCEir7MBV1lPXIQweMGBBcaYmH_bF8kfJ9WwuFUG_cCkeZCmUBYeeaks1AVlHB2Ix_iswPgIhW4hiPqNPaZVHF9nDFeZXNcnn57LUgZKFyFVU3GBtukan88oR9TLxOepuQLFv8D_OYgpUOJ9kZ7DRoFEH6ofciXHOW4Q77Kc2NZSc-VnQRC3I6iRMYC_GorYcncmvl5W47cbGjm_nxFjEbs95G0aNHD3RMy44JRqrnlx04FZCvwLJshJGG1cr-89xLJqzw1nd2CT8TU8U0o48bR5gH8bny9AGWRho0Xgd81NNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درحالی که همواره در سال‌های گذشته جنوب کشور در بین نفرات برتر هر رشته چندین نماینده‌‌ داشت، در کنکور سراسری امسال هیچ فردی از جنوب کشور جزو ده نفر اول هیچ‌کدام از رشته ها نبوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/695103" target="_blank">📅 12:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
دادستان میبد از تشکیل پرونده قضایی در پی فوت چهار نوزاد در بیمارستان این شهرستان خبر داد
🔹
علت دقیق این حادثه هنوز مشخص نشده و احتمال‌هایی از جمله قصور پزشکی، قطعی برق و مشکلات زیرساختی بیمارستان در دست بررسی قرار دارد./ ایسنا
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/695102" target="_blank">📅 12:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
درخواست پول بانک‌ها ناگهان کم شد
🔹
بازار پول هفته گذشته با یک تغییر عجیب رو به رو شد و تقاضای پول بانک‌ها از حدود ۴۲۰ همت به ۲۹۰ همت کاهش یافت.
هر چند بانک مرکزی سیاست‌های انقباضی را در پیش گرفته اما در شرایطی که تورم همچنان بالاست، کاهش نیاز بانک‌ها به پول چندان منطقی به نظر نمی‌رسد.
🔹
برخی تحلیلگران مدعی‌اند که شکل تأمین پول بانک‌ها تغییر کرده و بعید است نیاز آنها به پول واقعاً کم شده‌باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/695101" target="_blank">📅 12:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695100">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد
🔹
در جریان این درگیری لفظی، مردی که یک قبضه…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/695100" target="_blank">📅 12:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f299fb69.mp4?token=iaLomUV0HAYu7aBS1oJQ8i57UrBgHbk_MolNkRp5ooMtisIBGft5X0Wi2DpdqIDWc7DXnmBVp6Tbvauya4ttatoi4nOiVrSltUcUUJJoS3lBqi-gebXxtf-Qt5wBXvKCUX9nd9J2bge480coM74pgVCFiev5OFsAaCatcHN4F37jgpFYP_ZZntZyVpJThxghliIUIU-N62kXi-RysyAiAQTOkCDgEP-Yi_izjbuJMlVGyoi6hqzQet0F9ZWijYFf8whRRWqFAtAbbhYaKs_cpARxl8oC5ETrKdca6mcKiARqS5EXU5d9OGvnsA9ErxJ9lZd1To3bheBM9VtIHZHZt4B8JXV2wxnt_sScCrUJl12HScaAEpkhq1YezwUPLDkMP0jJLYjrfQtP2ErWKeicHdsHbCdnE6a8ZKz81zSXtR6uBrwdaGppscn251JnRaJ0AL156eWasFzCW8FQmQZ1a_CPDlgwDzM0xChB8NC5P9-dQ7PWFKy7WmKD_E7VkN0qji0uLuIGywrphndXuVxowkOg-DMsJUEsJraLAwSckCqN3bAxxdc4xAPu9xxci4Fl-eS88Bm1nMW2kx514HDWb9SXuwBMcZyOaw9apR_-BoZM8tE6tY2E8RWB9isCwVSxQWP36qQcO5350xea3Q-2P9X50DAvkf-11vkD2hTqaVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f299fb69.mp4?token=iaLomUV0HAYu7aBS1oJQ8i57UrBgHbk_MolNkRp5ooMtisIBGft5X0Wi2DpdqIDWc7DXnmBVp6Tbvauya4ttatoi4nOiVrSltUcUUJJoS3lBqi-gebXxtf-Qt5wBXvKCUX9nd9J2bge480coM74pgVCFiev5OFsAaCatcHN4F37jgpFYP_ZZntZyVpJThxghliIUIU-N62kXi-RysyAiAQTOkCDgEP-Yi_izjbuJMlVGyoi6hqzQet0F9ZWijYFf8whRRWqFAtAbbhYaKs_cpARxl8oC5ETrKdca6mcKiARqS5EXU5d9OGvnsA9ErxJ9lZd1To3bheBM9VtIHZHZt4B8JXV2wxnt_sScCrUJl12HScaAEpkhq1YezwUPLDkMP0jJLYjrfQtP2ErWKeicHdsHbCdnE6a8ZKz81zSXtR6uBrwdaGppscn251JnRaJ0AL156eWasFzCW8FQmQZ1a_CPDlgwDzM0xChB8NC5P9-dQ7PWFKy7WmKD_E7VkN0qji0uLuIGywrphndXuVxowkOg-DMsJUEsJraLAwSckCqN3bAxxdc4xAPu9xxci4Fl-eS88Bm1nMW2kx514HDWb9SXuwBMcZyOaw9apR_-BoZM8tE6tY2E8RWB9isCwVSxQWP36qQcO5350xea3Q-2P9X50DAvkf-11vkD2hTqaVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه اهل کوهنوردی و طبیعت رفتن هستید برای روشن کردن آتش، این ترفند معرکه رو حتما یاد بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/695099" target="_blank">📅 12:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695097">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXUtC121EPkUPDVZGuHUwsN_lhupCYxo0GbWDTBYeQlOEmUMSzS_AGXLIVcLMrhjujeqa_MtZJMXfla5fbTRbow3Rl6xUTHrXFWOPYRoJXjbymxJ5hFOl-vA2MZau60DZDm60KUHVLmFhrJNZgW2n0TdxqthxQks8kcowGpucUf2Z3sZ7Yc0s_IElBc2CuNzXOwqkzyb6uch9-PTnKeHVgMNnOuRPwJpeJaOjNtVoO-F5GMLsZJMRE-dyPGmnsKd6j_ZokgbuCQDtTzoIFC59sfbyIH3kYDwdawEtFGoIamnONCea8Oe4yIiJSOy0V4awq9R1Dw5McaJKpGdcR9-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسیرهای پروازی بین‌المللی برقرار با ایران و شرایط ویزا، پروازها از لحاظ تعداد و مقصد محدودتر شده اند، در این لحظه هنوز پرواز میان ایران و‌ عراق برقرار نیست. پروازهای میان و امارات هم وضعیت نامشخصی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/695097" target="_blank">📅 12:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695096">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=qUQk-REnk6EUYCnrzGjytOkdFxeCZLqEGOfZX6mWzk5a4VsuLrRho4QjHamDek1aEAt7fyCtSSNC4q88TvueYTKMAQ44wHD0oSif-Ok2VM9ht50O-4nuRM9UprACcbxeaBPWk6yBZkiSkc0NxagX-4upkrRkGvuek40zkGdnhV71OsAPRAs7NDDdNRS5KrTaRMbxusj39_2MBm4dy7lvl4BqRzOenxryzDxh5PsOG4q7c-yVJs2qSQRgUJWn8tduOEsgbenl9PoR6ti84Zsg3cb7cDvanYcfjuSSpkivCNHYPwpxUIjaWLQriFPmBYblBUf9IhYhdmo48G0DWcR_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=qUQk-REnk6EUYCnrzGjytOkdFxeCZLqEGOfZX6mWzk5a4VsuLrRho4QjHamDek1aEAt7fyCtSSNC4q88TvueYTKMAQ44wHD0oSif-Ok2VM9ht50O-4nuRM9UprACcbxeaBPWk6yBZkiSkc0NxagX-4upkrRkGvuek40zkGdnhV71OsAPRAs7NDDdNRS5KrTaRMbxusj39_2MBm4dy7lvl4BqRzOenxryzDxh5PsOG4q7c-yVJs2qSQRgUJWn8tduOEsgbenl9PoR6ti84Zsg3cb7cDvanYcfjuSSpkivCNHYPwpxUIjaWLQriFPmBYblBUf9IhYhdmo48G0DWcR_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان در لبنان: مجاهدان لبنانی پس از حمله اسرائیل به ایران و شهادت رهبر ما وارد جنگ شدند و با چند هزار شهید، نقش بازدارنده‌ای در برابر دشمن ایفا کردند
🔹
برای احترام به این فداکاری‌ها کافی است فقط ایرانی باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/695096" target="_blank">📅 12:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695094">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccb68a932b.mp4?token=GpZYXdjx2PkU21Xo5MC0BeS2iPVDmw_gS8ID2huvnTmfmdqV8-iijJTRG5JJrbEfy0uLFJdg2M2z42VNA6I3thuywXpQiRUEIBcfoGIpYnq6lkd0A2T82B4UYzsh8vGl9T9WMPzb9sIzF5mcJGRUOcMGf5zrUe9CyNxv_DLgdEp01Waw5wDTGkFA7syuqf6tRIm9TN2-eQxdZ5AOWt0WjmwdMHzh6sPi3lB2LR0h7hR7LwL6i-jxZe8wLeP5WAbqoqqEE0LEoE1UfGTxKuQ8EfKMt-vXVZLZ06OnXL8MXmlosHyIKGYR8lg0JpSD5lfsHLGNjIgUmRobAhcx4S-kGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccb68a932b.mp4?token=GpZYXdjx2PkU21Xo5MC0BeS2iPVDmw_gS8ID2huvnTmfmdqV8-iijJTRG5JJrbEfy0uLFJdg2M2z42VNA6I3thuywXpQiRUEIBcfoGIpYnq6lkd0A2T82B4UYzsh8vGl9T9WMPzb9sIzF5mcJGRUOcMGf5zrUe9CyNxv_DLgdEp01Waw5wDTGkFA7syuqf6tRIm9TN2-eQxdZ5AOWt0WjmwdMHzh6sPi3lB2LR0h7hR7LwL6i-jxZe8wLeP5WAbqoqqEE0LEoE1UfGTxKuQ8EfKMt-vXVZLZ06OnXL8MXmlosHyIKGYR8lg0JpSD5lfsHLGNjIgUmRobAhcx4S-kGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری تلخ از آب‌رفتن پول!
@titretejarat</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/695094" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695091">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تصاویر نفرات برتر کنکور  سراسری سال ۱۴۰۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695091" target="_blank">📅 12:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695090">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ویدیویی پربازدید از اعتراض به قیمت بنزین در آمریکا در گردهمایی با حضور ونس
🔹
این فرد معترض، هدیه ۵۰۰۰ دلاری ترامپ به رای دهندگان جمهوری‌خواه را هم به سخره گرفت‌.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/695090" target="_blank">📅 12:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6jVi2rLviktNizAsvdOxLz5LauJ2b3GChf0tFOQvjrJuMjx2cBqBrSIDbt0QFXHMnVYYyoVAiwXvFUVNuV6MgKbfwMTa2cacdpWFe8YNucbIGk1k_w2YwPWc5vZmqigRDauk69VS1_S6J_EK7FTdMR7JBt_Ia5m_-DYaS-HFZdxnZc_HZuGWwjqc4xUg7NIexQbx6xTn_9PyqP9bwoIZRaf5ShjMaVP4B8n-e3zsNkV4fYvfUDLQFqH-ayEqOD5pQ_7FsWBXJoUMNKhfJ5ovfyLRLkQIEOgU2AvqwMkbpiTytTVoGFhfCcZgxajdzFi-oVWHA9OSbbUe0t8wcowaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awi74xrYzQSd_RCONd4oDaJZNu6-j8LfPi9inruns5Sel2gLl_0jc0aq8XyD6J5wXoNgy_96rVN_tx_8tpbrii2chZHMRb_M7Y1tGm-b7oyUsdTE7ITSdV3Gbt04ByEpUD8btxRH5Uh2xfqIuLMUYPRWqRjGi2fx7slqzsa0YuiqZqHkFn4HvBFjsVappPJRxcms1eZt7jVbAyxp6AwIppC_97FRbLIjLkx6653BaJAVBpPpWADJxWCEdbXSTBnBSRYUcMsezS_fMUP04HrtnRMhKkDavZ_zUu7a9zOQErEI2owAFqmLzihgNbYQlHp0IJlBWUB3kPhghSv7QhTyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/of1F30rVmJwokHGFAsBfPocr19NTL71ASGqF-qm_ikr8ay6mo75RsEskazVeoNrlsueBvAQN6oizcWuvJ5XmZp6Ba84Fw3OrTmodLLtCLMDIQQpvfu44pslWWPD27-GHNTv9WjEd_VUvYwGbpa4CmOsdW4k3QwlARh4pXvhekkBsxHpSWMnERcKaBjkzKyTwa8Uglmw9OwmBjNffKPyh5lB7yo8s4SKDxejZFWtjW9fL299Bccain7Oadho1XTwZv4WPDOjFLq78XDEGkKUSJIa_Fs94g3nIpO213fgJcyf5PHq6-K7VTzhmQMWcB5RY2THz2XIV_1EhMQEGrA9drg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Em5Ld-4bO_yVtMWhKtpbcp9RCJC9oq-zMdJ1PSnyziNy2Jn_KFGD-qzFLf_-Q33-sp9OVaM135SRZdULmfgzltKeLlvwi7KmfBkV1R9aVCH5_58YB5_VPlkQO0_abLwYlRmaT1TU16Q5hapZK_V3iFKnECSBP758ztZcYRrb4pHPd4Nv0rs79rfJ8TGMl7EXpBWH9-JaT5H_PtscyvbkHJ_hfqPtg2VR1iqMIdMdYTldrBvyi3J-gyn-1Mf2Q7rbkv-kghD3OnxlwBk4ps9zeptnKK6vjyj8yQ1NUeTTr3UtZ5oU54I1zz6BcKkqlFPP0nappiX8mNxhshIVsmdBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suo8VvXPes7RA5G6KS8YGRucSEk9DWRuQGcmt-OW_UgdR0Wb9agQXNCbbxTo97u7U6OZ9mS0LI-EXoMHvz8kDqns2p5jdzR4-thOyXJoGD0QNMHXh6RdasJkWfRWMbuUVVKXeRwFE32A33EabHbazSPADSBWHxKi_k2MmHpFAR_E_I9x4kZbgWk2h23x79ojYguqfyc1r16GpAjTd1txPfl-V_X56A666nCUG8bflzJjNeM7nDBXTeW23b42-XLHvGQZ-AEShNOYZBPXnRUmQht_KVpnDiXx3RQox347r5YwVlnq6YsOwa9tKupDRhVpkEga05rgXHxhl9LYEcKRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPjwXyNbSpv9cO6FR6AD3-kDQ3NE1xBvHHUjvcP_vhbUDt9kaT6ZWJT6gwK9DdJlt42B24WU5qGU8H2qqhf-31vG7WZSFivD0XVbgTeHggeBnOMM1NBFrx-EOHCngE-ZGcIdE_zh14_1Sr2asi1qO8-GcPMCt_BesGI0vTr_1_tt4kq5JDMTlo-TvDK165IHL6NfoHgwoj_PUmGSjHPxTUBK16ek589neXHTBvCoEAN4pzDcS8674CvQRcQTzivKljnhD-uveqgHa71ApKLXDZxUjQKBpmS26uVrsa92a9egndyBvTjcBnH7XxsBIYM2qe3lvzKEgdt2jy-N4KWkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heWJViukE-yFT9UCwrMMnzPenfxgeJZCLMSWEcFXWKTqOoS6z5VE-yRc52K2G8IiNs4vj8xpfxqnilS2IfdFqLBe5XpEbjWcY8ad3mGtMVBaM5_5Hzga5c78tKXQb1a3T17WAmtD8KxxRq8ts9uUHE38CvWrQNjj88FclQRVq8FwslCZ7QXbvZZddJwAV2OJW-I0itEaDYXeBOedU9WturMe2XSWmLseZiS2qc9flZPzpEssPHGFe_uyqXJ5Ae9FfvC-qSC7-vfpObtQZfLBdWq_db2OYRcOOjYhJNHGddsdlDDLvoGsRZLxQe1oxmcXbomKVEYinPSGbz0zK9xj5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش آروین حسینی، رتبه دوم کنکور تجربی در کنار دوستانش زمان اعلام نتایج
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/695082" target="_blank">📅 12:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695081">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231efd4cb4.mp4?token=rz4C8aTrGW5VZqpYnBYNtNXRQ6TGjbxqizrWsC2HoTdtBmzNMfdmLd9EFhhqyJod4oDxiGd5Z1FM6PH1UsoqG-Svwny0MeF-zliBFyjzlqsXIfj_03XfWoeJGWd6cYm_-53Cy3IPRlBqu0vpuXUc39mDcjZnv69TnISv0-OaC2HfFa1okc4slu--KCZVwBjL4_07L9SUyDqVopfXnyXpJShjBOLkz5azJFaOLPUuM1BjWSw7-88BbRBxDB_lf9ha0Nvf7iYvVWAmh9mbnAUAAj0_qzFJ54VVe52k7O1PmXHNkpZxSXwmdDPYdIioGvACRL2AmUBlR1kKPE_xPLcDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231efd4cb4.mp4?token=rz4C8aTrGW5VZqpYnBYNtNXRQ6TGjbxqizrWsC2HoTdtBmzNMfdmLd9EFhhqyJod4oDxiGd5Z1FM6PH1UsoqG-Svwny0MeF-zliBFyjzlqsXIfj_03XfWoeJGWd6cYm_-53Cy3IPRlBqu0vpuXUc39mDcjZnv69TnISv0-OaC2HfFa1okc4slu--KCZVwBjL4_07L9SUyDqVopfXnyXpJShjBOLkz5azJFaOLPUuM1BjWSw7-88BbRBxDB_lf9ha0Nvf7iYvVWAmh9mbnAUAAj0_qzFJ54VVe52k7O1PmXHNkpZxSXwmdDPYdIioGvACRL2AmUBlR1kKPE_xPLcDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهرهای رتبه برترهای تجربی همه جزو شهرهایی هستند که در جنگ، تحت بمباران شدید بودند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695081" target="_blank">📅 12:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
بابک زنجانی شرایط همکاری در طرح تاکسی‌های دات‌وان تریپ تشریح کرد
🔹
طرح جدید تاکسی اینترنتی «دات‌وان تریپ» با دو مدل همکاری برای رانندگان و مالکان خودرو معرفی شد.
بر اساس این طرح، متقاضیان مشارکت می‌توانند خودرو را با تأمین ۲۰ درصد از هزینه توسط هلدینگ خریداری کنند و پیش‌پرداخت را بین ۲۰ تا ۸۰ درصد انتخاب کنند.
🔹
مبلغ باقی‌مانده به‌صورت اقساط ماهانه پرداخت می‌شود و درآمد هر سفر، پس از کسر کمیسیون، به راننده تعلق می‌گیرد.
🔹
در این ویدئو جزئیات متقاضیان خرید و مشارکت در طرح دات وان تریپ توسط بابک زنجانی کامل بیان شده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695080" target="_blank">📅 12:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/695079" target="_blank">📅 11:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=pcebvYpA25CKUQhWPdAvCkaEuJOOSgN6GLdTvzM7t0leL7yD2irhTpD4QjMssI83GHf8J7vWD4RFSM5nJH-Rt7spyZfnzo57IYEbolXnrlRiV5_NqEnYliTLtOnskhD5exj1Sc0rRLfRrqNNpV5wy2d-zn4uklo1qngSXULprPOu7a3Y651QK9zWmzH9rQY1t7cDlqhZsDZj74T0UTP7fbn1VK_gEfUaqss-q95hXDPTVGk1iB1fQ1Y1iXTta7D7iQWExC8r95aG9vA55hD9aro2sxGDQryRA4qPy-7MqeOZoLYOLgqGwanddVubvZVSRvxaKymUZGZhR7PrgMU5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=pcebvYpA25CKUQhWPdAvCkaEuJOOSgN6GLdTvzM7t0leL7yD2irhTpD4QjMssI83GHf8J7vWD4RFSM5nJH-Rt7spyZfnzo57IYEbolXnrlRiV5_NqEnYliTLtOnskhD5exj1Sc0rRLfRrqNNpV5wy2d-zn4uklo1qngSXULprPOu7a3Y651QK9zWmzH9rQY1t7cDlqhZsDZj74T0UTP7fbn1VK_gEfUaqss-q95hXDPTVGk1iB1fQ1Y1iXTta7D7iQWExC8r95aG9vA55hD9aro2sxGDQryRA4qPy-7MqeOZoLYOLgqGwanddVubvZVSRvxaKymUZGZhR7PrgMU5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان در لبنان: مقابل رزمندگان، مجروحان و خانواده‌های شهدای لبنان جز شرمندگی احساس دیگری نداشتم؛ این مجاهدان دارند جهاد می‌کنند/ خانواده‌هایی را دیدیم که چند شهید داده‌اند، خانه‌شان را از دست داده‌اند و در اتاق‌های کوچک زندگی می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695078" target="_blank">📅 11:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695076">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb9b5282b.mp4?token=GnfmqammsoJB1k5v8ajuVdyfvsAxGdLZuQ1VSsVBucdwuvjww036jtD5FoU16rzwlB9bx0NTmuag41zfZMcjTaMU_-PJOOyvc2o2dmkOusDD9lYQQ86gFXCY1svuD1l2awCf7tZCPeHu1QYKfu5GV0VWq-Y-EFEu6rrY42Q5gTMPe2qblnotBmt8u9921fi9mqeySCZXKQZhxc4uwKpA8HFIY6Z6Xhx10-i_rjWkJN4gg5rtcdWhAL5NZVcjTORD-s-DT2HqwSlmMrtpnZ-iCkA1zloDwFKfK1Jrcg9AIlZSpKm4NZxUWYHm-BFjHYL_gJ-uEekndx-XllNqVTS0MqZiGHFR6h5D5kkMGt_Ihs0BMydw483xJdM4t2ZZXn4-R9SipwCIaiOJ09ZWk9qDZ3NoHSkxtTALNO9ZNyslsdvsko7GIg0wuUB-Tjkv8hr_YCS2zQerkrJHAjVasi_pMhPeZgXvyjBXvRc_NBYWS4ZmxbiOkqRpMmcHsXbhP4Sdu80wlj2spWteYA0gmhHKjTqeYWCHQhtK9OBsmCBPVDrfUt_-_Cb47kIuMa3ERgpWBdsK3DtiLk3gIlJKtNrtKh1b_51_9QpaWrdbAc5lJSlZ0mZfDIFUDBG_OttVKpRNVXsd9FUe6fR2bb5gMTKYFl8ngx5_GmgxzXVMSFzSxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb9b5282b.mp4?token=GnfmqammsoJB1k5v8ajuVdyfvsAxGdLZuQ1VSsVBucdwuvjww036jtD5FoU16rzwlB9bx0NTmuag41zfZMcjTaMU_-PJOOyvc2o2dmkOusDD9lYQQ86gFXCY1svuD1l2awCf7tZCPeHu1QYKfu5GV0VWq-Y-EFEu6rrY42Q5gTMPe2qblnotBmt8u9921fi9mqeySCZXKQZhxc4uwKpA8HFIY6Z6Xhx10-i_rjWkJN4gg5rtcdWhAL5NZVcjTORD-s-DT2HqwSlmMrtpnZ-iCkA1zloDwFKfK1Jrcg9AIlZSpKm4NZxUWYHm-BFjHYL_gJ-uEekndx-XllNqVTS0MqZiGHFR6h5D5kkMGt_Ihs0BMydw483xJdM4t2ZZXn4-R9SipwCIaiOJ09ZWk9qDZ3NoHSkxtTALNO9ZNyslsdvsko7GIg0wuUB-Tjkv8hr_YCS2zQerkrJHAjVasi_pMhPeZgXvyjBXvRc_NBYWS4ZmxbiOkqRpMmcHsXbhP4Sdu80wlj2spWteYA0gmhHKjTqeYWCHQhtK9OBsmCBPVDrfUt_-_Cb47kIuMa3ERgpWBdsK3DtiLk3gIlJKtNrtKh1b_51_9QpaWrdbAc5lJSlZ0mZfDIFUDBG_OttVKpRNVXsd9FUe6fR2bb5gMTKYFl8ngx5_GmgxzXVMSFzSxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت روش ساتنا، پایا یا پل را بدانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/695076" target="_blank">📅 11:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695075">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGyA1RbK4Aigb3j9z4O5VFiNxH1X0WPD7x_ryn13Z9Bt30DGpR9mFHsKEVeXS3K3ZzTKO8OP8e1yGI8Pf9YORwm9HdK7Fw0LmZBdr8HchMXwQXx_VpII2UbCYVzrbYMZALcZ3SkXxKOrYSqF6OucUi6yW3K8Xurqmzm84mLoPfGoY_waWnWkXzpm4gwU8P7M7w469PY7o-eNXzwlWjJvcHr_xbygSYAodteM44O5G1kjJ0_oi0kTZbUvqg0lfhv71pTqOuMaGclFawZazGi7LUPQzta_qpAz76HCt7GIVpwzwJ_k6avZeZms7FN6F8qwG0u-nqZS0vBpCGqOhz5H-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلم جدید از درگیری در هواپیمای فلای دبی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/695075" target="_blank">📅 11:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695074">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4Dc_SwFKK0MwIYGVqeqT9KXpiDtzp-SU4GJmi4vEj5E2232vei2GueNOSnrTIUL3XdindzrsB1px0v5j5bvPeLjviNXPoVr0J7XeEFD36d9OUtQ7BakpindlE5ZPKj6wIJkfNfSQIPpoJxosF9aiVOWaKUUkfoAKm7mYtZOH8uBWCeRFOtYWKOHGJaJ_kWpgzUEXoSz2c6i1inhr-c39TCYUJibcpHG9E6YosbA4MT6vFJLcgezgLJPVNj-LW3r3l01ZB5YGm9EfCy16b-bJb37r_F8H5nGPjPE5FAOYnfxtXtljQiYqBTTYqQaWAImT-OfNCpjlr9F_oN2Aiw7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیوید کیز مشاور نتانیاهو در هفته گذشته: جمهوری اسلامی ایران در تاریخ ۱۱ مهرماه ساعت ۴:۳۳ دقیقه بامداد سقوط خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/695074" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695073">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد
🔹
در جریان این درگیری لفظی، مردی که یک قبضه سلاح کمری در دست داشت، به سمت زنان نزدیک شد و اقدام به تیراندازی کرد. جزئیات دقیق چگونگی وقوع حادثه و ابعاد آن تاکنون مشخص نشده است
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/695073" target="_blank">📅 11:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695072">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403128c4b6.mp4?token=VQdBBszge58ZmGZh2m3y3Ao1eGt9d4la9if43vELoaPZG9YD5Z8RNck0CieeytUBMqIjtX9Z1hnxlEuahQj4TROihFiur5i0nO6GFCOIK6oNA_zx4bal0FZSKDWlL6c1L8jgMgf7GdddYY435CKw2IGHEMRmUIjLum5QlgZ7bC3OH_gyRgY9npEzxvo2pB_bU3p_n91bUOV2MUCgFgncx-QoJXeRxgme9ydjyaVG3H93jH2hVo5FDyiN591vzJPUekBVKaZPL2ZhPZ1-lYdS9xmKaXYby_j5_VvKvpe6j-uhJM2UA5jyocddY_fdH0XMn_BqLL9ehpyS_qqwON1oGgexgPgA6DQPrcnmHHUXFlv-S6Rf1DX3cpbY2_AgtK59IxxYnPPbLPxJRcxPxHWOV71XnauofPUi4AhvpAc1XdO8XMp-Yc6YheIPHmg_YNWEFsZPVesixRx5YnqVcdn1CCLbWsFWpSJuVDyPXMKrTJSBUV5ptjT3Sg_u5cfEQ22rDE24MOuNlNwSNCy0U8Mvbrlz0gpc4Xfm-hAPOQs3RJ0vWtMsf8CrtvNRXbgjjz8D0GmWcI42PIHSPSzJcNxdcaTHFxWurjK5jpQLjnO5dcNJaUhO5o_OI3uNMqjIUf1wgb3IqxJ5aByCJnltfaYeX6u9ZfjpVjA1oWRtEGGM25M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403128c4b6.mp4?token=VQdBBszge58ZmGZh2m3y3Ao1eGt9d4la9if43vELoaPZG9YD5Z8RNck0CieeytUBMqIjtX9Z1hnxlEuahQj4TROihFiur5i0nO6GFCOIK6oNA_zx4bal0FZSKDWlL6c1L8jgMgf7GdddYY435CKw2IGHEMRmUIjLum5QlgZ7bC3OH_gyRgY9npEzxvo2pB_bU3p_n91bUOV2MUCgFgncx-QoJXeRxgme9ydjyaVG3H93jH2hVo5FDyiN591vzJPUekBVKaZPL2ZhPZ1-lYdS9xmKaXYby_j5_VvKvpe6j-uhJM2UA5jyocddY_fdH0XMn_BqLL9ehpyS_qqwON1oGgexgPgA6DQPrcnmHHUXFlv-S6Rf1DX3cpbY2_AgtK59IxxYnPPbLPxJRcxPxHWOV71XnauofPUi4AhvpAc1XdO8XMp-Yc6YheIPHmg_YNWEFsZPVesixRx5YnqVcdn1CCLbWsFWpSJuVDyPXMKrTJSBUV5ptjT3Sg_u5cfEQ22rDE24MOuNlNwSNCy0U8Mvbrlz0gpc4Xfm-hAPOQs3RJ0vWtMsf8CrtvNRXbgjjz8D0GmWcI42PIHSPSzJcNxdcaTHFxWurjK5jpQLjnO5dcNJaUhO5o_OI3uNMqjIUf1wgb3IqxJ5aByCJnltfaYeX6u9ZfjpVjA1oWRtEGGM25M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال‌ شده از مدرسه متفاوت یک دانش‌آموز به مانند کلبه‌های سوئیسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/695072" target="_blank">📅 11:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695071">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: غائبین آزمون‌های سراسری و تربیت معلم می‌توانند در انتخاب رشته براساس سوابق تحصیلی شرکت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/695071" target="_blank">📅 11:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695070">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر TV</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHe0x4aA_E_hi2zO1GO9D24bNcjEtPbXQ_ulJ1mUKkM_JibLk3KP1XjWTw2T7WLn9iOuinqm5TO_vbdPbpV-HsI___gxfkWhZNNwjrPh_tWl7_MWa6M8MAij6kNBH_PkngizWg9vFEprMj7joyy9B7HFazD3FkPSFp-h6P53xiGv02CAoqxNRmtbWCFhynghg9rFQ-nDkHVLWIdY0ORCMndK7Yy-d5VAfmp008gXEnwS7LJswuHseRaxn7cwlChenPkmS6u6FJcMzg7E2Omgpu-9Plt1fk6oce5ntJhCKC22EEthxuWwfUB4nH-AprTLz278sxxWiY3sCYBzYzsEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#اینفو_تیتر
| تورم نقطه به نقطه استان ها
🔹
یک شکاف تلخ اقتصادی؛ درحالی‌که تهرانی‌ها با ۷۴.۶ درصد کمترین تورم شهریورماه را ثبت کردند، ایلام با ۱۱۴.۳ درصد و هرمزگان با ۱۱۳.۸ درصد رکورددار گرانی شدند.
@tv_titr</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/695070" target="_blank">📅 11:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695069">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
قیمت دلار در بازار آزاد به ۲۶۵ هزار تومان رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/695069" target="_blank">📅 11:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695068">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سود سهام عدالت حدود ۲.۵ میلیون تومان
مدیر نظارت بر ناشران سازمان بورس:
🔹
میزان سود حدود دو میلیون تومان است، اما عدد پس از برگزاری کامل مجامع از سوی سپرده‌گذاری مرکزی اعلام می‌شود، ولی به نظر می‌رسد مبلغ سود بین ۲ تا ۲.۵ میلیون تومان باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/695068" target="_blank">📅 11:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695067">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
سردار نقدی: اگر آمریکا بار دیگر حمله کند، حمله‌اش به معنای خودکشی خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/695067" target="_blank">📅 11:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695066">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN9VCLhj11LouHTAvXxRwmbtz6Fd3ZySz9talThyz4HWYE5fCPLXUWWufdUpHm18mhYbs80d5-H7CVi48JfnjqFQVI54teHwz3HqSsllgYdALcNIPsl8MmABF8mOXbxqPRHzev6b_S8wy0Pxs4Fl_hvGVhGjrgg5quYy77TRfkyuJEkYOdnsAEOeojkKLJdRjHXrjHQB_zFUliLPtWljT1tN2-i0ZmxsvpcHiVoiA2aRgoOMNJ_dzSNoYLsvxMe1KLwXJ84woiXq6AvjBYXDoQOw3plpGpU0ZOLL-4jsGVnMSkYSXBZA2SPO5cAv95Edq9hIlnejjbBgWOJ9QkhGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهرهای رتبه برترهای تجربی همه جزو شهرهایی هستند که در جنگ، تحت بمباران شدید بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/695066" target="_blank">📅 11:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ca291056.mp4?token=FsPpUIbr_9p9H1DoxIY1AfW1L_Lr-ATThRbC1-h3njGOiQJClUG5-boMGYHkECuAxqUzC-cmSFCwkyqP3XG5Ydiq6ASvWBVsmuRaZ-fQaFr7kJngPV7jIMYoHrG27kU58bcBjktxJdxxjZD1u0NJeSDUPXTCbOIQgVyxcMkfJKD-uLhRVm_5vCJhQSj6ycrT6qkw_9iZCKUGjtDYZ5CzitGrO_JDu4nFqREbf2mmlzVZ7xxLoJXVptHM0WmNQnHPeDpAb8cid-X3llRVH6T51pGuT-KrNHPa6uQtOe4ca3y2yIMDU0aTGFIQs0_m9BVqZ9Gv1g_ItDtfOcrG8ip7jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ca291056.mp4?token=FsPpUIbr_9p9H1DoxIY1AfW1L_Lr-ATThRbC1-h3njGOiQJClUG5-boMGYHkECuAxqUzC-cmSFCwkyqP3XG5Ydiq6ASvWBVsmuRaZ-fQaFr7kJngPV7jIMYoHrG27kU58bcBjktxJdxxjZD1u0NJeSDUPXTCbOIQgVyxcMkfJKD-uLhRVm_5vCJhQSj6ycrT6qkw_9iZCKUGjtDYZ5CzitGrO_JDu4nFqREbf2mmlzVZ7xxLoJXVptHM0WmNQnHPeDpAb8cid-X3llRVH6T51pGuT-KrNHPa6uQtOe4ca3y2yIMDU0aTGFIQs0_m9BVqZ9Gv1g_ItDtfOcrG8ip7jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/695064" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
آکسیوس: آمریکا در «ضد حمله» عربستان به یمن شرکت نمی‌کند
🔹
عربستان سعودی به همراه نیروهای مزدور خود در حال آماده‌سازی یک «ضدحمله بزرگ» علیه جنبش انصارالله هستند، اما آمریکا دوباره درخواست ریاض برای مشارکت در حملات علیه یمن را رد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/695063" target="_blank">📅 11:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e8ca9871.mp4?token=GKHwPXTHTLift_sC3QrkwhwDOCcZYXYMgIGlFr6ApcDZjLr88Tzy4wC1FbpaqwzV-oztudUPhElgGFNDyk8UGxzSXin5TF8Db1QWiVwwV_lxMGmmJft8dsMCyQ3CNXIh5KfCda78THIWMef9vwklP_ePX6R2-A-p1DAdHTfHRxDA8KyAg0RTq-GJakxlTMFpL-_kC6AC87b7JO-oBmwP9El1-lH5h6jQhShoY0y7PsrWhFBrfxW9v5qpwxBXfKtuatUJKgwoEvDUNqeWVwqR5YMYVd9Rb3qJWDePUuEmuI15EVkIdUvFPsac-FbdQBwBmw3oRexuPNvqANHUtRB_7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e8ca9871.mp4?token=GKHwPXTHTLift_sC3QrkwhwDOCcZYXYMgIGlFr6ApcDZjLr88Tzy4wC1FbpaqwzV-oztudUPhElgGFNDyk8UGxzSXin5TF8Db1QWiVwwV_lxMGmmJft8dsMCyQ3CNXIh5KfCda78THIWMef9vwklP_ePX6R2-A-p1DAdHTfHRxDA8KyAg0RTq-GJakxlTMFpL-_kC6AC87b7JO-oBmwP9El1-lH5h6jQhShoY0y7PsrWhFBrfxW9v5qpwxBXfKtuatUJKgwoEvDUNqeWVwqR5YMYVd9Rb3qJWDePUuEmuI15EVkIdUvFPsac-FbdQBwBmw3oRexuPNvqANHUtRB_7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به دلیل حملات نیروهای مسلح یمن، دود از پالایشگاه ریاض، متعلق به شرکت نفتی آرامکو، به هوا برخاسته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/695062" target="_blank">📅 11:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU8dH6VAJl3owiOiFCO6te2Vj8RGxCRGQiUtmgi179GKFwL8SvditCtKVFL84JNnIRLW1gAoP1mH3XIrmoVkXLZqZ-f9tIAU1YpkkxBMXFuVJMjvKXuJzfZyTDnOXj8QzSF9_bH6OeYfyBVztuGwVLWTQd34J4lObxGFYMnGtWw5Tt9m39GDzTuHFLlI3_YF7zRHQf94v_cYrdQX9l7wIY7pnkFpLTKkqqS5P1wr2lwP_CitL5PSEwhy3HCna7ZbuP3pDp0m1ZtqN5i2nJhbSgzeYer-tqILsGckLM5tjv0ldYQGcDXCGgBsHxDWyj0colJ-Q6xmUBgkNgxCgyrfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس مشک حضرت عباس (ع)
به یاد حضرت عباس (ع) باش؛ همان علمداری که در سخت‌ترین لحظه‌ها، تکیه‌گاه دل‌های بی‌پناه بود.
این تندیس، یادآور وفاداری و سقاییِ بزرگی‌ست که هر بار نگاهش می‌کنی، دلت را به امیدِ یاری و دستگیری گره می‌زند.
✨
مشخصات محصول:
▫️
ابعاد: ۲۲.۵ × ۸ × ۶.۵ سانتی‌متر
▫️
وزن: ۶۷۰ گرم
▫️
متریال: پلی‌استر
▫️
طرح: مشک حضرت عباس (ع)
▫️
کاربرد: مناسب دکور مذهبی، هدیه معنوی و یادگاری ارزشمند
💰
قیمت: ۲ میلیون و ۳۹۱ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/695061" target="_blank">📅 11:21 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
