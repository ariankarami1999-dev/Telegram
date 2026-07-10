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
<img src="https://cdn4.telesco.pe/file/Uey9xI1TvSn_7vJSN913eJJ37MSYbhL6W4N8-K6MJAGj0dyzsCs_Z6YgSEJvslBSaJFnw-QJg9x-ayAWWR-hwsPnz_wR2-r_dc-5OgJdR6-DjygIUUu1hTXCj4NsiXmXU6Eporc059gLDmOSKVYAOWDNgx2EUJqgS_dH9nF9e2p02eUXxWTDMpOl3qSd52OI9HsUoSzB6Fev9NZRba8ugLw0wsx9ZPzqkMQyNMdXvAz8B7GnunTTZ7LGwj3SFftjfRQh9Ime4SDTvIz_rNp8ZQ0CrmaM8NPB4LFYkwTc1kjb7klZ5TzOjy8XkkRuCPKcX6FAfMNgj-iXRERpMZHTEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-669444">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qG4eHxXssG58zxK0JB6k3Qe9IId2HWVCQcC6g50_hKPFL7ulqw8ptKMUiuyI-Fh22gu0_rm_sMh_HqCQTR4VQAUON3lQ0oIj2hV1mwollGTw7S0Al50twLhFIgPZ-ZbL6SoDwJvO0fs11oRY6eRW63i2jmmKdHzs5tn-MUlpuI2BnKTydem3KOS9CgOUFqB1kF64xuxQq7C2tqDNb2DTLF1bpYbZT1SMGS36YJOwXsoySwNAzWeZ82lOC4WxFr2HiiTgkIbaCDnts0jo2qGMjlQeHg3qidHHFfcakQL1FFVP9T9QK3RtdjeA6L6f7aWjnrE1jaNa6P9zoSeogTI2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خارجه، رئیس مجلس و شماری از علمای اندونزی برای ادای احترام به رهبر شهید انقلاب وارد مشهد شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/akhbarefori/669444" target="_blank">📅 13:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669437">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKL3N5y0glfbB3pYPDDI9mJfvAMfhrcvetyAeGJrCWVl0iWB2YbZRiJYlH4WFB1ZUaUCyzYIqKQJ14wWtRH1rHhrweFW9t3PtkzMh2G4Gx2qr07kr_V5nwyxQ_8dfwtEJnSju-UkCOt67mH9fNXIifVSLh7fLfSChf0BC8AQdSu_cUp3rsOJsing5XsjUYtqrP1L6JYCfc4KEf1ktri31eEdtEqIj1Y07uYM1sh53v7pjmBM_alUqD3IejfKFL1Mqh7m11RQnjiJfXRXICJhDlJkunUNJ-sl55d1CCT60fdlfLPSURZo_dkz-odnrFA1WZow9iIpvyx34VxCkGzbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpUOQWvucjToy0gG-qVax3rOixm2Djii34pCSyUV1CNj--nertPb_HTEdAOQqwm505s6KJQT7pkX8IMUty7fTDL9SWjICrgy34bIsvajk09FoA05cyWhlSGJ5TBU2ABkKd6BJScA80gFQi9dF0ks0wCnOYqiEsL4xqRyrf4CH0nFqJ3mtIUIvNC7mAX7lqoiADKNbVhuoz0uQ9SSJBdw-voNPUpeXsD2IZBDcVeyWAodqYW35EDk4uTRc3_OVc6r5Rw6XQb1Glq5r9JNXMMLOurf6s0CwImV3PwP4tOXukpBH2LYf9KGYSd8O2mObbiOZjC2XXqbhk0cdazT4Ufqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRmVzCBPR1kB8UOqK22VfPcbsEtjzs3CiAUwwHRphb4ERUYIQoOwmWbtxxlHBOmyt7Q3Ku7CHJv5uuhGyyz_x34eKGxVTuHtM8mApvzCx-6xemzeDDe25l1wmGtb3Gv_oZPhng0pOaMU4_mNXqKMY-HZFxjclMXAvc7RGCf1baRCrflRGM9FBTSbS0COufoOnUx6JgyEOPVl9aGJALx8tCu7Thhsh_pLchFOkqVWLx_b8QN7OWj7GVxWW5DbyqWX2431t50uWRabtVhag7lK63aD3S87YM2fZ6lc3Q-hUwd2XSsvf14cgLSKlojitJrh-O-nb44eHEGhMSW10X6_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbkk-oJNdYqfR9I9B5QE-AQ6Mn-wV1WTx-V9MKf2LTDMndjkMQy2d6uuFVVctYREcdSYfUWZ65eHWP9yND86M5MLZvQbtFa2JiIDFkavOTVrVOtBtD1M1noKdKNjRcGsw0GY7jqii1eRJhQKgGtPJKGaTrPSzBxprZr_jNMyXKkl8_mxxX3lQ-Lo6o4zArkCi3hjkY_RZx5AWUPBJgdpcQKu38i46tvFpThsvy6MXuz2BqRDQ-JjGMb-tGFS18tnL-ndGA9wJRZhavoIFOxAWKceauGNNDt4KWx6P6kjlmjcHVhgEf5Y2DirUXJDjSigzw_Dw0vlu5XmKK9tFc5Myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGJIoxudl48t8DUtn6u9AEC3blDoF0631cUBRe6snPXoEzRFLUkVXk8s0T6LfkVqQBvIqZoMMNJ-HQQtC00mdkw0aM_UKORm6p1v8QEA4hn8s0Cl0dTczsOldCnkaWafaShzX7yCIwIpz2K3GNlTxq48WVR8amPhiQNGo29ZVgNrQj0M5V_hYESCqYRrTctI7hsjpkBW24BijhHUm7j63jgu_-sc4UzXguSH2A-LD9I7UrwgAmxUooY-gW5CIoIBULn_FTsMqYwIEHTwbvSff8vROqcVLKyKyn3t4zR8eWgPvWCSkJHmrsIF2M7Dc160UPTqkrXEzjUaPDt-4BtD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1xcmdoVFguVBsSoshOJV-fPuAkMgt3kzBtwKWbrlxlSpCP1lM8cz7dAthIJ4MQwcjmJXMufrryoa8Fi0y7ZqYHGkn1L9Oo28vqcHbv_wpm6x18bEJ5xShwH_gBl6XPdfQkXKoJidJyzG6jkhyagNED0NkWhAjPSkv45UOTSZx6e0dRFiMc4cfeIx6-PpRmXcHbb8VE2sVp_MlIqaevxZijPYwszvZBUuDWxjNDbIbsWm-vikP_TiXet01VS8kRfxrY-x-5pkPNFFNyloB5WUZJBnaVSulebKk62wQa4tm4_ZADKABRNva6qXr5ekhqbZ749wZprGzCqNDbZJwIfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8kHB5n6ODQax8hT0UCPG2XQG1W3nNurxjo8ScRfcS03Mb6_GN9dMqKfeAgtfAtrEK5G4ChQ342TbczjmBxMz3dq6gFoAL5Ucqf8lfM3ewN7Fz0xQUyFjq-HOCXeLpv69BkxJyWu2ysFkE6_8AdxS6v6y7JQfpGvjqiWavb13dtFI64HFuvD4BiILXD6qw645pDE2CzY98eRiyjrpA_oTYrkcnVFxKfmldr_1uY1If_obcuR7FDz8-UF_p_Ei77tKC0iU4olCd7zX3hbb7Dil7G7BDl3XhS4A0Y7aRINkHwKynN7YBeC5EPULG1hPEnsj0fTLSM71-0NAV1CIhmbEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دسر‌های ساده که می‌تونی با بیسکویت اماده‌شون کنی
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/akhbarefori/669437" target="_blank">📅 13:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669436">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsY-0AcBXufeGJvAFe6Grw6dY7_cfTALNXEH8WjiowH_cofALMWEeV9i_hqajx78Kckg2T8On-omTMqxGj37IC-e9wMBMxfQ2_sbgJ8W6Hc56snAeHRrAgBHJ8BAOnMsZXh4KE2adRk051pGcKCJzwwfvcKlWnvmHhgqU85cDGxEgWFxxdwgiHhv9wTGLTK_T8Ot3l6NJCsaZiJYBogv1B-oCtaYdbl_m7ZAgTB3NNqU3mb6fMxK-Eo4yZNckB-PTDV13OZb2ALX5k31ogZgtHy-1X1P4pUz_225HFFvkM4Xs87DwOUecueJFQn2GiZs0SN1fv61_EUpZP3Fo6U7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ شهر ایران در میان ۱۵ شهر گرم جهان؛ بندر دیر گرم‌ترین شهر دنیا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/669436" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669435">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f13f441b0.mp4?token=SdtdeUlZtNPxvjE_tbmfWCnqE_JA_r2d5mnq4kTBF5q7n3U4iH4y1wZWtoML6ZM_8baoGzisy46u10w5O84Qnz264LFFTpAYLqgsJ-uZKGqs_YJBMdbwH699uaDRWHr_zazONQ0FFhR0QE7p4TwM0Olvuywrd2xx2Cs52Mgnxlp-HfR9MqDQI-KK2XPBFsCQZyhhK3eiYAcVW3gS6s8tfL0nAvLOyEd0mKERqlIHoS_0NgzEFF91PeClOVFuEKk9dBTV_OJn5pQ20EwGtsuFvBX--gY8PLaSpJc3qhFDsGiyLG2wgky9TZW6GVXfyYORAc7SGwdBG4hG5mAAC67YgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f13f441b0.mp4?token=SdtdeUlZtNPxvjE_tbmfWCnqE_JA_r2d5mnq4kTBF5q7n3U4iH4y1wZWtoML6ZM_8baoGzisy46u10w5O84Qnz264LFFTpAYLqgsJ-uZKGqs_YJBMdbwH699uaDRWHr_zazONQ0FFhR0QE7p4TwM0Olvuywrd2xx2Cs52Mgnxlp-HfR9MqDQI-KK2XPBFsCQZyhhK3eiYAcVW3gS6s8tfL0nAvLOyEd0mKERqlIHoS_0NgzEFF91PeClOVFuEKk9dBTV_OJn5pQ20EwGtsuFvBX--gY8PLaSpJc3qhFDsGiyLG2wgky9TZW6GVXfyYORAc7SGwdBG4hG5mAAC67YgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای این دقایق روضه منوره و حرم مطهر امام رضا(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/669435" target="_blank">📅 13:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669434">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3IlExLM0sAf86H0qQnO3bGlig919-wJn0oF3cLhh2lexZUXigAWl8z_w-sLTlPcGmyn_CCVLY3ru7CnrYjnLC1Upq7uiZqoLXfCw9lXDicLlmSZXg3KAJ9DmFHlX27ijBIqrNetoXnJuIZZnrVbNV1h8I4AFN__3o-6jeLRIdXODx_PwZFVh7cypkGOgIVGu6z0Iuce8leEoGhn3lPHrk7f_O3gSmQClzqrlTZ-_b1HEUQweVIWjcZVRD_vM3ko3Mlrvv_QeTtdDHQ5TzGTGVxPLyETMhlchpaiGkP4O9V2itOg8yVzHnCR5PyuLB5QzRN-4G2b_IVqtRLpkDo4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی مسی در جام جهانی
🔹
مسی در ۱۹ بازی نخست خود در جام جهانی ۶ گل به ثمر رساند و بدون عنوان قهرمانی ماند.
🔹
اما در ۱۱ بازی اخیر، با ثبت ۱۵ گل، ضمن کسب قهرمانی جهان، به برترین گلزن تاریخ این رقابت‌ها بدل شد.
🔹
او اکنون تنها دو بازی تا رسیدن به سومین فینال فاصله دارد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/669434" target="_blank">📅 13:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669433">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fd9b7e8d.mp4?token=G4Q2BpWioKFKnFidY-5FUPR3CWMNSzvm1TfHGAXc4bKG-z-3LbM__gHDDBdfp1048DLyZWCCCIiLkXKp53vnsPb5qa0Fb1Pdz_CmtOg08RlESbuKGGUhSYx6HB5O9p1UxnVklCeeDxX_VHkaQLNEbF0f0up3wWlmBhregspB69TTmyDYQE0UwfkWaBgwJUiEKHj9pDeoC-ivOs_4_4pe14had_SuDD1ksKiF8QxrA_Qy48tTwPnIyRyILe5N1Rd5keV16WVMsh7--oppJvuBdoWq5EFqxTaj_zYeiaPYpZYtQm0YfEm7UpcejZTrLxuhbcVkw0hDhT81z9s9FRTkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fd9b7e8d.mp4?token=G4Q2BpWioKFKnFidY-5FUPR3CWMNSzvm1TfHGAXc4bKG-z-3LbM__gHDDBdfp1048DLyZWCCCIiLkXKp53vnsPb5qa0Fb1Pdz_CmtOg08RlESbuKGGUhSYx6HB5O9p1UxnVklCeeDxX_VHkaQLNEbF0f0up3wWlmBhregspB69TTmyDYQE0UwfkWaBgwJUiEKHj9pDeoC-ivOs_4_4pe14had_SuDD1ksKiF8QxrA_Qy48tTwPnIyRyILe5N1Rd5keV16WVMsh7--oppJvuBdoWq5EFqxTaj_zYeiaPYpZYtQm0YfEm7UpcejZTrLxuhbcVkw0hDhT81z9s9FRTkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مجری عرب به تشییع میلیونی رهبر شهید: آیا حاکمی در جهان عرب، حتی یک نفر وجود دارد که مردم برایش چنین کاری کنند؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/669433" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16b82185a.mp4?token=KpTAJvHm_HVxtWzlllLvno9HTNa13UOT-MFcMwCNdL8bXT96BHL2kB06qLHSlyEJ3AlZh54CdOQg2bZQ7fvdoai_IGfjNuNVcpXYYJxeTHowIJcweEEihnmSmh_6-rnu9oTqm4gecoHeHPSmOjBIo62Mf-L2MfjZJD1472xdCylQOIbSm3Uh0udyZah9HCHDL-YpzAPE8tOxU7mavvs8cemnMYj1sEoLqKUdfus7FE11-M27FaihNOyT-lABHvtAD_sy7jIs7_3lYXqjHMzSkS6IsQxRhjlwm0RIuQ-4JRzMUVSEZD5jgPQTbIVOb3slTGi7AC_XE4MGzeluKWvHzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16b82185a.mp4?token=KpTAJvHm_HVxtWzlllLvno9HTNa13UOT-MFcMwCNdL8bXT96BHL2kB06qLHSlyEJ3AlZh54CdOQg2bZQ7fvdoai_IGfjNuNVcpXYYJxeTHowIJcweEEihnmSmh_6-rnu9oTqm4gecoHeHPSmOjBIo62Mf-L2MfjZJD1472xdCylQOIbSm3Uh0udyZah9HCHDL-YpzAPE8tOxU7mavvs8cemnMYj1sEoLqKUdfus7FE11-M27FaihNOyT-lABHvtAD_sy7jIs7_3lYXqjHMzSkS6IsQxRhjlwm0RIuQ-4JRzMUVSEZD5jgPQTbIVOb3slTGi7AC_XE4MGzeluKWvHzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد شدید لری جانسون از سیاست‌های جنگ‌ طلبانه آمریکا و نقض تعهداتش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/669432" target="_blank">📅 13:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
این بار روایت مشهد را یک مهمان تعریف می‌کند...
🔹
شخصی که از کشوری دیگر برای حضور در مراسم تشییع به مشهد آمده، از نظم و پاکیزگی شهر شگفت‌زده شده و از آنچه دیده، فیلم گرفته است.
🔹
گاهی قضاوت یک مهمان، از هر تعریفی شنیدنی‌تر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/669431" target="_blank">📅 13:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669430">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
زمان قرعه‌کشی لیگ نخبگان و سطح ۲ آسیا اعلام شد
🔹
براساس اعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح ۲ آسیا در فصل جدید، سه‌شنبه ۲۷ مرداد در کوالالامپور برگزار خواهد شد.
🔹
از ایران، استقلال و تراکتور در لیگ نخبگان هستند و به احتمال زیاد چادرملو هم به عنوان نماینده سوم، در سطح ۲ حضور دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/669430" target="_blank">📅 13:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhijqSnYxqL3P8V3c6JkI_M7p0CP5O2T8jfC-_dRYi04lrucsNsZmvGf1qbNTpa8wlcI7maXUtN8nd9W5Vb2_dlDXU8JK58lYYmPifj1d8dwD45J4hW4VXJuFjQRrd9efTZxELVBCHKFpTNTQCx3xdIXB8P2HxHIdEyPrazft_5u1W9_JR03R1OTYM8jbgFctZdQbT1nhyl3TED9qPnmXlKBYZ_QdHq7VBHeHM9xvjFV7RBS0zbhPL0YvIxfHpxCHqxN2YessLMyoGrtGhC2corIe2eYw5r6V-x7AHrGz7XFamzNrN0svyYk4jkP5os-LVrA6_dh6X_4MRvKA2RbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشورهای دارای بزرگ‌ترین ذخایر ارزی جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669429" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669428">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7bc2349f3.mp4?token=haKin_4NcHdpPo7jGX_ebc_rhpmSnNkkm8hbpgh-C7ut6lFMexNj51qI07_jw-x4mLB8M1wGRy7AKq4grEriJdyF9Ig6cfrI1aAq6wWmpqN3isDJvv7QW1wtl_giFjVP9id0VMnaSWTi_IkQyJ1Py7rSlCBqCvnijDv6wUW3p6Mjc2v5C2S7tMLg5TS_r6amMZGu5CERJnLuKl-jslBt5yiWGioXBy1W3P00sZmtrrx-Yi-zZ7YGa0RUOapsvfTikR3CgnIxOZk_mQAB5qpI4CkkFOan4MpLIKcvpwFxzmw6s7YTgVf_6SANWVnYYwzD-hLcjhSY3WBMWmu9zZyDPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7bc2349f3.mp4?token=haKin_4NcHdpPo7jGX_ebc_rhpmSnNkkm8hbpgh-C7ut6lFMexNj51qI07_jw-x4mLB8M1wGRy7AKq4grEriJdyF9Ig6cfrI1aAq6wWmpqN3isDJvv7QW1wtl_giFjVP9id0VMnaSWTi_IkQyJ1Py7rSlCBqCvnijDv6wUW3p6Mjc2v5C2S7tMLg5TS_r6amMZGu5CERJnLuKl-jslBt5yiWGioXBy1W3P00sZmtrrx-Yi-zZ7YGa0RUOapsvfTikR3CgnIxOZk_mQAB5qpI4CkkFOan4MpLIKcvpwFxzmw6s7YTgVf_6SANWVnYYwzD-hLcjhSY3WBMWmu9zZyDPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در کارخانه کفش چین دست‌کم ۲۸ کشته بر جای گذاشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/669428" target="_blank">📅 12:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
۳۰ کشته در پی بارش‌های موسمی و رانش زمین در جنوب شرق بنگلادش
🔹
معاریو: اسرائیل به دلیل انزوای سیاسی با مشکل کمبود تجهیزات مواجه است.
🔹
پاکستان: حملات تروریستی از افغانستان سازماندهی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/669427" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بیمه دانا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imWgaFKj7JTSYYE6D1qO8thA907b9TIO0r1uCj3AW0Po-gGXxjU7s-PAENBa19DPUdQP21aoE98UwHVXJZbb1ZKoENGVLaB0RslAgyupVEJIHZen-4KCHE_rSccpY7h8MOyOcYz1KW8Dpewe7ICZZvLAC72CfT7LdbBlGgabpRpSF9CaTNsrbpsI2rOPXv6vIpn6_nbdZuwS4DFtaMtiyNnrQtrpg893qsNKezg66c_jGEii77wtPbkmNizeh0y0Vm4-da2-HBlm5QYPMYL-GOoRjze6E7W0-tqeDXe61kCP8g8lvF-rttHWq_lviJYm-YxtUDX-Roczi7L3fhnzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
حضور همکاران در ایام تشییع رهبر و آقای شهید ایران ؛
ارائه خدمات خسارت سیار بیمه دانا در سراسر کشور
🔺
همزمان با برگزاری آیین بدرقه، وداع و تشییع رهبر شهید انقلاب، شرکت بیمه دانا با هدف تسهیل خدمات‌رسانی به هموطنان و زائران، خودروهای خسارت سیار خود را در شهرها و مسیرهای منتهی به محل برگزاری مراسم مستقر نموده است.
🔺
به گزارش روابط‌عمومی بیمه دانا، خودروهای خسارت سیار شعب منتخب این شرکت در استان‌ها و شهرهای واقع در مسیر تردد زائران، به‌ویژه در مبادی ورودی و خروجی شهرها، مستقر شدند تا خدمات ارزیابی، تشکیل پرونده و رسیدگی به خسارت خودروها را در کوتاه‌ترین زمان ممکن به بیمه‌گذاران ارائه کنند.
🔺
این اقدام با هدف تسریع در فرآیند رسیدگی به خسارت‌ها، کاهش دغدغه هموطنان و تسهیل تردد زائران انجام می‌شود و بیمه دانا با بهره‌گیری از ظرفیت شعب و تیم‌های خسارت سیار خود، آمادگی کامل دارد تا در تمام ایام برگزاری مراسم، خدمات مورد نیاز بیمه‌گذاران را به‌صورت میدانی و در سریع‌ترین زمان ممکن ارائه دهد.
🏴
بدرقه آقای شهید ایران
#یالثارات_الحسین
(ع)
#باید_برخاست
☂️
بیمه دانا
📞
02182468
🔰
@dana24_insurance</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/669426" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669423">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B37LSt8c01TCC6hL8xcgEiqQQarq3VL_ZvVQFgIK2UhO1n7ew9y5k5dvw9h21dtS7PAyTgTgRvYJ2-g_VEB15J4ADfoHm_2WojqT8fQAFBIhfKmOUG9PDqtOVSVbVl52ahhM8AM7RxOmvYauF2vkzjA5XzxNB2Khjzg6xnF29_T0wIBwga-HBhD5T36d1M-17vfpo0QWIe95rXlLIMft2MzlVMGhLmevFeelOAJ1xlFvmib5rGUM4ObyxLN_KT4fduKc5t3LhCgN8cgN3Y97eJwkYgsVH5h0ddALDqp-wR29hNOjE35hNGodPWSe0-KT41b_lSUriGaO10ORgXZy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOYGsioFfsvN0zpXOYxf_XdZV9kNS-ykHAiX0rAkRToqdrPIOu2JJUg3a4rN0HrDF2ibzfjENQg_FUiU_hDSj03OkIpD8XUTPkIU9WX7D6a1_VpowItKxU4ZI-V4S0IlIHwp6TIZ7Q5c63dqJHu-f0w3sDmquso2siQ8Ec_-q3WKvShRGYOeZhtgqBF0vy-KE4gOT2TSeH62kD_mUpi8w04VTRKTCSZsoB75n51PVZHRUPmf51UfebUxnEk3fagurKpQA2cHsqaM2D7bU3x2Tafp4QKbHfGSSS8mr2D2A76s0hsIBoZG2S8AGBon1wirPPoNfJ4d5frYELQJKxRaQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807b5337d2.mp4?token=c6gbZ_Pym6sdCSMYUJo7xgNDWMr9N1BUWW17_8Mjhbax-LQsvLT9JcHpYchMBaPpz3REDvirlS1V77bxz4vDrYheamiKLLhC-pMwevg-ztgW4c3yIIKefU9jmlEyiBrESNRe7k4y3Yi2Bg46rsaxud_fYqGH7rqLjXPhgPqDAJeQ6lDNt1yNNPC_pFUl52gLkXlNPBB5O6-OqYPjmaD2U9G0lLQNh7EB2Kh4J7VaSAPGL9axV4JCuchS0J0nXYbmPQPUNk2_cfzPgkbCs0Py5DVwAdG8SHvg5wBSNF47tvUIPVPTh0e1YV7HkKzr71jz6xX-YiB4t65eJnIXT-7iZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807b5337d2.mp4?token=c6gbZ_Pym6sdCSMYUJo7xgNDWMr9N1BUWW17_8Mjhbax-LQsvLT9JcHpYchMBaPpz3REDvirlS1V77bxz4vDrYheamiKLLhC-pMwevg-ztgW4c3yIIKefU9jmlEyiBrESNRe7k4y3Yi2Bg46rsaxud_fYqGH7rqLjXPhgPqDAJeQ6lDNt1yNNPC_pFUl52gLkXlNPBB5O6-OqYPjmaD2U9G0lLQNh7EB2Kh4J7VaSAPGL9axV4JCuchS0J0nXYbmPQPUNk2_cfzPgkbCs0Py5DVwAdG8SHvg5wBSNF47tvUIPVPTh0e1YV7HkKzr71jz6xX-YiB4t65eJnIXT-7iZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری
زیبا از یادبود رهبر مسلمانان جهان در ونکوور کانادا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/669423" target="_blank">📅 12:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669422">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
آ
مریکا: همچنان به تفاهم نامه با ایران متعهدیم
🔹
۱۵۰ نقطه ایران زده شده
🔹
بیش از ده‌ها قایق مردم نابود شده
🔹
چند ده شهید هم داریم
🔹
برج چابهار و راه‌آهن اق قلا تخریب شده
🔹
پول هاتونم که ندادیم
🔹
ولی طبق تفاهم تنگه هرمز باز باشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/669422" target="_blank">📅 12:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669421">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgalDsfXT1Ii05hFcEQa2Cw6DxQBNXh6UKloCBVywPfX3hu1_Ctfkj6J16oZDRjjzXhpR0gXtDs26_YrUnrK20FcP4sV02Q5-PNdr6DzOv-q5bzZ7_FRnPSt-VjR-IFh04XIdY50VHUlixpppnWYNv_Xo90MjFHet1AyTBl4joDK8Xk5DrMVdr6eIpvWWIyF1GAgCm2GAzoW5JR2MGlqDYOxvRJk7CR72P44B9OtoKNeDsY1Hqs9RGNfXsiWXh96sV74eGy1-FOu8486iwsXFEgT59WhCv4t3ZyFz_7FzY7Viq-QgBGRlei2odmR5HjcIUdMfQzS4cVhBzXDaPhmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت عضو تیم مذاکره‌کننده: تفاهم خوب بود و شیوه اجرای آن هم تا الان خوب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/669421" target="_blank">📅 12:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669420">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqzME1ThdREqneUPiSNInKjOtqZgmFmnxEQGn7NnTM-v6PJe_HfqQKr-R2y6sDfZ0wBrFg-xzivnV_H9f4ne32jdUAgyjRot2H1R3Nn7z3sk5KgCBl884Frwdu_S8pMWqtqVqfVRo0ZAwpwqzg3q3Tej3sfH2QPcR2yIMmLoBCI8OPhavQcVVRSnjxnpxG_g6S_u9fdcsk_diAOxgjPbTm5sVY6-XCG3ozw6d76iKG0x3IcNtA1BcWUUvGudivrE1og90ZETqUbxgoP4V_1mH0970ZUbIQ48nbrAfFJmXuXMQijhnjAzlMiv30frnuwkR_n4E3uuHJtpeIoPmKPP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندی برنهام در یک قدمی کرسی نخست وزیری انگلیس
🔹
شهردار پیشین منچستر، با جلب حمایت ۳۲۲ نفر از بیش از ۴۰۰ نماینده حزب کارگر در نخستین روز از روند نامزدی رهبری این حزب، به گزینه اصلی برای رهبری سوسیال‌دموکرات‌های بریتانیا تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/669420" target="_blank">📅 12:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669419">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sezTbtO0DehCHDfdrANd_9f0k2-PimfaJIna9a4mjsrUAKW4YbqtEX64rvQiSATPp-si7Xk7M0B4IbjMjxcvdDyPoT0jZvTHB_6f4M5i9BRs_HScdhdFxUwvReiGSuZ-J0dA5Z0C6YlYeznbtdh5PAWe8soy3-ufxA3QokZr7iPbTCAydIOhbG4GzobNBCCd_o25QdFRliLLy5BQQ3RgT1eiQ06vseyTI8Lh0ckHUW1f7cbfAQ_4Un1TD6j7SqWYB1-fumT-Wv8_JVOaERnT3amZqkuFTBYT6EgmuRjV4Fw9HSVo8JAkGR55FqeRAOjoJMPYtd4eeivlqtyLaKt5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید اینستاگرام؛ اجازه ندهید از عکس‌هایتان برای هوش مصنوعی استفاده شود
🔹
اینستاگرام در اقدامی عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند.
🔹
اگر اکانت‌تان پابلیک می‌باشد، این قابلیت به‌ صورت پیش‌فرض فعال است؛ به این‌صورت آن را خاموش کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/669419" target="_blank">📅 12:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669418">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0393983043.mp4?token=Iczr-aMAbPphsPm2vQMCV3q-WE6zeITdgUfz5rxystuoa91VrK6_Rnn6dV8k17KMvt0I0BkzBp9k2epSm1kIQV3bIMYTgLSoxP3EciSaUpwGlVCsFQFI5gsXKaTfLYwv5RisOXoXEQZKihDVEfbA-rsPiKlGMcOocQOm3uwN2xW8lXnz548Wih0NHl9x1rJe06TMWNiuJnRdoynYECUeFYe0Rmz5QqSXboYTxDvbdBoKEZEfn67_oh-yIbHm5ypS7ehoW47Sx79YDORoeYAK_Bs8BqGPxeTzqYwRhUk49At-MhoZi4bxiOTJYlXEixZHMSQ_AuoOSGwBsSgx4hDjEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0393983043.mp4?token=Iczr-aMAbPphsPm2vQMCV3q-WE6zeITdgUfz5rxystuoa91VrK6_Rnn6dV8k17KMvt0I0BkzBp9k2epSm1kIQV3bIMYTgLSoxP3EciSaUpwGlVCsFQFI5gsXKaTfLYwv5RisOXoXEQZKihDVEfbA-rsPiKlGMcOocQOm3uwN2xW8lXnz548Wih0NHl9x1rJe06TMWNiuJnRdoynYECUeFYe0Rmz5QqSXboYTxDvbdBoKEZEfn67_oh-yIbHm5ypS7ehoW47Sx79YDORoeYAK_Bs8BqGPxeTzqYwRhUk49At-MhoZi4bxiOTJYlXEixZHMSQ_AuoOSGwBsSgx4hDjEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندازه‌گیری دقیق پا برای خرید آنلاین کفش
👠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/669418" target="_blank">📅 12:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669417">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تیم ملی والیبال نشسته مردان کشورمان در اولین دیدار در مسابقات قهرمانی جهان در هانگجو چین در مصاف با تیم لهستان ۳ بر یک به پیروزی رسید
🔹
تیم والیبال نشسته ایران مدافع عنوان قهرمانی رقابت‌ها است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/669417" target="_blank">📅 11:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669415">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu6qoXjSQ3wTiECPobijiIJgQtL1C1_AJHW64XwJ3sqPMbIexhv-Bdv1Bgb5_sC30pxouw7OwC-hS2NH3mkUKNCxWYpFXrDBinewl3MEz0OsOJOjOIgLCDAndBuKSfUO-Y0pHR1b31yGPpi4CTzpwC4ERbUH_kArDM5Fcxg6e7gWFxCwMNQkJ24zwN3Udfo1kwi2KRXdE9_No5okGvt1Jm_wSlgdIKvQM25ULG_hsiWmGmgxuTQJFSpR-c_KzMFl21mPkElnMsLYdc3jH2gHZG_cLSWCMeWAjJlrpGhMGjslFWYtLdRH8_cZwJhnh6Jaa0p1PZ9ymVvJ6NAwz3q1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز درباره ادامه مذاکرات آمریکا و ایران
🔹
خبرنگار شبکه «فاکس نیوز» امروز به نقل از یک مقام کاخ سفید گزارش داد که گفتگوهای فنی درباره برنامه هسته‌ای ایران در هفته پیش رو ادامه خواهند یافت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/669415" target="_blank">📅 11:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669414">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwe1Qz3mrqt2vGYm_09Y0zW5qs66votVxDqlBD-0e-tTsZvbF76XiQSlKAlE_nX0VK0I9s1gzKEsh0rwr8zFy_LtvdkheITIMRXymCwyh406JPkwQubALG837puyuXO_88F0X95TVZaOLzP7bO8YiZcpGFM0dWR4v7nhYRDmTg87mQe4wkExr-Kx784YjyKbGVroxdty8bnaSHiIgMTtz1JTImTAySo_Yq9A-jlzncYbIdCI68NK0ZBo5ZVuUSwvkw5L3bqcBAIW33S85jzb3VJ0V4BTGFfHfcFnGBb8U6IFOMchEdlz9J1n8mXSirvwZ9Knr_FuocZjn5fKGtQ1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجره‌نامه نورانیِ رهبر شهید
رهبر شهید انقلاب آیت‌الله سیدعلی خامنه‌ای با ۳۵ واسطه فرزندِ
امام سجّاد(ع)
می‌باشند که در شبِ شهادت جدش در جوار امام رئوف آرام گرفتند.
السَّلَامُ عَلَيْكَ يَا زَيْنَ الْعَابِدِينَ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/669414" target="_blank">📅 11:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669413">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیرعامل منطقه آزاد چابهار: فعالیت‌های بندری در چابهار بدون وقفه در حال انجام است.
🔹
پرواز‌های فرودگاه مشهد از سر گرفته شد.
🔹
ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/669413" target="_blank">📅 11:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669412">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27582de67.mp4?token=ClnucxG8FvJtJrDlDqHxwedfdABJcxwGIrCbrO4XtPDHy8MDhCyIvAGMLKe-X7ObI0A_AunZ2GYrI2mhxGxJYUWGt8YV7cJo-ZzKkIo6Grfke-Sbji56cMWmLMz_uFXpukIug1wA4W37lv4xNQFS8OyYJZI0V0tWjT-FFcfwPRJRoFBNBhGs5yUr3wxweBWtqMQcb_mgldJtPfsxG9Ded2QY5JWIvfXpfZMJl7JJcD0UQKV6VaMmxgJKzzsBg67whLHpQh11wp_lAsWF8_4AWrxvLxkXxg6j6KyY9_RaY5ulSTYz_QbXk83U6cBpHNm4oQxvtbNpQ6Cng4npaP9PkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27582de67.mp4?token=ClnucxG8FvJtJrDlDqHxwedfdABJcxwGIrCbrO4XtPDHy8MDhCyIvAGMLKe-X7ObI0A_AunZ2GYrI2mhxGxJYUWGt8YV7cJo-ZzKkIo6Grfke-Sbji56cMWmLMz_uFXpukIug1wA4W37lv4xNQFS8OyYJZI0V0tWjT-FFcfwPRJRoFBNBhGs5yUr3wxweBWtqMQcb_mgldJtPfsxG9Ded2QY5JWIvfXpfZMJl7JJcD0UQKV6VaMmxgJKzzsBg67whLHpQh11wp_lAsWF8_4AWrxvLxkXxg6j6KyY9_RaY5ulSTYz_QbXk83U6cBpHNm4oQxvtbNpQ6Cng4npaP9PkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش تشخیص ۵۰۰ هزار تومانی اصلی از تقلبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/669412" target="_blank">📅 11:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669411">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وزارت دادگستری آمریکا ۸ مرد را به توطئه برای ترور ونس و ترامپ متهم کرد
🔹
به نوشته روزنامه تایمز آو ایندیا، هر هشت مرد، ۱۹ تا ۳۲ ساله، روز پنجشنبه در یک کیفرخواست که در کلمبوس، اوهایو ارائه شد، به تلاش برای ترور ترامپ و معاونش متهم شدند.
🔹
اولین دستگیری در اوهایو انجام شد. وزارت دادگستری آمریکا اعلام کرد که متهمان باقی مانده نیز از آن زمان دستگیر شده‌اند./ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/669411" target="_blank">📅 11:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669410">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d613292d3.mp4?token=gN45s2ReL9-dJhKeofPlrny5sPCE0ogvY6RICXhlu6UPZDlUA5N3L37hdD2OFPVMcu7uruGlsacxFZ2XOJiIrO2pod7PcQzAHFJNvToiLvJzLLJZqxKleJyZcfHzcTadSDi4-symnHO0pN2GpBmQQzP9bxvbM3q-9a6V1xW6uHlJyz-li3wFkX7GcuoXkHjaikFlTbpAocZouiyUtJ2fmiJJH8y4jrA9dHTZYCsw2mBte9QTe1cXzulD1o67e3cDG40kdViLRjfFEy12vPzkt3WY2muxQttGfq9cPAcOUiRg9DbLSLhJ4pAcKYIGb-N0Bxsacu2WU2BkZZuvE2bERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d613292d3.mp4?token=gN45s2ReL9-dJhKeofPlrny5sPCE0ogvY6RICXhlu6UPZDlUA5N3L37hdD2OFPVMcu7uruGlsacxFZ2XOJiIrO2pod7PcQzAHFJNvToiLvJzLLJZqxKleJyZcfHzcTadSDi4-symnHO0pN2GpBmQQzP9bxvbM3q-9a6V1xW6uHlJyz-li3wFkX7GcuoXkHjaikFlTbpAocZouiyUtJ2fmiJJH8y4jrA9dHTZYCsw2mBte9QTe1cXzulD1o67e3cDG40kdViLRjfFEy12vPzkt3WY2muxQttGfq9cPAcOUiRg9DbLSLhJ4pAcKYIGb-N0Bxsacu2WU2BkZZuvE2bERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بله آقا! حق با شما بود
💔
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/669410" target="_blank">📅 11:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669409">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOSFjsYBupejngVLExjDmfX48x_CalHy1WsIF4dQezJx8xf-wgd8nFxCQDO1ZwgjN9DfK-26WyCbb7Ynj5tfHRYtjbc_r6tHtcK1nK4AQup1oKjpO0Bazm30ALxnW3PH4dkfP0FJN-Ki-iO8ZVqDNImBpX_L8pNYptTGpA96pTepUg24TTJ6pg-y7TpgM9GcwrMDX1A0PLXeA-r0WJWvDDQep9gyG1BYLCiFQwAFOa-CUPpdvwbmSSf72zQZnqm_AgEJOOXGcmRI3lu9zaoeoyfSlonHsOSUMc7J6pC3zkjNXNLwo06mrafJ-Mchj-Ap6Im4OeaqkgP3bxQBmDZOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایی ویژه از طواف پیکر آقای شهید ایران بر گرد ضریح مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/669409" target="_blank">📅 11:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669408">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmWIDQutLLgjC5dGhIhBRfiqrtTWQZm_uQSv9k0odRAFTNFZoOj8YtPP9czO4qDQgQtgr_301DYGauRXPG7Qrlgzb2HSUSOJd0-G-w2tUDhrPjmPZx4FX785DWFqLSe55tYH3N37eXI3dpBNRLLogHgh1DnBbFITFEdCiaRssU-I7eAxq-KfHRUpy0eghRlWZtWaIqnKCBc1RR64pYG75eL7xqMo75LPooivY_e32HzwXoKC56l0zR1ncHIw234_QA5gp6nrUiZ_7AOsDArEJgwjjAJunXIKABNaJ0mkK2W2MkMJplwupiJFU8d1vLxzsU19pnVNPLkUdmzGB3J0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاتالوگ کامل انواع مدل خودروهای آلمانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/669408" target="_blank">📅 11:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669407">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آغاز پیش‌ثبت‌نام حج ۱۴۰۶ از ۲۱ تیر
سازمان حج و زیارت:
🔹
پیش‌ثبت‌نام حج تمتع ۱۴۰۶ از ۲۱ تیر آغاز می‌شود. در مرحله نخست، اولویت با ثبت‌نام‌نشدگان اعزام حج ۱۴۰۵ است و سپس سایر دارندگان قبوض ودیعه براساس اولویت فراخوان می‌شوند. پیش‌ثبت‌نام رایگان بوده و از طریق سامانه‌های «پنجره واحد» و «حج من» انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/669407" target="_blank">📅 11:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669406">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
وزارت آموزش و پرورش:
🔹
آزمون‌های نهایی بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
🔹
دانش‌آموزان می‌توانند برای دریافت کارت ورود به جلسه آزمون‌های نهایی، حداکثر تا ۲۰ تیرماه از طریق مدرسه محل تحصیل یا با مراجعه به پنجره واحد خدمات الکترونیک وزارت آموزش و پرورش اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/669406" target="_blank">📅 11:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3Suh6nc2htjcZvO974kL-54LgEqNzNpVM4NdVWQ91dY51PGUZArIGDAkvmDByucCXdH2z1k8pdkfifC7zPACbda3DuYudpEqvtHTpT9iwQj_39AWg0G10-WSy33hdepWt3FdL_yZh9qYkyAvwD90dJqMGYH8XHnPSEWlA6YzEL2rnlHamA_-052QFy0YuXNk27qmegYn7BobmRjj1MJXKUc3TGZ5qmI5DPSOc3KrilASce5JUw6IF9W7tO5lhGalJl17zOMX8PXHl-rk4A-Bs2j5Mdl8-V6vFueGSnB6D-snECzXisZWNf8rw5kjby822AaEQXLeiLVn9DCQ971Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایستگاه فضایی بین‌المللی: نزدیک‌تر از آن‌چه تصور می‌کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/669405" target="_blank">📅 10:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تخریب ۳۰ فروند قایق صیادی در حمله آمریکا به اسکله پنج‌پله بندرعباس
عضو هیئت‌ مدیره تعاونی صیادان پشت‌شهر بندرعباس:
🔹
در جریان حملات روزهای ۱۷ و ۱۸ تیرماه به نوار ساحلی استان هرمزگان و در پی اصابت دو پرتابه ارتش آمریکا به اسکله صیادی پنج‌پله بندرعباس، دست‌کم ۳۰ فروند قایق صیادی با قیمت تقریبی هر فروند ۲ میلیارد تومان به‌طور کامل از بین رفت.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/669404" target="_blank">📅 10:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669403">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE5cVb9wssIlQ2nA2r6bCg0f8l6y4KT78KPh9kK5jRVleoErJJmIEqFwEfvgs27lNBR_k8LWtDU3nXI0hPDluEdbZDksq--0bvpMfY4VOjgKlmaQkgiv01mW5Kvm-fG7589O_a2e4nObgS_iKA5GBEW0V6oxlNpXvapiKPFrvQGrLCHZzQEyKZlWOHr-czvix_WXP3ic7J1KtHQhfYbvTYcRG5QbpHXT6ZI20oObXyEDlDyB4yB5if3eoV5B7WWJ25NxDMrVq_dWZnNs4ODq7yLZiJyYaOxEjYDRLr_lS9b-Bp1yTOKM4WU1a_WtaYnWty7uoUVhA89gHxv1I0xOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممانعت دولت خوک زرد از دیدار دستیار زهران ممدانی با نماینده ایران در سازمان ملل
🔹
منابع آگاه به روزنامه نیویورک پست اعلام کردند آنا ماریا آرچیلا، مسئول امور بین‌الملل زهران ممدانی، قصد داشت با امیر سعید ایروانی، نماینده دائم ایران در سازمان ملل، دیدار کند که دولت خوک زرد مانع برگزاری آن به بهانه تنش‌های اخیر میان ایران و آمریکا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669403" target="_blank">📅 10:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brwGN3o7leZPUmGazwlIvPIar_LcS-BqdnYNO2w3CBJHMX__54MU4K0NxmlyDaN8F4En_RkKku3dcGxZiFSiVz-3pimYogEU6N7Viz_w1cKMs1i_BPOUjGHo7_vuaovo7sgpcY9TXtIanSKW1SqdCrRNp6vpIkeAELRkdsYQZiBWQF_MihdCwWDPg7FB3HAvPs8w1nYuLJkqBcItqqwK-BHKPLzYYYNzC82v2Rrerq8uBMzcpoS8LDTEzpKTt91qH4mKHoiPmRLmj93EHZALLHc0TQvF2dkVB_nQB7mfTGUvbmlFV8mtyolq4DLQjtHRGLLFkkFl0WZqALXdk4NqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ابطحی به تشییع گسترده رهبر شهید توسط مردم ایران و عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/669402" target="_blank">📅 10:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669401">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
روسیه: رقیق‌سازی اورانیوم ایران در خاک ایران گزینه‌ای کاملاً عملی است/ رسیدن به توافق در شش ماه کاملا امکان پذیر است، حتی می‌تواند سریع‌تر هم باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669401" target="_blank">📅 10:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669400">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2bDyqMkRyhtjKyYVy6ik1Ivzebqgt-5oNgTP1Rcm-0Rbdx3Hmi_MSPUB1XFXbUZ1H7ZudFa5Sll7ggdU-iLtQisJiabVj2hTtTx2gnr8PCGoEvmXERxHdv9Xn8hGKPKMhEnzVH8awF2A95-0mb9-X9U_DMnRwQXWSLQLLH8r6wEXWmnVbaZrYXlWuKhed93jt0XCfcwC0PWI6kKWTSvBljD-2T4t24RJSd8GByI2E15ZbRll2iL60u_NlUB5jyExPqfqF8hv6Y88nAq-wAdzVGzf2Wtxq69VCYQRhD9it-SGcJv87MMGUDA5GmucePMP80mHZHMw2pGpm7W3oOhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله مرگبار به منزل یک رهبر سیاسی در پاکستان؛ دست‌کم ۱۷ نفر جان باختند
🔹
منابع امنیتی اعلام کردند دست‌کم ۱۷ نفر، از جمله نیروهای پلیس و محافظان، در حمله‌ای انتحاری به منزل «شفیق‌الرحمان منگل»، یکی از سران محلی حزب مردم پاکستان در شهر خضدار واقع در جنوب غرب پاکستان، کشته و بیش از ۲۴ تن دیگر زخمی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669400" target="_blank">📅 10:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رسانه عبری: ترامپ جنگ را از سر نمی‌گیرد
اسرائیل هیوم:
🔹
تحلیلگران در ایالات متحده متقاعد شده‌اند که ترامپ جنگ را از سر نخواهد  گرفت.
🔹
اگر ترامپ جنگ خود را قبل از انتخابات میان‌دوره‌ای از سر بگیرد، محبوبیت او به پایین‌ترین حد خود خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/669399" target="_blank">📅 10:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09cbcd90f4.mp4?token=fs4C0kzbdKj0hmnHs02lnBzl7aSeazCNMEjTruevgfvAfMMw3Is6G-9cqh-UF0fk21JLgiFqgyH1Jzp9O64vaItV997368VPMF_lQ4x1rjvsHTXzLMGcZ2bEwqAPngS31URGJcou9dq7rDTQhkvtqH4mVciUaCDqH0CC7ShI5O4qu0RxA7S-2Nx2haVKyj43V96j7zlFMTaXxbnF5KOvnwmGXTi_17dHKko2fETnueqDdwJiY2geJMLQSvz5W5SDKxaKJkOR621yeo6A5rI-hJhm8al3trWZAipNq-BWyWsXKe21_Rzu4YL65R-R6bn0-VjWxeFTKai0WymmxbyVmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09cbcd90f4.mp4?token=fs4C0kzbdKj0hmnHs02lnBzl7aSeazCNMEjTruevgfvAfMMw3Is6G-9cqh-UF0fk21JLgiFqgyH1Jzp9O64vaItV997368VPMF_lQ4x1rjvsHTXzLMGcZ2bEwqAPngS31URGJcou9dq7rDTQhkvtqH4mVciUaCDqH0CC7ShI5O4qu0RxA7S-2Nx2haVKyj43V96j7zlFMTaXxbnF5KOvnwmGXTi_17dHKko2fETnueqDdwJiY2geJMLQSvz5W5SDKxaKJkOR621yeo6A5rI-hJhm8al3trWZAipNq-BWyWsXKe21_Rzu4YL65R-R6bn0-VjWxeFTKai0WymmxbyVmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت ۲ دختر سنندجی که در توالت حبس شده بودند  سلمان حسینی، رییس اورژانس اجتماعی کشور در #گفتگو با خبر فوری:
🔹
همکاران ما در سنندج به محض اطلاع از این قضیه از طریق همکاران محترم‌مان در فراجا مداخلات تخصصی لازم را انجام دادند. درحال حاضر خواهر بزرگتر…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/669398" target="_blank">📅 10:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669397">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVZuLIEAmCL0NcRIPoVDal9Cc3PHy36z1Tqns1yv5j84c1nXdtlaK4YHQk299dg2VKd199Re_75cQVDjbMHT1MQHlYMQdJnyIHnYgyMMa3UJ1SYQLT18BDYlLmd-FmCbCjTI0NcGuejHuMaRj9SPm9AakW4pbkJv5xNdeefmp3wSn6XCxPzdU2v5FVeMxtKCMo49aGbcd8934uWzP7eY9hHGoSWz61NzYMSU-DDFahkLMKcD5-J-EEe3ob-y_kfuUNnzcvGckEoeu573AnUJQorjLwTaDZ8iwMdFFh-yzIWWUGBU_rISPzWWw39pLYYcA5N58qMFa4nGXUEpd2Gvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدامات لازم برای زمانی که مبلغی را اشتباهی واریز کردید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669397" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQjbdCG4fXNNoCfwzjoeyLX091gcpW9P_MTsLQ40OagNtdIysALVK9lZ4FYP81y0r27tHOZghh7CIuhLV8bsX6GUZHhKAxz9oGng3XGRyFekMU9bSOsGFn9aVpx2Qu3mFidTSuS-NwAhh_ohXyhc4l1Xn2i6vh8IavuEJhKFmd6vov94oUn5aETjcjKgpm9kN8IUc-locwZcktRW2eQl_wjRiHbIcPYrE0fGOTBqlh6xoOPbEOwEXVtfzw2jTBNo0uLYyBKPCUTzrntBHF6oclZ-DdrT0GN0NeZNLgnxcKfFnENbp2dQEsdxiYLnLSnrd3_v5jPj622KnvbcOiw_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آماده روزهای داغ باشید!
🔹
بر اساس اعلام سازمان هواشناسی، از
۱۹ تا ۲۵ تیر
با استقرار الگوی تابستانه، دمای هوا در بخش‌های گسترده‌ای از کشور افزایش می‌یابد و هوای گرم تداوم خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/669396" target="_blank">📅 10:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669395">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnTTXNcA97ke-2WUs1yzrhhYI1dtciqX2Am0eDN-K3z-w7hZMBJYdFr-X2oUln_2Fj6WirAWhxAvKDti1RfzWP0RhT7XKe81QC-W5iUrWT47ZAd1y4f3kQKYzaryTnEWC3bKcAOLk4iwyEbIsmeY2vMqUo50Ifi6IsfgG1gr43mNth-ohDexFP4DWCNt4Hmf3AOHvk1EtZEnviXvdKMJEWKClTba-_z3pwDyuc2hnR-flEbEL0f--L35ugfQC-r0pxqin-35bvzUoIL2nSuMl9c16K327hEEUNFdPhykSm8DTvta3v24D8fmnUXCh_mDA5XLM0A_eNExnBT6yjhzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سریع‌ترین عنکبوت جهان با سرعت ۱۳ کیلومتربرساعت شناسایی شد
🔹
دانشمندان با مطالعه ۲۵۸ گونه، سریع‌ترین عنکبوت جهان را در کوئینزلند استرالیا شناسایی کردند.
🔹
این عنکبوت شکارچی با سرعت ۳٫۶ متربرثانیه (۱۳ کیلومتربرساعت) می‌دود که از سرعت پیاده‌روی سریع انسان هم بیشتر است. پژوهش نشان داد که سرعت بالا نه به باریکی پاها، بلکه به بلندی پاها، جثه بزرگ‌تر و نیاز به شکار مربوط است./ دیجیاتو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/669395" target="_blank">📅 10:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM0gXURTTbRl6-BPqeW7fOrFK9BPeXbl0KH7bUHIIf0-qFYvLqqx2Y8mvdjYqUZmdeZFj50UISbUnbMkTE1et0nPROmbL0XaW2lb502mC33MezZoVJagf3HdozyldIZk1rZ16V6nY4n0gVwSME2ukA9BIYp10IztbUwLxt0rGVNbhYyQGCHBjkvy2k_WsVBFG2ZEBqOe40tSkSCddUhSQ9XpUC0rpHQK6UUasexewkLyyWWu2M7Rw0WRf455sZmvJcLoC1gxMQbn3CkhUDTpLt4UT-x1txzNC5zDfgsO6wIEXmr55x3xwUxAV1hybpI0brwMMRrPnwgaxyezmZRMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از دماوند زیبا، امروز صبح
🔹
عکاس: مجید قهرودی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/669394" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/669391" target="_blank">📅 09:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669387">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhPTkZ2KP7_sYGLphO8YewJ4FPwEgTvgYXe-UIGY5FybTRkWqbPI8ygrpVdBah1Zdr04GIeFeisdBZ_H7NjgJfZRlvsEnNMPScllKfAzERXpv9RbTlSBxmWbcJ742uNkXXK0K0Dm7Ro6Qzg_LUEK6b5l1Z2iIRQUsjqByTD0Rq_D8JUcxUKrSWl0DufGvzDMUEEbSMxWlBFIqynqiMDWA3qHmNRgin4yyFzZbffSq0OcQxld4XvKb_6wbQo-7rt4U0rnZy0oTpBqWQ8wMnvQjHSNS6b96w5r-zSTEuTEDWufWpuQum2ZEeJsDE1UHWESiVhYqPz9pck6TY6fhPgdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKmneAMAsbfTR4DOCvkpVj52GlyfnBEZ9VMe-lt2RBx4gmAGjtqkDBqYdPQMyBDIv9yG76V-zlY_QDQSvCRRW6bcGbNYlb4EFmwU9bbmsfoqzgdEAoY42XH-NjzGkWMmr2avUZEUkJaMgaG6xD5MnJfmKZxbwKQSdpDjf0M4S2hGNCGhJl3I3k5gXX1YEfZr0kFZHkpj0s9KTBcTnqVRCNGdKQ7Rc20y8I_s4jFBdibxieJbtaas_Lz6ruteXJkwuF6vdPi_LSRijHpEJB1S2tW_6LA59MdSckrwEUik94Lnz7UJ9u70n3t_-0tG3yUXy9TDdVNbMifCRhbFphpRMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5988ad7731.mp4?token=FdIwKi21DnIOzB-A3mJKzcaNEgr63_oQWR3QGLVlavdBBQzRvMWs760_yazasTBIjopJGNmwToRUS30rEp0HzqzAqWHqAnFYNQ4EE7zjX-2scdeQPfsMyY4zfYO77ZqF8fUa0v7FKZdlddWXo8nzXYtf8QLkwIzPqUpDihXxq7XT0JRT_nN68i8u43-B8BotEx_FdipowHP5_EZs05FP2Nj1lW-8y2PfQi9V8QVLx6w0m7_kqwtyQmBzvoJXltVwf7hsDdsglwypoo6uIx26xs-CXjU-v0nzXSm8vPLkrFmD_KfYvfI4e9rEjxNYzpBQ41QF16f0ot1nCIrAfG665w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5988ad7731.mp4?token=FdIwKi21DnIOzB-A3mJKzcaNEgr63_oQWR3QGLVlavdBBQzRvMWs760_yazasTBIjopJGNmwToRUS30rEp0HzqzAqWHqAnFYNQ4EE7zjX-2scdeQPfsMyY4zfYO77ZqF8fUa0v7FKZdlddWXo8nzXYtf8QLkwIzPqUpDihXxq7XT0JRT_nN68i8u43-B8BotEx_FdipowHP5_EZs05FP2Nj1lW-8y2PfQi9V8QVLx6w0m7_kqwtyQmBzvoJXltVwf7hsDdsglwypoo6uIx26xs-CXjU-v0nzXSm8vPLkrFmD_KfYvfI4e9rEjxNYzpBQ41QF16f0ot1nCIrAfG665w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برگزاری مراسم روضه و سینه‌زنی برای رهبر مسلمانان جهان در برلین آلمان
اخبار مربوط به آلمان را از اینجا دنبال کنید
👇
@AkhbareFori_DE</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/669387" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669386">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فردا شنبه ۲۰ تیر، کالابرگ سرپرست خانوارهای با کد ملی ۳، ۴، ۵ و ۶ شارژ می‌شود.
🔹
فردا، آخرین مهلت ثبت نمرات دانش‌آموزان پایه نهم است.
🔹
هشدار افزایش خطرناک UV: گرم‌ترین روزهای سال در راه هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/669386" target="_blank">📅 09:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669385">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzxKO9UM4b7jKDr9g2KDIC2Mlh5bWXi7aIrEi-6JNvj-VAf9JuDyMC4AypDCDATW0vxFr2jbfh9KGwQJLfvs0ise555qFpwed3ODA7w3m8pnvJoOhxV6AUol0BUHArhaoNkmDVEdkqnRcGz2Mdy7vEXrGR77y_PXeCsuFQeYIkEctp8WwIZHfHo0dBnGJqyXlQ9BC7h_3BFJm0x5U_fluzMoVXUnucumD_h6AMIRK2tqzOF4aj2OUxneYc-oUcnjW_C0dd5WcZEQcjwW90uKNi7oLIC15OwzZcNtcHlvIMKv6qoKv3kq2oRAYWVlIFLlqJ24QSKr4Mu8L9NxtmTYdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرور سریع مهم‌ترین اتفاقات فناوری در ایران وجهان #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/669385" target="_blank">📅 09:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شبکه‌های اجتماعی؛ آزمایشگاه هویتی نسل Z
چرا کامنت و آنفالو برایشان مهم است؟
سعیدی،روانشناس:
🔹
نسل Z (متولد ۱۳۸۰–۱۳۹۵) و آلفا (۱۳۹۶ به‌بعد) از نظر سن مواجهه با دیجیتال تفاوت اساسی دارند؛ آلفا از پیش‌دبستانی وارد فضای مجازی می‌شود.
🔹
برای نسل Z اما، کنش‌های کوچکی مثل سین‌نشدن پیام، حذف از گروه، تأخیر در پاسخ یا آنفالو، بار عاطفی واقعی دارد و شبکه‌های اجتماعی به آزمایشگاه هویت آن‌ها تبدیل شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/669384" target="_blank">📅 09:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/968ccb3c3e.mp4?token=c0Q7rc_6D7aJz1yYKmYVMc0lRKSSOQsqi53T4_sb7z0OOoy94_13FvfRaUebJ8MmEB3dajjI6vUNK_mQU7Eon0zRx51LPvvcnpsIg_lpa_K3E9bvMyo7PoYvQs1yed2qKBOBwBVWXzEqP6aJ8yf8bCqMifxCEiorvlqvR-dpnULtJLomMjghB5dUR3jmTazbM09aaODx1Qphq9j5oF0C0p4R0ecrXfwkkwW5KL3SK1ZIm__wL5yQrA2PCcUiErJATahGMQQg-NQIGPmnaGenFJ8u9MQX3VGRoak-EMkiJFqPZoDWdPLNl7_Jo0J_M9NVtFbUacsoiBUaqn4g0PwtoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/968ccb3c3e.mp4?token=c0Q7rc_6D7aJz1yYKmYVMc0lRKSSOQsqi53T4_sb7z0OOoy94_13FvfRaUebJ8MmEB3dajjI6vUNK_mQU7Eon0zRx51LPvvcnpsIg_lpa_K3E9bvMyo7PoYvQs1yed2qKBOBwBVWXzEqP6aJ8yf8bCqMifxCEiorvlqvR-dpnULtJLomMjghB5dUR3jmTazbM09aaODx1Qphq9j5oF0C0p4R0ecrXfwkkwW5KL3SK1ZIm__wL5yQrA2PCcUiErJATahGMQQg-NQIGPmnaGenFJ8u9MQX3VGRoak-EMkiJFqPZoDWdPLNl7_Jo0J_M9NVtFbUacsoiBUaqn4g0PwtoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مجری مطرح فاکس‌نیوز علیه ویتکاف و کوشنر؛ آنها آدم توافق با ایران نیستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/669383" target="_blank">📅 08:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1LDfhjsD9D-wLKUwVNTxzp3sV13MESSyr9ogfLYOz2djGCDzyQC9-l7QE4d-RMdxDocfV32I8POw8KuhYpiyypxzl6yh9rf0oQ0yM25Gk9pfCymL6NEhtYR7jfRjQpboS9raMz008aeVhaSVno2jxjJ9jZgpEZT2SJsNwkBiVTBgEBpjVgGJ4GXAhVaHcjPh_ZuzLYjBhDmOJSplpsHPU0YhoXLaFYnhZXdFD0FfOaRc7VBkOP3ge9rNhSnmJO0n8_vVT9agffdAjLE7CDyxaj_fnDEScsznN56yNWQsIvBz4Pk7t64LlmE0MhG6tjxe8JVImIoB1Hf5JR7ZX4qBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان روز اول مرحله ۱/۴ نهایی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/669377" target="_blank">📅 08:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehhDEFDMSSfoBs0LHjo6UtkwCfxDqeRgGW6yg5nW0gO4z3QG75BQz8nUPx32JV9pp0SwX0FEUmNd1fhe_Oy5p0xXOvpxzaaU6yBo2Jr22RVEbcT3geBJKTN-amCeCVei6glQ56bjt63LZVIE033nPsJ5MRoRuWpsU05lnTXFOor3q9GM-ufD8AvCSaevwzsfIJR8IUCmUI8tuc5XqrkusP1t59UixmD0z8nprv4Tg2rEWPCChm73GksFZGLLqPfUci6UMhj4WmAoduGQ70FLJT6vlPXDZVNHeIrLML5knheCD4o-eJe4a41BRoJ1Y_H5oZPTJ7NZouIbqcSGUoPdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳ هدف راهبردی ایران؛ چرا این تأسیسات آمریکایی در منطقه اهمیت داشتند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/669376" target="_blank">📅 08:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhwAEishfjjQXpLU_fam8KnQNcSeaR009Mj7TCsdFMMsFynEv1TGXX3cfoGHrsjU1fNltj5tcM2mvm3rOP-tPHOU8LnEhs6NzVxmvTmL4TMc0c8CeVXLcfzW2kd9hoGwMpasnTYPecRy5H9JBKCzqIsaeJxRx_S7irjTiGycIoLAZLclo4pAZZD8Y41D6TrjELmUUU_yHs19jKwuTp1A16Dn7yyrPsEqPerOJCSERFi82jN1zOriQo-VT7R0xdVL9SF0IEJlIEsOgYwYL4BzZrMsxpZna66Hp0TSTZLbta5ch9iYwwqH3PZf6B0WLheDUoFz2BdMGpekfH3wlnJleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرکت چیپسِ کشور مصر، تولید تمامیِ بسته‌بندی‌های و غذاهایی که برچسبِ لیونل مسی بر روی آنها خورده است رو متوقف کرد و از این به بعد عکس بازیکنانی مثل کریستیانو رونالدو، ارلینگ هالند و کیلیان امباپه رو میزنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/669375" target="_blank">📅 08:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669373">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7DD8KzslCguPSLeT5nOCtfLF3VKD5HW1i1Zw99zzUdoC63lgziepX9-NtJtrCmt4rRs8eYhonQlG4Bqy9lnttf9829eYdfBA511YAMPhcqMM6Aag0JgJgUyHz-AbJelGmGx1WfFkaK7mpM96t3CATJwuPwMHEx38QP8dHK9Cq3bc0ZjfBtWkNc2VaxX9plKcMzH_guohX-XBBpdnBiwxaFiA4_D_87AtmvKWtkcOjKEng_6MywV0LIGf507-6_An7U9j9XIaYZR_J1WSISOXitHEbd_DkoL1p-Jxc6frxcQ2yOMkhf6aUnVLIG75_xRw04O07bRnpP9VObkDK5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب اسلامی در دارالذکر حرم امام رضا(ع) به خاک سپرده شد #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/669373" target="_blank">📅 07:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669372">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
«محمد» در صدر نام‌های کودکان انگلیسی برای سومین سال پیاپی
🔹
بر اساس جدیدترین آمار منتشر شده از سوی ادارهٔ آمار ملی بریتانیا (ONS)، نام «محمد» برای سومین سال متوالی، محبوبترین نام برای پسران متولدشده در انگلستان و ولز باقی مانده است.
🔹
در سال ۲۰۲۵، نزدیک به ۶۰۰۰ پسر با این نام ثبت شده‌اند که تقریباً ۲۰۰۰ نفر بیشتر از نام رتبهٔ دوم، یعنی «نوح» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/669372" target="_blank">📅 07:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huQ_HEMlaHeJRtcfd2genYRuTDNiGRRH7Kw10tAjRm3U3reov5OStWUnVAjeEMH5g6o5AgJoMZUiQOlrkT4m72O8zEV8KIfJTKx3dC1pXt1esKKxeJaM5sRZvK0fbPf8jsC2WXtMNLDGiEx7qNJINJuM_aoML7dLl7oGCU2QjshdXGx_q3P3d-2xfbyvevFHKIlJT8NuFf_MAHxYFmO1yDxd0Pv1fOEDvF3SX8SXp87LynJd7tEoBRQtcJFreN7PaUvyMUcV2Kfx9l54QDwG72gMixA3EB0cOPeX8Sb_uhe3sr0sp8sqDbdBR-eFAUmibVU6TjtzYYSAqLbDwbkr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پسر نتانیاهو نام خانوادگی‌اش را تغییر داد
🔹
یائیر نتانیاهو، پسر نخست‌وزیر اسرائیل، نام خود را به «یوناتان هان» تغییر داده و در نهادهای رسمی ثبت کرده است.
🔹
این اقدام هم‌زمان با محکومیت‌های بین‌المللی علیه خانواده‌اش انجام شده و روزنامه هاآرتص این تغییر را از طریق اسناد مالیاتی کشف کرده است.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/669370" target="_blank">📅 07:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOA_3T8-LUiPoooU0TpH3WFRkZLOhKCaFJkZHyyT5SHzJpwTJtgAjzM6nbLig1FGAoH9CcF3dUJfKUvApqUpYDwQ94nOUQJNbbZM3t-cc7S1CiAtyaRtz8jmKRgCXwQl_JzMVJYirZUFj0RKadYHfuaMKr7eeVFtfDH6QD0olM-9bi9EYHNwp_W9DUk4ANnMCx3lQ1q1_Dp-dqAkF_cpc6qS0kf4hNLR_Hw8NbuaSmSaY9py_Seh5QTZRJgsBl9ifPAD838AvkzfrHh1kVgDedWe-0FeG_XFY9C9MTG-2rRlcuwZAszCRRmbBsB-ljzqrQ0MTEOlL6-ZcQPcVpM7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پخش صدای خواندن تلقین بر پیکر امام شهید ما در حرم مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/669367" target="_blank">📅 07:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmhiU1c4oltNDCS8wz1awuk7F6p-KHCosvcU0LuogcJDf79Ss5t95N5Nf3wSOyIjSi_QyMwTe4jJt0N6Ff3_RYt8hEzaa182JM-B9PuiWFsUT0zCr7BtF8VjUmm6fHe9siSWA5O23cDJNrAmmhzow5fEs0oebhoHmuPf752JqZi8EadubaqsqIuKNITYT0QFj9xen9KtBmgp0cdNLiYzTwTI1EtdWmePuoU0kY-j9q7My-ZAjIK-ObBvV2M50fspBB5YDxegY2oed_0gC-nzi4bErJ_py14JG2TiwCnJeUDU1vz89Um5mOY0diXhkiNBWHJT7eRGiExHYmLHSIONNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۹ تیر ماه
۲۵ محرم ۱۴۴۸
۱۰ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/669366" target="_blank">📅 07:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873ea1718c.mp4?token=ZKlVeZ_UKIAhooG6M9xtzn2ZAkza23ihp0JiFe4v1MJ1FJRrhNtKj-eKyOkJkb2mN4gJhoM-_cEJT_D1TcRo2hR9dnDEyhMbx32zhCTEW79ly7ILtDWUJ-8wj0dCrJo8QDJBz10qex9esnj28QhuQ-AnJFOOo_lXpXK3KS4DmUWOLVHLuCJiLW7cKenWD5SREfAbRb89ZFhlXAw8i600xEyw7bBocWA1oJFNxdS9P4_XJej3tILTfjiOo0CxWcXJpWPDofCa8god16z2j1KeNjUvR6f0ErkxdwSXC8Cejv7ZFZwMrM8s66nNojVXQrLpLXoV4twZeknvWaFQrQj8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873ea1718c.mp4?token=ZKlVeZ_UKIAhooG6M9xtzn2ZAkza23ihp0JiFe4v1MJ1FJRrhNtKj-eKyOkJkb2mN4gJhoM-_cEJT_D1TcRo2hR9dnDEyhMbx32zhCTEW79ly7ILtDWUJ-8wj0dCrJo8QDJBz10qex9esnj28QhuQ-AnJFOOo_lXpXK3KS4DmUWOLVHLuCJiLW7cKenWD5SREfAbRb89ZFhlXAw8i600xEyw7bBocWA1oJFNxdS9P4_XJej3tILTfjiOo0CxWcXJpWPDofCa8god16z2j1KeNjUvR6f0ErkxdwSXC8Cejv7ZFZwMrM8s66nNojVXQrLpLXoV4twZeknvWaFQrQj8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نگاهم به خالی‌ترین صندلی است
دلم تنگ لبخند سیدعلی است...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/669365" target="_blank">📅 06:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669363">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIcj4NiHeiiU8dzHOTPIzfSLS2hDlDlkH9BwMGQZ8T4qSugC_a2ef7-Ik8eLKv1QIdEuYpoaYmuN7BdBttSPcSumiUDkkHOGF7iUAMEFKc0cQYFc4NC3wO-gZTq1mP4c_BmIabOC-zSPYfFQQUMJ20CxrJphlqNYgEcAqKBAF2ehgsdqU1RD-UHwWOuF91YFsA0P9oiJkb3ZlmuqnGot8eSlkd5BUZ8g9-PmW5NYf2IhP9K9wBC1wDcyLVAFvU_4Absn6NEgDkCM_a5EeNRa8WkP31KSuSH31RabdPsBifFN-I9o3O33IlCJodVECEbrEqhnUdH7ODtO5PLD4H2qyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلگراف: میلیون‌ها نفر پیش از مراسم خاکسپاری رهبر مسلمانان جهان، خیابان‌ها را مملو از جمعیت کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/669363" target="_blank">📅 03:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLzLKazMeD3O_-szYRIS8ErV0S4i8b3zfP9VVhsxnY2ZXvjpiFYEAbdcBlPuWx1pdYfpA4KnBSrCE9Cn890I5kVJ8GNomL4Vrmf2hEq7pLv_3MplKw52rfhw5FIcOK4rmA0CEH62j18jILRhSZtmtXrSGbHWbN5aARR0yIc4-JNNilVDdHJ94MXJtwydSWBLJPUcRvKXtcRzlUeaLiwT1dRalLCu2ymwubiPQ0QC9HJb22YefE5IoKAFd2x9OQrJEM8YqTX1KPa9NSs5RROKXruJ0qHPnW5ASXll5IYkUAq0xzgXMaDZse30H4KP7oFbQJJPFmGJr_Rqes6ZZfP8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
نماز لیلةالدفن آقای شهیدمان
...
⚫️
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
💬
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ ابْعَثْ ثَوابَها إلی قَبرِ فُلانِ بنِ فُلانْ»
👈
(به جای «فلان بن فلان» اسم هر شهید و پدر ایشان گفته شود)
📝
اسامی شهدا به همراه نام پدر:
👇
🖤
حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای، نام پدر: سید جواد
▪️
شهید مصباح الهدی باقری کنی، نام پدر: محمدباقر
▪️
شهید زهرا حداد عادل، نام پدر: غلامعلی
▪️
شهید سیده بشری حسینی خامنه‌ای، نام پدر: سید علی
▪️
شهید زهرا محمدی گلپایگانی، نام پدر: محمد جواد
🏴
#باید_برخاست
|
نسخه قابل چاپ
🖥
Farsi.Khamenei.ir</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/669359" target="_blank">📅 02:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669357">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269183605e.mp4?token=qjbsr9tjTpQA-o2KwOo7iVGJEURAow_mijuJ1uisloQchDTW0AsHOnY9KxHhHwBsFNCXWoB36zRIB4itO0KvPeMX-y2Uliva-n-AKlaCX05qpZcNQHeYOfcRhj-Ut_d99u4L5BOusOaK5jL31c4rJy1eJXMUV-1mS3KviigNdFoVAlEWS3VNzsWw-s8y5Y6SRT-MSPfSyLoMBqkvtXxOzRRxuVDNhoywNWp0W03-N5PLKOvG1ms6r6odYA-33-JZ1STTFxn5fBcA2yuHE7ME9JAPvMwsYzwAwAHNIBT-1lCtj4wEOj7lYy87vwUkrtfSujP416lraNdSbmTbtNAi4XFpC9spyngmYpA4DnZO2zijQP7YEU3Ao3E4zfr0faaNGRvvrpz3Ddc6VEeFZaScIClJ1CJOdJQspEv1LD2VbtNOLgkIIkcg6OJUvMIEU-JExnMRO2HzGnalZfvc2fBR59pBMO47MI3UYRlBrHo59Ii1_ziiAL7BMbnKXkRqWL6XbqcgmYa8xuRR85q0Ls8irU8ywGoHU4PQ12LVU9lOiEV5n3LC1qp8c68iYIPo8e9c0Ar73NRrbwdO5WNFLERYBJZYc0xmJPihk3IDpsDOLym3DNviBEzCZfsz2_7ia5KGQ7c8uJT3YYg1fnoy_OKqYBAPe4HyxFlzAcOx9p-1ILc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269183605e.mp4?token=qjbsr9tjTpQA-o2KwOo7iVGJEURAow_mijuJ1uisloQchDTW0AsHOnY9KxHhHwBsFNCXWoB36zRIB4itO0KvPeMX-y2Uliva-n-AKlaCX05qpZcNQHeYOfcRhj-Ut_d99u4L5BOusOaK5jL31c4rJy1eJXMUV-1mS3KviigNdFoVAlEWS3VNzsWw-s8y5Y6SRT-MSPfSyLoMBqkvtXxOzRRxuVDNhoywNWp0W03-N5PLKOvG1ms6r6odYA-33-JZ1STTFxn5fBcA2yuHE7ME9JAPvMwsYzwAwAHNIBT-1lCtj4wEOj7lYy87vwUkrtfSujP416lraNdSbmTbtNAi4XFpC9spyngmYpA4DnZO2zijQP7YEU3Ao3E4zfr0faaNGRvvrpz3Ddc6VEeFZaScIClJ1CJOdJQspEv1LD2VbtNOLgkIIkcg6OJUvMIEU-JExnMRO2HzGnalZfvc2fBR59pBMO47MI3UYRlBrHo59Ii1_ziiAL7BMbnKXkRqWL6XbqcgmYa8xuRR85q0Ls8irU8ywGoHU4PQ12LVU9lOiEV5n3LC1qp8c68iYIPo8e9c0Ar73NRrbwdO5WNFLERYBJZYc0xmJPihk3IDpsDOLym3DNviBEzCZfsz2_7ia5KGQ7c8uJT3YYg1fnoy_OKqYBAPe4HyxFlzAcOx9p-1ILc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خواندن تلقین بر پیکر نوه خردسال آقای شهید، زهرا محمدی گلپایگانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/669357" target="_blank">📅 02:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669356">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پایان بدرقه تاریخی؛ آرامش ابدی رهبر شهید در جوار حرم رضوی
🔹
پیکر مطهر رهبر شهید، حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای پس از عمری مجاهدت و جانفشانی در راه اعتلای دین و سربلندی ایران در جوار نورانی امام رئوف حضرت علی بن موسی الرضا (ع) در مشهد مقدس آرام…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/akhbarefori/669356" target="_blank">📅 02:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438841b458.mp4?token=gusqvHVuTTWbUSsERBJ7U8poEousq6at7s1Ov3JgAe4Z8MJtdbIBT77exUimMeuOb3uFCr02CE3AFfAE7ScpVqLpqL15YLiBngW9eAySkjnO3_DEeSt7Tqz4UPQQmuxFwUdPRHCko7A_HWeFmRtejE6ooa5qE3_NBy-YnuK0E68V-YSHwox1eLT4TVdEhNCy5TsloVc6q6QVGaudho0HoVBnCC9GIk0JQwIYe64dFf2yQ7KlYTckvtrcLSVXaCZV_3s5DIFhIuFMyfOAOlUqCAT6o8kkG2gYIeG4V6umyG9KOcCHMvT9nAb9n32yRjm-sImRWix4F36WIhIMaPqvGgv1O9h8GjQJjABs_4jk5pfCK25NfqklC1geEiZNFDJxIZZ-n7RyKaAiIm8QRVYEFmM1BRUtRW4Vng--eIS9MOxhOb0s0S3Yxh9ULPWUP43MsCImAs8SXMziHzcuvqBbDzRpzv09o3vYoz0cEuZPnmeclc3XD4sy4cTYc5fFV4AMHJrlDYgfaB1NapL0Uii4TnLjLOIA_OCBQxtuihnhy74v5ggCX2hbx5m9mQLf763KMUCsDXdyZTcKdnuQlvb90by4hNfKKmNfFqYzK7fL4iH8OVvthQHK7Uq8Yeze3vPRP-rJsfmtZal1ZToNnDz1r_qf156ynMHAf-Hi4ApvC3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438841b458.mp4?token=gusqvHVuTTWbUSsERBJ7U8poEousq6at7s1Ov3JgAe4Z8MJtdbIBT77exUimMeuOb3uFCr02CE3AFfAE7ScpVqLpqL15YLiBngW9eAySkjnO3_DEeSt7Tqz4UPQQmuxFwUdPRHCko7A_HWeFmRtejE6ooa5qE3_NBy-YnuK0E68V-YSHwox1eLT4TVdEhNCy5TsloVc6q6QVGaudho0HoVBnCC9GIk0JQwIYe64dFf2yQ7KlYTckvtrcLSVXaCZV_3s5DIFhIuFMyfOAOlUqCAT6o8kkG2gYIeG4V6umyG9KOcCHMvT9nAb9n32yRjm-sImRWix4F36WIhIMaPqvGgv1O9h8GjQJjABs_4jk5pfCK25NfqklC1geEiZNFDJxIZZ-n7RyKaAiIm8QRVYEFmM1BRUtRW4Vng--eIS9MOxhOb0s0S3Yxh9ULPWUP43MsCImAs8SXMziHzcuvqBbDzRpzv09o3vYoz0cEuZPnmeclc3XD4sy4cTYc5fFV4AMHJrlDYgfaB1NapL0Uii4TnLjLOIA_OCBQxtuihnhy74v5ggCX2hbx5m9mQLf763KMUCsDXdyZTcKdnuQlvb90by4hNfKKmNfFqYzK7fL4iH8OVvthQHK7Uq8Yeze3vPRP-rJsfmtZal1ZToNnDz1r_qf156ynMHAf-Hi4ApvC3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش صدای خواندن تلقین بر پیکر امام شهید ما در حرم مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/akhbarefori/669354" target="_blank">📅 02:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZC1UzypNHRMyyuNFyhfRk3GMKdxEKrXtzTXIGRpndU7BzVwghtD_-OvWiJ3oiRecqUVLgfc0CRPQXj7LULb3B-UKCqUex7tYKq2eo2bK80Xp_J0NgveUEQFqitB6hLiqnu9a5UjZOQCxwYMzH6GJXKOzcmvUGnIpG9xSFPD26LO_6SfbtbaOnJqTOSW2xvRUspbhO63rkUJJjEiuL8rlplTSzHQdZjKSIcd84dh1AZkWcLPydWt3gi67bF9qyl1K2s_g-MT4yBHbLkYBLmP6KgYYxUOJu2FRKB8AFNtNcpnDearidgrJzweJmZRiXzbYoZILApm2mDmbWna1mNXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار پاکستانی: ایالات متحده و اسرائیل تمام تلاش خود را چه در بهترین حالت و چه در بدترین شکل به کار گرفتند تا جهان اسلام را دچار شکاف کنند، میان اهل سنت و شیعیان اختلاف و گسست ایجاد کنند و از بسیاری دیگر از نقاط اختلاف بهره‌برداری کنند؛ اما در نهایت نتیجه معکوس گرفتند و باعث اتحاد همگان شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/akhbarefori/669353" target="_blank">📅 02:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6367522cf0.mp4?token=APzWv_uedVh00gwDZ__nSqHt9w6FIaTcjFoel-dNCig2rsgCLJbdHv4dumj6_VAvVmxYDaOGarctub71vD2tnSMz2IM2_-JAZfachCY9KB96qw7KhY3qr4mIuVX1vQWZa7QwtcnzDOeMdenlnYiwY9Yxnhh7njIuQ71PjYNASPWVLByRHfXf69zIDC5xbaId9AR60tJo1U2Pbn-Lc3akw4dHD0DYb8dTesTYW0geai-W0TH12zvmj0N0-reV7YrpTMSVXgQKECHvJ7Nl-s6MtEuu1hmPXxGudiU8GFP4x4lg7eS-OuimgghKJcA_iISRpKG6BLwPW5DtPe-k1SdHdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6367522cf0.mp4?token=APzWv_uedVh00gwDZ__nSqHt9w6FIaTcjFoel-dNCig2rsgCLJbdHv4dumj6_VAvVmxYDaOGarctub71vD2tnSMz2IM2_-JAZfachCY9KB96qw7KhY3qr4mIuVX1vQWZa7QwtcnzDOeMdenlnYiwY9Yxnhh7njIuQ71PjYNASPWVLByRHfXf69zIDC5xbaId9AR60tJo1U2Pbn-Lc3akw4dHD0DYb8dTesTYW0geai-W0TH12zvmj0N0-reV7YrpTMSVXgQKECHvJ7Nl-s6MtEuu1hmPXxGudiU8GFP4x4lg7eS-OuimgghKJcA_iISRpKG6BLwPW5DtPe-k1SdHdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین ز خیل ملائک حرم پر از صف شد
علی‌ست زائر مولا، «امین» مُنَجَّف شد
🔹
قاب‌هایی از تشییع پیکر رهبر شهید ما در حرم امام علی علیه‌السلام
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/akhbarefori/669352" target="_blank">📅 02:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
روضه خدام حرم امام رضا علیه السلام بعد از تشییع پیکر امام شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/akhbarefori/669351" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2757dbcfa9.mp4?token=VbGWI7lY9gRvrXwqm82u5D-pkfwYIgEiKjcMaAN_khW9BANpLmB6-ZLFZksjq2e9an4ImEqFc95WZ-AglE_-9YXJh4RFTHoR__3NCQzFP3MDFBW4d8nXBMp7kujn8rRMwkoO549o3uNlVS8vVEAuxWB6uCcMuEEJy5uvKw4LvktjQruTSG4NwtRmUN65526YQSGDZ-jVcBL6pLPTYqE-SCHw1-38QXzo6eojOpLtC12RCyRPE7Hvcu-kxDhqjCIvF-5LFkK1RV63yVaxfJcmAE1TnX4pZgy61CMugHm7OQqLeqCgpk0nA1Ay7AOGHmsYaTXNa3IYNg4smWTHyBLhHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2757dbcfa9.mp4?token=VbGWI7lY9gRvrXwqm82u5D-pkfwYIgEiKjcMaAN_khW9BANpLmB6-ZLFZksjq2e9an4ImEqFc95WZ-AglE_-9YXJh4RFTHoR__3NCQzFP3MDFBW4d8nXBMp7kujn8rRMwkoO549o3uNlVS8vVEAuxWB6uCcMuEEJy5uvKw4LvktjQruTSG4NwtRmUN65526YQSGDZ-jVcBL6pLPTYqE-SCHw1-38QXzo6eojOpLtC12RCyRPE7Hvcu-kxDhqjCIvF-5LFkK1RV63yVaxfJcmAE1TnX4pZgy61CMugHm7OQqLeqCgpk0nA1Ay7AOGHmsYaTXNa3IYNg4smWTHyBLhHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به امید دیداری دیگر...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/akhbarefori/669350" target="_blank">📅 02:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b553e0cb.mp4?token=ToAnon5rhp_8UTHERJjG7Lvu-HtEj1Id2vKyJSglvPL8n9nhlYXBOkRvtvwrdic_AMbXS14us-6zhfQB1vusrY1AJnExXq_X9-WaCosWWreMEZt83LNyzJFP7ASEa6v_6Yai_IbQYvQkKojOxJQThScAMKqtHbN1S5RswN9QMEINZrcUJCTPvN3DExbYzdTpK5nwrOyAT29rCv8-C_atsCAOT5bKu_RxPzn2-60KfRVsvpJ2rPPogw_mPtR0gpLQH4f_uv5C7A-B8RuC7jeieAKEfKEukybK2wapKnb4g96_05zXLjYe3yfQzkrZYAC0D_1I306mwVwWR0UnQhc62Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b553e0cb.mp4?token=ToAnon5rhp_8UTHERJjG7Lvu-HtEj1Id2vKyJSglvPL8n9nhlYXBOkRvtvwrdic_AMbXS14us-6zhfQB1vusrY1AJnExXq_X9-WaCosWWreMEZt83LNyzJFP7ASEa6v_6Yai_IbQYvQkKojOxJQThScAMKqtHbN1S5RswN9QMEINZrcUJCTPvN3DExbYzdTpK5nwrOyAT29rCv8-C_atsCAOT5bKu_RxPzn2-60KfRVsvpJ2rPPogw_mPtR0gpLQH4f_uv5C7A-B8RuC7jeieAKEfKEukybK2wapKnb4g96_05zXLjYe3yfQzkrZYAC0D_1I306mwVwWR0UnQhc62Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار ما به قیامت آقای آسمانی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/akhbarefori/669349" target="_blank">📅 01:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2RA-lIcp0e3_WiziDkqsMC0JT_EWDBcdUjn8IwdlSWhOnmahY0qTqphvCJsO_H9gIfp6cGy_6xMY16iHJ-6XmeskdK5pygzenzRFpVuoJ2vb3K9SiF-2r3VeNmcMpvJub54L0kjvRPo0ttvZ2GR1s4FCrERMPpJTLGzcNF-fHwZkTn0ez3II9OViPbyVz-6CZoc-6D9ZdyML12-tdiTs2OE9TFk5tOfJvyf3EsmMbXLG87Wrp1SBDGDGMLvFSYsoLbwTG1EoG4Iq6jbgqpIEYwmveY5JlUGJ2lj0kCO_9mR93Uf4oUNkk127ZFpJc7Sle72mdJzU8K6bu9UwcgQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۱:۲۰</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/669348" target="_blank">📅 01:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb2e3a97f.mp4?token=ka0-Ir55R2YmY1uOiM02Vi_wk3Jo8-llZhVeB7HwBGI4dWfLiCpFjXnRwUz3NKk0H2e93-M4YW-WyWNxsRGMQgq7Hx2b_Y1Ka8S9M_lz0K2YozMcRdFql4tfF6IOCZKi8tLssubFs3QvFJDWMhwgKhN1uHc8LmTaoUOKftmFaa08ByADkihZnj8t3AYe3sAooG6Wz5IiQ6fopux3pF4D_FMzWv0H37KB-I0TScRkFvvJBBS8_H6qZq6UYvYOAcF5xW5CgpuGJq-BE4Sbcapnva3S7NbZOOj12RyPddg3cxhpw0eD7CrTiI60UCjiPndUKnMxxUHsmGRQuqjvGWh6OFkI-6Wc734zqW42jY1t2QsNaNzdsZviafqK_FknadJtKYZhZGWL8DvGSGx06rkGXgMZxlhtBgFl2-463wUVByO_MD13O7m2OosjNuat1qTaGd1rkcN_4Gw03fcNsCyNaLRrhyKriqqaXMcKAiyu__zC0GpTMTunGjFxOKL8Gm9m906JeC8UOkn5A979j93NZhZK_wI3vi4THii5AQFrbocOcKjztePHkxz8ARgPkJg-heSJpOORj4BXdzVPFVDrgLJQBpgnaoho7qattbEobS7bUD8oVCtskNPHJju8ZHnXhgMSbv6D54JPsHjMwdtsVIUd2FY6YQ5EPnNMmEx6kKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb2e3a97f.mp4?token=ka0-Ir55R2YmY1uOiM02Vi_wk3Jo8-llZhVeB7HwBGI4dWfLiCpFjXnRwUz3NKk0H2e93-M4YW-WyWNxsRGMQgq7Hx2b_Y1Ka8S9M_lz0K2YozMcRdFql4tfF6IOCZKi8tLssubFs3QvFJDWMhwgKhN1uHc8LmTaoUOKftmFaa08ByADkihZnj8t3AYe3sAooG6Wz5IiQ6fopux3pF4D_FMzWv0H37KB-I0TScRkFvvJBBS8_H6qZq6UYvYOAcF5xW5CgpuGJq-BE4Sbcapnva3S7NbZOOj12RyPddg3cxhpw0eD7CrTiI60UCjiPndUKnMxxUHsmGRQuqjvGWh6OFkI-6Wc734zqW42jY1t2QsNaNzdsZviafqK_FknadJtKYZhZGWL8DvGSGx06rkGXgMZxlhtBgFl2-463wUVByO_MD13O7m2OosjNuat1qTaGd1rkcN_4Gw03fcNsCyNaLRrhyKriqqaXMcKAiyu__zC0GpTMTunGjFxOKL8Gm9m906JeC8UOkn5A979j93NZhZK_wI3vi4THii5AQFrbocOcKjztePHkxz8ARgPkJg-heSJpOORj4BXdzVPFVDrgLJQBpgnaoho7qattbEobS7bUD8oVCtskNPHJju8ZHnXhgMSbv6D54JPsHjMwdtsVIUd2FY6YQ5EPnNMmEx6kKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بله، وقت تمام شد...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/akhbarefori/669347" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYigegoSYjOUo2SoHi0tS7eYHtkj3_F5uynqtVaSr3ikIhE0FRH0HxLuLoH6P5QMR1SL2Xu8-KxTKE9W54OGy79cVuoDqiEZ75iBeCuireRuHoGJV4QrVD7X-GSNgjcCU5bi7V729KUX5p9gNbtWa_PLJDh9S97KzKMBxGS7BxG514WdfIFdk_IVsKJ7gIUKskwpR1L003WugbTzaEeauk4ZV4P-H8FocWWAHCUB7plNPxs4R2A16W4kR-FTdaqNF8S-dzRfBDBu11BHWzy5kGgMvbjkUicAVh4XzpfeewkcdGjA4KF-g0MUF3bs6tPOLUTfZIT_gc398TTUUuABnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینک شما و وحشت دنیای بی علی...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/akhbarefori/669346" target="_blank">📅 01:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91faf2a0b.mp4?token=EdODjygXCrcfLlhHmpdLkGsgMPUeUIUviuPMaa5tBvNUd2YToNdicx3OvnpR1D1-p253nM54yu1brpNrP3t5VOQBqirsEDj_b8hZyKIIKwJYAzyfMYt1nw55P0yXIcU6Q1amvjPPSM7glZle5WA-lsKhB-zf1j6NJtY8l4QY7L7seqhPczeaFWKGwmTWwmltUmSoc3gHZ9lLV3SEPEMFBaZenWNKTh6JqyeylZ4WgCl5wP57HEdncftzwyh7mqeJABLKo77TIyBIcbSNtd7rWtTa9IwexR2dspmM75kyftHKvEQz__S3aJVrGC7AVNYPyhM29zrRPA_-LSv5Hw6_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91faf2a0b.mp4?token=EdODjygXCrcfLlhHmpdLkGsgMPUeUIUviuPMaa5tBvNUd2YToNdicx3OvnpR1D1-p253nM54yu1brpNrP3t5VOQBqirsEDj_b8hZyKIIKwJYAzyfMYt1nw55P0yXIcU6Q1amvjPPSM7glZle5WA-lsKhB-zf1j6NJtY8l4QY7L7seqhPczeaFWKGwmTWwmltUmSoc3gHZ9lLV3SEPEMFBaZenWNKTh6JqyeylZ4WgCl5wP57HEdncftzwyh7mqeJABLKo77TIyBIcbSNtd7rWtTa9IwexR2dspmM75kyftHKvEQz__S3aJVrGC7AVNYPyhM29zrRPA_-LSv5Hw6_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در جمع خادمانت، شوری به‌پا بود امشب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/akhbarefori/669345" target="_blank">📅 01:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1iBaFDorWX67BgDbCChPAmqz8VAwU4Sn021_kyrPrsf13FD_Kaw8X2PFST3KkQwI1skkpcRv4AqGfaeuNvQ64jAG4syV7l46f34W94Td1vAymrtyWi53_sDwlxIZd88NTL-4Wp0HU-iiakfjWD-WQlACxgnseqW5RuG0-mhE_xrtNiLbU8MfAOWa3ejEJCV5VfABAnZRBNDT3QvYVsyE1lJlFHbTGropgX9V3kj_ewdndtEEgV1XrVnY73LXZcmf1q3CFm7V7EG0z3Sv3GCEaAbmYoKCMzDYC95Lg-QpFu8_WVmcGwsAxxL8KQEudWd_ySqG1LWcJQ8DwqXZz5-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروس‌ها نخستین تیم صعودکننده به نیمه‌نهایی جام جهانی
🔹
تیم ملی فوتبال فرانسه با ۲ گل کیلین امباپه و عثمان دمبله با برد مقابل مراکش، برای سومین دوره پیاپی راهی نیمه‌نهایی شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/akhbarefori/669344" target="_blank">📅 01:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">نقطه‌ای که ادمینِ کانال اخبار رهبر شهید انقلاب بعد از طواف و خاکسپاری پیکر آقا گذاشت کار صدتا روضه رو انجام داد.</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/akhbarefori/669343" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H88ZtVQtw-lHh5lNn4LeKb4huDttl1X4Xtr-lqDlCRhPy1vNMEJrpm-JjCOaoLag5XcBW6_mADEEApFTJgrkUGa7OWpaBF5rWALYUwc7yb-4yJLp27qTwc_HC2kCcWIW5r8cmdoMyOobN7Qju1mnqAeCvwgl-JPE9wwalMnVcinEWS3hJqcrNWQsMUQY19z4g7WeZtrUgmK5Ts1J1BjJT1T1tICqlY5h7n8HFlYcmx58PkbnwAHbiGRWSSuIjE4117urjqe9sVdW6oZwmd9rlhn81ESFeN8nZ2WZ4T3fwGITK6VyuoeOzeCEEP7L4nrQ_skDtsWjORtFBOWAOJjnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقطه‌ای که ادمینِ کانال اخبار رهبر شهید انقلاب بعد از طواف و خاکسپاری پیکر آقا گذاشت کار صدتا روضه رو انجام داد.</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/akhbarefori/669342" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa8a1ef2d7.mp4?token=TVR8P1Y5X3MGGsE_u-HEFvAJrmc_5NcBpMO03XqNdCV4lQIn6A3Cc6ni_-7C40cQQwBC5-DHZTHP_l3WShzFNqawtlMMg9B0rjs3SadcN9BaT67JkJmZ-hmYjEGbjUv_DFVdx9QYr4o6fDgLYlIaiyVmIV1Jeg7_wbEyO7cdzdyXrn69DhdTErD1OfblRB4qrFv01UkEVMHoO6wg6zuFJ0JcAbcRt8c-R6ESFG35bX_qY2KeNpNsTWxxTZpEp_fmqHCLw9X090quxR1NnyvmAxFOI3wLF065M3gjzwmBuUAh3UCzs1is04NHWYCZIKh1PIPl2A2P4b5_Zd316iNEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa8a1ef2d7.mp4?token=TVR8P1Y5X3MGGsE_u-HEFvAJrmc_5NcBpMO03XqNdCV4lQIn6A3Cc6ni_-7C40cQQwBC5-DHZTHP_l3WShzFNqawtlMMg9B0rjs3SadcN9BaT67JkJmZ-hmYjEGbjUv_DFVdx9QYr4o6fDgLYlIaiyVmIV1Jeg7_wbEyO7cdzdyXrn69DhdTErD1OfblRB4qrFv01UkEVMHoO6wg6zuFJ0JcAbcRt8c-R6ESFG35bX_qY2KeNpNsTWxxTZpEp_fmqHCLw9X090quxR1NnyvmAxFOI3wLF065M3gjzwmBuUAh3UCzs1is04NHWYCZIKh1PIPl2A2P4b5_Zd316iNEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکرهای خانواده رهبر شهید برگرد ضریح مطهر حضرت رضا (ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/akhbarefori/669338" target="_blank">📅 01:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: اسرائیل به آمریکا اطلاعاتی داده که نشان از طرح ایران برای ترور ترامپ دارد
🔹
اسرائیل اخیراً اطلاعات جدیدی را با آمریکا به اشتراک گذاشته که به گفته آن، نشان می‌دهد ایران طرح جدیدی برای ترور ترامپ، دارد.
🔹
خوک نجس روز چهارشنبه در جریان نشست سران ناتو در آنکارا، ترکیه، به تهدیدهای ایران علیه جان خود اشاره کرد و گفت: «آن‌ها می‌خواهند رهبر آمریکا — یعنی من — را از بین ببرند... من در همه فهرست‌ها هستم. امروز صبح دیدم که در تک‌تک فهرست‌های آن‌ها قرار دارم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/akhbarefori/669336" target="_blank">📅 01:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPbAnmg8fyOCb30ywolAn3_WmJzAE6psa6OE0giYdlNUJXQ-vMGBsmNwlE2x_wUQ5FoOwDa83CYMRjZNCWQA62z7c1jgBDf_GM7Cgm6RYbTixUytb9s157up54pE7Va-TTEwdFqr93wnTKv4G_My3NbIZFwYGPiXWf8vzgElrDvPjlZ88PwmXTJzrIlQTydyFdTrTCg9P7d7oBHw8EEQZao7hi1NVL7HpdxhjgmyDPLkK5h7EYFJKyfz78FQqpIWJupYrbFUM_xm7IpPcSuDV6-eYOS4bvew9HDHv44XPm0sliPMY4RG1plwnJaE3t3fcvB39-1Hn4zoWHE8u5utQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا دشمن، از درک معمای حضور میلیونی مردم ایران در صحنه عاجز است؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/akhbarefori/669335" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55abc22245.mp4?token=hutxpcvyNDTewHIHrAqhHD92r7Vziq6JavdiEzHmvoB7qXq8pmRtIGYBxHPS7jmPN1bVzysT5NcDJ33klYKaBGb0NRsQ5eR8IW8JcbYosSdaEwcXMOsUsdPVo-P9C8J00YHeC2M62BixtVpKFCxxgnc3vQNVYfZ7C7e71mrtbY2A3GLrJPqO5xhrsu84b2OnJbK4o86a9h_iFnZeYM4JV45FrPxppARQr1MZ3RddG2zA3y1OC9CO6eF-aXLsb4bfym2CZbDvIkMS4jeb1Vqdo6fkQ4x_1GGuE42ZTrZgs-rhZU7SoRwuMgor_onebGYtNzHDKWFQL3NfuHIRUzaqIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55abc22245.mp4?token=hutxpcvyNDTewHIHrAqhHD92r7Vziq6JavdiEzHmvoB7qXq8pmRtIGYBxHPS7jmPN1bVzysT5NcDJ33klYKaBGb0NRsQ5eR8IW8JcbYosSdaEwcXMOsUsdPVo-P9C8J00YHeC2M62BixtVpKFCxxgnc3vQNVYfZ7C7e71mrtbY2A3GLrJPqO5xhrsu84b2OnJbK4o86a9h_iFnZeYM4JV45FrPxppARQr1MZ3RddG2zA3y1OC9CO6eF-aXLsb4bfym2CZbDvIkMS4jeb1Vqdo6fkQ4x_1GGuE42ZTrZgs-rhZU7SoRwuMgor_onebGYtNzHDKWFQL3NfuHIRUzaqIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حلالیت‌طلبی یوسف سلامی، خبرنگار صدا‌وسیما از رهبر شهید انقلاب به‌نیابت از همه کسانی‌که طلب حلالیت داشتند
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/akhbarefori/669334" target="_blank">📅 01:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هم‌اکنون سوزاندن نمادین طرح لگویی ترامپ در مشهد
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/akhbarefori/669333" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d589bff.mp4?token=G6xYPIITmsk7mkSVBDFc8Zg7nW_0X8iyh0OWlPM14h6uZeec1LNFXVOuAf47zK14BR1lFS0yTU41gjAYPZFVtP3NvnK_5ONSX63wtieCrlhVNAXUjHZAmlO5j2rnyhxBaH_qfEv99LVLDLh_YvGmzaYYq7hAtb-UG6CUlTfDh3JykMMBF3eYToYxbO8gF5ZVBpqR0UW85dCO0GHHmv1ZhVyZLEPPbQovjlCWpeJGRmSCFF3tnrx_Yvmdn47ZnO-PHN7Ib97ACLwP-VsJkdTCa6964FBrXwXAeUfPhU85-A5b6or8akqXlHvz84OEHpDQ6ZA-n_2AX8GrXtr5QdHqg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d589bff.mp4?token=G6xYPIITmsk7mkSVBDFc8Zg7nW_0X8iyh0OWlPM14h6uZeec1LNFXVOuAf47zK14BR1lFS0yTU41gjAYPZFVtP3NvnK_5ONSX63wtieCrlhVNAXUjHZAmlO5j2rnyhxBaH_qfEv99LVLDLh_YvGmzaYYq7hAtb-UG6CUlTfDh3JykMMBF3eYToYxbO8gF5ZVBpqR0UW85dCO0GHHmv1ZhVyZLEPPbQovjlCWpeJGRmSCFF3tnrx_Yvmdn47ZnO-PHN7Ib97ACLwP-VsJkdTCa6964FBrXwXAeUfPhU85-A5b6or8akqXlHvz84OEHpDQ6ZA-n_2AX8GrXtr5QdHqg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم فرانسه به مراکش توسط دمبله
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
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/akhbarefori/669331" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وقوع تیراندازی در مشهد تائید شد/ دو نفر کشته شدند
🔹
معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان مشهد و کشته شدن ۲ نفر را تایید کرد و از ارائه جزییات بیشتر در این باره خودداری و تاکید کرد: «هنوز علت حادثه و هویت کشته شدگان مشخص نیست.»/ ایرنا
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/akhbarefori/669329" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344822aa12.mp4?token=OXga43IVlOzSZ5mfj2SXKRqA-3mDlm_zcMr3egv1Tuogh62-zF-1h9NtQfkeCdI4tl1RtlaoMeEfo4PoS46ub5RPW-CSfgugB5xetm4Xc07yTexJl62LU4Fu26ANqHgnX2k-XsZy_SKJhKD-zddadscp07ogv4Qz5Ubk8CpDdZfZ68qrjjxtcxO2tWTJ2b2tAv8GBmEvZDz5FeXqnQVGeM1y99IPUzUlwaUiJ9kAoRpygLwJZaWBfl5KgYMmTF6f3UHLTWoKCZsauRebe0e_vudJuZC8-o2Y_VLMWJaZofv1OzslFTl0jwNMxAlUFhHE55R6cwh8uPzYC09KUEM7og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344822aa12.mp4?token=OXga43IVlOzSZ5mfj2SXKRqA-3mDlm_zcMr3egv1Tuogh62-zF-1h9NtQfkeCdI4tl1RtlaoMeEfo4PoS46ub5RPW-CSfgugB5xetm4Xc07yTexJl62LU4Fu26ANqHgnX2k-XsZy_SKJhKD-zddadscp07ogv4Qz5Ubk8CpDdZfZ68qrjjxtcxO2tWTJ2b2tAv8GBmEvZDz5FeXqnQVGeM1y99IPUzUlwaUiJ9kAoRpygLwJZaWBfl5KgYMmTF6f3UHLTWoKCZsauRebe0e_vudJuZC8-o2Y_VLMWJaZofv1OzslFTl0jwNMxAlUFhHE55R6cwh8uPzYC09KUEM7og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به مراکش توسط امباپه در دقیقه ۶
۰
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
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/akhbarefori/669328" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای جدید سنتکام درباره تنگه هرمز
سازمان تروریستی سنتکام:
🔹
ادعاهای رسانه‌های ایرانی مبنی بر اینکه عبور از تنگه هرمز فقط از طریق مسیرهای تعیین‌ شده توسط تهران مجاز است، نادرست است. آمریکا در هفته‌های گذشته مسیر جدیدی برای عبور کشتی‌ها از تنگه هرمز پیشنهاد داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/akhbarefori/669326" target="_blank">📅 00:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
علت عدم حضور آیت‌الله نوری همدانی برای اقامه نماز امام شهید
اطلاعیه دفتر معظم له:
🔹
با وجود آنکه مقدمات حضور معظم‌له در این مراسم مورد بررسی قرار گرفته بود، اما با توجه به ملاحظات جسمانی معظم‌له، بُعد مسافت و فراهم نشدن شرایط لازم برای انجام سفر، حضور ایشان میسر نگردید.
🔹
همچنین چند روز پیش از برگزاری مراسم، عدم امکان حضور معظم‌له اطلاع داده شده بود. با این حال، متأسفانه علی‌رغم اطلاع‌رسانی قبلی، خبر حضور معظم‌له تا ساعات پایانی مراسم در برخی رسانه‌ها منتشر شد و موجب بروز برخی ابهامات گردید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/669325" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669324">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46229c7a7a.mp4?token=MtMXPSDP4tatyVWgIDTH7yuFQM_L9DjE6cNqKG7Or88ivMTHvkNaLFRq-qRiTkuGPwgbR8d-ny790kaTu4n7UrgzJ9f3FWlZUcjsxSuLWbzoOP72fhSwNe-9A7pgJmjrbE7MQ5cxuHOg3wmdIRh8Uxyd0E0sBgjD_3qHjCLNJjtuKZgbqTzHclcEtIW80WTnO9S1xCRgzHTmF0YQtFdMDGpmT8SmMLCwMEvzwgzJ-VPxVrfFRqt_dlaEI4jtsUz1jKy9VzWUUvXV-h_xkLjKsMzfoHEPZV9hsFkS4QLv6OIloNYMRsFuh7fayhPs_plAHUhfog69ioJNdDplqzK5oE94asqa9b1cX0AXU96FaU_-cvhlrYSnR0WDNSn4tGrsq-N_lcZFr10jrqEaqYeeYWeL_p0eZGl-xEQopIKBOUPkgiNCLpTWMl_eKpWH1MkK5fzSpGa8GbdF94obuywWXRLCu9oIn-4Vod9yhn_81-iUtKx03DhLNILggME-451U8a10uRr4V9wThuzGxOBHnynY7_TGgDTHESNoNerXNECRQXub7oCyNRNpHX4NbpKnTLf46X5MWt7OFuDkY8hrsqDJskFtiKPuj9MeBztw6UPiWvg2qwcIXi-OHo0yF_jHDxYlzE3jY0bch9vIFvx-cQKad9XPT4n5iLfdOCmf5eM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46229c7a7a.mp4?token=MtMXPSDP4tatyVWgIDTH7yuFQM_L9DjE6cNqKG7Or88ivMTHvkNaLFRq-qRiTkuGPwgbR8d-ny790kaTu4n7UrgzJ9f3FWlZUcjsxSuLWbzoOP72fhSwNe-9A7pgJmjrbE7MQ5cxuHOg3wmdIRh8Uxyd0E0sBgjD_3qHjCLNJjtuKZgbqTzHclcEtIW80WTnO9S1xCRgzHTmF0YQtFdMDGpmT8SmMLCwMEvzwgzJ-VPxVrfFRqt_dlaEI4jtsUz1jKy9VzWUUvXV-h_xkLjKsMzfoHEPZV9hsFkS4QLv6OIloNYMRsFuh7fayhPs_plAHUhfog69ioJNdDplqzK5oE94asqa9b1cX0AXU96FaU_-cvhlrYSnR0WDNSn4tGrsq-N_lcZFr10jrqEaqYeeYWeL_p0eZGl-xEQopIKBOUPkgiNCLpTWMl_eKpWH1MkK5fzSpGa8GbdF94obuywWXRLCu9oIn-4Vod9yhn_81-iUtKx03DhLNILggME-451U8a10uRr4V9wThuzGxOBHnynY7_TGgDTHESNoNerXNECRQXub7oCyNRNpHX4NbpKnTLf46X5MWt7OFuDkY8hrsqDJskFtiKPuj9MeBztw6UPiWvg2qwcIXi-OHo0yF_jHDxYlzE3jY0bch9vIFvx-cQKad9XPT4n5iLfdOCmf5eM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکرهای اعضای شهید خانوادۀ ابرمرد شهید تاریخ به دور ضریح امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/669324" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc94faed.mp4?token=RVMV_1SauXiDsVz_Vcmu1YwfAibHWUvfMMiSIx9DGCVKnGKmER9ByvFgg4iyMM2w65bzUB-SoOpMoDD_pvqq_NA8_1jQ2rm-jznNu3m-rE7lLyUSew80TyFFuNE6EvbBKY3hUTtiseYvUNVmjURE85Fp7ascNtj5hsHzOC0zKAyV9gp1T60KFcYAScdrlH9_KqoESFfNosz4Ae0iCTV-2NVDAmw5cjpwIAPYe2vZThSEQYVyPHyht1RRDeipbfwNdJt3Exal1SAgdHA1uK2cVeeJRMgECdpIdnt4MuSVcSonrNPaNGcQ5yl1iyhohclTwmYbW3cILIwZYHOLAQa3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc94faed.mp4?token=RVMV_1SauXiDsVz_Vcmu1YwfAibHWUvfMMiSIx9DGCVKnGKmER9ByvFgg4iyMM2w65bzUB-SoOpMoDD_pvqq_NA8_1jQ2rm-jznNu3m-rE7lLyUSew80TyFFuNE6EvbBKY3hUTtiseYvUNVmjURE85Fp7ascNtj5hsHzOC0zKAyV9gp1T60KFcYAScdrlH9_KqoESFfNosz4Ae0iCTV-2NVDAmw5cjpwIAPYe2vZThSEQYVyPHyht1RRDeipbfwNdJt3Exal1SAgdHA1uK2cVeeJRMgECdpIdnt4MuSVcSonrNPaNGcQ5yl1iyhohclTwmYbW3cILIwZYHOLAQa3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوهٔ ۱۴ ماههٔ رهبر شهید به آغوش امام رضا رسید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/669323" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab92d02555.mp4?token=neP6w4lkr7vF3DRu8PNax76QdgErfhMudyGdFmuw3ImrDJ1KfkDoOihkeleFB88Ld011r0Ll9EizdQlHQOijqI8eQuPg_gzZfpXldWeMgQkx0gDTlbFCuQIqEOO8JM6EGlPVQ-hrhfnulCL0KfhU7vu-_58dqy4h4IO1u5SKTVBaflCfK-Tq0YYegVJ3NTue908W8uzPOiL6TfXX_qLNhAc4fxQwQWo1yadUypMPR_EN1TuJyDDT9rmJ9C06-QuNtHXT6d4NW_dBEd0waFOjzTS6PJ3eYff8JxJ3W47UgkZahr_XG6FJ9dXtPbUBoZIXabj9fwipp-_QIB069K_b8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab92d02555.mp4?token=neP6w4lkr7vF3DRu8PNax76QdgErfhMudyGdFmuw3ImrDJ1KfkDoOihkeleFB88Ld011r0Ll9EizdQlHQOijqI8eQuPg_gzZfpXldWeMgQkx0gDTlbFCuQIqEOO8JM6EGlPVQ-hrhfnulCL0KfhU7vu-_58dqy4h4IO1u5SKTVBaflCfK-Tq0YYegVJ3NTue908W8uzPOiL6TfXX_qLNhAc4fxQwQWo1yadUypMPR_EN1TuJyDDT9rmJ9C06-QuNtHXT6d4NW_dBEd0waFOjzTS6PJ3eYff8JxJ3W47UgkZahr_XG6FJ9dXtPbUBoZIXabj9fwipp-_QIB069K_b8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه محمود کریمی در فراق رهبر شهید و گریه بی‌امان خدام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/669322" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyCKgxIjJGT4h0fvvONkSx2RD5iyUzqBz4VQmVJILRshsHg4lRY-XOvOUpdrSoBwXaV4b-MHVoiwgkTIYFNVt3fY1TO4iG_yDe_1p8vt0m-v0TWj_foGxXtTlzGzoZPsaLNKqd2l_zsDtkjJq9Q_Jb4VGuhOSabpoo2ylXrxVYXbbPW1dNlAJ2xP1sN-0OQprn64KVAgLozbIAyyUNevbeOsJu3op3e86Xk0E4298M874ZLDCtTy7QE9AMg6uLOBOAB5gsilHQ4Zzxhgmb2j-KonXt4IxLjC206ryrUBYJg1BFWDkSNPhYPl_vZtXbxHIEqdhpV2qEoQLqoDQFxcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رزمندگان پای لانچر به مردم: خدا را شکر که جای خالی ما را در تشییع امام شهید پر کردید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/669321" target="_blank">📅 00:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqIUe8_POMDzUQJo6SitEMP2wvylI4VTHKOw5LLXAcytBFDElELapbMrcDrmQOe_NLqgTxqpyrcuTwrxBfiXI0chjN1lhs1DqCkkHAnyUZci8XK57X2iGOy4Nv7aLZpthbwnrFd124gv7wULV6fOBv7-P_7UOs1hdZ7Ula1f_V95WTfiNhzeW-u1hJEZ7eITGkfi2guEGFy0D5ySeCDPLkxDwcxVhhEj6wnfw9df4x-CH7IdWSSlG82Bgq5CyULpCgbc2fCR7LMCTtE9FkwfRhb9EfWbRM4l9k5CO444HQ4EptJZVSkA7-vlSEW0phctVGLRBpBDvWXXj8mrUp0KeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید در آغوش امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/669320" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9Dicrh-fcTGoUukM4HTrqogaMWj3RRiJOJ84oeBVtqt6pGj6o51cfx47oNm457rzjTw1TT0kIfh5h_BXW6KJW_KDn6tiE5C0Ku7W7C-Tk06Ss8S-5lb_uEMuCJKkhPFbiDxv06YpPc9g0XW6ipishwffmu66Bx8AF4AQkGmUFY1adXnInPQjvmZUPooaw6jxLyOI7rCPr2kvvHgHWAgy_-8SitTxpczg6RIyKXx-Yk6BQKnalcsaweEBJAatqR7635YhV62Zq_G6gw9evmFfyKpOd6yW3ij3r0UCi5AI7pFq-_RgS_HVebRKBpVr0a7JrhfXVr74VMUW44AT8A4ip4IOx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9Dicrh-fcTGoUukM4HTrqogaMWj3RRiJOJ84oeBVtqt6pGj6o51cfx47oNm457rzjTw1TT0kIfh5h_BXW6KJW_KDn6tiE5C0Ku7W7C-Tk06Ss8S-5lb_uEMuCJKkhPFbiDxv06YpPc9g0XW6ipishwffmu66Bx8AF4AQkGmUFY1adXnInPQjvmZUPooaw6jxLyOI7rCPr2kvvHgHWAgy_-8SitTxpczg6RIyKXx-Yk6BQKnalcsaweEBJAatqR7635YhV62Zq_G6gw9evmFfyKpOd6yW3ij3r0UCi5AI7pFq-_RgS_HVebRKBpVr0a7JrhfXVr74VMUW44AT8A4ip4IOx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر رهبر شهید روی دستان خادمان حرم امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/669319" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fc6307b0.mp4?token=szEj-iINWz6R4XAu6GnzdYR6nmoNE9PscxIiZatYzlBrR334BVS7rvA8p4kiy8Bz4ZEyv4qbk-CY0mlslcJ60JGANUIzzkOZXm6FWtJOoRmy7dA5SC8LKzdZOQlvqAqGwnEuGlpVvOTNIuNyA6wsfwBO93gaxhekbGnOsjjhWQ_qpoePsR9ZREIJ3HQaNMJUkBe92cunmaNqnBIkmfXKKBD6k8z9AKqtopvLG193NujJ70C77ObTddTxfyekvLYdI_HAZ1M-dar2eA42AnefjoFk8JuTCqdZdfknnvxk5G3JswCwEs-ePzNlvzd4B03TUxRJ79G_mcsLmQUtoniTYgbXncuntwrADWUHxjlwtGmag1Ukha6nfJPTLXk8qHWSC7QpQQA_jGN86Cb47VuPhK4Z0TO91vf82kv7AXN8UTbP_EiH9wj38Y-jVf1l7R8ygOYXWQNcy7yeKuLfCjbOkeJSgFk_93ixuQhqlkWuI7wHSaGmfqu3JEkyvBjjpn72bT4wXaufBDzhSTKY6y5T50rNMHjjkDz63o1Z9KnqzHXsKWHssJCH0h2fIjrybsD3nDVtJMhClw25QOaBSwWZXP-HrOJ3_S2ugFxHSOgt7dm2kgSeoaojPe-97LDpuoz3qEbfKWB4sP9vkFHZLl6_YfFZnhTWUWQmksFBfON_Z3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fc6307b0.mp4?token=szEj-iINWz6R4XAu6GnzdYR6nmoNE9PscxIiZatYzlBrR334BVS7rvA8p4kiy8Bz4ZEyv4qbk-CY0mlslcJ60JGANUIzzkOZXm6FWtJOoRmy7dA5SC8LKzdZOQlvqAqGwnEuGlpVvOTNIuNyA6wsfwBO93gaxhekbGnOsjjhWQ_qpoePsR9ZREIJ3HQaNMJUkBe92cunmaNqnBIkmfXKKBD6k8z9AKqtopvLG193NujJ70C77ObTddTxfyekvLYdI_HAZ1M-dar2eA42AnefjoFk8JuTCqdZdfknnvxk5G3JswCwEs-ePzNlvzd4B03TUxRJ79G_mcsLmQUtoniTYgbXncuntwrADWUHxjlwtGmag1Ukha6nfJPTLXk8qHWSC7QpQQA_jGN86Cb47VuPhK4Z0TO91vf82kv7AXN8UTbP_EiH9wj38Y-jVf1l7R8ygOYXWQNcy7yeKuLfCjbOkeJSgFk_93ixuQhqlkWuI7wHSaGmfqu3JEkyvBjjpn72bT4wXaufBDzhSTKY6y5T50rNMHjjkDz63o1Z9KnqzHXsKWHssJCH0h2fIjrybsD3nDVtJMhClw25QOaBSwWZXP-HrOJ3_S2ugFxHSOgt7dm2kgSeoaojPe-97LDpuoz3qEbfKWB4sP9vkFHZLl6_YfFZnhTWUWQmksFBfON_Z3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از روضه حاج میثم مطیعی قبل از تدفین پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/669318" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaLr7ayjD-ztWWXYWNJeCuv5y5ctiBMGptnoEgOw4KN5mCmB1t3fd44aUiiQe-CJGGuqOASv2yxv_DNx4eOFITE8IkpgyuDPaMdpv7G8f8qK25szDkl0tI8GaCgBP_XcenBbX7nFwe5QZozM9Yh8eY1MIUrM7W75FzUEr2WcYuLUwUCT8B5G5yPOGIwEkdn53vdfO8Yr35O0XAPayzn4t91c6pd3RSwEJeD6H3OZri-VGyDrAss2mFxQIDdmnjegP-QlawSzALZZjzZnoznRwlzlk5jodfTHbU3qpc18GJNT5mqaRGU23MJNovWCwmudBraOcSpFLTl839NL2P5Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رئیس خدام آستان قدس رضوی، امشب مهمان خاص امام رضاست
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/669317" target="_blank">📅 00:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYgqYE1_oGYwDSHoYDvVlBzbdPAggJS-t6E7NYRDCcs6aRoC0OnI_MfUpX39NYXy6w3jb_AJzFhq009_hwavOBKxNqkjKdQNoEOuWqZhec7aXSv7a_vJOvNYZtHX-6ilX8DD0a7gCBXELa6gL1J2Pb5EYuaQR0r1Cxfip0PPkzwDNN35ZmCx3lf8_c9WzAPI688VM5CDbsloRG9gb3hVf3WifNBTsUWgqtqw5U00szsUqGJR90HN0tObdKsHYtthUtq3rbaz52pVClqMLDgLUdjCjhmHqTbPhHj5POsINwCI_kGWxbfSXJ-E4Dvp41pd9uvmQiGCvzIvE5EHwAKSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور علی اصغر حجازی، قائم مقام دفتر رهبر شهید در مراسم تشییع و تدفین رهبر مسلمانان جهان در مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/669316" target="_blank">📅 00:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f920723e4a.mp4?token=Pnr8BpE3N-i6dnjSbeVljOaozw_MUQclkKuUyUxHVdoj0_VyBcTZcI8cVKzs4oLPDA2uygqDJQNjr7_XzYhxfLBlThdbxHKqkTQa4de4xrIJ_QhJ9csyIoaGXCRwSGX_IoB_xzbxmF0ePj85XwI9w4mmPaIFG730OAFprrKxNWVtrEnI_EfEFyK8niKmL5of_3mmwKclE4S2g6fDXKEsh4Irz5ILOqX45mP70m3jeCIkW7D-FqGEp_Gi0bVeXF-WNIcu9e-BmPIzJ0LOSog9NH3VJO7wPMGxglWFsquO7tNkc1GWog0olVf2Abotv47Qqpaxm0TDIWEXgIdYMJ1GBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f920723e4a.mp4?token=Pnr8BpE3N-i6dnjSbeVljOaozw_MUQclkKuUyUxHVdoj0_VyBcTZcI8cVKzs4oLPDA2uygqDJQNjr7_XzYhxfLBlThdbxHKqkTQa4de4xrIJ_QhJ9csyIoaGXCRwSGX_IoB_xzbxmF0ePj85XwI9w4mmPaIFG730OAFprrKxNWVtrEnI_EfEFyK8niKmL5of_3mmwKclE4S2g6fDXKEsh4Irz5ILOqX45mP70m3jeCIkW7D-FqGEp_Gi0bVeXF-WNIcu9e-BmPIzJ0LOSog9NH3VJO7wPMGxglWFsquO7tNkc1GWog0olVf2Abotv47Qqpaxm0TDIWEXgIdYMJ1GBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مهار پنالتی امباپه توسط یاسین بونو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/669315" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3FXIYE2aLtwZvP8ndygRl1OEpDqq4WrCh5HwEJiigg2Nk-7bX0BprBv1XpCmmADQkd26ZA0tOMHyKmQ6xy57LQgtVTuzeLmXQVB2EZpb-6eedhDFm1QGcY6rqfNKn8hMuOJWWjXjd84qc-JGpijOdhE4Y7d3AdSGiCtEsy1rXSr1sb4eNYeS2NzOr0QcU1zQ-EM-438jN7AsmWwIFobm-SYW9oY9NVY3cGjI4J1UmApi7ovsvEIdHYJz48HoEhSsg6ts804Lf8Zb58rBiW-GcE_d2gXI_Yb0cMkcJl0NmQkCp-Oynt5KKvYiKvO8UzQBJo0KjTjLblb4jk6VFvoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار | شروع مجدد جنگ و نوسان شدید طلا
⚠️
در جنگ دوازده روزه و هم در جنگ چهل روزه طلا ریزش بسیار شدیدی را تجربه کرد
❗️
این دفعه مجدد جنگ شروع بشود آیا قیمت طلا به گرمی
1
4
میلیون می‌رسد و دوباره قمیت
ملک
شدیداً رشد می‌کند؟
تحلیل تخصصی منتشر شد!! روی لینک زیر کلیک کن و تحلیل رو ببین تا دوباره ضرر نکنی.
⬇️
⬇️
⬇️
دریافت رایگان تحلیل طلا و ملک</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/669314" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3SvtjCnCo5R8iZPTiNusxgpOZj-pz6tRtH5voJTYJgA_IdmF7elDIGJujcDv9hP3Nbzhs24Kyoe25weTsrl76cXCwRC_DW_O6uB1ViAfhwyh-LVfk9fMPj0eUkFUMLU4sB-g5jaTzUbESGzixcp3hSgPGq3M87yMl66stgBDzs_7sKXU5qLBv0lyIwiRQD53NLbKASEII_XEoJ6NxYeqXl9sqX5j1gUUXa-yiSmiQoN07x58-kBWzufqLCZTsFlIen0aP9Z_HA7BH4NAj9B_bPKjxzCbVhsNUAtyU9krGLcZzwu2dJCAiM6tqqa-VUDm1Ff_InY56x3dv2iMXjaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/669313" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-text">📢
به اطلاع ملت بزرگ ایران و امّت اسلامی میرساند:
▪️
پس از مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی اعلی‌الله‌مقامه‌الشریف در مشهد مقدس و اقامه‌ی نماز بر پیکر ایشان در صحن پیامبر اعظم صلوات‌الله‌علیه‌وآله،
هم‌اکنون برنامه‌ی وداع خانواده مکرم رهبر شهید انقلاب با پیکر مطهر ایشان در حال برگزاری است و هنوز تدفین پیکر مطهر هنوز انجام نشده است.
👈
پس از انجام تدفین پیکر مطهر، اطلاع‌رسانی لازم برای انجام اعمال و نماز لیلةالدفن از رسانه‌ی
KHAMENEI.IR
انجام خواهد شد.
🏴
#باید_برخاست
🖥
Farsi.Khamenei.ir</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/669312" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
فرماندار کنارک: منطقه نظامی نیروی دریایی در دو مرحله هدف حمله دشمن قرار
گرفته است
فرماندار
کنارک
:
🔹
منطقه نظامی نیروی دریایی شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.
🔹
دستگاه‌های مسئول، نیروهای امدادی و نیروهای امنیتی بلافاصله در محل حادثه حاضر شدند و بررسی ابعاد و جزئیات این حمله در دستور کار قرار دارد./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/669311" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
عربستان به‌دنبال حذف اسرائیل از کریدور آیمک
شبکه عبری‌زبان «آی۲۴»:
🔹
عربستان سعودی در تلاش است تا اسرائیل را از پروژه کریدور اقتصادی هند-خاورمیانه-اروپا (IMEC) کنار گذاشته و مسیر آن را به سمت سوریه و ترکیه تغییر دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/669310" target="_blank">📅 23:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
فارس: اولین برآوردها از میزان شرکت‌کنندگان در تشییع رهبر شهید انقلاب ۴۱ تا ۴۳ میلیون نفر است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/669309" target="_blank">📅 23:43 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
