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
<img src="https://cdn4.telesco.pe/file/qCCw2ivLNQjEr2x69QSA-70FuMpS3IWDsO2q-oZjq67nf154DKoyK7cjPbI8AmVeQWjuyNqhnDok5rdA6bCrqwnyP-nO4OLxwbDXh9NxkhVTuVq06u_PFi0SN8u03NF2K5QnDYRaBQiwNZzKqJFObwK7K9hzN4F2d2c-VIrmNPsbEgzqlBsEMNCFzVvWFN7_PRj1wWg6gMImj0L0ZZvZdMOwQbpCnowFDrUxaYAF63NPXPtANj_pX_JgailNTX5tXzNH4msWv8v9APW3fv_IDK8h1oUCzg3UM89UZLWSxL1qjg4MyGRqFart62Qw_rUit15ssfcsGCxAmtJMR7BhZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 129K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 19:52:48</div>
<hr>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0at-EzimZbGx0ZkMra_Dk_TMcPXn3qqwbUjGtWsCPla95xe1iFbd40o-S_bMVir4JPUAnlg2ZpyDw3Ifoz9cMP3bNBbQLqfE1TfGMuHSsQX7_lbNwX9WMy8idjMCgtYVQqcqy7FHHJkffjhkUT9mR8gJw908IXCGxdiHH-kx8sWIQJ8uo_vpLvuNM6uhBldqLko5PcoEXVZcg640WkKe0MpnALyfVUYHckD0e4f53hIPlHvBtmNbjEK9Gg1whlu8efThAAz-RddywNyuXde1k904JOGAgCIUlBnEN_33b2GZ8Zz9t1oCzisJ-TF1SLPMCvvoU-u6CKbjh3ZUsMUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=kq_zQDeBPJCZwbMGh53xLCZKTbUAuw8Iu-mdqqh-DICOEpNiHyllohxdjqCmo0Te5akG3-zNv3SMndQwgU1KmNM_E5DZmHDHKljvjelNLRPHvqCUh4YDhR6B4_0C3fJxrI7R36haKJ9XMYpTfR8LrdLBizhwLLkSsAzv9kcZgsY_vNPg07xb6l1Dx6E8dHYk2Jbo6_OxSDAe-oVnq6s2IMUZ1cmYSVF7DQD_c1n1g0FzDdwJkb4Sk_ePMYEySGxY1SDkf10jVahL4OVk57uEv31nM8d8WLsSD2N-QV7EwAOgEQ6WV1tvw4XSSAqriM4BfcW7jpFNk6eJzACFb9SzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=kq_zQDeBPJCZwbMGh53xLCZKTbUAuw8Iu-mdqqh-DICOEpNiHyllohxdjqCmo0Te5akG3-zNv3SMndQwgU1KmNM_E5DZmHDHKljvjelNLRPHvqCUh4YDhR6B4_0C3fJxrI7R36haKJ9XMYpTfR8LrdLBizhwLLkSsAzv9kcZgsY_vNPg07xb6l1Dx6E8dHYk2Jbo6_OxSDAe-oVnq6s2IMUZ1cmYSVF7DQD_c1n1g0FzDdwJkb4Sk_ePMYEySGxY1SDkf10jVahL4OVk57uEv31nM8d8WLsSD2N-QV7EwAOgEQ6WV1tvw4XSSAqriM4BfcW7jpFNk6eJzACFb9SzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma1jFYgjMZ1v0HZhCD6qEZuezlQQ6i5IODLTZ4mV9hiJMfEsB_APTkXC4smrS65DXFAQrmfFl4Qae6HqITi6vFn1UPlsU2yZn5Z8DPg3McaJMNbKw159ZSqYeU95ijmny-keViwMTCcs5P-vuZTJ2XwvBEnpjzcG87rrNXVDx9yhJIbOen0pmd9WZk9x7RcjPLJf_NMpvx_yp2l8hsN-XN-D9EzDzoOupIPnoRT8UiSgcz-ggErKea8G-E0b3pY7EgFzoKsuUGEW4jOCVIqtp4qKPQW8uWJqhnQOYFDQNV3ASs94LA32Xgzo1wDL1NCrnQdtZLBW6pWSAqSYZpLy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=F_9-gcadp_eQt6pOLIl1twy5kQPGlokLvXlr5N_OIRum7ktMW7MvQUsVCJ8tk5u9VvTVtDB_-IJUu7yVXfIop-ZSUnisxW1iLV4nsyTcY8JNpSwxC3FWhnLltZ_G5AdGZY6qr_9HLWsYeu9bA9Y4XnK790a7jpHWoGRaQziLtMlWErmBKZMrzMljIlmTpAgRyoe0a2KE2RCpXD_ueFOKG5louD7vtuY57jdC-lTosxSESdoUxmGtyBz519Mr5I1Vj2Ll0rrc_uO73JnCnEec3zPwIiv-BtWcTvNpDJJXhVzoRjjR1S6NixOrgdry0jquifx_zKQYmgTYe-1hHU30gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=F_9-gcadp_eQt6pOLIl1twy5kQPGlokLvXlr5N_OIRum7ktMW7MvQUsVCJ8tk5u9VvTVtDB_-IJUu7yVXfIop-ZSUnisxW1iLV4nsyTcY8JNpSwxC3FWhnLltZ_G5AdGZY6qr_9HLWsYeu9bA9Y4XnK790a7jpHWoGRaQziLtMlWErmBKZMrzMljIlmTpAgRyoe0a2KE2RCpXD_ueFOKG5louD7vtuY57jdC-lTosxSESdoUxmGtyBz519Mr5I1Vj2Ll0rrc_uO73JnCnEec3zPwIiv-BtWcTvNpDJJXhVzoRjjR1S6NixOrgdry0jquifx_zKQYmgTYe-1hHU30gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=FAHAj_pAzQuphV85Y2JI4nH6GISaPC0ndzcZbWMJyKVDPCmmD2UOpfpjqG45AOvIRD7GYMlaVCSxYAHcMVYmCXvkEAwL50Gb7uMrJORbiBdC0RjKxjLLc52KLzKaml5JIPv40YS9-rfMB-WZbSwElpfOqknucYDBOeEfxxwBHNr5PuncJYaq3rpNRcL1eZ7nV9m8IjY9HLiWJ1Kof70k3-IOir4ZYJQUBYPchBfwLYr9ERbE-SHDZp2WL4QmUik8jynsbkAf3iSl2LE0xzgnTtfHmD47uSrusB3pJkoTuryyirQqi-pQl9nx7YphJYzUEktMqr4nk8V9Frpiiwfr1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=FAHAj_pAzQuphV85Y2JI4nH6GISaPC0ndzcZbWMJyKVDPCmmD2UOpfpjqG45AOvIRD7GYMlaVCSxYAHcMVYmCXvkEAwL50Gb7uMrJORbiBdC0RjKxjLLc52KLzKaml5JIPv40YS9-rfMB-WZbSwElpfOqknucYDBOeEfxxwBHNr5PuncJYaq3rpNRcL1eZ7nV9m8IjY9HLiWJ1Kof70k3-IOir4ZYJQUBYPchBfwLYr9ERbE-SHDZp2WL4QmUik8jynsbkAf3iSl2LE0xzgnTtfHmD47uSrusB3pJkoTuryyirQqi-pQl9nx7YphJYzUEktMqr4nk8V9Frpiiwfr1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=EOQziuA5jLhDe3I5A0FlQkMPPtNKOw74xOI4xHOwewnIgdDdnUScOmPsSK3Zwp76pImSjCU1CKOAeVK6LefHcR-XqYec-5LA7Hv0jwrSgw_nMq2c1Ak7FzQkFKQcQY8y49W-8aySsejUVEa5qOx18_IeIhtpv4u6wZA82a8XI-qAwdg5-snnNbweqUzPyvLwMym23G29HiD3zgE5svZ2Hmf6d2DqfXyOUzTzdOr-0vhV4sZ1PU9dNbbzptvHX46U78fWbz6Mk5s8f_Oi10M0yCAoCFwPqmFvqgQqOmybazBupeA6NzWgltaa6k_s1QsfX3CFmgYxEet3HaP4c_Bg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=EOQziuA5jLhDe3I5A0FlQkMPPtNKOw74xOI4xHOwewnIgdDdnUScOmPsSK3Zwp76pImSjCU1CKOAeVK6LefHcR-XqYec-5LA7Hv0jwrSgw_nMq2c1Ak7FzQkFKQcQY8y49W-8aySsejUVEa5qOx18_IeIhtpv4u6wZA82a8XI-qAwdg5-snnNbweqUzPyvLwMym23G29HiD3zgE5svZ2Hmf6d2DqfXyOUzTzdOr-0vhV4sZ1PU9dNbbzptvHX46U78fWbz6Mk5s8f_Oi10M0yCAoCFwPqmFvqgQqOmybazBupeA6NzWgltaa6k_s1QsfX3CFmgYxEet3HaP4c_Bg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=s57URb1aBqwXwPUYm2rZTApk_64Th7bmjOpmRGKiidsJPSssrwJ305IuPp8c0hF6Uk521nZ3QbKb2sWYVyfkslz8QF7PZSeRjsn-ZO_OboPETAcQ9zaevIbW_I5M0Ayk73daTZsnkuni6JPH9KzeAaOq6d8KRMclW1voDFhms0vQMwkixXiktM3q7dwhrNRhPwQAuM2FrK3XiVZJCUhfAnPavWty8viYXfDwZ9f9ui2cjIryXNYvsVmzMfcW61f999QXXdH0mtTkSRvVxog1w80hWrIIkvUfzkAuYwrLAPOTRCZF43JFC8p0J5HIHNDZOLAcJ981crWtkoUTEA_5oqY6CcM3ahCuhbQTB_jOLwLqiFCnRY7cLZLItlBjCfE6C1YH4sDuJPOEw62LXhj82Mtw45LrOalR1LbYqmCwLDs4C5adBh_iS3nv_4B-KQ4A7J50ABar8iIR44dUQFKjiS94sYHiSgmo6vK_vujR8-5I48fPpY5d2D9N4KufO3V0Lg6HpHArvGAoiixbw6wRsrizLOHqY5xX9AyvxpgUlNOqP3tI0Jq_-yJMRlVNxshYkXFvN2GCEo69LGI5NARJoUxYoUGfri6JkpJhNhoBZeoM_ZN_2gecCgPHTfzjO5jvCsPy8p4N5EePRj_rLhwK3uvpRtKcbchtrOkEFjyYJnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=s57URb1aBqwXwPUYm2rZTApk_64Th7bmjOpmRGKiidsJPSssrwJ305IuPp8c0hF6Uk521nZ3QbKb2sWYVyfkslz8QF7PZSeRjsn-ZO_OboPETAcQ9zaevIbW_I5M0Ayk73daTZsnkuni6JPH9KzeAaOq6d8KRMclW1voDFhms0vQMwkixXiktM3q7dwhrNRhPwQAuM2FrK3XiVZJCUhfAnPavWty8viYXfDwZ9f9ui2cjIryXNYvsVmzMfcW61f999QXXdH0mtTkSRvVxog1w80hWrIIkvUfzkAuYwrLAPOTRCZF43JFC8p0J5HIHNDZOLAcJ981crWtkoUTEA_5oqY6CcM3ahCuhbQTB_jOLwLqiFCnRY7cLZLItlBjCfE6C1YH4sDuJPOEw62LXhj82Mtw45LrOalR1LbYqmCwLDs4C5adBh_iS3nv_4B-KQ4A7J50ABar8iIR44dUQFKjiS94sYHiSgmo6vK_vujR8-5I48fPpY5d2D9N4KufO3V0Lg6HpHArvGAoiixbw6wRsrizLOHqY5xX9AyvxpgUlNOqP3tI0Jq_-yJMRlVNxshYkXFvN2GCEo69LGI5NARJoUxYoUGfri6JkpJhNhoBZeoM_ZN_2gecCgPHTfzjO5jvCsPy8p4N5EePRj_rLhwK3uvpRtKcbchtrOkEFjyYJnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=lFbxv2Md6v3yaFgVJyHFvtNfM7JzIf8-0mtSPruxFmqC-hOw541rvuvtLqK9t6LulchR96PUcOEdntzdD-Cjb20f4K2Q74_2Gm-5ItTlvseQxrTLfNAo7xVGxNAkfBalVBJpFJ3eYSnOE8ZqHI0IXMxHNYrBtVZo2786mz9Ic2zZqpoMZy4kEPHBhjTvkQaUK7O9ZgyWPSaB6o_dfybG1anhUGPW5adLWdQFnbpTzuSxns3T89rWbjPmKdmSdM81KjCRf5RXzlcNfD2SSoYPYyXbrYnLS8qwS3FFi1-EDee55pprzPSlV-2RSW6eOjSi4RAaieqkg_qVkMAPE72esTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=lFbxv2Md6v3yaFgVJyHFvtNfM7JzIf8-0mtSPruxFmqC-hOw541rvuvtLqK9t6LulchR96PUcOEdntzdD-Cjb20f4K2Q74_2Gm-5ItTlvseQxrTLfNAo7xVGxNAkfBalVBJpFJ3eYSnOE8ZqHI0IXMxHNYrBtVZo2786mz9Ic2zZqpoMZy4kEPHBhjTvkQaUK7O9ZgyWPSaB6o_dfybG1anhUGPW5adLWdQFnbpTzuSxns3T89rWbjPmKdmSdM81KjCRf5RXzlcNfD2SSoYPYyXbrYnLS8qwS3FFi1-EDee55pprzPSlV-2RSW6eOjSi4RAaieqkg_qVkMAPE72esTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sp5vCKw8H7zaRQcdWpma8dZ7yX9RCtwqRdMPswOfClLm9-dQcANTg8qc6YAkxP_f0NB8lLyXcbyahCtjxgDKYRLfDo_lI4LglvQ1SrwSJW-fMt9UTUsvF5Vc0TZOTxk1_fI_3yZnQE3ZZU9BLJEEvvtf5LxJ6a1fq5AAiGL7IFe1DYW6dXuqUIu4IflHeZVhywcaFbqf6_lY8vTcR1VAfZtrpt_q1yAdvgDQ-NTMVed-3D7XAvwEJezRC05-tJNQmVaMLSHyFs8BS4i6QcvaqQttL4nlsSd6VutRH-jBKrFouwZekXV8H96vevQqE06VxpDOi4Qrn5Mf2_74WRjKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkp4VEIBKoteS2SnEHcbYBSSejS3XPo2YWFEgHopIuHC0epyDgxmfAlFU4bqIKWMudW7SI3De3i9dUfhRzrV_qqf1CO5X4nz7h13PvOH0Cu5ih4kK3WCwkSpF8LBgKwCxRg4QshHwyxGMszfB0VR7CjLRD4sP3OXCNPFbLM9hJvF6qSY_FPh0DamO9HuHZTasp4LZxq4Nl2qZbdk-Hkq_d1V5k0wGnNG-5JmYWV49rMLcgGvOzC5YqLNrm-PPd4p-8Fw6RRAAWLmV-Aed1qKisvaLSmK1H0wSLU52Kcqk96cxbe_wu2Mq8uC28UhT4fg9NGHtUrpvZr-y4CXo-yN_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=lPmjfzlEJk1wnpcVB_VyABIPm_4d2ZYWVoTNvbY3BbibzuuRo_1xCHzX2KYhbTQPxDNjeLQocI7QlKISQh1W5Sh5OQUnWC9Y_urGPFvggpAtYdOf07VHk0rI9oNklLj3c-avDLKxgzJyR6THKx6gu4fiLqOqFn4sxszcl-Eig7TtyhROoFvubtzjQJCM-avdDzBfhJ48o-G8mB4Ijiw5666A6T0OVAttjlvrYJh7lOb_qOydZR244rKPEj012j-ZFPpQCFI3FT9hpVm0i0GjKegjj1lbzZcAEFfhE4U3SZZ8OdwK8LgP5gb-Ombi_tMSkaF6WKmEiW0bgUJD_n9MHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=lPmjfzlEJk1wnpcVB_VyABIPm_4d2ZYWVoTNvbY3BbibzuuRo_1xCHzX2KYhbTQPxDNjeLQocI7QlKISQh1W5Sh5OQUnWC9Y_urGPFvggpAtYdOf07VHk0rI9oNklLj3c-avDLKxgzJyR6THKx6gu4fiLqOqFn4sxszcl-Eig7TtyhROoFvubtzjQJCM-avdDzBfhJ48o-G8mB4Ijiw5666A6T0OVAttjlvrYJh7lOb_qOydZR244rKPEj012j-ZFPpQCFI3FT9hpVm0i0GjKegjj1lbzZcAEFfhE4U3SZZ8OdwK8LgP5gb-Ombi_tMSkaF6WKmEiW0bgUJD_n9MHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=noiWKi9YoYtr7rq_edEOUwYBdxqSAIRm-2Z3irqTZl-x5_QFfmysv5ShBCpjH0RqctKclqYBw-HP0vWEZTtzpSVxk4zNJMgcwKWe5b5gc-ybS8OVrnWKqhJV4TcoJ5MC-YYjgTXVjdRoh2Ol5H6WRgF5QH0oem0kzBD82jr4reZQhcQ-ApralO3UQ8QY7ho7rjrSvfb9cHBlorD4mtdxtDAxIcDTrbzbKup0oGIWH4mxtmpgM9WqotnHLgkHvhBTW1l6kJbyJAd4hniVe9ic9LgG1pe5IxucJO0PFBIp8pX1SocEcDJheQpHiSQoubHLnaJpi87IiKw4ffBa9c85Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=noiWKi9YoYtr7rq_edEOUwYBdxqSAIRm-2Z3irqTZl-x5_QFfmysv5ShBCpjH0RqctKclqYBw-HP0vWEZTtzpSVxk4zNJMgcwKWe5b5gc-ybS8OVrnWKqhJV4TcoJ5MC-YYjgTXVjdRoh2Ol5H6WRgF5QH0oem0kzBD82jr4reZQhcQ-ApralO3UQ8QY7ho7rjrSvfb9cHBlorD4mtdxtDAxIcDTrbzbKup0oGIWH4mxtmpgM9WqotnHLgkHvhBTW1l6kJbyJAd4hniVe9ic9LgG1pe5IxucJO0PFBIp8pX1SocEcDJheQpHiSQoubHLnaJpi87IiKw4ffBa9c85Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQJPvJddN_VYXnaRk8vB3A2CqHVKB16ZuUONUsc0J5hq3wqlWPmuQL9kk7y8qUIfdMxt_fgqAWtHz7picK4_kpUCTOqBM0cGeGIHvWb3-Jj8uku1dquNIQyGyRg8jfUdENlLJTIqXmq6NMhYmE_MAgxl8xIQjrkVXKBjAkfCZkcQ31zxSrbKOnDewHyjpszrzvxaUpenX-GUjixkhjw07I9WA3tgWquE_BqHDpEDGgRtfQKmj48uLG2SALjDNUT5sNLtbE_uQk-Xj3PdnpFawyag21zUzwJ_VihaEtEDHjWsWangPqklW4FkmmO_EK8z8h8EjApUdAlINxo9nmn5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=rPAkqv-3x05ZThgtJvl2TYoAHLsCew5xlsipPPExJIV7EWU6FKSJJ90Z7yazBHnRppbEtK6dO-GXQwUdAKryHY02-7Hx4zuBAFgbyzvlNS0Xvy8NFW5mG2M_wkq_GqHL0y4UZfI6fjGKjz5iphDr2YDGqSrLEFDeHWaTKVgjcPf82dpFz6VPZrUA2rPh_ubrFQR75N3ytFYNNakuD51CCzEQME8C0yn1tr-PxOm77NM_OZXC70lcwN5aCQGKcSxSYU3WOCZOsJBIqg_ucSvpTOvPt78Sd04evlXeircccqSU-ZJbTkjddul5XVRYbp29s8KqRPGYpq-sZZJnAfSPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=rPAkqv-3x05ZThgtJvl2TYoAHLsCew5xlsipPPExJIV7EWU6FKSJJ90Z7yazBHnRppbEtK6dO-GXQwUdAKryHY02-7Hx4zuBAFgbyzvlNS0Xvy8NFW5mG2M_wkq_GqHL0y4UZfI6fjGKjz5iphDr2YDGqSrLEFDeHWaTKVgjcPf82dpFz6VPZrUA2rPh_ubrFQR75N3ytFYNNakuD51CCzEQME8C0yn1tr-PxOm77NM_OZXC70lcwN5aCQGKcSxSYU3WOCZOsJBIqg_ucSvpTOvPt78Sd04evlXeircccqSU-ZJbTkjddul5XVRYbp29s8KqRPGYpq-sZZJnAfSPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=tbGcqSd53OT5sHIMu4M0nAqij47iE3bm_H9rmcmhRF5dDZP3-lcV9NWhCqyVz9ltuM2vbYQKddPFwKrhoezjaUrnHQqh6b0pfgBRrExxRLQBXuXhgV9HgbdW53jaCwOKk662E_FD8dzxydun0UkxqsnPfZpvp4xTVV4c15ylQxXFWtHSeT5fZPvf5wELZX15ER79k1xo2z1R9y31OgEZHo6PxYbgTGQoHQ8-_E6urkfsu9NaGt1OtB16WEHrtrdlobDOI1qbRwU30i3zYAYJWgdf6mtEG8twbI47faUHrhU3uyQ7qr1RPv5hm2uUG8d165IBY-wO7BHupSrbBxSHuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=tbGcqSd53OT5sHIMu4M0nAqij47iE3bm_H9rmcmhRF5dDZP3-lcV9NWhCqyVz9ltuM2vbYQKddPFwKrhoezjaUrnHQqh6b0pfgBRrExxRLQBXuXhgV9HgbdW53jaCwOKk662E_FD8dzxydun0UkxqsnPfZpvp4xTVV4c15ylQxXFWtHSeT5fZPvf5wELZX15ER79k1xo2z1R9y31OgEZHo6PxYbgTGQoHQ8-_E6urkfsu9NaGt1OtB16WEHrtrdlobDOI1qbRwU30i3zYAYJWgdf6mtEG8twbI47faUHrhU3uyQ7qr1RPv5hm2uUG8d165IBY-wO7BHupSrbBxSHuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=QQmIszP4ZkbNfK9mdXODMiMxYbgJZtgx98UvVYiGEX0jbidFKJIbN1ci4aADHxcmql7b6M42KPxZjqx-16O-a3aKxgtlolcwkzlyrvE-fhFO5WveAcnO4dNwPqarR4NDUenAt7-ByagJ6_Y-nMAGmjnV8oOz5J22ADHQwQWXP4wHH1gzi_dJn0ortzDNNNJ53fINPtQWnUiyqI4a6npNZ7RoiBO8mB0NoSAqwK3NpUEzU2wp2xHEvMLF11diBphXKSpSUeeZub_dNbkJV4A7ppvJcpO-j-W20SNsbK6C6Wnwb6Lq2SjGYPEwY-ytE-PWzLTex1hzP182ZCq0KANAKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=QQmIszP4ZkbNfK9mdXODMiMxYbgJZtgx98UvVYiGEX0jbidFKJIbN1ci4aADHxcmql7b6M42KPxZjqx-16O-a3aKxgtlolcwkzlyrvE-fhFO5WveAcnO4dNwPqarR4NDUenAt7-ByagJ6_Y-nMAGmjnV8oOz5J22ADHQwQWXP4wHH1gzi_dJn0ortzDNNNJ53fINPtQWnUiyqI4a6npNZ7RoiBO8mB0NoSAqwK3NpUEzU2wp2xHEvMLF11diBphXKSpSUeeZub_dNbkJV4A7ppvJcpO-j-W20SNsbK6C6Wnwb6Lq2SjGYPEwY-ytE-PWzLTex1hzP182ZCq0KANAKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=En1Z16W3ceQw1DrnI_5XYBZg52qkJgoqUWqOpwsKdVYXTRSDwvtrYQjIjBNGpAoLumBFVk5RrxazBfGEi_w9ObtIQm1gX8bOE-hhc8vFBn0znyEKqL6UXl6gk1VH8gJa7Wtb2uvzYM2iYe2McpkLsPn_3plAhwYWGVMxSvFmw8mt-XEyyafzoCXuN5-WfHf0EM-GO5u-ZQ-13iVhbRlzoAHDZJWIK9JIhXAgX93qLL0fpJt5aXIH7UaTB7wfec0tjtFeDcUVYvAm0GpCSASVQyZGj9vCQtFCKka0r0OIZliYmH38sVOm-WDEOwkbfU0nHym7ASFDnUvwpdEL8V9dWTaR5otlsSZqIqAVW3pkbJoWCvXjVvaVEY1QLIorpwURr56PJY9J0i9HKoAQpHkM4zEZP5PK9uUTiFGG9jT_voiVj42KEwmO_tX3FpPlQT0tMDUswZXMOAN-iib0ye8SBjMkYm2tvxyz53B9mDpXXwa2t-k8dZRdEVMkTGQRVVx3K_2cNVyFEbZhqPlaAsr22__EcWKpmyj61iyaiP3cDYQ41ADgZbtmZ0N__IWAZvXcOzbYAVf-NQ3hXA-SyfC4P6PKq44WxWkPPVJj-JoADfMcLeqWqA4qgIAfDhOWCN-e3HdiO4xe2SJhzP4q7fyo4Wj_ue11kKdAZSDgzSNc_HM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=En1Z16W3ceQw1DrnI_5XYBZg52qkJgoqUWqOpwsKdVYXTRSDwvtrYQjIjBNGpAoLumBFVk5RrxazBfGEi_w9ObtIQm1gX8bOE-hhc8vFBn0znyEKqL6UXl6gk1VH8gJa7Wtb2uvzYM2iYe2McpkLsPn_3plAhwYWGVMxSvFmw8mt-XEyyafzoCXuN5-WfHf0EM-GO5u-ZQ-13iVhbRlzoAHDZJWIK9JIhXAgX93qLL0fpJt5aXIH7UaTB7wfec0tjtFeDcUVYvAm0GpCSASVQyZGj9vCQtFCKka0r0OIZliYmH38sVOm-WDEOwkbfU0nHym7ASFDnUvwpdEL8V9dWTaR5otlsSZqIqAVW3pkbJoWCvXjVvaVEY1QLIorpwURr56PJY9J0i9HKoAQpHkM4zEZP5PK9uUTiFGG9jT_voiVj42KEwmO_tX3FpPlQT0tMDUswZXMOAN-iib0ye8SBjMkYm2tvxyz53B9mDpXXwa2t-k8dZRdEVMkTGQRVVx3K_2cNVyFEbZhqPlaAsr22__EcWKpmyj61iyaiP3cDYQ41ADgZbtmZ0N__IWAZvXcOzbYAVf-NQ3hXA-SyfC4P6PKq44WxWkPPVJj-JoADfMcLeqWqA4qgIAfDhOWCN-e3HdiO4xe2SJhzP4q7fyo4Wj_ue11kKdAZSDgzSNc_HM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=gMNSLpPY5lZzOYBt8Tmes5GaczRNVGQfCsEjvuiv2pWALv0_Ph4KAgmkUO50kWF0ZKGG5uHIZdNNXJB9rROrvSU8nvZVhoujOi1Q1-KcIU0dz3pGBmTDPq5ngS3jACEuLSmlXNNq_X95SXm9RScBWyZiELRZNjKkq-Fvb5BM6AhAmrEx8jfBesRsHeVsME9NzNMK7n9t_CTcLPCHQC49xPIUUD80gpyAgB_k8Awsj2wcVE1pOr4qj0xEPBYK7_1NvMiWlp4N9AfdeLNDf0hFF3gMozm3Xvbbg0t4nACwo5s1fCsOknKr4e7sGm0dEu6uTfKhZ7Cc-L1kfs9nvi2Sfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=gMNSLpPY5lZzOYBt8Tmes5GaczRNVGQfCsEjvuiv2pWALv0_Ph4KAgmkUO50kWF0ZKGG5uHIZdNNXJB9rROrvSU8nvZVhoujOi1Q1-KcIU0dz3pGBmTDPq5ngS3jACEuLSmlXNNq_X95SXm9RScBWyZiELRZNjKkq-Fvb5BM6AhAmrEx8jfBesRsHeVsME9NzNMK7n9t_CTcLPCHQC49xPIUUD80gpyAgB_k8Awsj2wcVE1pOr4qj0xEPBYK7_1NvMiWlp4N9AfdeLNDf0hFF3gMozm3Xvbbg0t4nACwo5s1fCsOknKr4e7sGm0dEu6uTfKhZ7Cc-L1kfs9nvi2Sfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=eTViVL0FvSG-oafPDDr3TZqDiarBMuH4tXJM5iHd77x_ixPNfRablcvBuXP5RJ9uEmFK4mc1WEVohaVuU61WUip03atvR5LCFt1XTEuJA6mLzVtbSzM7FZfAofdtwKUZDBupzBEif90uWmwvY7tFHkiX8VvcUty5BREj9MNwqz2vXxbWOikebFQXo-ghFtu-DIuvcb3Osqy28659NLVMXX7KB05jg8oVqBBRyXf4MylkFQFsR9abg-I41sycivQlTHxDmwkR1-YaJa9uy0C97SZS6hAd7smvOcWoRyegTK3yTo727_RasDA3Xlvm1i9aqJJzTKX7GBUKrUVDz5Ol82A-dNyZtPqc-9rHFoh02DM3H4XeosEwMyFa8SBynNySGpLFMlph3iGAAsCk98cufxHBoCWQdMuCuI8E9mUjjsVbsYydLYu1Ez3M4PTeWMZwyElYGBzmo0igytQeZCKTrFgQRRusUryWmJbjobf6MBRChLnP6d7_DBvpQaHfUS0X4DMfC-Q6l-k00V9S6TvRdv44CiWsLBCpO_lDIbJEzmdPNXy9Lgc49QjOsLPANVAM6K2xQBkBE37vZafuTGZC4JcdRacfG51dwbAGeSKwCWAq3EPoIujIcpnhGcyH1hVekMwVD9pwLr4yeBpPxCkSvgW9oYVaGkCoi-dPttqritE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=eTViVL0FvSG-oafPDDr3TZqDiarBMuH4tXJM5iHd77x_ixPNfRablcvBuXP5RJ9uEmFK4mc1WEVohaVuU61WUip03atvR5LCFt1XTEuJA6mLzVtbSzM7FZfAofdtwKUZDBupzBEif90uWmwvY7tFHkiX8VvcUty5BREj9MNwqz2vXxbWOikebFQXo-ghFtu-DIuvcb3Osqy28659NLVMXX7KB05jg8oVqBBRyXf4MylkFQFsR9abg-I41sycivQlTHxDmwkR1-YaJa9uy0C97SZS6hAd7smvOcWoRyegTK3yTo727_RasDA3Xlvm1i9aqJJzTKX7GBUKrUVDz5Ol82A-dNyZtPqc-9rHFoh02DM3H4XeosEwMyFa8SBynNySGpLFMlph3iGAAsCk98cufxHBoCWQdMuCuI8E9mUjjsVbsYydLYu1Ez3M4PTeWMZwyElYGBzmo0igytQeZCKTrFgQRRusUryWmJbjobf6MBRChLnP6d7_DBvpQaHfUS0X4DMfC-Q6l-k00V9S6TvRdv44CiWsLBCpO_lDIbJEzmdPNXy9Lgc49QjOsLPANVAM6K2xQBkBE37vZafuTGZC4JcdRacfG51dwbAGeSKwCWAq3EPoIujIcpnhGcyH1hVekMwVD9pwLr4yeBpPxCkSvgW9oYVaGkCoi-dPttqritE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=rwgRWaNaGx4XA7ZfyAOTy0V1jNGwpH4jolTzD4puVq2Kc42eKHwEi-x5eeSlIUqoZ961WDwIWG8KdTwM4NI9E0p7118NzDFlMca0-Su3FZv2d80DNAY92u-vhqpa03Xa33DPMaMOy-KR8Dmf1kenZRDSecSUnjBcwBTuBjWYJSsMgrrfytM369HCpcUdIQ0JfpOHh6QNKeWKgz0iVMPiPa53rXZ3mb5IMEixokJjCZtFOoPOaJK9BPQTimnoKrhoLK0CcVCg6GOV3BHQpJ2YgGKEDWQzm_L0Zp9Sdx9I8ovnudDrpvHMchDeukSUF74o4eFKkiqqN5_QnSXkYu4Aqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=rwgRWaNaGx4XA7ZfyAOTy0V1jNGwpH4jolTzD4puVq2Kc42eKHwEi-x5eeSlIUqoZ961WDwIWG8KdTwM4NI9E0p7118NzDFlMca0-Su3FZv2d80DNAY92u-vhqpa03Xa33DPMaMOy-KR8Dmf1kenZRDSecSUnjBcwBTuBjWYJSsMgrrfytM369HCpcUdIQ0JfpOHh6QNKeWKgz0iVMPiPa53rXZ3mb5IMEixokJjCZtFOoPOaJK9BPQTimnoKrhoLK0CcVCg6GOV3BHQpJ2YgGKEDWQzm_L0Zp9Sdx9I8ovnudDrpvHMchDeukSUF74o4eFKkiqqN5_QnSXkYu4Aqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOrIUiCg1IO2cbdmPEolU6nYYTbKRy_ytvK9qaCKhMRULf0_wxPII4bmsWOLGRP0pTTtxdYMO_ESxJjYyzluaWng4lT63neKx4JXbznKLLQ2prYBLS1JqePUehNpt5YNcF-fES_InaEFKFm1eO6i8rEGqXKBpJRm2v0wkPe6cuaCvBTEkwLzwneP_dDON2FvrRJU9Yse-SaBbLcf3nkqyB6KgHrVKnHQj7beuvRz9XKk8WWf6E6yAlQsPSfPk7bkJSJLy8RwWu4bbXiEaOWP_vGacVaQ2jzh-yB9VEz0pBCMX_sBHo3mhCKKB7MZd09STzCdaSEj28Pm9ClUDZ3ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=gbg9WJT6sz1_2aixdFoa4iRrvC3lJOjc8AqYWL_NMPmecZo1UpSl1TXmjRXVxYPqfXmixKG-sMVTtIdIoNRYwBq7a1p0Ua4gpySrTZjeYEiREHw6sPXsd9B1KoZxd5TZCZxDO7Ei-orWNogq4WMjPgXmRvHZeKRwBf4R8yyTfyVwaoNThNk9Upmdl-UgTDdbtXndL3TArNZMl6ldXykD2A2JW8SEgAh3x00nqvqz_FgxSQUBGyhm2w8-g7WKChfnIpbOvXlzwZtVjYGE5cfRlHDNH6HIX3RJkB1BgZaLzDwATofiQEKkPLBHbe9luAv-FsBmyvDmgywXPTncD2VOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=gbg9WJT6sz1_2aixdFoa4iRrvC3lJOjc8AqYWL_NMPmecZo1UpSl1TXmjRXVxYPqfXmixKG-sMVTtIdIoNRYwBq7a1p0Ua4gpySrTZjeYEiREHw6sPXsd9B1KoZxd5TZCZxDO7Ei-orWNogq4WMjPgXmRvHZeKRwBf4R8yyTfyVwaoNThNk9Upmdl-UgTDdbtXndL3TArNZMl6ldXykD2A2JW8SEgAh3x00nqvqz_FgxSQUBGyhm2w8-g7WKChfnIpbOvXlzwZtVjYGE5cfRlHDNH6HIX3RJkB1BgZaLzDwATofiQEKkPLBHbe9luAv-FsBmyvDmgywXPTncD2VOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=IDy_MP9sjUkJI2Mu9ve4Ihy1cIiKO8hymb2A9j8IaclwzkEtc_Pr9iceBv6zS4KHvEOUeQFpjTUWwgp7kQzuHLHZgp13Pqm4KeDt7tmSKr7BYNc-dlIUXihBUgeb0yrjeMOPMO5C7ZK8vEh-_-gDSeacwPgMtdGiHiCm9t2ftpUQzdL5Z3WTtLWWEVKiowWdduMtMTw2CdGb8Jmfir_gL9Yktclgr9Gs5KKjaisUNxf9cDEsK4qCmlxQevcDWDDegBd0a2cPyNs0NL3TAfLc7PqvTzNCZgTcvZSXRMT-CZ4td_CQJgcJ7x3Gq-OPYJiyJLMlRszwvjP6q4Cpd2BvVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=IDy_MP9sjUkJI2Mu9ve4Ihy1cIiKO8hymb2A9j8IaclwzkEtc_Pr9iceBv6zS4KHvEOUeQFpjTUWwgp7kQzuHLHZgp13Pqm4KeDt7tmSKr7BYNc-dlIUXihBUgeb0yrjeMOPMO5C7ZK8vEh-_-gDSeacwPgMtdGiHiCm9t2ftpUQzdL5Z3WTtLWWEVKiowWdduMtMTw2CdGb8Jmfir_gL9Yktclgr9Gs5KKjaisUNxf9cDEsK4qCmlxQevcDWDDegBd0a2cPyNs0NL3TAfLc7PqvTzNCZgTcvZSXRMT-CZ4td_CQJgcJ7x3Gq-OPYJiyJLMlRszwvjP6q4Cpd2BvVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=X-4qSlha0JrFoPLquYa39K20mwOW97yyB85QAa25Lc4TmjM0gT680SUEL0SC1-DBnBTcl86huza6QWBPaIAaMqYx_FcemPd1spNW9SSKsTNz_cxKHLdx8wGA6KBOjcUjaEOaGZzrM8xezzU29xeKcYPvTnmMwqqzFAp9qFJKtDu95MNT3bAU6dEt1ed23PJ1e2Ai-B94IDbIcUKxwnRQs5LOvOnh5m2itRWBKAZ7zxLEKtQkLxmYl_X7gIyVMq1cjD-l5PHf5vE8MEUDmhmKZp48dv682KHA3Wm6PV_PhB1cabkuOxI7xEXraiMMZNKI3l9Udw00NLS-XS5aUiMA5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=X-4qSlha0JrFoPLquYa39K20mwOW97yyB85QAa25Lc4TmjM0gT680SUEL0SC1-DBnBTcl86huza6QWBPaIAaMqYx_FcemPd1spNW9SSKsTNz_cxKHLdx8wGA6KBOjcUjaEOaGZzrM8xezzU29xeKcYPvTnmMwqqzFAp9qFJKtDu95MNT3bAU6dEt1ed23PJ1e2Ai-B94IDbIcUKxwnRQs5LOvOnh5m2itRWBKAZ7zxLEKtQkLxmYl_X7gIyVMq1cjD-l5PHf5vE8MEUDmhmKZp48dv682KHA3Wm6PV_PhB1cabkuOxI7xEXraiMMZNKI3l9Udw00NLS-XS5aUiMA5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAalZDk8Wivp1rb54E8kcJ5VThVJ22LOTeEUOU6S6b3hnxtsvmSn_B3-2ZTka-p_FWhjDAN2Kzgdy1T-2gmjvj_nM-MD1RZ3prV_JkuDQ2LpIU7g5QK648_O1TWbn4QeQeJuKXPEqgTnd19gsyKdoDHyp8zPWZyVZ_c1VI9BKpCEfSWslM2OmHvurPdkyKBtkhcqGSbWr3OzXfTHv6LAYhX9NXR46g7266VYxYsGQ6K10fkyaey8Pv5gGYmR1K7_obWoK70-xuzLr9jdJdHeHcVxQHXwVK-cfHGRS-E0b_Aw2oG4y7Mg1v-zlKrM5QARaQ5LjU3XMdDMs8ynS0J65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=mW-Ug_57wgUgDXLmyxDw5O-XYxVhA7S-igS2Uw8G5blNg6qF1slO0nlysQkLM1dBIBED87BiUSMu4HpQDaK93Ht1ITqiREbpCcbcWciFlpdVdpjM6Tvq6mf9bsllZOcuz3ZtEqx9ABTDUFH1WXJ40N-AlHbFSpA3f6EoOS0bson78KFXYO4vbCn6hFptWkKq60cfyhUtt5CggELQnGwvhkmpcipRbChjSjhAbgNThtP4sRmPL8Pf7p8FHV4D0xz7jcp3zj6X44dSrRItBrfUSn9MIsK1eDSLqAooeiOTLvMPWcX4nlz94x5C4bwfvxXIj0QN2ktWGIvsZJejn336FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=mW-Ug_57wgUgDXLmyxDw5O-XYxVhA7S-igS2Uw8G5blNg6qF1slO0nlysQkLM1dBIBED87BiUSMu4HpQDaK93Ht1ITqiREbpCcbcWciFlpdVdpjM6Tvq6mf9bsllZOcuz3ZtEqx9ABTDUFH1WXJ40N-AlHbFSpA3f6EoOS0bson78KFXYO4vbCn6hFptWkKq60cfyhUtt5CggELQnGwvhkmpcipRbChjSjhAbgNThtP4sRmPL8Pf7p8FHV4D0xz7jcp3zj6X44dSrRItBrfUSn9MIsK1eDSLqAooeiOTLvMPWcX4nlz94x5C4bwfvxXIj0QN2ktWGIvsZJejn336FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLT9nOrd8oXIU_faWtHmZjybtQspThvfagr1bJ6Mz7vLPjD22JbPLGvocevoaJIwo_o9_4A0LmWPRuG93DXuxQQ99b_uyNTKb27rGQU_8KszyHYoFcO0Mll5MMpWtIp_xPxHpOqVCb1oQrBrJeeixFgbTu-misf0uZHupwa7ofJHeWr5PiaWBkHkLqVs6L5V_fD6xIRSID2cO7_ls0CRWeoO3PLhGDmkiv9N5pr3R1tpXp4U6rGV8-WaT6AC88dP6WDeu79DkgaA_7b3LYPleBWoEjNCSZP9I05sUkqvzuM7navhV0YnRFDRwLKfa0CmGyGC27qBxKu0VZu5eX0QGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
51سال رفتار نامناسب!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69818" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=bfCMG8yW2sTsgJURA_fWZSbxtIbSOY2gOvciXoy1ijZKWHga1b57d2qRVJj3VI1_8p3eWvUxmwyOrjGWsTi87A7BRBK4dh6HpvHDTc3VnHSLYwmajVssr3-ivGaJxmrB0-eA6UqQ7061WiycMrKXcNT8fjc8eaI-nQLs3lqIdIbKpt2eU7EkBpouU7JaVqGgX6pD1M7BnslhjhHanHuy89u_1-6ZaOARw1CbvvFLRLBLEE_7lUGE7OgTJE7qK8_l4ME44Y_mMCmhtJgzcOdm2avbXucw6Fs8PNwJnRplJcAmervmLZxNDCxoOOKmVpSSiegl7aq2KU1yIVgNGoeMiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=bfCMG8yW2sTsgJURA_fWZSbxtIbSOY2gOvciXoy1ijZKWHga1b57d2qRVJj3VI1_8p3eWvUxmwyOrjGWsTi87A7BRBK4dh6HpvHDTc3VnHSLYwmajVssr3-ivGaJxmrB0-eA6UqQ7061WiycMrKXcNT8fjc8eaI-nQLs3lqIdIbKpt2eU7EkBpouU7JaVqGgX6pD1M7BnslhjhHanHuy89u_1-6ZaOARw1CbvvFLRLBLEE_7lUGE7OgTJE7qK8_l4ME44Y_mMCmhtJgzcOdm2avbXucw6Fs8PNwJnRplJcAmervmLZxNDCxoOOKmVpSSiegl7aq2KU1yIVgNGoeMiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی یک کشتی در پی حمله سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69817" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه‌پاسدارن یک کشتی را در تنگه هرمز هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69816" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69815">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=jHZN-e5Ju2bc8KZ04rUEH7DfSIT_gGf1QZ9vdY_FvTsl0kPcNDBhq0SHBfJdftjclz5_wZD3t_2oR4493RGl1KbJtTCKEa8KiZkkmHY71CrtiUi-eTzkCr0h83yJY1kA1I1CCAh4q99lIUX3UgnJkx-8DRMsmCBHwAB1GYNgIijyGsLlue6CP8htGoiSUwvgiXm9FpsjHIGIEluCsaGRlzRbRoOl7ACgRBLM3xIgh9RdGRJFHRy5MbI7oaPM8QpB_g885ANHJozWhnx-RKNLfKhwhyoiVIHrMDbf0tVOwdowzvE6TVXD8t_gb7RXHnAd0jJ6wdlRfVAUCQ1QEXPJsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=jHZN-e5Ju2bc8KZ04rUEH7DfSIT_gGf1QZ9vdY_FvTsl0kPcNDBhq0SHBfJdftjclz5_wZD3t_2oR4493RGl1KbJtTCKEa8KiZkkmHY71CrtiUi-eTzkCr0h83yJY1kA1I1CCAh4q99lIUX3UgnJkx-8DRMsmCBHwAB1GYNgIijyGsLlue6CP8htGoiSUwvgiXm9FpsjHIGIEluCsaGRlzRbRoOl7ACgRBLM3xIgh9RdGRJFHRy5MbI7oaPM8QpB_g885ANHJozWhnx-RKNLfKhwhyoiVIHrMDbf0tVOwdowzvE6TVXD8t_gb7RXHnAd0jJ6wdlRfVAUCQ1QEXPJsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یه پسرِ جوون تو تجمعات شبانه:
به ابالفضل راضی‌ام جنگ زمینی‌ بشه، یه تنه 500 نفرشون رو حریفم!
ایشالا روزی بشه مکه و فلسطین رو آزاد کنیم.
ایشالا روزی برسه آمریکا رو نابود کنیم و تو کاخ سفید نماز بخونیم.
نیاز به بسیجی‌ها نیست همین بچه‌لات‌ها اسرائیل رو میگیرین داداش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69815" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69814">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b396273688.mp4?token=jmFmCWdcFVtwtiIUSxeffNfjPqKpuZ8IA1HyfWUMtgbR1_YeY9jqMjdYcuJt6d5NZZopNzabRLY6BTdgMyCdKpf4a8wT_m_fMzVtuYiaP2OK2buxL12VkLWAX6Hz2MHpDnd1YfUjl8C3x63r_uyx_Mvl4owhkysZ_2ZrksFzAXzKOVePPcuOElCso7czis6dt3RhipEj30OsZQvJKnKwbZIKCSzNWg1VdHShvVad4oNjhLsDcr87oJTI3-vfv2PkfvKHpTJhom4bG3mTo_naQCJKvmGOdK4j0WOMcYAEaxEJbPIwnZGdQSQrb6Y14dRtkd3houmsVCPKz7YJrZAidgivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b396273688.mp4?token=jmFmCWdcFVtwtiIUSxeffNfjPqKpuZ8IA1HyfWUMtgbR1_YeY9jqMjdYcuJt6d5NZZopNzabRLY6BTdgMyCdKpf4a8wT_m_fMzVtuYiaP2OK2buxL12VkLWAX6Hz2MHpDnd1YfUjl8C3x63r_uyx_Mvl4owhkysZ_2ZrksFzAXzKOVePPcuOElCso7czis6dt3RhipEj30OsZQvJKnKwbZIKCSzNWg1VdHShvVad4oNjhLsDcr87oJTI3-vfv2PkfvKHpTJhom4bG3mTo_naQCJKvmGOdK4j0WOMcYAEaxEJbPIwnZGdQSQrb6Y14dRtkd3houmsVCPKz7YJrZAidgivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خرازی:
این کلیپ ها جعلی و هوش مصنوعی است؛
من این حرف‌ها را نزدم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69814" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=QqG_6UlDzGCbV-lHWzeJS_BycqdVSePLrPt2thJZH42ndtAleMmod2G9FEPooDHgKoki_6eaWW62EXCJeO8ax-ljxrkpe7M3YyDGTKjXP-kU6N5PYDqa_71MLCmDXNQTwZoGjBu8Kg1snPdg-3wDPYE7PZb6rjsy9IHmG768s_P_3rzLgQgdykTyYaPL3BfbTCrDYOU7o_bKVDNQ2hA6XzNmz1noBasOZGQz3I2fLoLOQ6MIYu3T_35rCP7xTMbdy_gtCuwVxSN21VKRCvsEO65occzbyx8Rzwo1ULiP48nHMDmfVaaRN8BA0ipcJ7GSv7YS1WrRze2hzTyR47cHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=QqG_6UlDzGCbV-lHWzeJS_BycqdVSePLrPt2thJZH42ndtAleMmod2G9FEPooDHgKoki_6eaWW62EXCJeO8ax-ljxrkpe7M3YyDGTKjXP-kU6N5PYDqa_71MLCmDXNQTwZoGjBu8Kg1snPdg-3wDPYE7PZb6rjsy9IHmG768s_P_3rzLgQgdykTyYaPL3BfbTCrDYOU7o_bKVDNQ2hA6XzNmz1noBasOZGQz3I2fLoLOQ6MIYu3T_35rCP7xTMbdy_gtCuwVxSN21VKRCvsEO65occzbyx8Rzwo1ULiP48nHMDmfVaaRN8BA0ipcJ7GSv7YS1WrRze2hzTyR47cHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ماجرای عجیب و تلخ که زندگی یه ورزشکار رو زیر و رو کرده
این بنده‌خدا یه ورزشکار ۱۳۰ کیلویی بوده، پرس سینه می‌زده و از بهترین راننده‌های جرثقیل هم بوده؛ ولی یه ماجرای مهریه کل زندگیشو زیر و رو کرده...
همسرش مهریه رو می‌ذاره اجرا و حکم جلبش صادر میشه. وقتی مأمور برای دستگیریش میاد، فرار می‌کنه و مأمور هم به کمرش شلیک می‌کنه؛ گلوله باعث میشه قطع نخاع بشه.
حالا با وثیقه آزاده، ولی هنوز داستان تموم نشده؛ همسرش گفته فقط یه هفته وقت داری، وگرنه دوباره باید بری زندان!
از یه آدم سالم و ورزشکار، رسیده به این وضعیت...
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69812" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69811">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇺🇸
وقوع یک حادثه امنیتی در نزدیکی باشگاه گلف ترامپ در شهر بیدمینستر، ایالت نیوجرسی؛
فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) دو فروند پهپاد را که حریم هوایی محدودشده بر فراز بد‌مینستر، نیوجرسی (Bedminster, NJ) در نزدیکی باشگاه گلف ترامپ را نقض کرده بودند، رهگیری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69811" target="_blank">📅 22:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69810">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgwFKpIHtlzeXzT82CB7DZdji1huTDYpsxxZmZBH_FGIc488NWWvwRmOLYQGa2JSs1qeGPtsg80yXolxt181SuLJBFRUdUJBtICug_7ZNr0zKa5pgwOxiHJaAFcfZ2lrxw7RZ5se6I2KKpzpGP53pd1RDq7dfx7yGTMn_QXwIDbkKqoGVVFRJdeFqaUMlVMBupAwYd7NEERM1ksjmflyATiRBjN-o79VtWccNEZ4KeA6YKOo25CzhAEcnyRej1-xftNtYewjSFK3_YdVphqdaNqj41PCQtvX6IUslsW2Fuj9TuwLfQ06TCJvXMPPLOYXuUlG_qxeNhRqRYekMugb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
با حکم مسعود پزشکیان محسن رضایی رسما دبیرکل شورای عالی امنیت ملی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69810" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
یه فلسطینی به زور بچه شو میفرسته جلو سربازای اسرائیلی، بهشون میگه شلیک کنید بهش!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69809" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmncPrG5mHce104jBLxS2X2l5oIom3p0Hu7ASxwvdAAF5N4LpYFxmJSbNDafS1a64wD_Nj_VAgFKGvGBZG12ekidRLgn7YT47M25hjkDN2xliKYm9HpOtvf8BdA7wAKzsN5dQNsZdm0hhVwJ1BjjTW2Og3WscEvX5nBBrhe5PLIRR1kK9GQArFubb7dtp6XaebkCcgqQzIJ7zppMYwYnZNZdksoINnInf0ovgukQY-tZ2y3jJ4nkb4masltZ8ovKWVhshmBwXeUaYPdVydpqgWk_npExatlk6fumBfGhFaBRsGx4i8-m5y3Poy2obC6Yz8IkRfw4qL4CEApqNLnGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
اکسیوس به نقل از ترامپ:
ایالات متحده در رابطه با ایران «بی‌سروصدا» عمل می‌کند، که نشان می‌دهد واشنگتن فعلاً از اقدام نظامی عمده جدید خودداری می‌کند و در عین حال اجازه می‌دهد فشار اقتصادی افزایش یابد.
ترامپ با این استدلال که ایران از نظر اقتصادی «در وضعیت بسیار بدی» است و در حالی که محاصره دریایی ایالات متحده فشار را تشدید می‌کند، برای پرداخت حقوق سربازان خود با مشکل مواجه است، گفت: «این [مشکل] حل خواهد شد. همیشه حل می‌شود. مثل یک بازی شطرنج است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69808" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69807">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🙂
لحظه کمیاب واژگونی کوه یخ غول‌پیکر در سواحل گرینلند؛
ویدئوی ثبت‌شده در ۲۵ ژوئیه ۲۰۲۶لحظه واژگونی یک کوه یخ عظیم در سواحل گرینلند رو نشون می‌ده.
با تغییر مرکز ثقل بر اثر آب شدن یا جدا شدن تیکه‌های یخ، این توده‌های عظیم برای رسیدن به تعادل جدید می‌چرخن.
در این فرآیند، بخش‌های آبی‌رنگ و شفافی که میلیون‌ها سال زیر آب فشرده شده بودن، برای لحظاتی در معرض دید قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69807" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69806">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=ftniLweDWCYrBrMVaJ_fKsvQNJAK5N1yy2GJy0vgUdstWS6etxuaBfe1Lshv15pNobWkp9OsO77A_vMywaVA8EqJh7IJK1jOwuAVqEUIiDKViqQgWCcA8NXW3Q2H3nUugQ9ts-CPLqEpbKcE41Tav8u3fN3cM6lg-1Ja8m5ES2JUO3wa_R9D4t41_PxokW4SG0u3X23h11mY5vDr_44fvGxtGtKvOEdeKVXo4AbADorTKNWmCu50f9uq6Bx1qnFkHxsi70l2bdSx3N1ciTSeXm33pN99vJh6NR9SSnFABPqxXG-zaN0rFUFRX2tzcOfdSFdAdHcPTJmqQP9DIJJAxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=ftniLweDWCYrBrMVaJ_fKsvQNJAK5N1yy2GJy0vgUdstWS6etxuaBfe1Lshv15pNobWkp9OsO77A_vMywaVA8EqJh7IJK1jOwuAVqEUIiDKViqQgWCcA8NXW3Q2H3nUugQ9ts-CPLqEpbKcE41Tav8u3fN3cM6lg-1Ja8m5ES2JUO3wa_R9D4t41_PxokW4SG0u3X23h11mY5vDr_44fvGxtGtKvOEdeKVXo4AbADorTKNWmCu50f9uq6Bx1qnFkHxsi70l2bdSx3N1ciTSeXm33pN99vJh6NR9SSnFABPqxXG-zaN0rFUFRX2tzcOfdSFdAdHcPTJmqQP9DIJJAxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
طرفدار حکومت در واکنش به کشته شدن حمیدرضا رجب‌زاده:
شما زدین مبارک شما ما زدیم مبارک خودمون
خدا سرشاهده جرائت دارید بریزید خیابون
یجوری تیکه تیکه تون بکنیم یجوری ریش ریش بکنیم شما رو تاریخ تو خودش ندیده
به جان امام شهید قسم به جان رهبر مجتبی قسم شما رو با کارتک از وسط خیابون جمع خواهند کرد
جنازه شماها رو میدیم سگ ها بخورن
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69806" target="_blank">📅 19:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69803">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QeyB1viPMKeqtls9Q0JZk-Nmb-6voo78Nj5t811FxK6W48Nn_kf0GSsevjnXbzZQG40Os_YCaTGF2I4qbWjeTAuHMk6RMy4E7XMckawygzn-Z-FMtL8we7Bkq1peOaNPd1m_1_bNqj50QDhspeZdW3sNr3JHuTlGAQXfn4uiv9zkhEzwdPjeQASGjYmko82tut8_zmPOjlgVFDNgMZABIuI7ARKU2RQicCgogbptRHqSZaEojMxSWiSckAigrKBbjZ6onlpvfl8xZ741imbGEOQahkroCgk3XYza6WRuf3PiCfkS8r3vvPtIUI1rCNXrOfxGa8fN0FgX5ZcqsjUo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ROj62qA_0OdyNr0NCUVm4qQMRx_EBzJRVncZJrgxYae2vp3FSYsQc9G3fD3R788etqOLCVCqYq_2ixskzjFsAtDx3Zx4AZQewc4oTCYS1uq0drhKDl1vDLjrqMrPLwyKLD1kw-SM2Xq3iQCDyKvEvhKyw666rb-6VeHQ2nHIaeb0fmcQ0EAbXhoo9T_KtpnlVkdWhcQol2zotSSqHvXcIdMXbzPL6kwuGS-pbv44LOR0CEmf-FqvqWeFeO3dtbVGyoVmBhmE_ALuXUjBZDVbl3zbOypnf35jhqaEmYjEDH1OmMfixMGDZDxUeRsayH5llDPay2gmPMIEOKv-6cYbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rsOeS6ROrYmLCWuiW4On05TAHx4EKjstqOf74kSJtUBEYNd_V4T8UMxWix-_A8CrTwawhLDmp9kqVXrlTMH8-eIzH4WM-jYpQKdP0MaBCXgunLRzTLngEJP-XBjA5VhXbM17QgIbXO-MhpwOFsGz8Img8qzm-OzJYT0761f3lvVGfECaxOtzOWHOV3gDTeLf0WjtbyPP5Ju63Y1UK1QfrX8C6JTya81b5KZNST0QKOerrYYjrojiVqNwIlujYzYysTUbEkPNHwirRIxDborAlhMQeEQdf5ILiESFHnBCwZPy5Flody8XeiYq90H2jsfnv7HHN4VVASFg6aZPt2a8ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ریورز یکی از مشهورترین فمنیست ها که زن رو برترین موجود میدونست و خودشم علنا لز اعلام کرده بود با یه پسر خوشگل و پولدار رفت قاطی مرغا
☺️
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69803" target="_blank">📅 19:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69802">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=rVbDcc_bedmkoE7abwmC_jWIE2SDxW8SKfthatFgxwz4jVfJF7b4KR4LpFATFzCXjSDY8E58QKt-5uv5KqDQJfEMQ-X_Nuj0CAG2HbuGzNVidP-WyCAJVQrgeHRYazkcn8olPySn-2WfqETeg6J17FtaWeySggoIP5n_pYuRybUGo-OW3yew39Jy0C1dYL12RpQKcLAWYqUWIDYxMgdlrHiGxEqPAa2hJFPM6eutSf67dBwp7JUU_u3ysAa_HFwiu3NVV7DrhkjczIX2s73duroqMqsU-4sagUjrnQr79xY4Sz8J_GLwWca5yXFFYYBvsDEP5hKe6o89gktGaf3WPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=rVbDcc_bedmkoE7abwmC_jWIE2SDxW8SKfthatFgxwz4jVfJF7b4KR4LpFATFzCXjSDY8E58QKt-5uv5KqDQJfEMQ-X_Nuj0CAG2HbuGzNVidP-WyCAJVQrgeHRYazkcn8olPySn-2WfqETeg6J17FtaWeySggoIP5n_pYuRybUGo-OW3yew39Jy0C1dYL12RpQKcLAWYqUWIDYxMgdlrHiGxEqPAa2hJFPM6eutSf67dBwp7JUU_u3ysAa_HFwiu3NVV7DrhkjczIX2s73duroqMqsU-4sagUjrnQr79xY4Sz8J_GLwWca5yXFFYYBvsDEP5hKe6o89gktGaf3WPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک فروند پهپاد بدون سرنشین جنگی (UCAV) نیروی هوایی ایالات متحده از نوع MQ-9A Reaper که از فرودگاه چابلی برخاسته بود، در نزدیکی گورستان چابلی در جیبوتی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69802" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69801">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69801" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69800">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PY_dbzVBF907WIgKucCiszqHVMnQprLbsaVCZgKATC6hGP-YZvjiPVsWMIdRFdZ_B74-riZmrHWEMCNhjA9GEiu_Mg7bNit-yTd9cNzR6QYT_ML2BaIHkkwHNiRKOblnnH8TVzQikVYCQi7p9Re26jBWLzYBNiQJFHvW0sDV3TBwwL9do2w2waCxHpv9n1rEbQCc5XyJSnt7guaGE8qOtGz5qkuqIC1Jqr25NB2kxK0y38baAFVprbHLTCtJJUmWf22a4VZgSC3QJMS-PM-4LlW5bKbrWiFCTbSjq6eclvkK4n_YHHEgwv2iw7bsJ75qNl4I_KjiZWHVB_Bcan11fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69800" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69799">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411943761d.mp4?token=TGZz0WSe2_tvG-Ikr262rpMT7y2jpxWIyW2TjNGMZuWFPiJ06prySUHAS67usx5PPpU5u96rry90Tf6GA_IhDODLw58TufeYLFFEmgj-GkqoRtVCky4Qfny1fqW0xuQwYOsxA30yKPr4-PhrvIz7WDgTWdUvm3AWojxd54dR1EFDlSuudMNm6pjdvoDssLctNbHvoEok_XrskKfy-JCf09qST_muDRnECjWIBBjMLPMFBp5EAVGKrS_jh5WlRl0Nv_A2KD51CeNXbbw1PhZ49zEjgAGyDR1hEqaoELWh2QTrnWc001BzxovYQCavj7-5eL4Gd3LeLEc1jww4c6jovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411943761d.mp4?token=TGZz0WSe2_tvG-Ikr262rpMT7y2jpxWIyW2TjNGMZuWFPiJ06prySUHAS67usx5PPpU5u96rry90Tf6GA_IhDODLw58TufeYLFFEmgj-GkqoRtVCky4Qfny1fqW0xuQwYOsxA30yKPr4-PhrvIz7WDgTWdUvm3AWojxd54dR1EFDlSuudMNm6pjdvoDssLctNbHvoEok_XrskKfy-JCf09qST_muDRnECjWIBBjMLPMFBp5EAVGKrS_jh5WlRl0Nv_A2KD51CeNXbbw1PhZ49zEjgAGyDR1hEqaoELWh2QTrnWc001BzxovYQCavj7-5eL4Gd3LeLEc1jww4c6jovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آقای پزشکیان بچه‌ها یه شوخی باهاتون کردن راجب درختی که میخواستید بکارید توی پاکستان، برامون بگید قضیه چی بود؟!
🇮🇷
مسعود:
من فیلم بلد نیستم بازی کنم.
اینکه الکی یه خاکی بریزی و بگی من درخت کاشتم پس تو نکاشتی.
ما نایب رئیس بودیم توی تبریز باید ده تا درخت میکاشتیم همشو خودمون کاشتیم.
ما کشاورزی میکردیم، همین الان اگه برم مزرعه خودمون بیل رو میگیرم کار میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69799" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69798">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=WyrJs5_kWwmDDlw0c1qlxeZHsp7TaLCb4Nh_Ta1j-SiLPhH60hefoMiXeojXmeLDKDAvlnXSRTQL7uoc4OCsmWlW2tI0t1x5a43HLjFuKGLBheEaynijnXY510PRrqzQdkVa-eQHYudo61ifz6W-TNK2SHoBhFYW48DieBFfGQR3qL3_cYs6aKD24lAXjQln-9j8Es0FIHRuffZru9tiVmFeqivFExJP9ls-mg0inLMDxi0FU9CtZmRuuOGwrJHDvyyRI4BER9kWWX7fch2agQ_ENWxCw-o5D-YiNdB_Tl_ND2vVZozVqpIHr-YXSzp_Nn7eXuFaMt0dwo4v99j32Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=WyrJs5_kWwmDDlw0c1qlxeZHsp7TaLCb4Nh_Ta1j-SiLPhH60hefoMiXeojXmeLDKDAvlnXSRTQL7uoc4OCsmWlW2tI0t1x5a43HLjFuKGLBheEaynijnXY510PRrqzQdkVa-eQHYudo61ifz6W-TNK2SHoBhFYW48DieBFfGQR3qL3_cYs6aKD24lAXjQln-9j8Es0FIHRuffZru9tiVmFeqivFExJP9ls-mg0inLMDxi0FU9CtZmRuuOGwrJHDvyyRI4BER9kWWX7fch2agQ_ENWxCw-o5D-YiNdB_Tl_ND2vVZozVqpIHr-YXSzp_Nn7eXuFaMt0dwo4v99j32Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخشی از مستند«پسرملا» روایتی از چند سال آخر زندگی روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69798" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69797">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.  او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69797" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69796">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr3KSWvgP7XVRHY9kjgFRNjSjYlOpje0l4LCqFNVyntIvSYcsMZVhW4VO5_foKLdgpogO6lZUzUBMBcRxuHnw3gGQy4NfUzhgsab8aGAdRhwvmzBxBfbIIKx2jcfCS7CyhhDcwXQXaHtStldRoR90-Nl9EtN_wF4ZQTgwgAb8b6l81MsRMhlANRCe21HirqYpWryKLPu6vi50bwV3-31EZNoQb9LU4xYnybovrY9e9uOdTFgle3u7jZuhupO832sfGNJTTEIkBsPh-2_i0BN1dbpZstD8X7AChN7J7dq23A3lVWlc8kZXnq3fL4Gt8Im92Fek2xHdZL4Dyt_ojqmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.
او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق هسته‌ای به پایان برساند.
ترامپ معتقد است که ایران احتمالاً در طول دوره ریاست‌جمهوری او، برنامه هسته‌ای خود را از سر نخواهد گرفت، به ویژه پس از اینکه آمریکا سال گذشته سه مرکز هسته‌ای بزرگ را بمباران کرد. مقامات آمریکایی می‌گویند که اگر واشنگتن بتواند فعالیت‌های هسته‌ای تهران را کنترل کند و ترافیک تجاری از طریق تنگه هرمز از سر گرفته شود، ترامپ احتمالاً تمایل بیشتری به تمدید آتش‌بس فعلی به طور نامحدود و رفع محاصره بنادر ایران خواهد داشت.
مقامات آمریکایی اعلام کرده‌اند که ترامپ همچنان مایل است تا در این بن‌بست دیپلماتیک جدید صبر کند، به ویژه زمانی که قیمت بنزین نسبتاً ثابت و در حدود 4.02 دلار به ازای هر گالن باقی مانده است، در حالی که سال گذشته این قیمت 3.16 دلار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69796" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69795">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=PEcUbhNLXy12mW-C8OkswUDD7BPMtzrEwJc1GFNJjvnAjcOkdTXjZJdk7z_YKBad0bhYZoLbneBVfja47XaiJz2VfDMVK-zVjvYxe_aj-XbJqKffVmKCvhFilBJlSAQMdLjNzLsGAcpaPe7wx89z-1K8qegWrfxW9IzlNkSE6GvrSsG5nWdOKzLlJXsADXZhhLd-5uF2K5R2JhQvNBxnfQDqqUQ6rDt5VhIhZR6JyucBvvOpw_D5-wyg3Dsna3CfImjAietaVSfAubgDeH-sZGTJCuBuGAAfyGd1ECYxOHV6n2rCQlmqf95BY4yqzRgHI540kPAZkFeLYL7ksReUgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=PEcUbhNLXy12mW-C8OkswUDD7BPMtzrEwJc1GFNJjvnAjcOkdTXjZJdk7z_YKBad0bhYZoLbneBVfja47XaiJz2VfDMVK-zVjvYxe_aj-XbJqKffVmKCvhFilBJlSAQMdLjNzLsGAcpaPe7wx89z-1K8qegWrfxW9IzlNkSE6GvrSsG5nWdOKzLlJXsADXZhhLd-5uF2K5R2JhQvNBxnfQDqqUQ6rDt5VhIhZR6JyucBvvOpw_D5-wyg3Dsna3CfImjAietaVSfAubgDeH-sZGTJCuBuGAAfyGd1ECYxOHV6n2rCQlmqf95BY4yqzRgHI540kPAZkFeLYL7ksReUgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از یک پهپاد تهاجمی اوکراینی که به طور موفقیت‌آمیزی سه بار متوالی، موشک‌های پدافند هوایی زمین به هوا از سیستم "پانتسیر" روسی را در دریای سیاه جاخالی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69795" target="_blank">📅 17:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69794">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⏺
معاون برق و انرژی وزارت نیرو:
خاموشی‌ها در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
همچنین برنامه داریم تا یک تا دو هفته آینده، محدودیت‌های برق را به حداقل برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69794" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69793">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJLxZii7N8-kUVAD8eOKyOtXChIvRZJpvW2VAyXtAbaptjv76oJ2SpjbmcuskBjw-0rzujoRS2ixRg9Fr6gz0qBQv7paqaJkqLUsW0mj3CYpFw7VmCq746Bd4uVtvwgqd1d6Zkj8g2HUv-FpxpvW-eecyOcEruxzOezeGevAhmcB97FVl6P_rurcusJ-EpciYiYKLZbhZ8lmpFp1VzakOOLKU17SK4LOPXaaecJ4gxdneV2py8IzlnlJNt-tp0woXX9Zs12pww7DIyZqjnUuRSP01dDQES4d6flPKROTb12sS5TS1uq3IC1t-KFL-hwBGEwHOUaEsmJjgMryoBciVsxnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJLxZii7N8-kUVAD8eOKyOtXChIvRZJpvW2VAyXtAbaptjv76oJ2SpjbmcuskBjw-0rzujoRS2ixRg9Fr6gz0qBQv7paqaJkqLUsW0mj3CYpFw7VmCq746Bd4uVtvwgqd1d6Zkj8g2HUv-FpxpvW-eecyOcEruxzOezeGevAhmcB97FVl6P_rurcusJ-EpciYiYKLZbhZ8lmpFp1VzakOOLKU17SK4LOPXaaecJ4gxdneV2py8IzlnlJNt-tp0woXX9Zs12pww7DIyZqjnUuRSP01dDQES4d6flPKROTb12sS5TS1uq3IC1t-KFL-hwBGEwHOUaEsmJjgMryoBciVsxnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
به یک نکته جالب توجه کردید که ایران به همه منطقه حتی فرای منطقه حمله کرد جز اسرائیل؟
تا الان به ما حمله نکرده ممکنه تو آینده بکنه ولی میدونه جوابش چقد سنگین و دردناک میشه.
شایعاتی هست که اسرائیل عقب نشینی کرده و ضعیف شده.
این شایعات از کسایی به ما روانه میشن که میگفتن اصلا نباید عملیاتی توی لبنان و ایران بکنید.
لازم باشد بخاطر منافع ملی به بزرگ ترین دوستانمان نیز نه خواهیم گفت.
منفعت اسرائیل رو پایبند به هیچ توافقی نخواهیم کرد و ما مستقل هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69793" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69792">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=iWdjnSoP4tdtpya16yy8VGh42z_rwTs6ON7pptou0_SM2VMXVxMk5hgF7tDmUfz3G5c6WTntRK8KK6zOzoeOOGlLroe6H48mSHnc5RGopA6_d42rs-c94EBPGEPGW2kGG3zVjI3WiahR5_Ml6H6VppPQznQ11jQEFZ_H_t9bwtb9wbTRqK6bkCCs58U5oWsJ5DKldxq8T1OiL8ssJH_88FRCPDfPgiw6a0AZ6SJ-C4-QTnDhiK3CTTt9zEwS3iglFRtkn3DELhKqBRyiy3-2zg8opwQIWEMBdSxTDSYj0k_O0xStTv18gR4ansceYpQHLB68GykYbEQ7ccGzaODQSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=iWdjnSoP4tdtpya16yy8VGh42z_rwTs6ON7pptou0_SM2VMXVxMk5hgF7tDmUfz3G5c6WTntRK8KK6zOzoeOOGlLroe6H48mSHnc5RGopA6_d42rs-c94EBPGEPGW2kGG3zVjI3WiahR5_Ml6H6VppPQznQ11jQEFZ_H_t9bwtb9wbTRqK6bkCCs58U5oWsJ5DKldxq8T1OiL8ssJH_88FRCPDfPgiw6a0AZ6SJ-C4-QTnDhiK3CTTt9zEwS3iglFRtkn3DELhKqBRyiy3-2zg8opwQIWEMBdSxTDSYj0k_O0xStTv18gR4ansceYpQHLB68GykYbEQ7ccGzaODQSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آمادگی جانفداها:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69792" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69791">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=UJC_i-YRNGicr5Epop_93hKWImSJOYP5OW-L3sgcmmz_-KqY10r2d8Ib7cWZ1qAO2E5ywbZtcj-CcK0KZNICq5Yq6ylBoQPw2yfHlxCZTOghv3iEYHS9uzKmmPfnsZM35dVMqIi74inlH1pWCA5PsCY-Me1Nz1aAuQusi4dEzXUbvcycUhX9AgetrzIZ4_YLpiHrq23Yb3aqnLO9t3B5XnGWb7KxGJnnswpYZB6O06B99_zpj5RZdjCZB5pomp7ZYT_heUPnk1YTqnoMFR7WIhz9V1K4bA85UK-t9YyPyj2QXBzNSsNRoYSAXq3NZV2W04yoUaRmzpft7YOqtrW0Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=UJC_i-YRNGicr5Epop_93hKWImSJOYP5OW-L3sgcmmz_-KqY10r2d8Ib7cWZ1qAO2E5ywbZtcj-CcK0KZNICq5Yq6ylBoQPw2yfHlxCZTOghv3iEYHS9uzKmmPfnsZM35dVMqIi74inlH1pWCA5PsCY-Me1Nz1aAuQusi4dEzXUbvcycUhX9AgetrzIZ4_YLpiHrq23Yb3aqnLO9t3B5XnGWb7KxGJnnswpYZB6O06B99_zpj5RZdjCZB5pomp7ZYT_heUPnk1YTqnoMFR7WIhz9V1K4bA85UK-t9YyPyj2QXBzNSsNRoYSAXq3NZV2W04yoUaRmzpft7YOqtrW0Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ژئوپولیتیک:
ایران سامانه‌های پدافند هوایی ساخت داخل خود را به عنوان جایگزینی کم‌هزینه‌تر برای سامانه‌های گران‌قیمت خارجی معرفی می‌کند.
طرفداران این سامانه‌ها مدعی‌اند که آن‌ها موفق به رهگیری هواپیماهای پیشرفته شده‌اند و استدلال می‌کنند که فناوری بومی می‌تواند بدون تحمیل هزینه‌های سنگینِ تجهیزات وارداتی، دفاعی کارآمد فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69791" target="_blank">📅 15:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69788">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFfWiX1UfdUOCJzbE0geG6tSUQ579atdR1kwPMNNO-8avoBI-MwS6KUKu-KGb5__jUqPiEZAqF9UYV04y830qOQRF0s-EVjq3ZM6TcQTqj-fWZX0Rx7h1jFbxVfqaRnY6JrJDQgyBzoENmlRkqZ-X_L7digtcEhy4248Lu8SSr-ZPxVMzblpfT8pF5wxGff0Bcj5RoS8QZK2po5nHVZJk4kVX-xT54uxfSrEX63rGFlO8ljLRprXFoJ5X1BSlGz2XTMa_AZZHlnmAL284oxs3d3agcYb7k6Ph3AfJbtTGq-7hQoKBbK4DcFkpwWUyXpd_nsQNhJSZUmqNq5RTjKSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LddomGsWKqjU-JAzYGN0Seui1HRhTKo_tuSqhitsL6KxbQ_Fnwk1VyIPb5kOOLlIw9JWlGREQ7Kp1qqIIOVl4wXLdvCU0403px--5MJdYxjEOjqDX80oxYgeT20w3CpDTJ08RJqZZeOBJmotzgZqMu3vVawkFVvPJhe2Buqt-OD049jlf6_S9G-33f9_1j86MiZh_317Ej7rTKQNV23ZXQOx8gWC1cav2zLeCIncl5S_mWZ7zXqHMyMa3PSkNJrm7VJU2ju0U6PbfIObW-gTmwrRS7FK7mkCppVWtQuclbzyXTkjve4y_jU3u5irV6yvd0OfNLUnE3n0gJLfDzi3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8ZBLtLFERL7_TLmwWAgcR4h6Yv6TNTwX7RHrYfKMrZs-6wJ8zVLKh6LPp7hkF6MWM68JpqPKxU6l86_-_0NmRMwKsunMkmI_AvdLy1YT3H_mxazZN1XHasPq0rf0yToU5wOPPOzbikCfNW74JVRwabz5wsr8SbMX7XZBsE-QNr7PntIwBDxQSnw_Zpnn_qqbsE6jnqXr84KliQ-0TKlUBqrcLO2kKBo0styt2yTXuwsa73aHH2daw2950-YZpjV7nBT5GL3GGJcw8toM5xZoN1LhzayORxdAc4u4NBP6r8xyfpRwe1XZjjoxVncnDZqAFAE0zNaN1GApMj36tUfKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🔞
ابعاد جدید ماجرای قتل حمیدرضا رجب‌زاده توسط یک بلاگر دختر:
حمیدرضا رجب‌زاده، یه مداح جوون، بعد از خروج از خونه ناپدید می‌شه. پلیس در تحقیقات به یه بلاگر زن می‌رسه که قبلاً با حمیدرضا در ارتباط بوده و اون روز هم ازش برای یه ملاقات حضوری دعوت کرده بود؛ حمیدرضا به این دختره بارها بخاطر حجابش تذکر می‌داده و بهش می‌گفته بحث سیاسی نکنه
طبق اعتراف متهم‌ها، این زن با کمک پنج مرد، حمیدرضا رو به یه محل خلوت کشونده، بیهوشش کرده و بعد اون رو با ضربات چاقو به قتل رسوندن و قلبشو از سینش دراوردن و رو صورتش مایع منی ریختن، بعد هم جسد رو به اطراف پرند بردن و آتیش زدن و از صحنه قتل فیلم گرفتن؛ با اینکه چند نفرو گرفتن ولی متهم اصلی هنوز فراریه!
🔞
ویدیویی که قاتل منتشر کرد
⚠️
⚠️
حاوی صحنه های وحشتناک
⚠️
‼️
اعترافات بلاگر دختر:
من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و زندگی مناسبی داشته باشم من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند او گفت که گروه های منافقین بابت قتل بسیجی ها پول پرداخت می کنند بخاطر همین بعد از اینکه مقتول کشته شد فیلمش را گرفت تا به آنها بفروشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69788" target="_blank">📅 15:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69787">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt6VSgR10OmuZlCVzDAoT2ntlfitzEO7i9DoZwEaEab3VkOECwdpx70M9iVt0OwA4RVLouEEBJ3FXUKpIUNo0tn3EGKPD1bjOz_fASYV6Xnib3g3b7BLLfg-61fltvELDt_levu1Cv49DV71T-FcNf3GZqPkrDnSpM4Pgn1UGIw-1-9DJOvZF_hRFRdjCK9Um209vwLD5cNfCvfROU1_huzI6m7nW041OSHmYNxbiW8HK1owO9dxCW15VliPqbe-AB8evCK5OCwV1idwyOwyxYiZq_BAiz80dooy7pVLsJa8Lh890zd52gTs29sk4NYgU3KIKVSXTy7GBPgjI7CJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فرماندهی مرکزی ایالات متحده:
ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند.
تا 8 آگوست، CENTCOM 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
🔴
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69787" target="_blank">📅 14:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69786">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای فارس:رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد.
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69786" target="_blank">📅 14:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69785">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
صحبتای این خانم در مورد کافه رفتن و پیدا کردن پسرای پولدار، خیلی وایرال و جنجالی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69785" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69784">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=EXqy5gEJVi_VwrkQirp12BDZma0B9BzSCy9nbFPxnlgSU1eua6kwnjZzLvc41g4eafkGCe-ZIAewizEZ-14LVumrcz8pCVX738ssvSbRt6DA5MdMKWiXG0ygyDEjBTcGkE5N4K8kJdhs7DxzUHODTdx7ClwG9aqxifYu-iCpWJBwZCuez4lMw5ds0TxnRjq3WlRAcfUXRew2df-DmE9SnqEnRQfUqRfZo4TZxhOjxuzZrFjXsqUDI00nIbqOw6fZdXKQUI7FRkgx2eIaj95Mb_c77hhrS9dOer3zm0N4CAZ8Tc88pWr7WZvtm7uGHj-adcq9nk6vFDYBsMnNPtInWA5taZUlRVeVBhtFU_ZbwVRlab4F7hq17aGn-ddhuRgcFw-N7saVUd57Q9c1ilKv5XYeGgzr_OQA5LaT45J3JNJh312GM3CyMe-v4y6ZiTZKxcu1xSV2jisaGE6pN9sF80VUeVAkJZ5qShwR6TZpuE6AFjP9YBMtpEmppqk374kPelP19sqwQPZ2wK8JGuHn8BEggpiLAzG4RvWKRoG8Vr44i9WjWrfOoV-x3RZeZ6O2-NggUdKd1gN5-orQ-i-xS35uiw1MUojMCOE8-hUKhjxWcDdYza8UYG2r6GWhDqKV0mAxpac_3dBrVY2XuaYjMOql7iWK7nW22jWxb-6qeWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=EXqy5gEJVi_VwrkQirp12BDZma0B9BzSCy9nbFPxnlgSU1eua6kwnjZzLvc41g4eafkGCe-ZIAewizEZ-14LVumrcz8pCVX738ssvSbRt6DA5MdMKWiXG0ygyDEjBTcGkE5N4K8kJdhs7DxzUHODTdx7ClwG9aqxifYu-iCpWJBwZCuez4lMw5ds0TxnRjq3WlRAcfUXRew2df-DmE9SnqEnRQfUqRfZo4TZxhOjxuzZrFjXsqUDI00nIbqOw6fZdXKQUI7FRkgx2eIaj95Mb_c77hhrS9dOer3zm0N4CAZ8Tc88pWr7WZvtm7uGHj-adcq9nk6vFDYBsMnNPtInWA5taZUlRVeVBhtFU_ZbwVRlab4F7hq17aGn-ddhuRgcFw-N7saVUd57Q9c1ilKv5XYeGgzr_OQA5LaT45J3JNJh312GM3CyMe-v4y6ZiTZKxcu1xSV2jisaGE6pN9sF80VUeVAkJZ5qShwR6TZpuE6AFjP9YBMtpEmppqk374kPelP19sqwQPZ2wK8JGuHn8BEggpiLAzG4RvWKRoG8Vr44i9WjWrfOoV-x3RZeZ6O2-NggUdKd1gN5-orQ-i-xS35uiw1MUojMCOE8-hUKhjxWcDdYza8UYG2r6GWhDqKV0mAxpac_3dBrVY2XuaYjMOql7iWK7nW22jWxb-6qeWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی:
اکنون هیچ مذاکره ای با آمریکا نداریم و نخواهیم داشت
شروع مذاکرات بدون پایبندی آمریکا به شروط تفاهم‌نامه غیرممکنه
ملت ما تسلیم اراده یک عده خاص نمیشه
بدون تحقق حق ملت ایران کوتاه نخواهیم آمد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69784" target="_blank">📅 13:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69783">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34556823e0.mp4?token=BKpnQO3NZVUCoI1EJfXgcKfLfm8eR6RjZzo45aJ07KdrlXK7N08eMrHWdMIhmjnX8ko6yvp_G8CQilh7P929ls2J0929JZ36bEFRo0zkmElK6au_a6OhFtNzzxcD2QsdDpxGKENLKndr_i6aeq1mTwKk6QigmZUEH-CNAM4Kr3AtoesByFxQvRfn7Io0f5AFAMUscCxUeFgFBOl01DhDZNPMtjIiQPlFrcKwN7N3_bSzqGzWN5rQC-OeoIVk5-yVJLZyY1RfXMGUQ0J5He2G_IAJ7Ldv9Qus3waT7IhYu-hVntGSvXQLZZy2u4CeKFFptBjUwvUYCpUAgz0qlL9Uag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34556823e0.mp4?token=BKpnQO3NZVUCoI1EJfXgcKfLfm8eR6RjZzo45aJ07KdrlXK7N08eMrHWdMIhmjnX8ko6yvp_G8CQilh7P929ls2J0929JZ36bEFRo0zkmElK6au_a6OhFtNzzxcD2QsdDpxGKENLKndr_i6aeq1mTwKk6QigmZUEH-CNAM4Kr3AtoesByFxQvRfn7Io0f5AFAMUscCxUeFgFBOl01DhDZNPMtjIiQPlFrcKwN7N3_bSzqGzWN5rQC-OeoIVk5-yVJLZyY1RfXMGUQ0J5He2G_IAJ7Ldv9Qus3waT7IhYu-hVntGSvXQLZZy2u4CeKFFptBjUwvUYCpUAgz0qlL9Uag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا متوجه بشید با قیمت الانِ یک نوشابه، تو سال ۹۵ می‌شد چه چیزایی خرید...
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69783" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69779">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_8OM_yQRv2mL04Cg-DY8qdVqK7bihC0U_-MNr-UJIbHhumo5wFSLhJfN_tswKHDg9b1x9QNiIOH4voJIsIfPpfJJFO8VebHo1aP8WPToGUsc7_S0lbJOIfUY6lVKHXOTxwL0VDebCLq1fcAxifw3sRXPt9j5DVR_KHGWauBRRvEQ43_cALz-RezwU5MgG8EzossNRCxfpj2xfukY44bXyGTLSJz20V_3EAJ6HvwI5B0GrIDCHG3ba_chFrCuZ3B0sbI-JKuDzoxihiCgHBg2gVjlimC5p-jk9_ea7muz4dFV_FQmb3uELnuZhjkVdi5P5GqmQGs7rN3p8IcHn7lzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=SyvDPZU3H4Ox-LInipAtO9l8oiYaFlIeWhgn9F4_b10XXAonhfJy8YdFSNxTbhbsKCNmLzU-BF0gU3NpViH9j7N3p7Smyodh5rjxYQAA4sk7hBd3n6cgt_fm_lXHO_o32CeNMMDPUJaYsR5q7gjNVZ40CGuGVvEV60emH15dZ3dcmLlNmcI8GfELI1XvLzdvQL0_sMtgdwAQzjQ4I_cfIX852KghHwySWc8zGwx3ntdDfUazPfliW7_YLP9t5xkJqS6supYxi4oAd079WLykUDDqKhw0uGx3PkPec7FMlecTW8xwGdTF4ruX2L-9hbNw_-R7Rkqihwd9zLO-YV5ghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=SyvDPZU3H4Ox-LInipAtO9l8oiYaFlIeWhgn9F4_b10XXAonhfJy8YdFSNxTbhbsKCNmLzU-BF0gU3NpViH9j7N3p7Smyodh5rjxYQAA4sk7hBd3n6cgt_fm_lXHO_o32CeNMMDPUJaYsR5q7gjNVZ40CGuGVvEV60emH15dZ3dcmLlNmcI8GfELI1XvLzdvQL0_sMtgdwAQzjQ4I_cfIX852KghHwySWc8zGwx3ntdDfUazPfliW7_YLP9t5xkJqS6supYxi4oAd079WLykUDDqKhw0uGx3PkPec7FMlecTW8xwGdTF4ruX2L-9hbNw_-R7Rkqihwd9zLO-YV5ghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به بلگورود
نیروهای اوکراینی شب گذشته حمله گسترده‌ای پهپادی به شهر بلگورود روسیه انجام دادند که در پی آن چندین ساختمان مسکونی هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69779" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69778">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69778" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69777">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N33x72PvhTEWZVK69ez0p9P-HDgf4t2EBz6xUJ7kjjf_ygVVHYIK6di5MbtLrMiV1-fXagCZcyaP8X6lzLJPKKi7RkHGQZJvcIGrMqd_1hf5HuqIASxb-FS_VBXArwIQ8Fr71LeFIJq1KKkjTP4M6odd57f0PUZG_ZfYnKpQjMPperCcXdu-M8Zif2HPTlzG7BQ5FH1olhezS0GkEhHQNQNn4k3z0TnWhbPD_MuvjJZjCMpwQQL9ipQhtE3Te-z-dN3HyD3GT9Ec-avYS0Tusnk_EbzG0c1aoaae39DZ14oGFhs3J2uqj-gVuSi_ta3REd6r7sEJh6iXs9BfrnGOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69777" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=v3WJAi_6k8EncNrHVviABfMhI1IjZfrj6rFQLeRx_IzZQQl1riYKCDxkGtpUWd6njdlJytGd8TZTwGpYilzduvzsHJl1_JhLBAaO6zHceRJVOW4CCGPJaMlDgUfNL1lTDNjE6nvq312trDUhI325a1u_QTxTyzg2nSUvGZezxHTbF62U-_QM_vTHN_ZrDkn9V8fOftXIPyDyox7cD5f2ji_yYZ8WeGHH2VZmaeFHuxmTSnGFV1-dYJP3f1KQ5VpaxKd39A7hMegzh_XibHBkQjm0d3tMnzwrKjpQDgtjw0bgltj5LWoB_PHnZGwCb4bbKGmCmx9nslBhKnGN4n-Qtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=v3WJAi_6k8EncNrHVviABfMhI1IjZfrj6rFQLeRx_IzZQQl1riYKCDxkGtpUWd6njdlJytGd8TZTwGpYilzduvzsHJl1_JhLBAaO6zHceRJVOW4CCGPJaMlDgUfNL1lTDNjE6nvq312trDUhI325a1u_QTxTyzg2nSUvGZezxHTbF62U-_QM_vTHN_ZrDkn9V8fOftXIPyDyox7cD5f2ji_yYZ8WeGHH2VZmaeFHuxmTSnGFV1-dYJP3f1KQ5VpaxKd39A7hMegzh_XibHBkQjm0d3tMnzwrKjpQDgtjw0bgltj5LWoB_PHnZGwCb4bbKGmCmx9nslBhKnGN4n-Qtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⚡️
تصاویر جالب از لحظه برخورد رعد و برق به ساختمان مرکز تجارت جهانی «اسپیرز» در نیویورک؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69775" target="_blank">📅 12:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=QjQsE2_gc1ObJ17GhBp8VaA5A5YWgfQ-K2RctgGmu_dy06fZuIUgHrvPz5PZkyG_W_UAiAu2Cw0mnsrHuARsv1xG3e01W5O7JRNi5MbAZ-XlcYH36sOSpiPa9S4jMXLyJk5rT3s2gdlntd2cd-UaVYkvoCtJIQROPx78f7R066EY-rFLYyI-4nOPl2Nfo93CS1fz5Lhu9m43ulxJjtRmQ8gpf-yljzlpcfQkQQIJ8IIi1UcBrHX6tKVtmVoI2Zk3kC6hjKZ2U1sGWRKZ1EOHhhirPrxYBPyKCjsr7v6G84-zxTxVGPlVtW3fdGFq1BgRGwGck025pjnXma2qa-fOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=QjQsE2_gc1ObJ17GhBp8VaA5A5YWgfQ-K2RctgGmu_dy06fZuIUgHrvPz5PZkyG_W_UAiAu2Cw0mnsrHuARsv1xG3e01W5O7JRNi5MbAZ-XlcYH36sOSpiPa9S4jMXLyJk5rT3s2gdlntd2cd-UaVYkvoCtJIQROPx78f7R066EY-rFLYyI-4nOPl2Nfo93CS1fz5Lhu9m43ulxJjtRmQ8gpf-yljzlpcfQkQQIJ8IIi1UcBrHX6tKVtmVoI2Zk3kC6hjKZ2U1sGWRKZ1EOHhhirPrxYBPyKCjsr7v6G84-zxTxVGPlVtW3fdGFq1BgRGwGck025pjnXma2qa-fOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
گوشه‌ای از سخنان وایرال شده خرازی، برادرزن مسعود خامنه‌ای:
جمهوری اسلامی یه موشکی به اسم «رستاخیز» داره که میتونه یه دور کامل دور زمین بچرخه و به راحتی خاک آمریکا رو بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69774" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ihTDv-4BRClK6tiyoRTF72cOhe_gRoD0kqf9KqFfkhef-rmZRUIU2pZ5Cnc4aD4hQIeG6zIXf38D1hMLjP3yIG2A_3U0Um8JtLf6IRpc5UeSCKE4mNBRmDpn-rdg73vs6X-nXZG8xtVFyvdt8dPWFF98BzIb16ZmwRjJq02UXJf9FCq1UPXlLhISCxMyQXUXpSp89ori8y-UNt1NHz1xZ-qTKLElT8f2hmfXt0m9Su9UPAxinoIOSMUBXBTDKFQV7kcBi4ocJT9U6v4fUxF3MhcdlTIQigfWWpb2QzzuwKqLsYiQwxuldJq5_mHJBtOInL8Hp5ZNnhyM9PBZGsDh05hg9PH-Q-qco8joqLJxVuCgEvVKFwuCqYiXOLDWT7Hte7COxEbSIVi3HB4DYlccXS_tcyACpMWaznwHtCxiAJOfaY83vClWqZfx9dDXwzmxac5_JpqOcQ47imIsQc4jrfS2GsmJMlOoVWHzuJboMlG1FqcGJCTB6_zJAOe9P6vSFQORZiRPEtL3Ej8hDm3TkVz3Toq9h2roBLFhBfDmFNGArSEfpZ-c6ZU9FuzT0WJIrZPU8sWavaTz9Ek19Fa3b90p4BRrwNw22zySdexz2QVBR7Lu41j2haHf67kGG1vmhn4N24hh8MIHsIfbu4JGI7MfG0mTGcA9BZUtqSqrNwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ihTDv-4BRClK6tiyoRTF72cOhe_gRoD0kqf9KqFfkhef-rmZRUIU2pZ5Cnc4aD4hQIeG6zIXf38D1hMLjP3yIG2A_3U0Um8JtLf6IRpc5UeSCKE4mNBRmDpn-rdg73vs6X-nXZG8xtVFyvdt8dPWFF98BzIb16ZmwRjJq02UXJf9FCq1UPXlLhISCxMyQXUXpSp89ori8y-UNt1NHz1xZ-qTKLElT8f2hmfXt0m9Su9UPAxinoIOSMUBXBTDKFQV7kcBi4ocJT9U6v4fUxF3MhcdlTIQigfWWpb2QzzuwKqLsYiQwxuldJq5_mHJBtOInL8Hp5ZNnhyM9PBZGsDh05hg9PH-Q-qco8joqLJxVuCgEvVKFwuCqYiXOLDWT7Hte7COxEbSIVi3HB4DYlccXS_tcyACpMWaznwHtCxiAJOfaY83vClWqZfx9dDXwzmxac5_JpqOcQ47imIsQc4jrfS2GsmJMlOoVWHzuJboMlG1FqcGJCTB6_zJAOe9P6vSFQORZiRPEtL3Ej8hDm3TkVz3Toq9h2roBLFhBfDmFNGArSEfpZ-c6ZU9FuzT0WJIrZPU8sWavaTz9Ek19Fa3b90p4BRrwNw22zySdexz2QVBR7Lu41j2haHf67kGG1vmhn4N24hh8MIHsIfbu4JGI7MfG0mTGcA9BZUtqSqrNwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابای این دختره چون دخترش توی امتحان گواهینامه قبول شده براش BMW 225 خریده ناقابل ۱۲ میلیارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69773" target="_blank">📅 11:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973161bf95.mp4?token=vSXtuxLGbZ_g_FYlBR4sY5soCeQTkMkJtxS3pLyVu4QT3b_aDHaz8oZKTkrBifNQ3fo8Ps7hyTEj4-fMHF83rCU46x-WQ8IgDQ9fSlgXb1L-FRXGMdJ8S_Afh08gbkB7TNZTOcTwfxbmIpg7im2O2T22xsZBSiv3j6ifBqIbp1uPklQLIbNjlKzV2NeQ4RnCgKRqgMaedkbF-OSxnz7G-VSvb0VSwO98OpisrZZdKCHpe8pzQiW_E0BuKDjZLZ3f4KFyCE5I9oHEsTJqKK2mbvEPZxBfIyqMOMBLLg90nA2jdIGKzC0IKFLba6o2WzqfHghcPuOx8JtWXmORi1re8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973161bf95.mp4?token=vSXtuxLGbZ_g_FYlBR4sY5soCeQTkMkJtxS3pLyVu4QT3b_aDHaz8oZKTkrBifNQ3fo8Ps7hyTEj4-fMHF83rCU46x-WQ8IgDQ9fSlgXb1L-FRXGMdJ8S_Afh08gbkB7TNZTOcTwfxbmIpg7im2O2T22xsZBSiv3j6ifBqIbp1uPklQLIbNjlKzV2NeQ4RnCgKRqgMaedkbF-OSxnz7G-VSvb0VSwO98OpisrZZdKCHpe8pzQiW_E0BuKDjZLZ3f4KFyCE5I9oHEsTJqKK2mbvEPZxBfIyqMOMBLLg90nA2jdIGKzC0IKFLba6o2WzqfHghcPuOx8JtWXmORi1re8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
علی مطهری، نایب‌رئیس پیشین مجلس شورای اسلامی:
از همان ابتدا، هدف ما ساخت بمب‌های هسته‌ای بود و باید تا پایان ادامه می‌دادیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69772" target="_blank">📅 10:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69768">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=DB0RTxoTdPK9EzFQiPTHV3I8WsvcPjvG44Ou4wPKiPV7xRzUVVscHHA-HgRcyR2xyypTX3wss81cG-mULy8ZzpQnRKf_a5TBmTXCikr0gm16b1VHLe4qGWLi57S_UK_p-Vn4d4DJ7dSTc_En9CQS7y18pKEQruoCG-ONOMZ2iB6qmpnzU7NCn_Pc8NQb-YAnADM-Qm02yOLfx4Ti1BVft8hDPetgUqkHZ4z2nDeGWUa8wWv4I0PGT4_YRkmP0wt7FFzYd30oPb-romfk0_NPXHqUFgMBgr_PVcG6LY9hLRN9bVnNctgccNXoCP2N3JAH449vJTq9Hw7u44msituaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=DB0RTxoTdPK9EzFQiPTHV3I8WsvcPjvG44Ou4wPKiPV7xRzUVVscHHA-HgRcyR2xyypTX3wss81cG-mULy8ZzpQnRKf_a5TBmTXCikr0gm16b1VHLe4qGWLi57S_UK_p-Vn4d4DJ7dSTc_En9CQS7y18pKEQruoCG-ONOMZ2iB6qmpnzU7NCn_Pc8NQb-YAnADM-Qm02yOLfx4Ti1BVft8hDPetgUqkHZ4z2nDeGWUa8wWv4I0PGT4_YRkmP0wt7FFzYd30oPb-romfk0_NPXHqUFgMBgr_PVcG6LY9hLRN9bVnNctgccNXoCP2N3JAH449vJTq9Hw7u44msituaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ایشون به اسم آرش، خودشو اولین:
همجنس‌بازه، شیعه، پادشاهی خواه، دو رگه تُرک و لر معرفی کرده که پشمای همه ریخته
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69768" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69767">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=Z0mVGTKaVEhnk0_-Ve6bqVVwhuRStV-_9Wk7muk6lSctKJahtTjpkVWk5KfpkN-Py04RDgtYXPbhaqa99JWe5MJer0XzhQ89RjJztiPdehkjFJa7MXxmZg9kALdqt1GH3ykj81iLYZBDArH_TPALrTFN6Ks4ZoOrVYgxtZisoLfXyGPLS-p-lucdtuMjDse__Evz2kneWP_-7RZMyPEZpS1MNYVqLkE5Gqg9kf1o3IhgQAceOXxLcOOx5a6Fo7Mm4fcncEcsGcqSVv4bSlKzZWm7LGzfL_NXFBddPq9FI-8hp5I36dtJaevzODBfIUWy4BpPKjTpzTMaSV38dm38Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=Z0mVGTKaVEhnk0_-Ve6bqVVwhuRStV-_9Wk7muk6lSctKJahtTjpkVWk5KfpkN-Py04RDgtYXPbhaqa99JWe5MJer0XzhQ89RjJztiPdehkjFJa7MXxmZg9kALdqt1GH3ykj81iLYZBDArH_TPALrTFN6Ks4ZoOrVYgxtZisoLfXyGPLS-p-lucdtuMjDse__Evz2kneWP_-7RZMyPEZpS1MNYVqLkE5Gqg9kf1o3IhgQAceOXxLcOOx5a6Fo7Mm4fcncEcsGcqSVv4bSlKzZWm7LGzfL_NXFBddPq9FI-8hp5I36dtJaevzODBfIUWy4BpPKjTpzTMaSV38dm38Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه طرفدار حکومت درباره حجاب:
آقای پزشکیان واقعا مرسی که گفتی نمیتونم قانون حجاب رو رعایت بکنم
مجلسی که ناظر هستی توام دمت گرم که اصلا فکری برا حجاب نمیکنی
پزشکیان داره میگه ععععععع مگه هنوزم گشت ارشاد هست؟؟
بحث دیگه حجاب نیست بحث پوششه پوشش و اصالت ما داره از بین میره
تو خود اروپا هم قانونی برا پوشش هست نه اینکه لخت بریزن خیابون
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69767" target="_blank">📅 09:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69766">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=GWmMX_jt7uyD213HAY6mZnmO1oWs8UbuVgilD_BsW3dQRJSa3Gi3KGhaIipJyLeuEH4em9pj3uM0l4GhjYjFNpFGb_L25hBPv632zA1-h_aMPwqAKdR4GNcCUM1Fv6qvNsZ7qD9r_Bm9mfFzeZp_ed-uIPYPTHfPoL4aO_FCRA-huN6LIvimQGVgYbcFqW6JM3omyOIsMYvm18EIdeqxoxbFwNryr7E4YVzCqPhz9IP_b9C064KzAh_qy8NQgKp_FUGgBn4TBKOTyR77sAmGwjRoi1N5ZA02eF9NetQ7ldWvqd0R9y1UqzA-ywrTGWpvhphKhHq9R5X8xqaHvnTG5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=GWmMX_jt7uyD213HAY6mZnmO1oWs8UbuVgilD_BsW3dQRJSa3Gi3KGhaIipJyLeuEH4em9pj3uM0l4GhjYjFNpFGb_L25hBPv632zA1-h_aMPwqAKdR4GNcCUM1Fv6qvNsZ7qD9r_Bm9mfFzeZp_ed-uIPYPTHfPoL4aO_FCRA-huN6LIvimQGVgYbcFqW6JM3omyOIsMYvm18EIdeqxoxbFwNryr7E4YVzCqPhz9IP_b9C064KzAh_qy8NQgKp_FUGgBn4TBKOTyR77sAmGwjRoi1N5ZA02eF9NetQ7ldWvqd0R9y1UqzA-ywrTGWpvhphKhHq9R5X8xqaHvnTG5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو وایرال شده از فردی که در زمان رفراندوم سال 57 حضور داشته
:
وقتی من روز رفراندوم رفتم بیرون و دیدم گفتن ۲۰ میلیون نفر رای دادن زنگ زدن آدما بهم گفتن بیا ببین چخبره.
اونجا رئیس حوزه آخوند بود و این بیجک های صدتایی رو میدادن دست مردم میگفتن بنداز صندوق بگو مرگ بر شاه.
جمعیت ایران اون زمان ۳۷ میلیون و ۲۰۰ هزار نفر بود.
کل کسانی که بالای ۱۶ سال بودنو و میتونستن رای بدن ۱۸ میلیون و ۷۳۲ هزار نفر بود.
آمار رو با خنده اعلام کردن ۳۰ میلیون نفر رای دادن.
توی وزارت کشور گفتن که اینطور نمیشه پس گفتن ۲۲ میلیون و ۴۰۰ هزار نفر رای دادن و ۲۰ میلیون و ۴۰۰ هزار نفر به جمهوری اسلامی بله گفتن.
اینو حساب کنید دیگه از کل ۱۸ میلیون نفر واجد شرایط مخالف بود مریض بود زندانی بود و.... از اینجا بود که من راهمو از اینا جدا کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69766" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69765">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69765" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69765" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69764">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq57fTCI9PtRwXeFcbJg6sebdrucmbgDSjFhZItpblsP7eCw6X8uWM9MXWj6vM26cRjmebMUwTDcPKwJPhiDCIUx6a2XhnE-Ors65Eu7MWZwAKVT2ssn3r_s1-0GakFKdFCydjK1KwXqFYlNTxXkXbT_W743Qf37tccxc3ygqo77ApyCcaorn-E8PQj5tJB9LGkpvzqOaIDliqj5FXdyaZ3YEZpz9WtqYch02aoA20NI4BY0t6og181Y7PC4wGdSheXCKYkaSbAqbVEHuyN5pMfsgUTO1wOybRKCVLot_HVrdGR91z4kL2Db1fsa8pGbWO7nFZgwm-YXdQa9fMr9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a17
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69764" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69763">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=m-MsbHBVYA2baoG1PJTTSENuQv5JjaQ5P-dRCXfQaaegJWWj6ozZC6H-0Q5sWr0L_P7VdzoST0fNcywe11Z9I3nhaSxr1JQCdTqtgBSJcumxbHQXlCn--VF3QYs9t6uScaZhmmtGHYgpIOqcoeigOOdofa99OBNUaH9yUfsaDgytaVUy4TRyTSx0knea1hC15nXqpd5ekNdfDuw5swv0ghEK77jpOjPTUfTtt65qbigM-cy8NY0A08O0YwUkHbLFAxXKQpZTmE9Wl48LWgwjDcUWlsKhoRXKSNfpsXyOzWRGB3gJJTAbjm0q86qQpYzric3VheLuScblDaEYaMywKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=m-MsbHBVYA2baoG1PJTTSENuQv5JjaQ5P-dRCXfQaaegJWWj6ozZC6H-0Q5sWr0L_P7VdzoST0fNcywe11Z9I3nhaSxr1JQCdTqtgBSJcumxbHQXlCn--VF3QYs9t6uScaZhmmtGHYgpIOqcoeigOOdofa99OBNUaH9yUfsaDgytaVUy4TRyTSx0knea1hC15nXqpd5ekNdfDuw5swv0ghEK77jpOjPTUfTtt65qbigM-cy8NY0A08O0YwUkHbLFAxXKQpZTmE9Wl48LWgwjDcUWlsKhoRXKSNfpsXyOzWRGB3gJJTAbjm0q86qQpYzric3VheLuScblDaEYaMywKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
سربازان روس با تفنگ موفق شدند پهباد اوکراینی رو سرنگون کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69763" target="_blank">📅 01:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69762">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده  ویدیوی قتل که قلبشو از سینش…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69762" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdYZ0cjkFY3VF0wI2VBACEKra0a9YrJopHPvIDrCdDnMz028zvCpfewxw3IMhA7M6U85fAOyRdOgMhhEaNdiAM2x2RhO821Hv3z9p9eRmzRMt16iJVzGLKNGW4DC7e3i0YSOrp6VDEjbJOo9Dacnz8Zu-0N8S4GaPr6CwzkT8owvW-vF3_gi4JUAYzJg-ruE6v9v3aJ9ObSpAuTWJ-PyfxgUC4-CcGxzIJkdwjS5ydzRqszbLHarXncZba8Rr9zCkaCO4GRb-4OmwIZHnIUtOPXNRDfco4vdZAanmMuo-EoaqEFUDOqDKxM8YylIHE-fBfkGBbPGgsitxlBDbhuc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=OXTXV8Tn_pZksKwb9MemOn4-fdsLGwcmyCbAOBhXXpMivxNeJY9JsNI5mqjwpgUi1Gy_FFVfEM3Kcph7VGm8V_ltJyTvM4lhMWgkBTdJo9CCqesfyi-Xkp52_fsxw-QZoDLE4qs79kreG_SSGwSn4OK2iMxGSNFQp-5SV0kKa0duxlBHuVGBz7kA_KZNrvi1bCYYE7nidKyM3mAizMbbiAHKp7IbDlFQd_xTE4L9XqflasUNjqmiDW2mUZcIlnwr5rW0ez2xr6LNRKjrIDxJWms0t4MjtZNimk5hFRJzBlpU-VTV-Cm-ldldzvp0yO7C61fRM-9BJ4KHhxCVmVHrkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=OXTXV8Tn_pZksKwb9MemOn4-fdsLGwcmyCbAOBhXXpMivxNeJY9JsNI5mqjwpgUi1Gy_FFVfEM3Kcph7VGm8V_ltJyTvM4lhMWgkBTdJo9CCqesfyi-Xkp52_fsxw-QZoDLE4qs79kreG_SSGwSn4OK2iMxGSNFQp-5SV0kKa0duxlBHuVGBz7kA_KZNrvi1bCYYE7nidKyM3mAizMbbiAHKp7IbDlFQd_xTE4L9XqflasUNjqmiDW2mUZcIlnwr5rW0ez2xr6LNRKjrIDxJWms0t4MjtZNimk5hFRJzBlpU-VTV-Cm-ldldzvp0yO7C61fRM-9BJ4KHhxCVmVHrkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69760" target="_blank">📅 00:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69758">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=ZHPEpD4NzGri8v5Vn1QIaSon0M4C-RPXLoqx-PqcNND-IOryB8o8Ohne7u1VHuqokM351q5HwPGxC7F47ziA5DVnOJVjEI6TEhnbuU2Ps1F0FlK7V8zfk4LGHPdE9t3-v44yUPlEL-_qK4poGXOzxdeOFwFfxCeGioBpktUHiT2Q73dhkN47vsTkmQLjJoAYPbGT6u-WEnBa08qsqsOSVwKaTZB_bL1OCl8j2tIWDBjtgCotaCAyZxUZKkhWQe8xb6yymMk940OA4KvYg52wStHL3uUHKT-wSHPLkZ4xJtI96ub9xNg_4EG3DTcUuyMYwhAMZ6ctsro0PCt-gt2V7yGc2kIISXpZDV-If8fPwJ8hvDqSKx_M94syKv-xwxfkfWshc08Pmg3rhAeXRfvIUIkGrAE-dCObkp_-24NsgLJQHX_9ix_bYS4fPq672TBbqSA8brvhvyhbCgl0QdKLKJ75rO5ntxvCYniwWjIaM9Oo2o1akZ5JN5ejJT6AHyxvvhI8IrkHiTNG8-wA2_sqIYcbO4JM1zUbCARMtELULQuCO-JepMCJ4jDSvdch1DA-5Fh9BDf4lPlW0FrqU3nTylDUZNOMOyrFGJpGuVi5Qw0XZbaOsiCiNRSDlwo-XYsSI7u59LoEVIaeCWHxLb26friHaeCMAuicBt0bC9wwIGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=ZHPEpD4NzGri8v5Vn1QIaSon0M4C-RPXLoqx-PqcNND-IOryB8o8Ohne7u1VHuqokM351q5HwPGxC7F47ziA5DVnOJVjEI6TEhnbuU2Ps1F0FlK7V8zfk4LGHPdE9t3-v44yUPlEL-_qK4poGXOzxdeOFwFfxCeGioBpktUHiT2Q73dhkN47vsTkmQLjJoAYPbGT6u-WEnBa08qsqsOSVwKaTZB_bL1OCl8j2tIWDBjtgCotaCAyZxUZKkhWQe8xb6yymMk940OA4KvYg52wStHL3uUHKT-wSHPLkZ4xJtI96ub9xNg_4EG3DTcUuyMYwhAMZ6ctsro0PCt-gt2V7yGc2kIISXpZDV-If8fPwJ8hvDqSKx_M94syKv-xwxfkfWshc08Pmg3rhAeXRfvIUIkGrAE-dCObkp_-24NsgLJQHX_9ix_bYS4fPq672TBbqSA8brvhvyhbCgl0QdKLKJ75rO5ntxvCYniwWjIaM9Oo2o1akZ5JN5ejJT6AHyxvvhI8IrkHiTNG8-wA2_sqIYcbO4JM1zUbCARMtELULQuCO-JepMCJ4jDSvdch1DA-5Fh9BDf4lPlW0FrqU3nTylDUZNOMOyrFGJpGuVi5Qw0XZbaOsiCiNRSDlwo-XYsSI7u59LoEVIaeCWHxLb26friHaeCMAuicBt0bC9wwIGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو این مملکت اگه پول داشته باشی، حتی کمپ ترک اعتیاد هم می‌تونه شبیه هتل چندستاره باشه!
● بعضی کمپ‌های لاکچری خدماتی مثل:
🍽️
غذای رستورانی
🏊
استخر، سونا و جکوزی
🎱
بیلیارد و پلی‌استیشن
👨‍⚕️
پزشک عمومی و روانشناس
📱
موبایل و لپ‌تاپ آزاد
🛏️
اتاق‌های VIP
ارائه میدن؛جایی که دیگه از کمپ های معمولی خیلی فاصله گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69758" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-H8IJ-G0ALVCAIfx5r-xaqLacsWxGEMG00DQkSQks_GxVVptPrrELCKxHhabRinrnhnwmYjiHRHbcVjZo2YP6lOZw-lSAWM7E_OXfcFesXM2crEcU4UzkmHL2do4vK2-XS_SFZ8V-c90Yf2-WLPjfDYJstVrMohK-uDQtNGEztNGcD24xp3gRjaiOtUGw3Cx9bSl6abpB3JGxKYgf8yHTlNXZ4JxE51G_cDE5TrsgHbQMOht6Ww17H6_GL70v3HYcLOV9YrciWIQskMDMBWdkDcGpHqg9A9I5j2AWFPXAuKBj8X6qq8P7ZgIT9LpVw4nunUdX0GjaVm5biVxcvKrg3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-H8IJ-G0ALVCAIfx5r-xaqLacsWxGEMG00DQkSQks_GxVVptPrrELCKxHhabRinrnhnwmYjiHRHbcVjZo2YP6lOZw-lSAWM7E_OXfcFesXM2crEcU4UzkmHL2do4vK2-XS_SFZ8V-c90Yf2-WLPjfDYJstVrMohK-uDQtNGEztNGcD24xp3gRjaiOtUGw3Cx9bSl6abpB3JGxKYgf8yHTlNXZ4JxE51G_cDE5TrsgHbQMOht6Ww17H6_GL70v3HYcLOV9YrciWIQskMDMBWdkDcGpHqg9A9I5j2AWFPXAuKBj8X6qq8P7ZgIT9LpVw4nunUdX0GjaVm5biVxcvKrg3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی به هدف قرار دادن تدارکات اوکراین ادامه می‌دهند و یک لوکوموتیو دیگر را در نزدیکی ایستگاه راه‌آهن «لوزووا» در استان خارکیف منهدم کردند؛
منطقه‌ای که یک کانون کلیدی برای کی‌یف جهت انتقال تجهیزات نظامی و نیروهای کمکی به سمت دونباس محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69757" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=QEl1XQOY6hIpzL5dsftGRrr8s_U4I_-vwER-_RwJ3XVXjxM7m-xn6A3N2o5-2cF41mo4KxfqP5a-m9monbsbjjOzNRy22UyXrUrvOVp5gK_-HYOYSIL6RmVFmH3990M5jgbY98qXGI3WYdSpDOf272NQwkFE7SWuL110Es0GaVcjJIk8UoA5PLrqoMZX04ra9pZeY2JbePpT29Gi8kClC_CduGtmcdd1BF2Hk7_5l2MOFXnY1IQ3bCItYV8ClV-nQUs4jgRy8PHoGhRtQvZuC6nfHJEZBeOyo1hBQALvXEW7xXPI4ipEpSlg8reOCv-50Iylkt3G9QVzEeWgSV4OCX52g6uDmqXstTDwyy__EGm9iCumcazIh9Pj0nqMD6jFBJcvC7OVgWWMNIr85QRrcwLwCN8Ca72d1hbcfbkyyWRz1u4KOioblwaNP1fE3SZi9qB7Q6eraD_ZLwroS-u9j_IpRn5XEqDwj3hCKFW3pJCLuUWkDeFKEqRJjy1wHlfC1VacI-OKXLwQcRd27KU0qc9yGCyDHPyNkxspQ-giS68tNU7PippOH47QTKeX3A9Fz-WYRh1qu0hQ_Zlg_OhuqRrzoGFqSVQ6PfELMc6l5w5D9oTNTfmzsfu1m_lDC_yEmHZRML5AG6GP3sIP4TYAmYFhuAaz02SUVs-6gFEryFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=QEl1XQOY6hIpzL5dsftGRrr8s_U4I_-vwER-_RwJ3XVXjxM7m-xn6A3N2o5-2cF41mo4KxfqP5a-m9monbsbjjOzNRy22UyXrUrvOVp5gK_-HYOYSIL6RmVFmH3990M5jgbY98qXGI3WYdSpDOf272NQwkFE7SWuL110Es0GaVcjJIk8UoA5PLrqoMZX04ra9pZeY2JbePpT29Gi8kClC_CduGtmcdd1BF2Hk7_5l2MOFXnY1IQ3bCItYV8ClV-nQUs4jgRy8PHoGhRtQvZuC6nfHJEZBeOyo1hBQALvXEW7xXPI4ipEpSlg8reOCv-50Iylkt3G9QVzEeWgSV4OCX52g6uDmqXstTDwyy__EGm9iCumcazIh9Pj0nqMD6jFBJcvC7OVgWWMNIr85QRrcwLwCN8Ca72d1hbcfbkyyWRz1u4KOioblwaNP1fE3SZi9qB7Q6eraD_ZLwroS-u9j_IpRn5XEqDwj3hCKFW3pJCLuUWkDeFKEqRJjy1wHlfC1VacI-OKXLwQcRd27KU0qc9yGCyDHPyNkxspQ-giS68tNU7PippOH47QTKeX3A9Fz-WYRh1qu0hQ_Zlg_OhuqRrzoGFqSVQ6PfELMc6l5w5D9oTNTfmzsfu1m_lDC_yEmHZRML5AG6GP3sIP4TYAmYFhuAaz02SUVs-6gFEryFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از مردم پرسیدن "چه فکریه که نمیذاره شب‌ها بخوابین؟"جواب‌هایی که دادن جالب و دردناک بود؛
میدونم پول دار شدن زمان‌بره ، ولی خب به این فکر میکنم که مامانم داره پیر میشه...
من چی کم داشتم که بهم خیانت کرد؟
برادرم که فوت شده، هنوز مراقبمه یا نه؟ دوسم داره یا اینکه واقعا ولم کرده؟
اینکه الان من بهش دارم فکر میکنم، اون داره به کی فکر میکنه؟
یه دختری هست که میخوام خوشبختش کنم، امیدوارم لیاقتشو داشته باشم..
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69756" target="_blank">📅 22:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⏺
ژنرال برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده، در اسرائیل فرود آمد تا جلساتی را با ژنرال زمیر، رئیس ستاد، و مقامات ارشد نظامی اسرائیل برگزار کند. این مقام آمریکایی پس از برگزاری جلساتی در بحرین و امارات متحده عربی، به اسرائیل سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69755" target="_blank">📅 21:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=H9Zm9KTeJ0rg9_L-tBTjX94tD0XbU42NAjfxhGy0th5zgT-VPTmNZk6X5ZNmXP40ppiAEdCB9RAXH57LubnOxDczs443O_Rx32jGeqTCH0VFPrAE9difSGEe-7R3ZmXGYunpg6rH3YxYpnX_cD9FhN8oFmdhEaGEjOGs2vxJg2xJN31PGQzT3Bh92fHbAhUotNpebX3inNwgj03Xf7v-3NtFWlLpvZTgAoKoMNWYOJD44KBp7qUmwMgo-u1htrcS9-sTjxObAcHdjldQrmRyh0VljZ37GjDPOiORzXhIQoECoRyfnpUB7B77l5i3cu0HeuJ4b-kylLA50b49XVvuU6ebPAjrfjTR6vS0_yzMaxrqxYTCSApjGkpIr6rQUd-aV6R1i_V5T7vP7ISnoK2CcDBoHxMeQfPngqwqeeMNZn9183iFja8hsjssG0LvblAkWfCUsjxfdtiWwCnY2cH4g5SfWMW5TE7PPIBkfkLSBCBrvSzMJ2AIditgoPovjm5dtKvE4Erle7Mw73xoab-vyTbV9LLw9I3x3G4aDulSZsMbeZN8sOscebyGpx1vDQG9EUoFCbaj6iwrfjEMFzMn9vabChBNTKP0aSKFYkXJCG28RFZhJA8o-8L6RPoDZocFV-ZTk9GYw28i4i-6i-dWUw21ly8uzVi8BMZGsytEgt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=H9Zm9KTeJ0rg9_L-tBTjX94tD0XbU42NAjfxhGy0th5zgT-VPTmNZk6X5ZNmXP40ppiAEdCB9RAXH57LubnOxDczs443O_Rx32jGeqTCH0VFPrAE9difSGEe-7R3ZmXGYunpg6rH3YxYpnX_cD9FhN8oFmdhEaGEjOGs2vxJg2xJN31PGQzT3Bh92fHbAhUotNpebX3inNwgj03Xf7v-3NtFWlLpvZTgAoKoMNWYOJD44KBp7qUmwMgo-u1htrcS9-sTjxObAcHdjldQrmRyh0VljZ37GjDPOiORzXhIQoECoRyfnpUB7B77l5i3cu0HeuJ4b-kylLA50b49XVvuU6ebPAjrfjTR6vS0_yzMaxrqxYTCSApjGkpIr6rQUd-aV6R1i_V5T7vP7ISnoK2CcDBoHxMeQfPngqwqeeMNZn9183iFja8hsjssG0LvblAkWfCUsjxfdtiWwCnY2cH4g5SfWMW5TE7PPIBkfkLSBCBrvSzMJ2AIditgoPovjm5dtKvE4Erle7Mw73xoab-vyTbV9LLw9I3x3G4aDulSZsMbeZN8sOscebyGpx1vDQG9EUoFCbaj6iwrfjEMFzMn9vabChBNTKP0aSKFYkXJCG28RFZhJA8o-8L6RPoDZocFV-ZTk9GYw28i4i-6i-dWUw21ly8uzVi8BMZGsytEgt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
شاهنشاه آریامهر: اون روز دیگه من نیستم ولی حقیقت هست
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69754" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX1SwOOELhSnWlmFpauu3sl856UcfZPiXswv5mviqKj1HjMsmEPsNK9ZBa4OfwCautf8L045L2pXPsyd1AmYEBnVKanVu471ZDZ_b88DrFYQOj-Oo0BmG23Spgj0ksU24DmWmzraydDI_SQBHiwqFAhdc0k-H4a1oG2kvTV_EtjOx7yBHoFB8NdM43-6zmZ4KrJ4jsgNRbv1KntyTlXYZ-MlOisIehSy8Pv6rPUiOl5qrK3y4RRmCEOgdVyS0q4G5TKpdqY3KmalJ5zIg64GZr799sEDiSH4lxDabPqpQOr_t_RgVg7hrM_h5aexJAfW32kwtXO0VUM7IZpl17jaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کانال ۱۳ اسرائیل:
اسرائیل خود را برای احتمال اقدام یک‌جانبه علیه ایران آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69753" target="_blank">📅 20:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69752">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=nr2h1bPU9oAxIG0QmXbUFZ-w1gJgF7OavOQMHyhEetoQTs7U5_s_kgJ4gQTPMVG6gPU_D53TzZY-8snv0bfEdOSYxvvaXMopXUur-NGmH6tF-T_s2NlBjBV5V9FdkmGA_lpPxx3pQ51KouwMzSE-8dTRdFbimIwKtYm2Be8GeYsUGutvF2mZu8aC50Gi-UUFARcBItq2h0ci-qAgwlEp58cxXKUAAOPiTVhn0l7CZHNWiwLSXAbYQRWrGta9GC6nh06lS3OktEuMqKORbnsqT662khNGtMvVs3p559EdXzvjU7k9b1mI9SRQlFY6_wZrT4bKPlKu3QyEBwvSKgWvqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=nr2h1bPU9oAxIG0QmXbUFZ-w1gJgF7OavOQMHyhEetoQTs7U5_s_kgJ4gQTPMVG6gPU_D53TzZY-8snv0bfEdOSYxvvaXMopXUur-NGmH6tF-T_s2NlBjBV5V9FdkmGA_lpPxx3pQ51KouwMzSE-8dTRdFbimIwKtYm2Be8GeYsUGutvF2mZu8aC50Gi-UUFARcBItq2h0ci-qAgwlEp58cxXKUAAOPiTVhn0l7CZHNWiwLSXAbYQRWrGta9GC6nh06lS3OktEuMqKORbnsqT662khNGtMvVs3p559EdXzvjU7k9b1mI9SRQlFY6_wZrT4bKPlKu3QyEBwvSKgWvqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خوایم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69752" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=m9vZmpqotg3s0hGDcobyQhPVDLU4qOxdCPtcshruhfjCWw3R1vwepe-d7XO8MT9zknv-1l7gSL0V8wLIzFsmkUAp8fsKnML-FBgOM8IK2TadslNimAqKBzuCayJ5Uu4R_jdNLkzAH2NFJ2gACgPc8iXnyzBvsAPotlz5mgbONXaZXK_lFvzfyuNhFkbdcaZSwVIy-ZKT8bh2Pm9x9SCEdwnVvoSNqlOy7HR8zinv4MEz6t1UxJ0FpzvpekeNo2mPN5Td_FD7k-ZrAW37YpRXNB4kQ6JrJsnp53NPpYqTR6-Z6XHOWIlWXVKMLcalEFk6dRokjARSgdoZQ4h2MkqLZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=m9vZmpqotg3s0hGDcobyQhPVDLU4qOxdCPtcshruhfjCWw3R1vwepe-d7XO8MT9zknv-1l7gSL0V8wLIzFsmkUAp8fsKnML-FBgOM8IK2TadslNimAqKBzuCayJ5Uu4R_jdNLkzAH2NFJ2gACgPc8iXnyzBvsAPotlz5mgbONXaZXK_lFvzfyuNhFkbdcaZSwVIy-ZKT8bh2Pm9x9SCEdwnVvoSNqlOy7HR8zinv4MEz6t1UxJ0FpzvpekeNo2mPN5Td_FD7k-ZrAW37YpRXNB4kQ6JrJsnp53NPpYqTR6-Z6XHOWIlWXVKMLcalEFk6dRokjARSgdoZQ4h2MkqLZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
معاون رئیس جمهور آمریکا آیت‌الله جی‌دی ونس:
در کنفرانسی، لحظه‌ای پیش آمد که من و یکی از دوستانم داشتیم درباره مسیحیت و مذهب کاتولیک صحبت می‌کردیم.
درست در همان حینِ گفتگو، لیوانی از روی دیوار پایین افتاد.
می‌دانید، فکر می‌کنم یک فرد خداناباور (آتئیست) احتمالاً آن را این‌طور نادیده می‌گرفت که: «خب، چه اهمیتی دارد؟ لیوانی از روی دیوار افتاده است.»
اما در آن لحظه، احساس کردم که گویی خداوند سعی دارد پیامی برایم بفرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69751" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=NwS-O2HE-3cEVPM_RpfljAfR5j9PnWz55IuIJV0UORcUD9TlhBXL_cSHIajC4VeyDcI50pSBfDXwsZJ_owbarLPmJb6rJk59v78Ee5cRFuDFYtp9bgqVyieMX0Nk01MoRaZw-8gE-0ekFkPwyFNFCXzCCL9vrao93yKiogTneCS5wmAWqctVNr3u9KNDOCyNY2IusnmYN06Ws6FOEiL1jsgG2EQPBUfsRX8oZCTC4psJVc4Zx3cuWDL4XaaUbdTHz2Ea-MiFNtiIO2DHbMLALYC_LkwPm4jWdchRu5kTdkAftGM423WW4pxqOadYlqC6LVS7KXNziuC6C0A7cAYXxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=NwS-O2HE-3cEVPM_RpfljAfR5j9PnWz55IuIJV0UORcUD9TlhBXL_cSHIajC4VeyDcI50pSBfDXwsZJ_owbarLPmJb6rJk59v78Ee5cRFuDFYtp9bgqVyieMX0Nk01MoRaZw-8gE-0ekFkPwyFNFCXzCCL9vrao93yKiogTneCS5wmAWqctVNr3u9KNDOCyNY2IusnmYN06Ws6FOEiL1jsgG2EQPBUfsRX8oZCTC4psJVc4Zx3cuWDL4XaaUbdTHz2Ea-MiFNtiIO2DHbMLALYC_LkwPm4jWdchRu5kTdkAftGM423WW4pxqOadYlqC6LVS7KXNziuC6C0A7cAYXxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما تصاویر مربوط به هواگرهای آمریکایی و اسرائیلی که توسط سپاه منهدم شدن رو منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69750" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69749" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR2Kc1kgp_Ehsz_pbu_Vho495u9hiqCaudYzlAJr3-8i35_NmU7IqlxQ-P33louXEWhvCWcclWZwaql28j_6e_tTKgqGUjyu2I8MAobZQ24m5jp4UQeeECVDD6oyHT1G8o7ALOtN2aGK1nq9ZLnl6XgCTmcdMp_N9Gvys4sLVrk1mXUX0fXXinWHKSoaXgC5pqc6LVRVdSlLnwLXUcZ7yTPDjD9oCwyXq6zUCD2BZjX2Wx7KamfhAyKEr4vTA5gxP4DXLZBpZKIqixQ6AibOA6rbuOLlG89v_KBUdzQqmjo3EnE-xYRucWo9aamoU6l2DGa_ZN1h4bd-oydIqUsZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69748" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jED358RGhhUCcYiPC-qdKQBnkox8OSvAx_1-AkvpjCG7j_01gYdLwiAC-xvSbsVRtEYFUhNxhKCuc4jy4LGjZ6ud-Y-yF67Ku4oSVJro_Ymvy1--a-CPs-FluYmzoJ4nUTweKbH_80QXxjiBulXL3oK38Ok8Z31gl64n_PFRVVesXbjAxHpLKo-ziDMU-x6AaITHVJq6gONRIEyPel9h9eB9oLwYhlp_GEdRPvaTlwD9cFT48USU87yDUxmELDXVueCxHnnnMMYKkLhNgiWZ4sFNXwSymGlCn17oui-Kfr3gwWFbTivm3foh6RrX0RA8EuKzifuJDx5ZBkLE_l037A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
بیانیه دبیرخانه شورای عالی امنیت ملی:
🔴
اگر ایالات متحده رفتار خود را اصلاح نکند، تنگه هرمز باز نخواهد شد.
اصلاح رفتار به معنای موارد زیر است:
عدم تهدید ایران به هیچ شکلی و به هیچ زبانی، و عدم توهین به مقدسات مردم ایران.
پایان دادن به جنگ و تجاوز علیه ایران و متحدان آن در لبنان، فلسطین، یمن و عراق، برای همیشه.
رفع محاصره دریایی و عقب‌نشینی نیروهای نظامی دریایی و هوایی از اطراف ایران.
پرداخت کامل غرامت خسارات وارده از دو جنگ تجاوزکارانه علیه ایران.
رفع تحریم‌های ظالمانه و غیرقانونی اعمال شده بر مردم ایران.
آزادسازی بدون قید و شرط وجوه مسدود شده و ضبط شده متعلق به مردم ایران.
🔴
اینها مطالبات مردم ایران هستند که در طول ۱۶۰ روز حضور مستمر در میدان‌های جنگ و خیابان‌ها، فریاد زده‌اند.
شورای عالی امنیت ملی هرگز عقب‌نشینی نخواهد کرد، نه در جنگ و نه در مذاکرات.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69747" target="_blank">📅 19:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK-9173oSAPB9QoO6nzHaGxG_PqvXxLlLdcOOYUlPEKBREWEOftpCJfj9dZxtmMhB-cf2ZtcgsxiDiE9-wYCLRdCiP_q_yzMSxviSW8Sp_i5BCZzXs8cCccGr54F-ENZ2mtQoTvol2yyr5kZnJFBG5k2Qdw17_qEeAnlhsHIAMVKxl8t7agF3xt67Ukn0I0arBxKXlqKI-Dp0y3zUfbgQ-klvFRDoRqZBnanayipv9S74An_f_Z-K_U92-BUDTlA8F1azlThQPX04-q3pKOlAvo3wvMpZfRm9ESS8zjsCaw8c-I0zln7uB9m6Qv3e5HMaHO_MLrm5aTxgbtj-fQ1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69746" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69744">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBu33wlHgcpf7PJq_f6V2mJLhkmOoHA4wK_mfKCqM7WMEI6FD0un-MeBlXow2xNSbrMJq1MSrOHKgix8VK3Js2zCij_L_BwzR_otXGqN3IjgpoUKNPT2zPEB4XPXXFnZxZUUfMCMp5stQWc_VYOu5o4lUSMGrc4ISOsRL8tvPan8ttx9iEham7jFzwDRJZ-Cbf200gjJBLyfYsPwkHnLdk3_etms6VskXMACg-kEU5i7PmPcCPKQCOFfZq-NQEvMpZK_AAflDSB4PIS1Kbubu86y0OYqaGqqlb0po-5_HrIBhHsBlRFTdXEV-DYvNumwon7DORveoH7kV6n00u1ZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز:
ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69744" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69743">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGsG8wfxEfFUitM7_TRbz8kYsCOvJaQonhCv4kGk-Gnf0bh8mfuxwmY0RAIgSN0BQkm6chH6Xzsh5dFmACTxHplgUgnvNRNZdo7mdjDYaAV6_NciU2SOGvPZL-R8sqNFOXWRMijlAOku7VldiePdO48oIUvqz4y2vb5bbo1yH6ixzyy4DtZgmsOApZwIhPfdvtoAtyVyzyEGWd-SGwHa6UBfl-wWgIixg9TkfzfMhIZMGsFYWyxva_gMI2TxyI187LfJ_R6RRyDXl0oPtrWvQjriVIGRi3uEFFXM5E8u_WZLt_KvYVczVBZjDYQZLbyT4-doedL-D9BhwwoHXD83Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان حمل و نقل دریایی بریتانیا (UKMTO):
گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.
یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش  خاموش شده است.
هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69743" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69742">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=fqY-bklbb1f1ZHUjP4SZ37gT4ak5UCKJ07zG2eJ22QEApIjxRyQzMp5wRKvkuqNhMW5Z4wnIZgvmbN-5V6z2Jc3NqwToHy_uHmzTexFv06pAM_1yUqRCwdPG6FLwMv9Sk0qadcr1RhDVZa8cCWIxbYZdi29mj-RNfas50wesFn4TZ_BF1YgxXmV7EUib-JlGdWeu9_jPMFLUtgx6WA9K9EXytkzle5r6CUGvee9AFtVIm2Dq6-D_xkhnNK4foQ1_37Ks1nWT-suSL_yUCB2DDHBGF8Yc4lOdiUy-2h4zNLL71KdHiqXpsb5QgAm1EwWFMWaTlRk8c94pZqkKyBZ6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=fqY-bklbb1f1ZHUjP4SZ37gT4ak5UCKJ07zG2eJ22QEApIjxRyQzMp5wRKvkuqNhMW5Z4wnIZgvmbN-5V6z2Jc3NqwToHy_uHmzTexFv06pAM_1yUqRCwdPG6FLwMv9Sk0qadcr1RhDVZa8cCWIxbYZdi29mj-RNfas50wesFn4TZ_BF1YgxXmV7EUib-JlGdWeu9_jPMFLUtgx6WA9K9EXytkzle5r6CUGvee9AFtVIm2Dq6-D_xkhnNK4foQ1_37Ks1nWT-suSL_yUCB2DDHBGF8Yc4lOdiUy-2h4zNLL71KdHiqXpsb5QgAm1EwWFMWaTlRk8c94pZqkKyBZ6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبتای یه وکیل مرد:
توی تمام این سال‌ها به این نتیجه رسیدم که نود، برای پسرا معجزه می‌کنه.
پسرا عاشق اینن پارتنرشون بهشون نود بده، اصلا هم براشون مهم نیست کجان، سرکار، خونه و...
من خودم یه بار وسط دادگاه بودم و دوس دخترم برام نود فرستاد، منم گفتم این واقعا محشره، مرسی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69742" target="_blank">📅 18:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69740">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t8QFTrpmQm7nNzv5j1_6ItH2CvID-cusmNrXfiSo_j6gaA-2IH7VbX2gq5W2f2nCOiQH9az2IMIF8pVd1a-Q4b0DnKyRPGrvt4Y1fP8Nv2buHaxERJrK93ycb5_72sCKIRDZ2gttP64jM9yinnY9V3gAhAOKjw3YhfclC5brsfVzr1VqUO5il_kQk9OGu77nJrWxyONNkFGRjg2ikVFwmry1GdS8wC4qd6JNnFLOKljSIYbNF5Wt4wtmOJaVkgtlmOhUzDVV0T1ZerZ54TWU47j0s4b2FJliLuNsF-T9m2fwP5l_FrN_DC9EjmAjJsO0bCVvJyhwmhkySvHHBfL_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=ZUb5oXrDmhdYj4iyQAcmJlPhYVVwl78oBknl_6Gv9ES_NTFF8iUCyKMgPsD73ZDHLKpriRHPPvXBFpcpFEseW9XprU0wSNFWb7065awAG_mlH5vucYPc5sthfA6bl3i4Q6Gb2Xg8SUKugSE8VNklKiDxf9_r-DItjOSzUA7H7OT93iQet9OWF6d4hKZ2qAiTf_Esvsw8TtOOEojhhd2jcwyhhcHM0fLK9Xd_WfcG7R_qU4znFj0mfG1wgW9rbosRE-3CAgOZBk1wS-1_ZI6gBN1yVFcTvvEc3bVzMpY4-LMqHfiqIFWwdsKj0_wZBiDNBUMPu6X5JttZUovIFyodog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=ZUb5oXrDmhdYj4iyQAcmJlPhYVVwl78oBknl_6Gv9ES_NTFF8iUCyKMgPsD73ZDHLKpriRHPPvXBFpcpFEseW9XprU0wSNFWb7065awAG_mlH5vucYPc5sthfA6bl3i4Q6Gb2Xg8SUKugSE8VNklKiDxf9_r-DItjOSzUA7H7OT93iQet9OWF6d4hKZ2qAiTf_Esvsw8TtOOEojhhd2jcwyhhcHM0fLK9Xd_WfcG7R_qU4znFj0mfG1wgW9rbosRE-3CAgOZBk1wS-1_ZI6gBN1yVFcTvvEc3bVzMpY4-LMqHfiqIFWwdsKj0_wZBiDNBUMPu6X5JttZUovIFyodog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به دو پالایشگاه نفت در روسیه
پهپادهای اوکراینی بار دیگر پالایشگاه نفت سیزران در استان سامارا را هدف قرار دادند که در پی آن، آتش‌سوزی گسترده‌ای در این پالایشگاه رخ داد.
در حمله‌ای جداگانه نیز پهپادهای اوکراینی به پالایشگاه نفت ایلسکی در منطقه کراسنودار حمله کردند که باعث وقوع آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69740" target="_blank">📅 17:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69739">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=bJsCE8oBfdlQO4OYu37xAHmmwJn3gbLcr2HpOCVsuGqiDnFneiiSPnmPLDJI39DMhwwe2F2_KFas3rMJBqxEGdIS-2zbmRsqWcR28BfjDYLFMxQVihRmHlEhsYCcknFlpg5rnG6ETu71Ti0nKZZBsg2Ty9GpifJv7JRDYwTAYhepVSHxz-1Vuj3z4Tcz1DYreEM-SxwGrsMAHp9TfFrYz1xqyJDoDdO9n_06zWqVrnS_5gytTdiiDxjnu23Kqa5ZCEvTmerBJlEVijmOqDHPgxqLBWflLaA_SV4TgiOXUx2i29fFy8dCGxvSBIhcEtqwsIyQ4_e2rYZ0AgtfjDwIwxc3OD5HtJvkEvL5HfafZcf1Gv7TTE5heLa3pvrLBgGG35OlGw44g5H2WJV_9Dwqer7rDSHtITDFGeUlZSJAdrTeQA6yMFL7YYdFtSOK37xEjkMyQQXTL6QVxLJOgAq0X8lBdy1GpzFMsLn-u9OORTxltQCPTU-GQLlNLFRjwx1rPpRxwCsmO-yV7G4FjhymyYc0zA6ZthQ-ZRYl6fXGoXQrXEKkVqQCZEfbB_cN1F9G7f8QNCBPiC6h5gNLSaEAyEmckg41U0au5Akh4Wyjfva9uqMhItOMD_w-FA-HXy_ypTdim28WRjpGBUTLYEx8EZDivv6zLrnqlqULjDq2Q9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=bJsCE8oBfdlQO4OYu37xAHmmwJn3gbLcr2HpOCVsuGqiDnFneiiSPnmPLDJI39DMhwwe2F2_KFas3rMJBqxEGdIS-2zbmRsqWcR28BfjDYLFMxQVihRmHlEhsYCcknFlpg5rnG6ETu71Ti0nKZZBsg2Ty9GpifJv7JRDYwTAYhepVSHxz-1Vuj3z4Tcz1DYreEM-SxwGrsMAHp9TfFrYz1xqyJDoDdO9n_06zWqVrnS_5gytTdiiDxjnu23Kqa5ZCEvTmerBJlEVijmOqDHPgxqLBWflLaA_SV4TgiOXUx2i29fFy8dCGxvSBIhcEtqwsIyQ4_e2rYZ0AgtfjDwIwxc3OD5HtJvkEvL5HfafZcf1Gv7TTE5heLa3pvrLBgGG35OlGw44g5H2WJV_9Dwqer7rDSHtITDFGeUlZSJAdrTeQA6yMFL7YYdFtSOK37xEjkMyQQXTL6QVxLJOgAq0X8lBdy1GpzFMsLn-u9OORTxltQCPTU-GQLlNLFRjwx1rPpRxwCsmO-yV7G4FjhymyYc0zA6ZthQ-ZRYl6fXGoXQrXEKkVqQCZEfbB_cN1F9G7f8QNCBPiC6h5gNLSaEAyEmckg41U0au5Akh4Wyjfva9uqMhItOMD_w-FA-HXy_ypTdim28WRjpGBUTLYEx8EZDivv6zLrnqlqULjDq2Q9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
تریلر اولین فیلم ساخته شده با هوش مصنوعی
!
فیلم Hell Grind
اولین فیلم بلند سینمایی است که تماماً و بدون دخالت ابزارهای دیگر توسط هوش مصنوعی ساخته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69739" target="_blank">📅 17:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69738">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPZFau6HFcQJI5L15L3k-rehEY7J5HfWq10ksAeTX7jF33Xxly06o_7TMWx6WFUkPQa4melhm18EuC7TzCZGPWSsmsSUIyy5WDEDa824hb4_kJek4hMUc6a_EXeJK-W9Ni0_6J4N0hMVgTBVxdhbBN_K_z4KwW0YEWaoZMKOu7_nEG0SglHq8QR3jBSQJcnkCwl6bzQdjHwq-YxoHIvl3VO1-f1NwkVcayyi-vhCQ2AsVl3ULI6QqEeNy0Szrj7domBDAzynok5WYpg-5mFb2j_0G3g5cI8VmZRYAZHztiljrfpvxOZR2ho9eXN9Z9UdRc4htkb_7I67kCZ3rs4cTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇦🇪
طبق گزارش الجزیره، ایران امروز صبح به یک تانکر نفتی دیگر متعلق به امارات متحده عربی حمله کرد.
این چهارمین تانکری است که متعلق به شرکت ملی نفت ابوظبی (ADNOC) است و تنها در این هفته مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69738" target="_blank">📅 16:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69737">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=dZkpycNRBDdTbFE4VkecMu3b9lC46rhzIbuOT73VIIqKNDE-F9BArXCw_F_K9MErfTk-aTri82VBsQPkEa6egQR1e6kpuQ9edr3cw5AKa6gfG2M6a4pM7OQhI2_xPPEtfbncSsHYQxe0wCcMvtDuH7QEDKYuLR1dMVdfsfaXgU6UArx-yhaqZDsmi2XUz0lJkEymx9xracbudPKPXLJutA6tGOeJGLCC4H25OjJF60hGTVZ42eNvjwzslUTKUDaD3payo9tcJiLmHBIX4QPSzDLZIiNBE_slke2DEkODMJLzzTtQUR0-Lgfb2ZvqYRVFwP7huU-LRDBvdKfJZUeqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=dZkpycNRBDdTbFE4VkecMu3b9lC46rhzIbuOT73VIIqKNDE-F9BArXCw_F_K9MErfTk-aTri82VBsQPkEa6egQR1e6kpuQ9edr3cw5AKa6gfG2M6a4pM7OQhI2_xPPEtfbncSsHYQxe0wCcMvtDuH7QEDKYuLR1dMVdfsfaXgU6UArx-yhaqZDsmi2XUz0lJkEymx9xracbudPKPXLJutA6tGOeJGLCC4H25OjJF60hGTVZ42eNvjwzslUTKUDaD3payo9tcJiLmHBIX4QPSzDLZIiNBE_slke2DEkODMJLzzTtQUR0-Lgfb2ZvqYRVFwP7huU-LRDBvdKfJZUeqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ظریف درباره سهم ایران از دریای خزر:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69737" target="_blank">📅 16:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69736">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=oLRO0X2_hP_H31hcC3TVsHiwvDtDEJdXSPg84J_Xbqi2g97xPddtFjdMeJ9oR4k32GF_wSt7kWLV4QrqnGlhcQoh6HB_jnX8-xAlCNceFWyessux1wZbI1IcgrT2QlyymqZgtngvXCPKfmLoDnTPZN3jl5j-BfT88lpX7NP7chy-88nTnKL0QUFEYq2IEOjqejyhdpH8oT9ExYUcYv8hCauCaFj1XtTLRoV6juPxVPxNBZK9bFlf4NT8t2mYpR7VVj_Ioa7HLaDUeEtgh4KiYoEshKjgjoYQzLWcbXgbeK0XxN0_eyiAFOMOXu7qXB6lyGdYJhxec8psixOllIrr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=oLRO0X2_hP_H31hcC3TVsHiwvDtDEJdXSPg84J_Xbqi2g97xPddtFjdMeJ9oR4k32GF_wSt7kWLV4QrqnGlhcQoh6HB_jnX8-xAlCNceFWyessux1wZbI1IcgrT2QlyymqZgtngvXCPKfmLoDnTPZN3jl5j-BfT88lpX7NP7chy-88nTnKL0QUFEYq2IEOjqejyhdpH8oT9ExYUcYv8hCauCaFj1XtTLRoV6juPxVPxNBZK9bFlf4NT8t2mYpR7VVj_Ioa7HLaDUeEtgh4KiYoEshKjgjoYQzLWcbXgbeK0XxN0_eyiAFOMOXu7qXB6lyGdYJhxec8psixOllIrr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه سکانس از فیلمای قبل انقلاب و داستانِ شب جمعه
😂
اسم فیلم: لج و لجبازی
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69736" target="_blank">📅 15:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69735">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
🔴
⏺
‌وزارت خارجه جمهوری اسلامی : کنوانسیون خزر منافع ایران را از بین نمی‌برد
🇮🇷
معاون وزیر خارجه:
در پی تصمیم برخی کشورهای ساحلی، پای بیگانگان در حال باز شدن به منطقه خزر است.
تصویب کنوانسیون رژیم حقوقی دریای خزر به معنای از دست رفتن منافع ایران نیست.
این کنوانسیون حضور نیروهای مسلح کشورهای غیرساحلی در خزر را ممنوع می‌کند.
تعیین خط مبدأ و حدود بستر و زیر‌بستر ایران موضوعی جداگانه است و در این کنوانسیون تعیین تکلیف نشده است.
به گفته غریب‌آبادی، اجرایی شدن کنوانسیون می‌تواند چارچوب حقوقی و امنیتی خزر را تقویت کند
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69735" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69734">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی سپاه پاسداران:
بازگشایی تنگه هرمز تابع سازوکارها و شرایط تعیین‌شده توسط جمهوری اسلامی ایران است و ارتباطی با مذاکرات ایران و عمان ندارد.
بازگشایی آن منوط به پذیرش کامل شرایط ما از سوی ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69734" target="_blank">📅 14:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69733">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
قوه قضاییه:
آیت‌الله خرازی به دلیل حرف های کذب و دروغش تحت تعقیب قرار گرفت و براش تشکیل پرونده دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69733" target="_blank">📅 13:54 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
