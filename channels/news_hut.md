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
<img src="https://cdn4.telesco.pe/file/kSSYCMxRQ3ZabGWMtc8p1Rp023JJtPm5kAYcFjrM9zVT4SNACixkbA8cdT66mQUl8UzwYU3Yl_VqRYa4UOO-PDssssI3tJNoAA020W5ucMEWtF7GIpQreeoqVJgzfsqyYbuLF4ziGCfXo7xxBUN7Ff-xuuu1gGB5KFa_YP7K1pewm4WbRJCiCWRmKOeG0sxqGo9cqqPBVqCrLwEGfL_Mo5mT_0zYjj81ndUiW6M497nJmFq5O7h3G8NPhWB45e9xKj745-t3NUhMVSehJ-Y100deKGTZOIx5SB2hQVpToM23XjDeMNTyUrr1_EqDVjGzkSeM39Y7G9Wl038qciBeAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 224K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-66206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=ErNE6wkOdVnN79NlIbiZuq7XjH3cLR7OfeAYe8Xrx6ETneKAMni8nrg70zdLKMJf31hf8pw1s4DG9i0PEwc_PhrqLibDvkSj6Iruc1Fz5BeXrx_pbVvGPGyVguE-W7v1yIA_O6oTxRLsgQBkySqEkLvQy_yI3zt2NqrY9J11muQhIUwWg4iCeBQTbuevwYcG-Q0ecUtL6mPGo81nxE1z5bYxIHCDZQdrymklkXT2n3v34rgsMtDZfRpLP4xkAdSNVMODHL93bX-bJAJxqDxYd7GAAtQp1Jj-_udFtY13bskNXLzGs8SRDZdBgxmS5vQ4Pf1t2JhhvChz4MIWgwzHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=ErNE6wkOdVnN79NlIbiZuq7XjH3cLR7OfeAYe8Xrx6ETneKAMni8nrg70zdLKMJf31hf8pw1s4DG9i0PEwc_PhrqLibDvkSj6Iruc1Fz5BeXrx_pbVvGPGyVguE-W7v1yIA_O6oTxRLsgQBkySqEkLvQy_yI3zt2NqrY9J11muQhIUwWg4iCeBQTbuevwYcG-Q0ecUtL6mPGo81nxE1z5bYxIHCDZQdrymklkXT2n3v34rgsMtDZfRpLP4xkAdSNVMODHL93bX-bJAJxqDxYd7GAAtQp1Jj-_udFtY13bskNXLzGs8SRDZdBgxmS5vQ4Pf1t2JhhvChz4MIWgwzHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چرا ترامپ مانند بایدن عمل کرد و چنین توافقی را امضا کرد؟
نتانیاهو: من این مقایسه را نمی‌کنم.
ما هنوز نمی‌دانیم توافق چه خواهد بود.
همچنین نتانیاهو درباره انتخابات گفت که قصد دارم نامزد شوم و همچنین قصد پیروز شدن را دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/news_hut/66206" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
نتانیاهو درباره توافق ایران ترامپ:
این توافق توسط ایالات متحده، توسط رئیس جمهور ایالات متحده، حاصل شده است و او معتقد است که می‌تواند هم به نظارت و هم به برچیدن برنامه هسته‌ای دست یابد.
گفتم: این تصمیم اوست. تکرار می‌کنم: این تصمیم اوست. او آن را رهبری می‌کند.
البته، من نظراتم را در گفتگوهای مختلف بیان کردم.
از سوی دیگر، گفتم که ما منافع خودمان را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/news_hut/66205" target="_blank">📅 22:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما ضیف، هنیه و بسیاری از رهبران حماس را کشتیم ، تقریباً همه آنها را.
فکر می‌کنم هنوز یک نفر باقی مانده است؛ او هم کشته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/news_hut/66204" target="_blank">📅 22:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
در ایالات متحده، می‌گویند که رئیس جمهور ترامپ هر کاری را که من بخواهم انجام می‌دهد، و در اسرائیل، برعکس می‌گویند که من هر کاری را که او بخواهد انجام می‌دهم. بنابراین این درست نیست، و این درست نیست.
این رابطه بین شرکایی است که مدت‌هاست یکدیگر را می‌شناسند.
بسیاری از اوقات ما موافقیم؛ گاهی اوقات نیز مخالفیم. این در بهترین خانواده‌ها اتفاق می‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/news_hut/66203" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
من نگفتم هدف ما سرنگونی رژیم ایران است
بلکه گفتم که می‌خواهیم به ایرانی‌ها در انجام این کار کمک کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/news_hut/66202" target="_blank">📅 22:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
نتانیاهو رسما اعلام کرد که عقب نشینی نخواهد کرد؛ نتانیاهو، در پاسخ به یک سؤال:
«جمهوری اسلامی می‌خواست ما از جنوب لبنان عقب‌نشینی کنیم، اما من بسیار، بسیار، بسیار قاطعانه امتناع کردم—و ما این کار را نخواهیم کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/news_hut/66201" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ترامپ توافق را با جمهوری اسلامی منعقد کرد و این تصمیم اوست و ما منافع خود را داریم
آمریکا به تصمیم ما در مورد منطقه حائل در لبنان احترام می‌گذارد.
روابط ما با ترامپ مبتنی بر مشارکت است و نه بر اساس تصمیمات تحمیلی
ترامپ رئیس جمهور آمریکا است، من نخست وزیر اسرائیل هستم - من از منافع خود دفاع می کنم.
مواردی وجود دارد که من و ترامپ با هم اختلاف نظر داریم.
مهم است که از منافع امنیتی اسرائیل به طور متفکرانه و مسئولانه دفاع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/news_hut/66200" target="_blank">📅 22:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349807e03a.mp4?token=DEdy2cXzf288V5skbmWDY5QmOJQX76QCHzesEFeErw5d_yz_SNQdpBrb1jwBx8VtXIAFlvXWwMOmyvlGqGcr6iIbIexjIgZpDYxxwT-5VbRwCU0_nffRpqVYX8H8QxMV7wr0Cq3Uyeob7rZ4GRE5iNrWLhlz-ff2UEjuh5THbKK5yZcWZ2NDZocxuvWpRnVAaf0ewjUkIu2GkXsVLl1sy_R90RR69POONMtx2J4sTpGg9BReCODDknPDJRNFdI8EJoSFEyxty2pFS5AC3DdGq9JeL9g3zuZ4At7BsEX0E7FNruJmkdxPMp3Hp7Kcht0qPnxbsd6NMYnVCcL0e-uLbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349807e03a.mp4?token=DEdy2cXzf288V5skbmWDY5QmOJQX76QCHzesEFeErw5d_yz_SNQdpBrb1jwBx8VtXIAFlvXWwMOmyvlGqGcr6iIbIexjIgZpDYxxwT-5VbRwCU0_nffRpqVYX8H8QxMV7wr0Cq3Uyeob7rZ4GRE5iNrWLhlz-ff2UEjuh5THbKK5yZcWZ2NDZocxuvWpRnVAaf0ewjUkIu2GkXsVLl1sy_R90RR69POONMtx2J4sTpGg9BReCODDknPDJRNFdI8EJoSFEyxty2pFS5AC3DdGq9JeL9g3zuZ4At7BsEX0E7FNruJmkdxPMp3Hp7Kcht0qPnxbsd6NMYnVCcL0e-uLbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏نتانیاهو:
ما تا زمانی که لازم باشد برای محافظت از کشور اسرائیل در «مناطق امنیتی» مختلفی که تصرف کرده‌ایم، باقی خواهیم ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/news_hut/66199" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=R2DCMtqZYQdsCSTM4IteP2QImpaArnNf_D96c06cuaT_oUAgLbuFBoBDEajFlFrCR8LKWYkv-V094M219mLIjisFAapPUENkTk2yFQ6GzaXGAZ_DiLvsuoEkWeQO34XCxSRstOfejUujxyct1BSkWxouO1yspUPbkoT1eHy3dZGSzcJpF4fOXwwi-OAFGk3Dit9eB-4yRFvMcrPtNVNpILdKnW1PY37V7MQfn8uPrwL4V0f2_owC_APymmY0J2IewR_O4Z7ieQzBSspDGKN42yltEiS4W6ZD2-JInCUHqethu-uBRReW4EMyIYZLpQOXdlHxDtwdy4jOsTbvxNK-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=R2DCMtqZYQdsCSTM4IteP2QImpaArnNf_D96c06cuaT_oUAgLbuFBoBDEajFlFrCR8LKWYkv-V094M219mLIjisFAapPUENkTk2yFQ6GzaXGAZ_DiLvsuoEkWeQO34XCxSRstOfejUujxyct1BSkWxouO1yspUPbkoT1eHy3dZGSzcJpF4fOXwwi-OAFGk3Dit9eB-4yRFvMcrPtNVNpILdKnW1PY37V7MQfn8uPrwL4V0f2_owC_APymmY0J2IewR_O4Z7ieQzBSspDGKN42yltEiS4W6ZD2-JInCUHqethu-uBRReW4EMyIYZLpQOXdlHxDtwdy4jOsTbvxNK-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما آسیب عظیمی به اقتصاد ایران وارد کردیم؛ برخی این خسارت رو یک تریلیون دلار تخمین میزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/news_hut/66198" target="_blank">📅 22:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=BNTrEgfa8cPpdiaPNyBR6YVAmutoB7BmIrzI3LFJurqn33CR1ZzRRIqlPSGEhdoWR83T28GtYaMsRP8zhTf35KyRJqRVv2hofR3TFZHV5lI7t8wAF6XBhGudu6MUROW-JAs6dSVFPws39xAolKYIyLWrZFsvSsKWAt1uwUhxfhzQ1ncwDSpufvmZBrGVHr2wcs2xcphDWTkl6njtBI6MC6Vfksm1aCWpVjBSDgmztjTgNk7AjoHiEgW7sRyyCbniP5CSQMxVcARXgLxwUjup352F73IGRzUrLTTbK2PxJgSN7I0Q0fdZkmNs1C8dPMeHc7bIN0k3ZiQyp4U56ykI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=BNTrEgfa8cPpdiaPNyBR6YVAmutoB7BmIrzI3LFJurqn33CR1ZzRRIqlPSGEhdoWR83T28GtYaMsRP8zhTf35KyRJqRVv2hofR3TFZHV5lI7t8wAF6XBhGudu6MUROW-JAs6dSVFPws39xAolKYIyLWrZFsvSsKWAt1uwUhxfhzQ1ncwDSpufvmZBrGVHr2wcs2xcphDWTkl6njtBI6MC6Vfksm1aCWpVjBSDgmztjTgNk7AjoHiEgW7sRyyCbniP5CSQMxVcARXgLxwUjup352F73IGRzUrLTTbK2PxJgSN7I0Q0fdZkmNs1C8dPMeHc7bIN0k3ZiQyp4U56ykI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
هر زمان که لازم باشد اقدام خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/news_hut/66197" target="_blank">📅 21:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=WQ3lemmaMNj74jDjWyRKljRc9aBkTHEaCI_8cp3Az75pBqAtrucyr4aN66YfFPxmG7F3csnRB4fg8NzDX-ttHOMSr6ZW0h77Q-TSInNN-CKTZblUvGy4XbmpJX_PATFBrsO1y-TQ5e3qod9nogoDBCjmc0BsxL-gvZUPtBh5XzsgFWKnWl5XLyMAWg_956-ylJdPmIcl46y8Ymq9UTLKo65zGwmZzB2zHY9EwRXu8zSVDYXnFMrKYKaw8SnvjELOq5hQaxsX0sbKDRtIslhPPJVCYK81A_ZKdjymYAz49cMoeR9yEZ2x1ADI3RkyzRuvOUPuwuk1OEhMbt82nU5Mpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=WQ3lemmaMNj74jDjWyRKljRc9aBkTHEaCI_8cp3Az75pBqAtrucyr4aN66YfFPxmG7F3csnRB4fg8NzDX-ttHOMSr6ZW0h77Q-TSInNN-CKTZblUvGy4XbmpJX_PATFBrsO1y-TQ5e3qod9nogoDBCjmc0BsxL-gvZUPtBh5XzsgFWKnWl5XLyMAWg_956-ylJdPmIcl46y8Ymq9UTLKo65zGwmZzB2zHY9EwRXu8zSVDYXnFMrKYKaw8SnvjELOq5hQaxsX0sbKDRtIslhPPJVCYK81A_ZKdjymYAz49cMoeR9yEZ2x1ADI3RkyzRuvOUPuwuk1OEhMbt82nU5Mpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ما در لبنان خواهیم ماند.
کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/news_hut/66196" target="_blank">📅 21:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66195">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
درگیری شدید طرفداران تیم ایران با مخالفان تیم قلعه‌نویی در لس‌آنجلس ساعاتی قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66195" target="_blank">📅 21:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66194">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0695d77536.mp4?token=lPJjAnV0S3orO8SQenVU0J9LvNExLUiUOBoa2wxiBp-Aac0qfs3pvoOrI80zz15XMTjUfKyQwlmE7F0dFOF7Fm8EtMW37S-IIx3SKjDF21BLXHDW5K0NiL8i-H5PQO6wup-NZlc4IcCmQK508zrx5je4ntAfZHTkC0WNXFj_bfjbbhBRXkU_SsaHAp0STCJwMZq9iKy46rKhIJBItspsBF4kAoGul2-2dWDRxvDWefVRLF5WRl-S6pDvZFoI4mGQgHXVbG0ryOuwyjwAQAACeAFQipmuX4mOD46J9UjdplyweumdJf_oaImigMFwYQPGkCYNoKyMQevTb12keDPB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0695d77536.mp4?token=lPJjAnV0S3orO8SQenVU0J9LvNExLUiUOBoa2wxiBp-Aac0qfs3pvoOrI80zz15XMTjUfKyQwlmE7F0dFOF7Fm8EtMW37S-IIx3SKjDF21BLXHDW5K0NiL8i-H5PQO6wup-NZlc4IcCmQK508zrx5je4ntAfZHTkC0WNXFj_bfjbbhBRXkU_SsaHAp0STCJwMZq9iKy46rKhIJBItspsBF4kAoGul2-2dWDRxvDWefVRLF5WRl-S6pDvZFoI4mGQgHXVbG0ryOuwyjwAQAACeAFQipmuX4mOD46J9UjdplyweumdJf_oaImigMFwYQPGkCYNoKyMQevTb12keDPB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه جنگ خواهد شد نه مذاکره خواهیم کرد
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66194" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66193">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlSGH-2MSV-JZdjKrGNrwCuHlwfxCpkz0ah6xoLOnmbP7q8rf2rAicC_IXKW6ifKeLKIud-ohkCVFZGA4B7tFHJ_xhUcarpysFyX7CI0C0vF_QKmKvl7vFJfo6yxCnxu_tlIzb5zGlr8ebMlpaD_paamZZ5wb0cm-6nD9WrV5VyH9Gi5q4aW-dHPX9bFE_mCIoyZtVr9o3SwJhusNUgbXOIXIlaREsjQt_FNJobZC7l9BbeDrmXgQWdCdZMP6sHGbDoTFFBRt0IoPxNNgXryVspLGVzyySg9ZijuZtN0Yj_sigK6v_5XW5ha8_pd4rbHvKKZTfLanxa5pwEpXP7CiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد از تلگرام بدون نیاز به ممبر و تولید محتوا؟
سیستمی به اسم MTP وجود داره که باهاش میتونی وارد پروژه‌های واقعی بشی و درآمد کسب کنی.
✅
بدون نیاز به ممبر
✅
بدون نیاز به فالوور
✅
بدون نیاز به تولید محتوا
✅
شروع سریع
✅
آموزش کامل و پشتیبانی
🎁
فقط برای ۳۰ نفر اول:
سه پروژه اولیه بهت داده میشه
مبلغ هر پروژه ۲۵ میلیون تومنه
یعنی از همون ابتدا امکان رسیدن به درآمدهای بالا برات فراهمه
اگر میخوای جزو ۳۰ نفر اول باشی، وارد کانال شو و شمارت رو ارسال کن:
👇
👇
👇
https://t.me/+QpsFnjSfC382MGQ0</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66193" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66192">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24683d102e.mp4?token=UofPn74p3fuvoNNLCVJ58cWPTNJ3UhmCxxoJ-Ef_WG_3kd4ru5200BP2JfDCU_C19M1IGrKmf-CmLKSVKjeMsajRoot2ScyRd4viuPpt0CW-876ztAWqLDL34NNDfJZjLT-SIrkAkgpzdfd-BtrK1h2MkSgVkIYxm-0O5bVV8qJJy-P5_oioVlblevEyREd20Z7i4rlfZAnJKkuuEW6UJpLHJaIGNxI_RxvowEGTB7xFYgrqPAaynxaqsoaNXpuRVqpT0OUdpMrMMiwRi5OO-OLTpwSikFfQ9cElO56SgmExlZB8Q3Ma_bJf67oWuim5umlfHl7ZS2jThowGTQBqeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24683d102e.mp4?token=UofPn74p3fuvoNNLCVJ58cWPTNJ3UhmCxxoJ-Ef_WG_3kd4ru5200BP2JfDCU_C19M1IGrKmf-CmLKSVKjeMsajRoot2ScyRd4viuPpt0CW-876ztAWqLDL34NNDfJZjLT-SIrkAkgpzdfd-BtrK1h2MkSgVkIYxm-0O5bVV8qJJy-P5_oioVlblevEyREd20Z7i4rlfZAnJKkuuEW6UJpLHJaIGNxI_RxvowEGTB7xFYgrqPAaynxaqsoaNXpuRVqpT0OUdpMrMMiwRi5OO-OLTpwSikFfQ9cElO56SgmExlZB8Q3Ma_bJf67oWuim5umlfHl7ZS2jThowGTQBqeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
آخرین مکالمه ترامپ و نتانیاهو بعد توافق:
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66192" target="_blank">📅 20:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66191">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=m8tvBAPgd4T9vNQH5VzKiPzoFnHXlKltSF2vihr_S1XXd8zWs-oQoPRH-O8y0P7wo3YyoRSaNSw0AAS1OcxMHRtQImq7Vd84QTVgrvgRdE2z3O25mnA0xwvc7gnI9AHcYhgMonq13vVZ60YRGz57Gd6JN4C4F05PHcHctfIssXvGY6anWwA93F2fde375c6Yqr1KjbGhaSzodXZP6cO67XoDpj35vzabunhQZOsw9OMZ2Qm3byk14rsPbfpb-LoPCo0_37uji30xPi-E_jsmUCvcIGPGBHSZxSivGUBODb4dp5y2J71biWnnEpHy40kv9S8LUfBYhi58e8i1cAI4JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=m8tvBAPgd4T9vNQH5VzKiPzoFnHXlKltSF2vihr_S1XXd8zWs-oQoPRH-O8y0P7wo3YyoRSaNSw0AAS1OcxMHRtQImq7Vd84QTVgrvgRdE2z3O25mnA0xwvc7gnI9AHcYhgMonq13vVZ60YRGz57Gd6JN4C4F05PHcHctfIssXvGY6anWwA93F2fde375c6Yqr1KjbGhaSzodXZP6cO67XoDpj35vzabunhQZOsw9OMZ2Qm3byk14rsPbfpb-LoPCo0_37uji30xPi-E_jsmUCvcIGPGBHSZxSivGUBODb4dp5y2J71biWnnEpHy40kv9S8LUfBYhi58e8i1cAI4JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: توافق شامل هیچ‌گونه تسهیل زودهنگام تحریم‌ها برای رژیم تروریستی جمهوری اسلامی نمی‌شود.
ترامپ در پاسخ به پرسشی درباره احتمال کاهش یا تعلیق زودهنگام تحریم‌ها علیه رژیم تروریستی جمهوری اسلامی تأکید کرد چنین موضوعی در توافق وجود ندارد و افزود این مسئله در نهایت به رفتار رژیم تروریستی جمهوری اسلامی بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66191" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66190">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66190" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66189">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0B9f7HTByHF_0ApipkkXdrGTaDl7AZrbCpcmKJHWHDAB1CHF2F3HKUncbFRlWXRPzTbkZgVrM_CoE0Oq5oDNq6b2J4cOsFJHVYCfHaFhxFstJO7qoZ3O21_LwK5UwI5DfYbINPj2p4BidSFKgtRm-bkr_pvATa6-KQEJL2u42I9aoQUNEOhn_jNlQrG0QK_T1RSBRCUNg-4LiNpdoHbGKLLEiLBLDa9i_4gwDJRFMmD6b6nJOLGn-X5vVH9Cu0jkP0Tj6Uy7FzJrSBpWlBFh9khTLrpjoH_HN070tn7pVCi1gTdNADEEIENQ-TAwOZZEN1uguo4SG7YZO2vAALGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66189" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66187">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=V76yHDMkf-owHHmC0IWayyLIKIER09-f8jjsBLBsefPuu0RgYQxg1EmM_NedbBjrIOiSRwjeqg-qoo3ZXn4cqKi5wfEbpTTqxElsSEpvauqNQR-BPhmMpWYUsHXR5-pHoIxDr0O8dKDbVdRBV8t4HdTLRe0x-tjAdfJiqv01lODoy9-pg4U_GPxWKlnmfRyhFYZ6_t3puu_A9WMWH8_OPw6ohl7rNwCOZWDlfHZRiVCw_aRe0KgxWb_YkMvs2wdvdFf7z_hg6JNcV4Y3_l1PW2vtj-WaeMqK6fBeXLh1fkB1kE8Dc5TB0dLnCeDCGyeLq8-n1vmzwQwmjExdYDLMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=V76yHDMkf-owHHmC0IWayyLIKIER09-f8jjsBLBsefPuu0RgYQxg1EmM_NedbBjrIOiSRwjeqg-qoo3ZXn4cqKi5wfEbpTTqxElsSEpvauqNQR-BPhmMpWYUsHXR5-pHoIxDr0O8dKDbVdRBV8t4HdTLRe0x-tjAdfJiqv01lODoy9-pg4U_GPxWKlnmfRyhFYZ6_t3puu_A9WMWH8_OPw6ohl7rNwCOZWDlfHZRiVCw_aRe0KgxWb_YkMvs2wdvdFf7z_hg6JNcV4Y3_l1PW2vtj-WaeMqK6fBeXLh1fkB1kE8Dc5TB0dLnCeDCGyeLq8-n1vmzwQwmjExdYDLMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
متن تفاهم‌نامه به زودی منتشر خواهد شد و سندی بسیار قدرتمند است
ترامپ در پاسخ به پرسشی درباره زمان انتشار متن تفاهم‌نامه گفت این سند احتمالاً خیلی زود منتشر می‌شود، زیرا مایل است افکار عمومی آن را مشاهده کنند. او همچنین تأکید کرد این تفاهم‌نامه سندی بسیار قدرتمند است و آن را با توافق دولت اوباما مقایسه کرد که به گفته او سندی بسیار بد بود. پرزیدنت ترامپ افزود انتشار متن احتمالاً در مقطعی پس از روز جمعه انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66187" target="_blank">📅 20:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66186">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=vdX5FXWAnBigyed7caKlsxh4c_NIq8NF-1lQzuSfhGwuXgCS-RszokkNFk5MbYtWL_FyyAi73c4Y7R3Tr6VEIvht9_vRdwUkIHjAqexPNYDXwHMuWx9eHMpi-kRLa9jTU5DfvBFz0McwLxQ5YV-tAkArNNl__elrxrSFx61i2MQwz6qFY01CmgXOodMbaltUvAXGdLCeH_iFbq4-kHmZ8cdtM4iumUcMGqnTs6eNy6MEyimhznsOf9_7VQmAMup88tbGWtdGoSzXj_CrXSnhNrXdcrH3jC_764yGcvnqYaUYQCQ6GVkrG1wXsU6wUzYkcVC0Z5cJbRbRcZ--4TWuMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=vdX5FXWAnBigyed7caKlsxh4c_NIq8NF-1lQzuSfhGwuXgCS-RszokkNFk5MbYtWL_FyyAi73c4Y7R3Tr6VEIvht9_vRdwUkIHjAqexPNYDXwHMuWx9eHMpi-kRLa9jTU5DfvBFz0McwLxQ5YV-tAkArNNl__elrxrSFx61i2MQwz6qFY01CmgXOodMbaltUvAXGdLCeH_iFbq4-kHmZ8cdtM4iumUcMGqnTs6eNy6MEyimhznsOf9_7VQmAMup88tbGWtdGoSzXj_CrXSnhNrXdcrH3jC_764yGcvnqYaUYQCQ6GVkrG1wXsU6wUzYkcVC0Z5cJbRbRcZ--4TWuMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: می‌خواهیم مسئله لبنان را حل کنیم.
آمریکا به دنبال آن است که ببیند آیا می‌تواند مسئله لبنان را سامان دهد، زیرا این بحران به نظر می‌رسد هرگز پایان نمی‌یابد. او افزود این موضوع در مقایسه با سایر پرونده‌ها نباید دشوار باشد و درباره گروه تروریستی حزب‌الله نیز گفت باید گفت‌وگوهایی در این خصوص انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66186" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66185">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=bvDq3eujVk3z2gojn_d3m-prVQzFxH9z8FLKPYv6EV5nAT8hnnb_brFaWSZqa0QRzFAxWuWlmqxXHUeGf6E3_TRbF13pMHFjNaM7Oy96MBBlNTem6caRqbu0Y-4o97SwXuPl4UBF9JcL728z13WEkgc8jlgirHH_avs8Q6_iU0ZL-8kUDHomYLZj7tLDcgXXzTEKrZdVpyDZnd-Z1Z1aK6MHI27RR00F_Qrm9ZL_3IuVNadvkJ1KG346c8r8ubSLPERTZMYCmcVYjejPjCK5TwhBFVcWoJYHM-_sHiMKG3GQcoYCWCm606Ypg34Q23fqQyWKfJ0YFEvbsQoWecxx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=bvDq3eujVk3z2gojn_d3m-prVQzFxH9z8FLKPYv6EV5nAT8hnnb_brFaWSZqa0QRzFAxWuWlmqxXHUeGf6E3_TRbF13pMHFjNaM7Oy96MBBlNTem6caRqbu0Y-4o97SwXuPl4UBF9JcL728z13WEkgc8jlgirHH_avs8Q6_iU0ZL-8kUDHomYLZj7tLDcgXXzTEKrZdVpyDZnd-Z1Z1aK6MHI27RR00F_Qrm9ZL_3IuVNadvkJ1KG346c8r8ubSLPERTZMYCmcVYjejPjCK5TwhBFVcWoJYHM-_sHiMKG3GQcoYCWCm606Ypg34Q23fqQyWKfJ0YFEvbsQoWecxx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
درباره باز بودن تنگه هرمز اختلاف‌نظرهایی وجود داشت، اما در نهایت عبور و مرور از این گذرگاه راهبردی بدون دریافت عوارض انجام خواهد شد. او افزود آمریکا احتمالاً به کمک زیادی نیاز نخواهد داشت، اما حضور یک یا دو کشتی از چند کشور دیگر می‌تواند مفید باشد و فرانسه نیز یکی از گزینه‌های مناسب برای مشارکت در این مأموریت است. پرزیدنت ترامپ همچنین تأکید کرد هیچ‌گاه نمی‌توان از تحولات آینده کاملاً مطمئن بود، اما به باور او تنگه هرمز باز خواهد ماند و رفت‌وآمد دریایی در آن آزادانه ادامه پیدا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66185" target="_blank">📅 20:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66184">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=ZusXSYSYRdA40yEFI2jEO5yKJvSabyQEWwrl0P_XmCfnuOzEwpO06j5No5i5GfjXXhMvcKmLT8lMImYmqS8PKDz581NBfTUF9u04El9dXmhw19q-270HHgXX7oi5sxmzbfdj_SaOf1sKzTXkdeSsMilqD8xoDg-0RilwtO-d627JngDaw_YV8MYCwz8fuGWHdCIgKdOic_Yb5HSEatV0te-ASkP3vFDsidte4en8UieQFV6KUwywKUnqQOnyjmtjiFQUWrtvxq1Ijr77cuDT28VCKsQgNUwnnB4lJvLmM4DM5ruLbFeTuhBPoB8LhfgTrylF4lMF7tlJjM9MWzuexQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=ZusXSYSYRdA40yEFI2jEO5yKJvSabyQEWwrl0P_XmCfnuOzEwpO06j5No5i5GfjXXhMvcKmLT8lMImYmqS8PKDz581NBfTUF9u04El9dXmhw19q-270HHgXX7oi5sxmzbfdj_SaOf1sKzTXkdeSsMilqD8xoDg-0RilwtO-d627JngDaw_YV8MYCwz8fuGWHdCIgKdOic_Yb5HSEatV0te-ASkP3vFDsidte4en8UieQFV6KUwywKUnqQOnyjmtjiFQUWrtvxq1Ijr77cuDT28VCKsQgNUwnnB4lJvLmM4DM5ruLbFeTuhBPoB8LhfgTrylF4lMF7tlJjM9MWzuexQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره حضور در مراسم امضای روز جمعه:
پرزیدنت ترامپ در پاسخ به پرسشی درباره حضورش در مراسم امضای روز جمعه گفت این موضوع به شرایط بستگی دارد و در ابتدا قرار بود جی دی ونس این مسئولیت را بر عهده بگیرد. او افزود ممکن است تا آن زمان برنامه‌های دیگری داشته باشد، زیرا قرار است تا دیروقت مشغول باشد و هنوز تصمیم نهایی درباره حضورش گرفته نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66184" target="_blank">📅 20:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66183">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=n_WEsPmNT00Zt7FVN7nmosuMq5CT8e_5y0gdmsPbsw58ZbQQnGMmTEMl9zyb3GROUXdQCnhE_RuA7m2OkNByoVQAbkcePeslMlIHipMhxpllzerMM6xIkjk3_mFOtYGorKsBVa0x8LsyiH_X8F87kYtoCmNm0R26XaK_I-YnsRHDm_RTDIqZsQ5DrXQe3miRhV-xHZflpGmzVziROxqipmDUSdviUr5Jv5yVgTbz0dkuvIfzapfS-YB-g4XigFIoBxTMsA6ZYhs3_osTIIwaxmJF82fJlVxuXIDkOjsE7gssudjMNtyGLbRuJpSFFvqHsmXDfNB0VkYscU4lPo1K-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=n_WEsPmNT00Zt7FVN7nmosuMq5CT8e_5y0gdmsPbsw58ZbQQnGMmTEMl9zyb3GROUXdQCnhE_RuA7m2OkNByoVQAbkcePeslMlIHipMhxpllzerMM6xIkjk3_mFOtYGorKsBVa0x8LsyiH_X8F87kYtoCmNm0R26XaK_I-YnsRHDm_RTDIqZsQ5DrXQe3miRhV-xHZflpGmzVziROxqipmDUSdviUr5Jv5yVgTbz0dkuvIfzapfS-YB-g4XigFIoBxTMsA6ZYhs3_osTIIwaxmJF82fJlVxuXIDkOjsE7gssudjMNtyGLbRuJpSFFvqHsmXDfNB0VkYscU4lPo1K-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
پرزیدنت ترامپ گفت آمریکا کار بزرگی انجام داده و امیدوار است روابط خوبی با رژیم تروریستی جمهوری اسلامی شکل بگیرد و دو طرف بتوانند با یکدیگر کنار بیایند. او افزود اگر این روند موفق نباشد، شرایط به نقطه شروع بازخواهد گشت، اما معتقد است نیازی به چنین سناریویی نخواهد بود. پرزیدنت ترامپ همچنین تأکید کرد توافق انجام‌شده با رژیم تروریستی جمهوری اسلامی می‌تواند دستاورد بزرگی برای جهان به همراه داشته باشد، زیرا برای مدتی جریان نفت در منطقه با محدودیت و اختلال مواجه شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66183" target="_blank">📅 20:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66182">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umdngKdICu0o3VLXXoihWOL5B-_Y2WpV5byu_eE9AK07uCns4UWCyZtuCPq5Rmef5CqIM9dxWsovdfEYhEjnCfBjiftB-QvYpXr2w1zKVpnok-KPdElgmYmL0VyRZeV3_ywncR4F9qZes3HDHtKiyYFakHcW5D_J540L8QKdmGY8OtRGlrlwWObBoyXmKCMT42VFBDvsjgC5X2_EKnM5H5T3SNIsEjx-qcwG0c5pCddQdrhPFmv0D_d0e0ReScozsmn-uyacN_sDlKOOCvBbveqg7oPdRPnYtmSRMYJpcz7Gpj5UninfC-LMhrwCy_KDJLUSLgSh1VGd9mrnTDjPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
ملت دوست‌داشتنی و سروقامت ایران! با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.
ایستاده‌ایم و در نهایت ‎
#ایران_ما
پیروز خواهد شد، به لطف خدا.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66182" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66181">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=vhsMvq89_PL31310VIMhXxUUNo8vbqU4M0URUBljVoqvAiXlS4cA_poDW_13lqfCJVgvJrutG4p1fdqhOe9DHhHpgVmMyz6FzqOdMTwQa0bhec7_eUU8Gs2EjnIaCkx0lOveWjqBZLtOK6CKRbfj9SuWgkZ8aG4O1X9JjFsF7JYC2Lf3_k2HbDdlkkBEwMHW25DaCSDhyMMLKslYBLCG5cJPj0MWtIHOf_1JltNeopPYx81NBt2FTNRD03f37Xdg_Bhk88GMbcMy76uXO1wn9cyqIbJiklsBo2nQM1qtn9n4IoRP5gwRO1IOIchKh3CrqD5WGbMEKLACPEVLwMcl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=vhsMvq89_PL31310VIMhXxUUNo8vbqU4M0URUBljVoqvAiXlS4cA_poDW_13lqfCJVgvJrutG4p1fdqhOe9DHhHpgVmMyz6FzqOdMTwQa0bhec7_eUU8Gs2EjnIaCkx0lOveWjqBZLtOK6CKRbfj9SuWgkZ8aG4O1X9JjFsF7JYC2Lf3_k2HbDdlkkBEwMHW25DaCSDhyMMLKslYBLCG5cJPj0MWtIHOf_1JltNeopPYx81NBt2FTNRD03f37Xdg_Bhk88GMbcMy76uXO1wn9cyqIbJiklsBo2nQM1qtn9n4IoRP5gwRO1IOIchKh3CrqD5WGbMEKLACPEVLwMcl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف بعد تعطیل کردن مجلس و انجام هر کاری که دلش میخواد
😂
:
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66181" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66180">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها 10 گیگ — 170 تومان 20 گیگ — 340 تومان نامحدود — 450 تومان (ترکیه)  برای خرید بهشون پیام بدین
⬇️
…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66180" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66179">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها
10 گیگ — 170 تومان
20 گیگ — 340 تومان
نامحدود — 450 تومان (ترکیه)
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66179" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66174">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWb_wjgvY83HgproSR8MnETrL3NvwmbRvPbTi-R5h-wQYUXux0M_7zw3nZwZJg4uDFnogAvObWuM6pc2UUGMM9QvtWEjNVjjHySaHc9mN7XZY3Evd7Ed53aFRJJReHR3giQaEzctr4pIoFMwiDXdhONMB4fFHyFO-w2KHnYWkhr1C6U3aWM0H5cWQcsf9mlgmg1cZ1oTVVcTODrHMeqD-tuDNArTiTCLHlM0MCPwM0stO_3JRSCFhptPuPgl1hwC4RCB92RhmLX470P6EMJ3OQGtGH4V42ipvGS--vbEKvhYtjjp86OpQz5kMdF6LNydKvC2r5JZkojahOqFDskE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxUl6c2jhdDJk4l0H8-84Nqu7zvPMCispm7ZLW0Emri4_popg6kS0UqhFje2uAG4_qPxOoXFgDMG01wVlp2QLqHOgQt_PHLhQtUM2dAiUvUjlaZ9lNJ0fd-CjMba0-sN3486diipH8G849WcgJvyNzeGw34yf2Zr1DlIIp29dvWssftNyVIOmZCXmBkiGdakG_31wuW68KfLUhXFmXH0s33e9sbMfkJjhcQtEn09Cs7HdCtKIwEflg7wJF2aN78pvBJ8cyPR9Xo8EkSSMJeQ8TjN71i5Bw69C8i1W2jAvL4SqkxYxEt55W1EoHjr05ntV2w2GDfdhPj97roC_LUx7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=kj716LHe-0ydGh1cl8jJmAPgLG6eA9wa9opId_mfW9PAs125ezOfva3BMXkSivglDlmEMMYiQpqyLba36KDxkw36LklyisNeUklqFPnl1j6KCG6URQJ2dSk4IM5ZDkFX0QPnN-f4PdzzIyXMes20lyNrEfNqM0TszzChZoFXnXMb7chRetKYML0UYraiuGA5zxt9Wfbl-wUsBXj5crfDqKvzLdRzZOQC-aGBLv1Q0_s-aSAnkYvV0vEUm0zKjMI04hq0WLfm_-ntCCDW5NGevfqSQleTWcs7FQQ35enocTbaoNX62O0EBUB5Tl5nKPbLx9zZ7DYAPHSXpa30IOCxkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=kj716LHe-0ydGh1cl8jJmAPgLG6eA9wa9opId_mfW9PAs125ezOfva3BMXkSivglDlmEMMYiQpqyLba36KDxkw36LklyisNeUklqFPnl1j6KCG6URQJ2dSk4IM5ZDkFX0QPnN-f4PdzzIyXMes20lyNrEfNqM0TszzChZoFXnXMb7chRetKYML0UYraiuGA5zxt9Wfbl-wUsBXj5crfDqKvzLdRzZOQC-aGBLv1Q0_s-aSAnkYvV0vEUm0zKjMI04hq0WLfm_-ntCCDW5NGevfqSQleTWcs7FQQ35enocTbaoNX62O0EBUB5Tl5nKPbLx9zZ7DYAPHSXpa30IOCxkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از آتش سوزی گسترده، میدان تجریش تهران
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66174" target="_blank">📅 19:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
نتانیاهو قراره تا چند ساعت دیگه سخنرانی کنه و این اولین واکنش اون نسبت به توافق هست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66173" target="_blank">📅 18:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما کاملاً آماده‌ایم که کشورهای خلیج فارس در بازسازی ایران سرمایه‌گذاری هنگفتی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66172" target="_blank">📅 18:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما دیروز به صورت دیجیتالی قرارداد را امضا کردیم و هیچ پولی آزاد نشده است. این موضوع تغییر نخواهد کرد،
این یک مسئله مبتنی بر عملکرد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66171" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=eV2M5YiUAb2tCiGTL2VplryPYvg-KAF4fhsgetvnzFE-1HRPHK6nl9mOIa5k9wLb3DU9rDO0Q4hGGuZYtrTQD9Y_ZYRyutB7d_VN__V3WUK4juI_cHfKaMwWVAhKwqn2iKIvQI_v0pN1ca_xLbmGBKxZUIiaTLn1iFkPwFCCV57XNxBbngZJZPPEyxsAwKpLhnALaj_C2RS2VZ9h8RrCJyauQuu45q3KZck2eHAgNLHtOgz1nNGHSt4uiipSjzbICMivC_cwFhFIcPKY6aHL7As4QL7gEm_FbeoU0-C-ZtydINi0_zTRv9SYEj-tv_hEZwmZg1Fynz1_2CQmPkrmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=eV2M5YiUAb2tCiGTL2VplryPYvg-KAF4fhsgetvnzFE-1HRPHK6nl9mOIa5k9wLb3DU9rDO0Q4hGGuZYtrTQD9Y_ZYRyutB7d_VN__V3WUK4juI_cHfKaMwWVAhKwqn2iKIvQI_v0pN1ca_xLbmGBKxZUIiaTLn1iFkPwFCCV57XNxBbngZJZPPEyxsAwKpLhnALaj_C2RS2VZ9h8RrCJyauQuu45q3KZck2eHAgNLHtOgz1nNGHSt4uiipSjzbICMivC_cwFhFIcPKY6aHL7As4QL7gEm_FbeoU0-C-ZtydINi0_zTRv9SYEj-tv_hEZwmZg1Fynz1_2CQmPkrmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ونس:
تمام ائتلاف کشورهای حاشیهٔ خلیج فارس از توافق هسته‌ای اوباما با ایران متنفر بودند، چون احساس می‌کردند این توافق به ایران قدرت می‌دهد که نقش یک بازیگر بد را ایفا کند
حالا ائتلاف خلیج فارس دربارهٔ توافق صلح ترامپ چه می‌گوید؟ آنها عاشق این توافق هستند، چون آن را فرصتی برای ساختن و آفریدن خاورمیانه‌ای جدید می‌بینند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66170" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=X9jkQgdsffLejSecz1k1oZMLJF8k0-P1DjfLXMXJmecL-dAKQ6feBelWEz0fOtv6p1wzv3miSkRrWeBoYO_z2cJkRRtPkXPzXyiTpNHUmfGF0QHiNJgdwZOJd-K0PgmnIUMqqp19W6GvyJ8Eve0OX9eq5a2IJ9SxMQFYviy_mHCMk30XsU2Jp2CcdxUCgJSk7CYVMBX9gjp7l8l7oBIEqXrFk6-BiypUQp2T8A7hLfep5uYdSx45sBcEhyn4LqRRKnouX0lUvR6EHS1BOgB6U53LdupIkemYwMGeIZOc0AY7yXnKeQ4-0z8Mm1i_tMTb8lvh1APluYmNgNZcFVzYTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=X9jkQgdsffLejSecz1k1oZMLJF8k0-P1DjfLXMXJmecL-dAKQ6feBelWEz0fOtv6p1wzv3miSkRrWeBoYO_z2cJkRRtPkXPzXyiTpNHUmfGF0QHiNJgdwZOJd-K0PgmnIUMqqp19W6GvyJ8Eve0OX9eq5a2IJ9SxMQFYviy_mHCMk30XsU2Jp2CcdxUCgJSk7CYVMBX9gjp7l8l7oBIEqXrFk6-BiypUQp2T8A7hLfep5uYdSx45sBcEhyn4LqRRKnouX0lUvR6EHS1BOgB6U53LdupIkemYwMGeIZOc0AY7yXnKeQ4-0z8Mm1i_tMTb8lvh1APluYmNgNZcFVzYTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس درباره ایران:
ما اکنون مستقیماً با نظام ایران صحبت می‌کنیم. روابط خوبی در آنجا داریم
دیگر پیام‌ها را از طریق کانال‌های پشتی منتقل نمی‌کنیم؛ در واقع با آن‌ها صحبت می‌کنیم.
وقتی با آن‌ها صحبت می‌کنید، متوجه می‌شوید چه چیزی واقعی است، چه چیزی جعلی است، درباره چه چیزی جدی هستند و درباره چه چیزی جدی نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66169" target="_blank">📅 18:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a8610027.mp4?token=kYrbdGO2kxUQ8bUAWquahxXX7NFCcb7jjr6VyiK50TNbZzNqcrSgTmfhqFqQ9KQaGA87oot8AAbyEbanTxNo4mGqqLCLLDv_JO_nRTbFD84mhn-UFjGkCIU7QgcfWEpKl_rCnPIcVdmXod2k63bJOoYWpQANoKk-xLWeo_wa6em8KrJP06J5EoH5wz8u7IxYf12418xDmuqvYd7En1Iu1zSjySBTgmBQ6-IZfVHgL1jo4C9X28C8YmX4D95JPlHtwwb-5rvPB9wd1bU9hutRz74JOiuT1McNLQ_FrNSIqWv9oA9azasjPYY8KyntmvL5cXw4gB8XF5taRsFzSp2-rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a8610027.mp4?token=kYrbdGO2kxUQ8bUAWquahxXX7NFCcb7jjr6VyiK50TNbZzNqcrSgTmfhqFqQ9KQaGA87oot8AAbyEbanTxNo4mGqqLCLLDv_JO_nRTbFD84mhn-UFjGkCIU7QgcfWEpKl_rCnPIcVdmXod2k63bJOoYWpQANoKk-xLWeo_wa6em8KrJP06J5EoH5wz8u7IxYf12418xDmuqvYd7En1Iu1zSjySBTgmBQ6-IZfVHgL1jo4C9X28C8YmX4D95JPlHtwwb-5rvPB9wd1bU9hutRz74JOiuT1McNLQ_FrNSIqWv9oA9azasjPYY8KyntmvL5cXw4gB8XF5taRsFzSp2-rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد ایران:
ما دستمان را به سوی ایران دراز می‌کنیم. اگر آنها بخواهند رابطه‌شان را با ما تغییر دهند، ما هم رابطه‌مان را با ایران تغییر خواهیم داد.
این پیشنهاد ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66168" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=olJHwsLyMm6dkPjKTwdLSO496Z5X-9aNOEMT0iZF79NvJrNQWntpeVqvvfOt2PPHjNv9fyIUMmNqVRmWxxyg_R7FGUIkX1cO4E4AuCbSL2iLMHAi8T1jCM5ioofJk3VQ7PX0l-IED_G4FR6xtYDuTkIjonN2ysbkniLvqB31Z2fO3bpUxE5Gz9kB1eYqmB9A0vGFA0pQHF8QwOrY7x4fPRksF8WsWCiA40f8PufIxiYmBwJy4vys5mIf18uIGp0uaiaUctzp_dMcCrn9LakZ48htGVmVDQj-M0xuhLKtNuZMK-XrwsnWAvWX3l1NcLVmtpOacPAczCVDwnw9PCHQAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=olJHwsLyMm6dkPjKTwdLSO496Z5X-9aNOEMT0iZF79NvJrNQWntpeVqvvfOt2PPHjNv9fyIUMmNqVRmWxxyg_R7FGUIkX1cO4E4AuCbSL2iLMHAi8T1jCM5ioofJk3VQ7PX0l-IED_G4FR6xtYDuTkIjonN2ysbkniLvqB31Z2fO3bpUxE5Gz9kB1eYqmB9A0vGFA0pQHF8QwOrY7x4fPRksF8WsWCiA40f8PufIxiYmBwJy4vys5mIf18uIGp0uaiaUctzp_dMcCrn9LakZ48htGVmVDQj-M0xuhLKtNuZMK-XrwsnWAvWX3l1NcLVmtpOacPAczCVDwnw9PCHQAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شده یک فروند بمب افکن Tu-22M3 نیروی هوایی در منطقه ایرکوتسک سقوط کرده و به گزارش وزارت دفاع روسیه تمام خدمه موفق شده اند با موفقیت اجکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66167" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66166">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
فقط یک نفر از اعضای شورای عالی امنیت ملی مخالف توافق بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66166" target="_blank">📅 17:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66165">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oc_Vb0iFJV79ymavIOt69i_f4nYCgiYmQ_haa46kdh5HmjOoI2BZFsZ4zrVVTkPglZuyY27elkVXuPZp9MPjJYs7GsQwktBy8HZ52Q_GO4FvjBu5cGaOiWq5dezhtkN9zfpcFixDLauu5CrWn4PAqnsauonmNXxCPhQuoGbfM23uSHLh05Chhj2PB1oq2BPVTdMJFMkclwjcJM9rpHeDMMPjZwf0r4USQDkfsZfM4W9tHTiAxMPBOUcpReh4PuV3N3xuhq8U4kd1wHYox9L7Qd_2greaTJXNLg-emi3aEo0E1r5LZQP2lIkxaG91Ur7lTydh8a98_kE1qQsPhbXq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل شروع بازی اسپانیا و کیپ ورده فاک بت اومده لاین داده ضریب ۲.۲۰ الانم میخواد آنالیز بزاره از بازی های جام جهانی نمیخوای بیایی سود کنی؟
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66165" target="_blank">📅 17:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66164">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I24zM9H7wXl1Zi6CJl1yaC9GY7kFkB_EJtK4aExD652SukLgx4OHyTPCcTsKaJAyzL32xCM81OGrGjGiEGOQT4y0fYy1a_jHNW6iCIYwRTByQvcSSGiU1l_VMZWIyrNAec23pmyCHBzswdtPRTWxPRChNh_wRRo0kgqB_UYMzNRYL7-c4JCix-0-yxEzD1KGZbGGuKqquvBtkPwLjbnEVNHUlK7fOemFftsMqfXbME5PNThUzTO7wafIWcldyWkQzUppwNPekTPJ-mkqz0VRxDibado-4w5TGdEOPxDhstCAWA3QpPcZDc5IpOhit8izN5ycFMPxeetjexrutS8fNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ در تروث سوشال :
پس از توافق تاریخی حاصل شده با ایران در آخر هفته، کشتی‌ها شروع به خروج از تنگه هرمز کرده‌اند، که بسیاری از آنها «پر از نفت» هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66164" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66163">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
صداوسیما:
تنگه هرمز تا اطلاع ثانوی بسته است و سپاه بیش از ۹۶ساعت هستش که اجازه عبور به هیچ شناوری رو نداده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66163" target="_blank">📅 16:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=aXhvmP-88_izTDxmypdSGDUZYRMG-Jk8F970DrjMyrlR9bMbemZctZhRMADLtiJSQvDaMcGcmQBz-BPd0u5fOeBSaKT_RoDzY2QxMHlmT0aVmUM1h9J1TfaH4VJok0mOu96Egbwx6-7IjU0CU9J-LbT3Dze5iv9SBryfgPtZmaQS3CeBb6JzBdn8E5SYLv1BNeuh3k7sAfE-JmzD7CyI8CCcg654IjHoLpsEzM0tOqvfdnS1yl5qtqpMZW_9c9vjjNrFtj6Xboy9A9T6v0-bBrtidUCstcqPouXZgyT9jyJgtTgKvsabHs6-CcS7qy1JvMW8aCroU3HSqKaCxV0dDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=aXhvmP-88_izTDxmypdSGDUZYRMG-Jk8F970DrjMyrlR9bMbemZctZhRMADLtiJSQvDaMcGcmQBz-BPd0u5fOeBSaKT_RoDzY2QxMHlmT0aVmUM1h9J1TfaH4VJok0mOu96Egbwx6-7IjU0CU9J-LbT3Dze5iv9SBryfgPtZmaQS3CeBb6JzBdn8E5SYLv1BNeuh3k7sAfE-JmzD7CyI8CCcg654IjHoLpsEzM0tOqvfdnS1yl5qtqpMZW_9c9vjjNrFtj6Xboy9A9T6v0-bBrtidUCstcqPouXZgyT9jyJgtTgKvsabHs6-CcS7qy1JvMW8aCroU3HSqKaCxV0dDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ممدباقر۲۰بهمن۱۴۰۳:
با قاتلین قاسم سلیمانی مذاکره نمیکنیم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66162" target="_blank">📅 16:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66161">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=Nr7KGdwd3YgH2_dE6CDK_3XRfIKtYVw5CI9JXOvy4tlFVGDlmNYDOKdXMC9PeYFJoubDME0HoHn3CZr2FOc6CR5Q3owrUxia_qJt6I_pDAvNQ6DAUitMf3p2LMKjY7qAgLcUtupzfxqD74Pav0AbP7Y83bIA0GBCSCWjmaodwOUymW9WmQjZWfoeZoj3tObE_nzcr44TCEEEBDMnKa8OHjpFOLKNZXpHPXuwAkKXcBCH998N0z9lB1i6AbRRvuQPTKyXOC2MT8YunDZ06oix-Z-obnjbCKlzDIcsXvQU3EWOiJBnt4u6oa8iu0IJ5HelNcaYwZwBS444ouRSYrTNaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=Nr7KGdwd3YgH2_dE6CDK_3XRfIKtYVw5CI9JXOvy4tlFVGDlmNYDOKdXMC9PeYFJoubDME0HoHn3CZr2FOc6CR5Q3owrUxia_qJt6I_pDAvNQ6DAUitMf3p2LMKjY7qAgLcUtupzfxqD74Pav0AbP7Y83bIA0GBCSCWjmaodwOUymW9WmQjZWfoeZoj3tObE_nzcr44TCEEEBDMnKa8OHjpFOLKNZXpHPXuwAkKXcBCH998N0z9lB1i6AbRRvuQPTKyXOC2MT8YunDZ06oix-Z-obnjbCKlzDIcsXvQU3EWOiJBnt4u6oa8iu0IJ5HelNcaYwZwBS444ouRSYrTNaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله پزشکیان به منتقدان و اراذل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66161" target="_blank">📅 15:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66160">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBlslAQxwGUFYkwWYbK7KZ1lqwXJCNOU8D5qeQ-UyFcC_vdjCshJEBRKqvA9ZYQMFoS7MgWNhI4fLNLvbhKHN93Gu8-bVO_PVbHNLR_tbvKNMfl2_kSYN-fRRSP1yYQXA6EAGopTAzdcqe64lgHxIRc94g8WGg0PmpZJ2cnFPfqCe-IbCESAJgoogoZ_8f0Raw0zbURSE9DjGmxrSghCWifluiHiyGXKiX0xsgtGR1KrK-LKLmj367lvb6-COShVuxCQttbSGrVvUsNu1jQk-yInM4ZULeruVtEPcbPE5ComvF1GzqscGKCj-gZ_zXijRxide2ZWFCW8NPnAXrGxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابوالفضل ابوترابی، نماینده مجلس:
استیضاح مسعود پزشکیان مطرح نیست، شاید خدا شهیدش کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66160" target="_blank">📅 15:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=sHrGQFZwqyz4_bGuIzUFK8mkefIFfTNP811glBEdPGdPHVgkGE3mup3eX3hqLa4yVYBO5DlKZeRsDSbrrbhmxq0MJOZxlljsLaQV3w4mD7c33nzIGcv48UxINMwlDC-7nYnNLiAOVxllcaN-ZGygIQO3rKF1hW2Qj2MIeUr6uP8tYYZzp1tonfwa1ouP56bplHPbFPDLeTz8qC8RF72UDUct3ShXknlHbKaL9ECVuQRfrGDYKLLaiGT2_ZePthBkZKB4XuotNbfCLQfWFtH3qzVXfVVzCIvOlp3n3HyWoITvc_FYjP2GusIzQysp2Yeo53jX256Vu2NAauAFTXZFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=sHrGQFZwqyz4_bGuIzUFK8mkefIFfTNP811glBEdPGdPHVgkGE3mup3eX3hqLa4yVYBO5DlKZeRsDSbrrbhmxq0MJOZxlljsLaQV3w4mD7c33nzIGcv48UxINMwlDC-7nYnNLiAOVxllcaN-ZGygIQO3rKF1hW2Qj2MIeUr6uP8tYYZzp1tonfwa1ouP56bplHPbFPDLeTz8qC8RF72UDUct3ShXknlHbKaL9ECVuQRfrGDYKLLaiGT2_ZePthBkZKB4XuotNbfCLQfWFtH3qzVXfVVzCIvOlp3n3HyWoITvc_FYjP2GusIzQysp2Yeo53jX256Vu2NAauAFTXZFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ برای شرکت در اجلاس گروه هفت به فرانسه سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66159" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqvcRR3nG4wDC75KJfObTgBj1VHoYg5XGxbxqE_zhjjEflR98nOwu9nWY4dpvuawifkOrCfKD1EzZ0HU0plS0rdB7YZZYuKH5wjgIdxh7t9Th77XHiLr8dTraFgkew53Sel0yT9W4EJqfEtKFhnzOmNDinohIas7eveso8mvfzncPPeEkeQIaqKX_cI30aLW_BHsOnjUEPnbqu5v97pnaB5MIuNJfmr4WmZzT_QPm3Q2UBujUesN8miuNwBIRqb1a2e7FSpjxoWWODGOHqebtoV8Cck95uvRA2O_-7M1Lb9KoKQnvdHX6rwtmKCPvVLhb-wxk0ZUIAYI3qkvkwCAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید حساب اسرائیل به فارسی:
یک سال پیش در چنین روزی جمهوری اسلامی با ساقط کردن چند فروند F35خلبانان اسرائیلی را به اسارت گرفت و ما همچنان در انتظار پخش اعترافات آنها در صداوسیما هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66158" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66157">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=u3AhkGxdm9I9gBBXf47tz_zim2PfLRVilSeo1xLiioB8t-kNBEDO7NKH8sO2BMOyw_c1LFZQRbEiw86g4HAK6uerPJcYO9WP3AkFDxaCRolGI4CDfxzS-X-YZmBhrI-uvJggGYYR4AtUggEpDv91NPjqlN-SDB49mlCkKF86Nhyhi6XkzfZ_0c2Ev8qRZhWwWEooyvC9_f49x3TS3q8Qs9-TiCMLFGugSrc0h7t8Hmh2jcSelH7PFQS49hqPIkrEK5PSOY-ifB4WxlFf6JA7S8-bOuGJGLR0flu93P6l05uB9DFDWwduG0hVnExX0aCAgkSGqxRzM7RUVTfjOK_06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=u3AhkGxdm9I9gBBXf47tz_zim2PfLRVilSeo1xLiioB8t-kNBEDO7NKH8sO2BMOyw_c1LFZQRbEiw86g4HAK6uerPJcYO9WP3AkFDxaCRolGI4CDfxzS-X-YZmBhrI-uvJggGYYR4AtUggEpDv91NPjqlN-SDB49mlCkKF86Nhyhi6XkzfZ_0c2Ev8qRZhWwWEooyvC9_f49x3TS3q8Qs9-TiCMLFGugSrc0h7t8Hmh2jcSelH7PFQS49hqPIkrEK5PSOY-ifB4WxlFf6JA7S8-bOuGJGLR0flu93P6l05uB9DFDWwduG0hVnExX0aCAgkSGqxRzM7RUVTfjOK_06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت«
ال ریسیتاس
» بازیگر اسپانیایی از اتفاقات جنگ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66157" target="_blank">📅 13:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66156">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=LnfUH0UTwPMCheNG35d5y2ZTiFshSuXNnt94Zx8nQjFOu1xnnPpiJO98JBWpPJk4MD13ZR0WXn_OkAKCamvTYovIXVEmQtjbyOlpsr_X7HNpfUBfoLVwu5gOTGE5f56qb_3wOYrApf8ylZJpItij0jt7wD2iMffkrO38zSQhb0C9ore-1nVib--qo7n9Z1PaBQM2MtWHCbp1x8EW423M7N-coOiywHTnq6K1x00IVTf2iCGzDrFgaG9zTrbw5e7E1qAVWKNoNbXkLOUGUaLq9ENNW-nRETjOcqiD3oApYjSf7Iul5sLa8vQgs4gi4PNApFVg9WOp_x8hb6iPvreafA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=LnfUH0UTwPMCheNG35d5y2ZTiFshSuXNnt94Zx8nQjFOu1xnnPpiJO98JBWpPJk4MD13ZR0WXn_OkAKCamvTYovIXVEmQtjbyOlpsr_X7HNpfUBfoLVwu5gOTGE5f56qb_3wOYrApf8ylZJpItij0jt7wD2iMffkrO38zSQhb0C9ore-1nVib--qo7n9Z1PaBQM2MtWHCbp1x8EW423M7N-coOiywHTnq6K1x00IVTf2iCGzDrFgaG9zTrbw5e7E1qAVWKNoNbXkLOUGUaLq9ENNW-nRETjOcqiD3oApYjSf7Iul5sLa8vQgs4gi4PNApFVg9WOp_x8hb6iPvreafA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حمله اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66156" target="_blank">📅 13:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti-UKLxBgTu39DANa4rIOIVheYyC8EQpNDBvVau8_iK2kdUDgEv7L9FOIVPUbpDY1rLwcJNEcF4QqerUHHpwNfSIju_9DklYQm9wJPvEo0cFc3CoHXEjmOEd9I4YFtBl4AY2F0v8qd5PsA9OhmLMpI4AGKb2pF-ee4CaSPN_X32CKqo_7YL824jqOBit9-EdaCFLuiP44yQs9EK7K3muLGDviuDJwP3hg9KMWzMfzvlNmk--ZjwzIj0yeVLQC06n6GZGeReB722z2IZAhooRMpYEvi6fGsUFuCqkObbSPm9FEkUHHaJUDWpCdoawCvz1FX1W4n6YG_KqL6OQh7gUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیس پزشکیان به تندروها:
متأسفم که به کسانی که دارن با مأموریت قانونی برای حفظ منافع و عزت کشور کار می‌کنن، برچسب خیانت و وطن‌فروشی می‌زنن. انتقاد کردن حق همه‌ست، ولی تخریب و له کردن این آدما کار مردونه و عادلانه‌ای نیست.
دولت باید از نیروهای خط مقدم که جونشون رو برای امنیت مردم کف دست گذاشتن کامل حمایت کنه. نمی‌شه ازشون انتظار فداکاری داشت ولی امکانات و نیازهاشون رو فراموش کرد.
ما جلوی هیچ قدرتی سر خم نمی‌کنیم، اما در برابر همهٔ مردم ایران و خواسته‌های درستشون پاسخگو و مسئول هستیم؛ نه فقط یه گروه خاص.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66155" target="_blank">📅 13:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66153">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEztlUHum1bj245YUZMlYijtEeyK3jSCUxEVBpgfb61rBcCzMDGth5fjCRZ4_x2BUHs_daqlW6J7e-oUAHV-Ti9FLNPtuMVJTt8PASv12-cVquzIu7VwKyBZ3ET1Ms4DMpXAiB5phwVruTHepvFMfVzRhxjnC3_1euprZqdLFtE9Iom-1Z_qUGU9EawEE3rnri947LHgIBF6vzOMrlhjVEHAh289JzgGKTLqh7HbzHdqI42tfY5vh2Iuf4KebTzNQ7e0cN0u6KhEFWoreL6N1RBGBmwDwiyt9PSW5lRFL-m4LEQekKKnw4xz7l64dfDRTf1dT6nLb-8-pwdxdg2_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Isz_IsmTQ-XOkbZsHxW1Ch1wJLTQbSbNWu9BV7druIqLGQWFd327ZZfi3hwffRwTke9CGyfvkGpPogEpwSzeBerb4VbT_kNMl-j6FxUedN7rLi2noip1vs2zCrqtCafKOFtEKSxDwkqT6M9Rv--2Hg3WwOvLJFaUN9cOMlUkBzrSN89lG9Lbj3NslhzyvUhSflXO1rPrcWJ9T0QjjWZTt30jz-HyTqkFjELyYBPfnQq1m1jZc-GpQ8kWfX0kd2kTsaIRElthC0WUpMC8aaCKErOD1xhdBUiB-Jd_LkVanfeS2Vn2EcLLltcrgqD8qI5LKjEUWjPYIciFrrd8VG8Wdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حمله هوایی ارتش اسرائیل به الخیام جنوب لبنان!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66153" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66152" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw1knCKk0Lv8M6cBYIZMrzp029yodaxd2aBazmnvELGpVVgQ-WyaeoduZMSIxR4yb3IVCYGG60ZfIkwoMGqqJ2rwW7LzvR1ju2kqO_d11q5OcW_jnJKNgP7ywCtZP-G7qhf4ImHRI8y6yrfPbc5Dw2rdz11Lzb8YTwwWzZ1PVVUIIZoJNy7V_e14OS6qpXn15Q5EfqE1DhRAtc-lMX57nmPfxFSsB5axPv8wiQTBMCiEGERYa_FuRfVLuIISsnQgLCW8jbnSEPWhDMS7LbNDzHqZgG6DqQ6Av4nb8O3J9_EDRUYvscRq7NbBN6ee6dHzJBZaXEqcz7JPKh6BWfZ4FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66151" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMr2bSB_GQMcDzlpfunSyvDVEV7QZ3BPBPDNqWGl40W1Cv04g0mSJopAfcQPGciC0Vq95xBcQa6wgW0rDbAvGg6pQzrovshgDKjSP_TEtqaBOi7fEb_T7DjJWS-TWGHG7uJHA3Xm1zjizSdXZoiSJusi0cAl8M5RASGcIHA5a_obf2Px3NLKprsKn_9wH-CfYTuEsYG_5fIW7q9gCcTXDMEPbvsGUlyOsF5u5D9uq8mB3-qvW7jmwYbiXwKj1eX5Li4UqP1mw7oRegdsJA0-9zDmLZ24CtmwT7jjjudnxCU-CJQMT8h5yio65Jjyev1xnNGyYm58QkrgrINSgvalhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیده شده در تجمعات
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66150" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz7xaDbl1SqDwiv5KhzEAhCi_cjopjvrYieMOwPmNsZgd6NVi3twILJY-Sj-yKxx5L0I04Pggnf7-_jsI6gRUNjR55HqN5QoUWfB1C7pRhrMnaMBIbSNxF0s9c8lKE5F0-_gF2lsA258gO5epw-y0aG5U_G8RkycvWOaz5aj8LtJCQd0a_6GnlqCHP5ZG5jaY4vmGZRok5ViyGJkdS9hAEPnZ2nVvmc56Vier_cwivn6x-A-ujeR0RoNmgsNf3Fb1Y32h5PbDOgBMPwEPEWmTuX67oPMxB_kvXQNz7z9MGTHXn1KXcx3ZljfegLu8mDE0GfmcQ7FYQHzBjuLUo7yTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل, کاتز:
وزیر دفاع اسرائیل، با رد فشارهای بین‌المللی و هشدار به تهران مبنی بر اینکه هرگونه حمله‌ای به اسرائیل با نیرویی کوبنده مواجه خواهد شد، اعلام کرد که نیروهای دفاعی اسرائیل به طور نامحدود در مناطق امنیتی در سراسر غزه، لبنان و سوریه باقی خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66149" target="_blank">📅 11:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=OeGu7Wg1FuRGREiIa7QEZ40x0HgLLXjmjZNl_NbMPBR8EmNolXQmgtB4MEoplpW6j3heaza3oFXTF4y63fwrraMV9aHUcMolXGB8VfNg_m6AFLu_bygnL8nN18YM2GaC4vA8204dUT1nTX44MS43JnxoeGrtgAf0yEaeUKP2w4Wkd55tRy2Uwtu_2388JfiF5jDFCnt0sgSfad3hlPj-WEc1rLCcyqp_MdU1wBzaOaG56OpPB4lGDorGCkgzhCf1SksM4-NPo0qPQTxKBEO0EmrVPJ6izq6x7cKaBSr2efWZhx4YzXzV8WG0211e9dstUOo-4q0Iho3kGwh3VrJeZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=OeGu7Wg1FuRGREiIa7QEZ40x0HgLLXjmjZNl_NbMPBR8EmNolXQmgtB4MEoplpW6j3heaza3oFXTF4y63fwrraMV9aHUcMolXGB8VfNg_m6AFLu_bygnL8nN18YM2GaC4vA8204dUT1nTX44MS43JnxoeGrtgAf0yEaeUKP2w4Wkd55tRy2Uwtu_2388JfiF5jDFCnt0sgSfad3hlPj-WEc1rLCcyqp_MdU1wBzaOaG56OpPB4lGDorGCkgzhCf1SksM4-NPo0qPQTxKBEO0EmrVPJ6izq6x7cKaBSr2efWZhx4YzXzV8WG0211e9dstUOo-4q0Iho3kGwh3VrJeZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان مقیم آمریکا طبق درخواست قلعه‌نویی واسه حمایت از تیم ملی ریختن جلوی هتل
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66148" target="_blank">📅 11:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEr_A1npoM4x2IXbaqW02rYvsKNEH78wql83--cZhxWo8yMRCOfZYPF_6PEkrHfYm89KsUtiCOdEFtCr_GbCaM1tyHg_xlCOVJtoXJCPskxkYnj-xtjyq3c_tEuQJkftjILURnOc5B5MF9WK-kCoPKWMDvvTFySsGizrMra_0Pw39IzUO5T0FEIeIp48h2N8JfA7otcU_iU_Zu2GxrJqSEWOAoIxzlz2npuR8EbcA-O0428rw-WhoLIwZ7XM0GAvBQ8j5ZDSweZPlYb4gTeKvTXbeqM1E3HsJLc5FtShxNjW2fbiKZ85GJaIQ_Ip_1Y33Kv0ONJe7zSRwDdQJpVPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت عرزشیا هم اکنون:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66147" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkjVdS5JigqRhxd_ck9fsjFjopy-bz5dHv_0ltUOf-MRj8_iv27vM2yG1K6zL6MZzkNzzrqt7RcLVkQg5D-NAQg52NROTc3SC0cG4QopVC9y5i9ddq9P7G8osFcnaSATs27knpjpH7KK6iSlCfOl6mnmzaDjkfh9eiRyAdTcseC2jQrEsPR0yoYAywPasBLGk0P2_A4JSud9gRce0JMeIIMyIxJGJM2uzggro7QoQ84cz9xMXvHqOqNy4vVrpbRVQPQxJGtOBk7HfQyOEk0ydhCdRRlHCjAwNKPTmEH-yMFgFOq8BZG3jiHx9XJ-tyCWIFqhw5z3Ee1LOR7hGwPVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عایشه قذافی دختر معمر قذافی در کتابش:
به پدرم گفتن موشک و برنامه هسته‌ای رو بذار کنار تا درهای رفاه و آسایش به روی لیبی باز بشه.
پدرم همین کارو کرد، اما ناتو شروع به بمباران لیبی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66146" target="_blank">📅 10:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccd116404.mp4?token=Es0zdngl-kzTbLn7mmq90qXZm_dfHUk1KLGSWLK5lBhw0bWOUkmkA3OUiXPWYYyrZ2ZpH9nb100_j5CQLnwHrG_3CZykJiF4anDRzqXzAK9Ic-vTdYRH8zJt_KvNLv9Fnrnid5LSjfQmyNND5JNag8qxWr2UrHZxgkAN2dvhN2lLzfexel4L3O6AZ65uuP2uvcEA2PA3zFi6K-fsxFk1zzKGGA0E-A9vnck3QMiAV4mbFARcl8N4Q6FX-fsH5Mp4cgB9DvsgIV1umjFFq309CYNmO-OpHAzL2s9MiEO8IFfn8E1QXIT6ScCznUdtcRCSPkWqGmjmEA8OxoSLgW-jlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccd116404.mp4?token=Es0zdngl-kzTbLn7mmq90qXZm_dfHUk1KLGSWLK5lBhw0bWOUkmkA3OUiXPWYYyrZ2ZpH9nb100_j5CQLnwHrG_3CZykJiF4anDRzqXzAK9Ic-vTdYRH8zJt_KvNLv9Fnrnid5LSjfQmyNND5JNag8qxWr2UrHZxgkAN2dvhN2lLzfexel4L3O6AZ65uuP2uvcEA2PA3zFi6K-fsxFk1zzKGGA0E-A9vnck3QMiAV4mbFARcl8N4Q6FX-fsH5Mp4cgB9DvsgIV1umjFFq309CYNmO-OpHAzL2s9MiEO8IFfn8E1QXIT6ScCznUdtcRCSPkWqGmjmEA8OxoSLgW-jlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس معاون ترامپ:
من قطعاً قصد دارم برای امضای توافق در سوئیس آنجا باشم، اما ممکن است خود رئیس جمهور ترامپ نیز آنجا باشد. ما این موضوع را حل خواهیم کرد.
فکر می‌کنم می‌توانیم با اطمینان بگوییم که ایران هرگز سلاح هسته‌ای نخواهد داشت.
ما کارهای زیادی برای انجام دادن داریم، اما امشب یک پیروزی بزرگ به دست آوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66145" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=Nrr4FKsFqVl8LrE46hsXpwPjfE_MN-iZ1lGlHzR3KHDOjbjewsfP-DBwHoDbwo4B1Ij53RgJDFNN7XwMsbqvzVs88iMas1Cpku_rORj7s_S3e1NxtLPZ3ndmgCET4P_FZZuePDPbsZMyC-4hPBzMUD8n1YtA5m5SytsoD3mtiMWbAEy0-Q7L2iOzfVHb4TFt_V2ziY_B_Oj_TnGdz4UaQzrZVcZwnWwtEJe9k2MSim6-Gx5NpNwFaZe-JkZvXyc5VOw3puRq4BMw-G_7yJ_jjjfmZzAp7wEGCO8VrA1P1n0ZN1g8s6oDB0BRc1YWm0Qqu1TFg3pt0Nx-apf69KnReA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=Nrr4FKsFqVl8LrE46hsXpwPjfE_MN-iZ1lGlHzR3KHDOjbjewsfP-DBwHoDbwo4B1Ij53RgJDFNN7XwMsbqvzVs88iMas1Cpku_rORj7s_S3e1NxtLPZ3ndmgCET4P_FZZuePDPbsZMyC-4hPBzMUD8n1YtA5m5SytsoD3mtiMWbAEy0-Q7L2iOzfVHb4TFt_V2ziY_B_Oj_TnGdz4UaQzrZVcZwnWwtEJe9k2MSim6-Gx5NpNwFaZe-JkZvXyc5VOw3puRq4BMw-G_7yJ_jjjfmZzAp7wEGCO8VrA1P1n0ZN1g8s6oDB0BRc1YWm0Qqu1TFg3pt0Nx-apf69KnReA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی خطاب به بسیجی‌ها:
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66144" target="_blank">📅 09:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
ترامپ به نیویورک تایمز :
اگر توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت یا در ازای ۲۰٪ از درآمدهای منطقه، واشنگتن را به نگهبان منطقه تبدیل خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/66143" target="_blank">📅 03:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=OC-otbkl80aojfReIMbia7lbxf8gJZcERvXjFWJKEoQhgZlzN07mid_NMo145st73cBFFVeFQIuY7KEeaCNvuV1ssGsbWxiYvrbDAnuyDmBuo9k6yAYBifNXSgrAHox7eITTWFoYrnimBwUF_OrmOd58FuQhF7uAs16EWCbP3Jhnu2x2iHceFseMcmdv1TgVIOfV2dxPzJfH_NcUAlXcXPUiNWJKrBpuyL351bSzeDRkFb8St37p7uVDlZavvGa4hzhkc3dHIzrgdbAi5tvl_mh4H6Enya6cYIgh3xjwGpz3EpCHE1uCx3eB0gRW9NEe0rZzVC-HlwVH2T26oTCcWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=OC-otbkl80aojfReIMbia7lbxf8gJZcERvXjFWJKEoQhgZlzN07mid_NMo145st73cBFFVeFQIuY7KEeaCNvuV1ssGsbWxiYvrbDAnuyDmBuo9k6yAYBifNXSgrAHox7eITTWFoYrnimBwUF_OrmOd58FuQhF7uAs16EWCbP3Jhnu2x2iHceFseMcmdv1TgVIOfV2dxPzJfH_NcUAlXcXPUiNWJKrBpuyL351bSzeDRkFb8St37p7uVDlZavvGa4hzhkc3dHIzrgdbAi5tvl_mh4H6Enya6cYIgh3xjwGpz3EpCHE1uCx3eB0gRW9NEe0rZzVC-HlwVH2T26oTCcWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم لبنان و نوچه‌های جمهوری اسلامی پس از اعلام توافق ایران و آمریکا
و عدم حملات از سوی اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/66142" target="_blank">📅 02:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
جزئیاتی از یادداشت تفاهم ایران و آمریکا:
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
آتش‌بس کامل در تمام مناطق و خروج ارتش اسرائیل از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/66141" target="_blank">📅 02:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBGf89-81J7eX5QF93d2scKyCNE1cxCn0xm6SNyx3Q5dkk-_5baxpzchRDZHgvEzT-jDGgI1pJv14Xhtkjld5ZNshI0w3tyY55TKP6PBtHLfMjlGWbPRivAo0mdibJfLmX8-OZFtOOkwk6q4jlAqMxlrxrRTJBiD9_ah_R15CkSnlEapiwPTlVz1uivHZeAqOmNkPvnTAbaHD_ARQ5a0IqH3tusuK-ZQD6VGjGxCjXpdzN_gud568kLMs8DKo7TWoiBJ5_gpKMRCui9lozGneYMCTmJkhZva27oQ_N0n7-bO3ZMTJ0gXP5MUl80bnWJDrZ97XcqDs59F_5ZaC7_sOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/66140" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/66139" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EXPIaCUF3T9uAfgYA4oMXm5MnmfXzIA1qP8gvbxd5J8j7X25Oy_fp_as-T--Qmnn7L8tOlSQrfKK9SN2K4OJVdTignCCIgPtr827091yrG4Lr3k515Na1gE-Mx3mjHWDsgHSaHzGlh6yJ8R8_ZWfcZnVV4-uMSbOrKk7P61RnnY1rBCfMWx5_ipPgeEr7DQaJkEsSOcHI8pkDdwyJ_k-fGyRHS01h89z8tzZf1P506vxwtqqfCa0H3-nC_4FVzAxAmRjtFrlRR330bKgWJvwYfniFWWeCeEDX41lu5IOgjC_H1Huo0xUheOGsqcmmOiEFG2lpKe5MNzqMem1gmdVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/66138" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEqTc63FuDVNVj2Xl8KD_Y_Rsc-8YSQIJG7hu2EaQSiLzxPYIavgOQSCGR3D7ap7p3MRC19is9W6XoDSh5xhD0cYAbeIIRqLJHZp83LePqR2O25OS9s5SFcXDhGh04gBRTtk70a8TnSHfSBzNeedmnbrOJuxKJmqTIBt9zExf_gTrOnH_hjI4QMeEFKc-u7Xl0q7uyHVT-dtG-fkwgXsdR9tQFZoqKxFV4sUXEcmVY1nxB54DSbuozMC7zxsncOPjJx8Cqn8_6UiALBLIrgc28JBvcmdYh7djQ_Xf7mBdVaZsLnPm-ST8MIPxrWVUNLM-vSjdNASWKxEfIqPgWbUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیتر شبکه خبر همراه با این تصویر
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/66137" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=i1vr600dqttzujOhhzNHC7vTiBadsODWpfQZ1_q6So7JKrZKgzs_9L7UjJHgfshImRtXxxzZBqt9xPJak8enKuA5dqmsJVOPWs3xjzD-HlzYyXW_JuSUUOc6_uncsgHcouDt32xOTofD1-Kqk-gbCxaPnbiH12eP8Q83ia4NJVjhiA1s49XjRlQPLNomh-DWExLi-0cORD93CbwIkh2QVPRg5-IKjIZ2NOWBoqQfl1_PWZ-DRkwSfPpN75IC1VcJG344LiRousWx2AyuDXNDfE6J-ShkLg0U_xoxCeTs_0JapqnTnTyT68_Fj6UPXT0hvwmAvcTm1DAlh2d8SEed2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=i1vr600dqttzujOhhzNHC7vTiBadsODWpfQZ1_q6So7JKrZKgzs_9L7UjJHgfshImRtXxxzZBqt9xPJak8enKuA5dqmsJVOPWs3xjzD-HlzYyXW_JuSUUOc6_uncsgHcouDt32xOTofD1-Kqk-gbCxaPnbiH12eP8Q83ia4NJVjhiA1s49XjRlQPLNomh-DWExLi-0cORD93CbwIkh2QVPRg5-IKjIZ2NOWBoqQfl1_PWZ-DRkwSfPpN75IC1VcJG344LiRousWx2AyuDXNDfE6J-ShkLg0U_xoxCeTs_0JapqnTnTyT68_Fj6UPXT0hvwmAvcTm1DAlh2d8SEed2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی‌خامنه‌ای یازده روز قبل از ترور:
امام حسین فرمود کسی مثل من با کسی مثل یزید بیعت نمیکنه: ملت ماهم بیعت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/66136" target="_blank">📅 01:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66134">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=BmT_aRJnpsW-bU5tq_zlINvEKkmuwgemVVWYuo__fn6jWvqaxHdZOrH5bRIYuknai2GAiXGXOpJk5_fHDLR__CD8ft6b4Ghmq0xn0Fe4N9eiGN2ojs3zuWToBcVFhfhsXlmMva_vn8vYVB6cEuIW3YGf4E8BlSgjM0mIIuJ8e4jzMvpy3Brf423dnqZIQZKq0B7EQuTw8rpGm2V3PpSyxeP64Zqw9lscZFJtZGJE13VYF6Oopn48EQy8dmJ0I5i6k846Fo6A8ls8OAWGdeto8a8_dKOHTy-lrKTyZqmqH14XSBooeOxYaK-IJyVRGoYRUzcnTFt-YCPNKS2I9E1fcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=BmT_aRJnpsW-bU5tq_zlINvEKkmuwgemVVWYuo__fn6jWvqaxHdZOrH5bRIYuknai2GAiXGXOpJk5_fHDLR__CD8ft6b4Ghmq0xn0Fe4N9eiGN2ojs3zuWToBcVFhfhsXlmMva_vn8vYVB6cEuIW3YGf4E8BlSgjM0mIIuJ8e4jzMvpy3Brf423dnqZIQZKq0B7EQuTw8rpGm2V3PpSyxeP64Zqw9lscZFJtZGJE13VYF6Oopn48EQy8dmJ0I5i6k846Fo6A8ls8OAWGdeto8a8_dKOHTy-lrKTyZqmqH14XSBooeOxYaK-IJyVRGoYRUzcnTFt-YCPNKS2I9E1fcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگر این توافق جمعه امضا بشه تازه میرسیم به شروع سناریو زنده یاد مانوک خدابخشیان.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66134" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66133">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
‼️
دبیرخانه شورای عالی امنیت ملی جمهوری اسلامی
:
آماده حمله سهمگین به اسرائیل بودیم اما به درخواست ترامپ و پس از گرفتن امتیازات لازم، از انجام این کار منصرف شده و‌ توافق صلح را پذیرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/66133" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66132">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd274791.mp4?token=cq-8saqq34CsJ-2L6IMhNKAzqAxKbVH5RkwB_ustTPyMvdQOoameVOdyFgrgwJ-x8ELj53s9mjTq-hLYbFWD7eSJFMBPvGoqkk5FwI1znjwAFPBddQjX3XqGLxrHZpRIoE6ELco-JwjIQPKJZfxrmbUy00H-e-T2v3-ghxQrBAxniQqeig1cL1PQi9KLPWBpvtugmabgKNB1TiIYSnIylztZ-ukCsPA3Der7jPVmAruyszlXjZT6JvPa84aCYonIC5kQCwx6SGpAlcOexxfcUfv2hDTz7AElyKDmUs76EaHppQot6soq91rcFqZZAB1Yyu4DoSZGNEWCkms32BaiNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd274791.mp4?token=cq-8saqq34CsJ-2L6IMhNKAzqAxKbVH5RkwB_ustTPyMvdQOoameVOdyFgrgwJ-x8ELj53s9mjTq-hLYbFWD7eSJFMBPvGoqkk5FwI1znjwAFPBddQjX3XqGLxrHZpRIoE6ELco-JwjIQPKJZfxrmbUy00H-e-T2v3-ghxQrBAxniQqeig1cL1PQi9KLPWBpvtugmabgKNB1TiIYSnIylztZ-ukCsPA3Der7jPVmAruyszlXjZT6JvPa84aCYonIC5kQCwx6SGpAlcOexxfcUfv2hDTz7AElyKDmUs76EaHppQot6soq91rcFqZZAB1Yyu4DoSZGNEWCkms32BaiNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دود سفید در کاخ سفید. طبق سنت، این به معنای امضای توافق‌نامه صلح جدید است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66132" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66131">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
📰
تسنیم: تا دقایقی دیگر مسئولان ایرانی درباره خبرهای منتشره راجع به تفاهم صحبت خواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66131" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66130">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeIBbfwv8WfBztXXh7g0U3tQBy26MxF0WgNNM0evAqM_gqm88reyNj0XqKtFEPt6A2NoWNugZymCbQ9RjXS0kwLvklQTlh0V7ELD6hB7qocwDCP6keGqaveUijZm9oDSDTT7DXIHRAeescsV9xZXOdmHGcWA3UnH2PcV2YHWG_DbMMAW02VppMP3snFk48j7QXqZ-nmabL9aYWLVmB0msdh_bpPjTnpnUJmM51ptWvgCAFzG4yKdUW4C2O94hMSk0TlbUCl8gpZN78-wzBmnAy10EgfTzBAJ74SwKDb9BCf3_nuT8ypv-hdGQInp2QY5gB6a1-TIHBktt5INz6ntYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
یکی جلو صداوسیما رو بگیره. چند دقیقه دیگه تیتر میزنه آمریکا رو نابود کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66130" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66129">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ_exaFGvVp9Ee00W9BZMu7XsU5htZXO6CRaxElfRp52q7FFh8LAy7qDGqeQQtgUMcjVZUpwuUVtEMbL5fi2-bpvUk6HoAmFlU0MXBPH-Kwvvj-rZb-ONCt5NTmnXDTr9MIMtOXp1_Si3xo3OSSMu15v-BZs1n2z0K2DOoFyhVR3AOhg0s97VN0tldqsjsxZIQluYA1wo1MsnNsg8WA05VWB-1rS_1EmeQj5Be54Xpkt0i31s9ymgeO07niTsgmL-5Sjref4EAY938Sk2wniIbSxsA-rx61AF--MZuktgpShicaHfZmA77lzFJHDPFvYoFPrPqI-5f8lxTyT32fKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان وقت چیه؟ آفرین حمله به ضاحیه بیروت
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66129" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66128">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66128" target="_blank">📅 01:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66127">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgmYgmEWGEs9Uh-Hm8B0H0fLsEIadonfJoZKZ3j79ANy7NsmBXNPW-wO_Ib0CMo4hyoqcSuNi-XNzIkAKonJ6BHFY-2JljifILu7pndLeXOWiWfGxfNKYigkiwbVylhseYllvgKGD7RDneY0ATe01HwnwdGnvfYFTwCS1kdsSF0Z0mJRz3AWHsGi9JLCsPPSW3s56F5N00nkqGOdQbfxRBhAeBlV3c-FtT2Vvfe8wlCQ0aOoL3WoCqbDYZWGDMn5NP-7MA0-KAQQgo_lRqT61qwvnYmOissRr4nbIYbtWqgVczMriX8pOBI8czFesetXm39xw8n7IFyEXKD7aYhlVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام خون رهبرتون گرفته شد برید خونه حالا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/66127" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66126">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=cpATydHY2g8n0T_YBCFiGxwkOXKfqVzcIORs9xS8h1SA_tzKn1Pn2FlkMzIfNOWNSiz_VfYSFAH4qcYVx0Zh7bgTR7aBLuIiOJhvwrs2fj92HbjOfDzetqc3gPjzKwSneZgJm4WoJwzuA6FdMzxNKASc3Ehf43lKTz3PP8TPDMBrh2zQx7MPf4HSCExFrYza5OnT2pwPm_kK3Omvq9xvsM7uZfjOGNovRwS6OxTdA42SEkvez-d2SBXiCRV6foZa6Wk7Ji6a-5tUjVNOQBKzsSTmQTbcFKa1BviVzpZnxAMr0NGXSvMTuLXRlJ_xO4cxYyIagEQi_scZUcznATpeFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=cpATydHY2g8n0T_YBCFiGxwkOXKfqVzcIORs9xS8h1SA_tzKn1Pn2FlkMzIfNOWNSiz_VfYSFAH4qcYVx0Zh7bgTR7aBLuIiOJhvwrs2fj92HbjOfDzetqc3gPjzKwSneZgJm4WoJwzuA6FdMzxNKASc3Ehf43lKTz3PP8TPDMBrh2zQx7MPf4HSCExFrYza5OnT2pwPm_kK3Omvq9xvsM7uZfjOGNovRwS6OxTdA42SEkvez-d2SBXiCRV6foZa6Wk7Ji6a-5tUjVNOQBKzsSTmQTbcFKa1BviVzpZnxAMr0NGXSvMTuLXRlJ_xO4cxYyIagEQi_scZUcznATpeFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش مجری شبکه خبر به امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66126" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66125">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVnm5t4jZzRygCwJe0XCe9_Y3vJIb7bjxITPo8bxfr-cvlo0Ojudhv8AQlJlLnJGhOClkyC1BaaeGx9MS1LDQesl2VsgADO8zaHyLkUhiEXJkHD-1JAfGx7ayG_y4qucGE1bjVcy1BiLslJR4IJneFYZ55Mgyiiyw3NZ21risN1FjYu2qd4p4hOe9LA3qr7HQaAFE95noVvFWCtMDUk7RXztNkXfkWXFC9p3LnYxn2R6xSvJBDi7CzTNMKVXEV_fs0O_XdX4-cT9YuRNbOoD-V2QyBCGr44bB8vUapxiyoi9yDZIgpYkYFiZr_52exl18p9UIzdwwnRzuoq-P6mDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری
؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد! رئیس‌جمهور دونالد ج. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66125" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66124">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3mpL9WdgRLOAvWvAez-6AnhjajAhsGKFwP9GSgpQKLKJSgxUucT8H1MxRALNE8MEOikcApST5VTghvKfIFLjLCwPpt7_q2QrDhegwnnnK0Ahe3kVTfSgkwGkqzuSmjn185f34vNaQwx9sruduo2JZmqPtp5W5t8xV5VlFI5nIgVHBY-Z5HZDltrQUrpTM-7k1w8K-C6pO2_pCbPKibl84oFhvhPbxauPSovynuHRz3U_4Rop6WTjQSZywVdqDwi9aMMs5IRCgbHrb74kIB0pNfco61wld0F4Cs3yEG0wL39-2yVNRi5d4r-tKeOekc1EA8fH4KEWWx3hzzvnt9a7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زیر نویس شبکه خبر:توافق با آمریکا انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66124" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66123">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
مراسم رسمی امضای توافق روز جمعه 19ژوئن در سوییس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66123" target="_blank">📅 00:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66122">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🇵🇰
🇵🇰
شهباز شریف نخست وزیر پاکستان:
پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران دست یافته‌ایم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد.
مراسم امضای رسمی این توافق‌نامه روز جمعه ۱۹ ژوئن در سوئیس برگزار خواهد شد.
از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این منازعه صمیمانه تشکر می‌کنیم. همچنین از برادرانمان در تلاش‌های میانجیگری و رهبری خردمندانه کشور قطر برای حمایت‌شان در رسیدن به این توافق قدردانی می‌نماییم. به طور ویژه از رهبری خردمندانه عربستان سعودی و جمهوری ترکیه برای مشارکت‌های ارزشمندشان در این زمینه تشکر می‌کنیم.
پس از امضای توافق‌نامه، میانجی‌ها تسهیل‌کننده سلسله‌ای از جلسات در این هفته خواهند بود. این بحث‌های مقدماتی پیش از اجرا، پایه و اساس مذاکرات فنی و مراسم امضای رسمی را فراهم خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66122" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66121">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
نتانیاهو از این توافق حمایت می کند و این برای او خوب است زیرا تحت هر شرایطی مانع از دستیابی ایران به سلاح هسته ای می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66121" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66120">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
محاصره دریایی اعمال شده علیه ایران موفقیت‌آمیز و قدرتمندتر از حملات است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66120" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
من هرگز به تغییر رژیم در ایران علاقه‌ای نداشته‌ام و در حال حاضر با گروه سوم که منطقی‌ترین هستند، سر و کار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66119" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: ایران در ازای توافق پول نقد دریافت نخواهد کرد، اما ممکن است تحریم‌ها کاهش یابد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66118" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
ما وقتی آماده باشیم، مواد هسته‌ای را دریافت خواهیم کرد و این اتفاق ظرف یک یا دو ماه رخ خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66117" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyvMNS6q0f8amKCIMPewMW44OPTRiWikiR9WPC4mzYYcTojKbMmOlA6vymArC2-P1QKYnTI-F44KQxrGf6picIxS7EhUVmOPrgZZhU2l6Ry9KsE2gJ-oDrxzp08vPC1sKKsRyo25ZtIrkY3Z6-TFCykA4nK7rHvombCjDU7REXUIvjAPjrbX4LTs8DVYBgn9kusHGpY7Rd3kL5QVMh78KXbzui-iH7dmHaqoWXTdxJLW7mM-ax0hCX1_Dtd6BBLb76gLaLTKz96ms7jZg514xqTXfqIMe_4OPw6wZcQxkWsEQPM9XBba4M2F2h1cjJNOdfXKxv80LxrHgVd1qC6OZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محتوای تماس بی‌بی با ترامپ:
#hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66116" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ و نتانیاهو دقایقی پیش به صورت تلفنی گفتگو کردند
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66115" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
ترامپ: این توافق به صورت الکترونیکی، یا توسط من یا معاون رئیس جمهور ونس، امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66114" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
بزودی بیانه ای صادر خواهم کرد تا تایید کنم ایالات متحده با توافق با ایران موافق کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66113" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
#غیررسمی؛تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66112" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjpcoJOAMD6wIDz4riwiCtgNoUBsi_0P0_ZaguKjvtBNrvXLtSSLWc5ybyymU5Vx55hJL6mDIKDngx-7M6OU_AKOoy_gSuug2FbIPyvCuVBTBQSHYlbwKdXmtt8qBHDF-SD-04MoRYLe7i3bk91pw7V8JGK1wVb-48F5p9S6aZn6kffyA1Ge65F75K-bp_0VK_BptooC0IiHNFX0Z2CF3SrfzVMZqYqJaJjUnWPEpd-X-DoHmRIbjmKsmWdmegcbnSuNO84C9idYweHkIQMA8dZd-WxL0jCn4QDuLM90E2n45J70nA7VXkEv4kU37dRKwjCXJGNYQcI20NBICPH8pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت وزیر کشور پاکستان: الله اکبر.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66111" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc582fcae.mp4?token=dBmw11l7gdefEX7rJl179YgJ1TRN17UTYcrESvSW2kc2gU611IebFb0RCkAf5-Oo2Cm3qnwOfpprIjKsPeRXke_0HqXIA11P4ORGZOucSHlElxLtRwIu-5VPR-BwHizmbJjnsM8wO5uffRvhLST2DIsDWtks5j18lB7My2tPcJ_g2lPBdhI9B47c0rcdCnpFSv1b1jIPVXvI4HCqZQcLR6yrsZjBf-YtNROPDt9lHHVnsPBFx_8DaU88wZhwu_RyfHo28HyI0Q8krle7ZsWNQoTmOyxFddamUdXlIxvLWH1nJ-1QgatL6BF7dg0D6ijmKAFDL88OEIpBtUVqtReUqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc582fcae.mp4?token=dBmw11l7gdefEX7rJl179YgJ1TRN17UTYcrESvSW2kc2gU611IebFb0RCkAf5-Oo2Cm3qnwOfpprIjKsPeRXke_0HqXIA11P4ORGZOucSHlElxLtRwIu-5VPR-BwHizmbJjnsM8wO5uffRvhLST2DIsDWtks5j18lB7My2tPcJ_g2lPBdhI9B47c0rcdCnpFSv1b1jIPVXvI4HCqZQcLR6yrsZjBf-YtNROPDt9lHHVnsPBFx_8DaU88wZhwu_RyfHo28HyI0Q8krle7ZsWNQoTmOyxFddamUdXlIxvLWH1nJ-1QgatL6BF7dg0D6ijmKAFDL88OEIpBtUVqtReUqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صداوسیما تو لبنان:
انشاالله امشب قراره ایران، یمن و حزب‌الله به صورت همزمان به اسرائیل حمله کنن و انتقام بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66110" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
#غیررسمی
؛
تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66109" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBxXu0wqEUCwQ4QA8c15JGmWqLLPhKar7GwZgw6SV5zGr2Ro2rD8zI1DjTh__gcwD76HWQAHwi5NlKYBnrT-S9YTebM186VyhuVfWFuoDzRkNwCWtUPdb5SRU5LPdhFqbgOwEUH80qGMiF4maaSeWt_opuKHmWBRo8liUXVdc3an9agDO2znGcGBQyQaN0W64dFV5M5PFG--ulAGD1OlxHGpzKgKiqdSZOJGdf91XT2ko9uF7iu2IJfrZo_2_pEguviS39n0SoxGKeRG5D_Q6EvNUXjDbLiWmcBhNMf5kBg56-OC7t_twneTdCs41hi1cN22zLPLrH7VNsi0u1EJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرزیدنت ترامپ از طریق Truth Social:
ایران هرگز سلاح هسته ای نخواهد داشت و تنگه هرمز به زودی برای تجارت باز خواهد شد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66108" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66107">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
#فوری
؛ ynet:
ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایران به اسرائیل جلوگیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66107" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66106">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">محمد باقر قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی‌ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66106" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66105">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بشتابیدددد که فاک بت آنالیز از بازی ژاپن و هلند گذاشته سریععع بیایید و ازش استفاده کنید
💸
@FutballFuckBet
💸
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66105" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
کابینه اسرائیل:
اگر ایران حمله کند، ما نیز حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66104" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66103">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsVn9Ekl2v5pt9KcGHYe1BTnSUjV9Aum5PCzuJ9gOFqCaJY0ts4eeRr7purNgJ558Qr4Y6clVB9dJQ5xTnukymphmFwiQ3ecAtafXQtGcFP2bZCLpqUlq6UD403TXLvhSnVcZWUD4D7rOeIEfEPAuaGHPdBSfnmO9JTXn3YYyiM30HsHWqMcqxRBTknVmcx-ea6dd55-Ycz9wJD3yIYbKmLTDGApb9ig_ih0qDxQwxdfmUSmYoiZ3J3duO1eClGOTKqcbZJnysjM4au-NeVCQpq1y6RRmurX_H5YTyeTIzAqfwdAh5cIRvkdJQddot1R1LwgkAEey4zUcyNKaR0xtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور هیتلر در ورزشگاه و حمایت از تیم ملی آلمان.
آلمان این بازی رو۷/۱ برد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66103" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66102">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8m4E2QbmeRIyiIzjMmXT159VogFrsvxaHd8nzS8eYa1nGyNDT5XlwSwnX5UoZRQ9nVBQJtGKOrT17rmL9tEAtOdBq-6fzLgC0zvUM_k_oXzLIjd6smUQFdarGk-8HoOBjSJz4NlI8Be15A6ippaVv577tK8o8jzMwBCEaBDRvCRdJu5W8PMbqcvLw5q9Dy8H0DXHnM0WKs9_bEuD154xpUwslZ4UI0U5hGWK_XbpX2jsQWbI2EFnTBeW2ZC5zk3LAEwWTBUGFhuNpRITEkpZwPE884Uw0m8FPQCAkiJ3alHzupbn4hnxE78AtqZMl5ch3lEAfyUXojrXKo2ziRZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان غیور لبنان و دیپلماسی مقتدرانهٔ جمهوری اسلامی ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66102" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66101">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
به گزارش Ynet:
نتانیاهو درخواست‌های ترامپ برای توقف آتش‌بس علیه لبنان و عقب‌نشینی نیروهای ارتش اسرائیل از این کشور را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66101" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66100">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری تسنیم: حریم هوایی غرب ایران بسته، و تمام پروازها در این مسیر لغو شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66100" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
