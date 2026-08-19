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
<img src="https://cdn4.telesco.pe/file/iPWQWdF9gImhvKyPevOeSYFxGjGXXb8G2mt_6z_dmyFC7IMMvvMn1qNI9PZjSgFQtCiv51QvB5T_lLVM21t65zCVIdqan2xapyWaMUqnnOVtSkPZx4p1Owt5x1XCN98EIb2rsZY-x2XwTjpttgWT-ozqJsJQtI_YWFiWAwMMZR4Q7jNgezdlpeo7XbrjcXSyRfQMVQ9aLOr801a8eUR-DhG90hYBRjtph643B84UVHJGG_BlkSSo7ahjLQ3W9wtXBOhmitCdwIBrDgy3pJW_m_IVTwqoNnrGqimLPLhAei9h4gqzZxKHgI4nCi4QFw0jKdtfGThsBTaNRloS7QRJhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 20:23:29</div>
<hr>

<div class="tg-post" id="msg-457056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=OJ5cYBGHGv7ndA792njjcOEuTsSgXtWSVk8G7Qu95Zi9HfKyHKLeM-zqWEYdtxZm7QenI0aQTPWmXi4o-IJWdCBqVbfrLJG2Yu1aWMuEUrJP1b70tuoBK-Ka7kiYXLVqZXF4C_Y2uYDj2wI7mx5J5TeDG5RsA5OPhba9421KSov9YNem3ETXFsE84I4UJWZ_kBI82xtfwgGqRNa-opyKNKa3AF_E8TQxXn1b5pLfyQAeeyNZ1F12rVqa4-nLGqjtVUapHKOO_Bq06Dg9J-_EN_EYyw5szNF6OF6hb37jhWo3C_qVnngluHaQF16UVvv_BssD8Tmdl6t5JDC39g5NGiWSTDgkd_0wqEy_DxQbWnxMSGrgRQFKRrSIjKmeVPLThSDVvE1psiWB3MxbXXkULuu52Yao0fEx6MO5qB-rTvw-Xs9Ck5wGW8ePIV-fv20ZamX7u1SOhhMraC5z8-8oPBsEUNsSTcP0GoUrPasMrMV-OEIuvNTQWHYR1cGBUAJ2EbX7JM5DEDzDAAMEf5KKSenBGaGJDor6peR30h5iyra7KA0pVvgLX1L4QAWoR-Z8_DELfcQP-7GKsvl4fY8b89eQNJSxrewPQq-bB09zSYVZD2RGtQ3wamPdxumt901_go2NW8npdaAwBTEfjm61tPcrtIg5gTg9HJsJ6s0A5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=OJ5cYBGHGv7ndA792njjcOEuTsSgXtWSVk8G7Qu95Zi9HfKyHKLeM-zqWEYdtxZm7QenI0aQTPWmXi4o-IJWdCBqVbfrLJG2Yu1aWMuEUrJP1b70tuoBK-Ka7kiYXLVqZXF4C_Y2uYDj2wI7mx5J5TeDG5RsA5OPhba9421KSov9YNem3ETXFsE84I4UJWZ_kBI82xtfwgGqRNa-opyKNKa3AF_E8TQxXn1b5pLfyQAeeyNZ1F12rVqa4-nLGqjtVUapHKOO_Bq06Dg9J-_EN_EYyw5szNF6OF6hb37jhWo3C_qVnngluHaQF16UVvv_BssD8Tmdl6t5JDC39g5NGiWSTDgkd_0wqEy_DxQbWnxMSGrgRQFKRrSIjKmeVPLThSDVvE1psiWB3MxbXXkULuu52Yao0fEx6MO5qB-rTvw-Xs9Ck5wGW8ePIV-fv20ZamX7u1SOhhMraC5z8-8oPBsEUNsSTcP0GoUrPasMrMV-OEIuvNTQWHYR1cGBUAJ2EbX7JM5DEDzDAAMEf5KKSenBGaGJDor6peR30h5iyra7KA0pVvgLX1L4QAWoR-Z8_DELfcQP-7GKsvl4fY8b89eQNJSxrewPQq-bB09zSYVZD2RGtQ3wamPdxumt901_go2NW8npdaAwBTEfjm61tPcrtIg5gTg9HJsJ6s0A5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «الله اکبر» و «مرگ بر آمریکا» در مراسم بزرگداشت چهلم «آقای شهید ایران» در حرم حضرت معصومه(س)  @Farsna</div>
<div class="tg-footer">👁️ 473 · <a href="https://t.me/farsna/457056" target="_blank">📅 20:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4502fdbd.mp4?token=C9womxQCnemCrR6q3SklvUiWnlaJhh4XQMwoDA1La-YPyAlD0cSl1P5w20mZPVoVCwab7PB28ojXx2BLIlJkkM58esyvMT1tEeL05eyI21bcnS3Klf5y0fYyRwmNTpqpolKvSXivHb7wSYVsKB4khjHeqIgWLzQQ4xG6QL4dBhMILtf3dWtxsE8nArPmbBFxHlAhBxCvpwjPc605xD42Sa12pqnvlQ9_VRFUnj_fh9E40w4lDvJM9hIRQ_TYEzsBy6a5_cejnuGJKnnmbsnb6wySf_Y2kHSFGBnzTB7GJensTJcgj9MXbX6O50HWYoi5D5CpVXFH9X3tM9oSuHVtOYz0SpYDnP9OGa3Qs_0hUC_JDe-3wBwc9EDPaPWIXzNzOIORm8L6Aa6-R1PAbpMqgLB_cI4sKdVD2rHzphxAY7pysVpkhImBYefC9MtCQTZ2m0Hy9R81W354wErHoUG5a7Yk_MFWfF2wpqPgMdYy0hDtECyj_sBzZqFDYd9MyKI2szdCaOXecJB291kEzgAOHpXE8D53cBFttgZhFpfP7CeMjEqyI-3XN09-tgIhouPVBoqqpFdfPeZ9hbm7Cy5PWJFFNNHA76LG30Xrn3GBiBebVGQUyrgqgWAoGldezKsHBCniAw7eyJuqEKi9mBCEXa4x2g8tjt10BVOT_b9fizM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4502fdbd.mp4?token=C9womxQCnemCrR6q3SklvUiWnlaJhh4XQMwoDA1La-YPyAlD0cSl1P5w20mZPVoVCwab7PB28ojXx2BLIlJkkM58esyvMT1tEeL05eyI21bcnS3Klf5y0fYyRwmNTpqpolKvSXivHb7wSYVsKB4khjHeqIgWLzQQ4xG6QL4dBhMILtf3dWtxsE8nArPmbBFxHlAhBxCvpwjPc605xD42Sa12pqnvlQ9_VRFUnj_fh9E40w4lDvJM9hIRQ_TYEzsBy6a5_cejnuGJKnnmbsnb6wySf_Y2kHSFGBnzTB7GJensTJcgj9MXbX6O50HWYoi5D5CpVXFH9X3tM9oSuHVtOYz0SpYDnP9OGa3Qs_0hUC_JDe-3wBwc9EDPaPWIXzNzOIORm8L6Aa6-R1PAbpMqgLB_cI4sKdVD2rHzphxAY7pysVpkhImBYefC9MtCQTZ2m0Hy9R81W354wErHoUG5a7Yk_MFWfF2wpqPgMdYy0hDtECyj_sBzZqFDYd9MyKI2szdCaOXecJB291kEzgAOHpXE8D53cBFttgZhFpfP7CeMjEqyI-3XN09-tgIhouPVBoqqpFdfPeZ9hbm7Cy5PWJFFNNHA76LG30Xrn3GBiBebVGQUyrgqgWAoGldezKsHBCniAw7eyJuqEKi9mBCEXa4x2g8tjt10BVOT_b9fizM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گردن‌کشی یک مونتاژکار مقابل دستور قضایی
🔹
پس از انجام برخی اقدامات و تغییر کاربری غیرمجاز از سوی گروه صنعتی بهمن در یک محدوده ۱۲۰ هکتاری کشاورزی در منطقه روستای دانش شهرستان قدس و حریم منطقه ۱۸ شهرداری تهران، با دستور دادستان شهرستان قدس عوامل جهاد کشاورزی…</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/farsna/457055" target="_blank">📅 20:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df437fbc7.mp4?token=rZWM7JRtlGJnxwIs14a1ejugOM_3iG6GQprWebyfcfDXunZpbHcN28IsHcOjtmpOZuJfkS3v7esV0IrfI9e4S8EqjRcM-3lzJ52eY3i0AdfYC3w_58rrddCI_udbu3niDIQMEmKnEXMivpj0mNobKpbMmIG9-Zc47gE1mBnV7NKleZdnU9nJROQ5i2wAeh_jRIeueuwuo5J8gqOyjdSA648n8Tda0PPb37IHeiy2joJwmgHAAa_pL1P3QBCONFQxm-i1_qKyyFZyfgNh-gGTGReLwGc8rd-goUjwG9f1QYnqfV5v1Qicl3QMEoSNp42fLR4HSw3x8GuIHEren_GvBD2ytKIb29St0NPVEqPrcenZyEYYmIWv2UQBKlbFjHHRd2JzxrjNU08LwMjZLGd8CnPSFOXTucwk8wDZ8d2Ix8pknkKFiqMVocOdVtlnFjCr_nxyZFgGW7EuC1c6NHF9g5Hx0SBWqBNBQ9ui298rPLr4WduH2Pvc8lWjYZCNDABNwL2bu9xFXm6j8rQ8zPqfY0wJxfTZS7d9ZQ71EeFUppfm-skoeoxp_fbgjhXlEesS6ynb_WJkZQHBb69AjX_ZjboDj9KA0XL4yF0IJWihrQACFXr5MZeGeH5j-2pSw7znH-lDXbTu5nVt_cS0n8qug_ELlta2AaPvKoeenGux1xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df437fbc7.mp4?token=rZWM7JRtlGJnxwIs14a1ejugOM_3iG6GQprWebyfcfDXunZpbHcN28IsHcOjtmpOZuJfkS3v7esV0IrfI9e4S8EqjRcM-3lzJ52eY3i0AdfYC3w_58rrddCI_udbu3niDIQMEmKnEXMivpj0mNobKpbMmIG9-Zc47gE1mBnV7NKleZdnU9nJROQ5i2wAeh_jRIeueuwuo5J8gqOyjdSA648n8Tda0PPb37IHeiy2joJwmgHAAa_pL1P3QBCONFQxm-i1_qKyyFZyfgNh-gGTGReLwGc8rd-goUjwG9f1QYnqfV5v1Qicl3QMEoSNp42fLR4HSw3x8GuIHEren_GvBD2ytKIb29St0NPVEqPrcenZyEYYmIWv2UQBKlbFjHHRd2JzxrjNU08LwMjZLGd8CnPSFOXTucwk8wDZ8d2Ix8pknkKFiqMVocOdVtlnFjCr_nxyZFgGW7EuC1c6NHF9g5Hx0SBWqBNBQ9ui298rPLr4WduH2Pvc8lWjYZCNDABNwL2bu9xFXm6j8rQ8zPqfY0wJxfTZS7d9ZQ71EeFUppfm-skoeoxp_fbgjhXlEesS6ynb_WJkZQHBb69AjX_ZjboDj9KA0XL4yF0IJWihrQACFXr5MZeGeH5j-2pSw7znH-lDXbTu5nVt_cS0n8qug_ELlta2AaPvKoeenGux1xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار «الله اکبر» و «مرگ بر آمریکا» در مراسم بزرگداشت چهلم «آقای شهید ایران» در حرم حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/farsna/457054" target="_blank">📅 20:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43389d44f7.mp4?token=eL4Q5-LDWhri3GpONdrVpnAZJfM6gt33cIz61By5cycSonAh0In7N3tsNF6dUUwA0Ku91b8Q7T8p5uC1hXu88MSI0lXVlF5Qy0_lioi6HxDLNE_dwlozKgq3r8M-ThrhrM6H5K6rddDsDOhH9QPtuevHEM_U1yrbEY3nGjJK0bhowp0ouROy9DvSdVf2pKjJxC9eE7jSTIhF_DOxmaJvjhU6x4VZnUqTE6JDYDFQSk2lfBEs-OeK-cymN9EqL-uCcwcr5wz7PrnbqDpVvmDW2gnPkoD9HYrg43PvN7jO8oN7_Hz92mHKBODJWcpVvUzUcfb9hICZTp7DgTzHKc6BxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43389d44f7.mp4?token=eL4Q5-LDWhri3GpONdrVpnAZJfM6gt33cIz61By5cycSonAh0In7N3tsNF6dUUwA0Ku91b8Q7T8p5uC1hXu88MSI0lXVlF5Qy0_lioi6HxDLNE_dwlozKgq3r8M-ThrhrM6H5K6rddDsDOhH9QPtuevHEM_U1yrbEY3nGjJK0bhowp0ouROy9DvSdVf2pKjJxC9eE7jSTIhF_DOxmaJvjhU6x4VZnUqTE6JDYDFQSk2lfBEs-OeK-cymN9EqL-uCcwcr5wz7PrnbqDpVvmDW2gnPkoD9HYrg43PvN7jO8oN7_Hz92mHKBODJWcpVvUzUcfb9hICZTp7DgTzHKc6BxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: رئیس‌جمهور تکلیف کردند که برق صنایع قطع نشود  @Farsna</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/farsna/457053" target="_blank">📅 20:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfffd7c1ce.mp4?token=aPkvSR1LRrs9Q2Sk-T5rroUbs-NE03t-AImvVDWI7izOnQQNLLuCIlJVQOjrK2Clug6YA6eAkzdvDMW1yas503oFdE53EiNqPHFvdRCe7ffs0UNG6x6sf0dGLpPkJO6zkn3XQt2Nwj3InMC84uXswcsufSM7m3_3P_J-w9nrtM7lMwFZRhHVFgTfW77VUr_ypkDxyDH_RPzBrVdo_YE0qkYSya__IIbhY0DSMPvlUjSTV-kYu7SStE22TQLkeue0ZRUjWzmT4rR-r3D0U4lTjOVAzIFAv3-IYmZE--6zJXZNYk_E2f5-YhN0H2_1bz58lj-DMJ4UNRQSIlEqnHPJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfffd7c1ce.mp4?token=aPkvSR1LRrs9Q2Sk-T5rroUbs-NE03t-AImvVDWI7izOnQQNLLuCIlJVQOjrK2Clug6YA6eAkzdvDMW1yas503oFdE53EiNqPHFvdRCe7ffs0UNG6x6sf0dGLpPkJO6zkn3XQt2Nwj3InMC84uXswcsufSM7m3_3P_J-w9nrtM7lMwFZRhHVFgTfW77VUr_ypkDxyDH_RPzBrVdo_YE0qkYSya__IIbhY0DSMPvlUjSTV-kYu7SStE22TQLkeue0ZRUjWzmT4rR-r3D0U4lTjOVAzIFAv3-IYmZE--6zJXZNYk_E2f5-YhN0H2_1bz58lj-DMJ4UNRQSIlEqnHPJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به استقلال خوزستان توسط خدابنده‌لو در دقیقۀ ۶
⚽️
پرسپولیس ۱ - ۰ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/457052" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457051">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4f517fbb.mp4?token=vNP1RAZX1x0lNd-6HcYKJXSauRXaJ0K_kJg7twTDDS2pR17rMwYDbLRdz1rYmfKxsiGRhZ2n5WiLc1a2dtkoxQ7HDwicAikkSk3cMjb3cKGP69JKvXOe7cMBDgoA259oACYog0EV2d3LM-3TGoaoaPNYzuLWHX1rXw_uCqohMdLz6_ebyyNPlNdHJ13RqKiBVTQS5FQw_qVyghHbVUVORSI4TjJcSdTdKt6vvj3jX8KXlzD3yVFgyzBHXsLjceW4QkGJRCA-qbtAPAjj9-a3ys0xA0f2LY6Cg91Kq5XXLvHsOY2UlBxIjO7kMOpTUMl9ia90EiwKcKcLyU5iUjop2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4f517fbb.mp4?token=vNP1RAZX1x0lNd-6HcYKJXSauRXaJ0K_kJg7twTDDS2pR17rMwYDbLRdz1rYmfKxsiGRhZ2n5WiLc1a2dtkoxQ7HDwicAikkSk3cMjb3cKGP69JKvXOe7cMBDgoA259oACYog0EV2d3LM-3TGoaoaPNYzuLWHX1rXw_uCqohMdLz6_ebyyNPlNdHJ13RqKiBVTQS5FQw_qVyghHbVUVORSI4TjJcSdTdKt6vvj3jX8KXlzD3yVFgyzBHXsLjceW4QkGJRCA-qbtAPAjj9-a3ys0xA0f2LY6Cg91Kq5XXLvHsOY2UlBxIjO7kMOpTUMl9ia90EiwKcKcLyU5iUjop2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: سند آیین‌نامهٔ ساماندهی خودرو در دولت چهاردهم تصویب شد  @Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/457051" target="_blank">📅 19:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457049">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ebe804d25.mp4?token=tmAUme6FpFETl5ZeJr3wopMT8CV_aH0-DwWubounSfYYXb4zgW5bMKI7cxpng02wKD1RqGqZjO6tnhvTvNSOL5Mz6UX8Dp6aAHYD3tMIBMKDl5FErqtGUr7heKf1m-6Y818uStNIkja5hx_xFSqUBrLjBWjNu9in5T1AeRpEnjli6t722JyRr2duEp1Ib5YBLtDhkOy0nvl8v_HB5zwLVu6bEKGhOhnTAbjzTS-jc-HQZc1juKC6D8IMhHN_uzU3iqZv3sYYjb3zKkpxCaY-OFN6gXraR4Cg0z2fSOL_4W5UfkiOMCCGx8Dj-cr_m1HmQMXxGpmI-HidpoH47ZcDHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ebe804d25.mp4?token=tmAUme6FpFETl5ZeJr3wopMT8CV_aH0-DwWubounSfYYXb4zgW5bMKI7cxpng02wKD1RqGqZjO6tnhvTvNSOL5Mz6UX8Dp6aAHYD3tMIBMKDl5FErqtGUr7heKf1m-6Y818uStNIkja5hx_xFSqUBrLjBWjNu9in5T1AeRpEnjli6t722JyRr2duEp1Ib5YBLtDhkOy0nvl8v_HB5zwLVu6bEKGhOhnTAbjzTS-jc-HQZc1juKC6D8IMhHN_uzU3iqZv3sYYjb3zKkpxCaY-OFN6gXraR4Cg0z2fSOL_4W5UfkiOMCCGx8Dj-cr_m1HmQMXxGpmI-HidpoH47ZcDHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به استقلال خوزستان توسط خدابنده‌لو در دقیقۀ ۶
⚽️
پرسپولیس ۱ - ۰ استقلال خوزستان
@Farsna</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/457049" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457042">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrrFouGc0tTRgGGqKSXD-4GdALtrjS9xLE1NHCk9sPCP5XM2essUdGUgpI-22rb-lQIx2IFZx_dxOz_TiyZ6KRcMetTp68LZX_9DZGl0rnLGnuZYWMOQDQDZ6pIbrn3mLP581yPGycqXOELsPyyvA6TdmRnwfDcI3isC63-TKYe9e0Crv_bzQsqR4gfBX9pvw6uALrWo8BQU4oK60z6ISWQkZrsXuvYnKC7k4MLJeGLeTpzRC9M0Qq4-QpfHbC_QTZ6YIGFJQ67dOPiM-FL2AC8-WYOT-OrFz9R30DOpM8tRSuHo6E3FtY35jQdD4C7Z2FDISVefC6kOhoNQeHzjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geX15_yNpVgt7TfY0BeJxg5-bLB3ckeIsFdCd7QtVTRZjA9D7ktLF6ZDi_zfekO-Gd65l9kF_XYo7TUbZOWFLkoAJdfIJs9cGzMYPeS_9ihlODt-C278f7sWpmJQI7fZLmxvkQJBpDN0um6AG_Fegeh84Iob3SNNXCoF-RgUP-TEhGkZg5oSSnM4SWwzFdnZFsjAaXG4I--5PZhlKCLVS29q85NwjqG_XSPSuS4gbKuF4cdamDvAJByOBqsSHwnfqZSRRXCzvfSkGCWNMUn-1LfYAsac3nEpYVUOTcIwlFMd6hbwaAWAshFM8z-iosxr0lF3JJWllTu1YeZ6ISseQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1zasdxm7JEKUAIGdwEnMvu7cFYsD6OS5gviDjQgGWVzpBw416JVm7XO8qSsghYkg0f7RkZfaGl30xxc7krRUnM1u-5bAjCxgsNHKNJkzptXvp8SAE5ZtZM3nktaz-LZF2cHm-esxj1Xn7PiCHh9fLyVG1xeRazWdAbZu-qWdCeN1i-Mq7VcpOhTPMDBTMYB1GxNGRgZfqLgy-Okud34Dm77g3nkXuj94aTyvF3fSFBXfi0pIgN9uGeIkVyE8VfMGM3qq_hnbb_UJLm3uu0thIWgOeb0HxAc05Y2jgZ2EXCZOOlzUyZhG3BgQiLmgFVyYEbVWvGwOHtSNQLidwZ9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVnugvAfH_B2fi_3nyxI0CjJ423uiOUaLGEdG8_gJHQYXLl9G34voxvMtIc7dekRSEtrmmO675RnBH8QV-NnpmwXjgTGmx-s_RCsvnuc5SDZcLAXXD65c-bhwUxdJTwIN9E0MLYiVrM0szrDBif8-pIMh5XpS2MvZ7EEaE4XuRZaDHZUUpfKAmtZvkk9qHCdFpKqrru7dq2R3B1A1GAbJvaRbzFp0dnhcSQcui_2bw5Yb9SKqzjqCE9qaCuR-HnCddR3l7SIXrWhfHiY-bRBN6a6W9q7nXwmqD91rh-m1jLBzkMCvQIU0Qk98VC3k6tvWfhXiTp-zOd1jhGUpXIp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfFEAQIeiEeAC1x4HYDxn8kS2JREbq26tQwjlnGMDETBI6E-AMXivLGp5ugUFhUdffet0sRMAHaOysu-rQmTnNDtEtEdhMJw8hT302Ws5D3J3CPqC0vwL3ZodaiEjFNAJ-bKon_wn6n_aryyjWFDhzwavbv3PHGKeurf4tZ_aaWH4XeJ11AmRqQGhLjkPtRXrmFTsXCX4C0Ea5Ts46MsMfu-qupbLHDgS380eeOk0sQn6iMcFx_6juXVSx56vl7YnwkzLcAJVzQZBZLHKncAFMhfUXI48sxJifRdJQ7XJS88xZRaSdiL4xsfqH-tzw06EXkvHOj8RNSwWQCR858zhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjVryOV9qqKbJ8bCqGkvy_jzKsKHr0jERvBZOq622yQSlfKvhpu7Yma60L0pbMYdGXBH0YHEbURxLXJJBMrss8PILl6WUKP20tZ3OjZsiu3NedTAe_3fuhoPOgddhHvSb-XEBdkDs-hLSLTEWL-1SvaBi-A5sCdjL-x6UHfSL-seC4SXLngS2BXv2edslhsYKQazDpGReVLQdJ3oG-pQEVF5FuQ10WkDXVDoK_c25nuEITebKdtXms8O0zbsxtu7uui39bYDmPxSo3jOwjfNmPMcoh71Ztkv2oJeFfZYQZiY_wBi57QCXH6txQwGYGGp2tfE41Oj54y98zgE3FPIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTm7lpmqfCBbtsU1eglrSvxOVHeeE0aJF-KANwSGwPpfbfeJ342DnvsK3_0_ocLXcinwcn8cS-HfUJdMXp_2Zj2Y4Ycb83pjLNl8OwLvxcHpiZZXwpXDk_HLly7X8WtTchxvujL3TolHDnD_hxRppG7uZpZaqbochA5EhcbPen6cGd0O4ZyAWG6ErfALKN7j64_TPqVCckg3fxjSxU_-xQ3nBmaezbnNt9QEAKoV198EOSp-fGoZaHGlfP7gr8imZP7H_qVhge381gNfHtSgLoANFK4K3q5agAhM223VeSouthq2-GjRoAmYGr7Xw2p9OF_FNFbo6I95iIzNjOLQ8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زنان امدادگر در میدان تمرین
🔹
۱۲۰ امدادگر زن از سراسر کشور در یک تمرین عملیاتی در فارسانِ چهارمحال‌وبختیاری، مهارت‌های خود را برای روزهای بحرانی محک زدند.
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/457042" target="_blank">📅 19:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457041">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d110f4cc.mp4?token=VxgmP784NrRMN66E6WI0K7sAZzOOYF1MqW7NPycHgR55Trj_wd7X2Z43rLr3NGsD8pn69p3zl2lEx59-EKpkZznHXl-Itoi3cPQqEXrnflCsoW5bW1_QMkGRuym-5t28TJXQ09wQnhTbhVY3HNE7elA9XKpwbOpTXuvze6v5OxRadv5EqDooTd9H34_qOk_dXNCEqUXpwRaW8mE2USUm6mX7HDTuuk6c0jQpe3r3xZjOogdEl0-PkDzxqrwmo10x9dZYsBIQ64Z680tI41pD5oeAEqIFu6tPuzOa8oynYXMMMbwijaJ01HotSzj9yYRFqauJ4V3DNLx-J28FeWa85A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d110f4cc.mp4?token=VxgmP784NrRMN66E6WI0K7sAZzOOYF1MqW7NPycHgR55Trj_wd7X2Z43rLr3NGsD8pn69p3zl2lEx59-EKpkZznHXl-Itoi3cPQqEXrnflCsoW5bW1_QMkGRuym-5t28TJXQ09wQnhTbhVY3HNE7elA9XKpwbOpTXuvze6v5OxRadv5EqDooTd9H34_qOk_dXNCEqUXpwRaW8mE2USUm6mX7HDTuuk6c0jQpe3r3xZjOogdEl0-PkDzxqrwmo10x9dZYsBIQ64Z680tI41pD5oeAEqIFu6tPuzOa8oynYXMMMbwijaJ01HotSzj9yYRFqauJ4V3DNLx-J28FeWa85A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: سند آیین‌نامهٔ ساماندهی خودرو در دولت چهاردهم تصویب شد
@Farsna</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/457041" target="_blank">📅 19:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457040">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
روایتی از ساعت اول جنگ رمضان
🔹
گفت‌وگو با یکی از همسایگان بیت رهبری و روایت او از ساعت‌های اولیه حمله آمریکا به تهران را در مستند «همسایۀ رهبر» ببینید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/457040" target="_blank">📅 19:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457039">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkBwM3loZzy7c_2JkK0XhZvHB6ZcLpplxi5fc0HjIeHjF9ccmVcAu7ZqtzrVng-ae1F5VyBtb5pnq1Nv_VXOo1Sl4ex-WV1wy2v0yY9zLrA6uFqpZFT6Bqa_QXz5GQ1IddZoVvvux0x6z9GM40c63XgpFay2BpWWrkBcrBZBoVKSEKgTQ_XfvpCoCvsRWXXvD5SGYP9bA2mzYbmOkbGE7T3-HBa8wgsyv6pWjjV2f0VJrbBqpUnZYqK9-6MexRKAbOxkEGcIldYmBa20IAp1bvyOHeqOWrAZUMcG4AAQUr1uXPd0hGcC04u2sKPNAdKVCC_OAW_8Gft9ECmHhe9qNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلمان طرح شهرک‌سازی رژیم اسرائیل در کرانه باختری را محکوم کرد
🔹
معاون سخنگوی وزارت خارجه آلمان: اجرای پروژهٔ E۱ عملاً کرانه باختری را به ۲ نیم تقسیم کرده و آن را از بیت‌المقدس شرقی جدا می‌کند و راه‌حل ۲ دولتی را غیرقابل اجرا می‌سازد.
🔹
آلمان هیچ تغییری در مرزهای ۱۹۶۷ را که مورد توافق طرف‌های درگیر نبوده باشد، به رسمیت نخواهد شناخت.
🔹
ما بار دیگر از اسرائیل می‌خواهیم که برنامه‌های شهرک‌سازی E۱ را متوقف کرده و ساخت شهرک‌ها در کرانه باختری را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/457039" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laEVYOLrenkOEvng5DDvkX0awgbR7vffNkSOUKpw3AKSc95kUdqGx9d2o5QKTbdF22ktRSlOXyadbJqMgIInfk2GjweKE2gWJ6WsQ_5GL84SHruu7XVlIxvKh1ovAFwcYvUfyA9BVfPIm48pcJj3QZ48oDYDDuP4IROMOv2uSjxDlCQbs0nmfMmwh9ZnyaUUIwovIeOSkbWqcbeltCiM3T-v_amOC5hktGM3pjK0AzAx-Xffi6ootIyRfgK6IznyGuLqJKKMR9cmHESN_BxdQ6tH3akfqQIq2Kz5NMs_PrvJmSPoAYjXDrOsuujPcRC-igbbyw0WjlPvY_EkH4koRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور نفتکش تحت تحریم آمریکا از محاصره
🔹
پایش‌های ماهواره‌ای نشان می‌دهد که نفتکش چینی «مایتی نویگیتور» حامل ال‌پی‌جی که تحت تحریم آمریکاست، از سنگاپور بازگشته و امروز از تنگه هرمز عبور کرده است.
🔹
ترامپ یک هفته پیش در تروث سوشال نوشت، همه می‌گویند محاصره ما دیوار آهنین است و ایران هیچ کاری از دستش برنمی‌آید؛ او روز گذشته هم گفت، تنگه هرمز باز است و محاصره به قوت خود باقی‌ست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/457038" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e41c1593.mp4?token=GiHc2LdHByc5WguKugocqFNez-wRRlTSRykfhl8URe60TpbSnJo-bC4_9Yrw2px2GbX2gp2oxVGmNSIHETxoPzUyQWfMjXhSJxPfqDDhVkakWMcGz_RmI53ZcapyadcrvjkdKq1W6JxtsSzi97qcUw4RUarFMS3qfde6SeW-zYGHESgDj3G5bnsG4SxxuwKiEVdA5zrDCSadTD6rr5nAXthf7RcwLt0JX-COlx7x38u089hPRmKTkRpDO-W1OC6Pwir0LDqfAH8h7ZdsQ6O3KH27bisbO9SBMlgrPNZormoWQvBFX8FujRXHfkv9DD2ta3UgAYd-qmI8_GFvPSGfEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e41c1593.mp4?token=GiHc2LdHByc5WguKugocqFNez-wRRlTSRykfhl8URe60TpbSnJo-bC4_9Yrw2px2GbX2gp2oxVGmNSIHETxoPzUyQWfMjXhSJxPfqDDhVkakWMcGz_RmI53ZcapyadcrvjkdKq1W6JxtsSzi97qcUw4RUarFMS3qfde6SeW-zYGHESgDj3G5bnsG4SxxuwKiEVdA5zrDCSadTD6rr5nAXthf7RcwLt0JX-COlx7x38u089hPRmKTkRpDO-W1OC6Pwir0LDqfAH8h7ZdsQ6O3KH27bisbO9SBMlgrPNZormoWQvBFX8FujRXHfkv9DD2ta3UgAYd-qmI8_GFvPSGfEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تودهنی رضا پهلوی به اینترنشنال و خودش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/457037" target="_blank">📅 19:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6x5tg4TGLNdgbOGketGenNlT6LA6r3nVkGKJ7NXqzFidi9QLicIFHsSmuMCEGK8xgDmQcietF36dLq3TZUZ8H7moOwbEG1ImoRcCfAFmQ2qGY2JPi8UTUcqry1f_-rx7CsBydXLMPImfQydUTsuQ9i4WWnBUHPHkTzSllihXBFR4eoExU4rIv-uRZGRK_5u4eUcqUV59HcjN6GXifOR7gvPufh4_v8IFuhMgagd4suL_0MaRLS5rjnlYuaGIA7PnK_QHyOwv2WSFWY3nJYlEUBJZ5dLLp9yonfVfkZ0rATfjQCX8MnCTspQ6oIVCsjwlGcTnIJY_HcIoLs1osNbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: هدف آمریکا چپاول کشورهای منطقه است
🔹
رئیس مجلس در دیدار با رئیس‌جمهور عراق: آمریکا به کشورهای خلیج فارس و منطقه نزدیک شده تا منابع آنها را چپاول و غارت کند.
🔹
ایران و عراق و ملت بزرگ آنها دریافته‌اند که بزرگترین مشکل و عامل اصلی تمامی اشکالات منطقه،…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/457036" target="_blank">📅 18:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457035">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDtCEK_06STlXFDyIj31mpCQShu2w4qkNHPCc_LUl0m7lyLuPKgSuNnH3CJkG4mZ56dRVsVBgX_We07AuUgaeT5t6D_oGEycVUtw-XcCVTafg2G7t_sdooOsHls--Fnwpwp5mD_tWwL05yHV6clEacpPO-62vcp0dGsLhgtNowJY2RZyL3texfveBaLztbZ4usV5v8gfTFFWOemd9gWTU1pacteOuEmlbAzK5EEDR6KgxxhfFKuOvknvpSXe-W7U_XhzWzQWHz2kTpZ-8M_maxV0cDAmE3hsgvS6ZU326eXwT8v7cqyDJElEVaqzYzn1qx7IkzIUUHedYjQJp4lO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قالیباف با رئیس‌جمهور عراق دیدار و گفت‌وگو کرد.  @Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/457035" target="_blank">📅 18:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyocFn8MQeCLgPx3NdL4zqst3ft-bbOQsdYySl60BkVdY3tf6UPpPaI2voDRx4dpC4lTO-befYFNEbWzyBwv8Vke1fsT6izAJZhM1X45pb-cyTYgd7qoCK9o9fu5tGgM5Nm6tYAEVY9P8qwPEpSqiY8-Qi8ZTKiYf976DDiNAKVq9wRPDWlleEnxaVdjg2iWHz6O7MCeNOaHQSD1mDNvlubMsKsstVGRS2-VXs0JGK7RHG5hd8IeFHMUE0oLgZ4HKC9vkq6I702ECajdZnoCRtfqxVIcJN_IAqIblyxZkxyAf4KChXaE5l736tWSWt77wLoY2OPYET0QH1Vj9gs1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصف دلار پتروشیمی‌ها باز نمی‌گردد
🔹
روند بازگشت ارز صادرکنندگان از سال ۱۳۹۷ تا ۱۴۰۵ نشان می‌دهد درصد بازگشت ارز به چرخه رسمی کشور در این سال‌ها از ۸۳ درصد به ۵۲ درصد کاهش پیدا کرده است.
🔹
دستیار ارزی رئیس بانک مرکزی می‌گوید که صادرکننده صادرات انجام داده و ارز برای خودش است و امکان دارد بخواهد با آن «در خارج کشور سرمایه‌گذاری کند یا در بازار آزاد بفروشد.»
🔹
اکثر ارز صادرات غیرنفتی مربوط به صادرات پتروشیمی و محصولات فلزی است که یارانه انرژی و خوراک ارزان از دولت دریافت کرده است.
🔹
میزان تخلف در بازگشت ارز صادرات غیرنفتی در سال گذشته ۲۰ میلیارد دلار بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/457034" target="_blank">📅 18:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457033">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G28Qn4ZAdUlGehAW2PRGXXVs8w46RwY3csok7KnSUt0vPkvKAGTPCiIs3oyJbhHiBeI6hB2F7X-KLhul1EHowM1tAHIG8pBqF55hNAUuNb9IyxwarjcBGi4ryqUcAKQTNz-VuG6dLx1HZAznochEGXaFPKMQh7LmT6A96vc_6OqpqeZZsV9vw3xkKKmKQZLJhZMm786bXccE1H1EHxo-mtpIjfSOGigxSbV9h5AUxr-MlADN2-Rom23oHAUFXVFMurmA6-8SjuAvY1ilZv01t43FaStt3j414pJ0hLwxnl3xVWCjrdQXoL5lGCbWfR3Z7Qlt2q4a0UWGuM0Md-yRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیمیل بخشی از کارهایش را به کلاود می‌سپارد
🔹
دیجیتال‌ترندز: کلاود با دریافت قابلیت جدیدی در اتصال به جیمیل، دیگر فقط دستیار شما برای خواندن و خلاصه‌کردن ایمیل‌ها نیست.
🔹
این هوش مصنوعی حالا می‌تواند بر اساس محتوای مکالمات، پاسخ مناسب تهیه کند و پس از تأیید کاربر، آن را از حساب جیمیل او ارسال کند.
🔹
کاربران می‌توانند از کلاود بخواهند صندوق ورودی را جست‌وجو کند، مکالمات طولانی را خلاصه کند، ایمیل‌های بی‌پاسخ را پیدا کند و اطلاعات موردنیاز را از چند پیام مختلف کنار هم قرار دهد.
🔹
قابلیت جدید نشان می‌دهد نقش دستیارهای هوش مصنوعی در حال تغییر است. کلاود دیگر صرفاً ابزاری برای پاسخ‌دادن به پرسش‌ها نیست و به سمت انجام مستقیم وظایف روزمره حرکت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/457033" target="_blank">📅 18:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457032">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/531e74ff2c.mp4?token=INGMXS7ZO_u1VooLT3UHO0pn15toQqp_sWJwA5FMtcVVSKQMoPZcbAcqhhGXFz4T-UQmiTxKXW-ffsW121n1mUcld7XcfSziurf6i8VTTl3n9k9pZcQqhkfvher5lGi3nw1SmVmXElLtelJx0bzuq1ITIEBmQ-EQ6F_VSxOse_Thb8oLWGidEl4tWGbr4h4PP-LExRgyUVK4hZyt0ol0MP5VjiVAufGyI9zRrtuZ7me2GQ7q2soIynwHCEBysG0IVh8RsvahqVkkS97sVkYJJSzKHMOrZ5pYiwz0nI0dApxnElfaPT_Fjo-PJS55J2Rz23GMa9393dxSerdFufBOgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/531e74ff2c.mp4?token=INGMXS7ZO_u1VooLT3UHO0pn15toQqp_sWJwA5FMtcVVSKQMoPZcbAcqhhGXFz4T-UQmiTxKXW-ffsW121n1mUcld7XcfSziurf6i8VTTl3n9k9pZcQqhkfvher5lGi3nw1SmVmXElLtelJx0bzuq1ITIEBmQ-EQ6F_VSxOse_Thb8oLWGidEl4tWGbr4h4PP-LExRgyUVK4hZyt0ol0MP5VjiVAufGyI9zRrtuZ7me2GQ7q2soIynwHCEBysG0IVh8RsvahqVkkS97sVkYJJSzKHMOrZ5pYiwz0nI0dApxnElfaPT_Fjo-PJS55J2Rz23GMa9393dxSerdFufBOgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرگ ۶ توریست در پی سقوط بالگرد در کنیا
🔸
آناتولی: درپی سقوط یک فروند بالگرد در شهرستان سامبورو، در فاصلهٔ حدود ۲۷۰ کیلومتری شمال نایروبی، ۶ گردشگر و یک خلبان جان باختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/457032" target="_blank">📅 18:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457031">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf0435e5e9.mp4?token=v4k8OvtMuzuEbzVWK2EBqVRH0G0dgli4_q_6HdXGU8v8MwooiCqHpjZooZkNOP3Fg3VNshGAhnPqzHvJDtxFtdt8hI833lPq-PsJrDlnTItkCkPmBkFtzEPS0zdlTM8WOTJtvDOIQrl7iWWprGJXprkN8pTqAUdB-YsSgaYLcvfEH6m5kOjvsqaI7ovfPJVJfguiOsOBlQV0kUOM2svHHqvAsJk8rWuHUaPyJXiyYOhjvsMVF0pLhzMgoAMnFnmJTBgj0l6huoYIAWvqJe9CR4xB0i7fUqfYYfFg42Y4Gt9nl4WDILjcmGcgbth7k2eb8djQNtxV40pS9qZrekuxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf0435e5e9.mp4?token=v4k8OvtMuzuEbzVWK2EBqVRH0G0dgli4_q_6HdXGU8v8MwooiCqHpjZooZkNOP3Fg3VNshGAhnPqzHvJDtxFtdt8hI833lPq-PsJrDlnTItkCkPmBkFtzEPS0zdlTM8WOTJtvDOIQrl7iWWprGJXprkN8pTqAUdB-YsSgaYLcvfEH6m5kOjvsqaI7ovfPJVJfguiOsOBlQV0kUOM2svHHqvAsJk8rWuHUaPyJXiyYOhjvsMVF0pLhzMgoAMnFnmJTBgj0l6huoYIAWvqJe9CR4xB0i7fUqfYYfFg42Y4Gt9nl4WDILjcmGcgbth7k2eb8djQNtxV40pS9qZrekuxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرکسی به شیوهٔ خودش برای رهبر شهید نذر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/457031" target="_blank">📅 18:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSjgZg5gnFgI78YzVEpp1XXbS-GH9SjFT05Ze6eIxCvHX9Z7LBL-3DBYq4Q9RS5OzpNX4sM-hLAB1LEQx95Jg-Wdkrcgj7vSET6P0n51mwb8ate4l0X-ehodP60oW-VYGFgfQDrBA1dx6kZQ_lTkgE4lHVJjYYv_4hK3a-hmxDgXlnNERsF3f1UQ7YyiAEwu85sv-5T6pSyts0Zt_skCCQ4cG4hbl9q20toLmlXN-YZhhpBQnYOQzJKuvmCRNJ4VoPjuqatYuUcGNDVrVb_a-6owcyASVfKiOYsjMbU8asGwv2Cd4SgMl9RPpeMyGI-OUdI-ROBvmowl4vAFYKghWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMaVmMT8YlKOHZtUAgdWYniapLuA7l6EYfNPqbUwy7Zfny43tcVOmuqBPZhMCrvaBNlLxVMC79uq0PXgwgsm0L_OX4RaKfyyjvBml0UeozHhOGw2uX-2AO2JuROtjsdj6zdy0eJs-uTnkNSQo4-SunmP8lGpKoHUk5UC4bEoZ-dUfazx6pevpNijY_wjex1r-mSjNoWg7_8mwzZGqXpbqq-2yWCOLMqld2TcFlXggPMHm_apc6O-Wx7zKUK4DX-6YVgkB9hTiMFn1J4YkLojhurZbl0cCQOYOvJFlmswoLiRu9xNH-FaFmDJCPT0t6VKNHVx1r6oO_3zi-77kWlGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLqKXhFXQlzqy_xLIlBOwY_ImwKzzHSdIg1i9I26oebKEic6Bf5DV3UsxnIMpA_zqhJD9gVM9w6NNJ-wzCSuKEkOjRP7sh1kH17TMvYigtGnw9uz9pY84ZyIyWMCB6Lvs-nr0ewC4kmN9osGxghSc1dVrs-K7iToqJaSoEP5mc-60dBJq1-veFUU00Eu0QwwZm6fYt12EbplgtzqWDH6ZrqN4NTH34JuFMQWEuEI06NzURr2iCUoZf4VnjNSE62vylKrXsYmsxi_1FXYf-7EKF0rEogPJJ7KNv_ASCCwLkZ9mVbmWj-UONBdQ3E_VwL--DLHCoJZh4RdR3tSPNsCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOlxdwXh_DZ3R8syjcBuSHJR6H0pCNbroI4K_zp-_mgoxpbVay3oEEcIgaXNw9qqi-7xUYBVeIu7XSKfxXw-Mv4TA1CYFna1TtK-c0uWQWAUeibweRROgBZgNUbP3B651cBJSx6F-ACGW5MNw7k6OCkH9VB2e93RTiOUr_xLSR-WPerhUWLkr6BSxqUcPi4KSg2DwwXiNgIeR8LvcivK9CcoJIx3SynfiXWOIYtkOXFydJvZoT-62bVnac5WGq4hCofk_s_5EeNZiDnaTx_2dY_SrzWaQGVkHhZTNppw0cxU6sy5WzhiSXNHJX_IkmqV1zNtbrn9vv3GUvLm__Xf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzlyIsAAfMs028wG5lLm6sH8JZ7xU1lhky8QtkZjGtbIVQo8o3vzKs2Vg_RxDp7_oK_HVjrA611Pui5q94k4aC8lizslnWzxvpuFl7nMC-p8rdMHipWD2thuard4vm0fjKaIx3AnyuAqdNmFukOmbWXdO5Y8InL9ju8cBgQlAaAI9LYl8aa_SFP8Sfg48oll-phZ692YaK9qn5IFhMMjMwV5C0FGZbxH_7QgP9za-82i3P22pVZ4rXSU2i77FwALx7MtyaKgAtX14V0Xa0wMkLbUGtA8NRIbW9FkSBXMKobsc9ZRlePT5mbfzBCjBdLilcin1BWrxsNUDyNFVmZVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/in7Au6_2NhQ32Kd8Hj1cqo4zXQYD2Fqt_PbcvxQrU_tgcit7UVe3aJkCC_qbBNbugzEZnHltjW2gFr7YkqeW9gtIW0DwaP20anyL-XR30ucnq1wPNTCo5Ry7JyE-kIS4cQgX3-fb5Oc1kkg0TbGqFn2AiFERcgOVRnG3STcxA7UO9TAr30LNCfJFlchcCosHHEbcNFIV1qKLqRs7527YVxFyjGj5aZlWV5WBTIq2c8FWC8pUl-ojKCtAFYzD6TcKiRu22kHSE8t2irg-qzLEdxOMWp8Z9fRD5-edHBSfobWqk4pZ0KaJJe7sBhhhBucoU5BXA_3Ejm_-dqTRYCyzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6g4lCvQpok4jcU8d2jFWBNwNfqRzHDzUsHwWTA3tyRR7DjdXxNyxq6_ZsoD847jEPD4Ra71z3DMf6kHSBAUyAMD8OlvZS2l_Z_E5uZHEthRbnjPN9YA1WhPHl0AK-8rmbYoBpU6StmqYubLI0j1hOXqOhzE5aNJs1rzIncpdhUGo1JIdw_fx6wEFOKbpb5Ng63ptGDHsC9xY8lfiXggSh02jL45A3bCYSN5hbzgbuoM2tar2lfh6gXeHLkYGViDOtlxrZGxUiw3pfxn_oa20J_VibnXdj-quZS13N5Qj1oJPtujEDEDdAQlX5lTGtLJjXZodNmwC9uONRAxSTEaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تقدیر از فعالان مراسم اربعین
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/457024" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc8a8e3503.mp4?token=X5sjlUKfQMc2fQ8GkVwCjAaBTWDX-RWQfsuNSLB7s12-rs1djfn4L1Qsh8FYVltZwTE1f5V8BlyFoskOQfHyuaycPZ5FjNrrXiDrhd15ZkgGIW_S8cYFukFc0pHEn33_RT1aO7nFdKw2dsn7w3ZA23wLcwr-70nUKPolvQUaLxt8DdGoocsmAqtHbysJ2HZgaYtCppjDoEqv5u68nmDZt7UNfHVLgTkxNJk5Q23LW-d0iIVisrZx1wclT6iyFz8Z1nSOSJ8SC0cVYoZDlPGdXHn8kfVqokN1mDLpSbIPD3eR7XQWj2XgPeWK0fwHMUSwCIRoO9gfiyA--3NpXATsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc8a8e3503.mp4?token=X5sjlUKfQMc2fQ8GkVwCjAaBTWDX-RWQfsuNSLB7s12-rs1djfn4L1Qsh8FYVltZwTE1f5V8BlyFoskOQfHyuaycPZ5FjNrrXiDrhd15ZkgGIW_S8cYFukFc0pHEn33_RT1aO7nFdKw2dsn7w3ZA23wLcwr-70nUKPolvQUaLxt8DdGoocsmAqtHbysJ2HZgaYtCppjDoEqv5u68nmDZt7UNfHVLgTkxNJk5Q23LW-d0iIVisrZx1wclT6iyFz8Z1nSOSJ8SC0cVYoZDlPGdXHn8kfVqokN1mDLpSbIPD3eR7XQWj2XgPeWK0fwHMUSwCIRoO9gfiyA--3NpXATsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک شادی گل با ۹ کارت قرمز!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/457023" target="_blank">📅 18:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L0aB7FqKOibeGU1WjIKaNUmJKu5tnAEPx_iDoliJ6j3crNXWQe5MXXQc-Ovn6k-d7vgyPJcvT1JKMPIoUkCVOW6UXHZfJRd1gbi_v4B8R1e5NvJ4MTilfw_FxeHMDWlrmx_2O3rd8QL3ybIYScrKUh9dY7BG8DNb9TOQMRp_h9y1zhR6q26f-iGWrNVQA8GVCQ0JKf4XR9vLxb0OeEzn9KV-qbYyr_L4wVZC2XEd_hie2X2AVSFTB6mYeN_rZeNDMT7n8OQYUp7RuMQZDfRrT8PLtBmvZ9S7r0bmOZB7oRuFKyVGNejGnyjC9tKt0yeNPtmUfazzE2jXAbjYLiyGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Una6Q-CKBzDgSWAp2nJWfZjjfzXMnUALhz7CfOJvlWZOAWy7GKVp6b5IpUakY7wocXry_b12oTzmmW-8zVVjJh_ik0U58qr6VIvQCaj8RtEf8f04hq528rnl1-IgO8hM6_T7k9AY4qJO0AeRPy-1Qt0JLJakfsvChjLu5WI4U4b1Lw5By2-ADgIH8dVyiu9LdT7dRse2QeGBS6LGqVOa49s-rwqqve_VFPEjW3tfEvuJtKTdzoADh6gS--9ky1HqOn54XSwQLIIe8CnAELlGao2XCO7-XB_g5T93aSJ9P-IJu7OSxGWbc1eYqd9OsKOGlzAYVYBSZ5X85vDdZPJj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PM4AND01LUNeDk_SMhDTj4A3rcskGzPsGy9o7nYF01gxlbUk7C29g66cu-XZvz14YZ7t4rIPoqj6Ou8RpLXXbDyTcQCoahhbteefqqgrrwV2npyWvnM6qn23Rf1Oc1_U9NDaaZcNHBzbXyB4eQWlC_RJ8vzKbvYpyjob1INWH0aUhkJZi9mB-HqevEZEGhzGqpKJyaFz-Qh__1eAdQN1YyIzpY7OVYQWESDbXD6MWuqBi3EvtHLabWYTQiQcbshKwXPAe8KsghXpnSwsq6E9Tgr3VPOiuvZ6_zAN2HWpnf09WlfsqF-OkMLBW5jnkqGR_y2LX6Ckn42--QwceDBLZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تداوم عملیات تخریب ساختمان‌های مسکونی در جنوب لبنان به دست صهیونیست‌ها
🔹
رسانه‌های لبنانی از وقوع انفجارها و عملیات تخریب منازل مردم در شهرک حولا و المنصوری به دست ارتش رژیم صهیونیستی خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/457019" target="_blank">📅 18:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1645b5f818.mp4?token=DTaDbk_Jy8gLw3ttTCIzXD7HKS4iVC9p8rsodTNNjYvos81MENX3Ighs3yFOC9TFRhvVLq9owao1dhy4bO7wOIqvsAsEJe8XJ_1aWIvEjcmsA5e5NQ45b7SrTPFlAE0TQKqeSeiOGZAnYmDV5zXiHlHf8ZePC_NzVCquIx9XIXN1ph5zRFVu_sZrLYFWUI-rO4dqGoYM0Pwlye_uy7fvbeQsgHbCMa3ixOk9OXiwPsy7J0Kz0mpwBQ0kPsZLkpAtPTQ-A0xbkJYRDndz0Irt5Eoimg_s4N4bAtEi2wvJzs1ccdUuPY4oeyHOTRjtxETClaC82m8bf9NVlj4HxISiJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1645b5f818.mp4?token=DTaDbk_Jy8gLw3ttTCIzXD7HKS4iVC9p8rsodTNNjYvos81MENX3Ighs3yFOC9TFRhvVLq9owao1dhy4bO7wOIqvsAsEJe8XJ_1aWIvEjcmsA5e5NQ45b7SrTPFlAE0TQKqeSeiOGZAnYmDV5zXiHlHf8ZePC_NzVCquIx9XIXN1ph5zRFVu_sZrLYFWUI-rO4dqGoYM0Pwlye_uy7fvbeQsgHbCMa3ixOk9OXiwPsy7J0Kz0mpwBQ0kPsZLkpAtPTQ-A0xbkJYRDndz0Irt5Eoimg_s4N4bAtEi2wvJzs1ccdUuPY4oeyHOTRjtxETClaC82m8bf9NVlj4HxISiJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه و اوکراین ۱۰۳ اسیر جنگی طرف مقابل را آزاد کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/457018" target="_blank">📅 17:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457017">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2694417128.mp4?token=q2CLH4gs1245DaC0C5h9j2XfH3UYtllU_5rQkRejBQSWFXBplRGueqws9EPNygJIs-8vB1rpaXPTNSBhJgC41Ys9oV0fUgqIsQpYvbAmtM8cdtRoAHmF0t6yc-I2x4V3_Sqt4Te_5p95NGP6mrvQLQQNTP7go0MURF0Qz3oFovbip58g4Ak9pqetK3DeKZ9Gx6_qex3j83f3jkvLro-vJb8WXBePB2Rq7df574XpCv3X4AHXGKTqhKlvwAr8SwrwWHSPkit2xfre-brY6LX4uBj5fDyzdFkmsB9A_5aqdCRZoiOIC1INpDoe35t78Yu_PkenSpgvGk3w55y2EgGUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2694417128.mp4?token=q2CLH4gs1245DaC0C5h9j2XfH3UYtllU_5rQkRejBQSWFXBplRGueqws9EPNygJIs-8vB1rpaXPTNSBhJgC41Ys9oV0fUgqIsQpYvbAmtM8cdtRoAHmF0t6yc-I2x4V3_Sqt4Te_5p95NGP6mrvQLQQNTP7go0MURF0Qz3oFovbip58g4Ak9pqetK3DeKZ9Gx6_qex3j83f3jkvLro-vJb8WXBePB2Rq7df574XpCv3X4AHXGKTqhKlvwAr8SwrwWHSPkit2xfre-brY6LX4uBj5fDyzdFkmsB9A_5aqdCRZoiOIC1INpDoe35t78Yu_PkenSpgvGk3w55y2EgGUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از صحن پیامبر اعظم(ص) تا مزار نورانی «آقای شهید ایران»
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/457017" target="_blank">📅 17:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457016">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEX5WU5f5eVEFWGskfspavIBzGu3GsYwCKypy4kfFW1FSooVtnrRKs9IVCt_SOnK2Ak_7u31N80C-2pyYoS_TFyUFINXStlGdaIFnTM9xi68JI74xWiZQldS8ISXI1mlPjc-B2-_Fk3F_UGhCghuIjYUpbDwnr__Tw8ln5U2dLxv8zYKmFHhtN1FNi7z1oxAx4i3NK4-Xh04m7up8TMD-uhSbfLwhzQM6sc1tZFWCbAVbKCX1eIAsCmJdRECXFQ54lj1veDJlzQ4MtlveNXwe9f89g3oTvv6AiLw80uIC15sGCEXKKthaHsNT-GWoz06NV_CT8DbOi58o23Q_X97Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقیب انتخاباتی نتانیاهو حرف‌های او را تکرار کرد
🔹
نفتالی بنت: حملات نیروهای نیابتی ایران باید به‌گونه‌ای تلقی شود که گویی مستقیماً از سوی ایران انجام شده‌اند.
🔹
اگر حزب‌الله به ما شلیک کند، ما به ایران حمله می‌کنیم و چنین حملاتی باید هزینه‌ای در داخل مرزهای ایران داشته باشد.
🔹
اسرائیل نباید تا زمان خلع سلاح حماس از غزه عقب‌نشینی کند و اجازه نخواهیم داد که قطر یا ترکیه نقشی در غزه پس از جنگ داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/457016" target="_blank">📅 17:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457015">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9775b0679.mp4?token=ogq4o-kI-p8CnChTDRRw5epD7yZo6j17EIR-J0Bn0SBLlfIVbqFEHOX9Apv3GGyeDo0AJAxVc_B9zcCKkU00HnE99Z0l-isfogkAcpGWgMFWC_UuS_mhvQ0rT3RB2n79cCRv4UdpjnegNWgkn2msfvBzxHKvxZ9FJa7RGn7MVDZWz1YOhsM0BnKHO9RbmJmzshpMyF0VKaTJQ8i4elaowXnu1nqc_u7Ej-K_av_rXRkFp9b1208zSzRi1Ox7V_ZmvdiMFmZCsXnagQV6v5yeHh6k5pYFIpoUi0VfJvM9lDwHj3dXsFd87cNduTVQn948DNHcXPqlwvdVUWnktCMJhV4956HQviV2sx0i43blss0N2WEiztEbMOv7WG-kmC9AI1fAfgl6hq5n6yBQgRRgSsBLTodAbdEM4lB4Hozy6oZjGz8uJhmeOpnD0cLxlkOZUHYUMksbDOmcmUNn4RMBV5saW2j6vjtMpwMQ0z_YF0G4M1f4D_U8PshEDbC75-jCTxQIcMhuf1s_68rX1cCLyF8yJOis5oFFWqmrOpGR1ruT3TvNT9--Ptwh1RrKabBoVMc9ciCk3afwYd2NQY9kxBFTpjZL7o0sy8u1zK8vVnmVBIWwilws6KN_jI_HXGUSsl5Ajh9NC4IZEmc0kXoNMUAsu3SVR-ZXfH0p_haFx_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9775b0679.mp4?token=ogq4o-kI-p8CnChTDRRw5epD7yZo6j17EIR-J0Bn0SBLlfIVbqFEHOX9Apv3GGyeDo0AJAxVc_B9zcCKkU00HnE99Z0l-isfogkAcpGWgMFWC_UuS_mhvQ0rT3RB2n79cCRv4UdpjnegNWgkn2msfvBzxHKvxZ9FJa7RGn7MVDZWz1YOhsM0BnKHO9RbmJmzshpMyF0VKaTJQ8i4elaowXnu1nqc_u7Ej-K_av_rXRkFp9b1208zSzRi1Ox7V_ZmvdiMFmZCsXnagQV6v5yeHh6k5pYFIpoUi0VfJvM9lDwHj3dXsFd87cNduTVQn948DNHcXPqlwvdVUWnktCMJhV4956HQviV2sx0i43blss0N2WEiztEbMOv7WG-kmC9AI1fAfgl6hq5n6yBQgRRgSsBLTodAbdEM4lB4Hozy6oZjGz8uJhmeOpnD0cLxlkOZUHYUMksbDOmcmUNn4RMBV5saW2j6vjtMpwMQ0z_YF0G4M1f4D_U8PshEDbC75-jCTxQIcMhuf1s_68rX1cCLyF8yJOis5oFFWqmrOpGR1ruT3TvNT9--Ptwh1RrKabBoVMc9ciCk3afwYd2NQY9kxBFTpjZL7o0sy8u1zK8vVnmVBIWwilws6KN_jI_HXGUSsl5Ajh9NC4IZEmc0kXoNMUAsu3SVR-ZXfH0p_haFx_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت انیمیشن لگویی از حملهٔ آمریکا به دادگستری لارستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/457015" target="_blank">📅 17:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHyiOo21elfP0OTWjj1d7CZGPBtVruo7e0bJlfryfZXIYIWUwzhpbTMyg164T04NbGBwgEdGAMUTlOMVcituehWZ01WrAiqb5e94cF3hyorp1ZKClmvaJAo-E-Stzc8ffhbceDLMY9IqeaM4I1mq-_6mNsExL4bSteF_UsHXeDvabq6LoF72Kgix6VspPDzMWtd33y9ZG90_P2L4tOvjeLk8WLEfny9tySYLZIixkw-leYrE0Z_WdSWg-YoMBAvdkqUKmJTBKeW-cu5C7pxWLS3ltEg-lMEi6tYjxSU3fIHAYqYnSmBm5u_F4OX-ceP4LfkiYsRkU0s0wcdjNfNHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: غاصبان فلسطین در سرزمین‌های اشغالی دچار «سرطان اجتماعی» شده‌اند
🔹
غاصبان فلسطین در سرزمین‌های اشغالی دچار «سرطان اجتماعی» شده‌اند؛ فروپاشی از درون، سرنوشت محتوم آنان است.
🔹
تروریست‌های وحشی و رهاشده در کرانه باختری نیز نمی‌توانند آرمان جهانی فلسطین را به حاشیه برانند. الحاق منتفی است و فروپاشی، قطعی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/457013" target="_blank">📅 17:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce2f0bcf33.mp4?token=E44by_9_m6hTsXdiNyTWYVZqxa12TdtjVKXB3w5Ssivtvo45Hndm50ZySpys9ZfB31uDPGhV1bnty_Fd-hTZ6UUp6IXfUIqyBsbenqGMCq9zoVXiYYS7dHfQJGtQurhGPl0Xhey2ApvZZbW2qOd0t1rEhaEsNcwPL2alxtoE5jeKct1-BbGyPUqz5seQ7X50UGRi03TMw4t4TQ80i2pFjwqImIgoOJGzQewptju3U9eh2OtpG5l8kFMck5Sdxk_T05cVlQHjlfHCH7EN2t0vwUOv9iQIQRCg2m86bgO6XqPhsOMit5Y3EUPJidJQ60BMHZ-p6Vt5VqWEzblwh19Ssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce2f0bcf33.mp4?token=E44by_9_m6hTsXdiNyTWYVZqxa12TdtjVKXB3w5Ssivtvo45Hndm50ZySpys9ZfB31uDPGhV1bnty_Fd-hTZ6UUp6IXfUIqyBsbenqGMCq9zoVXiYYS7dHfQJGtQurhGPl0Xhey2ApvZZbW2qOd0t1rEhaEsNcwPL2alxtoE5jeKct1-BbGyPUqz5seQ7X50UGRi03TMw4t4TQ80i2pFjwqImIgoOJGzQewptju3U9eh2OtpG5l8kFMck5Sdxk_T05cVlQHjlfHCH7EN2t0vwUOv9iQIQRCg2m86bgO6XqPhsOMit5Y3EUPJidJQ60BMHZ-p6Vt5VqWEzblwh19Ssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطر سرطان بیخ‌گوش چه کسانی است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/457012" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3L23sFa6lz7YrNQ6ApklnG-r8CGk8oXwJfnk0asrDJ-gkrsCwBI4BClseFJJbnO-Mq1t7MENy_cbLgutIZ1wB00jFjF8Ss6Z_YThVVD06asKxtYih4bvf6rq0eWLxCn-Yh-iwLzroGj2OFsD3siXUGsVlNo9ha69h8Eo328HDn1_LdSo857NjE36UZVt3lWRE1EurFbFYy7X1kK0UAkG13voJdIMtn9thpWD1wE4R4IxvfvbKi_jiCIj7a-3TQREigiTGMkJri2keVbE-6k4Ffvq1DRUDkcm1asP0MCouWIHiCij4AlcXNMQ9iC31A_Ui3vccjJKXGQc1v-3l8Rzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: مقاومت تنها راه پیروزی است و اگر آمادۀ جنگ نباشیم مذاکره هم ثمری نخواهد داشت
🔹
رئیس مجلس در دیدار با همتای عراقی: از دولت و ملت عراق برای تشییع میلیونی رهبر شهید انقلاب کمال قدردانی را دارم همچنین از میزبانی شایسته ملت و دولت عراق از زائران اربعین حسینی تشکر می‌کنم.
🔹
مقصر تمامی مسائل و بحران‌های منطقه آمریکای جنایتکار و دخالت های آنهاست. همچنین غده سرطانی اسرائیل که توسط انگلیس در منطقه ما نهاده شد این خسارت‌ها را به بار آورد.
🔹
ملت ایران با مقاومت و وفاداری، با نیروهای نظامی و درایت فرماندهی کل قوا هیمنۀ آمریکا را شکسته و آنها را پشیمان کردند تا جایی که امروز آمریکا که در استیصال به سر می برد، هم با خروج از جنگ دچار بی اعتباری می‌شود و هم با ادامۀ آن ده‌ها مشکل برای خود ایجاد می کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/457011" target="_blank">📅 17:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFmkYsOuRFMMflIkfn81dQuHkmUeEOz8J0iaTgHzNMHp6iZwynyrr8xagTzGAB2O7jRF5aKL6hI0-e3m6oPz7b2HxvwObFPbJYqw8syFvhJUKuAOWJHliu8kd5GHH_fA1h8nESEzyL4CZp-XwJUqZKXzqj0gjYy2PxOC6e2AcfKXjpv3MXCWI6Dx9-sfEweZA8urXKv4o8Kz_ML_5_h_gsv17vCFCmNI6hDg1osXSmaY1GP_hXWBQPUzkOwPxB8Rxf8oFIBw2aTUdn1pLLvm77DuuWjh9FMV8roBatKLHhK0xE1qE2JiJEQrkkaMaB6iJ_lriMQ-RhUtqe3suNiRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت صمت: محدودیت برق صنایع به یک روز کاهش یافت
🔹
معاون توسعۀ محیط کسب‌وکار وزارت صمت: با پیگیری‌های وزارتخانه، محدودیت برق در اکثر شهرک‌های صنعتی به حداکثر یک روز کاهش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/457010" target="_blank">📅 17:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITj_ifw8_K7XaUXP8xMcJEiUpssOxp6WjZRlCwfqorTJZibfKQZ9BFz-nQ5JtFWFcEe7u89m_pwNDKXfBFKDNC0IfSaw9ixxYU2KggFfyzVVuJeTc_FEOKhNsaN7Clx3IqJinLAudb65tqkE0oehkzyGbOibc8OXHTFwhhW9441NzpNrN9IVutK8av1FyUjRws9WprkobiXJTwqokkPVQxjO2YPpQb5Zn-4DKVNSzIGsOHmZoRU-zu6Lpx24_aUGBwc36jyfiRuXSWWcbTQZgp75Ueg1r5nSLEbCPXl5pjP8v1GptVP5pPEdZbSVU_vXqOeiHMGhkqu0mZHw7Y9cPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قالیباف با رئیس‌جمهور عراق دیدار و گفت‌وگو کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/457009" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffa382ff7.mp4?token=Lm0TpfxCkX_raFUNM6zvwqn_mDWtofMdqtZn9mt3EQwCBfgW9QqCwDFx5YAslHfKPLRIphTsIbDWp2j-KOwBPqHTA18W6279WAA1BeqFBrC9DUey084TGULClfmEL1wBjzOSmaMyL1fiMPRPJyfEnX1kJpY_u7GLBcfQLzllRRSDoKnqCLmLniOkz4mZWSvNLH1J9gkI6vslXh4YhRqXRVI254FfQvq4J6AmWdYyRbTpHG5nszhWcWtAmUiSTVjThjn58j5R8I2oKcsyPkX48GHWDaQkUfzp3y6wESkBpzfv-uL5cjsAMf1krYl4b-indFAEeLXxNNoLI8TxB1p8kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffa382ff7.mp4?token=Lm0TpfxCkX_raFUNM6zvwqn_mDWtofMdqtZn9mt3EQwCBfgW9QqCwDFx5YAslHfKPLRIphTsIbDWp2j-KOwBPqHTA18W6279WAA1BeqFBrC9DUey084TGULClfmEL1wBjzOSmaMyL1fiMPRPJyfEnX1kJpY_u7GLBcfQLzllRRSDoKnqCLmLniOkz4mZWSvNLH1J9gkI6vslXh4YhRqXRVI254FfQvq4J6AmWdYyRbTpHG5nszhWcWtAmUiSTVjThjn58j5R8I2oKcsyPkX48GHWDaQkUfzp3y6wESkBpzfv-uL5cjsAMf1krYl4b-indFAEeLXxNNoLI8TxB1p8kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح سقاب برای بنزین چه باگ‌هایی دارد؟  @Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/457008" target="_blank">📅 17:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46d12cc487.mp4?token=qGK_cKygWZzOgwFh-yowmUvaE14fGfii9MB0VrlKhoHcEs7CRXgu-5qnI-1tCAvAYPZFlwaQm8IWcJt8HnCEt29TGOdy4hDRrKaZVepOC6Nx9gvlX9F-214P_AdoR7V4rtlE2urkR9BmTh1b-rrYAElpW2RfXxV2hb0F5Mp26gcrvjBJ0jtAZli9_FzjJSKxI4BB4nSVnlQVT9OFhtEtwW5I9GE9h6qKg2dShek-ZIvMtgQNDROxMf89YW3XIaiDzsOxKDgX7uIqs09VlhDc0qn3cImCw-AbIt1bZ9IKLqkb2xZp45NytIFJD0k85ZZb82Kk6zcnQh4hotPpNoXqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46d12cc487.mp4?token=qGK_cKygWZzOgwFh-yowmUvaE14fGfii9MB0VrlKhoHcEs7CRXgu-5qnI-1tCAvAYPZFlwaQm8IWcJt8HnCEt29TGOdy4hDRrKaZVepOC6Nx9gvlX9F-214P_AdoR7V4rtlE2urkR9BmTh1b-rrYAElpW2RfXxV2hb0F5Mp26gcrvjBJ0jtAZli9_FzjJSKxI4BB4nSVnlQVT9OFhtEtwW5I9GE9h6qKg2dShek-ZIvMtgQNDROxMf89YW3XIaiDzsOxKDgX7uIqs09VlhDc0qn3cImCw-AbIt1bZ9IKLqkb2xZp45NytIFJD0k85ZZb82Kk6zcnQh4hotPpNoXqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنان «توانا» برای روزهای سخت آماده شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/457007" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQce106Q99fB25jZMaO6Ry-fWjiLAoHH7kHwpjqGreZoxyh0u5lnpg5Vhop4NCnGKEoHq63eg346PYOIVcwta8ZCfDuU32SlCqVxq4tqPwE1qv8biZmG6VijtFEf5ehX5F3YOey_Fdm2fnJojm2onrece6JveBh_kwfvhN9v7lWU-Csg_jEUNoYmaLKq63O4ROTPPYga8YmIk1JjRS9U3NC3pDOHe-9rZ-Lq5hWXe4bhM72uDVHdCw-XOJr-B2ohWjotpJ3C72T7VLhSLSiwZWH_OY5jSM4_TjDpVJkZLFwOw9xSnDEJ1Mk0nWwWgpN5j5wS5rH86lrqbEAcdTyMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشکیل کارگروه ویژۀ بنزین در مجلس
🔹
رئیس کمیسیون انرژی مجلس: کارگروه ویژۀ بنزین و سوخت زمستانی نیروگاه‌ها که از شنبۀ آینده آغاز به‌کار می‌کند، برای رفع ناترازی انرژی راهکار عقلایی با در نظر گرفتن منافع مردم اقدام خواهد کرد.
🔹
از هیئت‌رئیسۀ مجلس، دولت، سازمان بهینه‌سازی مصرف و شرکت پالایش و پخش در این کارگروه حضور خواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/457006" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7fbcfee5.mp4?token=qFU5oiqPG-LVUa8Z3DDS7tJ3AqUeTkpkfQSKY9BITQW5xNz1uV3ZMyNeD2piWWogWXqty0K1tKtgj4D1gLT9LNL5cz7U8xRTCHBF1JMctfIkoqkQd-Quzs2e0O1BrmWwdhlYQfQRADONoFvEUkIrxbNqv806Sxyr3WDfqlU6szWWuZLuIa2BZMJsgNbhSkgZrZ1ESYLwItvi0LfEbaZ7-T9goDXPYKGPScgflke3FRiZM8qGJ5v_1YHaq7gkmYFhyyNXusbr6J6C7rYZ1jSORVvTmqEZDy24pyHpoC0s_ZplcCisF1JYzAwtUdXRAwoiwbR35FLF0GfokMJJf08ukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7fbcfee5.mp4?token=qFU5oiqPG-LVUa8Z3DDS7tJ3AqUeTkpkfQSKY9BITQW5xNz1uV3ZMyNeD2piWWogWXqty0K1tKtgj4D1gLT9LNL5cz7U8xRTCHBF1JMctfIkoqkQd-Quzs2e0O1BrmWwdhlYQfQRADONoFvEUkIrxbNqv806Sxyr3WDfqlU6szWWuZLuIa2BZMJsgNbhSkgZrZ1ESYLwItvi0LfEbaZ7-T9goDXPYKGPScgflke3FRiZM8qGJ5v_1YHaq7gkmYFhyyNXusbr6J6C7rYZ1jSORVvTmqEZDy24pyHpoC0s_ZplcCisF1JYzAwtUdXRAwoiwbR35FLF0GfokMJJf08ukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزدان‌پناه، استاد دانشگاه: یکی از کارشناسان طرح سهمیهٔ بنزین می‌گفت اگر تا پایان مرداد این طرح تصویب نشود در پمپ بنزین‌ها خون‌ریزی می‌شود.
🔹
همچنین پارسال می‌گفتند که اگر برای برق فلان تصمیم را نگیریم مقدار خاموشی‌ها به‌طور فزاینده‌ای زیاد می‌شود؛ نه‌تنها…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/457005" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77e86f339a.mp4?token=Dtv68c7rzMyW8p3rqeZ6mO6-QSLccsOmveVvzxQcr9fT1yos6Cgx157wudjuSXqop94jkJyTtsAJavj1FRRB5mLyiQR6NoUSbOFMPjU9Xg72GQ9i63hnzjx7rwhspBwHJYck3cmUJ6AmyxRJburDgzXiEksng78sZlkaO7uUWNcqGjD9awfltTXDWkjYQ7VQ6b1hPdZ0ojLznxXje18ztHLGuCb8KEpVi_d0duUXbkqGdQofuoOdvaFgVgh5X7VAlV3o7QkzVs_M69mOiGjdzDDPjOqy5c6aYGQlnsCPHSx-Y-DP9a6rLGOt4HbQgXEqjONYJ7u8yQq6jNfOGjcQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77e86f339a.mp4?token=Dtv68c7rzMyW8p3rqeZ6mO6-QSLccsOmveVvzxQcr9fT1yos6Cgx157wudjuSXqop94jkJyTtsAJavj1FRRB5mLyiQR6NoUSbOFMPjU9Xg72GQ9i63hnzjx7rwhspBwHJYck3cmUJ6AmyxRJburDgzXiEksng78sZlkaO7uUWNcqGjD9awfltTXDWkjYQ7VQ6b1hPdZ0ojLznxXje18ztHLGuCb8KEpVi_d0duUXbkqGdQofuoOdvaFgVgh5X7VAlV3o7QkzVs_M69mOiGjdzDDPjOqy5c6aYGQlnsCPHSx-Y-DP9a6rLGOt4HbQgXEqjONYJ7u8yQq6jNfOGjcQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظفریان، معاون مرکز پژوهش‌ها: باید تبعات اجرای طرح سهمیهٔ بنزین پیش‌بینی شود.
🔹
حداقل کلیات این طرح مطرح شود تا با شوک‌های اجتماعی روبه‌رو نشویم. @Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/457004" target="_blank">📅 16:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b67b986b0.mp4?token=Wk8B7j622ppsyZNwTsfWZ1c6sYVUDIo197Vde3WC79WAcOoZwbFmG0nIOWgnXiaxqNsWFIXpbjTshXh1m9EGPvu3RxZjHFqukRMVBj-k54R6WJ2N_eUIONTNhpOtfDjU05ZWBWQmmvH8fCst_iU47xH8rNOcgXihihH-khqui7AcupNTBtElFBU-esEDLeDPy3AMV2M8cyTQ347VtJPGJiH2KX0xRohblSZPuQPhW-CMgYoZoeiS5hihOvUKcojzvCA0SEfzgWikp5vE1K9GXQ3ESR8sIOJ4OiWyHFd15VkpfSY3Fb_CzDUjmYti2V-CklMol56e5vwXbYIznx5Peg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b67b986b0.mp4?token=Wk8B7j622ppsyZNwTsfWZ1c6sYVUDIo197Vde3WC79WAcOoZwbFmG0nIOWgnXiaxqNsWFIXpbjTshXh1m9EGPvu3RxZjHFqukRMVBj-k54R6WJ2N_eUIONTNhpOtfDjU05ZWBWQmmvH8fCst_iU47xH8rNOcgXihihH-khqui7AcupNTBtElFBU-esEDLeDPy3AMV2M8cyTQ347VtJPGJiH2KX0xRohblSZPuQPhW-CMgYoZoeiS5hihOvUKcojzvCA0SEfzgWikp5vE1K9GXQ3ESR8sIOJ4OiWyHFd15VkpfSY3Fb_CzDUjmYti2V-CklMol56e5vwXbYIznx5Peg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظهوریان، نمایندهٔ مجلس: در طراحی سیاست‌ها باید جزئیات آن روشن شود تا زمینهٔ بروز خشونت جدید نشود.
🔹
باید مشخص شود که آیا توانمندی برای اجرای طرح سهمیهٔ بنزین وجود دارد؟! @Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/457003" target="_blank">📅 16:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457001">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ5ti7nq0ZO73IxPGlb1yOgWiXsdXj0BAhZl1ev6cz1SmKtoOm_yfkEZ91zDngYqppdeaq0NKJtjpdC9AV01bHtLP1cbf9u-NCzB77rO8VqtFuy484RwQ3N_WsEnmKMMlcMiT191d5jyRhbJKCyjXbzLZ0RNnTuVbwK_QL-e7GHxUMIe-yKwVCmZzvr7_CiDeDEBrV96FVVbUb5KFcS1RFR69JLvQ-t3qZFQ2O-UwwUBCzza1o1FWhRm8plzlbhQpRPxvMa0AyjP4zoDe8fmPfR_SI1GFOTUmVubF8eM98sHGQ7plpkrf9C3-7URw7jRjMoKU7GNfVGI_r6hG9RtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: ما به قدرتی رسیده‌ایم که معادلات را تعیین می‌کنیم و با کمک خداوند موفق به تحمیل ۳ معادله به دشمن سعودی شده‌ایم
🔹
معادلهٔ اول: محاصره؛ به این معنا که ما دشمن را در محاصره‌ای محکم قرار داده‌ایم که هیچ کشتی‌ای نمی‌تواند از آن عبور کند.
🔹
معادلهٔ دوم: هدف‌قراردادن هرگونه تجمع نیروهای سعودی، در هر مکانی که باشند.
🔹
معادلهٔ سوم: حفظ حاکمیت یمن و مقابله با هرگونه نفوذ دشمن.
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/457001" target="_blank">📅 16:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457000">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f8e3bd1a.mp4?token=OUJ4ARVUdUwdCC1JnOQzxK_IpS-odHWIAJYw5l9Bavjg15u_t6J2jYUAFcgaNF2fX4gqHhxUHJksHWBhnKEBB-EksCWBZTGMGJIcBaXAV-1TZAV3-y4sbtTG9mOz9bND6TaIazePljnO3R9b0veK0p2e5mYWSgLy17FQxPl3shpvGBGZjRDxnN7gxX15xo6mZhN9MzYiKZ-qwWLRD7uGqEGGBn_K5fV1gQb34NWMPiYnrDpZpIcX80Vr_gEDhDdN96Seu-JSbiw0r6XpoMHsId8jFjNFlBq1WaaTYgugltio0K_PXLv5wW2Gi_bhmKWM2xB2X4OH7X4okfwGEo3dZIUsO_r2yBrHpN-Xgn91wAKxLAmFJ6GV-nkcRr-pDDmJul8LZFThNyaEv9y5CFdB_gc-8NvtG4ygWypnYKAtBT08nz6Icig7dtg62M914nFRhbiaOSJGO3F-ImTDXTplMKIEDhCBdY3DplSC-AcqiBIZxdDqn42o0GCTuVVzCdIovs68Pvee999RM4oM4wGYn_gTvA1cYHwxmUVv7E1kE7TAhmzhj3EJ9eXlkCN65-cvX9KMBn3zVapKBEv_X-I5OqMY-O_r-k9uTtgtr5GPTRiqJ9pKwZdVmvHZPT3CuB-5vOITCKsbrYWZBSVvQyURpRN6KnZFldamaS2xHzJ6m08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f8e3bd1a.mp4?token=OUJ4ARVUdUwdCC1JnOQzxK_IpS-odHWIAJYw5l9Bavjg15u_t6J2jYUAFcgaNF2fX4gqHhxUHJksHWBhnKEBB-EksCWBZTGMGJIcBaXAV-1TZAV3-y4sbtTG9mOz9bND6TaIazePljnO3R9b0veK0p2e5mYWSgLy17FQxPl3shpvGBGZjRDxnN7gxX15xo6mZhN9MzYiKZ-qwWLRD7uGqEGGBn_K5fV1gQb34NWMPiYnrDpZpIcX80Vr_gEDhDdN96Seu-JSbiw0r6XpoMHsId8jFjNFlBq1WaaTYgugltio0K_PXLv5wW2Gi_bhmKWM2xB2X4OH7X4okfwGEo3dZIUsO_r2yBrHpN-Xgn91wAKxLAmFJ6GV-nkcRr-pDDmJul8LZFThNyaEv9y5CFdB_gc-8NvtG4ygWypnYKAtBT08nz6Icig7dtg62M914nFRhbiaOSJGO3F-ImTDXTplMKIEDhCBdY3DplSC-AcqiBIZxdDqn42o0GCTuVVzCdIovs68Pvee999RM4oM4wGYn_gTvA1cYHwxmUVv7E1kE7TAhmzhj3EJ9eXlkCN65-cvX9KMBn3zVapKBEv_X-I5OqMY-O_r-k9uTtgtr5GPTRiqJ9pKwZdVmvHZPT3CuB-5vOITCKsbrYWZBSVvQyURpRN6KnZFldamaS2xHzJ6m08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از دل‌باختگی عمیق و دیرینهٔ مردم افغانستان به امام شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/457000" target="_blank">📅 16:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456999">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc421912e.mp4?token=RFYVsRGFnJiw3KcunRn5QYrQChhG0TQ8KzI3ogrQaXW6avae1xd7B4tgo2VAJDVdfw8ofZ2kSZr7zBF8K3kpUMVCEQD-qSr_vZ4VnP_IxM7-xtVloCi-QRa5ulO66HelOooLW73PLNcauVPlTOeIWCYiTYdWK7p3oClBi1MiVQbrCpMyA1IqTfMpObK1I_rEcfd0hc1UM_PJ3hBzncawbIzHhnrKi8Kdq165IPhAZ_oGAt49alJip_lY4lCgqKMWSZAKbcWy4BmrMEph_UL6rJMCbwSZyTK0ZAs0L_ke1AtG5rsn1bNK87hurtLVRyconmWbTZJ4FJikG7CEO41nrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc421912e.mp4?token=RFYVsRGFnJiw3KcunRn5QYrQChhG0TQ8KzI3ogrQaXW6avae1xd7B4tgo2VAJDVdfw8ofZ2kSZr7zBF8K3kpUMVCEQD-qSr_vZ4VnP_IxM7-xtVloCi-QRa5ulO66HelOooLW73PLNcauVPlTOeIWCYiTYdWK7p3oClBi1MiVQbrCpMyA1IqTfMpObK1I_rEcfd0hc1UM_PJ3hBzncawbIzHhnrKi8Kdq165IPhAZ_oGAt49alJip_lY4lCgqKMWSZAKbcWy4BmrMEph_UL6rJMCbwSZyTK0ZAs0L_ke1AtG5rsn1bNK87hurtLVRyconmWbTZJ4FJikG7CEO41nrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظهوریان، نمایندهٔ مجلس: طرح آقای سقاب برای سال ۱۴۰۳ است و مختص ایشان نیست.
🔹
تنها تجربهٔ مشابه این طرح در ایران اتفاق افتاد که با شکست مواجه شد؛ این طرح در دنیا تجربهٔ موفقی نداشته است. @Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/456999" target="_blank">📅 15:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456998">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_EEE2j5eTXS4-JxN6-jl28PtzCfl8jNJReX21LGB4VIN8ZXwYi8G2azVrGLeeiIYUMRIOQN8OoxC7UJZF4L_pmJcr6T14r_-6TmO4P7CzPIvcDKR_6kNZT2lgWhvoOSmlZB2IQSUQVCh0s2_IXGE91NCDvwmVOPNaht5ssQOt6TDmTixcEczJkJq-ARuO_qMz0FIBGMae5d445BJtkri4IyfhtWAAc9_Vz_EjTPtWoTxjv0Ahj6FFynWDDY04JjiIVt7jZOYw66YL4dCdp-9qAlo3CyjRWwIFNQbBMSnU6XgnX8LvL4oCLpp-5yGG6wcX90jckQZzY1u1ny2_HrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصوبه ۴۷۳ چیست؟</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/456998" target="_blank">📅 15:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456997">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f8c2df6c.mp4?token=HrrywQPZSVXNKATM_-BpXXcJ9tKxobe9SY2_uzNrHL7p9lMq4EDuKz21Lumz5qd577Gv1fgmGMsGCpCYINH6m5jwgxpBlbMzWdievHhgyU59xi15zc3ZivlwzMM97v444zXcIUtnc3iMI3jq0ouanOf8Ve-rX9wSJ5iUn5FDg7JjjTzsu3TNBA2xWiSorgeS1VtMKv-xml8VtScZUOrxBft05uOhnCaWe92tPgAVglaqTNPUrLydv5vPeMdRTuwYDdeoyLr2fCXOGZ4MeEo2ANkXNaOSbcdmzwMMGBOHJZz8qUlhmRzuQz3TTQcwRNZFXArCZlQajzxPaxPtU13KCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f8c2df6c.mp4?token=HrrywQPZSVXNKATM_-BpXXcJ9tKxobe9SY2_uzNrHL7p9lMq4EDuKz21Lumz5qd577Gv1fgmGMsGCpCYINH6m5jwgxpBlbMzWdievHhgyU59xi15zc3ZivlwzMM97v444zXcIUtnc3iMI3jq0ouanOf8Ve-rX9wSJ5iUn5FDg7JjjTzsu3TNBA2xWiSorgeS1VtMKv-xml8VtScZUOrxBft05uOhnCaWe92tPgAVglaqTNPUrLydv5vPeMdRTuwYDdeoyLr2fCXOGZ4MeEo2ANkXNaOSbcdmzwMMGBOHJZz8qUlhmRzuQz3TTQcwRNZFXArCZlQajzxPaxPtU13KCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظفریان، معاون مرکز پژوهش‌ها: ادعای کسری روزانه ۱۵ تا ۲۰ میلیون لیتر بنزین غلط است.
🔹
با افزایش تولید بنزین از ابتدای سال تقریبا در مرداد ۲ تا ۳ میلیون لیتر در روز کسری داشته‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/456997" target="_blank">📅 15:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456996">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">واژگونی و آتش‌سوزی نیسان در شهرری ۲ قربانی گرفت
🔹
سخنگوی آتش‌نشانی تهران: پیش‌از ظهر امروز واژگونی آتش‌سوزی یک وانت نیسان در بزرگراه آوینی در ورودی شهرری، ۲ سرنشین خودرو در داخل کابین گرفتار شده بودند که نیروهای آتش‌نشانی همزمان با خاموش‌کردن آتش، عملیات نجات افراد محبوس را انجام دادند و آن‌ها را از خودرو خارج کردند.
🔹
پس‌از خارج‌کردن سرنشینان و تحویل آن‌ها به اورژانس، مشخص شد هر ۲ سرنشین که جوان هم بودند، به‌علت شدت سوختگی‌های وارده جان خود را از دست داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/456996" target="_blank">📅 15:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp5fE85PFHuzap9N1gNYqDI-7iNtgZEjsO8wjboWU0kFtuVtL0Ghabm0oeP7tpaT-rctxXV6L9hitYGypB_3TD1vaQ2ncVhAgsvhRps0QE0cVkUT2AMVOfEJyETySLbfpXhUr2svze3jojetKc0Vd-qlO-v_i8JnZ4WCGppO6VCf5rdn7z7wa0topqC0FXHbWynXLHFguNiyhKMydGLlLDBRqn1cCmJhE6Ln7NJxKzH-FKeMo4beIW64u7BfGVDn9GE40rg636qCTFRKEQotKmt0m_B8K7ogmdPFqxb7hcnDlcPFVUQRG3zhbYkW0ZkBEHU2y7X2KqyWF9Hvs6EQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورشکستی یک پلتفرم فروش آنلاین طلا در نبود ناظر
🔹
پلیس فتا امروز اعلام کرد که یک پلتفرم فروش آنلاین طلا «به‌خاطر خالی‌فروشی ورشکست شد» و در حال حاضر با ۲۰۰ هزار کاربر فعالیت آن لغو شده است.
🔹
پیش از این کاربران فارس اعلام کرده بودند که
یک پلتفرم
خرید‌و‌فروش آنلاین طلا اجازۀ برداشت دارایی‌های آن‌ها را نمی‌دهد.
🔹
فعالیت پلتفرم‌های فروش آنلاین طلا بدون نهاد ناظر شروع شد اما در حال حاضر بانک مرکزی سامانه‌ای را برای نظارت پیش‌بینی کرده است. قرار است تمامی پلتفرم‌های فروش آنلاین طلا شهریور ماه به سامانۀ ناظر متصل شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/456994" target="_blank">📅 15:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456993">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb1f98eb1.mp4?token=hjWQ7ymlpT3uoFfLe8JX0pirLHi7whZtX6Zux0Jjj48cZsulkHcjFf-eWssAX8ZCWq4UXN52WDF3Lm4-RtVzxg4vFmLnc3TkjR7nUpmCnUbFfsG6_s0exsCJwPvhtk9qkzISWsTFZEY6z2HHXFWujkxOBofUkqCz-urDvb80yiWQoKuhkEwq5a_mDrIG3C3txgjqgGPtFRorrfv7NTWNe3-zGOBKopjkmBH6F49YwtUb-0kaWnCZ1RuKr8RGybNvpQdBc7HRBuqxFE5gPR_A6bby0rI4anVJSWULLGfGFZtPIQ-r4n8Iwf-FQnuOi9h0yFJ9YcglkZiwwas84ZUaUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb1f98eb1.mp4?token=hjWQ7ymlpT3uoFfLe8JX0pirLHi7whZtX6Zux0Jjj48cZsulkHcjFf-eWssAX8ZCWq4UXN52WDF3Lm4-RtVzxg4vFmLnc3TkjR7nUpmCnUbFfsG6_s0exsCJwPvhtk9qkzISWsTFZEY6z2HHXFWujkxOBofUkqCz-urDvb80yiWQoKuhkEwq5a_mDrIG3C3txgjqgGPtFRorrfv7NTWNe3-zGOBKopjkmBH6F49YwtUb-0kaWnCZ1RuKr8RGybNvpQdBc7HRBuqxFE5gPR_A6bby0rI4anVJSWULLGfGFZtPIQ-r4n8Iwf-FQnuOi9h0yFJ9YcglkZiwwas84ZUaUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
میزگرد زوایای پنهان طرح سقاب برای بنزین را هم‌اکنون در پخش زندۀ تلگرام و آپارات فارس ببینید.  @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/456993" target="_blank">📅 15:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456992">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90fc52bf2.mp4?token=vso4TIHOWh7sYIB5bbYcPH66ngwq8MmV6uAMCAKB1lX8UF2TDzSeiOMptMY8pxqLWQBYsjPNbr6EJ8z8ctOQuVNeZ1uhhjaGK4_9ZvwZAyat6DUoUDkmqf80bnECSzdCxOiNC3CKy-S8xOKT3rf6WQKKWFPY_hTGKAwtPgT0lihJLpeooteXY036ny9Hz5G1khwPsPntUOj2BOwBFCK7k6VKBiX9O5gE33rrpLfFk5J32eD9VHcSLNBNziHe9wNB7VH4KJ_3AnYu9BQ0GXWeVUrkFrzrWy0iID9O0Sve7YzS_Zm1ADCC1RzP3qUnamWYmDJvCK1wg7dd9in306SA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90fc52bf2.mp4?token=vso4TIHOWh7sYIB5bbYcPH66ngwq8MmV6uAMCAKB1lX8UF2TDzSeiOMptMY8pxqLWQBYsjPNbr6EJ8z8ctOQuVNeZ1uhhjaGK4_9ZvwZAyat6DUoUDkmqf80bnECSzdCxOiNC3CKy-S8xOKT3rf6WQKKWFPY_hTGKAwtPgT0lihJLpeooteXY036ny9Hz5G1khwPsPntUOj2BOwBFCK7k6VKBiX9O5gE33rrpLfFk5J32eD9VHcSLNBNziHe9wNB7VH4KJ_3AnYu9BQ0GXWeVUrkFrzrWy0iID9O0Sve7YzS_Zm1ADCC1RzP3qUnamWYmDJvCK1wg7dd9in306SA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حنایی که دیگر رنگی ندارد
🔹
بعد از اینکه ترامپ، عمان را برای کنترل تنگه هرمز، تهدید به بمباران کرد، تحلیلگران و رسانه‌های آمریکایی گفتند، ترامپ آن‌قدر بلوف می‌زند که حتی عمانی‌ها هم چندان آنها را جدی نمی‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/456992" target="_blank">📅 15:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456991">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6047ef9a60.mp4?token=r4dFR4KzTjsIusTMERZE3bATZTeGL-chXBGrVD44dgPsDagsKxQ0miNFcp0e48_vxFrW59ZTWul_OF29vNTyIOJyXknOHgYBtkJBpAZju5Xx6Wtrv9LaF0D_XJxnYRlRgllAhnWDvyZ1xDAhR2-f-8blB7ZeZ1Pcr_F3Vh7GdxWeyK_fibkJe_lG1KoipQ3NwaoROZ_vkotvGE6ppOHRhycV9VUIzYKwDvFUGCcxJKgH9QJMmddKh1k5dn95h9-WgMHQPnMHKFPABvx6VGm70SCaRuv2XRpHLGdyJ2j9IBHSCgqaaG8O_jHuoiz4HGwQ_j6sTUYBUWFW5rgOr5XgO3Xal-vg1ElsMlcIqz8NCvnqDF3IN5XSBthsAJ4kiMAVb5VNjUcXNE9PtAFFr9n2jMN8bJs38Jrc9k-ARCEYeWmotsNjBnnHMbp2U-qCGR3_TEjSo9Md8v1hBAgkqhEgZ9xbPb-2Zofgr7LxhuLsmIC0b2Dfgy6oVfa0phphZpMXG4QfgNahAgm3EX_6P5tVnZWL2a0xVB8EstK4B5vzeMt_W0T-MjYTuhR0n73-YW4pGxTsedzSaHcwB5lI8LuiuoxlFXczYpD422p6_9UcZUPGCsxbjwFbfgi2X_aR1ESsrud9oUlJmvQ9OOTdxZLfnGiaBmRRVwdE62f-bp1Oth4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6047ef9a60.mp4?token=r4dFR4KzTjsIusTMERZE3bATZTeGL-chXBGrVD44dgPsDagsKxQ0miNFcp0e48_vxFrW59ZTWul_OF29vNTyIOJyXknOHgYBtkJBpAZju5Xx6Wtrv9LaF0D_XJxnYRlRgllAhnWDvyZ1xDAhR2-f-8blB7ZeZ1Pcr_F3Vh7GdxWeyK_fibkJe_lG1KoipQ3NwaoROZ_vkotvGE6ppOHRhycV9VUIzYKwDvFUGCcxJKgH9QJMmddKh1k5dn95h9-WgMHQPnMHKFPABvx6VGm70SCaRuv2XRpHLGdyJ2j9IBHSCgqaaG8O_jHuoiz4HGwQ_j6sTUYBUWFW5rgOr5XgO3Xal-vg1ElsMlcIqz8NCvnqDF3IN5XSBthsAJ4kiMAVb5VNjUcXNE9PtAFFr9n2jMN8bJs38Jrc9k-ARCEYeWmotsNjBnnHMbp2U-qCGR3_TEjSo9Md8v1hBAgkqhEgZ9xbPb-2Zofgr7LxhuLsmIC0b2Dfgy6oVfa0phphZpMXG4QfgNahAgm3EX_6P5tVnZWL2a0xVB8EstK4B5vzeMt_W0T-MjYTuhR0n73-YW4pGxTsedzSaHcwB5lI8LuiuoxlFXczYpD422p6_9UcZUPGCsxbjwFbfgi2X_aR1ESsrud9oUlJmvQ9OOTdxZLfnGiaBmRRVwdE62f-bp1Oth4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پویش ایران همدل به نیابت از رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/456991" target="_blank">📅 14:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456990">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns0ngNzYkViUdIcpUvMbduBqcVCL77eLiqbXy6VpfMs-YERpUUwKvhUlkxH_DB3nsOkS4Jh19TB430kHZwf1ifWvr0ep3ahYRvoJhilkcYw-9LPLJH8Z3bYA8lsEnqtXWcqPvRSWQhMP6FGQHmEpawi1cQQzyfbFoKs4CzqIzBnTYYcQo_7bA7dmJaX0miODUwj9CpgjCj__Nz500U4iPHcWu402nVwlm_AIDM0w74veVTfYV_tUdIE4NdJLcm7RSp-I6m9GbRn7hlZjxTdz1mrqMU33Pk8CoSIx3b4geFeUpx-PKLWDt8J33knYGjTBUGm3UmiLEN8kkz2ZEwSJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قالیباف خطاب به حاج قاسم و ابومهدی: بدانید که تا به نتیجه رساندن آرمان‌های شما از پا نخواهیم نشست
🔹
من در این مکان خطاب به این دو شهید عرض می‌کنم: ابومهدی و قاسم عزیز! ببینید ثمرۀ مجاهدت و خون پربرکت‌تان را.
🔹
بدانید که ما و همۀ باورمندان به مکتب شما در…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/456990" target="_blank">📅 14:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456988">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8iEWWPMZbDKckPlf9tVHTFkL1M3CS1mQQeqaFDhXGjpciUaRdV6_11z_FybWLx4kLq8FRW5jTYjvYpQmZe3QwGJ-17oqxnwi8zSjpfDbbxIcBhD0PRIObTktlo3iX_grdNb2tblqT85R4qymG-y2jj1vijKkKzP-QOSOFfz6i7Ulxwn5a0hUL9IO10uo5rlLy8NeDAvIPA4X0ZXWxy0IjqOxRBVZMVpI2rhGj5-86PaDzK6auxSO0wKdtKpngmo2pmwtnKLZO-_kZIpdKOYYJeFaeKo3OofoKjZPXc5AIdZtlaOmIFtBpqqySb5iKmDU_e3izQ4yegqSRmeNqlxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPjKWIG8I0wD7sPdiHrGUs62DI4wjjy9LE9ONlxiyFyDkKqNcc3m1rTK-o8GFfzcZfHmEiGaxsamxEng6DstHIrwV_JNGyIuacAWL-p5bCPREEOPCTqmCfGafxKvcT4lTsVjWdA6EW4C4pJfH7DCLndUuVMuWrk9hAE04COYaAFCyluctIYX8LrfahGaGGDrqQf3JVFrjnMb9K-KINUA5zFLIrm4Qijbfter8os2zEprQO6qaFhQ7PpX9yvUcXQw-cUSOYeiZgkAc2_O4Qv9JM0bnuuVlr4qDyDU95CjnHYYjtNJsx_Mltl9OR9-4V53Qr2Dzzx5LQzEn0vpUIOp6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر جنگ ترامپ زیر آتش تمسخر کاربران ایکس
🔹
افشاگری درباره مشکلات تدارکاتی ناو لینکلن و ادعای آسیب یا انهدام یک پایگاه مهم پشتیبانی آمریکا در حملات ایران، موجی از انتقاد و تمسخر کاربران آمریکایی علیه پیت هگزث، وزیر جنگ آمریکا، به راه انداخته است.
🔹
برخی کاربران، با اشاره به ادعای وارد شدن خسارت به پایگاه‌های آمریکا در جریان حملات ایران، هگزث را به پنهان‌کاری، بی‌کفایتی و سوءمدیریت جنگ متهم کرده‌اند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/456988" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456987">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C16YMqX_Scq9lC_tSQGlaSTQoHCiYaq6sJrRKKmfuV5yQnQ_09yV9sTgVDgJkj7xgaPP0xC2c9p4DxT6IdmABqv_yPRNf6avyU8oCjsYhQA8HMGvUFLXT1SaVI3_Roau5fFB2tCQgGwdq1lJh7Zo4N1p-6OzhAg9cXVnAWnqZjbXM8aQsMhVuQvMPnWtcawbRYUgVQCUHCYPDSbQlT7Se0GWgG590oWx2WFPHxJ4yetMMUWen1xNZNdnlKqVmIbrA4Js4P-SXiTO3nhTK9uOQr9EU-SKGT9yu4XAlrNjyZsbMExYEHdm84W_rt9ry0lSEqePXcn565UdB4P-DafdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهرانی‌ها منتظر کاهش ۵ درجه‌ای دمای هوا باشند
🔹
هواشناسی تهران: با ورود سامانهٔ بارشی از عصر جمعه تا دوشنبهٔ هفتهٔ آینده و بارش‌های پراکنده در نیمهٔ شمالی استان، میانگین دمای هوا ۳ تا ۵ درجه‌ کاهش می‌یابد.
🔹
وزش باد شدید نیز در برخی ساعات از دیگر پیامدهای فعالیت این سامانه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/456987" target="_blank">📅 14:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456986">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1faa4002b.mp4?token=o7E2A6XY9GaiJ3DODva9CeEIl4xsESFUQqWwyNHyA64EyhLy18mqorYqq-IBZaaKsCte-cGrQmfddXkSNJFoQJpt8jVd9Z7n-3LFYfFrShkwrX0R30Iiq-XNOeXciUCe68A0Y1D-HWGSfyrRVoAaE_jNXj20TEQUwCk3SAsb8hBaT2KD3pRw0-gcKg1aC1RfdDpvZKC-UbLk8AoxpxXgdnP7PHDcGRRQHLWHf4mMzjdNA7P6goDU4C0J3M1XNu_74sUINMwHaducZHbadyFacgrU79v0Oy6HdUSvek7hhh498I3CoCAtdyU_2Rgq5pbiLbMr68ySsi78xtyt6no1eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1faa4002b.mp4?token=o7E2A6XY9GaiJ3DODva9CeEIl4xsESFUQqWwyNHyA64EyhLy18mqorYqq-IBZaaKsCte-cGrQmfddXkSNJFoQJpt8jVd9Z7n-3LFYfFrShkwrX0R30Iiq-XNOeXciUCe68A0Y1D-HWGSfyrRVoAaE_jNXj20TEQUwCk3SAsb8hBaT2KD3pRw0-gcKg1aC1RfdDpvZKC-UbLk8AoxpxXgdnP7PHDcGRRQHLWHf4mMzjdNA7P6goDU4C0J3M1XNu_74sUINMwHaducZHbadyFacgrU79v0Oy6HdUSvek7hhh498I3CoCAtdyU_2Rgq5pbiLbMr68ySsi78xtyt6no1eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرگزاری فرانسه: تعداد کشته‌های زلزلهٔ ۷.۷ ریشتری اندونزی به ۲۰ نفر افزایش یافته است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/456986" target="_blank">📅 14:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456985">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f286fec11c.mp4?token=po6JDMddRjLYyojh9EkZkdI2E89q9aLbnSzpp5xBNr1VH53twHDvxodto9NpssHawcl9dfIMIOpKegJA2gxZ-4dC2oc0-1tCWy6wrs0reo7a26xJVr9wSjhnIjfRgz9nN-EhhR8DmwmirxptKtx17EEbKnGSZh0M7RB7CROHYglyIVf6apmgMS6dZw_iHmHhsWoHivVfBVF4_avx2zrKmSMcNNbYgGwUBaBaLiSO-q-INJzkcr7nNB1jcZaUCcZPpzrd9hF2fGuHdCz2ZmZw-8sWMP0EexzV0mogR27jQae6zoSjvgBJDNOYGDZSuzD2KuRy5vXkfng5T6UTPyaZEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f286fec11c.mp4?token=po6JDMddRjLYyojh9EkZkdI2E89q9aLbnSzpp5xBNr1VH53twHDvxodto9NpssHawcl9dfIMIOpKegJA2gxZ-4dC2oc0-1tCWy6wrs0reo7a26xJVr9wSjhnIjfRgz9nN-EhhR8DmwmirxptKtx17EEbKnGSZh0M7RB7CROHYglyIVf6apmgMS6dZw_iHmHhsWoHivVfBVF4_avx2zrKmSMcNNbYgGwUBaBaLiSO-q-INJzkcr7nNB1jcZaUCcZPpzrd9hF2fGuHdCz2ZmZw-8sWMP0EexzV0mogR27jQae6zoSjvgBJDNOYGDZSuzD2KuRy5vXkfng5T6UTPyaZEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ معاون اول قوه‌قضائیه: تغییراتِ دستگاه قضا ادامه دارد
🔹
دادستان انتظامی قضات پس از بررسی گزینه‌های موجود ظرف همین هفته انتخاب می‌شود.
🔹
در دیوان‌عالی کشور نیز تغییراتی مدنظر است که پس از طی تشریفات قانونی اقدام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/456985" target="_blank">📅 14:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456984">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaFGVZTSEf83BqyqCLVXxJmnMqnOLKIjXHxgFAOz59uNrT4VlI6b6c4XyoosdAUyD5zgnsLsNmMt0Mxca5NzuoI2sTp8Y_hWCb-VZYj6_BXQaOvaDcgimRIsaPF6saeliALOMluDccMf1cFj6ds8Hwx-jmB1dmOI6tLOYK4LmmhAxvIPZnbkhAExobf-t9Ot2nNmfiVXn7-KdGHpStiCDjj1SfCXjpVPW7jhCt4Bt_lQD1mL3HQ7_c1zKEMYCsGQVZZciCPgDDSiY1fxDyKHgL16F30NKhobSVVzcCDobBt_wgWpa-uc21y-YofvxohMYoe3YLcdhuskJwkPwNpD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات فروش نفت به آسیا را کاهش داد
🔹
شرکت ملی نفت ابوظبی(ادنوک) درپی توقف تردد نفتکش‌ها در تنگهٔ هرمز، سهمیهٔ نفت صادراتی خود به مشتریان آسیایی از جمله چین، هند، ژاپن و کرهٔ جنوبی را برای ماه‌های آگوست و سپتامبر کاهش می‌دهد.
🔹
این کاهش بیش‌از روند معمول تابستانی اعلام شده و در شرایطی رخ می‌دهد که امارات به‌دلیل وابستگی به هرمز، با محدودیت جدی در صادرات نفت مواجه است.
🔹
براساس گزارش‌ها صادرات نفت امارات از حدود ۳.۵ تا ۴ میلیون بشکه در روز پیش‌از بحران، به‌حدود ۱.۵ میلیون بشکه کاهش یافته است.
🔹
حمله به چند نفتکش اماراتی و افزایش نگرانی مالکان کشتی‌ها نیز موجب شده ابوظبی سیاست صادراتی خود را بازنگری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/456984" target="_blank">📅 14:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456983">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NID0zgZQ_g8TVo4b5SMW8MNYA1Mky0KdAxk5RKpp35XAxAmcIFY_r780SYUkyvwmHpb95sxRoxJKYmbc7Pi1TlEaYyYgwFcJonC2ZbJGbJsQ3e9OIWyL-5pB-GgcaLGbAPPxiAEQU_pandvN1Gyn3ZaaaSJtIn3cGnz5M6PbS5FbQO4aAGtOXdZhmUTKfZa8WIQWlXGXHGzTjNvkq3WISE7Yh0QV2a1Z-Fx-8-PxqasA_Pnrflsm2FGH50JFpB_blZTmQJp5zNFwA1IDljtF9nSv5LZBvDKBelFUBI5FP3ajylMERdyNbzMKN0GR5GmfbcA1C49kfiNIoJVTUbEnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی بنزینی سقاب‌اصفهانی در توئیتر!
🔹
رئیس سازمان بهینه‌سازی در آستانهٔ تصمیم دولت دربارهٔ آیندهٔ بنزین، ۳ راهکار پیشنهادی را در شبکهٔ اجتماعی ایکس به نظرسنجی گذاشت.
🔹
این نظرسنجی پس‌از ۱۰ ساعت تنها حدود ۱۱ هزار مشارکت داشت که در مقایسه با جمعیت ایران…</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/456983" target="_blank">📅 14:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456981">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">استقلال شهرآورد را به نقش‌جهان می‌برد؟
🔹
گزارشگر دیدار سپاهان و تراکتور گفته دبیر سازمان لیگ در ورزشگاه نقش‌جهان حضور دارد و دیدار استقلال و پرسپولیس ۱۱ شهریور، به‌احتمال فراوان در ورزشگاه نقش‌جهان اصفهان برگزار خواهد شد.
🔹
در این بازی استقلال میزبان است که…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/456981" target="_blank">📅 13:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456980">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ecfa62c1.mp4?token=Wo-uoIcpnfVd-f6f8_GNaPWc5yl1R8uNtCdbVjyc4S3Kp-De7zvEmQSc7jAO0NSuhn1N0a-9CMjaDD7BN1NgvzqdO23YV3-udYKYVgaFyabb-gIAT5kWCWeTKr4Z7B5sjpy_Y14jUqnhf619vTjuqQwqxlD_4J_Eusvj0X2tvLGkEUJZt1SoMhaTclhuJ9tI9OMTh9TozyTCAEuqOD9Z6wYDRuGgLj7WpHJGvojgKk-Gb_SsaSNaIfMwjmQCOjOckRocu0YaxRCA9Ll2l3aCiXv_5Jt8NXdUJCWL6wgauyFzw7YtYrhbKEfPEACVD6IAUr-tVm0WVdL_CGcselI0jIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ecfa62c1.mp4?token=Wo-uoIcpnfVd-f6f8_GNaPWc5yl1R8uNtCdbVjyc4S3Kp-De7zvEmQSc7jAO0NSuhn1N0a-9CMjaDD7BN1NgvzqdO23YV3-udYKYVgaFyabb-gIAT5kWCWeTKr4Z7B5sjpy_Y14jUqnhf619vTjuqQwqxlD_4J_Eusvj0X2tvLGkEUJZt1SoMhaTclhuJ9tI9OMTh9TozyTCAEuqOD9Z6wYDRuGgLj7WpHJGvojgKk-Gb_SsaSNaIfMwjmQCOjOckRocu0YaxRCA9Ll2l3aCiXv_5Jt8NXdUJCWL6wgauyFzw7YtYrhbKEfPEACVD6IAUr-tVm0WVdL_CGcselI0jIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عامل حملهٔ تروریستی به دادگستری بهبهان که عضو منافقان بود دستگیر شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/456980" target="_blank">📅 13:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456979">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKNRBEf5AMKWpwaiM__J9T0ftHCnhajDidYGW84uBkSEZakN1al1y3TlSDnFQfXWm1wEpc2khpwRjiuZQ-egsXbz91lrZNaxBDq9limh-JulslbdUQJJf7PG5B5-1H35lhXABkhF5bLPX_7y7JSfvzYCJT-UP_Q2l-R3TAZFLDl8n7aGSqyEvmRLBX993supsz8LjpPI_-qw7sY2L7pZrmuKnS_rm9WY6EhkOGhdt7YYpZEyC-8_mRW0IroP8qkGbJytpoEJ25PB31Z3INXE7c9dur2PMC3Ibw1B8LO8d6CKD47S0VldXmyfvQ0BD5sTb187NwZUTIb7By9-5d1K6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌خبری از ۹ صیاد بندرلنگه‌ای پس از پنج روز
🔹
فرماندار بندرلنگه: ۹ صیاد بندرلنگه‌ای که پنج روز پیش با ۳ قایق جداگانه از اسکله بندرکنگ و اسکله گشه راهی دریا شده‌اند، تاکنون به خانه بازنگشته‌اند.
🔹
احتمال تمام شدن سوخت، نقص فنی شناور و یا گرفتار شدن در شرایط…</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/456979" target="_blank">📅 13:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456978">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Iox4nPuyE1PFLJtOPCVU1eNSceQOubHJbPnZ0dtIImlgtNt8K3s35cAwbtoU2zdnT6NOp34zqaW4se_v2Xyzn7Vaz9V-buYD5A8Y-HjNNmSsGe1AFFVTrWULQ05T5u65DMzMY9iFVMQ8cFc0pEtxjf8q-tlu3HNYx7CxJPi68uRXJQY_2W21rFKcb1jszoLPJDgl_1jlnqhkrJtVn9Hu4bY8Zp7KRChM9oBM78_AVpL_YbK2UI3e2xc6XoK1iUvixNDG8NJWVHCjVWwE1bjC9ZXpI0LPMXqoIgDwvHTxJTSsqXkFw4kn_UxTzu1ljA1w25Bln1bojh1LcaE89Ptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز
ترانزیت ریلی نفت عراق به ترکیه و افغانستان از کرمانشاه
🔹
ترانزیت ریلی محصولات نفتی عراق به مقصد ترکیه و افغانستان از طریق راه‌آهن کرمانشاه با نخستین محمولهٔ ۵۰ هزار تنی آغاز شد.
🔹
معاون امور اقتصادی استانداری کرمانشاه در مراسم آغاز این ترانزیت گفت کرمانشاه با داشتن ۶ مرز با عراق می‌تواند به حلقهٔ اتصال شرق و غرب در تجارت منطقه‌ای تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/456978" target="_blank">📅 13:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456977">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNj5ssiG0ZlekMFM2UFlwgkiBczQCXN3jT1SRnAnkWoQaNcM3oCfEvreJpTNougG7-2GnLk8An4pyXXyYc_RgpIcQc5dZhtArdnMhlTYfDCbwyF3oV-LZ6QTScLnLTRaqoQSwXNL0wmGkPO20EWyCkfU23tsCY3iIum_JQpzKei3Fb6p3VKBDvJjeWbFyIzgNQHCxlmcc4K4RxtU0rxxRXpPKXuxGt6fdlggi49ESrIe0bMsqIoE4KBaIyNxkE-8xZNWmenHKxOtJp5mKAQMQ8-Wht87KMl1uJzrXBqq8rmwGek0qCjbI9pT0B061hU6NNoCo47BjnJVjw-izg-RfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پیام تبریک مدیرعامل بانک رفاه کارگران به مناسبت فرا رسیدن سالروز تأسیس این بانک
🖋
دکتر اسماعیل للـه‌گانی، مدیر عامل بانک رفاه کارگران در پیامی فرارسیدن بیست و هفتم مرداد ماه سالروز تاسیس این بانک را تبریک گفت.
🔹
در بخشی از این پیام آمده است، شصت‌ و شش سال حضور مستمر در عرصه اقتصادی کشور، برای بانک رفاه کارگران صرفاً یک سابقه تاریخی نیست؛ بلکه حاصل بیش از شش دهه خدمت، تجربه، اعتمادسازی و تلاش برای ایفای مسئولیت در قبال جامعه کار و تولید و پاسخگویی به نیازهای واقعی اقتصاد کشور است.
🔹
در این پیام تصریح شده است، بانک رفاه کارگران در این مسیر، همواره تلاش کرده است متناسب با تحولات اقتصادی، فناوری و نیازهای مشتریان، از یک بانک صرفاً خدمت‌رسان به مجموعه‌ای توانمند، رقابت‌پذیر و اثرگذار در نظام بانکی کشور تبدیل شود. افزایش سرمایه و ارتقای توان مالی، توسعه زیرساخت‌های بانکداری الکترونیک و خدمات نوین، تقویت ظرفیت‌های فناوری، طراحی و به‌کارگیری ابزارهای نوین تأمین مالی و حرکت به سوی روش‌های کارآمدتر و غیرتورمی در تأمین مالی، بخشی از این مسیر رو به پیشرفت است.
🔹
در ادامه این پیام خاطرنشان شده است، در شصت‌وششمین سالگرد تأسیس بانک رفاه کارگران، ضمن گرامیداشت این مسیر پرافتخار، از اعتماد و همراهی صاحبان سهام و تمامی ذی‌نفعان و همچنین تلاش صادقانه مدیران و کارکنان بانک در سراسر کشور قدردانی می‌کنم و امیدوارم با اتکا به این سرمایه ارزشمند و با تداوم رویکرد تحول‌گرا و نوآورانه، شاهد نقش‌آفرینی هرچه مؤثرتر بانک رفاه کارگران در خدمت به مردم، کار و تولید و پیشرفت اقتصادی کشور باشیم.
#دکتر_اسماعیل_للـه‌گانی
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/456977" target="_blank">📅 13:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456976">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6kYcDejaPX5Itbs2XDMT9nGbeAxIHkrF2Cat0qb1UUFCLWujAMVl_XLI9zUPZIGiex-x-4UxiiU8RxiOOUSxgVqBFwENHscuahHVUd7VZCIlV_Tp5weYOoB1DIwfE7zi1OfmpE2zVN6l7xqYVCeXkOs33C8m-AOgxA9H0RdyK4JnDI7hoh-TVqx5Gn3h6ulymIlzMiufS-Kxn5sDvfCBYgiDqCnwEV10ERZjdf-B3AY1r-Od2GXZ4UdwJND1efsyhLUIfJ3AUak1ONJv7Ah8I_MQ8kKQf0Ma7k3_Yl9Zlmu-Shn7h-qlG-d-gzVt-c2bcdeIUKW4pZiZ8gEoP5Gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرصت همکاری با گروه فناوری غذایی شهدآوران
🚨
پذیرش شریک توسعه بازار و نمایندگی انحصاری در شهرستان‌های سراسر کشور
🍯
سبد متنوع محصولات غذایی
📍
فعالیت انحصاری در محدوده تعیین‌شده
🤝
حمایت و پشتیبانی شرکت
📈
فرصت توسعه بازار و درآمد
اگر در حوزه فروش، پخش یا توزیع فعال هستید، با ما همراه شوید.
📞
09398260904 | 09103470429
شهدآوران؛ طبیعت، سلامت، نوآوری</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/456976" target="_blank">📅 13:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456975">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/456975" target="_blank">📅 13:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456974">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4BuBv742qL8lNoLEXRee33jpEgk56-gy7CT1GgTl8vIq0Kc3UH-QMtJL6xREdUSzRtzrvDLmKivIxy4QLXEh9JFOJOrWQfh5qOl5CXPD24KhObrM0oDePduOZ7gTVoU7-zpw0IF2RaIo8TzTUnizfQ_AdFLKW5daykub9JrhSRI9v8wVDNIrcqlwdOisNXu8Qi7ho6xhtJvIrbtCNDAbSNK-X0FwLJs0MREL39ZRv1L4X3PbLJm1eYvv3154OGMC06yXAF1wss8yUCJ-PnBbbtHdmp6Ji5EP7OM-GeowmBhfYol3YCFo-SxNr7LrnxwjXtLGXguyuf7NF0po2-2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش سهمیهٔ بنزین کرمانی‌ها به ۱۶۰ لیتر
🔹
شرکت ملی پخش فرآورده‌های نفتی کرمان: سهمیهٔ بنزین کارت سوخت شخصی شهروندان استان از ابتدای شهریور به ۱۶۰ لیتر افزایش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/456974" target="_blank">📅 13:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456971">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm8sEFWz1PPdJroyfn1J5-MfoiCQyMTSWLwlP-MLvKgDKAxvFYQXZTTH5ijBPPGRxiFbHemb-kWOTti-70Qa8fwO5WmVLPdRyUrM-R0nX_rTfx9PhD11yduptobvMlGbBJnFlmHmr5wIPbMpj9oParHSC9qiHoUnFisWWjkhtJDkEisxuptlgZ6V5gK1Q2RqHqcqRJH5FnWjrv9jiomFbHx0QJVH5-sVFdlH2si64tqz5WCcBrXb9nMoXJaaeqi9ZHP1dQShaTgpF-hIz3wlxFC_l0gamRwCimRk9OmKo2a3p689xYRFlgMdKeHH2WgMySLvMfC9E2AlQzG0dW1b9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJiq1mi9gD01iQYHdzI9lPPJBKzAsN68wraSX39AGCr5sLi4lqsIGjv4dosPeR30JxioDR0mDaDzAs_aGlZLeOPcXDchm907n_Yy5ePINcc0-ki0qLmy5dtkbrxQ-_FSXTkCd2xqgibtAjzpplcsQAAWSObK1bH56XZ8YxFRA2qGD3bxM5euI-DPPFp-hP7lxlv1d87O73i64ZA_A-70knZrkTWDEVkBjYbuE8LKwQRURckZbK-mxywF6v-O7ZO0vZCUY7fdd2s5ISNH9AM1nG4N-fB1cm5AJqZFeKwupuOYw0JdO5ZbtDH6tB2JF0L4iixxuGqvQzI_IV4ewDjNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snNgWoHU7cj8fhUq8tvvrPTkWNg89HYuJmdFMuCEWOw6jjDQ8CE66nrou8eNBqMQdVmGTMlUoYr92uUfFkaa05CxZEEzHlRim_7NOh0GfiS0rublA02BgsxCoad7Bsn3fpuvG9Tr5h1-b0ueOw58fKtkkN55JZAmFQAtAy9XDVjLJ2acKEnAbaBTwZ-GT_3_htdZOM_SjhfzcVbjJeT3S_E5_We0xp5v401-P2JTOqZKJievw2mhscHmK9KXmZhfT765aGtBWceDa58o7wx6LZqC3URv1yR5oR6pqh91otsLbsmI3FzoMhfnNh-oxfT_0nszcQUyr9YtSkw-v1xU4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
استقبال رئیس‌مجلس نمایندگان عراق از قالیباف در مقر مجلس   @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/456971" target="_blank">📅 12:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456970">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TImsPh0jTRXxai0J7___tPBJEvZ5t0sOaFfECSjfSlujsIUXUOZGP_DqahGqvbYqVPnwymvYLKzKjOOKTRzpUBoBlzNTJZP8sHOnNRdgE-RLcc7GbkGEotjbbNs0Z7HZuKhzoshyzdfSKsBqJ7DfsR9d2fVlkmuSDmeBAfpnHMnsQAYW6zga1svIeHIDPQ4srrURv6aydURuzkU4_sqlebHsM0YWvD2SN8ryNydlsalQ30plWwNYVanui6LH7dY7l2w80cpwm76TQUlalakrZk3nH0Yg79JzsPAPCdukjkTz9nNeYDYHRmKhN8wIDEbztHoyIkP64DWQ9xFRYFnGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۵ هزار واحدی به ۵ میلیون و ۹۵۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/456970" target="_blank">📅 12:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456969">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2318efe0.mp4?token=fqhHRxxUzq6v62zlgIiL6kuXoRfFHkEw5mBqEH0OXc1gxsUZH7A9ri0OewHhyQxgTs84TRHM5q5eCMHbEEnlsdZ7tnr5Oo_EPH1rbrS-JmVQusAoblFA4EOHDDHJ4DzlgasPPRC-QDq7EczwmFdhHBy22GPbKev3kboPyKOI6NtvIN0yBh55y38hhQbpwpyL7g881zbC51zY2TBVAt12cvGK6Xn8-7sciOPpaSwXAsibRrvVduBaL0ekvQK8D7vOLJh-uxE1lJOvb-81ZSrRzBd8H1oGOMomhbRpG-L_r-g8ta4V7vi4VEtAalAT4MNOJEApzjMRF_DG_VAoI88ZWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2318efe0.mp4?token=fqhHRxxUzq6v62zlgIiL6kuXoRfFHkEw5mBqEH0OXc1gxsUZH7A9ri0OewHhyQxgTs84TRHM5q5eCMHbEEnlsdZ7tnr5Oo_EPH1rbrS-JmVQusAoblFA4EOHDDHJ4DzlgasPPRC-QDq7EczwmFdhHBy22GPbKev3kboPyKOI6NtvIN0yBh55y38hhQbpwpyL7g881zbC51zY2TBVAt12cvGK6Xn8-7sciOPpaSwXAsibRrvVduBaL0ekvQK8D7vOLJh-uxE1lJOvb-81ZSrRzBd8H1oGOMomhbRpG-L_r-g8ta4V7vi4VEtAalAT4MNOJEApzjMRF_DG_VAoI88ZWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌بابایی: به‌عنوان یک مسئول خجالت‌زدۀ بازنشستگان هستم
🔹
نایب‌رئیس مجلس: برخی مدیران با گران‌سازی به‌دنبال عقب‌نشینی ایران مقابل آمریکا هستند.
🔹
در شرایط کنونی باید تمام پروژه‌ها و منابع کشور را با اولویت تأمین معیشت مردم تنظیم کنیم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/456969" target="_blank">📅 12:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456968">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UINI2aMzZlUWvu4NIXqbx-6HBI0Z3L8hZw8GelLWf8H95P9SZRi-r6sJPKLbOc4bZ8RoDw0WlCNiaf7JkVBKJjpjDgZQ51OTqSNDhIka0NuSpb3XpRTjtVs2G_QHdC4II-54rITj4k31u6B4sUcIT5_XkMhii9YvbQh-nsplEtq6Tq6IRtSwZ67HifRN94pfSHPEYr6r6ksfUuYj4QKQjhfCC97_wFbrG9skdmMJpXyKwHuTyK8mfsOAa3ir2KcMSmjzZwNpjuEuPiXxIvrleEhKaunFLNeZhABN_EAAQqvsZPxjG_BQgbKyL_PH9O3Ho1pcyMViFTubcMQ2wvt9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
حملۀ دوباره جنگنده‌های اسرائیلی به فرودگاه نظامی ابوالظهور در سوریه
🔹
منابع عربی از حملۀ مجدد جنگنده‌های اسرائیلی به فرودگاه نظامی ابوالظهور در ۷۰ کیلومتری مرز سوریه در استان ادلب خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/456968" target="_blank">📅 12:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456967">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVn4wnPrzDknzh70N8_ZQpuFfl7GTdCUKUCccaWsgaJ7gBR6gf2sT-uiN7TQuw_NCNNxxC51F2XNPXdGKaPf_ppWu7PRje3JCvJAfybdTge_Cpv0L13gK56IcITuM9vF7WTxxg8L3CeImijDFQvrZ0isQeu4m-oTzonruN2f7XeZYNHRaTlsHqMqehVwGyvObs8TncMA-xcZkj-ICTd7pFUpImbIcFsshP1zbixuu0cM9f9G2RVQQOfMjEBQa8Iv-XEmpZog05EUOVo9VyynexKVgQT2O6RritJ9r7SURvES46N5o1korZJrDF84WRHEnTJPwTmZiZzeJFfxJC1Gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن بانک اهدافش علیه عربستان را گسترش می‌دهد
🔹
درحالی‌که یمن به اعمال محاصرهٔ دریایی بر کشتی‌رانی سعودی ادامه می‌دهد و در واکنش به تشدید تنش‌های نظامی، شریان نفت و بنادر را هدف قرار داده و تهدید کرده که رویارویی را به مراحل گسترده‌تری پیش خواهد برد، روزنامه «الأخبار» لبنان از منابع آگاه مطلع شد که نیروهای یمنی ده‌ها هدف حیاتی دیگر در جیزان و نجران را به بانک اهداف نظامی خود افزوده‌اند.
🔹
حملهٔ دیروز که به‌گفتهٔ یک منبع نظامی در صنعا با تعدادی پهپاد انجام شد و واکنشی به نقض حریم هوایی استان‌های صعده و حجه توسط عربستان بود، در چهارچوب سلسله‌عملیاتی صورت می‌گیرد که از ۲ هفته پیش آغاز شده و تأسیسات نفتی سعودی متعلق به شرکت «آرامکو» را از جیزان تا نجران هدف قرار داده است.
🔹
در همین راستا، منابع پیش‌بینی کردند که این عملیات در جنوب عربستان در دورهٔ پیش‌رو تشدید شود؛ امری که واکنشی به افزایش حملات توپخانه‌ای نیروهای سعودی به روستاهای مرزی در استان صعده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/456967" target="_blank">📅 12:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456966">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca9db56.mp4?token=Cb9f4SrBZ7bp-nPY_tFRud0eHOX3Y3xW2JZHq7fLqzNN7Afnt2rouqWNiPgV4J1d40TPar8ACg3r7HPcd44AWxpUhya2tjGtcs5TQ2RIGenI5NHNngoL5ckO8EbH0hDAv2QFvCnELrGCi8NAAkUIUUwUaUTvi-rrFTa-Xe8-r7dRCk1SygGdhcGUu3B66ahVPMmWGIZJtN4iKV6AOv4ZqTl1RFuHsijPMc3R7xEQ3tU8nmtwnKtkHzDeujJKwgVHtNrK828X8Szd2_3oEwpIePqXeHQFRP7DP5kRCSsSIrpL0yn2fv96EASRtRUkhsnzNLiYxFd1cIk332TAEEq4Dl2-dPmXyv3vVjctXbFuCC9ral_QIrpnF43AIhwxBgYNe23KIU619SCPaKBflLOaCiit6WyFBHQkErHHPdD8Pq3BDigqORaF73fYYZUjYONFY7AnO-7a3eqghYEtf2ljRVlwWwKmDOWdkTsbKAF_lRnhjh-A8o4acSb24plLO2_VfvrmCbL-sLzI0TvXdGGZ-wWZWjOlXSsUzSzk6xCY3jB_x72nt8J-4iDKLYQ6eJPPJAGPPTfrT-YG_kx7ibHjOFvUTStoROcWxsF2V02dDUZYdZzwpnaO7br4Told95M-EaW9VnM62ZDpr8BZP2BNBH-SKMVq2eL9ROJCW8zteuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca9db56.mp4?token=Cb9f4SrBZ7bp-nPY_tFRud0eHOX3Y3xW2JZHq7fLqzNN7Afnt2rouqWNiPgV4J1d40TPar8ACg3r7HPcd44AWxpUhya2tjGtcs5TQ2RIGenI5NHNngoL5ckO8EbH0hDAv2QFvCnELrGCi8NAAkUIUUwUaUTvi-rrFTa-Xe8-r7dRCk1SygGdhcGUu3B66ahVPMmWGIZJtN4iKV6AOv4ZqTl1RFuHsijPMc3R7xEQ3tU8nmtwnKtkHzDeujJKwgVHtNrK828X8Szd2_3oEwpIePqXeHQFRP7DP5kRCSsSIrpL0yn2fv96EASRtRUkhsnzNLiYxFd1cIk332TAEEq4Dl2-dPmXyv3vVjctXbFuCC9ral_QIrpnF43AIhwxBgYNe23KIU619SCPaKBflLOaCiit6WyFBHQkErHHPdD8Pq3BDigqORaF73fYYZUjYONFY7AnO-7a3eqghYEtf2ljRVlwWwKmDOWdkTsbKAF_lRnhjh-A8o4acSb24plLO2_VfvrmCbL-sLzI0TvXdGGZ-wWZWjOlXSsUzSzk6xCY3jB_x72nt8J-4iDKLYQ6eJPPJAGPPTfrT-YG_kx7ibHjOFvUTStoROcWxsF2V02dDUZYdZzwpnaO7br4Told95M-EaW9VnM62ZDpr8BZP2BNBH-SKMVq2eL9ROJCW8zteuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله مروی: مگر می‌توانیم از خون امام شهیدمان بگذریم و انتقام نگیریم؟!
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/456966" target="_blank">📅 12:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456965">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUWLhGBnlRHYRaXGxdpG4z2750UvE21zi21DJCQ1bALuXfPOQ6vJxYu25S7_rjbO08XCrCmqTGbKlvBhAVWNNw2smlLFCAWaToGT4PwDzklZ_hm14oGSDS2LaKrvkOuqw9WUWgMmoy85Ce7DX9hc0RVxg7X-4EISCpPLmtAj91CawxeX9oyDbG4PnnNGgD97H-b2-7GFONGXUg5SwMoQfrHkyXZxv1aa_n4G6twjII1a0YmfoOgarREjwHxRo7QdqN6vonVGsRPGsJbWdDKWmulzBVVUh0kRhjM8m5omgaucH3tJsPboeUTv5flrVKhxXW7rGUdZqw3WbbCjI72fhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار سرپرست وزارت دفاع با خانوادۀ شهدای جنگ رمضان
🔹
سردار ابن‌الرضا در آستانه روز صنعت دفاعی، با خانواده‌های شهیدان دکتر مظفری‌نیا، دکتر جبل‌عاملیان، دکتر کریمی راهجردی، دکتر ببری، محمدی و جعفری از شهدای وزارت دفاع در جنگ رمضان دیدار و گفت‌وگو کرد.
🔹
در این دیدار درجۀ سرلشکری شهید مظفری‌نیا و شهید جبل‌عاملیان و درجۀ سرتیپی شهید دکتر کریمی راهجردی که به تصویب فرمانده معظم کل قوا رسیده، به خانواده‌های این سه شهید اهدا شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/456965" target="_blank">📅 12:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456964">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=bxsW7PnVP0Hk7HDi7jGqEGPhzegl5Ba46kiOIOymxjTTm4IVJ8gTAHDifmUEvC1E5Ij3EekoorRnJEkQQQDV-6wAVVGJI5Fb914Gj45Vv8Hfgs4cuiyq2f_M1_cxV89FBbXkHCaZX5BWa5woT-WV9oLQBxsqBi0xZWeAtPl7l9htyAgQ4naVX7Wlis6laJ5uOAAKQojeyuxoTnG6aBLqY-KLYPY_6kN38jtrhQU5XmHAw4fcxYDBvZ0QxHrwgrJCSAsYSZtjxsgvQSW_gig4BFQ_RfSEPXG-gVGpHBFM-iSlg4K39rc9XQS311KYxZmqfccDN_J-w0gWZQnnYfswFiymEiA8YncFDZ-2Yfx_OynzNGta7OC-lFGlgTmFpqF5BKtrwbsBRGLhRoJCAKTzHXcYEA-pQPn3JLeXRPbwjjs-gVQLCUOS_4fRVUkhaLwWun2g8e9bG6Vpoz3YFtn91saSjjhg1eBDaa9eivUqnvvBun2yST9NKhx48gftDMQI09CfCigJ0qoszVlDiVvV0Uil1cU1NlLM04hbPWMS9o0x0DrzXfvp9foaw09aZ8RX44NkL7HyG7GWknsJcpJX9muQwWlFasaG9oOIelfwGOWbpK43kKoM2UVE14e-mDi9ifkJFS0UOWQqrBhpUHtoVQz_qj2KxSXgIAM4GQP-nLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=bxsW7PnVP0Hk7HDi7jGqEGPhzegl5Ba46kiOIOymxjTTm4IVJ8gTAHDifmUEvC1E5Ij3EekoorRnJEkQQQDV-6wAVVGJI5Fb914Gj45Vv8Hfgs4cuiyq2f_M1_cxV89FBbXkHCaZX5BWa5woT-WV9oLQBxsqBi0xZWeAtPl7l9htyAgQ4naVX7Wlis6laJ5uOAAKQojeyuxoTnG6aBLqY-KLYPY_6kN38jtrhQU5XmHAw4fcxYDBvZ0QxHrwgrJCSAsYSZtjxsgvQSW_gig4BFQ_RfSEPXG-gVGpHBFM-iSlg4K39rc9XQS311KYxZmqfccDN_J-w0gWZQnnYfswFiymEiA8YncFDZ-2Yfx_OynzNGta7OC-lFGlgTmFpqF5BKtrwbsBRGLhRoJCAKTzHXcYEA-pQPn3JLeXRPbwjjs-gVQLCUOS_4fRVUkhaLwWun2g8e9bG6Vpoz3YFtn91saSjjhg1eBDaa9eivUqnvvBun2yST9NKhx48gftDMQI09CfCigJ0qoszVlDiVvV0Uil1cU1NlLM04hbPWMS9o0x0DrzXfvp9foaw09aZ8RX44NkL7HyG7GWknsJcpJX9muQwWlFasaG9oOIelfwGOWbpK43kKoM2UVE14e-mDi9ifkJFS0UOWQqrBhpUHtoVQz_qj2KxSXgIAM4GQP-nLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسگاه پلیس ترکیه هدف پهپاد قرار گرفت
🔹
طبق گزارش رسانه‌های ترکیه‌ای یک ایستگاه پلیس در استان «ترابزون» که در ساحل دریای سیاه قرار دارد، هدف یک پهپاد قرار گرفت.
🔹
«ترکیه تودی» گزارش کرد که این حادثه دیشب در منطقهٔ آرسین رخ داده و تلفاتی نداشته است. فرماندار ترابزون هم پس‌از بازدید از محل حادثه گفت: «اطلاعات پس‌از تکمیل تحقیقات در مورد منشأ هواپیما ارائه خواهد شد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/456964" target="_blank">📅 12:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456963">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiljTbsKTV5U3hageZ0KHLlAZmaUZbmfNk20xhZXeyTiVdjv60IbGNTazVxr8f8o_pq56lrUVesNyI8YqArEV4m1oHHFhYqO77-AmqxcjhqVGGS18paojRn5-7JrkISZM2ItQTW8RLnG4TADGDceKo-WH2Y-n-CCxDA0MDoMt4PC1rf8J1CwKRMIhQi0P2Xh949CfjNGi_I7yrL3Ht3pcmUD2qt3PM09ObbEJUCSPW7vq03yGunXN1sewmMXl_pfnGvHd5H3fw1FiQLo_gzAJ3lVjW1TVR_zpZjaPuLiWFwu29Hvg2kpsREwHE1K6zj3kM_nkfDG7z0Cg12HPGKV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکسازی داده‌ها در دولت ترامپ؛ صدها پایگاه اطلاعاتی آمریکا ناپدید شد
🔹
دولت ترامپ در ۱۸ ماه گذشته دست‌کم ۲۸ مجموعه داده فدرال را به‌طور کامل حذف و ۳۳۸ مجموعه دیگر را تغییر داده است. این آمار بر اساس ردیاب جدید مؤسسه
DataIndex.us
به دست آمده که تغییرات داده‌های دولتی در بیش از ۶۰ نهاد فدرال را بررسی می‌کند.
🔹
بر اساس این گزارش، داده‌های حوزه سلامت بیشترین آسیب را دیده‌اند و حدود ۴۰ درصد از مجموعه‌های حذف یا تغییر‌یافته را تشکیل می‌دهند. بسیاری از این تغییرات پس از دستور اجرایی ترامپ درباره سیاست‌های مرتبط با جنسیت صورت گرفته و برخی نظرسنجی‌های مراکز کنترل و پیشگیری بیماری آمریکا، از جمله سامانه‌های مربوط به HIV، مرگ‌های خشونت‌آمیز و خشونت جنسی، دیگر اطلاعات مربوط به هویت جنسیتی افراد را جمع‌آوری نمی‌کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/456963" target="_blank">📅 11:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456962">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMIsDSrxwOWwclmuP-b-RF3f9HMBHPAjgYOXUhQxKMX_diwezhNSolXN-AYWttDXCn9qGKrkYoqwR9nbtY5I_SRqVWqY-YKLg0I_LbFhGZ_MulwbWHPX7f7gl4cMF72QviAqwWSuQ1iRbqMs4EJoUM621t17WhnxmfFBVnBg2j8dJQNGS0OSoBtDbg5FKzRDbT2u0FuV-I5RAkb-KnEVk5h3nNmazs37RCQ3knyAZS5wZdLcFZrd3N791tiDSvC2Tizk02tsJfj1kZE5Wxrxkw9Mo8dJa_mUq1eVP80Ik4UC0BcHf7yZWSfTEIsiimQ2g3WX3ItpI0XlO68Dv6JOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شفاف‌سازی ایرانسل در خصوص نحوه محاسبه مصرف بسته‌های اینترنت
ایرانسل در یک نشست خبری با انجام تست‌های عملی در حضور خبرنگاران، شایعه کسر چندبرابری حجم اینترنت بین‌الملل را تکذیب و نحوه محاسبه مصرف بر اساس تعرفه‌های مصوب رگولاتوری را تشریح و تأکید کرد که ضریب 2.7 مربوط به اعمال تخفیف برای ترافیک داخلی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/456962" target="_blank">📅 11:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آیین آغاز عملیات اجرایی ساختمان اتاق بازرگانی جلفا</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/456961" target="_blank">📅 11:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456960">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/456960" target="_blank">📅 11:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456959">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4iQ9httf_qkDKa64_RG5TEtkgjD5mlLTT3I2H1k1vrwT7EZtNkAvRhLz9yz1H8c7aakLbiN-cAw3t6vLABADHS2vLOGsi4Erryz-SVsRt0KBshgBiNPEDzo0wF5NP2msnks8npEmJFk9lE71zv9_uzPHf9ijrlj0pviHNTJAou951cTMlwuZ_w1vDZozQqUHqi6f62M8vetb0vzoI02M5qfFPM2PBNo1l2v-aJUuLKStExUNENVSfgQZ2H65X-xEfGTJok-mZOp0qLVF-Tr8xg4Ox7vortoCBg9UqMl0iaB0gnPY8HVll3CifbDOH_tNMb7GtvtpNcv2v58RQyPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق صنایع آب رفت
🔹
حداکثر تولید برق نیروگاه‌های صنایع تابستان امسال با افت ۳۳ درصدی، از ۴۴۶۸ مگاوات به ۳۰۵۲ مگاوات کاهش یافته است.
🔸
۱۴۱۶ مگاوات برق از دست‌رفته، ظرفیتی در مقیاس مصرف برق خانگی کلان‌شهری مانند تهران در اوج تابستان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/456959" target="_blank">📅 11:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIklSPvsnqlhF3XZSPUf2aY_btgF3iFX1i59Jm6-R0ZNFhhpMzV_QefeHvoKJkp4ZOxcDc6wgYFj3mNLbUzpRe2rXqxxDjeaCfXcEIF5BunpM5mA0V1V-9bUX6nBk2bjcQ86nTYjyJycNrQCOowPoxdBStoRuw1mCOIf4HiUu9ncUXmwE-KhwqCU3nuZS7Alc3lRsutlCCH_5xNX5iXMhg6Wf_0mbcIy-wCotBmtfolfEd0cog9UPruRkLjjhgjWtc4ouARCMgnk37Wa-ou0uvx1y-QJWq--3rXXx7elXTRKC9MQ8TM900fzvvamr1vaMkf5-9H0ptGsVVT4WpXtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4U81f6A0lWOvURx-psixl4ufNyEhSL8BQy9K44WzlZ6mNOjWMeVvNEuAYI7nG7TH6prPYjjySbnVHk9HiosAT4csEY6QY_OW4fd_Cpa4ONZKWCFwX1jznYe_esIn1riuwhr67DqcvJ9wzwN_P9BUmiing53PxnXqeZV_t3r6xBRdBgtpJoM_BKyCl73lNWdxQ06TzjUT75otdtesVYSFeOOHoFPRWVA71GkuMXWlgYSTBCBzwOku2qX6ZJ7z59w2xlrYfejxGFiIsjU0QBYfqvuFbQFWkQzkAmxytXlu0N-EYs-d-59tsFOU5KEGE9gdYLDMRM6fmy6TQqIlqjoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDNgxDXa8F8M1cTfRJVsuXFDhlbXO3f6ihncnFZ1CeRlV5wl2Z8HdDu41wbkcta_z4LVsEJsJR0JlDI58KMzL-v0ri6I8xuM0OUAEqfPn0opYEJF36ggE4sBY7_2BQPTHki28B_OS_axo2vQIH-PxCoRdZgINfMpYmUHcSNmbc5i8GK9v_7aqCoLbGCuL18L3aPWg6K4Yb-dbkuFqVfb6zrHjrFxNJN0CVvc-rmIlj6FOYGelj6V4oT7nMcVLoEfWr2fXtL0QDiGgj_PCS3kmQBrtoSeDtySiSVcRc6LeP5JBwq2xpdsVHkisJySvFLo6BWzeKUomke_CJLwqrXcLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gP6ZK0Oeu25uS3g01rBNwbvjmudVOKoL39IekIqmJ5fV7h90Si-u1B4sdDc0MvlJrEJ5OZWpl2hbAn47z1MFIzoc2Nd9bJL84LP2ttVd00tPbHVL6ZDCM2cIlFEUQ9iwT15McSxeI6cnsOr37psY3H3ZXTc7AYdg4ViJPXX3-mhfjt80g6Wbg3PdHgPbcfutwhQyaTATzWJhe8cvxPuREA_209xaDYn-6XkQlAPeYNnqeahO6Tn0obn-_MmAwX7SDn0Uge8XuIwwYCfuPf6jKEArrXu_hybBwLjlj3evm8THStJjTbS98Wbyi9N4PkLGI-TWTPuBvKpRaOtDwZ9sTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قالیباف: اینجا نماد تقابل جبهۀ حق و باطل است
🔹
اینجا جایی است که دولت تروریست آمریکا به‌عنوان کانون اصلی جبهۀ باطل، زمانی که دید نمی‌تواند جلوی تقویت و گسترش جبهۀ مقاومت را بگیرد، دو تن از مردان بزرگ جبهۀ حق را ترور کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/456955" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌ روسای جدید دادگستری ۹ استان معرفی شدند
🔸
آذربایجان‌غربی: محمد علی‌نژاد
🔹
ایلام: جبار سپهری
🔸
لرستان: عمران علی‌محمدی
🔹
خراسان‌شمالی: مسلم محمدیاران
🔸
زنجان: محبوب افراسیاب
🔹
کهگیلویه‌وبویراحمد: محمدباقر نریمانی
🔸
چهارمحال‌وبختیاری: سیدحسین حسینی‌وردنجانی
🔹
کردستان:…</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/456954" target="_blank">📅 11:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌معاون اول قوه‌قضائیه: در ۱۴ استان هم‌زمان جابه‌جایی و تغییرات مدیریتی درحال انجام است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/456953" target="_blank">📅 11:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCoJRn5MYeJdXAUPXfxUfgnyZoUfkytIDqnPBJGf97AnM-Yk5FQsiEIMi1vxltKWT2X0-9LAWsCPAAq_MEHLsDS2LZ2tW1KpmwdpDCKm-KxFFZC6uhie3fDS0qON873I3GMtqykw7UnMXxtmogJ94oPG6mAT4SKpzFWjQm78SbI88R3VrpLL7W-DCce8muTPd9FRQ5JO2c0y4X0jE_PXipsKKqtGZwYd_HvoAJvwzyQB3Ko4EzRrIgnFdfCe80_-fx2yr-wTwnrY-IPDdNhYWQWne5RYJGZjZwse64-LfZx2Ev1qC-Y9njZsky8rqRGkDVOsR2tBf-wdV1Fu9rwPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیران جدید دستگاه قضایی معرفی شدند
🔹
ناصر عتباتی، رئیس دادگستری استان تهران
🔹
حیدر آسیابی، رئیس سازمان زندان‌ها
🔹
اصغر جهانگیر، رئیس سازمان بازرسی کل کشور
🔹
علی دانش‌آرا، رئیس مرکز حفاظت و اطلاعات قوه‌قضا‌ئیه
🔹
نورالله سلطانی، معاون قضایی قوه‌قضائیه
🔹
امیری‌اصفهانی،…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/456952" target="_blank">📅 11:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456951">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14759aee2.mp4?token=bvyelO3NXLRolNZDxPQ_bMjOzM73ch9Pet7jBVDe8Gjf8gvQ9uS82vNbLOBG9WIhFyyiw3M_ORNcTrmmB_ObKreFrvyqL2AuEwyNFwwDQo16lG04BSovbxOLHmZCETUje8Zr2-Jk82kOn_64ERDYYPya8o_Bs6qhtG8kozCYhdCQ_vqwyShOy6ztYNxLMekN7yFVHhunrQf8dWEem6RnqMYundaZqlDgC8wndj5Rke1YLOFynlxbYvtKEfTL0sPda28lBjqYk3Fug73rZUZnORvDZtyOTSOS6CjyyTLvx_UZTjWbP5HlO6flebYDOHfj6-mz-Vm80CfjtNhEdsZLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14759aee2.mp4?token=bvyelO3NXLRolNZDxPQ_bMjOzM73ch9Pet7jBVDe8Gjf8gvQ9uS82vNbLOBG9WIhFyyiw3M_ORNcTrmmB_ObKreFrvyqL2AuEwyNFwwDQo16lG04BSovbxOLHmZCETUje8Zr2-Jk82kOn_64ERDYYPya8o_Bs6qhtG8kozCYhdCQ_vqwyShOy6ztYNxLMekN7yFVHhunrQf8dWEem6RnqMYundaZqlDgC8wndj5Rke1YLOFynlxbYvtKEfTL0sPda28lBjqYk3Fug73rZUZnORvDZtyOTSOS6CjyyTLvx_UZTjWbP5HlO6flebYDOHfj6-mz-Vm80CfjtNhEdsZLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری یک حیوان‌آزار در تالش
🔹
پلیس راهور فراجا: پس‌از انتشار فیلمی در فضای مجازی که در آن یک خودرو در تالش اقدام به کشیدن یک سگ کرده بود، رانندهٔ خودرو به مراجع قضایی معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/456951" target="_blank">📅 10:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456950">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
اژه‌ای: در دورهٔ جدید قوه‌قضائیه انتصابات جدید انجام خواهد شد
🔹
برخی از افراد دور همین میز ممکن است به‌دلیل ایجاد تحرک، جابه‌جا شوند.
🔹
شخصاً پیشنهادات افرادی در دستگاه‌هایی خارج از قوه‌قضاییه از جمله سپاه، وزارت اطلاعات و برخی مسئولان سابق در دستگاه قضایی…</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/456950" target="_blank">📅 10:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456949">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">منبع نزدیک به تیم مذاکره‌کننده ادعای کاخ سفید را رد کرد
🔹
درپی ادعای کاخ سفید مبنی‌بر لغو مذاکرات با ایران تا اطلاع ثانوی، یک منبع آگاه نزدیک به تیم مذاکره‌کننده در گفت‌وگو با فارس گفت: اساساً مذاکره مستقیمی میان ایران و آمریکا در جریان نبوده.
🔹
گفت‌وگو برای اعمال حاکمیت بر تنگۀ هرمز با کشور عمان برگزار شده. پس از نقض تفاهم‌نامۀ اسلام آباد از طرف آمریکا گفت‌وگوها با طرف آمریکایی متوقف شده و گفت‌وگوهای اخیر نیز با طرف‌ عمانی ارتباطی به آمریکا نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/456949" target="_blank">📅 10:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuSaV_QL-NVVJ0iQqax4VymhNgYjvjmCEYYsnClotboAA6oeWzjJJt3buEnJ-ZU136pZfuAcPTknPn8mclEUfEKQgyNiMi_7P9Fs7zJGwxmpVhPOYBszDVKYBTheL8iVzhtNR2wBC1xLHLLk2rypp4c93qXMOexXIqDg2yLpycjIlqrnG-97_3JpEm-y0NUt9DpUMZQ3OVcfm6MbFNUX_IDChUsZUn4qa5x9lD_dnFHC-_rkflrPZmYnfOzAzus9dXiZdwEPQ7f6fBWqeWFAvYaI_PnxIuPydW-DlRaSQA354PttY0GJGp4fhCs4TcC4VhyvBPlmM36nPZyp0AHHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصمیم جنجالی دولت برای سرنوشت جمعیت ایران
🔹
براساس اطلاعی که خبرنگار فارس کسب کرده، موضوع تغییر ساختار ستاد ملی جمعیت در دولت مطرح شده و قرار است این ستاد منحل و مأموریت‌های آن به مجموعه‌ای در دل معاونت «امور زنان و خانواده» ریاست‌جمهوری منتقل شود؛ موضوعی که در صورت نهایی‌شدن، می‌تواند جایگاه سیاست‌گذاری جمعیت در دولت را با تغییر جدی مواجه کند.
🔹
البته هنوز مصوبهٔ رسمی و علنی برای انحلال ستاد ملی جمعیت منتشر نشده و باید منتظر اعلام رسمی دولت ماند؛ اما اصل مطرح‌شدن چنین تغییری و برگزاری جلساتی در دولت، آن هم در شرایطی که کشور با یکی از جدی‌ترین بحران‌های جمعیتی خود مواجه است، پرسش‌های جدی ایجاد می‌کند.
🔹
چرا دقیقاً در زمانی که نرخ تولد به پایین‌ترین سطح رسیده و خطر سالمندی جمعیت هر روز جدی‌تر می‌شود، باید ساختار متولی جمعیت تغییر کند؟
🔹
ستاد ملی جمعیت براساس قانون حمایت از خانواده و جوانی جمعیت ایجاد شده و ریاست آن بر عهدهٔ رئیس‌جمهور است. ترکیب این ستاد هم نشان می‌دهد که قانون‌گذار، جمعیت را مسئله‌ای فرابخشی و ملی و حاکمیتی دانسته است؛ پس انتقال این مأموریت به یک مجموعهٔ محدودتر، بدون آنکه مشخص شود اختیار و قدرت هماهنگی با سایر دستگاه‌ها چگونه حفظ خواهد شد، می‌تواند تبعات جدی برای سیاست‌گذاری جمعیتی کشور داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/456948" target="_blank">📅 10:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456947">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKuu7bwz2c4Yg5vomdw-5gnA1_yPRW6F_uLPc127PwA09vdH1dwuga1cbziv_sNx8oO4nZfgQTn3rXbkk6K8ioIWL6ydirrG8aE4MwlescwyZUS88H4qdiH8JlqPiUJuTdhZlfbtyG6UGVxR57JWk0sMk-0lqj1rK64xU5Kd060yB7FfJ1F-4315-b9XAKbPlusQ2dQjMNrHvMEgmO34Z2KL8EbJwhplKZ2mID-WWAd9A46UvPu04GcKR4igP3toGJs3c4Oor9ZoDYasWms9r3S6ijHj9Io33g0L3F-Dfud1aY-re5-w3pAcydeQrcrw8sHvhaCs-5dn-7lIuN3s7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رالی صعودی نفت آغاز شد
🔹
هر بشکهٔ نفت خام برنت امروز به ۹۱ دلار و ۶ سنت رسید و نفت وست‌تگزاس اینترمدیت آمریکا ۸۵ دلار و ۳۱ سنت معامله شد.
🔹
نبود قطعیت دربارهٔ وضعیت هرمز و به‌صفر رسیدن تردد نفتکش‌ها در تنگه در هفتهٔ جاری همزمان با تداوم حملات به کشتی‌ها در دریای سرخ، مهم‌ترین عامل فشار بر بازار نفت در روزهای اخیر بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/456947" target="_blank">📅 10:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b698366e68.mp4?token=Qxphj4AMj4qKV8Cu_HvX9ef0Ec8jYPEnSdbMyGZ5c48wFYxcoSWL4cx9jGQCZo9hkG1TvTla80G4TYtYBnrB26XrE48pm-zr7m6b4MZJecHIB5c_kPPgSmfv_DrNcdUEB7cMFwAk229p-BB02KgBMK5kPCOg9dnUD68PQbiTQkXmhzsjis-RhDpjfSd7xEcvFpLSHyHeYTRJW8XEL06pTheWVlm86mS7ngWzVhIZwzGlAjud0iW1xmFtQzAKaBJASf6QhmOHArBREshs1P9gOzZ7DtVClot5plouvYhU0vkuDbTqOcyZZcleEiA_SGX1xdFrmN7_AcQ8scHNQrLKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b698366e68.mp4?token=Qxphj4AMj4qKV8Cu_HvX9ef0Ec8jYPEnSdbMyGZ5c48wFYxcoSWL4cx9jGQCZo9hkG1TvTla80G4TYtYBnrB26XrE48pm-zr7m6b4MZJecHIB5c_kPPgSmfv_DrNcdUEB7cMFwAk229p-BB02KgBMK5kPCOg9dnUD68PQbiTQkXmhzsjis-RhDpjfSd7xEcvFpLSHyHeYTRJW8XEL06pTheWVlm86mS7ngWzVhIZwzGlAjud0iW1xmFtQzAKaBJASf6QhmOHArBREshs1P9gOzZ7DtVClot5plouvYhU0vkuDbTqOcyZZcleEiA_SGX1xdFrmN7_AcQ8scHNQrLKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف خطاب به حاج قاسم و ابومهدی: بدانید که تا به نتیجه رساندن آرمان‌های شما از پا نخواهیم نشست
🔹
من در این مکان خطاب به این دو شهید عرض می‌کنم: ابومهدی و قاسم عزیز! ببینید ثمرۀ مجاهدت و خون پربرکت‌تان را.
🔹
بدانید که ما و همۀ باورمندان به مکتب شما در…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/456946" target="_blank">📅 10:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60f37010a.mp4?token=QLK6NUsPJD5O33qJX5hp-urfC4z4KeiwutMKPCsPEwSGVGOb5r0ScwgLN2KJ-HJysc7ZSVWPYFxQr_FLEyG5bdEAnRbZG50KBE0V9O9Jsrxo3Fvvj6s3OqoUNt7IVOh-9USK0T92RHQw6EP8pEoO715o_ufGl5unDD80sDIJ7jVjMa0JwW5fxdfFv7ESZ-1NLOkRAiaBz6bOoOYgWt1Irh_e3ADeD2RdsYyEqn3Vg9KbhgNZ20qkUIwHHC11SciOolZrdycKDI_ZJNgMkfwu02NDMXeyj5cEnNPdGk-I10PHgCxiCpX6yFlqWaHYrrdadvBDwGy10PqGTXm7IsRMRRO5rmDfYei7egfqZ7UnEoI0_EWBh02fHyRTFdmjnleFgg7K2nSe2PavSy1bnmSSkhYI-pvLhovanZJxocwx8TFQN7wbfJU-hWm42ipw835ocUK5Uh1xPd1eedbpZOaoroYn4v6cPFpdiVygWN-8LCmaSRFdqbthS5IyZ2pbcNGT6_rHnieYhcamXmqKzPZGLAR1SaCiTABkIQ9Q8tknCOWZ5Vov8Ljtw1Ea59BgJ55NM89_jhNTmeLO28FCL50xTXakkuhZTCiaVJVuOFdTUrpPai6eZn9EU-eGkGqiUSUnMa3I5dU8rCqqoV7CmKdTVgEKqRfekwsJu6-aQs2UpzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60f37010a.mp4?token=QLK6NUsPJD5O33qJX5hp-urfC4z4KeiwutMKPCsPEwSGVGOb5r0ScwgLN2KJ-HJysc7ZSVWPYFxQr_FLEyG5bdEAnRbZG50KBE0V9O9Jsrxo3Fvvj6s3OqoUNt7IVOh-9USK0T92RHQw6EP8pEoO715o_ufGl5unDD80sDIJ7jVjMa0JwW5fxdfFv7ESZ-1NLOkRAiaBz6bOoOYgWt1Irh_e3ADeD2RdsYyEqn3Vg9KbhgNZ20qkUIwHHC11SciOolZrdycKDI_ZJNgMkfwu02NDMXeyj5cEnNPdGk-I10PHgCxiCpX6yFlqWaHYrrdadvBDwGy10PqGTXm7IsRMRRO5rmDfYei7egfqZ7UnEoI0_EWBh02fHyRTFdmjnleFgg7K2nSe2PavSy1bnmSSkhYI-pvLhovanZJxocwx8TFQN7wbfJU-hWm42ipw835ocUK5Uh1xPd1eedbpZOaoroYn4v6cPFpdiVygWN-8LCmaSRFdqbthS5IyZ2pbcNGT6_rHnieYhcamXmqKzPZGLAR1SaCiTABkIQ9Q8tknCOWZ5Vov8Ljtw1Ea59BgJ55NM89_jhNTmeLO28FCL50xTXakkuhZTCiaVJVuOFdTUrpPai6eZn9EU-eGkGqiUSUnMa3I5dU8rCqqoV7CmKdTVgEKqRfekwsJu6-aQs2UpzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویری از ناتوانی تجهیزات زرهی ارتش صهیونیستی در برابر پهپادها را منتشر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/456945" target="_blank">📅 10:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVwTU7GAcRWNuijulrTufhMAFaN3whYAaRCFVdQeQcsQxRF3N7av2x61MdSUDkl0Ptteti2vjwlh8a9uIta0ojvZCzvLeVYEGHtuH4bRfcN_-rpHKsAjI3Cnl12qDRGrregHmvRNeLSv16V2Exyua6wrqp8Miz-3-7hRuzgfqeYfaXOI_lWJzk8e6UqhdVm96wMX8CDybtWs2PV05-bgvBbdWA8azpBqepz79mO1O87bX7rfE45Poz40RRT72cK19y6IEJlwYDLMMnNZZLmUUIPJ6Az3YJZb4ZHn6G4f-Vl_wYGiEeauUj7bvwK9hjN3gYuJfyDhdZDN_sYXN0V9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژمانفر رئیس کمیسیون اصل ۹۰ مجلس ماند
🔹
در جلسۀ صحن علنی امروز مجلس، نصرالله پژمانفر با ۱۳۰ رای در ‌ِسمت رئیس کمیسیون اصل نود اجلاسیۀ سوم مجلس دوازدهم ابقا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/456944" target="_blank">📅 09:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۶ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/456943" target="_blank">📅 09:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456942">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2mTzGHfmicRFhCWZYPJVNOti79mztDUakB0NjOROz4k_685DFLnZqmKr5ghMZ4aIjomEZb_9heIeOgJw2XxPOnkNF8gHXPUjCh1pQNe0-i6vuHh7cOUAAZwB65G_1RBHBnviro4ULL7_dXRBbO5vGgTfs-UyzcBY7NwcKsp8e065KmiE39nfVQOVs8IweX6XugY6s0M7VrZwQA6iiR0cjsclxDLLtgwXsM0gisukH0fvXsAtTX2L1RUZGqTUFb6-V2ClrQ0v0qBFj3cFYi7PQwSPTf95eaqQJrtlRvhPgJjgtcxJKP_ZXcZJXmYnmQmcfGmPa_YbOVdakP89oHOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: چین دارد کانادا را تصاحب می‌کند
🔹
چین دارد به‌طور موفق و کامل کشور کانادا که زمانی بزرگ بود را به دست می‌گیرد. دیدن این اتفاق واقعاً ناراحت‌کننده است. فقط امیدوارم هاکی روی یخ را دیگر دست‌کاری نکنند! @Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/456942" target="_blank">📅 09:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456941">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=vQq-__c4xvb8bXDnn6bHA9fEgwL3StJYCu6Pf9DuCJm_APWxuL3YPX1VzQ_sh0lSmM5D65v9Aqnjr5aj1tmRYaiVV6yIf_rSFT1giHGUKIzs4aSq47Os-ibiunIENKVO_wB87POmyjbh2NLmYbW9n7r3aZaw74pUmHZlWzZ6drkTuDgjXZbZbSnAUESNiR9C2yGlxec4jhekfIxpBFim8fTp-iiRO8YlPgqBvPb0y-vehpXPOX5PxnM17t4xUhmVWrNCRzUvnXW8-kU5Fx_FKoSEEkb9AnfjsTFIFgZdEVvoz4KrqNRFqiANmoFiHak9qUr7xMvtm3OPbrwNEc0z4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=vQq-__c4xvb8bXDnn6bHA9fEgwL3StJYCu6Pf9DuCJm_APWxuL3YPX1VzQ_sh0lSmM5D65v9Aqnjr5aj1tmRYaiVV6yIf_rSFT1giHGUKIzs4aSq47Os-ibiunIENKVO_wB87POmyjbh2NLmYbW9n7r3aZaw74pUmHZlWzZ6drkTuDgjXZbZbSnAUESNiR9C2yGlxec4jhekfIxpBFim8fTp-iiRO8YlPgqBvPb0y-vehpXPOX5PxnM17t4xUhmVWrNCRzUvnXW8-kU5Fx_FKoSEEkb9AnfjsTFIFgZdEVvoz4KrqNRFqiANmoFiHak9qUr7xMvtm3OPbrwNEc0z4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ادای احترام قالیباف در محل شهادت حاج قاسم و ابومهدی در فرودگاه بغداد  @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/456941" target="_blank">📅 09:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456940">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe28ef4b47.mp4?token=jjhczC0kw6mw8iphoKshNpEUFmpZahd08PGBa19G0gKq-lcFlK7gI1Q2KpTbgzWeHmrgvdVeub8gh0jinGrvKiQ8GDAvpiwXumOI5-y9kHcQ4eMVNYmZVfuWG2KybuoFTN3URviSIvzZ_7ANLjgSyt7IvqyWe9c0tX17T5X36gf8WS59WNKr0WFF4fKdeP-U7GVJ9EY_lnNhSRUAtjiDwCmnXTk7nKESNT4JGJalunineLx3sxpf38KRJe04vcyxHlXDGdgrCK2pxonrHf3jIWB9v6jmgQwNjFNBSkOjwevN_HdDPqA9_HxYq0D-EiEMRXVKAkNk30lyyEEL2Hgrig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe28ef4b47.mp4?token=jjhczC0kw6mw8iphoKshNpEUFmpZahd08PGBa19G0gKq-lcFlK7gI1Q2KpTbgzWeHmrgvdVeub8gh0jinGrvKiQ8GDAvpiwXumOI5-y9kHcQ4eMVNYmZVfuWG2KybuoFTN3URviSIvzZ_7ANLjgSyt7IvqyWe9c0tX17T5X36gf8WS59WNKr0WFF4fKdeP-U7GVJ9EY_lnNhSRUAtjiDwCmnXTk7nKESNT4JGJalunineLx3sxpf38KRJe04vcyxHlXDGdgrCK2pxonrHf3jIWB9v6jmgQwNjFNBSkOjwevN_HdDPqA9_HxYq0D-EiEMRXVKAkNk30lyyEEL2Hgrig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان سنجش: در کنکور امسال ۶۵ درصد خانم‌ها و ۳۵ درصد آقایان شرکت کردند
🔹
امروز آخرین مهلت دریافت کارت کنکور است. آزمون فردا و پس‌فردا برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/456940" target="_blank">📅 09:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456939">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">محکومیت ۷.۵ هزار میلیاردی برای یکی از متهمان پرونده‌های کلان اقتصادی
🔹
رئیس دادگستری تهران: در راستای اجرای منویات رهبر شهید انقلاب و تاکیدات ریاست قوه قضاییه مبنی بر حفظ و صیانت از حقوق بیت‌المال و دقت مضاعف در رسیدگی به پرونده‌هایی که با منابع عمومی در ارتباط هستند، با قاطعیت و بدون اغماض در دستور کار قرار دارد.
🔹
کارگزاری بانک کشاورزی دادخواستی مبنی‌بر مطالبه ضرر و زیان ناشی از جرم علیه سعید جابری مطرح کرده بود که پس از صدور حکم اولیه مبنی‌بر بطلان دعوی در دادگاه بدوی، پرونده جهت رسیدگی دقیق‌تر به دادگاه تجدید نظر ارجاع شد.
🔹
دادگاه تجدید نظر با بررسی دقیق ابعاد پرونده و با عنایت به سوابق محکوم علیه در محاکم کیفری از جمله اخذ رشوه، تحصیل مال نامشروع و ابطال ضمانت نامه‌های بانکی، ضمن نقض رای بدوی، حکم به محکومیت نامبرده صادر کرد.
🔹
فرد مذکور به پرداخت مبلغ بیش از ۷۵ هزار میلیارد ریال محکوم گردید که این مبلغ با توجه به لزوم تعیین آن بر اساس شاخص اعلامی بانک مرکزی، در زمان اجرای حکم محاسبه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/456939" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKra7DQc1ZGXg81trWZuoswzPMfTe9nEQylQY3brx1NfqymbPmDubG1npvk2PVXjGFomI7BZZStfN0Ffzb3v_fwMa0cpKWbBWACLjJXaM5PoHC21sQbSKg9L4PnvpjCwZ7lrL2Do3jN_rPp5WPPfCQhFWus98iKe4Fl7EuoPVA8aF6NZAZjQ6ZzrPPxXXVvy2cAqEb37z2qNqrzlhCD6p_mUTNLRtoEM3S0WKO0GCgw3IVIn209ViCdUyR9EOk8TAXP6MVMqkXV2RoTcGZpJ_GqJjGC58SAo-vcK5sEoDB-PkTRP3SsS9_Rt1TL0Maf9Q1iqjUEvln2fisUfVfBUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2vtHlD0kPrbXhmn5w1I4M3i9W_gWusep3f5-KRdqQeF5Qwg9dndJqFTyVOeVMHePw2w_VChS70c0b0MbW_yrjZ_JmFoG1bfLMpCls8JVIcKzfozJQJt5rZmQakjYYmiFNJV03NgNIgje2xqVOd-sbH4_ZNctsn77FKDIrC_6-bfnsKzsy5jk_RSABk21QQE2XoppjVlkExliZm7gjJPGIgpGX8ZSNBrDqra6aFEMc3V7Cxwqjl0InlrR_okYBbWsjiIBJcL-E8GdQrVTq3enuEZsgr10Yr0msiJ6AnbnSvy0Rc3HFW19Z_xJyvAQx6eQhw3sLlbAcZSez0N1fg8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8zGB401EC02XwJdSsCEsr7aAsUlQAHoS7cILIgKLnpJatxuDNhLwjy-HpN8AUuCdsL6QxoGYtbi_uKcHhq5VUeGy1tuE51gWKmHz82cr-fwCPdcOJMVtAvAMAFqaZdz4EMG_k5j8jwClIakLOv2hhIO-dmBmXfWwt5woyWS15r-oBOVL7EKcA8qwlTDR_HTkSvimMArra07GcvH4R7wjR_sBxapQgrcqC2ZTusZ4a1v0La0SE-F6Mg75S16bAqhFURnnMOQmW40aJed6jkIVbZtO86iPFOgASHUkZhwDwkxrhhdV4hw-5323RekNuoZujztsvcFXvYuXA4yzoqGVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: شاهد نظم جديدی در آینده منطقه خواهیم بود
🔹
در سفر به عراق با شخصیت‌های بلندپایه مانند رئیس‌جمهور و تعدادی از شخصیت‌های اقتصادی و فرهنگی عراق هم ملاقات خواهیم کرد.
🔹
به نمایندگی از رهبر انقلاب در مراسم چهلمین روز تدفین امام شهیدمان در کربلا حضور خواهم…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/456936" target="_blank">📅 09:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB-z1M_xZzhSy1_qNC9cwr0hsegDE88mCvvekC14CtewwzJQL1qD9ZGqPuDFextZw3NknuKwyw-uajKNk9eMpbsOmO2O3pIh__l1URgcb7eRSv9s0hvhS8HhDfWHh3vTbXfzAqOWjMjQzctx-nz5dejwBhQsRPiG-2BC3KsaIqxaeR0-hX6ydFBteOIP9SnbiZHyl1_cWXEBRYLmRIVgb2YjhGIi8g0yk167veWef95qJ06RrSJ324FfsT6Pfb44PZSk4vPoVD1zV-Gzz7AecR_E6K9jAsjpELTHp2Y-2vjxoW4qs2e-8xbFOa05pNyxinmyKucrl2AI8lFsk2nGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هشدار رئیس ستادکل نیروهای مسلح در خصوص کمک به ارتش متجاوز آمریکا
🔹
سرلشکر عبداللهی: کشورهای حاشیۀ جنوبی خلیج فارس که با صدور بیانیه‌های مختلف اعلام می‌کنند اجازۀ استفادۀ آمریکا از سرزمین‌هایشان علیه ایران را نمی‌دهند، باید بدانند که چیزی از چشم ما پنهان نمی‌ماند.
🔹
این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.
🔹
هشدار می‌دهیم: هرگونه کمک و تسهیل‌گری به ارتش متجاوز آمریکا به منزلۀ مشارکت با نیروهای نظامی آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/456935" target="_blank">📅 09:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456934">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafae608c2.mp4?token=WJ-94JCorE9gPr-T2ZNPWxd_fkjdP9AoDuqL3QBNQdj2Xsghzp57IylzG_yqG9m7cktxFMztysBZGODYo60OYAZSlWYg6uudiOVm8e3IRq7PJIwtmhBnYcc98O1pLTPHIVcpcJ6BKp2YZmkl2B6lHkXDmq8nZtMNrCYtW1bb4HTDXh8JzluU3WCF8_tlmz5fFBNZs3bCGH_3zheMlvD4KgeBfQx6ugHA1TWPg6POF_Ufjf70qwkU4MJ3PvF6Vx2-zjLUkUKa3TsP4xU-YocMU1rnqm92G6dce98Axjl_l6kb25ywwvJ6MztpeOrJsm8cosfh6mUZ6S1xUjm8o-1SAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafae608c2.mp4?token=WJ-94JCorE9gPr-T2ZNPWxd_fkjdP9AoDuqL3QBNQdj2Xsghzp57IylzG_yqG9m7cktxFMztysBZGODYo60OYAZSlWYg6uudiOVm8e3IRq7PJIwtmhBnYcc98O1pLTPHIVcpcJ6BKp2YZmkl2B6lHkXDmq8nZtMNrCYtW1bb4HTDXh8JzluU3WCF8_tlmz5fFBNZs3bCGH_3zheMlvD4KgeBfQx6ugHA1TWPg6POF_Ufjf70qwkU4MJ3PvF6Vx2-zjLUkUKa3TsP4xU-YocMU1rnqm92G6dce98Axjl_l6kb25ywwvJ6MztpeOrJsm8cosfh6mUZ6S1xUjm8o-1SAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز توزیع کارت کنکور ۱۴۰۵
🔹
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت کنند.
🔹
آزمون تجربی صبح، هنر و زبان‌های خارجی بعدازظهر پنجشنبه ۲۹ مرداد، ریاضی، فنی و انسانی صبح جمعه ۳۰ مرداد برگزار خواهد شد.  @Farsna…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/456934" target="_blank">📅 09:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456933">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=IWPkf3OiWCfppHDNWPmav_1DRRc-mlZhUhJsmaIlKe-SEQN2OBDWCThrmhTw_10W1ywaly4qKIZ-uh-ZkhfO4C3bt2SVGSYuRowzbt3W9TgCDNzsEQbjs07nVnE5YxrlAcxvANqjoLXGXtlrivN7UvZdLFFLPwh_LfXV2Tp2SIhGY3Z7-QHCv6Ls3yJn25RSjVpYG_NtGmDwsoGYVRsczyHRrLj1vq4qAfqMYtGqWu85TjBsfMzP5Wye_u2GyM3mV_rYR494yJkJUKMyH9cFaKVhAXIbSpRh5VlyQP6jjDhldhIwxAzvt9J8WPKsOmi-NV-ZtIVxPP0wcBjA27FHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=IWPkf3OiWCfppHDNWPmav_1DRRc-mlZhUhJsmaIlKe-SEQN2OBDWCThrmhTw_10W1ywaly4qKIZ-uh-ZkhfO4C3bt2SVGSYuRowzbt3W9TgCDNzsEQbjs07nVnE5YxrlAcxvANqjoLXGXtlrivN7UvZdLFFLPwh_LfXV2Tp2SIhGY3Z7-QHCv6Ls3yJn25RSjVpYG_NtGmDwsoGYVRsczyHRrLj1vq4qAfqMYtGqWu85TjBsfMzP5Wye_u2GyM3mV_rYR494yJkJUKMyH9cFaKVhAXIbSpRh5VlyQP6jjDhldhIwxAzvt9J8WPKsOmi-NV-ZtIVxPP0wcBjA27FHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: به نظر می‌رسد از جمعه به‌بعد تهران دمای ۳۸ درجه به خود نبیند
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/456933" target="_blank">📅 08:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwukuWqxcpu0CDvSZ4UsbFYdfm74Ry5NvGdaq74mgZWCDcF9d3KGjBA1GJOT03-UvO1P0jElaOT8hGCIgoXjtL03NngHvT88yx9LCuYCGcuN3fdXu_jeQ2bVpBTdN7pruIld94b9TkjHMImQQ8-vaoujt5l-6En82EZa-pV-6kDjisXIznaHWoJl3shuGg66WXefs3zxey54K5lb63JMx2TzYiP_YddAyXN6BCbN-VTL6Tr8uikmJoUM-70VA5mPTrdnirpy3sep17fKsCjlAg2KZLUH7jBFnZwqXjT1mjl3B_alXC1BKZMAp7dHIQa6vxsJ0lDxcwC0eisYRZ_Tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم عراق شد
🔹
رئیس‌مجلس با هدف گفت‌وگو دربارۀ تحولات منطقه، تقویت همکاری‌های راهبردی تهران و بغداد و بررسی راهکارهای مشترک برای کمک به برقراری ثبات و امنیت در غرب آسیا، تهران را به مقصد بغداد ترک کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456932" target="_blank">📅 08:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlWjV9KBqiEpou_LcgCNEdgIfzN7C-qCwIY48tghfJ1f_eOWyzkQUU1uoerNgEoBqUEhrd4-Wkkq7N5_P_Ag9oQknglveUL8egTE8qdxrP2Xv1q7SQGDVzTMxLNRlwzNkZqV9KDgJsic6XQ8Csofo4JVd3Tz2hTT5vpqCYyRoZyLzZE5ARxGuVhdLOayIUADWptygE37lBqf6yGB1-0VK915XfH0hJds7vWz1BPMHTcYPidNsknBiKmHQgPVXt52oUG52j2ny7j9_77H4LKw0nD4j5XWEhtFlry-nCxylUGLeCGvo3KDif9enLs7W_rOcLvsHSaOERuxJMNK0Sl4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول نفت آمد؛ مخارج دلاری دولت تا دی‌ماه تامین شد
🔹
طبق اطلاعات کسب‌شده از وزارت نفت، ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفته است.
🔹
این رقم ۱.۵ برابر درآمد نفتی در ۴ ماه اول سال قبل است.
🔹
طبق روند بلندمدت هزینه‌های دلاری دولت، این رقم کفاف همۀ مخارج ارزی دولت از تیر تا دی‌ماه امسال را پشتیبانی می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456931" target="_blank">📅 08:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456930">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZcDBrGwT_fVD67TIBhEt8goZR8hgck6opbQCArOZJBffWnsoWZ3jVoc3A39N0xzYOSTCWiBxYzOmadXcSjOFoJsVKecYaWzncWtZxGJRubvkN2qU7BJiSOiKEeZfPbQoiXkKeCnemKHIA6rknd-fxUamQO82tpEvrz77Z46dPg6SNtM2SaWrFgGyB5LdCrvfL7V8PkeRBZQSrtLeDwnVcMeOK0L_sxSG0HGF9Ha8f1e2lZ5-hksnRMErQ-84XZLaiu5mo3rLFpfmvCcKR9oKFsClfWiulQv9NTDFaAXxrdE-CmKx2C4idCm-OylAfnyIldFXKMjAYMTY8AKAiJ8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش توقیفی امارات در راه بندرعباس
🔹
براساس اطلاعات سایت‌های ردیابی کشتی‌ها، نفتکش توقیف‌شده در تنگۀ هرمز به سمت بندرعباس تغییر مسیر داد.
🔹
مقصد این نفتکش ابتدا بندرجبل‌علی تعیین شد اما حالا به سمت بندرعباس می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456930" target="_blank">📅 07:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456928">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d41vgMQ0uVOHrON17QO3NyM5fO3Cfdw4vq60KmoA27MwtoI0oLBsxwntuh3PsyxqwuJ7z3x9MpeGH60KeCtl-CZ7bH0gM6yhPRDduPtvL2iihnKfM3FvrVM8HBkvXcJwyKEOnxnFCOrF4j7KSI9mwc71Xu4jxQy7CuPGMBUevoAagCulSdwOYaVOR5MN42DMWd9kyr9_1mFJflySOb0aV7mI5zBcwQ_bKe0neMmkQs_--DSviPTmrp1gYnn2Jhbm76TyKF5r0qwy_MOrb6bOsFthLGSHIyaGxm_Z0JzN6vjTYcYWlzfkCmadCDuhsJNzQuzQ6Tnu9qMG_LRA2bUPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف فردا به عراق می‌رود
🔹
رئیس‌مجلس با هدف گفت‌وگو دربارۀ تحولات منطقه، تقویت همکاری‌های راهبردی تهران و بغداد و بررسی راهکارهای مشترک برای کمک به برقراری ثبات و امنیت در غرب آسیا صبح فردا عازم عراق خواهد شد.   @Farsna - Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/456928" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
