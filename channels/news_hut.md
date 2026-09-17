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
<img src="https://cdn4.telesco.pe/file/VHa-eR98vradtqzR8xtJ1_vEV2jaCyfVwjGtR31hyK81_MdXJ7QBOXY08NdNlIzf4wMWJ6Q_aQSwYmGGbogK770ent1mXgT53WKauAOvXr8TDp3FacRySC2I-9fQLRY54Y18DUzcSRRbMNSy-bH7akmGC5T6wqIVoyyzJgj6ouCreAEE0j-qHz5RWM7abKaPv0aZTjBJZdW9fscOsMFuDXopyw_7hCp1GoTQPaA5MLzfKE8tH_ee9fYINbcCU7SpHBNheb2OKn7fWGB_xllKx5KPrVjTvanS-2eeX9oiIZoACGMAqGqcBljNesxcNzVsAJkcmNbwMPAGpZsCuPJ0GA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 13:03:18</div>
<hr>

<div class="tg-post" id="msg-71767">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0a15Cb7HfDskf4tHZPXhz0OVTHphwVZBKRHSuE8e-_933pQCmpFFWZnysBfYVrN_YKhRUwl1nJbLAeYb0cWGG8Z7hgvuCVd50DKN-EWQTAzepfIT77KYpyXxkbryofbOA6k6OpLwtCcFRfEbvN7z3ExwtsmFT4R6U6gHo5oKHckcaqmrH4XBcyl05dXkG14kMdttt_HAnWo2fToVGVGgrXDmHpxuzQ2J4l6eETri8NgW04Ol_kZwErDr2bnUP49SKjqyfhCmMtS5Y4mddZWKwcjbkt9vy2OTSn6m8TgpAFQ86c4-tYQRjrNPPQ5N7-PBmHydlMERJTVs5lbJK8X0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک به اونایی که بالای یک میلیارد تو حسابشون پول دارن، کارت سفید میده!
@News_Hut</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/news_hut/71767" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKNFXQD22cKhoEG-WYi84hKg0RhVjcghh5VI3QRhEGA3E0OTIyHIAbu2N_AFHpB8bE5pU65qsFxQahcmtZqV5oqvzF5qC3S_A5ytACddmpfMXQ1EYdSq2jpDfftBEdMTJz4fk-EkH226grJvKgmL_zdxosGg0igGkCpuaRs0r8FnjrSrM_JLF9ZYOf_O67Fgaia-Ui971Z5jFhn_Gu0ae6PEaureEI9taCzgldJI8FzFjusxNyBgFdbPFn8jQzQxCJ_0kULykyMc0NImsLyhko5o2jfWA2X0srVaCdvANExky7PjSEXY8kj2ZmC4zzmLGUh4pTNTXScQE3dm3nBMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6wrSEmVWq9ckxF5edkQ-IYDvK7OmqwfXToANRUtuUCL1FwgbkTs7FKQuG92SQrttFhDzQD0OsVIZO990doWXurxKVu_1zkC1NTJIizJTD9bxbfURjQJ8iONDqsbYU7zXshgW56_gNSNV9VDA8zUpTBySWz6mGsc6MNhUKmV5ZfsIKTkSYd8uY5e7qPemHmKcoWp1QlWJAUhjNJLw8547E98wdnxyAmiScRm3bdmvE7xFgD7I7LHtnG9GTGTDHXLBxw-qKt-P_6MNKZiAgzStH7YHAxF0GFbFWBNLZ9hBKGk-lxZ-_9fgPVuzt7esBSYip3VuLPnbmIS79zi4gYnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBvMert7ND8fhHPgspDJhg0tWz9TEBIGOx72qW92iKHmHxB8Q2yX6PJ2SnGU3EG1BECk06CHvBoSsBEDOxvGDA0kKv2AgabGzc3NR8qJSDqfXJPD7V-cmd0q1iAhZWlY-TIwCKK_o6Cl1PZRLaDfYvy3ZlCnxnd4nBFGI1DI9m_YXK4yd-cW3TQONH6E5k764r0Yp5nclcDmkPDAzwfyBFWgYgdKryhpWOi_7E9UQkWeqnqyvwKN0sjeEG1B37vR1XqxKQzB1p4xZhYZLUbzMs4sYgHbsZ_PF-1PpSCXQ-gDZ1ieeLjvn8LfE_HIXo43PSZOlVinUggnaDO8Ac5ZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMrMwK1ROC_79riddj9VfghCbdXLzOCMULMg7p17KidE6QlIczffGGcHrEL7WSp6KyfgodPSEYcSc_x4gSQA8VS05Nkxfrfg6954HdCshJRZE1NTMfxtR0FpHr5x78P3t0IWdL4Mx2aYsSyVSOwSZmo3CILQr7A1EqKHJ_n8xLpQJ1MNFvBYautiooJXf6eY2DNrKAHsTyIy-NOKBCtugcqDwEkcarjsEgNK0zFiR3VaYtuB6H3l5vJxc8h3saheIyhnDF5PlwmS2AM89UJyihVi1NSCXRf8gUBVpB3vEJy1uovv5aCyQO89F6GSqTGPEATMLDP0CXiHvfhMtgi68Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز ۲۶ شهریور،تولد کمبوجیه پسر کوروش بزرگ و روز پسره.
26شهریور؛ زادروز کمبوجیه دوم، پادشاه هخامنشی
کمبوجیه دوم، فرزند کوروش بزرگ و دومین پادشاه شاهنشاهی هخامنشی بود.
کمبوجیه پس از پدرش به پادشاهی رسید و راه گسترش قلمرو هخامنشی را ادامه داد.
مهم‌ترین دستاورد نظامی او، فتح مصر در سال ۵۲۵ پیش از میلاد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/news_hut/71763" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNnP-0AlN55vdKQfinAhKfsGx-WGfNBHQHWeAUGRFNbbvh3H5i_Lrcn7nQXMA1EHlYQ1nE8eg__GeZJmANpQYZeVTbLeznhCncf7wVLT20c_eMIrX4prWGGM0ef5vBtAWY2W3vh0Xy_slP4AvfI146ck_hZlhOixjM3uHSWLBvSehLErDpA7NAFj_AnCIuKkW8tKDDeNaTr4ydwlmiefG8l5ckgKHjGBd7KDp7mIzO0TeK9pNnPv2MLDx3fcZaO_qia-yCaF4PnSTCJXr1G9LyZdyv36DA5JPlnpcQV-IgEHJNNlHY5ntEUxucFt5eqSVevy1QB7zHlg0PhY2Z5bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=MSU-2qu0HljiIXKguGYCRidGLJis7xyUvwjfP2RhocKFCdDMSoxHqGHqMy4_3ygUsvwC3HUrCjBaokVkTdOd0eZj3UHmCAmGCoEoteSCUCls39fIr4q5ndaiYMYyNCC0vTY3-rWf7Kt7TDoviGxvs1OHBIFSgdrJNyNyDkClrx7PXNIU0ImLMoX1Q5KzoBPZg9TxAwyQCGp4VU1DkhMd_KzY9FKvdRJaypDGok4YgB8W2AE09p5gig4_G2zBbZiS0Dv4BBsSrVjPDXNpYd393CciEG0t4la5vHrv4Dk9BY0Ow5o_EycLkImCsPRPV9A717BIrN2Wojn3GtUAuN3Ptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=MSU-2qu0HljiIXKguGYCRidGLJis7xyUvwjfP2RhocKFCdDMSoxHqGHqMy4_3ygUsvwC3HUrCjBaokVkTdOd0eZj3UHmCAmGCoEoteSCUCls39fIr4q5ndaiYMYyNCC0vTY3-rWf7Kt7TDoviGxvs1OHBIFSgdrJNyNyDkClrx7PXNIU0ImLMoX1Q5KzoBPZg9TxAwyQCGp4VU1DkhMd_KzY9FKvdRJaypDGok4YgB8W2AE09p5gig4_G2zBbZiS0Dv4BBsSrVjPDXNpYd393CciEG0t4la5vHrv4Dk9BY0Ow5o_EycLkImCsPRPV9A717BIrN2Wojn3GtUAuN3Ptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اوکراینی شبانه به یک پایگاه هوایی نظامی در منطقه روستوف حمله کردند که منجر به وقوع انفجار و آتش‌سوزی شد.
حملات پهپادی همچنین پالایشگاه نفت یاروسلاول را هدف قرار داد و باعث آتش‌سوزی در محوطه صنعتی آن شد.
این پالایشگاه یکی از بزرگ‌ترین پالایشگاه‌های روسیه است و ظرفیت فرآوری بیش از ۱۵ میلیون تن نفت خام در سال را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/news_hut/71761" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/news_hut/71760" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZSKIghoUhonbP_-GlX9jldNEbmfUuW1NvE5_BXHngVDVlDkeojQuHw1bmRCzJoZUuLg-Ub3AtA_8oOkvd1fxrwGCh0s_NgboT5T58_mNr2ZuvhuDHFSX-YaE1hvrbNRzm3P6KzaVSrn34mkihO5J9EHzyJrLGaCJwjVQFGeF4xrLG5m2GtJ0alYLeMCpTMtyrwPKv2DP6hPsZmWTP3ICRNNrenPjdQnVE-nuP02L_d-TmA8Km18QkFZ6dGEe0tomuLC4Twni5WtAtbrDyVUwinRdx0_sTvk0FLvqbzfBzyRyoZE7nJNLZFjAGbhZKuAzlvotCIdXSw7F6eFnNPBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/news_hut/71759" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=UQjRmU9X08Q30VYX1U1gL3Mx4BFhw8QO1H8SBIqAylPxEAVIXdI4pcyvL6HtlBlQNhtZNkLnduTb4LvuRIJ9ZkH0NJJL7I2siGIAXDxXKdvrgkfCPyLinBDyvRDFucB2U3kiZcFMnMhFeZ09CqUwdelsKWoyl4rUUHy4qGgLXgUNEmbeXJTfCbuEK0oPRO25mUq0QCH1uzX_dR6NqvmCVSMqAKHCytikjx5oKIwXeIe-c4buT4iEwiti_BR_0DfNPPwwlO9w-FcE31-FFydwZ6ZgxnAFT9LvcppFkDQRqXkbKeRKf1wSaXbaAuss7L77n_9PCYy_RYV4Q2UxGQdLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=UQjRmU9X08Q30VYX1U1gL3Mx4BFhw8QO1H8SBIqAylPxEAVIXdI4pcyvL6HtlBlQNhtZNkLnduTb4LvuRIJ9ZkH0NJJL7I2siGIAXDxXKdvrgkfCPyLinBDyvRDFucB2U3kiZcFMnMhFeZ09CqUwdelsKWoyl4rUUHy4qGgLXgUNEmbeXJTfCbuEK0oPRO25mUq0QCH1uzX_dR6NqvmCVSMqAKHCytikjx5oKIwXeIe-c4buT4iEwiti_BR_0DfNPPwwlO9w-FcE31-FFydwZ6ZgxnAFT9LvcppFkDQRqXkbKeRKf1wSaXbaAuss7L77n_9PCYy_RYV4Q2UxGQdLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی یک تک‌تیرانداز در رقابت‌های ایرسافت!
خوبه که این یارو تفنگ واقعی دستش نیست!
همه رو هدشات کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/news_hut/71758" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=fyb-JFgVyYqLAmUD-Vau76_mAZ-D4sXBkEZsfS7CWUp70k7W6aaRgcq4hZv47snmkqr9JQOIrkw5HN6sRCYnzqxFOUsxjcR6JlKBLykTLNIFM5NdZC71ovyNZpSZm-s30Wm_ImndHLDqlgq44ayMysXP4zNsJ1g-BKPoFvQqkgbjGxHFTGhwCmR3EnYJi1bDBqY7EHLF0ZCB9zuncdinDD5lZ2PKk8XQzXD_yDlaRNgFyzm1NZWPQC_9ozctiQQQQxV7FKk8dEhNXuaSMYh2s3HgiusNkRvEeC7s8fxALGIdZYUJOimtf2cEVW763rXAqQ28fHdQ7kQHIxT4HUxLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=fyb-JFgVyYqLAmUD-Vau76_mAZ-D4sXBkEZsfS7CWUp70k7W6aaRgcq4hZv47snmkqr9JQOIrkw5HN6sRCYnzqxFOUsxjcR6JlKBLykTLNIFM5NdZC71ovyNZpSZm-s30Wm_ImndHLDqlgq44ayMysXP4zNsJ1g-BKPoFvQqkgbjGxHFTGhwCmR3EnYJi1bDBqY7EHLF0ZCB9zuncdinDD5lZ2PKk8XQzXD_yDlaRNgFyzm1NZWPQC_9ozctiQQQQxV7FKk8dEhNXuaSMYh2s3HgiusNkRvEeC7s8fxALGIdZYUJOimtf2cEVW763rXAqQ28fHdQ7kQHIxT4HUxLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات سالم در تیمارستان یمن
@News_Hut</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/news_hut/71757" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=kPk5cPzaiHjyavB4oG4VPlbJaJEPhXbQ68_WhYYzB488B_TTibMXWmWb_CCLkVC20-QgqU4eZ_Eg--GCjeL2rDyVrl4lR59Yh-ADFZPPbB4hbEWt5eJ_GKHhf16fMjPopP5Y0SbM9lZwKmWQWFRA9lKzPQwsLCsdEN0PWFzqxq4gd5qeRzw-CsdguhxhD0vzSFTi2mGkLhZ6Urhj0PVHEFXzzUYi8twTyGZVxe5zgXrWov5WzbLJCsL6HK0OXiQwlIYUrE5BoNlTd89m3BHqL6jMxq04fsWLTM6WKIx3r3alyv_MhPlvnuTkfRgITySg9IFBZuiB5wEV2_J81m2tdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=kPk5cPzaiHjyavB4oG4VPlbJaJEPhXbQ68_WhYYzB488B_TTibMXWmWb_CCLkVC20-QgqU4eZ_Eg--GCjeL2rDyVrl4lR59Yh-ADFZPPbB4hbEWt5eJ_GKHhf16fMjPopP5Y0SbM9lZwKmWQWFRA9lKzPQwsLCsdEN0PWFzqxq4gd5qeRzw-CsdguhxhD0vzSFTi2mGkLhZ6Urhj0PVHEFXzzUYi8twTyGZVxe5zgXrWov5WzbLJCsL6HK0OXiQwlIYUrE5BoNlTd89m3BHqL6jMxq04fsWLTM6WKIx3r3alyv_MhPlvnuTkfRgITySg9IFBZuiB5wEV2_J81m2tdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
قیمت بنزین برای شما بالاتر رفته است؛ اما این بهایی بسیار ناچیز در قبال کاری است که ما انجام داده‌ایم. این را به خاطر داشته باشید.
ایران نمی‌تواند به این وضعیت ادامه دهد. کشورشان ویران شده است.
ببینید چه اتفاقی برای ایران خواهد افتاد. نتیجه‌ای واقعاً خوب در کار خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/news_hut/71756" target="_blank">📅 10:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اکسیوس:
انتظار می‌رود ترامپ هفته آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران کشورهای حوزه خلیج فارس دیدار و درباره جنگ با ایران و برنامه‌های مربوط به دوران پس از آن گفتگو کند.
پیش‌بینی می‌شود که در این نشست مقاماتی از عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان حضور داشته باشند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/news_hut/71755" target="_blank">📅 10:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abM9PyP_pesQ1Y6_G-Zc9toCe0My2kzjWpX2wouZAc-IJltpGEtYPsKCYM-lCtGfZSzMDDyFx8P_OG0wV-TaTUEjWYH5i6c0URG2SMNKssLg8BH6JY6_nxmuIXekUa26t0ngvMukqZF78Cvp09gjwQ1cBpmBg4KwtIFq0CeZLmqxl7C0YA-Sl1IQ_j2Cgfb9koxQHjt8Z5kzVHCUrXZ0hiFtqxiDZvgYW--WJjPiIkRn5YwpdDUws0YlTR2mMSsZzIKCIGURM82EdfXe279i03esV6PhSNaIYBvf_WtfCqPNyj0xRslyU-m8g9W9MibrXW-uE9NtuElnaF3pvYcCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cba858231.mp4?token=TmRr0aiaRMBJ6QyOqybP-9ZJTXMyKAtC8fOtl5TuSzfEO3QOrGZMk0Jiph2gZRCUJOni_0eWQY324mz8yhGAzRsWa-EIBw8MIaMTPzHGT8A7uN31TsM72EEh2mILaLaXwmPRnZ3__mQDQBykIPwvTJmDBwIzQs3jTVwd0i_aVcsGpwKu_Jwo5MtI_qSNqqrc-gskSqbELxxwJMal-WHknCz8nnAXeKwpU9cBLHGcNLlw81paiSmbSYrRaeSicmmvCgF9WH6kGVvnD7F-It8MvsDtieLNCyIdYqsHAteZSAe8RgtICIig8ixTNo0YYfi9Wbi_1QFH8Y4yRfxL9l6ZEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cba858231.mp4?token=TmRr0aiaRMBJ6QyOqybP-9ZJTXMyKAtC8fOtl5TuSzfEO3QOrGZMk0Jiph2gZRCUJOni_0eWQY324mz8yhGAzRsWa-EIBw8MIaMTPzHGT8A7uN31TsM72EEh2mILaLaXwmPRnZ3__mQDQBykIPwvTJmDBwIzQs3jTVwd0i_aVcsGpwKu_Jwo5MtI_qSNqqrc-gskSqbELxxwJMal-WHknCz8nnAXeKwpU9cBLHGcNLlw81paiSmbSYrRaeSicmmvCgF9WH6kGVvnD7F-It8MvsDtieLNCyIdYqsHAteZSAe8RgtICIig8ixTNo0YYfi9Wbi_1QFH8Y4yRfxL9l6ZEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">« امیر نوری » بازیگر؛ چند روز قبل یه مصاحبه کرد گفت خیلی پولدارم و فقط میخورم و میخوابم و از زندگی لذت میبرم. حالا دو روز قبل چنان تصادفی کرده که با سطح هوشیاری پایین باید سریعا جراحی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/71753" target="_blank">📅 10:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoQQY08Fw_ID2GPb1amnn4RIOLAPpiDkmFGK9I7lJoaQyt4zwGxOxOMPUQU0r33_WYJCx-W36U-nn-Cwk1lj3bJwSZAgCcVu9LbTJZgWx7gce-vE1ASyw3HfI-FwYjLq_Yc8Obu8jG9frLpdeFsWEjC3AXAgKfNzZuDQLFc-BDwgyksOJzfDfPeVCZ8c4n6n8lDKN3cLHmIWxbzmo0-ZLkDq5n7D7hVFcb-vjizWoaaAclSZBGYmVL6soc9ZimoFZ1qSEdm-gvJbEUAmITQOPM8sno15CAbpC_wX_b8PwgwIQAuNjW-DqPYZlhUZxKf8WPwMcBA4H1NCc_BXbvVMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا بعد رزمایش جانفدا ها توی شهرری عقب نشینی رسمی خود رو از خاورمیانه اعلام کرد
اونی که اسلحه اسنایپر رو برعکس گرفته فقط
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71752" target="_blank">📅 09:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=JHlUl1XD027tWYl6koNzQHINaIOYwOEw1rzC8OkV4VGo8GYS3pPy3Dy6UgMTLUAlfSfFP9sxaFqODjdNnopx2wk2kJsxwq8u__I_X5G7AbBIVfh7Nodx4BkgdaWBhX4x5fRuoxEqYLNwXF2M9SifssCib4GMtpFq_5WneZDJbvxSBSH9plKW4V-shH2JSpkZNIYvNzsTuQUGq-wKNgR9Ypk2_v2SIMje-u7Ds5lN-jX7VaDlw16KVDG6B_ZbQgoIkTL_BnKnApY0QaFqaLfP3MPz5bBX0YW17CuJVtaq5qwN2papzdPRFRn-ZlXg_Yy8htt54KFy8ThADoSalixjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=JHlUl1XD027tWYl6koNzQHINaIOYwOEw1rzC8OkV4VGo8GYS3pPy3Dy6UgMTLUAlfSfFP9sxaFqODjdNnopx2wk2kJsxwq8u__I_X5G7AbBIVfh7Nodx4BkgdaWBhX4x5fRuoxEqYLNwXF2M9SifssCib4GMtpFq_5WneZDJbvxSBSH9plKW4V-shH2JSpkZNIYvNzsTuQUGq-wKNgR9Ypk2_v2SIMje-u7Ds5lN-jX7VaDlw16KVDG6B_ZbQgoIkTL_BnKnApY0QaFqaLfP3MPz5bBX0YW17CuJVtaq5qwN2papzdPRFRn-ZlXg_Yy8htt54KFy8ThADoSalixjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در میان مردم اسرائیل با استقبالی باشکوه
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71751" target="_blank">📅 09:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=EtJOUDquzH6_xnY14pXeg1a5QGhrHH2r5wUW-Uwefm-yXerAVpooFiIs7FPAsIOFHWfzZSJ4lNk9_Tbd1wvROAVnJLzdQVOGyoKstBj8dM98bFaeSAK6_MYyQyme_jro1heXei8MhF6ReV9BGP6hZv7jWjS9TWPXSwLRTqCPD7gKaACmds6gC5Am3HaGHrBBRHlV1SYy4kQAWdNpiCrFU_YZedJxNS-A7iXIe46P3aRm0kSHKmShAZrmZ0uI3Dm6cSawOzYVqMJ33PxK_F00JIkeTwxNvsFj24zzMzrLRHH7q12PaoKWbVMK-Cvvo344a3_swLh4y7N0Nf5ZEicQjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=EtJOUDquzH6_xnY14pXeg1a5QGhrHH2r5wUW-Uwefm-yXerAVpooFiIs7FPAsIOFHWfzZSJ4lNk9_Tbd1wvROAVnJLzdQVOGyoKstBj8dM98bFaeSAK6_MYyQyme_jro1heXei8MhF6ReV9BGP6hZv7jWjS9TWPXSwLRTqCPD7gKaACmds6gC5Am3HaGHrBBRHlV1SYy4kQAWdNpiCrFU_YZedJxNS-A7iXIe46P3aRm0kSHKmShAZrmZ0uI3Dm6cSawOzYVqMJ33PxK_F00JIkeTwxNvsFj24zzMzrLRHH7q12PaoKWbVMK-Cvvo344a3_swLh4y7N0Nf5ZEicQjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=QbzkGb98kB_zHD6kYsYugXZtd72nwsNZ4y6CfR71gB76lat7D8lBg4cElu2DS-ssORo8AH5f39v2ZEONsUrZQWGVDDQ-qTRGGy-RVXhT3nK1Pf_IwDPUyhdMz4LhSI6-fJemM0Xagch5aJpkrtYU4oBwplHVzrBQ8FA78irxozsjiz3Sbcbu2ARRkjElngZBiQACsQRH0Y9lNchtlGowmSOOM99DDOeJi5XPaNY7p4RSq7K9C2sTBLoy8DMSccFDMOVBo9ZNvhmM5PxAIMQbfBq9_dciLIqMvSjvriDEO7FU5PGtIpFIh2tTaMtw_04QT8fg62kek1Ju6vjlRHt9hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=QbzkGb98kB_zHD6kYsYugXZtd72nwsNZ4y6CfR71gB76lat7D8lBg4cElu2DS-ssORo8AH5f39v2ZEONsUrZQWGVDDQ-qTRGGy-RVXhT3nK1Pf_IwDPUyhdMz4LhSI6-fJemM0Xagch5aJpkrtYU4oBwplHVzrBQ8FA78irxozsjiz3Sbcbu2ARRkjElngZBiQACsQRH0Y9lNchtlGowmSOOM99DDOeJi5XPaNY7p4RSq7K9C2sTBLoy8DMSccFDMOVBo9ZNvhmM5PxAIMQbfBq9_dciLIqMvSjvriDEO7FU5PGtIpFIh2tTaMtw_04QT8fg62kek1Ju6vjlRHt9hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwpWSAQaqKz5WgJlRrxug1TGwVjpRdLWXQDaepaN_UD_H60nGLOLnUOJkej2mp8Hr7lPDLQlKx90VP11YigIRNZL5vn1HZMFdU8B-VpeCakr1Xy5b50balhjJlCjWlTQTbikwF4USv376-bulfpNybIRp6EENRLvGK-HK6s9he8Xgf6eOHs4FNBhGbT9OmgirlQzXrCgL19GgxLt7EfCN98aZnDMkQyVhtG_Qc5gMUDitBLYSH9G1KEia07rVTgjXfJVbAgSgl7xr_CqQwbNh676QEM9gz995I4AvgPRDrYw_nw8R9-Ln0XQpL7oWponSW8u6bLegXi-Ll_qbLfKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=hEwv_Qzyw7444A_YH2BZZijpmXs67JtuvkHBlUVG5GxbwbwxGG0KtJMcnUTfiMWWYKcCgnT50Pn0mhfVkpM7aFMSmj2svAiBuUSeAtZ7vLZVeKVhlE2IQ6mV46GhbRXV-ROwwbS5i4bzkNkD-WsfOqPokrd2A3hlO3I4DEIcHL-moWGb2Q_1X0WsBLUyBBEui_7DN_5DE0K_CCXoaL3frU3q4mITwrDWHdnvjT1f93FqrJA2SrZvsDx_ghiycMvPsryRcUpkCgmoqSjV9cH1nxa--hUegIlJJo5CtuAaxE_hlRhUsO_c-NwFzZ3PSDXt5h22zVE3__egqqYTBTygwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=hEwv_Qzyw7444A_YH2BZZijpmXs67JtuvkHBlUVG5GxbwbwxGG0KtJMcnUTfiMWWYKcCgnT50Pn0mhfVkpM7aFMSmj2svAiBuUSeAtZ7vLZVeKVhlE2IQ6mV46GhbRXV-ROwwbS5i4bzkNkD-WsfOqPokrd2A3hlO3I4DEIcHL-moWGb2Q_1X0WsBLUyBBEui_7DN_5DE0K_CCXoaL3frU3q4mITwrDWHdnvjT1f93FqrJA2SrZvsDx_ghiycMvPsryRcUpkCgmoqSjV9cH1nxa--hUegIlJJo5CtuAaxE_hlRhUsO_c-NwFzZ3PSDXt5h22zVE3__egqqYTBTygwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=rigTkHFkbmeEhC_XxdF9NTGAshucOCP7f0C_gRUJC5pv2Bhbe_VHYhCPnKFqhpJ1mhmbaJ844NI6kbQ-EQls8KsSwayFtH83yzEoF7xoc-hUfG_MOqH4VB5b5tLqkF-qyrOkOfgMy6oqLKV0fsAi8R23spX8sUXMBhkuRH1VjN6KBAI80M-KLLxJJy8IMrQ4wODWWuMEhYX1QoDkv3oh6dxnxUYx2cwKZVoFjJilaGqM1duxg8BcU5tSf_hfE-v1eWW3DLLcgbKtHoRPZyKTlp4vGpjm-YDmvbYjK3nLCKTwuXrrPrdK6Bq9YxjNsbMXyPKrM0YEgcr7UV5qiO31uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=rigTkHFkbmeEhC_XxdF9NTGAshucOCP7f0C_gRUJC5pv2Bhbe_VHYhCPnKFqhpJ1mhmbaJ844NI6kbQ-EQls8KsSwayFtH83yzEoF7xoc-hUfG_MOqH4VB5b5tLqkF-qyrOkOfgMy6oqLKV0fsAi8R23spX8sUXMBhkuRH1VjN6KBAI80M-KLLxJJy8IMrQ4wODWWuMEhYX1QoDkv3oh6dxnxUYx2cwKZVoFjJilaGqM1duxg8BcU5tSf_hfE-v1eWW3DLLcgbKtHoRPZyKTlp4vGpjm-YDmvbYjK3nLCKTwuXrrPrdK6Bq9YxjNsbMXyPKrM0YEgcr7UV5qiO31uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر از همه شانسش یک‌جا  استفاده کرد...
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71745" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=ZjoZ_KcJNv5nkrSeCmBDv5CN6difjTqVS5Mr7i5Evm90mipVBUXZYNPqM5dDfOWFqyQ_-b3fBZRYoJA5C0lu9gQhwa1U2gbRGO-LTySrT12mh9P2bDIpte89wXjhbQ5oKMLWbhIjO5rR3LUP6z31kV2aeizHxi9bqlLeb7uxRuAHSHIDX3rupwiAGvGWP2sfc5Dr3eLy_ioG97wVkXRDDKtk5x3yLWOfCnkHh_Syie0MKesh9L0st6Jw328ypl7jroQQsT8N9G93bpbjyWnbsujBj3bt2VD3nOJLXxPRJO3QGp4A9ERYukN4fG4r3FHk6bsxQ0lAkZ5FWp_Rh5ZWeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=ZjoZ_KcJNv5nkrSeCmBDv5CN6difjTqVS5Mr7i5Evm90mipVBUXZYNPqM5dDfOWFqyQ_-b3fBZRYoJA5C0lu9gQhwa1U2gbRGO-LTySrT12mh9P2bDIpte89wXjhbQ5oKMLWbhIjO5rR3LUP6z31kV2aeizHxi9bqlLeb7uxRuAHSHIDX3rupwiAGvGWP2sfc5Dr3eLy_ioG97wVkXRDDKtk5x3yLWOfCnkHh_Syie0MKesh9L0st6Jw328ypl7jroQQsT8N9G93bpbjyWnbsujBj3bt2VD3nOJLXxPRJO3QGp4A9ERYukN4fG4r3FHk6bsxQ0lAkZ5FWp_Rh5ZWeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نکته‌ای جالب درباره جنگنده سعودی که در مأرب یمن سرنگون شد:
شماره سریال (5529) روی دم هواپیما قابل مشاهده است که تأیید می‌کند این پرنده، مدل بسیار پیشرفته F-15SA ساخت آمریکا با ارزشی بیش از ۱۱۰ میلیون دلار است.
این هواپیما دو‌سرنشینه است؛ بدین معنا که شمار پرسنل اسیر یا کشته‌شده شامل دو خلبان می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71744" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=i153gskJwT4AWFMJ3VU9hKpPReRJMIEhsfDfpTILfxcQlfmnDO8UQHMdj_6EXlRNeGyCzuJcKg62pVMkndScsK_eqSPymfRc5j9hczJFwjukTnikaNdMgXCn17x8BaJk46yIdTVtUWHFUWE8dQKF6RcJZfAdnJykRoaHH2c7gFs3Hb6OXD8zxJggMbvbVj-IH1dIv-3evn-Kr8FYn5unSxxa-Xa9EGZsTElYZc6tlNjrwZRM9E96w0IY4ElNKomi5xhzXR4g31X62HT02GiJQLodeYXgrLmi7zONuMC3PkzCHN8rU90IIMj0VGdFzfsBDXAlux3ioxepX4W6zhGdPlnKLlmiWzvHivdSCNEMB83XZnRMaQTT5I81QNubCxdIhVPwDGUhFRrxtd4qCoVzhbgE51UTQXfOH88rbWZTv9x6pDn7aenCxE3AVe10K-dxG1_surmNRDAlvEJ2MIorSMxES7pXfyfL9URlr9YTZub8wCj-MgL5gBX2YxS7ZfCFnCREWSWquP-20j_n6Y93Coh-1JadCPONIR_K2XqvubtRgQmWlKB74CgspSw4upnQ71obuSaAw6LueSYD5cfYUSAoRHuBVuz1j17kY4hd78TPnq06tPnS-NBmwLr1HexFjIlEW18RSZXpOjZ6Uv9cPKiknj7F8yvycIA6KTBm4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=i153gskJwT4AWFMJ3VU9hKpPReRJMIEhsfDfpTILfxcQlfmnDO8UQHMdj_6EXlRNeGyCzuJcKg62pVMkndScsK_eqSPymfRc5j9hczJFwjukTnikaNdMgXCn17x8BaJk46yIdTVtUWHFUWE8dQKF6RcJZfAdnJykRoaHH2c7gFs3Hb6OXD8zxJggMbvbVj-IH1dIv-3evn-Kr8FYn5unSxxa-Xa9EGZsTElYZc6tlNjrwZRM9E96w0IY4ElNKomi5xhzXR4g31X62HT02GiJQLodeYXgrLmi7zONuMC3PkzCHN8rU90IIMj0VGdFzfsBDXAlux3ioxepX4W6zhGdPlnKLlmiWzvHivdSCNEMB83XZnRMaQTT5I81QNubCxdIhVPwDGUhFRrxtd4qCoVzhbgE51UTQXfOH88rbWZTv9x6pDn7aenCxE3AVe10K-dxG1_surmNRDAlvEJ2MIorSMxES7pXfyfL9URlr9YTZub8wCj-MgL5gBX2YxS7ZfCFnCREWSWquP-20j_n6Y93Coh-1JadCPONIR_K2XqvubtRgQmWlKB74CgspSw4upnQ71obuSaAw6LueSYD5cfYUSAoRHuBVuz1j17kY4hd78TPnq06tPnS-NBmwLr1HexFjIlEW18RSZXpOjZ6Uv9cPKiknj7F8yvycIA6KTBm4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار فاکس‌نیوز از روی عرشه ناو هواپیمابر جورج واشنگتن؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71743" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مجری از خلبان آمریکایی میپرسه چی بهت کمک کرد با اون وضعیت از کوه بالابری؟
میگه هیچوقت اجازه نده کمبود انگیزه باعث بشه از تلویزیون جمهوری اسلامی سر دراری:))
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71742" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=Mo0WCNF3Ahte5P2Nd9hNBi9L9diC7_c7TQpwusMr4NehkSmJOVva2bewzlG-gev_oYgCiTHacdCcvBLUut0ypdwP6iNMCYxpvmfC6fXyVW9KIvBIYQSn3SFwjP6RcDULbF4PK5xEgjQvVQrhldUyHKAEw3AHolqQtZYQMLp5mcF2MDbOyEH_lb-XXRg3VtEK59Uhjub5ALFV0Q5DPzWeygRev_5545yBaKyxryuYCxtDPlS-6U-F7mZWMoIX5-yXFjW02nZbPDYfNn3c2vZ9crjRdi5hEqz2yAJ5ylFaPxNldCkcEg6WAHEif34orkbRVqVVTaOtY1EQiaIX6fV8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=Mo0WCNF3Ahte5P2Nd9hNBi9L9diC7_c7TQpwusMr4NehkSmJOVva2bewzlG-gev_oYgCiTHacdCcvBLUut0ypdwP6iNMCYxpvmfC6fXyVW9KIvBIYQSn3SFwjP6RcDULbF4PK5xEgjQvVQrhldUyHKAEw3AHolqQtZYQMLp5mcF2MDbOyEH_lb-XXRg3VtEK59Uhjub5ALFV0Q5DPzWeygRev_5545yBaKyxryuYCxtDPlS-6U-F7mZWMoIX5-yXFjW02nZbPDYfNn3c2vZ9crjRdi5hEqz2yAJ5ylFaPxNldCkcEg6WAHEif34orkbRVqVVTaOtY1EQiaIX6fV8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله مرزبان بعد از دریافت جایزه بهترین بازیگر زن در جشنواره ونیز، جایزه‌ش رو به زنان ایران تقدیم کرد و گفت :
میدونیم که سخت ترین دوران زندگیمونو تجربه میکنیم ولی نباید ناامید بشیم
یه روز امیدوارم رویای مردممون برای آزادی و آینده بهتر به حقیقت برسه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71741" target="_blank">📅 20:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71740">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2env_GZjwfKzR0en6Xu2ebrFjjiIOgU4vIdt6DxOJoLDJIpiOZ6Xh9zaEegL9FDDoAmB98RMhwSx2V67bbj-V2S_0zYybJEYaz3UwjJndO4aR_lBHmYZRwxD394hkaU7YxYwkFgD4cLqWR60PPAXUXdyUVu0Q1V1YxqhYt_m-bY5kgT2aNODcqpaH78iYnoP2hz0rzOSgJYAaSoNEwI0R3BGW2kUWBiU_SlAPnkMWDqF5oUZPLqKYQJIbR0qhnMwPKQLkkLfvMVl5a7RDBvTmvOCVa5IJkWllbQVDFibWQ-JuJVhfH1nKUdzPNi-FlSPIaGXI6iVAuNS7j0Ocks6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت گسترده ترابری نیروی هوایی آمریکا و جابه‌جایی مهمات میان پایگاه‌های این کشور در اروپا و خاورمیانه امروز!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71740" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71739">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزارت نیرو از پایان قطعی‌های برق خبر داد؛
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو:
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد!
بیناموسا میگن دیگه خاموشی نداریم اما هرروز داره برق میره
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71739" target="_blank">📅 19:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71738">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iACmsZGePxlMo6MJDj5T7fx5ol983vfyU7BTB5bMidZSn8kkVpe1SR3oDskotu5bBJKW-xuApcLOk5kxEMBzz6uo3jUxs4A2NWd8B_SHJkk2GXGgPu8W46Yr-ruuHEENgv6aFX7wg5Mo1FoW5QN74wl5CTsOyCk4NW4V543oL9cjccLDmxra_zASTPrO-Yi7WxTeUHXuGqiO9rJ6sDiTIVmqhB9Peh_lD-Knu0VTkWvJJ9nPa8RDuU7oD0SDuEQjn7Wg9Z-KjGQXBkWdsXZEf5pgO0D06xaeL1_EAYuGAz3UK_lgdwiqwKrqj2e3_vlCbiqiplzsiQsZO-qA0lSa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، به «نیویورک پست» گفت که مناقشه میان ایالات متحده و ایران ممکن است ظرف چند ماه آینده وارد «مرحله‌ای بسیار متفاوت» شود؛ او با ترامپ هم‌نظر بود که این جنگ می‌تواند «بلافاصله پس از» انتخابات میان‌دوره‌ای به پایان برسد.
ونس اظهار داشت که تردد در تنگه هرمز به «بیش از ۵۰ درصد» سطح عادی بازگشته است و استدلال کرد که ایالات متحده دیگر دست به عملیات‌های تهاجمی نمی‌زند، در حالی که ایران همچنان به حملات گاه‌به‌گاه علیه کشتی‌های تجاری ادامه می‌دهد.
ونس گفت: «این ماجرا در واقع دو مرحله دارد و مرحله اول به پایان رسیده است.» او هدف اولیه را نابودی برنامه هسته‌ای، توان نظامی متعارف و قدرت اعمال نفوذ (توانِ قدرت‌نمایی) ایران توصیف کرد.
وی افزود که مرحله دوم، جلوگیری از بازسازی آن توانمندی‌ها توسط ایران و در عین حال حفظ ثبات جهانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71738" target="_blank">📅 19:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apeV68qyoOPErigKe1NMJMej3K0Yh50RufINYjmJtPhcg0cXBSqZcowkCZE89x3Xc994LzbfxyZMRF54m2QP-X76H9jIa3Wnw2TZFF5N7wUvWM7JrCDxq96b2Wd6bOZW7DXifZ2V1bxzvLcOvYMgICPnWooMyd8iIYyWueIcsrDAauSYbNtiKhb2F-JyxVdTQruK4NxoWN5dZcQ7_sdI49Jm10J7lbka_ZxAfFgVttAkl3rSR-ru8J-qnuvmggJ5zB729mMcHFUXZGE6dbIm69RtCQoYO3S738W0xr8_IcPPhFg4gL7L41wn5wUZXswSvInj6JdEz1c62bfTTek81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bao42zozIJkvHyZ7ixLEXhZkDiNUx900lxwTti4d48fe7uL2TaUdwGfah029mmbGsufxHiyiqkPwQpiHIQhwBNlMwKg-IQfOWx_IXT3YXpCEM5EDh5q-DM6_m_dH8vu2t6-YWMgk4G6C2Y7cagfzg98Y8S80O23tkLTD0ZiZY-zUogYWtVvYyrzngOD87DRDNch2PARuANp0FEzHaS900sqq7w32yfV02fYha-8rQy1OzzhqmW3UEglebZPA9V7bZxEuboS2XwQs2SvEVgK_i43CuMG-jq_q_eWnOSgRlGzQSW41jjTfSuoPrdVuRDqMecwGpf8eteB0dkbSLBGvoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=AKZfWx21y1b_e_aiGXF9F2JxZCX701qpe94jSgNXqFH3jb4Bt-mLZ2i5WtM_BY2EcoUWbDf3FSuqY73NmixV2Q5pV48Rn8iC6YKDX0pnf4TKCuSkYwz-iSYoc-L3I39D-Lav3C0aaCTtg6PVNN3uiYYqGULR5jqY2zDTDcvJS-ZT2KAWxT8t3TzRkTDcHw6_KHlhqqftDUgDBRFYvDSoZd_sBB_7og3HGQo5yQJMskKDNcpo8D8ws7i-xgGe68-C9rS6TeBeDaXuO1CLcz6PM7Kli8SrTwIrczlVZfOoMilzR-iKAe4lMlJtvroDEN0vVcEh8I6dRPphe4lnZU5tHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=AKZfWx21y1b_e_aiGXF9F2JxZCX701qpe94jSgNXqFH3jb4Bt-mLZ2i5WtM_BY2EcoUWbDf3FSuqY73NmixV2Q5pV48Rn8iC6YKDX0pnf4TKCuSkYwz-iSYoc-L3I39D-Lav3C0aaCTtg6PVNN3uiYYqGULR5jqY2zDTDcvJS-ZT2KAWxT8t3TzRkTDcHw6_KHlhqqftDUgDBRFYvDSoZd_sBB_7og3HGQo5yQJMskKDNcpo8D8ws7i-xgGe68-C9rS6TeBeDaXuO1CLcz6PM7Kli8SrTwIrczlVZfOoMilzR-iKAe4lMlJtvroDEN0vVcEh8I6dRPphe4lnZU5tHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71732">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQNJ-__BaFbRmtpxOCXAxwsj6x2wM_2-gjM7DfHO-djrfGDAvltkzmHYTHZvChJ-bZBsD3m6dOrQesm8oQ5CVFbPfFZ_A6FFqyx8swNYYHHcIfVeI7gnJ53eH3ISQyu35gKwZTbjc1dbFUFbJmXAu6WzI0LBty2sGK2j6mhcfv4EstwU7vDt64Rzeq_VzAoiNHlvkv9h_5VkQ4urs8gunSO_T8VLP2uR1w8UZtel_9i2Q34aJUemsGS_iOC1JZG-N0V9BkDWeYOQVrmwc28zjJov85PvEIg-NQbJDDfCMj8gPX9PeGRJKjX2zIZdRAoSQIva3XlgoQy7lythOMNeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71732" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71731">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=o_cS7KaDC9YXlOb4-vOTogvNUZKBfOm-cpIGJeQ1GeA1LelSxxy9V9xqxKlimNb7IEeiVJe4tP8ZCtx1JC6WMPLkwwmWV99si4RH1EIP551bDA-9nQIl_bbgkW5m6aN41gLjC5aDCVi2-nWYHfIl6IoKalqtkf7yz-vU3Kmi-U_Euava0jNF5RE9LOtxH4m5c2ST_Y7_aJaejTTSqMwayC6mjPhITAqt0SePaBm69Ppns78ujQCc-ZNmFmdwNDYbfHjNq5OhcwQk6llobctgY_FdzOJM6Eveai8zbWR8Pkfld6YyiHsq7H2G9s6UWjVuK7IlcHqQPescZuvbDjOgMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=o_cS7KaDC9YXlOb4-vOTogvNUZKBfOm-cpIGJeQ1GeA1LelSxxy9V9xqxKlimNb7IEeiVJe4tP8ZCtx1JC6WMPLkwwmWV99si4RH1EIP551bDA-9nQIl_bbgkW5m6aN41gLjC5aDCVi2-nWYHfIl6IoKalqtkf7yz-vU3Kmi-U_Euava0jNF5RE9LOtxH4m5c2ST_Y7_aJaejTTSqMwayC6mjPhITAqt0SePaBm69Ppns78ujQCc-ZNmFmdwNDYbfHjNq5OhcwQk6llobctgY_FdzOJM6Eveai8zbWR8Pkfld6YyiHsq7H2G9s6UWjVuK7IlcHqQPescZuvbDjOgMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71731" target="_blank">📅 17:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فاکس‌نیوز:
یک کشتی طرف قرارداد ایالات متحده در نزدیکی تنگه هرمز هدف حمله‌ای از سوی ایران قرار گرفت که در آن از چهار پهپاد و دست‌کم یک موشک استفاده شده بود.
این حمله منجر به جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد.
تعدادی از کارکنان آمریکایی در این کشتی حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71730" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71729">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeJwKBecWeh-UZwLT6BEjC324XgvPJgR3qIp8uMjdRgHoDH2XQsEM5OAe7zBAyFrQSzCwS4C6HAVNGw_2fMgAUrLJrW2q28W6pTvlSoKfNIuPDTQPnio79lk1NBmE7MzbDA-_DoWGmyJNOgeia5oiWlN-mNAXARO4vt4CD0F2GsZHnrV0j5dr6tgrblDb2SN84rGPcSxGHypbViDOzUQuCD6pqvyb_Ui6JAuWDNPY3RBk50oi4ScvW4LKMKJgA-GB5ItOM7apdJk9YA8ynMxWkQV658OtR4hglDk9jLNaR4eJif-y08b5o0bo7bbJozSW79bQrciicsukMu17rVyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در تجمعات شبانه:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71729" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71728">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2421361f81.mp4?token=gFv5jUUJWZIdH8dUnBpJul7WIEB8uIuc3gZtfTrMsUUq-M4TXb8mxbHUlW5yXQb57A6lwoglsJY7UNFX1cCo9L8uTy8Uhukx75azNJvWls2priRcv8Q6ex4pt28z9sLO9gLYTlHrUae9FiQ6nZoFMH9qHa-jhsiAUrJBYKEbQJ9IszAy55FG0TojQqcQZRj1bw-x8sAQCRcg4ZI8-qoadGrfSR49VG9cDQaE5yEntvjzIcpfIqhxbBpXE8MWcJEPy39A9bYhU584QPKd7q4j2wh5ae09IrqBiinH9aHz7CzPLZQ3T7xn9mNMX29gmeYc6NovxB07-KoDdRaqP6HhSo4-8F9aLqeYTCgy_7Z295A14pZW0cMrj75bBQgtEll7U91WW8wDDCyZBB6HkZilzDH-8gsLDqcABgpl_SfgPTYqu8Sddac4Ha-8zVsLDUDDvxFivYLpTFurlehLjceZ1Lv0nX38IjG1CWTOimTChaWpCxn75d_N3-HG8wZ_YekGCjUHpNqA7aE9bdlevRgh3QVU5XTtotQqUoEV0_Dv-5liJRvxuIg25x1wPUutxwklGU3LVnU3bVNNtRkOdKjgcID_66AkQsnx9f2Dqo8VOJy4UT8GXKFb0uxPzGnMA3r7Uiup0LUceGlzQ3mVySLXZH1ZANLLITxnjalNdhCn5SU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2421361f81.mp4?token=gFv5jUUJWZIdH8dUnBpJul7WIEB8uIuc3gZtfTrMsUUq-M4TXb8mxbHUlW5yXQb57A6lwoglsJY7UNFX1cCo9L8uTy8Uhukx75azNJvWls2priRcv8Q6ex4pt28z9sLO9gLYTlHrUae9FiQ6nZoFMH9qHa-jhsiAUrJBYKEbQJ9IszAy55FG0TojQqcQZRj1bw-x8sAQCRcg4ZI8-qoadGrfSR49VG9cDQaE5yEntvjzIcpfIqhxbBpXE8MWcJEPy39A9bYhU584QPKd7q4j2wh5ae09IrqBiinH9aHz7CzPLZQ3T7xn9mNMX29gmeYc6NovxB07-KoDdRaqP6HhSo4-8F9aLqeYTCgy_7Z295A14pZW0cMrj75bBQgtEll7U91WW8wDDCyZBB6HkZilzDH-8gsLDqcABgpl_SfgPTYqu8Sddac4Ha-8zVsLDUDDvxFivYLpTFurlehLjceZ1Lv0nX38IjG1CWTOimTChaWpCxn75d_N3-HG8wZ_YekGCjUHpNqA7aE9bdlevRgh3QVU5XTtotQqUoEV0_Dv-5liJRvxuIg25x1wPUutxwklGU3LVnU3bVNNtRkOdKjgcID_66AkQsnx9f2Dqo8VOJy4UT8GXKFb0uxPzGnMA3r7Uiup0LUceGlzQ3mVySLXZH1ZANLLITxnjalNdhCn5SU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیویس کیس سخنگوی سابق نخست‌وزیر اسرائیل:
دیکتاتورهای ایران ظرف چند هفته سقوط خواهند کرد؛
دو هفته، سه روز، شش ساعت و چهارده دقیقه دقیقاً
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71728" target="_blank">📅 16:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71727">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=JGO-D1d0QwL0Ygm-mf8L70_3J3zTx-KI4MY8AHlQiCJ-eblWFca0Awad4oQRQN9ibHSa9SAcuD9lHrjQG5FiDfTXiOmJqyK_aigtl4mENPfp11-1cWY5AYSFx-BZkeSde7K_s-tjl4J0YqPN6f--OE3oNAf2KX1khC6uG3hGMSJtY6jdupxsxfTFMDjcUrMncT2NrWiKHTNcXcm48Jyhc3AEJmtbanRTi31le2Cy8WhnLfbSEkQw6B_mOEG1pvtN2XGamLYwSTrHrjLYbBNnycflEEs9ExP7PFnOBShatUzTxj4RqTZiJaAP8tYvnrF3Ud-k2Jiiri_3nSNZG3QX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=JGO-D1d0QwL0Ygm-mf8L70_3J3zTx-KI4MY8AHlQiCJ-eblWFca0Awad4oQRQN9ibHSa9SAcuD9lHrjQG5FiDfTXiOmJqyK_aigtl4mENPfp11-1cWY5AYSFx-BZkeSde7K_s-tjl4J0YqPN6f--OE3oNAf2KX1khC6uG3hGMSJtY6jdupxsxfTFMDjcUrMncT2NrWiKHTNcXcm48Jyhc3AEJmtbanRTi31le2Cy8WhnLfbSEkQw6B_mOEG1pvtN2XGamLYwSTrHrjLYbBNnycflEEs9ExP7PFnOBShatUzTxj4RqTZiJaAP8tYvnrF3Ud-k2Jiiri_3nSNZG3QX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ دعوای این دو تا بچه گربه خیلی وایرال شده، از بس کوچولو ان، دستاشون به همدیگه نمیرسه و رو هوا همدیگرو کتک میزنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71727" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71726">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=hdecSHLXWph5asYGUquJMQv-QJe_0fDYlGtEEsBoRWX8RjJuhMJxKfFMjAapkWmVbt7BNvSUHe8VkSxLGP3ksaAQipN103kvpeMGDADGIhKyObFLSKTpDy3XXYqfHfEa3TB6BiH-TAQA8Pks0PMKPjjyZgKVmwX7LrQmcEQCzNqInv0RMmYL_-dvzWB7SwOyzxiK-9GJCMOdpRbsp_Wd3MgJogpT74NMZFDfUnTPjrpuZYemyG3scwyvDnVDRZKRScVN42abuK9maBaSbKMyF1VyeUHf9qdjMn9F4tPmWyZIqoBIuAWx-GZ9qIfdp4yjK7k8P7Qqo4T40MJRZtlGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=hdecSHLXWph5asYGUquJMQv-QJe_0fDYlGtEEsBoRWX8RjJuhMJxKfFMjAapkWmVbt7BNvSUHe8VkSxLGP3ksaAQipN103kvpeMGDADGIhKyObFLSKTpDy3XXYqfHfEa3TB6BiH-TAQA8Pks0PMKPjjyZgKVmwX7LrQmcEQCzNqInv0RMmYL_-dvzWB7SwOyzxiK-9GJCMOdpRbsp_Wd3MgJogpT74NMZFDfUnTPjrpuZYemyG3scwyvDnVDRZKRScVN42abuK9maBaSbKMyF1VyeUHf9qdjMn9F4tPmWyZIqoBIuAWx-GZ9qIfdp4yjK7k8P7Qqo4T40MJRZtlGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه رستوران تو آمریکا باز شده که تم بیمارستانی داره و تمام‌ کارکنانش کاستوم دکتری و پرستاری پوشیدن و اگه غذاتونو کامل نخورید باید براشون قمبل کنید تا خانوم دکتر بیاد شلاقتون بزنه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71726" target="_blank">📅 15:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71725">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=BrSwmY1tzPnuiEbR4HPZJyXs2VkPR4WgsIjVkZmCXt2d7M-KBt_Sjt2LzE9UGbnkFxwAobWnQPCURgKz71vBdjeSb7TUo1NbmxJLsLFuzTnIyQACdzub9ak3qB4GnTTYvJYMRsIZnSIO3C4YoLTwwhGDNPfz00ubTaQfHV61YD9IgRxa7hHOjgSKn2uQ4Oww6sgu08VN3ZfYTfCVU6ZoyZeGkYMx6CrYH_grvHSHKTaNsKtmHlQwuQI5ilqgJkOsaOcmP8B2oNmOHeUhaFcUMaNRcDw5FcsEGHtXfj1Y0SbRdyJxC8sr-fZY8Hs6ail-dybcUFfM-JMre0BjKbjo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=BrSwmY1tzPnuiEbR4HPZJyXs2VkPR4WgsIjVkZmCXt2d7M-KBt_Sjt2LzE9UGbnkFxwAobWnQPCURgKz71vBdjeSb7TUo1NbmxJLsLFuzTnIyQACdzub9ak3qB4GnTTYvJYMRsIZnSIO3C4YoLTwwhGDNPfz00ubTaQfHV61YD9IgRxa7hHOjgSKn2uQ4Oww6sgu08VN3ZfYTfCVU6ZoyZeGkYMx6CrYH_grvHSHKTaNsKtmHlQwuQI5ilqgJkOsaOcmP8B2oNmOHeUhaFcUMaNRcDw5FcsEGHtXfj1Y0SbRdyJxC8sr-fZY8Hs6ail-dybcUFfM-JMre0BjKbjo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71725" target="_blank">📅 15:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71724">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBircfuAO4fQzHEkv24keVbIIcFATHGqTWbWSmqiLimpf-nUCUNF1FdALPIMHo7DzlwkBW-SI_RzTFkVT0pZ0wCaQ-jgJDToLG0ZuUn3kw8zLvbMgTdThKbXtZpL7YGu6dgsmKPLTg09N2aLCHuN1oqGgDq4iFx94IJI3k97oCByNF9cf30_vt2d5myiAKSmknUxgnLZ1c-mHZZFdetTsD_2SW1bxtCUv3QCo4cJDD0N7q7Bb3OL6QWKg1UieZhKysyYZApxUiRlmiq24XJkce0w2aaRNVwjPnV7jqwmX3g57ODiLOwnBwOZkocaIZ-CRGkVhjn4xYifna887_UD1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛  سامانه‌پاتریوت شیطان‌بزرگ مانع شد خانه‌خدا توسط حوثی‌ها نابود شود!  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71724" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71723">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=oPY3whaWuoxiLL4qg8vdKDKG13Xz8p-FTXQdJ9Y5uTCCsTTmy-axF9Lcg00Xr1nPWFxJww1nNmqOylKYCFSdS14sxcL7bhZXfP92gjYE8EnJZ7KeLt1li3OCkIGT4hty7d8U-koRnC_ByoMwxvt3xBCflI01yOuuBxBFy8L4d8FjlvYRAsk27ALfvb0z2ALa80tNfn3VIZZlktjmn8PCGhosMoTc8aPyAK8qPKbv626pIlfioCovZE7oMqYtT8OYDKSMivljM8QOdPk1iU160MQJE5Uf4Tk2U9V30FnESEov01zy4r6f1WaGN8kTigXa6UsBFYaFPov9JrETMSkHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=oPY3whaWuoxiLL4qg8vdKDKG13Xz8p-FTXQdJ9Y5uTCCsTTmy-axF9Lcg00Xr1nPWFxJww1nNmqOylKYCFSdS14sxcL7bhZXfP92gjYE8EnJZ7KeLt1li3OCkIGT4hty7d8U-koRnC_ByoMwxvt3xBCflI01yOuuBxBFy8L4d8FjlvYRAsk27ALfvb0z2ALa80tNfn3VIZZlktjmn8PCGhosMoTc8aPyAK8qPKbv626pIlfioCovZE7oMqYtT8OYDKSMivljM8QOdPk1iU160MQJE5Uf4Tk2U9V30FnESEov01zy4r6f1WaGN8kTigXa6UsBFYaFPov9JrETMSkHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛
سامانه‌پاتریوت شیطان‌بزرگ مانع شد
خانه‌خدا توسط حوثی‌ها نابود شود!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71723" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71719">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7dNxcSUyAkuiFcY9FYd2jAisy2gWE0Q7zbHqy08JDZ9jNr0NrX5oqNr8hivlhLDAEnK5PZ4DLUx_wc1794ttfcE_ElbhpholqwmDs-RlISj8DljEfA8AUWeYBf1MOl80q_93GeqvchdugMsCk_Abc0zCfHtIP8VHmqeeCxF1H_WO6d6a4P1S5oCvqWfmFj7_6G6rf35vZcgv_Sllv60PGEwA-u6knU_rCOdtOqPfNN-xPeMS0H-njZy0R7eXOlRg19pP8MrQyedYhvUdBcCYZQhpEeW0qSgC-MGfyBF_L-xcuCR6iMC4MRuGnOPtDupjHEdLQ7x1GrzflJwVwmBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pW12F1okZyW41x2Th-2ai8PNirE9wBFFzGg-OAtL-sPXxIrneESWx3FFXZ0RDtGXajS13sCCSKmx66pDp2MTcBG5s7y0PBEYC2J3tw9hU0eK0s5lz96-BI9X3iBI3nKwvFDkypNRZNy9ot6nU2Geqg7eIOTxMUeyTH2X6C2DhBzU2xDugEcMx9fKo6mw5Q9rRsqJFerGDXdVs4KvSow2I0-7TH6WOvtz48hUIh9UvHjb8Fu4gDozknrXqOee8p14PhXoKtPdsDs4FpXYu_EHLrcmNpsRClJQabwXo-aZkfsEX3EHptrZLhMDrTGluK9izfRZWfhHTu7I3Ps6HTYE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSqxL8dyUaTmptnwg16rHmEiMOLdUc2vVPewk1MDC3TqFVm_MOuxqTCBNfm2wTUqkkCrChL6Ae1wWXztAb2aGXrKBpy43oCTB5vqG-OkZakmGZ7C-183lOWlRiONpnjMecVGMsKILQLaDxE7irT7rwuq5-0MOqnKg4LEaA00obz3v7nCbgk_V8aVMyxmYnUFtztv1pDQryYyW6mhHQW140mHE5K0JtS0PAp_JFZCRa7G3tlJjFmMtFWq9TSwQgPDWYzg9uAW0bpITSb6kvpMkYvL-uVfOjptRmBwSbMhM3vYvvnSq1R5D6vLda5iT4f8Wo-nOf1Jt32wvg7qMJtwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0c61SOWqDCkBmcaRRtko9loo1qi-BSuTDp10wsgn0cUGceoZAeVLtpoyJFTS8PYw507aXUmArOOHSqCVhHwMg2IdE8HS7KinFmQt1Rt2v4lzMy94ZwIayjvtAGR31p3j1FbfPxv40iPL8OFUgFeQa9fsHvHjAbCzKb69Snpq9sV9shYJUMMyQx5itmZUsU3zrA3t7vajPZ0rnbyBpmLgUrh7nwTRQGTJcXiSIDncD81jiL1Lx4FdcOSLaLmh5dL0hDpfbXliHgJ8EXLiyeV1qjv48ZB9zVr_T1jmVZa128Lprp7SrvKZriUFbuTOY3NzSWQyFuymIjbwYn2pwKe2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های اختصاصی که توسط سی‌بی‌اس نیوز به دست آمده، خسارات گسترده‌ای را در چندین موضع نظامی ایالات متحده در خاورمیانه پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
این تصاویر که توسط اعضای فعال ارتش که ناشناس هستند، ارائه شده است، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده را در پایگاه‌هایی در عربستان سعودی و کویت نشان می‌دهد.
در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای بوئینگ E-3 Sentry مورد اصابت قرار گرفت و قسمت دم آن جدا شد.
در کمپ بورینگ و کمپ عریفجان در کویت، عکس‌ها نشان دهنده پادگان‌ها، تریلرها و وسایل نقلیه آسیب‌دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71719" target="_blank">📅 14:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPV_ThVzibin24K3RtXRiKS3WnzmfphiMZYrgAAOUHOOclDeNZ2jU2Dh6B1r9cPG94p9A7UTkYKh6vxb11CccvCRTs_JOuf304cNJPMaxbL73mYNAdmEh_04WKKEvTtd4uUvXcyYF3SetPw_fN0VEVJlmnf_-D1A_WNOTSX5ibNlMdFk664k_1xUuJPVGKPjQ95GWCrXihIdofbLC3v9g4mZOpJFD_7BYVdDYjHDUA3tCM7qPUkOd3uOXk9jHwh2aFi4Cv3E_oV9zcrfCcZvhx7wZZQ5hdyGtyXI0vT696it5qoY2Wv0FoE3m_IBNsoaAPNyxFH-hxZB6CPHJfd5-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=CDte3JUZ9fCe9cWKs7r2nrwZstEASZIlyxLdfNgb0JxnjO2O_r6_vqonZKISDPHZm3btmSfdP1uPQ-z3RiogQM8TOGZ2e28Ofk7YjZ2D7DnG9GxxhRf6QFdSed8myjfqULV9HWllwmDvv90EOp_p5EOGch2ET27pf-UHg529XZakvtR3HHDGUZqPea8lG9P2tnfTlrv1v8IRhBgfhSxGOaEp2NOULj9OiV7ypwmEISKC1EOQ5I82vhi0oFMycwjDuKY71JG90AGT8xsDXuHzNnueL-yc4DWzVfmOoxoSUK52YYkIamraD5sgMZ9KhsGTIJXVxQJw2uwq7qjxo9LnTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=CDte3JUZ9fCe9cWKs7r2nrwZstEASZIlyxLdfNgb0JxnjO2O_r6_vqonZKISDPHZm3btmSfdP1uPQ-z3RiogQM8TOGZ2e28Ofk7YjZ2D7DnG9GxxhRf6QFdSed8myjfqULV9HWllwmDvv90EOp_p5EOGch2ET27pf-UHg529XZakvtR3HHDGUZqPea8lG9P2tnfTlrv1v8IRhBgfhSxGOaEp2NOULj9OiV7ypwmEISKC1EOQ5I82vhi0oFMycwjDuKY71JG90AGT8xsDXuHzNnueL-yc4DWzVfmOoxoSUK52YYkIamraD5sgMZ9KhsGTIJXVxQJw2uwq7qjxo9LnTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwHrECYnHAS_CDASpM1IvvINJ1hE2Xb1ps4R8FErxf9noDYhz4lx0DOROvLw-C7yrAFlWUqynm6g7OaDdFHFa1VLo3kTRDRYvGOSCWhzao1-FbH0NiI3q8Y1eWagrIIoWDchsOVkrxcDc4rG_mL2qBxzwuPhfjVmHivPbfBwBJhTWjj89lJuDIg9-3ex7t6iZyOgstOhaam15V7km6yd7M3LUmoYq2w2TrBy-pqXT6KrkXVgXxa2wSWvWj5uk7P6DAeRoc8o8u7nMCVkI4fubffYXJc9hocrql7P72r-IZNUFEITmDp4aR_1DsvzixK5L2do4ecHloqk_Gu-7O4JaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71710">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB8il_6tmWslpkX5-gKCOpWwVCEbROuKWldXUyqab73xcy4O-1E6hiyEXg1hRol-8h7K6fUJKm8yCdc9V2aMPDLLi17KXVMyF8G3ZGRQYjktRWcmURVL-x_kKAKyKfaeSLdUX9gyYC1goY7b3Gigm7ZftjYYzVR-N2zDethUXBF2yzE0AZ4ptB44f8xgv_2-yxROZ1zjxnNPsg60Ja1PGd9Z4URNaJ6QXQSp3FSEqdDB8OrRyS_8FMnXuRUk6ZYnLiGfSvKzxiYAgKngSU_b8FIpzqa-3R1IzID4n1XQbcPLwejZBtaEV5iITvRMuVtCBV0Uw83IwFuQS-DEeYBA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده برای اولین بار تأیید کرد که سلاح‌هایی در مدار دارد.
مینک، وزیر نیروی هوایی:
ایالات متحده اکنون سلاح‌های کنترل فضایی در مدار دارد که قادر به دفاع از نیروی مشترک در برابر اقدامات خصمانه دشمن هستند.
از بیان نوع، تعداد یا زمان پرتاب آنها خودداری کرد.
نیروی فضایی می‌گوید که می‌توان از آنها برای "اختلال، تخریب و حتی تخریب" به صورت تهاجمی یا دفاعی استفاده کرد.
کارشناسان فکر می‌کنند که به احتمال زیاد، پارازیت‌اندازهای فضایی یا جنگ الکترونیکی - سلاح‌های جنبشی - مشکلات مربوط به زباله‌های فضایی را ایجاد می‌کنند.
این به دهه‌ها ابهام رسمی پایان می‌دهد.
اولین نقاشی نیروی فضایی به معنای واقعی کلمه یک هواپیمای فضایی را در حال نابودی یک ماهواره متخاصم نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71710" target="_blank">📅 11:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71709">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26353c8137.mp4?token=Nz3TlVz--gYJ5eCm2dz4o6q-DqRLhKgQswYfxqSTA45GKCHlJ_LRGZ6cYPcZE40JvRkSsR7DGvFyS0z1UpG8wrE8FC94w6QUyqYpin0zU5rcsf8oZ-ZD6eQAzKxtL8B6ljzXULt4uZFVzBq4HrcyogqfBWEDL3Z2xK4wAWwPtemwIp6tuIqF6R58_SXghUCx2P94K1dBtmUkSC87Bcfp5B860k5dQyOEritRsw_aoz2MVx2F1ZIcI2hbnDgQmMdbefqugWwBsOAobCPcvwx0L3Mr9AQqBC1v-bSicqmZRCzPSJT_-BZwrCwBjnCPrCcgM3Hbg7giDQiq2dk5KHxp8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26353c8137.mp4?token=Nz3TlVz--gYJ5eCm2dz4o6q-DqRLhKgQswYfxqSTA45GKCHlJ_LRGZ6cYPcZE40JvRkSsR7DGvFyS0z1UpG8wrE8FC94w6QUyqYpin0zU5rcsf8oZ-ZD6eQAzKxtL8B6ljzXULt4uZFVzBq4HrcyogqfBWEDL3Z2xK4wAWwPtemwIp6tuIqF6R58_SXghUCx2P94K1dBtmUkSC87Bcfp5B860k5dQyOEritRsw_aoz2MVx2F1ZIcI2hbnDgQmMdbefqugWwBsOAobCPcvwx0L3Mr9AQqBC1v-bSicqmZRCzPSJT_-BZwrCwBjnCPrCcgM3Hbg7giDQiq2dk5KHxp8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک دانش‌آموز دختر برزیلی بعد از اینکه نمره‌ی خوبی تو امتحانش نگرفت با چاقو به معلمش حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71709" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71708">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=NTwYkH2l7jLwMaQYJ2YDC-PakDF4tfZGdM-c06LPz3MxUzd9VnOKoVPrAmQs0PY-hBdaXP-YmW5sPfLZLPFlW_uFzt-a-tCB_UdJhgSVxb9AlC9V5iiL35hWovVqDFAE-MqkU3lDrgjflN4CkQtJuQeu7S7jYOu5Dh5PoJGHn3gTEXcaR0mzdjIKRcAx8bsMiMQObUqr1lrQr13fz76FAIjZTPT1IhWn72Njdg2OmEoGZnQddln--WNYh3jTEa7HE7qThmcQrW8Q2jOmkvbSBxNaoRXsYuD0LAlDbE4pbsv88OnKu9NZOALkLKFYz-9rk1eVe1DlQuG6i9aQwbHrdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=NTwYkH2l7jLwMaQYJ2YDC-PakDF4tfZGdM-c06LPz3MxUzd9VnOKoVPrAmQs0PY-hBdaXP-YmW5sPfLZLPFlW_uFzt-a-tCB_UdJhgSVxb9AlC9V5iiL35hWovVqDFAE-MqkU3lDrgjflN4CkQtJuQeu7S7jYOu5Dh5PoJGHn3gTEXcaR0mzdjIKRcAx8bsMiMQObUqr1lrQr13fz76FAIjZTPT1IhWn72Njdg2OmEoGZnQddln--WNYh3jTEa7HE7qThmcQrW8Q2jOmkvbSBxNaoRXsYuD0LAlDbE4pbsv88OnKu9NZOALkLKFYz-9rk1eVe1DlQuG6i9aQwbHrdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته خانم دکتر(روانشناس بالینی)؛
خودارضایی نه تنها ضرری نداره بلکه خودارضایی یه چیز سالم و بی‌ضرره که به عملکرد ذهن و مغز کمک میکنه، باعث کاهش استرس میشه و حتی به رابطه شما کمک میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71708" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKuLbblk-VElTXo-Ss9EQ6O5dmdfZPML9kiR7lZ2_cn91HNc0XGRl2bbmyR8XkBFs2w8IvvzTWtNB-toG0Z06v1eWK8V1rdFWPJ1dbPDjGCrX0ijmiLhOlKVp2z7qiZso-4Wr4cY5YUnSzVEELFV640a5f3OPXqzRV2Yy9vM2p6_KAUKTxLMbZSXb1AOkt9L_QQfZ9mKyGyDYSN2N0A4_nviGP9tjDEP76IJjpS_5z_zo4BSruySPgsfkhmm0_zedAPmjHJYoxq7unwCRAO3qRufEvACAinXAY0pqV7ml05o4K6xIskx7tmFdQ30eF4gjvTN9tZuqnIqEg_pOgAdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=oHIJs3_MtgYP0-xjloNAXIjGOEAdPw1YD6UGp1zXjj8oQ4F7BXiOadbRYV1hbxeArFFW9eHE77Ao-BkhHEKEHKWY0RQj-Ok-FmQW2nH3hJN_jaRnHf3uJKvUBuhZmot45hfrYVvqYdmrO_bxSXd-Mzk2nTWaNY-SpYI49CP_IOdXdGOcSkq-IK2V0tE7mWwZEnXs6P1GnymLDWfckSN5IXVqSGGZnEVPsa_RlYYG0kDFnq9eQ1iO2UZ72vWZu-HodmRWPc2cCedpMn-pPsKDfJiJM1HTXHWdDm2B4ZXx2_hXtCNgIR1Y22sEyhR2tPb8C61vdODlpIEyygHNriWXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=oHIJs3_MtgYP0-xjloNAXIjGOEAdPw1YD6UGp1zXjj8oQ4F7BXiOadbRYV1hbxeArFFW9eHE77Ao-BkhHEKEHKWY0RQj-Ok-FmQW2nH3hJN_jaRnHf3uJKvUBuhZmot45hfrYVvqYdmrO_bxSXd-Mzk2nTWaNY-SpYI49CP_IOdXdGOcSkq-IK2V0tE7mWwZEnXs6P1GnymLDWfckSN5IXVqSGGZnEVPsa_RlYYG0kDFnq9eQ1iO2UZ72vWZu-HodmRWPc2cCedpMn-pPsKDfJiJM1HTXHWdDm2B4ZXx2_hXtCNgIR1Y22sEyhR2tPb8C61vdODlpIEyygHNriWXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر تیک تاکر به اسم فاطمه تاجیک دیشب توسط چندتا دختر که میگفتن عکساشونو گذاشته چنلش خفت شده و خودشو دوست پسرشو کتک زدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71704" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8MW1WgvJakMA3NFzJfGzDmsq0NL6R2imBG1Yu1x9XEaWYpRmBRM6LFtZSBCyEgbnVWTXIjQvPYgxwRzm95qULsa-WOz_OTbeT9uwbDPrB3XS6x9peLfMFVRIV4XQqQG-aV7ezeVSQ05bwMhCiQC0jxqgmeX2yX9KJzb12nvkFifhNQcwEkFGaJ0C6dd6Bt7WUv8WPEKE67Tkfqygi8fix1bvy4Tc03Av5xPtkAPFZ8HPgykKHev-844RX3gvHeBrbpsq-_Ke6eDwbcg9spZ7rGn5I7K9zrmytYxZV6hEro6KRXTEuXjXLh5KxtO3wAnGReVfEAhIZV1ByfUOwlq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس:
فرماندهان ارشد نظامی ایالات متحده، اسرائیل و هشت کشور عربی هفته گذشته در آلمان دیداری محرمانه برای گفتگو درباره جنگ با ایران و امنیت منطقه برگزار کردند.
این نشست که به میزبانی «سنتکام» (فرماندهی مرکزی ایالات متحده) برگزار شد، با حضور فرماندهان نظامی اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر همراه بود.
دریاسالار برد کوپر ضمن تأکید بر تداوم حضور نیروهای آمریکایی در منطقه با وجود حملات ایران، شرکت‌کنندگان را در جریان برنامه‌هایی برای گسترش تردد کشتی‌ها در تنگه هرمز قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71703" target="_blank">📅 09:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht013ER3f2KVA58T0W089JROWPh8tIEhbfyJ-kRNtGruEWMGVAwQPX6SR999SztWSn9AhpZfCdBLkacGcIv6ofwZ6tJf2WAFPyIaakxTecvpJ-c0rBo-ZJrz9HNMYtzCryrN40GBzVwT--JXU77asSjtEBprrcHjbMijszIdR74q3HyPHPriNF6FANePT25u2K6h3_ZkWjaRmsaHGV2zuNYzTN0qAz3O7nvobI_6N808CzQ3cOUCM_6a2Y6sLee8DPo1m5StpM5CkvEXPUEbF23goPBxpwD7rZAs5zRrH-q-qgjcP6rjLCPUGR-QUb_KrIwHBwne09KvC52VbfHzgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhcK-09PxDxFc61gg-EPSpyjQQ_zcgxvNaFHl5Kfn_x2X6Srx0xT61YdZG5-nqf1VLKYT0ttWCd12uy6S6LISdN9Ma-cidfm66ht9K916WXkLJxLGUJqYE8uAsoNFEJpP_Wt2YpkjoYy-biEEpjl3GmfVo_wnANNC_cABfnEndJOXIUjEAFHBTA5z7LRDy5FGMu5QNKpeDCXbSCfVgGaW8Rw1xvY_PS3C-q2zL1asHSDjinwMZvUdFPDAtRnHvpg_ZFPz_ydui4NfCKJ-HoX0yKCA71o60Ph3SetBnQHXcMVkGnab-iLS8YVbqYqigcuUVxD_2GfKJnDNpJ_sRNrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=N7nkDtB6mqAYIu5eMGPg4ACowDr2Wsuf9qzZg3BtVkLlTWmiSLk4cNAAK4nkRXP7I-DFuo8eTdstzOv4olwyNo7ZEaYoTP0S0QNs8jlnN25VAsCr92GSYTAt-fF6FwY3JYstekO0h6dm8tZBLrdbOFfY_CwKAfPcRZl-CDo3c3JRX8Nbx7fJPY45y2CiT916l2EgQA9M7ziJSphvnw4FfZMvMkCMY_qtRx5hbvix2YL8B0quXnkqZzuYkuTFcwmsWPmKaud1qZ26CynZyW1oSfUH3uNEA__qez1O_MibQb3hw9wN8LStLHrlwO3P3Km2XajGahRHrF3tv3gK73XxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=N7nkDtB6mqAYIu5eMGPg4ACowDr2Wsuf9qzZg3BtVkLlTWmiSLk4cNAAK4nkRXP7I-DFuo8eTdstzOv4olwyNo7ZEaYoTP0S0QNs8jlnN25VAsCr92GSYTAt-fF6FwY3JYstekO0h6dm8tZBLrdbOFfY_CwKAfPcRZl-CDo3c3JRX8Nbx7fJPY45y2CiT916l2EgQA9M7ziJSphvnw4FfZMvMkCMY_qtRx5hbvix2YL8B0quXnkqZzuYkuTFcwmsWPmKaud1qZ26CynZyW1oSfUH3uNEA__qez1O_MibQb3hw9wN8LStLHrlwO3P3Km2XajGahRHrF3tv3gK73XxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71696">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ونس امشب گفت که تو ماه‌های آینده، جنگ وارد مراحل جدیدی می‌شه؛
اما در شرایط فعلی همه‌ی تحلیلگرهای نظامی معتقدند که بخاطر انتخابات میان‌دوره‌ای، جنگی گسترده از آمریکا نمی‌بینم.
اما یه نکته‌ای اینجا وجود داره، انتخابات سنا و مجلس نمایندگان آمریکا  نوامبر ۲۰۲۶ (۱۲ آبان) برگزار می‌شه ولی نمایندگان انتخابی، با ۶۱ روز فاصله به سر کار میان، یعنی از ۱۲ آبان ۱۴۰۵ تا ۱۳ دی ۱۴۰۵، سنا و مجلس نمایندگان با همون اعضای قبلی ادامه می‌دن و می‌تونن قانون تصویب کنند؛ بنابراین از لحاظ تئوری، بهترین زمان برای حملات دوباره‌ی آمریکا همین دو ماهه (در صورتی که دموکرات ها پیروز بشن)
ولی یادمون نره که ترامپ یکی از غیرقابل پیش‌بینی ترین سیاستمدار های دنیاست
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71696" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71695">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdTvEhCDLi-0ifOcEL__U6IMzikHCgIKk5WZo_S0mk0kIQ9o5eEphYG183R8HtxbBbTeQd6MrxsHFwMGnKbSnF1aJE34jwM-6TPIlr0pot9xvJNfz3QKgAdxuvz_QQksC9m-H3H18QzTaHjm4zA8TKd_F5gmP643qem1ZmgHujpCWBgxk5nLgTeKcqCmcg8dRYzZKR9MenVf79coXUk5YCT9v4NdnXwojpiNHOSKRVQkn7_iD9C5wfDPYp7JlWPX1zm91O-4nszp0zvIPJFFj0DUughYkJrAyUzpJPx8I_ihNxRRo_YRRSSQRS6LEZv8Z42rVwBgLKxHk5z7mb0XQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلیا هاشمی:  امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت. مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71695" target="_blank">📅 00:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71694">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ایلیا هاشمی:
امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت.
مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین لحظه لغو شد؟ یا مسئله‌ای دیگر…
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71694" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71693">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=roIxfHPDo6yNg109eaxyv8VpMa406J4fctQHgykcKDckv9lbyC4U6vO5oGmUsc4e082_QXfY-02T-KiE9RZpUoYbmiFka_DBDgRBOIT57bAzar354GR4PmgbKFImHSvzl5aQzIP3DU5CoRPc8AgQ0uz0GfMnuQDnm8sFq9to-m77CL5ePB4U-quUR5AUvaIURp6oh8AWWuhwHbaC0dS7EPRSS4FknixYvGblvnEBjewem2gomRU50EqcghvS3ppbvQXzvaJYX4TiiLph127_A6vnbU2WXKJ4O0dvvW5jt5oscYcM59eu2ZXbJu8atxg86QyyTbN9FlfxM0PC1utMUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=roIxfHPDo6yNg109eaxyv8VpMa406J4fctQHgykcKDckv9lbyC4U6vO5oGmUsc4e082_QXfY-02T-KiE9RZpUoYbmiFka_DBDgRBOIT57bAzar354GR4PmgbKFImHSvzl5aQzIP3DU5CoRPc8AgQ0uz0GfMnuQDnm8sFq9to-m77CL5ePB4U-quUR5AUvaIURp6oh8AWWuhwHbaC0dS7EPRSS4FknixYvGblvnEBjewem2gomRU50EqcghvS3ppbvQXzvaJYX4TiiLph127_A6vnbU2WXKJ4O0dvvW5jt5oscYcM59eu2ZXbJu8atxg86QyyTbN9FlfxM0PC1utMUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سریع‌القلم:
آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات نظامی علیه ایران می‌آیند چه دموکرات ها پیروز شوند چه جمهوری خواهان!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71693" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71692">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71692" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71691">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71691" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71690">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=eVSywkqBHan2iqmZ4wf_0FK8oFghPGaYscywq4tkDbChTEn0ji-PGE6H7fTIP-8A1JNEmMplSkO95YAJHIYn29m8RwzRIt-b2sbxUQqSHZdS82d6Sqn1CN60oFJors2a2tfXkpBsq0V3PL24xcGgjviOPQb5SNZIA3anYzyYzLz8-biBXhtIEBLQ8C_XA-tpJHtnZYxVn8rW691tLNeOPeuYIOzM1I9NxjikvCvOujOHZbBu7BeS_h7_hc4l4T7uX9xFtYDWjcznaX-OraCHaT2RKwD5Cx72hWJRzJhwxrHlkce7DCskkm0k9yMbyUgXwECNid7AZ2RCG6d47aV5Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=eVSywkqBHan2iqmZ4wf_0FK8oFghPGaYscywq4tkDbChTEn0ji-PGE6H7fTIP-8A1JNEmMplSkO95YAJHIYn29m8RwzRIt-b2sbxUQqSHZdS82d6Sqn1CN60oFJors2a2tfXkpBsq0V3PL24xcGgjviOPQb5SNZIA3anYzyYzLz8-biBXhtIEBLQ8C_XA-tpJHtnZYxVn8rW691tLNeOPeuYIOzM1I9NxjikvCvOujOHZbBu7BeS_h7_hc4l4T7uX9xFtYDWjcznaX-OraCHaT2RKwD5Cx72hWJRzJhwxrHlkce7DCskkm0k9yMbyUgXwECNid7AZ2RCG6d47aV5Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای جنجالی یه
جنده
: دختری که ادعا می‌کنه باکره‌اس، دقیقا به چی افتخار می‌کنه؟
تو قطعا ایراد داری، مگه میشه یه نفر با کسی رابطه نداشته باشه؟ آقایون حتی توی سوراخ موش هم فرو میکنن، اونوقت تورو نکردن!؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71690" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=OvvE2jvhfWTNjRfQiH7Y-WxT2iymkfD-oKgtXDvz3-REgsskLUATalqncn_UmCJs9h_InUXOFRxlIKsug--pr4iwtUNlbZV0wuDmasBEGSpx5OjoP2LdfkjqWdFieNfV53tC6QPSYziZdwvUATHYV5QKizNwdInEzVs_yUQAfx6qL_svmpywduwv_H0qAqLduFXe3uyZmTSdvuHgLn2j1F2dniEHeb9nDr_181Z6CIaFHgucpJlhBl7oxRZ3u2DJJtEHcjcS6EtCAkKAyoIuwUffjEhGl84hbnF8zRidgJUqmChHh87qt8ZOUoPrMzTojdk3ejujNAUUNBR-qZbdKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=OvvE2jvhfWTNjRfQiH7Y-WxT2iymkfD-oKgtXDvz3-REgsskLUATalqncn_UmCJs9h_InUXOFRxlIKsug--pr4iwtUNlbZV0wuDmasBEGSpx5OjoP2LdfkjqWdFieNfV53tC6QPSYziZdwvUATHYV5QKizNwdInEzVs_yUQAfx6qL_svmpywduwv_H0qAqLduFXe3uyZmTSdvuHgLn2j1F2dniEHeb9nDr_181Z6CIaFHgucpJlhBl7oxRZ3u2DJJtEHcjcS6EtCAkKAyoIuwUffjEhGl84hbnF8zRidgJUqmChHh87qt8ZOUoPrMzTojdk3ejujNAUUNBR-qZbdKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=om9MhAJRJIpL0gBT4iaOxLU_UfTAAW0dWrmc7fqtSSf0sEsnR9RJiJW2RejvEjqbtaKjp4JFDNRV3aR2l3K-sHolc2HbcR9nLf8N8Pfssbk99WjvyulkYlMY6PVquiLSp3_pxJkBHABfYloZdguE4HOASao7O7oDSssOl3C7lKFIk8aOigv67-T64FpdqJfucow5AXn3HRctWEcvQXOkq-v6-saDjOzZSUqSq2-Oa4hWhRUIyJEC0yy03ufUYZL7OaOdaNqDLNU7e4mj_gAsbzA-sZmN0fo_WfBXYsSU1ZKa7I14tru7rRxfkpqggOcBKUAR5ZS_oM3PNv-JZXAanQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=om9MhAJRJIpL0gBT4iaOxLU_UfTAAW0dWrmc7fqtSSf0sEsnR9RJiJW2RejvEjqbtaKjp4JFDNRV3aR2l3K-sHolc2HbcR9nLf8N8Pfssbk99WjvyulkYlMY6PVquiLSp3_pxJkBHABfYloZdguE4HOASao7O7oDSssOl3C7lKFIk8aOigv67-T64FpdqJfucow5AXn3HRctWEcvQXOkq-v6-saDjOzZSUqSq2-Oa4hWhRUIyJEC0yy03ufUYZL7OaOdaNqDLNU7e4mj_gAsbzA-sZmN0fo_WfBXYsSU1ZKa7I14tru7rRxfkpqggOcBKUAR5ZS_oM3PNv-JZXAanQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/61894edf33.mp4?token=dy0iWXgbJ0BETfzSFwQjOAjHgpPaib19NGSVaKuybBxcDePyGDgNPRljqbDWWQh8sbsEAMwu-h0Nvx0KQM38fEOGVIjJBpTXf4t-o7XTtEZPTRj18sBU9hAefr5gXqd4lhrBVQOSNWruz6W_qwHYp3o5rXIAvLfQkLjaaHHE8MWagK2MIpJir92gm8AjEgMI6Ks8v0buERDazniA0DUXcPeVtCpr1kMJSC8gFB6Jc0NEdApIT25FO0gSwcLpRNKsjoculDbeArzqUfi_Wr6g_rf0Tchu8KxzNyrZK-YixoGfYZht5RFPr853yPKCLPYWkHSFm_EPaPQFrelm59VYkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/61894edf33.mp4?token=dy0iWXgbJ0BETfzSFwQjOAjHgpPaib19NGSVaKuybBxcDePyGDgNPRljqbDWWQh8sbsEAMwu-h0Nvx0KQM38fEOGVIjJBpTXf4t-o7XTtEZPTRj18sBU9hAefr5gXqd4lhrBVQOSNWruz6W_qwHYp3o5rXIAvLfQkLjaaHHE8MWagK2MIpJir92gm8AjEgMI6Ks8v0buERDazniA0DUXcPeVtCpr1kMJSC8gFB6Jc0NEdApIT25FO0gSwcLpRNKsjoculDbeArzqUfi_Wr6g_rf0Tchu8KxzNyrZK-YixoGfYZht5RFPr853yPKCLPYWkHSFm_EPaPQFrelm59VYkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، هواپیمای تهاجمی A-10C Thunderbolt II نیروی هوایی ایالات متحده، مواضع داعش را در نزدیکی «جبل‌العمور» در شرق استان حمص (مرکز سوریه) هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71685" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71684">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoCJ9_3oMFnJXhwhYH3OZSOeuu2ZkkMWC2MTSx3Tp8is6zsWO7jSiagbS2b8xF17H-BsV-GRK5pTRvFrY1Xbn24jsnUC80624I2tRSbT0___LajDNAJTEfpbvvoT3pVRF0d8ofoloY2vI-tjpBUAFjAfDTQ9cOWtSgCUDiJeLmVtOjCrmNQhdPbLAieDSdeGvsan4S3nNDNTDYP156_lz7gvr0D1RU8Vm6OoPZqoWj2jrdKkDwMLstsQ4ygopj7xyOofLAnsS27wqCBBl6pciWdIRjOzhAgDJB4Q-ArdmcRj1dMhV19Bk2DN6BBvZh074IHTRXBxtj9AF2m9hFqgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست:
دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از انواع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است؛ این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود که هزینه آن از محل پول مالیات‌دهندگان آمریکایی تأمین می‌گردد.
این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
این قرارداد برای تصویب به کنگره ارجاع می‌شود و می‌تواند آزمونی برای دموکرات‌ها باشد؛ چرا که در ماه ژوئیه، بیش از ۱۰۰ نماینده دموکرات مجلس نمایندگان به کاهش کمک‌ها به اسرائیل رأی داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71684" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71683">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=M3_cfIMknspQaMii28SUm_nLkkEA2-RxLUTE2_lqb2ikLpxT8VUc5xAujyHYGB2L1cPvfNd5OMS5v_sNX_iPXJ-ogWN4Tc4PpqA24QfnoMq-1IZx16G_D-7hNbVkTWPqiZE5Wqt8Ri2HnK1YXd4eQYU1Es3QGln7yIp_gbiWyRtDDiP9p1liY7hxG2C1upW84co-GbNBpOvR8sfZCXPGbF_SK7Nk0CwLlIBT0M-qGpttvxziGTettykThIgmpQLiBEcGikSkruuapGzY9QG9ZI7VgbVrIzVmXgghC0KbKOjf9l_ipkVtRfN3ZDMr71YTTAbRPfRZ-g1ICk4vM0aMQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=M3_cfIMknspQaMii28SUm_nLkkEA2-RxLUTE2_lqb2ikLpxT8VUc5xAujyHYGB2L1cPvfNd5OMS5v_sNX_iPXJ-ogWN4Tc4PpqA24QfnoMq-1IZx16G_D-7hNbVkTWPqiZE5Wqt8Ri2HnK1YXd4eQYU1Es3QGln7yIp_gbiWyRtDDiP9p1liY7hxG2C1upW84co-GbNBpOvR8sfZCXPGbF_SK7Nk0CwLlIBT0M-qGpttvxziGTettykThIgmpQLiBEcGikSkruuapGzY9QG9ZI7VgbVrIzVmXgghC0KbKOjf9l_ipkVtRfN3ZDMr71YTTAbRPfRZ-g1ICk4vM0aMQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از نفتکش «ال‌گایا» (EL GAIA) پس از اصابت به آن در بخش جنوبی تنگه هرمز منتشر کرد.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که ایران ماه گذشته با موشک و در پایان هفته جاری نیز با پهپاد به این نفتکش حمله کرده است؛
در مقابل، ایران مدعی است که این شناور پس از ورود به «منطقه ممنوعه» در بخش جنوبی تنگه، با یک مین دریایی برخورد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71683" target="_blank">📅 20:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbIWZp5cb67GK4GvnpFlPj2L51Gp5aFWE9IT3hqCQVTCPub_OiO9NLWE30ESiLNDdyn1Qth15W1fL4WXAoUr0LNQX4da2ufYFLAy2E7JUp3AltDYr5nqNPtO82pUfiIzyeOsMww0OrCoHlqVPzg3e6RNC8WJn3B1YcBohQUZsuXlkM2zvxtJA640ufpyFAgY0Ji1WFb1O5O1FFkiumjP9b3kaicN58KXCYALHsDKp9JDyd6wpqmdZmWkugSLAlImie27EHMMIv-i_P_2KcAHQLewTh30XzcDs_BrqBzURJnyf3HCuqPttau57WpeFL8_tX50s54IruHgVOOZPAMiGtEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbIWZp5cb67GK4GvnpFlPj2L51Gp5aFWE9IT3hqCQVTCPub_OiO9NLWE30ESiLNDdyn1Qth15W1fL4WXAoUr0LNQX4da2ufYFLAy2E7JUp3AltDYr5nqNPtO82pUfiIzyeOsMww0OrCoHlqVPzg3e6RNC8WJn3B1YcBohQUZsuXlkM2zvxtJA640ufpyFAgY0Ji1WFb1O5O1FFkiumjP9b3kaicN58KXCYALHsDKp9JDyd6wpqmdZmWkugSLAlImie27EHMMIv-i_P_2KcAHQLewTh30XzcDs_BrqBzURJnyf3HCuqPttau57WpeFL8_tX50s54IruHgVOOZPAMiGtEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=TfnrQTMQAS1lYaJcL5RYDmwKq95ji3IFdeEf37HzO1kkpWQa07xidozCbMKOiZa_Ep-LhzWFt8FeMzyXKkTf8Go-3fsL1m3L37xyULWq3Gb0Sxw6L3y16SzMf4IMcNPHT3c4NzvgNMnOZMANndsmC1-CpzfDzHozYOw0jgCmQTx8ZD7kYzBSSOp6EkM2QC7m0TEXOLQxfs8O5AhBjDbuxy_8y3k2FHVEJ35TjXRl0ph93ZbuJClVcS7YZU5nfDZnCYuWzLJvZppBRAdFpJ2e5ySkpeS-AxClnxK9cHH0J3BRBjyLl6ZPYSxgOT_JARFYZouQL4wbuCw_TtMdID91kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=TfnrQTMQAS1lYaJcL5RYDmwKq95ji3IFdeEf37HzO1kkpWQa07xidozCbMKOiZa_Ep-LhzWFt8FeMzyXKkTf8Go-3fsL1m3L37xyULWq3Gb0Sxw6L3y16SzMf4IMcNPHT3c4NzvgNMnOZMANndsmC1-CpzfDzHozYOw0jgCmQTx8ZD7kYzBSSOp6EkM2QC7m0TEXOLQxfs8O5AhBjDbuxy_8y3k2FHVEJ35TjXRl0ph93ZbuJClVcS7YZU5nfDZnCYuWzLJvZppBRAdFpJ2e5ySkpeS-AxClnxK9cHH0J3BRBjyLl6ZPYSxgOT_JARFYZouQL4wbuCw_TtMdID91kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=gMg2sVg5XBBvwvzPO-0cmGsuKOGRxtR_6iPiGDTnODjES7hZVzn7ExmbKHpLLuEVF43ix-4n9n4KN5LMpXZ6wU60mUHurUqD6JbgT-aoVb4RrQaE2_zv6DbJ7K-NmWozwskru-ql5Nfwdkk1GSGD5a_5UdMGVdpubEVgdzs-DkyyI2JwFKCgdFR9SeyQpyO337ZsAhRpYikPxhDEiXbDSxOGQkBFBMINYbOtFLZX7xdL0DMqlP_zZSI5FBaEdVxE9zohp-5wwF9iXxdUou-APrAmg0k82_m0g2iMXsv2lf46YYe9ZB0tTotTiYnb2yWmOvQaoAW9JyDRPlqv1DhtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=gMg2sVg5XBBvwvzPO-0cmGsuKOGRxtR_6iPiGDTnODjES7hZVzn7ExmbKHpLLuEVF43ix-4n9n4KN5LMpXZ6wU60mUHurUqD6JbgT-aoVb4RrQaE2_zv6DbJ7K-NmWozwskru-ql5Nfwdkk1GSGD5a_5UdMGVdpubEVgdzs-DkyyI2JwFKCgdFR9SeyQpyO337ZsAhRpYikPxhDEiXbDSxOGQkBFBMINYbOtFLZX7xdL0DMqlP_zZSI5FBaEdVxE9zohp-5wwF9iXxdUou-APrAmg0k82_m0g2iMXsv2lf46YYe9ZB0tTotTiYnb2yWmOvQaoAW9JyDRPlqv1DhtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhoh93dhu4AdNJzecWHPHNK3rHjnB5w3j3KM7mZuJ81Ww-HJvJLwd4iUwUXyrKvUHXB_wfsFwxLQgd1wG4qFZ96scrFCzRL8txopm6v74hmA4FSn_vOtS2mTfmHXnocR6xihruK5RUMl11re7C7SSVNjY2M1lVl2GOvKFmTEHEVpBbGlMigQ40OdWvF43E48_zCK54N9LRJ9hDVpa669QDFrRTJMNaEbYliB2w084RYDWw3K0AFddGtvD7cJVr19ANHqkZBjH5Hb3cRp6HPm0MfrBovXKe_4n4kcI7LmrDUrRlzm3aLp60E-cr9LXh3F9c48nniAOdlWIlMeoCwuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=m2amh2zrgDDHbjCNl2YD1E09y1brP4HO3ZizFrvnxNCMcdzQa6wQ8h_GFwM6nVKwIL4-vIoud6PWeyYc78FWk9w7PXQwnAgVdIEFIShCeGnNMu_A-3t4utcf9DqULKkn_eBzWWGIN0Axc274h87ia3NvLDIsus1wP_TF27M-yDxeB9MOl3rW4PavZQAdMtMcmYMRgpry3NJvzh7xOMEFfNlVrZ0zJ4KPsHbdunvlD1l4ISsqnaaZ1yLOK9KcOEzX2th78IahLj1zcd6uEUlBC9brhDz0I3lzmjjdJagB8xAP5LWBXU1idr1Vrc4144NjZ2shylEYTTR3MD1b8YS09w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=m2amh2zrgDDHbjCNl2YD1E09y1brP4HO3ZizFrvnxNCMcdzQa6wQ8h_GFwM6nVKwIL4-vIoud6PWeyYc78FWk9w7PXQwnAgVdIEFIShCeGnNMu_A-3t4utcf9DqULKkn_eBzWWGIN0Axc274h87ia3NvLDIsus1wP_TF27M-yDxeB9MOl3rW4PavZQAdMtMcmYMRgpry3NJvzh7xOMEFfNlVrZ0zJ4KPsHbdunvlD1l4ISsqnaaZ1yLOK9KcOEzX2th78IahLj1zcd6uEUlBC9brhDz0I3lzmjjdJagB8xAP5LWBXU1idr1Vrc4144NjZ2shylEYTTR3MD1b8YS09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9T1mr8I7VMj5AQnUbUmX_AIdl2zkYDpwIh70Q6Dp2f6o20iTLGeFKH6XoPPUCwGPQDI_Twz9N2VE9inWDE1ixzoEZiDYI29QodNC-kO5-3il4sRObAlnztBZVrl9r6gNswyjm-ApuHcr9_zEl7kpJ5AXpw3e7or5CwYQ4cZNmLRxILGjJtT_keEKcY8ts9tdZOPuvRegVGtiGGQCjJLKBjXusptDl6ejFXmtE1-oL-d0fEEK9B2O-BMrpbB0IcHkmZ5ppUX4sfdQT5roHx5U8Es9DBYTBQ_56LnkF78JsY4GGP2F0bHtZ1EFfm8AXj27jX74ddEHr0f2GvQ8BZ0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=E4y65jn9Dqs1ljRRhWURxng3B-B60WhOr0AcKVpX9LdowROY6RKqlcYU_fpqgqylNPGhRcxZhszKcFd11WuaPATWy7_BjM6RlvVIGrC4xAUrbnBEKNN2X_rj2KmDayquEXMNpE2leTIS_Of4nQjq6UM1QEd-AAGf4OE__f4jiGVgJnaUbzRh064HpXqzLvS2D3zVomvIu8VibCgk8gLIq4dXdZpgO93MiQ4SG2DPK_qmHLA_qhqa8pm5PDKokDFqGMXo_ayuCOsfisLqYlnx5cFLC9ej_N_dP3LfS08skbKOeb-uofi2nDoBOG6zLKX0Jd1KF9HaDJf-ktTd5T2l2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=E4y65jn9Dqs1ljRRhWURxng3B-B60WhOr0AcKVpX9LdowROY6RKqlcYU_fpqgqylNPGhRcxZhszKcFd11WuaPATWy7_BjM6RlvVIGrC4xAUrbnBEKNN2X_rj2KmDayquEXMNpE2leTIS_Of4nQjq6UM1QEd-AAGf4OE__f4jiGVgJnaUbzRh064HpXqzLvS2D3zVomvIu8VibCgk8gLIq4dXdZpgO93MiQ4SG2DPK_qmHLA_qhqa8pm5PDKokDFqGMXo_ayuCOsfisLqYlnx5cFLC9ej_N_dP3LfS08skbKOeb-uofi2nDoBOG6zLKX0Jd1KF9HaDJf-ktTd5T2l2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=Vst6ZVSITs4U7ZZz10rC4PynBGG8DWffmSB5OW8Ohj1sZaZmIEYLEB7qyTcG6fDc7siiajwOuzUvLblUutjFh2XoLZscBHSJTqNVashxTenMUymXEz9cLxg2wWybi8-9fL9jDFBkSLcmN3tkR44s2bYNvXUS5ReRDc6pbNlZvocLRdCnyEzfZ6NUXMRMEhgB41LVkMFlphs6V2XBWq8turB2reiqMhG7v38gYdS0ut2JkmMtPTvGoTSwJuQmgrZYBmUAQBiHnsnLOTgXcUlksW4QEUeccRR-b2TdfZGmad-X-8xAlNr5VRa2JoHwYwUSTnSll6h0CIBqo5iVzk7QBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=Vst6ZVSITs4U7ZZz10rC4PynBGG8DWffmSB5OW8Ohj1sZaZmIEYLEB7qyTcG6fDc7siiajwOuzUvLblUutjFh2XoLZscBHSJTqNVashxTenMUymXEz9cLxg2wWybi8-9fL9jDFBkSLcmN3tkR44s2bYNvXUS5ReRDc6pbNlZvocLRdCnyEzfZ6NUXMRMEhgB41LVkMFlphs6V2XBWq8turB2reiqMhG7v38gYdS0ut2JkmMtPTvGoTSwJuQmgrZYBmUAQBiHnsnLOTgXcUlksW4QEUeccRR-b2TdfZGmad-X-8xAlNr5VRa2JoHwYwUSTnSll6h0CIBqo5iVzk7QBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=gWDVrbot3Aeuw6bEVSDn5S35gviu3MGoDIzsDu0F0luzU2q_bdlcGAXwqBrW69y9f3DeD8ZwBN_3e736iYM0hT6TGJX8DAQ8I58a9Ro78dWAEW4euzJSSqp9_z8f2JP3w__MqWNca2-Ym63g6M97CM7wTclPmtljCqHenlzhKOo4Tqpho0dYTvyC0aXO_y8_TAHb6wiqzDN0-XOTucUuLjqmryxsVNI1h_XI47mOdWfjwJNTtRt5YmFWTHVEhqgQ4H5Lt-TGf_ob6UxWr3znA8SdDd8XDrMMGGJTcigz_ylKSqzMkz2oO6IJO3ICt9zsaVNLF_zzzNBFvFfucGEIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=gWDVrbot3Aeuw6bEVSDn5S35gviu3MGoDIzsDu0F0luzU2q_bdlcGAXwqBrW69y9f3DeD8ZwBN_3e736iYM0hT6TGJX8DAQ8I58a9Ro78dWAEW4euzJSSqp9_z8f2JP3w__MqWNca2-Ym63g6M97CM7wTclPmtljCqHenlzhKOo4Tqpho0dYTvyC0aXO_y8_TAHb6wiqzDN0-XOTucUuLjqmryxsVNI1h_XI47mOdWfjwJNTtRt5YmFWTHVEhqgQ4H5Lt-TGf_ob6UxWr3znA8SdDd8XDrMMGGJTcigz_ylKSqzMkz2oO6IJO3ICt9zsaVNLF_zzzNBFvFfucGEIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=IXjl-2EmHN3fRfBPcCE_ULX7TsHj9T3P_TROaDi2OBGQIGS6AeoZwNDEWT7SzX0h4xzMn0r9E3Ip-DELQi1iN5oufkv8hF2VVBsG-mEEpEwd5PW1RkR777Qid8k4a0dspoNPHdUpMIiIMHyS9BJDiU5OSwa-hjp28zJb9XTGes8b3YRH4yaQGHPvt7Hech-eahXqccwnN22HRkabByqK5uOB-RHM6JT_ZWJbj33FfQtKEGP92WUgb6jvoePpk3hFSb-jBsV50tM6f1_So_z2uI6akaZGqOitO-D5jeVd0PLoI1BuOVfdI1pMb90rTDbN-bV7zStunCewjkp0VsJ7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=IXjl-2EmHN3fRfBPcCE_ULX7TsHj9T3P_TROaDi2OBGQIGS6AeoZwNDEWT7SzX0h4xzMn0r9E3Ip-DELQi1iN5oufkv8hF2VVBsG-mEEpEwd5PW1RkR777Qid8k4a0dspoNPHdUpMIiIMHyS9BJDiU5OSwa-hjp28zJb9XTGes8b3YRH4yaQGHPvt7Hech-eahXqccwnN22HRkabByqK5uOB-RHM6JT_ZWJbj33FfQtKEGP92WUgb6jvoePpk3hFSb-jBsV50tM6f1_So_z2uI6akaZGqOitO-D5jeVd0PLoI1BuOVfdI1pMb90rTDbN-bV7zStunCewjkp0VsJ7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=t2cJexAe4lGTG7kqzkGSbT-6fDqq6auY6ansybXbv03q0Arkti0a9OPi-g_YjurMFOjelw0zi5v2G3VCyIPZgGOtEH-rL-MRppglSkzCUOxP60QasHyHnPEpNUYVwARxqGTxxM7uE5tLDolwv3tMwgohEUHkfSfeWfeTr1Y0qBrESeLlr1JU-dOowyHOvwxObGKnEbvx6rApcp390Uq00g7jH96pNa56_3ddpHG8t_BTwxBJOm2GYnT7z-6wypzYjwbmAbVMM6t-DUt5YfZ0S60N3LOSdBV7u4rPSiXRY61tgKTd2aIs2C_MYDKJcg2MDUv6zzuLq0TdJwfPuSxCpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=t2cJexAe4lGTG7kqzkGSbT-6fDqq6auY6ansybXbv03q0Arkti0a9OPi-g_YjurMFOjelw0zi5v2G3VCyIPZgGOtEH-rL-MRppglSkzCUOxP60QasHyHnPEpNUYVwARxqGTxxM7uE5tLDolwv3tMwgohEUHkfSfeWfeTr1Y0qBrESeLlr1JU-dOowyHOvwxObGKnEbvx6rApcp390Uq00g7jH96pNa56_3ddpHG8t_BTwxBJOm2GYnT7z-6wypzYjwbmAbVMM6t-DUt5YfZ0S60N3LOSdBV7u4rPSiXRY61tgKTd2aIs2C_MYDKJcg2MDUv6zzuLq0TdJwfPuSxCpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر زنِ مجتبی خامنه‌ای:
مجتبی خامنه‌ای با همسرش سریال " فرار از زندان " رو مفصل نشستن دیدن و درباره اتفاقاتی که داخل سریال افتاده بود هم صحبت میکردن.
یه بار تو یه جمعی گوشی یکی زنگ خورد، من گفتم این چه آهنگیه دیگه؟ که یهو مجتبی گفتش این آهنگِ یکی از فیلم‌های کریستوفر نولانه دیگه، چطوری نمیشناسیش؟
‌
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71669" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71668">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy-yjplBDeilGlwgMHhzAqR7efndbEo6shinzRKlWQrknNU1tJibxCYV1OwWlgvzFhbyzMoH117moDrh6EFIbSg0J05b2otk-qS0hRIAWcPaclPs07YPgESRsx5zaLSz4aFGd2PpBP3fkedYl6uqdPxjvXcmNJURGy2BaPCT1l_b7xjYkKh3oFWAwqhrnwgYs9rosHnKbScWisjtsPznQ5gTkBKyGdVZuQn3PajCJsd05U19FxhWH_WOyFOS7musCTFuIUAeI9xal32fx2aBb1y4_3sfyLNeTviKggyDZnDYQT4GP3JziHN5UJJVLiGye3acwaF9Ivb4RfGUMzd6fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی:
«نشست عمان» با حضور کشورهای خلیج فارس برای تثبیتِ مسیر تنگه هرمز، با نقش‌آفرینیِ جدیِ آمریکا و برخی از کشورهای حوزه خلیج فارس فعلا لغو شد
عربستان» به بهانه اصابت خط لوله‌اش و درخواستی که از پاکستانی‌ها داشته تا ایران را راضی کنند که به انصارلله بگوید از فتوحاتِ جدید عقب نشینی کند، «بحرین» بابتِ ناراحتی از جنگ رمضان و پرتابه‌‌های متعددی که بخاطر میزبانی از زیرساخت‌های نظامیِ آمریکا در خاکِ کشورش دریافت کرده و «امارات» هم بابتِ اُفت جایگاش در آینده‌‌ی منطقه در صورتی که مسیر جدید تنگه تثبیت شود، در نشستِ مهمِ عمان شرکت نکرده و کارشکنی کردند!
ولی بازیگرِ اصلیِ لغوِ این نشست، آمریکاست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71668" target="_blank">📅 13:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71667">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حملات موشکی/پهبادی حوثی های یمن به مکه، طائف و جده عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71667" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71666">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPEnyzkSUyxX3O6gE8FDXzPvtjxMCra0BlDPOutl1UQbibSiYvhSjBb0xqX2v5yX6Lu2m6Hh8K_WvLYnTJrS41yQPnnizzxeVvAiI4PuQgLi_leDsgu1El7N66PWCCPZLKdzV8_A-hpX06vMIrOrSylylbeJpBWUyFonaT8zU5-suCb2uSnJD7J12OyJJgIvmUBupM-YlYqRdWtx_xn9sf0nNOSrSBjnTANeaFGO0iDrqcrAl3R0GlC-Q2mMCFH_Q5duLKx447ii8ZmketKbNzq_SCKqbaIXW9X6B5Qp5QWoAmcmVWIjoLv751YiQ-3SElVi8_0Cmd7aTxjUP1KRhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) :
گزارشی با تأخیر زمانی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع موثق گزارش داده است که شناوری مورد اصابت یک پرتابه ناشناس قرار گرفته است.
هیچ‌گونه خسارت یا پیامد زیست‌محیطی گزارش نشده و مقامات در حال بررسی موضوع هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71666" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71665">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=JDHo9i8lWlvlg5yQgY6DKL0sdGkxWpFMnPNiP9lTJLs2Y7PmPR_sOExuXowd-rTFINwkxC1qXm-nQ-Haf-alBCXmzqSLEUorLtT58_ntQSyDNXHByqPI-gn-MZzt90GFUmX804NVE9iRE0qkPrECkM5inw7BFVhHL6tSren5i-UscKwDD5-o5lYAmOXsFIbPmw-PpjGHPCQmie1QOTNHbVApV3gYnDrc93hWJjOmZNL4B8EEc4AiK6H3CRCtKLQm6gpkk-eAqV92-6-U-cYvUOG0LfLjLOSuEzrGyPjUN-JOPJwnDwGkOPSMJpx4UbC3mIRBQpVNHFiyIi4Yqa4TOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=JDHo9i8lWlvlg5yQgY6DKL0sdGkxWpFMnPNiP9lTJLs2Y7PmPR_sOExuXowd-rTFINwkxC1qXm-nQ-Haf-alBCXmzqSLEUorLtT58_ntQSyDNXHByqPI-gn-MZzt90GFUmX804NVE9iRE0qkPrECkM5inw7BFVhHL6tSren5i-UscKwDD5-o5lYAmOXsFIbPmw-PpjGHPCQmie1QOTNHbVApV3gYnDrc93hWJjOmZNL4B8EEc4AiK6H3CRCtKLQm6gpkk-eAqV92-6-U-cYvUOG0LfLjLOSuEzrGyPjUN-JOPJwnDwGkOPSMJpx4UbC3mIRBQpVNHFiyIi4Yqa4TOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبه ناو سپاه با عنوان «رودکی» که در جنگ ۴۰ روزه منهدم شد در حال غرق شدن است. این کشتی تجاری بود اما به نظامی تغییر کاربری داد و گفته شد هلی‌کوپتربر است اما هدف حمله قرار گرفت و نابود شد.
در جریان جنگ ۴۰ روزه تقریبا تمام شبه ناوهای سـ.ـپاه و ارتش از بین رفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71665" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71664">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71664" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71663">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFTT-HYmCb2CoBTopWPKIwD3d0pRK1YZSULI3BeNzwmQySxnA0ApB5xJfujI2zXG2gZZiBwzkwhTjHr1WRg7OBvJ1kkAVub_7BV4gn3d6U7dmB-XpQ9NbQ1h6O1WniqgNCxc7I2dNJNX42Leox-Lw4s_CZ-G5maMHwteKjvpSjaP26BRP59ZTnDT-c7599_dcXhqm5i1TNRsRhY9HkWKttBwSsddeRQgeyZaJzuXETYx_yU8CCRZPhLQkaFR-hFwAnljUSnrisUfwpXDnnpKZGuCo73WujQMOHTmg27Hn96AQoB9fmG_XkN9W84xTj4VqD3GAYC3WsQWNjPOxvCPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71663" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ma20lhwX0OUqgppp-33Jb8ScQFOYgT8_rzkN6DHsIhaBiTh7ms2H4c7f0VQe04jbEeFtFNS5_brPec4xkVAISUYa0zY_nXc7wNv_dTLbtgIvI6ZNnb4zwzT_O5504zxp9tB-9dSLQKjhnFbqaPB1xMTus5Xc2ztTdRlnzha0GRQ_QUoS4OEx0pGyUGjXAv_WT1nCcJZ_N3Xl8HUUnxU7-GTBr3kcBDSRCNOGOiAgPuY9jllT7qof9S6Jq8mwWhcm4M3KTFo04UeOg193rR1KI4THN9p2RaL1hDWjuFCCGy1M2cclMPFkqMja7AtHxhX8a2M-Vl1S3RE1PUGUH3B_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71662" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=vUVneVPHmlG7wivWpVTAqj8DUfR-_7jxZjSCCLfQ8jBE1BPnk5dPg9P4aamLMrvfdkbkhicrxFbVqAz1Ptjq7KZh2fBDDf2xLafsqXCyuLKYWCHJuhIN5lS410GFLNNfGdIIG-BqqvHvlFfPROBTRg622f4FssyV49AE6SAityMFatvCtl8PWKsg7MzI__MeJ9nkJMpGyDLP554CF3pdUGC83TQPjw5Zn6wEU1siu8pN7VVFMajaISnDjCqR_XQDFU1XuegkMSVk8ygbnhsX1v3HXzy-CQSvflo_8mGVqZ2GYr0j5cuV_QdUVc0vYX1X22tfAkWSDmapSl7SEpOcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=vUVneVPHmlG7wivWpVTAqj8DUfR-_7jxZjSCCLfQ8jBE1BPnk5dPg9P4aamLMrvfdkbkhicrxFbVqAz1Ptjq7KZh2fBDDf2xLafsqXCyuLKYWCHJuhIN5lS410GFLNNfGdIIG-BqqvHvlFfPROBTRg622f4FssyV49AE6SAityMFatvCtl8PWKsg7MzI__MeJ9nkJMpGyDLP554CF3pdUGC83TQPjw5Zn6wEU1siu8pN7VVFMajaISnDjCqR_XQDFU1XuegkMSVk8ygbnhsX1v3HXzy-CQSvflo_8mGVqZ2GYr0j5cuV_QdUVc0vYX1X22tfAkWSDmapSl7SEpOcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: آیا قرار است همه ما تا ۱۰ سال دیگر بمیریم یا نه؟ موضوع بحث همین است.
ایلان ماسک: خب، متأسفم که باید این را بگویم، اما همه ما خواهیم مرد.
مجری: می‌شود یک بازه زمانی مشخص کنید؟
ایلان ماسک: بله، نرخ مرگ‌ومیر همچنان ثابت و ۱۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71661" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71659">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎙
صحبت های این خانم درباره سگش:
خرج ماهانه سگم حدود سیصد/چهارصد میلیون تومنه
😳
روتین روزانش صبح حدوداً ساعت ۱۰ بیدار می‌شه، یعنی صبح همه رو بیدار می‌کنه. بعد تا ساعت یازده که می‌شه، یه مربی شخصی داره که میاد می‌بردش یه جا مثل فضای باشگاه.
بعد هم که ساعت سه و چهار غذاشون رو می‌خوره. پوستش حساسه و یه سری شامپوهای خاص داره که ما همیشه می‌زنیم.
شب‌ها من یه دور پیاده‌روی می‌برمش و بعد هم شامشون رو خودم می‌دم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71659" target="_blank">📅 11:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71658">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=aGOmukhBBjMcBistEbf0WyfOeExygbQocIeazYcpzFJAZtTkNaL5JO0Q1QoZQ5Ctbl6YXetRROUdl34HY_iwq8--s-z7bNL4ROOj-CQxQm69u12-Xy1uZ-aXaaMENNn90lQCRCGG0S-HofEgolkEIOivuhBSD5x76bxU5Idd7jz_Aaz0ycynOW1Gr7Cv6xdUyy1cMvTzqstOLYwjGMjtHyzNcC4OV2n5MG_-H5WZDs2Uxsv9m4pjD0BB7b2jav1x2Fogvwl_tIbsx2Sjxg4sugy3HRMUfn0Qs6m8xm4PN6wqitWKQxUju5XyZAPNmBexe1IDC-p9yL64c_28pwKCsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=aGOmukhBBjMcBistEbf0WyfOeExygbQocIeazYcpzFJAZtTkNaL5JO0Q1QoZQ5Ctbl6YXetRROUdl34HY_iwq8--s-z7bNL4ROOj-CQxQm69u12-Xy1uZ-aXaaMENNn90lQCRCGG0S-HofEgolkEIOivuhBSD5x76bxU5Idd7jz_Aaz0ycynOW1Gr7Cv6xdUyy1cMvTzqstOLYwjGMjtHyzNcC4OV2n5MG_-H5WZDs2Uxsv9m4pjD0BB7b2jav1x2Fogvwl_tIbsx2Sjxg4sugy3HRMUfn0Qs6m8xm4PN6wqitWKQxUju5XyZAPNmBexe1IDC-p9yL64c_28pwKCsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب علیه روحانی در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71658" target="_blank">📅 11:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوباره آمار مبتلایان به کرونا تو کشور داره می‌ره بالا، خیلی مراقبت کنید
من خودمم دو روزه به شکل عجیبی گلو دردم
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71657" target="_blank">📅 10:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840407be05.mp4?token=gg9DUC3DZA2BRqX6YknwlgtDMSfSwwYzyZtkV6B-Fi9R0LHJ5nuzj4ibMpefzTC_1-afgnTi0lInlsVfanOWF5InA1VlT93qBmsIuuZP5L6S6VZAOzAJahGfdbW7NDhYDoT_mcAiGg84_b64AS2OhB2I4YdFBPHWUZZytVFO3sPEjpeC2R40vxZYNGH4CFFzSOIagwxXja3a5BPqDreWQV6ibp5GZKpPu4n6cloSp71U2Gj3cCdDgZPAUCpJwWxRpEt9X58tW32LpnkVXVfItDrdcNjUKFgy4x7S5NhcfSupsGktCP09c88b9u4DikRmIPOesCJKToJFZzjmMIi7Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840407be05.mp4?token=gg9DUC3DZA2BRqX6YknwlgtDMSfSwwYzyZtkV6B-Fi9R0LHJ5nuzj4ibMpefzTC_1-afgnTi0lInlsVfanOWF5InA1VlT93qBmsIuuZP5L6S6VZAOzAJahGfdbW7NDhYDoT_mcAiGg84_b64AS2OhB2I4YdFBPHWUZZytVFO3sPEjpeC2R40vxZYNGH4CFFzSOIagwxXja3a5BPqDreWQV6ibp5GZKpPu4n6cloSp71U2Gj3cCdDgZPAUCpJwWxRpEt9X58tW32LpnkVXVfItDrdcNjUKFgy4x7S5NhcfSupsGktCP09c88b9u4DikRmIPOesCJKToJFZzjmMIi7Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار شده 240 تومن؛
همون لحظه صداوسیما:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71656" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=nObALgYp21OwEgTQzA_PDCZEqkro-pDSFYs_jJPWJrZh5L6Sp0f9PC5KJYd56G0oWVw8caGWj0MiJvuODqZiqqKRl9ja14Mc1Ja6-TPaIfHE8muW9FK45BrcSfl2jFsgNtK9mha-sTWg0uQGcbny6rvMWIlIc2v77V3knGVNgD0q3PqJFGL2BAgmcayC2HN_UoBTeXvQ2S_BOQZlByIUgsJM8U1h-ftQIyGGE6wlyZfrbhFOz4Y7VMtaOK8z4oSd5ksTZLR1ED5AEbXSC0DRsDaVf7IcC5jh_aJ6HH_aail40uJA0RkN0G7qCQ376U0F3C07r185OAEv2Nz1uN8RfUxs9wyiOWJo09U06mJobRVhCP6nkLAbuyeGi3KY53wvrjiS1tMO9Cv7VVbjFyvQQxzbajlaNewKzYhxB7iBg9H25t_2nap7v_8D5PAJCZdWEZMBFhwStQjSvYB7vS0TteY7PiKw_bvmEVWBdYqBiqJ2Q0lNAdXJsKjQQn3_HCnX5Yb7teXDum3K_jB6x_1gXESDrgBcxNq85nPV7yLrIToY6Qm0Fs4bf_-yOjBcj5_QiG_oM8qLgtillX2sLPyGwIb6xD9wyAiog2w0U9ztvmqWpQ4xTXATPV0V0V0FCtD8TAqMbibKbaAbHJ1r_PZnKbEbqJ_Kdf9GuVE9OOyH5ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=nObALgYp21OwEgTQzA_PDCZEqkro-pDSFYs_jJPWJrZh5L6Sp0f9PC5KJYd56G0oWVw8caGWj0MiJvuODqZiqqKRl9ja14Mc1Ja6-TPaIfHE8muW9FK45BrcSfl2jFsgNtK9mha-sTWg0uQGcbny6rvMWIlIc2v77V3knGVNgD0q3PqJFGL2BAgmcayC2HN_UoBTeXvQ2S_BOQZlByIUgsJM8U1h-ftQIyGGE6wlyZfrbhFOz4Y7VMtaOK8z4oSd5ksTZLR1ED5AEbXSC0DRsDaVf7IcC5jh_aJ6HH_aail40uJA0RkN0G7qCQ376U0F3C07r185OAEv2Nz1uN8RfUxs9wyiOWJo09U06mJobRVhCP6nkLAbuyeGi3KY53wvrjiS1tMO9Cv7VVbjFyvQQxzbajlaNewKzYhxB7iBg9H25t_2nap7v_8D5PAJCZdWEZMBFhwStQjSvYB7vS0TteY7PiKw_bvmEVWBdYqBiqJ2Q0lNAdXJsKjQQn3_HCnX5Yb7teXDum3K_jB6x_1gXESDrgBcxNq85nPV7yLrIToY6Qm0Fs4bf_-yOjBcj5_QiG_oM8qLgtillX2sLPyGwIb6xD9wyAiog2w0U9ztvmqWpQ4xTXATPV0V0V0FCtD8TAqMbibKbaAbHJ1r_PZnKbEbqJ_Kdf9GuVE9OOyH5ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوهای این خانم معلم برزیلی مهربان و زحمتکش بخاطر سبک خاص تدریسش حسابی وایرال شده:
تو یکی از ویدیوهاش که حسابی هم وایرال شده به یه دانش آموز فوت فتیشش که درسشو خوب بلد بوده به عنوان جایزه اجازه داده پاهاشو لیس بزنه…
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71653" target="_blank">📅 10:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=iAD9NaiptUNFwyJqS7jAkDsdh3KXUNJn-IqDjBpQQWLCxHCIzrtcLBSiyae8rVHHYK2UViqdTw7Hyq9AvLluHs7zmhxeaZ8ccRfjc9JiE8uRRpEkEu4uJLz0kyD5d0dPBqEvKJnh7ih-mZfSxSYAVRyPGZffqCIED8l-BwauRSGD3RPd3aq1KYf3bEPYBRro1L0EzK2XbTb-JRG2mrytV0NWwQtTSna9rVh1s7LQxC_15SIcI8VoHmzOzpgC4zbstnkoJfvJrzmBPusrRvpVhXNXu6qkHLqYj5Rlcq56ipOYCWkdvrv98-zGZjstHMT783zzNsD8Nto-7ZxCddbBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=iAD9NaiptUNFwyJqS7jAkDsdh3KXUNJn-IqDjBpQQWLCxHCIzrtcLBSiyae8rVHHYK2UViqdTw7Hyq9AvLluHs7zmhxeaZ8ccRfjc9JiE8uRRpEkEu4uJLz0kyD5d0dPBqEvKJnh7ih-mZfSxSYAVRyPGZffqCIED8l-BwauRSGD3RPd3aq1KYf3bEPYBRro1L0EzK2XbTb-JRG2mrytV0NWwQtTSna9rVh1s7LQxC_15SIcI8VoHmzOzpgC4zbstnkoJfvJrzmBPusrRvpVhXNXu6qkHLqYj5Rlcq56ipOYCWkdvrv98-zGZjstHMT783zzNsD8Nto-7ZxCddbBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش‌چشم، کارشناس صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی موندن که سیستمش چیه. موشکی که بدون نیاز به ماهواره، ناو در حال حرکت رو پیدا میکنه و دنبالش میره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71652" target="_blank">📅 09:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168229fd60.mp4?token=a71Pz4T8sWfA1XpO_hypGEYo1gF0bhttOxGP0Hnum8RnDk92OZ-rMGs0zr1Hh0apzutZ9v0CUyF2A97rUrFJ0spkcy_tOL4oKABopoKtV5y3UtXjhU9YHkXrUL3GlgF2f1sPfKrPj8a7ksLPSGy_gLWPmSlB8d7ETj9mNeexPzTgCobmDB_Xl4Ms5anI1vbioynvapzH3zF74jhnRmaw_rdwWFssSDShqB78S2RfB9ZFXkVUtCTknTSOacp_X_C6lUTNIN_Vju-bUmpSOQGqMiZaxegoAJsW6wjSrjF9ooaaYMCn9EEZXCv2IpkgcLh99xLfwPkm-bGFF_zMQgPnEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168229fd60.mp4?token=a71Pz4T8sWfA1XpO_hypGEYo1gF0bhttOxGP0Hnum8RnDk92OZ-rMGs0zr1Hh0apzutZ9v0CUyF2A97rUrFJ0spkcy_tOL4oKABopoKtV5y3UtXjhU9YHkXrUL3GlgF2f1sPfKrPj8a7ksLPSGy_gLWPmSlB8d7ETj9mNeexPzTgCobmDB_Xl4Ms5anI1vbioynvapzH3zF74jhnRmaw_rdwWFssSDShqB78S2RfB9ZFXkVUtCTknTSOacp_X_C6lUTNIN_Vju-bUmpSOQGqMiZaxegoAJsW6wjSrjF9ooaaYMCn9EEZXCv2IpkgcLh99xLfwPkm-bGFF_zMQgPnEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواب رییس کمیسیون امنیت ملی به روحانی:
اون روزایی که تصمیمات غلط میگرفتن اون زمان دنبال رفراندوم نبودن بلکه دنبال حاشیه بودن
اکثریت مجلس خواستار برخورد قانونی با روحانی هستیم و این تقاضا رو ارسال کردیم
قرار نیست یکی تو گذشته مقامی داشته الان از عدل الهی و کشوری مصونیت داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71651" target="_blank">📅 09:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71648">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=T8AyY8Fp_OUUQ8pOvvGES_v76MD8ERIM2TeVONOXgOrKKWfFjw_4uiDrQxwXErVvNfA5kEAys1evv3WYtE0pmsCbfL7sr4cdbcT747FpakAbO13fKBhxtgc3z1f0TupwRcU0u5JK2bDr6hbYlX8dlF8RAL_XmXvnlJ0KVWdxwg0EeqfcQaOpHGur05XDVSpZ73UM3kPaJq2Rr7Kv7eYtLM47j9tJplgXXRf9g9ou3Fel9be0B8_uB0snH81HSyizBhhC38CEq-xXJ2fYEpEcKNkoO9nKZsInGAiJAzVo3SdkdkL_Y4XnDWMpPUGJjidhMbimDBpde3B6Ec0TPmRA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=T8AyY8Fp_OUUQ8pOvvGES_v76MD8ERIM2TeVONOXgOrKKWfFjw_4uiDrQxwXErVvNfA5kEAys1evv3WYtE0pmsCbfL7sr4cdbcT747FpakAbO13fKBhxtgc3z1f0TupwRcU0u5JK2bDr6hbYlX8dlF8RAL_XmXvnlJ0KVWdxwg0EeqfcQaOpHGur05XDVSpZ73UM3kPaJq2Rr7Kv7eYtLM47j9tJplgXXRf9g9ou3Fel9be0B8_uB0snH81HSyizBhhC38CEq-xXJ2fYEpEcKNkoO9nKZsInGAiJAzVo3SdkdkL_Y4XnDWMpPUGJjidhMbimDBpde3B6Ec0TPmRA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل یک عملیات ترور علیه یک فرمانده حماس در غزه انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71648" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71647">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7qZs_5PbcaOuDWI2gtZP9qj8k-3OZ6TNDJNluEZM1gkpvdsh_3hx8desr1gdyCpww7eK9hBxjYHOTo6IC1FL3qIb2M7Seg-wVow6TA_-2oYfVycROT_Me0Z2OgPsUTiOu2nTPvjOY4RLjG2cn34kzcgAoYtCw4n8DK-VayLSdIiae9nEJK2nDWOjGmikuNOnLRLzfxt1Brab5FRw7A6s8ii1QFMOWwd-P9vKwE1fW7EmfLTdW35icdRpNLTi8ZJd6pDI5x62uvBYXJVlPURfdumc729Q4y4d6VVsekjaqKVdjYUsoSEp3tZDBDscFaJEOqdhhOALc18qoHSOTJMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم». معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در‌راه است را نخواهد گرفت.
تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71647" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
