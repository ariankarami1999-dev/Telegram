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
<img src="https://cdn4.telesco.pe/file/jdzCdD02teaWhRXvzO-fYHEIUryDHlMNHyGLTXPzQzLrRHZUHl_h3Sg4DcrvBspnFYid0eZdaO1Xya59d7liD2krMN9SIkSWVli7GcJIXGL-LCLGZXIpvcjwgDJjz3TvnuQEJsFtmq72Kd46nM35NnlKlm3UPpxK3h8HM1HTvuMBFHThm-TIMIzEnedWLguZw2gNFeWcDi8c_FoOa4S53KmcBkBHtLSaBR74_4NhIAeSPzgL316oF5NB1esjpz1NY9QKxurZZxq_0X1dlzESUWsfMaHwoEJlMZAXS_txbkBdXTeF-b3HS_ImtTlyvjJL15kmZWCqgBfrVwL-7165OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-437080">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZojmf5my-rHfOf0fuLxRSos_z4BSByWEWJLlqLTKoBa-yVUgnMdF9UpYl-syDgh9dqEX2_QDAmRAnNZ104Tnt2qKQR2BWVEx9QhscR4-w_GSdV5AWPua7bUu7anE0s1zSp5BzJlilkQhQExUQvJFlaF4uGlEkSb8ZG6A1eO1yLmd9xYJcWd_pW5GiZywtuy6nW4HEF4iytjSy3wf3D_ZIl4DWLfX-S460J_DOgZ0t5xOHnWEYb1d5IghQFmGHvt2QdljfPcLRbjxYPuG3-S7w0Qi4MPIwsG69oSnu0cA6SSTJcn3kI6tsSgclPTZf_G0M7P9PUTJxZ1_RY0H65qGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«زمانه»؛ برنامه‌ای که از دل تحولات، زبان تازه‌ای پیدا کرد
🔹
امین سلیمی، مجری برنامه «زمانه» در گفت‌وگو بافارس: زمانه قبل از جنگ ۱۲ روزه روی آنتن نبود و ما در یک استراحتی بودیم. سه و نیم صبح به من زنگ زدند و گفتند تهران مورد اصابت قرار گرفته است و بیا. من روی پله‌ها آقای آزادی را دیدم و از ۶ صبح آن روز شروع کردیم.
🔹
این یک آنتن دیگر در جنگ بود و فضای ما نیز از حالت آسایشگاهی فاصله گرفت. همچنین آنتن بیشتری داشتیم و ماه رمضان بود. در مجموع زمانه جدیدی به وجود آمد.
🔹
یک نکته‌ای که در زمانه خوب است، این است که آن چیزی که مجری می‌گوید را از پشت دوربین به او نگفته‌اند؛ زیست مجری است. یعنی من آن کتاب و شعری که می‌گویم را خوانده‌ام.
🔹
برخی اوقات به من کتاب یا محتوایی داده‌اند و من روی آنتن نگفته‌ام. حتما هماهنگی وجود دارد و سردبیر محتوا را می‌رساند، اما عمدتا بداهه گویی است.
🔗
ادامه میزگرد برنامه «زمانه» با حضور عوامل را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 525 · <a href="https://t.me/farsna/437080" target="_blank">📅 17:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0d578360.mp4?token=lHhfzvNCJ3rZeIpFArrMPIOqtC1WbCds_ynDB0LAixXeaIc2PrS4nm0yRGkzuFXbiDW6YpFxoVrBizBtjZrlDKHrbb2-jXpeUG9yYXLHQPgobLjMfz0povk4vftM65TdkvsUznorYAo2I-nQ3bq0Zzk-51jFG-2bose61i7N2qsO9cz4M3Sq4cIe2bVNsA3fmCgATsYCCpuCfTLCvKRAGGWq5ALboIf2M70QalsKCik2EE_UohEXP8sdvQxvFPBQ-TUoK4pYYt3rIZlEWUePoUMmF7ngLuHATciT9wszCQ3_cYeBLsVs22I5-RDKe0TB7dp2-SjkzTChih_othnJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0d578360.mp4?token=lHhfzvNCJ3rZeIpFArrMPIOqtC1WbCds_ynDB0LAixXeaIc2PrS4nm0yRGkzuFXbiDW6YpFxoVrBizBtjZrlDKHrbb2-jXpeUG9yYXLHQPgobLjMfz0povk4vftM65TdkvsUznorYAo2I-nQ3bq0Zzk-51jFG-2bose61i7N2qsO9cz4M3Sq4cIe2bVNsA3fmCgATsYCCpuCfTLCvKRAGGWq5ALboIf2M70QalsKCik2EE_UohEXP8sdvQxvFPBQ-TUoK4pYYt3rIZlEWUePoUMmF7ngLuHATciT9wszCQ3_cYeBLsVs22I5-RDKe0TB7dp2-SjkzTChih_othnJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از پرنده کمیاب «هما» در منطقه حفاظت‌شده سبزکوه چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 484 · <a href="https://t.me/farsna/437079" target="_blank">📅 17:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
حزب‌الله: تجمع خودروها و سربازان رژیم صهیونیستی در شهر رشاف با چند پهپاد هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/farsna/437078" target="_blank">📅 17:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7GfgMoNYU84NPSn1vWfmPCjaruLVdAp7STMIj0T_BjgnB7y0yUBwJTAuR6_2LDlJ61hUlanPcGYThaSXBMazzfr6SZ2n0jL2gdV_EDsseH6QmLv8S0gi9LG5rOWk-rb7b0p5sykg-aio_YAU7IGbYA6bElt2Sk_yQapqiGufj7KEw5_hP5zEWPQbjD_iS56AMpPKF1tzULpXWCQKmtHVIAiZ2iEo2ZUQkP_6Wp_wRQ6X8I4XTL_rav2JCAXgUDzwe-XMLlFEGk9g27kXPTCATwXPLElXZUdYVW6PjBZ0NjRqjEAgoeg8C8kySUOur_kWNKma-tDaY0el615vo7hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان هنوز به ۱۱۵ زائر ایرانی روادید نداده است
🔹
یک هفته دیگر مناسک حج آغاز می‌شود اما رئیس سازمان حج می‌گوید: هنوز ۱۱۵ نفر از زائران حج کشورمان اعزام نشده‌اند.
🔹
باوجود گذشت ۲ روز از پایان عملیات انتقال زائران، سازمان حج می‌گوید «طرف سعودی قول مساعد داده…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/farsna/437077" target="_blank">📅 17:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قوه‌قضائیه: مدیرمسئول خبرگزاری دولت به دادسرا احضار شد
🔹
قوه‌قضائیه اعلام کرد: درپی انتشار تصاویری از یک خانم بدون رعایت قوانین و مقررات اسلامی کشور  از سوی خبرگزاری ایرنا، مدیر مسئول این رسانه برای ارائه توضیحات به دادسرای فرهنگ و رسانه احضار شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/farsna/437076" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437075">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تشکیل پروندۀ قضایی برای یک فیلم سینمایی با محتوای غیراخلاقی
🔹
درپی انتشار فیلم سینمایی «تهران کنارت» با محتوای مغایر با عفت عمومی، پروندۀ قضایی برای دست‌اندرکاران ان تشکیل شد.
🔹
همچنین رئیس سازمان سینمایی دربارۀ صدور پروانهٔ نمایش برای این فیلم با وجود محتوای غیراخلاقی و مغایر با عفت عمومی احضار و بازخواست شد.
🔹
با دستور مرجع قضایی و نظارت وزارت ارشاد، مقرر شد محتوای غیراخلاقی از فیلم حذف و نسخۀ اصلاحی در سینماهای سراسر کشور اکران شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/437075" target="_blank">📅 16:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437074">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌ کانادا و فنلاند سفیر اسرائیل را احضار کردند
🔹
کانادا سفیر رژیم صهیونیستی را در ارتباط با ربودن و بازداشت فعالان ناوگان جهانی صمود احضار کرد.
🔹
نخست‌وزیر کانادا گفته «کانادا از قبل تحریم‌های شدیدی را علیه بن‌گویر شامل مسدود کردن دارایی‌ها و ممنوعیت سفر، در…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/437074" target="_blank">📅 16:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437073">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
موج محکومیت اهانت وزیر امنیت داخلی رژیم صهیونیستی به بازداشت‌شدگان ناوگان کمک‌رسانی به غزه  @Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/437073" target="_blank">📅 16:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437068">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjYMdG6LJxTpO-gQ81X9JtjDsBEqRzX1_tGD61l9zhN-HDGzhjiOQQWHYUEczw89f8CgVoWoa-pE4OInSPTFgCCaVVDPPD7QU43vSCz1fBQLVAcnnfbTIwQ0zESbLAtM5SYNugH0woJ4hw3fb-3KaE-NYIoFapSG2oEGIezjjrGBzNvgzpeODXiAkVhjhPuFKvxI2H0OhWAO-9J7-4sCz2SbL13yY9QhwkPOXJhmlYOKYQd_FJSuEtTG3DanfkaAUgLxLmqzX4QA3k0ujf_GzNSKsSIg8xHxSge_TQ3WzscqxjCjXdokPY6uDgwyGAP7vltMvSp9s7oVrDgfIzWvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtYsOeLmwk39lj7sNUOxFjQ9ASebFsgFuOSJuO3VA8Nn-dU3IWXql82WODk-9vbTcyy3r1wq9LHDkPzpCzqWNijRGEogUI1nTWHPKQDrUHRcFr7f71d-jZUycmD6M8q34Ny4Gnp_QWldZIW5c7JeO5MVBnPSmAFi3PQ2F0RtFHpWiptGQ2GyJ0r6D2HiXxYcX9jwnf8fobMLXPXZy0Ucu-a-blloS-iBJRgYOwQak38tRtzwZDHe1pL0QPVlkh8ELtxZ-6NJU6mHveP5F0wyBFKXJEvhzHyBF6qPV8cpKIdmZaA8VnQyrhhB071Otgza8h5M3NvfsDahj1kEzZe0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUcxlNoH2kWJCg1OwqDwwd6Maan6_EpQrTVDavFRRYuIM5zjG69hu5BmCSPVkLqPQHo41hjxbFNe_ioeGN2YjdrOn6POqNW-q2vlu8b3UwOvAhJ3TIQzrEgThshMzXPbLKEu0657rm4BOpV2PHpzlpudWcNBfJ0o_Rm1BHM3ZrcSjVs4-pZisnTtRw1aZAqVAFn7lwEISc8-ViLMc4Y2hStzGNoPco6QyzIc0m5AgfvCOhO5zCSzHKo0b2C6PpalJGGZv_U40ncm0hUFiN2PpukQZgZ9N2y21zXyrNF0p_-JxJ7moSoWJVJAPX811Gr3u5JYHk2upWuQb2diEb0Ulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMT96ZTCJTUMTIq6r2o3VdKl0bI1A1Qj9sh9XzNwy8TVukDpBpSBwUjc_5dUliuV7Y-9C6X9119SgQhxyqlNg6G8nbT8nWApS13dBot04ZFRQDg9yn7yLDvAgTMjPyQ27-vmm9rVBjHiG2WELt9CCqY5DavWcQWld5U67FL8s3rYSCONDPtyJ13gqh8fTZlxxcpXddkt74VxZxl76yxEkBbTPtpfDaTGoJpUtbYLAzR5tbfb1Ns4UbvU5J4RCqLxezV1Ao0Ag_tsiMLdgVtYJK2crE7MM_F3H9Fvt8hQjPh_UAeJ0UseeFuqrtbbJDWp6HSLdHtIqhEYP2NWa67aMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiZpmq5rSmgQVuc5ZlrURxUwqfREYyz0dhwuwzXPwpjFhb6UpydHgXYNxCgL3V6WaXrhv51p4u5OfEIV1EfxalIqAAeOrEJl2YZ6apXt5PrQaq5ryhO99Qki-L_C85DMkfvvhu67c1-PrvYUt0__azbzQQZ6WfTc4PVmR-_AKsiQmi11qR-oaBF2xonyzIFZVR3oj9tQ4CNme8vXT_nMzpikT7qc44-FRyX2F97QhUV8DDNbz9eNIUMxQof8UKJnDfq8d6fB4wUXtsJWgiG7K_Xb7ukP6nlq0S2lBDlKd0eBqjiLQUQaiHkOurq9sFeIywXa0zvWMdebc592sxJi2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند
🔹
رئیس‌جمهور در دیدار با فرمانده کل ارتش: انسجام ملی و اقتدار نیروهای مسلح مهم‌ترین پشتوانۀ امنیت کشور است. دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند.
🔹
امروز انسجام ملی، آمادگی دفاعی…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/437068" target="_blank">📅 16:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b5170e37.mp4?token=HqcAnQCdZcKYh8DwcJ-lTBhObijc24Io1sg_E-6v-qkj1lHg6l1crNNX32Ocdg_hLwmJkyRjMKLVMq2W35Utw1ITCAI5KehWXPFhvnerMDAwboJTdoi-qLIM8FvIC-zvJBLv6yVFSwYp5ffmfQfamSOesC_7V2xVMd5W6et14fKoQHdh5_3lYbEFK7IDzZTwOemoWQpLZdpA-SsSNL7Ike9s3Tvv3OLmWGCoggbhsCCTIQYFpB8qa_6u9e0jxC_SynpGaeC-Lt7kONKimzFL_QGkp69BIz7hyicxlmzaWrDcgD1s-dp0oI7aHuMM5JBQIZ1rDC_QoiDJfU0vZ0xoxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b5170e37.mp4?token=HqcAnQCdZcKYh8DwcJ-lTBhObijc24Io1sg_E-6v-qkj1lHg6l1crNNX32Ocdg_hLwmJkyRjMKLVMq2W35Utw1ITCAI5KehWXPFhvnerMDAwboJTdoi-qLIM8FvIC-zvJBLv6yVFSwYp5ffmfQfamSOesC_7V2xVMd5W6et14fKoQHdh5_3lYbEFK7IDzZTwOemoWQpLZdpA-SsSNL7Ike9s3Tvv3OLmWGCoggbhsCCTIQYFpB8qa_6u9e0jxC_SynpGaeC-Lt7kONKimzFL_QGkp69BIz7hyicxlmzaWrDcgD1s-dp0oI7aHuMM5JBQIZ1rDC_QoiDJfU0vZ0xoxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی انرژی اتمی: دانش بومی تولید رادیوداروها با هیچ تهدیدی از بین نمی‌رود و روند تولید آنها همچنان ادامه دارد
🔹
تاکنون بیش از ۱۳ هزار دُز از رادیوداروی حیاتی تشخصی و درمان سرطان پروستات به‌همت متخصصان صنعت هسته‌ای کشورمان تولید شده.
@Farsna</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/437067" target="_blank">📅 15:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHtWblZojHr5z4tg85LiSz7hVixAQennp5BpqjtaPyyxKsVJUrZ795fHzckAJ-rOcgJd_86mR0iGo3azgfAzrODd1AY0VPrdzHcyWDKX-HzJVVqdI8ATOJpjFyXhPiO8qxRQ1uKeyKa7AbhagOsuM-I-gUb8t32G2OEH06HuSZDN7-40D3wGhUxUEvvYCdskUOREaeTfdgZJhPsjmSogwcMwqL-YxpNlV55I0qi0tRwCbDVxLTw_1aP3_zZUtdXyyjC9hSu2Lifmux_DrUOX1Q_Grh0k5CwFowGyiQfm9R23uXvsNu6IlQRIAU_E3Ekd-VZTiG-tfklRvrbMG6iKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار فرمانده کل ارتش با رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/437066" target="_blank">📅 15:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3e15c830.mp4?token=ODWjPUdZqbxsmAh3qHU7sLhuKMoApl3Y5HArW1jsPXZrtVwgBqlFN9OfuY9woaYlVivQ9TUQPhbE-IBR4zb_V03mllEaIJv6lm9E6qRluyrUqGVjzgNSpF3ioeRpBNYggRUm_Say_39OyZa0HuJ9qQquZXpepK2ibdcXdFG20s0ouEaHo4bmpxvEnjVBzpxTC-v6fZDoq3L5N1_IWYc5VlZiAp7VlPjeX-_mRSQwBnzvPAtZfR-UHDoKGHVg_ipp4KoXuaL_89Iwynr9j22oZ2Rf0of96TQUagUwWPP1Vz68xSEXPWoKjF0yDZ9dvqHL4KaoKnyOuOerFcWCvPHdzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3e15c830.mp4?token=ODWjPUdZqbxsmAh3qHU7sLhuKMoApl3Y5HArW1jsPXZrtVwgBqlFN9OfuY9woaYlVivQ9TUQPhbE-IBR4zb_V03mllEaIJv6lm9E6qRluyrUqGVjzgNSpF3ioeRpBNYggRUm_Say_39OyZa0HuJ9qQquZXpepK2ibdcXdFG20s0ouEaHo4bmpxvEnjVBzpxTC-v6fZDoq3L5N1_IWYc5VlZiAp7VlPjeX-_mRSQwBnzvPAtZfR-UHDoKGHVg_ipp4KoXuaL_89Iwynr9j22oZ2Rf0of96TQUagUwWPP1Vz68xSEXPWoKjF0yDZ9dvqHL4KaoKnyOuOerFcWCvPHdzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: رئیس‌جمهور و وزرای دولت برای حل مشکلات معیشتی مردم بی‌وقفه تلاش می‌کنند
🔹
مشاور رهبر انقلاب در دیدار تولیدکنندگان و فعالان دام و طیور: همه باید به دولت کمک کنیم تا با اقدامات لازم، گشایش‌های بزرگی انجام پذیرد.
🔹
دشمن آمریکایی‌صهیونیستی امیدش به فشار اقتصادی و تمام شدن تاب‌آوری مردم است و خوب می‌دانیم این بخش جنگ برعهدۀ تولیدکنندگان در سنگر امنیت غذایی است.
@Farsna</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/farsna/437065" target="_blank">📅 15:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcuU_-gufzF-W8BFRQZlQujG1P_Kj-HhANnnTQs8JRb7mCXnlHu4QUvLmei8RyM_dsmsxjCy7VkGEGh6p-3ESckPHfdcZj5qAAbe6bN6o8fkCMpfXQDWhLnaRf_suy43y0n6I2bpb9TXd-o9QF635l3DsaljqOFhEgzfqwcQNXnSW32FkNj5V6kOcdAi5qWSNap53Nw7nAp0rkxecDcOmoNrTOJYg0QzpRo9KQ5KbwsANa5gtB8oHqm-Q9heBsbhYr6ajkaWS1u8gq9dxttgdS6tNW6q8r5UyNzUM_m-_uZfKXUfRNUEbc6uJEL01cbhrKrCRckPiCcU7iRJ01AM4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
تأکید ایرانسل و سازمان اداری و استخدامی بر توسعه سراسری فواد۱۲۸
🔸
در نشست مشترک سازمان اداری و استخدامی کشور و ایرانسل، با حضور معاون رئیس‌‌جمهوری و رئیس سازمان اداری و استخدامی کشور، مدیرعامل و جمعی از معاونان و مدیران ایرانسل، ضمن ارزیابی آخرین گزارش‌ها از عملکرد سامانه فواد۱۲۸، بر لزوم توسعه این طرح و تسریع اجرای سراسری آن تأکید شد.
🔸
مدیرعامل ایرانسل، سامانه فواد۱۲۸ را یکی از پروژه‌های مؤثر در مسیر تحول دیجیتال و اصلاح نظام اداری کشور دانست و گفت: ایرانسل این پروژه را به‌صورت کامل پشتیبانی می‌کند و آمادگی دارد با توسعه زیرساخت‌ها و خدمات مرتبط، اجرای سراسری آن را در کشور تسریع کند.
🔸
رئیس سازمان اداری و استخدامی کشور، با تأکید بر نقش مردم در اصلاح فرایندهای اداری، سامانه «فواد۱۲۸» را بستری برای شنیدن صدای شهروندان، ارتقای کیفیت خدمات و افزایش پاسخگویی در نظام اداری کشور دانست.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/437064" target="_blank">📅 15:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437061">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWoFHNPx3NHT41xFJy8Sx3m7Y71gbu8in8UBC6ngsGhsOnbwDfi-FtX0xKhGg9-rA3SS0Ax8g6yIyORYPIHW1Nzk7ntTk7t5D7xs24KuJO_PTZ4DFyy1dMTv75hbKvIJuKCIqx9doI3JaVfApZDhrs-1jb-W71dkUswikAbK5lACB72E-gThns6QmKAxTQ3o-sLlphIvXGfAltr9EGwbifVm3cCJlVe2uXSiZ5O9cvhsZfjqmphGQr0MmFaLhFYdBXUTeisr6YQ9ahJd-PbcIp5Qy7qArNkBBDsoMzjLo08NAGXWHxIpSU1YcnKlTQrTKUtrMpYrCLESTlbQ2zHNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsMOciRI_Xjjfuh6yvLSYcT_9PKBVKpFHKs1kXkEdrfELKX86PlvV9DResRnrk5TKHHyni5I221X-YoEmgBdg4M9zvmm_quB3_P30LrC3xrIPQa06nA6yggxTiKUrLVEBjRVardXKuXeMrmbT5HyTsttSQe4Czk5p99OOLwZHEymdJbn0EAFL3GK2dvK04R9jhabJjs6qSpsChFGCXhAlsX8GNVoaose_uMg3a28qCioytQdaNx4amxyF8QxQDIOHlYG1oHDoJRMeRZ171_BOPAWIHFzfz2WDzru1t1gc2TduQ3ybEkETfr78W8FBoGuK32gphacNBBtTuUW4UKtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2ezK6pD224aeVEe9u48jqURE7jxHpaiK0w6R8sc5NN9yk3ytjPVCh8D69sRoax9Q-dYsr4tFsS_QPxbcMlVGUCMCZzrf2q1HFVzjwa5qkHt3PeqD8CzE95XzSi8FndwPJlThtLQSU_RrfR7fkuZlchVi9Vao1JDE7PIOh6Hdi8ShX8yEapQCtRptqk2ZvQubNt54F4Z-7DbsGT0RHQyhr4p3na5Dpyo4vNDu-pDE7rfJTleNoLARtfaOOqD0aI-LH0tztmuVPJpdhYoGWRDpmgh-yiW_UCwVdpSUI9S5MwbbYkqUdPEzs0mZPId78bQ82FTaqaGmrfBEaiUs41BsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
رونماییِ یک سامانه بومی در شرکت ملی مس؛
🔰
مس ایران در مسیر هوشمندسازی
🔻
آیین رونماییِ «سامانه جامع تحقیق، توسعه و نوآوری» در شرکت ملی صنایع مس ایران برگزار شد؛ سامانه‌ای بومی که با هدف هوشمندسازی فرآیندهای پژوهشی، کاهش خطای انسانی و تسریع مسیر تحول دیجیتال در صنعت مس کشور طراحی و پیاده‌سازی شده‌ است.
🔸
دکتر غلامرضا ملاطاهری، معاون طرح و برنامه‌ریزی راهبردی شرکت ملی صنایع مس ایران، چهارشنبه ۳۰اردیبهشت‌ماه در آیین رونمایی این سامانه و همچنین «ماژول تجهیزات حفاظت فردی- سامانه HSE» در مجتمع مس سرچشمه، با تأکید بر جایگاه ممتاز شرکت ملی مس در صنعت کشور گفت: برای حفظ اقتدار صنعتی، باید با شتاب بیشتری به سمت هوشمندسازی حرکت کنیم و روش‌های سنتی را پشت‌سر بگذاریم.
ادامه خبر در مس‌پرس
👇
https://mespress.ir/x6QN
@mespress_ir</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/437061" target="_blank">📅 15:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437060">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/437060" target="_blank">📅 15:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437059">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e85iIZgwP3-UD5gQTWrD4vkEkSdeoOsyqtzIDMiB4SYFM0a1UJxKyihNpzrWWP7JJUatvHxczSdW_zOwrX-0Gf7kErU4mKUjnhgx7nGWoS43WKA1vPwTUXB632XrY2q4CalEQDRPOnvUnafDWLIE1zoBkuGp5VG_gmmEUvcrvM2_z4Zn91XCEfl0Zqb3o9b-2SDV58rhzKo6Lf_SJNUIxK9kpNCan3Zv-usTuIk2Hm8MRE-5iyGrKmCgW0NKrqavyWi81RJgQ3dGk_CEo6R7oYCp8Z9uttansGUBFYlB_EssCvhX86S1uivfnn5n4hk6PfpxYaDcLNCa9d_G9jHm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار فرمانده کل ارتش با رئیس‌جمهور
@Farsna</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/437059" target="_blank">📅 15:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a4def724.mp4?token=g1rF4NmPhf6PMVNkHTQuVmQHURlOG3Oz5G0NaUuSqUbGaSGXmjgFRcBAe8rQSdwD0qscOTASpOjazqEYzIhpLh6JcXHVX7wRMApV11Zxu2useV1GNoBvCbMIvo5CB6iSXCTfhuw770BDpmMAJCX1RThrszRQqZTZ6By3mPpIgMCcSSS0zzzq_xd8x2no5rIUliRiLNzZ4r6h8N7oMtRNIx5w-TSQrP00IyNmoPKZs7V10_8mhylGFmsys6L1C2VeUB1wXfswtA0NFoa4a1YSontJrheB7PXCS1X11WGHLYv9sPlq_aBJiQNqpePHUayh2OfxxfFU78VcgaCcI6-Dhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a4def724.mp4?token=g1rF4NmPhf6PMVNkHTQuVmQHURlOG3Oz5G0NaUuSqUbGaSGXmjgFRcBAe8rQSdwD0qscOTASpOjazqEYzIhpLh6JcXHVX7wRMApV11Zxu2useV1GNoBvCbMIvo5CB6iSXCTfhuw770BDpmMAJCX1RThrszRQqZTZ6By3mPpIgMCcSSS0zzzq_xd8x2no5rIUliRiLNzZ4r6h8N7oMtRNIx5w-TSQrP00IyNmoPKZs7V10_8mhylGFmsys6L1C2VeUB1wXfswtA0NFoa4a1YSontJrheB7PXCS1X11WGHLYv9sPlq_aBJiQNqpePHUayh2OfxxfFU78VcgaCcI6-Dhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با ۱۲۲ تماس بگیرید و تجهیزات کاهندۀ مصرف آب دریافت کنید
🔹
با نصب تجهیزات کاهنده، میزان آب‌بها به‌طور قابل توجهی کاهش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/437058" target="_blank">📅 15:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437057">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f3aaf7f9.mp4?token=K5wUpBdOrzRnhBUXDfrOo7dQuPw2h-_L-HFF8BjU0Qhk5yAZqYfnd-O7yqLWgd_dZJLjsSl5wzAa031D3W-xKh3G0ne-zdFMr48zmd76KhF4wpBv8H3w0v1ulieitwLgg8wBWIWrst0K8lyAw-hxiYyNQn_-AC-3uiC048aUBwIs4qs05nOL02l-A9NcnkVEhjJvxmYYKqjdEN3DI935evg1bjYQ5cvYo6KxyUKAjIbRf4A9Y1DfXngZYpwbJSRY1IxW65bIl9jPVYe30uldfke0eGtFK1yx3WzLO4hwpxhQNUPBobINE87jVwvckugmLUfUvDH_3fNOD_GTJwC4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f3aaf7f9.mp4?token=K5wUpBdOrzRnhBUXDfrOo7dQuPw2h-_L-HFF8BjU0Qhk5yAZqYfnd-O7yqLWgd_dZJLjsSl5wzAa031D3W-xKh3G0ne-zdFMr48zmd76KhF4wpBv8H3w0v1ulieitwLgg8wBWIWrst0K8lyAw-hxiYyNQn_-AC-3uiC048aUBwIs4qs05nOL02l-A9NcnkVEhjJvxmYYKqjdEN3DI935evg1bjYQ5cvYo6KxyUKAjIbRf4A9Y1DfXngZYpwbJSRY1IxW65bIl9jPVYe30uldfke0eGtFK1yx3WzLO4hwpxhQNUPBobINE87jVwvckugmLUfUvDH_3fNOD_GTJwC4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ انگلیس کاردار اسرائیل را احضار کرد
🔹
انگلیس اعلام کرد که کاردار اسرائیل را به‌دلیل تصاویری که وزیر اسرائیلی از فعالان ناوگان صمود منتشر کرده و آن‌ها را درحالی که پس از توقیف کشتی‌هایشان زانو زده و دست‌وپا بسته دیده می‌شوند، مورد تمسخر قرار داده، احضار کرده…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/437057" target="_blank">📅 15:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437056">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd9663f89.mp4?token=POXz59fteX9CEBrN4HQpJ6_gwB9ll_Qmi6xHpNTk03JtVFKmEWEp8fASR5AWfasyIHihHbQz74GIhuOo49xlxAPNDoIPaaEFLziB6Dru5SO5RR8tdo3QjcbGS2wKsDpqyKDRP59HGOR5qWEtzXvwWLsmtNmPJN_XZvm2l6rdHQHZXXj55mTL3exH5I4hgHKjmptLhrEwnGqyD4SOeND4GjnddPRbNkwwFPH79uuwJ5GgD6pNdDwwSPMWEEXqwWBFbiiQwGudELplGvoPO11oI49quGXXR-jPSOp2iMOGMVO0Q2LjVS38B9MzFRUTRB8yeqgCTjpzE7ICFBRWKwqgtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd9663f89.mp4?token=POXz59fteX9CEBrN4HQpJ6_gwB9ll_Qmi6xHpNTk03JtVFKmEWEp8fASR5AWfasyIHihHbQz74GIhuOo49xlxAPNDoIPaaEFLziB6Dru5SO5RR8tdo3QjcbGS2wKsDpqyKDRP59HGOR5qWEtzXvwWLsmtNmPJN_XZvm2l6rdHQHZXXj55mTL3exH5I4hgHKjmptLhrEwnGqyD4SOeND4GjnddPRbNkwwFPH79uuwJ5GgD6pNdDwwSPMWEEXqwWBFbiiQwGudELplGvoPO11oI49quGXXR-jPSOp2iMOGMVO0Q2LjVS38B9MzFRUTRB8yeqgCTjpzE7ICFBRWKwqgtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقاضای حدود ۳۰ شناور برای عبور از تنگۀ هرمز
🔹
خبرنگار صداوسیما در تنگه هرمز: از دیشب تا الان ۳۰ مالک و کاپیتان کشتی با نیروی دریایی سپاه درحال هماهنگی برای گذشتن از تنگه هرمز هستند.
🔹
به احتمال بسیار زیاد این ۳۰ فروند امشب با هماهنگی نیروی دریای سپاه از مسیر تعیین‌شده از تنگه می‌گذرند.
@Farsna</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/437056" target="_blank">📅 14:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437055">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4410c0cfdb.mp4?token=MWJFf6gGOXvi_q3fJ47V6XwL99E2Vi5UZPfRyRANHv9YICZsZflS0XWZa_pbLk7k1SHcODfoivPevx16gXz6hp7CJOLM_ivVYnT0LxZRi4BvyXaIKsAd9_4tiVSyj67HUuqsR7KFxcU1PYX6YE9kFuGwFCqx8jW50oxxQ18nK4JXiyvne8d7BpjagcS3_IRr6Gb-iQuZG4E2ox7Hnr40KI5Adzz0Py0T95xvZtvEqXjq8c9AeZEwmSFPBCHfT3xM_4T7TBPrqsl-l5Ph9oXyOW7IPi90645G2ozWEam6DS1lbSeICXZpvuKLd95ce6PpcqAO9KpbI21OiE5_Jje32g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4410c0cfdb.mp4?token=MWJFf6gGOXvi_q3fJ47V6XwL99E2Vi5UZPfRyRANHv9YICZsZflS0XWZa_pbLk7k1SHcODfoivPevx16gXz6hp7CJOLM_ivVYnT0LxZRi4BvyXaIKsAd9_4tiVSyj67HUuqsR7KFxcU1PYX6YE9kFuGwFCqx8jW50oxxQ18nK4JXiyvne8d7BpjagcS3_IRr6Gb-iQuZG4E2ox7Hnr40KI5Adzz0Py0T95xvZtvEqXjq8c9AeZEwmSFPBCHfT3xM_4T7TBPrqsl-l5Ph9oXyOW7IPi90645G2ozWEam6DS1lbSeICXZpvuKLd95ce6PpcqAO9KpbI21OiE5_Jje32g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار فرماندهان اسرائیلی یکی پس از دیگری در لبنان
🔹
یگان اطلاعاتی حزب‌الله با رصد دقیق تحرکات ارتش اشغالگر، راه را برای پهپادهای مرگبار مقاومت باز کرده تا فرماندهان میدانی دشمن را یکی پس از دیگری هدف قرار دهد. از فرمانده تیپ ۳۰۰ در شومیرا گرفته تا فرمانده…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/437055" target="_blank">📅 14:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437054">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1afce8680.mp4?token=lSM295U4-439fBDCTG3MBI_zceSgmQuKss8BUC_yis6Gd72Nj_i4X9XZYRWQgg2T167ZhSDKQNfECLKrYSb0Hj_qFcZyhBxvMEznXEW_bwfSsqTtx69UGDhezDfmn9AiKrHqRFPnjFmrjZbV1mdlztlo7vd132kE0Xzb_XdKLdf6HW7_73A0rm6UAGiLAn8I5MC-KtpvCn_OtXnrInbvJ6YKEUOt0QPA9iecWvUb43DxolMVzMrGn-sCiyS8D2SSzlXZ8CS5Lbd1ZunXvJcsP_w0I7vNcUXdWF03_zXWOQYNgmh_Z6aM194bDPQ9QUaE3nIPLQPTnq1qVomhJhwVu6eD77c7qSK_BRwqaMJz1nOja9Cl8AjkEyn7I9Lgf-3iQJlICpoJeVe1mRWnSGfpaDQe-hcXwrKko7vtzzcXGsIv8pWSaRzWsPWJAAOtCFihkDJWppad13L__X4rFM154NWsxx3mtDkcPng08XcYGwN1Ht9ZqJ8rUcrzmYzSGw9duO6hWV4NCHU_3XFYHfglufV1cWm4XXLRiCl0G6W4KuT1mnpjNV_02esV4l3FXWfNxotXysGjndw-gMEZDSZvqELqSk8Rp9Jl3QPiviZu29uBSvsq6uJTxYX04plYQjvtTrYjsSIt_HC9MWak94ZzX2Dj1-Ny33MnZWUHLktYULI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1afce8680.mp4?token=lSM295U4-439fBDCTG3MBI_zceSgmQuKss8BUC_yis6Gd72Nj_i4X9XZYRWQgg2T167ZhSDKQNfECLKrYSb0Hj_qFcZyhBxvMEznXEW_bwfSsqTtx69UGDhezDfmn9AiKrHqRFPnjFmrjZbV1mdlztlo7vd132kE0Xzb_XdKLdf6HW7_73A0rm6UAGiLAn8I5MC-KtpvCn_OtXnrInbvJ6YKEUOt0QPA9iecWvUb43DxolMVzMrGn-sCiyS8D2SSzlXZ8CS5Lbd1ZunXvJcsP_w0I7vNcUXdWF03_zXWOQYNgmh_Z6aM194bDPQ9QUaE3nIPLQPTnq1qVomhJhwVu6eD77c7qSK_BRwqaMJz1nOja9Cl8AjkEyn7I9Lgf-3iQJlICpoJeVe1mRWnSGfpaDQe-hcXwrKko7vtzzcXGsIv8pWSaRzWsPWJAAOtCFihkDJWppad13L__X4rFM154NWsxx3mtDkcPng08XcYGwN1Ht9ZqJ8rUcrzmYzSGw9duO6hWV4NCHU_3XFYHfglufV1cWm4XXLRiCl0G6W4KuT1mnpjNV_02esV4l3FXWfNxotXysGjndw-gMEZDSZvqELqSk8Rp9Jl3QPiviZu29uBSvsq6uJTxYX04plYQjvtTrYjsSIt_HC9MWak94ZzX2Dj1-Ny33MnZWUHLktYULI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار فرماندهان اسرائیلی یکی پس از دیگری در لبنان
🔹
یگان اطلاعاتی حزب‌الله با رصد دقیق تحرکات ارتش اشغالگر، راه را برای پهپادهای مرگبار مقاومت باز کرده تا فرماندهان میدانی دشمن را یکی پس از دیگری هدف قرار دهد. از فرمانده تیپ ۳۰۰ در شومیرا گرفته تا فرمانده تیپ ۴۰۱ که هنوز در کماست.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/437054" target="_blank">📅 14:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437053">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181370e43b.mp4?token=k1bZD2_7bNgxs237SUxciAiFF_yVeApk4IKBGPIqzVK5c9Ot9yy5V3DR29ndIi7FpRTh0sTK69R2_MHRYygk3AYhmfi6aR3FYoIe-CLh4qYpLpzdEh8-FrIwX8AlIj87G1kXiJX6LJ2eKPnB9ToDGRnHeFneRpgYFmxAMfv8fUXaxkLxaTPFRvNYWuOy8zgfitKNzQ8LLijp_8REulj3KP2NuReYhuZn-YBVh7fZ8CSw7ixaUKhsIGE87sGcS8tq0rYHPRUmMtVWGJ_2Ls1C681-Z1LTXLcUtqUUCaSTSl8ERcFrZG7rTa91v9JIuThxU0UArawHwJNqBEyReNfoAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181370e43b.mp4?token=k1bZD2_7bNgxs237SUxciAiFF_yVeApk4IKBGPIqzVK5c9Ot9yy5V3DR29ndIi7FpRTh0sTK69R2_MHRYygk3AYhmfi6aR3FYoIe-CLh4qYpLpzdEh8-FrIwX8AlIj87G1kXiJX6LJ2eKPnB9ToDGRnHeFneRpgYFmxAMfv8fUXaxkLxaTPFRvNYWuOy8zgfitKNzQ8LLijp_8REulj3KP2NuReYhuZn-YBVh7fZ8CSw7ixaUKhsIGE87sGcS8tq0rYHPRUmMtVWGJ_2Ls1C681-Z1LTXLcUtqUUCaSTSl8ERcFrZG7rTa91v9JIuThxU0UArawHwJNqBEyReNfoAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: اسامی اداره‌های پرمصرف برق اعلام عمومی می‌شود
🔹
در مناطق غیرگرمسیری یک ساعت قبل از تمام شدن کار باید دستگاه‌های سرمایشی خاموش شوند.
@Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/437053" target="_blank">📅 14:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437052">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نخست‌وزیر اسپانیا: فشار می‌آورم تا کل اروپا وزیر امنیت اسرائیل را تحریم کند
🔹
تصاویر بن‌گویر، وزیر اسرائیلی، که اعضای ناوگان بین‌المللی حمایت از غزه را تحقیر می‌کند، غیرقابل قبول است. اجازه نمی‌دهیم کسی با شهروندان ما بدرفتاری کند.  @Farsna</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/437052" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437051">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0cca0ba9.mp4?token=b1vbir4xKuzN0wwXZuSXcSXyS_HX8TA6YxMsTMqs3smZ9dNNL6VTYoPm4VvD8CNorVLOvCuNOr4tv5-NWL4Y7oM0Pn5fNK7mjTNWWRm6LTW5jNS3jZU7pE3pTlTKWy2XQZNRjNaZMe0EtyYG3ZAdACKMYR7fzB_hQDyepH3kssMS1cFwbpjleiQrZpJDXHMgYhSyqZl1poqps7ff9dpIYy6uJc4EXlltJNu1C9ugyYdVQn6W00dU1H0KN2_y4amEJrYZBLEW1f0dJqI_CB6hayFTytxsFGGDnxpDOCsMTd3FFOSZ_SKBdXJcDTpLqnhKSG0b1-03jNxVwl9wEQ72tpGYwMwKEp-WeZt2YXVQO_WumFjb4QvsWYEs0BsKUo1ERLncp96ZLMnVi1Wqyg39IkojoSXYbJIVSirnz1n_6D9As3tNEZcqfDBOdmPV-0fuZaAxL7KrObQHBk0PacWYu6VsxckJU_bFkkSIp9vjzVIIRKV7sYAyFFEKcw0uXs3Vl5tl0L6rrefpNTMAmymsIfwgxyxZmRjxk4KKEfoapP3gRFNT5mLO22oz-uQAQkSPdDDr92IfxkRCc7mhGIUxPZjO-vJFIsGvweidXlNFLtc7wxZxkJo4rsnK2B3QIqcaFfNymRtGYiCraHhcUiVIg4iJ4jNatg6ordGJw1xJoks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0cca0ba9.mp4?token=b1vbir4xKuzN0wwXZuSXcSXyS_HX8TA6YxMsTMqs3smZ9dNNL6VTYoPm4VvD8CNorVLOvCuNOr4tv5-NWL4Y7oM0Pn5fNK7mjTNWWRm6LTW5jNS3jZU7pE3pTlTKWy2XQZNRjNaZMe0EtyYG3ZAdACKMYR7fzB_hQDyepH3kssMS1cFwbpjleiQrZpJDXHMgYhSyqZl1poqps7ff9dpIYy6uJc4EXlltJNu1C9ugyYdVQn6W00dU1H0KN2_y4amEJrYZBLEW1f0dJqI_CB6hayFTytxsFGGDnxpDOCsMTd3FFOSZ_SKBdXJcDTpLqnhKSG0b1-03jNxVwl9wEQ72tpGYwMwKEp-WeZt2YXVQO_WumFjb4QvsWYEs0BsKUo1ERLncp96ZLMnVi1Wqyg39IkojoSXYbJIVSirnz1n_6D9As3tNEZcqfDBOdmPV-0fuZaAxL7KrObQHBk0PacWYu6VsxckJU_bFkkSIp9vjzVIIRKV7sYAyFFEKcw0uXs3Vl5tl0L6rrefpNTMAmymsIfwgxyxZmRjxk4KKEfoapP3gRFNT5mLO22oz-uQAQkSPdDDr92IfxkRCc7mhGIUxPZjO-vJFIsGvweidXlNFLtc7wxZxkJo4rsnK2B3QIqcaFfNymRtGYiCraHhcUiVIg4iJ4jNatg6ordGJw1xJoks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلم برای رئیسی سوخت
🔹
روایتی از روزهای تلخ و پرالتهابِ عروج «شهید جمهور»؛ مروری بر روزهایی که رهبر شهید انقلاب، در قامت تکیه‌گاه یک ملت، ضمن آرامش‌بخشی به جامعه و تأکید بر اینکه «خللی در کار کشور ایجاد نمی‌شود»، با کلامی که در دل‌ها ماندگار شد از عمق یک اندوه بزرگ پرده برداشتند: «دلم برای رئیسی سوخت...»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/437051" target="_blank">📅 14:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437050">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlaiRoIfkXk2PtItiuCaIE318ZWuYbNQ4nHJr4J978NkSp3f8rFC56oPhpT3qPI_m9kJQIR4_0lPCTUI5Y_5d_3TIRHv-k05jXTrjH_wiOe25bcTMZS-rB8vrvhE43rC_kqbPzI_xasDLDaFCL2dvQ2ZN17QwPUDKH2GfHXhdkhT9IqLOA3FTBMO70KUACNDgqsdaIwwaLGQROXlgZivPZVHIDuJtOg4dTKHbCgBIuMLMvIAVxVEopzzbYjlE64Y4-XNYfrhS5nFKxtcQwCByQiCP-rIQ4O9ZJyN--eKwSiESRB3fJpQv7o1c04zmMNA8aJL81wZibXAfxrZFopqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی
وزارت خارجۀ روسیه: فقط خود ایران باید دربارۀ ذخایر اورانیومش تصمیم‌ بگیرد
🔹
مسئلۀ ایران تنها از طریق کانال‌های دیپلماتیک و با در نظر گرفتن منافع ایران قابل حل‌وفصل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/437050" target="_blank">📅 14:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437049">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjbgCtfbIC5WmcIEBsNygkFKvgN3qzCyHwVQjxhKA1FvVFwaHGnjMTh0NNyxhCdp98DIijbtTnAmLcvcH9rKbZPbTU5OuhQSZxjZDJ9mbNUcbmJu44F1q_ZxKb9B7IyeZ8lKTgk7KfAc-jfj12gUdAZVgk3sf83SHmCWgg2UcVmRldpbMSwzwNfWpbs5vOx70tXMjKy-hVjRffO03yVqdYyM07zMKe50DMFKReJyD25ToldmJDP09ylzmfCvASOoiM2Mjh-I7hxI3Jiqjk8CeQS1zOBhXmWyFTTn7ic6SrzRfKxuH8AbaX_A6_64dyYcSl4MZwCRTyU_vy-Avgn3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دومین سالگرد امیر دیپلماسی، شهید امیرعبداللهیان فردا در حرم حضرت عبدالعظیم برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/437049" target="_blank">📅 14:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437048">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b753e2edf.mp4?token=SNTbow4_KSznYmW-ESVWSLVyzHBHlUMFT-0ypt6C0VvnDXVP8UGKHlDE47LeoG1AwL6C58pVAtfmiu6b28I_BQr1CvBLN_GJmfpF3APd29hWSZ4HnkNSeVBE2eX-5jgqrInbPr_T28PLmdD1A3o5K81BSZQmAaHCLqHTsbSiyLx75sj4yLneIfR0A8fSoEOJBW8i4MgNh-TYY_0e5Y2oXQsA1MFoIOREMUr-jkMhI9rN_mZdqwMT41c4qfTKYr2T0IjPzr6h87VeTWfiAz4pWu887aPF5HKIY6jVkAe29nKpZK59hoFShzf7OwAVLtLQav_XjAtt9dhp5W3MCLKR-laLo7ArO2dSQiZGmo3sp6oWWKCzL-IkU2wQxqmvBfv2MavOhF9eexSBV7PPJS1wMywoULXh4iAE47gJ4vLKz0Nj9dtHSFfl6WQJGdzKM8Y5Ip3aRBOUZ60c8oTHGBkCZs6x_GOK068_wPbEIg3Mbzs5nDzC5V3sEQuVWWk7lAa6PllielyujfoFoQEVF4nhdiloU-jUdmuXCTD7sKUtTRQcpk1ZXOvC5qQa1qDQc1twZLzXczAqgzoKV7qlcsDQjjMhQ-GDtvRS8TLgMAvKdCVgXblSYoXiq4wdL2MmbYGJnYRN8VunKJMnilGK8l4FuLYkuJiOGlJM2lmy2cVoYVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b753e2edf.mp4?token=SNTbow4_KSznYmW-ESVWSLVyzHBHlUMFT-0ypt6C0VvnDXVP8UGKHlDE47LeoG1AwL6C58pVAtfmiu6b28I_BQr1CvBLN_GJmfpF3APd29hWSZ4HnkNSeVBE2eX-5jgqrInbPr_T28PLmdD1A3o5K81BSZQmAaHCLqHTsbSiyLx75sj4yLneIfR0A8fSoEOJBW8i4MgNh-TYY_0e5Y2oXQsA1MFoIOREMUr-jkMhI9rN_mZdqwMT41c4qfTKYr2T0IjPzr6h87VeTWfiAz4pWu887aPF5HKIY6jVkAe29nKpZK59hoFShzf7OwAVLtLQav_XjAtt9dhp5W3MCLKR-laLo7ArO2dSQiZGmo3sp6oWWKCzL-IkU2wQxqmvBfv2MavOhF9eexSBV7PPJS1wMywoULXh4iAE47gJ4vLKz0Nj9dtHSFfl6WQJGdzKM8Y5Ip3aRBOUZ60c8oTHGBkCZs6x_GOK068_wPbEIg3Mbzs5nDzC5V3sEQuVWWk7lAa6PllielyujfoFoQEVF4nhdiloU-jUdmuXCTD7sKUtTRQcpk1ZXOvC5qQa1qDQc1twZLzXczAqgzoKV7qlcsDQjjMhQ-GDtvRS8TLgMAvKdCVgXblSYoXiq4wdL2MmbYGJnYRN8VunKJMnilGK8l4FuLYkuJiOGlJM2lmy2cVoYVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلیمی در ثانیه پایانی طلایی شد
🥇
آرین سلیمی در فینال وزن  ۸۴+ کیلوگرم تکواندوی قهرمانی آسیا مقابل رقیب ازبکستانی برنده شد و طلا گرفت.
📊
نتیجه:
راند اول: ۷-۷ برنده ازبکستان
راند دوم: ۶-۳ برنده سلیمی
راند سوم: ۱۲-۱۰ برنده سلیمی
@Sportfars</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/437048" target="_blank">📅 14:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0XUxC2zFZ2pN_Y6ERClZvGr9y2K1sYo8AN9rOmL0vkksnH03uFuaL_wGhCNkB7QD5E6ekHC3SMigZmuF92dGDzXTy217LqIryNPV8lfDuqhjCoj5N578J-v60_1A3t8KwZSG1Qn-jqg_vq4kFCVBV1WwarE07tbOs1is5-DPxggQBDk5Co-T1rBMLbznxJFRwDilxRyEOU0e1DgEl5g8hGrGpT_gvhsn-tM0QbibXIAoi8YB6fR3KnA4K-fKFCBjzpyknI_QAidoW27OFw0-_0JVoyv5FABbL3WLNG58gSHafdLltfzAIHLk503DJnGvbX7orrqRIykybvhlWnlcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: نقشۀ کریدورهای منطقه را با واقعیت‌های میدانی تهران می‌نویسند
🔹
مشاور رهبر انقلاب در امور بین‌الملل: ترامپ در پارادوکس «تهدیدهای روزانۀ ایران» و «مشتریان عصبانی پمپ‌بنزین‌های آمریکا» گرفتار شده؛ او برای مهار تورم داخلی خود محتاج ثبات بازار و کاهش قیمت انرژی است.
🔹
از سوی دیگر، تغییر محاسبات در قفقاز و کمرنگ شدن واژه تحمیلی «کریدور ترامپ»(زنگزور)، نشان داد که اکنون نقشۀ کریدورهای (راهگذرهای ) منطقه را نه با تهدیدهای واشنگتن، بلکه با واقعیت‌های میدانی تهران می‌نویسند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/437046" target="_blank">📅 13:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA2ln2zGaDEURqlox4jhYRiB-NPl-8lBEZvTRpkLK804cugsBsxtfUUguzUuBYNhY2CIbT8Kp4QpqlYMMLTy7CqLOMgx96oM8q-nuRexEUCP_WnkirNdPH6ubPD4FCSqrI3ZIyg8xPNkC_t9V-IAPgI_IbvlMln9AXGFybNGyTTO9xkB2nCuUvZvWMnWEsrf0ceFAIYLpKpDwqZysCpz0ifgIp82O-6yatFIPqkXFtF53fhOyUJwZ9elSao_sgkzb2tvWPsiMklZgro41tFPbhPw8A0VjgK5zE-gWa-EuH1QKS-pOAGoJY0JoODxsYdeP3XhRznkBfdeiI9OnJv_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس،…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/437045" target="_blank">📅 13:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9ab1c59.mp4?token=qiycEJ9bZjEizalzD_rpEsdamRZTAzlPnmcfSMNQCrjOQWvewC40slralMBr35HWrASOuwdXq9hMIL38sCcfyhjqvx9jYkC24qQ0h__dEr1QFKcRHT0rpVOlgffYNDnLOrWausMz82KynsmIN2u_P3pukxg_I9ThjAeOpX3niez-c-gDEz5XvG3DC7FY-bUTKzUj3h4jKrr5c5sadY4cmmm_WwbGMEIyvP2fcBCwK9ZJqucraRFYgrFb7oEcHpugk4s2FJJs_qi4EL97H0InV1ATjg-YBPKwwCvEntogOHyJ6xvSmL3yUuf5SLzIs6wCqrlb67i8UisqNrZsTqWpIqVVIVsXM9RrpeDJsDYJGWgLHtSVJCE0byL6zLm6bQl5-iHSqR3BURIlDc4O0AGy_CFHz2_81kwLLEgizmaBr_TFXNFvebWzRpGe23XzFSKwLkKg3VU6t2Och8ToJCqfiBid1Z5Lf-CTHLC8LrN73_SaEpptz7Xa4fZWwW-zksVEbLJWhVIcd6gmuV9YETRyD03WWZXX6JYLQsPHu4fRKBLWGd60MHYNaMFpBe-WC_4-_fa913Cq6eQDV9IDJbROqBnFbZjHysI3tSFvSAu6hZw57xTnZCgiaZrBW3bI_ZCUSn-H5Hlj1JqKf9h1uf4tqa7bwrMq5G-o6jRQGS5K-Pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9ab1c59.mp4?token=qiycEJ9bZjEizalzD_rpEsdamRZTAzlPnmcfSMNQCrjOQWvewC40slralMBr35HWrASOuwdXq9hMIL38sCcfyhjqvx9jYkC24qQ0h__dEr1QFKcRHT0rpVOlgffYNDnLOrWausMz82KynsmIN2u_P3pukxg_I9ThjAeOpX3niez-c-gDEz5XvG3DC7FY-bUTKzUj3h4jKrr5c5sadY4cmmm_WwbGMEIyvP2fcBCwK9ZJqucraRFYgrFb7oEcHpugk4s2FJJs_qi4EL97H0InV1ATjg-YBPKwwCvEntogOHyJ6xvSmL3yUuf5SLzIs6wCqrlb67i8UisqNrZsTqWpIqVVIVsXM9RrpeDJsDYJGWgLHtSVJCE0byL6zLm6bQl5-iHSqR3BURIlDc4O0AGy_CFHz2_81kwLLEgizmaBr_TFXNFvebWzRpGe23XzFSKwLkKg3VU6t2Och8ToJCqfiBid1Z5Lf-CTHLC8LrN73_SaEpptz7Xa4fZWwW-zksVEbLJWhVIcd6gmuV9YETRyD03WWZXX6JYLQsPHu4fRKBLWGd60MHYNaMFpBe-WC_4-_fa913Cq6eQDV9IDJbROqBnFbZjHysI3tSFvSAu6hZw57xTnZCgiaZrBW3bI_ZCUSn-H5Hlj1JqKf9h1uf4tqa7bwrMq5G-o6jRQGS5K-Pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درس غیرت کارگر ایرانی به رضا پهلوی و وطن‌فروشان
اعتراف مهم رضا پهلوی و مشاورش: ما بودیم که تحریم‌های شدید اقتصادی ایران را درخواست کردیم. این تحریم‌ها دامن مردم را نیز خواهد گرفت.
@Fars_plus</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/437044" target="_blank">📅 13:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqarlO48sO1T-QbNqdWMt6jU046sORTICrH0-2U7FdLb3NdukCjzC33hlk4PIcIjljCkhDEcAXx1Wt5Uu2ktpDqA6QhSWtxeyHDt47m1ON0VUJc9v5JM6W7Qcr6Q52BRr39DJHVCdlhOng7PZAKrwKxGmSMJlCwzDH0o3lA8VycAYIVht2s4QfsuRTQdy4nDeQep5WqY1oJI75Nx8Z3XrThwRfsYGgooPj8-DJZf6YCAPNo56jUnMperJKo11BquYBxAD70KtW2oePtAh0FQLODH6LQu_LGEn7Mri-V0SpbpRW6XjAQ_3lyUdt_Tt7NL-PZMWu7gj0g2hh5bUAd0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
🌐
بانک رفاه کارگران و صندوق بازنشستگی کشوری تفاهم‌نامه همکاری امضا کردند*
🔹️
با هدف تامین مالی طرح‌های توسعه‌ای و سرمایه در گردش شرکت‌های زیرمجموعه صندوق بازنشستگی کشوری، تفاهم‌نامه همکاری بانک رفاه کارگران و این صندوق امضاء شد.
🔹️
این تفاهم‌نامه طی مراسمی که به همین منظور در محل بانک برگزار شد، به امضای دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران و دکتر ازوجی مدیرعامل صندوق رسید.
🔹️
دکتر اسماعیل للـه‌گانی، مدیرعامل بانک رفاه کارگران طی سخنانی در این مراسم که با حضور جمعی از مدیران دو مجموعه برگزار شد، بر ضرورت استفاده از ابزارهای نوین بانکی برای تامین مالی طرح‌های اجرایی و پروژه‌های توسعه‌ای صندوق تاکید کرد.
🔹️
دکتر ازوجی نیز طی سخنانی در این نشست با قدردانی از حمایت‌های بانک رفاه کارگران تاکید کرد: ضرورت دارد همکاری‌های متقابل صندوق بازنشستگی کشوری و بانک افزایش یابد و این مهم با جدیت بسیار در دستور کار صندوق است.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/437043" target="_blank">📅 13:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue2KYqs2Uf2ZBDeCR1D4LLmlse6v07HjlJjgJ2UkQsBKkzbu7NntvSAw5eW9UOOsTMJYyYCpXlJbIenXCzOF1Awp9w7IXzQ4DHpoewDaZkoa8DXCXdiJLcgFmn13lr4FcuAmtvNry07idDhi_87u4srVmGZnSGzxpTPPdlnCcfkHNoZiBfAa0TuDTFGDrb4IoYJnvMMxdl8cAiyTpt37q-vfcq9Jcm5yyGxTpX1AE4pFGrYW6XAcGdAsYMLGksEy_SHMr09mNDaLoaGyIM4BMCEjReezY0SQez94Mhll5IvZuvc135DN78dX8a79DltzwW__ASN4f7Fqx3_b23RhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/437042" target="_blank">📅 13:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/437041" target="_blank">📅 13:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4492e1f20e.mp4?token=dQvtbbkpBX0ilEyJiJiGvRaPiUKJQEJFKG8s5_bx2SoTVfOST56--xXYBIZ4Aw42ncyPuoYgio0joowHWNVW6fVM6Dnj6Sfz0gFHni7RJaH2fTxb25rXi21ZKDdu4oIX4fV4eOd-kDThCpvPmS-6RDVd9lgGUhdly5rQLfEg_iVkosOk2CwX1-N5zuu4IdBNxJhqgFYZWpKzWjiGcwfb6oVYCe-_5eczCdGSDU1Zq11z3MOoxOHi18Ly3Kp9ipS1Re8Qjb1qTFXyOQAJQ6HJigg32ZEYL8AHG_zh0NlOdV2tk8vSQYr6cTbJ6dW1w2absOqyfdW1XWQZXMwlTr7CWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4492e1f20e.mp4?token=dQvtbbkpBX0ilEyJiJiGvRaPiUKJQEJFKG8s5_bx2SoTVfOST56--xXYBIZ4Aw42ncyPuoYgio0joowHWNVW6fVM6Dnj6Sfz0gFHni7RJaH2fTxb25rXi21ZKDdu4oIX4fV4eOd-kDThCpvPmS-6RDVd9lgGUhdly5rQLfEg_iVkosOk2CwX1-N5zuu4IdBNxJhqgFYZWpKzWjiGcwfb6oVYCe-_5eczCdGSDU1Zq11z3MOoxOHi18Ly3Kp9ipS1Re8Qjb1qTFXyOQAJQ6HJigg32ZEYL8AHG_zh0NlOdV2tk8vSQYr6cTbJ6dW1w2absOqyfdW1XWQZXMwlTr7CWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکوردشکنی وزنه‌بردار ایران
🔹
علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی، ضمن شکستن رکورد دوضرب جهان، مدال طلای دوضرب، برنز یک‌ضرب و نقرۀ مجموع مسابقات قهرمانی آسیا را کسب کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/437040" target="_blank">📅 12:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9edae61e8.mp4?token=Bv8G_jayRlaWuhfPYjbqPDcxKGfibnQNztua4Y-EHDGKZpo6r0GIpfXR7ijAey-dIiCvfa2_vosLgXQXQ48vHnwPKQBtMK0YO16YD9jiN2H4aHRsWdlxYrJhBEgovv3JIW3U-4ZrtsdGDsF9RbtYVNhTb0GXgZRBRBB6Nn1znFT1Yju2e772VMpkbj41bIvWPvHhaP5hZBb_-4na4Kz6aC_ZN6dNGlv6_DESzIK_PUDD53-t06Z8dZqbPlr3TK0VkplSXR0HDw04lpfZDI9TKV466IcRi8bBqpH2fofyYAUhgdq_ma8k6zU_y6j2t86KVyuheLpO6fDDfq59wwHJ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9edae61e8.mp4?token=Bv8G_jayRlaWuhfPYjbqPDcxKGfibnQNztua4Y-EHDGKZpo6r0GIpfXR7ijAey-dIiCvfa2_vosLgXQXQ48vHnwPKQBtMK0YO16YD9jiN2H4aHRsWdlxYrJhBEgovv3JIW3U-4ZrtsdGDsF9RbtYVNhTb0GXgZRBRBB6Nn1znFT1Yju2e772VMpkbj41bIvWPvHhaP5hZBb_-4na4Kz6aC_ZN6dNGlv6_DESzIK_PUDD53-t06Z8dZqbPlr3TK0VkplSXR0HDw04lpfZDI9TKV466IcRi8bBqpH2fofyYAUhgdq_ma8k6zU_y6j2t86KVyuheLpO6fDDfq59wwHJ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت محسن منصوری از نصیحت شهید رئیسی به الهام علی‌اف
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/437039" target="_blank">📅 12:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پاکستان: آماده‌ایم تا ایمنی بازگشت ملوانان ایرانی از طریق پاکستان را فراهم کنیم
🔹
وزیر خارجه پاکستان: از سنگاپور درخواست حمایت در تسهیل رفاه و بازگشت ۱۱ ملوان پاکستانی و ۲۰ ملوان ایرانی، که سوار بر کشتی‌های توقیف شده توسط مقامات آمریکایی، در نزدیکی آب‌های…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/437038" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437037">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDAex0t4_h5U-X7NqNwoNMYQ12MsBH2-PEYtaMF2IMJlKxr0mXS1GnjlYBqrIbZBeC2jxQwpaC9EjkWIt9l5Z62-ptIdXcZZOV-K_zD630FJmPqH8vE9ojXc3pNECJlDqT3LY6fyzJkBQpQcWyMINqxSeald1QSc3Mk8QWlCFP77yX5t-U0WmrL304BkvlFdiIB3F9yuCayAODuFN2CHg8nA6Dh2pNgUkIEkysVVRI3lEpiceOhMXXse8gIwjfnjxSaWWCTOl4NX7oXbl0vOS0dogTSspph7INM9-LiwdvxTzNzkg8vhumOfgTLgLzpRiFXzEUwE1dDhlLG6IscwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/437037" target="_blank">📅 12:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437036">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj4w-2gcI03Pp0GvRVKQr3xRjvRLEE8gXGpHrnzQkSKUDSophvMAiKkSus3cy1LMrJ372aXZU1HKCuSYJxtmUSPu0FS_IGv9CS9Bu602_Plos0de56vy2U8xPDMXwHkIQGH1MZF1cFQ_3BMKoDWKUcjOldYiL5kIkyVOZZgDSUJIiWpTRNMqA8o5weRdLceKjIn-Vx_D0OTn4PEpSMlXsdxpvFW-9sqovO7FZEpqCgBlZ6Hr05K12mrOwurKt74HhWk1tStMoHpKVpVE54wh2M5lG8tQPRzXJa4sOGAz9jI8RiE-zFfGoFQpNmCI2KjYXT7-vmjSvs_7UVUPnDJ0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بچه‌ها استودیوی شبکه سه را به آتش کشیدند
🔹
روایت شیرینِ مادری که ۶ فرزند دارد از اتفاقاتی که در بستر این خانوادۀ زیبا رخ می‌دهد.
🔹
نام فرزند آیندۀ خودتان را به ۳۰۰۰۱۲۱۳ بفرستید و در قرعه‌کشی سفر به کربلا و مشهد شرکت کنید.  @Farsna</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/437036" target="_blank">📅 12:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437034">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1z6XGJ6HSx9bsahWxY_rw5yL8rnleaBQ86YDa0T06RqjzZygRiDE1TDGnR0daOJY5pwoBVMxl0H36OCbjaBvs5y00IAQyd-DggNtVaGjuJqF9hVxYvT5NPfvcBhjHn0Ox_TVbxrfjFvJU_dOkXydldc7csVXGzF_tC8xenLtkb3OcyxrCIQmZBz0A4xZ_9QbBdlT9w1bYrYgEKvlmwsYMp80SBu4QQEhIylCmy3VauZe9lpKzaoZAWX2AtZPQHtcoCC_BDTAOG2EC3gLQrvczFVkW8g-1vAnie8Q0q-ZJbMYwClrGav4VnqiYX2TrWmJ_PQvKUpLeByrJk7kf5XFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌آخرین وضعیت پروندۀ شهادت آرمان علی‌وردی
🔹
سخنگوی قوه‌قضائیه: پروندۀ شهادت علی‌وردی پس از نقض رای دیوان عالی کشور به دادگاه کیفری بازگشته و هم‌اکنون در حال رسیدگی برای رفع نقص است.
🔹
مطابق مادۀ ۲۴۲ قانون آیین دادرسی کیفری، در صورتی که بازداشت متهم ادامه یابد،…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/437034" target="_blank">📅 12:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437033">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-N1Vn2nNm0KzH-7n_il1zMlGAY8zgUmkgi3epn1U4tJiMhtbDhIc1m5rTeOAzIvzfkW6czLErwO4R6Mr-LjLFTaY0rCNx2U2FIIEz3CvSo4Yt2rCFa7q9hQlhvtI1UiGSVhhv3DOzP0Mqqlj6Mc51_hrCWXjRhgZKzjDNjIkp6TNGWxnmCnkxMsrxvpHNiZhtzJqShDOufUNEgzTp3BpKjFl6g5BB6rttSgTMa2r9EDwz2vheJSoywlTxmD9LIcMy8Nt0fUhZ7K4CeAjWO9rsUbymPI7r6YU75lPYArcv_FKt0vMIkNdT6CXFQi475pbwCeiEgdLST_V6A22_vkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات آمریکا: ایران به‌سرعت در حال بازسازی توان نظامی‌‌اش است
🔹
به گزارش سی‌ان‌ان،‌ ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد که ایران سریع‌تر از انتظارات در حال بازسازی پایگاه صنعتی نظامی خود است و تولید پهپادها را از سر گرفته است.
🔹
«ایران در طول آتش‌بس شش هفته‌ای که از اوایل آوریل آغاز شد، بخشی از تولید پهپادی خود را از سر گرفته که نشان می‌دهد به سرعت در حال بازسازی برخی از قابلیت‌های نظامی تضعیف‌شده‌اش در اثر حملات ایالات متحده و اسرائیل است» این بخشی از گزارش امروز سی‌ان‌ان به استناد اظهارات «دو منبع مطلع از ارزیابی‌های اطلاعاتی ایالات متحده» است.
🔹
طبق این گزارش به نقل از چهار منبع آگاه، «بازسازی توانایی‌های نظامی، از جمله جایگزینی سایت‌های موشکی، سامانه‌های پرتاب و ظرفیت تولید سیستم‌های تسلیحاتی کلیدی که در جریان جنگ نابود شدند، به این معنی است که اگر آمریکا بمباران را از سر بگیرد، ایران همچنان تهدیدی قابل توجه برای متحدان منطقه‌ای واشنگتن است».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/437033" target="_blank">📅 11:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmjzQh07OH06avm3Y4hh1Yu3k-zn4_HRUbyjUvLY5twMKJxDVuO29_IHsO6Qwx4rykPERYu4RKRnN12txet006lZb2f-qtyIlGuLvmn-xmptRgX9ZMo-KqryygUHCrezJ9YbXKV5etxhHmM_UF9cgwaxZxK9rtGllandNIHmfdtsoaZFohP94FKAgqlMnL-zNH-RXMOOPrWDkgCinTQWzBUHHtyWava56orgsfHMtq8ER0hft63_ayUcIn8yF5v5G891rCFW1QPz1pAEhJ8DsEYHMYEgsZvRgQ9Aac1w6T5p83uJJ1jyFv_vVaRrd8PzZmjUbRenXThECjxRAR10Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس صداوسیما: در حال تولید مستندی در تراز و شأن شخصیت شهید لاریجانی هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/437032" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f325018a0.mp4?token=N4IqlgPlL-z3O_20PxKxAM7N3EdnbtNFhGit1M2KbXmSvF6h7rtcJNTXXwhq2MbwlNvencg9H7_Ui1bAZ9JyhUfLS_EWWYPX8svutK-Qd5GikFXwvQa8F0WRDqTBbmQwH-1m01QQfMAy21NV6WaU2RJKXWE9O8xUJ3BJgh_FzV1v0jBOhstDfIHYPfDzDYRnZrxkWjrdddlxExbqS_7jOhLmnXaIjXIZ1-H6qgOKZpGxAmam4Qym0_dkPTbggUU2rgK-g-Go2RTc_Mh6VPsxraGVi9SUMFplFH5cVllcQgtZlB1z1SPP0RRg7Mh3CaH9KCVBNAE78QG2mQSEpZRqUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f325018a0.mp4?token=N4IqlgPlL-z3O_20PxKxAM7N3EdnbtNFhGit1M2KbXmSvF6h7rtcJNTXXwhq2MbwlNvencg9H7_Ui1bAZ9JyhUfLS_EWWYPX8svutK-Qd5GikFXwvQa8F0WRDqTBbmQwH-1m01QQfMAy21NV6WaU2RJKXWE9O8xUJ3BJgh_FzV1v0jBOhstDfIHYPfDzDYRnZrxkWjrdddlxExbqS_7jOhLmnXaIjXIZ1-H6qgOKZpGxAmam4Qym0_dkPTbggUU2rgK-g-Go2RTc_Mh6VPsxraGVi9SUMFplFH5cVllcQgtZlB1z1SPP0RRg7Mh3CaH9KCVBNAE78QG2mQSEpZRqUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بچه‌ها استودیوی شبکه سه را به آتش کشیدند
🔹
روایت شیرینِ مادری که ۶ فرزند دارد از اتفاقاتی که در بستر این خانوادۀ زیبا رخ می‌دهد.
🔹
نام فرزند آیندۀ خودتان را به ۳۰۰۰۱۲۱۳ بفرستید و در قرعه‌کشی سفر به کربلا و مشهد شرکت کنید.
@Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/437031" target="_blank">📅 10:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437030">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671c94d9f4.mp4?token=P27aFMRnvHVVL52ZV1dU75qVtO4ySp2iFVzQs_uOPXq07cHaw4iEdFsTOLejWdfTmbHKuT1P6YZhBtHvjLLKfecIsRtH-h3Xh8cGDC8y_POw39oWIaTMc9iBcPm8qozPJ-naKlZN8CrB0iOrVYv6zoY5wx5ijkYKakuEqmexYUwiRRUwZjJ5dqty13eMYQ1QO7T0YE1TQ_vpmmA5y5j6hC02ITIWaxOffjRooNwPoibFUwmCb6BqLs-n08GdgqR5TF14cM_ZVOW8297I95U_rtDnh5LERgyGANRrDhsuqLQ6acrbvwr8TzDltTy9dC6gJyz0_Nl0OZXZqxgIZzCZQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671c94d9f4.mp4?token=P27aFMRnvHVVL52ZV1dU75qVtO4ySp2iFVzQs_uOPXq07cHaw4iEdFsTOLejWdfTmbHKuT1P6YZhBtHvjLLKfecIsRtH-h3Xh8cGDC8y_POw39oWIaTMc9iBcPm8qozPJ-naKlZN8CrB0iOrVYv6zoY5wx5ijkYKakuEqmexYUwiRRUwZjJ5dqty13eMYQ1QO7T0YE1TQ_vpmmA5y5j6hC02ITIWaxOffjRooNwPoibFUwmCb6BqLs-n08GdgqR5TF14cM_ZVOW8297I95U_rtDnh5LERgyGANRrDhsuqLQ6acrbvwr8TzDltTy9dC6gJyz0_Nl0OZXZqxgIZzCZQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشور پاکستان با وزیر خارجۀ ایران دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/437030" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437029">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0933e54317.mp4?token=nPe17OlLZLhcrbeTtAe0mBQ1mpCCDtGkIP6H-pqqy4_UncQXRdkSCagzJhsCtvPPJBEoLcMoyiZrwxYcI2UwWL1I_g7_AAERWzK9jWTAQDnWahoP1hdARnuqDrH6ExgDOYTzDaow7fGmFGj9l8lBfo6qoXGtyWz1eWQXnmSFPplGivOxj544YRJ1DTb3EQ6kFTieLc-E22qoIYCZltuJNBchxVUTKCDdxcuvjLuWqk8LaQjawv7sVhLI1F7kG1QdG2o_i6jGRzzQCz27f1S_46tLVYeoMC46NAZXMIL2UVa2z4Q7XKvuldjWjypMvFnNNV4aQNei-o7R1N8Di0_Ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0933e54317.mp4?token=nPe17OlLZLhcrbeTtAe0mBQ1mpCCDtGkIP6H-pqqy4_UncQXRdkSCagzJhsCtvPPJBEoLcMoyiZrwxYcI2UwWL1I_g7_AAERWzK9jWTAQDnWahoP1hdARnuqDrH6ExgDOYTzDaow7fGmFGj9l8lBfo6qoXGtyWz1eWQXnmSFPplGivOxj544YRJ1DTb3EQ6kFTieLc-E22qoIYCZltuJNBchxVUTKCDdxcuvjLuWqk8LaQjawv7sVhLI1F7kG1QdG2o_i6jGRzzQCz27f1S_46tLVYeoMC46NAZXMIL2UVa2z4Q7XKvuldjWjypMvFnNNV4aQNei-o7R1N8Di0_Ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری مخلان نظم و امنیت در جنت‌آباد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/437029" target="_blank">📅 10:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437028">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
معاون وزیر دفاع: شهید موسوی همواره بهترین تدابیر را به‌کارگیری می‌کرد
🔹
امیر سرتیپ شهرام: شهید سپهبد موسوی در حوزه‌های مختلف همواره سرمشق و الگوی رفتاری، اخلاقی و کرداری برای هم‌رزمان، سربازان و نیروهای تحت امر خود بودند.
🔹
ایشان به‌دلیل اینکه دانش‌آموختۀ مکتب ولایت، اخلاق، صبر، استقامت و شهامت بودند، بهترین تدابیر را به‌کارگیری و ابلاغ می‌کردند و ما در عمل می‌دیدیم که این تدابیر تا چه اندازه کارگشا و راه‌گشاست.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/437028" target="_blank">📅 09:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437027">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0080955e3a.mp4?token=Kc8U05ifpfYevbai2TLAtGPdu6QOl9U27LfH9uEocRueuplMwaVHJHjnvm5rDdkgLHmL4p_oj60eaqTUhUb59RpfpuM2mGJ-C1Q6KHx_Cnuqt4yXnXUShDX0WkXT4w98J1yj6N68bFBIX84bn2fHMNe1L3aceCRCrWit6kE2KAVHwONw021s2SjIU7Wy7ICEGATYMjrzmytj3_BI3Y79WiAAZaTkvFE7Rj838oW49YzfQM_NnVeSu3jO2wLg3zUhKtI145_n87mYD3lXytfjW7zItwdUfwJsYCUY4YodSro-Ex9PJiXEgw2iOJPQuupbHFME4Rq2StJK7ltA0LjzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0080955e3a.mp4?token=Kc8U05ifpfYevbai2TLAtGPdu6QOl9U27LfH9uEocRueuplMwaVHJHjnvm5rDdkgLHmL4p_oj60eaqTUhUb59RpfpuM2mGJ-C1Q6KHx_Cnuqt4yXnXUShDX0WkXT4w98J1yj6N68bFBIX84bn2fHMNe1L3aceCRCrWit6kE2KAVHwONw021s2SjIU7Wy7ICEGATYMjrzmytj3_BI3Y79WiAAZaTkvFE7Rj838oW49YzfQM_NnVeSu3jO2wLg3zUhKtI145_n87mYD3lXytfjW7zItwdUfwJsYCUY4YodSro-Ex9PJiXEgw2iOJPQuupbHFME4Rq2StJK7ltA0LjzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکورد برداشت عسل طبیعی در کشور شکسته شد
🔹
در روستای چاه‌انجیر شهرستان سروستان در شیراز، یک زنبوردار توانسته از یک کندو به جای ۱۲ کیلو ۳۰ کیلو عسل برداشت کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/437027" target="_blank">📅 09:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437026">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">۲ تروریست تجزیه‌طلب اعدام شدند
🔹
رامین زله فرزند کمال و کریم معروف‌پور فرزند کمال عضویت در گروهک‌های تروریستی تجزیه‌طلب، به جرم تشکیل گروه با هدف برهم زدن امنیت کشور، قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه، تیراندازی و اقدام به ترور در راستای اهداف گروهک تروریستی به دار مجازات آویخته شدند.
🔹
براساس مفاد پرونده، رامین زله و کریم معروف‌پور، سال‌ها با گروهک تروریستی همکاری داشته و عضو هسته مخفی وابسته به گروهک تجزیه‌طلب بوده‌اند.
🔹
رامین زله پس از طی دوره‌های آموزشی از طرف گروهک ماموریت پیدا کرده بود تا در ناآرامی‌های کشور به عنوان لیدر شرکت کند.
🔹
نامبرده در اعترافات خود بیان کرده برای ترور فرمانده پایگاه سپاه یکی از شهرستان‌های غرب کشور با افرادی از جمله کریم معروف‌پور همکاری داشته است.
🔹
کریم‌پور در اعترافات خود اقرار کرده که از اقدامات مسلحانه گروهک آگاهی داشته و یکی از مسئولیت‌های وی نگهداری سلاح برای انجام عملیات‌های تروریستی بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/437026" target="_blank">📅 08:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437025">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d3f8421d.mp4?token=aNQe3kzsP7j8A4jBFDnFJOxiYWH1ph2iajy40HkWAJJ6WVEE-JBpxxrO6kk3uwhQ9PeKSG_UTiDtnimBE_5i3hlOBXP0MRVP9xMtOWuz8-Rz3_GVcDa-o2DuJQfthlu_LyGvdsDUI6WSsRUnTdmvoMNIun-ZjTQb25LvgSvbdJhF9cD_t36OgfCJ1iGn7AA7f1JUgvTJHBQIzH6LIQ5Z2VJcupw_u_Xx5IWeqe5bNCLoNnzw23qjEr8gg4FfWwbnXoDeW0K3RERJI6P_bOpzBg7xbJbq3_gJ8RO1hRinGfBzYy8IOdVieCTPgbyxAfe2XqVWSHfRLIiidi_7loYr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d3f8421d.mp4?token=aNQe3kzsP7j8A4jBFDnFJOxiYWH1ph2iajy40HkWAJJ6WVEE-JBpxxrO6kk3uwhQ9PeKSG_UTiDtnimBE_5i3hlOBXP0MRVP9xMtOWuz8-Rz3_GVcDa-o2DuJQfthlu_LyGvdsDUI6WSsRUnTdmvoMNIun-ZjTQb25LvgSvbdJhF9cD_t36OgfCJ1iGn7AA7f1JUgvTJHBQIzH6LIQ5Z2VJcupw_u_Xx5IWeqe5bNCLoNnzw23qjEr8gg4FfWwbnXoDeW0K3RERJI6P_bOpzBg7xbJbq3_gJ8RO1hRinGfBzYy8IOdVieCTPgbyxAfe2XqVWSHfRLIiidi_7loYr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اَبَرقدرت‌های دنیا را می‌شناسید؟
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/437025" target="_blank">📅 08:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437024">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70ca853bb.mp4?token=jbqjrHiX6TE9P3Umya80lvXjok1q1SSDT1GNrqmsTAATWMnRhkHXTbxqyxkMS1lyNkEWTmespr8WjhknwW2KhMnBiw-s-GZLTgYx1Ks_VX3wkK0dHi9VRbINCZylQMfEbAFvryaG-fzto78MyEQpufZi64Bn2shVe7avWkYabIqN3cJ8YdOQE_rf4gdODY7GOICrs2M4FvC_O1XMC_E7BXfNJ4pm8Lhn9qvTAcio26R7MiSFZYeRm_FvGLKsns8HxCeGDzOJBNz7QNnsmy2U4e6kizXxUi7ye9Ek4di8cva_78ywvAy_AHvOt6foxa6nwuyFWBSZGtzZn5jgprSFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70ca853bb.mp4?token=jbqjrHiX6TE9P3Umya80lvXjok1q1SSDT1GNrqmsTAATWMnRhkHXTbxqyxkMS1lyNkEWTmespr8WjhknwW2KhMnBiw-s-GZLTgYx1Ks_VX3wkK0dHi9VRbINCZylQMfEbAFvryaG-fzto78MyEQpufZi64Bn2shVe7avWkYabIqN3cJ8YdOQE_rf4gdODY7GOICrs2M4FvC_O1XMC_E7BXfNJ4pm8Lhn9qvTAcio26R7MiSFZYeRm_FvGLKsns8HxCeGDzOJBNz7QNnsmy2U4e6kizXxUi7ye9Ek4di8cva_78ywvAy_AHvOt6foxa6nwuyFWBSZGtzZn5jgprSFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به‌یاد مردی که در اردیبهشت، بهشتی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/437024" target="_blank">📅 07:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437023">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIOcK5DkJvgx1VLNDcFCgkZZyCS_U3wTIT1NXYGvslkwvDpnM-miF1YkThGsiIU6RWg65bdAQqvA5P7eRQAzKPDzsMw0EobVQzPcn_XfNOFcSWyd7gNCV7cHsIVjTvkgVcghMr-85VSLVHR6l7XCo9J3J96yax6Y1r2CUWaM2UG4gP9pIj8I3nMJ5KgqoxsSG04AMDB5sXplIhU53Rk9u1yz2OOxpU9w4ixISKpiBAjS_HA434KWXHnyGafZqq2pILkLSqMo6jhdrsfbU9cMnUN76SgW75J9Bx9eQfKLggCrbYWasR7RNSXCpEhXR3gyrsTave0MbMj4NIklC75-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا ویزای مرگ در جام‌جهانی را صادر کرد
🔹
شیوع سویۀ جدید ویروس آبولا در کنگو باعث شده تا زمزمه‌های کنار گذاشتن این تیم از جام‌جهانی مطرح شود اما طبق گزارش نیویورک تایمز، یکی از مسئولان برگزاری جام‌جهانی اعلام کرد که دولت آمریکا از کاروان تیم ملی کنگو استقبال می‌کند.
🔹
این اقدام آمریکا درحالیست که شمار قربانیان مرتبط با شیوع آبولا در شرق کنگو به ۱۳۱ نفر رسیده و تاکنون از ۵۱۶ مورد مشکوک و ۳۳ مورد تأییدشده در کنگو گزارش شده است.
🔸
این اقدام دولت آمریکا با رفتارهای ناعادلانه و سخت‌گیرانه نسبت به تیم‌های دیگر مثل ایران، الجزایر، سنگال و ساحل عاجل متضاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/437023" target="_blank">📅 07:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
حزب‌الله: خودروی فرمانده تیپ ۳۰۰ ارتش صهیونیستی در شهرک صهیونیست‌نشین «شومیرا» هدف حملهٔ پهپادی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/437022" target="_blank">📅 06:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmav5EnZMEl69pQly4H_z6-JvZ-gJ1BsiCFS4DjOz1y-VLoI9DHAvlCV7Z7lXyAWScu8Fn5za0_Ctu7OLutZ08n7BbjnzVF9FGoAGe8E5maFChqjJphyxP4NDxbz8zuv0Fh5qvszanO8hdwjFbaqON2WvNlS-oIKF6fO4WsK87f4qJtjRBZFPZ8OCs_pryh0chXVwvgrFMIDIQGUJqnRfv1T3oesXOJPOHkFtNZ6_-Hft4jp0hVDZOy9MdqitugX63k9vghO6ja-aKKcGTpoARZyenoNPsrCGLGXqLOkO5uqljpnNgqjfAtmuK8of-vdnKtzR3KOaECCDbF40R21hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ فروند بالگرد تا پایان سال به هلال‌احمر می‌پیوندد
🔹
کولیوند، رئیس جمعیت هلال‌احمر: بالگردهای هلال‌احمر از خارج از کشور خریداری می‌شود، که برای ۵ فروند قرارداد بسته شده و قبل از سال ۱۴۰۶ تحویل داده خواهد شد.
🔹
بالگردها دید در شب بوده و دارای سیستم جدید ناوبری هوایی، و امکانات امدادرسانی پیشرفته‌تری هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/437021" target="_blank">📅 06:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNOSrlAi8cMurzu6in4QDSzwotjTXnQFo96SzjPrU5d0uCgQJgMW5SPQeIOj2fufb2Z1H5WkFV1E5pdSwg-SHc-lE-pght6IobD4nIDvzsupq5EFwm_D97F9ex3yJo75xAsKZ9p7K7qLPFVPemOe41nUxyPmq22GzSjHQvNL0QlhLhuhXItHlHfDtreig43GqxxQ8CgPTe-J9KJaWHATMPaFMoIvqgf_PN0FWT-p3vf714DgJAE1uOltHCset7yGtp-_q_KTMPVQj1JZO2r-xJc0Vw4DkhagExXrE8_YAxr20FgYBJxeJrwIpiQx7Q62HpqJzrgCIcIE7bCzf-Liyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورق بود، مشتری نبود!
🔹
با وجود اینکه برخی از کارخانه‌های خودروسازی ادعا دارند عرضۀ ورق در بورس‌کالا کم است، اما طبق اطلاعات به دست آمده، روز گذشته از کل ۲۱.۸ هزار تن ورق گرم عرضه شده فقط برای ۱۰.۲ هزار تن آن تقاضا ثبت شده است.
🔹
به عبارتی، نصف ورق فولادی عرضه شده مشتری نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/437020" target="_blank">📅 05:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-lJHWstbTNLgVQNdbizNoYpse8y6axkYRDVUmwYw5XEM4x82CD28V4CdsF_lOLsRS7rgKrzCeG0Ai3EMy1tZnLQ__9hbn6yLcokC-chQEQ24J6Tn4Q4Fz5a_jbqxqxROYGEziRgKM9juhkGVIYzhSiAG-3PTTZ225YYpy3DDJhtpS-mnFqZo8v2ZOgvWQECVmMFUyXKlg4ChHT-R2bBKnLVLE8WjW3MlKH29qVcNdFjndpecWmjEYLcgFbc2d18qVfr185Y4ZJZdZgS1IjizsNvXnkfxZ9t7xxEX6PJyT074_1ZMKo_xN_VxJNt43P0fXdw5t-vKFEfCFEbTdZjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استرالیا سفیر رژیم صهیونیستی را احضار کرد
🔹
«پنی وانگ» وزیر خارجه استرالیا بامداد پنجشنبه ضمن محکوم کردن رفتار غیرانسانی رژیم صهیونیستی با فعالان ناوگان پایداری، اعتراض رسمی این کشور را به سفیر تل‌آویو ابلاغ کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/437019" target="_blank">📅 05:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-hf-AcdtKM5Hdh5sm-oHY-JqWwoUtRWKN3-uGTxrr9KE23btbob_sivtx3Zs3t8fVW2FgGxQOi7MqEwn9E42Kx--034gsd_Sb3XWwJ67zOjXKkBFl-NTpSVHvKwkOKXAOtQhXKOgnEr1ZdbKjDtKRPuWvDPZLFTQTRZFGuxfdaqidyB4cPJ8sH_JSyQ6mSi2bASaWht-245dOnH6HDroZ6pp7CkGgKJ0gwQK8_8R7K6NiS9xwFTbFIiu-QfusOBXWnbhJLsyuSm2f8AuQRxoTCFtYeCe5gAPSMScB8eBoIv64NdoY7X4eMPpcqo_mV7KstufbNaBENK21j1TlWqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایشگاه کتاب کودک‌ونوجوان «میناب ۱۶۸» آغاز به‌کار کرد
🔹
این نمایشگاه با مشارکت بیش از ۷۰ ناشر، تا ۱۲ خردادماه در مرکز آفرینش‌های هنری کانون پرورش‌فکری کودکان‌ونوجوانان، واقع در خیابان حجاب تهران، از ساعت ۱۵ تا ۲۱ میزبان علاقه‌مندان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/437018" target="_blank">📅 05:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437008">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osu6IgFbd7-Jl_dgCkb9jZsnqQT9aga8K52XRMctYUd3PS4OYzwiJEVD4hXj2MPwU0QKYxtSvQKDBWgV5wCbdtbwjLXvZ9x3k5AAyN3qSRVOgPSI4GlQB9515hbwG19LKEyQHi1mtyZXS0LLneZuGJPMJtlHj_UYbKlCsMerFzlmtz6ZHNO0xKWoAwDABVL85HlbmBGodYqex2KID4g2FcOKar3PqHObPkPQqRw-UFX5ETMxkKOCYN1mUcfLdRYqCHfWkZz6lTaSVT48-yckuOKlH-8vMPzGzQawFDxO706XxgisAo5W-7GcGcTERhNb-R_yl8FTVYi5cfPHDhzZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8FulG4bNujjCsD8hKVUI1S1AqBmw-jTQ2xW4zroQQPrNlnmtap0AfENZSkO8JYX_N_5Zs-0pTmyCtxZzpZthJBQykdmqQa4D-QLg5pP273cX2vQrInu7fBrouvlpsFB2yhE9XDjzRiAI63AIIV9a422-2fMcaJ0Tdcn3e71IzbV7QvPrfdylq6pj_egXJqPHVqoxVYO8rFlpDvztWLcdigJT0MZkC_SbNsY1QqerVTqCOWNKvLCfNl7d4oCrBONp2swzUcA5P1En42l4abigklyF5e_259P9H5VWWEnrMGldQPA2w0VGbX0HJON8Hbxmsp2gop5GAm66sR-53BQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-0XoJ_RiOmvqSpmKkQp44HovcMB1M9Gh4dgw67v6-oQCb26ryvfJWHdBAVzDwywvpvle2DTtz_NPSEI8OQqcFIfe-uHtQXFNsAeLcNgIOkcKVlyI4371EzrniwNKXyMYNAUq_AWiaF_q5vI4KyLEbpe9F0FIg-RRl_-g3VUUwwbEAmoCNoA559mdfYweLVuykwMC7CzJ4XguaaiOEQDI8YBf-XqY0p73zqcgsReRxsP7p92eHIuiz6ZevDUJO8ltfyRu7JL1kqO5dZ-OTE8rbjaWab8QgtndI7V3rsFAZqYBfAkJ0wI219mq4aRlBxDR8mRzXORshqZO_fI7wZj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PorALkFKGqjCQ3t_vLOE16TffWVoPQIFqAEWA8n8TDMVfHs5Y-2MK47u7Da2Rsr0c7ObKC34i1oBFmK0ilaqRdwglupztr-y3yU3ui6r-8akt-atafsuQ_djvvVzV44ps2sqlqAZqFyPXcCh8_Q7PFOCO4y76M0tNu2LC1hkrd1EoeZpJaUnNi6G6vkje2f_V2TVmgOvBeQCYpd67ro1AfNu7CYVUiWmC3-bAzL1KcyoIBZBM9p_uxpQkK2VexpMs6mFsFNGGp1HtsTtQ5C7tdo_0aR6hLU-bsHIGI5TLaMoK9Sxdi06UbxoTDKprseInrtgz96oc9ZS-prLprLizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTfsP0OKJUHZsAXFBKSJ1rHLBKzu04psvUxblT2B8tIBMqH98Gq-QTcM5VDdmTME4Po2dPlG6CsYpI5QiP6DR6NEYqt5P5FNw72JsRO2MXUcTtF6bBL7h3x0DjNtwsGpSkrNqGpEf28PI_vKEiC2FoMXTrSdPTynaODokcSOip4sZmerBnffMqCMh1ZjGJM8sxsBGPSaSoGEfGCh42YWB1nMdAY6ZASCpZ_AWOgoy2_LGYeLMGfhFvXTaOhqPpg_xST87hVfizWDm81hJsKEhJq7nJYqcov79vEp4Ho_v1b9VWPZHJF86WC10_7Z3wJPw6SC9HxXlxkQIKwK5ZfRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8C3B96tOB_HlAHR8Z2GAKjPrmUdcLagnvKD0hRBiF93FRyPX6dHC-JPSlIQfhcfioohPDAzxOu-u2AI72JEGqhwlVdEGA9gaj5W55GIOZFaovcNyR-dg7C2KIRT_pqpTDjkL-SUgtNDmcTze6Y7Z7p3DffyuD7smHSm3O4wG2zeBc_fCfScFNHACs81jKgssfTgyLq_4caZfsau7bangvLEjgj8g30EQQmi58I58n6m1lqnmsXXJEmhWgw84F0lHehkFRnj8RZsJ2TwZhYLG6IEI0oP4NdRduwkXFEC1T5eJ0BEE-j9_oOLk3KGaManZYRckOsAu1hbisJqbiyyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_mkC5n7WNMJ6ET_sCf5q2GpyihsAgXDxECyiwKXbEJEclVlDNwki8miYtzhH80MNn2XJdnRqnOVIjxxMQxAxT8RxKxvzfG2CQbH1xEDL2gcj2P1_-MdtCt5VY_FB4fIDU59EXOwmqdXYIfeEXFw3ULXE-ALgT2UQb4WSMkdad_uc3XT3q96u5363gtqRINJ_7ALyBm_pcWXPyKhXDuWg_pMoG0mnc6tXeCZuY2Ok63j_6pOBdVSivNEOQ0TVvMfly4wJkJN3ByVpjpRoU_y3ZbjbWskRDztqBA9PbbkfB9dcctSiuOBWkqzuHq3h9fbpWRYk1564uKTJhzwXGusyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0rNj_lCHF8MDLpCyYPh1B-rcwcfuXjlibZwrrtcVAQueNNP8e21R4BIk7ZB701xYDibqDzLYlTBF8vH6j-SQy07L4jxpnBsDwNHIE7lTDAZTqDZauCrRWWExhNF3sinD2goDmobYRwnQbcSb55o1711mJUV9P2ms5Gb2IqnJuo88ARuQaiDMgNJtG1uSlzCVaHB04bzw8Gw27ul3T05SsubKhFyNoZu3TZIIuQcX8XQMe3tOa4lBsAKSqrvqc5DWuJ45Su5C6bZoHRv78q1WFG1fbAORhV2Vuy3C9HGBF-GPhBqPv3btR8NxrZxyBULyEOEGOrkIpQ1L3E-AbUIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDHWu2WRa_KEbPLrSfetXTFVM89mCIiP_lzjSzFTG-d1vRdUjCTRMePTE31c7fMsdOKpB5U5_Ir_BdyuxzkFe94IVwV0h-sUk3974NDNsms2YojNDVUWH5l-zFY8Q2jxHlZclh5sDwVHwLVWUNMVUkz4m5DQmalX4q9vn2PDGZ8FNxifQ4fK3nZbcVq36G1EaLX1tm6Lkmx8mm7mGMkshV7DkheDnTfh2gFrcflF4HxLLvLbvV_0V8xgO9xhEX4fIWnAFXzdd9q5hxIvuqA3PxnoNbE9OKGcXfto2GfrShCcohBiSygavgrwA8vIAFD07HTjgx7rPs9iIUyyn9cCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2u9v28FyKWNVwQ0GEDtbYZjx-2MBtMVjPMkodwVrcPkayldMcKbqLfmLatgf3wkLF8zFcI3-0Dby1CC7cTce2cfGbu2cdOusWNsvh7rV0NaYoxIuO2W5YwZINWyD0CSLBthIhGb7pSQICtSgt8-Dnu_TFMekKT6iAHOjZBZDtpvznT600J2UfHEvfN2i4ouiV-wOVsVO8ko27Ah0WyhmoHGvkzQHV-vrMPUwW20906Z4NJ-tUDgC1oC1tgGT4Vzu08v5kuuBzg6BJ3MwRNrP-bbaZhqtLgH5wA7y2UEg4C3ljDe8JrOnlIwmA6EFZMR-z51fCp7FJljYFLklXYQYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کودکان میدان‌دار شب هشتادویکم در کرمان بودند
عکس:
مهدی امین زاده
@Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/437008" target="_blank">📅 04:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437006">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_mtIhadR-qJbrLRPL-dZ6YOuP2a9Lwg3e1EvBbbdErAWBj5HADse4wBfZZ8sfTolAZWeY2MOPjXWilE1YRIXPBIL9av_1c98iukbor3tK7GF5jiOhLadY96BmCK2d9VXczh1QtgQ55v0MniQA1iaq1P7yuGTjHCGwLdBLQS8bvb9MuQ5J9Q9y62tf6qYObD2jHW7PWVzBVVThKL240RDbF0iEAj_bbshQnJxl-GOhTMpsnwWL0I9eVAmF9Zde1xZyLmQmE6hH6fJioiS0UChkLEf0cGlI8D96CacevTEdM2aMeMuTgPdijpENmMRqZzB1zQUmiYiQRoKDjQchXzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور چین به کرۀشمالی می‌رود
🔹
مقام‌های اطلاعاتی کرۀجنوبی مدعی شدند رئیس‌جمهور چین هفتۀ آینده به پیونگ‌یانگ، پایتخت کرۀشمالی سفر خواهد کرد.
🔹
گفته می‌شود این سفر در شصت‌وپنجمین سالگرد معاهدۀ همکاری چین و کرۀشمالی انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/437006" target="_blank">📅 04:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437005">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مدارس سمپاد برای دانش‌آموزان دهک‌های ۱ تا ۴ درآمدی رایگان شد
🔹
رئیس سازمان ملی پرورش استعدادهای درخشان: حق‌الثبت برای دانش‌آموزان دهک‌های ۱ تا ۴ درآمدی به طور کامل رایگان است.
🔹
دانش‌آموزان تحت پوشش کمیتۀ امداد امام خمینی(ره) نیز در زمان ثبت‌نام آزمون‌های ورودی از پرداخت هرگونه هزینه معاف هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/437005" target="_blank">📅 04:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437004">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
تپش نبض انرژی ایران، با تخصص مهندسان ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/437004" target="_blank">📅 03:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437003">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9JJri0crQU0RCn6Kprdr3dFyj45lXDcupE53Vip9YQqj-8Xq_-2_Qa485jU0Fvt8iNVMcE9y-xPFWF0sQBXA7Y4AeeAqbZ2N7DJ98zPDHJqRyxXhL97RjZd6k6KY0I1JOo0noNzGy0ZddJgJqxrz3BNxZ5eJNbhRFMkaweN6cJCnkLyx1bqvVSSqkO8fyiRYdY5HHYuohKFBZ3KrWwBHngLrQoxHr9THMta6J9rg_V-vPsYW4FSoKtSmtzRsHgazB_jQm2CJ1M2k6ElJ8KkP0MmXnL8GBIDmwrzLETbExkYlAJxCIoEwM4yKqN_UqSbCOePZyRL7grHm2MeQzQ1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آشنایی با جدیدترین حریف ایران پیش از جام‌جهانی
🔹
تیم‌ملی فوتبال ایران روز ۱۴ خرداد در دومین بازی دوستانۀ خود در اردوی آنتالیا ترکیه، به مصاف مالی می‌رود.
🔹
مالی که در ۱۴ دوره حضور خود در جام ملت‌های آفریقا، نایب‌قهرمانی سال ۱۹۷۲ و سومی سال‌های ۲۰۱۲ و ۲۰۱۳ را در کارنامه دارد، تاکنون به جام‌جهانی صعود نکرده است.
🔗
برای آشنایی بیشتر با جدیدترین حریف ایران پیش از جام‌جهانی،
اینجا را بخوانید
.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/437003" target="_blank">📅 03:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437002">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک مقام ایرانی: آمادۀ استفاده از سلاح‌های جدید هستیم
🔹
یک منبع نظامی ایرانی در گفت‌وگو با شبکۀ روسی ریانووستی: در صورت تجاوز مجدد آمریکا، ایران نیز از تسلیحات جدید استفاده خواهد کرد.
🔹
ما سلاح‌های پیشرفته‌ای را در داخل کشور تولید کرده‌ایم که هنوز در میدان نبرد استفاده نشده، در واقع آزمایش نشده‌اند.
🔹
از نظر تجهیزات و قابلیت‌های دفاعی، ما هیچ کمبودی را که مانع دفاع از کشورمان شود، تجربه نمی‌کنیم. این‌بار، قصد نداریم با خویشتن‌داری عمل کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/437002" target="_blank">📅 02:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437001">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f127d7b3.mp4?token=JmNW6WFO6nZyZiJkpCfTBuSlDpFt3l1G_CqBHhQXRX6oAhu366g9i3OpowP-OFPwJyghz9A03SSHF9YDM4DPXnzusA5zXMwHn91Hb5LkEaPi0e41fnzw-uAUql8g7U2jY-KExy2KgPdJkR0Jm_nzmhBbrEATmEpsy114kf5WGIbK0PUEGlWGQlQht0wf03Y5Xme_SKPTZm3QDVf5IeOtD0z_1LizD-2kgQVdGhvqcM4ar5wbMmUmzp2kiMYhgX40cEHHvfCNyBAuJM41_QHzGjuzrSC90MgCarxto56V29BMfJ9RXYxOjn2Gz9LhL8SH2dKM8hpgw1qVlO42otSGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f127d7b3.mp4?token=JmNW6WFO6nZyZiJkpCfTBuSlDpFt3l1G_CqBHhQXRX6oAhu366g9i3OpowP-OFPwJyghz9A03SSHF9YDM4DPXnzusA5zXMwHn91Hb5LkEaPi0e41fnzw-uAUql8g7U2jY-KExy2KgPdJkR0Jm_nzmhBbrEATmEpsy114kf5WGIbK0PUEGlWGQlQht0wf03Y5Xme_SKPTZm3QDVf5IeOtD0z_1LizD-2kgQVdGhvqcM4ar5wbMmUmzp2kiMYhgX40cEHHvfCNyBAuJM41_QHzGjuzrSC90MgCarxto56V29BMfJ9RXYxOjn2Gz9LhL8SH2dKM8hpgw1qVlO42otSGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور اهوازی‌ها در هشتادویکمین شب حضور
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/437001" target="_blank">📅 02:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437000">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7l6FRzOylhwC3_k7jRd0az64McdwkySqJrxCgEsv8POHXd5asZ_qOLDPl-35wcP7cjl43cj9XFstRxbtpC5itcTTr-pB1LTEPIlKJZa_dy6sJl-2W-k-4GR7RZfq5mGtGuKFdTxxjspW-Phtn8zOimnlwdgZ6RtP2d3P7NrbWaA6QuHiy2PxeKzts3sWT09BtmslccMFwdwRikXExgiFtWZXH6P3h0YDleP924vb7GMhhaKvOBEeFWGTMZy1iWJL7cnUUkJRo1kECwDIJGLkYHg09Obikz1f_w7t-NBYE5j1mfGY_wMxi9zMNZK1pJrSK0HnHEf876lb9ddjWiu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ۲۵۵ هزار نسخه کتاب تا روز پنجم نمایشگاه مجازی
🔹
قائم‌مقام نمایشگاه بین‌المللی کتاب: تا روز پنجم، فروش بیش‌از ۲۵۵ هزار کتاب با حدود ۱۰۰ هزار سفارش در نمایشگاه مجازی ثبت شده‌ است.
🔹
ازین تعداد، ۲۲۵ هزار و ۶۱۰ نسخۀ چاپی و ۲۹ هزار و ۷۴۴ نسخۀ دیجیتال بوده است.
🔸
مخاطبان نمایشگاه تاکنون ۷۵ هزار و ۳۱۶ عنوان کتاب مختلف را خریداری کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/437000" target="_blank">📅 02:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tRPP0rVZkYS6css83TAszzEPda8ImdO3jCo9xvDrE-rQEOCHlfz5xA2vo0u-P6q-QpmabyC8Y6BNb7lS0s2KyJsZidO9tbvYZhp3BGFhvwh2tf8XgQRT2Tg0d3Ws7aogbNZJILFMLtIpLlcZdZzsKCZaF1M7rJKMT0K-cXnvLOQxkrYpINsP46fcH2BrU6GdTqtLuWavz_Sf6Etwn7RAworpCizRlsoNN9CghmzaNUa7r1bYGwZMQsn6TNJYzHwyZMfVHvvm8MEIBtkrECpP_-MTQsc854S9fazF1bbm6LvcVjxBaDciKtYkFYAmHGCflbDhNOVFSU0c7XhFcN_f3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6oILvdvlU7dAM1vNincyvfK3A8WyhaGIdHEuaxnVgjZLazxAt7kImMT1pkZgk1mG_8m4fFBSOvsutvFZSDwG0HPpDchNvLWL85wwb27YhIjr4Nybbf95eSVjOotBLU13GBvEDk5aKKxi2zBjlOI8mOmXcma0vqoanMj6tiRUskDJwq-lCGdLU0U-ng_lB9LWc_Qsi7BljZLaYYRCJ2s5hyTMuPhv4n40XMEI6_t-flbOKemn1Icbfk1QMV9jU1Xjw5WF7aLD4v8kzerk3ZT74sYCxv-4GXCtpWauVncuzGFsICnA1IpmpmXJOiybq3dpsk9P_vkGpQtrnzRh80NQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4PVDldcBLyyKRUlACqV5EwO1J9X7l1jt2QK-VQP73Bp5uPKA_D7h3HHaMFHGfKt1lQ7nF5RB2LlkYXScJelYrblPi9S2XoZhVthRx8ZErwVEy7J0wbsBV3cjamWG9pCC1MV_-sbPv_p-Cq199dlfFgxxcAvDq2_9Xt9g6CdJrYKEVDkb5PQpTdOqkHdQaVusuRAGrSVC8z700N2dMyQCwpuuwRnbyMX8qkLzEdwVXRT9c2xuSRP9rPX89geJ9RyswCIENHnzaqBgAeVnp54g6uvMSCtj60nyfR0O_rAnSOtotgwFyUJjgqOE9592rejSydFqnkt5u5CDXfIECwN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUA2oGr83pmoGuu9PkSchZNI0dY8fweqxS67y1mIfm3Av-ZGg5bGoZzaiCtP6tERpP_MCuq52yVPgob0Lzp3KCfCkaUeMn1e78Cfk6yqo1dZNOwWEmnxYatK-krJK7hThLrM_QSDPaC_5UDZGPH42_Qnew8oEK1iq7TG85FY-KkrRa9mj9bNCb-scRyC6rtrVy9-Tq-_WJpc1Q7L5vlX40WYeB4P9ReiohC9XL5c1ufkVS0gyLxR01YE9trwNgef9buxBSAqT_yc50nQ8QCuvCo1QsNuFJKShUTH3ibBz31JPQB-VgVZLHwTS0H3yOHEKwjmXxHehevIh_ZAj4KyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTM8_2P6h6KNbu6JQZJG3sS85gn3g4u7VDP8-IMTyPWwuzHY1R8O9MYmAVD6xzWOGASm1JcVt5k4-LYdLoTtUkU0J520-GPdGjnCq8n6LICvnj7EfDQpHJ8FozUqVVlQzcwhE4dBLaC9DdPGieFvL5-iKFukUwcEGuKUvCONIOX_JIOHr9q53i4w2yrnDLgx_m5bx2avzHtwuGyEpfP3iO5RN25qnEdxKCsfG8MAuIILp1KkVrxVVVPWrhPdAa-ujDsNGQaYNWQip_S4XCZ9tUCLHUxAOwMjZroMGL27rklTsEkXCcPB3oXiMIbTJQ0E10gWbCYuQ-sCqvJgwAoy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMDPmN4UYvVH9A65oC44iYMoU6_Z6VUgTBzjJ1xm8MM5-XOsf8Cz_SZQgESGVWpXjshxPSo99fDAb3YjgKfgE2Nr5COMXLNH5mEGZWh--GwtBSf94cDKZTEQGeh5ybRDj9NiszhZqKgE8yQ5cwMfA6-YqXVMoLHUEPQdr4WHsCjXZkb42NjqqGv667skeWn7Bsis8WSL7kVIb5RXNac6YW5wZjNgGYqw8UJsohuNR0NP6QRUapgvvTG76TVPP41LLzQhQumGg6Pun5JhN9AqH383PlgDFFOPadHORHZJWEnBkpwrXxrniP7JYy0LkiKKgLFJylsU27WHAgTkCKJdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwDJBCtS9ODhpREqzOO-ZEblRzGJMSGDHNbKPvrp0975Mishbnc7GRdcpFzvc9le4M_mvSMYzFvqe5eHWjtAoPWuz5dnMFax_qq5TOsdJCUH1NNMRQNNo5VNsFRJcYARbzFsHaXT8opYwmTwR8grXfA3pfTAsLuFwBSa4ahvtwB9Y3RZi7ECHrHpD-OPZc1LEPPTlCd6tmjdEq2de5J88sLNrNm_nJtiY4qYt9oS4QwnzJC0ddRSZUCCzHhm9dzpreLZsSuBBSpIF790YBd3KQ42xjWELHIixbFK7H4OnsO_1y0xvKi5hottOGexaMKi2QYgDIrxwWlmf172xTSjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBTFrODsZIa3s1ufyAbbGuE-UQ8q8nOalwetlrn52TSwDjK3JlZplMgQAwr_bsAE93nLOToVvEKI_Lm71lAWLmgw4WlWBEsYw_w6ZWPxU3YfTcrhI9zPPzBPtZ0sJxurmyPqnNpvFMCvWzsJ3k6dXoZ9hyKcDnGq5ERQOPz7JmmrUXp_-xVKDnUOH4ss14gRKh3dmyCJDoiJUHa7qfsHtTgPozu5LC0yQNcDcgiYX9lDGqwiA_e5SnElCRjCF5Sz3wzVryiukocJRSqJGq6ykw8M8DNjUBigoAIxZwNW8gWV07HeRCe8WA3pWq4HTDJRjLXHOCn-2UVACoVdj9evRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دومین سالگرد شهادت شهید جمهور، آیت‌الله سید ابراهیم رئیسی در میدان انقلاب تهران
عکاس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/436992" target="_blank">📅 02:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-Lm10LhvVVtVWJY1yPM_17yDi76TgPhbJZTnCegmMfKd9TlUTwWunNo4DORdVK3888iNO5LOfw2-zVrMSza5rdKkjOzoZnU4BMMEGD60UCcKLr097MZJgTNbvGHGNfmqQ3kpP27snZLY6EQLCAsG10ziHmnlcOYnZFEcbX31MtFlHeHGO3CJxPUE4b1ggYty-PhOi9oRJkuQXYMS8FIoLB8U3uyg48LGPHoOh2gpXRdC_-I4tq4mDsB2wWOGTBZ3AzSpueOyb637zeWTTgWYGgYWyesAJ0FsNF9m5mkiP6Xih933hnnbKXUEQcMv2ZL8e4uzAVK4hH1ShCeg-m8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام سازمان ملل: اسرائیل با مصونیت، نسل‌کشی می‌کند
🔹
گزارشگر ویژۀ سازمان ملل در امور حقوق‌بشر در سرزمین‌های اشغالی: اسرائیل حق ندارد کشتی‌های ناوگان آزادی را در آب‌های بین‌المللی یا اروپایی توقیف و فعالان آن را دستگیر کند.
🔹
اسرائیل هیچ مشروعیتی برای حضور در کرانۀ باختری، نوار غزه و قدس شرقی و اخراج فلسطینی‌ها از سرزمینشان ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/436991" target="_blank">📅 01:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌ زاکانی: اجازه نمی‌دهیم سرنوشت مردم به دست واسطه‌ها سپرده شود
🔹
با اتکا به انبارهای مملو از کالاهای اساسی و ایجاد شبکۀ خرید قراردادی، به دنبال آن هستیم که در تلاطم‌های بازار، نقش لنگرگاه اقتصادی را ایفا کنیم.
🔹
با حذف واسطه‌ها و سرمایه‌گذاری مستقیم، هدف‌گذاری…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/436990" target="_blank">📅 01:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436982">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hi7wHimvbiKNwK9GP4N0iT9ruosUG7jc1Alzwq7Mj6uLqvDK-JqfTM5YyU7xvEonuIgUvqFBVLjozrqeZxAdDthX-UXOgfPFj0k7oSmuZQ_RTSPpOpkLlaZAxaH7nGGGxOZZcJDBiCa-on71Pkhs-_BLJvAvLhvaCGlri0G6QcNqYpE3c_jbnnAbh7PVsDDtySh2c81QFw3iYQfr_ibiooJQE4u6a3TtXE7bDOj0qXGIvZ7ELvHaP1nSIUTuY9gOo-cZYUMpZwf5wKiqGwDPRL4oufqQFtPHxSSA1NkC-nddn9K9xaQzFQysAEtubYiN0C_ZqWI8WN_H5WsJ3e1Ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fjqke1kWmuYPFEMBqbTTGA75zNHChYnSS0XNlG7ooepFLa7OL9fl1S2aFjsqZUv3I8g1nxCkXsIUkRRoF9PS5c3xwffzrLSEdsX6ROGChkVDWuJgPqW7bayVnm1epsTcTqnvxjcO5lI43x-Cvhv5Y_71Ks6MxV6X2vptNLcmbRQ2LbexgGajT9hmj1qcw47yOX5VKyKwLuwzJ7JjJcJULWjlkBBZgskGmTR6NsP9lk93HKAtkEEOklIZBJCwY0UQQ5IeS8V7wPkNLlT-XCw5X2CRCTd1IIiOknuZJzm57FmAlTEaatOhwJXnDxfn00f7q_8qeoquOeHQILXt2WLT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYtFoRxiwa6VqI62enKOa5n0QUPvCUsMWwELTxpkGiO1KtCshhRvrJTgVJRZ7GbYojeb_hMrM6Jb8tMlNPhkNh0AHJdfDU5QnlTAEDtzgbmIFAoMgC3apUzfmqVJ-o_Ku4BPkFfuq2AJgZDCeQNssA5W7bbSX0Q0T5jH5yKBBcyv77Ylkvc8lhHWAZIU8pXQAPbN6mezl-cbNOm-C-0b6ZsJNrLhL4KELcLWmtkcHtKuzLa7KUAFtj0yQOxmTZ_IWiZ5aT9VwdzE8PSdvEfwq2g69VZxef-DvOJJKrwP6UFhouLSje7jOjmgUt5BzVbEQM3oxQE0kyIAd9BK-jSlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqWxeraCXvwTNLCmo7jcjoh5lSd0D6G8tkOAizGVX7nwEF4as_n4o6_PCR9kfDh5nwyv1t-04r4-HaMKn57ZzZgpBKXl8G9BQF-GSdM0jNiwZEsFDlPbXP01RBbGviPU3FYCAiIhZ6dAJFC6rbH-86rGGNSLQ3u1hVhVncqnXdZDFk-W7YhR6nao0VLbRik_8-G-tuXTm_Zfuh89MKtvVtHKDEMLU0sIW6F4dY94lHjxpZdnbCw4clk8RcJJyeXZ4bF_sQIX0UA4rhxzBQDmCnKLIEJpsswiTnjSesOSt4r7RQZ2Lb0XFY6xni2qg9VwOhJy54UyPFSet1CN37RH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4QrxGZPQQvwz4I2eYHKm2zNySssMb9rW3svl0pyAPGSTUQ0GQAT2HsoPt_1wSzCVNeluOrkAi27xPoy-j7XkbttyFmUW3tEOc0GOPl1fVjgAMMKJ_Bjd7Mnr2zbkHP_xOyZUGJSGB737mgF6pXy81-Tc5OqZQZxcQ1vgIsBD7eMexKyTLBq8z7J64tC7FGxTF2tz2deFEIxbMp02oxZi6j_PkbWy2SvOkzHIqJZ0-eol-YGLWoleSicA3EmVFAn-E4uGIbHI8Xg_-fZ9OTFMSvZiLMVBBt_9mnw1pXSn_b46g8aDpfcbbQTTl-T4oEFC71Ptx68TQTkb0D1MHVgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQPb1uwBU98FuOSiKhV1eZjCS1wlqBJ3iX4W_6ltg8AcOf_Z5PWikwIANDY1RXjMW5rNAgt9RcTOyvVUi6dASrY89YN4wAJKnzbsqHD9OPBANMwflyA-XQJzcLeKZobktAOxDrjtyrqgPLiGFgXRxiptXJ6cIyJbTwZJCmCfabEm8MDrDF7e1HX7tLciIznKI2Jjge_gX4QNnoQ101e-b_auSWGwHeJ4d2txhdI-1PrgWuY-b3suqDR9Bx-cz5mKcVTL-pepEzLn2m4t_mAurA9VlsSNUwSNIyFwy1QzgdIEdNm3nYSVmtGXjr_KEyeph9D39wPt7sIfPQNWRnzFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP_RwHTXns4I-4e9D7UmIfiWoc9Zo4Q0a-x9HnrhuyD7yEEtyFkK_O931mmV-_KfOykT0fehQAtgDGppiQAoUkNodOZRpTdOfX3MQmvr0xVELCpfey_3sVcZHPy3uqVkBAFrabL9aI2-xMtl1HEfDHxB5DjthMixeeikcx980FiyQ9lQRwaR2EWgocEgDaHdsXBIpr6DQIcSMB5D-tc61-XBFq6tj4e0ofYfQv88Fs7KqFX1i_-jxOW0P9TE01CvudF7cWh9jLlf9QwbEBH3LT_1qtrpitKq0WpSXHxdwjgVdSS6618PbP9A7KFtvFzhyCMMdtYkhA_-gTXsL-gQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qh6ozdZpkqcX9WS5C22PpR_nn6RZiNBYdZdCWlqiCh1QEnWf18YVVXJo1Ci4wRdf8iYobnpUconCQ6WRWeWiJrKVPahw9nEaZTPVgl3RpaIND_jRj5HpzC86vDYTFpXOpZ4JqkB-FnuWbhHLUPvWw-uUtiIHN2I90M-miReXesWZO2Xq6LbXZPHBv2NI1YmIzYb5L2RPQEuEV3CO7riNg_SjVkXBOQ5bFzbRG6G9UojxGpm3qwlkXmXqhK_IxzxJ3hqo-UL4TTyr4rI7ycrETqrv6qoSXiDqbA4kHB-m-DNq-9c_TY5ffUswb73N9IN-29mm-YJ_MeL0wXzOfeZJcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گرامیداشت دومین سالگرد «شهیدِ جمهور» در حرم حضرت معصومه(س)  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/436982" target="_blank">📅 01:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436981">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWte6PTjX2F4P9z9XmW2WR-VTItwSP4td09RSHmNvABttB13GKPKUswIMgBpCAELJFUWq3eaK1FJ3w23O1WQznbvuvQnYTfBcaN5xAa2_NSv1Q1eZGlDLY8tBJsUOz1qye9TBM-UIHAeS00HimEzkjmyVrsFI9wHeOMl-7EiDGaI0YCHC6WtsE9f90bV1cfnoVJvixgC4Nd1FYkyEEo80xcojwbKY-CeATzsE8uRr-G4APFQYx8YG6xikNhfEVstS0wYkAbO8zDvtOqt-sCaSmgnbb_vZZFWM-X2k_DhsNwrN3dmM8s27Xutbhyw3Q6GK1UgUoBnV9OjSeGiMu3tfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش شهید رئیسی به تنش میان آیت‌الله علم‌الهدی و آیت‌الله هاشمی‌رفسنجانی چه بود
🔹
آیت‌الله علم‌الهدی در گفت‌وگو با روزنامه خراسان: شهید رئیسی گاهی به من درباره برخی موضوعات که ورود می‌کردم می‌گفت حالا فلان موضوع به این سفتی که شما گفتید نیست. می‌گفت، لازم نیست شما این طور بگویید و یا برخورد کنید، چون با شما دشمن می‌شوند.
🔹
در ماجرای فتنه ۸۸، خداوند آقای هاشمی رفسنجانی را رحمت کند، در صحن مجلس خبرگان، بین من و او یک برخورد و درگیری سنگین پیش آمد که آقای رئیسی از این مواجهه خیلی ناراحت و احساساتی شد. بعد از آن گفت اگر شما این برخورد را نمی‌کردید کار درست نمی‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/436981" target="_blank">📅 01:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ زاکانی: بخش عمده‌ای از واحد‌های مسکونی آسیب‌دیده تعیین تکلیف شده است
🔹
بیش از ۹۶ درصد از عملیات بازسازی بخش‌های آسیب‌دیده نهایی شده و با خروج تدریجی مردم از هتل‌ها، بخش بزرگی از خانوارها به منازل خود بازگشته‌اند.
🔹
برای ۲۵۰۰ واحدی که نیاز به نوسازی کامل…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/436979" target="_blank">📅 00:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436975">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBRdptojuDdpnoyehWewvcoEIJqmGNVV6wJ-9oJC7cckyD9ExFiEcsMuhc8seqQRFm9dNs9hGJ6eHuIkh2jAOcuxFo-D5s9eHyDczxPfzZ_tb3qbH2qcob2mcbfL1BlnjAlx1yA1wV20Z_8lbHAAQfwE_wep5DUtmzcJolTeoMFJfgKZWzYID1K4L-VrEX6QH4GSAxvkQmHyWndV0nD1zgbfsZBwdYXWgReGB1hYgk_QzQiJ3Ls0PYECwXP5eYnZkfAJiV1Akm0aYI7zRetIi2xFBBGgNtZa4wKqdwZ9tcliYWRyajRAfgThM4C8F4k7_tZM5xZrTsei3j-vuK77dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqTRLg2OqZoOQkKQ7YjVbzJwltT0MbLNo-CqTgbiAAdYkVueyHTPKxdLpICwVZoYZa1eUcHgnY_BguM_O3Z3nRuvS1Mmu4JF13xmgIdGquchqYyQdsXJyYKA4ha9DmrYHP7WkDs9Dc43B4bV45oxwrrQnH6EmXMRYspeIKd2Ul1cLY4Y9xuFrCPMvSnMWGX9pgMseQy_LCLxf3C2opdkkHoqX9oD9-xFadAbdFl87e4BB82-sOsDy8Llyww9aDg9GWSldTydal1Xqsm97b2V6N2iUQL7RHE3x8V_kfTof_Fg9oGFdKe7cMkniKxKvJ0o83nxnNyGzavA1hnoHMsUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwNNpQYXCirnMOctLLuEUP_w5JtHbLAPBIMM4sCn64c1sjOuLin4a3fQDVRnOiBItokYdBPA0ISkIn_NOV17vSO9HFrI5dIqqER7kJuopOxpyaBetsXzIWXuJudg74V_EhpDbwuf3tmJtArMMvN2fhhQTOrg04y3hL8NTUlA61cb5cNLEbM0DSj9Htu4Roa9Y7pw5s_B0kbUh8x_x3y7TBWCQ93P8VEUM0-xnah5NKAeku2G2OriYm8hq7SuiBOCvdy45ZuCIZRrJWELrMNPdjGW3ch2l29bn_NJPaPmUI6hIA4Y5hWBcFQ5LO9WqnDwpQCMsnw96clePpya5d1QfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxqZkyvx5R_6KBW2vWF9Wqlk5URNm_NCry7KWHoYdfa4azdwTr3l-zKQxq1nBUzDyP_Q-g772Kblz5Fizb1v3MvHHWhUSDA2BlOuG-d3fERDkBpPWNBywGPAXkYR0XV5BMeWVwaxNv6YY-uFfdPseF8XnQa-pX0bXHMUZuE5UKO1CQ0Fo2RLb0pzInaiZCICq2_VNHt9jdJSh4aonCuIcqNU1BR3LinRrAy9t5Ahlum74uEVG4aP7Oadz4YSBsAlXl1PHzMQd36LdHofIUJt65eYZSzCei29HeIq2RitK3LvHa1UAMZA4KJS4ajgkFYTlQK0EYy2NuhLN1KjORPajg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۳۱ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/436975" target="_blank">📅 00:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436965">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjOEmA4SNPWzlL0Et0Idp6MmXFwSIsRe8BnURyMDyWhx6sx2JW6JQx_N8gukypQnRoRtYqoPYSab8OiAmpjfDbRZy4brszEPXVur-LS8HslKDhBiHwFQ6rMAUa_xH_D-kWqTQKv_x4ue8yqfe-9kjcLb0x8eT8xoB_ZazT62cxIn4Me4NYOeYvs359g5BriFRYZ92omJKNOrEZ4xyD8NgigS4PRfy_5izh_ZOIbVyuufkFTIceplL742NikfEAfIAs2WtPHlSQBW5iJpzgrls9YdlL01-zUMUuH_yfVssNKOPFPTYqSqpnwJwXH5ktlG2CbcEzn2wK6zNWtMMieNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zhhf5IhSEVL83gbiZOJtylu9bWFt1KUdWmqK0uMlIjlV1q7y--21xOGQukPR-nP8-bhLOxWZHHrejaIIuI4cVSPoBCVk8hXJhQ71c9xJkkPAT9mW4a0EGFlrKUK62bv37x83SI2HM7QD79rGNPTeSv__jI_FzuOcYExaimeXML_kz8Ss8NnW0AQCrwCSFQN4w6ro9dfQhEewE-sv79YjIBeLHjq37HQleHQJ-ZgChA9ltQZsL6MercKB8SEa_jKWBuj5OuRINHszUeIkQUdQ8cGxdk22uVxCll8t2iVu0baRYzIBg1EMqxNT4nvx0Bq1k8JfCYM3OY3ZqHHdI_1r_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVSkodWbBrE3euBd7_BdbGB4O8-5N20mN8pVA6zFdmgc8cFydu34nt4A_sXv6GfkJYZmt4Ppo7rs-sUbPUPWmsqn6XFJgRxwh1igNY3LfUEZ0CyI0xa0Dl-92SmRXWdLQt44z6SEynd5e961-HV_jh82n6Ldzr2K8uTzm_tYHxakNGfgqJ1qZaWVzi-XmCV1c90wiTDyZoi8ibcqh8Un-SdF3TIZ6Fn50G5icBc5s_O0fZ4ZYXW8yCi6M-qw64Gs9VkJhCHEWHPz64riDEEktiC8D6ffWza4_9qCpxTk9yg8I-070w7-ebX4eR_2MqJhSfxSoOWNLSJzE3oWHKuxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3XV06KT7r9GC70mctfHkBj6R8KVKcleb_VJ8C8BpgzVCAHHsU9DYKrymX71MH1BRAHdZzCOmyUqqg6T1AzXfHGgRZLRYo8u1qlS5pzLFXa31mZyu_TJcK5Q98zJVlL0mcV-9ZKYfDf7fQ_sZEHDaWRLtQVUSBL9vc2QA8BmMJvZI0RvPzCiUd8o4ON5iqGJlRYXeCcOhlaIUiRZVmNGj2GD0qRacCy1XPQ7Etj-yxFMnEZYQ3oqluQud-Wuko8BqZTQJU9hKKOSXCYo52qelIdivnq1tiDYua5bxEUufVf4McIkmPE-ozdPyLyV96RVqOnwqDAyrNSg9rULNE6aoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcA4eQ9S85lnG2wJVHJdI6DlVTXqc54sF56Tg2Dj6vj7b2V5lKMr7W1a8I1TU_uc6ZAJalwj_zDnPurlS_J55kC5BIJMryAmr_rwzyi22B1iA4PoWunSeg3fs0rgbhVb1Lxe4lomjdINVhu4EKthugNrgZHC3UJ-of-RbEinkagrBLC-Q2Uq70268_7TpPnsA__pk-zBnqyYUjWI0PkI9dyAOL5Sihahu0fmevh5aPV4yywzibX_PYuzSB1DKj7QvkF6ONdGWmVGwL7v3dCE8u-vjWKgN7Ndi5EZCDWxt1g7l0jFTe4-EaqZ0qB-7zOujmsODW9D7RFemOc91fKpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4YxJUvxOUv5W5zNvyD5D3SzR_nknHHRp4_kPxyyQs3xmzIF6zy_5sjLy8my-felxvqdAf2XpKUyV8wnqs0kBjVnX1rzwJiKsBg-dK8rCmUorxOz_tzRWfjX-GBw2WF0hhmMWDHy0JgZFAtRCErnhPM0JFOu2C3bl6zgY0qOGOOyMUTMjWZhnwuOg86NyW3XXAS64Bxm8ziZuCkD5v598xZvmRY7dfleqbNVXcVGZr2cMH7whu-HurLHqjZFQBNQqh7eIMY0DKCzCBSw77dhbDdHQViL8Dntf3w5IBEcFJoVlkCJRqFaG1_dg7W_TN_5saPpKoFeyQogENYfrQF9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQK5KhhaMfTs4RGVFuiUzKKabLEetB5Lhnh3ghaH7EkNvIZlUDZ4MGlCrTPs9ZdH7Kn8WKgjmxdat-EFAsGCbzR4W9lr4zRAuXhAeWo3h5F0huPpWyLUjWFJS2y9V-yWGOqkbFSn4QOK_VrNZ70XaQRHYjfhg0oKzrlRVJKJb8yNE_bgnikBLrnbhcXHZ5Ex1SVSM6Ii2f008QjrehhrXlTyJNM2IaIAa8cyMXBfFpBFw57QXvmmmWYTitfznuSI-ROhPOAzSkzrCyaP8DNEeeZsG6OSAI4QVCSf4BN6yoazZX6MROtz82ZaH5m8Zi7Yv5be-7rifL5SSkr2sp919Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVpf3_RicPqw3W590NoSKtrZhq-Ve1F16SJpqNL80BkpN2AMPijYaCTPu5Ke4WlLAjgQRDWnV0DsQ_ncif6RlUJ3RcSqzbpMW1LJx-AklUSqMCSPASSNDjLtjlqUjmni0UBPVX5UsE6GwUv8q3muUte8VxFvt4p96tEsk8fgw_uBqWjhz8jbuTGP0gMJXwKMsV6qIsNA47xogwOlB7tUMd_q52kjJG2aaEJ8O5jjIioyfZiCsTzFxULSxiUfJuy9s96_1YPy0NMrHtJe2yYPJHG5winDDw8M5n9Yfoo_kDlgmnDg9qYOL7xUh-piuNaGiE1RzQY5JgkWSPb_X8gqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwv79hzPjZ6QmRb_njIctUwIYpIXvtK-SdDBBR8ucy11chnvqlvT2nNQjfw8oJ9PgSlKU8HnM7p8W8lFubNJZPJNWGBobnrw2uq_htvgIh4u6TlnRF6WNcd6SU-uMikrmZn9XPR9A1Eg43hmOcClBBLmbLMoW0Se4RQ_MCNEOrkXNNIqq95iRVT--lF9sOUkmQI4QfuwvWlHPs5mpTo--_PON-LUrA9H7oMMkev_ywUvDwdnjfaeofTwAtYf6GuhTlV1P3NeV_6FZGbXx3HmKEDpZ5XZfvyOSvBs51Co-7jojALYnzVALLI_hG1ENV2MypdSLby9oEelEsFfplir1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEDiiHWJizrkGZJ_nMgQ8E1IwlqjSmMwUAjxuXIDkCvVA6nf-ykmyqBtSS0nVws7M6zMgLEXXrzypLTDc7Z3zw0aPvXsG15eDGd02YpjJOJZCDIW3w9PElhz9Juf-zWMfBCVbbGwqYoFhK5hkcSIlQEB-oJhdxwnfmTUTvpTNCS-0UDkrAEj0sFDfocjqdIkmEE2Ezke9XLxpZ5aovyh1B1x8QJBHxliHOgo4abfR85SN-_ndi_bZ9CXsyueAWH8ylMqaZ7q4sIZmYW-YXrLDpNr3S8pDOdxvwo5cG4JwC2qDcPq86jdMhHmjhlZee48m2l6KUlwWqktGgxo2uYg6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/436965" target="_blank">📅 00:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436964">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
حماسۀ ۸۱ دورودی‌ها به‌یاد شهید جمهور
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/436964" target="_blank">📅 00:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436963">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زاکانی: پشت سرمان بمباران بود اما ما به آسفالت کردن خیابان ادامه می‌دادیم
🔹
شهردار تهران در گفت‌وگوی ویژۀ خبری: در جنگ ۱۲ روزه، درحالی که مشغول آسفالت یک بزرگراه بودیم، پشت سر ما بمباران صورت می‌گرفت؛ اما ما کار خود را متوقف نکردیم.
🔹
آمریکا و دشمنان به دنبال…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/436963" target="_blank">📅 00:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436962">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ee60163b.mp4?token=ayqTncmMJ1rZbOzMOZ6XwYA4C6-0pFkB0cZdEzDlCLS9vMedxGgcPIK-tWYQzlljs4Y1f4Iz0s1R8MqhZGXnTmRG_YnTzCDtrJLzAz9d5P6NyTDgIymaW8rZdl8zt0f1JbMyBAr6g0YM5uwVAcnZf1JBY-pBth2aB6YlET0UciQvuYjbyKPGo4WFtXeBqMrztNJHIQklvu1U6ovPo5DrmrnkN2MeBZ6_kPCdTf4wmeivwLXMgyT0zFQIPG-gQqeR-wHeMXvdtmes4S2x8qx1CULGnm8csLRrQsrAQoQmM29MfrUJ8Z13xz9XLAExfeD_Wo5qC-hwNmkCAuJ5LQQtwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ee60163b.mp4?token=ayqTncmMJ1rZbOzMOZ6XwYA4C6-0pFkB0cZdEzDlCLS9vMedxGgcPIK-tWYQzlljs4Y1f4Iz0s1R8MqhZGXnTmRG_YnTzCDtrJLzAz9d5P6NyTDgIymaW8rZdl8zt0f1JbMyBAr6g0YM5uwVAcnZf1JBY-pBth2aB6YlET0UciQvuYjbyKPGo4WFtXeBqMrztNJHIQklvu1U6ovPo5DrmrnkN2MeBZ6_kPCdTf4wmeivwLXMgyT0zFQIPG-gQqeR-wHeMXvdtmes4S2x8qx1CULGnm8csLRrQsrAQoQmM29MfrUJ8Z13xz9XLAExfeD_Wo5qC-hwNmkCAuJ5LQQtwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعیت، مؤلفه قدرت تمدن‌ها
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/436962" target="_blank">📅 00:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436961">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زاکانی: پشت سرمان بمباران بود اما ما به آسفالت کردن خیابان ادامه می‌دادیم
🔹
شهردار تهران در گفت‌وگوی ویژۀ خبری: در جنگ ۱۲ روزه، درحالی که مشغول آسفالت یک بزرگراه بودیم، پشت سر ما بمباران صورت می‌گرفت؛ اما ما کار خود را متوقف نکردیم.
🔹
آمریکا و دشمنان به دنبال روایت یک کشور جنگ‌زده بودند، اما با تداوم کارهای روتین نشان دادیم که زندگی در تهران در جریان است.
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/436961" target="_blank">📅 00:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436960">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlyDTxEotbput4lZgnM9dgwo4Nv-MhidURY27aa7ycc--o9mzEDKqjysvC3KmaqVv0SNOmFFrpk1aIY40CJPVPloXQpthuQiIzJp6-ALoNb9GvXrEXWpiaEmj8YjUvhODGTZu8GmYFjaL0g6-78COYKBCYzdbX-Qn2Wp_e5w1O999kOaULAnYOykLhp3I0kwvT7-k-nffWH3IIjuAMxcZES-dWdEP4tQ1hgv1uDpSTtarCL9w4JsnwXXSs6o9ajWnMVr2Nuu1ozMOSFgfjMknVmd7AL9yGI_U_SBA02aAROVE9Yq7K0a2CJpmHA3Ir4ibvLmdfFt70TsZC4dP4lT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید رئیسی در کنار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/436960" target="_blank">📅 00:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436959">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b94098ad5.mp4?token=voOTz09TRgHmLOujIj34mCbHmDUgZX7bSrsnsZ3WxBZOq09MwXyhFzGAtCG6Tr9gs49VcrrTeJY56fzxIhbverCBjlUfw0rAe9X5PdDynEIrBWG5utD_nZCM_xAprhAMA0i81WC6866Ll6IrV6jIhyM9RwydPfyddpCZjJHranCng1aqorcwpYypgkw0RV51PE1SSEGQA8hH_ohpjNzAGIgTiAlXE2SlAoe5kGDwAjsVOEio44O90X-P_RPjM2zxGz6-Oo0UXAud1J_XN-wYGXsylLmZNW5UyrruXzGK3WFOtUiRPWkR8crYNYbC-1OHBpAMctmZjC0tanNdjGeUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b94098ad5.mp4?token=voOTz09TRgHmLOujIj34mCbHmDUgZX7bSrsnsZ3WxBZOq09MwXyhFzGAtCG6Tr9gs49VcrrTeJY56fzxIhbverCBjlUfw0rAe9X5PdDynEIrBWG5utD_nZCM_xAprhAMA0i81WC6866Ll6IrV6jIhyM9RwydPfyddpCZjJHranCng1aqorcwpYypgkw0RV51PE1SSEGQA8hH_ohpjNzAGIgTiAlXE2SlAoe5kGDwAjsVOEio44O90X-P_RPjM2zxGz6-Oo0UXAud1J_XN-wYGXsylLmZNW5UyrruXzGK3WFOtUiRPWkR8crYNYbC-1OHBpAMctmZjC0tanNdjGeUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدیۀ فرماندۀ هوافضا به مداحان میدان انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/436959" target="_blank">📅 00:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436958">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حمله به مقر گروه‌های ضدایرانی در شمال عراق
🔹
منابع عراقی از بلندشدن ستون‌های دود از مقر گروهک تروریستی کومله در استان سلیمانیۀ عراق پس از اصابت چندین فروند پهپاد خبر دادند.
🔹
پایگاه خبری «نایا» نیز از حملۀ موشکی به مقرهای گروه‌های کُرد ضدایرانی در استان اربیل گزارش داد.
🔹
همچنین این پایگاه خبری اعلام کرد مقر این گروه‌های تروریستی در منطقۀ بعشیقه در استان موصل نیز هدف حملۀ پهپادی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/436958" target="_blank">📅 00:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436957">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdcI_c9hhYGpPkipRpRJ1U3VPV0wACtpoeDZzbVW7wE3Xgf8DJkpk4CC_YPQ2zJTo-1ti1yLLHQDFg7b0s9qr22txiUCmsCI8nhRpLiqNaMu9Nr8GptE9AGjtwsLA5VgFmTmmPfYoyQVfPtAG3T7il9TFkqvyVnANQcGb57uxcOfJvAUxuhad5_Kk9-O02STfrIqvbdqF4G16niH4-uw7RI8Zw7d82ZcKeRevP22PzCu-nGIjvWdyy4kGXi5cLqFosbthJc0Tpfs9YHF_11-d_Je2AKSyYm5Tcj1BlbnSY8yLDPDrzkP4BYzZy_Z7SIJuuDeAbPuBT9_w3-3ClxHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌های خالیِ فاتحِ جهان
اسکندر در بستر مرگ، سردارانش را فراخواند و وصیت کرد که هنگام تشییع جنازه‌اش، این ۳ درخواست حتماً اجرا شوند:
🔸
درخواست اول: تابوت او را تنها پزشکانِ حاذق و برتر حمل کنند.
🔸
درخواست دوم: تمام طلا، جواهرات و ثروتی که در جنگ‌ها به دست آورده بود، در تمام مسیرِ منتهی به قبرستان بر روی زمین ریخته شود.
🔸
درخواست سوم: دستانِ او را از تابوت بیرون بگذارند تا در معرض دید همگان باشد و در هوا آویزان بماند.
سرداران با شگفتی دلیل این وصیت را پرسیدند و اسکندر چنین پاسخ داد:
🔸
۱. می‌خواهم مردم بدانند که پزشکان هر چقدر هم متبحر باشند، در برابرِ مرگ هیچ قدرتی ندارند.
🔸
۲. ثروت را بر زمین بریزید تا همگان ببینند که تمام این مال و اموال در دنیا باقی می‌ماند و ما حتی ذره‌ای از آن را نمی‌توانیم با خود به گور ببریم.
🔸
۳. دستانم را بیرون بگذارید تا جهانیان ببینند اسکندر که دنیا را فتح کرده بود، اکنون با دستان خالی از این جهان می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/436957" target="_blank">📅 00:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436956">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apcJSt8uPmA-tXc-x1bModSD8a8q9YPuebY8vteHdaz8QC6Xd0JA3NSFuBnxS1qF6SVLqM8wahZbE-NMyzql-t6gAcV4c8lvx3rnZ03I5_xL5JBDfJEQzexa38N2ZIi01uQWgQsfN2tU2dz_Zyw0P21OTWTnCDsvC1a4Cad95VuUPrtwsiNg4XZfJ_QNj6jSQwJpcCjAJsiNgdZZig__jCYLEOxUrYre_9xyxdR_Xat39gCHDJSX6RV5KQfQBIZJ4C5MnBWFg9eVNrCZHf-wzfHf3UdyEh4T2cAGHnglK22xZRqpXdHwbp4l2fqjdGSFGyK6rWAtdVgQMQp1pp_UXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس محدودهٔ نظارتی مدیریتی تنگهٔ هرمز را مشخص کرد
ايران محدودهٔ نظارتى مديریت تنگهٔ هرمز را به این شرح تعيین کرده است:
🔸
«خط اتصال كوه مبارک درايران و جنوب فجيره درامارات در شرق تنگه تا خط اتصال انتهاى جزيره قشم در ايران و ام‌القيوین امارات درغرب تنگه.»
🔸
تردد دراین محدوده برای عبور از تنگهٔ هرمز نیازمند هماهنگی با مدیریت آبراه خلیج فارس و مجوز این نهاد است.
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/436956" target="_blank">📅 23:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436955">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/160a5cb784.mp4?token=KLpBTpssEQ1fXRDH04PldR7l4UbHgYS2xTciz9fu4B8Qu-p694BY5OBrEtzLVYENSGSHEJ6VjLoTRU9dZM3crunwkDHcW-9_XYWsPKQFZ0RSeGYExFCPRGCrDR2cJyt_FLm5dB01h5Y805n_3SSxgoQyOaXJ1nmIywUcI0xSNAxFWKjE32c5wbYcc68Vsbf1kAlDWYrPfVMM7AIGP_YGKIOMLDUpB-SFJfXqnjvu5gBoWAl4mm_PSCQXwigPj7Vv8gA80XkMLzJ-8h-QYRCwfDhe7S44lCxSdVykJUpPJ1sdUytIu_1M7spfx0FzAGiKNwzzHvC58_OAaTj2z7o2QSVvRzd5V3bVAc43gtvnR8QAYlfDNOmv2UY9YVr3wCbHmIGku7eBAUIhDM6fynlhTrD0Xmj9cVv6yXe0QbXmb4Y5DSqI-yeRRiqOeT2z35dxqd0_IqKIFTONYo9oQ6yr75XZ4zSskcMMmprlII7GJJZMK7PQtzLI_5nxxjFtCWbnSTfqxVNI7EfCzvvXXAK7cX3bRxcnI6LX1wDAh6LZ09upPGPZHIHXUZ7z9ttjCby7DmtUF9E-4eiDyjYTLjahdTYC-w3JQ3G99JF6s9DamaJA4oxbJIbGBCgZ1BjnZR9jRpYeIqNEWUVOTx07E2sZMZFnqOcW0liIZ9wzenN3stE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/160a5cb784.mp4?token=KLpBTpssEQ1fXRDH04PldR7l4UbHgYS2xTciz9fu4B8Qu-p694BY5OBrEtzLVYENSGSHEJ6VjLoTRU9dZM3crunwkDHcW-9_XYWsPKQFZ0RSeGYExFCPRGCrDR2cJyt_FLm5dB01h5Y805n_3SSxgoQyOaXJ1nmIywUcI0xSNAxFWKjE32c5wbYcc68Vsbf1kAlDWYrPfVMM7AIGP_YGKIOMLDUpB-SFJfXqnjvu5gBoWAl4mm_PSCQXwigPj7Vv8gA80XkMLzJ-8h-QYRCwfDhe7S44lCxSdVykJUpPJ1sdUytIu_1M7spfx0FzAGiKNwzzHvC58_OAaTj2z7o2QSVvRzd5V3bVAc43gtvnR8QAYlfDNOmv2UY9YVr3wCbHmIGku7eBAUIhDM6fynlhTrD0Xmj9cVv6yXe0QbXmb4Y5DSqI-yeRRiqOeT2z35dxqd0_IqKIFTONYo9oQ6yr75XZ4zSskcMMmprlII7GJJZMK7PQtzLI_5nxxjFtCWbnSTfqxVNI7EfCzvvXXAK7cX3bRxcnI6LX1wDAh6LZ09upPGPZHIHXUZ7z9ttjCby7DmtUF9E-4eiDyjYTLjahdTYC-w3JQ3G99JF6s9DamaJA4oxbJIbGBCgZ1BjnZR9jRpYeIqNEWUVOTx07E2sZMZFnqOcW0liIZ9wzenN3stE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرکول به خانه بازگشت!
🔹
علیرضا یوسفی قهرمان وزنه‌برداری جهان امشب در ۸۱ شب از تجمعات مردمی به شهر خود قائمشهر بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/436955" target="_blank">📅 23:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436953">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN9eJ-MPla-gQi73Tw4nCLtl4OEhmPlr7Sc61XKUOk-VxwyYbwpo97AxsKAFskHDYT4NaSjekIllRJ6clYgtkfKKingHMm2Af6zy7v-LKXTLKVATMGK2EDP-Mf43U7xWK-oVN-oarmD0AKBtcbicpuj1TAIkwKYDT6dyMsFi_l9p-P8Qzjy6mG5zNFGoxI4EDc-JXNr-_TlUjZwj9XrgPNUTp1vP53IFSm3nUSMRZXTxvFBorRLNFbdjJ0R5PZ8gHZ9tbHxiEALdCgOGPV74jH7WSbxcliDIntRHyysmonpM69zn5yMnIZ5rqb36Xm_EW9_KD9RN6wnTCUe2WIVeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  اسپانیا، کانادا و هلند هم سفیر اسرائیل را احضار کردند
🔹
وزارت امور خارجۀ اسپانیا ضمن احضار کاردار اسرائیل گفت: «آنچه بر سر اعضای ناوگان آزادی به دست اسرائیل آمد، وحشیانه است و ما خواستار عذرخواهی رسمی اسرائیل هستیم.»
🔹
وزیر خارجۀ کانادا نیز از احضار سفیر…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/436953" target="_blank">📅 23:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436952">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d616ec2a.mp4?token=JuQBi9lhqN4EjWofzIFpWsZcIZYgnNlVpHg88BGC5Fh4Y3Pb5jlof6XtuhlsUF2AtsVBKrhoVPz3cuEpYpTIV9Bd26GKsOirJz63MwF9F3qYAlaz0dBO-Y9dJHX10MKS0vHX1q_Auvc4BrPEO3ARz9dNMIjdX-Qjaub3m4tJTfou-FS_KdB8nzn1NGDV9C5Z8-VFhOpbN0IPYlqEfFNAqdyOvDywNtmOHAcn7Of7pSM4E9NBOODqVmFJndan0pu6cDdUiRYEFajQTgQ2-6PPBRMo8HDKxjblULZX1n-SI0QTtdtAro3CFLrebepxj_Gf7AHhPInKgcD9xbP3xM4_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d616ec2a.mp4?token=JuQBi9lhqN4EjWofzIFpWsZcIZYgnNlVpHg88BGC5Fh4Y3Pb5jlof6XtuhlsUF2AtsVBKrhoVPz3cuEpYpTIV9Bd26GKsOirJz63MwF9F3qYAlaz0dBO-Y9dJHX10MKS0vHX1q_Auvc4BrPEO3ARz9dNMIjdX-Qjaub3m4tJTfou-FS_KdB8nzn1NGDV9C5Z8-VFhOpbN0IPYlqEfFNAqdyOvDywNtmOHAcn7Of7pSM4E9NBOODqVmFJndan0pu6cDdUiRYEFajQTgQ2-6PPBRMo8HDKxjblULZX1n-SI0QTtdtAro3CFLrebepxj_Gf7AHhPInKgcD9xbP3xM4_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همخوانی مردم میدان انقلاب در سالروز شهادت رئیس‌جمور شهید آیت‌الله رئیسی
🔸
چون شهیدِ جمهور، سرباز دین خدایم، من هم خادم‌الرضایم
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/436952" target="_blank">📅 23:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436951">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0ccbd1e2.mp4?token=BvJ6OLFWgiCTUKZXOGc2Gj30arDuB3JWnYhJPv2-HN1neIcX8ddXfyTNeLa4EJkwMVXihLjrIZwSCQYAdPUxHDkt36BlP7b1yDnu_I9NNf8mmF338AhjufC0YTsOMVM3TGTs-yox9Q87gLBZKEVtDgWq3scfZFYs487Ba7sXSN-Vxelgmjv8tFITonNouvH80OhBzqajyScrcc-k-yQvGdrA-XFu7n6aR3rApRRS5UDN2jC3j69kZmu6ThuWiRZszsGzafxz1x0JZ9d2eEB8s_E0XoA7jGZeWkuDpVhsEfUeFFX4P5MlYNJkXhYehK9eeCgifiClacKpYSGhiKZSnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0ccbd1e2.mp4?token=BvJ6OLFWgiCTUKZXOGc2Gj30arDuB3JWnYhJPv2-HN1neIcX8ddXfyTNeLa4EJkwMVXihLjrIZwSCQYAdPUxHDkt36BlP7b1yDnu_I9NNf8mmF338AhjufC0YTsOMVM3TGTs-yox9Q87gLBZKEVtDgWq3scfZFYs487Ba7sXSN-Vxelgmjv8tFITonNouvH80OhBzqajyScrcc-k-yQvGdrA-XFu7n6aR3rApRRS5UDN2jC3j69kZmu6ThuWiRZszsGzafxz1x0JZ9d2eEB8s_E0XoA7jGZeWkuDpVhsEfUeFFX4P5MlYNJkXhYehK9eeCgifiClacKpYSGhiKZSnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان‌فدا وارد مرحلهٔ جدیدی می‌شود
🔹
جان‌فدایان ایران، جهت تکمیل اطلاعات و انتخاب نقش و مسئولیت در کارهای مهم کشور، عدد ۲ را به ۳۰۰۰۱۱۵۵ ارسال نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436951" target="_blank">📅 23:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436950">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شهادت یک پلیس در سراوانِ سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان: ساعتی پیش، سرنشینان مسلح یک دستگاه خودروی سواری به سمت خادمان امنیت در یکی از جاده‌های شهرستان سراوان تیراندازی کردند که متأسفانه ستوان سوم امیرحسین شهرکی به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/436950" target="_blank">📅 23:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436949">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">احتمال اصلاح برنامهٔ توسعه و بودجه ۱۴۰۵
🔹
رئیس کمیسیون زیربنایی مجمع تشخیص: باتوجه‌به شرایط جنگ در راستای اصلاح برنامه ۵ ‌ساله و بودجه ۱۴۰۵ بررسی‌هایی انجام و پیشنهادهایی آماده شده است.
🔹
همچنین جلساتی برای تهیه پیشنهادها جهت تدوین پیش‌نویس سیاست‌های کلی پساجنگ برای بازسازی و اصلاح برنامه‌ها برگزار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/436949" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436948">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0PG1ZXHX-o6KlsTiP4ESW4XiJiPmQWrHM-rjAsgQw5Fq1qCaJvGMvA67EkxK0OlrbsrITMCJmYXuxIIobohxWHuyaEqbfN6kvF915HuGQV5hhjhWvNatlJTThohHfwRcAKo7af5XEYhpL7lzEZkyabP7Eg2j0jMxuCC7fCGCFJ64I2GbfR9y6DmcN0bcFwY_RMzLLmyeqCkOH0XmSESuQNVRXWjckI-opEfuRAYHc0Ajlpdki_oUqlQiD-FAOeatdOMpv237_Vip0N1_cTkY1w_ObZoU7PWd6BiwzZEPANTRXSA83TC6kgptClhgniGNO5Zoznz0p8wXYdfunsVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد تمدید خودکار قراردادهای اجاره‌خانه روی میز سران قوا
🔹
وزیر راه‌و‌شهرسازی: پیش‌نویس مصوبه‌ای شامل تعیین سقف برای افزایش اجاره‌خانه‌ها و تمدید خودکار قراردادها تهیه و به نشست سران ۳ قوه ارسال شده است که در صورت تصویب، بلافاصله ابلاغ و اجرایی خواهد شد.
🔹
تعیین نرخ دقیق در استان‌های مختلف برعهده شورای مسکن استان‌ها خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/436948" target="_blank">📅 23:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436947">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
هنوز چراغ حضور مردم جهرم خاموش نشده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/436947" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436946">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
ارتش اسرائیل: ۷ نظامی ما ازجمله ۲ افسر و ۵ سرباز در اثر حمله پهپادی حزب‌الله به‌شدت زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/436946" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436945">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzsRr8PIODU7Cj7rJSRfUhXMcxY449oXSZqe2jycl9zEta2XMnKF4wNpmT_JbPl4qvZ7xI_iWrRjgvG-q1H_MrN3FOXIOy8qI7rpVLyRPHiQhYX3If8X1YcshVPcq3-dUCSTSlrO7P3rgOmvjb8i1jZPhtva0YugE-YFDH1GnMZBtX3Uf1aMWiK4b8dsgvBhN8qTCjn8YVJZRkN2g0Vx8RK7FMsCrGj8IE1q92Rm45jhYzrD9KDVB8mhiKBmjw-sPgjP8DYvRuQNm1ABWIiGer8pi5U_FAd0D6wC_S_l0Qbm1g0PI09ZqFSsjPh8d3J8PZ4vSX-xWjRj-764qk7otA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیات برنامۀ تیم ملی در ترکیه و سفر به آمریکا
🔹
نبی، مدیر تیم ملی: ۸ خرداد در ترکیه با گامبیا بازی داریم و یک دیدار دیگر نیز برای ۱۴ خرداد برنامه‌ریزی کرده‌ایم که تا چند روز دیگر بازی با این تیم خوب هم قطعی می‌شود‌.
🔹
تیم ملی ۱۵ خرداد عازم کمپ خود در آریزونا…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/436945" target="_blank">📅 22:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436944">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c21b8367.mp4?token=Kw7uxuTvUak_o2xnzHtzm4mo7G4zRKid6xT8i3SaoDljAo_S8t2wIzMM3HWyTyO09Qm0_wt5MsBOPW0cr8SadDC_0yot0dYo3jHsprTJUILHTije6gnBpJDs5icChcs1-7t9SlGvh9BshfeK8mIDyMjxhccgRaYMefq-8rli2lfzru0059ACssCLYpsuFO9W0IaDlfNjowjBVDZEYchoFYKsqN7TfA-G4qWw5FbLmO4OD5Wp-VwP7ScOU41OC3bE_pLUibRpvWnFEOyvi_3jbnIs_PlBsGwwn8zH5HBIE-bjhlUl-QhTYJ14wNGKQAeKRf4xZirxoZQ7FHlBXBXvYld9mE7hpAbzFC0XQI5CtwAG99mpkoyOiwpTIl_vp_9aOvpJrCQVARVMOmiY_26m3W0drrW-v81vfX-cbcIB0lkRoCLxGfd-sXYx_qDKYbVAgZ7AGIoJINY9BL9NvG1ETShfjMl7Xn1JUeLUDqRT8Vhm3rfR7lBTd0BSoPxtGLPZUPhy6_uSXrYkhTCWLWj30ApIw-di01sQRR7qBPkv5XEgMIu0705YG8_GoFOfa5fCYCrjgQ6sgwtNuMvhpVB7mE7fMgIHJ8Bz5h-87M_LiBWKW4V9RPfA9UnX-gIs1GjcjzKPFDKl2P_JIuljQgqAEZM1XCClcx_825Tj00RjI40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c21b8367.mp4?token=Kw7uxuTvUak_o2xnzHtzm4mo7G4zRKid6xT8i3SaoDljAo_S8t2wIzMM3HWyTyO09Qm0_wt5MsBOPW0cr8SadDC_0yot0dYo3jHsprTJUILHTije6gnBpJDs5icChcs1-7t9SlGvh9BshfeK8mIDyMjxhccgRaYMefq-8rli2lfzru0059ACssCLYpsuFO9W0IaDlfNjowjBVDZEYchoFYKsqN7TfA-G4qWw5FbLmO4OD5Wp-VwP7ScOU41OC3bE_pLUibRpvWnFEOyvi_3jbnIs_PlBsGwwn8zH5HBIE-bjhlUl-QhTYJ14wNGKQAeKRf4xZirxoZQ7FHlBXBXvYld9mE7hpAbzFC0XQI5CtwAG99mpkoyOiwpTIl_vp_9aOvpJrCQVARVMOmiY_26m3W0drrW-v81vfX-cbcIB0lkRoCLxGfd-sXYx_qDKYbVAgZ7AGIoJINY9BL9NvG1ETShfjMl7Xn1JUeLUDqRT8Vhm3rfR7lBTd0BSoPxtGLPZUPhy6_uSXrYkhTCWLWj30ApIw-di01sQRR7qBPkv5XEgMIu0705YG8_GoFOfa5fCYCrjgQ6sgwtNuMvhpVB7mE7fMgIHJ8Bz5h-87M_LiBWKW4V9RPfA9UnX-gIs1GjcjzKPFDKl2P_JIuljQgqAEZM1XCClcx_825Tj00RjI40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولاک دهه‌نودی‌های کرمانی در بیعت با رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/436944" target="_blank">📅 22:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPPdOph8q3ETCmPv6ZTMj8hZ54OkJD9NIWmMl_kaUDAvWWNh9ItWV5RidUoIdsgmQWhh1PcjTnN5FK7aaq0YSS-fXUMBfMh9kXJoXPdjEKB79IGPRaYHp0M49B2Z7ZrJglZlempbp-LzgR7IrvKE3AuNsq8EwmqI9MT3cdmrsCjAFg_apqWKKt-hXSw9cY-tEaAyGHzzFs3K3zcwUFPYOp6QLZMwK-y6CyCc9HqJ4jSh1vUZOOz8jJRsYPJmB9u-YHHfEmdjxauFlLPsNByShQKWww5l2k-hw7BCTpi0SigDPj5xXz8Qf7cDIkpqoNNCeGNw6s0oHpBYm9BZvxkC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: پیروزی‌های ناوگان صمود ادامه دارد
🔹
دیوارهای تزویر آزادی‌های تمدن غرب را  فروریخت و فاشیست صهیونیست را بیش‌از‌پیش رسوا ساخت.
🔹
فلسطین را باز به کانون توجه جهانیان بازگرداند.
🔹
رژیم صهیونیستی مغلوب را که به تشدید سرکوب و جنایاتگری دست زده، سریع‌تر از قبل به نقطه پایان نزدیک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/436942" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-fMp709wz2M-XIfstPr8JcG3PJdUdLlkgPV5rT5i4XqD40kApC4NY3ckGVM3JSUp9Gi376fljZqHNZvv4yXutXCeF0OoofY3OEC5y_pz2NQ0AA5mf3RWt-dUVg6u2Z1uHH2ZU91mwECfuJ0f8bAYPsC5jDfhZgvfFiiSv9trPY-qF58UYFDSxYlX_h5NSvv_rbN0KwFaenXHOSOraDQFXcIUs3Day-MPjpIJAqnTnnS08MVaJTDLU1qdX4fgTKKhJMhhEZTcV7EqwHu25nzxjeiSGOb0mGeNgWfPBELPzTDz2L9jCVqE2w-itaXDFZvTgE5QozbS191WYPMg9J6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmdPDLktL20t39X7nYHZSeNarMtunvV6zI7I2yA6Tt0-lOVfiqu7UysWd9Hrn8Gw5EpUCce-2UABflPuxLkEgiVk7DgH9hACnaNBl8BZdgxNljs5apzl44uaEb7hm0HSAcsAB6o0iAirYKGPIaCFmlzTDMiBBPo-LgwXNFWguRDCHsDjEMrkgxFg9LTm4XYXECueHYsT5V7nUJSX19Z3TgQVKJ0tidqT9BByVDmN_xD3pSHvb4QcLoCFIFpjs0VAu1E-Qu96VdixydMAjmCLmZ9RIUxPTWN0fAJFQ8dBp3FWmXhQiSlNwB2tV1Kka53yxLXlrlu8VaFBlXV0fh0UKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPZzI7pnHnLJEqxgFDXJD67SagMIyTnnECx9Eytt94yDJcXcdmb3HY6J5YzQ9TkuTKYzfex2oX3dTwS2gzefQcEGdoyc3peFZg2NqtJJmOoOCJMLw4Ufhg7R0wPY6FTHydfVyRjR4eMzqbt6FSAkZsjMIutfCSqKREI6ciuKCYOFQtrC6Npjwq9MdMUTEp7q0zMR9-rn0KsI7_1B4o1ki-beR7UqlIB_-g0bv1mHQ17q7ApW0pjPhBFRtXeggodZ5ybFFto96RVkvyuCqjZXQ6GGf2-YNwdPFz1TtwHgkjTzahrjmwKMmXhNEyQteThDxRKXYwTifRBC_WKjZJTWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jbuebz_1s5pznjLg0jwN2PYkbnK24X4TPM9ie1_24ppO5IUi2n2_1lLJayxshf52NMwFFtHZYbrbL89jS9YVbns1aXmTPySQE1ARIkFCs56FEzytUSbGtLWskY2RMnBoIR8J4CEiUkyzS1KvF4DxErusXOWCGInFo9gCTiswGRGAXbDeKHOy2t1Q4n4jnL4GQKKB0erNARW9iC3N0D_YqC3XE4OGR9_kRcWaYyDhwKwgh9MCo5S603MXRJlabzQ78WhLytwzcQk9I8lPdfhnMfYm5cI0Q1auEC1UY36nAFTlQKH5_fgeUj_BFaABO_hA04Q9zTxZQJ43YFrDRkC2Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شیراز در حصار ریزگردها
🔹
با ورود سامانه گردوغبار به استان فارس، امروز وضعیت شاخص آلودگی هوای شیراز با ثبت عدد ۴۵۰ در وضعیت خطرناک قرار گرفت.
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/436938" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
خاطراتی از عزیز مردم
🔸
فرزند شهید آل‌هاشم از پدر خود می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436937" target="_blank">📅 22:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436936">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8o7-2OsaaSALYFEZtUbqG8uEVWc15LOKs7hzQPl3E9VRhWxqGZ_Z4WVLXcPDGm3fVJDXY08nzol8Gy0V1yTbveW7jw1gqr5GW9pgbg1t7HZhxFq-ERpyIKFdcY1lYXPFW4IynXK3mjuPs6RwWbJEuBv3HwxoYXXXYUOqlAHUHMO4uKNq1OEuscdNgVb58Eht853orm2y7SUkraNubkBsM7M4pMI6mqYDXd4A13PdrbwIFgBQ8RF7Wqq5fc_9x5jRVjtjX1NKnfPyVNbNMEQ1XLXoUWNhhq34S5nIhJg6ToK84ceQMWirkWyoy0jH7Rrh51xq1hqHTajexHCm3a_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: به تسلیم واداشتن ایران از طریق زور توهمی بیش نیست
🔹
ایران همواره بر تمام عهدهایش پایبند بوده و تمام راه‌های پرهیز از جنگ را هم آزموده. همه راه‌ها از طرف ایران باز است. به تسلیم واداشتن ایران از طریق زور توهمی بیش نیست.
🔹
دیپلماسیِ مبتنی بر احترام متقابل، کم‌هزینه‌تر، عاقلانه‌تر و ماندگارتر از جنگ است که ایران سال‌ها بر آن تاکید دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/436936" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436935">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎥
شب ۸۱ اعلام وفاداری آبیکی‌ها به ایران اسلامی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/436935" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436934">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40641a8da3.mp4?token=ts6kcIiMpSEUrLPsSnJhvxgfgwoo5kmnAfH0w286cZx2VoqKqpFKkU7STGYiurvpSJPpcNYfdY93iHrvVyKcQ27dcUKAGD0-tgBnQd88QyjCtI06Dyx8Dbp-yBatldJ1xS1q-vma8YqJR-VUZntWskfZxGpw_vgWuLG7XrTk3yGnrQU2-aF40CW3rjhBn6IubvlPaEPofPj47345cxPQGr4alZWnYcBQS81LZZa21fXFhipCPioCLAGQNelYhacnU6WVpGBdtJ1q82LpTSYxH8ckIWeQE-MIqHkEcV6Qhx2PpTPE3WGtk75LBkMXaA9Qr70Jf8Zp5KGKueUmykVUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40641a8da3.mp4?token=ts6kcIiMpSEUrLPsSnJhvxgfgwoo5kmnAfH0w286cZx2VoqKqpFKkU7STGYiurvpSJPpcNYfdY93iHrvVyKcQ27dcUKAGD0-tgBnQd88QyjCtI06Dyx8Dbp-yBatldJ1xS1q-vma8YqJR-VUZntWskfZxGpw_vgWuLG7XrTk3yGnrQU2-aF40CW3rjhBn6IubvlPaEPofPj47345cxPQGr4alZWnYcBQS81LZZa21fXFhipCPioCLAGQNelYhacnU6WVpGBdtJ1q82LpTSYxH8ckIWeQE-MIqHkEcV6Qhx2PpTPE3WGtk75LBkMXaA9Qr70Jf8Zp5KGKueUmykVUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
وزیر خارجۀ عربستان از ترامپ تشکر کرد
🔹
فیصل بن فرحان: عربستان سعودی از تصمیم ترامپ برای دادن فرصت به دیپلماسی جهت دستیابی به توافقی قابل قبول قدردانی می‌کند؛ توافقی که به جنگ پایان دهد، امنیت و آزادی کشتیرانی در تنگهٔ هرمز را به وضعیت پیش از ۲۸ فوریه ۲۰۲۶…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436934" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436933">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b238b716.mp4?token=ZdFB-XLGq0eImpoONyeN3uW_G7YzzHzLyaRVuWFdgVaW163wiAwfJAjtsGNRhlnfP9w6Cfnpet4s7YhY2cqKqGjS2HShnB8lGGEckq6w72ybjgVO82IXqpgwnG46r_ZL3SkNnT9qvwYn41AgLOS4ONiHogM_UNW0RLAaoIB-EvKhIyI3DzzzOyuIw6bywE7NXJQZs6mOAQYHzJIpliezNH0-a8UC7bI4qRzkESkTh1PtAeXb0M_krKgtyfrWmthsI5cIp7Q_81HLK9TvO6eRgBDum-kIlx6X9QGtb0tJ5MGhc696tsBZ_5a958nyrkej2JJF_kH1naFgbIvrtVGDUooqlsBGLAdMcWamQxV3QcV7Yp9zBrhHX3u5p9LG6n7yo25WgksQRww5vi25EYfHUTrUy_wsR4vdZ2ggqNqBLPBrBEZ3HmZUmBqhIu11Xa7JFl4MQUHqw1tJz5HSL-ewvGkQpPvsqA2dYFTpA4HfBqRu6RvWfXfIlL1m61sqz-Sfe03LiLKa9ymOzPgi1RWGT4AHzs0F_6rYNb9hO-pOXnxW8UlqgS5EGNUOJBP8puXoi0BmT5jLTndCzyuBSex-kV13Jhlsnnfzr2wSdCyrpmZf0LAirPr0YGtVcSC5TtDPaGWHqEFHV_cdqEpHk7CSzsn_f88TuVBLz8zCu1UjD0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b238b716.mp4?token=ZdFB-XLGq0eImpoONyeN3uW_G7YzzHzLyaRVuWFdgVaW163wiAwfJAjtsGNRhlnfP9w6Cfnpet4s7YhY2cqKqGjS2HShnB8lGGEckq6w72ybjgVO82IXqpgwnG46r_ZL3SkNnT9qvwYn41AgLOS4ONiHogM_UNW0RLAaoIB-EvKhIyI3DzzzOyuIw6bywE7NXJQZs6mOAQYHzJIpliezNH0-a8UC7bI4qRzkESkTh1PtAeXb0M_krKgtyfrWmthsI5cIp7Q_81HLK9TvO6eRgBDum-kIlx6X9QGtb0tJ5MGhc696tsBZ_5a958nyrkej2JJF_kH1naFgbIvrtVGDUooqlsBGLAdMcWamQxV3QcV7Yp9zBrhHX3u5p9LG6n7yo25WgksQRww5vi25EYfHUTrUy_wsR4vdZ2ggqNqBLPBrBEZ3HmZUmBqhIu11Xa7JFl4MQUHqw1tJz5HSL-ewvGkQpPvsqA2dYFTpA4HfBqRu6RvWfXfIlL1m61sqz-Sfe03LiLKa9ymOzPgi1RWGT4AHzs0F_6rYNb9hO-pOXnxW8UlqgS5EGNUOJBP8puXoi0BmT5jLTndCzyuBSex-kV13Jhlsnnfzr2wSdCyrpmZf0LAirPr0YGtVcSC5TtDPaGWHqEFHV_cdqEpHk7CSzsn_f88TuVBLz8zCu1UjD0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۸۱ و تداوم حضور پرشکوه گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436933" target="_blank">📅 22:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436932">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599fbd495f.mp4?token=HCk7LUPzXMZfdCcXiCORX5MvmVZQyEhIn6K4yueFFhQ9DQvnLVr568skkzFpOAhL5HtiHCc5hoe2KRtZulfK2TGv13RgxCRL5vcpJJQjHZHicpKazacOaCQ3Rzf6_uh4pXfeyq1T93yjNrJnC8LlmWJ2yM1Cfy6xMm_pX7ngOr59W_m-DNUl2z3-ALRtwUiJ1ARmrxtlQI6ikb5MsDx-TsJmyhcVeQc_g_iu8gYzm24YuVPeLDyswTMK4Cdbua1Hy6b5B2P8PFEquwDjYNmA1nRID5K1wtdO5PvfklrEuQQtLFfHQTZDkv7JeLY7A7_d8YRZxrwY_QeQ-oaArYkRHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599fbd495f.mp4?token=HCk7LUPzXMZfdCcXiCORX5MvmVZQyEhIn6K4yueFFhQ9DQvnLVr568skkzFpOAhL5HtiHCc5hoe2KRtZulfK2TGv13RgxCRL5vcpJJQjHZHicpKazacOaCQ3Rzf6_uh4pXfeyq1T93yjNrJnC8LlmWJ2yM1Cfy6xMm_pX7ngOr59W_m-DNUl2z3-ALRtwUiJ1ARmrxtlQI6ikb5MsDx-TsJmyhcVeQc_g_iu8gYzm24YuVPeLDyswTMK4Cdbua1Hy6b5B2P8PFEquwDjYNmA1nRID5K1wtdO5PvfklrEuQQtLFfHQTZDkv7JeLY7A7_d8YRZxrwY_QeQ-oaArYkRHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد شهید جمهور در هشتادویکمین اجتماع اقتدار کوهبنان در استان کرمان
@Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/436932" target="_blank">📅 22:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436931">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a44ad4f2e.mp4?token=e9PTYJtkr0hQYYwrTsE59dvt64rJifTV-IGHuQx15-UrsHuJLF6F2qH8eH67ssCeKhQuXLc8p9E18nJSM2bJpm8NKgiKdpL7r9l6EITRcN_9Zd6t0tYBvsL_ECfFDvkElFekpwv-4OpoA3jGW1zFr7xodRkMg_drJ-hsDkR3K9ITTziHTvkYR6CBSAXHB81JsnTUbzUMGLQTdAqFNmsaxIiOwouOVFK8XCX6JyW5YslLdIEvKo3nxnuGHYHK0JdUE-Iiz2rPYbK5eVpa3klIheQ2tRvhGO979hAgiGwRA1cq_09s4Mr0Lod0n6IfiGtb-ELdKxccKuQFh8fsP2Kdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a44ad4f2e.mp4?token=e9PTYJtkr0hQYYwrTsE59dvt64rJifTV-IGHuQx15-UrsHuJLF6F2qH8eH67ssCeKhQuXLc8p9E18nJSM2bJpm8NKgiKdpL7r9l6EITRcN_9Zd6t0tYBvsL_ECfFDvkElFekpwv-4OpoA3jGW1zFr7xodRkMg_drJ-hsDkR3K9ITTziHTvkYR6CBSAXHB81JsnTUbzUMGLQTdAqFNmsaxIiOwouOVFK8XCX6JyW5YslLdIEvKo3nxnuGHYHK0JdUE-Iiz2rPYbK5eVpa3klIheQ2tRvhGO979hAgiGwRA1cq_09s4Mr0Lod0n6IfiGtb-ELdKxccKuQFh8fsP2Kdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت روزبه چشمی در تمرین امروز تیم‌ملی فوتبال
🔹
طبق برآوردهای ابتدایی مصدومیت کاپیتان استقلال از ناحیه همسترینگ پای چپ است و او به‌زودی برای تشخیص دقیق میزان آسیب‌دیدگی خود باید ام‌ار‌آی بدهد.
🔹
بااین‌وجود باید دید پس از اعلام جواب ام‌آر‌آی، این بازیکن چه‌قدر برای حضور در جام جهانی شانس دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/436931" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
