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
<img src="https://cdn4.telesco.pe/file/EV2MqBw1UVHiVE985kcfIKpVREe4wNLiDznHDuk7drhdh2seC384itudXtYEokGSo4bL9VnDJI9MMZd8o7LpFfh0_Z0nOwUDuuME4b0yaioALblflBX7BsLnXiX6BFhs5HnWjvCX_KRAxsk6KxYzcX05PM8bIORt2RHJkmJsoTyUndNhDZCY3GM9cC97l75lSambeShB9wYfT7jeyH3vhdsYzPMLQC9dQqjkXcH8cQ_e-MCyJNGBWAHy8YqbnsfMiY4IfX8kNCuMuREbRN6dpZuGe8fTutx4YFWxcut_1TyvTEZWVcFJLb_mmKFQGDCWRxS3BjEsqVtVNlrFCCAAtw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 23:20:10</div>
<hr>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6tZNI3quD6nOf4FYwG3c0IY2VbcbEn58ULE3wTKPRplKtlbPi-7-8jS87Nu7mfOLC1PXCLHhS5zvhdfOn1AYqqK6A52-Cskg7I8hKO2DfG3kKdu9UDaECpeMX612XIwokr83JnET9ZggRZdtFhR3TzqZ-atjSD372m9V7GpSpm6gq9N2x86WX3A4t3xoQuF-B4hjVFMGfkep3NKgLURoD4e6pvYwnGC768bLTIIYtmDwYbN8TmIvNc1fodTbDN6RLZ3Q-etuzPdgkWnvbopPj9X4Z11Lmd9eJoVWh4hDP9t7fPt1aMvfi5J5BDBm0-9llB8QcZM1daSiHq5uHyAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jut8cQceE433CeJXf-9_g1_bIv0qU6giDxbpJgJVvXJbKl7UTJPo-DfH5AxDhgKeG_G32gnB-Oziab_FB9LLyGLQMIVS77wMRSQBI1wvzoX3BwIcePIUNbjDYY-UlaEM3ZhFPMfLav9CpFHj0jAeCM5I2xPghcSwhUmha0tou9OuhRGZxtVGlJjPxOhkyHKTe-2-SJqZp_WK1Oknw83qfab6U8WDLQ62SgFrrbOMRB6RNfQGFzLlplSfHIN6yM1kGCZld7aey4a9kMhapREtb2FIiWBrOX_y-Xv5KEvhkQLMzLb3EULX4PA3K__lFA16otma-1v99gtygWBggTGeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw6bpaBhOneVqI4HAkwRI-n4FmRNhSz5954foGCsGClRm5ldPNG_Y0VVx8NxSvl8jqIkKjtV0aNQ9gmyWeIg_Zg8I2Xsk-sVGj5eVUv7yBGfiT3ouwFd6PDrDice1397dgubbvOTPktnVliKyLVkzhhlXzGWrJCqtCpmhf33P_3RVm5az2yGYtRipgD-AXFI491fnACJKYMAGe35SLKdoWXgjIzHNICWy63w580RNeasTSnDd218RWxRBLTzg4XL-wgTESVKJkctWumhAzDFoEeAtQDMJyjnxy0vbB-kKBFW7TAoQ64Wxgan22HGAZ9I5uXQOR47486KiG_lhVBZBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZDC12oBufPddG70KmZA7zjfZUPnhmKYUvV4aUS6WINeP9XbTstDi2fAL5aWRr-YoJuu9Z6TCAFJYbGBmaTQMdbB3Bp4wF5luQoxVGSLa372BO7ODr3I2QJRGPYWPbqfA7g_suaQw72TZdKtaaoDP3StWQVm3FlGBiaeO0lv8odXQUDac4f2alQ4XuSiYpteXYxwt1zPkU0c0REjBpftlfyte3n1Ow9HrXbNBDsdP7laTJoPhxF2FRnUPd36KAUBT7b29j2JfhKCGD42ar7uVaxCN35IrS0_42MMisGd9AP76SJozRS4qwJRuTHLKZaqolpmkP1rIOZHmnzGh44-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5tsr5IzXk3jiI-qoQqo3P4SPx_vRWaDQm_DX-IZfkX5TpIJcq8vuS_cQGuQL-bVkDvfZLrzgjd8M-R5s4enJLlTPsEv0qV5grl8GN6RwVLmZ9S2FN4ykDfltQNVHHEiCFPffBUBCfoMw-qKWnFBbn1E7ED6Q1udNAsIEuZBPYULgL3uJFPIsGIRFvg1zriXsbe7H20I2Wa8In9LQ3v9XooNPQ-ABtY3cWuJF08k_RuwpiwqJd2m228GkOk2Bb8e72uKLbtiqXl4mUWWiYq88vbcUvWO0Cq--lSw4LOtN-Eey9vMbGu8Hu13jlQg_oi4BHCpvmUx9mIz6nKoXKk_xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2jvxndXuOlDQ90AS4zSGOMX9a898jsjr8sv3dRWPhb-jHNTbppzu0wHR2u3nPPCIa2kQ13MAftcNDA5C15hlyvmWitzWY-eu5RHfFcUgM_-OrcUBVGu6QTlicHiP_ZXgZJMYGhUO4IdyB-X7PjZf2faOOJ1FEd4fJObt5xlo9hhALXC2yyvhJfUD0ik4VSFoGM8J2UDoggZ4X4qVj_UlnIDP40Y94GFlWbt62bme7hvhZEq2JH_LbPiEt2y3krTRG5u7epc2cfL3tmq3QG-7bxrQhJo7ubGcsZJqj7U2_MeDTL9sHbZXsumbwdRCtc53QSWFFSSzrXOpRVrO3-ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9aPxx-ivjmeebdwMhUPzMmBWJpkYla_Xuv6QeLWSjWSFrJE7Fwmjw9I5b1cjQ6sjBTkwoFBS5FtEj6_pHYjXXpBxX95jsrcHb1EWMdeTRcEQTkv7X9t7n0eYDRxyV1ngsecIv1Dnf9RSFCG8wU9lG4BXqRLFAJ2PEoBxp5b_sU53LzjLuR6JdV_5673tscO_RQJgqGMd-VktOu8ZCvziRkGq9tDjcsXMr6u7CdIcoenWluSpdFHKQaG--jG4mCcaRrg86CuTCz2N0XfXniMAL96cKLLPt71EgktRMnFBo3zt2VrDMhap-XfekVCdHTPvNEppxJyg0hI-rMmGSjTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWR0F0taF1ctqMdfM1h9so9bW_B3JUxh1aJe1avLLFXw7Cv4Q8CHXQT-ozQseL2b4JnZRRMZEj4vCFos3tVUQ5BIvzWsfWYo7FJECZ81eNJ5Uz-T09_EVmuqlZFdWws8eefhJfMV3I41KD5TaVE1Zc4HPJp-nbswCVJxTlZKLyHL8kS0rW8eDrzLj1FezBBRd4JXV9FfsmKkyaQ1f3svvrO7Sa_vPqIypt47dz-TVpQ02sL9ODKTNwpOh69_uL70Ir6nXbO0xTzmuv-vFyy5Kynpn3zQA_iPCDRLsQr8GGz-qgW0--yYOrmOI6oKD-ea6_qsbJ3dGRlO0lyyhecSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzNBEuvuKFhvosmDZEZD_qHgdiES36oYGgbV82oIecEeS9rGiVpEnZ58AgmTh0hkIoPJmT8MoG45iHIbOkrQOKBPPytH9JaK8lxl6MeLThaq5fjFuDMPS-Ji9sedJP6L8kMJqctmUWORMOWwbatT-q5JCIL3l57lV0lzg6YrVSWAf6ywU_gTBApcXyiw2xJRY38gfhcb-iFdNJCQs_qkphRlLpgMrSon449xoL0WKlV4TWUho_ncX9rRuBl_21xvdWqGHyFxqKW1vBcQbv56LiTLIh_jDplKS7SxUshMfeO1pidEzy5cydQePF1spWz-bSTBZEjhdjkGMmzvFLzDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZscfZsJaB4umr5btkTkFLk0GLF2K4Nm1hCa4KCALW1b8s1rx1uVAcjKhc6yBPpR76vvvzLOegkqjBBvXZHjNoXtwS5SM7A3HPOTS7YKymS3h4qkXGcQ8Iew2SINoWph7yZ3SRtwSr105zKDpQzJqweUSiQFZr_fCou3i1At0M6CASqFiChCSLe5RjnSI8yXO7T7z8VDB4ETNR81-RkYBMUP-pLlkT8q-iVHSj_YsbNirvBAzUl5h9iMF6PsAV_jl6VCmpOniubJg7ZqgaA6kYk5io1yvuP-YHemkqcMloT22NE2k1AboMr5MaNXedvONvyiVFwusOHCQez7u8AEIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thwKCbMx9lgNTG1SBm-OIsX_WLPF3Ke3YCqGdYzZjcdt4OC02_r8AeHoEkvNV66vV4GLhY00LJrZHRJ_JYyUY4vaF5dxuR_L9kzvw8qkc6wOlelZGi0gJFzhyC9smOXrz1k2yavU5uk8i36P_kKSeA4EUS9dcqFkxxRG94rlM-CwvS0-r232hSCrBiWc3YyI2OCbYad1d4HUK3brY55MNMGNVkgXYBUN-nZQUHXhIUAJJORZW3cyawOO6w6ojo3GpRcV00ESXT-t871e1zFh5zwpxlDHw2L7tJp11wI5_EL-x8NsGFWZUBD2SBCuReiPvQOZ7DOYChLcOI6okxpNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CseJeoc5hJk3h3vKBolZyJ8FT4Jl6_pqtQMLt0LUF0WNoYi2KWpnc32CXxBIn-m-XK0iNiYSpQu4zh_N2VN1ERYdl9lOS0HOSZvDkXj5XcDBQOqpMj8U5u4e2_tRKqaV7ZrzuQq3B9DVGxVMq04H5S5RwJ3Xn0nNvw1pJ5FWr7RUGnAWgccFQDomsCJF3t3CwR4p92Gyvz_xV8vZrvvm6UrSde0E0mitXEGo0WVc0UDjK0S1IWeQnHzr8c0s3tQttL6vwS4uSdv_SlujM0ADhn3tBuxPnmCH-iIO-snLAHO1IldMXSd8Hvgzi-ff2iEjDK2gTBWSKGkGqkSSq_4AEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCxuUpgO8MfM4yU4DRmH2BVDrYiCUNMT0APl_OnfSMZ4ogaohBYlP-iGNA87FX2ln7GOcQYPe1gvGiR4npi6VGRBgGEgVlIedppXkMdpfHkuzgSudZwa9bdcsuphg9fd0z5OjP1TaF3bIPCRPQbbn5FzY5EXrJRlezKWwJ9EQOvcG7_2QI7hUCEZLAqSEt0nnhbQuLXl0sFYox09SbpReCfMHsaFeMC-67-otNvfVzp5xknssWynbVwNgDc9XZMbk-DkvXw9XCChCexOIRPlXdifWg9SR4TfXzRj4bpieaSoHrmeyhVcvNLzMuCDWlSk-hdCDnD8yvTuRo4ovb0olw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN1O9TJzKHZ0sCGpSmrxXtY1Ng9IEG3hCLFrbHTl7F83ilgqcevyAETOAOiqz3xrBKKcdpg6LhHIhnyEVCSwJ1lXJnS_G_F8Koxjg08p75YrE0GGfEXNTEXk0s2lSmWmAcnK5H0Oo9-HDccAnHicO_8mXHjnLbbmqZN9ERtmboOO9ADMVtrmuP0gFDp_QvZx2BrxX4Vbo18fpc4NJmWCTjfrgCdB8Lbu9VKEyE7R9vCVJfhybTDKD-a3ujAcp8iOhfl29o545Q4urTW84DlqYAmdiX_e9GMGn0H5APYttBaiGg0xCDh8nySm43Iv8NL0vUZ7BeraidjSS3_4vqc9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=V-8K5UUkQUXt1k1u8EObLZr9tdEaR9cIsR4lD74fmKsA_jMAhtHwFqQSz7wdiktI2yuMhWUq0_23oV3jZnO-fzRSSRsaUuTfvnyB_r9MwWkaDnCzf2sx1pABOMpG9MnEsIfV9DG0eouhOSQeqleiwl2Vqhj7Lp1BxUK8TOv6yfZrcRhqWUSztkm9jarhJOHXRNipnCsoUh_rTHRDFsTCOFFbidqd0sA1Q-2xb4CguqPPd8AgWDVp5vPW5DeRhiATakoHO1r04t76BUgXjE3-9U7C-hMzPqxFCzXf8FXsEoOg5NXVDOaSUi-pAU4cUF10JWfFq5oK5DSJLqaBoin2Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=V-8K5UUkQUXt1k1u8EObLZr9tdEaR9cIsR4lD74fmKsA_jMAhtHwFqQSz7wdiktI2yuMhWUq0_23oV3jZnO-fzRSSRsaUuTfvnyB_r9MwWkaDnCzf2sx1pABOMpG9MnEsIfV9DG0eouhOSQeqleiwl2Vqhj7Lp1BxUK8TOv6yfZrcRhqWUSztkm9jarhJOHXRNipnCsoUh_rTHRDFsTCOFFbidqd0sA1Q-2xb4CguqPPd8AgWDVp5vPW5DeRhiATakoHO1r04t76BUgXjE3-9U7C-hMzPqxFCzXf8FXsEoOg5NXVDOaSUi-pAU4cUF10JWfFq5oK5DSJLqaBoin2Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=qUFYB0Su5r590BUEsC55NbOUYyMDugkBKgeryMLnQOvQRkKqtbRWYOTBGu9IDTasUlZDaY5v3sLBkc1crhlE-LwIGaoS-rkeUV6NXXZXdTtr53B0ZQu70vr8s3IgfcRq8H42Eiaf2CNlEJCl7u93ELKxSamWatZsLYR5Aa6WsvZTqj6k4UdhxxuRf4C0U8TSU3NT7zCZeReKiDBFObqb0Ct-JHAc9zKnUV4RvCcIXX86jGEh3ZrVEORYZPQ6GmOs8CliBFv4enQ130Ehfq9Nxj8616SiVX8i5UDQp7z72Su-SYII-sLher1XY6DTCMUJr8IduMC4O7kHX-6zHfEkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=qUFYB0Su5r590BUEsC55NbOUYyMDugkBKgeryMLnQOvQRkKqtbRWYOTBGu9IDTasUlZDaY5v3sLBkc1crhlE-LwIGaoS-rkeUV6NXXZXdTtr53B0ZQu70vr8s3IgfcRq8H42Eiaf2CNlEJCl7u93ELKxSamWatZsLYR5Aa6WsvZTqj6k4UdhxxuRf4C0U8TSU3NT7zCZeReKiDBFObqb0Ct-JHAc9zKnUV4RvCcIXX86jGEh3ZrVEORYZPQ6GmOs8CliBFv4enQ130Ehfq9Nxj8616SiVX8i5UDQp7z72Su-SYII-sLher1XY6DTCMUJr8IduMC4O7kHX-6zHfEkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=KUxjV1_VP6FgDdzuyLOKwth_2KZP_0Er-BW9fx5v3jNEeLDyJHKSLvOO1WZaJKk86Mq6mE_Uo42l6aHDxMPJGyqDH1rEb5rHcKeXjMi7hXAD2YbSWQXl9FxVzTiNQgmpYC_tlyL8McooOj7ZsPOHTpt7Rk_DxjCVDxAqdC0SLFR50JsNFjwRPr8oW957RsWo0X9aGJmh6_K7yzB5n-OqurBgQ4sT3-TrjkHjbv6WwKi-Q20l75-8WF0chHhWiaBYuEFadc1e4Fs43Bur6Ijsck2dKX5YVPRzPlOnHBMQ5V-sOKXDdVnwnHG7Yg3UsbaITD6slAPmAslw-WsqVjqx3BWA1hCLJpfIT5q5L3v2_My0xsjYIsSqccrnhfUgxorrgEVg0NrWVLTxgskFEQeGxmUaKwAwi__rBY6R0K1xCZBby7pSD7SghgvmA77Wtcl4rWExxUxhZ9mYRjcabzqbJ9QkJafuCQNXtrCMzZOwz4xsgXcnUEalt7vApupc2JyQf9GqyIpXq1tWS7nfE1Ub4t6Jauae7i3U8BspP6Cmx_tH41Y0EaDc4OYGrBXjmsSAbXcumR6Xvzr-IE8OjaUgRJq7j6RVfQTXC6sEPmjwBaEE0KtaBzY2byJQQRtGQs7nv_rSQxXCi32O8_zGdaHvU7KIMfWT2JO-ySA9ZS--TmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=KUxjV1_VP6FgDdzuyLOKwth_2KZP_0Er-BW9fx5v3jNEeLDyJHKSLvOO1WZaJKk86Mq6mE_Uo42l6aHDxMPJGyqDH1rEb5rHcKeXjMi7hXAD2YbSWQXl9FxVzTiNQgmpYC_tlyL8McooOj7ZsPOHTpt7Rk_DxjCVDxAqdC0SLFR50JsNFjwRPr8oW957RsWo0X9aGJmh6_K7yzB5n-OqurBgQ4sT3-TrjkHjbv6WwKi-Q20l75-8WF0chHhWiaBYuEFadc1e4Fs43Bur6Ijsck2dKX5YVPRzPlOnHBMQ5V-sOKXDdVnwnHG7Yg3UsbaITD6slAPmAslw-WsqVjqx3BWA1hCLJpfIT5q5L3v2_My0xsjYIsSqccrnhfUgxorrgEVg0NrWVLTxgskFEQeGxmUaKwAwi__rBY6R0K1xCZBby7pSD7SghgvmA77Wtcl4rWExxUxhZ9mYRjcabzqbJ9QkJafuCQNXtrCMzZOwz4xsgXcnUEalt7vApupc2JyQf9GqyIpXq1tWS7nfE1Ub4t6Jauae7i3U8BspP6Cmx_tH41Y0EaDc4OYGrBXjmsSAbXcumR6Xvzr-IE8OjaUgRJq7j6RVfQTXC6sEPmjwBaEE0KtaBzY2byJQQRtGQs7nv_rSQxXCi32O8_zGdaHvU7KIMfWT2JO-ySA9ZS--TmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i00pLP2LVwjoZplz_NTVSbq89tEU4Ksh7Xsp_R67fsYCzIBUcXSqjounXr2M26LLHNC9u_boFPWr1rRfnqJZPWVijAbuADuOdgd-s_27hVKerTQSD6oTkynHvVfTHVUbcg2zTdJxv6FeFo6QSg253hQVSlV-fMCSJkMduHXe3OIUD4lpDQKUELQinZfhCgvqRDZDZfVA1lCnlF2VF4mvK6VE01Tvj4gBzdbuZ-sc2KuLTI3NBpOdHHZfreuVRyoR2UJMRbbwTMen03VtJOYOLfy_dWOJNlWWTQQ4sxQMU1o22LafAbPEkSv5-UZqeYu-uJxNbUz7m1fKbLpeyx7qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=EkpYUOm78j0HLl6waLio-fbWTkyj8V_h9WEbEuX-YiRnpAL6mRY-Cdz_1aB6L0iSByX5UoxiX2gQkoAyXR56770ezfLjxVsJaOY6EfeN15vj4oE44rh6U4TyVjzzG5yvVnCuHeGeP-efdkzGUiv0snd5C8JvJLDzUmX5ful3OR_23qzVyTXWVonNebo5W5mybZbeEVVMJXR13KOaG49ojt8T958eGdHs-ohePGDGhEHfy75h5rsEcQl7KFcyOlPnDwGzpw4B936j68sXwNyg21S72Eiw3Lnxa0jplxJDe0pmcfWsjFvYdZJgHU1G-3DsIxr0lQ__v9kjI1hgTMQpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=EkpYUOm78j0HLl6waLio-fbWTkyj8V_h9WEbEuX-YiRnpAL6mRY-Cdz_1aB6L0iSByX5UoxiX2gQkoAyXR56770ezfLjxVsJaOY6EfeN15vj4oE44rh6U4TyVjzzG5yvVnCuHeGeP-efdkzGUiv0snd5C8JvJLDzUmX5ful3OR_23qzVyTXWVonNebo5W5mybZbeEVVMJXR13KOaG49ojt8T958eGdHs-ohePGDGhEHfy75h5rsEcQl7KFcyOlPnDwGzpw4B936j68sXwNyg21S72Eiw3Lnxa0jplxJDe0pmcfWsjFvYdZJgHU1G-3DsIxr0lQ__v9kjI1hgTMQpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfbIzP1Z8UQMm9JvNeITN4alLIcIdwE-EgnSDMLdHvzHar8jDHmpL_TBlaPq5uJ_57635LmigvI_CgTfGoK8Znpqoh_R12Y0KqYWcdvOUmOjNjzgSbOD0Gyxq8aeKuJzzUMcQdAxwcx7BoxFWNIvJdJJQJiPueBn_eI4DrMUDKYZ0vLXHvUTrziww-Za-MkaewPH9ftOC0CnbgLUJ1qH4PNh2nQreAPiKqT5HZaYnmzCcl1gQbeJUxaLpeIctoGDs7-Hq2SL0U2xaSXeS4RPiLyFrgz92tZy2yuLfUa_VYlH24DDLJ_Lxbs97iApf4WisgYBh4nujUX3wIz2JOjUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7eNmZ8APDPsg86uw9OXbWcGJt3duMMt-LVPUx9k1MdVQwLFvbI7xMfMChSQ2sa5a6nO4hYyf-PZ3_j2zu4VSYbUnWGAu9H70A1zJfdqwSZs425cTn0-dywM8iYApXzkC6eALH4s1GY43KO4ORI8AOnF9I_hzlGMr0VYOb2sH-U6PxcWZUPYQ9cLFo4iE_a6VnXF3AHFChvwwVcnbZUSIb9Z7LxAF5-FB1NYkwnsHb7xyczlqAP9CqOzPFCLB-1uTqdqDUR3kIiWnQBpfCoJ_J3jDHsSROMExWQBMu9AnfV_YhS8yTC0mYYh5qeY-yOU6Hj1jXK0P7ZE-3SXl89wxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCC_cuKAtGZHSNOOUTf0ubfcWKhiZ_oVN_My4rA0zaN6q2RapM63X-oKZCugvFv9bI8E2iSqwpCmqtZK0aD29qGVITWUYNBBWExB38ZwQ9lNvR8sMrt5Ck6iFJaK2JVBRX0m0PN-p8UCXJxakvzFl5HBQtKaUR8PEnqPNatyq3I1w3CvJnosrM6zB13A0aX-Je2NaOEfkWr3sjn9bziyJaoSIct2GoFxE2AtJccSoUBCfhQLRtkx3ppS0G-iyMQIZ0fQicWjEdtbQWx0jGie8E9lgrEwKoj_OQ5ooX0R2nlHtyIr-BfRzIt-zkvBxE0cvtbr9_-2AgYvelrqXLSr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L185dcaWMi5NOK-vEWjo4xPJMmvgDa7CsS6GrRJWBgfBVV_MMSJJj6GSV8TKq6mgoOxG6LX3-jD57FGmAMrwzzV7fqOx1O34oHoRvw-12Q4vE0N3QDs7IlbDB9oSEIgGyf72W_NnLi4HaauuoLYdnqjyrqhKbDmb9ajDZPrGVaKK52vE1cNHj4uBEpkAcfD0GfoJ9qWahNIyU22d2atUISrGpxjyKDS3sM03UErAAl9uw7lF5s1kcC-Dgp9UyZcO1I5y6_5f6Crr8eAhhE81JnscbZuBTZEe873iOsGCYLHl8Pexq0u_wo4vKSK1SEm4zL_bGNNfwFbtGn5RFoP4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hr1_5wTSMCFp6Aw7PZxgk_2PtkjEW_E9PeN7mQSUuPj5N72L1qxiUFpOjramcWlqfBc1XT6QF4qyzatgYiayfhnAJBNn_P2e0r9Xq87TCTwU9IOq4_8KqNnCXkiRPVx8OXb3MMN8eC2guJvwDdVXzxUU7aKCfQLRrzC4bo470xBTqpsJef6k0hQoJ4S0vTm6VsR0iEIDV2bXCfyLiXgX13YBU45NNvxKpGE4gQLeScIDTjGGTb3lW96rdpcyyC_aQ6rDJXL4OAx6sHB1ACcf-_ArPEwM6b-Qcrwb7VrkNY4qR0H8pXFGt6OdgbYf3o43NNox96Mp7K_fTNlHrkFlaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUQecbIItQVlxrS60cy6iVEbVTzmLfa0gZI3-5vQd61XrbDOwQZiTrPXfLKj_8CRo10uKo-YEKQWIYwOK84Mwkw_HAKDfgl5zZ6lKzOWz55wt2OoRfKeXrfdj0qUz7HoubiKijs_uBQHltUvl2-L93DD7hFeNYoloxZbOAbo3z8UH5qeQcJBiZTRuIjkBiOWHXaIX5DNF3cFUNyGuKogkNewCmiyroKbYby53BT_LBesFJn3-JS394nnkCs2xK0zsGep5YT6Gyr5hOMvqVZpiMRUMcPmI5RbMyq6sah4VY4LcHqxbSDdOqCZXErDeu4oeyWluCV0H8zT7VyKqroB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQz0xF84f01wf4j0rnY8I6vqJpRBO4Sxfm7_aCYXRcyxTdrBFwMqMBv_wM3BXCRxAGWRa2r3Nb_nSdiR1iCJ1yTYyHjw45ET4ekrtLPwVHU4sj4NwqoCPDBlA29l66bcj_PEyAm5s44uswrsgOgP1kdP5Rlc4Ti0a0BKO2c7kBNmTw2PZwOdUTUfCn3gPsFJrtO8QgBcslO1AZKLaTcT6sE3FqRo-6vrU7izJaz-LyE7b5rCrdE-9Alqy0o8RaFNhC2pzROZXRIdaTsJgrQv_yDP6rlQG81KJfMizWrkkOYaOmiu-FHgRyuNdAGGXn_ouZbs7yNZv2vrnLuqe0LhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeyDY7eLgCaU5WDV7LNEnWy8Q1smU3h5AboXf0r4WGvTy7Kb39qQFlhC4ajVV3znHmSg6kc_a2iLcIjM4luRlFRtpHG3EoxCrSsq-XN9g4bFQ91Nx2gVarTzMVh_YtI4tto7Dvx4wBKQIC3VdKjp7dZszNTntTLjCVWe6Drc99NToVDZBrZrGHAbeXloJLOYxCIopf5HAehKsnhoU0Lr_WO4Bu5fNqn-zTq66IfGKrL2dfG2rt6t8XOQt8oZq6uKs9tBZDSXdtzdcZScDK4zD9S60z-U3SRixO_VsLJ0Ttz1kaFDSB4tgNUfO2kq0TXWlFhhq-Uc2UgEdQ29nJ_WeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEcgTT8rEtwYMN6bAwqHfr4QMhLJf96JkK781lbW-6BpA7GQ74tEraef3FXNMqu0iDWWC_MfSID5iptagC73wNX47VNI9qritMDkhi2UF2HzaRccXgvLNioihHu2XHIpjpub5hTVipE6dSH7ABowpMxf5iQBS7B_mgqxJ2EQIfC_tVNF2mEuVq4veV60g-3BP2axHsne4YaqOxc6PkXgYgebET3t6yWKbseCxoAH6vKxYelXHDENGs2hmtdO1EZ1xrOpzNGMjsDfWJWOiOXTGOUe35HxCglJiUaf6BOREbTZv2N14HqmsjtUxutS72B-2dqWK9VFkdNl6dV7SFJPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPNtPzkadzuIHSYil9fkv6T-7SACGzFSIDYctd4Oq-LDoZmqQl8COa0h1QHNgkmGqjzfetbZ0OYs519LXqW57IwRR54CMomcGULtZNdVsgfdbRgUT-bDdw-sJ97DfSE8MuSMhSxmQWa1PojPfykhpXi5fF7QbfSAjIbxyxinHKSAulLAOJAMrABDFODVqRv518dIFLDB9D50Y5vPGvmfd_gUn-q1XMEAg6EntPJka5SpSBDCI0eBIjS8IwBbQ3T8OS1p_SWzjt7Z1dc089nUYjs62yEw_TTtNKQqqsJTcoKW7a9lqA0kPk9MQ23o0ThovUcqH2RLW9u2GwyQPxnqIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1KHIVvg5BwWWiSYZ9wd2UIg5LJJcTfbD9QPHJtz1PMKTkBKrNAXAg1ku-pNamZhGL0OHqGBfWGJNUmbxsa2IpmIJhzduJlfVDzTMC3ToCEtjvb4HCq6RZKVdiLcaLr1kQhv1n5QgVV-75OO6gS88zEoVm9SyiEMwsIDHw08VQ5XaMHr5V1RmHi6IykYEL91JtR6A-W1n9B7zhaIXIYnoTtZ3Tv9jw7iydT2IT3XJKZzu5-kRpdmSsxtgK9X9QN_zVi16xhLfsxTkYb9pKCgCFD4maF480EZanbrws9zg8MX1iDLAYP_ZK_AB-KZtxO_Re7ZwYyaAVx7xuOAAdFHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbZ-J85VXhTztGxcEjbpHbSbdasAVPlxH5-GlqiaLB71wMtcimE5wl8SdPIeSodI3D8UxEG8HsvsCNoUw3XJcZnSS6TY6-3MyzThiRxSzK3elKtKvvINHpUy8f5IdxPRQex3c11Na_COA8191JRa5I_rE3thGOtb6Cij30R4T27TmqFa46N5Bxwri6ZECGzcxpo-_cedErXqFNWGFX3xwH1JFC2HljVcU7C908GUEUz1-BGLVbySApdzXPCg4kJHQsuo7Ye2Jj8cJ9FK0kdkt_6X6xCmjpWDdQ8Kuz8osjj4y-X-0DDTVpC22yFBRYTv04q0tmPbtz4zRvZGsOtGcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWAZMklwrClbBrxTTx509PJbiLrG4ZnqgOF9Ca3XS5ktapqy4rPY8mdhPWIZ9_BmvnUmuc6LOuJTGjhVEBFFAXSh0j5038yIhblAl1ZgUCbM4Iet2LAiZ6JTvnaFEg6gM6_K8fF7aNsDKUEQcsTI-bI8gg-edF5RyBguQcf5OLzlxi8Yl8lDK9xAfyG6GoY-slbqC7a36DYlsTORex4iiG8ufwUunhA1AVB9n7z4S_tL89h7kAmgaJbUKLSAF0l6IizBqcX08fXZcTXZ-hQ7OX0I3fqqgWb0QaVq2DjHXDNA8vNa4dUPA4HnEuLqiyYdrB-I1BUVJnwNaL-ePAaOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4_xTscmUhy9ag9cxu2SEJU1eLlRNtCIQYs6cg-X2DzJCxWzFO5bufUqQimjBu-DgFBgzUjeAQT0ew8oECXTjlfUZLE2ebpIK0EUWHZ3ASSIiNWjeMQD7Ops3zWSEJ7D7kP707rSgkFkuUDyPK-YJ4nDmsguN3u3zIQ1pM5HnytS6bkWMsjlK4uZLG4q-3UApztL-A1e3Ks8wTaa9Nujq0Q6tqIY_T_llE-j8BDiI5Kob6rMMVbefpi7R7rOWy9OHV-NtegBf5eviUDxZuwfg4zXTBqsyJQ8L6M4TorscPB8TxS0k0Q5C485aIDKZoInT-7i2i3sRCX5Isfq25tL2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m25udoIn4UZOluFg-nnjXwaWsEHjxC1WfX9952fWflPJfLoWZj-KEG-1yAkPHV0IF-6CsiWfWub6uNRLxkAbos6IRdOc_yFWrd_M_CxKk3n0QIuiWmODl5tSNAMjsYnDA2SI3dS-3akxQ3FdRCuP8Rlk-pozZcr2K2NX4nx1fpSIBQ_TbujJx9BJHy84PVzk9r7Dyn-cwHuolfvwDzQmdTZfFUhPMA5CyecSr-RZpANxBlRlKRVF3bFa75u1wRLNooSrSShEKJS0HhIoVpIVZ0lhn-gIa5TALM9C4LYh9p6ZrhgAFBECiYUOajE9EmkO-3o23kAbyEfE8Bi-_ykC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2-UScmemtIlFJeQvjIEyzh5Nps8u-XZKfEaNrmRTNr6A_519nPgIZsmKh82OMbZL4fesmY-MwDt3nf7JYcM35j7BI_sKjtQdC4Asqjdc8u5NGbM7VjGFdtIqUTc_ihsm6SdkV7inIEHY6wwnIM9r7VT5yUwg1CmMdkpM5BG6BUZxNiKO3jSFwwn6xnbb9saKYpOjLUNCSS5yEkMSEqixhbDrKaxDnlPruvYPVapF5SnH_NrsXwAYoSzJoQrN9FFLJUe6Idh9mrRgKIv-WEjYKz9AZmNOZvcgB-XE04WrtFGUABR3Tib5hcN5r_v-etEtTZw_8XIhdEQUxqQHaxhNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_frnCTO8SvfB_56RHEIPSiaUW68jrY3SNIedolPLA3cM6xFe6FkselCDsG4OKoNCAtRv-agZm3ErIvUYIhc5IlX2bnC_UukyvQ_rb_LGf5GQ8Tdv9B4rKgu2LBeQhh3QJMj_MT03Ga5xIfex7urQ5iYD1RvVzENEEzZKXY91YwaK6tCacDoxFVU6ArhF_GukjooWZble4Kroa8ov4d5BcxJRjw-9om0l3nr0wVL19AjezHBROzHmKEi3FoHSEDqYkKIEVJcpTGRtpY5dXyv4WfUnEZgYwVzPM_DMa9DVTuqSVwhuIwAfOWQwLhoT2xel0KowE_RsjSCjTenLSChJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=HT-T8iDD2pT92gTPLNghDMtMUpZi7FIm2GGe3diIpBp_jzRs0UglMfD3JOSZ4h_BFwHrSzyv89_1qS2AttZvqEK1zzLTr-CJ1GvDmqsHkESkkUSJUp_kifEhXyz8I5cBTT_qgluWZhZegM9EBGB6StJma_j5kGCTnZqkYfvk3Xdxa0or0mkMBtk1d-xVr7dLiWaN2gFrNEnVf3GZsNGPykK8EVbPAb-3GM4KMJJNBAHEmF8DDtmx_eED0SCCiH4J-FeBToHUjnOTYwQozCaQuhY353qF4Co4EpCOJVjODu97xNWPCix4wG4qf49YY5lPjj6NnDT8OmAI2UjedmQ37Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=HT-T8iDD2pT92gTPLNghDMtMUpZi7FIm2GGe3diIpBp_jzRs0UglMfD3JOSZ4h_BFwHrSzyv89_1qS2AttZvqEK1zzLTr-CJ1GvDmqsHkESkkUSJUp_kifEhXyz8I5cBTT_qgluWZhZegM9EBGB6StJma_j5kGCTnZqkYfvk3Xdxa0or0mkMBtk1d-xVr7dLiWaN2gFrNEnVf3GZsNGPykK8EVbPAb-3GM4KMJJNBAHEmF8DDtmx_eED0SCCiH4J-FeBToHUjnOTYwQozCaQuhY353qF4Co4EpCOJVjODu97xNWPCix4wG4qf49YY5lPjj6NnDT8OmAI2UjedmQ37Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZNZKdTpLolaHDBspq7l5GYaYUT9dkgxLu85LcpOJeyw-NSiL-MVNQTTUtiZzDiOCo_nMS-1eCBgnQYe21s9JRJxG7hqFz7QIk6_zT9ERBS08S_2XUSxabGBVjJgSBSfhtSqY9qQ-i_Um0ETgeQhM7cp0t9MOS_dfOqNUj4773LuyHEAstasodBS3Vufw29a-T7oOPENR8_3OOqTyd0QcYAi4qWnNVG8eMQPKGzQRi36Y3uo_aXZmj_osQVMV2IHjcTwBKF9UK_uF25MCKrL5nwDDyqrOOi0inJpicBF6r-WHGNXto23-DE6kjVvBIS8hrosP8OAttnZ7R_ngq0cGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b88WEu2Viskcr2I74Nrid-2fmTdv_K1e0tIga8cTz-lYvpXASxbAowQKoG047Gu_ZCUxji5rSKLSCC_oxeAE1y2G0X2Nnqilh5dlZe8tXriFwYNIZ3XPtDBDGWDXtjXz8ZzipHpAZLNTv9M7VTx9iIMMfqpkrnmTMyBhILyY4FI4jumatdfhCizclIdMJmjI4Qi6Jf0qP0NUINtzJg6tuuHSBP_Gi5ZmcXSvhSclUrKP6M0N1kd0YtA-AA2XxQWn6sFNG7kqcL-Hz5RMouRYHMSFQFW8Cht23uuWWISOI6h_0x1-ZPGZVORUaWV62mMX1FTCOH-zt1fcVb-CB9QzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYnSgFU6AxIr9yGtpMvg81k3BQ3dMWjQpoiKF59IlS9vVYuCFvxbRbzjpEiUV6VVcm8zJVj8JwW0GxwbxfCYT97728EVXcuVJC5gb2MRSLpw5QqwtBUZ6cywPK02n6YPu_AeVW0N53KXACplsKbXALvPMBSIhfE5-slvBWxUuyLSKmZAWq_kfuygGu4gaXfO3tHT3L6_EiTAKL1ytNarFJx52J9mXQT4KuXYyLfnC9BgOnoGP2vQ1IPiFhlIYQ9kXlWqNXNfN5bT_MW5iErC1fMeEkAMHE6Dn897jZOab66chqqop4pOul3daHQ9vCPGrhJYzAoiJOGvT-O3v15f1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=mXmW35gkrRocnfMWiepgIblL4Oppfz9uEByGDa9dzjEpmGYbjfKjebs705wNysd_M1IVGppTbu_zkDfORdhvspWtoBV_T3LyGS5aF3xzhWo3Db0ePP-TCsd-JvPGK4gMOFVus7INsAeiDVLTZ4xonjTnstKdKB98lnlF9ad16iz4oepHK2Cqjk6ytagQplynn-2cstttKVtRnpyf_nXtc8ybKjmWtBzwSRHFYVC2i2Uo9QqYJwwJJEw_osIJCg6Z5rxRoaC9u7jTdv14QlMV9zUpWd4q_T4DWmZXSk3fuHLK6OzAMX8VCxKsP1GbnIzxntniaQGh8A4x2IBqqcjmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=mXmW35gkrRocnfMWiepgIblL4Oppfz9uEByGDa9dzjEpmGYbjfKjebs705wNysd_M1IVGppTbu_zkDfORdhvspWtoBV_T3LyGS5aF3xzhWo3Db0ePP-TCsd-JvPGK4gMOFVus7INsAeiDVLTZ4xonjTnstKdKB98lnlF9ad16iz4oepHK2Cqjk6ytagQplynn-2cstttKVtRnpyf_nXtc8ybKjmWtBzwSRHFYVC2i2Uo9QqYJwwJJEw_osIJCg6Z5rxRoaC9u7jTdv14QlMV9zUpWd4q_T4DWmZXSk3fuHLK6OzAMX8VCxKsP1GbnIzxntniaQGh8A4x2IBqqcjmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b930UByr5XCpHSDlABogYplDGT1uOdaejJe-2Opqa2xLhH1Gbd7ujbeoQL3NaFHlDTozKq-ZVa0sQMHznp76PKS97suOeVe4vIlODd07OMEmcKcvSg-Jv-r0H5MBcnKV2sVZ3JXpjzWcC7XEZUfUJt3hffWoBf01WpDj8QgPHrRCyQfaP91guv1a5M31ms57lAvTt0fs3EtOa6sD1MaCV5g9I2_0Ag4WhcFFYnCr43l9wsuOTlb9TzJY1Ow4K2V-NSgk4U6lIhisvFFpUitjKZQsvVaFCjheHBOpO68bBHZJUiIFM95RkLZkmFH3yOgUCR3eSQJWP_c2WIEkfTmsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=V2pQ_N6l2hqmEcnQtEFzWJB0zpWafb36CWqu8Q3uEPfsHwUDZ8sYoy-KKKk8ecZYqwDKKl-RT1eInxYf4dFSZuT43XlpAh6WXx69GWmnYZvOywOcwhEisJ-becTAduJ9uFjxOGS8QZrTjsZBC522YyR2Mfe099y2LbpYbHw88V08EmZvp0XCSYZTNK8Fkp6JbvTD54uSc4CdA1g5DTShz3a_3EesX-YIYBenjHstThgc10rzIeoFc73JvCjkJjhL-zkGSO5T4WpgP1zZqJY9WD7LtTHBLswHIsrj-nmUTTnY1iXSax-6lFIU3rRMC-lWPaGhoHmvPcgDAcVuYnDtJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=V2pQ_N6l2hqmEcnQtEFzWJB0zpWafb36CWqu8Q3uEPfsHwUDZ8sYoy-KKKk8ecZYqwDKKl-RT1eInxYf4dFSZuT43XlpAh6WXx69GWmnYZvOywOcwhEisJ-becTAduJ9uFjxOGS8QZrTjsZBC522YyR2Mfe099y2LbpYbHw88V08EmZvp0XCSYZTNK8Fkp6JbvTD54uSc4CdA1g5DTShz3a_3EesX-YIYBenjHstThgc10rzIeoFc73JvCjkJjhL-zkGSO5T4WpgP1zZqJY9WD7LtTHBLswHIsrj-nmUTTnY1iXSax-6lFIU3rRMC-lWPaGhoHmvPcgDAcVuYnDtJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtgiUUmwA4qJ7KsyAcMFJfk5u4wCNEERjoi7gi8jvezrNJGCVTAW010BOyYx502rbq6wROIQS7h56SK4wRipoAITu8F-VNqcI1Y7bnWyhpsUFalWWmQZBG57VQtw7oDVmKO-3HmEh7wpSlLOpBi8nXvwnyDlPSLVomTCKRctfFY4DZheiOqkeOFmzSAIFqiqFO8LdZ894dmEknZbgb4qjUI2VmGX07cwgMWgB-kSFFBIYpE1qCXyoFMkklwPhArBnYKP3Oe4OJCsl4EzOofo6GNMmT_HxEzsK9DGNLwY3snLzYTiFvkzCQIWeGxio2PNBjBVS0eZdA01K-Ao5q1XXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBNVYBmFBGI1HPwc0AAY5pDva9bjDdGyyzuXcYIg9fkRk_jLoO7oHhZqISVDxk_oGKnKXtXQMiKqXMkSlVok1MFatrcoCb4PoXl4YqpWa87BtWIbPJIhURGa7qGrNhQ0evIxYuROyTSLFGdPEkV3eWmsKXluigeO7R2p8OtOPcPasqSMmbvhJFI4rfYX2oZOQjCyhOpXIrmtX16_lM2JUgjcPUmr4Wspe_ysAYLTmRP84zmnVEzsqhfPUJYKufsVkdX_LktQ0yHDem6_NL_-b-GyMWFi7WpY-6TpTi2BZYBKAliXib-L-fq7x7oguABxDdMb19ZiWAyNRzUaJaaNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=rTDXZ9XWG-9Ti5txBJo3YbET0u9898n3WDIHAJ3adyLG4gdGTL0S8tNJvmFXV97tB6peQPT7gmoYPDCnFDtSDDjn1kgciiqfHR3IaPtDt5-KVKbmVNZEb4OmfeXPrKIbCrdZVbAHe0oQg6rdfPkNnk1pos6T1oySdwZizTKukCWACHZQBe71qa3XiouCfCNR_ZFlrIVqH7gshrAfu0PV1do8nEZDGFN-riik9MyIYlKiYJLBG57FLcufu7ixgHLKZIHaYu0QxFwMLmYJZ_hkadP19q_mBJOezMdMN4cHJFWAUDcG-GpShMdl6zE3P4YtTqoPRVT5OLKFlHB1he7SR2TngXWnYv1DUz4fIF-zhR9z-uQSyi2s3mVLRvlHfERnCyvZT5o-zA_lkNRNmtvhfe4Nq8qwUlISiAubnOdAzeJRHGX-q9I9PhztcSYudqg14l4R9_vGPqZKeih2BScpVqZ6G6hgxyi2C4L_mqORQEsz6kTiTqwALjMZ0ruzy2AHdMSh1ldA6HiS0P0zypuNDcc32oaqPVJQ_Fv1yy1gNFf9Ohfy1fCnB8jf3rs2hbARHhkCnmMrtW7BBWXhvoWANZVTDP7T2RqsNqhVHRMhu2KHVy9i3woLyi_KBHCz57_VcFV-Rf4dh1pR1vjPrSAwFxR42ir_kZr2j1O3l2xbk9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=rTDXZ9XWG-9Ti5txBJo3YbET0u9898n3WDIHAJ3adyLG4gdGTL0S8tNJvmFXV97tB6peQPT7gmoYPDCnFDtSDDjn1kgciiqfHR3IaPtDt5-KVKbmVNZEb4OmfeXPrKIbCrdZVbAHe0oQg6rdfPkNnk1pos6T1oySdwZizTKukCWACHZQBe71qa3XiouCfCNR_ZFlrIVqH7gshrAfu0PV1do8nEZDGFN-riik9MyIYlKiYJLBG57FLcufu7ixgHLKZIHaYu0QxFwMLmYJZ_hkadP19q_mBJOezMdMN4cHJFWAUDcG-GpShMdl6zE3P4YtTqoPRVT5OLKFlHB1he7SR2TngXWnYv1DUz4fIF-zhR9z-uQSyi2s3mVLRvlHfERnCyvZT5o-zA_lkNRNmtvhfe4Nq8qwUlISiAubnOdAzeJRHGX-q9I9PhztcSYudqg14l4R9_vGPqZKeih2BScpVqZ6G6hgxyi2C4L_mqORQEsz6kTiTqwALjMZ0ruzy2AHdMSh1ldA6HiS0P0zypuNDcc32oaqPVJQ_Fv1yy1gNFf9Ohfy1fCnB8jf3rs2hbARHhkCnmMrtW7BBWXhvoWANZVTDP7T2RqsNqhVHRMhu2KHVy9i3woLyi_KBHCz57_VcFV-Rf4dh1pR1vjPrSAwFxR42ir_kZr2j1O3l2xbk9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=EOriB59zNNrMCYE0RnYe7rYAxvMM6Yzs6cz4MYZVyEDqfqxCFWLP8p7LYydUGNvrQQ-Oj0kivXId97PGdaI1NPQ9EVlj0m9epddLXgnC6D0vFKd2ymwLez2hGiI4QDv2HEQVqU48TiBRjWzAKm7-TI4NvkinSt9LZ08g2tJ59ZMsF96E2ROI6jeiAJBYZH3JyRBjKTJTfrFQk7thHybkenAy-yspfs7z3M-Qt4zF8LOOPbVq9x_tvZ9NrVGpx6kGUzMs7g23jWCoJFFr5LeSzVGlMgYJz5VuIB0YAQkU1i6yzZTW7kK4iySaBT6LIT5rZUFhwYfawF27hnEkrIvPog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=EOriB59zNNrMCYE0RnYe7rYAxvMM6Yzs6cz4MYZVyEDqfqxCFWLP8p7LYydUGNvrQQ-Oj0kivXId97PGdaI1NPQ9EVlj0m9epddLXgnC6D0vFKd2ymwLez2hGiI4QDv2HEQVqU48TiBRjWzAKm7-TI4NvkinSt9LZ08g2tJ59ZMsF96E2ROI6jeiAJBYZH3JyRBjKTJTfrFQk7thHybkenAy-yspfs7z3M-Qt4zF8LOOPbVq9x_tvZ9NrVGpx6kGUzMs7g23jWCoJFFr5LeSzVGlMgYJz5VuIB0YAQkU1i6yzZTW7kK4iySaBT6LIT5rZUFhwYfawF27hnEkrIvPog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WczFRWAS8PQXWvpiiOo5ZShNQZH4xQAu0vdt0E6RdOJhYcBENi9uO_0fGc7pULUd-FRzu0CGN_AoAiyVSCFyF-BxGrmo4VbwLY4mtPjPXtGH6dMLj0g71NGiCy5YS1nt4eS06Xwl2SDmbL4bweKhtKcxthquEphuOf6_sDZFlECoUBc3ZlAiri-5UaU_g84QGmFoYf2n4ngjhvdLgKNf7P6XhZHKusCh_Bi7BaOWfoT0AAbx3J7wk-Dxer4qd5jjRdOmjeS4bB0RnTq4BSxFXZcJ7qQBO76CBv2y_BCoH6mBuzieMJBAG6ksDRWVbNGiXEO41fDkUBE_UvpP8kbS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=aC-44g7FuYZlyEbBC2nvQj30BZRl8BKl3a7rq0lkCvBiM9kvMI_t-kZXjoOZR49G4cPOFRJFV32RSoeEZcAY9gJ-DlUKwoHfF520fXCAT1XmjER7CREbW8fDbuYBz5sYogka61IKWGE0qxMUturpzo5fou1f5_wMoX9PO96Sx9JnZUVNfr3lnxevLVEGouXlrV5AgeJJQb-fKgurA-1jTsd_KPVjWzJrVxt3LgP98Dgwjku_SUMRRRqTUgW48dg0liX519FfKReT7koX11RlTchTj31RAhSnolQ_jTEhr3eH9E8z8gVTBczvudeLotvNHEWPNwvOGdFppSS2csJFEzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=aC-44g7FuYZlyEbBC2nvQj30BZRl8BKl3a7rq0lkCvBiM9kvMI_t-kZXjoOZR49G4cPOFRJFV32RSoeEZcAY9gJ-DlUKwoHfF520fXCAT1XmjER7CREbW8fDbuYBz5sYogka61IKWGE0qxMUturpzo5fou1f5_wMoX9PO96Sx9JnZUVNfr3lnxevLVEGouXlrV5AgeJJQb-fKgurA-1jTsd_KPVjWzJrVxt3LgP98Dgwjku_SUMRRRqTUgW48dg0liX519FfKReT7koX11RlTchTj31RAhSnolQ_jTEhr3eH9E8z8gVTBczvudeLotvNHEWPNwvOGdFppSS2csJFEzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp1JsBjZap5jF61C3BAksNmvaWw0VW5Es7362J3PD3IQ5Fk30Ix8LhJhTLNhkjtxvMtGHp7LxrP7q1S2z2UitwWgV_vmeMJs0MOaq1UVXpczT8uQIgJZvE0q3aS6K0tljN56bXMbeyiRKlD41dWfpXIcXqLXILvDeVc6DBfw9Qfi0B3u7EcNuq7edvq0RgHhLz31zoHI43bE8Nj7hn9qkGSM1qZC4ESTk1Py3TuNif9aV0MDLbu5uLYEi7cmyc1Jh8O09wfgadibNrJFBPRpX453CIVvkZktrvwJLY0j8E1xbhPZHnjFJHyyfC9L5P6uSxBsjAoKmBmn-yxTvPJPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxvHO6RFzre3O8JdxmWlevd2Lzw1NErOCYbJxbNPZtzjXohJX5A8ZYxph-RL9tbPYmEsVy-ikfAqR8NXezUIARGQQn3goVZi2ge0R5fzVc8C_M-FEBsbxZUz_-pK0lUqRxVegzoPHZjeJVxgIrzU8EseIfNLJgTGPNBy-39oR8wbusT_L11bmcUvngkE0Jh6AHjGs__aCNkON539dROjn6laqDpe1zF2uNTiWiWd-gEYm0t1M7TJ6HntbmmPSr8UZtzrTrswRxTyVEO3YoxgN9KHx12u8O684E4CXdfUhK-IBYY8cOwsUfeEgHNjSlZO6QICeH9VGzAWo1tf3GFR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOGjBDdKRlttInHV24HDM6i8uf1pFsr11gMDiHGUB4RVVeP68c7VL0v1oB_E3XFiQkrBhrxWxfcNBn6BPDXDAgB4SZryfGlmkn0k4M9GYJnLdMuByw5HZTR4CIgGpFbHwtXMma5bk-sLIQFf56wJXKYSkPuFrsA1d7J2qb69oszy2T48lXqmus46ImmczM0VcLIT7QqHEmQamPO67W3av7k2ZBSvUNpmQdHL_UC_RWVB-7EUYWgljFMban9veK4cvgVXp_mf5cOlgnztfhf2vGM-a5rcokK_xgmNNt8uUrNQQuPuaXQRDnVngnXbWU_JgqEzCkiM83B7ES8tsOe5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3ToYf4sSV0cDMV_M0HSrM0I5k3E108uq8P3JdSlPx1oWIH-WGe6ipRrdU8vAS7Dpte-Y7KQ9HOeSBWI5GuWQvq41YayFJE68yxq4x6EJL-dUtO8etWgkwkoZUKEGNIDhdhrqerCyXl51zZSuPUJkXS1CKu-Sif-xfa9gIJts4_ki-smMsim068cGRrdOd1Fq7z2mp-vWqblY-RW1WVurfPqp3rJ7TmWtUFaDCOs1X4PdqWGK3RTAwzfo2JlZj7KxCyAl_yBJMhDph4ZI8XBun9zyh6ohfPwvy4G8YJs3iZHyFAUKfpg3bjHBdBUEsSILxjAZHYzyUZsuEn59cnK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg9Bcdvz3yz2lTQOdUZuDATpR0RzpwV0mo2WEkkE67twZ23N4xyA8rR0k1UWWWiLvQR0O2Dnzpli_KtwHNRl4dFZfA_EniC1jfm7zURUlCtENmHI99sG-7FraLYvdPWw_3lZ9aBWjE0-tWvmWCKxVy3SvAyXxA_EWxk8GNYWprf2KbHNWdjqtLPhtjxxMwt8983sSoDs4l0yTSi_DqHge3kX4AF5DlFwb8gLDc0umHEwnKRp1yWUwPlTu-FS0s_InCj95A-gFk3gzPI9MrALnHTvpE4KccKlf1aAsp-XSo0-if2LN7xyGp6Hq9rC3yO5dOpxJdV1Kscf1CCqZWQcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=aR11HLHACQqL4PkWV4427OjTgrhy-KPH9VqUZXBgR7PkrVu6Q1XHkJyDGKGUo8Pk9kZqAxtkmS-bCI5tMqoQ3s3gL1eVNRL25VO6tKqHvZ-EBUGvoSKV67O37nniHkMQEw5FtCoBx7vz7aZCql58VmKjvhhsVrJBmfQOPl_Ni5yvwbWsyhwr9aD9D-miaUZA0bGxgdA0-pHHoDMcYJcoEpgjT7F6w8Xq9yYcoATjfKTCzDSnyg-ee6cF-e2LZQF8VKQ8MSeM2vNIRFiFke8vYCVFyuho_1MQ0wQfYYw-yXP06YDg4HJ7vnAt7kRQ0dKxvBCkS3nJwTd1o8x_n0rQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=aR11HLHACQqL4PkWV4427OjTgrhy-KPH9VqUZXBgR7PkrVu6Q1XHkJyDGKGUo8Pk9kZqAxtkmS-bCI5tMqoQ3s3gL1eVNRL25VO6tKqHvZ-EBUGvoSKV67O37nniHkMQEw5FtCoBx7vz7aZCql58VmKjvhhsVrJBmfQOPl_Ni5yvwbWsyhwr9aD9D-miaUZA0bGxgdA0-pHHoDMcYJcoEpgjT7F6w8Xq9yYcoATjfKTCzDSnyg-ee6cF-e2LZQF8VKQ8MSeM2vNIRFiFke8vYCVFyuho_1MQ0wQfYYw-yXP06YDg4HJ7vnAt7kRQ0dKxvBCkS3nJwTd1o8x_n0rQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFZudU6UV2mupOwlKdynO5fEn1JbuyyZKzN2ZkrEmpAMR-0zYxiBsVVnbTPig7h9RE7r56Txd3tvygBJTdv2hs0oGvnFQXA9d6vniswbrQ2OvTFPMi7g1GoJngZSXyYQPbhkPonimO8NUlMuFKATNz8OesNJGs0pLbsHSilSrLjofUdMz62khWXHQGLSRbEomEPvVQYsWsR3bVrn0rPtKrZhiBfzLaCvwZFv4KQ3JC2jCPAkKYSfAaLaNP3DiviInDKRlXynEkuXD-GX7mVLoAiXSfTveVTCxWDutmGw1BUsSbEirX0nPMyX1yMqWOhGrcRsPQc5pXLmJ8WZBpCv4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOjo3EC5Dx8fE3_1R8RURhyD1Y4JW6NbjC_TIHBj2AutDfnA-roNQxLbSxnGxERYYdjv5IAeIVmCFqmJ6nRlmay2MMwRRZ1OWsXM81ovmPKu3LJiJ84iqylwq1_hciazUdROfUw78BxPblKJjUunr4fth_552xPXehtQ1nxF8Tj-DX1VHMHVU2UIKXdZchH5ln4JewOpMs66Yule3nVRCZirwrNjsJDlWgSYhaWL5caRDrAH-2LSZcHbSCmz-GAwprZrqamTWrddnj7-gAIPMDwggv8FoZvoyIB_ov0JBuQo9aPgVi5-ax7G45-MomnCuA5_jeL6nSamdX49sdGlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=igi5jsUnTuASNl3-hUofZ4pDOGA5_XxMDwpvn6H9Ga6hHuYgWNGJOuqi9YGbWgoV6zb2Gz2wJBHp46KCpu7hYdgBxjtgp4k6K-k1qn66HW_4Ym2u462FDhmJk7lmZYtqDyrMCq2wUeJ7p-qB95jukhAEjEFzH4Imw7h-hvac_F3aX3WkaGr22TXnPwGvlGnOemSbrWeVF7df7FBr0YW5ZgEyN8J-BIVUvfwYBikvL88GZJFwbds7tHj67GSOpzSn37wOPurXnBQ_T5kOkkNtW2iESGE__S_by5bprDpkn5mpuhWqUPhzi_77SvyA8UzMclsbTefzlKkwWM5bfkKmfC3-oHOSaLQdQwFfknLRBHpjEO_QzeV0RaeySZDXR08luXtK9DsUVZbaAH0mWQ7FRafcQe4249utQrGIsTVj6hULpAxIplIOgBFWPvg5pS_PJoxYgdaw9GvL3__i7tBVHLAoaT5np8Mo-GwpRXV673Idh3i2XvHY5xrgAqgCPMVaXqHduswE2X4isqEIjM_3-Cq-J7C0cK2lHZjil4aLA7_iQySDJ-bWCp7VsfYYJV08na4n4-8U6eA7X84bjGRA6F-IHAz5_6h0MtYpmaOPfo2SC3asAL0vjy0aINMI8cqdFeBdclft6H9X_ApUd9m1hWZZp8oFIPSARS3vz4y89DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=igi5jsUnTuASNl3-hUofZ4pDOGA5_XxMDwpvn6H9Ga6hHuYgWNGJOuqi9YGbWgoV6zb2Gz2wJBHp46KCpu7hYdgBxjtgp4k6K-k1qn66HW_4Ym2u462FDhmJk7lmZYtqDyrMCq2wUeJ7p-qB95jukhAEjEFzH4Imw7h-hvac_F3aX3WkaGr22TXnPwGvlGnOemSbrWeVF7df7FBr0YW5ZgEyN8J-BIVUvfwYBikvL88GZJFwbds7tHj67GSOpzSn37wOPurXnBQ_T5kOkkNtW2iESGE__S_by5bprDpkn5mpuhWqUPhzi_77SvyA8UzMclsbTefzlKkwWM5bfkKmfC3-oHOSaLQdQwFfknLRBHpjEO_QzeV0RaeySZDXR08luXtK9DsUVZbaAH0mWQ7FRafcQe4249utQrGIsTVj6hULpAxIplIOgBFWPvg5pS_PJoxYgdaw9GvL3__i7tBVHLAoaT5np8Mo-GwpRXV673Idh3i2XvHY5xrgAqgCPMVaXqHduswE2X4isqEIjM_3-Cq-J7C0cK2lHZjil4aLA7_iQySDJ-bWCp7VsfYYJV08na4n4-8U6eA7X84bjGRA6F-IHAz5_6h0MtYpmaOPfo2SC3asAL0vjy0aINMI8cqdFeBdclft6H9X_ApUd9m1hWZZp8oFIPSARS3vz4y89DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=Ym-ai-I73x3Mca3BwDCWV6J1ha08zAtyEuu3Jf3RIBHTfoz6AwNDr87V3hnfSzaXFrfVacirQFL7sKnI_Jv2M4vlmkhG3w2O-dQJbYhOrELUu9MOygZXuhcaKmXjUwB62oBTiOZukjSrXZpPxIGtZ-JeHGP3CAlihjWncyIzt2oADZCv9XAlR6dz_aQntipQkjm_f2pmdUnRZhRcjWGhPL9lEarIq7OOnUobQea1Gs-65bL9Abi-3_oyWJF_C05QWZ9QuTKuFaMQHklL-RDOSkbmdYc240cnSkH3JdF_370AiX5FozJy-gf0vQbNCAGwaOPGVnEYyk0W2Qsv8LEuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=Ym-ai-I73x3Mca3BwDCWV6J1ha08zAtyEuu3Jf3RIBHTfoz6AwNDr87V3hnfSzaXFrfVacirQFL7sKnI_Jv2M4vlmkhG3w2O-dQJbYhOrELUu9MOygZXuhcaKmXjUwB62oBTiOZukjSrXZpPxIGtZ-JeHGP3CAlihjWncyIzt2oADZCv9XAlR6dz_aQntipQkjm_f2pmdUnRZhRcjWGhPL9lEarIq7OOnUobQea1Gs-65bL9Abi-3_oyWJF_C05QWZ9QuTKuFaMQHklL-RDOSkbmdYc240cnSkH3JdF_370AiX5FozJy-gf0vQbNCAGwaOPGVnEYyk0W2Qsv8LEuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KChT2OsVg-Lv1RUOFBoT1bPWEr3JAsZjqIEZPzoR-tpVTleLO9Luisb8Neu-rWcjzHwUMcFyAtfp9sgcZXbg6ldGnrLVcF7getpgH9CRQmF6e63dO2yjEznV4_8gZqITYab3kXmZNsLLYmISwK0sLUQwyXMDPe12knbq_0aR1O3pwj9LYFoAyf28xeyT6aFsVRVc6yF9Fge3KZ9z2t9p5cmtWg2oEh7KspWy7x-O_p5iuWJZBaEqQtzOMd770tIxneAgtYJatYCt4BTyi6amW1I-81XcdzulSoFPUsnL8QFAmt8qvOK5DojtsGFq-f1szeeTNxhJqH2G7hDD0rIPO8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KChT2OsVg-Lv1RUOFBoT1bPWEr3JAsZjqIEZPzoR-tpVTleLO9Luisb8Neu-rWcjzHwUMcFyAtfp9sgcZXbg6ldGnrLVcF7getpgH9CRQmF6e63dO2yjEznV4_8gZqITYab3kXmZNsLLYmISwK0sLUQwyXMDPe12knbq_0aR1O3pwj9LYFoAyf28xeyT6aFsVRVc6yF9Fge3KZ9z2t9p5cmtWg2oEh7KspWy7x-O_p5iuWJZBaEqQtzOMd770tIxneAgtYJatYCt4BTyi6amW1I-81XcdzulSoFPUsnL8QFAmt8qvOK5DojtsGFq-f1szeeTNxhJqH2G7hDD0rIPO8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boatlpwWdWj-5BGzirhMwUb3L_i0jtlXzPDx5wLiXtk0I_IH5uTOziYfh5uBMvhtuG0fO5tKZiMlyZ-TwMpIfLOTli812n_au-roYxTQF87e1Cyif6G6gQuP0Sfe8PMkirxv-H7wqnjYN2ynqqaMKuPpypJB-MkHhqAAaMb6eBgQB1wAoTy8yuIvJujBp5I9q_iQpNdbNPfgDcmLI63buMXywXy45blHxeoa7cirhydWTSg9TzFUby3T4RHPK4BM8LkAOqYmIS9KpIsRddgDsKLV1zHvHODdy_SpyBxczf7g-90wHzutBxiBc52Zfi12P79XnW5KC4mNJPac1RZklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exwBQEKR922T2ryAys8X5Pj2kCrZCjpCyXD53ibuBOwve5wACzNgLuAC7Dfbx_nxtHibAlabPWWNVPU5KulmsA09OTBoQ9ggLOd1QAP2llImBCX7HCwUbf4pYPpD46u6nZQjTYsutnIMsqpWW1KKJf9bd0WLsIPiVaIjuTo-8ANSZz5Z7zkIRMyRP8gzNQYb9ougsyiOaXj0LX4chXoVaWIzFaasl1XokWVazk3nyQ_d-pGgP1D_XhCLA86ExxEXF4v0c3LLPDNFta536DzjYsvev66_us8fYJjXAWGkQEiFL6gjxC47r9pq0Dg1R5OAR6e1nXkYt3uutuUSYLtXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obX5OqLYnLNT-xYUjYZiaSpUspUSpo4aZ89Q7b4N2c4uQN52Mn9g9z6uQhKOYcVm4Yv2ZdRXVKuo2loxT-X1yYshOYj2-F7r3nLOAjsDQuEOPsqN9o-TfrLkZ9HisxBjeJCSYJB2roROBhbrZQ-YRfhSNlqubpiFETqVHH4ED-AcDvWInpC9ttli1BozfMK3doRIQ2BYCPiCq_0S3o_e1d3eRE4o-x_q4MrNzdDPlTFexc6p79EFpZJVQbcMrQoKEfWMQ1JMXhbjTYeYgv22L4pUsUgwlsCFlP1tqAcMJVN5JCQKKzRTJNnhLfihsNHd-ULw2Sz2LhC2cIiV39oxtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=rmLvWVnnjDB30oJlG1b5tmPiSxM3yjNGryXDFWyvxE4D1FFc3YiwSJEQP2TgIKy9Ech6CtHtJRcLq3np2E0_K-fwwXyuFHmX_WDP0Xryf5Vw5b8g0yo_uzMSKUq39LQjohP9IkDhQwEuZfi03yVltvIEiOw7JUGtwtZh4yRYzHitSwtSYHcn_YEA3KLycRAATg9WMh768H2EfRjIFYZcAlgjLxnRBfXK2XZefiGktldGnpn0iTTHbOKLcfy6rF3KMoXWUp5gYivVVlvlrWseZnxxOqaFbx3uYlGxNub4yMKrOg3tH8Lo__N1cLV8GZTsUaACMVJq2tWLMONCJlOvXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=rmLvWVnnjDB30oJlG1b5tmPiSxM3yjNGryXDFWyvxE4D1FFc3YiwSJEQP2TgIKy9Ech6CtHtJRcLq3np2E0_K-fwwXyuFHmX_WDP0Xryf5Vw5b8g0yo_uzMSKUq39LQjohP9IkDhQwEuZfi03yVltvIEiOw7JUGtwtZh4yRYzHitSwtSYHcn_YEA3KLycRAATg9WMh768H2EfRjIFYZcAlgjLxnRBfXK2XZefiGktldGnpn0iTTHbOKLcfy6rF3KMoXWUp5gYivVVlvlrWseZnxxOqaFbx3uYlGxNub4yMKrOg3tH8Lo__N1cLV8GZTsUaACMVJq2tWLMONCJlOvXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPgkT-ls1njbAIVJBbwa8-_BHTX-9kdRpmp5nEVYEJwFUoMLCA4Z667of7beb__PFtNnobYPdc8j5dQJbsANJunuyF0bJ91NECgGioHmteiM0j7J_7_3hvlVqrwFxHDCmuFuylanrAy7tVG9Gg8yh_8PoxjuZL5kVWjT-4b9yWFlXHqNYuxhEnwX5Shw0Tvi3qPrJ329h9BBCfyiZ3ZJriAtveQv0-dY3fk_rfFYnJGCjB71AyY3wfkUXE85QrJrK_izrgYOn86u-qQmKdGwM1qApO3eV6Wjb1ZXGtjSWgLPcXSmlIuwBHvKrTCRT6U913_b_9Si5B8_9-EMa2j2Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppP2pTDZQ0uLsYEsYJXllHsFtTzo6gDHY3d9gYpsqZrclcQqB5QGlgn1QArmmp9FKoYnbkPty7E7PrqTJgxRz4dzXuZeko6QmVbCA0EZy9gVKsm8t1KQU0MeIyDR-ZWmvPpfA7cC2V8SbfzE4zll9FOHwfkUeEr86K3jPjME7vFNix1fWhc8VcHEx0bjiqRH1pdO4me7Rs3_UBxC5P1bMlcjMcoNnbpkPcwdE3yHV_Bcz2V_D8Gav-4hX1i_gnj7B4lCXe9Rj1e9W5-C6nxzu2xsHFu24jK-YIuXcDmMe2-IoyHZPDv1HXquuiWNXsXLIX8BQbb9RZC0SqIwPcVJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hy09UMHmc6-hqxIyp7n5Ji0lV0E6vq7q8K7qaQey1B5biEPPILitOkPMNBscPtYYwsZaIV1uGWQun_6Th5rTCi0It4PxZMyFOJhOawzY8CtnrCrxUqnMgyoapsKLncaI_4i3NPzzHRmohBRNxVZ5Z2w_SA0pLygQpgIqL7137GGYnrk_MND5n2R0CwTjPUC9CYSaNeXmdBgl_tAyNaPmY4S7w_8IOA7A7sM8Ely3_pu1nGqVC5crzoItITnyVSb7JBQDlJvqtV4s9UsJvNvZIoO-Ag6O4S_QoVflaAGLO9xF7EQX4B7rI_fj4xktX8JsZxkreIq5a_V_VtnRctXeMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9w0HnSsr6DjOm_RoXUJ0CqLZfUNn5h9e-gAJQxbduP2pFQSvDEJSn_2Q8Zve3OddA5lmfarL9MaskcPnKpkG6vqxB01nchll_aN31DJmR0-Z07zNUbxvLvtXBua9mtDkR29d386Xo2aBZ6MMQDgHY5Q1_8BKX1ZjM26Q4flBhrnLY3wstzry3On5yxUTVBCGy5tqyQWrsCEJpUhh2C2GzDOwFQfdRE1Vwe46XY5kFraix6Fb41jh6F636WJe3DMrZE10SENDLgiPPoE715dpF9l_GS9qDmpV7N194laXmBmjUgXCwcLA10robJ1nFx_ZbYxUVB6oeBSgOLMKY4pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=fIvivddQK0snw_w6Fkw7T6G7GRbae1C0wD_Oxg6xlNtL9Rv3ZzGKUK0Ut4TXlOKNVEehP8QgrwL2P_aCLlXi4xs1EVIUuwN7_IhMechM_SWQLcMMUXdAWP6LKbNAc_tfSjqi7IgnhXEDvKS3JvJQLnGzGSjvMbyrjgMJ7fDn6KMTTeIqfduXXf0gEeNEqA2QSZ6QVauKgi4MKYGIxgXbjrl0LWAc7bECSuZDVB690f-B4JhO5qHo9diZjkA3zfQrnIKKp-mHtllcRfju_vTbLhc0wOX-DX1KCz6dwJ4nwIgJO-CsHo_6R1LThM545V-xyfoZok5wyCcCRYm93ibKADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=fIvivddQK0snw_w6Fkw7T6G7GRbae1C0wD_Oxg6xlNtL9Rv3ZzGKUK0Ut4TXlOKNVEehP8QgrwL2P_aCLlXi4xs1EVIUuwN7_IhMechM_SWQLcMMUXdAWP6LKbNAc_tfSjqi7IgnhXEDvKS3JvJQLnGzGSjvMbyrjgMJ7fDn6KMTTeIqfduXXf0gEeNEqA2QSZ6QVauKgi4MKYGIxgXbjrl0LWAc7bECSuZDVB690f-B4JhO5qHo9diZjkA3zfQrnIKKp-mHtllcRfju_vTbLhc0wOX-DX1KCz6dwJ4nwIgJO-CsHo_6R1LThM545V-xyfoZok5wyCcCRYm93ibKADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=baUdiK7ir6lHzWv5gTrGw6YO9oW8pFMjzyUJNmqbf9ALOG7Y4Tr2RsaeUpfyTnD3Pet2e--0RY150oGXGJg7O5usdaW_LBBC_C72lLtqHCk1YFR_5Y6ODlGD2ErrIobl9lonrOUlBFBUYkWT69ONWfNqeH7oTOR4Bq89myyWSGHvzdE6gMpnSns1nwwGURO9wQ6J6YvIpiq5Frq_frLyjSyDkRcUeGX1DxvRVEeyWZRWIT1aXx0XogXQZ0XdcSHOzSuTObO6UGPxaGyr06LSmerhJ2E62I36UmLQBeeSEgXG85r-E47TL4-j_GTCTc5LWl0LRuGTHZeGAIb72RoIZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=baUdiK7ir6lHzWv5gTrGw6YO9oW8pFMjzyUJNmqbf9ALOG7Y4Tr2RsaeUpfyTnD3Pet2e--0RY150oGXGJg7O5usdaW_LBBC_C72lLtqHCk1YFR_5Y6ODlGD2ErrIobl9lonrOUlBFBUYkWT69ONWfNqeH7oTOR4Bq89myyWSGHvzdE6gMpnSns1nwwGURO9wQ6J6YvIpiq5Frq_frLyjSyDkRcUeGX1DxvRVEeyWZRWIT1aXx0XogXQZ0XdcSHOzSuTObO6UGPxaGyr06LSmerhJ2E62I36UmLQBeeSEgXG85r-E47TL4-j_GTCTc5LWl0LRuGTHZeGAIb72RoIZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=AnvzwL9nVR41qqayeyk_4ALlMfIXsAl4HddC0RjneDisTkD9b9Umii8bNqSmcpcC9tuLVb2Lqj8m4PdloXIU2OPMmzQ__hQNQhrdSkhu7khHPrVQ3DCg8whd_yLvqOxGAiV40QhUddHGtfO64Zp-SuB8VyAWkt_Iol0HrN43js4EVGYIShv64AoOUzosW7FGi6qmDk0NbSzr76iLX6C5MKozdgxx3HjW4B9udMa_bpHxUzZjrwmsaXanER-anNWwMyQDeoQUnWzhZ6habj-uJKXj4YzwBkohPa_MWAqHR3HqWuuz_4nOB8eW_SPxunblBy3a8CxoU97bTCqRb7PMuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=AnvzwL9nVR41qqayeyk_4ALlMfIXsAl4HddC0RjneDisTkD9b9Umii8bNqSmcpcC9tuLVb2Lqj8m4PdloXIU2OPMmzQ__hQNQhrdSkhu7khHPrVQ3DCg8whd_yLvqOxGAiV40QhUddHGtfO64Zp-SuB8VyAWkt_Iol0HrN43js4EVGYIShv64AoOUzosW7FGi6qmDk0NbSzr76iLX6C5MKozdgxx3HjW4B9udMa_bpHxUzZjrwmsaXanER-anNWwMyQDeoQUnWzhZ6habj-uJKXj4YzwBkohPa_MWAqHR3HqWuuz_4nOB8eW_SPxunblBy3a8CxoU97bTCqRb7PMuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJJd9tHxERkiEd96GeT81VMkWHyD-sJneuI2j-oCtI4_IGG4qiIiSyTYlkZwlKQRUJFAZIR9ib3HeJ6cxP4CcWeeNtt_eV1nMVFqnxnAZh581obHP3quEUiNSya-tJLzv1Vx9NINMUwYxtBkFnS_xLiRGW9RQqXCVAK1_arxVDFNM5ctsEFyK61jBAgK8kR1yHPKnMwTRluqsaesHKPFieInsndGNDy4grgg09vhgFVGpP7oFROGFMFrFlb8TrWLU_BbWADrwyH_QUB0w7ExyJegmh8AW4Dlj2Q5T47olM10TeDAzwud2lqZg2WHhKNM9r4CwNf1OA2rS80N18-CBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
