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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 20:16:35</div>
<hr>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6tZNI3quD6nOf4FYwG3c0IY2VbcbEn58ULE3wTKPRplKtlbPi-7-8jS87Nu7mfOLC1PXCLHhS5zvhdfOn1AYqqK6A52-Cskg7I8hKO2DfG3kKdu9UDaECpeMX612XIwokr83JnET9ZggRZdtFhR3TzqZ-atjSD372m9V7GpSpm6gq9N2x86WX3A4t3xoQuF-B4hjVFMGfkep3NKgLURoD4e6pvYwnGC768bLTIIYtmDwYbN8TmIvNc1fodTbDN6RLZ3Q-etuzPdgkWnvbopPj9X4Z11Lmd9eJoVWh4hDP9t7fPt1aMvfi5J5BDBm0-9llB8QcZM1daSiHq5uHyAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jut8cQceE433CeJXf-9_g1_bIv0qU6giDxbpJgJVvXJbKl7UTJPo-DfH5AxDhgKeG_G32gnB-Oziab_FB9LLyGLQMIVS77wMRSQBI1wvzoX3BwIcePIUNbjDYY-UlaEM3ZhFPMfLav9CpFHj0jAeCM5I2xPghcSwhUmha0tou9OuhRGZxtVGlJjPxOhkyHKTe-2-SJqZp_WK1Oknw83qfab6U8WDLQ62SgFrrbOMRB6RNfQGFzLlplSfHIN6yM1kGCZld7aey4a9kMhapREtb2FIiWBrOX_y-Xv5KEvhkQLMzLb3EULX4PA3K__lFA16otma-1v99gtygWBggTGeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw6bpaBhOneVqI4HAkwRI-n4FmRNhSz5954foGCsGClRm5ldPNG_Y0VVx8NxSvl8jqIkKjtV0aNQ9gmyWeIg_Zg8I2Xsk-sVGj5eVUv7yBGfiT3ouwFd6PDrDice1397dgubbvOTPktnVliKyLVkzhhlXzGWrJCqtCpmhf33P_3RVm5az2yGYtRipgD-AXFI491fnACJKYMAGe35SLKdoWXgjIzHNICWy63w580RNeasTSnDd218RWxRBLTzg4XL-wgTESVKJkctWumhAzDFoEeAtQDMJyjnxy0vbB-kKBFW7TAoQ64Wxgan22HGAZ9I5uXQOR47486KiG_lhVBZBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZDC12oBufPddG70KmZA7zjfZUPnhmKYUvV4aUS6WINeP9XbTstDi2fAL5aWRr-YoJuu9Z6TCAFJYbGBmaTQMdbB3Bp4wF5luQoxVGSLa372BO7ODr3I2QJRGPYWPbqfA7g_suaQw72TZdKtaaoDP3StWQVm3FlGBiaeO0lv8odXQUDac4f2alQ4XuSiYpteXYxwt1zPkU0c0REjBpftlfyte3n1Ow9HrXbNBDsdP7laTJoPhxF2FRnUPd36KAUBT7b29j2JfhKCGD42ar7uVaxCN35IrS0_42MMisGd9AP76SJozRS4qwJRuTHLKZaqolpmkP1rIOZHmnzGh44-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2jvxndXuOlDQ90AS4zSGOMX9a898jsjr8sv3dRWPhb-jHNTbppzu0wHR2u3nPPCIa2kQ13MAftcNDA5C15hlyvmWitzWY-eu5RHfFcUgM_-OrcUBVGu6QTlicHiP_ZXgZJMYGhUO4IdyB-X7PjZf2faOOJ1FEd4fJObt5xlo9hhALXC2yyvhJfUD0ik4VSFoGM8J2UDoggZ4X4qVj_UlnIDP40Y94GFlWbt62bme7hvhZEq2JH_LbPiEt2y3krTRG5u7epc2cfL3tmq3QG-7bxrQhJo7ubGcsZJqj7U2_MeDTL9sHbZXsumbwdRCtc53QSWFFSSzrXOpRVrO3-ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9aPxx-ivjmeebdwMhUPzMmBWJpkYla_Xuv6QeLWSjWSFrJE7Fwmjw9I5b1cjQ6sjBTkwoFBS5FtEj6_pHYjXXpBxX95jsrcHb1EWMdeTRcEQTkv7X9t7n0eYDRxyV1ngsecIv1Dnf9RSFCG8wU9lG4BXqRLFAJ2PEoBxp5b_sU53LzjLuR6JdV_5673tscO_RQJgqGMd-VktOu8ZCvziRkGq9tDjcsXMr6u7CdIcoenWluSpdFHKQaG--jG4mCcaRrg86CuTCz2N0XfXniMAL96cKLLPt71EgktRMnFBo3zt2VrDMhap-XfekVCdHTPvNEppxJyg0hI-rMmGSjTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtxaaGa2NHgdANT6h6NVASJI_uCrr1X6OkpWbWA_CK2TIviPIeIQi9MYYFHKuUsTXjpvk_aw3gIi3rLa0ff6Y0NNlI3wHEBrzWoHd3UsB56U2f2lp3fCxKlG4YqQCDPar43PzAd97dUIEZo68MhH8gdcYmSbef6POekZynlaY_8dhhEP_sIAPFMahunBSlhAKjFzFg4SDajTLxbimArdzwLWd5mmG3oJCoGoUd8MAgnMXjch9bVJiJH7xW_i80VfxW_1C9qg-i3j1JMo4aGqclXhmzcwLz8dGYsAnUuY8-UD_JGqKcdIBMIbgkLT2IvK2K8l3JfYr7Vmm9ped5j-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzNBEuvuKFhvosmDZEZD_qHgdiES36oYGgbV82oIecEeS9rGiVpEnZ58AgmTh0hkIoPJmT8MoG45iHIbOkrQOKBPPytH9JaK8lxl6MeLThaq5fjFuDMPS-Ji9sedJP6L8kMJqctmUWORMOWwbatT-q5JCIL3l57lV0lzg6YrVSWAf6ywU_gTBApcXyiw2xJRY38gfhcb-iFdNJCQs_qkphRlLpgMrSon449xoL0WKlV4TWUho_ncX9rRuBl_21xvdWqGHyFxqKW1vBcQbv56LiTLIh_jDplKS7SxUshMfeO1pidEzy5cydQePF1spWz-bSTBZEjhdjkGMmzvFLzDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTkjkY8k_adEeXCdRfO7BT502kHYmUBVLbkhrKxVpa6b8c7qHA7SaGLgezVX_yLY2dg761SRIbtfD8eMLZGxXo7Oq7q0x9MPhgZAZKN_nK3C2N3LavnSCWmwak3ar7PdAMjfDN7lfcIfCihB201JZitqtqxWpBeo9LGjIeWo3d9TqqctQXTCyIg-_SQJYtu2sBjXZBdLnEmgxpuAWMezUvGF_76ZQgFZ_2BZ__6hQARUbLq_506R-YJFr3yN9nOWwHhwgZ0AnMadnFApuriWbsoVT3_yDQGkyl9OS2GX2ysCN-kFzRn9Hisfeqpu6YqOXIdSoOAObTROCtRSS1g3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7p4iP3_7HEJOsU-E6qTp8plL-KtCS3HqGyeaJl4TN-veIsKWg2n2M7yAzm9tHoOkwUzlufQuxyGHbjvKdK1iSLF-fRLZSpNfFYgs0XpGC3_8bfeetZ0b2ao0zu6HgancGnzgpCJICY8LrfVdloZmh30udhmLP_JadrxzzOxy5ScZ_SFxbkz7loWWM0r_vA44-8WKj435uzMCZxzXbBHiLt-HoIwnNv_NVdd1ZBTK67Q1_A_8pJ8aFwSleuVZTsWRM6UKD9_iux1wcbtRavJtwfZzIoqLJ3NLYJwLajchhO-Hh0n0pQraQZZx3fkG7OUilMsTzsVJ6tLwbHf9wSi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6r1wWKWkzVaOCpu_KSfo04HqZCSTOmvr0TTHkftG4WpdCVd1nAAfUohHTaQLuoG2TzvLeeSaJG96YB2c3h-T1xRQQEykKt7TmaTDHMCa2yfMZ4CKJ8j1vJDOQ2x1GllMuwM4gxbMhlVqYKdh6K7NuQEh4NHskMyJCo3y33_gHUYV5TSCJRtSsrxp8vTAOO66RYww43n5gTShzB-vjGY2l1MasXN9CFceT_4k7YsarE-l4B8ALFeCRbXLDLyGMVqjNoY7jWDlbXdlv5hiYD6pKiKRHcC4om22MD7SzzLiT12fCIarDAvYbFZ1lrwVcM_codHpTfFUXqFO4Q4byVPxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRYD8UHM7hRwJrTD2NEIT_qh4hV84gMBlIqa6oezO5n7yawa0NRwTQQj_K_l99rL9X1E731Pw8hg0wBkc54tGOE8WXUTF8saq3pQ4HlxF1izkNHmhc_58IBOpiBhv5zOokjyFFf4alVzzy0Gv1TlzGedgQvqnyMrp9dtNrR9bjGPdN-grPeu21DuZ5W0UegLa09uq9mf_HNmRqpps1QiKWCKRaNWwUfWelz47PV9v0VaeQ-rj9mIBjEDSlUG-2h7HPbl10RqAyqvw9AgK83fMZNiW6SZtpA16vU513PJYvjoQN1UBvCPPy_FZ2E3VMMBaJvSQj3za-S-t2Rzog2Q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO0kqdMrUaFWSh9H7iiX6d-OjD3V4nAelL0hzpbzsv5isQ9xQMxDjTpEWl1yKyi_XkCFwoxxCKet5jpDJqKOxD1zVRzqzc2r1yzFlNxcyshCTBMxpDoYq1IuvsF-_UyJw4JxSsRLz7BJ_DfFaeyacznDZkspaRlbeBtgCj2cdoBQDYbfem5MZC9gixi6uiXLtDyexNCQSW11LHKxnBqTwI5RbNuQOTWp9p7wlTALhvX4QOnyqrX96DiwBdLmUjOSZxpSMcAC3pKg7UjNByZxKEzp-05gEhSFjVzUpbsONfSPuAU9CxtdThoLcMWdSOtol_WMfr_X_qnAtqi_E-KG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=T9XjR7i-SQQ8uLMyQJD2S2rRlqnYkUXI7Mt8RXQM85jePum5CRn-T3pyTT04CKBeJ0IqiOlO5ou-5YfHd33CIWHRsK7BNFOJcVIxmhBfXjPQnhBrmxZWMf6TVhW1zAVsm2yRgp_UVqCs4Gr518_e90q9Eyan7k6AW5ZrLzTsxYKJ6m9bxLrsep9O0qUUB3xx3NYGk8TuzMcG5D55o4XK4NByp2UHBb7ShugIaK8TICamaEQb9ED2Ot2x2EPQRgdzrThyFaAI6UM4MrTlH7J5TQG7VpiaNMHw2ta_xrJm9suOErgzsLHRcSiVKtZveYtsnP4ewqQ2CkjHPokciBZWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=T9XjR7i-SQQ8uLMyQJD2S2rRlqnYkUXI7Mt8RXQM85jePum5CRn-T3pyTT04CKBeJ0IqiOlO5ou-5YfHd33CIWHRsK7BNFOJcVIxmhBfXjPQnhBrmxZWMf6TVhW1zAVsm2yRgp_UVqCs4Gr518_e90q9Eyan7k6AW5ZrLzTsxYKJ6m9bxLrsep9O0qUUB3xx3NYGk8TuzMcG5D55o4XK4NByp2UHBb7ShugIaK8TICamaEQb9ED2Ot2x2EPQRgdzrThyFaAI6UM4MrTlH7J5TQG7VpiaNMHw2ta_xrJm9suOErgzsLHRcSiVKtZveYtsnP4ewqQ2CkjHPokciBZWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=kHcEu1kImwuzorRBZFrWV5X9Lgsknb6U3-CiaMgVMHfbP-3HQnQqUTGOU8__UmXh4o_SCa8uQ_QXnux_iSnuyu6T6CHCWwYhfdcVdbZA_XZoTAfubiK11jixWvZ7sgyx4Htg3z8uu3s6eGQ0WprXrfjyqgtfVLw3_YLMxVH2YOtIskXZKzfirROdQUSylmx8fofTRowD9WlYCMxakVEbJgbFTJPk17ts8_rcamBFbkX13YB2lX4_oHgSPQvvpUg_A53GVIRVqJuooGfqzeaS82tDH0jjN8RLfBNE3fUzzjFNSpGM_lynAa5pb8d2MUx9w4gdEnOjLl6SVObwoQrTsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=kHcEu1kImwuzorRBZFrWV5X9Lgsknb6U3-CiaMgVMHfbP-3HQnQqUTGOU8__UmXh4o_SCa8uQ_QXnux_iSnuyu6T6CHCWwYhfdcVdbZA_XZoTAfubiK11jixWvZ7sgyx4Htg3z8uu3s6eGQ0WprXrfjyqgtfVLw3_YLMxVH2YOtIskXZKzfirROdQUSylmx8fofTRowD9WlYCMxakVEbJgbFTJPk17ts8_rcamBFbkX13YB2lX4_oHgSPQvvpUg_A53GVIRVqJuooGfqzeaS82tDH0jjN8RLfBNE3fUzzjFNSpGM_lynAa5pb8d2MUx9w4gdEnOjLl6SVObwoQrTsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=hddFlCA2wplMhth02jAAUD4BxAFFHaOBgPxcJhjx8nuC43C_SX-QDFAE20qvtOtrRG4y0nKbZ43Urlz7AzB7kgy5hyJYpWS9b6jjjIAr1zEK7xITlfaPdZF7kfqDGKJ3pdg1RhKCAlveffUCKNrD2L2E4u-1AL01zN3sG4EtylV90yDRct69q4xMKXyWt-0AyBMUkuXvlAMhygwUEAdwGiVmrY_1Fm_twtJ9912yJkNLGh0nkgPXlsgGEw5AV3MaGfVuImbHG1S0pk9sctQ1wRd1-Wfx3ZquHD6MrYogI6Jbu3y2A8F55Nmh8Sf9mHd9IrwCKAJbfnHxz2ry2krLXGXDEm9JOVAB7vHn50UVtfWHn-Qk1Q9K0H3_5doIdZVxNgdlR8it40eNDRokJ-SwPYPScK0v15lj0qfV46NU8Qyb1MaDLJfdQ65Wmanse3ejYaM4Ln8bVpB-eMRzT5UfsEW9mr1Dy8dOPNEqzZJK6vZSVNLKaMAyWetphaFkg9EiRu9TrUfj92bjyeRWyzs14Wmz4K3rv6pK8IvsdeOM1WegeT_y2eAt1k-w9rR1xDgETTya4Jyeo21PmndHVMv9QBEDc1fNDWwRVYewUF5FJMAiDiM951pITfyk_r4vOtwftcCwVTGQgDDfX4EneJLGn-AONiqmOH50I0ceDqVbl2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=hddFlCA2wplMhth02jAAUD4BxAFFHaOBgPxcJhjx8nuC43C_SX-QDFAE20qvtOtrRG4y0nKbZ43Urlz7AzB7kgy5hyJYpWS9b6jjjIAr1zEK7xITlfaPdZF7kfqDGKJ3pdg1RhKCAlveffUCKNrD2L2E4u-1AL01zN3sG4EtylV90yDRct69q4xMKXyWt-0AyBMUkuXvlAMhygwUEAdwGiVmrY_1Fm_twtJ9912yJkNLGh0nkgPXlsgGEw5AV3MaGfVuImbHG1S0pk9sctQ1wRd1-Wfx3ZquHD6MrYogI6Jbu3y2A8F55Nmh8Sf9mHd9IrwCKAJbfnHxz2ry2krLXGXDEm9JOVAB7vHn50UVtfWHn-Qk1Q9K0H3_5doIdZVxNgdlR8it40eNDRokJ-SwPYPScK0v15lj0qfV46NU8Qyb1MaDLJfdQ65Wmanse3ejYaM4Ln8bVpB-eMRzT5UfsEW9mr1Dy8dOPNEqzZJK6vZSVNLKaMAyWetphaFkg9EiRu9TrUfj92bjyeRWyzs14Wmz4K3rv6pK8IvsdeOM1WegeT_y2eAt1k-w9rR1xDgETTya4Jyeo21PmndHVMv9QBEDc1fNDWwRVYewUF5FJMAiDiM951pITfyk_r4vOtwftcCwVTGQgDDfX4EneJLGn-AONiqmOH50I0ceDqVbl2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-PiLH-fWuydbYUeGZhXCP5F_LG8lgF0O30BWWdUnpF43QeuwqmAWtpctLy60zj-2LwbOlZcTY3YeSI5z7gf30jJ-LegPtx5AyMV50_6gWfBL0u0L87j-1vFmsdsSGZsXzfw1ZIwWRjD_gvru7F_sGqN5mNT1lsypi8PFBPkT9D504tbh0xpsakC6Pm1UQPZS-FmLVCWVg5-YwRapM12bexkB_R4y6xpfSwo6nAsASydMc1FvpFTu8lg996oXoqGRKvesGf4oAGCMLdQ-tHxDYE1jD5P9WIV5olUa_3r7A00MhTp0fRUkOo8oO1IsVZVcJhKIKSBDjQmncE8El5Flg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=fhE-rTfSSvGMs3maA0IPUbuTvamju12MU4ILgJe3UinJUZIMRW0CWGtluw9dXBjMbERRlsFUcc9lgI5JEYxzXS9eO3GLMb-tk5Ibf-ZKHSbMy6AZeqVrQWy8acQhJmBMuym32Ro4zFvlAhNlDaE8aIzkjftvPE5T-kF_ozKyig3vjW-eTHDnp440JhkHrkAzztkHW-bUqByd8RjiEVKu9fNO2ARqqJIuN1qnqndl_P2yKqorMbNbT_fFH3SFW1W8RMTA_g4aNYCoYBWngjxvyy5FH39kjK9sfuljcUDM3mz_C99Rous_GP5RFoAeL4jNH2vqFm-r1rlj_sddo_TvHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=fhE-rTfSSvGMs3maA0IPUbuTvamju12MU4ILgJe3UinJUZIMRW0CWGtluw9dXBjMbERRlsFUcc9lgI5JEYxzXS9eO3GLMb-tk5Ibf-ZKHSbMy6AZeqVrQWy8acQhJmBMuym32Ro4zFvlAhNlDaE8aIzkjftvPE5T-kF_ozKyig3vjW-eTHDnp440JhkHrkAzztkHW-bUqByd8RjiEVKu9fNO2ARqqJIuN1qnqndl_P2yKqorMbNbT_fFH3SFW1W8RMTA_g4aNYCoYBWngjxvyy5FH39kjK9sfuljcUDM3mz_C99Rous_GP5RFoAeL4jNH2vqFm-r1rlj_sddo_TvHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL14hfm30DTl4JilWcUd4gVKvtdxcNsKX1Erus1WFz3puvO2QNNXUq-jF04WeP_7LU-P_cqemfBvSTO2sKrNZZcR2nwDdvxQ3SKu8-rJrNbTcgFvcOAsJVH7DnlazK7Q4wsBAMr1KfFHxttqKjLCPDFc3K-0yzDGUmgeeLjltACJ5W-7nzTd4wXsyA-u4QUDVeTGlrp_MwgKaC6F3koASkqwJQE-uvcPmn8-6xfNVg8N8gOKyZN2GoaBA9I0RUaPEAxAGCZ3o4-3dZFkQ0Ph5l8RPsIBzXSMV1mx6iZr5rlKcKfMJbaHj6D91sRB90V7FTQAvqTwWTCy7bodm91zSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC-UjClIcWhSIzrUtf0b42jgovWpxmZDjqjtH0pvYOF7H9ar3gbtWh95QO54FKsz_yh_fnb4571BMKFtt_gip2edFbHgZOjcZ0YkLaxDvn4xTUJdrGTbVBQs9gQVJxS29twpDLlx9ymN3tHxhcZ-XZ8vu_guNXVZ0M1AdHcvJOg-j8BUXGItIrNmOChwMMneKBYjyKzcC_M5sD_c43FMaCiqpTQeiOBzAn1T2M-s-KlRhjiCLsA81fIxstQf68v2ioFr9rh8aZ2lw69IY8h9-oLRU3BbJ2UUt-VFHkOx0JbskuFG-uB6-eJA0-K3vSEgJ58RRmdnC9H4DSRPbKSXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwmd-Z5bJnwS0hdSqUIZaU8pAnIlKMV1ePYY4pLyD0lCztfYOV9LKHgKrQ4eZ_gC8HsvL3CKqID-_wBSDxX94mJ-BED5BWf5PncZhaGDRuTdn5tblc8FoO8-lq1uJhd2hhRM0wnb6Trd_bWIDr8NrcNZpyZxU4CwF2htNfAqYp7mH6un4N95BxPC8HVuUpAbD27SdG7KdMdDowTEIlUHlRfk4uGzrm6EtRgyiegIlQet43luVAWp74dcnaiLqww3Z3_cqO2lBbT60PLfPceMNklqc5SxCYqNX_P2gDGUWfxlaIbxcZHoiY9C3bTaaXWRAeYtSF_FnaQX5EoYicEJUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQyLKCmATfELmF6laLGB-fhBmhHuDybZRmmRF1lFs7srnhf4LjaDJ73_RS7cVdVo0D2qeYAn70tAgjHuk68AL_B6pqP1mB54Evg-XyfOi9spid3nRBKi0n6e04kqTJm-XD4r1R-g5nLvwiQ7wttaFrc7ddbdafJzNq4SRQSvjJ5SlpCLFZh1vFcoAQLRd-fzfK0g6BsPCPOKI5zc3mfh0o8U5FY8fHjOVOrzSeI2DIheo4oSbmtNkFD3hXkpqO1JshDCUVSQR6tr5RYrwJp6eYM5YVk2NSNPEMhIT7cd1TlCDYzNIbuN0kuI4cihJV_EPkaK6xWPlMg_z3sltCHyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ks_7iE3CsB3bANpzkQuHBXjQ_vaLimYn51Pe1AQT0j8BC4egI5QbvelkiUw8ybdh83eRdRy0R1gRVOpc5W_rTiVa8OJzzfih9vcIIqVKyPRfJq2mGg4CVx6eAO74iM94H6ldxEYOIliepoST9UynQ_z3lpx5kHtH7RL_t7FgfNaZpvvtRodSWqg7lCBpA2EFL3J1fBVdb_KS8BqOm5Vigzajmii8-QM4P70mWeeOwpJ9fGWFdcUjHJM_DKmqTkaRAf8ZNBWoj-VHMjF_MjwjcqijEGoXJxf_SDGCA2yle8ZsrhUEW-uRACoS0s17A0a9ZARPldcYedcZvObRCu0uHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XutFyMONWEuqeXSdiL1tXWjrsbd3YAnaSPf3ZNcOonsnNjjXBV5sEUL9cz3I8NV_4EIy8QNIV5fyvstMSlQSM1xBzQ9j1h9EfIlOta4juzUYdnx6Fpr7eTi4fGvxxPD9MpVzPW7lBS6xlx1lMFDJfI3jPzdN1remFrY46no5hFC8CLDUGkR5iwKJEYgUXbkwYxTH9e1G-5EvjTQa21AvPPASLFMjdtS8-57eRZF22WhNsaOHQbXrrb4eeFMTh7bXG8XxuVcLAC1io3mR3HYi4O5DsmOIxC1M9-3b873-emeIZmSTRGB0DZtPuKrkmxFjSSQWijBO3xQeKtCOHX971g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMEZWJF199vGxsrPNt26u8isXFuzlHxu9_gYr4OYidUle_V3ETblKzFnrMra0afEEGAlDgM9NxjIvWEgAiJ19qVIrQKWsPimrKt0QBO5tjhIiUr3wfWyks5JblxCm6ugFfmIl39N_Fwv5C8T_XlnQQ2Pcz0h5efPi7-nG-LSvEn--iSgUNo7dSM5FdOOmnyoRUktIfeWut_qD1KMhIFMgBraU3zVocVUDVertrj5tb4KFAqpHRiK0uRNw2v97pQjv9JzKBpQIcjK-hCUHpS-ja2jBC2BH3ROerZ0ZIEvk_qivq0q-FuoABuPQDIIuiH-YNMweS5Iutg24pFSZ2VHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9bh25r018JvDau51h1xgfOCBHcB3tasSgMF-ccuDrn8212_Mr5rAIkjqmNCowcL8TzzMHS2OSobBsCOnwZAR3lJCQL7xIKqwW2thRFpEFpUwuAZOi7E0N_yjpNSnJyR-38t0T3wFbO7gfryAWQPwms0MufNfC7j0Zm0k5kRZn35T9PfayD3RnqiAc1xmNlgY1ZbPSXB4ClIiJpq4qFJ5XIkuULqIj2Mq0c265VGYtXbJhxe4bud49QKXMjmWc7fQRcAmFv0q3iE8ppNf1QHvXBUM-eL56zmY0PYiLWg8LAbPgqyqygdpwMNuEEIhQmwYNoArPp2sq2N656C0KJbWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqICYW7P3Xop_Th1BcvHT_zQps_ObH6ddNlX-JIY0mYqfrFbeh9r2DppljNrxhOjkzjgWvKYOdUtHjQFCtI8XDw3Vx4K61Pc7vzYQF94vFu9FQdIteZ_V90-e6Jtoh3SzsPgxUakh3-gb-DvOV_hCOqLO2ChyApNWXZAHGLDSc70fbev317hNCrCYMcocuYzNLMZy81FLXPISGH-xq81McCG25rNoHCSX8HAaa_rIEjqDzwgXIXbpDRIxPVSK5dIpVxTjZagvTMHTlJmC7RCgebR6amevgILqByjhlnjwfs3nu9OyJwqSmoeaEjuT6-ZPxkBDhb6G7PztBgZfAAlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqgrXP3_LYXXERz8wuztmD4tqdeMqgYqV_pWeeZwMK3V1kfO8_gu65AF9MBxlwmTAWgwXLy_kbFKIWlCWf7D_J-BhEy5lb8noxluHbSYR8cVIcvYg9GwopLp6I4tNLm_qxBvz4mwm4DQ1UMwPvW6RBMrEYwjuyTb0-1BQzRfImqefh9W715OIUPLXsUddzSTc9Gh7xCeO7qyhJgCgr5lu_RE0kX0P8AxY7GkzL4bIwyeLMgBFzVXj-6a6VeqmwqKx-o4yDa_BG7pCtFeZI2tGcvnmj3gthXlUwfnFD1q0YQRXe4byWrywicsnrWCzGJgu3HEQEHfTHa3CczuCwZWSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjK4iLRnyEDAjfmw8cQBDkupXHaLSti19zSnbWP9C5yVlC-0phK4VZ5ufW_dpZ-jSnqAOdN9ERwKAKodfF0UrYKZ_Fw0H2XkkYSea9jSuTIuNbdCBFeHN7bUE8QbjaesGwHxVjQhiDIoQ4r3GFIjNjcov9aAsArzV-iG--NJHaj6C9heFEOmca-KQXBumycjrMfNZ7HCgGdtYy65LwIrs2AgNpDteZsyi5bVyFK9bgjz9Br-DBZwjrWv6y-nin4IJTKDQjDzU_vGKmcng5EKROzAOAT46pBgEVq2-5hyUiTwVX3hR6ggexbQlqRwbe3z5g28GH92_bomcN8PEggO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDPHXo9Z_ZaeUfUiY54WPob6k-NW6TM-7XhGzWDC_GsjBa5Y3rxS3N0uvTant9L4xAW1aj9rEldGxoG34OvJiiZjMMu20HvYKSzAoY0seooIfCPUqMPGRSZ62tckD7sqdNbuOpQSKxu4z23IxB8GqrdC0deCkA8-jxKOSRzCZSCaACUjM2NC01LdQfAHiQHZA09NEq1cAbY3dogJQoe8YU_qjqix6LNBgUtlRGOVk-uoIH8iNGzenhWha26cgbk40WCYelC7ILrBtp4AcSH9twhtY0y3iUh2Ei9S_4JVLF4nkD7AvGLon9rx_V6Fw32nkPdEUzL3oK4Hr8zp8voM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1iiYTo4_Wt0U5z3VRaE76JanC2PY5tdnLbD5mBpmStY9JQTDqKoAKSmVyea9r8APi6i3MYUmFifDdbAE88VCTdahHp05ZzqE3fHnDh8olkYLd7BQKNe_rdDTe8VR-xUHml_Xjg7x4eX9x9B7P4UokX-USdmiEAtecdOLqFlcJROPiid7rr7uBZeMdxiPToKC5NsSnpROzKupDJMwlalNMhgWSe0fzH7MtLt-Xskn8kOKtYcpT6sJgXwxFRxXVth87wVNQUnT1iIm1HieRSPW8jcRp2CnaEfUW7MusyiI9eF_sT0-cGcKq1AFUnMUwny1VhnpGPRNkGcfdn6IXbm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4gkiDxt78lMNZuKhcmTDUPrW1eVceDrzCsSq3nz_RwVyxh2Bi9cNKPH-Ss0banEWRNWuGSzGm_rVGH3Rs_X_S5xhW2kCJbIXB5GxUW0uQjUbrPJG_Mzg_b6XpYCV-5VjUlFcxqgSY97GSgSRHA3koGPGFAJQMgX00mchG95k9bMcZOP2MYHPCBSJyw4gNSPetTbXCaoQUg9P6Z7giLhWFppkJ8t52t_Db85X44jtGtuThSVKI_U2JLTKQ8Usu0HYDP6yiN4PRtYnvW1vX-HBcyOLhz1BzOzYBkVxC62SI42NJFBNviFKjbGbPQR0ioA3bpgTVnOCHUwKWnCAy2sgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANID2fY0hhvp93x6kZv-w6qrxknyjknvEETfnUocKCN-1PDu3JlXdtXOlV7xrotc-ElfQkx_LH8HbZdyUEtdvqry7BoDcBUrCmgkTyfZrHzmTWfXvTlhXfLdq6P6kDVBHfLj5g8L-GgGMR7xfwSyXwirOuk-jD3RUn6_nGxoZo5HdLh8sMhji6AeuuaDoEm4HVhxIYkh2IljgL2ZmebhJVrN6cnn0dE50IjSUYFnUKFUfC0k6D18-1HmK6IgpKB6xObYm4ZYq6jIbono4VixITlYsO1V_ghvvfyOoKSn0ph2N9wtrMCOAatCfKQilJZFTCbQ1fWTHWRNdbRDK4sKpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3tNe_tYYRPtB-nUfMvX4ezeLr7o7-GrinD3D50M6FGxw897FuYKsnvBxiRKivS4r0-LBzGfLQpdH0BegcOCwm91SawZRXIAPEvxYzbQ-6sllC3GoLLPBQ5FSdrYNM9Qea091k1MFeswGj40jhgWA3AfSsj_G6lnbgfBED0EkEdhuyKvIQNDIoxq6gZUG_gb_Cw_MV84C1mZm8P-lLJUGSN_Er67qPOMXgcvH9cj6uV2zVmeSrWH1pkvdEaWZ-4F6_2qXXrHnD9o4CbgQMaI5KpOl8go8MUGOCdPu_LDdxgl3SK2bsXOzoJW8WTApc77SXLPBy6L8q6ew1-oBc0Kjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip858L6jSFg80aDDurNb0hg2iIaZBdcpePJQe8scCfheX0BYvJAYyShvR7WUSvSlHVzX5wwwVXEXv6mS-vwt-M9p2qF1UWObuIv8s6CATcdg8Z7uz6ZWPVgja3p8yToohQxaPItTp1YABYIlWyIA76vC2pl03plfG6iei1JUC-39upGz1VD_MwDObEvTkVk5BJrEzOncN7kRf_p3yvQTNzD1jV_zDRKPOI_M2UJu0vWzOR4qZa_acaF1eZOCGomBUG2ayCSyK4x9uQnOzaP2OWCSPI10iZb7Kt3RE9DkN6I7JCKoucDQZw6qsF5y-X4wYEStCursS2E21Hz5nMgJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=qt4RvEQmHpatpi2fGCC9z6SzCKSQuX66sRDElWjOXIWlimP57AKoOAg3Z1J-C08q-9iPWDpQ53-BmLN-shtF5wb8gLwQqTL_h8eV_tFH62ac2cpElPFxrd7_Qpkhhw87PTcMLS21oa0SROulpkKLYGBUy2PASDniwL9y9GiUNzKem-T4fcKwiINSyjJ2SRQKseeAjv4AH_W90Y89GYKfgC-0m1Dvr0hJXJlM8F-TDOmkY_mIr9fBzZS5JlKQdfGqM45PW5df-uYo7JpgQQjpoqLjUiIspHH6FU5XauP1eGs4xBK1rmR1jrJiTmAzo50djONRTMRdAtxRtqP1gLs13g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=qt4RvEQmHpatpi2fGCC9z6SzCKSQuX66sRDElWjOXIWlimP57AKoOAg3Z1J-C08q-9iPWDpQ53-BmLN-shtF5wb8gLwQqTL_h8eV_tFH62ac2cpElPFxrd7_Qpkhhw87PTcMLS21oa0SROulpkKLYGBUy2PASDniwL9y9GiUNzKem-T4fcKwiINSyjJ2SRQKseeAjv4AH_W90Y89GYKfgC-0m1Dvr0hJXJlM8F-TDOmkY_mIr9fBzZS5JlKQdfGqM45PW5df-uYo7JpgQQjpoqLjUiIspHH6FU5XauP1eGs4xBK1rmR1jrJiTmAzo50djONRTMRdAtxRtqP1gLs13g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACrKwpwT1wKtvzs05Hb3WSuPuqeNPXbjMhuqaBt39lGUVckh8ocW3IPcPFdX0tgkqrIC6DtW22CSBxzjJXLRtz5ETYn_MFxMnMax-BIlVqljDA24I0RoeY3hj8_A12BPcGLFBIfnDvo07U58u4iFrOy9q5rIUp5rOoIAXDbrtoRzsm-vGtC09OK4AojXNdJhnz55IooFtMjfdi2pSyGlD9Po7qhYBJdtjEHE-DVXOBuELtNmMntM2KkldLX-CdMfSIZFhs127QHDMM8Zfhq8wl9ipN6oCtrEYu9GJseC7uMHIBCwmtppTTQYqYJFk9wggoHV8mXSelxfDqPfVM7APg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeEKCIwtr1GXlRE6iySNUtOc1SWx1GCpPFW8M74oOBLLXCDJzt-h7p5xI3XTKL63yFCMtIHJhQAmlDbABUBUFZ71GKeEHY5xYB0OUh3VzLKteTxEvFHNEKeYXpmtSgYRm_DlG8Lr0EEYH-pXERXy-0nTHM59InpdYl3WveOjgiiCQE2pkCNYtNtjk9nazZcBNL3QNNhTi6E_gV0KviN9-_4HnW1HPmZuUfbQvFSeIqSFf8Ub_KYrZ0nbjK7B5JLZqHJXGm9cktsLJ7BFCcol1sK6SSpiHqIAgdmTswnAlPD2Sf6TPFHUTgsEx6NgD6Jp7WfaCC5ehiBmUkXVg1ZRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTSIllN6WLcHysDfyREKk3oMQ5eNoPSPw_twHg6FyyjevGaugf1KkOQGJF3oGgaj4wMvvzL-ZG3dKzBB4ok4JwFOR6GTCyp__fzC1BtVfyZCHipZaorT7_th-g0kuAMD3kDvtAgp3tYfee4F31SVVaW3nZACJJyeP8d2m2CDcq8zs3IzdL97AwhT872UI1sIpApd_TXhzfqWkaUwJu7-8AxITqdoEAwn2xcGzfKX6nG2ds-CCvAs0W7uA0Q-yoaHlP2MKNAP1OvFmG8k9ThkjMPZJ--zzahGHClg3VoIhz3Fis84lXf8933FZTEHnSWxj4NXSoz0fEcsQcE3fP4ttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=f4Cx4OEEqgsOWI6ep_qO4oztwKhY8E4jCxMi4K3P-n91Glo8T-6pOEcLH0_XCbiLl7DNMwxZqPY1Q0GDGMWp191bvOdq2Mz3PI-xUuYQVueAH3k61K6FK92zC0BUEGxuKN-8qQL6NlJKnHeGDXdT-UL8LxMJ7DIqUoZLCEd5xgmia-VSObt_G_Os3BTHviJYkmz9YgxD3Q49YO1BdqhKCyrIjIYcsWYUoWJfFk3wKfmIivEz9NbWgna_fkMBFVgZo0tV3ZsEmc4uon19YQSCWSQpxXA4vYqVm3BK6jYidkatAHc1l50KBqgAdJd-TYtcnkymwdHTBQl9TgIBN5Gi9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=f4Cx4OEEqgsOWI6ep_qO4oztwKhY8E4jCxMi4K3P-n91Glo8T-6pOEcLH0_XCbiLl7DNMwxZqPY1Q0GDGMWp191bvOdq2Mz3PI-xUuYQVueAH3k61K6FK92zC0BUEGxuKN-8qQL6NlJKnHeGDXdT-UL8LxMJ7DIqUoZLCEd5xgmia-VSObt_G_Os3BTHviJYkmz9YgxD3Q49YO1BdqhKCyrIjIYcsWYUoWJfFk3wKfmIivEz9NbWgna_fkMBFVgZo0tV3ZsEmc4uon19YQSCWSQpxXA4vYqVm3BK6jYidkatAHc1l50KBqgAdJd-TYtcnkymwdHTBQl9TgIBN5Gi9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHnADIVi5VhRmiYV1Hl2PpBXil8g-d3-khZUoFAXnZEU-gnqfSFvXiarjC7iozlzj9f4QI1M78P_1b4xMxQyVqRmdQpw3JjtFrnUJ-wddCneq77bRAKSzKSyFyTMKJ25jDIada5GAGOmG-e-vyfoO1T01pReEjrusXkSYQlZZ98TjchBduGSNNket34zrwaofhdz0adOGxwF-y0fJhNjgmnMiJJG5U4UYeawwJh9opJnKdn3XlSvLLFgvUe2XRV03cULMK4aXgS4g6Xcs3h_9HA9RMm_aDTxiEXbG7kSbZYtHey3s6RcIj87dLs5wuFMWGByfBrcm98wODXnUFTJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=CrD4w4dggSDnIT2w4E8JeaqMXTb9a1rwwbUw6nvJyaXYQp2ydabZKLgfCEHEXqdKVHYQWhFBN1fuIQBhVMf3S83Dbjl9kg0sGOtUyAa4mFmGf4HB5c3fhL2Yx6n2_YCQJfh79ljDEeMyJnDIkVqGzEzHxRO95jprKMtgxjpyNh3EKljC0YlYzDiwOhg6dSShR06RLYeg9K1Q2coLkhYtoNqJiWOwy92iInNmf31y6TuunSWmxhLexY59CwExmSW7cC2wn000fvtzgLh0zocvNMGsok9XbjHnd4rH3vbOLHQY2nJmwCmz_4igyiEaO_sD_RwP34y9JXUz7DtcYnla7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=CrD4w4dggSDnIT2w4E8JeaqMXTb9a1rwwbUw6nvJyaXYQp2ydabZKLgfCEHEXqdKVHYQWhFBN1fuIQBhVMf3S83Dbjl9kg0sGOtUyAa4mFmGf4HB5c3fhL2Yx6n2_YCQJfh79ljDEeMyJnDIkVqGzEzHxRO95jprKMtgxjpyNh3EKljC0YlYzDiwOhg6dSShR06RLYeg9K1Q2coLkhYtoNqJiWOwy92iInNmf31y6TuunSWmxhLexY59CwExmSW7cC2wn000fvtzgLh0zocvNMGsok9XbjHnd4rH3vbOLHQY2nJmwCmz_4igyiEaO_sD_RwP34y9JXUz7DtcYnla7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_lJ1-QPKASIaN5cwx3u_u4NNDZpTVea4Xzhsjf23EXRfKIF4KQSnVRfzlqSJGF5y4WvPnofheBPt_FKcWJq_LCZANUr_NDbiVgzfBSCp-rBPA5s9UF94Y4w3PNLuCfuDmOMpUJKRVzMvF7NERs9r6_ilWZGaYXAkG8713VAL_e6zoJmDUf0tFjhYI2l5vs4GU7KP-fRyZWulHMt-Gj0ieruEUQKuhFkDtCkZcKMJuPZa_6TEHQXm21agVI2gBPBydrxkZcHdrxAJPrsmZRGXap5Oc_KlXSUXIFrCbFFotCnjr6UcmHV6OoL2sa4IqdJWikCgCeVe1-9kLr7plqZ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFgJT3syef14sshRy7pZbdAJZYGh5P4CbbYFFahDbf2sH_jOG3A3P3bpzxUgeVFNHw_9y8S6Pc3FaON0prjGNCXz85UKo2LYfxb63GyEBw9BcCH8b0Bw2C4i3i83N62wQAao0dBEzxr3KrOGwoYMPRHIcu_EM4fjsS2nLWPDdc9m4NtQTOLFxAuhGgh7Ubbzd4iP0fy1FMUTKCYxCL9j48cYkNedTeKuKCmdpZwWzIlUIkPlEV6yvnix8CgH9ayhvwTm48jFxyFsjX0ClQNmcSeuNpirQeEHzh_weDmAtBSVqGIaP8-HKlfjYTMWW7PhM3FM1Z_FjLFSc7Ns4ZvHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KBrxUzEm4-3lMPdm6G3YvPdBwXxo53tGHv4ZiaYnui6ZpkMgh04eDBBkcAzey2EqE0P9V6dDsrEey32LjuTN2kdfY-J8rZNKuDDpSo69vbtZA_wTiQr19wLJPD51hCqdMFKeWNG97IJ3PMaeUcnF_li7IDQz0x4AMiCPL6GAF5otlQgrxEges_hE0E5vzpeDW34E6sKE30mKDwtekSTk3FStL2T4kPJTeMwVlYkd6fm6el2iIflpydSSESIq4kfe4HYepViqz2EONq_8F0QwIODvmUHZqnmwtCD5neQ3y1U9CTu3zAD3X-evxV3Rm35nJPAPYdC5o_Uxw9j0A1M9rJOi9cJr3ChwQcXYKYLFSTUJkkbPL9kshk9KRinxiPQFjkZLVCJWM6VXfT0iXMr-DsmXnthUZrL2yRo-HYbh9ioEnyfhI69hyyTkKTEKsvJH1Tf6OzCSozcD5j-yIOWgXcTHF1QZ0xk6KXjkePStGFyqyunImNJkoZs7fiFOgSZJyDYgUggdQzZUzF6LeEAaVJFFZmv2mx13aVpjlSbSFxa8iSOmxJEFpt_U4CsgOt4Mx_3jm2TgOOy8HUbq6Yg1BacW4SeBLLuvEr1T4op9pRI24VvCLLCdsgTFV-j058uUhY5LPBnxAlYpPtRiWn9jP07ksgC4meqbJcrQStRIeD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KBrxUzEm4-3lMPdm6G3YvPdBwXxo53tGHv4ZiaYnui6ZpkMgh04eDBBkcAzey2EqE0P9V6dDsrEey32LjuTN2kdfY-J8rZNKuDDpSo69vbtZA_wTiQr19wLJPD51hCqdMFKeWNG97IJ3PMaeUcnF_li7IDQz0x4AMiCPL6GAF5otlQgrxEges_hE0E5vzpeDW34E6sKE30mKDwtekSTk3FStL2T4kPJTeMwVlYkd6fm6el2iIflpydSSESIq4kfe4HYepViqz2EONq_8F0QwIODvmUHZqnmwtCD5neQ3y1U9CTu3zAD3X-evxV3Rm35nJPAPYdC5o_Uxw9j0A1M9rJOi9cJr3ChwQcXYKYLFSTUJkkbPL9kshk9KRinxiPQFjkZLVCJWM6VXfT0iXMr-DsmXnthUZrL2yRo-HYbh9ioEnyfhI69hyyTkKTEKsvJH1Tf6OzCSozcD5j-yIOWgXcTHF1QZ0xk6KXjkePStGFyqyunImNJkoZs7fiFOgSZJyDYgUggdQzZUzF6LeEAaVJFFZmv2mx13aVpjlSbSFxa8iSOmxJEFpt_U4CsgOt4Mx_3jm2TgOOy8HUbq6Yg1BacW4SeBLLuvEr1T4op9pRI24VvCLLCdsgTFV-j058uUhY5LPBnxAlYpPtRiWn9jP07ksgC4meqbJcrQStRIeD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=eflcG1nXi3zfqKsQHFwsMCp6J6rDbsC5V6WFJFg52qiw_wTOD49Yf7wu7iAUkZg0TrMABGUYGS2N626epi4B7VgymqOJn17tmku783gDefDiK0IZspAu2QK3i71-xRCiMWJ-7Yz7HfmJ20Y2U-piPYJ-EbhDLZ8CU25_LolNfR9tih4SAkT54IuRGkRU258IXls84qbszdq2mzsoOHFBn8ThsnOSwP7uX42tCsbPSc9mnPiBk9u-eVcj38WQtWVCgUdX3y5Uk9EFthea6bmWnJM09HNbdmhxZBtOINwiFSS7oM6q9xrDOQkcwQCLUJYOU9ZqGdK4x2ZYNYnPGSBcLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=eflcG1nXi3zfqKsQHFwsMCp6J6rDbsC5V6WFJFg52qiw_wTOD49Yf7wu7iAUkZg0TrMABGUYGS2N626epi4B7VgymqOJn17tmku783gDefDiK0IZspAu2QK3i71-xRCiMWJ-7Yz7HfmJ20Y2U-piPYJ-EbhDLZ8CU25_LolNfR9tih4SAkT54IuRGkRU258IXls84qbszdq2mzsoOHFBn8ThsnOSwP7uX42tCsbPSc9mnPiBk9u-eVcj38WQtWVCgUdX3y5Uk9EFthea6bmWnJM09HNbdmhxZBtOINwiFSS7oM6q9xrDOQkcwQCLUJYOU9ZqGdK4x2ZYNYnPGSBcLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl8MAPuJocp4hnlSt1KK3nLGmnzTAnytdTG-poFcH3VfJCeFp4laaU8ToqGNvRGN9nMgRPPW3-iy-OUUtk3p8zv4lgHTc0qImWcPe_VUujTayHYMeWqgA8pit-n1AOvWXdJTOMNklyM5lkNdRpuqR5kpYNvUPfIhqUZk6bod1U_TsXriXidJrOmypkmHBeUF51JmmX7Z2Y5lfoDYkHHabJAJd0JpONy6u8URysORBZ5YPFYyheIkxb12QmTUn2w9iwSXcytYTkdvQuEBJeKGF7I45jJPfGwBnNupdEePrAbGcj1_57WlRHFDEjyG0w7NcNBrHpmhwGXYdfgvKh7QIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=lCdrn0uKn0sU5kKpdaLQPpttfLEHItyjj8yd6d85x_QHlG2YAMMwJEenD8HfaO0kB3k5t8GDsx7gSzEWgkGJjAeT7u-MNx_HS3VbpIYABFIW3ghpOwHERuxKQZdqvihqSzJhP4ppt4LM9MS-M1W96JCQdg15XfyX-gV3OOwUhuKlg7MVvWZbAmq1Mrq8GeJLAaETLAIorR18OG4xu_dyLB-qThv8o1cYiwj3AYTc4qYzTZE7dIMPuzxREE0t0e73qrmqGxbax7CoNKpx0qejPgzeoV_2F-dJW5KBWzKygDlT1YmU5uKzhru2niP2w225paHTOyWpjynOU2mEW67kE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=lCdrn0uKn0sU5kKpdaLQPpttfLEHItyjj8yd6d85x_QHlG2YAMMwJEenD8HfaO0kB3k5t8GDsx7gSzEWgkGJjAeT7u-MNx_HS3VbpIYABFIW3ghpOwHERuxKQZdqvihqSzJhP4ppt4LM9MS-M1W96JCQdg15XfyX-gV3OOwUhuKlg7MVvWZbAmq1Mrq8GeJLAaETLAIorR18OG4xu_dyLB-qThv8o1cYiwj3AYTc4qYzTZE7dIMPuzxREE0t0e73qrmqGxbax7CoNKpx0qejPgzeoV_2F-dJW5KBWzKygDlT1YmU5uKzhru2niP2w225paHTOyWpjynOU2mEW67kE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY572pY5qZl_epWckA3ZeL13rtk4DvN208BaP_7AJYxZztIUeFbPGP_dNHhqTmT-1zuE03-TWQ-w_5LSfMCeB7Gks2Ny4dS1mNwLzy4GpxiCBSrGeBuCrTqhdzcVjcPynhaG9F6kV1okv6mvi3oeQ84E0E24PANYktYMPRzGvkI7nYS_5-T33iqInE3YRQXgIl6QCuL05WHdUU_1cnrmgIt6m3au-ilACAx6nLdsGfeeL2BFAcESE2jDMaEsV37vmXS74G0qRATfj4E9pk0biwFTbWANAUJVmcgl3nkhzomww_XzJW5k3LRRII5Kc4sQugu_AzPmPsfK45SsTi7GTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfV4JJfqkpirgxaQq_7lAqD_2z1UcAUcAzaC6lNhDvgsbHkTcMbBoW_KT30cFYRigKepe0KQiyDWUH3dG3ejunRJkbOQdiVcIMXonk4rzQZJCbYTKYUhY9lA7o87OO_VQxMIstEzCEm22XAXQBDSZkI1X48Mz4Evy5QNKHwPKowc0ALhFhKNqdFQi4mwOA-cYGXSJxa_SV5zqqps39ayJSQRuSgRYbvi2xtk7c5UXLIHB3ClH0JiGY8T5Wov3UrSHLd5Wkv680388t7-2d6Xc8Z9s4zZf2nLvkP0yyvhcb05ceMMkgrITY5LRfV_OD5OaXLJ12xX9eMO0ZH73gHyEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyPRJgVGz5OHjKTNRWojX5GOTSV-VVlQ2CGRmMKuYG8i6e_4IDUwCjpfTh62FFy3NdsBM4sGxTjGMdLvPD6Yg8XErsobzfzSy40Nd29dhIwSjqKd9x1B3FvdPebBpHRKCECAL6gdXSoEEaFICak0MQS3DCgkpBRnrPfJ47_EOg4AXOpRqobsXusZJWzSKE26xPJPPNT92_LAOvVmdxnmg_e2adBuiYVSKZQjhGbCJ2PQwQkeCoGW7MxWSNO13Sh2dRam6_TfBha5V-Ua1-dVZtJCs952JVntyfvId90AaQenj60f1uUbTa3G1KxrFE9nbLPCJEKG0bNjBDkOdYWyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF9RYc2qADwkikFffAOWuiy1ZfiaPliBaLi5F2Qe6t8fNoQi5lTnK_h44GM2-XsRJXcRxcQJBbq7z8H0euWGjKbEUexQkG3HdVXF90dFbkHsEmG8CObhT2Rn-30FTgmhEg2uL7-fz2tH9TCBP4nQkiFpfklrEDAKckA_lGUaiNfFrFMH89cW-9Fhkvcp7ms9eWMh-AgOubA4cn987ZsH70jY1O6yvyLSHcOSpfqupwwevtSU-FPIophy1DqHr7JuoCj_wIdAraD7Bw-TQlI981iQYwma6xuKBEl6RNcBFtgQ7Y-FV98JRxjGZ27KfPW0YB4ZqVYBtJQ4a-cxd4-FWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd4Sebmnsu095DEvngkOUeNA4ekAy0ayYJp7ZlLmwJB2X2pB1mDHbXILnihX7-qpvSCJ1P3GQl0kaZlHMuLNDRI408a557Xf3vhuQvOmzEMZyLMId21cs_uMRQwYTp5eBrBxwiG49u4QAasuZrhCOIqU6W4mGFe2uYvSG2aP_KI9n5fGPKilWF3aYH_AZUQoVvDDPQoxAzDCkIUOIZnBvkJRk-TUHB3XkgPO7NLN5H38WNUfFE-_SXjC2WIASu1g8fyJTmWlslxBr0jrAI8cQWZ4PcWbZVK8WaxD8Zh3eqw2ZEJkXomDGiKrgv7vVGT-5VPL9s5gH1Co2qGcrZHIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=f_PmtgVwSUH0MeloanmkTWHUjaOjZnNNXsxT5CjzP1iZLbgd_r6faABC9wak_9gjMoBtlB3BN34Ac5k_gs1s1NXDCVniU1JuKynqfx8g2VxImoZuZ58FzxxZEl1C3TWaZSc-cC5TaeWjptbCYTchIeXHNgo_mbrtJeAwpNxRgDq5iwYzQlZ9Bf3SgFWPCSwnM-SfJ087N7HmCly4p6bOCGNViEnOfdUvqsF8SxcmpmN61L9RkfrAMkLErV2BEQfCk_-YSdisIDJXw16vhZt_J0iylrgedqxuOiNKk22gM670pHt4m4eWoRbSjCB_iAqxIdYTdkz1UDluJPxtQsL-nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=f_PmtgVwSUH0MeloanmkTWHUjaOjZnNNXsxT5CjzP1iZLbgd_r6faABC9wak_9gjMoBtlB3BN34Ac5k_gs1s1NXDCVniU1JuKynqfx8g2VxImoZuZ58FzxxZEl1C3TWaZSc-cC5TaeWjptbCYTchIeXHNgo_mbrtJeAwpNxRgDq5iwYzQlZ9Bf3SgFWPCSwnM-SfJ087N7HmCly4p6bOCGNViEnOfdUvqsF8SxcmpmN61L9RkfrAMkLErV2BEQfCk_-YSdisIDJXw16vhZt_J0iylrgedqxuOiNKk22gM670pHt4m4eWoRbSjCB_iAqxIdYTdkz1UDluJPxtQsL-nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOzPIDfFIb-6HcvSnjyr6sbdLEJa98DY5D7dqoB7bxJ8as-P0N030K5mmMMmt3Zt2ixy20SPxjSHWYhiIhNG5XyrAgoSH6j1Ul90zztmS1uzSKLUN5lkkh687g4ImW7iMyXsJC0FvKv8He-aadM4_BOxpp2xPIW6Jcuoe5TXjZyBP6zqbrUYDNbSzTIfiEUyDSqX3rdGQDIuqmGtFsEQvuommN6zwd2H4wsZHB0bRH10e8mNEfSCMAfcab29yZ0ZrljgPCkeTJdP-K6m7v7EeQiiAurgz7wxbB_0ZLYZOfpucqV-0h2_R_eEAJ2m2yCBQdkBgOMlRZ9eodDEvFQCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z94UeaQtWuqW4nsl0wOOe3Z9S5q1K6dUqyUt2seSffYiNEale9v9N2d-vSUDQlqkMwqDTm1gYfWjVnZ84Zt5n1SDVE6HFIbJjSYtidMyVeRSni0D7_bV6DC3Bs3OFOYaOLrcmVxv66pgcooe1l8AZ4zgtKBbPMSuHCov1bwdfppg_4MZUXFcPmcOunse9GqvR0jiwDIFTVoAlLlRW3vw5pUQCFRk_c29Ntd2-AhMWvFKeUYOCvQn6x-Fx_e08xjZwxyGQN_HtvwqKYe5RpMMDx3W_hFRC5flXcnR1GwFUDSmKG9dSd6M-50V1PF_LhXN6LE0e2l3NJF-x3YeHgQJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=D3htuQn0nsjidGVXWqFnkARX5pTxc7OdrkNNkDn-5CZUymtH0O-v1Ss6iohdAd7AoQIQGVc7mmVkJzv6_4G-yhhwU97HFcx3g7GbhBV2FQcQnPG96CZF-OQc2SrkkB6HFfei4axwwVMUHePev554qLT9QZlsBn3tryQvFz7UlHbXBey091awA7tYMAY0N4epwJ7sJnl_iFLmo7uKuP8Y14hAdK0MUdQboLytvxZ9KpCx3KxrR3q1CGcbyKeySKWKLXvhcrm2CvL_urzb95NWPe4nSfTDGAiirWqJuF3ggskDl-ZQ6oIQW9QBPh_p50kUPPLA96apuHHvA7dHwrdEASx9k5-TlnvIeTmXTYYNlBFVOy4EXcNqFwim54desZLOf-juyhoRQtBlB5b_65QbnKjBUtV6lCDay0vz7wBvd78fTEX6c_tA022yXNkxfj2dH-Yfk_bLqN6GySO1qNfcCzOhPk69lm14gW2TmGmGrP9b-s2d4Rzo2V9cWKdKv-4LWvRIq0UA9dVP0S7OY4u91_mYyfCQQ8A_HY5_2tHEKtfXW7Iera69FzlF3pHNysUytW2D3p89kmIFfP6WuqFq9rtxxuz_P9S9D5ykfHlAq0xFiRC_89HnOVSsLEx6TXpLVydLLETt9Zi473M1BzamvRbqapdc9hJbkYctk_uj1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=D3htuQn0nsjidGVXWqFnkARX5pTxc7OdrkNNkDn-5CZUymtH0O-v1Ss6iohdAd7AoQIQGVc7mmVkJzv6_4G-yhhwU97HFcx3g7GbhBV2FQcQnPG96CZF-OQc2SrkkB6HFfei4axwwVMUHePev554qLT9QZlsBn3tryQvFz7UlHbXBey091awA7tYMAY0N4epwJ7sJnl_iFLmo7uKuP8Y14hAdK0MUdQboLytvxZ9KpCx3KxrR3q1CGcbyKeySKWKLXvhcrm2CvL_urzb95NWPe4nSfTDGAiirWqJuF3ggskDl-ZQ6oIQW9QBPh_p50kUPPLA96apuHHvA7dHwrdEASx9k5-TlnvIeTmXTYYNlBFVOy4EXcNqFwim54desZLOf-juyhoRQtBlB5b_65QbnKjBUtV6lCDay0vz7wBvd78fTEX6c_tA022yXNkxfj2dH-Yfk_bLqN6GySO1qNfcCzOhPk69lm14gW2TmGmGrP9b-s2d4Rzo2V9cWKdKv-4LWvRIq0UA9dVP0S7OY4u91_mYyfCQQ8A_HY5_2tHEKtfXW7Iera69FzlF3pHNysUytW2D3p89kmIFfP6WuqFq9rtxxuz_P9S9D5ykfHlAq0xFiRC_89HnOVSsLEx6TXpLVydLLETt9Zi473M1BzamvRbqapdc9hJbkYctk_uj1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=o1KH0l_TlqTfezNFy5FsS8MRR1YJ6ytXRpFvCqcAa4rdQWqMoRDCjopHVJr4YhTMqT5pUv4VNthAJzprrEIKesGZivbUeOOvlaRdlfhuh2Rz3XIWCOdoGJ_s2AFrxLBUFXJvb0YlLoTf5_u7UqDmuZ07B01rOGko7-sToQi97kIdf0c9Ckgtp3aK5TqAvBsu2yiXq9ZgTFQPrHNKhHg87Hjd_LPW9i9xjiBf1PhbJfrxOUY4q9Dt8fzpIDC7NkCX0w6wto9MpvJrMndf-TxFWSNu2h9Z2rvyqN0R391u3QutR8vJt0eV9eKjto9yQS3Lr1v3oemiLNp1BYZPX-49Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=o1KH0l_TlqTfezNFy5FsS8MRR1YJ6ytXRpFvCqcAa4rdQWqMoRDCjopHVJr4YhTMqT5pUv4VNthAJzprrEIKesGZivbUeOOvlaRdlfhuh2Rz3XIWCOdoGJ_s2AFrxLBUFXJvb0YlLoTf5_u7UqDmuZ07B01rOGko7-sToQi97kIdf0c9Ckgtp3aK5TqAvBsu2yiXq9ZgTFQPrHNKhHg87Hjd_LPW9i9xjiBf1PhbJfrxOUY4q9Dt8fzpIDC7NkCX0w6wto9MpvJrMndf-TxFWSNu2h9Z2rvyqN0R391u3QutR8vJt0eV9eKjto9yQS3Lr1v3oemiLNp1BYZPX-49Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCgh8tmXrS7lkoF3x1nicnFKJWMCv5Otajnrra2QGiMzmb5YgbyT1t2-WGLlSVMQax5p9tsAJqM-i6rsZ7pE61wrOeIV74Yh1ai2_glrorJxHB4XPyHaS8_4aj0LsL-MVjXNUEkS5hUWqH_XHD4_ik0pm2aEgf1hJdFntMEBrQWBvfASbfd5wYnQbl4QqSui64lDAmsREJKLp_ONzZ6I5wvlp0k3KmFrulbDnjD0XM4igdcafKKZyKKnIB3iQSzzWk0yDWMF-rlzaCLzjwkqE1NXS-e7cz9XRgVJHwmRIdxzO89J-v19JgoL3_Vl5eK-jCyoBUBeqsZmdvHqxjyZ6DGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCgh8tmXrS7lkoF3x1nicnFKJWMCv5Otajnrra2QGiMzmb5YgbyT1t2-WGLlSVMQax5p9tsAJqM-i6rsZ7pE61wrOeIV74Yh1ai2_glrorJxHB4XPyHaS8_4aj0LsL-MVjXNUEkS5hUWqH_XHD4_ik0pm2aEgf1hJdFntMEBrQWBvfASbfd5wYnQbl4QqSui64lDAmsREJKLp_ONzZ6I5wvlp0k3KmFrulbDnjD0XM4igdcafKKZyKKnIB3iQSzzWk0yDWMF-rlzaCLzjwkqE1NXS-e7cz9XRgVJHwmRIdxzO89J-v19JgoL3_Vl5eK-jCyoBUBeqsZmdvHqxjyZ6DGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNiLS1_c8_QREnVjwz6h0X2WsTfiHr1k-bDg9kLZVrPWh0QJpjC5V3Qdv3b3sQ1IlMA4p4bdT1slyve7QtF_GDMb-H_1ex4xgeDN_nSZY-Lbimn5pwqyIRWprmOde3GL61EfUQgvHybNe1-jM0Y1mTMgCIQkBu8QDVBFXRNmH86OQfj88kLcIMmzMAT5aUjUFM4Q_11QxmDkEwmvBWs8V1pOJERI_32DObbNHr4xU5D2rMlx0li6XqdZfH1THUPIFTFiN_qihqRXwok5L64QMcGhhJJLZU3pMllC_RAfXasI7ad9ssCbmt_iUPpLd5FApDBXU74jyWD20DTAX1gaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2O5GGsqHKQmj1R2KZXiswgFB6RacMw4HUVRdHivg389SPuZGHZ9M9SKfhk3KBrQaJOGUdChVTAip_zfGQyh7C4dhZjf6QZceC2HYBGXBWUBqHFWZxur3bn5tS7rQGfm2wNhLnTNYNWSTu_q-9mcycxeCn8uucnd-YghgJfOUChfnIeGdMlVJeH0JMJmfl4GDu4bz9o5L_24FJ0Yb6pzJZm8h0uWz1otPAlgr7Su2rgX08gvpAXqh324ZOyHkhsRTSY_qI2FEXGNwhS_3X5Kc2xQ-7-GheDtcR1u_BN7fbfSeOqnBbh6r7rUgTNCSe0MKS7OiplBJh-LYBZqxAVuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmQ0m1S7PRIxddY9FYjRlyEcZqVhz1I1YJIAHz3H3RICTpDV2k-QIknIGUjS9MHmdY-sd-h2Bcfhu5YX5txPVm6ZlvqxfSxURxjY8kTjcXW9iLCMIV08Jyi9GsTZdkFCQzQx1k3u5ev7oFyz43rmumY46F4jrZl14T7B3sC04k_bAno0b7Yt09Sb1p5KVJOMtr86K_Pt6FfvoAYrizPyDNgOjfH1iEn2O2qXu-8zKqcCNmDN90YKjdPHygwh237ueaUdAwMWlktVN3kX-1f1t07mOz0m8DT_d1_2jE8w7Tu-g7fhCRLBdb7yGeuMeBWSSkMRDYP25m0gHpWjrCj-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=pp1MoUJ0Oi-B9AGeroz7NbM21GBppNHTfO8eNnCyhXoa3HZHu_Tlwhu8Af7cyzV7tv1_lUSmPRFZ7vRTAhGLcn44Whgy0X8HJefV5PM-bkJZ5i703X_kEOarp0y-JHZPQ9NVEWo_roD93bMzbLhCUUUJtTaEMVXAG4Suhmq8SJ_6ECT4WdAMVlY8SL36yBQaVOzM-n0qKulgBo4CSzAP0_9HPKVfe4OM5dZpSBMZQXJULomRyEgVBnt2MjZYUqmb1zUlDb25LsYRqvd6IAkptwUAENw17WgZntbuXZAfzUkOH0PG7tAeZwucLDOA6Xb7iTaqkYY23l-aAAUSTK3yCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=pp1MoUJ0Oi-B9AGeroz7NbM21GBppNHTfO8eNnCyhXoa3HZHu_Tlwhu8Af7cyzV7tv1_lUSmPRFZ7vRTAhGLcn44Whgy0X8HJefV5PM-bkJZ5i703X_kEOarp0y-JHZPQ9NVEWo_roD93bMzbLhCUUUJtTaEMVXAG4Suhmq8SJ_6ECT4WdAMVlY8SL36yBQaVOzM-n0qKulgBo4CSzAP0_9HPKVfe4OM5dZpSBMZQXJULomRyEgVBnt2MjZYUqmb1zUlDb25LsYRqvd6IAkptwUAENw17WgZntbuXZAfzUkOH0PG7tAeZwucLDOA6Xb7iTaqkYY23l-aAAUSTK3yCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7TonENRj99N7axnCVFkY_lO52ccYHf4dav7jlax_OWqKeg24Y1wc5mlHoKZrDPk38oymjNb5BZTTgSF_gyGwo_7zk2e60Bm65U-BAr5Qf7Ka0ogjBxdcAFQpS8ADXuZGFlER2i8aj3YRGp4Gq8nV8GhJi4IMYEh5eguu6KbCnUy1xJn7Msj07iqQDMAKteG4T2NDwpvdZo1G-8frYpxkrpKaSqz1UQ2De4VNERv0FCoZC7nkzHBZGc7iPIKbk0syk3olJoz2DtHrvVK8P2JlVz4svO15XYXMjnd6_vl-9N5yrR63vqO9MNj6dSo00_dkGlJFKd7AINBQ9CzcHW9yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_xq-1DW1y3wplBugCpgZbaS4yOJXn8EyGShBMfvgcxKR98-7HAr4bhIM35Rsr6jeU8Rn9rwHfnrROhO0S16SOi5NJyuY_AAct0S9uHz9juX8ixV7Qr-l_xiqtLSOXLfbgQsshes4QXMJHfvZ14UWhUZXdD9E55b1VUPgZSZ1iMxtHRHT6Hy_VAzkbqp3KYZopXSqMzt4TeWpBVLSxISjq6_TtyFfLYJOf2rSu8vdfflgTszodMfZ3Odn5CyHhfoWqqJZcshL-6BCp__rPbj4OZzUPJxHZJux2EUKXXrh7KnEwVw40AlW8Of7aXcwDk4pCXM9g-igGWysJKlcOPI3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWbzwqLVVbWhFCzDL1RWhvpSIbPM24b5GPRUP3-OV6KkdyB15phoCL8LRFrmO6jqAPXTIeZMNk4g0zMsBAFO8x2xCtx2EYFfhXr5T7gYJSgdN1OA3oo98C9fXxKDxw1jpo5exms8GP82PqsPJysTHgpKfDVe3q0kxwJLmKldBuDeI7R9eZIZKAEU70xdUVKWuOUYWYs0S-V0cuFOM7aGZznffRIXCBKm448y4zRSUF83x5tXatt0eNOWQve-ZbvJ4KkL2J9fPwYYLA4ZsDldj0sIJvrpWTKEQlSEm0l-LxgAxxdhvg8yEasCRcGjAUnCV0OJyOnvalwU3wsOGwk7HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvbQwV5wM-xVN0bW2MXPCHKG7P3KtGdlEUA-Hhdq4iySRJpnTX2zgXg3GJ6ET5dRcUpIKvGlJrfPOPsizsOKYaAplCm-Ov1-ZHuNVxx8EjsutOK56JwydxqXP4pdVPtJsO5r2gVdS2RV205OAwZfGBcYlVnEgOmBno_sHMzFfI1ScOvFJoPYxo0nlqhDUhDP3W5iIijos92vsbZB2yWdnkI5PJc_gOLRMIcpNSsnJpdFTMk_9Ra4gXhpxVrcpT44D6ZuF0Ey7JMqEXSgDRxqJlsCLCx3ysitrSaTBj9lZxX_A_WuwA1bj4E_Wpah1dghBVQzNAzUEMbUyZat1FImmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=EB5UbBTSI5S0_2F27F7W39RkZ_tUotWac6FNdpjA792zVNdUKpc_cyks_xnwoTM7OMYAXzUZwbYRx7knngw4mNVRVS4zHosZuAZ3mDiuplKTjfiAZUBEXu9AHXPUYCOjNUNqlxDvOalw5EOyqXNYb-PeE5UTFDE08lUhTEgl6wCHQbiJ5R2-6WUzm9OlAfjmqj-YvDDeC43Aj3rS2a6SaLmWq2kUsu7DtjSTwB0DfGheVxtBBrtd2xlnh3mNrt64wMrqXQ3-9k8XPra0gEwKXidZrrHq42en-QRXxYCH5Dc0x5LYAnsOWLZGPqancF5F-4WPwGBRe-xcXUmq45Vz6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=EB5UbBTSI5S0_2F27F7W39RkZ_tUotWac6FNdpjA792zVNdUKpc_cyks_xnwoTM7OMYAXzUZwbYRx7knngw4mNVRVS4zHosZuAZ3mDiuplKTjfiAZUBEXu9AHXPUYCOjNUNqlxDvOalw5EOyqXNYb-PeE5UTFDE08lUhTEgl6wCHQbiJ5R2-6WUzm9OlAfjmqj-YvDDeC43Aj3rS2a6SaLmWq2kUsu7DtjSTwB0DfGheVxtBBrtd2xlnh3mNrt64wMrqXQ3-9k8XPra0gEwKXidZrrHq42en-QRXxYCH5Dc0x5LYAnsOWLZGPqancF5F-4WPwGBRe-xcXUmq45Vz6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=vc0yjheHnGpDydxRbTGdGi-ratXA77NVCSAARQJnwIG3uoZXP0gn53HknDneowXP0hDWtJVNOS1JSxefZOxu0Jgo3xNLbJpzAmn4_DIOJH-CSoFGsTQxMGDlTubQaCUJ4FRV_-AIrb5PHG1LUa6XKNmYhRRJe5GxbqeHUV_7HG1aHeIAkSJDoptzWlJkV1IZMEAJ8VY1CdZdi5bzy7tAwpNDM7bqhelYur1noygCRJ8xweYZuW5JHbAjjNeHDuPN4Mvt4SWeCuFFQIzgMIfZGURPpuCOwm_s39dzmd2oFRQW47IuE0UrNBnNWhE_uSJdoErijOEuBrKQcyrbIukCAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=vc0yjheHnGpDydxRbTGdGi-ratXA77NVCSAARQJnwIG3uoZXP0gn53HknDneowXP0hDWtJVNOS1JSxefZOxu0Jgo3xNLbJpzAmn4_DIOJH-CSoFGsTQxMGDlTubQaCUJ4FRV_-AIrb5PHG1LUa6XKNmYhRRJe5GxbqeHUV_7HG1aHeIAkSJDoptzWlJkV1IZMEAJ8VY1CdZdi5bzy7tAwpNDM7bqhelYur1noygCRJ8xweYZuW5JHbAjjNeHDuPN4Mvt4SWeCuFFQIzgMIfZGURPpuCOwm_s39dzmd2oFRQW47IuE0UrNBnNWhE_uSJdoErijOEuBrKQcyrbIukCAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=MT9JCxO_C33dopRgCOwyYNI9WEj9mGz7FQZAY6qQhGHk0AewPzmsakP9DagGcXFD7kC3IQM4L7GtKS0A7Jeo5sRg5nT7HMhuj32ty4aG7Qu4yTjws_0ksMJx2t_llYo__lr41OrINoDeUbHtzW_hNAxQsGH5dfG-40hNRTAP8WfQvlL4pvql-tJln93rMV3QyYJaLloHfOmVTe8UZOSW_zG3rgFMxPT91g0mwqVm83lrN2xGBTJTsbqQwjNnbbgUHRxSi7qe_zXrVK7nmvFRl1a2KfehkNKn_4XcIMmK4f-pLkrGfG-BzpAmCh53OQL7f05L02HipOrgYleWWmEsxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=MT9JCxO_C33dopRgCOwyYNI9WEj9mGz7FQZAY6qQhGHk0AewPzmsakP9DagGcXFD7kC3IQM4L7GtKS0A7Jeo5sRg5nT7HMhuj32ty4aG7Qu4yTjws_0ksMJx2t_llYo__lr41OrINoDeUbHtzW_hNAxQsGH5dfG-40hNRTAP8WfQvlL4pvql-tJln93rMV3QyYJaLloHfOmVTe8UZOSW_zG3rgFMxPT91g0mwqVm83lrN2xGBTJTsbqQwjNnbbgUHRxSi7qe_zXrVK7nmvFRl1a2KfehkNKn_4XcIMmK4f-pLkrGfG-BzpAmCh53OQL7f05L02HipOrgYleWWmEsxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUha3p4GpPCE-6l7t02l_bEv0gb_GfcVhiXRWu5YXfg9dg6AdGvhYF0odpHaxjB6WsiQYLF_s_Fjhkhjrys8NvtEs8ZcxCIuSQJx8cTqPwsK_5-dU7SrJiKvZ1tuNFRjkCvqPFqTwR_LDjHKsnGgc3DiDgMnb1nRcjw5TmpRjrvExzVbnglkSpVw7J_qJemTD54F8wDz-DUPcGhBimQYhpuIcwHInY4s2OGMEggVAEeVtfdpbf1zzENNk77DxUl2PYEMGFV4t-GyMz0P7RTMcEvFgnIkIYDaGuNyZnHGc_loynaKQ3G1CLJVMbRDhIB8PD8NtxUeuu-_zGOAalYHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Mk1ioHDvmxLYoBXZErN9eYbtQuHsmQdcdNj6N1bi3--e1No-fTRphkm2sIDa02z94YTgKAGQi_LbyiVgwsVHkK7BzJsbP3RiyCve5aEbgQHl0RWMmNoKHE5oB7vOfYdBSCrM6hrYEr5nbqmVkKRAW8JRyCZiPvU7mbnHWNIuzpofQeu7FET2K01qDbdDZiIlpSfIGdKs8tBY14qBZ1QIvEW5gh2M7FZTgZQvHvk_znIso1NwesKWQXCiTdzR875eMEGwNm2gDM34OV8TsuA1_edBg0rbnhDyZkGnk_7lFJolzjJu0EYxHiW7hrzUEDH9SfaGRDtXh0BoHWh4jGxFTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Mk1ioHDvmxLYoBXZErN9eYbtQuHsmQdcdNj6N1bi3--e1No-fTRphkm2sIDa02z94YTgKAGQi_LbyiVgwsVHkK7BzJsbP3RiyCve5aEbgQHl0RWMmNoKHE5oB7vOfYdBSCrM6hrYEr5nbqmVkKRAW8JRyCZiPvU7mbnHWNIuzpofQeu7FET2K01qDbdDZiIlpSfIGdKs8tBY14qBZ1QIvEW5gh2M7FZTgZQvHvk_znIso1NwesKWQXCiTdzR875eMEGwNm2gDM34OV8TsuA1_edBg0rbnhDyZkGnk_7lFJolzjJu0EYxHiW7hrzUEDH9SfaGRDtXh0BoHWh4jGxFTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
