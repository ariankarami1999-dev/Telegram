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
<img src="https://cdn4.telesco.pe/file/DMbufwhNWVs3kY7FiJwsPL0X2BHS37_PSpRVEIegdQ4-vah5PTwd60Jo7BJUM3kOUUvZWwzEWfsehRi1krhM2UhcbM7YAvVuJPLNaXoiBA36D6J_GzTFJVkyKkxNpK-ECQnvBRMAxU9MbesR4Y6SjMUBebwVj7ADjPL12um68FQ3u0p6bpO3dcCfddelBo-MHKn_fea__-HMTgvbR5mTbauUwb3lgulNlcrFRxOehSqQdVshzhTI3gRlyvyYv079jyPZxdeYvw4nPI0EAdgEt9DMhv14Fq0iL1uMaan-xytx3QW56RiQxyi5cjJN3I5PsNge08GR41_1PksoyvtJ9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 989K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 11:56:10</div>
<hr>

<div class="tg-post" id="msg-139560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فارس: به خاطر بسته بودن تنگه هرمز قیمت گوشت گاو تو آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/139560" target="_blank">📅 11:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما با کشورهای منطقه همواره در تماس هستیم.
🔴
از همان نخستین روزهای جنگ تحمیلی، به‌صورت منظم در تماس بوده‌ایم
🔴
دانایان منطقه به‌خوبی می‌دانند که امنیت در منطقه تجزیه‌ناپذیر است.
🔴
ناامنی علیه یک کشور منطقه، خواه‌ناخواه به سایر کشورهای منطقه نیز سرایت می‌کند.
🔴
همچنین به‌خوبی دریافته‌اند که حضور نظامی آمریکا ناامن‌ساز و ثبات‌زدا است.
🔴
طبیعتاً همه کسانی که واقعاً صادقانه به دنبال برقراری امنیت هستند، تلاش می‌کنند مانع از تشدید درگیری‌ها شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/139559" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
👈
آیا ایران به حمله اوکراین به کشتی ایرانی پاسخ می‌دهد؟
‏
🔴
بقایی، سخنگوی وزارت خارجه: به گفته مقامات اوکراینی این اقدام غیرعمد بود اما شواهد نشان می‌دهد که این حمله عامدانه بوده است.
‏
🔴
هر اقدامی لازم باشد انجام می‌دهیم که هم اوکراین پاسخگو باشد و هم اینکه دیگر این اتفاق نیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/139558" target="_blank">📅 11:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92447bf90.mp4?token=n36I5vANg78pBOiFUmDzstKKreoj3eW2Rf4ng4athkVS7_CA1fcJpOZ6xzoTOEYjkihs3gsHZuBbPz0vjLaSSdiC8g8Deel3Nudam9tC92D3EBpaK0b9Y3Fd7YYw0EJg3nh66ad1Ywg74hjZeuJNYoQ6rxO7P1RBpROAEAaeRRRSjmv_MAHV3LzoXhUXXq2FxavcXb_f7aC4SzKMYk4lR30g68RWxfVTKRduW0kdjRvXngoaMsQP-bIev_dFsX3avoVR1-YAcD0tcYeJuolWWyC28jWHv3coEW1xKTUlDGMg2VlxvkQoBHzBnIpg_NO7ber0CVNWjFkhm9LjtgKItzRbYIYOuw4x76FZ5B0sMu7jwKJDRrP23nVY_6TzvlxPyAoalShNmPV2LhKeOIyNOeYNPFKCCatzA4sQOTrZ6ANFVseI15qJQEelBANBKpRMFFKRjuusmEBB8Xovy2GZzKc-aHLPQxDuzt-e_28o14CHSkI4ds8AFUSX0XzIcaJqzGZ1vqBk-A-DK6d0awVuNzF1cODIKDgPEfnlOjilksw1lqZELziHpR05pgTEDrFS7yQYnGCDeco8MquaIMWUoASPahqq8pQQDsCMrWtG2VK438qFAw6PbRX4vmGwjApZK_VT0WwGKYONExCuXbM1JdARZBbuf87oh0cEIELVX10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92447bf90.mp4?token=n36I5vANg78pBOiFUmDzstKKreoj3eW2Rf4ng4athkVS7_CA1fcJpOZ6xzoTOEYjkihs3gsHZuBbPz0vjLaSSdiC8g8Deel3Nudam9tC92D3EBpaK0b9Y3Fd7YYw0EJg3nh66ad1Ywg74hjZeuJNYoQ6rxO7P1RBpROAEAaeRRRSjmv_MAHV3LzoXhUXXq2FxavcXb_f7aC4SzKMYk4lR30g68RWxfVTKRduW0kdjRvXngoaMsQP-bIev_dFsX3avoVR1-YAcD0tcYeJuolWWyC28jWHv3coEW1xKTUlDGMg2VlxvkQoBHzBnIpg_NO7ber0CVNWjFkhm9LjtgKItzRbYIYOuw4x76FZ5B0sMu7jwKJDRrP23nVY_6TzvlxPyAoalShNmPV2LhKeOIyNOeYNPFKCCatzA4sQOTrZ6ANFVseI15qJQEelBANBKpRMFFKRjuusmEBB8Xovy2GZzKc-aHLPQxDuzt-e_28o14CHSkI4ds8AFUSX0XzIcaJqzGZ1vqBk-A-DK6d0awVuNzF1cODIKDgPEfnlOjilksw1lqZELziHpR05pgTEDrFS7yQYnGCDeco8MquaIMWUoASPahqq8pQQDsCMrWtG2VK438qFAw6PbRX4vmGwjApZK_VT0WwGKYONExCuXbM1JdARZBbuf87oh0cEIELVX10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میانجی‌گر جدیدی به میانجیگران موجود اضافه نکرده‌ایم
🔴
بقایی: پاکستان میانجی‌گر ایران و آمریکا است، میانجی‌گر جدیدی از جمله چین اضافه نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/139557" target="_blank">📅 11:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بقایی: ما الان مذاکره با آمریکا نداریم/ مادامی که نقض عهد آمریکا ادامه دارد وضعیت تنگه هرمز تغییری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139556" target="_blank">📅 11:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139555">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بقایی: ما الان مذاکره با آمریکا نداریم/ مادامی که نقض عهد آمریکا ادامه دارد وضعیت تنگه هرمز تغییری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/139555" target="_blank">📅 11:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/139554" target="_blank">📅 11:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfCC51gmvTe_FAv2McM5Z48Dnr8Je3oNvo1TSRiyjA0QzUBdtkjrJ2eLmQdN-mC5NWL-lDVWzS_GJzKuwhayptKeP0JWmeXfbuKIOEHVoqBUXsFPrKebTo_BsgNfHCNJB0LkQG056ayEetA1Vsi0uleraog3WeBk9Vh-zASvgJXkRqVwH91xnZ30E4iNmyMGxtdJQRV4RL18kyO3hNhiLGcz1KRSDZH987YNi1zWBVbvj3IavwpzD7LxQbewK0U2tZj184Xt9iiR3BrHs7GiyXZrRxLDLV4MSPcHv_c7xxlbHH80kg4muwl7w1ErGt8lJjXSBayA3-vjj4g2MMWQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت برنت ۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/139553" target="_blank">📅 11:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcXIEu6j1vvwLrAmijD4Hf9v1pP3zyUkQcYYn3pxLlGZLChF9WEbSLEqqecxmnT15foMRZRFjhPiRehnJffKWFRPQeSPi3zmNMzgfLMYCjBYYsgw-o_RmUqVLFZJGpp9dla-tZHZ-XReuGpkHAHJgpHEA3bII0kV4aAkjrpBkFgOKkcFkBocW5Fv70n2W-ay9QNlJliuX_fhSgoTDL18hG04MH7l7IFqWAd3gXqQEfm7smGGL1NNNXVuykOQA8jcZDjFV61svV-x5K9BeQaIR5kIbZ5ReOOnJXh5ZJJlcHEf13EtRpYGmm3qSxjst7kgigu9aUoVGLk12c2HnOU2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSSfPdcj0UTsNKyAIWXweAS5P_H6nv2VjI-MJzY6EdDgBdJ4VOd3gHl0PSoV9YII0DwdRgCrGHiP8MKJNW1B50WlXNGbUauuHNYCwarZYRXIhFEDfUThBgHjiKysaZ28UUt_WGugpf8myW4A-YS7qsvCc2M_QS1D5OLtRy_2R5ZHw32RvNixbg_RlO4SN9rydZNjcK4RpnegjJZ23xLqJcJcuj2h5p775dXYJkRPqoEmjoHGyeC0joaYpoYr7pV1j-l1V2_l6FCyoD8MMYKM51wkoegfQreZH1cwdvnA_kuETEiD9CFdWeHqGyz6iMSJKaMOOg8CwY_-z2oLIQ3WDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YX-y7QmA7fY4ePU2RzbNbRtKAtgIZ6xfGsEGWbp9uloV_VTdShuk4EuIqCek83fh0dxFy6-bapAYQr9JLkggdUTchN7K5vro18CfVXEh6kCO-3NRvzWOj3s5DUT89eKvktayTU_burAVHUFkYY9Fj3h27BmknNmHFbPZ1xHUYNBezDp_rOtMbwsjEeE4M6xwItG9oly-Rg5RYW5P4TzMbTuLO8S0C30DU6U5999AM4TYR8PTJUkN9odwWfi8XJdpNk2czetYc9kDKxz-K5Nhh_9XOZMFQXyDfp6Cgo_S1T9mU-FbX8zVQw-NSEH1WF_iuExbZsmEn8yqKOpOf85i_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داشتم قیمت PS5 و تو دیجی کالا چک میکردم که چشمم خورد به کامنت‌هاش...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/139550" target="_blank">📅 11:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
یه سریا همه چیشون شده سیاسی، دین و زندگی و غذا خوردن حتی ریدنشون</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/139549" target="_blank">📅 11:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/139548" target="_blank">📅 11:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/139547" target="_blank">📅 11:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات با عمان در چند روز گذشته با جدیت ادامه پیدا کرده است
🔴
تماس وزیر خارجه با همتایانش با هدف جلوگیری از تشدید ناامنی و تامین منافع ملی ایران ادامه داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/139546" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d62bba082.mp4?token=O5EwoVuY2T5Zf8Vf2Nqqty3VSDRZkoWlATM4xYNizQMRIXeWDx3prs27cYXAoLbyg5M3OX8b09OWM0hldoHv_RwgfX2tD_yol0lL686_0ra2jKpghTH-WxQbYxuy-yc_2acIDvo9QR4f_A9MAhtE_XjMg7PtG0uzKwpVsmHnaCgyiq9iIe2xvbZjt30ATVooES7II26nm_qUsROIvc_Bf-KvQWRDfUaXQQIMbmRYKR7-oeEf4T3vTk0brb9Md3omYGSzj2JI2XCRWNSurm9UeZ563gI-SRh7ysw0ABORIVqrTaIDygzJWcbhDpD-5v7h1VnxWNiTbjdOnQ6T3enZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d62bba082.mp4?token=O5EwoVuY2T5Zf8Vf2Nqqty3VSDRZkoWlATM4xYNizQMRIXeWDx3prs27cYXAoLbyg5M3OX8b09OWM0hldoHv_RwgfX2tD_yol0lL686_0ra2jKpghTH-WxQbYxuy-yc_2acIDvo9QR4f_A9MAhtE_XjMg7PtG0uzKwpVsmHnaCgyiq9iIe2xvbZjt30ATVooES7II26nm_qUsROIvc_Bf-KvQWRDfUaXQQIMbmRYKR7-oeEf4T3vTk0brb9Md3omYGSzj2JI2XCRWNSurm9UeZ563gI-SRh7ysw0ABORIVqrTaIDygzJWcbhDpD-5v7h1VnxWNiTbjdOnQ6T3enZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: ‌ در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/139545" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/139544" target="_blank">📅 10:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سناتور روس: مناقشه پیرامون ایران احتمالا تا اوایل 2027 حل و فصل می‌شود
🔴
گریگوری کاراسین رئیس کمیته امور بین‌الملل شورای فدراسیون روسیه گفت، باور ندارم که مناقشه پیرامون ایران سال‌ها طول بکشد، طبق منطق رویدادها فکر می‌کنم این مناقشه تا پایان سال جاری یا تقریبا اوایل سال آینده (2027) حل و فصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/139543" target="_blank">📅 10:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkG5Y8EbaFN1CDE1X5Wqr5b-VWHG6V0tvSpDko3mHK7gJp2lV9EO9LNbihOJ_KemKImxMtl-XaV5bKBpHKAWi4Tdl9zawfPTfCcBwSJ4RAOs7_Tsndqq11GafphooZHVtUxeha8mbe4GmRvpwlK1Kez7BH4oMUliBIOJLoOh11cp4DEsB42M7DpQDNjmaetibxPUprCK4MZDsI-SHt9QfkTlkP1JfZrGbJEPb4D6X4EXrqbNSsGd_q5jdYHYnLZKaY5hrjaDwG2AZVfnakA_z7rozuIgbcvupBWUPAK6fXv6dJSfni4FfUs_IGNcRgfpHaahocpH0i0Y9nOa-t-pHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خط فقر برای یه خانواده ۴ نفره در تهران به ۹۰ میلیون تومن رسیده. این یعنی اگه درآمد کل خانواده از این مبلغ کمتر باشه، زیر خط فقر حساب می‌شن؛ در حالی که حقوق وزارت کار فقط ۱۷ میلیون تومنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/139542" target="_blank">📅 10:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
الجزیره: پاکستان و قطر نمایندگانی را برای مذاکرات آمریکا و ایران اعزام خواهند کرد
🔴
تماس‌های عراقچی با مقام‌های پاکستان، عربستان و عراق در شکل‌گیری این روند نقش داشته است
🔴
طبق گزارش الجزیره، هدف این است که روند گفت‌وگوها هرچه سریع‌تر آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139541" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139540">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f5ad2194.mp4?token=ozV608yGOPb_77Lxk8NtWx8Sp-foJAq7es5eWuCz2cCPHOl6QRDBkzGaLd4fY14_5gixDamMR8MUVjTkkfvCCw16g7xaRRumxdDtwTU0Bl_JfvGKUoeg-WiWwTTRp98Q5NSkCGYZ34NKgg6LVMBwohqWuyGPk0Q_6x7_JdM5BEsudoyVKCXgH6be4yMpJWZGVC_w5PJaC8gC5lqGMV5G0wXfmL8Ht8cpBM9RPf6cKC9-J8fT_HX-X-D4PLsf-DDPXZ0a1kvx1q6jrGScsCXy3SJ7JV1EwKoiLZDSH7fsFL8OoiK9piSlfrS-aD7scL8pj6r9xLAbgweVaZCY-AmUbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f5ad2194.mp4?token=ozV608yGOPb_77Lxk8NtWx8Sp-foJAq7es5eWuCz2cCPHOl6QRDBkzGaLd4fY14_5gixDamMR8MUVjTkkfvCCw16g7xaRRumxdDtwTU0Bl_JfvGKUoeg-WiWwTTRp98Q5NSkCGYZ34NKgg6LVMBwohqWuyGPk0Q_6x7_JdM5BEsudoyVKCXgH6be4yMpJWZGVC_w5PJaC8gC5lqGMV5G0wXfmL8Ht8cpBM9RPf6cKC9-J8fT_HX-X-D4PLsf-DDPXZ0a1kvx1q6jrGScsCXy3SJ7JV1EwKoiLZDSH7fsFL8OoiK9piSlfrS-aD7scL8pj6r9xLAbgweVaZCY-AmUbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی صنعت آب کشور: وضعیت برق آبی کشور بسیار مناسب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/139540" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرگزاری میزان اعلام کرد که صبح امروز امید بهزاد و پوریا صفوت، زندانی‌های سیاسی به اتهام همکاری با موساد و ارسال عکس و فیلم برای اونها اعدام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/139539" target="_blank">📅 10:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
الجزیره: وزیر کشور پاکستان و طرف قطری نمایندگانی برای آغاز مذاکرات ایران و آمریکا اعزام خواهند کرد تا این روند هرچه سریع‌تر آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/139538" target="_blank">📅 10:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مقام آمریکایی به CBS: پیشنهاد ترامپ بازگشت به مذاکرات و حل‌وفصل مسائل باقی‌مانده است.
🔴
هنوز توافقی با ایران حاصل نشده، اما تلاش‌های میانجی‌گرانه در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/139537" target="_blank">📅 10:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLjNqH3IBIMk19hMjg79ReKDWoYypxrR8Ke0kz2TmkfFldbhmeUTDRGYqaF4NwYx2PKthziqi89xP_k4HoDebVILxT7BywlZ-UTzK-3gtoY-oWysiHIbVC2qjIqFgE2IR6cmlCWIEA9MV5lERqfJ8ZotyMoMYUkMvI8gk7JGSzu6TXvIUGyjfYSOiQoBx7hMmqAG4Enxwg8BCfuWhypSPlKBBaG4ifMlPRouhVi0iMdn1Zv8SlLhgTJVrI1VL9ZUgBhYJkdrNmgTmIaBIflfATouSHC5j4kJU1DC8s13Qc7wfM4savrVrABYgqLZ4z2kw9DDgJV5Hh2AQRyA9KvkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ تصویری تولید شده با هوش مصنوعی از خود در کنار جورج واشنگتن  و آبراهام لینکلن منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139536" target="_blank">📅 09:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/73daa7c99d.mp4?token=BDTBt4AgLdoZoLRK9RJbHruSOPlg4I_HNNKWPWt1c-ewprTb02yVg6GkOTeJjjCo-b-UuMB-Be5GKl5PKlUnJ75G8H46V8HxXV8oDTs4m5EWOm229hzIzIHuAsMZ1AcXEUR-uGkbqQsP6uTFdPrVTZLn95N2zK4nerLOiQn8dF8WmiMNl55mNJU3HaJieZ03WSXeeVMi47QKjUpy0qRjiXXXn1vwxc_Gz4ieYNV0BoSaGykKhFrJEE3b5WHZjwrJdP4hj7Kr41hLTNyUKrMBhxDyuBghYkCyG5L_NslZbVa5UhJiOKz1PmLAQ0GwUeE4uzE0Q4pDX3vgR28VFL74Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/73daa7c99d.mp4?token=BDTBt4AgLdoZoLRK9RJbHruSOPlg4I_HNNKWPWt1c-ewprTb02yVg6GkOTeJjjCo-b-UuMB-Be5GKl5PKlUnJ75G8H46V8HxXV8oDTs4m5EWOm229hzIzIHuAsMZ1AcXEUR-uGkbqQsP6uTFdPrVTZLn95N2zK4nerLOiQn8dF8WmiMNl55mNJU3HaJieZ03WSXeeVMi47QKjUpy0qRjiXXXn1vwxc_Gz4ieYNV0BoSaGykKhFrJEE3b5WHZjwrJdP4hj7Kr41hLTNyUKrMBhxDyuBghYkCyG5L_NslZbVa5UhJiOKz1PmLAQ0GwUeE4uzE0Q4pDX3vgR28VFL74Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار در پالایشگاه استان صلاح الدین عراق به دلیل نقص فنی
🔴
بر اساس اعلام منابع رسانه‌ای عربی، انفجاری در واحد هیدروژن پالایشگاه بیجی در استان صلاح الدین عراق به دلیل نقص فنی، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/139535" target="_blank">📅 09:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
آکسیوس: خالد بن سلمان، وزیر دفاع عربستان سعودی در سفر به آمریکا پیام ولیعهد سعودی مبنی بر ضرورت کاهش تنش با ایران را به ترامپ منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/139534" target="_blank">📅 09:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139533">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ساعاتی پیش‌زلزله ۵ ریشتری قاهره را لرزاند و به دنبال آن، هشدار امنیتی برای برخی مناطق در اسرائیل نیز صادر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139533" target="_blank">📅 09:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139532">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3v4NX1Y89km9_IfneRs4I2BFq_gjM2E1uP7SO_73a8I5hR7VqV5Ce8WIJ7KtR679zcXytwmZ8UPpyM55qqTrhEj92vPSDDHGr6u3kkQd-LdbgOOaBgPjzGdDtUnRwUnCqB95vrN7ZkNtD9DGBTvFgzRE-Pw72Y1rvPk9uTDnFDaVG3Pa8NUlLYyf8sfgyj8nyeWQr1dcJD2U_oto7l9NiC0wzXpOkBJ7nhKdzg1fT-R0CKUntLc2rAxrb_e_25bY2cq3H9sSy4Fj3USdmdDfeEEHW_qZhLFig04XwkIo5R5qs2FvhXHDy5MF9FklI3riM_YkMc-fTlm_b9-nzL2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: قالیباف و پزشکیان شکست عشقی خورده اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/139532" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139531">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDhXNnHbgtslJebllo1OihZJhf6mwzrBHlJW2x3-MDMz4LHZViZ9jgYumZOyxfmZynD38mL06fX-lBPT7Z_OK4jqfNNqUTfjOodhYOfb5Ogf5pEZQrfoHPYZLTysO_O104jplCWFBGep-9KXXUfTdl7YRvfHfIzdvKju3QNEq8zJuGCFub3Nj8y0C52zhuEleChbXVUOvkqMj_eTQ3RlfFqk2mo6fYp7WgJzSDxhxQSHyXG2ImYfycAfo4DJrkqaCRokUkk3G2JbmOWp1ddzFeS8JJ1gV-5PGtFCXYzNn_MtG20ZaDBRQ9R4kPDzIgCskS0chaQbEb4r3xi9GWO-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری سنگین C-17A نیروی هوایی آمریکا، امروز از پایگاه هوایی اوسان در کره جنوبی به پایگاه هوایی علی السالم در کویت پرواز کرد
🔴
این هواپیما احتمالاً حامل موشک‌های رهگیر سامانه‌های پدافند هوایی یا خود سامانه پدافند هوایی تاد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/139531" target="_blank">📅 09:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139530">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Clq564Df8tOYG-aAxrpOpFq-oFBV6GiYfniY6Q55dD6fxQaVTqfRRxUehTzeQ7pU7olIua6Qu8aGPLHe1bJ3aZsbo8kZqBBDJo48Rh82WTsfr22mNeqRxBIJmJW4EuIMi54dO65LiKq6pMQvIkp0EJEiPvPvHWSG9zpDf2BlfEW2dzpb6VDLu8aNRyfJp2EccbZn7ehwColBU-0VkgPeOAsgl0JNCU_MkWPQFBJyS3VRQti3Snlg1l-sDykM_CbCC8e4-BeBy0WfhkoYDIpDambiEFbhmeGJtm3S9kw6xln4KFkih6Wuj270PfptWJkbU_ZkeaJDOewmuAy-bvxRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه اگهی عجیب وایرال شده تو دیوار
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139530" target="_blank">📅 09:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884692a20b.mp4?token=i-FXajITOCcgHsVldX62lxOwJF1H0Tx2tiY0xzjORdV0Gv6CoaNLgxpLgezcHVK_YsCSCcSemdkmKFQC3nXqMJeWxufKA5X__PI-bpZv31_YPh3RgamfwzA9kHzuau2ktfIx7R7Y4H0v-Pst_9QsKNch-SjveF8SQqaV3KqDn-YrmdRS-OzgeM_rdgBH2rkDyN3WqjlMwE5tfURqc5K_eXN69BaOGltZYOl4jr8-jVNvAc63LaMC9ARYtwnpOCrPcbQL_q5mkaYM_X001q4a7SQm_IJrgMG6zwYK5dvLKOc-Hjsdp8p2Bac2WGrBhkdfBf10hxioZfmz4dtAYvn7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884692a20b.mp4?token=i-FXajITOCcgHsVldX62lxOwJF1H0Tx2tiY0xzjORdV0Gv6CoaNLgxpLgezcHVK_YsCSCcSemdkmKFQC3nXqMJeWxufKA5X__PI-bpZv31_YPh3RgamfwzA9kHzuau2ktfIx7R7Y4H0v-Pst_9QsKNch-SjveF8SQqaV3KqDn-YrmdRS-OzgeM_rdgBH2rkDyN3WqjlMwE5tfURqc5K_eXN69BaOGltZYOl4jr8-jVNvAc63LaMC9ARYtwnpOCrPcbQL_q5mkaYM_X001q4a7SQm_IJrgMG6zwYK5dvLKOc-Hjsdp8p2Bac2WGrBhkdfBf10hxioZfmz4dtAYvn7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افراد مراکشی در سئوتا اسپانیا اکنون در حال غارت خیابان‌ها هستند و شهروندان محلی را خشمگین کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139529" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139528">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یک مقام آمریکایی:  هنوز به توافقی با ایران دست نیافته‌ایم، اما تلاش‌های میانجی‌گری همچنان ادامه دارد.
🔴
پیشنهاد ترامپ شامل باز کردن تنگه هرمز و توقف حملات ایران و شبه‌نظامیان وابسته به آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139528" target="_blank">📅 09:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh5QxCIn3T40nRnmY4esxZsK9uFsJ-zdM4ISgw1aIRBoongp8HqHTOGCSo7GnASq0AVNft2HHjfCijcinc-xza_Tcpo5DPnUKnMRqyG8FWZjYMy0dMagqjqKt3cZlIK2bZccYsoEcvxfxLfdyl6qNzLzwC66A2oaCnSmDbJrQ_y2ssXNz4Ytf7wuEa4sY8JmhE8zIxqciCFPgJd0fvGpQTZNMrHobRPp6Q1GYcoPOJj4HfXcSDcaFrR11TxeYofOsTbK_Z0cGm8xEicb_5mw-mEBMv2DDjVzvQ0V944ki1andK68HHq5ODm1FIz60mkp1QD8VPljh-uaHtIZD47v9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت با حتمال مذاکرات به 83 دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/139527" target="_blank">📅 09:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139526">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که با استفاده از پهپادها، ۴ فروند کشتی اوکراینی در دریای سیاه و همچنین بندر میکولائیف را که محموله‌های نظامی حمل می‌کردند، هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/139526" target="_blank">📅 09:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139525">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVLnzf07SogiOgWCz9AyMMrQExC70gzyVgTEUDtdnYL9X_a3bBm03CAWtKv2mf8HuvjpG1hkBO3gCVeWJXVk-wuMBZbRu9PQIuP-mELHBe0U-2BYsHiDZqaZLiO-e927jv0hHn0Z9HGzx24dMUloU3tkkPb2682klFMGX4BQ8SmYe-57iaACE4k2-6zdCKOvZNMyiWfCEvuxUsjmrS-u8nfftxKnp32SFJ0Ad0uYlx4xQ6VtaTb1zPLxSF2u5xh7FZUfprAR4Pc9JfHKuG76ANBSK8iEzE780cdbBrswl0zPAgxPytaFipRf9k0glXaF4rw6yrHpSi6XNPXmIqelnKn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVLnzf07SogiOgWCz9AyMMrQExC70gzyVgTEUDtdnYL9X_a3bBm03CAWtKv2mf8HuvjpG1hkBO3gCVeWJXVk-wuMBZbRu9PQIuP-mELHBe0U-2BYsHiDZqaZLiO-e927jv0hHn0Z9HGzx24dMUloU3tkkPb2682klFMGX4BQ8SmYe-57iaACE4k2-6zdCKOvZNMyiWfCEvuxUsjmrS-u8nfftxKnp32SFJ0Ad0uYlx4xQ6VtaTb1zPLxSF2u5xh7FZUfprAR4Pc9JfHKuG76ANBSK8iEzE780cdbBrswl0zPAgxPytaFipRf9k0glXaF4rw6yrHpSi6XNPXmIqelnKn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیشنهادات مارک لوین، مجری مشهور فاکس نیوز به ترامپ برای حمله به ایران:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/139525" target="_blank">📅 02:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EavyIe6vyaZQPzAbU2M5A7t3r0HSJGrOfPWd_1XlnnaRfnkCMM-w5BQJ33JHwONad-PSKKwdt6wkyVKb_qPMFo0hPt6rVrOOPJqX-gubKhJSz71E_kOnsjx2NdK7g0QzhjQILlWspYxpDbaDRh_MS9oGq2kkQ3xPEBewYwcJS3W0BMLdy7hvu9Eh7hl0vAOZWRJj4sCuJAEQNBrLFennrQtuFPM6pUzU5Re5Fg5itUidI5MLiTxIyK0KKRvHCTwvIoD6RN_sfRzNaz1YCuBc1FNq6eeMv2gHDwE7afLmuDG_kkTjg9KPGd27uMCIaSMwVqspn4chJ5JzgxxBCbhSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر بشکه نفت برنت 83$
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/139524" target="_blank">📅 02:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خبرنگار: آیا حمله برنامه‌ریزی‌شده شما به ایران، شامل اهداف انرژی می‌شد؟
🔴
ترامپ: نمی‌توانم این را بگویم؛ اما قرار بود حمله‌ای عظیم باشد، بزرگترین!
🔴
درنهایت خواهیم دید چه میشود؛ خواهیم دید آیا به یک توافق با ایران می‌رسیم یا نه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/139523" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139522">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caced3ead1.mp4?token=sPulSGr8nBN0AmBYAen6OvQNcjZWU07Fc1mx19G8FHIx-f0otoKqLzfpZF30UesITsRqUc03m1GKdupq15xRLt8FkfgsQdpUoH4ESgTcwFfVsJeD8hWZftLuNdjOGfLHYdobdly52ChASOnjPkFoXMQ9x2qtRQ7aSzsqzNQc004m_i0XrUxZ1wOZbqNZ_KypU_Mt4vaLvlcko3GtGG86kRWCDrjKXIFsK7WBkXLBr1WrZh4v1xHq9NqOVMxzkCNyZQOIKipaYDp_2rhxw7W26_7WD4-WEX67VDfvxh2dXxQG-HnYDqsFE64gJTklExmlxzFWAfAoGNJpdIw4DZz6kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caced3ead1.mp4?token=sPulSGr8nBN0AmBYAen6OvQNcjZWU07Fc1mx19G8FHIx-f0otoKqLzfpZF30UesITsRqUc03m1GKdupq15xRLt8FkfgsQdpUoH4ESgTcwFfVsJeD8hWZftLuNdjOGfLHYdobdly52ChASOnjPkFoXMQ9x2qtRQ7aSzsqzNQc004m_i0XrUxZ1wOZbqNZ_KypU_Mt4vaLvlcko3GtGG86kRWCDrjKXIFsK7WBkXLBr1WrZh4v1xHq9NqOVMxzkCNyZQOIKipaYDp_2rhxw7W26_7WD4-WEX67VDfvxh2dXxQG-HnYDqsFE64gJTklExmlxzFWAfAoGNJpdIw4DZz6kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا حمله برنامه‌ریزی‌شده شما به ایران، شامل اهداف انرژی می‌شد؟
🔴
ترامپ: نمی‌توانم این را بگویم؛ اما قرار بود حمله‌ای عظیم باشد، بزرگترین!
🔴
درنهایت خواهیم دید چه میشود؛ خواهیم دید آیا به یک توافق با ایران می‌رسیم یا نه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/139522" target="_blank">📅 02:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139521">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
/هم اکنون پرواز سوخت رسان‌های آمریکایی در خلیج فارس  @TitrDaily</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/139521" target="_blank">📅 02:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139520">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64bcf36d7b.mp4?token=XL2a06ky2-yC2ba3avPJCBDXQJGiea-W9awSgw1quxd2dwh076KnaxYaRt5CyjBiaeHuyP8QJYTaAaPlHE5wk5stjQE1q-ZhMQkkvFuIxVfmK3VkW_ZM0LpHCopChb_-ZjnMKNzIgeMxBdPxjiM0g-apyWk9qNP2oVTNtCzOQAs5x-hkt1RwNAsm8XWvmKThctRJh3aoNxdfU8PhX1SWh49FcSgCVlfVCywzSNd1d1q9zuEWqDv6C9PM4Zkj2hjw-EBFP5wL5lbawUpdIn0-01XGMdHYjDgj3GBhXtwelQves-1yovGLNiZbeyYHcvq3v7Wj_8My2vGWgJM0a2XYQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64bcf36d7b.mp4?token=XL2a06ky2-yC2ba3avPJCBDXQJGiea-W9awSgw1quxd2dwh076KnaxYaRt5CyjBiaeHuyP8QJYTaAaPlHE5wk5stjQE1q-ZhMQkkvFuIxVfmK3VkW_ZM0LpHCopChb_-ZjnMKNzIgeMxBdPxjiM0g-apyWk9qNP2oVTNtCzOQAs5x-hkt1RwNAsm8XWvmKThctRJh3aoNxdfU8PhX1SWh49FcSgCVlfVCywzSNd1d1q9zuEWqDv6C9PM4Zkj2hjw-EBFP5wL5lbawUpdIn0-01XGMdHYjDgj3GBhXtwelQves-1yovGLNiZbeyYHcvq3v7Wj_8My2vGWgJM0a2XYQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: "شما با کدام رسانه همکاری می‌کنید؟"
🔴
خبرنگار: "من از شبکه ABC هستم."
🔴
ترامپ: "بی‌بی‌سی؟"
🔴
خبرنگار: "ABC."
🔴
ترامپ: "آه، ABC. این بدتر است. در واقع، من بی‌بی‌سی را بیشتر از ABC دوست دارم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/139520" target="_blank">📅 02:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139519">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4dsdmDgMpN5_O-skvxkDqoWoWxux1yzq3nf3Qatnx9TlhRNldz41pmAmNBm19qDtXfGKiYJ7UvW01nHq64KFJ9GutTEXal8j6fWapBBlZp363ngF4TKOVM-LS16-6Z-XAStBaSK1WprPiXmrnIouoDOMTQE5FKMr11hd4u53JrwNoHfPaz3p56rxPENxBznOJzy8Vnr1gDM2auAYWRTXfj2hsjsanYCzsbitArO3JgsjwAQJpV1sL2jJgY8NV5zMhtmRgXwzBuZlE9UbOsT9_KRlkRn_lG45V-Ru5Hu3RqdSac-18GaHvlDb3AT6uYrs-5WJWGgg63Yf7pEUQqqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا:
موشک به کشتی اصابت نکرده و خدمه و کشتی سالم هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139519" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139518">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گزارش‌ها از اصابت موشک به یک نفتکش در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/139518" target="_blank">📅 01:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139517">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3502c8eb4.mp4?token=K_O-tGf2scaOSJI8hiqUlsg8rAA3DpjLqjO6m4PEYJyqfg2ime1esiCpFM0cvhPF85Oxf60ASKyJXfTD4Bn-enB3yZmwBLlOLibijzBcJk8h1xVS3oHGXhlxrIT5h3CGb3cd0rShuN48kWS2yquOYntfMicnysVjYi5L-PL_m93MGOCltvbyFN5yQiIa6DMa5vckgQzONsjZhOZJ1VXhhfSdOTdC5KM6cylWdLAorqadSyASg345tZdJUGiNnrI_vw8priiMlOJOEPijWAqiTLVftP9e0Flg6Jl8O4W6s9KgJmQ68af22L-LAhOobRk-X_gT6ylVTJP6LOQwe5_Dew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3502c8eb4.mp4?token=K_O-tGf2scaOSJI8hiqUlsg8rAA3DpjLqjO6m4PEYJyqfg2ime1esiCpFM0cvhPF85Oxf60ASKyJXfTD4Bn-enB3yZmwBLlOLibijzBcJk8h1xVS3oHGXhlxrIT5h3CGb3cd0rShuN48kWS2yquOYntfMicnysVjYi5L-PL_m93MGOCltvbyFN5yQiIa6DMa5vckgQzONsjZhOZJ1VXhhfSdOTdC5KM6cylWdLAorqadSyASg345tZdJUGiNnrI_vw8priiMlOJOEPijWAqiTLVftP9e0Flg6Jl8O4W6s9KgJmQ68af22L-LAhOobRk-X_gT6ylVTJP6LOQwe5_Dew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
من ترجیح می‌دهم توافق کنم. به دنبال کشتن مردم نیستم.
مردم می‌میرند. بسیاری از مردم می‌میرند. ما نمی‌خواهیم این اتفاق بیفتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/139517" target="_blank">📅 01:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139516">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ad698cc5d.mp4?token=eSFCvODsHtxs_qv6iXDulm7dByzr4X6Ghlv31V_0LzG_MiNKe37vYzCYGtSVLzbohu1NwhFRoMQXXDqNxBu26qD1-cliXmjpegJ8zicwYSt-FEGf5OBWGi0s2v-RKcSujPFkOeaO5hxzHL9k4D6na8Xgp66h9eXna6cUWfykwmvOGHfmQM5FNmwK_hEy3micpMmkWT2ev9uatwED0gO0UzECLCpIoH1ltKhlAx4FrGRpqMgjnKbHxm6Qw5Ut1PzmyMsEb8F3x3LvEcUXuE0Iceg2_NuI9SoP45L4YazpaGaylHW06sBd3T0t0maXnjhljIJm8WLYgS7l2eqmH0da3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ad698cc5d.mp4?token=eSFCvODsHtxs_qv6iXDulm7dByzr4X6Ghlv31V_0LzG_MiNKe37vYzCYGtSVLzbohu1NwhFRoMQXXDqNxBu26qD1-cliXmjpegJ8zicwYSt-FEGf5OBWGi0s2v-RKcSujPFkOeaO5hxzHL9k4D6na8Xgp66h9eXna6cUWfykwmvOGHfmQM5FNmwK_hEy3micpMmkWT2ev9uatwED0gO0UzECLCpIoH1ltKhlAx4FrGRpqMgjnKbHxm6Qw5Ut1PzmyMsEb8F3x3LvEcUXuE0Iceg2_NuI9SoP45L4YazpaGaylHW06sBd3T0t0maXnjhljIJm8WLYgS7l2eqmH0da3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
شما نمی‌دانید که این حملات به کجا منجر می‌شوند. منظورم این است که آیا همسایگان ایران با هجوم مردم به کشورهایشان غرق خواهند شد؟
یک فاجعه. اتفاقات بد زیادی می‌تواند بیفتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/139516" target="_blank">📅 01:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139515">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=kiAbsZrbEZbag6EnQo8y4WFy-8kBPOQbxVmNLDZ4VIaMh7TXtaHfJFxk9-woP5igsqptVH18TcbIVg85lfP3L7CQj9oIA-Gqjr_pAg97TR87ST8KJMIkKaVPKw7RbV8QYMn19gEMnYJ3W0Ue89RVhpwJsR_5FbYAg3Tdq82deVu755CD_np6XdTQUZl8mUUlGJMc08ZnthelqwVuiQpX_TGEskxmLI6QDsDaM1NZmKZ7BHfEaBBMku-ksI5pB_OK5xeaaLeFhtlkr1y5DgR9yR5uYB9xdxbT7RY5m4gGip9ABM3VOL7PRxQ2zYS5QxJZI6rs-KzALe78AcitMA9P7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=kiAbsZrbEZbag6EnQo8y4WFy-8kBPOQbxVmNLDZ4VIaMh7TXtaHfJFxk9-woP5igsqptVH18TcbIVg85lfP3L7CQj9oIA-Gqjr_pAg97TR87ST8KJMIkKaVPKw7RbV8QYMn19gEMnYJ3W0Ue89RVhpwJsR_5FbYAg3Tdq82deVu755CD_np6XdTQUZl8mUUlGJMc08ZnthelqwVuiQpX_TGEskxmLI6QDsDaM1NZmKZ7BHfEaBBMku-ksI5pB_OK5xeaaLeFhtlkr1y5DgR9yR5uYB9xdxbT7RY5m4gGip9ABM3VOL7PRxQ2zYS5QxJZI6rs-KzALe78AcitMA9P7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
🔴
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/139515" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c617d9274c.mp4?token=XJRW0J5HTN00-O1HtXFevgeVrJZAoV4zydpQ3IkqL4chH7dwRlhZrqb4OOaRnKsbcP94chgYNvo4rgzsCLPFYcATsbfka8jLkw3kWingz6J6Zl_mDRsXBE4wM2ftImFTpcxg-xjcEf-dKeDb-pFHCmFGuNLikUWUhByNGEXE58b7UOlDPwA1KE8VSrp_7_LSHv8bJdartzbytbmma0jhHu-QLakdNy3_7fZhgJUe1P10F3dZ1YYY1MqtVm815NCOZEd9__imW1-Ssk-1mt7EdUG-MsuclyOaKzemBP2kfBTdD2jkWJpDQDXWmVKRFQ1dULUSWQuIEudBD-WL62eS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c617d9274c.mp4?token=XJRW0J5HTN00-O1HtXFevgeVrJZAoV4zydpQ3IkqL4chH7dwRlhZrqb4OOaRnKsbcP94chgYNvo4rgzsCLPFYcATsbfka8jLkw3kWingz6J6Zl_mDRsXBE4wM2ftImFTpcxg-xjcEf-dKeDb-pFHCmFGuNLikUWUhByNGEXE58b7UOlDPwA1KE8VSrp_7_LSHv8bJdartzbytbmma0jhHu-QLakdNy3_7fZhgJUe1P10F3dZ1YYY1MqtVm815NCOZEd9__imW1-Ssk-1mt7EdUG-MsuclyOaKzemBP2kfBTdD2jkWJpDQDXWmVKRFQ1dULUSWQuIEudBD-WL62eS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:من 75 میلیارد دلار برای کشور درآمد داشتم. من برای خودم درست نکردم من آن را برای کشور ساختم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139514" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139513">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
👈
خبرنگار: آیا برای رسیدن به توافق با ایران، ضرب‌الاجلی تعیین کرده‌اید؟
🔴
ترامپ: خواهیم دید. من قصد ندارم مخصوصا به غیرنظامیان آسیب برسانم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/139513" target="_blank">📅 01:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ:
از ولیعهد عربستان سعودی پرسیدم: «ترجیح میدهید ما چه کار کنیم؟»
🔴
او گفت: «ما توافق را به حمله ترجیح میدهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/139512" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139511">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95889103bc.mp4?token=rPv8ZpmN2FqENctncQM1Mz0Zgxed96peuWX-l1Wv5fUsA51X0ELvWaoVPZ1LokaqZy_t8qlJ5h_aKTktGYw8OhxIFGdVOxm79-1zHKA-5Msghz0UHHIbdGXBx3E6vfpg01swQduN4zrTLPVuFnGPvTs6NQpSODaf6qlFEbgFWDcRDkdXza6tJSt07bWa-D4TI3EhRr1v6Rjb7_XFSF1L9_8U4vGKA2GseZtXT47Uo4PbDIYlm8qogG7HjAaltXuT1sU_D4LMpgq4anPXY8TK1UMi5QLEzsLmcT73D_JaZm6da2rQCiII61fonOQ1azx8i8kAjg5J08v8XRBkKmZvDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95889103bc.mp4?token=rPv8ZpmN2FqENctncQM1Mz0Zgxed96peuWX-l1Wv5fUsA51X0ELvWaoVPZ1LokaqZy_t8qlJ5h_aKTktGYw8OhxIFGdVOxm79-1zHKA-5Msghz0UHHIbdGXBx3E6vfpg01swQduN4zrTLPVuFnGPvTs6NQpSODaf6qlFEbgFWDcRDkdXza6tJSt07bWa-D4TI3EhRr1v6Rjb7_XFSF1L9_8U4vGKA2GseZtXT47Uo4PbDIYlm8qogG7HjAaltXuT1sU_D4LMpgq4anPXY8TK1UMi5QLEzsLmcT73D_JaZm6da2rQCiII61fonOQ1azx8i8kAjg5J08v8XRBkKmZvDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ژاپن:ژاپن بسیار خوب با ما رفتار کرده است، به جز البته، پرل هاربر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/139511" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139510">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75f718148.mp4?token=DfO9Vm0mwagbAPNLY46GQwtzhKPEaow8Cl0-ctFZPRlmlm5kkV852Wbg3Vq2OfPBhDE9Yx5L_vto5WqRufEXTvPvJQdHhSm1ujYp81HzNW_pntNQZDkaLzxbK9ipHqicqHav3esNOQ3Zt1At8EZNaEwN44X5UlXRc5yFUfuyVI56Ib625ADMbEUXlPBvepGnQZjQ1JAlDzyODlpI8Y4_6_AmVTmnEOpCqdviUa_HI7eqzMkOQLLYIrCT15Q2Rg8ltGwaNe91pOeML528-R_BL6B9Ie-rUL94JRXUHAGbGssoWkxxu84k632Fi2wJDTVQA4BC-TzDhvzepM771ZLthA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75f718148.mp4?token=DfO9Vm0mwagbAPNLY46GQwtzhKPEaow8Cl0-ctFZPRlmlm5kkV852Wbg3Vq2OfPBhDE9Yx5L_vto5WqRufEXTvPvJQdHhSm1ujYp81HzNW_pntNQZDkaLzxbK9ipHqicqHav3esNOQ3Zt1At8EZNaEwN44X5UlXRc5yFUfuyVI56Ib625ADMbEUXlPBvepGnQZjQ1JAlDzyODlpI8Y4_6_AmVTmnEOpCqdviUa_HI7eqzMkOQLLYIrCT15Q2Rg8ltGwaNe91pOeML528-R_BL6B9Ie-rUL94JRXUHAGbGssoWkxxu84k632Fi2wJDTVQA4BC-TzDhvzepM771ZLthA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
گزارشگر: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای نظامی ایالات متحده از کویت و بحرین هستید.
🔴
ترامپ: من نمی‌خواهم در این مورد اظهار نظری داشته باشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/139510" target="_blank">📅 01:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c1219395.mp4?token=YYlsAZYyKjvpOrrdv0G08qjIouWMeVeQoE8QkfmT_qRSL0Cop_fITSJaoPDwU3BCgcVtMNTOqXynODHEQmCUGsVB-g6pKl2YONw4fcUBLCS0BzFBaE5mMBcQBCc7SszGgCbkmx2C-L92esKb7XjbvdiziK1xWX551WYxUeC5x_m8p0APm-_SMUsmW-7AaUYJHfuJFHN2JXSl7iceQOC7UlzmPlhYwp6Xepgqk2yi3OW7xUQKm6egDft54YASpOnZW_jf4eIuKhqosS_GEYysa1NT3fzcLwA4tWmunDyxFKLUzq3v3ErYY2NRYevVP3alMeowiIhblfHdHCljBgpc8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c1219395.mp4?token=YYlsAZYyKjvpOrrdv0G08qjIouWMeVeQoE8QkfmT_qRSL0Cop_fITSJaoPDwU3BCgcVtMNTOqXynODHEQmCUGsVB-g6pKl2YONw4fcUBLCS0BzFBaE5mMBcQBCc7SszGgCbkmx2C-L92esKb7XjbvdiziK1xWX551WYxUeC5x_m8p0APm-_SMUsmW-7AaUYJHfuJFHN2JXSl7iceQOC7UlzmPlhYwp6Xepgqk2yi3OW7xUQKm6egDft54YASpOnZW_jf4eIuKhqosS_GEYysa1NT3fzcLwA4tWmunDyxFKLUzq3v3ErYY2NRYevVP3alMeowiIhblfHdHCljBgpc8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
قرار بود یک حمله عظیم باشد.
از ما خواستند که این کار را نکنیم. گفتند: «لطفاً این کار را نکنید.»
همسایگان نیز همین را گفتند. ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به یک توافق برسیم یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/139509" target="_blank">📅 01:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
👈
ترامپ درباره احتمال حمله به ایران:
گروه‌ای از افراد دوست دارند دست به حمله بزنم  یعنی خیلی ساده دست به بمباران بزنم و در مقابل، گروه دیگری هم هستند که اصلاً نمی‌خواهند چنین کاری انجام دهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/139508" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ:
از من خواسته شد که توسط عربستان سعودی، امارات متحده عربی، قطر و همچنین خود ایران، از انجام حملات خودداری کنم. این یک حمله بسیار بزرگ بود. وقتی متحدان درخواست کردند که این عملیات متوقف شود، باید بگوییم: "خب، بیایید ببینیم." متحدان فکر می‌کنند که یک توافق وجود دارد. یک توافق در مورد هرمز وجود دارد و این توافق در مورد مسائل هسته‌ای نیز خواهد بود. ما با آنها در حال گفتگو هستیم. این گفتگوها فردا بعد از ظهر آغاز خواهد شد. این کار می‌تواند جان‌های زیادی را نجات دهد. از ولیعهد عربستان پرسیدم ترجیح میدی چیکار کنیم؟ اون گفت بجای جنگ، به توافق
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/139507" target="_blank">📅 01:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: ما در حال مذاکره با ایران هستیم. این مذاکرات از فردا بعدازظهر آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139506" target="_blank">📅 01:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ:توافقی در مورد تنگه هرمز وجود خواهد داشت و توافقی در مورد خلع سلاح هسته‌ای نیز حاصل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139505" target="_blank">📅 01:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139503">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87d70cccd.mp4?token=LQT8AFjSrQ3LgComtoqntmXg_v9_jOc5jx78oljRpWn2clXGCHg161KG6XaBoKD5JxDn--7qSRyB07rWO32weFprezpsZqbdwaZdXk8z5NSovhAHipGVUrw6IA16zeAE8F5HVrSPESuN8V_Q_W-aNdSExCNT1YewapKQ-EJujnyxOWBe_-IebaMRi9Aqnuy0Ya6ehX9oPjtUERLO4RtsyY204IjHUVTwRQ-eJ_Yw0wslrwP6o7O46mfSinVZtz_vzKjaNWixolXBUqDSbr-0qp4FOjz-ufTXN5Y6wKTkjo4SIgSnpzVZjqvEjFYhKLhIBE73jb6eWGRUGh2vrwJw2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87d70cccd.mp4?token=LQT8AFjSrQ3LgComtoqntmXg_v9_jOc5jx78oljRpWn2clXGCHg161KG6XaBoKD5JxDn--7qSRyB07rWO32weFprezpsZqbdwaZdXk8z5NSovhAHipGVUrw6IA16zeAE8F5HVrSPESuN8V_Q_W-aNdSExCNT1YewapKQ-EJujnyxOWBe_-IebaMRi9Aqnuy0Ya6ehX9oPjtUERLO4RtsyY204IjHUVTwRQ-eJ_Yw0wslrwP6o7O46mfSinVZtz_vzKjaNWixolXBUqDSbr-0qp4FOjz-ufTXN5Y6wKTkjo4SIgSnpzVZjqvEjFYhKLhIBE73jb6eWGRUGh2vrwJw2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل به المنصوریه، جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/139503" target="_blank">📅 01:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139502">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ، از نیوجرسی به سمت کاخ سفید رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/139502" target="_blank">📅 00:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139501">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ظاهراً مسیرهای اینترنت بین‌الملل زیرساخت دوباره تغییر کرده و به‌جای عبور از آذربایجان و Delta Telecom، حالا در برخی مسیرها نام PCCW Global و رنج IPهای دیگر دیده می‌شود.
🔴
متأسفانه این تغییر هم بهبود خاصی نداشته؛ مثلاً پینگ کلودفلر روی 5G ایرانسل که قبلاً حدود ۸۰ تا ۹۰ میلی‌ثانیه بود، حالا به ۱۴۰ تا ۱۶۰ رسیده است. به نظر می‌رسد NAT شدن اینترنت هم کم‌کم به یک رویه عادی تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/139501" target="_blank">📅 00:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139500">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رکنا: آمار ثبت‌احوال نشون میده تعداد تولدها در ایران طی سال 1404 با 892,000 متولد، به کمترین سطح در 66 سال گذشته رسیده.
🔴
گرانی، تورم، هزینه بالای مسکن و کاهش تمایل جوانان به فرزندآوری از مهم‌ترین دلایل اونه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/139500" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9bc38bda3.mp4?token=LWRDGlvfrceHoGKX9FLMGd4C3w28jcPSAkXWUCFrtX1ywnbmlmAhUm19qlO4HwYNaPXBUi3XwvydpIXRWF8lZeYOkoV1LF8kM_dEyflf04Va5F_qB8pjhGvzHxAG_0a2ZTeqJK7Kmdt8jpMY4UjLK_RVmdp-pU7Q2M5KJRuqKBrFA1urZrULDh19BIN0yUbTyujlKjFkwKQtBligG224kC1KovGTT2YnR9CJYFevxpN7pkxKvWyhiymzD2_9yH-MEJaJuiVl_I0_Kfcu4-IUdM1vxfyFhyXllJTSLbridKxmIReTQRPp5UkJJcjYo_PrdVhu4pwl3nonmxgC2U2bWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9bc38bda3.mp4?token=LWRDGlvfrceHoGKX9FLMGd4C3w28jcPSAkXWUCFrtX1ywnbmlmAhUm19qlO4HwYNaPXBUi3XwvydpIXRWF8lZeYOkoV1LF8kM_dEyflf04Va5F_qB8pjhGvzHxAG_0a2ZTeqJK7Kmdt8jpMY4UjLK_RVmdp-pU7Q2M5KJRuqKBrFA1urZrULDh19BIN0yUbTyujlKjFkwKQtBligG224kC1KovGTT2YnR9CJYFevxpN7pkxKvWyhiymzD2_9yH-MEJaJuiVl_I0_Kfcu4-IUdM1vxfyFhyXllJTSLbridKxmIReTQRPp5UkJJcjYo_PrdVhu4pwl3nonmxgC2U2bWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاتز: همه چیز در جنوب لبنان نابود شده است!
🔴
وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:
ما ۲۴ روستای لبنانی را ویران کردیم. ما هر خانه را تخریب کردیم.
🔴
آنها برنخواهند گشت. آیا می‌دانید چرا؟ چون جایی برای بازگشت ندارند. همه چیز نابود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139499" target="_blank">📅 00:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
طبق گزارشات، اینترنت ایران امشب خیلی ضعیف بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/139498" target="_blank">📅 00:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
توی تهران یه دختر و پسر جوون رو دستگیر کردن!  حالا چرا؟ هر روز میرفتن توی پارک و دختره کیک، سس و... میمالیده روی پاش و پسره لیس میزده و میخورده. بعدش فیلمشو ضبط میکردن و به فوت فتیش‌ها میفروختن. آدمای توی پارکم لوشون دادن و دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/139497" target="_blank">📅 00:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbVnEZuptAkQhDHJnKB275Vh3iDrG-AN9CorhyY9oAHuNK5qjnioBggxejuIAca1mdquJHCrJcZ1q_NqQi90VavbqofwtMBg2Nl2bu3jgsox_eXuZBAf6YuYrj5hPnPdFjwU-2LjpOaBq_WjVmMDseF_p0hD87TJpw4TMnXg4qilsChjPq2uiHeC7ZQWuw04a8Q19Of7XASsB8EWvE-V5EbrpaPCQ97_uai3Iedc67uzB5GVfeZ38wFVU4E3huF_ls_HbKFBawzjwyrPNv8MLzQzqq_lUaUHkTGeQkG4DPcOuSqnYTys8u5CiVFKyNltb7q0MYeJcYSq68PTrw7Evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی تهران یه دختر و پسر جوون رو دستگیر کردن!
حالا چرا؟ هر روز میرفتن توی پارک و دختره کیک، سس و... میمالیده روی پاش و پسره لیس میزده و میخورده.
بعدش فیلمشو ضبط میکردن و به فوت فتیش‌ها میفروختن. آدمای توی پارکم لوشون دادن و دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/139496" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi2XtKeo5Zk19XL-ICZROwHoAL2Q1I8-vK89-15QAIMYs6z1ufRKL_coAeR1dkabGp3MlCRwkutoGw09BlgoeJ_QnWeAxK5O5AqaJqgRY99njV-yHhE8MBBR44nmJczJyxZ16lTmscMiCB80oHEwANGdCMQU8RLETzCVquU0jjJPZ_UTEDlBU61gmcnjDMPQRq0SvuC3kC661NUJYZ7uHYaom5NbSA4lm2vLLJujUyNv_BAQmBZyD6WKDtc3IW9tHf9P4_7fabzS239MqSgMMZm7LMu10rqgifgdTsxiZ3U4Ti193iqaolOwaFQtGJ9zdT1HMfOHiV0X4ctY9ARvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید: به ترامپ اعتماد کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/139495" target="_blank">📅 00:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HxY-xMmLqvoRCQaC231b-KT8lS9aBqNSvUypR64aWw6Bp-nR35le7psu6tDA83ql_XTvaxPj_BCeNG7mHH82vVrl2_YKolBQKsNo1OVBafoESLa2cM4Kcnm-SuriMUyye-ao-eVOmnDDZ-fk0m6rfxFpmjtZ6nF2-K1T-m6zKnRYFFfhjx9AEMupbcc-eiZrf40txma74yHsKlN5Z68_HcyEWQfhU4hqM80OwWF3ooZIlhpOl7_qryrY92Uyh8SgW89ndA_nBrilvurPaqQbw6SjBx3vA6Wvvk5kTT99AG7b0srruyfVaaX5igFhUTuSFupKJPsCTsPl50c9O5WWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aAdUe0JDQNgV3XmD6UCwybFq581vU-qdGoM6VX0gLM7cQxd0Get87I6H2ptCcegSSM8rnYds0chT0djbSTaEC1gJVTxMnRDw1299_FeO6Sphu_A0X8F6fpnSPG1hQNveHx67qR2st3QnT5zyhs7xrghNwxnTtdBVvkE5vb4PD0eb5JGFXTdJkgFvYTEcMfkPFrw_82KPcOzMgJob7t9p9Sdajq4nY2F5cadD8dATqtmg75dYdXpw4Pibk37abWKsa_f6qatNmnZOvw_AKC3iGKUjzBboHfaTpxPUS501vd-QEWCMamNf1xHvn0CIUwkW2tH8WLen_OjWlLiOTpW7ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ایسنا: یک هفته پس از حمله اوکراین به یک کشتی ایران، پیکر ملوان کشته شده در این حادثه به همراه هشت عضو بازمانده از خدمه و مالک کشتی، به ایران بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139493" target="_blank">📅 00:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
👈
تصویر تازه منتشر شده از لحظه انفجار پلیس امنیت فردوسی تهران در روزهای اول جنگ ۴۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/139492" target="_blank">📅 00:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
👈
تصویر تازه منتشر شده از لحظه انفجار پلیس امنیت فردوسی تهران در روزهای اول جنگ ۴۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/139491" target="_blank">📅 00:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_IIR3ueLzTP5IceQXd-wpeZjRQts_E4aTOhpSWWwZml5qLFzeqidxR4Oxty0H9bzcyNqOV9cJ2BedfIcT3QMHEl3TCnryl5fbrPPOBTPXCmYkcG_-Q8n_lX7e64vETgO1TGg3Jironi2voput_k1zpT3GAgudWRb8Ku36Ymt7oOKD-AONSzu8ECjNwedx8a7Botvu7PckTKEm9iIPcQghWOpmLSvlEvNK3mmRcPi6mhhB_wLMaY9_z-S-Y_JpINHaeAPMqNMXEn_KiYoG9Xs83epB5zRCTQ_He5zPCir2wyQlttaujGIoUn97fecGVOd0_XI6swnzWGgePaopAGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2Xp-H3ZuvjiPGKjG6ZGYRRTYZx-wBNqUOxDgm3FjxU2TqtbuiYiIQ-sbDBI8NXFQn2_B5yznfyJ2iq5frqOlocIYOPFzBRWKry_1mJ3HzFAUxpDrtaFGQ29W1YZeALP-J6j2ZBxsjGDuNJ1P__twaDGO0Su0gGcMG1JlAyZZGCkjrR7mRIuYJZILgRJkRE-jib5qAJHiY70tm3elJBcqQbnISPQJwCNfqcjEp3rj7RZAmr4800bVshsSdimSVTlRo4adqLHE2eTBhMUVe_tj3Yqrb5bSeXnwxvf-KH29RIyozgPRT3JgYEetyO3JZtB88dPiGBu_tjUTd0u_0lMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZE5oABdNbCmyQrB-s_JDQXDliD8pUH78AvqdIwYWlMGRBaKmooF68_FBk43FpEZINHO3Z8_NyTdWa6JM9KL30z-e_lvEbyOc2qaZe0YW_liwdCCIzxtkq3CWcM52iyulFmG-TDbs88IFVqBo8TnlVYHqisi26Wi7vzm50T5_wD4jvTjMYJZcXMRdKOhD9wkTfWWKmC_XsA_DrYDJOhYzg99viRifhLV3ORAZjBtuHoCUKPYOaGrwyhkHSHh0Pw_bONYS_H0-nb13HnEkqrF5jm-jW2UM5u0Moy8IIH0Y2kU3KtlKeer9XQK2eMZfG-Up9YxL4SFgkUuftCdKZzvpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c16e67daf.mp4?token=F8YPyUGCpt8oefg_6GbKYPkiatN0LLnKCQqUquR4TFEG64ivq7mu6nzV9tVIu-RS3_HfQk1Ffn_sA_aLv4qYgCH9DfEXmKJu7FIU5RicbiuWjVEE55FT8SHr3fxptJ1GfKCTuJSzrcMNaoPgn3s_xjU0eU806ko7aO-0gHGQAKZ2iX4v2fFpDRLjWL1f8_YZkCM6SV8-1k_3-ipjvj3KKyOTb5rzD17tTlB9H2nPYZHkatDUo82ULBIXi51lTajfXnTE_HCX3VUv2_hf030Io4deKBRopfCasbHW5QaAxFD8JuRmUybKI_plN1q6BHDkJJy2zzoKOFv_NDdprbhosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c16e67daf.mp4?token=F8YPyUGCpt8oefg_6GbKYPkiatN0LLnKCQqUquR4TFEG64ivq7mu6nzV9tVIu-RS3_HfQk1Ffn_sA_aLv4qYgCH9DfEXmKJu7FIU5RicbiuWjVEE55FT8SHr3fxptJ1GfKCTuJSzrcMNaoPgn3s_xjU0eU806ko7aO-0gHGQAKZ2iX4v2fFpDRLjWL1f8_YZkCM6SV8-1k_3-ipjvj3KKyOTb5rzD17tTlB9H2nPYZHkatDUo82ULBIXi51lTajfXnTE_HCX3VUv2_hf030Io4deKBRopfCasbHW5QaAxFD8JuRmUybKI_plN1q6BHDkJJy2zzoKOFv_NDdprbhosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در منطقه المانصوری و مجدل زون در جنوب لبنان عملیات تخریب گسترده‌ای را انجام می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/139487" target="_blank">📅 00:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMRa87WZ1QfEr5zxrKcqOxtM3ZPNFZnJF0ig2gzEDmp30c35GFxD-Jp3T9yDBelkdCBR9XV1c4sC6OXImTOl_R2YDKNPgRsdU4yiZAQX-bvtBmu4oA5hjArFQOOO2OVLoEIk_R-DsUUGVldrqgFYr4tlRljM5hVyT-H2w2CpxOJJy59Rntl1OSXT284NXQysbyNZuZ2a1lUUXr82dQCg357qECSb6ZM9yI58ARvbsnCI2Jxz1Ny2tgmOG-Ihh85Up0GYmgwEhCpytMNRy-Ud0ZZaqAwfKxnquFhSam-p6USc9sx7G5NrJT9eZe1ubFvC8xU5JMHrVPKDi4gc3-ftug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی زاده:
آخر سر آمریکا اعلام شکست میکنه و میزاره میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/139486" target="_blank">📅 00:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB4sKNO0gyq7-vo1pB-1xxXZ7dOIxk5qMATyuOK2QuzSeJDZlOixWNpeO1xrzivCHig4KffdedtvYtyrTucgBEGnQFNz8UAwAWqjl7xBU7KMHTi5OW4EB0su6NUE80deWiWF1QI5zchfVZV-0oojr3PHt5h0_v6OdJiomCoz_QmCVVwq7JLJryXTTLlNerQYTt_s34H88ghcBzwdUOK2R7jU_hkWvMcj2vlesCHVImdHPlLp0ked7gtFcEE-Jqr74b_6jfMUHQWSwmRCXG0Bx-s7UzrHkUcz6iRZah_4Wpeya-jEc9n0TRwQYbDE2he1aLGaHH64BB-zApzRUX_OVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: آخرین نبرد رو بازم‌ ما پیروز میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/139485" target="_blank">📅 00:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8549b9f30e.mp4?token=pxpasYUVIDNONkUH_4aTtdxAjbpq53ovI_FRsd2odbuNxc0xO_GmRHRxvXgYI_StP-txyZgFabiIJjzf9jKPjO9Y2I7fi1Uq8gfuX1n3lcQ3UvI792gHh0XOrbw9596K49x7YGRSB33u39CtbMxcqO1atGkVdQuo8kYOg3Sy3HOIIq__VA9hXtc6eF7u2EExS7VfAm8q-OtAZVumsLzKZOd3XkqCHMX2-kDsJSrjc7vgj2rDvUgx5OouiJaXf6BNFuUv7-z8Ajb-3VLXyKTKzVqeXvGhOOTqcBcacaOSg4EACzxf9pAkepszv5ty-JyxBVC5MaXU0rBQlRPXHIdfeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8549b9f30e.mp4?token=pxpasYUVIDNONkUH_4aTtdxAjbpq53ovI_FRsd2odbuNxc0xO_GmRHRxvXgYI_StP-txyZgFabiIJjzf9jKPjO9Y2I7fi1Uq8gfuX1n3lcQ3UvI792gHh0XOrbw9596K49x7YGRSB33u39CtbMxcqO1atGkVdQuo8kYOg3Sy3HOIIq__VA9hXtc6eF7u2EExS7VfAm8q-OtAZVumsLzKZOd3XkqCHMX2-kDsJSrjc7vgj2rDvUgx5OouiJaXf6BNFuUv7-z8Ajb-3VLXyKTKzVqeXvGhOOTqcBcacaOSg4EACzxf9pAkepszv5ty-JyxBVC5MaXU0rBQlRPXHIdfeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه اسم انواع رابطه ها رو بلد نیستید؛ این پست میتونه بهتون کمک کنه.
وان نایت؛ رابطه ای که فقط یک شبه.
اوپن ریلیشنشیپ؛ رابطه ای که هر دو نفر با رضایت هم بهم خیانت میکنن.
بنفیت؛ باهم دوستن و رابطه جـنسی هم دارن ولی تعهدی ندارن.
لانگ دیستانس؛ رابطه ای که دو نفر توی دو شهر یا کشور مختلفن.
سیچوئیشنشیپ؛ یعنی هم تو رابطن هم تو رابطه نیستن؛ یه روز هستن یه روز نیستن. خیلی وابستگی وجود نداره.
هلسی ریلیشنشیپ؛ رابطه عاطفی سالم که همه چی توش جدیه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/139484" target="_blank">📅 00:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfzgyYJqbLtmOyzf4AdZ3kPOiTcPnvuuZpRzs0f1bsa5HByzhO37Pa9JrTCJsionvjUxKrawRKk3hTj0SvQfTLKbPljR0fyzr_0vUkF231ZJ1ucGssGtA6J0Ndvy9Nb6xBGgkkqjKLRofANtUzCYqJou4YJKnImXZq9Fnyzd3X40DCRjLmsbx84_p4qF2F5AHzycKsnWwmJEBV6APfVbWX8KwKIHaz02dx1St9pFLVsijWu5NeQnoBqYgi7AuZs11p98Vyih5RaJmFaI2jWscgCto7Alq76F-hBxPZ2p5Jt98L20DiGRxmv2eGov-7VuVNJcsZKIga9T7TfQb_kO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رد پیشنهاد بی‌سابقه‌ 1.5 میلیارد یورویی به‌خاطر خانواده؛ وقتی مسی ثروت افسانه‌ای عربستان را ندید گرفت!
اظهارات تازه‌ و شگفت‌انگیز آنمار الحائلی، رئیس باشگاه الاتحاد عربستان، از یکی از بزرگ‌ترین پیشنهادات مالی تاریخ ورزش پرده برداشت؛ پیشنهادی که لیونل مسی بدون حتی یک لحظه تردید آن را رد کرد.
📌
رئیس باشگاه الاتحاد درباره روند مذاکره با فوق‌ستاره آرژانتینی گفت: ما پیشنهادی خفن و تاریخی به ارزش 1.5 میلیارد یورو به مسی ارائه دادیم، اما او این رقم باورنکردنی را رد کرد؛ چرا که خانواده‌اش ترجیح می‌دادند در میامی زندگی کنند. چیزی که ما را عمیقاً شگفت‌زده کرد این بود که او حتی یک ثانیه هم تردید نکرد. او می‌توانست تلاش کند خانواده‌اش را برای آمدن به عربستان قانع کند، اما بدون معطلی، آرامش و خواسته خانواده‌اش را به پول ترجیح داد. ما کاملاً به این تصمیم احترام می‌گذاریم، چرا که خانواده همیشه از هر مبلغ پولی در دنیا مهم‌تر است.
این تصمیم مسی نشان داد که خانواده برای او از هرچیزی مهم تر است
@AloSport</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/139483" target="_blank">📅 00:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb15c4e0e5.mp4?token=d2F1G2qscjvx8S_bmQkO0b2v0fe7imtNFf1u0b_JdHxrJAlBba_zmV7XMF_FuzbPzy5M-stgahsSYpdnN34KAmdpaFs_RRLxq2-DQve11zmhDAqagO6xwrRr5x3v2un3zvJ3M0kM8f_H5CujHlf1ZaovFkeu5qHdU9m_EadP4nZNYBWUTcn08uiJu7OoU-Ru4wFerZL44YstuTPpN-mwjeEKw2YVYpq9WKu0IkcUTUvVVI1WejBZedUrt9I2ZH8J1-6T5CIiiPXIFAwAw7IU_rhVX4aCxVR6rnoYmA5h-zb-O_5C4bDdnk32wlzlsRagbRtfotA71WqJy3HHmiklJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb15c4e0e5.mp4?token=d2F1G2qscjvx8S_bmQkO0b2v0fe7imtNFf1u0b_JdHxrJAlBba_zmV7XMF_FuzbPzy5M-stgahsSYpdnN34KAmdpaFs_RRLxq2-DQve11zmhDAqagO6xwrRr5x3v2un3zvJ3M0kM8f_H5CujHlf1ZaovFkeu5qHdU9m_EadP4nZNYBWUTcn08uiJu7OoU-Ru4wFerZL44YstuTPpN-mwjeEKw2YVYpq9WKu0IkcUTUvVVI1WejBZedUrt9I2ZH8J1-6T5CIiiPXIFAwAw7IU_rhVX4aCxVR6rnoYmA5h-zb-O_5C4bDdnk32wlzlsRagbRtfotA71WqJy3HHmiklJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیلا فرخی (همسرِ بیژن مرتضوی) مجری یه برنامه به نام TV10 شده و مجید واشقانی رو دعوت کرده؛
حالا بنظرتون چی جوری طرف رو معرفی کرده؟
🔴
"امروز میزبان یه هنرمند و تحلیل‌گر سیاسی هستیم که تقریبا تو همه جمع‌های خانوادگی، مردم دارن دربارش حرف میزنن!"
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139482" target="_blank">📅 00:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ecf46d77.mp4?token=kJ6d8E8J7zBY_oZIs7VepV1di-uMifSeXzSYju15hEwyIo-QJi68edAqKHCqH8m6SI5b3jzY1E3Ycn47H0QFfWx-u0uQCergzaSU03qNNOgjgNqiqORsvKnvY3pHL-4IlYfMudtdfvfBTroWXW-BTSuBkOiCc8CVOHmPggmiXAi-saSqWVp0UfnTJ_l61rMPe7gramVKbSicCbecsDxtS86yxc86W6Fw5lUphk5_PkV4aIQZfPBrj6ZkwXQLjxeGEeMorkhzEDvzTENv-WCLID4akcrKqpCN8uwiYVzOPi8Rwv8UzOr0Ryp5rQ9EbnTgLnoaK5CPidoOWjGsNUquVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ecf46d77.mp4?token=kJ6d8E8J7zBY_oZIs7VepV1di-uMifSeXzSYju15hEwyIo-QJi68edAqKHCqH8m6SI5b3jzY1E3Ycn47H0QFfWx-u0uQCergzaSU03qNNOgjgNqiqORsvKnvY3pHL-4IlYfMudtdfvfBTroWXW-BTSuBkOiCc8CVOHmPggmiXAi-saSqWVp0UfnTJ_l61rMPe7gramVKbSicCbecsDxtS86yxc86W6Fw5lUphk5_PkV4aIQZfPBrj6ZkwXQLjxeGEeMorkhzEDvzTENv-WCLID4akcrKqpCN8uwiYVzOPi8Rwv8UzOr0Ryp5rQ9EbnTgLnoaK5CPidoOWjGsNUquVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خمینی خودش سواد نداشت و مخالف سواد بود بعد طرفداراش میگن محمدرضا شاه بی سواده
🤔
یه مشت حرام زاده مفت خور که هیچ چیزی از وطن پرستی نمیفهمن و فقط از امت‌گرایی اسلامی میگن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/139481" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUxeYo8aW0sykL31Eif_fWgy0mK3_T_3trQoLEkOx69UlVLSxFsm5J4FYsHW71WqRFgBFPlz_CD-uNZn0NC9TtIvJ0swxwVbvgh4kHYqO0CBbL7XUy_jFoUTxdV4FdxLwYGtqHJNa2X2OPnFxFXi_4vvI1ElL9d1prhtMiBUo8L8X3_5BKwg1j4yhEafp6HTh3zA0DkRzUl9ELmdhMThG4UBfB8SGUdHZFLx1GsCCO2vJHxwCdOmvCCTvswtnLfKVPqxplmDdkZ9K2p12ILtitXariDpbTh6whVefLJRlrSs8vyiYQBSe6pH0kU3El-XowIlZDPZ9QGlZSotTxeVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی بازهم به عاصم منیر زنگ زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/139480" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش همچنان در آماده باش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/139479" target="_blank">📅 23:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚠️
امشب
پشت پرده
جنگ ایران و اسرائیل
فاش
میشه
ادعای ترامپ و نقش قطر، عربستان، ترکیه و پاکستان در آستانه بازگشایی بازار....
دیدن کامل خبر....
🔴
🔴
مجبورم لینک سریع پاک کنم حتما
کانال
داشته باشید</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/139478" target="_blank">📅 23:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omint8r1JzeY2uyUyl2oy8IUbs3N26DYkIExlnl1DcaRoCZY1NkhBA4R51xH1Y9Bno-whAVdrlQkISpd_3yhEq96vCrmt2z1__60GYtwr4SbZDTS0zAYCABxzmd2ddVNj3h5xmUGlsH8SD6yT50_hhCFAOqkUO3ytZJ3zIGHDaNR8rtsZ8BgqZ456YDgkguZv1Q8RwrfWWWnJ-f0HjYJiCbFcA_hPq0_wmlyfh2TgA3D5hB8HAKxqfsDHofrsUn5Q0qTU7EDkj_2DHbzOZgE-r81dJpvWP6SgwfXlFuZg8AgYe0TNrUWl-eNA1-uo54KekS5xaQfKrm2G4K2bz4Ozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
5 فروند هواپیمای آمریکایی تانکر سوخت، در حال پرواز بر فراز خاورمیانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/139477" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
منابع عبری: قرار بود اسرائیل در حمله آمریکا به ایران مشارکت داشته باشد اما قطر برای ادامه مذاکرات، زمان خواست، عربستان درباره جنگ هشدار داد و پاکستان و ترکیه فشار آوردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/139475" target="_blank">📅 23:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت کشور مراکش : تو جریان تلاش جمعی برای عبور به سمت سئوتا
🔴
۱۰ نفر غرق شد‌ و یک نفر هم بعد از سقوط از صخره جان باخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/139474" target="_blank">📅 23:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هواشناسی: پائیز قراره کلی بارون بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/139473" target="_blank">📅 23:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd3485532.mp4?token=Hx7n9aZZnEiRx8SPo6IlfVdpiI5DfpKKg92z5v4fjU2zywoKmAqkN-se61jelhjLfNS7LWBoPGbIwrJJuKoqLoXwQiRmkO9OR03zy79BJ4I3yw7TlIVjy-2JFUAGzwVp0vvRMNMi5tyKW59d2Jha5uHIY_diKAzTAmT_RnLoBKnAnnkCl6W9JgRVJM8DYKqW3ot2ZWsoyAQVVKxRPGVFc8K1Lsk4nnYR9iuvOg5qSw6AZUb66pskeb8uqb6M3FVltxmoL32eb3szu7LF8CUlPtOZjq_DU5XEH5fQww5jV8tY22Lb3HIwsOixqmG0uw6c23MVgecm86urBFK3tSZEDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd3485532.mp4?token=Hx7n9aZZnEiRx8SPo6IlfVdpiI5DfpKKg92z5v4fjU2zywoKmAqkN-se61jelhjLfNS7LWBoPGbIwrJJuKoqLoXwQiRmkO9OR03zy79BJ4I3yw7TlIVjy-2JFUAGzwVp0vvRMNMi5tyKW59d2Jha5uHIY_diKAzTAmT_RnLoBKnAnnkCl6W9JgRVJM8DYKqW3ot2ZWsoyAQVVKxRPGVFc8K1Lsk4nnYR9iuvOg5qSw6AZUb66pskeb8uqb6M3FVltxmoL32eb3szu7LF8CUlPtOZjq_DU5XEH5fQww5jV8tY22Lb3HIwsOixqmG0uw6c23MVgecm86urBFK3tSZEDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو کربلا موکب "خدمة ام البنین" به زائرا آیفون ۱۷، آیپد و طلای صلواتی داد!
🔴
منبع پولاش هم مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/139472" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
واشنگتن‌پست:
همزمان با ادعای ترامپ درباره پیشرفت در توافق پایان جنگ، ایران و اسرائیل همچنان در حالت آماده‌باش هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/139471" target="_blank">📅 23:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUXhKCZ43Dkq0vxY6YFHi7ACNIWwl_aDmL2Cb9WO_z91RpmHJ75m1snc-Q1u0VPx9b96ITGHq2H46vq4xf1zWTDQiPCcZ0UueXWLObpyeTH7VRvVg56ZU73uvblibXM3VVSBPtJDlH-d46js5X7jb6-WhJHIdIy0Pagkq-L5VXbog2pzghA7WydcRgoBjCcog0i-Y2DcljRhV0y94RN_YprBc2gOg2NUGxJou-hooLof-YFaMrW0x-_tCuYm8Y_POFAcLlHGBCPOMXm6e8IHIYjjaEjY-Tr7n8nXEXPhymyMraQDVXZeUc34tD5bORm98zG0fhE8urrsHPDOZ6MHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناتوانی سپاه در بستن تنگه هرمز بر اساس امار جدید تانکرترکز
🔴
از ۲۱ روز گذشته تاکنون که سپاه انسداد کامل تنگه هرمز را اعلام کرده روزانه بطور میانگین ۷.۵ میلیون بشکه نفت غیرایرانی از تنگه هرمز صادر شده است. در ۲۴ ساعت گذشته نیز ۱۳ میلیون بشکه ظرفیت نفتکش وارد خلیج فارس شده است تا شاهد استمرار این جریان باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/139470" target="_blank">📅 23:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
👈
والا نیوز:
قرار بود اسرائیل در حمله آمریکا به ایران مشارکت داشته باشد اما قطر برای ادامه مذاکرات، زمان خواست، عربستان درباره جنگ هشدار داد و پاکستان و ترکیه فشار آوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/139469" target="_blank">📅 22:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK4nRAOwdO-V38lROv0OjDkgfDGph9XqfZSki9WRWmJunZQINljdAf5AHEbUNOqqleRejfRhMKR6w_EM5gG9rmpJNLjCABx95DmIjwND_H9Qn5BEQJ19tb069AS3mK_dQuctIU_ZStvvzI3sY1LYKE6NYoSU5afj5-zFL8NnNi_9S9LuZXec3TRHydCkcV-nrVAXDYsZu81EzFDlWp5TaG19s50i4w68anz3nV_FkxdO32XyrWCeomvJ-WV0vaq0LWGSQNhpTYsrK0kCjryzaWWzNSuuH_VdLfdrWMV9rH1-3DuOrqwBYQCrwe_IXQQUEBoYP_s6fu49J0ypHLy4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش ها خط فقر در تهران برای یک خانواده ۴ نفره به ۹۰ میلیون تومن رسیده.
یعنی اگه یک خانواده ۴ نفره در تهران مجموع درآمدشون کمتر از ۹۰ میلیون تومن باشه؛ فقیرن.
🔴
حقوق وزارت کار چقدره؟! ۱۷ میلیون تومن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/139468" target="_blank">📅 22:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7b7518965c.mp4?token=vGo05dyBbF5frqP2CvGWD9axRwxKDIjAdnBoazskaDhzX3e3mHl5VY1ZCLX9rLWTjigAmkM421hUUrUyUDhQeEuwNudHNY9m9dZaKLQfNo1v2jfhhq682oCXrNeWJzJfhgkyiguy36liD64BQoB_F1RXqR6kthygNbiH7S6gC92IC3KzVimDwx66nm5tG4OX-e8x91ADVazQHdrbWwKLDtTVzZ_B-nEEkPP7xbWGbaaDLNEIMBUnEHoXSvmD_ZiCsRlMkJf02CZY336IyrUXaBNDd_rcppt1tRNuqHIFLwtW8_POUj-az2QbsApK_NbfBYv4qXJrSsj3IfQqYQIy8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7b7518965c.mp4?token=vGo05dyBbF5frqP2CvGWD9axRwxKDIjAdnBoazskaDhzX3e3mHl5VY1ZCLX9rLWTjigAmkM421hUUrUyUDhQeEuwNudHNY9m9dZaKLQfNo1v2jfhhq682oCXrNeWJzJfhgkyiguy36liD64BQoB_F1RXqR6kthygNbiH7S6gC92IC3KzVimDwx66nm5tG4OX-e8x91ADVazQHdrbWwKLDtTVzZ_B-nEEkPP7xbWGbaaDLNEIMBUnEHoXSvmD_ZiCsRlMkJf02CZY336IyrUXaBNDd_rcppt1tRNuqHIFLwtW8_POUj-az2QbsApK_NbfBYv4qXJrSsj3IfQqYQIy8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از طرف صدا و سیما اومده بودن از چند تا کرمانی بابت حفاظت از تنگه هرمز تشکر کنن؛ که بساط سیخ و سنگ راه انداخته بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/139467" target="_blank">📅 22:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaA65339QOhBmqDZIidsXYhUMyJLGQSWryW8JKpp9kg2VW8Y9kAIKOGYc2q8d6VrGcLKgDj1BEi_A3_EsaL0NC-kv0jCqZbuUFZ0v0k8F7QCcn74kmS8M1qeoCUkw-XI3G4N9kmGg8psVN4jAkLy43vUj4Ln22i1nUBjqoyYVbjJ-g9AUmzFau5QVGLMSr-2co5Huj-4Bt03vdKQqBpPM3tT3n-a-CMrK63dcC3kCYDZWJJCFiiAX2uxg35t74bIH2cfuHb1kh9mPBZViACRMyIINwZp7Q9_IaCzmkvCg3FC9IxPUMRn5SyqB4MGswqzWsPQ02fX5kjU1YoPvGHA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل:
ایران مستقیماً ادعاهای دونالد ترامپ مبنی بر دستیابی به یک توافق مهم را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139466" target="_blank">📅 22:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139465">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
فارس:
روسیه 11 تن غذای مفتی برامون فرستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/139465" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dfa1b7126.mp4?token=qG1kdriuDdsu_l5w_XNvEKFd-hu8iJTIYKIXMcsz2W6OUGNagRFHbxugAzWUAgqD5udjO1nNN_JpHWmiyXsph5My7Rclg_TOx_EgJsigmpHuhXQdRqeBJSkAd2ZZPCMel3KhVGN9IfwMZi2a2-UKaFntgsVtM5S0Cj6TE5FykTzEb5765DAgXvuS7SckAR256vT28BPGrjjC2S9YL3vR_s_H7oj6Gb4GlfphVkurhthICMIBxl8AvtuDDWoKPkafJBWWCBj0MeKEYcwo3uzy3LBjFcXEzXFpGEUH86k3e8kKbem54P0mTYn87pa-qe0cQPTw4kShMm5y3VBlJzkUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dfa1b7126.mp4?token=qG1kdriuDdsu_l5w_XNvEKFd-hu8iJTIYKIXMcsz2W6OUGNagRFHbxugAzWUAgqD5udjO1nNN_JpHWmiyXsph5My7Rclg_TOx_EgJsigmpHuhXQdRqeBJSkAd2ZZPCMel3KhVGN9IfwMZi2a2-UKaFntgsVtM5S0Cj6TE5FykTzEb5765DAgXvuS7SckAR256vT28BPGrjjC2S9YL3vR_s_H7oj6Gb4GlfphVkurhthICMIBxl8AvtuDDWoKPkafJBWWCBj0MeKEYcwo3uzy3LBjFcXEzXFpGEUH86k3e8kKbem54P0mTYn87pa-qe0cQPTw4kShMm5y3VBlJzkUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاق باورنکردنی در ایران
‼️
🔴
یک دزد، یک دزد دیگر را با لباس پلیس به خانه مادر یک دزد می‌فرستد تا ساعت ۸ میلیاردی را بدزدد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/139464" target="_blank">📅 22:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139463">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سخنگوی دولت:
تغییری در قیمت بنزین ایجاد نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/139463" target="_blank">📅 22:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=mPDVURkMj9rv1zGopZaBepQTCAb3_Ft9-CGKCKPTpPUBtakWJzyvT3HkSOFq6tJbg3TVfktA5HNaR0xJVYOwmqfJ-NRpZ3Jznv-5086q7aJynhzN4M3KbyxMmyC51k0zCCihpEWyVBzonwrQWn-zSl5u-TBAmLIvRfisTDAru3y3fA7pJ98OYrw7qt4PW5yxS7JGzA4BKH7bnQ3NTwtteD51s-x-j2E54oHc69XfT1VpmwN_e6qNlzSPH2DDdW5Ur9jT_COvZw8bkKkRPI1UaaUoqXvlFngk060JAZdd3-JENveXCaAhLRagmLguajU7zYt-FGTB31dfcLc2PtpriA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=mPDVURkMj9rv1zGopZaBepQTCAb3_Ft9-CGKCKPTpPUBtakWJzyvT3HkSOFq6tJbg3TVfktA5HNaR0xJVYOwmqfJ-NRpZ3Jznv-5086q7aJynhzN4M3KbyxMmyC51k0zCCihpEWyVBzonwrQWn-zSl5u-TBAmLIvRfisTDAru3y3fA7pJ98OYrw7qt4PW5yxS7JGzA4BKH7bnQ3NTwtteD51s-x-j2E54oHc69XfT1VpmwN_e6qNlzSPH2DDdW5Ur9jT_COvZw8bkKkRPI1UaaUoqXvlFngk060JAZdd3-JENveXCaAhLRagmLguajU7zYt-FGTB31dfcLc2PtpriA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت:
تا تهش پای این حکومت وایسادیم. بازم بیاین بیرون دوباره بهتون رحم نمیکنیم و با گلوله میکشیمتون؛ چون داریم دستور خدا رو انجام میدیم. پاینده باد جمهوری اسلامی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139462" target="_blank">📅 22:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIi6thGVLwx2Fb-n75I-Y34vzVJB7JwwxuqfC2-8RaAQztpoV7hDuTCI1N1MXBsZkdX8Xsx0Ie_7NtJ1JKoXeWqJDw-fInCQ0opbd6NwjLcfl3Y46aPTIKTs3xPvbIgNhQN9gFAp2lNrSHBj8VQKSy2A9pujHHtdNYCj-j9Bjk9M-lGoinRgTMEK8VGSs-ij_9jKljjFE_j8P7kUqx1VbwtD4QCcEkrFxT1_7Sfhy3QZBC4umEjAzQhTlh6QcsvX6H3pA4um7_1m3CpmejgdzhYdJLfNg62xi8vz7WYNfD3JLf3z53j5pb-FGWqogVVy0Sho-G5UvhaFtgOMK2aoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیر کل فرودگاه های اصفهان از برقراری پرواز های مستقیم بین اصفهان و استانبول از ۱۷ مرداد خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/139461" target="_blank">📅 22:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4Ij41z_yGeveEFMNOcUEB9IHijGhbssheQx2Tip0AbHSmZ3wdOxoxwrv7TNtta_ta5iguP1Huzfqya7GCfFeBQnI2x1APn5yi6FmoY0_ly0Z8YGQs0Ir-dbFt_nSFNU7HbH58Gea0fvC6QH2G1j9r5trkMEKO0oMQ_vKO4kNi7N-8raXHInTCOuBbpGhTWrdc9vvvotEBcMjCSDSVuZEHiHt8LJq40DSQwO5O9a3-cc1-uYRl-Z_A0a5uZ-zGxhLaW9DdkxSM6q3FWUgjhMDdV8xnhXE0KVwhb5x-5ePCWmJ9-slWiRa4Ij5XQMxLhV3DekhSMq_JfdIlkorU-dlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی شریفی زارچی:
وضعیت روزانه‌ی ایران توسط عاصم منیر و بدر البوسعیدی و محمد بن‌سلمان تعیین می‌شود؛ بعد می‌گویند خامنه‌ای برای ایران استقلال آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/139460" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNau7HlgxtfXnWMKrnoHr-TwnwKDKXHXlCBWcPAwJlfNnjOjUynoXz5SeaZGkTSHbMJF7Lea3VMOfSDWFK9m4sficuVnRJsRjwTxS6H8Kh5hscjUzQPCyPfDCZYOPCVwwPj4Ur8Hl-ZekUAY-BQCYvU2KHITwdiEsuQMDg_aBTvQYFxWRP9t8g8OOGm0cWiauoEO6Bm4deytLEST5H37JvJEBfGMM7eqRq2BUG5NwCpZ4da8ax0AjyELgegCWgzOwEWK-Rtf2XupcAV5e4iaVtnRKvnrYeLASFvq-L-Lo3xoIicP7lkF2w8BwWgnxVhLURb2UiSlpEDcFl5Zm07GKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: باید بکوشیم دشمن را وادار کنیم به آنچه در تفاهم‌نامه امضا کرده پایبند بماند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139459" target="_blank">📅 22:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139458">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
یک مقام امنیتی اسرائیل به کانال ۱۱ تلویزیون این کشور گفت
: واشنگتن برای دومین بار در یک هفته ما را از حمله‌ای قریب‌الوقوع که می‌تواند خاورمیانه را به لرزه درآورد، مطلع کرد، اما در آخرین لحظه و بدون هیچ توضیحی آن را لغو کرد و این به آمادگی عملیاتی اسرائیل آسیب می‌رساند و آن را تحلیل می‌برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/139458" target="_blank">📅 22:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
دولت سوریه با موافقت سفارت بحرین در دمشق، از ورود زائران شیعه بحرین برای ورود به کشور سوریه جلوگیری کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/139457" target="_blank">📅 21:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از منابع آگاه: اسرائیل تلاش کرده از فرماندهی مرکزی ارتش آمریکا (سنتکام) اطلاعاتی درباره حمله احتمالی آمریکا به دست آورد، اما پاسخی دریافت نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/139456" target="_blank">📅 21:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الحدث: گفتگوی وزرای خارجه عربستان، اردن و قطر درباره تلاش‌ها برای یکپارچه‌سازی مواضع با هدف کاهش تنش
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/139455" target="_blank">📅 21:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از مقامات امنیتی این کشور: ترامپ ما را در وضعیت ابهام و سردرگمی کامل رها کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/139454" target="_blank">📅 21:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
شبکه «کان» عبری: تصمیم ترامپ برای لغو عملیات گسترده علیه ایران، آمادگی عملیاتی اسرائیل را تضعیف و برنامه‌ریزی نظامی را زیر سوال برده است.
🔴
این دومین بار در یک هفته است که آمریکا حمله‌ای برنامه‌ریزی شده علیه ایران را در آخرین لحظه و بدون توضیح لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/139453" target="_blank">📅 21:25 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
