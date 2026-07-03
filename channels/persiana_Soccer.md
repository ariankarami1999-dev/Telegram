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
<img src="https://cdn4.telesco.pe/file/sY03fOO74UUqHjBwbIYUHnNakDRd_FWvEc3vMxQWpkj93fGTSGMN6vRgHYzTKCR5bZSoPIw45Dcr1iO9XknY9TmLARE62SAylc7G1tQgTTkjPsgZJ7TB9-DrkDfW8ULn3A5SsrC9cijMMOHJ8qRMiYSNOj5P0L58VX2KILWL99yM8BOqIBYqmea4WY-JnYIVUVUW8Pfsz8l1_Cgahn6nF4MRNM_eZu8GV4TvQoiCBs1cs8xGHvObU3hHGWzRDCu2HL421TSTJo16cNhU7Fl4esKuoKTM3yvphoHXKrqxsdmdsxf_H8CvYk_bkmnpMZq0D2t407-vBp2iYBMlr-pLdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 365K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 09:52:45</div>
<hr>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsub6-Ev98OQHQ1hrgZZbFla4PqbUui-tKBUk7fSByeqph6VFGLeITeQpN-RdbiMCpZNNe_Wa6pg4e0k37Ho9DQ4XOgzNet5SgS3xtbbdEyiqPjFYnKCjB6wEi9COKWsZpZmaNYYfV6zk4N8sEbmAc8pB13VJT7344hcWjVUbfIinx7J_8VwJiHdac1n2sOPXuHDRUby-kZe_9AuPycFP-mZfcMan_HylNglruaN1w_jXk-1RxMbiOaLbasDhUUVvBNKLmovGBGHEFF_tAUdh5kfbHUwVUyj9Ut6FiaxnffDBWTij8DpD5AJh2CZvoAQ5AR1J8XduYHmbyrYP7o7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZJH_DdQV4R3BEI8f_1c4yrnsa5qB31rX1HyE7fkniEJQ6fQKlrbE_TaFIREJ30Qz0r2Y7d5dWByGLkLqJQoylJ_FgBpRQSnmI6bEhGrVT1O7mgYHJ6dz8WwIYwDfjEpqkcIPdafPfAvgRdnEoLzpypdikcT-sL6vo-mtPOrYDJ48rJtJCtrr_LHPO2iivrlvARE23qmWF7Hi4JacLowz0mnDW9_Qp1d60vRaVD1v62rFJReWKhbNqAt9R8v9yEO2ERZ1Gnx18XxJNghro0MB_V5-bbMAun74lT2_W3wFpYg5VCO2WWQeRWALRkVhL2VVTBvOHB3ZLv-9KdOI4cu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ao3XEIqoEe35wxzH6olf-SEff9Y83Vcol1-HmlR1DfGRjZYp6Dyed3nlMcqbl7ezzOM6KdB06kzxwSJsqD90PT72lH75k60UhEAt6ZpnjTOTwki_66EJA_z0hDECskDSLRXzqUjHaK5bDLt48xX8Bv8b7xCxzQoHKtfE5ejXADT48o81PnqdNlNqP5NHMli1XAozFVutV9OUWVvEAQ9xaWJHhz2C9CaNlphfjtbQLRyi0IPSD9x__HpPg4TjXOVtZmMzSAr7npERZbGUwMJ-fg8BN7NeHKeZptmL57oI1qPQEEbQdJ7892G42jhTFWQWWyjX4kXcA3QPOrnBmxe8zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7U3ar2gEYMgYUr2F_9mu8gby5XQlnE4KRXeS3XnOniyMt0_Hj-JIc649u7A8GgPtN_joEn1GkFkeo3EvdhD83iFSIRu3RKwajk7WI4TMNqeFfjNR8Mdm10M8K_WWbmFb4Hqdozhed1P_VA-ykY3h5SysRck9gl8Tzf0FouCImGlh7lxZUb7vOSr9HEJmP1AV_K05hxPjZMvuFio4p28eFSkUzOwgAPyTsogZQ2v76v-m7cRO_sedEwHaeLr5AuUfQphQjQjDgZzrsG_lyG2pE1RuNF4x9HuHSmfeM7S5_faskIS4x2SWSW85IRyRbWGK1oiJTdO6du_EzQUc4bCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqhZU6uHNZm2T1QY8glJbp5e2ury-RwlfvCdAebu4WroGSm_SW4FZs0HSiVdZ11fIrI4RxPN4byPr0V05_gcfIewDSN8CGAxGCN7PiLX6YTZk-SFVOvDy57wJnR2CNNfuQj9E_-2EUO_5e3FgM0KEDWlZfl3Lk8zrZpWU63vjf2NmphqwXUqzEOZFk1VaH9qtHeEpeoDaWZB0OMFlNXDiy0-qtV96dAOZafcgLJUKZWZFNKIKFlZV3cL69xwthWJq1e89pxSG3sOI3P9wF_lkEql4_pjc1tiUCg-EnCm0qO3THcJEa1J_H1Lbj47ixqvYg6ZfZWGgTJ3NpvejX4euw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anbSbDZktwwjSk6fK6Tbjpk7ZvTr25LzIuUTsMbFZVKyB_ffy6CnRn9mSOLP408mzumr1Y7-CC22VkNpZBHPbE7UQarrA5nYHNFXBc8iJL5kkynZc_HH5VCD8sLXoOX-eoc7hT0pFXBiRCib7dLY48Z3HdyKO7AzwXwlwXp-sLjAry1dnRCoI9ZLnbHJ_BF7SpWNwEuUjQukizbnO5u5tV0tYbZ2778R2yridNBLzRycgKLuMzx5hVLU-NFPXQiL6TRgRTmx4lLNWgHhCE1Wjlu-IFIgZbnhwoTUtvSBbYz9M75kgqkFhELQ-MWR9mkq9I2yVGLb7ZXsx-39NDzd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swlr9SIaCrOQF4UWOreEPwTOScGoYV4mfQplUWCmdAG6kmQY5eEdMQO6EcTpGBPtJ-LC0PbaHxOE0FFlLD6gZPaug1g_y3p6fCc3bUR8GXZZeGlYEDKyVURd60m_574EXzCtIjmzJViOTvUQTDRAN2IcQ9Cni8joMovyvkK9omDEfPa5O2ot-vLUeHbOkXIkGCLs5XRFxi1QZRPvmQOaGv-NKOnrO3jsY75pfVrJjaSHbs_VpeywgFRrd0nNI1M8r_MWo3BRBJD5UJ9iwIGxL8w8nl4b092Ac4suMa7QNAWbV3ad-oLPXb_06FOQ6uVHMCijc-v58qzAOyRJ-uJJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSszuRasUzDwaXcd5rvbUBMJnSKuIA2bWq4gT-H1VwRo8-y-G29EYc7KrFI-6SgFg2RKNakwr4IudiMMCP2c7b5XE_9EzZ2HV0gD69655uaZX-svIZRh2fe90STIjQ39OvpjoDP5HVsjWUD94_3CyaneU-aXpSBZHw1uh4LV8EvcB8-z6Gkp3xBUsaFBVwwgaU_f_kNXBhwImluhHW2PA0ldOfPuplZRpLGhS9z6WaPJTQBHqwbTmaux5CxwlM2cB1GO2M6v71Xqg1mC-p_lcXH6zPljGQ_giumfqwkWfq8ijVpG2IoHFPJ-toZIqHx_uOsGrlDN-NtyKP1Ft3Bukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJVz-uRXOIpJQpyPxL-v8zgiX3rhUnO8_2FNBgr11YMWQzxpxD7Kq0pMMWbJRbbwflFkgVTXtouOmfQNXhb1AS_rr8eXqXsmLbzYUJWNLokmDIT7lip_MtJPOdfcFqjfqMHd0J3DDDXeo2wYdI-T-4JjTcOzyyuyBCwoKcVpTpWfSwm4zh-l8nid4h2roTa0xzQxH6DqzszDylDgdm4UvY1-zZtGawpXATBQAUpJRSKWUz4Y61brynFr00jUhjEHfsb6rcJ71qjslsxifSUHYG9FQ1WYtzowIUjxpOIK5isBZi8PyPs4FAWzah8KYiXyJJJkSHFmLe_o1cfaUsba2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeHRhZ_TbzB9mfo3nATNy5WYIGpTVR_NagvLv9JoYYLPbpIoq95GKiHi5dm93KDlaDhTejBBW6lZUxhs2ANvZpnfAEwCwcyerHtWlFe9xKHAzU8Fp5OQbdfk-UCAK2vauCOCthWI1bt3dFQY6A3Wy4Gv3ShGtBvIow0MumTIVe34WIoWuSvfwkYHFnzAZ9wuZp0wM6wUFUXLsrVxusSALJoQ6rXgvZNF6aaJ7Ci0dPz8XSYbWk0Fxhwyz-YQ8ooearjphbr1euJFHlpP66o7ROgqr8hmVgjDPkKr8eukPy0d-KVvLAuNvMHhoYdEuw_uFLpiLAQ72DXSsl8HrIHLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUPl_xPmE4s3_gsTHzlprBPaDb46Hzf-90HrhnyA9Nb1NlW4biYe7bcjsH6n8xhkXP_PvNrvoydU_7mPabEXhQLObpRngJUvsOi7SRLRojj-koDUtA8qMigCjkp6MgX4MjPDFMVWGLP1RQTSOw5yBFmyz9Yri1pkvrYL-pgcs9gQ1y03Rp8om_9r1uJ-vYdc_QOaUhPRE7-pU2aLJcJmdzJYT2wzVZxLBbQ2mUtYiVSfSKWuLpdWDLRILLmE5BpARYOHsfqchSfjZm-jiBbtSvZ8dngpkHo1Q1SqjrdGCypLsw6IKz2mgvFESECZ2l4iTXTaaK-ibB1vN52UDRUU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG0CmPIJQJp6frYKO1GYKHVB0IcJ08m_-2oLZt0lcl0BCZ5IkCCxx_KiCMZh29KADo4pGvubY85OVb1OHwcea0lh7YeCxmn557GWRT6j9ftR4XDcYIbh_5066AMqAOcolWxw7rpGuLibT0eYEEGUh7-At67jx9MhYHzo8TZPZyDnFjagg8xM2rUEhHdOND00kxWRr5LEnOrCyt5rFYyGsUjcuwRDAMFhMzKlwKEJObZsssl5C0P0nAXH952V5-4BX17I4kjSm3Zm9eTfQfzIwxT2BODZgHlsMi3hD3INqbBjHkN0QsO3LLG0oKaENaK8H7Y-HrCMIOj-Ic_yK_WjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#پرشیانابت
رو از دست نده
❌
🛍
ازاین‌لحظه به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a11
@betinjabet</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/24833" target="_blank">📅 01:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrAnHaoutHVmpwJGDM0rq71j9A-m3tPPU9HzGk4D55FVGbpV5J8S_nHZ3i8Apq2QDb4lZkC5lsjF9MLSRGA_MBI7uT0BlPMORO_ApJXP01gYOLv73X8KX3_2ElQe-6Tksw9v0Q3HpXgdJbHwIDbyvNmpA6o3u2ZZ4whgM9NIBh3_BRlIOIzq6ApkMOGWXI0NpROFLBl_osqntVCbKgghUu3kYL3t2NtCKUVuZShhIPOBKJvPmsN2Q4Mbh4sadbDt4VgzLgUSH63XXjGGDNXcOXWGBG1_1r22qjsmgFLnvIGHJZ3_8HhwtyE7CwISFussRJVv7XnEFEdKiLLQIkJjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U04UyirZYpSNoUlzbEf6WZ4b6UEcGNPwhMPXyldOOHp1iAz2AqUJzt4A8_ZRGPk3sWxOrJddwHhsVcUaHPjH1xGYgdHXN9thU_JKbKfCT-QsWL1gTA-FAeUM6zs_BKTWU3WLBm_8XTzCvvSO7odWURqRchljUls4_f44LYSiwZm3WhhwD0Tp-ATXB0PB_Uc1-M6lVHy_m2fUbdLwond-bruKLscuBOly3F4r9ZDeJ1vk5IQALuZ6OBVI81kV7_IVJ6qEJ92trob_Tnbdwo5dGNljBng-R0jvV07hfxaJhrL-G3PkOJJxPQ4kHNlUPmQxgtS4wYmsG1IjCqg8pvpGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7X1YSIvNKkMq0pVRarmbwPBMsfLrq8t_eDCa6OfK3cnassKdE5e9rlRAxz2o2cLGdLHVftstXN97lYJdQ_d4fH-Gm51EJr7siwpzxoYSNeLaTjlEaYz_X743WBF-a2oMIlj5VYOBko3NhcQJcdOYp6sta1yMPiDJRklq03QG8ayCC06QTk8zNRgsOuKeW7s5teJZRTpR4_-gNX3547hcLcEGcKPrZS0w6e8E8XApjsb2eYQ7Pb18tab1jRRFR7pgtOrROHf1AGubutUaY6YrCRUE0c6HNm9Q2tIZC8WRUSVr4XVLPytcklJyZ7RJf9UTvRGV669H-iTnzcQ-b4I0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLLNuIuDQuHeA9_cNVA2TU2NzWe7jGhOH997aZta73702QU3nfycN7rlQW-OQIa-N73hI8VEibjrvZqTF-qzfCggJ3N4llda_oCU9fE0li7uoQnNpGXLTTHTyFEZU3QnBNe6oT-4-rCl6zVJ1E1dV48EtK7USY590T0upZabxWSPoqwEKT6jskrepc8TGjlrZIUw4ph3crVm_8rASDak8fHx9fx5UsMTWQ4etbSreph-R8xQ4kQVzDw5bXAFvrmIY7uelY42WHytL4uFIfbvyMF4Ei87_02PI4qfGeRz-1hYluXtyEx3FI1Ak9h6GRO5lYH4CGteDJA1lcShFVM2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic9v7ryG-wSYgI_BHdv7LznsCkMYOBQPnexzB7qk2KVcBZ6r5I554UGQyvYCb11NzafAMWlshMG-Popjg82qcI_pdk0ZrpvONVuhha94cZ8_sfcJ6-OSFa2rtz8mPCo8kXC2Ou_HYNHwOOP8Jn7jFXjV8HIPqdGSzKxEn_EaAxfCAaRoBLPwTKjGizUYh6ttkoizQeL12SL-u77UMlYKF4tR2dBz2rsBpfi1AD9aZ2qJKML-FnmaGsBph9ZpTKDDX8N3o6UYHqI1-0MAiWW8LE4SJ9HkVSg_ArdVTg2ytIJ85bLxZRS6oz9Lm4CWn_-Fs0ctYlyfQ3UmzBchziYPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvnP3TbPIKGfn55KonGhMOkYespjZj_0uirOO_oLMleKBB8jNJ3tp-Viah299LaOebIXs6Mwqnfv5s1ml9uVnlXT7u4bS2ntgAeyGKp4SilkQq8_w3lC77SJb0YZXvhWFuVgkFTu3uQPA6RRBl6wv7G0HqhSYtner5DVsE-5ecTrRD3sFBBK1R0pC0_VTj_qf25mkJ5o37t3CwRn2_bTONBWDo4TEcTc-iB4nra8xAeS4c-FUE-4IH0Ki-SoPmONb8w_3FyH1XTdlu23z8y3SU4BiGxI8d1NNBAy63gneBNyhDvVs6aUmiW58bYaviF8iB-biPhAWWFEzj5KKGfMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdB-I0YVe5p7hQMHTM0GARecNw96Du1NRy9XVtMdYhwJeKBZX_-LAPNvcXaZSfVQxKf6i3xEaZNncowFAq-C2FCMjoHsMPDy_Tbtmb_ehwj1gML6bqjRgUyzcB5V54VrO0XiURD1faSaLqHpy8pEl4pUiiGhih7IF-hGk3lt9rRAWMzhl-ZcgXFt33krifMPdjS_uGuVZt1LrH9l2FyorNf0mgQfLM5YRW6Ki6sJVgBbGtkhQMhFW76zO2lyxQJ8h4KTB9YB1Rq4OK1nbdmoC7OYauuvTkr_DN_vyrJxBFQUMIIrMaMBSK8TZlwsMQx14G-yGngtewyQaNRLEX2oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtDRFVBi9ijMOGpe82BCFVaihCi_UogxchFj78rB_b7oyyOlky65f7HKxt1jtQ-LWZ2V5EhrOtW3iOm5931juyUKvqksN_6GV_0IylZ5_BT09_93aL3hRPbv3DYTFbWd3YfEfq2UxpRY-Vuv025VxdShVUvV3gTNFIaxMuMMyULBb-wVkDxBU2P7rGzpBw4nx5nHDEsT_S-8TWKcm48LQBNDPsKkOvFV9I8LrcVJDqepnVBbuLMhuNdkv1myK2Xqtog7obXXWhWVCQh2RAo2CkVhqA4-G5mFkKIqdyK_RcWyvcZ8Qf7COCU7GRoy_nqdnTTuRWpkvdV3GtvxoF_tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaw3tZvzTc_bI10qtXn1WVEnhEEC0FJVob2Idj9iiX2diBkHvbp0uwZ1IrKJyajtSnO4S2n-FRzkpxfabci4c3ANZT6SoQwoTNh0ffcwYg-cSQ04fXfV-FWat1GD2ifsh-0RfEwTdaiN-d2BbBsGKhpEfywO7HifGFamWoFUL3ZT2KHA6aR5xr5AFYJdmomeGhX4_uCS8ARpXDT-vO1ciPs3gwL98URDOHW4IZ6eFaCaqwRADsmmuBgjLLeoc24VVNj88ZEP7XpPq4SKYC2uZefStv-DjBW4eTB07knwLGX-B5OBodtQv63xkiQcSNuoZWHiaITki2XcPFsoDqWqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gar4xpOZGhJYAuX-f1Gl3-a6AmFFJ73xTSrtu5ZFCE6st3mXDEEmvTkNe-urFvmgUKcmK0NH9SRCqTm1T_5U5oDg8_gCJIdtdmfuDwUqO44e7vd1OprBDZUVFmLPYoTcWjXg7gPqkIlollKo5dCus_q9yoUhZKA-V6-eEHQMbwBoR51j3xWGV9xYaBtefK5YlHAN0o0jDSvWuUPG4a1oI9LYN1VxLaTNXqG_e3R97LbTlDe9pqBh6PGaMKAJks-azs8NxIghTiZ4cAbBdgtdUNEAnz8PdaAXmlKH86V6l03XVlfFl4PuVB8zL8dwdoIHnsAKH5jATEOjaq9igsl1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1utIXsIqGJQmOHephjY5DTB9Vern8dHo0ZHSdCsUP_4gEKx-CLDXiMJ0LdCZ_xz0l2VeEjj6b-EqTxYBQxNpl0a9KdPHNS8xaq5GpszUOQES8gGhQgkGZSYDvuhBc3HBQXj3Iw49SmpRz6rhhUvcXHsj81UHvCFXZ7KyP_MJnSA4_PnRZub1qg61VQ85v9ZMzfQDXQa788yiA3fHiwFOUMDDI2Uup42-f301Z-_NQ_5G74ePfStrHz7qjS0GyD7zrKllR_J22iOltWOS3RjWfTL1h0yt0QLNBohnnS8s0f5LsP4kDWNTNmbnK7EbjCNmDlbTKZzmQhz3D-2ovG7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZWjL4F6a7w1C7byZadK710x_tBzEHlpqcRxhIfX3qXGem82KUbkvBlGYuzNw9Rc81QPjxD-azpL4fFZM88TsRWZgi1vmkpgCcaLG0V673aklQPBzXrKaZKtT6Fmg6yLBd4aOrF3oU0hsO7_-npKpZwUiaxPNJdBfYmNII4heSl4TFGMwD1wMPMVr3rZapDgA5FzwLfFrApman009SooNWGTz1240xGz6T5LwMO-LO0KZrhUZECjWpxnu-81hBslIPxN8zRg9Z-Jh0xOd-FlR6Lp8YWrFTc61t1cX1muE-tfUv0EPYrpBMHny5Ikp1YtnX1SWEzA6GP9bvv3q9O-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkQ9Dl2SQsI39-KChvfrx5CPMexZpTEKVq0XmJ3mGZ05I9IsTfUGkZpTwocYdvUEdVpyOqiFr5ZttV29qsqbBeH-FQFoBkg1m1rERSxqtsCMzfiU0wPnrEt1tTM8vSec5zbEF9X1X037PsiV2pl7OzutpR2nfP6-BNyOPmUhWVm9WLcgoEcOd37wzdf-qLosHlyeR1vG-lPD5MlpeWw0AxYtS1Cu9uiAAu-XTjFMRBqImgnr7nq--1IJyJRJQg0QifchFxwYRgQFOdQ07zHPnUk4ssJsg4K8BHIN1E594wkrQ3rrCaC4pSKDXUnBzPKzn3IPANf4JU715hUTa2Z1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8NiN9iYUa1derQ9tHgxPVCQVEozTv8Jcd3pZ_Dr4Yr1EI41p2WKsLkUSfYD8kpz_xWnkSg_jV6d6E94BnWrS4_82OjFilDeyHLAxrOGBEbef8WDcrWFmVDRiM36pvozBkLf7VpalphfT8VhBoYX1FAb8M29l4_HWAYhhhcz5sh33BnGWUAZT9nmFoOFvWf5p8l4KGgyWEvBYkfvd-gQ4-wSJ2B1c58pIx-g5ySuJezZRrjt65Ix-b2d_goysxFaRDsHJ1fb9lglbQ8r29m-dmwfLfBMKPzZecQ95_o3o5XYAiMGENxuoULZr829pBcmD4kwtTBOOFWnudyXTmTebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnTPB_wMzPuJ_MQdvdGa7EpHH7CN5tOwWTDZ1gmCt5p6oz3zmuikoMKHOG-ev3fv4tUK8LXjHgyihxMXO0BlT2th5o80KTX86tWAXkC-wK3Ya3PipFxfabZFtL8sAaB2AdxIMYTIlOGlgCcw-xIeDJ7JtlsWwhjs4dBTW_N_W0sEs8WgaOE7m05KX0VNKrt_uaxVt_pa9pHJe_hsjYflSt-Xb0w58lzGz63mJRGkiox4kR0KlB7UM6w0QG_38rPYlGpqCkLhWui-Hr4veJGcPvkUKiayKhELyVn4I7puzjWHsJytoyFxFcu18KVOJyfhrml6ZKFRwhhKHDEn24Rgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAIV_epjLki3Z3ZwNaD6KOFfesx86XZasgo32ugs3RhwQ2v6bubwCiV_CScEIHppb2o3Tf4DrJ626S78tp6VvHxHq3oqhl4j0QcG8onkOeXICjmSieTO7C_i6Y1CSXk4MUdu6f2_bt2Ot4C89DQQwzUJ9t0O9QPzdmccdCSC27UIJXY2rYz-LMa0BUdsTGMsnlBh1KKiuD7cFYLNc4xjlSCtlxjdRpTqbOUL6sZDSC1XPb2tTTqmimnWh4PYnF2IxeOYU0I791MaPlJovAzvM3K3WX7H-mRkvugmoUa5YqI3d-cYvJAsmU6u-vLg1k3gCYvCN_casvIdMrH3EB3Fag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q999psRSudkRJR1kdMvRcHNd23DfV3RCXX0eABKxOB4hVVeDfzkyThb8lGlVt-1P1_lVPuqyYCGgEj87Zb6JlRk3qWx-1kVcENR5KcffegOH9MW-jjKlyq9IBTrIlHdCD6_T80XmqLOFEfG6l4rsWqeFuWW5LJWhYKPQVuxS1uy606NG84udkCV2e4I5CI70SHOakF4pmHGLkEa9mweLyVUEw-7Om-yFiVvTtZt29P3nXbmNv1tqEsbZI7z5R2d8wsWimetRUYgeJaiSAVfW2JG_HOsQWuFYUpFiq0HJCtSisRX6N2guA4Fijcfb0ojfUMEFZQzN3GULUZ7l51nllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmhS0D82oGIBpRbFlFJVv8AG04v88UWMkwVQXbkKFjo-bSS5Ff2lR-_KypGfDz_IIRDIEsFtJtMly7lbaHXKeQ96-t0nTV9HWfWl9rDOLnCvxePMIn8WuWC33qThigOk6r6EnEAv9KSCuUQCTtJo7ox5mNtURCTDuxYxkCdIXbWMIG-H3OYDfLIpJzfJdXJcmFgzoOgVYuNexdYvuN_s0H9Vxye3scnJwzFr1GrW1gQiKiX0As_YMP2quwpi34Ja9CXnfg-WS7fNbIW9-n5H7qqbj0kbRHMR6nVyVT-fLnGMHd-NxwOZw__EpaPyfkpe_524A4-Vog5hLGEAhBrcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8infYqaoOLRmwt9-p7VPZes0WJnwHKCOLmUyRcs7J4kIcsVaL2lkSiq5EoanWZX2MICHi8DuA0ZsyzzsqRnCOyZyLeR0Kc2WgyQTTEc9qZZPFoI1PuPpaQpgzC3hOFKXSxLP5ET_jj8eYvNHAbyOT1yuBx_n0bmHYGZjXI1Uj1kPXwONvIN61RhLcFu6usl9CFm4Ks8sbKTh1drZg2Ng1YIwZpsvh9l9skA_H_-4wsvjYlb9qzmCI7gIHLZ1HWEPS0NBAVPJO0j1_6BSxt1ATS6TBGmVqbXo0QwV7xxvaBFTaA7VjRG-DvYAIdAI8wYIDKV4GzmFtnbHmiMrt-JFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULeSItuNl_nbWBCuO9SmGj_69dVb6RHFqAVwSe7NnXQ4MlXRm7cRwO6zjjAXGivUPialwfqZuVK7EAtyxaB15MSoTs5l_igQrM6lGXhPxs2UHD5i45I42ViXFSHaT_Ez-8fffPwOpkJVFwgvNKxn3u0LCOFjcBbXCLkr73XYWH_5B8hP4YSqSwwGTu2Zg27xJtjzJBSx_T0Fw1vkHqqdxqydBX-T-MuMQjeRpbGwIp14ujaLKFI2yek7KGvHBKBmStZx6XFI8NtYHixdZW21H5bpzblZbMSHfxuAvFmHJNZI0tpyrchCjrvQdZoioSAIosLOyrYV_UTnJkCJRf2DiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=QiDg8mFeqsi4p5KdjXwIYlSwW53pPu_DZJVMr8HAfbUh2yNZnQ7B-lP7KwDlgEXAvP9_Qs4pG0s7fAGidSA9ygeH7vDvxav5DtuVElDHmzxcMJQDVMl_yTDjYxhPmgfXc-YKePG6BFdPSwy7UvXRwu6M8K5PnIXXiLgFr6vFbfGx96pKhQ4gRkMoEGoJHoSHOp3aCuo-78f-wLIbOQmJsgY_IO-DCUNdDUVufHDkdP9BwTVXrxbecn_w2UGRj6_J_XNNomb6eh6_VfN-MuW93E4BxS53sKKlYzHmUyhaNAdwVtchY89u5svi3mDmBEbaxiMzs5Eo8ZJn3d_4EB7koA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=QiDg8mFeqsi4p5KdjXwIYlSwW53pPu_DZJVMr8HAfbUh2yNZnQ7B-lP7KwDlgEXAvP9_Qs4pG0s7fAGidSA9ygeH7vDvxav5DtuVElDHmzxcMJQDVMl_yTDjYxhPmgfXc-YKePG6BFdPSwy7UvXRwu6M8K5PnIXXiLgFr6vFbfGx96pKhQ4gRkMoEGoJHoSHOp3aCuo-78f-wLIbOQmJsgY_IO-DCUNdDUVufHDkdP9BwTVXrxbecn_w2UGRj6_J_XNNomb6eh6_VfN-MuW93E4BxS53sKKlYzHmUyhaNAdwVtchY89u5svi3mDmBEbaxiMzs5Eo8ZJn3d_4EB7koA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XABAERqbc_2ykhfqYS4BGF9P-PCgYAOhhUnDtw0Tg7PN2xT7t2th5k8TFgVRPwv5xOpHkrATqBGI3wPDrimCQwZ_1iyVE1XsWWSAOsCk_FUP4iblnJKTJMDRBddRIhFZuE9ipw_aGCRdU0nGIY0oGdS25uw8YZ_pY5K5TRxc8T9uEiQr7I-rg6oRvEZYsvS5fhLDAnvY_8p7m0Q7jIHQ5wEO9Q9lfgKgeF_BJc_a-Adn7aC4SR6UfL3k51Jc2a8pTEus7k2rUfI8O7piuNXUWg7cnRJxyp1LQKHoCa-mZCQMqElpJz9Uj-P2KCFVMcx7DUqLPBjkyPK2dYF60IJp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=vsNehJh2WYWLwc1mMySrZGg6Zxx0cxyKeUSjupCXlcgG7O2OXLEXWCZb8sG1r5V_cQIhnlZznWi9wyCADrRJZtjvcBJlTDcIar3cRtpy1jXvjwABxZJGEhSJ6Ib7Y3kz5UGWZavND6qnmfBnqTx8vjEdUa-4RWd_srpm06WYZnPh5SSv_O44lJzoLc3dcWriUZSx_BH20PkypF1s2rqCeepyJ06XPIb-AjY9lyXzbxXad50xqlKyZSvAOZq8-QLGebAw_ZQMpOZ184Ms23igjFsSvZja1XfpFnB1gscL7w1Aenb7H1B1TJYddqGTVmdYT0v01ANC3Y6t4cnCV01LiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=vsNehJh2WYWLwc1mMySrZGg6Zxx0cxyKeUSjupCXlcgG7O2OXLEXWCZb8sG1r5V_cQIhnlZznWi9wyCADrRJZtjvcBJlTDcIar3cRtpy1jXvjwABxZJGEhSJ6Ib7Y3kz5UGWZavND6qnmfBnqTx8vjEdUa-4RWd_srpm06WYZnPh5SSv_O44lJzoLc3dcWriUZSx_BH20PkypF1s2rqCeepyJ06XPIb-AjY9lyXzbxXad50xqlKyZSvAOZq8-QLGebAw_ZQMpOZ184Ms23igjFsSvZja1XfpFnB1gscL7w1Aenb7H1B1TJYddqGTVmdYT0v01ANC3Y6t4cnCV01LiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAh6wx2ZZhnP6NtEuDHcONUeeFbhCM0r11-wM1dldnqvkbhefM2otFvHwAi-zr085Rqd4-cKAAU0-4hc88Ms8DUrxoiG2C8bGYr9Ub987k7d2nemHp8NxARJiuQZW6xR9VoK-O_uxnbRpZxrzglIKjnEvX6_VMUwkawtBX3T7g0aBWPjvHmVGYs8bTY-I2EBjc26329anxbBeiEgFKUA7ywaNzSAWkcIYgakf5PhNjn9w4IQlcKzb9Js0jONbaUC9m7_nf4XD3euJhFdLz2Hoy_7p46wxEoEI3_132T5O2YiBFEilhOrDBbm1Qk9v6HfaotfVGXK6cXajDAA-kHyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=X-APK2C--05MYV5QIvE087loGmk16eFsIGGZZIg4Jb5v58fNEvrLWc9i9kY3V7yLBcktY0zXcMeR7mfUsP9-KxuDNZhDvX00GHtHKZNseSf9ludgJApracB6MzDT18Tm8GgHYhNKXvtlzigYKDFXyk7tJ2FoPEya_4k69MPea_uOaharPpgOmOlNN1DOjDJm-YJDlBwB09-AKfOYt0VVSpMIbFQrZV1IXW9a_q7r5TT1u5zfyMOH7vq1MQQ9G80ht9qrT1KwfECx9Qo6WVPLG3s9C8nF7g7WzFKLMqe7DZBvvK0CPcLB7j-etbKkpynkTulZbzbTRaDKr1AgVS0llQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=X-APK2C--05MYV5QIvE087loGmk16eFsIGGZZIg4Jb5v58fNEvrLWc9i9kY3V7yLBcktY0zXcMeR7mfUsP9-KxuDNZhDvX00GHtHKZNseSf9ludgJApracB6MzDT18Tm8GgHYhNKXvtlzigYKDFXyk7tJ2FoPEya_4k69MPea_uOaharPpgOmOlNN1DOjDJm-YJDlBwB09-AKfOYt0VVSpMIbFQrZV1IXW9a_q7r5TT1u5zfyMOH7vq1MQQ9G80ht9qrT1KwfECx9Qo6WVPLG3s9C8nF7g7WzFKLMqe7DZBvvK0CPcLB7j-etbKkpynkTulZbzbTRaDKr1AgVS0llQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8E5_5YgEuhJzxV5iWlMSJCePczSq0jenREZFopqKrxxo9xZWlr5sZFf7JpyjPBnfpMycTT0idNgLFs2oUd8h800aiH8-rF0JuCEDHC45EQt8IPY09TGLpD5twu7jFKBsZy55ywmbsjBZK_z46byiceceNHgMB4hb6cbc3ZuPguJHCCt5aa9wto_IrGj4eYgAUttd6yjxlJLuYGVXObVlBfxWpPkGzo-ZhPd25uotOvLWI767lTNO8Uf7H7na-uMIwWoiuHmM2lJyD2_q70xwijX-2AN8geFwX1pv1nOvK202k88PnebWIa7-9ZhxhOWhwmkIUSOHyebrTRa9zqMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OorTkJ0ChEuQMdvaRqu1FajYuajRNTKvNBxBLhEy00oZMClIl4Ty5rYygLYdS3aRgqguXAfT27iHz9kh9HurTuyQPjmBhym_KkXlKvnvSu20uNAGX62lUS1fos0NbI-YXdrD4s3JQYj20mCxElqR8roNFHLFlWNrz61YKm_Do93SaedvwNcyY5_aLqE45qCXaHoQBw1welTu4KBXvXSvpd_8F1yR5-ozWzc4z1Q0RP6Rj_KxD-DhvtuwAOtzc0JxGe-xIAarJKNSAmkHvo5LvsuUaTccIcDEkWSdFM07kAZ9cfuDblut-xfHHKIHMtpheBTN5PWsXVgw1n2v4c9QDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGpz2o485tdIvaLLnCXZDjYhpyRfIr6nWdqnekTNe4MdP0E4inqHszX-31Ck_ALVG0-3ejGS-uZhdOlmrTWZx_ewX_n1PaoQ1eZ8T0fKKENl8NZEC5g-s7Jv5U7EnXT0Xgtdj293LLv-kZMPZGUch9-KpsucwYyfHx7P0oL_sR7wJN869Ieq0UANcwyfqpzWH0RpjraBOMBpSbZuYMLryMgOhocUvwyYA3n2lHmnWT5u_RRUeJJTwOAMLVPYjxnc24Xt2eadgy8-kbb3leaVL3jCnIoAw-pHy1CVAWYB8n0zSlnY9PgwMM41KmZefB_Sq6Xyq3LMy-aFqsSdvIKy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=uXUZvusY6Fcu_S6cWRSX_PdN9AE6wpmXp4PHP2JVcdLyZfC1iG3UTdRLd_dlYA2jOxUDbDR_8TPhNzZGDXcnQj-waKvpGN2FobIGnOAlDyWSHLxD6M7pfIIwxIKxIZK-lVizZ7qKZhg5fHx4u3FmogYPJofbDjSY5cm8Thf4iV0Fcf2edqeNfheDuhTPerbKW2Mol-jXBx2Mr8gEAJNDxk7uRnpGejKACJahxKgps9lfLtZURNIAClk37B97FHhw48-XhPYU5dIV3-4vCproTxu-We8NjQ1Jr431bFSAwQ39T1EF6zPD8AVtrUlUXXZY_9_gFETMWhfjR4umdBRRYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=uXUZvusY6Fcu_S6cWRSX_PdN9AE6wpmXp4PHP2JVcdLyZfC1iG3UTdRLd_dlYA2jOxUDbDR_8TPhNzZGDXcnQj-waKvpGN2FobIGnOAlDyWSHLxD6M7pfIIwxIKxIZK-lVizZ7qKZhg5fHx4u3FmogYPJofbDjSY5cm8Thf4iV0Fcf2edqeNfheDuhTPerbKW2Mol-jXBx2Mr8gEAJNDxk7uRnpGejKACJahxKgps9lfLtZURNIAClk37B97FHhw48-XhPYU5dIV3-4vCproTxu-We8NjQ1Jr431bFSAwQ39T1EF6zPD8AVtrUlUXXZY_9_gFETMWhfjR4umdBRRYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyOz9Q72tfa9bQwz9if06Jw0gEvzyw1kco-Kd0RHKHK8i75JMHSti1p04am7mbt7L-R0Tnc--xFUmmF5q-cyay589xYT5HrgdLgi4j0ya81jQYLMuC7-RK2p7QiZwP9Wm4RhEAXpgMbBv7i_bi0SGcThVpbK0sXs9_bQU944p1TDXKmDPZIdKxmDQj8_jYR9r3tSGk8l5bodqQpXPzlASXwOypJqT2OERjsoynoyX9Q8cSUMPWUG3FPpVcL_mQ34AKieIzhXbXJ9MF9qYkPeUfzylruyTCYIAViDccIjphyArsjvnsElRx6HtIWqi4MSdoZhXGTmS0bkQWJ7G7bkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSWm1rLWdrfy8c5jUeFzGFr5M3EeuWypXJi0RgVMN4BqMmjnMPNFlctBs-Sa8EpZNKT4gdkYFW4LcMHtsxUmjDnEhXoJTQ4a4gHdvDOrjbDyiV8y6KWNogdN26bn8STCGkLXIH_G1W8ujaRDVI7WpGAF8yk7C3ZIwfh1URUOy6-WbdS36mTrmT6Y4T2Z8DwqXHZn_-IEPRXeDIh64ew6Sxkk6xO_r6aUqjrOcF7gycNgXrga5xpyZFrukCXUKc2zRKsSc_2RevEH3SK-RR_i3lhnxRBBo0nKrLtVRFgv4QA9AI9PCfksJR9nrU1FP1WDOBGHXyIyIPK3t6DtWVRlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyIF9AIndP6zHQ5fkqfqjg4pINva7xhBAWNWEpSvj663tkCt82rTnNEtqBBLErcNTyd7w_JslNDG6xuPd42s_ag2-KQrpIZJCjzukhWAdxp6CxhjDESCJswUfWDX1n_hPj8cu46SqFX1Yw1NArbqXomyvLeMy0rHTBqjPHKWvZZbrtgZWaS9DokvZQJ04_q-MKakg4QMsFlMSlww8b8bSYPxAiZUcfBddWYHUHxUOh6LOS_1fwDp6fv93XDx_V_GR15RSXIqlaCvsiMgo5mm8g5JNQ2gG46J6tfT-sbOXtCNWHVIngnRkfBft59yt28_jf_e1DeVd3kPozdtw4MNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIv_ZM_Ud_UWK4DOnabpuVEXu6SYMaddKE-vB4gYKPcnyJmzOg63ZxlDdVjAAgJ8_08pLrULTzwwyA2wB80GWlH12BHNr4FmU0wgSNURX3hu044XeknKlklMDhq0_wnyhqM3xyQNaM07kP-CKdNeOmkVFaFrihfGsQDkjRSyHe-bz9UJZUuBqcKH0_b6Vb0UpEUZXn-XmYUZnqR1XfK_guEwEfQJisqYfSIQ3Bws-05dv14XS0FsUpmWyiaSUlFHC8brBZmIBciuZyXu2OH_tk4vgv_fDoMCS9-gBHEvgebbaz9GAyPhNstLavAaYYrnpsKhx_6jI52s7zWqPC_AdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxsrQsawIN0z0UgtN8I9kotQaJ2TVArVGfxKeJVooNMnADjsiYTkaPX0-cjoYG2r_3PL4_lFVUetEN09HnL2l-2hLx3S2uG4CrOjRzG5NUVTNT0vz3BXHvWFLPFGY7EjwyeFBJ4aTvG_kWYLS5iAkrAFGAQ_sy-EzLhqOTfHHSmiZJFZg8HTiKYX7Rh6mccFlfei2nBxgmxx8KXIEaGAZf-ZM-r5b3rZZImTrIWuXJgk3QNoW5JAFujTy0qhDXwcIm0ZeBoJgy7t3nFTg-tQIXYARHVYz3wEUYtmLHzLKC4GnW1xs7NDF93JtKauPu4Ec4FNmAw2UaLTxYSAF1zNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZT0yeO2ICuXbwAAP0nM2HV0jqVu5aLFDeLC54Z1ZwcOxgP0x2dOh7JoleFGQ8ghMLcIEPufB46f0lLMVMf4xfIKP9DWk80Boz1A0UyJpgpA3wRq5WGrwST92Hyfps0lltWi6TPa2xz4LTsYYQZV1f1cyA1EmNw0WHuhQjxF5H3p8P38e9_oTRqfb4LrMW1PiZ1BdVWva8PMdB_GW0uWuv2NkLCowekUxRv7hNHUZeApzXl4H5LetXekpqJkkgLiF-RigmWQYfmMbMGQs5Z1PSe3qWPrjamBCQz5rQ51_IQrLt8Lpx0zZ9Gn4x8pl71Bkervgc-XlLN4q7NbMFEL1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b48uVRAf4sWn6TgAYWWNiBQRBIE2nqsIhT54MzHcMgFH6MQ5FoebAfogRPwo785QdfU_hHUQFh3lsIHcYRIz8C7Ix6foCP1a74DjZBWfBhAjQROVL3PgqWM6C4ujISNge5Ztqdfa5Del9tZbMlwd2xW-B1O9u66cO2gpN6ARlmjnDxLz51hFO02UbAMMsM24h0Pfl4C1-HtMqi3qtTJc31pzJCrGaGpXtr3IChWr0fzHdsvKSrxLILdLMkTRSpbZds5PCX6Datg83mrudWb-zKEgeFm5TUbQPEexPxQNr7Z47KH5-4NusxkG9Ma1Nt7rcSzRqxiSf3KvSS6Ee6-eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paT8LMaSwLr0keU2qLjZ-iBZ4-emJdU5fsdbH_oL0JDHqoRXxdJFWmzFxSmPkfA_OeWtCzoVnyvsxZKtN4kXzQ8FtjZ6xw0s4x8Mp8ubLTfVXPfn3hmontxvaJT1CQwih8yw8KQ_VDdTFUyUsD5dJMWGJRaCRDAFYeDIYuixagDcXHh6s3IoLtVONOGPwQfpwi-i4Vdv29gc89evf_z7ZXBpHxyTupA2yU_IR7eCGhSrIktOYDKyB5uakJTs634EU37KYub7K_O9ynAA2I3v1pq-C7_w-TGMJvtxEXIaMdK70v-CbNu-hSfjf2vLTSqVlEOAVyPv5wrU9jj1WIbMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwXBAkCijDkBgC1tT7qEtFLm7Ui3wFVdyEtV4h13OeU1jIyWezyPGvCQhmGkdbuWrRiSoQZ6Ir5sBE6VBST5f9zp9sgkJjB18a9QhhRJcWTbeXexgyOUxfg1A_YEEpuw0ADh8OK97Xr2fgzSAliPZFktIHRlNn5_fM18Jk3aKzc6EnisXVIelGgObzorQ7kN6fncVEd8-xUh2WS5wbONIKEPSc0enCxxOFwmCsEDk3QAXoUCoyovlGzNodcNpTFyLKx_NQPcNbwZjIZb62mz6DX2DiHcgw9NT6B6hSKwXe013RPz1R9_9-68yvEFbpZLWzXzMBkaeEA3NJsS-bAi_aSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwXBAkCijDkBgC1tT7qEtFLm7Ui3wFVdyEtV4h13OeU1jIyWezyPGvCQhmGkdbuWrRiSoQZ6Ir5sBE6VBST5f9zp9sgkJjB18a9QhhRJcWTbeXexgyOUxfg1A_YEEpuw0ADh8OK97Xr2fgzSAliPZFktIHRlNn5_fM18Jk3aKzc6EnisXVIelGgObzorQ7kN6fncVEd8-xUh2WS5wbONIKEPSc0enCxxOFwmCsEDk3QAXoUCoyovlGzNodcNpTFyLKx_NQPcNbwZjIZb62mz6DX2DiHcgw9NT6B6hSKwXe013RPz1R9_9-68yvEFbpZLWzXzMBkaeEA3NJsS-bAi_aSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNRACRwwsrWum_28LN9D4WpSOUBP2wzTWLgYUQH8ap1Tzx5OR5e01F23vKvUkjBm6lR97Gcw9R49R6bVIaIP3BO2lsCuCfJGkbZ9cyknFxmsYWvde-eTWTUrl4-t2qAwB9AJEoPTjiSDWb1kKi_Xh49RecPzsp807zUWoOhuj1debNn8nZgNxQkeF4TU0ci5kT3Pa1OQwzUoFxET3kQdXFsOA2c9PlSXg-LVAR9ulvNqs7zDqFbnZBxjO6opQ_CYLkIuE9pGovem1qCL2bfYVaZChrtWtaIxmhsILi7isF9YXLT-DAezSgeXTVRNOSusChGzByDuzqOMn2yFnK5ZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDNfjeYZZQfNtx22SA1ANoj9nMlkkZEnmM2O_dMflwct4AOn97FCspiPF3W4KOAOgJwVd_euD8o5VFq8pUo1eLJNOreMIRw487Kj9SFRIBd0m3mnef1hbqeEOlHjXB7KFMx_xwVU3tj6VcWR4i4JnhzwTv4_uAT7HD7d_6Fg4n8YmcpKf6fxWB7k5yTMWJ_rGCDYSTCT5oX-dSLaaXXvS6prJxJA4elTjX22IFvjYBzE6yEt_5CVs53Za3fFG2YU_dVbDnFkqueG_cclyOXxT6IfxXyo7595MviK5F5hgjKr-QxfYqiS_O5tmqJ2W_TIu2miG_0TPqo3SH9hgCGt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=swmkTaP53XwTSv2btONvOCRq-IdbvQcE-H4JtRHBTnq9HV6kZWtqB3hPX55-L9wCLxQhVkI219KO4WsEfjNpnIJrMa5FX0v1e_DF8XM5Fk-4w9j694s8Ks6iDG_3qwhRHXI2JisqMum_7qmsUS3vL7BmhmR1Z_wybjmyUXY--fn3uDw__XOpR_H-2oxCj_WhN2SgozPjcOtXduuLi2pRjPfXtgukXGx7yFcjjzl5gHwRpL7c3GJDux6qndExkdrlBlTpu1jlEpG7RsXNOBOeWpZk7jJjG4r0DtmxVBYykEi7Sapg4PKa404n2CUur7rhN0P6aN5ot9PeQc-Q3ICP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=swmkTaP53XwTSv2btONvOCRq-IdbvQcE-H4JtRHBTnq9HV6kZWtqB3hPX55-L9wCLxQhVkI219KO4WsEfjNpnIJrMa5FX0v1e_DF8XM5Fk-4w9j694s8Ks6iDG_3qwhRHXI2JisqMum_7qmsUS3vL7BmhmR1Z_wybjmyUXY--fn3uDw__XOpR_H-2oxCj_WhN2SgozPjcOtXduuLi2pRjPfXtgukXGx7yFcjjzl5gHwRpL7c3GJDux6qndExkdrlBlTpu1jlEpG7RsXNOBOeWpZk7jJjG4r0DtmxVBYykEi7Sapg4PKa404n2CUur7rhN0P6aN5ot9PeQc-Q3ICP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSkBltCEy5c4LgnolqjGa18svj-VRoifkvbh-7Dkc7moIfcgFZ-NWuGni-pmfhXy5LZ-xUe32WIzC5ue2Qv12qfZSSi1LSaUZoxCN3eFuTLJNZpS24mUwUXn6MeCq2vpq11qdSEYQgKetkzyZ_r2j2_W0Iwqu-34Ybox18CWuU35bijcY5gict68_DoErr_HUhITy7CMSgD4d23uDJI87sX8waFoJkJiUBpLpQ7rUU90BM5vaJVidVBweXvq7Wl0kqXYDUjyVlL6mV9Uo5_UbiJRZ9VrhMugpCdxX8HXvGLmE_JsvpLIkSPEfRSrnk5RVGlUtdu3145zxSAVsqIYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuMvvztFp9Kzu6AhvU9o1mcczDg4Bs5IGe_w7-Unjwo1BCm6v-FZnUs__fSeuGZadq0jjKdTtNcYJ0rJUIPw6juLb4bXBMhI5W09svUp9zWOIQZjnQmwV3a2dpcYIAPW9oeLNfNemu2FjC_Nap5WS8aZHy0UODd27Jo-AHXHGGgpLzB2sbuA-RV1zO5rYcufnlZZGWSp-lPjtqIyGxniBXC_bAJcKdPcJa2xkeQHbuWm0exJ-9uaHzQi5q-77uYcMvJZdsFHSnPrtsxjsy_3bUFpgPC_fXLLjqLvwbabO-UxNYSZaX28Xc1kVfYU5iPxW72qIvY8Cfo3Ravhvv12rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=u2-zkcLJH5hIabXrE1gtWg3_g8nekr3-ImoUqEZc10rvYd6ug0YjIY44T3hB-H83hbOlv1eUTl1q6UtqTB_k_vitk28HYyzlNW4uZV0IQRhflyD3wVUC0-7f1aQ0NpUySboerF2NzprSj-Y1Orzuqr89albYx9m8b3siGgIEbvryI9I9Bc1Yv6-9B83ocf6OnceyeBVvFuF9y6i838ihZOmLyXjz0XXxGzR14xk8F0rTMAW2LQ5hsG2O8tGP8LCNEoXAzr0VQalMkJ8JzXkqdTRB-1_XRX-yv4xqLG-8d5X-waDgZFp74C-6hVlNThh2ue2V4PedkSZ0jjxu0sgscw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=u2-zkcLJH5hIabXrE1gtWg3_g8nekr3-ImoUqEZc10rvYd6ug0YjIY44T3hB-H83hbOlv1eUTl1q6UtqTB_k_vitk28HYyzlNW4uZV0IQRhflyD3wVUC0-7f1aQ0NpUySboerF2NzprSj-Y1Orzuqr89albYx9m8b3siGgIEbvryI9I9Bc1Yv6-9B83ocf6OnceyeBVvFuF9y6i838ihZOmLyXjz0XXxGzR14xk8F0rTMAW2LQ5hsG2O8tGP8LCNEoXAzr0VQalMkJ8JzXkqdTRB-1_XRX-yv4xqLG-8d5X-waDgZFp74C-6hVlNThh2ue2V4PedkSZ0jjxu0sgscw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNr-r5wJRMrloEUgc7EM5kKYoLRNqx6PL6hqZyADphM6deYf5vjiXgK9gJc_cHe7A9d-vm2TtUrqc4wd0uoTG58KEOq1M_WajU_XCdbYzDn-R-BDb9-iEZHC5l2yzABKpY74MiI5h3L6dHhpX1L34E60LuldluFKxjObdjmn7VOQkdEvnffHcW6yAYU-JdE3FuMzm638Vo580KwV8w5ZoBcY68rktLA9PX4bh1Sr4jFZFqkl8E7zUGUXbyvbWUTABJl6-IJx4oEwN7nMwCD75zdHUtT_YcrwybmYHhLGxs2qM5hpZQ_eY9Vvtav8Dds2e8PdNLk4bRWUmfBd7eKQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=eDZxPxB0kG0pdvrUBNB7J4ih6ow5QIAnGOBYHJeL2qPo7i6EaAapg4v3H-806XL8Efozn8_oQhN4e9J3RZVcyF7rwzjujc3CNysbAjN6gXShWYscHtlXpzuuNYejpOsSnjrWDTANEl-SOxIoSPtCwEPMtcQP4i8ggpFHgUbTFCRRBZaGO_u9UOmvt0IqfkEKObakYthSY2Tx4RA8-gO-u_4ZlhBFhO8HBS_Jznj-3Yjl0wR_k6So4ut2hFoVkaCg_TdySH7FQ-4ZdJONEiMfXU4-MiiD8CMVqQ6f1Xv-R_VmEgSl1fDSVDex3xhmG558ApdV7mNjzUjFppLuKWnybw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=eDZxPxB0kG0pdvrUBNB7J4ih6ow5QIAnGOBYHJeL2qPo7i6EaAapg4v3H-806XL8Efozn8_oQhN4e9J3RZVcyF7rwzjujc3CNysbAjN6gXShWYscHtlXpzuuNYejpOsSnjrWDTANEl-SOxIoSPtCwEPMtcQP4i8ggpFHgUbTFCRRBZaGO_u9UOmvt0IqfkEKObakYthSY2Tx4RA8-gO-u_4ZlhBFhO8HBS_Jznj-3Yjl0wR_k6So4ut2hFoVkaCg_TdySH7FQ-4ZdJONEiMfXU4-MiiD8CMVqQ6f1Xv-R_VmEgSl1fDSVDex3xhmG558ApdV7mNjzUjFppLuKWnybw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAoRvkEGH0TSaFfx2izyCtiN6ajHlYJj01yks8xYPcw1wFoacDsNwPqBlB2KN2fVXEOskiXT_IHqhGbJGpf_nw-kVMDvXLpNsuuQU0e0eXRwAWLcz8TKsEQhMpRDQH8pIT4AEEBQ0VLVaC_HUqnsostCB6_bkfWPhWMuiFXy9aErDlys8C5c-o3ikcEK2ZCOVmEnKLivf46S0r1ZA1QL4bgBKMuiR9TbWpeRPnHTwptW9z5cl1dMrIak1MnFoM03B6BCxXUX4kWjdFbsmco2Pniuzonz3CJV0Je2WvKIOf9aCYp9vInV6K0e8Ad5beytzyFGo2NpOzIKQtd5QNwI-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdtgaDqazBF3QuldCCCBpyzcNWdYC5P8l0rIhkUMpLKxntJoH6SrXsrBGWuSmCTUue5yetJYI8pOh9WtM8iuT7vznVxe_ojdCAjtVg4ZdQ-s2ASDBvS53FS5Shm75xamyIvi4_UljGyGZ8s7Tdx79-x6Fn7-WiZB0qv-3uy3hrfEsW80AOcb8XsYvZpvb6A40pUuR5Rs-3YzfHatj_X2GVX9w5L-lTk0kVnDvmOsZ0xq9nfWcNClGUaMVA1JzYgdkBegYrJ0qEdV9oQ1T6BxTBONj1qHHaca_XjzbUSfZaCNumgBG34eyfnQV6NO2zn3TJfTdkjb5RrfRbxhEJzUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=O9IcQFJirxp25Pczyb4HwpJBwdzlmbA2CIZvfNuNEmvm5JTJKoPaKnhmZldU78tobCTfoFH_xQjDg4d-zUOnoqawVmNxn3JmNPsBLaO5UzJlhPpm0f1Fuyc06qxbbb5uvXkBbW-VafJoT3dlWAxJ-CSJ3jxyGklDVkyVE47xv-Qc1OBZCMoRcgq9BwBRLU2ZUnAwEAIK-x1OpREEqDzLfYthU9dpBC6HjuwEAE5LNUv256IDADssyMes9DIBxbf5QYvqnOHGu1YvjEWW2ReCPskLfM91YiHAUclfzIhIBnCoq36K4R-BHYQqda8GrAWNOYRsROSB9yyphpgbUH9nnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=O9IcQFJirxp25Pczyb4HwpJBwdzlmbA2CIZvfNuNEmvm5JTJKoPaKnhmZldU78tobCTfoFH_xQjDg4d-zUOnoqawVmNxn3JmNPsBLaO5UzJlhPpm0f1Fuyc06qxbbb5uvXkBbW-VafJoT3dlWAxJ-CSJ3jxyGklDVkyVE47xv-Qc1OBZCMoRcgq9BwBRLU2ZUnAwEAIK-x1OpREEqDzLfYthU9dpBC6HjuwEAE5LNUv256IDADssyMes9DIBxbf5QYvqnOHGu1YvjEWW2ReCPskLfM91YiHAUclfzIhIBnCoq36K4R-BHYQqda8GrAWNOYRsROSB9yyphpgbUH9nnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=i7gBmRp5d3al444PyGDUWuwRqdb7R-EGyfwUdkbOy6XGYo3wjG6goxom0Aq-ogp-9INBGRwYtPuzEUnQWZEoFAEjZkPUD0sQyTqdzKd9cGy-0ka1YmqC3iLlGhq2Tq9S8hGOg41_vBIC-sepMadutHnioPp0NtXp5N0MALQIAAPFjG0aUa2vQYOJEfH6zL22XTRM31uw_oCC1bVRVayy_E0HvPlzpRkEup9WGefMjKYi201Z410zy8KADTLjy7F5XwsB8e8mOGqRNxkQ9LndjB5CiddMW_GcoINeKLR9HYAIaBjTt0BXps70ZZ2wp91GoSYYheDV105QP4-jfADAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=i7gBmRp5d3al444PyGDUWuwRqdb7R-EGyfwUdkbOy6XGYo3wjG6goxom0Aq-ogp-9INBGRwYtPuzEUnQWZEoFAEjZkPUD0sQyTqdzKd9cGy-0ka1YmqC3iLlGhq2Tq9S8hGOg41_vBIC-sepMadutHnioPp0NtXp5N0MALQIAAPFjG0aUa2vQYOJEfH6zL22XTRM31uw_oCC1bVRVayy_E0HvPlzpRkEup9WGefMjKYi201Z410zy8KADTLjy7F5XwsB8e8mOGqRNxkQ9LndjB5CiddMW_GcoINeKLR9HYAIaBjTt0BXps70ZZ2wp91GoSYYheDV105QP4-jfADAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnP475EymsljoI5t_3U91CY6tkIrDHhhqk03DBWSQGdbbbw9KYj_bCgrcx5jw0SB7hFFKepHRg_fuAMtXGFshL92deVx1aeOv9_6o2Hc6mvzNPUfyI7xJcnMwYVb4j2MXLpojMMDXhzhdWDCF-B91eCzNgNJnqzfNCc2uaURQZhASHmJCo5tmGlvGMQNXCFG1z_beI5T77tzTG8RMD1Wf06m3A-K6H1Wbc2lsGRbKcaMziXfRQPrlvN34OR3F9zJMIiPUodMO3yNtxjIfv_JWbhxJ16GV3sWcrKLw1WB0LBmZzxv02NjXTwOuUAewVz7joHV2AJ5EBNeZHbqKVsW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJYnWQ5U_yBiRMrYyT-hv8hv4q1PxbpIh_nx-tAw-EwCE3DIXVEi7EJRAXi3GU0cslhRkkVQq6oAW4RyufMpAleZO6X6_sJ6OiEr74vWNdVZ_g_bsLDajIviUzZwHYsKjP734KejdxnxMpsv3go6gR_f7IOCOFhPblO0Eh-WtDoehy6Ze8Oc_X_YTWykUuaNsUXQS3LGumgPaL0S_Lo2_pSQQ78SuLL3pEXuOO52MBL5LwRdKOvnPLVIsaNi-Xr0LCFciCGF9F3id96GO9AyPrgGESHfmCSaWZmLynYyB3ZgRqAnnaSgxpaaHPREID6SodXyOTWBPhgME2Gr6_NMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eenEveUZfjQm8WlD0Zi5RHtfw5PCEBvBQxgHdsqUSJj51cgguZWs6bm0JkE_iT_Xesg5B66gRMueqBwX1miheIunqz9pGG6Go_etbD3cdhXe5839F2u_wka4N8jkbsgbkDy9DM0V5SszG0fReDtvRvBcCLrlGY64PFQWtK9KQRfJ2NRu-zqsoeiT4Q3GLrZAoRHyBtoIq61nJ5PKlmCjikICxcIG5rVLvFGmWwlKrgXD_Zg-qg4q9bKT354W8BHrxsJzhDnW3KxDpmhKw6Iljov_gp8ATuLbi5lSXNIMiUaTkyWqrtKv379D1GrI5LTTFwk5B7EEgMNS7TJw-RQqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=eVOKEyw1uJMGzwBPebEORl6TbRVlU-bIZK5hstmIdpB2Je54n0Z412Wbslt3b9BUPo9Kh7Zl9o2vfjKdNJnSs-YzyGf6ATZXXC5AOhShxZLdEtGVPI4j50oOVS3dSfK7Ql-jC6whV2I_kQDkaDBE64_2boF88k3YczdLccwY5NLRvoVuwQxj9J0gvYd5DbEu6E76_Z2YHzT9YYzXtcWN8EysJs9uMiFgeZshv3Meu50I6RMqhF2STO3mbXnoRnsKqtPI5UoVt8anpombkFpIJ7Nh4h6r4LOT8iQGF9lndOTKJ4r-plpyPfp-r4rn9fVRJuhgV51USlp3_fvBEciB2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=eVOKEyw1uJMGzwBPebEORl6TbRVlU-bIZK5hstmIdpB2Je54n0Z412Wbslt3b9BUPo9Kh7Zl9o2vfjKdNJnSs-YzyGf6ATZXXC5AOhShxZLdEtGVPI4j50oOVS3dSfK7Ql-jC6whV2I_kQDkaDBE64_2boF88k3YczdLccwY5NLRvoVuwQxj9J0gvYd5DbEu6E76_Z2YHzT9YYzXtcWN8EysJs9uMiFgeZshv3Meu50I6RMqhF2STO3mbXnoRnsKqtPI5UoVt8anpombkFpIJ7Nh4h6r4LOT8iQGF9lndOTKJ4r-plpyPfp-r4rn9fVRJuhgV51USlp3_fvBEciB2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLSb4TbavwPizUijaUqFvR2pttvT9LN3RrGk4hyp4sNmNb2EhldEv9s6-1yzN2sc7CHm29oZpQZyXkblXXPmLDC1dP5LHQf5H2Mh4fcDhcSpyNQ5G1QJOGI2wVOnp1jRsUHqxvFzj6MTiUL72_mW7gDCoftFHkROZCRwtmnvLLc1sYroVz9RRETb1Xox5zvt3iFkNg4vf1RbIe3SbFXFG8oNI1fC6vXrF59-KBBdqmS_2dyggqdR_8t0yjQO92oNvfG4j-sEgVYcoDJuPP7FtdCC8E9fKpwDY8-QRiHI3wEHbo8_fdcFLTvLUHhEIPVKTQV839AXT_kNzm_o6oXuSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=ZQ1Ic1-AUS4KrNTV6PUlhl8BrDlBm1d_5QjSOMWawgnDkgom8Y81Y6pBN27iFkshdH7ZoHXrNOxJQA-aQFvtxwZHVprH_-E9B6ag9r_jIbzQ3M531ccHqQJE-N8WA9ZA0XUpGn4V5m3ZfY-AAhsC2U3n2-bhRhTBAHyABJuzKlBgDGp4-ILMomm8S8_k4J1TsNcOz5MUaqifF6v2hg3EMrqiERfgifUkvHdCVFOzh4OkquVdd2ZupRuf6ZvML8n5u5E0ZibMGYp1WdvUFT7Tte08PPFm0jZLP-n7j0Ol8cWwX--J7JdGRVrrx2qqrUXWg1jnTWC6XFCSPQtAjJoPPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=ZQ1Ic1-AUS4KrNTV6PUlhl8BrDlBm1d_5QjSOMWawgnDkgom8Y81Y6pBN27iFkshdH7ZoHXrNOxJQA-aQFvtxwZHVprH_-E9B6ag9r_jIbzQ3M531ccHqQJE-N8WA9ZA0XUpGn4V5m3ZfY-AAhsC2U3n2-bhRhTBAHyABJuzKlBgDGp4-ILMomm8S8_k4J1TsNcOz5MUaqifF6v2hg3EMrqiERfgifUkvHdCVFOzh4OkquVdd2ZupRuf6ZvML8n5u5E0ZibMGYp1WdvUFT7Tte08PPFm0jZLP-n7j0Ol8cWwX--J7JdGRVrrx2qqrUXWg1jnTWC6XFCSPQtAjJoPPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfD_6aD25qVEX7d4SU8lVetb8E0MPdUgN_b8VZ5ou6FCxKWxnug6lIsbH9dB-XSJTkyLIFJoLJWfYlcidq8sQ71x7MTciX5BFp1opzLjX3Ibj615Wb5gng0uhN2OkxQFtGrbZHsukJYCtn8W2b8gYNCA6dvFrAx9GmjUYaGZKP6PeG1FzrIRkLvgVwP4-aj10mz_j_LEX6f9W2sIUvX2UFZ9NfIBxF1FFtm0UmKUYvaW1imL10CX0XmeYz2z6pQWZFFZYQI73U2e2B7xJ68K0LCoBvYla5naBnh8bYwnYJtIQ1zY8lEDIBVOIpHoCRbsTD5mAoZHNMuL9wW6TX24YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=fpUjPbZZz9b35i4JrKirCdTPVAtDFmdA7I48RS5lflSgZxJDnmWOa6WBpAg2OuNlUIqlZz5t8jBDydcd2xaQPy32l6thWhwQXQjpfT72-EuMNhLbJbC2hMKy64e0NEhU10uyXmyBYhY3ZfzQdYoVbV_tuTlZ4IwMcuVX88jp2r88brqpnjvgmxJD-RI3xluKTpSkfme1rYP_dlM10JhMzsNIlCYwg7bWfj7XN_UM1HNWLxyARLCwyvDnw6Pzylfey7tHm6PDQiTT7MepcsII4b0UvcyOwl4KUAkA_gWhYZM7Uqn4KBXTN5O1uRCHOgugxxinvLWNB8JsCRNV5PyLmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=fpUjPbZZz9b35i4JrKirCdTPVAtDFmdA7I48RS5lflSgZxJDnmWOa6WBpAg2OuNlUIqlZz5t8jBDydcd2xaQPy32l6thWhwQXQjpfT72-EuMNhLbJbC2hMKy64e0NEhU10uyXmyBYhY3ZfzQdYoVbV_tuTlZ4IwMcuVX88jp2r88brqpnjvgmxJD-RI3xluKTpSkfme1rYP_dlM10JhMzsNIlCYwg7bWfj7XN_UM1HNWLxyARLCwyvDnw6Pzylfey7tHm6PDQiTT7MepcsII4b0UvcyOwl4KUAkA_gWhYZM7Uqn4KBXTN5O1uRCHOgugxxinvLWNB8JsCRNV5PyLmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFkQJz4O1oh0dDB5KYCWGoHXrP6lFuGYdHkzO2oYfia2OaK5eowt56Xw76pGgdrAB44tp0s8nA5zRKnyZHPKXUgXRMR-526OYTWKvQQVRZLb0wTqjtNUYB77qluzlmOJ3xa4MMpUgIaid7l0JR34R4VWjsjgpx7Rwxe6JdJfuG14v1pRFJfv1ZX93FkVZqMpIvw4WICxyuURZ7jLPEzbDzlzaBjd5Ofo8a4daD1gQfKjI3Gi5Q9QmwizAD2lAqfVrhJsovtD4gLA7r1AFuKQPxLtp0qrlbRUP5HJrjYu4_71JOdH9FJaDgIwYLS9HnKhTYSAMbh1LmvHHQx2mwp2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTHkAnXefd2568UpvdU7nyp8_eNpjEP3cvVzgQ0t-oKcIEsy8m04vOTUuZfbB2RLNJR52d1AFASq8cusoH6JxXhHTj3DV2bEYSajlRm_WGCJ2_jTga8ar7nvkvOReBJ32w4Ml-tuPvloCCloe_wRNODI4pfFvcg5lBBFV4_mA2EnEii4J4jNRACbIXmz9gndD55UeOXiPZyNNQoDk30MhICKrri8iutUEyn4Z6lQMxKGnIKCZGubbUPRYMfXrv25-gMoEFTZHKHsinAw3HRiROKWF324PWvdiLiuvJVfCHv7jNzeJxZNbY4ImTIJZuXxIniLofl0BW5q-UkyYb8SfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoOeapz-vwgosyMXNqMVzZuC3UYZlfAL_eftGW-5NWieOgrm3MeLEJBeu5AGh6HrnbfXdA_aUVzx1ZkB8pDDEXTWfp8X6z-xzhtvGlczk0is9ZeqMPFZw5AcZ0TSOa2GnCMd0eGelA1sGoVX7xM5HpVdwYd8cBFzlowiwXjh0qGb7y-y353RSzntJWNFuHZVYkbAcjIBYCZyADls6qdER5p_sL9hFIlyCt24NwBT05wbld4MtAs1Jioe3HXzvO8NQhOIm6DxiV68B1LoZGvaGUGrXNLgCfuVZ-aS5rVdBA-KvLByR46MLQXvY8tPpboUxtXMMLj-FQmKPWqrQZ3Hgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBfZ1nZtupYrST152VYw20r1_2WLzQelUkMqPiuJbFmWPtspCu0YmuYz04kZ6CL5XCizR-mU4alpn4VknNp32KspNZMbgJL0_J_fZ0dh1ZF5xEPNzifPBcX1VXK-r9FNmljH3ZR3Q2w1Sf2X5NkHSI1zcDKhfQV0EFc_KRwC-mmyOkiuXuduJfeWqoCDw1QzxMYmwyVU3FmBPebPvEwySs3EyLDnbQfStOG_qNLQkoPW6Q98J_vshE9rS7mFRORq_tIj3sBkzI9h8HvaiirzdMXsGNyfDPEIc6mS7jgTQaFicy1Cj-7nfNJCoRYElk_VAiSMWVh3HM0rVu5GRALf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLG8sdXV-v2jMiDRuLbQAe_UQlrlH44qES8JZEOZITaTpZnjj5-nsXayZaVv11pEscyIDLwyc-SxgXfcsaxb4KBZKxuAooGqsCgvd59JhbBTHcX5k0ExlLE4oAcTZG7NMZedkfz0yZp-VR3Ce-vEnsnbnNLTQbZ_UoP6g23svy8wcqPQVF995pEgALwcLJn0PywHsq1xt7RoTuwb5bmVuVNSFj3TIKsKHBsvDEptxEq6ApuhnSWn3hLSpRzBU74HowQ9GWxy3V2iw6VPTp9L-wYlPdWV-lnl8AbEF60IJ8skAKnE2Mg-_v39P_u_T7Ckiuv-EfuzEv5LlEBj6-7XlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=bjevJ2ZdQvNvgyA6nago99bkh9D4N2--kBw5q1iQm83Pl8-FGheIzppXEGBLqp1gwS43f2jj6FzkXXDznmcm155aoAhnnsLTk-jBxecexZBN2Gl2RmtKhbhAGE2QXqCgVgUCyAlr_WZRedfYi1IOVaRO4-Ol3Oh07yMU8QODM8wBr6TMfMNpuzx4YGr6-dpBwjcYuF7R_pM3NQDrl2eds5zmpVVPN7DJ1jlqzc6uNGOTizkLn_Sb479k85sCSVM-3eS962tMDx_SUxTNOQ2WuYORkTyd7vVlHO7_tbpysBMzVdE7sk7JgAUGbrqnCs7wLbEIKdQ8OgT1uwmZW3h4LmWwjB4IATi1r49S8tWVNrqY6qiwvQSQmmsVkOg0_Gaev49H1urxVyIeROdzLHEqeLS8Ka-OPAoSSzFHYCn59Yft6fpByz4fRs1JmZIFbc5RMQFJvTic_NbQiFxdtDzt0CBFEZ7ei-WP_kBKz5_0a5T1HuxgdPj_3W5GK6n7NoAzX6oQ5kSCvZQ_4Gj1AvyG-gIpkwbPhzQHjKJITrbtLLALjQe2t90Dg6ujCMJQaSbaxbUDuiZLc9HM4ePDE3LV5zatAqa30Pdz2lPe_k6jENuN86YzZK7KtX97TSEk-wMDDpndGEpqH0dQNpaOzkOZwCXxLxRI1uxUrQHCWFFf43k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=bjevJ2ZdQvNvgyA6nago99bkh9D4N2--kBw5q1iQm83Pl8-FGheIzppXEGBLqp1gwS43f2jj6FzkXXDznmcm155aoAhnnsLTk-jBxecexZBN2Gl2RmtKhbhAGE2QXqCgVgUCyAlr_WZRedfYi1IOVaRO4-Ol3Oh07yMU8QODM8wBr6TMfMNpuzx4YGr6-dpBwjcYuF7R_pM3NQDrl2eds5zmpVVPN7DJ1jlqzc6uNGOTizkLn_Sb479k85sCSVM-3eS962tMDx_SUxTNOQ2WuYORkTyd7vVlHO7_tbpysBMzVdE7sk7JgAUGbrqnCs7wLbEIKdQ8OgT1uwmZW3h4LmWwjB4IATi1r49S8tWVNrqY6qiwvQSQmmsVkOg0_Gaev49H1urxVyIeROdzLHEqeLS8Ka-OPAoSSzFHYCn59Yft6fpByz4fRs1JmZIFbc5RMQFJvTic_NbQiFxdtDzt0CBFEZ7ei-WP_kBKz5_0a5T1HuxgdPj_3W5GK6n7NoAzX6oQ5kSCvZQ_4Gj1AvyG-gIpkwbPhzQHjKJITrbtLLALjQe2t90Dg6ujCMJQaSbaxbUDuiZLc9HM4ePDE3LV5zatAqa30Pdz2lPe_k6jENuN86YzZK7KtX97TSEk-wMDDpndGEpqH0dQNpaOzkOZwCXxLxRI1uxUrQHCWFFf43k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=FlLfHAxKK1V3bXEnvu2oNHJZtxK4Hshm3f7M-OYS-EBxNTagFzwRtD7yVf5TxFbr9uxj0JV5JozS5chT5tGZYbJcFtErQyUKrSBRLAuX6ji6d56k0yl7F8GN2TEtUSUWyXhaTfofYOFZZSP-XjNNV8flY9WI_p32lDNDzAPOgeEAAgR7YlJNjWsuKUSansbvNIHrc6MXfLsb8uDbZxxtJb9CMbRSlCvr2RKyw7pJI_QM-mOs5ai1kqlpUWTxr_Tg3clJkSLlmzHiCA61gvsgcdPdkP9nlvJN7DC4ucs5g7acMf0WuEhG7Jc9L70TBVTZCBr-dN7vxB2UQMuDDWnZqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=FlLfHAxKK1V3bXEnvu2oNHJZtxK4Hshm3f7M-OYS-EBxNTagFzwRtD7yVf5TxFbr9uxj0JV5JozS5chT5tGZYbJcFtErQyUKrSBRLAuX6ji6d56k0yl7F8GN2TEtUSUWyXhaTfofYOFZZSP-XjNNV8flY9WI_p32lDNDzAPOgeEAAgR7YlJNjWsuKUSansbvNIHrc6MXfLsb8uDbZxxtJb9CMbRSlCvr2RKyw7pJI_QM-mOs5ai1kqlpUWTxr_Tg3clJkSLlmzHiCA61gvsgcdPdkP9nlvJN7DC4ucs5g7acMf0WuEhG7Jc9L70TBVTZCBr-dN7vxB2UQMuDDWnZqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igemv8oY7DE_WyAEl2nFrFCu11mIKxFPwoXdo560DeOKZxIbC2wsdACQ9-_6rbUn3jWTW_NZHBXUC_Qhc2pRKbB0H2A2e6VuIOwF9yDMzznTLwSsd-mo8ApWM0FT_E1w_-N4A1o-6uFZSj-Red-PXZIxIo4-WSuAMH_vW5-1_Os4b8RQVvrZr01NIOvvvZWkBm58VHnWYWCWjFhNJfPoSNlG1fu4niaCfRXrARD5xAiJtMJibOqHugHAJ6l0uPrqBqQhgUQDRmyGuSOeSn7-O1l7IkAAi2wWJRe5jO0eKTGzVsLyxWrxzlzIqPzaEF3egm8Ls84ZGAz6_6hE4Ky1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=RYfvTwRZlrxU6ooBS2ChWebBGJDv3yqc1EfiMYILKyIliLzDSegefSOyPfDpdGsqhjftt_lmV8mRjYPRPZZM7pFsR5y9AcDD9SQAnZg5aMHy8cNl_YWCl1WCYVteLatpjFwe1F5taQSEF5r2DT6gLpI5sUsfe_D_W72mFnhkDxzhf2WXy6FfEeGMk0gB_KhXKHJZHe1qOhNa0etSttgXr9XioSb6muYcjV9eVTGC8Zvf5syT6HhuGvtVO3FTpmEOOaDOoUWyfR9IbTIwlDmawvEc_QkzTmyyWuN1Un2i4KMfiFHTfB76cLOBwBJvm3XXN6MszpToPPKa56qUKxhEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=RYfvTwRZlrxU6ooBS2ChWebBGJDv3yqc1EfiMYILKyIliLzDSegefSOyPfDpdGsqhjftt_lmV8mRjYPRPZZM7pFsR5y9AcDD9SQAnZg5aMHy8cNl_YWCl1WCYVteLatpjFwe1F5taQSEF5r2DT6gLpI5sUsfe_D_W72mFnhkDxzhf2WXy6FfEeGMk0gB_KhXKHJZHe1qOhNa0etSttgXr9XioSb6muYcjV9eVTGC8Zvf5syT6HhuGvtVO3FTpmEOOaDOoUWyfR9IbTIwlDmawvEc_QkzTmyyWuN1Un2i4KMfiFHTfB76cLOBwBJvm3XXN6MszpToPPKa56qUKxhEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=UZb1NuHvocucRpOZRUlVMaCh6dhYG5I8BYRb7tOgiI2czYAMst5gBs81Jpl33No222NPi-fqxZ1UUmFh6Dv80useoKoq9IYC3pXTzt6tBXH4zEwzNmKypcFR00YMTdQ5yiV9NYdeD2bxWSjFJXXUWeIyVUQRTPGRD33tVuqBJjMdrx-J-UQSZmCwS43Zg5_OK_4Ye-Tl4HitRxyp1ty99menOvcic_AjY7_yipYCErfs7kPvycTQdRVJKSmmhbtx6h4tEO14EjNkxd4KABIObm3sY1g1TW7gbuE0dBeQCRZqYKuy1_bCxv9zfjE_-BpqtMBFm6Plkz_4nsaGzFOoyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=UZb1NuHvocucRpOZRUlVMaCh6dhYG5I8BYRb7tOgiI2czYAMst5gBs81Jpl33No222NPi-fqxZ1UUmFh6Dv80useoKoq9IYC3pXTzt6tBXH4zEwzNmKypcFR00YMTdQ5yiV9NYdeD2bxWSjFJXXUWeIyVUQRTPGRD33tVuqBJjMdrx-J-UQSZmCwS43Zg5_OK_4Ye-Tl4HitRxyp1ty99menOvcic_AjY7_yipYCErfs7kPvycTQdRVJKSmmhbtx6h4tEO14EjNkxd4KABIObm3sY1g1TW7gbuE0dBeQCRZqYKuy1_bCxv9zfjE_-BpqtMBFm6Plkz_4nsaGzFOoyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_nTdWtCeDblocBaXe-JZT4O7-Fm616Q_w6Vvw7lqbpwaokP2kaHSmDkx23gBu_g-pWf6M5bSv9iSIJTwB63SGIFqRpNMMBnxswgxRS_Cc3xu5mod3DA4l_3XhjyB93ACtyG2Fc3ur1aJpSSwyHZjp7jXEMM3CnWHbE9XKNmx6tv5hmwClwPpxA2W2tJf6tKWeLqX6j85WR8cTORbdB-5mQhXyIrj4rY8PehVuM5F3OuNB9vWKK5gjx5DWDvHVu86PYK4nDg4DSmkfcp91i6eV47H4fQdIZahXgInVhLdEf3uHabV6IA-MC4pFkRHjLr4gwMcd_iQhKFRQ1_UQxEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryW-rgwovhvPHh_A3TV7-Unp6CteiTmGwHYHixcNAvMwYYAMonX5mBtmQWNj-26RLOOHpVfMAGB42mW-9BWCTRIJ2Jac-AiHrLoOECHvWedN08U1bl7N3QROxjXFqe2Msh11wnXdDiO1rIjpd8AV1HGyroB18Efj3GBF1nvaMwXUx6VRBJL4DXLvKSbQRgLOeq6D8999AuGsICKikDcXuEUbO4BoutYZD2Xu33OFsWjTqKroRaTbvks5ZpND4oKoUvj86vQapO6w8jKqW9vVAup5PGMOQvdpT0veVYxgXWb1oxFvmce9EpCkpmuOvH5Ys5iMDVTBKghF9cyX_2ls1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5Ha8gFjdPlLdvxmTJ_v9ZCpo--BR4hxYzO-0VgPG5Inzh-orzKn8_VeEch_vcyw0yLODzYm1heOvlhhVPM6elKbxMnJ1kRnPdejSPdm8Uqhs05MqKaLr-xJj2qxBf4xyfQwGpPam5Bj6YK4iIQxv0dr-0rtVo8UbmHBo2ABfb8RaFZrhwBdrph0adqzi2fMoyycpnF4ewDpErUbNADlN1RbBeUNbc3F8j7YrHaF1tdspXDs1B3rR50J87Hom-tbPlJwZzEnvH4X2rO2Evkzq2xHjg05fbIhuH4ztsqkfyJGgfOeyFmC2zPUFPbfwtjqDamgJgzQmiVXtfaJ4mFQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6-0Xcp5vVLnaBvK1gRU-QDo6LCqMmVPw9yipqogAg43qVq2oxGahSthGv63FT_KGQs1-Uu7RY43Puvt3gwfGukia3-m4tW7oFGwZHvFXlq3_qp0zxWWAErOtIFbTOHDATFn_LjWQE0gNNeiRma0S5GnpahMG-c9QMc7nDGvh-iNMb_kvmTxX8ImCXYhV55WHujJSLeEe-WaHsDX_kW7Ttoj98-amgXoTtozi2HwzeX0v85KoD67qqwiAxi374LnSONcWToID2t3qqpE_Sv5UR7xn_j4rrR1Fa6cDAnCKt_ysmkDcWieUSK-dX5TC0FQEgYaDFVW7z_MzN600jx1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=u8TzRUMy13AfCJ44gqqWm_8UIhj05G6ggaSalNSM0jqrk61SPEvv0EKZ2jz9iIL_HrzgMganCyrS9JVVV5gtoxZu1ZD4jIy8OyO6Vv6gUfqUuMgAm2f2XOicDsfk2KMMsLtFR_egp_Goy8JCgwgqY7ipxSUF33nXVcWflmM06U4hqh5Bs05JrPYv7Jt8kjnLna7pxH4u7XsGfV62L48Od5R3AdvrUV0j_nH6VBnJMPVUzWgcvfRTJFoI58u5aXAOKN6rnOshNoEE7ehz80tsoIXn-GYjrnF5TkneyLXrhTpldruK8w8_df_DUlg_QcOZ8f9ZKvsBWZ5Y2R5kO_dT1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=u8TzRUMy13AfCJ44gqqWm_8UIhj05G6ggaSalNSM0jqrk61SPEvv0EKZ2jz9iIL_HrzgMganCyrS9JVVV5gtoxZu1ZD4jIy8OyO6Vv6gUfqUuMgAm2f2XOicDsfk2KMMsLtFR_egp_Goy8JCgwgqY7ipxSUF33nXVcWflmM06U4hqh5Bs05JrPYv7Jt8kjnLna7pxH4u7XsGfV62L48Od5R3AdvrUV0j_nH6VBnJMPVUzWgcvfRTJFoI58u5aXAOKN6rnOshNoEE7ehz80tsoIXn-GYjrnF5TkneyLXrhTpldruK8w8_df_DUlg_QcOZ8f9ZKvsBWZ5Y2R5kO_dT1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMdsVOixFOiYE5goWbr6LpONonCUExVEC2W8-U4XBG9GXRTDKqkyee2IbBmFg5tF6qhPcuJLQNGBycR6Co_O-C1ZqhQ3Iix3M9YPQWtB3dIDoQf7QpAos1VMbAke-DATsclEyiWYZ1WhK49XKI0lqbjc9vQMgn_Dqx3nJkL4xi40Wo9-0vvtsvE679qXmpugdQ439YIm4JaegcVGEadLHWvGcotmOYDkXc9bYa-m00Yx0nd3O0rJ1KNxAxTp4-soU1Zckjqq3sSu_DIy2_kkDANVkGnV616JZHMeMedD3MYW08Hn1tAJE5950rzgh9McfvsQ0MA4In7YvirI_PgulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9W_hguOoUycNvH7bWeUnmpkva3_zGUU48hkB6yWGoN84BUeBl6_cmAxfNvhwZK8De4F93S-cnsa1MpQFqaNfJbsnGper3Kzl69mkKU5Ei7_xZFbmBO63WtqeE6IhxX8FrF3BwwKjQYWxh9TIA9UkDN4v3_UpfRl3ncTCFFZsHWNtIPF-1ReJzTWvwvPhktFXrdEZqJQwWqvc4lMzfoEyRVzHEIlQTWkI2q1B8IrG9WBNrOHgUIjzENRyo2W1gWLy75ohhDpgtx-OTG-4SF8HvCoORePk0SK-jKSUeEnimBox-nz_6-iZqqYnHmzMNm-Hn1JgKXSJBrFDs0u_rcZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=LlYQ3QKtGNfTGHNdYUoNXnl9qRuNBczSFwhHCyaYW2hDQhL2z1jPLzt2xoslUx0gg-tSVn7r2nCcRfISFQqzS_3UXBN7DgJL3zRqmvCcDjjU2Ts-lGe2papHm3iLA-1-wRij8MgP-ccO4QB7xB26Es1cHDcvFAk58J3BGyxSEkZyuYU6vl2Vqe0Psemk8juCC9YdgdSrPgq9yejYQBiNQ67KdteaBdQ1qPoIfctc23gKFYmb5Q3KWQ2ViiyyUYudEUkmJl2xkcGYTqtav2XSzJ2wOpa4_WcRZEcp0etbSvnOGwFfqcjIS7o72vwmEjarrwB0Qdr37cHlXee4Qmashw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=LlYQ3QKtGNfTGHNdYUoNXnl9qRuNBczSFwhHCyaYW2hDQhL2z1jPLzt2xoslUx0gg-tSVn7r2nCcRfISFQqzS_3UXBN7DgJL3zRqmvCcDjjU2Ts-lGe2papHm3iLA-1-wRij8MgP-ccO4QB7xB26Es1cHDcvFAk58J3BGyxSEkZyuYU6vl2Vqe0Psemk8juCC9YdgdSrPgq9yejYQBiNQ67KdteaBdQ1qPoIfctc23gKFYmb5Q3KWQ2ViiyyUYudEUkmJl2xkcGYTqtav2XSzJ2wOpa4_WcRZEcp0etbSvnOGwFfqcjIS7o72vwmEjarrwB0Qdr37cHlXee4Qmashw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGi19OUNwtru449uWkvSCeRtg1M1J1rGsHN0dwM4MTtyehwEAvqT5DFB7UraP1f1d0UzYQTGNzu3mRe1IfJTP51Fg_CAzZbmPbE-2I5ZFuaXpuDUB90i8j-gYxpJA4ncYfBgc-jK19ZwOVZabrMhvkl2Ki8aNeNQmrxevU4Wc0ioEUPvSUDKHs_9fAMiJ4QZyrzJPQm9_9nKaulptKP5-w0iO5RZ5fdyD_V6BaDN8GuzpLTsDqcHXBQO0BIc46eIjWqJbDCrEFpxfuxQGKiVdEL7G3206xDG6XCga1D2TMl3sfnyADx_4sS2BiH4x1lzhYZuYCqsWptqYKNDkUsPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKOr8b4mYgdzxl8p56T9lL96oDXczGN0AW_EoVb04S-3tqaKQy3WroEFhhtEHnq8Le2vIqRVvUfS56SjM8otRj6DqZJNdP1YDTR59zX0cKm-tYFuPfQGuPFRzEnyZrGdAn412S5fWRxGyjJaZ8aMFSDilqjxB1lPx0u5yQ4loyBjzYAA8In0wqLSG9Vf6RcTpoIk9b1eW-YzcqgXiowjVsTSHnh_85TOjVHsPE8r8BAM8ZAuYQXlP8C006zpwdO9WSfDXGQ-EVhzAV4sCwFDC8BDwrbYqkVrED4Lz-PPVHubrRSOpXo1QpM-2oKDSDzfyWz9ErFYDNeFBhyZhn9ZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyqyN11NPkeQPxfeOBTNmLfQvsQDSEqMnzMLK0u7chCio47bChvjLGTu03JfdOn9l8ggwu15LGf7d4V8X7DWKOYkfC-I5uH93He-h9xcyiDFeT90ZzigmMznXar1RbcNrMd0OS-UneILXLmt10UkdebwIcpBYQlLSob9F05IOaE634tnZO9nuG460-RKcFLmW6XnK95gCjKH-m-fiUKk4kELKLqHHWRpwNVZRL7lDyCWV4lvLN5V8FEr4_oPzynC5Jf1EkKUY1HdGmvdU78X2BHrQyTj30uZitVXNE4AmByGLcfsbNkwZynGTC5JkWmVQbqfdyVYyB8iowFVPVbm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxAQCqfRdauxAr1nCSK7kcXUsyhq-qNOckrzdL62_GKTPn5AgUvaR3WNCnXSyL61dAgQSYCALmL2Wkp4XISRvR1NExDFcAr3_4HfNolzMeZfx2fJW4aSyTEGpCG9DXhZZ0PqGrWATvfdlvROMaxQ-ueHurtP7iDelfl42UxWA8ogUR2tacAkr0ETIK0KcSue3fFrImvkxiV2oifhO88XRJHNwb7uHLB5jnSQs7_9YhHJ69IN15B-C4q7TxBdqJb9fG71owMzV1wPa8hZ8uMwL5HdjA3n3CYiifrAynazizLB9p6-QThPBl94kGjtUYPzu413AsVhQK7wBrx93bJKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=rZWKMctNEOnxGGO0tosMbS2rm7K7stBu-5u8a4-QOGYfETpRldCw5dU243XwbdvMSF1K2TYKsopKqHKyflkqjOBsoA5xbRqhoIr77bvOvhGygnZOfZ0ArO202CCV5M5iuSAJtXGSDfdNCMSDFo_LaaZcOceIgGXk0hb2Mv12GKJHyQWuBGabMPgEuPI5Dvdt6xkxUKHWKvuM-O6C-WcSHrNvahFzO1GseXolluGoBQ29YxzZQsm1buM3Rqim8OdcZe6Lrrf9eMUi_0hMO5lB3qwVBa-vZO4YwdeXl43ypsGUb9CSu30fRZi5e2JIG0iDAZC5OEv_oDhp6z5sA5A2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=rZWKMctNEOnxGGO0tosMbS2rm7K7stBu-5u8a4-QOGYfETpRldCw5dU243XwbdvMSF1K2TYKsopKqHKyflkqjOBsoA5xbRqhoIr77bvOvhGygnZOfZ0ArO202CCV5M5iuSAJtXGSDfdNCMSDFo_LaaZcOceIgGXk0hb2Mv12GKJHyQWuBGabMPgEuPI5Dvdt6xkxUKHWKvuM-O6C-WcSHrNvahFzO1GseXolluGoBQ29YxzZQsm1buM3Rqim8OdcZe6Lrrf9eMUi_0hMO5lB3qwVBa-vZO4YwdeXl43ypsGUb9CSu30fRZi5e2JIG0iDAZC5OEv_oDhp6z5sA5A2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=FrfU2mr2R64Fc9nLX-qwrLX-PReQIBj242R1VhA10RuQZvf4z6FSRR7mavavO2rB8k77oZabFdPDaSyo2_41-Nw5jyBK2tfilslg1XyH_a0s03rRODvYGzIro-lnNoQu_ejAoAg2C5Bv6YRsoBLgG0zI2nJrSl9DKtPj2eJ_p15Pf73Winr-51NIqrJI0xYJAUskkMIpKGLLzSjmDlSKdzFJ57PPFA7_2qY6uoQbQ4ra7kc1gh_HZ6quD9ONgUjGqsWjh8ReeahsVeu2ageVHQRQLV4cAcfDYHboZpOiM5IM6ZQy-s1ufLUdmwHIW3enYTl0gfSP9oYptYlw1kqWWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=FrfU2mr2R64Fc9nLX-qwrLX-PReQIBj242R1VhA10RuQZvf4z6FSRR7mavavO2rB8k77oZabFdPDaSyo2_41-Nw5jyBK2tfilslg1XyH_a0s03rRODvYGzIro-lnNoQu_ejAoAg2C5Bv6YRsoBLgG0zI2nJrSl9DKtPj2eJ_p15Pf73Winr-51NIqrJI0xYJAUskkMIpKGLLzSjmDlSKdzFJ57PPFA7_2qY6uoQbQ4ra7kc1gh_HZ6quD9ONgUjGqsWjh8ReeahsVeu2ageVHQRQLV4cAcfDYHboZpOiM5IM6ZQy-s1ufLUdmwHIW3enYTl0gfSP9oYptYlw1kqWWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
