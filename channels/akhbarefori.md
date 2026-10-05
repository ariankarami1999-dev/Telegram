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
<img src="https://cdn4.telesco.pe/file/hORRUvpcKqnOS2mTyKrc7e9GrHLuFdESizufa5HIo79EUA5T_FV4RouRP2Pzfm7p11ISB60BJZNUjgGX66HLneswdv5u9KOyVau5V5iHF9CLt1xgW_I9Pwye1VNwAPK8bh18BIUkBu2OhdvgeT5h8xK5c1igCFs1Gr5bon35o7KujNWR-fmEh1crU4yQS3Qi8MZjiOKj8Qw9wsj1oTZnKQF8yd38uZ7Wt7XoEO0QFS7631-sqPqHNVZypAopWgySZe9WdlUGWh2l9u3jsZKm1PE_3uwn8fTxU5N70oNxx_VIVuTqHlpB5UXt8wy8SuxwCmuemRh-BwiLHTuhpiUPSA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-695739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PS4Qo0APS6nC5BBtMj2Cg-zY-nAk-P1Gdt_OKCmKjkWZIvYkO30RDPhVobHeS8lD9H4QDgWpunRueuD7EvbRwAJ9YitSD7dijQVLJ2PNOcK3TR8EJVtSgEJsf_rJxHGxGK8bOfz2XFjsX-ddw45VVyLBQdGkvBly1fWteMNYqfLHqD5b_sUi6X_Lg6DQCSjqdOIELDtRVNf-uUo0HdFTPorqEWME8TSlRKZJ3GAzcYPDhrWKUw2w9XEL7EGedGeVBS9efvlFHH5LS8xpKEdSq_TP4TpuTboc4Fhzf4nUIiS8KTR35qBpHAhtHNIniWDO94pUYLb68VJkKovivkxLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GInwWjs7R2AG4fejToO911ixZw3vS5BkUopZRBMbHWegcH6V-C8eun3ONWJG3qm9qYWk_XaNRpdXT3by2MJKsXBmgl3EyG-Si2LunfXAXDHhpWfR764TcPibkZVybtElAN3Jz9G0DuZfDylNbRvOzuDMUwiTe2vvhZB116XGmxZ0sOPJ1pHH2xZvITio0bMRA4Bgv3Y-pL3EFxfjbwwuVn0-cY9B6nbZG8j1rCcK2rWNtogOns2nrYM_B91mpybmmOx7B4bS4yXOoUoqNsD3RZOc62-lHvn6WYOvM1Sf_2xc0exoTHpOnTr-odPM3MGbaRXBRJdwUQ68Ga4xTXCMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDUfrbWXx2vQ9UVjcHStRjD13pXFKDRoZQvXK2jbptSJo3Tbd3J8pXZusgJt8zg9hyewSF-JJvA7dWz6qnXmpaoQy4sPjtYE3QJK76gDzoQugtaqTauWTwEY8w5DvMIPKWiQmvK0EeJDYmj_4Qv9qFcU8aVg2w-_3kFxlw6ZHlf3OBlUFdmQs6KqkcmZUr4aBBv90Qj6s90WraXBV0lPNUol90thBhPQyrpJYDp-C_IC13RIbVWYvAfxlHIQLn9ME_O5pbKKxP_f98A_fhdKJydXu4DXWBP-UTtenxpn3bOm7mPWJHpjHUVCwf9fX5ZlYSd4Dz0CCgwIdXSqhiAl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpfPN3CQRUoItC6iG2HRKyknCN9Xg9aLbmxHi0d13rBxpDlsa0gYGAlsHcuKF6nfcvvIIwAgDQX-kENzsI5qjSEC6g44Txkxq7v5qF-jeTOneKZm1cZ_p_W1_Ff_S0sBgqxD5ZpQQOq3mOEkj2ZiXJrxCPei-XFANfdF-QSN62O_fP6-oB2he2wbYOgaohw5Ne_4XqLO0Vnir-FXEqTJUMut7lMmDuuCrrInjoWnpBVWuV2UCVtk8yvtl8zbh-NFaSOCotb54614_gQJLLJuBEMksSRfGwElKeTeFnVvqSD-LJpvBrj9YisClNDd52XRT6Yvjc4eeUrbt6iihyFaAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشهورترین نوشیدنی ها با اسپرسو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/695739" target="_blank">📅 12:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6837aa1f.mp4?token=BLXa4CShJd1CIL1915uT3kf_5f_gIowMyeM9YghZrAeNzqZgXpuu_lCsyYXoAFlpog9IusgSUGnqmK-DYt5yZ_grV3c7r-YzaQx3cNOyfkqvTSy-V_EaCM6FHv9OxNDuFiNRHJluavVuxGZXHa34NJ5aQgC22W1Tze0f88CSH8PB-JCJdRL2EqWnB3MYuIOBWaXDIGOXONrhLKjsvFyHb2Iz_ehgN2lsiK-G7BfHbFYCaX-D4FXLar8GyzUdVuz-xdsaOMtKFkRGdnC-e8m2yRgup3HggH2QKS0x8ialRKPv5Kg5pDaVNCC_ckyf7VbKB05v-T-XJVKowPS3kFDk7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6837aa1f.mp4?token=BLXa4CShJd1CIL1915uT3kf_5f_gIowMyeM9YghZrAeNzqZgXpuu_lCsyYXoAFlpog9IusgSUGnqmK-DYt5yZ_grV3c7r-YzaQx3cNOyfkqvTSy-V_EaCM6FHv9OxNDuFiNRHJluavVuxGZXHa34NJ5aQgC22W1Tze0f88CSH8PB-JCJdRL2EqWnB3MYuIOBWaXDIGOXONrhLKjsvFyHb2Iz_ehgN2lsiK-G7BfHbFYCaX-D4FXLar8GyzUdVuz-xdsaOMtKFkRGdnC-e8m2yRgup3HggH2QKS0x8ialRKPv5Kg5pDaVNCC_ckyf7VbKB05v-T-XJVKowPS3kFDk7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای نفس‌گیر «مرد مارها» یک شاه‌کبرای عظیم را از داخل حمام خانه‌ای در هند زنده‌گیر کرد و بیرون برد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/akhbarefori/695738" target="_blank">📅 12:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq1AdsRwXbinl5wDSYTgme8CLF6_rJ2k137dVSrMRFXPpX5JNUbzhshtoKz2WmcTy0jJ55-2pGdMielKHzNff8cqXm34U0dETTNkJSyXcWO-RtIQanhiixskAwLkAsYa-WCWjMXNH17CNj9VJ345TWXv8gd5mU6XqkuV8hXMewUhaihPuNBd4LRb_mRh7udp2W_YAyrrnjqXphCtuFjv5c8me-EYny6n_80xTJ0IsLtMVsapJ4RGCJ0wU9MqLQzm3WLLmkyBkAnjIpsVB-FkwUdvm50xD08g22xcT0B0taUpVC_th_CUkZ3SFUVDzAveI15h4viZAeEYt5m8iD_y2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از زنان افغان که برنده جایزه عکس صلح سال ۲۰۲۶ شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/695737" target="_blank">📅 12:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تحلیل الجزیره: ترامپ قصد دارد حمله‌ای غافلگیرکننده به ایران انجام دهد
محمد الشرقاوی، استاد حل‌وفصل منازعات:
🔹
پیش‌بینی‌هایی درباره عزم ترامپ برای حمله غافلگیرکننده به ایران در فاصله هفته پایانی اکتبر تا اول نوامبر، همزمان با انتخابات کنگره، مطرح است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/695736" target="_blank">📅 12:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee1564c6.mp4?token=kf0h6zbyBdO2KsuBQFYii3N_cxPMp4fXGzgLOhyOSRX-FxRAXRQDXchtmnQB1MMSJ8wwERDaJnA4IrsLLxl_tZFsU6nlp3OyrNG0WYZy2L3O1xBvPrEYTCVI3mgBo4pOd-VYaBCbMDU2d5XH5iCTnNIrlcNDGRrfFW_L4Kg5XfYlMyag-kfBXWEEKR_D1f-VX0Vc2OYfjgoeUw75Shk8sZ6nLdH1UjjWoxV3F6V5YgEK6ypIl5NbwpVoZ9Ol-JUZ8kI7wrZ2fXK3iUy6zch2ribcEbTgs2TWF1CrCryVUsLy_oeYn79uu95UVsDe_zv4XV23nWSD82ex2rk6RWcdVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee1564c6.mp4?token=kf0h6zbyBdO2KsuBQFYii3N_cxPMp4fXGzgLOhyOSRX-FxRAXRQDXchtmnQB1MMSJ8wwERDaJnA4IrsLLxl_tZFsU6nlp3OyrNG0WYZy2L3O1xBvPrEYTCVI3mgBo4pOd-VYaBCbMDU2d5XH5iCTnNIrlcNDGRrfFW_L4Kg5XfYlMyag-kfBXWEEKR_D1f-VX0Vc2OYfjgoeUw75Shk8sZ6nLdH1UjjWoxV3F6V5YgEK6ypIl5NbwpVoZ9Ol-JUZ8kI7wrZ2fXK3iUy6zch2ribcEbTgs2TWF1CrCryVUsLy_oeYn79uu95UVsDe_zv4XV23nWSD82ex2rk6RWcdVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله تند بازیگر نقش هالک به ترامپ: باید او را به «اردک‌لنگ» تبدیل کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/695735" target="_blank">📅 12:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9e0c0260.mp4?token=c8pTKkWCB8g1owH20-VdJsx1HuaPJbl1pZZ5p1xyS1em9-8c_QXaUooA18GC72rqDBkxR3pFYrNSkaFZFyly50OS8OIIybsQQo1fxacw82mq67M4b5cUc2KF_8xSP2YtZl4L20xOLvTqtldlu-qGxZgoja9gq6UpVITPitsykm9jkcQciBN-NOhFjKFBI28PK5J_wYs4ianXl7l_N8SAlNsI5bROildoUfKhdffKr1PLDCXhToRGec1LLMgQBzyLQYRrTWWKKuU0Yz_JGBNEe5_r3hWZxCjdmXPjrej2hAAY61k7usamGDhwHywLfcyooYCG09hM5Y7c7_aR7nqM3TJ48Cdeh-uE1eRJ0o6m9PwmoQ5dDtLwS0r9_HhAHi1Sd4dAF8-_M8Ih-by-B8S6KMfunIHViZ_3d9QjPlli1yv0KYq4abY0hRBi4xoVMPlMJFDnLTbG90cVpQuzTWlQfngWqVRFOBgJQlp0wX8rM9GTS4o_PlX1E-sIOZuTVsRJVKEBuGa2fuL1K580DZWLndWsZQLuGLB2Y1FH2TgC5jSARzp5J0K-hmBreh205TLMvvgU0Ye_eYws02OV5IdPf9tZb4XarsZKMhBzEabTS347-Bg4zi4V9dFP9T85CTLMiL1nGWdvjPQiDwV4ybHfhZilxkDnEzkleNf9L6PimtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9e0c0260.mp4?token=c8pTKkWCB8g1owH20-VdJsx1HuaPJbl1pZZ5p1xyS1em9-8c_QXaUooA18GC72rqDBkxR3pFYrNSkaFZFyly50OS8OIIybsQQo1fxacw82mq67M4b5cUc2KF_8xSP2YtZl4L20xOLvTqtldlu-qGxZgoja9gq6UpVITPitsykm9jkcQciBN-NOhFjKFBI28PK5J_wYs4ianXl7l_N8SAlNsI5bROildoUfKhdffKr1PLDCXhToRGec1LLMgQBzyLQYRrTWWKKuU0Yz_JGBNEe5_r3hWZxCjdmXPjrej2hAAY61k7usamGDhwHywLfcyooYCG09hM5Y7c7_aR7nqM3TJ48Cdeh-uE1eRJ0o6m9PwmoQ5dDtLwS0r9_HhAHi1Sd4dAF8-_M8Ih-by-B8S6KMfunIHViZ_3d9QjPlli1yv0KYq4abY0hRBi4xoVMPlMJFDnLTbG90cVpQuzTWlQfngWqVRFOBgJQlp0wX8rM9GTS4o_PlX1E-sIOZuTVsRJVKEBuGa2fuL1K580DZWLndWsZQLuGLB2Y1FH2TgC5jSARzp5J0K-hmBreh205TLMvvgU0Ye_eYws02OV5IdPf9tZb4XarsZKMhBzEabTS347-Bg4zi4V9dFP9T85CTLMiL1nGWdvjPQiDwV4ybHfhZilxkDnEzkleNf9L6PimtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا خط لوله نفت عربستان هدف حمله جدیدی قرار گرفت؟
🔹
تصاویر جدید ماهواره‌ای از آسیب مجدد به خط لوله نفت «شرق-غرب» عربستان سعودی حکایت دارد؛ به طوری که ستون دود ناشی از آن تا حدود ۵۰ کیلومتری ایستگاه پمپاژ شماره ۲ در شرق ریاض امتداد یافته است. این خط لوله پیش‌تر و به دنبال حملات ماه سپتامبر (شهریور) تعمیر و بازسازی شده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/695734" target="_blank">📅 12:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سرلشکر عبداللهی: جنگ جدید دامن همه را می‌گیرد
🔹
رئیس ستادکل نیروهای مسلح با هشدار به سازمان‌های بین‌المللی و آژانس انرژی اتمی، ادعای نظامی‌شدن برنامه هسته‌ای ایران را توهم خواند و خواستار توقف اظهارنظرهای بی‌اساس شد.
🔹
ایران منتظر نتایج انتخابات کنگره آمریکا…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/695733" target="_blank">📅 12:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سرلشکر عبداللهی: جنگ جدید دامن همه را می‌گیرد
🔹
رئیس ستادکل نیروهای مسلح با هشدار به سازمان‌های بین‌المللی و آژانس انرژی اتمی، ادعای نظامی‌شدن برنامه هسته‌ای ایران را توهم خواند و خواستار توقف اظهارنظرهای بی‌اساس شد.
🔹
ایران منتظر نتایج انتخابات کنگره آمریکا نیست و برای ترامپ و دیگران تفاوتی قائل نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/695732" target="_blank">📅 12:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
میدری: هر روز با توطئه جدیدی از سمت دشمن روبه‌رو هستیم
وزیر کار، تعاون و رفاه اجتماعی:
🔹
شوک‌ها در بازار ارز و تورم مسائلی هستند که یکمرتبه رخ داده و ما هر روز با یک توطئه جدید روبه‌رو هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/695731" target="_blank">📅 12:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
روزنامه‌‌جمهوری
‌
اسلامی: باید به چین و هند بفهمانیم که خطر جنگ مجدد امریکا علیه ایران چقدر برای آنها هزینه دارد
جفری ساکس، استاد دانشگاه کلمبیا:
🔹
هشدار داد آمریکا فقط توافقی را امضا می‌کند که شامل تسلیم ایران باشد و جنگ دوباره آغاز می‌شود. به گفته او، جلوگیری از جنگ تنها با ائتلاف قدرتمند چین، هند، روسیه، پاکستان و عربستان ممکن است؛ کشورهایی که برای حفظ منافع خودشان هم باید برای توقف جنگ تلاش کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/695730" target="_blank">📅 12:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695729">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حمله تند روح‌الله جمعه‌ای به جلیلی در واکنش به اظهاراتش درباره روحانی
🔹
روح‌الله جمعه‌ای، فعال رسانه‌ای اصولگرا، در واکنش به آنچه «تحریف سخنان روحانی توسط جلیلی» خواند، به او تند حمله کرد و او را به دروغ‌گویی، برهم زدن امنیت روانی جامعه، تفسیر دروغ از قرآن و فرقه‌سازی متهم کرد. او همچنین عملکرد دیپلماتیک جلیلی را نقد کرد و او را در شکل‌گیری بخشی از مشکلات کشور مقصر دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/695729" target="_blank">📅 11:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695728">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
،
چله "چهارم"
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
|
محمد
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
،
شنود
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/695728" target="_blank">📅 11:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695727">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvmO9ShidIP1otmuBKEZ_yQo2vfALNFMj6DbNXYgG_DLcZgGecKnDCQsiZaxwtov6g-m4e3EE21EsKMBr7iIlZ9wnR3Miqct6dPoYmodAi9zFxJvh20UKAtEvwZ4lb4n4IapfOegz-NdiLz7bCT5iMnQ6y-giX03pp-gNDZFKiYo6_CbIiOaTEb5x71yn4d_0myVPk1esMplT_menW0tqxjo9U2c0vRmWh6tUuXTiL4kZkmAwZVrSFpTFA1lhYbdq85oNaYpjvHutbkBsTExOLSBmFrb90bjZfJ_sBQTMdbbKgpl6W3I9KSfcOI5jZd4RdIwsDMWV2trH3JRafkAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توسعه زیرساخت ارتباطی در تنگنای اقتصادی
🔹
علی توسلی، عضو کمیسیون اینترنت سازمان نظام صنفی رایانه‌ای، معتقد است فاصله میان هزینه‌های ارزی و درآمدهای ریالی، سرمایه‌گذاری در شبکه ارتباطی کشور را با چالش جدی روبه‌رو کرده است.
🔹
توسعه فیبر نوری در شرکت‌های ارائه‌دهنده اینترنت ثابت عملا متوقف شده و افزایش هزینه‌های زیرساختی، ادامه فعالیت و سرمایه‌گذاری این شرکت‌ها را با مشکل مواجه کرده است.
🔹
هزینه تجهیزات و توسعه شبکه به‌صورت ارزی است، در حالی که درآمد آنها ریالی است و فعالیت در حوزه‌های دیگر فعلا فقط بخشی از فشار مالی را جبران می‌کند.
🔹
تغییر تعرفه‌ها می‌تواند راهکاری موقت باشد، اما حل این مشکل به اصلاح مدل اقتصادی ارتباطات نیاز دارد./ تابناک
https://www.tabnak.ir/005rUZ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/695727" target="_blank">📅 11:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695726">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
بازار داغ اجاره جای پارک در تهران؛ ساعتی تا بیش از ۳۰۰ هزار تومان
🔹
گزارش میدانی از شکل‌گیری بازار غیررسمی اجاره جای پارک در تهران خبر می‌دهد که در آن افراد بدون مالکیت، از رانندگان پول می‌گیرند.
🔹
نرخ‌ها از ۷۵ هزار تومان در ساعت شروع شده و در ساعات اوج به بیش از ۳۰۰ هزار تومان می‌رسد. این موضوع کمبود پارکینگ و خلأ مدیریت شهری را برجسته کرده است/ تجارت نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/695726" target="_blank">📅 11:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbcjMyK1q-r3o75UUg5i40xhdOZmVXiVInnG6pOyjmCS8vb5ig68YEH3dQxOWUbNFhJuNGu4lNKB1KZDgmR1H9V-mclT-b7kHg7Cx-Rwuw8pO_-FauBCwEBZY1Q7u_SjiinkWe9m52aGly28aj5Pj6nuLvJ468GELzwGJ196TX_7xES3NvTXQzLqIYZQb9gsfyXJVnnoSYOO1XkIGrgBTS_zy4zjIFP10IU1U1TTOMBSe7M6Z0vCJwe2GtOch1L8-nwgsgiC4NaWNTdA6bip6dZOJNWzhZAh3seiKH3RLmEE7xADLLVqReB3ZitwE4G8JJXovkxs74otiSaaFvNfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcyFt7LPuLuRS4PruJdZJi-Oc7jFulYOdvjmyAESbfACSaWqIX43aOPzx-At7aJWJmW5atY1ZmdqHQmjy1emDfBABIRtv71RRbXYkYssceI5tQRLEg2m6nIt4-2tyKMzDccnArxgJUugPR2pI8Xehhh4W6pVJ1e-NsKr__9b46YFjccW8d6ve_g6RfGIsnPZTY47-OaAOp97upIzCdtOaLN2V3zpdPusaFXoZ_ySkTQPor0C6vQkW2VjOwAhMt9QA19PFRjvRuFBSmYPtdtMnuTeCaoLPB2GQi5BxHQPDi_5fE8TMlwy-bGI9bck-Tbwrjydy3lhQV7D00XVZK6Ecg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed633483d.mp4?token=X78O3MzuPNth7sSzI6-g3LO0POEovCPwXhUlOl-VgaXj-Jq8XamD2u2JkO5HsSYlf_sUITLlWLLSLot6S-NU7xh2TXcIZyy9wTjXBpOZwFRC145x3OcPf_dncxADVCkHtIBi-ABXLbRB_pmqum5taljAJ9dMss96lHAp_azGo0zg_hD_1ZDTtcpLaxGug9uqmc1X1EL34JOcQXfpTAYZyU4wTK7DCzji-EQoXvDOR9HiTuNzrCK2iwtG3eIvKHtNKjVJ4j54qcBZbvSiBwCbZjitRsUkCrf_hMN6yZLvedfSopHVJeIEJgV1PNcFmQ756G1f25hKRLny11jf49A6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed633483d.mp4?token=X78O3MzuPNth7sSzI6-g3LO0POEovCPwXhUlOl-VgaXj-Jq8XamD2u2JkO5HsSYlf_sUITLlWLLSLot6S-NU7xh2TXcIZyy9wTjXBpOZwFRC145x3OcPf_dncxADVCkHtIBi-ABXLbRB_pmqum5taljAJ9dMss96lHAp_azGo0zg_hD_1ZDTtcpLaxGug9uqmc1X1EL34JOcQXfpTAYZyU4wTK7DCzji-EQoXvDOR9HiTuNzrCK2iwtG3eIvKHtNKjVJ4j54qcBZbvSiBwCbZjitRsUkCrf_hMN6yZLvedfSopHVJeIEJgV1PNcFmQ756G1f25hKRLny11jf49A6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله تروریستی به گشت پلیس در بمپور؛ دو مأمور به شهادت رسید  روابط عمومی پلیس سیستان و بلوچستان:
🔹
حمله تروریست‌های مسلح به گشت انتظامی پاسگاه نوکجو در محور بمپور- ایرانشهر، به شهادت دو مأمور انتظامی و مجروح شدن یک نیروی دیگر منجر شد.
🔹
در پی این حمله استواردوم…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/695723" target="_blank">📅 11:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
رئیس سازمان هواشناسی: با توجه به پدیده ال‌نینو، سال ۲۰۲۷ گرمترین سال کره زمین پیش‌بینی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/695722" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695720">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c7ea927e.mp4?token=SfDGAPAiATj6Ro94TWpnGMZvy0_lhPHxuSX0j8czgkAUKaxi9EzHUGNOT-0xHD83OEuzRZmISQDHA4F0C3T4N2DqObOrxJqLmMFD79qe_PUVxhfuZxZpL6ltVNF2ioUyZ3HmitVaitHJ4Zimg6R88bbFOAIYFMFjQjC-jJm9d9_8WHQeYBx6mBKKfH9twOwTkDwp9Py0j9MR69PGp2TOHwvUAQ7i_2SKJ1OofGHPiNSsv8dgWKRwo9S7VMO8KjgToJ9teNXlR920QrzjHhGW3kDOoee5t8hH1XjA3HIomqh4RfctHhUd8T5F-CwbKs9fLuc3pNO1mZ3IjzxauZcAXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c7ea927e.mp4?token=SfDGAPAiATj6Ro94TWpnGMZvy0_lhPHxuSX0j8czgkAUKaxi9EzHUGNOT-0xHD83OEuzRZmISQDHA4F0C3T4N2DqObOrxJqLmMFD79qe_PUVxhfuZxZpL6ltVNF2ioUyZ3HmitVaitHJ4Zimg6R88bbFOAIYFMFjQjC-jJm9d9_8WHQeYBx6mBKKfH9twOwTkDwp9Py0j9MR69PGp2TOHwvUAQ7i_2SKJ1OofGHPiNSsv8dgWKRwo9S7VMO8KjgToJ9teNXlR920QrzjHhGW3kDOoee5t8hH1XjA3HIomqh4RfctHhUd8T5F-CwbKs9fLuc3pNO1mZ3IjzxauZcAXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش معنادار مشاور سابق پنتاگون به بیانیۀ سپاه خطاب به مردم آمریکا
🔹
داگلاس مک گریگور: ورق برگشته؛ حالا ایران به مردم آمریکا می‌گوید: «کنترل دولت‌تان را پس بگیرید!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/695720" target="_blank">📅 11:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695719">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4_KVvf7GjSVKZRCGcrhQu8Qqf_tDGfyK6gXyZaGUGYS1vdXxL2KIWFdKMGhWE8yKri0uADgSitfxNCychHsIDwzcBJzMJ-JFMXM2sNXS5kff9LMdYvn3XQz3ycf86hJhx6tX4IKq4_5Fr3xVQq1WJnQ77Ezgr29H_yusEqBFXxORUCN7LwncejoZNW1zRW9zh5VOyZ9XAX5LzccimR719L9pNFrWENake4o4sR4DfuaMEllIwQUb3eL2-p2iH5PU5Keyf1_E8cvdF7WGvzsSKkV8sxb3zatUyNuXO4Qv8waFyW6B6hrVLztbzv66_upoG1LOWTxTvqK45sjiMzyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر نوع درد دندان نشانه چیست
🦷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/695719" target="_blank">📅 11:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695718">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سخنگوی شورای نگهبان: فردی که توانایی مالی پرداخت مهریه را دارد، مکلف به پرداخت است و در صورت تمرد، حبس او مجاز است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/695718" target="_blank">📅 11:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695717">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌹
دسترسی آسان به فایل های صوتی شرح "چله علم‌النور۴"
سخنران: علی مقدم
🔹
دیباچه
🔹
اول
🔹
دوم
🔹
سوم
🔹
چهارم
🔹
پنجم
🔹
ششم
🔹
هفتم
🔹
هشتم
🔹
نهم
🔹
دهم
🔹
یازدهم
🔹
دوازدهم
🔹
سیزدهم
🔹
چهاردهم
🔹
پانزدهم
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/695717" target="_blank">📅 11:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695716">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
دستگیری سارق منزل با ترفند نذری در تهران
🔹
پلیس تهران بزرگ از دستگیری یکی از اعضای باند سارقان منزل خبر داد که با ترفند نذری وارد خانه شهروندی شده و پس از بستن دست‌وپای صاحبخانه، وجه نقد و تلفن همراه او را سرقت کرده بود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/695716" target="_blank">📅 11:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
گام بزرگ نیان الکترونیک در مدیریت مصرف انرژی؛ افتتاح خط تولید موتورهای فوق‌کم‌مصرف BLDC
(موتورهای پربازده BLDC)
🔹
طرح توسعه موتوردرایو گروه صنعتی نیان با حضور مقامات ارشد کشوری و استانی افتتاح شد.
🔹
این خط تولید با بومی‌سازی موتورهای پیشرفته BLDC، نقشی کلیدی در جهش راندمان و کاهش چشمگیر ناترازی برق ایفا می‌کند.
🔹
در راستای حمایت از تولید داخل و اقدامات فناورانه گروه نیان، مدیرعامل صندوق نوآوری و شکوفایی وعده سرمایه‌گذاری ۲ همتی در این مجموعه را داد.
🔹
چمنیان مدیرعامل مجموعه صنعتی نیان معتقد است با اجرای کامل این طرح، شاهد پایان خاموشی‌ها ناشی از ناترازی انرژی خواهیم بود و حدود ۱۴۰۰ مگاوات از مصرف برق در ساعات پیک کاهش پیدا خواهد کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/695715" target="_blank">📅 11:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
غضنفری: استفاده از بازنشستگان بدون مجوز خلاف قانون است/ وزارت اقتصاد باید درباره وضعیت صیدی بر مبنای قانون عمل کند
🔹
کامران غضنفری، نماینده مردم تهران در مجلس درباره ادامه فعالیت رئیس بازنشسته سازمان بورس با وجود تأکید وزارت اقتصاد بر منع به‌کارگیری بازنشستگان گفت: قانون، استفاده از بازنشستگان را محدود کرده و اگر فردی بدون مجوز قانونی از بازنشستگان استفاده کند، این اقدام خلاف قانون است و باید با آن برخورد شود.
🔹
هیچ وزیر، معاون وزیر و حتی رئیس‌جمهور بدون داشتن مجوز قانونی حق استفاده از افراد بازنشسته را ندارد و در موارد محدودی که قانون اجازه داده است نیز باید مجوز لازم اخذ شود؛ در غیر این صورت، ادامه فعالیت فرد بازنشسته تخلف محسوب می‌شود و باید از مسیر قانونی پیگیری شود.
🔹
اگر قانون رعایت نشود، باید موضوع مورد بررسی قرار گیرد و در صورت احراز تخلف، پرونده تشکیل و برای رسیدگی به دستگاه قضایی ارسال شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/695714" target="_blank">📅 11:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
باید هرچه سریعتر کنکور حذف شود/ برخورد با مافیای آموزش بیشتر در حد شعار است
احسان عظیمی راد، عضو کمیسیون آموزش مجلس:
🔹
باید دولت و مجلس هرچه سریعتر به نتیجه برسند و کنکور حذف شود.
🔹
بسیاری از داوطلبان استرس و فشار روانی زیادی را متحمل می‌شوند.
🔹
بسیاری از دانشجویانی که وارد رشته های پرمخاطب هم می‌شوند در نهایت موفق نیستند.
🔹
فرزندان خانواده های برخوردار در نهایت موفقیت بیشتری کسب می‌کنند و این عادلانه نیست.
🔹
مجموعه‌هایی در این شرایط فعالیت می‌کنند که می‌توان لقب مافیا هم به آنها نسبت داد.
برخورد با مافیای آموزش بیشتر در حد شعار است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/695713" target="_blank">📅 10:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
از رتبه ۵۰ هزار تا پزشکی؛ کنکور، نبرد با خود است نه رقابت با دیگران
دکتر بهادر بختیاروند، مشاور تخصصی کنکور:
🔹
«دانش‌آموزی بعد از سه سال ناکامی، با توقف اشتباهات تکراری به رتبه ۱۲۰۰ و قبولی پزشکی رسید.»
🔹
او در بخشی دیگر از گفتگو خطاب به خانواده ها تاکید کرد: «رتبه کنکور معیار مقایسه نیست؛ هیجان، حوادث غیرمنتظره و ضعف پایه می‌تواند نتیجه را تغییر دهد.»
🔹
همچنین گفتن: «لحظه اعلام نتایج، آزمون بزرگ خانواده‌هاست. محبت والدین نباید مشروط به رتبه باشد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/695712" target="_blank">📅 10:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1014e6473.mp4?token=ppmya0VFSEiPHAMb2AcfHmL9CNiyhT4Mq0aiNI3bcWjMIQLijbIfcXdUgJTc3JIznUPtbrqn_Xz369F2N2W-1YClfw7g_QQixTuf0xCRFV9K6B6HW0dfj_Bm-xLSOHFKEj31BKG0X2pYxl9zq0NXHwdwm2uZzUxmmnbvRdIQU4Q0o7Rn8hWbLzsXjVkEWjwKqDMo--zq4D__RUREqzAPJJypcBGdXh5pKzLC0m-o6ZERXSdv_bJVMS8OQYz_q6W03S8kY4c_X6Db0HyOBsbMivD-lix9xoHCZO7pJqOi0idfBiuI_zAKvbrYlh8r0jScBSG5Ij4eZEWO37hX_x0uZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1014e6473.mp4?token=ppmya0VFSEiPHAMb2AcfHmL9CNiyhT4Mq0aiNI3bcWjMIQLijbIfcXdUgJTc3JIznUPtbrqn_Xz369F2N2W-1YClfw7g_QQixTuf0xCRFV9K6B6HW0dfj_Bm-xLSOHFKEj31BKG0X2pYxl9zq0NXHwdwm2uZzUxmmnbvRdIQU4Q0o7Rn8hWbLzsXjVkEWjwKqDMo--zq4D__RUREqzAPJJypcBGdXh5pKzLC0m-o6ZERXSdv_bJVMS8OQYz_q6W03S8kY4c_X6Db0HyOBsbMivD-lix9xoHCZO7pJqOi0idfBiuI_zAKvbrYlh8r0jScBSG5Ij4eZEWO37hX_x0uZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درصد افت قیمت هر قسمت از ماشین که رنگ دارد را بدانید تا ارزش ماشین را بتوانید به‌راحتی بدست بیاورید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/695711" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695710">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای عادل فردوسی پور: فدراسیون از استقلال پول گرفته و الان پول نداره پس بده و میخواد استقلال رو بجای پول قهرمان لیگ اعلام کنه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/695710" target="_blank">📅 10:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
⁣⁣⁣⁣⁣⁣چای را فوت نکنید!
☕
🔹
ترکیب اسیدی حاصل از واکنش Co2 بازدم شما باچای داغ باعث پوکی استخوان، ضعف عضلانی،کاهش حافظه و ایجاد سنگ کلیه شده و روی باروری مردان تاثیر سوء میگذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/695709" target="_blank">📅 10:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb3932a41.mp4?token=dke-jlkmZUYrmAWo6EpBqh4Utfyf-LIpU5twAaipEpWcYf3CROdmGMV9UxQxcDrm3jsQHU8qIjSLq44KAPuk-D_o5CzlOjx3q2te8Asb1WzZ2ehZecwkdysS5L8f8lKhRq7Q4egepfn31AIfmqel6y8RFa7b22Jv6Ab6JzsP6D_s4buLJ091Miw2KCB-p2DXlceOvAgW0uP1OKWcwnUwnmvs4l-BoKJT55eWuPsLEnB0s7lQYo76o4wNb1hIllwftn3EtAXT_k2ONByhXkuXuNKEOehZQjddSmm39ISW4XjLcKdxKJFbLDxd88nHHVPmtsKoD7ttE4NzhJQlou1JXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb3932a41.mp4?token=dke-jlkmZUYrmAWo6EpBqh4Utfyf-LIpU5twAaipEpWcYf3CROdmGMV9UxQxcDrm3jsQHU8qIjSLq44KAPuk-D_o5CzlOjx3q2te8Asb1WzZ2ehZecwkdysS5L8f8lKhRq7Q4egepfn31AIfmqel6y8RFa7b22Jv6Ab6JzsP6D_s4buLJ091Miw2KCB-p2DXlceOvAgW0uP1OKWcwnUwnmvs4l-BoKJT55eWuPsLEnB0s7lQYo76o4wNb1hIllwftn3EtAXT_k2ONByhXkuXuNKEOehZQjddSmm39ISW4XjLcKdxKJFbLDxd88nHHVPmtsKoD7ttE4NzhJQlou1JXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الان که فصل پاییز و فصل آلرژی و سرماخوردگی هم هست، به‌همین راحتی میتونی آب‌ریزش بینی رو بند بیارید
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/695708" target="_blank">📅 10:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9PkLG5W9VS0dEcl9k0pI5V0ERxn-eL5d--Fxr2OFtZka_sRVSwAua3-H7HLCWrzNFMLLClFkQjQUWCXQS2xv1x3n0QxyuYMr10KrioOHgCXDgnjxh-yas_U_k5-r1B44Yj8XlzhpiOHViL2egpGos10hm03ke3IngumUIEOLo9HSvavXXL-wsAZijY12mGNvSezy3-9ISLL3llIgZF8EE-cUlfyrpRkacbeFobWett6Ts4ZvEX03fm0HOoO8Q7gOI6m2COk875dlf-HoSKZSKHtJOy---YGk99B0nb1QIqkL0S8zdOJtXFv0oCZKkcf4aNFFeXENLHmFPlSTAI7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وصله‌ تزریق ارز به همتی نمی‌چسبد
🔹
محمدحسین مصباح، فعال اقتصادی اصولگرا: همتی اسطوره جمع‌آوری دلار از بازار است، اهل ارزپاشی نیست.
🔹
دکتر همتی تنها رییس بانک مرکزی است که در این سال‌ها نه‌تنها به بازار ارز تزریق نکرده، بلکه در روزهای ابربحران از بازار دلار هم جمع کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/695707" target="_blank">📅 10:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfcMfei-edoSXVBdyQ9YGpBgWg7sUnDY2CY6WmpptD4o4JwA5WG3y9-IITVh-DptLGzdgSbQnk4u7T6C0JhzVDYBLYRu8I8T83n-d-TTLc3v11GMorFMqa3qsTaisl8VAtMIO3kTJnIIwHPQf-MOytPR54HVhgO0Du6ROKMbK-65zn9t2SRb6XmbA7SERpOk6IaFDHXV1Kf-Eqah8ReY8G6CipI3CPWc4LUmY_8-6JHv3ZnbnntTiJTBIP8FUJihLdw31-ua-Nb7LZxq3KK99p5R1lNwTUbcTdbQeykdd-mKOTV0FXOGC92sC23TtKMLDqT2MZVHHMk8t9u6oV-SGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💼
Work Mate | دفتر کار همراه شما
همه‌چیز برای یک روز کاری منظم، داخل یک کیف حرفه‌ای.
از جلسه و محل کار تا سفر؛ وسایلت همیشه مرتب، در دسترس و آماده استفاده‌اند.
✨
⚡️
پاوربانک ۸۰۰۰ میلی‌آمپرساعت
🔌
دارای کابل
Type-C و iOS
📱
هولدر موبایل
📋
تخته شاسی
برای یادداشت و جلسات
💳
جای کارت و مدارک
🗂
نظم‌دهنده لوازم و وسایل روزمره
🎁
انتخابی کاربردی برای استفاده شخصی یا یک هدیه متفاوت و حرفه‌ای.
💰
قیمت: ۶,۴۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/695706" target="_blank">📅 10:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
آمارهای عجیب و غریب از میزان تقاضای استارلینک در ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/695705" target="_blank">📅 10:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0bdc68659.mp4?token=YHKxjXxd-C2i6EL43yq4QqPF6sTZKXzpKG-sBDZbChSyWh0L_uNQlbQwMyUZ0BK6j80AjfmG7IKD_kW8Yt-3Pg7yHSE3GMeCics3b0hk2XYKeuMKpWOqcwW6DPm6IHcS9yqo9m-Mq4wvHQBwPIPeV3rDZQvl2ebxhvC2whcYDsOySHwToLnTCoZXzcUq8EiCfNmi3BrgriNQ2HSIe5AsTPghS7JAxC_UY0Cw6CDrMg8vDKiAD_ot_70VroOrVrN5UhuGe5M6ubx-xfMyVB3Y4OSU_6YfgvnexVSHVph0018dLQt1s33CRf42RK35R9shZtbD8MuFQeK6xx6aeb1NLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0bdc68659.mp4?token=YHKxjXxd-C2i6EL43yq4QqPF6sTZKXzpKG-sBDZbChSyWh0L_uNQlbQwMyUZ0BK6j80AjfmG7IKD_kW8Yt-3Pg7yHSE3GMeCics3b0hk2XYKeuMKpWOqcwW6DPm6IHcS9yqo9m-Mq4wvHQBwPIPeV3rDZQvl2ebxhvC2whcYDsOySHwToLnTCoZXzcUq8EiCfNmi3BrgriNQ2HSIe5AsTPghS7JAxC_UY0Cw6CDrMg8vDKiAD_ot_70VroOrVrN5UhuGe5M6ubx-xfMyVB3Y4OSU_6YfgvnexVSHVph0018dLQt1s33CRf42RK35R9shZtbD8MuFQeK6xx6aeb1NLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از خفتگیری بیرحمانه از دختر دانشجو در خراسان شمالی
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/695704" target="_blank">📅 10:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
شمش مس؛ کلاهبرداری جدید سودجوها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695703" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695701">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه درباره افزایش احتمالی حقوق کارمندان: افزایش حقوق‌ها فقط در بودجه اعمال می‌شود؛ بودجه آذر ماه به مجلس تقدیم می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/695701" target="_blank">📅 10:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695700">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e3ab31ba0.mp4?token=OpbK4oYRW3_yrhIBBNFHYkcTTNF_c9rDn5OMKj5wOXMzy0PD3B6_SMXGvcEQBp_uuQLK1mq7zOjBwJLxibFROXtptJSjyi1cWX7lvuG2H_-G_z_aDyQqf25e12Yzy1-BINWgmmzJQ0tErygti9xFCfEpN2StACM2zewpqX3YwLFwXUpuI7Z1eKyKT8w7vXLTS6vZw65wF4Aei4_1dTxcN0XZwx4G6Gv5W_gjRGfuFXFx4TVn5LGaE2uNqzamGXNOBUVzcuXKf2TrMSfVb1GLoDv3Od9Y8xF0Ru5HexKLwOSHtbGQmIpdyYkPZPSoFAG1N1Ib08q_UvdLmMWKgHERcLQg6CfsC1MUY-UnnZepmRTeNJY7hMrt3Ylx_9H3xLwW4ZyAADykna2EdT1PvRsoOwbrV00NKnE6gi4GEwNp1go4RL99M1UC0Qs0WcYfN4fIHt4xWmxUmnROok1TLXnkpZBFIcbqneHbjOLd-ALlDdzzPSQnocAp1q-2AtRE5wtAgLI3JzTVR226TA318xE_mOO8pp9GvsRnM45-prtIWs8R5_y9xYWpR6P5ykxgn8t74YwukzJwsEaBKsjLoCH0gJHdv-IQKijkEU1ICYKSKrJ6pZaG4ogzd-xHaxTMx1J8o7H0IF-L6TFXRWDPyBSKp7fj23lB7k7SMAuxvjiODOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e3ab31ba0.mp4?token=OpbK4oYRW3_yrhIBBNFHYkcTTNF_c9rDn5OMKj5wOXMzy0PD3B6_SMXGvcEQBp_uuQLK1mq7zOjBwJLxibFROXtptJSjyi1cWX7lvuG2H_-G_z_aDyQqf25e12Yzy1-BINWgmmzJQ0tErygti9xFCfEpN2StACM2zewpqX3YwLFwXUpuI7Z1eKyKT8w7vXLTS6vZw65wF4Aei4_1dTxcN0XZwx4G6Gv5W_gjRGfuFXFx4TVn5LGaE2uNqzamGXNOBUVzcuXKf2TrMSfVb1GLoDv3Od9Y8xF0Ru5HexKLwOSHtbGQmIpdyYkPZPSoFAG1N1Ib08q_UvdLmMWKgHERcLQg6CfsC1MUY-UnnZepmRTeNJY7hMrt3Ylx_9H3xLwW4ZyAADykna2EdT1PvRsoOwbrV00NKnE6gi4GEwNp1go4RL99M1UC0Qs0WcYfN4fIHt4xWmxUmnROok1TLXnkpZBFIcbqneHbjOLd-ALlDdzzPSQnocAp1q-2AtRE5wtAgLI3JzTVR226TA318xE_mOO8pp9GvsRnM45-prtIWs8R5_y9xYWpR6P5ykxgn8t74YwukzJwsEaBKsjLoCH0gJHdv-IQKijkEU1ICYKSKrJ6pZaG4ogzd-xHaxTMx1J8o7H0IF-L6TFXRWDPyBSKp7fj23lB7k7SMAuxvjiODOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک تغذیه ساده و جذاب برای مدرسه بچه‌ها  مواد لازم:
🔹
آرد ۳ پیمانه
🔹
شیر ۱ پیمانه
🔹
روغن ۱ پیمانه
🔹
تخم مرغ ۴ عدد
🔹
بیکینگ‌پودر ۱ ق غ
🔹
شکلات چیپسی
🔹
کاکائو ۳ ق غ
🔹
شکر ۱ پیمانه
🔹
کمی وانیل #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/695700" target="_blank">📅 10:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695699">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
حمله تروریستی به گشت پلیس در بمپور؛ دو مأمور به شهادت رسید
روابط عمومی پلیس سیستان و بلوچستان:
🔹
حمله تروریست‌های مسلح به گشت انتظامی پاسگاه نوکجو در محور بمپور- ایرانشهر، به شهادت دو مأمور انتظامی و مجروح شدن یک نیروی دیگر منجر شد.
🔹
در پی این حمله استواردوم امیرحسین قاسمی و گروهبان یکم نظام دست‌گشاده به شهادت رسیدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/695699" target="_blank">📅 09:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695698">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
گزارش‌ها از توقف پروازها در فرودگاه‌های ریاض و جده عربستان
🔹
برخی منابع از حمله موشکی بامدادی یمنی‌ها به فرودگاه ریاض و جده عربستان گزارش می‌دهند.
🔹
هنوز رسانه‌های یمنی و ارتش یمن بیانیه‌ای در این باره منتشر نکردند و رسانه‌های سعودی در این باره سکوت در پیش گرفتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/695698" target="_blank">📅 09:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e319b5a243.mp4?token=KzVoNsTGlWSefIi65pkFYzVodXjuZm4QQ-FjazqBqnBLr7WFcCrgrJRORn1xkhqswUCzesVOgvJ0-OfEhwBQ2nDpCPdOfgCzoIGE0qN7TR7F4RAm0nLiHnz0R6iQQUikaxTZkClSqgRk69KRYy_OYeRkPPYf5iXYAM_FzgPrpQ9zELoqPOvBXyKsmpqZmqtyK8CBOm-zaSkp56aYKBlxpaj2ZP38Scm1kyXi-5blXML2zUO0rdtiuRcX2XwKDK-RJ-dFIGSacN5IOtxQoWbxah5EeJ1iornV0WoaMjDWOIhxAwSi7deRMzm6T7nds_soOIqejsb2KW8BftxIndIN6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e319b5a243.mp4?token=KzVoNsTGlWSefIi65pkFYzVodXjuZm4QQ-FjazqBqnBLr7WFcCrgrJRORn1xkhqswUCzesVOgvJ0-OfEhwBQ2nDpCPdOfgCzoIGE0qN7TR7F4RAm0nLiHnz0R6iQQUikaxTZkClSqgRk69KRYy_OYeRkPPYf5iXYAM_FzgPrpQ9zELoqPOvBXyKsmpqZmqtyK8CBOm-zaSkp56aYKBlxpaj2ZP38Scm1kyXi-5blXML2zUO0rdtiuRcX2XwKDK-RJ-dFIGSacN5IOtxQoWbxah5EeJ1iornV0WoaMjDWOIhxAwSi7deRMzm6T7nds_soOIqejsb2KW8BftxIndIN6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چای بعد از غذا؛ بخوریم یا نه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/695697" target="_blank">📅 09:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/695696" target="_blank">📅 09:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEnE-5KrwXt3T-CRrUtcz_UKqDB1yKt2WXu4AuRsOyZXgJ3_YlCLPk6-lwctFcPeUK6A_7s6gUi_k7U6aQmHLTMjXIwtS7cotr6j1awJH7CKlBlXYrEvdqsb6pmdvCe1sGgjfHmsEwWXvGhhFnMai3UsM9jSY5Uysb0GZkHCWf6nqF92RgBSfKpsM1-3LZqP5dYSNyPXDT0E0rGSWrUW4gFELZcYLnVuEgiHpZEEw21HiT2IBXTQ2lgX2Xy9-YiCc6GwJW72kRNNQ55abKryAYa7Cg7AYY3q-hKNClwSft0g65DNktx7bKub4O95EewBrSmUYhx9ZfIPfyzRlKud8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوتی جنجالی ترامپ؛ انتخابات برزیل را با هند اشتباه گرفت
🔹
ترامپ، در پیامی در شبکه اجتماعی تروث سوشال، انتخابات ریاست‌جمهوری برزیل را با هند اشتباه گرفت و مدعی شد ۱۲۵ میلیون نفر در دور نخست «انتخابات ریاست‌جمهوری هند» رأی داده‌اند و نتایج نیز بلافاصله پس از پایان رأی‌گیری اعلام شده است.
🔹
سپس با مقایسه این ادعای خود با روند شمارش آرا در آمریکا، مدعی شد در شهرها و ایالت‌هایی مانند دیترویت، فیلادلفیا و کالیفرنیا، با وجود تعداد کمتر آرا، اعلام نتایج گاه هفته‌ها طول می‌کشد و در پایان، نظام رأی‌گیری آمریکا را «فاسد» خواند. او در متن خود همچنین عبارت «دستکاری» را نوشت و سپس آن را به «محاسبه» اصلاح کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/695694" target="_blank">📅 09:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695691">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNqSd20-9K-q92SFU4MpUWy9SvA7f3t2aQ07Zo6ssiAOUoEQivYRHZSjkDArbgtWsqMI_7kaINebIq1zspOIqdRnEyg9KOItByJLiJxzbPgOaGvLNnxRoyDduSsXmcGlxTDXrKmRLutOhgxGrWQzCvz7pr4jWFNRNlxoEfG2SQfbe-WB4dRwx4FV2f98Mwv7HYEo4RWSOGWgyV8L01lr6yfvKoXzDddb4_a1at8FD4VTUBH-BBAbWlCuagYFxRuWiQ9620NFyd45ZN0RxxseFhrJ-4SJb3CiwdEK-GkU7W1qxQl5VRiZ2drB6ISSZQ3Hntc-XhCVSmJPCbk7FAJyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFCvCBioR0I-fjX7Ipr5PFXKsrg5MTuVi7z_zxRRccUR4VJrDQFP5VR29_cCfwCimJO3d1iTxx4fC-wjzdLE-03BUY-jVcNG9bxAziTHXciRBhcdBxqCV54Umgw2bSrNfBVLXXEZWvfnPTAPpj0YRSUQqfqId8PHiCpsBgfyJrAz-VLp_QsXHz9S7tOcUVeYPBvXqIrY3_Z8ZSSk64qNNfYh7qOrrbd_x3qCTlvFzgFsZHdtEV1bZ50m5xBNpI5_LlwvieQmppm79izWgJJHVNygA9t1S_1V8iFktjFVrFbghkIYJUHozXgN7WjW4ZAgIpxZ6rHSYQdx-o-BQb8i4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpNzmbYJNdKvI5bMJXtkJUfrYUGntKiHwvILcR02P-fOulvCedcCH8cq7uAZJ0swU6Il0PJpvPHbJr8vhRuSDs3QmECASyF8q7c4McMDv4yfRiY4wyFFZGXIqQXPs2Hy0IHtgUiPq1asSA9iQ4eJuWYB0danSzl5bQo0QakJnVxLiLOvRrQ7I0_SlmmtYVMcg8nh0_QbERH96Akw13jRl2Nww5S20K2u9XeSqw2LPJzJsAqaGl6LCLx02pX_gEH3iEgUUBnmy02pVQkzuJ53tfdF73NRuYrclBXkX37uACrtNmWjpZA5hHZfQAdtWBQMY2xuWjevZHi3OWUGFHYlhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ماه و پل خواجو
🔹
محمد سلطانی
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695691" target="_blank">📅 09:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695690">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIsj4XmNYItnT4eNhZaCgxS2I2C7Xp0huqpbgx4T910318HDiyuBMLgFY_SB-HZZiOesaJ9AGlj-G8CJTBxJE9kNvCw_k23uP85soHtpTwt8SIw3NKWuG2kKWgPhtd5usL3ndLaya7C5OV9GtLh52r2jK764NKTW2U6ZVvaOvIoB76Fh6f3DCOg-RRnxtcGEX26Z3XSUnPAkm0myFOSWQjUXTqqE9P_m669vQy2a60Rw1b0lHMSuyVzEyQpwLHCVAanEwD0iCn4lKFLYn2L3yi_CpwpWdRCHt-tdHEwQoxXUrdB6ci4SPzMJ3aS1irceJ5tojGr82vtNuraiV_dXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی سی‌بی‌اس: دموکرات‌ها در انتخابات ماه آبان پیروز خواهند شد
🔹
بر اساس تازه‌ترین مدل پیش‌بینی خبرگزاری سی‌بی‌اس/ موسسه یوگاو؛ دموکرات‌ها در انتخابات ماه نوامبر (آبان) با ۲۲۹ کرسی در مقابل ۲۰۶ کرسی جمهوری‌خواهان، اکثریت مجلس نمایندگان را از آن خود خواهند کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695690" target="_blank">📅 09:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695689">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
معاون رفاه وزارت تعاون، کار و رفاه اجتماعی از واریز مرحله ششم اعتبار «کارت امید مادر» خبر داد/ به ازای هر کودک ۲ میلیون تومان به حساب مادر واریز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695689" target="_blank">📅 09:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695687">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mlxKGvfKNf25ROHBfFmoKfZO2ExUaHjSLDsQhkAcFsnC9QmkyHi9iY1HbBDGStypmfaNra5xUL-Ve1IPzjHz1L8byeUWo6zuc5YK9Bd5U9CCqjBCLsYjWMM3zTCoZDTKulnlzs2fp5Q_-AvsBSJfHze8JTd0q_VwBzcuhHkSRESn1_XsU3z-phwSjayaa9uTclRVYyyYHI_NZmtqL5c_GAIlbb68CtwGr2pwalkEE8O3E4iINJ7NRZJFQPIL9qC4HrQO04wCYnNtyL4OJEVZJZhLZ1iX5j_6M-TxNdQJhrSRxaBQrnBQ83vx-o6E9Ro32fL1FYjcqmk_Si-fDv6BqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از آبان باران‌های انفجاری شروع می‌شود و هفته‌ها ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/695687" target="_blank">📅 09:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695686">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه پانزدهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/695686" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه پانزدهم؛ شمیم بی‌نیازی
🔹
اگر انسان در اوج نیاز، به نام
بی‌نیاز «الصمد» وصل شود، به فرزانگی می‌رسد و در آغوش الهی، آرامش را حس می‌کند.
🔹
برکت نور «الصمد» خداوند، پرده از نیازهای انسان برمی‌دارد و با رهایی او از چاله‌ نیازها، حقیقت را آشکار می‌سازد.
🔹
اگر انسان با نگاه شکرگزارانه، پیش‌نویس‌های ذهنی را کنار بگذارد و پیش‌فرض قدردانی را در برابر خود قراردهد، می‌تواند به درک لطف الهی برسد.
🔹
انسان سالک در ایمان به غیب و در  توحید حق، به درستی مسیر خلقت و هدایت اعتراف می‌نماید و حضور پروردگار را در تک‌تک ذرات هستی درک می‌کند.
🔹
اگر مردمان خالصانه نور صمد را طلب کنند، این نور مبارک چراغ هدایت شده و این خاک را از شر دشمنان خارجی و خیانتکاران داخلی حفظ می‌کند.
🔹
نور صمد پروردگار، از قلب انسان‌ها به سرزمین‌ها تابش می‌کند و هرگونه کمبود را پاک کرده و همه ذرات را در امنیت بی‌نیازی الهی قرار می‌دهد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/695686" target="_blank">📅 09:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695684">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzlJyasr2tJe1wFHV_9Hle-x0dxh_s7dzHgF4M-At5lXU4BWQ3P2o0g15GPspfe4iuwfKySLycnUFYyT2kTFwkJM8YdVXjpX1JjlEqA8LcqP4y24LYBBQ_NVR65v7JxOLMcOq45kgdzABOJ0PC4BCuoBk_tc5Sh9i350rfFhaE-7IAAEbUr0n-iV8SXjL54iVBL3vboWX8Qw4YWnOImCJTeV6BKiLkWL7qpGcAio1RZ7PfBWdNiiX343Kbu9KKKuLe5hq4wPzjcvkzF-klB9nF0Pj8DHqkzw4oDXOnggx970yv0MVwNw7qvF8hZsVRGfefQYa-OsEBluEvbL-NRMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند
سلول هاى بنيادى فوليكول
هاى مو
را از خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی
۱۰۰۰ نفر
تست‌بالینی گرفته شده و
نتایج فوق العاده در قطع ریزش و رویش
مجدد
داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو
به همراه دارد
🧬
در حال حاضر در ایران این روش
بالای ۳۰۰۰+ نفر
رضایت‌درمانجو
داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان روی لینک واتساپ بزنید
👇
https://wa.me/message/TUKIUT5M7IO5O1</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/695684" target="_blank">📅 09:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPc4ovGHlqUQ-ntbjm6zkqOBVtRDS303QQH3JUP12lNEDeTI93XfJ06wIyhGlkK4ciKVOW92JUAOXpPbIpbbYEiPeZ17BHnY3M2PeyCm0o17kmgzgOXeo88gqWyfN0rGL-OShwjhY44obq6GSCkZTnjQ87i76ENP3N3UgcANmFa_xj8Y39_PEwKP58yEZbLQlGMggt2GrVV3nHpzQwSMSkAZLeKLbt_h3IoVU4Oy9omSBx-1RbFxNeuDgk6pkSlEPa3Pcv6Rg1da1WMBcH0nUJWihwoar8Rqsoq-8lSBiU6W80w2bCgKBnpQxYnFJbjiIapzUTirbvLDUfBS4-crMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3w4hHXFtnFYdbgEt0JaVpuwUZAO4ENR9OuK1TWDGJWmcS-jyrGLkKPC4qPNrjvJDLQNh26RM8pafXwi9SJRMrX9COFN0uxAO9PVfhiArJGtqfhY3T_-uzsKzZmbJ0Hy-uBF_93hbKAxPbRLEf_DVzWTTz4ofmOnoqETyAaH6veS9YPM8zgsa64_IiEMQJF4Ei04MUgFxUYuJthajwYnSRkQoKJy_35TmMyi5Q2tRnygc33z2JRF6OoMPGhclSRgoTIdcAaGpuyM2eEcXQ04nFoKjpoz1ix4uNi9OZDpqNJu69zvvjskixKAYDWbVmZuvJIDQ8zauWZ0vCcAnDKE-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16565927ef.mp4?token=KMRRGRkPxtgmh6tgTcWVnIc5TvK7m9Al15ALw4jLnKAEjFsrmHl40lUhOA4M5IEGrxIKmL7j5beGAbDic38RL4McN21gOQw9mMs4gogFb6R1vLb0F8NoNn-Y410MW3EHVOkfd6cyaPd2W8v_Y0J31miUyBhwVhh5fIWnDd4OqkvfbLBDDIxkr553Pn7TRlDx5q1Zs5a--F9xIg94NM5N6GNqvX6mwF9GQD4LmKt0IoUl9UUfrD_DriAh5g90KObuwtAz3l0sZpqBJCpKCtxWwEJWAPFTYORmX8ykY85VekPHW3MyXHNCRGpqwXa9EKpZLmBPjpZFa6I0g_OQFd0jEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16565927ef.mp4?token=KMRRGRkPxtgmh6tgTcWVnIc5TvK7m9Al15ALw4jLnKAEjFsrmHl40lUhOA4M5IEGrxIKmL7j5beGAbDic38RL4McN21gOQw9mMs4gogFb6R1vLb0F8NoNn-Y410MW3EHVOkfd6cyaPd2W8v_Y0J31miUyBhwVhh5fIWnDd4OqkvfbLBDDIxkr553Pn7TRlDx5q1Zs5a--F9xIg94NM5N6GNqvX6mwF9GQD4LmKt0IoUl9UUfrD_DriAh5g90KObuwtAz3l0sZpqBJCpKCtxWwEJWAPFTYORmX8ykY85VekPHW3MyXHNCRGpqwXa9EKpZLmBPjpZFa6I0g_OQFd0jEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خشونت علیه ربات‌ها؛ شرکت آمریکایی Figure AI ربات‌های قدیمی خودش را به کوره ذوب
فرستاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695680" target="_blank">📅 08:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
انقلاب اسلامی به انگلستان رسید؛ پس از فرانسه و آلمان، اسلام‌خواهان اروپایی خواهان حکومت اسلامی در انگلستان شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/695679" target="_blank">📅 08:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc6314ffc.mp4?token=nvnLYviXTF7GnLiHhQpij3LZJ2yGNydUylxjOm3hvTgeenU0uTaWpGbS5eYp9hgpF6ZjdxHdLXaAS2HcrSN1kOjPiFcMx7NMFLroskKzNrgaXJRO_HSiu1Sd3MBHSe8AyYs5b8RTjaZbLXNM1Sw9K6WebzLsJlOw9vUsn69EheXbzuLua-J6QnhQlCNzKL9L3czjHV4wkzDywgHQsUCpuFRP3bT549nhhys7dnaVu6hHM67BAEtB8B0vcSWPJPZ1q_1CSDR1UxumGUu6vjN9WzO527vIEA41jnw7kBzy6VzJ--MBY4_Z77mj_Oly0Ig2LgDUX8CL6GyTsxS8l5G9-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc6314ffc.mp4?token=nvnLYviXTF7GnLiHhQpij3LZJ2yGNydUylxjOm3hvTgeenU0uTaWpGbS5eYp9hgpF6ZjdxHdLXaAS2HcrSN1kOjPiFcMx7NMFLroskKzNrgaXJRO_HSiu1Sd3MBHSe8AyYs5b8RTjaZbLXNM1Sw9K6WebzLsJlOw9vUsn69EheXbzuLua-J6QnhQlCNzKL9L3czjHV4wkzDywgHQsUCpuFRP3bT549nhhys7dnaVu6hHM67BAEtB8B0vcSWPJPZ1q_1CSDR1UxumGUu6vjN9WzO527vIEA41jnw7kBzy6VzJ--MBY4_Z77mj_Oly0Ig2LgDUX8CL6GyTsxS8l5G9-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرقت ساعت ۵ میلیاردی سفیر فیلیپین در تهران
🔹
ساعت طلای سفیر فیلیپین در تهران از خانه او در شهرک غرب سرقت شد؛ پلیس یکی از پرستارانی را که برای نگهداری از فرزند سفیر استخدام شده بود، بازداشت کرد.
🔹
متهم به سرقت ساعت طلا و برلیان اعتراف کرده و تحقیقات درباره…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/695678" target="_blank">📅 08:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7a6e870c.mp4?token=iM08xqcj1kleW6iI17NSyitneHZYyuEIzj4aOGPT4Ez0hmB8RPb6eNQczDbBn2DAMqVEXZg3MDj1Dit4D48pI0nRKRGai7E-amtYwQtmKtq0n3DFTGm72TlG6joMfclwzeHK6fBqXgSzue4PaBcA12vNIc7EUdjHk5uCScCseRC5-tVebEe1N9cl-TtTld3bv4lEhSEbxrLoeN5YeqbJaxCLsFK6JkKNnpWuqGB1YElt_42orzxn3ZUaOApMIJHTEeErT2_26anlMr18JdvuULbrWNffAz34e5gtbxdTOBpQCvcPhEi9KAAjrHAYVdI5sXIrNgbYk-gQzck2L9KTBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7a6e870c.mp4?token=iM08xqcj1kleW6iI17NSyitneHZYyuEIzj4aOGPT4Ez0hmB8RPb6eNQczDbBn2DAMqVEXZg3MDj1Dit4D48pI0nRKRGai7E-amtYwQtmKtq0n3DFTGm72TlG6joMfclwzeHK6fBqXgSzue4PaBcA12vNIc7EUdjHk5uCScCseRC5-tVebEe1N9cl-TtTld3bv4lEhSEbxrLoeN5YeqbJaxCLsFK6JkKNnpWuqGB1YElt_42orzxn3ZUaOApMIJHTEeErT2_26anlMr18JdvuULbrWNffAz34e5gtbxdTOBpQCvcPhEi9KAAjrHAYVdI5sXIrNgbYk-gQzck2L9KTBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند تمرین کاربردی بالاتنه که می‌تونی صبح رو باهاش شروع کنی #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/695677" target="_blank">📅 08:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695675">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آمیت سگال، خبرنگار مشهور اسرائیلی: این هفته، خطرناک‌ترین هفته ۲۰۲۶ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/695675" target="_blank">📅 08:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695674">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETcBtb6HuWkzRzK6ZNRGoglYfkkE3woBAb8uO-_z6lj1VT_-u4gzKZtvZNPVY-8iaEcE1CCr6pSqP1t72AecRz5Iem_oUBWIaTHeNJ-Oa4tCYaG7iOMkxKiXLVt3y-ew9XZ2OABw9v58a8YX9qJvTNjawCh5Xsu_9q0L8D76iddBcOUaWx_hau-6D9nGpjlxQJurj2Ranajt2DtUeNbrec0WsgyJ1nJpUdg2qToLItMi5K_1zZAWWzd8iGrIvXnt6_oyEYYF_fQjVShogxPAj08sVKmkIXEU3B-QhxOyMYpDNSybXMqEZcN_c2W8FWCwD8fzrpqy-sD7MfqH6iL91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شلیک پلیس فرانسه به صورت نوجوان معترض
🔹
در جریان اعتراضات دانش‌آموزی و دانشجویی در فرانسه، ویدئویی از تیراندازی پلیس به صورت یک نوجوان معترض منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/695674" target="_blank">📅 08:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695673">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487b4300b3.mp4?token=KgTifb3Ns2lYw8MEdE_QzUXIkjA5Yd-tUu7qYFs_1FJxG_UnkSdxddwdTiSvFeJgI9bQvYaWspc3KzdOB0ISbDFykTGbp2Lr34EDwz-wRGVU76mMw-SaVsX0XIMN46wIBEoMJVWw402t2jj70rr-K127u39wLVBjiiz5bQvk8TNL9QhHk_lvMkN2KaHnS791B8FXZ9sMoZttqGB_X7BUgHYcYtkesttWyHm6rMfW19ipNbqYkmLLbSi1J-p8sA39gsYEXcbDoPlIP_IRrxaUzseRmlaN3KJ8EyvId2tIlU7xcE33uao3UeKDt1SkGB6hl24WZqlqIM_2aztuPzWAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487b4300b3.mp4?token=KgTifb3Ns2lYw8MEdE_QzUXIkjA5Yd-tUu7qYFs_1FJxG_UnkSdxddwdTiSvFeJgI9bQvYaWspc3KzdOB0ISbDFykTGbp2Lr34EDwz-wRGVU76mMw-SaVsX0XIMN46wIBEoMJVWw402t2jj70rr-K127u39wLVBjiiz5bQvk8TNL9QhHk_lvMkN2KaHnS791B8FXZ9sMoZttqGB_X7BUgHYcYtkesttWyHm6rMfW19ipNbqYkmLLbSi1J-p8sA39gsYEXcbDoPlIP_IRrxaUzseRmlaN3KJ8EyvId2tIlU7xcE33uao3UeKDt1SkGB6hl24WZqlqIM_2aztuPzWAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشور پاکستان: من رفتم ایران با تعجب برگشتم؛ ما هم باید مثل ایران بشویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/695673" target="_blank">📅 08:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695672">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ای‌بی‌سی به نقل از مقامات: کمک‌ خلبان هواپیمای فلای دبی که قصد داشت پرواز عازم اسرائیل را سرنگون کند، قبلا از پرواز برای شرکت عمان‌ایر تعلیق شده بود
🔹
او می‌گوید هدفش ساقط کردن هواپیما در اسرائیل بوده/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/695672" target="_blank">📅 08:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695671">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18a2e6b0f1.mp4?token=AyCC6juVey32r5jxZiqpE5FAVYUZ1lsjoouWePwYRUMT6I-_eGLbqLfE-08FGiKyZ5SUVVz0DvU5tKn8s1EOBPku13LExRo_aXHPy9bVCtdiPJuo9d9qOGX3pjRrtjiuVCAvzrFtMa6HOWs5ijRP9kadrZIjbcVOXUVk8wf_zl3pfgqNwq8g_BpBXpnI7lzDlswDOg_t0oUt5yb7VwznAb6mqx9wadYMaAAlL7rsfOQTKMH5FD_FPv9yeOyOanrVTq7wLPgSF8xH_7CjUn_kgUX5c3teX2IcLUQtIxHxubUvRt05dHKdI-6lEHaDtWusyIhGVlr3y_QYI9on1dJSXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18a2e6b0f1.mp4?token=AyCC6juVey32r5jxZiqpE5FAVYUZ1lsjoouWePwYRUMT6I-_eGLbqLfE-08FGiKyZ5SUVVz0DvU5tKn8s1EOBPku13LExRo_aXHPy9bVCtdiPJuo9d9qOGX3pjRrtjiuVCAvzrFtMa6HOWs5ijRP9kadrZIjbcVOXUVk8wf_zl3pfgqNwq8g_BpBXpnI7lzDlswDOg_t0oUt5yb7VwznAb6mqx9wadYMaAAlL7rsfOQTKMH5FD_FPv9yeOyOanrVTq7wLPgSF8xH_7CjUn_kgUX5c3teX2IcLUQtIxHxubUvRt05dHKdI-6lEHaDtWusyIhGVlr3y_QYI9on1dJSXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری زیبا از همنشینی برج میلاد و ماه کامل؛ مهر ۱۴۰۵
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/695671" target="_blank">📅 08:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
آغاز انتخاب رشته آزمون سراسری ۱۴۰۵ از امروز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695668" target="_blank">📅 08:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695667">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UccLGdSpa9nADVsOMeZe_wflk77ggY6uVx_N3ZXnnQs9Mc1f-86ctCpx0tM7Iv4Z1aRWT2m2HF96k2tAcVodhiscuv_Sk2UW5tl4h3iBxQhV7pLnextJ6uNEWI4MhlWg3xIWAs5jqPBaR5tiuGeCV2b_iJJLNwesJFTaU3gMOiNYIzr3nV_NeSQgjy2QXyvkvPErfu-WmHs4OmMutXidaxd9m77IHyHmxlvHKLFW9fJVKwxEuq_SoVQuzyi_F9zBC14Vw5WU6GwHCGJHEPfITDL-o_hOatOyi1dyxAGieKceouIAsog-NkTNX_Js-DCm1YFiyIlphvgFUsep5qschQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۳ مهر ماه
۲۳ ربیع‌الثانی ‌‌۱۴۴۸
۵ اکتبر ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/695667" target="_blank">📅 08:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695666">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تعطیلی مدارس و مراکز آموزشی بخش مرکزی شهر کرمان و بخش‌های چترود، ماهان، شهداد و راین و تأخیر یک‌ ساعته فعالیت ادارات به دلیل گردوغبار برای امروز دوشنبه ۱۳ مهر
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/695666" target="_blank">📅 07:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p48SWXaZd03X1AD9oW7BKcOKUX6JIvrqlNu0UoOV-7SK7B8AHznFTgluuMkhAhmH5lpQTjp2bril20AF6bFcP2VVHVaIx7AQUTcc32Ibf69CcekCvLiHk5M2sGMk_cJLgc_PShc7Rm8WvDSRjoJxvQtmNEOH6yQhhf1Cn_94Uzo2RE9pp4Sq5bXVc2UZmg8gMKYwbXTPyQE40rIYdi_SiWRfC2H5VEDyCJLVAbhoaB3cXCTauZfkWRiSY862CTY1zX56J62ABEuhvqjVN39U97Xs38SyVSKNtUwxobuKPyBbBnhOqPzuEANMT28C-oOv9RkaHwmSPV52V9WcbsGUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند
سلول هاى بنيادى فوليكول
هاى مو
را از خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی
۱۰۰۰ نفر
تست‌بالینی گرفته شده و
نتایج فوق العاده در قطع ریزش و رویش
مجدد
داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو
به همراه دارد
🧬
در حال حاضر در ایران این روش
بالای ۳۰۰۰+ نفر
رضایت‌درمانجو
داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان روی لینک واتساپ بزنید
👇
https://wa.me/message/TUKIUT5M7IO5O1</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/akhbarefori/695665" target="_blank">📅 00:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUYktEgb38e_210u_rnrUU3syouosvAYHiD7uk7bmJGMzg6ZCGK-c0TZquRIoksNa-w6WugOM92Z3Is3QWLfcCWx6A-AT-HSFF6jPzMGW4EWuCckHdXHiljOu8Tc_gEqh17EE0L0KTZnjBRNdFQD5XjTgBuQisK6RkXAY_pRJBXBkuMuaBgYgE3yGKY5B_thRnxn_Js6vmrYCzMiS05TVU5e11wfII4a_ExbbxTtnx06JOtZ3a7tRIAZtbOLr02l1Ft7dWNQJAQWkN84dhaXFrxhYn-J06PCSzxKg2rxPmvkLdXEzKEGN7yx4xmP3M03h4ZdyeVltN5-YM0j1kZ1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
سوییشرت مردانه خزدار؛ گرم و خوش‌استایل برای روزهای سرد!
❄️
جنس
مموری ضدآب
با آستر داخلی
خز تدی
؛ هم گرم و راحت، هم مناسب استفاده روزمره
👌
🧥
کلاه‌دار و جیب‌دار
🔒
زیپ‌دار
📏
فری‌سایز، مناسب تا وزن
۹۰ کیلو
💰
قیمت نقدی: ۱,۷۸۰,۰۰۰ تومان
💳
خرید قسطی: ۴ قسط 495 هزار تومانی
🏠
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
خرید تلفنی
👇
https://memarket24.ir/product/fast/50703/180124/</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/695664" target="_blank">📅 00:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aac7ff8f3.mp4?token=Ti67pd2YISHEgdQBAETpiEzOpo7YEGH97vkqVk2ZQQ-qIjO_58GGoi-CM1dQouhR_1ayADXj3C-V3Eikr4jY5PMKWjkURACZhGP0jqTidi7GxaObYC2L3QJoiIYHogS-4rJNnMXwF6rL04AmM368-1rgEitzFXyya-6k8nbSMND-eLpeHD56g8B9n-XrfDk4TMYr7jhyjVYrRZacIGsj2VNFh-4RXg2dWpbsr8iEw2s79X1ssMxcKZHzUy48GjWqWnwBowpfUTAH6eKgcRYjwKFKU3LD62yBUZ6BtR38todz1_3zIR4L3IcyAnUlxtY6v4RK-_vEn02YhE2Zz6QE2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aac7ff8f3.mp4?token=Ti67pd2YISHEgdQBAETpiEzOpo7YEGH97vkqVk2ZQQ-qIjO_58GGoi-CM1dQouhR_1ayADXj3C-V3Eikr4jY5PMKWjkURACZhGP0jqTidi7GxaObYC2L3QJoiIYHogS-4rJNnMXwF6rL04AmM368-1rgEitzFXyya-6k8nbSMND-eLpeHD56g8B9n-XrfDk4TMYr7jhyjVYrRZacIGsj2VNFh-4RXg2dWpbsr8iEw2s79X1ssMxcKZHzUy48GjWqWnwBowpfUTAH6eKgcRYjwKFKU3LD62yBUZ6BtR38todz1_3zIR4L3IcyAnUlxtY6v4RK-_vEn02YhE2Zz6QE2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوردن کره با شکم خالی چه بلایی سر بدن می‌آورد؟
🧈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/695663" target="_blank">📅 00:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695662">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gsh6w9uTa4gWicoGLbhSKC5HbhzgezSc0f0s-UfaMPKKexxR2dYSvIKpBmLqNNS_-NF9fG_4GxuSV8tth-gI1wgIGlD9qpz_KODQIZddot1cugBrIIe8WObHqvJxHVqk9TvwfzqdMC0yvrE5VtlfISxk44Lpnm0v4wKNGyogGctVRJ76p6qS4LI_qJlkeSaQPejA3axJgjciHWnMSH0mD3-LLukDzfzRcDrA8ttwtaIU_tCXWvGDpcCOwF1avEWTttzrDVFCSjOwZbNtDzhnClDJoyzFQ6yWSZeGust717t5bgv33WnHh2FA5A9Dt3TC7fJSwn1klwVxCY8l-zoKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید صفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/695662" target="_blank">📅 00:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695661">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqcipQh1XoZ1p6Nw9X210CKHlu1njvFdwSrtTmvTZvmCXgziA1VD5qVCY9FVtcmSPM7qrBmBHEyE2aZf0O1Qn86_yCSc5T3rwjfXRAZyb3qQPP2w9nqFkoMMX7ttK5cUk26qT0W0_W9tVqah0Rsmulg7d8_-EeAR_WdSu-vUHbOXg9Mx7gvhzJOt43LKnHm6dmgVRiGTB6TH1y-rSIPBXgeYEECJk68lF_9bGjgUsQNmDda9Z6lxD-w5pUzNel9sCUGwuAk900I8NUHQhvHiEY98ZeqAE2dsCLJka5ezGJmDIfIGFYusFzROjmboEhjKEx_Dd8cTR8TvBmUoV6sLdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/695661" target="_blank">📅 00:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695660">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
فرار بمب افکن های آمریکایی از ترس حمله ایران
وال‌استریت ژورنال:
🔹
بمب‌افکن‌های آمریکایی از پایگاه فیرفورد به داخل آمریکا منتقل شدند؛ یک مقام آمریکایی نیز مدعی شد واشنگتن از طرحی مرتبط با ایران برای حمله به این بمب‌افکن‌ها و کشتن نیروهای مستقر در فیرفورد اطلاع داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/695660" target="_blank">📅 00:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71b3a2afdf.mp4?token=CIZXfC8hPNcoQLD22koxMnunKwf3J8AOVjuSCzPVqpoRqd9_N_ZAxliPUYMR25r9grp0IYCI-37yrzhbo-zSn6u-jf0VMg-ps6_m-8isiqBjUaSpEDkTYy0kw4Zz_kx69uQvAs9npJTgGkaVS89Wm7BoNZOgxwzg9q5ke3q6UXSmsIJrk_r2SirKACU1p_5eUZ1iI5AyuR5i8oCKX_brA4dSyUMBjIt871WJ4Se7PwmxxYlXjMjN665fPemBmJrGPenLZKa7ZCQodrnO0ZoUQ2LhGp5ou7-SgpAHuERZ4ezkrPZzm_deISwmil4LMNz2HcCu1Koahm_DJ6r4ZgYSJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71b3a2afdf.mp4?token=CIZXfC8hPNcoQLD22koxMnunKwf3J8AOVjuSCzPVqpoRqd9_N_ZAxliPUYMR25r9grp0IYCI-37yrzhbo-zSn6u-jf0VMg-ps6_m-8isiqBjUaSpEDkTYy0kw4Zz_kx69uQvAs9npJTgGkaVS89Wm7BoNZOgxwzg9q5ke3q6UXSmsIJrk_r2SirKACU1p_5eUZ1iI5AyuR5i8oCKX_brA4dSyUMBjIt871WJ4Se7PwmxxYlXjMjN665fPemBmJrGPenLZKa7ZCQodrnO0ZoUQ2LhGp5ou7-SgpAHuERZ4ezkrPZzm_deISwmil4LMNz2HcCu1Koahm_DJ6r4ZgYSJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عددهای فشارسنج دیجیتالی رو چطور درست بخونیم؟
🩺
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/695659" target="_blank">📅 23:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سردار فد‌وی: مردم دنیا و مردم آمریکا می‌توانند خودشان یک مقایسه‌ای بین توانمندی‌های ما داشته باشند وقتی خود دشمنان می‌گویند که در مقابل حزب الله و یمن مستأصل شدند و مجبور شدند خیلی از کارها نظیر فرار از یمن را انجام بدهند قطعا حساب شأن در مقابل ایران مشخص…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/695658" target="_blank">📅 23:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695656">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn3xMon2P--BGvIdc35sifktr0JJYyHR-MBwxXE692sb8Mz3eQCoI4WSeigOmrkinUqvwG4rs_hBt78xpkNjbwVR0xBtgjuz0FgTIYbW9MJFtOJF2tDIQkPbMVqzDl0VpzUqOsrtGQjDYTmCw2yMxGyLr8RhMU2mmVZyOOlRTEGW3TjRklULjBhBAA6ADfB9w_EeZ-QRp5KOy3WMeG1q--E9wbvXgNaTWe_cDAE6yBXjqlqTZ3jHNAA86aFmFyQ7zIelihDpJkhBao3QBpvnHN3boz5VGAeH9ur33Z8taBCT38nAgFkSK6ikrlsjWB4MwKql399sukSsUki_z1AFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ مکانی که آب خوردن ممنوعه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/695656" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695655">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌹
فایل‌های صوتی تفسیر سوره محمد
با سخنرانی حجت‌الاسلام امینی‌خواه
🔹
جلسه اول
🔹
جلسه دوم
🔹
جلسه سوم
🔹
جلسه چهارم
🔹
جلسه پنجم
🔹
جلسه ششم
🔹
جلسه هفتم(بخش اول)
،
(بخش دوم)
🔹
جلسه هشتم
🔹
جلسه نهم
🔹
جلسه دهم
🔹
جلسه یازدهم
🔹
جلسه دوازدهم
🔹
جلسه سیزدهم
🔹
جلسه چهاردهم(بخش اول)
،
(بخش دوم)
🔹
جلسه پانزدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه شانزدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه هفدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه هجدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه نوزدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه بیستم(بخش اول)
،
(بخش دوم)
🔹
جلسه بیست‌ویکم(بخش اول)
،
(بخش دوم)
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/695655" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695654">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2463caf8.mp4?token=g6Q4_rZTGdX6NEVWjkB28mE4IzUqjPBIBN_yAwnsjCvWtMp0d-rKSnXPYijAYFtnCmDqsgYeHuOO7cXDXQ4w23V17RPIR0fPlVl_5ZTo-emVXTKpIKt2zpS6R12Re6bKJDegiLRvqTGdqGKUY2Hc4DMfGuHmKMy3HSe3lIMBDn_k9XRN8HW3oSokZ0CDOOik10jQgvH1G3zXXow6Qe75zcUwZD4A2U1d2uZabWl5Rj0QpyKXHxGEtJD-B4W9xYUGiSxhdVrmdmkS1UXEb3Jv-yIro2mJyH-VxD3Ey0d8RRh6QQPEBPlmfVfA9583rSIXnUFnoFJ5RE1p5j3ZdLP0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2463caf8.mp4?token=g6Q4_rZTGdX6NEVWjkB28mE4IzUqjPBIBN_yAwnsjCvWtMp0d-rKSnXPYijAYFtnCmDqsgYeHuOO7cXDXQ4w23V17RPIR0fPlVl_5ZTo-emVXTKpIKt2zpS6R12Re6bKJDegiLRvqTGdqGKUY2Hc4DMfGuHmKMy3HSe3lIMBDn_k9XRN8HW3oSokZ0CDOOik10jQgvH1G3zXXow6Qe75zcUwZD4A2U1d2uZabWl5Rj0QpyKXHxGEtJD-B4W9xYUGiSxhdVrmdmkS1UXEb3Jv-yIro2mJyH-VxD3Ey0d8RRh6QQPEBPlmfVfA9583rSIXnUFnoFJ5RE1p5j3ZdLP0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب بازار روز تایلند؛ جایی که کباب موش و حیوانات موذی خورده می‌شوند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/695654" target="_blank">📅 23:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695653">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da8reW74rfBmopmUxJahaHmsEVWL5fKuMA4aLhpXC72FR6SB17sYmXCeSHtK2O_J-pg-mqMxD_Ay87_GWopxBU24ztURf3sg6givPzuGLXUJ1s5xIlD6GaoJPetDdoSB738EC4t_65lZx4558EPMHxWOTyg3Z1uiRHxMAnZGL1kJbN5MkmISjp1eV38FHHHl2DkQa0cwIByvmSDqivGS4hN18v-CMeCc-KYx870vI_u2nOSa4-7sfiGuuBPtnHQ09Q_ycawgcgtsloPTKD9_Ov6Sb6naFiNUyAXWHvKw6MxNUTXDR3KsS9GT-KCNTztTXvOTZr0pXhxdhlrIvZQUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ با انتشار عکسی از خود در کنار رئیس‌جمهور چین: ترامپ جوان‌تر به نظر می‌رسد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/695653" target="_blank">📅 23:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695652">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b7bf20cd.mp4?token=TD-uPZkcBZzMrnPPCYk2kkSqahfJHhHY8YTGXSjhR4RMXUQl8yyDbQZ_STvQzEcJ32haEMWfuNoscixn5ExYo90li0qX4diZjH4qSWSDQx3xxOb-d_g8J7Bu4khpKjS7itLZxfFcvxeChLY3eT5JZ-DqCmHY4tflJzcIneK4qndGjezUpQqA2rk8DHbYv4nQw2rRxfTU_rLzifTPD4PS5glaf4tR8iGKOLH2cNkONwEgbvEggKqM67Y5Apz62t7oxFLwMriENsd-RZb3eBQ1PKgoc7y6Zq5KUrzd7RZXZ2ER3ez-aKs0pQpb2xbApCo6_wwhjtBAEFj_KkpEal9jog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b7bf20cd.mp4?token=TD-uPZkcBZzMrnPPCYk2kkSqahfJHhHY8YTGXSjhR4RMXUQl8yyDbQZ_STvQzEcJ32haEMWfuNoscixn5ExYo90li0qX4diZjH4qSWSDQx3xxOb-d_g8J7Bu4khpKjS7itLZxfFcvxeChLY3eT5JZ-DqCmHY4tflJzcIneK4qndGjezUpQqA2rk8DHbYv4nQw2rRxfTU_rLzifTPD4PS5glaf4tR8iGKOLH2cNkONwEgbvEggKqM67Y5Apz62t7oxFLwMriENsd-RZb3eBQ1PKgoc7y6Zq5KUrzd7RZXZ2ER3ez-aKs0pQpb2xbApCo6_wwhjtBAEFj_KkpEal9jog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۸ ریسک مهم سرمایه‌گذاری در طلا
🔹
قبل از اینکه پولت رو تبدیل به طلا کنی، این چند تا ریسک رو بشناس، چون ممکنه طلا گرون بشه و سرمایه‌ات اونقدری که فکر می‌کردی سود نکنه!
🔹
جزئیات را در این ویدیو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/695652" target="_blank">📅 23:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6911c9232.mp4?token=Fr7xoSlPHL1GmKAsuLzjdOoL-0xyjX-KwnqTL9byumyvUqCYorSbYw6AuM5jaxS_nBNcf8nMc0EjRx0yA7jv9vD92cUxiTmOI0ystX5ZTnTTXzLxBu00dM4qN27JoKkPgEUILSEYUbMxNghm8lBGqa1MN78m8XzklqY3CHVSPB_i7jk48Kb5kmznEd81N9TVqpA0d-tRHJKV7DpmNsl9AwcETXYP5Co3Rba4KrYFpO-mNPW-pf4OkaYGoXDGIercfWqXfIkma0lRHuVl4aE9E8LSNMkzsflepeUSdzKlH2SiaF_mQ18D66rKPWQnB_SJtOcHqT43mDGx67lvn8OYMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6911c9232.mp4?token=Fr7xoSlPHL1GmKAsuLzjdOoL-0xyjX-KwnqTL9byumyvUqCYorSbYw6AuM5jaxS_nBNcf8nMc0EjRx0yA7jv9vD92cUxiTmOI0ystX5ZTnTTXzLxBu00dM4qN27JoKkPgEUILSEYUbMxNghm8lBGqa1MN78m8XzklqY3CHVSPB_i7jk48Kb5kmznEd81N9TVqpA0d-tRHJKV7DpmNsl9AwcETXYP5Co3Rba4KrYFpO-mNPW-pf4OkaYGoXDGIercfWqXfIkma0lRHuVl4aE9E8LSNMkzsflepeUSdzKlH2SiaF_mQ18D66rKPWQnB_SJtOcHqT43mDGx67lvn8OYMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک لیوان آب سرد به‌راحتی فرق زعفران اصل و تقلبی رو متوجه شوید
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/695651" target="_blank">📅 23:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695650">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سردار فدوی: ایران و عمان بر تنگه هرمز حاکم هستند و قوانین تنگه هرمز را ما می نویسیم و در حال اجرا است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/695650" target="_blank">📅 23:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695649">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944336ecbf.mp4?token=nTOuB5yERH9wv6D6gVs8tygnf6BmMZXp31eonoQgXKMgCPv1BUhTheWjr3owMEtdNBX9ufEA6TY83-QMODcENvfbRWkl5OL35LYZ7qIQk7pVbVPtX-ZM8ZHlONbfVr9mkXvxXN6F2filRdLFjFlD2DciPFZ1ehgASvW1hzqt54oEa-Oy_pG-MaV47vd4oHehXdLLnjgF09zvaNe2g6T6_uRyXOZYhc36TShQGGdJZt2n0U04f0zSAHhRHqQC_DXm93OhU8pt43mFIgkc4cB6E91H178y-q1YmrzEnEYcrYr4I72vJMgDNKNwtmW5DH7W6hzBqMFY8k_9_9-2hPRCDXmiuvSJafyMxwTCXcBx_PnQR3rdJpWI8C7ZS8BnSsiydGlSFTXFJ2LsA8c6o0b86scFItBlbvQDyrMhK7aLRWiJxxsakiht23lSeQdS1JTLDj4CQpMOkBTXaiMViwJpbUVyStEIYXhQLEd9LYPzOnjsCs6v2yFR5dnVIJy4TYCa8yUQIMN2vkrqU2EIvdGFQ3_9TZerd6aAEOgNYf-QFarGFV_xUigN1mWnM0SUbusRD5IrpRTnVUbuKXts67ofgYiEJAdT2t79ybzTP24CJ7qqXY5nXZHE1EONCJJ-yw5djjq5ZHw2l-fFZOIu6jprSfDs3vQ82I-7in40HBe1F-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944336ecbf.mp4?token=nTOuB5yERH9wv6D6gVs8tygnf6BmMZXp31eonoQgXKMgCPv1BUhTheWjr3owMEtdNBX9ufEA6TY83-QMODcENvfbRWkl5OL35LYZ7qIQk7pVbVPtX-ZM8ZHlONbfVr9mkXvxXN6F2filRdLFjFlD2DciPFZ1ehgASvW1hzqt54oEa-Oy_pG-MaV47vd4oHehXdLLnjgF09zvaNe2g6T6_uRyXOZYhc36TShQGGdJZt2n0U04f0zSAHhRHqQC_DXm93OhU8pt43mFIgkc4cB6E91H178y-q1YmrzEnEYcrYr4I72vJMgDNKNwtmW5DH7W6hzBqMFY8k_9_9-2hPRCDXmiuvSJafyMxwTCXcBx_PnQR3rdJpWI8C7ZS8BnSsiydGlSFTXFJ2LsA8c6o0b86scFItBlbvQDyrMhK7aLRWiJxxsakiht23lSeQdS1JTLDj4CQpMOkBTXaiMViwJpbUVyStEIYXhQLEd9LYPzOnjsCs6v2yFR5dnVIJy4TYCa8yUQIMN2vkrqU2EIvdGFQ3_9TZerd6aAEOgNYf-QFarGFV_xUigN1mWnM0SUbusRD5IrpRTnVUbuKXts67ofgYiEJAdT2t79ybzTP24CJ7qqXY5nXZHE1EONCJJ-yw5djjq5ZHw2l-fFZOIu6jprSfDs3vQ82I-7in40HBe1F-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‌مدارس ایذه غیرحضوری شد/ مدارس شیفت صبح در ایذه خوزستان، امروز یکشنبه به دلیل بارش باران و سیلاب غیرحضوری شد  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/695649" target="_blank">📅 23:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695648">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 6- میدان ششم، قصد</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/695648" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان ششم، قصد
🔹
در عملی سالکانه نیت، قصد و اراده، معنا و مفهومی مجزا و جداگانه دارند.
🔹
با یاری رساندن به پروردگار، در حالی که وی نیازی به کمک از سوی ما ندارد، نشان‌دهنده‌ ارادت و قصد ما در طول مسیر می‌باشد.
🔹
استحکام قدم‌های ما و استواری گام‌هایمان مانع از رخنه کردن ترس در وجودمان خواهد شد.
🔹
قصد ما ترک هرچه غیر از او و روی‌آوری به خود اوست.
قصد سه قسم دارد:
🔹
قصد تن به خدمت: از جهد نیاسودن_از تنعم بکاستن_فراغت جستن
🔹
قصد دل به معرفت: رنج کشیدن_به ضرورت زیستن_خلوت گزیدن
🔹
قصد جان به محنت: نازک‌دل بودن_از سماع ناشکیب شدن_به مرگ گراییدن
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/695648" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695647">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سردار فدوی: قیمت گازوئیل در اروپا ۲ یورو شده که یعنی ۷۰۰ هزار تومان
🔹
ما اینجا ۱۰ هزار تومان پول بنزین می‌دهیم که حتی یک دلار هم نمی‌شود و اصلا متوجه نمی‌شویم گازوئیل لیتری ۲ یورویی یعنی چه.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/695647" target="_blank">📅 23:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695646">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
مدارس پنج شهرستان سیستان‌وبلوچستان فردا به‌دلیل وزش باد شدید، طوفان گردوخاک و افزایش غلظت ریزگردها تعطیل شد
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/695646" target="_blank">📅 22:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695645">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f64fad2c13.mp4?token=JRFbyeM8xNWMKATw4S_gsKFH1NFiKtUE-dF20Rc8B-RnbNRdV2MuzuB0oPaByMUSw3hn8OUkFCzjuSwWAUH5PJh-9_YR1sb05_ccXB1PSAP9OSbpfARDyuXIL0mvYNdQAKayEKyv0wNC-h0Zw14IYQoYhrsP-vQ3yiAj-jnoJEUcVXlDShaGHDqwGFcwmZ7jk94rbBpdpFo4Pj6Fwp_V1xqQ8plOU9DszztWLsNdwlUB6K88VBHqNPFNNpApsavPopRkVbaHooejyQ634sovzRPNiL3Br0JTCmqcX6PUnFCJ74c54-xGDjLPVVb4g5jbku1sXG7-NaS8FMvmh4pv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f64fad2c13.mp4?token=JRFbyeM8xNWMKATw4S_gsKFH1NFiKtUE-dF20Rc8B-RnbNRdV2MuzuB0oPaByMUSw3hn8OUkFCzjuSwWAUH5PJh-9_YR1sb05_ccXB1PSAP9OSbpfARDyuXIL0mvYNdQAKayEKyv0wNC-h0Zw14IYQoYhrsP-vQ3yiAj-jnoJEUcVXlDShaGHDqwGFcwmZ7jk94rbBpdpFo4Pj6Fwp_V1xqQ8plOU9DszztWLsNdwlUB6K88VBHqNPFNNpApsavPopRkVbaHooejyQ634sovzRPNiL3Br0JTCmqcX6PUnFCJ74c54-xGDjLPVVb4g5jbku1sXG7-NaS8FMvmh4pv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار فدوی: قیمت گازوئیل در اروپا ۲ یورو شده که یعنی ۷۰۰ هزار تومان
🔹
ما اینجا ۱۰ هزار تومان پول بنزین می‌دهیم که حتی یک دلار هم نمی‌شود و اصلا متوجه نمی‌شویم گازوئیل لیتری ۲ یورویی یعنی چه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/695645" target="_blank">📅 22:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695644">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سردار فدوی: ملوانان کشتی‌ها علنا اعلام کردند که توسط آمریکا مجبور شدند از مسیر جنوبی تنگه هرمز عبور کنند
🔹
برای نخستین بار هیچ شناور آمریکایی در خلیج فارس، تنگه هرمز و دریای عمان حضور ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/695644" target="_blank">📅 22:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695643">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4225e108.mp4?token=edm6mYkSvMxI82Lex2D71qT-Oo60P9czXxk4BrOVjridbCYy9cNz7wqmzTJ96kFJOHdRPJBShyDgiCShbj0FbrIX2VEY38YIX5MhDHiU4B6cFwGwzghmGsku4haswXRBZttuirdcY5rQFptj2Gz75M7i_0Or8OHHlrumV54Tgn3F_F6-4yW1XgOr3a3ATqmKzJfjjHm1mRIsCYIqf8bkijOJhvVjdIrvXFdYj2ZdHX4wyWBVxP1LdGMd-GmeJtgXMhYRhnhrY9c69JPUHkY0HMxUcrmByq4_kJyv6EFNPdubfBuwcqZCFAzgqPro7tWEyhOJ5WbaYXPgZzfikN-PbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4225e108.mp4?token=edm6mYkSvMxI82Lex2D71qT-Oo60P9czXxk4BrOVjridbCYy9cNz7wqmzTJ96kFJOHdRPJBShyDgiCShbj0FbrIX2VEY38YIX5MhDHiU4B6cFwGwzghmGsku4haswXRBZttuirdcY5rQFptj2Gz75M7i_0Or8OHHlrumV54Tgn3F_F6-4yW1XgOr3a3ATqmKzJfjjHm1mRIsCYIqf8bkijOJhvVjdIrvXFdYj2ZdHX4wyWBVxP1LdGMd-GmeJtgXMhYRhnhrY9c69JPUHkY0HMxUcrmByq4_kJyv6EFNPdubfBuwcqZCFAzgqPro7tWEyhOJ5WbaYXPgZzfikN-PbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای یمنی: شهر تربه به فضل خدا آزاد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/695643" target="_blank">📅 22:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695642">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq-t80hYLWO0RRVJLkajIhAnOcKLe-xnYm229CN9FCbdQ6ux4mSyb6GYKzxdFwy1Siu4UWTF5_bLp3s-RjEtRVezcms_Fn8iQ8lRvFAUQyGJMd3ftMHhuCLJP40PI8SLdJM2KPHGOrpCXAIkfipCyArfc8oLAe3k2rraSPHwpVdfrLtjrMsoK-KmD6FhoKwVq5bpyAD_g5gZTSRZzFZeJpWS2aDhwVCGtpUHYxr727vZCQfBCmN1EMUUtMwvf73GR80sDpZX3Fo-sBCpQnE3KMBnqPHQ0ddsFocvXc70selOHi9gzU2X7JH90orbZdpZZE-wEu53XoWt3Px_1AdSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ مصاحبه رتبه‌های برتر کنکور، پیش از اعلام نتایج در فضای مجازی وایرال شده؛ حالا سؤال کاربران این است که مؤسسات چطور قبل از اعلام نتایج به رتبه‌های برتر دسترسی پیدا کرده‌اند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/695642" target="_blank">📅 22:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695640">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQqok0st5dqaNtxGHDKBN7stTnlREwKuuz-QoEI27UcLCjnI4-c5XvZEKiDYDwqN0r4j4kDPC59ZwN3tW8t79-PZH6kTblsseyFFEdVbaquthtsCKL1L8Rqt60R8DMABwxKKMO9y78v-9oxPjFskMkR-XTmg0Aug5z8_5pNi98jY9KUEcPPRvnjNIRAEArY2T93i8YYUOAiIT9OWincMDwWeyFH_76WjxdHh7TEtHaaP2wv-aUp8UCjCMiMyIRpQpiXwPw_vfrQjaG9_t6Edqy7h5rB0ABBVVJeC1dzzSlAoXxw1UroxoDLRe_Ei8Ubp2ySK4viMoVF8tbwG2wI9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/695640" target="_blank">📅 22:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695639">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEhZ-WaCKz_62V_OpiZKpy_RSda52c-N_jJUMokiGETvL0CMD553ETd0nlFED6Pc2-YXhVQXFpZ7fNCUA19DO2EMjIW5zmVaxwL6iQPDrnIDM8Mu4Y2HkJZYrgBUny-kPVctD-heURbMufrX-aDIEwqYvJnmDyBuqFlll_wcTqeNwwHL_LjfzVxOWRZIzFe9a3jycDhXto0DKUDt77AzaEh8kLaqtI7V5GQ5WgQmJv7fT4w1s4h9w9xF6uHumeeGk1IH9sXOgxAovJqb3k7PYrEVHpoVgnzF_veKBlvroKXTMOFJl1laMBZEJruvHN6qclCU979MV8K3x-X_JH8Lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای مقایسه قبل از خرید، بیمه بازار داره!
وقتی می‌خواستم بیمه‌ام رو تمدید کنم، ترجیح دادم اول برم سراغ
بازارش
!
✅
چون می‌خواستم
قیمت‌ها
و
پوشش‌های
همه شرکت‌ها رو کنار هم بذارم، با دقت
مقایسه‌شون
کنم و
مناسب‌ترین
تصمیم رو نسبت به شرایط خودم بگیرم.
تازه، هزینه‌ش رو هم در
۱۱ قسط
پرداخت کردم؛ بدون اینکه دغدغه ای داشته باشم!
👈
برای مقایسه و خرید بیمه وارد بازارش شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/695639" target="_blank">📅 22:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695637">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiVr7V-mi8k5elzV0QdqqAb27WtsHh7RBHleGJlieIgpSkO3n0qCCXTKX91WTlhdZ1RnQQeCjzGbg3cMj79b8arzgCf7d-5v_JtFVuyY0lWUfSW6vPlHEIRCUUs7gM4Q34YOfBi5f8EdAz31zE4s-00C-_AGGm-o-mGidbZikBVY0_3El75wlAY4akNYCKvOooYowPFq1f8IprACnUS7NwL2Y48bvcnHitwApjnKlvpqcmQCGpFdPEtIhh-yY32kd595CMObS9EQ5MEfbSpOUl2uxsEpELiUPG8T7jp4Jyb0mgYZMkvGL7Gh1Egoizjx38VrHXo_uIV0Y_uYoKK-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: گزارش های مبنی بر
حمله به یک کشتی در تنگه باب‌المندب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/695637" target="_blank">📅 22:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695635">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
تغییراتی در کابینه رخ خواهد داد/ دولت شروع نکند مجلس دست بکار می‌شود
علیرضا سلیمی، عضو هیات رییسه مجلس:
🔹
از هفته آینده و با مجوز شورای عالی امنیت ملی جلسات مجلس به محل قبل بازخواهد گشت.
🔹
بخشی از مجلس در صحن است و بخشی به صورت مکمل و وبیناری برگزار خواهد شد.
استیضاح حق نمایندگان محترم هست و باید روند خود را طی کند.
🔹
اولویت ما این است که خود دولت دست به ترمیم بزند و شنیده‌ها حاکی از تغییرات است.
🔹
اگر دولت تصمیم نگیرد آنوقت مجلس از ظرفیت‌های خودش استفاده خواهد کرد./خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/695635" target="_blank">📅 22:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695634">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/695634" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695632">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekvjWU8jAzwIBS4ezZNtS1DXLwEZ_v-3JJsw7PMCnhXgIT1Tw-YiKFXt7kK6UIGO1d1I8IJqkUd1qYwkql2MuPo_npIATjpvxOUq47gbLDrdFJZ0qqRDJfgqw9SpPxSAHbHVLkZ34p7ddrYox3hTv5BSlS7tWTdJD26B2xNNOF7H2Dkf_mzHKV_WJk4q0FTRhzICuxOuAi8u3HoXjq6vG9MYbYz_uHCKmkJQrMxV13ScqMnuOhcxoYfYQwkViMzrYQNL1NxjQrpzz4pRZYFH58U-hWfMn7mGi3TlP-sccZv-71XbAud5zP4exeNx5NlQvgZlpe2-mS2de9p8XcYocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای و سیاسی یمنی: یک توطئه شوم در جریان است
!
🔹
پهپادهای «لوکاس» ساخت آمریکا به مناطق تحت کنترل عربستان در الجوف منتقل شده‌اند تا در طرحی تحت نظارت تیم سلطنتی عربستان، به سمت مکه و مناطق اطراف مسجدالحرام حمله کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/695632" target="_blank">📅 22:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695631">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حقوق کارکنان متناسب با تورم ۸۰ درصدی نیست/ در متمم بودجه امسال حتما باید افزایش حقوق دوباره لحاظ شود
پیمان فلسفی نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
کف حقوق کارکنان دولت پایین است و باید مناسب با تورم سالیانه باشد؛ در حال حاضر تورم به ۸۰ و ۹۰ درصد رسیده است.
🔹
ما پیشنهاد دادیم و رییس مجلس نیز مورد تاکید قرار داد که امسال دو بار افزایش حقوق خواهیم داد و در متمم بودجه امسال حتما باید این کار انجام شود.
🔹
قانونی را پیشنهاد دادیم و برای اقتصاد مقاومتی آماده کردیم که عدد نرخ و ارز، رشد قیمت ارز را ثابت در نظر بگیرد.
🔹
تنها کشوری هستیم (شاید بشود گفت یک یا دو کشور دیگر مشابه ما هستند) که شناور مدیریت شده قیمت ارز پیش می‌رود. در کشورهای دیگر نرخ ارز ثابت است یا افزایش بسیار جزیی دارد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/695631" target="_blank">📅 22:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695630">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkfMfVPruZ9QlpmASmZExmzKumgiZgYRRTLbbEQERif0UuKGEMb7hZdu_iSv2z0Ejp8Y7nJR-hqrhpsWsEYT_NUktfG2i3pCapza26_IhEldSYEfD458yDJ8kyeXTrcDAxXhp4gcHsulCIEkiKjZYwALcFzUd1I2zeWyKQU9y9J1f1vxWERVUaQ9jy7ojFUmQPFWPUUGKCkjH1mdZNpJQWtkAiLUTV71SYBpGaoRLUzyn16U5M8Ygh40ykvUVu2lOA5jdgMK0bhxd1kH76qPldzIGF3AlWAoo7KYNVsTAqfZPWFOSVR7Lu1C7cBKu6kV9YW5OJekL6GmyUsGFiYyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: عربستان پروژه ورزشگاه ۲.۵ میلیارد دلاری نئوم برای جام جهانی ۲۰۳۴ را متوقف کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/695630" target="_blank">📅 21:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695629">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-yiIfmy20qWCzJXRJt8cgWGErekFzl1dAJKEmOqaDyFJ2GGSP2Pj2hosXFVNS_ZfsTXg5iim6LZ7-VwkNmx8bMoolrEqbbHAzN-zGPQwZRiGOZG576IVuy0SGL7JGBbbCgkMiCKMfgKlUHZ4l6AVzRfTJJ8nRQXJ4hY1uHiXn18KSRQQKnYT3eMqZvLPjwMUo25k5hYEyADrDRuDMUaz2e8Yakm0qQcyy0SZhc1VSmaSzv5kWURR_vqV7M45hcEvTKhHX6jFU-NO4_cWl1fQbSUlqyYeO-HQNC4qQD9bnR4ATzGkhQizKb908_6VQGvzNdGfb_QGV8iSLP_PbESCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نفت استعفا داد   معاون دفتر پزشکیان:
🔹
با پذیرش استعفای محسن پاک نژاد طی حکمی از سوی دکتر پزشکیان رئیس جمهور، حمید بورد به عنوان سرپرست وزارت نفت منصوب شد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/695629" target="_blank">📅 21:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMMkYlZrRYVBgGL9ZBAyymfqUBoVDgSiIqaj6cU4Pdjy9w6D57d67iYFN_gD-psEBVz55t0dlEa050Y3HKcJrFP_CBjb7-OVEAa5RJ_3Zqyic94Mhky2qQZHgBsbQhZSOV2LVS878ePxH0diA_cNR7ZES45mAhl5x2vmE4CKCf9zJtUBJ5K4_HANCpSWModNNLQJqZg1hz2fpjsCZFv44HM9-WjfqOK1Cf-wo6F6-tepHJ2PPcMVunGN4L0C_oUmteXI_jFTyiy50HHnFu_7shdn_dR7E2o6IEiczhYdf3YBj7yodQ4h3m7g5kAdFRF8jPx7IjI_7BEwo-bUGP3pZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصغر فرهادی، کارگردان سینما: اصلا چه کسی از آمریکایی‌ها خواسته بیان مارو نجات بدن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/695628" target="_blank">📅 21:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695627">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c040077d42.mp4?token=Op-u5AHhx9GYoHZQjD2vu73YLUUo_2AKosd51mDZ-XafdmRygDpYrlNuKvO7V0ZPOiqeTdyHK6x6OVF3onmpzuEec7Zv2ZMaS5bRj_sjmkfRU9Jehiyuh23VXicbFBNVZpHPx1fAEioKE7luCujxUuzX2n-cqTy33QU8J8D9egaXRR1r5fuwV7LZG_QAf4CnEBhWbRtPFSG5m5-pROI5Kxd7C1l7D7Olu2GY5E16a4bFKLgQdYzx_w5IuttUd-x13Y0hCN1lUMbDUOE8iYS2Djeqi3uT3vWcOtIplYJk-fGGBuZOw0ZDYHoGYWkEAVmSkjWRw6LQjA1EUZdEKru3wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c040077d42.mp4?token=Op-u5AHhx9GYoHZQjD2vu73YLUUo_2AKosd51mDZ-XafdmRygDpYrlNuKvO7V0ZPOiqeTdyHK6x6OVF3onmpzuEec7Zv2ZMaS5bRj_sjmkfRU9Jehiyuh23VXicbFBNVZpHPx1fAEioKE7luCujxUuzX2n-cqTy33QU8J8D9egaXRR1r5fuwV7LZG_QAf4CnEBhWbRtPFSG5m5-pROI5Kxd7C1l7D7Olu2GY5E16a4bFKLgQdYzx_w5IuttUd-x13Y0hCN1lUMbDUOE8iYS2Djeqi3uT3vWcOtIplYJk-fGGBuZOw0ZDYHoGYWkEAVmSkjWRw6LQjA1EUZdEKru3wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
والله واگذاری زمین به مردم هیچ هزینه‌ای برای دولت ندارد!
عبدالجلال ایری، سخنگوی کمیسیون عمران مجلس:
🔹
اگر زمین به جوانان واگذار می‌شد، دست‌کم ۵۰ درصد هزینه مسکن جبران می‌شد؛ این زمین‌ها متعلق به خود مردم و بیت‌المال است و دولت نباید روی آن‌ها چنبره بزند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/695627" target="_blank">📅 21:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695626">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم از سمت دریا شنیده شد؛ اصابتی در سطح جزیره گزارش نشده است/ ایرنا  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/695626" target="_blank">📅 21:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشبکه اقتصاد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS5c3z7BefcO5xkepwjuO7VrNsVYrMH8wRi2NIOCkIr1K711Buplx1aQY-36Dku6_ciPWsYo_cWeP6a_bgo4UpwfkJVffptQuoLD6NjM1FZ4WYpdA_EeP9r4XC4Lu2I2XUpNTrRBmlg6IZG4wtY8zmnwq29IuncYsYejeS7Fspz5ZSY2dWTgKQ75NHoNZS81hleWviKoayDIHWSorvOcoYVKXy2fGeEdA2rWkbzVargMFptKFsOVNh_6tPFgDDhV2GYifGuSbb0RWI1VDM061oYuv4eCKZC-C3jJlDbjm5qR8-Tz89rs4A4sT7IkvUdxaYoi6WqGYAD_6P27lP6iEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش فعال رسانه‌ای به تقسیم کار علیه دولت
🔹
داوود حشمتی، فعال رسانه‌ای و روزنامه‌نگار در شبکه‌ای ایکس نوشت:
دلار بالا میره و تقسیم کار شده
‏عده ای میگن: چرا دولت کشور را رها کرده؟
‏دولت شروع به فروش ارز میکند
‏دسته دیگر واردشده بامغزهای ⁧
#کوچک_زنگزده
⁩ میگن: چرا دولت ارز میفروشند. مردم ندارند ۱۰ هزار دلار بخرند
‏نه عزیز. درد شما درد مردم نیست. درد سرمایه داران است که میترسند قیمت دلار کم بشه.
#شبکه_اقتصاد
@economynetwork</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/695624" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/albRsflM8ffhKog-CIYx2NICGjWiIQ7PMmimKh4aV_fmXGZ9Eu1S9oktQRTkaQnpNwObt9d3Fv4et205Kdl4MMCjbVrA_xYHrtFTRj8KlPi5dhvlBaz-ioBt1EDZByEORhwN5zvQlf-r_taZUsTxfc7njwI8VKAmkR-0cyicWbCH4hXls9ATVqFR8D83bpZrsU4XpCyUzalg54oxgZuwf_FZv9dc_i6Q3qK3MNS7HsYToP-RIClskOPzJrus4LPxRN8HSP2GMzGXfTuRmTvNLtXcNMWtdxJzd70u85ZZCAD0wvsFs3pGH6QvK6rpfqMAi96v4xwigu1OLW9Df7Vx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ مدعی شد: ما با دانمارک و گرینلند به توافقی رسیده‌ایم که به ما کنترل دائمی بر امنیت و سایر نیازهای گرینلند می‌دهد #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/695623" target="_blank">📅 21:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9500e3685b.mp4?token=dUO2V38y2P5PaZqvMIRVM8e_xBN3RORNoUCgsZ-KQ7ayn2-zwRS9UNicLDerqEZZjrUW2ANzIjWqohSyUgpCTrlLjbLwMMmme0uYBjX7qxtYDtd2h1MRvZSKvyrcWHCCMAyV2Ou0qZNb3TJD3P6cfoYekitJeqET6tB1o7EFF2h98ZnBKmfZPdYPLn_PyxQFoY2oQU4AEcIB1CFl4gc9Yg8iFXKB32T7znNAAdUYOr9uUqh3rK2iA8lQosQZd1Pkzp2Tuqn_kNmP8XcHoc0PCFF2VeiCJXuufN3RIIXWCIV5t2ZYShbjhVGedjWx0p2isYyx5idEeXsIutqHcUZvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9500e3685b.mp4?token=dUO2V38y2P5PaZqvMIRVM8e_xBN3RORNoUCgsZ-KQ7ayn2-zwRS9UNicLDerqEZZjrUW2ANzIjWqohSyUgpCTrlLjbLwMMmme0uYBjX7qxtYDtd2h1MRvZSKvyrcWHCCMAyV2Ou0qZNb3TJD3P6cfoYekitJeqET6tB1o7EFF2h98ZnBKmfZPdYPLn_PyxQFoY2oQU4AEcIB1CFl4gc9Yg8iFXKB32T7znNAAdUYOr9uUqh3rK2iA8lQosQZd1Pkzp2Tuqn_kNmP8XcHoc0PCFF2VeiCJXuufN3RIIXWCIV5t2ZYShbjhVGedjWx0p2isYyx5idEeXsIutqHcUZvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روحانی: اصلاً من نه کلمه رفراندوم را گفتم و نه کلمه همه‌پرسی را
🔹
بحث من، لزوم برخورداری «اهداف ملی» از پشتوانه مردم بوده است، نه برگزاری همه‌پرسی درباره دفاع در برابر تجاوز
🔹
اینکه جزو بدیهیات است که وقتی به ما تجاوز بشود، باید دفاع کنیم
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/695622" target="_blank">📅 21:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695620">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a0e649e7.mp4?token=ptIK56czXZPzRE2D4UyP-RltbWzFjxDMoQ_mnkgsdd9aQqURUjpfIBHb_jAMGOrGn48DO_ggU0QwDsSCEdFv7SOJDCxXm6qE0FrZ6W7R8l28gVGzwuBb2yZeIqKNcUu0JyWr2My9z2xtwn7LF1lJPJF2x41ApVwJmp4oKHYX4nuxmescH-ooPy8WeE_Einl4BM6_qP_VD0MaWP9m9dq_PsnCA2IyWjsFkJ7vB70WPxHpbE2ArdrF-MdYQBFYixtXMyvBH_GMmn2H-g7TLmIjmDmuoLqypG6ilu-2CspEejAcWB3XGeo4nBZQlFaF-aHetstl-KwOvmgL7SrhF0T9h2KYZH0UApi2KvX_rhNT6U_BmCmjjEa5ZuFLfgMoo_2CEaYY55plQpBafoHewMRMKfTrpInCSKM_7I60I05LbPDRPYxMcnoDa0pu0L0dicoNlXcyECDtkfsNrmjbaROGflZLeACrxWtnwlObxSz3YP-F76GVzwpMAdUH9GRfAJ6akvSthbm1kkR3zkirMs2t9RXu2xXgQj2NZLCJ5kFs_-A4zVysWJpSEIQfP7EvM01eS_2ERt6P4F781bnWFPfTiSdq9FvTk-Au5TZjg2K51DMHToSlCCSRynyjAzVuN-QO8l-hx_8GNTNom_3w_StKLOreyvc7SE6ZSQLxgWQpKtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a0e649e7.mp4?token=ptIK56czXZPzRE2D4UyP-RltbWzFjxDMoQ_mnkgsdd9aQqURUjpfIBHb_jAMGOrGn48DO_ggU0QwDsSCEdFv7SOJDCxXm6qE0FrZ6W7R8l28gVGzwuBb2yZeIqKNcUu0JyWr2My9z2xtwn7LF1lJPJF2x41ApVwJmp4oKHYX4nuxmescH-ooPy8WeE_Einl4BM6_qP_VD0MaWP9m9dq_PsnCA2IyWjsFkJ7vB70WPxHpbE2ArdrF-MdYQBFYixtXMyvBH_GMmn2H-g7TLmIjmDmuoLqypG6ilu-2CspEejAcWB3XGeo4nBZQlFaF-aHetstl-KwOvmgL7SrhF0T9h2KYZH0UApi2KvX_rhNT6U_BmCmjjEa5ZuFLfgMoo_2CEaYY55plQpBafoHewMRMKfTrpInCSKM_7I60I05LbPDRPYxMcnoDa0pu0L0dicoNlXcyECDtkfsNrmjbaROGflZLeACrxWtnwlObxSz3YP-F76GVzwpMAdUH9GRfAJ6akvSthbm1kkR3zkirMs2t9RXu2xXgQj2NZLCJ5kFs_-A4zVysWJpSEIQfP7EvM01eS_2ERt6P4F781bnWFPfTiSdq9FvTk-Au5TZjg2K51DMHToSlCCSRynyjAzVuN-QO8l-hx_8GNTNom_3w_StKLOreyvc7SE6ZSQLxgWQpKtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلف خرها، برنج روی مزرعه را هنوز برداشت نشده به ثمن بخس خریدند و با قیمتی چندبرابر می‌فروشند
پیمان فلسفی، نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
برای برنج سال گذشته پیشنهاد دادم که شما ۱۰۰ یا ۲۰۰ هزار تن از برنج تولیدی کشاورزها را وارد چرخه تعاونی‌ها کنید، دست واسطه‌ها قطع می شوند.
🔹
آنقدر تعلل کردند که سلف خرها و فرصت طلبان برنج را به صورت شلتوک خریداری کردند.
🔹
برنج روی مزرعه هنوز برداشت نشده به ثمن بخس از طریق دلالها و واسطه های بزرگ از کشاورز خریداری می‌شود که به واسطه همین عملکردشان قیمت محصولات کشاورزی را روزبه روز بالا می‌برند.
🔹
عملا سود نصیب کشاورز نشد، این‌ها در انبار و سیلوهای آقایان ذخیره می‌شود و در زمان مشخصی که خودشان تشخیص می‌دهند با قیمتی چندبرابر به فروش می‌رسانند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/695620" target="_blank">📅 21:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695619">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
قتل همکلاسی بعد از زنگ آخر مدرسه!
🔹
اختلاف دو نوجوان در سال ۱۴۰۲ پس از تعطیلی مدرسه به درگیری با چاقو در پارکی نزدیک مدرسه منجر شد؛ یکی از آنها مدعی است همکلاسی‌اش او را به پارک کشانده و از پشت به او حمله کرده است.
🔹
متهم اصل ضربات چاقو را پذیرفت اما قصد قتل را رد کرد و گفت هدفش «زهرچشم گرفتن» بوده است؛ قضات دادگاه کیفری یک استان تهران پس از بررسی اظهارات طرفین برای صدور رأی وارد شور شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/695619" target="_blank">📅 21:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695618">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMav04ojeisu4a-tzff1agy_oT5qdtYRjIKSQnrfJtouqf4CbvkAiiMOg-6Ytng_LcBAaXGLxN2ET-YjYVaJOHAk33LU5rZJtCaXLFuj6qbC91RSWTDsG7cZdbY4kMC6L5k1FQovd5sS-6EIWXw7UhvlcEqNE7p9LGSyydvLjx4nLD7HRRy4Hj-oIO-HSdTaq5h5vgiP43rI7rS4kPQK7gzF_Z6V8a-zBh__2u0kWmbwYYKpeR9us-6uUYMMR5g3kzAw4ndwrL8OTJdeU69Xl_9t6R6Q1Goa0hEx7XfVElsm5nOZb-e65SBRpPFEiKRipXNV5dbEYnepTlNoBvNMxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو هانکه، اقتصاددان برجسته دانشگاه جان‌هاپکینز: حالا در این جنگی که خودمان انتخاب کردیم و علیه ایران به راه انداختیم، کجا هستیم؟
🔹
ما داریم بدجوری شکست می‌خوریم؛ تنگه هرمز پیش از جنگ باز بود و مشکلی وجود نداشت. حالا با یک مشکل جدی مواجه هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/695618" target="_blank">📅 21:25 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
