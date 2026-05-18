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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve1t-OI_HZm5G3EVaBeezMQ24iR5Nd0qw0vbsHCvfmWTZRHCrDaMImIspzhSk28ijOc4nNKXzdTmQ6OlEse1PSN74-YdIUpqwdMH-QLh-MvUFgZRb_i86H6tqawRfObE0puD_kEjG8ysIvNPEX2oKYEVRTQLGBkE0W0_z_B9xLXxE8RE1r8L0-5vpX5DcxOILeZkNZoBml8s7vmvFvTgk4TUw4X1xIIAQuVbjq5-KVi3u4B9YCpqsw6XL-ZY2NHrMXuOF6NRrw1l1xMaAxHT3OkRknyJxLxuDZYwuAiIVutOVdgPFyVPUyJXxDo3H_GHZLwp_Y-y9Kur5UsZ5n-ZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn4pUQAh_qhz1yRM13i_qVdoaTkJxBoUJw057gC7YUmLCfjv6_PHFKNIhIoXA7riFwDtlQoEPdrenuZxa6srSbgyBtHqaVeort49dNn-de-MNnbe_Ww_1jg-TaemTeiUw8nh7dXXk_sprOXHvlaVuPj8fs2SAfc-8_NeoHPbqdjkktgU0eMxCYjLFZor1qauRKScsHwrpApfQ695HNyeMrKD_lSNfksW7GaGth-bc-R8MRa1mLa-TnIM3sF4viraOTkMTMofhxcL4XGSMwTzu2SuSbbIVpq68dBNcXmRb-eXVcZP1RqXWeTZvocINaMrAOAFd7FgyTY08g4dqZD7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsvmeNvCzeUAslGMTOkjRjDMuYtLFxmn8rZGi4wq6qrRcEWuiOmATEJYfkzrKQtaBw6-KSc8VlpStwLYNN4T3A9556XFHENwsba6rh1bNiG1Q7sqbbQEkjmhGZiKdbY77939h_o6FaCBEguwSKesuDXJyUNGs0ulYxi2srDJ3y_mBzb3QxfJiNEBTYzY10ZHrIAU7fRxh0svdFQB9bydGcKe4hzG3clPy4e5--b9AMKnoYADWKGxRNEo3U52OfAZkMtf4YmZLgcEAoJv37bxtg-CY1Y4uf0vnC3EH4E6ZkoLIsZJlL5WNGfNjEvB9ap59c4nxWcfUkxdXbzfuBUK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjpwFCEUGqG2K891Q3q-lObzyR729XQjUPZVTcxvg5yVk3KZuITqVdy46vDqofCD4hm_Oyo481UxF2M6SsPzimxl--QthWFh8xONZQVU0gGAsC5OxKxGqievzkSBy_0uTL_D9iszLDnA8kpih4WH-5pstiDnTC9lGQ6YhWUg65gK-SFs6bucyRpEsiiy0a06n1dfcFH0C3Nsvg-0chhITMvwJHCGICjOy169iFjTVPeRq05cvmckW5ipTKGCBbXChpwDtIBaieLbmMWpL7978TWtq9Or0mR597oT41Rl46Ne-_gslaO3AGvCrw3gNCzpVOhNoBftfikHIaNIP1TXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS5jr9TXz-BZNThv0aD8vhyMnjAWJFV_caWU2CFXDIDyUi85510Ml59JH5Q4nWFfN-z4_S_3wwWn2Fl9K1j34cHMMLPWAUmy5qS-UjQFO2HAxBEZkEDZquIlxaemhadIPLihzgPS4bcmV7m_KC2poqeON022dZZjOGE9rvfCr8TLYlnZjh67ALR1Wq19rRiYikX_bqErlOJABZcgjOflwS8d4Nh-FgeHlmOeHxCJqlFl8u1mbsWhF2aPc5KYHY_yfVgWsxOTEvuxbQIJs6RWl5YTJONHTE5shAslnuL9pO642xKXPUzQ-6xQFKvqdVwexL-qgBc4GIbQ3hRdNLxK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb90mKWJXFvA4xEWsH01HhGg-PeCE01raLzOkZMHvvslXCsw9Zd_0U7TDN3m3HzRD7K-XBE7AoAd-q2dCO6EzvrySmUwmMER_DdiO0u1vej-i-JCWH1Rvt_OaXm_0AfEvTN1UCtheZfwHs-rc_CBnLx12D6V2MZ1vGfsBpnijBow3yzQSsg2v1G7222PmPW_4-Y4D05XXcIoeK25qZeF0g3yS7lDRytO4AozWmF2vjrr9kWb9NHF6DMm5u7X7EtGS8uDEmnwMTFlLk9igI55UlLT5uFT60GYS9VuBgBb2sFWMdLFods8H7mquw3IPMVXycg_ua-sFpASyG0uyh3T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfuWyn1M5jFRTUSCwNsvyezcHuR0O9RHfQcPeelVdmo4KghY8n2ljTVKELQfG0u2LUuIKYQny8TD8v8hYcW3b-ej8LyWYyG2THy4SlZcAv3adBp2OnQDHa3XH3-xUs8qIT3ZEaG8O4PZx7yHC4gXLFiJeR2Cxe341ICjnQidptcbJsNfj0ZQK9ewz82tOtQ4JGtorMH-MPzIEJcChUubD9Occj946fv9NpWAARpmLsdS5dnibpRtNW77jfNBlxejEF26qlgLp0Shlq02chpmMXFantwBHLkaDm6YgL12j3dVKLJfEgtIYnaot52BK5Xc7JlHwnnqOuJvn_wGs0FYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAbJui02NkUEP2akQAio_JyGseOgetZRhqKHgMDbhtAF7zi5SIAJ-NAT7cAAxKlSPoSGd9XOKVJFX3l_1ZfQAw4_8sFp_oXCSUjCMl8p5eIVbkkbraamUfdVE30aoihDrq1USHQ7MlC0pqbBmj0snlTlNCTBgL4cKKnzvNXJNJc0G2wKoWe2_VL1vODravD3ukMAWJQ7MCNDmAU1741ZagEUX44Zh0JRLtBH9VM7kYKw6hMfWPI-02Fw8NT3q3XSNcm3Bbu44RjqyzkB8li8QL41Lh2x1bvgr06OxPTfjq7pwTcItLCUTLlMYe6bl8waehbI9bTWT5gGxdcUJQCM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhFoFvSxJqEoT-1KE3auTog1Pt-ynxIVjUF9OSDtyN4W0ErHyu4Y12jqWMAUaSlonvwwyxZcwL0Rz8SCGruML3R-tE90JwujMaYgFfqzC4dC7TDBhqZ5ylrn8nBggJqqWvRuq9MDqfhFmNBLXYh_wQzARXzMmAiDrAulIMXXCuJYh6mAJubjVFinIUAVkoWpoDKU6Qaup-UE4TMpWNyhInZ7qKixMGfoP9bfrQqdDguWQonqjUkt9nafQNd_blEmYwkGjGQDDVricp8qVrianfCHsS1VU4rL7fBNrAFuV-ZRUdhAG02PalVw-XAztPN_7auE3NrBaRpsz3hGPvN7JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIwjJ5o2g-Q6x925SPv9bCOg8mt42HqqSFsK91z0R4ni8E0fA_AIcIA5egUzaGU0K6-DMpDupIGPCHPz998O43b64RQUnEyBuFVaKrSzSKAlpkz5IMFw0sl93H6ydqk2SLmD_0YMKcCHB3B9jjsHZDTKHyYS5wZWl3jvYag9J7xSSH8HRHCyATbWJNQVBtlpJam9_Who5j0fXYxaCCXwPs6uzK76l4Ahvb_PkzBA8iZg-9mRA8B6nJ7dqK6yztC_hYBgcEzXtBMURN3QsLvIi6qqCavhjjP66ASDz8psmTF075aNcBcll6GASzuPKLNg7xGP_4IwZXuFKRwiTQmOOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfz1-7V0FhzF04VUd9Fj34wsP5uqT_rGu2E8EJ2eqa_8CB1alyPXamxmHl5AbbweErSovZ4tmVsNseMvGZ601S7rL0AV3IkCESMzatScOAn3u4Y8UiiZyxHuq-v-DusWT62z16wkU3DsGFg2tnQRzirWWgw-_nyn8Nw9trjBUyeZ86t98BM-EA9fMJmDwa3gfyDw_RD3f9iKpRNl3eMwuk1sghblrsGAXu5I4fYuaOhQb1Vhw7op8F86sLjrxBBQq6K8opkzR7NftspL7pt_rT_re1QH0AxxY5hL27vIWhPSL7Czl65uOYTnxTwd-T-CKZyR08ggN7vdI4GpTRuhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjU09ZcCPMEgPGAi0AQOa_fkT-Zp4KmWgElnMcRGe7oebXDBSwPjM_nZyfbJGPNufhHqdxVSB5V0YdoS2TMpg88wcKmeLhMnBYqo4lXm6w9hp82M920wmyHSaD-oukw-3_D1uto2URBpo_g-DgtBbxyFyWnQl89p_T6YepTrJJ_9SX5pw9Qd1Mh6ymNhbkG_0RP4yAT-qHzmzgZ-_YxoXkBrpr9wBLqpne3zPSMYFdzj-vdC2xcex7P2YEFHQ7ZmSA3BVTiUctRa36odMf46ZcFWD51riYnAsibt65e3gbZ4eGVaLl0G3a7Gv-3GKzWOTxn5DZKk-y1RhgL9VJUJtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=aNAMfuIG8Tti40xlLwIxOgpGJfzQd5CLsWkY9eLQqHiN0c6rfljzArF51wlbnQz5vvzs4B7qwmKNCElep35xrQIb1wiLAGRNhj1hOKFhgm0hqJauRM_EV3Ks3BOjK4YMDQ__MGdrSyAwcysEo5y61u4nqU6z2ZVBeN8xCxg6a1k5fjLAthDOI2qL0bElrcVOSlgIIDtfrMeMf5kHRYGQT521hr4ymL3h4y8JabU8AyioS6Kd8BEfvrXM5k4wvIg-Bh88sfCOUuPkROp00ZnUvWz3EZxMDhrh8JcCSnZP6A-Gc0dq3sdjLKPlk0mJVeeMWJo6Vy0qNKe8cLtW8N8W4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=aNAMfuIG8Tti40xlLwIxOgpGJfzQd5CLsWkY9eLQqHiN0c6rfljzArF51wlbnQz5vvzs4B7qwmKNCElep35xrQIb1wiLAGRNhj1hOKFhgm0hqJauRM_EV3Ks3BOjK4YMDQ__MGdrSyAwcysEo5y61u4nqU6z2ZVBeN8xCxg6a1k5fjLAthDOI2qL0bElrcVOSlgIIDtfrMeMf5kHRYGQT521hr4ymL3h4y8JabU8AyioS6Kd8BEfvrXM5k4wvIg-Bh88sfCOUuPkROp00ZnUvWz3EZxMDhrh8JcCSnZP6A-Gc0dq3sdjLKPlk0mJVeeMWJo6Vy0qNKe8cLtW8N8W4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=gXpYKJKc0xomodItMLL9_7rFlGhX2p73A8shmEw4QJf_K0zA5FWzzWc8aswwQluJ8iBTeBzPX4iSb7yQbBmmq9b2GNZp8_1c1j3bajI_KqC_E-VkN9cV0r-CrwJfzmC_bTZW3DXsEpTkHaTXBBxO8dgbeJFo4iEZhAy8PbkGaWByXSLrS0_ZXfdesCNEVt0amYX14-teLXYizA8FRMwLp7WA9QA0CxRIAL_s-PbrP61_faj4KPpk0Pvu-J7O4QMSAz5Ds2Lb5ROdMVw2yfbA0TcTBActPLzgBPN8qdlUFhNPlBbHI6QNjRqgDOZAQRd16qBqL1IwEiosxXSQRh9FfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=gXpYKJKc0xomodItMLL9_7rFlGhX2p73A8shmEw4QJf_K0zA5FWzzWc8aswwQluJ8iBTeBzPX4iSb7yQbBmmq9b2GNZp8_1c1j3bajI_KqC_E-VkN9cV0r-CrwJfzmC_bTZW3DXsEpTkHaTXBBxO8dgbeJFo4iEZhAy8PbkGaWByXSLrS0_ZXfdesCNEVt0amYX14-teLXYizA8FRMwLp7WA9QA0CxRIAL_s-PbrP61_faj4KPpk0Pvu-J7O4QMSAz5Ds2Lb5ROdMVw2yfbA0TcTBActPLzgBPN8qdlUFhNPlBbHI6QNjRqgDOZAQRd16qBqL1IwEiosxXSQRh9FfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5AveGs96y3ULgo8NBiuQv6__8IKeKqoLU7TPDRhMYqYw48KyWKbtZdmxAnP-qEtZPGGxlSQa-TPFycvkmx4O62Tcxh2VqizG2UIoL0OdYs7KLDrmpre0OlqhMLN4Kb6LWw3B5IVRhEwWMbnrmQ19plGddvWNeyZFthHqEXppFu8XvxI0Ipj8SPcDZ4bjGJ2_CBLeVw2Iz3rO0Me3AIJJRxLHpB96ULqkDZMpNT3L-urg8br-zmKf7FGa7OLItU8Kt7jlb7CFKFvv9YB7_Co_4M1K78ym0E0Jg-Rm9WdKD2wJVRQlBbJmHuxcq8RxdzaHQsZ01RgdOtfEyREOjAgtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1gdjxgw_24p3ZMWgfh-48fBcHenL-0nUYqD4g9AsKHvxDWb6T_xqLwfR_5yvC-Lt7hnYucoAusnug6Px-QsUeEQxO6247p4Hlv2t6H6NhJ740ZSijkha8YKSdT3oYkHAPa9jLc1ptZJjYTPbl5ZMzPA1d0T-R0FbKC0oDbaNFoUSY-VhtOwe2zPoqgcHOCQ4mii7OkVpsYLbAOh71Vpf6SKs8JAY8tUOgX3UowwgUbvnGmZGG61LIMBaaa7DDGoPUYZu-PJNPtd-eV9ORbutl6XHbHz1M7b9fD3QHmf3TuUxbyBPbwWzTvVxiuJSzmtSERwcFDdeAa8Wzj6xYyhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=l1O2of4wCLhMg5D-H3yc_zGwtfuiSDP-ww3Upg5xERraSBU7FhG8bEvLdmDH8mt8wEJOI6CXCfkAjSc5Z3o3TJ5do464tuuTZeOYMei2R737U25fBC3fV07xXb8c5YltZZpPZ-tl9miuB2UXO6AXSBWDT9cmMBjE8NRAr7Ae6eJHOKEFl24AjAeNXTMP3GIqjL_e-T4Vd1FJx8pl1PVxZe1WbSFeKj4gY6ueDG-A0r73H7XcpnB8GSy9Oi1Ix24S1c28JcvA4Q9S0ccMhi7Ox3nAhaT5DMgP4vITbc-HLeFwgJAgqbdFYJAFCAN6dxQ2pAQRSGWazfss_Ud0xnhPVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=l1O2of4wCLhMg5D-H3yc_zGwtfuiSDP-ww3Upg5xERraSBU7FhG8bEvLdmDH8mt8wEJOI6CXCfkAjSc5Z3o3TJ5do464tuuTZeOYMei2R737U25fBC3fV07xXb8c5YltZZpPZ-tl9miuB2UXO6AXSBWDT9cmMBjE8NRAr7Ae6eJHOKEFl24AjAeNXTMP3GIqjL_e-T4Vd1FJx8pl1PVxZe1WbSFeKj4gY6ueDG-A0r73H7XcpnB8GSy9Oi1Ix24S1c28JcvA4Q9S0ccMhi7Ox3nAhaT5DMgP4vITbc-HLeFwgJAgqbdFYJAFCAN6dxQ2pAQRSGWazfss_Ud0xnhPVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr8O6SO1I1R2LuUgPYxlssrRt_HwqpLBUgUg1iDB2ft_2PYd-vA5KGIemDY7IRR5VSDD8ptpRDwNZY3JOIyGiDDv6gmxkUbTl2T9miprdaBfTqgYU5IuHf4VtvG0Sf47WTYIYg_Wqwun4cvU8teD02URr0ViaT7kUBXIVbHm6kpVy9Ap5vw1eLYtmP3ny21FoG_xUp-ksJm30CdOyajJtR0fItvyzNJIJounPoaHwEVEW73PX6Qfyj9RLezyrTY6TvyHKsryQveu420AtrS232zI4BtDhUT5FQtIrB0oXs_IHja7tbhykzTGkx4vJGPosHycGOW99Xbv1jR4_Tm7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGQ8SeDCpeI0XaJDqmVhbIPELONbD__hlLp75DWyWTNZLTB4KLyOLTQ6NfatqqjZ4ahxhqv-T15shwe_oc7geIrjKESf5yZmH-9jOwh6-V-nP7NPWSucIxPkArSShRPcfgyoe6wS_LWOHgxBgrXRDmmZQ-qh7PMV_eXpfn-2LnylTgTdY6Go3NhUWAaXh4pFbhONbjNHjGCgPfu7ce7vusLVganMET_yi-5qlOx75BgJHMB5vk3Ad0naZvBgdu5711RB61FTVIWwYORfDJYBvCJ4nzsA7-PaAU-l8mkzxvzhHH4Lxo28FjMZ0jYSw6yycgr-3t3Ox8ixLAZHi6FAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTs5CIJ7XsV7o_Nmk7xPWKsDHGXipb-eNRwNClwFzHfoCpMxj43q5eyHaqlXywAkmzw-QG53yJ_4Upm41Xc7-UrMxcvHbx2fSr8QMHRpFpQ4k5YMxEuquixUxc28b-xlBDTdaNvtfZ_B1T-VsGPy_05gidWP26szAQcg3RUMe8rEJRDYWBGTSVJKfTI_A8WystOCtnCOkk2VUvNWkxClPqW5kp66BGImj4ehRAA8k5Gg9o2H2HHl6EOBsbQ-p7BECxsJqgBNGI3cN9UPsBvQboPq805P_ohy2FFsLf_3qkIEnJV8L6ItrLh_aC1EPTkdSpGHlVnH8cbZqzpd8NKWoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9xWNqgMJk6_nRgtPv-r8TTonz3rx3Pye1W-9yRqOOEqKqaJpsa-f0aGnkUJAnRQJBbH3XFvM6KCXRJMU3DY_iXyEitLGHZWRqHPBjCWG38XjUpR47WhNY21vsrH4XcP5yKpeukDgk4ym9cndWdHWB3rzI3XH9a2Le7nMmQQFYYtNc1MlvOC90C4TsxCUZFBlDRAJqD-MAoZHIWl-Tef6pzUdqN7WI5tRPZwVb7fkABcoarOiCmzGoUeeAJ4nvG2twD4tuVIb71irmMinOB3zRbtQpMLa4RZ9XnFSVhb_zWkUuMbf_WsyPo1fLH-wHe9doQZbPmY3hraE9Z60za8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNYK-1SM30znR_NMf6NBJVdgI9SKS7BRiGA1-t3GnJuFs0Yajm0klxevAi9ubJZiSbIwFtv2LuIRzrkgYkH8Obiz1LXhATTaMt5rVvB4FCnirg_C7dfKkmd3wUpm8d3o3u3Ek5MR1pnhThWX8OosCpTjP3UY-EaJga57W_MfIXBKGAjpgyEypwMbhO91tRj7Hsqkz-rh0lFrtc6QzjPMnO0egkvW0vS0kj1-oJlSkE0yrDkK5rd7WfmwAf_l5pV8xmtbjDkhv46IU1iuQ29fruFPgvQit8X6s5hc-yd4Z7SQvcUQgXxArnvsgb3bryorbldEPeJnj4Ty1wyYN50C8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=cBIJNJsIFMHVRLU8GYLmgk5e_UIkSWNWdRNxYoYVyFcnY4oJzPfKtasXV2iPcZ-UWCMKJWwlvT505SfpnxtcU1Mi_aYnO0nx5AzN70CAokweQfQr1hzLVMRreecQW3D_fDCKYg6JWck4BIHMkw9nZ_WBnrXgbfGxhpTA3THAj29rDmAVF6D-lu_E6HvIVynx9zkxCD77oJaWe1ZJxVupBfMjNxVS-SwjW3F9NCjBrbtuoPc-MwWhtyVzA0YtWAO8m8HV3gWxPhwCDQ1itm-Xiv8HG3vMa9zUYLOCZtBdWLjFCrrqJDMalfORbmD_Sb3BAEgBHyWBCdR1KaVpO7ZKhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=cBIJNJsIFMHVRLU8GYLmgk5e_UIkSWNWdRNxYoYVyFcnY4oJzPfKtasXV2iPcZ-UWCMKJWwlvT505SfpnxtcU1Mi_aYnO0nx5AzN70CAokweQfQr1hzLVMRreecQW3D_fDCKYg6JWck4BIHMkw9nZ_WBnrXgbfGxhpTA3THAj29rDmAVF6D-lu_E6HvIVynx9zkxCD77oJaWe1ZJxVupBfMjNxVS-SwjW3F9NCjBrbtuoPc-MwWhtyVzA0YtWAO8m8HV3gWxPhwCDQ1itm-Xiv8HG3vMa9zUYLOCZtBdWLjFCrrqJDMalfORbmD_Sb3BAEgBHyWBCdR1KaVpO7ZKhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=eXqmQ9jzZuo8XXAomiat6eceFEjaTp2OejUT-VHKrA3gwEt9vy7KC9dcsqrsZ27iqRxpkiqYRGuO2Rmm7YbYPzutDBonuHitwkN6crBZyLitUqQvhSKkOIbYNSKDIJYQ7TYMITziwOa7hOjD7-KBi6AOr55ro2eOZodjKremFfTTzCc8KEMl9v0_fjar5-1XgzPCygO1WQBG0PIM4TQ6dARQL_Q1PrlaH0KDQoymHvoB0fd00pNIgXJqS3ExO6ePRBSgNm2ehRoajSMRpWqNwkRZQQLpfqGnqRFDjYuFoN1UTxeQ12IR-uLJ6a66W5HYNcRoOEx4t-gdSrK8MjtVXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=eXqmQ9jzZuo8XXAomiat6eceFEjaTp2OejUT-VHKrA3gwEt9vy7KC9dcsqrsZ27iqRxpkiqYRGuO2Rmm7YbYPzutDBonuHitwkN6crBZyLitUqQvhSKkOIbYNSKDIJYQ7TYMITziwOa7hOjD7-KBi6AOr55ro2eOZodjKremFfTTzCc8KEMl9v0_fjar5-1XgzPCygO1WQBG0PIM4TQ6dARQL_Q1PrlaH0KDQoymHvoB0fd00pNIgXJqS3ExO6ePRBSgNm2ehRoajSMRpWqNwkRZQQLpfqGnqRFDjYuFoN1UTxeQ12IR-uLJ6a66W5HYNcRoOEx4t-gdSrK8MjtVXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=idOd3FdWIjNekQtaATJU585YHDlM7a_U2mn8vksre29_0l0abNLDctEjbMTUW78tg_aj_p9ntTYnPNvobf-R-ZuetD19wsaxOnD6e71BBRTiKpEVbSTx_oPOzmk6cfscFMyPw9o-wSweDj2p-5halofbzeW7yeORdZY27Yqu8ILBvLD4tN2i1cOj8vLDoFJiNcwXtQdjqf7Lu-LfmD5oFl_hXhAJPP-RD8HaNO6g7SF1CqUPjS1HgaSrEVkF5DUS-qGNvTo74U0mTZAxfZ_KjNvqopK3a1pJkE25j59_q-SR1c4xcfrD97KIysV0FH7dtIKC2rN14Om_2-p5BHBt1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=idOd3FdWIjNekQtaATJU585YHDlM7a_U2mn8vksre29_0l0abNLDctEjbMTUW78tg_aj_p9ntTYnPNvobf-R-ZuetD19wsaxOnD6e71BBRTiKpEVbSTx_oPOzmk6cfscFMyPw9o-wSweDj2p-5halofbzeW7yeORdZY27Yqu8ILBvLD4tN2i1cOj8vLDoFJiNcwXtQdjqf7Lu-LfmD5oFl_hXhAJPP-RD8HaNO6g7SF1CqUPjS1HgaSrEVkF5DUS-qGNvTo74U0mTZAxfZ_KjNvqopK3a1pJkE25j59_q-SR1c4xcfrD97KIysV0FH7dtIKC2rN14Om_2-p5BHBt1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pc6bZiphi7hvFnGpDR5CEb_k-ivtkeSSV1z2ocds3l-wTfL85PuZpCeUcgmMGll7ziYWvdTPkS0_iTAqhOr6aHabSHJH0iNFn5fXK7mcvj8GuiW1jpcAv6Mwshflcl27DxOygEuv3GcRwD4qyb4evQu6X9rS-kR7X2sTBEB9fXPXbOw2tdSNuKOvgREuzPZx_UDUBwwneYogpz2HdrZwL3eDXPKVy8pDAHa8uXgHqSydHg-gViwdRr5UzAWVglwUicmCdlBpNsMf0VP4Mp5OJu5PrBXECebHX5N0zTBFGlK7hCJmx_upSSPpAtBvqMRuXVhAqQApyO2TtQLRJ2Ssag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTQ1fh4D2iieNnV3Nt46iln42C5UZeG2rLFO2JHlzU_Zxpgqaatqbg8TW2CiHlovIp0rVbvXl_w9q_dO6-0mefleaqdJj_xHPuBGzeom35A5tbBFhjdEMXcinlwcYnmC0h-9ohhHj1NECi1LFmQZBqzENF0pdCG9GgxWHEkEXzNQ9O53CG-kHST_vIvx4TE7ohCFmF4fhgrkTt89htHS23CzKYJdD2B2FAMGIpB0FLgX4D--SCHNNXRICSIP83CN33VTQrj5NRk98hXHmec-kh6Kn4RYk-n71jjW6-z1F9lojiAadqnfuzzLIFNkCFIff7eWaPhF7-g1zkDaPit-4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0ECtayBGs0MIeEP818Y3e4C9LgJ2hj929FQwr8j-FRr6nqclOouuLdC6Pd92LHCGe1fFv7OrW9Mv5Gabqe3n4j82yt2WiB0ZpYVP3qrfiAaie3v8eppZ4HbUqy3GRc5mWEpBAdmdAwBajw_N1hLYVQO3cKgdg8pd_hgwk_pUSWzhagw36hRJGnExI_iG--QOCcBvgj2fORCymFSXWEQWwfe2JDqoKwpBj3Rpjd02Ob2HfbkgK3qX38qzbPsFkihvKJfyt-omldlIV3g0bEjE2R6efCU1apI-kitbgEltRMxiJXjUijML6YMpPsZvMPcvsaeSES2Anq79t7OIv6qgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOTCpSgZy1Q8GVp5DPoBWzhQpoYfhqsLYQ3ETzjAH2HANpROiTtrDkikTAs3zWAaHMpyfTwLSKQPybeclzaha-ZRv3zDNHRTcTZc5BGU9W6cibZjMOtIxIVXBmch2Y_DsfP0h-H89nzViPkJ_rzq06Hm7LlKY3zBwr1In1JS2BEZpjkVxyu3PF3VPCo1Yom3Lkzt7DdUmuVrYHSks2Sc0eoME_SJvH7oBC5ohKHoVTJGNq3oyLBujqBdjdS3IiLk2S7rR75OrsTfWmvVnfZ2a_Ajo2Y8_N7iGboi69-j_k5EV0kYdaVFEEqBFYx7c0TY4d_aswSDeVA1ANMhb9sNGQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=F_ETzFVFVPkghhfK6JmkcBf0YWDUAJQYzU0PyXuRuCRD8h-bSpYv2fi2bR5FqWqaNkTileG-UActo8q5Mozo_Z59BJycXlAqCDPNk4yRYopiko1Jyh8IM0btFkfxymrZlqmmZAiXrj0G2RYYvR0YZxxvsSYxKYNYWES79emjLZrbJGBmEwUt8dFmc0nmIRP_11kcsGVCZ5vwISljT0QSn_ZrgDqM_HR8DeW26dqZYRJzrSD-w1lb79CpAfTZNygsEE6F_Wlha4wyTg9snbMX1CHZpmQGexqxpfEVAQsoWBMZI1stUS0P-b05cwVzxxJHp7jEN6hD-pqxfxosYcPwtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=F_ETzFVFVPkghhfK6JmkcBf0YWDUAJQYzU0PyXuRuCRD8h-bSpYv2fi2bR5FqWqaNkTileG-UActo8q5Mozo_Z59BJycXlAqCDPNk4yRYopiko1Jyh8IM0btFkfxymrZlqmmZAiXrj0G2RYYvR0YZxxvsSYxKYNYWES79emjLZrbJGBmEwUt8dFmc0nmIRP_11kcsGVCZ5vwISljT0QSn_ZrgDqM_HR8DeW26dqZYRJzrSD-w1lb79CpAfTZNygsEE6F_Wlha4wyTg9snbMX1CHZpmQGexqxpfEVAQsoWBMZI1stUS0P-b05cwVzxxJHp7jEN6hD-pqxfxosYcPwtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XlaeKnALVKRfIg6SSvR_8k-vb83hsT0kOAmtaK7M4GrPGFDvzkaM9pEcBDxIwqe-MT6G1oVKrvAHQu-FLKnsXiJTreTabNTQvfQ8Y-0QUEFShcvtfNhRDVC3EYh8mF_O7GlFelfwJ6qpvEWuegcWz-kBj-GAcXQUZyJqS_c0sl5r0OmMmErriCGRKJXImX0KZJmI291Nxs9qA2kKb5gjR91n4MDtUTVQIK4EhsgzmsHvV2m_cth_HobAZNRFcxSfo-U1F3yIChGsaSjjE-PXEZ02Rwyuvi_5UOIDDtCrNyDhBDnsrFpb8enbgsZdmPdME6zptttpdWiXZsKdKaaUTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elDoHXno2KfbJ_9EJ12TnF164Jky5IE47FlfbVeuxguIeCTs43RcsVZpBMrWCg20O3tAXQ-1UNlnyr-wgSJBuxkstFJqpn0sf1svu6tBx6LinZsfY-tjCEFpVVDrxhINPAAuIvzFnsV9AXS8UFTNSAHybGZze8HFoIh1U-_FzZY-Ex6KcIuWN98Wit595Npb1NGPpRyD7cZpxY5SbOZ6agXhu9bM60HGoXKEkLiomlBcl51kt0Egl-k7cx6GCXeMVtgfYo6Wt-Zhg49vW7vd0tYNz5r4R6ECluLRSPFusWXMeWgZQQE49JArxy6ZdBudqUOA4TnKzHvmctT4srpdBg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=qbJBTnvy3NzmtNXMKWVOTJnsj50ZOthmBMC2ocEMlRLHZv838Nd_oBpjIlRRHSRLSv4nuE-xs1DDuM-zGsNJeBKB-6OvyiwEF67Rkzhc_lrYTZ31UWzZMHRiK7q_0iOu7TG5vNt0C0LwKNFs7rszewFEgL4kQm9UZH6yzVXP0LMV0pU9LE0SFzvhSl_N5Fs7v6H9uygwXbHmnhks59JYNTtpDLZTvsUUI7GUtgly-UecbawCZ3C_LOpFhwecGD4vZ5IZNFvvLDJXcn7ymUpcqdVsEFBPoNIRrV-CTJXi9K8VW7wqQ-PM5SVklUnAvkuCIn9zAwwFnh3i5NPqvbBJioFKJd2aPNFHur7ZmtFL9qgXR335AnR_HByqrhego5YgU7cPwbAanORClAvzC2XR865XRgrdDY0ZuyH0iXbZZ4J8VC8IwBt7JI04DL5MK9tBbYtQ1Nauu2RLxEo85MXC06WGuBfeU-Hn5rJqN_2sKk0m30gZZUNsygpfvN8q_d8s_3YTALlv5_uYmvv8fGm8ljahmpdDq4zo9RYvYZSru761q94QZSKmbTdCg_trEVBZVMZibE_0H7puZSM71j8_3MzFhWi8fGfgjtmQ4i_hVOY6gFAPZRzuBL9b4RFZCYf1cJEm38OqesYgY65kPmF1ykqrf_oBIGkjBQ0ZkuaYIm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=qbJBTnvy3NzmtNXMKWVOTJnsj50ZOthmBMC2ocEMlRLHZv838Nd_oBpjIlRRHSRLSv4nuE-xs1DDuM-zGsNJeBKB-6OvyiwEF67Rkzhc_lrYTZ31UWzZMHRiK7q_0iOu7TG5vNt0C0LwKNFs7rszewFEgL4kQm9UZH6yzVXP0LMV0pU9LE0SFzvhSl_N5Fs7v6H9uygwXbHmnhks59JYNTtpDLZTvsUUI7GUtgly-UecbawCZ3C_LOpFhwecGD4vZ5IZNFvvLDJXcn7ymUpcqdVsEFBPoNIRrV-CTJXi9K8VW7wqQ-PM5SVklUnAvkuCIn9zAwwFnh3i5NPqvbBJioFKJd2aPNFHur7ZmtFL9qgXR335AnR_HByqrhego5YgU7cPwbAanORClAvzC2XR865XRgrdDY0ZuyH0iXbZZ4J8VC8IwBt7JI04DL5MK9tBbYtQ1Nauu2RLxEo85MXC06WGuBfeU-Hn5rJqN_2sKk0m30gZZUNsygpfvN8q_d8s_3YTALlv5_uYmvv8fGm8ljahmpdDq4zo9RYvYZSru761q94QZSKmbTdCg_trEVBZVMZibE_0H7puZSM71j8_3MzFhWi8fGfgjtmQ4i_hVOY6gFAPZRzuBL9b4RFZCYf1cJEm38OqesYgY65kPmF1ykqrf_oBIGkjBQ0ZkuaYIm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=FS3qgGw8onKjMupi402oKRdAhE2v0uQYl27mv5mpuVOoO8izIBqeptplRHuq1rvE9SpI9QQXoh_MwYHIUegbW0Dsw3bwizSHwoyBAT5AD9BTTIBAWBw1Tb4FeCxoAQdQgOWw0VbrFayqk6hJLITJ6wF4muRTYEymT7Vx7Kt575htz5bF7Ui6cQHrssmMx-EPXuqmdlz2GU4I2cZd0GP19YD1xPgt5gdkWuUwEz1JGqe6_B81t6UUHgFfvO2ePcCoqo3tPaP7daaKDnwU9w72ACfsAgRxG6l10LWGeohAEENTHf0dyqQca0qlIYZ8jhtDaRLSLP0pN_1dcFxHihRzCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=FS3qgGw8onKjMupi402oKRdAhE2v0uQYl27mv5mpuVOoO8izIBqeptplRHuq1rvE9SpI9QQXoh_MwYHIUegbW0Dsw3bwizSHwoyBAT5AD9BTTIBAWBw1Tb4FeCxoAQdQgOWw0VbrFayqk6hJLITJ6wF4muRTYEymT7Vx7Kt575htz5bF7Ui6cQHrssmMx-EPXuqmdlz2GU4I2cZd0GP19YD1xPgt5gdkWuUwEz1JGqe6_B81t6UUHgFfvO2ePcCoqo3tPaP7daaKDnwU9w72ACfsAgRxG6l10LWGeohAEENTHf0dyqQca0qlIYZ8jhtDaRLSLP0pN_1dcFxHihRzCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=aCYFOVznASVFhi2jB_Qw0aY50nBUnkuntlLLQH5pXVn72MwTZglB_lNQrjV0zRXEo3yCfo-4vx-7ZWVyCZyvJgU2DVkRU9LRtGkN4tJIhcBnqlTbf1DjBj7GF87V29lKlS_GdLBan2I407DsKbGAmiZ_E3bA29GoCM2JomNgwzJHxo2ZPNgIW2bc3gL3gfANsJMQwcTiBDW0P9Au2FJ-nhdwvzKmehuqLSmDH-NRwsLupNuFT83je-6-e3mYjvHFC72XmcLWkRGIREKiucxsCqmzSAK7L95b7svViUPfE8JaPeDV5Qyok2aRt63RonbknnTOV9CafmmaJtPVQrncsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=aCYFOVznASVFhi2jB_Qw0aY50nBUnkuntlLLQH5pXVn72MwTZglB_lNQrjV0zRXEo3yCfo-4vx-7ZWVyCZyvJgU2DVkRU9LRtGkN4tJIhcBnqlTbf1DjBj7GF87V29lKlS_GdLBan2I407DsKbGAmiZ_E3bA29GoCM2JomNgwzJHxo2ZPNgIW2bc3gL3gfANsJMQwcTiBDW0P9Au2FJ-nhdwvzKmehuqLSmDH-NRwsLupNuFT83je-6-e3mYjvHFC72XmcLWkRGIREKiucxsCqmzSAK7L95b7svViUPfE8JaPeDV5Qyok2aRt63RonbknnTOV9CafmmaJtPVQrncsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=BUi0mOqVz_GnYa2AO2np3IhYRiwyIhRgssnPAPS8LfP8opkMsCJDobLoKpMHaynDv_X9KfBANjGBH02LsLOTR8RrPL8FCK_wI8xYcHDSiuu_hgtwO2r0rEZt70aahx_Oqw8Puw2qkTfFMNgPzx_p65lcBBMSrYsCRKxP9hPBgRdW8gnapmdV_NUu2dvX6cFpwGkPJ58UypKv1g0vcGRufUtClzXhZxU6oKhHUIn3lC43UbaVfBMQwGPIvEj245byG6Yhq3w_Hxyv8401X7C1ewttrwyDBY66fPti3CkZT0-saI4Va6SLyHUH-8_DzHZsAckIQifv7aGSJKIGxtaEIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=BUi0mOqVz_GnYa2AO2np3IhYRiwyIhRgssnPAPS8LfP8opkMsCJDobLoKpMHaynDv_X9KfBANjGBH02LsLOTR8RrPL8FCK_wI8xYcHDSiuu_hgtwO2r0rEZt70aahx_Oqw8Puw2qkTfFMNgPzx_p65lcBBMSrYsCRKxP9hPBgRdW8gnapmdV_NUu2dvX6cFpwGkPJ58UypKv1g0vcGRufUtClzXhZxU6oKhHUIn3lC43UbaVfBMQwGPIvEj245byG6Yhq3w_Hxyv8401X7C1ewttrwyDBY66fPti3CkZT0-saI4Va6SLyHUH-8_DzHZsAckIQifv7aGSJKIGxtaEIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=oJJp4vGPO4Z6Amr2Qw0UBgaymFxjwfXS5HwNEbEBYvy4dPVdxgnX7jfNBu8QkTQoR6zVoRZmm7-TK-b_egmcXIepBsJJ7aPwuWd9MeBJrcKhH8mKoPHwjk59m2JUgbLloaiO3UU7mxtltObfVFNZTNIqgokaILqB8BN-neZsa3lj9EQAhNgZirVkoLGxFzCLb3WNGchuU2b-mBYpA-CHFIMvYEyY3d53MGjqZooxxH1jQQ5QXJnVLj3uvoelanyRkYC8NKEN9x-wJDd1MX2vmhXy9waMXkGP60ArcmrttPkkfr5_yLLwskJz5Gkg3_kcqHHWdjwX7V5QU-9k8HTWHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=oJJp4vGPO4Z6Amr2Qw0UBgaymFxjwfXS5HwNEbEBYvy4dPVdxgnX7jfNBu8QkTQoR6zVoRZmm7-TK-b_egmcXIepBsJJ7aPwuWd9MeBJrcKhH8mKoPHwjk59m2JUgbLloaiO3UU7mxtltObfVFNZTNIqgokaILqB8BN-neZsa3lj9EQAhNgZirVkoLGxFzCLb3WNGchuU2b-mBYpA-CHFIMvYEyY3d53MGjqZooxxH1jQQ5QXJnVLj3uvoelanyRkYC8NKEN9x-wJDd1MX2vmhXy9waMXkGP60ArcmrttPkkfr5_yLLwskJz5Gkg3_kcqHHWdjwX7V5QU-9k8HTWHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egCMwomcwZipvEaSyDm-x9JDRwl4QzohaJh81lmagREqGSTdaJbinbC3zmuUebrkPiqqzD9HhXQTmxW7NYsNJpyIgmgFh_NbikKFSHt1v7t4M5bCgxKosYnYGN7wfQrg1bbr5-UdFz6JayNDCzFdbP6j-2dVwauTjpu3C3K3B-RBLpZuA23oyau5JT0YxZEerCgaqwbXarK7dsw7iHSbLt8VFWcEBHNazAv5nG2heg5-IVcbWDr6Hfwk9sVaNImGEBM95oM4pZs0PuQRUONOxmpF8AJenCQcoKKRRITqROytuLRNTCtycBPWyt6HYRs69Cn23GrmyRCIRIXDSJhJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBrGqkvQQ2DJ0ej9FcVnngf6B1zRjFurJ1eBDCzPfpHLHfgMKBXsRu4ZG8RUXrCjPN6RpMP3YpB6Co8L1-qTm874IjyggRpCZ9PV5WgDYeawho3EBXiqOjUgHln6wVK7MTP5tGv6i6zhLpkQhEPkQEYQYXLH9lMi1Ak2UpfppzWQ2qAas8zhaiHQSDxH1aXXDdNrYcismf1fhK8Cpf74lRCHmWY4XCdnErLUoIxKISf5tl1QOJTzOw02x58Px8N5P4PlroWXQ_wu1mFkAYGVSfpRlexoYO1RKsEvnCpuvz5UBijbCYF32-y-C1Wzlq2_JHjdDkG1OgbiTjmOdzVz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyLe8KLh1D5qwB8Zso27XJVwlooLopLc3K3tBx38e7RBHQ_DKMBmNQwzl5MMloRx84ekBn41gvqLB-OQwrkOKi5yUdzSb1QDuJ_e7f50jU06mrLKXDL8cz3wRFFnkjtoj9v8o0J1perSI5s6i648Zf9SJFjYUwnY-yS3u5whtHNddQEmIsvVEvlXQcODqIVEpoS6jU_xCDVVItY9Lpz6FuTTOKJ0sHaBX9bF3rnOlR-xcFelucceO13gK2m18H0o68Y84J1E1omrD2GQQzkL0OssRgoj6nDxl-nU3sUWHwTPu2aDyorQkjC6do1IHI1DKqaYuq8tbripIPMv1eybuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2t7rHlkTkE8oRISyf9-kJE9Gd6iYt5ZABo7Y6UXfH9NnFYXMex8zfgAl4GId8j2qmInUmOafkr6piaDW7E4jKPa2jDSz7WMkkciDd9tNTgOjcjT2XemY_5GepoIydX-nQaEDb0aVXpvvOyNI_U6UbRJjZ0yZM_4DV8xigmLkenntmrkmVBzyrgV-Ma0o8atexE42Q0xbjKqHdjqz-QlCeOlJEabhuH16w3jCYpSFK14DHZfB6iwRUJpNbDDR4kny_Kt1NQ5UyKv269dkLtMOmrwxc2q12yMN8JIjyKj_aLFH4CUM4g9DxMX-plU46hmuo90E0aGEiHoO0oXVBYrLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYl_gSWgdzLYBLaWcAPOHamvOq1J5mMncYylnk4pnF2vfO7ocnSOXSmX7WsHZCFPKKztXto8-ze3U1JpzxVjcPX-q_-DSi9a9ji-WIyfyXUYtPq4dd284R83iUXgQnaoOYZOpKAmdlwaN2jgwFVI61a1d3l6v8wmMPVtOBwjSkRiQ8ia0SLrNMd2a0LeVbtsOJi1hBsv7HSL1Kf_RAYDxSbz6j7UXsU5LR9AE0r580fNRUF5KxnQ2PPP3CxlzEpWc7E9kONdJla3m9fSTbuK0y0qrmHxhUduJolrsZ4zJuweUuQ7_Ab62b0Oi6Dc_mHvadlYhlMwBBbYYZNNrwiv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rJ_MZ4-YudW4WsTyEc5svk0wFT9b8aXYy906a9tfMi5EhaHpblpqXqaiksiisi__nDjxcuubDX_ssCGLq7YYMNBCBPqQcmyQ2KHesOutQRDEvTdKFZ4J-oSN5FfkfE335-48Z5FQGI0jba0LQ3ZGftxuvyFgnaswvsPjhAzQV-28ER5ZcJWzs4vSX0nUIlysSghXNuRKmaDyTsGImDmSXktyTGO7kzxgRL6KkTXI1Z9kni8FaadhG7LM_7TG023HAX36PKtbsZ0KCHjjLKqImwinpujA8Fc0LZ3fGo49HT40qNVJqGCSQAewzM5JPWxZju4kkD0UiEKvy08GQIpJuYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rJ_MZ4-YudW4WsTyEc5svk0wFT9b8aXYy906a9tfMi5EhaHpblpqXqaiksiisi__nDjxcuubDX_ssCGLq7YYMNBCBPqQcmyQ2KHesOutQRDEvTdKFZ4J-oSN5FfkfE335-48Z5FQGI0jba0LQ3ZGftxuvyFgnaswvsPjhAzQV-28ER5ZcJWzs4vSX0nUIlysSghXNuRKmaDyTsGImDmSXktyTGO7kzxgRL6KkTXI1Z9kni8FaadhG7LM_7TG023HAX36PKtbsZ0KCHjjLKqImwinpujA8Fc0LZ3fGo49HT40qNVJqGCSQAewzM5JPWxZju4kkD0UiEKvy08GQIpJuYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=fN-COdMchP2furcF8hcDikXlnrtEqoOLT1gvTG3Elq1Mkz1EbQhyypsxOn1f2dvt-5QgIDV-pcnwIHA3oBIyfIOuXXTXyLHCIs9K7TCXRVRoXtx9Wf_OXhoWwQuw1T5jX998QK0DGtCc90qEz8ZkF7npUVGCsBAHMTGwbt78QNgxCHeUsk3ZbAa5XDX3kEE6NW9wzNrfn1GebjS-xctV87gYZjXVsGaq7VlIuodXwQH8cPiMMKIlI8Irj0ys6WSdzXK_TjfhZcG9P_veaTT5u2MAQ3hbSFDC9dt2vYxnQt1jHcuVkagaHGyJzclKFPhiUWDiygvRcisBZUqn871L_4g1k0Tas_hIrVirAyl7dujFPFHMLHe_wfSjk3_XhbAx6YQsUVUCIMpa9w-MhUBsPwIar3bBc3mrZ0s-o3oiyM4NztnxY42hjnSc3bByVYCzmdxbk-rYy2ztoRO3qkuDsuTXEwVkKP-mrTe_nYydt7_ceK_dZibpB5aDgF-Mb3_BhQSWSEib-bAzsgynOWXMXqcxgNDkuizCx7h8uIdBgXfSHjKDodfux8FJn2JY72-bJTpwlufIajwfCWBnOcVqsr_y5Enhou2FdZThs2h3nMh1zw_lV3QMECIEYTAqmop5ltt_GRqGhtCHVtMvLorrKbrXqDGN56BZmzzW5NM4F1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=fN-COdMchP2furcF8hcDikXlnrtEqoOLT1gvTG3Elq1Mkz1EbQhyypsxOn1f2dvt-5QgIDV-pcnwIHA3oBIyfIOuXXTXyLHCIs9K7TCXRVRoXtx9Wf_OXhoWwQuw1T5jX998QK0DGtCc90qEz8ZkF7npUVGCsBAHMTGwbt78QNgxCHeUsk3ZbAa5XDX3kEE6NW9wzNrfn1GebjS-xctV87gYZjXVsGaq7VlIuodXwQH8cPiMMKIlI8Irj0ys6WSdzXK_TjfhZcG9P_veaTT5u2MAQ3hbSFDC9dt2vYxnQt1jHcuVkagaHGyJzclKFPhiUWDiygvRcisBZUqn871L_4g1k0Tas_hIrVirAyl7dujFPFHMLHe_wfSjk3_XhbAx6YQsUVUCIMpa9w-MhUBsPwIar3bBc3mrZ0s-o3oiyM4NztnxY42hjnSc3bByVYCzmdxbk-rYy2ztoRO3qkuDsuTXEwVkKP-mrTe_nYydt7_ceK_dZibpB5aDgF-Mb3_BhQSWSEib-bAzsgynOWXMXqcxgNDkuizCx7h8uIdBgXfSHjKDodfux8FJn2JY72-bJTpwlufIajwfCWBnOcVqsr_y5Enhou2FdZThs2h3nMh1zw_lV3QMECIEYTAqmop5ltt_GRqGhtCHVtMvLorrKbrXqDGN56BZmzzW5NM4F1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFhXtiEz4eqX3sV9uDHgAEhR6D86RLIrcvFKxEfGHxwmuwkfSIh82y4fPGfZYBCwc4EgHHZpp6pv6yzDmhm672WUPBSWVo8QqTZVZOyWkZwdetx32iXW9WmUW5gqvgzE1R0eCMhitDxxvUjhLRo7TiI7SiFHWkhAgIOg-lDaa_mfhv5MuPa0z2yBus9xY6zk0CwlzewgEEVWyiR-LX5gD7ts7_397yecAA7Oh_OKMZWw2VmpVOkZ8fuvQUB76R0gF820WH2S9F2OPLR9-db90ImwQe1t9WuOXg15Nfg_kPpaYRgHsgVIQYPu3VSL4UcG3PKnuQwuKAh-J-Q6KNkRWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL3pPCwDHwSxvFLIw01JyH_3Af4JyrPzFSvNIgh8C5sH9zD-BNcN4jI_G2vW0TQ8Q5-L8KeQuHkm30iZ29BSj2aT7r4O87nWNdOx0Ms3Cnn9FDZ6mEgPpmfddj-J6wf6T_Zqa4qTiO3Vcwo7Iy0Dmb99tE1J0vxzNbXLzFWWnCshAQP_5jDCIlVUeehopMq5EhRmvChwxCaz8v-SF_2S7RJMeTgn_D8SdJ5qHp0WAKcv3mQms8ocjSWS5fNqRWcv-az3xhp67IgBuBlMXytmLq6-3iHGwcI33v_H2Ijbt9LnbSAJhs0MRNlreIdeI9yrOvStBN4H1yfOrXyesj8dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UflJ_XVJiWfkA7wJoJSGM37OIgCBRulJI_p4G0Ex13kwXR659Su70HJF_5E-i7uM6JqdVsu87QwZmtyDai2XpIuzX00vUax40v4Aj_AHkRtAZSQxhiI9F04YzbeuorBuZXNR1nm7QApHQpNqiuH_rd6V6lCVMdHhgXtMZkx5Xgz4eEINPS0rba0VxkBLL09t2Wj4ka0pg7kbA4z57E6fXEQxquWSAKBmp63ztcEfFVPM-kIaq8ftOU_lGhquKuGMtT4Lp0VZE4INzBpsQpcNQLNN0BHtYSEOv1ZtoSPL0iXH7XewqQX9ID9SDP0ga5aq7ISb0cmgITy4LbZeljyKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkDuFYlGVKnThqoe2eszqjDQMrh-ahQOE3mcvrNlVjg-34wkj9PS9Ujo-W8vUrxa7zeIqAVDNReOFKIJCfn-5vqFknOMNTtkML8OiorJR9KtYblgIPLTAgzBZAqdgbWaNf-n4FK4Bb3YvlR14qAOx9GJX9-WITwIK5ppKWFxVm8Cy7WNxL3Lj7fZeJaiVH7a1wSaCCHPcznavB1n0v855sGuKIgayDMtialyUXzL3xP3JXSaliJYw0llVk2ojGrHxkri6tgqRL8AbGUKSL9sQ7SGMQeoIKAgDBCgy-y_1gixjU5qg4TqmfRxfFE8IaWv-GPgJOuqbP43zsYapGJmVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBvzsmw7JAYeVBEb777ual_Pys9bN5SuuXoCYvHoRzkw2YszmLMzK0zRGBRUzpS5-3IfpFbmEPBbTOtbuDcdE1vcr6gd_1bl4aYlU0sIWfSOz5sx0MC0JSR7tv54Q4094d1g8knboy0wdHvomwBo9tXeBgbITFTwCwZ9cA7KbPuFsrqgCRi-d1ZLfc_BriAdAl2hOCLht5tXcujssuJlmxCT3XtKUV3KydEamF4JhFLQRzDT1oWexGhVmBIioVIFQ0YyozgmVhJ7EdmFaXdAL2CK152foc5J-4XsjgPoCAfHJKSeaURG50N1i8JnocfgGKY4kS6GG5S66GfSjT9CsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRn-x5jGh910YplX2A7CkOcI1f9XFJBXZDZpLjyxngzsj6G6R6AUmMyWEtvbtDUnroJ1oMsVy6vxYnbZpisYS_uh8uyvzLXINfB2PI2fpMxDCZibN3WZEdy4KHN4VAVT-FJqFd3LbjcJs2S0EAlMB6khI8He93KcM3TnzXAXyZZfjF132-w4J4zBacZhPN5Ka_aGXxDFYStahP68eB5NQHcYGKqoXp94_ZMgWPvpdZC7XcNy2DdyAwbr1IWlNCuqq4INpVCfTJTXWI128C6SKCW25vkBRcgNSmN040BSpvev0O5GRuKmRETHR0yXeO0YyQdvP2QQF7lgqL3fGmKL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHIj8lGWTrXRrwBbC-ijCSgmwK-e6CfGZ1fOCejSB__CJDZFuJtFkSeyWb846o94IvIaFuKeP9efoPjyykKhUqZPA_KxEIS76Z58vo8fUafQ4keXeYhlL2S5nMtxl_k72zcE3c86qbHz5RysaJ5GpBgOXPEq2z_vdq4198b7rdOz2WH3DVWyoAVX9q9qUbhbVlOcCYLHh-VMbSjY0YKznN3Fv0uFSTFdHLaJahhhSF3lHwMBuGg2uVvq9w2vqFhl9YwIr9SSm_uFGBy6cjnLIi_E_Zx5gn3v2v-f4fCl1KVStY75X_q0O0EGjZBuwgHC2U1DHxpE18kElXj-xAFWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csyfNVcX2tku19YwlLY7V5a2wMgLpzW70aqJEhN52YoQWc0R2gVCCcQd5ZpfLA1qkBLs-lzmOwyCugyxP5vjtk-I_kL70F6xpfn4G7_Ah56jP7VBa1nHWQjhK1aKg3PFbuv2M3woGHQ5CfFNcmmXmJbrZ03vZq2hdB7VeC6-f2BAMigvvKq9xIUeOiopHHYthOFxEkNOJ1J2dEgSR1URROuaNlKToisbwE-Sh_Fya3SbCab6a93ehUF51UH2p3C-zwQaPVLJ4SjKa6Q76lC6NrWHPBDcxN6bUY26RtAoIctmNONSzxyRVS80b1UEDf2G-n50mAQa-K3mGe2ltVlsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
