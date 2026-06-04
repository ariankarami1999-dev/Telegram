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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 02:21:22</div>
<hr>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq936ugl26sbwnyE8iB79fB7noR5SqHorlpTfEf4JWFcR4T8eaoDeYDG48FmljMzDqMRdMtFNeDSPO-OZuF9ZWCiPlunWVwEFQ48jb_HekziTxJDe8_xWOvuAoKcAPb1J_lZ3JmWM3F4ZXLbEccpXTzdxcw3O8Ykkk6FTIjNQ_wNYvvaawlMT0YMXXFwwD2PX-MScveol36gyZ1r1mGap2XVtIqv0MwGzLZvWo7DsOligRE2Af1fL4zaL5yYb37mvqLPOC-y3qfiEdAvsU--D3Wn10-8zc-pgGSo9zt1WJVytyvxbqwwYeia-8BK0elWrmaO8DheQlBRJhAKLBC24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvsN94JSKqsljx9mgbDBRgV_llqF_WAaZnBseHlLELQKKJ3ws65dQqANeVtfIJlnDw9bUkamsXNJMxX4eg__jKNzrsB0NVBfezZhjqJtYhR-RnVEK9Ckf5mA_EDe2PbsO1jc5aPs8PmMOp7tRRFSZ96-ank0yI4ROcmu4mFjI_To5cjVmnd47taemzRA5xmbn_UiuMpRST9nNDkzN5Xvrk5AnGgzG21bPRm0MWUsQeVO7Io2NPo7jATmNBZmLQjg97FZaJOthxu6wfddjrAGzlSlU93BlZwS4XZ0OI1MIJCBBo2EDJ72Ws3dw1s08pVb6fNIhm7-33CJDgroWH2PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPQwDsb8e5BbH1hHBk83pdT9vAG1x79B7h0LBynwZ8NPcttZT5t3RZopf3hiWBBIv7zpMES_kv-3AWxgm-ma703Uu2nAx4--3HQ5b5KK8QyprJYZ9Ft5P5S97-VAKMwUo-QsunXTOQ7KcmsjlmuzbaVXvSL1sfB4EfGoOvbt6jf_AiZTzFWg1_G0QFq4aDz7AkSXX1ynXd6PIOxsZVA2dbUQrB4xdLPIEoldADTVvkmYTF9u6DhTZmrAR6os34aoVIF3XBtbtST4oRCo3oUSJlUc00N81jLobAJ0zjLd2Nj7V9Xw9yrxeItMrKQxrMm4ynMaC8bhmRAJY5cnOCQO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc7NeffMHacldACBXwHgF5KB9SWjsA0sz6BxNQeeGnJE-jIxQlN9t2ErNgCfzeUItF56PxYjnHLcBuelWVdoGpaz1osWXqIdC7EfeKEE5uwz1T8dONu3kkzI1TBluBsnmvHxLKqmiyauifcRfTzMUhcRTWmaWynDqTor0yBJcRh3JrIXAu8Pc-s0wEi7jxEIWhYsYErpmZwhHuX8CYUWGs8mQdF2qt9y-Oo-5BgiVAFlA6afJTyFra4MDCbMncbOYi8b6pcPSahlaJYSjrN77QaZhCM7H4bMRL8PcC3kVzeH2v7OI9iex9515vHqU-mH0Rvt7oZ0_c_FYX-z5VjIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=cdZfTw_io4yBNmSQ7LfZHKV-H71rBWle2MVpSDfdLPH6ZzJtAZXubBgYZc7CXi-SRjsstBZh9aECbLISzbmYiQvX8vaZ8KaC7PIwAwsh-ygoQua95Ei7cdsKo-2OoglWCMYVLsmXcwrMOyatffiGZ_zJI3lhpN2e0_LH9odmHkET3nmF7zy9n68iCxNfT6wyyVDOXXihVMY1hVvr9mm_w48qirjz-52Jp8IwCthMJ1HU4ZV35ULTdEbOTDwC7gawXv7MARHXHQjqy_ynZOFBLzYR7UMVIMbq2e5QTg_PH3YtV2t4EXw3ES1lUbZF4VCFJKF7iM7nzlkTUe0pebLZXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=cdZfTw_io4yBNmSQ7LfZHKV-H71rBWle2MVpSDfdLPH6ZzJtAZXubBgYZc7CXi-SRjsstBZh9aECbLISzbmYiQvX8vaZ8KaC7PIwAwsh-ygoQua95Ei7cdsKo-2OoglWCMYVLsmXcwrMOyatffiGZ_zJI3lhpN2e0_LH9odmHkET3nmF7zy9n68iCxNfT6wyyVDOXXihVMY1hVvr9mm_w48qirjz-52Jp8IwCthMJ1HU4ZV35ULTdEbOTDwC7gawXv7MARHXHQjqy_ynZOFBLzYR7UMVIMbq2e5QTg_PH3YtV2t4EXw3ES1lUbZF4VCFJKF7iM7nzlkTUe0pebLZXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OghOU7XyzHqPuLVM1WkCxapu50k6WN7l7VK5GWxgG4aU76ZQyZk7OUIEeg_SW6MtYuaTd-wEa4ubHD5XNGikb-mcgm8-V_Ja0poCElpKaJ3JCn7gx5ooL1wQrsBMqvBIJiUkbLPWls2sxXWjQMMgOxG3oopls8tGCLmcKfRdmOOwOyMwABwfNtDmIrecDRnkm-2PIluk5koiRUujfo-GJjD6mqYnNYYLmdSDofKVSMyqA0uq6pjZt4tpXMy0rwzXJxEztLZrQpNJztoGvSPFcO1qTIK8sFJmBudgO30gS39wxfPS6ZCfQoXAJoefa24blDc8HIAWd3cfI9bnnp2ADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGFJ_-xJRpBIc92oa-OvjuTU93ScKU6b1JF-lMXQTS3RaIf-f5U_PNaueqlvBl65R-wfPQGBVfmyE3VbU5-ZB8AJWDTerYusCWFgMQxKAAgo5j5YtsSk15c65rh7dK43Mn5r7gktgiHeJBXDTVQ3AQvvXl2zZ7PSX9NLFVWedmO7l538609Xw8eA_twbDfAzT0slNHtIinIi5XF0i3K-c5tP7ZxTkvUHCG-4hlMcvGwF11BMD3lGXGUaiN8r0yq--C4_-H02rF5ULOLaFOH-4qCfn1y_Lcc-daFQiomlaoFtAXlWB_lxtGKEi7CP26p-9xgyUFezYmFqYH-p9O63Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV3vEIPozSjilUKiOhDEJYwXHiTTOEbScylMx5BIpl8iHYbkinHBlsNm1UdiMX_ezr-8WZl4ZqWhthHzjAWzm72-3WE7bh2NLjWdvnHSuP2B9jbu1RF1kbGfi3IzjxjCbJ102GuCFrJ6IEF99ecH5Qw76Tndv-6yv9xQRvHz6Vc8uLmp64rZa9ATg7GZjcGYiZ-7NQy1hWCiOPyV5xpcRJUk4gK1Mm-3DQyhTz3sZC-VaZnDsanW2WUoN_pg92kcgJMMHC6P05ALvH2bcStiFvBrRVz5Pe8LYGSzP5bKJIh66Ohz5zDn4t5DeY_ms0yfIN9wbZyUtpE2RAbsCTwj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkL3oXHiKsRh1R5dD93jaUzXcd1a7dQ0Gxfs3w_lJUnReZUAibgU0kBPqALS-KT6MGoFZY0rV5BRqve0nGiJCdAaoNSGkgd566QbApF93lAqog4zEeuJ3mKK-CUfgMcVFoo6TkMT4lo7GfLfA3n2WfqKlSysVmo9qS2E3riF9ZeKQ5RBGO2MPHPqpOA3entfCwA6h8M2enNlKH80o9K6S6d3URDXnencQLjpJxH8cFzbXQ7V73ywkWFA3Impxg_poTDRLrcqEFLLcKvs8DvEaLlVvjubo8ndjLw8u90BqsaDq8IMxWRL8cSx5myBUlwMB_wHGxj_g_f75tsuyXrfnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=nqNmMpv9mk16MUmLw5NdZAOVDsOv7m0zvBssiT7oG8dwCnTBOvcdGigzHb4UZsTsV7qY7QTfztf1MANmMNMnBILzKEqDF0mX93YKAQRGjvFoIXERsSvGSk0bQCEWU1z9fCbPE6Nese2-BuPPlt_iuHEwC27M8h_2rnQF9XLqOYQOnro_Aew0gXD7ZIyzk_5AakuyHcLcQ_Cn05l9n2V52UaKOcej3NLm2bWOZG_1xC-w_0g_wN8caJ6HU1crVWhcT9GvRTvGIvsSEjMzQ5bei6EoFVzHWM8xv9q0LxuMkkcEaS2Y9woa7GkOGjR3lmwB1FbwEzbmjfkRxo84m1hGgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=nqNmMpv9mk16MUmLw5NdZAOVDsOv7m0zvBssiT7oG8dwCnTBOvcdGigzHb4UZsTsV7qY7QTfztf1MANmMNMnBILzKEqDF0mX93YKAQRGjvFoIXERsSvGSk0bQCEWU1z9fCbPE6Nese2-BuPPlt_iuHEwC27M8h_2rnQF9XLqOYQOnro_Aew0gXD7ZIyzk_5AakuyHcLcQ_Cn05l9n2V52UaKOcej3NLm2bWOZG_1xC-w_0g_wN8caJ6HU1crVWhcT9GvRTvGIvsSEjMzQ5bei6EoFVzHWM8xv9q0LxuMkkcEaS2Y9woa7GkOGjR3lmwB1FbwEzbmjfkRxo84m1hGgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUEfHsGzldn8qjiIPdQLu_aS6tIE0FTW5-QkKEOHqmWbV8S2NbcV4P7pDjWx0-qlV95N07hWfg6xiQUlQAkmxiWUkz55o7GG8Zh04qU4Qu0Vtx9n27XvBWnZN0GoiExP9jJBZ6fCaOROOKKwnol9Xo4ikBIqE7aYoP9qNIjWb2brDeS3lBk5IVPh1G79HDuPWlzPq9BTOF6DmVcs7Z2-pDtOulnwXdV592c6RZsn423xgCRz2Q9O-K0yTd11iPqAfePk7jSDpe2qgcde5ONpyMBIJ1rakpt2TCMjdisbF9WdK8z0eg833Z3iQYnatLYYXP5C6TbRPba16fHpQCeMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKlg8oEHLkpgG5vo9QQma19QRo0sznRiamMli02Wa0bQTuT-oemkxnPRBoDVX3ODV2kQ1EG6EE7gozDn5VA17r2oo7KWZcyQj8NcmolTuO2sk2FUTWIBAJPbQxOhiRGUO-f8NnQyq4AB-4eQJynlKNImR-PXjCekRi0D2Mde4oxzFL6nQ8yxRuG7ODc1ADCM_CehAJdmypGzmTkuD6uSQlJdYS3aoJCJzAhJHGr3reCz7jYZgsC8ONJ5RXvhAAb-tqebTdAayfKE1fteMUp0OjQN6xT13RPe2IsT-longNjgf6eFwYhchiUzNkK3_PiUuZkemNe5eLnSyfLcnFeqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqPCVGlTMxMDHp9Yr5B5k-67XTpD40BGi47I6U2jQLUgbMKQEbPp9D9SPcNmJa3s_KjGknOEGLQaM0eORC0XnbMl7BlEZdRghrevQx_4cALSlUKtN4UXGliKDnxYmN-ODiuFnxq4H5GlTgErvtkv5-0Ryr1wvPp2mBakQdPzyOYfUcWfnCRv_3AZds_9fYq4oIkAZyF_lU6R65O3NiS7wM6GfFcjhncEMT4OzVmwOKKDdHnWAeNlTMm2nn1yTS8REqAlch0euPA-ENct-_31lkmSbU4jNbTuGTpMA0W5X1Dc1EO-dsR1KRobk4Jm1-3MuYRDMp1NXTjFw4PKdNS_Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Enah4BU5AZjevZ9BtYh-Xyb5L4z3J1S9KgwstSuufOCMEeQhG30L8PVIp5yVXGurD6P6AC0u2S0xSYVn_ry5EzS9vLBp5twJLtBq0ZVlcPpaZgu1ooQnHFOAoFK6TBUin_yvEwwE5qPtMwjq4W5j94tTNkT-6mvoMTonnrs9TCrO4fyZgCe2Hf_S5r1NpWaPAAwZ_kizaqsA-fYkzJqsRovxOYCAdq9SysRshEvn7UWC9BJ-_90PfW3SHv3ZGJeMcOHzpRG6PwWCHdZbsuIkVhMkNw98B5DhVM3bgl9XkzcalyzRHSXbPPnKBNFE6gaYfjKjYRD0my0B5j9WqV9Cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqJL1c2rOJrOtkUkk5yYV2ru14rjXD6_SqMp-jYoXbZR9AvpoyZU75l9gk8utyrNc_567KuwXfjkCFSg3IgIKCtf1sTVGO04GOZWaGbsC9PU2Z9gP0tUITyV5vhzvsOOoNxKWaLm7pZnUFI4N6rgXEmwAgrlSVIg9X2gQWtmPebfadOn5MkFxdYV3eDT-_sDcyd35excedy0qcGcDpDLh_ORCiokesdElVx8OrzHgoNIo3rX0i16hDhHOnJVtsEPZ2EYblCcVaQDdC3gbi4grmPP6fM66V2uARV4eLBOHJDdwFqchZdu8ZGUiVsBVh6QzkRO_4PoTZ-QJPa0bp6H4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hykMpwN-aPRHCscIik7l-BFGx8LIWkmKULli1godfI6UXJ5j0h9ran6tSawOLjErh2O61aQmeFbRHaWz27J6xBDtYW1WEwjhR8L9ymQw1OkKMcPV-56rj7hzOAoDdzMeudBitCI1FsbWTLx_nQgRwvaLfzqKZXRB1pj4Wc3t2TAPkYtAtWsM3EU1i3MR9bMRhDRD81FEcr9_AaR-YzKztMmSg2crk8H3VvtesKXewsv17xKNnFrsPnk_r7YGHJdCXCfvqLIbm1PNfa3gq4WBsg0ExDkfUaK9kACKlwIkjvZH3izfVFMXGEHLnUICjV2ogpxH0icXGHl05KqCvhFhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJ5IJ4ecBupX5gYGw8B27_kWp-qh15mkWIG9Jvk05gZV0q8GblKM2QyPEMV3IHMq6Rar2s5RDdnfHkK-G1zGQIKoho5gMf7gUND9N6VJx8HkmY2D7oKUTc6wm27KigcO1qQ_7Wqtz_1rq7FfqXh5PrLfB03RsJmUNyB-Gz2_vPNNSLsd2uKkR5ovcmZIkPr9GRd2Jjnngcvk3RyfjzfoZE-Oe1ngXhaGfej1Z8grOVFmPljQxgCgW5o1x8A3li8YKhwCwA320JQRFYQNNZJtA7stZwmd_8SmRmMi8_RapPiluFkvRBBTg43_m1kjaydpLzNPmRTOAIqdRcN-Spwqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crRhketmY9GUKjrl6GrYv0rN1s3Z5O2EBcAXdEmRnhEswl3aWnnUcOmbMlqNlyRhH8rSqbiU51EigtA1FVWDIr0Ym9ah5Xll4XQIr-SGMvD0FnumqtCedA6b_72R6Gwm1XfjZkB5kJNqMY3v7u4J1mj5QVlF6C9cXupjvIIulZheKilxdI301n5tmszxVfMuX41DxoR-uYEix2ekWnVJ-UYovlyOTl4UJKpzKiL_520N7U8hvQmyeyWlRw_kYV_EVKI78HGrFhWvxvNw1Y0kSCyh89ju9MnvIDVlOXnrcuDM3sZ9UZOMXjuZkxt61DXudw1e9gGNaPMw2CViEujmhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=cVskn7jX5T4faO6mA8_tGGuQ8xw1FF-gUVH0HHwqywH4GITECeng3TPGhP1kPFST6txV3XiB6SncPgZ_Xzlyr015uONjOFXQIH4MkdEj0Qfaw8IXAJXj7BzYtT9DA380ASL9R0L6P6IwKULqWEuvkZPFRnXG3-Dj0b63InBMf-w-cK_sI1WtUtDstjrkMKhRBr2oGDnx1o-rI8OmWy5MK3Kz-Gx0yUFRAM8gmWDc1c7vfPuYybMWCO-YLAv_-uI8pBeUjyVF8oQeKgA34X9REqJkpt4WxuQMZLv73qp4Ii5mRggLrqGUyuWNwPLEqSrAsuv_hM8Le2DH_0zJW9dgCYNXaHUatJC_KDqWTk-zRNOcHBaXZn36bePMDH5W35ukdN3dKjkJz6bUAO9d94T-p4EdIQb_txfeswsXP-512Yd_0UPeHrNigclz5mzMUOZoaoXpoFe5_gURBmjApk8CY0nbZ-YVxw2Cl7t97jwCMiBILE4bQLmH-k59cR0KIyKiC05-2lqvMAq1F53kTh9RylCYvmvx5pnPWc7dPWTLQsWPHcd7GZ9Q-JRYytky0xEbM8LgynhqhHcDlxfoBpfFqiCekATyT4YSmUaYMjKQDQXaGbtKXigJg4Pbl2vF973l1op2HNen-vpfDHf0GPctajYbutSsBkjBSX5CfbCgpLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=cVskn7jX5T4faO6mA8_tGGuQ8xw1FF-gUVH0HHwqywH4GITECeng3TPGhP1kPFST6txV3XiB6SncPgZ_Xzlyr015uONjOFXQIH4MkdEj0Qfaw8IXAJXj7BzYtT9DA380ASL9R0L6P6IwKULqWEuvkZPFRnXG3-Dj0b63InBMf-w-cK_sI1WtUtDstjrkMKhRBr2oGDnx1o-rI8OmWy5MK3Kz-Gx0yUFRAM8gmWDc1c7vfPuYybMWCO-YLAv_-uI8pBeUjyVF8oQeKgA34X9REqJkpt4WxuQMZLv73qp4Ii5mRggLrqGUyuWNwPLEqSrAsuv_hM8Le2DH_0zJW9dgCYNXaHUatJC_KDqWTk-zRNOcHBaXZn36bePMDH5W35ukdN3dKjkJz6bUAO9d94T-p4EdIQb_txfeswsXP-512Yd_0UPeHrNigclz5mzMUOZoaoXpoFe5_gURBmjApk8CY0nbZ-YVxw2Cl7t97jwCMiBILE4bQLmH-k59cR0KIyKiC05-2lqvMAq1F53kTh9RylCYvmvx5pnPWc7dPWTLQsWPHcd7GZ9Q-JRYytky0xEbM8LgynhqhHcDlxfoBpfFqiCekATyT4YSmUaYMjKQDQXaGbtKXigJg4Pbl2vF973l1op2HNen-vpfDHf0GPctajYbutSsBkjBSX5CfbCgpLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=RU31yScL3eR9sD00dqntp2BZF4V7mngLsUTa9ZDEmZ0NZJC_1kecuWWW50ovQcSF2AmOPMz0U7kYK2R_SFyswIYinIM7E1Kkg2OvtEvZNz9PnmG9UhBCCveKS2957tewyn7GI6VwlkAma5sjETb3WREl7lkEbgHLwWsSkQpESUjj2YQJ-ckTEYi5HFOWOdYqJSoFmME802-Pq5YLnRxvYx0cINK-2dIL5EyndLYt39vucKEZcD7IPaPRMk_WO589NXZKkTlo5G34RBMZuLe5kh7mDiiqOqGkXtqkZaDUa5RhXm0Z3S5YbD1WBY6N0sUN30RO0E4cbGuC6qoLuAjJvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=RU31yScL3eR9sD00dqntp2BZF4V7mngLsUTa9ZDEmZ0NZJC_1kecuWWW50ovQcSF2AmOPMz0U7kYK2R_SFyswIYinIM7E1Kkg2OvtEvZNz9PnmG9UhBCCveKS2957tewyn7GI6VwlkAma5sjETb3WREl7lkEbgHLwWsSkQpESUjj2YQJ-ckTEYi5HFOWOdYqJSoFmME802-Pq5YLnRxvYx0cINK-2dIL5EyndLYt39vucKEZcD7IPaPRMk_WO589NXZKkTlo5G34RBMZuLe5kh7mDiiqOqGkXtqkZaDUa5RhXm0Z3S5YbD1WBY6N0sUN30RO0E4cbGuC6qoLuAjJvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsgzmPWp3vZOQRLJdEzuouPt5op0mHMvszMacluMKoaNG5WlOlbfWRZJJXlsYxJaMnGT0siygXwDEmGKL4CIGL1a96EqZS7e-anOq_tkqdn-CZtiRfTQjgpiaMVMt888kChmlrWelGYPhMGd5KQh4WsccMuTWj_eDJxM4D78sS9SMotzPx46vZsENNvMAVfRlxXB37Qs19JVbO2cq57mB3fQsTm9R2GBRjzbrHdzQdE97p2dTdiF9piodfLOHUbS0k3rQyUODdTq_lyUYB67wY388CwN_CY0qQ4XbMdsLKKk2-hhLQAKniClqw3QcY_3N5Wv8SRYXuuvbLSxAXFtmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPi2EZ56bpw3dRSq8vxwY7l4mwhweJ4gUEjRpP9S1YCKO64KWQzIVnLbQUuTzECNX9EGl0UxMP1wgAN-e2jZF4o2vt2lwXs63C0b1waGJlDu-yzMaL8rjzA6DHRCF7AKq8vb65spaceIip6mJTkdAGBm0E4xFifgf--N-gtFZqxoMkvgpywtHuJHoZIVfvAnHbcKlO618JD9DZs3lVh3XFqQ112MYUy6PjzNobUsw-JfxTL_wpN9yHOmX6h67-Ni7qnuDlCPgjxDKJrBwoSzDWOFA047z3Vl2Fb58HognG_c5Y_YmTLAe5NXaeYWqrMxYiMOuAYQ84KuYlaUIh8Z1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-OfmdoJHgj0CR8BW7McPPRmqpfgusITy-cPG3WjcSEtPTL9zpo2cnAttFEjHB5CGhln7DigBECAWiufzTVTGUoRm54TwVTN4y_Ram7jM_9l71i73bd9rtyPuZvc8kIJQGy3jbCPoXRt8sY4DhCiKLiwjWp9PyWZ2XQTE2HSAedWoyZ0y1l7X_l-JcjgEKD-5bUJVSyYJBT4k6kcSGgO93XmBcAQdWCUqEQmgzu7aoUfS8bcjQEwsVdHzo5edVfy7Cp7a0PB7U7KEMKagVFDvJ3gux6-HTUJ1bBoUQIwYX1AmP_8BxgIUkbYY0v2IoFTqnrWh2EY2rga2Cx-tDqDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGjcswbn2XW3iSjb7QmgZy1ViRROfvzCDRQvEotNrY4hDMsbimH2hRNDjuYpNDCKgQPksyxTpuq4clsgs1GDM_QTUjjBq_chIjd2Sb2Dj9Gplgcf1NBflnXIDnTpd7Nav9yyON8RJWWWYAGJyMXxukqmzDPZDnDzlC3CBPM1HdRNkMe4Qv4bqRY116FiUnzFFY0df7hOTGw0CZ7qld6BE60-oEEvrw1Pkcsj9BiqnBHCzemn1Q0w9yENFkNHakHSIGmlfdI5ow-yzsLMlehArM4JoHwk8sovdntFVREMdexQzlkTAYk16bIlh_o9AtOOTUVTxYLFuooxkPT1wnDWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQbgiPmfIO0V-HRrKA5L2JZDfLQlfDC5aWn-B7Ite-KCZAz5z3-_v3dETuoxXxu22fF7NmHM_2GxBJTOjOGpbYkQdfp6G5JNL_pSP8QsqkmeuShL9KTAvP1_IjhLEDhVogDoVVAxX6XCXZ2lOu2TLFcYTJWqYlLMnEJaD2Mk0ZYHzhpMZ5_MJ-2tfswvOCX5NmK0R2_ZBb0K5-zom-C6xV5pvfRIrvIrACokph1wT2G0SNiI7M5Ezxch6dQzZVNMcw_v5mfdTpaSqtTV9AnIxxizLcQ-ZI_xLqkYPijuG-gTsO1hBs5Coeuht5cvXLIsQpQIo7x3TwJmySS9c3cyrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQnfF6iBFW0_3M15w6I9vllT6aV3LjSepSOUSd5GHamxg4puolebdLyxEIMrs1hjDLqdT8zRBmfyRJSdpwT5hi1sCO1QD8HVocVZwg16A2zhiBhNlyRaECJY7_Y51JoGMHun_B7ZX9f9l2MR4kjxEeHVF4pQb0wdIuEe6Wo0YLARIsGCuqvcDVLTr7dQ5hNMSIybZVp49u9BmkPRUJi8BylFOtxy4sKrXTqR6HH5tyWusBzFfznxLd2sLzZdjxjJ_43Pyki9PLLFsijZ5X2g9qb27SlDtDgiC3J2zncPeJWd7dUigJR3_xP4k_Q7ECIAFUoHn3491fQIdcVePI18Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOclMSvOGiVovm2Jx_Yoca3IbJYVMmIlX7EAILs6_BQb1wh1jFs-5Jf5TlE4RttonKycnJ4U5Nj-sf2KzDqBhc5hbzc8gwF83xt_w0ymyeeQJxsGnJH8wuCIV869kUv2rlXoY2FLS-hetTr6i-uPp6I8QxzRHTnijOouHO4sqd6OuiXFIGWQii0m7LzQVUACNKPo9xYYn-P_8OBGkojHJOdhV-aVNoO9rz4W9HGtmmyfEV7Eu6HxKXL4k4UvZcMZl3CrEFXBW8tJP0vG3VR0GjllLfWVJSD2raUgOCrYGQiyI9l9_k_01DzujhlZkZmCRZosXvBkrwFN-ZnEOCteYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnxFIn_xqSb4fHJ64skA8qsbiJYZsmOQSVyBgICjN4pm1t1mk7bj41q_XNwsJiYoUG8MeKETxwF5AktRnWtieU5cuh3M8LnlK6qUAgTwqGA9YQhbQFTOTWEp6JPNAN2prQPZ_t6n5H2FG8EALXbBdores6F0nqzlUh8Ln-EXpFCBeu9SCeNsG_JiUxIjqBW50J55O_b_94KlQV6hAaBmqeOaYvVKLBgHs5rG7ugdFpYyWrC-g9NpYc0-FFa3k-uIWkdsuzpzMjnEtPCGMvhUKJvo5kd_vesE6fLo0NDNdTjBpEIXWN7AbA5mL9CAPemOIYKdC7hyciRmjsrdMjFzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z94fJzPLVkL0VhTKlMHDMsSTbkPqOcdtJIOi4kdls3zXNaNIvwON9C4O4bq2N7LjX8vHw-QzEKDdhnEaQsyn2HlkczhqBUw5EGm3y_IDAd5SADrTwCVhFS-hnDvqZwV0BJxtOnAdc7RDJa-l-SpIpg0bbOLrtfBjAUOYxdiIzEUxRfDbzWBMhk01VKfmsCVelztfM1E3mVbAZIFg2cAR8PKXy-2_8jd0E2Bd4oY8zac9dke4k1hCPK4VyOuZRZMEr_hHvRKudQW8mpkRbWe2fjseEqHR1p8RV-K_KcOhRR8M79D60MgQj365tCo4BjTna_JZxstlpYpeNIOVJ-N98g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=EJbONRewq8LzjmWsQwVAPy1K69atEBiKIrgh03_srmPY5idjDJNFMYHDFBKbrTq5MOGKoP4AuESxlUQccqpKMrcn9YHhgWODlIq4A254KBdAFdmQaryIEJw7CDhxX0kTqBaHn4oMLHq_D_Tmu75HSeUrbekbShWqAymg0bcZc42TrBQ3rBP2EUVm59lhbftD_LXUiRLmlSFfXTcxOE63Z8TI8ArxB1N-2PmCLV3DhFXTBuUtq-YDlpP0d5elcJOadVcPZecN_huNjvUwI2vrrgRYsJSk_Q8g-s9bvPFoYfqTVGTf_prlJeOtkJjsZ9vitpVVBOFWGsOT7IpFmvio8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=EJbONRewq8LzjmWsQwVAPy1K69atEBiKIrgh03_srmPY5idjDJNFMYHDFBKbrTq5MOGKoP4AuESxlUQccqpKMrcn9YHhgWODlIq4A254KBdAFdmQaryIEJw7CDhxX0kTqBaHn4oMLHq_D_Tmu75HSeUrbekbShWqAymg0bcZc42TrBQ3rBP2EUVm59lhbftD_LXUiRLmlSFfXTcxOE63Z8TI8ArxB1N-2PmCLV3DhFXTBuUtq-YDlpP0d5elcJOadVcPZecN_huNjvUwI2vrrgRYsJSk_Q8g-s9bvPFoYfqTVGTf_prlJeOtkJjsZ9vitpVVBOFWGsOT7IpFmvio8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRQsgfi3Z9Hq5EP8vMNDsHtcog7C-gzWLGEtSp-e5AWPvU16xZqx4_tB90RRmze4yfIqnNXKSIEEyZ1cMRackE0ZJUELyQFtLNx8eDLimhRhS9oLREaIrh6zdBeSggjWppSpDO902jgWdI3BXMLsfNT76vPeY709e0ATEo4Aw3BhfX_ywHMi6lIhuFesu06l6D8UkGUocDrX279Aqp-btU9c6Tsb8aZVYf8SK3G8d6s1FCStNCCvMW64hVcnxxD6h_U1W1PWERilDz1kmDxrbey9RZDxG4OMkhIF9FSEL0cmGQ6DNilFOyy1Emc2Wan5d80aRtaGmZ9MJyPn-8f_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=vDwwC8Y8MynrLyklH2CnQYSzHpEJcW4se16rMRdRIT9hlKOhOZdfbE1tVre89GqyKeKswxTozsSFJkvSGLkS3szHRqoBYEi8XrQhRY7u-nvFKa2A89_4NLjn9Iz4IHuYWzL26Pgc4QioXKwuX5QJ4qBkL8Umj5Ugc0DXM3MJj0WIVp-QSZrTU8nIjY2-0-pb6jvbZT1W_I2JmWBzJdKUt6MSPSjQvOXhKDIZ0MTl9iYDrCRnpNycxzY8O6UmnnjLeeQ-NazbAtgceL87a3ZDfql7-s1ExD1F8pqe-xJzkldQ34ZfG3aZ7FFL-A5Yl4xo4FJ8g_YZAgDhY-MW1lpxFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=vDwwC8Y8MynrLyklH2CnQYSzHpEJcW4se16rMRdRIT9hlKOhOZdfbE1tVre89GqyKeKswxTozsSFJkvSGLkS3szHRqoBYEi8XrQhRY7u-nvFKa2A89_4NLjn9Iz4IHuYWzL26Pgc4QioXKwuX5QJ4qBkL8Umj5Ugc0DXM3MJj0WIVp-QSZrTU8nIjY2-0-pb6jvbZT1W_I2JmWBzJdKUt6MSPSjQvOXhKDIZ0MTl9iYDrCRnpNycxzY8O6UmnnjLeeQ-NazbAtgceL87a3ZDfql7-s1ExD1F8pqe-xJzkldQ34ZfG3aZ7FFL-A5Yl4xo4FJ8g_YZAgDhY-MW1lpxFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=cSfgU7nqSLjq_XnV8zrOxzAhgB8ihSGvjHYECX-zFdWkYvoz0BAsA0na1wWBpyuUvUu9rnrtyASswX05CyS54bC_lJ9zFthd6FuaAQx4tCYDyoHXvmrQzBun5Bh931x0YUyNlJ1j4UhQymGlasOOzvzZnaAuccLGPlgO0sUlMa3ZD-nl2aXoFpHmCJte0sNfjeScWaiIAW8bMThu-37mR52fAX_5CfEafHzYPr1npGOrxwyAfUHaf5BDZlMi-M_It0dXfKsU_XIj32_gdzXUmOvzMJmgHKhax0BcNaN0ciWiFa6RdW-Prrd1e8lLx1TiZ2d6V2_APVqat-PER4xksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=cSfgU7nqSLjq_XnV8zrOxzAhgB8ihSGvjHYECX-zFdWkYvoz0BAsA0na1wWBpyuUvUu9rnrtyASswX05CyS54bC_lJ9zFthd6FuaAQx4tCYDyoHXvmrQzBun5Bh931x0YUyNlJ1j4UhQymGlasOOzvzZnaAuccLGPlgO0sUlMa3ZD-nl2aXoFpHmCJte0sNfjeScWaiIAW8bMThu-37mR52fAX_5CfEafHzYPr1npGOrxwyAfUHaf5BDZlMi-M_It0dXfKsU_XIj32_gdzXUmOvzMJmgHKhax0BcNaN0ciWiFa6RdW-Prrd1e8lLx1TiZ2d6V2_APVqat-PER4xksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=jNT-o6zwwEdA4paETd8Rz_fNx0eP_9EZ_EFcI7iG_b2zOJuc5MfA-6O_V99ePmoMvgIc-PHWmXk-e2S0m3REaHkhNO5YB-Iqhg8q7NqOdLZNVMWKiJrXXMDK_gna6V7CyZLYhmAmjzfsiXymf9yxybITjU034jdyatqmuQ6R8R82lGvE9kDb5TLFUzPOpAh9t0Uz_WdBpAAOZBv5N0IkrKvi5l-YU6kjGxMn2jwcAbfgiMnsN0LFJEjrM6jUn1yQqw_8AFLKnmRzfUCmDrS5qkS0Dxt4SUfq_T249TSk83yhAy9cJmGhilHyaU-V27SQIq2kbrL2UbaRaV427kGy_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=jNT-o6zwwEdA4paETd8Rz_fNx0eP_9EZ_EFcI7iG_b2zOJuc5MfA-6O_V99ePmoMvgIc-PHWmXk-e2S0m3REaHkhNO5YB-Iqhg8q7NqOdLZNVMWKiJrXXMDK_gna6V7CyZLYhmAmjzfsiXymf9yxybITjU034jdyatqmuQ6R8R82lGvE9kDb5TLFUzPOpAh9t0Uz_WdBpAAOZBv5N0IkrKvi5l-YU6kjGxMn2jwcAbfgiMnsN0LFJEjrM6jUn1yQqw_8AFLKnmRzfUCmDrS5qkS0Dxt4SUfq_T249TSk83yhAy9cJmGhilHyaU-V27SQIq2kbrL2UbaRaV427kGy_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlOgi-LnmWr-bUBQB-rlyCSqahU_k9u_fm_CUacYCVyWw0etAXs3QVOXzDli9DVFwFuE1g6KBqbrQd1llw327gnmPzskbFRi6e0ZOHJrQeECVd6xwoYWUTa4f01xNpE_fqn5pBwNTApvvadYdw11PT58ahXkHpShcInAgCXYVGzaCLodD5rultWxmedXdgBFKPq0EOQvI8vGD1wgbtIEl1qbxc-FVzRDUyXx-FObKBIoWHFZwg05OyaG_biSNuQKW05PuSLSwj8Ssz3IIHZdqfUSJCv-m736td9jrQuYmaXWxbjPC9eYWTdCfplwv-ZTWaxWdGnmPg27pW7WTcEA_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMRyhW1sIu0WVzqeNZjV3ZtML2uHT1E5pQMDEqpJ_kjfOpw_YB2Bw0UMd5LBTpss-VP48pAPKC6Uprf_KqYi6w-zmDgLjno6oB7pvhrFB1X-_TEov2vhkYa0cay_2EukcTeDVR9_-1A-4t5jxOj3ZMn0ByAx0MOj6GdO3II2a4lFAbwAxzRH5sWLf9vtbD1zYbxwHZzTP3lrAwwrBNHfZh5Dbvh6_wVZ_ea-yLkftg-m0iEw6QfOKOL7NYDRYfnCxj9dD6DzzTebQ5f6VWA9-63ogskv3cqrwrSy5hqxn_VV8P34xszoVEryVei1XmUYvrz1WlhoDGJxrE5lfcKjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtmNsc_8k6FmzGPi9viwfA-jZj6X07nHkZZyF7XghbNBnr_-V7R6luGd16Bc3KZRODULOaJfiqP2JHxQxTTDl-oCL6YklSQ0X7nVc-Dj20DKbuH9JXsGuHVRh0wXNhq3ifC67g9t0NZOGAs-8ZJOHEpYf5aPW9Ycwbzji4zGoIt-EDJaTGLroecNhdMkcWjuedFVsa50kOcMCbMdBeONtIM0Lx1uPe22ZKGEv-bhgkjBa1Y49ymYB2VYPCxyGId3L3zPhJEwWPFisZQn6ZfgDZPMlDScn2_AuqW0wS-3y-MwVCc5AN_cisxoib-fK1hQ1IDMwISWW7WBX2zYqNs8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHGAoAJ-QGWj4hDEMkLcHvnzNtTBLrUPDkC7RZRE9QA8iZtAjK-sWsaFHkDCe8uif6JlHwJLAYDb3DI3dzJcmj4XND_TOs4vbygUa7m7_UUbCe_RLrBJzd0dtD25JtBYi1Adl74CMHUSG4-vjgcXM4kwTTJGUhhyFfZ4hBY-W1XMyyXHOW3v7ZTqHmm2QcjOyW5QNklTW25WduUjoE0kq3WTdbJxIzLeCAf9JIXr9tGFisgJr9jIoS6xIJNVCIXknw47RO8XbAIkoGXPLP15L7CP672jU8gknMR_bs7lvHltxxdsl6vIvTVAZhYFr7AhG-zpVhuvGweqsh2uBvczRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jtm2Y5M9jUXuRPPpCvhN3l2_x8p6nZ2uY3tzFbgC9aK0qVkfy1rlg5sWnOTTclYZa0lzyQmVuJo6T63URVmxciGSJSTAl88addQM9hDJ2RXMEF5_GgLBCjW-NCqaBkkc6KZh6hBP8QCnlUsOoX8Qgst4SWmH3oKZmpXHbcoIu6Hs_x4KHr0GXgkf_NmNiGxidaxfDiKUPHPpeKGAFWQ0HEHRxW5MIp9P-vGt9_EvMR47aqvo1rCgOkzsCv3VT6xnPwfkIQ5QXHtdDNIkGnWYgsRCXkO0jDs9l-QnkIrTYD0RIv4TBUbCyNwqhhUjfRk2TY3iFk2VlJGXD3_7lOPUVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpY9Xyf2zAGBCOywe3VAGaJMSi5TOOi6RiMFv-egkyimw8efbBD1sEH08K4q2y6kF7pt7WwzXc5UBHfGHjiq4RT0MYJfn5pqh4ZrUeAjE5hdNvFhL9VlAyN9gvuG5puuSLk0IsvxiVmVNag0Vd1cZZtWAbKkk2_9ZwgTCVvt6aEjG6dsfe70DyDORONIuleBAGgxtiZZ3VVKPwXjHLejhIvrfav18iJE_XqzRQ3gvNO-8EtjESPV3yrUg9YgG6Wvz8k7fkeD5iZ__W-0a23AHY4L0xHuxIatnnYOl62xGy6hA2sZV0yuBw6KWFExRZolU-bdXAj1HYB-pS8GNNFRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5FN7fy8T1LHe3fqMK6uTYSxPutujgcdeSdCNxN0CptpdNVQESAgSuUADEU8qFs_x1L_I7vnUb6QMDJwNcw5KxFLXY9LQspH_tWVI1sbxKNHPut4WZ8VXG3GDY1LKO5iWGszx3ETGS6QFyh6dezzxPH98eT7-oVj4o51TYEHZCMkhkNmTHwoJUqWX257MOdv39c0Yzaw0GqY5ZvjqW8LC6DNoPz48f9Sz06-Kl8yUc7hOU_mmcPvbB98a_bkm6v4Aw6Gx1SZ4QNnQwwKEKrrgSe7J6vrDCVYQY4JVvTDY4RldThxNXBllIqktATOSz_Y2XTBx_y3EEGlE6Y1gWA9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJ-upZKxdYAEVFs2tyEBqfFDQgRCVnVH3UQWFt81DPe_jLGNJ7Vf6FoLsLnwwm5eJ_1XtdVxjcVwyTntixDyr8HLfwrVOJuFY6Xmiu9gs0VpAx9UEiB-fZLnHYyJHGwLJ14UgNm4p9qlEXbPJ6taOmwAKmkaejdfi1I-lVCMclVDA6vONw02BY0ic2EdKV-O9iibwdac32oW983_ljBTsLib5v2utm0z335HeqFA0nBIS_U_FUlwYzTaTkEpxMvE5bTe1fiL4PXe_UVahazuNCA3vSwCe4DXS0e0SaQshLkcJyRywSEmixC0zA6b1G9kyCPTNGK2B6PdAoMooxiM8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=rcA0OZpdDdjs_uNUqQNL_C87pbDE1BVpasuPcNC2xmVLUOkAtcfFIBLnUMoYY_SdC6btUEcUKrZLdEMzQIWsUJh3BclFiyBdd3BMD15Oubt0nRcILPS1siQjNY8-POlhNVFT82t8cWKZt1rrlCqIMiCQHOyOwS2_iQmmMcL9aeAT0GTJTTQzObYxhenX8TOXlU7KAjh8u5k4vAlYHwbB5aBxDh8nAFIGxN-Uv2O_043U9lKa1_c_LZ5BFypPDGKb8jQ87VsXmlh4LsXEIdjtuYLknO6b2ugi8wqrBKe2R1YYq2lgcFVchQHk9Z6kB8L2FHGlIkb8xysJznKnXlUvRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=rcA0OZpdDdjs_uNUqQNL_C87pbDE1BVpasuPcNC2xmVLUOkAtcfFIBLnUMoYY_SdC6btUEcUKrZLdEMzQIWsUJh3BclFiyBdd3BMD15Oubt0nRcILPS1siQjNY8-POlhNVFT82t8cWKZt1rrlCqIMiCQHOyOwS2_iQmmMcL9aeAT0GTJTTQzObYxhenX8TOXlU7KAjh8u5k4vAlYHwbB5aBxDh8nAFIGxN-Uv2O_043U9lKa1_c_LZ5BFypPDGKb8jQ87VsXmlh4LsXEIdjtuYLknO6b2ugi8wqrBKe2R1YYq2lgcFVchQHk9Z6kB8L2FHGlIkb8xysJznKnXlUvRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=QOAg80jRUxlo_ToIV1JX8OyikFGTMNWs0o7w4s0lS620PAMDwsWaEk7jEVqnBhE54KW7XEBK1jV5MF-82fGTWtX01W_8v2_LuZ5R9KmiCbp2__DfWCryUV0ClWmy-yqrspijt8KL_ib8iaYlvIqfbhuYZ_5aLThlhFDqvWAirBtl8nuB-vOMn3OXC4kd5P3MhCwRh7nL6QbpqIXhGDv6FeMhm84_1pB750XAhasGG8euKXuHEnM-f6SnkZKmM-WmlD3hp6KZ73n5cHqZsfvW37-H0P8fhMS6NpMUy6W_KLf5CB68xKQyPMcDYhkuiiFBynzyzH2VCxsbcU1_4tYvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=QOAg80jRUxlo_ToIV1JX8OyikFGTMNWs0o7w4s0lS620PAMDwsWaEk7jEVqnBhE54KW7XEBK1jV5MF-82fGTWtX01W_8v2_LuZ5R9KmiCbp2__DfWCryUV0ClWmy-yqrspijt8KL_ib8iaYlvIqfbhuYZ_5aLThlhFDqvWAirBtl8nuB-vOMn3OXC4kd5P3MhCwRh7nL6QbpqIXhGDv6FeMhm84_1pB750XAhasGG8euKXuHEnM-f6SnkZKmM-WmlD3hp6KZ73n5cHqZsfvW37-H0P8fhMS6NpMUy6W_KLf5CB68xKQyPMcDYhkuiiFBynzyzH2VCxsbcU1_4tYvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=JcEEsl8IdrV2GSG2BcKCCh31gxS4yy-og1EJpzgmIcx2sB_ueqcAfqn-L31NugsW26OkOQQ8l4Zteihpokl65WAiS-cnspuPoeLLotD8X9yWtpKVBgxWVPlu1bOW41lzdgkYdXy6JalJzdKEZ9R2vdKvP-0arIvXrGLnQ3BMApovv4Wge1j9Ai4DWWaN4mWfbIw6n0JTgFabZpBxfPQnzh0USVpVzEctEEhohVESCh7H-tewEQ7sx8MBrKV_H3CvWkuYBUkWEwjPqdKQCTdb50klo3nQ0GpIrE7NHQXGTsJa6YvoFaxRQTPHG_awB4r7Ldw7PATzDYf4JsG4Gx2x_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=JcEEsl8IdrV2GSG2BcKCCh31gxS4yy-og1EJpzgmIcx2sB_ueqcAfqn-L31NugsW26OkOQQ8l4Zteihpokl65WAiS-cnspuPoeLLotD8X9yWtpKVBgxWVPlu1bOW41lzdgkYdXy6JalJzdKEZ9R2vdKvP-0arIvXrGLnQ3BMApovv4Wge1j9Ai4DWWaN4mWfbIw6n0JTgFabZpBxfPQnzh0USVpVzEctEEhohVESCh7H-tewEQ7sx8MBrKV_H3CvWkuYBUkWEwjPqdKQCTdb50klo3nQ0GpIrE7NHQXGTsJa6YvoFaxRQTPHG_awB4r7Ldw7PATzDYf4JsG4Gx2x_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgvXx7eIqsJRK-HCD_cfkEmoPMcxSIazjVnH_1WVIROa7hPigJhIUja7VmJvobQtJThJwDIPyF2lkUc-y9ttL3v8bNDNQI9cH5l-bfmg4FAINjOv9IseljOF1r58pZ8qeQ8Q4KopSflYjI-vj6d9qRrj4CKbgEeFgPEvx8ZETlxkAMG3tg_PJRH_wO2lJAVQvLmGQN45DYCvZbIyxD0lfRYmZwyA35pioW5wqZ_qKkDJkCQVWFrKpbi0H2AzQcpvuXHFaBO-iVaD2y8iMc6Ok0CHCXMbawBEoeuIyrAmb89-tv6UX84sHfkH98qXb5Zdm_-BSBKb9rXPe7YIDPCb3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG9SYs1620oFTxrbFhxtciR63JblncSGu73g4AtAeb3fBdK4Q1xytpsvopOlawTTKPhX7Kn1YNS3852icc7WEtlxRiitk82sPu5Aw_SIAiaWSKz4h1rZsiBA6hfAo4bsc9ElDWpQ0HwpP1N0iFFC3siDCto0CkaV9P5eRTlMED9KdL-3cyxo10PhqZfKJryTaOkmVwOiAWjFKVIqUOSZnntAncCKRl8Z054v5OCbv3DXdSt7zVY8X73joPJTrjzGJLtAbRgXNcn9tdGhr9nD0hxXwc9_j7Iaqk-ZOuo3_u5YrZyiGFnIUKwShexN7Uq4ZIhG1zXiaiCGX9Tpu99dZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9CcgLlHnh9OYl2iKiO6ULXgIWdWk3dvyKvlqodlfHzTXwzA3jNWTIxnJIfDLdF_fOQyV626vWRJRyzfUnUwY9guyspYRJ6sI7YmlX2dQdQJILyBYQHVrni2nBWWtIpDj04K7dCA6wih9brHFVzdYCxeUitimZweIw9fLsx16REaPpy375sbnQUoALz1zGbl_AufZHvr_-yk0ur0_C_pXf3ZmBFloXSKtGuH97TdNkUw3LoPf9FuzRBSxOboOyoEAX1iZSG7oL63Qcrogr8lhEmdATowIrfaEZzDCjKDR07vprbid6PVfjzMdgBTIMxYNueqf1_gn3E6LzL3ZIyX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOqKnNwZ4xhBevCBU4o1Yi6vbYJXhprsVnZdJ2CEhIFGx7g_N91-hbl4RuHcUVY7GSY_INuLf-hcHzwXEHW1UUkt9HLXpqFTe5vB8WBkLsVbsHdPijAIduBszeB2NiM-AtGLpSrKu7Wh_gEFyE-4YpdiYYzHNPTNyoP1r8dQXC4YwtlFLGDew3oU8mOYQBw8CXzMdEezsJRT4PHfIvKgHdkJJVFdle9LuoiJAGCh8UaBSYQ4OLBmj88F8IVPHhJhh2D5iYUGVAEX9GwjUictp8ZOywqKy0BdxGkqd8vS3wE2xmg8LUysvrWSUy_HvyxRDT-hFFcIg5QrzhDwngDK3g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=EvJ02mfvGXYtKEnToVpc6jYR3y1xQ9nkOhDef2t4mScCbsmq7SI_pIn3E7j7wwN4Gl0vAS7iQWEAa4D3zBG5OYyKkr_jpwGFHCAFymf07s4WHghYXDBihu1kTratKw5O9RONkwqQ8b0F5v_B6XsDMifQTrJfmelgWO2SiPmX_228Ly7ztQHfJv7G8kfyitG8AWKJYZW2QpEJloFNV3XUnu4o6ZE_EF4a5reg39rlk7rlu4dKikHyhc_4x2Cavo5bU8zBt_AtrxhOenUhX9V-7BnZKXL291npKU7vV_aDJrH1DNwbsdjEZSFUI7tlnknBJ37xYXi1_gFN_94TE7uY6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=EvJ02mfvGXYtKEnToVpc6jYR3y1xQ9nkOhDef2t4mScCbsmq7SI_pIn3E7j7wwN4Gl0vAS7iQWEAa4D3zBG5OYyKkr_jpwGFHCAFymf07s4WHghYXDBihu1kTratKw5O9RONkwqQ8b0F5v_B6XsDMifQTrJfmelgWO2SiPmX_228Ly7ztQHfJv7G8kfyitG8AWKJYZW2QpEJloFNV3XUnu4o6ZE_EF4a5reg39rlk7rlu4dKikHyhc_4x2Cavo5bU8zBt_AtrxhOenUhX9V-7BnZKXL291npKU7vV_aDJrH1DNwbsdjEZSFUI7tlnknBJ37xYXi1_gFN_94TE7uY6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=ZOFib7qtP2YJEAVlYKArQVmUbp06sRlV67BZ2HpHNoQqrgzCzCPoXPnncSK4NTdrAYDzvTerPVCZGUQRRsnwHMPOfqzLLRX08kPvHHetxK9Px0KfFsB_7T6BWUjsa7jGaIZdTX_jjMbTLIm9KnOfRBxSLqdDdSQWCubPFZ4tJUHe4D_3g-kcsVCIr84JtxcyXUTjTGoXZfF9X3pzng4gClbNyUbSizNxZqNo6VgIpOx-cYUQaS8_b6JwnKosKTRWWkt3-5KOxqnMfq6tcKpnTelE6vf5N35LmWZdG3ERCVeKEkmwdd50dGm8haVHCQfyAkifz9fQL_o89XIWexc_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=ZOFib7qtP2YJEAVlYKArQVmUbp06sRlV67BZ2HpHNoQqrgzCzCPoXPnncSK4NTdrAYDzvTerPVCZGUQRRsnwHMPOfqzLLRX08kPvHHetxK9Px0KfFsB_7T6BWUjsa7jGaIZdTX_jjMbTLIm9KnOfRBxSLqdDdSQWCubPFZ4tJUHe4D_3g-kcsVCIr84JtxcyXUTjTGoXZfF9X3pzng4gClbNyUbSizNxZqNo6VgIpOx-cYUQaS8_b6JwnKosKTRWWkt3-5KOxqnMfq6tcKpnTelE6vf5N35LmWZdG3ERCVeKEkmwdd50dGm8haVHCQfyAkifz9fQL_o89XIWexc_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnLsXd-znPvxHf1c-7f7m3z7ydz3Ep3oOKY8z7JNd6rUfpuIIPsHCxV4xIzikgrAmxx1MDk-xUGMvgFkhvo0g4q1gohZ4GL1Duvrg2AEJpuyY1lmXL7IzT9iHeGiSsiVAHBfREcqHGSvqvaeOQK-ORyovGycV9ml0qqmQlI1Rd1xeNNgn3Ye-PPzeUS4yTo3pASrRs86WVqpzRkZVg0fVEdKN88Be9_IBIlPec0mZvKvwcHfDdTrseqBT_VnU5zy013YC8W9jQ7_rjR_-qZJpe3B-PLDGXYMaJprN3-9V8Ipa4OPb2e2owm6b6CwVIxd_ZQ-YHlqbmkm907W7fjDgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGdYsELZnniEZ0huh05lEBsFLpp4bNcdCgD6418TaruQHGr8GKS0AVmqR-rh83dha8Fz2GWxK1iRC6Pr_5twOv0uRmz5g5pP6svAHr7Atm5I97FtjQXa80XLLHRjc64HzpICugK2Koh1RRNRmxDgsVpLxW3-In8jhWZSymjmONzRTelD-WmAAWi0bzZ7oShDcFj2-1MTA9-wZ1rE-ItKr1bXIdppumZ8r6dUTjHCVC805AN7-FadF2SLcsj9eCvGw3dHmHuz0anoYekH3R6RI6rwnsUXhWmFYUhGCguwkWUCYwe9pxsCU-PqkoxNL-L1VlaEYmShKGgmrtd_RXm5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDy96LdBBi-ySQdUc8mBVlrQlMr_JZL-BSjduJ9ca3ySRmgs_lijZoCV2kTraQlZ8tVgx7Ij7YDtO_puFT2gh9ieIc_b1tukrextz7XeVMsWeZi5UvYfbmddaBmZ6ICQqKBdaj3r7pFln1gVEWpEVo1GIdm77F_iC2azRO6IeJYU5GsC5pBPPlydeAONwbQx0QPVqMyRbH756CanO0PXMZwjxsGf5GkEtKXbJ6LmCH6AsGHURo2xW2_nvSwhG7dYOkRC3NLIzscGmCsbD10vzzZtndO6BqjrI2j44bYBg7PKrrq1e-k6-p89PYlavT0Fg9DUNVgkqhjI5ZE7oRDx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXD-vs1b9Yeb0OssMoPxTpiK3_Kg44KYyWrnypzcewEM_RFtW_WH52UAX4mceQhV8Nk13Ylcop0or54tjVWiZ0TUGJjme8qO59Uktb43ING_-nQYXTuK_EsAX-sZK5OhcLk9UC55TnUaxEI_c0pcQlaEE_eRxsdkLtRN5LoSLsfNUFrbRe0dTraY8OEc1e49340PaDxmFVlQb0e_HdPGGSWjsw1-bQo_1KxPWtzmVUgQ_7htr9zbIIU8ZnByDRiungY56r0E6Z-23arn7gJOJJn_uuGz7aEm37PAN5x41qoCu8vxdMDwJNt_uYd8gcVx-JqHoC7512VnyDY22bqAXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pivUP3r0LytYWYcvLdJNDHVm9ezHD8-IvP8Phkyr9jAJsxRYe7LYb6R10AVjd4J7I0IR9mrbi04ltCbPWDt9BJ3J7qfs2WyZIzYU3VCCYEqadecMaJfkvxU6-5vWXYOf1WGLwhxWp_ADlRCr56yXzjYyhf1ahJVFLWNUDHkUUxh-whEFHu9D7hcP02eG1JE1LODlaztx9gKkAN2kROczG2bA5MD7ZVnanJuZiyQDEdQPLvKsn0m0sszGKm9md0NgqVpEzOed3NL_0tty2ArIEA2lQg4qdKpTghcELPLRkbkULpDnUflPJMqOIzfi8RtkQmPGac-Bek0RRwNx6dhWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCGZM9MPTR6u9wEkWsUMAy0gJg95-S31XTjSaT25AM-ZQOU6DjdVW77Ag30czsQ6vv6KzB0RFRKUGAW9hJD-IbUEpkp15cO_cA5-_ku5ZjCICWkUFYOFiqJ1ADsnZ5s66wtZHgpE0XlAeL8bZEAdcyWmdI7Y6Sl1Qte2JR0_DQMJstSvlwyaiUiKE2Jkwf7c5ExojiPnRjxeFEoHXejc6u4-bD87Taep6G6aKzReIS0CRBh6a6RcpIBHUQRgeAhze3zAstf5jJXPCbhEAJtkFZulR23tWC4uPYL4Lr8iZsE_0gLTUc7Fq5XUl2RDIuFGihx3CN9vcwLqppR0i5JbOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g227jmshUkloBAZMsCVENnqWW2bZi2bQoGPLfo9sQi7y748eTWcycX-UDOOACRZscAIN1BNhNVTx1hjd-2mbjcurk6W_nSGFrWubQ7u2KBunj42LR6PxRuOC-qZcAkYM-bnLvNVUcu9Oc9gyLdG5wxX0O1Qc-KLOGTsA6n3L-5XZ6qEWKM5Q03rXfIQbga3NFoypMYf1yLD_1s0znQN6VeshwAjbjFghqMY68rwSxVhETQoYFQKfcNmeUsiXCf1rNVGGQZuSaFLdUMWE7jGZIZ6W4WYBYmvA_1p9_CsV3LIReyIa9HnOb91pj566HstX0bvvec8LdusVu9CVuqQDMQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=oXwUJdaggjTsV5tfvYwrO2eLsGOqfyA_cIYNER2Z36DdGy_0HXJAUi0S1Yx9p1UvMfyC-LtJmjeAsp7zl0dNGcpvAtZVa5WhPPT9_ZUOaNEEy35NqPVfrHA6U8h6ntwLpgps9R1r1_SG3Hpc24rwgdCings4Zf85G9PTzb0B8II-en7EZrksczYSx6nUqgdcZ-_uQV077JEuwqUDor9Do0F5KPmokQvT6wJMhDBMgSJ6u111foo1bKJEG_h_14FKUwgXtYFxBtp8xZ0i_tX9_o-_bXjRGSoMbrwSTbw5MhHvu9rXWs4mxLXPgfAV_SrNZYHB34xijJ_vkjmjQxeRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=oXwUJdaggjTsV5tfvYwrO2eLsGOqfyA_cIYNER2Z36DdGy_0HXJAUi0S1Yx9p1UvMfyC-LtJmjeAsp7zl0dNGcpvAtZVa5WhPPT9_ZUOaNEEy35NqPVfrHA6U8h6ntwLpgps9R1r1_SG3Hpc24rwgdCings4Zf85G9PTzb0B8II-en7EZrksczYSx6nUqgdcZ-_uQV077JEuwqUDor9Do0F5KPmokQvT6wJMhDBMgSJ6u111foo1bKJEG_h_14FKUwgXtYFxBtp8xZ0i_tX9_o-_bXjRGSoMbrwSTbw5MhHvu9rXWs4mxLXPgfAV_SrNZYHB34xijJ_vkjmjQxeRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=s34NT4uaIV-vtI6itVeVFqLEz5UWDZ99BogBEOehJe9aP0zYw_mjRmaCF7glHsuuE-tCuNf6DIb3ru0q97k-XVgM8omtQ6LU5EFEOvNY5RTiLVaoXhSqSMsZkIWrpL479MURsXPlnBNvIIH2Zvq05piV9YPXxZgj8jSOpl19jfvYzFtJ3rQt6nA5KVNun4qMMVVLI7AaNG4X73en087xeyZBWOiQqkuXOA-L6rN_ARVpUBGXylcTWR03Ooy3eE1OL2A39YRJ11fvxgZwV5tNBgTgKHZjl2arQ0xFPjMPHF0pl76rHMmBvNOjnhdy25cLemZntyk5V7HVTYk6X_sIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=s34NT4uaIV-vtI6itVeVFqLEz5UWDZ99BogBEOehJe9aP0zYw_mjRmaCF7glHsuuE-tCuNf6DIb3ru0q97k-XVgM8omtQ6LU5EFEOvNY5RTiLVaoXhSqSMsZkIWrpL479MURsXPlnBNvIIH2Zvq05piV9YPXxZgj8jSOpl19jfvYzFtJ3rQt6nA5KVNun4qMMVVLI7AaNG4X73en087xeyZBWOiQqkuXOA-L6rN_ARVpUBGXylcTWR03Ooy3eE1OL2A39YRJ11fvxgZwV5tNBgTgKHZjl2arQ0xFPjMPHF0pl76rHMmBvNOjnhdy25cLemZntyk5V7HVTYk6X_sIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZSGGMEkY5GAN9iV8nJ2JNkBxSYnh3CZDEC2j1iw7K6ASIx8bEViAr_UA5Ba9cYko34pnZqHsMLZ0QlDBpcXf3L0jq-c4cbd_xQMYdy3fNP4FBC6K7uXKLCPUokj-JRUa_IoyY39ha8CXbifSEE_QrxjYo-E6p7SLn9ZYnSMufLFI_E9tXbVn2_a_BXPAOcD6E-UpNJ_9YEeddizKGmguj3jxX6nhYNpYZY49jfFsQLl1TADddXtd3_7BqgR9aJORp-p5bV2q5e_UlpQyRQdqIPrrs2ObCpqCZ15HvmeG2IYkPGIMAxjLEFw_pFg3opmVs57A1ixWD2frmjMRLWzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEXZSvphZG4FZ9hpnrHx0eE7RpGugVe9BjKh6TgoicMvbax3yYt3RBCw4inuTy6kth_HTw4i9AEn0JDncNcCM_EVAN8lbszFooShjDU8P6mRxvmoyTshTV3PvlVn0H0O_W5C405ZyveXBYaHJZeOceZcWUPcDW5wwKGwH-E47V865zBeuSAPZWBeMV4vnsLRdV3XHKcpXcB4UA6k_wqlUH8f8wiVLKNkNGYJD-N3wC5uzCQ9iUWd0fgdxtJv8zUOaM5pvIzwAWwOM2fuVV_bsajytzql53vkG7yDisITwNcbq2bl3Ii_V5mZHDGkdtZ6RH37GDmd44ktSVc6oqIA_Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=sQbHPnnTsceBg2llrw0neSz_3-WtjNkEGC3UxGQjobkIwquMh6q_opvFb9Ogx_qqGzuuurkcxcU6I042jllg9PtfQtDolMCVTLtS3S3ln2s2AqDikXu7nF0M9o3OMsf2xzteW8mJVkfSn60g71sbPMXrddqH8wtI8bylpcJbCycRPobJ5zG3sGBo_dC1Z9LjwCk1K5k2Pof8J1E330jqeojFYFqb96BCsk7gAsxX0CxG9yUGxkaJcJ3P--HdovjD1IatM2t-bpsESqe0SUi3zgTT-k2xiSJp2j1Wjiu5ViKGIpexFDPV_t-XkPXUA2Onyy2vgsJuIszlfYo6UwLixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=sQbHPnnTsceBg2llrw0neSz_3-WtjNkEGC3UxGQjobkIwquMh6q_opvFb9Ogx_qqGzuuurkcxcU6I042jllg9PtfQtDolMCVTLtS3S3ln2s2AqDikXu7nF0M9o3OMsf2xzteW8mJVkfSn60g71sbPMXrddqH8wtI8bylpcJbCycRPobJ5zG3sGBo_dC1Z9LjwCk1K5k2Pof8J1E330jqeojFYFqb96BCsk7gAsxX0CxG9yUGxkaJcJ3P--HdovjD1IatM2t-bpsESqe0SUi3zgTT-k2xiSJp2j1Wjiu5ViKGIpexFDPV_t-XkPXUA2Onyy2vgsJuIszlfYo6UwLixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRNbKLaw-dMGZJOUgIXvjzyAuiDoVViX-5H_wkrsQrngHaLN3vY04IXBKhNA-VlaTsIRUin9OV_UTWk8w0SB1VqUzXGzI7ev5XdUrbUnRr4V5FMnxfnTyfJ4sNnxVk0DA4eI8P-ZBJQg_K0hINYTThU3lu6JqqJ8-zbhvmZwx54O8xuMlycln80qJ-GjxJgU5kp_cVe3tPdOQvpEmk1uDJaAHgzZn78vytPXc41x1sgj4hCjIbhKf7XTGbexXwvllaxy7sUTzH2O7T40_CvMcLwVpouigVkTlsQTaQCiP6emfp2ipvoCDjh0B3jb35FwMlyt_ITWitFWa0KiGZRNsA.jpg" alt="photo" loading="lazy"/></div>
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
