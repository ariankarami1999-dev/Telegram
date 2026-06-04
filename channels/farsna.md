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
<img src="https://cdn4.telesco.pe/file/UvZolvtp92K9s7Snp8sAbm3VdXwsHK1X8g861xxNnFrJKO5zB2w1FBOMyaOcuBENmxOck0gX8e-2mMmTyITPd3vhfk6tGDc6a933qq6u6t9PzTysfWHUj6UV3vZuMxC4OIOAhNMvbMU7mEhnDikGgIZEs34JSLiwMRqmklRp9k0ENEdSZD6gjkRQPCuiYStqPaZSc7EiP9W3o6a5vpZFdca_2XrPQokkvYVE51QT5rIEB_pclemtYkfv2YAItY8Hw_wv3Sj4z5sTkoEFTbJ05EoNZ19pctva_UKvVtASovS7hxT-kQUuAXcn5FWU-luEB_MKmKfFnN8jLC1llljrIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-439927">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb2f3d61f9.mp4?token=lrHQ4a7012ot3YIYaBztV_4llVyV_9CMCzDyovTN3AcwCmh2kAwHIDuGakef-r4s4Pg1Gd4Jm2dRE50H9PwXyOi7yS-Nj6y_Zy-qgtp4iJ935fogOl48pvKQw3mK6XNi4IieIm5YCpOYBfGTcOu9hJpB3c2JxHJdQHvWj22NuzrFoNHZMEQrv77HUHAvPYbqIMhj-3ZwzI_Lq64WRwFMcTTCz6Pk4UtuO3trXWp5XsIFVsMfSifGlEQjXare2vCK69xrh9PJGNF3DZCUJ1HrDmvrWEcm0PnWSJAVbQKKZJ7-O8BYidPVrgsh0BKgq2TxxjCvA-S2-IQR-PEbRFBx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb2f3d61f9.mp4?token=lrHQ4a7012ot3YIYaBztV_4llVyV_9CMCzDyovTN3AcwCmh2kAwHIDuGakef-r4s4Pg1Gd4Jm2dRE50H9PwXyOi7yS-Nj6y_Zy-qgtp4iJ935fogOl48pvKQw3mK6XNi4IieIm5YCpOYBfGTcOu9hJpB3c2JxHJdQHvWj22NuzrFoNHZMEQrv77HUHAvPYbqIMhj-3ZwzI_Lq64WRwFMcTTCz6Pk4UtuO3trXWp5XsIFVsMfSifGlEQjXare2vCK69xrh9PJGNF3DZCUJ1HrDmvrWEcm0PnWSJAVbQKKZJ7-O8BYidPVrgsh0BKgq2TxxjCvA-S2-IQR-PEbRFBx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور بینش بلور (قیصر) خواننده ایرانی مقیم خارج از کشور در
جشن غدیر
🔹
قیصر که طی جنگ اخیر مواضع حمایتی از ایران داشته، پیش‌تر نیز قطعه‌ای برای دانش‌آموزان شهید مینابی ساخته بود.
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/439927" target="_blank">📅 20:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439926">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be575cff4.mp4?token=rr6wtZk-V4IAggspYloYvu_vYr3BXLSd6WNaU0OlOtu_-Lsvl5qTPQ8VlWTAn5PycfERwo43dPaQqjvVOvGK7VP5wOiORu3liSHjhgypRz5O2fEQeHE36DDrZCBh0krD2ezGX0IueYC2D18roPVFzXOvkG62hDH-femgfB3SeGLizMLniv1-8km92-qqaVtyFr5Y2WQpMUdBe0L8T279KgEcqfiB3qbcRupExoz4-5YAq7AE8p2Djpf4a7EUD4mN_miaJf9_PruEd16uvy10gZNKI8gMawbPiIjBTmVS48RgpJ42VSy2GrsxE60H66o9iumgFtPk82FpbKdpdI_8sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be575cff4.mp4?token=rr6wtZk-V4IAggspYloYvu_vYr3BXLSd6WNaU0OlOtu_-Lsvl5qTPQ8VlWTAn5PycfERwo43dPaQqjvVOvGK7VP5wOiORu3liSHjhgypRz5O2fEQeHE36DDrZCBh0krD2ezGX0IueYC2D18roPVFzXOvkG62hDH-femgfB3SeGLizMLniv1-8km92-qqaVtyFr5Y2WQpMUdBe0L8T279KgEcqfiB3qbcRupExoz4-5YAq7AE8p2Djpf4a7EUD4mN_miaJf9_PruEd16uvy10gZNKI8gMawbPiIjBTmVS48RgpJ42VSy2GrsxE60H66o9iumgFtPk82FpbKdpdI_8sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش
‌
زدن پرچم ایران در تلویزیون آمریکا در دوران پهلوی
🔹
درحالی‌که برخی مدام از «اعتبار پاسپورت»، «ژاندارم منطقه بودن» و «جایگاه جهانی» ایران در دوران پهلوی سخن می‌گویند، تصاویر تاریخی سال ۱۳۵۷ روایت دیگری را نشان می‌دهد؛ جایی که پرچم ایران در یک برنامه تلویزیونی آمریکا به آتش کشیده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/farsna/439926" target="_blank">📅 20:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439925">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac4c1c067.mp4?token=DNsz8UBwlF6fZgJHTTUMNRch507uzAKi9LODuKUsCVh9ExW8wXSVxziBEXEhpIQiThAboKtsg-4qwRz_nsG6fraedaGLtv8ZBPLCBjwDA-zpyiam1HJPpU90cfQ2byEMLloOxOh0cHVvcUbsSkvDWwCUYYMy2VwWlB0uEJVAcXrlAfpLalqAo_HPcxioLanJK2yRLjOaBYATulxnzOjYRQAB_2CIaWW8-fMUMbPHNfo9ilhxD080kArZahyUXR8lNdn_X4hTwrmwNT61IanFQaYseuBCDFYO-9-_Ga_lbVttni4ZGOUg2jmz3pBkzObkDGW8sIcn5ZT9bZtlAwdA3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac4c1c067.mp4?token=DNsz8UBwlF6fZgJHTTUMNRch507uzAKi9LODuKUsCVh9ExW8wXSVxziBEXEhpIQiThAboKtsg-4qwRz_nsG6fraedaGLtv8ZBPLCBjwDA-zpyiam1HJPpU90cfQ2byEMLloOxOh0cHVvcUbsSkvDWwCUYYMy2VwWlB0uEJVAcXrlAfpLalqAo_HPcxioLanJK2yRLjOaBYATulxnzOjYRQAB_2CIaWW8-fMUMbPHNfo9ilhxD080kArZahyUXR8lNdn_X4hTwrmwNT61IanFQaYseuBCDFYO-9-_Ga_lbVttni4ZGOUg2jmz3pBkzObkDGW8sIcn5ZT9bZtlAwdA3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن عید سعید غدیر در حرم رضوی با حضور آیت‌الله مروی، تولیت آستان قدس رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/farsna/439925" target="_blank">📅 20:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439924">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ee52ee10.mp4?token=Trud6t-PjPM1VEboMzew8-ybsoEbs0lx3niAtcvdHLipm9cwpp7fX03r5snDL0LfccAmNcWaaJRVOp9tSTRYeAAvtgd7oX8SMjM1iQAf1CC-t8vyp69kwijslyfV4A7FRFI4ybO3YdoSsqA9ascfBkf26uGtw6rkumzAQeeWkxvBVgLUq0fxIV5tvkZqR7Ti4IdVjaj3AvpXCYPoVdElic9yz3_ufXMcQBePVZzxN_JeeiwhKCd-L_hDAee0-aNZAj45laUIv7BN5jA02RBy7l8vrSrdW7MPn4Y2jParuSOvOIbN9Xvt96wpSIKR0AH4pr0Sya7VhOvAGe4Ym55aow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ee52ee10.mp4?token=Trud6t-PjPM1VEboMzew8-ybsoEbs0lx3niAtcvdHLipm9cwpp7fX03r5snDL0LfccAmNcWaaJRVOp9tSTRYeAAvtgd7oX8SMjM1iQAf1CC-t8vyp69kwijslyfV4A7FRFI4ybO3YdoSsqA9ascfBkf26uGtw6rkumzAQeeWkxvBVgLUq0fxIV5tvkZqR7Ti4IdVjaj3AvpXCYPoVdElic9yz3_ufXMcQBePVZzxN_JeeiwhKCd-L_hDAee0-aNZAj45laUIv7BN5jA02RBy7l8vrSrdW7MPn4Y2jParuSOvOIbN9Xvt96wpSIKR0AH4pr0Sya7VhOvAGe4Ym55aow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو مجلس نمایندگان آمریکا: جنگ با ایران به هر خانوادهٔ آمریکایی ۷۵۰ دلار ضرر زده است
🔹
ریچارد نیل: به‌خاطر جنگ با ایران، آمریکایی‌ها برای هر باک بنزین ۵۰ درصد هزینهٔ بیشتری می‌دهند.
🔹
گویا آن ۱,۷۰۰ دلار هزینه‌ای که تعرفه‌ها روی دست مردم گذاشتند کافی نبود،…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farsna/439924" target="_blank">📅 19:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439923">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/munrrlSfTC9zZSP2ApV-KqydsphAwJGcIpK78qVgKTRmVYpPMvWbcCd1nGNsqPTg1MyLiJdv-jAEPZxuqgyMaZfUgc4E6r9Uz7u3OjtXbO0a5diKnjnccemL0nLUTW53HYZ0yQTZB8rxXITi7SDf_kI6WDm47jRRM1-QygU0GUYV2JGY0bTIANXyRnjrahZbM3IqrRqVnC6UUompj4MkceXfUHuWwEQtVPoaJk7x6IYD-8ruAjxs8pTZPjq_2_wnK-QY13RjTm7iRfjmNDZXl5RfYFWoAdBx2SUQEEk6FUVBF_U-KcfPv7HPDzNqu4KbXsbxkXPJT4EclMTqpAo4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بولتون به جرم خود در زمینه نگهداری اسناد محرمانه اقرار می‌کند
🔹
جان بولتون، مشاور اسبق امنیت ملی دونالد ترامپ و یکی از منتقدان سرسخت او، با وزارت دادگستری آمریکا به توافق رسیده است که به یک فقره اتهام نگهداری غیرقانونی اطلاعات طبقه‌بندی‌شده اعتراف کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/farsna/439923" target="_blank">📅 19:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439922">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba77baa767.mp4?token=F1NEKJxvGTmQTtYfidzNVyuGjekUYsRmLlL7ie9xsVu07ioPx-8VktGEZxC_kWbGABWW5iYUNhDXUmmtzf62Qf1mOUR3nXNTxksWy0n-PmmB83WIzWZmU2A9ZuxJ1X3QwEBggto0bA8VFh2BBu73jQvRLkE8IzqWg1dEIuI36JFvNJw3VTr6qsSisgPyL9X3SZcyodvvB6jWnVPO_tKmnv3seRrefG5H2cj84CTKDFhK5Cn80JOiDFBoAY_iM9Fjvb5rmjDkWRdXh3hELK2GPfF57D1MlxGm1CDCkUGPNWz7YoPuSDjAR5fs0jwsZ2ywHR6fVjOp8T15pKQG2LjhSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba77baa767.mp4?token=F1NEKJxvGTmQTtYfidzNVyuGjekUYsRmLlL7ie9xsVu07ioPx-8VktGEZxC_kWbGABWW5iYUNhDXUmmtzf62Qf1mOUR3nXNTxksWy0n-PmmB83WIzWZmU2A9ZuxJ1X3QwEBggto0bA8VFh2BBu73jQvRLkE8IzqWg1dEIuI36JFvNJw3VTr6qsSisgPyL9X3SZcyodvvB6jWnVPO_tKmnv3seRrefG5H2cj84CTKDFhK5Cn80JOiDFBoAY_iM9Fjvb5rmjDkWRdXh3hELK2GPfF57D1MlxGm1CDCkUGPNWz7YoPuSDjAR5fs0jwsZ2ywHR6fVjOp8T15pKQG2LjhSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن غدیر را این مردها دوست‌داشتنی‌تر کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/439922" target="_blank">📅 19:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439920">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1pLniB1SNy_ncyk9QdiE9OeiDWymQxZlXpSoxwUycJeP2LLjkuCx9b0vtPWfCUxTDC7kdvHtbcWeulinpZ45O-FO3k8R2N-Jehbbzjcp3O6PLJeB3wcKY8P4XaqmjUaopZy9Y7WnnFKo850Y84_MoROdCBmy-9wg3n7-_QIUQTGz3wrb904JW3rNh9izp3GYqOB22BSniZcxf8dRyfVlry5Z980j8c8gK3WJvaEBA_7mJBOUS_hCg4TR-MFWpnGRm9VPOwLmDjAqgWdphYFz02AB_J1ulTKSw1iaTFZrmlj2c7-2CQlnr52ykjLgQBE8pOSjTfjafa5ZFA1HsO8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIV4ZRszbdx2RB1wHe7PewHVz7wVfG5fr_lYNJyhiTgsZElIw75hh8EgYxUG5X6b-J2pqcNMPilJEWJksBCC3YXHH1wgne5cpacTaEGDDS-C3rzLlLtg0djMIRfgVPEvaSvN1xHvkLmX5r2S_QN0e7hrsVbCZLBGv0jc7D1xtOhPayGzOPsV_7I4dhgGSKdyNXv6GrKk8_j6INBlg1It6vSxvanLsz10PdYTSfs-9-iW7uGFZivrV8x_YlB-rKH9-PpR3y-MIiQSvOy9eMxKMsvQhB7H-af6L5xZB0Irv3C5sJghFgaQ8CL-T6TxfjrEMFy6eGvHNEUhur-v7YGBqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کاروان غدیر در مهمونی ۱۰ کیلومتری
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/439920" target="_blank">📅 19:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439919">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6ae89b5.mp4?token=ntnBwvnFcTlUDzTTaMHn2xWOut8raF4HJxIchAwuRm1zSHrNDRX36PDAuk-7uR-JM4_rc92IX89uADoy9bpt0skRdZbGQpHcACTT7ePdgdx3GZnRF4SIOuCF5gaKbQhL2uE7Sebb5stVkgoRCAknrGkX7XyU1yMaYxTeYg5g84J6THIMFqkm5_JsOxsTX18-j2S0ttoCdIUhEavNkOJoQRx0mw2KyxHY2umB2mPdNbod7qwu441R2QmBJE0IDKwKhFkP_APV8l29Tt_N_rJ8MwqrPCbQStba2ig8ds-xRtMl_ahgZZG7shWqQPhCdp5h7Hv3aHqPHTcWoZ7dI8d_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6ae89b5.mp4?token=ntnBwvnFcTlUDzTTaMHn2xWOut8raF4HJxIchAwuRm1zSHrNDRX36PDAuk-7uR-JM4_rc92IX89uADoy9bpt0skRdZbGQpHcACTT7ePdgdx3GZnRF4SIOuCF5gaKbQhL2uE7Sebb5stVkgoRCAknrGkX7XyU1yMaYxTeYg5g84J6THIMFqkm5_JsOxsTX18-j2S0ttoCdIUhEavNkOJoQRx0mw2KyxHY2umB2mPdNbod7qwu441R2QmBJE0IDKwKhFkP_APV8l29Tt_N_rJ8MwqrPCbQStba2ig8ds-xRtMl_ahgZZG7shWqQPhCdp5h7Hv3aHqPHTcWoZ7dI8d_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو مجلس نمایندگان آمریکا: جنگ با ایران به هر خانوادهٔ آمریکایی ۷۵۰ دلار
ضرر زده است
🔹
ریچارد نیل: به‌خاطر جنگ با ایران، آمریکایی‌ها برای هر باک بنزین ۵۰ درصد هزینهٔ بیشتری می‌دهند.
🔹
گویا آن ۱,۷۰۰ دلار هزینه‌ای که تعرفه‌ها روی دست مردم گذاشتند کافی نبود، چراکه برآوردهای جدید نشان می‌دهد جنگ با ایران هم‌اکنون ۷۵۰ دلار دیگر به خانواده‌ها ضرر زده است.
🔹
ماه گذشته، نرخ تورم عملاً افزایش دستمزدها را بلعید.
🔹
اسکناس ۲۵۰ دلاری با عکس ترامپ شاید واقعاً به‌خاطر افزایش قیمت‌هایی که در راه است، نیاز باشد.
🔹
وقتی به این اقتصاد نگاه می‌کنیم، چیزی جز شکست پشت شکست نمی‌بینیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/farsna/439919" target="_blank">📅 19:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9a47b71f.mp4?token=RBKbybXrrTd7PnOETRNGHUSddVCYGw4d8ey8jJa1vrasbJCcAnxNv54v5YDQU4aC9yLmAF0w1CoQT6VKPcZBgzbsknfhJCZP7cigJmOEobeqF6m5W3_cT6NWG722XXfo8ljK7LF6hV_kaPffkBbUl8dw3-KJ773AroeoHDH01MDZEcKvWtDcsJ66XoP_ceMD9AmJhEyXPrg4vSto2oPvwyibi1Q8BU8NEnuNwrBv04igNoociJ9wRlBq434yDa6KalUSzjeB3n2BMrevV5x7OtxOb7huK9gp0EHUOYZ1y6c3hDh39J8HU1qJJmisp7yS2H10ZvUk3hkX3iZ5o_6HCgBAZq-D3ruADO73hl-b7ypqccWXsnNSRB4i7T5E5flA80yimJxNlzkRFeG9AXLrUXDp91Dbqqc5txA8Fd34do-ftfZJ1y8svxnhjDKc6dY48DbbScOqTyUS2CHIp3PQ_pimckeakBzFOYcRj91KSbMOi056M3vZ4XsLZwz8yCG4VXYFo6834frTVQYjc-1ITKkO0KZqKKbLcjtM5MHJQll6_Zi9BMEuIalytSDFdYTk9hhwCJuQqm_QQpfqJE8T-9vlxFVpCyTL-wt7Tb8L6NjK2yUsg0TKDEV-dqJB5x6BlhiTHrqm-8x3gxejbTdFNk68tnL-ocS5ECEnv9mjm_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9a47b71f.mp4?token=RBKbybXrrTd7PnOETRNGHUSddVCYGw4d8ey8jJa1vrasbJCcAnxNv54v5YDQU4aC9yLmAF0w1CoQT6VKPcZBgzbsknfhJCZP7cigJmOEobeqF6m5W3_cT6NWG722XXfo8ljK7LF6hV_kaPffkBbUl8dw3-KJ773AroeoHDH01MDZEcKvWtDcsJ66XoP_ceMD9AmJhEyXPrg4vSto2oPvwyibi1Q8BU8NEnuNwrBv04igNoociJ9wRlBq434yDa6KalUSzjeB3n2BMrevV5x7OtxOb7huK9gp0EHUOYZ1y6c3hDh39J8HU1qJJmisp7yS2H10ZvUk3hkX3iZ5o_6HCgBAZq-D3ruADO73hl-b7ypqccWXsnNSRB4i7T5E5flA80yimJxNlzkRFeG9AXLrUXDp91Dbqqc5txA8Fd34do-ftfZJ1y8svxnhjDKc6dY48DbbScOqTyUS2CHIp3PQ_pimckeakBzFOYcRj91KSbMOi056M3vZ4XsLZwz8yCG4VXYFo6834frTVQYjc-1ITKkO0KZqKKbLcjtM5MHJQll6_Zi9BMEuIalytSDFdYTk9hhwCJuQqm_QQpfqJE8T-9vlxFVpCyTL-wt7Tb8L6NjK2yUsg0TKDEV-dqJB5x6BlhiTHrqm-8x3gxejbTdFNk68tnL-ocS5ECEnv9mjm_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای «علی‌ شیر خدا» توسط خوانندهٔ پاکستانی در جشن غدیر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/farsna/439918" target="_blank">📅 19:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439917">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee027b35b.mp4?token=D-d5sLatUTIE9u6QDZTBW3C_uOPxpHtHAYSZjbKatZg8kY8mlDnpyYXSGGJxcz8ScLvP6vMKw0wFn6RifLUz11Niek26BXOXLruyobhnvVWVJTKl30g3eFAX9PRP32baXUMgmLvAm-Nyaa9YlCwG38AO3wBjvbxLWfrBdoCQhRDTECz94YYh3R7ms485XFvQdLopRlJby-R_FMBneOgprl9Nwc7tUqEaYNzkvenBZSl9AjHdhv2CP6rUgEEJzRo4zqOINpMtkZM3VKV0e_PS-3O-H2F5dCqQcPFiQsc_N0H_QU7AFwGbrbu19MZTeh6Awg1cemZlsZUqHjO8vfv_soWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee027b35b.mp4?token=D-d5sLatUTIE9u6QDZTBW3C_uOPxpHtHAYSZjbKatZg8kY8mlDnpyYXSGGJxcz8ScLvP6vMKw0wFn6RifLUz11Niek26BXOXLruyobhnvVWVJTKl30g3eFAX9PRP32baXUMgmLvAm-Nyaa9YlCwG38AO3wBjvbxLWfrBdoCQhRDTECz94YYh3R7ms485XFvQdLopRlJby-R_FMBneOgprl9Nwc7tUqEaYNzkvenBZSl9AjHdhv2CP6rUgEEJzRo4zqOINpMtkZM3VKV0e_PS-3O-H2F5dCqQcPFiQsc_N0H_QU7AFwGbrbu19MZTeh6Awg1cemZlsZUqHjO8vfv_soWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین مهمانی ایران در خیابان انقلاب تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/439917" target="_blank">📅 18:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdtj5s6SEQcwYZy-JrVA4quhAo6nDUzmU9G5vW3IXYFex5dAcRefZ89U4kGhjoCn9w7wJcR9w4l9WI9OM0pKKhwhrjtGZj-xWhZlTh5k_HR5SCSxIgAZtSzYEt9usbJUQT_RWW-0EGli158XTuXVaZ-u6L8DaHpHjITOMTPHIAsx1Z5eKQNgzKnlqKSm-4zv6MYhM1AX8R2CPADjx90UdZvkmMQPoLOEsskRHIEKQY9eqAKUCcw-0voDbXwKmAnBEMZVOL5CHByaveZKOXhT4GjNJ4L8dVLQT4RuCU2YmvcNa-ollmOYytmg2VW5CaOIZm3LX0TkZwgomVaBfMZ04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gs8Se5JkfBpS48NW74h_e_4CryAy1jvVO6TmfN0nZPquqMG1FlIqBfJkH5EIw2gftecyrf_RPsgl3EGBKYaTeetGloaK2nkJoHujZQXVKkIHWY3DBooJH-lWtQ-_GTwaol9Oc45lnAdRIQNvrasdeEs_caUJZEaAz04SVZmoHKnvkPevICLRRmabCctg8wqjabMs7boTgGzoyfeFZ2mXbeU4snY4Fl24O2gFf4u4VLtIcILvG0pqJEHrjuukGQ2uojvXLJt45gHYtKSUbpDbRLQqndlAbkm6DMYPXS-onNNwiuItJd8YLIRkrTIeXPpyCvQ4aqJ3danH4vopnFVoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEDTKhN4ZIpeyHvfCbgjlQ1FqAUxJAvi3ddGcDJkc9xW3hX1dgtu93oTL0yt285kRx2jNO0IYw8RCcUrwwfVb0MZC4TFq23U6o0UqlOsprNo7nnVf4EufXhtIi4A1-gw4PEa4SXdvkcAEB1PzlZzC4uEG9E4s2AIBbgIeQD4Pz5z7bxHbfH3YF5BG5RZGDvjif7zmxDRTGuPvVXVuymb2AnQVpeyITZxwtzsV5xyH4jxwi-LMjHJxIVAZMUIX_6iO5R95O8PraKLcEpoT0k79vIJnp3JrE7nUE7q2ajozycLopXPgWjE5gtGMWxW6kY8jbLqc5igbUcZRy4gvxIjuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nd5tjCNWOwAgc9gfg6t5kDOl4MHd41qnkTcnzBV2GoalAfqqETIgX-V2bUrzJaA1wNIoU0ZBIFHxWs7jSYdxJa32ym2wvRQfbRYIzrtXst9lzCM4Z8HZWcnb5BPyqNxop402SuaCNhcD6CVJQgkGECpPyR0prPjGQG1Ax-rxjojRORUM-1qowkLDeqkc0YTniiIN7xHTOodYA6OJktBYfZxAGQwuDOjLU6Gr55RQTVaUpIRN8kZ9dRdDrzKS68XxsUyK9KMTCPg_YDYKyyIYg7MEaupJZ8uvUJAFOyYvtzSAuD4s63Wjeuc42M3ZcWbL-FTrDa5xom0BxCJRUKKUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVvYzAPzASH3Etyb0lelrU5TiihKOIe-hDoCT93k_YWB1wQkrxCiqItqkyE5XJlJZhD_16UX8OV4O96NK2OdS_W-KZp0c4Ty3lyhT4aNHbVyCzsVG8Z9jOzTcI_6sVAvVxEeS6eiyysZT6EUZaqyFSBFiLs1cDJQrwGltWLbKYloRfpe-E1hLpbPcZs5pNhWuUpIpbKnnYRqRA7FY6tZHxhP6MPBZfLw6B_vogJqdlAAX9MQNmVudQ3umYcuWNjF2rjl53X9jEIxWBrfYJfZFlEa1eU1pL90AZF8sPLWGx-Lh2Uhd5wNQdL3foTToI9PU10LKXSXX7vgzdmhl4yBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIt8kwZT-65u62RLu5Eu6HgcjPA8JuezEkd-t0goVu3iRXL2Y6OzhCj-NBxwvSckbhRBLmJAelazs8No4qCro0RzilM61gNdgyP9y775WDzA52J26DJ3ARRktDa-DoVo6oafPnra84x7CLMGIlSjyoaYsc_lmtfP-pEPv_Abo0CbNKV98P8utVhyFyH46nmtAINZDg9rA-RF-renAOkb-UOzrXTOzEEjFl3xa0ucPT_xtvHfGzEqfHrkMq1IDr_4n5tSG4VapWM8gQCsil_NYNqfyiVQ_itTwfnhtgmaizRQJvk0psZUIkoxzMIrZNqF33HfsCw5LlgWjdzCcHAbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLagfabkjKaKXIUb5ubcUUfq9mgbuJS18Wp5AJB9AkN9qiZR-SkXxROqT_ADqILCMFtaZR4a2dwoh1-NhKw0C1o9cC5PMkQBkUxAZ0fVQ_001Ib6dhjPeFut3OyZJvjse0TDAZt-8WyKX1GX-dAOrHhMWGEblWeDlRMB5l56yYih1Zc5-7J_IQFeTzzXnqhY7OwCNGGTkYfdo12K8vzXZm1mO0sZa-8mvqRI4yzg0dcLmYxr0kI5zdKueKBod7uEQOk24RV1ekLag913K5mWcNQLO4FhWnicBfReKB87QbR-PEhid1r-AyNVdBZjXz5iDREz542cplh2RlCrNcNttg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
جشن ۱۰ کیلومتری غدیر در تهران
عکس:
زینب حمزه
‌
لویی
@farsimages</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/439910" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6709cecec9.mp4?token=oMafchHvV9hL9K-CniVh7mHOpwpGZE6a7RLWxMfqY5vRSCOOfS-PtTxTLTScjXXKPA1gK-yAXwbiqPocpJF6BDAnzOUBGZdZy03IZ-ig3gfcCzf5LTcErktgUdu3qgTNxONt8mi43O2Qtsdl4BaYI4EIkPZw7k_og-EZbY6-T_9tn5eUop9dgCMF4M5Slo5gIN0-8bGNMqDyJUDM2WeidCKx_rkoWvpo2P1LGyS3EtN0MeF0DXgSNXNk6gvFqZAJzrIq1uhCnrdUEVg1moNggjfnetS8YpuM8IfigxZ4F2o598RVl4GpFQmBLybJ-cWiHuuSpi1dpb1Cw0r9wSvmlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6709cecec9.mp4?token=oMafchHvV9hL9K-CniVh7mHOpwpGZE6a7RLWxMfqY5vRSCOOfS-PtTxTLTScjXXKPA1gK-yAXwbiqPocpJF6BDAnzOUBGZdZy03IZ-ig3gfcCzf5LTcErktgUdu3qgTNxONt8mi43O2Qtsdl4BaYI4EIkPZw7k_og-EZbY6-T_9tn5eUop9dgCMF4M5Slo5gIN0-8bGNMqDyJUDM2WeidCKx_rkoWvpo2P1LGyS3EtN0MeF0DXgSNXNk6gvFqZAJzrIq1uhCnrdUEVg1moNggjfnetS8YpuM8IfigxZ4F2o598RVl4GpFQmBLybJ-cWiHuuSpi1dpb1Cw0r9wSvmlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نذری پیراشکی‌فروش معروف میدان انقلاب در مهمونی ۱۰ کیلومتری عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/439909" target="_blank">📅 18:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439903">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScsCB36PDKIE5mgcibBsuPeXK3R5tmJ6jCK2zFSqC9Tpe27ICJFqLQX6W3xZuFoql-oeTvDPbFevWPR_agVVlyFYAk4es9R_M3_8GNFKjEHggtLgJ6jPlLq2o9EAjjOSHDeVeOOmE_gbgF_y38JCKh5m46HBlQe04ou5DBxGEHhjyPthd_vPVN0YiIXu9C2hVbAf_E85UH3jX-SF49rF08ZDsmsmQv6ABRL-bNJs9OdPMKMtV5MrteGAs_mDpwyuWyMAhXV41nx6_-6WuH4GExi7bfbJCBEJoP4Ltln1g4bzDCNZ-z4kFXwOxy-yMhev_Q__Ba_iwpYXBNbbfv-uTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UEe7ko87_2qHL-6ehXmlPkkWHS97-4M2IYq4WUPo2tPzZVHbUQELCDb9_klThueTdq74pxGC5wF2Gh0Ti6_RQmfcJx3HYPWT9uXQ9kDLQYj4vSZGzOTPrsvHy_FLdDFHGOBsZMxHG1sCH8NRJ_Tj1AeqZyfo72Yl1wMSqkXE1TGXtCBiBiu5sUFf4KF3AMLxNIJUqul2DU48J0bX9cMY3NJCAhnr1NFlRkAQiA4nOQ2ajNc2jmfEOgpuS0EwRiE7YJ9O--AepTDP0WZMNSebxTzQBUfD3l3AcaCL6UnEJhR3vpXC5jSGdT-LOAMzS9QupdrkjWMgXcuDxuLmwytqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVAhK609W4Xo8joDoKmha6MteaJlkjorWTrOuVBIL6uOmSVNRAGN9tzJPGpC3Uzh92-a-W13smIH7EcrwsV5r5f-CPgkIJUEvQXN9VKPxcUA0n0NAIRnOVah_PfgEfrlQPmB4jorYE2vGF-WVR7MYKpsop9sJl63lx9uiVq1jw2u-yaEn-Ze0Dp8ekdUYuIiHoZh6CU1uNV1rpj7pP_aShmKpzqDe3Sp9GvND1nIc7o0jZSS8WiArj9L9fYWR1R_X9w7RWIy0CmwSy6nZb3_ITX_tzquOv46btI4S8XLas7lh5csN7asUCPoRiRab2o0EqjjAHxmNb1mLMeX6iM-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDv0GEItw6qylbYEnrYU92l97kV236RjWNiLx8WeNVcjDaoiYfsquh0jq0-9Vlysa5hkdFkGbOTJaSCLYl-11ua59B08K2I4aQKCM6heilzmdd2OnnI-KFvzCuKwAUEAe3rgMiypDCeUcNJsvRjIz-Uh9SYW-tYV1etmaqAnkpiYIHj5-33JxT6CVAmRllcf7LWveK6QfNwYqXUFOxrhuuiuM1t5Z7P-kUCbvaQ-xP2CXQ_Blvpik9aFA4S51oT35YP5XEC48RvxVfd5DMqIo5Z1ADqSH4Ct9GfNLFkwuJ5LsPnOY0Fd0-UptQx__2560oBZ8UILRr_ixveNMHnB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6zgMrtEP9S8tkIGQtMzsROfEwCElG0UvBXizZYT_DW9eP667d6tkCaIm8P_-Bq8q4bowpDY5gE07bNIqBr32a2hm5KPHM64xUD4irDE_ovsgQbaZAR5FoQDMBILiOzGB5Far6jMxGUjWvizLtmlzYjAZP54kUrRlP0dAUONVR1oh2SK9tGs442PswzuBWG-u7dL6y8S-P0E0ZeTgHA2n372kvvptxU1Qzz9jdcuvjzBBbtz1A8KGWBQTub71MdGp43dAsg0tWhj2EwZnDdaxK2ZUo0wP2fpgbFPDvn709d_ttPkoI4Q69INsRe0g_ygX6ivaawoBBVjO_J-WTGyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2dBkJ56JabA5ozMqT8CW9weeApwKR7Gn5-xEH9H9v-7B2EzFlGsp7pPno3ivsJRe9DY-DUMIkCA_00LyJIWoLjfQYgc8ANTt0YwoIOyAyjmFUz_Yj3WFSrdcVxDGbV9Ezzr8YT2XRcU8TzVtVJ4ZKV3k6vWNQi3z4lP1td8Sn4i7MtMfrPGNK83SeqOrERXVx8E9Bd55_BENpjmBz4sbGvWcK97TjefdQlN8jUs27bvlbQbDSX5NEXbSHCRspCffD-X-08_AySyhG4335uHhufEjGBKZctIsnilPk2lmDJGZrV18YPqcxbo0qrR-6IhjTmi5hfz_OOwmsGsaki5Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر رهبر معظم انقلاب و امام شهید امت در دست مردم کشمیر هند در جشن عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/439903" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439902">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
رهبر انصارالله: تهدید دشمنان همهٔ مقدسات اسلامی را هدف قرار خواهد داد؛ از جمله مکه و مدینه را.  @Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/439902" target="_blank">📅 18:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439901">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea95831174.mp4?token=KDQr13i6ae9wm0ZoDokK3zBcJj-Ca-Wsnft4ZqakphYm3mDsANsB2CsVJPiMVZIt559QZ4-sByGajb6-bYPW0TmuJzmENJSxyXVoOD4tTRXnMwQgrpBBl5J7hQ7zvduy9uLpgaOFa9vACPfaSAwEv5XxL8QBGsqebe6Jw4Z6cCw_DpjCFOGQyJHwZmkNEWukHXo01a0brYiTxl13uSAm0ahpOag26VoKqT0RyLPRyQe42Wz6CJ8dypSvvb8lf8urMH2OroE9X5LhKBjkXo5iC3WQaLfaPgH3Rt5b-c2Y9yd7e5V8dRFR8T8v870FAPD5lFOA7MivZsWoo3vyIMbKjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea95831174.mp4?token=KDQr13i6ae9wm0ZoDokK3zBcJj-Ca-Wsnft4ZqakphYm3mDsANsB2CsVJPiMVZIt559QZ4-sByGajb6-bYPW0TmuJzmENJSxyXVoOD4tTRXnMwQgrpBBl5J7hQ7zvduy9uLpgaOFa9vACPfaSAwEv5XxL8QBGsqebe6Jw4Z6cCw_DpjCFOGQyJHwZmkNEWukHXo01a0brYiTxl13uSAm0ahpOag26VoKqT0RyLPRyQe42Wz6CJ8dypSvvb8lf8urMH2OroE9X5LhKBjkXo5iC3WQaLfaPgH3Rt5b-c2Y9yd7e5V8dRFR8T8v870FAPD5lFOA7MivZsWoo3vyIMbKjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نذر گلس موبایل در مهمونی کیلومتری غدیر!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/439901" target="_blank">📅 18:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439900">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
رهبر انصارالله: تهدید دشمنان همهٔ مقدسات اسلامی را هدف قرار خواهد داد؛ از جمله مکه و مدینه را.
@Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/439900" target="_blank">📅 18:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439899">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۵۶.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/439899" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۵۵.pdf</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/439899" target="_blank">📅 18:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439898">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d459ca0d.mp4?token=baC4Bhb8CQPTTVgIS8TRtzQCjsSNWpR-6xxtVCJSB9_GNqlhiv3IsJbQ2fRLkitfXZv-bMAvY_1EPiiOxU2RQYfESK3DgDSMpcBAkMTba3mkuTf4Wlrre4bXcPG8DmJTm2fkBZPIAiFv7dsmkjSkAnUmzSOd_NsxFYfTMVFDChlEN5135EQ8SjSuwlp1MZOHd7dC4vTq1gKoamXihUiywMhF-9EC2vF--YY8FFD_2P5s6iNRxZg9ShbN5cahGMJVU5-IjJtCRxbtPyNE2brpu7kMGdnqMAINdKL6MGzow5fK1hlKlaw1eOcbyB5otBOoIZofOQVXGDVx4h0UFWWjPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d459ca0d.mp4?token=baC4Bhb8CQPTTVgIS8TRtzQCjsSNWpR-6xxtVCJSB9_GNqlhiv3IsJbQ2fRLkitfXZv-bMAvY_1EPiiOxU2RQYfESK3DgDSMpcBAkMTba3mkuTf4Wlrre4bXcPG8DmJTm2fkBZPIAiFv7dsmkjSkAnUmzSOd_NsxFYfTMVFDChlEN5135EQ8SjSuwlp1MZOHd7dC4vTq1gKoamXihUiywMhF-9EC2vF--YY8FFD_2P5s6iNRxZg9ShbN5cahGMJVU5-IjJtCRxbtPyNE2brpu7kMGdnqMAINdKL6MGzow5fK1hlKlaw1eOcbyB5otBOoIZofOQVXGDVx4h0UFWWjPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم در میهمانی ۱۰ کیلومتری غدیر در میدان فردوسی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/439898" target="_blank">📅 17:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439896">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7hlJ920FkWPkPP3f4yQ_9dH4k-YCharBa_bsTQIbY-aAvHhAbSkRaHhsyCRJFNbX2tl67PdVGWjRcG49MGfuu1IPq1-YCbQYpImlmzfnVjcQhLYFb6XzHUB0l4rZPC8DSKa2DsJpCAixpZS9ro81D-HxzTTwNno2BIbZ0HtMeOwMpsctU7WcUsVBdrNLoYqYyKQBoSsYmBa3tmO0pTRB7-b5LaKcYa20YAdr9xGS3WruolYBdc8H3a5aqUb2E7jKmiS4ym3jMAi1K6ecRaMyBGYgPeEZmi331259yLcXXB8LaINfe7MQRxNnvFZWXMhYtiO5i8fPyWKPxoASfl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۳ محور مهم پیام امروز رهبر معظم انقلاب
@Farspolitics</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/439896" target="_blank">📅 17:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439895">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
خبرنگار شبکۀ فاکس‌نیوز: آژیرهای خطر در شمال اسرائیل درپی حملات راکتی و پهپادی حزب‌الله به‌صدا در آمدند.  @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/439895" target="_blank">📅 17:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: شرط اولیه ما برای پذیرش آتش بس در جنگ منطقه‌ای، آتش بس در تمامی جبهه‌ها از جمله لبنان بوده است.
🔹
دشمن می‌بایست با فوریت حملات خود به مردم لبنان را متوقف کند، و سریعاً با تخلیه سرزمین‌های اشغال شده لبنان به پشت مرزهای بین المللی عقب نشینی…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/439892" target="_blank">📅 17:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439887">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2g_bUz16422uWcIHVgA5K-BbuuiNCIaXBv3T5-gpdSSMDZoVM586ciwoBaA1XPVYf50EyjCCXQERa6r_e59VmhcW5JhAN0vAxsKjZmsglysaB9Mr30Mof9H63rA1oRjmKNqui-b2F32dC7JLUNQ55a-BztMFG0_i6Yr6CJlM-zLpIxKGPI9J76GmQ1rpycRgPt5NNq4YOGwRBrb235HhxauPcCYhahD1Pp9wC6F-oERANqqYWyil5EO6wwU5mliSMJSL5_E3KIA3qydWBXl8rzwLWd_Y1_cK2qwTbTK5s6PH1aIzI-VyJZrvJw8QCcSj7mulZsLfWbiTJBJRrwaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5O0TG1Rnuck6N4ubJfUYbxLu0Mv5pBxPwjWmV85OS2v_v0P4_uDWVo47TW8PKHgzQgRuX8gQLoe0BFVFcXmvN6r2WAwSl8lWZp1rq1_CDPP7hYjonexa-hfSFDFav_aSzIbwSrA0IXF0-WwnAhcPG2De-HRJSBYFvCH5ACaPwOTZfwj8WTxUgyYuyi0wCeYs-yO-F9TMeFfRrnlrQJu00BtBTAa5OY2RxJQmZgQumtVyosm5d4uV0w7BhxvQ0ogMWs1YC39aYb4PYWhThCum1PBhEXkxUk8GDhZIaYi-PZA7c2KO7Ky8K4gvBKLnLH6dLhW_ajuVTuaV6FaDXx-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQyjHqaxnmVjthHex3VBBoR9pjkPnNPJJikO7q_Y_D4K2xNl6-ZhVA_BkCicdVmSQYbDi6HbjjWe-GuIxfFX-2DR9bL358Ickc7Y3udJp1K-9AHKIlbPAA0o2AL-YrQYIrg6nuNTUth6ZjC6_e8Zl1eY5qR-5i7UP-S36pMKOD0otcK49EOGsIt7mSZXamIDudQlHMgiI6babEeHTsgbWUfphr7U71wyWu_CD8h8x16w3bSJOIBZ9CDY8UZA267Wl4qrEEiuhyp_5heiyXCcbwfmc_5uG2adztow5GXBBlup5yoStbGfhWLJ1juPx-uUK3xXtPHaW7A838G-dKcjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVTeg1HhxKggAhi_3g4q7g21CuYJfqwZHA_JC67zCt-5j7uLAY1oE-G2ITeLV2DoNPRO9D2FUVblrIAk1crGNLtgn6YqPUSql8ofnEzqXCXT1_GvMVVzJwKSHOyxcjt1H2bYezJ2e2qAO1OdW-22oM8Unwl1DPlNSpuksO-nzT2EVOr4hMzxcFTHU3_ziPxCWW8UQcamFU49DpsScr_WB72H1JtAgg7L5z9MPBqObzThWt9xPZ6ifEsvhCYqAJzjfNpxXzZmlOz29F1Jn-svW-1atC4vIygl53T_fdYye9bA63tSKI571JY2LBd6IF63m8cTDo3GD1cvjrCnEA7Ftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHvZoftfE7jZ9Ml2x_O1Aqx3WmOFJja-vTRzrrgk7Ine-9r9TOC1WShK8ehkNQ8_vyswlMP8uN7rEodz10jkR2vcvOt7WYnfTBMJzfpkHlDNbCUNB_5Unabcbfj4jcslqRLlkX-Bp65zWmcWmXL163TIH7z3zFbWG5jnCDctpzUy48-sAw69iWKe8OwphsYhrLD5K9eWHZ_2aSub9O0V9nNmbpBlI_UdIRNqoVu3mwBAeRfCtinf7k585_dwo3l55aDmbL4SBEhrx_VzDoDOtiGpzW3Y09M7SxHtHWxxvi7RrBFrI67T2-_2N8vxas1ePH0BFZ5HqIWZ-34DLqZr6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عید غدیر در حرم امیرالمؤمنین(ع)
عکس:
امیرحسین ‌رستم‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/439887" target="_blank">📅 17:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439886">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: ملت‌های منطقه مردم لبنان را تنها نخواهند گذاشت
🔹
ملت لبنان اجازه نمی‌دهند آنچه را که رژیم غاصب نتوانسته در جنگ به دست آورد را با حمایت رژیم کودک‌کش آمریکا با قرارداد تحمیلی به دست آورد. @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/439886" target="_blank">📅 17:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439885">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
سپاه پاسداران: دشمن باید با فوریت حملات خود به مردم لبنان را متوقف کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/439885" target="_blank">📅 17:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439884">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
سپاه پاسداران: دشمن باید با فوریت حملات خود به مردم لبنان را متوقف کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/439884" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439880">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f91e90be.mov?token=JB_Dvvn-r___DBAHd83cXyVQwHtQZfI5zvYf76W90ntI768atJjxFkWNtpXHn8_TktfVIfWe6KN24C0xmtzMQb9JTFVPU2Rqf2pSv6uzPeHtjl2rTSDLSSHE3Rbo50HWqSOlLthcTcMsav4GDgu70hpdAVkDdzkYT2I9i6Jgdo3BMiPZIrE2iUeoj9EnWFbS-D-bJLLHDUj7XDqP7U6gnD1w8hoPcw_oBdggiujzqMmy9fovsGksqu7DS-n8dvSQw8uAeA6Cn9ourSGcdY805epQoC17S4aIfsBB_p2G-3hYZbD2ewph-87EtVd6TpoFZA3QVdPBIjzeC_Z_Xx-nxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f91e90be.mov?token=JB_Dvvn-r___DBAHd83cXyVQwHtQZfI5zvYf76W90ntI768atJjxFkWNtpXHn8_TktfVIfWe6KN24C0xmtzMQb9JTFVPU2Rqf2pSv6uzPeHtjl2rTSDLSSHE3Rbo50HWqSOlLthcTcMsav4GDgu70hpdAVkDdzkYT2I9i6Jgdo3BMiPZIrE2iUeoj9EnWFbS-D-bJLLHDUj7XDqP7U6gnD1w8hoPcw_oBdggiujzqMmy9fovsGksqu7DS-n8dvSQw8uAeA6Cn9ourSGcdY805epQoC17S4aIfsBB_p2G-3hYZbD2ewph-87EtVd6TpoFZA3QVdPBIjzeC_Z_Xx-nxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی کودکان در میهمانی ۱۰ کیلومتری غدیر
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/439880" target="_blank">📅 17:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439879">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae53733e32.mp4?token=aUF_mqD9sD4UGnDF8BOgB1VQX1rONCtV90VAqUQJlmwhyhQ1aYk-fSnjdv48QrAyrFis6sO7AgK97ohH0mVygm3-5tTPoewcx3bO3H74NGn5w0LvEiPLSsPxgvwxzY0cbV53yZ55DfHn3xSUx9ADmwNOHBUQBnAnQ-bgt9iiOuRnzAd4Tipf6PYRCPeHzxzqLHi4OiAPedcF4RpHwQXvOta9FRsU8-NO4RnUzEX_6QlUeRmXv-aMBlRWX8R4cfonhftnlkQs17_ubO-Lqnb0p0lWYYd73dUMt5xyIclm1MmPM94iTVtdELHTscJ1muU5PJA3cQc07O3ZjGWwrxjimg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae53733e32.mp4?token=aUF_mqD9sD4UGnDF8BOgB1VQX1rONCtV90VAqUQJlmwhyhQ1aYk-fSnjdv48QrAyrFis6sO7AgK97ohH0mVygm3-5tTPoewcx3bO3H74NGn5w0LvEiPLSsPxgvwxzY0cbV53yZ55DfHn3xSUx9ADmwNOHBUQBnAnQ-bgt9iiOuRnzAd4Tipf6PYRCPeHzxzqLHi4OiAPedcF4RpHwQXvOta9FRsU8-NO4RnUzEX_6QlUeRmXv-aMBlRWX8R4cfonhftnlkQs17_ubO-Lqnb0p0lWYYd73dUMt5xyIclm1MmPM94iTVtdELHTscJ1muU5PJA3cQc07O3ZjGWwrxjimg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه اصابت پهپاد انتحاری حزب‌الله به خودروی زرهی ارتش اسرائیل در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/439879" target="_blank">📅 17:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439878">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv5_s2yNaj70BTsG1n3QrLpHReo2j2SBRtybFvRil6A05Adrrykfa8K68uay6ota5d1FKAHLFxNVrvNI4kosS8Bf2orWOcwSVCaFiib58XG41UGiTlckNDjLxjb73mYqkL-8-FRjarVWvCWzfZ9jqJrIDyHdmgdanT6yJY8XmsiuMpV-82qvzomrmddSeGhHWadgHKMVemb6NwGuLDbSx4NcMbRZLWkj2SurBbhD_QVp7JuXvXtUrJ3LkF4gC7r-odQLuw2LOKY9Q5KmDFFD6jceVj_rgWHowXl0Gj5rBeC0EMLKHsz3pL2IzAnGdfMsh_aejVmSqXI-YpR7zFryqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: حفظ وحدت، انسجام و اتحاد چارچوب و مبنای نظری دولت وفاق بوده است
🔹
با رهبری عالی‌قدر انقلاب تجدید پیمان می‌کنیم که از این سرمایه گران‌سنگ حفاظت و حراست کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/439878" target="_blank">📅 17:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439877">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
جشن خیابانی مردم بندرعباس در شب عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/439877" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439876">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f1aa555f.mp4?token=aT1rt8o5tTLwIhvvPsFDAnDbILUafkWJ2WY_02Y4pP1pk4Qm-OpEMzOGL5ETLIurSbjzAW_0KLQ2Rhu4HwF37cXM_tH-_MdrjOSbDIxb2qMP9Yz8f-BNJT9QlLFvI5u45gQnuWSmmo3t-EhDeEfCLGH90H6Oh4ALZxhboo1EiKG7kUPD0Ujpfu3e15a3ARfM9dCaWCAXJfSR_5aElUvGtOZgx-_yz8dSmItOo4SC_7kJ44IKkOqQjRUqzDhBDXkfoKZyYOQMqGIHwylagaltMwjiJLFH9Y4i6QdV5zDHfjEplWWZriocaNRG2tIw7gm5dfHefJCv5LGf2l9jT4zTvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f1aa555f.mp4?token=aT1rt8o5tTLwIhvvPsFDAnDbILUafkWJ2WY_02Y4pP1pk4Qm-OpEMzOGL5ETLIurSbjzAW_0KLQ2Rhu4HwF37cXM_tH-_MdrjOSbDIxb2qMP9Yz8f-BNJT9QlLFvI5u45gQnuWSmmo3t-EhDeEfCLGH90H6Oh4ALZxhboo1EiKG7kUPD0Ujpfu3e15a3ARfM9dCaWCAXJfSR_5aElUvGtOZgx-_yz8dSmItOo4SC_7kJ44IKkOqQjRUqzDhBDXkfoKZyYOQMqGIHwylagaltMwjiJLFH9Y4i6QdV5zDHfjEplWWZriocaNRG2tIw7gm5dfHefJCv5LGf2l9jT4zTvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگه بخوای از رهبرمون آقا سید مجتبی عیدی بگیری چی می‌گیری؟  @Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/439876" target="_blank">📅 16:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439875">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
خبرنگار شبکۀ فاکس‌نیوز: آژیرهای خطر در شمال اسرائیل درپی حملات راکتی و پهپادی حزب‌الله به‌صدا در آمدند.
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/439875" target="_blank">📅 16:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439874">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5e069b42.mp4?token=Y_lmZYtecQOSXIxtirolr7ikpDsSahxUeNqiZvHeysqcYrO4EkACj-PFdhARom95GI3XdalByoNubKNdPWKWK9CwBq2wNq-QsWt-F2gGuhnG-q1g4IpVLdbTr-CEiiQrKfyHmGQT9Fht1idNjBY4VSp7b3kvshUoXANqWnu9rEscPoN_kc7KFw2lmXiZNv-8JBSJ3GiMZtHdorcsytHBf6ou1TNEtHeooqo_G4Ps4fnA3C2JfLqfKtypwipgUx4SoBkOu507qDxutYUSdESeJStju5oMWKr0ROe8SdScnUbLfBhAmSdWF4x0bEts3YNNkw_sqAdbENor4YY0I96arw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5e069b42.mp4?token=Y_lmZYtecQOSXIxtirolr7ikpDsSahxUeNqiZvHeysqcYrO4EkACj-PFdhARom95GI3XdalByoNubKNdPWKWK9CwBq2wNq-QsWt-F2gGuhnG-q1g4IpVLdbTr-CEiiQrKfyHmGQT9Fht1idNjBY4VSp7b3kvshUoXANqWnu9rEscPoN_kc7KFw2lmXiZNv-8JBSJ3GiMZtHdorcsytHBf6ou1TNEtHeooqo_G4Ps4fnA3C2JfLqfKtypwipgUx4SoBkOu507qDxutYUSdESeJStju5oMWKr0ROe8SdScnUbLfBhAmSdWF4x0bEts3YNNkw_sqAdbENor4YY0I96arw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا حالا از سید عیدی گرفتی؟  @Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/439874" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439872">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0631d4a758.mp4?token=NOuVyAjML2TsdHmfg-R9AhpWQ5XPkBcu_PuRtc9twHo-OYCB--BxmeO8n3KeKZ4viaf0kH20KUFWZpZlROXnZePE-cg3Hff8Ym7wSpweG5sIUB0JMAnMysjxT8yvzdvbkYQFOSwuyHbGSv5cmKAgi-VIPNuPoddhQv1c8BYbSehEswSOP6LHia04rdJ0bppXXLPfqEtKnBfza4xk1lzB1Bk6SYKako10kmx6_eUJIrfUBbP2JOzXLRQyTYKSh14rTZuJFd6vlKU1ohTkGfJHIvcZlfotzhrowBLC9j4Fx7ofqsgusCzX4dybheYpQ5pSkz3jjJM7Larq8xrX8f3c0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0631d4a758.mp4?token=NOuVyAjML2TsdHmfg-R9AhpWQ5XPkBcu_PuRtc9twHo-OYCB--BxmeO8n3KeKZ4viaf0kH20KUFWZpZlROXnZePE-cg3Hff8Ym7wSpweG5sIUB0JMAnMysjxT8yvzdvbkYQFOSwuyHbGSv5cmKAgi-VIPNuPoddhQv1c8BYbSehEswSOP6LHia04rdJ0bppXXLPfqEtKnBfza4xk1lzB1Bk6SYKako10kmx6_eUJIrfUBbP2JOzXLRQyTYKSh14rTZuJFd6vlKU1ohTkGfJHIvcZlfotzhrowBLC9j4Fx7ofqsgusCzX4dybheYpQ5pSkz3jjJM7Larq8xrX8f3c0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حنظله مدعی شد: مدیر ارشد موساد در عملیات بمب‌گذاری به هلاکت رسید
🔹
گروه هکری «حنظله»: یکی از مدیران ارشد «واحد نفوذ جدید» موساد در بخش مرتبط با پرونده ایران، در جریان انفجار یک بمب کارگذاری‌شده در خودروی شخصی‌اش به هلاکت رسیده است.
🔹
این عملیات پس از ماه‌ها رصد اطلاعاتی، تعقیب و مراقبت مستمر به اجرا درآمده است.
🔹
آیا دستگاه‌های امنیتی رژیم صهیونیستی جرأت بیان حقیقت را خواهند داشت یا همچنان به انکار ادامه می‌دهند؟
🔹
حتی افرادی که تحت شدیدترین تدابیر حفاظتی و امنیتی قرار دارند نیز در سرزمین‌های اشغالی از دسترس مقاومت مصون نیستند.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/439872" target="_blank">📅 16:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439871">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64842bfe2c.mp4?token=VTecwrWTviBx1QoQyJyOvsFS4a2Ql_TDJomaYJlVAxjjAzgGI-SDZC_gtBNiELDoXt6GENmbMGqy3v4pU83Ahr1GkjIf3tpO_IE_VEwW4FlDy4SK3D1B166mHFIRbrL8ix1zWWNc6s3W4yU4vjicQHjbu2aVU1QiCehcBPBgMC9gaGsaY6VJVHQxPPqcSYmZu3gYS8IK-23ijd8h_cDRyvKESiSF2r6y0YdKSVOx9m8T0g7wnr0KMWvXOFVXHTxwWa4F-jSLR-dk91jW563vxINBPLbXrQrCYd3wICtmsS6qsC0A-Nagwk9-Ta_cUQoPUpes7c19cuvD2b0Td5c85Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64842bfe2c.mp4?token=VTecwrWTviBx1QoQyJyOvsFS4a2Ql_TDJomaYJlVAxjjAzgGI-SDZC_gtBNiELDoXt6GENmbMGqy3v4pU83Ahr1GkjIf3tpO_IE_VEwW4FlDy4SK3D1B166mHFIRbrL8ix1zWWNc6s3W4yU4vjicQHjbu2aVU1QiCehcBPBgMC9gaGsaY6VJVHQxPPqcSYmZu3gYS8IK-23ijd8h_cDRyvKESiSF2r6y0YdKSVOx9m8T0g7wnr0KMWvXOFVXHTxwWa4F-jSLR-dk91jW563vxINBPLbXrQrCYd3wICtmsS6qsC0A-Nagwk9-Ta_cUQoPUpes7c19cuvD2b0Td5c85Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دوست‌ دارید از رهبر انقلاب که سید هستند چه چیزی عیدی بگیرید؟  @Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/439871" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439870">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌ یوسفی: افزایش پلکانی حقوق، هفتۀ آینده پیگیری می‌شود
🔹
عضو کمیسیون عمران مجلس: اجرای کامل مرحلۀ سوم متناسب‌سازی حقوق بازنشستگان  و افزایش پلکانی معکوس ۲۱ تا ۴۳ درصدی برای شاغلان و بازنشستگان که در برخی صندوق‌ها و وزارتخانه‌ها اعمال نشده، هفتۀ آینده پیگیری…</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/439870" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439869">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef46a9d7.mp4?token=Rpx8J1iTOWu8JpVuNxXJW7Yy8qEFItpEv1r3jF8OkeW1_br8iTNNsr63nOF_Mt4G7JAhaA6vubreGFYrMqoKrEuSGzeyDFa5TExP0sYlEzbUHr6IcYJvY6Ov1RnG_ngo-i5WpcNjwhHf4zrp7yCy5hINfZBOJ_R09EIXub42Kw6v-CCJgNdowF8gRY3hhyobHKrMTaCD5iT0VK12qxsLXgDX5G5CXwkhfu6PkxSmwXIbj0XPJLzrFn6DFAvz8bhTyn_Md8iHjiW-d5A2aNwc6glBtrGutLWMAqDYuDEz512i0t0_mvItRbUt6ZECufwCSfZFbjOpe9kBHbct-U9uog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef46a9d7.mp4?token=Rpx8J1iTOWu8JpVuNxXJW7Yy8qEFItpEv1r3jF8OkeW1_br8iTNNsr63nOF_Mt4G7JAhaA6vubreGFYrMqoKrEuSGzeyDFa5TExP0sYlEzbUHr6IcYJvY6Ov1RnG_ngo-i5WpcNjwhHf4zrp7yCy5hINfZBOJ_R09EIXub42Kw6v-CCJgNdowF8gRY3hhyobHKrMTaCD5iT0VK12qxsLXgDX5G5CXwkhfu6PkxSmwXIbj0XPJLzrFn6DFAvz8bhTyn_Md8iHjiW-d5A2aNwc6glBtrGutLWMAqDYuDEz512i0t0_mvItRbUt6ZECufwCSfZFbjOpe9kBHbct-U9uog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📸
ساعات اولیۀ مهمانی ۱۰ کیلومتری  عکس: محمدمهدی دهقانی  @farsimages</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/439869" target="_blank">📅 16:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439868">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اینکه خلع سلاح مقاومت شرط اصلی توافق دولت لبنان با صهیونیست‌ها باشد، به معنای نابودی قدرت لبنان و تهدید موجودیت مردمی است که در برابر اشغالگری ایستاده‌اند.
🔹
نتیجه مذاکرات مستقیم دولت لبنان با صهیونیست‌ها از نظر ما بیهوده، تحقیرآمیز و…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/439868" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439867">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: قاتلان پیامبران در سرزمین ما آرام نخواهند گرفت
🔹
ما با متجاوزان خواهیم جنگید تا آن‌ها را از سرزمین خود بیرون کنیم و تجاوزشان را متوقف سازیم. @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/439867" target="_blank">📅 16:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439860">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_4Ukf2jaBbsKdzVYix2EsDsQj2Zn358t8or-nWgQKg_du1bGwfP-Qpc4P4zO0A35KlmyBYvoDPqgXQQ8vGIAqTxgl2HwLx_dBU21lUi78n17vghwYQix7MElLhQLs_fYbYa9C1cyMAiZ65T_cTyZrNhH-nfGRBdQ0I2NdFLqkog--skBUvyBZO9a0Uz1zK5PZp5ipDs3_XYNd1_leYxaUWRCKC_CcUQjyNcoeqyPEi2e52d-STQFrc8NtCsfu9xE1OdvnrrZDpajAptDS4dsfMBfsLw0LYYMvbwnu2nqB-qQPcgX5BtrQ2CSRfh0pAVA-a9-Fn5gZMnHDUmct7IAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rl_KBmDgHL8umt7vgvKu05EZBRTdj_NVUisnjb6S8PQE_2Cqx98Yf4G3gHP0y80SJb6VuaLnv4sUOIrt_Fz6GvaZO6LtYs5pICuEt4v-zpgBxs_KV-y9O5prCew1mxeWQx6tdcAle238Ugp6UiSMGvLz1Rd1V5jTAdZo_lQahVcO3kXM90Z_XKIpeCwqdzv2ES2UPEQtn2NbcAlbfcp_ZIZvt76-hoBzH5wmDhWXnMzxQsDdTyVFqg_911DxZgBX56A4MS-EJpXh4TOiNIDbcLeRdoZC-GkJ7SO59lKCmWqs0fhxH42jAcsbgk0EuFABuJxA4kAZFNhE5uajvylTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zs-ActBU4otSR5XGVsvw8J0sglUYH06Lo8S6ux5zpvwSqM8Tn-LQ79IMew6RsgbrnKlqm57RVQs2n1CgqCMridko64dfD_dN0YjUyef4ePEXA4U_GKM7V-_jwhM94ShXkGJpByp269IMD3aM94ctMN7Q46ws7HMVnyR3ZliwaAsEbGdX84yoQKEQcbYBviWhDm4u59gQBWomSy6NPcX5tb6_D6j4sn7KXj-uArYWiOWm2IXTyTJMglU8Cl2Dr-Ubtfvtlz3EFZIfMqg_voC1K6cGFS54OdcMftitQFIJpZ9Px4LYzwn4umw9f0_EyXv8vadaoNS7o6RwzmzG1ESldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNdXJ0YSOLLX8v8YweXdBEQaMybOPAGg5WlGqmaeT6CXMo_z4x7tRm4GYBISzy0-S0fz2XqeJuwzVG0731m4BK1_mIme_wG9WUaWIKdYW4To2HH65dZpHwopZyq7rgWJ5z7ODvIQIM9P3HIjFOEMLMfFOCvBAcWeyrxvF8W4a6o2LXF_z721xxBkiEiT1qCra2bhTkn9uS2sSqs0U29U6A-MTPgjpQ08gzSGWYU0o2QnK12MJ7oHV8QXFGOYH9HaUe-nmV4J4ZkP-ed0zauUlX9lvIPK36WSgZ3NcZZB0KioevhTvMwI3jW2BRri79tcOoLMlp-1bpBPWGuzPHxKAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nlifdvl11um1aYKvprUimk1EJgnfw70vGwTMjOR2KKjTcMQt2fs-gRYTuP7gx8e4xSXjhlhOsjoskaJxbimMtiVnu-TrWG9j61Vlq9mFe3lDPcr3eUO36tg1gXrNrTSaZG9w7N_AhuclUxe0Dory_9oyg_DOyNzFUNehCKywluIF_t0X2ZgQrtyggmwBFPyWalNHLZItihLEYYU9Nci-iAHJimCbYC_K7TX_M0ta4NbapUitTHe4WPKwlHGmH_AHV3J9pvXVYScJJTarY-CRdhs-fRqPGTSL2ojAM_bq4zoac0pb57VyIaUQcjunOOoj9gyYO79hqO6JDwkMBIjBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahRevkSZLM4WrHXh9e6yYrjjP0H_QqETUjAab733fVVBqGxDJeLniADPwvbTg_AfeyNwQnqIrBH1KU8YmvQf42uv_AR2ghjkze9hPseHOXQxfNdObJezLEAN3dtDzz0aTSyFhEVEW3yWhg70vJ6dXnMx_lTwAQi0fohI46jb-lk30osj0SA09iic9KF0kel8KzfJ18oMY-p0JOX5VBR6-CdBLxGv3jGZsuWUgtCX32xrgXIBhu22TEkIlNjqIk6CscnOJ3YCcf8IS3NGV5ffzlqgOyJbE6GzgGnniZRrUnh3YQnWcgxbGXnkGCGMpsVBhamzDZidK_BNmFrryBjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9Wuc3MdZKfhQouhKGcK1d65xpO6mQQnb8vv17_ruGqDV_QGua4yFnK7wCiI5kv-AKxAUsjQXYZLbWnqYEF9I31opERIlgM-FCoEnozpO7Yi7uK4dw96VsKQQtkVJwr99vRyOtN1kKtGYS9t1bC9n4zFfcMmfe_9GQ-4k31KM6k5a0OnaeKJ3OUXPJz8Inhk_fuodpV8HVCK8spHv9l3_I3TW200P9Ctn49asdj1Mls9U1Ebta7aa-8Lyhe43aGMlxqi_mtMAM1fErhRQPLKIZJV964zwhDs0XVTOtLExRHiKu5qRa4q4ofq42wTWl0xLuHEgdS8kVCsvPOqglaGTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
ساعات اولیۀ مهمانی ۱۰ کیلومتری
عکس:
محمدمهدی دهقانی
@farsimages</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/439860" target="_blank">📅 16:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439859">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: زمانی که روستاهای ما امنیت نداشته باشند و بمباران و تخریب شوند و مردم ما کشته شوند، شهرک‌های صهیونیستی نیز امنیت نخواهند داشت
🔸
آن‌ها صلابت و شدت عمل ما را خواهند دید. @Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/439859" target="_blank">📅 15:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439858">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: تا زمانی که حملات دشمن ادامه دارد، با تمام توان با آن مقابله خواهیم کرد و هرجا که تصمیم بگیریم و بتوانیم، دشمن را هدف قرار می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/439858" target="_blank">📅 15:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439857">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما به هیچ‌کس تعهدی مبنی بر عدم مقاومت در برابر تجاوز و پاسخ ندادن به حملات دشمن اسرائیلی نداده‌ایم
🔹
تا زمانی که اشغالگری وجود دارد، مقاومت ادامه دارد. @Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/439857" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439856">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: از ایران سپاسگزاریم که با وجود چالش‌های بزرگ خود، به ما برای بازپس‌گیری سرزمین و حق‌مان در مواجهه با تجاوزات اسرائیل و آمریکا کمک می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/439856" target="_blank">📅 15:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439855">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: مقاومت در لبنان از مکتب و اندیشه امام خمینی برای آزادسازی سرزمینش از دست دشمن غاصب در منطقه الهام گرفت
🔹
ما برای سرزمین و ملت خود و از روی طاعت از پروردگارمان می‌جنگیم تا بنده هیچ‌کس نباشیم و نسل‌های ما در میهن خود در کنار هم‌وطنانشان مستقل…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/439855" target="_blank">📅 15:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439854">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: مقاومت در لبنان از مکتب و اندیشه امام خمینی برای آزادسازی سرزمینش از دست دشمن غاصب در منطقه الهام گرفت
🔹
ما برای سرزمین و ملت خود و از روی طاعت از پروردگارمان می‌جنگیم تا بنده هیچ‌کس نباشیم و نسل‌های ما در میهن خود در کنار هم‌وطنانشان مستقل زندگی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/439854" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439853">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e04083cc32.mp4?token=tP67_gGjF3Lf1gze9GZPHFEwfYoLomGqsxaofNUlNXLXgHybdwBQrcQG_CceKS5LGucruVa42jgDg53S_FIAngOwk9tJ8LlO4NZXYrlYMBAe3qXqa1AYZ8aeUch0Gq4RDOYr_n6L9JRJjC-HYkzEJO2IwCkkT9ulei8ttWO2DSH6yfNI3a8NunpFtL6YOpVeG5Xs5F9w5QQ5XKDkkOcIA8RaO6aonj5cMwtN2djcKuo9_Sy_iJFisMB-Agds3YmOCJv45uquWm0eKYM85j0Yjz9BUhOvO_tBR3HdDVSj3mhijB5CFZR6XWuthGrQ5WeBlipZh4qZAQBV0HShoJoCZmdumCAhXMPPUsaoL21jWp_LbGabEglVLuO--ojIBB4hhZ0EAoZytg1bSsW3loWlNvKxz3-mwLOcj9PN42mZt7Xex4HQva9d3XD3yRPkH-rBaPa4vgTRbQ7NZ3pm3x3X1RWf9x47sIrZY18ovp0K2Rh88c8GdXoa9rEjuhSba-Vmg5LBAlypWTr-0FpF0qxkJ48gx9rfXNjGpsQGHDyDtAyqdbZY_fDl4heE4-Du-Z_imr8UjORV0OB9UOVdDOxXivY9g9eoAxRdWtU-rFIGL3lYV8AlV61CQv0RF4nesoP1YjdGHzo8g6TOGlDGk343_PiwUU2ysnK7hcQR4UiPJ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e04083cc32.mp4?token=tP67_gGjF3Lf1gze9GZPHFEwfYoLomGqsxaofNUlNXLXgHybdwBQrcQG_CceKS5LGucruVa42jgDg53S_FIAngOwk9tJ8LlO4NZXYrlYMBAe3qXqa1AYZ8aeUch0Gq4RDOYr_n6L9JRJjC-HYkzEJO2IwCkkT9ulei8ttWO2DSH6yfNI3a8NunpFtL6YOpVeG5Xs5F9w5QQ5XKDkkOcIA8RaO6aonj5cMwtN2djcKuo9_Sy_iJFisMB-Agds3YmOCJv45uquWm0eKYM85j0Yjz9BUhOvO_tBR3HdDVSj3mhijB5CFZR6XWuthGrQ5WeBlipZh4qZAQBV0HShoJoCZmdumCAhXMPPUsaoL21jWp_LbGabEglVLuO--ojIBB4hhZ0EAoZytg1bSsW3loWlNvKxz3-mwLOcj9PN42mZt7Xex4HQva9d3XD3yRPkH-rBaPa4vgTRbQ7NZ3pm3x3X1RWf9x47sIrZY18ovp0K2Rh88c8GdXoa9rEjuhSba-Vmg5LBAlypWTr-0FpF0qxkJ48gx9rfXNjGpsQGHDyDtAyqdbZY_fDl4heE4-Du-Z_imr8UjORV0OB9UOVdDOxXivY9g9eoAxRdWtU-rFIGL3lYV8AlV61CQv0RF4nesoP1YjdGHzo8g6TOGlDGk343_PiwUU2ysnK7hcQR4UiPJ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ ماهشهری‌ها در عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/439853" target="_blank">📅 15:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439852">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8abebd4f70.mp4?token=dJ4lzttERoyuW9CeC-H9fjslKmvR--JKmVjG9sU0JxQzp6J5qrIwRHZsytF8Cglb7M6mZKF-dv9jjKaaoD6kB2v1S87Hxu7vxc25EBuMzarbD3396PtH-8nUf7d6Mv3ysEBWBvj9cSPEVEPRjMYjmHs4eiNVnmASeHUnyOSFtE7Sd-XdMDrCPzUHmA6pFMA8fbBouuRjL2mGFwx4fTEx8OVJlFZ-r_vFUcZ4nr8azAvoZ4Swxzv0sqhLQFnR4Ifv96wOR9gHxtt8zCg1JPdQyX7WDh9m10SAHW1bww1VFnEWd8Eh6-QElAY5Cnq8o1vQ2WFlxoqgVasz8UjxOdAlCoPS3-f_2w1BmskrCKiLvpwKgXr7c5WP6a-CmavfD5_VFugYsSxvip0b-WVo9hpyOVSuF40DpJ8iBAj2S4LS9TvqE6UMmpFk2o03Dxfk5JE3A79Pt7YvH7fYlz2PIwDhhKJlp-mRzyDQuSPCGws_rgW96t8GET15bML2l1FnJOhsTx-UQqYMpRbwWOqYDqWjFPJQFDgz7UqWKzihzS4Ge60OYP0cv_8gnfeCMX4WDVXom-vHLIaMUcuD5r8YQeBJq6CHd5qn7Ge4xOeMe8wf5uOfuvtbqydtdgDRXyW-LA7ZAVpQkuc-217KPQ8T01ps39vsRKti0nLY2T1EXOk37qM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8abebd4f70.mp4?token=dJ4lzttERoyuW9CeC-H9fjslKmvR--JKmVjG9sU0JxQzp6J5qrIwRHZsytF8Cglb7M6mZKF-dv9jjKaaoD6kB2v1S87Hxu7vxc25EBuMzarbD3396PtH-8nUf7d6Mv3ysEBWBvj9cSPEVEPRjMYjmHs4eiNVnmASeHUnyOSFtE7Sd-XdMDrCPzUHmA6pFMA8fbBouuRjL2mGFwx4fTEx8OVJlFZ-r_vFUcZ4nr8azAvoZ4Swxzv0sqhLQFnR4Ifv96wOR9gHxtt8zCg1JPdQyX7WDh9m10SAHW1bww1VFnEWd8Eh6-QElAY5Cnq8o1vQ2WFlxoqgVasz8UjxOdAlCoPS3-f_2w1BmskrCKiLvpwKgXr7c5WP6a-CmavfD5_VFugYsSxvip0b-WVo9hpyOVSuF40DpJ8iBAj2S4LS9TvqE6UMmpFk2o03Dxfk5JE3A79Pt7YvH7fYlz2PIwDhhKJlp-mRzyDQuSPCGws_rgW96t8GET15bML2l1FnJOhsTx-UQqYMpRbwWOqYDqWjFPJQFDgz7UqWKzihzS4Ge60OYP0cv_8gnfeCMX4WDVXom-vHLIaMUcuD5r8YQeBJq6CHd5qn7Ge4xOeMe8wf5uOfuvtbqydtdgDRXyW-LA7ZAVpQkuc-217KPQ8T01ps39vsRKti0nLY2T1EXOk37qM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابَرپرچم‌های بیعت با ولایت در مسیر میهمانی ده کیلومتری غدیر تهران  @Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/439852" target="_blank">📅 15:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439851">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7aGMiIuE8trWTjKm2z7XynDsvr08AhzhMHaeLj9DC1CF7UBniqQ2OshTohm4FIg8qH5o8l_Rpwo2mqHfFGNNRuxXcpnLhtoQivf1D7OyWjpY_jKCB15hP2TzHqqPVLluT2cKsfnIJc2AZDpVX0xC1gIeare6yJJteic4rOkQoSCXKLzT3y7gRLr7fBcMVFWoVcQaVGcwglkXWYr_E5O4nBBxpvw5WMI1Wjnb7s298fFHTU8x5-NM3NVjoBonUhot39v9y8dF3t_eBYH7byLow3lJDssiB_ql8vPhYrT8v428hqjtNMX-3YqNpzNPPgsTpfVsWIYFY2fDrKd_5oXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
انتشار تصویری از رهبر شهید انقلاب به مناسبت عید سعید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/439851" target="_blank">📅 15:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439850">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fb369f7d.mp4?token=WXq4gt2Dj9lC0RdNFFN5Zj045m-2w9eMitwB7NTwDTtaf82gP-R8W2CeQXtSj0J5rb8njcjRBhw0zwpe3IsjOKh-IiXZtL4yYmvZ6hohP-jKErQ-NEn3couZVWt6IjI8OeHMCCMNo118lWVO6i9oX2fx7NxAQcbU7malbEWccXfXCcLXAccHKFLkXz7ghq_iDRd_BN81SPeZqQs3YowbfgQK7phkBso3MmxNfG1CglPb__8DLlDBDODRDVDMsRVH1cQykR0hbXotmQg-wpnjOutOLcg1uhCqBm7PekLUwSswq_yMQCxznJ3dhmoRNfkGqRpt8p69M_Jf9xQLThYOqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fb369f7d.mp4?token=WXq4gt2Dj9lC0RdNFFN5Zj045m-2w9eMitwB7NTwDTtaf82gP-R8W2CeQXtSj0J5rb8njcjRBhw0zwpe3IsjOKh-IiXZtL4yYmvZ6hohP-jKErQ-NEn3couZVWt6IjI8OeHMCCMNo118lWVO6i9oX2fx7NxAQcbU7malbEWccXfXCcLXAccHKFLkXz7ghq_iDRd_BN81SPeZqQs3YowbfgQK7phkBso3MmxNfG1CglPb__8DLlDBDODRDVDMsRVH1cQykR0hbXotmQg-wpnjOutOLcg1uhCqBm7PekLUwSswq_yMQCxznJ3dhmoRNfkGqRpt8p69M_Jf9xQLThYOqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اسرائیلی: با حزب‌الله آتش‌بس نخواهیم کرد
🔹
آتش‌بس در لبنان یک خیال‌پردازی است. حزب‌الله از شمال رودخانه لیتانی عقب‌نشینی نخواهد کرد.
🔹
وزیر امنیت داخلی رژیم صهیونیستی با اشاره به ادامه حملات پهپادی به شمالی فلسطین اشغالی گفت: «حزب‌الله قوی‌ و قوی‌تر شده است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/439850" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645d8440fd.mp4?token=DPeywUtlRrnUmZvep64Xsk2qtQcVcKnShNK6HhkDAod64B7g5y-sAhO40tCzEvMXegywOaEqpy2cSUxpSgEZ8_d8JkUscojDEHp7jrZc22jNLdwWednaRFBxhpily9YmCcEIxzvMwGUrTJWHmdryQgsfCiIv9BqsaV8R7MfNXLkASA-tXD72BzaIjXvKS2O-F6YsGZ1yokZ-sppeUC7tov22vZskQUqp4GGEsS_7eylpVxJEHGP1FVB5xhmftHzC3COvrEcqkwB-Y99NclPjYyQbFRB1AnShskhk3Cb6yo75IS_SPhDlOA_RcDkTxMgP-XN18O4p6qCXaB4Jp6HAc15W3gKBbCPuvFuV9qmNun1DGuBTQq5FvE-xEI--rwte585niIv6JJ_zzAxYvJalPr-vP7Cm1AyRLycUks52sw2BVaR34V2prQcukdMZgVo_byoYs8x6wzNmXSuPWqToqzUPcrmj6gCuc1ZteRCstjYOTvy3LY6hZlxiFzpQ4RMew-kaYQUHgJ6cB5n1LdXMOPtyjY5hqFP2wPrF4MW3Vz3t0O-PE9WPptRHpBLpEEJkQv2gbGc0Nc-l8JQzgnbAGjPgrVbp3OgHYfQnhgcKTCnxQCOWtmsMnWpPUICUzBis0m4FwyOt76LYdLXiYs-ZNxhYIWNSeQGbu1RglcCvAKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645d8440fd.mp4?token=DPeywUtlRrnUmZvep64Xsk2qtQcVcKnShNK6HhkDAod64B7g5y-sAhO40tCzEvMXegywOaEqpy2cSUxpSgEZ8_d8JkUscojDEHp7jrZc22jNLdwWednaRFBxhpily9YmCcEIxzvMwGUrTJWHmdryQgsfCiIv9BqsaV8R7MfNXLkASA-tXD72BzaIjXvKS2O-F6YsGZ1yokZ-sppeUC7tov22vZskQUqp4GGEsS_7eylpVxJEHGP1FVB5xhmftHzC3COvrEcqkwB-Y99NclPjYyQbFRB1AnShskhk3Cb6yo75IS_SPhDlOA_RcDkTxMgP-XN18O4p6qCXaB4Jp6HAc15W3gKBbCPuvFuV9qmNun1DGuBTQq5FvE-xEI--rwte585niIv6JJ_zzAxYvJalPr-vP7Cm1AyRLycUks52sw2BVaR34V2prQcukdMZgVo_byoYs8x6wzNmXSuPWqToqzUPcrmj6gCuc1ZteRCstjYOTvy3LY6hZlxiFzpQ4RMew-kaYQUHgJ6cB5n1LdXMOPtyjY5hqFP2wPrF4MW3Vz3t0O-PE9WPptRHpBLpEEJkQv2gbGc0Nc-l8JQzgnbAGjPgrVbp3OgHYfQnhgcKTCnxQCOWtmsMnWpPUICUzBis0m4FwyOt76LYdLXiYs-ZNxhYIWNSeQGbu1RglcCvAKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع پرشور مردم اهواز در جشن بزرگ ولایت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/439849" target="_blank">📅 15:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439848">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8f7f6d83.mp4?token=DdRw5-qwzSUXjsvLANXZQTOwF7Kj444PnvtXcoHYvzS0PAwp-gw3_wj32l7-s5j8D0UcjXGHNP5-iEFuwwvIJZCqqH-tAnurwsNnnxdOEi92IDDU1qDJA8jyCeg3w2rnJ3AogslBKJuO85QtcTUy5xVxZ3UtFhf0o4_RI2xMD_u8Uo9DRfvchqkBz21n6plKHyQX1i86Y_UgtsCn20SOHXW2jJZD54DLFOEjwwz_st-uT8uIXNCUzBbNguxY8VugAAF-vjudoo_Nb2GO5bYxCyt34vg4reX5opYdLgnhPVr_l0pr5rc4mv6kM2FO7JeN8ztqCJmI-6Qz9IwTw_HiCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8f7f6d83.mp4?token=DdRw5-qwzSUXjsvLANXZQTOwF7Kj444PnvtXcoHYvzS0PAwp-gw3_wj32l7-s5j8D0UcjXGHNP5-iEFuwwvIJZCqqH-tAnurwsNnnxdOEi92IDDU1qDJA8jyCeg3w2rnJ3AogslBKJuO85QtcTUy5xVxZ3UtFhf0o4_RI2xMD_u8Uo9DRfvchqkBz21n6plKHyQX1i86Y_UgtsCn20SOHXW2jJZD54DLFOEjwwz_st-uT8uIXNCUzBbNguxY8VugAAF-vjudoo_Nb2GO5bYxCyt34vg4reX5opYdLgnhPVr_l0pr5rc4mv6kM2FO7JeN8ztqCJmI-6Qz9IwTw_HiCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنان علی لاریجانی درباره شهدا، یک‌سال قبل از شهادت
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/439848" target="_blank">📅 15:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439847">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hma5STNFzTL1pbMaxfmZ4NKL6iZCbtUO0w-urmRXuRB_RN_Op2Ga7kQur4NUCJyADwp3cbv1S6uPpHwdFoi2cq9YOWImqJTCNHUviSMykL8RcijQ21YO8RMjTyXGhc0sO6TWGrq1DU25HWg03Ufp-4hmjhWxyKDBNC2PDCNaanontnb1SG03LnGDvYvNNN7yyfybpxkPAju4m-fTZuApkYhMWay3tvckZANF7syAMmiN4QLiyJLe9X-lRvL_6mQ4UZn9TZslKFjE4WUmi5anGwC29G3G86IkPoC_HgrcoiEEG4zWU9i6_UIAXyxevDBwW4W4SmvcylRIWgGsxzHBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بطری آب در جام جهانی ممنوع شد
🔹
فیفا در آستانه آغاز جام جهانی ۲۰۲۶، ورود بطری‌های آب چند بار مصرف را به‌تمامی ورزشگاه‌های این رقابت‌ها ممنوع کرد؛ این نهاد پیش‌تر اجازه ورود بطری‌های پلاستیکی شفاف و خالی را داده بود، اما با اصلاح آیین‌نامه ورزشگاه‌ها، این مجوز لغو شد.
🔹
دلیل این تصمیم مسائل امنیتی و جلوگیری از خطر آسیب‌دیدگی ناشی از پرتاب بطری‌ها و سایر اشیا به داخل زمین یا سکوها عنوان شده است. همچنین ورود اقلامی مانند قوطی، لیوان و شیشه نیز ممنوع خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/439847" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfbHqB2M0ODBZxjtXN7XM31-w78GDr2tzk5A5wGH4gOuRcynq1z3QNzxCDxHMGObOr_XrZzOs4WRouc7Vs9Yy5bmD--0OTmlRQ6BApBbqvpsLDvzR-8MbUh-P-zO4a9kJrygr7T2sicZXVrgjKEPBQB1A2fdNsDpi3B1EqtZpBTsoweZ_N2XrD0IMEhSoFTrqd9n9A3gBlCREC8KV8_wpsinsKO5vroPa4DKJETH3-mIMyPzU6QlWn7lDosDQ25V8Iy3W0k8lf8Ft3mhnNJKapmbDuYr0nk5L3NzHoNUHP-u-8EWqNgvXBdCnIfrZT0Akjf8HVN_S-CJJ6K6Al_V4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRipd5Tm2_DvXK3z-Dka0rpjK96AekXKRt0CINh4aMVA9PU--HqNVrWYZ1qGoFZJGMkpvrIRI1crR2rejSV-A9f-p4R9VnZFzgt_WowcUysD9R1lJgbLHPt7PBRShFZVMKjsAKbV0uEXwYt-IE41itEtuaUZk7KsYQruCJ8Dknao_K-c7jhcSzJmv88of9InIQox1DCoUYiU5f2-IlzrRYgfr1xLuG8mC1EI_lNv8-X6krV0s2HT22mx6fqUoMHzjBEpBnkqSluxV30jYU4nlgEBTg4b89qFmUkLZUSggchmJ94gicK6k7m5kpsDI7egd733lx_5qjxTXwHx6GtaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtDE1zpYyaXOrg6vsy3SX-GU2hXREIuVOqZODqNWuO7T1e__kJiCAg2uC1_TdRC9yUpy6vcBsa3Ew27bEUifhmQBSM6pex0jf58fpeuclPwg0rxqhaeyIfoGpc_dLQ_sLxOLeT1kr1fhy_iFf8vOtvI5tZz6VUwaHqJOCjCNgSqRu3es1o5qKXJdopz-n9WZCJZbxJ7nwxD_eNeGOxnMSJdmnrNFqnoBonQWr2qjJBWoT437VmzXT4NqWk0wGKxxjlnR1Lag1p7EpWq-yKzVvGSufwoqaw5pBnJZfRKsMtcC_VexLqo_fGymN3gNlS0KJV1BtJ-LNj9pmVtxEHsD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlfWuqVhkp5ZlL0GozuPAw7IhTIZTiU0-mI6KZrPw4Jr3LsLwEDE4JyARFQ4rDdrCG0VLbO_ZjXFPyZBG498O1DaIFb8FY6NI8GJ3obi2QzcC_h0YClj-MN0Fv7uho16UdM4j6BpxOzdup6qfm-tRfhC9IG2i2bauHbFPqm1Jgn-AJB_H439qz1WcJPuBeEvxr-9ln0Of2M0tRkTmn9rcCeimz_WJHuWd5gYlzKh_oIXiab8p_l1zo2Tp6CRuoHbs7EGIDLuJFkysVJeUFno5Lzmkiqn6yFLqdhcPkqc7sE7HmDPKxpJzeYi7Krw8m3AZXk9UEATTEuPtO5jSjh-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGeXMQTWl5JLjH1qAuj71oR6Gvu39JCZBU59jnb6rM9DYehq-qIftocQoxWZh-ke1ihyBSPfLedIPC8ubmifzJqoMEjXlv1nlqDrnq-2Wy_CHeXMDk5DvZWkkxcoiR_2m1QgJJW0H891RzwCfCMOrxySnqzxN3vIovz8tjRn3IjoPOWBR_8aZxtC0JcsPWAfaHkqzq5Zy6T_KL88uEbiA8pKiIIYkvr815b_IVrl8X4ab7S-45VVjK8vpNH0uXx54_-tnhdkv3xMrH6kPFcMuCZsiwyvmWxY91PO4Ud9BETDYnO8pJqk6AwhIgmAo4UINJqBIQIvSFh_EXTAg8bwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/siWKiDWgrtWVwxqPXrFcysWoZUVKUYREhT-CDRjilm2UdMNT41a_9HGlymdvclddn-F8Iomz0apnzvnZfOgw7srVnLtesHqCD959DUtHY1C9v6fXf0nKz40HtoyrMG-m1DEqIRonScPv7Jc8vpF2pVhD0if9aOzS4ijO_jZCLvdDmF_WelDlSMB4EwMiX3Ny1XugOma5LyV7CNzkq4kExRx2aIkMbFDZNl_EX0q3XCJ4WZFURpa1Ge5h7ffogHFDYR2UrkvENhjHfZGomtAAE1i9ovIRhR-kl6r8YVOBrrqHSmJhzOZQX42eGs83zxx-86UaONINhRRfxjtdcFnbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxrVy32pFIZf0FNBq5iC-bTRtpbLFMuTZ7hm61vQpe-8ConS7vvWygSJVETLD1tYTsfad39zno6x5adPVaCRuROy6eKo0rthR_6eaIa9IXFVZbE1eoAxBhaoylFDizPEDw_eytAxx8zebCFs1MCBA2yQyas_7I92lOMh81n_Qd_QWYZ3W_6CRJoai4ApzoVURxarOmlAkIRbWPmVQa7I4lxub3VhIRUSlXpsHYMYpQbn_RsMN0VKoNuYQejMZrzuvMBAVjXf5HSyLRzzCSjB0Pv4fI52NY2XUMsP_TT5qaZvvoKXlSUV_ahgUwCt2sTsUvec8SNRS3gMAUgEz-HiOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زیر سایۀ حیدر کرار
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/439840" target="_blank">📅 14:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سردار محبی: شناخت عملیاتی نیروهای مسلح از دشمن در جنگ تحمیلی سوم افزایش یافته
🔹
یکی از مهم‌ترین دستاوردهای میدانی جنگ تحمیلی سوم، افزایش شناخت عملیاتی نیروهای مسلح از دشمن است.
🔹
اگر در گذشته بخشی از شناخت ما نسبت به توانمندی‌ها و تجهیزات دشمن مبتنی‌بر اطلاعات…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/439839" target="_blank">📅 14:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051dd5187b.mp4?token=NyHFx9TKBf8NsMobrYkTtEX2iwHJeXw2R-e2sLnjY4_jneZcBU8t5AVDh5g3Fv9kSCqYYU7hF9XKf1a1-ktvprLdb3gLDRjtHiDaWs26vWRk_gGGx5XnkqKjQ_GW7xnTNk3nfAtg5W2C92sAVXZHGBNFlWDsKu4aiRQUHSmNWiD7E9pT_323ZJyoNUqcLj0Oy9X8KsKhACkJRBUpAegWQ31_6z0AqChFabdFMSMvayEq5u0PqYxogzUCvV9PLDgeZyztW8ou8LpdCR9o37T5yQJto6w2zthmSm8f3vOxhdDJD9iUIUxRrzdIYmh-40i9zXeKGg9XWo1BhaHzcRWkUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051dd5187b.mp4?token=NyHFx9TKBf8NsMobrYkTtEX2iwHJeXw2R-e2sLnjY4_jneZcBU8t5AVDh5g3Fv9kSCqYYU7hF9XKf1a1-ktvprLdb3gLDRjtHiDaWs26vWRk_gGGx5XnkqKjQ_GW7xnTNk3nfAtg5W2C92sAVXZHGBNFlWDsKu4aiRQUHSmNWiD7E9pT_323ZJyoNUqcLj0Oy9X8KsKhACkJRBUpAegWQ31_6z0AqChFabdFMSMvayEq5u0PqYxogzUCvV9PLDgeZyztW8ou8LpdCR9o37T5yQJto6w2zthmSm8f3vOxhdDJD9iUIUxRrzdIYmh-40i9zXeKGg9XWo1BhaHzcRWkUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی موکب‌ها یک ساعت مانده به آغاز میهمانی ۱۰ کیلومتری غدیر تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/439838" target="_blank">📅 14:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i73QqLz1Nrc7mAQqIJ0KjR7-AHocSf2vBhla612A1Ssr07bLPhluuElgHStPMXNi3PMT-o5sNvU2nQG5o7ICWbHYU6HZN-cj1-rhrvHfxVayfm3tCb4bQIkDKbc7aZS1DrAUkU40n7x8TU7hwRHLsHPNRswv4HwI-FZQL3uZowmzpVcgeVaebdjto1pZj3IGIzu3DHDK1vm1rMX9Ao0uNPL1U9EDDXvodGX0EXG8061BO4-tQ9dJVKnZKpxuzZILuDR1s0tR2U7zY0Pw8FGetCoJK4yJHKX9kvTaEkVCFaS5Lr0rSTalJkB3UTmJybtWHznf4OqmUdzRi1aQyyZ4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدی اولین فرنگی‌کار طلایی ایران در مغولستان شد
🔹
پیام احمدی فرنگی‌کار ۵۵ کیلوگرم کشورمان در رقابت‌های رنکینگ جهانی مغولستان صاحب مدال طلا شد.
🔸
دانیال سهرابی و محمدجواد رضایی نیز در ۷۲ کیلوگرم راهی فینال شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/439837" target="_blank">📅 14:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dccdd6099.mp4?token=MwiSDGvL68k-8gt61jpQmJvA5WNpmY2lVlvkp7elKR_qCQHx7ZQJZSd4C-eF6bk2cVVWnJUwKync5BHH7ZNnPGpCLJgZ311YyhOwDjyK4JLUqNe8LcTloEMUekB4XA0mCP7eDMdhZ1FWBh0V1rY8dGFiAlsBRloZM0yEAh364zMHHR534MQh-aWZHunD8Q9FhTkFuYhnprMtumK40xmYKtrXmeRK6WV9p8RSdwhwteiRuTAheAv9NbtukNT5D7MmbdPirIAuXyu04K67gXVTxZjBUybgrjOfKvmt9aeugMpZOn2Fbum3HqCNFzsFb045CpQ-K9huj7M1BWwwOugYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dccdd6099.mp4?token=MwiSDGvL68k-8gt61jpQmJvA5WNpmY2lVlvkp7elKR_qCQHx7ZQJZSd4C-eF6bk2cVVWnJUwKync5BHH7ZNnPGpCLJgZ311YyhOwDjyK4JLUqNe8LcTloEMUekB4XA0mCP7eDMdhZ1FWBh0V1rY8dGFiAlsBRloZM0yEAh364zMHHR534MQh-aWZHunD8Q9FhTkFuYhnprMtumK40xmYKtrXmeRK6WV9p8RSdwhwteiRuTAheAv9NbtukNT5D7MmbdPirIAuXyu04K67gXVTxZjBUybgrjOfKvmt9aeugMpZOn2Fbum3HqCNFzsFb045CpQ-K9huj7M1BWwwOugYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رضا پهلوی هم «ساواک» را گردن نگرفت!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/439836" target="_blank">📅 13:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5LKSzrdujVFEQD2mAp4tXvc-lbvvH3dbyGm-lPZKyOScO51qHnBy3AuTJWPdWxlBckPYbHXfeQ7nBDEZRR_3nLHVUs6I_OCMV1lW0G9USERlSHeKBkm_p3sM2bDvXIFnL_x3-Wy46dGVjwdtN0BjrA3ZDvSMeTca53yN0y1ZcxAEroyjc_ewb0N8yoBOudOt5MEuUQkkpL7qTeNQJdgRWJN1VQGsZLSJ1lfK-r3nwIF9F07vrEGgHRwcpjhpuk02mQGI8T34TTFu1n54-rlEfvaecwKZ_dghjCXL6vzt463HjIMDVfo-A3gEAiJnzhxfh__vdDlJOJQt9YaX3dCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
🔹
پشتیبانی از مقاومت در لبنان، وظیفه همه ما و اسرائیل‌زدایی از منطقه، آرمان دست یافتنی مسلمانان است؛ مجاهدین لبنانی، به زودی نتایج مقاومت شجاعانه خود را خواهند دید.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/439835" target="_blank">📅 13:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌ بازنشستگان تأمین اجتماعی امیدوار به جلسه با عارف
🔹
پنجکی، عضو هیئت‌مدیرۀ کانون عالی کارگران بازنشسته تأمین اجتماعی: در احکام اعلام‌شدۀ احکام بازنشستگان تأمین اجتماعی گفته شده ۱۵ مورد باید انجام شود، اما هنوز نگرانی‌هایی دربارۀ نحوه اجرا و پرداخت وجود دارد.…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/439834" target="_blank">📅 13:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439833">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۲ عضو شورای شهر ایلام با دستور مقام قضایی بازداشت شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/439833" target="_blank">📅 13:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439832">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbSSbhJbQr7_RtM29NdtVFNRNXTxpxOcpsUi2tJp9NePtHSQZjuLQWfNd2KSRoG-VgPtK4jdnZl2LsoaazbKS4kMXFpA1cZAHb_Ea9zn5kO6XyQVVhYeZ4c_B5nYZHiuO3QTwSAJ5s1HGP04WTwl4BD0u_iyBYQwEQbtttC8PPgoWZl4QHJRg_T9zMdrdVFJ85PAmdlKSH0oszL-Wr8LhdSo9nmlaDjXs3mzgYtOFS_birLuMvptJo1BSOxUTPMhuQyjZjSWpk0gGYSv33bJ_5K58GiJ1yNhiDiYZ0UOrD3Na3R2Jh7bt0oQgnqp3H-_19kY8qqmPHkRmM27uRyLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه،…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/439832" target="_blank">📅 13:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439831">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b0549ed4.mp4?token=KTeZuNBZs1szd5Zkc3HJ5Uua0DdD5E4gW7ZKde_CTQMQ69UbWwRqZmGK6hPu2yCoOuPH6Hl_FGEA1m0lkDqmlAF1RxADIn5XRTXsxFPHipM-2PEpIvazLfGIE1MQRvQkiBUhbqduwm9fFN7adyRiiEMC6sf-8EZ3Tdf1zQb6F8Ec9WPcsYVYWdWaF4wDrxygnBEuFgyw5e76pxTJmTsSHNv4xSi0HXcK_QmVsxmQ_5TGt7KgeFBKeN_PJ_RrBJjvMnJ3idV0UpvtqxQdpJHYkz9wR3Bq6qvSnCT5ofrFu5FSP1vie4N97fkTxooeZfGxoCghfxlPtM_tDbsPF2n4TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b0549ed4.mp4?token=KTeZuNBZs1szd5Zkc3HJ5Uua0DdD5E4gW7ZKde_CTQMQ69UbWwRqZmGK6hPu2yCoOuPH6Hl_FGEA1m0lkDqmlAF1RxADIn5XRTXsxFPHipM-2PEpIvazLfGIE1MQRvQkiBUhbqduwm9fFN7adyRiiEMC6sf-8EZ3Tdf1zQb6F8Ec9WPcsYVYWdWaF4wDrxygnBEuFgyw5e76pxTJmTsSHNv4xSi0HXcK_QmVsxmQ_5TGt7KgeFBKeN_PJ_RrBJjvMnJ3idV0UpvtqxQdpJHYkz9wR3Bq6qvSnCT5ofrFu5FSP1vie4N97fkTxooeZfGxoCghfxlPtM_tDbsPF2n4TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخت کیک ۲ هزار متری جشن عید غدیر در حرم امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/439831" target="_blank">📅 13:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439830">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa54eac8.mp4?token=szPH9YM7umHPm93iriwnWSLboEaL_tPmvBAvN8ysTQKw8WZ8ZKbslbzdCjEcbDBW3RNxTrTsPTYUFUs4gDDyt_HybxoyixC3Vgfe35hk0DY7bYNLzs_sa01Rq4-mEtE7lZQOaCUgI584rr5ZvAuTFtHgn8Y7PPzSBZ3W09K7FJtJtQe_hbZCR551KyUc25oP71iRFNvThIlvDorGR_kqqDqyoZbI6pf804s7o0tW55bmnQqLcJOAUSvwC_E9bN1BdfkRF-w74bbB4A9pvm1AOcWLl2aI1XU0ye4zx7zlKkrfIBhgYU6xC2YFjyuduY2VN2BBMI6sWc1kqs1c8yndL200MwcfoarEQUFnbd7GhtR1s9kkYobQ7kknZlmsyisCkmHtk_tXDI2cCrM9QAaNuGZ2jmpQ6LvR_dbdYvooUcdG5klPcauIWJyx15A4mIxaFgv8uZVkydzzQNrycwo2KoERmeuLhD_EAJxCsAoz6omFDKGo4DEk6XLacsf29qg7Ijz4VaQI4KGjR7RJy3-p3WaJXorqQTbjWESMzNDALUpLfwRj_bCvs85C9wGGn9SvcTdUIY-ASLIU00ZkrdChlagYikCf4XJdT4rCg-Z6m6Wca-sPQRD2QBUxYdtfuLjqAaNzFJ9XdMoeN8iVoMEv02GH4j4RBtXMSE1saG8bxPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa54eac8.mp4?token=szPH9YM7umHPm93iriwnWSLboEaL_tPmvBAvN8ysTQKw8WZ8ZKbslbzdCjEcbDBW3RNxTrTsPTYUFUs4gDDyt_HybxoyixC3Vgfe35hk0DY7bYNLzs_sa01Rq4-mEtE7lZQOaCUgI584rr5ZvAuTFtHgn8Y7PPzSBZ3W09K7FJtJtQe_hbZCR551KyUc25oP71iRFNvThIlvDorGR_kqqDqyoZbI6pf804s7o0tW55bmnQqLcJOAUSvwC_E9bN1BdfkRF-w74bbB4A9pvm1AOcWLl2aI1XU0ye4zx7zlKkrfIBhgYU6xC2YFjyuduY2VN2BBMI6sWc1kqs1c8yndL200MwcfoarEQUFnbd7GhtR1s9kkYobQ7kknZlmsyisCkmHtk_tXDI2cCrM9QAaNuGZ2jmpQ6LvR_dbdYvooUcdG5klPcauIWJyx15A4mIxaFgv8uZVkydzzQNrycwo2KoERmeuLhD_EAJxCsAoz6omFDKGo4DEk6XLacsf29qg7Ijz4VaQI4KGjR7RJy3-p3WaJXorqQTbjWESMzNDALUpLfwRj_bCvs85C9wGGn9SvcTdUIY-ASLIU00ZkrdChlagYikCf4XJdT4rCg-Z6m6Wca-sPQRD2QBUxYdtfuLjqAaNzFJ9XdMoeN8iVoMEv02GH4j4RBtXMSE1saG8bxPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهیدی که از روز ۱۴ خرداد ۱۳۶۸ رهبر ما شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/439830" target="_blank">📅 12:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439829">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ویزای اول برای تیم‌ملی صادر شد
🔹
رسانه‌های ترکیه اعلام کردند که ویزای کلیه اعضای تیم ملی فوتبال ایران برای سفر به مکزیک صادر و تحویل سفارت ایران در آنکارا شده است.
🔸
علی‌رغم صدور ویزای مکزیک و هماهنگی سفر تیم‌ملی به این کشور اما هنوز روادید آمریکا داده نشده…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/439829" target="_blank">📅 12:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439828">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
حجت‌الاسلام قمی: امیرالمؤمنین بالاترین مصداق کلام امام(ره) است که «هرکه به‌قدرت لایزال متصل شود قدرتمند است»
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/439828" target="_blank">📅 12:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439823">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQgeclq_O3BwfOjksjv1CV-khiPIaR0V1hEv33-ZVgM5iZXpxrkl9NOk9XUSyXQBdn2pSn19xJupbqCwqadn3iNYGJaCyka1lSHA-JiVQoLsKf8hFtQfjVH8HVlmMbcrD9Wtvy_vYJIw_Hc5Ct-zim9dFjh9dHuNPF7sbo9G08FhyNT0ApcxEJ2KH8nbgXQyLX1E8l_Q_ew59yHkvLqVp3aKPdUB3iUqYRQDiT2VDmj252sKQCOF0K-Bi4gCgstNStHQvdn1qXp4RDXrQPHkqEmQVsYfa7xxnzt6uG80ZwiSf--WTmv-axdoyruRLlG2Y6poqtPIZHYPlAxkFKCduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_kNz7F-bIfzQU5kFLnu54v7L76ShtJkaj7KLQ5D8Ct9trm-pwi_x7P_Y7LSeno9K7_5dqaRmve4iIihAuZ6AYEUO7EG_qLzhYdySO6muSsbdrFmW12tv3f83warkd7W2Oy2ujW_U6eiV1EWMg38ABCTnoExzt4gj13fLQXGvGq6MnDPdRxY3S2gbQ5HPghRdJBtMBI9id1h2_yp_ZZispKpc0kpYSNeDtjpO2RfOGUdZ0-7nUrGlSBS68Ri1UlRMK-Tq-BiMf8RRm3Z1fOoQM_KSDX7SGBQevZwh04zCkJ-p87x8yv2xLEahq-iMgylfP-bySc-_FErRZFRRPuTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYuodx6HF90gi5DaP1YDTLWNVFitrRhE7nrB2K-nHfBI5z_17a5zWibrQj_hXogXQmxalkNdMgWyoMX6_18e5DGrJpIQw5MkFBswyxPwrmAlzOfkFkRKAyj8oF42M5lNB0tpEkS25LUfHvXdagcrmfwW8FfqaF6tU9rTkQ5XbO39h5z5nfdRzRwzj8CembH2aVd4ivQ32lWiJIv24LJWQPiKqK8Uyox7nDOZLmVxNoa62e3iI5IPJrcVYSiBwFo7ctQAjcv3ynWyJd6AhSF7xiyqYO7j9VU6Pow4OyjXzTZE_aFdCMmvyXpVy8bcWaFmrldz-yctULarft9gPZ9-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNn67JB8gDaRKzdfAVzbJwyRNPmf4ZokJigbKDJsVAC_adRKaqy8PogpQc9SRrxxjjv1-p8z4lxcz5anddtOpE36CJnW7SInpErPgYVv0mUVDOB4RmsFZxYpoeRHzWbv5AvmxvsodwwLEuzr3ijbxO3TfUxUhlBQrFOUsM5pPYwPn1r5K2RNIgbLooR6iaTEZXwHonORcoQ8Q9tTVq0LrH66H1habhrSFVI2tK_oDfKiw5kdWZoq-PKZY8VsAdE_R6pk8nHEvq5Z5TL2JNzs9soNJi9V4iKCAmigsGq2sUotnuCsrsu8kE6Zhzg49Yu7rPABixONv8TQDU0Y-anZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vL5YIIL4Ppp5c2x2mGgjj8e-zoKV_Ogro7Mo67NhvjWG2a7LkBVbWr3ecoBX0PQ1Ma7WDSZjIv-m_L22wi7O5csug1iTg_bxm3OGdKAMsXWzW-VG-C2fqp20WH5RpbdfazSOk0uErtqG12KozOJ6avbmS94m6YJA5ECiiD-qd_WpE7-DQOXqlMgQERrq7LWSybfaqa3NAVF91CRkxGW0UROE-5nQTQJuBRKAjTgS5U2zgGZHDkCQSXsyMLK02h6XKq5XZSFXqClEzYduisP23N8TeKWiQIifPvbI1T7JC9qHkS9oLiCJzHZiC7rsGfDkVVQWWl6es_2LPItpv0J1UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عمامه‌گذاری طلاب در روز عید غدیر
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/439823" target="_blank">📅 12:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
تجدید میثاق مردم مرزنشین آستارا با آرمان‌های امام راحل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/439822" target="_blank">📅 12:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دستگیری عاملان شهادت مأمور کلانتری باغ‌فیض
🔹
فرماندهی انتظامی تهران: در پی شهادت یکی از مأموران گشت کلانتری ۱۴۰ باغ‌فیض در شب گذشته عملیاتی برای دستگیری عاملان این جنایت آغاز شد.
🔹
مخفیگاه متهمان متواری شناسایی و  هر ۳ متهم حاضر در صحنه جنایت در محل اختفای خود دستگیر شدند؛ متهمان در تحقیقات اولیه به ارتکاب قتل با سلاح گرم اعتراف کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/439821" target="_blank">📅 12:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0221fca49f.mp4?token=BnbHFz40ujLWMqLIqGyl46TOxn86XoFj8kHUGZ58rkNM4qDH0GlSOTJYTXlwExZ1KpQJDULU0CSgO2JRA0kmSfrRmj8jnlByOqkNmvTTgFWoazLN8wrl-eEJch99Vyjo-PhE_hXcxef6X_9YI7B3u3BrZyFiIc_y663qgz3HyOOMnIYORKrzYq1pNJ5qqAmq6fTp3MXeM_JZD4slBom65-qyh5PRjC-83hLEKu4EQcvpWhj2K4xUoo1vJwxnpMLtBA5ZI4djpJ9IjmYd66egGwK-8V0plt4JsAlqewfdO2xgfV5YpEmVpdEV1eqBATx4nWmN7cRdCMQs4TNAhZc2Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0221fca49f.mp4?token=BnbHFz40ujLWMqLIqGyl46TOxn86XoFj8kHUGZ58rkNM4qDH0GlSOTJYTXlwExZ1KpQJDULU0CSgO2JRA0kmSfrRmj8jnlByOqkNmvTTgFWoazLN8wrl-eEJch99Vyjo-PhE_hXcxef6X_9YI7B3u3BrZyFiIc_y663qgz3HyOOMnIYORKrzYq1pNJ5qqAmq6fTp3MXeM_JZD4slBom65-qyh5PRjC-83hLEKu4EQcvpWhj2K4xUoo1vJwxnpMLtBA5ZI4djpJ9IjmYd66egGwK-8V0plt4JsAlqewfdO2xgfV5YpEmVpdEV1eqBATx4nWmN7cRdCMQs4TNAhZc2Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله مرگبار آمریکا به یک قایق دیگر در اقیانوس آرام
🔹
ارتش آمریکا در ادامه حملات مرگبار خود به قایق‌ها در اقیانوس آرام به بهانه مبارزه با کارتل‌های مواد مخدر، به یک قایق در شرق اقیانوس آرام حمله کرد و سه نفر کشته شدند.
🔹
در بیانیه فرماندهی جنوبی آمریکا در…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/439820" target="_blank">📅 12:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17981bcf63.mp4?token=OwBGi--sqp075GwJfekijJw9G2LIVK5gatCu4OnFmcNJ38WgR-n46vn0LlGTYcNALpdKDIepOPF4hWuI6C0dWWk5RmCtblHnzyByOARwhcfRJBvtEjO30dz2WRJJUel1J2JU7REwPHmPK-p3AXzx833yzdTnJhlnoBexQgzD_u3gMzXjJfWPd8ZSm810jMkUKblAqqOOv4_xrNy55FpU6onoaQTBFOFL7DUBxOLSITsNEUnL3J_wAS8ngk8GiVRt9lvPsn85Bl3uRPfNpflKZ3uJBTWFxvqvZssJUnPBCnI6SkQ9ZtWOU5plfnk-6OdXjWUCUYg96-IH4PlgTJo9M4M9AdEVfi2q0c-CYTrugvtHUlLgDP2fvBrXdlAmLgu7IwMGgmrZ8-R6nPleTNkQyMfGWjFfu70Ua1bumiHCGnLY9_tKS6cJrwLZoGM1TmLBAv2hq_Bnb-vIWxVYB_FbURHvNQY2wivDS0A4Ap6XK1lupPRduw5atuLfaAyh1G2pHbTt8Z7-msIl2dmIDguC44JWFnPRLorN8d3Pw9bOL9F8KU41zNxNgjayWttP4E3N7AnMocPEvgEjSso_Oh5eh_rEMkBS5R8IkQua7K8QEpZptSM6uHMhMHfhmUgFP8mkK-X_qcU9R8k87nAXS6HX7HX8F1EC6DTIUuEgC6FHplE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17981bcf63.mp4?token=OwBGi--sqp075GwJfekijJw9G2LIVK5gatCu4OnFmcNJ38WgR-n46vn0LlGTYcNALpdKDIepOPF4hWuI6C0dWWk5RmCtblHnzyByOARwhcfRJBvtEjO30dz2WRJJUel1J2JU7REwPHmPK-p3AXzx833yzdTnJhlnoBexQgzD_u3gMzXjJfWPd8ZSm810jMkUKblAqqOOv4_xrNy55FpU6onoaQTBFOFL7DUBxOLSITsNEUnL3J_wAS8ngk8GiVRt9lvPsn85Bl3uRPfNpflKZ3uJBTWFxvqvZssJUnPBCnI6SkQ9ZtWOU5plfnk-6OdXjWUCUYg96-IH4PlgTJo9M4M9AdEVfi2q0c-CYTrugvtHUlLgDP2fvBrXdlAmLgu7IwMGgmrZ8-R6nPleTNkQyMfGWjFfu70Ua1bumiHCGnLY9_tKS6cJrwLZoGM1TmLBAv2hq_Bnb-vIWxVYB_FbURHvNQY2wivDS0A4Ap6XK1lupPRduw5atuLfaAyh1G2pHbTt8Z7-msIl2dmIDguC44JWFnPRLorN8d3Pw9bOL9F8KU41zNxNgjayWttP4E3N7AnMocPEvgEjSso_Oh5eh_rEMkBS5R8IkQua7K8QEpZptSM6uHMhMHfhmUgFP8mkK-X_qcU9R8k87nAXS6HX7HX8F1EC6DTIUuEgC6FHplE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی حسین طاهری در حرم امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/439819" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌ رهبر انقلاب: دشمن خبیث در مصاف با نیروهای مسلح ایران دچار شکست شده است
🔹
به ملت عزیز عرض می‌کنم دشمن خبیث حالا که در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده و به خصوص خاطر مواجهه با ضربه قاطع چه در نبرد نظامی و چه در میدان و خیابان تحقیری…</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/439818" target="_blank">📅 11:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/439817" target="_blank">📅 11:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/farsna/439815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: از خداوند متعال پیروزی نهایی ملت بعثت‌یافته را مسئلت می‌کنم.   قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/439815" target="_blank">📅 11:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04aafbfb01.mp4?token=QSYCE0TxnmkWpG_Xtx5OOIu2AfyQnSFRgQVpFsM41hNU4FliomGjcx25z7w-ns2G8ap6mhOqGLl8SBAQ3B-F5gfeyei9XtpKOtDaA_3Dv8vcR9DpcyIfSkFjMotoUbLaX1_9Yh-YVYmIhPNyYlduZi1GHeB4EqoDRa9gP6syai6mxvoAXKETbgO7JeniA2YvdlyZzK16h2aT0fIvY4mqeEQp4Oxd6UwiRJ0_Bf88S9MOHtMOCqkadUG0NADfzz5flFtP_UxXADf0WUxaYZq47ppmOySklO9dW2VzYykPat53Pm8F9m6FEZRYrr4wJiaoz-rOISKlcGvVDkR80rOrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04aafbfb01.mp4?token=QSYCE0TxnmkWpG_Xtx5OOIu2AfyQnSFRgQVpFsM41hNU4FliomGjcx25z7w-ns2G8ap6mhOqGLl8SBAQ3B-F5gfeyei9XtpKOtDaA_3Dv8vcR9DpcyIfSkFjMotoUbLaX1_9Yh-YVYmIhPNyYlduZi1GHeB4EqoDRa9gP6syai6mxvoAXKETbgO7JeniA2YvdlyZzK16h2aT0fIvY4mqeEQp4Oxd6UwiRJ0_Bf88S9MOHtMOCqkadUG0NADfzz5flFtP_UxXADf0WUxaYZq47ppmOySklO9dW2VzYykPat53Pm8F9m6FEZRYrr4wJiaoz-rOISKlcGvVDkR80rOrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: همگان با ایستادگی، روشن‌بینی و حفظ وحدت و اعتماد متقابل و هم‌صدایی‌نکردن با دشمن، نقشه او را خنثی نمایند.  قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/439814" target="_blank">📅 11:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4176f5c05f.mp4?token=NgK-bAid2KElLVjDmUqZ4QVo38j8W5QPCGoxnTGm_ooJTLRAgVcIW1LJH7aQ6TyV6k3aeAy7_bTcacg73whYP94QCDSHrdmvSb33NT9b7ScIMmkGSVI0V3h6kFbCRf6hXsvfO0dOadB8jNuDBVP1Qoaee_YfP3FnaV_ReehJCufmvfn4LIqxPSBtI11tEiTRZcIuEXrxrkCGoajZs5nqmU691RgcelcojIwQK2_XYKy8KoBBa-kAByJkiiSP3Iy0hS0Hyb3IZjVqJkDX-2kepJ0PC84cDoNOSz4wHpxV-_eFaC1B6-UoOXwEsiRZHYg7KrGAXVkxRbiYN45CelF5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4176f5c05f.mp4?token=NgK-bAid2KElLVjDmUqZ4QVo38j8W5QPCGoxnTGm_ooJTLRAgVcIW1LJH7aQ6TyV6k3aeAy7_bTcacg73whYP94QCDSHrdmvSb33NT9b7ScIMmkGSVI0V3h6kFbCRf6hXsvfO0dOadB8jNuDBVP1Qoaee_YfP3FnaV_ReehJCufmvfn4LIqxPSBtI11tEiTRZcIuEXrxrkCGoajZs5nqmU691RgcelcojIwQK2_XYKy8KoBBa-kAByJkiiSP3Iy0hS0Hyb3IZjVqJkDX-2kepJ0PC84cDoNOSz4wHpxV-_eFaC1B6-UoOXwEsiRZHYg7KrGAXVkxRbiYN45CelF5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: رهبر شهید ۱۴ خرداد را به فرصت میثاق سالیانۀ ملت با امام خمینی (ره) تبدیل کرده است.  قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439813" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e059d45a.mp4?token=qsWkNwtvVHNdP-exWoGLqhexxM7gU7zK42cYecuiZdKU6GM8uOVRofcwLIorgGYlO7EMChsGcNVQTxdsTHtlrds4zpDoYslAVLSuDAcBKrKSeVCjqUIZY6VIhZP-bb1wJXBZFsFf8FpivjuLgJmcMTFdCQGYOtXlhF9pbrmohsEEzcz14oet3qXNEdPwoa4Wp2Gr2cRsQINYdyZpWWFUNxHCSXubzE_wwyAeUobwfyZxF_rGlQU_T-u5NwjDnbQghQORn5wVtll1po9yDaAtmNsdZYzOdpazpaPTAu_TivT3uaAFeFV_a5pGufOuvVV3NNk_Yao2dDERJy5gqzlYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e059d45a.mp4?token=qsWkNwtvVHNdP-exWoGLqhexxM7gU7zK42cYecuiZdKU6GM8uOVRofcwLIorgGYlO7EMChsGcNVQTxdsTHtlrds4zpDoYslAVLSuDAcBKrKSeVCjqUIZY6VIhZP-bb1wJXBZFsFf8FpivjuLgJmcMTFdCQGYOtXlhF9pbrmohsEEzcz14oet3qXNEdPwoa4Wp2Gr2cRsQINYdyZpWWFUNxHCSXubzE_wwyAeUobwfyZxF_rGlQU_T-u5NwjDnbQghQORn5wVtll1po9yDaAtmNsdZYzOdpazpaPTAu_TivT3uaAFeFV_a5pGufOuvVV3NNk_Yao2dDERJy5gqzlYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: ملت ایران با بعثت تازه خود در کنار جبهه مقاومت مایه مباهات ملت‌های آزاده شده است.  قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/439812" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658513c42a.mp4?token=R-73HFpJ1LQbibpD3NnKRwpwyIFRCqp42qJ6ewr4VF-al6Xz8WIUjlj2DPUFMKX-egRIyT8T9UpyNwGk_psOP-4ulyO1eghHOFYEwjEo198h517aHBpCidTT6HDI1enZ_ryTW31AKOirAtQS0k6n22aWDa7ipVkG-QWNF6J3X1_7xmVI-MJcEdHJlkLjCEOomyY25l766jlsJ3gjWKfKmepoy7p8J6q4-PjpZtdnPg9wqCtjYCx0iVjfAwFcASKbYIYWIRCsDEakpWmHKKmr7eX0lFFNLuOwlbKS5NoRovEyFBzuSpw7NODzpGsm4QA-5beEdvh33JgRlTZdeXx1hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658513c42a.mp4?token=R-73HFpJ1LQbibpD3NnKRwpwyIFRCqp42qJ6ewr4VF-al6Xz8WIUjlj2DPUFMKX-egRIyT8T9UpyNwGk_psOP-4ulyO1eghHOFYEwjEo198h517aHBpCidTT6HDI1enZ_ryTW31AKOirAtQS0k6n22aWDa7ipVkG-QWNF6J3X1_7xmVI-MJcEdHJlkLjCEOomyY25l766jlsJ3gjWKfKmepoy7p8J6q4-PjpZtdnPg9wqCtjYCx0iVjfAwFcASKbYIYWIRCsDEakpWmHKKmr7eX0lFFNLuOwlbKS5NoRovEyFBzuSpw7NODzpGsm4QA-5beEdvh33JgRlTZdeXx1hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: خمینی کبیر و خامنه‌ای شهید آمادگی ملت را کشف و احیا نمودند.  @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/439811" target="_blank">📅 11:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb23c1d7e.mp4?token=izJz0gw_3cIUDQqrEhd9UdkTS8rWzT7L-4RxcPeNBeFJ8eW5KuMhLEBs_7g3h-UZ5EYFnTro6fgPcEQRfsK4FF04BS0MaOeVNg2Dg6Ai5hr1QdQ6jW_HGfgihvN2UtvVhNvc2T4po44R4R47IXCAL3eCo1OSF4628xTmeAJK87dpgrL0cjarrOEu0yISHV0-cnzp2RxSOM3xRFFDgxkOsOPKAzW-0XjcBaG6V6eiqiggaHa-bJARS8FMSWM3w-GHxsZUfhKgkgVfZhsMUIRRhFB5UrkiBUYZEZ32lpmI8pmNntPkd2UYxlI4SviKjKlE2NvVbmhSj3ZZSyxONG8z4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb23c1d7e.mp4?token=izJz0gw_3cIUDQqrEhd9UdkTS8rWzT7L-4RxcPeNBeFJ8eW5KuMhLEBs_7g3h-UZ5EYFnTro6fgPcEQRfsK4FF04BS0MaOeVNg2Dg6Ai5hr1QdQ6jW_HGfgihvN2UtvVhNvc2T4po44R4R47IXCAL3eCo1OSF4628xTmeAJK87dpgrL0cjarrOEu0yISHV0-cnzp2RxSOM3xRFFDgxkOsOPKAzW-0XjcBaG6V6eiqiggaHa-bJARS8FMSWM3w-GHxsZUfhKgkgVfZhsMUIRRhFB5UrkiBUYZEZ32lpmI8pmNntPkd2UYxlI4SviKjKlE2NvVbmhSj3ZZSyxONG8z4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: قیام لله زیربنای مکتب امام است
🔹
قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره) @Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/439810" target="_blank">📅 11:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439809">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a450c312.mp4?token=dnsUpVdzR0n93UY-Bfw20AgDCjFQPSZ7zhp-25tpRtof7PiusVmD1eqJM5k57ozIYnTK6rJbVzHwzDxaq-S0TC62bq6hXD7jB5KxobcmL7G_KmlZxfHyw5gnVRbZ8cm2WpFpnWcPPlLpuhgyctg9rFXl8UqsNdHyfYm7TcOfqB9K942nTVK44aabdTampIpMKz64n1Bh_I7pN9NYWZzNmhkxq6YzeT9-TWt8DiJSlg9IdIFSXzsqT7P2BXN9NmgKhubLRFGl0aaaL1pdJkqFJN1oO57Ag2XrPQIJ_y0pdfz6K81FHNN4zzn_r1Kv55jgPPwilHKu2yZI9Dt0HqKQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a450c312.mp4?token=dnsUpVdzR0n93UY-Bfw20AgDCjFQPSZ7zhp-25tpRtof7PiusVmD1eqJM5k57ozIYnTK6rJbVzHwzDxaq-S0TC62bq6hXD7jB5KxobcmL7G_KmlZxfHyw5gnVRbZ8cm2WpFpnWcPPlLpuhgyctg9rFXl8UqsNdHyfYm7TcOfqB9K942nTVK44aabdTampIpMKz64n1Bh_I7pN9NYWZzNmhkxq6YzeT9-TWt8DiJSlg9IdIFSXzsqT7P2BXN9NmgKhubLRFGl0aaaL1pdJkqFJN1oO57Ag2XrPQIJ_y0pdfz6K81FHNN4zzn_r1Kv55jgPPwilHKu2yZI9Dt0HqKQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: درک و شناخت امام چراغ راه آینده ایران اسلامی است.  @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/439809" target="_blank">📅 11:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dde0fa23c.mp4?token=KjaTpQHwJQ4XkPX-5QSHEuhe6T9-0qLO-q5FULiRFDPHPyemn8J5eAqluu_8OiBaG9eUbnl-sqPGWsAXN8UcKRD2bvJ328xyiez1t10s2zYXexDf3RvhH_HQYvfrgsKUW2EnhROo54vo5xqEF0boIvVvL8vxqLTt6R0TqCPwVDv8SJVBV91nHerB7K8HWfdK1PgQ6j-D3vowwrx6NWgsg33Tf5dl-cRjFT7Cqvx5meAlB5y0VSah433t4zykLjaQiKEf-_6iibjVbAg_oCqjCEIaaelcFzW6y3UBMpgV1ejnXvstIt1kEhuiwEhZZnE5jooeHLP9bbKh0NbiE6o04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dde0fa23c.mp4?token=KjaTpQHwJQ4XkPX-5QSHEuhe6T9-0qLO-q5FULiRFDPHPyemn8J5eAqluu_8OiBaG9eUbnl-sqPGWsAXN8UcKRD2bvJ328xyiez1t10s2zYXexDf3RvhH_HQYvfrgsKUW2EnhROo54vo5xqEF0boIvVvL8vxqLTt6R0TqCPwVDv8SJVBV91nHerB7K8HWfdK1PgQ6j-D3vowwrx6NWgsg33Tf5dl-cRjFT7Cqvx5meAlB5y0VSah433t4zykLjaQiKEf-_6iibjVbAg_oCqjCEIaaelcFzW6y3UBMpgV1ejnXvstIt1kEhuiwEhZZnE5jooeHLP9bbKh0NbiE6o04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: سند افتخار زندگی امامین انقلاب تأسی به حضرت علی(ع) بوده است  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/439808" target="_blank">📅 11:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439807">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007abf53f6.mp4?token=WsIc-1Bq6crnpKYKaCLdJpJNJXlC8eUaAHwck5uSCE69WaMKJDEoJE8GLtqCq4YP2On1_0kWCYnPbbdks15ULleb_mJUGBSCEjn5Y3SWHOso0m11vLGJ3gDC1UL2fpeeYtpm84Uq1K5-p-tcqVX62_aFV9mwrEl-W7kftVZ7Rrd90n5X8jMxa4kXGpyjaCY4s630RRTa38_ZqYAxUo-O-QrqeKYVpIIGaDSLNIGsAmGhPJBeaXNe5K-XJhVXOZqrmd7Q2ik_W4jFYAMt11jMBK3aVGxwuyxA0w3v77xb3KxXDO3N917kOE21qHN0iU58SY02_GKzhzrKNeL6f0Miyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007abf53f6.mp4?token=WsIc-1Bq6crnpKYKaCLdJpJNJXlC8eUaAHwck5uSCE69WaMKJDEoJE8GLtqCq4YP2On1_0kWCYnPbbdks15ULleb_mJUGBSCEjn5Y3SWHOso0m11vLGJ3gDC1UL2fpeeYtpm84Uq1K5-p-tcqVX62_aFV9mwrEl-W7kftVZ7Rrd90n5X8jMxa4kXGpyjaCY4s630RRTa38_ZqYAxUo-O-QrqeKYVpIIGaDSLNIGsAmGhPJBeaXNe5K-XJhVXOZqrmd7Q2ik_W4jFYAMt11jMBK3aVGxwuyxA0w3v77xb3KxXDO3N917kOE21qHN0iU58SY02_GKzhzrKNeL6f0Miyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انقلاب: اولین ۱۴ خردادی است که پدر مهربان امت، مهمان ضیافت الهی شده
🔹
قرائت پیام رهبر انقلاب اسلامی به‌مناسبت سی‌وهفتمین سالگرد ارتحال حضرت امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/439807" target="_blank">📅 10:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439806">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e30e2ea4.mp4?token=nHlpghNQZU6czzUZMZ7VmRTkdmcIkX0wJXz_6nCxUjyTBdbezvUWZ__VXk4QXwCCarsZxELafEM_LEbML5AiPxoTdxL2P5m-CqhrM6d7Ih-GUoDmw8kIWvGPfhsP7QInmW5XK3HM0rnK7rSqqcRk4EmmE8Km73feGLWqr1hBuR066clJziztlUji7MbouwSf2Me3MD_ypKcVpmCpAu4Vvk9JfMIWhKvLHqXHcr2258XzYxyuZiA2gDSEaFRjfcKEASOUoLsLs_qdXKWlexVnYjzudHsVooT8PrOT2RO59V9jWHY1F_CzBsjOvgPbeYosaENv6R2CetqKNDQ3bCxmjXGr_R0WNz6SJqrg36RLpb3QYIgYlClOCfDylS6DReEUR1Pc0AnkCJBweNuegJBBU8Nc4MrE-SYNhh8fcWL8iVwwO3fMLoIFEjWE6DvnXAp9__SUI7zGnGOZV5l3gl3lTil---zqCjvS0s2tILxCYXhquj87tN4D8kjQKIHPCwvKeuIydW4ztPnQkYqTihTW1vZPEIMgqmE5t1SOe5lkrtFch-rlznm2ehsYo0L9CnYLC68NhbrNGCxjGNBMYQ9M5En1rSmrUnyiNBIpmXxUaQmvaUMxBexL0Y7KPNwdeBXmDmm7kHvHAQLpMUKPF3mVIBlHeSnKNLBxdkuHQdja9GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e30e2ea4.mp4?token=nHlpghNQZU6czzUZMZ7VmRTkdmcIkX0wJXz_6nCxUjyTBdbezvUWZ__VXk4QXwCCarsZxELafEM_LEbML5AiPxoTdxL2P5m-CqhrM6d7Ih-GUoDmw8kIWvGPfhsP7QInmW5XK3HM0rnK7rSqqcRk4EmmE8Km73feGLWqr1hBuR066clJziztlUji7MbouwSf2Me3MD_ypKcVpmCpAu4Vvk9JfMIWhKvLHqXHcr2258XzYxyuZiA2gDSEaFRjfcKEASOUoLsLs_qdXKWlexVnYjzudHsVooT8PrOT2RO59V9jWHY1F_CzBsjOvgPbeYosaENv6R2CetqKNDQ3bCxmjXGr_R0WNz6SJqrg36RLpb3QYIgYlClOCfDylS6DReEUR1Pc0AnkCJBweNuegJBBU8Nc4MrE-SYNhh8fcWL8iVwwO3fMLoIFEjWE6DvnXAp9__SUI7zGnGOZV5l3gl3lTil---zqCjvS0s2tILxCYXhquj87tN4D8kjQKIHPCwvKeuIydW4ztPnQkYqTihTW1vZPEIMgqmE5t1SOe5lkrtFch-rlznm2ehsYo0L9CnYLC68NhbrNGCxjGNBMYQ9M5En1rSmrUnyiNBIpmXxUaQmvaUMxBexL0Y7KPNwdeBXmDmm7kHvHAQLpMUKPF3mVIBlHeSnKNLBxdkuHQdja9GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب به‌مناسبت سی‌و‌هفتمین سالگرد بزرگداشت امام خمینی(ره) تا دقایقی دیگر در حرم مطهر امام(ره) قرائت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/439806" target="_blank">📅 10:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439799">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PilY45H3DoQGVa4Od1qLtJCZnO98Qtfqz2vQP3Cq2lprNvdnyfc6sCu-d5SZdg7KPMy-Hg7kF7YheGfyeNPqhtwvfTzykOJEpEHf179orz3xzO8ALVJ9oosAqckzWw41UFT8TGl1Dcv5xEFZW-hjPVM63hrggy7QLE7KH7DGcbh-DvUNgcKKQvcBgutVF9kkD6nGeRs_wWi6Dar1BJeQ6DxQUfCtJleR5v33rz0RfWyTJAtdBvY8E13vWlGLhbbtCwom_XMxSfnqyGsvDHn5Wnzc36_Yt2kZK6qzqv77IrsYKRFChk1gB81HNYeUEVaWubV1OHyawEYBXBUogS-QEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7r6ijWrs5fgcZbUgB9JZACPX3hPCAwoAl9XYhOeB_hlvmipquovbbStxLI3JDghODPpbSfg183oK29RcDvds3qss1gP20ehYEnf0IbzIokmKZo7np-O3X9hOgDixHjL64vLJOFb5SBrU0cIpuG6E6OdADjaACoZviD7rUSgBFozjF8NOw2fpBIikseJwXoX59HiYbPu7rgfbtdNZ1tzMFvGFUdQxAPmoR-nW2qpmlY0ANR3rrfm6_UvRTRYebOx6JeIPqa5PULag37Vz115oFLGrbgmUmVvNt9h9-TkS36UBYH75LO8jv6GdEZcXggjrS7_tWFVwXoAJWfqXmheJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7EMAUQ2yo_3tx7DYo-Gv2N3C5Szgw4tsHYx-p5KXymiyRyN7WVL6tVsHAu3bKi-vSJv1rgWxwAm1WiOpzHqAlRonL79qEpLcmG-HFndjpiRvorM5x9_u0zzGj0kaNEDzcvfQWawfvYQZm5AjzSSIpb5lqABMwCqRmXdsKNJKRMtPtCNUypW8mykJGAqN_r3iay603SrtYRFNi_G1fVPwMzO_Ynp43hvGimy_QBX2L_UMXKRdUrX9T_JuFKKXzA-527ts5GM-OEuNLPxHsU3iY3KTjXTA_KKQju6Z8Wj52aQbf6mAoKOyWVSXxdJicKFCrSfO-vc2imOV2EMC_OfCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Klg0nHELTC9sN45AsYvfEZs60TL43eCxO4mkAQi-wbUGL5K3WlpUbrZU0V-q134oGqcTmi0GcFCZQ6XD65ABFPsDk6peG7YT7TRjnYdFX4hAHWXWKHGE5CWOek9enqCM68nLSejKnUr4vNf7wz5Qb9JYcsAV4yLTA3Al3RDBM8MN5GYh8X8XHTVB_fDUfkB4LluOh8dOoolNXQGx1mFVys66Vqr7aGwnV53IJAbpRqLhWENdFotbs5oZ6Ypkcavk0Iv4PYMLDGx1HAnibePrwFRJZc72ojUWKchJhkfthrAe7Q6F8YMDMTbH5Lakr6YHnLJWvBL6EWf_zOTwv4cy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMQEEw9C1N9HJ4L6Js6O5Ca4gJN0jlcx9pRxe73IsdYjE_z8rqwrzlqERFqvd1-ZZ3sL7T4UXO4SjqI17BNqtSo-Tdrfy_1PPMFfLmQg5obXcKoKC8wR3bYk4nZWZ7C2Gx3x3EeRGwhosaoOcqCALdb0P5tj_lCFKqLF-NWqFpY0IPknIOFairBK2CJWHxRIFCQOkLJV2MVT9VKOguGb_46NrRqzx8PwnByzIiXZLO2kgYFGeLHolG7ESSisArMN81wPq7ZVlsWYWycUFkNQaEf8rAWi_CbMJvLnqX7Pxg105LHrippO2F0xMGuKxfKKYLSNm5R0ySZBLFhlTHZFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTtfkcqUXP3EMTsow6iyQjgggrBD-plU3SmErMxwHuFd2DabgGD-SVQuuqlUFfXwdtByF6YZ-v4e6BaL8NWlEb1v756SvMskV-T6k8PGlHs7itcdg1YM3DnyzSHgtl_y4vidU9H8_2J71VXJF6KV8_aryCxyhEHh2mR4FNlLyzodV5_JjxIEInKMYQsRo-pqjXHtNdhMX_pXEq5ngVuLi6iwcsHQI25V1oIfAsag9kRrjWoz-eeqlyERsq28LZEvdNL51uf5USlD2e_mY5VVToD6OGcpT8BTOO5lqUkeZ2f2oZtGQZyC_FjCfpJq1_GMdoPDPq06AjfWA6QYa3ibWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sm4UtPAJfSwXVXi0IaJZK4N3qht-CtSiu_NvGe8obSynGlplDcLX5RhqabasApeCirYC4t1_-RtgVTv23bv6lyh8T8ZMzMj6ibGHN_Fu3HthtVCblNTkRGJPrgE7yRTRmJDIW_gmn1QE1q6JVgxL8u4iowBIDwJDwmX-zp_iQM5lQ6SLtBDu0G4ci0ZZKa8kbUtW7DgztUiHattTbPhysMPxzcjTwkDbFoT63FD_UEzHg0MUF_TXnFATVPfMTotzmxEpqODC1bY4pAowb1edNuW-YSoRT3gk9VNObyGYDHxFKNdwNUUPDnMAinzepL7iTKYufXPwohx8186R2AHVXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سنت ۲۰۰ سالۀ ندبه‌خوانی و اطعام عید غدیر در یزد
عکس:
علیرضا رجب زادگان
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/439799" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439798">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwW4J6-J0P_k4e_RzHmBOyeXWwUTcrTZmfenSdyTikA-gY8XhhfPHdC0B8POsqx9wzd2JoryG__IspZzfLp2eXzNc0K_1gg6WoV3utRyYRC5nFOHpfYkTgtJ4aP1_GoQDAreoWlJOy3CbW_cm6tX6LbN5h9iTtBHDaH1DiTkdiniNnppiTmsy9PTagsJ2IsZEqUcKxBaV4FAjNP9SweZWQmXxlsMQHkWEiXpIm9mASsBw0xaeXqIiziydAgc1RLrA7DzNBsSGX68zaIyv8zG08CQycw_JxkzZkaI6SpM87AaEi8xBXIIivwBoRmSCSdBIMr4x0H1XwLP5WBr4D6dgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه، رحلت این عالم دینی را تسلیت گفتند.
🔹
الزیدی در پیامی تصریح کرد: «عرصه تحقیق، اجتهاد و علوم اسلامی، امروز یکی از چهره‌های ماندگار فقه و مرجعیتی را از دست داد که تأثیری عمیق در اندیشه و تدریس برجای گذاشت».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/439798" target="_blank">📅 10:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439797">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب به‌مناسبت سی‌و‌هفتمین سالگرد بزرگداشت امام خمینی(ره) تا دقایقی دیگر در حرم مطهر امام(ره) قرائت می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/439797" target="_blank">📅 10:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439796">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e690df03ec.mp4?token=ny91sQoZeG4Qe3mN7-ZWVhXAm0uC17FFPiVo7Pcu98F6LKTLq0thEQWoOktiG0f848wS13MQVklJEE2w8UJqkV1OkLg3hvBHlke4ZvBw2b4VuMr550oIwdGbLCU5HRAwkWYK0kZEtIGpmGfUKuxIT_of-fD60kMxyly2fsxWnpsfGasH2DSa1LdHGQJv9l228X9hJZlsFlyxCeqq6ovclgwYxqKzCW3RXyvE8guSmHRr699YVbdR8kIbLNnsMC7nv4E7bhr5rwBo3ptkcX5Mf-kQXImLgdyBncQNV2fJaAThVD94E8TleEUOe4z4xLIV1HLDE9Jjj6REXrtUFm4reg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e690df03ec.mp4?token=ny91sQoZeG4Qe3mN7-ZWVhXAm0uC17FFPiVo7Pcu98F6LKTLq0thEQWoOktiG0f848wS13MQVklJEE2w8UJqkV1OkLg3hvBHlke4ZvBw2b4VuMr550oIwdGbLCU5HRAwkWYK0kZEtIGpmGfUKuxIT_of-fD60kMxyly2fsxWnpsfGasH2DSa1LdHGQJv9l228X9hJZlsFlyxCeqq6ovclgwYxqKzCW3RXyvE8guSmHRr699YVbdR8kIbLNnsMC7nv4E7bhr5rwBo3ptkcX5Mf-kQXImLgdyBncQNV2fJaAThVD94E8TleEUOe4z4xLIV1HLDE9Jjj6REXrtUFm4reg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین حضور رهبر شهید انقلاب در مراسم سالگرد ارتحال امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/439796" target="_blank">📅 10:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439795">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8103559134.mp4?token=FdUW6yiEfkEcazwecGQjT9xiEPHrfcnWZsL8ogqxsa19yyuVYzmEowT70ozdvfBVckFOjwLL9iRRdlAxOrd-oJuF5-D_rHAsQq5HCWg-TxdACcbK12PGhLdYm4r3OCVuDgfbkeT1nncbRdqhp84eH00qUKDZXZhEKnVU95vzEKwxtiirXrybI3R86sLdAfPO7U0ec0lvtJN3Ptfbcib97AUBRJA96UfeK59SS-TXAHyTr5BZ87pMrD4k5CK6TLtm5SLtl3IcvA76DbzYPAFbVsqe5V3niAqBMj88TV98ZfxHejxUah3VXjk3Qt81jaz9flEes3mGIFMdFf4llGsO2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8103559134.mp4?token=FdUW6yiEfkEcazwecGQjT9xiEPHrfcnWZsL8ogqxsa19yyuVYzmEowT70ozdvfBVckFOjwLL9iRRdlAxOrd-oJuF5-D_rHAsQq5HCWg-TxdACcbK12PGhLdYm4r3OCVuDgfbkeT1nncbRdqhp84eH00qUKDZXZhEKnVU95vzEKwxtiirXrybI3R86sLdAfPO7U0ec0lvtJN3Ptfbcib97AUBRJA96UfeK59SS-TXAHyTr5BZ87pMrD4k5CK6TLtm5SLtl3IcvA76DbzYPAFbVsqe5V3niAqBMj88TV98ZfxHejxUah3VXjk3Qt81jaz9flEes3mGIFMdFf4llGsO2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور حماسی اصفهانی‌ها در جشن کیلومتری عیدالله اکبر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/439795" target="_blank">📅 10:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggNF_wl_csSBh8kQsp5TLCJ222Ou1BdfyXONFzaj5MtDofIiRGKbNRoRdEFoGDI2MzDCBefvgM66tseb95ZjyX81B886n25w4d6cvYPb27dlWTUqKpGogqXUISdwAMcAC5V-VkFuYYlhseF8S7_fSxRLWrQCiyFPsYP97hvSmtF4KfFK8Om8OlS3V1lhPgOEXtFQGfyYryH5wDBy39BQiYgT3Jag0SgW3bugYv9ajouwpmaTojnA7ky9lBkZA3pFF09Nc5XM1e9sbwua9ta8c4oVuVWrfq73JTnZQrqoLTYYgvhST4uAXh96q8OY_PeonDQXFZosFLxg1QG6qYlmlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSpLhNUX4XfFzT5S00GZlkkQOUui1XELj2VtoaGoE2AXTAmYVW95rw9XidkwJkQ-aTHNyt6XQEx1qijU4rnfLiOuj5M-6zFtUK_zYWOdp4TTyp-lskyHNbPRwPLQokppcTLTX2XtA6QeuujT_bTiFMoiCNfg7SEL-x-ppdiu1Q4k9H04woG_v1gj5FLh78X9RMZZU5cptrXFpNSO3bf_oT-meRIIA0UYx7C55vHsXWTfg9TTHeLwiFjMPld2ZcAg24JCM1u9qkOOx46XQrazx01LWlGO1opTUQD2PfiWN6OZaNxf6OWXrN_hY5S6iV8-gipfWXGcF1_goOUyAJ-vbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHOGFgeyCNgGXQq5m-u02SoftdjppiAp3xxKtKOw8Inqq7yVWvHA5qZrI-o5o2htnn6RBOZ5lWfqPBvCuNCxI73jqcISOAlOkPdVD5gPv7n6TTu5PjPMC7oOHYYdVjWK3TUvsUf6DSYc5pQDXv0SBM87kydgiGiSdw9lDfB4YvXMbDcaFVigGbfoZ4vfGYZaY51pFEEx7i2c-5_L4k695fKV6yB-COUBsyNDqWVBR7rS-e8ou2F4NQfwvvAT1XItKq4gIkOAaPzQypZxlct6l9XSQbR7WPurpENnR97JPdz7spNy-QqZDwszcMA9Pfh6golKRaJBfqfLNUHqs3HHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlNBdcQm5aP6v0MjAnzqErXceojw8G1VlNaeDPxkQBRGKj56cJK682e7WmNYebjzeOzYsqxneiLsO1eeEoci3pNPKYEEDLaZhOKiT9DiHHt7vKGf9FOCuV6A-cUgst8i3p9zQrnOu-eBQamnkeCssCPTC0fzYNAPQB24dQw4KbpFgqnPSkAgkv5gAvT7zQDZKJQ02XFL6TrgGigqOblnwmkRJwB7NPMg0JaWdaUw36n771DhKIoHd9woEwXTI78E3YFO3UuRmY04EQbFGiLCUu_0klBvnr7914WYd87temQu6fa4E836QBqLb_djefBKYHYbuOBmJf1hKhFZAxhvCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیام اتمی جدید کره‌شمالی به آمریکا
🔹
همزمان با ادامۀ تنش‌های آمریکا و متحدانش با کره‌شمالی، کیم جونگ اون از یک کارخانۀ تولید مواد هسته‌ای بازدید کرد.
🔹
خبرگزاری مرکزی کره‌شمالی ضمن انتشار تصاویر این بازدید خبر داد که رهبر این کشور خواستار تقویت توان اتمی کره شمالی شد.
🔹
رهبر کره‌شمالی: میزان تولید مواد هسته‌ای قابل استفاده در ساخت سلاح‌های اتمی طی ۵ سال گذشته بیش از ۲ برابر افزایش یافته.
🔹
پیونگ‌یانگ در مسیر ارتقای توانمندی‌های راهبردی خود با شتاب بیشتری حرکت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/439791" target="_blank">📅 10:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439790">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cca8912fe.mp4?token=O6RD73VxJqWO7AslDo9h994ev9AGwhgceqETVuKfImT3ehGLnbups32t6599szq76agDql9eBPxgBrBEPxXm945nRyp2IsXt8HvuxcDW-ReG3ObnrLC8P4TKstDpNDD_9oaY7_4fJgWaBFzWcSjWQb5trRl-VoCaknCSV6a2se2Z8hzRbsVFwZPZEBgGzN-ZTLWvCULycIHvxUTSOpT4c0F8qtSopPLQwdadnkFplr7K4zL_3o6wIxl2VfJsfadzMbRp8EJ56KbQdXYjAnt0WK37yCDRm1GhKRU5E2nnd7qjaCgJJNr2NWxNGuuTSVbZRYtENNjV9YAnci0JCA1qxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cca8912fe.mp4?token=O6RD73VxJqWO7AslDo9h994ev9AGwhgceqETVuKfImT3ehGLnbups32t6599szq76agDql9eBPxgBrBEPxXm945nRyp2IsXt8HvuxcDW-ReG3ObnrLC8P4TKstDpNDD_9oaY7_4fJgWaBFzWcSjWQb5trRl-VoCaknCSV6a2se2Z8hzRbsVFwZPZEBgGzN-ZTLWvCULycIHvxUTSOpT4c0F8qtSopPLQwdadnkFplr7K4zL_3o6wIxl2VfJsfadzMbRp8EJ56KbQdXYjAnt0WK37yCDRm1GhKRU5E2nnd7qjaCgJJNr2NWxNGuuTSVbZRYtENNjV9YAnci0JCA1qxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابَرپرچم‌های بیعت با ولایت در مسیر میهمانی ده کیلومتری غدیر تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/439790" target="_blank">📅 10:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439783">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm-raRdl1pcM-psE9euvTuXY17O7lbGMdtU-kcb8sXE-zpkL_KYiEvREFO1Lb3R-cVZR7pyTQXsl3jfgbvNtVsQYsKbxiYnSOeLLEXSeFPlqj533uFTOnfMqhXvtjuiTaB0pc54AWdcVpL-1y3GJXBHQncXTxlHLyEfho_J6w_SE9krXHQOv8tapfdaYnjDFcuZUaiDk8r77GfXBLnKFyWSZcCuyTHD2nAWO0CrztcN5wpv4nncx5KuGTb7xwCUOIn_ns9G-LvwdA6mk455shuFTN9JfNe4cMISuWMLE3I5k5KPM1hMJBF-J4Z2pWhc06E7tVV5sVuTSZS3uZJ_upQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DlyOibk0ikIUVUt-2du9wpAO33F6RpnywHSPlmaDuN_HUGRpOprDnJXTva8Ul5U8UX0iMKFqBl8ReseC7hMa9g9FTqO1hVhXEf1j6MdaANmSgzFaU93AV_iwc6sV74j9Iv4fkYnDqyVuA54ul7hMmSQ5r6lcMNW_cWKUhl_oXTnkMQ0Grp2bDP-JgXzrx6VMyGsA9ox5CrqS1sF9lAXRfcHdfT1BW7vkXSvSGWjdaaDG5iaO3t0eXXiAsWNTh0ybXxNWDuyOIkLPtsbkosAa5Nq9QoHvEKsHlEghZNM_S-Q9dbZ4xNowtZ5mwdOeMzGueCjD1bc6kwgAEUMtebpJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAtqZr7xA2RQcVENPWnVeeN3e9G4QoFBVHHlEpMG3czB5_Z8d3TB-rtQUaT3BMjoCgM3AizCDz3C5fVuk5ArT1-FWMGcmdN6jX4iFQF7YbXayJXy8TAtISyeZHeLMose2-4oNGRzMQrexRiUwaVohqcTC5jyQfkE9OK98cbdQi0Yy_y4nBYULTNP1bF-0XvEjNCW84t6ry_KelMzGAuMyMsI0AX-iMiDIg2VEgXACR4bTWctLxcp4VXnR7xevKlKjfv6KK9_mpZdTqki8W9X3a3x7eK1sb4i3uMMXikjlsg0pWx2dbF-avDvBrnBDowJB_V22vUeK0EzJzLSRCOFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVHwcm-GxhEGG_dppupNjKi4AsWsqBtrl7-YqZn_E1CwtVatohX52IPi9IgRFvSF8GZA2EQWiYqPmk6JcbCOEe3G3gcdVQ9iRobeSOxUHCPB5hizxOb3Ch_PQURLCkFvRFBG0Z3BpbRM8alnpgyDFIKM1ytxDQHGN-SZXr8hXw0epeW70IEqjXkgT7vMYroC8aOTtHZEgMDhRvAME78odcOZ8Wwvv0NNn9RG19xRXaYeicWcgZJUZU0qr298lHO4MR7W9cSo_W227zBfbGuK0XspMGJ_-iGIOaALAtrcmxsllXHbicMD1CEubD2U2bSUuHrydj9g6Lf3Iuqx5GlrXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJ78Rucu4RhwO1QzE8f4lgbmWuNwprCFCh8lKx_Rpq_CfhnWjZJiqN6RQz69LD1YDqABq7gDPXXg75d0oSv5MlGeXrm8mp1ptiE4MxFqeZakMF_Tuhq_chqfFQ2FgCy3znWqHK2jSMsDwRwCrDHR1pupOBQd0Ccf6Va68t0K8C92rXu53Yk8E0i2x0gU2p7YlpDApWKxAiiJ9TPdHN_aYwDjnLQWH3t66MqpyM1J60tkAFDYc9m0GgZUr984o7y4RzNCxrjd7UA4tYsFaNphRijWsoUmQeMrGsQ-kmLMzkwRLcmPymJniV-X9s78Z7JVpLzpoDOVmdFEr4RyEwliUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw_SIm_RehzXM5nFNa5_vGvqJ4XZCk4Pwndr8rqt2UFb9klR23RipBdoeHPxtPNFTECesqHbo-AFqN8_b1SZcSOl3WrhvGfwpOsekldUOVvcOQZUt7vvdJlpa_dqm7q9LfqxfJFs-Kz53DVsS5tlThKRS89pqkhXWgXaarpXQuZc6_ONlxvs1_0j09RUmFcXpYOrfXTu39BNMmjJz4HBg9F-GzH1CP8uzR96P9Oib3rjwMsbgeOrlLv3mOw5Ji4GA8RGy4ZpxfXAVU9SF-xnAfcR2ii4GKANMh0zit_WhWBSE1cG9E64YEHgN-OI0w5W_UdOjyiyJKg2s-oW3N8jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQ1NdKnjPswBrveSIuMruOq7gVnr2Hgll0OC2N8i4E6oVcaxw9vqK2z6Z29XnMot6fj1ZeLnkgDoazrruqT2NEtYwlOiP6WPpGtJ72Wfa1Zt0g60SpmVU7cLPTuok2kC_Odba9kFugvw3fc_CLBXxC4B4l4GomWl3kk1DNU4nnmgntOtxIQtGzTPBY1QCmfhwIOqpzrzaUx4_JCpv4XEQIa1szAzchD7MuI-J-mdlEQPLgaGmjzfS58R8goEqeLMQ9GEG5YPmy5-DrZFEPJtE-GvCrF5tAQwAtyUH-XQdkm-DOCiNEnMYQPWjbLbOnpR--VqB7lDdUkY4a_k1Gv22w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم سی‌وهفتمین سالگرد ارتحال حضرت امام خمینی (ره)
عکس:
هادی هیربدوش
@farsimages</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/439783" target="_blank">📅 10:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439782">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e653079661.mp4?token=HHrl4iWSUL6x48OyoHnrdfFQKk0-_R0H2A04SdcgzSw5H5VlhtPAW5zutCnhiBNJyeV6P1JaxowILWBjQaRf9wJJC7ddhgY4G2o3KDQ4NmaIkKwfisN6ts9qurc4NTWe4cKoTylIS6qzSadLmSP5T8ch35O_3jEXeHTvWtJTtSUNUWtRt2D5miF5VAN2XP0XaAjKPBEFSDkAk3kpmM7oUBUb5k3BYwTQDLl594WosdCWktCO9-C1jH8n9uLoD7PkwTSs_uIfsby6ArgiCQlBfHo-VI3QfmPbsd4KduGF5R1qe0KsKahg1BzKXN00sWgIJG_zJcMg0H3AgB3_gRRxug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e653079661.mp4?token=HHrl4iWSUL6x48OyoHnrdfFQKk0-_R0H2A04SdcgzSw5H5VlhtPAW5zutCnhiBNJyeV6P1JaxowILWBjQaRf9wJJC7ddhgY4G2o3KDQ4NmaIkKwfisN6ts9qurc4NTWe4cKoTylIS6qzSadLmSP5T8ch35O_3jEXeHTvWtJTtSUNUWtRt2D5miF5VAN2XP0XaAjKPBEFSDkAk3kpmM7oUBUb5k3BYwTQDLl594WosdCWktCO9-C1jH8n9uLoD7PkwTSs_uIfsby6ArgiCQlBfHo-VI3QfmPbsd4KduGF5R1qe0KsKahg1BzKXN00sWgIJG_zJcMg0H3AgB3_gRRxug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)   @Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/439782" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439781">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sGRvxjjoIXHzW_EiYMkssPjSBW61_LxzHA3v2tAv59QHPidwzsW1UF5YTcTwWmsC4OVxJDLvdGnFL9iGi9aEMku_gYN0c0RYYIcT9IgmLSit89dcBqlMgYRuv5O-sA1aYZpLkA8F8i7zUFgOK3oTlZV_0hhh1NQrPATM1H79rumKygMNSRXSaHGErpweyrLgJl4ufAxoFXKx1YeJtHnkDcVONlMkX18lqhrqZpjRRqqop4hUxfNzMiJgEe20KmyZAXyyfKHPBfjPFBbFbo9FK7jMpCeqaYQne3kFmd3sq0xuwM-FzrjCQbhWKRTg1-ZHNJDkJp8eN0ZqDbBia6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدی اولین فرنگی‌کار طلایی ایران در مغولستان
شد
🔹
پیام احمدی فرنگی‌کار ۵۵ کیلوگرم کشورمان در رقابت‌های رنکینگ جهانی مغولستان صاحب مدال طلا شد.
🔸
دانیال سهرابی و محمدجواد رضایی نیز در ۷۲ کیلوگرم راهی فینال شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/439781" target="_blank">📅 09:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439780">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
آخرین
حضور رهبر شهید انقلاب در مراسم سالگرد ارتحال امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/439780" target="_blank">📅 09:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439779">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47cc1de4a.mp4?token=bKil7-lxbs86qwzDi2oxwPnO-d04OZsD0G0opJmxOfecSLb9NV3vFuecvG6s2GAkG1-HjIYIL-OmvE-vQ44Qo4EJ_OF3sTSdW6ogE0pBhI1czt3Znli6F4AW33J4QC3l76sSotITWKQAhOc6xkaM8GMWQf9PqCBgUCsufClQDwAJPXgUeZDmYh4ymB8OCiwnt8OwW8OrJhL3XwtK-nxKO30zcG-mBHRM3f58YjAMTwxYOs9vKNqugnFxDQaU5Xu30wSpyuwkaL8CQCe3gxUZcrzizsRUyas7tzfUkKkHItvWiRiFar6XiMTq7C5buX11iaKpJuGvCiA7yTfcdV98-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47cc1de4a.mp4?token=bKil7-lxbs86qwzDi2oxwPnO-d04OZsD0G0opJmxOfecSLb9NV3vFuecvG6s2GAkG1-HjIYIL-OmvE-vQ44Qo4EJ_OF3sTSdW6ogE0pBhI1czt3Znli6F4AW33J4QC3l76sSotITWKQAhOc6xkaM8GMWQf9PqCBgUCsufClQDwAJPXgUeZDmYh4ymB8OCiwnt8OwW8OrJhL3XwtK-nxKO30zcG-mBHRM3f58YjAMTwxYOs9vKNqugnFxDQaU5Xu30wSpyuwkaL8CQCe3gxUZcrzizsRUyas7tzfUkKkHItvWiRiFar6XiMTq7C5buX11iaKpJuGvCiA7yTfcdV98-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/439779" target="_blank">📅 09:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439774">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ey1XV78akM96460uSMEt5qPWZcfxK89RWd56gp004PpdDvlwTEZOiLzPb4OtRvX48GD2t-EN7VeU0-SjH2Z-ir-74VOvJxba34WkEKgjPnU9hA0tLVnghDQ7hesz0QF215p4ycIW3-MPHgMDkN3u4Dz11zAB7x7Pe7MPyc_BrB-FEhtiXW_n6yofaZQSx2ZyQIUOjHNWj1Qa3DPYRAyCtYREf8e2VBA_XAAJJpRx8JFSn09edBEPMenJvAQwMhvoPawDfT-tpuZ48tEQK0rkGkdDR2ECy-iBG1X4dKED2wv2Tf6W1mHyoAVMmSikPbBmINKEpG5J0znEUlZh1J6kGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-32MTHlrX9HD1Pp9aSI6EWiM6Ffe58gdZ5iYNTtq7JREAxsrjjIl6BGy16cWOmQq8xuUX_qlFJloQqSjq8H6ffRKV8kIfKXsvjGnn6UJ9rHY0j4JY30EflPbyAdXAHbpcxFcRAcgyUJWawwTvRafQ3sRZSwKgB8szEmHTh3aH37DgmIgupXPSf5EKZs81mMX58L08zbk8axr54AmYJRQbF_DHGZC3my66z3lELTB2_bF6KDV_QQBun77KbCXsn5KNagRoUgcRWUq48Bt_sN8wuj-gMM8fnSYdNEYwOBuq1ij3KLLxObMcB-eFpZgwWV8NwrZsvlXw1v7fJ5xFUPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2XE8ZpUHscqM0wHHhyflO0F_g-m4JX5Q-5UsGK_-ko6E2wiABWLwHJUiZPGKkH9NLB2SyADRVWE21NEV_uB_Edfr-ObyRVpYBPyKcxzI7BKu5GGCp6NUmZPgVkMdzuoPQHxt5BBX98zxSRhcM6b8zZzrdm2kQ4BbCSD2B4I1AqNtJR4jECXl3ZQplfI2G7V_Ourrs0G19RMFuaBmOtAVK-sDsGTYXhRbwUEejFnmsDdaNYlsWS47d3MlGNAD7L2EXp5eJ3d0w_at099YOvjUtb8yBL9fC-K_wLS1kFF8b5i0HPB8lkiICYy8z4yHwEm-rsYyfsTFC5WqbdgxkdLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egsZwhRWpOhpKQZqw0UbqfTkpvdmVm7tVDYa8RfhoMBKEZqXP6ze8ulbd6zhVqV_QCo55fDnCsFpQ-jx45MnTTgh8mST5nBinzRRYaSeepZwY2ykmklbJBy1qKVX3rEUjHxXZe58rY4vB2USYILUi57CImxi7QzzOkjQDv1ykaVkDLpPC7EE_wV8RS3IOuB2IL-0gpLHWmlc-QHs7o7Sdf1qmm32Mn-sSZ_t2-Bvi1G2Bz0uHE4TlJvwEnMahIYq6ieUq-Fd0Yjk00O15j9eMwqmC0VGaOZ1qIt7U1OA8PUzS4W81gdejJS9V546Na6_jjLCQ9MYnJOoCZeJx0aC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsNs3emvq-ka8oZHDDouolF_XjXsDakK5WH2qBVE7I_MznE0SnfuR4Ii1zSXRIDUOjXUnTMRceQulv3zRQZQtgHQAUlsIkwxnSC2sSMsAzYcC7IWuJx-vJM3FugSpJy00f20PUpNddRLHUNkyxug2usUZfC-jj5woj5HFukalZhO7o3xMhAdhL42V5-EHCkmyuChwui3OFoihO6rTnd2StOyY3WTBBr8dt30Xawu4ynfvhOgnbyM6nzOyhoK4Bv-72FzPKttuiiGrCZ1i3Lv-uU_3wRqDLj_pCrDgd84bY3T5p5Eo22AtbeM5AJmmoQ_i3LO13EX3OyJizNkPPUymQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مهمانی خیابانی شب عید غدیر در شهرکرد
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/439774" target="_blank">📅 08:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439773">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=EKIWKmiLBlhefZbhzc4Qk6fN7oGceHLPTCj3vImHXCTMx0kJpDkki-cmZbp2ScRpXlqHQ3yy81qF8eYUE4u-Xnf1ZY4K48mKynPWZKS2uRSLrJxPZmMt3qX92XFWchDPMzyrg_7EnGXd56Pf66WtNKnE0Yk3evC8Kxo_2eXiojTXtv1Ri-6OkYpF_9bIYPlYRQwXPCuN6aCwrQxAGEhGLpIaJG6Y60jWgbsxikGxnE2v2avpuJOc-KzfullFfjbN2sU7KA7i-DQzc0vz-rNg_VMfS93pAIAhgdWXckIZOtmQ5fD05yfM4mspFcID0o-Ht7CWgDbZija1xxv3Bo59vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=EKIWKmiLBlhefZbhzc4Qk6fN7oGceHLPTCj3vImHXCTMx0kJpDkki-cmZbp2ScRpXlqHQ3yy81qF8eYUE4u-Xnf1ZY4K48mKynPWZKS2uRSLrJxPZmMt3qX92XFWchDPMzyrg_7EnGXd56Pf66WtNKnE0Yk3evC8Kxo_2eXiojTXtv1Ri-6OkYpF_9bIYPlYRQwXPCuN6aCwrQxAGEhGLpIaJG6Y60jWgbsxikGxnE2v2avpuJOc-KzfullFfjbN2sU7KA7i-DQzc0vz-rNg_VMfS93pAIAhgdWXckIZOtmQ5fD05yfM4mspFcID0o-Ht7CWgDbZija1xxv3Bo59vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای با وضوح بالاتر از خسارات وارده به یکی از پناهگاه‌های پهپاد/هواگرد در پایگاه آمریکایی علی‌السالم کویت در پی حملات موشکی ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/439773" target="_blank">📅 08:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439772">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بخشودگی کامل جریمۀ حق بیمه برای وسایل فاقد بیمۀ شخص‌ثالث
🔹
بیمۀ مرکزی: همۀ دارندگان وسایل‌نقلیۀ موتوری زمینی و ریلی فاقد بیمه‌نامۀ شخص ثالث، می‌توانند از روز شنبه ۱۶ خرداد تا پایان ۳۰ خرداد نسبت به خرید بیمه‌نامه اقدام کرده و از بخشودگی ۱۰۰ درصدی جریمۀ حق بیمه بهره‌مند شوند.
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/439772" target="_blank">📅 08:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439771">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0322159ad.mp4?token=JX0qumBEVKuiNB4Su0ACIQ_y0OqnObpd0nk1bQCv_S4U88Qyz1e4L7GdKrbUuPNdUH-X0ztOPzvQ0jPnpIWcZYzohQ77_RHsZfocZcfKHUHXkQyb7aHRPR4Eh-6q-_sfiEai8wQkZBqg2kuMLNQuxI2rL825Y0zJY5hS1eQYmVumdBaVxWPVBfx-u_8MWore7tHih0wVHiqaHCu2icao7lYXW-WVRyMr9HAKiLYx56qsqX06NkNx21HfpDCn7gQSNE6LtgACMWEM4IUT8F7g2V8WeiV013zma74-uFM4fQkikT6djHSVnwasGscXHoNRwDOKI-YzK9rL0Qr57YsbWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0322159ad.mp4?token=JX0qumBEVKuiNB4Su0ACIQ_y0OqnObpd0nk1bQCv_S4U88Qyz1e4L7GdKrbUuPNdUH-X0ztOPzvQ0jPnpIWcZYzohQ77_RHsZfocZcfKHUHXkQyb7aHRPR4Eh-6q-_sfiEai8wQkZBqg2kuMLNQuxI2rL825Y0zJY5hS1eQYmVumdBaVxWPVBfx-u_8MWore7tHih0wVHiqaHCu2icao7lYXW-WVRyMr9HAKiLYx56qsqX06NkNx21HfpDCn7gQSNE6LtgACMWEM4IUT8F7g2V8WeiV013zma74-uFM4fQkikT6djHSVnwasGscXHoNRwDOKI-YzK9rL0Qr57YsbWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دره‌ای شگفت‌انگیز در قلب زاگرس
🔹
تنگۀ سرسبز شیرز، یکی از چشم‌نوازترین جاذبه‌های طبیعی غرب کشور، در ۵۵ کیلومتری کوهدشت و در محل تلاقی استان‌های لرستان، ایلام و کرمانشاه قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/439771" target="_blank">📅 08:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439770">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022cea969d.mp4?token=qhfVK0LapYHwcWeLbQFb2V2fFAMBRQ0UTIyAyRHyFF1tbK9p3MC8L5KjzpyyW3xsPbWEvYqZWo-fmPcEia60M4renb_ffiW51HPhRHHeSfJqsAMciwTadCp9GP5a02U0ceT_aXOhM90mRI42h0n_iHJbm1sNwjH8hcxR8U9-2Feyi5Y4jNMeR7ind0IKtDWj1kE7uYxyYF1Cw9JIiEhXviNnYo4oSMd30KBp30HtZ41VExI4VBXRmN5l6iV4ddPVgpl8QerHxjeoOzXlVq6qR2BYDb7RF7f2-9w5nlF529P8dlFtx96EkGu0DEOvVr-2BIpdQIDI7iVKtXrCjv7IDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022cea969d.mp4?token=qhfVK0LapYHwcWeLbQFb2V2fFAMBRQ0UTIyAyRHyFF1tbK9p3MC8L5KjzpyyW3xsPbWEvYqZWo-fmPcEia60M4renb_ffiW51HPhRHHeSfJqsAMciwTadCp9GP5a02U0ceT_aXOhM90mRI42h0n_iHJbm1sNwjH8hcxR8U9-2Feyi5Y4jNMeR7ind0IKtDWj1kE7uYxyYF1Cw9JIiEhXviNnYo4oSMd30KBp30HtZ41VExI4VBXRmN5l6iV4ddPVgpl8QerHxjeoOzXlVq6qR2BYDb7RF7f2-9w5nlF529P8dlFtx96EkGu0DEOvVr-2BIpdQIDI7iVKtXrCjv7IDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاه خالی امام شهید در سی‌وهفتمین سالگرد ارتحال امام(ره)
🔹
صندلی خالی مزین به عکس قائد شهید امت در جایگاه سخنران حرم امام خمینی(ره) حال‌وهوای دیگری به شبستان حرم داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/439770" target="_blank">📅 07:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439769">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
فیلمی دیگر از شنیده شدن صدای انفجار در بوستون و رود آیلند آمریکا
🔹
منابع غیررسمی از احتمال برخورد شهاب سنگ به این منطقه خبر داده‌اند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/439769" target="_blank">📅 06:54 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
