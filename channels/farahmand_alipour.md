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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 01:21:14</div>
<hr>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZDC12oBufPddG70KmZA7zjfZUPnhmKYUvV4aUS6WINeP9XbTstDi2fAL5aWRr-YoJuu9Z6TCAFJYbGBmaTQMdbB3Bp4wF5luQoxVGSLa372BO7ODr3I2QJRGPYWPbqfA7g_suaQw72TZdKtaaoDP3StWQVm3FlGBiaeO0lv8odXQUDac4f2alQ4XuSiYpteXYxwt1zPkU0c0REjBpftlfyte3n1Ow9HrXbNBDsdP7laTJoPhxF2FRnUPd36KAUBT7b29j2JfhKCGD42ar7uVaxCN35IrS0_42MMisGd9AP76SJozRS4qwJRuTHLKZaqolpmkP1rIOZHmnzGh44-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2jvxndXuOlDQ90AS4zSGOMX9a898jsjr8sv3dRWPhb-jHNTbppzu0wHR2u3nPPCIa2kQ13MAftcNDA5C15hlyvmWitzWY-eu5RHfFcUgM_-OrcUBVGu6QTlicHiP_ZXgZJMYGhUO4IdyB-X7PjZf2faOOJ1FEd4fJObt5xlo9hhALXC2yyvhJfUD0ik4VSFoGM8J2UDoggZ4X4qVj_UlnIDP40Y94GFlWbt62bme7hvhZEq2JH_LbPiEt2y3krTRG5u7epc2cfL3tmq3QG-7bxrQhJo7ubGcsZJqj7U2_MeDTL9sHbZXsumbwdRCtc53QSWFFSSzrXOpRVrO3-ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9aPxx-ivjmeebdwMhUPzMmBWJpkYla_Xuv6QeLWSjWSFrJE7Fwmjw9I5b1cjQ6sjBTkwoFBS5FtEj6_pHYjXXpBxX95jsrcHb1EWMdeTRcEQTkv7X9t7n0eYDRxyV1ngsecIv1Dnf9RSFCG8wU9lG4BXqRLFAJ2PEoBxp5b_sU53LzjLuR6JdV_5673tscO_RQJgqGMd-VktOu8ZCvziRkGq9tDjcsXMr6u7CdIcoenWluSpdFHKQaG--jG4mCcaRrg86CuTCz2N0XfXniMAL96cKLLPt71EgktRMnFBo3zt2VrDMhap-XfekVCdHTPvNEppxJyg0hI-rMmGSjTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWR0F0taF1ctqMdfM1h9so9bW_B3JUxh1aJe1avLLFXw7Cv4Q8CHXQT-ozQseL2b4JnZRRMZEj4vCFos3tVUQ5BIvzWsfWYo7FJECZ81eNJ5Uz-T09_EVmuqlZFdWws8eefhJfMV3I41KD5TaVE1Zc4HPJp-nbswCVJxTlZKLyHL8kS0rW8eDrzLj1FezBBRd4JXV9FfsmKkyaQ1f3svvrO7Sa_vPqIypt47dz-TVpQ02sL9ODKTNwpOh69_uL70Ir6nXbO0xTzmuv-vFyy5Kynpn3zQA_iPCDRLsQr8GGz-qgW0--yYOrmOI6oKD-ea6_qsbJ3dGRlO0lyyhecSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzNBEuvuKFhvosmDZEZD_qHgdiES36oYGgbV82oIecEeS9rGiVpEnZ58AgmTh0hkIoPJmT8MoG45iHIbOkrQOKBPPytH9JaK8lxl6MeLThaq5fjFuDMPS-Ji9sedJP6L8kMJqctmUWORMOWwbatT-q5JCIL3l57lV0lzg6YrVSWAf6ywU_gTBApcXyiw2xJRY38gfhcb-iFdNJCQs_qkphRlLpgMrSon449xoL0WKlV4TWUho_ncX9rRuBl_21xvdWqGHyFxqKW1vBcQbv56LiTLIh_jDplKS7SxUshMfeO1pidEzy5cydQePF1spWz-bSTBZEjhdjkGMmzvFLzDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZscfZsJaB4umr5btkTkFLk0GLF2K4Nm1hCa4KCALW1b8s1rx1uVAcjKhc6yBPpR76vvvzLOegkqjBBvXZHjNoXtwS5SM7A3HPOTS7YKymS3h4qkXGcQ8Iew2SINoWph7yZ3SRtwSr105zKDpQzJqweUSiQFZr_fCou3i1At0M6CASqFiChCSLe5RjnSI8yXO7T7z8VDB4ETNR81-RkYBMUP-pLlkT8q-iVHSj_YsbNirvBAzUl5h9iMF6PsAV_jl6VCmpOniubJg7ZqgaA6kYk5io1yvuP-YHemkqcMloT22NE2k1AboMr5MaNXedvONvyiVFwusOHCQez7u8AEIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYx2mSlAUCs2tXs5xIu3AlIvwGPTv8Fvi-dM91huexh3czIMi5hOWbhQYWDyQ2gjd_chDkvZ78DIrDNTBlrH7TbOg8xYqPyRNZ3lNBiljhamGwggtoUmUTWkUYrTSGX8FhEclXYfJjqng7mPa7TR56_vmLv4mFRrLaZ1cspEefZLeWkSoXbLFd9aZ7K3s0vP02BQpwa9GIXVmGoEjCvisvJS_IzW_gwMHiYsDhs3jWOEpUpOma0WNdQBA5uuHju71r9jCloZPdCgpnI6ijMCMHPro2El6MX3SNQISIl7PWy8BmWjRFfyCIgVgg2JdTJl_yF-veavlvjTCUDXmb-3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CseJeoc5hJk3h3vKBolZyJ8FT4Jl6_pqtQMLt0LUF0WNoYi2KWpnc32CXxBIn-m-XK0iNiYSpQu4zh_N2VN1ERYdl9lOS0HOSZvDkXj5XcDBQOqpMj8U5u4e2_tRKqaV7ZrzuQq3B9DVGxVMq04H5S5RwJ3Xn0nNvw1pJ5FWr7RUGnAWgccFQDomsCJF3t3CwR4p92Gyvz_xV8vZrvvm6UrSde0E0mitXEGo0WVc0UDjK0S1IWeQnHzr8c0s3tQttL6vwS4uSdv_SlujM0ADhn3tBuxPnmCH-iIO-snLAHO1IldMXSd8Hvgzi-ff2iEjDK2gTBWSKGkGqkSSq_4AEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCxuUpgO8MfM4yU4DRmH2BVDrYiCUNMT0APl_OnfSMZ4ogaohBYlP-iGNA87FX2ln7GOcQYPe1gvGiR4npi6VGRBgGEgVlIedppXkMdpfHkuzgSudZwa9bdcsuphg9fd0z5OjP1TaF3bIPCRPQbbn5FzY5EXrJRlezKWwJ9EQOvcG7_2QI7hUCEZLAqSEt0nnhbQuLXl0sFYox09SbpReCfMHsaFeMC-67-otNvfVzp5xknssWynbVwNgDc9XZMbk-DkvXw9XCChCexOIRPlXdifWg9SR4TfXzRj4bpieaSoHrmeyhVcvNLzMuCDWlSk-hdCDnD8yvTuRo4ovb0olw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB-WJ8knb9jYMzDZd3ildLyYPBae_2vaB0Vx9-jc96qpxtL695BdFs5hLCE5iZ7x_pK4zrWkdB6OOUfkD7sFzbIu3gQzYFZWzoHXr9xPFy0kzZvjZCrfkhLAqD3g7mQ77nzWMhsgz0KnifOD6Ze0C-7G-FDtHI9PrL9CHVPXjGdfPbdxvVhAN0c9WiGAUB-b0iHqL3YwOTlkK4VZ_mP1w4dFcHW0QTdT5mc-bA0a0q5S9cDLRwJ62_iujS6b1MGqsz2DRwKhlKPkd-OlFnebjStjMsDCYyLMKSeL59F40CAICDuo36LPy6Cxx5RhGPrHBZ8WLBvtchQ5VqEbpJSQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=kaZNuc6ZWcwvV6VbuUI1Th70FBF7vXlvsoweN3bpG3nOOBoNBHLnvAGkdFB91DVUgYYQpYbIh6hFlxw5AWHxHsYRnEPXnbTiHWoQMZIoY2sp2FYpJO5ilOOVLtTdKFRnRSeKQnADVC9Ci9E51Iqr_2dwCeZ4HagDGiiGgiTqNRQR9Vr9ZNS1PfwNGxcdI7wIZDsb3V5f4XWE3htKrQn77nqv1ElAbhs0Bavu-CHv4FwE6zcK0iJlmoFJp8PjL0A6HE-XEJXO5DWo0Ea7jsQ6em-BY3ZCP4pNKARntKijYp_PxlpnlxrpJ3X44o4sK2-Bt8z_5CxA_WVMlI_3xpFScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=kaZNuc6ZWcwvV6VbuUI1Th70FBF7vXlvsoweN3bpG3nOOBoNBHLnvAGkdFB91DVUgYYQpYbIh6hFlxw5AWHxHsYRnEPXnbTiHWoQMZIoY2sp2FYpJO5ilOOVLtTdKFRnRSeKQnADVC9Ci9E51Iqr_2dwCeZ4HagDGiiGgiTqNRQR9Vr9ZNS1PfwNGxcdI7wIZDsb3V5f4XWE3htKrQn77nqv1ElAbhs0Bavu-CHv4FwE6zcK0iJlmoFJp8PjL0A6HE-XEJXO5DWo0Ea7jsQ6em-BY3ZCP4pNKARntKijYp_PxlpnlxrpJ3X44o4sK2-Bt8z_5CxA_WVMlI_3xpFScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfbIzP1Z8UQMm9JvNeITN4alLIcIdwE-EgnSDMLdHvzHar8jDHmpL_TBlaPq5uJ_57635LmigvI_CgTfGoK8Znpqoh_R12Y0KqYWcdvOUmOjNjzgSbOD0Gyxq8aeKuJzzUMcQdAxwcx7BoxFWNIvJdJJQJiPueBn_eI4DrMUDKYZ0vLXHvUTrziww-Za-MkaewPH9ftOC0CnbgLUJ1qH4PNh2nQreAPiKqT5HZaYnmzCcl1gQbeJUxaLpeIctoGDs7-Hq2SL0U2xaSXeS4RPiLyFrgz92tZy2yuLfUa_VYlH24DDLJ_Lxbs97iApf4WisgYBh4nujUX3wIz2JOjUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca7ODK3REBo-2FYlpn1W-_moQYZB9FguLE-0q5mKT-iyhs3CiydGxInBOYr0bzd7WIeNyaboINyxR-vX6MshUhW4yOol_0pbM8r6Vz0SwkFPUzJ83X6DBdIQ5TszHYgiKrJzeWQXcnHT2FALyKdUUiAyavoLA4G3cS3j4IGg5eTSHx_57xOZlx_HogHRbwsgrhLLo6IYg0BHjLjaZ2iKx_oBaHkTtyWjyGArQ1wYOgTdQjxoLKiVNeOdbxkUERtbxoUmY_HRDqRC1q-NqZFVgvjTepR6-BseGuB8KIQdGI_ODyWAEzWOZKWngD7Pud5dROP5R4hPfVmXsQU2pC7GvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUYM1sZQfG843lpdx5S3p91i42AJEdcVCJHIiXkRUwW9hrVVajxnPkvtHCQkG3RahPTInd7yu6m6uBCZUaEkj-n9d1yX__aa8lFLcdReAe_zBaN-dKJO0qCjVuttT_FvCFmG57jkoH6ILpfVEHiaQ1z_NrcY0cT0v7oQvgxI_St4ifm58HxRBQOaymGQFWZE6fseMdwZs_GAdgC3CeFS8YZVG0VNenP9dQnNERZcsL5Xsqa9HZCWYoHqdbBF_snosukyQD3P-TiUsgCq3e99V4n-OKTyfY75nMNBKPGrr7cYbg1s3VPGUlOzJg7mo6HI9g49yEeifPvK-T3_Ve7HvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmheyMTLnT2rmT4-bzMHDK6mp9i2cJz4koRVEpj-VKspxbbdJi0uVTLBrRe8v5BGv5mp59lFR1YE2bDM7fwvTLRSWNoZM8FiYJ13c2DcTvPhi74ki36t1H3ygOU5j5B6ISPDjoGnDq8RmH0W8HjUdjJMowLQL2vxAl-UN9fO8rJM-3jHn-eqhWGO6BKACxpZj7GXidr4GtM5S6APPEhgcGERkDPLNBRvqNl-TL5pqL6x2tdZJvz-SzIbKt4ys41skXTSfkJsOnBrQd7ZzDZ6SEFxp55cnXOolqzN9DLtmNmU3EFM57tzSZlk_4dbCV4MhjUhGc2vLFRo0uVa6-wtOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ2A-d--Tzx4mAI3zUnfOVSQERb47QJWYmISpW4woFZ2CL8sc1tfHt-SeOxokxPKZVizXMBtpd-w84fiK0cVs8UGYbx20Xzvq0RBhWPqssEFXXXn7mqUR4aOVIJxSKXV-4eYt8tGBzSSThd2QVz3JmtfK0rb6R1SWccfi4nBdR5_ZuR9edHTK70OJyHUgQS4tshyr5CpliVya0mSLiMuS6-uLPZ1ea8am8n83o-iRnRlrNp0Kbhjo07-m6vKXD_N37i93rzC_lm8NDoTtayFmrR4SbxkAnsxokgQFHlV_RXrKganbXXgdhkwBZBfIjX1NaqKCNuXN9XjRXt3X1RuqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkcGxVCy9MZc5vkfhlj6aUQH0R7vX1rLJt8WsfZggR4ZKqmmMa508quw1kzisXYaheCIeblv0jfY6WOC53J6dqQ3n60oNfh4IEUIWFl093uMi9lpbx5mPe3jZse533BIEgZP94Ba8zFY7wgNsMWQthZdAS9KZZjKqETCiA1C5IkonaNY4jIGuiT-6TEdaebWNXENa4UN8a0SfOoIBJZ81Lg8RK8yvQgvfBEUQr1SsR8rW2wPTSQV_ZgYJBNINE1hcPmr_QHSiWBawvjvecfHNfrGL2dGkGyfdrUeJUP5S0kA2Tqv2yCkBXiM8BrwMcitUvPf0j9_n5U12oXh4YHi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-uKYO4OrtoHMLSj6U8F-X0FRB6tC8IGmHzQBooVhUi_Z7272HM8aMu3dctGhsDrUpy9QzK2jtDDh4szC-lTkFJ87lYrgiMt9PUp-N5pfQvCPGUfPV_ElKXqBsSNlbsTLq27_m2yDIomcVD7qMqSDKy59HzsiBSUvOjRWSFx-hJ7QmwhsmQIVExzsVdtBfNTZnRtklWehiKEvGl-DUDqEl8T2A-rlJIaeH0iSU6z79F22BFK5xNL9nuGTTVKjnUEUl2WtTD6qFiGy-OZwLfh21fEjOHztCIbWeAop751VjstQ34NXbVO8V0O2aTq5y-i-NQrhhF6bHIHQr9JT2RfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gfwn8WOJ--wUykz6v24zdXQe50BHbzjZmzUdi0pMuXMRMw76ZdFZ02Mdq7o5si4MuFPSQ-V6EondQ7HTbiU9tr0YS6giljp7FyESqk38KB0lYwEIQzZdPSkUEVF6T1hXnNFprMvtxWQoGx0unpVKc5bNyA4u2-ThYdvngFx5uccwCedw3VC5ky5QRNrYElM2j4v1jefchZaa-w6p71EhYkqbZaSpz_Akx8CoTT-eDXNZmlp04UUZGaYsmilLPKPPWdVY6x033Y3HluyilsP8zhieF4jTNK6VH5Ey1bsxVwMIYCoS4pdKP-6_XUQ29DiHBTWIgq1tE6TZKGtdwnJLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEY_LUqMEN-V4vXinRmP7tUlhpteGLU6P7OrL564l2fhfatjzxYNlcCkJHIsyicUCCqQfp4ilBI7xhAjnAegETWnMBZX15KiGfB3u9fbazr--39QOGq-u5qOTYxbfcrJMRcsXQD5IutMgO7d7NT0PKvdJPVql-letNAOwdv2D2hemPtSjdYaCJAIkC4yTBzFGe2a4mfGqP9UHTouQRnlVIaAev74FZojviJi7SRcLJrGlXhMArDIluIx_W-QWSYhvpxcePezdZcrADBK2KG_AUhGcer92LUezOCm8bTvyuiGANaLvmh17lXgE37w6yUrK13s3YkS_mzM-0DO3k3Pqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gOEWRVIwYnd3KnUpnjtrraVmRbB2ms_3PXn0bKT-IKD9_1BrVHOXD-UH_uapKb7JGQLrbnIDqLtp6Mw8zebIx54-VPkU-erNvTZezzjLVi6nflGYUxfmHGeIfZ8nHbluaPUERd5HFj9a3YzdHVdMLGP4UQIOosMA8b6zLBgcQsuBzj4rAnlck8tHpfnMnj6fUf2zHiJv6s0CGYMRr2J-xToO2C3rOUEEDA0VOPnStyN8ttah1YXDniq-WInWKfWGU5IJLGb1ai1pTHogDSBd9BVWErfjQ6-SIV04-Tin4m9SZvjHhYicfiGC6pmOwSkQ_3gewB5D64CO9-7MGJ64wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLZIA0KtXZSW8GLK-OqKIIal_1qhkVI2zKfod-sm6ErUvEPxBChbDubfHcIObgXfqVC7CaU0QR0Rb_xe5N8SgbmchegpNqObUp8sbHXMzLaBzP40nSwijf5ZWHJGTlTrxrp-Z9KFyDL6YiLB1I9O-V06tM2n-rFQWLiZAW51AcLzEaqbwRTm2QLELWhUVQCok5C9FrLQu7q6ZDNVTLtGll7LCB7H8x9z6DYYb1gPiFPlU9xfrQ6UxwJYkmsIMiJuswLcgNPj2SC8mi1S6UwoPW-TdyTYGl44jsEGDYctEbb9XXeFUHftevzh-_xspXNR2VNjRpJPXq6l8WH-sCha_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMyxQ9jhPyJW-cYdSqEsxvIGM1AEeBRSO8BUWXXj8qpRP7v9NN4ZGfymcTsEpsQ_tn5AtzzBNPaQGH6MedzGOoHHiUHTesUIL13MtShTGVpjkO3_aFuBtyQzcUFty6nm30pGS6_LQRu45MriI5IaQ0SIjc76tG7oCjjYaSFULG2xH_y5EKlqZImlE5gcVEgoF8C7BkRBr5qNysW1jGrUYGBmgURdylSg5_v3CmDb8BZDPbM_7mKcN2q2HqRRsCuOf-UZsKuvIncd3ldZhe5XYO2UM_9nuOhU-bkPD60Yq7PKk-AuYsnJbbiI1kN37FfsUYNauuOM1p3dbIgaAb_YgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-Gy0wiBS5Si8xWZVtyGfxTwJDuJk5lO3pL4DYo6pI01UQ3uONulNSYbtFwANk2wlCC4wLi1_p8gRcfZAPxmJIYmAgRF1RKZa5b0PcyJl1S8fRhhBWM0wKlRRhzcVYIY-xWkzWqXutulMMCHpJ1zHMRIy36ytXuTRjWJETKbNdXZB2ik96ZsldfCAO_lF4MGzX0l471VuyPraF5f52ALiM49AoAKvi0Me2wVjwe-HMFDZXjA8MQADd2JumnhwW7T2S2k5dt82cLrkLMhS6KTsOotY_71MzPnY7S_ppw1Q2Hc8I-cT68nEly9nusu6ZBh5uPKOni-tGaQt_HMi6DcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiWOlvKhhD3CYPl72Pb584XW4hjWbFyO72A6bsgyDT78jXTyY9R9bSkkQgsoXQNTq22xUZjrt0k_ruVFOWHy-mbzp713HROLYzfZHGVX8CeB49dryTjSLgfLVLGukPn9h-PIvDAkMEjJpsnnHbw7lSuocEKgSU0oZDuyOFA8gpX6MpiHaG5CRLpzbkHH9Z-OKcmvP9NKKjrn_L-EGLGin2WyfjYnTmyPwWnSd9j3CpWHl_6_Yaw_NKChlGHcMIWHMssya9mxN_SmeUs0fdw6MMGblbKtbmf9Lk1bk3ZUPLXtVmNOZyh45cTsUDuzRc9HQSwub1SmeLljDkLpIZWvyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuOW_dyUvsfGBE3m7Uz_41t7as_0I3AcQcXxJoXPanj4PdKyoroi1BpbmPGMWJyczo1gqg50Gm4W1OwmtIF3pz_JtImOT1LXO3FI4NOGYl_cPT6bGombQjyQxnQ1oKBaojF2KFu0ozymXV-rxWy6mYQLlmgneaN8QZLdJjYDdFEMcJWxlUHNrrQ0W-vTFD3hrW5JYbliL6WEk4yefxwNNVyrs2v4B7kawJJ0e5liz6KIS79gIAvno8FjcjrTsbm6coreuYUq2K4hxkZ391ew5u9k5La_dr1jnB4UQS8Y1ZLD9Fant8rRRG6pPItCn-eWsT4e9AJSiq6Mdn04Fq9mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TK2THHzQ7CofGyh91WuINmnijOMgUQUvcUjiTr0Dpjk91wyb837OsfWguMm84q-KVABWSOXE1OgA9qRzTflT2pDQsNhzr-9IXKd-ezzyZEwkeBiUzL8M44dHSI1GTLehrLPwSaD1i2cnwqLzlUBaZhr0BvH4nhgwUEzJIMu3o26H9lu9VeCg1A8NQACX-Uov_d6gjxS2R2SXotlFudCr8C4SbRB8ZGh-aRlSr_vwqE_kWhDwLb7sJW3Evp7eTCJUVdKr7A6uXGuvbkLB9fEfAM3A4x5kVFno8kPJIYHEkVxMjdZKgqpmBHTrNb_rKE95MAW9BW-Xj59CAX0jSvBK4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkb_8MQMB7-NdO-pZoGtGnsszG3NhK00JSHcZCGSmzdjckracNXPXP24ai1gAcIm3_c3pWQCydoZe2NrxWIPV_mPKPURoS6q5Isty9lhmAzrcngWxHdJKDcxp4HzZaOfIP613DFqllwvjKR93WDDH6fVR0cc-wPGY6trq6ZEXXuwIf1wQ-C4mqeFrfYltaan786S8x0lcUlUUjx1vJSRKbg9TF-AsBI8t0lXhbizn27PHso-tfxxchK7x4ZKtT9Dw5sBY69sbkhXl60tJ2akTXvKZbL1_PjTTgHmBt6zrFunzlUjifejqqQiqNAaGad4MZoewAjuikpvmZ7_oRewyg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=FltjegQUW44NEwRCfEGwBdD6rKFj0nB846KMYcw4k1GlZ5VJhBslVQqFp2ZLnStxU5OA9SB0uGDqyaL4Ko76phEgoMnrie9lB3FID6u8xmtH6QEELisTFGhD_XJ-PTVCMy4KCrPaFQr6ZhGBknbsLeBLdhi71GabFXt1ld_sbmuiHNEE9-n5t0RzXTpGab-FssIlUkm4-OK4BkTyNnok05GRx2unbBdS0tW2kuwT8a_YPgcXoghctWlNaR73iwcYoF-Oy_Zj8OMZDCvzzHnwY3U1EK-AYrE3lxb1Ci3WLJnOVsESEDjFoFSwwGrrWnen_1BPJBH9w8rXBqaViEtutg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=FltjegQUW44NEwRCfEGwBdD6rKFj0nB846KMYcw4k1GlZ5VJhBslVQqFp2ZLnStxU5OA9SB0uGDqyaL4Ko76phEgoMnrie9lB3FID6u8xmtH6QEELisTFGhD_XJ-PTVCMy4KCrPaFQr6ZhGBknbsLeBLdhi71GabFXt1ld_sbmuiHNEE9-n5t0RzXTpGab-FssIlUkm4-OK4BkTyNnok05GRx2unbBdS0tW2kuwT8a_YPgcXoghctWlNaR73iwcYoF-Oy_Zj8OMZDCvzzHnwY3U1EK-AYrE3lxb1Ci3WLJnOVsESEDjFoFSwwGrrWnen_1BPJBH9w8rXBqaViEtutg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKr3KBIHvpe-Dr8zxxzGqiSRFu74Qb_2gkHUhz4WAQYrXVgUfiFtuHq9fJHud2K1RtgXT-RCRNy1dArkJefhgvW6kzCnxJx1uM2cwqYDeSogqNR1YDBfdxFEj8P47QkA9Bi9q_-2OrXmW1sXsnVNDYvc2GzYeTrV2loxD6K30KVbdUHToMzMOFLD5fVDJZjC_Ghh1Lu9CNlphb27KpPNkCJF2WpGit-zSik6sYSS7FMc_lTvlUUVJtWT0xQRdbNGm8diSG5EoSvIO1pOGeN7goZFCcSyrBpNuWwYlf6x_Xhw6VUjvy9ztEGSGZJsTvj2q3Hgt_dVLDw9oXN0xqx-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThHuA5VAM08iuaxdirHXRorlkCMMwEbffVFacOXYD-CdrerhA6T4FGB52CTedDsMOJMNcP-GXzAu5IuLlbKDXfu3QmJNLjziMJUxC8O8ypOvT66JANMusdCYKQ1Va3zaED0rgGitrqN8Cp2TgvrisuGw51Y7O7ueMbSROYDay6Cfv18lArHq1lMYDmOjCN-9SKXKuuZuEdQsyEuyh_n51wberNSTTOyQYcjhAacWidsLw_w2wJVo1D_8azwz2Pbiu_Dp_bJciPiZ5r6YnNyh2Isr-SZKwEs6jtvv0kbEwVlPzaP4U6jsbN26C7V9g-u9ER_kbwzZdfTwMkIDGi340A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYXw098EzYYHwQVHgzf4Qs1O8IIJTknr5LcWmFNXgPRqiOFmECoROdJIgaM1VQlUQ-3XWBpr6hbLIU9xFS35JDSyNNRwK6rQDI02ugveUhQMoplJWSvrsTfnfwLbuD_iY7AmQV0QQHtjr3F3ah1_2JUrkVN6njbMK2CBkf9X8l7nNURq1tmxO10asY-1XSLKWRsKmKdLpb492WAc5NUPeNDovQ5WdposmdjHMrmoXfoTvThakmwC3SWttlHTU7hH336Rhh-NgTfO93FEniHMf4avYP-sQ2chHOTO40hjaVyti4SbdCDUtqq48k9O6af43Kq_20usllFw1O_-v8qu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=t-nHv8vQ2d3pOZ7hfD8_Z-yydBwABn6FZKAFdFd_WBCmZnzbnvgi__6cOKa3q_SADTjKB6IYVLXo4Ckv0NRLPRSJlOG61N2jlIEgalRFpoIFikub2z0cT9AhdHi7acXXcj_G9qTLtfzp-LGsLqVJDr-gmFpwiYBUgX7e7mf16XgRKqXKaehhed0CufOivz6TUzCGVvpLJkXQQF32cLqtedXAQZC91mMBKIDrgx7DMKiTKXJe4nvJlj55pFlZ596FxvxbwhHfoPXaNMjIbCvjjN8r2j36b1e-Fp7-NbPUCkElsTKDzQs-2jdk0PtoNsNDnZnX7510vSYZJQYC-tp1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=t-nHv8vQ2d3pOZ7hfD8_Z-yydBwABn6FZKAFdFd_WBCmZnzbnvgi__6cOKa3q_SADTjKB6IYVLXo4Ckv0NRLPRSJlOG61N2jlIEgalRFpoIFikub2z0cT9AhdHi7acXXcj_G9qTLtfzp-LGsLqVJDr-gmFpwiYBUgX7e7mf16XgRKqXKaehhed0CufOivz6TUzCGVvpLJkXQQF32cLqtedXAQZC91mMBKIDrgx7DMKiTKXJe4nvJlj55pFlZ596FxvxbwhHfoPXaNMjIbCvjjN8r2j36b1e-Fp7-NbPUCkElsTKDzQs-2jdk0PtoNsNDnZnX7510vSYZJQYC-tp1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQfXT579oBj2hlfFh36tgvWHIPqMS4a3Ann4_CgEh0Uc9_zTfXpwzBOCD_IqyX64_RVMkwIGCJoAN_pVCaXuMBj-UEuW16bg5nFV4U2YOSOsdp0P7COOq2o1s5ycl-StOAib1Z-9EI-EAG-iu0wP0dyVz77Wr9MLzXnbjObNWpVrYkYJycMazML6sDZ2XT557argc0A7SR0EQXxLio5Ey-NpxNHt4ZaN8B1l-UU0GZYvgtYfdCWntMrDeqrjTw4G7PWOlCZXbXapkr2tXFOYkxH6QQ0NQGPikV3Wu0ZF0Q5qJ0Qm5YEz9snU5ZxpLyKHPXRb63NpcF-vDd-qyiG7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=BOMLfNS7Ct6hhjm8KXRZIuUnlnv2oIRT9ZSmxIMkPiWZKpbVpkxXETtgzBOUX3TfP13ckiNdtwZpAItCnLPQRu2i4Gkr_X2TaPhSzbtlZxxKZOQBlz45H9Y5FODBMK68dVyjhmtuzX7_tV-7xSDoLXybI9KKRNHp5vzYEpgenJzTsxS2ttUSeQ2BUkVeBNSLDyvAbBa78C_l0D_L6a8n-iCqm5cXn3e3AoFxdefulMamD-SaWTziA5Yf6wNeivQtOpfeQWa57m6S9lnLixbWZNXYREcsqT0gq07Am-GaG079QhJHleiQekQC2YWXSXpXuAzynfrgU4b4InVWEx8xCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=BOMLfNS7Ct6hhjm8KXRZIuUnlnv2oIRT9ZSmxIMkPiWZKpbVpkxXETtgzBOUX3TfP13ckiNdtwZpAItCnLPQRu2i4Gkr_X2TaPhSzbtlZxxKZOQBlz45H9Y5FODBMK68dVyjhmtuzX7_tV-7xSDoLXybI9KKRNHp5vzYEpgenJzTsxS2ttUSeQ2BUkVeBNSLDyvAbBa78C_l0D_L6a8n-iCqm5cXn3e3AoFxdefulMamD-SaWTziA5Yf6wNeivQtOpfeQWa57m6S9lnLixbWZNXYREcsqT0gq07Am-GaG079QhJHleiQekQC2YWXSXpXuAzynfrgU4b4InVWEx8xCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWsp4vG-pbu6OllAWWOTAE4v9FW9c2mOSNTiL-8Dd0Ua9MxKHC8sTHSXb0eLTdTqE2v7aFsvdCRLAFR_vn-_kxr41j3gDbuyvCK0cEMHQs-ye0EKOutfhkX7NoSIVBO9v38BjGHU3VaccmjFO6J_cOI6J0rZikGgh1Ck9LglKKMZi-zyeywmDRn-MCLkI2btkAHMoasX6RFOmX1VnuuR7gConkdy_GCYueG98hDI4VNquAN4qLC2zwpZzqBiFVal75lljd_bFd2dz-ZYdxbobvMOo1kQQtI5Ukh-hLeDQ-RTjC-WyztuoIUpFEJOAVN64JJy2sbJVZmGIKP_ZJY2iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fs1A8H72gQP6n6D91xojyWr0YxSmgvNaoc5WO2bfrTgj9XE8AnwylrZ1ymoQjnnmWB15JRvtpA8hlBox2ANhSO012Yk6457BiS1LDY1F9qd5fx6KPfxnLKVEWPh58BHEKPORXofB4gA632SvoTjskBDORIzz_Mk9KAqDUfNbiHQOoGe4EUThh9txpFPDIpL2zugV8rrlGP_B4BGE2ZPXwpcmMIQg5AfuF0v-92sgxUJbJSSTIyUMShtSXFYxF4W1OH64aM_Tu-tBiPj5GR9KShWSBgPxZPQUDBaTIPDXAfbJhH0pUhlk1qzrhzdB3_fT9fSP81948kyZLPGJWUUtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=bUTxKgZ3STU9EDcQYMZzgShujXE7HXoAnBAQIrIGXwZEEAxLmwsT4Jvdap0md4bmYsseE1QW8fCBdKETzVif5OGVc5Syizy2xnpyc5BS1tODCrB5zLXpaSVBVXRH9orBRypyGccRyBOn-09dGev8ZegkkUCc5Cx80TOhG7WcxqtBhINbIv0YHsFC33sV5nFhMAW0QU5s4qpxb52iQr8Pf9ZkLML6KvJEnEP1zjF94KrQ7R9Skj5Avbz7HdCIiw6bw0ZP1rt0mRQZz29A3b_Txo8hxcpLIUyz5veiUFe0_7iUAUnYznOCpzci2cA7eZjYfjL4sL9R7jA7RuNys0gTbkWJLPFzea5gI-onM7B7KlF6ehn_SLSfOvF5nrz9EYXJ1wp64VcXPGZyK7KlGJlxJ7D9d0FWUFhMYwwqXYxNlQMrVKUdlz73zegKzum2nczECCjL2SWWj5-ltxLGlLzbojZUwbJ_Y-yn_iwOlY21-bLLcAdYSI8AwldmLOMgsmzgCG6s_GHBkqRDAgiiD7qbgu1fwaHBHLUSYk_HZ55wl-JtoA7suR0w_EI1Kzg6odsbDuaRMBdB3X7RX7mprBEo4bpG2Wdeu2SnBeQn_B-45NYLxuPvolPY9aobWpzKJsCMkEdrqo-DmfgbNcbQa3QAmdAEj-2_B1n2shTIjbL-600" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=bUTxKgZ3STU9EDcQYMZzgShujXE7HXoAnBAQIrIGXwZEEAxLmwsT4Jvdap0md4bmYsseE1QW8fCBdKETzVif5OGVc5Syizy2xnpyc5BS1tODCrB5zLXpaSVBVXRH9orBRypyGccRyBOn-09dGev8ZegkkUCc5Cx80TOhG7WcxqtBhINbIv0YHsFC33sV5nFhMAW0QU5s4qpxb52iQr8Pf9ZkLML6KvJEnEP1zjF94KrQ7R9Skj5Avbz7HdCIiw6bw0ZP1rt0mRQZz29A3b_Txo8hxcpLIUyz5veiUFe0_7iUAUnYznOCpzci2cA7eZjYfjL4sL9R7jA7RuNys0gTbkWJLPFzea5gI-onM7B7KlF6ehn_SLSfOvF5nrz9EYXJ1wp64VcXPGZyK7KlGJlxJ7D9d0FWUFhMYwwqXYxNlQMrVKUdlz73zegKzum2nczECCjL2SWWj5-ltxLGlLzbojZUwbJ_Y-yn_iwOlY21-bLLcAdYSI8AwldmLOMgsmzgCG6s_GHBkqRDAgiiD7qbgu1fwaHBHLUSYk_HZ55wl-JtoA7suR0w_EI1Kzg6odsbDuaRMBdB3X7RX7mprBEo4bpG2Wdeu2SnBeQn_B-45NYLxuPvolPY9aobWpzKJsCMkEdrqo-DmfgbNcbQa3QAmdAEj-2_B1n2shTIjbL-600" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=RpvkH6NN-_rPtT1wnqg2pBpWfD9Irxkp9H7RHwnaNbZ0jCNqtByGmdXQQaU4ixhpt9q0nUQ_TfaKUR1LFhcQTSWDUJw5_d6HqZ8fdiAUkcHeWbVmtHV-cR1e4vUEgaepO6AwyyKYZujsZpGVN00Hr754MWgWQU4298GfpeeDT0P6tuXhUoF0kJka3wX5JDMcDLIWegBIYnmvIOQWgSV4bkPnInTNX8UBTyTdKRr4DQNUCaqbDN7kRuX-_Gfa_FYY5AbgeF_289NWGfvLalCKogkiXHOCM3crlb34r-u2DHMqnRFJt3T4MrG5yMEMTKgsrLAi0ECMGFb513cw5E6IeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=RpvkH6NN-_rPtT1wnqg2pBpWfD9Irxkp9H7RHwnaNbZ0jCNqtByGmdXQQaU4ixhpt9q0nUQ_TfaKUR1LFhcQTSWDUJw5_d6HqZ8fdiAUkcHeWbVmtHV-cR1e4vUEgaepO6AwyyKYZujsZpGVN00Hr754MWgWQU4298GfpeeDT0P6tuXhUoF0kJka3wX5JDMcDLIWegBIYnmvIOQWgSV4bkPnInTNX8UBTyTdKRr4DQNUCaqbDN7kRuX-_Gfa_FYY5AbgeF_289NWGfvLalCKogkiXHOCM3crlb34r-u2DHMqnRFJt3T4MrG5yMEMTKgsrLAi0ECMGFb513cw5E6IeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcLesFiLNh3E-jkIvW3KkdE9VlBJQqwGiCcAehaRe9q6SFTuKZxaZKJg464knvIQMChqkqyTv8OkRLGtWUlJlma1ECdcfJaNA5sD4ltxg4FjG6oXMYidS6PpFAb15V1KDjDdyk8JQDpwS5PhhS1QC94Lp-HpAeH_pK65fB1dzXJX6F-VjhiCeQuzpqewBWJ1H2tA-TN-YjVKUsi_LO1qYFAco6chp8zMWGxflx33AH7T12skN2XM1s0QAMQZDKjIg2jAwb9e1IYl3XsXPJs7SniFWCnRVr6aAY8fcecXl8gUqnLu81-afu9tyw0iOWfSuJMjFxH4uOAR045k0fcz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=UEHCtz5UvT-03cZFvfBtntPB5H4c44Nyzr9nqzK4Znn0D81OiSP02P4yl23qaQju5ZZmehEyQ2fRhTdTZiCkQywfeIerRa031Z86j93BrilddpcKhND2AKOC6dkrT1w7Akcn7FEtaUkNfv_BpxhKE5x5fpCPU5dBAAdbdtXM3pPoYXq3ugxHxEYUJR3k8zgK4zccGq2kndH6YYsgeex6ACRJFGS3kP5a9kTILlFj3Qg7oTbLlvq-TOTlL4jIKGPmepoZCEqfJF056-rKbwYuj_SYlp4SStZU6cTOJo_fw1MO1ctuUaHbT9zdJIrJwmbL_SVH-CKcK03QmDC01MQfKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=UEHCtz5UvT-03cZFvfBtntPB5H4c44Nyzr9nqzK4Znn0D81OiSP02P4yl23qaQju5ZZmehEyQ2fRhTdTZiCkQywfeIerRa031Z86j93BrilddpcKhND2AKOC6dkrT1w7Akcn7FEtaUkNfv_BpxhKE5x5fpCPU5dBAAdbdtXM3pPoYXq3ugxHxEYUJR3k8zgK4zccGq2kndH6YYsgeex6ACRJFGS3kP5a9kTILlFj3Qg7oTbLlvq-TOTlL4jIKGPmepoZCEqfJF056-rKbwYuj_SYlp4SStZU6cTOJo_fw1MO1ctuUaHbT9zdJIrJwmbL_SVH-CKcK03QmDC01MQfKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIzpPJ6dYXQkOmkJesdp5OeyKPd1c7C4k7FNkD-YIQsjLKtmBNJnuRyfO3-dIEbvsfg2NKCdOJ6lMGLcVvboEQ5vLBMxmZETzTFrfUlBzY7Gwr8BMz3LkSmU7-fwoe7mpFMWADqTRcQs_BYRJrOvQ8RCXTSjNZ5WvbZnuq5Y8S3MATDyhdfVRn31H7SSeprpA57PHhySCeTyFBVVK62LwUZ8i3VSt3uL3LUjQJs5RC2IyFz9bjNXXDd-mccVLE6RI6HqjX_0d4wwJyjupaYiTSJiaAbBQTirbZGKQzD_eUcK4edIqreL2WvbYryXBRXeGQeadycGo6RWF8naaBa7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgPM0r4NAXPqAeeMb4Vp8OalOuf-QbSuKH1p_hVvg0Zhv0BzneyN4DgX4SX2D-MZZqBm-lXvDy9ACPIyASec0SC6BhcCtTgrQt1WrRwlxu7HCVaLZ2epVsWbZzq9STZOVNqkBUB0vt4OURl6wPPQyNkAyu9ZsTcLidZjKsBqem7W22mD4YOFRtzN9Jt_3UNSNvSmaFenm87sOwzKqfrMAKbaT8flUKBj0KsuLkulkHEIjbhZPrO_t9Uh4aXv4qQncZWPsclvJzQNdFLMoYD4hR8UYFcYwK-3nU9kthktbvAedYg6BmNbG3xns5z_GgwvsjsLO8_m1WFBOWxHEjR-5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgOGiJZ-dRQF2l120aJX_8RiJHRrlw8ZiIE5LCXl12hnOhiDXcZFtof7PYTosfQnTi5xpN2W_Z4LkVaI3YaTHkF94jjE_NoLAZcGc1tz2TWHs6d_1oHKl5kkbZEL1ngk3pPvXtZvT7JScDNXxla_amj0vNaIfqwaQCRKFUh7fo12z_Ca__c1PoNnRtuXtoX4vMUrrnNwVeHpjQHhW2ZKSWC5R5JkfEid5fMwGLhwOSkBXWV_YgG-2wY8AbXqGtllr47ze3LXJH_nbC5byKUOgBDPfVMgXGdAHXzSsgDWAlEvNkHMWiqR7i3u_h-3nWZp_S0WhOGijqbShHmGDrAfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhaUeQViATW4oM4uugcMvo6V9gslVSZw9L5uq8YzXEUqyLTgdsMRMwi87590795iN-KmDvy-F1BjSvf0pFXTSO-KGqxmTRO1ZggpqJ4fZ6gyeyJJzVG2mIofDXnMZljGe70_QaZe6tz5uuo59g4C0YPdYnVCe0tORnLRSPVNE7Re2I_p2P-niOjMRtAXtl9XKky11kip5aYHF3KQnroBjTY2Mkd1eb-Ht4G07CKnpa-fB9yVaUUnRVDBHeGr8AHajXx6-BJYfu7y3Pg0UIOKr62gyKJwcu0yNVfa6TkDDQfumjJULNuV0Whxn1zRAyi60oTGht01c4RK2TzytGjzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVwyAycd9qbOUk1FwEKpxNbmAUV3qsB-OHo8nFdlHyZDN3UQW5zJZxfIRPkM7zKzvZlEsQ2CodkwuqhNi78fye_-7gBLqYU1oYD5WYP_npw7sypGq4V_UvLkxX_fExDizSXrtQs39TCZdehnxGFPF-1Oe8KTGFo4OZdFFWnmhE18YacA_ghyQdM5MrpHQT3xUpkFvs5wW92Ib1u6NqLJLf4UiudYAsLt5uK0v1wNWCONqck2Q17Q6U0A1xuViT9UYubLrL9nvYF6xflnqfY-WgZd8AFFF0K99ORc0Jt973-GiqepfhO1hIDwkSpz-ssVqHAnf2Ug3CerxR3gfNwodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=EGdtA0VI3b_3yaTW0tOTjqsdu-rpeycOLLjfZaq2bvQzG9po6G2_7wJRHNc1Io33MN9E4_MN1fQTKz_tom5Ubr3Ay6NfGLn0DCsh6RnThtL6JoEPeUMZhBBuYX0NfQrVZH41ByD-UTrLNX_ljBG6Kg9pLnz3ole29KsvGxSx0IpKNzO2VEAu1JDhmDKjuK2GU6lugjDyCysI2BPTVkd6Ugcj115K_DBxu6lFp2MlVOxFePqZ4jugOmBnnw1UzJ3a6WKkWqdEg_6QR-e4pFoPRJWRiXGNQTh0a-j4KvIKsyA-lFSvZSmib8s1P3VTQuN7EDNyxu8PA9Y8y1q-ukpzZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=EGdtA0VI3b_3yaTW0tOTjqsdu-rpeycOLLjfZaq2bvQzG9po6G2_7wJRHNc1Io33MN9E4_MN1fQTKz_tom5Ubr3Ay6NfGLn0DCsh6RnThtL6JoEPeUMZhBBuYX0NfQrVZH41ByD-UTrLNX_ljBG6Kg9pLnz3ole29KsvGxSx0IpKNzO2VEAu1JDhmDKjuK2GU6lugjDyCysI2BPTVkd6Ugcj115K_DBxu6lFp2MlVOxFePqZ4jugOmBnnw1UzJ3a6WKkWqdEg_6QR-e4pFoPRJWRiXGNQTh0a-j4KvIKsyA-lFSvZSmib8s1P3VTQuN7EDNyxu8PA9Y8y1q-ukpzZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZVuuazXjQeS3bN2ucm0TfVVu9FGXSAcpzQQBOzpXWbeV9K5lB_C6w0vrVKekpu9BYsd-bwmhBJR6jHGKep38sA-0GsZ67LMEwRRpY31rXhdpyKt2FMuWta0_03M71JLORcut_3ikuhiJ3rsGLo4grLMnF3nA4Eh4x3XkouyvsK0AreKZSC9YVN_eOxulfakJCTLm6D5sJHJ3jKBADj3n3E8mzr-iZSPmv1sy3r7lIbiu4BRQkTNEWeTkrJwGXZHbbgTJbraNykePWtV9b9UfF5jTI08INsfnM3JrY9hBua66ta5XnVQm8XWnTlVq9iT7-iBuC1O1HxdK_DSE2vR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9X6NtvgvDisgLQjGpB2ZAgZWzo8VTpxPiAifX697mtZORH7zYW0UTmf5toAYV3LChp3sxyh8JcrpAzfATK_bxjuoN9TSfbtu9lkr2gtOFmstKEfZvdv-1pqdNMKK5ZF_GdoO4kn5H96h0tbnX-o2l7BPI5tCAlQRnYLpB87AZ2YRlccAITsYKrJSYn4_pnRjsN-EzNQg5NoQ6Bp9uqnfRXavxI460lV4JEN6J9ITaXBOEtsYVEmGVg0J33d7g2Es0Ykcbi_nSpHXBysYHyTcOkx4VyrhPIVi0SLvz_lXTKzmKLrKFdEYu_MF388OHWDUibLgYPVdEKc9CHKRv8HCg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=FxJtdI1sttQmDBr9qmdj9eorVKKvjc6SLmV5UulWjhOnqJjpfrFy4rWIsggdfFZKb8swDNZB1vhO4GKnjCTEADpdKgOqpIi-U28M7s6jdBHcb0UmZ2NIvFpAyB1O8lpE5rrDJVAK0WUZIrIpkbuEbpvmIy5ABDqXk0vFYQvK3vDJ3AhQbOsbR-brBVy7TU5_l5IotsTUE9qP2PjHKJMfn6boaTOwiXD3n9x3mF9XXfhIBZ4XVD0Dys8IUhVtbHw1EWOTL1WhCbwhSFdbMqEtYapTNqEfbEPK2uW712dr254FmDaNcVN6xOLVm1jXIlHek9lF1Ep4-hsfstj6p80wgA299cz6T9K5Tj7GB-5urEEMPBXQP5wgRWipYL3CwwnP0wKfWF1mdr5eczhw7LivwBx5vaPx1n1jYysLpv98ouV8Hto859CtKaZ8WZg_f-I-TZn9Fq1LEiXm-i68kBhNxS7ZAj_suWZjKlk7RKMB8NdaglVnVZD4VH32DM_znV1qfeETve0bIsmoRmB_acrpRV3WnylTF4b4Dw4cHbcAabup7a_Pab0jBMZaMuxO0zcMJVpEIk00bl6I_4-O9OTwNYdGrndFBLlT7LMqZGA7-O8uCiwKDEp_bVGDX7H-FvWaZy3pDD3a2ooKxucPskOVnbkzzIAIFJ5TARFN_3e2Ovo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=FxJtdI1sttQmDBr9qmdj9eorVKKvjc6SLmV5UulWjhOnqJjpfrFy4rWIsggdfFZKb8swDNZB1vhO4GKnjCTEADpdKgOqpIi-U28M7s6jdBHcb0UmZ2NIvFpAyB1O8lpE5rrDJVAK0WUZIrIpkbuEbpvmIy5ABDqXk0vFYQvK3vDJ3AhQbOsbR-brBVy7TU5_l5IotsTUE9qP2PjHKJMfn6boaTOwiXD3n9x3mF9XXfhIBZ4XVD0Dys8IUhVtbHw1EWOTL1WhCbwhSFdbMqEtYapTNqEfbEPK2uW712dr254FmDaNcVN6xOLVm1jXIlHek9lF1Ep4-hsfstj6p80wgA299cz6T9K5Tj7GB-5urEEMPBXQP5wgRWipYL3CwwnP0wKfWF1mdr5eczhw7LivwBx5vaPx1n1jYysLpv98ouV8Hto859CtKaZ8WZg_f-I-TZn9Fq1LEiXm-i68kBhNxS7ZAj_suWZjKlk7RKMB8NdaglVnVZD4VH32DM_znV1qfeETve0bIsmoRmB_acrpRV3WnylTF4b4Dw4cHbcAabup7a_Pab0jBMZaMuxO0zcMJVpEIk00bl6I_4-O9OTwNYdGrndFBLlT7LMqZGA7-O8uCiwKDEp_bVGDX7H-FvWaZy3pDD3a2ooKxucPskOVnbkzzIAIFJ5TARFN_3e2Ovo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=HjlattSm6hofT9XQvPm2OwraFhVbL4qwLDUb8Uimom6n9fkP_haSxodm09qG6qlHTWz7WfnFTqJiLK_Cd--zJldQPWnQ1E9AmGad9O2jz8zRacctZexZEZEBJkDYwfw1b_TLxF_boZR-qDR_KAfZN-fbFF5Q0p9vKtOOp0qybOopWq6-O7i_FoJpT-j5pWctCtKT-nJVwDyomkWT6MWuLG1rZXjqigoTPsbS9Y_tsAsv1t9EsRk9-0HHDNLE-UV_Pdm0QTqkD6BV3C2kQqOL1deBe_zlAjR3oLZ4mBQFLhA4CbdTkzgaYGkL3lxwNgz03HX1rRuqlDfSP1LukSkBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=HjlattSm6hofT9XQvPm2OwraFhVbL4qwLDUb8Uimom6n9fkP_haSxodm09qG6qlHTWz7WfnFTqJiLK_Cd--zJldQPWnQ1E9AmGad9O2jz8zRacctZexZEZEBJkDYwfw1b_TLxF_boZR-qDR_KAfZN-fbFF5Q0p9vKtOOp0qybOopWq6-O7i_FoJpT-j5pWctCtKT-nJVwDyomkWT6MWuLG1rZXjqigoTPsbS9Y_tsAsv1t9EsRk9-0HHDNLE-UV_Pdm0QTqkD6BV3C2kQqOL1deBe_zlAjR3oLZ4mBQFLhA4CbdTkzgaYGkL3lxwNgz03HX1rRuqlDfSP1LukSkBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCl3--H8f2XQXZtYDaogW5bBVfEVoRdSxMFqKcEpPHMwHwgjiU36BCajNOtH1lNmc9lsn79rqHD28vHsqhvLeHyPHTS0LKIu0nmYxbfsWYW4MDHBhDjdRtZnYP2S8L9J9DlvVAUz-B8Un9LgIlSvbW42P3lATg9BsiyabVQC0t9jKs4b0Ifp41A3eyDfNq8cx00IkhXn3ZsF4x9hBl_yEitvGow894bJ1vgDt9_KVaiM3OjhFyXsffhzLHVIuJY7ftLRqJquJzXK2qnxhkT1MD8JWrdJp7DVo7jYddWzJ1_Cjy9VjCL3jjlNiueA7fDFYe0lcuAERDDcAlQO4Y-B6w6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCl3--H8f2XQXZtYDaogW5bBVfEVoRdSxMFqKcEpPHMwHwgjiU36BCajNOtH1lNmc9lsn79rqHD28vHsqhvLeHyPHTS0LKIu0nmYxbfsWYW4MDHBhDjdRtZnYP2S8L9J9DlvVAUz-B8Un9LgIlSvbW42P3lATg9BsiyabVQC0t9jKs4b0Ifp41A3eyDfNq8cx00IkhXn3ZsF4x9hBl_yEitvGow894bJ1vgDt9_KVaiM3OjhFyXsffhzLHVIuJY7ftLRqJquJzXK2qnxhkT1MD8JWrdJp7DVo7jYddWzJ1_Cjy9VjCL3jjlNiueA7fDFYe0lcuAERDDcAlQO4Y-B6w6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGEL6LTU8zy87XARxofrm2LVtU9smvCbzq3dfR8xq-rGKvEbiPXp87vf8CZ62ZPct9bEV-csEtMI-3_PF43TJCmXpizq-xJchhO5XqHKvb_ksny3Hy8WvmaXpKfar0U9k6_ZWonvjLzMwO71HG55k6TD0lTqda7WuMjNiyFTrPipRAPYp9kwqdssIxkA9pLuOflCO-IoqLE195krbQ6JidEfdxf3u2Rg49Z3NVb2OJ8Ko5_2n60BIX6yzTjHSbxtKu_T-Vnsojk2HRjc7-EuL-QCNNgUrBJZMsQQiy1uxj-jx8uXYsS-jcd885zmXwo-4fPAceibVgMwAljDH9nR_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8FDqF-lXUSWMzqqe8CZ4FxlnuaTN8xG0PrrcWqC1SmgL_Q6n-Y1ugHAunlktx7fW4XhTF_fHlGurdyS3CrdpapEKpz5T8IStVRP8GIGA1LxtvIkl0HVYlur7zDlwvk4jz9ePqP3EymJ86trMn1klxD_pDXzr072oyUobnjW9LTHYvEcJnBHrfO0wUuszacmSvywkuklYVBVd49bm81K9fpcWbtUBRD6guhFSrEhvJQSyR7wlr1e0bwWRyniR6p9f4vYl9gX_YVWJahsKmplDB7NS3urZFHqWzYJNs4POZm-OsrVkw_vep6sDWFT-EGxMEc0P0waeWbj_ORC5lWmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X55vZTea1jfmMjLqX6ZfudbqxnHLBpXmDJ5ulZPv3I3L-cXGvm5PeNM9QMjv4KpS17D_NgpOYK2GDiLptgHMe10bMhTI7JsrDZwXKeiHtkITMi-waeF5YSfip7PDRR0biMlDrdgQ0mW0Zcltc1DZ4Ik80s9pSu8oVwLc1ACeka3IwB_JdoFgvipkERuJa6ud3R7t41qaiw-8JhZdYD9Dtpgj1N52YjhCQTNRRb3JfUpDXHevSA2k3QrYuZLJRIyzhjX2xTwZJ0XAMa466TYfTmNArYvx4AkrKfx9mdcQiI0WnqFOaExxRVNoDs3lJpgMWEaWXCkMLLZA4HChZj0zeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=cyZBl-EFA2SBKkPTySCtiCBMPM8PIpBEPPbZIVRA6wmcr9OxkT7KI1IMhqwmfzXpioUW7myWtrqdyLRvlPMHXBqDpc8EeVnwfw8hKGJeO9Y6g2fQwWTo27ZHsWZhjiUbZ9G6QC1a6BL_jivVVuUFrpQwSReWaH6Xd5yr6kCSNYx_uISwFPWRzLrFP_odSsCw65WfEMNsqX3eyQuuKYdX7hep_FreD0vcUbs_L1Hvb1lO9NgmZRIwxsYleWAIqQJ9TXCR2jFOVdcmUO0r-r3Q45PrCJvLO9-wjd12Z03DHDtWiJ-hfukYH7j5gQYmsGath1kL3Z1aJLgaXSU9DkHQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=cyZBl-EFA2SBKkPTySCtiCBMPM8PIpBEPPbZIVRA6wmcr9OxkT7KI1IMhqwmfzXpioUW7myWtrqdyLRvlPMHXBqDpc8EeVnwfw8hKGJeO9Y6g2fQwWTo27ZHsWZhjiUbZ9G6QC1a6BL_jivVVuUFrpQwSReWaH6Xd5yr6kCSNYx_uISwFPWRzLrFP_odSsCw65WfEMNsqX3eyQuuKYdX7hep_FreD0vcUbs_L1Hvb1lO9NgmZRIwxsYleWAIqQJ9TXCR2jFOVdcmUO0r-r3Q45PrCJvLO9-wjd12Z03DHDtWiJ-hfukYH7j5gQYmsGath1kL3Z1aJLgaXSU9DkHQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQq8aPJK0ph7b9aSJLB4-matWqO_AMdJZwPsonDlh09DHzvwiKNZ5mV9Q45Pb04SRofHmrmFtgNVDGAOSpueybMtHZszQeolgxRhFwQxpD67EYjeDA1X4Z3F7ESK9bgu340rLOkJgOaw1qE0YJkZjoC5pbm6y-1Jp9F2Aq1PJCMc6Ct72-Uvgc1__VzVSDMrkKwkG-Fck4Ja253A54KydXnW-pHItFWdG-CUcL8uFEgRH9w-sT6pHU0qhMMbx0UJlfEtlfIHIJRpuLjKpLJ2-UvLvluuyK1s6fZQ1GZ-N9A8nXEuhiicLDDCBf0FGNMsOFMC2WxJkU5wK3NECSzGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyfKxec-r0kVclFozU--e9nkG1iju9e85Dea1mcj_DdUPXxNIXGsapjYdqVQ4C6DNGS3hIQLgXL_O8S-2b_5FD-0PzD0L37OVk8ZuAswhEXiOaD76PTS71j5Q-sEHq4eKun1Yy_vLKZIQGEDv-NvqasRvWgwBTJ8iK3iZtrWlJ0OMU-u7oyW1h7H8YOOK5k8TfB5DL_04Wqkpk6lm9jN0zHfR76alUHnM8iElxwcinTTbQ7GPXEPHO2a9MDAxja9JwNI3KRI9XmSV-SUXQtUM4DtKIxiK9sTOFTTQGdL7JUZXycbmJz1aOhqpirpDKWFiXjbfxPqApAPowefQvi_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6fhRrDceYC_AGvzytzH4V2wYOmg4BLmHM0mFTbB8PIfKieZ8OpAd2s9PvQonkQeBcqg_O4EYaxcG9-9HdL4TuxjZM5pAnrKYj_rQQxTCbJ_UdsVbXUYgBqYxJFCyPAR0nTvQ3I9hGqLa7aZ0f8qsyn0aI_ZjWQ3p6bFxbb9FU7R8hsO4u-zNjC6strCJAOe6P8fLN7R0O9d1TN5BmId4mkllzOoaBy8xfRspDyM2jV8S3FDUGHGt91ryAiQOMqQZXWGAaj2HDoNQaYGXtJmnMeTiNeYPGWkhNe42pyOWQRDXBzC7vxWX9PW5XXmWe8IgXY0PTsTclCHsNTJ2jfyiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP9uqW9Iv6_af5U8WkYQnjyM8EMPWrLhup8OX0Hi-ECil6kSd5124DiOJfiOnF95Shhqz63QLBMuSbt5y5574rNOMyIOKBFcXo387dcTAjE14eyULD2cUXrpg_3aHE4GE_e_2S24oPqdtjySUfC-gwYKCWL7iZvwMHuOdN4hXIrRMmEQ7ed7lw-JVoZMzPr3w24qzfM1XTSvi9nza_jcZ9glAlx-bxlbdMJJnkAr9te316hq5EqP-KMYt8OD-Mhylkou_b1MtvRIquQ75JSkz6Dz31O4jDfhAktf2zHp9c-AsF7GJbopqe7MabgCCOQt2moRk3rQ2OV29sr0-oyjzQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=hMCjyf8kxDfi0rYwMoCbHHyEJqk3Rggup1maZXJ9gZSJi_7m9FiQQxTyvribzTMal-SmGj8mrpQjH3JfbW5g6Xv2mq4XV04-pEcDJG2xfOU8xGXWlYp6OgY9C6tPWzfqfpaYdrl4PzDm1THlNENpN9ailSsE-M18jXx1Vsj7nV6hscvYgs1k_V30cQ-_OknEDWMASOWb6JO4hgoBVOGYhezaNdiEPmdA5I85qvwrMzR_47cnlmkaYzkZ94lGj5mhFXGhQiNLeBZiJP6IX6p1bkdJZgH2eKLIFRJ-wGo_Ox_OdLSTq0lrnUZ3V1niEl-WMD48Xewf-DQ_ddqUIv5pJIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=hMCjyf8kxDfi0rYwMoCbHHyEJqk3Rggup1maZXJ9gZSJi_7m9FiQQxTyvribzTMal-SmGj8mrpQjH3JfbW5g6Xv2mq4XV04-pEcDJG2xfOU8xGXWlYp6OgY9C6tPWzfqfpaYdrl4PzDm1THlNENpN9ailSsE-M18jXx1Vsj7nV6hscvYgs1k_V30cQ-_OknEDWMASOWb6JO4hgoBVOGYhezaNdiEPmdA5I85qvwrMzR_47cnlmkaYzkZ94lGj5mhFXGhQiNLeBZiJP6IX6p1bkdJZgH2eKLIFRJ-wGo_Ox_OdLSTq0lrnUZ3V1niEl-WMD48Xewf-DQ_ddqUIv5pJIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=vvXjNfQzv1Hza9p9WUxGMjrRQv1dWhG_HU91iFapY09CHjXbEaqmIIwbv3lQ3LYXAeLSQjw4kaGdhSC4rnxy38S8IvBTicxuyb5LuLVWRzX6GwSzHqWB-V8UOnCw88YUyIrGp6-xL-cMPK6axzcj-CenRvmA6A7axwJ0ppWZ9_y90b1EzR3AjNpK_Fe8xuwXb54hburIshJXkIVrBofdNZ7HnANo12MatncFSVx4ckH_nQmTluJRP4E6ut0Nu_nO3Hl536O8UvcikCiEwCX2xRj2VkaQFHDcFdnPmWhuD6-iiGUL45xgET3bE7STdpJvzjad4j3e-sZyj2qHtENotw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=vvXjNfQzv1Hza9p9WUxGMjrRQv1dWhG_HU91iFapY09CHjXbEaqmIIwbv3lQ3LYXAeLSQjw4kaGdhSC4rnxy38S8IvBTicxuyb5LuLVWRzX6GwSzHqWB-V8UOnCw88YUyIrGp6-xL-cMPK6axzcj-CenRvmA6A7axwJ0ppWZ9_y90b1EzR3AjNpK_Fe8xuwXb54hburIshJXkIVrBofdNZ7HnANo12MatncFSVx4ckH_nQmTluJRP4E6ut0Nu_nO3Hl536O8UvcikCiEwCX2xRj2VkaQFHDcFdnPmWhuD6-iiGUL45xgET3bE7STdpJvzjad4j3e-sZyj2qHtENotw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=sBek0qyPRcoK6sPHh85KDXhqH-HTkkGJG4HkGkVfQwM-VbfmWfxBKYaG0AX4J6AB0w9TBT_-KMs3rHCSzHwBT2qcNeThkGoaPqpID1bmUEfsZf1uPP3eQuaqCM290Jx1obIyO8kYvIZRvSykBAa0R2XfjJUFQHMAj5D_YRIdNYXImPJuzz2G6Cz6hDCp8P8qWIBAKnov87zJMFtyLN9MUhc0fDeMs_fJOLDt3lv4qhmyNez08hIEeQIkCyL9yhx5UjF5TFcF0hXgbKnksx9zHHZ1KctHzQ8EKXhmrFJcq9gz-39FS2bTzpJ_6EBKDWHetZPEHRj2eaIcl6BmcrFi5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=sBek0qyPRcoK6sPHh85KDXhqH-HTkkGJG4HkGkVfQwM-VbfmWfxBKYaG0AX4J6AB0w9TBT_-KMs3rHCSzHwBT2qcNeThkGoaPqpID1bmUEfsZf1uPP3eQuaqCM290Jx1obIyO8kYvIZRvSykBAa0R2XfjJUFQHMAj5D_YRIdNYXImPJuzz2G6Cz6hDCp8P8qWIBAKnov87zJMFtyLN9MUhc0fDeMs_fJOLDt3lv4qhmyNez08hIEeQIkCyL9yhx5UjF5TFcF0hXgbKnksx9zHHZ1KctHzQ8EKXhmrFJcq9gz-39FS2bTzpJ_6EBKDWHetZPEHRj2eaIcl6BmcrFi5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY1B1PucpbAEov7ikylR8Q62H-ZlNL-I-APFPPg5BKFBPNMl7Ql9nR4Q3Vk_Jm_F8LodQedHHIRt_HYSDCHOZ3AcUHtFnPAcCSoL5jOC54EkthGDIYCvxKz0Vuev9opsMCkWGJ1w5X0ep44ndtV_hewhugtViB9l7XDyye8aJ-uiYHt272Fz9jfDg4KoIgf5cHQjZM989eK6_a7m68igBOxUV_nbKyCfYR6iRxwZIY_jLD5kk4ynmn2xL0cDt5wuFKMk29UjDEVjRc8wsIb_z-AhtodgZeXW-BIbWYxBLMfpsZiodk1HoIUov2Npt1jyLW_3s8MClZUUibYxp3NW_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
