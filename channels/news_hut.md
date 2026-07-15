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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 10:05:15</div>
<hr>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=i3RTp0BtuWG-JnRzeXQcAfoanTiSaPlTgr4j2IogXlyB_YrK2XULdymb7JDJCbqkFWqPpBYu8l0TxnplwEQfZSzGg54JXfHm24qn_9i1tLkjm6zjUXXF_w5maaEgxu_m-39eRaIVejfh9wAryzdP5TPfHmhKS7UdSbeHEJz8S2_lselV8nD4aqU77WUzSb0S9b0T-J4tmp_lk05AmTHFVQdnr-eJbUCD6TXqOwvoxSrqujzaY_eblI9Hj2aDRa9oEH7CxMEu3TQyPmR4wSK94Eyss-TU0OFjbeY16WGUhAw4N4Hc1aqzfT_xoWp_De8lri7QdeNqHayEPeh4dyz9SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=i3RTp0BtuWG-JnRzeXQcAfoanTiSaPlTgr4j2IogXlyB_YrK2XULdymb7JDJCbqkFWqPpBYu8l0TxnplwEQfZSzGg54JXfHm24qn_9i1tLkjm6zjUXXF_w5maaEgxu_m-39eRaIVejfh9wAryzdP5TPfHmhKS7UdSbeHEJz8S2_lselV8nD4aqU77WUzSb0S9b0T-J4tmp_lk05AmTHFVQdnr-eJbUCD6TXqOwvoxSrqujzaY_eblI9Hj2aDRa9oEH7CxMEu3TQyPmR4wSK94Eyss-TU0OFjbeY16WGUhAw4N4Hc1aqzfT_xoWp_De8lri7QdeNqHayEPeh4dyz9SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XckDtsiGtTUQto-Rogrdam5DkJeUQRS4Xyti8ZIzOvrDACp9ZwfWmUeV7W_UQWnSUsBLAaMO0tKNdQLjA5l-oHMWD4SONSmUof95ctv7-ny1S5tOWSrdafj58oQjzP5z9UEyP_iVTFNg5Nvtvg3axsJ74ypXTnHNDYBfhM2PlunnJRDwwarJOti8Oyn1-FBBfTWMnaHuraGxaVtvIgn0HM92XSwUvEu780r7H9yHL8LSVqJyLQOHOQfVTMW-TutlSI2hjrQQ11JlIoHezYyPSXJLcNJcGG-FlzSnlm7glwIhKYuqv-0UF9RvXz5pfdzz4D-b0oaDWZnD-qzR9MkoSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=NCqFi2yV9S7g9eYE4-57nJRNXGhifJMhwWcXxiZSNDLOevu9Z9p-Nf2d6_oeYu1nsEpiARa9lc-oPU9iue6iAydbdVUJqMuPpt824wE_TPzmPGh4KATQVczxBXR6cpl8T5yLQyPW4uwcVHaKp2YmP3190BtjHKPIEwP7hsfr6aFl8yfGMe5P3cgqkN53ODTLKoFZYT_4LoW74kxtHrlM1edETmBKZLp1bKK6mKreeaIJAImvLCQpFw2JlCfiV517207qFrQvsjToB7JZWmhu00DzhZkaeBxRWMLmeszSSv8YD6l-ttKPCIWCTT9wLiC6LO-1vwM_8CiMAPdF2ZqLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=NCqFi2yV9S7g9eYE4-57nJRNXGhifJMhwWcXxiZSNDLOevu9Z9p-Nf2d6_oeYu1nsEpiARa9lc-oPU9iue6iAydbdVUJqMuPpt824wE_TPzmPGh4KATQVczxBXR6cpl8T5yLQyPW4uwcVHaKp2YmP3190BtjHKPIEwP7hsfr6aFl8yfGMe5P3cgqkN53ODTLKoFZYT_4LoW74kxtHrlM1edETmBKZLp1bKK6mKreeaIJAImvLCQpFw2JlCfiV517207qFrQvsjToB7JZWmhu00DzhZkaeBxRWMLmeszSSv8YD6l-ttKPCIWCTT9wLiC6LO-1vwM_8CiMAPdF2ZqLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68137">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68137" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68136">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68136" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68135">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68135" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68134">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
مجری فاکس : آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68134" target="_blank">📅 01:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68133">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68133" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68132">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68132" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68131">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
حملات به ایران ادامه خواهند داشت تا زمانی که من بگویم کافیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68131" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68130">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68130" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68129">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36032be115.mp4?token=vAKy4emQerhddhfUPlsuJtOnp5IV0ITYRK7ZUatEq6nkzXdYKV6ucSHCFEyBZkaCAAe-DOlt8bVyutEdOWn5aKyownKN5oglBmU-gvJ77X_LkEicT5J02uQY6Nz8WuFjKkiloG3DvnigvzkI8aeY_NG94WkDLa70RwiuHsFX6vN0yrKxLvaihY8Vq9mP14B6hQ8MPd_jUlR53NgztqZDBURfDqEoM2aAyAXagd7iJ8VC8fKt60hxjcSv5K-7mRsLnOLYMd5w4mLa_QPpcFXSSU4B-PbBwWSK71kUZ5qu7qyDQYEZGplMrB-ZdrcClN6nCTsP9WC1W_iLK2SXlAXskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36032be115.mp4?token=vAKy4emQerhddhfUPlsuJtOnp5IV0ITYRK7ZUatEq6nkzXdYKV6ucSHCFEyBZkaCAAe-DOlt8bVyutEdOWn5aKyownKN5oglBmU-gvJ77X_LkEicT5J02uQY6Nz8WuFjKkiloG3DvnigvzkI8aeY_NG94WkDLa70RwiuHsFX6vN0yrKxLvaihY8Vq9mP14B6hQ8MPd_jUlR53NgztqZDBURfDqEoM2aAyAXagd7iJ8VC8fKt60hxjcSv5K-7mRsLnOLYMd5w4mLa_QPpcFXSSU4B-PbBwWSK71kUZ5qu7qyDQYEZGplMrB-ZdrcClN6nCTsP9WC1W_iLK2SXlAXskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا جنگ با ایران از سر گرفته شده است؟
⏺
ترامپ:
خب، گمان می‌کنم بتوانید هر طور که می‌خواهید آن را تعریف کنید، اما قطعاً ما داریم ضربات بسیار سختی به آن‌ها وارد می‌کنیم. آن‌ها باید ضربه بخورند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68129" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68128">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=fN36U7P5S7rilTXZoVS4qslTuFbrHhsl3zoqCHoGhnGhq-YZi9yo5zTrazF4oAcB0-EEcMCqncAfPmtnJVjbWjkw5295pdUhrZeUZ93KE4pD3SUhbMrwaoQj4pExthfV8f7cD0dC4wSNY4gsjM7J9BE0ex7V05rICyXscGeCqCMr--s_4Bp4mx8IViLLhp6ihJJjnSdDGfa5vk-MT9-ZE8XADc4lzPloQPqwNpk4zCuGHaZyMPkAB20a-fZifXAuSJd27qwmbdT_5lfHOUCxLoiRlX3zVfUdqi_qkEYCK8YuiM_rzoN-orBoWIOoAHXvjK1Q5C0J996Lbeq_sPXIOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=fN36U7P5S7rilTXZoVS4qslTuFbrHhsl3zoqCHoGhnGhq-YZi9yo5zTrazF4oAcB0-EEcMCqncAfPmtnJVjbWjkw5295pdUhrZeUZ93KE4pD3SUhbMrwaoQj4pExthfV8f7cD0dC4wSNY4gsjM7J9BE0ex7V05rICyXscGeCqCMr--s_4Bp4mx8IViLLhp6ihJJjnSdDGfa5vk-MT9-ZE8XADc4lzPloQPqwNpk4zCuGHaZyMPkAB20a-fZifXAuSJd27qwmbdT_5lfHOUCxLoiRlX3zVfUdqi_qkEYCK8YuiM_rzoN-orBoWIOoAHXvjK1Q5C0J996Lbeq_sPXIOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‏ارتش جمهوری اسلامی:
در مرحله هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف ۱۸ و سایت نگهداری تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68128" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68127">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68127" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68126">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
بندرعباس و سیریک بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68126" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68125">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=YaXGdzfo3mgNSzyPaSSlhtmpcz-h4SRvroH8x6UlctLi7gFxIaZRzKYzYH_te81RzMINC0drG66H6vJNaf6CNuc38TzrSDHV_6ABv2vlKfxpgFaOz0nzBuYoGVEycAr5siGACxsOmKmwbjuc4M1nyIzD14SBqBTjHB6-GWPYkj3KyljD1lLqWIn_eMWBtNAqU8qfXqExVX_YHWemJsnZK5YycWCnUNhmygXW4xFD9JW_zSeKLIIbDYnv2EE0xl-edVfZWNUZDYWLxILeERR6liaDLPf3LgMXet4ClNmGvWrNuH7Wa2gq1bvn3qvJnqvQtucV6EERv1szkgEWWRkucw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=YaXGdzfo3mgNSzyPaSSlhtmpcz-h4SRvroH8x6UlctLi7gFxIaZRzKYzYH_te81RzMINC0drG66H6vJNaf6CNuc38TzrSDHV_6ABv2vlKfxpgFaOz0nzBuYoGVEycAr5siGACxsOmKmwbjuc4M1nyIzD14SBqBTjHB6-GWPYkj3KyljD1lLqWIn_eMWBtNAqU8qfXqExVX_YHWemJsnZK5YycWCnUNhmygXW4xFD9JW_zSeKLIIbDYnv2EE0xl-edVfZWNUZDYWLxILeERR6liaDLPf3LgMXet4ClNmGvWrNuH7Wa2gq1bvn3qvJnqvQtucV6EERv1szkgEWWRkucw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
هم‌اکنون دارلین گراهام نوردون، خواهر لیندسی گراهام، در حال ادای سوگند برای گرفتن جای برادرش به عنوان سناتور کارولینای جنوبی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68125" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68124">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68124" target="_blank">📅 00:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68123">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
انفجار چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68123" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68122">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBiDhTe8fIeu8-V5GaUYw2KnldOwqYLsgUogaBiJEblsyIysvLokHEzm9lf07hNQJw6A_mtQzSYiIJtVEHa214FAO-PEWnZDDUDXmV40lj1veJm_2FoVsmj85c_X9Int2Cw_eZoahLAamGNsB79XvdqID1sgElsHjrARD3ZI7a9RzQc-_-neuNN-G_ng0XqGf_GapPU2mEkNDcBSORKpCskLlVKw5vcqHKj9R589iXzcBzy9sjoDbcFQ9Hj_B6UEOMpFdgu0yGzQC8TjZmVgj_x0Pch2WWLamlc02NsgGETwhB9GLg17XkHU6kRSRD8eJUfvQ3zE4pp1liDbSEEANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68122" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68121">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=Fj17xl2jBc7Db7KudE0X9g4l0wa2MnEH0i6EkyP8PdtSHhL6zNRK6UWFjvbINBoWafVfVwNvMclPZBjWUbKoJirLUj-Fmqx-dd5L-OzBCSwWUGDGug5QsH6nWqXAAs0TzO_cBcf9m3olfejQ-QU2sO4DN6nsx_-OK6-kuQXjG9ugrKtPbN4VwPYa-4O8QJjbjqdkPNZO9vGmc-rCeRIYAJ2qod5RBHqjNbAUxbJH1bfy_ynb3bYHrLyPzM3_aNqXrp9N-KQ-J0FXQQouNYZNj__JLEuoIbz3lHSmOtpBaq2OEoPlRx3cJHdqYqNaG_zmbd1qlKN8Hxq3S_b1lUUJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=Fj17xl2jBc7Db7KudE0X9g4l0wa2MnEH0i6EkyP8PdtSHhL6zNRK6UWFjvbINBoWafVfVwNvMclPZBjWUbKoJirLUj-Fmqx-dd5L-OzBCSwWUGDGug5QsH6nWqXAAs0TzO_cBcf9m3olfejQ-QU2sO4DN6nsx_-OK6-kuQXjG9ugrKtPbN4VwPYa-4O8QJjbjqdkPNZO9vGmc-rCeRIYAJ2qod5RBHqjNbAUxbJH1bfy_ynb3bYHrLyPzM3_aNqXrp9N-KQ-J0FXQQouNYZNj__JLEuoIbz3lHSmOtpBaq2OEoPlRx3cJHdqYqNaG_zmbd1qlKN8Hxq3S_b1lUUJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران تنها جاییه که بتمن هم به گا میره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68121" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjgaoN5NZxb__9uwiS6F8yAdcwBWT1V5matoIEKhjqF5exTIMNYSPy_cqugoOlKbixCm-_7ZSGLVoa9MjpdWtXDByZtOLagTLCfp5ddjLaVWpznRE31BwayJ9PCarjliLhtlW9M6KtiFVKpISlglG0NQv9Jvfa0FbaWmMmxp8Qagezwb873kltU9IBgarAb-Dis5wJKpkfSEALZLPWeSUcWKH4wQploc8BsQUqtwkQAcBBzXQkuVcsfYM3ASmFoG6QqznQ8DhuZ1JMG2LMZQlRIpROmLVWRD7YmfVLeOgE_GSpqPCqpQ-kyGWg_io5cs_ejxYfc8PFi5Rz36d5Rn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfN3V79ErlFZJlNmSPxvAagbh6ElpvUrVfaO_HLs2VL9BkMA2E5hyo0cNYPENkVsmZEDpK_JbPCGaBO0tmP-tOGQ0coVtxQZSo_HJL1RxH97e9a57gVhh1bQn1qvnVYj7a3jz7-SgIkHxGTEVIu6Ignt3N8nFH7zhDzWPXSunrFtfjGdkA2dubeG1nBAlQWApGOdrKqWYjj2UJ1mpb1XWQmCkTWiyjZ1lhytmSzakwj_EN3Nu4OE8-l3fxLmV5NTxpC-JAUWQUTMBKVRN83imaOBZPBveV2J9XT2beHmnN29lBPWq8j2NPqDaTGNzawmV-QhS6H2o5JgMUL-PIZPRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNR1r6SykprDH-2QOBBdh5ij5BWL-H7y0AYEtMpZg5V6uuFX5FNNp2gE0YvVYKY51BsxWQtpbOm6oOJda8f7sImfiSVwa0y6Nc9WQrcfS69um1anfStP7xvcEwM2l3vVQVlcseWdaHU7hvrG_eDEJM-OeigMYFjVQlBG_xz3g8gxhgWNygQ9XUhuWfP3yunwOtlx0TWlR2iSIgbKsbMjXRkjaYSVGfbTMxpJnKg3dvRxzdGtPbK20LMAPhJYHewwbSYKUBccT-wiea4JvTS_Wl9yq8bD4P8PFD59kah7wqdXnUqjASfEox_g-1xM9VU3gkTpd_01WihYVr_UHVmEXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68109" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68108" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HheP1e6rZQSZv27PbeerkefdeDqCBlvzNIVkA6jv4mN5wUMv4URBtwCEmTLad0YDtbdFQd_UnbcpZyzgI-YONIFvDWMzTIPayLZUGm1WMfoYlPQ_wAbVdhkXXD9R8Olv0g4MEGwW9hGU07Wh5_hiT6Rdj1qmoqnnBMVTwVl4PpKk0-B1HK12nyrYX2KZ9kDoGBen9Um-dcf8XCbQbdaKqMAcJIR8o9HCHVIGPwmZ2w-m-e1PY7xhPYecjM8REAB8zSHDpGEr2GWEgof0LV6g5pSlKqas7IILzt4bJUXnEN7RuLX0YV34eYkH87D6sGNzHgRLIFNVoqcayslpBwVb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAKnYv3lVG1YuC1vsV14JHLiKq4l4p7bYl9hw_5tj4V88_FbFkHLzmDXZ5xT98P37l5vFH_7Qv0vgo2vN3PXB-_6KGBdV_4RWeqKt8oFqBe2Z7EFPrCEHgqAfBpnfm-QLvvGSt_1lPRYSm3cE8MMHpYd_WQg1KMb7gUQiuiMEzNRGsiEHueQxwF0ESSBLDgzmD2dVsVR008qO3x31jVR7gS1Qrvj2fiEuYPEEshpAfRGnX_EEk2hFJ8d24cxUjSqZxpPfSf2LVeUqI-U14VEcU2gKY3RnDklWI70Z8r11s3royOyRUapRt4K1Xk-ZUGA1WOI-FSo8g-HDVWXlsV9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhQp5vJhHCQ09DRL6C0DOPxx77udTC8Vtpvdo9taj13-xHUznQi5x0n9tzF1on8VAnRaxgtvBTeR8HIXLzQbwRHfM2EBQMib_SRhXhnaqwixMR7SEg7KsZSBeEfjX6RoNgv4BBv-bI9b94Nvv2oGaQk7RqG0_fbAVihdkTilLIk5xwTp1bcRGUe9gzEMDMn0Cx89OKCOvT2ObjeaNuz60tIjXwsKu5Ae65zWuIfXtg26aArxrUT5s_k0pC6z_0D_FtEPY0-hDY6gaY1Y7w1HE3qtA9Cx5X9sATpnV3QxwIPrrvUv6q4laPIp5kKOczWk7h_sMILtVxlWJNCiTNL1xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXv4mrfMfTQDc59oJit_G4rkeZ1PpwLdJbk5P4lsGq0roblAhp3WSFE0RULEnhDhj6oG7UhxZKcSj9_MplNZMH5J9fstdUOgq-DnQ0kyCwUMmwU8NBIwzxWav5keMuhdclIGP_ewQCoYIi4jEJvaYOeb5NZQS8xLHqwAf-zc7Onv4tAgHp1RA3FX3zMNW2a23uWeHrII0gZmNwySR66emuli7s5bD6veQg6jFcBKXL32Ic7m3hpSyYgNJql7l8YznGXKtviDv4DjUok4E8uaQIva7tfAVlhOrBrmMv_0x-U5xKdj2h0lMqNelFYriH8vD4wIki_bo_-ka3z3L8A8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4gmgmsJ2_c8oIlinc346IwLTIzoqd6C0_m200T4gZHpaobW6um_Ds_UjoOnqxW1yC6zBtRCy3iaW78Qaf2F24UqMdWciVxvYYui0BuwRKSTq_tNdZH8w9VquQkGyCzLLKAOvC0kW9O1p64RHbFwll9W7Fk4JSA29Sna4OrxtPpaSMwQsg4bmdPt6419t5rl_x2ZxCnOuyhMCduWkwd5McnKXqMrLQV1--er2n721D6EibMzPrHaeutW1Q7ns3BRdPrj8OIBIgC2f3e0lx-ngPPk6RahedXo9TvFg0Byjr8C_9Zchxka1cqNXASn00GK_ldcXplnvW1RaFQIr-LgjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=Ih2HSnWGp2UW6DdA3HD9alwy159SD0CmzemCiHjFv3GCywqiRJ6edfbmnBA-kyDzGzzhdZjuPBg2h11jzU4BVB4yduKELrsd5R39AXNHxTZn1i7Ns6mxY_ySdLFJzC9-TrfGpx1_SnjPCYEvF_ui8dgtacwhL-vpcQQieMBcxQEVXAqz_sO0UVFwOgTw1gdgoixJ8-5jpNqt3zVe_RiVjwFisiGgRes6yfWQk9r4N6ygw_y_-6W7mRwYR_ECtNb-_U9yXQvmdBmgtQAVa81B4Wutd5fvR-CMs5ZyKAWK90I_pkP4teHkl2_NBOu1Qx5F26nXXX5cOmngQtaLNa-6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=Ih2HSnWGp2UW6DdA3HD9alwy159SD0CmzemCiHjFv3GCywqiRJ6edfbmnBA-kyDzGzzhdZjuPBg2h11jzU4BVB4yduKELrsd5R39AXNHxTZn1i7Ns6mxY_ySdLFJzC9-TrfGpx1_SnjPCYEvF_ui8dgtacwhL-vpcQQieMBcxQEVXAqz_sO0UVFwOgTw1gdgoixJ8-5jpNqt3zVe_RiVjwFisiGgRes6yfWQk9r4N6ygw_y_-6W7mRwYR_ECtNb-_U9yXQvmdBmgtQAVa81B4Wutd5fvR-CMs5ZyKAWK90I_pkP4teHkl2_NBOu1Qx5F26nXXX5cOmngQtaLNa-6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=KpoVNxap8U316xrlKR4-7Solccm-ZRtsLVHxtdgVOnhG97JdQomQneVkSRZD7j94ETtb6sO33Ewq2_SKUvEwaRGFzoKxBol2bR0_Amd6X5bY4Ylk0waT4kbmEbd48rjF6olwYpgki6dk5YP7LQ7W8UUxEBLIayYPblTLTOUwksQKOmOhVC8u_L8-WVexGzoZxvJdIpylvsPxihI_GtSUave3j5M1mmWnuKQUG45biUTyONu2ZCmXTvMNj8zsz3qtr6OgzdDRv1LpRQ3rgxurBeCzoyjYu2ibrJJXAa9hQvrtV9SBN7JIv9ScxZWLokGdO8B_Rhr8jodDv-iuzxmAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=KpoVNxap8U316xrlKR4-7Solccm-ZRtsLVHxtdgVOnhG97JdQomQneVkSRZD7j94ETtb6sO33Ewq2_SKUvEwaRGFzoKxBol2bR0_Amd6X5bY4Ylk0waT4kbmEbd48rjF6olwYpgki6dk5YP7LQ7W8UUxEBLIayYPblTLTOUwksQKOmOhVC8u_L8-WVexGzoZxvJdIpylvsPxihI_GtSUave3j5M1mmWnuKQUG45biUTyONu2ZCmXTvMNj8zsz3qtr6OgzdDRv1LpRQ3rgxurBeCzoyjYu2ibrJJXAa9hQvrtV9SBN7JIv9ScxZWLokGdO8B_Rhr8jodDv-iuzxmAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سر دادن شعار مرگ بر سازشگر در مصلی تهران
صداوسیما هم چندین بار صدا رو قطع کرد
🤣
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=NYCgLtVFhja37yP-QBkXptCy3JEqhRxrRkSI9nFyNOs6QMab0BUa1RNg4S2nag9nBr6Qo2OOI2x4bAKFoWJ4fQiW5bqwypKE8M7JFrosBgiwkeHzXwSVVxcqMtHTHIKFfKawK0zN8C1Ekn1pk8lWpb3QLU_KYeCwhHov06uOXboAyQ-rHEQOlQGeXWONVzsVgse-o8t-aE-AL0tykJKXPvJVYQdKynrvNtvXv_Z8lB0e66PTTGk9Dg5c0CB0CVaroFPWgPsDr2QKradSXyQLXVrv6zASDQfNfDjto1cDU8prptFmLtZ02654qbnAKoxmT1P_SaAl1QfTmg_53DMZ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=NYCgLtVFhja37yP-QBkXptCy3JEqhRxrRkSI9nFyNOs6QMab0BUa1RNg4S2nag9nBr6Qo2OOI2x4bAKFoWJ4fQiW5bqwypKE8M7JFrosBgiwkeHzXwSVVxcqMtHTHIKFfKawK0zN8C1Ekn1pk8lWpb3QLU_KYeCwhHov06uOXboAyQ-rHEQOlQGeXWONVzsVgse-o8t-aE-AL0tykJKXPvJVYQdKynrvNtvXv_Z8lB0e66PTTGk9Dg5c0CB0CVaroFPWgPsDr2QKradSXyQLXVrv6zASDQfNfDjto1cDU8prptFmLtZ02654qbnAKoxmT1P_SaAl1QfTmg_53DMZ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=URbM3xBsc-YUh4TfHSDecDSxdBDcDt7qb7XXZ6VBZwf5TY8yFkJw0XMcEKy-bCR2ddBqTjdK0A8Dp73YsGyjZSxGUqCDs-J6P24TgsjtVfnWorsrhK7--1viGzRHo7mZCVJ5bsmerdSb7uCY1idwB2o29p1XJLwEWXY5pCOMeKZz7s694uTkrubKFTwXQuEL8hg1NoyErnbUOgs3LvmJShImS9UfHdmkwGz9OptSdRUa2-7xZ5iRlathGJKRY79P8Ulp1vKwCF415QPenOUPBlsKNKuHEkxDz_INV7eU6Luk3aKMsBL8Yc6CRhk9-Q74BSNz3CHayQUUie636MQGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=URbM3xBsc-YUh4TfHSDecDSxdBDcDt7qb7XXZ6VBZwf5TY8yFkJw0XMcEKy-bCR2ddBqTjdK0A8Dp73YsGyjZSxGUqCDs-J6P24TgsjtVfnWorsrhK7--1viGzRHo7mZCVJ5bsmerdSb7uCY1idwB2o29p1XJLwEWXY5pCOMeKZz7s694uTkrubKFTwXQuEL8hg1NoyErnbUOgs3LvmJShImS9UfHdmkwGz9OptSdRUa2-7xZ5iRlathGJKRY79P8Ulp1vKwCF415QPenOUPBlsKNKuHEkxDz_INV7eU6Luk3aKMsBL8Yc6CRhk9-Q74BSNz3CHayQUUie636MQGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره لغو عوارض گرفتن از تنگه هرمز
:
«آنها (کشورهای عربی)گفتند: "ما ترجیح می‌دهیم سرمایه‌گذاری کنیم تا عوارض پرداخت کنیم." و من این را دوست دارم چون هیچ‌کس نباید بتواند برای تنگه عوارض دریافت کند.
«در مقابل این سرمایه‌گذاری، کشورهای حوزه خلیج‌فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری خواهند کرد. این در واقع خیلی بهتر است!»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO3NtkgIUevh76BMZWDR3oiblBpp800PQSTfKGFuxvHR4QL2GaEUeM9zr5wxQVJ66iCVMgxR7xBwWCYcHmB_nb1X7phb8gd8PN9cWhejfI_yB-ht6m9tYrDY5sRi6TpyBafy_GjOXC5tpUtZQGATpKy8PFGK6hjWUKxYwbs3eMsOeeQfbBRWMHS_PR7p_ACH1tVq_rKZZWnWoXz_HcPfoZWO2CWA17zQufqVUDxn8x8wdI93o9tMUlV24dp6GOBPknaQti2PbqW_gObgSzl6TPtIueK9nfCWHT0jiAaSSq9uRcXvUSuP0mp9mGheg8ITBEtY0yRYl4KcM0lcOnf0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agos1ustdTfcmRQHzFGiJxvISlYCgCMCY0smzEqU41X5w82s54NJpBwpYo_B-ksJn29GRwT0UxGwlChXy8nOq7PEy96gxSu74DWKz-NnE_sMS6ey0ozNwDKHj3oOESFvSmwiyjML66DlNb4pVUjx8pdRzcHal8wNcAFFtTX5lzbue4vq8DE3FGdumEa4sEpsd-CUSpqfU4IG98-X_MEjnh74rXeb7DS6jl91GG3C7km9JPlkiD6Rt2tiD_Vvl2lBp1IVTlvjfL5coUvIUTNNGt6Mb107CGo8bDVY9FUWD-dc-8VgJWrZN1KkDT953a0aoj0L0h7vNNIyu4CT0b9BSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68088">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=V1Ko2bWgs8kNKNiw1elNEhVnN_KlYCcKOXVxPQIf4QRZ39UTjUKmzmAS6IbCQMuBKF04pA_H7CufP4bnwzjhAdeo0yzAl6UWINGP38M6mMxb621QUhb4ek7QWzaINez4ar8laNX3OjkhoBT4YHjMO-Z4qmLd_MwxfxD1Pi24M0jV_fwuEJGEjzbWdlvLUio3lXOa7krOO_0GkVAv6xoS8xXz1DK-bv13-MuaM-_8WVF6ZlraLCGbcKVnA70kY6KXQVD8Enz83n_p0FsEjKgaRtPxlnFJ3R8aIu9laooBO6UKFWI4y94p5fWDrIQ81RL4WO_TET6efErorZd-J2fc2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=V1Ko2bWgs8kNKNiw1elNEhVnN_KlYCcKOXVxPQIf4QRZ39UTjUKmzmAS6IbCQMuBKF04pA_H7CufP4bnwzjhAdeo0yzAl6UWINGP38M6mMxb621QUhb4ek7QWzaINez4ar8laNX3OjkhoBT4YHjMO-Z4qmLd_MwxfxD1Pi24M0jV_fwuEJGEjzbWdlvLUio3lXOa7krOO_0GkVAv6xoS8xXz1DK-bv13-MuaM-_8WVF6ZlraLCGbcKVnA70kY6KXQVD8Enz83n_p0FsEjKgaRtPxlnFJ3R8aIu9laooBO6UKFWI4y94p5fWDrIQ81RL4WO_TET6efErorZd-J2fc2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نظر مراد ویسی در پاسخ به مخاطبی که گفت باید حرم امام‌رضا هدف باشد:
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68088" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=QT3RahQOHUJAnzQdXM6Ccca8jKjVmjOrvl04jBvme3Cuo73lSWt3c6YDE3QSU-26ABMyr3SlRuah554jb9dbR-rSogmyvPkdANkj77VNVf1H2N5eFfOM-ZWOTY5ABQhWxC2OUXsBm9oBeHylcrH9Hs-Lp7TGEU-i8Ferko5OnvjoGTAICZymzFnnvnh053sVc78Cky6Cu-K24WLmWHbTCsAO5yV9SXM1AYuUMe9RkWn6EDoZN7Yf9QZ2VO2NBkbjXzLi4pBvWarJt_CV6UUt9m6CjlTk8jtE7JFJJcrz6OFwSH25o-zkfMTO1dFQuR4L0tLdWtAg03qVnVwzhtXIW6Sa42yj7iA576CigUUqFbheY1QU-ucHkK1xlynz7c9KI0LwKO1sf3aBiLzpR1ZWROgjwtjfIhCLQFt04QhmZS4mLy2sPERmBba4s6R9-iC7zkE0UhF7ONo__f-lOxkwhdXhzywA23c6mdRVDFbjYdQ4eA2qDXxu-1siqGYHuxbwB-k4QtlmZ0-puuG_yDoT0v0Fa0MHyT4Ii_pUNj-XNsRH7faisOwI20HJfL-mV4dR63tAXu8bGdwzbq4jlKU4VoNgIZpI_Cm32ytVgV0Zl_sgzOd3Ijs7zajGTu1HV_jFkQxd0KqwiAxxfe55MtsUzFUt2b4YIYNMgd9TXkNnFkc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=QT3RahQOHUJAnzQdXM6Ccca8jKjVmjOrvl04jBvme3Cuo73lSWt3c6YDE3QSU-26ABMyr3SlRuah554jb9dbR-rSogmyvPkdANkj77VNVf1H2N5eFfOM-ZWOTY5ABQhWxC2OUXsBm9oBeHylcrH9Hs-Lp7TGEU-i8Ferko5OnvjoGTAICZymzFnnvnh053sVc78Cky6Cu-K24WLmWHbTCsAO5yV9SXM1AYuUMe9RkWn6EDoZN7Yf9QZ2VO2NBkbjXzLi4pBvWarJt_CV6UUt9m6CjlTk8jtE7JFJJcrz6OFwSH25o-zkfMTO1dFQuR4L0tLdWtAg03qVnVwzhtXIW6Sa42yj7iA576CigUUqFbheY1QU-ucHkK1xlynz7c9KI0LwKO1sf3aBiLzpR1ZWROgjwtjfIhCLQFt04QhmZS4mLy2sPERmBba4s6R9-iC7zkE0UhF7ONo__f-lOxkwhdXhzywA23c6mdRVDFbjYdQ4eA2qDXxu-1siqGYHuxbwB-k4QtlmZ0-puuG_yDoT0v0Fa0MHyT4Ii_pUNj-XNsRH7faisOwI20HJfL-mV4dR63tAXu8bGdwzbq4jlKU4VoNgIZpI_Cm32ytVgV0Zl_sgzOd3Ijs7zajGTu1HV_jFkQxd0KqwiAxxfe55MtsUzFUt2b4YIYNMgd9TXkNnFkc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مستند "عمامه صورتی" که در سال ۱۴۰۲ تولید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=tevLMBibpcc7Kecn5B6HM5y9RQ0t9dtXj7_qVz7lsJHfHTPItK2dz0IVcHjMRWGU0v0jgQ8M8GM8Itp1wo95WS3MI78_ISj8YqCGsmBCQsBFQ6X3qj6IUt7AnUUwboXDcfOmPihdmqwe6W4YuR9HDuoLmZ7PlQELb2bJDL8VB3gD54Uhjp6QAMlBRRWUjWDmtAoF9mPnXALQSprLETpdt5ruyDsogpbvSUU5qXxrpk16-BW2RrFhQAxNo3IJk8gAV8Mb5AePsUIl-cSPXZVvASC3_NdRtb_KLdGRINtw-m2E2ThN3T_PtAQxOZHS9NdSl9EU8P73cabl-9GpqHIKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=tevLMBibpcc7Kecn5B6HM5y9RQ0t9dtXj7_qVz7lsJHfHTPItK2dz0IVcHjMRWGU0v0jgQ8M8GM8Itp1wo95WS3MI78_ISj8YqCGsmBCQsBFQ6X3qj6IUt7AnUUwboXDcfOmPihdmqwe6W4YuR9HDuoLmZ7PlQELb2bJDL8VB3gD54Uhjp6QAMlBRRWUjWDmtAoF9mPnXALQSprLETpdt5ruyDsogpbvSUU5qXxrpk16-BW2RrFhQAxNo3IJk8gAV8Mb5AePsUIl-cSPXZVvASC3_NdRtb_KLdGRINtw-m2E2ThN3T_PtAQxOZHS9NdSl9EU8P73cabl-9GpqHIKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام ویدیو ای از حملات به ایران در طول شب منتشر کرد.
در اواسط ویدیو نشان میدهد که لانچرها در فضای باز هدف قرار میگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLxl1sZcRZo_tHPocuWKh9uBbKNpYEoME_3_hw591NSNx6VLsbJXkYV1s_pl1AdFbH7Q2-rSdY0Ooy-R6l9mcaLL8RVzvRl6dqUodeHRTE-qy27CLtznCJu4OI_IS4fvA0kagSsAWh1Yu9suPV6Ne-sfJd6chaRtf22ZluX6shRniz_hBNhJFU1SquK5A7EtKENJrcwgxK1RWfh6vF_KltUAaBd3B7HBSTnKYABrt_Jmz6pJD1pDDstcJisX8MoACBthMYYdYoORftCOprr-zHTXvT9KY3epGr_AU6J4HrkJRS_v4OLpOrwgrB4YgyFCHc8S0Ljddggtvf2bLrQSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULYvhq8Y2bTgXCWRl8J9BAce6nnVmYSnyWClYogkzfe237fNHGN6HIQ7_7sfzBxW2lfiHyLabiPKP_V2DWr34a-I_AVnQuPrAoOOsjzTUQRtddgaD6_L53L9j7QJggiHOa1hgPR3a7HEZzQXrOwemlYA9l2UTL4ILkk-eZ420yEhvHaEVVEB8Pyw3YbmCoAssYfWeuijDufNGy2ffQxk5mUJ6zJpkTsOfknPYisgmUrZS16P1eL9bK24v_lIfTOrWNh_jWlpTKYrM1LkKjzvEFOxDXSPWS4soDCuTBgIXNbGaI6Zb66reMJk5W-Q-RfhyWBv-7GsCjK0dIUaJSH2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=ek_HDOGnljm8-YcJIJpzM9Kid4lI1JXIWwlybvi3kCGAPp3Qzqn2qPJYiwhpLDQUqOkGHM1SM7v7RrNaJ9RxkjzYlpLtgY8-6S80idg22lwUXeoc0GD2mMNxdTReqEjBplN6FWovtALI_5mPnBM3GMIgRZaawvFpflHZ9-7gWaPtT-NpieY_VZVUTdUhKw-wXTU6RigTCwqpN_zohn8EpwP75FiV5WdF60drke_PwnijCQRD9mGGl82-uNs0D-WMVi1VGy1nf_jG15zHZLBAvZKQp0SGiZIJv6ezCaAG6mgyFfxB4_RSn1ibTjbifcgh8FuzoG1f__p-bklC1gEk9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=ek_HDOGnljm8-YcJIJpzM9Kid4lI1JXIWwlybvi3kCGAPp3Qzqn2qPJYiwhpLDQUqOkGHM1SM7v7RrNaJ9RxkjzYlpLtgY8-6S80idg22lwUXeoc0GD2mMNxdTReqEjBplN6FWovtALI_5mPnBM3GMIgRZaawvFpflHZ9-7gWaPtT-NpieY_VZVUTdUhKw-wXTU6RigTCwqpN_zohn8EpwP75FiV5WdF60drke_PwnijCQRD9mGGl82-uNs0D-WMVi1VGy1nf_jG15zHZLBAvZKQp0SGiZIJv6ezCaAG6mgyFfxB4_RSn1ibTjbifcgh8FuzoG1f__p-bklC1gEk9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7uUHiyOCy4lzbemJi2GkuJRjUxW1vQ5fodX9uPivQApYgQCurOX4wEcWFIu_l2n1IaSV6JMfVVfTIiZ1AIYCMMC2CubnCn0pHDZt8LmnoYodLdCI2yuSCiIOgLMNS3ft7HdCSxnH2oQK1Kg6Pl0a1wYqJVyEbkgOTBy9jMTq5jT2FYeWQfatpSOxobvXJF9PPCRQv2QG84QjI-Gk90KRbuIwWDg2g5jMQNuHH7m14pjIxSBfhIoRn3vp2AnV9Ro0z7WMrIybsUbbWbPtUoc44HQenzIWYgHLHkiePOHRhhe3ND7L78KsXUeUyYt-zQeCF8EWPHjXs29wzcYaHzmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_4K2hiQitqqr4eYF-kMVNlQtI-odagHKpy3UJUAksG0mjalapf0RIQuOSnTXorKeCLVI9q16U6398xX5C7gLiciz1TZJHM3-8eQfexM3QF6d_LEKOkSsynB6G3s2TAfZLj0IYWZij0f-OCSdibVe73pHAsyJtO0QWO6a42QkXAdAX3DcSdTOY4LHruDhN3DQ_5liH7harPKl92jsQCNysi9vfgwXgN1CTb43Z5R25eTuovSS1NuRTrhQPC_9mOGr543FkG7oSYH3vVbE-cct1UikQZDFn_DffN7TEqLz90iBARKRCDYQTJatnovTf-RGiuOrMrAJxQRp6-5nncwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=k_KWyPPL-jfbuwOtjqWHv42Qnipn0ln3p864fM1xf_IpmlLZkWymrSHcIZNSYWDfkU-9p0HoH_sv4VR--_2iMjBj8TfeJyRTI8qP58ZEvl7Bkpj5r2wQlPHWTUqu0ur9_dRgcxW-GSmKM3eu3WdFRXsTQ8npWCGjMYdOIOmSQF-lZcMG3v8kmcdd8AFOThO0FZvG_uDM-4RjlCO3x158vplW4jIDgMLIxjMZek2gNI95XL8oeNxhLCtRQ67l42nutMemdPeYz687MEU8rI2qqPbopLR4fG6EsXkmgLn1wZcfTbnVE-RHDM6Uv3n-LETnUAYVSNJKTdw12xMuXR9YeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=k_KWyPPL-jfbuwOtjqWHv42Qnipn0ln3p864fM1xf_IpmlLZkWymrSHcIZNSYWDfkU-9p0HoH_sv4VR--_2iMjBj8TfeJyRTI8qP58ZEvl7Bkpj5r2wQlPHWTUqu0ur9_dRgcxW-GSmKM3eu3WdFRXsTQ8npWCGjMYdOIOmSQF-lZcMG3v8kmcdd8AFOThO0FZvG_uDM-4RjlCO3x158vplW4jIDgMLIxjMZek2gNI95XL8oeNxhLCtRQ67l42nutMemdPeYz687MEU8rI2qqPbopLR4fG6EsXkmgLn1wZcfTbnVE-RHDM6Uv3n-LETnUAYVSNJKTdw12xMuXR9YeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=p0YkIqVeVjlCKgUy03omlN69UyXyNUzaAFln3APCH0O8udW-RKsq52WVnHXdEzJEjhmLInyiT_ExmezjyyAwHQrLc4jW66rajzQzouaDiznmuWR_oIzOxlap97OrHxsODsWCv0P6eLCXAaKmePgYbo4Ar6VZxC6GYVY-2Msl7ugWBUxHbQCq9lDqHIEzbYEfCwf0nnVKGhthsrRVpc2eSIh4pm4Da7JahxPpLYIgeR4tSnalTKq_LUyFpl2JQfHWpB90VufT9MU_urOWYlI_yoNN_vVdHu4B-lR5gmnsXtyd3aWJR9Ta7gXD82x86XUqSkExOOoM3C5YoFvIhyoQ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=p0YkIqVeVjlCKgUy03omlN69UyXyNUzaAFln3APCH0O8udW-RKsq52WVnHXdEzJEjhmLInyiT_ExmezjyyAwHQrLc4jW66rajzQzouaDiznmuWR_oIzOxlap97OrHxsODsWCv0P6eLCXAaKmePgYbo4Ar6VZxC6GYVY-2Msl7ugWBUxHbQCq9lDqHIEzbYEfCwf0nnVKGhthsrRVpc2eSIh4pm4Da7JahxPpLYIgeR4tSnalTKq_LUyFpl2JQfHWpB90VufT9MU_urOWYlI_yoNN_vVdHu4B-lR5gmnsXtyd3aWJR9Ta7gXD82x86XUqSkExOOoM3C5YoFvIhyoQ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_1D37AbBDzQMSLa8LlomPXqQYSO8_UmJOb2j68HUUlUs6Wki0UUZOdpbfSx7rv1HsJQ7ojzIIWtbVEb1_rGwSEbdbjQN-GW1bBzJiLPsEkZhB_ZuzXtTOme5ehPRquDmHIjDU_m7_n8kjQy46UP8_FW10D_9pZbFhkWYQKa28xXKqwS1bjo0x8etd6LXETTSblCsneYJ9pB2QzYbe4FrQ6lwvWz_4h2bfwkrYrhxqvXInk1rKB6hBGEuEkVlLA5O9KsmpZXUDgOwd-qyYk9vQ2buGXmKKEi3HOatB2KZkQpI2axTA2VtRaCrNSkgTf5Z06A0Zebc4XNVDv8YNAWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=MZbU7XLUr0wtrHVs54wwjG-t-_zfe8HsRLQMgMXOhaCn1ADP5arDuBCYfjA1i_Y9D1x0D9KgxwtO8h7SPX-jMQ62-pJNPIO7qN7-mbxbmlI2wtaLT8UVoDDupNe31wvYZF8j1om8TrVGN6C94GXsqNVLEiKU2il7K_T1o2d2DgdWnI6C0vqMrTq7NL76nv7uHQy01rff3ok_HhakyuyA4ihi2RH56BAyn-ZvYmzdDeDSPrf1K1IV1iyPVuv3JtKk4aK6Xlm34R7kriOeqP91IvrxFZa5n6Z4y1HX7mEz-wQLg9ZSM8idyHLxFzSdXiNqwHnKGHjZ0hXgLzCip8ImLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=MZbU7XLUr0wtrHVs54wwjG-t-_zfe8HsRLQMgMXOhaCn1ADP5arDuBCYfjA1i_Y9D1x0D9KgxwtO8h7SPX-jMQ62-pJNPIO7qN7-mbxbmlI2wtaLT8UVoDDupNe31wvYZF8j1om8TrVGN6C94GXsqNVLEiKU2il7K_T1o2d2DgdWnI6C0vqMrTq7NL76nv7uHQy01rff3ok_HhakyuyA4ihi2RH56BAyn-ZvYmzdDeDSPrf1K1IV1iyPVuv3JtKk4aK6Xlm34R7kriOeqP91IvrxFZa5n6Z4y1HX7mEz-wQLg9ZSM8idyHLxFzSdXiNqwHnKGHjZ0hXgLzCip8ImLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی،تحلیلگر ارشد اینترنشنال:
چشم انداز موجود تشدید جنگه،پاکستانم دیگه نمیتونه بین ایران و آمریکا میانجیگری کنه.
جنگ سوم بین دو کشور تو روزای آینده شروع میشه.
اگه اسرائیلم وارد بشه یه لایه دیگه از سران جمهوری اسلامی رو حذف میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TctvdNJlBbYnPbP1sPomUsdqjmq99jRAkANgPlYpcGZAkpdFxSELFKMYImtXoxKGYxOCXBRWIm7sRq81BQeBUtP_SZbuftq-kJ5nOGMtLdRfzu2ILzFUpbS15MJWp71m9xJrs6DvPJbdNDF3eXuiyCiuEl6asPRPvQkaNksbufBrv9raRJQGLhz3TD7OnwOGf2jPSQqHbaN-IqD_8wVTKbybP3imWETCIYeYlSrP-kVUhspCiPaJpEh2q2cMnwtgXVnAUTJncaUPoIaFqRtpVUi85FoBsCyTPbPvCSFmCR-vz2PT7ro-Jd6_Ngp7xNmRDCniOX6zMFwXY-OpFxH9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) آخرین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب (به وقت شرقی) روز ۱۳ ژوئیه به پایان رساند.
در جریان این عملیات پنج‌ساعته، نیروهای آمریکایی با هدف تضعیف بیشتر توانایی ایران در حمله به کشتی‌های تجاری، با موفقیت به اهداف نظامی در نقاط مختلف ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند.
نیروهای سنتکام برای هدف قرار دادن سامانه‌های پدافند ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران، از مهمات دقیق‌زن استفاده کردند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند.
نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار باقی مانده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68068" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=HG3P10hldCRV80e0UHe4jX-yPORJfeK0KeabkNBYMIWEkXxyeOwECvR79PTPIjgV8FxGks3SCtRUhYbuXlTgeo3ReMxi0x95BEPcgm9tU_LENWR_L7nGZp3a2evI_ZlLaBjkH41TyEHKtJ4uVdqwMj4rb3iUhp7Kwi-sVbN9qwv5c2tvgJIFx6iDGyKhQdZQMgVNZ866J0EypSAP4nYn4Pas0UPaOIwkRktxCdAJ_vVxiVjbDxbEcbYIdrwxGKYqasROBRK7754Ls6ld2HXqcTlAcVs7ComGM1vUicbumL85yGg2x7yeC-3KDslUrV3ogNA1W0tC6UXskGTcFYKYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=HG3P10hldCRV80e0UHe4jX-yPORJfeK0KeabkNBYMIWEkXxyeOwECvR79PTPIjgV8FxGks3SCtRUhYbuXlTgeo3ReMxi0x95BEPcgm9tU_LENWR_L7nGZp3a2evI_ZlLaBjkH41TyEHKtJ4uVdqwMj4rb3iUhp7Kwi-sVbN9qwv5c2tvgJIFx6iDGyKhQdZQMgVNZ866J0EypSAP4nYn4Pas0UPaOIwkRktxCdAJ_vVxiVjbDxbEcbYIdrwxGKYqasROBRK7754Ls6ld2HXqcTlAcVs7ComGM1vUicbumL85yGg2x7yeC-3KDslUrV3ogNA1W0tC6UXskGTcFYKYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخطار پلمب، مانکنت نامتعارفه !!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzsQ3Itm1_XzmRtHKcKPa0SpscSigLkDyjbEwcNdGK_KFFvFHO5ysrGHZT6BKooysK6lO0lE5LiIs5lJNQ9f-Gneqb-gsa-tGa5hS7EG-p4SdShkyz64OmzXE64-xLksqhgPYsGx2nqPllOUfetPiOmpa4kLd3MnsV8wIxvQXFvgC8vnoYhIjGFlWz9FZzxgDuP6-AJ8XC9Phh1dIVbcTDij0GowMKZyBARMdAwBa1Aqd8YwWRMVxmkSBe9mCElXbszS_HZeVUmh-4zpyrPZHeMUw_X8ovbqUJ5PIp5IRCy2cFq-jVThI9Iif38ow7RShK-SKnJk63fbZw_QiTfrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:
اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد.
در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای خارجی، از جمله در مجارستان، با احمدی‌نژاد دیدارهای محرمانه‌ای برگزار کردند و از رویدادهای دانشگاهی به‌عنوان پوشش این ملاقات‌ها استفاده کردند.
این طرح در جریان جنگ ایران و اسرائیل در سال ۲۰۲۶ به اوج خود رسید؛ زمانی که مأموران موساد پس از حمله هوایی اسرائیل به محل اقامت احمدی‌نژاد در تهران، او را از آنجا خارج کرده و به یک خانه امن در داخل ایران منتقل کردند. این اقدام بخشی از یک عملیات گسترده‌تر برای تغییر حکومت بود.
این عملیات در نهایت ناکام ماند، زیرا احمدی‌نژاد تحت شرایطی نامشخص خانه امن را ترک کرد.
به گفته مقام‌های ایرانی، او اکنون پس از آنکه مقامات از تماس‌های ادعایی‌اش با اسرائیل مطلع شدند، در حصر خانگی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68066" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afjrPQh5KlU2SfBJONGNu9ZPnCzd7vWxOAyagJprmE_ispdjmDV8cYkyhPP5y9MsP-req8l2YKzYbAd26Re6HMkiOp1GmRfcbGQwWoMB6O_VDugCRhEjTHi5CjOLZJ48XbJmarIRt2gHe2wt5rLXoOsCfDs9FsQszYj8MsTLENP4DFAUQpvurIRuvFoT2-a7pTIOgfd5Q9KHA9ydFOwmDbMykD41xX8QhCfIPt2t_elQiOPtIDYV4d3FP5wTMsE8dFO3xp3IQGSoef2uX1rsBPCEwxJD3LtEmVKk5XjxM3vw9aNIBnyscbhgtNv0hHVwWh9xc-Y4PclhPIx865ChEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=V8V91TI8Y2S10qxiQSs0e1WYtebuMjscC0qSxNmmfB-fPxWH-x7QGiFxzoCQ2gzhpLi7sWmTep9sXJZ1PYzSR2e40j3OEXE3Jr4k0VywWyOnI2cVK665vAc058YA8P-T_awvWC0wW7EJnms57XZScIN08h8h0Vn-E0aUEJBTJUwKB2eJcsVL_yEjZPDgxZ02CbLn1fDa4UWAmiFmd32jm8S_2SwQSv59v1leNGtoBEdCSKNKeW5AArxUZ7eyLjbUFOJVuI7rNUaSVrYulobOyQeeK4zWem2e8EjUSiQlEDhoXWDcB_n3YidICICPmP3LC65ea9vX0aehpYp5HGG0Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=V8V91TI8Y2S10qxiQSs0e1WYtebuMjscC0qSxNmmfB-fPxWH-x7QGiFxzoCQ2gzhpLi7sWmTep9sXJZ1PYzSR2e40j3OEXE3Jr4k0VywWyOnI2cVK665vAc058YA8P-T_awvWC0wW7EJnms57XZScIN08h8h0Vn-E0aUEJBTJUwKB2eJcsVL_yEjZPDgxZ02CbLn1fDa4UWAmiFmd32jm8S_2SwQSv59v1leNGtoBEdCSKNKeW5AArxUZ7eyLjbUFOJVuI7rNUaSVrYulobOyQeeK4zWem2e8EjUSiQlEDhoXWDcB_n3YidICICPmP3LC65ea9vX0aehpYp5HGG0Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو ای از حمله امشب آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68064" target="_blank">📅 02:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=Xo5wL_U1mOLmvbiVwCakeyhiuEkB2qOrGJGLVLXVDD_o5rdNUnTXzBtXGw6IrHyoZOhUlbXGpp0lHHJ3oJpFXIhV6tzmAoNIK2P4aheSSGDmnukHVSzo4AVXBRuKJVhfsR1jtcI_nB64ntrIsVcLBJuQrJpqxnyng4R_Em3EceHUp7LE4WAY2muy_kAUOVGt0lc6qqXAYRlqm5eAxntLCzom5LDRyVUPFGodeMqs8LWMh0_6ECshldIc8Kj4_oMw1Yyv3kBn-fS2pJN-kyfADQ_mnQbIx-i9yZ5cxi3RI6V8I0xtMpgMJ7PtzRaKjEgnuLV9R4zlvXSn87Kp7QadAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=Xo5wL_U1mOLmvbiVwCakeyhiuEkB2qOrGJGLVLXVDD_o5rdNUnTXzBtXGw6IrHyoZOhUlbXGpp0lHHJ3oJpFXIhV6tzmAoNIK2P4aheSSGDmnukHVSzo4AVXBRuKJVhfsR1jtcI_nB64ntrIsVcLBJuQrJpqxnyng4R_Em3EceHUp7LE4WAY2muy_kAUOVGt0lc6qqXAYRlqm5eAxntLCzom5LDRyVUPFGodeMqs8LWMh0_6ECshldIc8Kj4_oMw1Yyv3kBn-fS2pJN-kyfADQ_mnQbIx-i9yZ5cxi3RI6V8I0xtMpgMJ7PtzRaKjEgnuLV9R4zlvXSn87Kp7QadAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار سراوان سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68063" target="_blank">📅 02:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
انفجار امیدیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68062" target="_blank">📅 02:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
حمله به سپاهِ سراوان در سیستان و بلوچستان
@News_hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68061" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=EnOwlcOGEyz_a_vpCxsQodx7s22QNQbJUFckbTtPctzwNu9bbHIzgevzgr3c6xgjtMX6LsVGgL25u6E1-Xs2AB86A_UPT_cY8-qNPZXlbs9uSO0PMYa0MHl9Jqlcg6757YRUDLVlexo7okZN-cQ0gcXakebub0qlwNL0RjpAkH9t8kfXXzdnLqy96ar2GqFWijwF3ZOqOeWVIo014N-5sTp2tAZKZ2QkC7WsfserRwQ2I8TDTI-_tMZpZjjWPEKKbfABFyOmpQJth3GmvJAjrBCLohq5l5B_cs9PTcXep7b46UMAL0yZCHvYVW-MFC8Ocs-CUkeSyzZdP64jVZiv_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=EnOwlcOGEyz_a_vpCxsQodx7s22QNQbJUFckbTtPctzwNu9bbHIzgevzgr3c6xgjtMX6LsVGgL25u6E1-Xs2AB86A_UPT_cY8-qNPZXlbs9uSO0PMYa0MHl9Jqlcg6757YRUDLVlexo7okZN-cQ0gcXakebub0qlwNL0RjpAkH9t8kfXXzdnLqy96ar2GqFWijwF3ZOqOeWVIo014N-5sTp2tAZKZ2QkC7WsfserRwQ2I8TDTI-_tMZpZjjWPEKKbfABFyOmpQJth3GmvJAjrBCLohq5l5B_cs9PTcXep7b46UMAL0yZCHvYVW-MFC8Ocs-CUkeSyzZdP64jVZiv_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوهای رسیده به ایران‌اینترنشنال نشان می‌دهد شناورهای تندروی کلاس «گلف» سپاه پاسداران در بامداد سه‌شنبه ۲۳ تیر پس از حمله آمریکا به مواضع جمهوری اسلامی در بندرگاه و دریابانی کیش، در آتش می‌سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68060" target="_blank">📅 02:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=C5PMfs6zlDXfx9MyaK8_46rdIKi3HXvW7_2z3QbDIGYUf648OXWrcxmmTeIP018Arb_xsZg1d_QOSuCF9IlKeyC4TYsHawfl2GIY144IlXXemBrGgtwfhJxtvTA6Plj32ljhrtrecOc_jZKBPQcHDoL6o4TjqOlER4xnXsYYKeDhlkPZsmWNhVQ0jSQcfHU1YiXSCFw0doatMDSC-DRsZbu2x_fFExaNKP5qr0LKqUY8EttqAc2icSvvvH24pLIkyTEfWJNJXSJVuY1rk039stBVztUtm8HKfJrwGNJ0HA_iuBX2sMg3MLkKO903KdJwA71xb6dxMTIQEsPeGicA2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=C5PMfs6zlDXfx9MyaK8_46rdIKi3HXvW7_2z3QbDIGYUf648OXWrcxmmTeIP018Arb_xsZg1d_QOSuCF9IlKeyC4TYsHawfl2GIY144IlXXemBrGgtwfhJxtvTA6Plj32ljhrtrecOc_jZKBPQcHDoL6o4TjqOlER4xnXsYYKeDhlkPZsmWNhVQ0jSQcfHU1YiXSCFw0doatMDSC-DRsZbu2x_fFExaNKP5qr0LKqUY8EttqAc2icSvvvH24pLIkyTEfWJNJXSJVuY1rk039stBVztUtm8HKfJrwGNJ0HA_iuBX2sMg3MLkKO903KdJwA71xb6dxMTIQEsPeGicA2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا فکر می‌کنید دستیابی به توافق با ایران همچنان ممکن است؟
🔴
املاکی هزار‌ پدر: بله، فکر می‌کنم توافق ممکن است
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68059" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
ترامپ:  سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68058" target="_blank">📅 02:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=vI8dxgm7JntAKdknJcX9R5Hz-ry1JTog26AGwtULaht04t8RZpDlgEFyexykfG4V4YQCNRXJsybcD2w-7oJFl110FO-BXM3DiJYPQNK_omQSLXpFrY-C5moWi_4RWPlX4vF5nLnvSJsun92t2t0QzXcwug3B44KjB7rvrP9lZi_OMACtwQWtZq4mH2Lz9HTPaKjKCU2rCdCaQLkmW6uQ_p_iX5ppeVyQllefJHLoxDLLRRNxaKStHEllpvPjXgtYZ_IMTBIlggfE56ojz_ESCayoHNqqLrc8vdfgq8L2Clw8Z6B7cOM0MtmxIcMugKn7GrkB5LRovswgFCHfk5mzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=vI8dxgm7JntAKdknJcX9R5Hz-ry1JTog26AGwtULaht04t8RZpDlgEFyexykfG4V4YQCNRXJsybcD2w-7oJFl110FO-BXM3DiJYPQNK_omQSLXpFrY-C5moWi_4RWPlX4vF5nLnvSJsun92t2t0QzXcwug3B44KjB7rvrP9lZi_OMACtwQWtZq4mH2Lz9HTPaKjKCU2rCdCaQLkmW6uQ_p_iX5ppeVyQllefJHLoxDLLRRNxaKStHEllpvPjXgtYZ_IMTBIlggfE56ojz_ESCayoHNqqLrc8vdfgq8L2Clw8Z6B7cOM0MtmxIcMugKn7GrkB5LRovswgFCHfk5mzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ:
سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68057" target="_blank">📅 02:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی:
دو نفتکش ملی به نام‌های "ممباسا" و "الباهیه" در آب‌های منطقه‌ای عمان، در بخش جنوبی تنگه هرمز، مورد هدف دو موشک ضدکشتی ایرانی قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68056" target="_blank">📅 02:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=BlSqZ97pT-MMIUfINKhGkp-fkzsbfbTk4rbNt90lqThctuVxKQhxMflu09yxwX8OF1Z8NJEaVYEl-6zrUiHw-qAKax7OC0PaAo-ea9x1Bbyzg0Agm29cHg9dTNjZh1H8lN1VTYbuRvUL8r9giJGk2pY3cvqYJCAPTzYaQ-h94p8_5peEkFDfeJcnJGUw8TWpi0w8EdBB9EXLMDVniqGnHMwHWjGZ5F7M2XoadDy_g1w_WoyTOLxMZ_XHB-eUFWFH8LogjuN5KEoezJ3Cf7eUXmawsEPUOXPSkBcj2r6loERnA6zcDO6Uq0_qpTWIdl7J4B9ctKrbUMVqcw0EGKlAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=BlSqZ97pT-MMIUfINKhGkp-fkzsbfbTk4rbNt90lqThctuVxKQhxMflu09yxwX8OF1Z8NJEaVYEl-6zrUiHw-qAKax7OC0PaAo-ea9x1Bbyzg0Agm29cHg9dTNjZh1H8lN1VTYbuRvUL8r9giJGk2pY3cvqYJCAPTzYaQ-h94p8_5peEkFDfeJcnJGUw8TWpi0w8EdBB9EXLMDVniqGnHMwHWjGZ5F7M2XoadDy_g1w_WoyTOLxMZ_XHB-eUFWFH8LogjuN5KEoezJ3Cf7eUXmawsEPUOXPSkBcj2r6loERnA6zcDO6Uq0_qpTWIdl7J4B9ctKrbUMVqcw0EGKlAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
خبرنگار: ماه هاست که ایران را بمباران می کنید.
🔴
ترامپ: ما 19 سال در ویتنام بودیم. ما چهار ماهه اینجاییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68054" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=hkNTqHZgiCNnpbNYMQzU4kPme4Kk3gb4vnSMKivbA9qP2yBfJIEqq3LdjYC-Vb1OO3mZhGOSIpnXJ_-H6Rqw0DpA4dsqrMTFdQqeWKP4nSQaQ6470H4ILZjuxVrxtDxtJA3WH2B5fEFQwipiefV1I6Jnbkia9W8aOaSwfv3bcEAFCiOsJ_R9zDg6lge9JtJQDenyY4q9zTZr0I_ubOCTZp0lFP8U1JZClUSNS32uCLxuaB0G-dEVEVgGgqwrytrMbq3ISs24l96InazAZpiVxyzFWcAlxCTYYq__H0Ny-LsXBu7LdI2phBW9aWR4FNyLUSM2NNzTu0QWEEt2bI9jLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=hkNTqHZgiCNnpbNYMQzU4kPme4Kk3gb4vnSMKivbA9qP2yBfJIEqq3LdjYC-Vb1OO3mZhGOSIpnXJ_-H6Rqw0DpA4dsqrMTFdQqeWKP4nSQaQ6470H4ILZjuxVrxtDxtJA3WH2B5fEFQwipiefV1I6Jnbkia9W8aOaSwfv3bcEAFCiOsJ_R9zDg6lge9JtJQDenyY4q9zTZr0I_ubOCTZp0lFP8U1JZClUSNS32uCLxuaB0G-dEVEVgGgqwrytrMbq3ISs24l96InazAZpiVxyzFWcAlxCTYYq__H0Ny-LsXBu7LdI2phBW9aWR4FNyLUSM2NNzTu0QWEEt2bI9jLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آنها را در موقعیتی داریم که هیچ نظامی ندارند. هیچ کاری نمی توانند در مورد آن انجام دهند.
تنها چیزی که آنها دارند اخبار جعلی است زیرا آنها اخبار جعلی را دارند و ترجیح می دهند ما در جنگ شکست بخوریم تا اینکه در جنگ پیروز شویم، که واقعاً به نوعی خیانت است.
ما امشب یک حمله بسیار بزرگ دیگر انجام می دهیم. آنها می خواهند معامله کنند. ما دو روز پیش معامله ای انجام دادیم و آنها می خواهند معامله کنند.
آنها 47 سال است که مذاکره می کنند، اما هیچ کس هرگز آنها را مورد حمله نظامی قرار نداده است. ما خیلی سخت به آنها ضربه می زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68053" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=Wwm5VI5naHduQ6SsxZH8_mE6E9xi17DZ3CNFAfoKNAE_GyYbsx5jTK3GHe1GXcEi_k2SezY-rNf8IBaVF9R_eD7SmuuyCimifgKvJP9DpMuqU8J7apPeFcBdTlALELKRnqmoWcbPOTYhOFU21wgrbZJFQDSxjMytIqdlsRSY0gxFDXGrdDs1RXA3LJuVDWreySfLgPukVYoR_EwcSAobgWXoCJWnikMFx2i2WWdWNzOYKJUvhgZuin3CS7Ud5h2u5jyW-RgC58mg0RJOEel-VB_jW6lUCGaB9KCo0NdiQLigNuLhWEyxRdfuBTzoB_v9_4yQO1rMZGZbjJTFFLGdSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=Wwm5VI5naHduQ6SsxZH8_mE6E9xi17DZ3CNFAfoKNAE_GyYbsx5jTK3GHe1GXcEi_k2SezY-rNf8IBaVF9R_eD7SmuuyCimifgKvJP9DpMuqU8J7apPeFcBdTlALELKRnqmoWcbPOTYhOFU21wgrbZJFQDSxjMytIqdlsRSY0gxFDXGrdDs1RXA3LJuVDWreySfLgPukVYoR_EwcSAobgWXoCJWnikMFx2i2WWdWNzOYKJUvhgZuin3CS7Ud5h2u5jyW-RgC58mg0RJOEel-VB_jW6lUCGaB9KCo0NdiQLigNuLhWEyxRdfuBTzoB_v9_4yQO1rMZGZbjJTFFLGdSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ2Wd7cij38yg_zkr7Zf7BXfm_8cs7hbMYRvLqGvNNmh4VMLp1Ko2jUPUL7CUWxba_DrAvETpPuglkS4PHb1M1MiCSRuVs00aZS4EcY10ejcf-t0fQOHB3S6OuNL41AFN0qsAH5PkCcMC1Rxb5xflmNvQqCNp_sZ1x8HoAZUdpNWXGZ9NuUoA6fDwNgi0CPnf_BMobWBmIs0RktKRXetJhyts7SfYmTbH0-L9ybgKvE6BqARHx6JCNGfj_TYMelxCYuwwfSU2lqcRR6Dxyc8FIGs1FNsW6j_1iPJSXV8saNtZbbt4CEVRQ2cHTYClY4McobLmyBCxMTRzYN6t2usTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۴۰ مایل دریایی از منطقه قلهات در عمان هدف اصابت یک پرتابه قرار گرفته و این پرتابه به اتاق موتورخانه کشتی برخورد کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68051" target="_blank">📅 01:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=CptfIuAm2naOUE7V_t9jxr-VXVctiNu48hwmxIRxUQbv3P0khgGhxw9q-WS40Dc8cWD0Nxu_KoNvDPthaMmuonDoz8y-9a0ibgY_BVBlBU_PW4OkCffG6705cDYVZnbv8EOw4ELtxRkagcwF2np4hoNuYVNLWbxKwPV02izYFPf8DBlXHtM3zQAvxIG1Kr_ETt-tT6p-NbsjxpfEJfD1082R9C_qtes5OM5Yv3N2Qj9btuVCfvtFe_Z2yaVqAj7RbfgOzzT2IhAaHH-EoiW6dPIglVFSIA0TOgNRnOp-XZCQEsL6ksSxRB1JQwJCVW_4uBAEbqIm3aw_u5xvEVLSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=CptfIuAm2naOUE7V_t9jxr-VXVctiNu48hwmxIRxUQbv3P0khgGhxw9q-WS40Dc8cWD0Nxu_KoNvDPthaMmuonDoz8y-9a0ibgY_BVBlBU_PW4OkCffG6705cDYVZnbv8EOw4ELtxRkagcwF2np4hoNuYVNLWbxKwPV02izYFPf8DBlXHtM3zQAvxIG1Kr_ETt-tT6p-NbsjxpfEJfD1082R9C_qtes5OM5Yv3N2Qj9btuVCfvtFe_Z2yaVqAj7RbfgOzzT2IhAaHH-EoiW6dPIglVFSIA0TOgNRnOp-XZCQEsL6ksSxRB1JQwJCVW_4uBAEbqIm3aw_u5xvEVLSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68050" target="_blank">📅 01:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=tFtgVeJQp68Ddqs9SjHU9c8Np1TtCIUFg65u5hKelpUrlidDvsgRhLZG05HvUISF6BfyxcTBzp3rf-d6s1A69p65RXC84MCObesyRA0xfoQVndoYQPXTBFlvVolC6iWYoWmQb0HcV2JW8Aaclo4yStmDDjug51IXI2caOwOBWme0T22OVgneI-4Yi1WquyXd8ufuA8nWblt0bAiy0YayYvq5ern3D4_HiDLqTP9RtfmPoMokIXXZEQ_UjXvM3vS4MPsWpwqGGfpK0AVRB05-uPvhIpvqeWlfU73cwtejLm8C6GYo1Sjx_Ci67faEIgIJN-hHmnvdmNpCqwdaX5oX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=tFtgVeJQp68Ddqs9SjHU9c8Np1TtCIUFg65u5hKelpUrlidDvsgRhLZG05HvUISF6BfyxcTBzp3rf-d6s1A69p65RXC84MCObesyRA0xfoQVndoYQPXTBFlvVolC6iWYoWmQb0HcV2JW8Aaclo4yStmDDjug51IXI2caOwOBWme0T22OVgneI-4Yi1WquyXd8ufuA8nWblt0bAiy0YayYvq5ern3D4_HiDLqTP9RtfmPoMokIXXZEQ_UjXvM3vS4MPsWpwqGGfpK0AVRB05-uPvhIpvqeWlfU73cwtejLm8C6GYo1Sjx_Ci67faEIgIJN-hHmnvdmNpCqwdaX5oX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68049" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68047">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mBNrtkbpZx3hHmXseVun90QLfxeadFyflPOFCB6rykPEZtePhiuctcyE3eZQXTi-dc8EpPOh-MvwYFzFwhpNWF-alx8IjiSbnc_-chVSHGts23Mxme8cHomGo3BBhGsUO0YamTF76B6OIgLlpi4FuXBsIQQ7iP3W74Ze_jQd2pEJ3opXA06ZMNjvuDiO9LQ3yieyJMMBPjzMZTw_smV4mWVgVUxd_k5dcnj6x2GC-lGTjINHg6qOdkkZEvEXRdA_D6Hr_-4GXEmOGl4k95GGq9vF99xrUNOh21USktfgmiYhmQkD2AIINC0qZCE8cQ6WUL_bUAgZ6xW-dzIxPuwcgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K8vhCNTWIWIq6XMCC-yVLib5F46UoF6BJFZiaT8T3TAbOKEZbsrQZ6_A6zTNfnzPtH0lm-laxajZOpYvsC-O41Xw8tnULkykBzykdYs0L_380tOCmTt-K1_ttvZv3ft_ZmsKLRYH5oj8Yz37PiisBh0kx2046LL3oAwA6g5zzJEjKWvyzm5SIAg-UJdXuGJ6aW3MWj4IkYA95-Smz_jN_WlGhR8vbrLC6M0CkJ9MJIWJPpK-h5aMTxhpxZXCSKwKd3ihokQVDWJmECwgqV7czmN3HnmjP262MfaNHFcc9EamWzTh5SaB7OS6Pe4Eg0VyRrllbJ4ACgjSj47uuk2nuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویری دیگر از حملات آمریکا به جزیره کیش
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68047" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68046">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68046" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
