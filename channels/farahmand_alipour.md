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
<img src="https://cdn4.telesco.pe/file/USd_8-UIpPPpVpem14L9t5-iSahJGCZDavATvbt_4nilAPK9Ic8zknyqgXad9l3I2qfDWZyNjEAau8i_iBi2vG3-QXIH9ljNjs7P59YEnlgC287O264pJm2NcmWfZyiAs_7RPw5HWoJENHXlhEl55Cq_MnBDReQ2xMS3NmctOPSMJHzde5grz9S3KdoSlp5ztkhRccZgjN5ytpJhf2viHiplGLz7dVuFBQILs0Y55DsRFZHChVD4R9HIBLfsRw5i-Q5XgwkCmR91fkDXEVLlJYStkvHyABO1IPw46rQoKeQIAjQeIDjOfIfRozGzTojSO6JxlYbxmC5Q2o5ckYAUDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 10:58:31</div>
<hr>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJhPQDmkJLTlJpw6ja_zEZrEJd56ME-NkYkGZBoa9R0wbPGVCLnazAHwy-K8LUil6pDDdPgSsH48JpuylotF6bmjDrJxOOpQD1CQgElvjQAR4nxJbv8OSpEGHrreXhIrM6H97Ig17Nt-xpB64rGmYj9HQ53cU-fGDKS1cpnVfswQmu5lvKiDeJEtssKN4elISDwO4ITtE_M6LSdiGRbsg0hgp-URwUNt_D_pU1XFqS8T7FA15b9lRv7yBs-KJWaAXDOS1lIEb7CULvjs6UddmpF6YmVx12lmmum2lUSKxjex_PHoRmLFWtCWyXUpz4KYp-wJ_l7vQ7PAkUsJoriPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6tZNI3quD6nOf4FYwG3c0IY2VbcbEn58ULE3wTKPRplKtlbPi-7-8jS87Nu7mfOLC1PXCLHhS5zvhdfOn1AYqqK6A52-Cskg7I8hKO2DfG3kKdu9UDaECpeMX612XIwokr83JnET9ZggRZdtFhR3TzqZ-atjSD372m9V7GpSpm6gq9N2x86WX3A4t3xoQuF-B4hjVFMGfkep3NKgLURoD4e6pvYwnGC768bLTIIYtmDwYbN8TmIvNc1fodTbDN6RLZ3Q-etuzPdgkWnvbopPj9X4Z11Lmd9eJoVWh4hDP9t7fPt1aMvfi5J5BDBm0-9llB8QcZM1daSiHq5uHyAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jut8cQceE433CeJXf-9_g1_bIv0qU6giDxbpJgJVvXJbKl7UTJPo-DfH5AxDhgKeG_G32gnB-Oziab_FB9LLyGLQMIVS77wMRSQBI1wvzoX3BwIcePIUNbjDYY-UlaEM3ZhFPMfLav9CpFHj0jAeCM5I2xPghcSwhUmha0tou9OuhRGZxtVGlJjPxOhkyHKTe-2-SJqZp_WK1Oknw83qfab6U8WDLQ62SgFrrbOMRB6RNfQGFzLlplSfHIN6yM1kGCZld7aey4a9kMhapREtb2FIiWBrOX_y-Xv5KEvhkQLMzLb3EULX4PA3K__lFA16otma-1v99gtygWBggTGeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw6bpaBhOneVqI4HAkwRI-n4FmRNhSz5954foGCsGClRm5ldPNG_Y0VVx8NxSvl8jqIkKjtV0aNQ9gmyWeIg_Zg8I2Xsk-sVGj5eVUv7yBGfiT3ouwFd6PDrDice1397dgubbvOTPktnVliKyLVkzhhlXzGWrJCqtCpmhf33P_3RVm5az2yGYtRipgD-AXFI491fnACJKYMAGe35SLKdoWXgjIzHNICWy63w580RNeasTSnDd218RWxRBLTzg4XL-wgTESVKJkctWumhAzDFoEeAtQDMJyjnxy0vbB-kKBFW7TAoQ64Wxgan22HGAZ9I5uXQOR47486KiG_lhVBZBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Utev5yPOd-ooKzNstrUIc-ybcjSVSKLbqLtxIVNTXGsCaTykpa6pjGrUJnzmI0HmrtPRVPFmtT-RH-9OKU2XXh5WhM8vF76AZj6IcPL1pswXHJVigtuDV-oGucR-3x5ua5V0HeYf9UOnmDYEOGtkyqLXHMTQqv5A5mmPE5g3aGaZ9na90F8Il3WXM_3o9rdyzQoWwyy4EAgxK1E8WYtpBZha_Qn9mt85M7bK9_9GUYjfYqj4g9YvYNQb0koTegOVZKap0IhVSVnzFVk3dhc5f8G8MiNEZ1prBkF5gGE1tfazxQ9VVYXmWVPbTmnAony5TXG8FtmcMRGtqgI8xA99iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Utev5yPOd-ooKzNstrUIc-ybcjSVSKLbqLtxIVNTXGsCaTykpa6pjGrUJnzmI0HmrtPRVPFmtT-RH-9OKU2XXh5WhM8vF76AZj6IcPL1pswXHJVigtuDV-oGucR-3x5ua5V0HeYf9UOnmDYEOGtkyqLXHMTQqv5A5mmPE5g3aGaZ9na90F8Il3WXM_3o9rdyzQoWwyy4EAgxK1E8WYtpBZha_Qn9mt85M7bK9_9GUYjfYqj4g9YvYNQb0koTegOVZKap0IhVSVnzFVk3dhc5f8G8MiNEZ1prBkF5gGE1tfazxQ9VVYXmWVPbTmnAony5TXG8FtmcMRGtqgI8xA99iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZDC12oBufPddG70KmZA7zjfZUPnhmKYUvV4aUS6WINeP9XbTstDi2fAL5aWRr-YoJuu9Z6TCAFJYbGBmaTQMdbB3Bp4wF5luQoxVGSLa372BO7ODr3I2QJRGPYWPbqfA7g_suaQw72TZdKtaaoDP3StWQVm3FlGBiaeO0lv8odXQUDac4f2alQ4XuSiYpteXYxwt1zPkU0c0REjBpftlfyte3n1Ow9HrXbNBDsdP7laTJoPhxF2FRnUPd36KAUBT7b29j2JfhKCGD42ar7uVaxCN35IrS0_42MMisGd9AP76SJozRS4qwJRuTHLKZaqolpmkP1rIOZHmnzGh44-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJrw3ChXN3NCI9-ptnOcieOxVzrDApaY8cG7XHGcX80bifNNc1oCbcpsNtBAYT8WSZJguD_If1bchEoAANRUiNdgTxjjtR2nu0WusDDWjaMRRyLdKW67MQZWoaZLYlBlpB6nAxGRNCK_7buokA5LxL3ZN4aGItZS6f4CMC8Gocno_cBnr04eyi8fU--e-49hMdCXGQPfPXkiO1cShOcoO7SKLRsNKo0EIqUxdhpUkb7M5l4uVjxB6h6nVlNEJEsPnxH7WhiQnXryCGshjY4sVqJ-CNadxLGowYOQB-Q6o9slsVHWI8PeDX0ALzltigpjvOuytS72-_aAvocI0vuKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IwKb054uRCtUHTVCZZ09_lXiAeZyjTX9p8F71v8Qep6O9sqcP5xj1wSvzhkn0Lc3lkoUExRODxehDdqx01HfvnCuJcH3YJtqqQueDpv38K1wntMbCt5x3YDIlrOWgodcHuI8W8Hum2vdOjf7aJ_v6J0j4Ij2WMuQ58luQfPCZSRucYw0tf4viT9NP1lpnU_2z-eGXYS1F9zuId2oLstoCUUMU6x0a7rPW1XgaC5YzIODXVkZjc2VWrQBYwt99k6jXiuyOCeeseLT3XXw8IwdvTswjOBcj2fU6wA3iHVEH5ovUMakRoR1qTw8KVJo0-cIRwXVCsjI45xnTwshMx0f3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IwKb054uRCtUHTVCZZ09_lXiAeZyjTX9p8F71v8Qep6O9sqcP5xj1wSvzhkn0Lc3lkoUExRODxehDdqx01HfvnCuJcH3YJtqqQueDpv38K1wntMbCt5x3YDIlrOWgodcHuI8W8Hum2vdOjf7aJ_v6J0j4Ij2WMuQ58luQfPCZSRucYw0tf4viT9NP1lpnU_2z-eGXYS1F9zuId2oLstoCUUMU6x0a7rPW1XgaC5YzIODXVkZjc2VWrQBYwt99k6jXiuyOCeeseLT3XXw8IwdvTswjOBcj2fU6wA3iHVEH5ovUMakRoR1qTw8KVJo0-cIRwXVCsjI45xnTwshMx0f3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=vjYpivuP1BJYpcxyQuwpnL657gULW2v6HXt8_pr9dgz4JjZcv-rsQDA39r4nbkBxWMzWvbPHkgCj8DjzJOvfys8ibigL4Y-SgA5NdCQbJwr815z6uRH16p4-6fkNIEXFK9tuSToo4kd7l1efdvaRVaYcWbo4Zd_64dmYIGOUwBm2hg_3R-SdsNcPenbNcIuzFqqSPyECcKVYxGeydHPuH0lah5_QiyzLMBUfvCnNUv5ycPhwE0sEWPoW1H3DP3pt37Q0Gd_TdEt57lJtYzM5-0LKqJiWPLERTgpeNvb8qmq9IG-7zPz4imJ0AEWXLXvbJLIbFMrIUJxPuP96f7ETMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=vjYpivuP1BJYpcxyQuwpnL657gULW2v6HXt8_pr9dgz4JjZcv-rsQDA39r4nbkBxWMzWvbPHkgCj8DjzJOvfys8ibigL4Y-SgA5NdCQbJwr815z6uRH16p4-6fkNIEXFK9tuSToo4kd7l1efdvaRVaYcWbo4Zd_64dmYIGOUwBm2hg_3R-SdsNcPenbNcIuzFqqSPyECcKVYxGeydHPuH0lah5_QiyzLMBUfvCnNUv5ycPhwE0sEWPoW1H3DP3pt37Q0Gd_TdEt57lJtYzM5-0LKqJiWPLERTgpeNvb8qmq9IG-7zPz4imJ0AEWXLXvbJLIbFMrIUJxPuP96f7ETMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey0VmbIAUkiElqr6SWC70Y85W69OuL3mmi5unlyjdDXPvj3uUvdleu_5aj1Ky1t1pU2bPkxHFATQTZesrYrYVGGaLjw6FB7xA65fn9E4BZkuSF0CX_rEo0Yi2n_mkJZEefglyNDonAxIzzTMj8QCyCVohRY40CVyQCG67qrrMT2yEDN9lzvWxEi7AElQm0sDK9xBMsbuspCHJGLcMrHMTN03ddXEOJ6PVHDvtY1-1FvZfMsSWVwqKi4wl0ThAbgD5Lzo5IkK2Kh9WTzCUu7iyB8OrPUdALgEGNKjYmKVIz1kQASaN4V9aseVMnUbkiebMVCkVO3vTv1CdL7p47BhxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7qvoOItctJK-VdGQij_2wFAAVfwkf9OS60ENYyKCqeqehDSVHGKLOAn63k7qtetDOH7E3zqof0upDWIKV9NiQUQrFUCyFTRjMbnBRH_sFvBGIoFFU-SJIH17OSShXOKaKGT3sQXze8tcSegdh13hmWdEZuIA6FKLIYN2JxkEFUKGbnqJHsKLh67bAI-J-7kyXTwZpjLHgHWiXpNS_u9jrymtS9suSEIR2LJM0zK6VdsfcX9hR9lcEcx1QlGBftOa4jaZDLLIgq2UArmr4211uwG3c_f9w3oIFhYpzHsMxIfQHUSFkGWo4Pc3zi1ua07QO-MZ5MkWsISNCNYl3VBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4BK3EuCS29AB3BJPIpoHfUNLBeFp4ZKIXBWFtZvs5m-zqP-qPAfdSUZlZ7J4grjkCLXxUH8HIvkrCKiM5DXwAAOAED7EiBJqgdZmYLi97AgWp-4AbH7V3hWin-kiD3QgmJTNuQj5LEplreJOn0EqOm1e1aekD6LfkXlgNCMHx8BTLMMR_c3CicGlRgzGvwo-eldvAIxqQ-4Nq86FsXgRDPafuWEsk3725B4fK971hzG4GpP63JNHThj7u8nPoMgoAku3QJGMOkJnf8GmSIkJwA_bH4U5KzvgfxqTtPBTdhkvKamm3sdv2ndj-AceENm0ABO9vZEji0ggD5oFB68vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pP12ewpOnB5_rla7rrtIyAcxrW54N-4aJl11MSCetDckGmAlVxTkk8EdJlXEeirnd4kLpRrPYLMUabydECOXpJ7StdoSzGmGYqbPRVoAMu1o270zvdU4yR1FNxz7JH46QcU97Xq4BLwyXR8JpzBVJH6tBPPsBK6Ncfsi7XlMu09pg8p3mQjjp-LUYutUJImotCUiav43Jjk5esQL1MwM8nsu90bJpfG-UUYvZPlkDbg28TuReJTGIPFx41vNHf-vjsvdABMMurdG2mDAdq-_B8BeT15Pd6gnHW3zZ8Dly9_fk8LeKLGdT9I6-rD-d0wblQ8V06G4SpHQ2h6TJKfVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzNBEuvuKFhvosmDZEZD_qHgdiES36oYGgbV82oIecEeS9rGiVpEnZ58AgmTh0hkIoPJmT8MoG45iHIbOkrQOKBPPytH9JaK8lxl6MeLThaq5fjFuDMPS-Ji9sedJP6L8kMJqctmUWORMOWwbatT-q5JCIL3l57lV0lzg6YrVSWAf6ywU_gTBApcXyiw2xJRY38gfhcb-iFdNJCQs_qkphRlLpgMrSon449xoL0WKlV4TWUho_ncX9rRuBl_21xvdWqGHyFxqKW1vBcQbv56LiTLIh_jDplKS7SxUshMfeO1pidEzy5cydQePF1spWz-bSTBZEjhdjkGMmzvFLzDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVaCn8_B6eGBkYH8BPxnJFaEvHvBL1LBTT8PVXBcc2K8k6e_1RzNQFCAI1tMpAyBmmtHC4ftfr7aC95OX8K8VUQZZw96H81e0TNwAVn0im5Ajoz89MBq1TsPDu9CZrorhGy1C4KAQzYy0aOPYg0OtGIYHbUk3d1EtlMWELEdIB6IZ1di4xjPawInmfP5PPfrYPzhO1er0bDVVToFPakfwQDdcixedPnTPMKWUU2pAeY6JJoyCe2_k67Gsrsl3nIIEQx0I5guJgvBDn7K_hpY34gm7dvJqj-Bx-e5zYHmGGKEPpJZ_ZwiiAhiuQvrklgyOFOJYZyzfjPRxYh8pW-JQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqJOreUW6ibq7AZpMnn0cF8GdO_vldcp3NwWuPdjsPsww2b9uQipISzCt4UdHKN4OKS4rkh6w1FVerrdK9acndTOR3KYgH06YN26EPie9Eh2EHZfqG3mUG2EI4qnXzDGTs1kBT4S1eF__Kfi9NPLYn6-AcgXiU3VY-QYWi-a6Cd-uLoEpqsdXrY9UclTwLm6ksOev59RL3ZAJst-50AwqicrLZhaQUIpkP1qdpZjkdFV8edHb58GF6JK7EPczeYod4_IFVFo6zW-D-Y3rRyilz0eW0w0uWzAqN0hV5SXJa8uMj-fxB5OzRNQbFakxOp83oHJWx1hlhtfXj92vv-yFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhBrEdqAhaGll_rZ-oWCnxWc-AtQE9sLJ6CaRbYwnZEM_WD6Xa_5rTWZlhtTnmT3hrjQb1pBI7E4OP3fnyeuk-d2-HB-XR3jioy7Kvg4B6hBvmA-FB_ZPiB7FCMlSm3GbRFBj533HDZacVVsDH5AVHhcABRzQMq9uP8zyM2ihQVVbFUL182B_oKP8swqxUUEOttJiWKH8ZwPs_mb-673cZLWpgPpsNcnljDa23lQZAUsqeh1foL-a8fv3wzvBkBq5DH7NllCg_-ut1ekEZ4FAIrBU4VfAjSeppIb3JFGHGSKLhl6oqjmv3PN0nJj4H9oPvb7gObay3xsiQCL641s1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_7ogBuVhAg6QKtQyFfZAS6zOOW0KPMuDBPgrBM6N5y9S3WsnvfQUFXOjeQtT38YMg7i9G5s_9_FMgGUfzI6gbJl8ssPCGvIMY4KM-kqDFSB0YkfHUtHlEfJC5yfi-pKp4uY3uAgX2OgyoFljamp97P9zcdxAX3nrz4lI_pLLsmNfYzjJ866uSC1FTCSgNNFkrqKvS16up4MA4DZKUAzDCRZm_9MuiPgX9BKcZRdrKl5obAQ5h1std9HziYU8GRGelivzRI9dRf_wc7CfvZGmTzMr8Taxcnz80HmgBz-R3IxJJzvKEav1CK03Z-cuRBrSrwzbGznM7ny_XzaQGw7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8hTE4r9KzVcI9DCJP659drVV9DWAIJYwiGJOuVyP7jc4m73KqOS7PUpV4CJxZzZ3Tj9ImlteXIE_oEMMPEGBFXn4GBlFHzd4084YablBEFQa-UxFVld50jHAFZ5nqkQXzfF8QUP_CcKmXIK7woUpCzAsAHEzg6iZ6cK33okvMFFREgdEDyo4q26Yyfu8CWm3rwJ-c_ONvcnbHN9IsJ8jCSyNmp6b0wHP4VTU-7aP6pUm9miHT1llov3N9-8wZSP82WpPLD0GsdCfUepBwAjoM1AIf0jlgF0DugfX51B4jfphQAKil5euOsrenM1MJ_brPfSNoGC1KoIZDAaHNB3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=hyEG1Y_XA6XwYzTZQB4pTsB_fTAoeRsrRCUJsyOC5d7neEU4Gw3w-kRXkMg9HQsrFlEip3fI8Xk5cVgf7-qptm00DrbrvUgeCJYJrgLyb6gdBDTvSBcFL405r-9PDwlBjJ-DjuSo3ebCGKM7835pOdEHUWH9DjafC-N5uVPNktP1U2MlQZFcCDrR_Memlm-FnJq9VZmpYlNt1-KHgGlYeDzZNsSDtGo4pZELyVEoIMGou2VH68PE-VKMFih5nu2phqmbbB2cthFbgoP3gCohTOFbDBWBTAIR7nJjHfUZuBws0eJ679Pqh1oE6lJnjlSrvxuKcgARbJDx5kpm3NBGtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=hyEG1Y_XA6XwYzTZQB4pTsB_fTAoeRsrRCUJsyOC5d7neEU4Gw3w-kRXkMg9HQsrFlEip3fI8Xk5cVgf7-qptm00DrbrvUgeCJYJrgLyb6gdBDTvSBcFL405r-9PDwlBjJ-DjuSo3ebCGKM7835pOdEHUWH9DjafC-N5uVPNktP1U2MlQZFcCDrR_Memlm-FnJq9VZmpYlNt1-KHgGlYeDzZNsSDtGo4pZELyVEoIMGou2VH68PE-VKMFih5nu2phqmbbB2cthFbgoP3gCohTOFbDBWBTAIR7nJjHfUZuBws0eJ679Pqh1oE6lJnjlSrvxuKcgARbJDx5kpm3NBGtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Ac7rlIdXELKkbnuaOWf-6kvjN9VYeK7n4Nk1mh6NgKnDOea5EanRunbbW99qKSQM1bZOlw9BeUhkh_NgMUsMXUCRcpsWaJ-TaHiUOiEh0i-MsQv2RP3VT1ICVhWPUmFHcrnWi9GCbo58YWzc1nFOxTb245hW_b05YyDIh5DRB5G8Psffk8atU8RYBX3-HSIDwBTF8bJX2J52TwwWQz81C4M8w8AUYmlLDe6LHaLRmoTgFRlcj9WCi2Gd5TMNmM8O2m2n_i3F18QsMT_i6iR86t6_uWCEDiK9I5_z9MEoHMqB4i04TwrVv3R_-tC_ntt3O4CVl6647xIL5HAEQC_vbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Ac7rlIdXELKkbnuaOWf-6kvjN9VYeK7n4Nk1mh6NgKnDOea5EanRunbbW99qKSQM1bZOlw9BeUhkh_NgMUsMXUCRcpsWaJ-TaHiUOiEh0i-MsQv2RP3VT1ICVhWPUmFHcrnWi9GCbo58YWzc1nFOxTb245hW_b05YyDIh5DRB5G8Psffk8atU8RYBX3-HSIDwBTF8bJX2J52TwwWQz81C4M8w8AUYmlLDe6LHaLRmoTgFRlcj9WCi2Gd5TMNmM8O2m2n_i3F18QsMT_i6iR86t6_uWCEDiK9I5_z9MEoHMqB4i04TwrVv3R_-tC_ntt3O4CVl6647xIL5HAEQC_vbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=QrOH3dhcKK18RKrUtAnmQTDAVlSYpXmrPs5MJuCz0C_ucTmTTtURj_NW5eX0DJf0YH8l5XmB30vBnfXjdPNOWuMGSvyT9eFwyfEjhkwj5A43lJbmjil4EknKt43rj4c8OubZ7xutVvBWn5dWD5Ue30-siNvUXYKrr1j8UihJjP87cJdS_bqWpKvmwmj-bl05wMPdNTW97N0I9tpvv5K89WCN9_xtES6Z8D5aNyNoB2ubjI7kP3coP3q0rMTAkYqE6fzMqa7lpHUuXC_AswLskvCQSAm3rs4DRSuMvyRZbb2SCSWn5zbeYZ3Nc9g3wR6qZhyZ4_qYh25O1NtBHGyKI0WdXIU9Wig-i1YI6aQfB4DREJ8PYDcc-jcOUJcNDZJVgotIp0daj0cJJFrFRgAgARxpOTVbh6YOzL7B7RbBONYZ9hnoBPrhrzdhDaTMBoWqJQ68RI1c2QkGJf-yolwEeMlcPBVoM41I0JYKpJonKrn-IevUG5wDFYL41jsYcMXv-bdgzP7vDt59vis81I1Qtz5v4VPhLTFZrziYj0p1ywRH9aAcYiNyrFWJjxXKWrlDnNn9Lxrc9RM1Ne9iwpCPiZXPkPXc-qV-OrDvk22oWqIXkp-oG5OtNay7QYHAtqFGGjqgWtnrCzZFlQ4MlnMvz-F0J9uKK0Xt12axDzj6Sd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=QrOH3dhcKK18RKrUtAnmQTDAVlSYpXmrPs5MJuCz0C_ucTmTTtURj_NW5eX0DJf0YH8l5XmB30vBnfXjdPNOWuMGSvyT9eFwyfEjhkwj5A43lJbmjil4EknKt43rj4c8OubZ7xutVvBWn5dWD5Ue30-siNvUXYKrr1j8UihJjP87cJdS_bqWpKvmwmj-bl05wMPdNTW97N0I9tpvv5K89WCN9_xtES6Z8D5aNyNoB2ubjI7kP3coP3q0rMTAkYqE6fzMqa7lpHUuXC_AswLskvCQSAm3rs4DRSuMvyRZbb2SCSWn5zbeYZ3Nc9g3wR6qZhyZ4_qYh25O1NtBHGyKI0WdXIU9Wig-i1YI6aQfB4DREJ8PYDcc-jcOUJcNDZJVgotIp0daj0cJJFrFRgAgARxpOTVbh6YOzL7B7RbBONYZ9hnoBPrhrzdhDaTMBoWqJQ68RI1c2QkGJf-yolwEeMlcPBVoM41I0JYKpJonKrn-IevUG5wDFYL41jsYcMXv-bdgzP7vDt59vis81I1Qtz5v4VPhLTFZrziYj0p1ywRH9aAcYiNyrFWJjxXKWrlDnNn9Lxrc9RM1Ne9iwpCPiZXPkPXc-qV-OrDvk22oWqIXkp-oG5OtNay7QYHAtqFGGjqgWtnrCzZFlQ4MlnMvz-F0J9uKK0Xt12axDzj6Sd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M22af2yMDK1o-1AgtJK16KYRmis7zojR3zT7E5AXEC61YuFEsP-VVGZYXKh54vVBMG2igolGrqXepY8RXwh9wy4IWelHxHKFMsPOEmN7YnCKiNbBWMvS7YsMiQKCsniFLtKSrXEKmJvuE55Ns_cZSqG01WtlHG_4IIilb30JL94PEnVZChIUZvlll11GplnvdmOTr6SgCt5bsE6m9iSHYHTsPTqAkAFpRyY7mWb6cy_fXhl24ETlnRIAIVH1XZ4XTYIaZPZm6eXd_1h-SWi_lX4X1kjkSGbIIsKvmq3kJh_rhzRd8Bh2iYZ9Fg0BFY-RJgfS1210fDgMIwXR0HUUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=vRC6I4haM6iaaRGrmzHPLZ5iBoHxBaDzZNraqV4TBnjfzEqu0c-Ks6_g-3oK41kVmpgydOlaBIY-25M5xebcTtWf6fma6RZmbjleQ650Xntils_bX1vZZt02_KfHArIP0NJSrNKu4rTP1WcFFLmucgVNa9lgABYfV34cvY6WyOrUxacgd8CTr6Yd8N_8SlfeF1v3fPCtrm6w-Xpg9dgYylatMdwv6WL-qsohdZC6wEQ6PJD3U9p447QAilQtPFeW2_Ril6z1UxbF_VDt9XGBgqusHqwRcBJT__ooY3hvRFzEEww5Ut0UEf0w4BiyXRGF1WmNApEeRFT7-xOp5ti1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=vRC6I4haM6iaaRGrmzHPLZ5iBoHxBaDzZNraqV4TBnjfzEqu0c-Ks6_g-3oK41kVmpgydOlaBIY-25M5xebcTtWf6fma6RZmbjleQ650Xntils_bX1vZZt02_KfHArIP0NJSrNKu4rTP1WcFFLmucgVNa9lgABYfV34cvY6WyOrUxacgd8CTr6Yd8N_8SlfeF1v3fPCtrm6w-Xpg9dgYylatMdwv6WL-qsohdZC6wEQ6PJD3U9p447QAilQtPFeW2_Ril6z1UxbF_VDt9XGBgqusHqwRcBJT__ooY3hvRFzEEww5Ut0UEf0w4BiyXRGF1WmNApEeRFT7-xOp5ti1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2x5H9pcwKQic-kvRAbA2PKjQu1ip3FAxpur7Jxp2IeLAzC6DNMnaP90ZGizmx-vPCJKF8D5ryu0yLfAI_Xhgx4wj5yx5ZoDJeabN3Bf6b6h8VLbtZzFo7aytRSs4N91otrqCiuIz4rJ8Ss2GeX6AmGCiUNaQiXia-tHDzbn2Q06K2V93cVeDr7NPo9E8zrYxOPJ0bafVgcchlo0Yr3jb9949tI531AzGr2WPtg4D2c66Ps905o9WvkHTfvra6WIM8v1EwqiZbXujND9_XUgUEY4xYO1j-t9cBlksKyLHODlhw2B3vS5UghU8DysHQVmRWjsWMab7R2NCul068zLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKAJdU9NYOFwt65u8kEv-mqPa5Co0s0mDNs_IVuEQy3VQih_OWq65HQ-hBlpjHJYRH8vTtOyvyEqdEJ83lduUbAo60_XpEHO-Cxc6yU43LhxYUJ8QLds2XSc8QPAMvUjaswPdHViBPo5jnflZe9XCoLJb6qLB3FxmComoT2j0lXsusEXkHdFiTd12KHE-djJXDdjnvySQoE6Vay24-uOow6_xnXw4YyvXbOCEhi3VWDjizvKWSQ15qXGguF0NrCvQy9lPDPG7tiiFMFMs78p3YK0gJdJ1kUE7t9pDtWhJyplgdXSNQDf58Ik-ag4FtpcbJfDzkQ04ydAM7WK5fMNMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lsb7z4PRv3LTZiyVSYEmCs6ckD09kNu21AkUPUVgc0Ee_8sk5jYZJijsZapz71DlRXgaG8vGYtlJbVpk-OPxjtYiyRm3oquvs_3ZV_iX6TgVhjRXGIcZND9XWKj6OHS5n3AuOEeAnIbpQukYqeCM_sOQnJHkhAasNm-uSRNGgaAJK3VhcQTB0jAuWyc272v-kCoDS2sEDBNx3NuHDi34oxsfB3TmNJA5YWZ1P201FUc-3j9mqr2_RenlU4QwLM8bMfU2oO3iiPws0_4tCc__RV6ARAfi-d7fhCKf3FgmeVFnj2cWVUC9iF58QxAhdXBiN_EXbl6cOcj32tsvzwkkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWgbKs2NIUAzAZVPCdW84ubiysevigDs3oKbQICQHSyzh4RE-mTb2VEc_TS4ftfaafg27Dlg6QCL-m-sczdHpGBkXfONClZBKBoWSYx77WNVt5YBiKrCnwPtrIgIZEawRdj31JBv0ewm4Zbq7D9ediKVvU54HlkPqJDGMh9Q7iUCUIh-nbGspHQODc8hEaalz07C1MuQFkwg2mq3iZaLY07j9n4dlymUGZ4S5IkkBYkpk9rYRosIg48oOx9nH5vRW3XZBi_0OLpgnwlNomXL0-v_bfi5e9Q-jQ54NCFfcVR1EJt2zbuEs2CT_a1NS8Bfdbgm2ju00XEt0oV60SWrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vX2_7H7Te9qV9gc8hRKW7Ju7EqDNwxWEE879ghb3R-jPtlT8vZp65mMETIh5lVxU1--6HCd6zVROi9NqZDh0JZHsjmMHByHK9biDz5wuztTyusWaUee_nzD9VMjIdxeYx7MwqDFRiFt8EV8ZGg1yRBZw5Ap1g2bqhCJeZclCAyiK6DtdPVGFTcHab5x0TAn8Ko0eo8MkFEQ2CO5PjmqJJvv2os4D5DKm8GgSIcTBLp0f_ATHyJeXVKn8acPAOPaQnv1l2yQWx2K0_HmOmVgsHX4YJxHeL_bPNw3URnDpEeOk5U2QyxEZRWBHV63pp0y4K_o9YUP3aZ9uEYo03OxzOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9IQghdAK9v5po7XBzyxG5l_AjDurXnug-asAEVxyEKZZK82qBo6F7JxuIenZWsXUQZKIBkJwZ3MeIy3wmfBhDYcSsVhmS5lYA9JPzXPzFx0lrceQOHXy8NlK51Qq9UrBr4bFM1lq5zj24L4g657OpgjVDMLd3khwT-OONVb786nzng3bIWtvE6th0GP42TzrrMkdrWw7I4QIwFgKKi3qJ2BDssjCu_ha2xKjv6Y3K3U2h4idbzITN-GAFDX1qDvf9_V5xfoqkHx1fxLUefgcRiT2PexLQ4S8KZPusxiSc6nxS3caW9l4DnYNCNW6XoP680yMPKIGqxlzzfmW4YMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1Rt5MsBgHuXV-Q8EVWZxhvWsrAW1zo45Jb-SznACb-VI5JakBQ3avD_CReY1sMbqnUnPf97UHPlzyAj06C6sCgXruGc-L5s5Xxu70WOMTMrwxTBsFHT1QmzS3bleY2tDdiR0c3WRJIZrMFKt4JgWw956PHWve6-Pb3umjQRRjeuyBux8vsc30DbZZyxYi41cdxstS2tr79IdhURgojxfWcA_Y-gZYOeguCQUDm4cjg8ZHrv5fiTWpQjXjLE0Rv6rfZKCCYXQvUPqceCBpQs24_8WQZYJMKD_v1rwKATZ0wT0Byk_aFxjk4f2hbCNkMbYIOqfpu1OgXAQSVsI8II0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etbU2u6yfy1MAEnzy33olqxNKhkeU0W1L041TGvoBtSFJ6TrpY-g8guTdUkASIzNflaDUQOjrKgSvd0WbDswqO4S4H3xMzinNwv2j6WbBjpwV78mG3JhB8jGdNzZHUGcMNmvkYZqcJKt846Rh4DJOBSnga-h1sOMzUFSx9RfmdqHB5TxgdL83TnXA9Og8MM0hw_KucuMBsYAfONcGn-YHFfDiReSGmaAL7oS5HpI-2kX58bgft5Ypj_XOHquSnmAAYTZlO_rWc0NCiSPKFJbQ9Jxs8AhqYd6SHI1CX_wmgZ8ZMVT105H5dfxo4WJSzJ1qg_TShR02Q8V9L7M1cKuRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Svml4KfYBSJOslkIFan-OIUqlmzmgzaQiNIam6ep-YQsjsTp6r14C15h0XrM_DJhVCK48ls6EVwcUlaf6WjIvuVNgSDqMboGmhLwXOzoJnSUQFdKk8gxPTRejJu1trBmGdglLANzuVcTJxCSMH2J85LrHbaa2Ffuy8tCR41yrIzjV8p35MQfyVIFobuefBW70cFyEHdgGbZa9U87aPMYwvnfyVPIDAbcWO4npR2eEKH5z_iJtdrbar0pJboPkS04vTMGIsbEgcde2p--R1i127Nm_N6CkhpSDzd4-F-jZoRcumC1xs01kkaJYFQ97IdZ89W8dsBk_VD6LzYEmo_dog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8p6NeK7goQxA51Gv2xc-3NYMiE2udr-l3csasFjN8JFnWXhTHnS-zOVvO6NHyVpRrm9YiB07WXuj-3ogHTsG3UIzk0CHEjz9KT-3dy7fRWIGMSk331E4gSC0Gniyt29T14tXIhsrH4PREEpSkMLsd1wrdaMadtEtS-_ly88ec435GGX2JXN2PSDlQIyrgLP74v7vuw6JQG5hsF-j-2BB5pj03EEzVQ3s8aokYUfBNJ6lTZUHTLTpSDPCBVBUpJeNW1j6iDIf4ewUVg8q-hbXM6KXsDnsX_FIr643IdwOFFDVHnZ-G6VFLJZX2wy-M29EqD4X8HCnw_gpn0-1UJHbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f74Dnuo2H3uszz5I0bmormNxLu_QYi7yVje-TEXFuwGGs3Mm0aM8NQ4rwjLRqLWAPwOumz14BRwB1cYiUUANFKLLbog0uLS6Qe7_B2NICjrSIh3E3QUQbTP5kzxRvDnin-Fkn09m6MqV2rIqPDf5BJ_BIv7lVciUP4DqwL8t0dBVdMgGXy6UjkYOa7fEQIlosZ-NZAq2j7u3FmqinxzhUuk-emynn1ECIUpMV1kINavMBUyJCQYVmbL0XBeHuo2Lu-A_3kkFOlzV_Ru7-YWJ_VHE2v16TnA11nre8RoEJifb0Y1aG_CPC5SAibgKXI9QJNoSv5hxYrEhQysHcTikQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3hnPbjGYiuJuphNEIhqCO6GlmC6cc-r-s8JKReI21y5kTbjv8KdRcnwxghRKdmcam63CoYBcQIcST6r3JmG370XqZSqaX16EF7DiOyYCWyBlo7fLIxIJ9oY3wB9Ei-WyiLamubPnIgRg2KJ2yDnmsQDaXYdiS8uSumG_V69PtjiCVQWx3CjTx61WHklVOimEC-sWNrq3mbo92hjZPRB21Q5Amh8rApHt9HLyu0H_hCc0Ow2iYV4CAt7Zte0aapQD5_ecNDsjNxE1DVZ16S7uHTpv-4uhVGZTEJ8S6345WjrbpY--eseQViJ-zyhK6E90MZYl6gTMDp3J-8o79Frrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENlyYo7brBCs_BRBlA-KFYKpa4szmZznU5LniFNGr6DKNst6V5m6mQNv4lKRunmaRYDoduPI-mQumz-nEg-No42amiML8ZPtN2kZLnZfxzU0znb3ia_cn8_Kd9ml5RF84SsHxyjK2eb-PAmOxC4IhlwnhAStqtpjZWb9X-aDz5k4YtDZfR7X5TBJ1znzF8w14P6I4GuJPZXca2M50XIkh1NSJ1TslvXZWHMuHwl3SYPBoB_yh_RP6ZV44iJbROzpI_VKGFT5TAEn1dfKNa_3wDNUYwPIqtNnBlzYFVQnH0PQvu4KqPcKGRLMy-yhJVqffzZnk-2h6fUST_akT15YXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W49gKPvhZa6hIWZFyY51YGLHHNqB9p7iEH0OBaGlKL_ME_oQNekkWPIvZcwX4T0anr68niLc4QVGVANtBe5SUadMJvpjaILJn8vOPmIFC-pIWFgZKYW_YKo6BykmdK15DJx-Ute7KCqNsxf8tVFT6WE9gznPFyuz1-s7Gnru1r7o0gFjOFUeSzR3HJXPUSj5q4Qt-fQ-EYyKJUnqFobTzGZMSOARp7yN_OH-D_gigyeRDE01eOlbEL8EOqEwt9q6cT1oJObYa1YOXWWcumqCtqh67Ji2muOfXtm8U3o7BTZQN95DVvP-rpRDJOfZnAuqRhtX2gKAQqXbTSDNKazuMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xwg3TH1Dp-mkpsBoQd8UJJGXog41HP_t6eGbI7Ue0TB_atyGkf48rhEjRKUmneCLq43XQ4NkD_Rp_x7IMoJ3CQfj_kdq1vKNUS1fnyuxGVTj6ltCZl5ArRrKIfb0VLCRE2S714xd47TJd-pJFMu1VFGN-Eo1Uxr_Dxvx_pZsIO4Un9CoppOwsRQJQexHjxhq_5Jat7pG-QKEYB2nVgVDYcRxB2juz3YD4s5z1PSJt8_Dgv75mcDM_IiT72Ip4t2c-LBrW3bw3aDhyrl2qHauXi9vnyh8qz7ujIuc5NC7xvtgwlL4_eAKLZlQfhG1P3_om3mfqBfoEw4JOoaON3xISg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/coABVn47ijdzgpUfgrijwkc_F3XqdRnsj3ShygLt3KLoYbc-9ObkvDpyehIPtXVNU0VuAkOA3YLO2ExLkef3gArxGjJfKtNj8-MX_tuBF4BTfAGpwSIixjmtCIbgvUaPE2_EML4Jlgf_8wPR_SAIAL9i0e9BJJT4kpw-aO2fHvLoaQ58fSlEDHotJH0LfJ-xsNtm0LgWczrCFTe_eB5Hc7GI1jxfd2Hy_oQuQYXsLk5pyWdX3siMvjyUf7gpY4YbLzwWN5-roCgOX_pklS-L-QfSQ76hW-OuDkH_bGI9IwIj9UwFMFZa5I0bCfsNqOp2q0uGO-34xg0imhkwktZjHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYIJYqUkI0LE2jEUXkh39R5_asJpcNvbrekH8cGVb_-nyALZ_ixsHfu0IXcK3Ujpq_qtwMVDxr8EwotV1q7KF6cHVF_EzxkAw2MeLiSiAatu4Xb9jhsbVEJMefMzm6ZwuRYi2_mCa5UkmWholkpCwj-oQUcsQSXJAm3d9oi4CfG7nJMmr4WAcR-Wq4V06mdFQw3Ld7CJVt4tPszKjVzihpg3IOQZ6YLBvKSHejaPnPWt90yr259qq8pWONTPxyXqc3WVMJIyud-v9ia3byEymhgmoHYML-0t8kt5LSkpy5RZhRF4KvOvZ_yykNYoqZUFp57DOxctU4qwzRqqRBOStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=NQ2sbo56tlJSP99ds56C3immhAiEl62MwwEQcFWyELt6U2GpgC7-OnzDmgygK7gLs6_wjZcVngPlwMvrx5RtHb9zo_O3F3O3AdxVB2CvEKjpb5T3gvPNE7ft-QLOYIb5LuuiVL1QLBt8R_cMfp0AebPl3P0qWtPN5KGGkca-GcCNnMvDcsU8yHeutxn61d_1iANd01UtLpe5CeQEbSrNbmM3XuWM8lpyGNRWM41JiKMfJ3ssDj2waKHbiuRYcgwD0ZNXi1D2khJJwSO681uflyHKJHa3NQDD0CsnXoneNPL0gfARW1Mh3AnbAd5Hk-sqgGHTZUC7E7YuCibo3ZTDyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=NQ2sbo56tlJSP99ds56C3immhAiEl62MwwEQcFWyELt6U2GpgC7-OnzDmgygK7gLs6_wjZcVngPlwMvrx5RtHb9zo_O3F3O3AdxVB2CvEKjpb5T3gvPNE7ft-QLOYIb5LuuiVL1QLBt8R_cMfp0AebPl3P0qWtPN5KGGkca-GcCNnMvDcsU8yHeutxn61d_1iANd01UtLpe5CeQEbSrNbmM3XuWM8lpyGNRWM41JiKMfJ3ssDj2waKHbiuRYcgwD0ZNXi1D2khJJwSO681uflyHKJHa3NQDD0CsnXoneNPL0gfARW1Mh3AnbAd5Hk-sqgGHTZUC7E7YuCibo3ZTDyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb7ewXcKMBm77NLkxCOLv8PnHuDDjdb357Qr2LCV51r2gGxxhtYIM-uoepj96W2S2Rt_zWGkm37fIyfOO4rIsaicr44_VczyxjyDzNAUyqqzlaTcYy4w6GN3FQ-bSzz1Dyi_b_W5v_E9lXgE4TvUfK4YY_1JEpHssIYTf2yXLpV0G8n3dpnn2O80O3CPSyYGDXHg2OWV-57iLtNv8pFAM6-s1rOjSPa-b7jKh8OSRblQ32Y3kLLfMzHn5tbGNytdt1T-aOJUv_1nHwYRGbRSG4nqCawlGQLg-FPiOieKnZxR5oFPkKJZvk6txpvdr2-yqNO0r7briquxK2l4n88KfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXF7g1dRw5_PMBMuLW0rzP-RPZHGIg6fyv-YwBbh99UDXGpeLLxkvIoSNa6Y3FZk5qNmEJlZBAdD93LA3HrTxL5-gcESuFsGdiKYM4H3_bjf81ucVgjqMdNjV-VFWKSSFWv1a79iZRU7w56WRZG21jyE-NXH7kHhtXglKBvMOmFJBMhpdjJrUbSJB1rSXFNk1im-DLmCqvy2ShYvqi9gssAsp--i8KkF65WQe5CB0WT_ry9H6qQjpV-TeYtZKdZKBuaXJftcvV1keACdhOuY-nAtZCDUnZXJVLE7W18-DlJ2cfdVrhwY-PnvYxFwKqSV_1VKDV7MQNiiAANF5Uzr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMk-CnHlugheafsSXmT_VNonXFHwS9QTBYZeG6znyN-D2SuTncIpjGNch8VjDjoFL2nD7UkRPymEzMcy4INlubpm5cOljB5l8zGFOMD6trz840cbWVyegZ92Ao1ZS_ob0x6UihcxOjhvTDvJgAlpLqGB9V-04HR6t2YKT-WDhTn9RUtPD-Lxhtqs_CsZJMYL2Ede-M9wRbyzfeKcJcuxzIXuy50FR2bz-qZwNpdKd3GO5AH0LqLwhafjiF54snxRdU1mDmeY4dWYVbGAWKDrD7r6XL_0Do-XKngQ9xmVnc-LO-0pUatn9to1mPxRxDm7oz96yuwu-Kk8KadzeDQp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=bPUdnsycCP-SnSuugECFXqugx92X_Ka9BmBDi_uZRvQsPxHAINfUMCpDnt7qId89MyCptXRidBBJi_HGVlZmGmfOXLlo30g8Itc2Wer9payoNJGvwehz1Qm7DBF83OEAPP12G6k8b12oWbbgLS9_CnC530BpWYznQLlV0jAsZZYMeNXSf8Qd6x2qIcCO0phrg4vc0KFo30WY4EQ47-FbDEe89omSp0hOpRKPLT49VpGq4OuY4CPTXgcZgmFkxAUX-aadll6Vpaq6OTr92k1hI3tmF95RpfzBeQgJ2pc-IX1Chs571O9fTkfpn8Za0L0N5Zc9YsV1iBDmjo5Q8Se0Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=bPUdnsycCP-SnSuugECFXqugx92X_Ka9BmBDi_uZRvQsPxHAINfUMCpDnt7qId89MyCptXRidBBJi_HGVlZmGmfOXLlo30g8Itc2Wer9payoNJGvwehz1Qm7DBF83OEAPP12G6k8b12oWbbgLS9_CnC530BpWYznQLlV0jAsZZYMeNXSf8Qd6x2qIcCO0phrg4vc0KFo30WY4EQ47-FbDEe89omSp0hOpRKPLT49VpGq4OuY4CPTXgcZgmFkxAUX-aadll6Vpaq6OTr92k1hI3tmF95RpfzBeQgJ2pc-IX1Chs571O9fTkfpn8Za0L0N5Zc9YsV1iBDmjo5Q8Se0Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDFzmyICRazW4I39rZh64AGt1ByIsYMahn-IgeUomvooBEoQSLMrmaFg1sierJKkPlnPY7di4GU5VqGoIkaN7pLuITV8KcO90KkY0PeaGndSwQgoyNpP4QuB7SLFEvdStLEV2u35ueA0rN6AaJNci9NPw4N0MzfQ4cIsODLm8JktPTZHTtR8bgQPLCObe1M3k_t0uucKBxI1dspdeiE3Iv2WHVcdwT3FTXyTNLmqbpBaiW17HVBxRPQZOCZ7WxONiWVx5b4bqk-qmsxICk27UYUKd8g9Spx5K9hcYe1VoMGdoPinEEUY_lmy3hk1D1Nj4ioIlmPvtDNol2CHB2tUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Y48ggR4MMC1ztXiCCnwxpEM6Y3N3ibXKfnhM0Q58O8VnsVK08GM69b4-o6PZegrAr_CEQSFyXXQzAQaHwtcRItbJEPa1IeDNtaQsyhKriLL56vHplcgKMe447jVxgHR4smuIfkYC6jYTR2FMdkF3dAV7KMpg2LX0AINDTgLuLNXNpnpjYbU6zzxNidJWcAH5CylGKpQCyFnkgjQyGsdsgHIwH9lWvVYXu7YIjvXvAlQHlbkD-pn-YQJElLsa_p5TfC4-pTt_6ZuIGZuqI9VTv_xj3k_QBxZvpjRwBTDH99AMhQTDK5U40h3BlxfwK5yOa3UCUOcZGwNsdSJOIf_8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Y48ggR4MMC1ztXiCCnwxpEM6Y3N3ibXKfnhM0Q58O8VnsVK08GM69b4-o6PZegrAr_CEQSFyXXQzAQaHwtcRItbJEPa1IeDNtaQsyhKriLL56vHplcgKMe447jVxgHR4smuIfkYC6jYTR2FMdkF3dAV7KMpg2LX0AINDTgLuLNXNpnpjYbU6zzxNidJWcAH5CylGKpQCyFnkgjQyGsdsgHIwH9lWvVYXu7YIjvXvAlQHlbkD-pn-YQJElLsa_p5TfC4-pTt_6ZuIGZuqI9VTv_xj3k_QBxZvpjRwBTDH99AMhQTDK5U40h3BlxfwK5yOa3UCUOcZGwNsdSJOIf_8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa4RKXeT29Xp1d4AXUki5WMiOmgDrky4TxWNnt4seCVAIHWlXN3sv6dhXaf8y-OiZtl4tiheufOg5jMndSUyyvCs2ohRFK3E9JWh8_Eckm5Po9-_vQ2v5NKqb9So8agCaN1TyaFQ2KKQP9Uh54NOs1mmFYv967NBGbp3I6GswONObHHEe5AImNgK6WoBR-T3PwC0K1ayUySMqnQdRu6zrRNnOYu7qGXtkFlsPvRUBYHBMO2PJbv6ze-iH33b7yiQQDGLqUTU-Vjtkmg8oXkuURNV9B_o0ahNPt8hTJbvdlFEo_r4dMZsGk4Zy9DVi2Y7mhvtUkgEL2YaryBoKhGzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vo2eo6arAxRPj1vGwmTH5l3yC1rxcli_5Y1vrcNYpWWA9HIzzn7ZGh8qQzxJleG5_8gtxy9w6hhceF7EiOXc62epNjtAYXRy0ASk_HMae-LEEBiwI3gFVEYOGDcS9ORM2NTi2U3JXvKbh1ZTkJY6Es2MCwjgqE8gtM-uSHKwS5j48xs2daitEvDnkLjb0byuwM529YiRptmp56f0Q5toyHcRijMQ7KfEJV4cn_NSztQSaJs8WsRuDtVzZk4Jj69qbZxo5Wv7V8kq1iAHfPxtscxCVhbZd5JOhJxtc0mDg-_vUpeeXVrw79rN8QuIzRjyk_RCxaen5ZczxsOjvKtzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=NPtvZlF_rlRThpXXpOF3LFMMhQQ6pzxFvK1x9TFUikvYOfWlMxtserzDvESS-xODaaRZHgI7OV2x9R6s5YvaAwjDz3CdJRAX0E-XfAHfQEIpXm3imTF7QMfmDvHMY38XBy_RLMVYOYM_HFXaXeVIvZav5-TrW5M9lzOGVLcmruTYzDBmOBj5meB3lmn3Gob3AkeEM2d0oLZHLdEnwofPkJgCm9boNtngEPoCi9_e6l49F4U_yiKtlM1AYO3osHt1MJ6jB0Aosl34P0nk23Rgs82fgAxpN3wjRBK_uLopK3wDEyTahFV5c_4KD3wifPJfVVG9oxIw1CM_CLvvvH8NuahlwbpPCpTCcVhm93h3Oll7JCPI50FIwCsJZvR05mhUvegBaHg9TcihZG6zlmUZwuFjyasv0f5HIbyIjlX1xgqEsqUAEa_5zWZxgZ1vWG_ebh7vPLXu41ov-W90vhQqnSXcAtYjP4H35mAXj0OxXsPqV3F65-j2IrpmybnM1UZnmmhNxJ58bCW-M5jmDEfmY2Wx5cu7ianoh2vxRVfV-0-UiOMTSBrmw_5HygfgFlHQ08J2AQPbP4hGRibcDB_c0QKmrwDiwwRiPDdqnXPDd3bg34sIC4QOVpkGqKeDkzASAid-azXHiGNnLPGqLvzk_6Rw3OKXocpL2IFNovZ1koU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=NPtvZlF_rlRThpXXpOF3LFMMhQQ6pzxFvK1x9TFUikvYOfWlMxtserzDvESS-xODaaRZHgI7OV2x9R6s5YvaAwjDz3CdJRAX0E-XfAHfQEIpXm3imTF7QMfmDvHMY38XBy_RLMVYOYM_HFXaXeVIvZav5-TrW5M9lzOGVLcmruTYzDBmOBj5meB3lmn3Gob3AkeEM2d0oLZHLdEnwofPkJgCm9boNtngEPoCi9_e6l49F4U_yiKtlM1AYO3osHt1MJ6jB0Aosl34P0nk23Rgs82fgAxpN3wjRBK_uLopK3wDEyTahFV5c_4KD3wifPJfVVG9oxIw1CM_CLvvvH8NuahlwbpPCpTCcVhm93h3Oll7JCPI50FIwCsJZvR05mhUvegBaHg9TcihZG6zlmUZwuFjyasv0f5HIbyIjlX1xgqEsqUAEa_5zWZxgZ1vWG_ebh7vPLXu41ov-W90vhQqnSXcAtYjP4H35mAXj0OxXsPqV3F65-j2IrpmybnM1UZnmmhNxJ58bCW-M5jmDEfmY2Wx5cu7ianoh2vxRVfV-0-UiOMTSBrmw_5HygfgFlHQ08J2AQPbP4hGRibcDB_c0QKmrwDiwwRiPDdqnXPDd3bg34sIC4QOVpkGqKeDkzASAid-azXHiGNnLPGqLvzk_6Rw3OKXocpL2IFNovZ1koU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ZXGHJeFyQxanfqCs49GQe1jVCFy3L7u8TjqjQeGesESPCwkyZeKaRywtYq6qp047NloZdzMf8cC2CrQ4VJi7QvC7AHxql584ohD9Jcn3yCbCsf57zadTwnLbvh-NAVAWyK7dSyha5uHycudyb6SnzzqnbZjviWwQEGzYvbOCOMxvIUgRzWq61gwcHF31oHDN3InzhwAI9YTnqVUt1mUGY-0r4hdi8OjJShZGwPR_yuHJ0rqycVhxSRr5CLp6HvEagG6Q6BpxqvRcbEDEsrf4kRAA41xIAB4wMoEsIOil2oGnDBKbo091fS6eX-DPFX3AhycMDkfDF0D_cxMeyqJWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ZXGHJeFyQxanfqCs49GQe1jVCFy3L7u8TjqjQeGesESPCwkyZeKaRywtYq6qp047NloZdzMf8cC2CrQ4VJi7QvC7AHxql584ohD9Jcn3yCbCsf57zadTwnLbvh-NAVAWyK7dSyha5uHycudyb6SnzzqnbZjviWwQEGzYvbOCOMxvIUgRzWq61gwcHF31oHDN3InzhwAI9YTnqVUt1mUGY-0r4hdi8OjJShZGwPR_yuHJ0rqycVhxSRr5CLp6HvEagG6Q6BpxqvRcbEDEsrf4kRAA41xIAB4wMoEsIOil2oGnDBKbo091fS6eX-DPFX3AhycMDkfDF0D_cxMeyqJWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9fgDhRymVNlY1H2dEIdz-VdsBxaWWFCgSUF3VF1Kq-QOgsYouPwwcbYracLDOFycqaLte_wTc10gGVMk-l_O5TB7nH_68Ftl57BADiNUdygxJ_5alTp93BFQD9qtG3MC3NnIH5YA2SOGIvNWNGWPQY85y-VK5LnpLPoxB1HX2Y2qSdLANOk6yiSH9cDrnBqBGHFKObQp34Z5UZO7hT7jppP6eUUfgCo_Auhu-7uH-JA_lhnic6xcl4BOx3eS8iNb5MV3xCFjnW4YdLkTSt6c5H-xGtjG2j38FHrDq2xmlNJJz76fcg4vUkkACNCL7DhJokGATl6k4rDhIiMiYZXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=teAvyS1FLsIfdC_ndx_byUxwPw13Y6kAgt7UFDxcZModzSB5WUzag3vLbZbY589lKwUUmc19iZb_grXnlkpaSrXSb2qNDWzH_QbxNF0V6KgIc13wSJNf4seBKe1AeuBAiJy0IzqQd-Fn16Jk1RJEGv1OTgF5O1ainrhIqzyD3klo3MquDjIWxgpxxuYmbHFoti4cHzRKANfjM-XrmfW8QhAa-76qEDocEbLZjvB5AGb1NTQJ_x76wowsos07FzN-aLFGXKY8AqnWmVld8Plg1PcqS2NOTcCk1U6JNoZ5myWC4A40N576bpYebmXrrh7mET0YSfnRafy3zVPt70AB8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=teAvyS1FLsIfdC_ndx_byUxwPw13Y6kAgt7UFDxcZModzSB5WUzag3vLbZbY589lKwUUmc19iZb_grXnlkpaSrXSb2qNDWzH_QbxNF0V6KgIc13wSJNf4seBKe1AeuBAiJy0IzqQd-Fn16Jk1RJEGv1OTgF5O1ainrhIqzyD3klo3MquDjIWxgpxxuYmbHFoti4cHzRKANfjM-XrmfW8QhAa-76qEDocEbLZjvB5AGb1NTQJ_x76wowsos07FzN-aLFGXKY8AqnWmVld8Plg1PcqS2NOTcCk1U6JNoZ5myWC4A40N576bpYebmXrrh7mET0YSfnRafy3zVPt70AB8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzwr1s-myWmwE8PwQIFxHuF91aH8DgMZd5ZWN1uvpMJktrQMgDfI9czmhEpUrTi8SQiMpjkmmwjjeGDbV7I9sFoTNBT61c02D2wyXcilvDWFCEpbWc2LDFZKRg43E8ws4Ol2n7QoyK8q6TebN4YufvPPrdRHXuHsau84OOI9Eho7EaGqTlXgfz4e2rDkUcO4xwXy7davbjZ2pGlQaMm3IJNS_HQXc_IR7DjZIiB8BsQHq0WY5cewlfBRRdYBfXWElj9KtH3he5LYpDP4L9I5K4ylwgVkLxl5TSYYGazLvgQ2KydpGnlFxewrcmTaNsWSrnKQevIwLWWpCMDu96wJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj-8RnJVRKXXuyb1DrqPmi5XWwEOnNgb2w98rLAoRT_gZmn7tykzTqOBO8laJaLsYGynTxABD8WxPJPuZinTpwDhNPggK1VYSHgbyDn_7Us25JcgOx0anTEDpvKljNubs1--WfWvZ9Kn46NWQV_Nku_MyBmSXRTINIIBt1M3FAeNAyDiAzECNKJ_mltqYOkXQZsUsNlUds09TpAC4ecMFgQ395KKIQEHRuPuiRLptKU2fuo1if_6Q6bPUhPjacRd5xevKUrVy56ms_x-_4cFdVZseduhwZRuZGkc6Pg1OhDPKw-oHmton-vL4V_g8hfxvkKXnENgSuZ30z4Gl6iwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-bDx0LKOp_Uch1Qe7GIJiGOa-dH1s0fBa1fnj5aoziCeq4UytkoHqmF5AvgaCfWabNbKKxI3StJDxM6oSnDMW6ykf6ixyqfgD5tlZSG9-Cki6gAPm7f8xOES6Ww8UWZ64gXh4IN5s0xtHrn6JsRgDTOnCnsaMUpTKCfiig9XLlS4o2okc1HbxOWH_I9JIatt3N8gBJtsQPPD_vWZxGvxoOWyhIX8QLGudhNcKQNFHQ8dMCpBENXa1AWDBnKvy3KTN_lK7WqUGBDH7T6Cr7N1pnlhYmuNMxrBjfrYDeLDEKlXvYIpaHDWLNA1qNk6mzC5Bj4QCR50uLlFbjYiy0RQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbB-7blgqazB8U2HvqhiuxESIeddmdGjfkQXDO2ZI7aHW6vYtdNsbJE3rCf6T0o5JrocJHwgWSPss1xV_K5hqKvYWmMITH7g1aR547RElrvtc3bv-XnVlFdeeRz_f-U1syzLlmryc2kISAhXbNGdZc-HfKOjTisDYCruBe7vAfFoMrhA3Pw996KBzCelXwPhUpBoR4LgI-U13gskuBAzINNFfW_Oq5ScSVykwG5HG8TyX8EtOA9xhJotjUGLfRlHAMukeEutJRfr0bp0kguRppoDQVbH9jfxIvy3jpKETJ_-I3IpcroCCxZTKtpCk4Re2Y85HepRBgPqhnX46yAI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv6tTJIVmnZDZEXVUb60D_FtQJKh545E88IPWEFObWGFtuHMkRGpksoJ7mpuwDZRWdteWUO39fN2qRw78gJvNO-Qgtz6vnvw4vXAFP0O4aC_yfZ5RzxDz3RzvPniqUfkWS-2CITA-pSkAEdrjJEGD-PdMdGc3VEdkXzludOxjLOdtxelBhvyDyZo20K7OLO8m_tOWs_vqUzxEXogxOeATDnKULYJWlGGGIsBjM70VoZBA1XLBEPW65eh4tEQtw9meIKYycPQfEu8U2Z4B9SGf5ke-1eHQflz9t1D-uG0HVY3rpbC4h8lkNXTs9F7KkmWOVwLT6u6lB9ypNWGIv9Z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=ga6XoaCW7XPRM3UDy4ndsngjKclZSGAV2DefsJhqtr5-TLFQCZlqIzOMAnVXbJzfn2jdtCDu3sQ6lFn4B7yOYISykc75lkXEH2lsSyjStGgh1UrkIzjLaIbEcmRe32MKOtqCarQ3s-2pFkMBo-tedVbhqh6yDOIH143Kaa_c1DI3IGS4mTEaUA6UC8bmho-dmPGP_wS5xiyCra_xWz-qK7zTCpHQ-6f3h3Z3_uROYzmA5FnjCGANJm9eehcoelmOY_JkQ3G7Mb3reFfTVMBnSDxp2M0kKsAIwBfl1WssozMPD6P1v9jKwE91mtrixDhdJJT_OwkursgSpEe0fkHiUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=ga6XoaCW7XPRM3UDy4ndsngjKclZSGAV2DefsJhqtr5-TLFQCZlqIzOMAnVXbJzfn2jdtCDu3sQ6lFn4B7yOYISykc75lkXEH2lsSyjStGgh1UrkIzjLaIbEcmRe32MKOtqCarQ3s-2pFkMBo-tedVbhqh6yDOIH143Kaa_c1DI3IGS4mTEaUA6UC8bmho-dmPGP_wS5xiyCra_xWz-qK7zTCpHQ-6f3h3Z3_uROYzmA5FnjCGANJm9eehcoelmOY_JkQ3G7Mb3reFfTVMBnSDxp2M0kKsAIwBfl1WssozMPD6P1v9jKwE91mtrixDhdJJT_OwkursgSpEe0fkHiUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSf0y_xfs-Ls0rSTObK14xVgWzdmZ3lWwaMUDalkLxold601hUzAeIjY7vfwt-HW_qALAlkU27Qx7ncyCWS2V06PrzqEMzpJh_yKXfE-3HhGnqU2_NsyhsbcoUdCxGM7y5tNWBaZ8pZ8ey3DgFdkI6aceeY6jHcUBbeYtjTOUC2qAdoZbGzlbPJZD8uxK-P-Gc69P-JIlpAruREMOAHquQdivQmxa2pvlaKX49nt7-K_dUqJN2WBR3wH1vfCaMkANDOzZOjJ8C4NoEbJ3Z5T2ZPyGNWAx7d-8EsEUxV4TAButhwPMj8ocyPqB5wqqmBm2boRbcO4yYqsmCkIrpPAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuWxZ6x5Hge1OkA6ZAfRJbbkk1kzif1AO8vBUAcQKckgBsAN0aovmPES870KfhpPs36wIoSmstJ38HSsPolfjNMNNQ_hDXnrKOWMzS_2Hs_UMqU2r8W7M03nYuPYLfnuxMdqJCEtMZPHHWVrkx5qUu0eLTzsQGP63MvmmLoDqY5-mXyWu2cawgjBEdE_7f8isVSboIDmVq12FeMVlaNFjJwJCU-plbW-xVxTc-TddH_TVjY0grtQW4IIyU9fWp_pMW_QZgC3tmHOXSjGrAF_LBVlGaFrYEyAWfzJK8-8O2_sbGDKE7VfWM46Lmr2LhUtSR91R32BCG5iCRobCUNWXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=BaB64HyJ7Iy4wckYpEsB5a0JrzMBSwhMFn-6DMltOAtehFmPK4uKnEgLxbY6iEAERcN3hwPw_TiAK2vYSf5okHtbnsPxQBlycZAA14a1gbRKAmK6iftIPI1son_Ku_xoOho4_npcjKeNN1QVxFcgWDTJ8wWh5ZwMQLboHk9IYyfRntM6KLEHUPvusLwRc7MJD-rGHDVP3rNnSuOPaEbjrRpEuKBeUL5qobxCUS2k1juvmpeLgv3AVjigTKzHFYfQuKTJrYMhSTDomIXhzDnck77x0tFo3t87anT84YvLnNLlDQZZT-kBOQ-ug84uPUr1mTMITDOp8ozL3Vj8A_vG8aLdmLufDk4lC6TEw8Bbifmc7UQMbWA7604dH-JcAUfcJmDMMNrF0aH-0bxR7z4AvU0x76-6hXky3h46YhPFENyj_LdfhJQCJ7E_hK-13j-J8X1pC9qBqcxgy6BxmllUh4l7TEt14MbyfxKFcTAjx9HrFO4rUT2dqfohyfVSEAtDBjxw1-J9q9H6JJL-G_y7_7LBUD2iW779S8PCaGb4hzghxmJ4YPuHDt5Hx30N6SQR1jKD-S3iVCB1UatjllDwljy951GCNUDlVhutiTeAnDwesTHRZwB2ljV3ZrC-SMXFSDR07GNmhDL0qvJvEx3EJSE8WLJKELo8cFVRwP_RiGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=BaB64HyJ7Iy4wckYpEsB5a0JrzMBSwhMFn-6DMltOAtehFmPK4uKnEgLxbY6iEAERcN3hwPw_TiAK2vYSf5okHtbnsPxQBlycZAA14a1gbRKAmK6iftIPI1son_Ku_xoOho4_npcjKeNN1QVxFcgWDTJ8wWh5ZwMQLboHk9IYyfRntM6KLEHUPvusLwRc7MJD-rGHDVP3rNnSuOPaEbjrRpEuKBeUL5qobxCUS2k1juvmpeLgv3AVjigTKzHFYfQuKTJrYMhSTDomIXhzDnck77x0tFo3t87anT84YvLnNLlDQZZT-kBOQ-ug84uPUr1mTMITDOp8ozL3Vj8A_vG8aLdmLufDk4lC6TEw8Bbifmc7UQMbWA7604dH-JcAUfcJmDMMNrF0aH-0bxR7z4AvU0x76-6hXky3h46YhPFENyj_LdfhJQCJ7E_hK-13j-J8X1pC9qBqcxgy6BxmllUh4l7TEt14MbyfxKFcTAjx9HrFO4rUT2dqfohyfVSEAtDBjxw1-J9q9H6JJL-G_y7_7LBUD2iW779S8PCaGb4hzghxmJ4YPuHDt5Hx30N6SQR1jKD-S3iVCB1UatjllDwljy951GCNUDlVhutiTeAnDwesTHRZwB2ljV3ZrC-SMXFSDR07GNmhDL0qvJvEx3EJSE8WLJKELo8cFVRwP_RiGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=fvvyPpvTySC2GQWgiuP8YORIyUpa016EVdSYrBB5XhaRfcoCXIdiQ1FgMqxPc83UDzKoETU3M4QuQbvkzL1oEGDs780SkxzFxWcs9z1oNOaNmJu-Mzj8AYMhAArwGNwouxS7EcG7pt_ohuHqUNuE4WBPuRqV5qZttl2Modg7o514nqcvDPnds2R_Os2i4RNsUWBXFo1WsnZ9LWAkoSBlUTBY69CtQO1CkT7uH3DAGYtqUMkSQFOsJwCUIlJoa93DzRdn78OMrZYEDbPVQfx9B5nZuNGMGH42CZr76S1ky3_YEgone8JUl4s_LF2HBwqJAeHnqOTU4R22SiPQKqFe-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=fvvyPpvTySC2GQWgiuP8YORIyUpa016EVdSYrBB5XhaRfcoCXIdiQ1FgMqxPc83UDzKoETU3M4QuQbvkzL1oEGDs780SkxzFxWcs9z1oNOaNmJu-Mzj8AYMhAArwGNwouxS7EcG7pt_ohuHqUNuE4WBPuRqV5qZttl2Modg7o514nqcvDPnds2R_Os2i4RNsUWBXFo1WsnZ9LWAkoSBlUTBY69CtQO1CkT7uH3DAGYtqUMkSQFOsJwCUIlJoa93DzRdn78OMrZYEDbPVQfx9B5nZuNGMGH42CZr76S1ky3_YEgone8JUl4s_LF2HBwqJAeHnqOTU4R22SiPQKqFe-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCnGzHuMSPqU19gjZlqYWV7qjTlE7UV_UWaryDBj5zAhP2fEesaL3Jzi02klJ5SUE9_sr8IagpoZigR8Sm4vyFgAYDuz3x9QLs3_s59kzlWd7q011TBRUVbE5iWNDSBVVRD2fnJ-m08ej43TDlUWdjWSEtJylY6mxZCVLHFLjikW_rzJDRU_i9uQzKuMURmf_gy3867T4Wfg66nwgdy2D5DnriHawmeustirTTar6UPbSFK6bcTeoZ4OrPxkkyNZUCyaBWFDJMOD3W9oJRm36yQ2j7dVVUnhJC9rmZqx2_JsyjABwIIMttCOfbYouwiiT4uXIY6pWPCmWA3-seu5QYxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCnGzHuMSPqU19gjZlqYWV7qjTlE7UV_UWaryDBj5zAhP2fEesaL3Jzi02klJ5SUE9_sr8IagpoZigR8Sm4vyFgAYDuz3x9QLs3_s59kzlWd7q011TBRUVbE5iWNDSBVVRD2fnJ-m08ej43TDlUWdjWSEtJylY6mxZCVLHFLjikW_rzJDRU_i9uQzKuMURmf_gy3867T4Wfg66nwgdy2D5DnriHawmeustirTTar6UPbSFK6bcTeoZ4OrPxkkyNZUCyaBWFDJMOD3W9oJRm36yQ2j7dVVUnhJC9rmZqx2_JsyjABwIIMttCOfbYouwiiT4uXIY6pWPCmWA3-seu5QYxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaXnzU5jGd6VBiQTooQ0-CqZF9UxQOmi3P39Bj0gNh0N9bKAniQ0V6OY4D_skRu9yezzEBPkeJU24BxJmPJinXP9RaI5VuJQ91do7BNVJpDFWxl6njyRSoQi9CC6KnRxMu48uYKUk0UVYtsH0LQg2ut27w9Y9Zx_xt7CgpAdwjEt3VX80B7ynPWBZBDIIqt-KWHlBOk-crOxrcDYE7b6mTb-xtOaZ4yJHiXWFl4kiV0F_imI_HkHQbnrH2BKWwsADLNjOwjHT7kaLJameuzM-tJ6hp7t6nfPLvv4l6kF2iFeAnXPpf6EMhZXnuiT2n-zQbWy-6i-2p37AGL1bHR7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJPUW1sYCmXAc3kF0D8mOMb3jMP3rdyXrHTM35Q3z0WbRMLYB3pnmg97L6kT7pa4cPvnbw9YN6lkxC-hwT69mpKtCBF3UQRh7oKuUnJOIK95Yb-DOjJ5AVzBKaGzynoP6IvBc4O3F0YXZtTtBOvUFEkKNz9kLqJAp9y7N9ihxJz5609vk7RLygd3bpbDx7j4YBzaBzbK8QUj3Zh0zEcOtoARTxwgGZB4qpWrz8rVZzFCk2qC9gBoYmhM886nBTG_HORKiS7NsPWhw5Jcqju5Yupl5V31Y_TlD6QJtQvhTbUjY3UQ_yoTKUPidy_0jb5SjB1H32hAfPbfGarHdSg3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA5UQRbFxlp6yOR4UsFY0W6wGQbBg_AxG-rbxlCF7PcElUsiS-PBQXkAUBUBYgojYkkXUClRKDOmOKqDoXUw5mUfaj2rm27dlepFteyaBD7ofXUHc0JZtKPs2a6cFrfP5cYIrvnrRyjUIM-vydwNLe7jbgPU9Jy3I6jRUuqT0_WOaWa-sd2v-hUxTcmqu7sc_kldKVCqx_x1dO27WuVrwOwOOOWt8ZSO2bjk-2ABeIrA8Zy08al9iTHgcpklbMDoDg0Qr0W9alZuWje9Ih5d6Ic0zKcxSSG5JAA8t7LPhp5ZUMirDsCwSf3-_yKQjeKhXZaqZqRPkxIjfitvLmTidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=i5NsiVE5V8lPQZihSNIUCy2rtlLY44L7EJ1uFyoLldpSMePXUft5aZJVK2ALnWtphnNYw5N9A9O6KQ45zdsiPH3lIpqptB_HD18Aa-qNYpsaVJpNETMg5Fvb-zI3nx7RfPmZQbYEWYbLlexyeNiXSwt8TKgm94IAkjfNI4wExYPBmpZ19F5IYcaN8w-utMDMxQP8oZUPEsWJ7twCjtJ0KbYSV6JuDG1HwnNpu1M4j6sX2iyoHiOlNMZIXcDHZMcpp6IfjbZy83Sfe_czZGKqBq-q2pQmy1ZxXsxYeB0UHxKoIL1ChxT1mnx84hrnd1rPdMMVuUnpDg52AZpo8zuP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=i5NsiVE5V8lPQZihSNIUCy2rtlLY44L7EJ1uFyoLldpSMePXUft5aZJVK2ALnWtphnNYw5N9A9O6KQ45zdsiPH3lIpqptB_HD18Aa-qNYpsaVJpNETMg5Fvb-zI3nx7RfPmZQbYEWYbLlexyeNiXSwt8TKgm94IAkjfNI4wExYPBmpZ19F5IYcaN8w-utMDMxQP8oZUPEsWJ7twCjtJ0KbYSV6JuDG1HwnNpu1M4j6sX2iyoHiOlNMZIXcDHZMcpp6IfjbZy83Sfe_czZGKqBq-q2pQmy1ZxXsxYeB0UHxKoIL1ChxT1mnx84hrnd1rPdMMVuUnpDg52AZpo8zuP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPZWF0fVMxXE2JqPQh847r8z-NRNrBc66Fw-VnIASvM--JMAMu7M0IWRPlAv9YA3JC_RaevavXOa41kIiuquEROqemoILsI5A5kKMnQVxima8fc81DvVkGSmFrP41XsPC7b2mM4KfS5xbCj_SlsiCSFjMVimYdE6O-PrssYajRPRaQ2JEpChfq-H9kZqQdIifilb-FDRHDk-YC_kDf5MHB-N7Zw-qKcl8rT_5sF1BT4t0B9HjHg4K84sy5wDLPxFTV35jmcLUAENtS-um_lrl5akpQYyOaVIeHjWWPii2p_1Q7EBz2g6rqEdukKudKOtBed5SngW6N1oVtgJ3N33dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRIvGpNauY2x33NFr19TbwFAdat1wDvRz9D5g8cihAzA0spZSLuKdUOCm4R6vfk909sv9YsMi1bddAWhaQX24FjJh2vM07KkYGNNl-DFVI48Cj-kOG0a3bccHdy33-wR_C_FNYweBlFvSo8e5yuQ9amlHMWGqzZYxYxB-lDooA212Ez6VqaKUOgyl_JhVXCH19FwUw23yX2IHIykTSix9ZAdxezBxGu76L1JNxY_FucaTa7yzb6qDxJiTo1O1fS1aYE6uSpADoCKSpdV6g63eQAl8K_s1jM_3JQ7msRgpQVSzfmKNxgtt22R2KjW12KAkLzHQcgfs-og860BOT1Mpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSIMy3w1HR9uHW4QcuhpLdndC8XHVghBtNe9DlQ7AEoc2oLH937HoG6BhqjotkwMZa2Us5aD9XZfK0uE4fXB0d3_ob-JJMutKc9HGIPO4qAcrsI0MAQj6rlt68s6AFQatyeNxOFf5aAqiHIKclRVSPHqq7e1FDc4ecpWqI1_y2fR61Ytfyi6FoZYg4a9xmOBZA9MbnPwbxKkN1efWC7sUWUt3ejkSURIIYQmCDT6aNdTETdBZZUUhOy9in7c54QwQN0lUuYcP05mhstiiQJkkb7W6cI-USEySPVVU7cUxgRJlYDXKCIJFPKRFo97PClCX_dmYz02emPAvxeBHswGXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSuhKb-pylel8ABiXn4OlCs7MBfI1RaDs7VIuEDr8z9Q_qyZv-jSBN8cH8hUApC9yBjymMZtZQHIBi09firDJrp__CI95oUePpK7dkOVhLmIceEiiWIRDybKrGY6AuK4HRTMGoiXUKrasxFuUmbJO1CDBPgN8oq_KA14-Q_rUc_RT3JscdavRoPYN-jNJdvP3HZKaTL4-xiML8w-QNT_WeP2NU-LKARhOYigAguvKr5TvmriwvILUukbYTdxyFqPwlxKVUfvcGE2D9fjjhR4ZY-oW18IwzniLcQEUOYWt_ysX9JbdjZHjsZNBgiKYVWnq-iVSEAVWFBAjnZOosUR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=dWyLLlI-8RmX-HexBE3eBcIzgSCmNlMOyvOGzFBJhU8uysESvDcpNh_aVUdjQD90-xO3zg_ObAUdHl7Byy2x-GHrT6ZymssFJat1T2LMc9Gy-WVw0V57gKiKprgf89_FLLtcfZOHT7l-zfnE1jNZkQDW10tSbcX87i48-NTQ1xA00aKsb6qQSql9EcFVEj9LLXxMtGY9IJVG1iO9ri7IWUymXn7j7mHmd0nhoJOyS-cFywmnKmDFbT3SFvBGadqY5yCKnYbbArVsrNXDBC6MkL1UvfraCb0VzuicYokpubi7tJ2MH2fjDoRP-7B-ae2oVkvOIZVE6Q1eihfRgkPgUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=dWyLLlI-8RmX-HexBE3eBcIzgSCmNlMOyvOGzFBJhU8uysESvDcpNh_aVUdjQD90-xO3zg_ObAUdHl7Byy2x-GHrT6ZymssFJat1T2LMc9Gy-WVw0V57gKiKprgf89_FLLtcfZOHT7l-zfnE1jNZkQDW10tSbcX87i48-NTQ1xA00aKsb6qQSql9EcFVEj9LLXxMtGY9IJVG1iO9ri7IWUymXn7j7mHmd0nhoJOyS-cFywmnKmDFbT3SFvBGadqY5yCKnYbbArVsrNXDBC6MkL1UvfraCb0VzuicYokpubi7tJ2MH2fjDoRP-7B-ae2oVkvOIZVE6Q1eihfRgkPgUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=KQY1tPLsl1ptXYA6pTC9mzYQRwHj-uRaOxgE5DAmCGjXAA7GgyLVb8fApArhgYdYtCzgVi_lKqQYUEcNlxsR8FKXqAwClReUtlGAKFdtE9Z2GAHK7ytMNdE5lB5fUGanDcS-eQaSDTEtiP56S6Qpcwo8tUqMt7nbGVigeuxe2UGXOA6O-PBCwqjV314eD0Xw6Xa4FRr88ymdsxcUFWaVmfKKkwfn7PgfLO2LwkQaTpcBPZOYJ1EOEZjp-fsME8QpO_9vC8XqvElAPnrHEb1zd4XgizROOI3Vk7Yq1HHEu69bTwmapmzyr9KsgYF84JO3W48PHTOGl4am8CMP6wbe7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=KQY1tPLsl1ptXYA6pTC9mzYQRwHj-uRaOxgE5DAmCGjXAA7GgyLVb8fApArhgYdYtCzgVi_lKqQYUEcNlxsR8FKXqAwClReUtlGAKFdtE9Z2GAHK7ytMNdE5lB5fUGanDcS-eQaSDTEtiP56S6Qpcwo8tUqMt7nbGVigeuxe2UGXOA6O-PBCwqjV314eD0Xw6Xa4FRr88ymdsxcUFWaVmfKKkwfn7PgfLO2LwkQaTpcBPZOYJ1EOEZjp-fsME8QpO_9vC8XqvElAPnrHEb1zd4XgizROOI3Vk7Yq1HHEu69bTwmapmzyr9KsgYF84JO3W48PHTOGl4am8CMP6wbe7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
