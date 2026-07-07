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
<img src="https://cdn4.telesco.pe/file/eBh4UXPQ2xY0-9vmDHzCdL7TwRWkS5iQfxG5VoVWK3n2Y7ziC0gol_IP-PB9mXyZ6NbdUuwKVOuVhExU6PcnbkvKXSrnqrrUvWgAFE6LycpjUwSu3lc9JYKswvW4etKcH5my_meNJ6AynkIbJGK5EVxWYZYD0-A2Kz2FurihEgcAKNlbMu_5B-uBELPQshtKVXxdcMDAumEsM58_DZ2bnwxqBgxUfXYOFJr2R5W8QJ70TWKD9YU_p7-OO93x_ifiMa-JeJfTelwMAgX6KwgmJUn2m8ACT4YJMLtoU3pIrzA8de3ocm3BbMulq6BfU5Dk116plUpcit6ajCmCGZp8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.42M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-667811">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رویترز: انفجار بمب در نزدیکی هتل محل اقامت ماکرون در دمشق  رویترز به نقل از یک منبع امنیتی:
🔹
چندین بمب دست‌ساز در نزدیکی هتلی که امانوئل ماکرون در دمشق در آن اقامت دارد، منفجر شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/667811" target="_blank">📅 11:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJOqrRAfx_jmIEnbZaI1Nfmrto8y_R5KcJmBU9aZ2EkO_7zTUtEpI0d8wOEc-0VNIVTJ5y8NsUB0K5MkXjzuZz7wj4UKYEM9usUoRxE6kM9NGQhxgaujCBuEqZRHsJK_R7RyFMp7BU1PAq_ZdKYMSVMVv1yRmoJ_roEWv_0s7v4ss370AtWwA2tBowme-6BtobvVlyuL7U8IBv2z_S_86fJMyPVyjSdWQ8KaJ-e-6IOHYrXfr7xAfVop84ga2Esdelc63ULUeDWeqcKpAhZRdkyWE0oGPpTHSFPg7EaX2Vgx-io1zZWYPAWW1VclEADEY_S5tIvTbLXdDHzW-_zeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VADYvbrqUI2fx8iIH__juc9jeI4168EJxSWTiX4nHRxWIgy-m1qV9U1oMe1EuDbeg9rdC-Rgsnq96lBWzOdFZGkCAml0mp-j5LYVESqLbO8ce9JJFKpibAFoe4L-dyF5nDQ_62PBYNPWiMP-igQdFRpWqDDUiXuLrnAL6x1THfda_JMAbtf8NpUuv6ynovSeWLsEliG5ry_6CCOfMS5Jw18ca5y08Ws7hedVrdBJDTR_YUE3OdIf8MaP2anOWml3U-yMFavKu0-ZWt8qHLVB0rX7niUmPfxWNE2lW6iWHVF9s-AatCtJHQTST9chLSV2Y4fGTfgaVbor01sQEIhJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrkwe6HL3kYGB_lObYiKry4MsL37xU3Nc4DpK0sBMmZAQigOc-a9SoUuQFPaBArbuek8uN6dJEeCPofc02G2lxktAVGKBxmMrye8tOHqHIPQjP_Ogf21inkQeRSluySIugct6kM_nMqjizeecxEVLsGPRO7BSYV2Fr0px3vYFf5zHdXSWKA3IYR4yXua4xkjrHJ6439vSItqAsV_rdHiOXs6Emayn0IoCoBeqWs2-0ZdeOA-uUxXsQlctrRIoRd65mwnOXyuDlktIop-NeFyCG9SsUYa9GX5WlbaqlAjnN2IvPe5nu1ic7IKaOMFAAWzWzFsN6tDYVFgUNSRHsB8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIjrvx6FidZDdldrMG_Rq43EBfOpExXWB3kI5OUmOHbewH250Qna5hMk4uE-lyeOuFD1GTXHYp9wVEsH36RzK-lyiTayHmHhqz9cygHbecUSiZJjVL-1bdnWT8NlN7thpisSA8fSLiKscpJ8ikHrc2wuSKIZHV5_V-goegFWU-913718_Jz5e6nLlQgQXMZ-Dt_-HmCWJ4j12mYnTF3JxeIrj2_RKOtARImwxV6W0FK1fu2ftRutitypryC-Aa881hTFGwllZHnoEVqJ88VscjhFBmpUclRfUpyz6vWTz4VdIPy-eucRECwChz-A3kgXzgad2IxMkfUBscFNNIf3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dsBsGszyRNRW2evQ-UQZ07dXpTkxqJUoRi4sAvquKfkg248ZP-wYs4c3e5dKFR9Ios3vB9Nkb4rHW8CTzjfBfN3DXsKsvXma-CPdICmEYjc1ZwoPayWpFGBcuv3tFR059-Yw3gxATJ0Xxwb64E4Rb5VdjGXLeE4B9l3IZYHxT_96x114HIR3H8SlgVtFwE5SNRS-fhW928PweoJntSkLsL7X7zK33hZUNRjdeZtf-61A-G1P_18khz4Tpk67uMEdJ7KF0bI4SCZuCQon0fPX7wMsaigxm4BOfaV2zVy_16FmiZPNmw72SITV0v6xyS4SnZl2NhhKLPO-P9o4uIGr_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DT9rTgH3Nj8XI1UZoxqRR7AWQ0pWEDfOkX_qzSemnumFV59GcGhMnj4Vgr6NdSP__IE4hkDJM5lRc1SvSsRA8QO5a4MwFm2LFXKyDzzxzrYue5D9FHGqQqV8waiMIGOZ6RlA1T-Pea2wt_72Zp0utnFbPqC4zvUsoXhBxmKImNNgVo5_6bb09NbFjMvL9fHaYqInIEbWZNDg2w7oleCFlmvU63U0qbH3GbMNAjyJAnCVg76cDsVl1TZV2RnHGCA4ez1RXLb89Ap-Jt-U72LS-no1sUOvz1xMWJ1sMyOvLhbgtp-FDZxZdBYT_HOwR_PvD64V3DbmnoUalatT_XBQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmJKDFYoZi5pUOi-yZEAOokfL7ur-32gh_Bm6B0VQM-J6K5v7oIu0_RJAF2FfXEPZFEFGnNsqJLgu0R61fXpkTHI8aNnY5RUQJXJ8CtFYBXT1rbRcr5dyGwCeuATPbvoIOrgqKFSaNcYaoy0EzH5Fn8GsHQqAW9eEIjrKZwR5dYiQTlcZz_b9If6eSTMl-5llrccBgSfRbw_gHqAtV-MFFwStk5ZXEkmpqvIQ6UJR9i6Hdp59J7hLBq0ksfrtyIk_O6V9HEmk3-UqYX6spYH6a-i1y1s1DwzcTHPfunftFu_BcIcJVLEoFet5MzR83VSUlpjuDZ5Uz36sg7ZeQoucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoVVhSjA3JW10z4tLHpxk5bvwDW7odxrNNPfc-8yzhbguvWz6oPZpW3QuZgzwBPmMBFczp5xWOi3DPJNddkUtyBq7UgY5_bG3HFoa0ZgXeMar1rzMzCfKRM7cbfhixqEfLnvPZJB4SvWUSnjCCIkKY_SsxKE31o7gaffITwV4eytn3ubwdQ2mQpAg_tF86wdCso46JC1VmJsHAvqtirbbIdeuJQ2hg49Lqk9_a8ih18IzzZCvP5rDnGhtTTPDE4Rdjyql0UN3QTHtAiwTblCsMVy2hXLOMVBC6Z85jarr9L1lAdaYPaFzFIs_x5mRsBaoOdcJH0-0iP55Af7rTTYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-0Rl_6dbCHDfyl_mmWwPK1MRJEnlDY_Bg1gT5oNHhTxTBKJRX1mkCEKT3DWZK_MxsnU9Ty_IkZR-giwcsFOcgZANJKHMF49b-DO1x7vYiKKtBBMaMt8oKJEr_RCFxg0kbrNgT96xg-6c35_cNG_fz_wOi5n8aJIX4DdrHKN7xlEur5eZ9cwWNAKYa5nu-3-zAxBZgaS5fnXISwyalzTuwqB37fc1aNNr1Zsesg0zl1S6wzczNX39_acTbyb6j4hKn78diSIh9sRb6HWKYrK6UquHyRPjBqTFtcpT_nwbqKohIKKgwjKsnjxcTCq2Tw8SI1ZdTgWtNnjy2X4KQ4mMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xi9qm2DXSjd17SHEpe7OgMQN-3Puphxxg4dPwpR8SJClZbqyRuoCIDCD8D1ydaiDW8O0sMX8r8lwZK498k4xSGe-gqczCw0cjd4c4C3Uby5IfKg2tUM862opNIwNGO11H6EqugdvikO4olLOPgj3l6_OThQtWtDPuwiO0O_ZGecTrCvKQSCk5yyt_DNh8SUs0aI2jimq0jD1droShPprpafSqxYdwUzIQty3-apFD06yFjyKi78664TfwD1T8y2RGArYcbh_BHf7HwoznyPRE5x6ZPnjFweVfS94PSz7b3Gi-JGKS1AQYlPP6KXdGTiLK3bViWTcUIPRBAGh4P6spA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از اقامه نماز بر پیکر رهبر شهید انقلاب در مسجد مقدس جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/667801" target="_blank">📅 11:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667798">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6665157.mp4?token=muqbMAB5Be0BKC51EZYqhzEl0nopzgHwzHoMl6epwgNQYkOtCKOQEHSm11EX-87MjiFh_wOIF5rI9bX_ztma3a2-Gtb67Qdz3zEfVQRU4-bqZRXjwim-GdH34RloXQUTRIjLBNi28Tbq98LDzekKfu5Gx6cNsM36PuspRMvVPfTWwzhdpgjZ1o-zRtJVXIEgpUUtDbBLvhezxobL_Kz20pIDS-mmVhVipa0E3GZN0FN5wx_jEzAJpGec9-FtQ3FFtLDOoGkbtkF1zNigeKeekcp3tMo2G4HoazBCmKb5M3ZXRXODrz4I0rPK-vO0ZeyR7Dv2H-a5FeMOzASHEINttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6665157.mp4?token=muqbMAB5Be0BKC51EZYqhzEl0nopzgHwzHoMl6epwgNQYkOtCKOQEHSm11EX-87MjiFh_wOIF5rI9bX_ztma3a2-Gtb67Qdz3zEfVQRU4-bqZRXjwim-GdH34RloXQUTRIjLBNi28Tbq98LDzekKfu5Gx6cNsM36PuspRMvVPfTWwzhdpgjZ1o-zRtJVXIEgpUUtDbBLvhezxobL_Kz20pIDS-mmVhVipa0E3GZN0FN5wx_jEzAJpGec9-FtQ3FFtLDOoGkbtkF1zNigeKeekcp3tMo2G4HoazBCmKb5M3ZXRXODrz4I0rPK-vO0ZeyR7Dv2H-a5FeMOzASHEINttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای غمناک قم در آخرین ساعات تشییع پیکر رهبر شهید انقلاب به روایت دوربین خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/667798" target="_blank">📅 11:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667797">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d538d846.mp4?token=GVpqHk7Nu2UXOChmq6jsX_YRmR8XXw6phcd4Y8oeh1JJBX7bPJj8LIrT69ItZfufZA4thEw9TW-l13MwNlSMcElDQoVNCbGHyZVOmc-lmZILS0VpQFYES50mApW-KXCF4ArWLDwiiV-v-D2JDZhgaauPLZvDJf0zcdbLzhfzWN7qNONufTiSrl8M_7TrZJD61Nk5a5HR-MxHyI7tG_2wOTh2HphVhZqr5bh1PVVx1LUlbyxFKP6_J7IK7WvU09cPbzdD854-z_CW9BvO7vj9w9-eu-n8I8996xUYN9i3FIgqfiB7WbomTznsPBrpYsmZ1WqMIP0Ga27Fd6_3tu50UXwvX9vL_p8-hRNGn1zaJHIq5d8cZ_hbhjNZYC1DHAnqhHwdy-4gpxH4Orm7VhL0ipw_nm27MFyRKtJy8MOMNo1S4nlT8Y5QDgD_y-vlJA8rCj-z09urK6jlcLxQCqoNCaCZH9lqo5Ccw4RMWwsvZYvLuHJofF1-McE4FMIFKBce065LaRRnWF3DuZgIldH6dbMiekEhr8N52m5oIjLXdmN6vyRlKbcaq219dyiPcUjDirxHmfox1pxZKPtlKOlWAYmjfOBqCk9i2PIYacwzidnlbxnYI0BKn977KRnnb9XbDguotj-EQDNSXDwjUPq30YexogbX2lIeerLjsF-ygS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d538d846.mp4?token=GVpqHk7Nu2UXOChmq6jsX_YRmR8XXw6phcd4Y8oeh1JJBX7bPJj8LIrT69ItZfufZA4thEw9TW-l13MwNlSMcElDQoVNCbGHyZVOmc-lmZILS0VpQFYES50mApW-KXCF4ArWLDwiiV-v-D2JDZhgaauPLZvDJf0zcdbLzhfzWN7qNONufTiSrl8M_7TrZJD61Nk5a5HR-MxHyI7tG_2wOTh2HphVhZqr5bh1PVVx1LUlbyxFKP6_J7IK7WvU09cPbzdD854-z_CW9BvO7vj9w9-eu-n8I8996xUYN9i3FIgqfiB7WbomTznsPBrpYsmZ1WqMIP0Ga27Fd6_3tu50UXwvX9vL_p8-hRNGn1zaJHIq5d8cZ_hbhjNZYC1DHAnqhHwdy-4gpxH4Orm7VhL0ipw_nm27MFyRKtJy8MOMNo1S4nlT8Y5QDgD_y-vlJA8rCj-z09urK6jlcLxQCqoNCaCZH9lqo5Ccw4RMWwsvZYvLuHJofF1-McE4FMIFKBce065LaRRnWF3DuZgIldH6dbMiekEhr8N52m5oIjLXdmN6vyRlKbcaq219dyiPcUjDirxHmfox1pxZKPtlKOlWAYmjfOBqCk9i2PIYacwzidnlbxnYI0BKn977KRnnb9XbDguotj-EQDNSXDwjUPq30YexogbX2lIeerLjsF-ygS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر کوهرنگی رهبر شهید انقلاب خطاب به رهبر انقلاب: تا آخرین قطره خون بر عهدی که بستیم هستیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/667797" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667796">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
انفجار خودرو در دمشق همزمان با سفر ماکرون
🔹
انفجار شدید یک خودرو در نزدیکی هتل «فورسیزن» دمشق و برخاستن ستون‌های دود از این محل، همزمان با سفر رئیس‌جمهور فرانسه به سوریه گزارش شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667796" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667795">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ef7a3d27.mp4?token=USNiHrHDceL3VieJgHZgmaSTaeXN0dOxkVsAHto4swPjkNFs0GgyCYwugjTzkLyJ9naWFiFNYT8ka4dopTkv9bOrUed_R_4dEnc8YDy0ciq9Rm0DzEYUMSsqOQMIo4wmwHv-WWg2ZpieaQHBGNB4bTdDKm3nhfo8lZLZ8KGtyGzQHT9WPTJGNSud42s50MXyua63tl1ql7n5bcx8XCHLUR8JSeVC55Y4XxzVz6bAc1YI6qiCzn8OmDLn88xfv8yzzuoA7q4FtIyLBhA0ygzBzGGyxO_QM6a0mxgx4Y8Ksrnkn8bPPUPJgmDcgA-VVItH_sovJZHgIK0YHNeNQJjq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ef7a3d27.mp4?token=USNiHrHDceL3VieJgHZgmaSTaeXN0dOxkVsAHto4swPjkNFs0GgyCYwugjTzkLyJ9naWFiFNYT8ka4dopTkv9bOrUed_R_4dEnc8YDy0ciq9Rm0DzEYUMSsqOQMIo4wmwHv-WWg2ZpieaQHBGNB4bTdDKm3nhfo8lZLZ8KGtyGzQHT9WPTJGNSud42s50MXyua63tl1ql7n5bcx8XCHLUR8JSeVC55Y4XxzVz6bAc1YI6qiCzn8OmDLn88xfv8yzzuoA7q4FtIyLBhA0ygzBzGGyxO_QM6a0mxgx4Y8Ksrnkn8bPPUPJgmDcgA-VVItH_sovJZHgIK0YHNeNQJjq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دومینو حذف میزبان‌ها تکمیل شد؛ گل چهارم بلژیک به آمریکا توسط لوکاکو
🇺🇸
1️⃣
🏆
4️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667795" target="_blank">📅 11:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667794">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9JQwnNZasI5X8FBi5xACQ9HdgsB8d-nVhVbstdIa6nAUAICsV6XBHq3LSDQA4Y18uPsI4F9_3VdzAbjiGyBhfDi3Jzp0eWfPt-e0dNV_aVtxjjoxTFRO4QoIrP0WhI90QLoPCOHJ9GHiuvhe8_Q5GPqnQXeqviQPzTO7c_d0l7fL2JXBMJf4h7GAbiof74ccXdunszfu9S3tfdrBmuNzXbsJzxPo_yrva7Xovn95rLWBHuC053xu8bUNdvEfWzQIaKtqE3gpqoIjlpSddVYSBykR44nwbn7mSB5LYRbxZ1T3B81N3-wpy2MeGaND8q8pCcagrOUXOsqt75DKsbvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماکرون و ابومحمد الجولانی (احمد الشرع) در دمشق دیدار کردند
🔹
این اولین دیدار مقامات فرانسوی با رئسای جمهور سوریه است پس از ۱۸ سال.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667794" target="_blank">📅 10:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667793">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9cqffsPNLomArlPwcKtF5F5wTqCQek_-vyMIYNUQPZL0ZogA-gJs-XDs1e2egOqGAS-tfaa81TJ5B9TgqtsuLLfF43No4Pcqhr5wEKkdTBStFifW_2feQuklyPxxq6uK34X_toBgR0RTANt7CUs3LHaz9O8fSHFgoTsdq6klX-xl18WMcnm9pKcGvWqhsvaZcs0DVeJliDVsRtVp0_ce1zAAZnm-KZfDD-7F33t2lzK7TZiTWo7czkOH9bkJan5eRHJ1C2ra11G_QfMaA-uhYpZZQHOp9_N8-_xdDEUh5Vq-55DMM244yDF9Jh19oBvZLz6yUUSGHkpPITvS2Rulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده پاداش بزرگ برای اجرای حکم قصاص الهی
محسنی ثانی نماینده مجلس:
🔹
کمیسیون امنیت و سیاست خارجی مجلس طرحی را به تصویب رسانده و آماده ارائه به صحن مجلس کرده است که در آن، برای هر کسی که در اجرای حکم قصاص الهی نقش داشته باشد، پاداش نقدی بزرگ و قابل ملاحظه‌ای در نظر گرفته شده است/خبرفوری
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667793" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667792">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1B8lvmnFC5_hgOKgvkYT8GFuNcY8Fiq2r1j9mePzlt817DCWi75SUYb0cPaI-HDgZBKNj71MgMgMptChODE983pbex4eKcPzMHBpPMAc3UQPydIMIozvvb-wAo0706dCtdESIuKMFU4Xl4QyCsVDnNfuSLBU7yqo956AfNifto5rEfAfBb_Z8tsfU06Mw3jZ3zthRKPWr8leqYqqIoK6oCiyk7OMzt-RjfeVEeYZSUv1eooLSCfNmDnTZv6vHeDXIeoVhxpbyeEkWJZw_vzR-j956BCH5HxTPIq3_aJL4mt-pwvmJF55XDEnyuBxvkQkjnwLFMnKuEWRWfiGg8ITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم فلسطین در دستان خاویر باردم(بازیگر اسپانیایی) در جام جهانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667792" target="_blank">📅 10:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667791">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21385ee290.mp4?token=TsWoXEJnE7tHuD0MC2USKSe95kKBA1knO8mZjDYDu4KfWY2QVUF5wEvLbvnRsOQzgK3h9L7E_pslDYgBQmKe3Q7uJqQIAkOzdEYSoJadj5TJf_N8WmeQfgGdDzzzJJIUVhCHhRimB0uqTbFK_r56q2PpJWjtN35IPYBhFYflZ9o92wLZp9ow8y1RmNWqXrhQ_fN5_PeA8Gi23HHJcIbYgt_fa2E19hdrFJvZxx5FFAxjwEeydTw34rLfFyKI06HQQRxr6bvvcs_NScLgxwHugB0M0KrNd7kkLkXAifQpS5LULyAkckR6CapXMAOTcSQhkWP9cllE-fjVBDn8ysMipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21385ee290.mp4?token=TsWoXEJnE7tHuD0MC2USKSe95kKBA1knO8mZjDYDu4KfWY2QVUF5wEvLbvnRsOQzgK3h9L7E_pslDYgBQmKe3Q7uJqQIAkOzdEYSoJadj5TJf_N8WmeQfgGdDzzzJJIUVhCHhRimB0uqTbFK_r56q2PpJWjtN35IPYBhFYflZ9o92wLZp9ow8y1RmNWqXrhQ_fN5_PeA8Gi23HHJcIbYgt_fa2E19hdrFJvZxx5FFAxjwEeydTw34rLfFyKI06HQQRxr6bvvcs_NScLgxwHugB0M0KrNd7kkLkXAifQpS5LULyAkckR6CapXMAOTcSQhkWP9cllE-fjVBDn8ysMipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم بلژیک به آمریکا توسط واناکن
🇺🇸
1️⃣
🏆
3️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667791" target="_blank">📅 10:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667790">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e2400d94.mp4?token=acrTdYwzVP4a7ZAQHFkSt2kA-MTirxW27KQ_dqrGgVixikSSPTj4ro_tSKXgS69f_HjXdl7mjmzZTnDGWIPL_efcylDcgmbjhByGxgQUZ63Nqb8_F68KDE0l4xhNnnGT5c7ono4XPYAZnH5RDgmRWQ94HoQeBkiHUfT-FS-1FuSVDqrJtEjwZN18u_fU1s50oeCyrIcr87RNRLweXiPjJ_QA0zKhP7v2VpR-C99rdJnI4HFmTM0AyN_CPHrqEemq2mpCuJw1IZ6BPiuREJ87mCa4fgGKiq47z6eIEvQPMsdknym5DtnqOhdPQFEk3DBgS-ZEjfOZTR6vs0iQjQrY6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e2400d94.mp4?token=acrTdYwzVP4a7ZAQHFkSt2kA-MTirxW27KQ_dqrGgVixikSSPTj4ro_tSKXgS69f_HjXdl7mjmzZTnDGWIPL_efcylDcgmbjhByGxgQUZ63Nqb8_F68KDE0l4xhNnnGT5c7ono4XPYAZnH5RDgmRWQ94HoQeBkiHUfT-FS-1FuSVDqrJtEjwZN18u_fU1s50oeCyrIcr87RNRLweXiPjJ_QA0zKhP7v2VpR-C99rdJnI4HFmTM0AyN_CPHrqEemq2mpCuJw1IZ6BPiuREJ87mCa4fgGKiq47z6eIEvQPMsdknym5DtnqOhdPQFEk3DBgS-ZEjfOZTR6vs0iQjQrY6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
قم تا مرز انفجار شلوغ شده است</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667790" target="_blank">📅 10:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667789">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbc73046.mp4?token=lKi-Z0x-zM4_mFHR5iugXlaV6rT84dHkmZGCn426kjAuxbwzRriN148Rd28P1j_Ub0NTRKGXddKA4hIxprPoqSTRJK1XPcZBkIxN5vV5m0OnZXshPJVx48s96jOvA4GdpgIhFI88oTlZ2DXzYum_tsGVxGdYAtZ8I9eDUAmxOvF5Iqq4M24EVH4EhPHTKjtRQkO6tcfsvLlrRurov8OFQPk9FF3tiBJZaC5KnrIAomxpFj3k83GAw5ST5V0EFcipV3WZwuMf33bG502M0m7moIfHjo5AE1Mcg7-gWYY0asTAoiyA6D7bHROccyz_njfEL4x2TTy0Hh--sjWUqSTeqr6__5XW09BN-dsRJWldxGdKtUbJs6u9VVh-jCF3mKPNl6XVYRchPsZuj2NUejFgj1q5HXXPhq6Y8E8o-qscBlnVjtyuvvdB7HlK9J50GNSps_vsJYvCIEMiEEJSLvb-x6Js2c5uJnvcTj7YCiROP8WbLQEmhbNVqE0VcSyNDthSpKBfvCNCB4RyU_gi_pxLXLwwl-XFtXqnqDtm1c5jXpOHnKxP35TtgjBhQ8NCspPFp9HAf8CsKYWOfTDlnmwoNyxWXJKBHymtops1ytJ77vNhNxreGMjKd71qAfjL1oF1gZYOjtGSQfMZJIHiazoL3l2laiOj5Ngp088vwxAWU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbc73046.mp4?token=lKi-Z0x-zM4_mFHR5iugXlaV6rT84dHkmZGCn426kjAuxbwzRriN148Rd28P1j_Ub0NTRKGXddKA4hIxprPoqSTRJK1XPcZBkIxN5vV5m0OnZXshPJVx48s96jOvA4GdpgIhFI88oTlZ2DXzYum_tsGVxGdYAtZ8I9eDUAmxOvF5Iqq4M24EVH4EhPHTKjtRQkO6tcfsvLlrRurov8OFQPk9FF3tiBJZaC5KnrIAomxpFj3k83GAw5ST5V0EFcipV3WZwuMf33bG502M0m7moIfHjo5AE1Mcg7-gWYY0asTAoiyA6D7bHROccyz_njfEL4x2TTy0Hh--sjWUqSTeqr6__5XW09BN-dsRJWldxGdKtUbJs6u9VVh-jCF3mKPNl6XVYRchPsZuj2NUejFgj1q5HXXPhq6Y8E8o-qscBlnVjtyuvvdB7HlK9J50GNSps_vsJYvCIEMiEEJSLvb-x6Js2c5uJnvcTj7YCiROP8WbLQEmhbNVqE0VcSyNDthSpKBfvCNCB4RyU_gi_pxLXLwwl-XFtXqnqDtm1c5jXpOHnKxP35TtgjBhQ8NCspPFp9HAf8CsKYWOfTDlnmwoNyxWXJKBHymtops1ytJ77vNhNxreGMjKd71qAfjL1oF1gZYOjtGSQfMZJIHiazoL3l2laiOj5Ngp088vwxAWU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش وصف‌ناپذیر مردم قم در آخرین وداع با امام شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667789" target="_blank">📅 10:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667788">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89066c841a.mp4?token=GHOgBLZUpMlLWejhOn0dkeISTI_yTAE6bd4ANcu9GCr7JNq8i5fj0kfLQ33hg6CcME-sIs_QdAfR7_NVmWqq8Aa2jhqSUCiiGn4iskwYZ8xqUzlLTM3uC9-m0MSy0BPuGDGHDZsF3C6dtfelUZUdSrBYgxK15NKxFRAY-Jq3qifEUF4n8a_flG2n-KYjhsjnxp_LW7RXR6rpwONNnF_r_GvmgH8i7hJm_DyqcIi_tTuLU01WmchX08vZdmXDSRVQ7u47Mhzy0H9aM6jv79U8O8XkXJOA_Px602IHnh_Maiwhz8eQCIutTyoLYuNjf4K1e5bhFuoQwdz_qtrBuKCutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89066c841a.mp4?token=GHOgBLZUpMlLWejhOn0dkeISTI_yTAE6bd4ANcu9GCr7JNq8i5fj0kfLQ33hg6CcME-sIs_QdAfR7_NVmWqq8Aa2jhqSUCiiGn4iskwYZ8xqUzlLTM3uC9-m0MSy0BPuGDGHDZsF3C6dtfelUZUdSrBYgxK15NKxFRAY-Jq3qifEUF4n8a_flG2n-KYjhsjnxp_LW7RXR6rpwONNnF_r_GvmgH8i7hJm_DyqcIi_tTuLU01WmchX08vZdmXDSRVQ7u47Mhzy0H9aM6jv79U8O8XkXJOA_Px602IHnh_Maiwhz8eQCIutTyoLYuNjf4K1e5bhFuoQwdz_qtrBuKCutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم بلژیک به آمریکا توسط دکتلار
🇺🇸
1️⃣
🏆
2️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667788" target="_blank">📅 10:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667787">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqgyLipZ014ZEyl66-83-bQ3QtaaTawXi1VvdVSljYPHbuIblDJhIfAuFUHmUbWsxgKMmhaILwvxmLgOUlEMwf6ZMCXyeOHv35aZStDn1wce3oAz7IAN-NpXx5vPk49TQRgKCyChA9pTXGdLNSzNJXGnXFwyFg3sJzeKwvD4WBACSDgqNKVsITOJTNCPSop9YAa1DbI3kHUzvKOr8CrcdLfEwIsx7RNf0HKlIxN8_aK3i7mqiuX0Xo-QLYvLEIIgybZqNBL2cKsAQ_uP9KOVKPYC1lJqkoQ1XFBcvMkXPaCVtgXEL4X79roL_lD9blI2v2jt-BaGGCp8sBg1DMFgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماکرون و ابومحمد الجولانی (احمد الشرع) در دمشق دیدار کردند
🔹
این اولین دیدار مقامات فرانسوی با رئسای جمهور سوریه است پس از ۱۸ سال.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667787" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667786">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3897255d.mp4?token=F7ykz3pw0s-joCcBaVXwHnKfQ1B-jWPiVC-Scp4Rr2S_m-OBdeZufta5jfhIBT78xmi2MhV6TMOT2p0fD5NPiLcVaDZJMAYx9mTIN0t8UDVLN-G3GM62p_Jd9-eNdXHw8sbstEBwfL5Vskk6PyqXUEPx2p8zSJuLAAzzbNEUJzhmXMq8vu9pPutynB4a7G6bW4KEPpwD7r1-owcfoX6jlqHWBrBE6NLagD-kDUqKTWPPnLD6_pzbeaEnvlPJAShX7B7LMGvc3QRjSh6W9GID1aPbRLpCCZaodiTaB4Bjr5r3h2yLws_4VE-HxGxOzcFAXNqEtgm4R4HubqbW3AoEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3897255d.mp4?token=F7ykz3pw0s-joCcBaVXwHnKfQ1B-jWPiVC-Scp4Rr2S_m-OBdeZufta5jfhIBT78xmi2MhV6TMOT2p0fD5NPiLcVaDZJMAYx9mTIN0t8UDVLN-G3GM62p_Jd9-eNdXHw8sbstEBwfL5Vskk6PyqXUEPx2p8zSJuLAAzzbNEUJzhmXMq8vu9pPutynB4a7G6bW4KEPpwD7r1-owcfoX6jlqHWBrBE6NLagD-kDUqKTWPPnLD6_pzbeaEnvlPJAShX7B7LMGvc3QRjSh6W9GID1aPbRLpCCZaodiTaB4Bjr5r3h2yLws_4VE-HxGxOzcFAXNqEtgm4R4HubqbW3AoEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آمریکا به بلژیک توسط تیلمن
🇺🇸
1️⃣
🏆
1️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667786" target="_blank">📅 10:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667785">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d339b23a.mp4?token=aNsRyM5iP2Krzv0RYpL-ADaPhASwph_md6jY0UdeBY0z30sPK8H-WakxsXj52l8DhyUqP8UCkKwmxJAw5vHs2OhogWEu3gGh1e2VF1brJDYp7HnMco5rtl_2PX3LY8hkQClvb01Eu8VfCdqiWvjz-NETsqBLjrccf86Aj9e9IUL9Dcy9R-v13a_b4nq1em2s4iq86R80fRtCT0keWEAdWp8gCgr8U9CxWEMBi_FUNi3WDiIDCmn_3kGQVmWuiU2ny0JxcHAfU5ZzyIjUvABdzuaFgsAWcGWt0a2daMW96_GfimfkAeCW2-B-s-051p4Y-Q_EyOXLGVoXAaKMQ1zBzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d339b23a.mp4?token=aNsRyM5iP2Krzv0RYpL-ADaPhASwph_md6jY0UdeBY0z30sPK8H-WakxsXj52l8DhyUqP8UCkKwmxJAw5vHs2OhogWEu3gGh1e2VF1brJDYp7HnMco5rtl_2PX3LY8hkQClvb01Eu8VfCdqiWvjz-NETsqBLjrccf86Aj9e9IUL9Dcy9R-v13a_b4nq1em2s4iq86R80fRtCT0keWEAdWp8gCgr8U9CxWEMBi_FUNi3WDiIDCmn_3kGQVmWuiU2ny0JxcHAfU5ZzyIjUvABdzuaFgsAWcGWt0a2daMW96_GfimfkAeCW2-B-s-051p4Y-Q_EyOXLGVoXAaKMQ1zBzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری به نقل از فرمانده سپاه قم: ماشین حمل پیکر رهبر شهید انقلاب و خانواده‌اش تا زیرگذر حکیم خواهند رفت و از آنجا به حرم حضرت معصومه(س) منتقل خواهند شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667785" target="_blank">📅 10:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667784">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a510abb9.mp4?token=CbTeV9GDbpB-6E_3EWmnF1RcdrEoiywIFlB63DbAHG1r0Q-etKdkyjoJsDdlC4BUnGRbxFO_uact6b8SPjK8q8lS0YBzmJWbJyyQq8Q-_fx7Vv11Xj_wTNN-d7LqOTiyGqB8ukPgSokZtPgqbKUc3feW7s_fRq7pAK9jtEreYOgOpTPlzH74OueMgsRpdosA002fujNxPwGKyJc3qZLlkntsc1Wfye8Rk1vnyZrac9yb91-tq1iCbF1UxxZD95Y0RugaGdy3Lw3HzE4uXsth1TvFhxQS5q3us2CrgCF5WZLXbT18OolzUzsdT2L9XIdfkcINJ2pErFDfpmASKCcKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a510abb9.mp4?token=CbTeV9GDbpB-6E_3EWmnF1RcdrEoiywIFlB63DbAHG1r0Q-etKdkyjoJsDdlC4BUnGRbxFO_uact6b8SPjK8q8lS0YBzmJWbJyyQq8Q-_fx7Vv11Xj_wTNN-d7LqOTiyGqB8ukPgSokZtPgqbKUc3feW7s_fRq7pAK9jtEreYOgOpTPlzH74OueMgsRpdosA002fujNxPwGKyJc3qZLlkntsc1Wfye8Rk1vnyZrac9yb91-tq1iCbF1UxxZD95Y0RugaGdy3Lw3HzE4uXsth1TvFhxQS5q3us2CrgCF5WZLXbT18OolzUzsdT2L9XIdfkcINJ2pErFDfpmASKCcKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بلژیک به آمریکا توسط دکتلار
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667784" target="_blank">📅 10:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667783">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b72f9513c.mp4?token=NkZ6nmqOg7cFR9J-o3pZsXVeuaYaD4Rzibe9n9sfeQsqbo0fhYDkOnWITY_M_OZ568Vvs_Z9DCMzqV1fZG9tOA-PKwFRNDHMag8sEexwPJZZ_iu9qaEOuA-BA0d7slalbPNTcmyn2Rk7opozpo5BDN4Xmgy0pdA7bguzDRXJF3Dx9IzimF9fjZzwwy6L7lUrfP1qeNqbwXaoM3F4ONgkb9_DBTif6pjyX4NbIt8FnaAkkieyNT4IPKzTu6ns2UhGqwBVcAP9HinKqMSsIXv0ahlfp9qE-4K1fVpJrcR6QKj2CLzKUsGEO7VJnkL1tmGyy8nvicNmzyjyOlwq1HhLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b72f9513c.mp4?token=NkZ6nmqOg7cFR9J-o3pZsXVeuaYaD4Rzibe9n9sfeQsqbo0fhYDkOnWITY_M_OZ568Vvs_Z9DCMzqV1fZG9tOA-PKwFRNDHMag8sEexwPJZZ_iu9qaEOuA-BA0d7slalbPNTcmyn2Rk7opozpo5BDN4Xmgy0pdA7bguzDRXJF3Dx9IzimF9fjZzwwy6L7lUrfP1qeNqbwXaoM3F4ONgkb9_DBTif6pjyX4NbIt8FnaAkkieyNT4IPKzTu6ns2UhGqwBVcAP9HinKqMSsIXv0ahlfp9qE-4K1fVpJrcR6QKj2CLzKUsGEO7VJnkL1tmGyy8nvicNmzyjyOlwq1HhLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریستوفر هلالی، روزنامه‌نگار ساکن آمریکا در برنامه پرچمدار: رهبر شهید انقلاب به مانند امام حسین بدون ترس شهید شدند و غربی‌ها چنین چیزی را نمی‌فهمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667783" target="_blank">📅 10:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667782">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb471b531.mp4?token=uR5TNQoCna-ddCOwDMXUDMOIQp3zbHEHNV7H6yS055LZm4OzPK_ld-oNJ2tFmNUTYO8W2PnJY_O6A-gEUeTd8-IuS2ARKSCUkmQJ5uXdriK_QUFL768F16jGVdg9W4pqDh6tqqOh8YrzWjJXdLCsukbvl7Xld1CvYWpLVZB79qiZid2eHwyK7NoEMDwSTYsY5PKokKXO3bc_-AGRozEpZGsnQLjzhE_qfBntBD2wj2wu_V7y2JhAnkvBJijVnQDUgYYILR1XpwOYhv06k6CR66QOZNBM-29XHbyrJ858geBruR_101zctob7gdvEUfa0mLHCuSCo8H31hi1O8stmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb471b531.mp4?token=uR5TNQoCna-ddCOwDMXUDMOIQp3zbHEHNV7H6yS055LZm4OzPK_ld-oNJ2tFmNUTYO8W2PnJY_O6A-gEUeTd8-IuS2ARKSCUkmQJ5uXdriK_QUFL768F16jGVdg9W4pqDh6tqqOh8YrzWjJXdLCsukbvl7Xld1CvYWpLVZB79qiZid2eHwyK7NoEMDwSTYsY5PKokKXO3bc_-AGRozEpZGsnQLjzhE_qfBntBD2wj2wu_V7y2JhAnkvBJijVnQDUgYYILR1XpwOYhv06k6CR66QOZNBM-29XHbyrJ858geBruR_101zctob7gdvEUfa0mLHCuSCo8H31hi1O8stmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر عجیب از رانش زمین و سیل در شمال غربی چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667782" target="_blank">📅 10:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667772">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CngFvqLhwQqP7zHTuarbQoPoA6rQ7vAwYYK6H7gfEGME54BgujYf7LFWeNRsk1t7Y6sPiNKmUfXmlhoGS_0tAQ-tSLyyQAOqHCpsds5Xj8LVQ_4nd0Y99jTMsNx02t5qN2ZR5w_L9JmkgTcoT2T1xat71QbL-ExOA6IHpW4zE2-Tis9F9tcOsbUcd0bK_qk0_YRzR7bcjHyffdgAzed5AlH8l05Ry4Yyr1ufzLfKpSIsWbORrzBux6yiK58Mx6m5_0nGDu0iFoh9ladys5hTtvTtgL_JnZn3jcEPqgvlpXrRPNvSJ5Bs6ajRKzO3QBymjeukGAMYuFuVDSsQ3_1Aaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQVEvDP3LRXDbkvpPxTilrqqSrdVC8ccB9FLeNcomYGHMt39sfv2dhb1ftJEX9VlzECxVQfSMoyWvOg87SpebYIeIYIzXkpE9qWy0w-2u2SJFwhpWzU_gQhs2YmAwpnTmoO71BXbOwHx6X2sBEGEJ2EYI4O69CCtW4VrQLQvoBQvjMSJISnrR5b6G98B60t6ZR-rPCAhEa9oCSyycwpaGsv6j9rJ85BjJxk6ZXGm0UHurofaNlk4JHGFcY364B0A2s45mqeKLPo_8MScOmjbWWlrQw9lrutwRolPiNV7PVFQsiNRcwCZRB3zCIpDyonSTfcV5rbHolWZMcRC4vP05g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4Qq3IbVaR7JU0pBpwaOLsvIyhowouxtGl93Ez7_83vbIhO4DrDWHOs4m_6gCD3iI1h2LGYV9xWFn0hQ39OGF3HD0hJLNaEE8JfFM2optkiRfus6scpZNXrsmPhe5vGqVUirtgHYB2vLPeSoEcIJTEqfmPcKwm9I7eUhh4RoEc_I_Rm6hpVjK_Xb_iCC1TEuEyV9LUeOIRdl5R_V8-YczBo2SwUnRevqUnH4mjtYzC20sVvu8FnPloq9Bo_9zFG4WiyPbAPUmGa7xk__hKAIw4qVczJfxo_ikjKKhZTJrL77oe8CccFo6_DY4Y--tOL8r3jl9EHGvJ6CQriFpN7Q1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARuP93SZKIlKT8E2kYzjcKgdlVLiIFv1vjsFhrQOD5K3jFvrh9EMurreTutuX2Mje9qM57Blk7GBwHIQAsSv8Lx1XyWHY01-lwiAXYwWfGRV_6kbJ8AJkQE5vFIfnKNp6hn6rLHgf-rSV1H2l1ClECRvKyCAbQC212EOokLkLRzF-8b9pLiTwsfEPAZ52wzWgiBJQ0lwCDW226QdeQoqdkUxXzbeH9uZfvcooukjvDdRIn6MxFaa0O4pG06KJn8QdwcsIVhlrWUTxuOg9bvsK-d-5CB1pzFBwb8KhiUUxIZl87FGn5ji3iY9PhNBERA2jWacUIlXjv411M9Ed_Fs2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOlYw0ncHB3QfO4_vWEv-JcPWwdlyLw_qnMvgBE8Un9ADG5mj0aijNwAAdysD1KcVb3mXAFuLb7Z4LxbvzU6Ft8E3PMgBuNX8uvAekEqwvchWPnSqt8sov1TJzFkW8opHVadhLYD9J1hpA4VUT9e0e2AQS706M0TViXFDS-f2CJFvguUml2FvGyrXKDCmTwxYB4XGKeZHUDmAQkuLe8VqOP6r85NJ6WdoHkjlczzz-YJBJvCvuy-0gpl7l21NTxztodnX034UIbJ23rbQxmFgljmRbYpu39gfpEy43_s_W2_i6vUGRvPujMnfLFu-3tWrF4TuKKzoJT5DmguRrlifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O05xgr5b-fQNf9z-ejfUtfLYh6BSksR5SOuoEvlJlbXrf8eFk1pMOHc_v26WOtp80nI-jn95I_HWT3v-ImlwloNZ1EnlVr-CFlxcJ_imJiirXsTSiuhFJNbIfCjKG-WQkttBK0GsfciXaNAu4WH0-_TCHIHtkix-XzSA-S5Q4eOcKtdRBMBZvYj9CgNJbw5lzrX6yN7SCQRDRRSZbr9toV44UBNu0Rc0axtTQbonoxi-IYrk_V7FaLMg1BNbwrMlPIU02ljJnlyEWd5RTOftLJ_V3zJmkesAxHan-lCrDy3pLf7mWFKWTFOMElX740tiey0txXQekAUh6EXi0GhZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fy6GabTmnGqFiNIKGROO59eQOhCOOqHoP9xvgQWeEeLfRsITt4o5gajIqJCxMIz1WI6zq0e8nBA9Idv0DV-Kkv0JcE9rRpNgQ0x311SVyyYoNbED4xEvuJrDg2tllElKpqeBFdaJ2bBC9QXOPoFe9ZRu2e3oD_6XzOyjlu59m1yzbIK6ZceJDrLdCfruKR9EqDrb1Y0UE5HTfNFFSO3AhLdETkQTG7xcDou1nl-9zGPpCBVmZ-eMaYg-czVNHCENxJmKyNHBS07lGnCl4U0YPB_Li_4Fre1SLV_NzESPzLSN6szJosWU_LQTSO-9A7ZHqMU6vZ9fRHI9WEsK5evpeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEL3TP4T7Ixy9eNA2gjMEYxONk1NMsbZ1yfd-WIrTouannBVR1nshv33-9p0Wg_NZmFtm-7t2IiMySM4EqV0aphtX_sXOaO_kly9ACc3nUT-GKiorkqIiXskxmfOlTD4Y0phOfDClFu5mjtuFiXZlN2o21qfkXIklJuk3IwLwqMsTWL_cehOm8UH_zVoDLbpyX9TXZgrjBCW_VGBVZy6WTBcPjyIv75x_02zysBG6ApEyonTSGgMlI33tBtpWqHDHC47Nt2PDNFzaaXeOdDJmfz9EszIPid8e8HD57nr5KwAhlBU4VDYyHwZRjBnf4ViQhOHkwvTIeJ-oNJaGWZmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cax1AIDDN_0m-JoP2ZzrpgNPCorvl5WpNPiy2ZmGg_hmG4gnAKjYnZke4ZJzSlyJ5qU8CJBnxGotBtbmzbga9isL8kHiVN7EgSbOAPx4SJr7pZFZRLewkyBiul5XBgf0abGOGS3SHpy11Z2xWiwn79nexCuOi219X-HiceO6c4oPWsrX3zauzvTWyVr5WaD3YflPm_zYtq6Nv2SbxFM1qYrD3QjREZAMl691S2o3i-CYs3UTubCWFXe5548Gd83rXIMol90K58YyIpWPDXNMWUCkiQig5beVckPZKNg1bFwghLbzfpu1RhrkLqWz_C_URCabsmkr7jJeZuxAEGY6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKjlKBlVUVGq3AzM3ACASJUH_ViK8qWSXmaKA-Hu57jId9fsB6bQYL0ZWL90h8xQbVD0bQXyBduOhJs-Qq2_cpFlhkhOG_LfREK08GI_m7vL7SMqyPM5OZVk6HDHSaphk24D1-SMHICavLK9j-kadIxLrHRUIhUUApBegjEf9J2eZMLrjSUCXSbeWAkkgquW84LzN6nQ02dqLIvZJ2MBYUorwAipAgAramkom6Yy7g0lGvhoyRq3PZAqxtCpaYKFpZMtYGswkTvYe_NGA_O1laIVh2aFAgyYZBwjA3hXXGXrLqcVX4BK_YCE3vuoHUnEJbxxixS__33xK3ivgjjLKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش «مچ‌بند سرخ»
🔹
مچ‌بند سرخ، نمادی از وفاداری به آرمان شهیدان، ایستادگی در مسیر حق و خونخواهی رهبر شهید است. با حضور در مراسم تشییع و بستن مچ‌بند سرخ، بخشی از این روایت ماندگار باشید.
🔸
ارسال تصاویر از طریق آیدی‌های زیر
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667772" target="_blank">📅 10:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZkoSjpssCM4SXg4Iu8fpEEM2asKXm2qXU1DuleNP2pZlhe9ogV2AsLM_QT_Xp1OhY3aaQLiCtfATHhZ7HtDLgXV_PgLwTUkK9vHn_VZkUiznwAdlFGFAb_9cZprnGfudyKToWIHBnzO4ApHkHOC5vKMDiJr-PsmgEhD1H97XjSdio27MPDutYn-EtOUGilG4ZyfudHUe63yJuTWjpVTzVUv9V3vuahTI6bpAhNMxNIs6migXRWboNYdSFtQXabFxvoxPkZ6yN2r_zumEu3ETaXAjJMEyj-C3_nAkI_NsEPAduQvUOzoFMftQ3-3jA0E6usbZUC03N6eNdpN6RxDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه صفحه رسمی تیم ملی فوتبال ایران به اظهارات سخیف وزیر امنیت داخلی آمریکا و شکست امریکا برابر بلژیک:
Dance with me!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667771" target="_blank">📅 10:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
کنعانی‌مقدم: مجازات ترامپ و نتانیاهو، تکلیف شرعی و قطعی انقلابیون است
حسین کنعانی مقدم، کارشناس و تحلیل‌گر مسائل سیاسی:
🔹
حملات منتقدین به عملکرد دستگاه دیپلماسی منصفانه نیست و  زبان دیپلماسی چارچوب و ملاحظات خاص خود را در قوانین بین‌المللی دارد، اما این رفتار به معنای عقب‌نشینی از خون رهبر نبوده و کاملا در راستای دیپلماسی مقاومتی و کارآمد است.
🔹
هر دستگاه در جایگاه خود منتقم خون رهبر است و نمی‌توان از دستگاه دیپلماسی انتظار حمله نظامی داشت.
🔹
پیگیری حقوقی و محاکمه نتانیاهو و ترامپ در دادگاه‌های بین‌المللی وظیفه جدی دستگاه دیپلماسی است و این دو قاتل هستند و از مصونیت برخوردار نیستند.
🔹
شمشیر ذوالفقار در همه جای دنیا بالای سر جنایتکاران خواهد بود، همانند حکم سلمان رشدی، مجازات این جنایتکاران یک تکلیف شرعی و قطعی برای انقلابیون است.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667770" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
روایت المنار از خیل عظیم شرکت‌کنندگان در مراسم تشییع رهبر شهید در قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667769" target="_blank">📅 10:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
هرگونه اقدام در تنگه هرمز، بدون هماهنگی با  ایران محکوم به شکست است
بروجردی عضو کمیسیون امنیت ملی مجلس:
🔹
تصمیم درباره  تغییر رژیم حاکم بر تنگه هرمز به عنوان یک تصمیم ملی و متأثر از جنگ تحمیلی سوم در بالاترین سطوح نظام اتخاذ شده است، قطعاً اجرایی و نهایی خواهد شد.
🔹
قانون مربوط به مدیریت تنگه هرمز نیز در نخستین فرصت از سوی نمایندگان مجلس به تصویب خواهد رسید و مجموعه‌های مرتبط موظف به اجرای کامل مفاد آن خواهند بود.
🔹
ایران با اشراف کامل بر تحولات منطقه، هرگونه اقدام مرتبط با تنگه هرمز را در چارچوب منافع و امنیت ملی خود دنبال می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667768" target="_blank">📅 10:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون آموزشی وزارت علوم: مجوز برگزاری ترم تابستانی مجازی ابلاغ شد
🔹
فرزند دبیرکل اسبق حزب‌الله لبنان: تشییع پیکر شهید آیت‌الله خامنه‌ای «رفراندوم جهانی» است
🔹
ترافیک سنگین در ورودی‌های استان قم/ ورود خودروهای سنگین به قم ممنوع شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667767" target="_blank">📅 09:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bea211e5a.mp4?token=Wk8NDMmime0pEuseYt-xoDIw45Pv3HoVtZmUaCjqCzqrWG9h0ViHKy4lwOs-Kfu6fI2FYtvItCkc1PuObdIPoD4r_7U8yw0SW6US0x-t2wi_cqDQ0lf7WZvU1kQT_yqwYQkAaR-ZLxx-R9C51dX3ZFNojEfTb6qV_AFdn26OU5npwsvqMEsoJkHX82CZuHlHphHZj8B3CyinyQQrJ_ELWSeXNdDR97rNtSbN6ysezbT5ks_ZjBn9MWWOVATpuKEtQrYQvU-J_Aea2BxTaqM74-12OegyP5KWbtkwSmoatRObE0jJmJ2oybC1FPhLaaqGe9iXsUgNOvE_XLU3GDhg1wgcar6yVFP8raU2TRz_c3D9cYbb5AvFjimbtSFXF3dRAR611_TpXBbI3Stx3BHymcaSou6JVblANT9Xgyg4RJCdZz6map3r6qrUTMS923OlSooxrDWnzwTCojR6pF4phzos-YZs0Tx9K6OSw_NSSXVHNw2ThEKWxLKVhJSveObx1C0fHWxaUTHWxG7JScMbTiwFDzpzHMcuxfmFsND-KE4UiWHamUR_HnaNJzpLTr6k68oemVekEo2R2Y_PpUBABEm8Vdu201JCAd582YWhXpiLbLU1IuUHVuQgdOtNccXArDnUBL-sMFDiwOLrZiLQAyMvLEyijml7rYrfbOlAahc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bea211e5a.mp4?token=Wk8NDMmime0pEuseYt-xoDIw45Pv3HoVtZmUaCjqCzqrWG9h0ViHKy4lwOs-Kfu6fI2FYtvItCkc1PuObdIPoD4r_7U8yw0SW6US0x-t2wi_cqDQ0lf7WZvU1kQT_yqwYQkAaR-ZLxx-R9C51dX3ZFNojEfTb6qV_AFdn26OU5npwsvqMEsoJkHX82CZuHlHphHZj8B3CyinyQQrJ_ELWSeXNdDR97rNtSbN6ysezbT5ks_ZjBn9MWWOVATpuKEtQrYQvU-J_Aea2BxTaqM74-12OegyP5KWbtkwSmoatRObE0jJmJ2oybC1FPhLaaqGe9iXsUgNOvE_XLU3GDhg1wgcar6yVFP8raU2TRz_c3D9cYbb5AvFjimbtSFXF3dRAR611_TpXBbI3Stx3BHymcaSou6JVblANT9Xgyg4RJCdZz6map3r6qrUTMS923OlSooxrDWnzwTCojR6pF4phzos-YZs0Tx9K6OSw_NSSXVHNw2ThEKWxLKVhJSveObx1C0fHWxaUTHWxG7JScMbTiwFDzpzHMcuxfmFsND-KE4UiWHamUR_HnaNJzpLTr6k68oemVekEo2R2Y_PpUBABEm8Vdu201JCAd582YWhXpiLbLU1IuUHVuQgdOtNccXArDnUBL-sMFDiwOLrZiLQAyMvLEyijml7rYrfbOlAahc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب حضور گسترده عاشقان امام شهید در قم در شبکه العهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667766" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667758">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAW9IsmTPwIKjrG8j7HBx927w6g2wXJ-nXgLRno9iB5URZcR0qM8dNCbWrze5-MySEgasovsOMl1d4ISLgsXFbF0iFn8lEo1lJVinc5i9wgKS6H-9mwhqyV3Q75n-qAGCNHWuQWKQMHH6KOTLKexAk3FXu6IqyXVQXQWUmQrtyVwZwOPZkT7KKVpND_0fVlW4h3mWFsu45P36i9E09auqYc5ZinyS6IemIiCNpMD0Qrr2SVowoGsTnGHJcl1XYSyRZWGzjGnGvwEMHNVVTHH9TKbpiFjPRWQmpFwlXMQ06Y27WqK4HbKXxW62pG0GwHSEXIdzZ8RxyKuPPXdKkQsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfSBZ0fCeAIs3e7C7Y-7N_Tr6J96mv2qxcefl17y_3aIwk52vA3IhHWHMDimcx_iIQy3c0auMSQiJJ_9Ruv24v6hMyLFo331epj1wxAkgoA-SRRJdhhUtCYj81mZedeJf5KaH_HrPMeSJPAOOoJkiY-jUI2UQhaTSinCRUbCYhMGfUlqG_mrQXrmKOg7EPvHLDw-vRDNyHlhHZhe1TLn2mrP_McqsjUxUNhNZpYrEw7tToyZQJJDwSzMstyU6NbRLCRC3Jl1qpPonyyODt9uwEucOxNcZqfo_p2ihDXNmAtHLbXNKruv4wCs-BFAiatsQovfJ2uKFU6Qb4McCpbSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6rku2IZ0RQic9I5gM_1N5ltYiAS6Ht5YPwZNWIL8jHHG-Pzhi2LN0I5_2Q9qZH0ROO-WqCIr_Nplts0w6k9QRvKKfDahOnOCQ5948rBLT2oAY_iY_7NKcWq5eSZunZUeqX_2LR1QFrNF07SV3bLdPq8jic9O9UpkQcxvdqWByOcRw5gZNV9phLaB61emsReWcbyriEc0XslMI9XsLHLlx6cogt5_mZRqQomjhPmyNytI35WYIZ3DIIUV5DrjiFBg1rCXiqZCbF8WLkl1KyO_hppbQx3K2Am9IseqDuAZUGsMSKXAz75LBmT465nguCoaCvwbk6k-j7ESdcq-kPsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V50WVTwndWpneWSt6RRs2M9Xjt5mEjFx3O6esgLQift-n2qrnQTWR6TwqpRaJIdGMsLzmOXqF3RdmFuOWzQWsT-A80gPA7FqkVGM9LsBh4iB66dxniiNOS4xAnYXYEi_Qshyf6aTSBu6U0U_gHTmvHmt7X-ZvNnfC74DyrulRoTGSC-spZ6KO2pjloDRCzv243BHNt1euuCLUBhtUGgF_xaKBDPCTH00mAlJ9TnJiGz7ns51Ic6f3r_QbxaS8GwL-OtRH61T3UiYrrew0Mj2HpTGw6lbbKgx0VosWQQVOTmsAzFSCXlQtgSWvn1eiQxDSMUclAqnra4JSFiN17G3Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tF-LMUYb8JXvDUNL09eiGyNk4hG1uFkNzYVO7QrD6caWCJTTX87exBDgnDgTp1ppjcOjDtNoEkXZQj-yMYka_pacIj114qCZnAeM6YtlpK7L-AFLNDfAQBTceuSUGeGFIY_KYr8962yibp77d9qvqYVUEeRSuoz_dBpKk6zL74B5yml2-6zhHza7nE-UEzfb3Czn_iUrt4s2sIBBk5JYv_snFVLEvjcw02e3LI6VPrYPWrmfsPzoad5YQ1O8dxSTqtqHM6FXEnmJn0Ss5C14NZo5ndM9x3EJ-yRDuxwS5qfYryoyxu8UxFL-EQiT3cqklGmYoHufTH9p_8Fliyfw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxRGlmUszOcdJ9vDxpwSfuOGdUxnaOhRCqWnO0tOjtX5hrSoYltcUOgv-RRSUXqOekdzshNTbY6Oa8oqD288C1NppK876OE_-6sMJPt3hbJzqMLnDQg4qyML1NXnX_rUWm8mYVycujasMX4PKWkI3SF65aI36lgvrAzZNo3Kq-531j6W_bkzdMgpGOjTRX77PDmTsuLsS51jRbbpmTl2sGzlNhzLwDpLh58Z1-00Gxv-Ohn1XvjCRB2fV1z9H7UNN6TfeUIJDo4BbshhRP-_Bgm7zE0fwpAiem9-iSE7W-qErxwJ0Uy-Dau22cMS57r7qGNA2ewoG-KdODXH0H8dZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bk3mN6kZKI8SsltCHGc9cWVD9Kkjtbs4ZJWaui3jNnIIRyUoU3i5gDGGFpnee_M1Z-0scaoQHJRTu8Dhxv3Spw5LyA9SMEzRsX2S8wEf_y1KRiGudOSgjRalZ1TTcXq-RKzzkNeAl6BRhivZUrTATG4YDO8U3cJn2E0KAHIVOFnz9YA5widjfq9SR28cA3m89LUg1ihqsw_yDKQ6WosRHRyH7HIwI2l0NbT4mlFcPQ5h7N7Qc3eoLUhS3p1Ez6Eln7nRDoDzuw43hwlSgP47kJ9eXgUxz7NB82xklvv628OPqyVEgUVBsBDsCFc2FQA0FuD3qbdr3-86okY1TZn8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrovyh72sK-fGkIWgMYAxHPZtB5AH8r5pXxdtrIE2FescVKTVuYPn0ksyBdn9YOoVzt5HZyvanbsn_OvThgC_VyDWXyid3TtnWeDXpP57rxhQJ1H8pCApNP7atKFnkVRuctOvEVk9QONzF07JDnmemTgLh5dFS-FnkRkpB2WCTfFg0MH14zZzwhXxKkOaXbniQSNIpC6VDb8uXqmxUVkFTnvJuKirWR1ePm2AoEKM1FLDwY3jsEUAwrct7EmhqU5Z8znLYv_mrtoRJ4bRQ3e9XtZRGU67lYvzt5ILExYBgdBpHhB015Sd2YcYjvykQDCJ6NMLkxZbRMO1MYSNPU0EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال و هوای تشییع پیکر رهبر شهید به روایت عکاس خبرفوری
🔹
سمانه صالحی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667758" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667757">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDDYn_HJK6hiBJF4m8q86fUrGnRiVVmkZlZpZFlfdCgpoKzFKzMmDHnyTBuVyKMM2rufC4r1cTK5fQHfWgPFRHtrX-YRBQAjKetIOGKWFfFOAfjgMbRAGeq91V9UCRLB16zU9my8Szahi_RAl12sxNc5SbNeUbKKueY4Qpe1uz3kb1gejiKVLMEvAKSYJWbqImI8VcktLeCavI0r83U_wUomqitkM6rEzXShWiUrAH64D7NKWY4olpdIL7oMWUia72H4zBkoHursSJv8OwdrWSjSe4WiTnp3y8wxOkUv1d7qlGfKYYISkXPbkoyyQEmebloPQ0J7V9oi9Iul2XkgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا بار دیگر رکورد طولانی‌ترین دوره شکست‌ناپذیری تاریخ خود در همه رقابت‌ها را لمس کرد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667757" target="_blank">📅 09:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667756">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIBEmpD_VuTYsx0vpPqYY-jGC16i4rLH2v49YMMhZ43ptq725gYHBfLj0mUY_nCWQ3IjQ019pSIyQWIfxg6aqLBuFphCDfN7cC4HkC-AMiGLVtwPHuBLZWYl_cM_D6nZ3TAvgZ_V6DC4UYZPnKZBZ-i9MmmRZ74qeHEb-EVkxthanXPHkcl9b8j2w8aOGYjE8054TmtLUtfEo6qfeWENu8Wr8JOArqpWLMUCwhUAaRyJN4sq4ShhVrcZwvdSRRPOAOmCSbNNUntdeUgC-aajBpaSU4JgW6kflp5olRuh4oTXSwGWn6l5UxCDHd2p3MdgjLAG1KFBE_BISf5O6EIYfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۹۷ هزار واحدی شاخص بورس بعد از سه روز تعطیلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667756" target="_blank">📅 09:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667755">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f8b7cce9.mp4?token=tsf8qImSqaU9IVdK519BFeKzvbrUjN8oDHDotH_mPi9UApBjEs9uZN6mX0w4sQ1dVYp-X2i_ivEwv3TJ_JdK-YXlPjsVNv77PdG4O2ifjyGCwvNwQ2oJPIwxwS3xpsZ-2-yAfnKAO8LQsWP6t4iDYTCFh0D2jyNcDtIthI9mzEOOJXQanUIp--XsxEXbw_3SLhtxJ4YBzUAWRoAR_4b8vrIGpU3Y1XZGYbJexhroUVniOC8OogL0dDmU6naxbHKIWtc3MbesATnJuPYk4NVLZVPKBtNR9UFoskR5gMZFhWVVZF005AbC_a6cLZcnnnOdXp_27V1VhrzHsMmtRaofuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f8b7cce9.mp4?token=tsf8qImSqaU9IVdK519BFeKzvbrUjN8oDHDotH_mPi9UApBjEs9uZN6mX0w4sQ1dVYp-X2i_ivEwv3TJ_JdK-YXlPjsVNv77PdG4O2ifjyGCwvNwQ2oJPIwxwS3xpsZ-2-yAfnKAO8LQsWP6t4iDYTCFh0D2jyNcDtIthI9mzEOOJXQanUIp--XsxEXbw_3SLhtxJ4YBzUAWRoAR_4b8vrIGpU3Y1XZGYbJexhroUVniOC8OogL0dDmU6naxbHKIWtc3MbesATnJuPYk4NVLZVPKBtNR9UFoskR5gMZFhWVVZF005AbC_a6cLZcnnnOdXp_27V1VhrzHsMmtRaofuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو قاب متفاوت از آیت‌الله جوادی آملی و رهبر شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667755" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667751">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccHaSg3QZN2r7lgmQ9hXu0pJAY7BPpzpTLJbOE9gpCjIBUiVOeFGUlZh2E6o7lt5E_1mUwdgATEODbTt3yK1E8u6hiA5GdFiHGOqi8_oivX03Piuo6bxrXSqRGUHC7LzGb53N6XYNCQ6dKludkN84W6xX_6BGhnehm1SP6pxLUKdz-KkQaA64DY-W8sJzB6qSLPhe6KjkTON_0CLqw8Jq12FPS9Y3UOrWcYWSaISlNhdXs8cO7dtQW5FBO4LTrK0IRmLTk89ZEl0d9YdLk2TmA6GAGrgAxPs9QpmrC2QIkDHvLmRZPfqiUWSe0W3aIX_ZUt4dJUroipHRG5FJfOqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvCnVUBYDiwBIFdvHk6qcjCiUBYnCXxDqmAswlMvX47WfMxA2HVP1eDg11ASoBpHRHKQR6ZnEUXWPha1qGisAq9rK8PpoD42LqLYL0es9O7GT_vFuXnemrXIlGTdezKJoVq6jABQnyeCGFIWvnBMZOtnp-JRDoNs8jWCZBCXYrIQfhZr-NKy1wttRQE-myqrZb-VuL7euQx2dDWyQnMN6ooWK5n5Wm4VoIg3MA1v6g-XOKRiSexnViPrdHTlpF3Uap94vu5SLWPj9dmF3xyKXuWErTz3bYL71TX3lQ-Laq1AK-lH-eQSFjCGTex-hbFxCI8m2UeIunOYrEpCblyhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oaR_Wjayw0iRzmplxP14ZGWRegCQgQ-WZzU32edqJHBYAeYLkuAiYDVQQqhjqeX1FJGJlKkJJqFD9-aXpvIWdR6LB2rQSX8ijw6s_RG9zPEzqlfQyhKGM3LfkdqFkiXT_37gvJj268cD1cRiCuEEGg7Iv4zfqMkKl2iw32Oj3IyQT9XSA3Fd90lHKWMfdA8uJnTdecmj7r_RUldOVzQIWr--lGkyquCh_TAULen133WoMbqrTCAqABivA3qCzsrU3LUbMLNYXknyEVevLSFI8UgdvwBjtIdrZYfHa4GeAyjtz7QTP5PaHNTevWopOuLYXm48fkCZlFzSO6dafHANkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3JIE8bQn93fKFlth0uWGDLG19ZXF2LLyENkDGq4x3o47nB2ZaiUYfkJg-32YgwzWIub_SDvgdxCzzbSRscCwXX8keA5PYdg_bDT-ob5Log9lJCBxZzYXkzsafclQm78CAoScWZt-pOwTfcgrmQwMXeQrgZIEAOFXdbfrWRq9YfG-z2x1O17fFr357-3Dbf0MWdEcERv1snxR4T8bhDPEUI-Fllldv8w1XfKN3_D-4pYqEw4Vdde-MPdoBKmkBCf_H6kjS05tFOjkJIGD4pkvFgJMh3uTmplSBZRXSaS9uJsmz_-nrGtuFsOV_nc1X9p9G0cIQHKkW8kAr_tCVJdgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آماده‌سازی فرودگاه نجف برای استقبال رسمی از پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667751" target="_blank">📅 09:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667749">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e919e965a7.mp4?token=tOBXaceWlK7BuKr1V0-uiDsyoRpFd8dh-HXtbNwBrMPpm0G6moxqNj4sVhRJxb0mbSKhubxQEVrK6qQymf2fjNLZPJm5848sgEqUunmFdn-uhP3IKY31H37XUcYF4eOHrUWsLoBDRstVg1ufhgT8bq6-y3GHXMj0bdKj0FXcrEw6yJt7Wy4VpMRh4RZxjT93ys7fsJtTBu9Dtmv9vDI9u19UyxVgkT5MCxzl8GyHl3n7pPjY1SEnpaeHfPB11aAYQoX_q-kBmeWoN4XQ5GHcyBxv2SqnW4JwNEC_ZM_Yie36ysHfSNuzEa4VNo5sZTlX-4t_lCrc--1jwcj3ha-gHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e919e965a7.mp4?token=tOBXaceWlK7BuKr1V0-uiDsyoRpFd8dh-HXtbNwBrMPpm0G6moxqNj4sVhRJxb0mbSKhubxQEVrK6qQymf2fjNLZPJm5848sgEqUunmFdn-uhP3IKY31H37XUcYF4eOHrUWsLoBDRstVg1ufhgT8bq6-y3GHXMj0bdKj0FXcrEw6yJt7Wy4VpMRh4RZxjT93ys7fsJtTBu9Dtmv9vDI9u19UyxVgkT5MCxzl8GyHl3n7pPjY1SEnpaeHfPB11aAYQoX_q-kBmeWoN4XQ5GHcyBxv2SqnW4JwNEC_ZM_Yie36ysHfSNuzEa4VNo5sZTlX-4t_lCrc--1jwcj3ha-gHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری: پیکر مطهر رهبر شهید وارد بلوار پیامبر اعظم شد و این مسیر به سمت حرم حضرت معصومه طی می‌شود و بعد از آن به نجف منتقل خواهد شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667749" target="_blank">📅 09:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667748">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
رویترز: پیام ایرانی‌ها در مراسم باشکوه تشییع رهبر شهید خطاب به آمریکا و اسرائیل
رویترز:
🔹
برگزاری مراسم باشکوه تشییع رهبر شهید ایران تنها یک وداع ملی نبود بلکه به مثابه ارسال یک پیام مردمی مشخص به آمریکا و رژیم صهیونیستی به شمار می رود.
🔹
مراسم مذکور نشان داد که تلاش‌های واشنگتن و تل‌آویو برای تسلیم کردن جمهوری اسلامی ایران شکست خورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667748" target="_blank">📅 09:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667747">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993310a40d.mp4?token=X8wSJ1Lw7JxkfpGCOoihNhheanGgwRup1Ne3z2zNDacpF5AEbzB0OAieFJZ6g14mLW-rOKTWIpp6fP_4W8ke5uXik4Y6pn20mPAG-4dyX36RSE-QDzkICmrxuOIbccu1SBTgYmaON0AZ2_4S_dLBssTcoLisFNYZV9-AAKd--bOjzNJH8xBTOQEa4G7OHuAqZOqxXMmwxF5iMVc1NGP1Db74CLciVvy1mPWx5JA58L0QXC0LFjWKHa58PhQWtvw8v7gOpG3_ah_SnxDEzTCjrHAm99E3O_m3H2g3G7Bza2kDu1FK-1jJsbKv-sgHJlUH-t5XyCeh4P1-_c6-6bib_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993310a40d.mp4?token=X8wSJ1Lw7JxkfpGCOoihNhheanGgwRup1Ne3z2zNDacpF5AEbzB0OAieFJZ6g14mLW-rOKTWIpp6fP_4W8ke5uXik4Y6pn20mPAG-4dyX36RSE-QDzkICmrxuOIbccu1SBTgYmaON0AZ2_4S_dLBssTcoLisFNYZV9-AAKd--bOjzNJH8xBTOQEa4G7OHuAqZOqxXMmwxF5iMVc1NGP1Db74CLciVvy1mPWx5JA58L0QXC0LFjWKHa58PhQWtvw8v7gOpG3_ah_SnxDEzTCjrHAm99E3O_m3H2g3G7Bza2kDu1FK-1jJsbKv-sgHJlUH-t5XyCeh4P1-_c6-6bib_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون - قم/ حماسه ملت ایران در تشییع امام شهید
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667747" target="_blank">📅 09:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upswYnsqhr2nbpdlK8Zvb9QoFmk-2h6KcsGalTUJRxrFTwODN9jlksEvcKhTurAfCW0zBtcRR8m4IBl-0EQWhYI_YwJXTypTeCRiAQksYL1oDzVSAXd-vt8la8sSEQsEtVQbJdLjMiB7qPMUxYRVXIsn_6DeN-6XuSpkJSdh_uP5j_7hJsCyyLGrE0xAthKfB-V59ZhzSj59ayThtsFEKTllAAHfIb_7KBWm-j4KyZgPrUHqfi_MXtMMz8VoLoFc1eeCwugM3kFLwXQaXJDi_RobZ67IKYocfG4W4htdPKjwZcWJIdHMXq6TxyazoUvw9UDqVmmVXaa6QKQPCs-U2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش صفحه «Troll Football» به نتیجه تیم ملی ایران و آمریکا مقابل بلژیک در جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667746" target="_blank">📅 08:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAWaWFIDUihP-zhYVyWyaxfY9cmqlNWWCpSXr6HhaHYFS9wb0-tMWHQdgokpFeNv80b8Tg74lcrDGhoqDJ4FJu7ieELuYpsIB0hWbOwP55e16jYYSt9K1AK0MOmhVBcguJLIyiEuusq-8ybFNnEqusgdBvIBSiAwv5EPFhhiMZlyawkoeCZ0PWfiQXsIyiegjrQpLeDjaFseYat5RIm9UjPJPLtR4o1Pfvg8qHylQ_OoDXjcifstBJ0n2N9FkYqcOS5fru3sB-n7VL5MHBUGQlOOHFzjapgV0heToAYqKbHuqL0FZQnpp9rszhFjZuY2Md6iK2tLHgGmh5RlJaZz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4GAK-35bhgIi8gu94u0EQ17PpHRyXCa2nWRdMytaIWWS7ClwJZEGb03Z4nAz_7ZqaCZ33tVyOJxP9ru4uIaNewu5XMJwt3pAyhaiGD8OY9gTS9CURlv62iQ1aisVJaoOtr9LPgEozUrCsUpfGBxK_J3x3HIV1TslMRp65ttY9ZHzKISF5YoB1VeWF5DBMoWxktFFy_ahrzqCZ5jLZGV--Rl4yxoOxJWUTA4FKPHMZQEUjC1u1dJk6SsRJ7qy-p_3Ud13l8a5RpYABxa9lF6TaIXOTj5GRDORHGZ4J22tKlFu_jj6NZlpFj1ujoP91jANu6vB6Tp5VLfpKG4DiXIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHFhki5DJ19_x65P1PoXW672VoGi9T3vddrTiNaMNd-bUDC76b_Izk1R9yCOYK54NpziOecydnH-c96fppIv1BYKqfax5Hnq6NRPqCi6USjzct2s7fm1mxKuKSGK4b2T6MT0PJKkc1JCym6Yx2V-z9eBxvtkd-9NoWd3nMWlOrfK2HfkG0Hm4u5sflq88B88Brm2BnqLk2WiumMq73jAV5iQORWu5fWJQ4MXsUqnBG-Hz53kUsTs22vWvStk7TEGwO4AiTjEmEfdJEU18HmT_MWWWmFzGpT-TShVxVvkRpcvYXOjoiUxCRJOzN9-TZ5ucGhPO-TykaycSh-ejXBCaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUYQBAo0KoEisX-nB13fBguf9cnzORZM52z2iQbB_2mWM8040Jw4BjXk6OOFNQS3as0i0-_1x7PEf_paiAKzDwaUjhMXqqVJobG2iIoz_I40kkFNrCW6t3uWxzTedW_Y65aO0C8SpfgOw8X5a6Hr4m_VXGSEkAO751-6te0eKLpFhByxgYDsUPWZj87bnJYncdap0Z3xdhnk3aj3v5K5KJkWvhYJR4jjjKKhXsgmnqithIF95u3IbiIEVYxvZ6k3mMSVaCWtIUTmKFrJgFjeLZV9BhhqJAxZ_pZ646DuHoA8eRpYtXg8vHSW3ArkRT8wmn-f8K_-07G9EDMC1peCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0uDlX6PVJenTYAO0TjmlIJmohHWhEL8HPRMT8WSSofcCcFRM-D20yt8OmRNiVYYOr49PNGQqpXKEvShJvNSq_GYOmrpgW1LP94iQ3GNb7yqjU96HcLuzJheUIaG9lvhxXOLLRjJfOLoDJceB0yPc2vujLwTxb9XSqDhgWEOHfaiivN2LtF1ZwLVDQadIGVrjwA4C--_WosOIRmXEtJlhBnO9b298IxqjXYZfnSj2xPPlgkk_pS5WoqAxiWGu8tFwyS5KbB91cxw4kT3GjhlkuZROMUh-2k5LXzGpFt04WUYExFCnr6AumXt9VV29mUdNfgIDQI8v6e8TlwIbSJoBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFDtd8zACvv-Ju9Rr5nEyDGBM1XFMZXpnXikmOcS5yTXuhJ5wv3iGkN2eoCA7kdpE3gTT5ettw_ML2PE-qMiMFbmSItokATjiaPJHJGu5E_QSV6Hmt6QdUEWNHm1NjuDaFmrn026khB7L3TFoMZiIzWSG31DrGnEyRfQkQZE-w-l48DeXsKmQ3RDneTrmzV72Hlt7auVWm3G_nZUfstfUR191MLt3-VfTl6Ed1jQyIQ7YA_Uavkx4hsG9tgvZ6fDBqZZTeMKcWXlJJLFkOAQ2s7tRGH8Yi-1zesgoNfo5WeqANOK3vqn9rsN09TeLrBB81e1zOdYFAQMFrzli1GJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObDyQ0wsIa62w0EaLHXR_rINETGbOqhWZligeeE7UtonB9tj10Mu3_8E12VHOKW56Zz5fsztaIacgqYelLqqgJSjZTAjFSKYqXPhwHghmd4yGjX4lMCXguhw9F9pHyAC-h6t_s4HTn4tu0K-9Gl72LxUlW4J0_GE1fSpbhl0Ey01mzotNVNiKPsmZXYzDe_7VD6_ZdsBnMkg9BVSnUKZ5BJVBByH8m7aORQ82O7FTZ0WVE-MnB99nLzVJsP0gwHWMTK963o6KaBiVIJWoitevUezvS480h2OmGBSykRlGzTaNG704q-jeytckiIk2egcmbWUKcyD_H_F9PFZZluriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7Eu4vMGjaFc3MxyD4pSIRXutmQ6oT5tVzmYJbbQe3vnUPo9woBPqevMo_Sh6HBg0sQ_GcpxFhq-xZlxoGAvdzgC51_ldF5b7luKjSs2YGeICjtFuKAi_SJFGgVXZ5fd8_C3atw0w9H4N_N4FPw8Zb0Xacgh__pF5CPd_ALXZI5qIn-Pu0Il6IeqsgL9GZ6JANzkFljlVfm_OXqMqEwi_sYk6w81U5GqlRU6xSDjB6ZyXQKdd90-TOCKVDKHceiYiguoYZO2P8erj6ZQ878PqlGY9qBhv4cZcNqIY80tBkSqAlgjiLREBTblpHYW4X7ewHS6OWYV9HTUs9Dp0-mP6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قاب‌های هوایی از بدرقۀ امام شهید انقلاب در خیل عظیم جمعیت مردم قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667738" target="_blank">📅 08:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667735">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ab3e269f.mp4?token=mt80nJTlJ_5bgkIYYmEY0eJ6n1pgLHLKgEmfDxvI0wQWVhSJ1pQuB3sMfEIOG1t4Z4o3pRCgER92Wlkb7oJXzQKTAR-WYTByHP1f4iumuoPZH8jYW8Ic9t7cCuqwpvgjWtth-mdit_o2kA8pIzS6B5fn55oyoyWsC6d7C4kwkptCY6ZLJbb9kj58Al6LaBNNV1yYl-8zjj4i4se7uN_3lFbFULp9Deu0sRNqs3AMA7p4c4SSeGiN11ldz8grIO1zu6W7isHSQWI48a5OLinT8lcXQc5xSzvWWxft3yvLLwb9Q6fi8xZM1vCq0NmGoNhHAQcD_e2HW3gk5snEefIKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ab3e269f.mp4?token=mt80nJTlJ_5bgkIYYmEY0eJ6n1pgLHLKgEmfDxvI0wQWVhSJ1pQuB3sMfEIOG1t4Z4o3pRCgER92Wlkb7oJXzQKTAR-WYTByHP1f4iumuoPZH8jYW8Ic9t7cCuqwpvgjWtth-mdit_o2kA8pIzS6B5fn55oyoyWsC6d7C4kwkptCY6ZLJbb9kj58Al6LaBNNV1yYl-8zjj4i4se7uN_3lFbFULp9Deu0sRNqs3AMA7p4c4SSeGiN11ldz8grIO1zu6W7isHSQWI48a5OLinT8lcXQc5xSzvWWxft3yvLLwb9Q6fi8xZM1vCq0NmGoNhHAQcD_e2HW3gk5snEefIKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از حمل پیکر رهبر شهید در کنار مردم قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667735" target="_blank">📅 08:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667734">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA4PDRDwxWyXWFf5oVKkMzYhmFQk-LSpolXH8EPiJaP8t31g6746ooEFA0VIQ6PcBgldKxGYxa5-PQTGvbn2mwO3H7PFUYR6rY6P-z-H5MBkH6uuU74aMxaUbg2gNaRJyWGUtpeH_zbrTJZgJRwBipoccGIo87EGNh0dsmr45aThgNnuG8x0dZbkiEgJ4Ee5NTLWgqxozksn4YG05e0Ku3hmlYWJ_tO9KFzM5ORCbjvvF4GXkxw0gA8OHFOjybUq5ouhwPwPVQeAIUfMnVhjF23m91l6gSiNFmlo4orXOqADn9oXZKcKnQppv3MDcC1C9N6VMMP0bnouQeOZ-kp1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: نه مردم و نه نیروهای مسلح شجاع ما، از هیچ تهدیدی هراس به دل راه نمی‌دهند
🔹
میلیون‌ها ایرانی سرافراز با وحدت و همدلی گرد هم آمدند تا به حضرت آیت‌الله العظمی خامنه‌ای و میراث ماندگار ایشان ادای احترام کنند. نه آنان و نه نیروهای مسلح شجاع ما، از هیچ تهدیدی هراس به دل راه نمی‌دهند.
🔹
بند ۱۳ یادداشت تفاهم کاملاً روشن و صریح است: تا زمانی که تهدیدها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد. به امضای خود پایبند باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667734" target="_blank">📅 08:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621896a9b6.mp4?token=cmA1YGUUmb5Q8FRIzDMaO9MyHTjLvzB6GBLqz96MHRlwMNwVfo3am3gWIkGyCFFfK7FQsZHpnq6-In_gAqqYKlVZg8u6cb63rExfGYu7Wvhy3CUUiZaBUVvLhbzjXF2nb_cndF_oi52zi6jqA-9XqcEXIrizBg1-M8yKorv-dBIpun43PyHmVJ1w49RvfPepr6c9Vz3BEBF0cEskyG28mX8hwwGRrBnE2iUkXJTOUt50gIQayS-pkhanimDXIaUt_XeDGO2gfvqTL0AsfjuaxpFLkVVNLUUAtozhmQHkoF6sOM8EGn85cAW6kmigq6jvRJL1y4TyFSHlwK5ppyaoJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621896a9b6.mp4?token=cmA1YGUUmb5Q8FRIzDMaO9MyHTjLvzB6GBLqz96MHRlwMNwVfo3am3gWIkGyCFFfK7FQsZHpnq6-In_gAqqYKlVZg8u6cb63rExfGYu7Wvhy3CUUiZaBUVvLhbzjXF2nb_cndF_oi52zi6jqA-9XqcEXIrizBg1-M8yKorv-dBIpun43PyHmVJ1w49RvfPepr6c9Vz3BEBF0cEskyG28mX8hwwGRrBnE2iUkXJTOUt50gIQayS-pkhanimDXIaUt_XeDGO2gfvqTL0AsfjuaxpFLkVVNLUUAtozhmQHkoF6sOM8EGn85cAW6kmigq6jvRJL1y4TyFSHlwK5ppyaoJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودرو حامل پیکر مطهر امام شهید و خانواده ایشان در بین انبوه جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667733" target="_blank">📅 08:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde1b5e396.mp4?token=bDRxWLxcE2aw2s7zjN2yX8_knDnWGF9uA1Vzh6y0bh7hDYDEdZy0UrnBoAfdGiJZzTtALOarM7qOJkB9uLipS31AXuiuBFOwHv6SAT5ZTGnLF7uUwygUe1ZtTq00SDqIAK9hA5DQ5P7MNjK-NdShUHQZRZLx716UuagWZXufgat2gUAg8nPS31fiJ-blJlpc9EOf6QLYNiolAiNJAZLZZvca19LF7_-MgQmIklcrZTijlW4C_euUAs8wMDga-aPUfqv9ymZo8C2cdqz62ZObTy1orMSoHuTm2Vxk26L68YVRmdk-4etctb7tRDwSlzCpBC7S8vLLMI3IMTiLP1X6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde1b5e396.mp4?token=bDRxWLxcE2aw2s7zjN2yX8_knDnWGF9uA1Vzh6y0bh7hDYDEdZy0UrnBoAfdGiJZzTtALOarM7qOJkB9uLipS31AXuiuBFOwHv6SAT5ZTGnLF7uUwygUe1ZtTq00SDqIAK9hA5DQ5P7MNjK-NdShUHQZRZLx716UuagWZXufgat2gUAg8nPS31fiJ-blJlpc9EOf6QLYNiolAiNJAZLZZvca19LF7_-MgQmIklcrZTijlW4C_euUAs8wMDga-aPUfqv9ymZo8C2cdqz62ZObTy1orMSoHuTm2Vxk26L68YVRmdk-4etctb7tRDwSlzCpBC7S8vLLMI3IMTiLP1X6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع پیکرهای مطهر رهبر شهید و خانواده ایشان در شهر قم
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667732" target="_blank">📅 08:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3cfb2952.mp4?token=WIPxZ_5z2gsWtCf6zBqo7Y5qfqjdy-ml-fpvA8r79pb3SJBrL2eawhl0QDg0YlIKi0PXUl7FG2KJIZYcKPZ_cJnPqnyZl7WGkHaZ9ySFvqOzNCQcj-EMoYa6kUjdMJCx_aBft3JM8D9xpzEXjEfluftUNCWSZluO594yW-7LZZfSjHD20448ssxvfdJHXD0IYUgfzlgFgyb3jHHV9b37JEGyzBB3ayIsOUAr9IR3i7Am7ir02I2OXQKZ6zcIEX3CuzZ61PxQeJhqE_uqO6FlsGETdWvzkLonJN5UvtdmjPMD8cuLH68NgdLoe-72mAVo4EK_F4_Fjuz8W9O6mW9umA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3cfb2952.mp4?token=WIPxZ_5z2gsWtCf6zBqo7Y5qfqjdy-ml-fpvA8r79pb3SJBrL2eawhl0QDg0YlIKi0PXUl7FG2KJIZYcKPZ_cJnPqnyZl7WGkHaZ9ySFvqOzNCQcj-EMoYa6kUjdMJCx_aBft3JM8D9xpzEXjEfluftUNCWSZluO594yW-7LZZfSjHD20448ssxvfdJHXD0IYUgfzlgFgyb3jHHV9b37JEGyzBB3ayIsOUAr9IR3i7Am7ir02I2OXQKZ6zcIEX3CuzZ61PxQeJhqE_uqO6FlsGETdWvzkLonJN5UvtdmjPMD8cuLH68NgdLoe-72mAVo4EK_F4_Fjuz8W9O6mW9umA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور جوانانی با پرچم نیجریه در وداع با رهبر شهید در جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667731" target="_blank">📅 08:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667730">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هشدار دریایی در مازندران؛ شنا و صیادی از امروز تا پنجشنبه ممنوع است
🔹
معاون پیشین دومای روسیه: آیت‌الله خامنه‌ای نمادخرد، شجاعت و زندگی قهرمانانه است
🔹
وزارت کشور عراق: توافق عراق و سوریه برای هماهنگی امنیتی در مرز مشترک
🔹
نخست‌وزیر پیشین رژیم اسرائیل خواستار نافرمانی مدنی علیه کابینه نتانیاهو شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667730" target="_blank">📅 08:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7e992159.mp4?token=Cef7LVyBG8mqNLIYzP0u6Xoanac1r0-16WpxMWwzCUN6sn2tQqSPMd-ZQQP_dZfgPAyG4SuqSASN2kp21hTqce59qOxI5htUSw7fa2umvlVqB974fuax8KaO5PWvkWu_0SEZWZmhzgnDw7RX7dJuD44nMG8I7kC24XwTyN55tdCsLEzVlcqMGEHqVfgRH_kf6VlbGqNBebp39qBDLIm7l9hM9Y5cQsuWovLVc51OCilzBdcUIV2O_n5L5ICAvdFww9EBQZUwZ7AD_hqkQS4kL8RmaiaXj2ghp7fm2yoP4_IJe0EBuPoCu0sVLY8lLgjWmmKil2ZoH3N4kHN4nbt1VplB-kb3KnR_Bzcb9HuHywy6DeUtseedtYEd22RtUPvssxnwK2vOXZSCPW56s2z2bfUU78iohN6Fs_kyw1SX7d-HsAhL3cIwoYgItjIabM-n_QM9luxYdXlAhjWALNJXJ_5B5swdU9ais96NlAoF7Sr9sWKdCPl0ogCHauoF-1T-tW2EL4xeJQUhH-vkAbdueArF3NeogmwPt0bupmPGnH41tMVSbqHAjgiKEgr3q-9gURpVntkmfOwLR4VHw9kHfjAwsWI6pKWxR05TNaGJgQjHV9VtLPVvqHOQsZXCrD2pCHVq1e9N3O7ECSz_MitlhBJz9ilbNKXUJdRMeWebLBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7e992159.mp4?token=Cef7LVyBG8mqNLIYzP0u6Xoanac1r0-16WpxMWwzCUN6sn2tQqSPMd-ZQQP_dZfgPAyG4SuqSASN2kp21hTqce59qOxI5htUSw7fa2umvlVqB974fuax8KaO5PWvkWu_0SEZWZmhzgnDw7RX7dJuD44nMG8I7kC24XwTyN55tdCsLEzVlcqMGEHqVfgRH_kf6VlbGqNBebp39qBDLIm7l9hM9Y5cQsuWovLVc51OCilzBdcUIV2O_n5L5ICAvdFww9EBQZUwZ7AD_hqkQS4kL8RmaiaXj2ghp7fm2yoP4_IJe0EBuPoCu0sVLY8lLgjWmmKil2ZoH3N4kHN4nbt1VplB-kb3KnR_Bzcb9HuHywy6DeUtseedtYEd22RtUPvssxnwK2vOXZSCPW56s2z2bfUU78iohN6Fs_kyw1SX7d-HsAhL3cIwoYgItjIabM-n_QM9luxYdXlAhjWALNJXJ_5B5swdU9ais96NlAoF7Sr9sWKdCPl0ogCHauoF-1T-tW2EL4xeJQUhH-vkAbdueArF3NeogmwPt0bupmPGnH41tMVSbqHAjgiKEgr3q-9gURpVntkmfOwLR4VHw9kHfjAwsWI6pKWxR05TNaGJgQjHV9VtLPVvqHOQsZXCrD2pCHVq1e9N3O7ECSz_MitlhBJz9ilbNKXUJdRMeWebLBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای مردم در مسجد جمکران و وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667729" target="_blank">📅 08:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
خروج چند واگن قطار باری از ریل در زاهدان
روابط عمومی راه‌آهن ایران:
🔹
بامداد امروز تعدادی از واگن‌های قطار باری در زاهدان، از خط خارج و موجب مسدودی موقت این خط شد. کارشناسان فنی راه‌آهن، جهت بازگشایی مسیر در کوتاه‌ترین زمان ممکن به محل اعزام شدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667728" target="_blank">📅 07:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp6N0_Rzeyg4-VomKVki5NkI0hrB6VfGsGT3v26kD_Pu8hsHFsRi7sEaUVt4hdtZXOAQLK74h-7lRULpgCqAi8C6zyTRDqPJltyiB6vjlQMRYaEfujikt8gkAvQpvxo4QjlhCh9PpRmmQ9GE4Z5XMwW6cdU0z8GfkBg1jlbifoyTpVPbpqsQPOhyMaDhInK1tNHTBYTnBAguaaZeR_XGtFilX9X7gi7_Wccax2phOQaHSGC7YX89c51Sjr-WO1J3XSlng6HEiFMbmdHmrVeHgJMPU2Aba1pCLRrNq8v7b3MHtg-VezUVRTONzaGl94c0Ro1OiA0YMfdujXSySpTiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667727" target="_blank">📅 07:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc26bff3e.mp4?token=f2xNyeoaIpRAeenX7z-UfLil-AM5cEY8IAIcm3dV1oywqG6myoGRY2KjngX0Izy90qQEGSpEH9EV-lrUtfS4ioX89ZMkcf0iLP_CRDOtmWvG8ghXHPAJio0Ma0eio4X-1LGUf9k8IcjhHf4Xptfduly65ocve9hLs2uAhfwwwEdnXWXYS8DgGuL94CjcWbEVHm9sdFisBTE2fgluOfIg0PCWyMWK7G-7VRPi7AAWRaQbr4aJbeCz2OFMiJVuvpsQcWZ5KmeTxElHUYlUuwGT6GT035KT59nmMg4pq1d8y2JyQyRgHlWt8MjGUX75S3XEKpLfSvRLDBYkR4ADslqQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc26bff3e.mp4?token=f2xNyeoaIpRAeenX7z-UfLil-AM5cEY8IAIcm3dV1oywqG6myoGRY2KjngX0Izy90qQEGSpEH9EV-lrUtfS4ioX89ZMkcf0iLP_CRDOtmWvG8ghXHPAJio0Ma0eio4X-1LGUf9k8IcjhHf4Xptfduly65ocve9hLs2uAhfwwwEdnXWXYS8DgGuL94CjcWbEVHm9sdFisBTE2fgluOfIg0PCWyMWK7G-7VRPi7AAWRaQbr4aJbeCz2OFMiJVuvpsQcWZ5KmeTxElHUYlUuwGT6GT035KT59nmMg4pq1d8y2JyQyRgHlWt8MjGUX75S3XEKpLfSvRLDBYkR4ADslqQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم خونخواهی و یالثارات‌الخامنه‌ای در دست تشییع‌کنندگان مسجد جمکران
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667726" target="_blank">📅 07:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f642d5f0.mp4?token=Kebu_vAxwQ2jEr3PwcGPygbuZDU7nlTP21EmQe9gjlxJRuYdnfvCQkkgwMAJ0Cx9NDcJQmB9b54fNpeFY3mC23mN9fmrzMBbsSP4YzHJ6OAa-LFYfCg4eurclyvjCscwunb3bdpue4Q65pxP0nVjybX22OO3YMMKG5rIcErWOFfc2600EWcfBMoZbZPaXifG7soUxOiAzW8ptCCiEbRsuaQecDbznoxzMp8OD07gKQYZQrlQCv6mAAYO7HFGApaH2SkM0cjlcbeDr-zN9xRYG-RkudHygjb5MSLDBbVLB4DS8J-OgXqwgaLtoHcSwbg6ymhS9gepI5D4LbTAVIWitw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f642d5f0.mp4?token=Kebu_vAxwQ2jEr3PwcGPygbuZDU7nlTP21EmQe9gjlxJRuYdnfvCQkkgwMAJ0Cx9NDcJQmB9b54fNpeFY3mC23mN9fmrzMBbsSP4YzHJ6OAa-LFYfCg4eurclyvjCscwunb3bdpue4Q65pxP0nVjybX22OO3YMMKG5rIcErWOFfc2600EWcfBMoZbZPaXifG7soUxOiAzW8ptCCiEbRsuaQecDbznoxzMp8OD07gKQYZQrlQCv6mAAYO7HFGApaH2SkM0cjlcbeDr-zN9xRYG-RkudHygjb5MSLDBbVLB4DS8J-OgXqwgaLtoHcSwbg6ymhS9gepI5D4LbTAVIWitw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین شعار «لبیک سید مجتبی، فرمانده کل قوا» در مسجد جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667725" target="_blank">📅 07:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667723">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حضور جمعیت بی‌پایان عاشقان رهبر شهید در خیابان‌های اطراف مسجد جمکران پس از اقامه نماز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/667723" target="_blank">📅 07:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667722">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inpxhuUydXVvZ2lJrU1upEgCKE5KFinc_FtADi76OwvHRsCaZRChOHHSHHhuwx7JILHc0Q60InIoqC5nJqvTQOGkT3t8nGlIgJJ92ECucNNArtxj8hH4KpIjErmqq63Iivm_MAtZSiwS0gVMHv_y1HWZ9y6smRR-AjKxzkKWNkMBp9OBPo3aoOYBbbvHIkow9rkK48oC0z2HARaHVS0zpgHhcyrvZTIHXes47L7bQ-9xWhoD7zGNyLVOVt3JESaEu4XehF5EfdgDdMI6Mw11bh_A4UqygtoFBeJnSm929u3nDy_TJhmv2KJJJnpo8fn4UV59MTMDabRd7dtaDJx8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار درختی دور یک چهارم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667722" target="_blank">📅 07:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae3dbb160.mp4?token=IHcQgI4xntbYASVuATYR8mmZD6WluPy_pOaxbsNXz7KmkBsy_BKIgQNiDtCWZv_n1PkcEtdkp_6nPQbAbBh9gY3q7cI420AnkdNdcsB6t7GBuz1iByGSY7XA3snaIZr2PAU3yCTk7WoppDMAGammnE9dUGc4fGePYZ1KfGYI9D1qEuP7VgCmuPhI1JyCg8dHwLOj08qeA7IEbCAGJRxTlBgTsrFsUaaD88VWsKnM3Xcx7QH_uumJaKhkOvuBuXtD4Bg5NIqFS-xmjIXlBMxFeK39Vshs4-R4z5pXpCsB5-pVeYZjw15grWI6twavtnwGgUytAZg2ad23O1Oh141BGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae3dbb160.mp4?token=IHcQgI4xntbYASVuATYR8mmZD6WluPy_pOaxbsNXz7KmkBsy_BKIgQNiDtCWZv_n1PkcEtdkp_6nPQbAbBh9gY3q7cI420AnkdNdcsB6t7GBuz1iByGSY7XA3snaIZr2PAU3yCTk7WoppDMAGammnE9dUGc4fGePYZ1KfGYI9D1qEuP7VgCmuPhI1JyCg8dHwLOj08qeA7IEbCAGJRxTlBgTsrFsUaaD88VWsKnM3Xcx7QH_uumJaKhkOvuBuXtD4Bg5NIqFS-xmjIXlBMxFeK39Vshs4-R4z5pXpCsB5-pVeYZjw15grWI6twavtnwGgUytAZg2ad23O1Oh141BGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخواست سیدعمار الحکیم از ملت عراق برای حضور گسترده در مراسم تشییع پیکر رهبر شهید ایران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667721" target="_blank">📅 07:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667720">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQTLmpOW5RVkyKndiTGhUOJDoGBYASP_0b7DhwOfKJNG5ntWpdPxMvwcg3vhcDc-byXY7bYKnNONSNndbVj6K8mufA5_FsY732Xe9I1ACB00d57mFythfW6xTZpsdWApk2-JRine7Cs2Qd9mqfE86scmK5UNxXLlx9wVIV6nvhttpXtdEbvfNdnnN_bQV6kWfd0GexEFHKUqZKNLLyIp0O08taf0yg2y-f-nBdbYOdcbLO5-Vwh1LyLdjSAXGLBJ1TINQWOBy5a426OvaLBo6kjnSbrj0MzRlkd3gPj-NhEvXs_3YSTfpphIN6d93iI4wG2BY1RRu3ke9QZloYARKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب تشییع پیکر رهبر شهید در شهر قم در سی ان ان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/667720" target="_blank">📅 07:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUuTAprMxg-q_jfBQ-0BdJfwtUQzQ7fd0nJ2BkK6agmve9jC3Vi1jE1ZM1oUEh7bRePPWlJs2VPAV-QgkDYfrMkV0gLaJmG9T8i-cexoNWu7ujdaSy-v0wP_kSLYjgx1vezn8QzgbXz4e3IziZpRZWFqkPgwFxXSizTnE_npQk0isWROo3uRcLqNAFzouYLDyYogFY4oSE27MASWWDj2aUGjKABdSQWM9Qw8-khRM3EGN4sbadrw5CfFk91sUu9dpyYm-wDl1y3WJLL8WxBSYvmTCzqsTAx8JZHPql3z1xvVWorP-ih58F_s7Ez7m8PdltYs9Q5IATKWzuOkL69oUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور خیل عظیم مردم عزادار در مسجد مقدس جمکران برای اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/667719" target="_blank">📅 07:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhilzOJiOlPuYhYZc7suqc64DEH30Y_EnBmWKRFHVDI9G3jJcFpAqdxPqOv8JlxKjOJltH2VSgx4nc4Nk6_Gk_OtR1Zl4HfTINAh7h5kdu4ptNNhn4ZWmtWroewCtS7-2UMsprqG3BwgnLrN_TBfPMjUcfvqn2dL-FDYXMLZE5luXwtO4jzaQvFKX5edROnuzz8qrW_oVI4qdHIhf8-GjAWniOxgnEvQWiMhQrEO7d5WKg8r3T3fwj2dfYfAfu468ldzZM8u86nWOo0thjZ8-sevudkpv1gQMrZrJMLPV69aqTCprOCE3SqnFhtdfih2FiIdldsN7aGfiPBv1JAuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دخالت ترامپ هم مانع شکست آمریکا نشد
🔹
حالا جام‌جهانی بدون میزبانان پیش می‌رود؛ بلژیک با تحقیر آمریکا به دور بعد رفت
🔹
بلژیک ۴ - ۱ آمریکا  #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/667718" target="_blank">📅 07:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340788de5.mp4?token=rGRFParpYWj8NWyy_quDthkGYWIqkM2OHInCtBEz3xupDJiXUyxP2xhQ_XGv0SDXtGx49LMHW8hTEuZLD8qCq-N9CkPii5o20RjVESQinp1RcsWKrM8vLKd_4er2kVLsz-nrK2NPMQHMPPDCJI5jjvLpM5Em5urBHRSt8FtjTDuESy8pIFoPs5p9rgZHGoVgxNXG7AFhuBAn4VLiZR1HeUm7GXkisKzTW6ywwgFRxenyjGJTbICbht1kRjm4qwQ4v73Ntm3SKREbi0IJHP-wALUCOVSwxtrpSqhSW8hypdImtHmkMhMBT_s-mqFr4MSI3P22R7zgSpMrRrGBUqzxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340788de5.mp4?token=rGRFParpYWj8NWyy_quDthkGYWIqkM2OHInCtBEz3xupDJiXUyxP2xhQ_XGv0SDXtGx49LMHW8hTEuZLD8qCq-N9CkPii5o20RjVESQinp1RcsWKrM8vLKd_4er2kVLsz-nrK2NPMQHMPPDCJI5jjvLpM5Em5urBHRSt8FtjTDuESy8pIFoPs5p9rgZHGoVgxNXG7AFhuBAn4VLiZR1HeUm7GXkisKzTW6ywwgFRxenyjGJTbICbht1kRjm4qwQ4v73Ntm3SKREbi0IJHP-wALUCOVSwxtrpSqhSW8hypdImtHmkMhMBT_s-mqFr4MSI3P22R7zgSpMrRrGBUqzxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم تشییع رهبر شهید انقلاب از بلوار پیامبر اعظم(ص) قم به‌سمت حرم حضرت معصومه(س)
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/667717" target="_blank">📅 07:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667716">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65aac1072.mp4?token=kzAvyg3yyEupk_oVwK0MVWcFVHdlTdYIEuBcAcJkJhTfX_V_yV1NWDzYFAj0i38NYqubeQAeu0Y7ZgqLs3EmBw7q7SLm01uoynEftc5qeiItrwqQImYnOcd_x7MB8vR-CbKq6feMGB3pmhoZ0ik8M4NhBieoYqaaJgdSvL7ottrNU8HVMRqucvwhAaSxdr6pexGVgNSH2s_b3u0PX1BlD8A5iR0y4DfnTkqrXo835FEeeYM9_RHzxBj7BijydQRKwfpOg_dFq41Wv_eXV9vb_DyjO1FJxVNJpaB4Jix-y9Hr7GGyI9sVOjBOZwK0KAMBxswIlWfopVFd3BmfTPSigQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65aac1072.mp4?token=kzAvyg3yyEupk_oVwK0MVWcFVHdlTdYIEuBcAcJkJhTfX_V_yV1NWDzYFAj0i38NYqubeQAeu0Y7ZgqLs3EmBw7q7SLm01uoynEftc5qeiItrwqQImYnOcd_x7MB8vR-CbKq6feMGB3pmhoZ0ik8M4NhBieoYqaaJgdSvL7ottrNU8HVMRqucvwhAaSxdr6pexGVgNSH2s_b3u0PX1BlD8A5iR0y4DfnTkqrXo835FEeeYM9_RHzxBj7BijydQRKwfpOg_dFq41Wv_eXV9vb_DyjO1FJxVNJpaB4Jix-y9Hr7GGyI9sVOjBOZwK0KAMBxswIlWfopVFd3BmfTPSigQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از سیل جمعیت دلدادگان آقای شهید ایران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/667716" target="_blank">📅 06:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667715">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/667715" target="_blank">📅 06:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667714">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4da758a13.mp4?token=ny5529t_KWOeJfN8NI2nDBbqmCSBHcbSoZaGPU0yzppghz_gEfNZ1Coc7oIEon1VldLRHZwAvpcpVsEMN2_PqjjoGYL-kX_HZhU8vOAp4fCVROl7PkhTQKlBcli1BQejqlDcrDDVemR0rsp8_9nVdWDzkgXypfNqozZDicn6G81MCOD7BjqjFdtrTxU26lGNFU_8HRQqRm9gpi1HnwTbEZNA_ZuPqUkgCOmTMnTZliwslvoqMFRQrWqDvrFdoXtpW3MyL38IdNDGxeku7Ong6K2wZ3z15_5pvXjdlaeHKjAeco4Kt_O0W43S8_9tk497zMIghqpjw08Qj6fhzZr6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4da758a13.mp4?token=ny5529t_KWOeJfN8NI2nDBbqmCSBHcbSoZaGPU0yzppghz_gEfNZ1Coc7oIEon1VldLRHZwAvpcpVsEMN2_PqjjoGYL-kX_HZhU8vOAp4fCVROl7PkhTQKlBcli1BQejqlDcrDDVemR0rsp8_9nVdWDzkgXypfNqozZDicn6G81MCOD7BjqjFdtrTxU26lGNFU_8HRQqRm9gpi1HnwTbEZNA_ZuPqUkgCOmTMnTZliwslvoqMFRQrWqDvrFdoXtpW3MyL38IdNDGxeku7Ong6K2wZ3z15_5pvXjdlaeHKjAeco4Kt_O0W43S8_9tk497zMIghqpjw08Qj6fhzZr6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب اسلامی در جایگاه وداع با مردم در مسجد مقدس جمکران قرار گرفت
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/667714" target="_blank">📅 06:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667713">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d199e23a.mp4?token=bJT_uQLzF-KgjaEXiefCrExILm1v-FcVQhNsUyn3qRyjZCi39-Qx_ttnp29uIMhaeo5V9uik8sQHlwK9NCIEkhbTosaeH62q7pZaydJBje0_KwrzhYC13a2irKkp6q8N0BeNqJlnpxzdxNoFmrksMm_ojHIhWITxKGGmgRlDRt6BGnpyWVrawLppKn4SnE_Ktzj1d-WoOZ7PjpQtW0kioMz1iRdwM9afxJMhV6RbL0nWCPKB2pcJIfYfzG_bMR-I9tCjJJsjxSAQAxU3XA6zAcwvLyaxg0Lslu5hI0mFgaq43m1So7TAMCLbpZ6A6LclrAg3fQosnYFmNpv7bXfBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d199e23a.mp4?token=bJT_uQLzF-KgjaEXiefCrExILm1v-FcVQhNsUyn3qRyjZCi39-Qx_ttnp29uIMhaeo5V9uik8sQHlwK9NCIEkhbTosaeH62q7pZaydJBje0_KwrzhYC13a2irKkp6q8N0BeNqJlnpxzdxNoFmrksMm_ojHIhWITxKGGmgRlDRt6BGnpyWVrawLppKn4SnE_Ktzj1d-WoOZ7PjpQtW0kioMz1iRdwM9afxJMhV6RbL0nWCPKB2pcJIfYfzG_bMR-I9tCjJJsjxSAQAxU3XA6zAcwvLyaxg0Lslu5hI0mFgaq43m1So7TAMCLbpZ6A6LclrAg3fQosnYFmNpv7bXfBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوسه حجت‌الاسلام هادی خامنه‌ای، برادر رهبر شهید انقلاب بر تابوت ایشان
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/667713" target="_blank">📅 06:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667712">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708f8482bf.mp4?token=rdxvrQq5elQr9kBkogX9P5c9epGD4thOtAMRgTZsSZ2LMp8kV692GFr-J_hO3FNERPaGf15TgJhyVO5BRtAWKmAmSPkjQlhyGet6d9kn4e9gcOtttJT25-ng8j5bUbrXSURd_yN1jnDpctoTssGpFrN9SiMQxoY4wNbtzpjlw9VX1stz15Z2pJCP4wg-GSxAXtemhwTVFF-jrnN21dsOFtSmUxsGoke_5eZ574fKbbULHfJ1jy6UqWFnuufIt0lvE3QoSqd_s2sl0wt6dD2qL1CTYxIb_sOf1qWJzd010-kfdUGzKmKzVrJ0m01aqyZeBJcLXbR_XqZfg33TW_b9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708f8482bf.mp4?token=rdxvrQq5elQr9kBkogX9P5c9epGD4thOtAMRgTZsSZ2LMp8kV692GFr-J_hO3FNERPaGf15TgJhyVO5BRtAWKmAmSPkjQlhyGet6d9kn4e9gcOtttJT25-ng8j5bUbrXSURd_yN1jnDpctoTssGpFrN9SiMQxoY4wNbtzpjlw9VX1stz15Z2pJCP4wg-GSxAXtemhwTVFF-jrnN21dsOFtSmUxsGoke_5eZ574fKbbULHfJ1jy6UqWFnuufIt0lvE3QoSqd_s2sl0wt6dD2qL1CTYxIb_sOf1qWJzd010-kfdUGzKmKzVrJ0m01aqyZeBJcLXbR_XqZfg33TW_b9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری عشایر لر در مسیر حرکت به سوی مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/667712" target="_blank">📅 06:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667711">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f0b87e60.mp4?token=Pgalp4lt-PoqRzK8JqaAVgPKPG16JYwSmQCQIYmHmn7B-bexAl2306Tt3-ZgdJwkEV3VJ67lSAkP5KhA2KAwLf-bauq4vHPj_eUk8-6pnYR-w67YvS7vdQitdb-QMPu_5PD7bRQv_Fcworze6-4hyoGKFZbg-rJas70QG5ghl09iWD5a2awg0pw_rnVpXEmNVbJFqUyQoG7zurHbLShSzaNovAlxxRIRppt7rFBaRsptc12akahvtX5oSF9iYJkt_hyJ8jLsIAFC3NX8qOZsAZqCv4M2aefg5ASWFmuY16ZwfG1-cpuoaooWILCXu781xQvAjeNOkg13VYsT3t7MeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f0b87e60.mp4?token=Pgalp4lt-PoqRzK8JqaAVgPKPG16JYwSmQCQIYmHmn7B-bexAl2306Tt3-ZgdJwkEV3VJ67lSAkP5KhA2KAwLf-bauq4vHPj_eUk8-6pnYR-w67YvS7vdQitdb-QMPu_5PD7bRQv_Fcworze6-4hyoGKFZbg-rJas70QG5ghl09iWD5a2awg0pw_rnVpXEmNVbJFqUyQoG7zurHbLShSzaNovAlxxRIRppt7rFBaRsptc12akahvtX5oSF9iYJkt_hyJ8jLsIAFC3NX8qOZsAZqCv4M2aefg5ASWFmuY16ZwfG1-cpuoaooWILCXu781xQvAjeNOkg13VYsT3t7MeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بانگ الله‌اکبر زنان شهیدپرور در بدرقۀ آقای شهید ایران در جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667711" target="_blank">📅 06:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667710">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641069ca79.mp4?token=SknC-lOBZ-OQJQkWY5c8ScWM4QNhdnovG5L5WPTKDfauFJ3x1lQz79jn-LrNutMWHY_w6UzB8U2Ha2qrV3jH91rSaX2OthEgjjWmM6COjtbczZTAPdq2eQpx2AG_7SuosomfpV6Lo007p_BPM-h6mGSvmLsayb9Bb2EFfi88jTsSxe9YvIl6JUb9PyjZLx0J_R7jqB3fn6UunpqJcdKcdglnwpLpmCCyWRGCwvd9qwJvQIY3y0eBFdfams6NORSD6JpKtLO1xChzGT8KZgAt-OLNfkMoi8Z9Js1Xclfun4eXGIK_XDXAkPVsPOJh5nsUq6VPFD0yfpLrQRPU0n_ELIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641069ca79.mp4?token=SknC-lOBZ-OQJQkWY5c8ScWM4QNhdnovG5L5WPTKDfauFJ3x1lQz79jn-LrNutMWHY_w6UzB8U2Ha2qrV3jH91rSaX2OthEgjjWmM6COjtbczZTAPdq2eQpx2AG_7SuosomfpV6Lo007p_BPM-h6mGSvmLsayb9Bb2EFfi88jTsSxe9YvIl6JUb9PyjZLx0J_R7jqB3fn6UunpqJcdKcdglnwpLpmCCyWRGCwvd9qwJvQIY3y0eBFdfams6NORSD6JpKtLO1xChzGT8KZgAt-OLNfkMoi8Z9Js1Xclfun4eXGIK_XDXAkPVsPOJh5nsUq6VPFD0yfpLrQRPU0n_ELIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع علمای قم با امام شهید امت
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667710" target="_blank">📅 06:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bae6eed2.mp4?token=KDZSqFJCBnkZWI_s_RvuWPHiludLNgJ9pHRRW1e9PkFtMUv7UzsKvf77RTFn-hgEKcGz41M8uz9aqJYbR-yTI5nfOMNoxwUsGeCbxfmUoeWGA6CsY6dXo2nMAl52soaEuEf_FGSJzDi8X1EtybBaAZUKP1hM_F8Fa9IE6iUU1xwGeVpGEQ2gSex1mTxEiJTAsvdr5X_rmJC8PdlLhSfbTdaLh1oYizNFu06UcnCG6tBvIOQ3Z_AH8mkShN8BnqDbl5NX23wEpI0Xl3haQJG2dmGwnCWWkqQSm2Hk__b72EOKSLp4_kvuNM2mH3pWoElGH6tWhBNe48GwneDynEzBL5jZHn8Co-O3Rnzy3nqAV9WoPfZeA7-eAy6cly1mc0Azc88OTTRbGHoHpjcReDhPuw0nemKCdlc08LuHiZ1y4ebHPaO1uUHIFoqJJjwSsYtta0jvR0aQ6jelCeyqFlnINBx9g3KpaBx7KMf0PA99EE49R51iMnXUqIhmwxk3XDY7F2aaH2Y9EygqgYM9TeL1ARk3yYMBQyi1MBGNbaucwpbdDVMHSx8qdzuDTWsvVJzsvLVFe-EBXuTdvKwiPirAzuhjHWzrlgrXom5I0vFtN_pBoN7tZjks0SAqaMnmCVdPlXUBvG9cvgjmcvKPn1GMypMrVz6PPFUi8AfKo45xHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bae6eed2.mp4?token=KDZSqFJCBnkZWI_s_RvuWPHiludLNgJ9pHRRW1e9PkFtMUv7UzsKvf77RTFn-hgEKcGz41M8uz9aqJYbR-yTI5nfOMNoxwUsGeCbxfmUoeWGA6CsY6dXo2nMAl52soaEuEf_FGSJzDi8X1EtybBaAZUKP1hM_F8Fa9IE6iUU1xwGeVpGEQ2gSex1mTxEiJTAsvdr5X_rmJC8PdlLhSfbTdaLh1oYizNFu06UcnCG6tBvIOQ3Z_AH8mkShN8BnqDbl5NX23wEpI0Xl3haQJG2dmGwnCWWkqQSm2Hk__b72EOKSLp4_kvuNM2mH3pWoElGH6tWhBNe48GwneDynEzBL5jZHn8Co-O3Rnzy3nqAV9WoPfZeA7-eAy6cly1mc0Azc88OTTRbGHoHpjcReDhPuw0nemKCdlc08LuHiZ1y4ebHPaO1uUHIFoqJJjwSsYtta0jvR0aQ6jelCeyqFlnINBx9g3KpaBx7KMf0PA99EE49R51iMnXUqIhmwxk3XDY7F2aaH2Y9EygqgYM9TeL1ARk3yYMBQyi1MBGNbaucwpbdDVMHSx8qdzuDTWsvVJzsvLVFe-EBXuTdvKwiPirAzuhjHWzrlgrXom5I0vFtN_pBoN7tZjks0SAqaMnmCVdPlXUBvG9cvgjmcvKPn1GMypMrVz6PPFUi8AfKo45xHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«محراب جمکران»؛ لحظاتی خاطره انگیز از حضور رهبر شهید در مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/667709" target="_blank">📅 06:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667708">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7406fc2868.mp4?token=YgGnylfRSAdB-qP2v0-yD9KBwHshnRSKH5n4cUFFh206EyMD2d2-RHK3JIA2vxFkhGvvt2RPciGe0GGHjimRcI9-n4b_6hSYJvePMEYkhjef4j76qqphBn6R4lKAAQrQk0rtLOZH9J10I7iRdXAmPyifm1_Juea_bJ2puNSltUyrDlPCgsY8gulKVu-P26JHsbtOFiw9_x5_bJ3ihmrxOOo_i4tAGqexeSgmruuI4cwVWgToCG59-sE75RA9Z1k1tTYc8jxHFnf2u9VtCLrDTihZ2kZgFlektfSxpUri5sOyvPP83bWG0h-7ok7fti6GWLyJ5mmFHWeyCf9FBuCKWRLI-C3EfsG9Ih5rVm8_B35g9lt1tZFQUUmNbJ7EwFJgqTvww9wYgO6NG6tolWdXCx8N7BLlHXtl2uhr2HlhuYeQJRjYL1N58csNs8TyU1a3dA3mcMMrXDFNJLiI9b-3zizCt5ZN72GeSZ9TtHLlcySPrdkNzgQ6K6da1mI8bYZXJZ7ygvAzDr2RQWXtq9PMQ0Ei1Xb2VeoBT0pEqek8VRExXDph-4tM2IkAQxshhgfE-idB1lYcWwmI6qDp6c5dBt3JDe9dRWNkmbM8cxDdf1AIi34aqTkdxpOc6WYTidxKHKiMRVVxNA337SwWxKtUyIyewJdWruBjPKGe_xouUxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7406fc2868.mp4?token=YgGnylfRSAdB-qP2v0-yD9KBwHshnRSKH5n4cUFFh206EyMD2d2-RHK3JIA2vxFkhGvvt2RPciGe0GGHjimRcI9-n4b_6hSYJvePMEYkhjef4j76qqphBn6R4lKAAQrQk0rtLOZH9J10I7iRdXAmPyifm1_Juea_bJ2puNSltUyrDlPCgsY8gulKVu-P26JHsbtOFiw9_x5_bJ3ihmrxOOo_i4tAGqexeSgmruuI4cwVWgToCG59-sE75RA9Z1k1tTYc8jxHFnf2u9VtCLrDTihZ2kZgFlektfSxpUri5sOyvPP83bWG0h-7ok7fti6GWLyJ5mmFHWeyCf9FBuCKWRLI-C3EfsG9Ih5rVm8_B35g9lt1tZFQUUmNbJ7EwFJgqTvww9wYgO6NG6tolWdXCx8N7BLlHXtl2uhr2HlhuYeQJRjYL1N58csNs8TyU1a3dA3mcMMrXDFNJLiI9b-3zizCt5ZN72GeSZ9TtHLlcySPrdkNzgQ6K6da1mI8bYZXJZ7ygvAzDr2RQWXtq9PMQ0Ei1Xb2VeoBT0pEqek8VRExXDph-4tM2IkAQxshhgfE-idB1lYcWwmI6qDp6c5dBt3JDe9dRWNkmbM8cxDdf1AIi34aqTkdxpOc6WYTidxKHKiMRVVxNA337SwWxKtUyIyewJdWruBjPKGe_xouUxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مسجد جمکران در مراسم تشییع پیکر پاک رهبر شهید انقلاب و خانواده ایشان
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/667708" target="_blank">📅 06:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667707">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5477347a.mp4?token=ukUsrvBp7kDg1F3ok-4wT8skJ8GWSfyKssIE8v7qsnzykTIFwNmooIszqKNHYqKOHumMozYc-d2Vg3Zfj5G4aZHEGBTk-mh34O3J5ps6SqajYR2kZ7INik8oNRBiVnpIP6DtFg-p3iY90l_lhSJJA6DsmL0q7TFxcQ_AwAa9zyktk5HWWOEVS2VhUfigtlKtqsTgywsOLBXv0zGZXLg3xTWfApOKMK5c0-RgkedcA2xelYHM7jQFuQJe7N0-9XtPlb13NQERoOiDiBAJ8idhhWR1YYuGx29YtM1A5v14gnj7uZ2gdAZlIcOp4OOGZzsKcBaW7OdcAae4ZCkhmb6HfKUOWUaQjkJ_SkVfjTppRKjGLE9v8GaSkp5k4QWeNfuoUdv39kafDwsjQXVw4OV4eNcndreuPCiZHGlEI0s0oyc8FZIVRAFmMT-dLBvxcu3mzdzM0bB4jCEPYLDlSGtjv3y2f27JxVcHm1VOgWvQU7G1kc-LnNzzQ59ul3G3Mxf6xXxRlXfB_LLWpMewV5sjDLM9VHOXYdUTQ1YJq9wNDx22wsjUuj5ZbBv7AH9QqEcDHh3H6xL-yRwk6HQeAAzeifWA1GF4uyU9in7Y1W2s8qlmVakTW4CRu43AWz_QuG05-kRPOnElDdExdnPCm1Yc7giq_dRmWTCR68ODtE01V-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5477347a.mp4?token=ukUsrvBp7kDg1F3ok-4wT8skJ8GWSfyKssIE8v7qsnzykTIFwNmooIszqKNHYqKOHumMozYc-d2Vg3Zfj5G4aZHEGBTk-mh34O3J5ps6SqajYR2kZ7INik8oNRBiVnpIP6DtFg-p3iY90l_lhSJJA6DsmL0q7TFxcQ_AwAa9zyktk5HWWOEVS2VhUfigtlKtqsTgywsOLBXv0zGZXLg3xTWfApOKMK5c0-RgkedcA2xelYHM7jQFuQJe7N0-9XtPlb13NQERoOiDiBAJ8idhhWR1YYuGx29YtM1A5v14gnj7uZ2gdAZlIcOp4OOGZzsKcBaW7OdcAae4ZCkhmb6HfKUOWUaQjkJ_SkVfjTppRKjGLE9v8GaSkp5k4QWeNfuoUdv39kafDwsjQXVw4OV4eNcndreuPCiZHGlEI0s0oyc8FZIVRAFmMT-dLBvxcu3mzdzM0bB4jCEPYLDlSGtjv3y2f27JxVcHm1VOgWvQU7G1kc-LnNzzQ59ul3G3Mxf6xXxRlXfB_LLWpMewV5sjDLM9VHOXYdUTQ1YJq9wNDx22wsjUuj5ZbBv7AH9QqEcDHh3H6xL-yRwk6HQeAAzeifWA1GF4uyU9in7Y1W2s8qlmVakTW4CRu43AWz_QuG05-kRPOnElDdExdnPCm1Yc7giq_dRmWTCR68ODtE01V-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیتی که انتها ندارد ...
🔹
مسیر حرم بانوی کرامت تا مسجد جمکران مملو از جمعیت است؛ موجی از حضور که لحظه‌به‌لحظه بر گستردگی آن افزوده می‌شود.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/667707" target="_blank">📅 06:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667706">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=gJocUcyG736kB0k5y4dBTv4GDlFCk8T0iPHjkm80NiVfAWRlBqhzWjQYaXoZeXuM8qxxatYq3WgVNbdKTd9auBFlUyzldQajXweaH2-3ettSCnXAwl3YcUglCTKk1hsEClCgJoDqfD3aTaoTKMVV16_1R8Jl1FNQULAkxK2kjMgDguX87h0NHJEG60v8ujmmZJJkBNX-YZD3DxKdLTNN2U86fq1bPORKgSa1Cs9CqREqFGv41o3YxNnGOdh0GMaDHnyowE4ZO4s6hEJWbySbhaKvz1L4mCA8OC5DWvz1rOKehxPC-eM73ZJy0JGYdL40uD6Hb1BoWmVugEbNu5MAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=gJocUcyG736kB0k5y4dBTv4GDlFCk8T0iPHjkm80NiVfAWRlBqhzWjQYaXoZeXuM8qxxatYq3WgVNbdKTd9auBFlUyzldQajXweaH2-3ettSCnXAwl3YcUglCTKk1hsEClCgJoDqfD3aTaoTKMVV16_1R8Jl1FNQULAkxK2kjMgDguX87h0NHJEG60v8ujmmZJJkBNX-YZD3DxKdLTNN2U86fq1bPORKgSa1Cs9CqREqFGv41o3YxNnGOdh0GMaDHnyowE4ZO4s6hEJWbySbhaKvz1L4mCA8OC5DWvz1rOKehxPC-eM73ZJy0JGYdL40uD6Hb1BoWmVugEbNu5MAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین انداز شدن صدای آقای شهید ایران در مسجد جمکران و گریه‌های بی امان مردم عزادار
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/667706" target="_blank">📅 06:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667705">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae271e6a3e.mp4?token=a8S81seqZSVBzTkpuNHlRY3kyO3lnyXwGGOeg71MfE8JDHQMZ9ZbYzrLukt59Kd0f26ORgG5tTcnizlZnBHn17dPjZJS1qQRtph_shwsquL1y3q0uSAd8GZRZ7ocXyLH5cqmP582bR5nZas-_AvZXY8K4d9FOMxLd_fCois2sj_3HSn1kN3d5VZD-KOMfPNFoSew3CFuljiiyfpfJHE5SreJEdiq-M8L0clP9gX9o6PIwCLwgL0w0fKqCj-rVTYj6iC9bwaA-e69oB8akj4-w-szD1bPJCQe-4i7MJuDNMI6COzdHoZ1nAKEqzmVlQHdwIY8310R7KiCCA5C8SFf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae271e6a3e.mp4?token=a8S81seqZSVBzTkpuNHlRY3kyO3lnyXwGGOeg71MfE8JDHQMZ9ZbYzrLukt59Kd0f26ORgG5tTcnizlZnBHn17dPjZJS1qQRtph_shwsquL1y3q0uSAd8GZRZ7ocXyLH5cqmP582bR5nZas-_AvZXY8K4d9FOMxLd_fCois2sj_3HSn1kN3d5VZD-KOMfPNFoSew3CFuljiiyfpfJHE5SreJEdiq-M8L0clP9gX9o6PIwCLwgL0w0fKqCj-rVTYj6iC9bwaA-e69oB8akj4-w-szD1bPJCQe-4i7MJuDNMI6COzdHoZ1nAKEqzmVlQHdwIY8310R7KiCCA5C8SFf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار گرفتن پیکرهای مطهر شهدا در جایگاه ویژه وداع در مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/667705" target="_blank">📅 06:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667704">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9290566f32.mp4?token=X-4_2OBbVAO6QHYunY4HMen85ATDDk37CETtCc3z6zSQ9oE2bDjPuPfh7ojQMfKffw-NFJt48QAzkEWMtYBT_Gq451vd_Bwm40-_0I-tWPeQwThsDwVTf6H8RdGWaNfNa7IuRhNL3r8deEnYsOHR7dwvamT-SrXcdCwX1fRcKQ-_ykgqdsAR_cr40eayF05sB53yXmJ5zxMWVjbdVSdriZG8yWHG6Q112gXu18U1E3qxmGxJjAp37k1NXYEXcEb093fviqYsAM-oE05GIfd6lAOsWjsdy8w-TN81N4OOIZehjgQBGzEy-kAtOua5PRICvoxHddtaK-2YHPtt8uKfRketXuZr6Ca4s2d4eofUTwNcdDK1jYUveJNxL4ns2kVPaMDcZlCmfrEhA6Rbq395f6nB4CnvLFV0_pYpem29Ott3K2pcyp_2Z6Z1KKno3yjL4Vqsuyag00ocOd4O8qFdDj3RvmouEwqbSdf2FVKPdKUSBmR2wd89Mf4PMI8TYs3du0I-5uNwfjywcQqcSa31E2I2_1P6qcqwtbZnCtv2GTFkIQJQu7pONtGjNmSZMlnrkbXW-0n61YgN2wf7P290pYMHYJIZAmrqmDvpl5laOiDTlKXN0-4UljNwAlo-rLD4IepL41d2gGbmwMYdp3gNrjOZI2Z8Fl589wnPpVT-fYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9290566f32.mp4?token=X-4_2OBbVAO6QHYunY4HMen85ATDDk37CETtCc3z6zSQ9oE2bDjPuPfh7ojQMfKffw-NFJt48QAzkEWMtYBT_Gq451vd_Bwm40-_0I-tWPeQwThsDwVTf6H8RdGWaNfNa7IuRhNL3r8deEnYsOHR7dwvamT-SrXcdCwX1fRcKQ-_ykgqdsAR_cr40eayF05sB53yXmJ5zxMWVjbdVSdriZG8yWHG6Q112gXu18U1E3qxmGxJjAp37k1NXYEXcEb093fviqYsAM-oE05GIfd6lAOsWjsdy8w-TN81N4OOIZehjgQBGzEy-kAtOua5PRICvoxHddtaK-2YHPtt8uKfRketXuZr6Ca4s2d4eofUTwNcdDK1jYUveJNxL4ns2kVPaMDcZlCmfrEhA6Rbq395f6nB4CnvLFV0_pYpem29Ott3K2pcyp_2Z6Z1KKno3yjL4Vqsuyag00ocOd4O8qFdDj3RvmouEwqbSdf2FVKPdKUSBmR2wd89Mf4PMI8TYs3du0I-5uNwfjywcQqcSa31E2I2_1P6qcqwtbZnCtv2GTFkIQJQu7pONtGjNmSZMlnrkbXW-0n61YgN2wf7P290pYMHYJIZAmrqmDvpl5laOiDTlKXN0-4UljNwAlo-rLD4IepL41d2gGbmwMYdp3gNrjOZI2Z8Fl589wnPpVT-fYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه نماز دوم بر پیکرهای مطهر خانواده امام شهید امت
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/667704" target="_blank">📅 06:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667703">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
فیلم کامل اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان توسط حضرت آیت‌الله جوادی آملی در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/667703" target="_blank">📅 06:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667702">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2472917a.mp4?token=m0BoC7jAoGFMsk4hXo9nwkxvYn7dEd8N7XkHwJutGIjJ4kmIUWG4wPflwRS-yf__qcGmobp4QEZ2VN9iRgIWmo6DOxgZp19g8z-jEWE1j7UKe26UNxRv4xubEfQNWT5f8vSNA1U6kP0TLvdkod1n5N75OAoOWqQnVdxY0F49o7z6vSxWjIVZzQRf8Mbetx2P4EvPhm2zcNViuVqZ0hEPHrudwPjDLdeVd8A2Otu1h2PDnY1Imz8GnVimteAiBzKM0MwZjz28yqexrtSnYZGZ88Vazl-sD3B1G3LSZIBgzar8pvjaKfn9_gZXXgENx-9ZGDoGEkhhlj89CpGvsDsJfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2472917a.mp4?token=m0BoC7jAoGFMsk4hXo9nwkxvYn7dEd8N7XkHwJutGIjJ4kmIUWG4wPflwRS-yf__qcGmobp4QEZ2VN9iRgIWmo6DOxgZp19g8z-jEWE1j7UKe26UNxRv4xubEfQNWT5f8vSNA1U6kP0TLvdkod1n5N75OAoOWqQnVdxY0F49o7z6vSxWjIVZzQRf8Mbetx2P4EvPhm2zcNViuVqZ0hEPHrudwPjDLdeVd8A2Otu1h2PDnY1Imz8GnVimteAiBzKM0MwZjz28yqexrtSnYZGZ88Vazl-sD3B1G3LSZIBgzar8pvjaKfn9_gZXXgENx-9ZGDoGEkhhlj89CpGvsDsJfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حضور پرشور مردم در نماز بر پیکرهای مطهر شهدا
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/667702" target="_blank">📅 06:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667701">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38904b92d0.mp4?token=J6bUez6inClc3WSchBJ7SIYdFnPhuSDwHDGBBXygGW7CJtre1qkQxJnQCjFxYzcmNfu5uqPY1nA1MJJ0aLBNZS-gcEbPJvZYH5T8_nry0q-RRkoFeomrYzDEolW6dja_zzyfycmFrYU-kfLjK_DyWQbECWz2ZhnCLhZFchgjkdw4lneg44y9ZXMdMTfdLTwHsV8BXOeZaedPUepGFikA4gPMY1yp0mpoKw8NLUpMe1dCAZGsFASI20PmvQhNsvEBPCtECu8EzGGZN4p3Qv8Uj5P6YktCj9ysoSJ36OZgVsSl2ss35pv7XY5ltNLzS19o2PZLRNPwbP6mjG_Guc0g9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38904b92d0.mp4?token=J6bUez6inClc3WSchBJ7SIYdFnPhuSDwHDGBBXygGW7CJtre1qkQxJnQCjFxYzcmNfu5uqPY1nA1MJJ0aLBNZS-gcEbPJvZYH5T8_nry0q-RRkoFeomrYzDEolW6dja_zzyfycmFrYU-kfLjK_DyWQbECWz2ZhnCLhZFchgjkdw4lneg44y9ZXMdMTfdLTwHsV8BXOeZaedPUepGFikA4gPMY1yp0mpoKw8NLUpMe1dCAZGsFASI20PmvQhNsvEBPCtECu8EzGGZN4p3Qv8Uj5P6YktCj9ysoSJ36OZgVsSl2ss35pv7XY5ltNLzS19o2PZLRNPwbP6mjG_Guc0g9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعاهای خاص و همراه با بغض آیت‌الله جوادی آملی هنگام نماز بر آقای شهید ایران
اللهم انه نزل مجاهدا موحدا
اللهم اللهم اللهم انه نزل عندک شهیدا
اللهم انه نزل عندک قتیلا للاسلام قتیلا لامه مسلما
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/667701" target="_blank">📅 06:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667700">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
آغاز اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان توسط حضرت آیت‌الله جوادی آملی در مسجد مقدس جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667700" target="_blank">📅 06:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667699">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNx4oGnoHtfOORhmBHYI0bzwXYYq-UTq138ax99HXXQxjO54AO_O35LChQm3zHXxWFace-4kvsKE0TkZqPeqPWZSFDr1A3buW0QA4Z0XEdhiO1sgbI0KOYvEXRLiRsJUUF-Mwc-HQ8o4Ups_6yChIOZLcXRcPEtvcVhmmPiEi1C_pEee-HDVG4j9EeNNiXnPCCV99EJddbJMKEGwthlIeuOGaiEq8nbpLEpT2ik7iZ0hFdNmzc2vi53mEXpuMsix_FOYCrGrgoLbHsZm9s2Tn8Cg6KOooy_2tGfCyfBQep59CUdq0_JERUqMcAKcW1XNEZjTsYAzLooxwrRYUG0wcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دخالت ترامپ هم مانع شکست آمریکا نشد
🔹
حالا جام‌جهانی بدون میزبانان پیش می‌رود؛ بلژیک با تحقیر آمریکا به دور بعد رفت
🔹
بلژیک ۴ - ۱ آمریکا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667699" target="_blank">📅 06:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667698">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cb281cce.mp4?token=E4uW4w8GbD0YJ-va-Aygx8VU4KXlyWMPB-w13bYrXAUnMateglg314vd_yTbIUjgYY-zfwcOUq6WQ-tnE1dYb6s47kcheMtarTDqwZJQpBtey1lB_Z42wgYuGI6Bnj5ThQ_xRcJrtzBLI5LfcWs8HzQ4yGfw3AeXJCGQNIlavolWda2tkspHPFifQ5mu4Gh8THZJ4ObaOi3W2SQuFLhyfPt44inCS9FrEqRXJxs5hgjAywJJaiQFlQm3pC821DUkbrJNJ1_abqFgyVAO-obW1ETCbah-WttD2Rtknu7cNbpnbqUI-LFW7HCdKpgi_DEXW_5RzLN48h44G5dRM4OwEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cb281cce.mp4?token=E4uW4w8GbD0YJ-va-Aygx8VU4KXlyWMPB-w13bYrXAUnMateglg314vd_yTbIUjgYY-zfwcOUq6WQ-tnE1dYb6s47kcheMtarTDqwZJQpBtey1lB_Z42wgYuGI6Bnj5ThQ_xRcJrtzBLI5LfcWs8HzQ4yGfw3AeXJCGQNIlavolWda2tkspHPFifQ5mu4Gh8THZJ4ObaOi3W2SQuFLhyfPt44inCS9FrEqRXJxs5hgjAywJJaiQFlQm3pC821DUkbrJNJ1_abqFgyVAO-obW1ETCbah-WttD2Rtknu7cNbpnbqUI-LFW7HCdKpgi_DEXW_5RzLN48h44G5dRM4OwEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ انتقال پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان به جایگاه اقامه نماز بر پیکر ایشان در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/667698" target="_blank">📅 06:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667697">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01056f55dd.mp4?token=mPf_0xDPf_YqVi3cah484hCTWQHHPhgenR2NKZs0cU8tUz3sHkTihyNkYlOjXyF2sQHaBErZcaRwD9x2Be79WYl1o9f9ciiLgrNRjR6SF95S8M6xhnmgW-o-RleTHbcGcWoEqZ0f406v5tW--2xlMVa3o8WlskKaUNrLYAp8KbyNNi4bIF3GqOT8J5WBD3gTB1Hc9bMr0L5mGq0x4AeK6WzGMaaUcD9dgsFVb33p8K-GhLLRDdHjhs02V-CsO9cPcbn-YIKvkag-nJl3VDQOkWwChUyVi98sVbSc99J_7lcIPTH-kBgO5PaaFBYo6YkEe1XSdluHfJE4h-78yrxclQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01056f55dd.mp4?token=mPf_0xDPf_YqVi3cah484hCTWQHHPhgenR2NKZs0cU8tUz3sHkTihyNkYlOjXyF2sQHaBErZcaRwD9x2Be79WYl1o9f9ciiLgrNRjR6SF95S8M6xhnmgW-o-RleTHbcGcWoEqZ0f406v5tW--2xlMVa3o8WlskKaUNrLYAp8KbyNNi4bIF3GqOT8J5WBD3gTB1Hc9bMr0L5mGq0x4AeK6WzGMaaUcD9dgsFVb33p8K-GhLLRDdHjhs02V-CsO9cPcbn-YIKvkag-nJl3VDQOkWwChUyVi98sVbSc99J_7lcIPTH-kBgO5PaaFBYo6YkEe1XSdluHfJE4h-78yrxclQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ تصاویری از پیکر مطهر «آقای شهید ایران» در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/667697" target="_blank">📅 06:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667696">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=J9VD6YZLJuk8741PftqvSHfvun1aQlCN7b0o5JnmsNDIabWYuB6YPwAqBpKvbD5VPOabffD2H1Le4vAGBI1Uxahb9c114szpn5QKlaVt2yJGxdLAwIvtFvmoT2DlbuRQVbVh0axgGy18kMIFhqRcz6sUXPcvWQHh_RK0FyR_rBA3RJhdE9aAm5ncQ4NuJ3sCjDNaGLkTICXGDSRWTi72P8_Qcy820vATPCG1NiNsCYVUBP8X_OaEjKuLuKTCBnPugFJT6T8hfA7gVlPPANWYTHsa7O-Idb6LHFkJvBPdAfdQIX8d_VhQbyGwpk-LlZHi-6NV4WvwMAj6uCvh9kK47w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=J9VD6YZLJuk8741PftqvSHfvun1aQlCN7b0o5JnmsNDIabWYuB6YPwAqBpKvbD5VPOabffD2H1Le4vAGBI1Uxahb9c114szpn5QKlaVt2yJGxdLAwIvtFvmoT2DlbuRQVbVh0axgGy18kMIFhqRcz6sUXPcvWQHh_RK0FyR_rBA3RJhdE9aAm5ncQ4NuJ3sCjDNaGLkTICXGDSRWTi72P8_Qcy820vATPCG1NiNsCYVUBP8X_OaEjKuLuKTCBnPugFJT6T8hfA7gVlPPANWYTHsa7O-Idb6LHFkJvBPdAfdQIX8d_VhQbyGwpk-LlZHi-6NV4WvwMAj6uCvh9kK47w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوسه پدر زهرای ۱۴ ماهه بر تابوت دختر شهیدش در مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667696" target="_blank">📅 06:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667695">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3103f71a0f.mp4?token=TBBIqnvjbt2s8XTyOYUzGIW6CJ9MBy_q9CoLuo0rFPN4Qp4MT8K2O6-Lwoweh6-Wv16cS_BlzY2WQxTX3w7rRT9jw50obhjoCjwy4jX2VB5T-ZzS_YwyBMLePfpzyqxFsCB9JCy9H3YmB5MlNY1cUye6pkzztqviT5MnI-JqzOYfY7Q65ZMg3Shza5VH4v16_ocZgOlK8DcFjfkWQ8UweoaWl8aEV-P1ymAHFiYmRNmXY6WyBSaRwL9S1VpeKXgoLpuo006jMUG8B7b-aMd7k2S9hWGH2nmJq3o1SjGcoIZwBWHzWpZbPzO8WWodAZKdT705ey_AotLiMO-ikxIO4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3103f71a0f.mp4?token=TBBIqnvjbt2s8XTyOYUzGIW6CJ9MBy_q9CoLuo0rFPN4Qp4MT8K2O6-Lwoweh6-Wv16cS_BlzY2WQxTX3w7rRT9jw50obhjoCjwy4jX2VB5T-ZzS_YwyBMLePfpzyqxFsCB9JCy9H3YmB5MlNY1cUye6pkzztqviT5MnI-JqzOYfY7Q65ZMg3Shza5VH4v16_ocZgOlK8DcFjfkWQ8UweoaWl8aEV-P1ymAHFiYmRNmXY6WyBSaRwL9S1VpeKXgoLpuo006jMUG8B7b-aMd7k2S9hWGH2nmJq3o1SjGcoIZwBWHzWpZbPzO8WWodAZKdT705ey_AotLiMO-ikxIO4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای هوایی از حضور خیل عظیم عزاداران در مسجد مقدس جمکران و خیابان‌های اطراف پیش از اقامه نماز بر پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/667695" target="_blank">📅 06:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667694">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtoxOnsHaOMvnZbh7GihJf0NMCCPgVEDvdAbn1G-eeRjdGS8w4uHnO5rZHUWTXkhqx4ymTFoe0eKk84eQIp5lLOZ-B--yc9EYkWm0dcjj2dNH51siUqBusEH0tXChEsfPISZ5SaEnqr8X_BSBBE6_wySSayciMBz13hyBVRD2QOCe5yGeEhkx3Sb3-5lOpmIdYygUpvGmHIQIrxAB_wxbfYgfwoYv7iFbAQE5_qYDoacko99m2pZZFle-A3OcxRQQ4WDJN6eS_N-4FH6ybZJcN7bzeAA42lT0v-uCA3Jnldp01190St8RBNqTPrqMTS2btXe7RIe8bMJWvp0IMP6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۶ تیر ماه
۲۲ محرم ‌۱۴۴۸
۷ جولای ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/667694" target="_blank">📅 06:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667693">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV5DoRVyfLQvZIB4d8Lt0nXz33vAeEpDZUk2fRTJKPzOAcuSyRGOFfHN6_U-HR3UVcLuLCWLi0IBxVhk_HykUINKEjbO2_UXC3UE9DYlvZ0ULxt-PhigWx7Gkza7zBh0uCUeZhGbO9UGIpAqdF3tjdiuJ1cnfLPgKXEcsjLIOazLNMgEcxSkFB082B0M2_-LAWHr7vOyOvH5-uutJTHxkuxPXrXDuTuIzRWIvawd68EVtoM-_25_zXfVcRqxc2dOcGthFWz7lFaqa4aZ6RLc-hAYBkBygamdk975PTbUR6hbAtmx5swnn-1zO3KHRX1r2vPSH0VMdbRO6UcwgK0d7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک عما
ن
سازمان عملیات دریایی انگلیس بامداد سه‌شنبه:
🔹
یک نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابه نامشخص قرار گرفته و دچار آتش‌سوزی شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/667693" target="_blank">📅 03:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667692">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107cdb1cba.mp4?token=cYONGKA4Dpv0KDY0R1b6R76zBfg3sck7AeWhGcYKE_Jnhxy-Z_CfiYlyRYqKWbF_5zEtLsTgvSAHWm3naQeEAO2vlWueOqS2DAArCgRjCzZ5MDo3UJuBzTyoJBlFhyWEE1i3pOo-iU6tIFklQTSfOd14RBOYWBcv3jnQiTjTlET42laTpZ9IfyBwTU6XzdKr42Xv1GGR_DYtqxM1lGEAulnTsSAoIxbwnMiOc9EH-V39ywe0LGk5FSF4yOOLtMuzaBfPKjVqI_kMF0atZzcprW4DzxYNuo7rzzKTtyn5z4ODvYKQmRTEnROBli3C_DZHhqOSR4jZHVn2rs2jBZSKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107cdb1cba.mp4?token=cYONGKA4Dpv0KDY0R1b6R76zBfg3sck7AeWhGcYKE_Jnhxy-Z_CfiYlyRYqKWbF_5zEtLsTgvSAHWm3naQeEAO2vlWueOqS2DAArCgRjCzZ5MDo3UJuBzTyoJBlFhyWEE1i3pOo-iU6tIFklQTSfOd14RBOYWBcv3jnQiTjTlET42laTpZ9IfyBwTU6XzdKr42Xv1GGR_DYtqxM1lGEAulnTsSAoIxbwnMiOc9EH-V39ywe0LGk5FSF4yOOLtMuzaBfPKjVqI_kMF0atZzcprW4DzxYNuo7rzzKTtyn5z4ODvYKQmRTEnROBli3C_DZHhqOSR4jZHVn2rs2jBZSKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از تشییع رهبری در جمکران؛ ظرفیت جمکران درحال تکمیل شدن است/ پناهیان در جمکران: مسئولان در خونخواهی رهبر شهید صریح‌تر سخن بگویند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/667692" target="_blank">📅 01:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667691">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2N0GMkTcMHi6JDxKqHiGivVl5BPvsuNDK1QOtzSX4fU6CH-PnTVuAXLhI-UT_9CF8aaC3OSj4rBx3_shzRyakyPuGJcLkJFHKOvEeir26iTJ_68zOpMTCC5x3Uf3z8VOkUquvcsO2wnKp9vAQTTcT4TacP4iUmPdTsmdxMlpAeZrX3jDmPIUvKVhHrRDhYaT5XnHmCTsDYqtGW8PsLErlcSp9eLLt82Oaq47ycjaso8tg6lJhyLfmmkwnMJmc5u4pN0wKtklNsNzqbeFhYWEG0TvbCw-cLqDXPrmBWwW636eShncLQFdvfUlYWBwqKzEGV3aYRWOpnrBR8Drn_jgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استانداری کربلا با عنوان خیر مقدم به اولین زائر اربعین امسال به پیشواز تشییع رهبر شهید انقلاب اسلامی رفت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/667691" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667690">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9965753a95.mp4?token=QrYmnUKHGpInZX3IgD8vzc2zHdKm2t7w9pleNYy6vvkc7VdPIKwk31RGdegtIRzKw__-X_MK6YdzG3VjIoXT1dNAq8vqBJecZEAiQt8OeKxq45rFrDV0v0CrzFpZQBgzpKMXB-wRPFd3CO0n-Zwop5oVsJA4hD5L4iwUveEpKqvCatFQUZVs5L5emsS2kFHrsB60NvaB26AMLdZt4PMoayvBUAx4Y3ysc6v5mtaz6QzeelTJV6jyj9eTA7_QXQIYQvEO6LF7l4UrB3O01-8WHEOoD9wr6-wTuwwTU_4O7gCiaUahk6AqhWq3gbml7F6vcq7UmewVYEh8F2A59AIeGXDwGwUi-gJPm7Os3MejzZGS5VUSPSzHPwka4EEcvyAWBh4gd_NqvpYNTAJTEmSJkmoYVgq_t5-AYJ8SYisuOHisN5p2-1bJINGSvgWfuGlumXZmzM1dIWTY2rYF0JPoyN0CyU9JThku1C8SGSmuOBtiT7me9HpO_VxHEJ8Le94VKvZKdjupQxBdlYyu4n7gmFjoZQvOHeGSr4yJjUGgai60VjeYGJH5HlgmQqMZgj0mjRgTeW_KWplHl2yX5Tes9VymyhVYGvqdN033TJdO_HgHJTP9soAWrt2o4i5n21d3inQyzP0Xn0-XsemoCKVfx--g_mg6TjYTwn_C7B7-ueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9965753a95.mp4?token=QrYmnUKHGpInZX3IgD8vzc2zHdKm2t7w9pleNYy6vvkc7VdPIKwk31RGdegtIRzKw__-X_MK6YdzG3VjIoXT1dNAq8vqBJecZEAiQt8OeKxq45rFrDV0v0CrzFpZQBgzpKMXB-wRPFd3CO0n-Zwop5oVsJA4hD5L4iwUveEpKqvCatFQUZVs5L5emsS2kFHrsB60NvaB26AMLdZt4PMoayvBUAx4Y3ysc6v5mtaz6QzeelTJV6jyj9eTA7_QXQIYQvEO6LF7l4UrB3O01-8WHEOoD9wr6-wTuwwTU_4O7gCiaUahk6AqhWq3gbml7F6vcq7UmewVYEh8F2A59AIeGXDwGwUi-gJPm7Os3MejzZGS5VUSPSzHPwka4EEcvyAWBh4gd_NqvpYNTAJTEmSJkmoYVgq_t5-AYJ8SYisuOHisN5p2-1bJINGSvgWfuGlumXZmzM1dIWTY2rYF0JPoyN0CyU9JThku1C8SGSmuOBtiT7me9HpO_VxHEJ8Le94VKvZKdjupQxBdlYyu4n7gmFjoZQvOHeGSr4yJjUGgai60VjeYGJH5HlgmQqMZgj0mjRgTeW_KWplHl2yX5Tes9VymyhVYGvqdN033TJdO_HgHJTP9soAWrt2o4i5n21d3inQyzP0Xn0-XsemoCKVfx--g_mg6TjYTwn_C7B7-ueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل کتائب سیدالشهدا: هر که آرزو داشته در مراسم تشییع امام حسین و علی ابن ابی‌طالب علیهماالسلام شرکت کند، امروز در مراسم تشییع امام خامنه‌ای شهید شرکت کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/667690" target="_blank">📅 01:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667684">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKE92tBV-LgRPsJrf1KIuXiTI5C6_VB1OhwQrAff7PacHSaYFOdUbr4YoupDxhaFiEnZqJ7SCV33ATJAPu-JVaw4yLubdhcU3c6yypUQqt8wnum4GjfrBOwbl5VI2CLe_u6sM4aj7ejJndsbuwGAsH-yoiU2SZZDvX-uDPs2nXzSGb59-Bxl3gJL8i_0uiI3cbgPyDqLfQUlpM_7Uj0IR4r1d0DN8LWYqtCaYhSztl9NeLWjF4OxIv7-EkMuD3aaPbqGsk12vei1IX0K9cJrx49ZeDSe3wFRf0sTTttm6VFSdnAJhIU8fTxy-L1hYAE-eAQUZ-x4oDbrF6eR2haXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-w70DxBKI-lCzEeldT_HC5G4COBH9fgKyakqsMSIStlppPJGZMVgGa2vT9-wePhKH0KTZhjEVlRUCAfK3ixvFQ7KnvkfNxXg5jRr_nUsZat4HcpQD3BojbFfKfNPJ77iM4agE1Mj4sGAMvymPzCC3nGgQWR7C0z0OPFDePTsZlsqBQ5eqRgGn5qCwBhln-3ga2eamEBooder6c0Kuh93dl3IPuK4Pd7dpoP6JE-hXr3l5w-m_iI19MarOdF1NSx41DzzGGO6a57gA3zXHSdCXtGxbF3gXNqW8X4vHp3fUPcCBg82KEtQ4Qhs9ieuv1HSTrmliTbUy-vXv8vD3l49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaH_x6lojIVaqXPVS3dhDorFxP-QNumsdnZFXnd4I-uTB7Z-v7gjv5l4V1g2npILJRw8YrMPEY4cRYbFDbadmyxt_XYSUk4627tXH8mOlj0P4G8PzIQBwAh8KaSYH9DgOqCC5pkVruQZ2P_NoS5iqjgg-VM4QhpVt529phJ57tu0blteIalkYsu46AKsVXmyyxr1y7175UVF_RCvOdloSkNR8TPzS0-9DsJRVkud5Bgq5_dcKnvtbc-yL9rdchAsxo6nfOQfPu6iYMCJ11p6jkxX6BHEAUkt6rmSuA65XezGRx9gONyLymodH5O8NsgXQM-hesGQgfdgnuBx5S1HYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhG7Z16AEkVDUB3AIsm8ofXQmqUEtVbcMtgvHOj2xCkZfcrGwTBuStM4Bfy0M_O9IVYXkUcABG05AcII58iLd7-lhfglGw9qQ3QOTfpi3PhpPYv7DHxR2-wicupuHyYGJswDooPZzbuxvAHqhIcjoRy2THEZ3Jqj_vCP0sI-_Ooscq10_1wAM37S0hPb5mlZmGf_YjuJRXfUzy667q2MRmjdw9XRsXSCVisjQt_UbCBKOamBlctDBEGwldfg-486177-LLIaxI_wlA3n1KRMAzajurBCNHiAa6nm79_DIvRSSgQpKvvA1psBQJEbpDMubhRbZzZg7rqpGJ63oXbSOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd788d10a.mp4?token=oslpbYMJZ83SKkME1gbEWVJm482kPtim0XNk_eAGlO2AfvLyeJzPyJjLNITtcW4gU0e1CTJyGqoMLpSGoH6qyfzt67Bat9aU4WASA34jKrgaFEN8f1EfCnck4ihNovauhvsCNkhqa0XnPhT_Wxqw25_V3ml9iOyH3_a4oFjbX9KfDQ6ZvJYqmbPP3kgCzLI7bT6U2i-vDqd3yEK449Vuad6SPzzpT1WORiQ1Q-hDWDL--H4SXDWe0nj9GWd_rytK1KHKlEyp5nS-NuRFP-4C1N2uTU4ha0_YC78vFYp5AQ12bgw68IZaK-b-gLcbxXgIkswsaOM6XEC6C1uX28NDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd788d10a.mp4?token=oslpbYMJZ83SKkME1gbEWVJm482kPtim0XNk_eAGlO2AfvLyeJzPyJjLNITtcW4gU0e1CTJyGqoMLpSGoH6qyfzt67Bat9aU4WASA34jKrgaFEN8f1EfCnck4ihNovauhvsCNkhqa0XnPhT_Wxqw25_V3ml9iOyH3_a4oFjbX9KfDQ6ZvJYqmbPP3kgCzLI7bT6U2i-vDqd3yEK449Vuad6SPzzpT1WORiQ1Q-hDWDL--H4SXDWe0nj9GWd_rytK1KHKlEyp5nS-NuRFP-4C1N2uTU4ha0_YC78vFYp5AQ12bgw68IZaK-b-gLcbxXgIkswsaOM6XEC6C1uX28NDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک گردباد قوی امروز شهر هوانگان، با جمعیت ۶ میلیون نفر، در مرکز چین را در بر گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/667684" target="_blank">📅 01:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667683">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjZxpE1o-UF-CO1Bsp3rux4zNEnh2z-EKDM7c2ixuQngE-wxB1gqLgCSKGm1n5Nr_Qn9pcVZ5_-FkZ_SeJN0qXYjuSsPLDcbPFsIJJvxXJdMgyqDamt9Me53w5cnL_2icTpi1-wSCvmqze7ENQiNSlp3UA5FMAOnSXR_WQycpDIGyjjgIdZ5hujiC9bh_otyiLNotqKk5wwWjdGmxyFemk1pJll6x2IWdaA2kc6foyU2XYLqrpHJQw-MLsX2mjK-Yo8k-SoFzcppz5wUqq9cy59GRXxS-iMhshQ8WwJ1oBCOq_EMBz8QGed-VQBqic2a9MgTa1GdJQGHekmrvk3lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
🔹
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/667683" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667682">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حمله توپخانه‌ای رژیم صهیونیستی به محله الزیتون در شرق غزه
🔹
منابع فلسطینی از حمله توپخانه‌ای رژیم صهیونیستی به خیابان صلاح الدین در محله الزیتون در شرق شهر غزه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/667682" target="_blank">📅 01:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667681">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
معاون صدر اعظم آلمان: جنگ ترامپ علیه ایران غیرمسئولانه بود
لارس کلینگ‌بیل:
🔹
جنگ غیرمسئولانه‌ی ترامپ علیه ایران، رشد اقتصادی مورد انتظار آلمان در سال جاری را به نصف کاهش داد.
🔹
این جنگ هزینه‌های مالی سنگینی را بر آلمان تحمیل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/667681" target="_blank">📅 01:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667680">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1cc9f3e9.mp4?token=L0EfWrjnQtTjyzww85e-B2_BO8hlKyYbBVz1-ja4gJDqvvnBQQWhAugb8IeqR3XK6taxOOwZTwc2QHGcqKHECsBoLtuglmhMz-Xz81vpOY_u_CYWP9BepWWYxvcnm5a0x7cGw4jqEIISJUba2SG1WY5E_GCE98-d_-LPDutcwr-0hELn72F0ROS1Ht6Df3AAdZsJhY5rH7s1knUSzAeDgNLYyicG4IRM8_91Cm8lFzZoBG2QQxdwOUdWQD70giN8LQc8Uqd1O4eryOpAhrH7O4ENnVAdo-PN0wpNDNmjoJbTq8rBz09JmXkrWId_dHzm_y1OtQ_J5lKa4OjXtPc4Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1cc9f3e9.mp4?token=L0EfWrjnQtTjyzww85e-B2_BO8hlKyYbBVz1-ja4gJDqvvnBQQWhAugb8IeqR3XK6taxOOwZTwc2QHGcqKHECsBoLtuglmhMz-Xz81vpOY_u_CYWP9BepWWYxvcnm5a0x7cGw4jqEIISJUba2SG1WY5E_GCE98-d_-LPDutcwr-0hELn72F0ROS1Ht6Df3AAdZsJhY5rH7s1knUSzAeDgNLYyicG4IRM8_91Cm8lFzZoBG2QQxdwOUdWQD70giN8LQc8Uqd1O4eryOpAhrH7O4ENnVAdo-PN0wpNDNmjoJbTq8rBz09JmXkrWId_dHzm_y1OtQ_J5lKa4OjXtPc4Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ نمای هوایی از مسجد مقدس جمکران؛ ساعاتی پیش از مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان  #بدرقه_یار #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/667680" target="_blank">📅 01:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667679">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏆
آخرین لحظات حضور کریستیانو رونالدو در جام‌جهانی با صدای عادل فردوسی‌پور
🔹
وقتی برنده، تیم دیگری است ولی دوربین روی افسانه، فوکوس می‌کشند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/667679" target="_blank">📅 01:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667678">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHZHmqgXQbywpsCwqOq2huwXWl31EtlGuyrVhMJhK8-ZjdkUy3EpcAUlBFxqq7XCaj9J9xwHfsZbeNnSzQisgzGKeTNZJVYgCJXW7tY7iLokJGuI_171fvCJcm_cOdxRBn4L_gxSaZtEzxEeRfNh49aSqTSzhJQW1yeK_244-tnxPJgPiKVwe4_JWvIhBxP2DB-pDLcxNPbmSB_npU6ZWk-5wQk_yrHoinoVqGURfZWEAgjqPYLbjJqgMEJmHQvpvYmfyccEzGFLFLtizLq-DuCUFzx4IV_crTwa-siFR0DqaewVplmYLoS8P-_6f5W-spGkXtm8-8GOwkgCAKZzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موضع طلبکارانه آلمان درباره مین‌زدایی در تنگه هرمز
🔹
وزیر امور خارجه آلمان امروز دوشنبه مدعی شده که ایران بایستی در نهایت هزینه عملیات‌های بین‌المللی برای پاکسازی مین‌ها در تنگه هرمز را تقبل کند.
🔹
رئیس دستگاه دیپلماسی آلمان، «یوهان وادِفو» در مصاحبه‌ای…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/667678" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667677">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efbe8b7cc.mp4?token=QVfEHUHIm1gL7OP33bDJaYJ96n3bYMbJ7W8b82T1nP2K0U6zHWsp9cG7Ck0RqDk2fABfUdsUMof6IbNQJ-_fz2ocp558XEnFRmA7sxJBcPAurE2y4CAyGHR3SP4kohiL_xUCifJxJmmN2baqq0oy63tI1kKLd01mTQAyKkssFe5D6PHXTblFzuizMbq8-bkj6pjCPkGKO2iyFc2D7hMRGZRM8XKWUPy-UOybhW1DjZSKwG_RWEd4K1I4RbDRPPCP4rQuUkwWIX-D9yaGmLeoTSn_qMdSfT9IaVGEHCOXslz_aUjwMN4xQstuYdxX1DLvvZgiaV99avNJinRNADiITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efbe8b7cc.mp4?token=QVfEHUHIm1gL7OP33bDJaYJ96n3bYMbJ7W8b82T1nP2K0U6zHWsp9cG7Ck0RqDk2fABfUdsUMof6IbNQJ-_fz2ocp558XEnFRmA7sxJBcPAurE2y4CAyGHR3SP4kohiL_xUCifJxJmmN2baqq0oy63tI1kKLd01mTQAyKkssFe5D6PHXTblFzuizMbq8-bkj6pjCPkGKO2iyFc2D7hMRGZRM8XKWUPy-UOybhW1DjZSKwG_RWEd4K1I4RbDRPPCP4rQuUkwWIX-D9yaGmLeoTSn_qMdSfT9IaVGEHCOXslz_aUjwMN4xQstuYdxX1DLvvZgiaV99avNJinRNADiITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم‌های سرخ انتقام یالثارات الحسین در مسجد مقدس جمکران  #خونخواهی  ‏‌ #تقاص_خواهید_داد ‏‌ #WillPayThePrice ⁩
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/667677" target="_blank">📅 00:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667676">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxdkd4TkmL8MNwrPox1YKE1i_qGLxv5bN9RCsJxiXPVOd2xCw0QxukXrEvabZw5vG3es9HUn-ewKupnoWurAhpVpV4qdNfdgbDVCAl3-JmpRbhJGJnSTvGrcGbDKf_adbKjo4QXcSCqYsZElpU0dBXC-logj3Qq500W2edgWT6nKrho6sbg76sxvbd9KxE3TZvLyZNXEk_i_N8l7EzeheAiRZMgEzRxgMMlIq27OthK3YQjER0wt5MdEwGSL0wbp7ARWqklU2mTcsDCSOCOHm6vG8hsvZ6708CibF5gaqSUU4qJ3zdm0sQS-V5wKyz0_xlz4uFC8tjilbrjoXFQuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت بیت‌کوین به کانال ۶۴ هزار دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/667676" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667675">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1611978093.mp4?token=QM4wCerLySJasGAqsygNw5_foYKsT1FsL5D3Dv7Dj7vTH6zsM3Nsiv-6telrBFj7QnEjcxGsmvRcPcrMbZKqnTi27WeHQJU8LX-xP_q2yPyJ0cCBYG-sfgb-ab6bRxvZZ0GrHlW-RKwaxOhX6ahSit7AUCA9VH-Rzu4Rq213hssi9qbfZeUB0ANwvXmmVGXi9sl0h3WNhaZRPHBHimj_XJfRA0BgQDa-hWdrHBHVTPZW9lWwMBQi1-Abm8Iw9ogqZNgWjP0-t3BTujRna5a2LfrMJyZB-r7RJzYlkq3wxcVofFs4PmX_MOs4AwcXW8NMhh2u4Bori5-HTorrRpZHcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1611978093.mp4?token=QM4wCerLySJasGAqsygNw5_foYKsT1FsL5D3Dv7Dj7vTH6zsM3Nsiv-6telrBFj7QnEjcxGsmvRcPcrMbZKqnTi27WeHQJU8LX-xP_q2yPyJ0cCBYG-sfgb-ab6bRxvZZ0GrHlW-RKwaxOhX6ahSit7AUCA9VH-Rzu4Rq213hssi9qbfZeUB0ANwvXmmVGXi9sl0h3WNhaZRPHBHimj_XJfRA0BgQDa-hWdrHBHVTPZW9lWwMBQi1-Abm8Iw9ogqZNgWjP0-t3BTujRna5a2LfrMJyZB-r7RJzYlkq3wxcVofFs4PmX_MOs4AwcXW8NMhh2u4Bori5-HTorrRpZHcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسجد مقدس جمکران در آستانۀ تکمیل ظرفیت
🔹
خیل عاشقان رهبر شهید انقلاب خود را برای شرکت در مراسم تشییع به مسجد جمکران رساندند و علی‌رغم اینکه هنوز ساعت‌ها تا شروع مراسم تشییع باقی مانده است، صحن این مکان مقدس مملو از جمعیت است. #بدرقه_یار #اخبار_قم در فضای…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/667675" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667672">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYc_MNmLJjiv-cvYs18XOtzp58Ev0oZN0xH_f2FH3R5GpgOd9uSDksOhMMVHNJnut3nxkwIZxEpOasjCRgkSGxI0n3NeqeOz4aLhNL8PtgmjYcLgJ3haQ5iQ1a_H980K5fNq2hHkwAvSVJIdA-4EQvDCfP6vUhlIRwjc8jD3EoStiJzOv7QXY4yH7p3u_m80mVjLr_HbYRZKaFr--74-YRJV0zmtb1P9JCSk_ofuE9RpcJgWG3FNWuAf4gRUz6HHLrstAv_QTny8iSKXPNiJQnQ20YXhm3UKmmcdkO8JIiii0Y6kPPDe56nXxPu9XbieGIcKYsUWKmlF0FcpKs_AQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INo3qp485q_2P6Im5RV_M4SGu9GU9K1gKMrJcJC1-scjHxZZ0F1X5WmlZ2Xq_mx-3iuw940EuDEskqcycRs7B9BFRS75dIKGx_JNd8H8sWHsNkYrLvuzVDl2OKc1XbdIMSFzin_QnKRBlIhzKTxCeM_9jQNlIb2BZTu4-U0vN48AXlwpcFxLXcKxgEZQ1vwXt3w_9gLaZMtI0W4MfVamFiSNeffE1Lr2d8Qf92ydxlZTXER346vQD27MGMDjJC7ycS6d9X7t93tE7kAhFpqbySe7eGIxC0x8R6jbuZPYrmIqjJZhnQ4Nykn1BZKmf6Qzmy_sGxoz9tZyZPDRzJhVNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e8334a47.mp4?token=T3BP19pzGKOHBeWoFKzSP6jWEsaSrNkTIVWSgJnwmkRITHxgLNf9ckgiqSqc9EuqAHY0V_UKLTsbU8f26SZjC5RX4UqPL1POvOywnS9Qna4CxAcw5zx1mIx3R28Qi6o6yglWavQ_ziMi5HnYGJPPF7p-QXp0thWqSxtNOrryw0bIXHWStJd8wJLc9rlbrQY6vfsaBUO3CrRYsdNSl-jcy2AiLU_iDaBdmAKTgEc37-0eDXLjajSEJWrg-fhnt58lo7hjH40T0VygvRW8FTudkpXTrPFVs42trgvgzKGSCdkJG0OhBLJy194I0wIcVsX-bOcFJtfK38rI6-8g_lMjFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e8334a47.mp4?token=T3BP19pzGKOHBeWoFKzSP6jWEsaSrNkTIVWSgJnwmkRITHxgLNf9ckgiqSqc9EuqAHY0V_UKLTsbU8f26SZjC5RX4UqPL1POvOywnS9Qna4CxAcw5zx1mIx3R28Qi6o6yglWavQ_ziMi5HnYGJPPF7p-QXp0thWqSxtNOrryw0bIXHWStJd8wJLc9rlbrQY6vfsaBUO3CrRYsdNSl-jcy2AiLU_iDaBdmAKTgEc37-0eDXLjajSEJWrg-fhnt58lo7hjH40T0VygvRW8FTudkpXTrPFVs42trgvgzKGSCdkJG0OhBLJy194I0wIcVsX-bOcFJtfK38rI6-8g_lMjFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رونالدو پس از حذف در جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/667672" target="_blank">📅 00:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667671">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4AXvbTF2gAQ358i-biL_vuY5eKuJD_bWZe6s_ZKqYnNTC44TY8nFna1UFIYCss68-ISRPRhXKHyLwkakpkdXQZ9J31DMRQpFKekdtzfRnutX0u5Wz86YSICXotGhBeGEkCth8pBop1Oj_JRs-QyyEB_hSA0JhngaF_PHwdMEHtKFbfU51FQghaciNRf9r3y0axUY00L0VOnC-uHW1N3eB9weSrCl1I3iqRLov2w9uWvlTYhxY272E_LRj-h6BjmkZUNmdf8aTTT1wfEvT_hVjAVen4IGuQggHmR8NiQ2wmY0ORhGOk0ZUYiZjOYyGjUD2_okRHtCHKunh3jBZSr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عصبانیت رونالدو پس از گل مرینو  #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/667671" target="_blank">📅 00:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667670">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8180ac8e2.mp4?token=B8XNBPi5j8R1nHk9p9fkqxLbrGXe_8gHg0RErzKxd6WilY-7si80AYrOOmAufoNf60HkG1cNeVovpIpwkJ3NoG2T5QokXkR_44w5FpAsvptuoMWOFJHb9YI8AAz85xtheO0iGxC6kScwlGFEdJAxHvonBfEpX0BCmz9ds0pfmaa9MtE-1mxhOw2Fdh83akBAmtV0dUd0b027Wi80pIki1vK0wyYNGnHSwBr9FprRQ_6T2Nw8nlgMinG0QdT1fTAs-KVva85-4NPq0RIvpdyE4EOBV-1tacu0CXuZer-LMsVsn9Vkp60jh4Y8FtIA-CLwI4uuSSyCEHmSe2dtVGuRXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8180ac8e2.mp4?token=B8XNBPi5j8R1nHk9p9fkqxLbrGXe_8gHg0RErzKxd6WilY-7si80AYrOOmAufoNf60HkG1cNeVovpIpwkJ3NoG2T5QokXkR_44w5FpAsvptuoMWOFJHb9YI8AAz85xtheO0iGxC6kScwlGFEdJAxHvonBfEpX0BCmz9ds0pfmaa9MtE-1mxhOw2Fdh83akBAmtV0dUd0b027Wi80pIki1vK0wyYNGnHSwBr9FprRQ_6T2Nw8nlgMinG0QdT1fTAs-KVva85-4NPq0RIvpdyE4EOBV-1tacu0CXuZer-LMsVsn9Vkp60jh4Y8FtIA-CLwI4uuSSyCEHmSe2dtVGuRXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسجد مقدس جمکران در آستانۀ تکمیل ظرفیت
🔹
خیل عاشقان رهبر شهید انقلاب خود را برای شرکت در مراسم تشییع به مسجد جمکران رساندند و علی‌رغم اینکه هنوز ساعت‌ها تا شروع مراسم تشییع باقی مانده است، صحن این مکان مقدس مملو از جمعیت است.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/667670" target="_blank">📅 00:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667669">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWVYMhuJLPcsDyoHagVYACmWp2h6tmKLtMtDtLNRAfXUA5x-QyON6spNWW6BnKVV2lsg3aViOFog3T9u1piriZjOEOJjN1qrsdf0spsG9q_8gZELid_k6dfkcBvWf0NB9gfHM246YSX7-4kv2N9023KVZhKP5b-Ijux6xkZS3j1LRX-Xv4wS713I8FW5aaTyZsFyDhxaL9StD572jQP1CSgKVQb8-4nsK5i-D64lSH-Rag7po3wOxaLNmJETZRJQSb_T2WHnSoID7XDB7-G34loId-s9kxLK7viegFPiycGqSDfrWGZAaFYkiqjymBzQuKS3dkO1dlSj3E4M9NDg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل اول اسپانیا به پرتغال توسط مرینو ۱+۹۰
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا    #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/667669" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667668">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnFIcz2QGS-utAuu9qqAivQjNU40ranvtHN7pBhTbjewNTno1qlMDZ3ITUa9s6lyxg4hzCl6vuAPBYkB6NPFLCJ-mFsDbAJ4agbmsSSSJ5Svd8Cb_ezrmX-4nBlcW3xfL9w1hQ18MCkT4AQ_QLacsgd8xslxvDrUB6SrRTItNoWzS83G4AAT9FK4Vzr-RhRnJrU6Con8Cp3jMpMJHcnmj86v0gzu40WGTzIiJAbltjv4OZv0Vu06-wkzcHnf95VlBD3tB5g635QoDVsW8clWiKCeEqH91uD7ir50iswAFzu5FDhq2PiaXIX4WMB7YeS1m352aBuouRT7SK9R2IxUNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عصبانیت رونالدو پس از گل مرینو
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/667668" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667667">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722eb4a2b7.mp4?token=NU7W5vCASRbPI3rg_vg97GronoQbcX_mvK33O24bSwdx9tTC0Syflbs7saLcSBaA7vTLPXjI740HDwgd6dn6rok_SZpGsh_ifS5BWe20CTQL0mhvSxICugKnbiDbdXktew-KGe0W5qTP4jD_YYOzJVXhJTYqVTRa8vWKqyMbFF4ngrusF8fL_RQN2CTWnQb-a_uKHSf6gIENwgRMfB2g3sdduQwwiZf6R2RbCfL3Lfa_tY_HFjQSbzrJqp-1GsGDmoPac2Q-OiOhBi2l90T7aCnRYD4zEpOHEMewo8XRV4gtr-JrZ5PvZ5NIge-bTbFzyBSGgbmiBMyTipFguz40Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722eb4a2b7.mp4?token=NU7W5vCASRbPI3rg_vg97GronoQbcX_mvK33O24bSwdx9tTC0Syflbs7saLcSBaA7vTLPXjI740HDwgd6dn6rok_SZpGsh_ifS5BWe20CTQL0mhvSxICugKnbiDbdXktew-KGe0W5qTP4jD_YYOzJVXhJTYqVTRa8vWKqyMbFF4ngrusF8fL_RQN2CTWnQb-a_uKHSf6gIENwgRMfB2g3sdduQwwiZf6R2RbCfL3Lfa_tY_HFjQSbzrJqp-1GsGDmoPac2Q-OiOhBi2l90T7aCnRYD4zEpOHEMewo8XRV4gtr-JrZ5PvZ5NIge-bTbFzyBSGgbmiBMyTipFguz40Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به پرتغال توسط مرینو ۱+۹۰
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/667667" target="_blank">📅 00:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667665">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmEGg_nJN3gFYdEYi5oIS_Yw829ZFjB2GZzcXDglGdLzAxTEZiRdFGLpf7Y-k7r-wfMy180RopzassVBe-OBSsdf-HjdXHtUESbhcO6QzUVbwEGyvJ59qfSdRsX0oMRdmSf_MS8G5vstYAQ6SjgiEv8BtJGcMq0fMpiEdJwsRrNFe1KHc3XwqO3f4_bK26aRMKomby1fD9nezBFJmnCtK_371KTjWPt_3ZZeeGXuALgsbB2E9GvR5pWF6gtiQZr5Mc-N_eZ31EyaMGEx3-as21P8BtEpBV6df1ufjxsSfV1B5s9JDcgmwhpfSCi5lC3k9XN0wc0cUnZ1XktPNcX76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قصاص جنایتکاران نزدیک است
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/667665" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667664">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدرگاه فرهنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b651a243a.mp4?token=bTcS14z5rw5RsvIITwoYSav9JxzroysXz-LG8z-7_JNGyFdU3d2uWA7asd5RDsjxiEOvdAC_JoqVyVOj2j8oYAoVZ1gAW2WemfOvzZjivzo67yJMIvK9a3VR1prJ8CMiIGUQ5OzJ7rJmK9v16PcALHGqd3FWyP1hodaID3i8arTJ3eFjKD1FosEroZlATw2lROanqgw9FvVnJUfdMaMyzr93XDVZg2KKy_JA-GW8f05NvEL1FAjePfeoh_Em1QAh6HdbtWZ8fBLzg7WymRHCvPR1eJHcjdlxocosKzGYYISlGBypM83Ktty3NCt8nuhKosmkSlVy4p-JupMzE3DvziXDL0hsOgOlgeObhTtcIpcJvgrgYSuSEdIRZNsvUqC6jB8a1QnFHaIp-RHCmb86z3pW0NSSJyb-qYmYbN7TMlDa3M2OxOtFr88WemOSnp3qDoL9UWGjX7gFNORH4BbKTcB2lsIaKXbolHjQnnzgTpqMW0Ms0cKZR-ooZbQJ2IOOaQqJnbPFj_5OXWDTisrTn-wudpGW7SN8lJAtkSHYH7HpTds3w4Q-kfny6jPde_Ryr6OeY-JJUlK03sIBiVV9Kjm5LpFzK3JRlFPy1J8BS9gxeScpKIh-ZMC_e9_yEPrAFdIESMRkAsRcFuP-jVFcllnqPsAkou1WcebzViYz_2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b651a243a.mp4?token=bTcS14z5rw5RsvIITwoYSav9JxzroysXz-LG8z-7_JNGyFdU3d2uWA7asd5RDsjxiEOvdAC_JoqVyVOj2j8oYAoVZ1gAW2WemfOvzZjivzo67yJMIvK9a3VR1prJ8CMiIGUQ5OzJ7rJmK9v16PcALHGqd3FWyP1hodaID3i8arTJ3eFjKD1FosEroZlATw2lROanqgw9FvVnJUfdMaMyzr93XDVZg2KKy_JA-GW8f05NvEL1FAjePfeoh_Em1QAh6HdbtWZ8fBLzg7WymRHCvPR1eJHcjdlxocosKzGYYISlGBypM83Ktty3NCt8nuhKosmkSlVy4p-JupMzE3DvziXDL0hsOgOlgeObhTtcIpcJvgrgYSuSEdIRZNsvUqC6jB8a1QnFHaIp-RHCmb86z3pW0NSSJyb-qYmYbN7TMlDa3M2OxOtFr88WemOSnp3qDoL9UWGjX7gFNORH4BbKTcB2lsIaKXbolHjQnnzgTpqMW0Ms0cKZR-ooZbQJ2IOOaQqJnbPFj_5OXWDTisrTn-wudpGW7SN8lJAtkSHYH7HpTds3w4Q-kfny6jPde_Ryr6OeY-JJUlK03sIBiVV9Kjm5LpFzK3JRlFPy1J8BS9gxeScpKIh-ZMC_e9_yEPrAFdIESMRkAsRcFuP-jVFcllnqPsAkou1WcebzViYz_2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طنین اذان در لحظه ورود؛ گویی آسمان هم به استقبال رهبر شهید آمده بود
🏴
آخرین ورود به میدان آزادی
#باید_برخاست
#یالثارات_الحسین
@dargah_farhang</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/667664" target="_blank">📅 00:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667663">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
آکسیوس: یک تماس تلفنی، نتانیاهو از ترامپ خواست که رئیس‌جمهور اردوغان را «مهار» کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/667663" target="_blank">📅 00:12 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
