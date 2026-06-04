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
<img src="https://cdn4.telesco.pe/file/kAyG8iFHCkRzAq93ck83Zy3JcYaUprpimvrD-o0m5yGf0zooCjBz2my6cx1eCGd-4d27nEgAH_2ZtxM_FIC_SiCCYbt4GuNjgDWA7-Hdxd_s01rTYe5uEOmKMyT3zaXe7KynCG3MAGeOFxscJYztXqCD0kEksRdGC-3cZjbuXfTMm4NB-5tPFkfxWsAfeiZYWBGHUIFHR1QG9Qnk94bzy7O47N4F_89YoVW4UaFnP__gx3Z9AmK2cw2TiHDSgcnW5mkauwEh9dif6eL4JNYlavS4cGePLvEN59vr2Do2HaOkWSp-oz8VJpYR2mIvK3mmqtnM5J56p_AuopbYVYqiIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq936ugl26sbwnyE8iB79fB7noR5SqHorlpTfEf4JWFcR4T8eaoDeYDG48FmljMzDqMRdMtFNeDSPO-OZuF9ZWCiPlunWVwEFQ48jb_HekziTxJDe8_xWOvuAoKcAPb1J_lZ3JmWM3F4ZXLbEccpXTzdxcw3O8Ykkk6FTIjNQ_wNYvvaawlMT0YMXXFwwD2PX-MScveol36gyZ1r1mGap2XVtIqv0MwGzLZvWo7DsOligRE2Af1fL4zaL5yYb37mvqLPOC-y3qfiEdAvsU--D3Wn10-8zc-pgGSo9zt1WJVytyvxbqwwYeia-8BK0elWrmaO8DheQlBRJhAKLBC24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrEErn4I8PA5ae7z6EX7OpfecACK_ZIqCfiMArF47makxsbpt4g93RtkpF_w7L6BxKfuur2NYaiEjQlPMs5pAZUZ0mqYjIN8RN07SlcCqMxCXoBxgAXUDQPT0zj4x8XOxO7-_okcLe3DAuOjaeWXxPT7WBGIfOZsh8VgJv9PmZ9lIoVO9O1fRHpeJDZcPcgCSAHdTyFycZ1GlkeV-dAFadQaKkGCv9_4oZ_ZObQUFeBxQ82A8-8xvowmF2ZUPOQjHY97V4vVxbaEjL5XUev72Epo1IPn8QZsXWklHGeW2Q0jIaHdBpQh0sS-kwvUKyCMbw6DrzIdaMHYycn44n0sWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvsN94JSKqsljx9mgbDBRgV_llqF_WAaZnBseHlLELQKKJ3ws65dQqANeVtfIJlnDw9bUkamsXNJMxX4eg__jKNzrsB0NVBfezZhjqJtYhR-RnVEK9Ckf5mA_EDe2PbsO1jc5aPs8PmMOp7tRRFSZ96-ank0yI4ROcmu4mFjI_To5cjVmnd47taemzRA5xmbn_UiuMpRST9nNDkzN5Xvrk5AnGgzG21bPRm0MWUsQeVO7Io2NPo7jATmNBZmLQjg97FZaJOthxu6wfddjrAGzlSlU93BlZwS4XZ0OI1MIJCBBo2EDJ72Ws3dw1s08pVb6fNIhm7-33CJDgroWH2PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSzSJHYVHVhFewxWEpvvBqFV1gnDezgXfxULomicmmGdKIwaXklgjsp3MQYMR5f5I2HJ4PcQ9jldRJ9eZpoyWTp4-XZ5i26Aau4CqrqJht7DWk_RhpRdtNH0hdCAWctFwhZvAjxvSaBRwLAi-8zivbwFVWvdpsrZzFaUcdAsuUP4XxDM0co_wQhkFe5zmDt2Gt_ffBhKvaBBRX0v5ukeHrSsSYvDLnXp-vvl4WC_-3fiS3Ly9UsRWWyL65qjNGYU8aafGDDscO3Wxons_Wb6M6fDGT5d4AZcby1daud_Tjzzuu3Gx1AMISQH899uv-XkQypQJl8CVCBxs54ytOEQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc7NeffMHacldACBXwHgF5KB9SWjsA0sz6BxNQeeGnJE-jIxQlN9t2ErNgCfzeUItF56PxYjnHLcBuelWVdoGpaz1osWXqIdC7EfeKEE5uwz1T8dONu3kkzI1TBluBsnmvHxLKqmiyauifcRfTzMUhcRTWmaWynDqTor0yBJcRh3JrIXAu8Pc-s0wEi7jxEIWhYsYErpmZwhHuX8CYUWGs8mQdF2qt9y-Oo-5BgiVAFlA6afJTyFra4MDCbMncbOYi8b6pcPSahlaJYSjrN77QaZhCM7H4bMRL8PcC3kVzeH2v7OI9iex9515vHqU-mH0Rvt7oZ0_c_FYX-z5VjIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=jS4xDj_c3i1C68Pcam2LBwfQmnXNDiev2N4uUr6TZiO9H9g08Xq0HEHulBbRBrLUuGmVpEtI9rjZT489BRNPmDGD0eLvnV26JaBhV4w9Sl7RioKil7EISKJw1bAZeBh6ljy9PEfgXepm4syKc0DFh7--qTy4Gv1Uc-uY-h1tPlSyiRAVWE9hP2r_7DnWC1_V5WmMlSAiWhYywhOXNosv4C5W24bQ7qLSEErXltmvqHJ71xPizwMq_K2M0mVYPRRW-dSLrabmpJLo7l0K1NdqTl0qKbPM9Kh-szBLfQ9rvCpYgu1MwOP_vxq5VZ9dgxyApKnq9VwjgBRO1YD6sWmOaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=jS4xDj_c3i1C68Pcam2LBwfQmnXNDiev2N4uUr6TZiO9H9g08Xq0HEHulBbRBrLUuGmVpEtI9rjZT489BRNPmDGD0eLvnV26JaBhV4w9Sl7RioKil7EISKJw1bAZeBh6ljy9PEfgXepm4syKc0DFh7--qTy4Gv1Uc-uY-h1tPlSyiRAVWE9hP2r_7DnWC1_V5WmMlSAiWhYywhOXNosv4C5W24bQ7qLSEErXltmvqHJ71xPizwMq_K2M0mVYPRRW-dSLrabmpJLo7l0K1NdqTl0qKbPM9Kh-szBLfQ9rvCpYgu1MwOP_vxq5VZ9dgxyApKnq9VwjgBRO1YD6sWmOaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sB_h4J3ajcoo4MrVzxNnvIjZUBixGq4zulHGegUyYGdHTLtT08E8jz1W3XA4nhedTJXUXZWsKcx-VXtnZDAXFVAJxBdLyXNx1sX-GoNNCS7aYJg2SK-GbIy_JrwSAJWWpce_7UAeuUcH_ostBsPebiMTaL-bTQFd0-rtsV9UaVEgIVjTkdL1MjHlQBbAjxauPIkXTwXeORUX11K_7InXaxp1n9H2GBU1MXU-UflyhuZuQsx_hnAlTOeKCI5negBKzE-2yvdArIk5VOSS4wJL5y2GNByr4qSp2Ers_fLzM9VBrWwJGM7QUW4KM2VdxHnWBGn2LX9fTtRw7zR6G2v7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txebbeCzWXayH7eLVE4yIwEMmL7Uh2PuOzRC_NOnMGf7GLsQnq5QBFP4zbgqEmGuDiTVp2I2CuMZ0gDjeyBVblQVx3NanEpZ7KzOP1KpynPUd6QAmVlSi6HpPFVm6YRcxyrSCZLuSRQS7IAYGTOh-570c8kvHdHIKf0NAYCqi9sGg-d2n_va8_CDF5EI6d93VjsT8rRyViWCKv_8vEG3vmaCNiZuaUC4dH7YOPLPJBFL0peL9AprG5iX5Ayj2KH5_5BFvIwye2ekcu51pbWM8nxU3d847DEXziNTFzOWpIa9Znt0S_BjwDDcPPPdAOCPnG_iGIzep-owdqqHiDUgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuF6JUawgeSKBR1h4twdsPkVJj_xAbhBdm2oSyebFqXm6cvM-Oui7McAps9oRK5NkNvgGTT2ckO05Vwz3Kq1NIuOzbPHZaXH2njUWyfPUWvgyrH72Nb2WYc2bPv5CXU96nzBOewKFTIbjKTuyGOsqxGQhZbI6D3GggBOKkf4Ht9NSEhUaDG7UlkLXTen2g5E_6BFkeqk9M1oAiTk2OrBi070VYdl_R51vK8YeKTqJl9FAIw1WPenHFMFwTHFvdf22ewuMN_1ytmQsPlEwiO2I3Z0XjoRS2tfY26ltP1IO_pyHt24aRSpvJ1Hrlvs23hJFXyPfPaI-QcnI1BzTOw7ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qFuhHKhLSnnYEpXE323cfmbGwT2if47uWk4Y-wFLXBN0Z3D2O8DZdYokB8060_r_oaETIVqjq63WTqT-dI7FxbUVNboElcL7v4sGTaeMLjAkrgPH8FzqlLq-niTlyiJUa-WRM09i_nC6A0JiS7HK5SFPeTPM4ZMqPL_d835CJOTU1i2tDJjdut1eCQpwTtUPtlY5lGNmjuJfGjaFnaIcv5BvHZ2h8bFIzNOR4JhP6YictXG6YSiVvFkj-Zu-fAuKufXFAg-Z2dxN11JMLpaxZXYfqKjHS-K62BUrPFevUpz6pFXMKF2e8PLvHC5gS2NgLHf5u28Epx9Toe87GEPORg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qFuhHKhLSnnYEpXE323cfmbGwT2if47uWk4Y-wFLXBN0Z3D2O8DZdYokB8060_r_oaETIVqjq63WTqT-dI7FxbUVNboElcL7v4sGTaeMLjAkrgPH8FzqlLq-niTlyiJUa-WRM09i_nC6A0JiS7HK5SFPeTPM4ZMqPL_d835CJOTU1i2tDJjdut1eCQpwTtUPtlY5lGNmjuJfGjaFnaIcv5BvHZ2h8bFIzNOR4JhP6YictXG6YSiVvFkj-Zu-fAuKufXFAg-Z2dxN11JMLpaxZXYfqKjHS-K62BUrPFevUpz6pFXMKF2e8PLvHC5gS2NgLHf5u28Epx9Toe87GEPORg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=SYfe5TGmTxzxBPtHFMaA284xFIDzACzCAeaWMsElGnoc8i0CRaXCxVUYPpAV_-L6Y_k4ht7kRyLTkTJt6B6syU8sVm8WxOKo3xQvtWNmxXp-HdoAdQy9rz2wkcD8j-N49R4_PrQVhc7ro6Q0JaHlfk4g0AuLE_eqJZxuKnxirYTvtITnt9PvkRTNOToZ_UHMouRn0ae43acrHK9RGO234Ryn0UknOJUgJElABgedHqThsssg3m93kGXnt7xRoHdWAqALnSf6TWTcwx00t-wbgVHCd_smEeERMuFXHv2zwoFrjm966lvvQKn5nZZSjPh-_MV93GflC2Z3Cw4dsBKAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=SYfe5TGmTxzxBPtHFMaA284xFIDzACzCAeaWMsElGnoc8i0CRaXCxVUYPpAV_-L6Y_k4ht7kRyLTkTJt6B6syU8sVm8WxOKo3xQvtWNmxXp-HdoAdQy9rz2wkcD8j-N49R4_PrQVhc7ro6Q0JaHlfk4g0AuLE_eqJZxuKnxirYTvtITnt9PvkRTNOToZ_UHMouRn0ae43acrHK9RGO234Ryn0UknOJUgJElABgedHqThsssg3m93kGXnt7xRoHdWAqALnSf6TWTcwx00t-wbgVHCd_smEeERMuFXHv2zwoFrjm966lvvQKn5nZZSjPh-_MV93GflC2Z3Cw4dsBKAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxKOHkyAEiaCs7V2GZO-RRWzDx3LC-9GXbWPpK-qAOLBuInmp42-qIams4ncYwDzhxR7uvXtcgPpJJoZbIFpa9sV4PanMaAIpgiFOGqTozeLl6yBBVHwE_NJh5k9sZF4jQE5cUQOSUrWjMT0M1h-QD3130EvzZDcqIpuHk7R5b8kOosSk-E03USLxhGmY5wX8iX4renn2KbWtetMte8wQUxuh4Wn45-BuTqe1qFTzELGgdzQ_K5bOd_qnSoutXgwHpwm3C1i6HXgybMSiLua2uCO-2OWEIKjXm3hY1WwZUyvyHl4SJKsgR_5l4aO0msYiwI1Ak17JBLbcGLv8oF7a1FU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxKOHkyAEiaCs7V2GZO-RRWzDx3LC-9GXbWPpK-qAOLBuInmp42-qIams4ncYwDzhxR7uvXtcgPpJJoZbIFpa9sV4PanMaAIpgiFOGqTozeLl6yBBVHwE_NJh5k9sZF4jQE5cUQOSUrWjMT0M1h-QD3130EvzZDcqIpuHk7R5b8kOosSk-E03USLxhGmY5wX8iX4renn2KbWtetMte8wQUxuh4Wn45-BuTqe1qFTzELGgdzQ_K5bOd_qnSoutXgwHpwm3C1i6HXgybMSiLua2uCO-2OWEIKjXm3hY1WwZUyvyHl4SJKsgR_5l4aO0msYiwI1Ak17JBLbcGLv8oF7a1FU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fspQNsc5OYvFA62CuA3V6HUzrKr5w4d7OlMNtZ1cGgb4ZQo5nN5LGZAkDa9nFb3tFERQkCO0La9GIdb8IGQnQ2TebATHpQM98gymZsbF67ZRUDLLBsLQOjBbGjHHuzCCyz3ec4i8AU-O-mnh1S_VsjT07wjSZ1UK44WAbs-TcGrWpE_uIKyRRzaa_oIP34ueiyALfetcLwNvjXhQal129fQHBRqoU7wibpjom4LXn77nKmJhnPAa4K2PrsSSkO-3f2OBKEhDOuDp7xl3C_UzEPgkqMulEFSkTZmS9FuLXaLm9RsMpfbux1dYNq3cEnC0HomXc4hJNcf_S9p9EDWHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFeDPsRT5NZUqrTUVA6Vfz9rtxtRVDiM6A3gdGyWmjN0ndZmnctFVZuLN1j_1hXm-sp6jJigmg__vXtQz9misQ5VGQOvkCJxrlP6zkgDCt8hFsGlWYaKJ4VA4Fiu66GgC3uVn4ZKVqjx4ALOx5kWeixkqU0aSTos6Ma4TZzNzVsWwupAqmPJlXIj_c8EL4v0qeqUtHvmJAHIeluuM6GYg8BSkaEjsSnt0m6fncOL5Vpa0CH2WFItvP9VQbU7Oeg97fOTx81dpwtsPMD8UX-WTOenHn66eUnF_4Yi4vteueyUmJjw29GY9DymGtLC6U5_TlVnuUtDB3Wjk2ceFgna3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=WEJ2hfUbnb1CGi_4xA80dLU4NaVnyuruFoVq4pqvSj1_nNzYdkSljy8g41jzcV9HvhivmveBs1jum0oTjQDRSkobwimfu8RFUoHQK8iz-Z81jos9roaffv3Ntp2L9fR95PjbEx8DJL092MWFzqF74_PdR9xpTTJka5qPmfN44GDlDV81dVMhHmeywSN3HvkTIEMIm5bfSjYisIYuGTeQt6kv4dnQKXpQZTWwLOYgh_mo2Fc49u5WXE8eqFMsQTfwFrOS2xZMqV26aJAR5jzPpRQYcXgGcn09r6IkaZT7D6HfZCGW4-t3-w0hJxhcagGiWPmk4XYiFZZlr3EeoWZPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=WEJ2hfUbnb1CGi_4xA80dLU4NaVnyuruFoVq4pqvSj1_nNzYdkSljy8g41jzcV9HvhivmveBs1jum0oTjQDRSkobwimfu8RFUoHQK8iz-Z81jos9roaffv3Ntp2L9fR95PjbEx8DJL092MWFzqF74_PdR9xpTTJka5qPmfN44GDlDV81dVMhHmeywSN3HvkTIEMIm5bfSjYisIYuGTeQt6kv4dnQKXpQZTWwLOYgh_mo2Fc49u5WXE8eqFMsQTfwFrOS2xZMqV26aJAR5jzPpRQYcXgGcn09r6IkaZT7D6HfZCGW4-t3-w0hJxhcagGiWPmk4XYiFZZlr3EeoWZPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYlPxVoVfRkqIuE1MUrEsptQrMAfcL9NQUr4QcnChBtgvs8Sqex670cI4sFmxBvsycWX-kmlpPR7eBJStuIs50gVsOf54mmvogX8ujG-NUrwaiaib2xKPXTgc1Ur-UKwrlIaP73npPFDET6P4rfbiOBeR3MxOpLYuIMJOTddVtvo1l_BZQTeq4njdPFTknxbCC1puwZOkMurtjEg_u94ABYRIXEbA3eUCeLCWSXSI4YO3BXCixHIKMCDH092M_o3JYOsXFLxWdHay4PWs3te2P3exBo5CWQOVCWnP7AAVZdZa6JAtsDfhXbf6Av5IDVx4dxzY2jcT6oPKoYDHuxP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=MEFlNDeGBRQcEDqlmq7BHvfWkaTDlSMRkzKUm0FELCXvazs4P8a0DQ4Ikq8tkpjL1XfQ_hCvBUy8c6e8198LgfbsfLKoTb6Yh3tK53FtfvOjHOF0K1wJWi2mY7iJhasIFlEqZ_XyodL0S8uQ84JIi0VrpsaHUMhAqbnENy8Z9xm759drU40AoUzRGkzo7o2hAk9YHf9Ppr1NtuoMXhelSRQSDJR0krRrPemxncOo4u-rodlPnzQFTcY_tnKJkQqAm7U2XH7LQWHlv-yF1gIYbsEwQTG3FKuFMIjee-M78OxdJWFk7ylFXekJhISikOmTlJgTxPVz7Zuax3xteSUtOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=MEFlNDeGBRQcEDqlmq7BHvfWkaTDlSMRkzKUm0FELCXvazs4P8a0DQ4Ikq8tkpjL1XfQ_hCvBUy8c6e8198LgfbsfLKoTb6Yh3tK53FtfvOjHOF0K1wJWi2mY7iJhasIFlEqZ_XyodL0S8uQ84JIi0VrpsaHUMhAqbnENy8Z9xm759drU40AoUzRGkzo7o2hAk9YHf9Ppr1NtuoMXhelSRQSDJR0krRrPemxncOo4u-rodlPnzQFTcY_tnKJkQqAm7U2XH7LQWHlv-yF1gIYbsEwQTG3FKuFMIjee-M78OxdJWFk7ylFXekJhISikOmTlJgTxPVz7Zuax3xteSUtOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=BQWZMMtD0lJGlcLO3buoiJaj9RZ4V7kXXxtZe-GuavCcHN-heWC0LGiM3ilqh502QLRne4eXBKCGDOJ66c4VX7ehD2Z5-gWTXLatxw3Ksbzz-3l_Fb0lcdk4NGeaz7GNoTEbejIdqx4c222XIKGiv1GnU2icC2NokelXBp6bLXvchTPLsATVdwJwkH-QA48ekAVoJzh_T6194UPFcU0euJGYoM6XJbI_HoQeEa08Q4HQFWqRSxB-fUubvdlkIGqGPvLTcySft48rFTfb_12c23193CWfOxwrA4RopX-0OyIHZwoMs98_gUkiRF5CKOX9xbjXP3CqIVNrKkuq9fdOAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=BQWZMMtD0lJGlcLO3buoiJaj9RZ4V7kXXxtZe-GuavCcHN-heWC0LGiM3ilqh502QLRne4eXBKCGDOJ66c4VX7ehD2Z5-gWTXLatxw3Ksbzz-3l_Fb0lcdk4NGeaz7GNoTEbejIdqx4c222XIKGiv1GnU2icC2NokelXBp6bLXvchTPLsATVdwJwkH-QA48ekAVoJzh_T6194UPFcU0euJGYoM6XJbI_HoQeEa08Q4HQFWqRSxB-fUubvdlkIGqGPvLTcySft48rFTfb_12c23193CWfOxwrA4RopX-0OyIHZwoMs98_gUkiRF5CKOX9xbjXP3CqIVNrKkuq9fdOAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=uyCIO2AWegYH-aiwl83VFvfl8QXULieP3usPE6-0TFUgpa-mCxcDk4x7dVYnZ5h5qerI5bWRmiCcgnvRb7Pk4ogwBmhsFm8PIGJBJvOAKTiRm4e5PfZJ4rzv0TwDFFyzv1ggrHBXlnHLmwdAbsmurToIEcrox8YGzVBfB6ZF1byhZCViqrvFMo9Si9ITNyNgHt1xCdqbD6uO8QGo1yQQkgtr9rKDWUmut2d8HPGR3wseBX-xBohwo72st1QoWFmBw3iOaI-BNv4M0t2coTHtEBo3MWMiEeDBh1JjeSmzHN48Sabl9_6XHBHaxl1wZDzLq0DMtIPrzSqlShWT6aeK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=uyCIO2AWegYH-aiwl83VFvfl8QXULieP3usPE6-0TFUgpa-mCxcDk4x7dVYnZ5h5qerI5bWRmiCcgnvRb7Pk4ogwBmhsFm8PIGJBJvOAKTiRm4e5PfZJ4rzv0TwDFFyzv1ggrHBXlnHLmwdAbsmurToIEcrox8YGzVBfB6ZF1byhZCViqrvFMo9Si9ITNyNgHt1xCdqbD6uO8QGo1yQQkgtr9rKDWUmut2d8HPGR3wseBX-xBohwo72st1QoWFmBw3iOaI-BNv4M0t2coTHtEBo3MWMiEeDBh1JjeSmzHN48Sabl9_6XHBHaxl1wZDzLq0DMtIPrzSqlShWT6aeK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=SnJfQcSQ4nQaxBxS_dpoXkNS0403DegxFaDCax-vRXeHAQ5sMfRvZzx3POEHaTpp1_9V_xKyysJMv5uKeU8Mfj63nDWeElwtClkbg6ECO5m6JnPzysrMDV-YEo8x4x9cESxbnAZHK_5aGqjcKgL73rWtJSgDuWYDnxN6mj-GHDCrbwm43UknCs3KUo7EhLMXaR9EunWFJUKUOb1sh2EB0LaPucsJmgYwbe7zyQ1L2enNUjJ1LwuuVQ91Osu61NET8Hr4xyTVbXnkkmx1IRzg8a72C0sRGPcRdw4i3zObZIShc7pzzcKE-Yz2yguFUFWCJOk9G7XANjn3stI9kX9uDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=SnJfQcSQ4nQaxBxS_dpoXkNS0403DegxFaDCax-vRXeHAQ5sMfRvZzx3POEHaTpp1_9V_xKyysJMv5uKeU8Mfj63nDWeElwtClkbg6ECO5m6JnPzysrMDV-YEo8x4x9cESxbnAZHK_5aGqjcKgL73rWtJSgDuWYDnxN6mj-GHDCrbwm43UknCs3KUo7EhLMXaR9EunWFJUKUOb1sh2EB0LaPucsJmgYwbe7zyQ1L2enNUjJ1LwuuVQ91Osu61NET8Hr4xyTVbXnkkmx1IRzg8a72C0sRGPcRdw4i3zObZIShc7pzzcKE-Yz2yguFUFWCJOk9G7XANjn3stI9kX9uDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxduhlxDUlgBlcZWdJTqFHm3BApcblyulITl4qPVRe4mxzeBQA7ypHx2QjfvcpWluYVxPMyPJpXDj3GJDIlUDZKMLyrLxiDdbIg5N0TQsOccYW0hki2PheINAfsEIjpVlbGt73Djks2qfIKcW5AAp-6v0Y1cep1dl3oBlzeL94MTgkKOZ02spbOjuiMbKpoPAFhBp6t-fhnQrYSL4CBUnmPVb6YXAOZ63Dil5nCX-wjxzj0zUJDpAdJ_tYRiDSpGwcxdh4YM76ZsLlIFLfvYQOADobLT-2hICjaok-oM8Go-PsybIfTt4lyJPKD8-bPbJNY47rvibvRdgTWfu6YhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6ssxjms029gSxmuaMQCs-p4kpQGSigEakhrSKpUBk0h8hjaRqYyh5kg-XwGiwV9DAAMLXrb6P9jTd0HDSAQAUH8vD8xEPp8G-hPHQLnAnL8LhGYq2U5HC1gnaLND2fvPo8dSBwpdFTkQ5-UQETR-xZsCuTwrxG89QPFjGvzVM2B4DPAZCo6hDa9eMxTzklNsw_BiNMCq_sVMlkcDyt4RzKDn9e67sPul6VrGJzRgDbMbuFR9NEllPB8oTL94L_mVtm7npGPmIaRnb3sovZUd7Y9oP-9Pilh5W7aGCV0Tk9UNghRcwY-jkMA6vswc9cgl3C-6g2cfBD73cMYnXX4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE48b2FfCaHvARzYe2N_PeAC8Xg1u-uoYmB2mWcGy8zsASOVs-4X9NMMF8S8DxG8ykVu3JmJFIeafzQNAGZFB3g_zaj0DFm9wqHimnT-KSPj5KDb-ek59iWxgOeES726AevsQxSg8e6avCp6M6r7AvfralpV21k3QesJaPWS1s0K21Ncaybs65crceXI8QfxisKoYkbj_A2EmjLPjEMKszKJC_rXnIAhKRDG3Ym1xGrjVze4oOOn-1M2VyZSKHvtR9jhNYadTgY127gODmZMtdG5jusPtOpb_ZD24e0KqVHgjMMllFl_GX8egTU1hpfvyne9lhAkHlL6VZT-jVN9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIz7U3w6fhdrGxZgKn7GCsIuTGiwU3eOPAQu0x9ChYt5i5Ty6pHUNW5yBGQYjWmZK11jeNcS1d37TUnCxwaTYQR3TcOMZxeqWR4zXh2hG1pJZmyMYGh_7wryLvGwOzMOhBSLwKWPz7HXaw4v6hyZAisKLwO8BjwEm7EgXfjz8FM6zrMMiia3vYOot80Yi1o2zOacrne8v3MtPvk20QJMjET8Uyu-6LRedm7VueiqtJzZqj2KhqV-OghPnipp8u9ywkxLBtPPyIfnOu-s-2qm0RNW022Qblt1cXUeLiV_TJG4f8YWcMX7N4hj5V3Abd-XoLaDRneOYGw530G7LfqeUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaaL8EoD7IOoTqL83AcHsLPyyz0eiF-vFVpohJehW6eL4vikcFkT0Vs1s2IAqMZWOpAFD6yDUwibxrr4r1VJ2HX5lMvkBcb6DTVSwumFLGsEjFHA8Z0TGWTVxmeFmAk5pkaHL2lucU4GmMq2jfEcc4VaJcpQcno8bT7DpRkXqD8-hGgq0SOog9W1v502Wq9PXGnYTmzh0g8LYtLRzCzrJfKdl19KDqNZlBA8_YN_MEw61YGaxaJwcGN2iH-ERQLsB2rhbxdCW-QUHCX_8sQN3ApKLzB6X21EMfbBu4A63ekR7kn37BoCNvrp2rSakNhwAT55fbEkB3ngC2VX7iazdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGaQZXkj5GfwkQyhvwkkpRI0uBwctk6OhrjH9JXbjdvy-PNTvIKPnFq08YLP8l_MFSarURycyYJ7Z5gSs3xXpxe51i4dS_6Pp8XfY9RT45jh_2bZOY_B5tTeDcY0Ow0MxZ9rRJNaNJ52nqpXG-71JB0Nji3NoGo5oe1nAaWjAQgDKVKWJm1wMU_-YfBls3VkTh63pAp7ljd_Pl8ZIqekcPD2-bfQF7JH20V37ar3rwOAKyl-PCHAw_qV1_k01_EJcddien2HPj6HnrKqpt9gFsst3ADjbLX5aMCNkh7AqmS3Wc0qMmHTQ9-N_EYKuxkiNlbjaCH2Z9xCvW1XIb_R4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe0KIkDfdgQHaGPxzx4OeXgRFQd_MqjBfJzcBxOH5Y8TUO8zVmuzhamWmzixsS_FUDv9MrWjoN_6KUN-jGJnzfCFiCsiY1bZg5xD3F2NyiLre3ak_fqIq1hFySaIDYCm0YhibletGlDSq-q9v1aK-GxITo8ydcXZWGmupt15vZPgoQwMufDpGrIXSBmD5Ic0AE7IHV2XnVzybJf6bseYhpMalXE8inrHoxexj-O1Ue1r7nYpC04ma4GQAIyPYcxQ2a1p2zqjGtzU3pHuOqh2DUwSAHovbFJvUgthxclYlR6t1oAFwf_Dg194TSsNoQXTSBwbnrt50r5BpdewLJUiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=lhMnxa2AxFLUE2SsNO88jdCwvtsCZo6w6vKq00qYEJgYB_FTecBlTQNGu5y_KnsR7hCftK9gcpQ_r_zLpe-z1iYEJixJpdqdEpNhgC0xzE24DemUmM5w2sRJUI04-C9dR2H_1YEPwemUuiNbJFpWTNuQTof4RdTLLFv5uyB4eWueyZDRHUaLSLgobZRTPriRY58QBYuP2LMONhGd2ojRS8rj3Qp2J14zkRlE1UjYCdCQL55muPPKTKhdeInbAPxGP6btjaOY2lKrOsIsbkj02gt3X0NIeNWMkbqUjHcd7EwCzGroo_8wKllhlhaqt5XslPkm-bT__GweJorrlhzvfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=lhMnxa2AxFLUE2SsNO88jdCwvtsCZo6w6vKq00qYEJgYB_FTecBlTQNGu5y_KnsR7hCftK9gcpQ_r_zLpe-z1iYEJixJpdqdEpNhgC0xzE24DemUmM5w2sRJUI04-C9dR2H_1YEPwemUuiNbJFpWTNuQTof4RdTLLFv5uyB4eWueyZDRHUaLSLgobZRTPriRY58QBYuP2LMONhGd2ojRS8rj3Qp2J14zkRlE1UjYCdCQL55muPPKTKhdeInbAPxGP6btjaOY2lKrOsIsbkj02gt3X0NIeNWMkbqUjHcd7EwCzGroo_8wKllhlhaqt5XslPkm-bT__GweJorrlhzvfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdhEuw-e8Xm-VlYZoXsTwJvXpJUT1xkuLNuEWChxdLBGbWVRgEyJ8KiMbB7Crqemv5JZhyAK4b8x60Ak99mVEOd83yF-M5jCH4CuH3bCM-Z534sJYo4yjV2gZy5KgdrjONlY8dPHOiQBZB-qOYYEUNTXrEnGIRSgi8E7YEylb2BHOQwSOanwN20YfU-O0iMzLtng4bi--0hvQvZylghNbLfxdDJR0AC9k2qdu3-h0lca7DrEI0ITJMLmA2_Co2RMBr5619meu-L-TRb16VKrTLTjDyAuTnLbOCHeeNGipnJDY97Wnf4PmkJSu16yxXD-leyG3BnDmqidHlcQUTixjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfLgNMxUg42X9iN4fogX1iSlyoNbW6oc-e1qasykkKOtPq7cMkl2hafjTKyXKm_U7wneEzZtnRaPVO6b8_ipHCOQdoNcWLt_LcADQoxP67fJQEzEwZeugsBqbh6B7dI00uNgexKukWW_sMEx7zSB3oX8fAKm4jMKOrEeoU0ToRZ6d5OmE_vui1zRHMhecKP5oEKZX1OIHp9as-3Xz6eXByOzAQuJJ780rM8zP09kdexgqshNUEc0HKbz4kXNa0675H4uyVPswXXnTwAGvnjSy8kLXlUVbk2Vse5Ln44FIWz3rGBkis0r5Eq_0TcDMJBb3KU_Qy3y2M-_w7QtRwx8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPgo850L08-RiHf4h9Zl9mps-ll9FzpOG9OgwGpsId5DXGg9TU0gj8znJW4AGWnFqBPVI1JvH3cXgPcBcdZPiofr_WbHEhE0z4jwgHaKY3m4xY6jcu61qIK6Zdy7Zu_L-4EVxnnS-HLMBKRDVTUGxeE8AAYByEml8iMs7govclKoMPzl-TYiWB294wq8aSXkED6Vp0VwWqgbykDHuA0CvtJ3ywjT_b9Mw09ZPTWQ4aL12UF8uBVq_inBWI5zIGOF8vckN5MR-NYeS88vlU5DLPC0v4PTRYJ-MyejEyR684t3iAOzw-AUMFEdacvp-vOWq7YsxN7MOHZjGkAh3TX9ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv468ZIBiDKSMq-FGCvkAxc-UZ01UkvGNP95WQH_s3D9cnz1kuNMFO86zEj1USTrk6nzTiMUB9OnGvOkfPYWu42GL5qmLYBEPJ7VtW2kNBIoh1MAkev-AQsC8qNHfJTchn-P1XQAx1rbzN4kwGE_ufcHxsas4bydkOPxYHtJb1pOPFIGG-uz76fWwD1k9wnjCMzjDtoOoVyoraSQOgfNVGaWWH28rDil2u5OFbwz0-0vhcsHOxnpbVF165iuF6V2O3Wr2kgeympiMzJUatpIS3BdeW00gqjnCdtAy8jacOBsjlQB7ysBXMGh5yIOUWjG2A6KKDjkMsmIJUA9c3Tleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzIwlCeLAQVh9LMdknzVNh6_sZzsLp3_ksSfK8SKMlqocnBMoGzsSHYkidHfF2ZmEQc5EnUEAE46yitPr-32xcQzOw6olBSpggF2P2tNRDb-f77JlnGZZeFfgTfRxy3HqJlhdv-T7QIZKu-ojqVqJkkndxVwBzJIi4I_n3kiPD-Vhz3uj6Im8G4JQ7Dog8Kaew-Xz2ANhcRcQbW7s5GXzdKL1c3_vFh3sdQfXV-Vfo1rfUZQJyZNzNByPgIhyJR2wnmJk4z5zjLSsWQ_KJ_T0O6SmF98WRcKiuw4-yy_IDpYMhO9J_UKv_a1iG5-CwLrlfvbRQBKSltB9KDgmsWd7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLRwRPUhw2zhvxAWQgh8PzgLCjNZWLlwVtGdCBJNoq5_QMCuj9iqphp1ihihOqXExsqRn1eaZxX6sMVToL65pvb3qBV2YVWzS5cDxyD7s4NIe2SavOmd-QJTbpVfcOvQ-EVZsiUNyvylWXP4l3ST7qMAnzG3SOaUNwFG4unq-tMdblTSP2tKo9xqtToYUP6yt0poZ5tmosILW6adep26p4ARk1fxxTXzXVoUFe9Jh07rrumwezJvxP2XE_JdlJEGMoMvP4CafswuA3IU6zsx-95fNsQHiuDO_adsF9rKG7tb8E2R5gVr12rK6Th42KXKMdm_Uoq6lCnG9jQqY1gdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_de9OODz4l4fPRgAEV7KoC-HglOBWJl1I9Hf9rsT9Q3qndWQ3mpWbxNbCRRNA_KxEeXhyniqU2UQOY9rQo-BEp0mQED6pQy68kJaa4M5PxJYXusMAJkiP-Q67vZYJTOSyB_zpdYxmxAaWM-UM3u1eGOVCbxQTtSZOXcx2UFSHZem8ES-4dC_Kc7uGZgtWTtTeZVFCcP-sy6kDwxlnrMrSDvWbDYvksSlLNTlYLp7cxSG6rV_Img1NezEOexk0BSZNO39jsKIMXFsejH4_TLA0BYJa7s_mWyJAAH1TOnNjO9pJ0XHI3KefWzn_IJu-jojWThwLS1ug_bxt49PgVg2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OH_ei7_2Vw6bV74Io3Gb9dCfFn9DLRZKE5qj141mh-yPOg85E_nGijScgU-0bJcxxBdPKmVTM3laLQFE_6L8qnWWyHZBYtlva2B3oTvdXVltwesb7uhvd6nZWBNT0Uu8GkX7KWYfU9g3UfhvPeFll29tAhlJOsMvA952xzU4OJsfrFcZDSihQHbUq97aAAoun1FmU-ZJ8CzRa7oQlifzGuOSsA9e8EdzMuhUmqE-pn7t8yXPpKACpsAcBR3cu8wSvEgIMlHf5WjNyETfb7NVCaCT9vvysBiDx-6rSOWTdplpM8FU6IANDdUSTLzLoid7moIpdBSXdBLmRIXfrqFOeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=In0ae3GvfwthrLQyRJ-6wWEwutsFz4azKyeA5Y1gaY7cXYn5NqUCoPtJyJybQ4GuRxoAWtgmIvm_cC3a4rQkr9NOTLJFvpOsrkGZITDyH4qZnzFMD3bpPst_qUnSl_EW8kalYttaf9cLwZYA0fteKssmxofcrCmZ8oAia8_tAEshmMp5av5Hr-1AlyD-uToVu9SYXmcPKs2P0UqT3d4ANwlQO7XL08gjjHDzDBXHwbOMDvET2Vv2vN5zsRVPjCc-ccxjKA31TJReSH8lFa85taJP_lGo-rQmDCjOcjG2aHXqN1cf9UmoEcDVcIyVq6nnDaeLK-QlEc8tv4jLkzD87mFW4AqWDVuH9Dw7casj0cDur8X01TTqWMXigK7DWnR81LlP9Q6Y_0cI_Nf3V0DSiMMU_TWiqVbQfsd7Tb1FeTTg8sEa5Jj0EPAAe9rDPq0oD66L1pf2K9fuDB3IBaP_mRVaJqLmHQPTrbW4J0bBGvrkfSlk_4tlaBLRCifvCTP0EVeirB2KdgJc6xtqxfqwEKgpQfZDyUSlXawqzQq99yI7poSgf2DggKlXgGH_Fs11SJR6tPY05Z9teO25n4mEONyIh3AAEGwJM9s6aRFypu79maOZmntfQwoHFJDjxOVdpvSIpokDinNZvGpUqeec9FQZ_dmRuqbzYhV9mzU4NCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=In0ae3GvfwthrLQyRJ-6wWEwutsFz4azKyeA5Y1gaY7cXYn5NqUCoPtJyJybQ4GuRxoAWtgmIvm_cC3a4rQkr9NOTLJFvpOsrkGZITDyH4qZnzFMD3bpPst_qUnSl_EW8kalYttaf9cLwZYA0fteKssmxofcrCmZ8oAia8_tAEshmMp5av5Hr-1AlyD-uToVu9SYXmcPKs2P0UqT3d4ANwlQO7XL08gjjHDzDBXHwbOMDvET2Vv2vN5zsRVPjCc-ccxjKA31TJReSH8lFa85taJP_lGo-rQmDCjOcjG2aHXqN1cf9UmoEcDVcIyVq6nnDaeLK-QlEc8tv4jLkzD87mFW4AqWDVuH9Dw7casj0cDur8X01TTqWMXigK7DWnR81LlP9Q6Y_0cI_Nf3V0DSiMMU_TWiqVbQfsd7Tb1FeTTg8sEa5Jj0EPAAe9rDPq0oD66L1pf2K9fuDB3IBaP_mRVaJqLmHQPTrbW4J0bBGvrkfSlk_4tlaBLRCifvCTP0EVeirB2KdgJc6xtqxfqwEKgpQfZDyUSlXawqzQq99yI7poSgf2DggKlXgGH_Fs11SJR6tPY05Z9teO25n4mEONyIh3AAEGwJM9s6aRFypu79maOZmntfQwoHFJDjxOVdpvSIpokDinNZvGpUqeec9FQZ_dmRuqbzYhV9mzU4NCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=GjJgRi8i5l8_EQdsd4TIMdrSwQUMH44qeJs54-JZuGaaS1iZ_0KIQYm17kDUnZv38u2G-tH1dDWSZ_t8wKnbMFilaDe-1TI4wgh1sctPo9pWmS5b74pzvigZ4fphU4kYQrRLFmiCgUlDDhWaPM5PxZdjzfok1U40Bo4B5keAqNbSJ9mIYYFi3N8-DfC97-RIALS93jZ0RDlmCR6c4xEbuCOCDiKusRTP-rh3jXLchCbH-HEKbksJnB3FRDvK856MdXUq_aUraTiRcpSYOG3fldh93ZtuSvwxeDtjcR72_aNp0zT3sTekDcSmgeL8xyVCiHkPEeuPrU10SrsZjq2f4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=GjJgRi8i5l8_EQdsd4TIMdrSwQUMH44qeJs54-JZuGaaS1iZ_0KIQYm17kDUnZv38u2G-tH1dDWSZ_t8wKnbMFilaDe-1TI4wgh1sctPo9pWmS5b74pzvigZ4fphU4kYQrRLFmiCgUlDDhWaPM5PxZdjzfok1U40Bo4B5keAqNbSJ9mIYYFi3N8-DfC97-RIALS93jZ0RDlmCR6c4xEbuCOCDiKusRTP-rh3jXLchCbH-HEKbksJnB3FRDvK856MdXUq_aUraTiRcpSYOG3fldh93ZtuSvwxeDtjcR72_aNp0zT3sTekDcSmgeL8xyVCiHkPEeuPrU10SrsZjq2f4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYupJRuGUgDwKileR3a1IhLwh0M6CC_BZdnrL0A5c7uYH7CZEJCxXlJMISIH846kc9IvYoQaIKP5eHHR8aD_Pq-pYVOSQO6rUnOpuB6BKxfKXaQRzw1PwV3lhhLWqXccyQ1-dx6zM2WBlWeVsWcZp3y3lDN-P8K5sYYjMm7TvKFlUhAs8U7RKeH-vd7xpCHvRVyZP0Pt7swVADXLsnWI_L0RfZyZqYppqa2kO-adCRcu5vrH4-STpTsB9N-xtgqTlz19b2XyqeK3JsEwh5ZmKKSwX6btjPQ9Cqm8R0r6zHDkqlC0PJHu_eBR8X_y4TJUFUTRMqjbKYhqVPGdPHMgnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFWyPVjlHim8fHSgbcIdiL9NjThxtbD35qW_JNeWiHOkBBQjCvVP3ES7BTK3qoQGKcfQnFQmNvrNmgoXh34xbt9RRVwAkW4A-ZLop65DxUb1KWockqCD9cb-Z5MAv6TV99G-y2PwnQF6jtdCP0znh_iiUvPYw-89s-QFvJVl0dxkoDFquVFQSc3uF8wjAOeQGkdCUFileCsY9Vz0aVooaghd_YddjBvUP-rHBkqMa5otDjZyborwLlry4GvxFXqcrzPB1kf4pKR1Ne7KFcmyjUo2PiKBl41KD4gOw9PI6gclnHGgvT0xgyIQhOGlsRrYCDude7Xl-IQ-PwmELtW1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2gNdVL9u5xVtbWRSM4XeZY9DE6wANSkC97HI769mKhZ33o8KJcA1H6UlcJlaJO2sRAtm_D7X0CqILlRquXz3B2Km0fWsml7WhViCUHFXiJsxi-IMIYdrqMLKPgj18e2iAbU73J__8q80qr-49xU5OlIVndQj5AFdpEa67zoogh1i__YQF2gqdIN38Sl6FLD15Id9YA4uH9j_AraPYdhUdjh1Pqlw62SZveUjjsohrg5QQ7qOgAqP-B8rKqkM-PT0oKjxGnIsgfXpA5beWfAoKfRhlSZRfESYQuN5sIEkY0v0rJCEHQMtK_thw7KcDtYTlZ_4ki233qiDd0i_kAUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJBtetYtmPjeTBJwLcO27gxC2z3AKXdvGz5DAEtoHciNp0lNh-1EMLotpE-KQFm29Sv-L3ropH-RIVcGG7cfKISlu2ZBNMb8wTbvjZfK9UnMo52vUthRaf3I1tZv8EU8DLIjhB05Fb1lFywqOMdSEAUXWB3Lmcj5WT0oLZz3WRej9GmsNnHBNjc_gx0kAJqoDbx2BcvxFhWYpnxanROz7xJaNn-g3m2zaqNkl6eGefI2Av88Yq_fb5LvOST59cpH4JY4AkBztkJW4QTeT82edoy0QYBRnjsUvEm2IXEHTxLMKwqYorni-wLBuohHMqc1GnXoz73RQPoh-tH04odpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thbktvCXVc7EU7pjNzPuOv6o8ywjeSfzXAeJnFg-KwpNeKo12ES6k2DMSWUSG9c-t6cESDPwsQgslCyeMLK1R_FMxst7mJ6nxjG2uLIbittjXQJT3ktbrOpNhqHQVP_eJtIgD9BwCyuR3kz_8gZQuQI_eZsuwIaqPdLLH8osFbkVgcJgLcn9iSMZJ0u9rsSZhy-HJUb3IIM02MAMFrJHvqD-3b4SbAsWI8e8TNsczz1uilArA4G86cKibNAVFOvBSVdeEzvOy0msBuQS6vQHWZKGZkCn21PMRdcbq_RXaHLMA9EwrOsl2L9QHh-dV34CDs3K1pE-Y4aK7h5NtSFRKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7FULEYm5LYdmq6hINZbvTQpim4iGC_2SWV-nr-sfsGaeGP0Jlr6SPc51zeU_7FTSfXlDnTeFlpXtM3kHBBGou7LbcCf5Wx5pQ0CEUKbiw2Quvod9ZyGGGafzBYSJ6L6qtrmDIuQC1h17nEiUXUJTmHQubo9GV1p480-7ddHvsFLgTzJEPE-SDV8upQzHqql6b8vbmlJIuBjhZ8pDuvr0Hzazcdufx3Ju30oVL4ne8EuTOy8DSAyNYEPnHEyIGeixHL-8M5jwsTpGpBJTfJ6Ty5ahB_3UbRxLeH3kDeioi4nZtOao2dkBseJF_PRWMNPChcf60Ps-TcYvGWUyBTl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNvAyryOa6LwXVnpFRyVpcChVNHD1EAPE9O51hh6gTiL_RCFoHw01Cnv3ebBYm6t4ON-DwwBCSibGdrsdLsSdkWmBojLUoMMGNuPw0EI1q8NFevMqOhIhWpD6iAkr8gxc5TdJKKWo-ZiR2DcPam6JP33kXKi4Pe_9WEcoK4wcpD88TTapoYVjl47dX2mYHOk5K-2koSlHSQQYRGbb_vqeCivODwAa15RSOO60zKyiI28hVpk_nzkqxRx0BGqQWPpR51ObwfjBwdeGPcf0wNlP9scQCCeUqQtxxuXq7NOP40q-avw8omt-pnpsFvzvlxnK19WtYpHEgW6KF_-zPz-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULFvqJ5oGhbsRM7H1wayQBRCPnsu70flQ4-ASyTIdn3WsFWWerEv4DrpVf2cAgqDEFXrdpTxv3QZZMzG3eEt01SJxNVpPhAUvG4XY_QldNxNFzTE3IJQ0SvVvJ4n-45jLQUwQw3uJX519K805M2wqdLz64gntLTmqgQlN58cpL93CPshKfMI3Lj4pb_b0O0Jvpf4tKjrSt6SxfIvJsSoSR_9vB6IGFdKaXRQuBuxXf-i8jk838ACqUODTPoEoXQwnIP7NyTsCdP6gIMBTcmQhdAhMcCPQRpZJzmX0WnAnFdCMeAiVG949sU2TrbTRvKL2WarhRjKTLe74u3oqGwoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ti6S6ikUXAQqYx22nzG_-sP89zImBYjWGjVj8wSb0SdcwzvcVuhAQ_Ko4seBXVXq5ydwK7qx2xNI9EQ37tpfJnMLwLn2pE21JFxCD_WzOwpaCstnKI8S2pD6_31A8ezrsgkeA-ygJ4xSRKcjkj75oCC3KZ2yNow8Vo_ZsTN2Ag_zBo8GTbhAVuVTZUV4mMhv52J1RcDhSOI9H6lv7Uo2-n-TbW_by_kxwrCsdcdaOZBYm_F8KMADxNR3IF7tbgQYL4i90fDIpe5B95dLIQ5sMzvNUCAv8EDt82FzqboVexc61GCOEHoNhxLb0V7iiu3FMlvNpKS6w4PF9Kd63IXSUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=GFq0xfw8BijaQuNi75-BD56q_2isLhJRVRMBVIJdwN8FycODWHjklarGHFRjcsHCZ_gIqm4SdqPSYILSqcLiVENVNpR5L3gSDNuLVeU_7H1-G4c8O0n5GscA3M940sI56tgZpLZ6vzKNYnhVqA_I9nfi1J48F9OrZhg1KXxPr-CJ5IAAhAGSxS9HhWl-ch77RpTWoz6IXe5O5DaqztP2Q6x6F8PNxJjgBiOclE-8ggNQtEwN1PteyBlch5kpEv-ql_qJ372zU5_Ot5SloVf_78nrLmkbF8QYBbu1ZitCCh7mEC5v3SISFF3t6PpR_FOv5IKdoh-8J2-UkFN2qnpbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=GFq0xfw8BijaQuNi75-BD56q_2isLhJRVRMBVIJdwN8FycODWHjklarGHFRjcsHCZ_gIqm4SdqPSYILSqcLiVENVNpR5L3gSDNuLVeU_7H1-G4c8O0n5GscA3M940sI56tgZpLZ6vzKNYnhVqA_I9nfi1J48F9OrZhg1KXxPr-CJ5IAAhAGSxS9HhWl-ch77RpTWoz6IXe5O5DaqztP2Q6x6F8PNxJjgBiOclE-8ggNQtEwN1PteyBlch5kpEv-ql_qJ372zU5_Ot5SloVf_78nrLmkbF8QYBbu1ZitCCh7mEC5v3SISFF3t6PpR_FOv5IKdoh-8J2-UkFN2qnpbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSwy-j_ZVY7vV4s5AFYH5e5JaMfsRIej-dbKiH1g0g8Sicg1DgdAluo0nOQA-yG4zLOC5G1MWPdaN4nS7mpIhVrtVoPMDxR18A7VuYW0RfYiK7x-WwbtaoDbsib7IjWdZkzFUTvAzOmwvt5GTqvwgzX2-H_kP976R0EVkc1_zUtyf8JajMDcAadjjVIRU0F0p_2cng1R6sOA1TLHiEAIRimQ1xY_I8BGLps2p7RnZZDeMrb22H4zbg2Jm2iZrnJV6F40tvF8tgQYWbFUpe0pUCqnS8nuddtP115Kk9QgM7sWLt1GKO_PkzwqgzwdF0rGYc_RihGbAlPH7Uewktx61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=asnifyK4SYRNrTl28hmDI8abZl699ufVNg0Kxr67iC6RwUYn5UeQA3xf8-eE8e-w0QMPI4Wv8-zO2v9G0bTDVBfQb14zQQsLk2QIRoqRNfAq4LhunG287SldIOIDa83RC8TNqFDcVNh2ZHyWk42edOmqn2hxpgomkhX-CIZqlyhuC3x8JcLZ7QYahhRuae6FaKlVXBsFZq88QNCzslmBtBm2Xibdm7XXDOOLYs1kWqghA_MXnTnvm8o6-9Wsseo18OUzaw9hNb8RO7IWXRzGISckYWFPCgtOVf1FmUT9YGueBOFFDjhu4IdPJZUJzixEgOaTxoz7xUYXykKZNzpN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=asnifyK4SYRNrTl28hmDI8abZl699ufVNg0Kxr67iC6RwUYn5UeQA3xf8-eE8e-w0QMPI4Wv8-zO2v9G0bTDVBfQb14zQQsLk2QIRoqRNfAq4LhunG287SldIOIDa83RC8TNqFDcVNh2ZHyWk42edOmqn2hxpgomkhX-CIZqlyhuC3x8JcLZ7QYahhRuae6FaKlVXBsFZq88QNCzslmBtBm2Xibdm7XXDOOLYs1kWqghA_MXnTnvm8o6-9Wsseo18OUzaw9hNb8RO7IWXRzGISckYWFPCgtOVf1FmUT9YGueBOFFDjhu4IdPJZUJzixEgOaTxoz7xUYXykKZNzpN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=lgmcrvhFw_2_yeRr8KgiDoyBSKsUOPMECOFl-tU7g-d9_t6Z1EU26Chj3qagB_kTwXoQkujDNumIRsu-jLlMM0upX71WYb4GEsnaj5eeQjuIrdwAF57UXCa20YOMyHsIXY7xqt1ULXHiZD2a_yvhVZevm1Gw9umdaie1hPenDlG4d9w1awdGtSwlvBHqLBHwZH1zNvjve4QYEb-NRNUT8CIlaTAKllP1Ip9KLr8CdsZhuX4hEb01t522ouLiI8e3aPBtCuFE_4OUPZJs0gG5BAUAoaF45jRjb9m2Fqgiloj0m3JCe3-7DQZQsVWlKMVPj8ROZYJUfn1bcYTqi8D2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=lgmcrvhFw_2_yeRr8KgiDoyBSKsUOPMECOFl-tU7g-d9_t6Z1EU26Chj3qagB_kTwXoQkujDNumIRsu-jLlMM0upX71WYb4GEsnaj5eeQjuIrdwAF57UXCa20YOMyHsIXY7xqt1ULXHiZD2a_yvhVZevm1Gw9umdaie1hPenDlG4d9w1awdGtSwlvBHqLBHwZH1zNvjve4QYEb-NRNUT8CIlaTAKllP1Ip9KLr8CdsZhuX4hEb01t522ouLiI8e3aPBtCuFE_4OUPZJs0gG5BAUAoaF45jRjb9m2Fqgiloj0m3JCe3-7DQZQsVWlKMVPj8ROZYJUfn1bcYTqi8D2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlNFJKZmbVKxGDUNExNx8XK2-KJ_EVCo7fmLit_koD8l2tbudXwYokjr30YVq0J95_VxEoxbmuzdw84MMgFP7W6NyicF9mL06VXCY_B1NuJxpjD0W-GsXphrN7X-83KWFe5GTOaEqx6Ri05VHHSLSeOsVFt5LAd_Vzn2mRfiylOmqKc8_x8-DbbZ4EQ2AtkEwayBB8KZ7e7e2hLDtFn9NcnH0pv72zlF1d7tLsu6oLs9Ne8m-5KmyXwVCVE1FIMELqsJxLywhXEpz7Z69e8nxQHdRX6X4egA4rkQnHiFCVkh7fN25-WOqg61mtNuRmc_s0UIU33wF233K3Me05n1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=rPaNg_GhzmMWqHk5XYQCxvF-3L_bQiiglOTYkWmkymtacdSPOecqLodk5aiDOsmAUFt_5dUVRs-FeTJm0HAXMKojFDePROLa_K179SZ-mkjZgrwN4oQeDkJUxEqGb8L1QpwRd1A9YmrNpKgdcmGs6idDjc5qpF9lAvBVl6JVYW4B0mVFOpgysfKoXHY9d3cdvMiLiyXPRn6hqBWiCnSxXPXyQW1PKsSZdUvrzlK-2S5GTkXcK6y_W6UB3YBj8kEkqaGJ7WOWpvS27StIYYh3skqSbgg5rvo05u7mIbDvqWNqaTqx3GDFt09hzTivtR80bEnTLu2LljdF4q5oBzn5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=rPaNg_GhzmMWqHk5XYQCxvF-3L_bQiiglOTYkWmkymtacdSPOecqLodk5aiDOsmAUFt_5dUVRs-FeTJm0HAXMKojFDePROLa_K179SZ-mkjZgrwN4oQeDkJUxEqGb8L1QpwRd1A9YmrNpKgdcmGs6idDjc5qpF9lAvBVl6JVYW4B0mVFOpgysfKoXHY9d3cdvMiLiyXPRn6hqBWiCnSxXPXyQW1PKsSZdUvrzlK-2S5GTkXcK6y_W6UB3YBj8kEkqaGJ7WOWpvS27StIYYh3skqSbgg5rvo05u7mIbDvqWNqaTqx3GDFt09hzTivtR80bEnTLu2LljdF4q5oBzn5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN02bHCdx-Y58G5m_JqEibbaatJCOVOeLJJC01hlct5-Sl3hYOBXOIrDZoP-pEKksy9ta21_iCWEEKO6XC7BIaBvYz4IYHJfniJtP1bZhobCh5_9qS0dwD8qYRKXgh__1LGzbR5Pf5aITRvb3bo936YegzygqLhyTSvgxTKX5acb2-h2SPIvl4iUp1FlOUiAwclstaGQdmfNjFbF9y396gfDuaWqlxPATgP2KRnb2559pwKNEEumEC4cQK7pOuM0_iD54ksZY02nc1JF7rl7AIlOVQoLemHMhvOESGnd79i5AH8FUbdg7g7xUsX9dhgG5gSRH0oRXlt8zy8UhjmVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrDUHQwc9p1bbIZD8ZHbhP68hYu0ZNWkCC6cy67K5t49nuv0js-PYh2zt947ziKeJOSN7nvKjaw5kWIoOc2OH2N70blIdP1vInWkh2zzD6Iz-ZFbXBY1RGRRs53hBx5Kry3bukKtKGkuQUypHZrFc5m7xQy6z48lTyMbqHF_M3F2tucl5J9o--y0cl7r5-O_LiY67HnGDk91FvEx9Fwb9blzHz4XLMSBfy6ii5Z0la_yM2Z0duk_ieFOTf4dE9taDzTo4HYrzqO31tU4x86aQj-_W2670U7PBKMni8tK4Vl9a0ej8ATvyZItuKGh2Yupj359Bxvpoh_-izBRqnkkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTs01YKu5myRiG2LOcJoeTInpln-vPPAWr6AUm1H2PR7ExkDFLazeSpVYD-N-7i293BzFFnhQgl73v7CelkQHOgwF7qkUlfaZpPqEKoy7K-_brRig9RzCRXmeLd0GaQMyx32l2CENKMC5Ua-3-UDdRnBLIyyqwk_q9JODO8oKLjsczqfij2lqJmB8p6R5p_zxxg_MIOE4JYvFDRZnVKKJ1wJzAtJD8yTA4OroG92yOnGo5XikdeJMB5qn9S3dLIVGKAHDpF234jOsiQzEAPFY6wX-2ikhI-9J83FeElhYI0_iKR5Sw1sS39HkB6pp3y6v5KzohlX2KwXQrBamG6z-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdstn736e4tksfKdYS8S4oWk_FHaLAiHbKweFYVZDHoIkiT3AKlG0t_L9MYTcyA-vkXM7Xv6Tp4C3A5DM5gOhCmSBYH-rW09ZQZg8uScjv9bQcg04FS-hUyYCsuBAK79wABfSMxN-cVLJr3t6k2xP5bM_TTd8Z5URYgoPXIbU67cblN-u3_v3Vi7OAUT8tZkXFoqqcDW0XpPRa12cWWL8xaQ-nnbfqBP0hF9ilSGo_GG5nB_XHtXrLVYgvYrYqZN9NT0KjOPRqvhPx2C588Z3Uy-Ug9UETQuS0LHSY6uZVHmoGOo7CH33sBcscZmv9d4pRABl2tZCsqVI1O3t3qnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofbQh4uapjHvRFDr_c9OseLtkeXaWcQ1SKJGG4vFO7GiXnlOqmxyKxD-m6fo4iJSllTzyFGlkQiiISGN-PQL1ZHln5l4WWXZcYonlJHPVG8V-Nl9CsCv7G0rsdRMRaPlnn--mpaSRwCaB2awAKCS79kQXoIfePsHF3XPdHBWeyV9T-yruXAT1Y3mOIrjB4yWDwKGubyNc3x-kzBe1SW7lFHp9dA9UlhYVJEXfMqzDijg1iTCuuV-3gcQMLyMg7EaIuJnIbgsrH-Zyd6n1-fEg5d6VcUKqhjiRMvfVieNfOTk0SLvTQ8N-kQPv6Mz8hrRz1AUmKxKiKBubhZ-tEl9aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YD8YNl0BpU6-ysuPeYJmFgl7Or0SG3IfQoU1nd20a9tOLLJepNzMGB18vpY3mrYODw9Wj78XZRJywPem2ydeNbOwaiMWt6fWgHv7LjXdlcRdrjheJhgOmyL1dOSqNnXsOw8XPWs5rjP92UMccw6HhiZ0aBb8oAGygn1-Wv9TjIqZt_1Mi4MrkGSKtdvd-7PPgZPGUarlRTgvwiwBfxl3cilkw5NZqVaH8Sj2aPdMZEd9J4FQTHQgtTB_5gAWJsDLJ94VTK4RL2p4-DYKyYzn1NX4Kv6lTzVEU7H3bkZpR8FFehJufaixDT_geOtzZUeQQnnKEhMQxRhImEw7sf54OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdfCAFVSvV7Ru7MVl4SVjnrD7t6XWvjDFLp9zli3vqyOvZNqANY6e5ej_-eyrENRN-EFGaOi4bIwnwx_mo_2cV4nN33mdgtu-evUy53FwnFLqPTpljxX6tNTQ1vffbYpYjp5QOojcD6-f_IU_EmyEnt2RbNiSprRjFqbw9wIioOD-59ubEmooShJbqNqM49dOMafkk9QVPh31q86WVVAnAyh5D1VNFnso6zD5bpAQ_Hd7Z-OysjocbDiKxjl-KVlnFSXUW-vuVo9_Tuh262x4VMCq9qXAyueW6K3IwtDr7hjyjDK-vgCGEgohoPrlab8noyt4ENx9ixlAPJgQfFgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0Ez4u00n_npqV3SxFGMeU7H0ML6iuUXgGA_euKl7zPAnGzKJYgxC5EB-eUqbUSPS9keC0HSkXKrtrcwDGeq81UponWDeoOXrrfFsoO5bkT6C4KOfRVmdKscrS0OlrkNtJbBYV2c7kX3-DzBrobOCE0e5uUWZA6E5erWzcqNpghmiN0HYHrtKRzPIjpB5iZCFhFBfD1YoxQWx87FBU_i9o76WDwQCMNCc_riuM9h2sfN4wytW28mtNLjpovQZa5-JjDbw8mxhKXQIDJhg4CL_ImgYVYx3fs4MDSZrIPtRNa2hYkOzGOdQtVgDuUt_uzrimhiE0p08HEfACDc40yn6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=EpQz6IrYuAc0KquUKY0-0UoyknLiDUqqUdSVfq0EWhEirvP0Nhe3HSlUp96QC7ZYzvz_M-hywgzrkiXq1QFahrbf4cJ9Y4u9fUkSxlammjZJViv0GaNLeq3dSBRDgY9e0QDL9yVW0deCVa1aDxuU3gO3CGB4VBeKZP462fSma9k1p47I9H2MrHK-v4W1EaWuhs7Pf_VBhncllH4RJmKMX7hsr40bO-gyOTBZDuwETnzTKrWJVnuqXtTxGuF49INZQpT8dQUmNDFGJMVL2r-BpEnx0Pa54VJtBblVQx5NhbfU6zUHS-BhYF69FcxRtMe8ZAONMqt-ZVFUVxFKhWwTAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=EpQz6IrYuAc0KquUKY0-0UoyknLiDUqqUdSVfq0EWhEirvP0Nhe3HSlUp96QC7ZYzvz_M-hywgzrkiXq1QFahrbf4cJ9Y4u9fUkSxlammjZJViv0GaNLeq3dSBRDgY9e0QDL9yVW0deCVa1aDxuU3gO3CGB4VBeKZP462fSma9k1p47I9H2MrHK-v4W1EaWuhs7Pf_VBhncllH4RJmKMX7hsr40bO-gyOTBZDuwETnzTKrWJVnuqXtTxGuF49INZQpT8dQUmNDFGJMVL2r-BpEnx0Pa54VJtBblVQx5NhbfU6zUHS-BhYF69FcxRtMe8ZAONMqt-ZVFUVxFKhWwTAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=QyNSsXh8_3-O9vZtSpss6UyOXRfd9eJ_rCSeylavdzowJklqrYnFUpEfJ-abELMC-in6L91XvDrWpsGw6VDVq7-Ft3TO5rom5I7ktbRNyJuPsjVnw12B5q54vq9c9uuse9HhFzU-CCTO-G_3Ri49tWMAayvVST5duhp7cUayyzt8z_t1C0RCfL5q4k-vUv5D9SRP-pHA-mKPZgMUHSrYJ0y5qAijung2MRaiZiNafB6yhfzeB_7ecj7NPy2G9lt3r5_D4D9JYCDxjMJuuxbseZNswUiTd9KNyummtQniqdnkYLvl05Cr9rjPY4OX1YUnyD60zBnM9ow6hrWuDQZVmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=QyNSsXh8_3-O9vZtSpss6UyOXRfd9eJ_rCSeylavdzowJklqrYnFUpEfJ-abELMC-in6L91XvDrWpsGw6VDVq7-Ft3TO5rom5I7ktbRNyJuPsjVnw12B5q54vq9c9uuse9HhFzU-CCTO-G_3Ri49tWMAayvVST5duhp7cUayyzt8z_t1C0RCfL5q4k-vUv5D9SRP-pHA-mKPZgMUHSrYJ0y5qAijung2MRaiZiNafB6yhfzeB_7ecj7NPy2G9lt3r5_D4D9JYCDxjMJuuxbseZNswUiTd9KNyummtQniqdnkYLvl05Cr9rjPY4OX1YUnyD60zBnM9ow6hrWuDQZVmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=u1kRLdhpC2QFan_GnWpnIN0n_hu1AzekXDl4Ret2JUArrAiueOhsLJMbJgih0p6NN8bIGjDBpyzFKmKbuADpO25NZ9USFUcwyOyJ7w4IjW0FGdjud1-oVoNQr4JszG7-oE9KTJZ9kWoVyfer4BhhNxltx4IaiBVCziUgrHnyT_pdNx2CSJpM4Teye6rCiZpNmq_oxhn1kjlIx3DEPFOd3qY_wGRO3Vs-N3ggD8WaxURlkuzOWE0U8K93O7lI3k-2lPtErjLyabhB6nrLh98TP0ibGYTZHcaahDYCXklmM24W5HHSVembcQL3HihbfbD-TWtnfl_ZSMA9FdA6iy8sXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=u1kRLdhpC2QFan_GnWpnIN0n_hu1AzekXDl4Ret2JUArrAiueOhsLJMbJgih0p6NN8bIGjDBpyzFKmKbuADpO25NZ9USFUcwyOyJ7w4IjW0FGdjud1-oVoNQr4JszG7-oE9KTJZ9kWoVyfer4BhhNxltx4IaiBVCziUgrHnyT_pdNx2CSJpM4Teye6rCiZpNmq_oxhn1kjlIx3DEPFOd3qY_wGRO3Vs-N3ggD8WaxURlkuzOWE0U8K93O7lI3k-2lPtErjLyabhB6nrLh98TP0ibGYTZHcaahDYCXklmM24W5HHSVembcQL3HihbfbD-TWtnfl_ZSMA9FdA6iy8sXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_9qR8lVLaec5SD7_Vf5_x0Ax-wkkwfPSOffaptjc7ZqEV-lB9T242L6toG9yuTzFWlNh_UfQaanHiyUAE7L0AqzYThVHWq0POl0bldphSQC1ixkPuJNnKMv8vgVkQKRtb8AXqRJanqXJUYdnQmRttVZWfODrQ-soYqalNvNWQnQYCFByRyBMBFcHXIvepbnhom1XMGtYHuNpZFxTGT0gW3vXTCTmbN2-gtl3oUZGcn-5a2YfVbrF9SooaUvn3ollK5YvqKZlJltMzkC-oeftUkgbrIFWnEpIMaWIGts_PnW9T35R4_RcBSKvwPKT-pjSkNvzeYN7g4rY_doYlwThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc5TOXSu5MBExAjC2D5lwg3nN1oAgu25nqWOBF99tHIxnDdu4SpW8gg072MAy1CRRKjZZkeKbwZCdcrIRXVbXteCNzDdFH6BJFIIm16I1raooBGI1so8aVYwP6I_WreBxns7Ih4KQQyMHRel-sjTqN9nbzFzpewfOhawi9HS_b6lVxM1F2UhE615QiKBvEIw9ypaTmJqAt2Q3Yyf9H7DPC4ph3aQJ1poH98xC5c5IM8Ah66sAA_DtjqxPBkkkKRooTwJFmPplj-FYodiGcBmML3yoyisoTCywZgh8huXrKIXJT_Ozo7J10sv0U1mZRLYYKFjEze3PLKv6USmw7-U_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjshLAQ05c1s57t3wBHTEstqkqrbPPxK0zOsHN-uYmV005q0mMU8t7Fq6RaNWZjHG1MPREA4EU95Xqz4EV1QJmUa_MWJifhRCMijTy2g8mPA2If9RcMFRphq8QG6dASn7znJLEWQSsH073GUCsjPV5DWyj6L-nqtC-u7xK6Dn6qWHvhK3XP7bFLIHTgRDZ53KZOFBKqxinlSZ6MCqnrw2jSNisr17T-q53jjSBtPBaWo7WEhxH7E0slZfGwec5SInDkHAWfDBMCbzxAqv3GF0OCRUTpRA097c2cX7Trglummros0UAsyB6MFYAu5MU8OGeONrw7Xpdv-aHvLSsorOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUHcBl1tZrsbvLznc_jEaJh4JsSFJWZGvKpipztuEPBhht3g-Hw1M3hmVZnpf1gduQieR93zgAxfGnA8aTrm-qFHZ-x2cPcKXJVux3CKLmbgmuOYNEQCmxcOxJsxAmruKwFfClXHY-W8nn0BIx2GoXsk306BFSoBw3eSMLjdqf7X5X4fE_2RVCq5UooqklRgIpAOwLOZ7dmPTh1uBaGEsqSw-X_8Ch4OU0dny8KVlRO9HrH-xHQUdBC-ti_BLzgS-gQQk-LLaCB5cSceo6gf-bh_UlSQiOu2Y27ve3HWYEdBpVXw9IbXHKzCF37Y6yumbIfHLlKb1775trIyYMDMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=eCJMCSh3DVr6pqR1kXPXLwGlVyI-eTXBcYJE1XDPSkhlyoh_jy4poC_5rgMNWmjMu65XHqf5_FUzwjA2c97x61od8pVvhtA3iKvak3L1x3SNFCM35BtU9D5R4XINT0kcyspdszYEUL3TppTeJDbjih2HM_w6F10MwdPm3I3m0DkrX5Aiv6r41P-ac7AiXWWqyxg6ixCG5HKHGaYP3ZKDyW28Uq0VbELVH2536ygtFc4mdleDnnES2oWL1XQ_3sq84K3Hk1LgGJXzcHcUb0r2WAefTR6afKnoe2EauljR3Ydl7MHkp8RBYNCCV6QWYmhUFtYDq0t-tLZsJihUQF0Llg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=eCJMCSh3DVr6pqR1kXPXLwGlVyI-eTXBcYJE1XDPSkhlyoh_jy4poC_5rgMNWmjMu65XHqf5_FUzwjA2c97x61od8pVvhtA3iKvak3L1x3SNFCM35BtU9D5R4XINT0kcyspdszYEUL3TppTeJDbjih2HM_w6F10MwdPm3I3m0DkrX5Aiv6r41P-ac7AiXWWqyxg6ixCG5HKHGaYP3ZKDyW28Uq0VbELVH2536ygtFc4mdleDnnES2oWL1XQ_3sq84K3Hk1LgGJXzcHcUb0r2WAefTR6afKnoe2EauljR3Ydl7MHkp8RBYNCCV6QWYmhUFtYDq0t-tLZsJihUQF0Llg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=fQVmVQuiQT5mwRuq8mW_WljNO-XpBxknaZ6rqD1lwkdZKs8ZywFGuHQTuJS6Kn0WDpgllm1vE_HpuAv-Gz_PmIBD3j7_fogkGXNnHlQS8EL56R2fYDj4dVtDTESJl5ir8q3bGoIm2vAcPCJdsmjDC5GArnTMfrPQ3UNDPFJ9kp_nzG3X2dkXZOj6unwDEGmDmdz1yV5SPlOAam3FsXpFruZTOaRX3ko9hTwvGTthUkwkRwDqwmfqipYGOLfHkzJzPg6dd3zbH1yYHBfTHYGwhGSh9xNa0OXUutkqEK479O5lVzc6OKuD8ErZKjYaOYf5lec0dj8IcTI_8X_wQJ5Hvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=fQVmVQuiQT5mwRuq8mW_WljNO-XpBxknaZ6rqD1lwkdZKs8ZywFGuHQTuJS6Kn0WDpgllm1vE_HpuAv-Gz_PmIBD3j7_fogkGXNnHlQS8EL56R2fYDj4dVtDTESJl5ir8q3bGoIm2vAcPCJdsmjDC5GArnTMfrPQ3UNDPFJ9kp_nzG3X2dkXZOj6unwDEGmDmdz1yV5SPlOAam3FsXpFruZTOaRX3ko9hTwvGTthUkwkRwDqwmfqipYGOLfHkzJzPg6dd3zbH1yYHBfTHYGwhGSh9xNa0OXUutkqEK479O5lVzc6OKuD8ErZKjYaOYf5lec0dj8IcTI_8X_wQJ5Hvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnFXtROuYcishrdl7nJeRPN4IpUNuoARH86nGLRzJgf2WVz52lsR5_P6pNjpCtQxdKAIIXEa9acVNNkM0gsWTTU0ThtjE79cyC9dLULfuhFeddzN90GUOYbI4bIFoAN9joDH-WyF_ue8NU_4cxCoHpf2kBdsI88zFsZo6WpVpvUhtDisJcWeJfbK7qIYGIjJVNIsjUoyPqYgEJ2F7kaYim5hRf_RzGiVUwOvt5sdomnh8iecE5hqVhJ9uQL_-Vitbx8N28JxmTi7VMY35rJO0pBWQ0Btmg7A2q3w9Wf0PfdYTg1z9NYbNNSby8y2eDGJpSi7SaqKBGTLFinYriogyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH0s4vTRqLC-IZDAjLsQefOr5nsHi78dLUFcF6Rj5mSDNm6-jDIxLcjtP9drBCiw3AEa0gu8F1Uaiaaa3M73OV9qgI48Be-nHhsTBUvt_h924-XuvFIpx3RJo8-5sv3x9BfngWjJITIwXRc4JGFrGdETvOxFhSfGYXMGgup7sTbD3TZIzBBssk1BHj2lyInscpG6Qm_Fz7bE8al4exxW8z6gOGaCXcHPKU6qJXQU4awsC_llRjSgJ8Y23bccwBnQ0E8GV4mzKVT2hp4Dl4bcE_0xJk1k_-YCktzlh3ljVig65sUnJeDfUs0dFZ8nWWZfL0wXVlEA8OfdEwyTm_tEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuWhwdL6yM8rHyWR7Vkyk953L8gv0ZAjwT3ZibyzIKhpeaIjuRo3UbacLm5TPDtceeT2EDLI8VT7wRkHlwWepNLg9fYgmQ0Zb1paciqUt2He36Q7N1OAxVknyqbLBsjYETQ-WarO5NiycVFB2vDoGYBtqbA2nfKrC-wCS0Eoe08TjOW_9zIXTAlN07gJoz9O7KVYGurj8PbTago8yCpyIerFSjY1drC4fIdo2feBYoKcDxcswTQ3bG3IqQ6a9nz56IyEXSNX7V8BYfsIjPk4O99wZiM9sUESGy9GQQr80YiG57Ec3zVuCBCGjupJtAdmL-8CUkDpZR4ux1g5LMfyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu1WviniQlVPi--Ln9PElpOOrR04tEWRxrWMulsxIekpphJR3eyroQs4_4TLMgWPBudCzHY7whI5pBMBLU9_gfxZXfXApD-R4ZjdlMevd7YJwZDuC5J_dSKBCXBcvKK70y6DbLW89T5dsZR6UldwdcdpO1uEyU4Q68iNx8-Oxm4NfF4h9zONrr_x6lzOb7FUzJHCON3LvcRfWtkLoub4OqnCBzEbtwFLHs9WbvxbX5vBxrhweR07MQpcORxsfVY2GXKI1vmIh_3hAny4WQegLAsEjFFCKnUmR_6SxRmgYPhzXNWHiG5ui8oKr6p7t2Klp_4afhD33UDHLkZ82S76pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSBonrirrdwnZ2SSPe2wUiqNeLjjoCZlM8HBnjG07_vEUSgiBrwPyTDxavsmYPSkXsk81teeq8E3a4LSaK4rhFsxz9twjkbKZDGE_8AE1_OIkAlI18umOPjWKN0Zt3JXruzAqXVHH8PBL0HGB1Cd5vwCCtvSMF6pxbrOp1x6uEnPIK5rMWDt3FTOwwKJc-vKn387c6ZUKlrIQ1kScCczLacz9lWgU7B3o4mgZwY9DqairTQJYkpJ1BTpItoUnxo-Wzwx_mYfo_H715Hh_tkVWyi7lE5LNnB603Zf2K3erc4a-yIuJGkNeXTCXEXkduV__8na-fdF-OF_JgVMHJOKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-ZoP8vvPIdzk51IVaOK6oUg1pJjqN7Nc_UWrD4lF0GsCmeKL2xU-qupnTT7jRaPAgFtM1oeFlcMiU7D8SaM8DFHsrAqSNL4vPlaQQkWzFa6shpBiAr5-XudDJDWRw1jQrnMiQbj71wjnFqOGKKsYVbDsLHZs-kAOquOdKUYJtkUX7TUmT6pl6LsceS8VTmYGJDZuS6e9W5Knt6fLDGM5ZTCdLXjoHPTcsJJkYjsBVEmMwpeu4AK11RhQoE-tnJ7-ESSSd0hezVqViDRkphUgyIxlRi9Y8skQoBvW_HiTu4lvvFNSMn-B_-SL6AKWpkP6605B9RqPKs_2d0ULfwqRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WfWdxF_Lv374p9uVsVue2c9yEI6DgGWd4rbby6-OeU9NInkqhtrKPd_y7IPCUr-aeLKPc4jilagS3LweMLz3lmKEFdrLmXoZqH4hB-VkgXa_yCuZpeThp7dksNt-AfxgrTqDTW80QhL5OnvouF5bu_QCXd1EzJYMsbmNbic_stE_-f9_PEXDMOc0tLq0NWM44XhVfb9XGepphLIHTVB4RPFReQtMQ62WLNyhQXuyZTziPLDP8kOFbCay_LzpsTSP2ESFDjIRDxaeTIrM8Xh5owlFAaDaUGUIPkRzJ-I-RLaBqtUw_UravlMf6eFUC-sTJWFrB91hVnBqZDMlaJDISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuijZi5CyyTBLp7cLQHX-s5xnQx7XMUcQ4mkia6x81L2M-VmL98712R6sD_04GabiaHirdAP_vYY9NHCp3aXRzJoWUczvPeZRqIVo0riMLFEvz78225vJRn--civRk5RPKkvpDZxv4kXoUqZA364QkypF2dbjjCVd8EwKEpFPtt6nNRgtVUGyYBrQkJ9BVvcZ324j4YARJJRSrt1-L-f3DQ7opzJtUvyhJ9CRse7AWf53j1w33KpNWPXqwJZn6idifS75sPNrVMGj6jRNZPi5Z3sphaXGF-s4Hc4svi5ryH4Svy9ARxUnV5gLmpTK9m9320S3DxIsQVwt_CjZfVjnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=FpuwbBSR9n6Q2kAtxS9_FN0h4-lF2UNyUEd6KeDlMEOeUU9vJ24r2FdpEJOxwZQQobCS6q2vXKACVz0WJiilwrL9wQBxdJcd7kerFPnwyv9tnMjbhdP4vUqnoVdEX5_okrxAsDh6UpbT8GVimdbGmJqoA9KjSVvVQvr5tO4ohbPnprHrVmIki_U8ONxQZl4txxqbCLK_zffP-_XdZ5-THtjTujLzES1J7gzN6J_WXM56goklJgI3z0c8FLRgKiyBniQgj3kiW4Uo3irM5D6dZFvmDrkcX2CzJu1nuQSvlK1_nk3ndC3L7UhQMnRYq1Tw5fQCWDFc3W8lMAal0SygKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=FpuwbBSR9n6Q2kAtxS9_FN0h4-lF2UNyUEd6KeDlMEOeUU9vJ24r2FdpEJOxwZQQobCS6q2vXKACVz0WJiilwrL9wQBxdJcd7kerFPnwyv9tnMjbhdP4vUqnoVdEX5_okrxAsDh6UpbT8GVimdbGmJqoA9KjSVvVQvr5tO4ohbPnprHrVmIki_U8ONxQZl4txxqbCLK_zffP-_XdZ5-THtjTujLzES1J7gzN6J_WXM56goklJgI3z0c8FLRgKiyBniQgj3kiW4Uo3irM5D6dZFvmDrkcX2CzJu1nuQSvlK1_nk3ndC3L7UhQMnRYq1Tw5fQCWDFc3W8lMAal0SygKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=rkwrgD7FsgURmRNTCFQAYoe2uXGaC7a_fhbwpTqw1aKLep_LWzpiV_6PnwmpJoILVmNaoOYnosDtaMc-FKsrw3oVkdwILaguycVP0Wz9QV_2zubc34I8HbJEQgV4b7_BtcoIN2xAaAfpq3j3jOrRPnP3x8whyxC84jcI0E2LB5WiAZRrsSoYZns82imaAlaOdBAKIk3UVB7hDkQrWU65Evxzw6c2UKnnHv4gobbgDlST0RB_nrkMEBQEr-nA0z2p85y7-jONgRv_uwlmRWapw2so_gb2LZek5Y6hyWXKKu_oZbvhExQsJZsCqf6BQtFKsAHVmooA3W1u2MOCB4CNnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=rkwrgD7FsgURmRNTCFQAYoe2uXGaC7a_fhbwpTqw1aKLep_LWzpiV_6PnwmpJoILVmNaoOYnosDtaMc-FKsrw3oVkdwILaguycVP0Wz9QV_2zubc34I8HbJEQgV4b7_BtcoIN2xAaAfpq3j3jOrRPnP3x8whyxC84jcI0E2LB5WiAZRrsSoYZns82imaAlaOdBAKIk3UVB7hDkQrWU65Evxzw6c2UKnnHv4gobbgDlST0RB_nrkMEBQEr-nA0z2p85y7-jONgRv_uwlmRWapw2so_gb2LZek5Y6hyWXKKu_oZbvhExQsJZsCqf6BQtFKsAHVmooA3W1u2MOCB4CNnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amrfTm0IPCK-WvBwVbvCtG5nZ31TlbNQlfRqDS-RBsgqbxv5UNzjtNWaRwwab53r8lFO5JeCI6PHtcMZjrzi_r6YL5MmUg_a9G8lW4JnpQJZ48C2mWbsc6Lgh7nSVoByhObOy4j98QEeGo9f0Ibdh_zH41R2uXdw0-_ShWcygVYj7DdMxgzMIpVXB4MfLbQmkzyqn3rNvF1ycBnuBLAj_jUYTDYfLnr2bQmKYvc7jk663v4YIjhKCufYJ4EgGB8ItfFZAqSX9MJKMIe_CNSuM48fXZVd8StulZwKn58h_eICfZnmTA9QGN1LsZlHRSobMeFCa9Wjpw8oqLEHBegt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csvKt6_SgKemmg813btedEREOU9IAHUxJwalY4_VfPmgCKMAge-eSyaiM8XMzzRP2ZCx5LDFO1UFGZxf1BfvzUH-VtzxwkR5lE0dy2MGetmpvEMXapIb_ezYCpJEHbu1a6AaqOrfb9TLMEzo40uhxBU7LNvqxqHDefJcq3IlqYAd1cBd0fwrX6QKo6W-xBNIV4BGaj_-6Lm-M9dsoOnYnW-zQCO0UBIzFBGkhKjdogOEcmyd4cJE_tqImC4RXzQ15AHkIR0PMNWj6n9UhKNzDRiYG8ZniS4gAOlXOtR3ZVCc6Z8w8ueTChPZRxRk-y7M5k2d2hIYPo5N2kokc_y8xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=Ch859g1gmtJ9BScr5XWs5hU8R-de_p-gzc4E_yCbJFRD_tYreM5U9FCnf7akVilfcvII4gRwKlsngK3R02pnhIK1-903-ThxlQk-NGtTqxWX58Y_EY4Ta95m_DnUa_IFwygjnSYb-lNzOe7fEYsf29hCASGypCzz_fuEqziUO-QPtWOGx28PBMTV6aBAuFae3-CeEst7FQGpWOt3QC4USnLPyXho5OS9tKQ4OW_9nC_Zt934-FDVvsPDoHEN2ZLMCZHUOu3E0BilKIgCFuO0ctfRTbhhKtxsbav_b2WWFNlWFtthuVaFpq3Ouh3TRDbLKyQNse7xRgQkx8jTchfaBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=Ch859g1gmtJ9BScr5XWs5hU8R-de_p-gzc4E_yCbJFRD_tYreM5U9FCnf7akVilfcvII4gRwKlsngK3R02pnhIK1-903-ThxlQk-NGtTqxWX58Y_EY4Ta95m_DnUa_IFwygjnSYb-lNzOe7fEYsf29hCASGypCzz_fuEqziUO-QPtWOGx28PBMTV6aBAuFae3-CeEst7FQGpWOt3QC4USnLPyXho5OS9tKQ4OW_9nC_Zt934-FDVvsPDoHEN2ZLMCZHUOu3E0BilKIgCFuO0ctfRTbhhKtxsbav_b2WWFNlWFtthuVaFpq3Ouh3TRDbLKyQNse7xRgQkx8jTchfaBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5GvI8J9mwNmsnIOUptIXKWIkRVNZyhdjAPY0F8HwAg5Q68BUP1SPzTEYuvbayIfermijDCzJImuXwPMkzkt3YbfSvwTQxCQyQ1TTMK7wOlvAyxZvrj9kv8fn6zjwg3UCfSECcPy7WfGfbzuph3bI7_z31r3VW60-J55YMubDA2ORc4vA4rxS6YMoKshEHDFEFfjy2XvZwyl9DND4wlBSxVyT6umobvWowIJtQKdUQrxJ6sqKVo9Zp3qVV_CYj1f7-bPmE9n9AcUPE2erH5jQFJjqQfe1KKSZQMmFQhXx8UN9O8p0RxqIF5WJ4AfEQUqdSpXw0LT-SgGWm_CZgsPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
