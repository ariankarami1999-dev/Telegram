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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 00:38:51</div>
<hr>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq936ugl26sbwnyE8iB79fB7noR5SqHorlpTfEf4JWFcR4T8eaoDeYDG48FmljMzDqMRdMtFNeDSPO-OZuF9ZWCiPlunWVwEFQ48jb_HekziTxJDe8_xWOvuAoKcAPb1J_lZ3JmWM3F4ZXLbEccpXTzdxcw3O8Ykkk6FTIjNQ_wNYvvaawlMT0YMXXFwwD2PX-MScveol36gyZ1r1mGap2XVtIqv0MwGzLZvWo7DsOligRE2Af1fL4zaL5yYb37mvqLPOC-y3qfiEdAvsU--D3Wn10-8zc-pgGSo9zt1WJVytyvxbqwwYeia-8BK0elWrmaO8DheQlBRJhAKLBC24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvsN94JSKqsljx9mgbDBRgV_llqF_WAaZnBseHlLELQKKJ3ws65dQqANeVtfIJlnDw9bUkamsXNJMxX4eg__jKNzrsB0NVBfezZhjqJtYhR-RnVEK9Ckf5mA_EDe2PbsO1jc5aPs8PmMOp7tRRFSZ96-ank0yI4ROcmu4mFjI_To5cjVmnd47taemzRA5xmbn_UiuMpRST9nNDkzN5Xvrk5AnGgzG21bPRm0MWUsQeVO7Io2NPo7jATmNBZmLQjg97FZaJOthxu6wfddjrAGzlSlU93BlZwS4XZ0OI1MIJCBBo2EDJ72Ws3dw1s08pVb6fNIhm7-33CJDgroWH2PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPQwDsb8e5BbH1hHBk83pdT9vAG1x79B7h0LBynwZ8NPcttZT5t3RZopf3hiWBBIv7zpMES_kv-3AWxgm-ma703Uu2nAx4--3HQ5b5KK8QyprJYZ9Ft5P5S97-VAKMwUo-QsunXTOQ7KcmsjlmuzbaVXvSL1sfB4EfGoOvbt6jf_AiZTzFWg1_G0QFq4aDz7AkSXX1ynXd6PIOxsZVA2dbUQrB4xdLPIEoldADTVvkmYTF9u6DhTZmrAR6os34aoVIF3XBtbtST4oRCo3oUSJlUc00N81jLobAJ0zjLd2Nj7V9Xw9yrxeItMrKQxrMm4ynMaC8bhmRAJY5cnOCQO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc7NeffMHacldACBXwHgF5KB9SWjsA0sz6BxNQeeGnJE-jIxQlN9t2ErNgCfzeUItF56PxYjnHLcBuelWVdoGpaz1osWXqIdC7EfeKEE5uwz1T8dONu3kkzI1TBluBsnmvHxLKqmiyauifcRfTzMUhcRTWmaWynDqTor0yBJcRh3JrIXAu8Pc-s0wEi7jxEIWhYsYErpmZwhHuX8CYUWGs8mQdF2qt9y-Oo-5BgiVAFlA6afJTyFra4MDCbMncbOYi8b6pcPSahlaJYSjrN77QaZhCM7H4bMRL8PcC3kVzeH2v7OI9iex9515vHqU-mH0Rvt7oZ0_c_FYX-z5VjIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrXoZAPK08RIdQIG_M2QFsScHv5vwNulT4d-olkXsNsYT_kWdRU-TE6KNUoOLSNe_wcmi1GpwzzPtKcazgEuKy7Mnk0kioyMsuNCFasmTAeo8L8p5JBqWCCm4cpVlSFIoFRKnle95u6PKw8qoCd40xF3x3JkRsJNCxkSf0QbxQXaScAxv4SDY4CI2AXM4XFJRRaJUQhop7_0xVjJhmow9H1cTPIpS1MdyFiybQKTFdVFF0j3T-0wvqEwFoOTR5fMjXs4qmURCS9VqLHEUxOYriTaZ0brZcfeh-WYBwi8Y0OqZS3V09_ZZTnI4F9XSRBxSGS-93RI9F5p7j8BYN7NMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Qxi6kBaGfPqHQqrtwxcX13kcvvMcWHo0MWoZz5Z2Q4cS4vIVZgh5mO_KRh0o7Dob7_aG6GpimO4z3Tb7QYPYcGT4XLV20fa3X-urJz4a_aecSQ3vkkwd-_EwffQILkslQwr1cXRp0F70Mf6HetEvmdlgtEbonYea29fIgwBc8nSB3EZ9Yf43xWFEZCEEzdZQ8n69i-zaKn6VUL5Qv8Pe1EAFeCdnWBzKi8N1Oo7xHXh2bBjIksClokd-M-m6cSaA4cszrfe0RU5dou4GOMELmOn5QBOcOTpH4hb2xFlGJ6l3H2_vhQF78BhoOfFFGwQ0KY6Mk-WoNaYgxodVh5pDpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Qxi6kBaGfPqHQqrtwxcX13kcvvMcWHo0MWoZz5Z2Q4cS4vIVZgh5mO_KRh0o7Dob7_aG6GpimO4z3Tb7QYPYcGT4XLV20fa3X-urJz4a_aecSQ3vkkwd-_EwffQILkslQwr1cXRp0F70Mf6HetEvmdlgtEbonYea29fIgwBc8nSB3EZ9Yf43xWFEZCEEzdZQ8n69i-zaKn6VUL5Qv8Pe1EAFeCdnWBzKi8N1Oo7xHXh2bBjIksClokd-M-m6cSaA4cszrfe0RU5dou4GOMELmOn5QBOcOTpH4hb2xFlGJ6l3H2_vhQF78BhoOfFFGwQ0KY6Mk-WoNaYgxodVh5pDpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=SxIg-Ti3-3tdGw2PftLSAwmUHfk31AwxznzYBgkQ13aXYI-PzGL88fd0s6JI5HyHAK5U1Ar5a65KpdLQ5nYvj1YVHNm06JBvUnhNgj4PxOXLP0bhkv9j4XHzaZnBXnmEkzPbnOVO-gahK_PSBruy7UFWlW1kyWOplZFhrhXgML2eU_bIYSiC-gBr6UcLrS4dn4ToLBcIC0Pg02QhdkmK-U2cJn8oEeKL29wBRTjyzuoTd2wORMzuq7sDjcM8U1TxveFXNFrZbhZqlqxlDXRaXICNNZuB0pwGszSJ7h-afGolA8YGNBBZeFiJ-HYK7rxd3hk1SWeM6NHxvpOOB0rArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=SxIg-Ti3-3tdGw2PftLSAwmUHfk31AwxznzYBgkQ13aXYI-PzGL88fd0s6JI5HyHAK5U1Ar5a65KpdLQ5nYvj1YVHNm06JBvUnhNgj4PxOXLP0bhkv9j4XHzaZnBXnmEkzPbnOVO-gahK_PSBruy7UFWlW1kyWOplZFhrhXgML2eU_bIYSiC-gBr6UcLrS4dn4ToLBcIC0Pg02QhdkmK-U2cJn8oEeKL29wBRTjyzuoTd2wORMzuq7sDjcM8U1TxveFXNFrZbhZqlqxlDXRaXICNNZuB0pwGszSJ7h-afGolA8YGNBBZeFiJ-HYK7rxd3hk1SWeM6NHxvpOOB0rArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=h_UTwXMkOg9mF3GUYRTgQyF_bh81lUQE5MP0grfbvJ28YG9_xNdgZ7Go0YuNE7d1cOn8ng1UhSvf6IIsGly7vOdDXqtV3lqd0v24oGcNxyKLtlkml_64xqgryE8I6ddBmkWpYufg7kX-9w8z6Wv2_zV3GRIOar08EmEMwoQflfN4J_KsudXFAlGLiiNH3zSBlRK7J63la4Zzf4TcIR6TpdcOcbDIy2i3EDilFUx8TY0GkeoXQFWRS3x_yqr2zLBGZRyymHrjZ0SnEteUgVctLBLyECmlO3W8CSy_ysm0SF_hm_rXhz1vA9PhRNqLwb0EJ4GLhMiU4T1XjbX8RiMxwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=h_UTwXMkOg9mF3GUYRTgQyF_bh81lUQE5MP0grfbvJ28YG9_xNdgZ7Go0YuNE7d1cOn8ng1UhSvf6IIsGly7vOdDXqtV3lqd0v24oGcNxyKLtlkml_64xqgryE8I6ddBmkWpYufg7kX-9w8z6Wv2_zV3GRIOar08EmEMwoQflfN4J_KsudXFAlGLiiNH3zSBlRK7J63la4Zzf4TcIR6TpdcOcbDIy2i3EDilFUx8TY0GkeoXQFWRS3x_yqr2zLBGZRyymHrjZ0SnEteUgVctLBLyECmlO3W8CSy_ysm0SF_hm_rXhz1vA9PhRNqLwb0EJ4GLhMiU4T1XjbX8RiMxwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=QgRJEFiQ18nCa8i3SCjwjgKVggbRbHugPZaV6oAFP-d9awprUzpw1PmFzHYCsbXmdqVEEQQ_kcioG6KNk89uS60_ZVqA7r1yFzk4jpfa4-YuJFLV4HlljRRQze2k70ZC64D3seyjaT1ntq39c2qdW1YrQE3SeVDIn38UHO3AiNdBjhr4ihNq_ZyoDMUk9R7-RFXeuPZgHD0246mGRZq9JRbFwKD6OBskJMwVcomIHrbIGrnabz3NyUClmqmk0g9CLaaO8pMo7WQFKZ1beajnZ-xc3ZRvP1K_CL-Ayi1gJolRuuE8-ig50YlbqX1LAbEolAG7Ua1rWw6FTI_dwXr2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=QgRJEFiQ18nCa8i3SCjwjgKVggbRbHugPZaV6oAFP-d9awprUzpw1PmFzHYCsbXmdqVEEQQ_kcioG6KNk89uS60_ZVqA7r1yFzk4jpfa4-YuJFLV4HlljRRQze2k70ZC64D3seyjaT1ntq39c2qdW1YrQE3SeVDIn38UHO3AiNdBjhr4ihNq_ZyoDMUk9R7-RFXeuPZgHD0246mGRZq9JRbFwKD6OBskJMwVcomIHrbIGrnabz3NyUClmqmk0g9CLaaO8pMo7WQFKZ1beajnZ-xc3ZRvP1K_CL-Ayi1gJolRuuE8-ig50YlbqX1LAbEolAG7Ua1rWw6FTI_dwXr2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-Xls6dvkSnorcL_TWPVZA0NOfPs2JEMj0nBuGU28oUPpCkcKNL-bDnuJZ1_gZT1g9FgVRshtcUeQBm11VRhbLOiADWLaSdaGuqgbpmLDutpPldVtYzdA6tKshb7nIqKUWPCbXyD4BJMJkfmbtSwqmiWgC8pqCA-VjqmEjcPKK77Ow5dNv3RW5aDZEnpO8ceKbWd8-MjNnln-pkLF8WXOPRvsA-Upyqyl9g86aPh7TyL_J3oNj4m8Wp80Ajhyr_h6D7XLTk-h5FTmMc0mxSjV48B0-x1lOZevq3NtraGrVgUpabrlZjCPvayrMXqljqC84VYUnXveaoEn45wypNUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCco5FRb-DzdyvL60kXdFrGhm_t_452Bt_JpsEG8NdJVly7ppwouthtbmmXi_CTXW8wmPuLqH0RU7ILvfYmeG0TLtUkkoQP-K270eUo8xwU5T5jt22LI7XQLQetpVcmCzZUVwudMCuK1kLMe0IiXD0c_-G_9aDTS-Wu05Lswq2sC2xPu9XAmJdtp44O9bVaTtdNZntall5w2RsvuKxH7qB3Y3_P7SL_2-yX6L2Frjf2_tgnkAjSq6LJFOqbi_Aa08hgCGMvAiPFysxwTgW1oETd-ur5SsChUhAoyAw6r2enJvitneJiFkxQN14DGq1Y6aWFGerXKLo-mNnfiMRrRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCKibkXQYMPS4TSIVljfsuvEVVil3xjlc8wO6y070pFO5Cr34UccFWCSa9VJv5-rpP_fPrc-08tXfda421ptZbQ3ZDcTyxCoIfzOBiFEdaDosGqgcuxnaQjhRpNNkS_MEU4LIW6kyW8uCnoNd0ZNMyX1AenkAnJCr91Gt6e3P00dgbfSbhDFx7zpRPGVbF7CHdA1nqFJrF3Wq3Ud88Pg8RsiJkaYUGDIjKtVKM6R29r_-0Vhntjz-Gbb6KgLTvEOecjbEmpsz7O1V1rk6kDhQqUhLlFGqvew9n8b1iCQeTKJnmGczzDP2YpWF9dDOzH9HppTdl7fdfmVWMKKXR1zPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uUHtuMBFJk1XaMSXYeePRcxnGMAzuwYwsjg9cKX8UXcbGMXiAefxbrHDmiQhAaADkL24Hh5yCOYF18LvYVje0opRlOmxSQTQ_EPKkSnXxXi8s0aFWpHjXCxH5TPU7WmI0wL0NrqOpKT_VAfhLpGa_EKMxk_zt_VYljVeGWciroCsg1sVycvFwG1cyaD4l9tq06qwshsoapLuQ2atCwJCko4KY0HWjlTJ_IiTgM_uUoGCX-QhppNylAtSmYjfdxm9kZPZqMZFplk40QCf4CpZGwPjf1b4s-HEjQwq-_3xtfh3tYOCMas4eKLwp_DDpXGZzxfjICRYTU89klkrQwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yso5q690B9ob3t37wwUEWitP_BTQBbDmCtM3nVRp7aXkDACUfCbIMQU9FeCV_aR2BUtrKNQemLbZvkqlFtigFSLE4mVabkYWT1dLJWOQ4Uywm7pgCjTJ5aZHmmrzMrQvTnAhOgevNUoJGmdllqwMHu_X7Cey8amic0-C-PrxAI-cHTmuiUNCWlrplr01UEkdLucgtCke_Qa9ZGpKTzKlmwGbjuhJMcOghE3CfICXCPZjJ6vnnjPoY7OQSO6jh4ijbLiN3xp6gvXtdv8-qRX4bVhNVb-G1K3fcJhEmRyQCaLa5OWJFZdXT4BjdJhYB2KuIbPNoWmhT5wXXTzGyF-jlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFGBVdomBvTtn6LMJ5tB-9itsqdne6UrglQKjzAG6b2dhFIEahfunlSt1CIlpgSRpI3CNL5OzFY2X31gPOS_sjaQ7jOEEIJ7Tec7V1xkE1LSBZGtrzF8vpEcT7YteFT83nFW-rn2q1RuNdXNa8HbdL8_hPV2DhoKZgMPv9i7_UteK1YaceuKfWUa2qygdLLP1nWboCoOtdbZI7znLQktYWGQkXqgkkIQGet_HGpbZsAKXwbiCUdDyWzHW61BIwtilKu_4Z4FdIjl70SIBQ6T6ft1ulEQoFY8Ii7dWu1Jgr4SoFkBVoj3SQvusM8ctGHB20tgx0QkeKyDHXFH1FKgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD6iVpA8TKuZDY-bU0_bxy_rJtL1T4QUVl0_nEVZCp4Ol7MwvgOxw2QCMCkHvtGbFaoREqpQSzx9LGtMQ7PiRRP3Cfvctkn0t4D9IXdxZoGhndzphY3AEcpCActV2M9scrbASZB081h9kMRSYqhWY1c-KGCKGfBm-9pXl6H1qiMPK07PKvzk5ZvocYoXzexwMfk6Tit6MwymIra6a5ez7n4dx5QcgbfQWM_k77rf9-zj5omsLjMJbhc2b7UEiz710YWF6AYzGeSm1XEjiYqzbOYmos1qOrH0Jk6AwgePK82dkYduh5w6ayAv02FB-p63vBachL2vensM6q8tt3J3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ZwJmFWAdhNcFUtsDQtIHC8wDh3ebbDmKvH447P_ot0ImDy0XsJgAi-Vma_9TnLJ0RSN6wKggGzkea2Rpd-po0izWyzWk8TjB_yzvqxz3Ap1zm5zxYHa186jUx90AZLnRrFh2G1P4eCqAR1Be1kM1WAl461bnBxgd7e2V3A83xPyHzF3bC5Km6a1geWPOmkzyRBqx4UWkihJ0VS06LtUERD6mCqYMAzvl_uMltRocsTqFPyZ3rBzexY5gM24a_pVo_RUuCJo2kpIQbGbaMs2VoQtBlLN_8CTBG82CfM3Lo0ATbIn3i6zqpelowuuZ5pUdDxyOeu-CrLzwox7LRR9yhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ZwJmFWAdhNcFUtsDQtIHC8wDh3ebbDmKvH447P_ot0ImDy0XsJgAi-Vma_9TnLJ0RSN6wKggGzkea2Rpd-po0izWyzWk8TjB_yzvqxz3Ap1zm5zxYHa186jUx90AZLnRrFh2G1P4eCqAR1Be1kM1WAl461bnBxgd7e2V3A83xPyHzF3bC5Km6a1geWPOmkzyRBqx4UWkihJ0VS06LtUERD6mCqYMAzvl_uMltRocsTqFPyZ3rBzexY5gM24a_pVo_RUuCJo2kpIQbGbaMs2VoQtBlLN_8CTBG82CfM3Lo0ATbIn3i6zqpelowuuZ5pUdDxyOeu-CrLzwox7LRR9yhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9aOtCo0fnWWqqPlrSGpU0nvseGjDextdsq6lRr5ZWWHJUzO_qzrRAHi266eK6ETH2n4ngLW_zbcUK8exR6XK118IZQAiTBP_FTQXw7EoSh4CzQaHPQ718qvcCEbHMOZflKZ2es0wGMpmVPJ5E8LQt97ENTYoQSFwMzO0STNjvQsdm6_JBSV9d8if60_-aG_lfH6fKZBiOog0UksbPle1SgIdUrOibmf2PiwXINdECkFI57rFzVWO4wSrLsN_DiSM9M1viaXRiHF9IF8eQG9KS00bL6HZ7ytep76G6EPDCJyqHlhYtlnW0WV3OGPPoem_ds-2uesI8VYrisk1GwzCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWdNOEF4y1C5Qn_Qd4NIMggn_awe_stnj4iFVlQ3R-U27eEGYhk0J26eFUpLmoQIodyouov0MML8On8XsaP8z8bjB3hDLIiIt1-Aa2uc4NsqQIAeLxPT-012I1U2bY_gHZ0qkneYeeEAm1UmmqoMubw5JkLjO_9NhH_Atx2_q8ISkmNL_aDEd_-SogAdspUdFwNjA8G8x2qIi6UhyVealB2IeY8_dgXhdvOpYkSfxvMXpDofFI0ubtW_MGtSzv6DltsNC4F-xTPA5ay7UucI-Qul-rGBL_ZpQMCh5IfzhaqCrFD_JFfHTQ35NMw-30G5qatXw83v_9gxcA6U9Gu6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDN-0xocYXFPM2-iX8DdbyjK__q-Yxc0xv3BtiAr_zcs00h29KY4djHrBlMh8oA1fkHaj5DGsVLa_g34A0pVnM1-5zb_QdxeV_GIL32bE1mrTw7fyKHPARInwkWjfobNSuidyMUwrASRNxQJcEpCmvYI9IvBvjV9W7veb_6BHDWyk16nIhX-hagatsIZ9SzpF5RgDTXt7q_dtwvBWLlHLoShS4k_WE22geuSZoPlFIne-85lZfbWXDIV91rQVmdFSzwGvExmkptdz-3QGUsdwPD7RWwdbY_D0kIJNEJ-2QcI6fa9xIJZmTEre6Nv6pAoCjT8Tyw_TXGGH1ijTIYxwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISqQspxtRBSMzImH6feD_inH3JA1xkiIxET7FB4wYj4XgyAbfUyKVhjoSnUNz03hreQywCrK5hQVkWuqeOT-8KKmfKJSdMxrgP5gv8AuX9J_geUZLIr0xuXYiz_0xZLF_bm8XOK00UaOkFq0wayhSpO5XweRokb0tPGGpyvziI1Z56DmqMzGFHcot5CW_PHrRGQAcvty-L3r3PlpJdn55xl0W5TjrBl5czQdzC1ctwS-YopWanGI6VomnKg3Alk6v0cCM4n6xDjV9mlFnq9FolRt74A9yBqLe93WAFKnQpfG0ZqGliZnp4eKdF1J7rShJ44zmM7frP1WW1C9CYaN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAIqhoCQxWZye0_emkAeIWJ84lIqQXLVkW6MJxNHyHB5eatwDt5qAVFx4ipRmTMXbbEaAx0fyzyyoq3t5gs5wCWl9UCuuYdtQH0dFbdusJCyUwsZdIDmubR7oD7G2WMsoaFmR3hLj9yXJL0_duti7LbSFUwVjdhK-rTSIspTgdypbr9Bbl1m6YA3wrkxr87dZIKM8TYKzLXqHuBiC9fmSyxJvmiO3Ud3RXJRSZGaJtKQR4ZeZcl6lsqC-CrnAXxB8eIbNsK7mxBaqUI0Iil1_5QtC08ICCQoUIFzZGXzzNy8HhLdA5rAaV_dzzAaLd3r44HvtcT9b10E5Ob5-RLmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Si8fmMiC8aiq25ONb4RhF8fIFz1JBh46zmEey5S2SS4FUdimRv9547rR8Yah2yguk8dSq-TRheenc0fTXSaI7c_lftTbLHPZAYQGmiZRCqbtpLtYouYqg7WiL1ZRpovZPp7O8my1z8pNwsSwc_0ITnZKQsGO1dFCt0P5sUtcIX6jf7Rlzpsx_FTIAU_2OWlzMujwRHGQBQ3ELOb0VoQYQ3ztpO8czA4ykkCavrnqtJJM0YJk56Z_Tib6dqXsqKdyd8qvGhQBhzxB74Tf-zV8ZcF6jwTvcupaw1t2JUyU4_JoznDK7xEyQO6dCWMr0COgVFOrNdEYCWyXGENAo2ohyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7jSZ0RzcGZq7em7GwlYd17T_LSSwD9obp0GL0hEgL2YraHicroq7gvxEEn89IJc5XqAopcCm0AdOWTIHBwvWADzlVTv3ZB9eLWm7N1h35N9oiXW7PXkdiTw3GeVW3kGaxiJngQfOCrTq8nfKM1xpbxL5VqIJ9H_T5N0YKMkiUy90y05LKlaK2kmvl_mWySYBdrL0BGSzxmr4gqh5550eaIwXaPCdxMwgzsVHR7aS3xqNx3xD35K_ICV3TpSZHRlAaHrCv8r_gikG8AllyMA4fepuqFFVhBiFxplPlAq_JixaRbWGOvGewq0_N_Z8h_EN-pEgPvEx8WZa7gBc7EEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OExW6ntjDvblG5RNyk41VjkuuutKLMo8WofPNdwR5kWYujwl5WMnUXMem358hZiVBajUmRbYylGliweWvoKm9s4VPPZg5s5vwwb-KZPOuGBI_bO_yU4WZYzQXojVRCnhEBczf6ikifhdkfki8C2iGRBabBO5bn1NqaONsRRoae00OO1-JUPh37b8pELN8fJLS1-WIzkAkUcVkzgc2lua2PYx41gxXX_c66PtKPH2gpI4cZmjNdVYqAIpCGhtTzBBcaDDNSgrBx68hivto-CdsKIpclS_MAn-pV9BBcv9_H4KJqxu9tb7rjm3D9T9iJzkIKdlJ3lz4GL9zpbBPJHmyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=iCw9_OsTINX1W37YK5i2KM_AdwhN2HowGObmrmJ2aWF3rk5YhxqGE_4ZFBNfBXw6nhDgldw0PgVv8djKzaFoebepYWGg-o1mFEO-lbTSXsxNKcqiT65reH9wWjkc0eFfK31l1MbNaivfz5CTLFjz3Rx6fuHWXbpC6wtxJBrN5gVcOzdM4nLeYl1Kk9u30FCKuPeQg5AVHZH6cYd5wyjC8OCxNtPlRMX0nAv2SQ0gAPtK08pxKEpijFZPAHEb4CKua9SwyjA8UzTg7gW-o0JXNsBN5nGn9YsCbm1utGp-HQgh6qn2F5OC6ocwZbs-7QaAi83EEzXzUzduQwBar-spU5fY7CKMJaqlTcthI7J4Yg0l3c2L_wZ1AVpJajxvK8aC30DjDcudznHz1FHBvBZMeUrQeAId60ZGV2rVjUEKorS1QQcfQwIHc66g4XI0WPgN-VfmZngHUoOVn2hu7-epiSIElVpw_3MiMua-HOO6wK2CA54x6ivo363rFUHSF4bjGmD679UdFiafp6o6bj1w2_FQw-zefPd2qncK0Tp7D-dwuMtrou56obqe9KHxROI4gdEE4IQW3GbuzatugrWwsGj71W36tdFjRs46n8GtgBq1jRCTP1jzNqOjItZOBiQvJ8hGWaVSDtrfwp6bVMfgw-bvK1DcMq5xxzZ2R2A96Kk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=iCw9_OsTINX1W37YK5i2KM_AdwhN2HowGObmrmJ2aWF3rk5YhxqGE_4ZFBNfBXw6nhDgldw0PgVv8djKzaFoebepYWGg-o1mFEO-lbTSXsxNKcqiT65reH9wWjkc0eFfK31l1MbNaivfz5CTLFjz3Rx6fuHWXbpC6wtxJBrN5gVcOzdM4nLeYl1Kk9u30FCKuPeQg5AVHZH6cYd5wyjC8OCxNtPlRMX0nAv2SQ0gAPtK08pxKEpijFZPAHEb4CKua9SwyjA8UzTg7gW-o0JXNsBN5nGn9YsCbm1utGp-HQgh6qn2F5OC6ocwZbs-7QaAi83EEzXzUzduQwBar-spU5fY7CKMJaqlTcthI7J4Yg0l3c2L_wZ1AVpJajxvK8aC30DjDcudznHz1FHBvBZMeUrQeAId60ZGV2rVjUEKorS1QQcfQwIHc66g4XI0WPgN-VfmZngHUoOVn2hu7-epiSIElVpw_3MiMua-HOO6wK2CA54x6ivo363rFUHSF4bjGmD679UdFiafp6o6bj1w2_FQw-zefPd2qncK0Tp7D-dwuMtrou56obqe9KHxROI4gdEE4IQW3GbuzatugrWwsGj71W36tdFjRs46n8GtgBq1jRCTP1jzNqOjItZOBiQvJ8hGWaVSDtrfwp6bVMfgw-bvK1DcMq5xxzZ2R2A96Kk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=BpYkwX8U4pT4Nlobc-3iJJI1qqhGz5MSdzNV9JQRALH4wBrjn7L6UwntcSIMr35yN6rQJBaJdBVM2YL9RsaXxXEmAQgKPiPqEv29EDW9de-_AkfVFnLfKICb2j-3t_XqW8qGqnZhZyba_hN6-tF_LZFHf10mMNokkF_atOLpzRfjetIKHh0zOu3OV8WvjaVNur_ebk21M34wMjUGkGQnAtk_z0VEEYUHcr6SnRpDUFXoog25-nbCJ6_-LHeQggAsW36z0Sj9I6qx3xE06HnVt7PMvBPhKaT-WF7Tlin1jVrmgqUHnNJBChTdUyT7fqnhC-j9-QZHralhjpvcV_qnkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=BpYkwX8U4pT4Nlobc-3iJJI1qqhGz5MSdzNV9JQRALH4wBrjn7L6UwntcSIMr35yN6rQJBaJdBVM2YL9RsaXxXEmAQgKPiPqEv29EDW9de-_AkfVFnLfKICb2j-3t_XqW8qGqnZhZyba_hN6-tF_LZFHf10mMNokkF_atOLpzRfjetIKHh0zOu3OV8WvjaVNur_ebk21M34wMjUGkGQnAtk_z0VEEYUHcr6SnRpDUFXoog25-nbCJ6_-LHeQggAsW36z0Sj9I6qx3xE06HnVt7PMvBPhKaT-WF7Tlin1jVrmgqUHnNJBChTdUyT7fqnhC-j9-QZHralhjpvcV_qnkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY06QuyGUe6Wyw7NCWIZXDcf5sJ9yt19usg5EFKt0jO2EfGAzos8kuimdPVFvmRhI4nuT7ophAgwHb8LE3GwRNBOHzNhcevYNMCaQlbJl0al-FHkbjriKdOTpgiORZGdLu4Fov7t1ExtAEmFv8gghxdjbaPf4whw9IeCcL2W99PjIzzAnwIinQ88InzS0dnVZDv0cp-ThpK9O1a8r7aEeZs7fswufMAyYyXZz3hY0c59z8_40Jw_yhk9x4rYiUsW1hpESnLkcW9PoYBJsCvsvA9FoHt3P8JxLQ-mAWU3YZP94GjEiuofXDWBx850GCv80pn36ccdYlpoU0jBhQJuPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekeC1zISMuNS98YSmLjwW2i110l_ImYWOyosQeCf8sxcwvuk8qwr9xKNTj8i4fzC1FgEsx3s2lipL3zg1YF9tmamfBn76ptMdIiMQy4b7M6QN715ByGupl4KoZ2ZTfv9DB_cEnzTKyFMAxPFYvjemShAibLF-W4CdgRmojoI5Ij0RC4X266oAxSCngwK2NfKHe3Yzi1TJ_y0_tz8FQp4NG4PDz3caSjkzQgUBJq5OZi99Bs1f66hgUJyq2ebXy1FeuAORhnbkSbI27yuQ1Dxikf8efvT26mS2Jsymt6JewpkDJYodvOEP5O11HICb2xiAce0KyOdQpTJd8iPvVm63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLnJ56x82vyy_0WV6StyjpZcBQBucB9rdXeJ7AMxj20W30bXNLoHhXg_bnON98JAIKFWxSPQuhBiQshCGDEud4kMe9hHWI0XxJkixIiJD355yUdUSXzNGunJFvXC6HIiDqQz1Ir7kU8la8216bgaNqOMfH1qoOPvyrr3Shi6U_cH8puLvqd6ldENTsn0u9BpaAEgL6MZW8Y6WXE833tZuTmHnb-KnTBb0wgtHrHrjZLIsdxxx6F7bkcoy6jcGuh9CzPaz1XzPZi7usUxaIRWjD_BD9k10mbz0IEgJ1R6QVQNkQmmY90NOJQb5Bs2RjZwwWvGvI7Eorvy6p3EFPS_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG0qEIYawLu1B1v-t4YuPP4vOh159DwqIdIW2dbU-0XfMk5ezxBLFVOKTnOV4PNQbb4KTmYBT_90v8zVbdgUkWHlO79H43x390MiJ4He7vwTPeJk86PN7Y7pqzPNuhgD8iyasVZq2S-zrmFVfb3c1OCkdXSandTkTe_JVp6apTxt28aecqyeC14XreksgC_zzlXV15RG8be-g1426vchjPWqNJ3Eh9HzI2CW0PLqJd1SMfHRdT4lT8hnd2_bZJljfK5Opx8vdcEuLHzXiKCqGHtdZ7xFBROS0uYSgZpUDwSWT3UcS7GNYcjCCxTFtOhD7v8wIB14mmFw6dE9Imuo3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paSngHPevhIf2u3FJ-EwiK-Czp3w8vJpqbVwRL6JVdF6mqZ6kkDxmPc5VDUSjSgRinX0T-8AwlZz4-_9eyxL9RDIqSTQlWIMHBqrHRkLgU93O6eejZ13f25yrU4Gf4aCXiFKxq0zfCEx-EQAhTXC_C6Qxyrr5orFMDaUpyshhFO20mChr0iYv0YQXPmZji4BR1fSOxbWpNghyp9wc8GG9SimuQsnyE66jHpH5uDYUVShg5nJRomMltw3oErjLXzFCafvi-KlXZaKcPgDTgpp2sak1w9lmjPF9gaSajNXfT9tyQ62CWWcXk7er4jAzmu7skYEF_HPoTZRbzmhpUKoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa56N-jUnwpP7Y4FvcTAQvA-nGkLbG0bt0vKv_LFAk5zxquIKXa5Em7HZlA1_NWwjxZEDuvuWFn4ptaC9wJEWETLUPd_rjHWD_HbZmtvHWUM3Hg02r4OR9kE6IsRf99uNB5MiLwm2qrbP_2pYf4S41gVIdaSylk2YhiO8jpgCfc-BmP4tqMKyP5VyBAFavmdh3iRuv1cGoPmxOu9EGMnSbiUhJXbBMaIkOk5ImO9_gKfyNmHcvXCB9bH7CUOivpTol9QE3twoKbztLBF-1OwPqjjIo2TauLZxztq3eAJdNdNa7Jx7VM2lldV2iwKhM_-DnzFeC_sNqj5SAJqkmCBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU7HBq6GwD4Qi993tpjdlVPovaIRitMBjCPLRhDTmAUTa93ndL9toiLm9e8suy5aBWu9BiwkRaqDSNFJf8rziT6zG5cTK0t2r_V4QGTjOd40fFPwwi-8fQmjh7iVh8OMA_wFDrmQIGHp9tKB6Cmlv54Jo0VbLvLjEHINuVE23WL-SwCT5d-c4xv4bocZKZLkLJEbj7GRY-U3-89BOrzh6-4ImmNUxDQDcPIIfMyI56h1Kh-R3HRcLyXGt8ReERZvM8r5CKIQ0-XbUVODvGHx_VXWblYN-x5xWjW3z7lVv27zldUnzgUkvW0mHL3mEYso2l6BSNrk0ftTgFE0FRC6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2bzL_C_GemcoDG6HfoL030KjKGaDJDKn_xuqGUOmB6wHoYRqy_KOiPQxYioNhlESTohW7KMgdPdQ9_LNzzdiotoFQo4HKjYOGrkeUWGXguOLQcyhQnZHwkVbend5Y_ofyAd2xNXkRT0jPC_KYvOTJk6cHnMVBbLXHjSHCEy5Nj5mZOT0VnElcOtiZSdFcRrb9ap4Fx2qPMo4Y7x_s5yXanlN2auClUEhrY1o4vZM-OWKMY-_b54AdpblyE-9J3BVBcgFUrgLgY4H_LpXLppwDHXm5bvyen4mlCz8S--w1Sv3GNpJCZVCc4GIgg4zjsrlDqi8wCJFjZFmvr2ScpMRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V26wwdeSxSUdJjUcv7Gsvcqv3CnGLfw62zDAduk-h-n-UtBHEF4uIC3NHo8gPcH8UFp2-bddtZ9W1fYTBJXilUICiSgBj31ulvP3ek1FK60V1eSJeE8j20hcqkXsLQ-Pwko66GF7EFTaWQgeqOUwgdLPF1-zOcJPgWUHQuvorh8m12Q_QhjBf1nSdr7-tAgjJ6X6zwNTo-B68N2BW61qSlW9TQn8jCIMSREIngFkFXONrilMUVR3qiJ1B5O4Dq7PkSVCLv_B6JeDf0EEqeia78uX5U_M9WluIa_lwN_9m45yZDkDXeaCelDeF1-30rGoH67w1mp-vP7HeZG2C8vIyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=kfNQRuHpRy5RFDSHgyFe1UndnR4dfBPM_nLQEgYPIfVJcVw5IYi6pSVvJf1-ptupekZknGowVsQZXKNQrSwumqGXTq3aJ304a0aNyiZfAFWTQdVOzuLa3ubzWOD6WL5G1v4inTqfX2floMLVu6ItaxU_85nPPOaxmIn0RLiPzucvHhWipQAuQmBk8nzkztwizwAMWwuCtSEEZ7pXlyRIA9uwF_4qL_JCkd_UyFNHHlBRuC7779FngMNWHKevNZzR8vWHCh7UsYVVkOuJzfU_8RLOe3V-RjvEgOmj0n02DgYmIVJDgBpwfuL6tUo3TmWZR9Cdqczfzp-pIxkXBoBcEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=kfNQRuHpRy5RFDSHgyFe1UndnR4dfBPM_nLQEgYPIfVJcVw5IYi6pSVvJf1-ptupekZknGowVsQZXKNQrSwumqGXTq3aJ304a0aNyiZfAFWTQdVOzuLa3ubzWOD6WL5G1v4inTqfX2floMLVu6ItaxU_85nPPOaxmIn0RLiPzucvHhWipQAuQmBk8nzkztwizwAMWwuCtSEEZ7pXlyRIA9uwF_4qL_JCkd_UyFNHHlBRuC7779FngMNWHKevNZzR8vWHCh7UsYVVkOuJzfU_8RLOe3V-RjvEgOmj0n02DgYmIVJDgBpwfuL6tUo3TmWZR9Cdqczfzp-pIxkXBoBcEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmANvu0Ha_3belo_0sB2WxRkqA7euamfVB6QWt9m-GHxXK12LomF7FBbDhW1OFoIWdKOs4VCwzBXD1GcSWcAVmhXN4v1skiHKE1MRqYZnDewRtimyvOqSsdJ5qyT0EXq49QCsUUGnODe3fXnDv0xr8d1ZtStkeEAFXf4J2qVeK2iV3hCvf0b3hIrXixAUqnFJSyg5wgPbLb6iAy8nGjK8b_egAPS3FXh_yG0P0md8ynbIoY30TJ3HmJwFbj1ljo9yKkT6FnhuG8DOWgVcMCpo1Q4X-MZs36IchjMD9UpPMtQpiQT5yYt41vQ5rNMaJ2JbIQBq9FRV0-0pflKgLTxTg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=cEA4cHs0ovsSG5o49muC5kvqQudFQ2wn3LIOQwNXkJ-Imw1YxFT6mwoQhOZ962fJwy4wCsSm3iy1YAJrvuUjtgKDjfwxYwmCqf7HzN7cy7OsnCo8wn4oAAtN1Zs2VDWuUKDepjayo0r7A9NgNLy1vfE5Cb8A7ZEFCwXopzpkkOhKtQPosZZT2rxUE07xSHn_qe3pWUoZmeCnoaimFUZkSlprdhsn96I_czx6yHzUU9-6AYi0Flp5LNvjEML8F9zmfS_EaI7WCN_s72x2lgQYLvHZ1QYX6ufXkDjzSiWwUkhEZSebDbdptcbW942ebxU98zsimGiKg5tVkOODYyTyhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=cEA4cHs0ovsSG5o49muC5kvqQudFQ2wn3LIOQwNXkJ-Imw1YxFT6mwoQhOZ962fJwy4wCsSm3iy1YAJrvuUjtgKDjfwxYwmCqf7HzN7cy7OsnCo8wn4oAAtN1Zs2VDWuUKDepjayo0r7A9NgNLy1vfE5Cb8A7ZEFCwXopzpkkOhKtQPosZZT2rxUE07xSHn_qe3pWUoZmeCnoaimFUZkSlprdhsn96I_czx6yHzUU9-6AYi0Flp5LNvjEML8F9zmfS_EaI7WCN_s72x2lgQYLvHZ1QYX6ufXkDjzSiWwUkhEZSebDbdptcbW942ebxU98zsimGiKg5tVkOODYyTyhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=SCWaR1P3p96C-cxvg9uQ3SOQ-dcENFWbKGp5y8MebkQjylv5tK8zRnYKrxq_kM9ZAveDIOnLdMc9XdJptDvoBlPWk4pNIhq7H384bC3gcxnqfZw29sw5ps71Dj2NAzmbehWkG9J5wxmDs_khXZgKl6QGUSP0PiDEAWik_TypOrzIJNOcMixgwm4YqXAVNtlDt1KKYp9AjaImyXSUddTct9UrA3W8Fy6CQCAvxfTdkNRYQGV6UDu2ts36ZNzqKvsx2H2VhPcIwXT6GiJYMAinvFQy-utMLkqpWm3k63FHLkm-ZSutpqOnX9LE3epJiWx5LOjWVgyEYyHFxCYLFYl4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=SCWaR1P3p96C-cxvg9uQ3SOQ-dcENFWbKGp5y8MebkQjylv5tK8zRnYKrxq_kM9ZAveDIOnLdMc9XdJptDvoBlPWk4pNIhq7H384bC3gcxnqfZw29sw5ps71Dj2NAzmbehWkG9J5wxmDs_khXZgKl6QGUSP0PiDEAWik_TypOrzIJNOcMixgwm4YqXAVNtlDt1KKYp9AjaImyXSUddTct9UrA3W8Fy6CQCAvxfTdkNRYQGV6UDu2ts36ZNzqKvsx2H2VhPcIwXT6GiJYMAinvFQy-utMLkqpWm3k63FHLkm-ZSutpqOnX9LE3epJiWx5LOjWVgyEYyHFxCYLFYl4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv0Rh1fhznySSGtuJSgwqiBLnHWDr0pzwEeZMBgdzWNkkxsRDMBQhuL-Teh5NnkyjUDAm-mvE6DDNMvTTBXO4wcEj434FvkudDc4lzwh1-H-YXeB5EAqwqyJ0U4EFYcJB85C7BN9t1LXbc2T7LeSSiTWG-_--bQqHN6cL4nCCDan9jrVf7amlyqX85S3lOOQ6Ld_XGQQf245T-gFM3hTa94Nojaa6wfQI4R4jRIJRe__8W2a5MXCff4MsDJtjRBcfGbsbT_KvE39-12iqi4FaB_C3LglKWfHhfntbS3KUIhAGYMJU72be6tYtzGjo-pGrlY0tCPJC8G6S3rEN95CAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=veab5lWs6AJzWj-KQGiYIE5_MC8BIixys30PP0FltTA0hTEBeZXyJ7UYnlmrzTtPTj8IdemtLZRETFgYgvUx3bppNtrK_5Q3DuhEIK-bjjuEPX5xBM5EJbJclmL7O7vwa2tNbq-MNUokDvcox7ZaiXJN2eb-LVOsN5ZNn4xzy7ICHy2T7A_3YtDFPFpc6mZMtCXOP7sVVJ6aT5PmyyPmcttP9wIp25vHLLtsYm63WFERapl2rx7lmlBahs1csGYZ9Q15KBCnHAouE-iKM8ohj9j5ojeZTiHWaysVBREwDOvtdNQxog8fFVtfBfZLyxRdnwpeNeRDGWKGwVMF24FKew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=veab5lWs6AJzWj-KQGiYIE5_MC8BIixys30PP0FltTA0hTEBeZXyJ7UYnlmrzTtPTj8IdemtLZRETFgYgvUx3bppNtrK_5Q3DuhEIK-bjjuEPX5xBM5EJbJclmL7O7vwa2tNbq-MNUokDvcox7ZaiXJN2eb-LVOsN5ZNn4xzy7ICHy2T7A_3YtDFPFpc6mZMtCXOP7sVVJ6aT5PmyyPmcttP9wIp25vHLLtsYm63WFERapl2rx7lmlBahs1csGYZ9Q15KBCnHAouE-iKM8ohj9j5ojeZTiHWaysVBREwDOvtdNQxog8fFVtfBfZLyxRdnwpeNeRDGWKGwVMF24FKew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBd2xd8Luqb84l_YuMFljicCHztyZXtjiGP44daM216Y8qxdQLvaQhewo1wMYsB5XmPms1UD2aBSuIaMBMULlrTWVW3Gn93AXa7obLZ-fm4X5sWenjyVJN4-rhEPvqyW9eDRhDA9_Jq0GznwAJIULFwSqAAmc84D_z0xP6AiaV5uuxafMzZizDeAIHjROOcl4o8_PFectdwBHtIVkwi9wDYq_S2by59K952Wz9KNYbsJCcP-zu8Oh_W5u2Ud_W28QRZMRtv-g26F5D5i1hzeBUmRPrGSIBcB4YNyOCX_mMMA8wEp4hdEEhnar9hXnCAdOFBCtgtvgatkEx6HfRdiHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxWRHBL1LxLbVLH6e6aZ0QAwZFaSrZngzJ5MJZqJq-KUKndnrG05q4bA21iNV-J6JkmsFXs8dOrLIRx_bH9fgg4AxIOGePfuo6HTgBYaaKKbu5E_ByUoOqW41vcEnoaGiOMHmFf8ZOKNiNOXPsGCFHqR34eXjBVbP321w4TVbfqykGNzUhvP902V9X4FovOQs6jdOCpvkvynrSKXKNkLU-UkiqhvABw11BfX4gqJleXA1qWSGhnGk_fRDM93PgsRtJtW7cb-DVdLUffCTv3j9LIJWSg-I-5CYrcPP9U2hfYLIy8SxNhmGNHGKBbLzcikouanZM79soaXeknXUdw3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUdUcC0g_1Pf6uKimI-ZTSNH1793hURcATSzbS7DwKqQjY7KNFAHDNBqk4vKuSw0IroMB0giUu9cRCHK5fSHiZ88PIhcLwybTnqRo2UnpL7BW8owJQ5jQy3tNV6bbJLQzp2Jl8pjUK86cUmJQig-SHZ2JA8ThUUjtntETX73mTJ1uxf81Rhk4ihiSWNNda4_UGZfF3D3HlNpZ1ziCGOvMl-vjnmvpcjiXc1v4Y4StuP8iwXAOoNZHIMuwIrqqfnin-USvreGDhqhR5VXNPEzRUUWbuuumbk-2JSr1gPFK8HQMIvhNMIIl8q3oAsZOsJm01C_mgKGL2viHM946-6FXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c75HhwYpfPfhjt6h4HuzDwcE0WHPkmGHeKwD_KowU1wUGdQVUvRatLAA1WV2lPwNr_GYfPwaCpTER262TBDBH6Vbp9g0iUucr4nWvhbS-otV5Uh2sZ8KBclpb6kTlqL-AJMS-rplayYFi6hOIzFAfhIejYm09fiPlMk_vY8TvyjBIpqApQayXwZO7Ge2ssdC4M019stHt9yUsp7MqZBbn3Fjw8TF2trIEsgWdOirjVnaiaghQDQ8321riuCMH0sZDlqZbEV7t_t-jyjgIn_HMZC4ceBRLpCKMsBQvkQVDIxad4lWYdvApHVMvvVkjfau9LfFTKWjwhtSIPeNdJCKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtJ8QdqMa73UIQWA2pETEmq68kBca4y7f8aCQ1arOc4vCy6qqTbHgJ5m4C7A5pIm6A-kq_idwKr12FCY1t_97qyf07EgqO_lXzqvRzy8MxYXEYPZWl9TJeroVxtLwJ_oOgaZs9aFZKojFCezR3thi_FFV9g7M67L1qpJF4hOM6I8bjGeIZeXH6YtPjEKGJYTMnQZ3Xh0Vs2JHSNN3Q3KFU5J7l7r0tB5xGTgtN0PeAdERgfy4KF7Ef53ptikKJtV0-a34FlezZZGmHYW6X_y0YCCo8wu4rvFifZcqzIFiHjQ05yFY1xaC7o9pkUAXATPH5kdEC2S0fvaAUCOKld0kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGab_prWqQpPEfarkZbw14JXMg5JH7NPvxLX-ymnyqq0-Y-sxpJWJ1FxyeNltB0LtDqxrOWHIUGpramto4TrVMIbxbgfUHDcTw_8dWoZ_moL8amaLCVLkl75f3ctfP8PvuLgwcrVX-3zrxVhHJ4CwUaaZela4uJSl2wTS8yGy2ZhBp70gCbYhGWqMA1nu8sH6RzFHTgzPaa6F2Pas-Eph5l7_tWv5DCQBOX4Aketf3hpYy-mjxDTxIS8YmabPkaR8wVToOU6x02M1Cnr-vvpPZgO9DGlY_UotjdVH0TkM8zzbGBCWt9TrC14g18r5H8iMEHZBO1hu4jeY7pgvQvJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDyCMatZqY6MmVvfkqWTo8oNoP7paLA_2usRHsZzj4CwiN1fsHKVMMoTUvFlcLgt_lm8xRlkAGLdRzy5SvYcoCt2enYseEHbOMzCg4WVPd-joLUUbCEd-i7EzLJdCGv7gwGyTP7wXypX92rs4mFw5VObtV9s8hDYeWYqNf4VPgBK4VuewftWsnJKjDJpCKAWMhxi7SA2MOkw78RM5419iF_KDVkG4tZCjM5epYv-P1dy30pV6FRNFuo8ItKlZ8MhGrG9ueA9OrcLRAqy64ks2JAvxFSLWp0nsblOAE_99ypxpqV10JPHnivEv6wexLuoImKAAPziaE3KNCS_chKAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUlwqp79cGcNta7_Jt0bLHtEVz89KPwtDw9PvtE2LPWUQuuGnxHGOVCBOuRq0hKcoSFUeQ9z4ek3P1pahpAW1XGJoaY2LMgxCeJwwHbwh_V2pugyglZPzE9uRd3FAv61O0QvY4VbbD2ZgWnfZyNyNBd2Jt_2ITBzk1ustUQT0lqju8QUmQVH8t_Gqa5zBwLB8TXfp6-sAjU-8-GE9uuCVitfKJrmAV95Xv3ah8SuqtZh12yb_Oko1ludPr__yFaOK38jEq9VFFI0lJMg10womLO8BG-NNhQeH3f3dpo94kaMB7S1f5o37hUv2c5AlF7HYfS7rUiZIl8r5-Hwfhk8qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=iZ3pQXEaHYNRmY9qGl0G4ByULvQ4Npku9_dhrpZ-BVDQbxg1fx7IqAV0bMvLseZMKR2ir4KKkzpCvo1MAnxpfjtG1SpUviTGtpbaqVMwTiCYGL2QCjsBsmAlIHul_oJ3w87pxuVJLfEyc4CdCGpWqy7CqI_eNTLKlDf6H9WgwB-584ZbODOwJQzaQF6HW2a9l3Tv91P_g7L48__sGYou2xB8brFLX6AmpQX7dxi_pzRXMFlrLNUH5jBcJXIs3suEIgnhqRp34Fr30UhLyyO-wDKb4E2KOR7ID2zq49WZ8X9nI37Cku-ntz68RWjQf66At02UMmfEkzMFCPTnfgbeYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=iZ3pQXEaHYNRmY9qGl0G4ByULvQ4Npku9_dhrpZ-BVDQbxg1fx7IqAV0bMvLseZMKR2ir4KKkzpCvo1MAnxpfjtG1SpUviTGtpbaqVMwTiCYGL2QCjsBsmAlIHul_oJ3w87pxuVJLfEyc4CdCGpWqy7CqI_eNTLKlDf6H9WgwB-584ZbODOwJQzaQF6HW2a9l3Tv91P_g7L48__sGYou2xB8brFLX6AmpQX7dxi_pzRXMFlrLNUH5jBcJXIs3suEIgnhqRp34Fr30UhLyyO-wDKb4E2KOR7ID2zq49WZ8X9nI37Cku-ntz68RWjQf66At02UMmfEkzMFCPTnfgbeYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=d--i1-D3Qt1l6DSFndlJunfey7Zz5shSNYgP20Qjpp4k2W3-yRDl3kaRqsF0AAq6xqFs-gIEaIj7RomHB4zm-RgWbvQfTKxE2h-1LEsfpl4kv-VAfGinob7RXxgat8REW1ObzXezD3M-5znZlgHDxdBvcgOhNwHi5xFExey68Em0HjOeqdqAW9UxUF2rqlFHCpC6Mp9F5y7Kz6JFVD0anC1pDCqiCNSL29WUBRqgZlyw8Evc-n18f7gn7NRoTvphkaKVx2oNmG5BCDvky0q-_wiWKMEWXksH2rtmqTe54eUewv7Y8YU3uA7ZoZRPLwkyaY6TzrGqNIn8sJRWpkSzeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=d--i1-D3Qt1l6DSFndlJunfey7Zz5shSNYgP20Qjpp4k2W3-yRDl3kaRqsF0AAq6xqFs-gIEaIj7RomHB4zm-RgWbvQfTKxE2h-1LEsfpl4kv-VAfGinob7RXxgat8REW1ObzXezD3M-5znZlgHDxdBvcgOhNwHi5xFExey68Em0HjOeqdqAW9UxUF2rqlFHCpC6Mp9F5y7Kz6JFVD0anC1pDCqiCNSL29WUBRqgZlyw8Evc-n18f7gn7NRoTvphkaKVx2oNmG5BCDvky0q-_wiWKMEWXksH2rtmqTe54eUewv7Y8YU3uA7ZoZRPLwkyaY6TzrGqNIn8sJRWpkSzeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=n-DjkWxmITWlVbE-deF4tJPIoyT-Hu8ASjAWqjYdvglh6w751nUWH6FCAEVG4UGS8gpvFluNVLSydwTdn3Hx2R03UajkavWM8kBpR3Okq4unjxg_p19_cZdkXhZ6ryQFJHfj95XnM2a6qfJBQNnXJQROXbROLD3bF4QxzwnqPqTSBHJkuRVZij9pYafS4u2KbDdM0ADAJN0MH4ndNYeMDy4QprNaZS2lvo0oh-VvHuGHtz8i_t8RGLvxsIVuoh8nlc2yQ6T_CBiKXdkCyHuVaL9j1nISFtxOfRAIw78zcFRJZMKUIeFdNsLrxjMqhA9lSuMrX9yrKF9pyE9T94rz_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=n-DjkWxmITWlVbE-deF4tJPIoyT-Hu8ASjAWqjYdvglh6w751nUWH6FCAEVG4UGS8gpvFluNVLSydwTdn3Hx2R03UajkavWM8kBpR3Okq4unjxg_p19_cZdkXhZ6ryQFJHfj95XnM2a6qfJBQNnXJQROXbROLD3bF4QxzwnqPqTSBHJkuRVZij9pYafS4u2KbDdM0ADAJN0MH4ndNYeMDy4QprNaZS2lvo0oh-VvHuGHtz8i_t8RGLvxsIVuoh8nlc2yQ6T_CBiKXdkCyHuVaL9j1nISFtxOfRAIw78zcFRJZMKUIeFdNsLrxjMqhA9lSuMrX9yrKF9pyE9T94rz_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD4h5BLF5bGxbmBMQAOm1JhGoCWp0jPK2TccNsYi_Um4e7kVrFHwa5xVklgLwFFj3WHwi2sN-KboKFiaiTSouG5EunGleZdpudD6gqv2C3p3BATveS0xbJG9h-EW28z21hsPiwLNyVEBXaBsupKSovXRvomcJpe6-sB3OxHu7RfPBJssniAoSa7m0BNPt0BAeY-sBj0vmjZ2c_ANB2qmw4E-grb3E0ioDfUbG7J-w_tgaMoOXb4fmpFZ2-r9Hg00FCZ_nZDyN-aF48IOJKehF5kf3FCGRm5-kg8ZAD72YzppiejguX4sj8F88TQ-R6nZWqG8ZZ64evEFQdQxsDmXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7D7d05Wfn9B5XshPoIrJKo7N7p7Per6cnTLt4pLsYbP2YM1EcpPo71-HdLRxM91BXRbj_3BtkAjprkWuh86ZUs2dW3SElgHcWXucUd09wofgMlYHynADm3sew349gZHZpd_B71TivK9A-DAtu1xjDtXohqARQ8pQDa_nsVANoZisGzUsZCTCuzz_95RhrwRRc6fJO8e7IGqVVeNz7aherBZX1PWQvLiKo7yz87ne0Xjod82Y1_LmadC1JSX_DC5N5QiMn-OsmvA03_BQHmX-vPkX1gaqRJ7u10I6oe_G4jL6XZ9V-nFhCEOYGQpnpqF_T8n22YuQJkmvvL-SrFUBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti2Fbsy42JIuBZeFkBktawh-hofeuEiLel6_fr2w88sia-aermxM-9tXXB-xeUQ3hfGuUgvhXMK-DXhF3Q6_YWJzd3mljl1wASk_lD8FQn5NIczFAs4Me1a7W4dACNS5kb9n5ulr2NZ27F7LkT8UiT7ds1GxXHe1JLGsd1MxYEuojfjxWbAOHo4u15MEYRXqCIWgr3m1LG8apYtzLUTEYKVSWmUcngkAmTii6FJpRBywnj44pbD-0vqXb6qtSXN-fDfStwIxF15O2LtKp9xmgyYSRq-On_aosh98KCCPO5xKdivWBg0gkl7UPHfT0MEQU3jeXEK2Tpk2qYoFWmym3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pflhe7oAE-YfK3oNpyxReRyiEl27dxOevju3cy_q3wMCd79_KXgIXtq6-Ta5Qa-PZ7joOcfNpqUbGQ8x5prlKfxm2P0XhUYn6-nTvO44eXcc7iMP9vn5lqiO4pLl-CUs33Aano9ITK9heelxXzNfVLe6RbAhqZjoWH4SLL17oUN6BSF2IYk2-IpxokA4GQZCrADalSTlH9jYBwIKFkaBDpYAdk37FZ4DHeohuJvxXn8BgHbmrRKrVpj8KFZunKN_pBOZ4E-3JT66F4LuwpIZL476PCPBtDZ2XNI1rWAyQu-rQmoaIqMlq1uRNfwIoQfcNno8CaNqsPcYKW5qBhoS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=UpimHT2WxVU2qvpk0IMNSKTVcXbbsFvnkm74yKHU70EPcBkGpzO0c_6M3O_z3_ltv8Fnxe66QEr5D-Gn7f9bAqAFrbZJsMP6eGJ1CYhmqgxh4yVkEPofC1YdYgh1OQX7G9LTb_uYm6Ctv2hMFgXltm9BsX4RvvgQxLEFZ7FG0MiJUmzqWBxLY8_2hAF_i6TqXXinwpL9W_XvCkNelWTAfpX_2JV6JbdEojJsZ60b2ib_oq80akJUTQtfRRBNVIvdeZITzYCZD7r_x116fwj239azIzNaHEqRE2XA6ikodZYonF27aYB6wkSDvH0-xGnd9DEYYngHmH7CBKirW8Xl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=UpimHT2WxVU2qvpk0IMNSKTVcXbbsFvnkm74yKHU70EPcBkGpzO0c_6M3O_z3_ltv8Fnxe66QEr5D-Gn7f9bAqAFrbZJsMP6eGJ1CYhmqgxh4yVkEPofC1YdYgh1OQX7G9LTb_uYm6Ctv2hMFgXltm9BsX4RvvgQxLEFZ7FG0MiJUmzqWBxLY8_2hAF_i6TqXXinwpL9W_XvCkNelWTAfpX_2JV6JbdEojJsZ60b2ib_oq80akJUTQtfRRBNVIvdeZITzYCZD7r_x116fwj239azIzNaHEqRE2XA6ikodZYonF27aYB6wkSDvH0-xGnd9DEYYngHmH7CBKirW8Xl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=jusWI6Q3oyy4C7cLfwoFx7T1TAeyL0ofOLs1s9PxuEOxlZUHxfccxyPr_r45d4edPn8ZdhAUNCnFuyIQXYtKGi-lsYtepKt0Q2Z7itgT-hqP33ztPA46gkAT1HlUXlxueaJirdXD78IFuEO-ZBeZ7Bq7H2P7LDMuVrH1F_2sVzIfKZnJ1k_eeLRklulr5ddkG5cO5ZtuYts-hweBgxf4pgiNdMY8oq6MLM-j-JJIaw5QWLvDm7XAJjPGJmXqUwX3JciDutg0cfc0d5cFurIWBP7X25cDKHWttovE8Ya2noMxsce0Gg82KLVQQTZKgy0r7_oraluHcLNh0LxxErUk1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=jusWI6Q3oyy4C7cLfwoFx7T1TAeyL0ofOLs1s9PxuEOxlZUHxfccxyPr_r45d4edPn8ZdhAUNCnFuyIQXYtKGi-lsYtepKt0Q2Z7itgT-hqP33ztPA46gkAT1HlUXlxueaJirdXD78IFuEO-ZBeZ7Bq7H2P7LDMuVrH1F_2sVzIfKZnJ1k_eeLRklulr5ddkG5cO5ZtuYts-hweBgxf4pgiNdMY8oq6MLM-j-JJIaw5QWLvDm7XAJjPGJmXqUwX3JciDutg0cfc0d5cFurIWBP7X25cDKHWttovE8Ya2noMxsce0Gg82KLVQQTZKgy0r7_oraluHcLNh0LxxErUk1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ7ldjLYF9Tac6iKigU9bcgyVNQJQyiKYlFa6HCi5G_FGCvGM_FARL-f8StxjUm0yerPlLBMWIUyjK-lsJ3awUb85HDC6P2wDsynQbE9kuGdIAgR7jxyXx33NnIUYLkVVeosXssfVA8HgBjkBcq6bktSMa2t5Eyg6y77F3X8SquAtidEI9nRF0j9IC2p_uxuUMGDKCarzwzP5ysBnLdvdhHZa61s-95q_XX4loaSddEWFDcw-rDjrxqYWes7zrybYy9U_0B2lfezKX9ZYFsF0X_DRZqDWFt2hf1k2-ag2LZyAC4sFPfz3stLyYrcTn6TleDP57ca2Js0nrnNtlX9Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mizX5yHETmoH23Nfr3rJ3XywtvUCJUOsjyeT-J_w_lIgOCzGa2xL9tORI88OZpnv4n3CB0MBleO5oqXVwhdKqXoKXLfgf1S6PN8S1AAE3MoyfQAptTZ_ToN7GqBYotUcNYN7FF6wWna1I_u8k8sBlfjbvQmfU_Wo6-mtyxfd8cfa7dHS1L3qVKKVan73W-RclbfJobjUssagsdSyskey9eNFg_1zKAi6KhJ-X6ygrdfOKgEfKZyvp225ffZTtHi1iCNEDRDyzGRGHOLF6IChklu0a9-at-tbNpAwFSHdPl9Ob9krZlBKxFJtQffKGqteQPVWBtsrpfFt8ynnE4-zFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJunSCDaGYdMpvaF2ZzmHJAsYGO4PuB9FyOWWTeT8lH0MTe-7BlSA9Jsetn0g06XtMCFVc1dmmgL85-5V-cJ4OCadyNPGtifrp9KibXrfxpqEW5mJkopXt0etjk2WghCgkx3S1oPrlMPdcQhtcg5Q_VCO6-eax9NQs5bjIaC1Dt2pMfHmYoGfQEVBd5xF2aARhsyikXt6-qaEaic8cyqDSdVr0h63FEycNfNaWO_plE4dWa9fLVvGRI1AyPbKgd6sGOUS5kTrXJICf6OPCKSuSO2s3uOTFXyQJNQttizKHs36Ycs3Xv_FIiXgmOrHTePwYt0-hbgha4ediMBeKzgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu8LiCjVCWEwvhVE0dH9-HtDoenJv9seiUj6kgC9q6HSiK-bCvw_g7bEsF--y4lkhoFoEub9ep4lHNKSa7HhyrKVPT7PKcxhr0BQQxiYHQZ64MVBFXnHJqZu9GwBDkmqiCqycBhlIVB1zgLO_Koz57WeWF4Cq3lSV4DUjvnyn3bIQfiRdgaG2KVQ9oFFGTrsmHCcbTNb1UQeznm4lrJkpPcrAcjdKfVOOM4JR8H_0ZksPx_DPsGxFj7gWBpugUeqASzEFmwMimGN9FGZM6atedwqE1uMp8-FlN74tJ_bV4WFYoqp8naLuOL-l9DzEMeHRwAECE64DPSLlDRk931v-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfLK4Nv-X71ZGw_YOoUhmLHLDrW5A4A2Ov4hRhE4jnp2VijSc9nFmPZ_tWVJI5a_DiD9yq2DVA26N2p_5Uwzrabfq0Jp-9nF-GzeU217dt2R2K_CC9Tr4JoM6mfkndQsA0qCVqdooy9WddWcDz3QI0CcKDmPDZAEOJoCQ9P8HH5G5iLe-GiyHHQpY7fwgCQ0BdSejiXVjmja-LogMvU96MrcaKp_D0-3fwZuanoZt78KzLy0Gp2RoeU0EnczARNAzPV09JARQxh4_zlSlSkidvoRw5MnA54wnHiWEYnN1btuzrQ9YMUkp1OZJRFPhMXp9vriEW1iGKS-sfhUk0vGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uO76EN88NJZCgFK3ji_8BEZHukxJezPhVmpaW0lnhIS8_ldEzkb1DKCiNizABAAlv5SLjMmd_msXrlxdtl6tmgj7_ijRAJWNKsO3grVzFQ0ILgho0xrSkolMfn6UZ-A9yy5mzB8BSV5vl9jFAcn7iJjH2hBuWrXIzXbZrcO3ondWiSxoaQhOEZbb7D5_yLFYY0Ey0c2oTHXAVE6-lehfk-OH9AQDyLb026lRCzCOljhV_iikR8I-MqkVYFjeQCwhlKBeenI-BLNbY-2tS0EswmS1Hn8ALd6wCii_b66ni50wz9pFpsgmlU2dHHlf8ZScry3_LU2uZqFxlOovIBiy0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRTIieYcXM__3neAMOwk2nbMT-GWya01SrVZ30O5xRPBIbzxtgj_ojH0YrraKbaa46csbiQrUgTz5hPrM3qHk1kCjEgGG6EJSkbY1POy9OsTY7VxJtMAUk5Zg-sZuBgCpZ8119b8GYmP-j2CV7AAR7Nk6MwC23LxAmkbxjmLucCVAH0L2Lz2MDKcypvIviu_6y529xryvQHhQeE5VUBM_42c4Q0AXF6PtgNfv5r-Mh0hkWmJoYBdn9_qLsn3emZQ8qLgFos25bQ0ITlns5WFiXYva0lZWsKkUckHMzsPO8qG066vsHCJ_XrHgz9emFfam0C79tqBHmWVl2UwaPJofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snXtIbgeEGhFjpLnpzF0mTroVfv7Lh-StrY2O1xTYLMLVZ72q_O4Oej-yThcTloMxUoeYJH7GmLnE90cq7ezmUu4A6Bc_9EQB8DZJGUa-Fzl3vxl5unvjjNuL5TmjDzK044ccET7szWO8cZTiEC7siLAV-mYU0XMEnOoZY2P3xQ_he-nAf5HX81RLpPhJbbQwc3I8-AnNwiwXSB4HcpYDVaRVAf5lWBFWg33DZ99xHHe43576U0-yVFecl2OsT_KkkZR8UVTh9FIADFD2mxhxhAK1Mrtf8Aujq9bI23whIrNo6q-GLmvrwBrGv62v6czJEg0NV2w365af8nSsNOv6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=ElqZos5pwB4lwpPfpSPf6EWokxGx46sMZjeoWXrxjMxZNWLQweFkQb4-WhnEAK5oL0yTYzW5w46mQcG1dS29AuXwv7pzdKOUQzpHUMlnh2fJnXh0g5eJzZi1GtVZG0CXKr0kgnih1TJUHk5soiPQgVc2KRiQI_8l2Wo0j4AsHdjd_Vg8MoI2jf14wX13alaRG89Y5TP358J1C-QmOJKNMtbEOEPqxpcAk-a-rNAsCTeydhMGDe0Gw0P1adIGRjH3aor1794Q1N3NLLF6ck5rTLi3i3ith0j5CZC9XeuaKCwgo_nOm9a8ols2DQ9hcGnDidCM44LYgqZd-VFj8rjJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=ElqZos5pwB4lwpPfpSPf6EWokxGx46sMZjeoWXrxjMxZNWLQweFkQb4-WhnEAK5oL0yTYzW5w46mQcG1dS29AuXwv7pzdKOUQzpHUMlnh2fJnXh0g5eJzZi1GtVZG0CXKr0kgnih1TJUHk5soiPQgVc2KRiQI_8l2Wo0j4AsHdjd_Vg8MoI2jf14wX13alaRG89Y5TP358J1C-QmOJKNMtbEOEPqxpcAk-a-rNAsCTeydhMGDe0Gw0P1adIGRjH3aor1794Q1N3NLLF6ck5rTLi3i3ith0j5CZC9XeuaKCwgo_nOm9a8ols2DQ9hcGnDidCM44LYgqZd-VFj8rjJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=O8z3LN83moLOLgWAE6_yFbKx06WaBvOF53O9qt8Wjw_yxnGEUaEwAafNQw3wacsrXPCvsYbTy1q0YS5kJbjcTt6UYM0z926-mZxe4s3W702ruQz3V33p3xKilrEgtDqYZ1yHqZ0RDGK_KN8O-GGut1lsgtYENBT6t_V2U0C0Wqwr8g42Sn5BWLezuizj8-cKeOndhHEnI_s4pv8u1c2PecmOcX2y59CJUcs4lxBu54zuTVcuYxShtnKcYCKUA9q9qePGHPIwlpGe8yrgPMIocYhQNITVcd4APaRdnL0pBJSLt8YE0UeTDiP9jdRSbPKPg1gdatBsb2QYEKgh5o9ltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=O8z3LN83moLOLgWAE6_yFbKx06WaBvOF53O9qt8Wjw_yxnGEUaEwAafNQw3wacsrXPCvsYbTy1q0YS5kJbjcTt6UYM0z926-mZxe4s3W702ruQz3V33p3xKilrEgtDqYZ1yHqZ0RDGK_KN8O-GGut1lsgtYENBT6t_V2U0C0Wqwr8g42Sn5BWLezuizj8-cKeOndhHEnI_s4pv8u1c2PecmOcX2y59CJUcs4lxBu54zuTVcuYxShtnKcYCKUA9q9qePGHPIwlpGe8yrgPMIocYhQNITVcd4APaRdnL0pBJSLt8YE0UeTDiP9jdRSbPKPg1gdatBsb2QYEKgh5o9ltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlWSaoDK6rpdBf8e1mGMYKWrFhwIFP3IIr3nufLQoJp7fehmsHJfC28ttw6xMc2oc4GrPhr3ygTT3UgrXarDwneMqz60kOxiRR6JYakKnbab_6qxiqeFBHt8x0apFdJnN7HMBbxJmDiP0yGprEg4bONTD7HarMyzqD55swCXlProGH-3qSQmQcFsDoxIrIBYypq1ThSS1Z99wgRjI99pWiyGU5A7eye9iptbtjDZYeU1ZSxgFRurHySfWOMx_OyrBhXRg9wOL_v7un2GefKyC4Tx4wmAsnju0JMG2ZNzv72TyCKODTHN3LhB5i_xdxbRvr6GdCgyJXbgZxFRfYGcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epPAmULBkLO1ozrLqeaawsb6VU9EPKahqndZGCsU-yfcPmzE-ugFTrsn7YBHVqSa_M3qg8kKmKu6z72NivXqg5z3Q6A4v0k4MmkxvERIc7j0WK8NN0S_96Jeo2LZU2zW99HsCVTWGIBVOL8AIO1Rhr6SHr0qcjQtJkoBYFJu38-nVPyokqeW-66b7KEsplylJJ5f6yxznscqA5rgALu32OdEHBeAK15iilC8B0yW5NoJT3Qhs4s3zjUywomvVb-MZklOI95ZcfZAxDbcrAwVMsOyNEOf1fuu0EA3DGCNDNt047w07bCrYsaQnHIHyBCFz5OG6CoTdpOufeJ4jK32kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=kUzlWE_3jra-mJEtfwjhMcRb5PobJUlmB_vmDk-Qe1U5lYqc_F0RDTiTlk8E3GfvItod8q2Xph3IB5SRAzlljJoRXB3E1YeTgbNhCpGHp2oO5Y05Ki8C7xOCgPAw8Nm9hwJ9wktKX-v_7_JJR-ZNLLUaKk9mWP0Jf7_hdJmcSSfb7dMdvLJP2eZT1kC-03uJsyXjvdaJ2srsIUfMl7VecPJ0AjXTHaWaqetA_Ukp0nkpZI_uhWtDhR_yddC9Ip95MD4OgNDEJ2aqTvad1GvaaJf0OPe1PGzYhI7EGuE8FskzJ-SjKh_pKU1dAZJ9y6jRckHjGTX5ijW6Myi6ZgFCuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=kUzlWE_3jra-mJEtfwjhMcRb5PobJUlmB_vmDk-Qe1U5lYqc_F0RDTiTlk8E3GfvItod8q2Xph3IB5SRAzlljJoRXB3E1YeTgbNhCpGHp2oO5Y05Ki8C7xOCgPAw8Nm9hwJ9wktKX-v_7_JJR-ZNLLUaKk9mWP0Jf7_hdJmcSSfb7dMdvLJP2eZT1kC-03uJsyXjvdaJ2srsIUfMl7VecPJ0AjXTHaWaqetA_Ukp0nkpZI_uhWtDhR_yddC9Ip95MD4OgNDEJ2aqTvad1GvaaJf0OPe1PGzYhI7EGuE8FskzJ-SjKh_pKU1dAZJ9y6jRckHjGTX5ijW6Myi6ZgFCuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTxBVMY4bdQMnhTptJa7X2fR91QmuY1V-GTGMerv9tsjnjofUg13Bic6x58MwnDZnbavbTAeifRqbEbb4CmSUbTZMA2wf0HGeBER_oTe90Kma6zoJE7sikvDXYqzJJCM4ZZhWrKS5YMkg85PPnLk5dVPaiSlkZRcr9Xf_YZY3XhhEozXrY7Me4u__m2F2fcCwARTkSEKp7TGJ2d0EJol2wiIGPNqCrRAkzcnrxG-RhJDxRNhFa5EVii4Tbjwu17Gaepuh4AC94fLC9WNGOfUnoDxZva8YFVLfC_i8WndvEK6zzNJXUUy7BK-dWVqTjjbZzrHejOmUdnfUYP3vO-KYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
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
