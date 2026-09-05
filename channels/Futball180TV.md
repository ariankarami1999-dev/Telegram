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
<img src="https://cdn5.telesco.pe/file/QcDJAgCY8Hj73dMOAKhWYEG4ikGZHtW7sI6SI-zwEbnYlLk3-8p-8RK-SEWM5bU4ZjAJfMiWaQmVB6EMHiGwFgL3w6_KjIalXkXvxE0q66tdAWvO4cjZw7cdAUu-y4wcPvtUYcLBiJKfxcmAquJmaYzRzGoxZkgeGr67P-V3lbckc5HmYmsTQt6YB6mJMPj6OXnumkpFfwOfpYOEJRyvbxZf80cU7AeQa6VRvu_LQjrzpVhDRiZNYYjmmctHAeUUxzZA7hEgMD_vXEjsTwopjgjmq9OV8KLv45Pb3X0ptc3w8RrifMNRe1CtE2RG-748uZMdZVdz7OcpydqtjOYLYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 426K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 21:59:09</div>
<hr>

<div class="tg-post" id="msg-105640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fes7krtB-XoqFR7HVJaeSGqYmgqumnHDDLqfrsGDcBFVXApxOQlxtmqjk9Emg09VyJCrfr-aly4_tqvm7ntpLA0wQ9P787grF3OhFTRt0a9qKpuEwyGB6zyvyufmA6WnVpLfCXL_jsEkcByjCiB-xPS60pJRWEzgQNFBq09_6hGqmrjlX5TE16TTKtLN4KvUinjr_yPY5-pxtjwxltVzAkLUUsa1yh8eBwh9BA4-tARr846TKFxlkgmTEmPC0gn3C-C0T_4Nk8ZUbO5G89IjpJ0GlNyQIHm8aTGw9A3V6M7aBMeASEriCmgXPYk2BmnUCDuR3Tl3ifDsUJxDY5T6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
محمد عمری بازیکن پرسپولیس بدلیل کشیدگی رباط زانو حداقل یکماه غایب است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/Futball180TV/105640" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=AsWSuOb5N-5wGZ1CKiBvvI21wd3klBWxQgoL5jOZ_gTS1l78DC0Ca71HK0cjC6DoFHmD1pORtS-GEmLgjcjvQScJ0nM1tUe3N_rV6oJpdxKbSA0FAjtyVgiM9kA6lgSuk6l4-TJr2-bX1GDbqEy5IOApOLRifImEgDo2ULqrRehrQIQ3Hf-FFHziXtpL0XI0Mt0bfjGJS9mG4zg0aeQQUT0dJt9pL91MU0FaNkiWA8pHZ11wlLbCIFeTVMxLgZH_y7CesJROwbWc2snXOY7Fv4YDXrxrbm3celrI3TuM4-d-rWC6-ytQUHYRJfwZUafmiMWtP8haQ7PcSz41LIbKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=AsWSuOb5N-5wGZ1CKiBvvI21wd3klBWxQgoL5jOZ_gTS1l78DC0Ca71HK0cjC6DoFHmD1pORtS-GEmLgjcjvQScJ0nM1tUe3N_rV6oJpdxKbSA0FAjtyVgiM9kA6lgSuk6l4-TJr2-bX1GDbqEy5IOApOLRifImEgDo2ULqrRehrQIQ3Hf-FFHziXtpL0XI0Mt0bfjGJS9mG4zg0aeQQUT0dJt9pL91MU0FaNkiWA8pHZ11wlLbCIFeTVMxLgZH_y7CesJROwbWc2snXOY7Fv4YDXrxrbm3celrI3TuM4-d-rWC6-ytQUHYRJfwZUafmiMWtP8haQ7PcSz41LIbKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت‌کریمی، مدیر عامل تراکتور: از آقای تاج درخواست داریم ستادی که علیه داوری بازی‌های تراکتور تشکیل شده است را پیگیری کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/105639" target="_blank">📅 21:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkWFOPnxA2EC4r2PupsxxqySXxLLJsWYC-2kY0YEKxzih3c4yeAocwKsOFCAbmSjd04vGLZBA_MXRx-EN5Lz_zUVLae3NpNo5DXWKaURIz27mTeBBHqitfWzUIsGiCVPCDdL-Y38vnE_nD2zt98v8VF8fkXnbIwil7Dpm8YOY-b16AU8-osoGfYgeToyav82f8IE1OzYBtg9QIkuPjaOs0rWVd90AUDVGNsyg1ZJnKLM3udcCc75ZDoyYBtjm3JjrByuQ_u_yJ95NWswZQMBAEhgZ-OCyx5fSX0ZMlSVyT_trqmtSWK9LhIFvk3l00uRK5r2iWTLU942zUMHsmMyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🇮🇹
گل‌سوم اینتر به ناپولی توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/105638" target="_blank">📅 21:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f75618ba1.mp4?token=OdwD3UxE6j1N8IMeRFCiZOORAvB63AyG8QUzYrDllYYSAeMZFNbbB2ogx28cKNZKvhUwA38CYNis5uiTKrUvmoQfeiuv0ZRGbTrZ3l7a5oXtQwFpYGm1cqw7T_1Nffuk5COUYcgLfJP0ltWDybfc7O2Xdr0pEd1PkGwc5u_mptbPJ24cE_K5ozOvQs-7-_6NOFLxNQ3_eDgaxTfQ4eLiDAhFKzVFUw0PmaMz0VdwQaR_iR1puIDVmtwQaOwGIXh8tecX3cO0rBRzYOZhx3O7eaY3zBqJEh6tnlF4psSND_YlFstAyNgR5JI7MiPeL2ckCfNT176cIqbD0cywegzB-HGRIRf-GXYbejhsXElhBiH_UnkMYcidryV4-j-p4PB8WJwDEqLmaeM5sJzoZnztt4KaeMpstIfGt77W9xqVv86TTfVfZhtjB4zlWhQxqX5Onx6UfBql_zTDUA8pASyNHHT_KGzi6JYMbaTbmySWlxP0pWbk0uFm9s684CXqlD1y2M4Y1y2Ei_d2vHRq1Mmz19Oh8DkGV-1lVNSYpM9sGNApnEneq1rKgNkPqcaSX9ZJZQMrQ5BE5Gj_rq5bVYxMJBXdab3gPN2M8WG6hIJVB71GHX5uSs8HYAMTMl099V8xEFL7ZTp4OCsy_xPR4hsN5lFtPB2-biT5ZcJh0JSB59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f75618ba1.mp4?token=OdwD3UxE6j1N8IMeRFCiZOORAvB63AyG8QUzYrDllYYSAeMZFNbbB2ogx28cKNZKvhUwA38CYNis5uiTKrUvmoQfeiuv0ZRGbTrZ3l7a5oXtQwFpYGm1cqw7T_1Nffuk5COUYcgLfJP0ltWDybfc7O2Xdr0pEd1PkGwc5u_mptbPJ24cE_K5ozOvQs-7-_6NOFLxNQ3_eDgaxTfQ4eLiDAhFKzVFUw0PmaMz0VdwQaR_iR1puIDVmtwQaOwGIXh8tecX3cO0rBRzYOZhx3O7eaY3zBqJEh6tnlF4psSND_YlFstAyNgR5JI7MiPeL2ckCfNT176cIqbD0cywegzB-HGRIRf-GXYbejhsXElhBiH_UnkMYcidryV4-j-p4PB8WJwDEqLmaeM5sJzoZnztt4KaeMpstIfGt77W9xqVv86TTfVfZhtjB4zlWhQxqX5Onx6UfBql_zTDUA8pASyNHHT_KGzi6JYMbaTbmySWlxP0pWbk0uFm9s684CXqlD1y2M4Y1y2Ei_d2vHRq1Mmz19Oh8DkGV-1lVNSYpM9sGNApnEneq1rKgNkPqcaSX9ZJZQMrQ5BE5Gj_rq5bVYxMJBXdab3gPN2M8WG6hIJVB71GHX5uSs8HYAMTMl099V8xEFL7ZTp4OCsy_xPR4hsN5lFtPB2-biT5ZcJh0JSB59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🇮🇹
گل‌سوم اینتر به ناپولی توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/105637" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8ffHm8eDwE6KH3blBsKX6sXDpea1fdp3EaTVLyxvXWso2n3O26mZC6LzpxwJRuxhsiYAfPC_fpOYC4rgL_pfa8QPz6RNu4D3oUQeB8XfrEm7aqhUDnGJy5DoJNaKXtJES2BVu89nK6oEFusCOKTCB9kJA8yOzgmh1AHqOy6ahUn5mSZubyywKJaXLfT3tp2ryFqrYOkgtJkh8MYi7m_WEfuj5dgNHe3AiR30BwvWxLshg8qljsG4gCybD0s2km1LgIKqpJyJOKIomYz_O9rJ6ToTaEOmQwmlfNyCF4deewDv7rtVvE1Nnqx5fNCkRaf8PkYVe9_OZdjlicGn_vSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/105636" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3686a0d49d.mp4?token=CJZkTe1TSuJ91GVq5DWKe9v6QLpIokW7x1HX0e7itQj0KpKWq-i33jJHX6DGe8zd0JAZWA022h6gWiTu1zeo-2LDES3bbYiAFv-y6ZM0Tdg1m_vI-EDkXoUPnTsTarhPN8uwsGOLF6AsGiLEi7K5Dv4R_Nh8XwXEc31_bR_mBbfjmLTKjZ9ud-YqsJu1KCUBGL1nmVbGw1NkDa8Xra_4r6WhuSrMCneelQNxm7mksPCRQm9QKcU8cOFtNUpwbDCI9fGj01wJsQI_D9IBdPCxY9i76p6L2XZpBrJp0iq3CuDQEpxZAPsdvZqVAKqRNJ-IE8xuD7jydZq_-XelvcpUXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3686a0d49d.mp4?token=CJZkTe1TSuJ91GVq5DWKe9v6QLpIokW7x1HX0e7itQj0KpKWq-i33jJHX6DGe8zd0JAZWA022h6gWiTu1zeo-2LDES3bbYiAFv-y6ZM0Tdg1m_vI-EDkXoUPnTsTarhPN8uwsGOLF6AsGiLEi7K5Dv4R_Nh8XwXEc31_bR_mBbfjmLTKjZ9ud-YqsJu1KCUBGL1nmVbGw1NkDa8Xra_4r6WhuSrMCneelQNxm7mksPCRQm9QKcU8cOFtNUpwbDCI9fGj01wJsQI_D9IBdPCxY9i76p6L2XZpBrJp0iq3CuDQEpxZAPsdvZqVAKqRNJ-IE8xuD7jydZq_-XelvcpUXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
گل‌تساوی اینتر به ناپولی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/105635" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/105634" target="_blank">📅 21:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=TgzuauekKI3PsKUTFH_hQJbMoUpJn-ad4B3KXPKEDsnaee5ofUGZbl20-C9JVxI8LNREe6MI506-cOy3x86Wz-88AROXeJTkq-Uha2spiBbXqLCl2gJdJbiTJxxQ4DdBmqn5GK_h87UF2c_K3dyfEPMCXmbFkgRiCRO8aVBrPVQ54lluxde0TTtld7HNe18uymvUHxQYWtNH__EzUJWd8SqJlg8ccnDVkm7eStFK7KijtstGYdVRDbfNSr1vnYH_-N_Zr12H4uMVeDbQlp10I5DF8Kv9gsWw9e7peP8zKnOanPYbPchYi8-MKKYwMeBZvEK1A8T_eKN0kzOh6J6MBREKpa4UKtfCrTR1qUoTEEgV9wm3N3D7_3MLHtXNl9ck5vYLZkjpMeSQpplZ4IVOSg8jbfvIrA5n07J7DJMtZuggo_xvN0IpTM7xW09pJhegAFm9QZfoxlcj1PUtpHpg8DIZXxUA4mDDsOxvVjwSQpVS9-y8pVMAB7J2HTGSR0fnLz9I1435FxD60wPugW1Ru8Nn2I3OZivM2Mq6Nb69Iglr4OCh_TFIdYrgKI6DXkYUzHDS9NuNOIvxb2ypFnm98vn1nvP1Mh0dsVOXDU4eIp5Vu5ujcx4-mZq2anwXVoNjM7o-MUrEE8uYEAgHg2ZjAkjSFh4BladG4Top7mOmVLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=TgzuauekKI3PsKUTFH_hQJbMoUpJn-ad4B3KXPKEDsnaee5ofUGZbl20-C9JVxI8LNREe6MI506-cOy3x86Wz-88AROXeJTkq-Uha2spiBbXqLCl2gJdJbiTJxxQ4DdBmqn5GK_h87UF2c_K3dyfEPMCXmbFkgRiCRO8aVBrPVQ54lluxde0TTtld7HNe18uymvUHxQYWtNH__EzUJWd8SqJlg8ccnDVkm7eStFK7KijtstGYdVRDbfNSr1vnYH_-N_Zr12H4uMVeDbQlp10I5DF8Kv9gsWw9e7peP8zKnOanPYbPchYi8-MKKYwMeBZvEK1A8T_eKN0kzOh6J6MBREKpa4UKtfCrTR1qUoTEEgV9wm3N3D7_3MLHtXNl9ck5vYLZkjpMeSQpplZ4IVOSg8jbfvIrA5n07J7DJMtZuggo_xvN0IpTM7xW09pJhegAFm9QZfoxlcj1PUtpHpg8DIZXxUA4mDDsOxvVjwSQpVS9-y8pVMAB7J2HTGSR0fnLz9I1435FxD60wPugW1Ru8Nn2I3OZivM2Mq6Nb69Iglr4OCh_TFIdYrgKI6DXkYUzHDS9NuNOIvxb2ypFnm98vn1nvP1Mh0dsVOXDU4eIp5Vu5ujcx4-mZq2anwXVoNjM7o-MUrEE8uYEAgHg2ZjAkjSFh4BladG4Top7mOmVLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
صحبت‌های جنجالی علیه عالیشاه؛
خداداد عزیزی: او اصلا در حد من نیست
🔴
بیاید بگوید کجا بازی کرده است؟!
🔴
اگر یک بازی ملی داشت بیاد صحبت کنیم
🔴
این همه مربی آمدند رفتند هیچکس تو را نخواست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/105633" target="_blank">📅 21:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8b13cd017.mp4?token=ZkkWZO6RDaGIW4nE6eDFWyTMScz-I4VqkkpFu1egxw7I9mku4yIx1EGXhPs00K-O9RJU0jfkLAonSq-_185BVDa4twedgNpbImJz62EifBwy5-dYn2shz8KN3JH3hR-Ugow7AEflOj6iDUyGKNafhQG9uXHVFSeLs2H4RRrIcW5nVt5rbeJX11NHbEvQUYC5IO09XHUwufG7E1TapW5AJdbaRFhkwmbmd76YWp1K0cFvj2HUdebdale7UychUzztKVVllH-GUSnRSDSwfhijTMe2_TaiXhalkCtc4t-LPphkXX0TNFLsy8emnVFHNNGauYVROuwOA0thhlUHet2TFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8b13cd017.mp4?token=ZkkWZO6RDaGIW4nE6eDFWyTMScz-I4VqkkpFu1egxw7I9mku4yIx1EGXhPs00K-O9RJU0jfkLAonSq-_185BVDa4twedgNpbImJz62EifBwy5-dYn2shz8KN3JH3hR-Ugow7AEflOj6iDUyGKNafhQG9uXHVFSeLs2H4RRrIcW5nVt5rbeJX11NHbEvQUYC5IO09XHUwufG7E1TapW5AJdbaRFhkwmbmd76YWp1K0cFvj2HUdebdale7UychUzztKVVllH-GUSnRSDSwfhijTMe2_TaiXhalkCtc4t-LPphkXX0TNFLsy8emnVFHNNGauYVROuwOA0thhlUHet2TFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول اینتر به میلان توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/Futball180TV/105632" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f3a740412.mp4?token=D4NbPjUW6PZfk3H2ZIfcvDvMgN-W_x2piRAkiqXyuHHUiRLsL-Z7sWMr4qTYFxCb2zTaQzaW8bA3I6RPOVEPe7egEuKZCP2ux7ASSim2yoH-DgAxEoSW5y8w2NGtEJFR-ScWgCa8Mj_J9kuKq54goaUq-FqEhDBWXUMHxcKCKUv0BU2fzYiCNFgFix2defuz5BM9F9GiBHa2tldkMw26fnU8lvjJ3WrGCZCpYhyM18otgVfpYVy9wQhXyx6ne9AzvPbngIyLWBmVA_xFPfHsaq4qMaOYQvKyLNb2zcIR7_jtb4M4u0_Uer80a4MYY9WxBlQpZBWYVRsEEgpxQRjyOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f3a740412.mp4?token=D4NbPjUW6PZfk3H2ZIfcvDvMgN-W_x2piRAkiqXyuHHUiRLsL-Z7sWMr4qTYFxCb2zTaQzaW8bA3I6RPOVEPe7egEuKZCP2ux7ASSim2yoH-DgAxEoSW5y8w2NGtEJFR-ScWgCa8Mj_J9kuKq54goaUq-FqEhDBWXUMHxcKCKUv0BU2fzYiCNFgFix2defuz5BM9F9GiBHa2tldkMw26fnU8lvjJ3WrGCZCpYhyM18otgVfpYVy9wQhXyx6ne9AzvPbngIyLWBmVA_xFPfHsaq4qMaOYQvKyLNb2zcIR7_jtb4M4u0_Uer80a4MYY9WxBlQpZBWYVRsEEgpxQRjyOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌دوم ناپولی به اینتر توسط هویلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/105631" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105630">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3255aa137.mp4?token=nljlfyfE_QE_lI9k-UH4JssAXt_47x-hEIi5Av39pKtbsk4sld5dIqEyjVywwMZi9hGhfwhFrnmbxjygxrbVF5KxaMIMhcQ-jWgpDSN31DuQcAVEHUantr5Qxy9JcGhIt9K9XVnA5Y8wv8-Mg6R3Q0WGcJ8npJYrWAKvsuDx1wv49pDP9WZuQ7idj9GOamKskcdt8RXgs39FZji9-cwZwVl4_0r3yGfekpddNxOSQO9Dms430wut7QWAc06vBybVupUDnZwd_kXBjaupoPqdXGxIQ8h1g4caa14eTrbZscq3VPF_nr1Jf2Fxromq05WOe7gBd7H2d8TzSgh-iI-6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3255aa137.mp4?token=nljlfyfE_QE_lI9k-UH4JssAXt_47x-hEIi5Av39pKtbsk4sld5dIqEyjVywwMZi9hGhfwhFrnmbxjygxrbVF5KxaMIMhcQ-jWgpDSN31DuQcAVEHUantr5Qxy9JcGhIt9K9XVnA5Y8wv8-Mg6R3Q0WGcJ8npJYrWAKvsuDx1wv49pDP9WZuQ7idj9GOamKskcdt8RXgs39FZji9-cwZwVl4_0r3yGfekpddNxOSQO9Dms430wut7QWAc06vBybVupUDnZwd_kXBjaupoPqdXGxIQ8h1g4caa14eTrbZscq3VPF_nr1Jf2Fxromq05WOe7gBd7H2d8TzSgh-iI-6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول ناپولی به اینتر توسط متئو پولیتانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/105630" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105629">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbX4gQce3Ygf9gSnZkOcQfrmQF3Pb_n9EywhZYDfcPcM96zf2-TFdVFYHvAPHc4HlLacal-kOhNEnILR5sWi3UEKFXaodHCmoZyYxII54kY_DpI2MZsjVZGlJZlv3_gsDOci_VtiqSZSwciKhjfjpApCosi54IBxH6O9Hyax4YgDAouY3tYf3JEpKR__eXjnCBejkOjX4zi05XHDvRCH8r8qFCJaN-szMfz2EjSCpBPjCLWH8PZXxKU6GoRju9-Q3EXXQ-LUhDctzR6ddclhGe8vNwko_EVWgkJBPU7n8bhdOj75yVQCGdXN-S-EPxN77InFoJkMILdI8rnWFvg-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/105629" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105628">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=qCGEhisukerYOVmqFr9HIwu-nBBJj0FUI7xnG6tk-Ii0gBv13Fi6vpjGF86aeswMGUt_ociRIFNmvAJmq_rzbPX6W2SzC6qwXwifpLGQdVoaBfIewoY-67IsnqAoTSmXk1bK-FGRLj65pdVuAI8wsntQnp0p9X9WVm6coOLuB1wzRJPflh_AgaKp0_BroMclAd2Mhz5sp7CMlwxDA0KQ2wFbXTASdbJHq8OublvUL38OzV9yTleOyC-Dms1thngVq5lV_Zz0iBS7X0aAz7Urdk3whk262hreqbUGuXKiqAMPNULZyETs8OP15lJVhvlxbRVHP9v-IQe4vURyi-pF60bsFCc3sZPRMTXs-ySgdA9xRoumea5mPTCTBukQ7MwWgrRhveDl6vTuRB38kpMDl3HBGiXulFMBGIHowQzz4lbnnHJ31pfgNJyzbxVjkfk7L-6hrdljtb8DqhGYc0hDUlLIVlpxXI5Oenthy3EpMsriyyqnlHCuejBGrvZYKFKKZ-GX9zglB_xv1Y3v7UrPva2KGYOqkSEB_0WPPN-nMuqMt-X59Del8fhI178dzBHXhytjUyE4QkgLK9xAC4ZdhljaTcQ9ZNo5oNtUBl37C3g2mNcbZ7RKNdpWx2Gvkd4xNWqShOiznPKEGvYe0SYATJctoNxHVl4boVo6mcGVTKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=qCGEhisukerYOVmqFr9HIwu-nBBJj0FUI7xnG6tk-Ii0gBv13Fi6vpjGF86aeswMGUt_ociRIFNmvAJmq_rzbPX6W2SzC6qwXwifpLGQdVoaBfIewoY-67IsnqAoTSmXk1bK-FGRLj65pdVuAI8wsntQnp0p9X9WVm6coOLuB1wzRJPflh_AgaKp0_BroMclAd2Mhz5sp7CMlwxDA0KQ2wFbXTASdbJHq8OublvUL38OzV9yTleOyC-Dms1thngVq5lV_Zz0iBS7X0aAz7Urdk3whk262hreqbUGuXKiqAMPNULZyETs8OP15lJVhvlxbRVHP9v-IQe4vURyi-pF60bsFCc3sZPRMTXs-ySgdA9xRoumea5mPTCTBukQ7MwWgrRhveDl6vTuRB38kpMDl3HBGiXulFMBGIHowQzz4lbnnHJ31pfgNJyzbxVjkfk7L-6hrdljtb8DqhGYc0hDUlLIVlpxXI5Oenthy3EpMsriyyqnlHCuejBGrvZYKFKKZ-GX9zglB_xv1Y3v7UrPva2KGYOqkSEB_0WPPN-nMuqMt-X59Del8fhI178dzBHXhytjUyE4QkgLK9xAC4ZdhljaTcQ9ZNo5oNtUBl37C3g2mNcbZ7RKNdpWx2Gvkd4xNWqShOiznPKEGvYe0SYATJctoNxHVl4boVo6mcGVTKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
🇮🇷
سهراب
بختیاری‌زاده با کنایه به صالح حردانی: کاپیتان دوم ما باید یادش باشد که زمانی ناصر حجازی، پورحیدری، شاهین بیانی و زرینچه کاپیتان استقلال بوده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105628" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105627">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105627" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105626">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105626" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105625">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEfWKDZtZfw3ZlDM9zwIAOr51YNLDYvyD1b4WBvCoD_m4pA5_R_05XNJ4RcLh6pQoRIbvraOifzWZjw6oRtH8zhCJBwchMg8EHEWcXLEQBD76dD8RCUxEMBpRjQyyG8_VijR7SfqAfwilI4CNQWCDmurc5R4E6_pABWL9Fjmy7cLmcjuU3Kracuf0Qj89yw1hQukWk5aBedpXso_9WtMVyOLRT3fz0S3t8xiRYyD0SpTje-hEgxbjwwUYm5spcVYyWd-3BhpIUA3OyhVky1o2Q965mIzuO9FZ70r7pvXt7KS5t9ezkp5gSVnGqV1PJPSDkL63oQpCvM5v6a1UzrrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
ترکیب النصر مقابل الاتحاد با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105625" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105624">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoW86EBi1OjI2oq8P3Gi5aHU7zaBiCeNhn5-2Ks0A79JVidnz0O-dFEhLihHg2mv09-trur3FG6eGIKx_jjnLI5b-g-lfKhDdiY3X8yQ1XuSCj-ciZVKWwkPGzZSGj3oeWpD4WKyWgllDLAm2ahI-aXnBP-RRoNDQiHdg4msgDRlPc5rwFyfO_fTwqUx0G0IcII4wJKotv8EGMwCkMhd3qMFRDE9AUw7DeFCtS3EWX8eMJSVJOAOONWYoHB_tYBwry-S1h9f1QTTTFTVf438G2DSplQNf75_UiAm-djNaCJaez4UBO129HkKqvvLnbQvTmTh8zVABB4QVqrGd1l_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم لیگ‌برتر؛ پنجمین برد نکونام اینبار مقابل همبازی سابقش رحمتی؛ تراکتور با تک‌گل جنجالی امیرحسین حسین‌زاده در اوج باقی‌ماند!
🇮🇷
تراکتور
😃
-
😏
گل‌گهر سیرجان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/105624" target="_blank">📅 20:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105623">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYet1nlpnfQDAPZHM5ciMCFs0crLSqnpSS31lozMjIrw9O7Bl5UL5ekTiRK7ZGLz5U7soquM8xR4US5hyvJiBavZdUj5BAfBLwQbnBA0k8j_Tr8pAciRlgFCTarxtAVaf4Jy5oqrwFfU6c9MUJWo0ir22b3WqY7z-Y3STRQeMnouADuaz86dK7A8WkIEbf8zO2cwUdALPWmkOrEp18p9aq92qLplnybP7ECNEQ0hu3BEXb4DQwdeIKlJYvyrltDxzJUG9wM71_m9xFgQ_teSLfFHX8JZvPGHuE3XLQNkQM_sW4S515O8KE9CnZm7R6cuNV6lupPyf955iXit9Z44ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/105623" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgECjQm_s5crvmw2WJwTITd4cuCv0DzKrXRxihGYbr81zI8Nu5P6V-hrwlzF9cHHA0c7lKAYeey94zBWkpBX6OAMDWyeSeTTZ9TymArD6deCB_7Xj-5VXjPNZQE2YhwBK_CflOfS-D5xtaZgWPTw3yt0ce2xrA_G8NMWNIiIyWBJzmSrNNm50rAMh6eelq5gPNa6dVKaKMcuAfdG4ZMSD7IbZzGFCgnTlb6-qmYQNw1d-2_ce2RUsIRy_f7t-llo59bJzVa3HeKH4smqe6jGEaHeR7eCiUvxVTofmUnNxnJCJTH02tZWxchB71hM9iVGRv1yowPcvjYm-DrH8GxOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پایان بازی؛
🇪🇸
بیلبائو
😆
-
😏
اتلتیکو مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105622" target="_blank">📅 19:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKZfJVbEcBtnjtDoWQhlbPv0Gn1KjDXkt1zFZ8aHBixia9fmf1VZYfVHAD4iH0f1DxWTM7Yjbk0DBXBvlSVq0qtIRTRWwPQeAQHTl1kYhqztRi9i1BfCyxT9wJmskz6HDbw8LoED4RDUKDVPwhkeyoLLeBg4h9AVv4EsiOp21MpBkGAb8lqqDX3dUiW9fkAmIQUsCiJakJ_9XKfROcWenU3-ifrnbYUtlwbvPz9VubK8FcpD3XrYJouO3aTiIH5soMTksnAZfkfgxhPk_nM37aRvO9KRoZRDcZBxAWCS5xXa5Bd8u60_2HC15yS2pbLxqa0D9dW97L-9vksgHZADnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105621" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105620" target="_blank">📅 19:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اعتراضات شدید خداداد عزیزی به داور بازی؛ واقعا بعضی وقتا کسخل میشه الکی کارت میگیره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105619" target="_blank">📅 19:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🟥
خبر کوتاه بود و تکراری؛ خداداد عزیزی در بازی امشب تراکتور هم کارت قرمز گرفت و اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105618" target="_blank">📅 19:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105617">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQsM-d_Q5P0cd0ihPl_Xl-JuEoO8Do-8irmOwnaVLGyl91kMbjfWOFvD8B4fyrDN3wd3upOO7PngEaJTfzPBDayJPJ4dwhwfuLV2iVWdKtqX3Ejw0fh8T_thoWhA8HpZDuyorSw0Q4YR-5E0TPRO0FaLbXP0N_o9QnoaoJ2CtO5tTvlYV4HRiAiImdNL36PeLTv1vtN1AtwM5xekhOXsNNHuAR4dMh8HB-RMS8NBFcydgnTrTvwwNk6cvhNhlWd8xe2ZP9mNqMaq1DPcc2wJV8BB8AWBUGli3s8Bch6RXeJUr9jznHMeFVXl5NgmHNzj7mx1he-HrL4__KW-P7hicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تاتنهام برای سومین هفته متوالی در لیگ برتر، بدون پیروزی و بدون گل باقی ماند!
😵‍💫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 3-0 مقابل برنتفورد.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 2-0 مقابل نیوکاسل.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تساوی 0-0 مقابل ناتینگهام.
💸
باشگاه بیش از 300 میلیون پوند هزینه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105617" target="_blank">📅 19:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105616">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
‼️
🇮🇷
🎙
صالح‌حردانی: مشکل خاصی میان من و آقا سهراب وجود نداره و‌ بزودی شرایط به روال قبل برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105616" target="_blank">📅 19:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105615">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105615" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105614">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhvY6r3v6B-OcfC3h3YfJvFSiK8yet22CYBABCpG5jwbysBf8XZ6oGglCrmypRihQY6PjJN3MRmJT1n_FmoPB0bHw6_TlXlGDKZIb9hP8XEHT04hEP903hj14-qfHNQ18ozEF8_P3HRJRnl7TcX3A7ssaJJTYaTExSWy5pcsEIaKjzPIpys_Tc7JW6piJ74h6S7_7RpN8X_51iTEVv3X6MS981XG3BGW8tzL_HMQ8Lkh4dXFSO495XSTEpL9bGPhsihVPnzTmC4P0SMb7rBc2H1uthaGSRXmaXRUnr_4KnBxPIy-drHVw18466bH0AKuT-CtKfLXwlp57Z2u4TjgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105614" target="_blank">📅 19:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105613">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=FxENXGmuD50N_ogIT5ZbqhSMIr83Y7ii6dt-rD1OlWFUr3e6bOxELE2vD0X34K6rAJJUelE2WBF_PJ2hgtSGpFCJiWLnJUj5lwdIt0rUByeix3FLxMUY2BUcF_BhuaKSuTyJkeECyOJ_fuh-A9MuuX1-T8swl35A1wQtBMp3l86xFRU-kC4InvHWV07C_ywkHsGP6O-ZfXQ2k0e6GbRaqRhYCA5yqFZqV-J7F0Lk3OpsInzRUzHbxghm3YslWPw-vR34k96PVTKaEITWFm9gDtMmbe8kbeZDoAdaXpsBkhnP9EEwycPXF44dPDk-D0elg-2HnO9UPMjV2M1MW-05Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=FxENXGmuD50N_ogIT5ZbqhSMIr83Y7ii6dt-rD1OlWFUr3e6bOxELE2vD0X34K6rAJJUelE2WBF_PJ2hgtSGpFCJiWLnJUj5lwdIt0rUByeix3FLxMUY2BUcF_BhuaKSuTyJkeECyOJ_fuh-A9MuuX1-T8swl35A1wQtBMp3l86xFRU-kC4InvHWV07C_ywkHsGP6O-ZfXQ2k0e6GbRaqRhYCA5yqFZqV-J7F0Lk3OpsInzRUzHbxghm3YslWPw-vR34k96PVTKaEITWFm9gDtMmbe8kbeZDoAdaXpsBkhnP9EEwycPXF44dPDk-D0elg-2HnO9UPMjV2M1MW-05Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
عصبانیت فوق‌العاده شدید مهدی‌رحمتی از داوری بازی تیمش مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105613" target="_blank">📅 19:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105612">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im0APaUhlFgjwTWL9l7UjhZ8CfYrHTBEhFZZa1gJF1FuegPz0M_rI9sPnujvl0BiAXery7hFMO-9Q3jVYrktn798bKOo_rfw3NhENK-44_njXgBriKs37Snz_O4SLQD3aWTwc707UpPrudbfNZhVu4rR4nw7hZs3Rcv1rrMvC1kDI2IZuhedFNwiVDymgkbJySCOb_ozcJ5hcCrnfraJbVt5WAvVo6CqA8rqYA1PbneIuK9I3bbKfSvIISCb99g6F0JwSe6MElvMLFivTar7U59UWO_AT9j_J9QKhlWxGtO7oIpQMYhI4n1vF6ZVXksH_q5qR6TgnUjcY5iQ5UZicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌مونیخ مقابل شالکه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105612" target="_blank">📅 19:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105611">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=Y2PoLTojF5T6yx-ec33f-yyis_MU6PK4pD8vmbDwFJVgQoObqlVXgF_ueaSdhuOWVEANsSOwkZQcG4bvjPP6v1NrIuY80HswEtieOeHt713bXVQ07Uwf8GxbwNFuwMdWrMF5GwNwM4PAZVhvG1nozKwjL1l3gVPr9ZtO_zuzU46f0SBG0vGoX2aIOTLKskAuB_miIBFcRCHwLmTSfFgEMhikDp_xii1RuSIlpiMqikQmTlfMbyAf5Eh5ek7ktu3MF2-LJ5aW97_xKxzP2LWNTvqWsH-SXVmlWzGXa41qnchDGxFvwW6o3jr2S0rppPIPQORmu8KKyHdx5S6bbVMk07mUlQOlkicSYYZ1fiQXuxfMxB8X7YBYYMG0WENOEnomkMd7rw4aEI5WHJ2t4W7pfo6kqzgXy0KS4uQGIG5d0iPDnBoOKxTowm3PSd0v4DRyQAFWk3S9JS9wZNTWm2nQDWeoGXwDzgjg1u8NA2_HjRDOroXIL_e_9JxApmEanOLXLCxNaPrNBYrPkh869nXQOKIZIOnM4BzC3FtozHEThiKQFIbdVl32eKBKs1cW-gqoHzugpHJi3EgnhLDg3jcDYx1w2FDndo3rb3KEayaGkVYnkkjxqrDfC7h06n15mvtj-12lVmY089i0W0tNqTd2jqMuo1KJGZpkItxC5qDm1rI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=Y2PoLTojF5T6yx-ec33f-yyis_MU6PK4pD8vmbDwFJVgQoObqlVXgF_ueaSdhuOWVEANsSOwkZQcG4bvjPP6v1NrIuY80HswEtieOeHt713bXVQ07Uwf8GxbwNFuwMdWrMF5GwNwM4PAZVhvG1nozKwjL1l3gVPr9ZtO_zuzU46f0SBG0vGoX2aIOTLKskAuB_miIBFcRCHwLmTSfFgEMhikDp_xii1RuSIlpiMqikQmTlfMbyAf5Eh5ek7ktu3MF2-LJ5aW97_xKxzP2LWNTvqWsH-SXVmlWzGXa41qnchDGxFvwW6o3jr2S0rppPIPQORmu8KKyHdx5S6bbVMk07mUlQOlkicSYYZ1fiQXuxfMxB8X7YBYYMG0WENOEnomkMd7rw4aEI5WHJ2t4W7pfo6kqzgXy0KS4uQGIG5d0iPDnBoOKxTowm3PSd0v4DRyQAFWk3S9JS9wZNTWm2nQDWeoGXwDzgjg1u8NA2_HjRDOroXIL_e_9JxApmEanOLXLCxNaPrNBYrPkh869nXQOKIZIOnM4BzC3FtozHEThiKQFIbdVl32eKBKs1cW-gqoHzugpHJi3EgnhLDg3jcDYx1w2FDndo3rb3KEayaGkVYnkkjxqrDfC7h06n15mvtj-12lVmY089i0W0tNqTd2jqMuo1KJGZpkItxC5qDm1rI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بیلبائو به اتلتیکومادرید توسط ناوارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105611" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105610">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=UQuD5rQedljy2-qJj_imBZPCQhY96T31Pjc_KK7_IB9XnTwvvR73M3aZhfwRuS-fGzGFej5Hyq1BYyd_QZ1DuqIPP6yV3zjjLWA9S_CtSH0I85MUTqInw3fPjX_AME08ZKdUYxyyzOFdMDXTaEKiZEXGHUJ4VggQ7TTeDxe8-ANLMDjNbMakgTiYNlNiZUenHlXIM9wvbfY-9lwu1XI0jIt-N2R1297lnIrEudG8L-t0zxkpFHdon9S8TG4csoU5mQXB2FV593WQT2ctpPV3Is6WDvauN6-K-Dt2dIduM2YXhau9D5i0k2FuNKXBtJFwXCnqRfthvRHFZ-ewP3D7szVljGH_wNgWonv09z9ZIpeLbXPIihYZHF-Ku5adWmWvdIb4ykfKk6bBvjn5OJQnuN4T_3lKsC980CehuR_Bx9oDjBxS6I395bvmIjuLzEKrvwb3lvaF3ohbHhn6h_DExERV2F7XKqXh4yOSrls5L0lBvRrLmOpJiLxczH8Ivfd5OHZwE3fdI1cWPsKTHml8oDME3hu-N2xBhq7PnHxfl1zNysvwHlPqRPD0WI0J6JysbcmuZv5BIJFnQafhzNqpNms7vLatzqTBgPVOY9hVVcjMsPA7slLxkQKmUX4Wkd6KX8aIbz3yoAn6egVNH7KdwMSmoLJCltdR3JfvtcNRBbk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=UQuD5rQedljy2-qJj_imBZPCQhY96T31Pjc_KK7_IB9XnTwvvR73M3aZhfwRuS-fGzGFej5Hyq1BYyd_QZ1DuqIPP6yV3zjjLWA9S_CtSH0I85MUTqInw3fPjX_AME08ZKdUYxyyzOFdMDXTaEKiZEXGHUJ4VggQ7TTeDxe8-ANLMDjNbMakgTiYNlNiZUenHlXIM9wvbfY-9lwu1XI0jIt-N2R1297lnIrEudG8L-t0zxkpFHdon9S8TG4csoU5mQXB2FV593WQT2ctpPV3Is6WDvauN6-K-Dt2dIduM2YXhau9D5i0k2FuNKXBtJFwXCnqRfthvRHFZ-ewP3D7szVljGH_wNgWonv09z9ZIpeLbXPIihYZHF-Ku5adWmWvdIb4ykfKk6bBvjn5OJQnuN4T_3lKsC980CehuR_Bx9oDjBxS6I395bvmIjuLzEKrvwb3lvaF3ohbHhn6h_DExERV2F7XKqXh4yOSrls5L0lBvRrLmOpJiLxczH8Ivfd5OHZwE3fdI1cWPsKTHml8oDME3hu-N2xBhq7PnHxfl1zNysvwHlPqRPD0WI0J6JysbcmuZv5BIJFnQafhzNqpNms7vLatzqTBgPVOY9hVVcjMsPA7slLxkQKmUX4Wkd6KX8aIbz3yoAn6egVNH7KdwMSmoLJCltdR3JfvtcNRBbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بیلبائو به اتلتیکومادرید توسط ویلیامز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105610" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105609">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105609" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105608">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=XxD3yu5H4ieLGPJECP2rZPAASvMovCAFnIrogF-UvInoLQumKEo9VEQwNfVNOJ1uXgSH-i7nmZWaMGn1BMlz-0ug-1Egbv2PKDRP83RDYTR1bAllQO-Dpl125q5GaH8fjqVrSsuhAxpkQenrkP5vJux9rB9JgLY1ehAP7u2vjfgyEGoKQJWC3wHT_R97X9c99qZtEptFuBnjNFWFVJ6c6Z1z6hMJbRSW4tr8vHPvkOGlRwQqNoJeocAYYZx9Jw0u7IOP2bSJbJImGIpchPJB6Orb8vNUo8H6oOM5e2FybK_drkVuPpj2diJ4GjGsMs8GA6tEbbR0MUtgJ0w6riQleg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=XxD3yu5H4ieLGPJECP2rZPAASvMovCAFnIrogF-UvInoLQumKEo9VEQwNfVNOJ1uXgSH-i7nmZWaMGn1BMlz-0ug-1Egbv2PKDRP83RDYTR1bAllQO-Dpl125q5GaH8fjqVrSsuhAxpkQenrkP5vJux9rB9JgLY1ehAP7u2vjfgyEGoKQJWC3wHT_R97X9c99qZtEptFuBnjNFWFVJ6c6Z1z6hMJbRSW4tr8vHPvkOGlRwQqNoJeocAYYZx9Jw0u7IOP2bSJbJImGIpchPJB6Orb8vNUo8H6oOM5e2FybK_drkVuPpj2diJ4GjGsMs8GA6tEbbR0MUtgJ0w6riQleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده
روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105608" target="_blank">📅 19:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105607">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تراکتور زدددددددد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105607" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105606">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105606" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105605">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105605" target="_blank">📅 18:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105604">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=e7WTuTvqN2UkWm1ThPIlwZ0Xlm7dDQZlWwoYnatFC5vajrQ0JeZ0QmgZZneqz9XSrt9iE9DdaKrkChioQewJte8lsm08o5T3jT1f2-xh0T9v2BUqRMbXu8-teXbRzz-Yg8DZVyiLF6WZUOv_t27xIwNPZfMnUZi-bUj_Ie0-zw8jgonbu3myG8-yiwD2x1GatATQhZ3G78PJipIacxUYEU8JaZQz-c7xEhjZqBbH-9HnjhibaV8HoPIyvcwa7t8UVoRe7F8oLrS6NsxGpl7bSZ_vW22WjPCIvxcTIkS4oXRevj7J_k-P33MgxPVEvSHPTbqmlW893rEp0qYaEp5vtEFC1K_oSik-LYZKUWZUJ2rOKEJrh1JIHdKhJtSUlHQWeCYBcgvlFz6_wO9iFX1mLHP9hZM1qfgWoYNFNUUJDkbrcv2uHUpkxebk6qrKTjFH62yEBF2NAyCnnf_XuBrT44SRCyRjk-A-k6mQ02wQfN1pJfIB0ykiW6GLuxYPa4KT9KjM5WTH8vZL_i6NCVURjqE0nt82yJqk0G8HNXeRfNk9X4QZ-Up0y_L7N4FfXB0aGFv2VeMJc8kKWOsGf2yARihWqt6YRSY4vc_l47IzDcF0sbBcl6bHHB2ptKhtifRQ5tmID33pzNAg_AdueXF4ZYjVF4uoL77Q0jhJzE04kBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=e7WTuTvqN2UkWm1ThPIlwZ0Xlm7dDQZlWwoYnatFC5vajrQ0JeZ0QmgZZneqz9XSrt9iE9DdaKrkChioQewJte8lsm08o5T3jT1f2-xh0T9v2BUqRMbXu8-teXbRzz-Yg8DZVyiLF6WZUOv_t27xIwNPZfMnUZi-bUj_Ie0-zw8jgonbu3myG8-yiwD2x1GatATQhZ3G78PJipIacxUYEU8JaZQz-c7xEhjZqBbH-9HnjhibaV8HoPIyvcwa7t8UVoRe7F8oLrS6NsxGpl7bSZ_vW22WjPCIvxcTIkS4oXRevj7J_k-P33MgxPVEvSHPTbqmlW893rEp0qYaEp5vtEFC1K_oSik-LYZKUWZUJ2rOKEJrh1JIHdKhJtSUlHQWeCYBcgvlFz6_wO9iFX1mLHP9hZM1qfgWoYNFNUUJDkbrcv2uHUpkxebk6qrKTjFH62yEBF2NAyCnnf_XuBrT44SRCyRjk-A-k6mQ02wQfN1pJfIB0ykiW6GLuxYPa4KT9KjM5WTH8vZL_i6NCVURjqE0nt82yJqk0G8HNXeRfNk9X4QZ-Up0y_L7N4FfXB0aGFv2VeMJc8kKWOsGf2yARihWqt6YRSY4vc_l47IzDcF0sbBcl6bHHB2ptKhtifRQ5tmID33pzNAg_AdueXF4ZYjVF4uoL77Q0jhJzE04kBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
تمجید لوکا مودریچ از کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105604" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105603">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105603" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105602">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reVHXGgZqr1xM72b7hiZSedSU69VLG9m0rrrxJA6V0E13Oc2rpg9Hz7gmxVBbYSdVk91-GUwa6EAxSG3pFB84rqpKEEERaFxrLC6ok2Ri2n4PwgINq89x9hiGIdx8WK1K2TrA4Z1h1sVOoMqhKpdcJoSxyC7deGJzGOyh5S6uwKg7dsEvIoWfhWHmYHWliCZc7Y8fl_5P4b3k3W9_cTHHeSC-vUsHcgRDPc8WnQyPFl5BT5iK1RZKhFren11dRGvWf9JfV-ioJ-k7fVsT836Hb3gDda1eq6f-OtZotY2bl_hS-N7TRcg0Tm1-nb6QrmDz01AoSyGInhbvz0FBiPkVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105602" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105601">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=fSWFgge7FtXCUs8go_i9TS8LK1UjC-yE6Fcdqt3nEbg7ogZivO7MwijkMiV_6wnDMieVsivsNwjATR8bF_-TxftXX4dzxU4leK8vheU493wPThKi3n_Eay7xK0VdFQtLFbMDgIQ5IUQPbvCyOBUbYOxGjogaMIQnQjGG5wLhI7Xxf3QHoJ4Zd_Tm9cgSt0eIx2UgGXgQUKd4HDaQG0AQvcwqrYUeIffQlviSgH_LSOGMF-yM7I7p95MqxfWXa-z5m2p-SpLnGVJsNGqWvnhDq52VKsVrff0I9_lA5CkWRGwQYQHfQl4rc6NCvafeKogSbI_PX6x5sP58IP1QVeEhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=fSWFgge7FtXCUs8go_i9TS8LK1UjC-yE6Fcdqt3nEbg7ogZivO7MwijkMiV_6wnDMieVsivsNwjATR8bF_-TxftXX4dzxU4leK8vheU493wPThKi3n_Eay7xK0VdFQtLFbMDgIQ5IUQPbvCyOBUbYOxGjogaMIQnQjGG5wLhI7Xxf3QHoJ4Zd_Tm9cgSt0eIx2UgGXgQUKd4HDaQG0AQvcwqrYUeIffQlviSgH_LSOGMF-yM7I7p95MqxfWXa-z5m2p-SpLnGVJsNGqWvnhDq52VKsVrff0I9_lA5CkWRGwQYQHfQl4rc6NCvafeKogSbI_PX6x5sP58IP1QVeEhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
فحاشی هواداران تراکتور به امید عالیشاه در بازی مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105601" target="_blank">📅 18:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105600">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKC_1eXeDRiK5DYCI1dJ-_hqXhUbIuauByZpdfRBhi8t0GGMic2vF5kHoe8qcJFGmYep2YxKYJ3DWRXtMmTSnFX5m2oVU2Wc7OrCUDxU5a7cx8hPTIkq3uoVxJsYNe2-k7a0-oPHMFUqrf8Zl_plIYczn2kIGG924M3Nfp8yR5UoBMFJpT34u1UWwEHZz6vBMYzgh7ne0CAILbJgGlfawvvGSHb9sTX1WtzKvOZ5EPRDVz_pjFfJaTG2fZsrJ3vfJWgjNunp9kPgC1itS7ndovEZSl_mKVBzFAwET5v2R41EohpTwKEYMiH0q0yZ6ReHPwW_25tznuWF7otzV3JHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🤯
🔵
هالند مقابل تمام تیم‌هایی که در لیگ انگلیس با آن‌ها بازی کرده، گلزنی کرده است، به جز یک تیم، یعنی ساندرلند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105600" target="_blank">📅 18:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105599">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRBijhBxhXgZbmyPiGEI0jEX_Sdsmfn3uwpyN1nu6Hd-XBQkQRdfmIYXwZIjR3eUhRsp3XQwdfeHo_VvztetDhibvoHhRHxxlxNV-1S7QN51Agp0KcvlzNNPkLingS6TKpnbZSUcskSqPjP8GI4oZqDhCvgF0sg4wrsTCI5pK1_wqiJF35VAqmEX4cut6QK_iB36d4oDdba0DJAmSKuT86yVr41f6guO4c1uZtaA689TU2ifjXpC0UJyFwU9aqUEKfPcSUgllmZbMjimLISqdOSKhBcyPptt_Xi1sXbGegdJ5pIcBJBwdq7WDtjukEWmsgWDZzJHDLmWhienlaFcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اصلی اینتر مقابل ناپولی؛ ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105599" target="_blank">📅 18:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105598">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpNpMMVTBmP_t46Wymfv4LDf2LIupGNt0xD6uBjG0DY3B9bZvYyi7kqTYsPl8PY-PmudV0z_a4vFZquHt9oQbhd-nHGtsYJ_y9pTLjtLAQzqg64qfbG2bEmc3h5dVMBXCps8nNWeCuB5Sr-VIfWDAVFSvjXEUVnDLbXYfn81V7Lu2X0JgoYAJj7AC8Q4RQhzr9SrADrtmnT5Y4s3fhWXdPigyh0arTvRfuTHPTRSpbtOgWJLemlufhyzUpld_ZjIGQ21a_Y2XxlPs4i5odlCM-bSWu7WsZgSr4LAM20Rr1TDnvlN6Q5xlz64XLwhFnFpMJiPpnUJ9_EkhFiOyGCahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خولیان آلوارز امروز هم نیمکت‌نشین اتلتیکو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105598" target="_blank">📅 18:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105597">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=c2oJtHqT01n3IbEGeUQz7ghgxmhCvgTjL1vBCNLXylmOs7_jBBAlETI10AwWY766Pu2fXSakIvaveiOnJuARnqw5SCKkhPQZrkAwsLEVfv98zhiyhULUaT--dOl_90AMT-HxtmZHuuDlaBLn06lxBhBj7yTIqroTwgJrRx-uYsDzkRsGclO7ak8QQIe_DeBPmnH9QUAq9o5JXFCYwbnscihmeV2pebvSwqCHwftl3mBAohNsY3-q0T9d9JxCiN0oUzD6kgFg1ZfsELFVN3twKtfRL6aCBYTDVWa_Gp6YPQSYORgHuCl3vh_PAFjeu0AW_jZeyDzbjlsFT_iRQncPsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=c2oJtHqT01n3IbEGeUQz7ghgxmhCvgTjL1vBCNLXylmOs7_jBBAlETI10AwWY766Pu2fXSakIvaveiOnJuARnqw5SCKkhPQZrkAwsLEVfv98zhiyhULUaT--dOl_90AMT-HxtmZHuuDlaBLn06lxBhBj7yTIqroTwgJrRx-uYsDzkRsGclO7ak8QQIe_DeBPmnH9QUAq9o5JXFCYwbnscihmeV2pebvSwqCHwftl3mBAohNsY3-q0T9d9JxCiN0oUzD6kgFg1ZfsELFVN3twKtfRL6aCBYTDVWa_Gp6YPQSYORgHuCl3vh_PAFjeu0AW_jZeyDzbjlsFT_iRQncPsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105597" target="_blank">📅 18:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
🎙
🇮🇷
حمله رسول‌خطیبی به هواداران شیرازی: لابد پارسال فجرسپاسی قهرمان شده و من بی‌خبرم‌. یا من فوتبال نمی‌فهمم یا این چند نفر هوادار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105596" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇺🇸
سنتکام این ویدیو رو‌ منتشر کرد و گفت امروز سه نفتکش ایرانی رو با موشک‌‌ هدف قرار دادیم
نفتکش "دانی" را در نزدیکی جزیره خارک و نفتکش "استارک 1" را در نزدیکی جاسک به طور دائم از کار انداخت و نفتکش "کایلو" را در خلیج عمان به طور کامل نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105595" target="_blank">📅 17:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105594">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇨🇳
🏀
ژانگ زییو، ستاره‌ی 19 ساله و قدبلند (2.23 متر) از چین
🥶
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105594" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105593" target="_blank">📅 17:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixv-GINYk7AgClNeAnf2rZCJ4BB6uXqf4wkPFNQkiqH4J-DJ6iBYS-BD2cbeZEBC7OQV_wiNvql6U6mImW-bOrCxqc51T76a6aHbiABn_an-Smg4wFSEwFi80vcqevM52h-K6x_c01G5CtOkQ7ou1tnYMQOhdKiTJXOoROZMZk048TSAZYp1bOjnVSx-1oH3zHDB4PeuzCRFJuqcWT2tLPIL3oA-qhPaVHjTMDJNkNmky5guNccJwlY-dVdKc9cmmS3lZeI-qK4zvgz37e5dY8XPpSJvBEH7KvmCWRKOHGpSeCIThywy5i6fFSi9fcfAElqBiqcEVD-G11gi02AGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
لیگ برتر ایران؛ ترکیب تراکتور مقابل گل‌گهر
تراکتور- گل‌گهر (١٨:١۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105592" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=HidpGq7GtQArNxzFeYzE0h88tTw1Cqw2JiS6PAso7yqhHCcUs6hz_v608YIVEpRUCBIegQLpL6B673kig2YkP3_Z0TKP1CV-jHLlwrEvydsEKISCcRqIXzo-ZgwybNkffaIfFrEJwqgQr_bHjmDYaEhP3i78q-FqVPnXJcZkGM1_tB_oYvDlZOlinTiHBLpWBH4c-nt1fa-XC-nb24fAQdDoqY9--igXQEpq6Vp4Yq_dSSEMOs0Rqu7QmFSKhg0ysU-XRlYUcSioaPaw2I_w0FxJYC9OLqsvERfJ5hE1XtFcyzcB654pWoeJmBAURo2gi60tuR7NBlABAFdP8q9cIjDHJpVgrHEVuSBHE8tG0sQfyX9G14GurfDb79e7uBz3BH4deXHm6XgO_ajbYCVC3gh6Xa6K6-uRHIUGBTPftT5S7gl7UYuMpovOBlKwrJ6bWqR73BJr1YCCuEhTRqyYAPzVe1oFoyMg-rKPhrw0jAt7sTELk-0jFbbx4ikpfsHS5332W1spSANJkCzEWxqwiHf8_or8zOb77-Gg169ke-xAKFO-OOKcSsv-IiX75AZ0ZFmH3AHXQZ41Jk0nX1bB2WMIbnjPdNdaj2-yW5MRn4a0GwoXFzIH2sCaDLIgqaF0hDt9MSn2HJecOKogbFdCnTSi81nRNpZcxyyMV0nW_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=HidpGq7GtQArNxzFeYzE0h88tTw1Cqw2JiS6PAso7yqhHCcUs6hz_v608YIVEpRUCBIegQLpL6B673kig2YkP3_Z0TKP1CV-jHLlwrEvydsEKISCcRqIXzo-ZgwybNkffaIfFrEJwqgQr_bHjmDYaEhP3i78q-FqVPnXJcZkGM1_tB_oYvDlZOlinTiHBLpWBH4c-nt1fa-XC-nb24fAQdDoqY9--igXQEpq6Vp4Yq_dSSEMOs0Rqu7QmFSKhg0ysU-XRlYUcSioaPaw2I_w0FxJYC9OLqsvERfJ5hE1XtFcyzcB654pWoeJmBAURo2gi60tuR7NBlABAFdP8q9cIjDHJpVgrHEVuSBHE8tG0sQfyX9G14GurfDb79e7uBz3BH4deXHm6XgO_ajbYCVC3gh6Xa6K6-uRHIUGBTPftT5S7gl7UYuMpovOBlKwrJ6bWqR73BJr1YCCuEhTRqyYAPzVe1oFoyMg-rKPhrw0jAt7sTELk-0jFbbx4ikpfsHS5332W1spSANJkCzEWxqwiHf8_or8zOb77-Gg169ke-xAKFO-OOKcSsv-IiX75AZ0ZFmH3AHXQZ41Jk0nX1bB2WMIbnjPdNdaj2-yW5MRn4a0GwoXFzIH2sCaDLIgqaF0hDt9MSn2HJecOKogbFdCnTSi81nRNpZcxyyMV0nW_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
لحظاتی از مسابقه طناب‌کشی تیم ایران در بازی‌های جهانی عشایری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105591" target="_blank">📅 16:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fca94904.mp4?token=KNORPgSzYphI-BAk7rX7vQ-Y1sLHO90S7NYUkL986WEpIjfYHD79rvSb6XEnS5g1Z2VxERDASB_5eS8Js1fiqh26xnV_n5Yyj0BvKQlZdm3ur0LQOjy2Bwv55gmERLk8co7C7jg6pkuN8yQ23Iqh8J9DrANxBTFPuXvJ95t9zbQ092u4-xzFjF2W0gAEyF9IuoTAsYf_RJGowHuKd2RSrv7GGBOz_Dgo23kH2mOWPYqCemrFTrvB-hnxvAhQFsfLdv9p5xgJeSoz4am8wptkCS8_0libwOWPx6I--ZSMK4HjG5a3HANLKoCqYxN8XrJlYgZqxkUBreiO1QxhJo0fGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fca94904.mp4?token=KNORPgSzYphI-BAk7rX7vQ-Y1sLHO90S7NYUkL986WEpIjfYHD79rvSb6XEnS5g1Z2VxERDASB_5eS8Js1fiqh26xnV_n5Yyj0BvKQlZdm3ur0LQOjy2Bwv55gmERLk8co7C7jg6pkuN8yQ23Iqh8J9DrANxBTFPuXvJ95t9zbQ092u4-xzFjF2W0gAEyF9IuoTAsYf_RJGowHuKd2RSrv7GGBOz_Dgo23kH2mOWPYqCemrFTrvB-hnxvAhQFsfLdv9p5xgJeSoz4am8wptkCS8_0libwOWPx6I--ZSMK4HjG5a3HANLKoCqYxN8XrJlYgZqxkUBreiO1QxhJo0fGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
هوادارای بارسا جلو کمپ تمرینی این تیم منتظر حضور رافینیا بودن. حالا رافینیایی که جلوشون دراومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105590" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKjEQPTEQ8C8Z1oRZuAhHQhjsldbGHAiqAP-jyDgOhL_lPtb624a-xeTEWWnKSZ2a-n7au8p3_8tTmokzO-uq3Zk6EyEDEdZRZMJ1NaSeQc5wM6hcPedvTE722eAALT6aWph7ke21gxs5eirPRv9w4ERuvrTPMluzDEe2dD91bZF6IyimxJwZsudF3URoqc1dlXTh64XgUAUmsREYkRqwn3o9cpJlIV0kAWu_C8JiTiwwV9kFe0K9gQh9tF7HTIt9No-Sl4XnGP6CUSb6yzcoKpqts_o-88KUCrt80Tx-_cb49qyEC03g9tf2V2soUQHembXSGeq1vA3Z0Vg0-hKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس برنده شدن باهاته!
🎁
تا ۲۰ شهریور
با خرید هر بیمه‌ای از اسنپ‌بیمه در
قرعه‌کشی موتور یاماها، آیفون 17 و PS5
شرکت می‌کنی
🤩
چرا با اسنپ‌بیمه بیمه بگیرم؟
✅
با پرداخت قسطی هم می‌تونی تخفیف بگیری
✅
برای هر سوال یا مشکلی، پشتیبانی ۲۴ساعته داری
✅
و در قرعه‌کشی
موتور یاماها، iphone 17 و PS5
شرکت می‌کنی
این فرصت رو از دست نده؛ چون با اسنپ‌بیمه شانس باهاته
💙
وارد لینک زیر شو و جایزه ببر:
👇
👇
👇
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105589" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
‼️
🎙
مُچ گیری عادل فردوسی‌پور از محمود فکری: کُل دنیا دیدند دارم به صورتم گِل می‌مالم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105588" target="_blank">📅 16:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29285b8410.mp4?token=IZGXPQ1KF3hBGTmGPpU5oo143t6kVMT4cgel7gt-saTlzVn0bBR1D7cn8RPqQY4XP5n6d87cByXIqFchhmNE95mEkQJN2TstkqMuCLGlSlLcbJI-jZW2pMcPtoPs3AipHARYIPjunH-UN_JISXNpsYrTRoDJN_pw5OpyWPZ1a66udJ12_zj9wKkGh5oKqx9nYeoFeUsrlWHqyBYEaRK0Dhb3xRD-G3nkTV2SQTSsBxCwBIQhQlKxscAscTlxyavbK-RCN3D5_UyMk7GB0UUpDoaWu_4tlobnTvB4MTDKVVdXZomODSiRWGuaIpzlKCcrWCwM39bn_1Rv2UTex9qGkax_y7jOc33Ca1xeibXNhVq_vSCt4tNv3dXV--vPZoRqZ9oNL8uXZda96_KXuFcypC0y5zMrBNd_5oYyuGmDY1-5xV10vd0w-_wxt97YP-hk9vX7YlQ_w3amdKA6EsEqwxLeVWX_86wg0r9eU_Rtisv1SWS3XXZRsiUQsnREIBu0iowlCX-YqNSFMslSzJIBZi-rP85dDnYhdTYxi_ZCWCOZc35XtmKVTUB5U_-xb0ltqm_BAA4AzGrZLzNTwgUCdn9RLBhd_A4C-72Bj20OgGzdOt0QQE376x5VXKkUPjsV_B7cokqjqKw0YT-Lmwv7aYxqd5qi4CE_5dy0NZyvWXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29285b8410.mp4?token=IZGXPQ1KF3hBGTmGPpU5oo143t6kVMT4cgel7gt-saTlzVn0bBR1D7cn8RPqQY4XP5n6d87cByXIqFchhmNE95mEkQJN2TstkqMuCLGlSlLcbJI-jZW2pMcPtoPs3AipHARYIPjunH-UN_JISXNpsYrTRoDJN_pw5OpyWPZ1a66udJ12_zj9wKkGh5oKqx9nYeoFeUsrlWHqyBYEaRK0Dhb3xRD-G3nkTV2SQTSsBxCwBIQhQlKxscAscTlxyavbK-RCN3D5_UyMk7GB0UUpDoaWu_4tlobnTvB4MTDKVVdXZomODSiRWGuaIpzlKCcrWCwM39bn_1Rv2UTex9qGkax_y7jOc33Ca1xeibXNhVq_vSCt4tNv3dXV--vPZoRqZ9oNL8uXZda96_KXuFcypC0y5zMrBNd_5oYyuGmDY1-5xV10vd0w-_wxt97YP-hk9vX7YlQ_w3amdKA6EsEqwxLeVWX_86wg0r9eU_Rtisv1SWS3XXZRsiUQsnREIBu0iowlCX-YqNSFMslSzJIBZi-rP85dDnYhdTYxi_ZCWCOZc35XtmKVTUB5U_-xb0ltqm_BAA4AzGrZLzNTwgUCdn9RLBhd_A4C-72Bj20OgGzdOt0QQE376x5VXKkUPjsV_B7cokqjqKw0YT-Lmwv7aYxqd5qi4CE_5dy0NZyvWXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطرات شنیدنی ستاره سابق آبی‌ها از دربی شش هیچ؛ قراب: همایون بهزادی زبیاترین گلهای تاریخ را به تاج زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105587" target="_blank">📅 15:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=QFPTCUM7DDVKAwVB9y_Ipg4C6pdLbslHcRxlbDrt3QgeJCb24sKReUAzNWcQy-1ExiNblFXnoiUjdJXW5jUsDuo4obcLz68g8-XzsbEiN1b8w_k3F2IFx39otR2EdyKvVXv1hGPfkW0xnJjWu8cw7jTYdNlnteZPoGOa-nqVjxQbBW1Ju8qRc37jt5Vgj2wthZBC5jK4LsT_wEm5RLeUpwaSJVVYPAY65TJyrNwg1_69UC9vxBQkMmqbLOLD79YSU9PosWF1H6XBzCm56JWWhUnx5NeH_KzNfK7w-dzvxUP765N_1z6vmws2FeeODZ7HPqXg9IvavcI5CIP6AfNiRDv4YXN48O3ESf_IqgIlGPiwGEiGp84bUJUmz9FJ6XXqxmzHgosBR3lnk-vyT2zxb3IP0fHtB3jG86vvhfx5snmSrFsib9KbWk-jtHe35Z-8oyDgqETi-L4CPVK4vLVuBI4uQbFW7zRAvOnBvkXfjA07Mkbz0ZBDP6jMSpVcr5mp5y4ovAs5Iaae2o9fsJZo6X23Yvu-J4EudZ435pmSnNfM90wroBqZQnT8yx8If75qn9HcD8L3PcaRgWH35Dk7jmcbs90sKhAk7S7INX8XbDbOmuRXPhMD3gqo9Bmcwvsgx2P4zEYAN0qBgH61vptm2yffVcmqVzDcNdacLMa-Woo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=QFPTCUM7DDVKAwVB9y_Ipg4C6pdLbslHcRxlbDrt3QgeJCb24sKReUAzNWcQy-1ExiNblFXnoiUjdJXW5jUsDuo4obcLz68g8-XzsbEiN1b8w_k3F2IFx39otR2EdyKvVXv1hGPfkW0xnJjWu8cw7jTYdNlnteZPoGOa-nqVjxQbBW1Ju8qRc37jt5Vgj2wthZBC5jK4LsT_wEm5RLeUpwaSJVVYPAY65TJyrNwg1_69UC9vxBQkMmqbLOLD79YSU9PosWF1H6XBzCm56JWWhUnx5NeH_KzNfK7w-dzvxUP765N_1z6vmws2FeeODZ7HPqXg9IvavcI5CIP6AfNiRDv4YXN48O3ESf_IqgIlGPiwGEiGp84bUJUmz9FJ6XXqxmzHgosBR3lnk-vyT2zxb3IP0fHtB3jG86vvhfx5snmSrFsib9KbWk-jtHe35Z-8oyDgqETi-L4CPVK4vLVuBI4uQbFW7zRAvOnBvkXfjA07Mkbz0ZBDP6jMSpVcr5mp5y4ovAs5Iaae2o9fsJZo6X23Yvu-J4EudZ435pmSnNfM90wroBqZQnT8yx8If75qn9HcD8L3PcaRgWH35Dk7jmcbs90sKhAk7S7INX8XbDbOmuRXPhMD3gqo9Bmcwvsgx2P4zEYAN0qBgH61vptm2yffVcmqVzDcNdacLMa-Woo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پریمیرلیگ هنوز شروع نشده، جنجال‌های داوریش شروع شده!
⁣
🎙
📹
مایک دین، داور بازنشسته پریمیرلیگ، توی مصاحبه با پادکست جیمی واردی اعتراف کرده که زمان داوریش بعضی وقت‌ها برای خودش چالش می‌ذاشته؛ مثلاً ببینه چقدر می‌تونه بدون سوت زدن بازی رو ادامه بده یا چقدر می‌تونه توی دایره وسط زمین بمونه و ازش خارج نشه!⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105586" target="_blank">📅 15:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rGibcEXWG2-x3HM0dgQy0Z9_mB_TKc3W2D7_oT8oQOg0FzkEL2iNnCWehI5DhWaW0N7Q7df5PXshxMFgBxXTbPY2lLZV3LN1LzUBmuT1WoiCRJhfgD-KA89SI5zEeK4ar4qB1cPSY0u725R4whHKm47e6F0un2ydB_tQaOtPmK1fYitqF0wogQ8Pq0nHGKR_8-8RrJIHKZZkhzsrN-JLZqwQ8e7b0HXgbl7LvNEj4tz7tdfvfxX9iBm1-YEbYimgTzjm2qYGsbEVbOZabFRYEVYVaIaw8ArMuzqVZS_olM2WWPsRDollHFIJJhRtYmwBJ7_66vDm5J4SXcYK0fwkTRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rGibcEXWG2-x3HM0dgQy0Z9_mB_TKc3W2D7_oT8oQOg0FzkEL2iNnCWehI5DhWaW0N7Q7df5PXshxMFgBxXTbPY2lLZV3LN1LzUBmuT1WoiCRJhfgD-KA89SI5zEeK4ar4qB1cPSY0u725R4whHKm47e6F0un2ydB_tQaOtPmK1fYitqF0wogQ8Pq0nHGKR_8-8RrJIHKZZkhzsrN-JLZqwQ8e7b0HXgbl7LvNEj4tz7tdfvfxX9iBm1-YEbYimgTzjm2qYGsbEVbOZabFRYEVYVaIaw8ArMuzqVZS_olM2WWPsRDollHFIJJhRtYmwBJ7_66vDm5J4SXcYK0fwkTRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
🇮🇷
🇮🇷
لب‌خوانی صحبت‌ها در صحنه جنجالی داربی؛ کنعانی‌زادگان درخواست احترام گذاشتن داشت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105585" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0gekWzKuK0kPmpYJ0liQW-1w2R0sGss-UIgEjBvaOKHHFvAHQFSv6rayQgnTCskX7-V4mSWEQq_KeQ01nay2e_X_4FR_glBhYj0OP5JuN-HJocAjox3Licg1GqT4TWdHn8DkNPk246NOFGAfVyE-AwwYw4-UBkTPMhIhLJ8VuAbmZz9f_3AN5QRfDTcsA2w2trgDlqvPmApCHpj4k3chJrfO0ZFmUSYVh4kKD7fO0AaHsmSNpuXmHbu1AS4pb-t4Rc6iaSrfFK6U1GDsh9GxuKVsw3eViN1zkH978DlArBLlhknAYceTUmLfVPTBFZW_2V_1ItLHelvbdGnjgVefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇮🇷
💸
هلدینگ‌خلیج‌فارس مالک باشگاه استقلال اعلام کرد که در ۱۲ ماهه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به کسب سود خالص بیش 187 هزار میلیارد تومانی شده است که در مقایسه با مدت مشابه سال گذشته حدود پنجاه درصد افزایش داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105584" target="_blank">📅 14:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105583">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=BY-IawaQnGYHYXKJlhT2y58RNyXmD7QkADVn_WP5j1YoZ2bseP2BH7K1OejC6Q281Kv-2Cop07QF3_BjdR3qAYM29EgAlHEZLkbkz1JWFJw92yR38626YWNIMhecyYHQYW89xmwkYDXPNjKgyNv7o1yfQLC1ZmLYjqdLERgdHL8vIQa6y3hVfVjQyL2BANrywY70XvW3mqi92lw4SVGlEiHxGwYWoLhwZs0B6411iGfLsbBif2fJOYzjPqSvjbFrmvDJXGxPM5Lqq9Sp9vTSfwUZPOPu3k23IiN83PexGBkX3xexRtOXMr_Jhf8Q4SWLbIDL9r7DqtvHY_3iwI1jrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=BY-IawaQnGYHYXKJlhT2y58RNyXmD7QkADVn_WP5j1YoZ2bseP2BH7K1OejC6Q281Kv-2Cop07QF3_BjdR3qAYM29EgAlHEZLkbkz1JWFJw92yR38626YWNIMhecyYHQYW89xmwkYDXPNjKgyNv7o1yfQLC1ZmLYjqdLERgdHL8vIQa6y3hVfVjQyL2BANrywY70XvW3mqi92lw4SVGlEiHxGwYWoLhwZs0B6411iGfLsbBif2fJOYzjPqSvjbFrmvDJXGxPM5Lqq9Sp9vTSfwUZPOPu3k23IiN83PexGBkX3xexRtOXMr_Jhf8Q4SWLbIDL9r7DqtvHY_3iwI1jrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
آیا پنالتی امباپه باید تکرار میشد؟⁣
📹
تحلیل صحنه پنالتی توسط روزنامه مارکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105583" target="_blank">📅 14:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105582">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PN2LSFoSPtSoGSEfkJLqjiYrHMTPUtzFphcUgFPL-zlEehMSRRanJdOyS84eQ_l5_aIdj95YjG1we07WjB2KNcnrSn_tzzcKikpp4YcrLs-cBcDjQxwJ2L2KlTiZJuB2MQ0J7cwbyBLEHaNf9i7k-c0gYGXKetHRHyyRmbmMNE3tsX-RS6c7H94Pu3S8cZpTgk4jX8BrocsbMiVd5rZWFPzUGwoVqduJVOwIRKLXU1HXz00GthckqwWbadWPYb0MzXPJih4vu91ElmfhB-qYa8CrhSgi0AEq4GIQ6qjLwA8FqGGLMTZrs5EEXW6mrG3m5nBuzEDmJdAUi5H-fTgIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PN2LSFoSPtSoGSEfkJLqjiYrHMTPUtzFphcUgFPL-zlEehMSRRanJdOyS84eQ_l5_aIdj95YjG1we07WjB2KNcnrSn_tzzcKikpp4YcrLs-cBcDjQxwJ2L2KlTiZJuB2MQ0J7cwbyBLEHaNf9i7k-c0gYGXKetHRHyyRmbmMNE3tsX-RS6c7H94Pu3S8cZpTgk4jX8BrocsbMiVd5rZWFPzUGwoVqduJVOwIRKLXU1HXz00GthckqwWbadWPYb0MzXPJih4vu91ElmfhB-qYa8CrhSgi0AEq4GIQ6qjLwA8FqGGLMTZrs5EEXW6mrG3m5nBuzEDmJdAUi5H-fTgIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
وضعیت دیشب فوتبالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105582" target="_blank">📅 13:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105581">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACNSvTwnSqAFppks4HnY46JzQc2IxGOUrgLMA6I533Lant5BmqU8F3b8RGpmSh1-MF1Hy1VsrpK4kcd-VphjpEiSYT8zKAsVXuh5TyUfJCJ-j9KodfiaESiFEJHXLIb_WLRcx7dM0mtgiVl1NJk0xH2ZX1CkSjUan95wLsyzBqzmUWBqwi61Z7Y9ZSpPvQ_FXni5-0ABuzO15JYTWLwb9q4cjuW8dWe_pC1a8qM6MVbq4V8e718W06k1HgTi1cRPdzL4fDXy6MWBBbEEki38Gf-Duis-0PCCCPdueU1Vwi1JUCL1haDb5hNrtgKqZ7IpMgZzERiXsMZnZyhrXtrATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
20 تیم برتر جهان، رتبه‌بندی شده بر اساس ارزش‌های بازار، طبق داده‌های سایت ترانسفرمارکت
💸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105581" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105580">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105580" target="_blank">📅 13:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105579">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105579" target="_blank">📅 12:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
‼️
🇮🇷
سهراب بختیاری‌زاده درخواست برخی از پیشکسوتان و بازیکنان استقلال برای بخشیدن صالح‌حردانی را رد کرد و نام این بازیکن را برای بازی فردا مقابل آلومینیوم اراک خط زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105578" target="_blank">📅 12:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105577">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105577" target="_blank">📅 12:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇪🇸
لامین‌یامال در آخرین تمرین بارسا پیش از بازی با والنسیا بدلایل نامشخص غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105576" target="_blank">📅 11:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105575">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzGAwe8e5Wj81rEIEBpig6-oBzW90Y2JGiR22z7oDbkDINKI4dZm12_BOSK-3eeQsreTA4hCNo6o2D6icZ3vTEM8m6RwkyML-qbKJNgOhgObzKLGtAFim4ijkNHDXHnr32OF7fcK-R8v6hagDM8okbF9gc3gfWkZ3r7Oy1F8I2wCW6mGc7BMPuNZf030VeQMDg10jXqJL6UCiYRdi9MLDAPnUXrnGPZhX1d_eOpF5HgCcDcUKmkVhqi0gddHY96eJJnqtbLPtw-1mIPROjYatdnIpQFda-ne-JJd3jSrC3zdiXRdb7nnhO3Mbxe2dxnxzJvWwYnhSgkbqffKsWM2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج رئال‌مادرید در ورزشگاه بتیس از سال ۲۰۲۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105575" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
زوج فوق‌العاده پشم‌ریزون ازه و اولیسه در تیم کریستال‌پالاس دو سال پیش رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105574" target="_blank">📅 11:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105573" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRtU-qoICwppvaN8uiQ_uIY_SQ89mZ1fD3n8Zg59Gyv3R0WjLWmTYxae4bnVJRkSHhe-aojIbZM4zmd93ZyqLBIJ0KyRTm1_7EyPDTK6oFaphAxR6dnIO3bIIoVL-xbRiUW4yiNoD-blgWj9a_YE9_71IkG2Twkh9Gbtpixgz8jlBXuaP89P4-vZ5IbMhZSEItRnuREnWn0zo97PSubn36AVhTXDls0xEpj88-RbFdU2ekRwT6V9R-Vf1nshjJsrV8S2T0Lx2YqYyag-xx5UOHTDLpD1_HWDsH6tGkuUtToWZa3MbAEt6SlYk-KCiyQyVpwHlteNCvOKmgYnoLM0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105572" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=i-NVTaJ36HxGioJzToEn4TpGI2OGjT5RijLJC5_3RL6sc7XppcGI1TGTiH59NRfmLyPtrQk4R2dEDiWAEwQMS1yJg-EZ839xEMpKofJfP1hM-re9TLZrHEFLfKDhhx-pJ1iRac9TrrO9OsLCvBqA2X-hRQhxnJjoVOVYLeJVRJUUOq5GLhOw_Qo04JVm0dAuC8zT-5y-6AzYxmioiNPs1RN67DmGVKEWhd5vGaigSc74oh7vPbiPfsI1lizrajnEqt95ZOlqfJVJEwOEW4IhWH_CX0MRkh02orBAovqq94FcAtWo0KrZ7QSdhVQAMUHE3-LsKeopvAr3jXJHehh3nZdHT1XRw0vgFQJTVLShfVGF5C4r8S_u8Gvvu1rL_1bjtyyEkDWdCjPoUlCgM6-8ccFxUdM7o3J9VZCscS7y6JZ0Jxynec_u3D6wO5PSu4vM70qJXuliwUDmWd4c1UEaNyGdGyQhRIzMiVIZQ-T0PdSboSninubykkkiRoILrw1KSm3PAeIHNo0vkQRfKK8Q141virnObaFQZIRJwddOI-DYqcJtBbh52Sdqzh5muiarMVbWuSIzeIEK0nmXMTu-P1YVZmPrs0wxY5QnPENhVt6O0OvMK2Xybk8woKKeMTaylwgukjKwoDQF2sBcTbRQdpBHTSMdwb9zikSO13PewxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=i-NVTaJ36HxGioJzToEn4TpGI2OGjT5RijLJC5_3RL6sc7XppcGI1TGTiH59NRfmLyPtrQk4R2dEDiWAEwQMS1yJg-EZ839xEMpKofJfP1hM-re9TLZrHEFLfKDhhx-pJ1iRac9TrrO9OsLCvBqA2X-hRQhxnJjoVOVYLeJVRJUUOq5GLhOw_Qo04JVm0dAuC8zT-5y-6AzYxmioiNPs1RN67DmGVKEWhd5vGaigSc74oh7vPbiPfsI1lizrajnEqt95ZOlqfJVJEwOEW4IhWH_CX0MRkh02orBAovqq94FcAtWo0KrZ7QSdhVQAMUHE3-LsKeopvAr3jXJHehh3nZdHT1XRw0vgFQJTVLShfVGF5C4r8S_u8Gvvu1rL_1bjtyyEkDWdCjPoUlCgM6-8ccFxUdM7o3J9VZCscS7y6JZ0Jxynec_u3D6wO5PSu4vM70qJXuliwUDmWd4c1UEaNyGdGyQhRIzMiVIZQ-T0PdSboSninubykkkiRoILrw1KSm3PAeIHNo0vkQRfKK8Q141virnObaFQZIRJwddOI-DYqcJtBbh52Sdqzh5muiarMVbWuSIzeIEK0nmXMTu-P1YVZmPrs0wxY5QnPENhVt6O0OvMK2Xybk8woKKeMTaylwgukjKwoDQF2sBcTbRQdpBHTSMdwb9zikSO13PewxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
واکنش مورینیو‌‌ و نیمکت‌نشینان رئال‌مادرید به پنالتی که امباپه از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105571" target="_blank">📅 11:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105570">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
✅
🇮🇷
صالح‌حردانی که دیشب یک استوری در حمایت از سهراب بختیاری‌زاده گذاشته بود، استوری خود را حذف کرده! با این حال سرپرست آبی‌ها به حردانی اطمینان داده که تنها با یک عذرخواهی ساده می‌تواند به تمرینات تیمش برگردد که تا این لحظه این اتفاقی از سوی حردانی رخ نداده…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105570" target="_blank">📅 10:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=fwVmovC_Tjug6TI_bTWBEK8FUH-FBiQAT1LnXwJA8_JYO2BAqmh_SGzbddzVN609CJz05SpeCcN2GMmU_FcbxanIz6GWmmkd2D84k-C4AMzPSfBz_ZcAKioCqUXdPnlilkTUBhH-SWb-GO9PVShkBPJpNfAUn4PiNGRA54jJsj7iRd0x3QcrWn7oXQrYT4pdB268aPLrf7wLYqGYviianHJD_qL8CzEGNJ9jFaj9zkalySHHe6vvQJxMtbetVlaKXdfCovRTpNhIDvoNHyyfyavvO4aUcUUK-NK0neU4fzVYeZcG14Jumx-ArBtPu4xK2uavHS-lVIAiikUWsr5fBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=fwVmovC_Tjug6TI_bTWBEK8FUH-FBiQAT1LnXwJA8_JYO2BAqmh_SGzbddzVN609CJz05SpeCcN2GMmU_FcbxanIz6GWmmkd2D84k-C4AMzPSfBz_ZcAKioCqUXdPnlilkTUBhH-SWb-GO9PVShkBPJpNfAUn4PiNGRA54jJsj7iRd0x3QcrWn7oXQrYT4pdB268aPLrf7wLYqGYviianHJD_qL8CzEGNJ9jFaj9zkalySHHe6vvQJxMtbetVlaKXdfCovRTpNhIDvoNHyyfyavvO4aUcUUK-NK0neU4fzVYeZcG14Jumx-ArBtPu4xK2uavHS-lVIAiikUWsr5fBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
اولین شکست فصل رئال در خانه بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105569" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQXZLKOozhID2sbLhADObvbb9RbgrZD2abGubfLPichqQUVvE6jWCKiuTzbIMkEC0EaTxXujMHA5m4NugSEZc8VKFEyF1nwnpLkJNqg0KAnx82Ne_nAUOn5YP-i7daV0InKvbyKlZLO0n-ON7a_H9T4mzrQI3gVtWdSpj2uQOLgnfHGnrNI8nhyKFu564btBDI-kL4YXsXXRf593EntdK_Qqv4ykyg-6QZRzGTMGTQkWL08iSctJKZlokB6A55jYWZ03Na7xKUhvU0PXYckUe_MsiXi1kcYK1z8vihqNcgmiR6ql6-v1_hbfX_HkefRDf0M8B-9nHRMC8vhU5tHYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇫🇷
لوئیز انریکه درباره نتایج ضعیف تیمش: اگر دوست‌داشتید میتونیم روی قهرمان این‌فصل فرانسه شرط‌ ببندیم هرچند که من شرطی که خواهم بست رو لو نمیدم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105568" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105567">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=Qnb289lJilqNXfxTHv0TyiBQyo6PGfdgYSEk7a5MlTtfZRw-EdLgyFtk4YzKfUPZixzhVAujWWURv5PNLknwpRCFgpfdfxo5VO-g99fqeiCrh3axN68wXzOJVjK_NOY6Rg63uenmo8Iwctg6x261aobAMPlXuUi9UFaspPONj-cstE8rRBYCEpRzXS0LP9HnipmbPgzXxQ9no4yb_W_q_bTy3_PsoXXLAp1TkzFg2f30CqV60TGh0pE9YF4KklsBoisiqGTZNIduAFSo0F4P-nIIF_9oVGn9cKpSwmLoskL4cT-YkAZnqXfJx5t3yaULEoc63VaWLG_DyDV4DWDTrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=Qnb289lJilqNXfxTHv0TyiBQyo6PGfdgYSEk7a5MlTtfZRw-EdLgyFtk4YzKfUPZixzhVAujWWURv5PNLknwpRCFgpfdfxo5VO-g99fqeiCrh3axN68wXzOJVjK_NOY6Rg63uenmo8Iwctg6x261aobAMPlXuUi9UFaspPONj-cstE8rRBYCEpRzXS0LP9HnipmbPgzXxQ9no4yb_W_q_bTy3_PsoXXLAp1TkzFg2f30CqV60TGh0pE9YF4KklsBoisiqGTZNIduAFSo0F4P-nIIF_9oVGn9cKpSwmLoskL4cT-YkAZnqXfJx5t3yaULEoc63VaWLG_DyDV4DWDTrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
به‌نظر شما دلیل فحاشی به شجاع خلیل‌زاده در ورزشگاه عادل فردوسی‌پور است یا رفتارهای او در داخل زمین؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105567" target="_blank">📅 10:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105566">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=YuDjCUgHuLxsZhT1w01LMBovI1cTwju9oCCm7CQD2pTsfCMDAdOFEfpV8METdMpCZbyX2gSE2Yf6EJ3Pq_4IbFHenoF_wjh_Pl-N1z2Z2wj5qqlMGISRfqq8SAtcDdrRCaT5GGImr6ZCr7JEeaNchdOw-edO-0YQ2Iix0UzT292JPIPbyM20MWJH3B7Igsh_0nz8HaGfTudy9JYt9MteZ7jZEppmeEcECypDJVOAwYcT-R0loTSdtla8cYgCCqkk9lWDcuttVLl1RjD2GD0uHRj69i5sRZb7Y8ev9uqLM4u9w4r6OKMj4K6K56dZsz-TwJfQ-259ZWFH5tKp_jkGyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=YuDjCUgHuLxsZhT1w01LMBovI1cTwju9oCCm7CQD2pTsfCMDAdOFEfpV8METdMpCZbyX2gSE2Yf6EJ3Pq_4IbFHenoF_wjh_Pl-N1z2Z2wj5qqlMGISRfqq8SAtcDdrRCaT5GGImr6ZCr7JEeaNchdOw-edO-0YQ2Iix0UzT292JPIPbyM20MWJH3B7Igsh_0nz8HaGfTudy9JYt9MteZ7jZEppmeEcECypDJVOAwYcT-R0loTSdtla8cYgCCqkk9lWDcuttVLl1RjD2GD0uHRj69i5sRZb7Y8ev9uqLM4u9w4r6OKMj4K6K56dZsz-TwJfQ-259ZWFH5tKp_jkGyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‌مخ زنی به سبک مهران مدیری در سریال جدید مرد سه‌هزار چهره: فقط اونجاش که میگه برای من منگنه بشید
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105566" target="_blank">📅 09:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105565">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=IPpEwc7CCrd2RYbQojSBS6ytp7THjpVfB63ZKu10LHCCL38L5s_zX0lrlmsSojJ_njTjsgg0YprBTqGfOJR6MWeXPGwF05DYdB9g28NbpfIg7cccZ3uIJmpcGqwjnTjwepQHljFAzWI_FzaPtajwAWNIMPfXoHofIotfm1FdnOJZgF-VIfnOUyUIaEcldfSyyfN_5H-_cCWaGepEZ1GAk2UUjos7ZFl3We0mxVhQXnBWKS1YR-bXsa9SJfQ1wKycAO31C3aTCUqLi4eClSjnDbF1N1oci3MlUMkh6nsUQE4vwGLqo1a6jBMfhq5B0iRVYMdYmuQHiHmoplo14tXuaAzo4H-mPMaIV39H2w74c4t-MBliv2MM8kQSX6oQrHptHGPErKmsbMQGeLAe_ZHghuDcBvryxmRcCfa3NXZGCgseHWBHNkLCqYlz_DC3bvhdcube9OFd2FSDwFm-vI2rl1eYCs3aBfDJshRC4jpDAbN1x7YGK4U7c_SU6DYyalt4T0B9rwJUwZ1TrMC0ROS8siJpq9EzVTXOnRWgugb4ufrk7gEPZUv804s7NDOESgsvSwVlav9HMRMVDotOeXT6QwJyW6XPiYHRq0iIU2ZZjPtP38x73C0L2KLOpRe3uzw9gh8AFSgRsx7-3V-aZr8XqfbRgmLY8u268Q_i0uw6Zdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=IPpEwc7CCrd2RYbQojSBS6ytp7THjpVfB63ZKu10LHCCL38L5s_zX0lrlmsSojJ_njTjsgg0YprBTqGfOJR6MWeXPGwF05DYdB9g28NbpfIg7cccZ3uIJmpcGqwjnTjwepQHljFAzWI_FzaPtajwAWNIMPfXoHofIotfm1FdnOJZgF-VIfnOUyUIaEcldfSyyfN_5H-_cCWaGepEZ1GAk2UUjos7ZFl3We0mxVhQXnBWKS1YR-bXsa9SJfQ1wKycAO31C3aTCUqLi4eClSjnDbF1N1oci3MlUMkh6nsUQE4vwGLqo1a6jBMfhq5B0iRVYMdYmuQHiHmoplo14tXuaAzo4H-mPMaIV39H2w74c4t-MBliv2MM8kQSX6oQrHptHGPErKmsbMQGeLAe_ZHghuDcBvryxmRcCfa3NXZGCgseHWBHNkLCqYlz_DC3bvhdcube9OFd2FSDwFm-vI2rl1eYCs3aBfDJshRC4jpDAbN1x7YGK4U7c_SU6DYyalt4T0B9rwJUwZ1TrMC0ROS8siJpq9EzVTXOnRWgugb4ufrk7gEPZUv804s7NDOESgsvSwVlav9HMRMVDotOeXT6QwJyW6XPiYHRq0iIU2ZZjPtP38x73C0L2KLOpRe3uzw9gh8AFSgRsx7-3V-aZr8XqfbRgmLY8u268Q_i0uw6Zdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
باشگاه نوریچ سیتی هر سال نشست خبری ویژه‌ای با عنوان "نشست خبری با قناری‌های نوجوان" برای هوادارای نوجوانش برگزار می‌کنه تا بتونن مستقیماً سؤالاتشون رو از سرمربی تیم بپرسن. امسال هم این برنامه برگزار شد و البته با یه اتفاق ویژه همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105565" target="_blank">📅 09:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105564">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=b-Sh3yLyvsjllfu1jnBrzJ0sj8NSpbQ7hvIqlFlVinmMj5ekQdIU26wdaiNM_8W-K7w3B0yz5lwOh1LWi861HmADUx9t9btSvN59gEzt3f-8s3YaftmvHCnauM4PS3dWUNPIM-nnQj0EfWHYCy0gVWH-yHAEXOM5X_YfwlCqlq0c3N14e64GDlijGIaqfKtiHusZHFW1E_CaY5OXAm1CckiW5VuMz09RDlOTq0xpLDs6dogaP_bLTxvW_DK9TsS2Psk2GIFDYRy_Aa0G1ljUxtSWDaMjD9SGbnE3Z9uUdQUWnN5lT_evKeTwdscyewuXziK7G-oSS_se8bAnM5FVHkrwj3TavomxRVkr5j_gOd_roCz7mA994-oLAxNpdYMetHLTQErDE46m3-hNoR2eTiTxrw2BZg4E3IKBI2GtLXY9ySV90wG5d-3ExlRWVtMIvYjah2-TZqX0eOm-Fq3NUN95fNcgp7O_iGxb2K3e_U7Ro2y9LHS8G_1ejg45In8O8DhLq3zg-uqg8TbZ15je5vVox8aIsgP03ZPeePFRrhGQSF4ynJGxNJWYoNpEMoX_92hg3yGl7aCPASwdpbHO1uuD3tT_g-TolldcthE7DpYIm8TnM4AwZQcJeTAorwnUqvYANWVALYUBmVI25XZbZxYVQkmZ0K2llrLmN5Pof7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=b-Sh3yLyvsjllfu1jnBrzJ0sj8NSpbQ7hvIqlFlVinmMj5ekQdIU26wdaiNM_8W-K7w3B0yz5lwOh1LWi861HmADUx9t9btSvN59gEzt3f-8s3YaftmvHCnauM4PS3dWUNPIM-nnQj0EfWHYCy0gVWH-yHAEXOM5X_YfwlCqlq0c3N14e64GDlijGIaqfKtiHusZHFW1E_CaY5OXAm1CckiW5VuMz09RDlOTq0xpLDs6dogaP_bLTxvW_DK9TsS2Psk2GIFDYRy_Aa0G1ljUxtSWDaMjD9SGbnE3Z9uUdQUWnN5lT_evKeTwdscyewuXziK7G-oSS_se8bAnM5FVHkrwj3TavomxRVkr5j_gOd_roCz7mA994-oLAxNpdYMetHLTQErDE46m3-hNoR2eTiTxrw2BZg4E3IKBI2GtLXY9ySV90wG5d-3ExlRWVtMIvYjah2-TZqX0eOm-Fq3NUN95fNcgp7O_iGxb2K3e_U7Ro2y9LHS8G_1ejg45In8O8DhLq3zg-uqg8TbZ15je5vVox8aIsgP03ZPeePFRrhGQSF4ynJGxNJWYoNpEMoX_92hg3yGl7aCPASwdpbHO1uuD3tT_g-TolldcthE7DpYIm8TnM4AwZQcJeTAorwnUqvYANWVALYUBmVI25XZbZxYVQkmZ0K2llrLmN5Pof7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: مردم فکر می‌کردند این آخرین جام‌جهانی ما باشد. میخواهیم در جام‌جهانی بعدی هم باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105564" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105563">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=HyPkFoOLkS1Xco2EJ7HAJ21JLaxmnXi2_UAEOqN3zLtQeu-Oz3W7uh5dsfGdTzfDMPot4Ar3vDZ2jlTlYC-MnaUvlOuGiI8rVUcw6QPAA_MC36pP8ugY1c6J4qxogY-XCkxSq2isk90kN2dPHq2f2K3TBGsuO6ubdZLpNCEmvu7Ksbryrb_KYlCzFgGPnxnlAxWshhOW3shGLlFl-nnCB509eh62vSD1KSOLo3tpEgmHXHEWYageMLC_Y8ShgtOcVpDNVW0xt7cYZ3zvFgEcudsbPEw09sfSkVGpQeGAZ9Fq9IFNMfoY65H24Wgbfu_IkRgRH0Vc-c8RyBMBsJiRdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=HyPkFoOLkS1Xco2EJ7HAJ21JLaxmnXi2_UAEOqN3zLtQeu-Oz3W7uh5dsfGdTzfDMPot4Ar3vDZ2jlTlYC-MnaUvlOuGiI8rVUcw6QPAA_MC36pP8ugY1c6J4qxogY-XCkxSq2isk90kN2dPHq2f2K3TBGsuO6ubdZLpNCEmvu7Ksbryrb_KYlCzFgGPnxnlAxWshhOW3shGLlFl-nnCB509eh62vSD1KSOLo3tpEgmHXHEWYageMLC_Y8ShgtOcVpDNVW0xt7cYZ3zvFgEcudsbPEw09sfSkVGpQeGAZ9Fq9IFNMfoY65H24Wgbfu_IkRgRH0Vc-c8RyBMBsJiRdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🔥
جورجینا همسر CR7 با لباسی از برند گوچی در هشتاد و سومین دوره جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105563" target="_blank">📅 08:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105562" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbQ1TIsCRNUwMRFZmTriSIsl6PKelSrQ6vmPk1N1hINrkB99Tr6H_E7CDEXgedW7JwE4vpMLoMtpZvCYC5yXes5u1iN9XFxRCk7ymWyHrSloP0KJssh78c_k333BT4Bay6-xsmd3_p4yC4Akw8Ze7t7hAzxQXYGK4q6TjvdsOVxCOVD6nPYlSbEgqmglTWiESduFYBp4TZFfyG_dYVMCEM_8wpE-cC3j3__M3xpAlnBVn7MhG4Z9KkQXDDYuC7mT60bS9fwcJiiZtBi8mA6qgf1oo1CT0gCKGK4HUbsvZFZKWxQqlOVVh2dwyCfZ_27rnkE12dFgs0KS9vTIpORyMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105561" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105560" target="_blank">📅 01:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105559">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=MHONacyN4a-t60yS5mjODdiWjjMijKzX7NQgcLCOJ3YFOjz8KaS5za1xCeDUPIWGNzrXNndt1S0i804ShmzYXEPGuZ2LM7Lqu3pXqH2Q1u_IxRCkkjQEpuoR45z0PHTuyokzRYNwoQwEltWeISwelSroNx6ochv4Qmq3RdKj6q20hVuYs8-WDY7oO-2Aey8AWOyoYv7gq7Zs5ft_9pruLQlI0ExpoD5alXJ-ftiM6vSqjgKy-rkmLcQHINmUuAfNy4BgDO0kn82fDNl1PV2wV_-y-qwt4fxalB8Y-IoCUbX6NE-xp_Yat_Gs56uy66slzzy_0rlZyfAHqRTpH2VR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=MHONacyN4a-t60yS5mjODdiWjjMijKzX7NQgcLCOJ3YFOjz8KaS5za1xCeDUPIWGNzrXNndt1S0i804ShmzYXEPGuZ2LM7Lqu3pXqH2Q1u_IxRCkkjQEpuoR45z0PHTuyokzRYNwoQwEltWeISwelSroNx6ochv4Qmq3RdKj6q20hVuYs8-WDY7oO-2Aey8AWOyoYv7gq7Zs5ft_9pruLQlI0ExpoD5alXJ-ftiM6vSqjgKy-rkmLcQHINmUuAfNy4BgDO0kn82fDNl1PV2wV_-y-qwt4fxalB8Y-IoCUbX6NE-xp_Yat_Gs56uy66slzzy_0rlZyfAHqRTpH2VR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رفتار سرد مورینیو و وینیسیوس بعد بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105559" target="_blank">📅 01:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105558">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY-onRsEZjJYLZMVbY9ElxNqzfz12Rbni29r18Jcr9Z6gCMIryHGSowzT3aCvqDhgALSWQeiM_2Ah7ohRTLpTFtdpE7dAD5TuytCqwpQ6Sp-_04kydMeihwKmpyxyrn3-b5JbyIqAWfw67uNo3Hb7Kk8PmMpn857DUpbBs8LIENd7sfQMA6vwMJY-BMM-L7DXEli2dtM0vOlQ8k7uOxRlsmox6e1PgTSLdDlWjPqu48xPzkUe6TzF_u5iP3DKkXnZ8pqHS2KvMYZ_ez_VkmbtAjBzbr2ZgICbk_FkDU9HwaR2uymdXlhM9TQv7cVMOBfCgkEVOhzAwLYBey5H2GUhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
#فکت
؛ در آخرین‌فصلی که رئال‌مادرید مورینیو مقابل بتیس در خارج از خانه باخت، آخر فصل بارسلونا با کسب ۱۰۰ امتیاز قهرمان لالیگا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105558" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105557">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPXak7p80vNpj_fWZZltiaZxm-EmQQdZRMHnJ1SoPYmLZfp4TwhGUoCeo6AeAkNBfl-NfeZGdPHWHj1iBvafIRjih4h1fps9x1f5PyCQE2R-hMZGRRVupohpV9D4NufbfbgWEymdLZzFnV7PRe7cGOgkOC966i6tZ9qjxT2cUxXKR-VF5PRSNV3_MzLrtdCQTg4wDxXkJJd2Z6_35Q6JqBX14SuelrXLWSPIzRTureUXfzUUp6MHWOERktau0ZbGJKVyNd7g-cnedw030tHGg2903k485mxqAVOR5RFgGEMi-OK0hkor6wwCnaFmt99mBwoaAoYQvQJP_yq6zndgoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105557" target="_blank">📅 01:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105556">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv3tIYixe35QemoiI0VrVmDWZCvFsFSuEJ7beeFamNCqg6oz-Bqv302QPzPg8C3iNCFFBTIlJkwnC4VzlfDpWBwVvaAth3AAwZrQPmdRm1GzdrtVZHBoXwQ2inqnTBhyjBJSZGh02tS4Cigs5rKuwCi-594IgiTcCfIn48QBUoYSt6GKuAO-shBRnSkobF7KNmxi51U8RIoKtkBiwHZB6qU6Hp0CCKw4YTOKIJH9dShqXvpUkJoGOyGTQ1mE-4uUPjPyU4TGMI65rrv8TlHAAHK6PxWso1rCGQPzQtFqlh5i1D3idgTKCaSzuYHEhNfFB9r9vk6IRMztLbDOxvYFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وسط ریدمان رئال‌مادرید گویا باید از اونور یه فکری به حال پاری‌سن‌ژرمن فلک زده بشه. سه تا بازی کردن دوتاشو مساوی گرفتن امشبم باختن! گویا اثرات جذب فران تورس داره خودش نشون میده
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105556" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105555">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9tvMt0y9AyHoI96QIQ5sUrX-QGzGIlUNlD-nCSz8zqYbaXxv9rbIKkr-jRgv1TMifs-cJ5WCqej0YQSGYFWeiyQ69n_K7HQNNrBUiaUgg9-fxB7RdO-4sk2ZzLN8nxo2Pq6TfFb1p6C92CAeAAXxZuSmPVl8QCqF7sw2AiklY9olFgw6slTqoVkWKAo348bVAYHg4EK4dTiR1XPy8IZvubuZP-_lmXLSK4UZ9OOnf5ysK2QEakUa820vaV3ONjhZpwCTOu_iXJV3nRJgeOJIooQkUwDsVzCZF8jVMDBxiU0tZvtPxB98myLFekHitE7hv33ZjQmqKCq3fJdR03FCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105555" target="_blank">📅 01:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105554">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🧕
البته گویا این صحنه هم آفساید شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105554" target="_blank">📅 00:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105553">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAN5hmugoEi6FI7VT8V_7yDViYO1xeUhAdK88vDpyc-87MOUwtM789x5xvuDszZe6npf3WttMdXv6S0nonG-uf5URZVrTyMQhyyUrqWM0bdQlOKvurAtMIumggduu30bn0Gp9oDTnB9X0Z4x9j3BcEPYe0HMB1JklZv3GYQu7xdrnPp4F9teOaE2XqGDFboRFeRFkYk9smoE7mdOaJZUeXVdCwVCkRMJv8S8-dUYOjJlbDoPy-YdL2a_Dbm0oHAFvVzxuHpxhlNm71nDR_qod0GVjjJdsn2JFEnYqJRGokRybzk2d8btvNB6bzFENZzhaGUR2t5fb3efqGjniS8JYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🇪🇸
رئال مادرید در پنج فصل متوالی در لیگ، نتوانسته مقابل بتیس به پیروزی برسد [سه تساوی و دو باخت].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105553" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105552">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPCK6AD4kXJxQPyLELQY4SGXd8dbcpcTyzxkpgHuzP2JKJst3aAYFWdhqH0xcY3uA_JkiLA4uTR9PFv1iwHHhC1qzwhhYZt2Ao4avkB6kG4xKx4aIxVfyAzxthU7Xhmfsdxch_KjLaHRI583X02j1yyKHJE0EddCUKo9iAnz_u67pc2lVZGQUHkq4U1dMRq1EF_FPQgn8_fa8-lJVQPdps7XX6dABLGNcz71ciNT9u7tHWImVIm8SdAQfQVgQJRgDG1NG15eu00YmlCGPQs6ritEK68B339V0Esjs0GxHZl42WPnk9PaPBOLxCQ-WATOzQx6KIuH26wxNq12DX6Bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105552" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105551">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyl0qL3MVwKFHsmcwJIO2-vTebsVLtDGCEWo9aAiP6GfUg6tVVuwGvugWGGSA_Jx_lIipypSlMOpOsfkhNDVqebX4wC_IBBP2uhsCFvrXUh7CI9eQCNF6aNP5ByG1e1QDMMaW3Wl0NZHBpqKOxWyoONTImznFsC2Dhd5i8SV_vKx9agDOu1rd8lHjffpjT0PUTPi4IwL4mq7VqlrAAfOA-m04YqB77Sg_G57UnBRANTOOEoEzObcXR7M1rLEQFlBqYN51mqPoCA_n8_ecO_Faep53eqYSZggsNGPI36O9sXGQRQWPIA2aE9Ewu_Nuhj5ANvzC0UyVRyFUB7iriHlIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105551" target="_blank">📅 00:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105550" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105549">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE6jfLixIJt-yaneNJOWSXNSiZgDjKiOTCkrN80xcavxW7RjBjdRR8wEVz7YWLatU9DC-nldIFcbMx7ovJzENK153dzNq9ihWgjPsdOFkZC5yJwNshgGnbDwPVXvbegT46DJljEjmWga1vJ_-_fV0IkkRPEmTQxzDDLiaEKoHLP1eN-EEVOCh5s09gVTSa0v3OPkzmkN-EjDuvzmjHC5li5B7FNPjzFP-tNZsdaQCN_Z_m9Llf8hvAy0bUf2FjIGls1spB4DBChlgm8gvEhFWeRpJq7VK9fHUpy8e0s3qpxgi0MxLuR44lyJYwYG2K1gp671RMVUGzwkmKLcskTc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105549" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105548">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رئال‌مادرید بدشانسسسسسسس
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105548" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105547">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وای خداااااااا چه شبی شده
😂
😂
😂
😭
🔥</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105547" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105546">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
امباپه ریددددددددد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105546" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105545">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بدلیل خطا روی وینیسیوس
😐
😐
😐
😳
😳
😳</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105545" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105544">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برای رئال
😐
😐
😐
😐
😂
😂
😐
😂
😐
😂
😐
😂
😐</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105544" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105543">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پنالتییییییی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105543" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105542">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGJszKmcoabhUHV0XnegQdiD16IMIIUjQ-R_KbchnlwOk1FDulQkp1PEUqOup4jWy2nifD-o-BfYJUp-U-U0uOwl-DOzUR6m4YlrKHDflZZFcX0nEbDfk-OoL73HKYyXbtm4Eo989RoZF9rlRSCWr5Z2QWsgh22gf_d1O7WGgzYkMTq7dvIVC7XSPC_xKfnpDlK4lkjPZdKupkuUEat0cCxI6lbzZbPxNTVOyElxAlhXp7O1WXanv5jIGIXRsPhjWz0XdTnX6YlvWjHg4_x39bXAf9V89tmgFjei6_6wOT6-hlo7ZYelrzPMBnC-tGeCDDy7Wz5RgF5boCV76CGrvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آفساید ببینید و برینید
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105542" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105541">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105541" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
