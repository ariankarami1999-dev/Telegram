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
<img src="https://cdn4.telesco.pe/file/dxjWttm1eoD7zvH2Mb2Uw7FZ-8PkdNfpiViSv_GRNxSYrbP3suAn01wluDKPcu7rJ0hGvSwteZGH1xjXW1Kfm-2QI4q00AN9vUC-MItuVyXFhda0DE59wXlQwG1IHHMy3NDWdfwRFfBacrr6mxrQCGcy8jcjxURnFqZBdRlQ9EZcrl57kYXveMEkGne0mSAmR-Z0EnryxOGI8ti4GBLUK1CeUv-kuwnPQIznEU3WqLjsnh3BU_LR5EG9x1oKN0yIm6fma-vSDmfDR__fSOfFIg3BqCKTsju9tuk39dnvcKqdKNNWLCBdIJy6wWfqSY4LYtHRhzR7KUl8OR-tbUOUdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 621K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 17:53:49</div>
<hr>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7il336NRPpXbyHYYBpkWOJz2FB0RUzPyF50hQo-fyNlgHYX9qUZftBarh6tHhYQBq2vERuWP-Ne2abCYWcqyxgtvGXd3TuspKHT_NgmhDF9NENelFXTeX9uILUmUW1W3VRg2H30ubvqsqhivbCLeQ2qpjKDfKwrprAcx03PwkTrnbfjNH_uZSmt9NG2vkZkBH14Bs6E5gloLGQDLFUIEwuzbkzYFo3XbGeZzwf-xdPlc1rlEaGkqlbXnER-10x1hE3MnZz5sjekcuXh4oPAlptVmAMePyvWyQDKdJx39UiRkzPPZyRs6wo0TDHc8Zlu5YhsIuCwztLyy5QzPcz-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=aTMEICLJtDH9DFbAvBCrRwQY6yFuoUkar3RM6LsZM3fYtF_bEwVaxG8eUuhAA92lfY8s5_0jD3xTVLtCd3yOASl1oho6sN08LDWUrDdVzyI4SuRFDQ-k5ISKB9VOwYAMYsFRGrCtz5Pd0OIFMW6Qh6qKeiXzTdK21Z9uqoPKLHDrIaWP-VLa9iEOffkqKEiSgznKpaaQQCZ0mJv3gtH050rUFTvZJPtxEdwIrR7ckEbJudA-HB7cFUlZuIbS6uIp2A6tFfzDVBHmeCv2xjWG6SrX1PbXnh_lYhXRQPN8v1dyi_3Y-Iwsm3Fv63hQBOKnThrtlzHHyrj7VuC7c88lpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=aTMEICLJtDH9DFbAvBCrRwQY6yFuoUkar3RM6LsZM3fYtF_bEwVaxG8eUuhAA92lfY8s5_0jD3xTVLtCd3yOASl1oho6sN08LDWUrDdVzyI4SuRFDQ-k5ISKB9VOwYAMYsFRGrCtz5Pd0OIFMW6Qh6qKeiXzTdK21Z9uqoPKLHDrIaWP-VLa9iEOffkqKEiSgznKpaaQQCZ0mJv3gtH050rUFTvZJPtxEdwIrR7ckEbJudA-HB7cFUlZuIbS6uIp2A6tFfzDVBHmeCv2xjWG6SrX1PbXnh_lYhXRQPN8v1dyi_3Y-Iwsm3Fv63hQBOKnThrtlzHHyrj7VuC7c88lpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWMqrd7NjMuoNTynUp7lxBNWN7HwdAU2OPamPfZJyjBOreBKXOoVqcu_YmvvbwF5VHvkFbnn6CXtCrXuxApc-QPb6SHLh-vWZAMPxo79bhPJ1aY3C4JKIcUee5297DPvofAUxaj5N5vfQWtVyap6MGoA0OJwEtLWsrkXYiKMDY5qNlQFpEDOYbZdIp3n-cJmrNTM0o09fz9QZDxhbDOUy9mRGlFWru_FXjCJoJ3VTYw6UZdp1aCIAOHp0XGnHVaTtzJmvOcWbSg9qvSihH6kbqHlmUlIL6kgHaBYikIAeEDbCJzA6tY3FtSynSgojgLUJacfbxPBH7q55ZSsMkZEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suQ3-q0Qx8xJ0qBMWZUzTPjQkXBe_XT1pPtS2buayryq9YbJnWcCDj3oPq6jiObc4F_hS-e_5j38te8aO-Rg9GrJWQ-obDjY6VWXoq8pi0OpRpSELcp9jPSwm-LaNGy5xUUu7cP1seL-iXv2LraQAzqlo7U25MZBE6bcsMVBtPEVx2DMMFImw2DYdkELL8TxtLaTwU2vfUPUr6gyRajHHRvuepXKtWsjx-PA3X4vBf3lIQA8vKyC09zh_sU5aq7uejH7l5tB-3gXM8Sfx0iLTSWyjUylTszp6e7LZhE_7XV_7Wk04oPzEqr0D9rnPmx4IhpwcFC7u9jXGl9t2qD1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb60syzutHYf_LIFRRNfrYosUkQMjUOdGygNQzooXjJjSwtk_z-HLetduX9SwcYHQS7_yFmhrtGY63oSZf_twGgvrmkzC-CLmpD4Op4NgOrL-ecDummP4zT98HWtMV7cvO6qPg7wBy8lclZMKGGLPD1SEtHEuH8NpFyGAzL7jYviPE-2t97U4Qd538ej9J_ymFJep-FM-1yIPwAoFSs-FiuZ7260u7q3ST6xUROwEUwpUCJc7-Ro-eBIyAeX0k_RVX7G3ZYR9eSgLo92XUCPmaie_-wyEOPKAX4Kpt-YtRwoGTXCziNtRRD_99aLJ6ioPN4a8-V99EdOCZl-TdwBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlmPw9jeHSLC-WcaYBm19hmevwkjdXY8qkGX_Y3i9o-HL6vPXBBHHVxGi7sLHXuzUK9vzK8qQbbXGdHiXbZoK4Y9aZYy3gfk-RdycjzUgMjzRpnqZUGuO-UZa9IiBQ0MBPnT6fwgoDqrq2X64KpQmMMhUZ8rBzjagxHuunBMcUMMLDJ8YJd8tTDBZApJcukDOsWCZ1GyM3DzW1t_NlixHZgPgZY0rz6oUpADsxOiXs-jHbMIGHtDldO4UTvsygWLTzdG9_59pOTM8Kxn-Cm7Hdghr0f0blAaw6m4KTcasp1Mde2OeIDQJQ6QCefdzUpFXuutr0lM0lIaOaINoyxmgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTDNcPC55xa3RzZtmDxAyxZgOf9hX_Srpv_JVKpiLg-WGp-FJSN7IFVDTr8ZWt-16mVrOFjlIZvEZpMhTmGtOCw6OP85sGbx9w2HTiZ0C3JHXf2ajapcdTMgHjUzATglpGUNpFFrgi8z3XAykGKralLsDpIEz91CRW95ADdQZW5evVI8zhUE65uDKOQeKMftiNo-pvl9ZupXgjnMNv0AjmhF2t1Nj-ubx0ugeT2o5Vwg2yNK7avePlzO3C9UxbkA8bXy8JA7XQ7RzexnzLCYCwzhEIKvkqsh2nnx5stNbwQD9kQzzfrJtUN62MQJ1lHQXGPI-mm5wskp9m10k7jt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp9nLHpIPhYJxCh5Bj9mvGk6ELrofafm1cq-vbbGTE01k3i5B1fGidTN2pc9vxqqEQmvhS28r-lDodMgso8xHGP3cFgQPM5PrJgvNKTZeJuim4QsKen14u0gZn3GV4CehRNSlXyrP40mqRxvZAul9i0WMmpq_XutU8kPjs84_4WcWKgQe9kSWlXbM7DMrI9wCZAOEIdCeJEZelxr9tt_9ItbiGm29ptSbZda12iFLG0R1qB4_UduA8OTHsEga-xVp8N4J7TIVoyCfVgi5W24uO0X4JNy7dz-huDTKaRKBuUaYeC-gCJbV8NRawgO3Yn5ZqMubLy7TgaJzxCd1h2TzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPywgJl4AXlkBKlO9vCsKscbGDP1Xj-SQlZuyhnjSmtx8r1pdfkdUyn6tTWrLhn839BR495fT9b_-PqLrO1yN9WDnFpqp0ZrSd3tbWSViE6dvqus327bj_nBsMlmya2kUOdZQQ7R3U_IkyYyJT0zUprmrtxMzFvhPZF8AfoJoxcZ1_Ccj4COujImkbGwzqF_4Lm_5WtetSQhneexraSaArlquEpifp56BTTfIoUHpKyLUnKQ1ucqxY2B8zJNLnEYupTW5hX33qfjddcBUeKh47zHAhAAD6zW6HS64CJKA7vsy08_H-FpBzQLaCmNASpbjWywnCl6j6Xg2_IRBopppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCaFHizyCYbDyB7059VA0AS6eoxVTVb2fHJfM4CXVLg6_eE9rfHMg7YKa9WGGOGeZgMxDm6CzcDHGIQmz5fz5Ltse-HY6hPxbTQA8kIEEflBfXuaPppOO6asrJmjYZU2EuXv6ne3OYeAW4eyiyQUWyuM97V5W87Ec9T3iGayGaLhTFti7ir7ZrDStCYrbQBzu2xtLWYM9hBw4GooxFmUlcaQXUIfbZN70_DDAsNZ7C8umoLt60fV9mri0InWWGb9ZAoMbAlmylIrfUGx1nL7gJdMXFt6FHFyZ40am4DJS6GeEVAW5rcyJmuQsCELKUv0CmXWPPMR7teCuEHPvxU-hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDjI2zW1drL50oMAt12zluMJsnpT61iV3j8KLAwZ6RhiAChPCldC_AABKU0c9dYxTCwJ3JuBVPpEfS2UlvRaQZELsVrZ5cyq7Fmvh_UC0-tcYaALitj3kUFNTBdajP5yNH7jr7C6SqC1SYncokVGkK6ShEDKgrsenPRb5ZKN0Gq-sKHAi6rzodu2D93Yo4Qxc_F8bFW3R8rTHFIH_aNUj-USbxYSFFDLqA-S47xfwJpgZPIiQjRW2bu19khnHJ-IPZmIzoKzxSiyh0_LtN0RhnbUhEpJch37Nc7LpICJ43ll92vVIJNx61EyJq2a3r-n7K3h7i1_DiaBD63uhsjp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP8RKHHMHs4iwx5G59ANnqYE6lbIwos2f5mLf9C12i_-Ni4dZBMr7UPIlpPkNlBFKUaCwUiPVwc1a_j-An67RqjZt5un8u-NMgVMEYKxsPcflCwLB8fc2ELOIAD1QlxfYOB84m7Z2FhCU0qNRqhNU3lclfJ-0wWbtEPEow0midPIwGvRVfbUQZ-y15uWltRkrjebE0Dnww99OqNiij_G4pz9Y6Kgpu5Gcv6-R0vMYMHZNtojH2yLpPNrLd2BIiOv3XsoeyvyoQP9meV00QOCFFjC13Egf6eqVu5pWZHxkYVlntBLFGpWRgpHGc4oXAxDwpgqPh3mfkB1duaVzmLq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=VCwxrZtqkn_aCeGzsFDVMOiQkMpWWItU7KUGLuOfxK6UV68CA_fii18rqfDeBTgwFC-_OO2zHyKF7sTopwLuF-ZCkDa4qVhTbpVEfy2iruzo3zYgjZqjcCuctveyNc1KTBsV40IosFSomrqU8bxCHbfB9_fEuKuencp9fcpetvaEidSSUhMrq3Ggui_gMAANKSuHZOy4Ssqaw50nk6-kZGT7S-aYNysoGfXci5pEB01wHG_pO-3aome_DrMjkGmcmzaFfVNfj2UyXKLCYsw2647uB59_0U5CZrTgG-0nDJMYq3hyyFOsOiMWiZVVUcO_RFyq-Y7ehQuwnUm2oCaVkRf8NeJWUMxQlYJTNqr9idb0nrIA6vqePMksljdPP_dGjkLXLDcz4QWmrUarVQ2wYS9keNo0QeTG260sizeHTDYhxBJat9UG8qx0sExHrwWkDfNH0Mx77AyWJAGTggs7e6EUcX3pN5OX9KGdCa6LCw6mfVjseICqgQrI0j8EnIs6uDH9hPxLpiI-hGHR2XNcmjyVuYdgQQ5_yGF205U1HpGRhuS_4tlvBabWnq_WWzdibp-eTny-XKI5Sm7mRIVtxGmDkRvVmSGrA-hDnbR_EgWi3GODg_12zEwNOpzWXCU8aYJ8lZb3goXwRH7szxZdSFAmX9Ol3-T-da5sXm_lmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=VCwxrZtqkn_aCeGzsFDVMOiQkMpWWItU7KUGLuOfxK6UV68CA_fii18rqfDeBTgwFC-_OO2zHyKF7sTopwLuF-ZCkDa4qVhTbpVEfy2iruzo3zYgjZqjcCuctveyNc1KTBsV40IosFSomrqU8bxCHbfB9_fEuKuencp9fcpetvaEidSSUhMrq3Ggui_gMAANKSuHZOy4Ssqaw50nk6-kZGT7S-aYNysoGfXci5pEB01wHG_pO-3aome_DrMjkGmcmzaFfVNfj2UyXKLCYsw2647uB59_0U5CZrTgG-0nDJMYq3hyyFOsOiMWiZVVUcO_RFyq-Y7ehQuwnUm2oCaVkRf8NeJWUMxQlYJTNqr9idb0nrIA6vqePMksljdPP_dGjkLXLDcz4QWmrUarVQ2wYS9keNo0QeTG260sizeHTDYhxBJat9UG8qx0sExHrwWkDfNH0Mx77AyWJAGTggs7e6EUcX3pN5OX9KGdCa6LCw6mfVjseICqgQrI0j8EnIs6uDH9hPxLpiI-hGHR2XNcmjyVuYdgQQ5_yGF205U1HpGRhuS_4tlvBabWnq_WWzdibp-eTny-XKI5Sm7mRIVtxGmDkRvVmSGrA-hDnbR_EgWi3GODg_12zEwNOpzWXCU8aYJ8lZb3goXwRH7szxZdSFAmX9Ol3-T-da5sXm_lmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=LQiuCHNvb2RBVqioEPOVBcKtprV5SGkgdKEGTiEaPK6nfbyxeDT6OZ3jipIp0GktgUCQH9FA9vfjOp3CW8WX8gJ83c_viAThj7OcKjwMz88Y-qq_sJaKKcPQrP5MhmJqfkKqBqTqgnvLma71LM9O6ugm_lvYE1ozHo6HSFUIYRrPi2ke896bv2dFadTzi-UUCrOg8tEBNQMkqSyHGVgJLm5STvTsGUWWrJrKO1Ld6jwKNLfw2mQLApiTlt_u9DPPRo78vFHQfq_BCZWsSzrlEaiePWabcq6D-gJGu1a8U8LkTxLjUELhiZEpmawdnGYb9PFeX-MBCiKPmpvCufTC0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=LQiuCHNvb2RBVqioEPOVBcKtprV5SGkgdKEGTiEaPK6nfbyxeDT6OZ3jipIp0GktgUCQH9FA9vfjOp3CW8WX8gJ83c_viAThj7OcKjwMz88Y-qq_sJaKKcPQrP5MhmJqfkKqBqTqgnvLma71LM9O6ugm_lvYE1ozHo6HSFUIYRrPi2ke896bv2dFadTzi-UUCrOg8tEBNQMkqSyHGVgJLm5STvTsGUWWrJrKO1Ld6jwKNLfw2mQLApiTlt_u9DPPRo78vFHQfq_BCZWsSzrlEaiePWabcq6D-gJGu1a8U8LkTxLjUELhiZEpmawdnGYb9PFeX-MBCiKPmpvCufTC0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XezlMsPINut5WgkCLkPQ21uOOBdiQancF1TGyrCR0n2-HC2opYEFlW1aK7WunI7nPBVM3seBcOej1D-OzH3d9CLrI6MQdCMy5Rw0kM6hzhQPP-v1sYl16c1iiCZHAfoybDfOMoOH3CTiZz4V8iwVy4Yrq4ys-dy3llsakbWCoMSUGcmXbww52Mur5TMYzIZtUSrKNdCES2mXiPpl5A2wXaS_Gtare5jtwrBvmjuh6UFr6LXkH08uBRFGJeYBpmUqvLnzEH-azIjn5MgyO4jy2XBFZ23WT2SGDKS3mXSUQER9hnbAhtb9oMvSKgYmGrYieW7B8MY6yIBfJZ-aP98EUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSUfSfYiRhSKt_6xThMTXAKEsSGuUfqmztwD6lMK6gGzjE-LD9NxMgNVLgjPLkr0f2uu4cLSx8LUI3cgkSW_xoklyN1RScL92s6oXluGb4DQv77sRiGvKHwAUGDSSTJV-6yzCuvZ0u6x2ViETDsa_Q7I5cAaayrrDLk71GX4Pi-8YkXMMSsjdtmpKd3RBe6TYks_Frs_ttltjKyh8MJx6SN9iWvx1S3uOOY7tN1VQqrhs_ac7DVUR1v1pA2wj0AUTnG_27S7sgPGgK1w7Pzyez_Ck_GiFWDoa3kSYJt1zIeediNWaKEGiCN2KCreDFSVdRULEi_qOnyfk08ZFpUKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKuZwRjc89gCgwm_HK47ecVqg498Z-9UeUWrCckfhJ0QV8gnCnSnGG8MhN4911ievxw9z--ziu-GRvzlJtZoITQBju4KMUhcfRxcZ3NJT7qDH4kN7E5zst6Aw51JOwdMiu05oDOPir7ASIVByWiV7-jGamwO_TgUz_PH8F2Hj4usQcbcpxrwhJQ7KdcNBX7AtiFXBdincZ3TD03Zh_f_0VxwnUc-UEm3My0cv0ZoLsnYrYtuOIwV_wrnaD3pbjE38Q2GgayO83yp0M4Avg3hmHCblAyoS-T5BEIyObgVeemG35v4BXs5Jz_ECnSxdhl7jUS0DmsqSzbgRvnzkivxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdofmu1Tnu4tS1-2gStyKLk78GlRF7zTILJRg-_2vEbzYcnhbuZJTdyV20zRSNaRUUIxGMXxGa9ZWH9hudVBISDdlmIxGuEPtqMFZorPMlAC_0qgfNQm-Xhdy26GxZA7RUn6IivjHhTPLFSGTGa6MvRk_f9Kol4YOWX5lu-S_T3v0XKMiRzsjbpvNlo4on1SQZzoNA6D3hQJcDaKM3iB8IgH9MMYWxZ7GvIVq8G5y7iRA1xZydCSn4iddOw8igWAJPJXEUkYAr1vGrQGsXOo5CLiqOumzBSm6vLBzxTacrLt6MTJLAU-8W3npR_ZGIuZftxpMSlKRD_8FtG9Fu3t2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26989">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58235729a.mp4?token=n_oHd7JeKOKIwaf1_KzhWHubmVePKkYBuKSDmlHRt2o3D8_rZvMLj28BOratuSdWTiuct_Bq-SKdIK5IE7aqFZXwTG7mJfDAFQdiRLuTjiuttt0yBrjPsXL76ZqTxLBeCKe4LpUqsT9qDaZrUxcHsRH5NWmRGIbKZcqXbdOXqutGMEfuelHY1uSGFw2szAcIvdlYcOZInIuG_K8WcghbwSdnp32g8JvySup9ZfOGPWj2W_WgQTZmWHIA0EKAyXDlOQv_Xc__Hk9CbnInrTM_ZASjzlt1O4rMlkgoNXz8375iMZjD8xfLQ_AEQEjO2slvLu0_yk7mLY9bFFYTUDEHDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58235729a.mp4?token=n_oHd7JeKOKIwaf1_KzhWHubmVePKkYBuKSDmlHRt2o3D8_rZvMLj28BOratuSdWTiuct_Bq-SKdIK5IE7aqFZXwTG7mJfDAFQdiRLuTjiuttt0yBrjPsXL76ZqTxLBeCKe4LpUqsT9qDaZrUxcHsRH5NWmRGIbKZcqXbdOXqutGMEfuelHY1uSGFw2szAcIvdlYcOZInIuG_K8WcghbwSdnp32g8JvySup9ZfOGPWj2W_WgQTZmWHIA0EKAyXDlOQv_Xc__Hk9CbnInrTM_ZASjzlt1O4rMlkgoNXz8375iMZjD8xfLQ_AEQEjO2slvLu0_yk7mLY9bFFYTUDEHDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26989" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26988">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMNbAUW_Gll_jRUG0chSxwYwIQUOiIPdp6LTEdTl-qv-QIdx8IKA0dxGOMi_Ng9pDQCzoxOiOQ-ZW8_L4L9wk3KkY2hsuCp21tAPUG2Tupa1xg61wJKd9a9_S7Y3Nwpjn7xT-Pbg3hera-eevse2xq8mJ9KnOJpqBQHB3SkutOGqyDpCq8Je0C5pn5sMqImDXt1Q5xJNO8xxKkKVnZhkUGQxo8JAbD4sre2wSFXmY0mvj5x3C1wsxxEEVniLvEUuCZ34yI4lGTn-2f40NwpHgBCvkZhFvuD-13cqmDcPWra4jOlSFipVhZYrpA4QX-XLwLFfi28m1bx4kP7b9B78Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26988" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26987">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436452afaf.mp4?token=ZiCbsiJcPUBqMhzAJeazdiv9mw9a9R6N2wTSHap2XxhmZwXiRjxRRQhIWKTepfxcfcPX6StAvxMgoN1eNkbuA5eG6NjDVJ1jeKFexj_ba3zDRwzbrK1I70ybXO0zGuPNXFB0QO_6lctjzZ85IJft8IUOqPHAZQvj4_SljjYSEta9DK8pfPSQMrIMATCgRv7rakU20LhV76-7yEG1_z-nyKfOckkop65-dPdowhgcbYy6pPgEZUzS1dSZ39xkg7s7B-96FGN6tSz_lD99DxT2_rvTMeF20Jjj463BDZrSsykp-68Q0ILugQHFmmMIiDg0EE3ERmbm1b2NqCO8oxqang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436452afaf.mp4?token=ZiCbsiJcPUBqMhzAJeazdiv9mw9a9R6N2wTSHap2XxhmZwXiRjxRRQhIWKTepfxcfcPX6StAvxMgoN1eNkbuA5eG6NjDVJ1jeKFexj_ba3zDRwzbrK1I70ybXO0zGuPNXFB0QO_6lctjzZ85IJft8IUOqPHAZQvj4_SljjYSEta9DK8pfPSQMrIMATCgRv7rakU20LhV76-7yEG1_z-nyKfOckkop65-dPdowhgcbYy6pPgEZUzS1dSZ39xkg7s7B-96FGN6tSz_lD99DxT2_rvTMeF20Jjj463BDZrSsykp-68Q0ILugQHFmmMIiDg0EE3ERmbm1b2NqCO8oxqang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه بازی فینال و رده بندی لیگ ملتای والیبال؛ فردا ساعت 15:00 مسابقه فینال برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26987" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26986">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9LbR0P1OExvy4EXKKPWFnimUZMt4s4yb4o4A0R37Zu47ExWkWHVbcIr38YtED-01uZTaWQGABzoNaZ-9tkPY8Ti3YswuXV_smz1Zc_l4VsLpsdMzqLclJxGnffK9H5RrjwYEZxouw9Dk96bOtOmYR5dBJaV4xr-agUcugovPrd2_3F5fU27667a9mbK-cac6-QCvBEgHmZAWafekQdPBx4yjymQWgZ1-J6AnVQ5NcUEwIU68itFfQwxETY-L0KBUS5LRBDIUZe-iAfacl34751dJUAc-oZSnX1xAflwrijtaVRhMhwN2trSGog6Q7NUeemLqsIdSZMXvSbLgBT_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوری از دیوید اورنشتاین: وینیسیوس در حال تصمیم‌گیری برای خروج‌رایگان در ۲۰۲۷ یا پیوستن به آرسنال درهمین‌تابستان است. آرسنال تمام منابع مالی رافراهم کرده و بازیکن به این ایده علاقه نشان داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26986" target="_blank">📅 11:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26985">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ3EfO6TyY8da0zjuFEnH1cQsG8pJZEpqulFHLW1NoN7-FZqNKQ2i6lKBRmHDTnrJsAEm0XiknX-VelLbA4ykcQztEW4qmBUyJsK9re1b5DtJbWVpCMH9dFZ0_tLF8iEkNiHTp3BkcMuqWWtH6t7r_bynz6t0N5KXHEJ-Frge9NejajcC9vKeFypivdFHBqh44zKxF6ttCCh04o11iCDE_BoNJITEl6eFnmV-TtoSIb10v2J89IglOpsYHdwYOe2NHlvaQJ9Onc6IbIiRvir0V_9E2ThAhxWqMLIHq-lp31IHAICt_4GAPbVssXzfp39LZcxC0OhmI2YFk4yoSIYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26985" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26984">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12920f454e.mp4?token=ixsfrHmPJUIELMc6tnmi_G4mYurmZLFu_mv6nUyYP5-xjA3zn0SaZIcYHs5IOjuTPLv9_pq2ctKtRorp2I2u3flUIOyeALsIjNyzbE2-WBeDr377MTtxi3e2mV9XwarVEB2oAu3D-Uayuyut5Bhm7ME5h7LKP9PtxNfCzumkA3ubpEmIYJ9hApO5y5jAbhjRiI7v1iWU3c6F8qXvJ9GXZWYoM1sLKHRWCqkCriJSQ6pqnLkc3SQ1_0nWYfTpWiNcuxHMUz9O0RbT2q_yFm8i-0yg_3B4nBXwosbrPv1h9lVOlV1ydwY-SmT0ZRAf84mcKjjVoX9ACVutrlp1r-RsZGgm1iSLoMEn3wkvOC0FzynozBu1hJNCVO4rEyCOiVymB-Az8jn5EP0-qOn72LN1Wi_n0YTeu46UBFgTyFQNtY-MeI-tyb35ePN3IR6Th97xchyrHfmoVWFgnGwdrolJ0M4gj-v0tTS_7Jjjae3dGw1e5viy6aalzF9dlqpzFAiBP4A1fDCFDLyFow01zgmHqD-SxQFj-GAZtcq8RaO9GaqXKoA5tlZQ0vcZZcvG4ljRZFAltlsLtfEFqbEeUsP-HJ74OOH31UeFJbKjjAty5i4SFKVNlQsxPwfAWHSIX957BLVT1Ybx_HrClsfYniaPDy5aKcmvpjlMD1QJE7TlWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12920f454e.mp4?token=ixsfrHmPJUIELMc6tnmi_G4mYurmZLFu_mv6nUyYP5-xjA3zn0SaZIcYHs5IOjuTPLv9_pq2ctKtRorp2I2u3flUIOyeALsIjNyzbE2-WBeDr377MTtxi3e2mV9XwarVEB2oAu3D-Uayuyut5Bhm7ME5h7LKP9PtxNfCzumkA3ubpEmIYJ9hApO5y5jAbhjRiI7v1iWU3c6F8qXvJ9GXZWYoM1sLKHRWCqkCriJSQ6pqnLkc3SQ1_0nWYfTpWiNcuxHMUz9O0RbT2q_yFm8i-0yg_3B4nBXwosbrPv1h9lVOlV1ydwY-SmT0ZRAf84mcKjjVoX9ACVutrlp1r-RsZGgm1iSLoMEn3wkvOC0FzynozBu1hJNCVO4rEyCOiVymB-Az8jn5EP0-qOn72LN1Wi_n0YTeu46UBFgTyFQNtY-MeI-tyb35ePN3IR6Th97xchyrHfmoVWFgnGwdrolJ0M4gj-v0tTS_7Jjjae3dGw1e5viy6aalzF9dlqpzFAiBP4A1fDCFDLyFow01zgmHqD-SxQFj-GAZtcq8RaO9GaqXKoA5tlZQ0vcZZcvG4ljRZFAltlsLtfEFqbEeUsP-HJ74OOH31UeFJbKjjAty5i4SFKVNlQsxPwfAWHSIX957BLVT1Ybx_HrClsfYniaPDy5aKcmvpjlMD1QJE7TlWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26984" target="_blank">📅 11:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26983">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=Zggm6QbOIBHgocokerjK_4B9vAUIHHi5Hj0TIFGZAmm0f74hTs6v39gjmJTSLXU_TICC1yQksvSAGk5sdTas0sQZZRmGaSu-bzS8rKAvLUSFa8eCCGJ5dXg98K0klGD54nwX8_9hgf3PlkQInTSoUdeFwgUeOFIhF9kBD1_nGqRbNd0NcnVzGRI7QN27h37k2lsTuOPYQceqT9iE-5DrGpt6lMBHDapmAVEvpoSWW2LJQdRC2tIr1ZRi5QA-L6ZNT0qsJqHNY-7CApvWfxftWTpH2P3G-8I7veJxI6B3hePv2BWTwOHAxpAihoPsRTxtI8DYdto_BqGxJIJAVeHgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=Zggm6QbOIBHgocokerjK_4B9vAUIHHi5Hj0TIFGZAmm0f74hTs6v39gjmJTSLXU_TICC1yQksvSAGk5sdTas0sQZZRmGaSu-bzS8rKAvLUSFa8eCCGJ5dXg98K0klGD54nwX8_9hgf3PlkQInTSoUdeFwgUeOFIhF9kBD1_nGqRbNd0NcnVzGRI7QN27h37k2lsTuOPYQceqT9iE-5DrGpt6lMBHDapmAVEvpoSWW2LJQdRC2tIr1ZRi5QA-L6ZNT0qsJqHNY-7CApvWfxftWTpH2P3G-8I7veJxI6B3hePv2BWTwOHAxpAihoPsRTxtI8DYdto_BqGxJIJAVeHgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسمیرو بعد از پیوستن به اینترمیامی: اومدم به لیونل مسی کمک کنم که جام‌های بیشتری رو برنده بشه؛ برادر در بازی اولش برای این تیم امریکایی:  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26983" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26982">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKwYJQIGnJl12oqfnvmYxjYhkIp0SWTgwZPWbcka3LKHaP6m4S4xrs5kY9O4K-cTEHS91NijXifCZp4Bh73QLQODd9e3AvaVMiHwVGA3BR0w-EbkAhxTm6120WL926bcfLw0GVEsn7dwXtLnwxrwfkf-cXsH8EXNZ5jKRHFydb01zG7YlQIMLAlEmh_Qg4cl7iLiMvsKtVS7LG-bNu6uc0Eq1n6qI8Qv-wWDA47BkeYT68lOEEr4Ez_p2mXqyA-RcibLaknkV5Cw6_WYwZBsC0_e18qBtm8nEyKKm4a_wrXK-Lp-k13iigQCQp55O-emRoXa37hXdgkdoNbWPkQ_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایدباورتون‌نشه ولی‌این‌دراز فقط ۱۸ سالشه!
‼️
«جونگکوچ ماچ» بسکتبالیست اهل استرالیا با ۲۲۹ سانتی‌‌متر قد، درحال حاضر بلند قد ترین جوان دنیاست و عکس‌هاش‌این‌روزها حسابی‌وایرال شده. حالا بخش جالب ماجرا اینجاست که پزشکان گفتن ممکنه از اینی که هست بلندتر هم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26982" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26981">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=Chd79kauRmMx4CoYAaIAHBAyaCe1xDGbGV3-dN5ykq3r9BM-SqKUmmverFcjKtJB7OYb7fNRD6MpvGfpDvrwc9ZaNWZHt9ewNZb32xtjAwSJwEZh8-WY8BcSlcaDzdcjcsJhypVlXU6_iRFDgJS2lPN-LbdFWyUStvSumxfw_DbHv-YZYjl8r7D12gV58XXmKeaSkOS7adFV82Lm9_M4Q2gzN-gDZ0hsY5b3cSyQRMVsZalzULwgLQcKpjOJ53sQCKNFKmTDBNCiCjzt9j8BSWbPYDHWkl4CfP3TVWlYv5tHdpKDR_BVeUEOJrow0tyoNtHk9Zss4Z4W7M60um07Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=Chd79kauRmMx4CoYAaIAHBAyaCe1xDGbGV3-dN5ykq3r9BM-SqKUmmverFcjKtJB7OYb7fNRD6MpvGfpDvrwc9ZaNWZHt9ewNZb32xtjAwSJwEZh8-WY8BcSlcaDzdcjcsJhypVlXU6_iRFDgJS2lPN-LbdFWyUStvSumxfw_DbHv-YZYjl8r7D12gV58XXmKeaSkOS7adFV82Lm9_M4Q2gzN-gDZ0hsY5b3cSyQRMVsZalzULwgLQcKpjOJ53sQCKNFKmTDBNCiCjzt9j8BSWbPYDHWkl4CfP3TVWlYv5tHdpKDR_BVeUEOJrow0tyoNtHk9Zss4Z4W7M60um07Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
محمد نوری کاپیتان سابق پرسپولیس ملقب به جمله معروف و تاریخی "هرگز نرسییییدن بهتر از دیر رسیدن است" با عقد قراردادی یک ساله بعنوان سرمربی جدید صنعت نفت آبادان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26981" target="_blank">📅 10:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26980">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr-MlHcZoHURs3YRxyH4_q7qfCtR5azhDFAM392zFo5bsweCCpEK3-B5NgOLdB5Peyk15S-8U2DfB2N9E1ltsAy4quVF3YjRfjUfY3rWq0looXYva2CowNOGi4iAzHDrBmf8NRP6VPcIVZcEtjoHgxAtDDWoszu7aNaAVs_sr7vfQyUZdclwRkkTNo3lBYvjHbLOpB55PTmcOZmFZ54xBNwOpkEbFepjax_quzybS7m5gvHGReAAVmXFb-iHkEGXWMZbrdGyMFk10YHzPGi3FFoqlL0hin0tXUOOUubmzesloUiT2d5rzVYw7OKPCw4DL_OELA-B3siMpfmDj7E_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رکوردداران بیشترین‌تعدادبازی درجام حذفی:
🔴
محمد نوری: ۶ تیم با ۴۷ بازی
🔵
محمود فکری: ۳ تیم با ۴۵ بازی
🔵
مهدی رحمتی:  ۶ تیم با ۴۱ بازی
🔴
مرتضی فنونی‌زاده: ۲ تیم با ۳۹ بازی
⚪️
پژمان نوری: ۵ تیم با ۳۹ بازی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26980" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m920qkEA6wA7S9p5_sdJUIaTmqp-myCGep4aLlxfb5qlYed1crPlR3Pg60t-RJNS9DBU-SOonbE_YldJScAOhPY7-PTJGNBhbN9cwTedj6th8bHBLLXt4MXxEJBk4tEv6dbCdxtCwS9Y5ZUMqvveYkGYdHzTg3D_aikish_xcyxePSIPJfJvJ76NIlbdO7x3xaThFMNCGmyoFP8hEjhWZvuCr9EUHcFfDMy4VoyBGv05m9IN8WQBRYhAgWNNHKNE0qYgy-4gOitXLGI_N_V-AuxhzuE9VDbwRwTeCsdZzM2kbspoEY3FyYEbiPZIKJpjQWKEh7EZxZhew8Z1gvWQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E10L5c_OqYjhgnAi8s3j3LrbbWWEmkCb-2M6oOMxUCVy8o-O13PYXtj4aAr43-2C7CnUTbNFKSarfXz2Rn1Cg7EE0nii8EzSX64Y7QqH3EjZiZv_iPiEvh-NiSFerWK7euWhQpAlWS4iPbGC1WoIkB9rXWEta9jAREoXCnxG624A4A8qtGIlM38DwwPJnmQyCGjANq0RgFz5keoX355i2BGVuhY60Zenyc050bVJEgBdHxvu5jm3ICRDN8HYONoTT7fdBROo3ED9DleWtr3CWLwUR-jm13x5Ff7RuwzthzUeHNy7pY75vHcAFFaaTF5qrucnz89BfbE6QK0kIkWZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFlTkjgBGKXEdefTvvxj8o8dF6sXwJaS-7re12pPoKvsQhd4eVHMVcZssphQLUMYQgenq4c7TDb4cIt0YHiwW7SqDxxVMIFxBK-HAq6a_m-I1tfR5VfEGRKqQpCbTP6tuiLxmzgLLgCHuL3IKoJgHjhKvTCVLI-wyj1N6yg0MrYf63B6qxoTG__07V_fMlS9D8GVmmpDVu7fWZzQuiDik4cMaNHK0-XxH2CVxK2ivfdPJXe8otDepRb7bhLX0A74Qg6v57bh59vt2zQ6gJo9mL0fdXhVEt3AUuUkhc6vf4510GBXRkTAbb2NfujTEb3TzfZYWz1EIMQAlba1WdY8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/namfBsEFqdZxMC9ANAziQL6ZzDOb2TqQXMf-vlBHT0nj-ZtyjnVKDzOzup5gTZhn8Bkhu9h7BYj8gGn3V_W48W49SiYSbFDxTV-UB03M8abn_XvuCxv6HIIEXtofQ7G4dNbqFbarjKSsYerR3J2_HMJRgT8HVJ_yzBto3seoqJJkRkfFhtK4T3ngmsGfMupnb4zIIiZNDIc1nEFY7I1whfhD3O8lRpimFj2mNC2oBHRciFVausj9mTH3wOOu3-PMj4bZcPRxhCPE9hl63Swoy9d9fXT0gBaynQC0USKiGuLwQi18gLrGWCMTTtvQa7WlibOK2XUywshMUaCjtIpNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX1Ji_nYSX5FYFf5QvrKid0WdMFQxeUpmWnAiytD5hmJkZdNiP7GcC8BXX5P0xtjWxFQFKbExrF5b7NQCLf65REvDYtxFZCa_TdazQkYvB8b-iib-oSXCpIfYU3Zqxz25KQW7BoZi7BwlUaYMvW7JKPeb7A0KSM81uzdQnSftzqqilZPZxweTsbLG-WmMJvGiYg0d-9iBCa2TRIpAskkPhsu8T5A5tOgFtBP0Qw41nsQK24aU-VKUd5s6UnyeVtyEWw1gi6033qyhhbQ1m3Yw9LNUEz0K2bIbSaw68WLGZyd9DK3CTlT65eavrhmwkJSYTjhBBJQ9vKgWWTmFT93Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOTA8Bu5H8UMT4uRv5sc6w8OGxBVV8NmNc3q0fhJNzk1YSPXPGxxu4fZH5fkfHKNBY1zX8D1WLPtKvPw9wLf2IMEcdyq_jupw8FtowyVXCk5vlfJAQcNhnZicthVatFf1uzY6i2-BaBBCBAm2ql_ZlcyTVGjL7wWc9j2vuqK7jhM4TJaJcm_74FoP193970Plf8FANTyWIFbS77a8GleLvXiSX9BBEQqLJgzPibK6Ikj1MGBAplxLbUOWrc3BQkqqv2MtzrzlWwHLnWF4dSpupNZf3ytF7jJi8wg2T8zav0BxPaz80X_6GqjgDyZfi7Ui6pkXAXHDRPocbHtzCrkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXsQf-QfEwUw355lSPgnSTnVp3RZm7Kr1bv_2YSmu9E9slAOM2vBRUsamTmtN1NmYv6ykk6wKrFC6wjuJT8hDRrYHIB8wt1moa7MCnMtjVegxzjtd93qIZfoZG3W95Ho0pBufOlhWYmHPawePQvbSkoVc8j0nh0eJTxvJMW63elMYEAjGvVi9UiOb88lmeX6yggLQEld6OmrbhUE_zqM_8ojm0qAlBw9I1hEnhWP7kDdUHHDD48I4G5gWfqMC2tItSc8ThuyZfboSbHcp7F8bUo00qbseNCmv2axQNt_hKd3626LdI2ekM5Dn8NrOuNIqkYG2b6UviYZ3Rjy7vhhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhIbpPE6PLIdehsWdq7IhO_QCSp7sb1-YglLczv0wPxhzmRCBgzZE5n-l0i0kpMUknqiCn723I3_8fQ4stmYXYqDPx6TDA48nQ5evYZHAMUc1odnk4i4i0pBC5NFxZwAl9TGLbcvt14MQGta0QGGOUGXmife0qUnQwovGTd63mhC_WV546gJzjrOxLiAHQ16cZ_5xzQxGJsGRyjwvntH_UuCjHfoHEqhbDOXE29gBXY6PRk0qo2UWAtV7HpvA67wGeUN-uaagOOWMbtKlAF7vPNKb0LKpLsDQnkya7mqQlj4R1ChS_fLp5jMaUaZhxV_A5GzMlMWJZxIUb3RVQ7o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HW8JcJop0fdjUhP7O2ZCEYeBFpNiGK4TM10YmO0tJgbrIkiPEikJZHXjYMeVzmm1xJj6oa_nomR-UgmJrMkzeAlNGQNoZYU0SyqSAIrdXwmxUp13qFNgqzh5tkI5KrhKUzVK-uD1FDdrlKubJa7Qxmndsfa-2fxXl_nt0sORhS-ZujlRFGk3SJUYhG8_FnqibCrdjDL0PukKxnToElHwNtAGKVg0jS99tqjLlSGc_rex6qHixgooXdynTruPxcgBvvWHiOjiaW2C1gUtiy3b-N3vFFTuYxkiIl0E9psEH8Qh2Z6n34H3vOBSl1iDR2ON7V6ynW94vkKZY8DhR2-21w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGkj0yp-MGBx2IaJGP7PmCZo_G-RgMhArGXjuj6mgNNNbG1KHIUBj4nYHROQ7iBW95kGXiMQDN6e4T1ca6mzofyWZ7B7F3n_iVr5vBoZyaBF1VZ0CMvLn9o9Sl4B6xKULw4kC8f6FC4sKA-OibgwmFPEIAtkyEBXpZKnR1IHfGXB5aleUJh9mPO2dm1RBeBrkpdv0msuB9t6UI8WZyZjFO1QrMHrM7188Oby_lHaZaXYp3ATEHMUYiK1GJsPXmd7SczIstBuIebr-Kl02iNK6qhNwvF15PB7c3scBhNt-85xFGKCDhepVfuCNwDxEmRL2dpEcq9qtwNiHvuEedGN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJcGmFTgXeKGsArk0bLpQypS4TrFGYuiEt-dcAUkE_V5fHyfAXtQAXmIU3eyH5NhR4nfMGccWbEGi6iJTszlAma8G8YqmDoUKwNCXTL1CrKRw2Xtt7Os06wzGl0qp8TQA8ixEnBYcYkh6_1_iLUL9kcUu0K8fDbl-jptA1zYzEhthy619GQDSfLfCPF3OkpQIWefQClfyIFQiA7jMa9SfrEftM7x8jSjQyBmRHh8EqLaCpenbQ4SeQfVFYxft0orNx8Fm5h0wLEka4Q4ytOvKs0hSe9rcFhdcSXXPZGBmBiDZqayPu_xPbk5pPeC_ZHTNl04Pb6LRoJqhU08BhhBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL4M4pDR0qeyngTH3G2rl5nXsujun4Qd2RrygoLb0CJJdSQ2q2i9MLpNx9M6WuchLfAM9fKE9TBMO3FC8Ot2AvWNX5HdTSMMCUknRnT2-izRVbllxRNULbLU1fgoWlQ9RkibDIY_yeoXjPeN7xyrkCSWwbNBnEmOTvaqkBYgI0If9FmftMVVuLZzzAo4W-qmq6MgEaI5aWAAVmxCWvkR8orRprbjS2mCToWlfPnRGNj6ouhgRSaEHc_80Yr1saH6vHLjDNMihwgwm2C7mBKbMCiOoc-xxYNAMbedfxCVxJg5Xep_oWDqe_f23ZCVit1-O7nFCi1l6mwbZe_9ID3s9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBoivn64JUdRZr2isyCIh7za7kdAZ6TnMFM9amcc7-dPW-OCLxcN-mWL6wIBlZVieoiC_W-KDuAq3wOXDw8-ZJa68yj4f7p3w4CgNdS61olk4cjja4Ol2n_OlyGdJKCXua2Tig3pvineSrnfHnz0MTIrKyoFo_b-2o1OvalXM-8OD-_Ae-WoZe0aMIfvEhJ-E5ONYmVJIVKj6kF3JrmqC10dv7XcJOC1A3Bc9G4_jwm0VOqwqY7GQ-dtbT7Xn_nRAQ1h9UyStGanJc_66QhttY5LMUsutMp56f0BOm33Ad7JA4KSzzUSVhlbR_DIPb3ttyNMybi_s53EvkLPCh4Trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW70BsjGJ7O1MFImFenjokgD-7Vf9ZTo9JitdhXIprOj6Y1TRr_mJAFCcNKoziSDK-PKr2LD13SgVplbMajXAMtbaxLVKWV_DXotIS6RB-LlPfcjlOKwnTEINf3OtDiOmOJHL1-Xy3s_zOfsDHhChFlUGhVKGXgtnA08Nwt_C0RSt7rA6CjQ10d3GeaMt4o8o60d8JYfG4kXq0Z184U2scOYytgQTw1qLgn7v757ToED7-KgEQJkN044vB9KYT8If0yh4itrsKoMVqyIHicd0eJ3dwahOinpIgWhDzOCvcbPifxMLhw87SiXcGOg2pLquc5cWNlqx2m-lACC4CQs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIPqeXDYxBrS0iA2D4u_ZCig_AUO3ewbJI4TP-g-bfd7oB4sWoZxSfjJmxugwaYTuUaiQ5jcT0dB3061yjm0rd-8ReyvZl_eyOH4L3NQvazyQvdVxit60BmLZySaiNToa2JFR_cxM2qFhifuTQ54dSd51IoFWmnDADLGpTsN7-FqAL-Q0A_NAQLIOdTgnA_2ZC_ZqRtmOazeZz4ZujNHgh1AnxlCLHCO9E_sXMH78PoEmz906nRh-Z8Eo_0o8RJDMEpyj281GYJpOMr5SXGerOeeG5e7eonhkltY4to7VI5SAD5pl9EGS8aCHcq3d8ftoNfcutqCx_IkPsftIR1uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLjGodyE8R1ZiMlBFrsE2Cgq0WtucCb9tGmxlOQsdZR4k3IKSxDsJsGONaHqRZjh3oPxiUecDaPiRiIOyewc0S54240tU1YKCEjfEkD-3F1yDABy76sFu0bo12KfE_GhK1PVyEI8_CeumSHwofUV4CP5gJ94jwfqZAf5s8xahp1WcCC3YY_9fUkz5opJP7C1qTBzf8dYHgwmunuKM6NdjVWuLX-dlpHq6qsbb7Hm5Rm2ntxkYaNa8CLpD02TeL_yFzkvOezJ54Ean-H1-UFouNKTh4-CMd4GvsN1zBE-ZZ8JzcS6dVkDy7lRnM6HuAa8884cpRWf3-x5cwJmcbKlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26962">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMWHSodLrFtsWCPFw5HbG1Ihq6ql7DlIzOjqQ9nhHK_O9UlWPCdB5k2SOQEYvLadQAVNmDlDdkVmB7eG20VVZzFEOdzfR4yEuvhgtxGBMPhXE71pKv3Zdc2x2OUAP41xKiUwwkI3k-s40uleYvzamv4vBggrzB8tuxmY4jYHK2yX873a3UoOYN2eOVc0PNEpXJ9KhnkZM1ifgjMnbTiCbpvUbF7kG_aDldMBnQ_DW26OQ5I9VtYMFkZN_g_UTfXTxOzIRYxDwNG5XbXNyV8G-e1geLs8FIpc-XHGzALoUCy38q-APOhuPY6h8Op6VtMLXiQ9HmdrJu16UGq8GlLc8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26962" target="_blank">📅 21:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26961">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipQ5ITNIWNnV_Uj4I87G2SFjoNbIB41kffpZM8qXPaHxNF6OJF9o0Tgvc2NTvDkjxPxmqCkLup9z5v4zZj35gzy1AuGhAWnh1QQfmvKLHcIOwVLyutmzmwC0rCr9blDK78k0qtgTG00rPACxh8xiD3dxKKre6A3jctprVeOgz6TPztwME-B28K421HeUbLW8Ysl4yFch-2pFLAPGpdvyapebhpzoTd3a_BoeNS63iLvY43OQ4Rgh_iKnrLnw3UQVj3WSRV_C2MJZWE1X91EQbLE8mTjiP7_MKTTUVKoXD4oEOSC0PPIppmvNzlBI6O2xS42CEYl8d483CiI_NR8DiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ های رسانه پرشیانا؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ سنگالی علاقمند به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26961" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26960">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNz_UuJhz-KxiN4dvqsrHRuBHcxQbuv2doYvclCk92zW7afCZEwaH-q7ATi2IaqZ0NoGAWErxMUp5Q8qgzyATqbkxsg6zM0dyx2ylj87aPgKhPuZG4spQueA0IQMyJ7kMhkBk-sIhsMszHw8R5ttWjQ5IcL1vhT9Uco9OiGtd7YNKF7PexoYtPihHWIsW4FLHs2X2rBNP7exRWaRK021stnHRfk2HF4lcmQCpQFTZBjE6K4Q5Bbp9wUmesPeZFZjqNkYrs79yW95pmwrAyF5InniYlOqyQJcjjWWvQilHlRAtthC7Il0CiYS9jywiJ5rSFcx21Si7an3PyAedYMaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26960" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26958">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GLiFGNdzi-ogH9TrFru1o-zv6lBUQaEF1x8QZg5of9iZ611YAp7aDJqBL8ndwg4PYzgzDrQbSkM6FdtkIbPLWabQXEmz921bmzaCgJWGWc6bxRYq05udMv5IrF9d6eiJs7gXTcNlYk5XOgGQcBqpiMoA8TBwYgLJ1nEkyfMnBMdgwSxI3ufTj3fa_W2t0nSC4iR-0xnUH3_b8rKV69wlzU0nGFpvr59dFFkbx1njp334Jw_sGRvLOXM4-nC9D-lJqiCOVf_UmPBS-anPWPJTUkpzUjI9HyczPkxvNKZb0WaK_EDYRjQY0hZy1vOXe7MOdYRqqMcwux_FW2rtNGEKwn9aXXv2mD5UDmd-DxWh1AyEnsAirbLvvwUi18vhL0ilAQw0eELpeyTDF_92wxO-ZuqiLEiwTg7CMLeqQraOIe62_kTClxVwzboAaSCyiq4qznGvHtf_zcaSbI8JKpw8OEa1AbhUg-3BhlH2YH95HWiIPFvCwXfs0-9o9Mp45G8lVr8QAhwctSHEED_dAMoiZgXJT_-f7hJvIT4gRAo-JmvqBiCZsUafOpUB76E-YNoEb-i4ODNgs_wIZmCoP5hG6cmaV53acL943LutbYtIaJ85yXYkhIW6gdK-c-Mx5zytodbToMSad3kNQetbu3iHEKDQVlWjhjIJYxatwQnQtbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GLiFGNdzi-ogH9TrFru1o-zv6lBUQaEF1x8QZg5of9iZ611YAp7aDJqBL8ndwg4PYzgzDrQbSkM6FdtkIbPLWabQXEmz921bmzaCgJWGWc6bxRYq05udMv5IrF9d6eiJs7gXTcNlYk5XOgGQcBqpiMoA8TBwYgLJ1nEkyfMnBMdgwSxI3ufTj3fa_W2t0nSC4iR-0xnUH3_b8rKV69wlzU0nGFpvr59dFFkbx1njp334Jw_sGRvLOXM4-nC9D-lJqiCOVf_UmPBS-anPWPJTUkpzUjI9HyczPkxvNKZb0WaK_EDYRjQY0hZy1vOXe7MOdYRqqMcwux_FW2rtNGEKwn9aXXv2mD5UDmd-DxWh1AyEnsAirbLvvwUi18vhL0ilAQw0eELpeyTDF_92wxO-ZuqiLEiwTg7CMLeqQraOIe62_kTClxVwzboAaSCyiq4qznGvHtf_zcaSbI8JKpw8OEa1AbhUg-3BhlH2YH95HWiIPFvCwXfs0-9o9Mp45G8lVr8QAhwctSHEED_dAMoiZgXJT_-f7hJvIT4gRAo-JmvqBiCZsUafOpUB76E-YNoEb-i4ODNgs_wIZmCoP5hG6cmaV53acL943LutbYtIaJ85yXYkhIW6gdK-c-Mx5zytodbToMSad3kNQetbu3iHEKDQVlWjhjIJYxatwQnQtbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
پوستر رسمی باشگاه لخ پوزنان لهستان برای اللهیار صیادمنش مهاجم جدید و 24 ساله این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26958" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7YBI8KT-nEePgqubG2io7_lag6P6QfF-UHsttMKChsLKHz56HMXECqJe4913j9edm6FM82AN7Gmnp1S6yzjON5wh1p5pR9PNAUW2sLRUIFjQcfbXszsASGkv9yvcMT8gfhDznBU0R6c27F06SgZcU-5g2hjqzDVgzGnGGt9FUGnaSDp0-vf-dqda2mq-oDKXqMdEBx_3R7wthKLny_X7OO0o1LWd_cppdeEY75zl4cJxyJxp2mxGeovtftIQkwFQw8mpAmObJLgglh4x-u4CqC6e7EuviI6yPZGWoeyC2LB6arWkhVQZtQTQa_d90JnSrWBbghUhLrzbmCq9ldy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfDErY7x4m8eplMUlbzvYbhkuHilawZnr1pGjNkeXpGu0BG_tfPIObaewToDkbNSKIu4m2meL1WUBIlqEKdSxZbAA9kVPqVU1iAclnIsHv9rUF-rrzN8H6WJYfcbH22vJy-U3akdSkmwN3Xr1jp_P_3ik1LSNUa6Kggbwvqt5yhGh1Y9BVwDL72TMUGupN-2JFkMgwoZaLgC2b1VD8bi0CwaQxNYxVfkku2TtrkeOH4rZZEhLkcZfsoyaX4Z162tv8dPXtH_pJ2SOicsdeQBhjlT-DN-lZ9drmSOzR39Jh0k9ZWFq3cSVJR5x3BftuHO6j5LS-wxisYmUIyqy06eNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCnLKJ6dzrNWYcaYIG5q2nYcUiOS46An4ktx-25VYySRf4SlsEZr4yn95uHgnF-GH9k0bXHzFS4l6YCzj9Vx51ogxBVGQws-C-5AAyMB7dS-jTEAH8xKA3W8-HqtJWOo5aguIpreMaCPteAHWWusN0JlVCG_9hayqcBkhygX5HzgY9XZqwINLOBTE_sCoS-T9Hk0HFxTqRBt5sxkgts6_8jPjPQVz8TkqPWlTuLpnZK3hweRHTH_WxJ3xK05Dqs8VCFUsOiHnvdrrYypV3IdVHniCQWfsczFKL0QHfQJhUCA-Tzg2ef-XN3rsQ1zDA_nPDTLVA0uLPu3l5H_RrTC2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkAiM8MPx81KI7AiCBYyudS7dxxHO62A8u-dMFVxp1fKkQOKUcbSYrrO7I71hWOwqHlEfTQhC7iKWkoTgarZrkGrvH0BCNPgUTXnkS5uhosDFhtFBoNNs2x2_uwfHiO_MLnyXRrxZ6hGHRYNjUMfeg9DwgTONKIwUGej14_TB30HmvAtHAUqSOgotAVGM--KfqSdclljfYRuELD9CWczrCJRAOuDyALJ5cH1S_2CuSmbwHcivOqi1z3BIcXyGbhtZN03rgtfikwWGtgq_Z7zm0yaJWaQs0fpPJa37aMlqx6W6HXi6Nns65mT1hlk0lzTQ6ZSmRgK3spcOC_bqeSzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMD5MdQ7XIuCJrBrlLFagx76psu_i9F7Rap1Z7uRGfyQYyFlfe5MA-ByjX1XjXN5aB12XmAig_sErkNspN9Q59c0UOcHjmzt3ack-96pMYGbuGLhX_IHx7oxSe4kGuUkCMAaJXPm2WMEHaSlp5ZmtxUtTTqtNDH2ogQgSO14VaqoL_2b-XoCgvIT-gg_sA7AsMBv61pvktarRgPTY3R_P-OarJqdrXP99pfz7VCakAnJY0nAP8OJY2FMARPSteaLemcdXPExunSczTUP85GEVTamAifbX8aWIEPE2dpcV7TJh6fYWwe7EKzbJtcgh3safbNLzU08zYuKNEpjBlo4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3Y7TGkxDvA164wjrSbwFDfVORl7X5XCVxI9aXZfh75Ih91vz6wT_CHHJY2hvh06Z0A4ycp1UDXNX3FOSqQw347EYQ5gpldhzxfzIpoeE6Z2PtvBuh_n2D8r-Y0oa4zdFlJ2AZ5CubunElulG0Q9MbvmJwqk2GB2DS8C87iM9vLyA9pz9oECKCgFIE_HaaXac_9oZugxdVLkxE-AwZ_P_P2HQtkk64IAHp5CxRTvKTPoH3lT6sax-sMgJIeTWts27OU6YdX_Xr7-3rDbalK8Jh7_FS4DXFBbCO04aule_nv-G3Nk4iUZFyISnagXPgorq_CErImZLsXOJVHZsxeg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=KVvGwE35IcsXUqALS8I8MWlp-VCFhZQxE7WhRcccummgXWSnS5nePfuGlOOHorRhBBq0KdpfDCZ6xkuGj0d7l_7NOWPBUl5SQpQJBs6YPpUTZ0LNZxB3rX4PJBaymc8bg_mvsGQAAsHeQZACPPM2L5Ydq--T-Aay4Gbs4k7B5tKZWairyaFpDLrjP52nJXDD0CR4OQJWcwWh8VnEpIdVSVqnV_G5OXSaVD5bpkwVyQxfMfR_BH5hfxjEbMbfTSdd8Zj83VFzRrBRM_UeHHij70yJds_M6tsTJDp-G60uFeoEE1s7p5bR8OWb2B_2LOScdFrP5rUNh--1nfZGSXB2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=KVvGwE35IcsXUqALS8I8MWlp-VCFhZQxE7WhRcccummgXWSnS5nePfuGlOOHorRhBBq0KdpfDCZ6xkuGj0d7l_7NOWPBUl5SQpQJBs6YPpUTZ0LNZxB3rX4PJBaymc8bg_mvsGQAAsHeQZACPPM2L5Ydq--T-Aay4Gbs4k7B5tKZWairyaFpDLrjP52nJXDD0CR4OQJWcwWh8VnEpIdVSVqnV_G5OXSaVD5bpkwVyQxfMfR_BH5hfxjEbMbfTSdd8Zj83VFzRrBRM_UeHHij70yJds_M6tsTJDp-G60uFeoEE1s7p5bR8OWb2B_2LOScdFrP5rUNh--1nfZGSXB2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALveS1NIHITL0nP8wxOdDWMSkt-c3ndXip5niVvsf7861YjcKy9CUC0AvE27x6zzsx051MzAKUjmf4VYa2u-jJLc9bheV9vemLyMdk1nNM94ygdPlNkTLURmuWeYb5tCneG6G3quiPffWhM8c97llQe8JyP5fPiw9hC_3LSEyf2vfZIpBpDxfo3OQvuWA4I6Aw4nKXy0zzLcVVXDPXbprV3yEoF76GVOdCICqvUXsOfT0EhByXtNNHFD82qzfv9Lcuwt-JnXA-GsbaGKGj9GXKICTMa7hsYwiNt83058YJA7V3xrWHIDf4vqo7uNs9Q039LAV264EiCjieCFvJeQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQNhnn6_P5sCQli5uZytMLWxgVap_1t5pt9xfVrUR2OqV3LhONyrXtZT0WvnaJDEqVLb3EVcAvJ3f2WUd2flwP156YvYyGEDj2x8Wmp41dL_CDscDPx6uP3Cfl2a9lg9xD5487lbNfTyl2fxkja0YEbKKo2neOAhpuQ2f_jyfqRpouQJfIJplZwFApVTnQNeICwM3pVit02yFYtKVqB9N4WysFYI_2-Ew5WnzUF05FA_1EL79toJfGJTkFqFQqnKNVvS1wl9Pq9vbtbgwWGqhG4ZWwe_dll3JOOux86l0dIkk6n37aIlpZtPkPrakRjxvogks4dNzWRJnefRPGgvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmUrqmNoSWZyGwLXNOjITJ2m8NeMUI81mppeXUsdiENC6JDAsbTF1n1ledWXsbxnsHBaI0EZ2Q47vOzMClCqDNjm7eiNj4gAwx38268RbqOih31fXOkgkvmvK0clUE3nVYKJ4BmV1MjljJVDuwkArU-I1_xu5kamQP2NFA7aG_JDSW8XrnoFr5mh3xXjIu_EnRdpcoOzrKY4TSMDQJWF-s_t8hcXGm9zVwbpljNYxld51fAR1AiBxAJioAZ4UCzB8Cq5sS1RuPVWzLAX45xpdKOlX_yP7n1wRRGH-ygNNItIul1DJbksW5ChrMt9RP86liMKasTJi7Zz38OfN7sucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLoBrSFz040lClJFPYy2nRe4MSgWJUZvvxASPUa_sVlXtuVSmjI7bq3dOo0GmflMHFULzeRs9Kwf3Tln5HFKqf-TlGoRRGSPqCw_3B6dfyL8W1t6vWE8gPDOGCUMaC4uh9kAhoPZ0ouweVflHXwlb6Mw4vjpU7buMZm2arc1aBucqJ-AHoui_YSjXVaN7nEV28jU0a5goak4-J20XYPav3McdJnO6BkRpmFCbqYSMc6qeCZ3twuNKddyda4jvCJ6Iru6kolD1NU4xeF385EtUt-f6ri6zyCzMpyIuwHS94oQHFRbNmt8aD9gUojYIziiyHnkfpfE_kMBFqmBqStzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psKLfoo-FtJwAFrVbovmE_eS_f4JPIMA9LVgQCN9jZwmXUqNobGLoVoKdZN8n-R78P3DOf4S_q1zhGFBVv0-ol95jfYQJFgyA8WOht41QvjGUNsVePhreC9W9GmAseLBC7WRQpRdoVWuwexPBep3ifsXQ6g2A2G69Gv3nbZRFLJiIsWgBIiBbdghVpY7j_3dOzG0xsd0WEAPvZwwiEiCh5h2s0OcZfgy9VZ7tfx-M1PuXj3ggJosimiZuG4gengJT0ZzG2HGEIrzRZquA4zDTchRjbDRU6ahM19M311-yHV_uraldjtWY_G0r5dEbed7tzFHL0G2khIALX3y6IHLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQEheb6fXjGAz9eCkEoh9nbTiXu15gX2tZLqHepVDe2nB_XKWzmaxCCZF93RUN48APjZLQ4N5c8yJKoOZvfTpU5zP_kRHp1csn7MI1A2EMkqy5Rblm8lWOhdDzgodFKrybXRXHWg1UgEITkpcKamTlj9WysY2GJEtyQG9hkwJ3nNcZT4-8cQPeES_cYr1atxw3rQe23qZdB64GfiBaiArdQrjOYvPav8bA5fG4UMTysy1mWLjeSWQW1S8XaNasOsQfkrl8cxAvy3KL0JB6ZVQm0bRddOjaGzNv6XhlKM6cqukhYJZ-HaK_xuzXwtSpTmqI9ABgKn0TYMrPkFaNsSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xyk8AFekK1ZgQXX6-B3GH51Vl1bAPJo5NP-fQguiJLLxC2KCmIzuyuXdNWq-wTv95yES049kaKdfEaz0FHrs2f9dnJDCENA8xrRGOL987U2-yzgUpsp6ATjjHPMt14tSev5FING3dReedpDt1A2ymG03NwDFeJuXZE1SCJeLDLM1Tr425g6tK5fJozRpK259C42bOyxuxkg5VIdBCeIzQm8MOU-xCBSFSCdJLfhPgfc-lVVXT448ovHn8whAjCD9GMrOTM-m_o_NksygXSf4_31JlLLlyJw8JGSZRK5OTxwGd0uUziFjqBvacjRUyQFUAzpWykuEUoqV93RNgDPODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=Fn5PLfNWhuW-kAlodaqcAll55fQ_tn76R7CNdkPHSsO0e2T2FqeK7GxsdrBND_j5YF1gMUD8tuMTqQrYfiR0oXWvQTLl59KRCA55COlFW3srwJCnJuMFToCFhe6fiwe16vCwoki6mR-5r6-GTFk0aObbNmYhigxmxMLAB1TpQSsYYKW43hcDzprzAUt1J4WKzIUz-mtTdRgZENYj1W3q6yIv3VuX_Rngw6kwjxHueg27Cjs6KXxum7FSlxsXSOK2xOh1Z3LzJe_Yhtv7Ee82wZkJXWQPaSWVKIoPLfUfWiDQitpSQT5vQAAkdBoF1EBnhJRVo_6h4h80ITDSabLKug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=Fn5PLfNWhuW-kAlodaqcAll55fQ_tn76R7CNdkPHSsO0e2T2FqeK7GxsdrBND_j5YF1gMUD8tuMTqQrYfiR0oXWvQTLl59KRCA55COlFW3srwJCnJuMFToCFhe6fiwe16vCwoki6mR-5r6-GTFk0aObbNmYhigxmxMLAB1TpQSsYYKW43hcDzprzAUt1J4WKzIUz-mtTdRgZENYj1W3q6yIv3VuX_Rngw6kwjxHueg27Cjs6KXxum7FSlxsXSOK2xOh1Z3LzJe_Yhtv7Ee82wZkJXWQPaSWVKIoPLfUfWiDQitpSQT5vQAAkdBoF1EBnhJRVo_6h4h80ITDSabLKug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=c9wY-Vn99VUG76fBnvvanWZbVsqMdT7AREoQhhLQMcpWEfIqYZAevzbDxvk0h1U9xi0A6u_shqgs3NS8vqERUxHd7iqCXjyQ6dNYtYm_2rj0iAzJjV4sUzv6xQqvuXrcV_yltWZj2gZvmR2ae6qqThr5lD9BW70GJGEC8GgpsHzgKRqlwCmMmZ89s_RCwneMNoMesuSeX864OfmGBKwlF82sdP2B9Lb39sQuvcAqWRfWVjOjIWiH7anKRmbgQ5cq3wX1G241SXZKXSHk_Rsef8PHtyHDkodsCSVdzFJ1ccWBjlyPNPcsFOmMyv9qN7LOKNqCXpImoZ_qZAF3nEXhPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=c9wY-Vn99VUG76fBnvvanWZbVsqMdT7AREoQhhLQMcpWEfIqYZAevzbDxvk0h1U9xi0A6u_shqgs3NS8vqERUxHd7iqCXjyQ6dNYtYm_2rj0iAzJjV4sUzv6xQqvuXrcV_yltWZj2gZvmR2ae6qqThr5lD9BW70GJGEC8GgpsHzgKRqlwCmMmZ89s_RCwneMNoMesuSeX864OfmGBKwlF82sdP2B9Lb39sQuvcAqWRfWVjOjIWiH7anKRmbgQ5cq3wX1G241SXZKXSHk_Rsef8PHtyHDkodsCSVdzFJ1ccWBjlyPNPcsFOmMyv9qN7LOKNqCXpImoZ_qZAF3nEXhPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aegDHXD9ZBRBqjLj2qEK93-mQlRxWbUVS6Vj7YrgqeFj4qCrnWBHhbRVjLCJsBPXddQQF5XDfETSuHUya1otf3PFaMWE6zRFJwoZEWIEdaiiGTl2aQjJqa-iul_0josUD9QtMp-MhoYmAd95Kggu8t7ieW-zA42zcxR78otoUhQsojWZuoIWmDAg6RaARYm_1RYQmJCuotMcn807tUa0wpX_zZytxNrWiQvPcOZ31k_tVPFkdYoorxecstZB2sGN5B17Xv0Q0isz6fyjpsOJEqL2hk_KWvlxNaWkcLzmhb8Ql7wvhw0USLdd5mxxYDTkVgPHDvWNWOd5-D0Q9UVROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l059O7TOfKHJdDv8DsPu-maP6crRrY36youECHM3_NiScD9sIvJwYF4HWjwZtRdsKJRHZla9DeSdrniHYNDAbUCYB_g87YvYzvV8H9OZkMkHxrKnROiUHUsUIMTm2hBgzUl3EvoD-snH-3Is-7pblGH-Hj0_6lbXajynOKaWDPj3Bc-g6ln5PYf0QZ4lc6W53xhl8WFx1YhsAT8VLgtdVCMt4unntPweBMZntGR6sAr3WKQfeXGqoLww-BygmVB1nglqMxz9HSAltRXpGlo4qAvzKd-ksQ2fEPriG-LeOk_fQ82N1vHV7prIx-FNeHvJOpN8H-bTAl1wg5zKleI_1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdXkUT4deWX2fUeqfUAL8bS5SRyT_LiiiPV7keN2M9NMRT3TZW14ZpgK01ZJuvdUsxOQ1q0cV3o16oV7BlOGNyz1bU5QT-Lov3qGtDk7O5czBIcvn5hl5kFGFNFb3VOZZKvdmB8rIIhGzVCWhtHHeIYZfK2wkYvoQiVYi8pElSm3qcXJ4-cSjXiPbC416MpeHGVcjDqL4vJexBkyXh2UZu_34kTFWQtAjt-paMfpXptadUkcVOyc0gBEaZ5E-aQJHAySjAtHF2kDOPgOTIX6LCC9kWh50Zmt4pPdGPqckbdGQO0hMMTlY_78zsaDCWKgtoUuhQ5tr0C8a-h7N7KJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=ZGupp3faeZnZdSXKDk3ZKCG1NKhNOtCTQO09AbS6g82yz-tMJc409pb0yJD7xl5oUPAbBf2ZylQ6Ycki6DPwyqNXj_8v6wA8UlIRbavKFWl-DQ68T_o7rNGYrSWApxqj8LvAMvUUgklvjcSgH-P0y2fehNZkGvIVxw263S1dQT8Kn6K9v75zHiG3i0sW1abT3SEDERSMdwA8TFCC65xKIHe9ZR-b2dmEL4IwN5-PCyOIXsi8QAa212x3bBOOaN7LNAyBV4QjUONJrlB1IkDNMroTmY_RXubsFg3jnrtb8C8pu7W_83ivvPZChxbqgEzhoxyWgfO2-LSf3OtYgYNGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=ZGupp3faeZnZdSXKDk3ZKCG1NKhNOtCTQO09AbS6g82yz-tMJc409pb0yJD7xl5oUPAbBf2ZylQ6Ycki6DPwyqNXj_8v6wA8UlIRbavKFWl-DQ68T_o7rNGYrSWApxqj8LvAMvUUgklvjcSgH-P0y2fehNZkGvIVxw263S1dQT8Kn6K9v75zHiG3i0sW1abT3SEDERSMdwA8TFCC65xKIHe9ZR-b2dmEL4IwN5-PCyOIXsi8QAa212x3bBOOaN7LNAyBV4QjUONJrlB1IkDNMroTmY_RXubsFg3jnrtb8C8pu7W_83ivvPZChxbqgEzhoxyWgfO2-LSf3OtYgYNGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh6Kul_8HjGFV2WI7VaH77d9rONsyt7JoYVOLNVJ9GYr5KNEG9NSiUV3Pl6hoJHaDDU2n1iWzOZpmwynoaVe5fBtXpYbVrM6rjJ7y8M979OKVflfg56HQaC3bjCD4hHDiM4bzjABbKfCP6uWAf5bydmSaeKvxThDF-dWneiXYIoToRihqqlvGqbMnxVJdW1MHY5nQIYXDDSYWJhfTDWsA-Cgn4VV-w2zFC9fYx9q2YdISBVt9bSwXUegAGgNwb5Ikz2hPnhroPuyRQMWj4tnrU0wfyx3H4WeqKaPljaEp_Dlm3UMDgcEpbOQmxm4ihkBWRTTxoJDB3DMqBmGzSBv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9-hp4SIP3naSXq_fTyxXhg58kyiab5dcjiwi2bTThF79CIpfDdQY2LAqIfyKnUiE3QSmDktshdjXFhiQCNQoExie7mhfkBoYeyiMWU7jlJstDxaT50iY-Q97qj2Uipt0LMsyswKUES3Y6fdYyz4m77G3FTNxaw32YxNoR8hR4NiYn4P7lNYYjXCWQDDOMMueKa-SfEjq4CF67_zi9Ee953yE0drqhddrdKEok47CwTHajtYNfmO7_Fc2JxHXFKzWo2bWAISDQuszi4zZrKFA6xjp4LjZ-KCoxEdDZgSJO66nqV4yTobQThf1xkI_eKIVczphQXGWiFnXQbirOVohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEAn8eYt95QT-wm1BCk--zh2Ie0M6dQv7iU3TUBSq5XD1LtBDrEulXjlGtgS9JLmwYpFsrSmv5GwhKq0IXLSo1DoH8pz3l-uXtvg4vP-ekGNoSC1pe3YrpRHOX5kvA-UsAeziuWvW7hBrkuwLXjOFeyh-ewlI3ZlqFTotNlyOCuARkAaFascmqXXnJyCtCzXp9t6ncFYMnEmekwSMofDCDsAB36fboqAc5MuOtpX_1gpljlCpkhqvHPp-uz6S4qoGFoBmnpM1_aC7HDJ_TkPpuefYc_72qNbJWqEKiWmjx4zIZa9Fsgjav-2X9DxwSe06EKXkN3PdrqtxfdIA6FicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_2AERa26NBBSvDpxSecRXKXg4KOjn-B3gmvBfz38ebfC7br4TvAQugwMZYUhsY5cjbxSQf7mCXn2u8qKzbLnq34hQkBuHNRMR5ZGpMei3i8gIxf5E43gkZEliTqM5YCa8lGPoZ4cYCL4mxJ1KYNB7GTJjgSvIejSwKDJjDrOKI5GszMBJB8UXfG_HsldufGCmCaRmJTWvxgga47LDq8oj4IgzWnbggsj52SL04u4uGJA9GIzlNrh25lBn4xGKS4ehAjhgTAzkG_jcZUaZlEvC0nOj4q7THq68QQ_XEIRgMPkKCv4MUdDZQa_8OAfvhO8yhf-HDkf92Gbaz01G0ZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v68u99cGFqXIdpIkUlPVGtVq-nku4WvZdzJzKs1PafHPgBoxlYolSp-EFcz5KbJ3UdV4VCh_XcbIHKhb5eXIcIvF7XAkpNdyaKQTntSIFV34_UrYX1sVC1TOa_crMVqUXOUJCq50yz15tUGOYCGCMqlu7SbnihV2b4wEptmP5ZLUEz6bMhInY9F_Cen7XJ6IIvHpp_6jfzLM_w0pTYHon5vRmf3xsSxCfafK9lB-tu_6G4158kHf4-FmR1Llm6MkaYft9U0WUWRr_RLRxMyv14VepTdqpcEWpre7nEws955zkXaHK85Gv7rG9DVvP0eQosa64nSMGfzm2hjVz1WI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXaFp9AF45mY1M956j6qDHZryrYHwmLPhtbPOhwF6I7O-CbKIhA8MmMXMBNG0AEsFeta7TzZENUqlWv3VqQ72naEp73bruhzlckjwgDtuRAOuoznS6WC6n4gAGzGM1yEjq8btekgoLATP-6WvyXIwGSPTTMzs0nrDYRSh-usV3ZsXe583q8MYjHrITWQGIT6re9PCx43HErG_mBdBwvYfF0rgAI29-Jzn2T0g984vtB-LNzl1kT_d_xgCtqJNIxkc9mqhYROggopOBvKDctqBodlhE4NxektcBukWQVA3kV1sGEuSmr2zR1LRX9gdl6lUDa7JxP9HGWWNQbdvTcGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWs2Wl2FhroIggs6Mr6En6Fmv1LQgu_SH5vq1xDK-oaVlZpx48DkutGCcN5Ig5-noSyGqmc1IW8yBtgXH0tBGf2OpcO6tQ1LISuOiHtn_LQ2dE4MpRM0E9YAM3P5jzo2K_OU6MjzQRTWrJrkm6AXcLf-10AFBge1wnzLOEL7dS6D5Zi-Ga6PG-pl62uk-yLihK3-7hLeeXSXHFG-ZCfDnkr-RWXg4m7TKo3vHZw-fnbgJgESYwTZlJnRz6vqon80cPYx3Ouis6etpTggB2FvOWScEhQKOq26rlq7ySGVBP1_yekgDRko6kQnIRuDopHtI7Q1ojWEyMa3vHNus0Jkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0ng3BmioMnF5WtvpXP3Wp_V6JMfPlTXIBAZPqM-4DP0yKvwipwPD49IDkJEf34D1CPJ34eCJqTRclwzZxORuikrws1Kapl6xu7uzk6rpBAj0_zJIWlur4SQJeIu2PXxoNmf3kj11P897CZRT03D22PomYa6hBwWk0DXIQkGLWfpdDZsSECFujNz2_5_W6SIAoQVE9guCaEgnfjJP_UXUiwA10dW8Z3wtf_oDZs-VD9YxDV6uh9ny1Q0H1kH0bCdyU59G8JMS1XTY20AAZG-nEz1XusMpWoIjYVMmQ5E4jMgdVBeCv3X4P3jGhKuRY1-l_QalbjzZAUyJiYs3jh0eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buqzQeVFXKidFl3wzagY0DK6_ynTshPJXLEH_x31jxGpIpa2CkhDBafKd0QqRXQW655uI19wpZ0TrVBLg9L2OG2WuffijZFcPamA3Nd38Yj5ug3SBcTXF3eHpjp6Otm5Z2sQL0wqKP-tMiGJQyC6CVx0bIJnw7-2XR9XrrmnqEM0Ax7KXSAYk50IcYBCre9lUsrQFnULPsGT8VGOvP6ldsckhLHd7PIGUtI60qxblcQwfPG5YF5nMROXR5HkKKg_3Jj3Zshp0ZWVwNRCY34At9Q4z3ZZNIw0Axx9Kv_3Gu1E2NbEBSLlYiwJjwA7eMMon7PTbelVC5sp9wd8GL-_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf0zfUKwD26adNl6AndatQ56W1GGtCjKc2Y5YYoovtKpE7RHy90Ejb-_fWfHLYx1YdCezpuU2wWrRZeRLHI3RrqNEFMoy2PaTvhwG3giklAg8dFD3NC7xZNtK2skND5Z1MaZ-udCzbhUcwn5UAiJy4dLmNZ7tqJOeykhLHr6YFH_72kvLYoTOE4IMshgV-JU53qFfsNfp9CJ4-S74ZNXi24jiVxBfCpfR_8g7b0WHpI9rCPMy0bw88Zhq3dNpkODe_YPI1gg9TrWHAM8jKTW1oxmMacEyvF-AwLm54G5NJopxCqqtwRiAPvjbrf1aV95Eh6uxglwa4BC6vj5GQfvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX4GG5hvP9ua8gMrz9plEBYvombWOkOxQqTqw9rAzL7VFE3bz9f47KYbG8r2T6bAseAZ6FcWHbWEPGCo-YqUSnQTBPWQ8bJzHNFbDWAheAlOcEUejlMOkevWjxvTiOisqSK5rwWTuK9MUwUn3vzVgkqZmnsdC-4_8bCGC08HI7lQhIVeYbY_7lxg3UDueoZ2ssgigHrTVoNdbKmtRh0hdeo_R5JPYwwSKKOOGuLbqjb2X1k95fCo946ZOvzKH21aSPQcDd7VkxSI1Z1wkpVRCnLcCp8MOa56bs6ba9e1koxD_aBEzN8FOcm3Inuahl1EbdeNEyvIvCsCsiS1zd185g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jI89zspHFxI4v80M5383RXNf6PbxcYSzDo_Nqrb8WYFy4owvi49FSy67b_SGLyvXB32LcPyqROrFjfZZVtA-Te1ZzMogxkugOZZ636vRTgMxExgh2CmcwTIRGKh4QlxWVNUhDm8Qo6SCodeKIRQ-u4r93XvdIKBuqeizgT3OQDre2rsDMx9uMr4RJT4JYK9uC5-PIklgWaD78XDFZtsE5YusmUZ9rVbigRXD76ou1t3l1FPuhPDQKcgG0axEz4elfOyDpIrz284_SRGrmfvyo0msfa5vf1mfSvYiTPIJhuA4CQyt3tAgKtevwdaHeNg8iJTeV0VtntH_4X50wRZT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRBy5a1ef1hiHNrepu2_ma8l0XLaGO9_3STJnrbMoG0JK8p8l1IXkBZiBk869YdZlPSOxhCQpsDG3NaiFOa0pFm9_C3Olkic9-AWYLNGqwXydKHAnEBWBFk97ePYF97LXn3pWRtHXwMGRp35ywEyliT_Du7TqL5jovbDI0-8fDTa7MqePh1UIMc7dIHFhX0ATJ38Lrvf15yPJ2vj8bHk1KqS75PiFqsRBkCZZFqpVl4HcPiQLEz53f4-SoI3BBZ370WF6lLHCFl0tvMVpJHIKROSO-YKpLFmSZUWwqE22mVbNXdIK1LiccG2sCo02XD8vARwGyZkBaBsYKiiBuIpFd-HU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRBy5a1ef1hiHNrepu2_ma8l0XLaGO9_3STJnrbMoG0JK8p8l1IXkBZiBk869YdZlPSOxhCQpsDG3NaiFOa0pFm9_C3Olkic9-AWYLNGqwXydKHAnEBWBFk97ePYF97LXn3pWRtHXwMGRp35ywEyliT_Du7TqL5jovbDI0-8fDTa7MqePh1UIMc7dIHFhX0ATJ38Lrvf15yPJ2vj8bHk1KqS75PiFqsRBkCZZFqpVl4HcPiQLEz53f4-SoI3BBZ370WF6lLHCFl0tvMVpJHIKROSO-YKpLFmSZUWwqE22mVbNXdIK1LiccG2sCo02XD8vARwGyZkBaBsYKiiBuIpFd-HU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b09njUTAgHdXh3RK8nEqZggQHwFbSoXLXhwz74FqTP7fwzc3otUjLX9nh6GOx00zNAFqLlZl0_yBGxSNRwwETSxkMOZ7eZ5NyybZolNVmyvAt0swXK_WDHsbMpuV3FDD8G7K1JAS2i5soqMg161N7eTmMLLhuHWh6IJSKcr0-nJbnufr2Sl74LLTLp52oaBPVluQwYgaFgPUJd0d6FHdouTkKPs2vpnmw-CoQNGUcWbbNtS7enof_1A50VaTpMEBWF_RqO1A7AU35C9BaU5MhO2E4l8haLB3avdd2wvioARCQBvyQxi-uh0Mk2yqiDLuLlzLirIJoKhOs_quCiHS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS9u8QKxGZjXjbn-JZYXqJrb726_7taeLv3V9ZEPkcVJi7DQvCEfQH5NhoWhE9BSjP-FFTd149weXW-k6HrTKI1U1TjeiEYiu2hgcqLmgd_3z6rUaKF-LKt21qiWuHxlxdJRoZ2GZuQ2pvpiU8xxs6o6oWiTHg-ttKa_W8RGO8Omo4MdqIxN0Nec1MzjTSRwYh9Lv_a1F8z58N3tw7rbCWfug1CSL-VNGPCOhHtz8I0OSCn4PBk4izogd_adVNv8UFL32h3yKetWnRjrzz14ZTPdylqMHA9HAc34Og_7USZ6lLhgGEvfM54ZMotjsJdaMpzuuFb0cLJmyjei90Nnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gj9duF0uON4qK2WbAU3YZJtJFX9ZzTK7DzUaa50VDRvgkSPBnfqFZZmyGXYglUN_oOC4wRWfKyh6zRJO1PAirHigFBtBtQvk2DgO4qosxe6vhee3fBx9pf2IIcXWp5QJFz2v_-8DbCId3wqI9qFTcNAqJ3jpyinCMlw8TNwcIAyvMMhEbdL8E6-0EJTWgx8AhgMGxdi_L13GGP0S9wRryN4K4_eiP-KE94dYF7dy6Z1fPVhR1ocTu-55rLST-3OKTyWNnLQ5RBNgWjjPWtqeNTK0zu27bjl1n6cqD96HEwgux6loigcENWYr4ljTXoHC99o_iKSyOEenPNtFbvWN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URC3cg0faA5tFDa0EZcPSWlNbTJDqlQe4kR9huOE4mHQJ46BLT51jxEQauTwhqXfV4Fy2tldMLvv7omHGBNmJwLclFgcW5vb54igKVjslB-wY5QJ_OiyFx_TtYHktoQZZg3oMuug_oIn0z9Q6SzIFlFfu24B4kNdn42p0J2Nldk7q232jPgL5l4KnEACZPHwVr2c16qN47E5HhWyjvOV0u1QMQgyXmzj1xM_FZDBIAtIa0EBRXHki_7eBi0GfIvxvbB-3OIYJ4ZNHsC-oiGWMULJlHgcKT6Rg_EDYq6f2avPTWZIAIIWt87zwwcgJiLiY_okz2QV5phMLx03S_tagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_n0_-q2hSMuFr7QdhaJtIcaCtJ6xOIbwtBUMZGl8h5mOTjqAigVO9IicD-5er0SYaCnXaKwdb2ngc_u_N2Ku9ZknbQYQfAFy1DC15ttNoDRsTIpKr1vHeLmEEXhW-iCtNoIqhbjCo5SyD4X_6P6fleojRDGoYrfRDvwiWJ0yPQtYZW4BNED4BigDiIGOUB_vdD9e_3VplPa2PaHpA8WYF-TGS931nCO8lz5DOG5mFTWEXlwBmVme26fmVNqvqTOUwi8VlmFEu0Pf83VcxXzNpLk0tOtDlqdKceRmHDoe7p5KWqDoJhuSc159rJ8yjMwLnXFsLHqblrhVFox7xArOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtQOHXtw_1TXTX11cQgIWPnTQq4l30z8gtZmsw1zYH-xgvtGRsv_xIfrP_rIbEFQpkNM9CmRUDxALIsD58Wxjeka61Y8RbLh5zterrirMHhUbLYe-fXbJ-F-oRcvvgvjsKDIN_4vwv_IqdLt0CaAon8rAPY5qC__B8O3O5VbA9mxbVyvL7b6-i5hhcDQsJNatmwqjhCfFbAje6DvbdwR4wdtBtVcRDl7NDDCNojEnC1sZm2INzCwsuipYsZqDrhJlgyAgHllHlBJucBTOEKZoXDWYJWT6zSuAQ_dH9HyvR5eYm7p8YOVjr64lmJtzONCZl0J_daPOpPi7NvYM-Ycdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9vwzGdtMo9XgtBjflIJAHadNUISSR3WXFLmNLewVKcCpVwQKY0ZEhPEhu9O_WpcBKNDR5MqBgp8r6w5A1bGocq9MGDVo7UYVBdhQMMDNllPYY8gR8L294yGKmtnucTGZWAXjpPHYjK_hDVZYxRtsJQbUZQDe_4sYEVxSlDHrT7YHSQOP1qQ4EHLlLRc7TBiCGFUS8MIDd4b1LbvpIWuz1T8ilNFKr7xhhQRNwTjTPB-N4B2uU2pogzsEBKxIp96bcl43N-grpD2Mcc8qvLMeQFEbYFQ2GGln4h5cuxHvssZIC1J9nSmp4jmj1a74M_i5KU3Opfa-blpdaMRVfkJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVnVRNBL3zWVFDhXt2bP4fKmGgpskIbiZLzBXtJNLKQak53M5I1_EKMVwkRz5YKsb_40tHWnekkZBk2z-KNfwssxDhLvFIK1_TafyxEtVNrv5rNULgbdYYcK1Ob4oEU4GKk1Xw2HQWW99gk8VfmjG47CQOwylVo4wNO0RycGCWYELRwrERiCMN9q7VldpHj5BhvTHeXqv7mTd3NT5JMygRbHuvjTBW5rdVeMItjS7s_RYMzvVVslLOyvO1ahVSBqvJiVNKkT6cSa_BnddNdmxUU9wjODT0aqovMpsrGfq3tV_Xc4I9SuXfMm0HAos4A_cO_HdxZwjhRJwhvQoYA7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0riWR0B0GPeS2vjn_OBOdMvzA2oz2QN3dAybPmiivEND6442Y78AXamGbAdIs731qg25TfKQuQ0C4TdCERoNByCRSe0VYWttzlZEFOB-mMF8gKlZZbY9qetdlsyb8NJI3tkn_fDhe1MomCZHTtXw1tKNC9COl3OR809kTmGZKP5h8t_uW_5Ff7EKpyEppXDCfagWkbrbpFh05sW2aeug_5_5jDuUCDhHBi6wUEobvqB4zn8GsHY5l9WVWJiSZxU6RDeOR2hQkyAK5m3N29ONP84U-YwODg2AX3QgbmC8MjnWy68Sck3WPiH-vgBjQHfXU1s4NF96f0R-c7WE5deDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqxOMBqyLD5H4sUyiV4kiyjqtsgWCP8FFwHE3PGS0S3X86YhYyZUQVhDaVh7b2McbMIctQPeODtVXynKCTcs364zGBiAYx_mRJI8uEUx4mDuBCycMARLotjp-wRA8Paa3tdRS1i13x6XkoSHJxcxy1StH3Avijebx2h2uelQ6Q4isXbErsnhyl4CPKLXwYWR7w3CK5liFpc4wmtkORlvOyySGED_kO32QA9ii6_2QcFgzdgPnxZTjGPYzCeS689v4Qb477Bv5exZRNGJ9QQEsTznd8--z965UaFOGT1lSjMJarV6DE5iVWEjMWq4hbP20k6E7nSCNqU4XMr-lgzDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMFjoRrpo7zxIvOQHkXRru2v6rQQ4rSXFflq4u68NAownN4rcKIzssnS4CLNo2QHyAKjjg-024XVTt-ESikom3i4-0IC79oCZ_Ij69M4XscmKEp67TgHkGfSEv8exmyWtFRvNrZQCY_XLPaFDmH4jctDn6LR1g9PAv5dwnj1m99ka5haatWFa39zWAMCwsa4frKHczZJ6rCahthEfRxZ_nEwjb5rVovwyEeiRpRCs6iHPYRI5L_3x_gCh-W00PPAqe8ZBdqFbgTYKYkZRfdy-alNe-i1M3C4M3cGRk_VdStmVbxcnDlyf67AroPyZCR4y0TvChHEvuI4KaWSEscjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0s1tkeCDAbK-m2UnwkwVzlKGraclPm2xmy4XQ_AWF4eLP_U_YIXCvk0MFt5L1tyEymkDXiNXrqwb0khXrW2697V9QBCIXzK_dex0t4xEhmTgvPXmBjNeNkwqXVHgmJEIpLoxURi9Y52w9KMcEot0q2jHzk79CxFW0aFi6OnjLwBsdUu44rtCBLw65lax0g8E0suzPqRuFsHhQniS5ovHPUqwzDdJigRf9TOKyDv1NGyemjbSE3Y0AJm2vznErOO666otUjUukfINTLcanHMjcRz-QQn5-5d8toZ0BtWWoPMiCeTmjphDtrKPPpg_ZjGYoHmlc_4l5PszH5Izocdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcI5jvF84qb4IlPvTXAzv21pYI7fTrVVXIMSK3ICIOLiufvWGFd8nGipsGxZGWpEi4XIgjMmvTiltOeawbii2qfdmyfAWEpuF66MZeJrXlkUsaP_LSor-7a_d3AF8mYTXVR0qDHOW-PjonFF87qYhIYzHyd-q4MxqIbFa_2nEICTg9VJBw3mIKqcgDZmJ6IX9eHXs_jac3W0rgBjxGmwdCf4o3TTo46OzKzLNqR9BV2DhNmpJG1CT1c6welgbNYKplelSzIH_KqEAbfXK1k4hA-HeWl62WhxdzLxcCvhTM3QObDyEMGzIIk-dZnVbTRVzr6xygyqQ9lTPNkGhf2OnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRP77EMtkGjvs1FGTCazZUaZz6Rn0A7CSxHfbfGIGJIPoDfvsah3cnAIx1U0L900rRFzPOa2xSwZNAe8M0hbXWevM7R3gs2OuSQJn86e89F4pYnaCCrtDhkIW1QypfPJdhOjd9pEI8YybYKhiGOdI2wh-QfChaELh3S2Z5vBZbeR4wgBBKhmMpubEApK187QOeW-uNN8AD6cIDp6haqXgrSIZ6OeRbp0hvu6PEhThxIoN08gSj7Cz8gWHu-pIvl28WcP02A-iPhtLU5xpNqe3UkxyzbS9Yej7y91WXgLAmoSpekzrDdfmxffBZaG3kRK2P5TR9kW9_qvqU3Il234QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmglajmAnS8d9Az1T6Z7d9OjQk_K8TS1jNZNQ7U3qJyeJZf86l6DeBhU8yhmKAsjIaciepuGUdhWxHrN20mtfHJIsPgExxxD6fal4TkVDAjzc1t6cN7mOuKxqlTkQm46Lcyv6jd3mtNFRTPgAW-TVkREKh2K-j3MIr4RCkq85YgewVWfD5Dy5q2CxcRrThUX5qqom3-YPn9jlSlY2thFFm_kDKEdgraU-QeEt_KKTQGiGHJK-oZy0CWJsTkHC1ZNKYg_Gq7jLU5P5PTZ9gyPZHEby3U467HXuloP6UoU0ZmEBp00bEENMosxOMg50f9TNX2YEJ5HXzEBkVnLoVKmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv_uleCr3-Eg7xIJBA-HAS6g2fHHT9ClqI8_0m5DrkENPZrSsz-CVnLiZp888a_pAX5sOmWGYmjHvGH6qfoNps80VdjSAmft2ifVej6wQ1nU3g5rjuoK1G1m9lewo8t1BIig51ZA7cfWktxaUN2YBlCawyLMzDPasZCMtoziRX66_PKce6tqC66PcGYlsfXQoi6eoSl2zK4gswnbgCdgIHNJ1a_xyxyb6H6az0sczP6CdzK5-Y47IgCZfnCZl-0euaWsECAF9HUYLuKyCpONXwwsKVJWmi60F2MEqhcUct7f_XxgbLkl5rNSUefpsoSzVpBreatZBkmt68AXHDNhQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeKV6muvRcIi6lDgoRQsW8ZV5e00gnzrqWAC1YJJ57hbXj9VwZoXN5rh5CLwzN5SjVnY117B4l2dlz5TD6mgk1R4VrnUiMiLufbit_NTjfiSK81IqDy6z_EAYE7EiexEOX33wzBhm5nnXx3j5G8xclf5CIiXXKzgBS_BMABBLbPLiuHragwTOeyt50t6P-ms7c-U2tWtsRFzYh_4HD1WZAQt2rCvERWxtHvg7OBg0sfEyNuQuPDc9mjOoN4wztrRxDwCPP0mFZ8Y5mt82rAZnbu2UJZ7hMxmZi1I9-dpCKq_vK0GiXvGAfdwJ3Uut-ov3NmVrogOXvE6wI21l1lz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9JYREA-gnIp34BB7ba2HiGFW8Ik69Nw_CX3ZqzONMbR0O73ui_fv_zEEm5H-eq6-U6uLkXDyZlVXsOKT_MroWaZXXQI86KwoOQ6NR6Nbl7LcrKNLJsuwh7_lFnsvLfOC8Iv5Ey-LvE5U_oGumwMgfNBAu8hWsblRPae-5TonT8gEgyPsO7EKyls1ojCqcmvB2mgzDqVw1EunQ1EcmFG230BkvUSUnQ9yG6tU7jiz8F-wTILrioAC2a1e4bqytTKgwvI6zo_RFgzedme_FUu57OOyLqH_E5Ts8ANR3I2sz7fBPZhrYpcBbBEiLq4YNekeqDFYTM7Eevd7BEVJd-D8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlEQJ1vcUqxHExd0FK4EDaTI86X2xkZKGLbZEhaYQlOpN9xgs_JUdAU0RJw5rgfFNHFX34PjEhGq0CZuFiPv4yiXiXO9vEMe2aJhfT0eV2VNHgMCBZEmDf_NOmcppccCi8YYhz14XZTZy2LYFck8R66HoHWE-wcs6nd7JPkcQiXN0OpRf0IrTVWyRN0xf77N3t13uzaTWK3-cAvGNTOet-NzCcR1_WRBkTGxEw1UWR9JUI4EW2Q05ugArqsSuVVsAnv-ggsHqDhgNFHRU_YTLVnqmZ04TCWM_zsMepFdlIJI9KVsdD3pQLM0vxHz50xq4pOFM0caUf4C0QR4tcNBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwg3WUjLr_k1TKwimPXvlXRI6TXMOUcpsYbkKvOu4OEkFaM2JOYX2bScnWsk81A6X4-KrlGHUhdREi4Y0CRxQYJy3vbL2xCpI1iIPiR8NJlbA0o2Q55bVyw9ivTkb1MLJOvk2J0zfFHoHBV4g8ZZPQ031nMwvyuY5Jk2BWhKYDewOD2SNkwmDMJhgvy1AJL22P5xMcBFBXB5y4ETsDDnAeDfddQPoMSvYhYrvB40LWA063LX9G9hCJ5fIBKVlucgvw2s8lrGELKzK7bgFkBWCaSA37F6FaYKZABz_QtJtb2RJpYHuwTM2TRqJTk1L_Sv7HsPqI-CheEuNNf55iHOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=hwPhUFNJ-dFQ2SB3ZiVc003CT_v2VYK9UZmEHPV8OpE7g0aHAsSzcQxO8_pY8Auq4Dsx4pV0wJG5giTq_b6rZR4Zyrz3yp8DvjmuuPnTTpJYfkXaFaVzRNG85uK3ZPL1QDXMKFjBWorRyctViwkF3ULP4xjzq7UW4okFmf1NM1-sLQjOmECkfwYvyJLECTw9bZckDs_3heyP4uwC1kW_y5G0w7Sk2TZEYM5Ymp1t3lkW8ODkOEG_bOSHk_UaVxIixB4nR-S8_0u4wFkqcoyYJqTZrmQzWRGP8dek04MwclEkSDyaJriu02TyCtEc_J8w4xHGQqN814zTRBdVc76yVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=hwPhUFNJ-dFQ2SB3ZiVc003CT_v2VYK9UZmEHPV8OpE7g0aHAsSzcQxO8_pY8Auq4Dsx4pV0wJG5giTq_b6rZR4Zyrz3yp8DvjmuuPnTTpJYfkXaFaVzRNG85uK3ZPL1QDXMKFjBWorRyctViwkF3ULP4xjzq7UW4okFmf1NM1-sLQjOmECkfwYvyJLECTw9bZckDs_3heyP4uwC1kW_y5G0w7Sk2TZEYM5Ymp1t3lkW8ODkOEG_bOSHk_UaVxIixB4nR-S8_0u4wFkqcoyYJqTZrmQzWRGP8dek04MwclEkSDyaJriu02TyCtEc_J8w4xHGQqN814zTRBdVc76yVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
