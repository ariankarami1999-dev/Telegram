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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 665K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-97448">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNlN7KR1hT65z1F4XIb6lpqUKwl-ZSzZKNkGqntUMhJX0JYl-972Ze46TJVSiBYH5QLKAEphpJWFtz4pEJCQlOKIMgYcR0MXc4wdHt2K-P-6Va9yctOBzk75founnHg0sbWLaOtUGOpd-mOoVI4ByJ_WgMBh-4XjxNB3HXvUzRND5kXbT5UbCJRSB_fYf7TSOHIOxthU3WDRAWrZEbyq_J1o8Sf7R9Rhusgrt5fTGESpGt5HRitp6e98J9mHDtibxxYrjXSts-ulxiSG0cF-U_PP1IeI114NQtiCuW_wHDI8oLjioAESezqPY-9R6IrqYyvfVebNRWRpv-3pTAn_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
خط هافبک تاتنهام برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/97448" target="_blank">📅 22:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97447">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇩🇪
#فووووووری؛ قرارداد ناگلمزمن با آلمان بزودی توافقی فسخ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/97447" target="_blank">📅 22:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KHcLAZIABikBDTSVHRF5fePgFYfglLqd1TjSEs88EM8xM2lIwnJVUyJ3WRHlDqaBvZmvME89-nogAWeNvAJwLB9yDKijDiY3W70bgTraHwKHfpBTbtShDGfrcsiCTsU0Fm4RDaHcJk6vBw2U0KPcdEp870Li7mGf5d8bcvJ30QgAjqd-71w-8Glt8J2FVVOxxUbZ2pQG1gJ4doVxRxvfnhvdqWLxhXMD2eAU6XTrALuUxTfDfMvEhY_-vOVPArnPXm858dH4rKIpnkR0TEOlFzGUYn_gVOAvhbICMpt6-Vczz9GA1UWDivcFK-R8mQnH3iO7AH7plaxZVvOBpMik5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V4qyVfu5V2Ji_2TTIlThUAVz7V6xvW-8_rZ2PQpUt-Kz7vCvGK7oGJoC-_BFcrhA-ZoQBixAj813xBfJ2B8UrY2pFlgUZ-NrNb4mN3cGs8MxrERyN4XlE0dwpambVsiHNWEIJ8C8p4nUoIfZxmFlzemeCtbugGBojdpxs4o9VujS18X3jONeM2H2vJarqKJJBY0og1XaoIaUAlghUtktSKF4ojMBqb4hN4boZhsatPx8VqjYvhlyq-gmOhvzJRiBQsla-i4nqI60U9gkoJ07RvVrSDTCXIYOO5Z5Hs-WoGnSzjcWg2roWY3V_o1h55frWkr5SVOhmJ14xqLIFY1t6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
🇧🇪
🇸🇳
ترکیب بلژیک و سنگال؛ 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/97445" target="_blank">📅 22:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT0KV_0dI9tetyrvTYC0X-C8B3a18WKs3NCSfGOk-MRWYutkeySyly0PyN6VLMsci5_qMjr0D5-cdYBPw6eWTZ4fWfal1ibLDdv6zMRgye9MR2f6hJAcNymRAZqfslpQOYMs9tnAkqxH9eXeH-pPYck8ZkxFD0SEMprFca8mjivvjqUbMIyHL2ADNvOF6RDvhvHdrJJsfZDCWEosy42c-I-LNJgGEXUEDf1J19kB9ObEWWXT6cpHmvYNnICpx2daT3drk0X9hbDrl7pzGZ50VNCATknX3ppnkxCmTFVqxQps32ZH4XWp7AbDcbcNX640FMfvdX7XWqD0kp8SGMve3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فووووووری
؛ قرارداد ناگلمزمن با آلمان بزودی توافقی فسخ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/97444" target="_blank">📅 22:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddt7qnrIC9tLO-Q-V_BG1kC-5-ybfj5Vf4vhNlI2AFreTzVGEp3tSrFsVfJCEDRQRdM3ibAIV8rfXNesOjgEoBhG-FaBvzvIxLTDwCN3luJiZBz1-6Cv25o5GZGksWCWy0PM2Rmy0LZSLn1hSIZ8S-sxBLWt74RpLQ4LWciqvOu8TL6rYAsVCn6gguFIg88oOCXAMrWoe1fliPZaeNlf7aU-7tNXaJCrmAMYLvSCx-ZpIR4jL2o_iCNeLq6oJUdTPDJOFRTTWQRA94CGhC9i2L23RPbXaABpNlATWiuBvMPt9Az6wxhAyc-fdUCa9YcW6UKVuxwcSzUESZ86dKmKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
گزارش Bild آلمان درباره وضعیت مایکل اولیسه برای بایرن مونیخ کمی نگران‌کننده شده است.
- شایعاتی درباره این بازیکن فرانسوی وجود دارد که گفته می‌شود نزدیکانش معتقدند او می‌داند که می‌تواند با بایرن مونیخ قهرمان لیگ شود، اما او این کار را قبلاً انجام داده و اکنون جام داخلی را هم دارد.
- اما قهرمانی در لیگ قهرمانان اروپا شاید کمی سخت‌تر با بایرن مونیخ باشد.
- شایعاتی وجود دارد که او می‌خواهد به باشگاه دیگری برود و رئال مادرید باشگاهی است که باید به پیوستن به آن رویا داشته باشد. اولیسه زیاد صحبت نمی‌کند، بنابراین نمی‌توان صحت این شایعات را تأیید کرد.
- با این حال، گفته می‌شود کسانی که درباره او صحبت می‌کنند بسیار به او نزدیک هستند. این ممکن است برای بایرن مشکل‌ساز شود، زیرا همه می‌دانند بازیکنان ناراضی بازیکنان خوبی نیستند. انتظار ندارم این بازیکن ملی‌پوش فرانسوی در آینده نزدیک قرارداد جدیدی با بایرن امضا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/97443" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/97442" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDRXknPG4Zsgdav7Ebh34sGTRFZ52biN-7wDpnCRwazTx1aPLwCzxzeX7NwziU4jfDpXziwK36DLtjVR3pxfqj5W1a313badhYO374LhmNOX0dHILViZ4ZGlj5GA4J_QLP_hdWh9VowX5Bsu3fHQTckezi1EG5SqB2KrYtqBeQDDFBT8zyFz4KMOG4QizKSGpQv86JPyeM4L7EAhMW3-3hc8Ydwlebysz2Cv9CUjfb_ukL-rb2W2f3DKaLQ4f3qa1p6tyOfltCpHOGZ7-a6912rM0QOeUvWjtQCfdabIpgH3YAkhA0KssnvFuRd5PPkgREZuSzGE3t7R9KpXNBh53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
برترین گلزنان تاریخ تیم ملی انگلیس در مراحل حذفی جام جهانی:
⚽️
۶ گل — گری لینکر
⚽️
۵ گل — هری کین
🆕
🔥
⚽️
۴ گل — جف هرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/97441" target="_blank">📅 22:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su_DTFhGhQJZCAeRjPxv9CjrAGhTuWiTKKutK3xUDwjAjfLUyITxZgTeMSKHJdvVEbAzWLiIzf51xtJ3MnwXk_gp6HQcwe9HKCttQy_FLhxSQyoPyo1oOyDIeWjqze4bIWJrLUsu1JnkLpJtw7tEjrj1NigVbVnMHDf71TLlNeulWnzVKGBbeqkMrNi6-L8RIhI4i-XEZj1HH17zySxQgApuAv8FodkGA8-i9IXstPvkDnUCUR53tWUK2NQHPBknzHzuOnbX-Nm0cO6kmTqBHnI6HSyQOvHswXxhSd1EU8yvTF65Q5Q0LigjSlk_FYnS_1dlJTYRszfWgtqQnwVoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/97440" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv7YespFt7KXboy_WBKS1h7fYf3GvhE8MI-KSLN6HO-i8RXhhGxEUqGLBi5pGqBtbashEpnD9yy_DAx4MnzlnWUgMUkHbM8DBm5lmsbeZagfVZMoKo-07JJpdcxJhk7qFt3EmU86XP7__dWmh_QDGFgLXK79eJ5agpwAFrtvOEop7ugRtm_mG89aXanq8-wacVJlMgZak6EtbuPKtTTbs8DfLHBzueTH2xUjjS4fKsLOX_qD5sr9rcIyJyM6U5ikkmZchnoByvyZuRXF5HrdKxnHrMF-rxRWouRvk_rWgcZpRINb7U3kVJ7S9DfeZ3jhj2Kj7UHXdqpSZCgGMU7vdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیکتاتور هری‌کین
❌
کاپیتان هری‌کین
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/97439" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5s2TGI1U_SM80m2t-noP3W7vuvT_PjCYhxfZq64DlqbB9escx5yyHDrpE9LD_Ren_IDhDUAsIAXXEgs8hKUVdcdGGo2OMUxFk5JiAk1e1tkMPmlHWpp2Myr0S-eBuq8L0gfRT0buLb_HAoY_oM91TMnS_FHHo7T-OoESeD6-FN92FNM2P7bwi-mZ_gekFM7jTpqQ9MdDYSRZcCGrF8z1x3P8MeGZ8LaVbh94ni5Czg3aYHSrF63BXRiIZIH2NgQdtHMDpdMbEDlKYrEnaS6vG8OpDPytb9AFAD5U-b2sXYg8KBAHAt-BD5wgaCKKhBNtSlTEy158CECiwLiWxH7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
🎙
اشلی کول:
هری
کین بهترین مهاجم در تاریخ فوتبال انگلیس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/97438" target="_blank">📅 22:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5-Af8vimrR260e2C6AW5FIPYUwGWoiBsWPTOGWxtv78VYicT56L5ukonbFL_QZ5roSvFhDjph80FHy7wmdFIQa0zlX_8D7uZ3goqzHCfiwjLshsaqbnFUIVTGs-8QKNHBZcpqd0w-sDeCv23inadzAsMQ7pJVzqvKzBan-G9un9Arai402e8GIrgC5xC7GoFxTlW3KZzdrMQXV6Ftoly5_sWNUsM77CIO3wnNwSUCRs245RWuymSqahMuZkk2Hi-5ZNM9_tCPes_Tq62KGHZiSOYv4QbCFJzvUMyPRY17VvDhvAv0pORLhoGg1eUdgV5a5r9J-rRY1luw9FObWgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار مرحله حذفی جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/97437" target="_blank">📅 21:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brhKWbBkCeaH5EWw-M5M7i3HODrSJbW5YxC3A5T3yQx4Irc2-m6TbcYCvP358zSnU3F-ocKopV1OWik9z67ftFdw5kP1x2gfkLx7YILGf5Ra54Sat9iME3qLnJYWOL28Gr5ZynLRXosW9DP1eyA4SrBzLy_wR3q0bp34A_NVuo5NtrmJal58yLjfHWt8WYYzloof_FhrWs9Pk2_DJb1KRfqUm0Vt9irhOOcqzi4CHTmFb1MLeh5uWcbUcoGm2qiNv-XTv5TsKY1tgikrqTyWFN1ht9QWpAElSV1iWW0t7gpHp74ZRNSpji2Vd4hDaiLIeTURYX6fM3PPISQynXaWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار هری کین در جام جهانی ها:
15 بازی
13 گل
3 پاس گل
بهترین گلزن تاریخ انگلیس در جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/97436" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEo4d4BM2RYRDp744hmkWuTck_4v554VTfO6RobjTbv7Q9EuwGRaNeN8pFptNNsGMqSwtOiikOCJxiibUQCu8a7BskUAY-kbKdNJ_eLIpZk7AsMpgxiOIu34rkBbIze-R80884WcDXUqgkbRMBH7F3mMHm4Zkj4NXVQh72s8HSPVtMLItwj1DRdD3aYZDA2SWB-0aufgMUSmxCafsau_oAKYVjuKlOVoM3YnlcZC7FJKBdL4hvaHmyJOSkb8BU_IEQkqr2GC997JZli-83ClEuPCgdmA1Z7OXNAkanxTuDZWZB5eSoFZ26QSlWCXZccWQR9ltNCamtTXYYfEGwhHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
جدول بهترین گلزنان جام که شاهزاده هری هم وارد رقابت با بقیه ستاره‌ها شده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/97435" target="_blank">📅 21:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97433">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yeww7JOOemsI498xVMiubgaa6tDpvncV3oFP2OQ2dzkDRyP0OwNaBNp6HOZYhtqaIdKaFVNeVYlkC5WC7H3njUmWHzKTd-y-WFGcm_s2Bk4BP66Y0fBoe6NNehcmeAf2aV-xmOQUC06mDhH4KVrqj4CHRclDDRKFNXIS1UvxHqoFRhXHBgrtQXRYTa79uHuUUshqG3a8qaEpJMbcS2oVvwGI_9MxiOvoL_ViKqJu6jgFyn8pMUhZJLi1ETp6kRI3cAhFCuD-0gY_DIhYR1KtxiKzuokPOcArBfFhWllsqES5GhYG7OmsIARti87mJQawDhwSnBF38IjOQe_QSLrclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFnSvTX9_PE5wQCAZd6znltTYhVAqM_FVbjHOcmdqQQ_0n2ZVFALNicozQr-mzWFftiSPrfLTnK8km2VmZMRd9YqYEB7X_L_A81gehMW3mVSeByJ9kkC8esL__0DW3whyOHBHJIU_8VNIEyyXwruxde8uMfTRqEi_vw_xVvTxswi4KiNAV2Pdz6ib7mhIFzQMtdGVsOzMHT952ralCbWj5XGz5w1wk8xAIekovHjGIMJsyvveEpzhYmsm2HZSALHjES9zOPmXMhi2lybuSIdSGVsYd7fwJupwq93dOKQxYzZttWbYgAet5RavgDsS99m51xzrWk0Sre7KFMw44PRPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🆚
🇧🇦
🗓️
۱۱ تیر
⏰
۰۳:۳۰
آمریکا
🆚
بوسنی و هرزگوین
📌
میزبان در مسیر صعود یا فرصت طلایی بوسنی؟
آمریکا با حمایت هوادارانش برای ادامه مسیر وارد میدان می‌شود، اما بوسنی به دنبال غافلگیری است.
👀
⚡️
آمریکا میزبان صعود می‌کند یا بوسنی معادلات را تغییر می‌دهد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/97433" target="_blank">📅 21:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97431">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw5sk_A_8GrcIi5KhyLHGpq076d6cG1VDcOmhjdcBeJpy4ySKNv2D8ILkmL_A3-LFhDdUnAlIO8wvEamZxkhUz2sD19MQW-25eeaRiN2Vywg6AnqKRBvkJLVHhtiwFSymmb2q7-BN1sAhM5bq5IfWkRwbsgFAku9iwkPY4c56Sl3AmAoBgzN2UHgB_2WrBs-8ES3ieyfoOQQET8bkqJ65nMZIrYBBphg7VJv-cyKJuP-i98pTI9UYuS_VxT2-y7Qtj6_Xp-RCKGHRoeF3RCmMPfOKtxmFLNboCiV0PzmA2otNY_DtgF6o7_dzLyDuDe9trqD4gdUFs66ZCEyUX9u5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاپیتان هری کین پس از پیروزی:
‏
🔺
امروز جشن میگیریم اما تمرکزمان روی فردای پیش رو است.
🔥
🏴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/97431" target="_blank">📅 21:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97430">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-ArUew_jh1p5pK-yYR1iulFTTPUBdzCe0eXEPckPbu88ZrglUuIC4z3FDIjLyJ3gA_CsW3Z0rU4MSIxnusfO6KWY2wQ7aP7_poXswew-GaSs3VO2FHNWSH06gYW0lupKxrg0EzBq02vZX-WgqtQxLVMPyKbpr5xLcayq63QutKWmXOh0zdh-DCLPloTdotBrlpZG71G0nC_yHdlIxOAmXKqb0YKcrmtLtnkpOXr8h04E7kTEHlSbiGzrfOsxRwXeq3l43s37SpWyxnruSeOEIdRRheoBL794b3AinHviN5NKk1g66KynJxUmxHjyv0kMdXaCffLnsXAnG_9QxH8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴
آنتونی گوردون اولین بازیکنیه که به عنوان بازیکن ذخیره در یک بازی حذفی در کل تاریخ جام جهانی دو پاس گل داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97430" target="_blank">📅 21:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97429">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btEc2_hG684xFtV8mczCDzLAaldyK4PvJh63mGZhw2yc6vQ7p4r5SsoKHuAyUXutTaUQhiS37zSaNbPg8TIy7FWwzAgp6k7GkXMGkprAdxWawwUBEWg0tOWai6QU9QlkzJoRQnye2NvEn3UzqK5wPi8hWB4UksvM0DrYlORVb5l6WSouuVQUVy8lKInVB4mZcd3_XBxKJeSrE08uMWWcESbpxzJjVwU6oEfMmYOMtIxFy8u78mNPfPP9FdHAFbvpDomXXAKfIXaInY54AYDz429cThBvJWiknUMgXQ1akQDo6KoWNGcqmdO2pdMEQRvnSHsaUSvIH6X0Y64Lp6ZBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان هرگز در یک بازی حذفی جام جهانی مقابل هیچ تیم آفریقایی شکست نخورده است:
◉ انگلستان ۳-۲ کامرون (۱۹۹۰)
◉ انگلستان ۳-۰ سنگال (۲۰۲۲)
◉ انگلستان ۲-۱ جمهوری دموکراتیک کنگو (۲۰۲۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97429" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97428">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHwZgMVClLUvISUp1hN341ay084x9tX5kr6dTkk7TKrYQJ7SMcfzzM0YipLZ4jagkuL8c8M40_-KGKzc8_9hvd4PxU7YiyiEq1BNm90-PPIp8tGuMG8zBRz4uy7X9JcPWCBrSeeQHLA6LGtUlm23qq1JxW1JnKc6x6RG6ZwO59V7b2Ilw8t0DnASt8OQ994qD2VM0p2ixa28g6BVx_xlTaQmfaPg-lQZorMXI_F97JC3y_DHugtdxG_C3IZcuUrVWsUUckIqEE1kRrSTBYDv-k2a8gLGFvWKLB5LSWfEFzvGIk5I8aAiSDaARoxkiFC9EiUccyECh1uBX1W0-7Zu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤖
هری کین رکورد خود را به عنوان بهترین گلزن تاریخ تیم ملی انگلستان در جام جهانی بهبود بخشید (۱۳ گل)!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/97428" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97427">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9FSenmsAtUASLFe2st2BIXFVb-dY2202rRUZm-e5eQ2VyFWNeCUnXovdC-V6UZkojE-LA-cHBT2NEb70YfdXZdgVj5vBekr-nuEvxJiAFbRMyeTwXkM034BeEigO9x-2b2sLTa9hRE8Y7_NPXVI8BqtiIuZ0N1EVfMSGxF_AUubWHMaAE0utIz0XfLdj6GSNZ-e7_5xCThy9lj7kHRpbtvwbt3tjvIjM9z5jLMtLy27xgzEONOXQ1HAIXhsea_Oz-oFoy95bNpWBAWwgpksv0S5Mh9ZcQpRhw2pV7wGK66OsykTa4NYrI_xWUdbH8P8lFb8gZkKlf7nObyA_KIDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
مکزیک
🇲🇽
🗓
دوشنبه
۱۵ تیر ساعت
03:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97427" target="_blank">📅 21:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97426">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp6k9fmDt27CeTeZstNFK5tnbQdEMSvdxcLdFmdesLPjXqr5hqon8sEeZXmq_oUj8GwlV7ZgzKh62jUR-gVmGWclkX4O7idkjIY-aoytN4Y-9hmaAIzgXiuhtCAeOEvG5CXxHQBI60epuVTZDn3-p5fJixAAugrpmNCvytONThq6TOigqjiQ-8csN0gl5gcXC4pXIqMiUysCi90aJEJGHzBJ3sFPePTJMM8Am40aJm78EaoVoURR1i0v4iQFdGrE9M4dtqQofIez1jmkDMdn7qYi2NSoXadWd2Yrs4PT-dPNGmp2lc54LV6Wx46W6efQD_d0EydA2VJncgDPD7_SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ انگلیس
😀
-
😃
کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97426" target="_blank">📅 21:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97425">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxyPuefDw8bUTcPU83lVWo0PBMEjDrXEk_mMfMEgxWAThwEWuUgY8KN76PGCqG7avq5ObIpw9X_M7ForzjxkjDwXdLPJzw3pvV12Iftka5G4Gexkrt-pCBbwJVP8_eNuIUHCf-KqXIE3mNSDfRslbbu5x9qR9cUCwavsDgfXYOwODGGF5XL5P3lQiK6QxUXnY9MtRlf03C8Z3RwF_1RwAuyzdl_rRUFmkY8Slf6k_1fxgQwoqCZlfNOYlrNj4SbckDqO91tn6P4qJ63cTQdgmo9ugm-stloF5W7b706DfCn2YJ79nQHiEQR49d7lV9fLzWvPqHg6vBDURGshuoqJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوردون بازیکن جدید بارسا امشب دو تا پاس گل داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97425" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97424">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97424" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97423">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exnSfqvCw4JBthE6JkwFjvW1-IHzK5biuA8jCnt_qSvLwoXFU8U3Dp-gi3vz5nitzTBw6rKTkC-3JMyDg6Z6NN9eHLBbpzZkAPF6CbUdQrD_cMf4PTo5C31TZMTZXRu8ksgZ7CVd-_M9kUq5Gbb6Mf-bnOWbERtTDFCbQG0c4ws0a2yPpfms53ehC2LBdozARmBntUpX90Ln8mSJkOn20uZBIPuyMySYpOe145T4QdWNVW852xCsosOp2E3Vt_oAZUrMAZCOCHSmuoNho1MST6GTBUh0_sALTsAuLqpANAziClybbRbROwuoSsAide_CYnY8M66R3DTiAhmvXtgF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97423" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97422">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97422" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97421">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5faa5495c9.mp4?token=O-4t6A6oPBi5QW6cD4BC1tpzdPPV3d3gonNPr1_BTrFQwyg1UeOEty6Qprd7IT2wU6JfSp5T-YMP7vheBVGfBwSdeuvUokNVqX_e9J5iga-RzwES8aKGMYkyHvFB76TRH20uf8eZA_FgCm_cz1JI_9wLDifBUV06pqHKZ-zQSUmVNaxWNw5pbf67OXXq8AkicwqpoAd003yKIPdpcFOoTpJq0TT3Nl8B8Q34Xn-IZzpksezu2MIS0Ow0WvCfMl9644mPlSh3tsw_W92WUMePMsM3ENGsi-h1kehKjWu9vyF8r5i50MxmPW3IuO98SbPhVXSlrobwxHiwyGlpd5an53HyV3t2l9m-QSewiauIrRE7ZlADhgHlZI2AlkNmlA9fT_l23H4tV22eTa9Ye-nC8WZJzjdssqBNJC5jurb22bceVQvo-R7NeiwXXoK83HjfGH2TRPCQXbB5XVEOdbei0_klJpo76WBN8EEnPCXTsjPEVVLAnJ_bhJYl93fid3aTCz8F1VXwVnAz6C4EUy2bwa-rUvjw3K1E20Vev57_L1Jh71ce5nUkiAHhflwxdVaEdPljAaW98XDjpr5_nM1PnsOsdyNVAC9PxJ9AK_G0e6SIw4xBWlWCv_299wj9qQt96Qb9gNiOvufOX90tFWtTCY6lE3JJu3mpQK2wLmXq1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5faa5495c9.mp4?token=O-4t6A6oPBi5QW6cD4BC1tpzdPPV3d3gonNPr1_BTrFQwyg1UeOEty6Qprd7IT2wU6JfSp5T-YMP7vheBVGfBwSdeuvUokNVqX_e9J5iga-RzwES8aKGMYkyHvFB76TRH20uf8eZA_FgCm_cz1JI_9wLDifBUV06pqHKZ-zQSUmVNaxWNw5pbf67OXXq8AkicwqpoAd003yKIPdpcFOoTpJq0TT3Nl8B8Q34Xn-IZzpksezu2MIS0Ow0WvCfMl9644mPlSh3tsw_W92WUMePMsM3ENGsi-h1kehKjWu9vyF8r5i50MxmPW3IuO98SbPhVXSlrobwxHiwyGlpd5an53HyV3t2l9m-QSewiauIrRE7ZlADhgHlZI2AlkNmlA9fT_l23H4tV22eTa9Ye-nC8WZJzjdssqBNJC5jurb22bceVQvo-R7NeiwXXoK83HjfGH2TRPCQXbB5XVEOdbei0_klJpo76WBN8EEnPCXTsjPEVVLAnJ_bhJYl93fid3aTCz8F1VXwVnAz6C4EUy2bwa-rUvjw3K1E20Vev57_L1Jh71ce5nUkiAHhflwxdVaEdPljAaW98XDjpr5_nM1PnsOsdyNVAC9PxJ9AK_G0e6SIw4xBWlWCv_299wj9qQt96Qb9gNiOvufOX90tFWtTCY6lE3JJu3mpQK2wLmXq1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به کنگو توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97421" target="_blank">📅 21:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97420">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97420" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97419">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوممممممم انگلیسسسسسس</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97419" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97418">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هررررری کینننننن</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97418" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97417">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگلگگلگلگل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97417" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97416">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5851711fa4.mp4?token=aRUB1Fs7jWofzpxI3VP96KLGV-CEox4j9JQ6WSvUT21jQ0mjQP3hLkgLpnRRlXaOvS4pNtf0XiFBqQZBL8AIlJ5cM8ITpDFa6_cL2_XFwQzAu00GdpEIR9LU1ioRjnZLnRlxX_LWNSqFn0vqb9T3yP4FCsmfzC550ufpmVx57L79uMj3N_GDsrDxvrARcBfpYWbGuAVTRbXpTqf4X3jnxtesrsIu-4SAsOT1usOiUWKpQqV-8h1xl5dQzmoxnISUvbLnrcz-QBcWsGN4NX5NhsqnyIXGma2fscRMYUkHRo5DqVZ18WSmCDtRazn2XHfYEKYSMyuy4CFa2IhIrKgjpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5851711fa4.mp4?token=aRUB1Fs7jWofzpxI3VP96KLGV-CEox4j9JQ6WSvUT21jQ0mjQP3hLkgLpnRRlXaOvS4pNtf0XiFBqQZBL8AIlJ5cM8ITpDFa6_cL2_XFwQzAu00GdpEIR9LU1ioRjnZLnRlxX_LWNSqFn0vqb9T3yP4FCsmfzC550ufpmVx57L79uMj3N_GDsrDxvrARcBfpYWbGuAVTRbXpTqf4X3jnxtesrsIu-4SAsOT1usOiUWKpQqV-8h1xl5dQzmoxnISUvbLnrcz-QBcWsGN4NX5NhsqnyIXGma2fscRMYUkHRo5DqVZ18WSmCDtRazn2XHfYEKYSMyuy4CFa2IhIrKgjpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول انگلیس به کنگو توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97416" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97415">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شاهزاده هری کیننننن</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97415" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97414">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انگلیسسسسس</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97414" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97413">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97413" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97412">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYzcinkafQy2Pbxtcdnt3NbkeGAQpDJ_GCUjzIzIsDiun7GtXRie03y727Jia3zr0lOZwZi68rKOrJid3YroeFolY4YoSxjuEbZUOmjldBohtMZHcBPpD-Uk_NyUyOlq-aT-aX66LuJpj86n_TVh8vkqIMLnld8zqr5CpeEryCHT-lqmsgsW8nE7NjFVMQBhb83HcHgYlzDBK3Tw362O6bKEhPuJXxAQ227VJydknIor091SfK90WNww3MKNLX8Ed74dv__D6GkA1ayzKtS_18DSBaElbz5w9LKq2v5L2v3DPAgq_MBA8yfCOPtO3FkYrITJ0K8t8v88jIyiQmA7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇩
گل‌اول کنگو به انگلیس در دقیقه ۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97412" target="_blank">📅 21:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97411">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انگلیس فعلا نتونسته کاری بکنهه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/97411" target="_blank">📅 21:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97410">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97410" target="_blank">📅 20:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97409">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITAMWR1SuEUquQIqrHSzTVjJG6ZSwSA8yN54iAJdMRr4cNLF4izNT724QPrkJ5T328JHRecB_kMIIea1Y9qTBQoYwKpHDl9RU5v-LEnf5iNyWCLltc723npTX_SEtPuHHeSGRC2-EHZknE_bHSn2pMK2qidiqCK1gZmb8vNTrEmeC0VW5qVDAdDMGl2Fi__0cB1IkSRYFPvEamaGoQ54DKAU5YfbSN2ZA5LEX89bQ2AY4YdTyndhXfKDZS-P82RwLjyg_gBgYP_HSzz_vHw0RuIj4VGFbekwgWR1Yn9eb1L4tR-fFaV6oLw1BuwsqrZfaihKFhVtvR6iP5UhQO6IUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقطه ای که گلر کنگو باهاش سیو کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97409" target="_blank">📅 20:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97408">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممم مصاحبه فیروز کریمیو:
😆
😆
😆
😆
فیروز کریمی روی آنتن زنده: قلعه نویی ۵ سانت و ۱۰ سانت را تحمل کرد، دیگه ۳۰ سانت را کجایش بگذارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97408" target="_blank">📅 20:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97407">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🏆
پایان نیمه‌اول با برتری یک‌گله کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97407" target="_blank">📅 20:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97406">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلرررررر کنگووووو بازم گرفتتتتتت</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97406" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97405">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97405" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97404">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=IDx2Ud5NDJO-nKHfwbExV8sCoidfbznJQqKbsPGXHhd1linFbtMhet-s7t_ZjRk50CD6gwNnYHOgfHoqNiBK4rkObQYHfndTeVTuP2-ADhYYBICspFiFFEyqzlWIgxd9r5rxpndTsKA0azOGrLEQo3agB70oUF8BX3PHDXcMYK82hHc9cxcOh8c8oX1c9hxNcNoI5xo7oU8oX8MuLXfDF5BgVTv0BwQ7z0M-F0yXgn4nEbRj6NcTkbwPccoC2DqVwY5f_wWTKSwJQOlRr72kjW00HjMaNeDwYJ5PN-VqbIRYKojqeI8RhIa2XcpR7gOxDTXvduR-0SlCiaADU9q3ng" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=IDx2Ud5NDJO-nKHfwbExV8sCoidfbznJQqKbsPGXHhd1linFbtMhet-s7t_ZjRk50CD6gwNnYHOgfHoqNiBK4rkObQYHfndTeVTuP2-ADhYYBICspFiFFEyqzlWIgxd9r5rxpndTsKA0azOGrLEQo3agB70oUF8BX3PHDXcMYK82hHc9cxcOh8c8oX1c9hxNcNoI5xo7oU8oX8MuLXfDF5BgVTv0BwQ7z0M-F0yXgn4nEbRj6NcTkbwPccoC2DqVwY5f_wWTKSwJQOlRr72kjW00HjMaNeDwYJ5PN-VqbIRYKojqeI8RhIa2XcpR7gOxDTXvduR-0SlCiaADU9q3ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممم مصاحبه فیروز کریمیو
:
😆
😆
😆
😆
فیروز کریمی روی آنتن زنده: قلعه نویی ۵ سانت و ۱۰ سانت را تحمل کرد، دیگه ۳۰ سانت را کجایش بگذارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97404" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97403">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلرررررر کنگووووو چی گرفتتتتتتت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97403" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97402">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چی گلگلگلگگلگلگلگل نشددددددد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97402" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97401">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97401" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97400">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رشفووووورد ریددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97400" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97399">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTYbcRo-MlTFeKE7aLDOu8xPB74dRMw3gkQUFheOfzwkWrb5yJ0h3OLZRCHffr-A-ijHGAcmU5QFU--ArNLJxGNhBPmw9XNk41pIbAIMJWPtKMJEVY9P3cdvChQ2wMQYvxuzQ68Yk8XeSiXvwuq_WdgLRuZVR9hs4bXVaVIi0LFSqIZISfHcDcu1Nze_mMoOE_b3NVjjkK62LrF5pD1LEGk7nZW-DVBia59EPJVUVMCEp8-t4mxABEz9szinWDarjQCAN3ByHX0n3wIYCJdKM3nv7HIcTN6i9zOVIcmFt08iV-zo7hwTQy_DrFgpFime4X-N0lEeMv-LWnqkoiSnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
👍
بوووووود یا نبوووووود
👎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97399" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97398">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نگرفتتتتتت</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97398" target="_blank">📅 20:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97397">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خیلی مشکوکهههههه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/97397" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97396">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">داور تمارض هری‌کین گرفتتتت</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97396" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97395">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پنالتی نشددددد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97395" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97394">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انگلیس داره گاییده میشههههه
😐
😐
😐</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97394" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97393">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کنگوووووو زدد تیررررررر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97393" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97392">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97392" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97391">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97391" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97390">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpWOFkzC-mYl9jkVn1r4dI6BlAL7OB-K4e3XGGSZuXN2q9plDYtVFSshbNLEtsSAhe6e80gcK17aoTTpn0agMmkgV7YrDb5COJvafr9SDuWTQrVuXeJsNP3Qj3PJWYGYBCD9EqxyyCN-Ud9rzo4De6Gvq2uFiUxExCDSvTI4i1cSET9bDPuF1n2hYBMhQY3x3p15unhZLrTQby6xqS2W7lslGYOtfxUEjGL-NcogA3O-_QZLKt7Y_w3C7RGWTI7UECjKbOc5oGr34vSfpcYGRqouqqXqUKDZfRAXDXr4XeB5eMlZ9OrWzBKd4h8a8XceT_V6fRvNUPlsF2zngq4Dhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
رشفورد اینجوری ریدددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97390" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97389">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کنگو خیلی کیری سخته
پرتغال هم اذیت شد جلو اینا</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/97389" target="_blank">📅 20:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97388">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چه تووپپپی از رو خط در آوردن کنگو</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97388" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97387">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97387" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97386">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کارت زرد برای بلینگام</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97386" target="_blank">📅 19:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97385">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این که کنگوئه اینجوری حرامبال میزنه حرامبال کیروش دیگه دیدن داره.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97385" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O15XWCyvTF2HwAj6KXuSR-BivwY3IfI_wGFzEke3rV6W8VUR4H6nOaE9u1R3l-RXTpc3-YtDPue6ypg3X60Gp36D5BIMatALT5KIh86GJCI3IG9y-qYsKtksFPBBZ3oxspxDzBa4LqOqjbirWm_LYk-G4chJ4F0U54Coy23ccyv9BTbolHhqz_S3jCK8Ak9xViwQiLPkTlSBmZhBWg1S0RZMFI3Fu2dWbc8UPydHD5WTK_i8jaqVpFchUBZgcWMXV1_qlZVzas6kZkBj3iqDkEJKoP1trfi4k5Pa8epbLlEnaIn__jE8vjulDFoa-FOAEpG5vwn06dKcgRxjIut8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار به روایت تصویر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97384" target="_blank">📅 19:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8df51f9cca.mp4?token=R_5YWMldhqLUKU2etuxlnfV1w5xwSq38ZrNWyXFF-NHBXeVnyDc6168pirI4kg-d_avpTHC4--Ll7EnTHWGExj4Gan4nyjxfskU__oRapdFRZl1oZav6ZssiG7rxV07QiskrPEDLfn2I1i8_saTBQZULvPdHYmymqdaT0-2fduco2sD_t2jbfWnrqArN8CGOuo2HTdVF8EbzWpROhpdjdRatKfQ2iGHR3uMSmB0WcWG1VRjfLzgg_toWzLhFs-9cS7adKam0zSiqTcr8-SoPq4vkbOEJff3I5AdvBGtc6zWV7OVcUpCsJVqM7WkQknIsKNgzCAx5hH6JjRsb2ZxIGpURzjgRBRc6ByAMz5-2VfPmQbBsnc-fd4khURlKXWLjfGISrll2au_1U3zQjZg6uC1X69cxGt65KJ71tZmhu9fSSFFZUEUi9Kfag4E6wlNW4Y_EBdlUHK2O49WeT8o-MNzSvRbbylNt4ebfbIQjLqcVOFC77Osg5wrHsMORL8jquS0vjtEN2l8wIzfAQYXGo5l6dDzRADjmxAI7cvv3-6M4LLgX4Z5VEt93h7zEIbWLSw3qT4S12-Fog1wFAuHZfiZkD7sPkGwniiyUXlGWzGIp9BhURys6PdcsJiJmnduvesOURxnKF19EiG1_p4juN_MTUQqZUICBoMBSxDdqzUE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8df51f9cca.mp4?token=R_5YWMldhqLUKU2etuxlnfV1w5xwSq38ZrNWyXFF-NHBXeVnyDc6168pirI4kg-d_avpTHC4--Ll7EnTHWGExj4Gan4nyjxfskU__oRapdFRZl1oZav6ZssiG7rxV07QiskrPEDLfn2I1i8_saTBQZULvPdHYmymqdaT0-2fduco2sD_t2jbfWnrqArN8CGOuo2HTdVF8EbzWpROhpdjdRatKfQ2iGHR3uMSmB0WcWG1VRjfLzgg_toWzLhFs-9cS7adKam0zSiqTcr8-SoPq4vkbOEJff3I5AdvBGtc6zWV7OVcUpCsJVqM7WkQknIsKNgzCAx5hH6JjRsb2ZxIGpURzjgRBRc6ByAMz5-2VfPmQbBsnc-fd4khURlKXWLjfGISrll2au_1U3zQjZg6uC1X69cxGt65KJ71tZmhu9fSSFFZUEUi9Kfag4E6wlNW4Y_EBdlUHK2O49WeT8o-MNzSvRbbylNt4ebfbIQjLqcVOFC77Osg5wrHsMORL8jquS0vjtEN2l8wIzfAQYXGo5l6dDzRADjmxAI7cvv3-6M4LLgX4Z5VEt93h7zEIbWLSw3qT4S12-Fog1wFAuHZfiZkD7sPkGwniiyUXlGWzGIp9BhURys6PdcsJiJmnduvesOURxnKF19EiG1_p4juN_MTUQqZUICBoMBSxDdqzUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇩
گل‌اول کنگو به انگلیس در دقیقه ۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97383" target="_blank">📅 19:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چه گلییییبییییی پشمامممممم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97382" target="_blank">📅 19:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پشمامممممممم</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97381" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97380">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کنگووووووووووو زددددددد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97380" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97379">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97379" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97378">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇨🇩
آغاز بازی کنگو و انگلیس</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97378" target="_blank">📅 19:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97377">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjBSXDToBeAYLVeM-8nEsoaMgH6EKuGkTkTa8nxqQe3H_aaz01qBa8wKunjUK6IQYlfRO_NrQlhvGR1jPgMweIT5vtVcb2eDp1R0xlyi86R0rLlGxXXBOXZDR2hAWpJkw8ad-5PYtFxhwR2lSP3fbEIKc6WxZw4fwNrHN9y-BZ2hWXgqhtgA2prgpaCKRGh00aSbHdBLCl_f7JBoXgf_TpOqma9X28LGEoNiEygGieC9XKwjtYeSlw_-sW6iQjrpwSH5OgQ7j6QvxIsaY2OzZtOqZWIQCzWFY_2woS-tDJQT4dEqOoRqERsIp8pdUKGoifGYLu_zs59tSXfmmm2Kyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسماعیل سایباری رسما تا سال 2031 به بایرن مونیخ پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97377" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97376">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84477c6b89.mp4?token=QMzJ2Fhh9FhXBpxjF2yOzOCDQE-rZX67Bo2iVb1QlAUV1uDSKzXk0O0RRZKuqO8vVo0X3fX8mhMUXVBLR5jFXvJOTbLzRB-hAQ4WurODErs5I6vWHPyL8PsooxMVfRnPm4NEVN-9H_3h8yKLw7o5TxvBgJ3dCDDv8Q0Ov04SqLbmQ58BnTq4QBMtHo9eQL33jBj9beT5pOqJBx12ex6W1R_z-ZeEsAOc9w_Ngwhf8E63-jLjGUAjDjS-6JVBvlxVK6ydbC9rNj7mfrdpN0XAfTw3jYV_rPGBOp0WMw3hsZ_ZvASV42WIA8T-lol1C_55RDTVBApexTLP4pLeliF9rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84477c6b89.mp4?token=QMzJ2Fhh9FhXBpxjF2yOzOCDQE-rZX67Bo2iVb1QlAUV1uDSKzXk0O0RRZKuqO8vVo0X3fX8mhMUXVBLR5jFXvJOTbLzRB-hAQ4WurODErs5I6vWHPyL8PsooxMVfRnPm4NEVN-9H_3h8yKLw7o5TxvBgJ3dCDDv8Q0Ov04SqLbmQ58BnTq4QBMtHo9eQL33jBj9beT5pOqJBx12ex6W1R_z-ZeEsAOc9w_Ngwhf8E63-jLjGUAjDjS-6JVBvlxVK6ydbC9rNj7mfrdpN0XAfTw3jYV_rPGBOp0WMw3hsZ_ZvASV42WIA8T-lol1C_55RDTVBApexTLP4pLeliF9rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
تیری‌آنری: حرکت دیشب دشان موقع تعویض امباپه نهایت بازیکن‌سالاری بود و اگه باعث ایجاد دودستگی در تیم بشه مقصرش صدردصد سرمربی هست که به بازیکن فاز دیکتاتور میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97376" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97375">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd23d495ee.mp4?token=dCnU52ce-Ko7vv7kdjbqembNxnWzuosd_HybjWMUOAdIa2Pb3df5Sjaj4Ghxe_hPYBwi5t-UleUWGQjG6nJjjwzScr_LS1JSetQilN89q8yssd6XhOSyuX9LItIzXhN8sLFj0_eUVwackxqasj1FTXy15WnRMcSkYhY9QPSsqPaJc--5hZotHc9sb6--Km4eD3mRjsEUMia0o5adY94p1pyvus8JIw2VwqsHMzgKg2VovBISV4JI88p9zdiISpceqgTJN5Ve4iT6fPf2cpNFmrKW4P8utkUD90MxEuWfBnWI_Lg35ExVWPwZ1ZRqeivg57pV4Ex-Rf5S7hSLktxFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd23d495ee.mp4?token=dCnU52ce-Ko7vv7kdjbqembNxnWzuosd_HybjWMUOAdIa2Pb3df5Sjaj4Ghxe_hPYBwi5t-UleUWGQjG6nJjjwzScr_LS1JSetQilN89q8yssd6XhOSyuX9LItIzXhN8sLFj0_eUVwackxqasj1FTXy15WnRMcSkYhY9QPSsqPaJc--5hZotHc9sb6--Km4eD3mRjsEUMia0o5adY94p1pyvus8JIw2VwqsHMzgKg2VovBISV4JI88p9zdiISpceqgTJN5Ve4iT6fPf2cpNFmrKW4P8utkUD90MxEuWfBnWI_Lg35ExVWPwZ1ZRqeivg57pV4Ex-Rf5S7hSLktxFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های عجیب محسن‌مسلمان از ازدواج ناموفق و دادن مهریه کلان در سال ۱۳۹۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97375" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97374">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AOrqYUaB-JWlbczr2ac_8hQZLah8OdAWqzfzqUyRDicQw31gj0gSxrXTtCMSc680plkKAqZbSZe8Hk-dChtlcGIr9X4HY1DobJP_BiZFbQ-B49Yz26FkZ438sKuf3CV4iwUPkPXR6vt7aaZGBz4IdhnxAKAgvDV1OQ2Zl5LT-6Y3aaXitHWg9MPTfB9l3gTyNmiWE7pFUxVcDbrpaEgRMG6QMuTK6Xrb-7aOA4i528MvgBDNam7G5tmYZyhuigtLmg46h7o4n2MLhNEIoGNSvPZRJwoQ0oVAeyxCmUYZ3MTfhl6d18lhV3TZebNNgHMm2OBDxjRZHrBKn_3VBUDdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تام‌الاختیار مدیرعامل باشگاه چادرملو اردکان:
اجازه نخواهیم داد حق باشگاه و مردم اردکان ضایع شود
به گزارش روابط عمومی باشگاه چادرملو اردکان، امیر سیدین نماینده تام‌الاختیار مدیرعامل گروه معدنی و صنعتی چادرملو در باشگاه، شایعه معرفی تیمی غیر از چادرملو اردکان به عنوان نماینده سوم ایران در آسیا را یک شوخی بی‌معنی خواند.
سیدین افزود: مگر می‌شود فدراسیون اصرار بر برگزاری تورنمنت سه جانبه داشته باشد، ما را مجبور کند که بدون تمرین وارد مسابقات شویم، چند بازیکن مصدوم روی دستمان بگذارد و در نهایت بگوید این تورنمنت بی‌معنی بوده و تیم دیگری قبل از همه این ماجراها به AFC معرفی شده است؟
سیدین ضمن تاکید بر دفاع از حقوق مردم اردکان و استان یزد، افزود: مطمئن باشید ما زیربار چنین ظلمی نخواهیم رفت و نه تنها از مراجع قانونی داخلی و بین‌المللی پیگیری خواهیم کرد که در مورد ادامه حضورمان در لیگ فوتبال هم ممکن است تجدیدنظر کنیم.
سیدین در پایان تاکید کرد: مردم ایران، چنین اتفاقی را به عنوان نمونه‌ای بارز از بی‌کفایتی مسئولان فوتبال کشور به خاطر خواهند سپرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97374" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97373">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAEklGceT4pksrox_9sZ8zMqt6Dmf2KS0jyTYojLkr--reEIPek3s2PNyA2plao17D5lXdvzkJVClNDM6wZGvRRlbOGy6Az1OO4IgWCud9VlQeADjMDFnQP93ZG5aoqOXQUVRcgXPLlFsQZ3f6IrngH2wKxYnPOpgjsYKTIDuWlaGhcDawrBzW1Xt8wUx7tajMmtv1ZLn9sgHQ7bxnZwCsfwUZoGOCmzlW42ooqEA3f3zc3Ju3KgNWSVoqFua-ZbqQuQiONU03R6QjozlijnRjuUguAyXaETXzKvkAkeae9M--CJPpZb8i8NHuVT7Q8GBEUghB15tiwALFy7ChXrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
آپدیت بهترین گلزنان تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97373" target="_blank">📅 18:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97372">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq-KRRVChTNywZJVdbb_wUJ5q1CRfcsuSl1wIHYb6PkVXv0-Y4Liy9MU8yiZCcY9HapjrTPYYoHK27-YT86asPf26d6dQTuw4nkWIrR4FOdbly4YNsppMsJk_WBwZplYD_bAW0YM3Oqp75zCSjdtlUXxA4zPeVhJrpwcXutsj-xsK353KjVA5nkH2ZIzLFdoS9BFHVIVZVi2gHDvAtd4NbNZsmp7bkH8EoA8higGYLqJ7TUI5TLW1E9J4PBLJRVjFQWTAZJCOuDoRHxn2WF3GzA8-5o_Xp1Bq_D1RiDufRXIUq3vh2dSHlcSZNQ3et7GvxittHqXWqNRg7f84kzuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
قلعه نویی در بدو ورود به فرودگاه:
دستاوردهای زیادی داشتیم و الان همه دنیا درباره درخشش تیم ما صحبت میکنن. گل شجاع صحیح بود حقمونو خوردن، با آمریکا جانانه جنگیدیم ما عملکردمون عالی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97372" target="_blank">📅 18:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97371">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3ZdjL6osFaD-ryVAWdzVIk0jOfiVdKegWbxm1QB6PFAl8nmM2Kl3Qqsq0GeNUs_V7Mkc1Dkvi_LYahjAsABMiVOgt5rstvrA-YGgTV4JWwha1F3iBjp4JwxG6dlpeIKUDA6s1vmvJ75b4sdme2lcyHVKqCt1N0JTsENIX6d0EJ6SmuHxXs4V6vbF6aJeezggYKYsnKc1v-ag6nUF9wnXzGKdVWiigJc3AedPREwWnjduaEXqtcHRdDX0fRFBYMFFHkYQ7sJj59OKtc490fLFvveJEzG_2FmMj6BIpb1C2gp9Lk4nn-EWTuc9hRM8g0ccuuKQvnHfU1UDzp_3nYXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
مایکل اولیسه فقط 1 پاس گل تا رسیدن به رکورد طولانی مدت پله برای بیشترین پاس گل در یک دوره جام جهانی فاصله داره. و این درحالیه که ما هنوز حتی به مرحله یک هشتم نهایی هم نرسیدیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97371" target="_blank">📅 18:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97370">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35fd6c28be.mp4?token=XMOBs5MPTcitvYjXNOiSgV_uDUz7ocbhHXO39vgIAi_NYlImhJap93WuzC_IqEVvaLPEM1wJC3zoBIcN2TrAxIQe82ArwgGbrGB2K4nhINDN3iNEm3mwQyRBfACP13hL21z1Pded5XCGkP_F17HvhYLU4tmgdaJIfmGgbIY2WkhvAzBGnvpHyaayZDih0pIgV-D4t8uqF9lyZHgOY38cnfR1OL8Hs44-Jq_jTZXHq7aAjTcas49QsMB7sPqYNAHT5d318nZHMiLHshtci_1oG0dVaw23dLt_K96Ib2VltYOiMPfMZkz8wy49N3sCHLduWFwGwJ07RbQetxajJmBHqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35fd6c28be.mp4?token=XMOBs5MPTcitvYjXNOiSgV_uDUz7ocbhHXO39vgIAi_NYlImhJap93WuzC_IqEVvaLPEM1wJC3zoBIcN2TrAxIQe82ArwgGbrGB2K4nhINDN3iNEm3mwQyRBfACP13hL21z1Pded5XCGkP_F17HvhYLU4tmgdaJIfmGgbIY2WkhvAzBGnvpHyaayZDih0pIgV-D4t8uqF9lyZHgOY38cnfR1OL8Hs44-Jq_jTZXHq7aAjTcas49QsMB7sPqYNAHT5d318nZHMiLHshtci_1oG0dVaw23dLt_K96Ib2VltYOiMPfMZkz8wy49N3sCHLduWFwGwJ07RbQetxajJmBHqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇴
سوپرسیو گلر نروژ در بازی دیشب از این زاویه که واقعا فوق‌العاده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97370" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh-WGobb_LcKiszBL6lmLiZeoAkL-zSo4UPOHhaSzgfbeWtHJLnE9B85w4g5WYCg1HNoZ0IUwA4RWqvY9d2usG826z90pi8lm_3zSTQd5D1bvaqH7KZkFB0CWn-fykZgumPrHf1ywDax9gqFZQJLWTr8U-ufeRyzRGp9DHxK4PDCIZRXHhsGWspVmjDpO1G3DeWzLPE2BS8UM5X2WZ0g8o7rf6q72g9GRjP2hEGaDOFx5QXRDjmHM3gzqNqny3AocL9U-Jq9EiXv-dVDTqJAh0oPqezH8Ib540W-3e3MotkemR_272ykwrshiOkpeUaqRfUDbXyQTonoNjgGetV_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPantQJPgV4MHR9GIFMNAUPrv32p7BYwoi5Z7hukIfHuZxdiAQRr2te_NbzD3fu-k9JRta4cIwYcVT6EJuKzXRHcoMfupEPurOZGYfmSOf_yTgpoQ7jHEFZumdZiDTmFLB4Ne1foPIKta-MZgZgLkNt2hQ_FktlB_1i6A8wL6P3hIky75dNKhUQK1YtlY6Hk-FOinBTSOFrN8iyuinXd2iECzAzBi9jB1PaXAA4TMuxJuIj7E0fcBB9MPRuIO3fc1BANb1J-inxsHSka3BjLLdue5sZj-0_O7NQ5a9k1Q6A2yA-YyQx0KJePBI706MSyq6LroCgWqptFxXLLxv96Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇩
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس و کنگو؛ ساعت 19:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97368" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97367" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d8b32dc.mp4?token=F_wnV9lmh-nx3aCMPafui-5h9ADliIUkLK_0lLsnCLtufvzK2xwd0cANNKXwX6kcCL2aIFFRvBCoW5icz89RIIoLKrOuCwfQ7jccGcQHrS03chy42pUF9Le5VFmbMr6AYVMP-mDuQzolid7io0lbV5ZTgWYOaS0a24c47Z4_HTEF62wC4V6J1xfG74vSah22ydKs0ZS-5XQUpi5Az1KYpmVZxHgGJRAUiHx9IMc6Aa6FTtgiW7MM-b1JM38U9HrvgPBVid1rF5GURmTdHG17fCg3ACsivDinfUpubAP8a6pMJzEoFEqPZ09DC6e1xr1LXoeHs76_oQy2cDhUzQ4ejA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d8b32dc.mp4?token=F_wnV9lmh-nx3aCMPafui-5h9ADliIUkLK_0lLsnCLtufvzK2xwd0cANNKXwX6kcCL2aIFFRvBCoW5icz89RIIoLKrOuCwfQ7jccGcQHrS03chy42pUF9Le5VFmbMr6AYVMP-mDuQzolid7io0lbV5ZTgWYOaS0a24c47Z4_HTEF62wC4V6J1xfG74vSah22ydKs0ZS-5XQUpi5Az1KYpmVZxHgGJRAUiHx9IMc6Aa6FTtgiW7MM-b1JM38U9HrvgPBVid1rF5GURmTdHG17fCg3ACsivDinfUpubAP8a6pMJzEoFEqPZ09DC6e1xr1LXoeHs76_oQy2cDhUzQ4ejA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇫🇷
ویدیو وایرال شده بعد بازی دیشب فرانسه که رایان‌چرکی اینجوری سرمربی تیم دشان رو دایورت میکنه و از دستش عصبیه. دشان هم هرچی از در خایه‌مالی وارد میشه جوابی نمیگیره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97364" target="_blank">📅 17:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj2KMiY1-eRTs5AkLpckxi9UqpS-WEKytylK5TCFBFU56ZpgpK-HfE2XWcTUid6WAPs8jdykyvfLdD1LxndamqnY6rDJ7Q939eYgh5QGVgOrOneT63kOTeQ2bvPHl0l4m0AuBosYzOPU1eiIgvD-WdEhmngYNHYPYiK5Pbl-Sp-uQBaWHCHy4XCqm9ANK1gm0AYGm1gXKLcNN8gPYGRtu_R3iIrUX5spDpm8SR9-hvkufryly2RXuJURtuQYwq7aXiuGQqrhtVJe8UpEZ-xnkd7Y8j2DidCQTvp-EKYU1jbQY2_rSQ6SkzA9rxafLvl1vuJqhatTghCf-FUYTitQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
دیشب بعد از پیروزی مکزیک مقابل اکوادور و صعود این تیم، 1 میلیون نفر میریزن کف خیابون و جشن میگیرن که در اثر ازدحام جمعیت 3 نفر بر اثر خفگی میمیرن.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97363" target="_blank">📅 17:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh4kqMevQGcN0a1HoAo2Fa6ENneXhZEzWmoS42BZrH2ivzwxCgVvqFg50m8Gl5snGuezV0wConx67phEdz5U4YdO9ndrMjbPb3Ht-2eo3OIMluhkPCIUPkM48R4xV7K3w851Fuf8_A-2mZ6knpiF-yD4ionH4gBQBKEOMxCuqyKvN7t9Tw_BAo3-H026aF8GplNgz-Rkwq0_XCimJ5v3ANyCfqzxMIi-KZlqd74h-gHqi1PZHLRzeDYO3lXVw4-v2rc3UJ9B8-WL8pJ5KK9E_dngTzN8zylymUQGm4A3niBEPhCjeq-cn4WI8oIF2gYHDrfglTwtgiE9TtTMZa4H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97362" target="_blank">📅 17:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ddb483137.mp4?token=ODFNpNkkSDDJDw0gUYezTIQIyAORYvH5ZLCvf3M7JRmPFbQ8am_mtzyS54OuSQzACPrvq3FH5xbuzEPKE3WzkOFcTj4dhU_Bnn_jyTySCrEgDKIRZmwshT6GsPJ8hrKTX2bKTU5DGUd8kNCVnS107iWecxdo3s4oGE0ftIogsjBDffWvLsm3LRLyRmoJWeER0buEHVRbWm4BRZ_gMQ0FXMkLjMstvTbJJKxb8ffDpfX6rFzk5D2e8_2mxpjC6RgYUQV0baN1EWRYX-PQiIyJKjI8BAM4_sQvVwjY6FH_96Oai_JqK7RRhfOgZ18x50IYNFR9ZxRsWOWE_UZ9wt5scg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ddb483137.mp4?token=ODFNpNkkSDDJDw0gUYezTIQIyAORYvH5ZLCvf3M7JRmPFbQ8am_mtzyS54OuSQzACPrvq3FH5xbuzEPKE3WzkOFcTj4dhU_Bnn_jyTySCrEgDKIRZmwshT6GsPJ8hrKTX2bKTU5DGUd8kNCVnS107iWecxdo3s4oGE0ftIogsjBDffWvLsm3LRLyRmoJWeER0buEHVRbWm4BRZ_gMQ0FXMkLjMstvTbJJKxb8ffDpfX6rFzk5D2e8_2mxpjC6RgYUQV0baN1EWRYX-PQiIyJKjI8BAM4_sQvVwjY6FH_96Oai_JqK7RRhfOgZ18x50IYNFR9ZxRsWOWE_UZ9wt5scg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
دخترای کم‌سن‌وسال با دسته‌گل رفتن استقبال رامین‌رضاییان تو فرودگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97361" target="_blank">📅 17:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOi5zAP2KtnMCeIMjUPeP4nBNfZfskiFURfHAZ-bIfnsfPHm5yWgx6Tmklc3q3I3GCpG80yqiXWgCfVLT_OCzlLDqCTS2Z9of6mj8vdEdAI450Gl1Bs7JQzBgk5FqTBIXSrBA_RmRlwi_JWn_JpQGc-NQw619VhP-4WDSD9529IAxqXDW4snzN627LvD1Kjhwx8KcrPsvTM34t0vsprdWpm_fhFHuyPVDIDNTq6qVO1mpY_vGcqNFPdx3f6KtjTkFH5GhH3BN8yqnlgxjiCj7Jbwku76Yzu7WJM2mMU_FefsZ0IZTQOAxf6-HnuU2bgWSG2BhO7nnFWHD844iQJfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
#فوری #اختصاصی_فوتبال‌180   باشگاه پرسپولیس به ریاست مدیریت بانک شهر پس از شکست مقابل چادرملو حکم اخراج اوسمار را صادر کرد و بزودی این خبر توسط رسانه رسمی این باشگاه اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97360" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfExN0uAskAP71QSj2vIqacdHvHPLutN_ZY2mo6U3QQe-yE3u7luQUVtStDnaNXhLxkWy7Xug5zIrsmh0FveUgiOA6AIZMfUft5ZFjneHqz9CPQ-GoPt0da11rGnPY_LolZgX4mBrCVw-foAUzxS9RKaZxmNoxF16GbXUlZy26XvFCIqiEOBnj3ivlYko9Q2wLGMEfUMyaKNFO9NvsxO6qAVLM72JCvS3e7lfDpDJiCm-f_9Ci-Bw5_HfI_Vxxedp-2wtJLqD0I4fa3JNIflFwL8ZRbgwwdrfblQk6WH1am83XVA_coUREQXzugkYzqRv2B9qK3K-qYyffJwUEjcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇨🇩
سایت Score 90: ترکیب منتخب بین انگلستان و کنگو قبل از دیدار
امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97359" target="_blank">📅 17:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97358">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsbZoj_OCcqE35QocmqYBSwCJS0CB69586w0ksS1gr1chB-aszwbaLxBiVVSuq0T_BR_TZE8fpGkd_il1LVe4o9lI40iO3Hg1lNK3PiDEjzNFRH3ZL-tInux5x4-TiClFybaGjbJwbYK-vnNLZ_YN1ftnp5D8t5Z9Wl1kIs9K3yVWwQmfOcredq6dBJjMdxqCFHyrwt_aLahazH4kkApAYoShPJ_1pmKEQ3LZvHeaxB7_vjdmcW3VzKw6r7gF1qlAHB9Pw0LYSCxolmob8VSD71HACFI4sQm2NojX2dvCd-0j_pFIwrMz4t66v-UW5XTGlHbnrffr12DjImwCZXmjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فووووری؛ لاپورتا: ما برای آلوارز پیشنهاد جدیدی فرستادیم و امیدوارم در مورد تصمیمشون بازنگری کنن و این پیشنهاد قبول شه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97358" target="_blank">📅 17:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97357">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ238mhUdXWM4V_DP52me4_OnAviSa0Q--Bhza7d5ItXy-EbaylCx3mVtl-TfkDHDKzsWFdbZhckVE1xDb4qlnL3m3Cm5Nlzj0qslIqrRKpw3ruo7Cmvyf49phGy3Iotm6ZozYyxzQpnDthZoI6MRq0QuaYKXZ5HAuqvTUYe16uvrCMnZ_x1Rp_Ifoz91nevK6Uwj87jqPNFvPQD3IjvsCrGFAqZ3NEnOdDlK_hYOMgsCds_1vsiUkFq-GUG9HOYH6EhrXZszLPEPYPTeGOq79TlbE_LW4oRE0rcAubwbL3fUQsqzLan3rpDustdRG7VX871zrGbMyUiTbeyGnbhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فووووری
؛ لاپورتا: ما برای آلوارز پیشنهاد جدیدی فرستادیم و امیدوارم در مورد تصمیمشون بازنگری کنن و این پیشنهاد قبول شه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97357" target="_blank">📅 17:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbd905f72.mp4?token=iO6sYsP5Fm-yv7ZJOw5TTn66NHWAeIhXVhfIEFWbiYhJVpM8te32IUl39Y-dZKK6lgTSGRm2MsEem9TepprwB0N-XIFoIXcjtUfc2FZNho4eopPqxHH6vE9J3pPT3WMpJVCdOwNdL6TXgnt8LB5fxi7jW48GgYU1R8RMeWM8Cdu3MF8-zrAm4RWfOtqBwKRc6fkLuOR5WdiJaaQARjuwjAtPpNROlPILnvNiX5lGUu8DOCE3w43KJHPaBnC-asV800Xcq4TAbdkf98wmoGD6Y31YEWR7KE9Tj6HKvHS53zV2KogLz9zRv7acQ89PlJVOLRaefFn85GJVF06npve1mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbd905f72.mp4?token=iO6sYsP5Fm-yv7ZJOw5TTn66NHWAeIhXVhfIEFWbiYhJVpM8te32IUl39Y-dZKK6lgTSGRm2MsEem9TepprwB0N-XIFoIXcjtUfc2FZNho4eopPqxHH6vE9J3pPT3WMpJVCdOwNdL6TXgnt8LB5fxi7jW48GgYU1R8RMeWM8Cdu3MF8-zrAm4RWfOtqBwKRc6fkLuOR5WdiJaaQARjuwjAtPpNROlPILnvNiX5lGUu8DOCE3w43KJHPaBnC-asV800Xcq4TAbdkf98wmoGD6Y31YEWR7KE9Tj6HKvHS53zV2KogLz9zRv7acQ89PlJVOLRaefFn85GJVF06npve1mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ارضا شدن دسته‌های ارزشی از دیدن هواپیمای تیم منتخب ایران در آسمان تهران
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97356" target="_blank">📅 17:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW4ZRB17h_YpygBTncaGrT8lLrojE1roLfRUb9R4FIpZDY93IMrIUhadHf5Uf4p3VtOzzNUABLhvtq9yczJLQSG9dhOW98NwE1JKVv5aPZI1Xld-YYRcMVHxApqZuFab_B-8m-31D-rkhn7Gu7bbrn6JE1lJmaB186UAs5uXuQsVR8457qXqY_G_fcgq8y3lTEaijMLFEJbMDjFrtboMDx0yFora5mkLcUo8xJRxMkpSD8mRn0H2uO8nKu9m6toCjglZF_0jeQboQyhzDLxh7xZoBOkVVYErrt67KW1Ggsxnc7XJ-oHiKPdhjpQsbb2DzxTzVzWyldmTrPRU8dTvmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونمایی فدراسیون فوتبال پرتغال از لوگو جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97355" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97354" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLBOIxATTMxw_YodkW84hXWXFjXx8A--BuxZFl-c0UDDkBfa_vLV_vDjqj1rDKhIbxR9OCPIJwDTjNe5IQfW4tmIAVScZEem1R6r2YQOM1pelKAw-9Q5Fg6f-3DXdugYMGED4I507kESqnLZdtajoFZEha2uwjL3Y_pQYnb-BObph6L1eH1_lZN9efY69nK0pCeHYZTvtJeM5QQVdxt5jouWumuQzZTjxGH0nB3xlLPHaHIuqNkUTCfvDhEUgGIRD80Z-vNl-4r3k3Gist6tMVzZc3wlAaRXe-CiG8Efl_aRuJVzj1Hszwspi6Ds5YwnFLmM09zeLpHjA3Mt4hExDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97353" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=uZrf6GdX5PAjTPZH1g15fY2VnkxxK6tZSEtONjwjEN-DHFy2rgQzxIYW1v_wDX2D5vnTTfiH0zqTNhYSNvQMrc-hiIDgjcJfsdy6rny5rYQAq5NDrAVHZcUamv9D3DWXmmgUz3wVx7pArQfnM6swf74UAaH0udCPg975qsYfjmQfv2Q1BV55iw1Uftg5O2xp_VXBUXbTxwi1qrXQTYk0emC6TXyWVUC7JC8I-gAIvRgvl99CQgMkWsBWbiO9wqR17rVkS_sjDgXFhZ_n2_9lH32m4KxhPuCnLhv_38qM4hyqEwHFAkmnaQc3Ltp1CMh8ZmW_ddTx5bpx2xKRL5w_i7seNQ7kDJaXZ73elHlGg2MGf55BAIlSjR0VDf0xz-RGdcgzaOaXkWRxzJgRLksxGprcSGyRKmHrFEa22qkWkIUnem2q0eTKxlaj3Qb-8e6SpxIL909JUAvwoXIvRxTs4tzfKEpr76Ryy-5htw23zPG44v8K6rve5YgGlBsAtgZhrg4OdQXc5qIcKT9D3g8iysUHZG7jHfFACetk0HOoAaKGFzTup5-51iA1vNLTW4PK5k3IczaXBE_r4cAzxmT_PL5O3vyuldvlX3bMH5UpQlTJzsi7Q8IF5X4B6f5RrA66S_99u1K3FUSePo2TGjZ_KNo7d2BhfIitpa_LUumehs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=uZrf6GdX5PAjTPZH1g15fY2VnkxxK6tZSEtONjwjEN-DHFy2rgQzxIYW1v_wDX2D5vnTTfiH0zqTNhYSNvQMrc-hiIDgjcJfsdy6rny5rYQAq5NDrAVHZcUamv9D3DWXmmgUz3wVx7pArQfnM6swf74UAaH0udCPg975qsYfjmQfv2Q1BV55iw1Uftg5O2xp_VXBUXbTxwi1qrXQTYk0emC6TXyWVUC7JC8I-gAIvRgvl99CQgMkWsBWbiO9wqR17rVkS_sjDgXFhZ_n2_9lH32m4KxhPuCnLhv_38qM4hyqEwHFAkmnaQc3Ltp1CMh8ZmW_ddTx5bpx2xKRL5w_i7seNQ7kDJaXZ73elHlGg2MGf55BAIlSjR0VDf0xz-RGdcgzaOaXkWRxzJgRLksxGprcSGyRKmHrFEa22qkWkIUnem2q0eTKxlaj3Qb-8e6SpxIL909JUAvwoXIvRxTs4tzfKEpr76Ryy-5htw23zPG44v8K6rve5YgGlBsAtgZhrg4OdQXc5qIcKT9D3g8iysUHZG7jHfFACetk0HOoAaKGFzTup5-51iA1vNLTW4PK5k3IczaXBE_r4cAzxmT_PL5O3vyuldvlX3bMH5UpQlTJzsi7Q8IF5X4B6f5RrA66S_99u1K3FUSePo2TGjZ_KNo7d2BhfIitpa_LUumehs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرزشیا تو فرودگاه اومدن به سبک نروژی ها تشویق کنن ریدن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97352" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PLqQDb9OAkHGgXGQOxubMo0GMMKGU4QXNEN-gCYJlKIo9p1Ug34OHPwMFZ6oURexat580kb9pG-04yUwSoS7hpOSGYTTcXtyuBXs0j3rQGO2Sk5cUIc8bphezRcCtks2EjYiWjt4CxEvhQHRi_si_svP1wEPMzMUFWqNhxQobyNEvE01MDKItjOoiNbZaC8RbadMkJiUBi7Xgva0q3TARE9bzP-OROQ4l_OG1QcWBsHvElkys25ljlhQU8mn5atNc1672NKeCYnnamK4H-onakdKzPk4_E9j5ECpKgw0jrcRHTDXYwSHWZh3Vb6vvcGmPy8heeu5562so4BpFWiWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تونی کروس:
ما در حال حاضر هیچ بازیکنی در سطح جهانی در تیم ملی آلمان نداریم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97351" target="_blank">📅 16:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a746294c0.mp4?token=ojYol5o9QN3evVXVmmY7wkIjAyd12hGf-uxBxPlP41jcCrJZcagHmgKWbH1KwSdp2T7Lx2OQ3l1qQTxoVXPVHaSVZLuqbTDPoRX5Rgl2ZcOk7EKOowSd2Na0TLjBRuWPfyB5gILG17aEYTpR3xc5m77YgzwpFXgcTR1VWwpUu2Ws4_vt_MqaMULpXeY_AQ3RIX2aDho-T9B2yd32x4pZwwQ_OIBycNVIlXUM9pyYxNce1Qv_FBfq-BQ-1Ebei_nWSGdV2mdgzLHB8xxtjwcray61vtRuxkbx4NBUlJVylfUT1T71vyvwWvxARYFd90w0sqbNEtHAErDEZpV-BbvvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a746294c0.mp4?token=ojYol5o9QN3evVXVmmY7wkIjAyd12hGf-uxBxPlP41jcCrJZcagHmgKWbH1KwSdp2T7Lx2OQ3l1qQTxoVXPVHaSVZLuqbTDPoRX5Rgl2ZcOk7EKOowSd2Na0TLjBRuWPfyB5gILG17aEYTpR3xc5m77YgzwpFXgcTR1VWwpUu2Ws4_vt_MqaMULpXeY_AQ3RIX2aDho-T9B2yd32x4pZwwQ_OIBycNVIlXUM9pyYxNce1Qv_FBfq-BQ-1Ebei_nWSGdV2mdgzLHB8xxtjwcray61vtRuxkbx4NBUlJVylfUT1T71vyvwWvxARYFd90w0sqbNEtHAErDEZpV-BbvvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تبلیغات داره به جاهای بدی میرسه دیگه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97350" target="_blank">📅 16:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNhJHapf2VzNMq7sOTAbNMA9Z-eeouM3iRKQg0128rWJiHLb36hCmNHAV8XffA16m8bCR_TpN06xCLUbUiJNxpshy_wfSiwmedrne3Cva-mco00QMwEWEhHlRRQ1MYm-WMdn1WeI6xoPd-lMSILVnlvODA3BQl_7TG1tw9O3W_QxB1lZPmY4-cyIwY25qQQMYPc48Y8B_UQeR5E_Zv6Q0hDuBG175PUk39DjVkFomqZDQbiVKIR722cO01fSGw2QYrcWrWHvlCRc-MHo2jzfBHX0jlfvBoJo2hONlNp6EnwdJvMO9ouxGxRUGAf55uk_HnLX0cOaTKjMJEwXJb0bPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئیس اتلتیکو مادرید :
آلوارز بازیکن ماست، حتی اگه پیشنهادم واسش بیاد قرار نیست بفروشیمش، من از اظهارات آلوارز تعجب کردم اما موضع ما واضح و روشنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97349" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97348" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97347">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97347" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97346">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91afe7d0a4.mp4?token=CqK4zRP1_lxi5O3X5MQGftqG1N5poXHTCAEvRH2wwBqgej8SONbcrjM3nzOw5lhJOfdrYywWWPtOcFk-oPUIhJlZfdf3SYKongMbZWE5CQ4QFvlBJ4CO9dy8mk-OKJQzvBfKaKdD1vgBDS_tWW-QuGK7i7TjT_zKMffKIUSIGuXygufs3GOaZhZuSRBoC54ZdhSCpdGBI2N9fvpNs95Bora0fS7RhlY1611xz8cJ2Jn7lc0zGPr6NdWuctWRPYkZi2OeTMIwGkphoRyXUc-UAdmaYP-HSlMki82prOzJVXx4nRQH18260gOYN0BqZUYeegrVp4pXRjOEwuTdvm9PEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91afe7d0a4.mp4?token=CqK4zRP1_lxi5O3X5MQGftqG1N5poXHTCAEvRH2wwBqgej8SONbcrjM3nzOw5lhJOfdrYywWWPtOcFk-oPUIhJlZfdf3SYKongMbZWE5CQ4QFvlBJ4CO9dy8mk-OKJQzvBfKaKdD1vgBDS_tWW-QuGK7i7TjT_zKMffKIUSIGuXygufs3GOaZhZuSRBoC54ZdhSCpdGBI2N9fvpNs95Bora0fS7RhlY1611xz8cJ2Jn7lc0zGPr6NdWuctWRPYkZi2OeTMIwGkphoRyXUc-UAdmaYP-HSlMki82prOzJVXx4nRQH18260gOYN0BqZUYeegrVp4pXRjOEwuTdvm9PEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
شادی مردم نروژ در استادیوم پایتخت این کشور پس از برتری مقابل ساحل‌عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97346" target="_blank">📅 15:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97345">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd228c0fbc.mp4?token=PBytgI-_OfjNdHZzn7upolCy4uLYQNTKtvMzgvmsnDf5OXtjlcP-HaXIYn3RQ34lK1m6B_vbWOSTkkfOWjY6SUcIsWP8WVyMQ0cqlUDTZ1bLuiqjWhIy4iInJw7Pxvku6gp_muFl4XOm6tarHX-9sJrIjTIMyscVJsxi_JdO7o9-0Y6XvERH-t5D1rIYkODMmJyZwV8UoiP92wKKapOwARQyib36fRSjSoSF3Wx8if0bHI9T7WJ3P9kQt3JHwa1UK_CdgB8KHtdfP-1OQHx5e3z7vVIL11ovPRO-kjqSh1toue_W2x86E1EtBtLDStQjtI3DLJr9Ffi6REOxfVZanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd228c0fbc.mp4?token=PBytgI-_OfjNdHZzn7upolCy4uLYQNTKtvMzgvmsnDf5OXtjlcP-HaXIYn3RQ34lK1m6B_vbWOSTkkfOWjY6SUcIsWP8WVyMQ0cqlUDTZ1bLuiqjWhIy4iInJw7Pxvku6gp_muFl4XOm6tarHX-9sJrIjTIMyscVJsxi_JdO7o9-0Y6XvERH-t5D1rIYkODMmJyZwV8UoiP92wKKapOwARQyib36fRSjSoSF3Wx8if0bHI9T7WJ3P9kQt3JHwa1UK_CdgB8KHtdfP-1OQHx5e3z7vVIL11ovPRO-kjqSh1toue_W2x86E1EtBtLDStQjtI3DLJr9Ffi6REOxfVZanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👶
🇧🇷
بچه‌رو چرا موقع فوتبال دیدن اذیت میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97345" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97344">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bece496424.mp4?token=YNqfpoV94u3K2ZGA6H51HIYnG_zX37dx0b7XpB_a0cnTUf-kffRbx8Z0v69bJGbwKBnLNoP4vzJDMq4mtQ6lPSO-wywrHvuR2e42au3WgT3BhHklhAPbEhZTDiLV2a0HM1PQGsrUSMGXpALpU5jbUMEZ4a2O-o6Fpl462ec5rw7AgA2fK4jX9sJLIHS-irNlfwK2UsMViwdEgfDkUK-68mEmyEU1hb8lWHSMxJgjaPrfRSX4SOTJkyGfEvvJ1iTgQp14HGeHNnIflQVf1B2TGRfmC4Npk_-5osjDd9U0uwinkQ5oGnrl1nHhwFgcIbSvV3YOx3jJ_tA_FW-crJnmAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bece496424.mp4?token=YNqfpoV94u3K2ZGA6H51HIYnG_zX37dx0b7XpB_a0cnTUf-kffRbx8Z0v69bJGbwKBnLNoP4vzJDMq4mtQ6lPSO-wywrHvuR2e42au3WgT3BhHklhAPbEhZTDiLV2a0HM1PQGsrUSMGXpALpU5jbUMEZ4a2O-o6Fpl462ec5rw7AgA2fK4jX9sJLIHS-irNlfwK2UsMViwdEgfDkUK-68mEmyEU1hb8lWHSMxJgjaPrfRSX4SOTJkyGfEvvJ1iTgQp14HGeHNnIflQVf1B2TGRfmC4Npk_-5osjDd9U0uwinkQ5oGnrl1nHhwFgcIbSvV3YOx3jJ_tA_FW-crJnmAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
‼️
در سال ۱۹۸۳، ریک چارلز و چهار شیرجه‌زن نخبه از برجی به ارتفاع ۱۷۲ فوت (حدود ۵۲ متر) در سی‌ورلد پریدند و رکورد جهانی شیرجه از ارتفاع را ثبت کردند؛ رکوردی که گفته می‌شود تاکنون شکسته نشده است. چارلز با سرعتی بیش از ۱۱۶ کیلومتر بر ساعت به سمت آب سقوط کرد و پیش از برخورد، یک پشتک سه‌گانه اجرا کرد. بدن او هنگام برخورد با آب نیرویی در حدود ۱۰ جی را تحمل کرد. در حالی که بسیاری از تلاش‌های بعدی برای ثبت رکوردهای مشابه با آسیب‌های شدید همراه بوده‌اند، چارلز به لطف ورودی کاملاً عمودی و بی‌نقص به آب، بدون آسیب جدی از آب بیرون آمد. بیش از ۴۰ سال بعد، هنوز هیچ‌کس به این رکورد نزدیک نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97344" target="_blank">📅 15:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97343">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceeabbf9a.mp4?token=nZjmHrUoUeJQH-tGT56h7RTEZLMtsToU2eDFOCbo61iEJxgG57ksZIxwWd42-mYU7ymfNTHmSICB2PgnK3k8bRHPU3lDri75DoBBdNhPp8whMQaFbry1qx97WdsXfh-46ctDgzZHT5XnNzlPQvmIf6l-V1LkAaylJuSshhrOSeUxkinEZmSn0TBNyDW_J84W9eRcCsUNWp1EQRkSuNSeCYY_7PuRZWXydT1g6uQAwrNZrzz77KnnEKn6QHEusf5UorvU3P0C2ULgZSHLwjreQ3zoa70D4zZUru-iZC1KZNzab8vPZ8iwkuzK7MJD2NylY6WZ25sI53qIJJkEAJRL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceeabbf9a.mp4?token=nZjmHrUoUeJQH-tGT56h7RTEZLMtsToU2eDFOCbo61iEJxgG57ksZIxwWd42-mYU7ymfNTHmSICB2PgnK3k8bRHPU3lDri75DoBBdNhPp8whMQaFbry1qx97WdsXfh-46ctDgzZHT5XnNzlPQvmIf6l-V1LkAaylJuSshhrOSeUxkinEZmSn0TBNyDW_J84W9eRcCsUNWp1EQRkSuNSeCYY_7PuRZWXydT1g6uQAwrNZrzz77KnnEKn6QHEusf5UorvU3P0C2ULgZSHLwjreQ3zoa70D4zZUru-iZC1KZNzab8vPZ8iwkuzK7MJD2NylY6WZ25sI53qIJJkEAJRL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌رحمتی: بیشترین ضربه رو از کی‌روش من دیدم ولی واقعیت اینه فوتبال ایران باهاش خیلی پیشرفت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97343" target="_blank">📅 14:40 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
