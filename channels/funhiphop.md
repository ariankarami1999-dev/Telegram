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
<img src="https://cdn4.telesco.pe/file/YRlf3yV0WdkXmhC3oijvY43JLq9KDyfua5r5UDzWKAjbm7Rr4hggLWzOzBTU_Jxphayv4Wtan6JHmLIdBTKPcoV_kt-Y2ACebKwJBE1e5xmjhhcNxHQzLujjL2loBccfF0wKRLcc7AqUOb8E4fpMt0Go-8uO0wwpwqUnc3bNnJbvHDyuN1R_Eivi7SNzC7W_eCaxHmbzf2uA3-eTVYddvyufqghtvyRnMXfqsFZ27rdhJOT3xiQxsEDUCZLVgg9OUSE-X4I_USQ0GiJe00eTsDXzNCjBEHJJ5C8d2KLJHfaUx8PHB_PGbvoWQ111S7PH8-qCXG9gdp4_tTtnrV96BA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 139K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 20:07:55</div>
<hr>

<div class="tg-post" id="msg-74789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9tJ8d0mI1y4rgHRnO8FoiIbiyYC-puo2fRea8ySWFDLv9hQnCouKBM5DUYtl7s3O53_9tu4s-ejqbKqk6GTDMhOfX1HpEKv5P9IsL3mM50cC5VxM1EvilNHoDRnCiMm74C5PVWSdNBNzOFUxqmqVFmmQFnjmhkSKIOktipTh0_riZi_tTtKOKCn2w-8ew-MCvN-ZT8TNQectllRh8x4-22FPdlxQemM8Hpy0ptZC3xXJGtMYziXtKlQ7ofAPF7_6c4fcZ9qM59-4ZBjiOVO45xH_-ddbli0Yox20edF_J3Nyb9ykVLXjGjcWhbycmq-vaa8Q3mRxka0BMDd04L4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه شب بخیر
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 286 · <a href="https://t.me/funhiphop/74789" target="_blank">📅 20:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMhxqPnyIV7mFtLfUz06iIL5nq1I0_eS7CNhjvgNYEc0cyVA41mQrIXwL8ulnVrwonbEeJD0xIV2PgR72GJTOJprtCXu1uYJ1Ur2A-ASjtAdQrbLL7flj5Me67O1NE02rpVDUfUu4bnA0Cr4jkB1mmx6Ljdwh3YA-zdBazspF-n5lsW9lOVuak4NMfpZFIpOTqpQ4BTKnUULC5vQ8K-Ub-Q7Dexm0R_OmIgKrStukmvKynSJPwhJV8gpW3iYzAaDvzgEKiSvqVWrdgw-pbBf9FLJpiwq3mlbeRp8txDNdD1nEhE2VDCwnj2P-IYsxeC7EO1ranie7JeQUfg-kuNjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره خبری که منتظرش بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/funhiphop/74788" target="_blank">📅 19:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فون برند
🔝
فقط با برند میتونی آفرای ویژه ببینی
🛠
🔵
سرویس های V2ray    1G
➡️
230,000   2G
➡️
460,000   3G
➡️
990,000   5G
➡️
1,150,000 10G
➡️
2,300,000 15G
➡️
3,450,000
🟠
سرویس های open و L2tp     5G
➡️
1,533,000 10G
➡️
2,830,000   با برند، یه کیفیت برند رو تجربه…</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/funhiphop/74787" target="_blank">📅 19:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMilbFakx51XTw-OlUgiel5ZyxBwJn8DST8SMp-A2xSmD5OW1qiO5yeG4PV1GjpfQHXp0RUb3tuqJsrvHtKwQvMgm40MSU86FKHhq2cl2lQGg5H-A4MrlfZX2_9xBVYZbDXoKgjKBfGhApnctZRTW51cTDJR0Vnh1Ql-FK3SznWAzYnZskyoIUbmZ5WyKvXZOAaeP3IphmHnVqyhqCzPkPuiePN1SB7eFW-u3YfN4Ibon1dyduJfH_a-1mYb2UnpR9CCloNQgL9sFQ9M1GGA61PhmW48rIPwUR3h8hUkOaIY6fbxYAWxY6Q2wqkOwXPGSRnsX8aX-deWX2Cb6TBAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فون برند
🔝
فقط با برند میتونی آفرای ویژه ببینی
🛠
🔵
سرویس های V2ray
1G
➡️
230,000
2G
➡️
460,000
3G
➡️
990,000
5G
➡️
1,150,000
10G
➡️
2,300,000
15G
➡️
3,450,000
🟠
سرویس های open و L2tp
5G
➡️
1,533,000
10G
➡️
2,830,000
با برند، یه کیفیت برند رو تجربه کن
🦅
@phonebrand13
✅
@phonebrand_support
✅</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/funhiphop/74786" target="_blank">📅 19:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پدر احسان افراشته (جوانی که امروز به اتهام جاسوسی برای اسرائیل اعدام شد) با شنیدن خبر اعدام فرزندش سکته قلبی کرد و در گذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/funhiphop/74785" target="_blank">📅 18:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74784">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روزنامه های فرانسوی مدعی شدن گلشیفته فراهانی و امانوئل مکرون رل زدن برا همین کله زن مکرون ازش کیری بوده  این اولین باری نیست که این شایعه پخش شده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/funhiphop/74784" target="_blank">📅 18:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روزنامه های فرانسوی مدعی شدن گلشیفته فراهانی و امانوئل مکرون رل زدن برا همین کله زن مکرون ازش کیری بوده
این اولین باری نیست که این شایعه پخش شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/funhiphop/74783" target="_blank">📅 18:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530c2c0a1f.mp4?token=Mpivqe9TimKgN3172anhfDpiFXagONP45Ns32YHA3CbP6k1H_AeVtRDHwldCnEbUSGpl0pf6vDeJf5wybUdYY6Jmyxg1Qjj7-HpRS_4FwkiX-MPaOJZJFK6gRfP-P9sJmS3LOKay_ueMh8OpVdplwBrstJOoCaIwRZ8LCeczNDv51_cV-CtnuC3EwCJcfK1TMzYncspVrq4rA8OR_GRJEqdL6aEiH3Qooa8p_Qhpq2FSEKXoOAH-FX4hYEPFhYQ8mIIe76addjNdT2D-PQDSJwXHyrN820mbJV-NSlS7QneunWDx3FdX96PhQuI7d0N0CqyBpKJad7mt69qcCcZTsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530c2c0a1f.mp4?token=Mpivqe9TimKgN3172anhfDpiFXagONP45Ns32YHA3CbP6k1H_AeVtRDHwldCnEbUSGpl0pf6vDeJf5wybUdYY6Jmyxg1Qjj7-HpRS_4FwkiX-MPaOJZJFK6gRfP-P9sJmS3LOKay_ueMh8OpVdplwBrstJOoCaIwRZ8LCeczNDv51_cV-CtnuC3EwCJcfK1TMzYncspVrq4rA8OR_GRJEqdL6aEiH3Qooa8p_Qhpq2FSEKXoOAH-FX4hYEPFhYQ8mIIe76addjNdT2D-PQDSJwXHyrN820mbJV-NSlS7QneunWDx3FdX96PhQuI7d0N0CqyBpKJad7mt69qcCcZTsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز خیلی عجیب و خیلی سنگین دارن به جنوب لبنان اتک میزنن
جنوب لبنان تبدیل به یک مکان آخرالزمانی شده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/funhiphop/74782" target="_blank">📅 16:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74781">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b397b8f97.mp4?token=dd37Wg94kRBXlvyeJbzUBQdy5boWarhnZ3Xa0S2o0FdZvcQDtOYjIaOBKgf5lY9gdkDwfhKxRHSQuSuxbslxQT99lHVTUzjSQWKiFcT4Z_mzwJ1ebDa0qP59baosB8yUXY3JNcbErBQzthX80uL1l2aLOSY4vH77rk6lzlkNjz9wYJiThIjCvgtaqJzhD5ubjNJ8N_YjA8UkvoKiFZub_MmlYTgk8OfLSO9cByuioDBmz9a-3n2EyTmZlTtFqmhWfQUPsnZrnrssbzT6dvbrMXuBQQvsLkWhjPR9v2c9E4tB-_V4AtQxeJHQllyog9sOqOY80f99LecCHo1veZZb2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b397b8f97.mp4?token=dd37Wg94kRBXlvyeJbzUBQdy5boWarhnZ3Xa0S2o0FdZvcQDtOYjIaOBKgf5lY9gdkDwfhKxRHSQuSuxbslxQT99lHVTUzjSQWKiFcT4Z_mzwJ1ebDa0qP59baosB8yUXY3JNcbErBQzthX80uL1l2aLOSY4vH77rk6lzlkNjz9wYJiThIjCvgtaqJzhD5ubjNJ8N_YjA8UkvoKiFZub_MmlYTgk8OfLSO9cByuioDBmz9a-3n2EyTmZlTtFqmhWfQUPsnZrnrssbzT6dvbrMXuBQQvsLkWhjPR9v2c9E4tB-_V4AtQxeJHQllyog9sOqOY80f99LecCHo1veZZb2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/funhiphop/74781" target="_blank">📅 16:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74780">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISO-T0StdMlnqIe8YzcDGf3qGfooZ_NHshIhBCbvs61Lm61S_1mQfSkDkZGXK8CMF8IzrUYusewyenhWaslplBRSFuXzeJK8zgykZslclGFch9svdjTkLkF2Y5U6UDMuXd2Dki0sgbN9Fk4zZjtT1stEkmThXDAzndnDaQq4bdseYT0nNs6JgdWM1-kS6qO1KCewaBmonLB5rAfnFQDglCr-ri5UKQOYuHjz_tJLoZgVryJKR2jREfAgbDfqwNsSpnecq7hSVB2w6a1ssVvO8W3sxknjBz69EdVyW4oK0Ylk4QRM0jM-r8af6Jb_1p5xWNuGrjTn_UMZa9QGnHb1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید نقطه زن هواپیما رو با موشک بزن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/funhiphop/74780" target="_blank">📅 15:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74779">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMMd</strong></div>
<div class="tg-text">ژنرال رضایی وقتشه آمریکارو تصرف کنیم تا خالیه</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/74779" target="_blank">📅 15:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ریاست جمهوری آمریکا پس از
11 سال
وارد خاک چین شد.
ترامپ به همراه غول های اقتصادی ایالات متحده آمریکا و همچنین کابینه دولتی خودش
هم اکنون وارد چین شدن
.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/74777" target="_blank">📅 15:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این خبر نمایندگی اپل تو افغانستان هم فیک بود
ظاهرا یک نفر با خلاقیت بالایی که داشته یک نمونه مشابهشو ایجاد کرده
این شخص هم افغانی بوده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/funhiphop/74776" target="_blank">📅 15:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74774">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDeRBELNveFQydKQJCNKPxrZBMGZyl3G7CC47NhGkXA6YvjIKy3pX_prOvDZObqsPlh3jbT4Wqi1VB0aMIkezOYSetoBTsv4C0Lzhw_6XJmEU4Jtiksbo9eOnkVXtdXFQ8YpM3Co1-zHYCD5lV6KIQuv9Tt64AMHglFldDshcrgxK2sKLChxr3hX-Awl9ggbahzwQ3JAQOmnItHOscKjETqpcO3QETD5VMZteJMcMqP73aj2khujyGOYI_wXKKoMJ3d1t7f9wfC_PDn0vyLX904t1p2U-dtyfOfCVbjytzDX8l_S7kiZs-5LzHP_BH6Gbyw1t6bPNQuFoIaiXAq0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان رو سفت بچسبید
بر اساس ادعای خبرگزاری ترکیه ای ویروس هانتا باعث کوچک شدن آلت تناسلی مردانه تا 6 سانت میشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/funhiphop/74774" target="_blank">📅 14:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74773">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411849ba8d.mp4?token=ns6s009qXMzaB6z6HDy61jeaFStiKEqgzhtAUb4VDjHQquFvfQ1zxGgMdYBCiYp1lk_AtS9ayY_qfwnDOqkmGT1lMiq6qOu6Khn0ErZmJQ4f6Qfd4UTmjKDYzuqOkut3aALG0IfG27KjUPUdZP_HyMK6n0cOpmOl1voojdygr0jSJ8y-qN33I4vJhUddbkCPKUNjMav2DEJY8TnLchXIVpGUEQLqOiDpXJOj69oyLauJN2v5eTuejRk021cy8u11YshOROoemS46-DfEwCs81HHDWXfmA2DyRrE8MPexilh_wiDhwknNiqwGt7xka76ArS_OCGcXnV06Z7tALGrwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411849ba8d.mp4?token=ns6s009qXMzaB6z6HDy61jeaFStiKEqgzhtAUb4VDjHQquFvfQ1zxGgMdYBCiYp1lk_AtS9ayY_qfwnDOqkmGT1lMiq6qOu6Khn0ErZmJQ4f6Qfd4UTmjKDYzuqOkut3aALG0IfG27KjUPUdZP_HyMK6n0cOpmOl1voojdygr0jSJ8y-qN33I4vJhUddbkCPKUNjMav2DEJY8TnLchXIVpGUEQLqOiDpXJOj69oyLauJN2v5eTuejRk021cy8u11YshOROoemS46-DfEwCs81HHDWXfmA2DyRrE8MPexilh_wiDhwknNiqwGt7xka76ArS_OCGcXnV06Z7tALGrwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/funhiphop/74773" target="_blank">📅 13:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کصخلا زمان شاه همین اینترنت الانم نداشتن ملت  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/funhiphop/74772" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کصخلا زمان شاه همین اینترنت الانم نداشتن ملت
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/funhiphop/74771" target="_blank">📅 13:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74770">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران:
اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/74770" target="_blank">📅 13:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74769">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فرق میرا و گراک مثل فرق اونیه که مدرسه غیرانتفاعی درس خونده با اونی که مدرسه دولتی درس خونده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/funhiphop/74769" target="_blank">📅 12:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74761">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmahdi</strong></div>
<div class="tg-text">فک کن ایران صعود کنه به یه طریقی بخوره به پرتغال پرتغالو حذف کنه
بشاشه تو جام جهانی گرفتن رونالدو</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/funhiphop/74761" target="_blank">📅 11:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74760">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ایران ب تو کدوم گروه جام جهانی افتاد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/74760" target="_blank">📅 10:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr5WA6MK692-xoVkGIzf_8DmGemSG3Q7H26qgyDMyfVYX61dm5L39rU_ydTci43ROHw6BJCFqF3oJW2bokOm5OEyLpvVpSI7_-9Lo7JLCc9si_DzUluKGUGe2VgMkr0RMqbgnSQbAcbroDQJWzr629MuicNjBj54ZVCViFNYm_wxtHcMJBCFMBQoSoWA_PZP0gORfx17YqRQSbVFm4J0oa_Mv59nZqGiI5pE5fM6tfWSmFOLNUTBO6HSr1deZu5WwMXkUTadtSZoWxpYtqMatjsnXM3GnpDVAQGfK5_eEvt2JFXhCxjAwImjj5cB8nlhobQii_b33tJDKIT6DfiSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسشر ترین توییتای قرن همش مال ترامپه میگی نه توییت بعدیشو ببین
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/funhiphop/74756" target="_blank">📅 03:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1n3BPJzd6--6OuSJ-1SrGGG9lMfLSYSqmxLq62m2nghe8Wboyw3oqoE0GyKSUCvSoaoRZt-HCS4Jm1PZx9t0U_fZsfsb7D3tVyYFhkmoJuOktDHLc2hmWTbZojXir2KS-oWlDS_M5QDOTclnD8FXaw19Sxe8i1XoyebtnWkizs6ZhKNsCsIBBtHbL4ir2Uk7lCKxhHK5znlqfSPlIuywDghLdJMfB3QNamkrT6JpWW-FK4iLRL3ka95GvCSknxrGaANKBv9sBur7gnG0Lhxpuf8pOzjCK-aI8ANfWoAIr8uQwF351lYfm6hOOzZLp_gx3P2gN9__j3e_e4o4C0F_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxhz3agwij6ikx50ptc0jVESauJJKo7Jcc-jDpwylFw_eUKYHhkaQ_v6wK7AQ-hGNr5HCWuUDRjzMZYuAZunUWhESHZNxQlB0Bo6MK3dKweopDHv4dNpGRd3NL4QNg4r5281G9m9vPwTwi4SFbY34Hc5wJ3gCyMnQEI1MPXnq2QvhhbgytQzHsDKmlPtYy15wyngnQeagWcf9tqGUPkadGTeuKIT5v5JxH6YphRqScEHlnwnhqsqMWdSNTgheAQykVl5yFt3pVV4r8FW_LgGm5SUDCvdtW-vbQEy_dss0DmAUXC5vfHuPxHFTOWRAUpP4y4xKVTeEG1Itq0gl_DmLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو تو هواپیمایی که باهاش دارن به چین سفر می‌کنن لباس معروف مادورو موقع دستگیر شدن رو پوشیده که احتمالا داره به رئیس جمهور چین تیکه می‌ندازه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/funhiphop/74754" target="_blank">📅 02:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسماعیل بقایی در ادامه: آنها می‌گویند ما قلدریم؛ درحالیکه ایران ثابت کرده است که قدرتی مسئول در منطقه است و در عین حال قدرتی ضد قلدر است. ما قلدر نیستیم؛ ما ضد قلدر هستیم. فقط به اقدامات ما و آنها نگاه کنید. آیا ما کسانی بودیم که هزاران مایل دورتر به آمریکا…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/funhiphop/74753" target="_blank">📅 01:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هم اکنون؛ تهران زیر رعد و برق شدید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/74752" target="_blank">📅 01:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رسانه‌های عبری:
آمریکا در جریان جنگ ۴۰ روزه با ایران، ۱۳۰۰ فروند موشک پاتریوت مصرف کرده است. هر موشک پاتریوت بین ۴ تا ۴.۵ میلیون دلار هزینه دارد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/funhiphop/74751" target="_blank">📅 01:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5j5O0DWWHEPzLvUwNS7KsA11ystItHn0r8FVSMPsKelQlc3XLZWatBwpYZ12sm1xfSGE-Sb68_pqKaDpCjrylEK1O8k5sKZsce9xE_UxlMll50GS0HrgqaASK0lC0yX8jKptaKGBrM2wz02erm5Oiz7AZ2P4bJr1Os85pYP-QxFyWrhhRKfUR7BmqSfC9K9CYf3NQfL1vBBOXpjxJXEWsh7kencuxsx-kdX0HhCgbQdDCh3L_SVU7BYMKDK3R2dmKwdmI-fZjHuUSuPPCPkdTv1AldBIMZJy_Z1_zJfZGPh9VBVdvRe6Hm92-VCDyxlvCQPmfQ1TTmDRFwKo1loRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هم اکنون کوین ترامپ
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/funhiphop/74750" target="_blank">📅 01:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تو هرچی کم داشته باشیم تو موشک کم نداریم انگاری
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/74749" target="_blank">📅 01:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیویورک تایمز به نقل از سازمان‌های اطلاعاتی: ایران به اکثریت سایت‌های موشکی و پرتاب خود دسترسی پیدا کرده و گزارش شده که ۹۰٪ از آن‌ها عملیاتی هستند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/74748" target="_blank">📅 01:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیویورک تایمز به نقل از سازمان‌های اطلاعاتی:
ایران به اکثریت سایت‌های موشکی و پرتاب خود دسترسی پیدا کرده و گزارش شده که ۹۰٪ از آن‌ها عملیاتی هستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/funhiphop/74747" target="_blank">📅 01:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74744">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هواپیمایی قطر:
بارها آقای سعید جلیلی از گیت می‌خواسته رد شه و هی دستگاه صدا می‌داده
میپرسیدیم چیزی تو شکمتونه؟
می‌گفته دستگاه خرابه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/74744" target="_blank">📅 00:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جلیلی سیستم گوارشش بهم ریخته</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/funhiphop/74743" target="_blank">📅 00:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74742">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">درسته بحث بحث وطنه ولی تهران لرزید باز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/funhiphop/74742" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">داداش من خودم زلزله هستم ولی الان بحث، بحث وطنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/74741" target="_blank">📅 00:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74740">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رای قلعه نویی برای توپ طلا مشخص شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/funhiphop/74740" target="_blank">📅 00:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74739">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سعيد جليلى: ‏من حاضرم 200 كيلو اورانيوم را لقمه لقمه بخورم ولى دست دشمن ندم.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/74739" target="_blank">📅 00:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74738">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جوری داریم یه زلزله ساده رو پوشش میدیم انگار زیر بمب اتمیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/74738" target="_blank">📅 00:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش مقدماتی زمین‌لرزه
بزرگی: ۴.۶ ریشتر
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/funhiphop/74737" target="_blank">📅 00:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من کانفیگم قطع بود الان لرزیدم</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/74736" target="_blank">📅 00:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">میگم تشعشعات رادیواکتیو از تل‌اویو به ایران میرسه؟
@FunHipHop
| Ali</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/funhiphop/74735" target="_blank">📅 00:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74732">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سفت بچسبید که نزدیکی شمال از سمت تهران هم ۴.۶ ریشتر زازله اومد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/funhiphop/74732" target="_blank">📅 00:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74731">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تهران لرزید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/funhiphop/74731" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74730">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تهران لرزید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/funhiphop/74730" target="_blank">📅 23:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74729">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تهران لرزید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/funhiphop/74729" target="_blank">📅 23:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74728">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تهران لرزید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/74728" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74727">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تهران لرزید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/funhiphop/74727" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74726">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu0EH6mV8LGqnHeH2g16JWtEDdPULxlUpG_LYd_k_kCdZj3PikgbfP9C1aramE1kzt6NcXgBCwyeCEttGK5_F2yf4pVm06hK_r5ZgssLqjKYgrcsp9UnuaY--mcM38ZBw13t5ezh3kecCE97Tp_aNc601QkFEHCFbD7_kKYrJg5Ya8q74gRqAc0z6xITUuBUNgggJ6BPDfUwbHsBQIQDNX6bpHstO8dLksjfSfl5fbPVb_8o62z94qNiF3Py1ggpQCQmcyvzaNwuJUaon5DhyzeUFyHwKmhQ-iAg6CJSH-O8UUpFbwjjvd_u8Hn2Z9CGqOM64P4wAZbeW9sspuocQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنتو زنت گاییدست
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/74726" target="_blank">📅 23:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74725">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e19475e71.mp4?token=IPkKQTUmrOmQMxErNUq3K1ULAMBe7eG_hJmJx8SptkOc8AdzJ9dEdYgrRzTh0R2l8Ae4j0vVGMh2cV44tmLaqogxXiyt7L6P94VCrZ5bjts49fRYcJvFdj6QWydrpr4MPVt6robB1pB2Qmy7Avxg2a7mq_cvvlpwVFKaTLYgmsB1JwJlCMv6Z-k73bK1qK1uJ2jgkvawGe0Fj6-MiIk9XJiB2q0hs_wxayOhkr4Z9Q0ISydsca1aDNCMKw67f_YkxKhbXLr5Jg2pwIIP9iwxFzeIMO-D87aEVX6K4JPILi7npxZ7lNEgRQ_p-6F38E3rdViTBcOJJUeVP8u9-OkSQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e19475e71.mp4?token=IPkKQTUmrOmQMxErNUq3K1ULAMBe7eG_hJmJx8SptkOc8AdzJ9dEdYgrRzTh0R2l8Ae4j0vVGMh2cV44tmLaqogxXiyt7L6P94VCrZ5bjts49fRYcJvFdj6QWydrpr4MPVt6robB1pB2Qmy7Avxg2a7mq_cvvlpwVFKaTLYgmsB1JwJlCMv6Z-k73bK1qK1uJ2jgkvawGe0Fj6-MiIk9XJiB2q0hs_wxayOhkr4Z9Q0ISydsca1aDNCMKw67f_YkxKhbXLr5Jg2pwIIP9iwxFzeIMO-D87aEVX6K4JPILi7npxZ7lNEgRQ_p-6F38E3rdViTBcOJJUeVP8u9-OkSQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممممم  آمریکا با بالگرد اومده تو خاک ایران خلبانشون که افتاده بود رو برداره ببره  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/funhiphop/74725" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74724">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZkhcrVM544Qee8g2MkWHW2UvefDokV6Bc8yTU3TSdHV4zEpCIXiXVwRwHJA-R67Qg237drOjralmhv0mQL0ohZ4e6LTcpty3pfitn-giFZkAS8Av14rzK-2vwfHTRPNnG0kVDAEpe07UeZbKdlU6_kaTTGpv0D4y4TDni6Vl7m14ovwBARJqhhNpSY3yauRFgq8ubZUgwpAoPL_0V4GlHLBDdwIoAEfHcz-3NiB6XQVaEPtcjofHLxOMLZg9tBN0UMN58IH3Lg5xIe-vC25T3Fx9KiqD41nXcLQlr-1AAYIowgPGsxbTEnCpGDcakeXE2BcDXbMryAZjEUTk3-zYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/74724" target="_blank">📅 23:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74723">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">😑
حلقه قدرت ترامپ در چین
ایلان ماسک — مدیرعامل تسلا و اسپیس‌ایکس
تیم کوک — مدیرعامل اپل
لری فینک — مدیرعامل بلک‌راک
کلی اورتبرگ — مدیرعامل بوئینگ
استیون شوارتزمن — مدیرعامل بلک‌استون
برایان سایکس — مدیرعامل کارگیل
جین فریزر — مدیرعامل سیتی‌گروپ
جیم اندرسون — مدیرعامل شرکت Coherent
اچ. لارنس کالپ — مدیرعامل جنرال الکتریک هوافضا (GE Aerospace)
دیوید سولومون — مدیرعامل گلدمن ساکس
یاکوب تایسن — مدیرعامل شرکت Illumina
مایکل میباخ — مدیرعامل مسترکارت
دینا پاول مک‌کورمیک — معاون و مدیر ارشد سابق گلدمن ساکس و مقام پیشین کاخ سفید
سانجای مهروترا — مدیرعامل مایکرون تکنولوژی
کریستیانو آمون — مدیرعامل کوالکام
رایان مک‌اینرنی — مدیرعامل ویزا
⛔️
آمریکا غول‌های اقتصادشو برده چین؛ یعنی ابرقدرتا مستقیم دارن روی آینده دنیا معامله می‌کنن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/funhiphop/74723" target="_blank">📅 23:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74722">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جمهوری اسلامی عزیز، خشم و انتقام حماسی به شدت خفن تر و قوی تر و شیک تره
باور کنید نیاز نیست برید مزرعه دار شید داس بگیرید دستتون، یا چکش بگیرید دستتون میخ بکوبید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/funhiphop/74722" target="_blank">📅 22:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74721">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUZso2CDvzBQWOUyV_L0X1TLb3o2SbThttZ8f_MakxWTgcwqqxsm7mKblSmtTFFc1kG6vqXmWXiYochdgUmCqD94fOa79ZHr5L5ruxltMtxYb2F9w5CYQEQfcgklqC0uE0qrnCy1nTBfopxmOKHO5Bz3gD1q8ojIGYkdjxZvlKPjmMUVlP-Eh8quF34bRUcZtrmhMH5-KH1lphsPS0LToBLedQGcWiOBA1SUUVSQXHc7JZSkY6vH5pBAWciAz-0BXuI9qMCI1OpKQb-OTEJvYWfTjCfg3uyP2fSvGUY8k7OZd1UscyD9aXI6BZfCjP_WwTVsdrM9gMoJBvGCQAlW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">NBC News:
ارتش ایالات متحده در نظر دارد در صورت فروپاشی آتش‌بس و تصمیم رئیس‌جمهور ترامپ برای از سرگیری عملیات‌های عمده رزمی، نام درگیری خود با ایران را به «عملیات چکش سنگین» تغییر دهد و این جایگزین نام قبلی «عملیات خشم حماسی» خواهد شد.
این تغییر نام همچنین به دولت اجازه می‌دهد تا ساعت مجوز ۶۰ روزه کنگره تحت قانون اختیارات جنگ ۱۹۷۳ را به طور مؤثری از نو راه‌اندازی کند، زیرا کاخ سفید استدلال خواهد کرد که این یک عملیات جدید است.
ترامپ هنوز دستور از سرگیری خصومت‌ها را صادر نکرده است، با این حال مقامات اشاره کرده‌اند که محاصره جاری در حال حاضر اهرمی فراهم می‌کند بدون نیاز به اقدام نظامی عمده، اگرچه
یک مقام هشدار داده است که «وضعیت موجود پایدار نخواهد ماند.»
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/funhiphop/74721" target="_blank">📅 22:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74720">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگه مادرجنده باشی ایران بهترین جا برا زندگیه پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/funhiphop/74720" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74719">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ایلان ماسکم با ترامپ میره چین
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/74719" target="_blank">📅 22:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74718">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99d9c3f71.mp4?token=jA7KkIzvmYY_rjl411kTrW5oC0cVDF4Xsn3Lkhf26tN5O4qilKAoLN1YtBuEYl93ZDerstJm3IDYWIUE3CoOzjdG1vyTsqdi6PyzpNhafeX6vpjVkHkJXj6AyXibsQYCN3nJhmFCeYQM_nEJfoBE9NeUoPX-vWkab9GcoDRfv4mUdIazluiovey6hgfE2Qb3Jjm8SHjR6eGCsDNWz62q9Z1SdMQSRN90aOBhvD3QF_bl0DPZb7Zyl3bbQ--7hOOwPHOV6LUIh222pwauRQodFc4iPqnXw74wZXgHO3KmyeJ29sZuYeU0qjZ8O6Fvfj2TM1ucPIy83neDZ8gVGCsSQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99d9c3f71.mp4?token=jA7KkIzvmYY_rjl411kTrW5oC0cVDF4Xsn3Lkhf26tN5O4qilKAoLN1YtBuEYl93ZDerstJm3IDYWIUE3CoOzjdG1vyTsqdi6PyzpNhafeX6vpjVkHkJXj6AyXibsQYCN3nJhmFCeYQM_nEJfoBE9NeUoPX-vWkab9GcoDRfv4mUdIazluiovey6hgfE2Qb3Jjm8SHjR6eGCsDNWz62q9Z1SdMQSRN90aOBhvD3QF_bl0DPZb7Zyl3bbQ--7hOOwPHOV6LUIh222pwauRQodFc4iPqnXw74wZXgHO3KmyeJ29sZuYeU0qjZ8O6Fvfj2TM1ucPIy83neDZ8gVGCsSQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ما ایران را کاملاً تحت کنترل داریم.
یا یک توافق خواهیم کرد، یا آنها نابود خواهند شد. به هر حال، ما پیروز می‌شویم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/74718" target="_blank">📅 21:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74717">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f5582997.mp4?token=PGoZDJdWmtXBo-J0GRjoZ0Biqb7V66LTW5EOgbqsxYxTj2X4hFlogcx2OMxI0mp1v011rCmZmWkUqkPz7vj-WV8W9mY4ZiFM2SUk47kOzdk71UJtfoaPgctUB7no4v7ObUUe-l4LvyRWyRxGhIBs-nv9Yyqfxuf9ozZmpvecnG5KFx2yZG4HFYsfxEEcokIFkbq0vEdCZNlsULKgM3bZzdW2gY3MgIFFFZiBYicHtiIThDYvFORVJh35IKrGAKbZH9VrEds-PW065eO12M1sZzBSDky5KYoCHEai_o8cl3QY4wO7_yQ7fdELp0_YTsmGu_kKiTYiFEN4WDo8R0pVvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f5582997.mp4?token=PGoZDJdWmtXBo-J0GRjoZ0Biqb7V66LTW5EOgbqsxYxTj2X4hFlogcx2OMxI0mp1v011rCmZmWkUqkPz7vj-WV8W9mY4ZiFM2SUk47kOzdk71UJtfoaPgctUB7no4v7ObUUe-l4LvyRWyRxGhIBs-nv9Yyqfxuf9ozZmpvecnG5KFx2yZG4HFYsfxEEcokIFkbq0vEdCZNlsULKgM3bZzdW2gY3MgIFFFZiBYicHtiIThDYvFORVJh35IKrGAKbZH9VrEds-PW065eO12M1sZzBSDky5KYoCHEai_o8cl3QY4wO7_yQ7fdELp0_YTsmGu_kKiTYiFEN4WDo8R0pVvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
رهبران ایران یا کار درست را انجام خواهند داد، یا ما کار را تمام خواهیم کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/funhiphop/74717" target="_blank">📅 21:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74712">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj6rjSMHK7CG71rPHqRU6U0PsohzhmdQM59mJauwmPY2lbAsuNp5_6TlFmEwQgbHEVKKBoJOj9DXyD03u0ifY6AQaRxpyMv9Sqc4fRlYZhkepr_Zbrlpm-0clkWU4hxQprJaUeyPvaJVZUEPmxzh1guCy5eNkvkD4rbjaur5dAoigLGdJ6gMZ656HvlJFMcuTlVlf4o5FmqxcI3xRN9lxI8bXOxIhx24zzIu44lwCf8kl3xI08x_EkqeV_P3AFAbu2UqTcmAv2z8Pp1ftXevh8uJMQ5Mdp1zlkBHsT5jwnYbE9laVsp_yCRmPLBEMeJ6FZVq9qzVLrUiGQBGJQ2vTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند شما، قدرتمندتر از همیشه!
🤖
اکانت
Gemini Pro
🔥
فقط با
299,000
هزار تومان
(اختصاصی)
روی ایمیل شخصی شما بدون ورود
پرداخت امن با درگاه پرداخت
💳
| کارت به کارت
🪪
| پرداخت با کریپتو
💸
همین حالا ارتقا دهید
لینک خرید از وب سایت:
🌐
Zhimunplus.com
لینک چنل:
✅
@Zhimun_plus</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/funhiphop/74712" target="_blank">📅 21:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74711">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رضا پهلوی: هر زمان که مردم توان مقابله داشته باشن، فراخوان خواهیم داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/74711" target="_blank">📅 20:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74710">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
انتظار می‌رود ترامپ پس از بازگشت از چین در پایان هفته، تصمیمات نهایی درباره ایران را اتخاذ کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/funhiphop/74710" target="_blank">📅 20:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انگلیس:
ما در مأموریتی چندملیتی برای تأمین امنیت تنگه هرمز، با ناوگان هواپیماهای بدون سرنشین، جنگنده‌ها و یک ناو جنگی مشارکت خواهیم کرد.
مأموریت تنگه هرمز چندملیتی، دفاعی و مستقل خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/funhiphop/74709" target="_blank">📅 20:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الجزیره:
رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند:
— پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان)
— رفع همه تحریم‌ها
— آزادسازی همه‌ی دارایی‌های مسدود شده
— جبران خسارات و زیان‌های جنگ
— به رسمیت شناختن حق حاکمیت ایران بر تنگه هرمز
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/74708" target="_blank">📅 20:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شاهین نجفی هزار پدر حداقل آنبلاک کن بتونم بیام پیویت بگم کیرم تو کنسرتی که گذاشتی</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/74707" target="_blank">📅 20:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMuh8dkTVCc0UZaC_nmXQ_7HtGZeakE6-kziufUTKrvMXiOqmm8PG3AjptkPIw_HXy3Fod94DUPsDtGUpNXw4agz2lpGz_9aiL8N8rjmKukNLT3N0UY7NOYm5YG1_srhMMJ1_3X2o5jDjK6gTh7WDfIg4mxxqOWKLxS0tnjButJBWYFS_I-OqL9giZGqvds8avFHklb34Pk_SEn3cohzHGlMreDulgcsK0w_793S87WzLM9niKfrmFszgc47xDy2_s0gKRWKqKvrxKLUWkRGERSzMZqsxnWj2R_JEKLAPp9zGJVQjnaQH_wQffiAnpvwXmrwdKT_hN6h6a10REwesQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس، ابراهیم رضایی:
یکی از گزینه‌های ایران در صورت حمله مجدد می‌تواند غنی‌سازی ۹۰ درصد باشد.
این موضوع را در مجلس بررسی خواهیم کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/funhiphop/74706" target="_blank">📅 19:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74705">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubVXGqMAFKE_Nk2DVR1ueV-n9xnX2UWsWZ0dweFOrgZnPwolJrPdWtjUH44-bjT_n5vpozz6ffV4RFP-zJ56pWujDWMJC88h97hpyMofgJAuoBJDyVGew4dG7UZS-1CA9xw2dcadbf25QUzVOcYheMFAgDassVuXg6YX2bloL5ZbDccgEoz8W3Fw4LdSMUqKwhMqdkgDx1WFi2hqF7LymB545srMfDmgK8RCW2b_OrAp8OYdJEQDgKnZPuOMGtI1eGAS9Pqsc0iXEFUhwp0O51fW90QLlb1EabwKWPesr4icUdogE5oizlSwGE4U5sdnwdAP8s4V06lejmpjh18NPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفه شو
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/funhiphop/74705" target="_blank">📅 19:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سرورهامون با بالاترین سرعت و کیفیت ممکن هستند
💢
تعرفه هامون به صورت زیر هست
📥
1G- 250
⚡️
2G- 500
🌟
3G- 750
💎
5G- 1,200
👑
10G- 2,300
⚡️
20G- 4,500
👁
سرویس‌ها به‌صورت یک‌ماهه ارائه میشن و هیچ‌گونه محدودیت کاربری ندارن
👥
🤩
با خیال راحت روی چند دستگاه استفاده…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/74704" target="_blank">📅 19:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74703">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShyPxnGuin🐧</strong></div>
<div class="tg-text">سرورهامون با بالاترین سرعت و کیفیت ممکن هستند
💢
تعرفه هامون به صورت زیر هست
📥
1G- 250
⚡️
2G- 500
🌟
3G- 750
💎
5G- 1,200
👑
10G- 2,300
⚡️
20G- 4,500
👁
سرویس‌ها به‌صورت
یک‌ماهه
ارائه میشن و هیچ‌گونه
محدودیت کاربری
ندارن
👥
🤩
با خیال راحت روی چند دستگاه استفاده کنین و بدون دغدغه از کیفیت و سرعت لذت ببرین
🚀
حتما دقت کنید سرورها همراه با ساب و بدون ضریب هستند
👍
@PenGu_Sup
🐧
@PxnGuin
⚡️</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/funhiphop/74703" target="_blank">📅 19:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74702">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اکسیوس:
ممکنه آمریکا بزودی به کوبا حمله کنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/funhiphop/74702" target="_blank">📅 18:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74701">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">احتمالا هفته دیگ پیش خریدGTAVI به قیمت ۸۰ دلار رو کنسول ها میاد.    @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/funhiphop/74701" target="_blank">📅 18:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74700">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">احتمالا هفته دیگ پیش خریدGTAVI به قیمت ۸۰ دلار رو کنسول ها میاد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/74700" target="_blank">📅 18:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74699">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رویترز:
یک مقام پنتاگون می‌گوید جنگ با ایران تا این لحظه حدود ۲۹ میلیارد دلار برای ایالات متحده هزینه داشته است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/74699" target="_blank">📅 17:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74698">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMQGVJ667FjCG3rpKKHZ8bg7xbN6l4vhcrCYryLr_dbWk61LYgjNkZMGXcDR2Xw-GriPc8zB4UlJgb1Vj5tZGoDQkR5DWqd_hxGoywS1zHK_IFvN9giwnpFzWN347KoQLEkUS4xKQtFudTOWL81Jlv1FO_A3-4XGAw1p6AhXfhUoJyWUgnwJSV5DqlpAn2OtCTr8t2R4wlS7ZO21vaQmLtNmqI6d0L2xNItVfIsBJlUa1o98VlBDi-CahCHV4U0Zvvvup9tzlqCxa8_pvoleLDslo4ms7V0apv5-cOw_a0FouMrTAO9p4mgJumtjAqFrbyHLWam1iOmlemNoVHBU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال بر خلاف چیزی که خیلی ها تصور میکنند! چین در مذاکرات جدید با امریکا کارت برتری نسبت به ترامپ نداره. اقتصاد چین با مشکل هایی چون رشد ضعیف, بیکاری جوانان, کاهش مصرف داخلی و بحران بدهی رو به رو هست. بخش بزرگی از اقتصاد چین بر پایه صادرات و عرضه…</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/funhiphop/74698" target="_blank">📅 17:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74697">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ
ایران از نظر نظامی شکست خورده و
احتمالاً هنوز خودش هم این را نفهمیده است
.
اگر
نیویورک‌تایمز
را بخوانید، فکر می‌کنید ایران اوضاعش خیلی خوب است.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/funhiphop/74697" target="_blank">📅 17:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74696">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ
چین قدرتمند است،
اما ما از چین هم قوی‌تریم
. از نظر نظامی از هر کشور دیگری قدرتمندتریم.
این را در ونزوئلا دیدید. برای بیشتر کشورها آن عملیات خیلی سخت می‌بود، اما ما در یک روز انجامش دادیم و حالا
نتیجه‌اش
را ببینید.
به ایران هم نگاه کنید... آن‌ها همه‌چیزِ بزرگی داشتند،
اما حالا همه‌اش از بین رفته است.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/funhiphop/74696" target="_blank">📅 17:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74695">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ
ما صددرصد به آثار و بقایای هسته‌ای دست پیدا می‌کنیم؛ کل ماجرا را کامل به دست می‌آوریم.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/funhiphop/74695" target="_blank">📅 17:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74694">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ
ما قوی‌ترین ارتش دنیا را داریم.
الان هم این را می‌بینید؛ مثلاً درباره ونزوئلا. الان رابطه خیلی خوبی با ونزوئلا داریم. میزان محبوبیتم آنجا به ۹۹٪ رسیده، باور می‌کنید؟
حالا ایران هم تقریباً همین وضعیت را دارد؛ فقط کشور بزرگ‌تری است با ۹۵ میلیون جمعیت. راستش را بخواهید، ما همه‌چیز را نابود کردیم.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/funhiphop/74694" target="_blank">📅 17:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74693">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ
من رابطه خیلی خوبی با بی‌بی دارم. ما واقعاً مثل دو شریک واقعی کنار هم بودیم.
اگر ما دوتا نبودیم، اسرائیلی هم وجود نداشت؛ مخصوصاً بدون من قطعاً چنین چیزی ممکن نبود.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/funhiphop/74693" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74692">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سید روزنبرگ
«آقای ترامپ، آیا واقعاً در
تهِ دلتون
باور دارید که می‌تونید جلوی غنی‌سازی اورانیوم ایران رو بگیرید تا
اصلاً و ابداً
دستشون به بمب نرسه؟»
ترامپ
«
شک نکنید، صد در صد!
اونا متوقف می‌شن. ایرانی‌ها خودشون به من گفتن که ما قراره به اون
"غبار هسته‌ای"
برسیم (ما مواد رو ازشون می‌گیریم).»
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/funhiphop/74692" target="_blank">📅 17:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5168dede5b.mp4?token=dH3L64-2Zu1znc240OTsd5uUZ0L4Wdyya0PL-G5mrLRtqMEaKx3Su6p40HcPqUiKpmaYOcF6k1-8LiqAgRqccPuTdEp0EK96URVSLDtzLSik6j1T0KquELve0bprTsjKW4nJ3A1liPp6OP8WNX8hJnyV-Z7DNg2VhmX-PuKwnvkhYcsCpuc7pUIea28Fa_PNmwBsmjKhkPR5nfyFEMLXpfSmVjQclilSuCVa8U1nixzaSqTSX8ekj1Pad0PKmLBJnQses_hOCXiSEpsYTM71n00p4MVhy9NxIvYBAXOLrrbEZe8osvKUNGU4WNj7Kjvp9Di1XAbgapXarS-UZqvEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5168dede5b.mp4?token=dH3L64-2Zu1znc240OTsd5uUZ0L4Wdyya0PL-G5mrLRtqMEaKx3Su6p40HcPqUiKpmaYOcF6k1-8LiqAgRqccPuTdEp0EK96URVSLDtzLSik6j1T0KquELve0bprTsjKW4nJ3A1liPp6OP8WNX8hJnyV-Z7DNg2VhmX-PuKwnvkhYcsCpuc7pUIea28Fa_PNmwBsmjKhkPR5nfyFEMLXpfSmVjQclilSuCVa8U1nixzaSqTSX8ekj1Pad0PKmLBJnQses_hOCXiSEpsYTM71n00p4MVhy9NxIvYBAXOLrrbEZe8osvKUNGU4WNj7Kjvp9Di1XAbgapXarS-UZqvEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست:
قطعاً، ما در حال پیروز شدن هستیم.
و در تمام مراحل این نبرد پیروز شده‌ایم.
ایران بر اساس کاهش چشم‌گیر توانمندی‌هایش، این موضوع را به‌خوبی می‌داند؛ به همین دلیل است که شاهد تمایل آن‌ها برای نشستن پای میز مذاکره بودیم.
چگونگی حل‌وفصل این موضوع بر اساس
شرایط ما و شرایط پرزیدنت ترامپ خواهد بود.
ما تمام مهمات و توانمندی‌های لازم برای این کار را در اختیار داریم.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/funhiphop/74691" target="_blank">📅 17:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1516ee5e2a.mp4?token=mmCNEAlQgW8Gvi8RsiXo8JGy5ol6RXbT7k60bc3POr2rgQI66ICjYF7QDykm5x-twP5ehFt8WPWjkJ2WVT3lws_7uOdfmIDL2Meee6nZ-fDY1hUjUpIU72V3ch6p1drH_ZvR_0SHriq9Fw9rskrLoaHngKlqA6M9gW1rDj61QcHXFI58r3j0aZOG3VU26I2Y8m35oUKRUHZBXFak1qyuGk8RY86tFWHsaIy7ZcU4jc6QoFFUNX6bzP3nxsQkxybMAhH4luKO79G6G5R760TXw-6VECSzLFuo9xd7CNUiN5p2iz81B3c6z2sWV7UsE_yEfigzZqt7iaakxAszzTYnSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1516ee5e2a.mp4?token=mmCNEAlQgW8Gvi8RsiXo8JGy5ol6RXbT7k60bc3POr2rgQI66ICjYF7QDykm5x-twP5ehFt8WPWjkJ2WVT3lws_7uOdfmIDL2Meee6nZ-fDY1hUjUpIU72V3ch6p1drH_ZvR_0SHriq9Fw9rskrLoaHngKlqA6M9gW1rDj61QcHXFI58r3j0aZOG3VU26I2Y8m35oUKRUHZBXFak1qyuGk8RY86tFWHsaIy7ZcU4jc6QoFFUNX6bzP3nxsQkxybMAhH4luKO79G6G5R760TXw-6VECSzLFuo9xd7CNUiN5p2iz81B3c6z2sWV7UsE_yEfigzZqt7iaakxAszzTYnSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانم مک‌کالوم
«به عقیده من، "قانون اختیارات جنگی" باید فعال شود و موضوع به کنگره بیاید؛ هرچند نمی‌دانیم نتیجه چه خواهد بود. آیا شما
طرح جایگزینی (Plan B)
دارید؟»
پیت هگست
«عضو ارشد، باید بگویم که ما برای تمامی این سناریوها برنامه داریم. برنامه‌ای برای
تشدید عملیات
در صورت لزوم، برنامه‌ای برای
عقب‌نشینی تاکتیکی
در صورت نیاز و برنامه‌ای برای
جابه‌جایی تجهیزات و نیروها
. اما قطعاً در این نشست، با توجه به
حساسیت مأموریتی
که رئیس‌جمهور برای اطمینان از عدم دستیابی ایران به سلاح هسته‌ای بر عهده گرفته است، گام بعدی را فاش نخواهیم کرد.»
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/funhiphop/74690" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگه اینترنت پرو برا کنترل فضای مجازیه و برا همه نیست با کدوم منطقی پیامکش برا بابا بزرگم اومده</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/funhiphop/74688" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قطعی اینترنت قطعا بخاطر مسائل امنیتی نیست، قطعا بخاطرجلوگیری از ارتباط اجنت موساد با خارج از کشور نیست، قطعا بخاطر نفرستادن محتوا به اینترنشنال نیست
فقط یک دلیل داره اونم رانت و سود کلان برای دولته، سودی که اپراتورهای موبایل و دیتاسنترهای بزرگ مثل آروان‌کلود در این ۱۰ هفته بدست اوردن برابری میکنه با بودجه کامل چندین ساله مملکت پس به عبارتی حالا‌حالا‌ها قرار نیست وضعیت اینترنت برگرده به شرایط عادی و شاید هم هیچوقت برنگرده
دلایل مختلفی داره از جمله اینکه یواش‌یواش و در خفای کامل پیامک اینترنت‌پرو به حجم عظیمی از مردم ارسال شده و ملت درمانده مجبور به خرید اینترنت‌پرو و یا خرید سرویس‌های VPN به قیمت بالا شدن، به عبارتی مردم دارن خودشونو با این وضعیت وفق میدن و فعلا خبری از اینترنت بین‌المللی برای عموم مردم نیست
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/74687" target="_blank">📅 16:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">با ۳۰ میلیون تومان موجودی، برای سه ماه آینده باید ۴۰۰ میلیون چک و بدهی پاس کنم و نمیدونم چه کنم
این یکی از برکات پیروزی های ج.ا در جنگ مقابل حمله بشردوستانه آمریکاست، به مشکی مادرخراب و شاه تحلیلگران مرادویسی برسونید اینارو با واقعیت دل جامعه رو به رو شن</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/funhiphop/74686" target="_blank">📅 16:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستان به یامال خرده نگیرید یارو تو ناف اروپا بزرگ شده و تنها ایدش از اسلام وجود الله و روزه گرفتن و نماز خوندنه</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/funhiphop/74685" target="_blank">📅 16:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در لفافه اینو میگم:
دین محترم اسلام به بهترین شکل در حال اجرا شدنه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/74684" target="_blank">📅 16:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l85tAp2tKdcFHuSRunEknbmBYBGDa6wwz0ZAQw7KHtST6cPp6RHtitqB3CGJiTUSZh0S97JnB2B2vTqXcFO2kfQBjDdhVKZ09vHp2g_SmbsqDTi409mZW-t0ZjM-Ob4Me_VYdZpMkUIgVSRTz87iDd2r_uQ_aAtcbFycdGijFnhcEod88h1F9c5OBHZsKEGgiOwmeOuNjCHYIJgfon-JjBIULAap7hXhcg40UUK9fPNRpxrSdo67z6hvVz2RSf7KPSObetZYRGxnfk9NR7plPLRpAcyTtZ-VYFgOOYXR2KYXfZSKkLxwk--kjxN4XxuFFd1pVByJa1LVtGtzDkq9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریباً توی این ۲۰ سال و اندی زندگی اندکی که داشتم، هیچ موجود زنده ای رو ندیدم که آرزوی مرگ کنه واسه نوزاد کسی.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/74683" target="_blank">📅 15:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pe9rKjgDNpdk19uw8eqgAk4yMPO7Cn80PMrgpPkTkOlhnhGqqzDqQlYnse4iE7arKnsLjuUxKp53j7ymuD5mm2CYOn3wPmnCgkWphr5d9vraU_M2H731VFq8bI6pRv0PQg60RGI_ppnWF4qXiBlZRrbCNrIYfvIODYF68CXYJDEjst1egXr3iW_uNb_-It8BtW6kcf9JXvpLliHAil917insLCO0paMKhP2RdjYQ1EmCfMRqszsDL6-fhAd8TTQ_hKkG6avaalrfYrIcJKw-OajjE8QiQRtFTXEeI7YZjGqT4MCN80wjBu405KRQ3XHFs4SbOm3T1K4crXKh2BeiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5fQaw4auCoziP3D2sBiTChEZwVujGUq1bUbJL9f9hGWaneyFI7TdX--LgLoSoFOZqHKnsBicfBOzymEPQUQgamAhBXWfq9JvUwosBCGMwokvswr7Cvx4ED5fRDM-2iXDajNY4qar-H17wjD51nhgBGW0Zyns7mMW9HtTCLWZZ4hnMK2hc4lsUPqviZI1orsmb3TU4jpWEKbp15yHmsCzNIBNPsyufsPXoB_OfWjJ7aR-zohljCvWiopv_w0Oe1dcKl-zql_mqo6Ba7tAVgf8eS7z_QSmv_yOQdYmACJsBHiZdjYXhGraU6EvtdHYznp8ASJ7JufqAhH-PbfmDjQXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت های جدید ترامپ
بای بای قایق های سریع
دموکرات ها عاشق
فاضلاب
هستند.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/74681" target="_blank">📅 15:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">😠
ترامپ
کوبا درخواست کمک کرده و قرار است با آن‌ها گفت‌وگو کنیم.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/74680" target="_blank">📅 15:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کشف خط لوله قاچاق سوخت تو بندرعباس
دریابانی بندرعباس یه
خط لوله ۶ کیلومتری قاچاق سوخت
رو پیدا و منهدم کرده؛
خطی که قاچاقچی‌ها زیر ماسه‌ها و بستر دریا قایمش کرده بودن.
ظاهراً سوخت از ساحل مستقیم با این خط لوله به شناورهای داخل دریا منتقل می‌شده و ماجرا خیلی فراتر از قاچاق‌های ساده بوده.
این کشف دوباره نشون میده قاچاق سوخت تو بعضی مناطق جنوب کشور داره به شکل حرفه‌ای‌تر و سازمان‌یافته‌تری انجام میشه.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/74679" target="_blank">📅 15:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjiZFJ2jV_qlrbs79EabXmNgELEWvs2dS1_3Q2rUnIkggBHhyP7-e8cyG0YScJvzHNjalPv9NdwHEzkx0nMJTH1PfyTmTNu1zunfIMPj5Lmv3k03HWQxCMVPCOKusCJr6YACvroPrBHCoIQv_8nbbyAiYoKppDbstbovW6Fi4UZykMWstu-bs4sE50iu_aOWYiI8QtTt5h-Ls8PUnJ_psaNGpO5TWuqS_rBjCFwWP_D5-ODyo8_K6iqkRSwZyzybg0k6O36AtRuhdTPyjhPdp3TyyjszWm59J6Lk_9rnsYaeJO7AUgMowAEsHK-Cs_Ol363uKDJNe3f_4pv30ROlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارکس سیتی پرو
فشار نفت و هرمز روی بورس هند
بورس هند این روزها زیر فشار نگرانی‌های نفت، تنش‌های هرمز و فضای ریسک‌گریز بازار قرار گرفته و معامله‌گرها محتاط‌تر شدن.
صحبت‌های اخیر دولت هند هم
کمکی به آرامش بازار نکرده
و فشار فروش رو تو بعضی بخش‌ها بیشتر کرده.
هند یکی از بزرگ‌ترین واردکننده‌های نفت دنیاست و هر تنش در تنگه هرمز می‌تونه مستقیم روی اقتصاد و بازار مالی این کشور اثر بذاره.
از طرفی چون هند جامعه بزرگی از کاربران
کریپتو
داره،
کاهش
ریسک‌پذیری
تو این بازار می‌تونه روی فضای کریپتو هم تاثیر
منفی
داشته باشه.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/74678" target="_blank">📅 15:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74676">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ویو ها یکم بیشتر شده
سوراخ جدیدی باز شده؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/funhiphop/74676" target="_blank">📅 14:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74675">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزیر اقتصاد
شصت همت (هزار میلیارد تومان) برا خسارت جنگ کنار گذاشتیم عشقا, اصلا نگران نباشید.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/funhiphop/74675" target="_blank">📅 13:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74674">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سیناب خبر از برنامه های جدید خودشو پیشرو و تیمش میده، یه دزدی دیگه تو راهه فکر کنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/74674" target="_blank">📅 13:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74673">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">توهم
بزرگترین عامل سقوط است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/74673" target="_blank">📅 13:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74672">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وال استریت ژورنال
بر خلاف چیزی که خیلی ها تصور میکنند!
چین در مذاکرات جدید با امریکا کارت برتری نسبت به ترامپ
نداره
.
اقتصاد چین با مشکل هایی چون ر
شد ضعیف, بیکاری جوانان, کاهش مصرف داخلی و بحران بدهی
رو به رو هست.
بخش بزرگی از اقتصاد چین بر پایه
صادرات و عرضه زیاد
بنا شده, از
خودرو
و
فولاد
گرفته تا
پنل های خورشیدی
و اگه آمریکا و متحداش تعرفه های سنگین تری اعمال کنن میتونن مستقیم به روی
کارخانه ها
و
صادرات
و
جریان نقدینگی
چین اثر منفی بزارن.
از طرف دیگه ترامپ ابزار هایی مثل
تعرفه جدید
,
تحریم بانک های چینی
و
محدود کردن دسترسی چین به سیستم مالی غرب
و کاملا در اختیار داره.
حتی برخی تحلیل ها میگن که واشنگتن ممکن هست که از پکن بخواد حمایت اقتصادی خودشو از
ایران
و
روسیه
کاهش بده و محدود تر کنه.
@FunHipHop
| NIC333</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/74672" target="_blank">📅 12:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74671">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCyW-ys8grKboiPrwO-3_ZDYS_f3qU7u81Xl2HOAkAwTW3OUC0GJkCbvNVrHzdYhGMKygPbhHSMCpSUI1DGtrXx6liyjOU34lo90tVoqpDuV85pIgKwmLCSI3u5aI3ntLwfWGRduj_MGQPA3225Pt2lNBdjw6fUcrzmubGAlvMQHHuawterXIrAluPvBTh4E8s2ywnd7syRfFhBtUbWklKDjBkVT1YrC-lXQ1-Xd3wVoKTBDGXOqbCpJBlhRJlbVlt683CAcUOF6bJ2iR_3fRUvIi6lePNd6dFaUwb_yiyU-2KzfIP4ZiCvFryn4jX-ujJt1AwrG2sxV_i9rLixFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظر بمب اتم باشید
ابراهیم رضایی عضو کمیسیون امنیت ملی مجلس: اگه حمله کنید اتم درست میکنیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/74671" target="_blank">📅 12:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4814fa6eb9.mp4?token=mUaQvFCPuBCRICR2Il9U9s3_8V5RwdkI6V1PYV8Wlqhn59rjtOReNg-9Q10IUctAJfRSb5CsCKYaGcsX5EXbaWIBYDRYK4oUhdTIM3v3OzKt2NEu3e5PTVxVFm3tsqmCgMm35jLADXxXun8v6UtNQYVJD1e7QQDiasyisYmaQn3l10htIyiiTHJ1MjNOIYy_LBjMg2zlpoHGS5I0zdGNDNvzXjq4jsjqCE9jGp5hcVyt5MmadVnjRu9YK3uSOoH9qIlCKZZdzNpSfmfRCOXBdUB0dpkqJ3YF6bnQXB1monY_VwF20i_vq8ItQ_fq-dh6FTxHE6lSl3sT-gT1fEFaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4814fa6eb9.mp4?token=mUaQvFCPuBCRICR2Il9U9s3_8V5RwdkI6V1PYV8Wlqhn59rjtOReNg-9Q10IUctAJfRSb5CsCKYaGcsX5EXbaWIBYDRYK4oUhdTIM3v3OzKt2NEu3e5PTVxVFm3tsqmCgMm35jLADXxXun8v6UtNQYVJD1e7QQDiasyisYmaQn3l10htIyiiTHJ1MjNOIYy_LBjMg2zlpoHGS5I0zdGNDNvzXjq4jsjqCE9jGp5hcVyt5MmadVnjRu9YK3uSOoH9qIlCKZZdzNpSfmfRCOXBdUB0dpkqJ3YF6bnQXB1monY_VwF20i_vq8ItQ_fq-dh6FTxHE6lSl3sT-gT1fEFaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های عبری از شناسایی نخستین مورد ابتلا به ویروس نادر «هانتا» در تل‌آویو خبر دادند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/funhiphop/74670" target="_blank">📅 12:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74669">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک خبر بسیار جدید و غیر منتظره: امروز در جریان شهادت نتانیاهو در دادگاه، نتانیاهو یک پاکت محرمانه دریافت کرد و پس از خواندن آن گفت: «باید فورا بروم. باید»  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/funhiphop/74669" target="_blank">📅 12:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">"نتانیاهو به علت دریافت یک پاکت فوق محرمانه جلسه دادگاه خود را ترک کرد"  ناموسا وکیل اینو پیدا کنید، ۱۰ ساله داره دادگاهی که میدونه توش محکوم میشه رو میپیچونه هیچ کاریشم نمیشه کرد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/74668" target="_blank">📅 12:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74667">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ری اکشنا چرا رفته بالا</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/funhiphop/74667" target="_blank">📅 11:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74665">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf0tBGmwXBbs4t0tGrCnd88thDJwJIjCV1mRPPJsfcO5yCGjX5Ih4TrzpDwBdiTZ8Tyn0abZ0LfZu6RIkBRDGL-z_WJIzN384kp-jDhnjxMKQQaIwN1r2XgN0z63UMX0m00vU88QKkccvDHT1cX0nSv9bfcO8_6Lw0tCTcAccH3gQIdS2Y4uMjCyuMZZXfnuuMsn6DQ605AueoJ64t_OG6b-Z9Pd3JEC-x2SGGmX4Q6oziOmzvccFWItngcRS1qIGFgHGmPlrifnRwB2isqdJkUv6Ns7jqk3Dv3ZFLxUW0KXSiYV223Ak_GyGrpR7dM6fkgDHi4FK7IAzPozQAi16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیامی که روی بسیاری از تلفن‌های اسرائیلی دریافت شده:
جمهوری اسلامی ایران شما را به همکاری در زمینه اطلاعات دعوت می‌کند.
برای همکاری، با سفارت‌های ایران در کشورهای مختلف یا یکی از اپراتورهای سایبری ایرانی به صورت آنلاین تماس بگیرید. هم‌اکنون ساختن آینده خود را آغاز کنید.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/74665" target="_blank">📅 11:07 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
