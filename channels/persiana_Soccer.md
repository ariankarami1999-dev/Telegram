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
<img src="https://cdn4.telesco.pe/file/OcA9oU9QPTndMhxsxWOTHCWJ3bZrVdUZ5TrO6Hw4XQysfrmOCnhntcXrMhTkC6Fl8wbodEgL7Y3hExvjtJQ7lbIqUG6pFNOmGNHc6XsEIAB4pwJ5O3BCBAt63X5crSFWwIYWVrRFSaqf4PpuTSsRWEoGEx_-a8P2_8Wds8A3i-NK-5PBaDrUfV_KgBRohoSK3jbOnushSuB2yj-7chp7JqIX5m1UtKsS27Xg7igjtHL3GTk3x8NdAkj3N63LukTd0Uiinz3lSpWvSq1BtPe_2RVkXQhkSs9DeIsSIHX_H76QA9UShyZEQgC3qSLJ2c4_TWAVajQQpAnGxH-QRHMDUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 588K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 19:05:58</div>
<hr>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=Prr34NRaDEQlZsXpAVf6w4QQMe7N05hshoHKZSKuy2EbLyfDjusFEOioANxjDo-g2jy4M6Yixje1UrpH9p5Vms3c5TxhR_9etmHDaeqh56tCntmSI0qnvu8MZ40w_UgxcjkccLRACYr3SryeowJ3V9bBIbfMxBhnPZ-fzEpp2yLu-q9nRlQbGmGQQqedCILNqtA_PfXZrwRD835vAo54mHjCYo62y8kDP-hi4CmfYPp2GfJGQNQW7HdCcBPi350dFRaxD1Fu2K7bPgd1IBQNWriCjL9RqLQIrYvtJSqzaMxQe5qHpZv4FDycq0mpqhZR8knoNiBNgNEZvmbffgpchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=Prr34NRaDEQlZsXpAVf6w4QQMe7N05hshoHKZSKuy2EbLyfDjusFEOioANxjDo-g2jy4M6Yixje1UrpH9p5Vms3c5TxhR_9etmHDaeqh56tCntmSI0qnvu8MZ40w_UgxcjkccLRACYr3SryeowJ3V9bBIbfMxBhnPZ-fzEpp2yLu-q9nRlQbGmGQQqedCILNqtA_PfXZrwRD835vAo54mHjCYo62y8kDP-hi4CmfYPp2GfJGQNQW7HdCcBPi350dFRaxD1Fu2K7bPgd1IBQNWriCjL9RqLQIrYvtJSqzaMxQe5qHpZv4FDycq0mpqhZR8knoNiBNgNEZvmbffgpchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiJCH_9-o_I-KfU8hMwx8RminURe5qgAq6RNNdCIaTyY-m4g-PitIBtZmR6hLRJvfycAV4Osf3If2QusbKfZRbvq3e99koFFdArUxf7euPGkP1jdEy64j-KFqkpVR-0xq3KDBKzlzRJmh45-F8awq5x97kehKtn6UP0CzVnQVwAAp9A2nmq8KgHIBWJWseQxi5mtGmkmeTiz0C2WvB8x3j0AD0td4hNWtXhWbaY2fkQv8Svjn5K8ItxBO_eTZhKxoFw3p9EqB8hQhEE6PnXgv8AYlqw3Lu9gwMmWx5HgSP2fDHGlk0fIv2pUVlxt4WMTdgXKLyqkTs_JV8ldxd7T8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzrnZc3PF2ZjbenaLwEfwRr0ifU95f-LXQUwROkdIGfgcy7x1tGhKqZE-qYJjQpNM_ZLNnjas-vP89S4Fdnp0Euw9Laf1VtGcBHshDSBq4__4Ij3RrK5kJvGypp640Bl-6VG1B4cTdw8G-G7l0IA8wzvZ42POH1exwv0tOJEDh7D4zoYgtk01iOrsEm0Rr5XRuaNdRSWgfbRTUclTfO5_4CbGkipFhUYw3QcchpC_7t7S4qEdgp9JvGlREQ8mmTHFjgkOBv4zaVYmVJEIk6Lja5vPBxvOvBCElkrg80AiMMxst5-diX3HfeiA0_h-MLjk8TDv2Pso1599KHsKnFVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKq4T1vZSP1je--aJiVhKfRaQfQR7DEhhrRZPmchhLHIs8VRwCuJIpeSbAntHFaEt1tk0ruB6GXh-h10gXetHvmA0ovMzo96dRhPpUthpssIqfm7i8d57d5Oz-INpKiokqUBHVop_sgDt15GUTjj_dPZ2o7v5kZ1cu6gcxKQvtWVgOFEEFYjDgqNQ9YfZhcp4B7lf6tOuX0yPuKO64DNqImDm4yhSlqF2GEmCRgkAOxQDJNDzAU5QYzbGQ4LL72qiDYkn1O3Ke0QRklaNG6ISLZAWn_uc5uQ7P1ursGPGRVdCUop1dnoVZMGqfbOa97QKajG6kTkLT9-N1QHdRwN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrIlwwzjYCy-iEpbXe1UdW51TGrbHy8uLuod6Xo9JhYlmBRPuZFNKReO8kl4uXt1ELceVv7vsrJ_sEQS4CfPpOyq0gFSqMmD5Ps0ia2XimAogI34cVEVylrou9Nfp5_-Uyxt1woCK9KOuWK53uhNGEipy1yLr0tPW2CFeNCtGfjP0ArEOk6q5WUsLzU2qIV5R_jx1tQtPPRR05uQfMkmALwB0fbkN2yl1-RqCIJ4ouGRW5TOZLrvUQ15EobCmqAt02E-nFhoKJi4NVwQNH6ET1syUsCm8F8h4-pJWWWgyWXgL07oC1A5xRFVy-nABLabASH5NFmsspUBT4pShCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2VW5LJvz0BUEUutl19NASI6Boupbja26bx5avyWVUEeXIRrVN6G8tVQCaX9aanxLeJ9_YOu6hFTlyofvG_gOM3gW3jWd3dZR0me7wx2f_lwp-LOEsA6DgCxqCfgmzrMh4V1wo-8tyMmXx5QWADxgJn6Vf0axmt11OJF8tPReH1D1nmWOu-9FuW-pBOHRCJPjeolWqlPWTKAmyvATvwFQ3EQVK28Ycnwq3DOjYZQbw6VI6JP0UcNM_7MWlRmXJp2TWiQiY9aIV-QBhfjWiNTjJXTD3yMQfsMN7LRxTs5A_YwlOwnvR0uvf3MyCA0Th-uaRh1nGVDvMD6xR6rujldPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_sbgI_3m5iiuF1qwdZCCWHQJDzRZydvEcz3-rQ_U37iX5Wqs88AaDA7ApNZbGxsZiWe_8iitLuQq0y_d2GCbTyiVMO66kG-mY2sZ1hCbyWpTB6pIoS_si6rMCBlPeElp1K_INKPjKLX6BQAW8SQBS7hyUSQgKtYZsCtqz7lwpNmzMXOL_WqpSsttvHBkzFBX8HN1OUIqB8XNjI2weCRQ0Ml8P9kXf3hPlR3czJ2AimEIyMKtvH3Jcaq4BxXwo1wqEJeQMpIyy06kpvmFUKVKZzvSST-QEFmrQyDr771N-KqkaNTI40WqNPVfL9BfsPIxjBYTWZVZZaGKHjSTzxceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26553">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spAe5Zw4JmryIT7TSxJ4faMuko2ehzuzV_gHzfI1eVeXEZgEkHAv5jRZ5lYH472lDzfXvMbe9YlBFV1vMeDC2g_0BpCiqgitkAYM6cP_CzG7zF-NX8CQ5tGW4MmuK8sHP2pX4GhV9Nvm485w8XxSFPUt1zNhjiQZlNO4oHFQvnIsKJbVPU8u8befCldC45RLnzfyVKqtnBZi4AYZFVGd8R86_duQOFbAs7LpdHcN5gpOlbwIMKlkFagQUa4QFB_3uCBfES4c6alZvj1DQu6tNswQp0IqFzTK5ZXHUx4BFA4qhUqqpWvcqP8kSzH1v_dNYxqSy63pKLMhmEYK2MwqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛همراه‌شب‌های‌فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/26553" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFyIg9yz0mLAbJarvskX-v6b0-vGO8fs74pidC0m9FfjRMcbS3PGev05929daig8YJUsFFMnKPmbboHp4TvHGhphGbNNP7DIuPoasoSak-LfpYu07GjCAWAmwn2ug1Vmjxebm6enRy55SEsCitBaMnXbglLqic6nsNwMnd8IPlZyTvpPtfI8ehEpMY5xwmUtBTd_lKBEwsb-hKHnirNhZOwPfTnBrtwSDMm5C4WsjsEVAbsJhkFPY8GgkvDgjFV7f8i0l0vG7FycBLYoZ2_lFYbXPxlhakwNaJnX2ZUHYUyhfZ8xQj4EFrZQ-Bge94iRKfHIo3Jxf3FJpKp6LTG15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjkJkh0qjA_6d4vkFa8nhklDpj6-vu5CknE__AK4VkZxn4et3YjOnLEwgNLDNecKj3CwHaHl4cinPKgFPQy_8ivDcZ9xA-60YNiwFLck6ZaMMgwmuVU5BPwzpbwpxI8QphSP3PEdm6yOcPtLJTjdHsZMeXQDOBpHik5N0FML-KOUUBTuFW_ctJLKmXTI3a0jKtbhjaxXGIgNquQNuh-qqoUCT3oAKx28rTMu-ZHrH9fxBm7UbCudMVbSt0sefxk3FvBJiRgM35Td48CBWNAL1vsAyUE7cZRPNGNyZ1DPb_eS4Zmqfoo0Z2VY1XMFFG9jvLyn9jWCFWKFWYQaZPlx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoPgrCrjqds4K2MQoABNBGV6ivdfKIznpVvNneZnNmdqve7YVYIt71shdCVRadwIa1VFsnQjGuxyK-7svyOHsn5YoRt_WYfLZcqdydZK6YwtPJglGwuitJWXN-iMBfXwMOHboDHtItBp6RecWPpZZpPrSDMLDUuBB2ODyU50_YjP39qVuF7VLKEt5BQ8TajfHXe28FyqaYxzWpu0diL55d2ljO8Czusx4QG6LQBHvix9sGM-qk0i42siYM6ezBqjSGJjodQzTYZqovw0jdOx2alVGYgRuIE-0Uno3MaIttj3PEGoYRx9C8IM9bL2Mf0vvwKKHL-qBth_mAM0DrKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LElJA7r2XpTHYq6qzGDo4YfuKN_aUJTuyBSAmC-XqXYOIZxL6dx7inq2qQ0Y8Y6ubt-jwUNEgzPEmm2fFLPYKROYVAlxOlNgSwL3i3K5ruxrJysN25oznwcUBzrK-gWOVzVfSTPEB-Yh96YUEVMOuhlLjxBAFKzEXd9Tlu-ZPFKOoo3yfgwnnPSVQzLDI35ZGU6XWD8ecy-gGix0E2_lQcK65AvEiwig5eDE8KT2mPB96ehN7fHhnxlTQnqrQpgYyVkIS7MQljcOfwZSmgk5_j2GadpUTiaJl1kKeglxRXX3jUXbR-0PhoEt_nuwGOY0ctxW9lOs-PYFTA9PmM1Jfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8HVOEFgsqTdh6EGiGM0nhGO_JGjDm3vImg-gyyb8Ac5tAT1lw6x4Hgt9lDvltZxdufEy-0mro-E6gj6rUDvKhYMtTtUUtbGUddymyAMqIJzKpJOSWyDWsz6Fy5eyEc06DfveAuHknXY3UfI5cBfQ45u_YqA9t9K1ejwnhcPGMxgNOEgnXcZkJdLkADLyg2dJ3lax3wAhi_EXe4SInJ9fH3aAZ8-DgLeHzgAFP1ig-xcBNObUpatafKXkKQo3d6Dz0ZUc7tkciOtpTvgvFLc18g3sQJnthy7OTXPqZ1Nl3ypxI0bPpRirQZwR0lfnEfc7UxAFpIuKCb4_6YkR_FIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myEUM4LfVoGAktSpz__EHsRUJGm-jbzTAeaCzIVL_kElalS6SI8qrXSGDalGv5XM76UaGtwqXiLeC_bcmB6JoffKHuoLINqAQ8H3OrF9bULvuOFK_eFibMsRWrakoX4ksok-f44RHDv3NBQanfGVrKDR6FhXXuVe2NsnrBp-nGpYuoihTyXS3iBs8WNSB3eonbMhB0D_v2DDsc57nsa6c4mHyrwN7-2Bne7gQTAb6-KuvxpfAHzEwjTPlRT564mftQ-QEAGKZYPkyh_5r_Uz734xacdV-nXhDpxZU_835oy2f_FNMlhTXQGXeiBvT3QmIOgprLUs5gyO2PgQ91zJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn6a1eYzY7IAMvsK7-_3lQB8CDdM692rqGEBTMlN9MJrUBsqso91MPF_koMSl4Xm1kG1SuAkDBmSUMm_ISKCS7G0TtmF_XvBueiv5ACIzyn5RPy1ZYtv3edgv6sJGCD_na43TUosZmk3gc9IPLqpN3BrPuA-z8vmz8JmZ1x0Nmuc9kttU8SWXJagQS99HuIp5MryEmAp4Y6nFOTnFZilFlDDLNp7RiV0M8oiNarubpRhFjfvkL-28bAt_NG8AKjUoQj25uoySe4M3VJEKwq1dfqx8SOTGRti1T_H-SXqyaBPI-BTOYmf0TKPI5PKjqRRq7TGBKuremOmbUhQJtq1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=uwKqCZ4HfuM-1Vvha_eX4JEMOdLMHTPatNwE6yBifbfS3lhCYqJA6NdILpk3CwWzTj4OE1bpZPjRGylhDVNYHyBSahdEqU4xF4SxdT_7gf-cNnF4bpglUfFohO2HR4pkbcPI9vYDg-Yc-G-CmsvHU34pf2wVKn9oReVCyYDV_1hoHP-b17sVfWRO4TLl9RkAPUrLixiBD9B6ZAq39KQ0xPFjk4J3mf_ijpR3FQuzTYbqt9hguyrA433Z3YvLtjentttnJYwCy5Tg0nPo6chTzYFEocYw_ZQ98RjTzS9cIWqQs6WhEA-kGLFBBxNHT5zUmbrQjAnAgAE3u8zvhlMjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=uwKqCZ4HfuM-1Vvha_eX4JEMOdLMHTPatNwE6yBifbfS3lhCYqJA6NdILpk3CwWzTj4OE1bpZPjRGylhDVNYHyBSahdEqU4xF4SxdT_7gf-cNnF4bpglUfFohO2HR4pkbcPI9vYDg-Yc-G-CmsvHU34pf2wVKn9oReVCyYDV_1hoHP-b17sVfWRO4TLl9RkAPUrLixiBD9B6ZAq39KQ0xPFjk4J3mf_ijpR3FQuzTYbqt9hguyrA433Z3YvLtjentttnJYwCy5Tg0nPo6chTzYFEocYw_ZQ98RjTzS9cIWqQs6WhEA-kGLFBBxNHT5zUmbrQjAnAgAE3u8zvhlMjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYi1qd0y94-tUhZZ_LDlzg9JxOlwB2-qt09RFb0IR-L8r0CfMAl_bP4gObtynSDFG8totKzSTiVR6UTPWpm1aP0s60ZimT_Lv6JB3VJVJBrgxzIFUYGWLlWMD17PUcFfrOFMPqXm4PJqN2jBtz-PKZ_PKTRMRkxGaDsCpatbO0paljPn9aActhnAAI9txAJ4x8MjFvy4EvpjUaY6u5Ih_J8NY2_y6dm9RSfLfX9r-7kZiXVu3Txbrd9MhN2NhkafQN8gshh7pvxwtssnCgYMhPkTEM_lSgr18kotCvwMkwPIFPI169SoNqqc2jR5hUOPTSf9GKQVu2HiOcfhvU3O5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuC6yZ90xYW_VDFyxdjZ_6EVQeoT1titII7-PxI3nCeaBrfiBRZuSKR6L2i5r-zOdUVxsLa2dlY7yj1gNWCb-mX8ohuc1wm7V6Wr53w5g6RTfKv2boGznc8Tdn4p-CHRvAgJ1jKV1J9VPku8f4zyfllVk_s9607WrgKYnwmhutBDdsODHk9vFJR8aV_BrrwNiLOY_V4wH5wHp-Sv1MjG8ZOmyha4XKY8QHc3hB5C3S5VYFFs2HnRBb--upnWj7Tdygwp061HPu4QAWJKC0rpVV8CVjsQI58FIz_qL8Zx5h1bvWmuCxyLGtQzW_tTBHFTDT4r09ZJw8_TW3myefXafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f10IkFTZeAnG0mQW9KqpyZWCcyHI557L3hPbGBSpdaL0hB8Xs5W1KzTb8jvqEfqx4ayPhp9YjkZLSSgHXJt2X3nA1xxL6t2hHmLhraFTkc4131Cv_Xo1HsiWTJX3m02l0-OzYYOnW0wiInvXosq-RQJX4odDkbsx7WvXhtUYVIhGr_lj-FVN81zFz8_zweL9A60905vC_9gdTw-KLBBcL-OAY2GGoQ8bny1XoGk9ExIGXKfkM_Eh5f0N07a0SRZrWc-W4WL3aKDVGFKffwu0BURKJHFnleX0F4svzOnneB70jByud3cySovsdaPJgLHjPdjZHF1gqbFrogGaNj9U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4_2XYAWcZ6-9bsLS50OGFaaQVpEr_QXGe4L8djHhp5jf49KotNjj3xlOb6aduNSfalLai7VfNg9FGXO8d7LTdfqUOVR7MQNBHC7b3MKYsdbX5-Jovz8zNkzvttgcw48R8Xp_aGzlXXFSL71n__COuGxuaoJgPVNafELt2x72N1PgBl31GSLxnXmcygMDNCD4gT-vS7bzfjONF7xeBq0vbaavsGckLG5b2BtZQq5uxHCFVfK8D6QotcIC0NXMlMlcRCJR90SwT_i8PKHiAdR5joMneqft86RJrDtDtY5DQP_jDfTiS_7fgo4EoUhhNTtLG-rvCLfWbupjGu538cmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWwuJTUf98mouHzKY_GVZ_-IvaWVMs5S6bE1iYKjUi1qulLhdGtkLmz7vmIycghjTBAt2tZNIRYx6PeHcbyHAPO32Fu0X81Q56qqGpJuQMk8EiLnq8NRevfwJbVTAsnm58pPVeY5EhKVW_rz19BwPhYV7HCIFkuFILbgGuuG4FrdHvs2Ex8JEz-DdcSL5mXqu1dumDlDUM9H_MwGgKekjjAW-iH5_vPHZOXyeKV_tQHzWWjhS_zIj6UO1pe8kwEbLVBTWCZYq8A3GYupmYG0XFnCsj60NYrLbByMkPKwdqD_fgTF1TFHFlf_Vmf5aZ5gwuk4DSytooypq_pKAPAnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDgskXSdDbTbJsJ0AeF0Osj1AT1g570v8v8WbIsbmndA3EVUR39aiFSxhMI3X60K2ukTXfKpGWEn71HdkT224P52mE2PWqpkovxQVQUoPeLH3ka75myC88hmaehD3r7HCXg-TVq0vqP_McyNJ-F2TaAfA9z3Tpq3ngmAlc4bsdQ8u6uKyhB1W0ArVqphiLwc-SAIf7M2P8PcnV0gbWZt-2cz57Tr1d03tSgeNwNy5sozYd8LYtPfk45-YcfxV9-qzQuImZuhh8LTe_mo7zADsSerY_pRQANavvYkZ6R6s-VJqx4USehfl7aX15eTrsMEb3sC8WrVpSrDqj43NZYqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1cX394acANflFYD0cRYdCRawGpVDP2z_n5p4jF6UzKZ_a-gc5izhAsBwcAZUbyqc7O_BFLU5OYfL2HuXSsaXz0ZrXfpoRv1S92LQTch_DEoFiqfAyiFVSDJS6dYQm3_B_8LSxTCC-E_AaWiLaoyrnnC5F4qtira4u98yQQKBlQgey8xNz4RieWbjgSePjHeJR5CTrS0hlBn-ixJaSKv_SHjlsCFCSV0XvpXenUidg4MNNyJ8OLsp8JU_S3L1FrX_vOVrY5iatPNwXv2n7CMp1EuHzwSUM6eyoMo5EHo2XEcSqOYRtKE3jZK340zPyEB-t74wOX3GJnI6jwIELlMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smbh71vMQYYHSgBhdIccs1ffGIXpYPT_v-2mF2e5pZWJxJ63QJ4Gjl4TGNiceTo9iL9dJD5b1EzskaDpqz5RhE8Iy0ARoG7I-mBI0-iTdKFsMCRhVieecpSlVl064IR30fIw_izNnF71hD2a9ERSiEnF-CIEWAdPTOiqf0mfEyd2bSD5cCCS2NycR0-3lvCLSS8dMVhMzneShKfvKu9ui1Xjq3Aapt3z6SKcjQH2o0SBsM4TtiBME3wka1iW5Zd6wX6uNpHtgl9nXb6T-_96Et-F1Bm7jyg0jJjavEpAqNKP4LChBc4BexxO0v8Xgrf2Wkd260xqr6rPHu0_SPnz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spT2ZCwfr6FwvrBTyYB5FiMP9TBru1lZ0mR62Ykv4YZaaFW_TEzr--Jdh1XOihpQJg4KMVo_gvoks5tKearEDLzXROMXbHKyxFqUN3WHKeZl1M1PjGoqZNhPeaDAMwnsK2gMb-dm092VtOX2rSDGCkZRKy3aL9-22F8zaKHkzc-wGCA4j04i6h7GHrogpLpMDzneW-c2hszeWGCnI-KXUFXP85LlBeXanJZorB3Xq1W59Y3LasZIE2RuMx6hEmWjMvCBPVcE4jsmmGfm5Ds90BRKD2pLuF5v0FVq9Lkx7WCzAO-BW3rFiNc3KTqjN18bBUu5rP2gX5rdqByzmCAZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l07_8IYma-UTmYO8ovVWRfdKsOOov2LTrxGhmqFQv2X2uuQF9iLLv_TGolkjCVCEi9gfRrS60sbTU0UCCJylfX3JXAKnemQjscQ_otwQKFDtUg5nh-hoDU7Q_Hbbfn1_Kb9ha-PfkLDWk3cmHGtzmTmkdrPTjSfS31Jh7rI3BeltKwFogvGb3rsyjXWV7Nx66P5AGD3OQpn-X7SmP54lCyn1x-BaWZePpvXd1qD6poWoEYhluMj8H7_92QdDknDtU0M_p7EoqpnfmUhPLB9aBOqUHCgsfr3IA6_fYowr6qPhCD4ZDqYhJCdlOFn-u6hRIalCF_hbS6PK3ZMrwClidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1N7nP8TEDc_OsezK4dXeC0YYtQwLgVclfkPsmGyelFp6_DsLVKvbiEAOT6W0Nr-beGf7AFrMWJQkzEZmTXq5c4cRiw-WAutJorVlXghh-8TEpzXHJDWnfkogCYUKGhi9qlW5F6PkqLDxw1hj5P_BtA2lOkY3EP5mdwthR8EBu3egjnZdh-n0gB0xpdsxYGymtWcX75rn4Fx5YKvPgEY-V81m6nViUEPjEmTrI9XEnGjJi57V2cu6Fdb22LGH-0m8EEJG4siVFPQ6pyoWlH_LJP6dUWHWOzdGZdKTNqEVPTKjE-bieWCuhkbesQYkZ6AO6RWIgdFnC8OGSi68wOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=uyFjJKRvWGt0O45edsdvnPoSxD2sKqKgXly5tF07IPhLO_1e09f-HXaUsJU6RqYciCs0A0fOiK0K-NneIa6IheqzZfPVkWf0MpazP1sXZ0lpb-MfxfoPZoaH9A_iuhzZBhFsg5Z0G6Ps3Vqo_SQEDAAv41iPUmaGmWpGG9-JpHBb_EsxnzvH5nY_49YWIq9BuCqb-iUSK6wB3Qrq2GMQ_RN-n8WlxAyyJKA0rTnf2qG0hMs-QPQZtEjfHzSKz7Ct3UOpUCKVOSEs0POo9OfdCleHIRSpCkQwKWq5LZXLx7byElz7ALp_mcpOKZCehPnOBSnhaNtFsL-fI2KDsx0eI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=uyFjJKRvWGt0O45edsdvnPoSxD2sKqKgXly5tF07IPhLO_1e09f-HXaUsJU6RqYciCs0A0fOiK0K-NneIa6IheqzZfPVkWf0MpazP1sXZ0lpb-MfxfoPZoaH9A_iuhzZBhFsg5Z0G6Ps3Vqo_SQEDAAv41iPUmaGmWpGG9-JpHBb_EsxnzvH5nY_49YWIq9BuCqb-iUSK6wB3Qrq2GMQ_RN-n8WlxAyyJKA0rTnf2qG0hMs-QPQZtEjfHzSKz7Ct3UOpUCKVOSEs0POo9OfdCleHIRSpCkQwKWq5LZXLx7byElz7ALp_mcpOKZCehPnOBSnhaNtFsL-fI2KDsx0eI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaMhsmamGPqSjJxyi4Xh18vqBafS3xNQbiVKYoLsNNEqsOySJ_nJc5WhCNYAUDvIMtwcCBwaA8uaLIaXojRFjtUR85JNH-rnwdq5Ui-Ydo-h7g7Q9jw_FWF99hkoqTyfPynrGg6fZuBNAP5hZhOJ8MTe10iLw1d-WV3DReu7Va6xt_EPjCr6mJ1CfQ3FzIB-I0QdmHDHeLBK9JDgsyYtViF9P4TliSbPizRllxdFUM9HJBbg0XhOuXOc7OuLdLmwtKQe-uz7Ydglt_JIzGwxVG_1cmHwCibh-PVZiUXgQ-I-r3c63PYuvr2SVJUsXPnB2VBP7KAqhGBH1Ah8HxTcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuaO5azUhCWWEJNsHPwJXUiqXK2DJjFbJN-dOjRARrqYYjQHOXZ0deEJFJLIgXb5U67hUuGy3PqBPkkE3RAOfUZaZI_e0Hppph5sLwy2Jl-thbjO6OjXTCNtXexZWyBv7Ai1LToKrr-437dTn7XUVrpMdxTRcyqCm7ByDC7FEjd1I9cJZwHtxcTHB8FN0bi-GwFOyvr7eIl2BZ9haPYlgLvBs2pwdaN_ULewVRhtEJOldivhFprFWtwX1KOl9TJiY5XblZOiW9KKeoeD9NFJxvOWmvyHwJNvEunoJNlbzdPeHtu8El4ZBiWPJIBlmL8LDc1IqvqGbLb2aZMws5Ue1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4F2wpyn19V3pT4kbp4ML3LSWwMTvbOrGdZXxzSMpzuq5_1SXPHcRxT4cmQgJCMAzwynzUtVSMfSV_p0piFTElsBN46UyzduY8O-J2g0TV6L8UfYAf-YRhQSlWBbPZm8CBVnFb0-_O5pJYpG8wcsOsQvDygPKo_q5EfllFPqb7Tcq-pTcfDtbLfO6cWKhuEBvhZN6IpL2oIZxcKD5156sNOGVVn4-J9X5Rc-Opq4QvElVO2zjKLS3adZGh_AVJf5k7hhaZ5sRZU2JMO-4VW7klWQJAc2n7CNJF0IShr8UrmJmcg23W4PLSEwCorIuWu-2m90Spb_qrYasGy0ag2e1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_pseSP3OwS3dhnPN6BB7klRl0Z-GlPLuH12WiqdASz_YhlosgJ9Zd4L4xgK8yhSZXqbJt0ewefGVTkfEkB0I0L0nOJBq_yDWUKQC6V0jKxP4CD2mv3-Evmdlozyiik7NahnISlPo9d4ivK22vtANEV0WxppHvVGYJOTNCHiXepiXQADY2eX8l0k8sWYeS4vLykjekk6-cI2PK4KdPInJ6XPKZipOcAdfezOtDn7fVOkFOg4jkatMp92v1kZKXP85pRm3NCsnkFq9Bd1uXw4XmMGUnMJS23Id5UDBf9Iv17T75Ej0rwHEeG9Kss_a-x0F_XeE1Pgl4uh5dY2bJ0coA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rdg2SYvCJyHfjg8HXdr0OLl5fl865RCKD7K6P6kJp7AJ9n_vDjhz-tVuPeLahLl4r7f5fTJJSILJDGc0hldkpD10qEFO7TYKZC-gg8lLpP_Yuxoxc6VrYFMyNKJ-IDCMf3DtyNFlDhHcp3Lktq9qHPpP2uS0rHvZMKQ9DuI11TeyRkNG5clyiUMm_u4gzxhhn5EEthUb03hSY390OjsXrLAPcfo5B7y_0T3lDQm95J3T173Ep220zbInR7L3uP42RGMQQC6e24umFsx7JyrBwXEFkOzaX-L307wqCPewlhulv-zrWuHyhekSA_j8Cdv8kZLIcTDfdqN6CjgcbMlWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-cdtBJEE0SEei2-efi2SraqwWsuA1f6XxSw7NC192iSb_YHgkJsclvTgNQuNJqG5mCcocZLB51u7AfrTuMjb3zwevfIJnuTbQl314yDKSwC9FUcjwGz5A0t473j4OflIK1pb_xEaGeydvtOwDwWP8Gwhj2LZb5Z4ZJDfg7vgcknTbMjPiLlsCNgVNTdapvgrYSoZ4jKetc_BzlWSRWYkhp_TzZKNr_ickFQ3-udm45erRGz1MRNVGojamq11l5sG5EY_uXCHFjEeuqm3znWmR8DsbD45J6DrR-m0ynSHjfxL27hg43Fwl04EQ60Fe7FpJvodAVlJavImguPBrY0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFDMLXzh0Pf2v-5J021VT3fCB1qAYhQLSjC30HmXvPEYVYIPxYNc0WJjiU43l42xlSoHxyC1R6GPkIhI39N5oUx3ibu9nlUS_UC070I_uXCig88iEqrrvSQpDQE1V5NW_DQzAa87DMsPdCOdOI6O5KbOq4hFgq-uIrJCtT9cb1W6eyEhz_koNmchX9MIYWR920TarvJVsvYbeSpBXqh_rokWnzC8u-5PsMP4KhDSp_IJHfqpuzrOsXyYoR01vbWig62JMr701QY5aeSXBqiuDIW4Iej9h0FdfTQRTXzmbwxhexuAEoU6C1TofWR1frcPqfHfZopbJeGeayljUrFeGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYPMbS-hejp2P2tef14cBlhogKKh4EurB-th1mAc0KzDYO1gH0enJhqK8oBy2sxMTBVsGslmwnXfEeUZvNUiP47sk1zExdKFPR7QI9ukuuu1I1BOqwjLkeDQPeu-0EhJhfuKhXfKc9y0g7wh6pkiCUCqhO3Y7vY_bWiNMsifx2gDqwGe-5uu5HuKI6M8EBg7iIDVymfN3O17uD9hDp4MsWRCVDukLAw5LWzLy4XfNdvokD9jN8lABOElv-JTEjvQA4vygH4diDmHawMqpRFA6pZLG97ahtRMoi2Dy2EJn16hZCZGj-10YiNXP-41K1LQdm_DDl7mE-s6-oK6IVEWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbnR6CPUk0ffKrOcm7y9moPTLqPn0bPeXmYUSHOkHPlicDQ3MThWvHYv5hfqp81RvaQT9qWFCLZjcqWd7wu7ICaXC74bYJbMs4kpEwnPZa3ElKT3BaweBEpyVKOCetA0G-ZxK_JeGOZhrMBZsYOy5Rql23sZVI1AnO3ITj_qeb1cgEUdECWOmMzeNHRBrXtqBRy78AHNfA8a_fb4frr9yhNNE8w-BEom4-n35pP-xeOiwUDayPUW1mW2rWIBYdftM542Hf2l3jvYrG3Q-Y7z50pTRZ6rBAT1tdrMjyBKXF3mgr3tBWkwQFxvnUgpX5ZkzpzWoqNivkFw3tIkjWNcBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcWYrD8MRCeoi4m6ccRf8t5Xakr0eArHsYfSBbWfaE8MQEKczqKLvBWZVjLemyjYwp6BMY1QPnxsy55Hc20tLuErDEalidDOmm-O2ouMfku8t8ybS3d5GSH-S5APTysKN0ygh7AIa8hfcuKu9vDmqU4sPRm06dzjRxeyfRD7ge5xYaYReK7Mi1DHcbDGYwBPDew4a2JNnu_0eWJCKHyzYZ7Bzirn1CAQxLfZibEK6FFpwKJbc_d6nw4SMffEZGWjEf89sukcv3f_6RcJxWRnqxbeB6UQoeFFqgmNBAtoZ2HAiCLx4F27vyQyfdaUc1VlHGysC2jhJxEfFzMcrK7-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pP9aZ3uG6OvdEKmtShydbLXR0xjj28pX4MfCt33Cc8TIOgvPtpSFZVFZT3YIn4043_QCLEgGUIXo1-DDwVHRdXgZBe2umSb4-c-TeirYwxYNLxNNtOblcIzZW-xh0HBn4lpwUVULc65iXbcSdGQ6_6V1c2uOBgp5Jm6AvVjlGkHWdOHYNFq35YrBRCUJrqDN-d4GOCHO3v6-XgORWaKBoL-AC6w-GkcJbQjMjzFwMh_KnoJqFU8rruznnQqEtl8uslZ8VcwqAzNy6HIOWq6qxQFiGof9hqdgDN_6liPmzmlIJ8ZZnoiYO22Q6PrSyFfsWDUeaxhwF7jG8Zjo35jPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjBJFnM9979tshvdoGOJrfI_vscsHChL7c9Hp8RtAmGyD-2p5qm9YgPKwwb8STxKQp8j30vECKvoKRsiGbD8ZWLxUqfX24zFbLVv275wKyHWYl0oZN-1wheJ0vGnDt9Gbr8l2XWIlcYf7_FSS0XThF8W80gvPpCef6J7WeZTRmQQmSLZci0D58eTFGgZkrHWODj0uD4nueHiHbsPZs1Agwh0Hpk40eqMA857dh8f27N93HM2q_eN180u6pcGjAqOllWn2U3K6WF8OVqqMqFbPHOWSmLryHNEmb7uJP1PY2jQq1U6n2Zw91ZkS_OaU1ovwzFT5rlZJwIJxUSpmWVJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXsobAH8m0vuFHG80nARImY5bdr7rUeUqTV009zZV_BAKn2Y0w9M6fOpAH_ZNwQR4sieWyN5y_eSvlMqNYMrM9KikJ3Aa33mFLVMO5V23pV7sE6TTEmha1hedP3_LwSeIKwpORwGOHwDmJ6ZJZt6wsYWb0x0TLiB_tAaIqlO852LMTd3FbtjtCAYej2LRyBnk5uA8O97Mp874Icx7YzzWJfSFDbPNJWbJtpj7Cjj7IRu10-MuHjoie3l3jm4B_zxxJFrn-bvXauhNv0EKVGcjizYHMUCXwTzYiUW7_9fHceXWwLoDG0uLktTrVagta6NWk4k_4tt3pKpPy8bb1vP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkXMAFYtmteE0RD64SuaXQ1dRJ9frmm5h0SHW3OIJ38m_F_GgHQyRkFAnhXPIpIDtcYOMbvgSyVXSml-8Q0PI6LrxWuKauPDtfp5awzmVrt9AsyvbCgo4aoq9E_1vPT4J3A8NnqLM8eI6E9pL1yrT7LUHlClcZpSKKIySvPpzMyU1FUEtwmF5RBNhsLoc0377p56AYnKvO-gzqHG21BWTw7z3jP_Bs-6E59omA4okKm8SDm2cCMuwHJHFcJViTJVOVXXEl15USXOHCnPpldTrDXgOnVEN_Yv7-yzHrQcJJW5FvBO5FazheVPUo2T4-XVjiwF8NfsNqd3hFD4X350tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkjfu534nINNbhat9KMrP_lbFMNz6rTPKW8sIRvBKFWmEP5A7WsnIJK6vI-UWFPTy_PK06i6bTkUVnz-D-FqZnGdaXtMfpqPwQ869IXoz4KfJU-_xAftDY_x3hZp-PKq3EAko8eqYWwZoDoDB6Sav0QLCtSuAzfWCGQs5AeqP0JSX52bNSCrGq5roP5lCJjTBkmc13oXf1NWAxV4YcPVyUDEFPcgejjYbE9StLHdRcwFOgoLTbG23Zhckeo9mY7KF6uecTDHJ5QvvMX_MUdbz7kIk7PFCPiHmVKxhwmG_Wu2sejg0oLAl29oUWpjxuDOiVthIduMASbSSm5NyruoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3PCQl-vsZeJOcpxotaS0jbLHCiHytBfNEtFOcmkRgnbC4ic1pQ8bNjBVeegGuc_p8Jkmj3njX_CCC83rgaVOa0EX0uZ8Tqncm28RSvC5qVJMiqKPbnQ55nfK-ISvACAWIv4C2R_ePowyyC7kXwkKQw_hZeiKic-5Y-p5Xrgbsz6lcoNgYGaTmc3XmNJ3vsQ8QFwnlqHspeM7x6Im4vjIm64JRoIY6iC_3CSQioQ-N59ECHKS6h4Chzvbmhw5Fq4FVZ4Xwxwr17HjBkNSceEU3GaczfrECyaHkMd7LnB50CmeDjGuwu2DLknUN9eyY82kzSzdPSXimXjZVBBb4nj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3WCJAUwoIftRmlgQDAcGx-uJMbCOevDjKrgfgGbd7RRYcCvxOnmWoIM_Y2H_VZ893DB5oSGT0NhMr3LS1YOfk9TQScNr6ZvSReY6o9lawWDEHJA2Qkmq8xU_wvTChq6Q2cnByulrcXAXSeunnfzk3EI4TMqrBWnMqhUCvhXu3WLWPzByhncOAjkYBUh01ITEi7Nc3f68NWb9RZ-521yQeyvSU6hvlI2PKamFiAk8QRImUfYtND0oguYVltT-H_vdnftAAoG9Qx7aDzun7OrR3DUaXTQWYlcp7uwmxCyf7jQFYKaSKD7iucUzF9uOM4OoPmz1_wahw1udd9AYb39LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=RZOdMp5azqzGWLYJJA4Tg9_6eSrpG65GJTHXVuFm0tFct8A1E_xxLT-vHQcp0oFVZce6zuj11tTRRbE3bfsF5PZo3aFB2bsYloTYKdX-nrB8X6tF4Vya5oXTgdkc6JBuRbhmgtbpyVPTm1C3HKeqjSjPnePZj_1y1R2fgZvA--hOMZ6QdM7ldD3_Yc761eVbCLTFSu9NKIkQHBcmjjDJ6YaroM-0s7hkUdunZYB8nCzAfdr1Mv5bI2nJomJ6GXSaEr5ghL9FbOs4INEFkstR75yFKZ6KB4XbsIElpEFgJXy4moO9jh9z-BM6Z4Fnj102EWENfXsQhYUCub3w3lwGCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=RZOdMp5azqzGWLYJJA4Tg9_6eSrpG65GJTHXVuFm0tFct8A1E_xxLT-vHQcp0oFVZce6zuj11tTRRbE3bfsF5PZo3aFB2bsYloTYKdX-nrB8X6tF4Vya5oXTgdkc6JBuRbhmgtbpyVPTm1C3HKeqjSjPnePZj_1y1R2fgZvA--hOMZ6QdM7ldD3_Yc761eVbCLTFSu9NKIkQHBcmjjDJ6YaroM-0s7hkUdunZYB8nCzAfdr1Mv5bI2nJomJ6GXSaEr5ghL9FbOs4INEFkstR75yFKZ6KB4XbsIElpEFgJXy4moO9jh9z-BM6Z4Fnj102EWENfXsQhYUCub3w3lwGCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3uPS5zqpkPPFiNwY3qWh_PWXUC96HoFezsHAQNTRpO5kYi8R1r9NI4Q09gBzhGeMIbnS1qm0gihnGGHmSOCYVX1l15aW8Wt6aeyOc3DrfTtwiCfUEyKFxPXsTP14FveWtK47V2Jy3YEZ8hFMBhpANqtgNOkZXy3xUtwatMZwKoKNDQ8n3wrLdPrf8w8MS25q8kohYI9gdO54sRoumxF5CeQplaGjQcH30zr8RGw_9N8qzlolSvE5bE6UUa5YvP9ycufUYXQuJYMXFcJnyrIiNMS83JoQMWA1BsivLsopV4tsfPoO_lKpd_cXGRt8r-aJUUt4xwvUgoGjSyvp_Q08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQwgTauyhX00B4UGs5PSWj6YS3w3Thhvqopum_NyVb-eWJAU48zNNvRunxF2L2D01EhtltC66Ta-MyuP84Nn6kwfEx0hhM1bZ1bHwe6nR0TN4ySA6df3nJ_22qd9eLdbAxcz3mj_54QP0oZanyyFKtY3RKJDij0QdvBC9UaAKtQXKknst5JnZhqri5AnkPjGozK_Nug7tVta9yfpdhyEiN2AoLaqhffNVpkAxVLxcjbzKha4rNrFH_LVAlh4Ddq68DMN8NuylNOwIFSP7z9WfinnuI0zG2KhzsC1FgTBcaNfJwS9yur85h5r9bEG93Rq9BqnSXfA1EeVo1nyQPSfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO1VDG9GTkpLGU0sJPLg1BsFxGYa11Qi7iDvapJJ4E2aVR4t3W4wScFmz4utxOhOu14zj56OVuV2r7K-0EhILxw7-zwXUc0WBS1sh_y-IlSguoVv2GKWaprG7v_E6vvKv0UK7cPRuiRGxG-tZdhokNT_I4LEhmBiPn3CF_InEgjyEEDPZTJfvNddT_if_3cV812u_UsJj-GRR5P9VSMs3ckgiHOXcIQEhTW4iwQ2GoMQUh1UhU7ZT2YVm3lhM8_bDYRxII_BVVPbCpebA5FZpgbtXjRhyKmo1W7J8fWMBvkCRRCWAphwk6iIIsoZVReZqySpN_zAmh7e3frGovt-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=LUKPYzj1artgPcEdZq3582qwyP0kg3lYCiTLGw5xxuqnXomMwU2s-IKkkEKRgnw_sDcFxH7w2xHbzxAs6DFLc0y5zzM-UW7GDCT_e1Q6XxGqze2EDVyZ1Hr7woN5j7uRO3Bu3Z7oNWajCZFzRvRL5AUCmAvx7eSAroMTdIEkam9ysBBT2nM41s5WBMZAEc7bmfjLs_T_Q3IFns9byGepUiflqOtrYu9aQC1lE6rGbiqptX4XNwOJnYluJUHJFAvif-vtZzgTlm5gCaXN8Z4xConW_sQgsG9Ju8hT7-gRvCaFW9z1uu3iYe1oOGSUFY3DcUHnkem3h_LNNQ9Bm5_t4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=LUKPYzj1artgPcEdZq3582qwyP0kg3lYCiTLGw5xxuqnXomMwU2s-IKkkEKRgnw_sDcFxH7w2xHbzxAs6DFLc0y5zzM-UW7GDCT_e1Q6XxGqze2EDVyZ1Hr7woN5j7uRO3Bu3Z7oNWajCZFzRvRL5AUCmAvx7eSAroMTdIEkam9ysBBT2nM41s5WBMZAEc7bmfjLs_T_Q3IFns9byGepUiflqOtrYu9aQC1lE6rGbiqptX4XNwOJnYluJUHJFAvif-vtZzgTlm5gCaXN8Z4xConW_sQgsG9Ju8hT7-gRvCaFW9z1uu3iYe1oOGSUFY3DcUHnkem3h_LNNQ9Bm5_t4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKocpaxI-f7dwEy4ZeTM1w0qiwjTKMWDOL4if1401SjyqYMAOjL9It1onmwwhriod6AEg9xDZ1rY4kuN7SpRZm1oYJunkk4yCKa-qYTK7I1MavahyW3pSZ8TzAqGn2FstSdXwpEzHzUZXlpTGgGXPLgeeGgb5H80Vhuj4Qps3JOK8aOpKU8NGY2HxKb6n0z59zHEGjUeDXQN54SWpmLFa2LL4DcEHujDya9C3Cn8-CVUjeG1liiHNKcQXrfUmvqOxPV6NQ8lk5t2p4da9Iv-R6ELRxsc7E68V8BzC5qftXrAt8eoK1M5fg5YIJyN3g_Z8IGIKgV_roo3VOpPqAP_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=ZKkJ5Qvw9T-RKWiUxBvq5AiQjmZ6DMubGCu90V8J8T8SClczJn8-BuAt_HhkgtXsxPFaLUugqE7j_TQQzK9c8dOe7J2ezJlAvH5LmphpWq4TPapJukgcCJrB-rxtBU_3jWcPmllsY3zgTiorAuw0WFeenwTnJY32kTtA8jT-rO9KcL1GMZxmpDZnWN9XYMSS1BkG0WKoVq-bIEnYEnW_Ovw4FlC314BcfUxMaqNMFYDzH1JV5YA3zVfKGtnxkRUJFTtyydQg5W3q0TJ8K1bcaRjZyuFGFU8xsUTrw4yxYi1xlXKI9S_VtPU7ewTykGRymgKt6bjklom3MQOKSTiIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=ZKkJ5Qvw9T-RKWiUxBvq5AiQjmZ6DMubGCu90V8J8T8SClczJn8-BuAt_HhkgtXsxPFaLUugqE7j_TQQzK9c8dOe7J2ezJlAvH5LmphpWq4TPapJukgcCJrB-rxtBU_3jWcPmllsY3zgTiorAuw0WFeenwTnJY32kTtA8jT-rO9KcL1GMZxmpDZnWN9XYMSS1BkG0WKoVq-bIEnYEnW_Ovw4FlC314BcfUxMaqNMFYDzH1JV5YA3zVfKGtnxkRUJFTtyydQg5W3q0TJ8K1bcaRjZyuFGFU8xsUTrw4yxYi1xlXKI9S_VtPU7ewTykGRymgKt6bjklom3MQOKSTiIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q99kZl4d9JgW4-u62QjdoVfatMIFGwmiu1dj46PH6VEamte501OUIlqO3AiuegmEjVO-v8voYb1z7RUfSL-0ZjGn2C87DsCNxaG3peSo6y4QdN3OWQZvgG9WvqTYTHsZuVCTz-Pm7O3sab0VbISrIXLOc0pOwwgJAU9SoFsWpcg7Or11WmPZWYabNl2NcxInNwGujdAGpUgbsQA32aFBHKVWZz2DPn1NPPJ2U0rEEn8Hwy8cwuWSOj5pCxuRWMlW8egX5uJJUNNVVT8wFn_ZEL75MVhMPCf3AGPOpxF-LpnQEsWkAeNjQ0_W4bovfd3AkoUwY9mWN82HA8tqlYnrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jndpi4czBE41IOb5d2xUcDmiBMKpXTGsJ9IhGC-HkOtXaolSytDm7mI8dsjFHdgfNyoQdb1z4yRAXjw4ttTfOesiOeFSYLCqVinyFkbLKylNboKFc6Kcnq8-VAnkRoWSfrB1qcWBvMP2X5Hg25IQXI5gAbkOGZ9WYbRfA5uWW43o5Udw10SaS00uCpZl5C-imbmOx6ojR1BoaPKrCVhxbjRO_CCai-8fqaM81dXvnPvVHEaCZfzLBVhpDFHpvA0KymfJh2ysZGEykBS6D-852oZzOLvoMneOmxnu2JqjcIizCth12cQUAjR5zpmrXqiO7BRVxmY9kaIepwkP9I92jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXTUcc-f-spn8zl4fG48pbGxsEufvRn1FlgpfBbl3Z4tMMLLoj9o8JspYx-dt4JIfnTxkf78_2yL0_GlASg6GbMtftEbBcXiLLWTBKGrW8poMON8m-24M72Jv7Ew1ImopOGJqETzQVQqRs5ar4NSXEwPj5cQrlgX_4eBJFmdJSS5GAMs6-0ax7hP39KAlilBsxOG5f8tNxY_esTSz7BeRIJmaXuVDjHkLWiE6hNl2259Z4JA9icGyXRZemiit0XVr687sCnyjiHC-AkB5lHjZRApBjUL8oQLxF1Yw6r0rhjKhLYwvjEO7vYo9WsBJHrKKIpQcQi_QqueubUr1Q623A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wy1DE620_aCVWAPY4woU9d4twQZW9nNmqlWktjmIr9kqmgEH6tsTXr7rqHJK7VjHEX4-ZACVYbGJ1i8kTAd2bL-BYwzr65_4YfocIGxXb0bDq1n3xswkJuYHI9HdDdW5SXcADFThWAWNeI2DkifyRqOZR8YmfrXFZE4cr86ES0iXBZm1dF1MhubNpNa79gPXF2abg-50IXWNAFaPeKCYlhMPDEJV7N-VvR533Sppfm-MDfY_en7TPsuCybb0t7aatTJA6V1XCJe-MFFvHbMsBHVvAzkEqpOn_2b-T-91ddiRc87SgbNQKg1Y-aJm-gc8cU3nQfLxeZXtrhV5EYKlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XirRmdR3phLq9fNs-7CRLmBo1Fq9mBe783zvSSQvDKe7WsBRX1n7mugj9PntX_9wg-d8PgvYyBMTnLn55BhzgzrpQkmCZxbZBpYgHPl0xf5modm6r_5UbcRy3ewbTqxhPI7mnXddHfUbrJLczd8cY1kQMEEDr65Th2YrcDl_pNHkHvfQ5qTWVhNJM2Zs1cNPpaLOZDuYUcZckFKf65TbaRCGlDYza06QPkryAF_hXTLu7H-lz68slFU9MYl-2lheBfQJQ3yqVISUfVFGHFq0_tu_K0XS0FlVyt4KZ6nh75HASdKdtQ0Xq5__ZK5V8-6_oyTWLrdQuYwHDvTyA_H6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSew3DshI9s-_UkSlkvs9xSKYWEal0LsV20Rn7Us9zSIcfkmH1msHr_q2l2_HXI4F6TqfHKNLXbYcE82JdDUv25ZCXdJ-iwb7HGZsQ4GTlRwdK_mQxklT3z18ad0MEEmuglYfocy9_hznedX7ocOwURBtDxrsw3bRLF-RsKIFoEm_n2Xq-daEb6eGHQJE5FvydlB9mieuOokjin0V-M2E_510mlk6YkbMWw4J505BGZDLGhKUiwvIfh418ODWxvjdX7G7Xroi9AzuI9qAN-1XKe1APqUTZ1J1j0fWRpMkiuxwKHRHBhAAR7NKVZNUBQkH-inGQCNxBHXhKaGFZbZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5MINNBmaJ5istU9RTeFpRcHgQeFJrnqgqUPCmHuKwHIe0pLe-u2lhRmwp-ky1RwM5ljTxzu_HT09uPEAbjYwnMgLV6ShSGGmH31MH0z-InhEyS_OJ1IGDC7vr3N0Hx1YOgfZ4xia80sR8UigByfNXEQIjmFLV_pIOEbyZT2_Kez721rTUs9e6pdqYkpMFiwyPoXY7UDAvHOXzXsrfImt70MR9pAg25qdv6BfC9IJduIJHAI8Tbn1JcmfOtMQR29e1oxzJoPYG5djNZEpPCnp-xoGOyGcq0kJYtQOjVr5jBXX4V7BYCZ6rgdkZjzXYV2jL_6iyMhuhbnSRin2MPdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJZHmhI_vyjdjIgztAu23J57WFiFJNizoGTy4uLrs-yuuXk2wejSbraZJPy_GjAXjlQiqt9TOEFHEP8RYr40etQA6DRK0rbPp-jzh4I4ExHoBkGXKqQrtsO24TeYv9wpAhm8crv4HNW6Nrg4gbzf3EhnC2I-AMYx6TVaxTdRzhLYlNLcYQA2H1x-szUbggiAE5DmfG7o9APhhbvJ2986maAekejDBhk-MSXxcgXMdql0dUl--BecLRx1xZwoAhvwsFlgt5P7cqR81OCP9KTi_w3E6lh-79RPFhCTgjAhD7CUCvY9iqSoyEjUV5zWd7FJ-vtbeq_XVkSPCKb6Co5plw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=XluPg-67M2BW-CK6pak4qvWKs7zwZA4prodPletjgWlPbhREhnAOuMX9T5Sz9CY8hOiVx9G4RlP17PodqeuALmYGBxJmdiVHmRKXog39qG8S2kDqVquZaFAvqzqTvTmM1XN5aePP_uvgaQ5ThXwcY5ZyawGbbb7RW9gH4xxfmfz67gDmtysC4TLdw17QOlwTnmViPJL1JMAo7i8Rx7MBD-xkDfezkr3EXs5gRevXHOKx5I91JyPAXRl3Cp84yQzYnCgUZ0ZYdnlqWAN64oC7DtiSnys1rGeyhYbThdFJ_l5uKiHxoMw9cmRIHLwabeJG9rQgZ3IbXhx9co6ghw-npV3mHQlBHjwzKUFcGvy6gnPBKK17t8mBmLuvmWxsLpsAhUZv7OQlozzd0QaRx3bOZqWgA4SzSkp_STDbIcb2XG9pNKmJr82GsGJ3HioXp6KHONPOVPWx9VQAolnpAQt0yWAlokuVJ8yIb6DbvtMfnwGYmy1zRcgF2n4fuWZa_FM8qtM9YLHrEty-syRITrgwkvftMSuCqVGKZLs1-6GO2JZSBnXF8JRPvyDPT_Ff6c1xfulURdswbSJCejSv4Xn2w6hcgV8MGEv0thekPDaAJ1R1_TJp43LG1rYg1p1qF-m2jVjuyoTtlwQAaC7jRHRtz_iUyekEbvjR_JSBVOEEMvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=XluPg-67M2BW-CK6pak4qvWKs7zwZA4prodPletjgWlPbhREhnAOuMX9T5Sz9CY8hOiVx9G4RlP17PodqeuALmYGBxJmdiVHmRKXog39qG8S2kDqVquZaFAvqzqTvTmM1XN5aePP_uvgaQ5ThXwcY5ZyawGbbb7RW9gH4xxfmfz67gDmtysC4TLdw17QOlwTnmViPJL1JMAo7i8Rx7MBD-xkDfezkr3EXs5gRevXHOKx5I91JyPAXRl3Cp84yQzYnCgUZ0ZYdnlqWAN64oC7DtiSnys1rGeyhYbThdFJ_l5uKiHxoMw9cmRIHLwabeJG9rQgZ3IbXhx9co6ghw-npV3mHQlBHjwzKUFcGvy6gnPBKK17t8mBmLuvmWxsLpsAhUZv7OQlozzd0QaRx3bOZqWgA4SzSkp_STDbIcb2XG9pNKmJr82GsGJ3HioXp6KHONPOVPWx9VQAolnpAQt0yWAlokuVJ8yIb6DbvtMfnwGYmy1zRcgF2n4fuWZa_FM8qtM9YLHrEty-syRITrgwkvftMSuCqVGKZLs1-6GO2JZSBnXF8JRPvyDPT_Ff6c1xfulURdswbSJCejSv4Xn2w6hcgV8MGEv0thekPDaAJ1R1_TJp43LG1rYg1p1qF-m2jVjuyoTtlwQAaC7jRHRtz_iUyekEbvjR_JSBVOEEMvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqzYrtArIWwl4ix4Q4Cjr-Y3y4EWrPkLB0-7pE0op97bWdIDK9aywRQHRTFmfkSVo9dtpb8KZnCBKYewG48vvQ01f9XX8yNh_K2YfXjPbL1eOyfOmyyBnBY6eS5ujf9f7hxPysp71jIx_qFOw-OSl67OjWcgZlq_leVqzW6_6HA7BlNAXIu0tiD1D4weFLpWR9EErr2hlEwzhypB4kuNkDwFZQso0s1-1BjhuH9mOXwwSrNsrF5F4ItKlV0FiI3gXVPMJBJ-b_uGbUNDbtkDd4CHNFPSWP7nIGFCced_MA75-BJkTXc6Bf2yULTNbLUi2kepYBzruhjkyaN84h8qgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjYgDPv3iL3awxjnbNdEvfu3-E6bf9bos00-0oEhwKQAqtT276qQzCwWg3k2ZWT4SuDQ1u_b4Qdhd5jeNF5rMAFJCbUu9OBBlJ6tQj5XiUkZ-58GBjLDKbObWVBmA9nNvUTb2ugF61dX8gigfcnuHPoJ9stsQgJH9WOdrtjJdBuBab8lE0TL7gM0f87JwIBg51uCU9HNvKi9HifjtvCLm0_7nYbaVuixjg1PRZu2u_qY2vKAuclQC7qLDtLI77yhDre4enqrxCXHrx0j8ZOQz4jivfK_EjSiHEZMyPRl6skUH8S7IxDfhlGv0LGL9Kdlwll8JYX9Nmm_6RPaw6AD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7o8OBXOuAu1frQK_z1XOOaKgiY4JFUkWlZtGupbU2zmMt-RRKJrRYynro1xxcB48W_QNIPee5j5c66XmvLNstXoXxWlfJpjqjUqzcEIK1CyABps0byS_58fT081XoMsxCM_h7h7aVux5caQg1TEoqVGluxHxjC2JVp2N0ayLoAOPUxfJmDPMA1BUzv1QTcyjQi1M1_gji0TriGs9Fa6I5thUJ_g0AWoDg5JHMc5RZyDc5DXYwVQW-OEqk5oPlyM3_JEmtVBeLB80RiTEnY9W4S_da-lQUR3FNbCCamDK3mHa2xdOYY_3NwFOzNlqI9XrXEYB6xJgGBVA3zd7LSBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pAkzw5mWHNS3iEPd7wffXiU7KcGwKoMffG6i1YBTf7QBUgLRZ3cpYM3nyI_pPhU1AhvDrwQm57HKxGHIU2g8pBHmhSy2uUbWDyPXdj-TprR5DxRMCGAmgVm7dqQDaxVMcZav1IrDQTn_gAebmeqWBOHAOXVTa533C05X9PdijbRW4Moli_Fi4l6A_lgEBBBX_mtQy1zvssDmqMtESM0o6TPoi8VepezDDuLeJr5yUhLiWMZ8EMvxxiHKVZwEL3dicBOpP0gs1H5NyFFWUy7Txp5upgVdgMSfI9RRgafiQLtU90QJaYTOSdHTKELdFRvR1iBPoIwovDtEqiLmM_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZSkaS2U0-GT5ZY0YsAxU93hvALZU70q6ZOZSA-dNIKkq8pGLrDuf4sNFjEPkYb8yDdF3XskRgwa7lpZybSK-5wP2A8jun5IihkYg67BUXZ32Jmd-1CAaBz3MrL64GMxmPR0y10TGDwiLThGJrtVPiVpXDOnQuOr86qIK5SLet4qzyJL1vOGHExok6uz3Ex0axZuj5IfpeU5FIqL_HWCg-rWWZ_b39txpMck-rDxAWvRnTJRMg0MKZNf2cuwF1_xBJ_dlKgnfGfQagzzafPWqcm4Km_F88cKrNw1ybCwNZfnhnVHalXmn4FD56167zhBIJKVqGQ2oglLx7HZBXo_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUlYLIaebiDtknVK0D2p-8vNJIOUBjXTmRX5HeWabNDu7BYwwhH0Ce7mvbQHJk4QHF35kOH8VP_2ccqJphE7olrvUt5i6mzTvdktPoCaw3W56OYGMsVx9dBWHmRhVf0z2DVyb4TKcZrNZPzoZ2cM4SRaMI7x66s4LYgBpKHlk5m8i4WuXL-0JGgAzQvhU_UEL4NeQC_t05Om0Opf_F4wUeDAvu5c3j4D6oL6xrhkM8YPV-vdN0BgE4WfsNN4fxnCtyzo80CJP-LCoj15NHNrW86WgRe6T1UGiQgAOqAVlDEVWYRxvrtH0rUugRwasRv7WCjPTYKl4YXS7vkjDqip_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=JoQ1BrmbRDp-c3GrKJOBJGAbECDvtOdVjd_NIZ3sEjhCr3Y-Ps0EghRN4PlGGqZcFKH5wtV3K6wOUPopAkaJaAmbv9itShVWSk98ZBYvuqs4qQocjdbvZny4dn1i81i7dQarQZJdr-b1Xr19Bxk2COz3rmoxsGzEzH_2sUrbFTuYK-aXpo9duFESSUM8uXT4O2QVmXy1MzWmT4ZEp6muaDDhyVlPWdSmuKKDA3Zd0GLGQYq0CRK87hvl2yJoScknDHZvPY-2mmK2ZXGQtiqECyxAolK9jVNmEiujSvqP5366wmTHfVChNKh5WejaNuB_5uETeKXHdY3Aj1kXjDcU2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=JoQ1BrmbRDp-c3GrKJOBJGAbECDvtOdVjd_NIZ3sEjhCr3Y-Ps0EghRN4PlGGqZcFKH5wtV3K6wOUPopAkaJaAmbv9itShVWSk98ZBYvuqs4qQocjdbvZny4dn1i81i7dQarQZJdr-b1Xr19Bxk2COz3rmoxsGzEzH_2sUrbFTuYK-aXpo9duFESSUM8uXT4O2QVmXy1MzWmT4ZEp6muaDDhyVlPWdSmuKKDA3Zd0GLGQYq0CRK87hvl2yJoScknDHZvPY-2mmK2ZXGQtiqECyxAolK9jVNmEiujSvqP5366wmTHfVChNKh5WejaNuB_5uETeKXHdY3Aj1kXjDcU2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzJxX0jMa2vBo_5YtoC6FH8bqLFlG_3iECSapuCgbyfnsLoA2eNbY8KW4x9thAdSS9ebQgsYYwlRrRdRJ-tzop4O9MSnbXDgKSd3sO7_qZ2WVuxPtHvPF683wcZ8D84qD6l1GaGIXvfccJk5AfYMuDpHHZOhkzNIsRkq0PlpQLBtXmwbmRx8XTpVaErma_TE61DtULTOMNgEWsgE64cYZxNs0DjIt6DVt3ElfXQydOuw1FvEIoePb4J-9ekPC0Dy_RE6cQnG5xyXkg1qcs62A3oyWXdfM77RmM2aSFMgBK1h12-rXpwHHwAJacmRgKRmU8St0y4NflXY4qg1y6E23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGOwVqOPkh7PUCpt0o3IfSu8j1fSg0lhb6D1LfLEKun_pzIHK4Bxv7Z0Nz_ypiduX9-VvViHMvAeXcxM44AFjZXAzzpYqGeuhekINdIyrTXWRxGRSHwxh3MHm3KoFrvpyuSl-TqCy_dxKBVEqAkg3MK_BFoR0ZocZDdnnQSmesPUlqGKbQQOQZSONJ-G7JcGlrLh-i89zKOYtgpsHBjwp_POp-Wn8d-PNzOoAetI28qzB5HOh8xqiK-L5Taa6Zk3ohyNEoWmftjjc8jUgITpaeFtTB3RksatDBCxJCBBKHxFSabOEw4zuXNfwMY1aATJiikpeR_c31A6NjDIxr6IyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgqY9nQFElSw-gtlT8DmS56V9smhQP__pyF63L_idvZht-LoUjFP7TAFn-yTWg3ffGmKEgv1jFoI6N7ikRqIjlZwv872R5sg4Y54z78LnangbHJ7BBh_AdEMvLE0f0oxa05VAgMJfMpbzRxvuLysFL2TsU2tcf0BDLxzRSFOROlJDU2MDprWXV48UjfWVzgYp83fsu5-PlgmOEKOIZcdx70VCBC3_Xu9mjXuS69jCbXbdItRuYgKpAKTvP_sK-B84jKfmoifQc92JX_eiiGJpJHhC41NqDWOvoYK1iIBNAIzc8uOuUB9kLCQl8QoVjXeiuz-sr3BjogxJHhj4-z-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dosu2JkfzNNZ9bZP1xyrR6o9PUjR9KxpEwuV8WAfs4m4724ffcwqN4pc0NqD4TMhg-lyV__h1P0p39b7ZyW_81xC5V0z0ncdmRT0BFgg5REDzfOOnboLoUX0wLAG41si624Dc-UuCHP8Z-i2ORjnPDyOcgLdRGCHX-g7SiqhV-uuEYqr0W3GF8HPVytAVU9IXqndws6TBWJSDbrfKreqS79RDX76wTKbtApANr5SyhhvJGyws3LG2U13Uiq210FINOO0ARiq3VplJgkH_30244r7vQtcTOUEVgZWS17U77KRbC2kR99vCFlXgFg3K4Zhcjc7JkL4ZKszGEmF5wJv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZmovTvnldwAB1CSALQvavoqjSgsgU9VVsNRvylY27XLODWtyV8p71DjGYTkRhVMIXsNrf0mhU5LxbXb9uCNXOsO-LRN5ZOC-INIG2NyzdL3rpDGj1usXekJuqr4xAGifqqpnJsyBJVvzLasp6SVucozTK3dlWC_D0ONcsssVqZPv6DaOZECwZG-2UeNrw5Hrsp_ECIp7c0fkTQuRjZnBNeVW5dilUGEMWd1EnfVVOX1P34BfEJRGfp4d4Hc6nN39JrQXFk7ILfw_eyEm1UVQ5VqOtQSkMxkP2Gym68xAj3vmNlS1JqjBgdLjqX0vV6gzUGWt75kb8S79WygDE-_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-wOVCtV9rqBsOjxgyOQxvzHNTqvVNEQ1ux3HuaSXR2HTZNNsihuJhzTtSLyi3fC8BHA_L4seXaD4GixccNnULAY9-hr7g-aNYuYpAA9d9Gpc5afmlQzfGIWvACcV2iDLSqz7EALxjXi9d1DNVK6PO1Ash6pjyImZZBvJDNxUBu-mfCvWmMvFDBFtqx_ihK23DWk7kll8fXjrHgOPsQdb74XHjLnj41NwpOUtQV1ZFM0r_HOVjkN_8RnmaafNtXX7Uo9FL47TDjwL35jGjwD6SQ9PDklVBJkLFcoAlxJSRE7EmRfNyhFav3SH2t3JMYkLSteeG_oU4szTWQw-0ub0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhwL_uuqHcNS_uWu2J2N2uQTJ235XwttFOHSiSUHm_A_TIkdLs4tAnZlIp578kaLdA1P1LDRlX98KV7GAiRJ1YACs7_gpdZsL9dzsSMDYN62IN2KGV5RqneXbokgIzZNGFull2gALZ58uu-iH0ZaACirH7W1QMb0GwDy2cYdL5IMM-5Fn1IA5WiUnb2K3mx3QpgaymymC84IlpE9riQh4i-4dattKwTZmPx45ncPppxjtxiLiq6dbqs147yMWpRH4_fjAjregtPgPWjuKd8zVLkH7p1eO6r88ipsu3KGsWrDDjmyAdk3Eh5JOKElpEl1ZmKFm6KJVaIwQHe359iS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h57wteBm4kWjrYiwVCJ_PFT73datsM6M0Wj06t2nvlYSDgvndaO4NKIZXk9Rimw6AbVkWBM1eTQauXOIeOIOiAPSINsF0QWMkiv7jTHFdkgNZSxKk4zSoEGiuKSRoCUGf9vJ48h3Ks732w1LKzACkAl5sUpKKoRCzw6GTos4WV_do1mk8DRJRN-1y32wqeDKxTmJCr65-uZl2ldH6qH4G3h7-uWyiymjjbw4RceQYKsb5kqYvgNFFENjfV760qHXDH3ioJ9pK9uaUByARvIkOygSp26VLm_PC5VYede5Cfy0zVA7A8V0xKWdr3qJMMi3_hlWtwTHxXjjdybO7DUsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msxYetyncp95ZM-q-vMmo4R3kFmKgVYu52_Ic_GiY7Ym4slaox-cM0r8no4hc3-9YTIcBVyfyq54EJTFhEEuJ9VvFrSjs8A-Cr2MpniuTnnQl4YAynoxmCJo8NHSdFWGfYjGigMP6kNrqdZrfOH4C5II1adhnlrw-Ifq1WB9fjG3R-ORQfeh1e0zUahSpFtG0fxTfC4iNZxsAzr0pxVk7DoBPgOYruqqz-n4qeCCh2OQaoD0rpOKttiIwl_Ijkz-MNJjvWgBGV2p4YmD9JLPl1fUw4qiER3rUHtggnTwi69q3R1PDIQW2kGANxGVFQSBL84wecWLFeACKlIBXWS5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdRZG-YC6iLpLeI9nZIv7Fb0_yY8XIts6Aij5mYbiUG0k0WDoiTesFBQyiNHTCDF-rd9LHaDQvaVI7MEklzY2MKSj-LPPlmgTeDZ4fwi6oz-f4xEMaYLk4UUNQN-Bf72cqxR5FF05-4dlpCNpkiN3cbSFI4oz4otIAbvF0bbjgO7V9zo6wiBCUKGbcOJ-7uWFr76dmSYgaBVNPwRljXc7OeqAQ0rzuCX1AiEhY3rCMBsCWdrZCc7Y1K5R6G7RquJQaeipkrWgpxqMUKBw7rSJgFhMT4Qbc28Kj4d1Z5M4h7Qsae8XhcFv-sygaESVh4JSwIzP5Vx9eBOC6LUWmRPRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=A-SHo88VgfpVD404JQ7iDAEyGCipXiRRBZjNsObluYNHsKfvZX4hMLlaK6T4WoxcDmDqjusFWvhmQiPVzZqc9mUhu5XJZSbzscRwS-04npi5xHK79bOc3HMTtXMXFAgqmDT0O6s3GLCvp_YfHPqyhegk29CW_9w0ks_Yzi5J5ZosPONOAR9kJYZ8EgjwNeLfYNxDLjeEhx-ZJ2VupvEuQQa9qU61GRidVafK-KJEjkM2o0uGRLdRCIlJHWwrbVySH6uCv5GSZn7M4HVuzJkzaxSs5VLZ7focneCkeoCa9I82aVuBufzbRW5Oc12626GVX1YNfDs2LJmGM4jo2_bXF51lZlfDzirmMwgg3DjeDkJ6f78IyMwcE0My05bk6iIJ4q1oP5chYs73JfMFESMc35LpytL2qM2Be72rNzwbjqdqVK1Sg4yQErFpXSEBgibsqzpfBk3WxZUBQLDK0MBz1w2q86YoVKSVzgqRgBu0SM4jlbFhWy5b-Vj2DfQgN6zk-bbW7vgAP68zQTuzeLPS8SKBW99PEtceDsEht-UVn4LayN9jE0Z3QeswDYx-Yka7tD4xuiO4I_plhpr-CbZIxvyLQV_qBouB4rTN79dTqbe98rMNaamLkACqJtnnJv0nlQ3Re1iDq1iSXeaSYJ6UKsq-Qnd9GdaQ9VAwih_Cri4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=A-SHo88VgfpVD404JQ7iDAEyGCipXiRRBZjNsObluYNHsKfvZX4hMLlaK6T4WoxcDmDqjusFWvhmQiPVzZqc9mUhu5XJZSbzscRwS-04npi5xHK79bOc3HMTtXMXFAgqmDT0O6s3GLCvp_YfHPqyhegk29CW_9w0ks_Yzi5J5ZosPONOAR9kJYZ8EgjwNeLfYNxDLjeEhx-ZJ2VupvEuQQa9qU61GRidVafK-KJEjkM2o0uGRLdRCIlJHWwrbVySH6uCv5GSZn7M4HVuzJkzaxSs5VLZ7focneCkeoCa9I82aVuBufzbRW5Oc12626GVX1YNfDs2LJmGM4jo2_bXF51lZlfDzirmMwgg3DjeDkJ6f78IyMwcE0My05bk6iIJ4q1oP5chYs73JfMFESMc35LpytL2qM2Be72rNzwbjqdqVK1Sg4yQErFpXSEBgibsqzpfBk3WxZUBQLDK0MBz1w2q86YoVKSVzgqRgBu0SM4jlbFhWy5b-Vj2DfQgN6zk-bbW7vgAP68zQTuzeLPS8SKBW99PEtceDsEht-UVn4LayN9jE0Z3QeswDYx-Yka7tD4xuiO4I_plhpr-CbZIxvyLQV_qBouB4rTN79dTqbe98rMNaamLkACqJtnnJv0nlQ3Re1iDq1iSXeaSYJ6UKsq-Qnd9GdaQ9VAwih_Cri4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No9LwjL2ZiycI9thZhospC_rqTnVgu-Xy1EoOHWQJaRtL4xUmOrmlp4MBTJYzcsrPxhjXhDrGbe8CSD6DRsebituXiHWTpnw9h7Tuj-xXclH021g16DLW6K5D8VGep40vDIj9WB1EbPnMqvAw0Vno025tI0A52RiPncAqW7LGptwiM8l5RpXTGWCy5zgLK9R4QNZwyewMS3Oi-eodihpWtTbKL50-Ci1KAt1F6xw8BUuegfu-Rac4wHz0EsOoKtPjGnofmDhHAZCBpe5ohwHCVhXYe8bbr8iRdDFJQcyFkXM7GNj5okwIf1Q0up4NAm39Mekq3AFGZ012CUMeIUSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0vsjxyY8qQQXUBf0wqxcAdt5fGfrg2iLMW9c5d4C2VLJeVlBlULTDK1-qdzzKuPvCnL0SirspU0C4V30Zh13MPeUZrgHQ1vC-2tgaYPTnbnZ8_MydoGc0tYucHLKVyh7cD_0_B7zzY3uAaSK87UQP0XL4ATk4UAidIn2K9ZQ7Ag2vZEB1RsXN9wPv9J9NWiuCsnu9p__-j93XtjOtfIj8Ia_dT4A05_DK9el84-d7fvfNMf7htQBJJwig-gFTp68HfgMWbBivUhlvm4PUBFZDLSVKNV3J0bWBA1H5YdbwLmX3xshHaZ8GKQvDKTnWlo6FQyFcGJnufe8rezTBaXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzSR1o76oIdtuBPhwVVmBVTMCgr7rpVUMop79A43u7usild51nP_dmswiZajt5jcVs8BXFM83PI6ZHaOmn2uOu02UdnnQKTimVMdqFvEfnJvFjHIctezB9G260Ln39lhL9aGzO4OMKV0SRKCUmYYfR_HeoIkRBJyWNs7rzBbvavWhTEViKRjCNcgg5RdvZmgya0qLAbEumqToM_Orr9ZIX_DKJ-yB23bBdi1sqpSpQBPWkHSDmNMoGLxG2_984CqOrWXkniIRgcZyvEZ4Zi62FpZldlDgm-mQFqtmv0-EooHCIhX-ziPCEwsakaH4tnILnTSf2gDGk-Ih1kGZmIPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj9h7cPBlf_HNmVf7XxbXtQrruIF1ofyRsU7C8PVZPQITfmLlvYNa6cTrCeKG2FWuEtLdCNh2FoMdGKkNM7dYG50N9svd7XIf6Mv4avtQgrUqh2EjMzNgDSinK4jvYdO7Rxq45fxTuJAoB0SuW1Vo6khNic9aDHecGz8nolmFPwnef2HBUdv6De3hpWQLTl1kX4Rw1a00OIQx_RiRUJa7Y666OkhUUJtJU79c5LmSpB7mZax0l3fWB-3ZF7n94PqcB9JNIeO6Oi2y-o8-Oreg4l6PqxP1vVEWDf9P4vj9AnF_ZG97txKEegCCpksneO_eqHlDV5rFobzI4OGAUq6Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXxv-LWAsYZCUird1tUZlwmaJ88a2vnxVK9Pztn8GHdD1ZJnchH_RYf3SnLCQhj1l_Du7UToFGBMv1remess0s52zaJyNVKwgh6qPUWiVoWiDOy6DLFbQL7rLfOVHN9bqbmWIfvvtpWx09Ow_ut2oK1F47pN4T4k4lBUE-jUfHvgjd51V81L55z6vRtimB34uZVfRC6OJxeiiBcyRIamKT7YmLAOsLsH-6ezFpZJC5TuVnqkYDw7ktcLk8Yvdvg0MrMZe1coGmmxevC0nyLYAgJeXj8RRb5_uDQkw4UWnrY_RK_9lw0AdDoLmVGCJ2Wk9LM-QZ2s5TBh4mHLZvy9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV79T0vd7wXq4RXO5ViXfCzEK74MGuIqGpd9lMza12XoRjFs8cluCx-0LeD3zi46AB39ARx82UIqckCscomzUoZhimiQYsAJ6_AnZfALuud6PT9TmOG2OYQNjLk_VnFerCBm8-qhYV9ahq28Dn0Ly2G7aQzKpPsHLLcPHOmVZ6meICqCb0LqG8BlKbz5MzbN1AkTp0rlMmtcj8gQ4j5MPokAJCc6QKoEg_V0NpZBfS6sCrkjNNqjdWHhfaI9NtnEt20FUZ3DYKm8gOtv458BY3h43FIR32klUTk6JK4UNpKL7vpUOLx0D8EOUg-DqKf5m5tJQAk4LKI2hK1OoIezkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Quj7uiOhR71-BaPLUFxrvEs-f1ZjLMe3h3I-3dbGZgBCfprLhMf55u52VbQKIcLXU-d7Z1SB5Uk9RzMF_8M4qYvLs-gv5qcSQGHFP3DWh7slzXhyTjbDPw1l5stUfiA4SpkQcCJ6iz2FnJ0Pnquok_h6_PYBOXigkTE_FAqUe0SHTO7UCYLf86aXQzrNfKCKpQtiI-nKKhVP8U631RDjoOpqmubOu1sZtv5MoRkyYwkKLU4EBvJUqmxBEYBksM7-xc1yWZ15BivlRyMYJGST86c8kQcz6u4jr6zvhb3tVVqKW8CoWxrvSKfNuUi3l6phFnCEE9ZrqTBsEr_IEAe6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=b8e_hyqDxh7BPLWUCSPDEzEYQn2ZLv2W9P_dfvHelAnCrCvvAeugjDVeAsaLn9gr2czSw5L1RP9b8Fqoh2yxb7Xyn5808O87roFeAbfcLGbr7ekq4jA9e-i9pdy-tZfbjqxd1NF-0e2PL6c2qo6eTPHoOws54eclWD6_TuZSWKue68ehkSrpmJgi8bQgjQVYN7ukJSlSwcTY4i-Fhylkm7mCTLoKYd6HFz8gyJZu-gW-I3lRFF3q43fBozEzW1eBKDMJ6d4ieHIhcPkOynztORNDv89--X_-GYEOfYBGCgArMso22rIZ4IvSwdnB2pBvXm2CAkoxFIiZjHFHhINsRTecgsrmho2558FtF-G2rnqHs8es-a2tBu0gso-5p1RCn5fzzrB4_UsREDr8Oj5gHxwgauM91tLSeqqhPSe28F5qI5bGqFGGW67plSqWxJ96-eUEOqDnqF7jstLsN_3b9lthjeahyydxgvSbo09277HIBLZy02gArTJ2BwquztEA4NaFnmqsM0CbPjM2RCyENXeF4ngWkrTDSbcxab6GZYAJRwXVZoQLdi2XyimCdgOLXy6D_QbRxCHIEbKE91D-3kXgXTya6tn1Ea3RZDWktq9hcmt_saC7HKxCKPoD6EZLKf4CjoMQq9pkVUiolz0g4VjerEFF-tPS6Gm1tBiQImc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=b8e_hyqDxh7BPLWUCSPDEzEYQn2ZLv2W9P_dfvHelAnCrCvvAeugjDVeAsaLn9gr2czSw5L1RP9b8Fqoh2yxb7Xyn5808O87roFeAbfcLGbr7ekq4jA9e-i9pdy-tZfbjqxd1NF-0e2PL6c2qo6eTPHoOws54eclWD6_TuZSWKue68ehkSrpmJgi8bQgjQVYN7ukJSlSwcTY4i-Fhylkm7mCTLoKYd6HFz8gyJZu-gW-I3lRFF3q43fBozEzW1eBKDMJ6d4ieHIhcPkOynztORNDv89--X_-GYEOfYBGCgArMso22rIZ4IvSwdnB2pBvXm2CAkoxFIiZjHFHhINsRTecgsrmho2558FtF-G2rnqHs8es-a2tBu0gso-5p1RCn5fzzrB4_UsREDr8Oj5gHxwgauM91tLSeqqhPSe28F5qI5bGqFGGW67plSqWxJ96-eUEOqDnqF7jstLsN_3b9lthjeahyydxgvSbo09277HIBLZy02gArTJ2BwquztEA4NaFnmqsM0CbPjM2RCyENXeF4ngWkrTDSbcxab6GZYAJRwXVZoQLdi2XyimCdgOLXy6D_QbRxCHIEbKE91D-3kXgXTya6tn1Ea3RZDWktq9hcmt_saC7HKxCKPoD6EZLKf4CjoMQq9pkVUiolz0g4VjerEFF-tPS6Gm1tBiQImc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfGTSizN3aZGKhJsj3-3RlyN1u99Y0t0M9cnzxYdQBQLydjS4BjIpDZD78GZnAf0THAyNzFT1W8u-z-wzZLoeykcdr0YpdHx73-XuUdqGz1IMGpZFEZTOxkqTSP2gkS24aTgDeq1xUEutPAlkXyrHAlq43rOl14UKyKM8eogyLRBzDNuMQgbFY1sHfayScM6ugncSvAW-j7sr2C7bgWAc386JcS-vMSdt8HSrZW5G7MGKDxk3oWSWZyPQWm8W-hgaFt3nWQFrkrz-QN4PnsptqLQ4I_SFI4rFrlSYPdxVhHKyKuUHG3AYxJEugOX70JzphdxQXxq-tg6n-O1nJm0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWVIrvc0jdkgsMQD2GTU9C6xNQn_gV7NqI9NABLL1AG0DP6P7Tb6jO9As_JPWrdDH6-jbfWQVmnv43_O7pigSBO2ndDWzA6oniK3hylNx1iVDyJzWZRdfC_O26u5RC119L6n4MCPWbOQF9OvMNidwzdgzF2SY5eCO9Axbs9qOIQVa_bf0vI2gAFc8BIertPg_Z1SB7X8aCKBPl5oy2DC1ywFboSscvcO8yQj2kqU6EIB8EXJjSEdcI3rGqP7AEIEwcYuajDG-whC-b5WZskRj2WrPRAOK0GVMd_P1kB6XkZReiqwdSDJjAehMUASgZ4L34XW69rZcEuAduqlDMBLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYdminVJtQcOIAyJ-RtQtu1ysZvwECx_fRgbcaNtcjeRADBAMHNLESRugsW_jWVBKnBuEr76_3eXoaveY2_niF4leqWsljS41HsF6otJkvamnTHSWQU2yKkVh08nQmFD0ivDYChuZHCU-5WIJSj2He8xetUDItf6ItTQz3PiXfYEhciToq6sGd5-eifmlqU0NOSPmvvqppg6Jar1BQzfDnMoZKUhlgU5ruXaFsoJHN2iy9r6P0LR-naCcnCegsEl_rIVfCcJrP_eIrsr9YGdHpnpZvqt2g20Yo11ZkzEXlywChQkEvbS-e1dXEOaYq2sNT9sjalzU0C2e-Zn7RjDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU1tLc5-CvmD7pNoDuwXkI038MZxCrJdhFNrpF7mrUhuqEWUyE75DmNWi0ySwxGj1UX6XkT1ZtedpaCann05ZLck2_OayCyQzuZ1dOZVOepYeLwjv6Xpf9sHTcvWQjJKb3KwRGuvSXhRT8oOtltRCIrwBFUojU316ID8L1V5T8BprMFXmsC0tz2cNpWMiRodG8krPayFbwXpsQf1wh745ierKn4K3XoCpeGNN3TRRC7KS0jkI3ENEt-inklAOdKuEf9W5XgEsrapNXnlkYVrvFF7PQo_1yD9W_gL4djE8iP8AOwlXS3mDcwitITcTdTlFAwpUeejs9xWFE6tonINhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
