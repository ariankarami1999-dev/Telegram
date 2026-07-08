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
<img src="https://cdn4.telesco.pe/file/Z78h1wQn5tDrchqtg4Yz0Bkx-wMdPgIuOTETZtTWt11oMJ0Kufl9pM7lg3uGAxuswBPeWK6vFvVNZmQQQ9V7DM2omv_27kdRwiraMHI2scF1WFLxZjakyrdxiboz5fDOlexAF7dDp_m7R0vAaIw3y_fQAJk_Hpw9SWH1p40huxq6HMBtrBmYCisBZ-II7FCBpdMnacDA3AKnt55Nubbw4QLC3FkI33fiP9raoVOVZszdC2pV1nPcYKW9DJKZERnyGG5tWyl5g-_6tdOxsD7uXfjLIf0QrDIEQWlmZEevWAQx-56cVjgymZRJELk_A3tQUJiB_NUHCHhkx_HFxUfocA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 422K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=WuzpmhGVwALG53aMhU10QideSYmanOdqPaZOiDCDU3X5th1XcJkS6fBJPWHIQkjqPnsDxbw2eP-a-WYklTQWK_IN--0FGN-rNbwDHVr8xx_4sF-d9t9lwqFb8uSb1LosflK1tENyIRNcRbthNimMf-r5faUvQ2_clxycxR7sOCv2BGyGnLCmQKbQaPoorZeuwZl2ZdZFHXGQo0Rw1pWsa6H6cvs_tKoxcOI9wkgcrIovHbIBttoLaEhnXBLy1N-fUQN6ShcctccbEgC-Z7C6qg2FYz96rVzp1z98dJmO-QtL8ip6L_x-xcsrz_F5FUwAeauBxMR0409qQZEF_V4dQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=WuzpmhGVwALG53aMhU10QideSYmanOdqPaZOiDCDU3X5th1XcJkS6fBJPWHIQkjqPnsDxbw2eP-a-WYklTQWK_IN--0FGN-rNbwDHVr8xx_4sF-d9t9lwqFb8uSb1LosflK1tENyIRNcRbthNimMf-r5faUvQ2_clxycxR7sOCv2BGyGnLCmQKbQaPoorZeuwZl2ZdZFHXGQo0Rw1pWsa6H6cvs_tKoxcOI9wkgcrIovHbIBttoLaEhnXBLy1N-fUQN6ShcctccbEgC-Z7C6qg2FYz96rVzp1z98dJmO-QtL8ip6L_x-xcsrz_F5FUwAeauBxMR0409qQZEF_V4dQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCqQtgXx_8VWKtJRoEbuPKBHdNURkzmz1o9MSxUCFrH12zTOFrG68-W0NvtjTyt1kf03sM6NC32lnpBnG5xI6vajPy9SN2sXq3f6uPOKy_OMs4NOE_3F1e2pA2KAypJU1CsH-0C514zp0MIFxuUK0k-s2p2-dAXsDLXeCyECMYchWxsKJbZlwJVM3WHEsqRPNEanp8lFyZj48c9GTj4yuAIquGYodIcLs76UMqJkgeaKf0EC9vos8wMy6zgcGRkTTjeCxy95f-c1PF3EKDZs3E7BO3WKueBDAVeQbmkxUKJR3Id7HQ3n0gOLHZbtmKQWWxqHCcuZ16SxTIc91hhlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CflROHh8yk50lUIQpeWZ7eSVcU7WN9XbHeFzvTKj_POWXCo4GxY-iriwiMPkpDsQ2no-0nxOYc-KtLxn5IQfz4b_e82fwqi8kL6eFIcivYYyp9cXZ5KHpWqEh2ktdexTwt0nWYfriKV9lMD6lF7WQq1Bp7QQoyYxXaWTpf5-BPILQ4nWI63dqu6IbNJxt_sh0e6zCcQGCrg44jAxXHO8y9cgFIUo-IY3RSQhVk7xYoj_3IM87XHXcibPn5r_XoX9cQLKflCMkxcTzdTgJEjD3aoBbRtoVJrKPaeSp6kNHqsYRGSX4U7_HvlBjaa1Wijy59YfGIzpojP9vaWO2NAucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3EqiKjt8VrOCgmuCD1NXFWhWs7hm-b2D7v5W227kQifFCZhjtNnCdEtNMkgRjBZ5g2WU-2Xdd8H-XX1idyM08OgXAtolr5xkirpfV0J5Ufb0I8nyg2s_ZpNQYNwvjI6KDF9yw2hIzREo3yshNVsMk_griqwiufpKSpqmq4Zi7mqwkB-B0GLqMlMzznhpVO8CbSgl1cARObypYnq-YichtfIl9OJDo1w5jiABHIVUrW3hm_a66oTU5MAXo1ir9p-uA9V-AN8XCt-MyTStWsDQLyvqn8ottLk38tk9B-ewB7KthxJdSPxdUyE5dULIp0bFaKXhqhUcWvSzenVBVXZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueQVm6RtqT0ayFNYVY28Lt1nGupixwNFqnqBf0Go7UjszpxZ62NXhipilZ0mBsVTes3qWgGf252sAIRouMH_GwnEnm2NAlt3xHLmGCAYfIYHqtuf6-N_friS0Q-kOwUh8ZrivjZaFWLaG2KdT9yWPQQgdRax71TTXOJF_pgtkKvIdZslmvm2Ro38hmxYovrsxZxYTVaxOsL33wnMUS8-3flZ1et4wla8DtlISswZLovFD0tTjah40g8JLE5AKllkZKMUIuTI0OAqS3zJSY1dU1j_zWvLo5-bmkIlTvZJ1vop-Ep_XlWC26Y8TgjVGBKVr6l9MowaUgOV8M4iyaiPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=WEpxWZvkSM7CjA6ZZJtjyUoNhaG0fDRJwNLj78h7zgYac5L4Z9UVDPBxMyUe1H6lFT2MEO07oybRI8qfDntMslGhYnxx8WRDMqyWrenI74MCPfQiww9AsFUrCbk5V4DDGfDT3C24x-7rr5i_7oJzRoGAdJ8RdHhdYMUQnGkyoLGkM0mCRV-bseoiW9-yx-ZwVfeHhj92wkUrhFN4Soal2bR2SnukbjKwYAD6iff6dQ9CEkS9yLGcdfoCuPCAc_R8c0ry1XgNZrM9gc2Bx9OWPoq57CjcKWIANTsYYwCKhUsPi5QO6hYbrf75uYHof987OeirwF-hda19611QlV6tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=WEpxWZvkSM7CjA6ZZJtjyUoNhaG0fDRJwNLj78h7zgYac5L4Z9UVDPBxMyUe1H6lFT2MEO07oybRI8qfDntMslGhYnxx8WRDMqyWrenI74MCPfQiww9AsFUrCbk5V4DDGfDT3C24x-7rr5i_7oJzRoGAdJ8RdHhdYMUQnGkyoLGkM0mCRV-bseoiW9-yx-ZwVfeHhj92wkUrhFN4Soal2bR2SnukbjKwYAD6iff6dQ9CEkS9yLGcdfoCuPCAc_R8c0ry1XgNZrM9gc2Bx9OWPoq57CjcKWIANTsYYwCKhUsPi5QO6hYbrf75uYHof987OeirwF-hda19611QlV6tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAfckIPctkyuNfjN-WXrss_LiY4JzQt-xPa7pTtSq60VR_3DRnUgDarTwoGvTX5iVO46uRlCZOBhEpd5zAPR7X4JvnT5SG-laPrmkQbdg3YxNlIulMv9Wz56C2RHp6xIk4RE2KW0-pN3nS0J797KpUGuH4i-ERnt-OA89ogS7TxrldQxgUD5VQ_hhe3cpqR05EH6DzBEqFWpwoGKAiNW2Sq5qWOge_62DZG45NSQuC6GpOoO8fXgtn5sq2Fj4LdTobsYOO5Wfr1WLtwFBrs7NGXI_NuATZ7G-ZVoBDsNioUp1PnUgcUbYDEfgOQnl97shfkqhVSdRROTwvxqkBZz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJtLX453BWhRydlUoN7GE6dtd0xqofIjF9iwImSPsdtmTqDA3tK01R7synRu82EkxAUPbJ6eK5L_E3xt8Nayxz4_rTfaN4_wbgh3CRjfPjrEXEPInYimoo3fg72LdXYvfE1Wejq5SYUKCzMg0lKkEOSM-CWc5Vw3DRZjudwGH-VkNmvQQwCZ7QwGBZ_FwKzwXwC7vsrQownG6blwP4OQ4-r0GBLnH1-pYQ1mKXeWRs-ZJ_oxz_A2X2vb5-wffHxjNjjsEXyyAjioHcX8POYLyQdl197c701_uK7Q7oQoq0kBdrFhBikcK1oSyi9piGXOaY8a2j0HrPSDAneNX4MOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=XCjyf-_PHk-bnHvYW9ZRNJoZtbuMqWKCGqABa1ftUVcHaCoCFgQFlyHxogKv-SXEZmmPbpswlDonAb3gDgEesMQGCwflDzrfV1pn_eY9bgE7I5ERKysszhbFoNXSx5GlGQ0_fL4bai0ZLUWCK_ICtEHoyPSNWjZzuI23WR2iNn3rIt16Ie98qKbaT8ZMMVOAWPF6WAxUcF-Zb4FQ6UU3gNG5psqEWHM0gGnJmvECf9pqcJnV8gZ0BwI1d019YppgaeIBP_ta1TChJmP8h4IQ_TM1VBXU0mjIfCgejhg_NGqJxtwTx7BI1RYy2ojCI4F9CS9xgdPBbBcENCRYyd7pRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=XCjyf-_PHk-bnHvYW9ZRNJoZtbuMqWKCGqABa1ftUVcHaCoCFgQFlyHxogKv-SXEZmmPbpswlDonAb3gDgEesMQGCwflDzrfV1pn_eY9bgE7I5ERKysszhbFoNXSx5GlGQ0_fL4bai0ZLUWCK_ICtEHoyPSNWjZzuI23WR2iNn3rIt16Ie98qKbaT8ZMMVOAWPF6WAxUcF-Zb4FQ6UU3gNG5psqEWHM0gGnJmvECf9pqcJnV8gZ0BwI1d019YppgaeIBP_ta1TChJmP8h4IQ_TM1VBXU0mjIfCgejhg_NGqJxtwTx7BI1RYy2ojCI4F9CS9xgdPBbBcENCRYyd7pRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=m-raVWwDxo6kCN4gWi0ztKQS0ILostn3NGg2043KawJFkBDRgsC68M6O8xYO-e4o8XhW4xmEZawxM-_YOHxfgH6p4G7EITywSsCRr0diKdm-bzG5gWcJDViTtHfQ5AVxAROtQRgP4pwRfrXw267lUd4FF2q_JkDMovS3yBLTa-hkHrr6VE9vfMHdxvK2O-1_wxM51j0ZNmTiogN9VBUWXrDaPQxmFEyC-nMYeAnZuPsGX_vuTMj8QwzVw-emK8EbJMBhufR4_OYL_wdH2Vug0CooRJdFztOQse-it9iA90bW5WpJ3mfIN46LII2B-_r0592Lt3ZLmJw59kVOUQQD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=m-raVWwDxo6kCN4gWi0ztKQS0ILostn3NGg2043KawJFkBDRgsC68M6O8xYO-e4o8XhW4xmEZawxM-_YOHxfgH6p4G7EITywSsCRr0diKdm-bzG5gWcJDViTtHfQ5AVxAROtQRgP4pwRfrXw267lUd4FF2q_JkDMovS3yBLTa-hkHrr6VE9vfMHdxvK2O-1_wxM51j0ZNmTiogN9VBUWXrDaPQxmFEyC-nMYeAnZuPsGX_vuTMj8QwzVw-emK8EbJMBhufR4_OYL_wdH2Vug0CooRJdFztOQse-it9iA90bW5WpJ3mfIN46LII2B-_r0592Lt3ZLmJw59kVOUQQD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqXsfHkEIUSLEV6Cs7ln8GHLoP9PL-abFSVLQ_myZQsATigIsO5nIbCYmouyNV8roiugJvgsZvicPAEJvmqcGDOiQB4Ifu85BoA4SPgobnhtK5JXlZTd1GKw3bRj3G3zSTaXc1CjPErrqC0KH6v7iLIutyMWSTGVwnSFy9l7mG7L6qYjzDP2USptayGC8qZ8ROHSLA25xiIEsxVU51BafcITJzktxgfDqQTIOCvl3cQvYUqnJEuCJy5NKOjFg0wwpmAyk8RhDgnBsoYimrnUDoRSdFOwSCj2TdSiugavWb2lEpBMBtj-yybebvnto6NpomVJCYXbDvI8mjY5jyyT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEwDv0T2aKMSk6TqUnOkbQj9SrGNjOlU5zfJsp1kcWjbmozhx-i6030CBZB-bRdTfEFXueiepyNaDQJNsaoILHn8fQPn4bNNwhSGp-60CwOJo2o8bfMmg8QhiQtw90A_FOTyNcKdJ8dJoCVTl_lh1IaYslYl51MuXZqkDVhjYCalITPA_amgDQMn8vSmH3As-K9IIErrR11WGBb6SxOuY_4sRYTum8kEAo-AqRc441mmciiKTmiF4gNXoB0b11n7it9zc2bjzYUg1-LYbIOK8xwNeWk8w86l_PKm8e108Sh-uRbJGZEm0LLAZyvOQhcFTpAN5bZV_JvaFnC53AJSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP3HpIq2JsDxDBJk_F-344YxVP-dnsub8-VSE9BNxH-7VQHq9UWdeVQKkMrRtYDB-6Gkp2I2t-nT8nzZQu3ePn8G7OjON9ynlz5PVPfS_-yLRi9q0nKsf3I5OVddKPc8Z1h_WkjiKdpymEWtc8YRZ7CY_B76B1cZMS0Dz-vT0cTRANwjW21nASYunhFBDbmm73kBJvYMP6nAfkWNPleSHLBybLIKYoYONe8goXNRVtwRqI8-xSY95qKDMWlSbwWEVUEf4oTAElYyndwDYYhITi34VYGfZoJZwiYOc-QIIvkcKA4nBEk4hTtFrd5l2SJqKT7z6JXS5X_jDhbtWcAX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=RBKSJD9aIMHMsrOY6YOBi8IgwOEfpaptv91N9GYOwzaok0Jbgkgn-sj8BIVy_kaBCtgErjsmH0wXANeoygLhPRHz1ZGDjSFz6UZxTejMh8gOJywg6zX9QPMYR-fIf3CsQUWXpeUcsANDUkUVflWTGOoMDDXcqQC2CC-nWebg5FALBvesf7qU_eJ5EToWw9NY5PhlZdPxy9fnsoCnhQmnRQ7KoJg6m-GwK-g7OHkWQaGn-fKBF3b6Zz6Qq3T9labuLD4xqAuZhTAuruSf_vnrJRVSgO7Dv85xCZ4I1t9cgeAvNy9nDWwX6FHf0NWtySrKZSLkvSRkwpF9Li0-pk40ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=RBKSJD9aIMHMsrOY6YOBi8IgwOEfpaptv91N9GYOwzaok0Jbgkgn-sj8BIVy_kaBCtgErjsmH0wXANeoygLhPRHz1ZGDjSFz6UZxTejMh8gOJywg6zX9QPMYR-fIf3CsQUWXpeUcsANDUkUVflWTGOoMDDXcqQC2CC-nWebg5FALBvesf7qU_eJ5EToWw9NY5PhlZdPxy9fnsoCnhQmnRQ7KoJg6m-GwK-g7OHkWQaGn-fKBF3b6Zz6Qq3T9labuLD4xqAuZhTAuruSf_vnrJRVSgO7Dv85xCZ4I1t9cgeAvNy9nDWwX6FHf0NWtySrKZSLkvSRkwpF9Li0-pk40ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=C-Klz2NXWpVxmbbFJjQXoQTyA6yRI7j2tSCIW5gIwIf1mofC4IoJTpIxr_aIxCjtkK_hDQcYrvFVycJcQo8EDyLdW9_AiGuxtlabSL9L4kxmLnOd3NeakqAPS12cyy6LoW73hlB5VZzG54-o87ltWyk-hnIvubJjbnyZlvyTMuWLEbDi7ttajGRwKOfwjiUNvlU6duisL0M9QFg2bdENeLvO8hpLyOPaabrj52dy-RIcMKdZahZJuO-2Q-I8Z3ZnlNrux5jony3i-qL0r-jXv6sIwB9hvEMoz5hcdaSxKXloV4O6kr7H9DlzT6tkbjxtEvIMHuDuu2_Q_SEH3JoF_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=C-Klz2NXWpVxmbbFJjQXoQTyA6yRI7j2tSCIW5gIwIf1mofC4IoJTpIxr_aIxCjtkK_hDQcYrvFVycJcQo8EDyLdW9_AiGuxtlabSL9L4kxmLnOd3NeakqAPS12cyy6LoW73hlB5VZzG54-o87ltWyk-hnIvubJjbnyZlvyTMuWLEbDi7ttajGRwKOfwjiUNvlU6duisL0M9QFg2bdENeLvO8hpLyOPaabrj52dy-RIcMKdZahZJuO-2Q-I8Z3ZnlNrux5jony3i-qL0r-jXv6sIwB9hvEMoz5hcdaSxKXloV4O6kr7H9DlzT6tkbjxtEvIMHuDuu2_Q_SEH3JoF_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCID2MXxy6zHk5YObNzRAS9QdqDZt483EukimwDwT5be-8RwBrp33tZ8iqov8umcUGZTlR0aoockA-T6jpQ7AYdpn5uX7QTS7K0RDuulAjU_OaPX0qASqOibbenDhL484n4DGrq7rITrkWkF-Wo3iMIqo9pUx8jGaYv6Vs5ksJTKt3Dm1H8nsepEQPSh-oI23pIm0e1Cer8UYhyBHdJmMDyy7XxsY705JKc_k8NdIAiu-ZQoLO0NKV0FqyadKM22U7hVlIT-R2QKSDhwAnUOcAPpABDaxDynq2vMLjXe8WEDcWWjW-4rQT7y7-sqjBZ1U3_rTvOEPzID2xHxscdUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQSMf-0ClGK8NOdkR-E0SEzhmhBkqTaJouAtvkqhGcVB3_8PlvYbvbnU1zqOW5m5_bgoHCaDqgVSuVm7MYrXHlRGr2f0NDjZuwNYS4Xt41vMqufWNajLd96EHEL090mkCcp8viAk-2ugT0eEuHOrbTdYT0uwCI3vEK3-V1TwqIuBZK4bRYSMMuStha_PSVdNiFsh7zh1ZA9_fzWtRRLEYdqkeQspK-McDg02kNyoflIrZPNptyXGZmynw57QnmJ1UOfhVwyUu-OP8SY8F1dMsO90BGkwJbyabj0ZsYYePCy3LrzRMkeQ87F0shm4gkr5HvVed_wiqBO0WVzhs8JX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chHr-gE8c7xKyDlrMhKADzTPz3XUwSqH_gVxP_wPsOf-2XvUGXcN4HK_mU8WxfvFtsgJwI634RYwU-KZGVIhimRM895Dca9SWvaaIq2EdKd4FiK8lbDfday3jdX_tCc8OGmOauHDRwmfo_D42uWNzOdcPffmJKj32AjX5ngiin189fb-tADZbL7IeywnFYOQu67vph50mLIqsDOkn87eOyxnnB2hdGbC9xyb-SqMoGTjrzB_e_3O2-E1P_Laz_SguvSPTJ1oailfjHiA1cJ_F74KwiSeBeZYQIaUHNFy9gZ2eDJL8_4FvuwPCxFxfp7OT-3f9cgMW0b_7F1UUMycoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB5iNiIITrLGHX7CHeKk1xpzwn_D6SMmmnPSwLea41fjV08AUu-fNIWvM84NClXgkhPyJ6Gzc2xYlncPdUnMS7fhTyf9KI4NhnfVjbyUK4LpMskQV-G7pZNC4yzH993U3xDhSX24FU0WklNnq677KU9_4v1HKOnsZVaqLToQMHWTbFmZdOYd-GHy_JJpkEPlO6ocxHl4BCyqCoMZ9RwpaYBOFG4KtFGhHS_gn8uR4pd2pdZ_ospjjQTnTyAXrBOY8WKS4EikjZiSckp3FNs4pQpOyvo5hVwvpO0e3HJUYW9_K8QXqF5FnLAWNOCM0rfwiznFDfgFpIIk89RSlQvkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwkMYG5uWb3yXqLq2ZWSBOZL5pz9Wd0jDNsHRKOhXuzyuGo5kwIieryGyYn81MU4tz8_sta3vfScxSN_RmsCPLq6f6zF6dSizLrvwNuWnBIUEyc2CdTyQD4mgeKa0VoHB0lw_Ou2PFzNL3Dvde8-FGXHtDdiVzhfH9oZ1jTI7xfuWFR79hPBZoTC3GBubNzyeUlKdj9oRfwb9rr4CfTmQozIh-t4UZwUbrZscszEeF2pPLCgLb1cnjiJZEyMHfN540iDmDHXjOJxwCmHFrlR5Ixleen4LEvzg6qIma4RDDCb5Buh23ycqKLWKuUa9rtD0oO0ZcS-9GgoywjASx5YPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAMCtsOKFAneuywziLtQw_-YL8SmVMUt-Igh74AdVUkVxALgncYEn8p-v20wJzCQahy97rWisjAbmzOf9csNUqxT3r91BVqxv2LejNGNiUJV5Frfp1g9is69nbfNUnxuXifNorud9vHeEzuWLxc2MAycntr5Bv1XXzHZTXg1RZpJegxFA15ep63iGKA7DVLqr5mAwZMoEGB6LLCvfcJUBKGEqzh_mDAfEgYFv4tpqx1aataQtDkKLE9Sn42_ZHWRtIMQ3K_fEaa8-o9iPCWYYYPi9EHpmtdgqlCZG7tl8nYzbMp7bGnwiknaDvNzm5Ip35v9HraCpNGYlOV0VGMLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYROZbdDK_NxMC2HyUbQvOf_qT3p13ltJTvVyE_a7yLuE0urp9TFh-t2R1hfBxLiOOhoZoCXKDUB2_53yNAdodTb6GyLbssibuxMozQboLN6APB3FNbB2USyBftbFoxeSFfjcuc3E0VYP_oI9MeAaEKTdagFUfzEOQmeY58DJGYzTAzIz4IyIYT1aAJVCpS1ZsB5lYPCh2z-KyG8uxgHfoMKqRqlj-x1a1LB8kd_iJcUE8DedeEWt45xzdLB1jJxq_NPjOWxK8GXJIFjbPnDJn0BlCgOlNrU1QcCE6ufqMGzVwHwol_Ti0F-4F6cY3K0OmMJukmGkR9W8MGbzCBzog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGgaRuVbRi6f0hNF49iILqfBBmbHFbJGO8DBNrP6YEe_2Mln_KAAEcKh26egBlQPS1QGw6Ykw2gTUI-5quIH_Yup81i0uyEEHZyuQj46LsP6m4nZhMs5Yqpus0mmAURu620W7-GaoFKdizNcQXYFPV2rJiKmQCZ-R9J6RGtn5l6hwXPWRpbXycqMd7DYrWxhPFPjcCLGlrguUhAUIEB1KbCf9Zbq9QAHHhZoQSVLcGfFpu5pU_3uWGLa_dbXzcJLuuFKR0TuAQnyRbnT3O03JSiIoF3UhOliWzn0J7q4L0VuB6vzzE1AkQ7t-Xar974lymqCIXUCgVhe7bBypVZyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=axqS-ADnNxhav6IAehisNgBTo4DxyqTmOjPfOpqCT3IXPg0BssEnqqdcdz2DkHFbv5eeYj1caFEld5x7-tv94vtwvSTQZAOGXBspaP5GjPgDc9E9XEyOaGH7NI2r31CPtsWyvdQEkFvPU3ZvnTjg3883GvrdZ-0wt2IVsNyNQlzM2l64BDlYBi2S1V3WvfEwmZsy39eV4rOFXHnL5W7HqPgOj810FKAnbzcp_K1X4Xj9aVUmKo5WtmQLx1E0_BjBg3iOsZS5zajEBNPTzQXpkkqQ29Y2stAAYosmbWmdk0MOD3LmDMIgfVJEX5mp6G55TaMEmbLfL4FdjKdxz-eikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=axqS-ADnNxhav6IAehisNgBTo4DxyqTmOjPfOpqCT3IXPg0BssEnqqdcdz2DkHFbv5eeYj1caFEld5x7-tv94vtwvSTQZAOGXBspaP5GjPgDc9E9XEyOaGH7NI2r31CPtsWyvdQEkFvPU3ZvnTjg3883GvrdZ-0wt2IVsNyNQlzM2l64BDlYBi2S1V3WvfEwmZsy39eV4rOFXHnL5W7HqPgOj810FKAnbzcp_K1X4Xj9aVUmKo5WtmQLx1E0_BjBg3iOsZS5zajEBNPTzQXpkkqQ29Y2stAAYosmbWmdk0MOD3LmDMIgfVJEX5mp6G55TaMEmbLfL4FdjKdxz-eikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=WxAkFusHBrF9pE3Pg6IGhnPbJNkb7kiizwovFazQGB18JgATtsNqWzEFIKrGys8G1ZfmMCrI440AuQoVCNo5cajMff3OBdEm0OsCaBuiWj5wtXFZxih_5iGzFvSWZC1ZS8PdteK5YacYha8Lg8dYSNqKhhlSARAHCl5CIboepXed83a7ldDSiNd_SSPdx2gVOQzIxeX2srDswhO_Or72pB3kdukQPwCDTkfu0nw4HS9jRs2Aka_oeqrN5dUcNDbHAplXDJb6xGwZ-kyiNI4mks2qWDx2-LT62tWmSUngXlhcxgQkUKR3Q6ZVuHVUKxN-g34m17OlBbt-RrOJHkk8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=WxAkFusHBrF9pE3Pg6IGhnPbJNkb7kiizwovFazQGB18JgATtsNqWzEFIKrGys8G1ZfmMCrI440AuQoVCNo5cajMff3OBdEm0OsCaBuiWj5wtXFZxih_5iGzFvSWZC1ZS8PdteK5YacYha8Lg8dYSNqKhhlSARAHCl5CIboepXed83a7ldDSiNd_SSPdx2gVOQzIxeX2srDswhO_Or72pB3kdukQPwCDTkfu0nw4HS9jRs2Aka_oeqrN5dUcNDbHAplXDJb6xGwZ-kyiNI4mks2qWDx2-LT62tWmSUngXlhcxgQkUKR3Q6ZVuHVUKxN-g34m17OlBbt-RrOJHkk8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgekOCoOTqFii5JHZdaWysgwzfeIhJPcQT5gSZ1Xw-u3tvnufsrGKIWvqRmk5-OMboQyBjjNZcFTmWQP2CNR86Y4PmcmQG0vQ_i7wqbcSYc6FjvHCBvqwG8Je9sKcRHashjJvDum1zK35zNDb6P_h_J3YXbvT-h-l3gII_jq2FLDyFuX48ta-rAX6XyI29sM7wN61fhxiiIzzZT6laiWnta108brjQq2Vp2632bu6NGeqZEYtDfj8cJ4Mc_bEQS5aMxATGzr5sUzQy9w0PBr6XoEYOkOO6AX07Anfevj72OmtGjYnUarUtu1EZa_0B6Y_YOBxYwP-rkZLZBXB-pC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_YCvpSJO7psqko0jc87T4B-kgA7FDZ-Bu5QRngCa43alzva7RNcp8RlheTGAD9zK8Wi8IBUyKW_pbyizPgavZsv3KU0SFmBZqyxYBnjqu7d_T8adjOaXGkRzT3VYs5U14v36h-GJ6NMkeC-vR2w-b4aAw9Mry9YxMChzdOjefT8nhrTjihY_qR6hpN0FpQK__x7q8wP8E-w2aipMCwhzbzdzjyO93xKJwsAT3rAWpjnxw9egBtoustmwQ7XcJeDk2Ambwzey0VruakL1ATbH1uC9SlRaaYic1maVseuGtHCuFOtkiX-nj3DlvGlpSCG2z9w0qPfb-tFXCCgGTBnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=Twsv18sgVgkZ2cIQ0RsjyDYEDk4xAwYOCPwdfqboKk452lJYIAcMt27uyfSQ_-R1RTxDuooI2PGUpvjRQZtkfUlRpO07bxFeeR8joQ6ECs1cozqw1xmi0otGPp8KO-3wi6i3SytQh4iBOJnmGleFFXj4wVV7TeJdB17CDC0wggyTN7UphJwyCx_byO01uOtDNSahRysoCWaff5y5afBFLs5QdMXE9OjcbPG9MZkvKSlzN5Xu8iUgrWU-iWGvmhaPGmML0CbZYeFo2GcWaTfhhmuU8LAAr4jYfZbsg3xuUN6HrGNMlW3PJMH1pQznLugbs2tbSZzaV3oZuvck2fhLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=Twsv18sgVgkZ2cIQ0RsjyDYEDk4xAwYOCPwdfqboKk452lJYIAcMt27uyfSQ_-R1RTxDuooI2PGUpvjRQZtkfUlRpO07bxFeeR8joQ6ECs1cozqw1xmi0otGPp8KO-3wi6i3SytQh4iBOJnmGleFFXj4wVV7TeJdB17CDC0wggyTN7UphJwyCx_byO01uOtDNSahRysoCWaff5y5afBFLs5QdMXE9OjcbPG9MZkvKSlzN5Xu8iUgrWU-iWGvmhaPGmML0CbZYeFo2GcWaTfhhmuU8LAAr4jYfZbsg3xuUN6HrGNMlW3PJMH1pQznLugbs2tbSZzaV3oZuvck2fhLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCXUyXse0tTDNCC96eVKPMg-v4EeZms7nZOtxdk2rSyMYpakkbcSOCeM7LbszV4KWDmR7iTYpn6Mhn4AbiqDLdKvGbZ382RkEB_Y4MRBogtILJUlrrwtVvsp6WeTNQDoOunX5wDWZlVFIRr3e4yO6-LcsqxzEI_pcLemwXqZ5jw21up1cW6C3G_QJ8e88n49qw7wJSdjAj-8uCTRBbGNVxYtkkcWUJcSObvXN-gzSBIkeHm4Sv9sHksTr3-kutVFrPvQRDec8LODY03cho5MfPF4F-UYJdjH3fQBic6xNVhxjRKYO7qd78Ju764DHDq_FBn5zIZs_eV6hSVRRLsRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baO54Tn3L4cXH1CBrnO9g5J05n2Lg3Iq4PYEDBxj8tkQisvMUHlVqgNQvwLVMejJ_4P2p2VWaD4Z06uthgwVtn84SiU0DZpqmgEYP1YxGYcrATFUdGWCNdwM_1IJQq7TdXq682iW09HXtueB689aOotBcxFOT3JfsQmL6-n4z6NARnxL0MFpsR2aej-z1IvI9ahq5aSA7jTcejiN0XwAP45EiZCfi1vB8HIfn56nBFeaFx-2YnHZOhsverQhhlGyPK8CgfxlLiBc_1OqG6tUkp0BVhqDvCg0_Y9UPBGs41k5ch5vMHAYAgv9htcuuhwgUtZHyDLoH5gG-CWqLK8rFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaiNmebR_Q1X2qZDqad9U2LHyTJjda-Q8CL_0G82Gs8Rnx5CHJOJaf-eC3x97_xuLD--3wmJ9P4ddZobWbPpPtkV3Mr_fg9cNA52hqZj6QMOftiy1T1rdwpGbz-xaRCPyHPtfAqVUpR5sWmTQN4nrm88bQ3fYryUSN2TVZQyoj8HWBG_4AVVmIyPxlBOLhz-gWEY5vA-BTGvRQzlgeuoeZxaX8I9S3-h0MoxRSlpy8yd0_JVkzqt6K_OfZALLygrcNpe7xHf6H2Qx11bJy1qjphJI4oRQyUucptH1lLGRlpc8GHCEjm7pEOC3jJHkWetTlhwcAlow2tDGErNhLMePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piKSKYTkgy8HSB4D0JRhPpngmOHIiz8lPbJ0Ry5oZhtr02CY41YGm1UFPdw9Km4FnQAo071qXwojYFcEUHz-SOyN3G69la0qyrGSrUUB-4_e9MhtIVX0u6cWhuGzIbXT5nWCdDHSHZK12ZHAVgHnMEiaFp0htyxe0UrSR-1uNdR7E7mmV_gA6K7fQZesuHsUtqPPMOI9z2iy6r1hDtZUagzmLipIDue7EFLWZTS9LQiKcDwYuqiwhuhUnX_IGvHM1KVrtpMNbQOzGPliPDabGiBsRh15s5BjqgmUAhGY-kzXp0H5M2L3Guho2kfU4X8bN73n6qAkaXULlebShgYdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ0So-KK8F6qvtyt5bSJs2lRx1rtzo9divyML6OCyHuz5lWUs29Bvcy0tDpryNk2F4LWZvXyQzJxO43o0DQBraa4AV0fZLNAv51f_lH6ekHFm6opjdWpmVZyc3OCsJ4wTHbVi1zx4yR8tXZiOSe3-Xiucp8dtuK0zFNJ51NtBVz5Z5iEy4NcK2vGQ0WToXj9GYu2PEA6fnaAArNnu6vfATyurKh7GLw06CbEJjpNM8WewoCOQNEWx-OkXxFa8spSPjQCJf8ZbepyYut88jY1stnBlzE1Y-qAEzuOuld9V4PDinpb9LnhRRbyKNAca_gxNkX_z98XXJNP8PAiuyRFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsAfNq48NmfOJddOtI9gYW-liBej1q0HeU04eBT33tCj2JQ8okGMKNiVYkmdCqfSiD2PpxRfp3KqhhJEN75qjSwMKArH0M-wu9HcQ4muFjMeiP9s5c7zgh5TAjW4nX1YG8x4ktbgwRiwiKa1Rk8SXCsAlYQwkTg99XBlc94Q7gKcF-oeAei2SZsvu8LKaKZ2HpIlWBeIB4aCUKhzNrSk7iFDUET_XfjSgqcs46coqwaGCu7yIXzRQiLx2PS2xU3yZ47zS6aCpqWy6dCqk_91YsG04q11cnloOGepQiASjmR2a6AY_HAkJpAYBUa669yT1X342sCqLeV8uNACluJ2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnCZf0rH0f7fXYiBCSpiSJxzh3DIru8j74yHbwuhvqos7gkKHWmNWxatuKT7WgHFYGUls5ZqaImBGZ_FIyG4QZiixY-mdJnhmrMMscyKZ1n-fZKVAxP3ja4PnqTUFiyTVzk6tBa0ntrLBzJy_moq5ATAcIwWqD01Y_bvGygPlAMDbmRqRyGv4B5HuEHg0wWhypwIkBbDd3MR2fyfZKuKK_CjoW6RgnQZAANpxi59DvnfSkhRBes_biTLFx8KoHfpA38VJZ680DXw4NfQyUl7VaNzYWjXmtallceWhIFbTpbBWnPaylfUW_50_ZmsYR3mVHPg5m2h6XyM62mzjEIigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2E50vwC7OKzCFOLlPWwEmBIcyXIYWyUpkmKPRwqQKWaYjjrEXZe0X4oZ94LMEIFCHAooBXp1s1871c9glxvCDPVneyoe1JDqMRHNfQzRJHHtyaVt6MdOGtcSWqWF2U3vU1v-JBnDasW4awBAYDWDUKV8LXydQU4lwl1r7rCcooa92yV9Ssu1QcsMMcawBZOggvPaRutX5dlfyl3xbYIS0UOkEji-OTC4VsJw2FG23rkYgFQkFeJxebcBBze91FtnyyzJ_J5swwM4mAqv8l5ZssAp2_DQ4PYzEqrPR61JCa77khOjRuezxjC7otEmgGtOPufIVcE3pbRD9Mf4TxEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e90cVu1xty361ViTPchJ2sVMRVQ4sjoqp_bL7cn9lVaOp-n-W-SkDmcd0NxhxH2h9k8tiauOR3ZEF3fluW28ooVv7rPfWQj3pBbWVhFV4CdW-7DHwb61f6Il0B-v95DUa2wBF5MlaeYROYwR43DzUbMGuhpJQYfy38fd762Anv2qrrpoy2RRYjA61dkSdk9K70qrlV2sDLRNNtPkc0AU8kIfZ8WnZZb6idagFQwXuHLkeZgusEvF0LRp-gFS0fmnH5Dj0ursdjvP9Fnb5wMnRd400pfxDRg706MBv_sqf_n_Oyr3W9F8SEKjNXFRhZSuFiDb21Zt_1YWK4H2CcSq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfnmzCbJuC_b3X1o6O5WZdhTSzGjm_WE_i9WjPrF85OCkDyUwCHJBfk-TODdiZ0Rh48ilnxQnq-RLl43e338sWd6MwN2jWbDgcclQzBbaVD5NgVArAloiFTXqeoexG6UU3ICwy2J9sRshsXI-zm9DJXBuHZdbKklEBk5BO_nbMG6Aw3DFkt_tRlZEN4wYDJji57oVPkJ4jlR4LABC41wHeQhQ40L_ICmrva8rZNPrNGMYQZCwzw2jxiyKUqbtvIY2_BFohBzkV763ot4vIFDIx_NDw5TeX-zpQiJ1Dbsv7w5H5IC_QcYRYshGjZXYkuOjqPrpu6NE8CbRQRaPVUmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IggWiju_-0Xjt4i3W-loj21CpQvGBMx-p0Vz_16oHxpBLGuCVLwUugtavEL7Mt6CD-VPs6QghE9mlPkMVgi1Ckd6OpgcFL27_LQJsbPsXewu2ZnPTFMR65AEYxqjxALmdtscv4glBrejj6wqzpQLDwVXB4DHA45V1Br4T73rhV3QA3AGhyC3h7KcdCte2RiY9jAvfneFCeRBDtABwyfTp7nBAh_ns40guE5HHNgjaYm2fCPUYyKOKirpEKNWmMrzTmVA8dKA-0Zr_EbDI-JVj76ubKU1oAQWLWd-Ut6GMmIr7fw-NvYMxyHlWpC8DY9y_HiyNXIUGQfg_i7iK5qodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b58KpsytLWK48qROarbTb721jNIuBcZH-9ewpQ5IhMoMaQ5RjAFVVM39uNmB8R-8mcm2XPqXzTlMoVSTbpMv6Dpx27vvtDzd--qLm-ABkLAN-SIowmXXAgntbh1dcsY76J41FupoCpQJIyrBj7RWu99JrjAf-Szw3guNE93aXFlqFko9RnlvfYECAsGcganEXIkfPTl3ZKLlkfxXvzIBGn7bo_Nkyax2Y8eR1yf_9Q5xAMWPY7dEzAVCoWwziShWdiSg5y6EKb0ns67EEQ5Clp5SCeYSDWXAXCEWSJzYURDY2x9iNY_a_028ALLWnRe4yeAPYjtA6hvbZpiKRH3o9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-n2R69IEGmuLgPbpMeAGpE1arJNiq7YPEpg7curngiFGWBDrnw2ziaZl-TTyJzO2e3hesWidvJaSjNUrsqAxMl_1_lHrAzBts5DMQ9jjvePvwS8Gjr9YPWXO-7tJM3LbWLRzD_iRy5brU4ASDadzhI3ldKlMc6EEYYSMt_IqEzaPYSQbeLpjtLuO_FrwUyWYkdEBX66s77WCJC2g5gD24q60Gl5ppJNkdq7niNsE2lm_hpqON4IU4We9Vq1SeVJVqdmtTQneqUcnW0XAcjncZvjI6dZQFsVHgxPBr2dbcdf8e_ucp5rIsjJgSleLUX3CZ2lEIhqJno3xkL9p0nlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMvWAJGbB5JnUeaVSHoGjYu_tBd4JGbBpYArxV0lBMVluPtom1VBF_fkNrhnAakOC4TMwtSVz8RvqipN8kEHGvJrq-s0RbSTUyfdaODtPTONrQY33914N31ytq4tpinLMAo0SG-oGNPANJdCN7-xOc4vlH-J6t2XDrZ5vF6GuaGKpgKyDq9Whsb-f5cD_HXS3ZlUMIBcpjr8JPKOjHIYz2i-IgQoLEDsIz9RHBlVlFcFQmTcyppOji70aJTlspppborA90PWNoaN2xNVdMP6wJQzXOZrqe-yzJwBhL87-SJyyWOZHIFbnpGIUfrD9WM_CYR4lkVQXNFDBhB3WSkpiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go77RYcIgWCvVZQ_TS4jOvg-3dAn1p5AZScdfeHMenKVPRIKGaYGTeaHUWygGvb4LrK_4fxwzfrHAlBox-vaj04jkF_tRZgV4I8iGygtD7amBn16snv5Nc-C9bInY2VBM4MkLL1onKtx0ZZBQFxnbGF9iDFifzK24a-8r4mE0y4KT96gDOqXjBBTBa6k9CGKzi45a7UmoWrS3JdpNU_h8iba5j2T8V0Jw5KJHsA60Z8ys8_IaJV4BTomJOEr7J9LqBYIwR_aX5XNLafFfBXLFJDCmaU-5lJseFgN7DxdhUWvIZbqSxxaPRq4euXp2F1ySjgpebtwxMtmnTeD3PDqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqoeMlHE3TkhNOPyDVaqBdCOj_sQ65Qn_W8ioP8hiVSGz73BayvsFtINsx-DLVMmIUiubNeGSKRMWOarF4Ns2G95dYv1USXpIlBR7ophvWhCea2eBk7_E03e3eoAg4AhDyYgiOt_U8rzBLDf1JBda0gRE-xJW1BPvbIxrH873LdAf-JW2sFQdPjTucjaAoT8QIjvQ-M20abjYbUEgaDOk_adPgsG68yr34Mm_O-Z4yOeH0naaTScW-31BZ4HUke0r_4oF25YKvxUY77jmpPstZCAVbpdlGAmih5sOuQm_JO0HYg4V861ASFVforwYbPar_iGW3vnnKD0JkcOfoZwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpKPQuY7hxwal9Kt1wo43oid6kjd_8_Bagb1IlHnNtSAs6KXBtEPMHdyNYFOFUoLeY8W0BB20gTJORAnGGgbZQZ8XPMikR9DliLch1iQB2ClFsatJpK60USE9BKp8cbDcy1_WOjDn8bKaGlgjZ5SDlcrSFb5WZpnqTugfqvC1kUDA8_tICnWRxXcrwdz3y1coiFNegTnvd7dKsGwri0PPZRAOiTA3hbxQmiQ1ZTyDrIvQStQ-FJQ3F-cGNa-e16VAbZ-C5duQKytiiN3VbFE_kMGAJdvS4qSTJcXtDFw0Cn0PbDmbg1WU0vmJHqyFj140W2NqjHmjP4bo14jvz9vWQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpKPQuY7hxwal9Kt1wo43oid6kjd_8_Bagb1IlHnNtSAs6KXBtEPMHdyNYFOFUoLeY8W0BB20gTJORAnGGgbZQZ8XPMikR9DliLch1iQB2ClFsatJpK60USE9BKp8cbDcy1_WOjDn8bKaGlgjZ5SDlcrSFb5WZpnqTugfqvC1kUDA8_tICnWRxXcrwdz3y1coiFNegTnvd7dKsGwri0PPZRAOiTA3hbxQmiQ1ZTyDrIvQStQ-FJQ3F-cGNa-e16VAbZ-C5duQKytiiN3VbFE_kMGAJdvS4qSTJcXtDFw0Cn0PbDmbg1WU0vmJHqyFj140W2NqjHmjP4bo14jvz9vWQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJC5UFLtIHlLDOq0J-2eGjn1AaExKa5y4e67jNcdQdYqQeFnR8dK56cuIBML3NrdxfbYrjLCZQI-Php0F6GKMzw5y33YXRAfdTkJk8D7sfiXErL3krcb17EDGG2G_GLvSZ6blQZzEAc9rKLBmGb7RrjXLg-2xv8vWvCMoWhJafAAVTFWjnDSQo_mtbqsb5gAXZzCOkjEkrHgB1md7VVFzSaFBbc4aYJKAuL_9pGQa-cSgTYW4jZxj8-d5M3wTVGwAojm_mjFAsFemX0YK5Wcgc0qqm7sBnJSNXgZ73nttYHVSoD3o8Bsl-FrwKLFgcmJsHahOkqYq5W4lIzqaig82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOp9DMxfHfa_y7H9nJRqcQG7zezK2LSXXG7s9iE-_S177je3sVIbMMYg3onMks9vk2NhcTCVhy-rtUKjGVKctji_G1iyse4XnZsSrbiuXIoE-plgV1XP2JVDs-Sqvl_XvCiX6av74gLFf9RBjz8Xt4cShj04NsR9pRMFmqQ3IrGhO2SWk4iD4hoJkAHVMZHEnnjl9S0s0s6U6f8kDYNvLlq2HutHqFb8f0rqfJJNLdWWyqs1EXuKkSHVQACQyJyKZWZOZpUrJtfqkX9Xhrtj5nMch7vByQ8qtzGVQ85oloWJ0MB1URoQ8okXpGqEp7d561wTUmo_CuBsaQ5jzoBw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQs7aKRut4Udi0EQKZBJfjVQHRNQbbML7_sRDTtWWlDWe13Mn3n8j_9Z0d2wh2ZRz-KSj9rIxszpis5MLTAUpc2EdyeGlkshx2jKEAdzvq1OABWg98gz3MSk614vgBOW7Zl_SL-FAZmQSP80YD7GGwGVPsckQ_ECTKbYxBU37hdPUv0C0AFdgCZsT84vQ30yBSl5WtG0YGONyjBT9GpJ7zcat8NbjNzAzpmKQL1rmu20QeQc7YoVyqi-ZGfw5uHMBOortP-pRfiYjmLxIlAYigH3BKdpbL_-ZhcKQ_Qwanek6WnOhS7UEiQw1me1-vQ4d8LCIDTcWC811RWAyVAiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=UFq3ipQBrd8llrR0QUf51YzTM-251MoGnGoWQIgMoiUJbfwPFYI-6GJCo2xLbI2kQmfu4aN5Cb_u-nhIVCZ-rsf3fTJuBqUAmxtC8FvFdYJAq6xGNag_4FvRvOjRyM5VD1PaBRZ2VzSA6tTmSDr-5wo2XEMC6rKVDGQkH77S3LnUVlF87Fl2NkX9O4jff1LZqYXtwNRh-0DxzxGkwbjozBaTe2ju9dMdg6HiWhEIT4aKGELXPhfBPcvimYUgDG0XT4fcxHnT32gWMiW5vMjMvCk8HFYE0vCBks3yWAB5D6C6li_3y5eDNFp9kocXKUib4h7TOtPO2u9KRZ979RXcJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=UFq3ipQBrd8llrR0QUf51YzTM-251MoGnGoWQIgMoiUJbfwPFYI-6GJCo2xLbI2kQmfu4aN5Cb_u-nhIVCZ-rsf3fTJuBqUAmxtC8FvFdYJAq6xGNag_4FvRvOjRyM5VD1PaBRZ2VzSA6tTmSDr-5wo2XEMC6rKVDGQkH77S3LnUVlF87Fl2NkX9O4jff1LZqYXtwNRh-0DxzxGkwbjozBaTe2ju9dMdg6HiWhEIT4aKGELXPhfBPcvimYUgDG0XT4fcxHnT32gWMiW5vMjMvCk8HFYE0vCBks3yWAB5D6C6li_3y5eDNFp9kocXKUib4h7TOtPO2u9KRZ979RXcJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=aWxQrxbq9ZMAuFZJBCE2t4nvaaALUE_CKYhC00dQya5Bn4xVv0mTXPsVlq5-Et-VKPM1QOGAyS37JRTn9x9CcFxL12vSFUETHfGhqMgd1xUSxW0LGgeqeHKHWekHl1ZcN5wYtFDurtzmE8AcOUiMOZWLlaEAm7ogJL_mejXdbzolVhBl0rLaviuFwL-0GHFvjqHr6CmUtMEiNAFWZ3p8aZnJxwzsNWAYWSoe0SRstNcH90naQOpjaNmPdNKG18JvqsJEqxHgXUGUo-tvHumbA54IzK6OSyWAp3T1LRfl44U8FWibJ1wPWLznRtREAc9lnkJIbXRAV5mDCiAYsg8QVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=aWxQrxbq9ZMAuFZJBCE2t4nvaaALUE_CKYhC00dQya5Bn4xVv0mTXPsVlq5-Et-VKPM1QOGAyS37JRTn9x9CcFxL12vSFUETHfGhqMgd1xUSxW0LGgeqeHKHWekHl1ZcN5wYtFDurtzmE8AcOUiMOZWLlaEAm7ogJL_mejXdbzolVhBl0rLaviuFwL-0GHFvjqHr6CmUtMEiNAFWZ3p8aZnJxwzsNWAYWSoe0SRstNcH90naQOpjaNmPdNKG18JvqsJEqxHgXUGUo-tvHumbA54IzK6OSyWAp3T1LRfl44U8FWibJ1wPWLznRtREAc9lnkJIbXRAV5mDCiAYsg8QVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCC9OhFt0sPA4Ygs5NHE7drI_ZHM5jZqKAtcPZ6eHqJd6Ls4E1pEVrPnaM_WUiJWkHX--ZpxFJ878lOsOfokg9QfrH3WAdXg1mpSm49uMjE_Exda-ROA0e6TTxeN07NLZ7sak9gilU_QB-IyKHk-6jvguIO7QKhmVJ3jYezuBwh56R-lHrGjuhIr8v4aS9rROMoVPUxLAZT3hQRg0X2_f-tUGQrmcSZlroX6jclcdh-8OXxvLE49W6EKEtIr85D0PwKj3uaw76XZpFnGjUX6zTfok6DHCeDJ0krhVuW-zYqkaf_ne5-THdhbAVwky6_LoR-poegFY7V5B964_aN1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtWryRGlsDRFggO8dc9bh0FLqUoNIjmLbfE_1_GbuJfSHiuU_pxTe22ugVx_TZXFiFAAPD5cK-Tw4G9gGUkPz6TxLmXoh8YLru1qZGQRHIkUevgzDBe5oWVJrbE4KJrb2XkmHo0vMawk0hoL2cuVx1EZ9KdW0iiQ7SBxMeWYxflxrqGIjh8JaM9WLN4Q8yUXqyaqFe1Fk5R0rrKNXlYHH5Diz1HU9rWw4eUD6TxS6ZuWKVVG0VxjKq1oc8GeXPpty3Q_S5Dp30FzuV7lqCw4mE1W4uVDtUl7Ryd_RfYgJFNCW-wkhSL-5KKYt5cY3Q5EkXNpAyyXNzRgQ4Klzetduw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkWRv0JjIdB92fAfdgokmfYrxyg2_Uww43pmeDkyDhVDsvvAqp4AsTwAKlCLnmci_hMPJGSVxZ1eImdd7SPC7qokuuiGt77fNsN07wdEFAgk5BAd5_os35NbROfWq2gqPdDDpAq6U1IpIU7-_EJPVgXE_wZPSgBpmXH4zT3LIsRZn1llYW_Mrk2_vbAip0f4ktRL9ZhitbWcLFnQKiDLgIcOFQSeyEsuViPWE3Z8usvBfZwKRlb5RSLJ1CTonoM34DyctETs2wLqlQV_HRBayHB0kBho_hzVi8nq_RnIwYz3LrpLqWf3txLccI_XJcLiY9df7EEP6N-SCKsXB5iiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIW0oFgQX1U9jdsepVvIzlm-akTsEK_6fezY5A72LFuZ4goai2Qtz9baEbGlNHz3uvXzmU1Cvd3UQ0GJpcUTnVykbW7K8nVatPc-oSmZCjboZCusznFPtMp60bRthVxOqnv6EoJJjwwLozDfNoRzykXuKGPciOZWczRluTMveJmQNoAuIX-vsnyyahyfgbgnPq9qEVZIOShgsSMDAHSxwD-ZHXYtXvzgwIBEAnpB2QL2qZsnEMX1nhTPnlSiELz1Z3qiIdgJN_cJChOrwhDJdtusW898sM9dxPNC8d9Wmw3E0HP_jh1PYDnWKZHdUkfEgMPZMXDTWcglhLUIRLLJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta1Hoc1NPbFlE3VIv4QL-2Uf9_4LE1YX4c0SzS9N3mRqI9kBqQUq1CK9YimPPB49GR267TTc_IJ8j8-y3HTMHyyb2QCT4aO7MVSpJL5ZdNAspiQO0Z7NzaB_czKSi8JB9bjqrQylSl3o8Z1xJX7d_MoKvuWMQZNzeaAv8PAED4CFcn10nR-syKFEFtztg91iVEzltswbTNFQPcwDZPK6Gnj8_od20BxFMeYDkQimuM0m8qvMWU0sKzf1WXtdl4aY5388OAEocz4s2SQ0bTLeXg3YwNxg36n_KFJHAo_0gvUvJRNfVefo11jE_4zCGkOXYwdGb19pWTqjomNL60qrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY-O4S-p170jF45-ahUmkFq_GDcy5ZvLXKM7TuMSoI6jO--jo1zHU3KJesj2aAnaNVycZv9xvsq_Qai7csZq3n3smziWaxPMiIA2jl8p0CnfalbbHQN53AxqU6do6ZdUk_2hUhP35ezuW31iVNwHMd-OpcOYl0lBm5TNo9nzRBNGzbxaiaRmB0rbHevZoQ_c7z3SUeoeIetcx1ZicSUYTwVCZMhMd41KHowZnSyrGXPnlLs5cwD-VBBp3Qr-eke7kGj-NB_ltFYX-jBocAyZHaMU4gXtJThcl4yMtmAB3My0_ZTEAuNnjl8p-JN47C0XN19M1yTThr1hA2_oqy4gDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF0muo2IKfYMvLhhPUy9zQVblkmvZrmcnMVQezeP4ucH5wf_2viv5D4I7fWm-hoDn6MP0VdGIVBmtGtQAeOvZ8iy1hkbpFXZ7OxGeeNwEk7gxumsnSrXUxcAW5-JyKAQQueT_MY8N9PtV7wLFZXJ92hmov4Qjpy_uSt5nZQbd9iONrW19tra6TLHVHWFaY8P5P5u2G7KJT6RRESKuf2OnQggfXoMaHmhozdgci7cKPhPysfwkXECjeHAxubAozP6WoJHSVTVCW1PL_qppTYDsdDcJdPXMxPXUjsDY1f0NnZ5zev2tR8p9gBPybVLKFJndEH6OO-lPpnjYBF4Ry7otw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVGCOZdysRCCmNAMLPKKLuDm7BUphE2lKGfbh8hWd2C7V8aoyj1FUylne-ZJe8WMqqwAVxByQ6hv7ARrN6JduC5Yb9jsFVIWq-qMbHdV8y0s77LAbzYUWtC3JtOxlTsVDVG7TPT2y0ObZ_KsJ_oYFgUFbAjI-TEptdqtsYHBr3TKVCbQS40_dDYSA98XNFWAsMqxDziJqLI4DK0lLSYujZduUFa7UPsa7WPIIaSOnhctSUxFCKPUaLuaaOXcP2jEdo85dbmG3OpbG8XuxtueGZau2cuEvw8a5tP1sg7WEe4x20nVLyt-HLeHGZdkmEsMzf7hNfXBWf3zIXmJjqnGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7jr3BbHeJSH_W3AbPYsZugFYPbbuO8wcxV7qDG5EzpwOK5mbIS_qTh10FlbPbBzntyFE1vZsSlpGLPzRorzYOqnD_FCKMG2ATDYCmDr3vEeGoiwBZITPa3zIqimVd4aIZ44q5BX2itOxll4C8WvHowGzI3qNEqWMygcsqVI1Unb132WD8pN7UXEa00AbNwOluFM0y1l5LvOfie1Mzqfp5qLGLBtus0EKMJrWjGJGmhIOESfu6y0p8LQwyPkoHsR8IJF-YuIFa3EL8GxnHHsqjoNz4x3D47CDcdkw2q3UQUl9uVwRtAYVoTaCS6FJpa77J8jecgSOe_IvkBDNPxy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyNV8oQJsL-2txYPL_OqQnTEhIkdNGXjl8KhjVxJMHpc8_Rgtj5LhIkNtNU2DJxngItakvij4vGCxih66X9TacWUqhjQiUdgi6zeZxyv63S1pMQz7t-Nfaz3cOyO2EKcDyqx4UC0rWMGx8arfqHiczwvy3Wd9x4nx72qXgdgckFEOTm-OlWKHl7iY4lMpJJLBJbNrCKWRsIf3k84qJdimj8nLlM1_RuyC2lGq6pb3GPlIxQ168FLh8sMxoN5LuFcyO2vSyaRQbsoqPUE4JqR5R84fQU9TGvruPop_jnh-iyOQzfwgVfBgmHD73cm1mB67DpirNxuiB1qrAROdSR0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhdzGcCfILj78ugMaSZGpWW0jadKtXl7f8YUp84hBlr-edcFdKG28MkRpn6OJbN0mrm9Xg1PbBJ-bDmsFWw-a8A37LQX0s2edJybugDdRa8zIYyAAGKHbfbfGyoQNkTfibQvlBsvw7wEhZoeNqoqENgIK3n-UzTpv4vfqHr-Fu-juake-Wne5JE_nTyJEHh0I-cacOglAhTyaaZF13alETxmBAlrKII6Ucb4NK9cMrQZvCmiNBZCiSZUdxO3MCE4hr1f6QyjPMeiig3UE4QPNrxr1ApesefBn2P6mYnZbNAquB_gKEqzhGwAM0fBGDwthKIn0wWABOeyCLeqZ5nPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISOdcstdI-e5B9LtpqYsYTgkUeLz4alL5DUsvOHTxlf8MJagZlsQBqE4V45Xxo9kSrRdcz9nYJePYuEF_mfWCLa-UcqM5e21-fdQg7u36p1FNkDPn4q0tRI7WyBu-N-DekDTB9z6Bnv9TWYsflOfDUld4BW-yy7odCVYRfo3b1xwMwjFVFim8xYOQZSWTbnMRTI7bjfMKdJg7Dlmiw5JEf-R3q33eODUMiD8mIWIPHpxB4F3VCm4yuknjKnBfz1Jq8KguqvL1WXkrBkyvc-THAUnVgg8E4q6pgH8iurFLwzYNZUYtvCCdGHgnLZx-D52r6yNj4QrdkwRDLOdJMTLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzY9LvWXkje9TbljBjUU6A91mJpGktEWLpRVcJ6VMsZxvc5c9biHXBUC4TlThVBlBzIa6WyzkeFFgTKdQNg4BskKss1gMaVokzOdpBoeYPavL2V9o5jquNh7AdQDvsfUfV9YBgKW0Lzy1cPyWipVVb7HB9jiO87KTrmkO2sjgHiWWsP25558xrl-Z5J7A4-HvYC918ju_CdWk1AEq-DTBXJWCsw59yI7iD-gdK4syTdNAdudZ5n-4GolqdZCspuOsIUP1KqTHtbKhRk4IehNCFtWy4qr15AzaZOd_1WHe7etwgNj0N6ek7wDmxeBD8gJFWmJ6ZcpRyiIQ-Qi9_zqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqWTtcdfNEjYttSSzU4XG28wk0PqvdW5EpmbfCTBcUj-X9h4vSFRxfkxMMBKg45nIrG5rsN1_bGCwlWToPvQUV_Ds7frX7siYVdnZqMXRm1Pm3QSF-eeKev04gES8coPCMWGGbXIk7N5_yqj69XX9iWJj_bu-_p6ssj-Am-cq-kLOOx4sGFuJ05e9zdIqVkmU6e8riz5KSrhlObrlpG3wCWcl-0SrpF3q4YL9Bo2tDUIywT2JbYaz6D6wAg484n5rTavse9V5aK9OtefhgelckvJySK8rmDLarUWqQ96HfkdOopvhtKHk4rmx-hvnq2Zn6btFLCjiOm0Hno1P9lZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD2WV6LKOyBiQXNBDkapgT6dvUoxWjiSK9VIkerfNXedzj1eEsY6ugjt3yIHVT5Fo72hsW9GSHdhXcQqKRyBaRI8tzA2T93ijEwx7F7sM__AFIAjhzkSFLdZRfKzJr4ihU15Nh_LIW5Gctb9f1PLjsldjCC_pNghQ4PglBft6qt9364b-MbPG7h39nTQm0K-PuRQo_oiTECV33cIO1DR9XDRcSt4r-3Gw23AO96DL0zPNxMqcspiUsqd2HesL3X5U2iWHe10FxvP-aVplO00uG1rNwWC1kNxdKrGx6hpVgjknFV1vdD8N_UlIsrd5ZrX1V74mvfPSbHm_vFefl9tJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA1hNzOcfv9J0LKdg9Vo1PwMjVPa-F5pVbxweKLQhZ_tqqGQbc1WB0C5ZP6kjKyKvRfyspyjcvPlaBO2NCuDxv1RzPhkkm52nHrjy8XOWuB3WSEzJ0IeEmJqP_GJMxcxIufDZ17AH0_00Whr3-ekPkm9-E7oS_l7Mav5sehjOm-vTJCXTBkyFZfTPZtAYyPTzMzn53lIpxr7LQYzhlIyd9OX3CJeIfSK6MdsYAGDSFNEr-Iw8zpF70dCFSnelQCbqvu3PhsHpdF2hT41BI2X5Nc2MNBvlFbvpdh_UjfnpPywIjRKuCyKHc5Rr_S9gCfFESlqi4hopOmO7thzl8VMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_7D2wolFvtRFL2pktx9M-v7hLcS-01oFGNUdusSvtS7de2bzbgu7CcjEifqWjdtezuuMnpv9ct1SMzzDnFVoNLJHSnhOTkN2AmVoAC6uu8Kr0aWKjfSH8Qw2RE3wFflFv9Fcq0anautp5-fMm1IOwh7oiA3Ro-0Y1qHD7qVENzlkvkmNdKnfb7BfXI4r6TaRzYHce66XBgyWVadrDWpPqB0oEarmrXIA_sL8slAD-aXXtivzf1jxlWzN5B2IFkIk533XqVRUYvfYRmmjuegZaKmzjO4orYSD2m2rXaglCzLDV8ftZsaMsDAFlgPxLb39LxohxNpsLLq7TFTnEkxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkO-Ba48AlGJH3oOhG73zW6OBOdNO0MwJHByMVtJg_atQHNjadR8vqavz4ALFIN6cGfhSGC0IFgMOfaqXWvU_PlhX6FP4eWBgKZzKH4v074rRVQDhRgWZLZPOJaTRxdMghcllTQdbGJ77laqGjg6Ol7op_a5RifmOhKnQEU46YC2bE22Lj-iuox4-xKJMo78LpTp8_hUZFHvaYjIwiONeU5AroFQ2a8yuR9yFQ9tujWi21yuB7H5XMb6SBRFf0-NKmbvMYxC7HVByYnqC-E0n0vTvFf7nejT2AbuCXtec0XeQHvqA0j7lkstdqmQEc70oyIEX5vkbXkuetPVubPiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQubczjSJOHLUHqcdIG4wdyjNRa91IsoUN8ytjvM6fKmqV5A02MWCunEZ2OuSk1SwNBNQrLBtv3t8DN6O8iTYQYsO-NIrMyZwl1msSscfoWzSbLtSfI6HPmV3iCD-waLGMshZIc6Bg9zzIrJz-s-LDS9fY-TFbK7sCRMcGZH1j6SVsnfkDyR_XcEvlBQeJvQJKB3M3wsL3rFD14_0j0lSCprl7J_UAPZy61KIfYuX0HTPHFRkJpeg-PVjPtM2JqzQFxb4y7orIpdAMAcwG77Mgs44tEbn-IwVnw526ygg-vQrVHE07bmZleeAaTYkGcGwVbCNQoiApo0h78IB4v3Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5Tk_YplwQJujNLVGMtaUlEeiWROF2RFsdykbTfVnjs6mJ2WOExC4q6tFwVAck-5u2N21G9st_mlJfvvAp3TnMD7JJJ_k4_Wr2Vo7Yg7INwiy1nhRTERkp3oM2a1iMAnsWOhph_zXvU1E3sida0yumET-VxP3jzxFiuLOsB8sMByUTxEINL0uyLTjiCHkZdwmOB6LtQpTEFfXj-Cu3NI6VANlvBN8vMfoVNbNdk8pbzAABpXHIC3YILgufXP-c6TCQ5WWTuayKwg1n_PCv6-tCZ96aMzDW_DY6Y7eo5bLcpeRyMLYXX1hGorDW4acGx-TCAinrW64Q3XS1BACYTXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqCeZBDGFBGZImj6C9qQ0zCjSFjcmG-8-TW4LgxE8oE_fe880cBLyMS9LbyJPAANgX8rnViNQmCaBYpBRJydGHqahWLtWnuglryQ1gBuogWUL4V4zGdWam_pgjJy1r7pztmUlerl4SloP6FOu7CBfXtH6hXq2SQQK-9KwFg2fra9yQwihNmbCp6c8XOC7pwz5tLmS4Qr07KOx2_Uy8_92_h5WN6lwR3pPzO1pys_-YfoQYwK2bw6L1iN5sKxYiYfi41B-P_DxoQMUfVOFDa0BpYt7AC2eTT9zp-el_FzDB1xA3PGAl2cfQILEI24Tjpo_PUkbXWmy88c0JgCwNvwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=fnuWv37caZQjB5bxIouL1zXegJKZ8stU0YJfAYijvbcL7xAMADZemLP75tv4zlCR5xqBgXSQJWUtC4JxO_jwDTGwZVRCiS465nBy4gdY4AMJUXDRVijLeHssI-yHmBSU9HjP30E_61YZiyaYdk3F1cRN_m2dlXGwVK7sexo81FDPGvEmCEilYhClogM9Zyd7bg2ScUfmMg9aXxFTU_D3a4ZkvAw7Hw9N_SZg5Tjnsl7YnRaQR3LAO_f3d58RcUCLKuRh9058pX-tDmPCyZFlngLamzIs4wFr7botH30svl5elAJiK8TOYyOL99LI7u_J69uPvmYKl2xTRyE-bP_Agg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=fnuWv37caZQjB5bxIouL1zXegJKZ8stU0YJfAYijvbcL7xAMADZemLP75tv4zlCR5xqBgXSQJWUtC4JxO_jwDTGwZVRCiS465nBy4gdY4AMJUXDRVijLeHssI-yHmBSU9HjP30E_61YZiyaYdk3F1cRN_m2dlXGwVK7sexo81FDPGvEmCEilYhClogM9Zyd7bg2ScUfmMg9aXxFTU_D3a4ZkvAw7Hw9N_SZg5Tjnsl7YnRaQR3LAO_f3d58RcUCLKuRh9058pX-tDmPCyZFlngLamzIs4wFr7botH30svl5elAJiK8TOYyOL99LI7u_J69uPvmYKl2xTRyE-bP_Agg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPdfazcl-tFxflbh_GONZs7JDrsJiDZHdgq9vs2UCxFRkpPvfLZ0TlFA_wEI4apL1kt1n0xGXpf2vAap7ddoluYhNo0Iq3SsvrLYcnfCFURZxEQ8EJ7wsQ15eIMNf15mkKS9YvthNUV5G6Vp0D5AWnGKBi4GX8GEbu5pUlIG4sZAOi56UOuGL9WGFoD-3Xf6TBHSFrtktAaIITjeSSJNozg36FI9k-y5mB1EC59fYSxEs2izYEP1KCsL4OCduQwb-xES-WUN5Czi13Bnxvg1EmPD-7BBO3b252k2ltQUrGuIsyZIVesx6GsgWkGx3lpQSgJclQu3VcyaIL-Pzphv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ia8N974875B-ozEpChknGW-ebaHhmSxMM7OoO6kHX0BgiMwPEzTqIifQJtnz18Ak6TmHdJyA-HfSYgd7Q_n0DA40VIRzSqthN2tYIcIRzRaXYKlBiRGhRpklIYEm9W9unB5jJdUj1zaLx61x9i7ufc_IiltFoXo_mEd9SmImGrITQicN202rhGJCnYh3rKtqUduzhrIlGNJXWm9D3EEJfDKVTogL1Rshqex1sFu4qKWX26k_acCXrpEBPg_XHi4aM5nddTxSRgyKg_POV0qYnJUx5xOic6aYTu0El5vvmW1xLEuisZE8wv_lA2tLcwlV0Eu0YDIDRCXHFy_e4l-f3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGgJEhamHe3F2zwTs9_nkOA3KxNqyvRT8BKwGzh-cCQhzB6AuDp0Vyl2DTP9W0BTuYgLWoNfq1YwSM7yA7BwvofjfkTnD1_2-ev8GJqgV7I6YVRgGA80xAx0S2C0SvN6QBeXTEqhhaXY6vRqbg7V2T-9vOqtpGCRbgWhnjfWdrN1snhvJcdBbQhZ1g7l7Cz0q30O5gg9g1k8HL_GiaZ1iw8FUroWHq84V-o8_AHdu9kde4r-tD1pq7L42CL04JbIw2TSOMJhtv2mOJ665kJZFV1HjD79LpFfdOY3YaJjK_Fgsc8pC701Uh9GJFxmXDy9zqPQtA4vgvCitWJS00sHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnFnMlIPRG1nROAY8IKeKW9xHYhMpPKbSHaQQbMhnpcgPmeSaCrvPv3bvZiHnb9oC74FRbVLGQjNVuq56bXdrQ0mWuI33APxrjCQ2kHk6n3OHRlV79xc6zZsxiZjUrprMMqVe0bAYY48-IvG7tRZOq15tWF5rM_RhE0j9QHQvWZBOqdmDVRAhCSB_yG0lpOjrPBgD8iLz_ax4uUXjBds5SL6-TE3DXy_PTZGxG2Be807Ad6VQ_4vebM-y22W_eCqxwt1XR8o4ZlyewBU43kxF0WOSEWK6FyHFgb23wWBKL5a8DwkX-IwJGb-A0PHRtjWmEnOk2nvJJUQj9pFw_kEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3of8Iw0NRHHYlHsTI9fDOHuV-3aRh-g2YisHQuwQRXehLeyVxpWpKcZHwSHtCqUWUecFGQDzrVP05QK8jg4MsxM_relFoPPKgIyfYMNP3P3vQ8bzOLCXu4i1Lv0JNRCYBiv2tiL0_ys83eYHc0EjAmTL-I2IKk7AGbn5-IPmCApwTEuFoEq8GhBkFy5_6nsMcYO2vHJJd8f_y0zbJUfPRnSMWcoDIJCAQSaBnSXuSJwKPjPtJ8vjamZL8PDumKHIJjEmxHhubth3P3x-vErPRRhdgbBdGOooRH93hY16SGsCupw9_JgbCODkdao14ya0fQfooPoM_3vwJBZVgVLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9BRRPuCpTVcj1t-4oozzFYY2EKoNqHUP7EP2t3AQDBLZ_9BZ60NlHB0K6kdT49pd1PMJ41Y5qe5VMDKbdKR_ii1bWjpCZxVyavtFCOxeyk9aSwJrprt_VICmtFj7TimD0PrKMcvW5L_lnniJCtzFJlhCQPoojlV9mWYDcOVrXuK3jmb_OHBWiTt5wWfdijDHGL3asqSfaI2VeunuC1SWcDzErqlAeIjwL1S5PifVKi1U5IlW3GH-P6yDT8YWU6Szh4lkjHPwIw1HbmaSMTqWBvLvgGA3C5Njm7C4pBC765ixZCv1WMu_ZqJgNrN7QkZswWU75hrTXFDpkEXxYpThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e28p0nuT4pvs3Z1yZKkGi2Y8G29Lr_MX-fnJCMfQKdU9Y7Lm0-93vVw01EV_whMiDwaeaZz7y15VjcvoS6qjd4lfVpVO-TzIcdrVzKjuGHbsJrCvS8fbOd-Lxvtmm-zuCfzzwjISrvcMt0ekYY1ps5NEWqvbDsrIxavXc4-kAr0P4UlWJhXVROEXZ-Q0LbKMuj8NyYUy0TLF02RXYbNlg_42CGLFlrNSHb0z_wkYybwFhpa96E7CtCwJ-FJADRZwXw0hrCl0sBYvmw3ZuffUAYed04mF-_sWrubO1WtVvLDJs5aBV46EysSiY71Zqy1ZF3XFlS6e0Coh8AKnj4tFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czs4jmvMTmicCp3n_KwUQsAxB9IRb737NgqPKadIQr7wnyHg6bKHL_UpGs53QBAYphWRDvvp0lp_K8wTaWUywZlqOzRFufyC6cHXDldksFjcwJDo47eIomntsWFTFU6WMs1ljMtxliJLnwOOBF5drJqN1dJGivjo9TP6UUD4ZfappBoIWxct1ByaVqhxrmcJmNSS6YDj-ieIvfVVYKif1ZqcfGUg7OUONHCbigmdAfRJzcfzRHF4EOR0O0ppiK3Jh5SlPKZ4d5cgPYwTLMX-d5wyem_oNmI52tXm82uRORvKrL0hCE8YiOTUVf6pxze3LhBUytBs-RTONw70rJcT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=pEM8amiuTmiRU5uiyPZNQIYwohB2QJeF58pnGiPhALDcy_XYMkFp2pGXHB4oEdHHxyOZG3zrir4a0Q4ROv8QuR6BjBbuOrVff46QIqpvlgsf_-Nkmi0-XZcw0sXCWsZK5hH7MRjYgm09P9BOegPbcqrYb3kOUT4fs4YvLmHk_YzZcvzlNT0GZLbGu8BhwJhU1V--a4q3d1INCTCd6XyFI604oolPIKF4qcPCoH3NSofrZJLfAT_tkTMHh3vOUNEy4DZqPsm7Yf49TWw6g0SJz_e86NxWh5Gyz8xyYLICj08oW-Mr7dgfeMXTJXxMHKbzXpzKkKlNRyxBOJyZeutjmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=pEM8amiuTmiRU5uiyPZNQIYwohB2QJeF58pnGiPhALDcy_XYMkFp2pGXHB4oEdHHxyOZG3zrir4a0Q4ROv8QuR6BjBbuOrVff46QIqpvlgsf_-Nkmi0-XZcw0sXCWsZK5hH7MRjYgm09P9BOegPbcqrYb3kOUT4fs4YvLmHk_YzZcvzlNT0GZLbGu8BhwJhU1V--a4q3d1INCTCd6XyFI604oolPIKF4qcPCoH3NSofrZJLfAT_tkTMHh3vOUNEy4DZqPsm7Yf49TWw6g0SJz_e86NxWh5Gyz8xyYLICj08oW-Mr7dgfeMXTJXxMHKbzXpzKkKlNRyxBOJyZeutjmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6rzECIdi28qPxfQAOMrPmiv8pxTIQIhcrwRp2W2PYzCqhAQKmD5q1Sw6rBfHBHiYTw7KkUgYaFxh7mogoDVExW5MODYuVF2KQcLViZh98yyIUXY4z7xyBpNrA-xLCGvt_ngaQzEkuFQ2Pg3uC7Ydbz-fWtfvkeFYMvH9G7DrTOGPmB_bcjWEDQjdlVuNmSA_c3MXsBcO9-rrjDhjmdrzc2NVLvmwoVgn1dOnFwFcSCZxoUn8Jm5rZlin_NA35Jh07NQZHnXkj1so6bVptNUOEjVwYa2-T35_i6zEKHC1I9m9xq-9guPaJDUNpVxFr6atr5VBCWxckvQMIuIFy8lNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=JHBiuiMET4rPXjRjOETTBoB9fx8xaKgLECpksALgQbMq-UCKYoiGjvX6Cgh56A6eTU9W_a0Z34LJYnxxDAejgQR19MZmzAIOShWIOWqNUxtwXGuoINuiwc2_4NzKb3YSywRhgKXASRwOV_3bbFmES0FgpcPIVZC6bniv1oPtNwVLpz1mRapkU0Ru5d9KZnewHW_27qx3JB4K5-JU_4seZ6cOHMJDRgQS3-NOpBs4YIrzQnZUaophfF80f3ua323rJonGvnWFUNv0fO7LoU1i_FVX_E8UgXQr7xRiBzrl9J7egzK9wRm-CybnFSiZ6A1TqjRhhVz_dB1YtlwPXz4HOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=JHBiuiMET4rPXjRjOETTBoB9fx8xaKgLECpksALgQbMq-UCKYoiGjvX6Cgh56A6eTU9W_a0Z34LJYnxxDAejgQR19MZmzAIOShWIOWqNUxtwXGuoINuiwc2_4NzKb3YSywRhgKXASRwOV_3bbFmES0FgpcPIVZC6bniv1oPtNwVLpz1mRapkU0Ru5d9KZnewHW_27qx3JB4K5-JU_4seZ6cOHMJDRgQS3-NOpBs4YIrzQnZUaophfF80f3ua323rJonGvnWFUNv0fO7LoU1i_FVX_E8UgXQr7xRiBzrl9J7egzK9wRm-CybnFSiZ6A1TqjRhhVz_dB1YtlwPXz4HOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=d-cTwVJs-OqfwW1p9iCm_qkz1O9MJYnzPCJ1NkKGrNW5Gy0WEbCHZijvFTnCPTCN1QrsezicmwNQUf2X-zozlRwHbj4cbvb9Q-gxQPiNrCguE4k-Wwo3vJSG8ANINvDJFeIq5rqcgFEKAT8LwwLVTNy6zMjKtTAfA8PJhjcALQUyeAq7YACdyvAH0AoXngHfut9q4Dd3SJ3LC6HQnMNk0vPuqjAjXeWa44yvfVtwPtDYoi57x-MKBP_JjHIIC4E_f83DYVx3GPRuyG-zfy5NXpKGt8JcnL_a1xOqcTgBdApcIr_G_TGAjjHZRjuvq2nsutn218RF0X-SNN5M6LyHkYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=d-cTwVJs-OqfwW1p9iCm_qkz1O9MJYnzPCJ1NkKGrNW5Gy0WEbCHZijvFTnCPTCN1QrsezicmwNQUf2X-zozlRwHbj4cbvb9Q-gxQPiNrCguE4k-Wwo3vJSG8ANINvDJFeIq5rqcgFEKAT8LwwLVTNy6zMjKtTAfA8PJhjcALQUyeAq7YACdyvAH0AoXngHfut9q4Dd3SJ3LC6HQnMNk0vPuqjAjXeWa44yvfVtwPtDYoi57x-MKBP_JjHIIC4E_f83DYVx3GPRuyG-zfy5NXpKGt8JcnL_a1xOqcTgBdApcIr_G_TGAjjHZRjuvq2nsutn218RF0X-SNN5M6LyHkYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=fcMqELcUMr9Py_wGIJ3sejEDGxKx6CKvW-RkXePvidOWqk_1qcRysKn8i5MftUe8BC-bjMK7wHLa7Iq4SHLmHeUlEY-nFCMXCi4R9Jkt9Uy2t8J-j3ZRGPoNUnm2vLZ7jq4N7SS7l6cg9gBDo_NrmzC5RLqsXWsUhfOGlfts90hGqGyW6BFKKLOL1hJ3diauNApsigJ4lkYlAhTcc7RfpSs_tCABHEMXbmkU-4IggRZnSxWcGWqxgHFC5y46p7-l7mD0abz8L4IaKNyNkd-HkS2pjC5M71e6z7Mp2VYpXo6bQCvSJv2Hm6Krdy0RwiNQ3aTn2xPXU6zjL-5tXCTvuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=fcMqELcUMr9Py_wGIJ3sejEDGxKx6CKvW-RkXePvidOWqk_1qcRysKn8i5MftUe8BC-bjMK7wHLa7Iq4SHLmHeUlEY-nFCMXCi4R9Jkt9Uy2t8J-j3ZRGPoNUnm2vLZ7jq4N7SS7l6cg9gBDo_NrmzC5RLqsXWsUhfOGlfts90hGqGyW6BFKKLOL1hJ3diauNApsigJ4lkYlAhTcc7RfpSs_tCABHEMXbmkU-4IggRZnSxWcGWqxgHFC5y46p7-l7mD0abz8L4IaKNyNkd-HkS2pjC5M71e6z7Mp2VYpXo6bQCvSJv2Hm6Krdy0RwiNQ3aTn2xPXU6zjL-5tXCTvuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNBxTHEN0dSi5QNaPnjqAbsBi6QovBfu9Y3OHvx6bxEV2PlNoFzhSC2DcnC3v3pftIw1mWRHpLpcEOJ4HArvYVkC1Q3lMb_izvl8XDS2eZ1URmpn2axQvKqyXtLp6zimg43dAIUJ9sODKaUHg593fm2q2dO_t4MbsKIQqX_PUVlGhBuf0xrWjjDrwmIDx2zFGVQ2q7ir9IdnGoyMqzJfjTQv0a3IqYdzBPK26m-q5DH-w78qdrcdfofdb375C9yN9_xIWtMbEQTJe4hyYfUc8pkDOur72gBojwT7xROHAKIRFXGdCiFBwrhtaCTWhwN8IatkuQJf03xdzGBJ_W3hIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sisISb-E36yk41JbMqM-qxTSs1F-THEOIl5mfJe0idDzIlxLAdMF6KqlBd4ycxnQ--9_XyuvIq0PVWIzyCiOMlsA6-Ef0ZoMr77TAaEAH-EhVptJ2ky1gHjBbhkAbC_0X4Sm-9tpYFHBmYiTyjsj5I3o32ccsZulIn9zcQ7TWdjxwj_h-e2iKWq4skxgzh0fu1xM-HKp5fIIsVKziwE9tm4Pv39h7rI7uaYOFXZRfB-qyqfbFfs1j55ZLB0OiZmhzdQkovww3-U2Vdshy2TEa0eSQOnQ8Uku9Z4cm-UARonA3Gh-VZ0HBRdl7lVzIhR2ko7dvDk6kfuVIFlRJMX8VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMrPC27nsQsHL2gMjKZGiFTRkxj3z7_9Ry7kuOCvyPm2fOLcRuoxWGmJA2l5MvIF_dRQPZ13nOzX4ae5O_m5sgf0hWBqRRRrqit_S9uSQMRBHgBy1A4MSd_D45K-s68fTO3hwfGXvYMOmk2W9RKSTIUcWq5uurphhpWMMTvPKWEYP5hwSrWshlf9W_WjioCxtO0m-Lt1g8h_YeCfIzFtaEV_y-KgjtJsuDOf1ljVJWr6fV8gyTOewcSYDf0SGEHX_xIht03a_eidBzw1SkuBpqcUjJ6AvuWJRKMaXebUahosKQK1zDzwarS7OKN0_nqNjt2VhcpVesXTFQkMDh6IMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIs9yUIIl4EWGx8SW3cH3Dm-UEmIGb_C1ru4Z0ftKKf4ynSb9Sg20NPaMQeG5wlG8b5Nrq0ofxmSc__ER8qH2psrnVgUNSrjBNXlYebsiXiCijng3a0vSop1mFFG8-nFCPOtrh1_3eRIuahirInkCsnvc595fV06C2uhEvgVVf8UOrTrVMDOJ0pMERukrTVxpjFmed2b6kFc3yr-Msg_QbNfcZ_c4UkO_qRmO7e4MLH21rgb-ydhUFSIzhchzEUfpo59uCNdanDwHzfAul7U0AYBk684beOzCJC7PPgoudZRJaM2lLmi_agL3g5MCyhFFpB6iYG-ulbPgB3d-yrtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=DDi4fl7Z17Th3ngw3dFZ8BYTwdkdDRRLHv_8b3Md5CP9H4Nd5T96T39hg7DL9aKcHls9_M_jC_g9_kCrJfl7oao8rj6js57x7aOFNhosqLJHt2MW8h7DhugxO_ptkBLPLbG2tgC3zykMnLVn-jIsvMD9C6iG0QTcJeShiuAGFDZj6ZXkj3c-TXzDGHhuaA-IKGtaiGy9ZcsIrhv07pq0VSefd0SVyB2F_Wma3SUX0ZQS_MnGgwhbbOljE7B8KLyRMl0EyjRvpKZMTRCk_4nqvaq1nVhVJw3iV9FRwjR0lZjmgfjkmo3oX96NqK1QXrwFo_40s2E9MHEGGHuiKW6OsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=DDi4fl7Z17Th3ngw3dFZ8BYTwdkdDRRLHv_8b3Md5CP9H4Nd5T96T39hg7DL9aKcHls9_M_jC_g9_kCrJfl7oao8rj6js57x7aOFNhosqLJHt2MW8h7DhugxO_ptkBLPLbG2tgC3zykMnLVn-jIsvMD9C6iG0QTcJeShiuAGFDZj6ZXkj3c-TXzDGHhuaA-IKGtaiGy9ZcsIrhv07pq0VSefd0SVyB2F_Wma3SUX0ZQS_MnGgwhbbOljE7B8KLyRMl0EyjRvpKZMTRCk_4nqvaq1nVhVJw3iV9FRwjR0lZjmgfjkmo3oX96NqK1QXrwFo_40s2E9MHEGGHuiKW6OsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGK1a14v-PXmXhzQdmp68jTY0Stg-gzLLkfeZv2ZBWVfXlUbID3i3-9KTdn_-3lr-tzfaV71Yy9jqmneQsf8pNyYS8_KtqDwdQAVAEWbpICQpfq330iiFw23nlpDOvePxK-kJ6i2kZRb7YaAcoobcQRe-f0SF-XOBU0D-Z96m0q23dQLlILmRMs2F5b3cZetISNkWmyWqgXGnXNfb3wUHyBBybN6Cwf7wqCrlc8qadGkFZfzrNiSR5ob449VRJdxKtR7NVitdOpRhThkCvMfJR2kALdTrxD412QRt2qEN6jTzqjkjqsbpm-6oDTcPvssOrq8uRy1Ri_Ak5C92mvrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2tS5gTLA00gWkp73sjX8QaBewJdiZ7OmfKbmMs2gepXs-xffP1OurXosQpGzzFcGJ_shAqCutVuacz_hBQq0-BEY8sRWgJG3MOXCRXpemtVMZr-PDD4SnlPi3_goaSKvtnT9ZOy8LQx7N8pdC75O8oqnA6ADZqWSkdWCjWcfKOjJ-rF6BNGOwJfKWkkmzohE30hy2CZ64H2O2N_BgNUYgiy4XG6iDLl2DICnZHjScnZULeZlJjOfEUvSKis9pp0p7z8PONZ41W2Cqb6yucfBLPfq5bsE0FNHy2G4Feaetc0Ua7pYw6YndFqGCUC1HtVaT8dEbRBE1Z54ta4MNJvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_kb07lWskascTGxtulbcdNoTwDVQuw3QXjTI1j7_N1Scpz3stJUewuV39rOZMB05wRz9FVn7CKCFLEyb-VrJOL5x-WBFG1jeYbFr7CAZC0XOcHX1kGZQbQbPm2e7vF9nwgjrJHlJSc-Tr5Ehw7sS9xGtCosN436KUmmL0eT5aV8bUGphKpel9-kOCYyi9WE4yGOTD18FcIf1v16WGNmnDC8EabrSdXfzonoIisDQ03vTzgSCVxSTnd5iVWs39o7eZWrwW9n94j7LaVYmYJvReZX6HZGvBFA6AAXqof3Kxdr-qZkZWQAw7RTJ3CUxMChAO2CkW_NRSZsn6IesTQfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJxSi-z_pvoV-ktbZeb8pxHk_YultB17PAQ6ONKwycCXBNzukUnL_DAK01sIqVog64NHaP3i5TsIS_eLsK4m-TqwGiYJEc2O37yXhJ4EEKzuq3E2vYBXHqSJHNqhxt75WtsDVYy0v7Pee3oFr7Aeu23SDkXf0F378ynKMagF_iQqhZvD3bYPFsDqQCOvBr6odMIlO0gihHPmrh-zALnAMyiq1OI9WKxwmk0x2AweWzEGC-6o0Jj2s9Xiivy6-N9wRS8JI0T6OKwrkR_BiGtGG7RbxBlhMw1hP6F0OpNWccrBm30hRjQz0FrMpn7yNQ5Mj_HxdKJ-smYhMXPb7fLeuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVt1KcpA2UCbnQEj1FUPtOtxP93gnMHWtuf4C0hzursUoRXjsq7Vz8CyUZ44NapxpvMP9SM49UL_dR_HeiLn_IEnqIHjyIGYJDXF-OBGd7B10D-6NJ6DVqugS7_BT1SA7yRhCwG40RfiO_jDHO8hEKLacp33WEbfpt7QH0VdwAOmFhMwyrq8AgF2AVvo7Tg3dMYxX3WGTI0uMPwKO940ny-GZyIviO6a-nISGYQgDnKDCtf9YDSuudjMW7lgVx98XJtRgNMaj98WJhvsfCynBd85l6dE0FvmPVw8MMqHeAneQzhR3DzmBTL1Q5OD2KUuSaLyQ1VQhT5Owrm3ySJhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhwJgjAvKRDq3ikAOrNkbNBqy_J9jBmhvpm8oTh_jJfKqe2yoRyx9umqr3satZeC88kA0OJDSFitf4FVYwG9F1taEv0an9Lcnr-ov42R274-3qocM_aVF3A4W_5tMXGTZoSzo3RQqGoJhg4B9KM7b548_E1gkvHcCR6aPl6vUegCM4Kmda-j8K8AxOOEoPyEHpiTadqhkAg_TrjkzEIe5562EcD2sfYHhfr2HJQLRDfaOZ6txymOSWcaXVVMcW0yaxAq1YO5ulbhSk80wrWHelFgyI0ociF1ohn-gHvrNWVa63NvinEcIDupEWJG6EHbjR45TgLQfnOLFY_WYJCIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=kE9cMri4uPvO6XOR5l9HjkdqaH-3fXLhNo9H_KeVvez14KyyORv3lunhtpnxgZrsH-ddtZtPv9mIws3E-t23E8WsXFxYuPSWT-ju0cIH7qoqcVj2_so6NQ3FsbQUgrfP2gzT8XRbHP_lUVshnGZhRiyLPbD0Rk1h-yyRozvujwDUCMAOIUz1WdJSTnHkV0qxzhmYbq0bA3BVs-PIDMkmxcrhB6rl4Up_eblTw9AMVHQzd0g3apYCEsVT_7OT1gwNMlCoH2MAzu6qYfrWCSIMkOQakpUBEO6Oh1dvrVpdI4bHhSv4Zwuhg-vRQ5i9iBSbTKjFy07sln9iokCuE-dfiIhEtEz8IpIJ-bviwMuW2lkT-F2zz_3_WQh7iTJ5dUIzt0NnOYv_3zsEAw9MTRfQNxqUTS0LQvV1ojb1ngbfQ6SpN6zL2_KqTFVWXrMG2hg7fhz5zyVHHG1JGK3B9knibA8BQ0Q1VPhoc_h-0QhQ2X2f9upfSqHhH_mTQezqVaUGXfQKs7Q1vf0aGafIxjudCjqZwkMc7kG6FY_qim1iAkIhWEqEE7rInuSRco-MdQHmh3fY7bHhEeJSerHsAslNptPcGAAKtGoxek-C3Xwl9sRwMcRyuzJ6hWlORdUGcKLqkb2clUbxWFx1TO84SFncDx9skOdzrHP3NWG-HIjLM1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=kE9cMri4uPvO6XOR5l9HjkdqaH-3fXLhNo9H_KeVvez14KyyORv3lunhtpnxgZrsH-ddtZtPv9mIws3E-t23E8WsXFxYuPSWT-ju0cIH7qoqcVj2_so6NQ3FsbQUgrfP2gzT8XRbHP_lUVshnGZhRiyLPbD0Rk1h-yyRozvujwDUCMAOIUz1WdJSTnHkV0qxzhmYbq0bA3BVs-PIDMkmxcrhB6rl4Up_eblTw9AMVHQzd0g3apYCEsVT_7OT1gwNMlCoH2MAzu6qYfrWCSIMkOQakpUBEO6Oh1dvrVpdI4bHhSv4Zwuhg-vRQ5i9iBSbTKjFy07sln9iokCuE-dfiIhEtEz8IpIJ-bviwMuW2lkT-F2zz_3_WQh7iTJ5dUIzt0NnOYv_3zsEAw9MTRfQNxqUTS0LQvV1ojb1ngbfQ6SpN6zL2_KqTFVWXrMG2hg7fhz5zyVHHG1JGK3B9knibA8BQ0Q1VPhoc_h-0QhQ2X2f9upfSqHhH_mTQezqVaUGXfQKs7Q1vf0aGafIxjudCjqZwkMc7kG6FY_qim1iAkIhWEqEE7rInuSRco-MdQHmh3fY7bHhEeJSerHsAslNptPcGAAKtGoxek-C3Xwl9sRwMcRyuzJ6hWlORdUGcKLqkb2clUbxWFx1TO84SFncDx9skOdzrHP3NWG-HIjLM1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=pFEt6V3gvrzVX4k9ckNaPvGO7IdnfkZ-uMrT_gvo4-vhjGYf9tka2phhKq-lDDKhUOrKI8K6R6LRSJZ4YgQe2F4hmYybfK0KB2WFzKfeuQAw03A8qseiEKy-r5HMUVpWof2FE6gBpJNNtGFwiP4yb82qqCNsmePx7kAL1YiFD5fOneubHNbjT7DkPWvo0XA2D638RxiGEGUQsCtS32dmZokM7PWhlaN-bJba37lm0NCSCDgBGDHKoXtqy2K8nf1FErcdRYOdgouynX2RTh3U-dIANqWP_Dfapn0N49FS6iroSorp732NktGM9KKj5vVD89DaDcAYALgrsxtexH2FD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=pFEt6V3gvrzVX4k9ckNaPvGO7IdnfkZ-uMrT_gvo4-vhjGYf9tka2phhKq-lDDKhUOrKI8K6R6LRSJZ4YgQe2F4hmYybfK0KB2WFzKfeuQAw03A8qseiEKy-r5HMUVpWof2FE6gBpJNNtGFwiP4yb82qqCNsmePx7kAL1YiFD5fOneubHNbjT7DkPWvo0XA2D638RxiGEGUQsCtS32dmZokM7PWhlaN-bJba37lm0NCSCDgBGDHKoXtqy2K8nf1FErcdRYOdgouynX2RTh3U-dIANqWP_Dfapn0N49FS6iroSorp732NktGM9KKj5vVD89DaDcAYALgrsxtexH2FD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHIwD0zHLPAWT2gVs463t_YRe6BF5gxwH-4lZkMCYL-BdRuAvZUxIxZNC9twrUwSotADejbyo5aLDRSEpZNjYenFskB9hBV-OuRO_Y-RjzUV2j3qlXPqV7nv3eqUAXeBxg0CZQW_azNKC41-jXoj_VoFWtIBxLOVd-TBsXmLai7UplDo6vLq9AEsMwwPEj8gpg61b96houig70_OCChS52Mzhd_8JMc_EegyCRmfkJO1_QPEK-iaYR_ggZF2LoH3RZygjIqckDUTaxV30soadxPRIY9B7lMatYnMaozeYabQlqTjUWfkrCaJI3sYy5LOW2LN9ec6Lilm7yoSbjQxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEATt82ehB2_wo7j14qUPW8PwdUufC3IJSSmPPK4R4y2rfv3CIy9TNyKvT75A7VNQM8Cx6zmgXlif3-TV4hlaUV68lVqX2_V2zMu_8p76RMTcqCmVBBvu29gjzW6C_J9tC983maq_xLDDQLunhBC7aHFi_SFZtZDP5-9nb1pgT0UjLe-Ro1ldr0q43gh8FDZAN3ROH3AIISuzX-q8CCLKJ6NvaAZ3dLtQcV-l8KZOMHm4gfEQN5FgJA8SOqmLdxKotNc23f702e0Ry4Ab63I-YSP-U2On6E-AJwVHbkRWPxD27F1lnCBlWWBJcmk65jJrdtzDovQZcaUpbPKnh1aXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amlXPB3uJvozCu2e-2K-UTsV_TD9ct8aJRFWQlMvLFFYlH4AnASKz_EwVXOH7tEp6DT2o5RvOk2qxm7B0Or55JcIfp-6TWTFKgHG3qQjkg4opRGR8tQUaBl1y0Xbi_pGpEzYyLPaHey8oy7iAV2t15cBCKfn76INhCa5lcbKFCvJHdv3ISUc-gRZUyEP-4EbfX6eH6HIFPxMLG4oo_G9YJywTSuKgIWDPe1erXKwp2Txr__jijAQWiPo6ZAuz7J1Oz0oyQMHJTCpnmsDlI556mh8r2BBBKAO-NRJVujYlCryyQOJE9eoqebs7F-7cUdSsOd1EBM1Tj2rfYLvTK_3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL_T2Yt0Hu-b18fjioSWPdxiCmvwzui5MoxOPFDnhNSR_PL0VVhOyA0SNIb6pS9dk7zVC1XZwR_JG4fg8RCD96vnsrgT9fluuSFnpWvf21PzlGhkIPhS-pxgk1-dmA89apIkIPUYfNRMRMaub4APNRZO6rnvZU2k3YcBDrWMWSgbHC3rSAgjda-TQQpE3UoKR_Jz4Fqh6wJ2eDj1tgbBiuyaVVZVyq33Q5ow7u76x1W9zkuG2lig6Ts-Uw9sqQvGEOePmW9o3VklXQZ10t5-VxN5E-J31IuK1vDb1JktRrPJ6wsE8qKGjzZUhjbO3T4DopLIq-EmLaMP7_aUXaISSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
