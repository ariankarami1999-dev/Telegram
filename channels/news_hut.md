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
<img src="https://cdn4.telesco.pe/file/HgkoQVlOyRrj3YgIiyBX1ZAUiF7bDbh8fW_S10At4-li5FNmrdSrgjlxr9heuiCmt-RiJmfAEuC_mJRkXfnL4sIDto9Gpak3xlBY9TSSDwv2vFO9dAKabIqBNsQAr3j7kp5jv_bsWQ3celvuTdUIWti89KTIj4G7HyCTPh21Jx4OP-TLyVWgqoZbfDTXuKUFDVJNCzT_GbA4m9eWSeL7WAxsMoFNw9sEcdYgTwgoZd6UETxmPp2uvIQxBJy5pbw8NjFUJudH_jiwBOdDhfEeHBWMPSWxlkoRHmXWLhrBTPncWLb-TF5dJXjKw2JTDA051HhJJh8RNNGz0eKidst52g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 172K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 07:57:58</div>
<hr>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=NCqFi2yV9S7g9eYE4-57nJRNXGhifJMhwWcXxiZSNDLOevu9Z9p-Nf2d6_oeYu1nsEpiARa9lc-oPU9iue6iAydbdVUJqMuPpt824wE_TPzmPGh4KATQVczxBXR6cpl8T5yLQyPW4uwcVHaKp2YmP3190BtjHKPIEwP7hsfr6aFl8yfGMe5P3cgqkN53ODTLKoFZYT_4LoW74kxtHrlM1edETmBKZLp1bKK6mKreeaIJAImvLCQpFw2JlCfiV517207qFrQvsjToB7JZWmhu00DzhZkaeBxRWMLmeszSSv8YD6l-ttKPCIWCTT9wLiC6LO-1vwM_8CiMAPdF2ZqLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=NCqFi2yV9S7g9eYE4-57nJRNXGhifJMhwWcXxiZSNDLOevu9Z9p-Nf2d6_oeYu1nsEpiARa9lc-oPU9iue6iAydbdVUJqMuPpt824wE_TPzmPGh4KATQVczxBXR6cpl8T5yLQyPW4uwcVHaKp2YmP3190BtjHKPIEwP7hsfr6aFl8yfGMe5P3cgqkN53ODTLKoFZYT_4LoW74kxtHrlM1edETmBKZLp1bKK6mKreeaIJAImvLCQpFw2JlCfiV517207qFrQvsjToB7JZWmhu00DzhZkaeBxRWMLmeszSSv8YD6l-ttKPCIWCTT9wLiC6LO-1vwM_8CiMAPdF2ZqLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=tVSK62kVAl3JAxAYtsgkZJOUQNGEs714xKnngdJD04yuyM_bZ2dR7BK-rlc-Gv2XAjQv9Mw4Fn_jB6Pz5-Y602PAV_5AKCZgYfCbrmRp5H7I_9JN2T0G3l_Nb57nud0mscfDqXeuTGF2h7a-Us4nG-h6kVNb0b4eIfJaKqi57-ROB2nfzgR7Wr3PGpbAKEJ4zRP5COmzy4mWMtNkPQZn55FQrdSwt7xT12fiGO-JLMwmNfw5lDD06iwrqHtEYw8OjBy14-ir8ABwvYm6dvgEavWHFloVBHFppY3bTlcLDJ9LZXAihmKnf5QXXHHIOZ526HiTGW1RF1B4tN83NSP66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=tVSK62kVAl3JAxAYtsgkZJOUQNGEs714xKnngdJD04yuyM_bZ2dR7BK-rlc-Gv2XAjQv9Mw4Fn_jB6Pz5-Y602PAV_5AKCZgYfCbrmRp5H7I_9JN2T0G3l_Nb57nud0mscfDqXeuTGF2h7a-Us4nG-h6kVNb0b4eIfJaKqi57-ROB2nfzgR7Wr3PGpbAKEJ4zRP5COmzy4mWMtNkPQZn55FQrdSwt7xT12fiGO-JLMwmNfw5lDD06iwrqHtEYw8OjBy14-ir8ABwvYm6dvgEavWHFloVBHFppY3bTlcLDJ9LZXAihmKnf5QXXHHIOZ526HiTGW1RF1B4tN83NSP66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=U9fWYpOhdKEoV8LLAB_jrDJZFjW-PUYLbqKTEqTzfMKaJ-uAX2Q5Y7TGle6s_8EXv_oeLiWDGj-58oMPUYyJzdJbNeInOidU8zi5dqVyzTWzmbipqUKzuJC0pFq1J_Og7gVpduBn501ISnNQBi2ud3jZk6GMekOQsUMlDFyEMpiIFrxFz9pk1CRQJ938UybWXtfIBpGM0ePLIicfE5wODL6CYhHs38oTUEWqfs6VTn4ZUDFEScS6YPopWppy-sxKUSd6Ka5b8Rt0ED6uyqZqYH5c6a5PXEuycvxOz_-sTmdps4pImBZwXnSSXNBZzEwZGaYPbcmmOaj3rJHhGAv4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=U9fWYpOhdKEoV8LLAB_jrDJZFjW-PUYLbqKTEqTzfMKaJ-uAX2Q5Y7TGle6s_8EXv_oeLiWDGj-58oMPUYyJzdJbNeInOidU8zi5dqVyzTWzmbipqUKzuJC0pFq1J_Og7gVpduBn501ISnNQBi2ud3jZk6GMekOQsUMlDFyEMpiIFrxFz9pk1CRQJ938UybWXtfIBpGM0ePLIicfE5wODL6CYhHs38oTUEWqfs6VTn4ZUDFEScS6YPopWppy-sxKUSd6Ka5b8Rt0ED6uyqZqYH5c6a5PXEuycvxOz_-sTmdps4pImBZwXnSSXNBZzEwZGaYPbcmmOaj3rJHhGAv4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=aaRGCekMwjqezy6n04xyoXdU-5uBH4lhVh7-tory4dI-UNkGoKRv4hQCdIfI5NhcvqqqqfBgdD-dvSVyjZuOsXUL8YiNXcMrUWC5RVbFCmHq6fYztfw8FDpEHVaRfQBXE-fcyuxXoaELc-t0iPrWAAGyGn8DIQiPGywvmWTqZ1wLWDAS2xO1q5VFUEAqdsG5pEdTS0F173UT5DU-wDe3GMJ9MmvugNI95o0erCXsu6Sg9gikVCAUQ7UzpWzkRcZPMMEFdX5lTy8AIs34BKHHaDz9iXKJDIqhjt_azCuvGK12HCT7RMX1rKq2fdCHgC5NBDhtRp1JIb4KAIDRj5xIMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=aaRGCekMwjqezy6n04xyoXdU-5uBH4lhVh7-tory4dI-UNkGoKRv4hQCdIfI5NhcvqqqqfBgdD-dvSVyjZuOsXUL8YiNXcMrUWC5RVbFCmHq6fYztfw8FDpEHVaRfQBXE-fcyuxXoaELc-t0iPrWAAGyGn8DIQiPGywvmWTqZ1wLWDAS2xO1q5VFUEAqdsG5pEdTS0F173UT5DU-wDe3GMJ9MmvugNI95o0erCXsu6Sg9gikVCAUQ7UzpWzkRcZPMMEFdX5lTy8AIs34BKHHaDz9iXKJDIqhjt_azCuvGK12HCT7RMX1rKq2fdCHgC5NBDhtRp1JIb4KAIDRj5xIMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای دیگر از شلیک موشک‌های سپاه به سمت پایگاه های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=OZB5EphMn_S7aVJbMh0m0SYRN2E53VahSTs8s1zoKGIEQqzPhdR4JMrY74u0J1uZrBmfgRb8J3PnRWUkJEw5U9_461XOjEGdIWD6mvhS00k3tIZGPdSF52J4sp8yYYIHH79zGkYRbuXQMtDhMr9Iu2hFF5urhhhMt4-znZn848yS4NUOh6BgHpfnPtkcGmg31v6Z8-TEZTq1dt9zrB1VMdEuCFxQh9JTJnjs0bnRoQZihfE1PnIlAEci88HJa_XScSKYDr4LAcVm-YXGGutlLu7srZLlG1tRg3VKxEsRTXqDi6-fcJIDdEvL72w_vniHNEqZhnrZa9mTBtH_f6pTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=OZB5EphMn_S7aVJbMh0m0SYRN2E53VahSTs8s1zoKGIEQqzPhdR4JMrY74u0J1uZrBmfgRb8J3PnRWUkJEw5U9_461XOjEGdIWD6mvhS00k3tIZGPdSF52J4sp8yYYIHH79zGkYRbuXQMtDhMr9Iu2hFF5urhhhMt4-znZn848yS4NUOh6BgHpfnPtkcGmg31v6Z8-TEZTq1dt9zrB1VMdEuCFxQh9JTJnjs0bnRoQZihfE1PnIlAEci88HJa_XScSKYDr4LAcVm-YXGGutlLu7srZLlG1tRg3VKxEsRTXqDi6-fcJIDdEvL72w_vniHNEqZhnrZa9mTBtH_f6pTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68137">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=l9KYibH_UoxOV9jbR8_FceQ3-03X5GvZD0SOOnM0s753dH4EXC0ItSJddMb1TRMRrH8tpywu-wEgZ6Uxx_GMXlLx_q4T99MHmOssO1CDuar520mtNeYlejjIMNaPZFZ4jvGLltBOm10C7IFcUiQwXx2ypVZNVQraOHfAtrvU108TEZsnSWufGPWmH0s6e-iUrLrvr_gVBPdCv0yK6wyJTlbTfaRpJGBvfKM8fa3rMUz0NFlYVbnH2Fh6YJw2VJ1lZEmJ7tnWeJaoLe6AFG1mRXC4y-0d3KCyFsib2BA-Vv0Ao9buKlLrLaFZx2zux9r_-LFYWiomy4VWDgrtdHSZNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=l9KYibH_UoxOV9jbR8_FceQ3-03X5GvZD0SOOnM0s753dH4EXC0ItSJddMb1TRMRrH8tpywu-wEgZ6Uxx_GMXlLx_q4T99MHmOssO1CDuar520mtNeYlejjIMNaPZFZ4jvGLltBOm10C7IFcUiQwXx2ypVZNVQraOHfAtrvU108TEZsnSWufGPWmH0s6e-iUrLrvr_gVBPdCv0yK6wyJTlbTfaRpJGBvfKM8fa3rMUz0NFlYVbnH2Fh6YJw2VJ1lZEmJ7tnWeJaoLe6AFG1mRXC4y-0d3KCyFsib2BA-Vv0Ao9buKlLrLaFZx2zux9r_-LFYWiomy4VWDgrtdHSZNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا همچنان قصد دارید جزیره خارگ را تصرف کنید؟
⏺
ترامپ:
خب، نمی‌توانم چنین چیزی به شما بگویم، چون اگر بگویم حماقت است. اما کار جالبی می‌شد و کمی هم خبرساز می‌شد.
⏺
مجری:
آیا احتمال عملیات زمینی را رد می‌کنید؟
⏺
ترامپ:
می‌گویم نه؛ البته اگر شرایط اقتضا کند [رد نمی‌کنم]. گاهی اوقات به عملیات زمینی نیاز است، اما ما افراد دیگری را داریم که عملیات زمینی را برایمان انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/68137" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68136">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=RFoFrEsuiwi-m7Ti_dxPbVvpxI4rH2WlVIY6qgv96PvT0t5mJgApjz76bjc0PFbAmMO6JdOe_o78GJ48NoCmQAHfPiNjjvXW5iNWdcp8ogQvzI5pvsxVf1G_lb-_HLXXe_qiHYQoX7I_vowwy7s6WUDF4izDikBWvTY8dWOec1Us_NYlCKnWuRsrJKip3dvxaSoWfUoIWStGw8s7NPRcYSRLi6SM_S0TUIEr-pxW-3-g4k0Y9acWB_ZH51X9XiJH09yZR71uqVAQnMpTwSAtZGPYYfywuYBkUhfCuGy1Wmq4vjxLeGVg5d4JyyHgJ_ZMBQmKcbgoRcSP-wt-xaXRtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=RFoFrEsuiwi-m7Ti_dxPbVvpxI4rH2WlVIY6qgv96PvT0t5mJgApjz76bjc0PFbAmMO6JdOe_o78GJ48NoCmQAHfPiNjjvXW5iNWdcp8ogQvzI5pvsxVf1G_lb-_HLXXe_qiHYQoX7I_vowwy7s6WUDF4izDikBWvTY8dWOec1Us_NYlCKnWuRsrJKip3dvxaSoWfUoIWStGw8s7NPRcYSRLi6SM_S0TUIEr-pxW-3-g4k0Y9acWB_ZH51X9XiJH09yZR71uqVAQnMpTwSAtZGPYYfywuYBkUhfCuGy1Wmq4vjxLeGVg5d4JyyHgJ_ZMBQmKcbgoRcSP-wt-xaXRtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم. ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/68136" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68135">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=BqB_iTGIMSHXTLIx108o-o8lN859KkIGJtKsdL92VW0GK1hjUE6MFakgzr6JkI5YoX3LJklAk25OhgkmTZYtfaXq0ZuLLdeeD98HpJ54a3XAFxQMzvfyApVdgYk-HXd_93_Bp_6cApLwfIMqfWQDzbBJImoG9iKOniLAE3DGy-8T_j2uJzncpjnzQkbkusvrHzX2H_8jzMgZQPYx08fnShDHCjXJD_1AKX4RgQrhzcxyums7WYTE2drxUK_QXME7x226TgowZGPAkFb7St5F_Ajl1Va77Pp76wJ8CmnsToPh-l-tuTOxDjAhHgND2latb8jqc3hqPjdPD0mG1l7_Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=BqB_iTGIMSHXTLIx108o-o8lN859KkIGJtKsdL92VW0GK1hjUE6MFakgzr6JkI5YoX3LJklAk25OhgkmTZYtfaXq0ZuLLdeeD98HpJ54a3XAFxQMzvfyApVdgYk-HXd_93_Bp_6cApLwfIMqfWQDzbBJImoG9iKOniLAE3DGy-8T_j2uJzncpjnzQkbkusvrHzX2H_8jzMgZQPYx08fnShDHCjXJD_1AKX4RgQrhzcxyums7WYTE2drxUK_QXME7x226TgowZGPAkFb7St5F_Ajl1Va77Pp76wJ8CmnsToPh-l-tuTOxDjAhHgND2latb8jqc3hqPjdPD0mG1l7_Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
«۱۰ فروند کشتی روز دوشنبه از تنگهٔ هرمز عبور کردند — کمتر از ۱۰ درصد چیزی که معمولاً از این آبراههٔ حیاتی عبور می‌کند. وقتی می‌گویید «تنگه باز است»، منظورتان چیست؟»
⏺
ترامپ:
«اگر مردم بخواهند از آن عبور کنند، باز است. ما آن را برای ایران باز نمی‌کنیم… الان باز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68135" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68134">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
مجری فاکس : آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68134" target="_blank">📅 01:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68133">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=sM5KE5Xo0OH0-_7tYrzAe5j7BhNBFqMQsOoY7JrhDteCNyjCAx1U29N_CA6ao4vaRoNM1MCZtOpN_4geGe1WrEz7Zt6-3HfvMisXv-au87d6XfeutOVjCQqZqzBsuiQJtF17PralL1Ene4uyCykv359e94Og6b3tv8iaVp14Nj880ZLDkoaHflg88rTsUl2EvqyiJsPodv1GRZt_kSgslVxEyyv3ncM2mCpSCIA8uZo-u_G1RbZTQUPNP40ERUR7aqQTVMWVoTI-2ZpHpxEZZ8MDsBycIRLlLlCeI7ujPG-QPPSgY197jZ08mTHPTRoBp4F-kJMSLKbqYVgCkMFeqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=sM5KE5Xo0OH0-_7tYrzAe5j7BhNBFqMQsOoY7JrhDteCNyjCAx1U29N_CA6ao4vaRoNM1MCZtOpN_4geGe1WrEz7Zt6-3HfvMisXv-au87d6XfeutOVjCQqZqzBsuiQJtF17PralL1Ene4uyCykv359e94Og6b3tv8iaVp14Nj880ZLDkoaHflg88rTsUl2EvqyiJsPodv1GRZt_kSgslVxEyyv3ncM2mCpSCIA8uZo-u_G1RbZTQUPNP40ERUR7aqQTVMWVoTI-2ZpHpxEZZ8MDsBycIRLlLlCeI7ujPG-QPPSgY197jZ08mTHPTRoBp4F-kJMSLKbqYVgCkMFeqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا اطلاعات خاصی وجود داشت که باعث شد تصمیم به آغاز این عملیات بگیرید؟
⏺
ترامپ:
ما می‌دانستیم که آن‌ها خواهان سلاح هسته‌ای هستند.
⏺
خبرنگار:
آن‌ها می‌گفتند که خواهان سلاح هسته‌ای نیستند.
🔴
ترامپ:
هر چه می‌گویند دروغ است. آن‌ها دروغ می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/68133" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68132">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=RVW3LqkhZZuoJQ5_ECWwweu3aa4l3BGXiRQrGbu3saAWUXYdndhr9hW0lsGFPigaL2-5g5KUoxHtmlyVtHKOYNmSqiaaX9MR3HZibO0F4j1FXMwhHxTg6m6SNMUtXRHntXnmaRKTJwmsAtlimwPZYPQB_Ihr7gKNT_WLFlsV8JaIcOs_sVwoKti7ElZgirCzA3QBotO0J6d5rLgQHv_TKER5XLw--_W1i4s3_w4fspLggQ2FNhIbxCZWhGQ-tVzAIvpTq7qDwt_z5qdpataDSd82r5eajvs_6SQhjhJaR18EK4t3DBG-GW3c6swWirKKPCEG3AtK3MKYKJ7JE-7ftw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=RVW3LqkhZZuoJQ5_ECWwweu3aa4l3BGXiRQrGbu3saAWUXYdndhr9hW0lsGFPigaL2-5g5KUoxHtmlyVtHKOYNmSqiaaX9MR3HZibO0F4j1FXMwhHxTg6m6SNMUtXRHntXnmaRKTJwmsAtlimwPZYPQB_Ihr7gKNT_WLFlsV8JaIcOs_sVwoKti7ElZgirCzA3QBotO0J6d5rLgQHv_TKER5XLw--_W1i4s3_w4fspLggQ2FNhIbxCZWhGQ-tVzAIvpTq7qDwt_z5qdpataDSd82r5eajvs_6SQhjhJaR18EK4t3DBG-GW3c6swWirKKPCEG3AtK3MKYKJ7JE-7ftw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«همان‌طور که می‌دانید، ما پیش‌تر دو بار به جزیره خارگ حمله کرده‌ایم... اما در مورد تصرف آن، اگر بتوانیم توان آن‌ها را به اندازه‌ای کافی و عمیق تضعیف کنیم، این کار را انجام خواهم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68132" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68131">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
حملات به ایران ادامه خواهند داشت تا زمانی که من بگویم کافیست.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68131" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68130">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=v6MkYx2AKxqcsxpRcw31gIw9RhZquDM1FjB3Rdo2lOlewHvIlEE9JHKa1dpoHXya3GYAExdG8VLdhhEta1dobOpqMyTpoAzcP8GCdqYq3hGCr-zCEaAEGvqdLSz6bOF9OsNgXqvRHYZA71R7BcNJ_KXh9clRx33UJjUJbRmFUOVrFwrctQb1v8pbRwV2jw27u2ypF2NkNGjpH842rAohH7xJD2euUjEZkVwERaxtijGWguC0q7d1ApsuV265KqZSqXZOb651sBFdadIEwK0ipV7CProB5b2p9jVCLpgQ9YTz9JzQCpMFf4S8fUMmavUVIob5O1dk4_u7xZTIR_xDDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=v6MkYx2AKxqcsxpRcw31gIw9RhZquDM1FjB3Rdo2lOlewHvIlEE9JHKa1dpoHXya3GYAExdG8VLdhhEta1dobOpqMyTpoAzcP8GCdqYq3hGCr-zCEaAEGvqdLSz6bOF9OsNgXqvRHYZA71R7BcNJ_KXh9clRx33UJjUJbRmFUOVrFwrctQb1v8pbRwV2jw27u2ypF2NkNGjpH842rAohH7xJD2euUjEZkVwERaxtijGWguC0q7d1ApsuV265KqZSqXZOb651sBFdadIEwK0ipV7CProB5b2p9jVCLpgQ9YTz9JzQCpMFf4S8fUMmavUVIob5O1dk4_u7xZTIR_xDDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«در نهایت، اهداف حوزه انرژی در ایران را هدف قرار خواهیم داد. نوبت به پل‌ها می‌رسد؛ هفته آینده سراغ آن‌ها می‌رویم. ما تمام نیروگاه‌هایشان را از کار خواهیم انداخت. تمام پل‌هایشان را نابود خواهیم کرد، مگر اینکه پای میز مذاکره بیایند.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68130" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68129">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36032be115.mp4?token=O0czXPB3B92CNLW4s7ZLcKYoWe980CO2vYDHE6EVqbFuyY3VY4oOtNXqIzOU16su5HkJn7kXIG-nkW-IHAW-CpJo-YXKxoJlR_tAj1-hzl-b63v5b-ndcYBM8zT3lLvC2VrMDh5aigw4Q_Nu7YYOWXVyzc4fkGu7C_dsr6jPYh1SmdKeaPhxAlMPuM0YDxcpEQIn6ushgSi1GXVkuwsXVoE7e4Mm-pstZ0U6eSuPOP0Rp0W5JJixzs6ICHjKxCxFPx4WpIQjBt36mvDD5AKzau4zl5AZvqrpPSFtPeiMA-YDQuoFbnn0sv-ghE9JSsPPKMLKtaYW7LA11m9bGgZC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36032be115.mp4?token=O0czXPB3B92CNLW4s7ZLcKYoWe980CO2vYDHE6EVqbFuyY3VY4oOtNXqIzOU16su5HkJn7kXIG-nkW-IHAW-CpJo-YXKxoJlR_tAj1-hzl-b63v5b-ndcYBM8zT3lLvC2VrMDh5aigw4Q_Nu7YYOWXVyzc4fkGu7C_dsr6jPYh1SmdKeaPhxAlMPuM0YDxcpEQIn6ushgSi1GXVkuwsXVoE7e4Mm-pstZ0U6eSuPOP0Rp0W5JJixzs6ICHjKxCxFPx4WpIQjBt36mvDD5AKzau4zl5AZvqrpPSFtPeiMA-YDQuoFbnn0sv-ghE9JSsPPKMLKtaYW7LA11m9bGgZC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا جنگ با ایران از سر گرفته شده است؟
⏺
ترامپ:
خب، گمان می‌کنم بتوانید هر طور که می‌خواهید آن را تعریف کنید، اما قطعاً ما داریم ضربات بسیار سختی به آن‌ها وارد می‌کنیم. آن‌ها باید ضربه بخورند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/68129" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68128">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=dKK1F8bpQVQ84uWnr-4Kp3vyGum_JOGaSG9ZQrwAcsF6rhaAzmZUSCY-jjMCgtwMVXNWcK0yC204WaOEkES3S5ZFxmYYLzSpYHK5XHQKHveBakju0SrCgHqwWV7CzHjZxP8YQO5SQCADK2EufiMYdDOAb2mgKAqEuRl_gEz2JhdcYcLW7zLeWst_8eVbuN-I4TSX-3eDk56WaY5RkM91SeRiyHmPFU-xzyQz_2YSykSf2n0iFEw10SvDxkFAMx_WOv84fmfVQ1Li-8QvJ0VbGJpPHMBMpT0_UJkgJvAPvFqN9gpmDw-dW0WYzS6YP2XFOt9XOe0K8R6akqt9dMBz2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=dKK1F8bpQVQ84uWnr-4Kp3vyGum_JOGaSG9ZQrwAcsF6rhaAzmZUSCY-jjMCgtwMVXNWcK0yC204WaOEkES3S5ZFxmYYLzSpYHK5XHQKHveBakju0SrCgHqwWV7CzHjZxP8YQO5SQCADK2EufiMYdDOAb2mgKAqEuRl_gEz2JhdcYcLW7zLeWst_8eVbuN-I4TSX-3eDk56WaY5RkM91SeRiyHmPFU-xzyQz_2YSykSf2n0iFEw10SvDxkFAMx_WOv84fmfVQ1Li-8QvJ0VbGJpPHMBMpT0_UJkgJvAPvFqN9gpmDw-dW0WYzS6YP2XFOt9XOe0K8R6akqt9dMBz2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‏ارتش جمهوری اسلامی:
در مرحله هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف ۱۸ و سایت نگهداری تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68128" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68127">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68127" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68126">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
بندرعباس و سیریک بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68126" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68125">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=CZzOD1RmZM0P5y8eVjGOOE3eJ6egsaZoCs7c9mbtTqYlDLdMkszS5XIoqYXGz9YqMGiQIFIZraz2x5bapjY2KOYUPD5kGafon3kDrBtJfKwHzOYWXxyowBap2z2mW61QqbVkVZeDkg6W9FMKzhbxwk8hps5id7uoDUtUW9fcCkmm6HBVqgDlzduM3pDwvkDtZuTC722dsTI4cWPMTOmSPLa_X5uiqb_Omj50i-6IVg9aoB9YOPFLgfis3UsSYLJrs7HJf3koYwfc1GVwsQ2mCNDDbmZ0JS19qgFD8Dd-mlKwUYzPKiwavRmlPy8LypZEs-Ac8SBC3jwG1sS1hmPaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=CZzOD1RmZM0P5y8eVjGOOE3eJ6egsaZoCs7c9mbtTqYlDLdMkszS5XIoqYXGz9YqMGiQIFIZraz2x5bapjY2KOYUPD5kGafon3kDrBtJfKwHzOYWXxyowBap2z2mW61QqbVkVZeDkg6W9FMKzhbxwk8hps5id7uoDUtUW9fcCkmm6HBVqgDlzduM3pDwvkDtZuTC722dsTI4cWPMTOmSPLa_X5uiqb_Omj50i-6IVg9aoB9YOPFLgfis3UsSYLJrs7HJf3koYwfc1GVwsQ2mCNDDbmZ0JS19qgFD8Dd-mlKwUYzPKiwavRmlPy8LypZEs-Ac8SBC3jwG1sS1hmPaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
هم‌اکنون دارلین گراهام نوردون، خواهر لیندسی گراهام، در حال ادای سوگند برای گرفتن جای برادرش به عنوان سناتور کارولینای جنوبی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68125" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68124">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68124" target="_blank">📅 00:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68123">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
انفجار چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68123" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68122">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul5kIS09y3DZgjjhz_MYalp1I-nKrvbwfMD3LELFzKvRJz8AgV_mxxl50UEEm9IuG1-D4sNNQ8xL1vvcTGiLfkDwDCSoA9duxUP49FvIAA98bDQmKEHj_CcN34UmEDU8EWI3AaG4iGqo7m-oXq--124Q1pdC1KSHFCzEUH5a0TuxxX9H-HK2sh5YdM7yKxEby-wStVFu7B4QOI5BUmAbpd4pwOT0FThlFFr4RP18Ry-t2uNNWfkwRO2L_Hr-DVn6WHVMOviY4m8Ju_5i_0ezjJ6HnlQYyvKhSib2WXlHS_e0CSzXbUbVY8fKfNk46Pf72GBXw9oIhHIsvidHH955xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68122" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68121">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=ZFyyjhAXLZYhYt7E3KUzv4u0SM1UFRjTDOAdAYohN_YUZTNsDZ7W9YDbKGoUQOagMv8o2gfsRT7TmF_y7QGr6yM11O-OH0xctC8ZI_NDb2DvGHrD2Fhuj-ror-VIV13cTYQzbd2R4fTFiB7N2XwZdyBu6gHNim1BqC5_mMZ6PEp1OhAoJe3Ni0zIcCaImoKkiyVxMqxrGmNqBIYz_4akYnJboRo8jsW1O6obBkSfx4zjeTZ1_Got0UI7GL-TCZpU5l2Zo2lngiWqKgoBYfPJfvfKD2SxmNa3ljmsA1oQux5xC0lFzSilC_TL0xJGhhxDGBgsXM1q4rPUCCk9YdsLUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=ZFyyjhAXLZYhYt7E3KUzv4u0SM1UFRjTDOAdAYohN_YUZTNsDZ7W9YDbKGoUQOagMv8o2gfsRT7TmF_y7QGr6yM11O-OH0xctC8ZI_NDb2DvGHrD2Fhuj-ror-VIV13cTYQzbd2R4fTFiB7N2XwZdyBu6gHNim1BqC5_mMZ6PEp1OhAoJe3Ni0zIcCaImoKkiyVxMqxrGmNqBIYz_4akYnJboRo8jsW1O6obBkSfx4zjeTZ1_Got0UI7GL-TCZpU5l2Zo2lngiWqKgoBYfPJfvfKD2SxmNa3ljmsA1oQux5xC0lFzSilC_TL0xJGhhxDGBgsXM1q4rPUCCk9YdsLUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران تنها جاییه که بتمن هم به گا میره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68121" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gixIlmQbyp91PoQR8d5_MBHRV5u36-FTvwYmPW1uoWEsb-eFEJf58THc8nBMgwFczZT9j7nvARp-5akrtGYPcjcJkmEbMNMYmggoxJSAF-tABPckeBcdD9w6NYxw9_9RGzTzs2874x_Gni5-8Pc_suoPYVVCs1ySY4yH1g2D7YTSWMfTxu4IhRzMCs8_n_7at8rhquTmpj-d54VRPcPzpgYN7lLuguWuijyXNveeN0j1uh3AbdzoCEWssLCTIyvhXl-1d86IrpD-aD8dJ1d0lePv3uZZIBFuk5KGeeGZRQVpsgJYrDioOQCdoOE2KuB7fhRiT2_Vc6HhRFYZSB-nfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=lfN5mQMykvORxZXnkwCOyS0kwPiJQlnoPD29cNi3lpdOdfzE0l12DYZAO9BpDrMgi6CY8OTuEaHXhgg-Q3QYjk0HSrV3Y0kh4X3Rqbbrr2rYrliXlnD1YoAX_U5teztS2rc3BWxN6tNv4qrkcYXzu1yUyIoa9RKfW1zKjpapqGJUwZyDpgxwGGO1HYCY8IcL720XwLak1rP5Gal_KNrDTNeUXwcrXR-4KCzX7DHduAFNdedM1Xh_JKxyQwPi4adS78nO96MPpSJLC8Y8dKEpBR5BswVhX-lOe8loL4-hPVvU4b2hIfpkAP5uYmjUPIhGhj0D-tV89pYITK8NWRgVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=lfN5mQMykvORxZXnkwCOyS0kwPiJQlnoPD29cNi3lpdOdfzE0l12DYZAO9BpDrMgi6CY8OTuEaHXhgg-Q3QYjk0HSrV3Y0kh4X3Rqbbrr2rYrliXlnD1YoAX_U5teztS2rc3BWxN6tNv4qrkcYXzu1yUyIoa9RKfW1zKjpapqGJUwZyDpgxwGGO1HYCY8IcL720XwLak1rP5Gal_KNrDTNeUXwcrXR-4KCzX7DHduAFNdedM1Xh_JKxyQwPi4adS78nO96MPpSJLC8Y8dKEpBR5BswVhX-lOe8loL4-hPVvU4b2hIfpkAP5uYmjUPIhGhj0D-tV89pYITK8NWRgVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
علی خامنه‌ای، (19 دی 1404):
ترامپ که با نخوت و غرور نشسته آنجا راجع به همه‌ی دنیا قضاوت میکند بداند که مستبدین و مستکبران عالم، از قبیل فرعون و نمرود وقتی که در اوج غرور بودند سرنگون شدند، این هم سرنگون خواهد شد.
⏺
🇺🇸
دونالد ترامپ، (10 اسفند 1404):
آیت‌الله خامنه‌ای ایز دد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mp3e9wOs1_E22JcirZOLRkrifznWgYF-_9wRLw7K3FpxtsSAOyof6t8XBJhzKet1YpmKKVMYuNdQC-3uNzXzxw2qrB-eAu36XEujh7j7pcERCanFNJGph80WUWC-gH3Ck1vLs73peNpQiT5dIeDkA0moGc8hGliXxq4RlWa93FaJZIHVSAktGeGhrCWSrAaSmPLmRJXvHqFa3HUY_wGT_n-_aJk_TdFnbyCPrkWFwM4ATDh7uYZDXTnPVhi1JpPYlsTwHCZ9g2vMsAOXrWe6BH1zi4FXQhMpHgRlabVWAA-KEHo-9aCgFSvOMkETTHpkf0_u2suIEn65Z65qi7Ikow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqVvXCNAHlEW8s2gtQGi6hfbOfhuX4bVdDqaQM_da-FF-0_bxlZs_g_gu_QFZOxXjNvv8HYLnnP0j9_N-8opWceZ5XQdsTx9uqMjPQPamEfKtdSDUQTZWwVkwcjIfTfG9V7QLaG7QLWa2Cv9NnArP9Ad6nHg6WLNVzH2Qm9p_rRiEbujTYSrl1XeJvKpv2acEMboJs6wUEvaqponzaPhp8iCrpLHTiGKBQWnl9xgNCuj7LHhSCWgtQrB8ZgyEmI3d3q0-CuTnvKYtqq5Uw-g7CIoXlFtQEe2knE0w2WsmrNuz9JI9ZeFCLolQXYPgJ4iIcZUg13SJlGoaz-lIMpkBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68109">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68109" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68108">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68108" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUYCGgMwNy8sxejDt2YrRfV6OgLBLimggol9KBSgF9DesC6kxASMnI7rrJuCrVJQaIJU0C3xcOvYDKzz2eIryOeJZsRRGQYrGb9v_BuAomZcmv10vm7g23WGztfPMKu5qvl-YcZgaIL3fjRaPdCggxlvdvAnRuFsp9h6PvG-ZCMNOirLB9yEGC4RaFBm8wa-BIpdXdvnyTUTOqwdeEXesMsDhPvZX7pd8pOJ-nDl7Efer5EPJ11JnwcUGr6IHIfvyaVTAn_l5v65YJ4jC6uZjnuARi5rKoOka1wHroyCefnqmwbAPSdVUxjk8BB_1R_7rjVM8tuEwC5Odi8FHF0etg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m81fjI_D88be3YxCJOwOCgWPLo3g5fYjak95RZi2JMHe4i2iTtD7Y9sis2q8fuJkrIatrSLdylFMTDgi8KxV4CZ85yaQuzg82QnfUqQHrUtevcciLTElP2Z9z87RUQp6bMPXi1dxEOnzQZ5abWV6tKjsRmUtMXJl0W3MeYyu73jo31J-EWDw-ENHuk4tcX59npZcy4yIImqtnUuNbky9BOGLx_TAWaMADUftbMGM1-f9GtIYTVCKIBjZp-bGr-DlIJMi8kq9dVePbcNU6w8L-75VQTjmRK2FUnTU25ccmtP41Y4mpsirs_8njT-uJnASpEdktTh8Q-vkPN3y4pEnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHt9I5gaWtQOlfCQidwsxATO1nzhwzvNlBe0nzCiV22aR9APLCilbcaTLKadkQZK9aSKU1LzaGbvhj16Xwtn4NJjjLhESIoElEUEgY2cWLDC4jctDWNye4UHlXTO-zd1jTs5jAT0_Xs6Rofd1dyqgFJq9qkn3PAGAf98jm-4W4OGdoIolen3pMci4EBoDDA1OzOZV2oNgGuQu3CLFshYe9Ov1hBzzeRF12eFWJ-OWlDqh5oDRwdSzSNqWtzTdLDhbWKSfbF7ZKFGjrqAIQcjemVNjEUYN12MTT1q3EK1iHqj9nlxmxMe3CcmdwbtSfsNrcVkOqWgX2j_Zdi-A47B6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXv4mrfMfTQDc59oJit_G4rkeZ1PpwLdJbk5P4lsGq0roblAhp3WSFE0RULEnhDhj6oG7UhxZKcSj9_MplNZMH5J9fstdUOgq-DnQ0kyCwUMmwU8NBIwzxWav5keMuhdclIGP_ewQCoYIi4jEJvaYOeb5NZQS8xLHqwAf-zc7Onv4tAgHp1RA3FX3zMNW2a23uWeHrII0gZmNwySR66emuli7s5bD6veQg6jFcBKXL32Ic7m3hpSyYgNJql7l8YznGXKtviDv4DjUok4E8uaQIva7tfAVlhOrBrmMv_0x-U5xKdj2h0lMqNelFYriH8vD4wIki_bo_-ka3z3L8A8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnnBFoblak4eTOWAx2GcRD2FmPuA7awHBK0uMNK5y3Lcjb1OtYB7nC-cdFJC-EurFEqUJWwJWsIk0ArMS2K69I3735hqvWmyZSB2PQEDOLmS4nQdevoUARh3n_MBciYgDdI-q3l50w4QKJTOjLrQdz6wG8hnEEFtm-T60W-oDDmwvFqDQhXCAYyScBGeDqFdMQxwCC24yl8qssEGmdK9Z_kpUmJlITGvdM4Mzti8aZIZ3VdeSHo84Mq5c_A1OCvp8OWEy38aEbsx-X8nWSQUAA4jZG5Fm8pGW5VZk6fxMEdLhGw-IGPhWhZvZmxuV7byZ4aW6rsQU9YDVRRs-jwQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=kWqwW64a_LJBebhhCOh0AS-VyripCbLoJb9_AHYRD8bs5GoVLk9Vk2JKUJCU2octsRvV50TP2JzOH2Lxn_aNywNB4-wQ_0IBersQ8Kz9QSw5rD7FeBo9PqbnFJ3WqZtvOcZNCypuUHSgYn8YUCjnvMg80qIjVOtfnoQZHa4R_UEqIdZzb3NVnqG3LY9mLu_oi2exXOGJYQxPQg6VRzlwpJ8hcpap8wOV7Q6gu9Kc1jfpaUL9vXlgXReIDSyRxhxsaXQzlaJNkjoFzYMsD1ZdKnE35lJjMUn3DjkQWf9yLHonZQFXpKUVKUi9QTO7BABlg1r2Qau0uWyZJOPIGztkJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=kWqwW64a_LJBebhhCOh0AS-VyripCbLoJb9_AHYRD8bs5GoVLk9Vk2JKUJCU2octsRvV50TP2JzOH2Lxn_aNywNB4-wQ_0IBersQ8Kz9QSw5rD7FeBo9PqbnFJ3WqZtvOcZNCypuUHSgYn8YUCjnvMg80qIjVOtfnoQZHa4R_UEqIdZzb3NVnqG3LY9mLu_oi2exXOGJYQxPQg6VRzlwpJ8hcpap8wOV7Q6gu9Kc1jfpaUL9vXlgXReIDSyRxhxsaXQzlaJNkjoFzYMsD1ZdKnE35lJjMUn3DjkQWf9yLHonZQFXpKUVKUi9QTO7BABlg1r2Qau0uWyZJOPIGztkJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=aFup_udgQ2t__XVB_VNQXXFvEjclru8urH7ctWXtE4G7MnltSWC2VjS5Bgx9lrivPJXE8-IIsQ9a7OPbL0UztGX6B9oTN-clKSGua4uNxW0FwGop2yBbhSw8PhzCc2ANMz9hIx-1uhIZGstpWbvo23KiPgXdi-gNOKRYY8aYNC3qjNHZMJTZZ97Vj5DqiFDLrewWnQ0ixe_K4qTZenVpRhp0NXCkTUAWq61RPA-ZjiqP_DUth9rEx6NQXBZyUFutYp0PQYhT_kxBiolchU-LQJaEoLbDEVjXYtfhR7Ww1UHUGMFY5TrKJeC-RPMvM53GGteapap1PCbdcc27lIpumw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=aFup_udgQ2t__XVB_VNQXXFvEjclru8urH7ctWXtE4G7MnltSWC2VjS5Bgx9lrivPJXE8-IIsQ9a7OPbL0UztGX6B9oTN-clKSGua4uNxW0FwGop2yBbhSw8PhzCc2ANMz9hIx-1uhIZGstpWbvo23KiPgXdi-gNOKRYY8aYNC3qjNHZMJTZZ97Vj5DqiFDLrewWnQ0ixe_K4qTZenVpRhp0NXCkTUAWq61RPA-ZjiqP_DUth9rEx6NQXBZyUFutYp0PQYhT_kxBiolchU-LQJaEoLbDEVjXYtfhR7Ww1UHUGMFY5TrKJeC-RPMvM53GGteapap1PCbdcc27lIpumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سر دادن شعار مرگ بر سازشگر در مصلی تهران
صداوسیما هم چندین بار صدا رو قطع کرد
🤣
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=Xx4Yv0hUksA2qSM0omHTBuQeFXYsZsLeMJ5IJaYaobIVYv0mSBS2-inR8sTbmAtPPPN5-htNuJf0VxdU1kioGuuyTUavDPkoZceMAKgCK8etuJv78KRdVcHlbYIRelpdAeAX7gYv65KiAFw-bJzmJy385D5YCGZKNjFBOeFX75_6YPdlgQ6BDeAdCPetc3OlDeJ4vCxgO49tmHsmHeEpYaMwYOQ3m2ACEQHfRhrFRGq3qKZQ_WInZ_oxXdCePAAf_pDbIpv_Xi_fo29Aotx9kBdFGPmaAUiPYaMQ0OzudUFh-L_EVwErbnnInwyA5KDyqR0ESfPCTwWBm5j6iiplDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=Xx4Yv0hUksA2qSM0omHTBuQeFXYsZsLeMJ5IJaYaobIVYv0mSBS2-inR8sTbmAtPPPN5-htNuJf0VxdU1kioGuuyTUavDPkoZceMAKgCK8etuJv78KRdVcHlbYIRelpdAeAX7gYv65KiAFw-bJzmJy385D5YCGZKNjFBOeFX75_6YPdlgQ6BDeAdCPetc3OlDeJ4vCxgO49tmHsmHeEpYaMwYOQ3m2ACEQHfRhrFRGq3qKZQ_WInZ_oxXdCePAAf_pDbIpv_Xi_fo29Aotx9kBdFGPmaAUiPYaMQ0OzudUFh-L_EVwErbnnInwyA5KDyqR0ESfPCTwWBm5j6iiplDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب ترامپ درباره تحقیقات اف‌بی‌آی درباره مرگ لیندسی گراهام
⏺
خبرنگار:
«آیا می‌دانید چرا اف‌بی‌آی در حال بررسی مرگ سناتور گراهام است؟»
⏺
ترامپ:
«نمی‌دانم چرا، چون فکر می‌کنم او مشکلی داشته... من شرارت زیادی در آن نمی‌بینم. می‌دانم که انواع و اقسام تئوری‌های توطئه وجود دارد. فکر می‌کنم اف‌بی‌آی وقتش را تلف می‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=sz2CxIVdZk-jvvNX0CxgMjs8eJhJ-74JDChC1w4oXnDPlW2tDBYuUWdhhLvOddtdyf8G8MnfmcQo8zG65xEN_IhXdiuV_WG0ppzr4dheGytJrOwZQ1Hd05FubqRVusdIOeIxP6XzsTDtC3NYQdIHE_TnV2VQFQV6XoCI5U28VG4BMKqiOI141ZZTbYAvu7tf18vbAEzvahxhlwuRa5yHQ-WjhK9thwncyEHHzVEGEkrGouTvH-RLjUjNFA_VgGsIgmeoMF5x2TPXNnVsDIedDcwcSZzzfq4qkRGUHyEn4dTEh2aVMDvMQ10-1YHE8zBlhmHWO98XNKvhEZW2ySp5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=sz2CxIVdZk-jvvNX0CxgMjs8eJhJ-74JDChC1w4oXnDPlW2tDBYuUWdhhLvOddtdyf8G8MnfmcQo8zG65xEN_IhXdiuV_WG0ppzr4dheGytJrOwZQ1Hd05FubqRVusdIOeIxP6XzsTDtC3NYQdIHE_TnV2VQFQV6XoCI5U28VG4BMKqiOI141ZZTbYAvu7tf18vbAEzvahxhlwuRa5yHQ-WjhK9thwncyEHHzVEGEkrGouTvH-RLjUjNFA_VgGsIgmeoMF5x2TPXNnVsDIedDcwcSZzzfq4qkRGUHyEn4dTEh2aVMDvMQ10-1YHE8zBlhmHWO98XNKvhEZW2ySp5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره لغو عوارض گرفتن از تنگه هرمز
:
«آنها (کشورهای عربی)گفتند: "ما ترجیح می‌دهیم سرمایه‌گذاری کنیم تا عوارض پرداخت کنیم." و من این را دوست دارم چون هیچ‌کس نباید بتواند برای تنگه عوارض دریافت کند.
«در مقابل این سرمایه‌گذاری، کشورهای حوزه خلیج‌فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری خواهند کرد. این در واقع خیلی بهتر است!»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dhts4byZApzyz9400K9OWEBmh3Fnf100wCl6lAVCcl3juOm5kriy6JMeIt-_C-0MlGghkWevs7DmIDVxmsPSawMPcJLINkk5MLc5fLgb3f-xvdDxPViFtOUHX4k8zoabZuibN4i52MAQITr2M1hzbWlLH8Bo4g6QgeKmcODlUObiTdQeUo2oKziMM4cPQxuIxpJvGYcVYnx2lc67Y1ntmOEHQVsdWHd7ajSYu7PV1Pg8RT8YEM1sY89OI_EBBB4A85LsS_EStk6A9A-ysE9I9-gaKMO0c4abeZ1YWyRK4xTT2TMFRKVRXBYx2lZdR45LOoKxEAp8tGELtQgqFvva4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp7PA4WsdFzgeslThhYSt4x1X9kt_sQx_ETW4ATUHst3OGV20tfPtQOnN01CgwvrEHZ99Kj-Km8CoAYdvZEHWbWDLQTx1hAQUVaIu4xDfdb_uGva9TqxBIOoMysvtHI4TpnL4SdkpZst1zNyLJIghI5XQqJPy139WFWYlVx5zAvuLdEH7A0htl6Ar2eVtuoe-L0m2ECILieGFTnG3XG7rV7WsKbMW8yXHxJ1Xer4K6Dq5aO3psFx_Aj0QKJvUXpWjqwaEDweD1frtW0qfQNngEt9nz7zv9PLcfVgP0bJUHLL3GButfSQkiTXnl6B8SXu8SPIdvXI-mbH4NP9pFuUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68088">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=cfBcTKO2xzq9Aq9B5NwXC_FLAZi_zpGukTHHfVhMhHL5nl11IEX-YbyItABA5rv3vhFapIzlRC4TPEAIgJ4u0Evn-ZUBGC6tBd4GaQQY54k92yRv_cgMuv7ZLRRz9Rej5jHVE1ZwX5O_00NbnC_k5T9iqK1UpZVqKwHJIjmc5v_OSEYnMaGTdx_WB8VpLcTKZrU1JeX_xok3J_XTHs5ki9bFTFVUGUBSYqlqEbolKfAXj3CUwfPSzwpJFUxHfrlWwNg58MGKebGfuHaFSJh_gushhpAAIGwWvb0vmAN84Q2UAVGCdK-Qqv811yMfFibAObYpM-OFPoQgISXaqsjHeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=cfBcTKO2xzq9Aq9B5NwXC_FLAZi_zpGukTHHfVhMhHL5nl11IEX-YbyItABA5rv3vhFapIzlRC4TPEAIgJ4u0Evn-ZUBGC6tBd4GaQQY54k92yRv_cgMuv7ZLRRz9Rej5jHVE1ZwX5O_00NbnC_k5T9iqK1UpZVqKwHJIjmc5v_OSEYnMaGTdx_WB8VpLcTKZrU1JeX_xok3J_XTHs5ki9bFTFVUGUBSYqlqEbolKfAXj3CUwfPSzwpJFUxHfrlWwNg58MGKebGfuHaFSJh_gushhpAAIGwWvb0vmAN84Q2UAVGCdK-Qqv811yMfFibAObYpM-OFPoQgISXaqsjHeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نظر مراد ویسی در پاسخ به مخاطبی که گفت باید حرم امام‌رضا هدف باشد:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68088" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=GFzSpVhTRYMSj-goHjL0X1Pjacfgn_o41nI-dMO-zVx8IcV2gE9BRbTxWJG5zYz9mLbeb82hRZn4A3kP9wg7UhHa978ixJnCxKZJh8aLmxKTi5Tk7UKJ19GNZ3yzuxMBsL0AVLRxmIBkBSJVHTiAAVyicIKMq-VF914-Ti6GTqT4hpMcwnCU4EPMab0zyFR75bExHzs9VKJ-caqKKMDZMvg5vxJ6ixPupIUKvntvJT0lH_8QnwAuKM37L9qp0itjIN5Oqphc4BFPoxJl3we3kLEFLjXPTxArPGS5hYMwyqyJzD6baPYlE_i7xmcHl5ZdfRcjgUINg-DJCJuca9EOvXbVd0k_KrzKG4CM7IZFqgYH3ZdhWaa1FM23bKqmk-ET7gYqtuVSoNDd2QS9nlxMzBcWgV5TwroZcpLVZpIjVmmNIJNuZxiqBl-CRu7BbdEwxqvPTya-7iP3TrPvtscskI1UNKSpzulQJ-x2BTEK8Q2D7DnFS9CMCUgVjw3TRmNhDqi8uYiOu4LBpvDJ0NI4FWGnP6pkCH8bnBfI8Cu56t5ZILZ-hpPwe3n8ZGh9rOa4pidKsFhDyQGDfl1VOp4K0HpaNwFC4ierrpLMtZmAsLCr_laAIX_E_-7w7DJfHCvMAyvXivSR2XwfgTCWtOctiE-SK0qC_xRCaNt2cwm40TI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=GFzSpVhTRYMSj-goHjL0X1Pjacfgn_o41nI-dMO-zVx8IcV2gE9BRbTxWJG5zYz9mLbeb82hRZn4A3kP9wg7UhHa978ixJnCxKZJh8aLmxKTi5Tk7UKJ19GNZ3yzuxMBsL0AVLRxmIBkBSJVHTiAAVyicIKMq-VF914-Ti6GTqT4hpMcwnCU4EPMab0zyFR75bExHzs9VKJ-caqKKMDZMvg5vxJ6ixPupIUKvntvJT0lH_8QnwAuKM37L9qp0itjIN5Oqphc4BFPoxJl3we3kLEFLjXPTxArPGS5hYMwyqyJzD6baPYlE_i7xmcHl5ZdfRcjgUINg-DJCJuca9EOvXbVd0k_KrzKG4CM7IZFqgYH3ZdhWaa1FM23bKqmk-ET7gYqtuVSoNDd2QS9nlxMzBcWgV5TwroZcpLVZpIjVmmNIJNuZxiqBl-CRu7BbdEwxqvPTya-7iP3TrPvtscskI1UNKSpzulQJ-x2BTEK8Q2D7DnFS9CMCUgVjw3TRmNhDqi8uYiOu4LBpvDJ0NI4FWGnP6pkCH8bnBfI8Cu56t5ZILZ-hpPwe3n8ZGh9rOa4pidKsFhDyQGDfl1VOp4K0HpaNwFC4ierrpLMtZmAsLCr_laAIX_E_-7w7DJfHCvMAyvXivSR2XwfgTCWtOctiE-SK0qC_xRCaNt2cwm40TI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مستند "عمامه صورتی" که در سال ۱۴۰۲ تولید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=pD0DYNc8dfaNUHP3l_C-Z4_o9A69ZIqB-myf0zNcfyXLx-PVlVHyANTJ5L1fMmhYVZz3j1ZglL1cfOTl6yGW6uGMgbscE5Hr9ZBwY4JiIY78IkO-5KbfHkhu3GPXxU7di34JkXVRLnMVQoO2aCPEkj93Q76Ct8m9r3giEEMsytqEJyFL1-mcRf39uzCweEcJ9N1nL1YGKCjzqlpBY8zacyeOAGCAhuo-xmbvmYFWcWtSze8kBBKFukENZRydczdO-P9fwXbnhfjB0C1eUofihabcI5az5FXkS_4Tz89P07jJ9L6sRzneW7J6EuFaTdPK_UP36lGNczQ-2atcs-u1Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=pD0DYNc8dfaNUHP3l_C-Z4_o9A69ZIqB-myf0zNcfyXLx-PVlVHyANTJ5L1fMmhYVZz3j1ZglL1cfOTl6yGW6uGMgbscE5Hr9ZBwY4JiIY78IkO-5KbfHkhu3GPXxU7di34JkXVRLnMVQoO2aCPEkj93Q76Ct8m9r3giEEMsytqEJyFL1-mcRf39uzCweEcJ9N1nL1YGKCjzqlpBY8zacyeOAGCAhuo-xmbvmYFWcWtSze8kBBKFukENZRydczdO-P9fwXbnhfjB0C1eUofihabcI5az5FXkS_4Tz89P07jJ9L6sRzneW7J6EuFaTdPK_UP36lGNczQ-2atcs-u1Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام ویدیو ای از حملات به ایران در طول شب منتشر کرد.
در اواسط ویدیو نشان میدهد که لانچرها در فضای باز هدف قرار میگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdI6sQNg8c9l8npIlxZLOwyJLwcAFqR7qEHebaztYVJl4aJdjvcp8TLdhlFwIjwykE0bkkhxxLmy09wvpK9hA-CfRVNFbudqoqJzK4dnXq1OKmT-9cHvoyVGPzctO7W5B1xwygFw713AWQYCM2Z2zTWmJy1IovSYiQvJZHc03CrT6f1fuoEb8NAfODxIMeXxqCeSE0SuBZum8CkniOfnE9KItk3p4KgienAFO3JJO2EO69bFqDlou1KlYSKExyyw1Nrq73C7Du2wxNgdEfxP3eQtnzdzmou-aWHoiGmjhvR09xqKICwQXH_ASBU6jeA3etamyliirK872E_OGEgilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=j2tllj09FH1F0UR21kFQlXCM6r8raP4SoE81IzUZQdKXxbqG_pSVNXWSgD5bH6cdTnoxFr_8OnVi7dwW1PG09e7-yY52-X1J6Tlsdc0KVQ_wb8NEg3CTJlxtNhIt74zNMJdaIuyZW6n8V_qAuWSUrSuWfZlhYQcR0RayCMWT_y7mJPHkEtjJQdcyGERL7UI0-FK1DFpUgn1AzpE_KOlU38tU6b5utqia91U54b4e5cf8WOm4DnpkhveVcIQcuVnob8EEgstQMvUtF0Htdunagz49_Nan2g4TDX5aX3JH-_2CoegB3qK4EZOHjtkOGAlooD3woRMPpvVVMzxEj2vAmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=j2tllj09FH1F0UR21kFQlXCM6r8raP4SoE81IzUZQdKXxbqG_pSVNXWSgD5bH6cdTnoxFr_8OnVi7dwW1PG09e7-yY52-X1J6Tlsdc0KVQ_wb8NEg3CTJlxtNhIt74zNMJdaIuyZW6n8V_qAuWSUrSuWfZlhYQcR0RayCMWT_y7mJPHkEtjJQdcyGERL7UI0-FK1DFpUgn1AzpE_KOlU38tU6b5utqia91U54b4e5cf8WOm4DnpkhveVcIQcuVnob8EEgstQMvUtF0Htdunagz49_Nan2g4TDX5aX3JH-_2CoegB3qK4EZOHjtkOGAlooD3woRMPpvVVMzxEj2vAmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده(سنتکام):
ملوانان آمریکایی بر روی ناو «یو‌اس‌اس جورج اچ. دابلیو. بوش» (CVN 77) عملیات پروازی انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXTap9VgC4JfqwDNhOrltsVIHBdcIanzBfW9exqMz4L7liDNqWJa3-vsptbmylmamve9DLiEcNyFPy56Lemeuk8_J3wLBQDTctXW3iufQp8P1m3kW0iqZMYOUMDTe5WhTUmbwJ3WKNtEUnTjdQWo1IITZt_3nTpeLyifmvF7fS1jrzHPEzr_w1osLfvp56zM4wKwkvhvNcg_i3LI0RpzVc7Lh5_wJK1CTzFhlDOjxEfljdRr4hNLNvqYq2Tgq9sCD2k60ivZstiXH2YpBn9loIw10_KsLiMIp7FzZse3D8nVtQbnLdFz9VjjHbnBiv467cs34nGnaSZR_7CDlwguTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=T7-1BUl_Hq353mzVxIjVetNqikg_GWHzrGYbWPJb9ra0wt-yyS0O0_cQhfgtKwWX1BNl_TrqIs7N8BI2GrBCfJWaf3cxrQM7HUEoKEnbH0Kn3pxVUum2yGPITPQMqzGGdl2fo7v2pCOUPvN1GmPlhehlujN4tXL91AsKGAA-bRW7VcI3lzinRgfF7nzEyPpzGWKgMdtbZIuKQv3UsnJcWgHqv99OlrbYFGOHkIy0NAMvlthNnXECApTJP2g7q4jtiWT1wpXjmWNS1bCF16xELceKtaLJUlRnyrtLgspysm0h0nFd0FYXnvmMQCYGy78RVa5ApKFet27gb_HKOKV4iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=T7-1BUl_Hq353mzVxIjVetNqikg_GWHzrGYbWPJb9ra0wt-yyS0O0_cQhfgtKwWX1BNl_TrqIs7N8BI2GrBCfJWaf3cxrQM7HUEoKEnbH0Kn3pxVUum2yGPITPQMqzGGdl2fo7v2pCOUPvN1GmPlhehlujN4tXL91AsKGAA-bRW7VcI3lzinRgfF7nzEyPpzGWKgMdtbZIuKQv3UsnJcWgHqv99OlrbYFGOHkIy0NAMvlthNnXECApTJP2g7q4jtiWT1wpXjmWNS1bCF16xELceKtaLJUlRnyrtLgspysm0h0nFd0FYXnvmMQCYGy78RVa5ApKFet27gb_HKOKV4iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX2yz-YkPkpvbXN5RruGpYJ70va-LKi1bv_WmBzfAy-5mzJDcQXrFmIUc4uOa2WROl00_Rs_DpmQKpgby1F0Z1SDFh_bsh6GkT2mqHXYiMbTcySZ7bFvS4En0tDXhmpBnujnjitMoKoejDDiza9b0w6yfXlDIsKOUkcK1RtDamvYzYXVotNwmplybi-XLZln7UtibO_uT86vHBUusmmJO5jDLjHgDTnbC228rZh05oyaS2QkmTs5QqLzojIU8CdhQOTqzFdVz_ryB9YzAzYieevOub5vOfO7Y6im5NMQ8dSFIY8lkJxaOoJzBjDtQkGkF74PAm5GyRX7TjfCXFZ2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2QeTXSxMBxtw3Mv8GTUPuwwbv2z18x6K452k6d3pMcLIhkvTItqN3UDCo5lGtj3FF9J8xBE2474_wFu2bvSUhfEaE4irQPJbG6M4I9m0uEFcID0ppypkFdmRIq8ogxSKweSddTEy31kcEbTsL_iWqjUwQC6lBRCP_jWHs54M2JVOK5nLLv-MsAgbT5_R6kivnvR4KDlsle5q9Y4RsAKJS1pkbm7oJ_P1iX-nNcl-HChYQxPR0DNfW4agyUiJBEolRbh6w6m_cfhw2b9XUTTx95ntnnVvZG6WGAOBt5SoRh_RU6ZlVBS364fB3VB96lh8IOHErxdWSOuqGfyNbWcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=hQebsLSc9qgH6lk_S7ubEzaVHHiLmXh7-A4vPsMdUlRO8czUCQUtK__I_kaxlFwYIopF4U2wY660toQ2zR-cXor6dnmtx2VQ0JDn7-VRl8Y6rEt7ogLo3DYtx4lZiOdr0RDKkot4SY_UgUGrpTybRQxySRZ1Urr-lDA1GKgoSZKD-haCxkkAcw9SpKnq7e1n72ZOMgYnPjTG4YP5I_9rCPkxw6hpmD8NMQhj8wYdG1X-AL6edWZBVJvrhCFYgdemyV2Aa-AJALkcRhELWKAYeMwZ_SCEqtNovC3VIaBOmKoFh2K5TNK2DoBiCaLTCNPcVQS1cZBhq5Ox5BkpOooonw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=hQebsLSc9qgH6lk_S7ubEzaVHHiLmXh7-A4vPsMdUlRO8czUCQUtK__I_kaxlFwYIopF4U2wY660toQ2zR-cXor6dnmtx2VQ0JDn7-VRl8Y6rEt7ogLo3DYtx4lZiOdr0RDKkot4SY_UgUGrpTybRQxySRZ1Urr-lDA1GKgoSZKD-haCxkkAcw9SpKnq7e1n72ZOMgYnPjTG4YP5I_9rCPkxw6hpmD8NMQhj8wYdG1X-AL6edWZBVJvrhCFYgdemyV2Aa-AJALkcRhELWKAYeMwZ_SCEqtNovC3VIaBOmKoFh2K5TNK2DoBiCaLTCNPcVQS1cZBhq5Ox5BkpOooonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=in6G5svR5U-Rkx2o_j-yuuEqgm357AdxA5HNrsGxdixQzT_lPHQz6YIMTijhrumiyXnvVNWK0i2YPQV-eFWw85kss3kfg72xnSlhrKd29lyOUoOJ3gRVpwQg8yehXG7PsPbv_Q8heZwm-trndrJogjeOQ4YKS8m8sneqGvVrA0Eb1jnr3FS_95xXQZJBlZBkjqtkY7Tk9yI6HtPAt-i3dF_3IZXi9KdZ8kfRIqziezRtIo_hZBdkdPD4HnMIz0UiVJxfw0RDxic0Y-tuqxmVYEhOOY7nn5BYCOPSqWynNXIw0hc6rbYCska3W4rG5hPrUTTttCzxo46_Kaq7mMrhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=in6G5svR5U-Rkx2o_j-yuuEqgm357AdxA5HNrsGxdixQzT_lPHQz6YIMTijhrumiyXnvVNWK0i2YPQV-eFWw85kss3kfg72xnSlhrKd29lyOUoOJ3gRVpwQg8yehXG7PsPbv_Q8heZwm-trndrJogjeOQ4YKS8m8sneqGvVrA0Eb1jnr3FS_95xXQZJBlZBkjqtkY7Tk9yI6HtPAt-i3dF_3IZXi9KdZ8kfRIqziezRtIo_hZBdkdPD4HnMIz0UiVJxfw0RDxic0Y-tuqxmVYEhOOY7nn5BYCOPSqWynNXIw0hc6rbYCska3W4rG5hPrUTTttCzxo46_Kaq7mMrhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhT_PFwtbqLAZr6y7t5nC-FLdPZ24OmPhpSyGeeqCnFGz8ZsFImBlOCfAk3Jv7TBPexdOIatDSKyZDifWHMZj8Zf9BVEGtWqBPKHN5eBvTMIffXL0MMc_cSjiojyQADy8YVF46S4XeeyQsrGQfLxYvJJ1D4WyQtZdHC_ZD8Iz7QO60AnBgs2kBONkXi893E4vb2R-a-LkGNUd-kKltHgNVdW-osvzBxGsuM6MpHq8aqr1l6XOz0lk45bc42mpgO4SdHytpWaVrWj4veCd6jy9B8yA0i8YCBfqgFOS0W97vJ8_ksHvIzv5i28fZSttkv4N9I9DQl4Vd3HSqmI611BAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=G5e7PeClUN0r99FfcgSZn5HTjJJkoZwZF071PZmMVZoHNGRXqreP-tn-cy-1smeWLyfTPC8eAnmfe2OVz3tcVeLJOFsB6AOTxDNq6JBGB8Rk59lGzMAimJJcMNKsWL6sfj5jPtJJMYatydmkL15becdVnuQjOkLClhCzgLByQ0DS-9PJqOo6nPsoNamNgY9UvOIIZByjYyfANAyskebT5BjNKcpHvnWfFDJehQeennx8G6scENoorLnUkI-xKMnRxM1u11QfNecLdcYX1l9IaePHXj4KS6nxSiAPzY798dZei5cc8u_2B3fNp2bB194HPgxpSYVLBPxFJ14BXtgjSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=G5e7PeClUN0r99FfcgSZn5HTjJJkoZwZF071PZmMVZoHNGRXqreP-tn-cy-1smeWLyfTPC8eAnmfe2OVz3tcVeLJOFsB6AOTxDNq6JBGB8Rk59lGzMAimJJcMNKsWL6sfj5jPtJJMYatydmkL15becdVnuQjOkLClhCzgLByQ0DS-9PJqOo6nPsoNamNgY9UvOIIZByjYyfANAyskebT5BjNKcpHvnWfFDJehQeennx8G6scENoorLnUkI-xKMnRxM1u11QfNecLdcYX1l9IaePHXj4KS6nxSiAPzY798dZei5cc8u_2B3fNp2bB194HPgxpSYVLBPxFJ14BXtgjSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی،تحلیلگر ارشد اینترنشنال:
چشم انداز موجود تشدید جنگه،پاکستانم دیگه نمیتونه بین ایران و آمریکا میانجیگری کنه.
جنگ سوم بین دو کشور تو روزای آینده شروع میشه.
اگه اسرائیلم وارد بشه یه لایه دیگه از سران جمهوری اسلامی رو حذف میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68068">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNAlqo0i_AbI1mlnvs2hmQnFzGgoMOYuPw6Jsp2iwjHce3aP0VzQkhmiiDbLCJda58DPJqnSTjtMnqimS8HUSJEqYcF7wVtz_f0cxaMwnbSoHFvCgoboVLzeU51oGUp2aeSNjmXvR64TG34nlwJM1Vp2vfOGFpwc26v93jF9x4Tgf9l1rXWyqcgkQ-WsnIMRy_kqvgobnKplnTSEgsMpL1QEvTcLAPNGr1R3CyjIYLhjGddLiMVs2ptyZL7d5qO1fyNcUkhqk3kYbq9J7XynO1GnGzINNU-KaR37bfI5IO6_NGmNdhHuJWwNY2NOLs0aTjqftJT4Qqx2E4WoP6V7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) آخرین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب (به وقت شرقی) روز ۱۳ ژوئیه به پایان رساند.
در جریان این عملیات پنج‌ساعته، نیروهای آمریکایی با هدف تضعیف بیشتر توانایی ایران در حمله به کشتی‌های تجاری، با موفقیت به اهداف نظامی در نقاط مختلف ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند.
نیروهای سنتکام برای هدف قرار دادن سامانه‌های پدافند ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران، از مهمات دقیق‌زن استفاده کردند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند.
نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار باقی مانده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68068" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68067">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=Hg4m9YIDHOQf7QYvRMi_vGPXB3QRNZOKyh1g_fIChTxs8bKJNPV_yxVPYBXMu3gJCHJZJnvNrWL4rUUIFo2iawrsldNWDNEgAgoaL49RGFWLnQ373z5HX4x5daiJqlJqLXLN-cQIMOmoiecpR1wZ2UAbGa9vX7sfp0srdldzJ_5xUtpG3IKEBG_VWexXR0byqyfFjEfquYTLjrC-keO2gyMmWN_WJzKT_KSULZJSt-dvciAXYIyr4GqsjhNESqWAm2s5Hkf0vpF3OTNxUM2wxZ0QmT5e0gg-5urCpyIl7A4eOnInAAxeEuoyXPyRLJdnpT7OPMR9eVUpCkue1KLe3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=Hg4m9YIDHOQf7QYvRMi_vGPXB3QRNZOKyh1g_fIChTxs8bKJNPV_yxVPYBXMu3gJCHJZJnvNrWL4rUUIFo2iawrsldNWDNEgAgoaL49RGFWLnQ373z5HX4x5daiJqlJqLXLN-cQIMOmoiecpR1wZ2UAbGa9vX7sfp0srdldzJ_5xUtpG3IKEBG_VWexXR0byqyfFjEfquYTLjrC-keO2gyMmWN_WJzKT_KSULZJSt-dvciAXYIyr4GqsjhNESqWAm2s5Hkf0vpF3OTNxUM2wxZ0QmT5e0gg-5urCpyIl7A4eOnInAAxeEuoyXPyRLJdnpT7OPMR9eVUpCkue1KLe3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخطار پلمب، مانکنت نامتعارفه !!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68066">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJRXGZsCKJ09zC3Q1w2YeoLH0TWfDYinuXPqSUxTxri_44oNiQDg5n5fwvsyk7VjrBwYOZrjFHCZ8W4_Gyjd9WtuXUwL10KZf17jVaCy1-Ry7F19Ai3rScFj6pAp_DNnsIfY0MAhfVBLYdH-DnXh4w3v5ZsqS98Dt-_aUxQtzXSbIkRwRWpkG5k5Xn8gtr2PD9NUCXEupRVrxWQEbJQnSkxL7K7voJIfqDkTAkIdG-qIscmhk902CeC7y8KIVfwj4Gi0knAjM_w3I2UeIl6hQoSMEHJd0jNaQdV-SleLXoOGt12bKqfDohOZgiUVtNTaWsgALs0cS3AwdwkpaJ3Dbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:
اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد.
در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای خارجی، از جمله در مجارستان، با احمدی‌نژاد دیدارهای محرمانه‌ای برگزار کردند و از رویدادهای دانشگاهی به‌عنوان پوشش این ملاقات‌ها استفاده کردند.
این طرح در جریان جنگ ایران و اسرائیل در سال ۲۰۲۶ به اوج خود رسید؛ زمانی که مأموران موساد پس از حمله هوایی اسرائیل به محل اقامت احمدی‌نژاد در تهران، او را از آنجا خارج کرده و به یک خانه امن در داخل ایران منتقل کردند. این اقدام بخشی از یک عملیات گسترده‌تر برای تغییر حکومت بود.
این عملیات در نهایت ناکام ماند، زیرا احمدی‌نژاد تحت شرایطی نامشخص خانه امن را ترک کرد.
به گفته مقام‌های ایرانی، او اکنون پس از آنکه مقامات از تماس‌های ادعایی‌اش با اسرائیل مطلع شدند، در حصر خانگی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68066" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68065">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr9dGfvFo0HUsHl8b2VZB68I64DuhfL6NJLc3oeqqLkkYaA8HH2g-BkHXcvzkcYqcgEwC6oVeGU_cq8gWYL5k_fLbkNVJo9qBWUzOnjChdegl9qDerD7ZrlY_nG6UU8vsjrPn_JoO41EaL3AxFYlZ7EVm_n3F0Q12NweBH0s3I00yXfQf5LuBdgaZueFMCm6R1OZkUXKQi3l-NxN13uuM3PCmjYCrETDAgAgTXpjV5-CS3Y69oNlV6cf-gkN_yZCFyeesPwigwv806EksfcxfKH4sFP_mZQOu-dRNmNlqrrr9Wo74Ve05cJaHihYQrktjEZMX6teAkXnLvCINdE64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
وین ریت 80٪
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇳🇴
وین شد
✅
🇦🇷
⚔️
🇨🇭
وین شد
✅
حالا هم دو تیم فینالیست مشخص و در کانال تلگراممون اطلاع رسانی شده
⏳
🇪🇸
⚔️
🇫🇷
‌
󐁢󐁥󐁮󐁧󐁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
t.me/bet__gg</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68065" target="_blank">📅 03:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68064">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=TEpCMYxOnyaBLSoZsr8NwXG_Uakf0uFVSeqvTrivoc_yvN7a-AMAt2vzOBqpFGt6_xbKWsrnXuiHiBrtsqzYZo3xkP5GINmUGHfVsnk5BdYLqJ7LNsedWwsZUwRZtoNqhulrhegQpCw35Vwl1PHy10htvjSNgDhQnufQhpUN6tAhp9tVgILUn6J0LW80N-GZ1ppDutmhhO6aj20i2IxUF_a_RSAmKmihYJflXIVUD1xqNAE3cUISzZN0fUOymIKrNthlwvMBd5qPwpBZXZ2kIPgcyEUNMOToBP61VU0-ro7MdPEDnCnWrulG447AJ6Oe-4Bd_XiHWIpiSo2sexLn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=TEpCMYxOnyaBLSoZsr8NwXG_Uakf0uFVSeqvTrivoc_yvN7a-AMAt2vzOBqpFGt6_xbKWsrnXuiHiBrtsqzYZo3xkP5GINmUGHfVsnk5BdYLqJ7LNsedWwsZUwRZtoNqhulrhegQpCw35Vwl1PHy10htvjSNgDhQnufQhpUN6tAhp9tVgILUn6J0LW80N-GZ1ppDutmhhO6aj20i2IxUF_a_RSAmKmihYJflXIVUD1xqNAE3cUISzZN0fUOymIKrNthlwvMBd5qPwpBZXZ2kIPgcyEUNMOToBP61VU0-ro7MdPEDnCnWrulG447AJ6Oe-4Bd_XiHWIpiSo2sexLn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو ای از حمله امشب آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68064" target="_blank">📅 02:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68063">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=DVNiQPmRLG8W7z3eVUUbsR59skG-9IH44_mU010G_f3FjRK6EelKTtt5eg3mHOuztdcp-rmdddRUa8q69D0rA95yvZsiGr978oYaq3BoQIiAU1BtdlAgLZldj9bXJ_C5X8H3kY8rOa-ldW8Fp6vJHegJ9XoDnFOQy6VLY9-qvVJsxB4fBtqWlsoVS87bQnXfw32bXjSaYCO_hG3Moj0jCVuUyj79eAdyRszM8fcJ-NqB8ic1NEC6HyLPL9hDfw1V2W5ukHq3vG_sUrkBj3kInWpSXAvZIAo6XcbhUut1w09vujw3x4tt1qmIkhxSmvvN-CskL4YMHaz9YxFTFxdU1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=DVNiQPmRLG8W7z3eVUUbsR59skG-9IH44_mU010G_f3FjRK6EelKTtt5eg3mHOuztdcp-rmdddRUa8q69D0rA95yvZsiGr978oYaq3BoQIiAU1BtdlAgLZldj9bXJ_C5X8H3kY8rOa-ldW8Fp6vJHegJ9XoDnFOQy6VLY9-qvVJsxB4fBtqWlsoVS87bQnXfw32bXjSaYCO_hG3Moj0jCVuUyj79eAdyRszM8fcJ-NqB8ic1NEC6HyLPL9hDfw1V2W5ukHq3vG_sUrkBj3kInWpSXAvZIAo6XcbhUut1w09vujw3x4tt1qmIkhxSmvvN-CskL4YMHaz9YxFTFxdU1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار سراوان سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68063" target="_blank">📅 02:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68062">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
انفجار امیدیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68062" target="_blank">📅 02:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68061">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
حمله به سپاهِ سراوان در سیستان و بلوچستان
@News_hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68061" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68060">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=HVLqjkEg2TDHVzLfN6fDAYlV-3q7pnZqjkHCiGYeweHFgl7St8i3_vvvXHB1VRjGp8Gd7Iv76UKTLM5ptE2rPJ38rP2DWI4vPqJ6mMKk2Ti8fBUz5xCCrd5dOtgeemSEs8Sd-nowPWZgAIXbYw-6CMrGP4zsTC0Ve9p-QRpknvVFQkXq3dLW5KHtWDQp-3FpTAkukUojSqMKDJlxJcVAsrvBKD8IB1YfPZ22DNAy5r5XFbNWhFEdRuLDeJTjok4Cww4IVD98f8SEMRgpXnI2BSr3wvKVUE7gwZKXENJkfKVDVQa_1gG9uXviR1g4VtQ9PD9IwgCfXiKx_f5SX-kcVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=HVLqjkEg2TDHVzLfN6fDAYlV-3q7pnZqjkHCiGYeweHFgl7St8i3_vvvXHB1VRjGp8Gd7Iv76UKTLM5ptE2rPJ38rP2DWI4vPqJ6mMKk2Ti8fBUz5xCCrd5dOtgeemSEs8Sd-nowPWZgAIXbYw-6CMrGP4zsTC0Ve9p-QRpknvVFQkXq3dLW5KHtWDQp-3FpTAkukUojSqMKDJlxJcVAsrvBKD8IB1YfPZ22DNAy5r5XFbNWhFEdRuLDeJTjok4Cww4IVD98f8SEMRgpXnI2BSr3wvKVUE7gwZKXENJkfKVDVQa_1gG9uXviR1g4VtQ9PD9IwgCfXiKx_f5SX-kcVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوهای رسیده به ایران‌اینترنشنال نشان می‌دهد شناورهای تندروی کلاس «گلف» سپاه پاسداران در بامداد سه‌شنبه ۲۳ تیر پس از حمله آمریکا به مواضع جمهوری اسلامی در بندرگاه و دریابانی کیش، در آتش می‌سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68060" target="_blank">📅 02:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68059">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=gIf048lWTnjdMk3GiwQI0_vlZ92lh4YM9-6rPuvWuGZnFnHa9WBnYf25uAt9zYE8UPMVBu2ENtbg79Flcklsw3SxvCvE0wP36uLZ0W1Iy65VD7HtBeo8607fX_38jnh_owajCz6c22QieRO9AxT2FkW2fGSo7PLiotk_mwB4x5WhrvJiIfdnQOS3xtbWsqPVdEsAFtAjbv5KcrTZly0DAaeOLin3zuQ0XIny6gAGRcYEH7kIKOz6jt6o0afPIyMTAbORxOdkAP2EDDQ6N_e94kQ67JYJXdFFZ_bkcRD3WE7VqU2oHrFV9o9m7eN7zEfWimEo0Sr7gOGC-epFmCrjiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=gIf048lWTnjdMk3GiwQI0_vlZ92lh4YM9-6rPuvWuGZnFnHa9WBnYf25uAt9zYE8UPMVBu2ENtbg79Flcklsw3SxvCvE0wP36uLZ0W1Iy65VD7HtBeo8607fX_38jnh_owajCz6c22QieRO9AxT2FkW2fGSo7PLiotk_mwB4x5WhrvJiIfdnQOS3xtbWsqPVdEsAFtAjbv5KcrTZly0DAaeOLin3zuQ0XIny6gAGRcYEH7kIKOz6jt6o0afPIyMTAbORxOdkAP2EDDQ6N_e94kQ67JYJXdFFZ_bkcRD3WE7VqU2oHrFV9o9m7eN7zEfWimEo0Sr7gOGC-epFmCrjiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا فکر می‌کنید دستیابی به توافق با ایران همچنان ممکن است؟
🔴
املاکی هزار‌ پدر: بله، فکر می‌کنم توافق ممکن است
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68059" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68058">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
ترامپ:  سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68058" target="_blank">📅 02:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68057">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=jnkgRemSzGOR0GZo404kxFwwJCJA32F_lOEtsJ75UoGZ22Q-NUkIJPIGnVNOnyWEjzNXALi-1RZLDZpBrHlyJDDm-OfG-YoZ5mutaaLBdujeiTds4tEOmeyjcHcjK-6gbxYvcIi-eL1bmhsKzHlWbSyOvxAZxiZaHZWm6ln2ZtQgFitbRTqhx-e-d1vqw-1UM_gZhs-Msc2EvbxR06XHZ4miS4URFnfvT5ZaLeSU9ZFUtBeTkH-39MLTcmIMjkAL0elJhlKIWfMVb5P5YHrsols2kabM_bKI83dlmTqJ1Fhr-1RUaff6GmedngaQuprxO2kB0jOPDnOi6y7JKVpO5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=jnkgRemSzGOR0GZo404kxFwwJCJA32F_lOEtsJ75UoGZ22Q-NUkIJPIGnVNOnyWEjzNXALi-1RZLDZpBrHlyJDDm-OfG-YoZ5mutaaLBdujeiTds4tEOmeyjcHcjK-6gbxYvcIi-eL1bmhsKzHlWbSyOvxAZxiZaHZWm6ln2ZtQgFitbRTqhx-e-d1vqw-1UM_gZhs-Msc2EvbxR06XHZ4miS4URFnfvT5ZaLeSU9ZFUtBeTkH-39MLTcmIMjkAL0elJhlKIWfMVb5P5YHrsols2kabM_bKI83dlmTqJ1Fhr-1RUaff6GmedngaQuprxO2kB0jOPDnOi6y7JKVpO5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ:
سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68057" target="_blank">📅 02:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68056">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی:
دو نفتکش ملی به نام‌های "ممباسا" و "الباهیه" در آب‌های منطقه‌ای عمان، در بخش جنوبی تنگه هرمز، مورد هدف دو موشک ضدکشتی ایرانی قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68056" target="_blank">📅 02:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68055">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=vC1wLJNOxhjJuBwGMEgsNv0yavOYTPxNBV5O8XgCi_jWbiGIfmOpWTMqmIkdTtb5dw0VQ5rxqR77CH3rvJL3reKISFY3IN4eG4DtgKHQVUkk1y6RjIGj4VQljf9bPH_Lg9imElBZASUmYbbZMzvDEmlnAG0C9Y7u_2iOBcpocRnzatZWH_o5BgR2MITAs5tGbPRjwLl9ohtL7Nf5LxwaClPcHI3MUdiFgcR0iniinl3yCMhfM7NecFRi8tqIs0d4MxxsIzdLbHI9rA-2aOzqnXFBhtxwi69Oy55EDDF_cOqoxgsXaDig7RvSDv-VycX80LzSDJCMjmbC_w53lhlgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=vC1wLJNOxhjJuBwGMEgsNv0yavOYTPxNBV5O8XgCi_jWbiGIfmOpWTMqmIkdTtb5dw0VQ5rxqR77CH3rvJL3reKISFY3IN4eG4DtgKHQVUkk1y6RjIGj4VQljf9bPH_Lg9imElBZASUmYbbZMzvDEmlnAG0C9Y7u_2iOBcpocRnzatZWH_o5BgR2MITAs5tGbPRjwLl9ohtL7Nf5LxwaClPcHI3MUdiFgcR0iniinl3yCMhfM7NecFRi8tqIs0d4MxxsIzdLbHI9rA-2aOzqnXFBhtxwi69Oy55EDDF_cOqoxgsXaDig7RvSDv-VycX80LzSDJCMjmbC_w53lhlgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: محاصره دریایی فقط مختص ایران است.
🔴
خبرنگار:
آیا می‌خواهید هزینه‌تان جبران شود؟
🔴
ترامپ:
بله. چون ما از بخش بسیار ثروتمندی از جهان محافظت می‌کنیم. قرار است هزینه محافظت ما جبران شود.
🔴
خبرنگار:
توسط چه کسی؟
🔴
ترامپ:
توسط کشورهایی که از آنها محافظت می‌کنیم. عربستان سعودی، امارات متحده عربی، قطر، کویت، بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68055" target="_blank">📅 02:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68054">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
خبرنگار: ماه هاست که ایران را بمباران می کنید.
🔴
ترامپ: ما 19 سال در ویتنام بودیم. ما چهار ماهه اینجاییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68054" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68053">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=ow6uw2m0SIjfxrU48YGOkRseOwt58eS06ThF1RBofcpDl2MasSrO0WWNRisXhU8rmX0HXmuPVm8jMjVXg8xNmHPPAmSIcxAN4TKaOQgO_y_OPsFUK-i8H3xlXOeUXCy7Srj64TnyzSbSHYyOUh7_oBI8nzx964ErmDTvWgavLwGS55W0aPDH41RPZkUrIACsWstb54nK4_r4zIaFn8Sofu_eXJz6h5XIfhK86p1Ge5GelqXVneCc69si7_JPJW8I9WtWB_qwKMCTR5l6fjuznZWLe9PCUwMvOxxsixhiqKpFpIBLIvcdiN6Ov0dRygODV5YoS84PlDA8uFggIHAdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=ow6uw2m0SIjfxrU48YGOkRseOwt58eS06ThF1RBofcpDl2MasSrO0WWNRisXhU8rmX0HXmuPVm8jMjVXg8xNmHPPAmSIcxAN4TKaOQgO_y_OPsFUK-i8H3xlXOeUXCy7Srj64TnyzSbSHYyOUh7_oBI8nzx964ErmDTvWgavLwGS55W0aPDH41RPZkUrIACsWstb54nK4_r4zIaFn8Sofu_eXJz6h5XIfhK86p1Ge5GelqXVneCc69si7_JPJW8I9WtWB_qwKMCTR5l6fjuznZWLe9PCUwMvOxxsixhiqKpFpIBLIvcdiN6Ov0dRygODV5YoS84PlDA8uFggIHAdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آنها را در موقعیتی داریم که هیچ نظامی ندارند. هیچ کاری نمی توانند در مورد آن انجام دهند.
تنها چیزی که آنها دارند اخبار جعلی است زیرا آنها اخبار جعلی را دارند و ترجیح می دهند ما در جنگ شکست بخوریم تا اینکه در جنگ پیروز شویم، که واقعاً به نوعی خیانت است.
ما امشب یک حمله بسیار بزرگ دیگر انجام می دهیم. آنها می خواهند معامله کنند. ما دو روز پیش معامله ای انجام دادیم و آنها می خواهند معامله کنند.
آنها 47 سال است که مذاکره می کنند، اما هیچ کس هرگز آنها را مورد حمله نظامی قرار نداده است. ما خیلی سخت به آنها ضربه می زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68053" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68052">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=Y-wqnUx-Eu-3TEmHfpGz_UWB_7JRdZZRjKc7odYJwtItQXbdbqLjSIOg6bVAVIFIWFIn6oMXjZeFlXAfAetJwJbySDngV76YYzXYdcQlwI0f6JMVSTS_Hzmvjasr34uD_2c_omkfBFIx6O8bZQuat2aGeQLx9xcu4gZvOm91p788METMggzp_nnnVOZy0uM8ixvXlXQQq5oBXUBtrrFAKzj5-TZjwrmyA1xc1-Preup4MurZ_yZrq-otrIGe4k5gRY4aataDj65x-ERlF4jjo8B3F91mdokg_G369MlDqZ4U6LMPYpVWtTljbyXR1uCW5QZMlWY2DUiwpeHVFRSrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=Y-wqnUx-Eu-3TEmHfpGz_UWB_7JRdZZRjKc7odYJwtItQXbdbqLjSIOg6bVAVIFIWFIn6oMXjZeFlXAfAetJwJbySDngV76YYzXYdcQlwI0f6JMVSTS_Hzmvjasr34uD_2c_omkfBFIx6O8bZQuat2aGeQLx9xcu4gZvOm91p788METMggzp_nnnVOZy0uM8ixvXlXQQq5oBXUBtrrFAKzj5-TZjwrmyA1xc1-Preup4MurZ_yZrq-otrIGe4k5gRY4aataDj65x-ERlF4jjo8B3F91mdokg_G369MlDqZ4U6LMPYpVWtTljbyXR1uCW5QZMlWY2DUiwpeHVFRSrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چهار ماه پیش، این‌ها نیروی نظامی بسیار قدرتمندی داشتند؛ بی‌شک قوی‌ترین نیرو، احتمالاً در کل خاورمیانه. آن‌ها را «قلدر خاورمیانه» می‌نامیدند. اما حالا دیگر نیروی دریایی ندارند. ۱۵۹ فروند از کشتی‌هایشان به زیر آب رفته است. آن‌ها ۲۳۰ فروند هواپیما، یعنی هواپیمای تهاجمی، داشتند؛ که همگی از دست رفته‌اند. آن‌ها سیستم‌های راداری فوق‌العاده‌ای داشتند که همگی از بین رفته‌اند. پدافند هوایی بسیار قدرتمندی داشتند که آن هم از میان رفته است. متأسفانه، رهبری‌شان نیز از بین رفته است. رهبران رده‌اول و رده‌دوم همگی کشته شده‌اند. حتی برخی از رهبران رده‌سومشان ــ که کم‌وبیش با آن‌ها سروکار داریم ــ نیز از میان رفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68052" target="_blank">📅 01:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68051">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQaW3vTpG4Ah7xJh1EPCmh4NsRC8HJ3KWP2vNc_WBnsfjtjdNs6uuhWtiQiNlCN79cegvslzXaBuYsnUvq2f9Ba0pX_OBBoob3wiH_poT2lO2zdvkcA-Jq9Xv-i0MX62D29hmQ9HhaxwfEIQRJNXn89QE51SbM3TjOaXOYffVjXk1B_3O3YRdlenwbLuPtpolabHjCSM9jJBmA7ITqv9W7a7wfqfGAUWy3NgfDTeAFMDNdOplc7e9crXX7czuiYdz5rYRaEg39qy_7IW1HPjcdGBHqWsBWLke2N524rQGvyP-ZKeFYY1jPNDPDRjHj-7oDdlXYx-lEIYA9YS90B0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۴۰ مایل دریایی از منطقه قلهات در عمان هدف اصابت یک پرتابه قرار گرفته و این پرتابه به اتاق موتورخانه کشتی برخورد کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68051" target="_blank">📅 01:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68050">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=P2zpGDoj_Kt2DduUJbyMfLyrJKVHRQA9A8rUQOn25xj7V4n9iWZ22Y-a1CIhd0pxZinBhpCkn880O8EGaT-p5aAHFPT5PtJp8uePK0NFbaIE_ys6zWKjdoNbdPzGejnqY699r9_wcISs-Kb4W3PsXBfHHVJFo_gXXfgTlwVM-8Kj1LoPcIXIAd17ySwK-FsxNxF8quNgx6NbEU0QbTdrRDdYU37G83RZVCWFlutZYRhV55_iubd2GNvYWgvGYOQyns3rpe_1lSSthgCJlIqkHfmrVvsvnBceteYUOouq9yMvtulyGv0DuUxKfcA54evtBzyv36iQwr9H5Pt-YnCvSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=P2zpGDoj_Kt2DduUJbyMfLyrJKVHRQA9A8rUQOn25xj7V4n9iWZ22Y-a1CIhd0pxZinBhpCkn880O8EGaT-p5aAHFPT5PtJp8uePK0NFbaIE_ys6zWKjdoNbdPzGejnqY699r9_wcISs-Kb4W3PsXBfHHVJFo_gXXfgTlwVM-8Kj1LoPcIXIAd17ySwK-FsxNxF8quNgx6NbEU0QbTdrRDdYU37G83RZVCWFlutZYRhV55_iubd2GNvYWgvGYOQyns3rpe_1lSSthgCJlIqkHfmrVvsvnBceteYUOouq9yMvtulyGv0DuUxKfcA54evtBzyv36iQwr9H5Pt-YnCvSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
همان‌طور که می‌دانید، امشب ضربات سنگینی به آن‌ها وارد می‌کنیم.
ما حجم عظیمی از مهمات در اختیار داریم؛ موجودی ما در سطحی است که سال‌ها نظیر آن را نداشته‌ایم. ما ضربات بسیار سختی به آن‌ها می‌زنیم؛
این روند ادامه خواهد یافت و در نهایت خواهیم دید چه میشود.
ما در حال نابود کردن تمام توان تهاجمی آن‌ها و در کنترل گرفتن تنگه‌ها هستیم.
ما دوباره سیاست محاصره را اعمال می‌کنیم. شاید محاصره مؤثرتر از حملات مستقیم باشد، اما به گمانم ترکیبی از این دو روش است که واقعاً کارساز خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68050" target="_blank">📅 01:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68049">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=BgcYJ-qnxO49SkPeAgnUKvldamN749OD9oPE_b-bCSrA4OKQJE2fh09gF1J3MkiKmL0Gl_DzC39DtLcIKYbcjMVNE3MGt5G8WFA10G56eraau3ihWhOmtNv-uRq1r7MG2Jffo7GZCIVBA0f-2M0BcVb98uU1pm3eiPLeD1WoG_8TfUrL0dmuZwH1HKvVTjbzZjZoUDBjing_9ykKNrjokW37zojmpOigQDK-Du8s0Je_qhABm1N5Rzvycc6sAa0gxCguKVIybnaZqot467nSlw5ox9hY22ecmHvY7XcTZztZxOgt7NRI2WdhqhyuGOxvklkhjAbGAahz1qXv_47wAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=BgcYJ-qnxO49SkPeAgnUKvldamN749OD9oPE_b-bCSrA4OKQJE2fh09gF1J3MkiKmL0Gl_DzC39DtLcIKYbcjMVNE3MGt5G8WFA10G56eraau3ihWhOmtNv-uRq1r7MG2Jffo7GZCIVBA0f-2M0BcVb98uU1pm3eiPLeD1WoG_8TfUrL0dmuZwH1HKvVTjbzZjZoUDBjing_9ykKNrjokW37zojmpOigQDK-Du8s0Je_qhABm1N5Rzvycc6sAa0gxCguKVIybnaZqot467nSlw5ox9hY22ecmHvY7XcTZztZxOgt7NRI2WdhqhyuGOxvklkhjAbGAahz1qXv_47wAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ارتش آن‌ها را درهم کوبیده‌ایم. ضربات بسیار سختی به آن‌ها وارد می‌کنیم.
ما همین دیروز یا پریروز توافقی داشتیم. کار تمام شده بود، اما آن‌ها بلافاصله توافق را برهم زدند، چون متوجه شدند نکته‌ای در آن وجود دارد که باب میلشان نیست.
طرز فکر و رفتار آن‌ها متفاوت است و ما چنین چیزی را تحمل نخواهیم کرد. ما فقط به پیش می‌رویم.
ما امشب به آن‌ها حمله می‌کنیم. ما تمام توانمندی‌هایشان را در هر زمینه‌ای که به تنگه هرمز مربوط می‌شود، از بین می‌بریم.
گمان می‌کنم در نهایت، کنترل کامل آنجا را در دست خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68049" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68047">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VzAwJXzeB-HRbK2neEet0RDXririyhcCqf_tprPjDZBn49gpGbQrcZiC-eKKTO_NFFPp5CDObJ3PMJU1v2jbn4_W4WuC6Dh6Tuc_rC98Z82vWkbRGn0q2TliEHjL0LNKbI8MnrLmltjldl9d8tjEi7SMTM8anCtnuF8CKAIVuxlVoq30O_8WO5QeUkrhun5A_gE3_8GFTCmjlnbQa1kDU5ZjjhVcBL3rfepcFJUH5F5kXEtaGbf91P0oAvoYhKAeKy7vX8L7ZGP0_2UnQPLxwyuH94uG5MD7MCtYr1FyOPKoofyF_aLqs6jjzU-zenTA3ushJBHXeCCXyOjjyxwzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qZ0CrqINm6DY61renYf0jupfZTAaFi13riIeKVENdHxnJrcdQr9wWNAx81YGHmcWONo574801ItPm2MEqL_WJhairMjp8Ga_xHuhldgyEoiE-WBERAsF7Oelb6RqnHUBStFpMNGtpW6GiRY8wx6JxFCEuzTxyMATw8Dz7kKgHnCVYaOD8T93IJb43TYuN9nYqflKcz8YAPP2Tq7yiHpkkfpxs9tWhsTqTUpd2CEVVBU7EF3V_k8pB-dPEbDgCLVNtKI208LyR21dxjhKJGn53hjlCoQJxEpBOayQqUdi__0jLqO37sN-HqhEQ4WZQkn6YAXeQ5H96QWpAYWeBwS0Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویری دیگر از حملات آمریکا به جزیره کیش
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68047" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68046">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68046" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68045">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع چندین انفجار در  کیش
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68045" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68044">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN6i9_z2CYZQMxULJ9LF4xYAhnFoKqxIQUmSyqhQliQVqexYxaSKTnQTN98MMAnBlVXTDHbedxg1y8B-uW-IOnA-WLsluRMpH4uxVJNWkdVWdMHhtbnFyoRI6dF0BQxWNUDFtceEg3Fo8fF60Gfq10I5LAb74B_QD4ob5WO8GtfFbVeDy7Cq1H6wR67gc2B67t2xonEq3FrYP5IFmTTFSDqQVAUiq2DLkwswaVfa4tSyIg8s9EKL-qK2h_A3ysJblgYFN3XCouryx00QhsacWw-vmd7tXX_62DJLouUxGpEKuvd4OxlEhFxQdYMfzGPiMG8dKr1ewTvAjG22K9mnGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68044" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
