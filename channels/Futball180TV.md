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
<img src="https://cdn5.telesco.pe/file/KX6WaudVpnhPjmhPkiCidedTWThIbMksinPEOu-qhPEugewpb1EwhLwr1sQbob9rBUbqUBzVnCfbwwGseXgIp6JmvBAn4ZFxKLiy_R8JQ9Aw_AW77ZNXA0vwq8F-RCL5pqa5qDKQw4LBgN-0lBWoFoHy-UbUJElEd_hAbOhp5nKt8eKpdS4LfdnS9gZbIAWx5GQUvC7aRYZLRxd1A5L4nOm_C0E9J1POBKKKi_7k-Bktv6YxkeLfbWv-_5FdJK-pVNB3eMfW4akYsCbYofXxkrF1QJBJUM58EObip5i9W6wVD5jp9feq7d0z25VLb1gEpvArO2UthRXk6JWylS4U6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 603K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 06:50:05</div>
<hr>

<div class="tg-post" id="msg-99343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuJRzR0QMZRjAmVoPyTRCY2kPdGIDT1AJJctpjSNQ-VaFvC39h_gMzyb618QKo3wlf1Q2VEbmN9XONjYMeQ_h2cvN4XA6poJ74dh8-S70O5x7e60U8k1gKkRbIXLwsya0n3cFr6pTRRCfH6gaJwhC-6BHxQs-hV-OX9eMUfuTaesiskGRskVY38GNRuEaLBZQSPQZgl9ukI5cSkyuFmItmOmQsCRTE5TIhZF2YjN7nBYhhRGLYa8IwKc86yBDxeKH5TqgsjTRoxanv1yyQij1gobe3lXCIYgQQgc5-ZtCYuvcnvPaH4xGdP8DY-GYmHt_E3uInsYZsojmnVAHJAJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Legend
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/99343" target="_blank">📅 05:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnmBcbspDEVWB33cY7t7K-a8KRp2dyO9p5Sw-K2qfMx7UScA5Jr6l1IdwslHvueA7oHf84AGePIjDGzXhjNHitxNuotrm7Z02EnMJIaAwP1rXv2GYAmtRiHVjS0ZMTYkcKpOIbhNKIJv9Psi6DH4X8u8Ci7pWwwhP-wLGzdDsxVX-ucUnuDkFXBLMSD-a_7TxqHdvxyeIqnTeH97NM5FKcw_HizNIWTMnHjeVceLvf1kEg62U-zfyK2Iojirwl9zStdPDmEKtw6cTnJ-V2UlzOGYeyfhaIiqvZvekKIqhxLdM1ALH2ECkaqhj-DDDnf6iBQnIel73JHGobPwGAVB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
مصریای کصخل بعد بازی با آرژانتین یه کمپین راه انداختن برای آنفالو کردن مسی، بعد از 511 میلیون نفر فالوورای مسی رسیده به 512 میلیون نفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/99342" target="_blank">📅 04:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qut_ymDc6ynM857jX2XdiDbcde_lnVC76PTJXCs3YRzSLC1VrUH4yZFrd-u84knHRC7oBUNzQ5mdmRAEjx9UgxNsAi6Uka6P-AoW21hllsWjLUIQmZ8YygQC3Bz54unrvF_xpa_ks1ueUa71y96V7MvARl1YiI54F8bxXXJ3b9bSKtl6z030zpmsCbvJ5v3Fz2UcWlmjhNTWubmp2ndqu3RPzWyzjW-NP8fgNoS3IhMsQw6a1q2rYbiQNXuGZeXFqqX822qxv2fGhp00uzVEZyGJUaCbUwey0FoiTxcpS9xrA4r8eTBo9rOLrJJyvp7gYpYjd0RcXwSv0R98nvk8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwpYhskUAEkz1uL3PnLvcJC2sYPmHE4DFVOXoa1VRZ12BU9OTb0nELqCJhjjmw-N5tj8T-Af7SOo2-rpixe65PFSMIxw-wrN7aLzQtrWVSilzKuBt4HhN6vRUmzoGpniJpOjxCQ1laJG4ojffaeLDdoa6AAjmgav1Qu5Y9oEpf63AsJV9zfkhlxlNsDd82GPWNlZSfTNHWQDD4scYHuXSevWV65eBrZMi82FbmqfiIAbwDG4KunDqF_q2p2btHF1hW64fYTyylg7LRtDkSDylZXB-66zVXZWXTAjf74NN9sxG54o1jAyCuEivzxHGrxqJey0Vi9J0k1YMDWosVVBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkU6V79P8HOXbIM4_Dzfqg1osp7XeDKgsC8lzMdzmW4Qi_syITLqPpFUpn5s5tGgkw8ZlLG07EfVipdMGkXKmw__JtPfKSt1ZyB5Tq6JkEOPv5cIDvgr8ETnqW8dUqwPaQwBzePYhIvTnIymwu3rnxPuSUUSGBflGHOkc6QlnEEeDciB6E19nhDxltfDf57lb-Sqf8F1g6L6P3owafNkFpiaCvwIvRXqisy75OENVxRA7pBr-B0vLuwCXcxyYLaLqZbEzz-WU54SC_6xWK-mgfCPvzBbApXzUPecoP9N-5OOpz3ht2snVSumXNC2_puJwt8E7MQsH8RJZjj-gS4cKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7eoIftTRpi60yar21dSzoQn1uciKpcFp5y0cqPAG2OV9S7nHaSzCqBy4Sj6kIRqmnZchIGfe3zcPBOrFBI1SaQnD4gapQQAqb3h9MHA78Fo25a1xlAjTRu-xtuMW6UuPd8dz09xzgwF_licLSrz3vCfAI-Z6vDtcGpJwhoOMS2Hrpd0jNRG0CHduHnaRv1NMVRX65b84-miNMs9pWlgJIWwy-26v7w66KYInKzTjQGjccBnr8Ir91F12DrkItiksuxW6VS88l-YssX1CW6RbTGAMk6v082Ltqs_bL31Lu5EsSgnuX4zaEIOslN-bvldqynctZUXibppR5DLeqmZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbYBDDD2f5Fh8Zb6WlKv9CLPKw7Y9nl5TYo93esJhV2JBTsJ6YpyN69VqxsDteH5LMPotGuN3Yy6BEliwsdjKFFlzvvL-mcSf2m1hi6YZmRxJE31CBh9lI-zq0ebwrsQ4Qv1baYmleTa-Tpbc5GjDfNIidd4Ro92U-K8qpsTgnYAoPT_7FM4H-oyYE3FrNfcVpurxBkw80Kd0PKjWVCZBc5proihmqkCo17X2PeuIiP9ga6ghjWnr08fvOu7-qoX-gj1pp4XzZPDMX4et8HjbDctAlcNOJ5-ZEekAfURBYJhb0ooRRFponvsulwUNg2gmwT7f_PYm3E71jGtDeprpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/99337" target="_blank">📅 03:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8c2f73aa.mp4?token=DLn03WCJdDM52nm3hPFKMUfbZRTgypnq2wvKYSkgSCXqC0hs6_XatiRnv6hbg5r7EalPfJMqF4ub-FbG8dIv6gxboUsVL2CclA0lo12sdTGg52IQD8MNjgGY40m3nR37Vn31moyvVKLkFvJBCxWqOo6aDdZqUjwOkMxv1A3wFtBO5msBHa_mcDOpCbrwQltze5eO6cUDlN8rBCXn_xVq3cvJufjmKU9abvYTHEJHwyFNHaLMFuYoui66hKfwy1jFCqx6ijdKSakSwy5O9r7xd5ZQZiUhLHBv9RvVyX_wgmvNzj12hPYOmQ6XMUe7swtnjlpTg6sDaj181cVLqu6eAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8c2f73aa.mp4?token=DLn03WCJdDM52nm3hPFKMUfbZRTgypnq2wvKYSkgSCXqC0hs6_XatiRnv6hbg5r7EalPfJMqF4ub-FbG8dIv6gxboUsVL2CclA0lo12sdTGg52IQD8MNjgGY40m3nR37Vn31moyvVKLkFvJBCxWqOo6aDdZqUjwOkMxv1A3wFtBO5msBHa_mcDOpCbrwQltze5eO6cUDlN8rBCXn_xVq3cvJufjmKU9abvYTHEJHwyFNHaLMFuYoui66hKfwy1jFCqx6ijdKSakSwy5O9r7xd5ZQZiUhLHBv9RvVyX_wgmvNzj12hPYOmQ6XMUe7swtnjlpTg6sDaj181cVLqu6eAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه نداره از دوره بعدی بیای آلمان؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99336" target="_blank">📅 02:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f8503771.mp4?token=FHlcjMrfos9KR3avcdWazgrVH9WXjE5C8m39ny86iEHwC2g-rsn8FPaEfojWTGRhbbobpAc71i1ueCbnsoywBm0DI1_R5kb_3xEHkIDxkii9SU-SfQHUkyiSxrvcWlGtFx1LQSctyCBLlLygTcpombcQqsWn0tcN3SZwEjKZWQhuVTbF-3WqHLPW5JO_BO4JOKRvR4pQgxDouY8NNjuxphFUM0xkjw3mfeyvdEAYf_5wB40yFC85RZmkpNXKrQ5w1Bylt_HRNnXhYERZARLJ0lAxMSmFk9Le_9Sm6zgte5OkizhESp_7sJuRuvEkX9we-JUx00Bk4VT4oiXV-gS9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f8503771.mp4?token=FHlcjMrfos9KR3avcdWazgrVH9WXjE5C8m39ny86iEHwC2g-rsn8FPaEfojWTGRhbbobpAc71i1ueCbnsoywBm0DI1_R5kb_3xEHkIDxkii9SU-SfQHUkyiSxrvcWlGtFx1LQSctyCBLlLygTcpombcQqsWn0tcN3SZwEjKZWQhuVTbF-3WqHLPW5JO_BO4JOKRvR4pQgxDouY8NNjuxphFUM0xkjw3mfeyvdEAYf_5wB40yFC85RZmkpNXKrQ5w1Bylt_HRNnXhYERZARLJ0lAxMSmFk9Le_9Sm6zgte5OkizhESp_7sJuRuvEkX9we-JUx00Bk4VT4oiXV-gS9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
😆
برسونید دست گزارشگر صداوسیما بازی امشب مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99335" target="_blank">📅 02:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99333">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sL4NkLxQIasg_NzgicRFffN6UXKtPdtOZtDkcHVpL7qFn_f-aNXrwBYLlULRpd6rPo54v6F5mAxMi-qngtCj6UY61pYSYIgEEFoJqgTK1EGsqPaFC6f3Lak4I3vXqdxwIl9IKEkZ0R1iYNtoHjmqNiJ8v6bYReweNn5rYrVo1xLUUTKvPZ6iPNMqqIIGaRlmlkYu6joZfVGjDalFNlCOp2r_ojywledX_T4TWHMPorqZTpjUwYE_bxPmW7rLWarcv9fgJD0ExfZhw9rZp9FSPEUFGxd2y28X2pwbjts0YaBvG5ikvaU6Y3ZoBL_Y7QdUB1pl4vGxhefPbqRsf-eM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_O2VtGjtG5_QjHrMehHG-VXPmFckwfTVq5BlO_xiFbBqDkEwBtCGPQHJGcNqW5kmjkN5_u9vbvfGYMwzub4mGg0mZFPo2YYicCUL_UU6z29Vnngb-d6NV6K_JRyv5o96cOfO2l94e_c1LzTUp5LNt1GJx2l9N2Z-wgVGpqsWEFDJVvH1P0BGOs7pajI8nbWSdwcc9w_hLJOG-S3vxjmxSUaLg-5d1eh9q0km3s0TrI6WbHjR4BDk2lHw51bNaA98-WqBHydyCCp0L0wipEzZMHAlGh_Qlb-l0_SG_fMuHX-IuFwvf-tzVxcaLaa4ruuFqwbtp7UNpbyodFI-uyNcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
📊
🏆
در طول 60 سال گذشته، تنها 4 بار پیش آمده است که یک بازیکن در یک بازی از جام جهانی، هم گل زده باشد، هم پاس گل داده باشد و هم یک پنالتی را از دست بدهد.
جالب اینجاست که 2 مورد از این 4 مورد در 3 روز گذشته رخ داده است:
🇦🇷
لیونل مسی در مقابل مصر
🇫🇷
کیلیان امباپه در مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99333" target="_blank">📅 02:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99332">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
🇪🇸
#فوری
؛ بر اساس قوانین لالیگا، بازی هفته اول بارسا و رئال در لالیگا بدلیل داشتن حداقل یک بازیکن در مرحله نیمه‌نهایی جام‌جهانی به تعویق خواهد افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99332" target="_blank">📅 01:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99331">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgROE3WOaHNgpOGjskKbzt8XSymXr7gkDb8UxPXcvAiwlXm2S2haQOaiMPUgmS1vIwpEevNJhzEXT78LDp5FIDiyGUXe9RBjzJfh3Pku3XpI0nFcWsMoKSZJHQIf-x1NfJsarvgvQS_B_q__w7cySTpNJauyJoL7SL4xZ-DZj0lLewW1_ORs7OBZJfyRoYmSzW8tkz6TwoBIDG__WUz4tAnOdopKv5fg-MVzGHDockFvd-7IslYJilMCj6I6H1_jPE704_PCquZzEe5kjUfq7mDjizf6Y5d3JZPtwbpYmnX4c2AHbHVy-XKAIWAFmRVB6sPsMKKvfVnzaT2YAz8h3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🏆
| تیم‌ملی فرانسه با قضاوت داوران از آرژانتین تاکنون 6 پیروزی در جام جهانی کسب کرده است، که بالاترین تعداد پیروزی برای هر تیمی در تاریخ این مسابقات است.
🇫🇷
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99331" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99330">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqINMFoAACVugTFk0jLWLMw-e-Gj5cNlQkxL9OBUhxHpTOKDIkULP4lcBzrl45cC_iDirydo6GP7TXVWcE4s0C2jvrRIUkZU6im5Um-y0ZPrVIqUt35Xd0XubOAGX_HIGOBQNsJ26oDMpJKIHqmeMq7eteCxcKaeuRGOIt64CiA1n8KiQWxSt8hlBj34J46Vkw4u9LYreNB22bsmzVJn48lkmfTWyYXBdrXbrGaC3fYQLUAgbyA993F5uzzG63FtcCdujY3JgzVq8ip12KoWA3oD0lGxn8bK3Eq5IL0Xm74NkxcgoBFrumZ2cPl2wz3bJzfKcIXy3r-k86J-bv9u5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
کیلیان امباپه: از ناراحتی اشرف حکیمی اصلا ناراحت نشدم زیرا در زمین مسابقه چیزی به نام احساسات وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99330" target="_blank">📅 01:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏆
Man Of The Match.
🇫🇷
👑
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99329" target="_blank">📅 01:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syJLkyPTTzmTrwVbmRLBunUuvT_xrNjQtJwTgsMCsDOzkto-68SS770hqu86A_DLLkDchEqUvxgnDT5RKarYwnI9gyHi7MIRu123SKUTtmtqE53aPP22DTe2pkhrVdi5JeiDjFkZfBYTd_SiHwEhj97oTq7pxKAGVaiF4k4TGDh2ZRixIYJ4kGHNshGZWhGbq4JEa8tzfKu56SZHEcNdIfeNOfZcklosU4KMoq_Wh9iPOX-Spsz2VWR0hVWSv9I6WEbCooDGayaENjAj70oE92jztd679Jj8OC6yYsZfxbJl1QRed_xwvx6bDm7h-9T2xoF328nHZhwfsP1QIIsUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
M
an Of The Match.
🇫🇷
👑
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99328" target="_blank">📅 01:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4AzvouJ0jjwLOuLAYDKe3yhTiXIG4DhUzcIDNffMWu3RIGzIlqHLzGdh-FYDuMXPu6Ek7u1CCx5hl7mJexTOrPK4rZ4cLyn6OdjGWXo6IGh33b6s1VdKM-rni_SF8eUZgYeIwx4Jdg669lPS6WyJpiUg0zWtY4T317MQ-0EpnINlh_sqRpLZaJ9ppXHAJahD8XiqjyHcqr-4EjRQq-Iy2OXqwgkuHiBgtHpaNS7ySX0WpoMZomsoxxAsLHLUZIjMPtQRRcuXHbCM6dVjnTUyKQTcq3lh8GQ8E2orK0i5W9pIP-wIm9qNXX47vgAfmdU332V4utjtIkT-cgDmYS5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
😀
-
😏
مراکش
🇲🇦
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/Futball180TV/99327" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n160sYda8lCAdmlKJuKISayYIzLH44e4fSS1VUtcKjzj-46Gt-sl88spGeQsGc8oFCDIYQ6P6QtVACb5LaeIZ9v6-2e5EzgkZQrHY7CHrwAGyJDWJ_MwMgeobKrED41sW3_99-_CvgpY0eubdk_eOWe2wfMB7bVLOkxiRwR2S4_vV8LMrA5auth7_Kt02MGARiFUFlcutKB3PXzeIkBDLbHPbYSVaof48Y2g-WdBgeOmYz6WuOlQrKhdzdYxMokpKf_0jQSDkjVJ07KkrwtyPwxEMqayiRevBrGFPjyVxzkeQ0nY1M6XrAV-VVopu0oignCgRGGvu4i04YtHQlg5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمامی تیم های آفریقایی از جام جهانی 2026 حذف شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99326" target="_blank">📅 01:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2XXORevHOwoJwYcpAxw9nK3-yNrn_5GKiYULMROwD7XioOk_6YQbinqTL1VZ8MPZi1hthA2jJIuPDIZIGB_xxYdDeWqtMoN3XZN9j4j68GtGA08bX0EHDa_F-IAp1S5AK8rGlZ_XN4NfgB0Yfrevj5PC6sBj684OzDn3k5ZZwR87CB8b28fh3DkfTbOa3AZeBQ6QOSjeAI_DLXIrty-SfjgcB0_Mc7WoncSTBFHNvZaIhU7JPj6GPP5cNz-gShP9CoqFc_BxkX1_OVFr3otIphQk6xSYRlXA5ckUQoSR89F2P0ZQkBiqLyoCa9O78gX3c1yBLZ77Op2ZhHn-roJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان با یورگن کلوپ بعد از پایان مسابقه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99325" target="_blank">📅 01:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8cueqfJpLMMsNMHMEewc0Za9nrzjpzm6H8f6VG6yflKQjQ5bOQbtQdlrZtV-zmnRpAmYfQTQLzSwnETHcDx50PnCcMx3FmOqPYLofI1zvomIjW5Q9SfEQQetAmRvrLtIjPnWyanRmqUzfEuOdc8RiFIz_m__nvRqXguiUCeRJ9aGmOkDezO3Y8aV1m0MOF-Wvunk-icJo3SoPub3oY66joAglINYdHFQdckl46JN3TEcfUC2C_iECQ7HR3zVr5XzwhLfYk4uRMG1TFDHDxkW_wPON8ZLLAgvdvIAKeztN4n8e5H2a90gVgX4Cy5guPpzKPNsarIcXrpCrkrZUOunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• کیلیان امباپه در رقابت‌های سال 2022:
🏟️
— 7 مسابقه
⚽️
— 8 گل
🅰️
— 2 پاس گل
🚨
📊
• کیلیان امباپه در رقابت‌های سال 2026:
🏟️
— 6 مسابقه
⚽️
— 8 گل
🅰️
— 3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99324" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq_HtO4lCKukj4HDXhMrO65KYz21zcP_F16dhlBPm1rZGpdI3Trj0Hy7RX_gbf1Wsd1K74v2RKlKZBZOAI4_nOSqrKqvzqCKGj3tTdw9itdpK0UPhNnJROoBQoWpAZ3Djp28Eb9nXL34-uT2FV4EAaAyFaRpgW04Eg5cmrIfBbL0YdgJ1sFRIypXLXeRwWQKLj9onnPm6pJlL7_kmkAG2_Z6lrpUGh6QtAZntd_Na4hd5TpgXvaJ2AUGL3xOLEo_g2ocY4Hkpm9Vudo50xivVao8fHvqy1YgJ0d0UTxmUTk19Gouwb471ofB-yI_tHpmm4DsMe-aTvzHzc7p0FeCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آخرین آپدیت مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99323" target="_blank">📅 01:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99322">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrwfsKXxYdIwPOX3qXV8MIRYuYDZAMvyAVSQRQL7wbEx2i1MbAb4QkcbPMqRABd-C_as5e8IaoOMemB-klr-GlSFnqsvzS1XD81VNujGQtfZLug8V9V3bu8gB705-fhWdb8O7La3fugLcUdDILZb46v-H7EZYibQsKGhQmhoJ3-lCC6YpAUOPaU3D41dBfghOXeme7lvpUXs8wy5dZdcLB7AN36TI6e_s1QbT0Ng0JXvwMmjshN3yBtvUXV9jV9MLo6oSjgwMNjmkwrjDiQC_FUsGUVgZCOMlW6CukB2aK4ZpqmD9tvARPpZtm0C4tOKGfwdspb5iqq3WvqS5cG19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 بازی در جام جهانی؛ 20 گل، کیلیان فاکینگ امباپه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/99322" target="_blank">📅 01:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99318">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTc54q-TXy1Pp8k8Kiy2-IHYyMuApevZL8gXuyplXOy6AijC95vbhtyPzp3fPkSOUHkvCw76daRXaYHAar2IL9bdFxzXmSKlsabbdqADtmpp_0MP9jYk3bOr5bI9dX4RjE85wU7kBDoFS_yrgW9vHhmARIuqyQIlIpQah9VhIhftu2Kg_72R8mMBUic-OrFqm5Dx4D7SDDSlZ21lm4oXHPkIxVcCE6zFBeEMRWLSwZ7bPPHyyLgE9I5oiaqazWv2rAdzDSna7o-EDtHXgdrRUVbFoETVdc4JeSgEIWiX995EHaDUqe_oj4djUkwabGGVuQT0trD58uXZOluRpEgSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfcSaEl6ZDXSXD9Oyw5ckoIJ3Y5yupp6m160eqkstNOvJu4eIa9Mb1F9YxuYNRzCs3NQChd0H7jcP_le-cK9gZAsU8BNKWS08mDtNBk5lxUXZuSFXeSi-XEIf-kh2-krAFNj-C9JTXmjyydByL8UjkOxpUK6meXhBy6QvPH02848xOq01aMG_FiYgW8HA1_7wei9FtgZ5paFJWG6eYiMpkcYWrAqzt0ssAs31pxSsZpfrtQZ4GxatXxB9GDFE2ZJ8dDATgwZ3siArLEb3K-3A0USuc4yF5J24QuerALEfBHqzAXAHjNPgZz0p_fy-JS1CeoOCESZKweSzE9b2O3mfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1lohrNWHlCDBNmsDJiqAlFiih5zyaYeru9yc5a8FpDNh2dY8abMc5EQFy_pOfNU_rLPhpLQeDe4BQlGPKYKR6gXSZI4liqlyJ2r616ShVOoT1Y0I8G50JQZTqdjWVANSZu7ZSnvBYR-1uUoQj0gmDS3gdwO7cheYZ1JL3NCKVjs6WxFCdcNdSmPLVLx14isRNHpEPFHsOpMZpaVjia0RxeN9OaOjPSPB7N1DTdjsF38G_kk6revAj_l_cwAHKZtQUQouZZSvPKj5-n3AQCUf4rWMBaSkMsZl18n7a9JZfTBlDuDCDWzF9W5BFmrKxAA_FsQVKzaGnZOSXyJ6oEWOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3B-Gj2qJ_eEl20vz4i2I_WpoGvEbQ1RAqstTvklA4kJxHCHRy1Ir7e7Sgx0ZVZAw8BtF1E0144j_B-87OWvuiti2QXKx-60_pEO6d55fKn4Gaa5YCkV4zARRkzbwBG93jC5mTe3M17O2DfZ9RRe2vFhR3BJz_Dv5XtmPazM2w7ZFUISEjsfsFuRmJSNjdwKeUwLcIC1TUzgxZwKJGbuc2ax0hKJCSpeT2V6W4FfNnioWYeW1bptCIWiOZK79-EqHN2ZPFOtX8BrpxMDSzkiUi48ISz-z_eAXQYhbdQZXfDU93ueC3dwPu70idO_eA0vbFYjNgZrACix-ZQzQ0Z0_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🤯
📊
🏆
آمار گلزنی مهاجمان فرانسوی در ۶ بازی اول جام جهانی:
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
🎯
🎯
کیلیان امباپه
⚽️
⚽️
⚽️
⚽️
⚽️
🎯
🎯
عثمان دمبله
🎯
🎯
🎯
🎯
🎯
اولیسه
⚽️
⚽️
🎯
بارکولا
⚽️
🎯
دوئه
آمار فوق‌العاده‌ای از خط حمله وحشی و عجیب و غریب تیم‌ملی فرانسه.
🇫🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99318" target="_blank">📅 01:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99317">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9k95oxljQs34B1ZO4YkaySoWc2jZzNok5ChbcMYa7dvKnwrbxoOpFsgvAQ27zrg0T8VNDt-ljZ6nzoSENn4S6fvFS1unAgpjAptj1D0i9Mf6TdGWSnUdEiUMBpKRrIsXvOAmfgCa1UUEA_KRX62QHcN4dVVaj0up2E2XLqOkZWrauV-eXngV3d5i2Xt7FCO3Trk6RMGlro3mIO5_ZjAoAIjauZEUa_FSswyal6zhrhDXtrFVdTDcLy-Wt_cNMqOg862qyV9WNFDTN47xzpZTu6P5M0-vadRFsUa3iZh363Sc2Cn49j-7SR8fHGPrgsIandw6KOrzt0E4I-AoZxT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه در 11 گل از 16 گل فرانسه در جام جهانی 2026 نقش داشته است.
8 گل
3 پاس گل‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/99317" target="_blank">📅 01:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99316">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXfRS_qY3GA8sd-ld4BPpU8XT-BmnksL0WJdWiObnSkegu9iD2WYSUQa1M4cIpmSitI7nhp7WPq6PzBWg0Ofah7gYJvsJb5KC-V3a20l4l5S1EriFocCWXRahUEGPBgibl7UKdDjv8jXIprqh2sXaqGijMJw9wQnHHwnF9RZlx5njDdWcy11ICIX7eNZ6fcvaAvyQ8ycoVG3vRh3wZy7_bbE1ULMk6cev4n-9CkS8OnWrjWg_sM2Prl8lygAOHErYW4ZZTyIiNqmAhdVXA6cvSNjYRDaFWQLVI3ijpVWcy81oj76_RsSMj6Bhq-g2LpzN3cWoSWOG8u85_kczMN1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
کیلیان امباپه همچنان در حال تاریخ
‌سازی است
✅
اولین بازیکنی از سال 1970 که در یک دوره از جام جهانی به 11 گل یا پاس گل رسیده است.
✅
اولین بازیکنی از سال 1966 که در دو دوره متوالی از جام جهانی، بیش از 10 گل یا پاس گل داشته است.
آقای دیکتاتور کیلیان امباپه.
🇫🇷
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/99316" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/99315" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nWtAkXizy_Mo3QaxL09IDfH1jAbtcQo7IkoS5aR-iSqCyptyTRzYX7diGZ-2kYWUBLabTKV2ctMZvsCaDGP9x43pnrlyPwP16VJZpfTtFFpMY6Iqg3vt5xHYr331tmDEf7ACtak0veK9CBCXyGxUxZoVW3inhzvHWFyYLb-RZAZN6NdC0vWP1R88ueu03J9kNSsuvbsCsFnpU-hWONPauU4BypvWEEJlqJ48Bwz5S4KQSPrSsyJAwZ-NRMtL-PRIZ5bWzwbvb0LhWKWfDcyU_Sz6jnUETkxH23Fu5AqIvTdKkE0pYdkzjD7mwG2Bow0nISpy4bxR4Cc01Qn1DHw0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99314" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj19Iqyj9fznVgkmcYbR006lHGCikJJHhT90H56Z6TFBHfayYedmQOiMu2JiBkgVFKQ1WsYeZ9Z5jW_e6nTEuIGTCqHGedWsvQX-SKrkpiamRQC2owWbIJoNjjYNA0DeRW3tXIxZ4OPLIfoo1kPgdZHLyuVin18Ww_cCtHfXjHGHF-TIXJiNWCXv8bapj7zpGm82UbBGGHIKBYHodnxfacYpEqPDO_66My-FV_VCgIVJoMG3uHRNuiJvAzdAsBfWkRIEnWSloMuek6b5wMbmov5PFitl1RoNOJUCKu6OC1EFxLQjbKXB0DqywAcZEXj4IvUqmkrMJ2xTJZ9axvv9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
کیلیان امباپه بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/99313" target="_blank">📅 01:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJpWOCxBRFf3xMUkLeKxx_YXQdliFsnvoVWfCMcmwBEzeGFrHZd-AYtdk7VytHzAstLUxilRhcydbXBv97zLlvwewNa7aqiVxNHGSCNo7Cqimz1nqvPYfcZdzVRIPXNwxPHvAWxcy2SW7lICdsdPxQMuZaMI4wOGZv6ybp0WRnVdIvftelISntVcvAgXNVt0y243m_-jSh4c7GVZdQNllV_OPgmGX1TLJyyCpOv1u9E0i0o4QTavqGShSeVr6-gMOB4k7FqGagshdbU1rRfi5k1su9Nkoe_nn0g9TQD2by-1nQrSP_BP3lig5P0H99bGPxCV0tr6kCu6pO8hovrszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنده دیدار فرداشب بلژیک و اسپانیا به مصاف فرانسه در نیمه‌نهایی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/99312" target="_blank">📅 01:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99311">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5gnuv4AJBLzAR51zGwdMfvIVI1_426bwVL4K43K45Ncls2olGhhjckJst-JiWFXj-WEChgM04sE-E1SDeOEoeWf3fo4lORYjRQ-_0ZoD7gQEhgrm3JkTeEk2n0PsSe8jBC__tuetRbJIv_4pfAJgz-QvznuMqK3dIIFfORvytH3lLEkoAObgoTFfxCzYk91OgD1oDD02xd8YLLWAn_RMvzC9K2eNSd7fHIZ9l_KNgYY5gzMHYCLMahtnznBupaydUV25OKisn52UMfGev9qy6se8-pt5ErCEKqbpdiVhMFmW2ff8clvqYeDa5kxc_MeeKa8ynRI8PVCCK4bMyIeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|اولین تیم نیمه‌نهایی مشخص شد؛ بوی قهرمانی شدیدا به مشام می‌رسد؛ فرانسه به رهبری دیکتاتور امباپه با برد مقابل مراکش برای سومین دوره پیاپی راهی نیمه‌نهایی شد
🇫🇷
فرانسه
😀
-
😏
مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99311" target="_blank">📅 01:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99310">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl9rZ2oAfg9dRgV6qE-1wN3R2_D5XzMIb6DW9-1M96qUEJOY9sbYVnvjpuyO8sZpDm-z7rJscyU-5bd0gqidZKLL-KpwKM_83JZS2cYnTkI-cdj8eSjMxsVjVF329JE0g5idpvC5PE4cW_9gQ7M-3TqW7tImQBGwemigVARhw6_8TtjNZTBsU4QrR7Rr71CXnZNVcop7Fp2B6FYqmJ9p_v8d-omHzK8sNbqnkv4LuM4EKXM9awC9y_JqyEpnrtfLD-CL1JjzTbguph5n7hKo6Ww1MS9ZnhSp3WVgjJaF8y_hqIwjBLBdoZ-mn3CCTSQwHSxrKxFOYBZVcPFivueczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داداشمون چرا ناراحته؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99310" target="_blank">📅 01:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99309">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXDzthJmfARGpEm_HJmZGTgvMb6mHSX6wiEnIagNpT6-yuOjjEsvTXHjNkjKq5iDMoTDq0SeG3GobXXldEfyDnqG4YrjZ9_gxOP8VlT-oH5rQ0HTviWp_-YFp24KxzsBPCcr78AKXgi2OTEzbyUD03dw-ysXGnWzLPhJJXKibpoM4QrNbLXNfqcPbiPk-YKLEJEzwe7T7NuWFHfAa-KzWSe_iIMUPYEV2hLPXF_lfOoOevj8ChCk8Vb3n8BLR-1JoI4s_Sh-BBkJU4gORmC4o0SKOT3wivws6y1mMjfvUJDOSF3S6Q0nhtg8HN5QCEcpdhLPnKprFYmNp2HwWqf4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
کیلیان امباپه در تمام مسابقات این فصل:
👕
58 بازی
🌟
68 گل/ پاس گل
⚽️
56 گل
🅰️
12 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99309" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99308">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">باید یه تحقیقی روی آربلوا بکنن بفهمن چطوری موفق شده بود از این امباپه هیولا اون شیر تعزیه‌ای که تو نیم‌فصل دوم دیدیمو بکشه بیرون. این همه نبوغ نباید یه راز کشف‌نشده باقی بمونه.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99308" target="_blank">📅 01:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99307">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5N-epY4b9-jDJp4KshPBqcTpHsuij0XAR51BDtRu1T77-_4Xc9AjH-p9qjrrrfF_AomAKMUD6gbLAZtfDThutF_7gTHzqoIrZT2LX7xrbjstbVAl3JGMGAEAqFAIzeAImbMaMIr2eX9UgMeaIg9lEA_JetL5xQZ9yOJxJ4En9YEVFxZ4Aqp6Uv_1iIfjMJng7_VG_fZT-_7tusErC1Kj12UkntBdaQrT0G2xBbLKN1CN17k3JKWB1XBDT27ZAnnbXM1IZWmjkw9rO1oXfaHETDS75wNvnrMKC5scjpnZHP3yl5ae1ZoUMowiUDN4a3eDtVh3TmPyHeXnBNxihT2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لحظه‌ای که لاکشپت درخواست تعویض داد
مصدوم شد یا خودشو زد به مصدمیت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99307" target="_blank">📅 01:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99306">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امباپه تعویض شد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99306" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99305">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGO0oxGXfOHguXCsYqLuixu-Zap_AwlP8mB5k927WqA_MZIfm-kNS7IGPBA1QOD6RYIJpfKBpHG7ez6rv-zbIhtRFSnIJ_RYKpgLgvYIomqBVTftDFKqfoQRuSzlDO1QxKzf0i5Jw24du__s3yZpRLsWVfW3GfHVuth_fNxNQ9b3Y3tz8yvKn_8MjO1nJxUICq23e4R43sFllyoyNEaBlgE0EAej4uux8oUEKISwnEEhCwb1tK6hk6v2qQksxcCLDxBALPwh6avNBuySITWgToR3rhjkcDZbt5gsJpqs0aH5kxFsQHLRyMV_OUP-tjPw4BMkknZN05_m-Sh2uTxJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌎
بیشترین مشارکت در گل‌ها در تاریخ جام جهانی:
🇦🇷
🤩
[30] مشارکت برای لیونل مسی.
🇫🇷
🇫🇷
[24] مشارکت برای کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99305" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f95dc0a96.mp4?token=gtnfcx-Xcqxc_BxCo0HiQT-yRlyXUYcPPCt9xtJ5Xv0W7NMQdjQ7bGQjn4mtudmEHUJvjwhyhLdAa0A_hpq-BVuCzvXI4WslbIOd5rHKjjmWuD2HjjKwcoK0fcL0DtctuEXoxT2F4SwgIO0KqGw6z-1k_uOcFC_uzfymtCjZu1FbCmynHnIwNuEYs0PtSrtLPiNj7o9eBX8_w1nvIv_QeWAA9f2sScOBBwNKhYQydqqknOd9ypfDv4T8rZkld6pGzWuSpAiiJLufmYAdv6TPlNkxn1OyJLml2tbXFu3LuXy8QWO4tQiz8q9qJpypCltIUO91EYUfcm0vTXcWqmFf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f95dc0a96.mp4?token=gtnfcx-Xcqxc_BxCo0HiQT-yRlyXUYcPPCt9xtJ5Xv0W7NMQdjQ7bGQjn4mtudmEHUJvjwhyhLdAa0A_hpq-BVuCzvXI4WslbIOd5rHKjjmWuD2HjjKwcoK0fcL0DtctuEXoxT2F4SwgIO0KqGw6z-1k_uOcFC_uzfymtCjZu1FbCmynHnIwNuEYs0PtSrtLPiNj7o9eBX8_w1nvIv_QeWAA9f2sScOBBwNKhYQydqqknOd9ypfDv4T8rZkld6pGzWuSpAiiJLufmYAdv6TPlNkxn1OyJLml2tbXFu3LuXy8QWO4tQiz8q9qJpypCltIUO91EYUfcm0vTXcWqmFf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌دوم فرانسه با گزارش عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99304" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAB5Af-0ja0Os9LtEd1RDDURATZaKMFDiAE4WfaNnsaD77HfWvem42vB3BX30bBTJivIjj5qPbTb9X3v7hNClLUOfvQjGtswbcDlg814mA9DwTXmPEiWCU_awhR6APVFbSP0D4vYU2mjYIZZphY0V3uQ0AgKYfLQ4tH54EYPS5dLK02eGyhw19VaP0LIBRVKd4BE5juwC2skTBJqNahGIeYt_1H6mhauyvgrQSaqeGn1bGFu6f8fV8Ywvp4OE0jn8h39r7azTn1Fl-IhrR-_HAc6Sy8xiX7-S9MpcOhefx3SifUIS-KMBhZrKwPF3x-fb4bT-iBDzhW1CTPi2vZeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار کیلیان امباپه در جام جهانی تاکنون :
20 بازی
20 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99303" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آرژانتینی خایه کن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99302" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چه سوپررررر گلی زددددد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99301" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دمبلهههههههههه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99300" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دومممممممم فرانسههههههه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99299" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99298">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگلگگلگلگللا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99298" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99297">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-rMZtscjcLlAyLqkVr2j5znhXEAh9VB9cUmraThygIaZBJBbYViih5yVkbEJDkICWL84YJ0kbPf-AmItS1OwUrZnADTPpo3GKeJwT72ZqRviFENsqJIOOtvPZZ8a7YhHZsKAmGG4EnBeO8pmekezEP7Bk4pUCt9du4ENBnWhu0W3fwl_0t_y3BBj7xJUR1ispxf9C_mIRi2QoskUHXU3d_oPS2Wd6DFzOj4hgk1s7zdWUO0ShXt2s69i5w5apJUshXZkVQpP13QjsAw5gd8wZ1KtiQSp8CfPGLT4DBzkoYI5MQzrIWXVDeUXaMhcbWIERIz7T60mNX25t_FI8YzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گل‌اول فرانسه به مراکش توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99297" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9SiupUp_LTa4G7idFGM-TicBFyiQkQA07a3nLDVFS2tSIjzLVFc0YzGdyb8ORQovyIRxHcllv5ntIfxnv00KGpnvWLBsq32pHSLzK_xjeOzbaDdQKpQCsbhfJz0EO-ICXI8MEG42TKDdRa8Ib6EDl2xxZsu_A_rhImZqQ_eqQppXsmQ5706IDb4hP9kN-mpKGetDpuRBfPg3ovp71zxOOLLmDCbgKgGzz5YQuowrrMsilRv81SLbiBnmQ2IzpddMPsoG0p8-opsnEJIr9MNTwNFn7DhEaQcbIr3Sdobult0dxUZYf4ipDOSW2fOaPZQ-4qsgq1iNV6YnHIos3Z0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره بعد این همه موقعیت و 16 تا شوت گلم دیدیم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99296" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99295">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3ab125a3.mp4?token=MK3JRANWfnYTALq0V4ozgiVHA5dHtFpdYIMVlqmSNYRNuYGE3Rt6QGQOn-Uydsi_CXKeXfwquPdeYjYAh_H6LSPnXn5JDlwfHg5x69uFcLwOh-MQmtlsd9Nccfrw3jOFcMV7e2ZGGZjij8xLhudoQHA_dJPcEXTINfBLrCZ25umLkhmOsot_kIOkuRcmcMP_uGe79ZV1NVNuwnmvkU3MqLUyUViwYAIBNYekylBa0u8LgjzNBFbR-j0oY2Grn0aNvjz4dygLgwjYllgqwR9-4PF2lAejdIvs0LmN563O3aLApKMWIg-eKEfxUMBecuqQtjP9PZk_fNNSUUF21jf87T2Gd_MazGymtZ2WoZE2f3Cna0nYOej4ZYmsVvU3SravcOkjalEwk1Ungy387y-0aRVNgGHGJFvzWLlkEwsS5Ys21SC7icm-1FIqEemFK5XAejKTViqmZCxz_cjwd7ATeO99AFkHVwJ4R6aeKlNzSoVy8OlcHuagTU4xzLh9-3Z-OPRlb78ovg1mbZjnK0sZdJWMBCQBcquKSCJljVWEJtL5WZBK3SQ4fypaIHsnuGlJGr6YSf10xFfnOHeg2gvNxdukkWYQYGmyPpnbNKd4MBcWppuSfaRDf9Oz7Zu92Q109bXajGeCMK-TlaKOFR6jwgOcujik_xBQ8Q3JfEcT8fU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3ab125a3.mp4?token=MK3JRANWfnYTALq0V4ozgiVHA5dHtFpdYIMVlqmSNYRNuYGE3Rt6QGQOn-Uydsi_CXKeXfwquPdeYjYAh_H6LSPnXn5JDlwfHg5x69uFcLwOh-MQmtlsd9Nccfrw3jOFcMV7e2ZGGZjij8xLhudoQHA_dJPcEXTINfBLrCZ25umLkhmOsot_kIOkuRcmcMP_uGe79ZV1NVNuwnmvkU3MqLUyUViwYAIBNYekylBa0u8LgjzNBFbR-j0oY2Grn0aNvjz4dygLgwjYllgqwR9-4PF2lAejdIvs0LmN563O3aLApKMWIg-eKEfxUMBecuqQtjP9PZk_fNNSUUF21jf87T2Gd_MazGymtZ2WoZE2f3Cna0nYOej4ZYmsVvU3SravcOkjalEwk1Ungy387y-0aRVNgGHGJFvzWLlkEwsS5Ys21SC7icm-1FIqEemFK5XAejKTViqmZCxz_cjwd7ATeO99AFkHVwJ4R6aeKlNzSoVy8OlcHuagTU4xzLh9-3Z-OPRlb78ovg1mbZjnK0sZdJWMBCQBcquKSCJljVWEJtL5WZBK3SQ4fypaIHsnuGlJGr6YSf10xFfnOHeg2gvNxdukkWYQYGmyPpnbNKd4MBcWppuSfaRDf9Oz7Zu92Q109bXajGeCMK-TlaKOFR6jwgOcujik_xBQ8Q3JfEcT8fU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گل‌اول فرانسه به مراکش توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99295" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99294">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گل کاملا صحیحهههههه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99294" target="_blank">📅 00:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99293">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امباپههههههههههه
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99293" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99292">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بالاخرهههههههه شددددددددد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99292" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فرانسههههههههه زددددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99291" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99290" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k2bu9l8tVg2mPO6ylduW7b6-839zMKVJGdieF97R0QWSLDsjkEKcZ3nOc9RAn8jzM08ZLqbrax1oj0EsCuKtT0n8UTgvxyHm8tg3m4gdgwihi6tDgFGKlsFNSgiE05G3fjlzUo1Tj3JPbPvJmE7KGTIY2larStSitVWu7ORK54YFu8aVeypF120WomrA35Pr4V0OR8982BjWk1k4sZLaGplGFpwQ_alorOLIhagquNwtN81nAX5sIjj47cCjp1Ij5BImFQ6DfthEsRYBDDrzxO-cMB8uO2E-ZnO6kPBDgR_PrItKDtJK8z8sUVWNTJ6VOR_Fm2JR87y8QvBv5sZzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99289" target="_blank">📅 00:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرانسه چییییووووو ریددددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99288" target="_blank">📅 00:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99287" target="_blank">📅 00:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بونووووو چی گرفتنتتتت</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99286" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99285" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آغاز نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99284" target="_blank">📅 00:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3tDS5Ox4OqvQYicHSblytHkRDoUeabhTfaiWTcMkuV0KLt44jzvYktI-wOUfYStzQYclEQwYMGH3Ub1nWQS3qzERYqwxn75Y6iDmKSiySwXhicrDcuJfrODZ0-9xNDDbfSbUH7tD4KtuTgrNwMejMgCrqR3u_mWdVEIvR1kgEfeskOAhnurGQlGyK9XlUnUcBr_1URX9m9PLBkPsTcWgRMAiZQ-26vQwZjBb9GSrJq88XgaDVpe7Fyvxrx-kWQJBPEtfAa253utOXusF_3Skk9PQFSHbYi08RkH6QY1Mi3T2vOnaijs5Dk_A8vE-4X6g8Qk-fw7mF-qkuVLbYhi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✔️
حمایت هالند از اعتراض امباپه
5 دقیقه وقفه برای زدن یک ضربه پنالتی خیلی زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99283" target="_blank">📅 00:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">😟
🚨
🚨
🚨
#فوووووری
؛ در پی تیراندازی در اطراف حرم مشهد، حداقل ۴ نفر کشته شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99282" target="_blank">📅 00:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvG1e5EC_9dDxnoduiMZSJh3q6NfZPDb5VGZYpLSfe5IWYi9jd6YQ3NZFbejTPbZxhUZjl-zZDjrG7YF7QcdanNRhAvQ-IO3_nie3d9fyAqJmyj8fmAIhRoX9PQWaf5Q7uNzPeJfJMdyJit5Zg9CLN2_sSb8m5Cqtb5_B3zU4CEzlblDAe99DH7uku1Slq8n-J-uASH39Lj3ipEC2wXROl2nqLR_QTHW_vlINhm3ka6dnXF5bYpz5mh2YD3-n_qL9UFB05A7tUALASe3dVmhac756LG2AXUg5ZrY6ynVoh3Jy4svqK17DJr7fw3RaQTDH8KZttyRyOjG5EfVo-lljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌هایی که در تاریخ جام جهانی بیشترین تعداد پنالتی را کسب کرده‌اند:
🥇
🇦🇷
آرژانتین — 19 پنالتی
🥈
🇪🇸
اسپانیا — 18
🥈
🇫🇷
فرانسه — 18
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99281" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
پایان نیمه اول با تساوی بدون گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99280" target="_blank">📅 00:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQJ_JtZplRv9ruKQRg9qkWTvBIzqIzSqmrxfln5YLroeMLA6SAaBQB3pfRk_UQIIxN-DBVS2BfxGGu_ZzIBRv7c6ItgAPaqEDChaWC9QycGtRwE2G63xuvOJhmQ5rLUFceAvpw5ohIoT0TB6Hb41kkEvA5ZPgZLP6S2d8QHw5B0udCEROtFD4VtxwED-dqPAhfFagzSzSHE0E-2MAPAiTvYfYj_rh-QIji2NEhBeO4My1GqpO5CDH7Yd5uAMDV1EMlyGX3U0R3_FUyArDNj-5diTBv9kRZqfhEoJfBuglirsNfi42XnruhJByBwT3E0y7pnQQcJbj7uEyHaCvQlRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همه مراکش مراکش میکردن همین بود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99279" target="_blank">📅 00:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99278">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EO68vRFgkLxCtXoo-2H_MSLzbdFJ4Jf5AT7GtzfKTAQ-4VsieWkI2CQe4tJZ2q7yj5dl7RDCq9sGPiA6lUv_dh7lotlAc-AEldUgYq9wU-jjk9lCIo-EQydQtodo4Q5lQ3blqhmCxXJdkM1Eam8fdN_xE07mT-YSPZoQBKy5g5qwpfzOnSDyR8BrqUdJCP3Rw_25wEtbVGuV0Rr4ittN4aKN37E9xOEUxdkaoR4wGyrDdFz1-4MTicocfsAGrAr3Bvz5oyQhpBaUFOM3oDQPZ01UpwiNMmJFyKPriJKPo0sLls5tSCH1iCfg9wR_QLrbFPBM8jBsMwcAs6tB9qzjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم شکیرا تو ورزشگاه
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99278" target="_blank">📅 00:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99277">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANRnoVAaqA14104oy2aLo8GSYKS_jSh-3KLP47GPDVXkH4r3TdCHZb5VAMQh4VRG9U_Ft5TXzqJanB4l2QHX2orYxlDe2962VNMXodQSNrsKnim_TDWt2WXUCkjxOKXV-wvbb-FTvr88u-HSQOplhffASiFQa0qn_v23QE9VXNUpdcgZmlVZooGfz1DA5DM3Y1ckw864HEG-Ho6XxNukv0J5Ij42wFJ6P6dCyz5-8TjCoCjN6v13eAmvzcU8wDc6hkoCNbLnzIL303ZcDGsdqdeQDXhQkb6227swTln_Ms4rnJk43oMXF9XjoMZBcJhfJ3o0JnXoc1X9rENmJIJx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم شکیرا تو ورزشگاه
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99277" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/df5b3f9b34.mp4?token=Su6UnOMoARCjTJTLcc_FS-8hDF1IglRLfKZBqVBRxoeFkRgdjgCyCC9H9gKMiGWBSkDZ1RadO3S8VNOtqpiC7eaAK_PDDxD4a770k79O1Fs3sURydoivxH77QnQfB2Y2qvCXJnCGUIIq_OvMufG9siWBj0NMJ__BLKv8vz7qXs4gB-i46IIEgN4rndNpRqdemKqQZ4bPMmzGj9Mjao5lTtuzB5pIxQ239NE4FVhOWTfP3w-1AFarFb5n2l7NN102lgVj_XSbGcc_PA9bQn4bL3w7b9CVcELXOwDnLudMHESIxIy0G1M59xGaLW_BEySHygF2PhxFd59VbW6nlBVeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/df5b3f9b34.mp4?token=Su6UnOMoARCjTJTLcc_FS-8hDF1IglRLfKZBqVBRxoeFkRgdjgCyCC9H9gKMiGWBSkDZ1RadO3S8VNOtqpiC7eaAK_PDDxD4a770k79O1Fs3sURydoivxH77QnQfB2Y2qvCXJnCGUIIq_OvMufG9siWBj0NMJ__BLKv8vz7qXs4gB-i46IIEgN4rndNpRqdemKqQZ4bPMmzGj9Mjao5lTtuzB5pIxQ239NE4FVhOWTfP3w-1AFarFb5n2l7NN102lgVj_XSbGcc_PA9bQn4bL3w7b9CVcELXOwDnLudMHESIxIy0G1M59xGaLW_BEySHygF2PhxFd59VbW6nlBVeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
صحنه مهار پنالتی امباپه توسط یاسین‌بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99276" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99275">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR9Hy4OmtkjYJYcT18xRFF_uGi0YRnLXEBlHnX8CzROrpn6qWQkkKsaDMX__uB0gtr_1pnybp6C9XjX1xsXtfqozHJ-e8QB-PSCg6grp0Iwj5cq0Dn-fZChgyphVCbHhXN7ah2vvBSy7itSMFyPJXF2cxr0XMmMvH_6WnF2Fckit8joZKTjZFYbwkhRTGwfKdITHtfFccIDK4rjXQv0vLS8Jg_miJCrHnC4Zg30S9nHp_ja4ZCkvLLJ3tIEAgYe0QZNdLrkHvcLKa-PyfgsI_Sf-4xx4dtPgXzZANxIF1OJjlvnyftVe3qv2SEK9OVE2lPUrA7Q2sH5_6z-FJVzh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید که تو بازیای قبلی کیت هر تیمیو پوشیده اون تیم بفنا رفته امشب اینجوری رفته استادیوم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99275" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99274">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بازم بونووووو</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99274" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99273">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99273" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99272">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ5k8l-lxLaZ1YlK5Y2ws6_ZnbNsowSuQKovf-g8H7DRsEFhjK_7gLESCejjzMXQozXkNF4Po9xrYY9Y3pPiprzH4M-Q81Qvv-zqCHwzc0uvGC2F2CxdWqHlwelBh2C5pP4ucwz0M4lD9bngOuEFJ-D4tuB6nSpHfxiEbD8km9TnjsRlQ9e_KUudROlf1jc37bnm5mU2uHYk3DF_ey1mWD4RGyR50YQPfWpomtX2zpLszO7RBXedwIVlVz0Qsy14YqgsE2fgw4B3xfJXxXtV0Hznb-aibmXUnrYmznm_-9GOcfkliVbKq3EXhnqsey6ckg-YNAF8f_rwnX0cjNqFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کصخنده‌هایی میزنه فیروز کریمی تو شبکه جم اسپورت
😂
😂
😂
مجید نامجو مطلق و پرویز برومند هم تو بازیای قبلی کارشناس بودن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99272" target="_blank">📅 00:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99271">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آب درنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99271" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99270">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چقد خوبه این بونو واقعا هرچند امباپه هم بد زد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99270" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99269">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بونو در نقش گلر مصررررر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99269" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رییییییید امباپه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99268" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گررررفت</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99267" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99264">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دیکتاتور پشت توپ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99264" target="_blank">📅 23:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99263">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">برای فرانسهههههه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99263" target="_blank">📅 23:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99262">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پنالتیییییی</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99262" target="_blank">📅 23:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99261">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازی دست فرانسس</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99261" target="_blank">📅 23:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99260">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7J4yu3ix-fK5GPfeg3b8gb9mMKHCzNnVOR2c5FnkMVG7YWsgPrSzXHR2BpQCKFV2jVSfH9wRTt4-vY-DAk9d9E3tkBHJrP0YAjVCZy6HGTyHvB-uADbcxVDm9gdNoyX8cCyaZLbo3-OE9yshGhT-6cXNCinfGcmCBQcktlwNkFjt4rpfuiIw1QvoImiad-KDusiVYG2Fm1cst4f8OEefRbhGXVVIYDOjQkOcTFpg6VJA-Rw2eo0dOOw4VkTqh5McudPR4CY6dfePUamTRMbAgvkIH6Lz6SV6j_MccB7qZXAK3R7jRq7cwwNm1qedEEoVhrbDM1SUw8wfZ9JkbYOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناسی کردن فیروز کریمی تو شبکه جم جزو آخرین چیزایی بود که انتظار داشتم تو این دنیا ببینم
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99260" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99259">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTZyp0uP3jilImrt-QB6HtwolleC4JwVO89Lz2E2HsOZHNqzzoaCfELrwCaU4ht_krEJRs8QVee0SXhptZhCdIwKeNZxHxtTp7NSV_Gb33Pn4tHZwIzaVeOlEznq9VlxDdmweZ2EcCFfj0KOk6TFp2BV4dROVrAcveuG8a8R8ZCH3YNTDco1oVR-BLFIfAuAfeJ0IoxNxDoiPHMQE85--4EJ-ZlwlTgA5cn-yfvGgzbnE3ZleublpsinN5nHZ1hchqiGZqZucpL1fJQYHkQKTZ86AoUAnPyQvx3vaHOOrhUmHXrDYeGupn5F9IRgaVEqIGJfaLLYcHNpd2Xt-l4KmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناسی کردن فیروز کریمی تو شبکه جم جزو آخرین چیزایی بود که انتظار داشتم تو این دنیا ببینم
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99259" target="_blank">📅 23:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99258">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is9nez6nowDZjwaF40EBlihAuiIIr7wpkbFoS1_q_LVIzGnM4bt9dkJZ15h0w3ZThBu11JjWQE4SQIXmWd4rd9M3RheizkkwgWx47T1HESweNbQg-ylM2rZ9WcIVAVM9--vHLyoZ_QYv2f58cum8kNU_AsOPRuxIGFeM9tK5Ayzb2kFBmm2F43ovWrvvOwfiT0743LMD7kCKwlJo6c3-drxQC--HA9BsFra84vZ9qOER9vbS-1elJTu6Uilc5NFShFD0LBUs5SuQ4p-hGRkvosY57Wf8HGK4AJWSs0SrOBblZjYA-5Kk05UJ2VBK6tHRurRzb_BHvBKm6XLJ1Mk4oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99258" target="_blank">📅 23:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99257">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">همه فکر کردن گل زد امباپه
🤣</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99257" target="_blank">📅 23:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99256">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چه سیووووی کرد بونو</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99256" target="_blank">📅 23:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99255">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">برییییم سراغ بازی جذاب مراکش و فرانسه
🔥</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99255" target="_blank">📅 23:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99254">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ50DZaX0yztwdLi2-zrYfieGQnHyA-LEoqa7uA9fC0s3g2Z7UHCUjU4Mm9ZdUA_eNHZQhykgRNQz5uTRgJbIJTLPjOo4OzFA9FWFx8fLf1H1AY1seiykgbjpJODNMDUEyJX6sSZkfYZ4wfOIoZSU9lVBcFhnk4lEUsbnOT0AfCZBLlTo-IqKzNBlqMv8XEZWvuOMrdx1dl1fmpZKLbMk5o4H_Rrq3HTpoJz7bKrVTsJZG71-4iCc3zoYYXG7KLg15MvXcEGwuxjjxrRr6eMTMtpygeHSfLFQXQC7dY8f0qXTK1UZc28rNCSGL8uTyFrNSGxFNssdV0OcEjjQlPeAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
؛ رئال‌مادرید برای جذب یک هافبک ذخیره ترکیبش به عقد قرارداد با بروزوویچ ستاره سابق النصر عربستان علاقه نشان داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99254" target="_blank">📅 23:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc725a0eda.mp4?token=CeeHredA0FUckoplXpqjShKs-msglX2KI6a3QwwFmad3xOCmxtvnag2ndOyAS5tw7xGmayKZqnu0aZfAC4NBx2DX0ORuRAwp0IQZ2nytS_7A1Zp0TSNN9A_7v56EErNinHKHG0H806D_7Gn3kGuKkbGUWFCytpWRA3slifiYRMveNXuoMFlgZIY8ftdB66sBgf7Y9JJ4FdZfGAfwjmcGzEFfRnFir9dK2RmNlhRjZsditNfK-0A2V-xuKdoOCXyf9_d5IAkUtyFO3FnQ6HeKzLrTO2poQ8iUbbrRez6BiIfx-G3mFPskse0EImMQCEyDS4qQLTcqc0HzRNaiwhEBbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc725a0eda.mp4?token=CeeHredA0FUckoplXpqjShKs-msglX2KI6a3QwwFmad3xOCmxtvnag2ndOyAS5tw7xGmayKZqnu0aZfAC4NBx2DX0ORuRAwp0IQZ2nytS_7A1Zp0TSNN9A_7v56EErNinHKHG0H806D_7Gn3kGuKkbGUWFCytpWRA3slifiYRMveNXuoMFlgZIY8ftdB66sBgf7Y9JJ4FdZfGAfwjmcGzEFfRnFir9dK2RmNlhRjZsditNfK-0A2V-xuKdoOCXyf9_d5IAkUtyFO3FnQ6HeKzLrTO2poQ8iUbbrRez6BiIfx-G3mFPskse0EImMQCEyDS4qQLTcqc0HzRNaiwhEBbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تنها هشت بازی تا پایان جام‌جهانی تاریخی امسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99253" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99252">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2CGwBJkQKrusqXxjkSuITp8nvzOe2DAa-n6PGAhZ2vkQIe0p8I6H_F6--21RQwMesQ09NMKv1wR8T1EatdQACOgj07esxe68DmlqGAGdee8isN_m18vpu7lkTa9rhdKbruJ2EF5LopCSExRsSVB8sCS2cJwaPJG49L62nmdEPLmMy1DZH307ThAsIr7nH8V5YttTKEuFqYL-PA1GthlkXvsNqGC-zockPwWABjDuk-x7uS0ck3Y8kYg_AF8cvjuU5a5rl-rqbreCuTlO1BsdCdt17nQdj4njehsNSFClUKxccYiwuVb6BdrDIu52nAO2_3Gmu0NVfAyR0166giv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مربیانی که بیشترین بازی ها را در جام جهانی سرمربیگری کردند:
25 بازی - هلموت شون (1966-1978)
25 مسابقه - دیدیه دشان (2012-2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99252" target="_blank">📅 22:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99251">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
یک مقام آمریکایی به CNN گفته است که ارتش ایالات متحده در حال حاضر مشغول انجام حملات نظامی نیست. گفته میشه کویت داره به ایران حمله میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99251" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99250">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
#فوووووری؛ شنیده شدن صدای انفجار در بوشهر، چابهار و اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99250" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99249">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z56DSIvuNxNW552Pz81KGHPbcI_ae6X0d_uq1dQYfYL_rb916X9jYzglQ2QwhPQpkJaFe16nRLdwTSbSWf7Y4Wc5SUtzIQzOi-aruDTa_9xZcmHDU3HJkierPS1tFplE13_4nxnek5COj6rl8HRMndO-C6cS4QdJVdqqlIwdUp7ISjrYjJ0GWfV6fgsynXps-bU-TB3qM4t-aaBOHle7s5gojGtcrpQE4XrjNXaKq-SIcar-NecHtXuY9fnxvxob6ojztvpGLkdvoJT-1J5LBa8Fc9zhQQmDQ_mLXrV2xpmD6V6mw7An6WYruV4xsbieYwUUiTpA4pGGsrqeJZeDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب فرانسه مقابل مراکش؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99249" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99248">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irutz77VdKmiTTu9p2IW8NgGcIKV8zK1zFgBC_bXQZRaSqgexW_s6IIcx27Fy5SzcippBbhZkaz5-EGFoChbMZ2VUqFtDgmebqcOj0Ybk53RA2aj7AfRuCKOYLaE8TWhiKzI1rYwqmgVVXnv3H24HIjMuS6lspVpBY-_zFc2d1iLGubBBY29ItEOf8N3uczELargPtOYFmGYUgwt0T_rLx6PRHA8o1MdilTCERiD44IGPYbrC_LYzvck6iqPM8djJVipk8fqX87wx3XFe-7krue54A6jGWjaZSzmYT5ugT5Nc6ojuiXSXqS3ZiBmBpRz3f5cKOhBdVvCb0401TrQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب فرانسه مقابل مراکش؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99248" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99247">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdImeOHgLoRg6a_Np-urU1Og0QVRCUwUdP66MxPLU4F51TghiBcWh7ruSLXEerxx0AznZUUjQD3S-TD3eR7yfTLBzzbiZmiHBiuwDkU_nKsqBekpfWvRv0j0lxU8wY-5hRhn-A0B76gKD5me3atM31-agPtHBgjDrjz-h5y51CrRUw-oxQvi7ricWEGqsizx5yUM-Zs9KS9OYXExV3Yd-38Zd_zbEvaPOtvtRZgHz8KcsT68k2KEQtZ-QakFa-JHJ2xiBu0We8aCae7wVhZwtvKVEY3BSPzp8bkLHk8Pez0AZxo6Q-cEGATzlIH4_npMFT4vMhzrFc8eIHx7bssGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر لیونل‌مسی با توپ فینال‌ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99247" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99246">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bfe433ba.mp4?token=sdBFb1Srva04fGq9nnqpIqsf8nneeAwby1sM2wsLWPDom-reHIVChni0F4I2xDF9xkzKfGOx__CZOIj1D60dFQC4sqihRbX459rBrp0OmQGA5u5u7Hh_a65-D1oCsmEWR42mDly9nPlPQ5_l9L7dlDEtaaiDrlhAsKvF75-EqRYKP9UxDHp3biLGD8lTOEtlPHU_94ADyhgyftjSIGs3mAm2cMQX2tqr4P2cYd7pAN240SKs6szp_8yh3y3bNGu1y7zH-gboGSyh2W34hrrG6YRo8J2zFBL-253MikjlRVy5P2g-XgAEJ0PAy0spfDf90mLPBiyI31BcgKKvakOT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bfe433ba.mp4?token=sdBFb1Srva04fGq9nnqpIqsf8nneeAwby1sM2wsLWPDom-reHIVChni0F4I2xDF9xkzKfGOx__CZOIj1D60dFQC4sqihRbX459rBrp0OmQGA5u5u7Hh_a65-D1oCsmEWR42mDly9nPlPQ5_l9L7dlDEtaaiDrlhAsKvF75-EqRYKP9UxDHp3biLGD8lTOEtlPHU_94ADyhgyftjSIGs3mAm2cMQX2tqr4P2cYd7pAN240SKs6szp_8yh3y3bNGu1y7zH-gboGSyh2W34hrrG6YRo8J2zFBL-253MikjlRVy5P2g-XgAEJ0PAy0spfDf90mLPBiyI31BcgKKvakOT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت رونالدو فنا تو دایرکت امباپه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99246" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99245">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
#فوووووری
؛ شنیده شدن صدای انفجار در بوشهر، چابهار و اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99245" target="_blank">📅 21:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99244">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgdoTqCt_2VHMN3IKz541SAIQ1gnM0qNNRguJy9uRkZi6KY6UfUj4phH2htHVNajp5toB_wT6D3WVEjcr3vd8HalGf2ZADpCcYn4QXoQ82ivu4_9dl9bxKvx0Ao4Pf8dB1VQArJCW6SzOL91lmjKCK3qUaTY2x9SGgef6sT8Qvz1Td-9V1hsMCNmL-bwv7A6XhNbiH2bGcWkq4RIpCypFPTQoD26M3AeYVQZeVfBF_EEZkHk7xxmqOEBNZFpoI2osz2i3lLfK8XfqzVQJZYR4A9VkJCFp3we9bAeg-kSmgpacrDXghiZPGALJDQ2B0UyrtKPgIzTalMKciGT7mFdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🏆
دیدیه دشان امشب با ۲۵ بازی، رکورد بیشترین تعداد بازی به عنوان سرمربی در تاریخ جام جهانی را به نام خود ثبت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99244" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99243">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG_LmlxDiWnAywIvzj_GAsw3OSBUCpDGTWuN5DZ6kdoUCr3WOJa9sv7OxOWDcliuth1rnys0DC7TwpHrYDMltLeH3BrtEVIGsV4Ii1Xi3ZSQJllGG8CujyxXXPowQz2AjUkYlei_pB3pjaZGwGQyuTIgp2bhXQ-RyBx4TyLb1H81HSDvy8aDBm-IoFHSOSXKjogDJk2-3OOSY53KriPjdMTA7IKhoVtRLKqwo_yx4g_GUDu300aaBVJO0YRcqFcLsdDzy7s2gMigAjyJO8C3YxdpI2L3DJezgZyPJV1HiYJsJZ-Jt9miOwWgBLuzG9D5ZMsPQRnWEXLzLzemxeaJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: باشگاه چلسی از عملکرد آلخاندرو گارناچو رضایت ندارد و بزودی این بازیکن در تابستان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99243" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99241">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTgvvqORu7-U5JEmaM7u-Fu8qO1ABCCMF45EfaMDUbc1vytZcHLoNv_IAsV93r4kV1KgpXqJHcyPgXzplG1Aiu5PJFGGDhNUoLP1biVRu2zWSFcYnsvQr4c_EMUA-RsUK1DATXMjMNhCfSQJSMkHe-CSJtjiRKY8YOxaW16y6wZEcgNJJQ-DFOAcCz3rp8VtnJDodKTZNldADrBgSUoV9hko65CI9Uc-o9tfzFSfAAbeQp6gnOToUMup6oFCTy4q96vW81REKkpYEa3sSmy9JjB14573uezR4uA2X6LyhqXOJW7XrQR3iVk-2_mDXUkR9B6PJ4NwDlggT1ZXd_tg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6n0Fv-0qK61HpY9Ba5qL_3d3qHkF-ltQpvt4WyKJN0h3Q-YhYr-dlEl6kFgJj7NySPC6qr36u7Qu_Iheuaj4HlOisj2msjJ3TAY5w6aH19fSv6vApSvKpGZRiYI4qgqVgNvdAWu-KpliBKICpmw7QI7mUaxgY5vEORU7O1d77VZK3FTZ1UxaCZd9HF7thFxyj2z8wrXCU81x0rRvjL4lP3N0o1r2zKQsM-GSXne3VoogWTIVdJr2ommKAxwppV7dTNLgtfiM7vOg8Aexzcjo3dXE1qOIqK6Z1Peo_9Wv7dLR-yA_594oHfEOFpCJcbDWLXCC55fDNmPl-aJgXrlYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادارای مراکش و فرانسه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99241" target="_blank">📅 21:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99240">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsfjWiCLNL3GlWO5t7JtBtBUg7UAMqKH-n6s2WNdyCPXkugzAf1nG2JX0a2X7EhQVHaSnBCSvWfhAq23CvTfRXHyZ4HD82g1JM4FJ8lKiyUNVxGOfBhsYZYnUrebvtoe5L1RE58w4W5T91jwd2CmIUS5kh4tN9aza5qC2xq1vc_vQun9IfkxJHCZN0xrbEyB1EBwTqLMdkIDyG37CZbAkjP5hkuXBEFdzh4PGU4A-Lu0o-ke_c4JfO5JlJJq10mdwDGmjnmZM1N3FL5B81uGDA-CS17FPORWioLBx9I5_XUonZqO02Dm6zAprO8Wc0GAG2b8bo-pHEi5JTiDtSdxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔵
ژابی آلونسو درباره چلسی:
این یکی از بهترین باشگاه‌های جهان است و در دهه‌های اخیر موفقیت‌های بزرگی کسب کرده است. افتخار بزرگی است که بخشی از آن باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99240" target="_blank">📅 21:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apnBJ_2Wzz3VNVyY8eJXEKt08RVynZeJt_-mHgnDGeXHVlN4R9laQb2EUA2tsF9_EzAUTEf6-heQ-j3X3BJC-seXGjbyKck-FMDWtT0uPCSNCf60IUlRPukALbVpXJKIgjH6niqF4R5jsYi29DAsPnaXgLnVIGCYEmZGh-g5rC5JNJH6Pi8LxKfKFYXdVWmtqNbyy91bijE3zP11x07OTLZ8gEiEb9XwG-Kz1d83yoert7mzdLvKEJ8cuoaY56HwySeO9oJDHmCa1IeZenrokz8Nfz-eo6IUacX9R8uMFneTbMpkyNd1Z-0T3H9wxoOUbzdsjQJQWiBuL8XPbdw1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏9 جولای 2006.
🇮🇹
در چنین روزی بیست سال پیش، ایتالیا قهرمان جهان شد و دیگر هرگز در جام جهانی، مسابقه‌ای حذفی را تجربه نکرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99239" target="_blank">📅 20:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3KCwapqZB0UmDMwKYMxMlJpY2o-tL7ma0O9kAln9LIIdEONS21NndNWw1rGXA4wDcSHSl5hQlH6WxZ6P1tfiOEfy0xZDcFpaslTL7sovk25KTE7J6lyn1JHUAXRf_t4LOcDkYeqkHq0sFNCC9wRujXiLC8uG8QNXGFGLC81KShjmIzBaNWiVbSFu7LqRkljwtctZxI4mc8iMVaX2FKX9JATp_7UUU1kn-4LGD8qMdM4I29IX4CvvQbr7bD3p_F1ot-nrJL3Nh8AVRzZU-bClx5keTzLWmMuW48KIoALz_xgiwW08dkmj747xDU25Xo6_LI_PEZ4DdooFmAIZdi5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
🇦🇷
نتانیاهو: راستش رو بخوای، مسی 39 سالشه و اون قبلاً هر چیزی که می‌خواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی خودش رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99238" target="_blank">📅 20:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWnMk6kGoqXkMY9nSIvXsuxKYQPMXG5OBKZlqKY2hiuln5qZcE8BGny-8xK1tb1a6GsOTPDAmASQwCnheTfVPYj991U_1Po7ofVQbIezGEjVm4wGzA5ugxiAm7BeICIoKmSwVtCJXR3p1Q_hyHeNYOzK2udIdlXLKyZjfJMTLTm0XMPGLPsyYuV92KA0AQsGQjfV8RDJ1GOXNUQcWL_VvpwYu_ECanz0XmFpMy5Y_ykOOnBzAnnh0kdEMfYxyoJp2t9-_Xu8cFxdRHDjS2cXRlMXOIfqf4M--qQ1NgM6Z_l8B1FMwNuZ86xI713UpAbSqqXLP3BTbmcUkVyU1BgJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
کارل دارلو گلر لیدز یونایتد به منچستریونایتد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99237" target="_blank">📅 20:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99236">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7zmvaJL05Xh6dmbcL7Jyml-e21wyleDtboT2lCBXkTyK6hHaqQsG8E_gqSODWwh5uH6gr-Wq0_IuAhHmAc6N5KcsFEnpj8cqC1kxcW5hFzPMyj1O3yuLcYb5VnI4z5szKHfKRntMqGAkI0eAsLlNrmO7jgQYc2UDM1gV4-Ml18MmufXG3jbp0fHHw9UoqCPBNWrlrA0ouv9p-t5qHCorswgpuDyY5vL3eZS2MZ0CUd32D8XJKemzbbIgmx9fYsaAwjJgIgPhjJtnNjkABjGc5lyXvjeVJugNXfH58WvnynzPXoDVTGWaOIMfyIwYsrAvxyZVH1PKz4PFSFlDT25RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتامندی نگرانی‌ای بابت بسته شدن تی وی تایم نداره چون همه سریالایی که میبینه رو روی کمرش تتو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99236" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krks4vEjLSwG25DPDuateLrDhbylf7syVKhiTu__KSIQvPBd-791qQ05b-MFbhTkqjfUvxXQSTw051sbObjY05gIhSj8vYd95Ymf1UYmImhH6KSbyIqw4Tg5apkzn0VQCsyWXdRnGO0jSFUZRe_foB2FhjixFdsXkbAOT-7mlK4nHQT8afGlYqHO2ijTLUPpbqjCmPFXOlBd_a9DoBUKVzChDITaVMUpxtv85Q6UaovzPOmqinMKlendlESpKloYc8MW_5bAfibG0iBIAZk1AlE5w1SAxv6lA_PJmngQX7bhh4-2S6pKfu2ipM_0wez9aZLzl-B1JWG2nls3MCoVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇨🇭
ژائو پینیرو داور پرتغالی به عنوان داور بازی آرژانتین و سوئیس انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99235" target="_blank">📅 20:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmt3azy4D6GTvVFLopgjcwtYrY2cKl_tLodLZZg0mOeJ6muAbknsGBP3wHb1-IbMoP40HVPXtaW_n0HM4TRUuqy_Tp7kVRHTsdti0vy7OVamBjusETBdYPRyC8CNcFnxavydJN1wxblOd-BIZhKl9Dm_g1ymKRiHPLtaSuLvhDxLE9ZEGrhQtONLSXHkAJV4m1tW0N0MqroDlQYnkyVuoVXx7qjOZpAKSQwETLYYsGO4jaaroIijwo6uY61IG7q_mTc5TRsKARsxADyDuaqT4K6A17q-17sYOZYk5_a7eg6eORTRSnqRBoulLhfAD4h3rrqy77BeocX2xsTUPwx_IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بی بی سی نیوز:
قانونگذاران یوفا خواستار تحقیقات درباره اینفانتینو، رئیس فیفا هستند و ادعا میکنند که وی به طور کامل کنترل مسابقات را از دست داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99234" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99233">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66bc2aaa07.mp4?token=iHYMWth3fTBKe0FEVleLInixuNhX_3wKqgvhCJuo9ze2Ec1oWkNGHMz0PqPv9o-u35xr8YlZjKC9DfWL8PVpTeu8ZNk_PJVD7yWchJt6Gf0_iARQXWdvfcGFC0Q7tV-0Fk3hV1iR_UDSmOEzo8hrz_u4hEQDFmE-KJMdTPNAxG52v5ruGg_Du1iil5e_9BV_zCMhS4BSnwiGZvXyEqVKYeqZbbeabz7Sb0mpVKMi16z3c-05g4-PLnEuKVRK1jWdV-gZExaFGXNzcdxxA86KrDwWtiN-aIg1gb3gVhfKymJNZCb1U5mxve3aO61w0x9zKNz6zwDYM1bVXdA8bX1Vyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66bc2aaa07.mp4?token=iHYMWth3fTBKe0FEVleLInixuNhX_3wKqgvhCJuo9ze2Ec1oWkNGHMz0PqPv9o-u35xr8YlZjKC9DfWL8PVpTeu8ZNk_PJVD7yWchJt6Gf0_iARQXWdvfcGFC0Q7tV-0Fk3hV1iR_UDSmOEzo8hrz_u4hEQDFmE-KJMdTPNAxG52v5ruGg_Du1iil5e_9BV_zCMhS4BSnwiGZvXyEqVKYeqZbbeabz7Sb0mpVKMi16z3c-05g4-PLnEuKVRK1jWdV-gZExaFGXNzcdxxA86KrDwWtiN-aIg1gb3gVhfKymJNZCb1U5mxve3aO61w0x9zKNz6zwDYM1bVXdA8bX1Vyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریزمان تو اولین بازی دوستانه برای اورلاندو سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99233" target="_blank">📅 20:16 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
