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
<img src="https://cdn4.telesco.pe/file/i8YK43z2eXTE5KeXgvS0kEYH8oPa8dGmhvM80gb9P29YPlqClGS_c4-i2J0OfNveJcQ7c59vgN8dWHk7aDJnyVQ4mZFyKX1QXt9paeD83s0lrfBdTw_--B5dOr3VWZa1Yc2722IYxri-xn8KqqBu3D1Tcz4vZ4UUt6a_v4a0xzXmWhYeuZ_j3YZ-ChAeyrgzKOvBVBzEeR5baLietXKMi_Zs3BjZqU6oQtpDrendq0UHLfoLDep_yqjGSEFjW92ofFrETUnJaKPwIMs6lSbabt4Hgb6XVvJk14KQee_PfQRVomAycKTMpFpPBfG-DTRCp2ZILHOqP6OvjD2P4jMsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 919K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 08:01:41</div>
<hr>

<div class="tg-post" id="msg-133642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133642" target="_blank">📅 04:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133638">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-1L2PB_hOU6Q9tzL0Jm8N9T0nB_x17oO-AZUU5WjEjMtts53xItQvcJcBsK5zI9AYsFUKYiKL9YROA98HtG8DBHTAW09yR41VfDXRU5b3sPy4RozH4Uegg5dBIOn-RxCYTayfcsKdkRS4es2onDX24j6wObWWu8sNs6la6TlLtdUtmlGvWfeFGxXrKZDL4YXyEcGSZzOF8Ybgyl9SeiBtt-sa2ufx7ekUvgV98XaN8EfNYOAZIPQCB0imaOA04DsWnLmeODQimKOhANISpbpbTlQLjhgk2ZmXx74pzdNJ7Q4WfkZGA78Ie_M95u9kcFJFsCjrZzPqLKCFt5Hwg4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsi49wdMK9hRRB7QOd0So41GNUo9PCZIoxDbUnB6G3pUurIQ6gGTDVaH_AN9OxnP0PAKhcm3UlBFytAT0qtX2M72zb8WrnEh7_T05UQiU79365OKpeOyGtibeiASkccTxZ7uka4XunX8RBf-Ib643fQepyx5wYyyFtUkgPrYcE_1Hjghl6qYtE-7Vdb3lYfrbSL855dnG5U0EKx4lmMKxalALGfugbiS8Upd8M8FoF1clg8jZq-WrvQK_0xfoWfa_hccmQ3YQLGh4LMsPVwxhQwo6UAUFKqEmWEfsNRB7gNI6RKOV1242XYAKcnLP0zrN0g7AsOjyj8u-2yIlnTuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxyD6jTdBa6huPYl78mpZrLBpDwTWuoPDXqFhhMk5sZnr_zDGN9QemOKuPHEZ6e9VH3nhVJDnl1waNvNkF7SrleNnhDDm80K9rWku1MU3O_UsVP2vdmpwussY5dvLDTEl0QrpD74FjDTuax0eGJoz87ZPv0Q83lU0VRMOcrSak3Td--BgvPV6gJ7Ob5mLUG8HpMTs6EJAM2tpX7voWMvGRZvKjqN2O9hCScKwlCVVgl7tHXquFjvAtlAkhdNoYLGKSzsOwCMpAAG-PNqCfS1l28DzNuiaxlbL4WWt5QqJr22GnxJvG0aXbxwo_9axjF7ciwKwPmegyvaeDN_CRAdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6odDisTAwp-Qmz9bOIcLguqP5HNSyDswkfv_c8MGnBU6Q7iUrf-8yqIDTOlNCpzv4z2JaN5GYVIDE1bOb6rvMuXKrHRbVrcPM1veFI9_vn9BERjkBb0cOxt85-DutPjCp6qfZte-WNw1KaEG4fsmKAKH4Lm_K82EzkODpY1CfG0scOgEu11H1RMspKhPZKPo63tBM8vEOEvG67Eih6-D6xRsxYgb5Rfnt_ZpM4tg6d6Se6TKP-peTHMLo-H1YsJYMXTsYCLGPr8-gs-HOyfuC3PI1opbN1giD4NqMgY1G6MvYARLZiGBeRsu9otard9_0wV6rq4xD5Qx_74kH0K2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگری از شلیک موشکهای سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/133638" target="_blank">📅 04:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133637">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فعال شدن پدافند اردن و صدای انفجار در آسمان این کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133637" target="_blank">📅 04:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133635">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qYdSE_MttnKoF1P6gDtI169-q2lO0bTkwFAiVW03VcVWlHF7G6rHHI4OzRWUMdvCeGydAy2-3n3eRDO3HnU-ZPItrue0gDnTRJiH5h-_li3JcZdP8qVdd9dO24OiQBynJ4gE8PYRVzPiAIyV0BXNUWVoAO2rY3hVvRQo-ZQD_4yZDf7zXZY-rJJWm9A_Dkk_tKb3GzHFtEWpieGQB3scgndOhZo7IQW2jHN43xQFg7em5lOgX9CbQKMQGl0VVPqskH425k6ludmPx96oOEDNJO80kTCRghI332tSBMwORZ9QM_qXzIGWuCaFtVIjQjYiXEMcLOsTfVwJRK09kF_BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_jxFE34kYopIc1TEPyQ2IC9dHHbLdOQ_jq6ESv1xD4YH-3-E1B8hcOpJqkmh0XEXBECTRk7b955EFmxJO7-LXqMPWlgZeHFFm38ARnfQlA-zQHEunuEHoDxkfi-zmmZ2kkammMX-ERdq3tLoQoCqringatlotdW8yAK1jSbbBRe9cB4HNKNp_FZHEMTgI-nV9IDntJnsSR7MT7u843tWhWD_iqAP5aXduwOIWzveKQnw8eVMtVKoqx-oNKH_tCBWRRUfKBqPS3Z5pQ40woPkWLzGaLvuoelSuaAcGhGAld6DLrcwjoTGwkzpHjKaRSiRqumOkbTecwiimW5dD2J4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
از خمین هم موشک شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133635" target="_blank">📅 04:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133634">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh0q1daGIoto5UJXQ63GWAq_dP8MQZsoT_ngf-vigwixMYKo7dpOxk7rP9qEdtLigAZU77L64p9jeQIp--RFZ8wTJRUb44zpIuAPXZNqtvk7hS2g4rYprQyKsh01onDUXmInFrhmfjCuLz7mF0b5ynqYPu2ad7GLouO_n9h6sld1wBYQtD77wMIVzurYuVsdm4p6cpWjnun-3hUtoGS6G4Hs0mdTATYVNzYq1tJ-aNc0nbDyYnfVW_oSbFw-v9WZi11s7-cedTpkGnVowRtgLuklVLMIWpt1_UUOisXT_taYX8UUw7og-it7iR5Pgmm6HmqWryTL3cIog-6xAlhizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ پیت هگستث:
خداحافظ، لیندزی گراهام.
یک قهرمان بی‌پشیمانی برای ارتش ما، کادر نظامی ما و کشور ما. یک میهن‌پرست تا در اعماق وجودش. او از خط مقدم رهبری کرد، هم در لباس نظامی و هم در سنا. افتخار می‌کنم که او را به مدت دو دهه می‌شناختم.
کار خوب انجام شد سرگرد، از اینجا مراقب هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133634" target="_blank">📅 04:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133633">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c43c2d219.mp4?token=r9OEG-3IGlsfzPEE8JOXKhHITliXJLYaExmtv4BJSOsR8tsne_SOsadQVkNR41_iq9jJQDfR56fD4Pvm74koIMfDt-dMexXWFTVb6MmT3zIiD7siXYkfiHtbX-3EJsRB3OI8FEvGELTuL9iTHHr0bnBIjDXjMCaod7CKCnie_ysOCehBFiAujU9midwFWx7puS8f2epr4MoggqcQkGItxE9GKDRmFhLGAXnmhI-C28Cd3mdCft3mf5G-T2Kp446ZFEgPlnTv497D7wRrZSwjgV2Q-A9Wf4kN2krZ02T0BCBHJA0gRG2XzSI-GgeR2ClG3z8YrZ7yiU4TEPlrUS0AtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c43c2d219.mp4?token=r9OEG-3IGlsfzPEE8JOXKhHITliXJLYaExmtv4BJSOsR8tsne_SOsadQVkNR41_iq9jJQDfR56fD4Pvm74koIMfDt-dMexXWFTVb6MmT3zIiD7siXYkfiHtbX-3EJsRB3OI8FEvGELTuL9iTHHr0bnBIjDXjMCaod7CKCnie_ysOCehBFiAujU9midwFWx7puS8f2epr4MoggqcQkGItxE9GKDRmFhLGAXnmhI-C28Cd3mdCft3mf5G-T2Kp446ZFEgPlnTv497D7wRrZSwjgV2Q-A9Wf4kN2krZ02T0BCBHJA0gRG2XzSI-GgeR2ClG3z8YrZ7yiU4TEPlrUS0AtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی کاربران/ زنجان، سه موشک فرستادن یکیش افتاد نزدیک یه روستا خودمون
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133633" target="_blank">📅 04:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b8eec877.mp4?token=hT68DHQH16PFtfSmkeQqRpaZ46ufCuq_ozbsD1j7WiQ1TYu3Eza1beC22noVKSyxZQaF9k2CCsG2T9Z0SfbMtJbDbHvL14UnNb5ALu83LYB0ew3fE7DZXkTiIwD4IzV63DRLz0mODBCfDY4YL_gak95NN1OIkDkXn1k9pt-Ap3x6InPOLwGYn18Ua2z-NM45AzCmn0D2zuh5tcPWAqEsaTPGpfsEC7ER-KfgMjt78_Dt6q88BbzbfCYIWZid4zuQm08nhf4gzjfVIqcp1X_e_YBqgtEoZHwTBhdwpZaoIkr5Nr0bAtbP38L_bPeYH7cd9y_lxbq_c45JCc-caqf2Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b8eec877.mp4?token=hT68DHQH16PFtfSmkeQqRpaZ46ufCuq_ozbsD1j7WiQ1TYu3Eza1beC22noVKSyxZQaF9k2CCsG2T9Z0SfbMtJbDbHvL14UnNb5ALu83LYB0ew3fE7DZXkTiIwD4IzV63DRLz0mODBCfDY4YL_gak95NN1OIkDkXn1k9pt-Ap3x6InPOLwGYn18Ua2z-NM45AzCmn0D2zuh5tcPWAqEsaTPGpfsEC7ER-KfgMjt78_Dt6q88BbzbfCYIWZid4zuQm08nhf4gzjfVIqcp1X_e_YBqgtEoZHwTBhdwpZaoIkr5Nr0bAtbP38L_bPeYH7cd9y_lxbq_c45JCc-caqf2Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/سپاه موشک شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133632" target="_blank">📅 04:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/گزارش شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133631" target="_blank">📅 04:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی ان ان: حملات به ایران هنوز تموم نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133630" target="_blank">📅 04:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c70af372b.mp4?token=W67Gn4tahi78GdcBzMbOPDv_36jnlVO1qAAIwYk7Qx39eiI5K-b2gKA5mowosxi94f2nSDgPXEk5270P-fYal8p4kOyB85n_mlufmQo5b1wtOqIi8rhktHB6hRzL6Lpci77H8SkoH8GDyp01gQBgeM1EEe9dVIqT6-JF4i72bB0pzVegxntaGlurCZsbJYIfC8e8l4DIUlFlp4sUr_CYsUmb0wjxacDTqee_r1C3RwWPfD7SXFsQxQXz-AFcZsom7u0SuTG3OSngC_WAjJUEbn_ICSfjhsJ5j9lujsYjkMGh_q5xdub3rizTOTL377B31H_r00hUuiLZ5lzyID1gbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c70af372b.mp4?token=W67Gn4tahi78GdcBzMbOPDv_36jnlVO1qAAIwYk7Qx39eiI5K-b2gKA5mowosxi94f2nSDgPXEk5270P-fYal8p4kOyB85n_mlufmQo5b1wtOqIi8rhktHB6hRzL6Lpci77H8SkoH8GDyp01gQBgeM1EEe9dVIqT6-JF4i72bB0pzVegxntaGlurCZsbJYIfC8e8l4DIUlFlp4sUr_CYsUmb0wjxacDTqee_r1C3RwWPfD7SXFsQxQXz-AFcZsom7u0SuTG3OSngC_WAjJUEbn_ICSfjhsJ5j9lujsYjkMGh_q5xdub3rizTOTL377B31H_r00hUuiLZ5lzyID1gbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پادگان باکری دزفول در حال سوختن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/133629" target="_blank">📅 03:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HglBZvMDvDw-RDtbcVlkWzSpTqBWrhxFHQ609ahho_z2k2Xizzwz-yzzDUEn5clXKh4WyiwSQcX3gjxEofa-nyehUcbgXND_k8suYt9q542Nvh5jE1HEqwYuRprO4PnlOdgWK0VTeY4uy8vGmjygCGCAixbCn4C4ocbtY5goYCvq_f52d1739a_rUJueHSpHvOOu2O0InH_0OLyTUuSX8mI0nTWwpVrBjuCPV5Hy1BzWW64kaxES7_hrfwAyHcqCUkbkCVaGTthb6MO-XvD9t1Ikfj8-MRjtp8q_XChXxcbBmG8-g74AVfMKkncZ-H3qpE5QAkH41MHdnEHBl8PhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از انفجار عجیب ساعتی قبل در امیدیه خوزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/133628" target="_blank">📅 03:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری سی‌بی‌اس:
حملات امشب آمریکا علیه ایران تموم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/133627" target="_blank">📅 03:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f41a3af54.mp4?token=QA5U_yuZQ46TRK8D1qrtCg4BN4yuXtkLiflP3f1ROXVJoYzYODkJnyBu26ttIhXHctbOH1sIos8rPGow1F5Jg-zcu2uZVIt9mEoIk6CFwGvkbSIGDA7tvdu4cdqCELGP5i5GBnGHdfQwyhI4OxrHYM4l3qm5RIEL5LaUbqXqGnTLcZxE8-CoN2Wmy_Yah99xS7PbMlTDHugP0ssQLYjf7rg4UiaMRs1ZKcZo59jDzSknS8aHFITcIsdX7szAo6U7uVqmlYXRvAaw1dVFkH9QtpFDfDILu3NJY97t3JC6Emd70ari1BXSxlgj4fA-p186c252_-IIxHv8Oc9vLQTkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f41a3af54.mp4?token=QA5U_yuZQ46TRK8D1qrtCg4BN4yuXtkLiflP3f1ROXVJoYzYODkJnyBu26ttIhXHctbOH1sIos8rPGow1F5Jg-zcu2uZVIt9mEoIk6CFwGvkbSIGDA7tvdu4cdqCELGP5i5GBnGHdfQwyhI4OxrHYM4l3qm5RIEL5LaUbqXqGnTLcZxE8-CoN2Wmy_Yah99xS7PbMlTDHugP0ssQLYjf7rg4UiaMRs1ZKcZo59jDzSknS8aHFITcIsdX7szAo6U7uVqmlYXRvAaw1dVFkH9QtpFDfDILu3NJY97t3JC6Emd70ari1BXSxlgj4fA-p186c252_-IIxHv8Oc9vLQTkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به امیدیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/133626" target="_blank">📅 03:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDiWFdkGiv-w-G-buomGJPT7LO8sKBLhpphtKoWf086Dr9Hpd_xzWhH3SVWS9gRDavS_49uA78jGLkJIAKB2i31pHBfvLbF-p8hCyhAsxF-zhsSJKby2Wp_WN3JF3dDax6du1_04w2rPpN7OwlQzTFx_0zGm3iZcGtwymCCPe4K6tUcehh_80atdMLd96VtnDv_iMt3ZZILo1U-hJOFyiin59GNW73HGMt7lqYqYusl1og7hlwpjMfJPu2jybhYf7dKEWhKHU36N753VCbuqyTOLagRbD-veaV3Bb0snrcwsAelkMMrsh990jSsS8BMjr0zHJ8YS-WhIxyDdZHtbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون پرواز ۱۰ فروند هواپیمای سوخت‌رسان ارتش آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/133625" target="_blank">📅 03:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
گزارشی از انفجار در فرودگاه آغاجاری خوزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/133624" target="_blank">📅 03:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133623">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc7be2cab.mp4?token=azTT_0gPu94WccIV9BaK9B8SdZ6RDE0nkJpIxjUwIGdDwkC9tN_xPQKwI6NXtO6Ethv_TQ5ywfUnlrfV2Og0fBuJsyV92Rs5c6KCK2_p41B4L6yuF5IvdlFhWlq6ZrI_FRGFo_MPhpxz92eyPA1XH_2-NULdVoC0QVtKcHETX2dqZYA2We0nQP_DOANpsa3GuYZYaL9uWjNxzeBF8-yi-x2y4ZpO4VaRT3w_ODC7UlsPQ--Bpn5p-WK6Aa0VAq0fC_sjwJVMBG5CDWM1UwENpiiA6KJxfUTxmX3y-vm6KeCnx3mKX2_YXkNrve99bwV1wpWo1BNUDYCNyohdIpAiQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc7be2cab.mp4?token=azTT_0gPu94WccIV9BaK9B8SdZ6RDE0nkJpIxjUwIGdDwkC9tN_xPQKwI6NXtO6Ethv_TQ5ywfUnlrfV2Og0fBuJsyV92Rs5c6KCK2_p41B4L6yuF5IvdlFhWlq6ZrI_FRGFo_MPhpxz92eyPA1XH_2-NULdVoC0QVtKcHETX2dqZYA2We0nQP_DOANpsa3GuYZYaL9uWjNxzeBF8-yi-x2y4ZpO4VaRT3w_ODC7UlsPQ--Bpn5p-WK6Aa0VAq0fC_sjwJVMBG5CDWM1UwENpiiA6KJxfUTxmX3y-vm6KeCnx3mKX2_YXkNrve99bwV1wpWo1BNUDYCNyohdIpAiQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که تو ایتا منتشر شده مبنی بر هدف قرار گرفتن آبراهام لینکلن، فیکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/133623" target="_blank">📅 03:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
گزارش‌هایی منتشر شده مبنی بر اینکه کلانتری روستای مالحه (شوش) در خوزستان در حملات هوایی آمریکا مورد اصابت قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/133622" target="_blank">📅 03:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133620">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تعداد زیادی سوخت رسان از ریاض عربستان بلند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/133620" target="_blank">📅 03:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133619">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
مقام آمریکایی به نیویورک پست:
انتظار می‌رود امشب شاهد حملات گسترده‌تری از سوی آمریکا علیه اهداف نظامی ایران باشیم، حملاتی که از حملات قبلی نیز بزرگ‌تر خواهند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133619" target="_blank">📅 02:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133618">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
اخبار اولیه و تایید نشده‌ای مبنی بر هدف قرار گرفتن گذرگاه مرزی "چذابة" متعلق به ایران در مرز با عراق منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133618" target="_blank">📅 02:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
شهر هایی که مورد حمله ارتش ایالات متحده آمریکا قرار گرفته اند
🔴
قشم
🔴
سیریک
🔴
بندرعباس
🔴
جاسک
🔴
بوشهر
🔴
خنداب
🔴
بندر ماهشهر
🔴
بهبهان
🔴
اندیمشک
🔴
دزفول
🔴
اهواز
🔴
آبادان
🔴
خرمشهر
🔴
گسترده تر شدن حملات ارتش آمریکا نسبت به حملات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133617" target="_blank">📅 02:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
6 انفجار بندر خرمشهر را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133616" target="_blank">📅 02:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
جنگنده‌های نیروی هوایی ارتش ایران از پایگاه هوایی وحدتی دزفول به پرواز درآمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133615" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
تقریبا کل شهرهای خوزستان انفجار داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133614" target="_blank">📅 02:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
انفجار در هویزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133613" target="_blank">📅 02:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوووووووووووری/جنگنده در آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133612" target="_blank">📅 02:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
انفجار مجدد در دزفول
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133611" target="_blank">📅 02:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
انفجار در سوسنگرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133610" target="_blank">📅 02:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/عمران عقیلی، رئیس واحد ارتباطات عملیات ویژه در فرودگاه اهواز ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133609" target="_blank">📅 02:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
انفجار در اندیمشک
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133608" target="_blank">📅 02:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133607">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
چندین انفجار در بندر خمیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133607" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133606">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
تیپ زرهی ۲۹۲ دزفول توسط آمریکا هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133606" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133605">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
لغو پرواز های مشهد به تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133605" target="_blank">📅 02:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133604">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
به دلیل نبود پدافند موثر، هر موشکی که شلیک میکنن به هدف میخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133604" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133603">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🤩
@khabari_18 | پروکسی متصل</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133603" target="_blank">📅 02:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133602">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حمله به امیدیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133602" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133601">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133601" target="_blank">📅 02:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133600">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133600" target="_blank">📅 02:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133599">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/انفجار در دزفول
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133599" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133598">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P37mCZlZpaUmzqmgCqEBCfPWKAXbuLId6JGY4ULvj58v2K8o--S9KoZ10EizNazp2j8fDu5z7Io-4tQGQFs_S_uLnwW9JEXV9x-wpgUqVtLhcl4EUZsQU9pD-EipDE0IK5uIL8VKb8xaaQHcwJkUhNJZ9AT1x9CFpULBsaCf-d-YhH_HBMMrfY6gE-H2uZpSPQlZ8NcdFAdcxT4WSQP1N1OOGBRZ2zuwpsBjC9hHoyhKcmxTmcGHfQoSP3mQtsl1XHtq76FOji73Khdr_olYald6_XU-sFKoSMTRQctq5U_CUZCue-O7AjGiJdPKwstbs355dILOgJ32tb5rZqI4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به فرودگاه اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133598" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133597">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
جنوب ایرانم شده عین جنوب لبنان، الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133597" target="_blank">📅 02:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133596">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
جنوب کشور زیر حملات شدید هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133596" target="_blank">📅 02:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133595">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
انفجارهای شدید در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/133595" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133594">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری/گزارش شلیک موشک از کویت به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133594" target="_blank">📅 01:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133593">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پرواز جنگنده در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/133593" target="_blank">📅 01:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133592">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
به گفته یک مقام آمریکایی، نیروهای مسلح آمریکا یک موشک کروز و یک پهپاد ایرانی را رهگیری و سرنگون کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/133592" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133591">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/انفجار در سیستان و بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/133591" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133590">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
فرودگاه اهواز رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/133590" target="_blank">📅 01:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133589">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/133589" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133588">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-mxTFe_Xis-l1O4_hXexKpciPPDcKix1CqFnpPJl4dPH2IMzEdp4K1fyoztDk_sa1G4T7KYS6SqWzWw-XJeOp0vo0tkP2cBOjHH_g50ObXhLTBbDDmHZei6GHwHAkyWD-z_scXztvJZf7Ny7MBx7ashWbrCafXFAs4JxjcFCAqj0w7G-x8R1KmKPEbBDQjlNhOcfh0IwWz26DC_t1lkReVLOs-hFAa9LSw05EUNVBIevqvdbjpkPadPYVfmNpPLpD3p-7TWeh9d5nOg7-v2aNYxBg7S7AiPRprTrM5paHdu8rhQMqeJNOqJypI7ODUkWfdpbwsHkXpdcrOch22bPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/133588" target="_blank">📅 01:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133587">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/133587" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133586">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/اعلان وضعیت قرمز برای فرمانده های کشور ارسال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/133586" target="_blank">📅 01:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133585">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
انفجار در شهبندر هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/133585" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/133584" target="_blank">📅 01:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133583">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوووری/حمله به خنداب اراک
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/133583" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133582">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYhqV0jOpBtv6-h6kuwJGo64bBo6fhXTtnYhcojo9CEkqeBhG7HQWFoLCYP07YQg-0R3pPDRzYkQHn45qiMZBgdHxCps8lret3s5t63GgUTMH_o8GTq7moC9AsK26xtTgfaffiiGuQ9NJzH4KuR5acLLrNuF8KQouNQNVqNnSL07uwmCb2c9ezbGwPhux_ZSKpCy99mRLI4Dc_Ll3GSwoRF0Fk0xmMF__u0vmGQ0t5p3aIc2SGbkGTQbWpzm-m3sbxay5oBuEYlqQGX2fsi9jDWBKE2E2mU4DPFARTPBRf2qDjf-N_W7UZDGvvkEFepTz_tAQCijlyHCuPe6S08yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/انفجار عظیم در سیریک
🔴
خورشید از جنوب طلوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/133582" target="_blank">📅 01:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133581">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری موج جدید حملات به جنوب ایران آغاز شد
💧
Rainbet.com the #1 Non-KYC Crypto Casino & Sportsbook @rainbetcom
🗞
@iraninterpshm</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/133581" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133580">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
صدای انفجار در جزیره هنگام، برای اولین بار پس از جنگ چهل روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/133580" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133579">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/133579" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133577">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pcbzs3AjMsIznfHzliuyZKmIDx9dfiKSd58YhxQjqdP9MD1ypCQT9pjoC47qPAfIcjeNCVo2MY1aXx0OX2H91-lM9YTupmUrxo03_FjvNfMQLdyX-ZbEl0YeNjhg230EcBLN0i4O1OMZZAK5YsHg76juKgxfG7evq7Mb7T9cqQKRyub-EOzeb-cSCBd9ydCQRMNX5FwX3YLcLJ-ZtFh4j8ShWuZ0KWuVmODtuHwiuTBUpA2_v47wHWEhoDxlj-5IAeC4_9yK9mCJBWePYMa9K6jWhBfMqjLgH-pYFXgZl8fo8rI115wwOekbkRnWT03xD3coWIFiYwJ3Rn2R6B4dRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعلامیه فرماندهی مرکزی ایالات متحده:
امروز، ساعت 17:00 (به وقت سواحل شرقی ایالات متحده)، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) حملات بیشتری علیه ایران آغاز کردند.
🔴
هدف از این حملات، ادامه تضعیف توانایی ایران در حمله به کشتی‌های غیرنظامی و کشتی‌های تجاری است که آزادانه در تنگه هرمز تردد می‌کنند.
🔴
فرمانده کل نیروهای مسلح دستور انجام این حملات را صادر کرده است تا مسئولیت اقدامات نیروهای ایرانی را تعیین کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/133577" target="_blank">📅 00:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133576">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/انفجار در میناب
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/133576" target="_blank">📅 00:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133575">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/133575" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133574">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/133574" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133573">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/133573" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133572">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/حملات سنگین آمریکا شروع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/133572" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133571">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/133571" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133570">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/133570" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133569">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyATDsouAxGKEMBOFfE288sebzxK--WPROrewIJp9pyssrJ5T9VgsMg38qaHUv7qs6cvc5KyggK0yinTuzYFyOS28NEWTUtL-lNSNvpKxYOKZN0_HGJXWYiqRPNTtnF1YgWd35oHOJECEYccFryzWd86LR-d2NH4W93TWIVSv1ParbmiyyNUXU9oeHbRay6LeYuuYpH4jkvnz9bDo5oh89mXZu5DZ3NtvBQPwbZ1WreRgbdEuyF_LcAp2GWe6SiWC5q0PODU6ZbtXvHFYNSwgD-W8E5N72Sr94d_Prpk0_d19n0avGn-D41b8Z4otWYrnqoXQxOw0b4IFzYTuCdLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه تا سوخت رسان داره از سمت اسراییل میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/133569" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133568">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfs8CQ65fYKmJJkyX_2_saCpm49e00WzeMCoSXuiNDvJliqkU8SzV40XOi5i3QHDELeTavJxZFGADp_7qa1JzXJBZlI6zerjgOH95l78EaTxyfsdYLIAW7toxcmivIv7BEqsYkbR6Qy8a3yrU89PfQsLRhSjW4CC18ix-ywMS8Bk23JpidKmaie2M8SvlD45IqQvxp8nzJrtSqPPb7Um0Hf5cyDN-uy0KKZMqsDosSSoWSw3VZ_4I_SDsHbi_hKCmLc1-NJ9DpbGv4NCzCBI-d9vPTLYj_yMqU5Sbngaww8w7wpVK2mImct-6NTwjZGpr0ku6AGHiqAgVpx3EDcHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنت‌کام
: رسانه‌های تبلیغاتی ایران امروز مدعی شدند که در حملات ایران به کویت، سه نظامی آمریکایی کشته شده‌اند.
نادرست.
🔴
واقعیت
: هیچ گزارشی از کشته یا زخمی شدن نیروهای آمریکایی در منطقه وجود ندارد و تمام نیروهای آمریکایی در سلامت هستند و حضور همه آن‌ها تأیید شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/133568" target="_blank">📅 00:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTTdrjNko_ud9bT0ux9wfORz975MH_qaEVgyTyGzhXS3wJ0i0AASplzEmLH9Hy-O9KlTDzKwRUaH9ghv35BkPLiHtVXh00yS_LvutXW4471Y1xy3X5k_3QlrqIZD88cyaUZROWP16Fg8SsCu2-77-l0vO-Wqo4FMgW48YLhWiM5P4b5_32xaMyCQmiWVh1kRfGDnpOQKgmbwmlB3O5tkyiPLLAjQKPCYUEL7LJUHdGPaR8C5jQKm2S1ZVi-TRgJQJBrbtfkUTtdnXn7YQ8NlENQl4n2Eo-0IQaUCN0vh7eHUmZqyH0inPqcQ5zq8a8I1Jkdy-rHu54bmYzYrTvBydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOkHpiiVfFlT2ksO1jaEMDvfthhYUzrMoNPfz9qpsR-UjTp5lPfIcAob6V5QNMC6iBBNWq49cD8qzA763f_ZfN-68DQpVd2janDH6FNFS3bG1x3t-w2iyRt4_sRPhJ8b6ZBebNYFVpZqP5XJBpwwAeyfvvN1a-h92Hm5NpQx3nZzH3wuGowCL5Q3deHRk7GspfYHBhQ8vNiQWEt1Fi_M02VvtZfkZ7I53VaOENchc1YhSplQJtDVF6OLDbd7f7GechbaYoYLlsX_cVHpOTQJOkRJrdleC_OtdfIfax_nZLLpX6rZndKhomO7Za4ZVOpcdbn5JGnAeIFVvxv4kuEd9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکسای دیگه ای که ترامپ پست کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/133566" target="_blank">📅 00:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fabe17e0f.mp4?token=qmP-jFczG2VTvvTKvB1l09bdGyw4eKLRrNyWRtFb_j2YSzoaBgbDuneHFKyQZSm_-m0bKxdLwD0yo1eGjOk4JHg834i7TTuvnwqCoYhivX3YUmMmPNFhgIkcTXyOcBZTD4aE12gN4XVZ6R5E5rJ6YnYW8WQFzrQ2lH4nRG0Sn8gAMsZa5bebjdIYrZrY9moafwF8H6pV59wRDzsAvjGJjaoEc6bbY8FCiLEq5N0dzTVmsaXJdX-QVTYREzn3aCcJaYncyqoMkFtAF3JZxB5JNi4JuPWbt6pmluvJaOflaQIKHaRBLPQ_7_TjGS2J2V1MzkzH-6CfAS1BCzbPz0tHhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fabe17e0f.mp4?token=qmP-jFczG2VTvvTKvB1l09bdGyw4eKLRrNyWRtFb_j2YSzoaBgbDuneHFKyQZSm_-m0bKxdLwD0yo1eGjOk4JHg834i7TTuvnwqCoYhivX3YUmMmPNFhgIkcTXyOcBZTD4aE12gN4XVZ6R5E5rJ6YnYW8WQFzrQ2lH4nRG0Sn8gAMsZa5bebjdIYrZrY9moafwF8H6pV59wRDzsAvjGJjaoEc6bbY8FCiLEq5N0dzTVmsaXJdX-QVTYREzn3aCcJaYncyqoMkFtAF3JZxB5JNi4JuPWbt6pmluvJaOflaQIKHaRBLPQ_7_TjGS2J2V1MzkzH-6CfAS1BCzbPz0tHhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه نفر در حال فیلم گرفتن از خرابی‌های غزه بود که همون لحظه چند تا موشک دیگه تو چند متریش فرود اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/133564" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNsXqyVedGLSmdpJd9JjGIBzXkyHvlHKX7meevmHcVActDBZ_D71szzK03Z7CBE4ib-2y6JmLA0MQjdKVzV48GsH3DAVUzFcQ67Tdf0mINQx_l17Nb7R-wWS8I0RkedPMrBYdPygxmCBINAbYb1mgkVUsuYjwDn7ghLSoRJK1tZEKmbKORZeEyykeu1GWV9nJ9_vMA8f_q7zQuyODTCJS9tHUzVtXGwuxQlg6Bdu4h0DJ1cgH3GtJE8I4rFg54uqkEu5Ylv9uYQ0JNbf68hyTYdR6DpDGY4D1Ym2Azd9bUlIfhmzNLF3aMRaKffHvQS4iQvEiAK9MBNKb-38Ho97xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/133562" target="_blank">📅 23:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">قاتل همیشه اونیه که گردن نمیگیره، نه اونی که جار میزنه کار منه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/133561" target="_blank">📅 23:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dba5acc7a.mp4?token=ICXZ_P6eGudDmGXYyjFp2A6JKiSRsKqgrXO4h-LV0CqBECKpn09SRfRgcOnOxT8sU7_1jXWUp2kpF2-WkC6glCrA2Zp4hOp9Z3RgY4-EPsR6a4Pzp7yEJfKOKpoLD7TkuwWqXt9Beq3uMGsPpvE7FPH_7GehhCqFxQSYAcJheMtmLSrpc5TMzIDDaF4lHt8j97EqPHQiaBXbZoDgpLApOaCdQq5A54hdvhF2S0SBToaIbIc2ywnOsL8zML_oWAKDsvjd1StNrJtSfy5JKNCfhAZxRZYbhDGFE7-brlV5pjLBpRBgBz8Y5U4D0WgbdtPO9XWOkko0XhzIxn0yyk3Z6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dba5acc7a.mp4?token=ICXZ_P6eGudDmGXYyjFp2A6JKiSRsKqgrXO4h-LV0CqBECKpn09SRfRgcOnOxT8sU7_1jXWUp2kpF2-WkC6glCrA2Zp4hOp9Z3RgY4-EPsR6a4Pzp7yEJfKOKpoLD7TkuwWqXt9Beq3uMGsPpvE7FPH_7GehhCqFxQSYAcJheMtmLSrpc5TMzIDDaF4lHt8j97EqPHQiaBXbZoDgpLApOaCdQq5A54hdvhF2S0SBToaIbIc2ywnOsL8zML_oWAKDsvjd1StNrJtSfy5JKNCfhAZxRZYbhDGFE7-brlV5pjLBpRBgBz8Y5U4D0WgbdtPO9XWOkko0XhzIxn0yyk3Z6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه های قطر از تشییع پیکر امیر سابق این کشور در دوحه و دفن آن در مقبره شهر لوسیل خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/133560" target="_blank">📅 23:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133559">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrIiv2O2LtZo4Ut9Mi7TlTxzdUvkNZ6OmCPEHGQUUR6uwzTb-Y6-B_XhL4YeF0JufYgZIvjbdDQSfIo6lkzHpma__67y27Po362lFQ5SYJ-QPGzkH9CYOmeRgW7gYhTagCoyjbastPl_ucuJYYreOOdZ6cM9kagnFsrrDlLzktMhe28RL-S2R0og0Je25DbYkXJhDDf_l5Qp2UrWZxU4NQwYzHMW-o6Up8-fEDjbnCrDGp2MEnK9bTWYa0rz1ss65S0K49f2P-LqRWJfQkvSUlfj3CAqYGYbz6djRm2pejqHHXMCW4lHN2k21amSUe7G4ejQzN_oaQRWm0G-gCTUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری : آیا ممکنه لیندسی گراهام رو روس ها کشته باشند؟!
🔴
حسین پاک: نه،باتوجه به بیانیه رهبری درخصوص انتقام،گزینه روسیه منتفیه،این راهیه که حاج قاسم وعمادمغنیه بنیان گذاشتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/133559" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133558">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHO5G641bDvoQ7KVkPI-jrTzYAG-oreDQ2g8KRmVj-iEKCIHt8F2JLx6kfwDknkJXQ74QWbGBY-MqqmEJxNq1MMgVDlYnkK0Rd25pttho6VwXAWz4vrj4xTb6LhVt8NdlPAzG2w0eJletxIImQmkhkCEqaEKGzG8YUjceJucZ6ICElu9a1wo0CPfDgStd26xIdOBXy0AvaZ6RKF-Ju9uR-AgxcB-ejkyZoAx1GT1Nu0GtNqloLBnu39GiBJccvCnTkMqAyYTEb3KLq6wAk-wt13_6j1JXCdwP0RhvpWonBy9FAjc9i5f_R2V6bPgWtRkgKE7TCWpy0W4lehFThJp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/133558" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133557">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBIolWdVM5e6cs_3dNbSW1cJcO8D91JBKfeCjCRWGIfZCc9pyV9bRy6KY_vb5TLFZmbnEHiWT-b2zLmFzT7KZ0OiEY1DgYv07F3RfbxRRywF23KFcUPCIydw9Z4XjIuvW8PEMVWC3jbI7yKl18UK0rdMCNPFljUZtVwB5o2kQRESuPZaFAtw-SlwxRHKbq3XEGF6mO6tkCcvwT_S7hOyd1Y3EHPgAAXn4LmAMW24Tg4c7Raw7A6qJNm2iX3QgMCKEIMjryFiRPugFoqUX-VuKC0jqIwenTDPqBB7UyHHlvX_Dds5d2LcxHbt7xpFDMsSUrEyL9wJ8EJxfl9g0E0wgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/133557" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133556">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: «الگوی رفح را در جنوب لبنان اجرایی کردیم/منازل و زیرساخت‌های ۲۴ روستای مرزی لبنان را ویران ساختیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/133556" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/723cbb9eb0.mp4?token=O0FCy7k-5mtfqR7pfzP0RanEgp2O1gDuatsr7t6vk0xS4hCtyTK3kjywATLAexGL4hUhRHnRh7i2RmW0ECpudDBQqOL9ZsDrZiPaCoAvAouvyppeUFN7J4cpU5gdJaFnSEiczGyS0FyCxRzXZNZKz4dAI5yCwQj4-NCxQQxdrMtufZYqwSmVWHzwjw4ggpdB8Ryom1vQ99_GYdsvLuPZ6pn-ZIZwnZK-uRuUFR9ZIX6TcSvnin_Darh1Z8Rdh9PZdBmnt9a7GW1ZWAgPB3pn_KyedUbKu78GtTCMs8rXVrs2eX02BAuznYtOHk-LwqA2dDQYt7ByiXcxXICgJuxcugkcNE8TNE__tguh0FnZz_3wHgMAS6ZagfBhN33DV1lB8w_imWD2Izw54QOpVi61QgePu168NWjRvrSUzGYyCkfjsvLv39BiwWnrtFC0BsdY_GsQWXVe_S8sHb1KhCUO-LA3mX5wsGG68L5fxrjkasb2uV8Xt9IhN0zgRdE-jik7ITtI1hTJKlokesoDZTqXfGC9mEEtnXCLEuXckiMn9A-oebiGsNgPGVv5IrdvwkqNvxlOBfu7MfT-Bp6PYsjg2qUfmouyRWYkPtjjUGMJpuqrQkdMH6oqjaId3TQ3tSbLZTolThqjP0wtRi2G3m4s1lraxOyMGIQ2LixQRgTn5q4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/723cbb9eb0.mp4?token=O0FCy7k-5mtfqR7pfzP0RanEgp2O1gDuatsr7t6vk0xS4hCtyTK3kjywATLAexGL4hUhRHnRh7i2RmW0ECpudDBQqOL9ZsDrZiPaCoAvAouvyppeUFN7J4cpU5gdJaFnSEiczGyS0FyCxRzXZNZKz4dAI5yCwQj4-NCxQQxdrMtufZYqwSmVWHzwjw4ggpdB8Ryom1vQ99_GYdsvLuPZ6pn-ZIZwnZK-uRuUFR9ZIX6TcSvnin_Darh1Z8Rdh9PZdBmnt9a7GW1ZWAgPB3pn_KyedUbKu78GtTCMs8rXVrs2eX02BAuznYtOHk-LwqA2dDQYt7ByiXcxXICgJuxcugkcNE8TNE__tguh0FnZz_3wHgMAS6ZagfBhN33DV1lB8w_imWD2Izw54QOpVi61QgePu168NWjRvrSUzGYyCkfjsvLv39BiwWnrtFC0BsdY_GsQWXVe_S8sHb1KhCUO-LA3mX5wsGG68L5fxrjkasb2uV8Xt9IhN0zgRdE-jik7ITtI1hTJKlokesoDZTqXfGC9mEEtnXCLEuXckiMn9A-oebiGsNgPGVv5IrdvwkqNvxlOBfu7MfT-Bp6PYsjg2qUfmouyRWYkPtjjUGMJpuqrQkdMH6oqjaId3TQ3tSbLZTolThqjP0wtRi2G3m4s1lraxOyMGIQ2LixQRgTn5q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید جلیلی در واکنش به پرسش مردم که «دولت گفته همه رأی مثبت دادند»، پاسخ داد: «اشتباه کردند؛ من بارها رأی منفی خود را اعلام کردم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/133555" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9054413b86.mp4?token=bqS9YW9cNv8pGTTqqbfTys6i1a62XjhTnTMgB_DGxMgq7pxoNY7Vg_bCn9nQ2I77Dz_rtue8F4pZ9h8MZUp8GrGr4JKtxygApTSAGLFuTA6nzwF9FMcu8PTktpkZTTLWwGOw1yK3GtwZbzMuqVJhzSPL4uPvYmhP-M63juQL2kcjdhSex2-793lr5YWWq4ffYjHpUKAC-UnlCEG69DXM7mteBIiq-T9P-74TiF9EQpbNxbqaFo4E3rVFSexwimW5B-a82ppygLMigXO8rdXPhuAzpvxVMIHTj0poDJGJfAjQeRjVPP_wcr7mpJYirOBJOmPSH--mjlRGOu1jlfdZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9054413b86.mp4?token=bqS9YW9cNv8pGTTqqbfTys6i1a62XjhTnTMgB_DGxMgq7pxoNY7Vg_bCn9nQ2I77Dz_rtue8F4pZ9h8MZUp8GrGr4JKtxygApTSAGLFuTA6nzwF9FMcu8PTktpkZTTLWwGOw1yK3GtwZbzMuqVJhzSPL4uPvYmhP-M63juQL2kcjdhSex2-793lr5YWWq4ffYjHpUKAC-UnlCEG69DXM7mteBIiq-T9P-74TiF9EQpbNxbqaFo4E3rVFSexwimW5B-a82ppygLMigXO8rdXPhuAzpvxVMIHTj0poDJGJfAjQeRjVPP_wcr7mpJYirOBJOmPSH--mjlRGOu1jlfdZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده جدید نیروی دریایی سپاه:
هیچ کشتی خارجی بدون شناسایی ایران از تنگه هرمز نمی‌گذرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/133554" target="_blank">📅 23:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133553">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نیروهای نظامی ایران با هشداری از شهروندان کشورهای امارات، بحرین و کویت خواستند از مراکز نظامی دوری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/133553" target="_blank">📅 23:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133552">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065c481a53.mp4?token=SD1MfNKTJi1wXsYjGzvzqIKMb-V7IFXP6C8T5CFb9ReklPcxP0si0_Xo2RC7nEVOVb8bqkyQTikpKQh20PPCowvss6HR85EiAvMDr2ho5WVmXSVqyWi58BzVD4yaD_S0c_OwlU_mdtXorqReH9mH_HFyzSWgU_gE7UWKRHYNLlEjhY7w3a0GLM-k2XtBjXxaUSoyDpgLi4cHusdVWmqiOkBNUcBO8HLtfVS1GOicQ2eTKqiIEPvYQ-bD9U-kY4ZNLaLQIypKByPAOJPUcwseFPhbii2thFJ4zFDUXr7zqQmjEZuzt05dEM3452xTUej3iun09XRu22bK0-oQkVwPAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065c481a53.mp4?token=SD1MfNKTJi1wXsYjGzvzqIKMb-V7IFXP6C8T5CFb9ReklPcxP0si0_Xo2RC7nEVOVb8bqkyQTikpKQh20PPCowvss6HR85EiAvMDr2ho5WVmXSVqyWi58BzVD4yaD_S0c_OwlU_mdtXorqReH9mH_HFyzSWgU_gE7UWKRHYNLlEjhY7w3a0GLM-k2XtBjXxaUSoyDpgLi4cHusdVWmqiOkBNUcBO8HLtfVS1GOicQ2eTKqiIEPvYQ-bD9U-kY4ZNLaLQIypKByPAOJPUcwseFPhbii2thFJ4zFDUXr7zqQmjEZuzt05dEM3452xTUej3iun09XRu22bK0-oQkVwPAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره فوت لیندسی گراهام:
در اسرائیل، ما ناراحت هستیم در ایران، جشن گرفته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/133552" target="_blank">📅 22:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133551">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6y67aks9c3ewZLjODzdGH4B-8aLQKt2FlRD1Ojitv1LAQc-oEakib3p1WuOM6nqSDdlyP8d6hATWQW3oooiAktQAXLZBZqUE57jRBtvBpAF5fZsZhT1oregjj2WA7jxqB1RYiYKyvuxdMztLSJzhuU-2Y4JX23RHYwGnISwXqAb2Zeu8lXYHMGzc5asMPDhOVwPqce2ZS44Gg_Cl0Eq1SEWuI2kaY5NAgSzhptEEIdjQBB9M3BqTh5VRFPVjsA2IUsN54Gn41NrBDYdl0s6CXcl0Q5UUJOh5dkKnnVr-o4qu90-Li2_B31d2BLwSIENSFuB6yBOYLgHibLcCt5zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون آموزش: استرس، ترک آزمون، برگه‌های سفید، ناامنی در مناطق جنوبی و احتمال تقلب و لو رفتن سوالات؛ ماحصل روز اول امتحانات نهایی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/133551" target="_blank">📅 22:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133550">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fce8q8uPf_MdWOMWdAsvMhhCCUDCrdjJJNhc5pfVBncXt2-b3u4ycQ1lk3JV0LhG5HP_S5di0t2rzCJ67ufH0EC8VQUxzhaoikHdHDIMZILRQJdW2l-gE7ErWK9SctpNDqiW9-bhATgnmjInAfaPweH9XbfhYS_f5V9jSAB0FtHW5tpkIK3_Gs7OXzYwdk0iAwAsYTau66MsNxHzJqgev32QbAeQSIQEY86fqkfOS2vhwqcbNCcXKSjbvYAOK-epVoXUASSWrU_IhrSxIDfjSrQhWccxNAZILy8Kcn9as72fBOH0SCQIcdDku_TK8rrRuDdItUfMVzVG2Mffi-iPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دومین هواپیمای معراج مخصوص گروه مذاکره کننده ایرانی از مشهد به سمت بغداد درحال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/133550" target="_blank">📅 22:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133549">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخرید و پشتیبانی</strong></div>
<div class="tg-text">💫
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید.
📣
با توجه به سابقه عملکرد سرویس‌های SafeVPN در زمان
📣
اختلالات و‌قطعی کامل اینترنت بین الملل سرویس های
📣
خریداری شما فعال خاهد بود.
خرید فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/133549" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133548">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخرید و پشتیبانی</strong></div>
<div class="tg-text">🚀
تعرفه سرویس تک‌لوکیشن های مختلف Safe VPN
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000 تومان
▫️
۴۰ گیگابایت — 60,000 تومان
▫️
۶۰ گیگابایت — 90,000 تومان
▫️
۸۰ گیگابایت — 120,000 تومان
▫️
۱۰۰ گیگابایت — 150,000 تومان
▫️
۱۵۰ گیگابایت — 210,000 تومان
▫️
۲۰۰ گیگابایت — 300,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 450,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 50,000 تومان
♦️
۵۰ گیگابایت — 80,000 تومان
♦️
۷۰ گیگابایت — 105,000 تومان
♦️
۱۰۰ گیگابایت — 155,000 تومان
♦️
۱۵۰ گیگابایت — 230,000 تومان
♦️
۲۰۰ گیگابایت — 305,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 585,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 160,000 تومان
▫️
۱۰۰ گیگابایت — 200,000 تومان
▫️
۱۵۰ گیگابایت — 300,000 تومان
▫️
۲۰۰ گیگابایت — 400,000 تومان
▫️
۳۰۰ گیگابایت — 600,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 680,000 تومان
⭐️
تعرفه سرویس‌های مولتی لوکیشن SafeVPN
▫️
10 گیگ ➜ 50,000 تومان
▫️
20 گیگ ➜ 100,000 تومان
▫️
30 گیگ➜ 150,000 تومان
▫️
50 گیگ ➜ 250,000 تومان
━━━━━━━━━━━━━━
🤖
ربات خرید
@SafeVPNXBot
✅
📞
پشتیبانی
@safevpn_secureSupport
✅
😍
رضایت مشتریان
@safevpn_feedback
✅</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/133548" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133547">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رویترز از حمله پهپادی به اردوگاه کردهای مخالف ایران در سلیمانیه عراق خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/133547" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133546">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرگزاری فارس: قطر و عربستان بازوهای حملات هوایی آمریکا به ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/133546" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133545">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/پرواز چندین سوخت رسان آمریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/133545" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133544">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نتانیاهو: سناتور گراهام به من توصیه کرده بود به تأسیسات هسته‌ای ایران حمله کنیم
🔴
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در واکنش به مرگ سناتور لیندسی گراهام که امروز درگذشت، اظهار داشت:
🔴
«او به من گفته بود: باید به تأسیسات هسته‌ای ایران حمله کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/133544" target="_blank">📅 22:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
یک هواپیمای دولتی عمان درحال فرود در فرودگاه بغداد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/133541" target="_blank">📅 22:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bJM1LjbECUjdo6pGlWj66l7qV13b-6deVeRdiwXcUx6z_HV_mePBTQlyjPe3dedwqja9WuDsqGmU2Ix1-eSjr91gBmg9emjpB5myw6pYNFGGN-2Vt1WsDCCJVELDEgaSaBdkgF_52FVHmhf88lGiGHhi2V5F6_xYTGG6AYFwIekqkBElaOJd6njhO9xfqFX9YhJ2xNmJoW3JslosDVYYJEKHbxUqW8-orRK_8YKoK6hwzF9uuGxF59Yf8AZt_KZgpgLs7YT6Ldh0u6NUfmrCTJ9ytI5SQCovCBNli8otl4Xr3XN5h5bsirZJMVa8XkW1i_b_aUzLu6ySoDky-wGi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای میناب ۱۶۸ متعلق به تیم مذاکره کننده ایرانی (عراقچی و قالیباف) بدون مشخص کردن مبدا و مقصد و همچنین روشن کردن رادارش در نزدیکی مرز ، رو آسمون عراق درحال ورود به بغداد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/alonews/133539" target="_blank">📅 21:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
معاون سیاسی امنیتی و اجتماعی استاندار بوشهر خبر منتشر شده در فضای مجازی، مبنی بر حمله به محدوده تیروگاه اتمی بوشهر را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/133538" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
واکنش دبیرکل سازمان ملل به درگیری‌ها و حملات سپاه و سنتکام: بسه دیگه خیلی نگرانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/133537" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYdB7dW46YJGc60zF0sEXH4QjlnL69Ml0NxvyH_03W79S7q9tzhw4ZRGDe29UbPs_CVX2WvFD0MhCZDU8_Ml4IoSObsE2az6ddBvzRWhEjfdKHo3xCNC-ixBicw2Zawx7vgaM7Olkc02eYefwXBjROsmDkyPCtResVDp6fUveyVXXEWcmKZdyrYNW1QB3EUPZnwDXoPZgRdvdm0amBOP0sZ8uNBcwhcDGYYX9uLwdtOSoP2SVd5GZSzQad_mZswlZvcrAtn8d8gUqiFKMxZDpCkoxT3YC5nnugJNV8xEGaPzRu0NGVliMmI_sQDIBQfiKG7cTSWiuiIlV6hYQxjZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه فرهیختگان خطاب به رضا پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/133536" target="_blank">📅 21:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnQkSEsYbVOnUFaZaM_ebBzB7GF__OcSn37c6aBGFRhguKdSvEwW66O9Xy-af62ZKjBuLt3VyA0bmRdrTkUcY4f5fFszIp3BGY1rN7rf-Blimj2DB6vjoUt2BkNUT9wx4WUS9vV51hPFoGtee8gLTA4tFMxq68N93JpSElhxskk_LF-tDTaK7k55zD_tTms-j4VcsGkqrc7oqfC6o-jye6QBcM8hfE3DotT-20qs92WhwOxRUvOfHTAqxzMpIDcox2v4_BTHPsoj9rhP1zRtBrldh0evgqFgGzYsx2rNnJ8-qyyl3BBr5C3K1Zu9RHljfTtC_urBRtwAHVzBt7l2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون /وضعیت آسمان پروازی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/133535" target="_blank">📅 21:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/133534" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فیصل بن فرحان، وزیر امور خارجه عربستان سعودی، در تماس‌های تلفنی متعدد با همتایان خود در کشورهای قطر، عمان، بحرین و اردن، تحولات اخیر منطقه را بررسی کرد.
🔴
وزرای خارجه این کشورها بر ضرورت تلاش‌های دیپلماتیک برای بازیابی امنیت و کاهش تنش‌های منطقه‌ای تأکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/133533" target="_blank">📅 21:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC2BfCelgJwJPS-dndkIx9IhGokb3IZozqJ9xpAfe8pzkw6uBmkfA7CjqoTo6vklaSt_2TWB_SQa3vGQSjJlg-4tEKKO4XFmox8e1zjaqkqKiAsrrZUZGwI2caMQgr6jrud0wRGf2yg0_rqT3JPi5ncgjIGJeXAPkNkS6wNA-k8bumVUawNUUQ4cg8U9tPIIGA-u0dF7ZrnU0lr2Ast_XAYwkPP38AI-lB8nvJykfwH0Ba4FUpGSQHS3KtXTkpEv-F3C9Dk_Zvm1FJBtgBKr1insIv_R_-EFq_zCbGA_EA9c_-sv-jCg0j4w6ZTMAGsuWdeCHRG-jv3qgJM2qutJ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون فعالیت گسترده نیروهای امریکایی در جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/133532" target="_blank">📅 21:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
هم اکنون هواپیماهای هشدار اولیه و سوخت‌رسانی هوایی ارتش ایالات متحده از پایگاه‌های مستقر در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/133531" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
