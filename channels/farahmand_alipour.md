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
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 07:35:57</div>
<hr>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq936ugl26sbwnyE8iB79fB7noR5SqHorlpTfEf4JWFcR4T8eaoDeYDG48FmljMzDqMRdMtFNeDSPO-OZuF9ZWCiPlunWVwEFQ48jb_HekziTxJDe8_xWOvuAoKcAPb1J_lZ3JmWM3F4ZXLbEccpXTzdxcw3O8Ykkk6FTIjNQ_wNYvvaawlMT0YMXXFwwD2PX-MScveol36gyZ1r1mGap2XVtIqv0MwGzLZvWo7DsOligRE2Af1fL4zaL5yYb37mvqLPOC-y3qfiEdAvsU--D3Wn10-8zc-pgGSo9zt1WJVytyvxbqwwYeia-8BK0elWrmaO8DheQlBRJhAKLBC24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvsN94JSKqsljx9mgbDBRgV_llqF_WAaZnBseHlLELQKKJ3ws65dQqANeVtfIJlnDw9bUkamsXNJMxX4eg__jKNzrsB0NVBfezZhjqJtYhR-RnVEK9Ckf5mA_EDe2PbsO1jc5aPs8PmMOp7tRRFSZ96-ank0yI4ROcmu4mFjI_To5cjVmnd47taemzRA5xmbn_UiuMpRST9nNDkzN5Xvrk5AnGgzG21bPRm0MWUsQeVO7Io2NPo7jATmNBZmLQjg97FZaJOthxu6wfddjrAGzlSlU93BlZwS4XZ0OI1MIJCBBo2EDJ72Ws3dw1s08pVb6fNIhm7-33CJDgroWH2PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPQwDsb8e5BbH1hHBk83pdT9vAG1x79B7h0LBynwZ8NPcttZT5t3RZopf3hiWBBIv7zpMES_kv-3AWxgm-ma703Uu2nAx4--3HQ5b5KK8QyprJYZ9Ft5P5S97-VAKMwUo-QsunXTOQ7KcmsjlmuzbaVXvSL1sfB4EfGoOvbt6jf_AiZTzFWg1_G0QFq4aDz7AkSXX1ynXd6PIOxsZVA2dbUQrB4xdLPIEoldADTVvkmYTF9u6DhTZmrAR6os34aoVIF3XBtbtST4oRCo3oUSJlUc00N81jLobAJ0zjLd2Nj7V9Xw9yrxeItMrKQxrMm4ynMaC8bhmRAJY5cnOCQO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc7NeffMHacldACBXwHgF5KB9SWjsA0sz6BxNQeeGnJE-jIxQlN9t2ErNgCfzeUItF56PxYjnHLcBuelWVdoGpaz1osWXqIdC7EfeKEE5uwz1T8dONu3kkzI1TBluBsnmvHxLKqmiyauifcRfTzMUhcRTWmaWynDqTor0yBJcRh3JrIXAu8Pc-s0wEi7jxEIWhYsYErpmZwhHuX8CYUWGs8mQdF2qt9y-Oo-5BgiVAFlA6afJTyFra4MDCbMncbOYi8b6pcPSahlaJYSjrN77QaZhCM7H4bMRL8PcC3kVzeH2v7OI9iex9515vHqU-mH0Rvt7oZ0_c_FYX-z5VjIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwSIuYsVvYEuHst8hbsHvBuvvk5k7_H78EJP-TOxZQ5XZTuhUHTNrHE1PVEdtwBfAtU2nO6G3O48JPO_w1iKjtjRqlM46sx6k6fUjq9yYSJeHsSPgu-Q32Sbj9GgspNw0jj-i4sUzvprsz9_nqyr7-6FULyp0FFytF_E4xKcARAN6HYnG_HIcnRjO_RHz4EULqpdg5NYoGHSnKs-YEAjK4us5wnH7HozUw2fDWCgwrhhtTO99sSdMr-UJaTplaoKM0R6UBHUSi1aGlzI4A77lSr_I9hGrzOFjjKhmWe8f9QmSyfbA7HfRCtmH6C2U_fCmUk5eWd7N-lxz9OegU5nSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=RW3VLxAgxgqeE-AZZMFgYu70W8xdEXVrj6yleQ21lL9l9CcQAC4a_y-6Ol56y-E6YfJunDIKFVUWAXdandecOuCe2c1K7dpr_KLiB5uWUlsLs4TucoonZEd293ZVbmRE6bvIGg1I5eKyvbwl-9acgjl8C-spEF4MNSEei-4ll620_m6NM7BFkhVzd6kBp1IohWG4zypDwfY58ihHLGrcTgQgT_oPHNn0HAWoXTWvO5YBZgFeLaqZU9Eabjjj4Cui6Fqtui1jNm_h45Tt7A2EmIg8K8ii0ml-elcg0EoUcANrwjYiPCZHPyKIscD7y8Hd2QhJoo2tLtYlIjWIurobLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=RW3VLxAgxgqeE-AZZMFgYu70W8xdEXVrj6yleQ21lL9l9CcQAC4a_y-6Ol56y-E6YfJunDIKFVUWAXdandecOuCe2c1K7dpr_KLiB5uWUlsLs4TucoonZEd293ZVbmRE6bvIGg1I5eKyvbwl-9acgjl8C-spEF4MNSEei-4ll620_m6NM7BFkhVzd6kBp1IohWG4zypDwfY58ihHLGrcTgQgT_oPHNn0HAWoXTWvO5YBZgFeLaqZU9Eabjjj4Cui6Fqtui1jNm_h45Tt7A2EmIg8K8ii0ml-elcg0EoUcANrwjYiPCZHPyKIscD7y8Hd2QhJoo2tLtYlIjWIurobLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=ltAtAMRr-OcC_ClHKJU1cF2SUujQf1sSXFbKXSAxzQo8eRZ4VQ3ciqTt_42LFUrEse_oCq3hPEPhdlADwDV8z6td4vjzn_2_8UMPiIl1ZKdCpqMXE1a08iOSb44TyuWga8cVIqgG-wrr8QDTiFIwEV4hgs8HfyumYy_LsCMENYbvqImoLBHfwp1MpM2qixY93XgNA6DVKf684oM7qWR1iF8DfOJw8rP-90PKMvaf-G7EfQOTOmpUAOW5BoajkOYf9CmhC8rJhd_n6xTJ6OFTOxd8CE6Z6lWUSqlgjmnDNbYdBJfcgiUPzfCUr0fWb_yZB1d6ZBqsyIuOIVico3Tumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=ltAtAMRr-OcC_ClHKJU1cF2SUujQf1sSXFbKXSAxzQo8eRZ4VQ3ciqTt_42LFUrEse_oCq3hPEPhdlADwDV8z6td4vjzn_2_8UMPiIl1ZKdCpqMXE1a08iOSb44TyuWga8cVIqgG-wrr8QDTiFIwEV4hgs8HfyumYy_LsCMENYbvqImoLBHfwp1MpM2qixY93XgNA6DVKf684oM7qWR1iF8DfOJw8rP-90PKMvaf-G7EfQOTOmpUAOW5BoajkOYf9CmhC8rJhd_n6xTJ6OFTOxd8CE6Z6lWUSqlgjmnDNbYdBJfcgiUPzfCUr0fWb_yZB1d6ZBqsyIuOIVico3Tumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=bg_EzlFWCRVMYHzMfkqTcGjzSHZ7tdzjNhH1_nwihHE7Th6jlqI3_qSdDgsBmVFSU_Rnq0x-sOEyFTug3EF-ewa0r66nATQMdaRU43ndwR369C-nCXRMeQGnJ40PyMraz1pEKb_kRFwgEdMs3tJVysWkURm9Zl__s3t0HptsaXMSx3Gt0wq7RTe-SZQBwadxYClG8dmlLcfJm03Afn97I6BrEiAy9BWc6oQvY98Qw2P_w3xbXztimeLwYpKgjT2sXxCfTcoq5FPQcyR1KURdKT5z2GEpOPQGnN8RNp-McvKTdjf5XCl20mPJBz6m2uUpmdJHCkfjo6tdVOGHJPJUtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=bg_EzlFWCRVMYHzMfkqTcGjzSHZ7tdzjNhH1_nwihHE7Th6jlqI3_qSdDgsBmVFSU_Rnq0x-sOEyFTug3EF-ewa0r66nATQMdaRU43ndwR369C-nCXRMeQGnJ40PyMraz1pEKb_kRFwgEdMs3tJVysWkURm9Zl__s3t0HptsaXMSx3Gt0wq7RTe-SZQBwadxYClG8dmlLcfJm03Afn97I6BrEiAy9BWc6oQvY98Qw2P_w3xbXztimeLwYpKgjT2sXxCfTcoq5FPQcyR1KURdKT5z2GEpOPQGnN8RNp-McvKTdjf5XCl20mPJBz6m2uUpmdJHCkfjo6tdVOGHJPJUtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=gdjBN86l3iFu8kKNBCLwF79O_yo4oSklq2ePMnFx5eW5WlL9YQSpfZZDLX1aDA3gE-sSDiaZGJlcNlFYEburx3jKI7w8qSx5ClCUbbntbM_WgitOugJmslQu6uBSo8WbzCWbs3W99nULfg6bfoJhsmMNk_L2RJIIRZUSfZVcubWMSZThzuP5Z7XlX2ViybV6_SA4fOAimizcVjV4tzX1-ol9mE-5YB8kgrwl8C6zU0dVPbAhp7zrMrEZ1XMZ0Y3WU6Vj0o9f40ZR9vyPFBC5AGvskj--_DrpktV2aEN-6h9QAoWtYKdF90U9Q67Aoexf9JusGBp4-f0jkNZ6YMTfPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=gdjBN86l3iFu8kKNBCLwF79O_yo4oSklq2ePMnFx5eW5WlL9YQSpfZZDLX1aDA3gE-sSDiaZGJlcNlFYEburx3jKI7w8qSx5ClCUbbntbM_WgitOugJmslQu6uBSo8WbzCWbs3W99nULfg6bfoJhsmMNk_L2RJIIRZUSfZVcubWMSZThzuP5Z7XlX2ViybV6_SA4fOAimizcVjV4tzX1-ol9mE-5YB8kgrwl8C6zU0dVPbAhp7zrMrEZ1XMZ0Y3WU6Vj0o9f40ZR9vyPFBC5AGvskj--_DrpktV2aEN-6h9QAoWtYKdF90U9Q67Aoexf9JusGBp4-f0jkNZ6YMTfPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-Xls6dvkSnorcL_TWPVZA0NOfPs2JEMj0nBuGU28oUPpCkcKNL-bDnuJZ1_gZT1g9FgVRshtcUeQBm11VRhbLOiADWLaSdaGuqgbpmLDutpPldVtYzdA6tKshb7nIqKUWPCbXyD4BJMJkfmbtSwqmiWgC8pqCA-VjqmEjcPKK77Ow5dNv3RW5aDZEnpO8ceKbWd8-MjNnln-pkLF8WXOPRvsA-Upyqyl9g86aPh7TyL_J3oNj4m8Wp80Ajhyr_h6D7XLTk-h5FTmMc0mxSjV48B0-x1lOZevq3NtraGrVgUpabrlZjCPvayrMXqljqC84VYUnXveaoEn45wypNUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfDn7YPfccVeqA0O4YzdObBW7TgrggGyhVKGZLMdPHoGsVQNTY4zvWvrF0NxygfceiIBl2dW-6I_ogy0Jv1Zit5J2bPvXd5-XZgvuKbIfKAjO86i5jiSdUkXdV0OWI7wM0aYnt7yAuSeGHV9VFrDinq0qBvEU1CXwMsddxGWBjuQ2o2MWZzA4GrrWgTFAt-gR9GgYA9pnHeZ1-o3e6HUaSMep9pqfz0pk9sdSgMC8alyxcNWDSw6qiyx6TnmbJeLGa_5domNoqZCTLwhEWysvBv5Sb_1Mhjmvlpkj-rCoq0b7qtyXV1L-BEjQpOOgWOxz8RlDtp1LGVJctRrY6Rl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0JpOEfwJ7tJF8J2OSp9stcopU1mwv_XrbmyJep-6xJbaxNskvE9bP343tgBAEV8z30tSubcRQi5p7elYmsPxTcwc4WHcTJNzZs-Tgoqdawbvm4sRpew_ue3GoO9iCZsq3bMGb0nEdnP0mM3FtbwxxOVscj3WI0dy871m-TCfe6QhiPZzenmOhfWqIXE7pgZeTnI2e8sJwpwLg6bxD27Mz5Ekvoz0fgQvRQSpTvm3eq4571pHlHZK-UfB4RughlJxQymvBFwa7vQJhz7A0vGhhNghvJ8wx3PP43gOQruGWrmTyCNJUqOT7M0cUTKB0DRBiA5QFVLgk_b5fQ0QMKT1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYKgmjHJFlKAgrodLRkf0GGy94ke-YDYrFl5NH51vJ-eB680coWE6axdphzCw7RejEnTPdaKpSi1aATlkqmaDSOP4yowg0uiDt1x81e-IW4pBzdiqH3NONHuON5OhjGCF5UryNpkJ4pEwzYtFQhiliUI-ET2Z3FwUuTAMflIvom-16cPT66fKdPh1fAd4V1bv3H1zIRNtqu7TLJZBUgOjF4nrClknfzQVHVkRWLxxxdjUC2fKzCBjsGhCBIsVunRzlWnwUjwJUmrgAB7wMaGDtYDh3odDHsNupbB2e49P8MX9fvtQ-O2chz_lL2eJgp-HcnF6ydys3XrZep1N0o1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC0GWpoZ4XqGb0bzF9FjjJaBh_L-9xTHsZAj6D4eoVheUAKVfO72Cf-60kIDiOFlAzh0IpwNI9Xf3IBWfDy2OJMCleLcpyjrHNtYIYZHcntXadE3Gaq_yqfyLoCfMoFxdJ4YkXHbcnZYmi_szjU26_KtCUMgbeGonm1XD5W6eM84GaXpjYjgtZYXiG7Oi_rZ0IgEKGDylUA9Do5fKXEM8GyDH-O3U_gpNElTcaR0ry3vXs1U_iNn9vKXHo3A288RUHDcsUNeX78At50MQOs7NhnmUhPKrQR_ptX34_G5Iq7GFDQHp8da7Myd6fU5p4ry7wg_1wEwJDg1DqC72DHapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH_6S7XbQeG8bQ_JdvmkcP1BQXLz2z_8veOQiz7POusN1javduWsdzq3l4fxb17ZnA-OUf6WFz1Z8yQJP1YRiE9PrR-oe8_NaB5MjIjgI0GgIa9Sy5YJdzMWNKaLryZF7A8R0V8SDzKIU1-F39tDGRIetcMzIEbCqn6Bdkw-sISrkQjJgekPmRKkq6KJltx5oRXZZHCuVGq7cTJi_O-AKRzBLHzUbynPbG8KVvOcFq67FfD16-a0WlSVJbKntJ-yNSNcl47HTMkT9jcOmEq_0RFwnqZN-RAJBC9tM_rAYQ88G0FIQU0ltqQl5wfV-voAJUhhcBIJBkoqj8ZdslIDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb5A920PjyBsmraV69EtIHqlaXM9MSLkk8JYISIcR2gkuVy7WKh7iyqLGuPTD98u_FhN1T3S3ZHkGVllclCf2xNhPw2UrbtV7rJIwV8d1QV_XrPVcuI-WvtHW00mHwJppwi9aqp2tfpK5saKBAJZzdnOZgUXU4g8o3E_QL1hPI6unyU_xabo7zm-8dS-dZaISmR-7-wpZO3jZPFlMNHIhHBS2Ag6uRaN-UcCbnTdjJrfPxLnO4PRAgzfXlA8qMB169XnbUWofa6D_yIAJwyALNmDUsgj6cgWdZ7abMdgvyZoOqLcZN2GKGSIj3JZfNWv-Yd9clLEhVU5j3DKDaHmWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=HaZMnsfZ5cS0ouXlx9asExrAuyLJT2bJTeDpBX0wFg49YHX_6fY5_HBTcSCpEd-vN90qxtDJ9IxW1q5KDZvPzS1bP7GC2W7-LlDO_OUxGAE1o_Um07JyWprNmuK2fQw_9g1QGsw9QPgLaYdZ-lo10T0q6OJPLOB_xTGf7iTo4KTo_5kFe6q67nZf_qY7dpfnwoXOfG4otkhe0c8TkLWqJoYeIud2a35yBxf5xu0SXPm2V3DVHvdyK4GEj34GOiIqF1-rEkJo9fhc3jtGtWSbjUjcxkE_820txTl9CW5NQj8xkHtBuSm7oQIPSFKUaaFlt1CaGcLXUyQNPNDzQ-y-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=HaZMnsfZ5cS0ouXlx9asExrAuyLJT2bJTeDpBX0wFg49YHX_6fY5_HBTcSCpEd-vN90qxtDJ9IxW1q5KDZvPzS1bP7GC2W7-LlDO_OUxGAE1o_Um07JyWprNmuK2fQw_9g1QGsw9QPgLaYdZ-lo10T0q6OJPLOB_xTGf7iTo4KTo_5kFe6q67nZf_qY7dpfnwoXOfG4otkhe0c8TkLWqJoYeIud2a35yBxf5xu0SXPm2V3DVHvdyK4GEj34GOiIqF1-rEkJo9fhc3jtGtWSbjUjcxkE_820txTl9CW5NQj8xkHtBuSm7oQIPSFKUaaFlt1CaGcLXUyQNPNDzQ-y-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hieEjFvkPUSlTk7cq_MSjd4okDEforM1Raez2kN-sT-FoffBzUP2UjlmXruBq8587oLLT_2u9vAKJAjWH7mhcxHPi3qeLo6ENcdGmhcGQNCYTuBhmgarbjVq_JLHIbyrXvw49wDgB0tURXb3mnANukQWSbx2plbL3GjlU0KLllyjuix7ES80vFM2xCSv2xBuyY-OSoCF-DJ2dQ_E5B462B4zYRarmG-QY4ybEYsUyw5rnrgHVSJnXC7iVzcG9jIXTygUaIcqAa_mYb41INt62BdhNnj1g_rQysQex6rQxAULJtY0vtYLikSWSyf92FWEhGIGI7RJ5yQ5WIgDdjH_Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BncZt44htNp4zydC14NNAwzIeF00QY4YntVdXKHQZn45DzDdeT4nKS_HbiwrQfYkM1ef0T_B88rT0HlFuoqXItFM3uczDL_pUrKTq6y2DDSWRbqwLbTfjCgCSP-j9D9SEZawU45AZn73voyZ1m5qrgVJZnUY8fGj2n5Arzlk3hsGI-iPdITBHseeABf1YNyZqBekwGz7OZAN9lEWdNVUnrRGQ05r6IpqvClU5g2wYFG5OOAesnCcdkgj-urOq8U5q5xl22i0tFB-9kbDGgy3bomjUYWgJdwZnmG53HY0cGQwIymUjHaa634MTemkukyJ4p50o_Cbdj0-ld-IyqvRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tjo1RHOZw8AJlsyY0nK3PbxjchxLCPzkJrrlMFnjS5_Z5mI9hqGKZ-0bwjTyB3GDsWvUoL1PEKBiuXzsnbkfSMFHAKKADK63l2zJFH-FkqkqPyCeM_Di0sASYh0S_HQ6qbr-SNeehUFb2k6gD_2ux9yhCToB1UlotBMuHEHl6sakOkWEqTpYWDVX0AQtxl27Av7eN5HdG4TYbnsR12B2RVtYMuyn6KZ8vbR-IVtcbT2En00d9ZXg1afDVuWgWvPVwx2qZT_NQJfspLJ32Wn8wX1w6WFuJ4QBYvFyptYvJN7PlHtGAJ2XhmFSDDBqhnBx4kOi0CoKYd9CHKdgMTtmkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLH42cadR66oeH2Sx83wjUpfQJ7RnXuDbLxP4Ksbde0WHZCB4m3sjIUerzZQ3F4qO0OajMIsavGWkiiBhUSZuA32ALA378KywznAgv2HpEQjbDDb3T8dGtStWyRCA6TudQbiTmFL4VK6lRM4tyvBocrekfdjDidX4oEdl3rebVlT152mimVq5ta761Alo7KvRJhN5csyUvQk-MA3ObJkA0FRy-NDvlD2iE-baFfYC1NVaVIAAS7Fhj6aNKALp7Kz8pen4CWYnT95KHOs5SnLoqC67DsIukjPYH5rwwyMO2z_2gwrpkBvLI64Zq1KCSeTkjVx0-Rei3nPceaD-zsrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-NnKsXwiW8tX7TqlRWpS9fwFefctUsfMyjdWZ2eKYg_EcEBZWYJH0jMvv2AN7i8qrmWoR8V8Zfc0BuX-Clmiv1kdjl7I33Nn2iSTyOCgJUJFex4hyuGhOirl0251ek9eiJsfdEbEj5AP0BwoJDe7cVuzb_Fz7MWrgw29WtoQQYUjCEmjn8Yk0yPqZQ6ucR6fIkhgCwcJLMuf16FHrSdBvn1MbyR0HDJw7m-1gRceOeSkwqnEHwWs8A58sPAwbz3v5rLz5mbudjtBJfL8zFO6R2L6UrkuDlcWgG_i_q4QAqCLJQbZYHLaZG0pvWlQ7Je_R33OnWiFdpFN6mV183DZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onSYhZ2KAw9EFM89vvd6AWst0kmrj1yBgEv4LBiIZkxZbPEgtpOdBSalFxEPBEGIqU7wrHipPPWvAYkqdPzbfouoP4GxPMr0wwz1UcwG9DMpG9NUSYY6DgP_foBeP7ekBLYFy96lBWWcoTaV-YJnRohDNrHw2rDmaX42TyuhimPP6AYduufWZ4k-tjzCOvZYrs3okmJWgiLgJnnnz0_sughEDG7dQC5ybkIeGVY61Sl_q2mj-x81lOidi-3O9rOvJGoe8ei_50vaqS-oUXBMJMuhUL9lhfC1upW6RroOkSlxhQCBkAqDlYJ5lcB8qBW0gnnnSHbb1DW5zy7tOMW14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4yNSUOcORd_P8xXW8p2zPDfeh0_fUztYB-IvzaQC88_xBphXuHjnM0Ljc2Q2-o7MO4eiHnnwHeE6v8pwKkp9VTuHUcjqv8cnaEt2Hx4VwKUuIyDFAmChm7m0WyMRhwyAc_qbh6cXZ1EatX0TFAzusJ2eNGozjoAbKh02PhZ-XFdQlnRIk6_o0crnX8LwsaipRTCGmcMF8bt9-s7QUF-3qWq59jaQpmhCTZAoHgo52pmvvRI0kGn8tdvs7E-XPXi_Twmiiy8A7COkXJgJQuebkZOU8UrYQ7asx6X6pVMGO9XT8H532GSw6A1mD_FjN8JaNYBFtxsxugUjZqeh8PHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SV9z_04CoxRqSlLphok_ir7F4jKnOTi8WY0E3mU_qYeXw8LkGLmo5d0hfBV0A5a-FP-2y1SAA-r-0_xgCRnMIFAq2zIreMAhvDYz8ULzzak57PTJr4ip03AiTpohdM8x16t9s9FtESRotDsqe2w66nau7k0bsG3-SkALIfGdY5lv4jvT83tvX_yDXfF3_4LJGReCZMDEM7vfJHoaj4FlQzXr0uP4MysSJZIyIigPlJAjjOl_uBKE5B_htbee125nma5FPZDuqLdz-hO0LsDneMTlg-GUtpao42s4kD5Os26ifKE3gmjeVusEenoYnTWT1IWMb5IiWgGE7z0GhaCprQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=f-AnlVY0B-AVc8jgjktCnXCxGp5sM_3CnmISPPI5oU20LRDbhWNmK1rpxrd7wy0T4AJr0m1tejJiZbdhMjZjcen220tEHxNyHWgkBfUN7q4OX1g23A3LDxcHebAbmZPa4hFqBQp685rUJQIiz8tQJJbC33BTmK7SGz-8pVpvC6CMkl66GAebe7o8Km1okIPiJqBorWrLlKsNAT2Uu6JUQ15Jv4LjJ4uCdd2CG9-AqNwQiFpl3LOLlD_oW8zmFjEYrr8nBSF9d9Uqn5GPC3E8EVNmccAhOR4aITSKem2K0rHvxD0390oFhDEhpCtQiC_T2fJ9eQHdv7PkK-n7z5WvTyg74uNfBWM6ZlDMdUAU6QqWVGqZ1kFJspQlnrlctqWzNRsYplxy8TlD0NpaP6J1cK42IaaszZJXqSGA6qJ26s2risg35hPyUeWZltbw-WadnbwH-Fk3mufJy_5X-Qa8sfn6KDAyHw7LU840AlJRmFGKMuZZ4vxLkoijVm83aIsMs6_8-0pQhucZ1h529F3fwvpOVb9Z8XgyVQSAVlxytRAn3-i3SsPgkj4hC_1ujEXZbj95-U4zfOQnEhDR4VtB9FwHDY0KUMX6qsMkzmvgxGC8bpw3jgJQr1PyYaWXgVhYj039HETNOZ__55mR6JeFfPlJXHRfLtdE8aw4jfJof4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=f-AnlVY0B-AVc8jgjktCnXCxGp5sM_3CnmISPPI5oU20LRDbhWNmK1rpxrd7wy0T4AJr0m1tejJiZbdhMjZjcen220tEHxNyHWgkBfUN7q4OX1g23A3LDxcHebAbmZPa4hFqBQp685rUJQIiz8tQJJbC33BTmK7SGz-8pVpvC6CMkl66GAebe7o8Km1okIPiJqBorWrLlKsNAT2Uu6JUQ15Jv4LjJ4uCdd2CG9-AqNwQiFpl3LOLlD_oW8zmFjEYrr8nBSF9d9Uqn5GPC3E8EVNmccAhOR4aITSKem2K0rHvxD0390oFhDEhpCtQiC_T2fJ9eQHdv7PkK-n7z5WvTyg74uNfBWM6ZlDMdUAU6QqWVGqZ1kFJspQlnrlctqWzNRsYplxy8TlD0NpaP6J1cK42IaaszZJXqSGA6qJ26s2risg35hPyUeWZltbw-WadnbwH-Fk3mufJy_5X-Qa8sfn6KDAyHw7LU840AlJRmFGKMuZZ4vxLkoijVm83aIsMs6_8-0pQhucZ1h529F3fwvpOVb9Z8XgyVQSAVlxytRAn3-i3SsPgkj4hC_1ujEXZbj95-U4zfOQnEhDR4VtB9FwHDY0KUMX6qsMkzmvgxGC8bpw3jgJQr1PyYaWXgVhYj039HETNOZ__55mR6JeFfPlJXHRfLtdE8aw4jfJof4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=p7XoS4-f5yhlAXEnB69Eni2WA26Eq2yFi8rxhKpug0Rgl0uztuLWYNkFrC0r7fzvzi1oqFYBgahOJn_DB4skCmcltx99u3Y3ecuZnKYnqKd8UlCU8zi1cnnFg4hIzSN89gizTgCUGJ6Wtp9PMyMFPiXADHM7cJ8fxX18UdanANMxppqfjotqqM7deXXBYjtnja9v7Y1N7qY1k_Aje3bJtFC6iEdCPj_Py0y95N6u0x4rjMxU7NFjzQG3i2pdCMqodyrCmN9Ut66YuBSgYiic8a720OMALXV8GTyjDleh2bGjMoY3gSJrJinYM2MhpABq8z9-GrrcRzzPNNpS1J6fvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=p7XoS4-f5yhlAXEnB69Eni2WA26Eq2yFi8rxhKpug0Rgl0uztuLWYNkFrC0r7fzvzi1oqFYBgahOJn_DB4skCmcltx99u3Y3ecuZnKYnqKd8UlCU8zi1cnnFg4hIzSN89gizTgCUGJ6Wtp9PMyMFPiXADHM7cJ8fxX18UdanANMxppqfjotqqM7deXXBYjtnja9v7Y1N7qY1k_Aje3bJtFC6iEdCPj_Py0y95N6u0x4rjMxU7NFjzQG3i2pdCMqodyrCmN9Ut66YuBSgYiic8a720OMALXV8GTyjDleh2bGjMoY3gSJrJinYM2MhpABq8z9-GrrcRzzPNNpS1J6fvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjGD6uvbm1BJAJnlz3yhvhICLIwBfpFsNRdHnkiYtmIaXF0-GwmFz2hG-LMYIa6gFXFpUY16gXDNJXj_LkEQSTN_ljt06e4jrVsDqVHFcScInYeuLwMsMTlCV6ZKZHgE4_5WNX5ltzJjTvv71dVTuCu9P0we3OUxSG4j5ina9ZPyZ7agNnmHJJ3cTBTaZ_Y3dv-bhW944qC7ddg9x79_5uo5tPwmpV0y1AggQBLyw1_E_fkVVSHXdQVTrP7Nsxdl0Ul9mySCYgq7s6V4bhmjv-sdnCaAJ6FAc_a0jm7IViYi23RnvjRWTw4gw1cCrWHorNtbJ5CWD_GLruFTTpKP4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkEZVVsLSaZDa4cqdP6Sc12Sr-thXq87353M8xgY-Qo4csShQh0_s5l2xVnMOdIp0Q8-qvkEFm3CmZ6LMX1nDjyNnYnZrT0AUD5g-Vxa4Jn_J5B-I8cZRmtQNbBsHnOTP4t4iVPAVKCdSoR2fVUT3TmfpZupmqnjRbjc1aA14PMJ-fQ9Yfk3Vt7URS6vI9HcrzOf4mfEr0gxvmP-Mi6msImYmiWRsd5meJczSG08hYpO-xS2F_PlTRi14ncm_2bc-3hVybym_2I_g_0Hho_Pr7ma4593QMC59cmqe0-IS79dFwrTWqyxdlqrm7mNqZNrrbPzwOXFCrVKjCZGcUl2OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbpf1IWMWyFdXvPtOA_fM7KLypVKSDHl2VU7RMeyJotrs3n07pMqrEgRRwy6sBeZEL84BGS6AselZjWFG4XTm2Unljuof8VHlTD1iAYvT1Jc8GYAdYBgcvVL9PzzbwngY_uRYXmW-ikmd9z-DekgNuWtG80W1-0vvbE2g0Sp0nW6p1-yrdg8sOSolTMduB_MZJE4QWivoOY7cXEqhdnFhiPbX5cbk8WmxS2-qjGoRidx-mNpJakoSaVea29TvgqPxM41ZvBUFYwcUOkwlTeLqJL8uwy3HhwrAUHXabneqMUb6YUV0T4Fqu9ANDL8uRQcUVoj-PSQHSLnMC-jWpnIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv09zhQXeyuSIUc3yKWFcDQwhyIcJpFB6Fc5fcx50zzv88v9YoKJ2TpEAO4gj_0q_kK6mM3KjSzYlFjaBQvvmofrYjMMeHzD-BxpXvnrL5MSQ1TpKZbTDLaGCt0ZZAontLl0ODulonL7Vl5uXNZp6UPeqCvWmq7KZKEhZ6VFCxhB0AZv3fFO5uJkQZ_LWiIA_EfnGe5ZjJrQmBH5rmoOUE7kRANQvS_tJqU5sIbSKn0vk3Fkd4EDaQfj4_4ru_KB9oJ8S_crKhnTQkuwdz1Odh8ptiA3gmSHwl84tDx1dk4PBEOaxJS9UsY8VXWApPS8AnvRUQRACZxDcGQGsA7IQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R81cXB7mUQKTrAXZm58yqOunh9JQW4VkqQuPz5eXxBj0oEnAzzDIJSJv2kNJ4BStarKiGqhkGHrwFcdepAa2iwgp_QhkmpZBSd1yn0Am8iiGqfjA0QqNioBPi87tgO85CizrWp56mCnxYyWyZPIIt0KR24N36C0p-bk1wtrUs7cxmHqMcDzDlU-P5NNhTQiwS-aB5sacthPdSqx8hfXuUQfrbgufRUmecB8eLqUHs_7uYmsMTPUgmxZLQ4a0Sb3ZVK0__sgxeB8mWq1zQ69gf11hnbcQ2BFbq0gCSvFJEE3ur8pB_W-TTyQCWxCs-il2_R_XbGfMYmOkFiht0ShfOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-kSk1ydGcboZu5Cruq-myIGZsVlEqDpcWSxMyx75-Suc1YlWtvJmeBAm448utEJ5V36iJVxOAd40vgEjFgQPCl_VjlaHku9nAxGvWBp6T3Zl3ok1FrJciDKPYPb4XQks6PQimIMlxx9EbCpvtOIrKG8amuguP2TQNNa5QX8FXuCDTU-R9aUIIEZvlVRGfgPl3e2BqZagd96rCYxdgKCab0u10RdOXBA3dKuawxa5TYM0IAa3xEKafJBY8tDkH05CQRo1F7peOTmdgz5H5rm3lflZ5DDNOJJ_oYhJu52Z-v9nQ2u4CWqR-GtXKM9mI8JPT75FbqVWlb6iiogyFpiiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_SAyuOZT4kDqZoPatC7ctuFVpGeGTAsdZmyGilyPiJUQ_dsAhDDavOj_ABvzYPk2yX3iblZKLPOsKCR7S9872cp6xBlAHHoRQicdeCZNTv4dgaVu7G-uSpLwUth73Dj4nQexCj6STiuiobEaxCyKAXW_AL98Yco1cXuFZ0d0AAYK021luQ3kFtjsQvdUecUmGlphVHEfMamKH7tHIqNKbZfSns9f7Hg9z4NVo8o8yhwt9Nt0L_edeVN46QrB7A1GwtuW7Nz1NMOx87mcY1HQw3LsbMB6YJFtFk5ICTm8sd2wB8YvhGwKA52j1kVoETIp2lqI5FwEJ26sXMYyZbTpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2_YkJukEAwD5L9-30tRX9knxNuNQHJtdUq2ehFtDG7JopYy1TA1L-xwUaiF1StBrRD3onL5F8I8c2H0k0cgAh8Wh6yo91muuhK2kbxdlf00hxEJ0MV3Q1HWFqwacu2hqxsGzqLiURsc03dy2_nV4cCvFd4qSfRDHJZRwGrtPqAFIi_pfUXbxjEKPnpAim6BpHfWXya_K249CEafWWNi2TCHyRANlT262jFbTvYoQLJByq5jHLumGgrm_VF04EVjRjUwRKYu6Ryy4zNgx0QkXopNiNVjMM9Z24TabwDxxsJ0XQhh9LxzI8X-EBfpOwjXwHCVk15_mMhbmK_fgW3Gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjTOHQtLZ76vP0_er7JqXPZIR6lLbmciC0DdAWjF7XhpYdCE5wWNPyGPvBRAtpTnaeci38jtTq3m_GfGJ2czmAQ_vQOLsHDJNjvnSxl7LszPOneOj-rmky2MZnjLu-LA5jBcoIB5-zJC5xe82JMVGYUn7CDzoJAjZkxpaUWG0iVD2KC2l6KraGwLmOnvzfcsAD8XUmTfgYGsVwaS-XSjLd4AYd92jAzHu9Y25RHWOf_0b-vW7-9HTTwAX5pfKos7SVZj3FfIAcpzdNpOe3kFAhuomqWWV9RGfhimXYd4zaxonJ__vmXm6okDSveM5Yy0vibkViFFqkuSKFQCt-VltA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=K-oRxvatbrKWxncFnr1uwHEAAQQLkFW7gR_zyxulqN68nQ2vcguBPlVBRToldddtUDZ85MjE7PpgY3ZyfqQ4mkicipFAfTJwGQJWVDEU924Vb4Lrla5L2xYHKl8f6G2h2d-6sWDfvuSy9dLO7hwadcP1fOfMKfA5X2453SKuQHbr51zL-VlphhrvcSHym_L8xyqzYTz4VeLoEgS9LT9TqkpCENwqHA-ply58XTDv3A4e8Ktd1RtOqDOUg_wVs35Rvhc7VIqO1sS8gc3jx3pigFWooePG4tA2oN7bAfA78bM0cPxVXok7qbusVaarViP_-GbS2I-d0-FPHeFbztso1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=K-oRxvatbrKWxncFnr1uwHEAAQQLkFW7gR_zyxulqN68nQ2vcguBPlVBRToldddtUDZ85MjE7PpgY3ZyfqQ4mkicipFAfTJwGQJWVDEU924Vb4Lrla5L2xYHKl8f6G2h2d-6sWDfvuSy9dLO7hwadcP1fOfMKfA5X2453SKuQHbr51zL-VlphhrvcSHym_L8xyqzYTz4VeLoEgS9LT9TqkpCENwqHA-ply58XTDv3A4e8Ktd1RtOqDOUg_wVs35Rvhc7VIqO1sS8gc3jx3pigFWooePG4tA2oN7bAfA78bM0cPxVXok7qbusVaarViP_-GbS2I-d0-FPHeFbztso1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b63gax155Ex0VqO4OFszzBLQD7ivNtzSGEct3bH7008P_DrBJItXtrG6gLaw284LdEXdDeGVnXWTOFpTZHiZj1neIxFbtwRMNCT4LXcad93_Kd41HOWcqQZQM9lEiXWWGBudP80jeeJJEe9oB6gmge-9wFaRH9PHBi4g4uH_aSKUNTCKF2trcrsbRD-BdAvj3C9Pyp-QUkn-PgBTxym5T7dy-AW9o-_Hl3Z1nF_wXsJw5PCjOjc4UdXKQKJ_WhP1zYtUxWQIUoThZJCZIKHyTbWiSy-lueuwQOHBqbkRTDN8RmbBCQivwUgEMOjaYaHZQSpJqG0HqB6fSaPWhhnODw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Eamh2RG0ek2KHZ13V200ugLUXvkrlJId21bLag0TdkP2Ey_VDAD0alYhro6KjkWCCNHn1ZhJNnWTLjaWT0VC_s0z8jyY6k5fUfM3UM9ohIfXZad-GoVxUqV2LlR2hMy9THpHt3ZLa7sKRtxhYn3Zs9Q5vK57ZD9RAssux7mii7p6w24NBT2zCOs86FuGKpQeDq_LCeMOVPoFYrpsc-DuLsEBrKmU53qwD-dI1-10KZJQ0p__7H6BGR0XI3TQyNnT2skJefXspDz-IWf8e_YikfYCo6VoC3Spf1gr-U-aS_GE2Zfc7ByjLcBjixdfPzsctenrvS3OJjZtGXuoUp4-5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Eamh2RG0ek2KHZ13V200ugLUXvkrlJId21bLag0TdkP2Ey_VDAD0alYhro6KjkWCCNHn1ZhJNnWTLjaWT0VC_s0z8jyY6k5fUfM3UM9ohIfXZad-GoVxUqV2LlR2hMy9THpHt3ZLa7sKRtxhYn3Zs9Q5vK57ZD9RAssux7mii7p6w24NBT2zCOs86FuGKpQeDq_LCeMOVPoFYrpsc-DuLsEBrKmU53qwD-dI1-10KZJQ0p__7H6BGR0XI3TQyNnT2skJefXspDz-IWf8e_YikfYCo6VoC3Spf1gr-U-aS_GE2Zfc7ByjLcBjixdfPzsctenrvS3OJjZtGXuoUp4-5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=RyOs-KThwbScmF5aaKz0Dhkcl3t__cKC3stFdxw6mOvfUVDS9Rtz5DS5f18dNJPfTHsFGjDotzXp13hIJS6VB6zxfrYqYExBtlE9D9kitGlsvvXA2c4m-T9nzcvEt_hSAmBN1qX4hLU2p_Lk6YFOnCf9pgnQAOOUud-yyDjX3p5CDLAUoi08aEWxJ49V3X65do45xLTK9vLQK9I3TGxL0Y6I1R_Iszl3Sb6WFI_6NmUyVPwcI1u2PhyyviVefU_Ndevn7HBpbG2tpGlthj6IZamfiB746a8IhXieTWQ8_bHrDujRgfvCcGS_r82qPUENfZbvBPID4a5_mFEIOJVw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=RyOs-KThwbScmF5aaKz0Dhkcl3t__cKC3stFdxw6mOvfUVDS9Rtz5DS5f18dNJPfTHsFGjDotzXp13hIJS6VB6zxfrYqYExBtlE9D9kitGlsvvXA2c4m-T9nzcvEt_hSAmBN1qX4hLU2p_Lk6YFOnCf9pgnQAOOUud-yyDjX3p5CDLAUoi08aEWxJ49V3X65do45xLTK9vLQK9I3TGxL0Y6I1R_Iszl3Sb6WFI_6NmUyVPwcI1u2PhyyviVefU_Ndevn7HBpbG2tpGlthj6IZamfiB746a8IhXieTWQ8_bHrDujRgfvCcGS_r82qPUENfZbvBPID4a5_mFEIOJVw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=ITwgnA-T91HHOquxEvHd8HvKgwC4kRqEy80zqaQPekdT76IXMdEmQFjhnczt1paGLYJ3K9sqz6OQrNrUlRNrCG8C82YVUHYxtlz-5ie_3LHJjVLMCakKXHrDLyKacxZeRaQb6GW5CAzGb1DPDQEf82j2-cuLxQA31QbYvUDWBrTx915mI9097Xukp3zaqFm9CJ1qoU-FSgHvnX-J1IiIzs4n6iFEzgoR7A17Y_KGbH9__z4gD-U6rLoxCXGHOOgUFNLFNdKSK59JBMZV9MPzEaUoTOBmVGo73RZVc-0Bqk79cWmJOubNbdmkzCymo2e0tI9uRkBFlCUQTLxOmPQ_Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=ITwgnA-T91HHOquxEvHd8HvKgwC4kRqEy80zqaQPekdT76IXMdEmQFjhnczt1paGLYJ3K9sqz6OQrNrUlRNrCG8C82YVUHYxtlz-5ie_3LHJjVLMCakKXHrDLyKacxZeRaQb6GW5CAzGb1DPDQEf82j2-cuLxQA31QbYvUDWBrTx915mI9097Xukp3zaqFm9CJ1qoU-FSgHvnX-J1IiIzs4n6iFEzgoR7A17Y_KGbH9__z4gD-U6rLoxCXGHOOgUFNLFNdKSK59JBMZV9MPzEaUoTOBmVGo73RZVc-0Bqk79cWmJOubNbdmkzCymo2e0tI9uRkBFlCUQTLxOmPQ_Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9VMxZG6SlF0XupX5WnJykrW_Oa0A__mDfknp2plgHyJ4BSXSCtDoqMs0cuctImZUorcAzWv2dBbgQzwJlcATkXb95TFVKWYe6UJn45CqTHIN_F9AvHkGBwa5FaleUVy8aqvSbBxIYwtndVOHjgLpMH1PbBQtyLnFw_jri1bLXEnG-bf0eQLVZCiGdiXsr2_Xba_oeohv3XSmZyeklXaweZWSuPeJdALWlCmH4m7uuC8MNIqCrAQnLPS54h5sjE1EKv0qsma0choJXWneRZnPm8Vo66Bg_RU4lbBrbreNrKNmN2Xir6YRkSoRB9JgBlfPj9bVYy80qbGi7G2a1Hmrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIIHW2JefzSoVYhwDVoeQhtYesIkeXZdq9LxFXisfu1KtKUVmU-4GvvWSVngewswgj__kYX_uoto1mLX5o_DIdD5cyfo1nE7rf6d2lDsiSFsylMJffYmSCh3lKaz_igdhS72TufbrGHDqkGXsJzBGhcZ5m1kih1r_b2L2FuUoY65PnDDE-EoqZnmohR0VsGFk1bb8bnjpn0ue7RiXsCDTSC-BNr6Q5vzOPSjTD7Pt-7tJ-dhml4qdyNFSpVjQmdLpncr5nIIPJiPRYhcmlK9hyvlop1a6YjQ-RrYFkJJBL8P_UsINc-mwAAbt98diHg_JXe8ZYNnxa_P6ihwkKnHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBYZoHIB--b2SDbjJjSaw-t4caueH-uaINjydbQwxErib--JOz-HzdM7RPfcIDhXIJdTmI68bZqkf5J2QF9ctACZ7mk_EuZv9Pg4wj-ApGBq0sVN-wIwW0zdCC9Acx_HUKMYpiYJVFo1VN50XEMnJ07p9WFkWqpWnhgOHrZZbB_DiFkOlFJwodhLSA_VBBa2dUWrE1cn7kaXGJ2l3tldmr3DGGq5bYQ9r3GuG60UpcLKRh-XXFxx2NfqqmoYdxE80Dh5LS2wEkLgajgWvH3x28SF8bJaPri7vwEvK2hEL5MvaEQGhgTvJs2KZPcjXSWW494KEivRcsReUgOzO6Nh8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arJXq_a8mTRyJvc8syc8RIdBAa1vH8u2lx3S0F0e5QVisowDPJx0ABy02nFuLZdywFc6us5O1AeH6uqRFNSO5RwEnER5MwWBHSJhMMnNgTEdwHBFEvbC56K6_5gb5GNPl6t9-Aji5DQVdQG38CgMc4_ug727P0E68ugBmb3Bv946C_W1cX2kdTGviRAksQR9eUv-6oUFmf-KL7XUiHxs73DulrE4lCzF2p-mCBT1tRxGhcsd2hgNrtbeBFxA8vgbYVA4PuD8fk_C_2gNNTxFVl2JXCdIRhF4tfOTusuC3nUk1ygXeCIsvmOTeXagXdqFauF8N4BIAMR6d2pQnydzow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIek6HNkT3suyDk99jNur4esOl5VwIhHdi9m7xt3gz3dgY34uet7JIYMVSA3cju9FGFkK4etGcZWbCD2MA5akU4ubiD7QEwIWp_PJXQ94nGGxcxQ7HoSu8Y_uopkRhkMMGyS0r0XtUCFsWV9lOUEtjL9GW6IYsWTpsv4ftv70fEujCqSSnG9J1uHCL8Qnsen-ocKdDS1mgH8Y6L4lSXtH-KSx7vfTb4TD-4jlBWjRQQxLkS0_6_GCQBpkC9c8rzE53E3mC2Tx3w-manTyQU322I4A9Nf0p5YBPFiPZu-gE2rHBlxJYB8Ezsmk_Hc9mCNrXd36M4VrXumW8eoo2agHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvOtFVh-WbPEhAdYtoMqQgtea-XSU1JMlzp5H-2w_ZXPtsbl6aF7m-P_8RDHsljqBZ1ggXpoLt_yyIP1NkUHVcMGAONBuCj_GWeunM81qDErNwILWA68SKlJ8vkBnUjIWK64QlM6QfGqY3P4Oe1ZJkwQXCzZ40NnTlGOOX0osF-dq4UQNcEbm77sa7XSKoofPIcRKzePveYpLJF3kfRe4DBrliz6Xe-OV2sDq2wLgVGpbBvbUEOQ966b9muNE9TWryRtcDFbsoZfG9IIYTKK0KHAQz68O4g1Nzux-xYTX7wBEf9kBFxfVOuvRtwrw_5Ny6BbTgR4FoTlQP8kKW18NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS3ttRHtdKjqkmp6eqqfLsyJELcRcO9XdopxP6472WP14wIqN23REtZeWAg9TOZznIl9efOXLZGPuWxjAbA1UbF8mmAB8fpIMOC2FmWcS-J9SYBgfmYnvTykvJH_S1XoUz6yTl6owkynh6La6Y9KApyk-hOfnu1I9-Fyb8K8hsEDWil7U0XzeAT0bWHcXiOPS7uLiUuYxNeSvBS3rTrn1tTkZ8-PZ_X44F2YfjrOT8fM9YgSPDtom8zQjIlyjft7fjiN_4DHjAOylsqm4ZX8EZPyWWPgcIfZAVZHbp3zbyJKOsoWaBlyqbfwgYUF5Pfy1CDe5oEMg0CBQTBHEi34pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbA8799BMYlXFzVYWDWeBHvD8sfKmB4wmYWu3f08J5wwiflomfhDqgPNuTq-0ofbFnYQ9r8J4ulfMR6GQm660meZgbuaXuNXmTqcxe4thp1MKtteDn3AfOJ2oMjQb3CgR1GRoVAW7b4fwMXB2tGrYrioc5KqzyZX5XaM53uyPpdiMR_w97WRD08rEHC0LE8n-3oi2GB8V-1be5s02uWiLJuy0c0hWREEcQbzMWZD3RoncbAk0-GuNEvTlMZhg91e97ME3o-XsnP94HCnapDuwcKRYBqT8RAde2mDR9dZwJovcfMDcxpY_Yg0EZAXDTmtzlkkv55ZOKpk9dCdF9vaRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=TN-EtUCmPXTYk41bdP7Y6GxIbxWI9kfSE5fq1JcVzRQ3zblZzDznlpQna8jIXctOwIW0GFCqaycE9E3hd8q-ndPvNowvx0vmchhNnXKTbMy-vS6_owJzARSl-o_VIhJZaulo7Q8hSEaYobfGV_FpZ8vGCzZIE_JvmyvvtnIb908TLPyVvsLg7SiZm2iB3pgwUCcyz4OVbgr6uP6NfMvCbaMzqw4CUy-8IbIKGeqJ5AjClZ1ibOZ3okr-n9crNgDyJ2Pcqy3RKSv-zrKaMzzIAZ2RhFfu4W8GKC3qyXK0TZXTnLiQG8-ywVksUAC4K4d6PNkVY6Wef8am9p02W7OiFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=TN-EtUCmPXTYk41bdP7Y6GxIbxWI9kfSE5fq1JcVzRQ3zblZzDznlpQna8jIXctOwIW0GFCqaycE9E3hd8q-ndPvNowvx0vmchhNnXKTbMy-vS6_owJzARSl-o_VIhJZaulo7Q8hSEaYobfGV_FpZ8vGCzZIE_JvmyvvtnIb908TLPyVvsLg7SiZm2iB3pgwUCcyz4OVbgr6uP6NfMvCbaMzqw4CUy-8IbIKGeqJ5AjClZ1ibOZ3okr-n9crNgDyJ2Pcqy3RKSv-zrKaMzzIAZ2RhFfu4W8GKC3qyXK0TZXTnLiQG8-ywVksUAC4K4d6PNkVY6Wef8am9p02W7OiFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=bLeh0t4VMLzIdqsrgCOXt65Nl86X8cPxJ3hgXWYE5CLCfpdbdH6VBEbXko68mALafaMCdrwEsEvk595JT-o7EPBcD7rbB1NJqVUushenS_y83l_bTKFqpPGhMUnuwPqG2o8dIKpVY9w5VyOzWz-bI7g8sDiMyK41BM2h5uy_l0iE_qa1mXV1X0jnI4WItEjhz629CJdlIppWNTe0JaYo5Y2ve-_mVVD4vyUmeOxUmXe3kueb_1tSKtknzQLKT-il1WiItqEdK-ubFbMNGYmRZECc77dK-fkSfnlrWYpgHmWN7f9-UvSj29RnUquglGJjlu73gZylaXYJY6BqIZpi1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=bLeh0t4VMLzIdqsrgCOXt65Nl86X8cPxJ3hgXWYE5CLCfpdbdH6VBEbXko68mALafaMCdrwEsEvk595JT-o7EPBcD7rbB1NJqVUushenS_y83l_bTKFqpPGhMUnuwPqG2o8dIKpVY9w5VyOzWz-bI7g8sDiMyK41BM2h5uy_l0iE_qa1mXV1X0jnI4WItEjhz629CJdlIppWNTe0JaYo5Y2ve-_mVVD4vyUmeOxUmXe3kueb_1tSKtknzQLKT-il1WiItqEdK-ubFbMNGYmRZECc77dK-fkSfnlrWYpgHmWN7f9-UvSj29RnUquglGJjlu73gZylaXYJY6BqIZpi1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=T5uEjdIzWePUOrdGpvFEmWt1ivnFSX21wBsLEIK6WmHMUlppE5pPKwYVR70M8iwy4k00qMUzCQZlpnWxKCgrAVcO-Z38T_I36_9Z2jnPVp07GmjyrURTd-nW4gmLUBodxtIZBEH3EIJ7xrUC2ROjBF7ThVKt__kUPRi3ja7ODJqYNJJDBOITP1_Mp4qBzd1cqLaSrtA6SEWwjQRfcfotGRy1nlmTyfKKiSKd8I38BBL4cxgvcXKLjkJDIeoa9S2ShpfE1sdDnEHq8w25qkgRjK4xrBtPEUHxdgRioKGOayJKhCnoZPFO-HjU4qfD4xV1VC65xTnjbjGS3ajHrt6OXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=T5uEjdIzWePUOrdGpvFEmWt1ivnFSX21wBsLEIK6WmHMUlppE5pPKwYVR70M8iwy4k00qMUzCQZlpnWxKCgrAVcO-Z38T_I36_9Z2jnPVp07GmjyrURTd-nW4gmLUBodxtIZBEH3EIJ7xrUC2ROjBF7ThVKt__kUPRi3ja7ODJqYNJJDBOITP1_Mp4qBzd1cqLaSrtA6SEWwjQRfcfotGRy1nlmTyfKKiSKd8I38BBL4cxgvcXKLjkJDIeoa9S2ShpfE1sdDnEHq8w25qkgRjK4xrBtPEUHxdgRioKGOayJKhCnoZPFO-HjU4qfD4xV1VC65xTnjbjGS3ajHrt6OXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avYsug-A1YU8K2EvKSdZnMF2bsYjy5IsvGgYF1-71qzX7PvWc5oX_GJFGgxULnylHzBx2SpQXvRcjNcuzQkIk-1ef9Lpcb6HaD-lxPOgACsQLjHAoRkvDSHEE5PZX3YqFwa7oTcs0fNCCuIwX80OkOmhai6Lwjw1rHYAtqwNPSJ9mmzicpdvxifxkOAgt2yO90GEUIB7-l6Jet-LRDIdXjh_H903PW_xlra4eWgSaTaP5qzEM1-jrWHx5dBrVXb6j3HODVOGEER2aTLRamxkOsXqJQsy_zI4c0sPl6UaKQklnb7zCPbY04nIj0PDiuOoFA1djp3xZ_5lAAx7JhwCQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf4xvL0RDg_JLOhqJyJs2Fa0zOZHVn0ZUktSi_5wt5AJUQXlPksnn0VrUbSIxMHHspIm7q_WStXXII4m-6BMnvyvTfB-5DAQtS0TiV8GgDuWq6CuDriZKllBJIIrXo9fDyfGEOYLE3I7oQvb-JDSKJuUTy1HsysheJB--xOODis34UnqVBT6GYEnMFN-D6-8Nla-SkBx9DIFLLX4YvlBFt9ez2sGDx-b5xzYFO-NASrijkf9c0AtpQtE-_D1sGqxt-RufWy2JtS1XXF3wDqYcUGYoulidwejwirxjVH9TV00Aq4gz6TnXQ3clY5bBIlYEDxZ58Pa-FbsLoTFef1X6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjHR1EsW0_j3BNWynDKtNrH3SdYZWDZBJwelKTgK6brOX7oCwQyyUjmJLz-uVFu66aRHeXtGkXDREYPnE2hV6biPU6if8UBZ-l4GrDNzYh-PlNLRgOfQr_CHsWMZNUWXKsCSR02d1OpFGdHRU-aD2qwT26v8Et7oTGqkxy4JeR7DLY-C9N5fUAZhg7gcnsCpjn1OF1vBkiXIPKTR8eTsdVYV579KF7Bk6YDbzpIabOClQWlU9SrwUZ4Kxp9n-6dvDNZ16BB4aaXry0wx1uzBGr5SyOyA5FGcnIlAthuLsj30JQqnIr4uUPZ4xXHoI0jEefp1PM1kiR9bYSyKxIlj8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBjEwAoLEF9sDaq1b4kGf98pDpogrNaDjMbwZEDr4Pu1AWkFdhljllHL0qU-DoFX7pCtoys8WrIF89IBMU3ICfsdnw2-_LvOgw0gLhM3Jjjxlpuq2Yaqtm6iRcdZlksORSRjsXrrvZWrwfYviY3zp9vcVwjVADml90muQ8J47O8sSPXknF7982-x9ng3usxBv2PjMsWWwlzemqkY7d5IqPrfxESMUt4j7BwZkwvWVLrO5Q95bDqT56Sath670LDRYEUopwHT2kFNFnTStnovH9lq7ArsKmxsvi03xW4QPFVq_LkY4PYL9zYlq_nFWvZijCvBzDv6j2lbrOkmdn4ZbQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=CQHCM7nKLPUXXzmiHLGyAqiKDYQHUpkp5IhNVmtxZp1pBzwWZi-Hu6CXCP_g9z2e9_WZSj-fFJ2oTYwNS8iVBzBPmNzXAL-eCm4HskiprD38uTKyt_1MC7Il7rYSRPhzlawaq44OxjUqcG5Pk8cEo85TtOm0F6NH3sabyJ8sY19raGqjLI3m5-GpcWZys8W-rNz2QnecfhDrh4A49x6-uQxCPCMJT0VmbY79Wm46a1Fw4bObjLiyJgHJxQhDnNBRIB44vSLZlRAZAao0YdFKundul29bY92Ctf0e2xOIiT3JL0jFtWP1SXhM-LfdIdi8uC7mpP7CkBYZ2lxb71jdvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=CQHCM7nKLPUXXzmiHLGyAqiKDYQHUpkp5IhNVmtxZp1pBzwWZi-Hu6CXCP_g9z2e9_WZSj-fFJ2oTYwNS8iVBzBPmNzXAL-eCm4HskiprD38uTKyt_1MC7Il7rYSRPhzlawaq44OxjUqcG5Pk8cEo85TtOm0F6NH3sabyJ8sY19raGqjLI3m5-GpcWZys8W-rNz2QnecfhDrh4A49x6-uQxCPCMJT0VmbY79Wm46a1Fw4bObjLiyJgHJxQhDnNBRIB44vSLZlRAZAao0YdFKundul29bY92Ctf0e2xOIiT3JL0jFtWP1SXhM-LfdIdi8uC7mpP7CkBYZ2lxb71jdvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=O6AFfdnSMyjcsA1YQFmfnoK93LzLgMsGwlPFFfXMh3B_c9p_a4XqiFyYmVEuwwVkzzhmcMa6g0Ge9GTDMxUYEqRPaGreF5VTn4LmKxXprBazxFeOdQDj-Z1jD2P9o_ucGzRM3wsRN_kIzbUUqjM32MLQKQlW8VULBLIzuM_gU2qAuGvix_0Cz7kWI-4qyugsYivGQSnT3e-QuYFhPDG3ioX2Q290jpr9V53pwOgh5SirxqU3WZVnGbC_K_8GykcamGGVrZ_7CaDbYvNe2nhPtIbxZoXitBpqhoBKty5YN9wBQYd8PhAPfVSWc0EvA44zrRgKcELgBlCYTAUa2eZFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=O6AFfdnSMyjcsA1YQFmfnoK93LzLgMsGwlPFFfXMh3B_c9p_a4XqiFyYmVEuwwVkzzhmcMa6g0Ge9GTDMxUYEqRPaGreF5VTn4LmKxXprBazxFeOdQDj-Z1jD2P9o_ucGzRM3wsRN_kIzbUUqjM32MLQKQlW8VULBLIzuM_gU2qAuGvix_0Cz7kWI-4qyugsYivGQSnT3e-QuYFhPDG3ioX2Q290jpr9V53pwOgh5SirxqU3WZVnGbC_K_8GykcamGGVrZ_7CaDbYvNe2nhPtIbxZoXitBpqhoBKty5YN9wBQYd8PhAPfVSWc0EvA44zrRgKcELgBlCYTAUa2eZFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM_EnfyHE-EQ9RUWCNperctLycKe-Tren7vVGOoilUNhG34ITg3W7pZlncvAxAK0Mgt3exkjOluhk5KG1SUEQ7EPxCDW1QatPJ3iPxeammT3PVYr8p7-p3Op7OeguAc4trHD53w90gKIRfQV69NAzSQ-D05-XUeO3yqNZcNJYG_hDZyRyTcYImUNPB2kvrbPXLQOqaeeg2Lx3fRumyCMTw1l99ap54bFhM-24BfZ7njB74A8ciCHmYbOsUiUR42twofFMYHPUiH0evShbdKQ7nEhym04gK3N0XH6aAENM7QO8ObWyDyDrO0uHp1Vb_2HQcqez0qotMOoTnMPD4jI0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0H91TwNSEdfVMHuG0RYMpWl2Ki1N3fui70d75-YiWwDlvu9YSa9vM67mV4DUr1fYZoaTo9ijSrVAjPMstDrqjyhIF-ux7ZszYH5DLHm2SeiU6g2FRzQisr9ndjeG0pNGlhGeo2N7yZ_DnFJVtdh3DNm6YXsS8iXtOTOEO4ut-P4N20PRWt9tS4e2903tf6iUd9_GjxI9ZmjnMJXZt_3ruPSkODptT2kD1Rf8MVI_94iqpzC_Y20WZYFh0SNnbg7E66CWXTUdAf8KPl6kUe5NlKxoB1T8JXcKGn-svmY6MmxqOCnwJm3HAw711dvno_3lLn2XN6s9-BeeA-7PlUoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqOaRYzUniMNiIX4gOMny59lvLOJUmS-tugazPFyzPPR2O6qH0HS-xeyLtN0pMI8YMc8AfLujHoGi8HRo5e3umd5BIdj21F0YY1BF4ue3k1AFX32rPmzZ_GYvhqhgD5Dw6KujIa2QaCD-OL8Jkaz72apfD__jvkKyRNJOd5EsDeTq7iYfdQJ4txmHvXJ5u3aDGvmMR_nmXSG64LL6UI-kUUTR5YdEgxR4kKAdkIPlsg7qTUbZpe-ErL8LNAS2zs5uFYQIC5wbsnimUdovUfhm_6BrnIqd8ievMP8fGQPxHJLhquM1BR9eLjrtEH4KK4CMMKs0MaxitoUCVGZzBigzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF1xeu9pYnOzBKU9uNf9up6C7KOKAsZF_JLORYz26hGU_TFqcJvDJ7eXuK26COxbhXnF7hz7_6V03fxw1qhduMwo60VGctHVc09EMxvuEZBYNzRkrEQlDXjx04N4TYaMy2JV7eBDD6u_ELiIwcyULPWf0ocxcBG-s6_4W6DfySizhuNJFGbDWQW_qL5JmlMI1tEV6RXK7H6FcN2rdw8bR2Kgk4f5mf7qowLdhJHopNTBfdbSrWlppZVkueyns1CMNyP6MsPqfcrOO3dSa4nZj1zafqZI7wEW-23dyN7Rs-bQvWJ98x2gvpuf3mtADtTpW8Oy0b8Pk7QEQp2f4lW8xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMO5o4fkqaBbCldyWL8cqsPp-Rbeyoo9entuodxh2hufdJAcBAeGClybmdtkVPN6Fyt9wt8XwADlMdlGe2mX_fs827LpvQhoDpwhn5jdKiFwCAPLjGkQrheskZhKuL87_4L3Hp3cZsgwLchXlJCajohiInX59cSMrGX-Dz13Un91pNC3UbYmN9slNfC7y7r-6CgleGyXl3DyftH6XhUdFgGc1cvnQKa3mjyQ3iMR5sJMRqki7rMFt0FgadWd1j1tNQa0z85XW6Ky9DPUh9KPVw4200pY7RX7cRFT_J7mat5PaS48QUB2MYc2TUC_YbY8imSC4sol6Ro1RFfCvBZujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdAx3t8fUxOV-sS0nFvjpt2D0mFpoEYkkndjDwZ2TiscvOOvRrfp1v_eiO39S1j8Bzv-CvW0NRJIzM7cGVLnYnXt0ewfbiCAPuJTxK5hbyz5losEd4WYnb1_3PblFHGJGIpXi5ppaXVASS9X5iLQERKJgBYU-4Lk9dOtYsdU2NBSbJZ04y_q3zo8EKSLTNNvu16rfTM0ly91G6ks8bZdMKeyk58CknrtWJGhs7o8hDZw8p25q263ZVf0QqjqC0czJFFVaK6rjyocWZnWZgBV2xizkZUKLlJyEGzUgdCKAGJHVlx_G4C6k0mfy5w5URZwxXD8Ih7pBMbZYB0hDxW6kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WX5yGdGOzFZWIiWt4-Vpa805yrlGuQT6bE1jQKMGH3IZibwL68NXeltrX0zvk7FcyruK2i_5hHc_YSC0risDMcRD5LejLnL-19q-6TWTW48CrYC32F-hUygUGIQ38KJsmq7k-juK0YZVwD_kOytQltIO0XeQ60suZNlL_oDTVmkaV1AlCTnrjmpH9Srlz7YWUYouMfLUR8Qogc65yFdvJ1Oo_PP_RZ0Rv84LFrPsY0q1ysT8PuN0EMYQ2cTjpeHtU2F0Wa_8wdO_BQ05UH8iJjRqI060TRy2x0shH1qeY6abhqwNUP7vi7byvQ3fArQ52vsl5BsuRb8Dte7Z5Z8Fug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=BJtK0qH4HjT_twZCFY_rHo17VdFVUSEcVEgnPMNXfGYzIhxl_Vwtb2MRFUVhcs2LdF-cD8fCQCfsbFToAA0zixhu83t-2v90DTepV6dOkvhp-ep8i889u8LtKGBFx8d2ZsA60a9DwVVFhhforYuZIgTCMfSQY4qBDgzTNmYRdwtnMs5t8dCYgUTtNFQbblCOkh_P-Ab-hSWtHJVp3ZWJmoQZqVzT_0pRk6SM26fD2QZkX9psylPSrUFfhfKwtmbeRlyynM8zM0vf6s5YOef_vm9a3vFHdm5OdpmAfnCYoF6yCxZAaaF4_t8YFJdhATniKReUZWu3ljnVmZbFLetTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=BJtK0qH4HjT_twZCFY_rHo17VdFVUSEcVEgnPMNXfGYzIhxl_Vwtb2MRFUVhcs2LdF-cD8fCQCfsbFToAA0zixhu83t-2v90DTepV6dOkvhp-ep8i889u8LtKGBFx8d2ZsA60a9DwVVFhhforYuZIgTCMfSQY4qBDgzTNmYRdwtnMs5t8dCYgUTtNFQbblCOkh_P-Ab-hSWtHJVp3ZWJmoQZqVzT_0pRk6SM26fD2QZkX9psylPSrUFfhfKwtmbeRlyynM8zM0vf6s5YOef_vm9a3vFHdm5OdpmAfnCYoF6yCxZAaaF4_t8YFJdhATniKReUZWu3ljnVmZbFLetTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=Y-E763KBY13Mqf55rNpNNtcBJZzM6rejVjKqnO7rp3X7giSl2S6adf7vrQOtdqW-Bs1FSjH6Yz3_VLv8ipfj8OggpzNozpKxgOFjY1BmC_GV7PVMGNJSua8Y3qZsE0fYQhx73dRmy8Rq25nLSWltYwJ09uVV9oxl9aaQkjYQFD4AtIbunKG7_FBeWfM9W0ELTvtqUc7mCR_bgALyx1XChyxDruBS84qeH6l7Y4X1t2nizOZKnXQsEQh3mtBvnkgZ2K3VBfmuuj3gxAnMuoYw4LDBnHJFkr3wZebgHnfVNwRSnvZL3J8dBpA8qI8CGrgr20p9eVLbjTKizxhseWqdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=Y-E763KBY13Mqf55rNpNNtcBJZzM6rejVjKqnO7rp3X7giSl2S6adf7vrQOtdqW-Bs1FSjH6Yz3_VLv8ipfj8OggpzNozpKxgOFjY1BmC_GV7PVMGNJSua8Y3qZsE0fYQhx73dRmy8Rq25nLSWltYwJ09uVV9oxl9aaQkjYQFD4AtIbunKG7_FBeWfM9W0ELTvtqUc7mCR_bgALyx1XChyxDruBS84qeH6l7Y4X1t2nizOZKnXQsEQh3mtBvnkgZ2K3VBfmuuj3gxAnMuoYw4LDBnHJFkr3wZebgHnfVNwRSnvZL3J8dBpA8qI8CGrgr20p9eVLbjTKizxhseWqdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlsTlTtGiFJRCMj1BU4N4pZdpWDTPbXdXYQoU-L4vg2OxtdjqAbO2VfrC4IzLJQUwogvjbP_eLW1Kh-UwieMrWa0a7Tmp17Y1DgI395Y_0ZQLhab6G18ZavTrJaGI4AttjSykvLIOlUs11jmQoZsTh0sbiM9RC3DDJZAV6WvWE29bWdIv09Qu4VQtm7TgDPe2pd9LLmuvztYeb9uhjA2Rn6hwD64FrK7oIlM1yliOZlhO4NZOZD5cvz28R9XcscdfKBNLoT-bLxk40kh_Br7IluHIdWaslkBTbn81qBmoVZOI07g6s9aEcsBwOooOvcEauAzJLOUZ74gXEOgcSwgVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LdYQaMa0sG3FL-MYTw_A_405XWf8s9dFZ_tQm6C5pziP5yJrSWatGjQitD2BAl4Ul70zmNSAv6-Lxirvr1Zjc3PHEbwPOJ3HzCXy7MTLXCeUXxYDOeAaurPGToArhZDNs5L-_opbRjEuTpsvvTlaleENNL2eQTLFRn7Dxct5A_g4meRIID2x4Td_qobEErAfTZylqkG3QowOGlEGT8Xi0D0A0rLA4NPMhrjHbNx0sXOTxRAJQlcow9xlC0slbB_qjxyYc7jQsUBnBo3-0v2emkOBjiGnFDUeoTKkiz5C4bgH_wvOUfb6LNCAYm8FpfRANkVQmPzijZ2bKPB4r-hwQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=cFWdK2mpiXEWe0xde39d2dsJXBvPfkg1yAkFIlfMc-OPp1fVBDw52eypmjn0zJ1E9dpKqAZC5r3myOcswbcq3U1BP8bmgUKiGL3WrTzkBQKEeQsN0EQIqOui7MvQCSGZ4IYcWFvTq-iRGoSMrGsBHdZgBMx0roQfOyzGM27dgUWRdDBfpejEogw6DLfjft5VoglW7-pphH3E9LuxutLCjRdwdc6WaoYkRaI3iNCXb_kiYPENUaf8v6SeFiyAis3CFfBDFBvLX570F8v5R4IY7mJCIHsf8SwKax4pMSej55WAhWZn27Mr2vlkqZSX4Gta8C7YZJ9O0G1ClR8Oes5jIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=cFWdK2mpiXEWe0xde39d2dsJXBvPfkg1yAkFIlfMc-OPp1fVBDw52eypmjn0zJ1E9dpKqAZC5r3myOcswbcq3U1BP8bmgUKiGL3WrTzkBQKEeQsN0EQIqOui7MvQCSGZ4IYcWFvTq-iRGoSMrGsBHdZgBMx0roQfOyzGM27dgUWRdDBfpejEogw6DLfjft5VoglW7-pphH3E9LuxutLCjRdwdc6WaoYkRaI3iNCXb_kiYPENUaf8v6SeFiyAis3CFfBDFBvLX570F8v5R4IY7mJCIHsf8SwKax4pMSej55WAhWZn27Mr2vlkqZSX4Gta8C7YZJ9O0G1ClR8Oes5jIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBl13FaAP98LzgB_7-k_d1E1z-aMekQ4fMi0o6EQiQmgB52jYOo2zjMtEwowMsBGbTSB8PiOvVkREAHhfYYgyllSRxaCEpx_LbE9O4p4Ylg2mlkLrPbQsM-dH56Jw49QtXHgyiT90MXUcipmxqgJNByQSNvFTlpN5SjMpySScq5JqcFb4LcBDOfABEFPfomkvNe2mofKbuMEEC3iBPM8jdfS0s43fGXmqJg245Ai6N053r_NMhjjFbPQsfS95uhFaxqOw46O-2RYkyY0GG_ciYXaRFngQTzICj3I9Ste9eyDOKVqljzPUWV7LiTJzkdD4bygC-L8vY9w9Dcnxe9lcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
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
