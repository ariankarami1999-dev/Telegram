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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 08:19:41</div>
<hr>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6tZNI3quD6nOf4FYwG3c0IY2VbcbEn58ULE3wTKPRplKtlbPi-7-8jS87Nu7mfOLC1PXCLHhS5zvhdfOn1AYqqK6A52-Cskg7I8hKO2DfG3kKdu9UDaECpeMX612XIwokr83JnET9ZggRZdtFhR3TzqZ-atjSD372m9V7GpSpm6gq9N2x86WX3A4t3xoQuF-B4hjVFMGfkep3NKgLURoD4e6pvYwnGC768bLTIIYtmDwYbN8TmIvNc1fodTbDN6RLZ3Q-etuzPdgkWnvbopPj9X4Z11Lmd9eJoVWh4hDP9t7fPt1aMvfi5J5BDBm0-9llB8QcZM1daSiHq5uHyAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jut8cQceE433CeJXf-9_g1_bIv0qU6giDxbpJgJVvXJbKl7UTJPo-DfH5AxDhgKeG_G32gnB-Oziab_FB9LLyGLQMIVS77wMRSQBI1wvzoX3BwIcePIUNbjDYY-UlaEM3ZhFPMfLav9CpFHj0jAeCM5I2xPghcSwhUmha0tou9OuhRGZxtVGlJjPxOhkyHKTe-2-SJqZp_WK1Oknw83qfab6U8WDLQ62SgFrrbOMRB6RNfQGFzLlplSfHIN6yM1kGCZld7aey4a9kMhapREtb2FIiWBrOX_y-Xv5KEvhkQLMzLb3EULX4PA3K__lFA16otma-1v99gtygWBggTGeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw6bpaBhOneVqI4HAkwRI-n4FmRNhSz5954foGCsGClRm5ldPNG_Y0VVx8NxSvl8jqIkKjtV0aNQ9gmyWeIg_Zg8I2Xsk-sVGj5eVUv7yBGfiT3ouwFd6PDrDice1397dgubbvOTPktnVliKyLVkzhhlXzGWrJCqtCpmhf33P_3RVm5az2yGYtRipgD-AXFI491fnACJKYMAGe35SLKdoWXgjIzHNICWy63w580RNeasTSnDd218RWxRBLTzg4XL-wgTESVKJkctWumhAzDFoEeAtQDMJyjnxy0vbB-kKBFW7TAoQ64Wxgan22HGAZ9I5uXQOR47486KiG_lhVBZBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZDC12oBufPddG70KmZA7zjfZUPnhmKYUvV4aUS6WINeP9XbTstDi2fAL5aWRr-YoJuu9Z6TCAFJYbGBmaTQMdbB3Bp4wF5luQoxVGSLa372BO7ODr3I2QJRGPYWPbqfA7g_suaQw72TZdKtaaoDP3StWQVm3FlGBiaeO0lv8odXQUDac4f2alQ4XuSiYpteXYxwt1zPkU0c0REjBpftlfyte3n1Ow9HrXbNBDsdP7laTJoPhxF2FRnUPd36KAUBT7b29j2JfhKCGD42ar7uVaxCN35IrS0_42MMisGd9AP76SJozRS4qwJRuTHLKZaqolpmkP1rIOZHmnzGh44-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7qvoOItctJK-VdGQij_2wFAAVfwkf9OS60ENYyKCqeqehDSVHGKLOAn63k7qtetDOH7E3zqof0upDWIKV9NiQUQrFUCyFTRjMbnBRH_sFvBGIoFFU-SJIH17OSShXOKaKGT3sQXze8tcSegdh13hmWdEZuIA6FKLIYN2JxkEFUKGbnqJHsKLh67bAI-J-7kyXTwZpjLHgHWiXpNS_u9jrymtS9suSEIR2LJM0zK6VdsfcX9hR9lcEcx1QlGBftOa4jaZDLLIgq2UArmr4211uwG3c_f9w3oIFhYpzHsMxIfQHUSFkGWo4Pc3zi1ua07QO-MZ5MkWsISNCNYl3VBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-nVsNvHD-fXqJ4hYoMDj--TalJDReMAocadhdcjpG071GlPW3qbqb2M1c1YPMj_7-tJh4Shk7MPHrKPGmei88wmJoUi1m1Dd78Fl9kUuofffGALxkhBPcL3iH18ROyYisVudVX5c4y-VZ4x75OUI0Tgd6NG0US6YUiE4ehVZ_eM7SPRh4ajRQ5IQrEMBqFnMXExPx13zyLbTKr6BSfdavfnquWuwqc01QYadoy-HQanI7zSa01O_3KY5c0kaw_0fQE9LHzmCfKliojJskXndWxLldbHl5derPIEbvHE6z677CkaV3Db5jmk3CLxiY5CLmYTwfYQhTdl07QLJ6PQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWR0F0taF1ctqMdfM1h9so9bW_B3JUxh1aJe1avLLFXw7Cv4Q8CHXQT-ozQseL2b4JnZRRMZEj4vCFos3tVUQ5BIvzWsfWYo7FJECZ81eNJ5Uz-T09_EVmuqlZFdWws8eefhJfMV3I41KD5TaVE1Zc4HPJp-nbswCVJxTlZKLyHL8kS0rW8eDrzLj1FezBBRd4JXV9FfsmKkyaQ1f3svvrO7Sa_vPqIypt47dz-TVpQ02sL9ODKTNwpOh69_uL70Ir6nXbO0xTzmuv-vFyy5Kynpn3zQA_iPCDRLsQr8GGz-qgW0--yYOrmOI6oKD-ea6_qsbJ3dGRlO0lyyhecSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzNBEuvuKFhvosmDZEZD_qHgdiES36oYGgbV82oIecEeS9rGiVpEnZ58AgmTh0hkIoPJmT8MoG45iHIbOkrQOKBPPytH9JaK8lxl6MeLThaq5fjFuDMPS-Ji9sedJP6L8kMJqctmUWORMOWwbatT-q5JCIL3l57lV0lzg6YrVSWAf6ywU_gTBApcXyiw2xJRY38gfhcb-iFdNJCQs_qkphRlLpgMrSon449xoL0WKlV4TWUho_ncX9rRuBl_21xvdWqGHyFxqKW1vBcQbv56LiTLIh_jDplKS7SxUshMfeO1pidEzy5cydQePF1spWz-bSTBZEjhdjkGMmzvFLzDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZscfZsJaB4umr5btkTkFLk0GLF2K4Nm1hCa4KCALW1b8s1rx1uVAcjKhc6yBPpR76vvvzLOegkqjBBvXZHjNoXtwS5SM7A3HPOTS7YKymS3h4qkXGcQ8Iew2SINoWph7yZ3SRtwSr105zKDpQzJqweUSiQFZr_fCou3i1At0M6CASqFiChCSLe5RjnSI8yXO7T7z8VDB4ETNR81-RkYBMUP-pLlkT8q-iVHSj_YsbNirvBAzUl5h9iMF6PsAV_jl6VCmpOniubJg7ZqgaA6kYk5io1yvuP-YHemkqcMloT22NE2k1AboMr5MaNXedvONvyiVFwusOHCQez7u8AEIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKm3ABWCXaR8ex-vJeuA4HCrlpoJOl56wWM0YznNhtl0CAs104RdPf3gO3Ia7_VxJpjknXOuxbF7AxrjS6UcKPO_tWGSGZi9Yhp17g8ClkBraSApdrr7A3r-DQvkRbWbB7E_P3rNjD2OHnEQyGTapND2scBtj0NFxIwqstCw_sxl6mrOS4vrWrl-zESi-VlPjwFP_ua8t6mohiFMwjj37WS0cvnL0ZHQfbzHdEhfpmDRLXzx7kar7XE_AIiLLpUypHXHKGmF1PQ1Gn5We7_bDTRsOzAhCgqLy76uonAMjNswjvP6-4KClYD9gQgSZR2hCA5d8an2ZzLJ_7aOXgKePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CseJeoc5hJk3h3vKBolZyJ8FT4Jl6_pqtQMLt0LUF0WNoYi2KWpnc32CXxBIn-m-XK0iNiYSpQu4zh_N2VN1ERYdl9lOS0HOSZvDkXj5XcDBQOqpMj8U5u4e2_tRKqaV7ZrzuQq3B9DVGxVMq04H5S5RwJ3Xn0nNvw1pJ5FWr7RUGnAWgccFQDomsCJF3t3CwR4p92Gyvz_xV8vZrvvm6UrSde0E0mitXEGo0WVc0UDjK0S1IWeQnHzr8c0s3tQttL6vwS4uSdv_SlujM0ADhn3tBuxPnmCH-iIO-snLAHO1IldMXSd8Hvgzi-ff2iEjDK2gTBWSKGkGqkSSq_4AEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCxuUpgO8MfM4yU4DRmH2BVDrYiCUNMT0APl_OnfSMZ4ogaohBYlP-iGNA87FX2ln7GOcQYPe1gvGiR4npi6VGRBgGEgVlIedppXkMdpfHkuzgSudZwa9bdcsuphg9fd0z5OjP1TaF3bIPCRPQbbn5FzY5EXrJRlezKWwJ9EQOvcG7_2QI7hUCEZLAqSEt0nnhbQuLXl0sFYox09SbpReCfMHsaFeMC-67-otNvfVzp5xknssWynbVwNgDc9XZMbk-DkvXw9XCChCexOIRPlXdifWg9SR4TfXzRj4bpieaSoHrmeyhVcvNLzMuCDWlSk-hdCDnD8yvTuRo4ovb0olw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB-WJ8knb9jYMzDZd3ildLyYPBae_2vaB0Vx9-jc96qpxtL695BdFs5hLCE5iZ7x_pK4zrWkdB6OOUfkD7sFzbIu3gQzYFZWzoHXr9xPFy0kzZvjZCrfkhLAqD3g7mQ77nzWMhsgz0KnifOD6Ze0C-7G-FDtHI9PrL9CHVPXjGdfPbdxvVhAN0c9WiGAUB-b0iHqL3YwOTlkK4VZ_mP1w4dFcHW0QTdT5mc-bA0a0q5S9cDLRwJ62_iujS6b1MGqsz2DRwKhlKPkd-OlFnebjStjMsDCYyLMKSeL59F40CAICDuo36LPy6Cxx5RhGPrHBZ8WLBvtchQ5VqEbpJSQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=qUFYB0Su5r590BUEsC55NbOUYyMDugkBKgeryMLnQOvQRkKqtbRWYOTBGu9IDTasUlZDaY5v3sLBkc1crhlE-LwIGaoS-rkeUV6NXXZXdTtr53B0ZQu70vr8s3IgfcRq8H42Eiaf2CNlEJCl7u93ELKxSamWatZsLYR5Aa6WsvZTqj6k4UdhxxuRf4C0U8TSU3NT7zCZeReKiDBFObqb0Ct-JHAc9zKnUV4RvCcIXX86jGEh3ZrVEORYZPQ6GmOs8CliBFv4enQ130Ehfq9Nxj8616SiVX8i5UDQp7z72Su-SYII-sLher1XY6DTCMUJr8IduMC4O7kHX-6zHfEkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=qUFYB0Su5r590BUEsC55NbOUYyMDugkBKgeryMLnQOvQRkKqtbRWYOTBGu9IDTasUlZDaY5v3sLBkc1crhlE-LwIGaoS-rkeUV6NXXZXdTtr53B0ZQu70vr8s3IgfcRq8H42Eiaf2CNlEJCl7u93ELKxSamWatZsLYR5Aa6WsvZTqj6k4UdhxxuRf4C0U8TSU3NT7zCZeReKiDBFObqb0Ct-JHAc9zKnUV4RvCcIXX86jGEh3ZrVEORYZPQ6GmOs8CliBFv4enQ130Ehfq9Nxj8616SiVX8i5UDQp7z72Su-SYII-sLher1XY6DTCMUJr8IduMC4O7kHX-6zHfEkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i00pLP2LVwjoZplz_NTVSbq89tEU4Ksh7Xsp_R67fsYCzIBUcXSqjounXr2M26LLHNC9u_boFPWr1rRfnqJZPWVijAbuADuOdgd-s_27hVKerTQSD6oTkynHvVfTHVUbcg2zTdJxv6FeFo6QSg253hQVSlV-fMCSJkMduHXe3OIUD4lpDQKUELQinZfhCgvqRDZDZfVA1lCnlF2VF4mvK6VE01Tvj4gBzdbuZ-sc2KuLTI3NBpOdHHZfreuVRyoR2UJMRbbwTMen03VtJOYOLfy_dWOJNlWWTQQ4sxQMU1o22LafAbPEkSv5-UZqeYu-uJxNbUz7m1fKbLpeyx7qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=kaZNuc6ZWcwvV6VbuUI1Th70FBF7vXlvsoweN3bpG3nOOBoNBHLnvAGkdFB91DVUgYYQpYbIh6hFlxw5AWHxHsYRnEPXnbTiHWoQMZIoY2sp2FYpJO5ilOOVLtTdKFRnRSeKQnADVC9Ci9E51Iqr_2dwCeZ4HagDGiiGgiTqNRQR9Vr9ZNS1PfwNGxcdI7wIZDsb3V5f4XWE3htKrQn77nqv1ElAbhs0Bavu-CHv4FwE6zcK0iJlmoFJp8PjL0A6HE-XEJXO5DWo0Ea7jsQ6em-BY3ZCP4pNKARntKijYp_PxlpnlxrpJ3X44o4sK2-Bt8z_5CxA_WVMlI_3xpFScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=kaZNuc6ZWcwvV6VbuUI1Th70FBF7vXlvsoweN3bpG3nOOBoNBHLnvAGkdFB91DVUgYYQpYbIh6hFlxw5AWHxHsYRnEPXnbTiHWoQMZIoY2sp2FYpJO5ilOOVLtTdKFRnRSeKQnADVC9Ci9E51Iqr_2dwCeZ4HagDGiiGgiTqNRQR9Vr9ZNS1PfwNGxcdI7wIZDsb3V5f4XWE3htKrQn77nqv1ElAbhs0Bavu-CHv4FwE6zcK0iJlmoFJp8PjL0A6HE-XEJXO5DWo0Ea7jsQ6em-BY3ZCP4pNKARntKijYp_PxlpnlxrpJ3X44o4sK2-Bt8z_5CxA_WVMlI_3xpFScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGDEhhtKrIxUYkAt7gR8PMAxYH7EN0ll5ERM7suRhAz8lu76MrYJCuqz1ywJxBfKsOdLHKe-yDVas-xrNfr2-LutaB0-HVozOimUqtyc_dLVaeixxdRQbEQtla8e1nGf3_OkQXzOlewbjVe8iiQNfpSYYAEZIy0LHPXTH4e7h93_uEyNmjHCPlp6gVwrXW13pR2KTI0p-f-5jPsc3DIBaRHZDqfGQ4EeRYN62rFMZaBE6F_ztGPTQNKwCQS6x2uWtalYgYWMiLM5mKObJCXAIRNl52YQXg96dzc6v6YIbdWGNHBAhalLn6FufEoC0uUQrkKZbTo-0aKYZ-ir8jbkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub6rTHHmU_0wExBMdQZoikzewDQF_pl9BwQt5eNFVLuVJUsGj2adULXYOmk0O0XGhvHCokKMT2TJxxQUNCWyrsFyM_0TUwD3vNdKPnThfwJnJqqdWkcheITxuop3M0R1F_J7l5MrdivtJ6dSd5Bx1XaMnw1dl2k1mzeAor4WUsrufz9iRZqu_5LOycyFpuj_jib5gnLe7UV74sBPuQbMMg0Y4c9rmgLc-lT9wu-b5QeXyMX-I-Ijxz2gNCH9bRdIMVlV0IYUBVPBlHH5l07wi39pey7DNuG9f6FpKKXeHhpmAdCgWbhNDdtzLM57HzoE8_igRVGzPXR80q_kqq2ieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CI-A04wVXao4aDUDmaK9CVsEX8WlD4ad9BM2Q2vSpr5AUqQH2VEmc35tuSk6zTdPd7rDRl_BCHeCvEL3nK6VEzoOwOzUb8JVXdBOBuyHMn-eySRGWrH5Z8G0OYejcCDCpQT-obcvnWKFtjB6qPL5EnkI_R9ih79oNrNrrMdwCKTSbf-tC5nWd9nhEL4YWupLY8dmGvLOjEx8-ujuO_k52JDysGaW7j40rJho2fewDTreQYxYCrHVKnp0hzFBw9AQYPxDasF58Wtod58_5z4KEUwM0BwfuwS-koaBE4AjnTmSGgR_UQlC3yocUBX1y2cv8LDnvMXaKbmn8BgPJ7pbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeBuJsM7fTiJwqZx4QoegjMg2XiBA0PSTYB7X_tmLIWhugVSr8JSxAs9X1p9Nr8B4g7lagHQFp1PgNHdH7x885PrgWGsIh1qSt6tAFQMd5RMu5kpON0lL0YJxGh7fRv4jg0KjI38ytYpSTr1gJqFjmVTM0kiib2L5FQHBgpklCu0rcbtciMYbReZwvcjPFUBYDa7iYTPAkwtKvVzJTsQzsqnwpS44wWTIGSCyLBg1_kuJN8pNA3Hql-rPnQw6Joe6i3SLa6XOQ4uaPiZCjQ86_acAYoyowQqtFSdi6suxN-HTnp97jQGD24tGXjiYgdrvsPmGdioz44kdiV2pqviww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELLBSPt2vBQD5dRqoCCSFs2SzjnhDBXmIe6jfo_u08goihSm2fL3TozDX7Q4FvMiEZPwfEBfV9kNTWhSkUFI9DdcEg1VZZ0y00oz00Mwc8yIr3w-9NSm3tIbY3HHZWIDu2XKqEARRNRZ6plTUAF6S2LPPIHUyvH-V8JMr-mslhmDvlx9tLSet6j317cmcjo_vYJCEM-7bDURLY52BvI_iT58EdijWSOFZ-VNW8KULgS-vY0QeXWdoGmAondCPfOib7lXwMPdI5Y_EzYvUbG8469SMahmJwd5fNbt1pz9Aq6qvN27YhzI9JPOTUMtVv3cOcuKhDdppWAtMNfyAWEuww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyrVEZJaU3YrT99NjDi1ZJpQRt0WaW68xML0tcSDay9AhdL0r4JOrGIRYBXnYaawza5Xn0enbpdyQbrOXKqvnog2RDbbcCTkXXpWVvlakk8utzEWLEAlGg5ABDF4qAoMCmwojL61_M83WuPP4uxHxmuYH46ra-WleE-MhM8TX2R9KtNdVsiApunyZ1369WiD_2JmAWELHcko45janqeISNMcehHp3ZfVvzmaS8LCbdMF791U_bdBB-b_kCfEITMH8KoADHKXFJrNMt245qS7C2NEZcsrOJ4n8P7wMQ_4Uq2svU20U8_H1yulrmOk9RilbBPw_BdNEZkc4fSMai1Gzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYzDop084tshK4IDwEk1QDEfDmzQ4SEnjZL5xnRnGcTo0uFoZT8sVVQ1aQcqH95iSqZ9I7Brq1pBb4ROWhfeni_ZtCYrDNAt89GZtP368WApqPKCtjAN2N9igg6ZkibtguT6rhhNm7t5grsH6tZMPy7OPWSOiIW95FTPAGnxwhIpko-bKCKxcQ--wpWqEYCXzNWzIVC_N4lstH1TooCIiYrjH44mjQDcyTx0tEzGzE70pvEvxowSPd96QRuaLIJo_RIXnCSSVA75R1rCs__ndXJNYVGvCFpF1FCPeRpE1uevJEbEu57rqmCCcnya502IOc9GcjAnAH8nJy4uNnUDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2KkPyIVQte3IHlUGW3VLJgFCHoE5FUUFB7IfwKWyHO1W5F3aYiIY0g9ds9Gou8R8p79AswNCNHs3Sj0SXh7KHdahIcqoFgdeJaS1s-8GtyQ7n54moLfAPc_s4DSgjkdSpH4x7fv7eb3-xUtjR7AOLXGWgr6Ew-1naP0Fpv-Edqk2JnLkyrTAADDIAa2-YMwX2din4dtZqIOvjr-reNQ-TfPFK3dxCLhqt-wsP38N6Q5vPjpka1RyIwgoNTbUwCjts1EC7rfDwZxWLK92mQCNVoAFI83GKZS-OhYiFLQzbU4X78oid5CyeGhW7JOlEy_QbbIZGwY8mOJ6QqioEq_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQ7_VMFQRvLafJx3cKuIln9NUkw-9WMT6DvjdixowbmuEQIkib_7TabPmJQfrNjVDv0VO7i-ZMGGWVR4QntT0YE6QOJJJXuXZ0KUZdiF220jrTdqNx2WTN1yrNA9RWkuzccRuQCXaibTDGC8_uKDjTuBcaKFWvkZePjWEN1utEIqQgv6a7ppZawEUd0lWi685mhegRKV8Kcsc0MD2SBrfq8mYDRaB3YMC7nfGXtTWR5yc_Ft5Wt1_75I5Gz3w6AEucifGlKHTxBokTfeaUEwp-GhTViSR-EVy1kPoom3zKp4L9UzSsxYqadriYRK_S-tDSC11F3jU4G7GIOP6wcrvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQAJewxCZVveucIhtu4N3qJCSu5dp0Js9cbNPTWSG4NYMBJu-w0WX8jbnOOgbKd09WCXVawSmTuEvrqzH3nLKsligEGreuzOputPmLI8FDCf2iwlqH6mcCq3gz3GykgFKqkWBk0fM9XorI0qe0JOWpPTC6VLrOud07gYZ5OVgMNU_lowbcW62YcK01ALZuCtsE08qEbVC749L1a_pJUJe08F1UmNdZ7RZMIHUrHEgQaAz8G8Yv6PzVVw9SABVCEULtHUO7V1dPh6IwhfW4lADbEPcAZxo9a2RLJTc4H2APrmx6ZRJlg_giatYK19_XCeo7rjGtejaGMDjm5n9ApqcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTiKNkY2q6OaWrKmxurSeuVZXgGjKAsRVx39CWzA6gJF1p1XeiaRFEGHXupmuHzwm6NqbdSuNWYiQpcnOWoSskkdjYvk-ZmZpR7Gl9S7dGQZm6XDyuklXxkI_FzZWe20SJWt6D2nGbWqp0RzSiwUbYUV2Fv16z9hYm9fJm97WPw83uhEwM314jGKDZ17mHen2H2szGUNdLfn1fBxs3yAc07_uggiLgD9JpQ7WStrsdz111fAGMkDg7Vawx0PV7L3awzHtt_Ox5jYk8WwvS3BRB5SBOeJR_HcCRdDQ5KnFMkUTCqzyNfIZCekvA7wu_uzAzWDzaezitM2fD_An7q6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lODL76og3WcV20IThzIGHLkjgeLwZC3shz2_NVl-jEOW4bQSorOqEufpv-8YRYOPF0U-xPasRmRmsy7fNJoGlpg00583qHaCDL7_up8X-Lvb8JCpacxx2TGsUrSDmMj_j_bIMnjtEYoUMndd-de4L0v3QuOfKJ8uO_YyuSXBZHw4x2FXY5h0DvsfZXLDaddxf23c_lc41g4g46JGPVmOnWUre3Wm050ZITlOLbfDQ_Zr7PzCozcb5Wttsa3g-DCdgpwiJOPKldFfNFazAHLK8gxmT8rwSs96554eI09oCiVImZ0CxELx5gB_k1CIs7JaSBUCN-FYcsgqTvo2kOaftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xvwh6QNFCKXwUTA846jNvYR4ReHMAYv3Au4vKLfzek4wAx3ZJodAfcv0cNPj1bm8rNNVv5t8dFsM12-OCkG9H-9Ls0hc3ZMXtwg8fZq-kASlfFQYZA26q9O7X1p7YJRCE2rgVUejX1LRhUV0p4NefdQRUhBLhYgrZyXu-joKfxPQ35IHSHvx1SNfX0TLm4gPHHTyyNjF0KaA-yyn5ItqHiw-KFD0Hr8G95VPsqNztXmGlsMYgO8Jy25scckU9CUDND8vmZwwnK1ZdZGd4zxZH0kiX8D8FJkytJqBtiz_K5lQJk1i-7RR7qsUeOvnZxZuV5tvOrPY42tXTlpJ-jj-fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZjB09dDZl6qUY0RQVxWo1GPN6hPRdTVOZxYithNbq9JOuvUXGfXW6VH5uZjOUeS-5dzbRtV-mIcT_h-NbYwQ1FPOSVGd1V-5J8nSpJuTVoYJR2sNJ0zR2_NJ-hjjVFTvFy2iiEYi-2VQrQ6FG0ET0NyKEtFdAWXZPPStLGr4h7m6zWj81qP7DIDejnUEpJECp7xU2yLG7LDeeYpLtMjJChBSuB9DP6Z5zJGBldf3a6-NeRmAmlBRww6Yzsq5q4O3nJABRzUeTfEWNpPSxUYbhvCP0JU4Tt61x-8jafihbJ6FU8rq85H7ydasqq99ZPSf9UhpBHLY1qfRIUFwlQDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQTkLx_gio3X_VxTX2cNeyFwCVufhiw73X1BXWyNQYC-Na0J5GnVeN90bsF3cWOG_tB9A0sryjiHWcX_20o36ruyASSMYlCVCUdWALalM8NYeEm3nMoW5pSC8kR1UH9gopiqO3jdBixpAj62auyMiIvirq6djrktlx47O9rvv85TNZe0HRLwi8xes2d8ry95jrtxbFTGPVPIMBprfBXmu6a0IoX_RuXxdhWeSFYbaJ2WNCm_yJjcoPm-srG8m7FhF950ljKRL_yYNMfbVFX8uSrMd6XtQyRKh5EB3lagChwdemlEGhv6ipSDTe4l1208G3Lmia2gIjSvuRRxOloz5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSmExRVBymxvv_yUX0wM2wYrgcFam-0uZpAULkQnMe7SH9xFXYCsGjom11vxynv-oHBQGS6S1u4G8EjVysaFfHTdplqeMs_fbkkIlJFK6NdhZrEnUrFH56gY6laVUQI6PxmA7-h6BTxrLPobC5va2SPFfPCgxtpj-or2cwiNFLN6kbIzvTUFZUtVaoG3UKI1VTGZPsFb7SRS00wXlnD2KG7pv0aZkbs4hPOZ3KomVz-wAA7c1D-aiq1RkuqLHdA6YGlztiwDOrn1fawAxvyxfBXb2GYQU7doK_SvZNKxKATJnsP-Z4tSJFO8kuqHP-XyIVbTtEsQR6ikJ4oqywC7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=uc7Ohgp7LCzOkcsdm5UD1l5AkHcAeqgGIc1VPIA3S55JZRlaDRP5Omd7BS7_KtfGrGV3FhyBiM4crm6YCbmPC2ztNPsb2yXSbImIenq6M65Nul4Ne72stk3pJopZQjCFVjR2B0K5nTXCri7Wcxd9u_O0q7yao6HALP91bMUyFpeunGHpixYp15LUd6eyaxPJOi-H24O53hL7ubb1e5w2n9W1QTG6YltAPLjB4eyAeaYUD9PmiDlUjCCxurrltmfVMKGu-2dxN5izZ_Snr4KjX6w_yVrK3QzUwbDmCynfsc8QXz_dGPbOEP4dYHRTJyaKYxPXzgvYxHtKmbWvARV3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=uc7Ohgp7LCzOkcsdm5UD1l5AkHcAeqgGIc1VPIA3S55JZRlaDRP5Omd7BS7_KtfGrGV3FhyBiM4crm6YCbmPC2ztNPsb2yXSbImIenq6M65Nul4Ne72stk3pJopZQjCFVjR2B0K5nTXCri7Wcxd9u_O0q7yao6HALP91bMUyFpeunGHpixYp15LUd6eyaxPJOi-H24O53hL7ubb1e5w2n9W1QTG6YltAPLjB4eyAeaYUD9PmiDlUjCCxurrltmfVMKGu-2dxN5izZ_Snr4KjX6w_yVrK3QzUwbDmCynfsc8QXz_dGPbOEP4dYHRTJyaKYxPXzgvYxHtKmbWvARV3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7C5ooqwLOYis180gN2hOLQ1bdQ3DG3fbXqWT3djlEoztl2Tllx8fDlscvVvj76QTXtEMZATBQYN-KAoIgzBJhNlO44j_pxckblruRf1GS5ZKvixrvSL0oGOgBQRxhCT6YISg83aii3bRM64QkhHd5lw8n7LAQ4glC0prs7zD8eixXmKpszxOOsyxsw8M3DzHgRWZHoleVTFgTPHvAr_fJ6ekq1114-HkR8sWthrXqb51BEd946JHHWSDszDuTi47uPw9ejTk2Sof3W4DLaSeQO18LQrkXHXpsEz4Sj2woEOJW6CddAbuqEcM1Ybvt5d9fU3mCIrWAXSbm3pv9bZ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOPGs4x83PIgTh6TaXb7BfaDOpW1ZA44nhy08R9zA6iYqlOl38ORK4O2MywH9ePVMyLGtifrklnOxqveCG22TGGfKtDdltXgWE6Kc8nrAuqi_d4Jlu3L2IPYCiqM2Y2OzDAvQjhirCjV0bt1CpUI9qafkjP4Paue8bbT_IXNZkQhQPTJ8D7n7QMzLCYJn7T0KoWAF6pinszMO5FplzB-WPN0SldPdQ3I8gmkK2IXyiaMcGNPdGC_JIcZQ_oZFUXoLmwYowhkI-O9J9wx4bwWscPmvONs1ynkqXOCFcwwvnW7uJia4kE2xnXtY7Tp1iATkzh2izxyKQyvHOkxF9DH3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Marnx3cAGx9cqSYZMvvH-CamW_knJX_qQI9iZgIrAbhesYeyKqFe1x6CZ_FtxmLP-rhxZKc_qtHABO8pWLustOOeMuoxZ-d7m9QWj-PZoxEM7YVy8hAeFxzLTu_Jbw6YiirFlu-f-cSz0J9djpDiaR4p2gZKrPkpj7g0s62_b1voa5BAHdBLIiPDYBubnwhxAxBPw7wJzsrdG-C575S9FcCVOtR6zNBTtpyCb6Pu_rWAywV3_cSIeG_Supr7uoiy1j06Fh9_oAC8B5XZNMSvAfiRODHWtPTViecHDu-wsSsf7ESIBEmLV4_bUG8hyxGlm4U44AMvfi6sBx2cyF2nuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=RdZHyMDTNsaO4s-kg5vgqturGwtlUZU_GdIZDKXxQCeGtfA8h0GTEEd_pKxlH_JI-YjQ1ke01TaiWbgTV2P9qo1QLh4XRyNEkz_9v4zjic7cKR1x28QXsMEseH1SxnmfjQBOExYKentBnE90HUV_vzwKZH_ijpG2JBLlSksWOGZnfiPPaUDforznq25QuLfzZRFTUhEHFsl9oxkST1JzqQHQ1kcQkByPFrUXUWVTz6QsbsnYu5VLocJzN48vaPgdsvvVmAAZhL9XHX8JtEr4-2yPIXPLX3dnv29ZYcJluV35WI79SIRKlall68DS2ZIT1IyxyKlOWndOKwf4NzIbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=RdZHyMDTNsaO4s-kg5vgqturGwtlUZU_GdIZDKXxQCeGtfA8h0GTEEd_pKxlH_JI-YjQ1ke01TaiWbgTV2P9qo1QLh4XRyNEkz_9v4zjic7cKR1x28QXsMEseH1SxnmfjQBOExYKentBnE90HUV_vzwKZH_ijpG2JBLlSksWOGZnfiPPaUDforznq25QuLfzZRFTUhEHFsl9oxkST1JzqQHQ1kcQkByPFrUXUWVTz6QsbsnYu5VLocJzN48vaPgdsvvVmAAZhL9XHX8JtEr4-2yPIXPLX3dnv29ZYcJluV35WI79SIRKlall68DS2ZIT1IyxyKlOWndOKwf4NzIbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8o_wVWPzxtx9y29GuRv2CR1fBOFnNsFxJwo4rzjX4A13r0TPzNWDQNvmoXTBRK3OCpBzVDyxRKAO7mquop2nHaHoDyE0RYzbSklgxyko12X017r9WAZEV7mTLpqFLKikYuxqnxJb1f3JNUO3j0KBD1MDgbSjG_PPUzraKHckAVa9TxPaJ77J1QkZI2Kdwrr29ZZKRsFVC-1MqzrFrDlopBG6etCAUt69LyYadxlBLlCFYxSz4G7_4NXw7solEh0YE5J0L5ACkJWaRauNMtWOXDABM1ol1V6ikIExF_iKToyMOZ7B4AEsC_QcGFvdtno2uUCFuP-bXYqX4-v2cJN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=crqQm4mkgU_o42-iqyLG8t9FayyQn8Q_4YNDiUJwAAXGCL9WOQM0CnO0Um2ykCG77lF27UahRUFSh_e3pn9XmbPttO3CrbN5eHSO2-QFAr13vAntuSmpYl937FN0WQ9kv436-M-R00VX9Slwi80KuhHO7tz-zb0afhiZq_1mTPGO4vEJQE1RbQqqDEIerUXJBO3rfXXvQow6Gm5UQM8P7AbHjfj4NfSJzC6BIEwLXs2htqMeBj_e0291-m5RNPNjSaoWg9ZoAbsKxJQhS5zii-qWyEHio-aU2TjFRRRmf23rZjiIxfPh4RzrLj9JVvjd173mNxw8Wp6ooM94lfutAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=crqQm4mkgU_o42-iqyLG8t9FayyQn8Q_4YNDiUJwAAXGCL9WOQM0CnO0Um2ykCG77lF27UahRUFSh_e3pn9XmbPttO3CrbN5eHSO2-QFAr13vAntuSmpYl937FN0WQ9kv436-M-R00VX9Slwi80KuhHO7tz-zb0afhiZq_1mTPGO4vEJQE1RbQqqDEIerUXJBO3rfXXvQow6Gm5UQM8P7AbHjfj4NfSJzC6BIEwLXs2htqMeBj_e0291-m5RNPNjSaoWg9ZoAbsKxJQhS5zii-qWyEHio-aU2TjFRRRmf23rZjiIxfPh4RzrLj9JVvjd173mNxw8Wp6ooM94lfutAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjwJODRRBlQyEJC8BuxIjXFxH8ap6DpHO7ohpF_0Mz-LmxzjaeA-FrkmxhlQ_lTvXd-aPjrJMyDyBP_F8ApOboDeLrcHMux03g_STUZMcEE4OkqrW1Ij6EjJq5nsQ-ztveRt03wMK5bgOVFqLIqOdsA2-V8y2LGrQRyxvg1u0Gyk-2762HciCrMPsvIrSYExogkyKXHQizPt8Z4-9GKzM_mnYFrKPcHV9z_-UqcEk_tdDBbcijzuPT50H630YOROT1yOxmVaJaqgyGjVdHJWUjmLJz5d5TUbVtpTSWs0aO9QI1dEl-Jc7nn_5aiZARRy_Mp82Z4Aha-bMvQ5QiRU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVBO7cVRQlnVwj4RDSYotqb1H_MGzXEXBsI1WprHt80poUWFFJCvDR9BJqHoQXDmEuLorSi5K1lVDd2Sr5ZHm0jyPV_-kMVBILPT7D96DMPCo5EARR-7Cjy9xpPtty89Ob3aGJnCvtyn45Kdh59UnDTlQjV4lhTXhgft8YAs49VAQEyYuXGziMgNEdmPphH093zfSSP-vXQqyiZCALLbItHOYwkQrbGjWy5u2qv9MpwjNvICgYtXEv85AJxWhQcnqiMru-VRmzz0234wV2EDJq3TiFYm6iLifehTKJ3tdcAnc6QWyH_5-QzcLtwJ83u_iGuP4Gnf4xVmELU62C-ejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=Wqb5GvdZrmf9lSJn87Jo_8UCav3MKH1qQKj1ZQGtVnIbd_TNUF9LN4tAH6ZHMexyNgRef4wNjlOR-JjZHVnNReDgNeX2_JE5WTRSrNZ6cjXCxyadhr_d758i46iEhIcbQfa6nlH1Qqp5yPXFsedEfIjOsZn-rYIk-rRE4bwoz5CmUDE6QyPA7kxJGribc-vVbiuxNl0cHqNQLCERIdBS_ks9g9g1q8nNwFzRqmgebDDwc76NdVg0gTqN6WnW2F2zVVTjCszpwzoXux-7w-WwvF5CrTrGYBF7cTLmQbSJGjhpH6jmmbmQ51mHUV7cC30GB9DeBgl5jmvqz5vGloB8UpzFtZaSJrbecBV_4PBhrTGcfjxZTCj-ZSY-vUl7fo_cQFDTiPVieCmgUfeTZqL23PZA7e9-f9A963Rphk4GtoGpI5r4cvI9oviUIOOgeeTWqkdTIRye59OJQZc_YI4zOWiTDnYTvMaL4aAmRneM5PO9xDSU9al-ZxifLOUU70CpmcwqRtqEz7xCU6SZ5mLPilJ7xFUpIw2EH43YsqR0KlfEvXq3PNEIqnF-hlPZpk5PaRM9aXM_8mq8BNApBWOERkQIyZkTzp3KNsUwRj3WlXuMQ1r6o58zubkvmbITupIIN_wo0DiWwiln-ln5uUvV4676I1O-gvSW1Mu7uFYzxcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=Wqb5GvdZrmf9lSJn87Jo_8UCav3MKH1qQKj1ZQGtVnIbd_TNUF9LN4tAH6ZHMexyNgRef4wNjlOR-JjZHVnNReDgNeX2_JE5WTRSrNZ6cjXCxyadhr_d758i46iEhIcbQfa6nlH1Qqp5yPXFsedEfIjOsZn-rYIk-rRE4bwoz5CmUDE6QyPA7kxJGribc-vVbiuxNl0cHqNQLCERIdBS_ks9g9g1q8nNwFzRqmgebDDwc76NdVg0gTqN6WnW2F2zVVTjCszpwzoXux-7w-WwvF5CrTrGYBF7cTLmQbSJGjhpH6jmmbmQ51mHUV7cC30GB9DeBgl5jmvqz5vGloB8UpzFtZaSJrbecBV_4PBhrTGcfjxZTCj-ZSY-vUl7fo_cQFDTiPVieCmgUfeTZqL23PZA7e9-f9A963Rphk4GtoGpI5r4cvI9oviUIOOgeeTWqkdTIRye59OJQZc_YI4zOWiTDnYTvMaL4aAmRneM5PO9xDSU9al-ZxifLOUU70CpmcwqRtqEz7xCU6SZ5mLPilJ7xFUpIw2EH43YsqR0KlfEvXq3PNEIqnF-hlPZpk5PaRM9aXM_8mq8BNApBWOERkQIyZkTzp3KNsUwRj3WlXuMQ1r6o58zubkvmbITupIIN_wo0DiWwiln-ln5uUvV4676I1O-gvSW1Mu7uFYzxcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Rji-lwYuILb9Eg7_4nLZT7VqwRsNjaXMgIn4A70LGIy6LjwwsrjQBfTsL9xOkCZIdm_i6w1dKTvmm-Xrgkbv1PkCZFe6DwQEv1FZNYOmEt772PYhu7CadNEOJn_3DbK7y-7mNd7zoYc_RyB2wWk53jHlXb8h47mzUS_C1hmut7CketAnDXNz1vayINM1aUJ-dufRYwX518YygWuoiY7GU5Q2pDB88FoAwoKCB2bgvNmxpMBXkukDz4D8mUuvobkIop0oIBShNiwnhT4WlpICebuqn_TT2lj4YgN0dhUCgwpXwXVpWnt5VzN6DLSH88_aDrNn0GIdTeERcv_0PdXt2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Rji-lwYuILb9Eg7_4nLZT7VqwRsNjaXMgIn4A70LGIy6LjwwsrjQBfTsL9xOkCZIdm_i6w1dKTvmm-Xrgkbv1PkCZFe6DwQEv1FZNYOmEt772PYhu7CadNEOJn_3DbK7y-7mNd7zoYc_RyB2wWk53jHlXb8h47mzUS_C1hmut7CketAnDXNz1vayINM1aUJ-dufRYwX518YygWuoiY7GU5Q2pDB88FoAwoKCB2bgvNmxpMBXkukDz4D8mUuvobkIop0oIBShNiwnhT4WlpICebuqn_TT2lj4YgN0dhUCgwpXwXVpWnt5VzN6DLSH88_aDrNn0GIdTeERcv_0PdXt2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KznvBQ4HOm_hgiJeVokb9wYZoXNaiX4cR_l2K10duP9_vlhdmYaUhs2QQUYD7PJqB6EwONKw32d__HT65MvTJeoffcEoucUVPKF575yoeSUDSlAi1nH6VoXG3q-OECY6NGNaDX5tbdUOJP80j1_WFAHbYrWV_P6ynlSrD0UcY1lWelwdS4_Nt0yI4cGTtm6R80_ZDFUQNxWrlD3zSH598PG4JKKlLuPB48IvdwWA0NWzpwZH8dS4N6bjBCLIrWYKPSbFPhtw3esum2MAMZ062sLBYlk_dkjrd50cDaeMmOrncE3EePJXLUl3waBv_w-h3vDGtZXj4TP-7eO0yf6GZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Pv1_cPIWJAmldhNx-3ltdK6mmgjFN5Wq59UNc_Cn6p8g78QFOLZ8s47b9Sn8naeBA_Oz0OWUUxVOZtdqKWi4Wm3-hanLd3kjJjf_1pSilMJLZM_ddRupjzQYKUY4qPTfHi2Ap2nM7cme9V18QVGzSQvu9DqN2kaMKVHOGaVDkhckxaGXHDts9-KXeWMjRRypErul_hfaNc7Xb44Ik16pg79h2b_8m2wrRYe9RruYmypToSoctmx_5T5mbbdgpEn6hlcJOcFvJnbl_kpKofZxsgWmeG4REi1PJN_jlQJ-B8KLMQ24IZFWHoTEqFchcKDqEv5-cgEPlOWoGtPRFqHljDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Pv1_cPIWJAmldhNx-3ltdK6mmgjFN5Wq59UNc_Cn6p8g78QFOLZ8s47b9Sn8naeBA_Oz0OWUUxVOZtdqKWi4Wm3-hanLd3kjJjf_1pSilMJLZM_ddRupjzQYKUY4qPTfHi2Ap2nM7cme9V18QVGzSQvu9DqN2kaMKVHOGaVDkhckxaGXHDts9-KXeWMjRRypErul_hfaNc7Xb44Ik16pg79h2b_8m2wrRYe9RruYmypToSoctmx_5T5mbbdgpEn6hlcJOcFvJnbl_kpKofZxsgWmeG4REi1PJN_jlQJ-B8KLMQ24IZFWHoTEqFchcKDqEv5-cgEPlOWoGtPRFqHljDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRq7ogPT5-Wu9D0mzlMsFvIoAxmq4KnCngZRpV-FZkCLCoHRbEAgSOyF6MpSB4ZxHHYLTjxD1p0bybDnAPpz1dLHBcZLUq7ByMhH-PJ4JkgvUbu8NjdYZEs4eGc9aeSMBEX0mcHhZt4OVi9A0uJhBCx5ndXfUJ5-jveuMtNLlIcwx40573hv-W5lpKAukOKkQE7hRwsI1cCUSeSx_XkxhZMuZg7xSinc5uBAGCl_haG4gQC-wD1-XqQ8q_tFnTZmU2wYAqPUkwHav7fvSppllI2Jb5QfPJEe_dNGBY9FNgn5n2-90pet23z0uV5l2_7K5S2k5n4cmil41LJECJ4PTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwOGbXH_Es-oiLy0KjpGoz2d9Iz51KZpYh69h_af2MfYJq0arF9ViFFQhBdm9Bz0r88l31t9IJEi7fr55vFDqvYLgw__tOg2d6ILMIiK-qnuPei04OgDLEExwgMGAyPecQ7sNJFbN8HLlHgj9QgZbJv-9a7OhqDAkuZc9xiQfECCiV8K-4BPF8nB5JYGKYwZuPD0nc2mJUZVhnvlCWh-kuu6ippAyQRkYHF4oa5eDI5cigwWzJRiOfSE6suSE5F5rQ6JVPNzW7CjJfG2Uq2wpTJgbbDR2Ad-YvVbPG9sOhfQMkumroEP8up3x_gUCndiulSA9pmYweQj1mcwmUfwIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN1wB6Xoc5qWFS6anYB7mBGhqrYNZoIXU9jZZ0fHAYf3eOCoB0EELh75keudqDZnPzBzGG89Pm4Tt2LlxHlM_tWDjMuriiyXKDF74cXtA8Y3nR3iegZgzNGRqjoBqnQ0tdoJPgVshV1LJhF479mXvYrft8jgAKw3baOPnccfK3MQ9_A3UWr5RkTvSl4GONyp8a2-OHQzuH1ZVQDSFsD5Fof2FJpDwpF_skQh0kLnVBnQUwBe7KCN5xX6znzNQ4F7gPzS5s8OnzvLu6WynZvB3J9upJCInwCmiwnTECQwQfp6Llsyv_l3QttKAqkM8ad2MY89YXWwMgL2MHKqtmQdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pgi5DVmNPNXBU8sdxVkKTn612_qX_u0APtGAYpprH2X8wsTYypUHeQBpa5FiH1GdsTgM_iLu9os4hFDMaBHxsnonUfQdiilU8qTvDaA1BJ6TKl6_x_dbUosT9Tnvh_6virApkXk9n_Yb-UnMfttpcmnzGFx6sD-kPS5k7CFkBNewA55pM47lf6qpWhLgAodculnvokn1ohjNqaVr9Ni8geZv4eI8KynRbyXZzugpltkAGuEb0kpRS6iLHcpSLubIRUJ6smtDE2I5isrOO-1r7VEHToFNCqx_GB9sXGfuaUwRwsz5eECfxNlg5d1LoF0Gy5lp6iGJJTZ-TLDHLDcaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD5GR7qJVXjb3C92n9iNvRbUH2m4nvy_dazbwnQCtQ1LGazUU-P25StGljjx3YO57szulsEzrObpzRf2-onFh_Q6kh8Z5_da3qEgdAo8zwU82EOAKfj00GUdGsFJIAxSmJ-n1bTxgcx8q2k40HyzWMbP2yK52LEOi8E-Rumq387c5IdzM9W6KiVOJP-fRFYRZs6hAoZHMVMImL-rww3eFnO8b8N4-OosziLdZc2VP_ipdU_qxXtPHYgDGLVR6AKn9JYh_drmsmXNQ6Hw-RhqZPOXxT5Ep-56qjNpLmyLJsCzMz9HetqCoSectBJBxBjyUtTiadWYg7RB4xxU3RmhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=ppkxsI8Uld-XGf97ySoR4lBMqTISXju7LklvCADYHlBTxPSjrfs3qSSKWMQtbTThQrVxd5Aha2ka_kih9iSMuGEmHYUlG0E7HCcCkwyDf-xgdnXfx4NiyLwCCX7GQl0W95IlRnPFFvcTdK138rhCMoK5HvWrbj1gr4NbSAkmQ9aLF-Gk1vlqJr2heDyJ5YgPs5sM9mScpy8uCabNTzJxChW1Db27D9Q8urEST2Y2x3mf9VzBVHFS9ZbPzIRwEyTwr2NMv7rfhUTeeh7agzb_aMoMEnYqKpFh31ZU3WNC6mk81L2B-XRTqEjQSBD1NV_rcNAHGQoO5_IMAA8cXWWwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=ppkxsI8Uld-XGf97ySoR4lBMqTISXju7LklvCADYHlBTxPSjrfs3qSSKWMQtbTThQrVxd5Aha2ka_kih9iSMuGEmHYUlG0E7HCcCkwyDf-xgdnXfx4NiyLwCCX7GQl0W95IlRnPFFvcTdK138rhCMoK5HvWrbj1gr4NbSAkmQ9aLF-Gk1vlqJr2heDyJ5YgPs5sM9mScpy8uCabNTzJxChW1Db27D9Q8urEST2Y2x3mf9VzBVHFS9ZbPzIRwEyTwr2NMv7rfhUTeeh7agzb_aMoMEnYqKpFh31ZU3WNC6mk81L2B-XRTqEjQSBD1NV_rcNAHGQoO5_IMAA8cXWWwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0iZTQcmpDh5ax3ZlNbJe89Hj5PBe825zJAzIOxXOOvbkeoaBmkA4LmrM0s_8_ciF_0dB9yM2_PgDwQnt_UGgppSjpsCE_koStwXrZQoPLAYfz3yx4vZsW8a5btsW1hG3VAhFgoUozDAe54_IrKSHyZUxzozxysX_iaPn3Kc5A4P39u1Zbc6wpkEkDz17yA2TcXJOs7DYP-H8rUyS9ETAM21MLvuIrU4DWRcYpcP1WnYXNtSjWG11tiJtT3oA_6cVhJcq5ZPOqt7oYp8rA8NgUAtt6Fkul9Yyx05NKP3bqn5K_8XNFE55DtUak7pXuRPUR98rDt2V5p9QPHXiAbhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8lrIb-nLJstncoPmFA87p1m5tA9chMRWLXAZSatgrfusU7gx4dqhKdMkVGGAYnfaUCaBX9ZnMZCvKGPEMMbA9yMGUi2KZqwtvc9whxCLqeOIpg3vnhzXTK0ruL1hqlwO_AaEiwiXCSN9iumv3DI5m_9pjc606mXFtGMApn1_mlYQgNS0_-zggvg3nUrSFPZqLuW6wjV-E0AT0j6z9wI2YJ4V5OPPHBfu92ABWs8aJd3xm-Qdcezw034-DfUO7kaeoimHrh7MVtWC3gBqaO2kiZw92TMukwMfLwhePYOUL1thndQ2oebS5qtz6-YdewrR1ht0fqzTa4iJYdHq_fuvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Up32o7gJasrwfGFW5DVAedXrtwyf8p10eNG5_CGRNGGFBJl3GlGGPMAc-oTIBdAsIA-NfnvLMyu6_CfJCBqE2uX-wjev8UGuNXvHJpiJ4WYBfPU3toMWZqqN34GGXRmVAkfrtyvooNb8rsS-rD30WTD2TnDv6FcaskZfRrEOoqt-wEUF7omRMZfpJuLDDtAmlYHYP5JQXUUJv6qm3iCvVoYtn7wloRDGjm7CZH96TGrpJLXPXETJKXCmJ7W5mwyk56ii6R2zRpNHoJUY7WgSxZimjWBfbxof0XT9LOcZTtbUs-3t7PTO8tq1n6ksy2AEWJCKv6EzG8qWp74gcc_dfoeqGYj2KwANsUt5c-mhdrel3jej53xpucIY6Bow6qyYHTj6c6lDudkgihrSaqEH3sYeY0rffhwrx9zXgx23Gj6Csk_ncOgs3liFS-tn6pAFRHfrFeiu543AkZnnmBZJpmcGmlxAkwqm4rkUMaxL8lnVI4zZoDIBnPNGXUmyBXZhEX2lCJov73Jrf7qIWzIHiCSP1ll5MzJjjwTyW2wUahOoTaIuBVU7kqHcD-fI3ArjO30LT5BMWbzkg_9-O05Ma7tKZPtjeKTnm9Ys0Sa1chObJV0B29PkItKKV_K0KNsxMfxaDYbl9IxDP8ElXXRmhGTnYkK1yiMLIcC_8oSBLjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Up32o7gJasrwfGFW5DVAedXrtwyf8p10eNG5_CGRNGGFBJl3GlGGPMAc-oTIBdAsIA-NfnvLMyu6_CfJCBqE2uX-wjev8UGuNXvHJpiJ4WYBfPU3toMWZqqN34GGXRmVAkfrtyvooNb8rsS-rD30WTD2TnDv6FcaskZfRrEOoqt-wEUF7omRMZfpJuLDDtAmlYHYP5JQXUUJv6qm3iCvVoYtn7wloRDGjm7CZH96TGrpJLXPXETJKXCmJ7W5mwyk56ii6R2zRpNHoJUY7WgSxZimjWBfbxof0XT9LOcZTtbUs-3t7PTO8tq1n6ksy2AEWJCKv6EzG8qWp74gcc_dfoeqGYj2KwANsUt5c-mhdrel3jej53xpucIY6Bow6qyYHTj6c6lDudkgihrSaqEH3sYeY0rffhwrx9zXgx23Gj6Csk_ncOgs3liFS-tn6pAFRHfrFeiu543AkZnnmBZJpmcGmlxAkwqm4rkUMaxL8lnVI4zZoDIBnPNGXUmyBXZhEX2lCJov73Jrf7qIWzIHiCSP1ll5MzJjjwTyW2wUahOoTaIuBVU7kqHcD-fI3ArjO30LT5BMWbzkg_9-O05Ma7tKZPtjeKTnm9Ys0Sa1chObJV0B29PkItKKV_K0KNsxMfxaDYbl9IxDP8ElXXRmhGTnYkK1yiMLIcC_8oSBLjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=FcfnO8AMtT_pwJ8rofo4uxODxildP8PSxvJoJCEeykM3X6k-SubrW9LifPi4Dhgqgs4OkVmrGigjDag-5DjLFaBiazO7qzBATrGeBNF10ZGCS_UfhOBAtYFPZSGtqGSK6gsubrVNir_uW8sIFnacye7q3mQufx-Y-wNsATJlFRGcK065F2jS9j80-3InQpxpwDTMnflpzJkQJNnz2jzVXmcqZY3dhTDm39XnnVtoz2Ns4cvTJ_n5DuR_qyu-QPb9Jc2jw3jCzAPlEZwkXj-y9YX3bzA2t0G3gJkGYTq-mMPk-KeQknnBgnwwOslKyVzf2TGInuT-0TGrgZDxpEhcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=FcfnO8AMtT_pwJ8rofo4uxODxildP8PSxvJoJCEeykM3X6k-SubrW9LifPi4Dhgqgs4OkVmrGigjDag-5DjLFaBiazO7qzBATrGeBNF10ZGCS_UfhOBAtYFPZSGtqGSK6gsubrVNir_uW8sIFnacye7q3mQufx-Y-wNsATJlFRGcK065F2jS9j80-3InQpxpwDTMnflpzJkQJNnz2jzVXmcqZY3dhTDm39XnnVtoz2Ns4cvTJ_n5DuR_qyu-QPb9Jc2jw3jCzAPlEZwkXj-y9YX3bzA2t0G3gJkGYTq-mMPk-KeQknnBgnwwOslKyVzf2TGInuT-0TGrgZDxpEhcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCiCJx3B5X07RVRf7jo2Aq2xWQZBoh02bkzA7fHJ3U47IffHoLlEZ9OoY9pyt9OWN34STwHzmFaOM1xdwUrG5Bclv1W-n4jf1wd4hsRwA3UA_A8LZ53zsiuWFEywyYndkuGAvrkjBPZ9jiblybZeP43bGtPPU7Nlmyzfxn9dvj-vRCDp2k2ZO04u6UDw88XjDWIaW5jZIMtKayvsXd7wlW0CHT8169SPjnj6KfKFygTglQXzikldNgqW4x3NhU0X-4RiG_Zt7LjOoxyD0iyqBI4yREGPszlARao_t53Ba1lyPilbw50OZez_Di-ErYP3CsnMKIHWPFiQH89sw5jpIk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCiCJx3B5X07RVRf7jo2Aq2xWQZBoh02bkzA7fHJ3U47IffHoLlEZ9OoY9pyt9OWN34STwHzmFaOM1xdwUrG5Bclv1W-n4jf1wd4hsRwA3UA_A8LZ53zsiuWFEywyYndkuGAvrkjBPZ9jiblybZeP43bGtPPU7Nlmyzfxn9dvj-vRCDp2k2ZO04u6UDw88XjDWIaW5jZIMtKayvsXd7wlW0CHT8169SPjnj6KfKFygTglQXzikldNgqW4x3NhU0X-4RiG_Zt7LjOoxyD0iyqBI4yREGPszlARao_t53Ba1lyPilbw50OZez_Di-ErYP3CsnMKIHWPFiQH89sw5jpIk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbRb7vnu0PNZFyBfob2MXqKXjBYngxZcwK1Nucd5xG_6r16inAN8gPaRkttDqsoiEaLMiKlKJg-6QRSkO_UAG6yVt2VldCr_XdCUXxszqtBTW7kOYAMG2x2hL1n1IDdBSesbZaypHzayC7Ah3eKKtw1yEjeH3eFXc9PA9Cl2KSuFqWpuy2s8SeH1FgDCKLHtWkhlUXB2weit9U-IOQMfK0sgM7ReKGiVSEJknyoXNqfH8SooILGBvqc4ODuZhXDd2QAmBeSUX7UCzA8RmFBGhc7PebV9TOLEGvH4vzLoMHq1nPZrc4GTG7VNtqBYFtDWqYO1zZCOdSv1jm8jozi7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clF2w2BEvbu1i_1RDOaTlf3jHPU5ZojN1dMgSqICt_xgdo8DbTEzRfS5y774JFDKMN8ZbbMRQ2AH1tS2UgQ3kEImBESgNMtBoEtNPzPheNrN11K4sqhh5WNANnb__pabNfC2Ouu74J8zNbu39w0gt6VCHTJv0fULRy9XHft3umkAmgefSFdeK7LE02_IP7hx8gH4Ye1UHeJjEAk_bLjkKzulCg5t3XtIbnISC5jqlFyoE1Q-MaVtwUSMcbUKvn7olFjWdr99K7Wgz3J9fMD8OtwVW02FMvATwgYl-xNWY3GQteBZkHZ28ARBJ-nOq891EXcFH8NZU-SXzXkz74EaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUwq_OJo7ihcPj59tnrt1C5bU_-XxTuMNpuC1AdvqvtezHO_785NRwuzR13pAV5-SSvIMnBSWq-rvCyFjjQ-xN1MuGaJRq3aYaZWRBX2ZaJWi1pwac0rH8pxMrDGWK0gMC8FZAk-LFNe1mCODDIZEEf8eMvQ-WCz07xYf5Re7vcV5WKfRB-Y1H4wbG9YbIsJWxERHqZXmtJlzU_hO6f6nIEpWahnxBitox77dTEoJ3z2xTKTfFPyP-ceAvHwb5rrZI0zDoePiEUvC7LSrbf_5QMoYz0KA-G1_V4kGUMQJ19sqAN9osDBu3B_1UQ2FjD1nYBMGQPP2rUUiKKy9ZNDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=HHUITH4gyO14n0hQGy1Sy0GNbZHpkN2E02dnTL6Aff-_UOX96ULjuzs1B7bh0Dxz9J-z3cc95OJs436VHd_z5hu9WGcsYdz25buuHjl5WHnjVbfnk9u7DybMxVU7nVFe7Lb5xwZgf_k3qC636PHFF2qdAtqeudU5iXzLVn3GZxhXlT2OGlWom_Zad4HjA-HFRqAosXYGKfhjdC45nUBTLPcFeRzhVJ8oorlFjgx3eqlNQMqOFf8t407BsCWiAcGlhMu0JFhz2wufIAvakyS20_F9jxws0XR6bGBhq--vMmLaBvOXAsWyr6fCXaQQ11v62ynLspeS21ychjwrMlddKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=HHUITH4gyO14n0hQGy1Sy0GNbZHpkN2E02dnTL6Aff-_UOX96ULjuzs1B7bh0Dxz9J-z3cc95OJs436VHd_z5hu9WGcsYdz25buuHjl5WHnjVbfnk9u7DybMxVU7nVFe7Lb5xwZgf_k3qC636PHFF2qdAtqeudU5iXzLVn3GZxhXlT2OGlWom_Zad4HjA-HFRqAosXYGKfhjdC45nUBTLPcFeRzhVJ8oorlFjgx3eqlNQMqOFf8t407BsCWiAcGlhMu0JFhz2wufIAvakyS20_F9jxws0XR6bGBhq--vMmLaBvOXAsWyr6fCXaQQ11v62ynLspeS21ychjwrMlddKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB-xqnxBLDaCWkfuPTb71GZvrOuC6SYdZrwQbi5LPDSDPH9hZfzy6nGW5PKGoa9xGqmWyF9IvfE8ns_OEA4WMC60XB4MQvjyiAGWb4jUtdLdMybOWIgUpW0B3IAJ1vpdqea9D4y55uREWTy2G2Y8XQQSAI7NMFfG7tprWbnxbCN2GeEgmvoXzsbB-avGirOUJ357Es-58CLMjswTIswciAIEyD04pSrHexkeEIBbZvQCMSbPCghOukpWPoc6KJDtw7i8Xfr9LSY2g-gIYnxlj7w9f7b_SD2XWL_2jrtlqLyKz9i2SFj1vYbE5r7mYgKqMHcorgb8LO2teJz6GzwOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ul_QcvveACPfxpjfNagxeUZloF3dD-hM5pb-8EhSdM57deigpxmU0EoxUkuO14QPzX5OUzzBJ2g17NE7GnIs2LU_8UocopikJdJUaRWSjvMZDDlzty5DDkZM4y9yJtrVLiwY_yACZM5QZIpXxTD2Xd7_XHG7bTZPBa4v5MNV1obJW6qO_bEfqrMn2zxvraQUvoT6dlY5F8Z33uD6YDaab-BNyxcUhPZq-IokyDfE2lZ6JiR2TQAgwimxwoSXoJ1VeC5gyl8wrjN54Qi61_q38lJi8FfyngV-aNXPlYWzpv0_R3iLvo7lUM2gC29LQz2o7Uxt_OpU3UmFT-uRXPsTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YllGPEUA4oO1jAoPT1gzuUbmSWf9MsoTdaeaB9Go-bDSJQxY_zjmRviIPlHfrXkMxscGoy5akH7424FNRF5nja-du9KmEC4BWo3TCiNEzorOfYD2FP1T38haEAHSF2QmQAoT0-tbOu4dFucHAEhEFChJJ6cM-qvVN2goEh--TCYDCjOxT-rHibHctlyU2iw7mA0kW6gqjDD3SrgN-dAakw86leOqUAmUAUmuNDHF2AIKa9aqpaRbg-nsuhsxUHSj9ohXXn2zMBdqPSzXdsbjI-QdObVeeKOCo4F3_gRGRyDXG5aAXd_koO6dfevOzJxfb23RC0Ouh9lnxmw8W1K2vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmZDh83U9mAy9lABg5Rfbe9cPwIebMmZBdyqUdj6cMl5gWdDFUME-thz_PhX4nLdhE5epSOMM8TiC2zcr89oIUsQJ85lybAZyRIGM1_DhYA7hGJap0-ZdrzPbhRQNeI_8Tw5r8BhjRrqVkIFhmWCK8iHvvuAXl6l1TZwMGEgSIxfMLIWrpoIfjUhVT2XucJC0SBhgR0JdW4mXyZ0K6KxcaxZyqX9GzLvw_zNt03LbNYMgKkFQF8QqRKHFMx9EMmppqomiF3V44FoC8URjBUlBbIQ-frRnqRWGcityeeYB12xRRZ07CdVC9Rs6KkPt_XVASdp0QfPWx6lxJuQ19pKKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=e4Exj6BLtkriE2BhEGeDQU-DsKnpROqulSnpbAwqz-sPjKiDpiHteUDx02dJ2aY50yICmqxwqRh7PrSAm_G6Q6XyKlpHexhBCZfrbXLKBtke8XNqr1Q8WalLnH57zK3X99v9XlfykvWYVzsrUeei3qdBxZbEkNcM7CEaZApv8jNy57Kx1qnA4qJhcfeN9675H9q5zrRNmge6czbWLmhZFJJ5zwxfDwYWnrpiXxn9CQbB6nvW9yjnpF9JbGEddxgGGghmVvUfCSG4Wib3g6SIVLUK5-zWggNTPpNCtjNJevqA7gOK3t3aPQjCD6bbPxU9vA4iLvZVwXdxJAkvvT4lFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=e4Exj6BLtkriE2BhEGeDQU-DsKnpROqulSnpbAwqz-sPjKiDpiHteUDx02dJ2aY50yICmqxwqRh7PrSAm_G6Q6XyKlpHexhBCZfrbXLKBtke8XNqr1Q8WalLnH57zK3X99v9XlfykvWYVzsrUeei3qdBxZbEkNcM7CEaZApv8jNy57Kx1qnA4qJhcfeN9675H9q5zrRNmge6czbWLmhZFJJ5zwxfDwYWnrpiXxn9CQbB6nvW9yjnpF9JbGEddxgGGghmVvUfCSG4Wib3g6SIVLUK5-zWggNTPpNCtjNJevqA7gOK3t3aPQjCD6bbPxU9vA4iLvZVwXdxJAkvvT4lFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=NGUXJQql6byvmqkUE4O3o2Q3qaqICSfQk7Ooq1YApOnGSbznyLKMYJBMcc_6zpU8UQSKVsvMDbfLM8MCle2UsCpF2u4av_ZMZQuAx9bKgKJVuqL_KAiJwSQjB2xS2V33yKrHHafKpgQWm6tiE16v7DfQCxUVIkJvQ5FpqrRtEgZXpj9IHXbTauIPBudiurA2EJ2kNjLT1nP028ZHcTHF3R4Cp-QrNmHs83JgFL0yLv6O2gS17iLqUzyB5g6etjEgteDbL4FNOrAZZPcdVmDA4OMB6hRJFsSX1BelaxTiSW46f8WVpLp2KOk1aGSW8baFKqcDN1dYGAsNCAWqP4bs9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=NGUXJQql6byvmqkUE4O3o2Q3qaqICSfQk7Ooq1YApOnGSbznyLKMYJBMcc_6zpU8UQSKVsvMDbfLM8MCle2UsCpF2u4av_ZMZQuAx9bKgKJVuqL_KAiJwSQjB2xS2V33yKrHHafKpgQWm6tiE16v7DfQCxUVIkJvQ5FpqrRtEgZXpj9IHXbTauIPBudiurA2EJ2kNjLT1nP028ZHcTHF3R4Cp-QrNmHs83JgFL0yLv6O2gS17iLqUzyB5g6etjEgteDbL4FNOrAZZPcdVmDA4OMB6hRJFsSX1BelaxTiSW46f8WVpLp2KOk1aGSW8baFKqcDN1dYGAsNCAWqP4bs9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=KQ_xA1TNzV-jiv3TVLF0_G4HVoP4XymN-1Qf5JZx6MlrnULQxfds7M1PajSWYKy9Vn73sukEOVGvpBhgTj3UlBTzO2tJRdAzktaF4RpJ-xwEm_4O-e5QyQksH1TX9-O6Smi1SHeSOF2y8eDzQ6gDjfH44PD3mhMrqgavyLvQvzDcgg-Jpjl4W4G0pH_w1zRbniAUbCvnVpJAGhnKP-IrYYhQB5E5ZIInifm8K2NgqQL2n6MAvz8wq4K6OWHE2CHtpCfmGalw7KtWZncRqhmB24rV5LXw2Q7aSvQUoyd5xfkkOGzeg3rI8iKKpOZmm6CunPkXg6GEykLfwRHAPS9_Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=KQ_xA1TNzV-jiv3TVLF0_G4HVoP4XymN-1Qf5JZx6MlrnULQxfds7M1PajSWYKy9Vn73sukEOVGvpBhgTj3UlBTzO2tJRdAzktaF4RpJ-xwEm_4O-e5QyQksH1TX9-O6Smi1SHeSOF2y8eDzQ6gDjfH44PD3mhMrqgavyLvQvzDcgg-Jpjl4W4G0pH_w1zRbniAUbCvnVpJAGhnKP-IrYYhQB5E5ZIInifm8K2NgqQL2n6MAvz8wq4K6OWHE2CHtpCfmGalw7KtWZncRqhmB24rV5LXw2Q7aSvQUoyd5xfkkOGzeg3rI8iKKpOZmm6CunPkXg6GEykLfwRHAPS9_Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
