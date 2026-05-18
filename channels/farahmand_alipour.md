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
<img src="https://cdn4.telesco.pe/file/rsO-zBEIJdxgi0T1gBBOHdj7wdTw6I9A_3vxFq_l63eo4DTLJpk32HTnUm68QxC4M4aCXed_Gq5Gz7Vz0hU_CuoLktBOVjI5ATD84JhWUieknrEmXIH6TArblb7am25mqakE90vj-Z3KYU7wgjEkuwmz_qN9_J701VQckyCiDBnvLMk7ijbbNAw9g_LejBgYq7UNhj2c4883yeJL2kW7hvZ-Jb5tmkWmX5RCTP1dCe4lJ-K_mS_loRZuBB6GPsN6y5RXgH3e_IutscqFxxKXrBa2dQAWGuDvlf99tHRCiLv2_OQbxp22SV-XwMekAoxhUFoltT0fGLH5tsEC8kwdbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=XD5xZqUvgRkK1pE8xj_b0YoD6f71n2v9Y0W8Xymb2inyRHzFZ0iHEMlMoijcYNBw62NQK2AKMNHcmgSLjb9RVDZlKSyRjEFobHYDEt58euIRm8r5Nykc_ckC4TTX3GCpUaqaiEL2diCYdwFysSmY2BscNV1888fJc3cPYT_GvuOBRKMAbdh0MsJo0Rp7O5DVeW66U_DD7z6UqVp3k99hyBVDz9-52IrLTbgyH-GD1DDdT6G3evBVPqP_o-rxYfywVOrU-85FUZw1D3gRufQt_qwEDWcs7mMlYruIVgtxE6Xx6hv8CvVeGShS7fYUefI57x7wOxdTXzEy3PNa_AljzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=XD5xZqUvgRkK1pE8xj_b0YoD6f71n2v9Y0W8Xymb2inyRHzFZ0iHEMlMoijcYNBw62NQK2AKMNHcmgSLjb9RVDZlKSyRjEFobHYDEt58euIRm8r5Nykc_ckC4TTX3GCpUaqaiEL2diCYdwFysSmY2BscNV1888fJc3cPYT_GvuOBRKMAbdh0MsJo0Rp7O5DVeW66U_DD7z6UqVp3k99hyBVDz9-52IrLTbgyH-GD1DDdT6G3evBVPqP_o-rxYfywVOrU-85FUZw1D3gRufQt_qwEDWcs7mMlYruIVgtxE6Xx6hv8CvVeGShS7fYUefI57x7wOxdTXzEy3PNa_AljzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve1t-OI_HZm5G3EVaBeezMQ24iR5Nd0qw0vbsHCvfmWTZRHCrDaMImIspzhSk28ijOc4nNKXzdTmQ6OlEse1PSN74-YdIUpqwdMH-QLh-MvUFgZRb_i86H6tqawRfObE0puD_kEjG8ysIvNPEX2oKYEVRTQLGBkE0W0_z_B9xLXxE8RE1r8L0-5vpX5DcxOILeZkNZoBml8s7vmvFvTgk4TUw4X1xIIAQuVbjq5-KVi3u4B9YCpqsw6XL-ZY2NHrMXuOF6NRrw1l1xMaAxHT3OkRknyJxLxuDZYwuAiIVutOVdgPFyVPUyJXxDo3H_GHZLwp_Y-y9Kur5UsZ5n-ZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn4pUQAh_qhz1yRM13i_qVdoaTkJxBoUJw057gC7YUmLCfjv6_PHFKNIhIoXA7riFwDtlQoEPdrenuZxa6srSbgyBtHqaVeort49dNn-de-MNnbe_Ww_1jg-TaemTeiUw8nh7dXXk_sprOXHvlaVuPj8fs2SAfc-8_NeoHPbqdjkktgU0eMxCYjLFZor1qauRKScsHwrpApfQ695HNyeMrKD_lSNfksW7GaGth-bc-R8MRa1mLa-TnIM3sF4viraOTkMTMofhxcL4XGSMwTzu2SuSbbIVpq68dBNcXmRb-eXVcZP1RqXWeTZvocINaMrAOAFd7FgyTY08g4dqZD7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YW9SuNGfEb0Nz04W31WoC4GM6gQP43LokDjHtEMD-zSJ3xAYeNs-G41tqt5XnfRzGWL9AwxTge2uuVUWf7AZ0hIczIYOgb362HdOtNetw3WRWkRh6CsAXrDYx-lEk4haBb_bz8t1OBa8Sz7-9mV20Y7O28kD78ErFtIgn_Kc437MJOCyD27TIfskHDca3PdMhjf-YP3c0Rf4tBLcDcpNPWhjiLAom4j42IsC9y-82LENWUSkc5oqDo0Rbaqnb7BnFmAh6maRDaSZAtujHJN6nDMmYPG9VtB3U3_CxNAAQjGqB6WKDMVAiTWvrfUCFdrIofrIloE-xkewqsKbXQm19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcVnPfCf8AoeTkqs-Cj0yyvXKUaSKlmvmGINZoxkj2T1vDjuIOI7gdkjShkJQp50hV4lM477HZiF22vKjy2qa6Vmy_zlKKeiuF4CA28tv5gWVz7gCNzmvydfVp1qOvl2OUnI0FBO0sXlfRHHNXHJ2k2wr3wxoyuOe-KFlrJDYgpDIlRuEPY4iGNo5fHKvnCv6YIV7z-ruf8YW0mIYsPSCYC3FUsjJXn7ckFQ4Qa58YFePdof5xVd8Hpr_l9F5anT10c1UBgl0CJoxwRNEVE-o-n9i2aXz-0jeD76aLI03AYpLnE2pSl1zOf-QS9VvuhhWJ3X96PV74fsQDifhHTC2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=RKKHOdIWSr7RJsq2mRWEeybL1e9uDvoayaEMeV5gzcZ7EKG-gUBytg7rtAWg56NlYp_NGwZwPHi8DJXNA8Af7NO_uaYrRB8LGGBJKcqNTybrLXZ3DKAFb-wbFGAcluHL-tIUFUnLhjUFUfDiDKNwucRXug_GxcVbTwyfsF5NIccDNYtevj9gISzBDIhEnv4PQV1IOqmUcj-k-T0FqtXjz74JY-auFRBvh-3j6sEXXuehj2HJH1yCtUj4HZsgoAvqgTJ4hB_0AUm5XzOFfQqZ9fjVS4xF_v0DIsa0E_MV7zgpkgPSEYn4digh23zsEZRpE0JBnPUgIjbw9iwZwkQO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=RKKHOdIWSr7RJsq2mRWEeybL1e9uDvoayaEMeV5gzcZ7EKG-gUBytg7rtAWg56NlYp_NGwZwPHi8DJXNA8Af7NO_uaYrRB8LGGBJKcqNTybrLXZ3DKAFb-wbFGAcluHL-tIUFUnLhjUFUfDiDKNwucRXug_GxcVbTwyfsF5NIccDNYtevj9gISzBDIhEnv4PQV1IOqmUcj-k-T0FqtXjz74JY-auFRBvh-3j6sEXXuehj2HJH1yCtUj4HZsgoAvqgTJ4hB_0AUm5XzOFfQqZ9fjVS4xF_v0DIsa0E_MV7zgpkgPSEYn4digh23zsEZRpE0JBnPUgIjbw9iwZwkQO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=EF6R4ch1m5tCbC0wRV5zakM2ERLBIk8GmftA-qMX0DOn70QkTnrvPdJ7ch4tKMGLg7toGZfNnhyI4RSiRdEnYwJqD9azybbkCNbrrgjHXQpIjsJBJ4_IvayO5SmFIgpGcSLFDWjgMoajuB5xDoukMADdXCnOpf1Jo-FbNSoIqD1AcWSf2kCJCYTgnGrOHCJRpD3-cnyKhKSfE89N_fVoGHBJ2UwjJKyb46FRMHme-2u_74mpRkEFzdxBLbIEbYs0wn-0A0Q-rnpdmLhW2iZWj5GHlv6lyNLxQt4A8YVZtVrBX38LOr2fX45Vh3E8HaWNp_nNAtMwtOhiUmyq4UocvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=EF6R4ch1m5tCbC0wRV5zakM2ERLBIk8GmftA-qMX0DOn70QkTnrvPdJ7ch4tKMGLg7toGZfNnhyI4RSiRdEnYwJqD9azybbkCNbrrgjHXQpIjsJBJ4_IvayO5SmFIgpGcSLFDWjgMoajuB5xDoukMADdXCnOpf1Jo-FbNSoIqD1AcWSf2kCJCYTgnGrOHCJRpD3-cnyKhKSfE89N_fVoGHBJ2UwjJKyb46FRMHme-2u_74mpRkEFzdxBLbIEbYs0wn-0A0Q-rnpdmLhW2iZWj5GHlv6lyNLxQt4A8YVZtVrBX38LOr2fX45Vh3E8HaWNp_nNAtMwtOhiUmyq4UocvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsvmeNvCzeUAslGMTOkjRjDMuYtLFxmn8rZGi4wq6qrRcEWuiOmATEJYfkzrKQtaBw6-KSc8VlpStwLYNN4T3A9556XFHENwsba6rh1bNiG1Q7sqbbQEkjmhGZiKdbY77939h_o6FaCBEguwSKesuDXJyUNGs0ulYxi2srDJ3y_mBzb3QxfJiNEBTYzY10ZHrIAU7fRxh0svdFQB9bydGcKe4hzG3clPy4e5--b9AMKnoYADWKGxRNEo3U52OfAZkMtf4YmZLgcEAoJv37bxtg-CY1Y4uf0vnC3EH4E6ZkoLIsZJlL5WNGfNjEvB9ap59c4nxWcfUkxdXbzfuBUK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjpwFCEUGqG2K891Q3q-lObzyR729XQjUPZVTcxvg5yVk3KZuITqVdy46vDqofCD4hm_Oyo481UxF2M6SsPzimxl--QthWFh8xONZQVU0gGAsC5OxKxGqievzkSBy_0uTL_D9iszLDnA8kpih4WH-5pstiDnTC9lGQ6YhWUg65gK-SFs6bucyRpEsiiy0a06n1dfcFH0C3Nsvg-0chhITMvwJHCGICjOy169iFjTVPeRq05cvmckW5ipTKGCBbXChpwDtIBaieLbmMWpL7978TWtq9Or0mR597oT41Rl46Ne-_gslaO3AGvCrw3gNCzpVOhNoBftfikHIaNIP1TXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS5jr9TXz-BZNThv0aD8vhyMnjAWJFV_caWU2CFXDIDyUi85510Ml59JH5Q4nWFfN-z4_S_3wwWn2Fl9K1j34cHMMLPWAUmy5qS-UjQFO2HAxBEZkEDZquIlxaemhadIPLihzgPS4bcmV7m_KC2poqeON022dZZjOGE9rvfCr8TLYlnZjh67ALR1Wq19rRiYikX_bqErlOJABZcgjOflwS8d4Nh-FgeHlmOeHxCJqlFl8u1mbsWhF2aPc5KYHY_yfVgWsxOTEvuxbQIJs6RWl5YTJONHTE5shAslnuL9pO642xKXPUzQ-6xQFKvqdVwexL-qgBc4GIbQ3hRdNLxK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfrZGxn8WhUXslglsgCgjVMCQr1MGCB5CH9X54CAJb-sogVXf1kUwbhyvxK7aPwVDccux9wPrRe1DqItV5Z2__rRSWBuxm0iFPbNYVseyfKZmEmwdAFZbvfInqwGpwn1ehCdYnxUIQqvHrp5-WTJ7cHVokfBdzaigG-OFaKHnwgQm2RbKYVFPeYfGcFZwNp2lQY3rP1luTTVxpZRIbOiAabvJyY7T74S-X4Y86VcWoUXm-pygi7F8q93616qws_35C3c4dtPViMv3dtBsW09mJW9hCCJYYZr889mIoCldLe_ppVZxA5Sqe_vwSUnXycs_EKyKev_3OfBkpIsUTZ65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=am78DGyLrFNFBw_08MHjqeuUqLVR8DYRfxIGuG1faOhvMsSCXUqDrN7F69r0yuXQUkZApSt2UWZGB4dXhVj_Vwpatr8aovlBStK7HyQebL9cbVD4sJaFxjhts1gAxyPeEzBJ0k1ZsapcoiG_PQaIju7XA1gKn40jt41V3M4FY6RIt3xPKY4uwGZCH7jZz7UdNIWqye079_jQUeCAEqTqNh-RggfBXEHAiYRcnEIg_OeiUvoMAuMX9HkNiVprK-Pbni7oM2PPpHbFuIF7jGeANj4q7HkDJxW3JWHMsE0Jl296eygbsaWMd49AMb_buUiNVMvDV5Bl7M7MTH4lSxiWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=am78DGyLrFNFBw_08MHjqeuUqLVR8DYRfxIGuG1faOhvMsSCXUqDrN7F69r0yuXQUkZApSt2UWZGB4dXhVj_Vwpatr8aovlBStK7HyQebL9cbVD4sJaFxjhts1gAxyPeEzBJ0k1ZsapcoiG_PQaIju7XA1gKn40jt41V3M4FY6RIt3xPKY4uwGZCH7jZz7UdNIWqye079_jQUeCAEqTqNh-RggfBXEHAiYRcnEIg_OeiUvoMAuMX9HkNiVprK-Pbni7oM2PPpHbFuIF7jGeANj4q7HkDJxW3JWHMsE0Jl296eygbsaWMd49AMb_buUiNVMvDV5Bl7M7MTH4lSxiWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb90mKWJXFvA4xEWsH01HhGg-PeCE01raLzOkZMHvvslXCsw9Zd_0U7TDN3m3HzRD7K-XBE7AoAd-q2dCO6EzvrySmUwmMER_DdiO0u1vej-i-JCWH1Rvt_OaXm_0AfEvTN1UCtheZfwHs-rc_CBnLx12D6V2MZ1vGfsBpnijBow3yzQSsg2v1G7222PmPW_4-Y4D05XXcIoeK25qZeF0g3yS7lDRytO4AozWmF2vjrr9kWb9NHF6DMm5u7X7EtGS8uDEmnwMTFlLk9igI55UlLT5uFT60GYS9VuBgBb2sFWMdLFods8H7mquw3IPMVXycg_ua-sFpASyG0uyh3T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfuWyn1M5jFRTUSCwNsvyezcHuR0O9RHfQcPeelVdmo4KghY8n2ljTVKELQfG0u2LUuIKYQny8TD8v8hYcW3b-ej8LyWYyG2THy4SlZcAv3adBp2OnQDHa3XH3-xUs8qIT3ZEaG8O4PZx7yHC4gXLFiJeR2Cxe341ICjnQidptcbJsNfj0ZQK9ewz82tOtQ4JGtorMH-MPzIEJcChUubD9Occj946fv9NpWAARpmLsdS5dnibpRtNW77jfNBlxejEF26qlgLp0Shlq02chpmMXFantwBHLkaDm6YgL12j3dVKLJfEgtIYnaot52BK5Xc7JlHwnnqOuJvn_wGs0FYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=Or81p-DT5kvgzuBSuIwzjoT0J2gV09-eBNOv71lVluGZgECu2mc_2cPeSSahuxpEAqj1Z8mFil5XgYP89_1RiJeTbhUdLRpgaOomtoU91Lhrfq_Mv6WenjPVqKigKKAG6ay6Zy7JVR2UTeEu0q7zBuIbDZiJ7IGyqvkSyzQ8yi00rNbaOAG84rPxCIY8rX3vlmVZlzrCp77nFWtbfnNMq3Fg7f1EM4xUvRMK132pqwifte-GPkwsi2WzSvEnWKH2LjpwpjRnVgzkATej0Cr5lG61kJVXkpRYYU3Dhc0SzGeu2XgBNMG9tkftlQDK7OvwfiX65a6rHKIf3WRJeMrncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=Or81p-DT5kvgzuBSuIwzjoT0J2gV09-eBNOv71lVluGZgECu2mc_2cPeSSahuxpEAqj1Z8mFil5XgYP89_1RiJeTbhUdLRpgaOomtoU91Lhrfq_Mv6WenjPVqKigKKAG6ay6Zy7JVR2UTeEu0q7zBuIbDZiJ7IGyqvkSyzQ8yi00rNbaOAG84rPxCIY8rX3vlmVZlzrCp77nFWtbfnNMq3Fg7f1EM4xUvRMK132pqwifte-GPkwsi2WzSvEnWKH2LjpwpjRnVgzkATej0Cr5lG61kJVXkpRYYU3Dhc0SzGeu2XgBNMG9tkftlQDK7OvwfiX65a6rHKIf3WRJeMrncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAbJui02NkUEP2akQAio_JyGseOgetZRhqKHgMDbhtAF7zi5SIAJ-NAT7cAAxKlSPoSGd9XOKVJFX3l_1ZfQAw4_8sFp_oXCSUjCMl8p5eIVbkkbraamUfdVE30aoihDrq1USHQ7MlC0pqbBmj0snlTlNCTBgL4cKKnzvNXJNJc0G2wKoWe2_VL1vODravD3ukMAWJQ7MCNDmAU1741ZagEUX44Zh0JRLtBH9VM7kYKw6hMfWPI-02Fw8NT3q3XSNcm3Bbu44RjqyzkB8li8QL41Lh2x1bvgr06OxPTfjq7pwTcItLCUTLlMYe6bl8waehbI9bTWT5gGxdcUJQCM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=FO7IeKhr5XL0eQ3-6kj-h6Jb1jGruz2rsVxOmDVauD0zL6pZpLNsOfcZlV3cMr6Z4YxeZ4BLQzqsuK9t8R_7odP610mlb0bq9IK-HXck6GtGeDyehwqGDZupzAn7tKDbDLTP71mEz1h-ZMUXSHHs9Tff-LLMoOwziu_A0dWHpZ1Hctw6-fZ6nVMNWwegEBXsgzm_OQKPtXrI-uunnW1wbhbMpUZGcMWoTV1ILWRluYJSnauv4IeZLzdK3aDsULYLf_cbCRqbu2AKaYMR1CnhLguBMsd3YxajiX1K4MhXud2fMCa2e-gxC6C0Znnu2UQRI1pAZHaEwmZlEZ8rSw20ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=FO7IeKhr5XL0eQ3-6kj-h6Jb1jGruz2rsVxOmDVauD0zL6pZpLNsOfcZlV3cMr6Z4YxeZ4BLQzqsuK9t8R_7odP610mlb0bq9IK-HXck6GtGeDyehwqGDZupzAn7tKDbDLTP71mEz1h-ZMUXSHHs9Tff-LLMoOwziu_A0dWHpZ1Hctw6-fZ6nVMNWwegEBXsgzm_OQKPtXrI-uunnW1wbhbMpUZGcMWoTV1ILWRluYJSnauv4IeZLzdK3aDsULYLf_cbCRqbu2AKaYMR1CnhLguBMsd3YxajiX1K4MhXud2fMCa2e-gxC6C0Znnu2UQRI1pAZHaEwmZlEZ8rSw20ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=C3dkqXmiigfjrGRR850nJw6AlomyFoDLd4SD_8rtUa7QqNXWHhH3c779bjsaQfcpm3AMCQ6J8ozV1AaIU1sTrr6dPpUH2v36ES9T9QEEdyXQNot3FyU9QmZ2o_A2WpRXpHrSmosZN2oU6PxVBjaIApbMPxg8FtLyS6wLLE2HDTGD4W7qc6k2v6azEwH7YiGqDeHpBSE4pExGHB0A3tjauaL2-mGK12x86YCaXc67RoOsYiMqzXK9VB8TuW5NZrhkLgBsX-mEr1Um4fbFPlGMWe1IK-sMAb_XOAtFO5Dy-hg21eCxROmWywEtsNP7wUpzqPDLXP6M55J-yUnhUAmySw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=C3dkqXmiigfjrGRR850nJw6AlomyFoDLd4SD_8rtUa7QqNXWHhH3c779bjsaQfcpm3AMCQ6J8ozV1AaIU1sTrr6dPpUH2v36ES9T9QEEdyXQNot3FyU9QmZ2o_A2WpRXpHrSmosZN2oU6PxVBjaIApbMPxg8FtLyS6wLLE2HDTGD4W7qc6k2v6azEwH7YiGqDeHpBSE4pExGHB0A3tjauaL2-mGK12x86YCaXc67RoOsYiMqzXK9VB8TuW5NZrhkLgBsX-mEr1Um4fbFPlGMWe1IK-sMAb_XOAtFO5Dy-hg21eCxROmWywEtsNP7wUpzqPDLXP6M55J-yUnhUAmySw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=J-8gCo8YOYOe0AYVwVVq_jKKAL-9RgdGUUOnC69khZfU61iGXXpSOj0FPVJHTc_vGhJIdMpw72dHl4wQwXaJ_Xma4Kpcb7J2iQRfyzFMECgnYIDgJh3VYRIJAEQnIy3VfOGpTf_sK8D0FI-QXJ-tSHLcFQSJniTkShCiT88rIOHH4mjRKRe5QbUdsLGvLpubYanlXu-5cACPXROh-w2oX47mIpLA4LlWj8G2rYKN4gaGiFPcoKNCK6cXiIyXVn_P-sy1YnFUbPSNKN0oKvT9heh8x-O2b_4yZ50wY8mQo0Anj8lAG4SNdSmI8vGSAbFZwyR2MtJ1YuZ0bv2XwQ3oxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=J-8gCo8YOYOe0AYVwVVq_jKKAL-9RgdGUUOnC69khZfU61iGXXpSOj0FPVJHTc_vGhJIdMpw72dHl4wQwXaJ_Xma4Kpcb7J2iQRfyzFMECgnYIDgJh3VYRIJAEQnIy3VfOGpTf_sK8D0FI-QXJ-tSHLcFQSJniTkShCiT88rIOHH4mjRKRe5QbUdsLGvLpubYanlXu-5cACPXROh-w2oX47mIpLA4LlWj8G2rYKN4gaGiFPcoKNCK6cXiIyXVn_P-sy1YnFUbPSNKN0oKvT9heh8x-O2b_4yZ50wY8mQo0Anj8lAG4SNdSmI8vGSAbFZwyR2MtJ1YuZ0bv2XwQ3oxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=iWHDHv3zmQ1LW7U3EBp23jd0GTH56IbF0P7NPjKS2XBxsLiT_MqjIBtFIKGvbySzTDE5Xny0dmCaGcUtWztfElL6E2IhIb-rBmCoXDIHR9j89aXLeSlO4fwxa5k_upbnWSXQu3LloL_szMaNeWXp2WfhpwGttrYp8ttOWPVJWyk5c3Q1H84GDfNOrP48GTE-fLN5uLoDPJHaMWEKL-MqQPqfQLhMFj0-a2eYMZ4H4nRGb0ZEYiRZc2DgHww6yYjKggrlLu5EGgbMNYwev8hVe9Ohm3LoYr0s222wU2jiQq1U_qENYa0Oza5q_0qTvceWAMjF0umQB79AUJkRskd5hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=iWHDHv3zmQ1LW7U3EBp23jd0GTH56IbF0P7NPjKS2XBxsLiT_MqjIBtFIKGvbySzTDE5Xny0dmCaGcUtWztfElL6E2IhIb-rBmCoXDIHR9j89aXLeSlO4fwxa5k_upbnWSXQu3LloL_szMaNeWXp2WfhpwGttrYp8ttOWPVJWyk5c3Q1H84GDfNOrP48GTE-fLN5uLoDPJHaMWEKL-MqQPqfQLhMFj0-a2eYMZ4H4nRGb0ZEYiRZc2DgHww6yYjKggrlLu5EGgbMNYwev8hVe9Ohm3LoYr0s222wU2jiQq1U_qENYa0Oza5q_0qTvceWAMjF0umQB79AUJkRskd5hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=VWQG6izZIdnqi4sMsOkI0xlXR1O-ViUM-WkTSc5mhg8Ul6Sg7HiFCPDGa9s5Tpn0bOwjo1slXeGov_PhyTnk49UfPJR9c8kSy1x4hKK3UClt4SBp95vRXSteqvlQD6Xp7HP5pNrjSTHm3iYC0Spbt0oE5x8T4jYu59FSf07653aL7TbVqGI7F1sVue9y8wcvkamqFVrNxgaGwBHMr4n-TT54mablYVrPBdvC1rMABmWUHX4D5eU1pJC5EP7Y4ARpkmIj4fUFQ5aK6BKcLlTfHyFNMRHx-HfYtaDOis92x4sGq2K2ddN6li3N2nOzmE_iLEUOR4fRuXPNK5ziY2Medg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=VWQG6izZIdnqi4sMsOkI0xlXR1O-ViUM-WkTSc5mhg8Ul6Sg7HiFCPDGa9s5Tpn0bOwjo1slXeGov_PhyTnk49UfPJR9c8kSy1x4hKK3UClt4SBp95vRXSteqvlQD6Xp7HP5pNrjSTHm3iYC0Spbt0oE5x8T4jYu59FSf07653aL7TbVqGI7F1sVue9y8wcvkamqFVrNxgaGwBHMr4n-TT54mablYVrPBdvC1rMABmWUHX4D5eU1pJC5EP7Y4ARpkmIj4fUFQ5aK6BKcLlTfHyFNMRHx-HfYtaDOis92x4sGq2K2ddN6li3N2nOzmE_iLEUOR4fRuXPNK5ziY2Medg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9I76Dx9TUrKrHfRnxBMZ4SqpOmv_DbInTk_kFNNLIbwpL88n8lkX3EFlB29elpfWuqe74B_4tEqK6Rd3i_HiW0pR7wGquHh-1ibvIRX7gT7j6EAWiHBTO2dToRqFbnpA7kdepAcc7F1HpH3Wpl3kieXglvMW21vRQCbRiahl4AWZIEayP6897TlxinqTW53GkoOiqN41dbeUfe_KvtodamU3gr1-K1lNvZb5uFSpfEjKTA95raUJiqN0ZBrzVXnRKAPt3p5KCYZ6ykq5kvLSBN2RBL9pj7WbvlKzYx1fQiuBUNnEcsyp0qj-VFG80_IG7rsQz2_LVGuZMWM_zU7jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIwjJ5o2g-Q6x925SPv9bCOg8mt42HqqSFsK91z0R4ni8E0fA_AIcIA5egUzaGU0K6-DMpDupIGPCHPz998O43b64RQUnEyBuFVaKrSzSKAlpkz5IMFw0sl93H6ydqk2SLmD_0YMKcCHB3B9jjsHZDTKHyYS5wZWl3jvYag9J7xSSH8HRHCyATbWJNQVBtlpJam9_Who5j0fXYxaCCXwPs6uzK76l4Ahvb_PkzBA8iZg-9mRA8B6nJ7dqK6yztC_hYBgcEzXtBMURN3QsLvIi6qqCavhjjP66ASDz8psmTF075aNcBcll6GASzuPKLNg7xGP_4IwZXuFKRwiTQmOOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcoV0ZGU9jcnrKhF9M6G2WUVvNXnqCSiunFvVsfdFadVnuACPBkq5oL7ot6HAEKISj9l1RNkBONCeN3WRWzsmvOzREggjuthDZvxa-MH9FOC-Z6LB_GFFWwkLlLSsM0mGfdX89EoCDOVW9zQGWO3R0eh45lYUV044X-8DryvtyKLv2jqD-BaJUO9Yq8nFwmfVhfPCBKfK8lG4khWFnD4ZvXaECaeb6Zozm0c-OIz5bRBNRXl8W8thi2knuVEzPoLkqBG5qYQef1xjk5zo67Bqp4zLFGzz5JTA25ZwGES2rl1mofDvNWt4Wa5A3obXg7mE1iVzGWeZkW2wQbzMoiLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXk8R-W4G8fUgZqAtsk21hD6UGFdM8vRY2gM8Vgy_DPYvzJv5mTsiU_zxkXLteLrMYBp0bet-9AW55giLWG8YVYXFLe5YWOqmNfweuiMS8qI3ZanRwq-CWEj73o-yhIwFK8qjq1OLMvn6ffVWdyk4PLW3QjflokZoa0fNgq4a3DU0EqOK3Y7OSFirxB0sLIxKmrm6WO7oZU0d70Wgnvg82myb9LPN_MqN3Yn9inZTia0Ck_mYfGu0_XpJhNHvmmFJLMSngd_11sCvNBtXoa3BOHskAbNNZ4cNWdYRC_eHGYdsI0rJP-triTJpROy3aaSVZ-fvg9x5rGmttKi9OfouA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=kBHdQH1wSqsb30kbZ_WsBKUFX_67RKrmIfCpWY3tiksKQVp9zmtI6eMnHVfoINAh87b1jnCxM5q6nh2LGeG1UHFoJevsCb8RrJ1iHW9b4qH1Ubf_u7G7Du-hchRswV610f6DqFqCoH6N8W6BLw7AGsp3GLUD1jF5KhcQKUjoGAGtuElO6-LgkVRPcTF2NCsbZ2RnGM3yRoaJ3buS0flQCukS19KHy4oTUZwHJhaas5e1CpVc1d2KuSyhkZfplDflrgpVrbrGBNlXTApBXe_rBl55XA-hIjLBPuKIbkP44qtDVQoM30Q8mZGDVVH4YoceBtmPiKshroBQASqqOyzkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=kBHdQH1wSqsb30kbZ_WsBKUFX_67RKrmIfCpWY3tiksKQVp9zmtI6eMnHVfoINAh87b1jnCxM5q6nh2LGeG1UHFoJevsCb8RrJ1iHW9b4qH1Ubf_u7G7Du-hchRswV610f6DqFqCoH6N8W6BLw7AGsp3GLUD1jF5KhcQKUjoGAGtuElO6-LgkVRPcTF2NCsbZ2RnGM3yRoaJ3buS0flQCukS19KHy4oTUZwHJhaas5e1CpVc1d2KuSyhkZfplDflrgpVrbrGBNlXTApBXe_rBl55XA-hIjLBPuKIbkP44qtDVQoM30Q8mZGDVVH4YoceBtmPiKshroBQASqqOyzkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=DkKg3GA_mC5giC0JIkT6e0EocIR4EyxYm5jiymhJK_d188-0_ZU42utWgZpjRu9nVsx-2GYiXSmWui4nbNGDSoAuzIorTYfzn--6lyhMCiikqhq0bNybVuShk6xjoy0kj2nKieT2qPlZ2dzM7ZvlBwiodulSjaedMDWsb_zbv-9Um05wxzK2F1m2UzZYOUUGtuphWSeDPxMySOxsZS3EuFGaVALjfMlxjVoZqHsQrFtKo4HohErglkCYTRlg8w5dgVJ2eOPXcmatHVs8AeF82gEJdWYR-6MJ07wJ7UrEwF4rbygcPTWTP60BerRG_nSEit5085FC24oW8By8KIYeig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=DkKg3GA_mC5giC0JIkT6e0EocIR4EyxYm5jiymhJK_d188-0_ZU42utWgZpjRu9nVsx-2GYiXSmWui4nbNGDSoAuzIorTYfzn--6lyhMCiikqhq0bNybVuShk6xjoy0kj2nKieT2qPlZ2dzM7ZvlBwiodulSjaedMDWsb_zbv-9Um05wxzK2F1m2UzZYOUUGtuphWSeDPxMySOxsZS3EuFGaVALjfMlxjVoZqHsQrFtKo4HohErglkCYTRlg8w5dgVJ2eOPXcmatHVs8AeF82gEJdWYR-6MJ07wJ7UrEwF4rbygcPTWTP60BerRG_nSEit5085FC24oW8By8KIYeig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=ccCSdD6Q_zmS6xn2iv6QqksrZxvvP6WycUsWAb8BOoLlI62_As5iBJmf63Q3vStWs_ZJlnCaTIkdPUA4TfTVqnuMDoNoQ4qk5R7jwGEIL8aoUkFcW07xpzd3yL7A9alLcohgI_0k8JYjzlTWhcp705NmM4ucHK7IdIIsrQK3bCMig4PYEYf26u2C2gyXxvbzMZIVEU4wBbJjU_suQe4ulswpHNzfrC-4ynw9qu2UTop00osAacoLJbsMeCHSt1j047ERO0ojVXgdIQ0jbV0VjU0jnxmmrgZQtV5hevrhJ2Inzi_Y7ZRsqoE1kh1qaOrTIkkigIg8ua6SGD85BEakfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=ccCSdD6Q_zmS6xn2iv6QqksrZxvvP6WycUsWAb8BOoLlI62_As5iBJmf63Q3vStWs_ZJlnCaTIkdPUA4TfTVqnuMDoNoQ4qk5R7jwGEIL8aoUkFcW07xpzd3yL7A9alLcohgI_0k8JYjzlTWhcp705NmM4ucHK7IdIIsrQK3bCMig4PYEYf26u2C2gyXxvbzMZIVEU4wBbJjU_suQe4ulswpHNzfrC-4ynw9qu2UTop00osAacoLJbsMeCHSt1j047ERO0ojVXgdIQ0jbV0VjU0jnxmmrgZQtV5hevrhJ2Inzi_Y7ZRsqoE1kh1qaOrTIkkigIg8ua6SGD85BEakfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVLJQK9nMCOMjsJJOSlYdIvyxe1zz0YBqOouyORYBY2DWgys3pSXUyiN0QJulB1C41DgZaiJB9BS8Ioc33ROs6LT0y_dgPIc20mXMXgugUohN8iYu1ORjr4EdgcE8kwCBoy3i9VAlA1OIDR7m6QpesvOAhF4toguLZFKvpOcPfBK1L3LkfEsv-M7vrAfAcmr1MPyzyCJjW77x5Li9z9M01fVnPsnmtcCCDPpQ3jj8fsEIsz9ow4D9T-kwEyGC3K2CwG57vyQq0hiZNoaKjELebIYYngklGoqqDJzMchgziKTNQ5SCVUedzT51thF4DFW7O9IAqPo05QVdDcTfqxJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=QAQXO3I0PNb3-hdl_fQ0kC5g7zphC0Udn2h-23Nx7-tOJQnOBuV8d2qJHq2PAEtpdFqWb6-rM9-20CKOHGA3GhFMjf6kYvR65ha1_2iWe6iqNzVI3iiKrbX3lVdhRU78Gl2e4hPVdC0piIASRf0uTeIkO6JHzXO3kO6fzfx40-GG3CXAy4nLKPD7kms0njq_2ZsQtSGAGHbGPnbxDV_LEOko2t75ihyyARSqhhmfsZ72p6lztTaOfvlfIzwH4MVoEr8v1Q4iwXXEOwYOPPoHecAGoWLo71SFzJd1tRFOd9PRyWOdUvY1-sHMivsXtxQ7lakl7Uh0-i6xujwBoDiwyqGqpWZHrJ0xsiS4SvCEQvewuNFsGajl3B0mrPFPXYTQW1R88xtjAA_79kJPTMvN4lj9D7QUltkJ8uJMUhFYGzkgX3EeiGKe9rDAAkuJwPtmS6T5Hk5fvJLKh1Ke2-5GIih4KORVXD_lQ92mm9EDexhCHdKjnm6T7TbtOVnzR640x6gVufgeSKzD0c4YPZVxloHk5q6bxs5sh0blUN3InGxMlNgtxpKDUDByDJF5rEdWX6HJ5wmUbHgVjueNrOjaA49bmgHJpsY_2rBPLqO5T9c9Jr8PDNcTExm29ESlk26nnwIn0eL3rWxESQcivyBMz4dagm9Bm3QNY3Lr4Odc9kI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=QAQXO3I0PNb3-hdl_fQ0kC5g7zphC0Udn2h-23Nx7-tOJQnOBuV8d2qJHq2PAEtpdFqWb6-rM9-20CKOHGA3GhFMjf6kYvR65ha1_2iWe6iqNzVI3iiKrbX3lVdhRU78Gl2e4hPVdC0piIASRf0uTeIkO6JHzXO3kO6fzfx40-GG3CXAy4nLKPD7kms0njq_2ZsQtSGAGHbGPnbxDV_LEOko2t75ihyyARSqhhmfsZ72p6lztTaOfvlfIzwH4MVoEr8v1Q4iwXXEOwYOPPoHecAGoWLo71SFzJd1tRFOd9PRyWOdUvY1-sHMivsXtxQ7lakl7Uh0-i6xujwBoDiwyqGqpWZHrJ0xsiS4SvCEQvewuNFsGajl3B0mrPFPXYTQW1R88xtjAA_79kJPTMvN4lj9D7QUltkJ8uJMUhFYGzkgX3EeiGKe9rDAAkuJwPtmS6T5Hk5fvJLKh1Ke2-5GIih4KORVXD_lQ92mm9EDexhCHdKjnm6T7TbtOVnzR640x6gVufgeSKzD0c4YPZVxloHk5q6bxs5sh0blUN3InGxMlNgtxpKDUDByDJF5rEdWX6HJ5wmUbHgVjueNrOjaA49bmgHJpsY_2rBPLqO5T9c9Jr8PDNcTExm29ESlk26nnwIn0eL3rWxESQcivyBMz4dagm9Bm3QNY3Lr4Odc9kI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By6a8XN8d5WPkjoAnY57QC5vqeW4Czbnzktq-_WpjCXVHRBwDByJf8Jlc8IDIbTE-7c3ERK5slc-afBmv2njrD2eVyLymUE1l84JcX5NLanlEZmcZzsu-AXrCGZtCtBgo4mZF1vvH8yqxF0JsLQMW0a8vEo4815GEc_ySO4Q6aE4xocOpc1zuHuj6DQGik4mFp3IPTy_fuMqzEUikl4ub9PIazgToLiFNtslrVil3Nx-pEDeKEck1OW5A8uqUFScvp2BVgqqJcrMzwJCpTEWomwSTK2e5-0R6IKBxTpjASqD5IaLIauFi7-VSsBVNBGwtTN-2u6Lc1qv5B5R_UIGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=lBU-9-U4zLJWwo-5OPs7B0IDemzojGlDA3wgBeSMJvForgLfhnPr_B82Br_cRu0JvuG6UcdHKgUuEqyWl6qP07EKCgRplREsq3byknmqHMp4H4-LB7Vlj-B4ceCpZyM0F-qNS9spkL0B_7TgozKZZKRCEPafLkUIN_T0C7w5tdzR0zdmdTYdbAuCwwj59xJCJoPgOkMJ4JV4_sR7dKj7--TbrwcuUUFMBO7oALEEGtLHFZafGL7ybhby6mbhe5PYzvZJMjuygj0Gy1yZ8LAj2mnsouHbZptY0_nyBzZO7qkPov37KJZ8yTXhdKlC8mAr1mUX6COVpOWSyiT8duen2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=lBU-9-U4zLJWwo-5OPs7B0IDemzojGlDA3wgBeSMJvForgLfhnPr_B82Br_cRu0JvuG6UcdHKgUuEqyWl6qP07EKCgRplREsq3byknmqHMp4H4-LB7Vlj-B4ceCpZyM0F-qNS9spkL0B_7TgozKZZKRCEPafLkUIN_T0C7w5tdzR0zdmdTYdbAuCwwj59xJCJoPgOkMJ4JV4_sR7dKj7--TbrwcuUUFMBO7oALEEGtLHFZafGL7ybhby6mbhe5PYzvZJMjuygj0Gy1yZ8LAj2mnsouHbZptY0_nyBzZO7qkPov37KJZ8yTXhdKlC8mAr1mUX6COVpOWSyiT8duen2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr8O6SO1I1R2LuUgPYxlssrRt_HwqpLBUgUg1iDB2ft_2PYd-vA5KGIemDY7IRR5VSDD8ptpRDwNZY3JOIyGiDDv6gmxkUbTl2T9miprdaBfTqgYU5IuHf4VtvG0Sf47WTYIYg_Wqwun4cvU8teD02URr0ViaT7kUBXIVbHm6kpVy9Ap5vw1eLYtmP3ny21FoG_xUp-ksJm30CdOyajJtR0fItvyzNJIJounPoaHwEVEW73PX6Qfyj9RLezyrTY6TvyHKsryQveu420AtrS232zI4BtDhUT5FQtIrB0oXs_IHja7tbhykzTGkx4vJGPosHycGOW99Xbv1jR4_Tm7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-bk1_-9b1EDTbJYPfyNg_SdAMgXQTCwaI0jPCd_c0J1ez7fZnMTRKyJwWocFSPcv2QfI34kg9XKMQzkTL098rNGQpJAE_9EnFvg7SkwoU8-auv03kelSVhMJe5FhmkCoKih_VOfwgCd5O3tpEc-u8MzXrEhH55q_BsEThwirlJh2slq05FaZT5fYtpbXs0QdxdtUujXTzhYRAo4Is7QQGXmHGAcDWoNfHZNSdQURVzLLNVfUgugS-vDUa22qWw0Ng8BhX9jPi1MzyJb2Ef2PDE2qM0Pk-byLdSCqw1PdeyJdCzfDe04iAHGexrUF8IjzaKFol2h8hj4NXEW4cPCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5kLZOfOAmPPb9RjS6rExVxY0iv98Z1tfJjLLw-eM39M8HcwTLvT-P38nxwtZFzKcrvkqOAWlxThfCCBsXAw_SjPPI9__NGQF7-M7WLl75PsU_IPE6tqzCXUdhAO2uepthMWyUp31ensOBXqZ0iSM2O4lvWd8gIV_mXFacHJ1zt23gr4x3Y-fIYL0maeibz2rMGYL74G3BPgyA9JHU4T6sky_cwm_ib5piJoY7WPpNkXMoAdLnl7CciPTaW24yYTM5O2kuNFr-bf-qe5heGwbCLWRQdj8J1NOf1yJsYUDY3SY1fX55S1bVl5PM5gsCYMedm8_I6bZ8NElNzseaZ2mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEvcSb8dDLyJWP58u9gHHulWWrpZP8A6QXe6obCgQcOgrHOyp5mFXc8WcOmM-AqWhzSIY3YXYhNuyT6Dl6kaD_RfBKPep9TlsDcGsBZriiWIJkKT5MM5hrRtaaN_0-X_wR7LnCr7agej_HdVpBdgenuHK3N0zyrO14AoP0iGbPU5tHXzOygS4ODoqxq6baHkcV8eCu7RHHYzuJlbxuCF_OLdLlEKiZR3EsvLvMiR8f6XL5yLZfeHmyHFYu97Osox3MTxZ_NjcmNNLFu9y_Vln51_F2ZFipGPQhDlc5d-gEDS6Jup_wLOY5zumNLpA9P8Fc1RqLX_EHBj1e3jIb0rOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkJzVP2PbWKTJfz9N1Doen53ZY1tvhz6h3GUjhaR3ypFbRx4qOnbXWSfBwppbYwwTubZ1LPXmVGeiq-QvVy1W_IY7UO6REkxEsOPi-E0V7t8mTob0lI7iIKy6yAWDO6UxzUi_VSvoh9BRh7CKOEggC1pK0rpkzMHiB4XyA_tnNlvkLyS42BodY2bjIFKN-DYOrOzkSEGQsn_hsm7J_v3uYp-7Bx7Q2KUD2qNE8hyQj2X2kZATo8KS8x8oTY-FRhuI_Eb9VUNb1aL7yoC2BVly7KQuL_8qfKfl_UagwZ2F7TF6D6oAg20ryF1CFDoirZn3FugtWbTiE2VqNUxOB3EIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4NXmAtEmmDugh6Pf23_ttgXEVW0rpRST36_XfYycX_JAIt-HCUyMF-uPCT-QPIBUsYa-NGYnrUKzaIKqsAm-YzkFDWPwW-JSeEuHY4LgF5ZJV7N9Gb3-fH8NmV6jeg0sUuGHNm9vkenW21koYVxHyD6dA3QCQshqWXnq2ZsB6FW9syVCtWOgIJNZigAlX58x-W-ZGNck7M7e3qoc3xnrpiRiuFotFvZO2OfQt9RLkJhGRwgN8dhPbcNr46m1vVg4NuZ42URQq5okoGsWvZafQVIOstr8SvToNZANLxat3MSRl6chGbnbZPRDy3VYvbinqVS0K1LbIRLHVwyWU1AMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUQaWdGT57Bzi0rHzKflYQku6r04NFAUhrVug7y2q9yiXeBAyAiFs7J2JUZmWGgi_LrqfjrEDK0DJwNZvvl9OVe0ebHc00rGVivrduiIgH4Hmh-5ixRp8_l7ozOwzSkBA1EnI5LzMwLCg4r-rWv1BhT2m0gj0ngQJj84oO2_rl7-RRDK8_mQ-zQiVhO_JCIyuOfr_-f2KYdNSi5qNJwbiuzH7Vb9FGIYkfVWRqJeJh_HfjggAePM-DijJTrWuZ5S9iwO-C_CysOELUKAO-T5faEal9S0kB72ZSPLerocayc452CWvJl3_p2FnBx-TJ1zKNozNRCkXg3mVapYvdcU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=q2m1wGd-qzxZ9OJe6WqI7SpbKBPnGD4t3pdzXemuNLcPkVvDLF6z5pqOZCuj4xffFeRbctKWdjBPyMN-KT72aWzE0TbFqxiLzWDJoGiQrSCk82CorvAwMPF_eGgr9Vvg3ioh6Riv-MbSsHOyXt9wkNFoV8mLWEZbIWuFXK9N2ZXjYlSPvlEG19VJ1ABueyz45en7RposjwuOUAvPdW8HWDUF9J_ojZIlkxdYYvIPBbvaQL00Y7u6qNw5uVhD-cVeubMS972xsE8MpLKl7xuC0E4Su9Fw3b4zGBBd4jK4J_5GbzreFmnHhfZ3gKDGCzsDBn-RPhXQ5ppskW-q3XpJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=q2m1wGd-qzxZ9OJe6WqI7SpbKBPnGD4t3pdzXemuNLcPkVvDLF6z5pqOZCuj4xffFeRbctKWdjBPyMN-KT72aWzE0TbFqxiLzWDJoGiQrSCk82CorvAwMPF_eGgr9Vvg3ioh6Riv-MbSsHOyXt9wkNFoV8mLWEZbIWuFXK9N2ZXjYlSPvlEG19VJ1ABueyz45en7RposjwuOUAvPdW8HWDUF9J_ojZIlkxdYYvIPBbvaQL00Y7u6qNw5uVhD-cVeubMS972xsE8MpLKl7xuC0E4Su9Fw3b4zGBBd4jK4J_5GbzreFmnHhfZ3gKDGCzsDBn-RPhXQ5ppskW-q3XpJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe1daTQprcBLcdBehNNROBKonoPlRq_w-kHhe9798mlGe9CNcvu0ggg_LM5P2Bwh5-owfZNZqTL8kNhtWm5f2mEe7t8eMcFm6F3RCHlUQpllpalCkze7JYeOj3Lr8E_oVjTTB3vfP39k4UCaGrusQk5tH_zF0qEZYo3k4p90s5jqoso9cdYoDNKeLp-RjKtGxNZL2NmXZUZBG9-mChqQgU3B--wJJ5W4w6Rnj25l_0EYihdno_T0Fa_e1RLGFiNKKJEFHEUf2OdDgBTxPu9oYwojqJQa8tvsKfiGSMLWV0WPDkoTTYnrrov95Zswjdq0GavXN3QvxIsP14GmkpIwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWFJnBFdrJPeEA1gS3FO4wv4gDnuU1yGIxX56yjtKFv6ybvIx3THpr9dDRq89QnjNML6mQqI72Ub-dBMGLLxPBOKHT3ddqj4DLFUKCGVMJXTg3gpTWsi5DJX-0kvzwoNXf21mG6NCJWFjpzjUA1ik0X3vLaXedr-awUhOsCDc9qp3feZBrOujYI7tul1u5k413llBVjURhRcwkAs4GqIIzDz5qPSlCFonjNKRRc1bCWZsnFDJclqMUjYzllheqfgj_ruMmQabb8JFfVgqIKmQCkDTK4TIhLaXc8HG2IdAHoSzRJUvwOmQJD_jnoFFIo_-7eet5ATF6kPNUGnW46D4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=cx6-MotcllCrlDH8472sW5q9jGqKjFJL1efqqcVNhlPGRzS570--_HpHF-czqtcZAN2wC7pnZyTrBGFbItFvPPSMjSyPWhzH1h6WqCH_DLluY_u3MUE5IcBCHk1thTkduW3MzIIumWaX_oSEmuHvm1q2KoBT4oulreAa5yjSHMX1ySu3n8-iZX60QDyQCaX5a53oHbTZ-6UtYoTLSH0sGBOh5pNW2qdEdb0-nQB1iHIEzZiibXm100tfOHoqt_YhBAT6AsER2Wr_4QI0XoNqa1kbzgHkRJIN2XXRRi6Y1ylTtZqwxwTlSgOU6Qs8uOzOI-K7ht4D6Z-wFikWogl8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=cx6-MotcllCrlDH8472sW5q9jGqKjFJL1efqqcVNhlPGRzS570--_HpHF-czqtcZAN2wC7pnZyTrBGFbItFvPPSMjSyPWhzH1h6WqCH_DLluY_u3MUE5IcBCHk1thTkduW3MzIIumWaX_oSEmuHvm1q2KoBT4oulreAa5yjSHMX1ySu3n8-iZX60QDyQCaX5a53oHbTZ-6UtYoTLSH0sGBOh5pNW2qdEdb0-nQB1iHIEzZiibXm100tfOHoqt_YhBAT6AsER2Wr_4QI0XoNqa1kbzgHkRJIN2XXRRi6Y1ylTtZqwxwTlSgOU6Qs8uOzOI-K7ht4D6Z-wFikWogl8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=OenGGZhDuNM7sTNrp2rWM6x9EMSowVNjTUQE1Cq21ywuDYYpzsOtCeVsiuoDV4a1GlbJmoAVA0GQeIkq3DCc5bM5JwZzXvwW6-2oI1J4AE6526C7I4BX2IcbM5y6kbVvr4SWhKfuqgm1Jpq0JdxmkF116-nT3Xm4pl2nJkMOguWXtLfXaeqs0vXOwpCvES5xJ-aOIbOo8LGqWlivbKTV4fB02mo1YrLlmSDF7X_zrcLhrzezr-mqsbtRrdtPCdmtbCzYcnLRMdh_b7q3JCORqWGOzZmaf2QEle6OvY3_cbJQkwjZWmenA5V6fAwYzjrhYUvPR25wUEuHqaokAvBBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=OenGGZhDuNM7sTNrp2rWM6x9EMSowVNjTUQE1Cq21ywuDYYpzsOtCeVsiuoDV4a1GlbJmoAVA0GQeIkq3DCc5bM5JwZzXvwW6-2oI1J4AE6526C7I4BX2IcbM5y6kbVvr4SWhKfuqgm1Jpq0JdxmkF116-nT3Xm4pl2nJkMOguWXtLfXaeqs0vXOwpCvES5xJ-aOIbOo8LGqWlivbKTV4fB02mo1YrLlmSDF7X_zrcLhrzezr-mqsbtRrdtPCdmtbCzYcnLRMdh_b7q3JCORqWGOzZmaf2QEle6OvY3_cbJQkwjZWmenA5V6fAwYzjrhYUvPR25wUEuHqaokAvBBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulzDRiR7y2oOc2IzG0UdrMCm8LoPvXXArKWvWjbubSCZYdm6stFbQrKyJrr6gIedfH9pWN6PLJEHdRKcouBe-TsUi7ODy0CjGV-rihDVcgeg4BYvjXXkIDyVUA8p9BXf4mF4Al1GU60mgcxP5kYCpRWpXgfOBEtzcH5HIP2GImBDUBXSwMwxTwfkge0oMbGgXo_Fe_AA34a9_SYebPFMUtQqVDQLQiFeW67xRJHqV_FGcg5jqDOOb8zU8osbXG4UM4YlgeH5xTc6C-XcYnjeyu-lx_68hPHeNXZbTu4qXuwOD0QAk-RoE_s8TAAwudJMtreCpBOUd8DrTBOjCljGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=dpOokyQc0aPuM5vFeT-fnPvT-w5h7fis1WbXTzlPcY6XYL-0bZAYDn3dlCIBhv-25zEEqQ1XNR6yoJpedNXzV9eY4vBF1jpBYXlPtsi1EOuQNYhIPIfB353LiEOyvmdHXHHORJpV50aGtwV6pNIdTpnzXSibPgs7zbQbFQMca2aLp32aRH08MKf_3kbIr4-2WwTl4etP7yG6YCnoVbu8jk1-KdBdTgsC8FyP4edW4G9Gb9Qz26cUfLERlv6sgiYbClPOVVFgjDbEgaOnt89FbP_oWrrs5XwdJ_SAW3QQg8q0WWRh8z6Y5BtAWmTO5cjwVmjCvC-6kU_8PJjLVO3IjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=dpOokyQc0aPuM5vFeT-fnPvT-w5h7fis1WbXTzlPcY6XYL-0bZAYDn3dlCIBhv-25zEEqQ1XNR6yoJpedNXzV9eY4vBF1jpBYXlPtsi1EOuQNYhIPIfB353LiEOyvmdHXHHORJpV50aGtwV6pNIdTpnzXSibPgs7zbQbFQMca2aLp32aRH08MKf_3kbIr4-2WwTl4etP7yG6YCnoVbu8jk1-KdBdTgsC8FyP4edW4G9Gb9Qz26cUfLERlv6sgiYbClPOVVFgjDbEgaOnt89FbP_oWrrs5XwdJ_SAW3QQg8q0WWRh8z6Y5BtAWmTO5cjwVmjCvC-6kU_8PJjLVO3IjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=EdhGAbQPY19b9WfCSjvkCq2e00oix_oSkciPC3e2EYdMYpaDLwUM_VcFAtOjApYXsjXSpxNlYtJhtfRd4b_rqfDFy9gceJYE4-fWYaa22EO_9vjysBSzRax036jCM1LSvU71VT1c_ia2cJtdSzxCkEFdBiT_df8cMnU7-HIukIqtZ2TKMU8Ntf2Xmi-cD2Gan84oEJ6DUR0SY2AhtAz4_ZsedSmXE-Mnile7XVvxtNB5RLcW_jNcFl2cxyunjaxXneNiwQkN60c_CrjvWWJ68Xdi9TRd8fkbYVsHju5SvuthBRVWENTtgDTn5hXmksAHx30ActxUuv1m6Pujxcypdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=EdhGAbQPY19b9WfCSjvkCq2e00oix_oSkciPC3e2EYdMYpaDLwUM_VcFAtOjApYXsjXSpxNlYtJhtfRd4b_rqfDFy9gceJYE4-fWYaa22EO_9vjysBSzRax036jCM1LSvU71VT1c_ia2cJtdSzxCkEFdBiT_df8cMnU7-HIukIqtZ2TKMU8Ntf2Xmi-cD2Gan84oEJ6DUR0SY2AhtAz4_ZsedSmXE-Mnile7XVvxtNB5RLcW_jNcFl2cxyunjaxXneNiwQkN60c_CrjvWWJ68Xdi9TRd8fkbYVsHju5SvuthBRVWENTtgDTn5hXmksAHx30ActxUuv1m6Pujxcypdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpntBovu8mk179PkRoJB5_02ONrsaJyZmCVSSBlzcSzK5za0qXUZ1vlXUzWSn3BWMz8w7tJzkbdiIY2EXcQpaYITtmiTuhktqh4TBmYwmejUlK4c6PMjqxr6Qc7lpwk_-5FdsmzYLo6_B2xQBZ1ibvcz5aPk_4PC4V6DaI-00INEV7jAQ8gjgUHnjp5HI335EgYJ3zsAHs03S4NjbMytTG-zqQ-eULepHahF-j20b3edhmIA8S9fh6xn8GaPEGlSbgBVdytj6vx8Xt8-JU4GKi9AvRHSBirVogKbdVTDJNc0PJZyWuU9XB2ELcObMhdWjbEr-WDtrUr_qen5nLOWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CurhCqwY9xhgdZYpsagCt17FGLFVJ18jw4NIQcbmnIBLanXFbDTh0fW7u2mrW4fKqUe4W9Q9l40BE0D2MgCb1VLAycwVHwItT7NTOaEfqHKt9-1P59RO6jzGm7irwFz45-GsOI0LXncvizMN74rWmGURdzjUFT11-X74V4Yw_JJtmsv2BlmnwA0rtyHkT_HJm7BEuPoVjzdVxhindt_47kMMajlieorAwoEpKmwJlK6kZWdPkNGT0rcqULsYL5Gm4Kb03-uLZkZlVl30MgHTaG_V3lb8EPEN55PuHiuvoA6aKJZu7h78A9giaTVBaANAhqVG_FPNEscVo1jYJDQTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsk952JoMWqmam_R8pd4ZqgEvQYXffJYbmv4kz9q9dD5Sx-oQ2bg-BZdmUxeykJNQ3g3wc4LgaWGRcxmS3keAtABjFeAAxq0AP3fBYG2ItdyyflkMZ687eg-rSeqJ12ssQmhxHcLVBRXgS9G1H-NN54t9rimaR6XhoCoLHJlBpkzy3utflteXttFsPDNP9Yi_8kcZZ1jKzZIM-8e6XWtrR5uI8gZ9OnulS6cN4agp2JfY8FE2YyjWjjE03c52r5mnYf66m2oRmJvcgrTgbaGP4bnn7llHt78H-iVfibYeVCR_xfK0ynzdjDJgREaOWnjPClPWcf6lUL5jjvtVLdprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_4KNvqSkiqyVBRnqip-CLBaR8fQoUlzPuur1eJVDcovMPdlY2BwjbTOcu4-pajwctic1obBcVsocJCSpj7aHFgXKhYgZVYzkhOVkXkMP3gkjqtJ7uyocOVL5BV1sxgdpD8mjINf0-FDfyAJqWK4Cp7_3y-Ekm5ePzEhUaGRGt9gFOMzb3C4JFdkGWFts9oN4N-UjcPU-ZRBbBtTYvfUHxqf7VqeQ9Q__NoPLGAqBoA1CIhLddw09UA144XTO7htJ9n8ZwwI1gMxv5tOR0YUTG3_zbxE_4ac7hAH77ldgccfDkUa-nHVueXY3WpeHnLcG5NPMnXgO6q0z5kNbnrTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=JNtN5txDEHvSJ0aLu5883bs1xztcJu4oUj7kGiGBYc8FaZw5fmOndQTjOEe74gyfBHoMTi4xl2dyvjS5JFVY8qY0AFsX9M0vAgRYQmrU2KyCww6Xn3snf3TZCZ-D2i6aLyLxwGmzuzNBpFjHTHClhXIJpjI_4JugX_bK0vSey29EWEltY8Pw9fTrfd2cbQ8HEboFf6pWzs7dSCV2khojUIBvp65FZJ6LrRfsf6q_O4dng7P7cmhgavKglHbGmzHrd_RX38H8GP7cK5espyG3tOI0ZPpJ5tAD3oSsfXsxZ_XED3v12WScp27bl9ypkXVmCCyGBQ2EXF171AwmWSmUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=JNtN5txDEHvSJ0aLu5883bs1xztcJu4oUj7kGiGBYc8FaZw5fmOndQTjOEe74gyfBHoMTi4xl2dyvjS5JFVY8qY0AFsX9M0vAgRYQmrU2KyCww6Xn3snf3TZCZ-D2i6aLyLxwGmzuzNBpFjHTHClhXIJpjI_4JugX_bK0vSey29EWEltY8Pw9fTrfd2cbQ8HEboFf6pWzs7dSCV2khojUIBvp65FZJ6LrRfsf6q_O4dng7P7cmhgavKglHbGmzHrd_RX38H8GP7cK5espyG3tOI0ZPpJ5tAD3oSsfXsxZ_XED3v12WScp27bl9ypkXVmCCyGBQ2EXF171AwmWSmUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajDGudSJz68TjaLrxVQgleI0GveVDBbVwTx-3Bg8an_2PXpWjJMqpiMphDkrW1BI_dHtXLBYocf5ojI8bMa46k6AXm0qKkn9XaAAVgcx93NyhF_QTOhyg2-W0dQFKf3W2ZWq2irYpN85sBQWacg6oq4tVeR--iSgfQJn-9t6cY-exAvNxujHUbMC7W63UIq5_yJEheKxL0E776o3026xmheuNemMnO1NLc6vc7B0MXcd4VkHYZph6DoM6KR-gyRA78vvtxhslExLiYLkB5IckUKwLptI49MnCM3UiYztT0FmMhyg7ctck9ZhiWUQNziNQDCN_XezT-XEN0d8JbJuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIGu3d2_ZTn4m-cQqnxDXWF-B-GutwkjH8LDeYxLyZidbQ3kr0CZ35pn2N71nCjFg5pcuv6vrORh4wYWlUjch1XYMHvMjFI_OaJvD3351Ru8uCEPKcxxsMZb5RR8xybRZsAmVpz551W0yojYQnBFcEMQAf5nOFIiF9Ct1H5EOXJGchy5t72UldYmE99Vv6r698UhfelzQO_RP3n7mg5Bx1x8b37sQdmhi-p0bDP1qAlUcZWVEFoTHlFG8if-fAqw48_y32T5R-0PqczdDzIYGslbRGA5EXX1zThFExlMqNy5xDDxzwL968yaWuKBwGR1uUauNNKPXAnWj6cSRxiwDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eppX1SWfGkDnS8r9mFfCFWnOnrhTxtsjiDBl0PR04yldJTHdLkhwvTLL5Zv9NcL-e_3Sxv3IliiIgaCvZLTBPmxt_NC7wFEML_NHdkLGEPqH0vzzgkMrGFbgJ0OyxQA4vwZ4MrSRIC6cep8MGgdlyGHONknsMWW0Gj2vG0wPYsAjtk_AcBY_PLHLnWE-arur6GoMzF87Hx16baL0IeAj6K1MyzaIM3M0bsF3kDcv3OM90CNH6ThTCHqLdvFsh9KsVd1dFZmhQpcajE3eBKiAs9aUY9Dg4S9C_L8iseTwtaL-Blji12LBg6PK_i3gemCoOa91KbYIXaxHgeylbv0C1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=scRjhJSb1qa10VkqciW0paTbrYdSAdOBZQIh6XDtxhQviJaGIC_nXTSx1YGhm3HYkPMztF0JdBQbfnoGohF6sySCNk0X8a-SooKcW2Fv_kGnxfjAyP74sopjQp5IF0LhKsbL0co32xxDE1OKMG6i7THu4XhzO2Iw9TM9LgrW8qSLAAwtUIE5hc7tPKVinhYXbBVcA5rWvB3hYjLtJMNtkreU8U_LhqIQP9STKNVLmPzLU74ISAJIBJVRLwwhZugfIIOSMWz57lFOoB0fw--SZHlsoare5hDpYjkxwiUHHqO2lVxrs3URDqyn9hXR-C7DSt58yD80C3Nln8AmC0fy9iQc_P5EexFBBZgYLbcxKMguGWg81S5e5NqoIx2S_lFr6QwE5Uz2r467IhvINdMOm3e9gskhTYOtObivFfZrjPuCYXklGi3VDQPJ8xnBFkxVaxV2OrCMicWk6IXiEkhOhskV9xQPjKhf4Jh0_qAaJ-mm_D2bGHOUXl6Oz0oCTb99lL9IhK9MFUXS8g2rkaPEsYw9odGaK1khBheK28dd3tBUIvsBgbVReLWk9xWa4Lv4GzRbt5_gAoyEw06gzpJcjJ-q_bOdolnluGnkNPsq_TZiEk74NCDrAuwMkLUAkWpFix4ATJLOx0mla06c8iM9ZHLUKXzw7qibC-m3VYJb6V4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=scRjhJSb1qa10VkqciW0paTbrYdSAdOBZQIh6XDtxhQviJaGIC_nXTSx1YGhm3HYkPMztF0JdBQbfnoGohF6sySCNk0X8a-SooKcW2Fv_kGnxfjAyP74sopjQp5IF0LhKsbL0co32xxDE1OKMG6i7THu4XhzO2Iw9TM9LgrW8qSLAAwtUIE5hc7tPKVinhYXbBVcA5rWvB3hYjLtJMNtkreU8U_LhqIQP9STKNVLmPzLU74ISAJIBJVRLwwhZugfIIOSMWz57lFOoB0fw--SZHlsoare5hDpYjkxwiUHHqO2lVxrs3URDqyn9hXR-C7DSt58yD80C3Nln8AmC0fy9iQc_P5EexFBBZgYLbcxKMguGWg81S5e5NqoIx2S_lFr6QwE5Uz2r467IhvINdMOm3e9gskhTYOtObivFfZrjPuCYXklGi3VDQPJ8xnBFkxVaxV2OrCMicWk6IXiEkhOhskV9xQPjKhf4Jh0_qAaJ-mm_D2bGHOUXl6Oz0oCTb99lL9IhK9MFUXS8g2rkaPEsYw9odGaK1khBheK28dd3tBUIvsBgbVReLWk9xWa4Lv4GzRbt5_gAoyEw06gzpJcjJ-q_bOdolnluGnkNPsq_TZiEk74NCDrAuwMkLUAkWpFix4ATJLOx0mla06c8iM9ZHLUKXzw7qibC-m3VYJb6V4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hOl4a5iLu2nJh0hxrp9qm8L1TLeO6rkelEJjvD29VnpLyR3SAjFJlk8ll_ZuD3IUIdEvskuaCix7VurEXuwfIT0xIP8E5gQMCSi575gjp2IaxpcVkNQZZNkt5ylrJJFXbjZ_5QkdFg-zs85BXwpsOGm3elmI-tG681jKI6LpIgNQJVCR9LX2LnQs-UwZ1qsfSuqte_g9A9nVr7Q7iWo-Tcy9aBh3Ld43UR-wc5qfZxoGezhmbXIczTlJeAheYZCseupdwrFHDSuXSoh2xLnChFPs6yww9tW0Jbf_5HrSTrQQMZMbieRgK4qhaFAqjG7mmwrtWbhGEcJJor4Dm291hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hOl4a5iLu2nJh0hxrp9qm8L1TLeO6rkelEJjvD29VnpLyR3SAjFJlk8ll_ZuD3IUIdEvskuaCix7VurEXuwfIT0xIP8E5gQMCSi575gjp2IaxpcVkNQZZNkt5ylrJJFXbjZ_5QkdFg-zs85BXwpsOGm3elmI-tG681jKI6LpIgNQJVCR9LX2LnQs-UwZ1qsfSuqte_g9A9nVr7Q7iWo-Tcy9aBh3Ld43UR-wc5qfZxoGezhmbXIczTlJeAheYZCseupdwrFHDSuXSoh2xLnChFPs6yww9tW0Jbf_5HrSTrQQMZMbieRgK4qhaFAqjG7mmwrtWbhGEcJJor4Dm291hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=pQh4eP2elHXJ-Ruwbf4tO_K01w9U0TgdgC4nBxv-P-rDVExTDabqI0Dxgc6Ttq5sU2QI7IJgDXAFV4H4cfFIFodVAYRiNxUSiK6E05p-BETPgR4dbcYyn_JlvjHAk8xf5QRvGz8tW8BCVVfqta2eAvgpTUe8nnrcVOLOFK_pxp4lt9WBd_yg3XzLtq3hSsp7d8BqD1t5Tf8naO3tGG3Xm__9U7zzFoKsjtZvarnKx1Xilx-ohri9k1JNK9nerTwP07lt07IMARTaACMryft9s57Z05eiPFt_eeOcjw39wApeo-4gY6BRa9yuHW-upE58YzzPNUi7q2tYf1KIyYvLOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=pQh4eP2elHXJ-Ruwbf4tO_K01w9U0TgdgC4nBxv-P-rDVExTDabqI0Dxgc6Ttq5sU2QI7IJgDXAFV4H4cfFIFodVAYRiNxUSiK6E05p-BETPgR4dbcYyn_JlvjHAk8xf5QRvGz8tW8BCVVfqta2eAvgpTUe8nnrcVOLOFK_pxp4lt9WBd_yg3XzLtq3hSsp7d8BqD1t5Tf8naO3tGG3Xm__9U7zzFoKsjtZvarnKx1Xilx-ohri9k1JNK9nerTwP07lt07IMARTaACMryft9s57Z05eiPFt_eeOcjw39wApeo-4gY6BRa9yuHW-upE58YzzPNUi7q2tYf1KIyYvLOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=J4f21UOsIAnSlIpFzql5SfuDAYR6S7_KlQ1G5oya-V9DxPqObBkXm0D9cm4io3KrSiTLc3DMDSrVHZy35oGkgn-h7EL9_a3-C87loDWHa6YbQJh6_8Y6YSgy8sW0oZYer8M-T-JmdsG5LinlWHuqyh7GIXKoBmuSUjz_Z6JCgTG8u98kRxUkSyg0ZZo-Q9BeeMUPI_1AyHEJxRAkQFlZ25JXemnyuIgbFpi4ZQkZILPTstvpVyMVkTlPw00QsUDdKNYox6SAUJMhmXZsFB55UZvWAZ-FWvTcJp9ccFoWt7NzsuYbUvWo53yJfHQgaQ8teX80oaNDWoORfqbxJhKOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=J4f21UOsIAnSlIpFzql5SfuDAYR6S7_KlQ1G5oya-V9DxPqObBkXm0D9cm4io3KrSiTLc3DMDSrVHZy35oGkgn-h7EL9_a3-C87loDWHa6YbQJh6_8Y6YSgy8sW0oZYer8M-T-JmdsG5LinlWHuqyh7GIXKoBmuSUjz_Z6JCgTG8u98kRxUkSyg0ZZo-Q9BeeMUPI_1AyHEJxRAkQFlZ25JXemnyuIgbFpi4ZQkZILPTstvpVyMVkTlPw00QsUDdKNYox6SAUJMhmXZsFB55UZvWAZ-FWvTcJp9ccFoWt7NzsuYbUvWo53yJfHQgaQ8teX80oaNDWoORfqbxJhKOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=OhGhEdxooYP5bGCFZp6DWYsh4UGH68Jl_erM3WFYGp5XkKr4YdIrNbUqMp696L30zClxz77mAvA1NvdxYvA9G9tNw6XOB-QSC7F6kpRE_HlAWIYQ8_rO1UmZgTHT71DXHI35_SoSxBOYjkNjDcqP6DptwUdfdbRDh7cdWmosO1T0WgHSEYPXc1fenB2KO0qIbO3ztCHIpdeqNKl0OKS3kFQgNhwqD9-efG5cDpNakvEWUrQK8_44ojDfH3ywyRjsl0Q3zFO7ZZfFQ2rgmZgaG2u4Eyg8NTix4jxGVHcepZBMF3LQWMKTK3KSU47cU8T3HDt5fpmeJapDt7NwVNTx-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=OhGhEdxooYP5bGCFZp6DWYsh4UGH68Jl_erM3WFYGp5XkKr4YdIrNbUqMp696L30zClxz77mAvA1NvdxYvA9G9tNw6XOB-QSC7F6kpRE_HlAWIYQ8_rO1UmZgTHT71DXHI35_SoSxBOYjkNjDcqP6DptwUdfdbRDh7cdWmosO1T0WgHSEYPXc1fenB2KO0qIbO3ztCHIpdeqNKl0OKS3kFQgNhwqD9-efG5cDpNakvEWUrQK8_44ojDfH3ywyRjsl0Q3zFO7ZZfFQ2rgmZgaG2u4Eyg8NTix4jxGVHcepZBMF3LQWMKTK3KSU47cU8T3HDt5fpmeJapDt7NwVNTx-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIGTJ--nwbvNzvI5-DAADgPqSkxgv9TAWz4eSX3hvyO_Suv_iNHkhXvydsWPn2m-HRYHWvWvTgQEzBxWWeevnDEfYvsbKPi2rhX91VnRXt18T9bjE0n4_gOtWAZKlnTLxygSJlhJCRcyDjg3mgHY8rMik4afqAT4A4eEI-ax94tqm3wJxB4ud54RGMrnluKpdT7zG12_Bp5MpoICNVrWtNpevSxvgToX7zRFgA2og0gqY_gbN7sIqBSrCEoqnZgAIL8o3QjojsXh0tDtLI4586iLEFmv6BRrWJdNrSXyXGLzG5MOOBitB8cxZKkyu8gXFL3QCE54hnKtUvFArCY28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMjGvOihoy7x0rN8OKcTYHtivaeCX-nKqbs2VAvd2yTiAPAtwtk0prGV1odrqMOYNRLKdmlMlBIskZQR6pmW3F89rs2wPiOGj2ewebZeQBFVOHfd6B1QJPgJCWcrBxCC5xAPAzNQsjXV1kHjJ6bTIFML0a36PKL-pRQLCWJpncpjcmkXYLGqqTVfb1gIpQyz7z3zEGNnUU7yK3CVlOkkSQEfNAI5DbkAkFbcYQIjVay-FXnt5e3t4bwxRnvWEUfO3rJXlfWUMEwJ_HSOjqxFFm13R2CN6RwsjqdLyyW4l7taPvGXofdzM5oI3mjIDQWl6RSLoajrNsW-K5sof-z-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWnPnOMOeRuJPp78oMSG1x_IdvspHDQpUV_Pu-5IcyGq9uCtcvoKrKkNg2-yYvHprJi01SogsuPo6YZlVwg20bAo27lx9o9gSFisD2ikMtth_UajjaPxx8TRteI_apXa8Kmk8ELMUhxdFszYaPU7dGevpalip7voDEVVhbxIQgq-BNa5E-2t5VRALStXqb9MY9bV7zwPA_ylqBipMDoibLdVMUSU8V5asygLmJLPy5DgHxCuYz-kAqaGdC3ulaG7NpDv6Vad6kMxzIy_PR1gpcqIc2KJWA8gr7ExBQvto0AdQw-8WIaZzmxaOvWuh70arXjwlh41sT3LC0ZDWxXTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8xUHu3t-MfhEsuozzGsXd85XF0HQ8y-ixVeVEhEkzFt6B9iIC7pOoqZn64J_q6P01973WK6xR4fgr3XLJCK1bvzXLaRfEZtDxnuK01EBlnXO-frq_g-pJ_LrZuthLUsCpVFe3F0Kb_yv0oykrVYUDVPnK8LrdoPPXIbmlebk9Cb_4UhRaKgfEhzW483JhfOixehYVw09CXf3B5cXDejqD6HPairmuSHNN-RdnjTVPFTvObuchjwZo6MZE0eHT0zlFLrIX8rlBsO0VPwYz4pHs6GOg2S0XR7f0KGkwNECUpBpAZufWEF-fEYJvHot-D0WvenZzHwQ7-Hjuw9QK29Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0YRVO_fkf5hXZKZcwAD0GmTnW03a6vDOBCVAA64XyWo2W9r4VwBKZWNN7k37h1qfexwVChqATQ_Pk96zpf7gMGA2jALIFTQEcHXlVDcqPRHIjMQyHaN1sAQyQxYNJOP-phzur-2WqK5TDTnC_uPJS0x5zT_GfvetftNcP5I9oajP21q3QoP6WrxmqJt3BLM1K9lciW4xVbEfKCaWDZJB102WeJFQOUVJmUOLsKeTWQdBAKDYfCt5P6SrZzc2knTBSszNUQQJNjJOgK15JHQxrh_1lqR_DwbJj6yzc4pIfH_9pFWY6spuSS_te2FffH8tghHEcbWfVm5BTVNIllBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rKXU_LwFtitezMyrUy5PBlFqC725EQ1VCFyYZefD-Ndyyplw4vpHMjrygUt5baKfYoE_sHVswY3OQblyaCOjwupAcB1nrmfOaiVvsVCxSZp3dr3Fnp3JBBNHkuTNfOGdEOvn-Bc4jPlYNp7XW4dP3GmbcyGz1p6bqBrW03xOxnFga8kFTuAZMBIR55b8DVKZ2D2DZ7W2ij7-bu8R7RQL-s3PO5Pja-3IZvKzOyIvKvcP8uKphQBz2VGOpsRMB-s2odBbYsjtC75dAj645HK8DJykh6vKopZhqY0sscmBvTZ6K6U0Sj0_kot8gge1oxJkKU9HalGR09kK-2JsvLYXBq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rKXU_LwFtitezMyrUy5PBlFqC725EQ1VCFyYZefD-Ndyyplw4vpHMjrygUt5baKfYoE_sHVswY3OQblyaCOjwupAcB1nrmfOaiVvsVCxSZp3dr3Fnp3JBBNHkuTNfOGdEOvn-Bc4jPlYNp7XW4dP3GmbcyGz1p6bqBrW03xOxnFga8kFTuAZMBIR55b8DVKZ2D2DZ7W2ij7-bu8R7RQL-s3PO5Pja-3IZvKzOyIvKvcP8uKphQBz2VGOpsRMB-s2odBbYsjtC75dAj645HK8DJykh6vKopZhqY0sscmBvTZ6K6U0Sj0_kot8gge1oxJkKU9HalGR09kK-2JsvLYXBq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=CZ_gHMg6o_d6dQwwG4fGY5Uz26R7yxz-FVhB1NCJznFix56YpqHBH77_STblQAJpYTifXjyAieIK4Oz4_wre0LUjsPwSoK-BYvHUO5FzxCEINYd-KkdoJVp2wpEKviUvIiEfHLvY8DH2C3XPdh6YwbQV3s4DTPvIGC9fdP9aU97XtB_ezZm4QTy6y3geBIbctCvtpmwSyqNhv3wSC4f3EyWMntyXoTZT3vBU9Zue3OQdhI9fbuozVldQgcR059tDGbsZakruCenD58p30j9tBl3GzvZvBkUDLyh5whPB1xP0ctYrdT6wvmPWibyKk4nQqNDqBZhx-tGhLaBx9bFHYJ06jqDVby8b7owh_LivM5s-4udbsF6IykmkBuMzIBHJeqwjZpXy1MX-jEKG3mpvYBMDjQNQzAHZ1Y3ka9FmDTGnnV24aDfhrHJf2A0ziEbC5bQRUtJ1-aVY7ABGYTY1wC4GcSaaKYlRfc9XLIl7G33LknyDY14YDB85LO4nsZ0bJxrtuNsZd99_uvm6K0BUfL4X1xzE2wgDU1XJqbNnzhOwG20FTm3ppIEkI9ECCvhXAb0LWEcmR6h7wWlRlg2LpmQXIhOei0g9FL_o4rbQlpVqQK5Ru72qmVZyQBgcgKMxmt_9P2e3WaRuSSqifFXOgVBnC8hRhqRMin3k0Mb0Wzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=CZ_gHMg6o_d6dQwwG4fGY5Uz26R7yxz-FVhB1NCJznFix56YpqHBH77_STblQAJpYTifXjyAieIK4Oz4_wre0LUjsPwSoK-BYvHUO5FzxCEINYd-KkdoJVp2wpEKviUvIiEfHLvY8DH2C3XPdh6YwbQV3s4DTPvIGC9fdP9aU97XtB_ezZm4QTy6y3geBIbctCvtpmwSyqNhv3wSC4f3EyWMntyXoTZT3vBU9Zue3OQdhI9fbuozVldQgcR059tDGbsZakruCenD58p30j9tBl3GzvZvBkUDLyh5whPB1xP0ctYrdT6wvmPWibyKk4nQqNDqBZhx-tGhLaBx9bFHYJ06jqDVby8b7owh_LivM5s-4udbsF6IykmkBuMzIBHJeqwjZpXy1MX-jEKG3mpvYBMDjQNQzAHZ1Y3ka9FmDTGnnV24aDfhrHJf2A0ziEbC5bQRUtJ1-aVY7ABGYTY1wC4GcSaaKYlRfc9XLIl7G33LknyDY14YDB85LO4nsZ0bJxrtuNsZd99_uvm6K0BUfL4X1xzE2wgDU1XJqbNnzhOwG20FTm3ppIEkI9ECCvhXAb0LWEcmR6h7wWlRlg2LpmQXIhOei0g9FL_o4rbQlpVqQK5Ru72qmVZyQBgcgKMxmt_9P2e3WaRuSSqifFXOgVBnC8hRhqRMin3k0Mb0Wzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mG0ECPoIR7qkY6xgBdxKvtkLm2MGuuIkAvPJMYP-_Rc7GQZbcGxQnWlw99AzBIdnfnr-Ic6SMmKuLVm4Qif5aXAit0vNKNCYKTlwrMEiXeSgiT9_HBqyVkC38RWbUUkOS4Q8xPLsNNDdpTqHvMk7K8kJKOivFAQtqLzqoZvdLFUfDeagPePFrizFLWfa58e5by-A-FsZGmkQ_yFbey9GIwfP65pQ_YF6KmKsVhKM_f4Je34tMFcwH8y87w_OZBEZDTZ6zEcdv6smsaqoxXt2cJPYVXW-wXEk3jJI64RLRz7CMI073VYkCTQ3dUKo8BB5Orl04_CziSOpn0A38PEZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAIHSl0cXhO4uf_DsKioB9oo2m44gUWiHw8inTNZKm47RLoN0Jo_FehNYoJyHqV7xUSfzuoE7dD8kEHmcRVJ0aML3E7R3E317bAW89FgmCJ60LADIsGmYfsmVj2brAT0eXytzjP_Xe57Z1aJN_r3Pz6oAfiRjA0wVtMb8QXP38HUgPx87NPj93r6gPuxyFeOlMRTBqXD2mqsHeNsqB68JtcjayD1DtuxGoH_lIsztE7MGaMUElgwm0HtHrGvnEoSlVAQ_Zo7EBWUEMzIihAGOGDcbyQIpalFDkmyPjWgLoBX6A1eDc_ISwZgmx5Ai0csVfvoquUFccpBtnrQevh2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK9vmuz2HVlhybsv6vkxoFfuL0Ojm-Bc0S8rH9EKq_OvvT9vXwYFgblmjxO6vpitK--4WmyfIOC-RBxw4AZnAml7XPJXvEziFYtvd8vDD1TJa-0vQNzpwDlIEDLd0w_pbdHOY61owaZkh53HCMzwzbo9MHgU1IBZv9Vwgja2Lg1CBkB_qCYsiEVPq8W48sJfO6WRRLtZN1qShUqILTsCI4uwCM0GZ63YKIHoPczLE5ZVG8sW1sKvMlvMiCjQ91ugtp4TiucOhgwyvCI8uvE-wQnFnwpTcFyrfgUCjbPedBFq8O-gyYf29_1KhOkCAvVKQNI7c0QFbWG0DQEi6wVjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-yFHt9nasEjjXSMzztr1Wer9KR8oNUOXDbcGO7dm7wQjVCdZ9Br9w9F8ylZhH_xiq67QEAE6xTXzqNQmd8womxypp1QLil0Dq8stsbdiz2_pRIz5QBe60wj6lr2rUlh5cGt4JQ5xDmLQq4gZdO7XbEO7tadYT2TA0TI0GOC7bgORhGWvPOsYis1Pmi7wpH4IDRmyXFnyPczs7YPOfjYAZJHYmESBTOe-hpqASHiRwh3bW9Mr4PilwCPe12R97XPtD_m9NGQsxjkVvUU4BFgn1dP2TfRQE1Rz6lC5UTZcM-cdOOFeffmYrGNMVOX4qxzQj0mEVXKJzRPP5odhYJ_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGK_M0P2W5R2DN4bZGQabS8n2yzOZqrQtDe5W07EW290CF0H9NGfMORililn14KKiK_Ae8cWnitUAcWVnE04RE5wlvIFUomP8iQxMywSf85bM6U8_CvpgveC6nkN5MQW5eg69_2Q1zh6rNlbaNnRqfI75wDshn0foSxUx9OltsmgYgrNpYkkxdMj4oMNeBvCUnQwPM2xWX8he2js1xSozbnn4NqpcT7ZmBfOHlyYPVf87pwUvyQd5oDHrrvFMmAFN2B85x52T-xWmvOq5hKLKWq_s76anCf5IFpWOTIGZZYCNW2EUXr4D9dDgUUwbNGk0QB9nOUEM-ZjWTW1KauOGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3HjUxPtKZHqfnNcBEj1i3m5QZtltTR0H72Gzg1Ro2dwdeQ_ZnMx28GaGZH0DxsATXM3oJHoY0UazlcUH80ZnvcVrYg-V9_CPV7lMt1dtbQCg3mp7ASmaYIDjSJyU-Hdv1K1UUI_PsxTK4NaGhrA7L_rtgEsIH1qFadvUFZOJfP4rkTn_oo54i8zsoCAqPk4jHHEC_fgsnQSennHiqQOOpwei7MEqnCCoVf1V51sFGCnebkpa52YG39-HBNYvoBAgN2dWcKYYQMWpBE_azLOPc_IQJ3k5QLv-fmyV6PW_Jg-4tQG_fwMxzRcUSuiIfyw69WkkuxCypAwQMm5PrKlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-TmJwBz6pkOXM5x5ZszNZy4_-OzKVqYXpKZzVQfgYxq7uvApR7MPO3RYqpeU2T6quuzwwEOs1shR0MGY49A4xl29HCIA6AkOixKm0TjD5dCWEEix0ITzngR6T5SCOR45QoEX8EK3BAAjsrloKKeBAZ5hoDCYk3VvYDO_HYr_qGiQeWKpob7fUI34xi2RCU9XbNWtPVqT8NIbXEgF5kZuOvHPr-5ukYyvo4LwmTej_ZQq0YOZpXrhstAGy274jkhwz9NQiaBX8ukpOwABIp994nyioKjoKwD_On1oO9TYP4ZOIln67oR7aKmlt37lcwniGXJzPbZyF5KPj0gDFrHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8DzRpuJWpBwVGfvmJF9kYys9YxOgEn4njkBp2vHv_tU7IOTlHWF4zIvqug9nDicz3a2TpdeTAtNuauvVVSX3euF7PGYjOvaLu6jcSr3K2EELeSQMw256AqVBR5TVosEmTBYaMXihZGt5qkdbai5CqyShLz8w-uvmMlvkun3o3FRLiq8I2Hdd7GjPxH3ARzrCDCHq_et26j_ijJkMvUyMwI6E252lh1JURCsOx7UrifnTkN6oKkIYdGvZuPxczYsXxMZVLTwdqBU3GyQmTMxsu8OrYn6KlwYDj677AkxMKJ0l98dz9qCu9umWKF8YmBjp52OLFX19FjHVSAmreMbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
