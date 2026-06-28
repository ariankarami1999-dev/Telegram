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
<img src="https://cdn4.telesco.pe/file/BuIeljnvCH4Dy_OvHVaKkCoDYWF8q11ZPScvC-zfUvJTqlsv_gMava8bts3q_3ET_PYXygpT28Vrf7fFAyCMwi4vA-MnZWgQ8ZGtb0JWO32SFy-dkGpZUd5pYQ9esOWO12esdIqFud7RukC8159nidbUMSJ87X2O1xxOp-VPEDUB0_D6i1aNd2nOPnMNt8RmgqSiTkbkw-Wf0xx6mFpFUPF23gfV5eqlf_rJiKHNVEhJVUhG-fYlMpxSfo-BC1eB-dflg0TZ5NaZYg1OnU9c9UlkzsW_zaxNpqAesrbXac_j8DTocUQumjei0UWjapwh3QePS4EnAA4yVgewUDMv5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 334K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 17:50:05</div>
<hr>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ema4j1ooSJbESNM_v-R3SOvnQTapSpt_3BCQNrBNNSor8UkIBtiRJolT41GBgnsON0TqodGFkOayvuSsAyf4A15hbtKlmlWQ0pjQI5rLW2CmqBfK9SJhpD9L8I_VADLR6QSXeUF-0vL_ce29HgTC2eNUJyldulQfRyyhoGpL_TXyS7D6dAdbiyJenS2CfqXs_crIwraQMFUmk8cPPz364L6ZtZTkMWlNH3H4EG8jO4KfQB59zubBALDdfnBGuqRyrv1Wpjs0OthIBwE3akpKLkXD5_n-7WhGZMBrzF7ng7tAwJrKp5owvumkp4J-11zap3eZnFMhdvb6M8fpRvWZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSzGB67SdAGaRXEGZLiwF_ft94N_0_4RLYVzQSsm1PmsSncAnecT5BqcI3TZbiv6nOq-UMIhti29vfykaQCYg3XzQFsZx-35-J6DkggLpdaLG7lTHDE4JuIXmOp1BsCLbwMHup8EOFbNzUKlCOumwZDTf6auHjJHWZRmPMaOLQeMqPat585A8RjToyyWeNB1nbBWq7BtGXRQ7FQam62Vqf4cqPx1D1Hhv7-iDTfek4Aos2x19BHwxa6kh9P7rfpS2ye2b_4pHtelypt1bC4Jzcs1G-7da8_Xlky85ppJft5N2E-h3uKAt-bKVoMQYJODk3LPWqAGkNd60VU2qwZ5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwnOZ_m9JN_sIUuQI3fRuFgbifAaB-XF1laoAqvmT4DYfumxPW07DrTjpPPMUZTFYEQ96IsRd371DWkMUSmMQRA2FRtFKlKaz1jUY_E6Bk_SzUDZV43O65sX0o7s_43RHSYr4bAbFOAJ-TaA84Tqx7FLBuuukLayY0Qf25FevVzfRUmv8aOrMZ03UMfEcXoqIcim_z2vzupy3BbehCd2wWcPGUeeQBP5GmyaCQqEokEHVyYREAPpOG8bSEb1Efvt5gfmyMIGrxnz3E_wfirsp9wB0EjkvY8CUEWA-C53ufUmOEMDsf7ubwe9FlyTF_T0kUODrM-qOTK6aSGQRxUCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-kg2ncUVlUXg4K3XO-TmXPQPDBTMsz0Clae2KzqC0wCLWNUHotoz5shQmak2LsKIP09MIiSIR4ifYvT9TryXkJrJpqgqm1BZsamAdUFsbOWBUhqNrONsVRu9wqsR4nKDhLVZPIuwvYH5XtviYNLOW1S6qzQN3kqdiG-Q-I2xsX5JcqoruT45usGWB6fDMKGRUVvq_CrIYlFlTDfTRNeD36XGUQcDqhOwAZh64-ZTlLLtjv93D9cqjr91Rwo2Un3PHCpLr9Gryo__IBf3kcrNJ6tJk7_EH34ueqxSWvGlIz6_Gw42yD-59f_Ne-_EXUL7Em2DmP7E482sBH6_oZBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikL4Qk2tPCmLjTAhmx8rndSanhUkqXZ7hR3T0g0i2IOzGsGUmLWt6gKBvolHnBr2IXWYI-hYuDehZo4N0N0F8Ci0Uqj1bxqwEdauTAXh-q-ceEIJPwdrJdzfJDwaI594oPVUEXNmh_0GsfYHv3KQVHabUEm32upeTSilGWN2WCs9VprVAB0pZxm1ArOy5zG8tGfmd5yjLZPpuA9jiuGXa4yCv-J_Bweju4EMUyphtzdEH35CTChOAc0m-QiYwMdBi1_cEoLm38EPKl1SpLeDzwVs03h-gzG50QbmL4zH850YGTrODjstp9SJFm4qcqwy_rx933zELBCBOzIFNgimlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiJg4U_QPMfONezQ3RUv8UZpCSPinOVicvgNYvU0XgwlyrTU9OL1yEEPlvjHhn6I9tqHSQlv-GImk6Mn1F5CCXnplCSTV50fkp_Vl9clNdSyrG_DCcR6PJiorUAkC9suisyAPjqW8HYqMUtW52MQHb1hTxSz5YJUGFp0CRy-zx_-bxtSGuTkV4BJq7L32p2v6lZHVvHbZkt92m0uXmPehrkmFOGQmCnFrVyDESHgPogfd9XrKFr4NsR8mEMasWy_NM2g97FQwyxeocd6ygDLoDQ0dXkX0itxIU8M4GO_DO2kEq9pKR83CiwVL2vNwdOPwdVy9Hpj5sZxUisI-jkNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn07myubOlcHeRcSxL4WaTSG-JulvXyRXLlSD8aRXyGuQaA6KdrARfJrepKuptyuQUXcW0WidWG-0OpgklwIUUvlgZOFbTPkjoJPMlPnzgmmmdeAA4sCgRya9DAPF0VPH02gwXWAccQNYADoEuwbNNk984KNC4qJ4lwP0-ftF7Gpi8OMt1AdOiqACHFbqrQGbTrJth2EXY0E5elnjypwraHjFmBjBSvI3Oir65FCe9Is83fKvsHpmJPRd7O5-sKkAGg-HUQ9NeXHRAOtJvq9X_V_Oze_hP0QytYHQQwVhFiGJ4nWMlTc_eJYK23uaUcZFIu5e8mWTP_VsoI5paWhnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zc_qsw_1D0IM3Mmth-sZQHYF0ErK6OQYGyN77LwCyj2ATFHDwyjn17V4khRZk5xia0xrQ--jlSYXK_bAB8W8uJOmtpjIMIL0Z2e6ZOHEa2XyiaXFrAlenOvjf-h_MkaC0xYQfA00KWumLHXVQY0K47UURuHfrfXlwCxmIMQyFsaIlBFCzbUV51YbyAnP3JM7fMNUs1-zPiUXeXUW4VlKBgBDpDZzuWkgxacw4aph_D6L_TJd6Fc67X3cysYvvK3UXCDJRvTRLPk_54ggKRBtPUYHmiViwRiPL3oF-KMUXcVcfMDz1frSd4Ds4dlUgIloThMMLUkwgHIrIsBtkotf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zc_qsw_1D0IM3Mmth-sZQHYF0ErK6OQYGyN77LwCyj2ATFHDwyjn17V4khRZk5xia0xrQ--jlSYXK_bAB8W8uJOmtpjIMIL0Z2e6ZOHEa2XyiaXFrAlenOvjf-h_MkaC0xYQfA00KWumLHXVQY0K47UURuHfrfXlwCxmIMQyFsaIlBFCzbUV51YbyAnP3JM7fMNUs1-zPiUXeXUW4VlKBgBDpDZzuWkgxacw4aph_D6L_TJd6Fc67X3cysYvvK3UXCDJRvTRLPk_54ggKRBtPUYHmiViwRiPL3oF-KMUXcVcfMDz1frSd4Ds4dlUgIloThMMLUkwgHIrIsBtkotf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COHdbmYdKtB5tSRyNzAKSzCHBDpMYz8bJziwrsvNFrky3GSNsJLxpyiNv-1bWuVmG_gYHffGduYlLRcYzAS69fhca8ReqprpSJv0L4FCgkmNDSxnULKWULZBSSs6gX8AnGisytqcnkbZMdeJNE1F5Ctm1foFlnR-26aOVNSbRWqngbZnFaFUALRqx4r8tuWIub6L0yNl4zNtshsM00ZHnCbCkf5c2hGnBqfRydWGIv0bbXJVLNQdkBtx90dzU8NNdcg_G9sCcfN_xRyqNwYNSXZFwH1ic3o_Yeo7kMupu7UHrQgIC3BGOulRkhvHy9Yhtx0Ni2ux7-nAnPYP02AChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCKVYQmNdKc_HEqnWUnzta2rmLuVAT5digCngF52po758pvbd76s0Oa3Z2kq8VN49EVS-T88gmKuYjnweI2cZStWw_n4D3AOXNR631K6EYQxWS_NzwMS9XdlyRQZUFj23uE8ijVFhhJmiSnhv5o_2JvhKWPb1Ut-0fB05wpvpneg_-4_9Elxq0RikxC5cjqHYAY_W-0XUlruILxQBql0cYFHFABdSosQ6EzbhmIuf542Di-cHiseLbGsMDEMpjTd0k76VyxNNZNFtlh3izq7lkh2iTOtkAeBjWLX98WPsgw94iZ7Fd7sd9eaRR0OdHuv958JkKLADN7OgPapmpFVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_W8yB-nC-ncJ9Ayc0lAgAPo8He8yAM87Ja7vh56nM0CYm84WJ2XuSQOag8rWMxeUtn_Re8tGvxhGguQ8pmCBYdbcdvkAgRzGIpPDWxlhQnzYbSmQ_HkM9oHhxnMxnf96c0GEOiRJDMEk1jcBugjjQ2fqJOPoz0bzZayrcOPylULMrRsVFizsxKLv-M79NeRzzMX7nE0GNfTX3yTqd4WWJ6ve5RieiAU8gpIkvvFsz9QWZeJtOBQfpLhPdzRTsgItcfJZaqj3wOww4e7KFCyRqPuP1LsbqVNCL-BzBjssc829Ektd-XCC8t2mN5pJdHy2MFnOorpBeFwAq32we8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK9XigW6u7bmYUaRSRtZkf4AYCPHHry4yXA8l0Biio8jQg9LvqEoVVvs6aWOXs_rbGATYuyt7ow4P2kkoiTToLoBVb5H9G8vHymstArzw_XxGo0SWx7dPB4hYCtZhlEZc_iGmz5KSwcCBmzT3bTYmJPouboNzrkjNO8yVyi9IyZ9TpEEx0PH6BiuBYIuDm6WWNAuBsrpoJZhY0V14G4JR6kbhTdXyxPRB4cuSUP8syPYQ_I6zqqfGytb05D4zOxNiRc7Jq9WH_mWjk3CxyTEdqo4YTddkQ1X6T6K72MVX3FxY9mGpClS7bge4hNN0rToe0I0dfok8JR7GE_rGRee-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWUMmcdQy4gbPFnoppVQ4Ql4XXZMb7hDBi2U_u2_Z9TJTuipybnErQIabFUzwCr2cQ8kTjf2UgYd63X2VNFfp5kZgt-3xvXHQOz9VqMEW7emBERC8kkTObEvwp99zS-t19JIpY-WMDB8-KImyG3cckplJbCq8TOzbssuLCYm9PH2tLcBYGI1h888u_xL09yC7RGRq0LuPJaFDpuuYTbZbKgVWveV0Tw5mthm0YOoTvYn-Ui3rgQtKPHQyhQ1tRonEkYiF2ae-Xm7Uz8Zj8Cm4yopaop6UmwU-vZ-JVTUkqkAu2rWWiOVRXmrv_6WoJouegXzneU5YwyRAsp-q94Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWyH6B9zVohG0e--Nz6QHMlv_4qU53J15KKfKYRs17AHRlhxbIXFB7DNZwyE-vxgELN6lFWOKcQtzMBZQm3BgDk2Fv9Dhi8PXlxpC46Wj8e7UWU6e4lumbdgEfGT5N1o-LZ8t5ztR73ycKE6eghuyADHtiGSLOOUL0JXrvsIOPCA6YzrFoiNp1-esuAUPByyIDbP2RMTLZs0L-gQzMshK5PpopjgU4z397ZG8ibaPGRKIod4688Axt8BV_J0VS--21kdCwd3l9lhS7oLolac0xF6EGG1bDObpXFNGsZBnFWEG5354iKaqrvnXk7AGMJOvx9ZM9WT97V3aKZvuwqdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=KUGAJNybchwRKF8SREptRQ_IeAwFWXdW_MrbfKOoOLLlThUCaMukpBic2LxD8ndSEAMjqyS2Kr0rrsLhD2yAXYNARhfhnwy4v5ybbH9MMN1h-A-qRRq5962iQGmim32BBbmuuAwwxuIkPr3Gu0AfFgL_2sDkw27W46D4WJUvFluq9ddPTEqFc6zX38UzHHJPik07R8u4cL51nKmGIcgJ3-byw_QWYkeLF5xTSinUiuO-wu_aGoPlvuY8jc7XmzmRVhTfKiG7pozbJiRTOhP-8Iame6hGC1bkCcgzUpB078fnLQNOiwLmKz8e26cIez2ifrelITlSaFZHsHpYuExQFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=KUGAJNybchwRKF8SREptRQ_IeAwFWXdW_MrbfKOoOLLlThUCaMukpBic2LxD8ndSEAMjqyS2Kr0rrsLhD2yAXYNARhfhnwy4v5ybbH9MMN1h-A-qRRq5962iQGmim32BBbmuuAwwxuIkPr3Gu0AfFgL_2sDkw27W46D4WJUvFluq9ddPTEqFc6zX38UzHHJPik07R8u4cL51nKmGIcgJ3-byw_QWYkeLF5xTSinUiuO-wu_aGoPlvuY8jc7XmzmRVhTfKiG7pozbJiRTOhP-8Iame6hGC1bkCcgzUpB078fnLQNOiwLmKz8e26cIez2ifrelITlSaFZHsHpYuExQFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=lTC8VHE1YrT4YVHKbDIigdgxFyGoG2UeyWlDysASaC-hqXIzf_fA8YyDu11c0RVhAt1YQL05Il86x_bN9ZqGwSHWlDt-ZppUlHfPvZSZV-Yb1W5VpMAHbFqJZg4Qbg-MIR1Cc3AKDg2PiIaQFBu9VlnKxi9YHC7GNuocxphh18VZPsoGzdMFrkyfEks9K5Cuu_zSybmnrPioW7zEpnvCFfpkVWVPLl-rGeGczXXXbCboVT7LMcqYL01nkc8SeGxEaZ7Uew9zbCrwmXBwbtAEmnVnSSA9edCehY253fgy85ZpNJrb_-xuwZwOw_vIbINbvgTNZQlVntBQBGPIILY-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=lTC8VHE1YrT4YVHKbDIigdgxFyGoG2UeyWlDysASaC-hqXIzf_fA8YyDu11c0RVhAt1YQL05Il86x_bN9ZqGwSHWlDt-ZppUlHfPvZSZV-Yb1W5VpMAHbFqJZg4Qbg-MIR1Cc3AKDg2PiIaQFBu9VlnKxi9YHC7GNuocxphh18VZPsoGzdMFrkyfEks9K5Cuu_zSybmnrPioW7zEpnvCFfpkVWVPLl-rGeGczXXXbCboVT7LMcqYL01nkc8SeGxEaZ7Uew9zbCrwmXBwbtAEmnVnSSA9edCehY253fgy85ZpNJrb_-xuwZwOw_vIbINbvgTNZQlVntBQBGPIILY-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Totb5PsJf9-iP-KmJaTmhK7Q5RW-sadKdTrZ_bYkYRygzGaq2TrsQ-jUoJIZVjLVO9w-0IXBidml_vmW5wm95nYRIiJXHJtRXKzGbvQz7MxWYtk2HJoeI13zCSLWBapRrgS29wkJrLY9gEkr_vgSCv7wlI2ov-8QSSDkChnWYjEZKRJycD4zd2DQMwcIoS0QkNEq1bwmOzHoBCW51gVex3DmHO0jVmSpmVIr3qWqgfEQVCeUUq-fEhe7uy5fAr8gkBmzq4RlXWpbJjE1--qVx8xZN-VMjg0m2HuI973j20XJjvbChm-xkX4LF6EvUNVnAA9hM0bdQtHkjL_3Z-EKcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agm7aCLOs4hyv_Unh2Harf2pQJ5zxdkBAvPO6O17xN6xuyp0ujhyGrb1DkDptV78s-1l-t5RFii0LUivhfidP2LjBnUDK0O9gaSfPgvRH2TlTsSLIURN1CwV9zuNpmMt_U_PujdCD1LNqYvZqL-gPk91-LppNI2ToqH9GKEY-1R8abt-0A3wlQJgzfOYs1VR38Cx8AsG9Q_qsEB0gZLHME8NMhKvcZ6kq18zkcXhLGpU3gapIRaO-udGmNXSnby7u6WxHjMQDvpvrShMHX2WE5ZhTRVl3BZpB9XcSYnQlmUPmGHNuxlbj1ox4_dCxewYDy_wzIN0kQqyXhdCIGSCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKcfWuNwHLAHqVZ47YcUI4Vxmpx_zQg6RyIhT6_p8K2rmoxUwwiX3zexleU60UZ4jD7ZJknNJTHYp39KvLT9Evqfbq6rTBkTDI2hJhUKvl7t5vyUOtdss54aESIWQ2Xa9r6QpgGOgWiW3IGQjw5Vedw80hcKTyMdjY-ZP84VlAhYx1VdcozhF8KEVmKl_v-DWoxo-78kuHa5_J6V_SBFM0lg-cx-DCmpYcFkG1y4Ih-76ptvpo3MVP2GvvDClW8cImprCkCuLbKqfeBfwgdLJxv19Duo4tK4TvaKIzAPZyiR8g9Yzp7QsYkhJ-OXbxCCkIgzzSNi23QNrYR1tHodsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWk-JyTIUlQxXyDBmZGpuQP0ibDa9Kaa411AynCp1qol6I7tm3V6QvZe6DaFdi2XyFdnFSc-FNvuhFKxvsEryr7LOQixd9-LNjQQsjO4bg5QqbEq10kBPdzPEPVKkv4V-3afGEbJvyPCW-a1rkiii2HwlmYwWbO7XjRZr64MGrcmw2ylW6KNYrscdcHIOJkbFJjvyOrhj-LLwgc42enmCxnsvOw5ArEZp9DpzJeWJoca1XReK2PmOubPXNtsdv-DtpaGLO9fU8LZ6BpANNFEtAjYmYORHOy3Cr6M_jXx1pvL9OKojyiB2ArGTX3ENij0XD9WjcP8y-8ZvXV6MXhXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MujZELIeh3QyKn1l9i-ELVu9tFAI9t3D1AH5DaxfavFAET9nrXf1e7PM5GgLDII_Ba4COEJAS5u2I_mh1tw-xVLcu0WjnR_wnYLsGNEz60Luz0foh5bCc_kryE_pS3nEb0-QPl7WZZpibuXHvy7NoPtVdSuqosWYDa8ohcX-JCyGYmbNZmC96WF9vqbPXnjdw2mkvL36GlDi62PbS4tisCdTh_0G7w7St74ntYvFIQP3_-ymhPrakSDAPJFhgzSmDJJJgTmWhR8ceueqEocgjBYbCSjxrb6OyYZjY6_tvbN4gxeQ3hAKUowWEHvOoz2yWWMhQxzXA1pUZnZLGG_MQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چرااین‌روزهاسایت
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالات
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24517" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=jX_ZxJ6-Pf2v6jqkRzdsI6zfutkfXMceIErc555MbAzdvhNtcj7Zb39CBtiL54Sz462-gUp-Fkg8He0kp7t9Mwgdky_GwDQC-bYYBjCGUHOpZYWtAPlNQxfB4ko0mI3psev9L9HSP6sYuYqTkB6GHn8ddHuejE3gL6Q4mifLqiLjbf-v5tBQRoxgo3_VXSdvyeK8wBjT3zfenNoZ0HOjF9-9ZVST9-6jIuJaIWaNxij-xs6DHk1VbKaDvBoE5KXE3s2PCvu1XG_lGaZM9fVnXz_pRvBwzpolktGKmj0oRWP8y2nHf0fiVjCN22wWydkUNeioymJaK3wiJgewT-Jhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=jX_ZxJ6-Pf2v6jqkRzdsI6zfutkfXMceIErc555MbAzdvhNtcj7Zb39CBtiL54Sz462-gUp-Fkg8He0kp7t9Mwgdky_GwDQC-bYYBjCGUHOpZYWtAPlNQxfB4ko0mI3psev9L9HSP6sYuYqTkB6GHn8ddHuejE3gL6Q4mifLqiLjbf-v5tBQRoxgo3_VXSdvyeK8wBjT3zfenNoZ0HOjF9-9ZVST9-6jIuJaIWaNxij-xs6DHk1VbKaDvBoE5KXE3s2PCvu1XG_lGaZM9fVnXz_pRvBwzpolktGKmj0oRWP8y2nHf0fiVjCN22wWydkUNeioymJaK3wiJgewT-Jhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=MW9KUSTJdC0brtCcAH7c6csBEdG0kWW7f9Ru5ys2t1dh_azjwuDVc239PbpU0cZg0k6GjcjuOacjatjeLR8w6pxXcuMzpaOyUiCe5jGnedx4shiHjsOVb1IDk5sopCtcDIzCxwBCs43sHW4_Mrm0f6x5p89TtwK4PGcukGASYN-juuezLDMyGHd93zIa_CBPOMDMZRzX3B-SRzI4m1S2zumg8l7FLMK4hji1JPzW2imB1tZJjlsIzCvvEsvnWZM3nWYlZeQ03m0dzuq1kPZg9js2U1SNypmd3YG9JCxInrapOpVIs583SSTSTEbi5e0I5XxAnQX-ztUGZNkiS5aDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=MW9KUSTJdC0brtCcAH7c6csBEdG0kWW7f9Ru5ys2t1dh_azjwuDVc239PbpU0cZg0k6GjcjuOacjatjeLR8w6pxXcuMzpaOyUiCe5jGnedx4shiHjsOVb1IDk5sopCtcDIzCxwBCs43sHW4_Mrm0f6x5p89TtwK4PGcukGASYN-juuezLDMyGHd93zIa_CBPOMDMZRzX3B-SRzI4m1S2zumg8l7FLMK4hji1JPzW2imB1tZJjlsIzCvvEsvnWZM3nWYlZeQ03m0dzuq1kPZg9js2U1SNypmd3YG9JCxInrapOpVIs583SSTSTEbi5e0I5XxAnQX-ztUGZNkiS5aDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGCW6VH5UY1r-qvNPytx3au5dMiSsAhA3ydGBlVg37brUnJTHwS6zwg1pK2fcRQ6Z30M4LR6poKWgXdesqgJSl9bHDqHBeFlaT8RhsPUwmxBPgUCN6jYyV4pSA5iqpzFxs-d4n-Uh0fo81qYEXduxF2yaLEtyhY5WG4NTuteXCurPt4kzKXs_9MCr4G4Dz6hs6AvP5qqo-H6w_VNri0DJslfmqmowDqUQ9na06cD43qvO8HZkWNtHrGuE9POY5YFM38Nsa0z5jDWESKXAsyReQEiYi7Lx3dTE6sTNZ3zhQ__4igEn5EcD3wJHT4uHyiN892Gy2kzRITm-LMjc2cNghP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGCW6VH5UY1r-qvNPytx3au5dMiSsAhA3ydGBlVg37brUnJTHwS6zwg1pK2fcRQ6Z30M4LR6poKWgXdesqgJSl9bHDqHBeFlaT8RhsPUwmxBPgUCN6jYyV4pSA5iqpzFxs-d4n-Uh0fo81qYEXduxF2yaLEtyhY5WG4NTuteXCurPt4kzKXs_9MCr4G4Dz6hs6AvP5qqo-H6w_VNri0DJslfmqmowDqUQ9na06cD43qvO8HZkWNtHrGuE9POY5YFM38Nsa0z5jDWESKXAsyReQEiYi7Lx3dTE6sTNZ3zhQ__4igEn5EcD3wJHT4uHyiN892Gy2kzRITm-LMjc2cNghP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXOzK0Fke1hrGE-SU9Ts-S8Nr9P2kHSyDaXSEDVLQBOmEKZVw27ToYZkrQJBGaeA_sfh59Whl4Z3ks4ykxg2LBRzU7RpQQt_GGeLQC8ZNxxKMeuz69VUKwWm6wACXvH3xkYu0FZQdSeiPxnR_OFvMvlBDU46cL67l6kWJMEJF4OyNsdTpy20eWEl3RnGHTXPzs6AKNBzd0qJK3_F5GoXBUMDEzX7d4lpX-RM5gYsW8jQIBSgTZuMFB-6dUghcEfqmPtQvAdE-J2E0hnmYi6TE-U_OzDuk_Tm89D6aGWQKrdVv2uB-DdPuPygYOWq-Md5zcp9BmzCjuP1c9faruGTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHJTFJM3vGjC6WRDRQFhc-wKpm3a1DbLx4s_4lwhrMYu7aldY3EfyOuezvx_gzXFczs1J_HqL259wZ4Kl6mN_AHl_n6eFEAK64EjlNiQOle7xlCQ1Q6IbCT4YopSSTKAUrmUxAm1dFG17LsMKp6ZhBeGHZe8AX3lfxWXqXWjEhK09sMxUmgegzpL5rR7RV4oWuiUtoFdBRukweXTfK8UEUyDqXtFnbg8FXmfySpAtna7HkOWSJCEEY_NUyMhJGrHI8jvCLO-f5c0M1ljJPIiY75f2iSQViAq9yf7KkPpsZ-2m4EReiP6t89qstyJ3Lo4t8i_r-JAT8pOefZRsmoj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzSCmv423KPdCiBRGo0T6J8H0vHq9b2xWFHu9DFGuDZbn92GBPShgJGz297sx-TVYVx6A2sOGqFgnSPsLM_RxSvhZTAeHqwkKtKfjEQnYh3M0AIJ0fJ3YOJHKdZ8DALR6SdlVFbS9E5Io0hMyq6oHWQEyvfGnakX15qAd8-QOH0IJ2yU_g-an99nz5sAz2oCMv_SJAc9vW2hOKc5u1xdW181l_BAEiZ8nslMLKHRHrWfFXwnQllIKvQHPlwTZonQvE_C4AhLYu1YqYjZEQmuFF8EGiDk_TOr1odjrIaLnmv_UHgjmms_GFbDdw7x5LJq0IXcoeiKdbNPznzsYGlgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bz_VCu8G8auuJQDJfChJPoC8vNv9T-tWBOHhWKlE9lvqukjaUSVnyGnHkFl3BFrj2VNQsfA3fuml-BoXINzDj3YaWRYCHoeYilUznwTZ6fmpglYck9TfTJVOttwoOWkolKVP4AMtUMtj9CV9491z7OUvZfCJUrmVK6uScNwSMrdX2nFjR_mkaS1MZZyo2Lj-9VzA5ghyP6AZwxNV_ANrCXsm0ndS3wPU0lSB5ZKUt-9DQ2ov4E0XyMruXCkemza5B3VpItqomHPlgHs2kMI87BO_WXHyykYC3cYGdq3XdcOrB0eUH5QZMR-dj8jnhpkPPym7CJALHiBcwvGp-K7N2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=tR0UnNqCHzVLcjjbXUzaEbYOIFy69StwDlmGQUqG_eKMYhXMOd4mldWBJ1eiZT54jfiVUjajiO4_2Un9hlP5txafRrO9KjU9_lqqmlP1dt7Q1KlrjXGjt2P6S7i_U4IsQ2lLQk5Zi_gNK6H4ftK-7x-oerGFGf_OkLsv4Kw2MVzPSOZumhWDjM2iW6ySKPJWgJguujGucv-18zZslQtuIaafZDw5jTPY23ry93Ol2UJK0OSGuNyTuwnKNEg9FlRlRHt9OvsCJMeGyPFhAwRrmQDyc0hrVHessAw60hitBYoWbtXoTsosCcvEm7f4QRnFbLBRzxFXtaQQUqjUHrM2Gm99QWBgcZUZbX-nxv0QpWEG9WQw1bDGGY87RogurNYkyroEjqiGW1NzviwRn7yWNGTHfeXLMuTGj_ulRULj6ge3PFxSaSrCRfKnQM-6ObPC8YoT8xAUIJV6rqvusBoPsESZLgbcBKNhi_BpUpF8eXIgqDwLK733G72l7ArJd6Tlii2OZQK-dRgaNXCC5bN5nleMyMqGQODjnY4J4qkEtRADPUJFAc5FxrW0UFJcHXs9Q5qLIhRfUZlxCQ10CtmKGUNVfKLznaIx3yy-D9Ic5f9QnM2FbmXibsFl-2Ok4682ZfdrwzzaX6UF5PXuwMRf1RMs7sQc9skbDCf9e-eUfXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=tR0UnNqCHzVLcjjbXUzaEbYOIFy69StwDlmGQUqG_eKMYhXMOd4mldWBJ1eiZT54jfiVUjajiO4_2Un9hlP5txafRrO9KjU9_lqqmlP1dt7Q1KlrjXGjt2P6S7i_U4IsQ2lLQk5Zi_gNK6H4ftK-7x-oerGFGf_OkLsv4Kw2MVzPSOZumhWDjM2iW6ySKPJWgJguujGucv-18zZslQtuIaafZDw5jTPY23ry93Ol2UJK0OSGuNyTuwnKNEg9FlRlRHt9OvsCJMeGyPFhAwRrmQDyc0hrVHessAw60hitBYoWbtXoTsosCcvEm7f4QRnFbLBRzxFXtaQQUqjUHrM2Gm99QWBgcZUZbX-nxv0QpWEG9WQw1bDGGY87RogurNYkyroEjqiGW1NzviwRn7yWNGTHfeXLMuTGj_ulRULj6ge3PFxSaSrCRfKnQM-6ObPC8YoT8xAUIJV6rqvusBoPsESZLgbcBKNhi_BpUpF8eXIgqDwLK733G72l7ArJd6Tlii2OZQK-dRgaNXCC5bN5nleMyMqGQODjnY4J4qkEtRADPUJFAc5FxrW0UFJcHXs9Q5qLIhRfUZlxCQ10CtmKGUNVfKLznaIx3yy-D9Ic5f9QnM2FbmXibsFl-2Ok4682ZfdrwzzaX6UF5PXuwMRf1RMs7sQc9skbDCf9e-eUfXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB4QnEYREw1qLeqYMXReT-2KhhLFO5eiVIAayIBNoEQNC9alRcPddhCqAcwp5q3VnEYFGKSlyFor4aEMiQQUoKoO-V7q-MWOdvXfSO1-2Y-t_lPxGJ5jnEWSr9mJSKCkjrT9aD9wAV7z62eGNtKzsBc9SasmEmRONFQaHnJ-7RJQlKfnt57SKpM5dNSLxOgv_0HiyNGq9KPExOMRqED8EcfHihaaGnZU468q_TLe3OCVcQ2YLvrHnAE06TwewchMVptuKVXpM77TFlv-wVScJ4lggnwnoXc7hYCh_K0W_Cz9586wBfMlJN5y96KapFyXDVgQ3imIQpNaqUmP-BbF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=EnrqamBINMRaJaq-_7L54_SZBmSnRPK5IzwiTAt-PNwtzAiYsB6_JdgZmZewTsqCA2cyVRQ_IK5NsbGrgBlcgAB2z2pye93N739Svn3HuIBSAW_skYSQMpttIZ4VqQbqSPEwSS5tsqCJy2EblDq8uu2UGqF8s9-9YOFEk8c79yzpjlmhgtkz_sQvM_M7-rY83XaA7rbYVZRzquICEl-KA6RJ4KiMbNh4OBbk5RF6MfaFy_WOC172ZBve-8I8k5QO2QutFswLeI0hMaqkpMJw0aKSk03tEKyC78S9w3fxdxraBr5FlUyEf7t7b0qbI0HekKAFekjN0MXcG46JIXYiKzk4qLxDA1rKoHZPVfyYg--8EZ2mQsKG_OJhsN-4kVdZoCnaodr0Wr1PDx9f3bRBcrInyB8lv7-cZDhdk4W-MS3MiGF5F1ZC014IGH6LHUMwJSR7N_53NSA63bG4zUdUO8mfiSTrR0n1tTyCQy0pRmaQ4C_wBbQemU8AWqr1foLmvXWDcqtUouZnHqDxpd3jfI1yDMZlx0E_BbwVK38hfxA80zeHog_UIzkfMDBWuiI5a0ltELkknwRCKISOynhoxPOvO4coroeLhvFUGJRsOs82kQ3R7JPX1yOwd3w3TWKQ1c957XwxaaglGmiGqBQi_ROZarVwHIX28TEzSkimcc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=EnrqamBINMRaJaq-_7L54_SZBmSnRPK5IzwiTAt-PNwtzAiYsB6_JdgZmZewTsqCA2cyVRQ_IK5NsbGrgBlcgAB2z2pye93N739Svn3HuIBSAW_skYSQMpttIZ4VqQbqSPEwSS5tsqCJy2EblDq8uu2UGqF8s9-9YOFEk8c79yzpjlmhgtkz_sQvM_M7-rY83XaA7rbYVZRzquICEl-KA6RJ4KiMbNh4OBbk5RF6MfaFy_WOC172ZBve-8I8k5QO2QutFswLeI0hMaqkpMJw0aKSk03tEKyC78S9w3fxdxraBr5FlUyEf7t7b0qbI0HekKAFekjN0MXcG46JIXYiKzk4qLxDA1rKoHZPVfyYg--8EZ2mQsKG_OJhsN-4kVdZoCnaodr0Wr1PDx9f3bRBcrInyB8lv7-cZDhdk4W-MS3MiGF5F1ZC014IGH6LHUMwJSR7N_53NSA63bG4zUdUO8mfiSTrR0n1tTyCQy0pRmaQ4C_wBbQemU8AWqr1foLmvXWDcqtUouZnHqDxpd3jfI1yDMZlx0E_BbwVK38hfxA80zeHog_UIzkfMDBWuiI5a0ltELkknwRCKISOynhoxPOvO4coroeLhvFUGJRsOs82kQ3R7JPX1yOwd3w3TWKQ1c957XwxaaglGmiGqBQi_ROZarVwHIX28TEzSkimcc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsOLbCiF4k4FagHekbK2j7tcvZq03lv0IAnVzc78ancVP2NYByyzrF7Ydhgwre7rN1S7Qs5F6dnpXj_ehkxZwl3_1cEQ2Klx-IJydnTsRhxXxVa4pTiR3FgDc7OxH_eYiyI-oXGUEN9Wr2Fx54t9eoUNHL0-wH6JMFsldDmK6ZJU_85sm5cZqPfvOK-hFX5Xtd5CsA1Lk7rxsmtBZ2tfV9Mio2iyS2JX7tDC8fR-6yg7y7mfeHGkC0wPA1WNNAZE5bYZn3Sz-V1F4zTB1LdEt6-rLnqTa016uzof1XdybWZ40FpypXFs7WLzzOV3SuOfVsXhIRARLzkBIdaghBRqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njnUrpCDSmaiR5oZyuaAcxuyvHZTVCcIVhp3U1OfVvKVLdsk5kQ2Ggh_Gs4CGgZhiVaqP5wv2gPsJPOvni1u7ZVWXrZGabmFYecNm4fTamvr70SbGk25gg55V5fw3Ubu6UGnooqLWvMTf9AJtw3Ayp1I-ziFxnGDoZuS_IRILP1jbiiNNqwB_X6aOpmV1hgsjJd2S0gLf_OPmBHYRrdUv0z25-Xbwyxl-SNxr5NDucn-547P6OKTohfuns0etPd8xAmG_Fdo3_i409rL16n3v7OWpcdQOxGOksODERT3-dLRcBLt5Jajf739rBn5VGl-1jfdIFKuuDSypIP3c1eH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qp18ZrHovZfyo5wn3Oecy279QXu15cwRBhIXiaYtkrEhyYQL0Xl1L35lWAlA32rXUFCqXLbNVWWJTstBVwArVTTt2FwTNE5HMmKNSwYlpVHrKFsUjTetNpA0_hgEaNihzZOvGXdDgMumi_9_Zo3ADm0nrMaMRC-wD8-yOZkO2fpJwj2zA04qSarNIMS5FoPFl9IJ2QgHJORU7S-kb17gvraUjEcSsxCix0P2aMP8YsApYUhs3UpBgWuJINVgttDT_FLiU0Sx0IQudfXY1P2qjRpGmEm8yUUIYeLWXczNQVyud1Emv3QBQMbVa6-c23tfHhN-ERnTxghM74liN-jcCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o88HaBt9ZaAl9li0u4Ov0lu92eoHcu2ntR9Sqjp1CIGa27GL9n8MH4yi35KWuZVcfL8TyiN45bg8UkMNBdTMVrvMyJeFRXfawAdPQwjDFFZCOtkI63PL7Cy1OZCaV4ebFsrFSy_WbIyzOJOpMyvhQez7euzC2ZMJTst-uIiAnqRWZt6MK1cGlhL1ooV3Q7v1mR8YbpVQpAND8r5HbOnyhin5wlox3PVhpS2Yc0KuX-Mm3O8R0WrVtOFzQpkK4WM6R88ulgSKwWgW4WqZ5kMSd_7oU7aJX0d-ONrxtHUh_qayk7kK1-ZWcybcp7eG2EXHimZLS6V5YeO9eVRsVnRWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZBW5aBG3jD1ZdNdXJvcJPlAAMmdAuSmIdot0lWZYkYhWzTnYmLoIdr7SYuCHrndTIGGAJAZaI2ClYPRW6HHWgBLxbGkMntdcEynhbH-wtT1re68C1D9-yKLAvzy8M_r5OI0BRWNjchHk9i1ADlUP6yUh4V8Dhrh9VNkSCaTfkXfUUXILnuc3qFdIOP7ocpa2v00l-gl48Qv2QHSc8CiJrdZxvK5Ln51fOYknw6Zq2WyROFU5EB1sVgtIrwK-l47dTkXgZhtnCG06_XFgyttBpNB9Gu7jYGI7Z0AGBBMTP_kvrppVPnAFEubKjBWgDvs8XbaobxE1vq0NnrrfxmK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvDlkGJtl6-YnQURwbMZd6qCUKfypJCNdpyfOmt_Lk6jVAD6KgL3wglT4ljlNsfo7ImI19ZxYRyfpn_PNhzh9dxJnUk4k2JZxNkf6kfCfDDQw9M3i3hwfTdhaCqgvC2STmPMQHVYL20txpYpE2fPnkKuU7cIR0NbePRBQPr-pCtp0XXiTt3k8KadNyHKTGqdpoUvLkEVjQyx67DsGe8Rey4Ry9GkCnvQChveD7xr_8gp7YYoigU-nN-_4-tS-6uAchaEV7HXu4dhaPDIjdDt_SGQuyyWgH8Hnzgp3SFxXGVyxEDlWLQyCSLXGdXXJK88AXR5PEbV2aONm9Bq7E8vVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDCxCkmo7fHOSVlmXEoVvnWLMqiA6_JPCtAcs6-nRnNkzOqCUfjeZs2_GXufZ0lFVu00JuOBW0nabqvhlApymLBW-eCEvAZVvvfMZQu9Omq6-D7nNnZU76RIo7eBUKq9wkqpuJstmSwKCaVUEq8FvDopXh4tUhMSzAxXnrXTy79SZUx4CfSESze7XnC9jfaCytn-F50UjbsxbHbbWY2IJi8HTVSr-Gvkdjl19EdrONPpvnB_gY4aQorvM4qB0NDpneBnwI_vxwJCbofl5IfM53GnpHvQs6GO80PbATmUh8BQAlMnTDhgT7XzYw1DoRa_yiEt1R-7Yn1cH5LGmCsX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV7zXK0iY4TydqEu5k0Am6mTzLXs3UOs8kzzGFi7BRftkJBboDupjdFr3C2CBsSMzJxim7cGurmmySNB2r7RG9dpXpbWSmXxAlAorlogOENvDTqV0K8D144OgA69tJAIZRzJwVrp5-zG_6LkXON5oeDe0_I0EN20-p7JEIlgS6LKI3AB24-Tedt6bvaodrOyiN591s1qKIUKXnfRjjHBavkqM4ZmmKBFK0Tkcrrhe9Dj_JTIWs-dif9zOHo_IcGfTXfnPUg2ovOyyPJkn_eAKCLSmIrOgLl1edVrTZarEg9f0p0QAFoTrh0oMwCRnoWWJ827v9iF4RhnJ794drDkkKic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV7zXK0iY4TydqEu5k0Am6mTzLXs3UOs8kzzGFi7BRftkJBboDupjdFr3C2CBsSMzJxim7cGurmmySNB2r7RG9dpXpbWSmXxAlAorlogOENvDTqV0K8D144OgA69tJAIZRzJwVrp5-zG_6LkXON5oeDe0_I0EN20-p7JEIlgS6LKI3AB24-Tedt6bvaodrOyiN591s1qKIUKXnfRjjHBavkqM4ZmmKBFK0Tkcrrhe9Dj_JTIWs-dif9zOHo_IcGfTXfnPUg2ovOyyPJkn_eAKCLSmIrOgLl1edVrTZarEg9f0p0QAFoTrh0oMwCRnoWWJ827v9iF4RhnJ794drDkkKic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVbKB5IRWwA4enaRtsbU-NSFLGzmmNERCt3THgOtGO-0Zsmo_jwT3L8rEUCVJ_rHcYZP1gCKirraS_1i-6e86RqMfzusTsBIJGQsvkG_ug5BiFQEtcVmRfhfCXVi-6l2x57IDKdOlOpJVKmFgyd_a6N_nXREk4jWD_PSWIsnWwiMLJOeE4JJRm5cMLxo1SvZ74yPzfTwoaprGjOasOBLw5cuhKON4Xy0pQE8UX15cIKIYpbucm3Do_157VIzOs-q1nsvejdFcT7ODbIfhfp0kYw8Z_3GPczCklU12Pg8YkNkkG78BxUXpOAcvpQjJgIqZUn-eXHd3ZpnHaOQShiZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLThSbE2X_BVUk71qFjSivVFtMJTHvSgskdRV24iAjcTw18-3bro2XlE1cD1nUcGhjVl99tig7o3Y2JKW6miuWIAoVecKlYK-6Hqv9Z9rHZbfrqOFevhH6H42m7mrWcPNixs_239oFi5dw74R9Qfbx4vcAaqoTrhPcn02NyFFRpBFmINIuMtQzQV86Y_Yb_eYv-i3uUnDvHIy5PT92BhV4tGDqCX8gwXIZz0I-GWX04xoqMY4pyzFpBONHrxn9L8cCj3MoPwJ56L1FNBfKi3WAwOryhmgVMeHKDqvjagLtuHmL_h21PqsdWb2Ej7-y080ipS-3KgYxECheI3Jf8j-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtJiVNem37YLhktCzWLIbJEiR7JJPZE5ZLhqT0Uj1lyUmJgMzZhTKv3jMp3XxPNZ3MGPdNJHaTYUNgYIhGH-MPjC5iQqym3-yaZnVzxtI7HhX1-ZzFqvkJzF7aMfIP8WdNAlfCZtgxqci62c9nbxqrTh4wJYcGlQHywzEOFM6eIuft3Ndh2AgSZSpShZowX7p776637cT4asvOShwNWU9Dx33diDCb8zWmsStHss73qZRhW-QDTNAnsrDyUep6h83EoiaaP8hIQndC-CwSV4HF3XFUZ4mvIYCfiKNSEnWfrjFSqpdSuyn6aMH3_cGhXsDE86eDrD2WpDJqa-p6hXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=sJHtjWLdPIMA8x_kzzsAH7p4_RUV7DPhXrFX2cQCK8DGOMC0Lj8rqk_AdIkD6togFyZ8hAF0CEFHRFgn17cAS46RiuV0yZv5jH7hhNlKndQH_m_jmqCqCRKuYc-tFPGtLGWGvcv9sLdEZU0H64PDVKr5ZjdxOmlS-E4rQU7hlHKU33V6vxWUxBVaJSheqzlBHLjvZX8CLo9SX1IwhwMhytHI1aH8pmcgsMqvj9NvMXSdA3Ubt6YIRCCOvT1tkqYABPJinTumHOs-b0TGRxpnVatCbueOcjttfgwu6524b5bnwOnS8WmlCaidRcZOgE1KISYhJcV9J6zz08jKn8y4ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=sJHtjWLdPIMA8x_kzzsAH7p4_RUV7DPhXrFX2cQCK8DGOMC0Lj8rqk_AdIkD6togFyZ8hAF0CEFHRFgn17cAS46RiuV0yZv5jH7hhNlKndQH_m_jmqCqCRKuYc-tFPGtLGWGvcv9sLdEZU0H64PDVKr5ZjdxOmlS-E4rQU7hlHKU33V6vxWUxBVaJSheqzlBHLjvZX8CLo9SX1IwhwMhytHI1aH8pmcgsMqvj9NvMXSdA3Ubt6YIRCCOvT1tkqYABPJinTumHOs-b0TGRxpnVatCbueOcjttfgwu6524b5bnwOnS8WmlCaidRcZOgE1KISYhJcV9J6zz08jKn8y4ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So9W_Ehg0M4uYgRMDxhZ4Eu1vVlFcmPDNqPdowMfGzQshbDFqUxPGYFChypz9eHXJt33WwTK3HxVvLujGeQMu_SU1Vizp7yzHDnJ3p6cIq12RJzfOv0BRzNzQ2-o0GBjb0l6ydI9KFjVygVZjLrtqJaASGxIHPdAY8vrQA1cO8DUfOSSSb0yGvQZ5I5-YmxaMTpIraihm04h5DrcEjrkWO-FZZ9RW8ReeKRYPB38nkAUi48h3RggUi8K1FBDEg9S3t6NFrpIRStoOPhEG1WcM5xGmzfsehrFWmzehaWj0JoGjJ74fY_BeJmD_Hi_J44vmLvjBURZT9vwtRKhWEbW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxW35w7My5sFgkVz8WlwBcdzGme99H1cFF9iKr8JY5n6S7x3QkzA-DGmYYa4jU_JZ6ihO5Z-zo2rG4mnoJE3QBNgyX4OIkAUmV_vzlyYEnTSiTb0mhSxcwTkrmaHHGQEN1v5Edbz5ZtQWbzyd79zeQjGf4NpB78vuU1DJzB4LK9ZcLagKZLT1d7wHslcjLfMK0ghWdDCn4KUewt5jlzvhmfmtXY1_iUPLPVKLrHG9zS_6FlTb_5qI3PctC92NpAUt3FoSNOfXl5QtO6KnzLC8OTuu_roQrk88IgnnQXF4FMJBIqtraeamCYb9yAQ4UzMBdPL07F_p7L6GN34PkLgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGJ_3Q5HyM2bvPy3I0KxHasCfRse9pgc5MzR4QasJLzlC5nwD-hzC6wxVrMweHcR3I_8KhoAAghp5Uhqqn7-BqX4caFaCj231egNGouyHm9xnRVIQ2F6ql_o5NI1LjXybHvlsJVlgJ3Y9fcaR7frs0XkGbHGgFVEo39Y0VWtfT1HtnIQbBFZUlzqR9V81ohRJ1xNznTyXkgtue1Tl8kk2Gp0ElDoJFiFh-jG9pNH4fvIVPhjzlZB0GxH8x7wxMhS1UhIsZqn40Fppv_fvw-VHq-PtMQ7wty1Pz620ctp7KLdtRdQoHqizgGn-U-xdB9H4ewJ-v5DQG1wlcZENRyziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt4sPDjkmWvTXGYasFTipDzdqLVXX-Gjp-WIkVPemy-FajFexOKOerxuelFieps0v3ff5oZdOZ5rB8t74tMEWfyHz00_wH-JCCL9qOwbTW8hdUcvIo-tT9CaWHNgdJFuDRr9kXXz5zTRG1y0HY4MsljHMdtVDL2v7Texz8KjEa4F3JzRfrSgxSzKJdbAUDD6hT--ITOUq5m7fdYNA_EUWvD_qxyUuc57q8EF-vRSO4LqNata7UOWpjc-taNIro0WwsCwacEVCIaFAmG6WiP7Fd2BkiDLirzDRNakLj7DuYtXcsHGz90v0MNGYqs9D31mGYzA_GcRy2H1MeeJAFYAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxsQOSa2reUldnBBItv9RLN_l-uJFW3XeQzKW915aGBvVVK3r5DS2XrQDjNvMOqy-0lNUyITDvZ_35ik1mqQZpoJyvZNja19XEitYfpqKkRbVytgHeEWWClMWJwkvJnf-kyW1ALshzz8uvs8SrFxTghi-WjhfM5sfozVcsqueTZ_LvPQU784alLhUIsM_yXyGdeGtVQKIqFyyKHKpTyp_gfd6eVEjF6yElj-zJfDMZTJFL5BMSbn-ra8IlxKFPEUgoXb1C_jRpDgEZw2uPq0KWhPrcV7p6TC31NnSnzV_kPMfNRO2zL4gAR2xAvyzEpURJ0EDB1f_wr-Mm9gZTCz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcjgbdWLOAkhHHe22J7ghAyZ9ewzGQ8HWk3pWu_FnEjGSH-W0begY-fDg5_ZOS1NUNlWWe-awQb-lpUr31qEEERcOUl94py8POxb82T9ruRoNtqWuRgfvO3PfqK7yjTpXbWCA2jzb7AGmK3lRkYgVlIOilNOOSjJk3_ds3ReaH8oaGUqe2Eg1pfCsrJdvlu8aKkLJnNFozzRFL0wM1VVe6ePcIX-yPj1FNojxSGxj8aYVP9gbsaJyqAy820J1TWRduBtrTSDWknM43wo3GkKink84JrXykOusgxHa_bykJpS40I7iBPch4WkRpGLZw-hQUXszLXrjZW0qdVm-hthGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmgO3nSxEpi6l_nOemmhZ5xM0EXY1CwD1AgAyW9qqDrywIeXeOztwiyEki1U0Sbv_8-5y7KBuYmG3Bfii5PBRiu0-3viL_w1uJB3LoeftLy5UU_Y-H49nm9jr8J0zi2AcyE9kmcPfOTAGq6LHwGE6JXm5D9OrkwUq-uDR_xFPeY_0lyZQBe1n8EYv_3MML0mL71K5LSXMgEulISL3y2wM2CoLmwrorG_F6RpHV5IUUrUx-yG5NpX9zUu-KYCyI-hdGMPt_8Cb5ft86qnvC0iAl2T_65fv7WPtk393jpBRBDUO7VVPUO5bwOMk4SduwAo-h5tecJtvWmiiWjH0fJjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9iPRLlYzi-QETEhfDzP0h9J-M9OZtTU60-JAXFtVTQGf3CRWVNOIgJC9tFrkTbdU8gm3TK6mUtmrrKlzLS1qD99rbkQhelznwU-vFdAq1vSZOCypQY6YuSnADa9dzFpGv-uKPCd0gKf5i1plaEfwOV9h-9PgPDRmS0ngcUsRQQq2YOa6R-OyNu6lfMFSIo8d3-nWu_fO0vRIVTb-HHpKpu_Po80uuNYA9smq-rzlpcgD5Plpk0kCQAXX2IKRZHk64WecICfnPmYM5K_Eog0DomftA5KBS2q2xK3Dfn83Jh7-CMsz1aFh56792CWLiQEH5FqEhzeg66hOOMtIOa83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=nda2nFxB6v1Q9ZEhAKd6SYrgT9oV62db4RRvpaNfYCF1SBvOiFtkLmEzA7jbWmUNbTc47SaDGl0sVKrXV4cQVlErsSSXvl26RVIVG5qHDnmAWGDJRx-zpGTeoJOGZZj8ptUA-Ee41GGdrL7UYUZFfrxj-THxFoDEgeH8zOIn0sNnK264aYMfECCRbNn_mO4WWeOSrvPS0I3vi91tF6QoSqU-bcwhPAUV-4KYnAl5aTfcWIqw8I3GMJzyXNR8tiaV5A3oOw-00kbKrJD3BF5ZSaIJEz0MxbN7I4YBsTl_laCNGDyNpsvgy8icA999dVgX6D23LJZcCgvfwZwSY5WU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=nda2nFxB6v1Q9ZEhAKd6SYrgT9oV62db4RRvpaNfYCF1SBvOiFtkLmEzA7jbWmUNbTc47SaDGl0sVKrXV4cQVlErsSSXvl26RVIVG5qHDnmAWGDJRx-zpGTeoJOGZZj8ptUA-Ee41GGdrL7UYUZFfrxj-THxFoDEgeH8zOIn0sNnK264aYMfECCRbNn_mO4WWeOSrvPS0I3vi91tF6QoSqU-bcwhPAUV-4KYnAl5aTfcWIqw8I3GMJzyXNR8tiaV5A3oOw-00kbKrJD3BF5ZSaIJEz0MxbN7I4YBsTl_laCNGDyNpsvgy8icA999dVgX6D23LJZcCgvfwZwSY5WU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H34dB17LZRMtgJJsPxb4cSoSoAXHXMqGS5_jYbtvD3G7B1SF9rWk2u13P5EEPkLIEd1Ad1uBV4gkWvtbXvIpYnV9wJNCTMGLqRsuO0T8AnBLCG-vfbm-NvoIWXyVeo6r2V2bbBZH0hxQKTyVbFPTNUKvMyfed7mo7vk62o_8mdRmmtljSXKrnb6SbScshAvOzJfzM4dtUgAgWTDNdtQ-i__lZZSIwnqxTlkftiQel1OssLrB3ic-kWKbczsOdDNzq1xKuRgD-rs-zkZlh4fo_VoOWOPCbpnfEj3zUf44xwmwVSdZq-nTE32x4-L-V0phhL93MwCWjGrW1dBA8UFQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkIiz6Dap-Y67IOkmsNeNUwVvJ6S_HCr9_zFu2G6coKCBOSpu_0Ne--cG0hZPuUA0zTIMPSadO6gYQ-xd_lowBagk8ff-lALNTfIhMi_tVVl6d-Oh0xEFUVmVFit-Bfol1U4NNBRYm6WK7XvQXA1K9jBdODKS9dVPOo8L1No9xJEP24LXLNhDEiD8wt7yzbgQZKjli_4742fzqGjCb2q7CAwQvxBoUVEhE_XRXzJXlCzRp9YUj-tqcA22KL0JScDqPDdqEjvfY9khqvb4mcC5WJY8qSCJp58rN-5-h7MIvZn8wL6Khmoc0dJkt2vqwv3pMtcl59JtOgJAL_MUnkvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaBcSCC_OKpiCQ7S_FQmZaRayto8nB1NU3_jL2cbliKfZAtgVEblf1IoMYna1xF9w0jX2h6VcKw6_ChJOLFQDuXhmV7zpiE1qGAICw7Zu59YfUOoKYLOtjRAAYxwkhITY83moP51GFavGk4IO-EkX-Ffd0KK0D0zY3FTz0ugFIctA77aOejgYxRlnak8MR88wAniayzUVpAbEKqrCMTkv5gCAVbXbIpQXCXi-t2ihiHNw7gevs2HyTyN7cshFVL88hnhYT53B5i8f4P7HNPZYyNYA0r_0XN56WMpUyrB3GBIT0o0pwFsjb0uQjtp2lk8yPm9p0jKuTKXybb6ZO_JlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIFKKzszAym6V65VTlw1mVk0qPP5yKKClEYjOhtU5jYMfC5Dy9939HKzqIDQcGrRgSWx0iJymLjObQ10CCgoahG804xcwCfwOsFy40zf7KncSekPwuOi4Y-75sqKCuyLM6o1496e64duVwqqpgxMzbP32K7N9rK79sqhj0pz2Vh-UIapYa9h4rJfeP8bojzvf-QwwzEaicXIbk4zg0ztHPaXVmntfHCobH8PTgw6h_gfTpdj1TZlP9z5jk1CWuVvAf1Htz-qp1ixA9irTayTNx_AfE-BnQAZMzFoZIOSQUkWLL0Q_WBQW4M2qT4NvVl9hJm3pYKAnVWdZCnULvVUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=gOhUeCbjYWjAyIsUVbL7f2AXPAMP339X-k5635Hh7AW_hIwIQDFHNvTV7VcnRA6Flsr0TWSVtKHTJBLepMSC2Exa-OnGNq68jDHu9j0meVFNg02xnzMPHDsZ0v64Afv_olM8pJLuNW7R6ul9_NkkNnSSTeFaFKQLnjimKGR9S2a2PD-cZT5pBJ7LMI2J1HIDPo7vV-y5TSknDWlL2VZiNLAMNUbmh4FQSIv3RUjy5vV5fjKZM1ywJfciV9mBN7F0HiXpuQKmufNkVmE4v6SALrUxoOCv0NMHGaPP7RwgmMMZfmvPyDdThXUDjjN27PLdzVKV1ceSKf1qW5j1x049lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=gOhUeCbjYWjAyIsUVbL7f2AXPAMP339X-k5635Hh7AW_hIwIQDFHNvTV7VcnRA6Flsr0TWSVtKHTJBLepMSC2Exa-OnGNq68jDHu9j0meVFNg02xnzMPHDsZ0v64Afv_olM8pJLuNW7R6ul9_NkkNnSSTeFaFKQLnjimKGR9S2a2PD-cZT5pBJ7LMI2J1HIDPo7vV-y5TSknDWlL2VZiNLAMNUbmh4FQSIv3RUjy5vV5fjKZM1ywJfciV9mBN7F0HiXpuQKmufNkVmE4v6SALrUxoOCv0NMHGaPP7RwgmMMZfmvPyDdThXUDjjN27PLdzVKV1ceSKf1qW5j1x049lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXeG1Ad8Vq_9DnCdCv1SmXTULm47SSKBFAieKCDb9_M-mCTdmTvffh_opgxYGJAeKDfZV-bk3dt6lg1n0usW7iOFvvLjdB2rshaXFuSgHtmvsMvCrkl2wITcjfRhtGc_IIg3jDxI-GpwqiiuF7lkHux0e0igJAMheG-ZcK-13_OoaGM72UMVopaUxJ19_wiWD_AHkU8XxPs20ACbHFBaK9Ma3HpEWDcmf-ZdLrxWegqYqByYPWgFCEb2nukyq9CJfcVjvz8xGMzeU6lWXotPtGWUX9u3_2ipMBK2TF9RDwqbLFyFxGzy6lNp16UcdZgWwgI-7MfwvabzWCwV0ueg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIgUwFjNYvQjNPY8Ehqt39HtgVsz4hQsEeBHk956q4xGfVbkSmbczX2TLP3DWxFB6v92IaDBIyh0QB6nAO3Knhpp-3plyXie97D9cGYYF4jpBMhDA4WQFBnVh9pCmPI-rxegjifzcCAHtIlTJfnk4faYJBHNX_ZoJjHKcOnsaJneD0a3Afhp4-ndpQf4l1_ZahAa2MNUb6ycXvwxBDoJOisCIEMeLDooq_62rJFJoeVLHMMLb5f2k6Bu0DHUWu4v_S0txVy6vwwGwznWRT3B_XgYaej5KzFT-MZAXtoFtvOtqQD73gtNAtCuM8zP0MFuvqBn1uGl3z93LVPz6oD3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5XwSENMLQ0CnkJ8M6QHR7t_jpAFYQZWSv9b_KxEBFtCU3frvBx7dqwbmXfemgmxfHF0uwbnQNl3A-Yhqjn5an_a2EP14yce-NqCQ04h463cGBkZO9ESTWP3GvGV7yPdMz25nVzhHhNKBI-npZrqyyroNkxySIntl0xk32s1DMonLA-BQgH3qxdH3Lv5Oh3mwAbDnfF8b3CSkJiWAlUK6cH7YLVRU7b5lRrv37Cq9tbtet2ebvzv8gkmf0sn16J2Bt-MHiQ4P2CkE-QWgNFOTK-QjNimIugsWw63CNPJ3AyNx7ZqcX5lONKNkytvxqXlpCU7m6agDzlHicyWpgcDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3M_DOrLsrEt4-qZ3GDoKABQj7YeJOEE2R5C4Dmy2m38mvRfTt_nUe9orx-WH9bXcjj4MYwQagpOS-RPL2YS75rDB4ffxogCT300mqIVXWzEyx-UXJ024W_DN3gp-th9l6x92LrXMZDYE0PBPH33ninMiVFq8tGPTGhTQoiigZa1Cd7dCU-JSU12RM11vhPOW7pjKZJzWnN1t0JzYqXf92h4RQmXpKXHN8P5TDPxU0E6k_V0AMqsnHE0QbbfC5d1mAO677H_LMOADS0OxG9mn7qaskMeK2m8Nh6l4GAkNZBcfOQ9RXBJQbmAyEJRn658WN4BxSt3OSVApu6ju10b1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6-P3bniim6QpP_V3DkJgyPS6YwY89tAlb7Yjko1gyrdifqw3E0K65kJpUbTWhxadynPLiFpsTlsWgApzgm4LEoo_VLO4x0qEIFCtUYbg71zHPRg5pncLhb8Rolw4iASfZBhKy2MPNIOazycplLVeAhzMSBtBMLaI1ci2TQuP3aHQ5a9WniMtqVsuDjPW5AkcyqoSh9Sk2Gp0Lu431thIT1ganrLzz-4wTC6zo-SJAlbrNBON7jeHfpHkmT_c-eCcNMxWr7Z7eFG4BVbFSrqlgeDmzj0YQwAFG7CmSCchcesnhdElnfi_2FiCKauiZJxizvUWj3n7CVexC122cS0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Haa1X6nrSTAACxAuTmFv3prI8MBb-P0NM7uHP5cbVeMfG3SiVnuSlMKsXdSLgwjT6IetVU_JA_wPtEHmCxUYgE3k1CMmHda0GJ2ZsvD9vxz85DIRZt9UccHiRzQIW5laHwD6O9N8Ipn1SxLpxX5wHwbVnHDr9X_ii6t_6c_VPHKrKZ4smS4F0xPj6SYo18kqqzbCAg_HOJXi_8bAlzDQR-nM32vtS_3eHT2LIFR5KSNA2HulVMyhvNL9BCesLJYhl4bKkmDb1L7c5Jtt8tGl6hWsHJDSOq_mMGw19MZHEzveNy-17RAC-AZf-sAuOj0c8Ctl_X_4zqaMP7hlZf7FcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG8kfvLGbDpV0BXWvjhGjD8QIGuikyHLX5VhqrLKBZiOe3GexmEHcDzuicZynJab1kON8-DXvhLPi7vaT1fOyWLAwjVEFxcNLn8skUL7evzLtPxASchAibkNiLGxTNe_TtJbP0ofaj2COTxtwWHI43enD3CZ_i4V2UYdxNLcXIhyBKMi0sVGoXwBoeTT_-YDaSJ2Ccc5Qv7Udw7zuEdwTPVx55Ama9dHGyBYtrtYTFRsaSRI9On92mLRtqr9XOPkiDdCw3UtdYBgjMnb2eZFDUB8kB0gc7EmRTyJ8dYLpi-6tJGSlXw8WuxqnteWKwlpJvi5iG0jR3-SW-2PctRmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQT9SR9eFpsq0SXUgQqePadmRC7zE7bRFKIV-8NJrYOn2bPC3-r2CqGIjuI24Fsgjq3N_vOu_AwqgAyu-DKJjGGcrCp8refGDtB_HRTH4Z5Kd1WMYZYYAzOinQF3sgY44AgUE7b_UmZMGZLRSUhp6w-FiFLKWtXMm2nuta1v4AkKRH1tO2s2n11WIaUjMSC3MIWuC8IXP5M_gF-go_a1qbDAwJaxH5jQTjhJpjGFWCnAF-jN5ERsMkjz6XI14RPQ_FxvLH2_88u33q10v_hO7XomBI7IgTaOrSiK8DtVoyvKtua2BIEeGg8BV9-6KN0gxITDUJo9UMjbhOJy-kn9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=HCEw25TuyjkkDWq_zF3_xHhnzmgP-R7FYGmtsUBX27a2ZcGqjko5-WsPv0gWyCH3J8I2HTko0RZdk8Ohtaq8wNGDIK5sE9iqLVHY5YGj30WokjqdRRhkBNiRLDwNHYu5FFeLa9zriF9WaXpeE9jmA5QGf8gqnv2P2Sq1fbdIL8T2UDnzzVuc12R_U_whw77J-uEAYuUOwtu9Fd7VgICA8dK5lGXEat8MQN8N1KkYrVRhqbnOacbs2mZX4IuAmHr-6v0iRsiXzE4geHJeMqajZmJMOIV-iqw3I2a3LoTb96SGwKHmvLernuxnhgnEIrURVwyvbk7PJMrt-vEMtzBxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=HCEw25TuyjkkDWq_zF3_xHhnzmgP-R7FYGmtsUBX27a2ZcGqjko5-WsPv0gWyCH3J8I2HTko0RZdk8Ohtaq8wNGDIK5sE9iqLVHY5YGj30WokjqdRRhkBNiRLDwNHYu5FFeLa9zriF9WaXpeE9jmA5QGf8gqnv2P2Sq1fbdIL8T2UDnzzVuc12R_U_whw77J-uEAYuUOwtu9Fd7VgICA8dK5lGXEat8MQN8N1KkYrVRhqbnOacbs2mZX4IuAmHr-6v0iRsiXzE4geHJeMqajZmJMOIV-iqw3I2a3LoTb96SGwKHmvLernuxnhgnEIrURVwyvbk7PJMrt-vEMtzBxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=Ec6bX7waF5DbuEhhEHhip9xy4YNVqRSbewm3mrTSuVZHLQ13Q3Ge-HzlBanEx6La-oPKmxFYVSOQhn4-2j69ru6TROd_P1BBzzgHXBVIGnO4YQwOMO8p1vjX_Tb3qPWCcajsfbBhfDtPuj6gDpXfOHim6AJf2Ord-G5dT7UOtMj-grxaTdPS40F-bZ6-nwvBFCT8OUNdZU5eWtPt0AU8bs_-_6AX9t8Q0x3S0gZPRNr4zuZssO74qe9QcZZUyjziyRbcl7AqYcLTT--VgVzbAafPIV_3yIx0EwVMKxQuNg2Cw4jt2UO1n0PdYXp8P7kAEgeHYOxur6ybBD9XJFoG5xprIAVUSS1493drrzJFJcueK4Ba0WQjm-hiCf2Yb2GZdS9HQC7rbWfC91O1veJN1pXl_vY9aZVT1tkR4ULVUjsW5C8qGi3802AN1CQKhZiNQlAOtL9uuVK8T_KszBayqXkwf8tXQBgiiQ92Jn_rk-I-_U7FPb-aIrNxxvdU8ogSYe_QmcjB9U3Lj3vsPm4cWBQYHJEjGBtqLE3oL_WNnX0HS-_XKwDbLEI_vRRsC3GgYdzSnA04XLmJjF6pK-PNx8vTuaMjgKR6bFh5RTw1x3SjoqTHxHNvGEZhTcq7CrBIXQffUtLhZcuUMG4Im-KaujqxxJFNuVtfqfW-AxrrOps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=Ec6bX7waF5DbuEhhEHhip9xy4YNVqRSbewm3mrTSuVZHLQ13Q3Ge-HzlBanEx6La-oPKmxFYVSOQhn4-2j69ru6TROd_P1BBzzgHXBVIGnO4YQwOMO8p1vjX_Tb3qPWCcajsfbBhfDtPuj6gDpXfOHim6AJf2Ord-G5dT7UOtMj-grxaTdPS40F-bZ6-nwvBFCT8OUNdZU5eWtPt0AU8bs_-_6AX9t8Q0x3S0gZPRNr4zuZssO74qe9QcZZUyjziyRbcl7AqYcLTT--VgVzbAafPIV_3yIx0EwVMKxQuNg2Cw4jt2UO1n0PdYXp8P7kAEgeHYOxur6ybBD9XJFoG5xprIAVUSS1493drrzJFJcueK4Ba0WQjm-hiCf2Yb2GZdS9HQC7rbWfC91O1veJN1pXl_vY9aZVT1tkR4ULVUjsW5C8qGi3802AN1CQKhZiNQlAOtL9uuVK8T_KszBayqXkwf8tXQBgiiQ92Jn_rk-I-_U7FPb-aIrNxxvdU8ogSYe_QmcjB9U3Lj3vsPm4cWBQYHJEjGBtqLE3oL_WNnX0HS-_XKwDbLEI_vRRsC3GgYdzSnA04XLmJjF6pK-PNx8vTuaMjgKR6bFh5RTw1x3SjoqTHxHNvGEZhTcq7CrBIXQffUtLhZcuUMG4Im-KaujqxxJFNuVtfqfW-AxrrOps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=v-rGTDqzMMJfMjy9Zt0NNpKYQB7Y9-prG2iAv7ao5vljArkN3Ell_Z3_NZtmUT9GZRzpSDj6aSinuCC4pQ0jLwPnzR-7OD8XQaYhS6rjkJghpB4IhSgUFKF_8BeehLRG5RuUGrvHtoLHUDCfGsIXKk-yBV1xqTK2k6jTG-5QKnDeQgFB2Zs2bN0p6VXzjjbtp9ijllYCLwWox0RZxYqtpMIbmBiHgPGv1VnOHLzHzfDHjthCov1d5eBLaJcgZJ744KfaxNTMWmOhASRdH1rRJdbtuXhhTdfmVoxX5a2p3IZ-D8ZI4bTCLUTAGgYs-ySM1S0PWhS8AgSsg74__ZgAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=v-rGTDqzMMJfMjy9Zt0NNpKYQB7Y9-prG2iAv7ao5vljArkN3Ell_Z3_NZtmUT9GZRzpSDj6aSinuCC4pQ0jLwPnzR-7OD8XQaYhS6rjkJghpB4IhSgUFKF_8BeehLRG5RuUGrvHtoLHUDCfGsIXKk-yBV1xqTK2k6jTG-5QKnDeQgFB2Zs2bN0p6VXzjjbtp9ijllYCLwWox0RZxYqtpMIbmBiHgPGv1VnOHLzHzfDHjthCov1d5eBLaJcgZJ744KfaxNTMWmOhASRdH1rRJdbtuXhhTdfmVoxX5a2p3IZ-D8ZI4bTCLUTAGgYs-ySM1S0PWhS8AgSsg74__ZgAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vrp3pAJLqAMTIeqsx0dI2NPkXRhbpp-UIiHjiPqmdd1VwJLN04eB4jItzgGe4vqnV5fvePDXHiJed9Tl5nwd5AufKSW-wUxxrGscd-o5Q7caerWolYMKbhsrbaQ-KgubkYiNoxYuGkPOuQE3ss3SmnVn_uTPzsg0spxNlBQLZlbuKeUYreGjKLonHSBLpGjkp0C6ix8BcEWFOtp7_Suwmrc32Mx73_LZReB1O1g7Oj6IZpM5CUPKUGxtyFbZl3UFQg_fMQTEiKRPLiiBo-sI1BUNF8IHM5pNUgM8kZwuxDL5ryvZiNIUE5a15xG1gWmIpZLZKcC5dHlZllV1V6JPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrBLPwvIOJi9OGwME6z6i1zuFNHZRdhqXKhixEKfsTOckvsgQDX4lz5HmF_Vg5KfJZ1gRyE1OpOJUUVwHeQw6CTRLAdWtloLgsloqrtRUthI1YD52J0SaG1T8AVGrNjZzDn_Gq7xSP7HtV73r8XdROvXWSJMl8F5zG6vcU8uCFPU7SYJCTKocegnEdFIEILsG3OkxNkPxILHkH-Ht3n4F-FyofmpDvgYO0KUbUpnylcMyGI42PdxRFvf1Fm6KS-mYfG6Rha9qjcZX-fAjiIAiLRiEPOIGULIefcLgX32HrTfBLjBY1ERtboedLLfnAgCbPqnQDc1SHGwiO1bEkbmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=ksl_6VmHPALn1jclUN-6mqVkoaEQBdPSqZd5B-xN3uaTaf4hkzRxrvaxMiUk-oik58UvUKnrRH5-IEjeQAHacJYeK_sv_L3kbggGEUsak2jpJ2SDmWUJjIs8_8p8e_gIwc0VX1XCMcvebOy3GcfE90aeVI3Si9qwVi-beqys9kHVQYzhvQ-C6VbSVNcAu3UoG3_GfjPj7FCgSmRvaqjxllD4wZ9c5UEUfT7PDA8dbD4HOuNWmeHHT_iRqeLnFyJILWsx8HynRXG-Y9i59nfUN8tVpyB9kw4cxtHfZfMUJiREsMmqUMqVdphMr1qV3-hR_BlCVVyMG6ijOhNzVYra4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=ksl_6VmHPALn1jclUN-6mqVkoaEQBdPSqZd5B-xN3uaTaf4hkzRxrvaxMiUk-oik58UvUKnrRH5-IEjeQAHacJYeK_sv_L3kbggGEUsak2jpJ2SDmWUJjIs8_8p8e_gIwc0VX1XCMcvebOy3GcfE90aeVI3Si9qwVi-beqys9kHVQYzhvQ-C6VbSVNcAu3UoG3_GfjPj7FCgSmRvaqjxllD4wZ9c5UEUfT7PDA8dbD4HOuNWmeHHT_iRqeLnFyJILWsx8HynRXG-Y9i59nfUN8tVpyB9kw4cxtHfZfMUJiREsMmqUMqVdphMr1qV3-hR_BlCVVyMG6ijOhNzVYra4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTaHF_40QgtmlGjWklOFvGXQzlkoCjXfTNs8zsmBZzoYOwlTTOcNbwg3-2o2diqDyhzcPNiDzRV57OsNmzHeZiSv8p1FhlCaJPap3DUPgL9L0mDuZSSpjzatQ2c3AizyaQZjmr549N8IZwMv3sPLH_ZO3JFu7QgeNMk3gSZU6aEWJvRrJbfkcD_DtSjOYcd17qn6frY8J5Ph-tYxVmepy4QK7Rb6nHAXSf0MRKhjXIIyCCDikMHNrZfbMFzU9GVvTz3ihLeZUXp70VqQvdWFT7jaPDiBSxV5Jg0FuD5ljTfzPK2dGhM3hJtNy7a_WJiWv2-XW0KAAMpfzyRiCp8QTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPvB4EMr9VCD9uemRRFuZpakCvp5Dpdj8KTYX2GhVT7_deSCOaIY2uLRwpS2KaZoc0BHX3Au2EdIJVr-9GEXJGO_M4DE_a624oevn3COXdo8rHAIp92teOFi5LgRNcwvuKBZytQiAQU8kOEhkTlYu1wgFPS38-VgRUI3zLVlAxvNlRm9XywNu38097Sce1QtBvRuANaB4PYDTbLZY0dKEkpfJgff778JHoCCX18EnthaYsNXIuB3wltdAnqZ1QXx2ibH-t40zkRIarDS19l81hAhi9pQeexPGxgWsLOFz-FssHJDRZ-y-RlKr3-xonpTIbQKK8IgZd2vGxg4mEwt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMUlKctFii-VAua4vwg3CfG_TAL7oZdw0Bt-tGzm2ouNK15XJNIwerOWb2qRezIs55mfIRml00UE7pHiPaR7S_C_e-6Efz-mizMhKsHmDnaRGnnsrYUXYoDPXT5pgPqsIeZtUrGq-XH4j3gD4YxIoD12xAoQ8Gn6Ovaw8nPkLsGRWjr5gHV9d7Cl33fz0Y57zub-97HsoLliTFjV1mVQDvMBfMFf2704wA_Q3jWbuQ_aGqJfZZeOq5gnJkMOCS-qcS085lWldRy6GS484pH619sCB2DbEKmJVJebowzJUBjqlw2Lx-fWdjpX3UL7ig6RrhmSY5s7Nm3Jvlogf2yxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuKObnosJtHYAopkw_hsAivb5Cd9qnL76Gz4S4EQ6V3qQCJFOm98AmDWX_DAaDg4KtCq8ZV3VBvi8QRltZ9MJndIsBX7nBMo-3iRF6LkVUIynhVgdDF9PaYbghK0-6s1v1SJNIT8ovJ3q70xm-gG5Gz-LALmaBNyDrsqndqmCXOwLpmdrQS9Eq8Ao_HUakR30BS9Wv-aX2YM8KQZ1RSqrk-Oq1uu5CLulpNlNn93llsfR_MeT1Zj6eYLRsN71TdH4vqrkKYdBaGqH5x7p0t-gB9JXxbEpFlBDKAnTEYz9QVuvQ8J6p_pnC81cpNxKeBTy0aoFFc-y_V_X63PAVilvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR7X0YvM4DUWyqCqsmLYryFigRIqEJU-bsxZPmfKfT3L_oXgTo7MeKI8Z6EBsAQtoACDqi6WeY1roEExfrrNaqi4VAAQZSs3RqMZQJ77OCk5GjLhbfQq89-FTVSebY8ZrAEpKloD-ti9MvYrbAMoTXg7jlyMC3OhSTU1LubSjywAZVOO1QF2zS3iChEcDrXq96aJqj-ysGrKG7wSoCpYfZCr8PyYkRhqPWn1FDfSYamNl8IdiVLBVmYj7CjAym1Tu0OFvn-V7k-HQQlLddVT--nJMWebZoVEbITlZbLe8Ts_Ayd18-NrY_BEbcxAi2gLs-E9R8LOgPHJwTa3R3b05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpuRnee3YithfTUe1ZDb5BxfaWW8PdFmanBwyk-raxvYDRRPujA2Q-9x_NEWlHEPa6JjCxAeaOaMZEAKFmpm0BGvkpnwDiCIe8mNsgjMxh5btfCP_uB2rp69PAD0Rbu4hPmxxOb2VC6yn7neUG-Bv5toraqt0WCIx70XlE1uM56f_oWd7EE8ZdD44xG7H6SnSh8Tu9e-vKdOmrHuPjoJMRleULFlPbUs1pGye_GIQFo_BnKcJe0VPUEEtckl69BBijm5INHMDPuls23NLeGOzNtwScIx-zfMbLI64w-PFcAb31db5m_RxZy7WxbwLGji3zD7uN_G-DxLI47lJZH5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vwu6KcMqVRqs646EuzAUDGH1D_bdiZ6fWjUmIj83Sh6PS94dg9AQSGBZeM1GDHc_LwFH3PDuK8JjL3coFooHvv6_uSXZ9khgW2-XHPNp1XtAHrhkzWAoMj5EAv9IflRMHufi1x48_RC_aAMw53A1sZicaN3TjqZAFf_X7YvrXC1-c3iv5658yGh5pfANc7kcutypTvndQje_5BVCXSk_UTq4AILsZDRCSiDsoa3sFGgODckQKSFS0abmMJclIu7aq_lerqBs3nrAZIbw6AoqTruz_YhladLt68lOJyUqaUZpEypsAwGS_Th3TrFp8ksTNtoZw15pRqpmz9RifXiT8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLAUD51X6f8-89xDh4iF4wEBMU5g8RQTF12Y9U0VOWAfYRskAz4Xq2QVsn0LLC7kUOtKzd1pfCIr8wJqPGlu6WyOkk9WPl6lSnK_WfCVmxEhWx64LTS6R3EV1_imGmTt2RRFeX_PdG5Pk-oRvRFxjZHK4p49FhRacyhSbQNYnVkxTU0lCKIdX_SO41v_GYiWfpkG63DeVzJiDWIiMzD6MZOqO_zS6n1n4gG8xUDqhAh-eIfp08ktVZttselpTUOJF77nDkc9VEXLec-tDDaTqZadF3YZ2vnTELqCg-tFMcxSOuyuUrnuwxhoqWkeciU9YcKGhSR-Z0TDIQQsqin_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_0F997NKjdBkPSefGxn8Uhh617F-TcsKg-FNW45dcT8EX9hQqh-gYDBs5baEaGKx_aobO25LApgKaMco1td5JLk3G5xEOOpsAbhlCebizV_V2sUsRCy0FD0BUxjBYAmWagrGdUOT4rpI8O7AjLmqRu_DCM7q49h7cYgVtzmyvQdkzohHHUqjR7boiRuYYqzIWHAUdXX_cGjzmUrxMM5PYS7cJS-pnWHpaM0A6fx0rCT6I1lYEPFSuRY6s7OXV33-8JLaa1t5HWBlVx-yHiDAG9aTk5kBYFAv7YoNXTQUFR5B92H7or5B2Y3PWCUaCgW-NwTMbTDy7Kh1xFXL7KFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=JkOUKlYO78TbBpe2z2uJ6sVOvX6-uctYtDdF-d7-oHPqEb-vKR2k3TOtiVL5C8DHy3HOb414kDfA00hc5ZmPD1SZCNed_pW49gJcwNyiLA6RRzRYbsoN3zvztMTcHwgFHRH463kW04j7GzbkYf4WleEBtdqWgFRfWeRwPd1HDNQICR4bSLUKoWCdwyrvlowh9NWW1YwGEJjvTKbSWCHXvcFsfkl1UEgQVkrlMAQJwQq6vKv__MXZ2eCAMhmxvY21OKJgkO8lw1bczzoukhkIP0y8G2xoQHVQHYPtihmStX9wyKtEu1Ac7tMhWBhijIKCE6D5hiBKfV8rqmoYuitL-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=JkOUKlYO78TbBpe2z2uJ6sVOvX6-uctYtDdF-d7-oHPqEb-vKR2k3TOtiVL5C8DHy3HOb414kDfA00hc5ZmPD1SZCNed_pW49gJcwNyiLA6RRzRYbsoN3zvztMTcHwgFHRH463kW04j7GzbkYf4WleEBtdqWgFRfWeRwPd1HDNQICR4bSLUKoWCdwyrvlowh9NWW1YwGEJjvTKbSWCHXvcFsfkl1UEgQVkrlMAQJwQq6vKv__MXZ2eCAMhmxvY21OKJgkO8lw1bczzoukhkIP0y8G2xoQHVQHYPtihmStX9wyKtEu1Ac7tMhWBhijIKCE6D5hiBKfV8rqmoYuitL-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=v4orQxDJZ6zVQ471WUOeAtwTmVOnX4Ts_MxFDoTDdVj33R0FVZIp7Esol88EHcUpy37Nl5oZm2CwR1ltN2WZqQdZYLh9hSmzDrcPTlhmaBpJ0Hs-1QZj1TfPCQoSS3QQhQmOoFeTypY15PRHJggKdM5ctYPaGSX2k4xYz1AjnmuswHixPBNXgItS_O0IOCPCwYcdE9dwLt3jPKR8noMbkjdXvCcuopss1WCR13g4pT_uo9XRBqpwvGBfjw8nAZvl2FOnmONoTjiKxKdKPb-Y-bqWCxIeGVRTOWcXC4UkW1bcx9-eE-0UgJ-P8__fptHDOX4AzkG8apJ0Ht0Mw18CSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=v4orQxDJZ6zVQ471WUOeAtwTmVOnX4Ts_MxFDoTDdVj33R0FVZIp7Esol88EHcUpy37Nl5oZm2CwR1ltN2WZqQdZYLh9hSmzDrcPTlhmaBpJ0Hs-1QZj1TfPCQoSS3QQhQmOoFeTypY15PRHJggKdM5ctYPaGSX2k4xYz1AjnmuswHixPBNXgItS_O0IOCPCwYcdE9dwLt3jPKR8noMbkjdXvCcuopss1WCR13g4pT_uo9XRBqpwvGBfjw8nAZvl2FOnmONoTjiKxKdKPb-Y-bqWCxIeGVRTOWcXC4UkW1bcx9-eE-0UgJ-P8__fptHDOX4AzkG8apJ0Ht0Mw18CSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQjTjHqa1rRfyB4D9zL16lTCibVznZ7vBjfXQoi5SnmYaNcSeArYjcnFu17fjuADskhNLFnTjdqQdHpkbffMSVTIoV2nzEVBol1zEd2kQT3nTKpZK7GHsvSg-Q75alxy2pcfaxJ2MAzrmOMxqK4II10gy88s5Ne-wkzhN3idkLKFDi1GKxcdv0kSYhPDFHFfn5Srld2VzSrIuZpFF2bzs2haCoB6h2BlyVukn4qc-L6ls9uOVFI8qsaf_JxH4xNq_HnfIWt_YNP27s6glPjZ7k9viOiXYwPS3OeKabcX_gyW413HW1IE5JOjfTHJagyZq2GP06tDbAJcmayNxpBYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9jyrdng5S6bURCWjJhFmV3rajLGYde9GTgPagIsBVfandypCxpHEQhYQQrhYx0k3vW5Po1Wr6Su9RrUijcRmoZPFJvz-FktM0VUmy6upnf7LQk58F_wtYusf70ciob9fSBlNEf8jKna6SYkicwT_aD2mH3s7NUm6Tt8z-lzSWINcQskW0hJ0HJ2ia-WC61qw3MpjBHguKwaBfHtzFje1QAHupLJMVCLljPtg_YS10zuTXTbN01tiCnGy1AnPIERA74Hcb-7nLSZYufn2AJ1ZuR4eYUlXXCRlDHkMhDt1LNiq5ydRG_t6WMTs-_EcWIt7QyxnN973rnc7kNjyFumAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=JFPy3BdiGMnlbpEEqpuT9nSz03quRRAoR9xo67KgwoF2-DjNw4K5JnCupbscUjJeaYX0cyrLa2whDzX8Whxm5dwbv5VCPV5Hx2FnRzqm_gUjC2qNblPVAs5btK_fTpDuhVPBvb_PiFFYx2kvdLQy167LeBLNWYVFNkbYW8GkJn0SB8tbx9n_mggeCmxTRdqZJOL1dhWfWFciIOiIhcMIvbtfu5aKSV3VYBYgOSwkAu1R21GvEdOXmCUJoER93t0pZoeBoMSPzav04JAI62Scq6koX7tQ2j0_Z9ajfHCTxTjeZP9QKIDQzGCXufFbDkB_XGfi98xffP_LHstfruqgEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=JFPy3BdiGMnlbpEEqpuT9nSz03quRRAoR9xo67KgwoF2-DjNw4K5JnCupbscUjJeaYX0cyrLa2whDzX8Whxm5dwbv5VCPV5Hx2FnRzqm_gUjC2qNblPVAs5btK_fTpDuhVPBvb_PiFFYx2kvdLQy167LeBLNWYVFNkbYW8GkJn0SB8tbx9n_mggeCmxTRdqZJOL1dhWfWFciIOiIhcMIvbtfu5aKSV3VYBYgOSwkAu1R21GvEdOXmCUJoER93t0pZoeBoMSPzav04JAI62Scq6koX7tQ2j0_Z9ajfHCTxTjeZP9QKIDQzGCXufFbDkB_XGfi98xffP_LHstfruqgEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=awt9EJLzIBza1wx-ipaFTWFV7gBADCibk2Yo2Ni0FAgvAlZytgl6DYQL0BWHwvLIk4a4BVSIWS77d8tky97QjIKQwLe6N5OFwAq8HX3OzPcdXmzhc8irjqBEeGNh3JpRymvOVgkMbzwloBql66ZD5vuapB4Tlh8NjdQxvTyGyLapCoqozALQmq2Il2I_-cFXanSP1PS2ve0212VZDQb2lMGLEIzv7cof90e1WxsmKjl7KZavlAWHkVUe_bfNGJNGpbmEorB0WMj6xxeqrTLrEgQ9zGzmV1L_zApmOnV0YwVTgs6v3AapLIvAL5AE56-y0r5QmlTw5siCG7a0YwrUFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=awt9EJLzIBza1wx-ipaFTWFV7gBADCibk2Yo2Ni0FAgvAlZytgl6DYQL0BWHwvLIk4a4BVSIWS77d8tky97QjIKQwLe6N5OFwAq8HX3OzPcdXmzhc8irjqBEeGNh3JpRymvOVgkMbzwloBql66ZD5vuapB4Tlh8NjdQxvTyGyLapCoqozALQmq2Il2I_-cFXanSP1PS2ve0212VZDQb2lMGLEIzv7cof90e1WxsmKjl7KZavlAWHkVUe_bfNGJNGpbmEorB0WMj6xxeqrTLrEgQ9zGzmV1L_zApmOnV0YwVTgs6v3AapLIvAL5AE56-y0r5QmlTw5siCG7a0YwrUFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQU2kV9f7TSkHpFmZzkTP6bd2FhypFFIilUfD208oYuHOpTILtWkFNzqKa_7lXgV_MxZjUgIBrn9cQCW4E5R0SugwizBGHzzxaSFdbRJC0Z-tznzknAADLF8fg_l0naa3D6hleWkKnyngoaENZ1w9QHIgOAkZcd9bM63XBWtv6KJ_0mw8riB-HW8eKPaUxzU037kPyAX0n3xgNQDh5dsUgN6g88UEITcLuQqMsqng67dv5tZw6SU6jzEFSuqzYqZ8dgSKBfANSemMn2hwP6hU8quKdhu2-9cxfa8ICZBawZhcy0g5_-lqMjyVQC9i2RTs9vTTb2BNiJ9jnAvmUmNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p562CmIc8YBWi6u4LEkXY4lNFR9BEScQD6kFiu-7BoauFiQ0oPg8638Fkv59C_v5aAAr_jIEEnBpPvCFSJn_E0reLO1XIRSaAM9lDTZmDSfXn-mGIY3xoQs9mmw7_Ny18tQAyEnspqg_MXrR4Ev3lLvUOmGsg8Z-gIqz7NPzOVDYAs015-1TMgju8O4cQ8b3M5nrdLMx6jy7pT3DO3qn_9DDRRF2q3oQPueojFzAgaThZb4853R00AttgTs4GTBMatlzdd6yJubcQ2bcDtofBsAoPbFobM5Tjho485n8bNn1TjUkLpA_oC_2Tntsu9kHCXghC9OLKvvkJNDDmja3Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHg5L_7iD9ivRtEmdb8P7nCGp81RVANNBlOwNjYFjPovs8efWK9nlcM_85PJId5iZLOW-dY2oCQgWhtltwqNWUBy2NOXErDfGOWZEt8zPZ--OJ7IZ7xZCVvb6pNnwuSa3tasw876H0Dq5Cu14k530BSa8i-1d-FsC8qPJNQGpgOVyqPnlql_hd7DyOlulPhH1OBz1rb1EsHtNfBVIzN42buiS60wKJJL16pQA26NrJD0SAdjajZNG5RlsRNmNrtxROCB3BK0KPCH5noE4FROLmJeRlbgmnbIzzk12LLLRRxQTNTmTTiqipxv2mldPUoW6pBfgGHGj0tQRpF6CHV24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dP-swvaOivEq1GVeozd-8U5_uzIsnMC8UpF8PCamRf1BoctuXk35g10CMwjNSayy-_pZwJRaBMCX_cbnI_0qjGjVP21bTxKa1LSh2U5w9C2GF-MA8qkHT-fC1AzaWUpoUIupIzyzpYj6rqcVNXdGR_AfId6hA2oKQBEKAeAO7N_obXSHUPCHqC0lCNZ-H-BWcxWt83vvUvHiuhT1MwYcc5fE98unAcTbKDWjEX462yYM8qYu3OFOG9yskNa9Hhw4I2X3Dcmm0FT0CUC2nn6Wq3eezbfvOpzKOgisa-s9aYvLPDW9s46JS5MLtGQh7_n0hfLxLcNsNlOxmj6F6Wq5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRnd4scVR6p-UJvw4-qRO5L0JL6tZ1shy1FEyPxU0TKOhGkrTLrmZmJsf1EQWuOsZlfSWz19AGsxlKxOQmh0Xd0uLi90li_jT4vDgfFp94KxCKXJCZdrwvs5qr5vu0rlLBQSAfvM2m0N-9lQkHtRdT-wiA0jEKRZ1n_2xBE8LOfaYX3hBetopuDbt8Q8whUllO4I9E72ov2Q1qO-L3VI3tuI4zE8DzP4WMkrAQVmDfGFHebVPGb8Qt-Z6_ko4PwlDKVCjFPyHPKx1lOzMg4EBwZlEWyqbdPuAQGIaCUaTC_FFD3KqtT5nCdqis-Tu66GcPcx4JjlIqziQXJxaIuDbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTVnM7tu5PjMmRVx96Yf0yt4z39wa9Vmk2bW3Xsq6fNiWh2t-T_x2ka4FLsD4Zqv0nlwT2xkbXeDDC3oskZOrLgch47lygOeJq0R6ZFvhTvwvkoe4xy0BTGtDAGkZJOQO-ULKsCraj6q_tAWtczLnsuvDLP3K-rBMpcaI_K-1hcW0CQrWMAcxbqYUSYEQkhboRFxeIVKa4UUkQ1gw5wTZ2zPC7pASn3ikaSnD7O8mJsJGAXslhaTFjHeoLSZPvB_0gpqb8jiq9V7UaP4BpwqUp2OMFNeIu0iO4oRUCLQAEeNCu5GDWTRsBM6bx1v0QGD_2Ro-mpGaAlZucIHr1b8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFvUrkydRXj-i26IvkIVjTghDIyTmKKeXnS_zcfmGIjJtyzqJvC0ySXAgniK8WzXn52oENPED1AcXqT61id2UO0oPsEE4vZHPuNbnMSgzlQ9SpJDkiFBcMv3Ba4Kj3Xt1hHeb6X6-pg9uJmLKGffzDW0e0r82d6AbtqRAbZfGxatvSIDH310k_7LWfXJaVHWR87ux6x4PvC3ETru5DjZtBERfKRqAXmHjoX2wm3_AHi1lb_saAQFs-oflU3PwCPnWsj74xwaGkdYwJNUN45BqHO8boWi-DF8joqE9qNecEuTrFqejr4wOYUac6-T8CmQ2HCSP8IdnjcWQqucpDujtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/beIF71_FcqW-lHQe9XpRqxDEOos1GXizh1mQH9DxxMromyqQr1TE3CvHJvm2I_uOnyGjqWdxvTEmPKoR-0po9u36sC6VV919NsqRKpFQfWuNnOfKIULkEhw72rOF0HvG4n2alkBq0-d3l1GgJ6pbRQXRhfBextyeqj4UrsuIaro-7V-4NUd8TF6UXNJW-LtMjEa1FpApdXVW1Z7BnUntZef2iTwPclW56AKFxpgtse86RxK8-3-HJjf60PDuY3v2ObNAIHOUWsOc4FCYNYG0mkZw33Fmps4gUWCF1QXXiAZEIQB4kvxHl36gbs6_74z0t0CoptkwSXPDYsEJ3aC2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7NJVa19FhjixwtsRwKWrPC7Af8UF_1dYi_DvBpInr2OVMxQ8ZoRlgROI_eiFhUtaI4SAB-QxesCkDtmWxPRNi8421lqEXYwOZ6SgAOHW88DOsS_nFubcmD0b2uxX3WwGyy9BWIso8bEzfoNfr8djHWkKb3PoocCvfF9MUs7-Z_YtZ3IRvc1oIfZJyry8soyFvHQ6K56EnXeqQiCdnTc8jzBlv8s5QKQbcpiN-77COtKG4HM_T3qFU5SpLji5yCM3a80WFaJGP5n02608vCBrivu5Tai6ZZsFv6F9TGOFiVjpG-EyZ6u5rvQNHXyzYoXWLOXHJ4URwa-F2iX2NfiYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
