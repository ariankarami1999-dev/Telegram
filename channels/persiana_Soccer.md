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
<img src="https://cdn4.telesco.pe/file/bwaMKbaQ0tl2qFfmCtEE4xRXkzepqC17cHGG7IZcE0Igo-X-PIHVQHuoYlDZBIGLR2iVcUfrcVPouA3H7mFKV6C8jYEFSYKbsxgoqtjzoTo5ASs3lIqMLWJI0wfVmtUhb1bHkYg1nFLrfHi-uDco9vpKaqDyBPYvtMDd0HlxgoT6mcqhcTGEp8-K82RNDgaiDaKy5Ierg0-CestEpn0m7PrJLVW2aIvSwqsKc0lhSalK7YH_ShxkYSdiSK4Q_6wBJPpipnBNw9YIDpZ6LBOVww5qwJt3GEhhrOOH-dteER3b3fgHaNLdOBs9PKMsxA6Pw6ciyDj4cyoQC8xUrMnfRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 431K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 09:45:22</div>
<hr>

<div class="tg-post" id="msg-30778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdLw2JYtdm6b42ycuydhjBrJEVtgVIWEFsYhGvEHv-oXealPGYIyWRsuepTYKTIVvHHZHkFJVdaQoG4KXk1ox-T3Qe95WmwdkypN7FXmb8GSqnxLv1rXCYCZMqZOHRWNdi8e4-VJeNm11EdMZ2bfIlM2Na13EVQYQFShn0-KOic1XnKpBaN16qBDTo5PLmrz7Jh2J9FyMRDnJMqWeZY-XQ8et9CRi0e7D0U6A9EEH3KMT5j5ZX8zxu6_y3B2UPKc1XCET5A5kNvDv8tuWnopCaHwY-i9C_YKZ-UGt82A1iL51KifItQyXg7fwLpPoeaRDe_laNRrjYFczCUFZvLsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تکمیلی؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ دو باشگاه الوحده امارات و پرسپولیس در آستانه توافق برسر رقم رضایت نامه مبین دهقان قرار گرفته اند و احتمال دارد بزودی رضایت نامه دهقات با پرداخت 500 هزار دلار از سوی اماراتی‌ها صادر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/30778" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=Tv2RGnzPCvOSMXdTX4Z23BR8r6MbeuK3YgOJZ02qN58ZIpHJFpFhonCWh-4qWQ--LmKjDKo0_6kXwJ0niDuYWeCIp2Hy68qd2FncbARV6Zn_4LeEvnUtyNCi4JN3EzDFrgen8irfdT6RJjPfvars4R0C9VjUt3PwgudqOcgEoj0zlYrmZ8tX9RNboMk-cgLN77dzDVktP5TTxRpKqaFrFxj8b5axfGPXNVmCJPj5WGq6Nvr7q-HdM98iBlE1RdST9PO0Ed97_doGwNEdlzCYmEbBDy_YqjHaUNasuKb807c2e7xxfkeAumN3uoyuhK6om1dadlm1UGjVeT3HH-0VQ3F2GjSa4HgJj-HK6GgyEHNqazcuzQ06Pa5EAEs1jiIC3_v568oy9mgXpLZskkxlBSDh7XPjiz1JKr2dDwxHnQKDcyBlFWQmBd94qHtVM3to8d5GuJbjjyg5LAy7GwcVdB7N27mBlaScAINuMpyMGsEIhntUfbxC3_yFUCWWHe--ndwY2eaOU-eq2PwaNXkMjyKKvFRnO4I_5Aq71HLMUzBEbQygHqb2Jud4tBeZLnQ1RPPZyPOmXSP8BSkpNJIsr4i1alCNI5oBDhNG7q1ZEtlY7kRIKOogWuov6liy795tjo0ShiIk3J1jXtVeYqgPX7yaf4YRZAM7vGimjoKcG3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=Tv2RGnzPCvOSMXdTX4Z23BR8r6MbeuK3YgOJZ02qN58ZIpHJFpFhonCWh-4qWQ--LmKjDKo0_6kXwJ0niDuYWeCIp2Hy68qd2FncbARV6Zn_4LeEvnUtyNCi4JN3EzDFrgen8irfdT6RJjPfvars4R0C9VjUt3PwgudqOcgEoj0zlYrmZ8tX9RNboMk-cgLN77dzDVktP5TTxRpKqaFrFxj8b5axfGPXNVmCJPj5WGq6Nvr7q-HdM98iBlE1RdST9PO0Ed97_doGwNEdlzCYmEbBDy_YqjHaUNasuKb807c2e7xxfkeAumN3uoyuhK6om1dadlm1UGjVeT3HH-0VQ3F2GjSa4HgJj-HK6GgyEHNqazcuzQ06Pa5EAEs1jiIC3_v568oy9mgXpLZskkxlBSDh7XPjiz1JKr2dDwxHnQKDcyBlFWQmBd94qHtVM3to8d5GuJbjjyg5LAy7GwcVdB7N27mBlaScAINuMpyMGsEIhntUfbxC3_yFUCWWHe--ndwY2eaOU-eq2PwaNXkMjyKKvFRnO4I_5Aq71HLMUzBEbQygHqb2Jud4tBeZLnQ1RPPZyPOmXSP8BSkpNJIsr4i1alCNI5oBDhNG7q1ZEtlY7kRIKOogWuov6liy795tjo0ShiIk3J1jXtVeYqgPX7yaf4YRZAM7vGimjoKcG3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌مناسبت خداحافظی غریبانه کریس رونالدو از تیم‌ملی‌پرتغال؛ یادی کنیم از این هتریک تماشایی و خیره کننده او در یکی از بازی‌های تیم ملی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/persiana_Soccer/30777" target="_blank">📅 09:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJYX0ESXlinnfMWZVXdMdlOXvnUnN3GCNGfMV3MZqrfDi8a1sT6XaoVmIRHhJREwjuT_SMQFB53RwflrRE-bPonxjd0k8mfamXFXwkJsrGwD9zE5e6U4O0IwEXcEAyBv1skZwah097z__jPNVAzRX3l35FAKWkgBrfJFXNYCPmDzFfk3YvT6bdXCAdcaJfHjs8Kj5LLaz4afVjyZ8ufM4tdpxtXKgZuDTuKDhQYrpl1jlwjtuEqDXhZvXW5wGwUMKgcOvRhYt3izolELAwGgTCHkzcu1fOse7MypH2_d3WmH_ebJ6QJjfPS4BEMdHY8BOSPcHavIDU5Ukw8LtJUrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/30776" target="_blank">📅 08:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-janbXR8lDz8jnJoDpR59TCV2T-Oh0z-hls2wc2aDm7ngEmSs8leCBu3ZGGDTUWXIyElbxYgC_tJu62kjNVb1YxtkKm5lGoqz3jxwQXrHL52u7PjA35KbgkiqWD6JpwuG_N2NxPcWJrfFARpnWPNVVPasxyOArrOe4v7rr1rbqu8Cq4zesT8yQhfut_uz1G3t-41JQWOoQd_DBdBjefjjNyX8ZtmtdxengrtVKd0pZC5r-lEIk6iHynN-_1DVvH65R36B-z9z6JKOahiAvuYKFeHqdH6KNuymsRQVm9-FtxdkoBbG0ORxct4jnDOZ_ubor7X-kUDe2lVv8lbWk9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/30775" target="_blank">📅 01:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30773">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbbdoZrX2YmJ8bZRRc2jZHm21kGRCG8fW-WrlBufRHQMhIf5cMM2ETq4dFOv77kp7wCFDLXke_0SzXW8g5jSdQsaIdrtow1tdmk09TUDU6RotbiZUTW9Ll7u1eR-gOXSROYJ5zVbiI_khHZqH0fb5_tK7LNSDn7tR0Jb2wh0TLuBr1ubyT2V9_5Ae5z5eAeIx8gf27NDwwg4dw60-Z2YaPQWtsvYrVDwc7dtMeHHP35xpB2fp-4EmIYDHNP6TKk2uMs7opiJNOzf6MMZqNra4S05TjA0sfl6Lv8ivu-TQoMCx83YDaWcWUHPEozKZJv60kWWZ6sfMMJfllkkMMSVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از این به بعد جای این دو اسطوره تاریخ در تمام فیفادی‌ها خالی خواهد بود و بعد از سال‌‌ها دیگه قرار نیست آن‌هارو در مسابقات ملی ببینیم.
🇵🇹
💔
🤩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/30773" target="_blank">📅 01:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ3q2e4JNCLhs4vQO4jQaGKRvF-3fg4QAFzUOmxeoSXEw62HA7Illf7pC3dDfhmd6PrB55-437X_jh67KX2iBaw6qd9RzkmouR8WG9m_HrTIR_xtr0U_ABGe9dLT0YXeOIJtqeEjrYbnd01glX6TI-cOg6PGUhPBUsqpdwhm_CnD-MyIVSjJGpwS0UfZlVVK-nGthzaPELNA6QrK9fKP-um6yzp-er4ie99Jh0bD7d8Z8oT1BgyGvgKWYpschfDw7SDoevYUk_mnsosbH5daRz6SIDchIauCVWB-_5y6UdnJa6cbYvO9EvVa162N6IwogytoJMsn80h9wLAzaZlmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف آرژانتین و پرتغال برابر بولیوی و دانمارک در غیاب لیونل مسی و کریس رونالدو دو ابرستاره محبوب تاریخ مستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/30772" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3y_P0YRkGPOcuPwyWLwrY6_Jo8k0EszrxD0xsxdYpnBRCsxJGXVSUW6WY0d-efrJiZ3QCnQONJLsAdBE1WQutSyAt2nS92sdL14yQuA-NWjcbJxinBR3qfnaMOgugrUhilt4tqgdQUPnmHzKHIwWpYCnPqqOwv_Lg8R_po59MKSvqLJDsSTBoLa1VWbsVnQvZ9av-4JkjMgIIsPebfgjtAbwfdHoa-i7rDRrdvLBX1CyFdt9Zow_LFBzAsp9TCH-VsThTpz6_Sy-sfSHChidc5jABYCFTsWPNaQn07wAFy8lduK0RBytAnE1y9uNXF5JmX9aOSHwYtS_M2pdyjDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
برد خانگی یانکی‌ها مقابل شیلی و دومین تساوی مکزیک پس از برکناری آگیره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/30771" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNMW3TP3cuHXt_UG20jqU60SrMQUB0DK66Z_JcJrphQiAvo-LKqJ0cWnInt4gdBm9kq1uFxJxiiI3f7S10D9cKCue_B27WMyKFtpgdBPRHBh91AxLjYHT2VOUvkbJFnkvMOZFHCmID1mip676daHwUulba8c4hvTZmUv3aMRy6rPYrGgmb7UOKqi9fluPepA5N-5rCV87BWNtM4SIKRIH9xwj8RDtuRrKz3BqLl-k3gcF-QJgqa4_AAjsv7HuiqtVm4cBupBTA7iEAflwybqNQodxZWq2oKzelHWlaxRBjMZBUY9Cb6Yb0LEueJMPu4xWqSdBsFmK4Nv6sJfeqAWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
P8
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/30770" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6TJk4tnYHlkCGMZdFZSkqniPF6JcXy6DAUy3ayH3WimiRBZPAkN2g2tFMMqzwxsBnFRhENeiT2Mtf1oHIPj_viIfRJTy5hqy5L1UN_O3fZ9TclRaczcnCe9VkErPCkwFT6tro9Eoxp4k3U5QByb-teac0vrPU27yWl1vDTA9sy2DqYWfnGCYIUFyPpQtSe9iAf2I3LF3tqzSR6JoZcNSuY_RcP3of-p3HZ27fprPEG9bdMcciccDI7ofn-3s212dCT9wGqkUcaGDsp2580Q4CHOQFfueyeltFyRfcNi-paV-ninvtNsNcIIJd7YIyCUYE1sgxW0S3_fqcwrmQ6h-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/30769" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVr83Q36zngaqFv6keuRYfjPR_XHR7H1fLi-kSG7XLpL18VEjptj6ejzOuyE8vyVcrrL5UR1hYmupcHEK3SC3sqJwLPdRFmMDmn_13EQfpxionQ3ZFARsU34zvnsSLirLAH3qfuJFk-EYrBHpiHJTBPwT0hFyKusuCSnWw0bm9oxqr8wo_71bTrwQuOHdBMSjhEG-opyNXL-Ptb9hdFA2asYxDDOmeF8aPEZe0-zEEADUb-GKYc7XM68UKXCSWWnyXgAXaB64vwkGSEqcYDBtRrt5wzk2s6tzQ5-Qe8R4KD4Uk9DiVySCeGqkN_bGNlM9R13LueQ0zCsuzPNEhNiHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
روزنامه‌ اوجوگو: کریس رونالدو دیگه قصد برگشت به تیم ملی پرتغال رو نداره و درآینده نزدیک هم بصورت رسمی از تیم ملی خداحافظی می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/30768" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ploTWtDolDS4HyV0DGA8QfcoX4seeT3xQH8dUBsWlV1Mdh5Mwl2oIPZJ8NBM3M8h5-W7rcAnrtLHrhelApoRi23m6oopE4O1GclvVwluy3k23v7OlLneYgx2BbGPN46uEzglRDITxWS2NGKFHFNTmgE-RmrHk79pSTfVDrpBlCOWSdz3f6ctt9r7XycVPnfG8879eQRUvdjhXQMGt5jm4t057bhkZ_lLcDSAYfmd3yHHAeQ2lEbG6HPiclNEqYwED291EwZgpr8JpQILRrawMVq-MRBP3paqLCbU2oinm8TzTXvnxYnIk9yEW68qWu0HSdYIm2AEj5J0_AxELNYCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/30767" target="_blank">📅 00:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq9PWfRS50GEK4h3d0Ln_7VnNItWDLP_BxjUkpfNvHmCW2ZsX0OX78_ubxHWNWDWyFYVc4Kt-40pttigIXleusrGyDZv6b04jF11_ZomESmRsJKkbvZnf08zrif2GBvg8TeLw8UjuxvlJ1VjmZE-KpV_P20vjm9O_L59s7xMSu6PUKb_52t1qB77esewhI4j5UClJKg5tV5Su138syTE2KDUfhnC-T3quHLZs66s6xaEA8NiDGHewgakcjgd63FIyiT7klxQE5tMLkx0V15bqBSM0aVbyyW0s0aRHU1pTfn5g_wawj9Prg0CpmxQeDZjHB9GVOIMDWXJ22AT4sTLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30766" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=ZTel60mz8qgKsqLQ6_LaoXMWcmq4BfNE0Ksjc6Soeql73dmEtOxCN5TXC7E5WNu-2rl5oHbEx4pjwfsN8CyWFUvsvQUD0mJwsYpo7aM1Pafqo5FSC0QqZJedke4U_3prIwRNR3NG2qhlV3XZ6cME4c2qYVXPNOmQu3EbZN-Cl4USL4bAk836MIH2AawUJilV419g7MomVAir78qfDUzF5undEqw5GZQnp9a4DpPsg00cafLRGi9JCWEBqOB99Y_tqipv6kLi6b2uSkRoQ00Saij05WST7dzwR8OmvVoCeDaycWPFUcC4uxtJSuBGAb_gXbNP9AHq41CXcP7oVI0t-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=ZTel60mz8qgKsqLQ6_LaoXMWcmq4BfNE0Ksjc6Soeql73dmEtOxCN5TXC7E5WNu-2rl5oHbEx4pjwfsN8CyWFUvsvQUD0mJwsYpo7aM1Pafqo5FSC0QqZJedke4U_3prIwRNR3NG2qhlV3XZ6cME4c2qYVXPNOmQu3EbZN-Cl4USL4bAk836MIH2AawUJilV419g7MomVAir78qfDUzF5undEqw5GZQnp9a4DpPsg00cafLRGi9JCWEBqOB99Y_tqipv6kLi6b2uSkRoQ00Saij05WST7dzwR8OmvVoCeDaycWPFUcC4uxtJSuBGAb_gXbNP9AHq41CXcP7oVI0t-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر رونالدو: ماپرتغالی‌ها نادان و ناسپاسیم و لایق داشتن بهترین‌ها نیستیم. تیم ملی پرتغال هم به همون چیزی برمیگرده که قبل کریس رونالدو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/30765" target="_blank">📅 23:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ1H6Bn5fxcFS6DR_pH6ioPO6ICbonASsMgDUYx3qFPAl45Ba7isOK0GdhQk_6qPsb8nq7dEB3Rz_oubeGswnH7jD6hq61US65LQc5UR2JmaX_ToFAofhV3wXREzv069pDDnEobM8_f1xBaXB0uEK8oN6X9vOITPbDk-4H970K9zyDRm2wVBxh8Yi7eMuBg19hXi2xzJSTY8Y2rFhxyVdZrRwO7BzEeh6FWAaE9NgbkNmlz3qQQTryT6vsI3GEJxpDHxuZGukaA_jQ9EWU7EqmA43Rj--fbU_l_lUIcjBvLTxdNmF9ZsPwX7sFYdeBXY_Qzd9BXW7lWDgVtdxS_-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30764" target="_blank">📅 23:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=dVGhXYMte3qIib2f5QQ7BiRXsoyEOw7N8YhmaREC03Z298yLs6gUbR2yNSHErtJ0m2Nd1Rv0fhTVZNiSZUXmnhMIaVf9L92EcR9W4yYta6Wm1P1rbxq7mzzfENPv77qHw-_xpa1oQNv8B1Kos5yY4ijdHSSp9I_JOo-UuXo3pNpIFRWUhjuF1Xjd0cKvUg7Awx0WFCMvkL1_NTUsyDaIzDTN56ckdp-0AqjeAx9VMsmYhuFHt4X0Q1DugAggTgmo6bOrbYUWKFGagl4mZjheTVEsLRm49_XqeB9TJl6awzvaE-5hQO64pOKJr5DXg2wRG9e7VgNv13mnhV8tgPaoYb1Cf8daxEP0SVTw_2DgGIeW8sB7ugrzweDkeN3EsQjrRo5yFye5lrBVDQtmdqAb9AMianoKz1XRR6p2O1mqBCtdY4G_v0YMtITwh6sjR_II0l2OfV7mb3zBjbZEONoAwViL4v1d34wzxPZtXGjv8WiGN_SUkL43B8P9FQtSEYJ65a-Q3RqTR22fzyM5F1a_1LFAXRxEwJ0jG7fCp8q7SmLTUPN79fZjsWxHZQfYjFJNv1EoNnUdi9q71h8NdN9DS289tOt2yNWCefaRsuy1Px5Etr6k_O9WR0Aqa0cDb67BlUXG74P8quHCdtR3a2ABn2H4NPgWDFDelHAL_ms_9Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=dVGhXYMte3qIib2f5QQ7BiRXsoyEOw7N8YhmaREC03Z298yLs6gUbR2yNSHErtJ0m2Nd1Rv0fhTVZNiSZUXmnhMIaVf9L92EcR9W4yYta6Wm1P1rbxq7mzzfENPv77qHw-_xpa1oQNv8B1Kos5yY4ijdHSSp9I_JOo-UuXo3pNpIFRWUhjuF1Xjd0cKvUg7Awx0WFCMvkL1_NTUsyDaIzDTN56ckdp-0AqjeAx9VMsmYhuFHt4X0Q1DugAggTgmo6bOrbYUWKFGagl4mZjheTVEsLRm49_XqeB9TJl6awzvaE-5hQO64pOKJr5DXg2wRG9e7VgNv13mnhV8tgPaoYb1Cf8daxEP0SVTw_2DgGIeW8sB7ugrzweDkeN3EsQjrRo5yFye5lrBVDQtmdqAb9AMianoKz1XRR6p2O1mqBCtdY4G_v0YMtITwh6sjR_II0l2OfV7mb3zBjbZEONoAwViL4v1d34wzxPZtXGjv8WiGN_SUkL43B8P9FQtSEYJ65a-Q3RqTR22fzyM5F1a_1LFAXRxEwJ0jG7fCp8q7SmLTUPN79fZjsWxHZQfYjFJNv1EoNnUdi9q71h8NdN9DS289tOt2yNWCefaRsuy1Px5Etr6k_O9WR0Aqa0cDb67BlUXG74P8quHCdtR3a2ABn2H4NPgWDFDelHAL_ms_9Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
#تکمیلی؛ یکی از شروطی که فرهاد مجیدی سرمربی سابق استقلال پیش پای فدراسیون فوتبال گذاشته در جام ملت‌های آسیا روی نیمکت تیم ملی بشینه اینه که مشکل سیاسی اللهیار برطرف بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30763" target="_blank">📅 23:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNJ_kXPAKrYz7CpNaf3Kalyun9kQFQXipQ1xxjFPDajMnUsMpYaag6erBCE46qgsOvZXvVqtcDAhe6CdgYP_eM0y580jbRdyotU2R-gyOztpDR1MtcWVR3imPgS8GL2OE_lIvHeI2l9oIeqjC5aHctqGZ9zAHQO8dXB0bVCuRWF7AxREeUQSgE04lmiS0Q1ZA480fMccVFDSud_eDogyYgtDA7ritnUe5jzANUO83X71dO1e3_BNcW2dnDF1OLlvsfkapGmIAHbk2-A6TshjsGfRxK3maFGmktnWC2oX1HkNwpmaoGjIzbFkXL8-QjNvIvI18NxR1DfIVvR2dCy3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
نگاهی به عملکرد و افتخارات کریس رونالدو در تیم ملی پرتغال؛ بزرگ مردی که یک اسم میوه رو تبدیل به یکی از پر افتخار ترین تیم‌های اروپا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30762" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arBaHdAhsXRypl5Nh1NGzyyCv26TrohO53kEWat7gdljHi643jJ4b3xIxcVjAwIY8L9XFH9hGsktVVh3wDz4qEbrrOS2MdSxixKFYEvPzAvZIna69FNH70JXJNKiLvGtacjORMXrd3IGYI1dFlf1RIlT6LzCab_rlJ7Ydgq6f_Hz57p9iXNNZ8TalKQWY8AHSoDFLc2ag860G2cikYeM5TxZRZQeBFFqI3LTBd7bKAh23mFSIx7HmM1yZNF_hme2dFUitiJnZvZiwXTy4-_SFMM7V5Z9Q-hBGWkYPWh7MCbRwkWWxccp8elIn2Jfb0zLpYf2Pje-r6LZKWty9FDFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعدِ پیگیری‌های‌میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد. خدمت تسویه و تحویل که بعلت‌مسدودی‌دارایی‌های میلی دربانک کارگشایی مختل شده‌بود فردا عصر پس‌از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت. همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30761" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkoi-jrwSsykb1hC376AK1N1FMT1Le4M_tDEjUovKLDt1REgPcQC_2qMk1nTShxSq7rzYVSfUEE9WCUN6poNsB91NgPfUuOHLMdNkJ8R34vmBOrX3w7ZQON0sTWXyt2sNyZ--hL2dyo2XZ9XJmg-jkdWB6HRpHsT7zuGdXCoRW0QmWXhI7f3dOTciQIK7XkeV67L1kPvPFMIqiteVX7vqQBdddZ0KSfYxpYioh-fde2Q4PG1XFKaAmy1TZeRRMjON2tin-Yx2iThB10JU-06VFnveKg4QEmrcUBtGCrf_GCPH2cJQZWDEcauA0rnBXzw4ncAnJ8-R2HJrm_8MQET6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30760" target="_blank">📅 22:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGAaRo8ZgtJN_AT190xwsZnkAUFhYYUOH-zxkcz4OAjTPJTgjfh7yuqT8Fbbeeuwv3XAksFVnDqF3kcmILzj6AIa-N9zOH3XVmcNHgtzYMMCPWk3-Yxt-XV7Vki9xqK0ikQ1VgDjkngrQBqI2lbYOaAZXSAgLdrMml81bJiGqfy_xh0BnyeYTxyTzZFegrJSCFvo82dXDe53XsUnvt_BvAqkkkBp7kLrRhBew752eI0pXlq6bIk_mqQRISQs_ndljKos5KG2J52X-awQ4K8ySTSTsocFXfa4Gbq6gaSuUTn45zBcRO0RUqsIsM-jW_xaYqYxcnIb6VTIuALyZ3kL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یورگن‌کلوپ‌سرمربی‌آلمان:
توپ طلا؟ اگه تعصبو بذارین کنار و آمار امسال رونگاه کنین متوجه میشین که‌توپ طلا باید به مسی برسه. اون تو 39 سالگی یه تیم رو تا فینال برد و نیازی به حرف زدن نداره دیگه. چون با بازی کردنش همه چیز رو بیان میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30759" target="_blank">📅 22:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUfD-2wT7PcLrq9i6mLGN_jxufYPWsLgw41Q_bxN7RHLDok5Ed4S_mpb-X9weCKS4UxLq373t8YaAsTdkEalsvwawrRRtvRZdulARpMMkiBhJDL3Q4a2dec0aXPWLtKeWx1OqcGlr-nspDizxEnsK6MH1KKZbArWJ0yn9sJo6nRv4MnQEwjWpLUnhZ_eYnt-McvoVGwuZyeMjqRTjQBmrb3r5-rxXiJmMaHYTfHMX1D6Xk8jYon5IF0JNB4tRnDTDuDipnixHslOFjYynzeHbLAIrhtfxM6DNb1LZMttaKLkULuPCg9zOoz8fi_oBUhilYi0yiXLmeRK9g64TdffVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کریس رونالدو: اگه کادرفنی‌پرتغال نیازی به من نداره خیلی راحت این قضیه رو بیان کنند هیچ گونه مشکلی بااین‌قضیه‌ندارم و خیلی راحت کنار میکشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30758" target="_blank">📅 22:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH259du6z3Fsj7cLyxwF2LswoFt536wqeKc1Na5OqFMJ53GgqcJBMIagq2zZcudUdyh7oixM2D1-uLHeGHMIIljwCGnT9TMutIpQm5FIQGP5ETWZxdW6sd_TMDHoMkSAqu2m9a6_arlaqD4aUp__fHHPWmrl_k_OZvgkfdyJqB_1WzRdK9ah-gA1Ne-tmFTQ9KQJsGi5y3tniYShk7J3pgt6ZqW8UDVtkwHSET1ZNxrO9Ere7DpnR-BKlulFuFUUo-APmeFxsJAvdrw_dNnqsk9tKNgq1dF8-9yVo6GiIkODW8LAL5qUTDN4ZhgphrGPrQY-G03w951-NR84xXS-c4es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH259du6z3Fsj7cLyxwF2LswoFt536wqeKc1Na5OqFMJ53GgqcJBMIagq2zZcudUdyh7oixM2D1-uLHeGHMIIljwCGnT9TMutIpQm5FIQGP5ETWZxdW6sd_TMDHoMkSAqu2m9a6_arlaqD4aUp__fHHPWmrl_k_OZvgkfdyJqB_1WzRdK9ah-gA1Ne-tmFTQ9KQJsGi5y3tniYShk7J3pgt6ZqW8UDVtkwHSET1ZNxrO9Ere7DpnR-BKlulFuFUUo-APmeFxsJAvdrw_dNnqsk9tKNgq1dF8-9yVo6GiIkODW8LAL5qUTDN4ZhgphrGPrQY-G03w951-NR84xXS-c4es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وکلفت ابوطالب حسینی به رقم قرارداد امیر قلعه نویی در تیم ملی فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30757" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N963pTbc80NeYoyJqYidjHxf2k2VkKLdX3CQK0HIFai3Dxl4c5h8oH8jA8AmGWjG2zxBelg9ikf4TcfKBbvTLVpkA6W1m9kZVPecDLeYQTpLtBHZBl2L9vt2dMZiaGoiR_CTC1GhH4wPk-atHH3SCOPsXTGcMY1omJWbqylmD6fptGK3TgzetMYC2d0Me-f-p2Q394V7HVwNz81ooSf_A4W_aDxdPf65ushGy7F6iVLABDPy8cWawQf0Vv4--_bafM1h0A-pHjCnXw2xiuCQtJdMnr5bl7CWn5zMX0440EPXKs2xMW_iHuI8XSUifldX7IetfEL4bbB9EB6zWfDCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30756" target="_blank">📅 21:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzwzeTbqODUp8UGosLSUsAoNAet6RiNSgWWNS1vdpNGXWaGzECXrk4LWKP7xJhW8mhPi3v9eQBHy-GOSk29Exw3b2eEcFu9YNNDQX9qP9aLQH2v-rDbpa_qffBOPcaYqjcSCu3MU1n-xBtu2CUa0lgoXuoy1u4VPiQDSbCEfD2jREgOCUTje65ZDIpdHg4V_mlCCeBRip8EOnoSxqDKpVkKv0UGHvjh3gdIxjbNTPBYJojwh6TzoU76GgQgeW9peZfIB9Blt3cGF7qFFkNxvzuIlvuZxOzdE_GP0WxPZII4PIkL1YXaK0I5Mzsg6B0abl1xk86rwNrHmvv3wGafSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30755" target="_blank">📅 20:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwkaFtrCLm5szlSomR-Q29RQc6oJJlr51OT7mtnY1xcTm_eX1GwmzYWu-qtV3LUL5XvES1tnBoUIvAgxS_3MMsKIYqkPJdwoE3wYjM51XkYR3HIcN0k07VzQ_bval8nKxR9bC8FFXhWCtq-MuUokUY-OR4KJNh4aURdCEMqe8bcJyt142g2d5aDCQ3DGU-EX3o9JrT5zHwYmTgfAc2P_MAGMOWeHFL7cycRSMqPXsRH6a7WjM8UNcDYoTyacUSFQGZ0Vee-_ReEtzpOEOfs9bEfplrusCaTsSm21oQW25v1DtrLyy5ITz57OYqv_VPBI4RW0oOXBgR2S6l4EvpYORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تالار افتخارات ۴ تیم مدعی لیگ برتر؛
استقلال و پرسپولیس با ۳۹ جام رسمی بر بام فوتبال ایران؛ سپاهان با ۳۰ قهرمانی نزدیکترین تعقیب کننده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30754" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=IB5jGEQdYCgCVPRCz5rvcN7Mo0AhmKx6iwp2-yxOH-B6hMuqtPax5V_yLYx-STh5h2dXc9KZ3s0q066g_lGAga_C8D_zAUILNUmvLNTvMeaT0OjQRIZZs7YypjwJhvlZiZn7wVpo-DxexNlQ6m-kP7GY8Hfqtb_Cb4nSAGdmpNIAXGjdwnYonIslMIhoLra_h0fJeD2RNKFGzxiWmazjhDZSsX4zF7BzA3U9iEdCCOednpI_JIiY6U-36tH8B5Sk2Lk82xPVwqyZ1w-4QXB7CbI0uIfSQpW_3WQitFb2bDy5iQ4efz7HU5j2E9eT-CzFgooazI758kbNaat7vuGrZbM39DXJa9S8F3T4VpLyli9EuISQ722TEDfDggSEbhfzbnOG0BeTBbuFRkrcXq-lTNpiehqtic_iz4GDEoBrnZit1J3zOvr9VHS6CZTnf4lgEl1V_PFOwjANFJk4dChN3k5xLpYBmGxrKzqFYloNqY6ehv4GH4prWYCvTLohXmPIJuclSyg7l_ILh8ZjjYvqT2z5qvUj85CLAbc0Mp6CKvSliR4R8k12UJPr9rT8JrGFNERtM4E5RBbysCbCiSwCqVssrrMNnCKlAkDs3bVM_Sj-m-w9TtNWJ3bxBJe3ROweq8xdRCfc_mhtCl26M4WRo5KDoV6ba3W4suvG01UEFE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=IB5jGEQdYCgCVPRCz5rvcN7Mo0AhmKx6iwp2-yxOH-B6hMuqtPax5V_yLYx-STh5h2dXc9KZ3s0q066g_lGAga_C8D_zAUILNUmvLNTvMeaT0OjQRIZZs7YypjwJhvlZiZn7wVpo-DxexNlQ6m-kP7GY8Hfqtb_Cb4nSAGdmpNIAXGjdwnYonIslMIhoLra_h0fJeD2RNKFGzxiWmazjhDZSsX4zF7BzA3U9iEdCCOednpI_JIiY6U-36tH8B5Sk2Lk82xPVwqyZ1w-4QXB7CbI0uIfSQpW_3WQitFb2bDy5iQ4efz7HU5j2E9eT-CzFgooazI758kbNaat7vuGrZbM39DXJa9S8F3T4VpLyli9EuISQ722TEDfDggSEbhfzbnOG0BeTBbuFRkrcXq-lTNpiehqtic_iz4GDEoBrnZit1J3zOvr9VHS6CZTnf4lgEl1V_PFOwjANFJk4dChN3k5xLpYBmGxrKzqFYloNqY6ehv4GH4prWYCvTLohXmPIJuclSyg7l_ILh8ZjjYvqT2z5qvUj85CLAbc0Mp6CKvSliR4R8k12UJPr9rT8JrGFNERtM4E5RBbysCbCiSwCqVssrrMNnCKlAkDs3bVM_Sj-m-w9TtNWJ3bxBJe3ROweq8xdRCfc_mhtCl26M4WRo5KDoV6ba3W4suvG01UEFE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30753" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyAilKfZr-Cr3nswfg11guhdY7X5-qX_uABwepiPPtk1exRY-ryk8c1zt9Sne9Yfs1E5PWLuuQFF6Z5s-6SydJ0kWYil6UbgeMUcS8WG3jPc5i38GaZcGYZUhvO2BNEJHou4XGD784UfPApoDSjQgMF9r_2Y1dR9fzeXn3Dn-n_es2Q0s9qHKt4Ov8HcNqLsBLnshZMBh66i93N8Uah0OrFSvBhRdj157EYxXauDSlZnsx0eay9ovMFeMoL3t0Gbb58MB5J_V3tq2xoI8zCs-AFPgiwTPxWJzJmLgdZGKx9lEkCN34QXoHoT-WRnUaQSJG55UoxgcUggOsPL6MmW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30752" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42ded691.mp4?token=jf7fxEU0SRI0Rk3BeJsidT45SNVa97yG0bkIA5fPlvb0uMom8CENmF34UwdauMwjJLf8nwLbiVDxwH0xpE7ldL615Oh9RJ_Opow3Rco375gry-Ggbzb9ISYyRchlycO0MgZYsyWbpnAOGAULmx9lYqyt4Ii6Du6c0boszy81XdB0Gi6K1g-VNu7SQonjhFnS_VBsQLQthY3pNspxo09TjYWSd_5GFnv6GMEpf9bba9IYtEGjksgw1ZuBzytfK9Rb7w5txW_pDxHqznaYY4OszYOvdk_LeHtZauQmTKqlav0Q1MuV_SjAY8VctlEfE3VsNkyQpt6_J1mupUC7o4yHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42ded691.mp4?token=jf7fxEU0SRI0Rk3BeJsidT45SNVa97yG0bkIA5fPlvb0uMom8CENmF34UwdauMwjJLf8nwLbiVDxwH0xpE7ldL615Oh9RJ_Opow3Rco375gry-Ggbzb9ISYyRchlycO0MgZYsyWbpnAOGAULmx9lYqyt4Ii6Du6c0boszy81XdB0Gi6K1g-VNu7SQonjhFnS_VBsQLQthY3pNspxo09TjYWSd_5GFnv6GMEpf9bba9IYtEGjksgw1ZuBzytfK9Rb7w5txW_pDxHqznaYY4OszYOvdk_LeHtZauQmTKqlav0Q1MuV_SjAY8VctlEfE3VsNkyQpt6_J1mupUC7o4yHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از ابراهیم‌شکوری درتیم‌امید تا رحمان رضایی در تیم‌ملی؛ درجواب‌ناکامی بگویید: یخورده سرما دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30751" target="_blank">📅 19:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm9UzV8aX34N1ILOj7y8PZTPq1gBmd-S81XYyRZii0BSi3zlmk0hGPjP4MiAcLfQ6ynVmuCcM914_fu0BPK-TUXwzVkdaKev2hP5fw26lytdUtJbNtkyKj2-lDbRy3mTlijCjwQ6N5jBpZH04plsw3SI1G4cuYP5WdBNpbIjsxsk-JVP_xf75zbrtfsZgVORZYPrHbsueSbDV_C8VnZsyNN6hWs8JhIclZ4pEOXJZVx8w8ZXyYDSYfl4Zzc16KBvRobjOGsdRote0oOpU6wDxdZh1hcztFAw9JIWGRTwOGrL5HmsxGENbIzzlhcKqZ60vqkKB1HPTUFNh8_DNe8sWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30750" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=stBSHfa7xUaiyw9gPwrY8kwDUt5X2jo9LOpAZ4uNToECTODx-CyiRBt4WGQpvVNMFWwZid2k2hja2cYCd7jAr3rPAebVMNO095ene823joNvJ5B9dAapy-7YEcJNRREnpejcNA2GB4HRkrlRn7H0iVCpXMtpjSvr7_NbEfxuQdBlBRJbwv2G28PU_mEtncq0tk_JwpOSB8BC2NnMj06Be6_RmamLVnqDw9PvkfseVjP1H2NyaDl9kJWIWplgv791xTHMrhKrYtsSHbXI6cFt37VPLuKVtdSKJjBllsdJH6iMwwLKQNUg4lH522lIl5lxR6IthVqyOTJtZouH2nFO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=stBSHfa7xUaiyw9gPwrY8kwDUt5X2jo9LOpAZ4uNToECTODx-CyiRBt4WGQpvVNMFWwZid2k2hja2cYCd7jAr3rPAebVMNO095ene823joNvJ5B9dAapy-7YEcJNRREnpejcNA2GB4HRkrlRn7H0iVCpXMtpjSvr7_NbEfxuQdBlBRJbwv2G28PU_mEtncq0tk_JwpOSB8BC2NnMj06Be6_RmamLVnqDw9PvkfseVjP1H2NyaDl9kJWIWplgv791xTHMrhKrYtsSHbXI6cFt37VPLuKVtdSKJjBllsdJH6iMwwLKQNUg4lH522lIl5lxR6IthVqyOTJtZouH2nFO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
به بهانه سرباز بودن دروازه‌بان تیم تراکتور؛ وقتی‌بیرانوند از خیابانی تو خدمت مرخصی میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30749" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗶𝗽𝘀𝘁𝗲𝗿 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktfglt_asellSkLDkgOCSemKbuwIv_EMm529giWIXAx7WdYetwIBaksIk-_5F6U4yrsVCOMRsTORfbggBzrN158Y2M7NeoG6h9JC5xjblDV_N79LUEwPGEWEObIGCepDbROIoUdicaDvdnQWT73EFMfjxE35-y-HraJBf2Q7h0_CBCV20HMnFkZj_M4r6ewUSKgJfLmTXT986sSpvfwUxrzFsPLS6cOTOtpbAAbsnGdKrVrDoafE4im17Wtr2hs0IbKd1FgMGYoxYQIXj5ifcoaNbhymJWxVR5MwK0MWPeP7mmBirZmMdYwil6CwSXBB34KMbKNruW3g1u0tEnq7Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/30748" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2SXVCiHn2lpX0DlmsuH-WmO8xrTDYShrcJ5F1ci5IHPNZSzE-plEtfm42gIZLmtlBbh2NZ4zEDzjOzoZkJHeRCsN99N9ndvJWrtQAN32CdV-_vsLdxf3bqwvUqVatA7vqzUCF1LkrjaDR1prs5PxGgsmk3eDVGoICU_vh2ia6dzRGk6d1AQldE64gWKlDG_sLpBGHn-uuiFvkQxPwLBnrDXaRH3L1vJ_cmMkYn4UPkiYOiWE1AH96rbuEZKJWCTXLwLf4IebiONNRUlgZv51OYMOm5hk0bLG6brIoFiKBOWPvLu1u-c1cp3XKVkMrV8d-rVP-1EnRDxcLvBMY4ZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30747" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQbdrtn1g1RGLC4P_9Jm0uJgTGj0AadMTEOc8kFgWvHD03Mg0QR1tKm46vMuMpZhjt1lFrAcWINRusQ35hTgglUM-mxBv-izOUHYpkXDILij_K6YX5Dt_bcOxJuNp7g2PtTQ2W12U-Naub4xhmZrC8ZIYgJC8ZFdpUiUXBCzf965LmlVTULd8v3h1sXA8EHJ-6e-EzbVlhJiHDXQBTVYCV0p08pYfalKEJbclQiz4bP1OdG0eizSonvEa_Ivg8ZZnIbyJzthVTZy1z_hf2w3_ztixoXxDk62_xal3psLOFaO-A8nM15wNj5JSyvdk3I8ipQFYVO4vTKorKH5-XMg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛ ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30746" target="_blank">📅 18:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb0fXGTgz75m331Mxi9CYamsMI6ayuVEuM1wc9pYtjGQ6tJnIkz-Pbh3jWFapq0if9ze5KZSPf6xDBoYgxh1MqMQydIXyRQeDkid3fu0lS82kFIJODaPmgxEuHiPFas3MI-bpLnuDlp6b2eJfk2QmTWQj8oQQqIekyfqdkV7eQkI-pDyctzW6VYw7cJRJx_gidPw7xZ7inzlvOot_fE5ifwFZdwhYUkDDSQOf1vrJbNowLq6r1dPQ8PJxE8DXh1zX4Y_7c9PM1tkeCQorhwWyUCEirHzL9CwV1MNhdHVIj7ZEUTrR_cbORiE2t_YYHmxNxDm0ADyiBMhF64OhLIjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛
ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30745" target="_blank">📅 18:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQYI3LH1oOvkNU2BYD7GyBYbSBbdSFoBALNRQ7djaFc-XBP63925eRMd6wk7UKxgCoem70nRl3-49znXAmKXfAf9o2mb0T3YO7BvEjg8jHOCG3wvuGtc3xZVvphpd5040RH5byK_WRBO9zmG5j6rIjLTs80xbXxFZV6hd7EYXaQbeFQiuxDqpswzYTrYmTzzJoreANZ684n64k5KE-xPXGrdex0ZL6V8urFON_NRlc4AqaQnH_-CmGWlsJNiQbTw7DTYn5eVGMpofhI7sB_j-VsT-DA0dcH2EbSHazwVntQv27SEkkBVmqtfIHi1mMeeLV5WYhYiaQY0wBlzalXCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتقاد دوباره پیروزقربانی از کادرفنی تیم ملی: من با تیم آلومینیوم تیم ملی ازبکستان رو میبردم. با احترام به کادر فنی اگه سرمربی تیم عوض نشود در جام‌ملت‌هانهایتا ازمرحله گروهی صعود خواهند کرد و دراولین‌مسابقه مرحله‌حذفی حذف خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30744" target="_blank">📅 17:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4OJ69h5U5YD6VjC2sK2XvP8ohB0LE7RxkASFlrVsskXQPIgHLzG4UZxzHoYD65L4ePtiC5S424_NRMD81UBVkaq-WIiBuScUSxCFkEK3N2fdEsIeaiXATSnFF9dT0WHDxc9Vh3t1vQG4mOoztTgPYCgU8J-hVJ0fWB2M8bvKAMqpy5fBypgErFTglkrdN_C6b560I0HHe_XEhUNv0_I9ClHEwjNb-TWRV9sIEpUAGGurQGdKQs-TAEaGGzLH1fVteAAEcjCtAcf2e8V4pu7YOQPJlwTeg1mgxzAshIvVPVyahA6Q7Dw_EbXJM4qPC16yChw5FwmaHxeAaEFgF3LSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داوید نرس ستاره ناپولی:
وقتی خیلی جوون بودم تو زادگاهم 2 تا دختر بودن مسخره‌ام میکردن. پنج سال بعدش وقتی به چیزی که الان هستم تبدیل شدم برگشتم زادگاهم و هردوتاشون‌روبردم‌یه‌اتاق تو هتل 5 ستاره. بهشون گفتم باید برم دستشویی، بعد کلید ماشینمو برداشتم و بدون اینکه پول اتاق‌ها رو بدم سریعات برگشتم خونه تا کونشون پاره شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30743" target="_blank">📅 17:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZr7jp2KM4dQuzT9c7NRN2SYmQvKKevGf3tENlKJvRwphT71xZ8oG97XGNmojW-S_7cS92NKMVmkTCF6IOXqJAL1K03r7kuzdRjfLDCK_yp0l9KUSL-fZxSdC-Njfgk7uhwPe-4U6_L_9krZrfaiP8jo7swIepst9CRGlgE-X4yb0pER1FRJWprV1wcstjEbG2Gz49beF5maxxUQkQKkrBB1MlFM94B0yxX2pjlxsoaNRT97Z2TjYWjtZniIWuemhREuTZydlVXbY1INbqaXaHGGtwD-ifhsN2uI_Q3LqjOX1LOvG4-mC5c9Qndvc98AknyUK0xSpHv14E3jLkpIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علاوه بر مهدی‌ترابی؛
مهدی هاشم نژاد ستاره جوان تراکتور نیز به‌دلیل‌مصدومیت دیدار هفته آینده با استقلال در هفته هشتم لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30742" target="_blank">📅 17:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGpjxCwhxoaDCx056qs3B5Rs5ZwHxw0pPONunYvm3KA1IXPyd0LHK4kXnt9Rn---bVi6i4uC12bU3TiKUEDFhuJiHXRmrINxiFv4t6bhG7g3le-D-hLCUtLqE9k5LthDxD4976lGRRCtR3FIzdUpuX6THJOkqo9ERJNK0_irvQVHxwuFEBcKcwyC0PE4yJOzQp3ghv5LwN3SqeUBYnpigw_mU2h5KJgjUde65wL-Q6AUh03Q1jaWkdtE1yVfIAxbueIYxbnl_ZooXtOeKJbIcmJP12Ffgbh6cqzOUuNYoU_JsRFSmtJVSAJVTuN_mIGcLu9-hFiZ_qhEUVhR5bMz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
لیگ‌جزیره هم ازباشگاه‌منچسترسیتی بابت تخلفاتی‌که انجام داده شکایت کرده و احتمال گرفتن جام‌ها از باشگاه منچستر سیتی و سقوط این تیم به دسته‌های پایین تر بشدت قوت گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30741" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipgCBOn-RZUqBdDt13TluNS-21hfEgG9V73WVblBEqEgLTPtvUVazSjhZ1WXtfyC2o7UWCRwEszZFTTQnQLxmqlXLYdqv1DrCwiAUxgTB-HZ47xcheHiHLGzl6SItRP9PaERsaL0XoeYwgXN3tvc-vSWg0BAtjdcXwv63FoIcWsG0nzmglULjZbAnSpSpRJ7PtiV3ziOv66R2jGWiKbhZBuzUfkGyZPA3dlL_7iBRW_cqwa8JEZ0plAnu-6iuhBEeFMPJx1Sqc6yhCWdp26NFZgJkbMQwbKxmBR2XgHqaZ4Ayn-CuqnSFgwjV87lDotDXg2SaQmEUNnt2vL3g-UY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30739" target="_blank">📅 16:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
#تکمیلی؛ طعنه عادل فردوسی پور به بالا رفتن عجیب و غریب قیمت دلار به عدد 245 هزار تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30738" target="_blank">📅 16:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb8jkgRHn3qJIgmJW8ldXCSsTjnSLhFdQBLg8L2plJ_aKzK_pwjoufqXMCBCmB3NsELLy6KkIf9MzJOPvnHA9S1wO3RaNBiLm3vXGieEQ-k8485azYzDDiMrWJ1h3Ru8wI_HSjH0wn7xWPOXsjSrMHJ1XYFVzn9EWFjlLp3FVR20JL_uWaV08tVWSzvonN_yR0zjRahq9OIqzK18MPd6KL6L_kVdeX4VBUS5CZvFgYmTk5oh2RCvbN1hs3MNWB8l1dNFEqqFY0ctnm5GxxPCNLUF3kgY3-k-du6JVxnAxYBv4mFetgjuMfl76zGEvbtwMU4IFnIVgT-XW9aSvv8sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
نشریه‌مارکا:رائول‌آسنسیو مدافع رئال مادرید ساق پای راست مصدوم خود را به تیغ جراحان سپرد و حدود سه ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30737" target="_blank">📅 16:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
کی فکرش رو میکرد که نکات فنی مهدی طارمی دررختکن تیم‌ملی یه‌روز به مدال قایقرانی ختم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30736" target="_blank">📅 15:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsEv9A-OjNiXxgsRDX--KDK8alwFWn7Pq0HZWJoAjgmjh15P36jJOAHS3cy14CyRgf47EmARJNpfYcLtYRJqtQOG3ns1pyib41AyjdNjEmNuHghP5Z0EcGtsllkW4otu9_RkHf1ywLBGCVh4kzuuxKUi9X3orsrImIzHtnDG0HpMAtDaGbhjsUrLrXCEYnPWj5W7K4DN0F-32HlqGIuYBR0g6DkDhZrVn1zHSvIVwq4OD6dcbpS-45AXq60qknBwBeNytd_oVmnKFjfUzK8YC2OOn8KHvFsT_VJ07ErsZ9CES2LrltEUJ8QSkDr--GZG5r4_cpB-AQnxLqQU6VF7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxpPKrm7XMbx03LIoApLg2C4Zw8FQBE3fEwNABbWBlS-rR6y6vxgG83CrmAtwhSr3-ukvCfMfND8xg7mh7nodgyZx9r9HXXSfouB6OZmQwMBWAn5Feh87E-tO1qUnt8SAZDSSc-Lg0KiQTvZNfrawAvlyQsko5fI4az0GAdIUzszpWZLgARbrK_0B1NUx9g3ZvVgQFjAHt4ZcYUboa9kzpJD05GLMGvn227LaQnxrb9B_1Dt19rFk5KPNeMp9tszZvSNFFi7bV8oHMqVatZDcS1WvaVg-FPjbStCLR-Ew6BkwztUv2Fzdiq5Qud4664AsZsAab1ACuOso4FKJP1ggw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز ستاره تیم ملی برزیل برای درمان مصدومیت‌اش اردوی تیم‌ملی برزیل رو ترک کرد و به بارسلون برگشت. مصدومیت رافینیا حاد نیست و بعد از فیفادی به تمرینات بارسلونا بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30734" target="_blank">📅 15:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVyn62i5eAaa-VeopKnDdq8fZsVO-VeFvuyqTauhylPY36Fug6-DKO1gy-16ejVF9DD30G_5FzM3BTyNqgLdE8Pi0sSXG10WdZFYnslV5oY1fvI4ZoUDZyGkYpwMMSZsM6aw9nNDEN8U8tY8XC0-0C2Q4ctkwDuU0k5vf-jdHNh1rHxA5Fsn4z2oaw6Bcvg8uR6_9ajObTvuva8s17-18gpapKOopuEYg9yn1gFe61HWIE01cvcQKi4ki3iDqX7qfa7fFlCso3FjGhVisIHYkAr7FM_bXS9j0L1yaCD3kY69SxzFz-qRNlcS1_D-9uQ2jcH1Ez9p3jgYIVR4MavmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30733" target="_blank">📅 15:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqoBbNgIp-0sTv20OW7HxyG2yDYwEnBGMXOboIkexVz4KDRMaXUQ6wJXXUzB2-sGRIMPIAt8dOLjKwVdwG0mk9KdXICb9QbolvttrW5EL-YYM8Vm4vjYqqTSMiFUPZTlq6K3lHHPhnOOMLqfnJAF1COOeVy96vCJ8ancNs071tEAlUZoFhCvD-ASqo-RLP__gxycuN9c75I076UESba3ZEaeAu0qGTmE9ewil_cdo-G3ahcme7eDtyZcM2IIrlGbnKKNS2a-46DVArPzypfnD2Id6bTasj1ivLI4GxUIOZggW76Vy-PcBtOzh37eeV6l7pNJBb3tXuiP6DB_lBhzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30732" target="_blank">📅 14:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltVwAogPTFKRX3HvvDoqEazc75__JrTRfXk_gHLSr9bZ7bXammgiWCtQXbQiaNYr_G02U9Z2MaIUERhZCbtrMQ5qau6GjZIRmsMPSuWt4KVUbDhQweviwlvZXzCqupLRO2zsKmZY70p9klJ-kwmbu62JGAD3_RpOo_hw0X3928y9kEh-ZCkomuwfLg7nF8PmLR65Ere87cfIMwUkmVzMyGpZzyXNNPkcAdHQfJBT_SDwi8c-x3PXUTi9ulEd-LSj6Q4bziOVAwFTzyATmsa7tUrLmCMM4bQBR_cSc_q0NmRPSczm6JgHb5PylVNl_FJOMu-lYVHDoNmby78rcsod_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
کول پالمر ستاره اسپانیایی و انگلیسی بارسا و چلسی در کریرشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30731" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luxBqxSX_zXmpqI1LWOgDb1WHCxXEs0IwGbK1e3367mo5atX_X-LLJlH26-rL6gRehNCTVO7jvVMC7A7aHnxYHYShX9ZlDH5qA155sW90pCIjYGWVF3paSNPt3og7G2Vh4siimZukp-2_RL7-6z99weKfZyzcBewCiwzFbn_ca1SXAIeViUJ4bls1GUT1tpVaR0FP2x5iEPzT4z32kMm3W7fezN0vLkTenyMNxycQ0u3aNi08wKBXgFeni-U8-LHE9auLvejREw3yxUp9Wtb8m7A9POBeKoNJCt7GMHKfXV5Xlq5ggQ_VJHFpRbtHYHkGhAkSM4RXvZFA7uCjQkjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون: در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30730" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYtRT2mPaMzOBKxfa6n38b0Y4QZbZeVb9sd0uy7Ysq8sjKccYVOUlVeTke_VDKcmyJUMVoudDQ8b-zHBBgwfVSm99JqFgYqVeZQ6HCYHY47bxmV2zPuLYuy1chAxO2FBNTJ9LAJS_ay_A_fDqD_HULL6_C4lj2tg3KabMImpVD2QMwxsClaNNckaS21mT8Thh5ok-sbIK55FVT1J5O_ihspJwwAN-2W24IEKyi7iExIo8mXZRutpBrtcGzPqzPuMuZRBQavF5DngA1Wd0wpVhac_F0VFQ-s8DH3tMZYKm2_377TUVnobxALg_GFHHpBYIG5hZFB87200fGZk-A5lWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون:
در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30729" target="_blank">📅 13:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqHsaRVof-oYh1wefpniPDxmgBlnqSO72olhOLDKRhpJvi5HDX8mvzVsl2_ttvwUM5-iQbNRVbTGYkHT7--VlSUTx5pmjx7mTTvDYNH6tXE5xww4JIoz6smFz_Kl1gheYW7B6IqPFdDlDthCAFsg3k4rRx6I2y7DbqnO17aA_YnhWS0nhmVETInZgGuhAns3YHgIeurCjcQGob74vgmVuFE33WzPmVLcavhLipXylGnlhIXBwyOndwP4ulE26x31_9jB-xScjix0_fbYhHa0MDIeu9cv-cZ-Y-ITW-pvLcQo_MafG17J0PcLH1NSDFoYIGNTN6zrdmLM9YoYW_PfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30728" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRRq3_kdHpwzN_qFqPAQg5Pxg4MnjGLXgpAHXODaPRqu-DBhiMqnetn92krl0tLhoLMyyb-d57ODSGC5MqcMZKyTgFuN-6uq7iKdKlOqpkW1wxn6_sZlVjMkp0ck88APOB34BtfMb6pYnLfCmsQqqsZTWsqoexFIft0y5oypObCeZbz7MswdWQGJLOcUSJkPIodkCLmpBhrE0XcdLuHxYk1SZnjvnOBNXtfVcywwFh0wR2G-dqa7HAZcrJok8YMAYDCzhOQMUiqbVQbBSMRLtw8J07DpvOmxfal1JAT5ogzXlJAYB8G0xGWH-UYK8FhHf_hdo0_KNtxYGwwRDUrN5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لئونورملکه‌آینده‌اسپانیا:امیدوارم یامال برنده توپ طلا شود. او لیاقت این جایزه ارزشمند رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30727" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPlSc7r1-ojEwSuChWcBv-Jgu-hoRa848UQzXhMnPnfcynU45Tq8mY3YCwv1LoMjPOxx9ye2PL4_GWrQVgM4H-Uw4HysIP6Fouq3wn725g2lnk2HJL2DAPbnaffmoVkCH_RZzYUYtzGxgtG57LpAWjW83zqgs-d7xVRUgqQ3oF-VTfpMJ7vDFh_ABPULo70aXTrygy0DLyaax1ULlWxTdhz8eHPwnYfyOKDhpenRQ1japC3kt3mYMBp_Gawo-R05nOuEV12EUW260VnLH-92Sdx43zH9fowBC_b1ElM6y8zPYguoBQwLkz_eyp0UMxx6rUEsq_IZ5g1-ZsIPYRQIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30726" target="_blank">📅 12:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=k5IRC0TWOZFsiM7YLsQ3BQzC9r_bDWstAluKEmzNa-2Q_qQkRcpJ6r63UNNBmPUOBN4IUzJsI09MupDl5jzO_hvhGm5TbVWywqy-jcu6z30uXqcLuKr_28joovOS0unZTCwCe8PXWnvEaA84kWTlQzazqsmYBFpwPFw2IAVG42OhXt7OrtagsQi0nOmKKEZhNXYIT8OZcEtb919B1AqvLtqgLcv-IqR2ndorcHxRpDwfY7z8_uksuoUFQ3arYPlFeYTAb0j7FXvz6Ojxgkq5G7fxpfXCKxsZUl0WR2SppbxASb_Zt7Ix2fdZQ2rIwd1pBII51SN49P2i06UjJ5aXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=k5IRC0TWOZFsiM7YLsQ3BQzC9r_bDWstAluKEmzNa-2Q_qQkRcpJ6r63UNNBmPUOBN4IUzJsI09MupDl5jzO_hvhGm5TbVWywqy-jcu6z30uXqcLuKr_28joovOS0unZTCwCe8PXWnvEaA84kWTlQzazqsmYBFpwPFw2IAVG42OhXt7OrtagsQi0nOmKKEZhNXYIT8OZcEtb919B1AqvLtqgLcv-IqR2ndorcHxRpDwfY7z8_uksuoUFQ3arYPlFeYTAb0j7FXvz6Ojxgkq5G7fxpfXCKxsZUl0WR2SppbxASb_Zt7Ix2fdZQ2rIwd1pBII51SN49P2i06UjJ5aXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیرتولید محتوای شبکه تماشا: درپایان سریال امپراطور دریا؛ باتوجه به‌درخواست‌های مخاطبان بار دیگر سریال پرطرفدار جومونگ پخش خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30725" target="_blank">📅 12:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30724">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mutLJEf0m9QjbhOg8WnpI_Ekgq1uiNXdJAPq-YBCtxJt0vRSjDi7ErEqkk2-SvaYlvrCP4o47HXen7ryaClqRkypNKRi8xB3bfGPK-px8wefrWGh5vN7ke0VU0JLug_r__aHJMR1coAe2THu4DhxcbG9Ep8adPKSPkukw2Sq8d40kzkpo-p1-Fna0Y3neI5EKk9IwdunfYqdbbZo_5GpYY62b2CQATDlqk75AqlOdzFair0s8XqX4cPKstR2z2vW-JH7ahr_fLpADHX1T-ajnsrpNV5pBJfYfGnX42yLsMRWW5Plw5dEgThj8tDubaVFu0l8nHgMGv6dwpgEy5fElw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛
محمد حسین کنعانی زادگان کاپیتان 32 ساله پرسپولیس از طریق ایجنتش آمادگی خود را برای تمدید قراردادش باتیم پرسپولیس درنیم فصل به مدت دو فصل اعلام کرده. قرارداد کنعانی در پایان فصل به پایان میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30724" target="_blank">📅 12:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30722">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=cmpZg3ECrL_zMbnuOgTdOi9GSzDuOTwkZcEcBpSo5JSbvmEdAEdxZ0FM9hvaq9n6DYOd112M4mOEbQNLrsrRQX4XgT64vGUwAfnGMLefSclxY9JFqeeh3Xd24u4PE9QfXSLo587c94ZoRqrfyVxnFteEv9PgtT3kF8ly77BnCmVpfhcBJqTgRt2Af-0ViZ8tUKHnW0LEcAgB9fibFzzqPqPdFaIx2GWm-z9hWvxQNKU-ia7kaqjYZnSE3q8x3mLRIzCfUMM9KHBIFg-buxH3I5X-xALxxHhjX6S7tH9CqcxJo1PlBMk8_tQ8zP8KUPNKq38JuxV74xm2UodUMAN8Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=cmpZg3ECrL_zMbnuOgTdOi9GSzDuOTwkZcEcBpSo5JSbvmEdAEdxZ0FM9hvaq9n6DYOd112M4mOEbQNLrsrRQX4XgT64vGUwAfnGMLefSclxY9JFqeeh3Xd24u4PE9QfXSLo587c94ZoRqrfyVxnFteEv9PgtT3kF8ly77BnCmVpfhcBJqTgRt2Af-0ViZ8tUKHnW0LEcAgB9fibFzzqPqPdFaIx2GWm-z9hWvxQNKU-ia7kaqjYZnSE3q8x3mLRIzCfUMM9KHBIFg-buxH3I5X-xALxxHhjX6S7tH9CqcxJo1PlBMk8_tQ8zP8KUPNKq38JuxV74xm2UodUMAN8Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30722" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkeBKGcr1Vv3drMKxeYatlC82LLtIo3vMqkwYLNKX257ceTMjl0XnxHgYlt8hH81ydr8JpHNP_vHvc_BWBTrgbubza2tYsMoFj8OD1HHw6TAaKv63Bi5BZqzEAZIv9bSY0XnjKFMY4iUqBOWHUIyJlSUjXZIAzZsahXYCqUI5D2rHhGIJRjdMwxhNZgDv5PMUn4Elnw-WfR-oXF-62XJyX1mJgF-sX_CF0VpphsuSJ_8-TDHjMyCv2XYSFd13m_UnDzfHOzhx6P8yunIcCHNaeyAGERRxI5KSKtt7GKXjLgB6P2nQwq1RiduUads3PnSu30PWQLVTQpMAEQmiBsn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30721" target="_blank">📅 11:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30720">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjxbFKaMzF_Riim9KIBmJwKdv77g2XtVzsQxBmxGgP4Gsyn5nrPvhFO4zd58SM3fjQBE6iYcOhyroHpWkYlhza6GA8ZHLRzFLCbAL5-v6ZVaQMHfOPPzCpN2qMa969fCJ-2KFKJu37VThMj1kbdcsym4EHdPkv6dy4Hk8HfP4RiAN4hOaCLtSLI4R28iBogLzH5mYcReh9PW4jKAAoxeIkVkZU-DHhx72e398KDQzIgmceOvo8zbnnakjskH5IpvmBIOEkTGnUqHkfxaLDIXrJ26gh9KzC-U5V3F0NdH1wScLE61Gds5FKRYaxAeFwKwaYuyntSerr35D-mOyC9yzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
تیم‌ملی‌برزیل امروز ظهر در دیداری دوستانه بمصاف تیم ملی استرالیا رفت که در پایان به تساوی یک‌بریک رسید. رافینیا در واپسین دقایق بازی با یک پاس‌گل دیدنی مانع شکست سلسائو دراین‌بازی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30720" target="_blank">📅 11:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30719">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liA25XHwgBtIa-RRpkgjzUOQ8KxTZHMVz4wY1U_7AzBNBfPTbjl7oKbtvT7T_KCNQnodZpNVlgwrfF-dWnEuhgfiuo5BAw_ivxQAv3d9IPUcG-pWFOdqQmGQ4UX7bu1Pu4Hg1G2mDG5ViXdhgGQawlxs5oeSMkCsaJCJJW4l0EDlvi6t8n2_ZIMX4tpFjjLdhFRM7ir6QkAHl0vmdFNJ9z6BU5Gf7Jhj3zpgM3N-p8WjASkSsoHEZvDPqR_VdVdg-CmZIC0-UJ_paWkvlg3cqIQqQ1Nq1RVum0h6FnvFu28skWhH4MvZhbdIhsmlU_h8iI7hi5ZAIhCKamW7Dp2FRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با حکم فیفا؛ باشگاه استقلال محکوم به پرداخت مبلغ 30هزاردلار به مسعود جوما مهاجم کنیایی سابق خود شد. آبی‌ها 40 روز فرصت دارند تا این رقم رو پرداخت کنند و پرونده او در فیفا بسته شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30719" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30718">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDMf5vT4tIo5ArYuG3n4UBfyWpAYyXa3Fy-diUXNJ8J29hPlngIb6Mjw5ALrr8RO8ll46ufBxJMMU5jgK3kQajiM3xlLJiqnYsvRcsg0rq6J9uCm6Kg2cZcZQJVgJF1cbXFfVZnNFF0ECXR5cnDzF6zhr5ofkEdOgOUfvRZbzdOD9R5iUPehTg9iazYatCRp-Potw5ygAx3tA-NB7AxynC8LsTBJXElS2ouC1MG8V-99vW82E21iMSo7wvCtQ_ROsdyEPZO44eIiW1dyF9DO8nxBnGUuPqofZTVICXQCj5ca5heOBlNgby5lnWXPQKxSHnjZOtkDTUi2rJ5hRRkw9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد اسفناک تیم قلعه‌نویی مقابل 50 تیم برتر رنکینگ بندی فیفا؛ هفت مسابقه و تنها یک پیروزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30718" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#آپدیت
اپلیکیشن بدون فیلتر(WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
✅
سالها فعالیت در رده بین‌المللی
✨
ویپاری
🎁
نسل مدرن شرطبندی
😮‍💨
پاداش‌
100درصدی
اولین واریز</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30717" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30716">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pm8dIDzJfRIZbggKzAy8Lh0bGbTSu3Yv-3nXLU3zlFBayix5cHWWDoRq1cJUhX76bUUoVuSC7BrkEYuZLL7dtdXIkUifcqEp4GYLJW1uuW5vJCSlfb2-fhmCxLT0lYwrSUamVzu1YSQcaT8BOU1D9naDW7MiKAtIVPe5qvG9cP89-VT9aj3e4nUvr238UO7eXaz58NYGWVwkkyTQQfAzLlrlbKj9s1LtJzvuX6hMY6GOTYjmr4t1KicYw8SyumXURBy23cpeBvK0TBdIgMjeOtdhUJ1JVseEfNCkLvfNkxZkF4TDFsMTyCyFR3AJQVtJM44IR3opfF4as7dGStYNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
میدونی چرا حرفه‌ای ها سایت ویپاری رو برای پیش بینی انتخاب میکنن؟!
🎁
┅━━━━━━━━━━━
✅
4بونس روی چهار واریز اولت(به ترتیب ۱۰۰٪ ۱۰۰٪ ۷۵٪ و ۵۰٪) هیچ سایتی همچین بونسی بهتون نمیده
🍷
برداشت زیر 2 دقیقه بدون احراز هویت
😃
درگاه شارژ ریالی پیک پی
⚡
تا 25% کش بک هفتگی
⚡
هر شنبه 100% پاداش واریز
⚡
هر دوشنبه 50% بونس واریز
⚡
باز پرداخت 100% شرط های اکسپرس
✔️
بونس 1500یورو + 150 اسپین رایگان کازینو
🔵
لینک ورود به سایت(با وی-پی-ان)
🔽
🌐
www.wepari.com
🌐
www.wepari.com</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30716" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmO2gfxFktnFzUEwwvZfEpB347iyo4iTTQnvTHfg4I0oGhbnsP7aElTN5gRuLU54hvVDFyuAfmN2TuW5j3VB4I_ryWE8l6YAMYq-lmasgdiN3a_GVBNIvdzaZstQ7BlplfJcGgAhqdSwcLdQnI4jijMWT_E0wjFjYtydublDPRDKTNJcAJF8-wSS_ppvF4BO9kTc4JRiwtZcIrdfxZRF7okEJdiu455ngZvOLgQ6qXsYvA4rK8PWqI4VfrrjXY4ARneMhAJ6wivYtmMnLw8XwojRoTwvYYHio1_CLe-Zhy-ug65JqBkxApzUOC9AWH2ih95yyUVSOmb99smCG1USaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30715" target="_blank">📅 10:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6-1LbbM4LDMu0YhzH9q_6jzHar6-bNa0ohbALyBQCFA-sqmZjw7Gdfs17jFYUR7WXqyv8c2Fh7X6zm8cJ2LXmJa6WIdfldI2qv40T-Zj4UF5a0HC4YXltEJfv8a14Ce8Io3ixLUzQCbhjjBeVdWIeiP91ubBVJfgjkDQsyNqgwuVHNg1Ru-UvGf0-dtXsW3SEeAMGx2Rkvh9QQPLJqGa8GGxgSQQg8BP-hekIV9D-vQs7AZ-6xhD0lEAyS45K4IDqvCsQgMQoZkaVfuN6p8g3lSiupoLy28Z6H9fvaGdBMxHlEmhRRihPUpKJ8YrUsyKTfUlMozLx8lJulFYHFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30714" target="_blank">📅 09:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=vQTlp2BlI83Otd2Rmvhrvwrtonj-6toNnqZt_MQ0YhHdNBWj-BOsY0ZtkSDD_wC5XlwV3mxft_XmZ21dCwOSikViQMFpZzp2wGoLZ6-PUIzopA0bmMCjfpBD5OyESjCyOjhSAMM5XxzgrBm-cASwGMiezCOmPfr1sbEe1FoANTUtv7Ia7ibtcpvGylE9OSttanFcXFesNXN4GwxoosBGrxRFQLECsIb_nS0hmSlzyAzLySwR0Q8UDupYCfJ00vhvFiHGmr15SBUatbG8EWCFt-qu-9C9VpmzAf80CVmk3Hk4KtxBgluld0neSvAolAr-qGzyXKK7Cr2wOAuOmL-xWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=vQTlp2BlI83Otd2Rmvhrvwrtonj-6toNnqZt_MQ0YhHdNBWj-BOsY0ZtkSDD_wC5XlwV3mxft_XmZ21dCwOSikViQMFpZzp2wGoLZ6-PUIzopA0bmMCjfpBD5OyESjCyOjhSAMM5XxzgrBm-cASwGMiezCOmPfr1sbEe1FoANTUtv7Ia7ibtcpvGylE9OSttanFcXFesNXN4GwxoosBGrxRFQLECsIb_nS0hmSlzyAzLySwR0Q8UDupYCfJ00vhvFiHGmr15SBUatbG8EWCFt-qu-9C9VpmzAf80CVmk3Hk4KtxBgluld0neSvAolAr-qGzyXKK7Cr2wOAuOmL-xWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟! دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30713" target="_blank">📅 09:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=B_nTl5JbUdD84BIgUtZDg3SK0mSk6jqshFq53I90lV_mlWA-vpUaeKpdd25-X5UHK0GUqnNftBySPApXEWWgHTL24laEqwCCgcccRjBvY9zGC8br1SKkRA9E5TSWyiXImsq5lEkqppoImpXaEV4s9ousfuYNbiKkMJVfO-5D7BnzTC5XDgeIdnYtSe6b8FBekNABEQxSYlmEFo3AYwNKXhmDli1TaFGLpMn5rOTcK7cor8sPwnzinH--2lSDAFSibvNrNNq4fQqHJB1OMAUAE2bMfxTYJrZoxixsL16o9ygia7WRuLwaNBBwXvRtcPlAPFG4KjKGpxNp1E2auf3TLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=B_nTl5JbUdD84BIgUtZDg3SK0mSk6jqshFq53I90lV_mlWA-vpUaeKpdd25-X5UHK0GUqnNftBySPApXEWWgHTL24laEqwCCgcccRjBvY9zGC8br1SKkRA9E5TSWyiXImsq5lEkqppoImpXaEV4s9ousfuYNbiKkMJVfO-5D7BnzTC5XDgeIdnYtSe6b8FBekNABEQxSYlmEFo3AYwNKXhmDli1TaFGLpMn5rOTcK7cor8sPwnzinH--2lSDAFSibvNrNNq4fQqHJB1OMAUAE2bMfxTYJrZoxixsL16o9ygia7WRuLwaNBBwXvRtcPlAPFG4KjKGpxNp1E2auf3TLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟!
دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30712" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lglgnfo8_-hTHwSyCQDKHkB9evZ0j619-pRXetTyGE7EwGpxuFU8X4xtB9KDmHBUA1Hw-CqM20gSIp-1fuMv-5qNoEtaN70G09IO6xo5ozyvJi4sX7MB8L8GqpHQBRT9f0fYdXtQvXBvcmrDzUxatmpjjDAKiyyFxhLGy7QDShsJPuTbNZiaMC3qd2G4jol-yv0WEsMWbhrH1-UMw0V8srqsoLpkz4R-nxRXmELB-CQq7202jJT5LexLiZWvVszkWgjbBQEqX9DHpY_6rWTD3IVjFTz6T5Uo2q3-98MDNUGYyfEcquTf0lMEhV3H1Pc5ayUJrDKpZ0k0VfuWS7TNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف تدارکاتی شاگردان مائوریسیو پوچتینو با تیم ملی شیلی در سن‌دیگو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30710" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKGn3i9f_KFRjmXF61vnaTErYGW3LuhGXiZ16EDxqpxlAH7_9o6p176s2DNxL-GmWd2fQs9c2YYgo29OW9tMzFut_yEWS7rJxDv_NvZd8UrF8GHKP3BZETcCbirs1PH1sA0YiinxxjQbhIvwcS1K4B-PSw_eCvcsIjomONOZVxpGB8Kh3qtcpzYsF2m9XNHUWuKOSETDBa0J73pIYXyakCeiYr3p0QomlwbI5MwM4sBswEDg8UU3lullXqzyGFVSwMt0wdVnOu6mS98OFDyVgd4VpllxBm3LlZsfIVxrRGrqBaLVEPJ-Xymak_O-0r4eHFiM73KJRKetjdccezutGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برد پرگل ماتادور‌ها با درخشش یامال و دومین‌باخت پیاپی تیم قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30709" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4ZZ4XIhLhBYFY58SQ2OZI03eCLz1tuWAokr3Ubh_-_31eSmNoUlNe1F2DLRe18c1mc3-TljSBikkHyK76OoodJfy2tmW4JYEMZ3VY2zy0NP05O55OzsmSnVsedSfvP7QwCRLd6cdJQ_O5wK2swJtG_woIspv5CM6HBOVIYGs-pTMngBFPp1ZdNUpHar9Ha_l66j5qLogCODpNJ9ekXrJjYd0DfS1Sdk3uIgJ0GglySDKKGezi2DxbZJurxiP53oNR5s0hcpLIuCcxBiLRxa6HSAabLaoS957uJntAWa21WStl0GEE_BzVQ_K8uLKI0U6qOJnDxQ3Ag6QtfgK8cWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج مسابقات تیم‌های آسیایی روز اول و دوم فیفادی مهرماه؛ ایران بزرگ‌ترین ناکام این فیفادی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30708" target="_blank">📅 01:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppI6OlcmKNYfvm5w4Qfn4Plg23MTDRNmUkXz2Afp7beDOKDQ6GK7SqZQO3-kFBMTqPigsC66c0ECcZWaFKPTRZO_Vp7Ug9r6BNxphT_4CelU5zNFxy-qCDbKpW7Ye-fPKeozBozht7TRgeczM7omclZvthoMQQ8x8qFXGx8udSRnm16OfLELbphMGA8tAVPE7iLIDJlpkyFIdrpLrSOTke_c-5vDCZlADQebILbDUcLVih7Io_0Fwypftupt0hD78AhAulxlSjwl5eYPqNbCB4wdt1CeOAIoLW4lqzcy50PpTcUSfrYHGVsZEB8pwNUKv-GpMllP63rOrjwi6g3SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30707" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFJB2ZZMEaXQ-33ZoSWJ3QWObj74_ltdnMe8OZIxvkWbaw8FzVlTWMQzcth3W92cVriKjOhuNRumKiJDpU_aDNAfNSBZs4bhGP9VNMVrdSOH0ETwoG-6RRgwY50owlrqugy3aifrlYzXCTjXvaeoKMt234L93cQ1FU6A6whAgg5zc4Vduju0EBb7y17EblqHN08Nx8e_aCgg46V4o2jKg9LRtJKoS-Kv2_jNr5xj_Zgo2mtsprLlPzSFWt3KiPrMTWRw1vctwbg4pwurMGpo8wDA5DsXdgaHp31ZxG3SaDwH7zLbb0E1VE6kfOd-wiBJ9YQ10GaRMvvYeTKUdvnI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با شکست امشب تیم ملی مقابل روسیه؛ پروژه اخراج امیر قلعه نویی از هدایت تیم ملی آغاز شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30706" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30704">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6W0UnzO2O6LHFpMeQl7ajG91_nwYC1vd5MWI90nNHDc4T2gpcXzfWRnBkdyAzCLNUL2x2iYkMoq9WcQKz0sAFm0a75B3d-V-9KibjNCenWdD-ypQwA2woJMpNN7Ud7dPFA4nvHY4l0kNBSOKav2i5wyfNZ2_vVn0AsL8IIz3PV1XWwRU2U5Mc-XJ4bz4xREcrlReImd2fqnOMzuotndyOc5Quod1QZaEj-ErmcV6IM94M_qHCk4bit2865cN-LGA0P4Hq0llrR_aGYZK26lmAUuWz2eJpSAwznIHkDNS3mYDX69Q-4SpwxH8x4qNT8dgh5bicGFLd1nTb4HfVIKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ طبق شنیده‌ها؛ فرهاد مجیدی اگه اوکی رو به فدراسیون بده حتی ممکنه در جام ملت های آسیا رو نیمکت تیم ملی باشه چون تاج بشدت دنبال اینه اون رو بیاره سرمربی تیم ملی بکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30704" target="_blank">📅 00:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30703">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های اروپا؛ پیروزی ارزشمند سه شیرها مقابل جمهوری چک و آتش بازی تماشایی شاگردان دلافوئینته مقابل یاران لوکا مودریچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30703" target="_blank">📅 00:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30702">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reMhfRjhqSMrxyVkIKuzNiD2WBKCs7Z37s2co0NDtx0yfAgqD41krEMcnt2R88TwZ6_AI7iQxxyB2oqT60xvV-OD9Pm9eGH9t5Ic39hoMilIk02aPwipZWtF4r0RUJuH5I7RY9EBol4tLiSkHJPyTi0rRdGCk6HrIlMaUX6-0xAk65-4uiO7dhcyD3knoQNenPucA3jKbb1uJyFKXKwmE5X12Z4gadn3fYUXaOYzi4Eq-ZfyaKVbObfG792wievC5tjoEWHvs2D9FkdhfIkqAY93Zf3Ma9z2o8KfbxLauiu7-YemayRBuUnyfQwAKlZ_EgYZX_GPSqEOzVOtQC-GnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30702" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c014a889.mp4?token=M5mkx-C_8LkOW2WCMsc8ykJh9tFn7OBPK1Hqd6LWpMBfr93q_7dJxXtShaYRPOhSaRfInBGpzghC6VvDc_5ZRrNnjHGdRU_RCQW6STdDoKNYtVKutR6_5eBqNBy0ItbaY2Z2XaDftcyp34ruYeAP_evoW3PgH8D12FYIkF5H5PeSMFJtsvBhNL3za00a1oKWBdUAtmKu3hCmCKzKY0udH87uLzyqlPO19g55NV0u6APuuzgeV39IzTYRoY_tciIlnFSArUPS3GijYIj3zWExOjl7Fzbo6i-TdTNivweV3OfE-7FJMRD9F-sI7ihWPZLCa5pWrew7Ozc4TZ-7NY81JCc6WdqY0SU1AEjR3gAAr5WrRViEGYQ4Na9wyhUbODSeOucWEpNI0V_GPdcdZu15QeaXtKV4iWytQYyv3aqYs8TW8T3S8JiiTQagcIFPLP42-cixPbH1Obvq-AwWnP6Rs017g-bGt5qSGgP7VMCGPAVaHMLXQ3UKvCWxFGm-AKmKEm0zCcTdeXEyZmVIz-uxc9p1DOzuAulEV86TJQKjByk4LezCNHKpU_CVbX4wZXQJyHgvNT4t1_uH30AJCLKB5m2msJ7Qtm7zhFl490jUUmVsdkdBZbW5tS7GgMTTHtOArjuNRYeCHu5VCPv1ASoRxBv40St2g_oqI76DnqOw7MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c014a889.mp4?token=M5mkx-C_8LkOW2WCMsc8ykJh9tFn7OBPK1Hqd6LWpMBfr93q_7dJxXtShaYRPOhSaRfInBGpzghC6VvDc_5ZRrNnjHGdRU_RCQW6STdDoKNYtVKutR6_5eBqNBy0ItbaY2Z2XaDftcyp34ruYeAP_evoW3PgH8D12FYIkF5H5PeSMFJtsvBhNL3za00a1oKWBdUAtmKu3hCmCKzKY0udH87uLzyqlPO19g55NV0u6APuuzgeV39IzTYRoY_tciIlnFSArUPS3GijYIj3zWExOjl7Fzbo6i-TdTNivweV3OfE-7FJMRD9F-sI7ihWPZLCa5pWrew7Ozc4TZ-7NY81JCc6WdqY0SU1AEjR3gAAr5WrRViEGYQ4Na9wyhUbODSeOucWEpNI0V_GPdcdZu15QeaXtKV4iWytQYyv3aqYs8TW8T3S8JiiTQagcIFPLP42-cixPbH1Obvq-AwWnP6Rs017g-bGt5qSGgP7VMCGPAVaHMLXQ3UKvCWxFGm-AKmKEm0zCcTdeXEyZmVIz-uxc9p1DOzuAulEV86TJQKjByk4LezCNHKpU_CVbX4wZXQJyHgvNT4t1_uH30AJCLKB5m2msJ7Qtm7zhFl490jUUmVsdkdBZbW5tS7GgMTTHtOArjuNRYeCHu5VCPv1ASoRxBv40St2g_oqI76DnqOw7MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد سه دروازه‌بان تیم ملی ایران در فیفادی مهر ماه؛ دو بازی، پنج گل خورده، صفر کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30701" target="_blank">📅 00:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30700">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icX6P6QngZM5_rr6IIeO2i10uTnUKBGGNJ8ikHfSUVacEnfq8ArAkM-RRZrP2eubIecKG_UACjSMa_8TcUIbXFMbueWTjCz379vDz5yN7UJObjSdJsRFYFW9CER-nsF4nfaG8Davo8XT4GuuzvXJK5pSaEC7joog-Qv7CBsY4Asywy9viNuNvxwmj2d6lrv3Njx-1jVyJvthvni10S1WSSyfwK1PIfLPiH8TMVxPu_UoW-rSU97v3s1-lE6jsAr2hJByPHtE0eDUSAAOyPksiPwHFSDcohy8EH80xfS2hWeA4f3Xa33iJiyS3VBF2JmP4f6sYgDfSrXba9oOhhvHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30700" target="_blank">📅 23:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30699">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO6gtMoNtVqcX1uy9QA9xupYJvi0i9SxFz8BrXY4HPBw3txdAfzqPosERpbQewmA9O7OxeqYLa6MeH_T70gXwJW430MEQ96UKqed7hXwdtWxsyTYYQSrxbCDQmDy4I5xmk16AFH28VVbDHLDQOnaBAH4WWsE8JoxZg5bMCWYMAfq6L_VUK5HbcpLbOYuSA4NcOOrvJOd6EyYxfwa9IXAC8e85wWh7bQtDARE7l4KjuW4MhZvh18Caxa6iPDa3ynMjs5n9pN6qEjetFbtBavaWXMuyqNak8S63-ESbhursqEFv-CVi_oR9O8aXNmYJHvtslmFce5AT76iHaF1B_JcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30699" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30698">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42de6680af.mp4?token=omhRF7IRKKlUssG4hO_84NKJkEzXhPg-4HTYzDFrZDkHOtlNA2GqapYZOBqofuGvh2WHytAblU8zZstj3veQLJ21UUanlmzqZJShuFgWJ-YQJCWPeq8IMGc8nUUfPNeiyegDuRJsho6Pd04ZaSBA5CgsOOLGCD5DFYZClKPLqAt2eKSyqUSU0XPajVyOnT0WOwRCu2xnyAKV31nGHTDtMddkbO10bvX8qKZ_H0r65Ea7pMU5ly7YCZe-x_YGK7homlNw_ANyZwXackUC8j4e2pvhd8pLUlXSRficqJlW9dzYr64Hxw452O2W1uV9McvFmsOYmUKk5ZwYIlwLwI07ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42de6680af.mp4?token=omhRF7IRKKlUssG4hO_84NKJkEzXhPg-4HTYzDFrZDkHOtlNA2GqapYZOBqofuGvh2WHytAblU8zZstj3veQLJ21UUanlmzqZJShuFgWJ-YQJCWPeq8IMGc8nUUfPNeiyegDuRJsho6Pd04ZaSBA5CgsOOLGCD5DFYZClKPLqAt2eKSyqUSU0XPajVyOnT0WOwRCu2xnyAKV31nGHTDtMddkbO10bvX8qKZ_H0r65Ea7pMU5ly7YCZe-x_YGK7homlNw_ANyZwXackUC8j4e2pvhd8pLUlXSRficqJlW9dzYr64Hxw452O2W1uV9McvFmsOYmUKk5ZwYIlwLwI07ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛
فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30698" target="_blank">📅 23:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImJDO95o4nouArms9r8HY4YgCnBPsGwqG9EzcIxq4UL_1FzQ9mUzE75IVHCFGdb_InrjSLM2_8D_x2m8bjn8LKc_ebvOCrA8auo-QyOfZxy_cfHx2CXGfTxbmhQ5z25HeVpzj9U8X8kQ8dGwMUxkXxnRPrA6U-OpDNz2Vbb9y0Upnz_iRmOtFQi93zUIip9_R3kC8l1_OIpmnb2L9ibYHnK5QFufB0QB-s2tSWlnMHx0S_hC4jrDYzMg6V5a45yZI15JdgXH-eKxNSJN6o7J2WiBOBV3xcnUcKY4_BboX_qzkmVQ55p7VzAstcDTiejqGjWC_eAXppT_68aDzH6sVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توپ طلای امسال یه‌وضعیتیه‌که از بین گزینه‌ها هرکی بگیره هم حقشه هم حقش نیست یه جورایی. کی میبره بالاخره این جایزه رو امسال؟ سایت های شرط بندی میگن شانس یامال از کین بیشتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30697" target="_blank">📅 22:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1wOHWvonxVeoXAYK5xNMTbJi6SszCvj4HnCoF9rJcFPgcc13-BZ0zahobeQrJ6Anc4Ed-YoBB81U6RLJ37FUJNq41HQaFN7j0SZiI5fE-jaV3kE3704BaWLkmmGCOKi875gc4RFFH_qHGtVbqTsMFkuVhFZ_s_GhZ-EzCrehg9h-urLG-FQSsYksAs_gA9JP9UQHwyTJZ-Tp36oaP7TP4VO042wUOZZwk7OEyt_92hVaJxN8Uiocg2Bb0iZak1w_HWxXqaBkysDrq8qo1B7DnVjsU_L34kJCubTRoYSiS7rCgbHHCl76AyOAD2NpF23g9KZ9Ow-78DHI9j8iRwujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی؛ شاگردان امیر قلعه نویی در دومین بازی تدارکاتی خود 2 بر 0 به روسیه باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30696" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTCt-mZz3HeiMNx9dBK9IiT6Z6hrgRrDe02KQ8KywzN-PZPt_Dh5cTDlg5_mhqKkrx_KYX8GIRDzj2BV8B0uQ1ITmpNSBLGHTuscADzb1wkRJyegyYU5Uh3BVEmK0MLbYI8HxUAchW8cj7ejZGJR1HZr5UQaj_BUWeMH1ZfavsNXJ0gklAqC0KkxxG9s3eHaU-DkJaPxzIEZ2GODyp9jFah9T3wWqa99U_dW9GXAhG4l0twRY0JZLIuvex3jmFEQxeudRyu2PEfZLpXnylv0MTrbcMOzHuAr37-A_50tk28oZKYPH6SOWIywsyAvU-4RZPmBt6qHGv6sBlDvz1IqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره ناراحت قلعه‌نویی روی نیمکت تیم ملی؛ حقارت سرمربی‌تیم‌ملی فقط اونجایی که از یکی مثل سعید الهویی که هیچ‌کارنامه و سابقه‌ای نداره مشاوره میگیره. یه استعفا بده هم خودت راحت کن هم ما رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30695" target="_blank">📅 21:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=o99MMBkNqCWjKGRJo1rkVvbdiiD0r_oB3aUoxi92rp4lHu2uS2H8p0LnIKd40ghox3FY0J-MkEGjgaYPjAvhuhYRqxrD5WmgUymeZgcZkk9cFG-i9oAnUCCdo5GU3_38-5raJHyQOAdfzGSFziIcGNWqMcVaorLL-HYVCHz4q9gyPA_LzaQ6Qqfs0uhguQ91hhcuwls5mKrtsC9pSUTYg8cIuhuOkMMEuABd92fKL_egYk-Le6uu4qDZpNNBZSBp5AvFzGmSd0PgSaw2xav39w1tw3xRn91aUnYPOvlD9pgN6RgRzdXcpOKG0Kn4W6ghecw-aqLFoaZfBaljqFn-4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=o99MMBkNqCWjKGRJo1rkVvbdiiD0r_oB3aUoxi92rp4lHu2uS2H8p0LnIKd40ghox3FY0J-MkEGjgaYPjAvhuhYRqxrD5WmgUymeZgcZkk9cFG-i9oAnUCCdo5GU3_38-5raJHyQOAdfzGSFziIcGNWqMcVaorLL-HYVCHz4q9gyPA_LzaQ6Qqfs0uhguQ91hhcuwls5mKrtsC9pSUTYg8cIuhuOkMMEuABd92fKL_egYk-Le6uu4qDZpNNBZSBp5AvFzGmSd0PgSaw2xav39w1tw3xRn91aUnYPOvlD9pgN6RgRzdXcpOKG0Kn4W6ghecw-aqLFoaZfBaljqFn-4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار نیمه‌اول دیدار دوستانه ایران
🆚
روسیه همراه با نمرات بازیکنان تیم ملی در این مسابقه.
‼️
سیدحسین حسینی با نمره 5.3 ضعیف ترین بازیکن نیمه اول این دیدار دوستانه لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30694" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30693">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAixBxm-TVmnKZATTF1wQ5XtyPN2Tf6UHv_QB61q6idR5aDDu894LWcvhgVoTDaSQnVB4dBv5ViRaxY92vS3xU52twaHWZhGnWhk7Pyv7gHn5AiqVt2ANbNVHrfByu4MdXDEyQkBAfBABdweyxe_ud-EZ6zT4xOG50zLud7D5cIvR4emT0odPtG-KozAQBf_F215fuDvZCCDjvMhi4sqgRkm_7L34AHmk5vQNWCsH7Q1bp4SpSd6b65Gzad8Ca065P22xiR_M958FGx3Q65TRuv2jBytA7F3l103T7J0HaBZruHMGFKGDkcBpH6dOBsoZusbCiFfiBZYFmheaOyQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30693" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30692">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRUHepTQM1G4lXfsekLTJUF0E9MUU1X3SNKoP5pJw1O2UgtSVrj8VJBk4T5TUeH3skw2dhz26DTVJ5_PZfVNtfSx6bO6Xij7XyGBtG0OLBPKXJu0qFgUzlV5t787wq9R7VE1DJntxXHjXdhB3oPqp917vN47Tw-pJzbskb3bG8jO4ocsnnnE_ziD5sp4MUkRCqIBa1uQ6lUa6ICeoX_qCwq-Lq4Smhefveetob-pNfRGgnawbu3vHNPQXTRKwhAWXA57rhstRhK8Rx-0EXiMIriKQwfXSM9d3_5MHVjb6qujI2XOzFr32WlE9E272WbFUkmU4h5vpgJa1C_u6i2mVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30692" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=XBse-V_2OvufaLmDFYmm9v1Oo9-z21g10kc86k0-QY68U9mRbm0TmTzB9GnAmXFz4FtKf5Tr5LdtWkj42E1ExT-1t0wJ8KlFZ-S_JNWRtMfC0LR7WfvRi2g_oBIzdCyFHgpjPP8iWDCv_gpVDYbrnPorBM6xV1g6hkFV4ADjgBOfnKo00zbg0Llmzybg-hz1FrrKgyFxMogM2KDKG_R6QMSlgZ7qU5fzZfU0-lhzseMORmWslwJUgzb0fuWNOLgePqFZDtmKHgdEciAUkZrYhYnzIhuQyQeZa14BE9ak1wW8By3s2o9x2PdoWAKNioc85Fj5GJarDs9gEKbkc5H5Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=XBse-V_2OvufaLmDFYmm9v1Oo9-z21g10kc86k0-QY68U9mRbm0TmTzB9GnAmXFz4FtKf5Tr5LdtWkj42E1ExT-1t0wJ8KlFZ-S_JNWRtMfC0LR7WfvRi2g_oBIzdCyFHgpjPP8iWDCv_gpVDYbrnPorBM6xV1g6hkFV4ADjgBOfnKo00zbg0Llmzybg-hz1FrrKgyFxMogM2KDKG_R6QMSlgZ7qU5fzZfU0-lhzseMORmWslwJUgzb0fuWNOLgePqFZDtmKHgdEciAUkZrYhYnzIhuQyQeZa14BE9ak1wW8By3s2o9x2PdoWAKNioc85Fj5GJarDs9gEKbkc5H5Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله ژوله به قیاسی و قلعه‌نویی؛
وسط برنامه زنگ زد به قیاسی و ماجرای مهدی قائدی رو پرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30691" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30688">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQ5NEjXPrdFUPD1wDk6TWwYKpv4DxAKXxsZio15KVEp0ZjSpy8F1GL8pk-WChhRm1ujyjh6LZT1WUbsmKXbaCdYBBf421nKKiOc5XrC3QQmfoHndrNrGsjfCoThMFwVecbkufp93s8t7o15mgZTEPVU3yc7y0-eqjpobUoWkBh3Rd24O3iQjEYXl_VsQPRSfJ-NnjIqrUChwX96RexvggbrmRJfApjSmTTfVJ0hbCQ1sjr_sLt5Z4B0lxIHUS0_oLIS0tSSb9V_nzAu_POuQ36JoklU14ECpLccNBgBvVFpONG7bS5a4FBdiTXbRhJFRYUuH4SPp3QkKp8g9UATNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K93dw4BXkhIZLDa2xI7kVZOUh5Ul-gVEyhBSIMFhB92ffXFwVaeXrLNzpgxJaSnJ6yqhD_KlkdFQ7QA4SGLc0w5JUqTekfCrg1rCA0GUcHNnlGJs56-Vk-ar3Y0RKF-kl0vmLjhnXTqs-KUEJzkFg9qg0_jXAol_3gLP1IhOjz3y4a-kqzZDKf_s8JOkRaalNnxa2s04sW1VBAfNb3N9HYYieHl-KTO0m1WuZu8U2I53kZPMi3YQoZrtb2FRCF94z-7dHK3ifEeTx0i5m__4F0i4UzLLdPuBOtKJED8a8WR17zLjV_9GV67YUyHiembqvF-F-YwopgTNw7T1MOoerw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دومی رو به این شکل سوپرگل خوردند؛ گل دوم روسیه‌به‌ایران‌توسط الکساندر گوگووین در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30688" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30687">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=TiddkVoSZn8fL_wTzHPgqZPaMg6eU-Da0bsrlbXMq_kQ0P_34kmKCsplzxPPArCu9yQsCWNnZmu7wKNaOMpCmY7m1_yDiviAkC0d57hxwjnB0mJ_i-BxKyrZkEfIhfWyC6VZBFfuTobVYaETzYjCIYlY7KEgM4HskdIE-g0dRSNFV7B8vZoWtY4KG9ciG0IwTbYxvIhsTQZhMjnL-QXCseTqFQnPcil5CVFUJcaJ9ftc1dMJyJYCIfwpoqIeCtV5ACXGAw4ENw291gsTLdzcJy51bJJPwN0DvqHH4xoo6Du9FnP8sd3czNYKDXH3ve5LJr1aBT4aTtHdwjJzBm2oaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=TiddkVoSZn8fL_wTzHPgqZPaMg6eU-Da0bsrlbXMq_kQ0P_34kmKCsplzxPPArCu9yQsCWNnZmu7wKNaOMpCmY7m1_yDiviAkC0d57hxwjnB0mJ_i-BxKyrZkEfIhfWyC6VZBFfuTobVYaETzYjCIYlY7KEgM4HskdIE-g0dRSNFV7B8vZoWtY4KG9ciG0IwTbYxvIhsTQZhMjnL-QXCseTqFQnPcil5CVFUJcaJ9ftc1dMJyJYCIfwpoqIeCtV5ACXGAw4ENw291gsTLdzcJy51bJJPwN0DvqHH4xoo6Du9FnP8sd3czNYKDXH3ve5LJr1aBT4aTtHdwjJzBm2oaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولی رو تیم قلعه نویی خورد؛ گل اول روسیه به ایران توسط الکساندر گولووین در دقیقه 21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30687" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30686">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afda25603.mp4?token=pZFDkvUbnfcNvmKe-7tmopjaZTZh4ONqGdgFUXY0jOuVPq1oCq4CPwosqi1B260Ae0R4E3I4aQj7NFgmDZsFg_GXOLFS9Ka4fE5jz58PpGQc7RjHeGmMpVZlcHKCCr_7BmYETF0IxVEvGJU-G-KTM--4mMJaIVKGVo9_dBcluAXdip16vlWiss-xmsMwYNKYc7ajG6quRfptSTPsATj_28GYFut4y9ewjH-PAKQARI2WAj8QYjZll9PyWftJ4_tPQgDJYWRGJNyMWqfsUHXesWjmgmL42aWbVihMnNWtAUmVlKSVoNKrYnP_jcpdfGHjTIhPEF23ysHUbO_rIglOAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afda25603.mp4?token=pZFDkvUbnfcNvmKe-7tmopjaZTZh4ONqGdgFUXY0jOuVPq1oCq4CPwosqi1B260Ae0R4E3I4aQj7NFgmDZsFg_GXOLFS9Ka4fE5jz58PpGQc7RjHeGmMpVZlcHKCCr_7BmYETF0IxVEvGJU-G-KTM--4mMJaIVKGVo9_dBcluAXdip16vlWiss-xmsMwYNKYc7ajG6quRfptSTPsATj_28GYFut4y9ewjH-PAKQARI2WAj8QYjZll9PyWftJ4_tPQgDJYWRGJNyMWqfsUHXesWjmgmL42aWbVihMnNWtAUmVlKSVoNKrYnP_jcpdfGHjTIhPEF23ysHUbO_rIglOAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30686" target="_blank">📅 20:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30685">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twpTwP0cTN2PgX4QHuovPiSVInFnOG2PA1b6laoB4nM0E-eYtYUfVgPxhOxsgM1YP8BKL-X4Py8Ei7MYbvsOAkI293gEfOXLdLlgWKpuq_gH_B20igS-cMT_h3dlO6sJTy3aQ2rM_5lGyuUaaJb-EqwiKugozCgpHxHgxm_oIvgK0ojccCV7GtTiE4HV3oC74wKAzUNW9yxdifTeW8sXe5QFN3cOojQox3Sd4asQez_tszUDOAsg00QrtaIZSGu40icg7oUNA9NsZnF3GLs5PAPsFKmoOhlUY5VAUJ25jX8jsoz9pnCnTBWO5Yo1F8k4JP1n_mqZZ0Q6h2cVejv1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30685" target="_blank">📅 19:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30684">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJCGHHktv9Muz9q3YveOHcQeuaDci8hPFf_8uiAf4FHaYiLe0_c55iZoh8VWMELcFjw4uQOKmsCC6X_6KBeyxvQN66_LEBU1J7QaH_OEufBaQU3bk4xVnUcZMz5r7htfwAtqBDeah8yydxDvTTn4M8ETdmTZE-TrdLpSqhtQ4dQjAQSIK2Q9thNDH0VgxxJn5KGlj_yiaAVcnwdKcpEqD2_IUEaxGCEbrzrEY-uC1H_swBcjXqXLoic6TjgoOasjUBKZpQOEzkDMFWv7RLv3_NdJF5YtaaPzhVebARzKjhdQQkYVYGbXAN8vnCPJcG8UvPtIc5fR53TZ3ziIwaLTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30684" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30683">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS0Y8xFuSfMAzPz8kDb10z3P3IUG1QQ9BoEpjRzx5mlRLPsYZBvvWmgPyoaTgW9vANrnwDhOmidfnq5spPGdaduHHi1vzXWYI7a8y1qDeRbdKZ-vnWRE1WHzph9_SLKLnRIi8TrOMe-vLvYQzFzF4ibhc8AArKRgDiJpq73qTe55RT1N86uLIJULJix4osMfTqls8tla9u5hUHrBuyHUqAC-VhAkqwlT61wsMzcCOw6IgABGqpW6sumW_Tlnsf9xZvPD5RSJmltkynyRWF30oFpLByH2kzBkMe-HqLAePx09ijo0XDULPADxmep4aYR8eSMRZiyGil02CQ4EDN5trA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30683" target="_blank">📅 19:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30682">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrgulH_F1hwUon9553TFIhDAuAJUzdACrfenUz01tmHGINP-HvgApVr1gIhMvmL1gaxO4lRLCiS1z2QxSAv4Hye_-d_SuonufjnRVWCHUOsTYexjuIxARMiHYGuFbqh_pO0Em1vMtfRnA-6EA9t0cxcMoXPqGqN1bepR6qxB4kcCsdvWsZeF8W-ZGYntGJBtwMuvm9tPQiSkaSFpkWnIKUaF9hfQrCIn9zDgFtngtSCXZa64gH71lQSHjOppUF0_PypY13ASqBwBBA6bmdnj2Sjvg8rdnNHsvLpO37zmP36mFs4wzaN1gey8ut5ygBFmffujyPvWBPeQAfD0qjqbrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30682" target="_blank">📅 18:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30681">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPpQLdNZwYElQb8LHGG9m2rCfnsMMZHWm0VikHR55z0W7sJrGVM9_bEommefPiVgqmIkzCnjJTwi8yTM4BzdhcZHH2fIqbBsXKuiVOFG4200tClUsF8_Iqfod5-uWSR7Z8UgUJYzsXizlbRZkZVW5aojlDRlCy0KZv2DO6N26IO5elbl0HfBI7hlRsx0DIjfqaO6TuOi3jT14U2FMZiXRvXF0NTa65I5ewG3DtVqxeXdgPmd1Mvvg8DsvYZX8mW4Ci7W_5wVOo2uZyuGDg0aLnwIXohPRGpM8e_WQyae6Cpi_UnDfV7qGjjCo0S_rZE3HciwGWHaxLLPoAblZem2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30681" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30680">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsAE7ZbkgrzKJ1AyzW_g8l8rNcvcaXpMURPmnNgtaLuHSsurDZNpa8H1z_tBQi5j8m-zwnBQtQKQDc5a-lw7EOSb7zTwq-Xpyezi9H3iYSFvHRDvoGFl1KF_LWagdtocuhVIVlOwt0CXqLCtHL2p2yr747EEnwKKRM3R0LKoLXsGfknORgHBwRIhb99c9yGQG3OI_fRBdeWHSdQ-iFqDL4k09oKm8uZxWstA-hK9nfKU3SMIEqAcg-NnjgNQ0lMT4-nxxcTX5u3FOWf87qzI5BRCFldZta8ID1JG6ajkAjS62ZoQ4HX4jw8gJOh5vrdRBnqeAnENHB10waOIfd0zXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛
ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30680" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVi_aRnrq3M6WieB4lxnNz8vakhi1RG58kciAUUIu8_KIk_6ajJ-JSCvH29o-ETcS4yhm-ogJ-5PbOAucUpo3vuDXa1Shx6NvtMfTm0zhrWPcGXUGPiqb_SOncu6aJhfbLqOzeazrdvXXRM45zF3Q2G9paP7FZPzM7kR_tEVzFuuS48y6X_ZQGryXvARasiInrR4Un2JG8mupibdfmIyCxYbymkbYe2XWz6h6w0zSSE7G9263iqVH8ghA4TXcqFUI_y_btZXNKEyCHdaNfeHmFfN04L76Mq-VbB0G92R6IZUomb1XKbb0XmYg2nsfiuVbZAlR7hujcgUQ-XfhfcFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jElRMMPCdHAursBI5CNhs3iL4LUT0yxXCLL3A4j4f2OGAHnUGyLmkZl0Zo8IluoE1o8UFkqQNScvOAGW9-tXx-frWIZZcT_7DeAmoZbO8JgUsfLlpzcCL_YnmTcrVDnGHPBB-2XV3KKiV_sCp8IzLnpP6pcrCb4lKlPbm7CP2DAMn35egvCPEggn8hezDtF_W0dnSZNPIvACIxXWx6RZmf1hfluW7mKQYVqISuhsI6z0coUU-Y7u9E9f9WyB00CKYAbwtPxfnmiepp5hoJeyTtrQGxMvkSxLds9b9KXGSWetZFJtluVG8OwFPWNJP9NZva7m79-mBPaZMwngaC6_OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30678" target="_blank">📅 18:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=pApXMe9MPUQo3JAeN9t1NxvW9vP3Eub2jqlxMRK4KLMhcxRIuuPMn_4-D1BSUO_4yUmAsH3ydxfzrl0F0moVioykyyniu2yshdzWePAwCmsFTpXIXF3qH99PIRtJ3vthchXEbB38fOPFTd5_I0yW_RK5yFQqQwgk9PjKoEang646BixjvxfYAMWxtr3sPenjomv6_1kMtjTYmTxgeI3zbR7RVdAmDRyF3okKU1vTzTfGV8udifP_lMnv0cav3gKr4PER4FwoZJCUPG8R4285GwvuJWJrl-PUYD8xOL6DUiJAry5z2ciKFmPnGGojVxWMW1otdBdSJ8u4eJflFJc6pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=pApXMe9MPUQo3JAeN9t1NxvW9vP3Eub2jqlxMRK4KLMhcxRIuuPMn_4-D1BSUO_4yUmAsH3ydxfzrl0F0moVioykyyniu2yshdzWePAwCmsFTpXIXF3qH99PIRtJ3vthchXEbB38fOPFTd5_I0yW_RK5yFQqQwgk9PjKoEang646BixjvxfYAMWxtr3sPenjomv6_1kMtjTYmTxgeI3zbR7RVdAmDRyF3okKU1vTzTfGV8udifP_lMnv0cav3gKr4PER4FwoZJCUPG8R4285GwvuJWJrl-PUYD8xOL6DUiJAry5z2ciKFmPnGGojVxWMW1otdBdSJ8u4eJflFJc6pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابوطالب‌حسینی یه‌تیکه خیلی سنگین به ماجرای حضور خداداد تو مدارس مشهد انداخته و لحظات با مزه‌ای از وقتی که دانش‌آموز کلاس اول اون مدرسه به‌دنیا اومده رو نشون میده! عالی بود از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30677" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30676" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
قسمت اول اتفاقات بامزه فوتبال ایران با اجرای امیر مهدی ژوله بعنوان جانشین ابوطالب حسینی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30675" target="_blank">📅 16:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5W8qqHUPIsJ8LxZneb6xUC8oYbNsXUOh-TVWd9IqIopwWReySesAjTKgJjr338Rp2-hWdOZynw_i5RnUt-iOj3pcGVmAu2fnqmG5hixoRbjatqpQoapZ11GV54K-OjfjnsWZ8ThBToFnobx4jatQXXOzhbOGnrsbEdEX5-sCdhIFuIQSvegZRrSBHRIIQzs6-77oeunfobl_JtWtI_07Bf-ibmzX_m_duQWuOvDAEGfhATlslCvU918FUG1FtapyJQjAJ5WvOxPRjH8uc_hGZgx4mhTgJRF6RzXY0EU0q9qLByDJgpZEcXaGd559HT279WgI8faxz-syb2KTnZZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30674" target="_blank">📅 16:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS_Y67ghPiVqADMS-TMxNlsfO1AoYbqYtKdNmTPeKUhAc0ZzHDDE2jVzQyUe0jm7-sweaYOXrRcfXEoTpUiaVIfNI9EDScn1NRfRxW0YkIsMcIadiL1zGjiuvpFU2thkyh52QGNO2NN6EdKewlnD-jApiMTQrYHOucWuh_GrL6EHlRa7m6ZMb5vLCdduLc11CJSLNbZ1Vma9IKiWdZYOnU7LtUTzPKlonq9wpQP3oiNwlF11QfnVmAkIIjjnxc83DFOy3tW30LVwPOku4Wj_nCTGTeWuHcnMzE6KiogOzcQh4ln3QqjmwaELrhMhovAs9ciuo-EWtbd2B5nt0-b9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30673" target="_blank">📅 16:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30672">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlCh6HPv6qhBpSTpE-HDR07K8WudOZ4EFQM2DVSycQ690rLYfX4ExG28biuXm_fEkLaTcMKPf-sOD6nMn15LVZ2vKqLg5PqjTYXDHQWqPi7w_a2kQ0G5klpLZYUgQsOiMjd3KDsYzM-0sF88EV0UugUVbHclfSZegSNbblP1yQ6kVBaQM94EDdM1ISoAMvez7hJ693JPKwBFRYYWpR7gAyXHtxRQdAfiI2MC5u0ic-JUjtzFZGsb-yCJfLIFPH9kPERUCKpafNjucUI6ZUhRPneQ-MaRR5ZvrIfqWzJszinHspNgsXQvqpQPjt2mM832M9XU9b1s0kPU-sWMn3LSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علیرضا بیرانوند دروازه‌بان‌ملی‌پوش تراکتور: با کسری‌هایی‌ که گرفته‌ام کل سربازی من پنج ماه است و احتمال زیاد به فجر نخواهم رفت و در همان تبریز به‌پادگان خواهم‌رفت و با تراکتور تمرین خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30672" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl7xyw3RZXeHkQtOH73MZV39ZnBoMBD72WR_2wY1VBKhNl2gh5ZRD5E1iFbD4LyKF9UU4HWmviUbjcF3tSpmPzWdG9h0Pyii5I_YkGV6ZTvIJHg89T5Dn_hhXALZenBC3v3gQCMICFJrUJwtBvYN_6vbNXmxvGcAFprmNyDOFDVa7BIc3nbbdvzExNEO1QxBtzD7EPsgZ_SQliVhgumZmJLP---rTeo0iaWROQ-z1bkFDaKnkTC5kmmseB4d1tXBePxBUMvNnRWApHW_jgHvkk9_ojthXhyWFi0lGkGl5zX8ieyNBcKZayGPdFErciP6hyfwHv3FdadFvJUlvcLk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ باشگاه استقلال از روز گذشته تماس‌های خود را با ایجنت یوسف مزرعه ستاره جوان تیم فولاد خوزستان مجددا آغاز کرده و قصد داره این بازیکن رو نیم فصل آبی پوش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30671" target="_blank">📅 16:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUi7WE_7hIYTGaFilypyYZMvQLhonKfk3ElA8ovJVfN_xpfn_ulsoY_wp5df6wbHZlAd37CJoVI-2gulQpI-lgdvqMTNj5H6bMq2kM3sIezMhNpGtpWV7ZbZi9X6dju5IWI5dyzl_HBh2glwHt094wyalyST0ugvPiOYx81v-A82he8hr72XYz-xy2SihqvkgY4UJbVpI0lYYedLQzjTfv6q4DlQxJts2s0zd9kUQlHDrvR33zGnQ7QYJ50UNPgpv6Gaf2YbSFSJKiEy1KAvGibAgXKH_Nq7d-wIvP1PaOzyRF1rzXa-DbfHPJcbZ19jU2Pt8R58dFkplj_TCKvaRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رافینیادیازستاره‌برزیلی بارسا در این فصل در تمام رقابت‌ها؛ 15 گل زده و 4 پاس گل؛ دربازی امروز برزیل هم به دلیل درد عضلانی تعویض شد و بزودی‌میزان مصدومیت او نیز مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30670" target="_blank">📅 15:43 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
