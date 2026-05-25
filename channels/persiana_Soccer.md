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
<img src="https://cdn4.telesco.pe/file/tjs8j3mUWFgV3TwVn8pogu7I3yRJHM6csRK_1c-o5-BcEq6SQMSd7Ag_xYgni2kWHkJ6s7T0sM8uubL_zhd_FkAy-_N1f5GeXW-d4XG00M4XmI1U9ulXntyhQgFpTBcbCSPNLWqjVDXsdLr0t9YnZFw6RKp_HPul_srnY4EhwDgfTkd-LAm3bNrax8gRxzMsVyzGLPE3I9YOTlf5pZpPQ_Q4hdrVC_uNmuWBak-wahLIrEIoHe65HEl2SWncWJBcllyDGGWdTFgaCGmGmmglyEhIJWrJxMEvtJmwfwXhPMqhiTQBjMdNQXN8IYclpBmyeWyYlm18PePF5G0IpqtwPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 192K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 01:10:31</div>
<hr>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVpUPW2gU5JgWaMKnfqD7WxrvTNXJXAKYcRErzOKUNHAtOhDY-njvl8Afs3l5sAE5dzwH12VtFtcbZBSHQvEB1bXjhG0ce_nmsuHA-4_eNKCvjHTGEcVlzvXJwPAESfPfG7NNbc5Sqa28pqFaIVOfvP4031QvZZPowwQWIFcbKDkOcuYgy7YIUB-R_MW8qNioNu36xT9e6FO3Cocwh2-mwYu4Z6mz_Yuv8VbCs6gSQlsRkiF37DluKK0VBhnWuqj9kfK0zCSAU_VxuriXCnOfFUi_1RGh-1P7pDauG7imPWJ1FlBDL9SfMxsHA40pv6WyZur0BcYUNT3oLrdWj9soA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGV1ORvAAIuBpo9aDOB6EY5VQEONoL4xUwZNDXs3IiGpz9AONnNVq2s7XZC4afQ-JUe24b5Kn9E8iV4ZH8TdExdef3lcHN3ZNT3tLeuVx65AflE9Y5mdmAVsRX8y0yYNzMDrLWRK7PxgmeYVGuhOWD6I45xTm6MIaX4O5fKj_JWljMmCZ8j3lV2sQndqZ5ZJDHmOkzMzLJE-ox5iuVV3P7TlgeOw70ujZwM14eH9QTaDnkU7q9VcHt_CdBtkGEu1y4vTuhfH2YfwgOhGforhqZuX0ihgR4-d4Wm3MUIxlS_HCF0IHjVfBstJ9AD-vmk5MMPa-xflISqtmFXinoIBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDkiZ40y68WNrm2qC4HLObzKOnpx5VJRQYG12zg_51ePGaxoQ6pguDY5PGT1ZJxVDRx44tFuckbbYnv6AomHaO7q08bVVw7kbo7wEDepPd4Ocqx-j5x9Kn8szswghQZzZXuE-mK82HheFE8GdnsBuMzey-EjE_6dixEJndPDxwFz9O1y-zC3q77o-MEsq2Hj7Apwh23gUVtBBLGz7HM_4ucFwsKTFzx6WFAFhMgccrhVcnPb8SzCmkICp4rfQYwqCT4XDFU03PvB-7uA6hIaRHe1xHGBASy2hKwWhWYsNeo7siS4MXIntumXWCyQoXGLoIgfV2waqGiS4u-eBCJT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgaSg90UL9xNVM7BfLhlqUV2Hzqi9KRyukY49qeVhUjX_goq55Zt_WE2jAAg5j7uI4UbHqqwR9gjgJFG2crgzxUkHwWC2xr9BB1tSuf4Wp8BCZLL_PClDZ57rGev9hadn8SdcEQzsUkHJlqSQyIn9yklX2_38yj0ntVOOfbIauZpdyJ0bs45Ss4hprKNJZhcX-OFeFMHeS7l3fB6rFvMqDjKfKp-FN6PgNCuieT3Sdiy9MBP1gvskI6BiZHh2hepJhtN1J-JoWpLa3qtme_Hn4kYxCGR0n9VIPgLajCrcBsY5r0yECunPGeLp5mr9Y0ePsPX9JuZ7n65i0JaojTqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFDlYgfWzyxw8W4JtohS1QmbRMiab5q9fO6H-ii4qEDvhatLDBDvEsU8q0RA-rZpu4PrkPOKnkmHTfpQei33TfxCpX25abNuo7urRsJ6ZkS_9jEAFSYKqUKfpFHtwFB_Ol4hZ_atDZj6LcmDOhz4G5Ch5bt28HhbeVWZSo-jRkLST2l2LsnTP6rGw_PJmockLQnKHq5Phs0lDjAGDXas5EfVpCr4sxSwnIvZvd4s5nffymwLyChs8XulLTGPAwphhtYIhznwxkDTci-0zwqNefFzgzjOMr8OecEs666ogQk-vyBADQH3SS8raf15o3OF8tdgBkoy2xChKPEvPiK-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1IpdWoWvP99oxRELwuqmDaHTaCqoKXjoOZZcuvyjb6gaeWbjVXC2RLA_PRWXxS2kCgDbTCUxo7x6YdFZXFZ_cVa2YvjaNl-t8nzyhcfW8Ib7042ifJlR5h0x0Ybu6inLoVQ37sPDztnL7_uFba7YQ7TOEwJcr54qMCF1GHk5CmZb0BdJaz0BFhf0kTICFvMMKoWHQ_VGlzVWgKvrUK7tDtinhSd-hWy2xy2y1-RqG0acodam3tA_rR2wDBiWTxWWqzOMSc86194gYhoB9k5A3JjWhkLnezkIDuiTK_hJW7xTECLeKWMyZMJjhwDka5AjaDw7Fe2kJ8w4NlqIopDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SY7Iam_IEY3NXkK1OWOMMXpB5ZfvBMLAKgpQ61khcr6Qqdx8YzhPjm8bCulJP6Q4x8cNkBcJ83hGgd8yJFZA3b7TpQRw8wXN8QMNit2PqSWEe3PTUJ28WZQPu3dyXw_IzwvooYF488VabPhFGu2lqCVL9u_VmeGtPivobfUrMXpdVRB4HVe0FEoMHP9HYe3o8GCgm7__6C_4C7HVajQohfmBK-VUUDkgFqjwL4pu1Yu8eH_198MPLLC0EN7v49WknEPUHptSL8lDs73I-T35RQwIl6SAk4sndA4evoNSqIL6ZZnPRUohOBzBTzdMqU1pAJ_kHeK_z8EuQhOzClE4hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcgWM0Ikj3YCnKSqcfbVDn-yD6CRHDyso8S2WMjaQYzuKvrmRJrx2C1O_qGkMWE5wBuLDfrGTvGo-8gJykgeiX65BhXKwV9PnXvzqinqmASjKeGL2bIb1fQXtKnxTdVAS9WTUn42YCiNp74wJh9oAQ3DepGZ06i2KwofNastNV11PvOXzsnBLxCSVzoqEmTeNF2XHk5Xq2eJEaVN6Uu-N6IsvCX0JW5VIl7vp8G80QJ-kYygWYAVARNUwGRno1zLRmunxVKi5d9m-PAkohgF43zmRdy7cwaVMcF10neR-w1aN6RlOWlDbQZjR_ImNMtdq7HVgEi2rsqefUHOUYi-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahCwkqXX8-GJWs5uy9CCgdcwB3-OOq42Yg5hOJa07Sj4pkM2yd1qoK_M9kI8yw1BezJ7_Lh85188ezWFMzSd_ouhym9ItQe2HJ3sF_T_XwlQ3uV-OqU-u8dCqgtH3fHoJ3EzWSyPVt0QOAa1IH4BybWsMW0IIIjxpnO9N5KY3FBNixLoDHqgtwKpGW70I81RUGOjXGaABPS7Men7kS_Je0LSRnyBEld2-nBztyw3gi2DpZX_nQStGi0utmGZOc1Mnv8jAbPsCTKB5EVFQACL7W0QS30VCiCOYy1kFlNRm1Tywp1U6roAVdBMwgqEZk0VhcUf3mVXneKTFjDJ_OsYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxoxQN48bqJejR4ZK21QKiSvcjAJ2nN8Jk8z7luV6S40htk0TYcQEvrnGUusHhP3wfoiGt27H0cnIZnnzKDGtDqcjclbE4XQAGBHCUGmntcGezIC28qmZa6mP5fR2fuxzlaofJKSPQNedZYz-37P8vk3q_ToF5017Me4xcaoHQmF1yKiPVPPq1svYsaNVMHCm_z-AbyxTGWar1FFqwVRPv9CHB4n5jtb8gENU-r-0E3L4Sv9AwkbDuXyvWqLuD54Wh3YYtAByG77J_2il_QXhzm3bIYHIBfGquWoIbRq3HXHGZdJOqjNOgvOA2trJrMkTC9o2aVrJgceCu6mn9lPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKrP8UNRRFAWvgYss6jSMzRfaWWYdNta9C5z237IZZ7SIy4UAhIjM2JY-9z1YjFpE2z3vXXEIGMO1EyFVseWmBc1q3ulcH2aaJ3n4pEwl46qEJoAKD4tP8UGtNOgOCVZxfeZhdBu9qBaNq67Qwh6imSQSGOYHYtptTmT2Eff57LaWqbfQ-jym7Grf_KY-KFwEN_nUuoMBUhF8KDw6-k2JIZUVvAh-EpO5PU4DX7xGHiGkzkniXtCLs_YruE4MiiOpHLrPklNuD6ooiALzzFWJaShj2Ko_XBC51tNMNEpzDWtJv3W6fMxy32IbCYkdZbOQPW73MOH79DjQU5VjI2IbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA-LOKhRMdBHUP1ozvCzKr2i1eWAJ9NWIf88MEwaSM1se-XB7u8NYurhIRFh350oSughxSpR6dNZ7fDy3MCeyay9tPraXOuxl4RIxgObtCf60VmKCJodBGcCYhhAitGO2NlVXf10U-NCrR_nZV4KW7NSI0ebuJ4jtm6gIZyVQiVPl_L4Exg_2fUwf7wS_CTnB_zo3ygxkPCsW0N6A9jTyrExyp0Vn8qiJnYAoFjjGofxQhaDxZ3H40nMw3lJVjoPOBhgkumEHaBUHRmu6XKBgBz56brqvLlxXUjpcjbYa6CKNScnaKF3zbq5YsnpbKPxjbqs4cxFWtUa0ru9Zk6uDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_w4_onSSrxRLuHOqx_Dn2vL90lJe0ESN6TCu809s69L9B-18ptTDFfOzz6G-z2hzyORhKxL16HIZoq0DXhFSKbWmy56U2tj9Jlal7n0e4nB1T-qPIHCVve6t1K4RX94gd7ZcSIq1xqHM-7WU1uRXuGrRyVgh8JOxWH1M-C19h_Zrj5fvNUyoq-_B1kaXXmW5CzEmKBMX_s-PYu2vV3eqg4cjUc9ONrjWc6yU_xpVwYGxlIkbSpVmi3qnvWzYlqX0U2RoIgtGTJs7j9aTrDzAoSSv8_7ATueh_M2ZCdOrW82ZcxZAJCDfiCMqyvTD0AfbjJ6FVBqgBAlV7F9hwGpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlwtrIBqlbUlaNxlitqMEaZh8yij9kEQpdbTtrKIA0J61EcMlh42QE2oCDXcGcSrywpN2bdk399G0B7sC9jiEC7Bd4SmPU5ZiPjB2Ro5X7HSyTh46AVosusGhpBG92cyuI4spLjs_4Ku24Yh5orHaTcy3RcK0utSpFbccBkv9yHHub2Qwwg5AktlzWM_hqo0vdFb_kVIZVuYTaIl0Bm18pHPBxMILq1VzXZy1IVe3M2Mmbohm83MBhdmdwEMsqTe_XmW77xkI9GJ3z_ARB2NcRz5o2ebB-ZOFNXbP1Vd1FtxEsJIL-iBy2U1l0z_Fb2yTu1KbwDU7ZtUz_hstQ9jVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQmLHudhcuUUBY48l7gAoKZEDsyu-GoPtNtEdAS2BjSd2I1C5ym3IgUva93tm5tsdLm6SLE6fpguvwCg82b9H3lSY2X3ibbU2HT-_vAQgCzlEiyUIb6MQuO_6VcSw_0giejW7iOyeftfghAkem9fhoW1wIFi_lI0sU_f3Iu3ew0qsIDjOqysErG-oT_eVVmZenRxYYHRLWPkwt6Uuc534KCebIuALxI0PKrk6q2WAJyq8TpQ4bqaPUuH476q89h5q6wQASdpCqweXKma5uTbLvApFpyrbaZCL-tuj1CgkSLdGbuFG1tLIvK9GjEepSVXq10q7yfqRgPiQ3OFPcUbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGAzZiI0tUf5x4QvigXvROoE7iQXjyvUmat6cWC77DpwnmkZoX3GYB9TvrjRd_RK_LhDNjMauf68JSbTDeXrsb3KA-NlXYklDLvJS5iDmWOXM-gcZyZT8FOsfXm7JpQEYVaJIIfmhuSVVF1Ca-RFBKN28g2_gQ7xKqkgi0SUF5a3tHOphbgfNAju2BsxZ1JLfZ_XCxoLeAH-REFSex3owocuJqYiIsKUtxdmSS2bE7L9MRKvPsFzl07jFVnLC38m_5GJljvU43-QF6JRMTtt6QfH2faMnRSIkK1NSo681LrO2KcG1d7Q5Bbye96f4cr-ITy6c-M1xRyWOZ3_YpaFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn-j1ieCO0EmtCC2B-hSg0NFH6cd6_0RAnMWU0GHeiDAjW5G25UFs0fXVn-MwD04H9_PMkA3k64f-HMHApAMgWLJxRnqAY5uaULroeI17Pqx0uYr8QJR-U3wTuVb4CgWXy07RJFq2OZus9IHCCALbJ_EVTYKlCaaeD6PWdHwKR14StET4THeBbOL4I6Rvh2g1EMTQMyup27D5MJIC4dykbS5CkcoDkC7vhUqG-YQnto3O4wR0tv5wbC7nxgBWWU5tvN1yshUBa_PjXFByJ59CgsfHoG8gsQeToKN2CW-pvCpQySuRX5VqcZSWUOswLRi48PdRWLtukI08jcP6aDgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leXX1szEh9fmY4N-y8TrVmCZvy9bh_BelFUe31__n0kMX5QYqqLyEX0mmJN2N-nvRKJ4UjWzbThlDLT93hpSXJuwzn83xEDHaErp5yFhAuHz9PHqYKhak3DhLm5YjrdvuWyfOt8GMYfPFCi7NyXoaJVOPDGGayqrJvpcWiMteG_5kwUyl9nQGgQ3zuSz0FaefdmmL3JyjzL9H6gqJHWLhixm5Moex0oRyOBgbt-lAR2qZZ4sriWmmy6YRL3FpU3YCJU5sWkC7n8cxId5Tj2nseVnkXqAH70pcvsZlGopg1w7_TR6QVAMSOCOSGfFZ6oA3f9hGz8Wt7z2u3lG2YGCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJgJ6RZGrNn41YYRvKQADFw4ti-BY3_Y65cTWLW7wqjSOdGz8GHrC8maiAo4xQQx_DRRLpFpO1LIdLZfin5F5tu31YJgGkGXRYUO2IQcNvAvSsSOiksQP_JtFhQzFtKwyzAUS1y47xl4KMnMZoyBvi55c4N0UPEqvzP7CZRzK_728Egiq1RNREaB193jgkN7dyVD5-OHtXVoQhvqyfz2uaFqVWsNzdLzrdJrN4OQ-33roQAPdkuzKM2Sockq4HoUNt0l0lehs2GUUjBsjR9rJUJGxPMSayAvvTl_ZewGZvb9c1Ewi4XKfzygCApI8fzGTnsk9D2v5DHBvAQkzMJPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVyWzS-_TPmsiBPLbpcWDIzeH4nd40vx0zKSr9fq4JsYSCxN1N0FOm6qQWe6WWjC4lSQUQnCTDrmCMbqT3n57FiGuhNGZqRxjqOflfVVljBrwbg90zmxb3Dw02shNtpgIQW4GABtg0FAcJ2BM24CZ4tw7w2yOVqrBPFHimfjcWy0w2bnhH-udrlYriJbq8z5uGAZDoFSiTEt6srh9MF_yr_0a13ZZIt1r9uHPYy-HWMqovzw7egxt_RHf0q_Pb1ZBQ9_vlsvsmRTBK_7GqzSxmT5EZrAMaqQuZ__MiZdNCgYTbnFbLXcivYpaJ1yhZnAZ8pT45sGAPtxMierg4HVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuzOQ4T5C7al80ic4z3aijr6lfDCfp5pnHgkRU5GpEZ3EWUzcg5lDF2rie60JQW56S1K94CUqkkFBX1t-54ThXT5zPoM-zU0_ExPuSCe9DwOdjf8uUDT0DaaXqWMZND0KKV_pggJhRpjhzpT9qGy32hzkh66lMDc5TdZGGxPSDxkhPxVX1DpPBLAgEDnbcH7kgHoUEld-qKY0kFntahv0q1j8d-u1Tu3ZbC5ototc4QgHzklAaqW04JpYb4_BJpPULHZz6TUQZ8qZLtmYxMnw1Oi1vd30YdNslDVXsQu2FZjSjXpl7gBAthY_i0FzIdwNVSw9cNMRq27oZejh8drrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkeF3-9kCvDFTZstC10KVWe6iIP7FTffFI9nO0PtMykm0mbWlzbEnHg40NV1STih0YrUFl7i-XZbvHAsQC3Vipj0oqTQF4tq7CR558FyUirmF49e2dO6ET9il0SOgZzO0nyIAgWFYGCMcArE-KNfYozcKqq37Fhczfvl6LpboiJUFqgtOfPdjzRGiV9AD1dnkZYCGnSx4_4Gz0lkjtwSXIiNiWIhrEZ9LKMmugXtixI3xeiOMUY8bZU1OFXcGp_TCQUakw282mI2mWxUab5uy4NBD4JPDAsroxccxezwwoJcNgmUGob2KYNJqTSDQN8VLvwSefuMlbXg0WzOsd-oFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFhWCV3_5zAqhAfpaPJu2ydQw9d0r1WDBwLY9HMlqpy2VqucTSfafkj9M-jje2NvZDla3YyIzixAVsq5sJEnvhDDry7eVCgdTZrulevmy7HlCRDNOsk09OFYujdWHF4N65i4V9P8BWERFkwWv7ncqYOLA-Pn5MKqu12bpsEAnHuwmXtXnzTm9vxhgdyVLwQhac06LEKk5nvzvxys1zx4CitsXvmaQwXs6u7gqCkuee5uedzjiI8dxhBBiHtot2izpMEQ9f5n_cFVakeXDQn3NIhMXuF97tUw0kOs7JSeka_haxec8syOa_XRlGew8_xL3Rw7lY3RtEtoCFqumEFlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8FzMwax7X218jqLqbLugCcn6UTCMlutIZBMN2p8x4j0tMmxRjo0VDnCdZB8dI113j_vqWL_3Cuu2NCjToQsaiHo2O0P4giVHbXQqCWN7LNyiVPoKhujbxUqdpJcV8HbH_jitmeGUP3ziFTrAa6CMSrVxWYoEqqEcs3FlwTwfCoBQ07VMi6TCGWpANYGI1yw7U1JeBq0GiKYC53ZdqBmNvYgvC6hA-Who0oFeKLeAHphOS7BMT7F6k6ekY33FYXRE6YBFf2A7y8Mu648p1lULDPvK7YF5C3xvnP2jScj_vlFJIBZ-4Q7D8jhW-dB-0mNmskTC3-RZ9Fg2aQD4-cICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULikcLgpTgs5FaF7ohZPjvi3RTn4UbdWTy_pLmvkIOqgSIVOHp3_vKLDX_s9PU0oloVeyz97pQfhSl53_P1T3RngXeUUdp6gMXNd-RugXrK4Ra-czx2jEr9fCflOVs93_-vsmcDWhNezW_1z1lciXqcoVKrQShn4G7eQKp9GmXyrDyEpTWOAto7ylYuruf0ic74N3clP7PwJ-fj0UgI3mUa1a_JCrfL1cfMznEnYSJ7tjiAg1gax5XYSMWaGYwKnVQEd9sRuCIsacBT5nPyqzwKs5t8pFug2t7kPFuVP0aPhINFkIs64aGavvX80gcv0IduOoMuVa2K6O0ljlkdMyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CP5tGw9ATm9oeHG2vvw7MBB4iA1PRX13paBc5ib23doQzlyOWbPTgLAzHvc0sK5AaJwtj8-EIdU-P1Er5fw-aXA2ErErNSBoHODp4-PppaKWB17CqSotcqv3BUBLTEntseH9s2qfOxeWcbT4mbyOzRSh14_CYGI8Iu5RN9QxiPDItH_5S0Lb11jFb_7J9lSTY-XGUktSl-RCDWzrKAgahAqR7IheFxqIizpc6Ce1jDHO8wSG6jcwPs4CtZt8GZV-ao1gevHoWdkT-y1DFomPQY6tv0GhdII_3aBb9yg40oc2sTctJbtvj6m03M8N2iRwwjBg2taPfn4j0bm2yqCy4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIe092sc8JR4wgiX8GH0ifAQA_xwnTgO3zppg5L7H1eoswEG9aZ6s1a4SZ23zgYqN3-PtrAj8ntdsTnT3B9v6kGc1GHJr1bVKY-IR6nAxudyGS_Mlusv2i6548JIyJ282up360198naeNhEHQbFuGPqYRog65zqlAxpqZuNEv3vO4QkhR0K353o_7w3BuPYBheNqKGFo8BuVRVCgF3oicbOqeeIxlFAjYmhZNH7smL4LkP2MqgG91GXv2YoiwPAGqvpIvmSp3GQVLInyI5aN6NX1oXJIBtLndQTTuREvc0-FPDyNfGUr5Xyef0aATl3Vv3JObvHgWUQUC-mAzYWAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKWCBnOI6IYqqtyxoUC8rfTiKzyZSkh1jS1cUkG2RvagL10EEuPq4bnRzJg2q7kp518t9yzKUjTHpa-7lXtqj_u6vT5Ne1Yf1tXOpYX9pL9R9LNoOlZSb85toidu427VevoaLXbUv6awLC5MsIafQs4t-dEomLXDjjLXTdhDFhFbEHTceKhdvybga-TyMMCpSTqC1ML28yUaeUVHhplZKAwTTZ57jAplCkwRKWIQNZNMFcW9oRzp3A6ENlsBqeyMSy9fe1KnG_pwbrVbmm1jH1GTA03Wq2ypVIaGpF5iKbty17m0X9c1-1u8TuRNruZdfTdVzf3stPStgrz7_8mBMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-jPI--Fy5fEVySHSD6OI6opylUk-mIWcIuq9O9an0pa-V1uZVNrssiecbMWo-XpS7LjY4odq9F1SgX1GtulCNLiaG0QcYZoppLEB6JOay2f9mgbatHMGgokS5o7unBw6MYNAT9joc_C07TII0iUpyLSrdr0IHhYVeN2jTslYJ1AcOxYN-qmb6SbuZ21uZ7TYqMM_WDbv5L2W4PoAG_BB0wl8l2zlNhCI760zNt0ag6l1tlS8XJw9s8pUAZFwRShcXUnvcPqKmadI6YgPs8bxZuSM1tX6cJaoxZScqtSm_-f02pwV8cu0HbGUvyY_0Bt6V_T2Tqh63CSR4uaRcuI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9syQkKgAf7GDRuAQohJqFUhx4TWgYyHNHHiL9Pekqp1lazUxgKN8Px7TgquTHXUSn3Sp9LWG_POopxMN3_HCWzUCv6n6LTPHfJo6yamOyeOLy1OJ1R1iqEAHO-ZqX6KoBprh_cg-fXwqy637Z5kwWE6l05kjBOZ_Dez0kSmhvjFe8PWpmo6B3vq-2DN_6I3ofNFlhmWlvxnzZdrT8Kajz_3_i0vjhjks9kQrHWYDXWYHlkFxAzGMrvIaKyA9Akg588OnjDfv72GfDUoo2EKhXoWNCFmT5acSAw1byFoAwSnL9MiwBY3WBzrtN7KYcP8GaAFEsmFP3gG0dPwzZSwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQj3YXu1qMxTulsUbvRwRbLY5lWaZjydkTpjXDB8cGpewGYgzolonlgRArnyZezUJnDOqAC9bletlV3I0LLuRHe-fsKQxkud21f0UQ_Mfawj7riQEjU7KXDC29hxxEQEQy135sBzAJjRi-b8Mlb3anNKFmU1EprYia95ouoz7U6gwAyayeZmN3hwCJvUj5ZzYCES8ljZfvDL3CuDJEFMnb4a2t9vy8jeBDv6cNoydVFgYzEawVALpZbfTZ-4pDdDp476O0TJh9guownSrjmUDPTvYbTBHuSLNptvibzvsiFRGt8JE1knbusm4ntCwOzYYWZumBON0bm-wZcmru7lfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZhRwYnjv87AHlJ3B4R30JIszJKgsGjkBS-di_YclgjE4t2KsN99hVWrWJgzoEKyPjbSz624pYJZKsOjtmfmLGZtEPDlWEsHLvZTfh0AEqVWw8p3EWnXqsHSAT6CFdl74TL6zpYEY8RRXZ-VdiXYleFOqXBKSITa_K-cDI_uxhYJdrLjGfoIDj2GRjHkAwMK1Tegk2EzcT3HoSceLHWmSgb47mgd-uvdlP_9hhsew6hhjzWf2swo85Czmm1y2Jc6j11WR5qlGpy0CXl4i6ZAcJVYqSqFhPhjYKWdxXATQEMJZUkuaRii18A3etg5R9hbhxzAXAfp6jE-DJaEsjJp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY9bwBGrrXbPJzZPXaQ2fW-oBhm2EnABplWJn3zos8FVw_LPpZZ9aA-kENMoqSE_rUx1QGtpmbu-Snp5muXY9LTPbSqhPqyBuyLueWx7HPpoIJ3d-HAOPtN--oDkJzBciDmhuOBP82JUH43W9AWn5GNlc_08FicePAu16jHsUdIeOO_yWzVKhPCO99sKdGFVbW9dYhU50o5Trs9mA61WLNkxbt0S-hNXE2wzQZzct0Emc-y35uK_U33jk1bxlRbu9BvG10pRa8JDDzi8halwJj4S1kwN1MpK_mWqm8v8stIDmATj_4bWNmlsfbRFo7qRY859F_xCzXOvVy4K5vIv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCAw56jEbG3TudDJB9NbEfUtQZQTWLAJUSOpTK8bCq5oASZh0n7bebemejgH9UsvBzPhUTZTBbn-7Df2fHvk7Kl0yVHBH7WkpYSJpUx7MZYTUbAZW-4TLik8Q5LwlIq5TVnC94w0o33hEivleGGn9ImWBQAHbGL0-waxXFsGPUbq4dl5B8G2hMiZZi0kYS1CRQiEBlnq-64n-n8vRHGmMuNizOBkvCiExkjEIisbrbYQn5NPcOOo7uoyRiS-WFOr0yz7UoT8qM0UufitBN7qPoAMEoktZypZKMGGaBtKlXOURMhryoFgo8xeBM9gItd521xVhDIfHNteu8KjMHYHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI7akCO72Wg4gGhlJgXWFP2YG8_tD1Cj_Ca3g01l-0QBgLmlIz8lZoZ16GpUvQi2b69jnpqgwoJ3PqHP_7p3Zsk6GHFsreq8UPo2ICzVdZlzLikYtmghkMFuomgdOX6pWaRO-sRi_CnmzfwnjGyxz5Fq8Xh9F3TQBjV5Y9TcV5IZnmCw98R2YXo9bOMhy_6riTwkgVh6YyvxnJWe8qKUMdm8bu2GPvg8vGdEnCzLW4FZXORVtFggAwLemLySSbLwIhqRpGMLXsvRQZ9SHFF8deZcnXLKn68vECNp5dtfi0cRgdM59RJHA2Ms9Y4RwP6O9_8s9h2ZJWYeaPmBpW0hmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j24cmZvBzT9Ct4I8EWErk8gXgqUemCiajw9ZWrzNdkcdbCcWd1OENfx3ScMOizYRhJ-_d85a80derhef1c_4jkcitg6KzhbLb1l_0c1GYF0pDsb2F_9I22BaLK7G5_jkqc1NKS8rfJHOq684z6iLUIV8F4yCo35PVrPgGisnb1jWb2jazX8YK4eT3U07ipSDMDxSIKL3kfSxmVL0WO3Q4u9Y0oSUFsi-aldRem13z52dlkXEPuCqFymKA6Pf9eDj8JEX2btMPQjukan27pKuYpoh8oiQN4k8mRj4OSVkFfaa7NwVmx9RBmpishxx9KZ0_WXZ-exdAhCJGc821k4SRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Q9gXGeziE5rCIQn-qV2h1jXXfc0b7rOowHIT2Ju02RK0DfhSBE5g3f5HktcTDAlvcjLItCIyyGayQ7aoBUl4hh6YwO3zcfDvsGWW5Ki96WKwWyijMm0r13aO2kqwpQ3mQ3ipaNG434y4ONNpH_8ZuJEpm0uiQ68x6RaBWpcCasbFbk504paBfNoXIbdOE9bQh2RlztpF-ZlcHQGQNcjvMlvuAKv9oHWgEFZmD_3VXRjOJuO6hcVeXNSonBL1vYH1FI4wv7R9-YE3VTTjFw4mZtd-b7So--xdp4oA5839C3mRmI9BiXcQ-_QpjsUdYpsTcN2CKzR293IoJzaEhQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=IeDpfBF9TXDTwbXA38vLXPonJf8K9GB2VF2MBvGdn7RLlnuCHxgJ5n9ed9iNMXmSoBW0VfTLrmr9hJ1XD87VXMgOdFyVbmvuMVEV5IUNlMZ3et01Axd9KvHKYCDzJ7WKEXtIGHPopxWY3KNk5Iyt6UTd4Qu1HIF_6TSDqAOJS0FawzDebEiy-YCHrY8KJ5OLMtF_BG9eGFFGBaQPBEEjl1yy7NhWDjP3l_EZZWRp77duIKmIr0IwLZih_sEaUzuF665kmCBSXl25jCEsh07eJpzVWEKS7fE1JwpPyPp8RVhrH5UQhXWDK3mBkw2_cHsTOwqeIlSk1ee4SYpGvhOqWoRUQmJIlN8y8Gz7Svu36rTeU_M6Rf-2YNv_nT2Xp18lFjo9yrjIvQEsuQjhCCKl_eBsxhTey-5nfCTmLf4S0KXVALxsVw2MtoD6iB7o4gSprrjysWGXyx_SjdAYxOyxX7DkpRJcHME738d6rczBvipAXvDlOMjGDtgWeeMT1IeEYKKaSNZ8nF12ndwHwc8PKqclgcfBXk-MfVmfX0PcZ5Bvz9t-od1A5pdx4lyzCbbPVdF-j-eQF5biw0CF6b0rPPypgWmOVv8ChRSEmKX1uqCbPyCthBAo3EjRQlbOJB3qsxnirH2OD4fCisUR2kDofODDtnHUMrUK4cZrhGW132Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=IeDpfBF9TXDTwbXA38vLXPonJf8K9GB2VF2MBvGdn7RLlnuCHxgJ5n9ed9iNMXmSoBW0VfTLrmr9hJ1XD87VXMgOdFyVbmvuMVEV5IUNlMZ3et01Axd9KvHKYCDzJ7WKEXtIGHPopxWY3KNk5Iyt6UTd4Qu1HIF_6TSDqAOJS0FawzDebEiy-YCHrY8KJ5OLMtF_BG9eGFFGBaQPBEEjl1yy7NhWDjP3l_EZZWRp77duIKmIr0IwLZih_sEaUzuF665kmCBSXl25jCEsh07eJpzVWEKS7fE1JwpPyPp8RVhrH5UQhXWDK3mBkw2_cHsTOwqeIlSk1ee4SYpGvhOqWoRUQmJIlN8y8Gz7Svu36rTeU_M6Rf-2YNv_nT2Xp18lFjo9yrjIvQEsuQjhCCKl_eBsxhTey-5nfCTmLf4S0KXVALxsVw2MtoD6iB7o4gSprrjysWGXyx_SjdAYxOyxX7DkpRJcHME738d6rczBvipAXvDlOMjGDtgWeeMT1IeEYKKaSNZ8nF12ndwHwc8PKqclgcfBXk-MfVmfX0PcZ5Bvz9t-od1A5pdx4lyzCbbPVdF-j-eQF5biw0CF6b0rPPypgWmOVv8ChRSEmKX1uqCbPyCthBAo3EjRQlbOJB3qsxnirH2OD4fCisUR2kDofODDtnHUMrUK4cZrhGW132Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfTQinDaTFnk7QW_0DaF_GyKuBQHxecnMDhc_Jq9IXNNmQiwlUEDbg2V8CF5Xu3ulFEnBT7bkY4MzeJZ4AdRMT7DKAVBrDra4T2Kt3_bGWJbimFoDkvZW85fWzess60jimd4OtogoCZAMNeW97Px7SADDSwpLxGinCxT7nmV8cgKcF51DVZQSK2YQu_q7vfmlbh-H_wMOVadOJqeDqY_OPCU440TZjNyMRyhX0wF8j_kIhh6bbrTj1dBJNuOcg5HDUqwHODR5abJWFLqGfOMMaqbpkj2oQwFmzZJAB4TI8oJJc-QHy7fc9ZCij-vSreMuNVO5GZ9yAVW0uRl4fc_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=ai73lw0gFsw82qJrie3Q3bVNRernAawi6a-pPDdBAi16ZAW81Sl4U3iROVF4XN6QwZJjaZQ3-NgQ8bLUG7VyeDVqivUNb0fWA6N02t6IxXBIondZHxFUrakfSVld8MWdR1dirDaV6QOk4ZY6BzrpCYL2Ss5QePWa162zXuYWzQhw-qn-Sjw1eHbszx0H5a1FcR7pRFZbWRQFxIY0fpqDv38LC2XuotQ1AB5uOtYWS4WhvAKEHIG291tT-UEUd32bZQAJzE-K6OECDhZ0DxDpyUy42qn8_iBnZ7hb10AlyuF4AuzwHDOPuo6CGP1yjJeMud9EAhyYgxbC-LzJLRmk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=ai73lw0gFsw82qJrie3Q3bVNRernAawi6a-pPDdBAi16ZAW81Sl4U3iROVF4XN6QwZJjaZQ3-NgQ8bLUG7VyeDVqivUNb0fWA6N02t6IxXBIondZHxFUrakfSVld8MWdR1dirDaV6QOk4ZY6BzrpCYL2Ss5QePWa162zXuYWzQhw-qn-Sjw1eHbszx0H5a1FcR7pRFZbWRQFxIY0fpqDv38LC2XuotQ1AB5uOtYWS4WhvAKEHIG291tT-UEUd32bZQAJzE-K6OECDhZ0DxDpyUy42qn8_iBnZ7hb10AlyuF4AuzwHDOPuo6CGP1yjJeMud9EAhyYgxbC-LzJLRmk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_yPP4-oq_IaKtcHL7jaZSTfUB73aAniaFAw53SBLNK5B1LZ2-ocdzBBsnq4Q8mz6Ovjn_fkfIpFOyqGrBWU9B8yqdSq8BAoD0QgHIvBulLvX0L8pe7gArhl6siFzPT3gLRG01kMfgsrcgQtWs1PmG5MxtcuhCeZGcNLKJWB4zq_EqkiPTzThRnc00AEh3yUHZ9IWrQ8j7KRChr5pLNpoD5SgR_K_HAvIPRTSf7QY9o4bWzFmBIxRo8MKXxAcxsXYncISRGrD1g5wEkhofo4JInfjQizBUgPoJ4lWsUhqLEr_zcS2pkYi0AdI0xqXxI89DEQlCEiJv-tR29qZI73JvZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_yPP4-oq_IaKtcHL7jaZSTfUB73aAniaFAw53SBLNK5B1LZ2-ocdzBBsnq4Q8mz6Ovjn_fkfIpFOyqGrBWU9B8yqdSq8BAoD0QgHIvBulLvX0L8pe7gArhl6siFzPT3gLRG01kMfgsrcgQtWs1PmG5MxtcuhCeZGcNLKJWB4zq_EqkiPTzThRnc00AEh3yUHZ9IWrQ8j7KRChr5pLNpoD5SgR_K_HAvIPRTSf7QY9o4bWzFmBIxRo8MKXxAcxsXYncISRGrD1g5wEkhofo4JInfjQizBUgPoJ4lWsUhqLEr_zcS2pkYi0AdI0xqXxI89DEQlCEiJv-tR29qZI73JvZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJwiV_S-Zh86JfKecbb3AoCUsnuv_SMsssK9o0iKlhC20qDK-dAu6LD4UsVKbdWnjgp7k2gBMsw2st4djJcALQ1P0nEvVA_jL82PhtLIelaMWTM4DfH3qNVCYwWOR1M_6lHwSuu_3r2LTiKRukGRQQX3bdSCTCMkLUgvQMi7HEOraVAD94I4XKXV6UcORP6f_HfOb3GcnFpj9mOwG1bZf8Ti0zFGSZnvhlqf5U4s2QH5FdCQD_mWVkgP_C3ijwcFX3BzEJOTF1Si_br49mH9pSHRYyKS2b16Dh_BUosPFJUF6Rnqr3thezN26ZWmM6uAaBchagrfZJkNLcey2NOJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFYk4AgTrLjRyWkl2btTtoNX_9SRj8M0moo_RiOzQEkleSJH2Yvn5TTgNJKABc39f7IUHeZIEdIqez4ahzPA8pCuthLk_-zB7NTaOwJ4Xaoj_P6AbGxVxXfw3u--hzOUBaBRr4qCM4Lg6GA-q33ktydhULsQXm1tBLVn7oinbSLs9ViwMsiD-3pgNNAZ72z9GJ8GmMknIvAKIhaAFt9aLHuuhYPEXQkSd2iS81Dktl8h8CMC0hwYyZLKREXuYgrFQrxs377YBAUnc0L3mglDmSPduV9XT60KBi4Gs5GMBuCg2gOPk5ab9adtDPa5Hrp0s8NOKoB5fLwlEZqEmWZHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDWFOolOI15wufL9lh5fzzZlMCdo_ku93kL_wbzz1BMBSiuL1wCCnstQ7GHiAP8k54MBPPF8QfRXynu30pxF3xmYfGTWA6ESoIhuvHMyu77Dq7HIKFkuE9Xu1u1eMoc6dCj4II31db9WC6SUQKU2kFOhnke256-HZcBZQ_llENADyCLEA0JbAAJksKTvb-4MnUzCkM0UqbIWuI6kmIBuqbMIbBI808UjUDp9zc5SKhYTJacLm-hy3eo_2k1RYYLQw13x0Jo4LlGsEbQY_UaKbHEaIQMN0Huv8eaZHExAgMq9EJaVanTEjILR6bUvovlfJ9DNK2PvduiJbE_euxVWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRkgmKF6C2B3YwOCtDLfM5EI1nesCA8BT7O1LkFxcC_XBUPf0c36tsZ5E0vVdKXqIpD35qNDs3Pwetq_YPV8Dh3DDYKQJdrnaTIq2HjJqwJod0Nq83TUAU6-CYIGIKt2zk5mSCVVV48xfCvrV0jbkxQtL6QF9sNeUje5HOG9OAYrZNG-4mLYpRbpa-w2ZdTvQA93cZmnHw4CmM8Qa5iDckgp2KDWObjkTUcLQ8uV6Tj82yQ8g4F1VFtqCbO1xLxp8or1FiDe9h8BXqg_UW_10vTqBlxqY5RyETa7ThlifawMNyiUgnv7xzR9aF-zzxOdm18nXxNdnnJW3rvuDNSpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRi33X-8OqzybTftlJwT0otLe-lWzBWOoPVcuXT3SGHsvxD4uuh5fDFDrVDGDK_50kUc3uF_HTjhrWylnvTGqA_FDd1RV5FOTuoiLmXPnekBOLVOIM8UaqD3mU1UVGRj85R84LXb-VtA37Xp6l2GPXCpIMPkrZAoMEvwuf1DsrQPtKnRm9FYRWh42OvKiS6dqKxrY3w_bQNvBM2Fv8Sq1Uy1CRy6ZrI1K7AOeM471vM_Su7_1rS4NU19InQh85fNI686PQPLfSIoD68yxuVCPq6AsW6M6OJN7AqIU5KAdJaeYaNoAeXeIa5K_1Y7A04bOeu9_45heYgy-z5RuarAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrt_hyMRM5SJItNqWQrCgTd39wLRvw_Hs6YyHwQXjeeW5HBWdxTNj5AYkiS6v-2IIdhkC6mnhbzd9m0A4gdzbG_uSHlvGpiD8mOsxKH-9_cLu5qR3M3ivMfYpoxv5egeCEjw41YsBIKJ5DDAPKlVfdIsZc4kNtUK2SCVO3burdj_YzhKuZELcp4TkYRSVcIDhgV1_z5OD5N-0teJLrnvhYnLT03F2_88SNcV0iZYEzCo-fTD6oSIzt9ERCLUaCTlj3-OK6DH6IyshFmgdmwBkdWssIHKklNliU4pr9iJauzAXobWff8mbYQK6Bk4ULc8QO82OrbhEGItPbx5EWjUOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRhfLqmGxbtZYRdDMpyrmn4GTnDn2gxFEHRCxgg-yDd9kTHDzRk0n8mJO3VRGdnjuLS1JHnViiDjXVaoL1mSAsuweIu6P7aC3uPXX8vy_y9Pu32uVAEI4SlLd0vcNy3aHHTMGKJWQWc7MGPSPHLlBPF-Y4M9QRsOhQti3bpLtPByWTPI53dXu_rt0ncsDV3nwo-pDNgbxI9F4x2k4HcHE8AgPuUQhgX9x4j-xKuzTuv5JRTqDJ6oZMx6_YoVXTUFhi_hT35CGcUR-p8uu9NGMrjHmyCDoxQYH_eBDY_RX9a8mN4SBjLcZoMtParoAOfkwVfkz3PZ9TDQUrzhobMpSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r43YlmSDwvPf2ndV58pVTqXkFgxL3EkX5LwOdRMDtJIkw45BjJJCbEtz_Vl98KnPRSFINFb3oRTaDZJSLBI6rQjVLw74h5WAuE0S7mg4r20W06h2xPcHcD0F74kAsRvFUc4uxLY4oHuJEbkg_jeyKYFTEnD4i9B1tAPi4zLf0LGyaVsNBryKdmfpcYl72QWOpLn9FxGDTZmTrO6HclQWo6Vf8wScslbX1LEFTrcjagd3HZIrp2_Wuy9TZCw9ILlzPylzXDRIxD2GjGt3Lqya4mcOombzQvxhBfxF20_qolEvgDsKA4UXgZ7xtbeAe6xrD0UOfReyI5EpJr0q95SJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZpltP73a5nFP8uww-dRomhj58HsOJxBXNl_pVGk1Gjs2z7DRrYQxeq_lrYxwgVZJ6VMrruZhWc6zSaMfecaiaHKVEnl9lWCgSbhJGL77enT_P17oppX2Je9L4JQQ_EqSwP_lThxfTrjAxPX1YbK-3g1qQHjD9jtWhroLYl6mYSKkiQfEFymY13tCHsmuQC2UTWNC2_a9Sfv8eqkyQRBdECK0-ZEqZOWVCJSp0Ld1kuLZColW80j6_kNbMkXXUoIjR8ZjOgeeNxSPv9V7yJ6iZ90sQvf8-wwJ4wjFg-aPg72zFDVIHcV_k2OSUUAQVoMxlMwx91w3z1BFpQOGDXRYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXafzWpRVK63CSNiTNqvX0OMpgH3DX8V90huJojTSe9m_T9Tp3n_Oz-pF5P18yqn3joi8sT6nrn4UqsL-mF5xahw4oBgSYOAXovVEr5Tozls_xlq83isFFgSe8PVJF9-LEw8tKN_ZDxv7pUUpOHJGwqS-DZLrDXgcQKQ3SuHlHAxM1JtnKqGBPY9lQvEf67KU3P4fh5TAMaUlqT7dKQEn0opUVBySNESMWAHZQybDwEMyz58s2OocekClIRjcE5xOv6vwOPDrp4U5d_GUZk24n6-e5qP1stnPKdZ4o8yO3IBR65_bLpzT-bKH3R49IqN6PGPy1kmLr40EfwawBKD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUGExLNNA5k4QJWS6x-68yIHyWCnCdFJNJMKB0YclvZe4Bcar7E-ILVho8WZJGD1HSeePSJ5Qg8jkxgYueEh2QUjWOIcXp0tE3oAPiSUBZHWkiarbcUSPyTQ2E4f9h-gkTModzE4Mynkw2h0v0xp5fN2ZCESMyn339zLAHUpsDZ8Ic4_-xGfUvNfSiyIl6gNlTs8VVsbCBYRFj1nGb8xF391Ogp503yrDum32itcYYpCtE7FNZp1XQY7ymgMqXMMyaJgh6mdtLUWPj3F0yJxozYQzXOpVxu3lWzmLJp7g4wxt222-jkE7JGKNvOOkCtR5bnEKTCrRTso_4Y5fuJ9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bizr_9Tk_4om1yjd0pDj0LvPL0EvAagTYKdSv-sA9tw_-H_iJJgMKU_Ub2pxqb9ZG0_d_sJ1uLv-5a82h9S8gD4gI2PUI0I-zrC5k2KbBfrlde9lAW0ss_7sRuRRR4VFhy3qwIByCZ1KHos4UYfaKiPB65HbRpSG5abhg8SX464XeQuUNLDpgCYF2RXVnlPgaagrJoNUCNUDfUo1xUdEZpXwU9gEgAz-Kv0OIdTvzaAfGFgvMH_CbCPPlTcJm5YVq4BbnAt_WRCxhPCtJIUrOmPTjoLpElPviJceN3SuyrOkGA3KwNiMh3D442Hv7thw5wHcFs0eX9mOjxosNIEMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJeBleObrVT-SZJqUgfcvCePMovJCQTgnZzq_elE2A94ivx_ZApTynoSp2DpvQKLFD2Ks6gTPF01MNcysR17Qio5SQLv00x6JzRT9JC8MD_Lbt_c5YkVhhsCxgY-mQUeHXE0mktkpK-U2GnDvAsMvVTyViaP0FTlsg9JU5MCbPV6P6XCWvp7k-df34ZNQuTtWMJJpepxMOH-2TxZZ5uj0le1bhjYMLK_n-86V8Mw9IxLgJPG_5ZnjrjYQ4fRTlEikCXLk2KvB_rJFUbgbQ-TZU8TsNxsDMRHnDmnB9lq1imPRhRjpqceLb0Dfv88E1Boip5QoiXWMqrwiGB0tP1IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTuti_QEG9_vF_MyXI-Mz0XfdoQqgvfUHzp68OUzSdGzoWKO0iIWHAcgpexyO4_rVUPyexCAfVcfu2xFLhOoHjm11bLDdX30GzOjX8y7u6VEVGaduyiTVnbKPdfIe4XOudGQOk85rv6s4WYV5cAQw_sNl7FLiAzwhzIcqcUTu4Lj7GSGL2HEW2c1FPG62h-I9i42zTSzsuPvCCJVe0MuGirCaLHjy7H-3UhyawA4WGfv2aHOrzykWQJjT2sAToPOxNC9nEMgOYcAm_9w-dQ5ahzzYCJaCfrdPFGUBB1m-1sX2oCV8QhpSNVGENIrqvhXqhZNmDtynnm00kMqbczzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raEwb1T6XXdI7xAVt-SbGixA21ln7yBOWqDHJwWPdlqocCcpIw-U-mF6JLq9j6KaN3TQPND8s0WhH63VEly2n0Mo9rHy8D6Z3DIcY6ZPpu-6q38sw1GeWQuV3MnLOOFoZ56vDMSRa2bHp0QPyGwjRuxoEAJ6utvvtuJalCFAtOJqZs0IwmG5st6ab0k6P3NqWL8iArwEidgPIlq-fssKmblLiS-QRwnWMDsMAjVKVgIBwfCxQCmLT9pVJmzqCVwE_2WM7n61Z7XX8p_kc06XZA6MMigQwLZcWIJunQ_YPYwewTDFUjcEoZKduWeCHa6dc0rkXZajuL7CWMeJganw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek5tnUnaTjOu1LvTswtwTd4Cf88iN0qe2-WDYs69uBFHESJWKmhqmvsAlnFnyj93tbT39CvSbXGk-fpbHfQ97AYnU-nd04SUP2kHs1G1g4CCSAc8rwdBIWlvw0Vr730vVkdpEXtqpfTE7Q-UWC8q_56Og5P4Hwvsp3BFQdGLnaTE-SRUdzdRrOq9FBB9HiczXSFn7RPbtgo-nwdRKahxGAxmoyXwoF4-RLZiu0kzKTTVjHtIkk7-vKaFytl5CNtuvoIQIQw9hHSDOEvlAi6n62K8qsctym__wJ1CN2rElYnYRrTONYCG9oYL1lb8IoFl3gVqjN-Nm4wDF7RQsWcFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4uiOjJ0AAOp5xP3Mgfvh5L2GcmSDuf_t0mkT6sgFhnWXx-lkIw-n6bNg6e9fViTtt2hVeB2XCcaWrAWmOsP6pCbQmvIz66Lq4Ulc4dxqWPnXd9wfWYOyHjLSUfVjZgYKESJ5n8P4Mxfj9VSc7SyDa88mgB5dQ3u4vzFHTTuDtg_VYqoT71Mxjv1zDysUpvvUOPqnALfbV8MsTJY44uT-wmPY6DwpL3_FbCSNXTrfHLmtjJA8YtatI_Pn-xcHwN0OS5ZbVm-wQsCFfH-Z7UhrTkYj9KhVmF0iJR8NQKjOvXOgTX-cqfpvzjyXbN1Zq7mXpLvOSOTNHpr4a2UVcCTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF99Fn7a-xwswCm4qjJWFYPbT-pobPJuuuyubzRbvTF3fSbJ14Yac0bN-o0KofCTf-aUV0hn3llBn5KFi76JCEmvVL07ptdc_MZwC_ULCobswKdTt83kv4vmAuP8WVjoAzNFtEoszB68NdDMiejig5AbkxWsDq8cYzLaTZlQpe6yXKcuPI6vlY5F01gTkV04jr7ZwxpnXPA9TPOS5oN79vpprcGJVNVCq8jvp899Jrhul7x0QjWE8ux2MuC5HapADURNRW3K31n2uV12tRvVd4FICdDcpcyqlZ7wLBTPOEMzHc2l2y22CzVbglniFd_rmvf1jZtHGXlXRtONJKp2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkyfSGHdbiSH_6fGqwLRA-ejuyAajSze1GgHsT0gLA5nX1yA6W0sf6Hk2Q-lLAxO9PoBekYaRKLJ7bOtMNzKXfmiUiZDx2CTeTTjhLWw2BcUfGFSWbnW5wTfgrfSySCCWrLFZ7kvoDYeiYtNci5031Mx6LQvzCzk8EeO9J043CrIlRtJOVoKGcFK-hhq0IfMqhIyDqkGgknm792-ev6cHzs97RTlo0UlB-mA4ABXhXzEB9LiRZ5iUUVj5DM_pU3cZCr_Dy1LWdgNZa4XWW146y4WY8sB6jnDBw2MPXB2F8PjJGxT4nAHoAx7uAaEkWc3wnydiOCr55s8XJXPqbh2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veXo-jKuNKRuJQFMOdBFbWTsYKNhuisJEh3_1Z-fiJRMP_lDOz_pSWW20P26VPhkiq1nXD-OsNm-JzoQxMe4y03txbgpNODiDqkKF2HU_aIx0vpkL-136NiT92y58YfkF9gJbybPQi12yTphu2_12wxf2KEPvh7s5JIIza5vQQ7py06NtT9FoylJSL6eXuY3nfQj1oAyJTiwQEO3btKj5VNkR4jvzkUKLyxvzHoV5VYb07-hb6u2mk8mSA7bDodmmihjgwnAvjMELrjZk2ZpD4qwi3JxduI4IWVaMd-dTaJlFFAVliFHOUYrnblbNX29bsqn1YoNnqIWrNpQTLk4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=Tvec9fI5hYl8wOHKshWPuYSntDH19MDI2V5FHbPR6ir9CCXMGlUx1lukXosa9G9ZOG2Brv727BP_WRHO3XOwqPEceK5EmpPwaj9rXyQUdf1zpyq6lffFqvNpCvIznvRwoSDOO4mvR23vWE9vSZJot6oYnAvDqyQl3wivFtapvVOxFhiYsT6xBl0oxcQBvl42thEdrzd9LEt2eafhPN_AfLm9VVcDkYsKnvcxQML18uIvT5N_UCT_RWaDQ4tqQrjdOrD8yarPwTMIijVfcU06sPdv97CtEYPnYQLYknihoJ7485b3PZFjOBLy96Kpvo4lD7FiTDPwNkGj2zAg1Nk3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=Tvec9fI5hYl8wOHKshWPuYSntDH19MDI2V5FHbPR6ir9CCXMGlUx1lukXosa9G9ZOG2Brv727BP_WRHO3XOwqPEceK5EmpPwaj9rXyQUdf1zpyq6lffFqvNpCvIznvRwoSDOO4mvR23vWE9vSZJot6oYnAvDqyQl3wivFtapvVOxFhiYsT6xBl0oxcQBvl42thEdrzd9LEt2eafhPN_AfLm9VVcDkYsKnvcxQML18uIvT5N_UCT_RWaDQ4tqQrjdOrD8yarPwTMIijVfcU06sPdv97CtEYPnYQLYknihoJ7485b3PZFjOBLy96Kpvo4lD7FiTDPwNkGj2zAg1Nk3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSusU9GSvmSkWPTssVw-i_R4rYuFRUY5mZ94IA4RRX2rsAwS2OD36X1lm66inasKO6LJqPepedRUzoVnikBJQy8I0TZI4Rq46rUzjBVWZgJjqZFNPlm6ZSOUqI40QZejuKwgwtXiDccIT_ZOqo4LIlgFtmhdYx_rSyTjhTS4ifNDMXSGRTC1ntoAx4NDz_RWsvHWc-NsotPIQWZym-O6YsZFrn1roV13kE-0Ds677otQ5BSh1m93MDHC-ezfvcZSA4XwpjJM_sQ8ocrzQ1nMnUqXsw_2pXJ1aoUEDtAiMO2rQhLQIErCJTHL4HYRGCj3lMlTCgIVAE8hsNyvBWUZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQh69KejAjvNokCSOxflfxzPscQexcvGlZH0_5xX5Pn9_QQ_MgkKMMAoEk0icdVoqeuqsRvWEHSU3A696rlukBYNwBwdZapX7sEccdpSn_63DEqp7eOdkDoEHO0c1waTW2Llmo7bE6WJwKxZYkZOTbk0wknc5q6-HyyCfkhxBU3YuBk824id8euIylLgDXnFiefDnePFd764XEKBqaE2--adTNlb_pcr4g9hDKMBmpTbBVe6cxPEE4E86e1FH4GPWEEt4VlqH_c9LbKlMdV_3BuGa68uF2PqpacE5znrbIaNYPlYIhd0ygbR-S11wBY_wmwxy_HbvqOKtjoK02g8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6LGzWyUGmUsct1I8wx1qeoQ2x1eOO70Co7rLkxH7uUyYQ0Fa8IjU1P6hRk4Wjqo5Bvylq6YjEwp3-VXo-uRU3WymKH09n3_rSHfkFWYpcRAGp3rmoX78QGZLrcdUfiMU6qzkDgSTTf3TGDDXtkTGHHbyGY9490ltV0poSkOyCUT06k5viHC4xvYyS-sEnzpVnUE3PUNjbBMj2OSWP6DsoU6xLCFozo3T6STonmG_2_jXDnWMFZodnzh6imJR_Ru26L296Own5NtqP3EQvJMrZAiuwWxksgNgD4bnX5lLGBPOiNzHVUL2xZFO8IoAYR1Oq-jtHzPpI804PvYhdAC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3qDSigbqq-YOyxKnVAopcVQphlrgypqp0Uku8NtZJFS60XgeIek8CFJSLkHDHgCELnlCfP6DIPlx0axEc-z2BKMblP38O1aPT_kcQ0gK71xph7ClweytZ5ApjSP1NrGtMMogTXwXWRvyFB4dqtvontaNgwz-4Q6vlGK77VYhEaVqYM1sNeJ8wKnJS205f7FF0W12J4LcnsbndZX8OtbDsLLswke15a1fzh91hPaKzqa6rInaRw0f_QDdjN8-F5i9ThHkbIbv_LpFYIs7n3wKrQ0JzFdlN88341iloq9Lp72uT0veybFKggJKrNbmf4Di6i1PX4AcUjbAQKRdkBaJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoKD82lWa9FFAQ9h47ek6QACmL7ITRrw3CobRtfMVAkIwqVdUQGMRi-QssZd70_bCvVyQ7w_eFpamJYdRq-Q5g50YKiOQCdDYc2DjT89YEWPpOgthD0aG9e0EDhOQNCWwFzrD8zJENOZQ9qw405uwj7D9-pT6SzvNrEUiEkFRJO3awi38RN-FPLNOs16T1B7z0ZTPDLrHl3zyWh_NVHdRmbwIPLdOwJ0sKnJn1V1fwR5UJ3H8OVk_LCLgtWGL-siCUd7HLIJhy3n5A3XMHpOhwpWv7-bGVj0pMRv2DnqI3S7SirMD-Ozy2_IcglBzO6fBXBVHatRXCryUxVJqlzGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoIWuafsHQNgKmr6by0iw1DYosfxULK_2kp9Y3t6w9t2ynosloQ3nJYiGaOE7zY9HSZeq2d-I-HMzfjmTo4L_KppFwtRrvviguP4L0hY8Y9ds_D9P2fwLdJi7YPska9zqRJRpLsabBq7jfJnko6OghNgRXT2UcKHi9p-KKnN2cGl1oBY7Z-ZdioUT1TeKPDMNzZxXOLB-IUa7toUMQnfUvHUra31cbhvKQoeG8kUa3Yb0PqhRlD0iFIekleyptx9zXdE9g-jCu5RT4tMPN1RawWLz8pybQw4S_lpLDtx1Vk5rQKWxD3_lTvSzf95B8QFLvZB_Xum7-1yRRQaPUymxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAokvYgs39jQKMqbB50H7zAoRWezhpT3d9AqkaJ_JNZZ-5oiTXOdqECWBlM4ELnXvDPrG8R4JK8Mmy-6Bvz9EUEUQukQVPUPYyB7EGzt5hFRurZ1sbExJoYRF4vhqFIpB1oxFXvoMkY1ybxcFo5EADRjsYor5ASOm18wD6MvD1aTdViPWlMTi7T7UqW9ON0PDre6rXSUzX_2I83rUV-ge4RqsanprMzyn7_FQ6arPOjGkXB_gC7CkuggxvuiFv8Vri0ltp5jIS4aQtKRO8-76tGOpn9OoTurFlG8l6b16Uv44CqyqR_KhUYre1mPmkUsudnLY4PUOPHtv6retKQzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPlzxQnS2Xbj0BuqLUbLEhjhILNg7wHkwMtu53kFHSsW_KZf9SVgn6w1XTlk1mhSuCvQzwJTYzA9AAyV2ybiiSF4YJd31URs8wk4noSmK5ZhBr81W5CTiUEjKZ1qOMuBqPkVQigtkpMepQKlzcalJwrEU_dKa0gmxrg9zPCxU78yV5qpCpfvPKBd_-H_ti2uvQJsNfnKUltxbSsuMn8RBWPi49Y2EyTCYkI9SWiND6hokinSwtgCRGMgRY3ICxFVhtybBFpOGOUjSQASFYgduqKJESKxTy8wOAuVSZroNkCYKWgrJEXaBFEaObRG_Rf-hPtsjSA9Mh_aBKRAU9MlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfIDrugEnDVMiAschoD51gDNKxZBcr-5HCxfpDeJ5gtMyh991PBVAETxshqZ2rtWo8VKcE4vMwalzDSTP5szB252vrXf39lHMWIUJba1rLKsJKFOcrw_RYq-YMM0m_r68NBfoy4FgjbnqCn8W4-IbbXc6bQia4vJkUNQVn-2g0iN17t530sOKOhLiDAhefiBeCdqzj56n-4TQQOkXkFkdrmjQcsU6v2PCDGFSskFu5wvh9uzXPL_X5ox2m0CiH_5CcC1mLs5-GUni27lmupnb3bYyzrqIiGHYVT-H7X4HPh3Uw6jDYCPAAAYv8HtmWahvkNqpx5Z4FbqeTVekKKNeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exsLgsvFp6neBlNLeSikXxuTtb-wUZp3xs8TFEjIspgbd41k8VFtlMo-BQZgTey0ba_tkTotK4CQzVeeeMcyZfEeO52cvFwqssbLQBAGYPhAIcjs0XGvcVioq81jeHlKu-VDqWtNBj7xOc2dY7KemAeh8ez4h5OJsA9xTk9UiPyugzY9ouwzG2iqO4ZkIIpKygbXUgaN7J1CtNTDqxuJ5YweynnbVyEfbSKffUy5VMxT4MfjnlwJXCPnbs20kljQNu3lprFGrmebZwXGdF7j3BVDdOsfBAL5QkXQKgMTj_FpOKPcZjJGgB9NW6BM6ZacbnJW-Y0YhNOwESZjRZzZ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pcvyl_GS2t5ghEHkpiYqUfnVD3-7UFFaoAI4svRMvnPA585sjntbWXy98IOms3c0erpdu66qiBpKtQtaySVs4GUjb7Kd_KMxohnvHGcOMQYgLQIcOZ4cSg1pYlUkf69XwOEDwkkM3GXdXs3XaThex4omCZTSg0FLetE_7gAj4O4gCqBclymTcC3U6op-WgbKBoKjlI4jKPbPvimJ8jo8gVzGtIEJj2QGrzZ8c-zkQmt58kyCyBTB-L1lBj1EZWuTxrLA9LvHGLmrM1VKo8CXdDkJjQSMP-lWvmIcUVPsRFdXNBslbR60cG-fPOn0_j3k1p9xhaNCUyYfMwtnjL_ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLLgfHZSctAD13UF3_Dhis8G17Ms1N6ZRlMAVEmybVUXsyM8rrKaYg2Jo0UaYiZhg54Prvt_9cz-d0IdraYwkf7iaMxmMYOPxr3-EMRaIz7txtmLT1cuuy5JDS0duPsXhyAd3ZG_Mk2xD3AkTdI9uxRXavodjemwHkw_GtNJC12xj_Fa42in8SJXfZZi_46idQ8aF72NyJvroalmb_N-HxM1MypRMIlV_Xj_tL-6FG5mzMM4W1HLchEYbYxtAeTNq2ikRfNECJwtvWeY22e2f5A04TlTSLUIM6BBRUR6ihoH7mQE7C_2ou-ZC2mLPocOUrUvVnKlZiX7a8d1xcE-gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIWrFYjgQRUVV1JIO5cW6vB4Eu2B_FZv3sVH-Y4jn9gSjqsSeh9yD-5aNicCUpRMn1AGIofW36eZU8MdCkwJFdbihY5TwTLMslHShIF1YWteXFQw0F4G_Y_OYzHgmyW2vvU2hrcmf791mGTSFajcOSVYPxk0wXpebWrvGm-kZcrgUIwQZd3d0namSH8ONCLjt0Rq6YH188OgeLaELcztu9PgWQM-83QxMv_wxN3CGc2kOyBE_FjSVgHwuj7exqstNUwEc2fBqNJojqxahAonBtjCbgTt8FQMuuBzHNccUTS2GCWzNGIBahhacDgwvEH-GHMEb1VLlvUIMkxL5tNXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkRcNLDdw_FT0SIGj6-U0DOE_XQI7DZT306VEo_X871UnOdB0vWFvwcCOd3w79RqeAvFWP5DkVC8xkMnpr1par1l6rPg4jdghKZiulbh4SdlTf_mKjOxaeLp1zd_7Ue_jE2SZ19AkpsF2Mo8BR133WIx6Oxa36NCZOtUJizdEpT7Fj-VEkPEn2Xpptq3sh5P0sSnEf7BoJyFyQEpSCOaLjWsBaoJhlxkArNUDP_92nXIpFYckiz1b1RKDYjhQgLC_iBcxZScgRFxVZJHTZSNIHmNjKUHigYw_pKNX9h4P1oNwjbyINySSZPnpKG4n21fll3zSh8WEKZrAjoYB9aUbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDVX0Y3bfR6G2zMvJmZOLnKrZJ1GwqQEQa6huKGye88i6MP_jcBGcP1fXu3pwI8vIyDZgXyrk5AnbYSVomrfAybIvwm_aoMdsQzt-YmrjYupLa6P1dFA_iZ-zjK2guW2ajvztP1MDuN3yvXZVfyWFLGzyRqJ2JRBXdGJcp5GWF3dSXxHKTNXr-0JiyZcZLYAmYuE2iv1XrnHT4wHWJjXXDD2NCh-P80g-uD-UbnkF3q3zMOgeBDO1L3oPIQmetP21bY14BqaUDt6z0kZ07ShRY6zQkL3xCIaj7fc7lPn7PZQJj9dV6U_BzY8gTJqIhffua_Byx6U67n8znOznc4WOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKTXa7-LWA04KT-YNuSl1kFKLTQhuCUVYlJEFGeYucqpnhM8jIi1MnJSk3ZvjVXOBPP1FWEi-WL-CLGq0_Ad5HXrIOiMtprF_wUZuuLvJCS9jumiWgo4Ox8OZuQnPuTqt3ZcKyPrg_JpBkONVXdVMxUQBZE6N4sLta37uPQIlMKvcEdGYpnWnB0Z-A7lW88SpmcY9sZRfjE5uPQKy3fxB1SUj3Rrwv8owfhg_mfmKAgQR1wTER7gA0h1VxNi6Pphp7xOtU99mgFri5syfupDwOlbsT-d7cHxLHO6zMFzFCC6DQuYsKEyMhSJ3Ri3GEKL9F5aq1UDqBXY18llyR1OnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE0kIoaje-9sXA5BuaKRQnlwyEaxHxG0DMfv1r60h7Lqwc1M_rNouGR3OX5Vi6FvJC5MIXYqbn9PX3x6NIahv0o_g6kLaXbaqr3vvCaLTugADgO-QlWLseLjN0gxu_LYjuwpcVvVcIilGba08jrDf12mZNL-dyHdUTvhdLTmeUc2tVlcNdkCAFhvSihjLo4KkHd1DcPKaD-rzG5eYVZZWXdIixlR7z41DILNbI3AzVyuV4Xo-QsprG83s2HjozaYnNHLsm_ZORBdaJyDRW09KBuCDDyUdO1nWhn8m_kAQUwwX7BEZif-Tyjn9AnY1EBXE367Y8NPJlAn2ZqN6zaUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWuSeY5UU-7dg4XySFf4LRhXnaJnE0F7Kb1LyH9U8olbKgnJxkCMa52Oa9df-OUkZR8JdkIewO3AYxN6wjekL0mU-svqfnadisTxk5pI4tQ8wXm_Zj7z6fqax9KRAItdJog8nKS8Jd2c9b5Kcdw27kmi2hRohn38Uav1uCxO1CvV-K_4Y4W2aOgm9i8IjeMEEp-ce_8CNeO4RYa1boO2QQpamLDSNimvjPYxG672WbL6ZxwLupP6SgjZXNhaagR8b1bdWrmY18Hft6EUKsyby10WTm7iugRx4SMayrS-Lml0gB_zug0-kPsyUwzsLTIxiWsAGKvH85z0zcBnnVL4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=vjdab1w6BBXysSxbFS5BjPK3z3JcHw2c8-9Xn1dJ2F1WvGi7a5kOrDt_rJP_IVLpxYVoJojak0MsBgMVGpAQWzjMb4c6N80KA8QOgsmvOAz3O1PQnYz3HUUHHR8bLKXqt8Fx0nej5DvzNQvyLD_7UI-eElvkExbup21zNEJqWeDwuJgc8pmFEccI529Smj38wXmHrmzjGVCirjsC_9w79G7XtJMJfb-zCKYgUP1gogWlYAKESESkDyT9mTcqeTM27YKeVU3X5y_PXfTDgJa6y4DFdDV3NmSNjMbG3m0IQK4nahotB9ZLwY5vxZ1v61wDyV6hwjkEl4sw2rAbC9bvPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=vjdab1w6BBXysSxbFS5BjPK3z3JcHw2c8-9Xn1dJ2F1WvGi7a5kOrDt_rJP_IVLpxYVoJojak0MsBgMVGpAQWzjMb4c6N80KA8QOgsmvOAz3O1PQnYz3HUUHHR8bLKXqt8Fx0nej5DvzNQvyLD_7UI-eElvkExbup21zNEJqWeDwuJgc8pmFEccI529Smj38wXmHrmzjGVCirjsC_9w79G7XtJMJfb-zCKYgUP1gogWlYAKESESkDyT9mTcqeTM27YKeVU3X5y_PXfTDgJa6y4DFdDV3NmSNjMbG3m0IQK4nahotB9ZLwY5vxZ1v61wDyV6hwjkEl4sw2rAbC9bvPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=pr1I4u55t1vvmv4vNRRtKepM2UwSBIIxY7fhaBpFtYC0hPDMH68YmOH1hbjorb7ihSfTEQaFrRsjZB_juJTgNeasaWPfWMlm1Pv3BAC-HaCjthxOlmy8G52I9rheLGOWNViBtV5mEP7emD6UIVdRy7RHXluiJFFfcgJ8Jmh3gpWO3WvCDL2KWexLFOuh1yN-LgaUX4zblB0m72i_sCILImXf3ar0rPRnDhRJ8YABp3NQKsi3nJ0NQibLz0X3E4vxKxj1A-Y6AO89xlz7qec4SBC0JxiWKnM2H45zu1XXlPVwzO_DQaf2myW9CgxdGoExIIUBXb0XfMex0IDWqBlzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=pr1I4u55t1vvmv4vNRRtKepM2UwSBIIxY7fhaBpFtYC0hPDMH68YmOH1hbjorb7ihSfTEQaFrRsjZB_juJTgNeasaWPfWMlm1Pv3BAC-HaCjthxOlmy8G52I9rheLGOWNViBtV5mEP7emD6UIVdRy7RHXluiJFFfcgJ8Jmh3gpWO3WvCDL2KWexLFOuh1yN-LgaUX4zblB0m72i_sCILImXf3ar0rPRnDhRJ8YABp3NQKsi3nJ0NQibLz0X3E4vxKxj1A-Y6AO89xlz7qec4SBC0JxiWKnM2H45zu1XXlPVwzO_DQaf2myW9CgxdGoExIIUBXb0XfMex0IDWqBlzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVRE4qyZRQi34R-oajtbx_AuteSXtTPiiVdabpdA3Orr-Chq9Xqmy5fqEvgGyZrvRR4iT3h_YqCpZH58HEbSZvChzAcalYwiXjYsEvc13XATC0Om6cKHD9HYe_Tq5dXmSsvgyHdD4mF4wtYUNZBzBKWyJRYASw0KoaajFgtsqXMQ6Z7_Y2-JOKPen7qIKB91B0nDaXr1IyW1UA1InEnawOapIJ5rdi0ME720JeYfqU1ebWQvfJ0966EhgHlM61owesWeB5U0TdjXcXn34agY2ZmfB_Qb7IdowNrZvo8j9S0R6wYseDmhBlmmHoU2fL1-DpmLM92vkrD2Wy9Cg1OIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7-Nxtavbd5Ki11eY9n-i8jIVzcTwwTU_F6HkOHLfr942_14wT-J_uSViO_QOD6XyvxNd0tLS2tWy8wg8je92Chltks5B2Nifkyr3MJ_6HeVjD5jSjk4U_Ua3A9Usr_hnAF0nQm34CmVvPL8OrArjN-0YpFjnUJ_3TZ9WETxjesXpPT0KAHEh-qaLtqFdMu61elVFZ1PasesKgQzLqGqpA-08DxbKtgG3Id5IL7_zBRoS7a7nOZn7ETSJ-mWe2tHvxstk_g5lV2hl5ow9RLmp9BqvgEwNi-rrFU3odH-5FO9CuQ2fn6bUuveGORylJFpQgZVembYZ-0ibktS8RFw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWAhZf6VzjWNjKGYf2RWPsscr1qW7MTY2dRk4blZeYxunMFY5sEwLm977_tOEfXKM_ClTuDaby8EHgWAsUUR3gMQk1pAPUPwSk0cClW9xL1bDsZzVCTHk-gSGuxz33lJSPi1D-PSsZyzvtAVpK5cTevDRx1sZpcHJMcGAJSH_4DRONRpf8vcfoJS9r5KCqOpcc1D74Wo85QjhTiXWO3wUgtT0DsbfGbUT4PEZpe6xHknBdLJ_7iUXXCImjxKmWXvA9Lj6SEdDtHUOsD0rYOAZoOSjMliySv-s4jup1g_5pXBJ4QvaAF4xfqm0S4KQiRxuIk5syfq80fmsw0LyyQQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox5IgmYn3pQQRavpUbh-J0vzAxWIuTM0Ibgtu82qapScJ20buVa837DW-5B2GcaE0TdQHpTpBYq0g9acUGDM_OTYrqejpVJM9UDaFTVaLYIyG0p1LCXITzJMTw6qhOvOBuhZuj_rzuU_Okd5D6ard7-nVAEsW7WkjA1TkTKGir8cJLV8o15lL4RE-jMazANT_ftevL1oeEn5gKUIe8JtcRq85EdPB3vNAClVbAcWLdkWf2kvpyXevFB2_tmgc4boO6f1P_opXM3ipKb-Pogj_mwTuhhA4VHYSCQWLkLxPTBN3dXyvQminUFYfWesnDl_K80aHtz5mbJGarUCd8Pt5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBNaY79FbWJ2uvUsoalDdpa1Llej83Qab1G5ckIQefNc5qSe1l8_sk2XV3NjlkCxnkYfae8j4e9zKXJOYNc04RsqpRcjrcnsIsQ1g7Dh5PpA1dnsFIUlHTOvUu0HL5jToHFG9euneTBuBHBHl4oAnQN98FjTIa-JKinFzvKFZCpP5p0q8XMhAyIqi9DpUF5qmdFse-3JVBRGx8iGuMxivpJ2HhYTu0F_hSAVfwj7kOOcgZ-EPluuwEzMlT1w2QsZp9pXP6amhgTBibDhHYZDQq6KVzyzefwfQ_qO2lj5QDyld-xk6ZspQzcaVeA0HGoZcWYD59NiS2FElLTAAdmkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ4Aiwat1BOyM4OMVznOrnDNLt3EgWFr7R7crNaMHrw8n0klQ2-zPmNyfg5nfQSPvBxui2coA9x1-bENgKuLlDsxyXIxAWfizkHbrTRwI6rBu0buBJV05T_8hLxATClqr_4MgxNOzPTjZGmI1zBz-hiJ6m8kmUCNDmFvwSO2IU29mnHelgicZ6XKPsvEwtWAksCoVPFkixXUAGf5l8dP2pLhBHT8aAQHhb9Pp3ihVeVG6xTdJJEr7Qb8LG9shn8B-nY9w9ImZtV4q3GeYiiabVgeHrnFT1xBoRP-l9JIUXKvpSpQfhzJeJSS-VBk1OHuCC4aiQ7zztM_ZiKuLpWdpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUKIuC3wEpMyrznEudLBAwqsnWZyei7wtZDrQDNWhgBqRYEdmxc-sT4OLnJG5upm4AxoFG6_ctSx_3Uh4wFFnrDZB6cMO0P8eNlDKf8PuKPiSCBkJJLAh46DUd-Gpc5Y6UbpxGu_xgxEbZUmDmhWUbO3ZafIdwOGh4uPkdbx7wQU-xKTI4NxUo7zlSAEUMyTZcNSK82BKUnsdbapwEn30q3LaQey_vNmUvZgu3zCiJn468xuXlHEsOyXiewn6pKUenA36cBbKsAdrcv78aqIFaEcx29-HDX14Pt1ir8-7p7sHdoI0exgP1teywOp_DFoDBh6AjPoYnwAp5eBKMmVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0tHdATCGlwgRXabf8a1JGou1-LMbOUCZvO-fgbjQ5a79SAn0GY-juwSy1Kpdi9pfHwGO_Lr9qB4rL4pz9RjuZrXo-7KZkiMBuB_8jN8ZcAiIrbc6VUURyYrsMjUzkH-XzaRnVpJAgL0Uge4FYFlvk4qFYu2ozMpiyAiWKzEJ34T_3JoBuUzVZGVnIumw_2H7ax5zEeyjwCRdcztm9uh30TREMYdVzIrmQP09Guy8HPcTg-OBhvOBJPeT7z8CyoPjPfKWDE7pnd_kUdaDoejEi7hbVZLPoCUF2mdTe-GwatchbfktHOvnL0QY2SWriUyuKe19Vp-4GOti89vVkzbMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrJZiQsO9MosWY1PWKOgOUt9DKh_UtW1IfydN6-BPxuW3BXZS5lAS-fMj9xUglG-qvOC5LmGrwCizMI_BZeNtwKjRzA7RSbqQSTxq4ujHIJHr3PANh7wsyn6t2rVmX-63yBcll3bSwrmvf8osnPgawQ7rtID8I27KHjzEwzTVQbZcmuLudeZnkZFrFu-lm-pG3ctM9mAG_EZhH5TaO7grGLSpRYurUyyCOR8x4DS5ttHx9XDjtd4SEEsRjzMDTCCWF1o1UDWvZ2FudF9F7ElICgl-xDI9-a5jcJaSsQyCBdkSrtoe9nhUCFxKn0bub0mSiN51ks8fit1BtuGirQ6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo8NaLz33KidnyT37MEwekm-p1-Jj_BLSF6Aes2EMz1YvygE6f9N_igapCJCNkoMY4YXvNaeA1ZZpY1oRo8YDbPEH00A8LIFjm4luRuLt_QWy-QIEgxq-0XoE0aHlNbg0a4lOFqLoLZc88uIsas1gIcce793Gn2ntA4V92Y7RIsfyJ2wWTICoRJsWekkLrYjb3FSryTogHMxpKTHsqu5g3glaZBlivyVGPLcpg2LhrAL7XYLcNCK156Y7gxpARTMg2jMlh7CcUgenFaFdsgJvgsOvynMYfg5-P8Zw7ULogRXmgal7SN7JKIC3GDjiL8EfbE9Gv0Y1IEgCu-zDQwAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE3Ia7T3rUWRmyH1MRhZ7V3ra-M25cQ6qUNDXIIFtYKepLXpEDkO7mdvsbRY_aoo7McYFT8uXyldtHZerkHI21oXfB28Il8W_ckdJ1y8-YaWmlThUUvLZVrq5yy13zOI526PYtLrS2Fzx507FvnYb_8mP-fxoYIvkIuq_1tiUHQk1gQyUaOUwgaJacU9WaBM2qk_ltfRg7sRHRsRY3gpU_FLX8uq86mHcR4RgxLEynk_r5KrMNgn0IaSmHJm-xpwg-rflwAo4_DZScZkHY3vyIBoyMzntDqVkbhXMxSlKkzytmf3k5s8IStidq3UMRR9GL3-HWwpXd55xB-wX_L7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQ3eE9kgvpwOUXtFm7kugUaWM8S_D55wJNs5sbl5tBd2wrjDl0kDQ0qiYvFKiobzU-NLmQEVH4mS_5ROIHbYATId3yaiB4ItiqHoJV70_oC3BXZyOup18ZdEl1OSkQtYlqhG8qJxsoo6k11_oQ7G_yFqTjYuw9jLHvEpliHSZkUzMNtBArMtxFIeqxAPe-4tCBrt1d9cYjHqdxkAv_D9O9BurA3edwhxds96J3GOxunbDhyIDZ8TavNeFxyFzvI3TEc93VsZYarFU3Tk9rEWzxDqiAYqkwetix265vzBIatFpRAoPgMOg9oaIovhXQgkFK7tMszq6vPZtU9cX0eBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw62KnSY8JX_q5RJ_l65MDJwmX0dOADSk7gYHFTysuRcsBVEGDCH6zu82yBF8JC4MvxRCYQyDNFZg8NTId-hHEZu3g706o9iTz72GrAPjRbzBDthjCqIpQC206UGtyJz4WCZXCjUHaO6FsL2vzsjPREkmU6RtglkVTYB7lOz0IbGP_jpn7ZPTRi4i3VHVol9OPURyrqwqySAYB7AggB2saUJKItK0AoYyqPTEp7qDz7g91pbwJsCIG-zK8EKs_YFyUJD7SIPVu2j5XYonYx3Bkt6pfig3bMpdFPAIv8NalgJDQnZyDWGJuBVHz_3_kVYaq7QCDAtVB-QY-cemHRJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbMOeAYiZwkx23G2WfbempHlBww0PgNBti76YKLWIlqaP2SuPSP220Q5nNvUb1Z2JB9C89_eQ1FoWfNjAn7TaxfGNyp_dpbSvyuRrKACqp7ZhjreVj5JDjrA4HEnWnv5JTjxIjRxUMzm9r_32tIlYQAc4rKfpSr58zIyIBAnlDQM9GPxECzZO-U2lD5quv68t41Qs2hIc9l8MX_hhKFqbnMbu_ALLmpTF81SqpGOQsR0camkKC9hT-RpsJzlUqKfngaU5jEHcd7V3nX6s6DpYHy4sw0hPtJ7iLMRJ5e1obN_j8Qw2nCiXhXiRTe-fDKCmOpWU_v_xxDcHknVwUPo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0YoDxaLbJ57-kd4a9WbtKIs2IEDAvCTYSJnG_K3_-3p7YiqTwfS_lmusafcP_TpDbg5CCsc1DJ15cwpyL5qrVsgZ_P128xpauM-uR_vnDiNItwujWM0oMPP_h2XuVO_nhXZNEkzn8d1_TW25rWu85JmLOygzXAOoRrsi1qJw7upDOHcvHBbF2R7AADhL5B2WWDcwIEK5WLCN5MEqi1usuc34DDxELs_oVce2kC2MufrGpI4PoM82fEjD95xCBN3iQYroJ7obTc9sS4sM3_v0t9R2fL7vWx9WC4hAp8ce-wFXzz2A0UqA4K1QqS7ysKjwO0m_La2eRqwo7xDe4SndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAJ1ttvz0qi4qsqxncZiF7ECEkwZZxei373IRUv1iyurhSALN2erEPmoAl1ZkOhO9fDCDBBv_v9g3D1mvDQQ37QJb35nMMY3P3UyLnFhWoR1iG9FR8brdjP8V4vS54ZFbfBqR-e4JpgFoYvwvN25IXMF8XF5AXmYisuK8Ou-SlIWDjjJQfL7CHtvnK9HyXlLTa3LzLYzvwhFd65jkSpv1wR0JSsnVMd54XmL2Oi8zLbQaUfUdBzgfsg0ZVczn0tyi-2PFUIIwtazE3oSMZs8fv8wqRRd8q91TReed6YwMvU0wa4kLFOU-gjVtr40UBQ9TCxaw5ASGvRU9xKrq0tLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYUvoRM1OCYFERpPXcLx9SEvFfb9TWY8SLspySeKsWAJ7tkc2TNmYOTkXz59pq6UOIqbxitSJn2q4bofv0ceKN49_Og-1e4w1ZLkAJqNzz80rpm7S2qieJpglReEaKsEDifnc_rXmtr6QkGRYcz3zOV8CR75w_AoiCOVPm3E_7hSYpR1jii9CMe5Q5spX2m6UQ7QOU4mYPrRWuRU9hKudH5mmlYztELklvHCuulAAmk5Jngfg4_gCeG9THODetLbfTgEcAvSu-aKD5tn2nYkF5kxr2caUkxNZcuzOewJfDqKcMWnl6v_SaUYaah1oLoBqPZcCHy3JT7svk5_xS5zPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtNLoq-PDmvk_uXCFxA7uRtILte4w0GRi1EteD0ol8Dx3LIIkEtCStN66fGMTmCtmm7LJt3fCbia6YqWMw0gbWWmFJYkxHeIwHCU0-br0RMEIYvlWTcnydb6ir_BqpOFQSDpVb1fv0Y8NMV5b2hbVv2R56hilzHhKvYRAyr6GjAqM0l60JtTD7RvnP2mVw6wQVZ1gP0UhdLR3vZ7VNWFXPffhUo7hpOTvl6FeMgXDM-bJj5qjC4tsck5xWoZpfwXQbciOfEDWXaZj-Zo8SW21SHgli0Yxfu9WWYApivn8guVNzSo-i1-hNcKPxH3Gqb9g0JspaqbFNpxqHzuIQoo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBcc4ZGoW_PVTPzW0ZNcHB135cb2NZ3KAuGvVJMlTxMoKjB7fq0_TSSQstltfXsg5sDxvhOZ4zpTWdv63Q6Pyc0_gEB42qwxUdjLgBECUurQFFFlwmlfmBh-dp0_Gf-o1ZCl2KOQMXYKcKkhPdnZHdLcdMS79-BaqTaFy4MoWUwS6PTMOxgS_k-D_78QpzAg9kizqhqOIfOEWN6O1N_Y3yU-Dhs1E6w0Tkz48epi7L5A3LJaKj0G8tEppWW1DqDB36JQDZntwRFP-JVCS2VfDeX9KA_5J0qNwxTbwkNC5drQu6KTZbuIax2b0zNrElnr4rYlafukekTBwznCisdyoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXDMlY1iAabCwGaOuO5ZdwzteDg5GS8fi9cgyKouCG5e1O8nCffvgtoBdkBmuRBaVUNP0XG0sK5r0doltfUx-VlzRHytJH-94r4GZba3tXB7DD4v9e5Wc28wgk3T8s_x2PsTWD-rOtd1mj_6aVsGSHEy1t5t6w5mg-7pVaGv0uNOWrF7ssZJuD8SwINi-nYi-OADlyoysN0exsoVZ_zjkYY-JBqbqqQVcAdX_Licb3xLw5Lxeas5nfCOuoOyR1eG7yXYg5QwFmGQWyclL5NTd_OJmMXzYT0BIHqrG9Rqv_OfL6HzX8HMKzev717s7C5WLGX9bBsxFLLT6RWwj0vibA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=mZ8BGGQWaGkw4MCiqyqUtOUqKzApi-m9pXMtn6MupFO8DLdJA9XEt9d-K82MgSUomyHUTZwW38BB0OqdTFZA3lBeUMPqlkfOHYIqvSFPNyIBsedu79C6H4_yTVdoW424GXR-TpgJ5kafEC0nMyFldz0Vk52THJLSBoqVQpojR45gB3cjq9-6nqyoD5CEBPZbjz3MIyAyhkrgrqJhdzK93LOE7PI3mugjMh6Pyr_FaGxzy3Azw0PU_pXc0xN5Y-MJgbnFBpM7jo_bVa494dsOkJL-lkpx5qusKYokWOfLulIrHHaHLSY1_kQiJbA2qugncHmkDFcML1mbJbDzxZGtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=mZ8BGGQWaGkw4MCiqyqUtOUqKzApi-m9pXMtn6MupFO8DLdJA9XEt9d-K82MgSUomyHUTZwW38BB0OqdTFZA3lBeUMPqlkfOHYIqvSFPNyIBsedu79C6H4_yTVdoW424GXR-TpgJ5kafEC0nMyFldz0Vk52THJLSBoqVQpojR45gB3cjq9-6nqyoD5CEBPZbjz3MIyAyhkrgrqJhdzK93LOE7PI3mugjMh6Pyr_FaGxzy3Azw0PU_pXc0xN5Y-MJgbnFBpM7jo_bVa494dsOkJL-lkpx5qusKYokWOfLulIrHHaHLSY1_kQiJbA2qugncHmkDFcML1mbJbDzxZGtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzkapmM3iPXKcem3AFra22X1GKL9lRBIZw9BQUBvLvC5Ep0ACyelQ9VnSVvnIHFRpr6Hi73Zx7b6ovc__3v4PQ7fnmCGhT9VqCBu1n4ngl60GW1TmJBVAVm5DXdtMJ-wUmMJEfATMZp4fbEUioqrCJeNREuxVzugy0R9VDyGksJQ3h-eX68ugv9VMWuD9IMZMipZpoLYdpvfXNEPxDNK_JWLm3MCnxS5Yb6KkOrNv72OYdcYrzY-7BSteKutt1b1s4Le4eesvxCoYpPx3k3puyYgbR1ORHUgXm7A1fQvJos6hZGZTnlSNfUrRC6lUbYYGj8BYS4_Qwj6B-CoB-g6Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
