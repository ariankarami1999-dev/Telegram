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
<img src="https://cdn4.telesco.pe/file/XmOr1_SGKVCUaNaqu2FltioBJuIZEJDMvTaj8WaZ_VlYZEQox_gSTJIlPyRFauox_wdU2ZzdhmSLoYVk9DqdVR1Pw7hMHYS8EF-k29xm3ed3BFmhRt8qDgHkok3EWVjKRDfbc4_-QrLgU5a6ukr_RqeNre62eU9OXWQHN9ieJ0g3kTh1aPdebfT7dtpATBApRiWGY_ik-pbbSIeqtSy41b_wRcUMoKY8ac1d1XYBDY_FCf6yseD3OxX_azLiPDLydKntydCLB9jr0of7xC1paQF5IwAozQsjp9998DgAwlm59HNvPTUBKxSYpq-MuIuVNZPF3lIDurH2GxeZrsn3Mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvsN94JSKqsljx9mgbDBRgV_llqF_WAaZnBseHlLELQKKJ3ws65dQqANeVtfIJlnDw9bUkamsXNJMxX4eg__jKNzrsB0NVBfezZhjqJtYhR-RnVEK9Ckf5mA_EDe2PbsO1jc5aPs8PmMOp7tRRFSZ96-ank0yI4ROcmu4mFjI_To5cjVmnd47taemzRA5xmbn_UiuMpRST9nNDkzN5Xvrk5AnGgzG21bPRm0MWUsQeVO7Io2NPo7jATmNBZmLQjg97FZaJOthxu6wfddjrAGzlSlU93BlZwS4XZ0OI1MIJCBBo2EDJ72Ws3dw1s08pVb6fNIhm7-33CJDgroWH2PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSzSJHYVHVhFewxWEpvvBqFV1gnDezgXfxULomicmmGdKIwaXklgjsp3MQYMR5f5I2HJ4PcQ9jldRJ9eZpoyWTp4-XZ5i26Aau4CqrqJht7DWk_RhpRdtNH0hdCAWctFwhZvAjxvSaBRwLAi-8zivbwFVWvdpsrZzFaUcdAsuUP4XxDM0co_wQhkFe5zmDt2Gt_ffBhKvaBBRX0v5ukeHrSsSYvDLnXp-vvl4WC_-3fiS3Ly9UsRWWyL65qjNGYU8aafGDDscO3Wxons_Wb6M6fDGT5d4AZcby1daud_Tjzzuu3Gx1AMISQH899uv-XkQypQJl8CVCBxs54ytOEQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR7MSmD4ceg44KxOVt_gVCsntJEWKwc2FX31xcKBwYnKqeYikgwIdPMWEs-InCiCL_kPIN9qORACCUY7Cab7C6lec2w_dcDAUuaY2cXJwyuALsygLtEhOzGWwrj-XBxHPIVQ93QiqGBeygduhDOxKswXRP395TaUCj3t2Eumfv2-J8-oHtpFoM-Xk2aBtCX_EpyZMOGdqSkmlyKCVbhdR1o99Em93pBqWyo2icaCTFOlFrQMY8_KNIPpBLkmyz_26qvVmBaTLXHDLPPcxHkqiHwqCFgkjs38XfGPri4HFaoWS7FXWQyJSQj5X8sQDXwIkb88FuKIaGG9ZJqBcDtWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=btNb9eqeRBLLia0qoB07j12joadq3NuYsf_q51jIvDCiTQDRssOmto6P17t5I8v_ms9WH_uIqTkQrYqpbGjEcmFXsmNA4-sEnMAVumdnTbk4T98RAL5fBNCgxhVK73UkJJX-S_8WVxSCBlZHtPjsCTDqo1zpDit6t4yKGTK-mfdxCbqYdDdfNtb3LDnQf5l7MUjFPUk5hQFRbSEgj_OdwSyiwo6i7iIQ40h7tdEggO7l3zpf_P2m3B4SolHRRx-mkSD-AV6t6uAi2dxT8MoTjXz3M_JEoVa7inZnWR0i6k1UA-Rbrqig_X3h3uLMVZY1TVDoMu2JlJFgwj9-8AdE4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=btNb9eqeRBLLia0qoB07j12joadq3NuYsf_q51jIvDCiTQDRssOmto6P17t5I8v_ms9WH_uIqTkQrYqpbGjEcmFXsmNA4-sEnMAVumdnTbk4T98RAL5fBNCgxhVK73UkJJX-S_8WVxSCBlZHtPjsCTDqo1zpDit6t4yKGTK-mfdxCbqYdDdfNtb3LDnQf5l7MUjFPUk5hQFRbSEgj_OdwSyiwo6i7iIQ40h7tdEggO7l3zpf_P2m3B4SolHRRx-mkSD-AV6t6uAi2dxT8MoTjXz3M_JEoVa7inZnWR0i6k1UA-Rbrqig_X3h3uLMVZY1TVDoMu2JlJFgwj9-8AdE4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sB_h4J3ajcoo4MrVzxNnvIjZUBixGq4zulHGegUyYGdHTLtT08E8jz1W3XA4nhedTJXUXZWsKcx-VXtnZDAXFVAJxBdLyXNx1sX-GoNNCS7aYJg2SK-GbIy_JrwSAJWWpce_7UAeuUcH_ostBsPebiMTaL-bTQFd0-rtsV9UaVEgIVjTkdL1MjHlQBbAjxauPIkXTwXeORUX11K_7InXaxp1n9H2GBU1MXU-UflyhuZuQsx_hnAlTOeKCI5negBKzE-2yvdArIk5VOSS4wJL5y2GNByr4qSp2Ers_fLzM9VBrWwJGM7QUW4KM2VdxHnWBGn2LX9fTtRw7zR6G2v7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txebbeCzWXayH7eLVE4yIwEMmL7Uh2PuOzRC_NOnMGf7GLsQnq5QBFP4zbgqEmGuDiTVp2I2CuMZ0gDjeyBVblQVx3NanEpZ7KzOP1KpynPUd6QAmVlSi6HpPFVm6YRcxyrSCZLuSRQS7IAYGTOh-570c8kvHdHIKf0NAYCqi9sGg-d2n_va8_CDF5EI6d93VjsT8rRyViWCKv_8vEG3vmaCNiZuaUC4dH7YOPLPJBFL0peL9AprG5iX5Ayj2KH5_5BFvIwye2ekcu51pbWM8nxU3d847DEXziNTFzOWpIa9Znt0S_BjwDDcPPPdAOCPnG_iGIzep-owdqqHiDUgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuF6JUawgeSKBR1h4twdsPkVJj_xAbhBdm2oSyebFqXm6cvM-Oui7McAps9oRK5NkNvgGTT2ckO05Vwz3Kq1NIuOzbPHZaXH2njUWyfPUWvgyrH72Nb2WYc2bPv5CXU96nzBOewKFTIbjKTuyGOsqxGQhZbI6D3GggBOKkf4Ht9NSEhUaDG7UlkLXTen2g5E_6BFkeqk9M1oAiTk2OrBi070VYdl_R51vK8YeKTqJl9FAIw1WPenHFMFwTHFvdf22ewuMN_1ytmQsPlEwiO2I3Z0XjoRS2tfY26ltP1IO_pyHt24aRSpvJ1Hrlvs23hJFXyPfPaI-QcnI1BzTOw7ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qFuhHKhLSnnYEpXE323cfmbGwT2if47uWk4Y-wFLXBN0Z3D2O8DZdYokB8060_r_oaETIVqjq63WTqT-dI7FxbUVNboElcL7v4sGTaeMLjAkrgPH8FzqlLq-niTlyiJUa-WRM09i_nC6A0JiS7HK5SFPeTPM4ZMqPL_d835CJOTU1i2tDJjdut1eCQpwTtUPtlY5lGNmjuJfGjaFnaIcv5BvHZ2h8bFIzNOR4JhP6YictXG6YSiVvFkj-Zu-fAuKufXFAg-Z2dxN11JMLpaxZXYfqKjHS-K62BUrPFevUpz6pFXMKF2e8PLvHC5gS2NgLHf5u28Epx9Toe87GEPORg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qFuhHKhLSnnYEpXE323cfmbGwT2if47uWk4Y-wFLXBN0Z3D2O8DZdYokB8060_r_oaETIVqjq63WTqT-dI7FxbUVNboElcL7v4sGTaeMLjAkrgPH8FzqlLq-niTlyiJUa-WRM09i_nC6A0JiS7HK5SFPeTPM4ZMqPL_d835CJOTU1i2tDJjdut1eCQpwTtUPtlY5lGNmjuJfGjaFnaIcv5BvHZ2h8bFIzNOR4JhP6YictXG6YSiVvFkj-Zu-fAuKufXFAg-Z2dxN11JMLpaxZXYfqKjHS-K62BUrPFevUpz6pFXMKF2e8PLvHC5gS2NgLHf5u28Epx9Toe87GEPORg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=SYfe5TGmTxzxBPtHFMaA284xFIDzACzCAeaWMsElGnoc8i0CRaXCxVUYPpAV_-L6Y_k4ht7kRyLTkTJt6B6syU8sVm8WxOKo3xQvtWNmxXp-HdoAdQy9rz2wkcD8j-N49R4_PrQVhc7ro6Q0JaHlfk4g0AuLE_eqJZxuKnxirYTvtITnt9PvkRTNOToZ_UHMouRn0ae43acrHK9RGO234Ryn0UknOJUgJElABgedHqThsssg3m93kGXnt7xRoHdWAqALnSf6TWTcwx00t-wbgVHCd_smEeERMuFXHv2zwoFrjm966lvvQKn5nZZSjPh-_MV93GflC2Z3Cw4dsBKAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=SYfe5TGmTxzxBPtHFMaA284xFIDzACzCAeaWMsElGnoc8i0CRaXCxVUYPpAV_-L6Y_k4ht7kRyLTkTJt6B6syU8sVm8WxOKo3xQvtWNmxXp-HdoAdQy9rz2wkcD8j-N49R4_PrQVhc7ro6Q0JaHlfk4g0AuLE_eqJZxuKnxirYTvtITnt9PvkRTNOToZ_UHMouRn0ae43acrHK9RGO234Ryn0UknOJUgJElABgedHqThsssg3m93kGXnt7xRoHdWAqALnSf6TWTcwx00t-wbgVHCd_smEeERMuFXHv2zwoFrjm966lvvQKn5nZZSjPh-_MV93GflC2Z3Cw4dsBKAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fspQNsc5OYvFA62CuA3V6HUzrKr5w4d7OlMNtZ1cGgb4ZQo5nN5LGZAkDa9nFb3tFERQkCO0La9GIdb8IGQnQ2TebATHpQM98gymZsbF67ZRUDLLBsLQOjBbGjHHuzCCyz3ec4i8AU-O-mnh1S_VsjT07wjSZ1UK44WAbs-TcGrWpE_uIKyRRzaa_oIP34ueiyALfetcLwNvjXhQal129fQHBRqoU7wibpjom4LXn77nKmJhnPAa4K2PrsSSkO-3f2OBKEhDOuDp7xl3C_UzEPgkqMulEFSkTZmS9FuLXaLm9RsMpfbux1dYNq3cEnC0HomXc4hJNcf_S9p9EDWHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJtUvfyw2dKXNUcwDk8qkMPA6pCV-gKroRA-nJVJaBR8cuFurnueqlnGgj1wv-5QdRWzDGTzcgGtIyHEXNMbXvgOfA4lf7Cq1BgpFkCra6MYW2HPOjXUTn8IRWL8jhC2XiqERSIcTxShcXY9DjfTUgCJay_CcpPR2_gBeEQnoA82zLTDxlUUGpc2hwT7ZQwwCuvQXRNbsBFSq-0Dap5CD1Wcz0u_D1IT3kdjpZrx3wbfskSzxKKTDMiPjITl34_h3NKW0KDHbDDo9yRu78IQSm5UpfE_AOrgzlhRy8tmF1yrJpJ3pEu39W_7fED9nqUFNJBWyvyHK-kutkH8VHK_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=tMocppq1pxgX7O9qezujBnzttgCV1rZXqXTxgAbz20V8d9fkO8ukva-Fl0AG8mc2b_88OkV2awqEByBvGHvboo1MzIR5PguhnUSkrbcCyWLASS-oz-zZSgXoBN8p409c5rfbO1uHtbzvt6sc7SOgWjgU19MpyViZAznDsYg8QMvaAIt_jtpmNLQZSkNYq6Q4KUVQ9iF0ODGAPnDFLYDxDh7BgKuwE32OlvZIuzSS0YOQKqh3hMh7wlcLcfl4EI9i9haycv31IPi1LzG-I1sQeX0VGGeM6XG7DWyzFnIfckMmzFj3VBcI0EKcRvjQTB7owb8RmSU7D6f0SRMtvHsIHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=tMocppq1pxgX7O9qezujBnzttgCV1rZXqXTxgAbz20V8d9fkO8ukva-Fl0AG8mc2b_88OkV2awqEByBvGHvboo1MzIR5PguhnUSkrbcCyWLASS-oz-zZSgXoBN8p409c5rfbO1uHtbzvt6sc7SOgWjgU19MpyViZAznDsYg8QMvaAIt_jtpmNLQZSkNYq6Q4KUVQ9iF0ODGAPnDFLYDxDh7BgKuwE32OlvZIuzSS0YOQKqh3hMh7wlcLcfl4EI9i9haycv31IPi1LzG-I1sQeX0VGGeM6XG7DWyzFnIfckMmzFj3VBcI0EKcRvjQTB7owb8RmSU7D6f0SRMtvHsIHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=cMO09B5rRg5_uOGwC98F1xK00V_t0aslB6TOXi5t17gOlAgNzzCu00vNjxQFCYWaLDxIaujLGtlGqeRbWZKmXVeX5Kdp-QOnrX8gp_UUedzsVwsGBXUKxI3wC0nPB6kgFed82C62XOvm2l7rEMFfeOrQ6GO83T_vinmtyfDdevUc84GJbsvZiWKVA9zJEMpE3Q4W9fpTJLwxDZOSDRi1aUSwYyymG2Kzsbq1qBEDiGjiSFk3BRy8zwXoBaZEmM4YyVmKcn_fiHUUT1Ezi8uArMvRvR-mWLv_ekCDcIzX_3yT6hKy7-EcRIgAHycKxlLYjXZ703JTAafEbcBOv5tH1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=cMO09B5rRg5_uOGwC98F1xK00V_t0aslB6TOXi5t17gOlAgNzzCu00vNjxQFCYWaLDxIaujLGtlGqeRbWZKmXVeX5Kdp-QOnrX8gp_UUedzsVwsGBXUKxI3wC0nPB6kgFed82C62XOvm2l7rEMFfeOrQ6GO83T_vinmtyfDdevUc84GJbsvZiWKVA9zJEMpE3Q4W9fpTJLwxDZOSDRi1aUSwYyymG2Kzsbq1qBEDiGjiSFk3BRy8zwXoBaZEmM4YyVmKcn_fiHUUT1Ezi8uArMvRvR-mWLv_ekCDcIzX_3yT6hKy7-EcRIgAHycKxlLYjXZ703JTAafEbcBOv5tH1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=KvrLlxSqRafF_sW0gIrOk9R2vxSetrRkPa1l3nQsvCeRbCSiRPqa3zouAY6uDgB3m_WiaUN9xumdJrJRllZb3B4uFMy0TTEvgjTg7a1r1DSklTOCBeMrTJzvzaakMcM6Z_yzPVTof3UAECDsfXx_mHKgGcVwcn8mpqDn_OEKxuGFoZNEFbyjWP8zE1DeYxEYe3_YQItWHaYCGO6TjuoVJtu62FFE1Ch292t5TqtLcuSwOUexN-yhQfHU7zZX24TWGmLtDozFJ4yagPwJ5BEBGML0yUlSoj9DuX72x9sjc2ndsuZMeKwMDAJURvqodY3mWrkp7LZj9FuLuu9xTtP6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=KvrLlxSqRafF_sW0gIrOk9R2vxSetrRkPa1l3nQsvCeRbCSiRPqa3zouAY6uDgB3m_WiaUN9xumdJrJRllZb3B4uFMy0TTEvgjTg7a1r1DSklTOCBeMrTJzvzaakMcM6Z_yzPVTof3UAECDsfXx_mHKgGcVwcn8mpqDn_OEKxuGFoZNEFbyjWP8zE1DeYxEYe3_YQItWHaYCGO6TjuoVJtu62FFE1Ch292t5TqtLcuSwOUexN-yhQfHU7zZX24TWGmLtDozFJ4yagPwJ5BEBGML0yUlSoj9DuX72x9sjc2ndsuZMeKwMDAJURvqodY3mWrkp7LZj9FuLuu9xTtP6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=pBnTfaCMggQaU32K2gkoQrr9Dvgx-kq2Zpwc-X8CtjXp_tz_RwBCVNsJFccm2Tt40U20iWMKMQWXf0SDtl7VFIg16NMqqU45bsPhZI6uOZ017NQRnGQjXTGcSHQyp1K7BPNJ-W8R26QCKvgJhckUelNumfDOyqpRWNEInra_KvpNkytSUMhWgiQbOSgfRmAdAuzVKSnyLRJOQtGqe6b1U1W83qBLnNKmLiGZO97vsE-0YJywUS09kKZszi2VPsSlmMr2q1Ln8aFS61yPXc_CJkf8oDoTW1CpSUDtJEfpj_cdLO5qPth21Oio8FS_1t9eqBvFH2aHtO8W7HzOElI7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=pBnTfaCMggQaU32K2gkoQrr9Dvgx-kq2Zpwc-X8CtjXp_tz_RwBCVNsJFccm2Tt40U20iWMKMQWXf0SDtl7VFIg16NMqqU45bsPhZI6uOZ017NQRnGQjXTGcSHQyp1K7BPNJ-W8R26QCKvgJhckUelNumfDOyqpRWNEInra_KvpNkytSUMhWgiQbOSgfRmAdAuzVKSnyLRJOQtGqe6b1U1W83qBLnNKmLiGZO97vsE-0YJywUS09kKZszi2VPsSlmMr2q1Ln8aFS61yPXc_CJkf8oDoTW1CpSUDtJEfpj_cdLO5qPth21Oio8FS_1t9eqBvFH2aHtO8W7HzOElI7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWXtBtql11TZpaviuxDvAPS8oQvVJQeT3qLtKlp7AgFT4kMqHZ8-oQVvDKYlQBv1kVKlwNCFqMkuyNkQsOVVV-1RTd-siUM70bTjKVuypapJgnxqzA1As-eUeu0Gx6AUZ9f_vGSFW0N43rRLYzn4pX6YyiFo6PksbtaNBAwu-F1P_vNKekI2g-EifRIyfFrRTu51fVXLBE6QH0MHp6HyxFdKQPNqHTh0wSaYBX2_myUw5q3lGdRbt7Z2VTt-0a0HG6lqKBRBtPCMMpDei-w9LM2Qp0IEDVkmpCxSbLa-Q8PbLdPxsv-iI1IoUNyYJlnjlkuYvYtyPuO-4DOTXeCKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCMSfcag-82tW38SasX9U-M_YLXEvlC0qCsAJIovsqpy5zjT6v0g6FLYUxD9F_ppjrjjC88vKkIpweHUnQ4TbYFvQ_LOfwJFQoXI-Be0YLMqqq6665Rde_JVBKATZU2DHnC1SSgD6CXbP_1yUi8ZL00QJnmly0l46I8oHkVFL7qhAtJBzd2lUovp0QO3aPFtMjV-N7wEgVH2Y5enQX8mo6MaBhGdsQk2XMhMnGNPXiCfTQ4QM7l9rPsIXe7ML1Ya-BSvncPb6E71W1mYw6k7LEOk0f9IuUfAzg1n4XmiBaBj1NrrM19iNzLE6FdnYGdlDgoF80ur2PhkpzxcaSqaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUl16Ynk_yfNdG9iFpe42F4Y_LglXxEJRJW3jmGBGcfP99LRivt0kTqYsf7oeAvabIHthdW2NfEcCHCncM2ld-h4_EqR6SIAbGum-6HupxyVot7Epzxs7_j1e9GLA9-ay-8CoQIOmmzOEtUfDLqueWzyBqD762ZE9mNXvd-pTwnWGqrRMqRm7jMWt9iHeND5QutEFpweFJ8kE2WUqHBa43uVsSC7XxujD5wdo0524DpTEgT9sdjYx6CNgp6mlFtgoCXY_cuAQ63KglUAgnmZ6LvzcJYQ77xyBHjr6t30d0MWKKQXoT72fYjKjDuKbsAEx2Z1SS73RGRbQG7B-sswbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXkyjfT00if0O3s3vOH853WN6IS2XgmaOQI0NR9hABvMOvhAiVq8GRLhBEhbVmNGJvLLkVy3xWfTNKx0wtY38UNudBhKokp_WBjLEgj_HBwX007FrOTu-OFNLTfp-VVWE_ApZ7a34XXZrJO6Wbu0MawFxhTcUiZS2v-JGOCPL0B0FeGCt6sQZ7_7IJzcFMR9Br6ShgVG2G3ysrwkFn9OpuO52367BimlOhV34BmCjZhjPS5hExMsiJ4PydlPjEjdJYzHv89IvbwWdPygpOqxWH9wkk-joCfZNMTom7ztA9U_pIekD0fOYlerLO830vh6jWmjao4-jc3OXdPMXkVwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re89JbxXvvXRmVqw_ecEr1APOOE_4GsS6xuHSPQcKD2MHkRwoZNyhUDmo7Ae0i3an_4QCXQC2xgWlvJ9DhVMtKUVfjAzmqbg1c0-qc1ulH47Ec-_fUR46AkVSQF477Tvp8Wcs4updUqK1oZUI3B_LvcmMOyp3BpgubTp6NgIHZsgfWfWT_XE2ZZIixNZYMmLt1OLMmCBFswSkSxfCx7rlxSq3o2-rmSxPHxHtADTPu0skDkD_smYtC4y9rlh6CjqxSBJ1nJsWtS9Ay-o1Kysn-zVDNr-E0FDfRJMlVOMPk5hAj1OlMWL96MAGbzGgkxYcVQLcl-6IT5XDRrfN42PFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTtMWrdGWaGqab9fHe3xBMSjJuMGgvEjMPfilwhjCpegqK-4RzxneUraKo9EKLCnppKH9XE3PZThEDI6s2LheZOKmspurR8heMPALjazmSHKcu6O0ndMDCpE00W7yKY8ik7Eo0PqsmomokLkCZech3Iv49jYcSHYerJK1nxgnSgSDzebBSpb780n3v5RUWq98WnqwS5-T52Jdp_-f-hKZzmHPilYp4B4boH9SNNdLMKokT8wKYNo37ZpdNOm0FgovFzPF1HalQg5fSPopNxWxgFGE0WQqAURR5S4TpzLv86mMgqsHmKQUlt9UpviGQdc-Bk2xcE6cr29viST4De7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyaq4zIi77kOm_iAloz3pXm6gVGCv6p2u97_FcQuw-xvUyjq6sMPNI7awt4HIrD2URxrvPoZPUWhbkXRKkgEs1AwJ44jbnuWFqDPv7OTVXlxURPaU0kazx79LXWPVkAzuo-ZLL1llAGtPxaoqm6YY_BFN63L_byWLi3XlJZMy1bj0fk8POPn7-OkGbc2rNbXq3FiK8DlYPVbHVGWIgm6x-8SDp-EpI_-93RRuYpymljhS8S8DqeSryXPILVA0YUIp6Ruxk2f1Bv02FlpUkjGUXC8cC2IrHkvE8ExLzFx8WOuq17uNk7G99PsXn7kNvN5NrIcpVmoiZbkwumaTmPqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=No9yXYxDn9YB8Mp-avYgZjIPTs4lUHzYmC92MuLeSrQhQdXp-QmI1XDmQb1KJUxRZEmtgNmCcAgXUabdPqnjt79-5KH2KSBwlpOmgtg6Mba1hS5n4HHzNp98mqidWL9CP6ftOO9MR2Nw699Uylx8EcoA2Gv6z5kvHGSqKixA1ZD91Hx9CDpOes1HnqQLLR9tdClmyQkruHb_dXvkbP6bJZUkcd89nQbAJFYKya3IaAO_WXxG_5N5XQyCOqr_Tx0QgXCUvANgy5WbMHeZhFhVZim559LgGVLe54O2p99ZIMebi3eI3zfDM3tL5t0BuOiPm5EDPT_3IOHcCu0PHua_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=No9yXYxDn9YB8Mp-avYgZjIPTs4lUHzYmC92MuLeSrQhQdXp-QmI1XDmQb1KJUxRZEmtgNmCcAgXUabdPqnjt79-5KH2KSBwlpOmgtg6Mba1hS5n4HHzNp98mqidWL9CP6ftOO9MR2Nw699Uylx8EcoA2Gv6z5kvHGSqKixA1ZD91Hx9CDpOes1HnqQLLR9tdClmyQkruHb_dXvkbP6bJZUkcd89nQbAJFYKya3IaAO_WXxG_5N5XQyCOqr_Tx0QgXCUvANgy5WbMHeZhFhVZim559LgGVLe54O2p99ZIMebi3eI3zfDM3tL5t0BuOiPm5EDPT_3IOHcCu0PHua_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmmC37XILmS1XQVGnEmBsCuX8iWtR_KTqlt4vbHrbMe7ld7RS2J-MxDafJGK6UkY0JDc26xBhdx2sEnbDlZ0X5q7ioIGKWMF7KCNfkU5TG0RkcZ8vSxYb1zAxPt9-a3c61GPpkp0gO1ZJlDurHz70_FuIL28v32UNLqtCwR2fItwjMhQD0hiZwJ1i_XBLKkAmZzSq66Ty0iUCTKo4cTCfXgIL6BPAdmxqO6uTkKSTAsHvYUzEzJvcsE_gt7qVAHzAEe1dXpbC7mg7j4BY2YxwqmZDsT98DQrJELGFEEz7POcqGKvoHdsu103AbtradVaym4K9yY4KA0r1-ECLI-zww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxLiW962NhOMzJ7HTKRy-QssHh-5z4e3HLUoG-PTDlYyeOKJw5dnuKOUxywdg-q2TCspL-btHjtII3edmn0qPbUHHAq3nNSjcDVGB7exE16fqRyrWD2UiVUV5zJGkA3_aOfJb3VDePqk5a6SNUMIXM9P_PqhN0xbuwZkk11V7y_xdnxcF4OOwN6BZX_Q4wdiQHQBlJ6dYr34r_GyEB0omEY3p4AXvdQTrddVIdZTQN7gCUbp6JF1MpIIBFIDY5tXA-Do9jGJtkAtz37IS5XiB9h2r4299LWczd0V5dcNgtGAinsVx-tObN5ReJwVEjnr6Fk1SvkujXN248wGjRGwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsjvpAVv_wDh0Tq3E6NNfChMxvECie1C6hAJG7r07EPg_wzjE2x-D7P5Jx9FNCsbRvNoAMrW5abnIsIcyjQTAFUJAhGWMPTIj-PUID5gbJupW2weY_P0M6Jjc_gfufcDZmKJbRv3e6Scm8t4gsMvPNq5mGESCWfJnv8dwJd-oJRT9RsWS_-r0HdSwpjwAOM-U2Gv22g7ejUePyGL8dirjJT8bTFxSr6L56d65m9XhYmvNBdtnTh7EI25StcWzZ6QmIYpp-SceaHojvAxQ5DgRHja3hbUSmZQEZ1YNmBACKkHspKK8oam2x_zbg4Ivw5CQUUj5G7rZN5KVBRTf_0Pkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLWQCYRXwH29LGd8SlGAEoYKAugp4YEzPVqkaZvcw6rt1ZVuAQfzlQJms05U4cG6BTcsCU15X2Rm7IztWvAPxkTBrdty_f3jo8t1rmshJPF5SlJYZVRabZSPd5dqCl26hqk5f5Mai7fNnudmvn1UmO7qTjlMuKInvIKeDq7UP9FMa4v1ckyIB6yb2a4SNHE_iPYfsoUOt45Br5Sd1KtXtkbDk7Eo1FoexgQoUYJEpDT2JyqQKY9VdYmDGpE-Fp5iH4_qKXIiJ_wR3QBxRldQpwjOhYZfSpdIXS-fz2foFeiOLmuQzFqpMttTccFSgqanSui0n4MJR2L3yMVVvCPfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKKCrnu8jVeFS1eoizj7T04wmMfehG6RWbIfVOogDGsTeGuZekrisgDqWcHb-cK0aem1SyYe7cnI8zR2siSdpVNd8_mKHN7bmxDbOH9slMZu9yhvd_raJ9TkogoAlloDekOuK5v3lMM5uHJM_prQTQZY8hyEZeo6n--PiLtnoUT76fiTLYQKA1FI8h_iSiO_glty3mvkK1dlUi0WdaIF8NVN1o8M3B9NnC0PPE8fsFR_n6IAOGEnCjMPE1-OS6wPuZW34F1cmRhoWttkiX7hXyoCwakHIpRvxgGKM7Tr0uUm_KDHA8Fzzo_Mt3sfVPrQhhhxlZDTBduqc_PDsCqZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgxiyFI0CC7nr2y2ohEyPoVTsrhM8y47nB2vuLbQ-m-glrkGnwweeWwe248GDYdyF1h-Ti4FzTBmgZdBU0WDkD74G46U5k-rGYhekWUE_wyICEHjHHPFatFp-VVHeaD-BaEaJ6bb6uQfgYVLzKWr8u_2y_zrnVgFEg0p9n0MZKo19txlxCuIwM9Z5iRL_SfU9BBd1hr3mjK3zeauBEg93IbEEtFK4PCbV_rB5mP9mrnIfhQqhA3h2UYarepVuMYoButISArPoyos9XCEisprQUfB8Bz9Z3goKJncaFAPqYA_cMG2E1lA7ABVtZ1eVbgxArplAwL4Ln17hk3eb8VTAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WEBbRZITKfSsCW7addZF_7vGUbT27vanWTBPhcTYWmu8uoaE0EywWKWzKDpw7T6H7Giav3MRRnBd327iv0k-ZI-UXtRAxJVgXTME6P-SAlVBFiT9sbaC7quUUIjcPtqvdqncQRvPzh-Z50TNM4gTbgOqeR47-IjCVfSjmZEQiKjq78GV2qPV5Gc35VWIPPbiQyDFhqxi9-JccoU96vSTGBKOv4ibZcuX1BJBa_XUYwnIEkfFYxtgb_6MLrP9IBv2KLYWmkpQT4v1AY5V1IsGQbh6kEzPLf_ZXAZzMWGFc_jz5WcYU2uXe-JZ29q7etQW1_UGbBk7XhbbNcP2uyNh5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EpwnSoCy1i6KaTgXGuWDIx63si2rgiMFKKznvxytE3qDkA9AK-bjOjbRf31pktu_zbRVJsOJwT9lPxmV2j5pfrlmDeMK121Qsi0LBz7y0VdkZFehwcyH5UgUgoH1RVTk06hLPekzfWj_mmuutX6XmJ-Gm071BYfjWCZpV-Mw4lNUZV46Lj8acAJP77FW7YsqF9YVHU2nZOI7l25gVzJTy96IjYohopmB016JdTsRh1E0Bqw9NMznNZOl5XsNyw1XqKaEpgbXVmrcV8_BZweKo2-9KvWjSy4Cg1oYbupoTLC926xA-UuK9WB8EzYNkH4bAvE5dCY7JBss_F5Q2nG4Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=kbF7KL03Uy4EK6PNexEF-K51EiFK9MOGN4sBgBsWwvd3I8jfVq8nFXZ2ync3tMtDo7e7CSxezMAYtKy93q77P8C6oOSCHDhYJt74ErnVV7uONA-cpt28zUgPw7XJ2uS8MyVqc4MqkhaP1NhxSEYLqcKxIfmZ3Lp1K3_uSn3khOK2Qk6TdWvs5hoqQlJJy_WoD6dd57-rBcc0p30nK0MGSXUMOEH4XB6SwULTACErq61MdFF8LFqL0dnGDI0eDVgH5RgVnAJtgO6TXlvbIXsHVz0gB9UZhKoEuu-4T4veTjzCL-po_8K4Z82ap6x5KEwdEIzz4aoA5rAumh2rSl0cqF2WjQ0Au6J_zN2yTUPMr98wjo9DAjllKD1cRYKhwehNk9EEsW0xd07jOXM4BIIVvW5uOcfDXHLaWXgEhP1Qo9BZdmRcTFksnkCkM1lYwytchc8lHBU6CaxgxheZBDBfjLOeTnly9zBYp4fL59U80Dwl_aR270-mYHMXHqUaFaTT1OOQDA-AVZE3mKEMDRUURO1x7nqeBVXUtzMxba2gFQVo1SvhkJLeNWhqBIXuBx8gpQ2k2SdgwT5wZQunX8REAMDbvZgyeboAeXsXgg7xsGLCoz92dXkZcMyVX6ZfhdDnfoelTSkMxhnnyjyxTHxCzz7nUfxVDSyP5mr5nhk_6qI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=kbF7KL03Uy4EK6PNexEF-K51EiFK9MOGN4sBgBsWwvd3I8jfVq8nFXZ2ync3tMtDo7e7CSxezMAYtKy93q77P8C6oOSCHDhYJt74ErnVV7uONA-cpt28zUgPw7XJ2uS8MyVqc4MqkhaP1NhxSEYLqcKxIfmZ3Lp1K3_uSn3khOK2Qk6TdWvs5hoqQlJJy_WoD6dd57-rBcc0p30nK0MGSXUMOEH4XB6SwULTACErq61MdFF8LFqL0dnGDI0eDVgH5RgVnAJtgO6TXlvbIXsHVz0gB9UZhKoEuu-4T4veTjzCL-po_8K4Z82ap6x5KEwdEIzz4aoA5rAumh2rSl0cqF2WjQ0Au6J_zN2yTUPMr98wjo9DAjllKD1cRYKhwehNk9EEsW0xd07jOXM4BIIVvW5uOcfDXHLaWXgEhP1Qo9BZdmRcTFksnkCkM1lYwytchc8lHBU6CaxgxheZBDBfjLOeTnly9zBYp4fL59U80Dwl_aR270-mYHMXHqUaFaTT1OOQDA-AVZE3mKEMDRUURO1x7nqeBVXUtzMxba2gFQVo1SvhkJLeNWhqBIXuBx8gpQ2k2SdgwT5wZQunX8REAMDbvZgyeboAeXsXgg7xsGLCoz92dXkZcMyVX6ZfhdDnfoelTSkMxhnnyjyxTHxCzz7nUfxVDSyP5mr5nhk_6qI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=jQCuwSqUdPd9lE9O8V_qaV507sPY2hKoT6tzhG8RbNCSZIzfzc0Zw1mBgc5WOqw7BjF4I3DjmdOnbFzfHvHYbmvZ2BACck5pRZnlIylTuQkcGVqM12sHIugmfkJh6wBW4EZGONkQnGMvvviF-zlE5h-7gq5W5i-5ODoMfw-q6VhlwDfyViZWeqHLAfu1iGcrIdlNlv3NEKJQUSqP4COmpfkqXygt2VDKSya2q0QOvo2ZKvfpr24JRXCS5pgZ8NCUXqPY9RSEo6mRD8_4Z9D71CiHu0vcUj1reIxu2rs0d9_hCGFfL-spa-I7i6SJ4mSYyKC0gAM_b0_2vD4BONEgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=jQCuwSqUdPd9lE9O8V_qaV507sPY2hKoT6tzhG8RbNCSZIzfzc0Zw1mBgc5WOqw7BjF4I3DjmdOnbFzfHvHYbmvZ2BACck5pRZnlIylTuQkcGVqM12sHIugmfkJh6wBW4EZGONkQnGMvvviF-zlE5h-7gq5W5i-5ODoMfw-q6VhlwDfyViZWeqHLAfu1iGcrIdlNlv3NEKJQUSqP4COmpfkqXygt2VDKSya2q0QOvo2ZKvfpr24JRXCS5pgZ8NCUXqPY9RSEo6mRD8_4Z9D71CiHu0vcUj1reIxu2rs0d9_hCGFfL-spa-I7i6SJ4mSYyKC0gAM_b0_2vD4BONEgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_KPVOqgvhbSAiLooCFtUbXrkzfuuFriH7mgBuhkwrFbS9OKC9byOMCsXzNPbhRKhNVWTuTKZdgGH9xpJRNF2DizhlQGuwxxgPHqZhth6CtixwTOwKoOIHVJ2qqNblVmJMfCD9hqzhpLOCq30Q7WWaRVKVOPRbO9YFoOS2_ftY-hAgnou0wd1BFwnPC3lFuuXdyq1n7rRudNHtytIWX6cO-57qxBbR3QdLfwT9AmyQBCKypHHVGD2e3AYTVvhcnlKXXfW_EV2Yxt2Xv698F40iBj5qS8eOpDrcfEA5sRN9GRNtdWrzlslr5PjEeZk-2ZL1VOmePwGQjFXRd36kAy8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5RF-ijvW7wJgJD1mLdtir3_wcQoJIT_WK-rKhSeNC0B1mhddFKhyB9AHG7Ol3rqFYGl0JQ5EHjXnKf1eysPcDsjxtt_zLiUoa26VUh-vgyKxQl0pLWKPDyyhyOsVCCEcLpJ20z9U1JeqOYjtfCNuIzjjSZCLUZtj61pMag_4c7DCGoQl7bwjdVfO-tdTr1BEkJ5uMPfyirhLtAAuLyx0RqwLzJWgxDqCEl9rB5dDzqwWRTOuUfv9ctcY-IZUFC11pwTOWVkau94dKYg01PluZOAdOXbgJaGl-xd5uPmDOQpCcnnoJJe-secFnsRQIWCn9AvrmfL-VicC7M_oRE1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0u8h-aGc5rOXdrc3IO9GKSoh1VF87-eVgFHHQuIj7QgRohZbS0rykw_ZArZLVc2OZQovBebN1lPyNbEm1lt4DF6Nyt6LDpx30WStvDQWz5Ml8OA7TtpaIy6jbPfK350vHGUyVSRLh9OMLkCeCJwRNbQITxmYQaGvj0J8viwDYTpJERE6agL9faOEvcQC553z6Lk84vT9wVcU7ocFeh-bQyAFY02v6Y8DuMLkXr8MOC53idCNX66P4Jf3qhW6fho3ulllLXbowmMaRlrs1PDmEJModMUCYOh1PNSj3It_9vQC90qdxijpK2L6kKhtrrejMsKlf2U7uP4_lpQpsOFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_x9KXN1tsJAZyz5uHLrNU5oCmpOdCA43Qt31WoE5gZ78hG8pTAQsiLUh6JnGcK-ix7c35WsWt_kEJLqb7hHTaspXTL6psJxF1wyhPz9T9m9H5SxwiUXjhMcYdOon98eakw9Tp1BocX-gmLZGM_SL8MYXASgl-L8InRrE1r3shQ6p2tgx4M3z0nT1230wd0tpLUjZtb3Rkr4Vqqt-otfO35j5lrd7IR2EvKFnGS7meFu3AgBIBU54zNmFGf4YyZ0fsGZWCUg6ql4mYx7TFQMqvCHXh5EDq-uOT1C7VA-KbNXtDjcUEAchyabgwaIBemecCLU6ZpFrBNUHH1NPAUWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4rxNDIylOkyo3g0vueufHW8n4C1N7VRxcJlZAQUDZkeyjj4u6nwUFoOVqPgeDjpVG-sHtGPJgl1YzeWd3RaXiK5xlpu2RVLi3EcXZfx4sDU9MVODqDrFo0QuBPDDsig6HAI3ZpNWnrm554ZAXjwHfHUcK9m3nVpcDHEXJ2WPt5W3AM0Hnq97yGFFAr-NXUpMxaXkOT7HAZTQlBG_CKxQ193ZaHmH8kYtiNik8ZexVN5kgHW8L39cev2hY2BgsJbkIQ251ZBnmh3EpkLlbeOMx-7caKyKmfJS6btfHFfVAWULh-BAWQ5vDXN_1jRjjfUQ6tTtqdRr87NVjvD7AQ-Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0r5vIfBvAd5zsmxiUXqwtTLOnujnfGaYsowFMuiF_pI2LB0PcFHcyXmXBv5N_wZ1HY2WFXeM0Max-GuW8Udl8257uqJ8JpzgHWJMMQD8AWUVHoxBPS4hJiCdLos4ZMnmYDbBnreZn-2m7-u5kPRvZkfSZTCgRWdrtKWxb8aU9XPlJn0cwLk6FrkvLvo5Rgr7qIQgYndb5Xor46EJjeM4OoKMLlERz8lX4I6OE5thTAOEJc0sbQAPHXuZyzE7rFAAGtizZ68hcueqFzXYZbLHeMdVhWgdSQk5h2HFn74QPsClzJq1lW4vl_4T_MtRyZzA_3njdgosam9pPzXjZE5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tza8e_BQf6h1FtEeuh2urNkaMGUDaC2Y5sRnjP94VYkSAKSJCBUXS0p8CNenP-vEHTQW08K44_ftwn34KBjegyQhn4dbhyilXk8g-w4vuSDeC2O4KYNUgM6G7-NoIVDsUW3TMXXqyMmDOSebN6zOvf-dEcLTGsOHIA2uynUJu4j_b7oIF-CbHsqrzcM7kIhwux_Z5-zeRdKSIYU61spj5Cz3Wew3YX2F1ViUYop4lHtEQcx9yOomPW-ibW3iEdIYaYkjyHjCnSfoLsqm4ZP_sUo9YxtpxF8uA9lvpDMB3O0kOAwNBgZfJEvNOHIciAVmCXoBwpggIATbC4XPBljKVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPRtlp6_-ZpqXXxnSeoimlWwNPQk0TM2prNRY-Gtz3Cc2VtRbfILlRpZ8lIsINlLb4OnHa5JFl2VgaRLb7EnRysr0QBVBsbHoo8P3CRj4jAITvC4CS5UO_D-aWaiiUB9Jsydt_x_UyFESwmHRojC3eUYYZ8ZFnM4y8YsivVGX_a7Rf2HABteO0d04BOt2yERvwsFcrcn42FnmGqiODL01KyIQ3hNUWTd0b6keI8GFSGN2syFqksk-Tv-J8jjy0347K8OoXPyR09IWNtc-iIlK59OUTNJfdsb1KyYnJxmbWoXfV78g_LXCgyRM9_xIdkUK7Xr6LVSnTaLJTQlcYubdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajDuu7imoGmR_YwhVbYkv_3ck7gxwjerEpwUWCPIJTVfNXzsfWfuqGEhYqGyOxf_t_8fpx3lHjsAkJByIsYvVeyR43I1WvuANAMvXePpxnJTq6bvG_a9xI3RfI2FFja-STfwHO4Qq5x9j-PKkBJGyVBq-rImNa9jVc8dpw92MigY85s-Jy5kF-dh57jyF3j0-kPLuQoBherTnd-Kprira-lMe677R-m7y1jh3W1YKYZo8ccKnZ-lUNgBObQYCdMh5Pm0e7Jh09vr7ZOMUR4dsq9hWGdyyVKVovDiHzIV2o5Gyxk_kxkqQUE5S61-tG8_1Ol-crKy42avHP0ZyLoBSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=v2_4NMSBqEK-1_HYHtpEIBf9e9hb3lLINuzYuJ9wZ1zlB2yTKBEeLdtmaYSPdcjPXDhaMPZxB-VT6tjRiTg3UFEBKbh4WE_qYiRcg_HYCUEenXL2LXrqQu2KdSFvoBVZJwLrLq9Pg5ASB8EAFRzYBk6N-e5kM5rDZeHrzoEslvg3zIZmt1C4-ZrNz_e-4d-RqQnTy7unobs1NOH2H2d9wIfou28v3QuIZyt9tLMdcji81xtLiCL1Fo-4u4NgfUzzrFqGbcoxm_UdU_bXxeMNOgK36MMS1H1GL2suZCtQrX6GBnA4Mgdou_5bONR_8VxlNz3N3ARxK8l7DUBJOzIjhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=v2_4NMSBqEK-1_HYHtpEIBf9e9hb3lLINuzYuJ9wZ1zlB2yTKBEeLdtmaYSPdcjPXDhaMPZxB-VT6tjRiTg3UFEBKbh4WE_qYiRcg_HYCUEenXL2LXrqQu2KdSFvoBVZJwLrLq9Pg5ASB8EAFRzYBk6N-e5kM5rDZeHrzoEslvg3zIZmt1C4-ZrNz_e-4d-RqQnTy7unobs1NOH2H2d9wIfou28v3QuIZyt9tLMdcji81xtLiCL1Fo-4u4NgfUzzrFqGbcoxm_UdU_bXxeMNOgK36MMS1H1GL2suZCtQrX6GBnA4Mgdou_5bONR_8VxlNz3N3ARxK8l7DUBJOzIjhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhjGby1IjL16RN-dOuy4d5LIOcM57_kYHu5IO-WqUzqEVJdcPzCnAshq7kHGVCFdIOsuJYTBIZWblCfARKfLuCJyFCLNZKOAUgqfYaEqTgTI4MNpVVzhKraVQLdS8ZEYMwL8jEgJtXnfrZbB9yqUamPNmXVQHD6ruEcr-6KjZ2XycEVwIWAdno2fsvLzQkbTaE0iTdG1McZ3ArPSronpGZjmhVQczMiPM-7Kw41o53tnwPyyc-yRzRlBs8MSTN5v4eV5lWm35F6HIqbCZYXmM7ijUb6N8GYf69Gbn8LNUDrKL4b4Fs25VoEry75iKpKkUaWrdHY20e5TJRscNNhDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=R6js_8zEAXNXPjv6mgfJpBLM-cCr1egZHVSWhXz9VT-ThLvpM5O8gOuDZi55lW-Mw8nhtRRwWANCyYXqn_LfQHUo7LFuVGAujg2Lhfc5GFmMkn_8uDrCRQQHF5L3FEhfc3NZfJt0dp4aAN6hHNfj67sbBr3vriAwsyCUbbu2vlsuTyu7xB6GQWHeQcI-xOHgdh2z2P2_U19Y9FludczDmR_ucgflF1jG53eOzTydsXOMtwKtSLywOxhBjiJx2YNU5m_NGTV_-qEPZzpTaYj4krjtzbwxekqsqwFSwya3Gswhy8x1PJ51QrjEfO6eqDErYXntEFMbQcFHdVJm0S0tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=R6js_8zEAXNXPjv6mgfJpBLM-cCr1egZHVSWhXz9VT-ThLvpM5O8gOuDZi55lW-Mw8nhtRRwWANCyYXqn_LfQHUo7LFuVGAujg2Lhfc5GFmMkn_8uDrCRQQHF5L3FEhfc3NZfJt0dp4aAN6hHNfj67sbBr3vriAwsyCUbbu2vlsuTyu7xB6GQWHeQcI-xOHgdh2z2P2_U19Y9FludczDmR_ucgflF1jG53eOzTydsXOMtwKtSLywOxhBjiJx2YNU5m_NGTV_-qEPZzpTaYj4krjtzbwxekqsqwFSwya3Gswhy8x1PJ51QrjEfO6eqDErYXntEFMbQcFHdVJm0S0tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=lLNRFiFrTHFT2jUBa2SWW5Vtte1s6185ZM8hukyKG1-qAo4ubE0TU4p5isumVlhGC3Ecq3zzZ-EryBZeKbSQX16kZ56843RM9rx8k_YDthePQP4xVrakkPMFi7P8LxJY1JdS_ikcRQazZy9aqbngiE9Dj891rRscPtbnwLn_a7LG9rDmOEg5Z4XAMJNh0wrLglvct-t5MaOwnWDhUBbUFUgIHubQfQDxB3Afh4UW_NI6k-S0lTNcbSMCk6NgrrqEHhe8oxFxGgEuv6J8o4LEorbxPS8FR9BbpvDoRh0T1Daja0tLHLmOVtlizy5jZwXSc8OTbmw_c4SQQNa8aRdzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=lLNRFiFrTHFT2jUBa2SWW5Vtte1s6185ZM8hukyKG1-qAo4ubE0TU4p5isumVlhGC3Ecq3zzZ-EryBZeKbSQX16kZ56843RM9rx8k_YDthePQP4xVrakkPMFi7P8LxJY1JdS_ikcRQazZy9aqbngiE9Dj891rRscPtbnwLn_a7LG9rDmOEg5Z4XAMJNh0wrLglvct-t5MaOwnWDhUBbUFUgIHubQfQDxB3Afh4UW_NI6k-S0lTNcbSMCk6NgrrqEHhe8oxFxGgEuv6J8o4LEorbxPS8FR9BbpvDoRh0T1Daja0tLHLmOVtlizy5jZwXSc8OTbmw_c4SQQNa8aRdzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly1pf9M7KwVC1nyDpqZKfS6zMx6Re9G2RUBztCoBJ1bxLB006XlpATd-DVBwzECRTJT-0W2Nn0NM73a7o4Srjdku0BmFRcta9MLTPlqe_VEpkr9-fYVPg9VD8R8fFLUNKB-A7Rp9gJXjfJ12FXln4oMH_TZktktTjfHW--HubxzST9MTskg0BQGA7N38u1TvzTEu8YJCwyXZG_ru4yRDeRh4P9IywCcBfpVr-69NZlJ7hf0-aOdlH1_94VaBK2K2xHpdrcIRhy-Hlg8qkUzvJNPbrVC6JaKZIyWFF6WIM3VVX9VSzoB4s2AmcNG4f3Cn-M2AVTBfQORmYZEFvHYQOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=R9DJeVKnvNw6ANB6xHJgngEWf0jswwHUdCtNSI68Fr3Pt4Sm_38oGow5P9l11yzM4MUjbAOVkHMfVKNTG2lRaITvxjIq8roDjxYKpjpV5darDyEyX6-ZpPAHrHIObdyN9yAErgtndLHI4Iv9fd-p5-vlSOssqLN-CTeToYsKq1mzQN6YW43i5xNFtMeRDLFAdPcyP6zsUgphPgrdxBX6dC45MgJhbltufl7N-WNipxfHi6sYoaGwCvCLx0I6XPTSWm4mTO1M3FoKcWmE6I4V34Y0B0IMdCSdMlVHx2HhwzTF_tmXN3W8gT4V7ab-vOnSmCFWGKwKD3cs51R14D2VRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=R9DJeVKnvNw6ANB6xHJgngEWf0jswwHUdCtNSI68Fr3Pt4Sm_38oGow5P9l11yzM4MUjbAOVkHMfVKNTG2lRaITvxjIq8roDjxYKpjpV5darDyEyX6-ZpPAHrHIObdyN9yAErgtndLHI4Iv9fd-p5-vlSOssqLN-CTeToYsKq1mzQN6YW43i5xNFtMeRDLFAdPcyP6zsUgphPgrdxBX6dC45MgJhbltufl7N-WNipxfHi6sYoaGwCvCLx0I6XPTSWm4mTO1M3FoKcWmE6I4V34Y0B0IMdCSdMlVHx2HhwzTF_tmXN3W8gT4V7ab-vOnSmCFWGKwKD3cs51R14D2VRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_nMhamzsOw71p8NcuQVpgzLFlkkvnPqLCeO9rSTP4jZyiadohSElQ3b0I2TRlwnBaVQ379OF3-txISib2scgpxTFQg1vAUxxE-TztjpjMsRNxfT9_X6w3Wk0qyUOm7JDZ5AN58f4XS-eWlWufiYNXtw9URKhKX9t_urSxLZbYELW8Exm6ifN-aUeJJEUBwqwqCk9Zz35_TI17z1_7UV2tNBBdwD0X7frXpkaaAu8Bianv1v9OhCDHb5UoaZIoR7x4CFuhDNU7xF7czQ5uLAf8DQPZxPgqj-AKd24XNDeIM9pIWIo2Ptpzg-vvTRmJI21ZU0EG7qUV_1aOHIhjQ7ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyaPd16yAtMSYmPAWL4lSQm1Dd7pOTI53k75HXEifCO7rtTDpMDZFzjGkBJeweR6Pgrezr5YJJKOwD8HA19Jkq5xBmm42B4lBIshlQy21IQL8QwKWDjADrX5DSx_IZh5iSH_dh8G1_eMzs0JPneeGD6fVu0gNP-5ZWHrLPmhCoPbvynvLBUFQ8SOUlNMLl_OEuLHV_I9c3YuBmntRZYP5yX93Gd10d366jh3KBrpx4wqnpIHSvev52AhhFZg5e3ag8TNtzX35eHt4RDblToySfFjgEEgRUdjSVXZnca84OVysTMa9OseIcak6QmehE1AQvV0BLLx3hXLaIfBIGq5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KKYOCHxr5WkEM8hjq7WePxi01IMYuVGqHPC825FmqibFH-nR9fd1VY80HKO7fNWlJsieb73DVktUfNApBD3LMCG1MFBMhVC7nABk5qDgRW24ptYnXwtkKpWLKLyaWcBSIBuiNhzxFNFjlRbVcZSMmhdaUAZhMgksDQ_FXdWR-WkVg6MbPxzwyDIayFnSG2d_aH2ztNF9TFAKKXcZa-AdnTSb2aKTXct9mLlA7mc0rrscCJEizH1RDzwU3GHIZ9pQMiNGcjkGM1gVm3aL1XSwCFv1MSQmd65icbjcKbEkYj4xLxSqEds2BH4Nr__CPV0qryaoMNnf2TfJ_VdGLXgNpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFyoQTbSGo41pkOM9lYaFnwd-c749VoukGMMlng_FV3pbVNqkwnZMsMco-mR-jB7Nbj1MgEyAJLKSPVJqssRO65SW4Ra4CCl5g3WGuJm2gaq9cLZUe9YPibybwIMtWZXb0VRs8l2A7ljqgl2YoSglmF9_dTcbTrYnBtwlbdBKiMcL34HZaWlwqKRT9sumduAfleF6R_hPZf-be6gTt6ytpDhRTUC8dU8UOqcXoQ3JHL-TNOJ52_TO3aiJZHd_yyO0-Q9RxjPPfsLB3o4NFd2T162GLmJvHWjZEKkRV3u9ylp4w8wdaKqLLD9enjOrPz7Kk1W6elJ3GpitKdJsgwdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oorT-byvIYvN84x_QZa04S69u9VNtoUvGPFtkIf5zNAq4-7ah32kjfGnCCN4OBBWMrf6fqZCq8gOTF0zCWezGnJuQ3HDG6DQJ5D3ONoWDDNKC1fsGJReAgDtC4I9mAHetmHQPGHlwia_evG7gXvpafAkiod-7nzEaro9PMhSGJM2yc93oe64dFnN0EZd-XspMkWD6VHpt86REPL2uNBioOnMNp3i4SLYi0YBKaoIsf8Qs4i_qOH1iDIzVp4YBadtYlHD-dSpyRgw7kSuR4jNQBzqROpQUwli3N6mVgurX4E4PxNIdI6pd_0TmSyZDCleFld7y1uBkRLaBryCZZrdGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXqCwLVDVVhqMlO3UsUD2V3fBvtTGXJG2JewAdNigAdG0bcCAXmlQWgAZUykU2EfDNdcWUq7kZSY0Med3unA5i9DtsHwQAxwPmwORx-QkySUn64NtGbNznPioy0iik7yPWyMLd-rCK2ybGoblABt39nXWjo0CLh6j-UOcN0_uBGQsfJBmei1YufEUtndxeAK-onmtZTLPYsqGNJrjY0oLRUFasPLobgW5AKRY_JlK9NTwY0s2pWq0ArDKVvq4HOmn-a4SShA5CslKNl0fdnnHoKZmYDboZ9TjpsYFAolPEy_FCymbzZLPef7ne1wzYGy7RC3vLjaOiUtsfSnB2ZQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9OObgchAJcPia8p9hBisXZ2kj9C0XiVa56TdPQixnYcXtLp6ONZJyFO7ia8ZOr28BxB3wyS4plzqV0wsblgjF1dIcRjyMiIpVPhGJOv4b52AUZqED5EZM6EpI3gZdNat_N13aXdTCiPcxV3uvdUlQ1K_jlEiLYH54pt-Ry_6wtbxqLCKZYuiQKOdHKu-O0qfED_z9RAPcbepjuYhaaRQERLFyDMZIdfHDApbyNVcxxsIttpJEUuNuy0WtWPLmyJlxaXpzKp_3-DlCfZYN9DuCMx-5X2-k9zEWCjHLrpkKwEY5RPPeim05khcGmmlYncVl71gBQp4YjH8a9eczH2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKJYQD414MUzxedqfMrIwXGR7ihjnkt_B5YF1G8EN7T4-1NbB-4U8Rf_vyCOowxQnkduekbwUZXRxYuVy7YTWt2uPCFEpJyCxliD6Mj57E8_wDK-cYzN3ZMf3g9tc4fgCUAXyBCvVpxsrDb1KbOuQpnyuZjS5IyZaWHjM52lYuA7ukAloSBVhlMOVH4Pbtw-spLdo-1qc5M_vPqMezmhZs33x1M3odbXBZwIRzR2Zi-cu3QroJi-k6S-4iEUm5blYco1n2GHnuDkGpX0ie4I3KD9S3LimBktajhMLlKC2f1ryXZR-nIXlbdoYYEidzIHlLsI5H7oRj7aHlN7MjlNLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=W1_oUV66KOi1bVlR96EWV_XHYxwp3t1EFT8kISjQi4iHMbo5STwXB9jvKkozu7i48XQmP9yddmf-wvS0kJ0LVDIc-6jWotXTkkvR3m22ccrm6yH7IgbZbGmXXlB6ieR000lekHoCm0jRDRYS8gDIAhreH1kmrf67gCnqx17wwug0P_Y_5ScgNUNZAUjo73K3Q7JB4PQQghfIYgz_aV2C_LygYhxHd2GXAPHg0C9fyop7Lmnwlmf04bBKJYyMe56kizzqcWD7kTgxzkzR4BomWIYz3g7tSkjz9RoNe5z56vflvJuFEzGlLzGqrGdERA31lxQBq4k0S_zQ6SbVZsX5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=W1_oUV66KOi1bVlR96EWV_XHYxwp3t1EFT8kISjQi4iHMbo5STwXB9jvKkozu7i48XQmP9yddmf-wvS0kJ0LVDIc-6jWotXTkkvR3m22ccrm6yH7IgbZbGmXXlB6ieR000lekHoCm0jRDRYS8gDIAhreH1kmrf67gCnqx17wwug0P_Y_5ScgNUNZAUjo73K3Q7JB4PQQghfIYgz_aV2C_LygYhxHd2GXAPHg0C9fyop7Lmnwlmf04bBKJYyMe56kizzqcWD7kTgxzkzR4BomWIYz3g7tSkjz9RoNe5z56vflvJuFEzGlLzGqrGdERA31lxQBq4k0S_zQ6SbVZsX5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=gTGAZolgUtsjburtj1sSX2OCYEhTk18Rfi0N9GBWalfjyXYQ3izJcYhyYxfxR81eghRlXSZSZTJoVxLXOJebOY2crChJ1KmfSNe3EcpnTC7Ei2F0ymxDIKvAZeazYs7j95YOYpfU0zUd9pzW-VIO7lGv_R8uWAvV_tqaHDEL2o9FlRzA-js0VKHQdLIEnfHpNx1eP5VVFmE82W_e8QCimicNng1tCWopnnmCxNY2okp0ph4Z2dKbvCIjMkKRJdU2PfcJkuo8bzinr3hdX18yblAVp59RlCLhRB0V3JkJmyKcWQ0WGGZALmmt90Jfab8Po_hPmH_jIlR3Ln2GYaKdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=gTGAZolgUtsjburtj1sSX2OCYEhTk18Rfi0N9GBWalfjyXYQ3izJcYhyYxfxR81eghRlXSZSZTJoVxLXOJebOY2crChJ1KmfSNe3EcpnTC7Ei2F0ymxDIKvAZeazYs7j95YOYpfU0zUd9pzW-VIO7lGv_R8uWAvV_tqaHDEL2o9FlRzA-js0VKHQdLIEnfHpNx1eP5VVFmE82W_e8QCimicNng1tCWopnnmCxNY2okp0ph4Z2dKbvCIjMkKRJdU2PfcJkuo8bzinr3hdX18yblAVp59RlCLhRB0V3JkJmyKcWQ0WGGZALmmt90Jfab8Po_hPmH_jIlR3Ln2GYaKdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=SjSZ4Kd-hFOXiYDKolmZOeth8f68gfhWIWklaCMu8nVSjNc66mmo-GLvqMDRucji5d6VU_aQaglXMZQ34R4Hc8E6GiAp2BN1YeCq2vXaxHGEpuUmjfNE3yLvMEKWqr96RYvjDEp1IHM5e3-L2meawJQFxpfPGrQv0iIcSodgjUdzblVmSNbi3AFHF_WYFxtuIgc8h8EqyB73UFrMPldkroJYjO6F55mhElp3KUJrquHlg0UNkamnM2OPy8ib67QSus1f9-OX_5JdBzXKPK1bT4oK0b5QDMumcUKu6wkRCDkMelC_jCIrRz0TMvDdV5PYQd5yanclaPcp6nKpJL2Pgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=SjSZ4Kd-hFOXiYDKolmZOeth8f68gfhWIWklaCMu8nVSjNc66mmo-GLvqMDRucji5d6VU_aQaglXMZQ34R4Hc8E6GiAp2BN1YeCq2vXaxHGEpuUmjfNE3yLvMEKWqr96RYvjDEp1IHM5e3-L2meawJQFxpfPGrQv0iIcSodgjUdzblVmSNbi3AFHF_WYFxtuIgc8h8EqyB73UFrMPldkroJYjO6F55mhElp3KUJrquHlg0UNkamnM2OPy8ib67QSus1f9-OX_5JdBzXKPK1bT4oK0b5QDMumcUKu6wkRCDkMelC_jCIrRz0TMvDdV5PYQd5yanclaPcp6nKpJL2Pgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5D46fBvHQPLGPf0PaBCOsF7Aiq0n2o6xLQTxwqk2Ay-Wa0ltzEiB1EJt6ZOQcqB-Q-wpw_icD8H7KFV5vvRtGQ1HU5O3Iww5wn8cnaqkcbPdlKivLjDwgidG1YhXkdkdj347IdKTQZZGpCGGANnQxzdF7zXCtCMMZJtDTXtSbPXtgQzlj1uY1o0Oz0tqNFerBSy8o-sB3MaLX2VF_ZWZz4xzMUgPhDedmMtDIEF37MbkdoPL2EwcZOq-bG_yUOUT5xtpZG5Tl-34u-BwElsXpEw8J9ezGIcalMkPTMKPwXj1bKG8EUNxVaQelR43ZCblOq_2zSADHAZYFsB-0d3xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG7qkD36uoz7Kmya8OQFHPHsbH6NGOqe-T7Bh2H5oCwr0LHpR1mXknew-x_QuM877xV8sygoGbykxSJHqI2WY7KZMn0L4loXc-JJ1RNhoxyjPEENy6BVUY0fCmf5JS7BsFWwUoUtxpY0diP977qtg4Pmba5qPqRmYTUF6m9Yhy5MJnVEPUcov0YG-YcmII1RKC1Vu2jxPOpU3PSOPT4CL_Yp83gB9wPCn74eej2SZLCx8OPkykYjtdTizkTQIovZdcfsNnvTKUtDXBOPowvnKB5ezaYctMvZMtJ0jyI28HML0molA2Wfsa8Qnz_qxcaSLIRtu95zLUCc3s3Tc0IZKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz4UpAfbPUxUufFKuiPbQGUoGSlmtfnrs4HxPT-KceCKmDFsIIF6lUQN6Qr6g4xRU2blCasWTV6QPS5OX46d9pE-9i80HKxAFjnPzbXf9EnL7aObGi7yD0hWTwR4xB3XF0hN-TPG9RFWX8keOrst0qazTRzLc9wBV9HnD_nNpuTDjjJVAocGIlkwojhmVP_iL3YB5UdWkn-FgrsCTYrCdy739j2Cf6qQsKNkYZDhqqrRFgbrWcxCUhi0r80YFWImMb-0_Hp4Rd03S6ZbAg_ukI6rDb3cypBz7-Dx-DP7JO6nI_mkLkiaC41c2Vh6DeMDbSaZH4B-iJSS_EFcf2nNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjfEhxQlhh4WvUH_zU7k8rbIlZG8bd6zGBMuAfP16zRgyBMQtRbT6EsN54OCaUZKJW89NDd6Wxy9xh4ayo9LROxmGSWKKvsnkPy1Ar8Y1BtmF5DqI-kOyfmzA3ALGpVzv4hZWJbAJL-AqBmQeQOpJBGNIUhgTCKkzTl3I8wNwIQPeX9CvNmYgdaUyNpDmdG-ojnhjYYMme2IO3Hd8FDURJZnwS6voMXV0eVTp-YQFrhxvkNuKbzEo-kH2AOcxxhEWRkf9JHEMh7kZVJ2Tq8eOofRzocYLjCBCugLKJrxH2JWNjmae0RRCvze9e9LMdJI5_LRFOb1lbE359SSqBJsLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=eD7g8OmnM9FC0Ufun-3jXzHpb9MZCiLRPnrm9OW9ieh2UiuuV1IRfGzZ8TnN_lH2BaveD0djhTY-XUegsE5rQMLumgKxnaF4Pw0psFhXP4R7BvAz5kB0fEYjSjXF99zDhImAzoaUiBDbeOpg4V0Z3_Jcbdi3HWKhCfJK-CsWcvY37a2_-RtNRciKzCAZLPbuNue-wcPXiDKCDtu5wAmIk0XW6n8wMTq0eFx0pZOnlKPf-5YZXYx6zopu20JlhTMbG7KqMq_IuKgGzJWzohS-lT6a6dsHI7634LvlmPhKK8HtTQaX7yPO3VzLyTQ_3r-VEZdnUSPzHw3gxbi_JGZRwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=eD7g8OmnM9FC0Ufun-3jXzHpb9MZCiLRPnrm9OW9ieh2UiuuV1IRfGzZ8TnN_lH2BaveD0djhTY-XUegsE5rQMLumgKxnaF4Pw0psFhXP4R7BvAz5kB0fEYjSjXF99zDhImAzoaUiBDbeOpg4V0Z3_Jcbdi3HWKhCfJK-CsWcvY37a2_-RtNRciKzCAZLPbuNue-wcPXiDKCDtu5wAmIk0XW6n8wMTq0eFx0pZOnlKPf-5YZXYx6zopu20JlhTMbG7KqMq_IuKgGzJWzohS-lT6a6dsHI7634LvlmPhKK8HtTQaX7yPO3VzLyTQ_3r-VEZdnUSPzHw3gxbi_JGZRwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=h9C-ApkfHkVLvS4rJkN6VvIauFR49qx-P2jEhGPC5kG-PiejmKp8XwGICxlFc9q5SeqWTf8_f8Up0QPL-KktSEIc_vDabHath2LUoxXxWkpfJ3Z3dicUGuqPvlIhg6un_A0qEWSlLuPp38OOP-uA5SdJTaJ1sMcZ-KtVIMML3A5yJJY04MYxLFN8DXM0GM1T4Aq7QLVPmtfcEa-2ZrKM9R5fKTmDEKbTRwMzHSxyko3oDz2Gd_pwV1jPygmzlpizAkHj-TMGgGdHj2X2pq3jHYs2xhChSPKN9EiNFwE9MDp7H7sVMG0NqTS31f4YIH-qKdKOoxzvYYFDNC9G1vvRqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=h9C-ApkfHkVLvS4rJkN6VvIauFR49qx-P2jEhGPC5kG-PiejmKp8XwGICxlFc9q5SeqWTf8_f8Up0QPL-KktSEIc_vDabHath2LUoxXxWkpfJ3Z3dicUGuqPvlIhg6un_A0qEWSlLuPp38OOP-uA5SdJTaJ1sMcZ-KtVIMML3A5yJJY04MYxLFN8DXM0GM1T4Aq7QLVPmtfcEa-2ZrKM9R5fKTmDEKbTRwMzHSxyko3oDz2Gd_pwV1jPygmzlpizAkHj-TMGgGdHj2X2pq3jHYs2xhChSPKN9EiNFwE9MDp7H7sVMG0NqTS31f4YIH-qKdKOoxzvYYFDNC9G1vvRqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwIINVmClA7ROPYKzeeqCp-Tb53YE2NwECIjmUjE1Onx2p1LcnRExdvi82ToQOLg_z582VFKtvb_MxU-_T0UVoVg0mQu3kcMiYiLDZgOe_D8uz9zlW2gdjdtfYy8jMaZYQ-foDPzRiRbI6O9zz-N6t1uwFdMqjXjjnnusm5rax4TZxNDVXt6mNPXJcU7nFW-gSRGmfy2DGkm_H7c5gUtb7a--RbcSKF70XX8mU5VZCcIIukL7debX_OFC2P6_5m2ctTzAjL0fgx2nUFdNvpMyjV-E2v1_53LjbFaWVHx1-tQbnS8KCxsd1K4Yt-mUoPuffO1-tu5VeZ3e8V_pR1vOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9Pklq1S4cYHoITbOs04MdY69k6YluuWFD13BaXL8ja7P_T_S_eCYtdEl_C2xzkecap_ptjeQS9ewaaJC8zPpcLTwst_CwWsNVQBRda1S4h_tWVzCFa-REEXZF413Tfd_hgfd0mqUx_aoGxZFOP2kGGvTMo8xXJwJzQ1mlABuCimJdp87Mro1opPVvt8iRD4lk19cCoKtOqxwOOMq66jXwZZ_08ATx2mxGiCBMZrbR-TRpb51vspP6YNJM7w5oZgJzKtByeZ-YZlCN2Qogd34Lv-FmyImOrszgg2NQmlF_smH9enSjjNGPDulfuM7h9zj65JYPoWcPmXCt0M44EKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp1WW0gQZ-gtslo3M8-1GATmeO6P_OTYr2uwnenIoXLay4HJXgtAvEHs4Mbd-nj9ZWDRYR2iiEUiYwgEZUc1UUZzi43dDbYVYnmd85xEnWco5pHo3-0wd0YXA8fpUlb5WnAZ6q7gPVHn631uUU-zsVQS60Prvl9gtIjQkQ5sHiib7TCXZKQfnSRtzLuKTRhH_g55wx5tU531BmfSSF9FH2ojgXQzw-NG4Kq_o1qr5-X4uTsgPE0EdrCuNr0aZ5keeVj1ILHVgbKrB3nuhKIivVaY_zhWdBuZnsNqLN1Ib1UeOQXN73_MjHoIcun9SiJujTW144BtbDFqrUy2zRpxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_eagV0pbDvQvxSfzr2BvsuS8M-xYLSZJxb2XEq1nLj371teyTlr06zNPpxDFbKQOiwUhnUtpzPW4BLRkHpBHRerClrge_YMSerSSHveqAKewXhcAdgQY-WS0vt2t45luAqreqGvq019QnOgprLk6iKLZJjuVkmB4fB6rvSUwpDHNNq1xROoqfegLwjGmk-F-xz-2WR7u6jh_XMZPSP4sCSYqGXflMIRo31GYvfPfawhQ3oezowxjlkqVpjPcNmvoDdtcT-bH3o1HxfKjZiEnptUBpc0RU6ue5PmvgKPHoSKTRwOx0EHKoPhfq3taWC3H47s3eu1cAGyAsH6k6ZGvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttdjnRpesVhYfEeCdtV8eWvJSssMmu-YHvtESXKK66G6Iwp85gk0hbnP3-6npCYkut3hrm-PDk6TY1D8Jz7GFfQuObYzSOfzHG9_glqALz5FM3XUDs4PfB0UgRK-Lu9cQ8fC2uqGCJefYnAsIML80yCGgHQVFK1lWRa0U2Ux_dCYRlBmkWzgY--TsxORZhY4WTuRbBGWLj_-93KbeadrJgrV4LpMbsDk3x6T7gCzNPtr6zMJcFzpGH1kalEIZ9GzrOTIpjSdEYHv2Uaon3Vp7zSPo99z6_X_M1w0Tgay78vUoC2S0mfNcwp0OXaHzFAHtq92V4YYGXKhM63JvdqDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRPjU7ic_pY-hBa3e95iAxf91sWnND-u8LNf7xiDxAj_ReDexHc3tiVUSGkKGCWrPfSITPaGqJjOG3lTFrvXGDSzkD4sWy6Nm2gwUIpgFi147Ntv-yoJ7HpruJlDPOngwjO3UHegO5lAioLaUtJp6HIoxwLU90_pdV3u8EEVJR4pXqnl1oVl3AwGD5i5wTbE1TjtSK1oqKWpGhPb-qtqBc_S9Ql2LxuyHIZOio2A-z9VrT4cB88iprsI36H0GSxCxBYXBLX0a4nByuswzKGFodeHz_SCYWeALr8Jvun2Z0VQ7GvgKScFzulnIZvE0_t_izGgLfWYpFrRx_ot7R7JCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNZgTjZH2euLs_eQmhqoRna3cdXC6vqrm2BEq-LIkPQ75DM1kSSOAdsGjxH_w2J7jG76502KysdttlWt_cifNAMlGL0enz5TAVI5w92plaQGs7j1xcJHhOWbu0JFgKYwsFmEFSCGsfZHnhG-70ZxH2sG5aMd4zTplRJ8lkng-WYhSdKIwRANGMLmS6RZkIU-9L067_82wQDEYGqONfwev92ikRMQzZUXwjPIhlOsiSSsQfCH1ZTxodqWh3-pNH4zhbrEXJvsUC-CT-ck5uVK5rXHsz5lIE18pgi1nT3XknCV8r5D_9FShTQBtRIaHihY_xUvRn774ggWdYaMWFWwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoohPIXbXixJtsr_v4WeVbljqAddFxUo8Sq0jBJYOmvivTmbVTm9UhFHV6VxIysnz0g_9ZtaUxWTX1kNJk_T_fYCsxPFSnFNqgNpZF9MAw8VD_XcvIZUWXm9kICSpNUzMYs1f_WHaJ5AsUY-4g1hcsw60ZFqsl4pZt2EKbmOM9TNM3xZeL3Hkw9CZ1oTCB2wX6h3eWACdPJlnYV1-XFJ99WRRvie1ysPAvPg6u7e2MQaIuu1pnXTg07BgxsBlwOw0yQBiXFSD_HRk2OFHX9bA9xLLbbFbV5HTjA30CTEChnA31pxMPS_tjdn0iydeslrGDMOewC2A8rHfeyUKGDqNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=LdWsIR72QVtao4cs2f58fbrdYijlXeHDm0R_ho1XBDJ0GV555dKhqI99pw4jeE55ettIqTrae_yhHaMmzRzhArE01yesBOFvvj_ofKEqSKfO8e0MiucLc-Hi2InpH94YVNSkfGkIye0YNp24HIrlGX7co8gpHyNCp0GYu66TtaVE2POiwhp0hJ_rYnkd2kTMAGUhAWdKAIqkBOzW5qspku5HoxENAHXVyeWOVdbenk9hkjXHQZf30vak4njn4euFkoFsJJg90nQTTcrC8TEBj6U_1wCBIXpNhloIM-AfFbUqAffUTl1WbUp0jpv_0uJg7p6JodyYvSDbY9SzMWsqyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=LdWsIR72QVtao4cs2f58fbrdYijlXeHDm0R_ho1XBDJ0GV555dKhqI99pw4jeE55ettIqTrae_yhHaMmzRzhArE01yesBOFvvj_ofKEqSKfO8e0MiucLc-Hi2InpH94YVNSkfGkIye0YNp24HIrlGX7co8gpHyNCp0GYu66TtaVE2POiwhp0hJ_rYnkd2kTMAGUhAWdKAIqkBOzW5qspku5HoxENAHXVyeWOVdbenk9hkjXHQZf30vak4njn4euFkoFsJJg90nQTTcrC8TEBj6U_1wCBIXpNhloIM-AfFbUqAffUTl1WbUp0jpv_0uJg7p6JodyYvSDbY9SzMWsqyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=DATefvkUyVMUYgvU6NzkM_A3Jol8Apb4_rpxfFjccUv0GxcUvNQa6RI0lEAwD78CpEb_mmJc_6ZAEajjHVe0DA2PxulkVXH-cvbVSQOOB4I3kqXh91F_9lrCupgt9OX1k3Tt_LBwydD632LIpgT7s4sWSHfVX60kgBdP-GyBRVEvfFVeVp0oUIhq0Fc7y8UzXkR1_3-Nl_U35K3kD8rKblcx3K0dDMjxZ74Pfcw_7Cz-utve1-8BCZAC7sOZg22rKjJjrCjJPmWtEvuPXI6Ql5V8AgICIydFyoxVAYHWAws_QqKgyIeWY6FiBB7vzv-lu-MkH2P0_ayx9N-OlIM4uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=DATefvkUyVMUYgvU6NzkM_A3Jol8Apb4_rpxfFjccUv0GxcUvNQa6RI0lEAwD78CpEb_mmJc_6ZAEajjHVe0DA2PxulkVXH-cvbVSQOOB4I3kqXh91F_9lrCupgt9OX1k3Tt_LBwydD632LIpgT7s4sWSHfVX60kgBdP-GyBRVEvfFVeVp0oUIhq0Fc7y8UzXkR1_3-Nl_U35K3kD8rKblcx3K0dDMjxZ74Pfcw_7Cz-utve1-8BCZAC7sOZg22rKjJjrCjJPmWtEvuPXI6Ql5V8AgICIydFyoxVAYHWAws_QqKgyIeWY6FiBB7vzv-lu-MkH2P0_ayx9N-OlIM4uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMAKN0zGkJrL4_7fyoZhKltu24HaUJEYGH8ilXLkNiRk7jb1l2mDjzGJSI7WerQY0kaVn-bRkgh0CF0SVEFEbchuozoIsMupd41WCebw37ol0CM-OK60yxD0thj69N3HcM8Jvr_Dc-UmDYfDt5sdl2-usHYNY1JCVZ5Vw7y8m24Hk2xl4JA456-J0QnnivL2VFRY9CqpUg_hXL94luCLdqPssIQkFJpizjUZ32K8vKqlnX5JBc9RY3r6wOMA6D0LneqfABsEIwurJBG5EUN0gm1DM7FtP4In9YsA-TAJCmPT0R1JKn4yIgdjhndpCfF22Qtw8V-vu5jEwTY7hbrnvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejbUcjIK4M8Gb9npL3WK4ui3oGKAwFeN6SdB2TzCl2b3STp001QTBAcy8zEkh6OL-LLOGlEf_XCP-zjHMiv3j-5GmVkEFB1HH8cz2GUmUMmKzAMkHlxXGGU5KWg7zu3w3d-N1IRLPRs3JJb2pqx89EGK_jhSUiVnlVM24JMhi-jJ3cnBoFBhtAuoorBu_DV0uq3OwIaRgSMB17raOJ8-ZhWTxsNwtOx-0I2RvmTF54FXsrRdB-j4F7N6_Nm3H9d_kfAGP7WOLogo4lEmjdu_zBo5c7D1oMH_jC06ixym_Ybfo-VnSdH3Qb4QoSTHLcfqzP3bsf_rjzNfypBCI6KF2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=W7r7wcAXX3Y1WnpPWmfKga1JJni4yCwC9fiMki8CL4L-8Q3wqi0hiZSiEvmfoLALBF9RbcIJfltkMlWAiJJaOBdquRda79o2xvHIpQQgTaENF4QA302ytN1p6OVkp2Lj894VTo17HRHeg8xe4yAK4CbASO3irlXxGktN5rS4umhffTyII89ZHH4F0X5vmHq2GNfEBgZ82OoNmmUxs9MfW52hlRoOHszOtxyPG_LqCFb_bcdiPN97wkCWx45lEB-_9yBjUWbyj1W0toZJ9_uBL7sxW2mmvFRdiozm5FUmzONQdZ6VqGXGuKmP6FinQdgb4IrqfIggt-VN3_mSUnVD0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=W7r7wcAXX3Y1WnpPWmfKga1JJni4yCwC9fiMki8CL4L-8Q3wqi0hiZSiEvmfoLALBF9RbcIJfltkMlWAiJJaOBdquRda79o2xvHIpQQgTaENF4QA302ytN1p6OVkp2Lj894VTo17HRHeg8xe4yAK4CbASO3irlXxGktN5rS4umhffTyII89ZHH4F0X5vmHq2GNfEBgZ82OoNmmUxs9MfW52hlRoOHszOtxyPG_LqCFb_bcdiPN97wkCWx45lEB-_9yBjUWbyj1W0toZJ9_uBL7sxW2mmvFRdiozm5FUmzONQdZ6VqGXGuKmP6FinQdgb4IrqfIggt-VN3_mSUnVD0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg-Ycf5H-rI_90mTVBKSRO6O9cmiF0eSc310sIOnZz98EIL4phMB06JB7P_Pz5r0Jgx10Jb4PzWXnXMN1TXZxaV-2qzncfKzbaC8D7RNU4EHIwWAn0sD8FyV2AZWsfcQ2g1b9kkk25Rddrkzach4t9kOatiiUK3xTnCq23UaLOmaZQpZ9ya-G8YOvmXYkkHnC3qeyDZsZ7g6F3JoqxAC9411FweAeerBSM6l_CrhNcZAZcSHftX5qY7d0debrUrAR5OWMCN7_X7LxeJyNdSlHhjvU5EOzC7Ac6qIaJ3948STufQXy8HRJG8orKi9SbyXLTGhLXdVIAc3BbnXH9nONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
