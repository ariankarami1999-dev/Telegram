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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 13:12:49</div>
<hr>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve1t-OI_HZm5G3EVaBeezMQ24iR5Nd0qw0vbsHCvfmWTZRHCrDaMImIspzhSk28ijOc4nNKXzdTmQ6OlEse1PSN74-YdIUpqwdMH-QLh-MvUFgZRb_i86H6tqawRfObE0puD_kEjG8ysIvNPEX2oKYEVRTQLGBkE0W0_z_B9xLXxE8RE1r8L0-5vpX5DcxOILeZkNZoBml8s7vmvFvTgk4TUw4X1xIIAQuVbjq5-KVi3u4B9YCpqsw6XL-ZY2NHrMXuOF6NRrw1l1xMaAxHT3OkRknyJxLxuDZYwuAiIVutOVdgPFyVPUyJXxDo3H_GHZLwp_Y-y9Kur5UsZ5n-ZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn4pUQAh_qhz1yRM13i_qVdoaTkJxBoUJw057gC7YUmLCfjv6_PHFKNIhIoXA7riFwDtlQoEPdrenuZxa6srSbgyBtHqaVeort49dNn-de-MNnbe_Ww_1jg-TaemTeiUw8nh7dXXk_sprOXHvlaVuPj8fs2SAfc-8_NeoHPbqdjkktgU0eMxCYjLFZor1qauRKScsHwrpApfQ695HNyeMrKD_lSNfksW7GaGth-bc-R8MRa1mLa-TnIM3sF4viraOTkMTMofhxcL4XGSMwTzu2SuSbbIVpq68dBNcXmRb-eXVcZP1RqXWeTZvocINaMrAOAFd7FgyTY08g4dqZD7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YW9SuNGfEb0Nz04W31WoC4GM6gQP43LokDjHtEMD-zSJ3xAYeNs-G41tqt5XnfRzGWL9AwxTge2uuVUWf7AZ0hIczIYOgb362HdOtNetw3WRWkRh6CsAXrDYx-lEk4haBb_bz8t1OBa8Sz7-9mV20Y7O28kD78ErFtIgn_Kc437MJOCyD27TIfskHDca3PdMhjf-YP3c0Rf4tBLcDcpNPWhjiLAom4j42IsC9y-82LENWUSkc5oqDo0Rbaqnb7BnFmAh6maRDaSZAtujHJN6nDMmYPG9VtB3U3_CxNAAQjGqB6WKDMVAiTWvrfUCFdrIofrIloE-xkewqsKbXQm19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcVnPfCf8AoeTkqs-Cj0yyvXKUaSKlmvmGINZoxkj2T1vDjuIOI7gdkjShkJQp50hV4lM477HZiF22vKjy2qa6Vmy_zlKKeiuF4CA28tv5gWVz7gCNzmvydfVp1qOvl2OUnI0FBO0sXlfRHHNXHJ2k2wr3wxoyuOe-KFlrJDYgpDIlRuEPY4iGNo5fHKvnCv6YIV7z-ruf8YW0mIYsPSCYC3FUsjJXn7ckFQ4Qa58YFePdof5xVd8Hpr_l9F5anT10c1UBgl0CJoxwRNEVE-o-n9i2aXz-0jeD76aLI03AYpLnE2pSl1zOf-QS9VvuhhWJ3X96PV74fsQDifhHTC2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=RKKHOdIWSr7RJsq2mRWEeybL1e9uDvoayaEMeV5gzcZ7EKG-gUBytg7rtAWg56NlYp_NGwZwPHi8DJXNA8Af7NO_uaYrRB8LGGBJKcqNTybrLXZ3DKAFb-wbFGAcluHL-tIUFUnLhjUFUfDiDKNwucRXug_GxcVbTwyfsF5NIccDNYtevj9gISzBDIhEnv4PQV1IOqmUcj-k-T0FqtXjz74JY-auFRBvh-3j6sEXXuehj2HJH1yCtUj4HZsgoAvqgTJ4hB_0AUm5XzOFfQqZ9fjVS4xF_v0DIsa0E_MV7zgpkgPSEYn4digh23zsEZRpE0JBnPUgIjbw9iwZwkQO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=RKKHOdIWSr7RJsq2mRWEeybL1e9uDvoayaEMeV5gzcZ7EKG-gUBytg7rtAWg56NlYp_NGwZwPHi8DJXNA8Af7NO_uaYrRB8LGGBJKcqNTybrLXZ3DKAFb-wbFGAcluHL-tIUFUnLhjUFUfDiDKNwucRXug_GxcVbTwyfsF5NIccDNYtevj9gISzBDIhEnv4PQV1IOqmUcj-k-T0FqtXjz74JY-auFRBvh-3j6sEXXuehj2HJH1yCtUj4HZsgoAvqgTJ4hB_0AUm5XzOFfQqZ9fjVS4xF_v0DIsa0E_MV7zgpkgPSEYn4digh23zsEZRpE0JBnPUgIjbw9iwZwkQO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsvmeNvCzeUAslGMTOkjRjDMuYtLFxmn8rZGi4wq6qrRcEWuiOmATEJYfkzrKQtaBw6-KSc8VlpStwLYNN4T3A9556XFHENwsba6rh1bNiG1Q7sqbbQEkjmhGZiKdbY77939h_o6FaCBEguwSKesuDXJyUNGs0ulYxi2srDJ3y_mBzb3QxfJiNEBTYzY10ZHrIAU7fRxh0svdFQB9bydGcKe4hzG3clPy4e5--b9AMKnoYADWKGxRNEo3U52OfAZkMtf4YmZLgcEAoJv37bxtg-CY1Y4uf0vnC3EH4E6ZkoLIsZJlL5WNGfNjEvB9ap59c4nxWcfUkxdXbzfuBUK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjpwFCEUGqG2K891Q3q-lObzyR729XQjUPZVTcxvg5yVk3KZuITqVdy46vDqofCD4hm_Oyo481UxF2M6SsPzimxl--QthWFh8xONZQVU0gGAsC5OxKxGqievzkSBy_0uTL_D9iszLDnA8kpih4WH-5pstiDnTC9lGQ6YhWUg65gK-SFs6bucyRpEsiiy0a06n1dfcFH0C3Nsvg-0chhITMvwJHCGICjOy169iFjTVPeRq05cvmckW5ipTKGCBbXChpwDtIBaieLbmMWpL7978TWtq9Or0mR597oT41Rl46Ne-_gslaO3AGvCrw3gNCzpVOhNoBftfikHIaNIP1TXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS5jr9TXz-BZNThv0aD8vhyMnjAWJFV_caWU2CFXDIDyUi85510Ml59JH5Q4nWFfN-z4_S_3wwWn2Fl9K1j34cHMMLPWAUmy5qS-UjQFO2HAxBEZkEDZquIlxaemhadIPLihzgPS4bcmV7m_KC2poqeON022dZZjOGE9rvfCr8TLYlnZjh67ALR1Wq19rRiYikX_bqErlOJABZcgjOflwS8d4Nh-FgeHlmOeHxCJqlFl8u1mbsWhF2aPc5KYHY_yfVgWsxOTEvuxbQIJs6RWl5YTJONHTE5shAslnuL9pO642xKXPUzQ-6xQFKvqdVwexL-qgBc4GIbQ3hRdNLxK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfrZGxn8WhUXslglsgCgjVMCQr1MGCB5CH9X54CAJb-sogVXf1kUwbhyvxK7aPwVDccux9wPrRe1DqItV5Z2__rRSWBuxm0iFPbNYVseyfKZmEmwdAFZbvfInqwGpwn1ehCdYnxUIQqvHrp5-WTJ7cHVokfBdzaigG-OFaKHnwgQm2RbKYVFPeYfGcFZwNp2lQY3rP1luTTVxpZRIbOiAabvJyY7T74S-X4Y86VcWoUXm-pygi7F8q93616qws_35C3c4dtPViMv3dtBsW09mJW9hCCJYYZr889mIoCldLe_ppVZxA5Sqe_vwSUnXycs_EKyKev_3OfBkpIsUTZ65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=am78DGyLrFNFBw_08MHjqeuUqLVR8DYRfxIGuG1faOhvMsSCXUqDrN7F69r0yuXQUkZApSt2UWZGB4dXhVj_Vwpatr8aovlBStK7HyQebL9cbVD4sJaFxjhts1gAxyPeEzBJ0k1ZsapcoiG_PQaIju7XA1gKn40jt41V3M4FY6RIt3xPKY4uwGZCH7jZz7UdNIWqye079_jQUeCAEqTqNh-RggfBXEHAiYRcnEIg_OeiUvoMAuMX9HkNiVprK-Pbni7oM2PPpHbFuIF7jGeANj4q7HkDJxW3JWHMsE0Jl296eygbsaWMd49AMb_buUiNVMvDV5Bl7M7MTH4lSxiWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=am78DGyLrFNFBw_08MHjqeuUqLVR8DYRfxIGuG1faOhvMsSCXUqDrN7F69r0yuXQUkZApSt2UWZGB4dXhVj_Vwpatr8aovlBStK7HyQebL9cbVD4sJaFxjhts1gAxyPeEzBJ0k1ZsapcoiG_PQaIju7XA1gKn40jt41V3M4FY6RIt3xPKY4uwGZCH7jZz7UdNIWqye079_jQUeCAEqTqNh-RggfBXEHAiYRcnEIg_OeiUvoMAuMX9HkNiVprK-Pbni7oM2PPpHbFuIF7jGeANj4q7HkDJxW3JWHMsE0Jl296eygbsaWMd49AMb_buUiNVMvDV5Bl7M7MTH4lSxiWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb90mKWJXFvA4xEWsH01HhGg-PeCE01raLzOkZMHvvslXCsw9Zd_0U7TDN3m3HzRD7K-XBE7AoAd-q2dCO6EzvrySmUwmMER_DdiO0u1vej-i-JCWH1Rvt_OaXm_0AfEvTN1UCtheZfwHs-rc_CBnLx12D6V2MZ1vGfsBpnijBow3yzQSsg2v1G7222PmPW_4-Y4D05XXcIoeK25qZeF0g3yS7lDRytO4AozWmF2vjrr9kWb9NHF6DMm5u7X7EtGS8uDEmnwMTFlLk9igI55UlLT5uFT60GYS9VuBgBb2sFWMdLFods8H7mquw3IPMVXycg_ua-sFpASyG0uyh3T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igZLit5pizLp9xSIxK5j6B5jZ2ZzkmBhhYUFo1oHltrFCprfcQDBaWUpIVHka0-V1OO2FgIO36BVqjvGtFApTTHz6y9zyammk6PAPjti4x5M6-Au_5o9SDdBuES-I4aDvbh_hCbgtxpMLJNnMwfimjSrFy0_-_E-jAE1XJbvb-qFhif60kN5pzbS4AnUtmAISbjNY4zanY_fydhb9m2-t9zfxVbwX2EDh2VtxutN29JlCr1y5zdsNUpvnGyNATexILbgObdlSaO5l6Jijdu1eSlOVwudN2RSB7J6-Tm6fXDJmps-BHPW-IZfobPb5p_HwBxJNkZ8yOvXBrCxACbYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=pzpTLBtIyCIPebZPcUpyZxT_elwUdiHz4Jll41uPlFKAoF54iiuoslcdd3EwSTvejzR0nrg-8i4bdup4OtAcnB6WgsB7LPtn8KV7mcrtwVxiaa_YwnuP9cNeu7aMPmDDvGgBwzExdyAxJtEqclZVIYkV9SwpizicWrWV1JOJ_oqYeFGh6A5ahJx2l3no0a755skP1johYh3dLQkbiLY-GY4m6_69fOfO7dW6KrMRUusZtfoWUsriMEHT9e8MBYF4Gq0___8lHclr4oKwHZNQNvgVH7E7UQXxbTdRfctIzCQfodEgIQ5MQ0a1owU5v3qQ1dRkX1YOf9kq5ugWgaFOog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=pzpTLBtIyCIPebZPcUpyZxT_elwUdiHz4Jll41uPlFKAoF54iiuoslcdd3EwSTvejzR0nrg-8i4bdup4OtAcnB6WgsB7LPtn8KV7mcrtwVxiaa_YwnuP9cNeu7aMPmDDvGgBwzExdyAxJtEqclZVIYkV9SwpizicWrWV1JOJ_oqYeFGh6A5ahJx2l3no0a755skP1johYh3dLQkbiLY-GY4m6_69fOfO7dW6KrMRUusZtfoWUsriMEHT9e8MBYF4Gq0___8lHclr4oKwHZNQNvgVH7E7UQXxbTdRfctIzCQfodEgIQ5MQ0a1owU5v3qQ1dRkX1YOf9kq5ugWgaFOog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNZnsSWcYDLjNLErsV5T8EOXccfUb-EaSsx1JWp0LbmCtTE-zhDgkWFWFcwNqiJFGBRc6W6wIL6-bNGEp4_R5U7WsNNvLJEGBDW95sCUODnyDXfggYIGUpW7nONOdvJ2qYe7yob7sQrMRM7Agk_EjQVjCkbMJ0LwY49UHeHzzH93NV3MwRllIHwceOAC6KsEjj-DwZ4SAPZ5bW9NsjJ97NNlisaLJ144eD-G8BpJXVZiVWegWrKFF8a6CnGZ2yB6Q4OH1vzp_dBua5uKen3pcxBMcJmX8HPOYvkOiaR4ldXk_4sPs1_PuSz00Asho-UJ1bsS5Yyf32rd95a57L1P7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=gfR-ChQh0ycUUvTwdRE2b-M5_DDQRmDG2U4QMZtZIs5B6c057w1YR0c-ywxxo_dPRQ42TvqcZI-aoaXFvzUX1EOA-yUAQ3e1jjKOaQC4nkp8ELHccRfPFLh53-abeGL1AbuAvV44WupI7cd4VxmGMUtICuxNVCijJn2rJUap-BhoPleYcfbVhjVthVpc6J5AIOmRmfa3tQY4FjJwtNYfL8faRsWRYPdfu9q6TFLYTky4zqASQ0Zp4nqKCtM08hnAOW_R6ocJ0yyHzDvUd4wZNZPdaaQTIkSw2JNmosz7XOVTGRN3mU1tcOjSIxdzjdofE-m9dRZqALLeOIcLRD9olQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=gfR-ChQh0ycUUvTwdRE2b-M5_DDQRmDG2U4QMZtZIs5B6c057w1YR0c-ywxxo_dPRQ42TvqcZI-aoaXFvzUX1EOA-yUAQ3e1jjKOaQC4nkp8ELHccRfPFLh53-abeGL1AbuAvV44WupI7cd4VxmGMUtICuxNVCijJn2rJUap-BhoPleYcfbVhjVthVpc6J5AIOmRmfa3tQY4FjJwtNYfL8faRsWRYPdfu9q6TFLYTky4zqASQ0Zp4nqKCtM08hnAOW_R6ocJ0yyHzDvUd4wZNZPdaaQTIkSw2JNmosz7XOVTGRN3mU1tcOjSIxdzjdofE-m9dRZqALLeOIcLRD9olQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=opqjJdlFoYhLNfljg6IiMyhk7__2BpfZL01lSMFBORWvyUNktEaXQDsljPdCDHkDcDp5-vvGSoR-IsM1411hONIueXETi-mTeXvyrNhKxxBrT4v4uR4Tyg4p5rqC471O6_ZuTobrrwNiHWi6Kp1otvBRE6xi6Eo6-ae08tn-Qx3VDhM2BHtYvqqtL0P-mcSkKgp8pU1RxcWNL-5Ljt3BLDCnf0CyZkMWHlZJtev5STwCyyraiqmri4ggN6gqI8qa7LetjaXubIU1K8_qHWnFNra_zhHEeq4Py20CWzh-XizcIhuFdvrw2Vn-2GBf05Msi_oB-ay0x29PGuD09eWrTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=opqjJdlFoYhLNfljg6IiMyhk7__2BpfZL01lSMFBORWvyUNktEaXQDsljPdCDHkDcDp5-vvGSoR-IsM1411hONIueXETi-mTeXvyrNhKxxBrT4v4uR4Tyg4p5rqC471O6_ZuTobrrwNiHWi6Kp1otvBRE6xi6Eo6-ae08tn-Qx3VDhM2BHtYvqqtL0P-mcSkKgp8pU1RxcWNL-5Ljt3BLDCnf0CyZkMWHlZJtev5STwCyyraiqmri4ggN6gqI8qa7LetjaXubIU1K8_qHWnFNra_zhHEeq4Py20CWzh-XizcIhuFdvrw2Vn-2GBf05Msi_oB-ay0x29PGuD09eWrTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=JsvoPfcBQ07uZi6KM4EXo7vPZr0QZc56w7GLFbWOrNo8Rf3Q7yTOxNg2eSlvWwmopmGJhxV0gD2pZrwm4nkgIgni8X1LK5sfK6AGB7y6TnOt4MMhAAR3wVTpEWY6xue-6r5_g5XO7wgo6cLVEGLicNtK1IudKHPeUXELb5Wx4YDjoauxUeBI2nGbxaeFJhprzc2nJoAxpf1cF0LVqO83cd4cT7Wi8gd_ON-npu8BYBgL1lRBz9-5PCT6TzGo-hJZn2ehrFNXynp8-XP8dm8KYV2X4FNHKa9G3JSgXaxmrhK8zhshuku9Ybozp0KeoW7bMn0zNY7tdTb0Ih8bE0owLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=JsvoPfcBQ07uZi6KM4EXo7vPZr0QZc56w7GLFbWOrNo8Rf3Q7yTOxNg2eSlvWwmopmGJhxV0gD2pZrwm4nkgIgni8X1LK5sfK6AGB7y6TnOt4MMhAAR3wVTpEWY6xue-6r5_g5XO7wgo6cLVEGLicNtK1IudKHPeUXELb5Wx4YDjoauxUeBI2nGbxaeFJhprzc2nJoAxpf1cF0LVqO83cd4cT7Wi8gd_ON-npu8BYBgL1lRBz9-5PCT6TzGo-hJZn2ehrFNXynp8-XP8dm8KYV2X4FNHKa9G3JSgXaxmrhK8zhshuku9Ybozp0KeoW7bMn0zNY7tdTb0Ih8bE0owLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=XV4RfQVfzO1wDVUFTnWb1WZnh5SmqPEAm7uOk37awSl3EBXO8yhtqg2hun-VeHBjpuLOd8_RLFsKZGnp8PpYhHs8sEHI0QeowZFFM5f-uexH4WD-IXrD97uf4H5Du_0gjLRMziRHGFLNqHA3iwYLqQ3PhN_iNCEfwAyXpuSQjWiONdxFyAxHoOWixg8viNaiSxxazFlzaOdsfv0FiNNQPAs3wG3R0ZgMhwa45esiGxeVk6BWySt-I2ZMxKpEUJPF9IiVQjbtyll_JekMixBo3XM8eBBRNIU4Whd-ML7M9tZbeXnEorRDFem-Y_6GTF5F9qvIEkYoX_6IC3uaj8IEwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=XV4RfQVfzO1wDVUFTnWb1WZnh5SmqPEAm7uOk37awSl3EBXO8yhtqg2hun-VeHBjpuLOd8_RLFsKZGnp8PpYhHs8sEHI0QeowZFFM5f-uexH4WD-IXrD97uf4H5Du_0gjLRMziRHGFLNqHA3iwYLqQ3PhN_iNCEfwAyXpuSQjWiONdxFyAxHoOWixg8viNaiSxxazFlzaOdsfv0FiNNQPAs3wG3R0ZgMhwa45esiGxeVk6BWySt-I2ZMxKpEUJPF9IiVQjbtyll_JekMixBo3XM8eBBRNIU4Whd-ML7M9tZbeXnEorRDFem-Y_6GTF5F9qvIEkYoX_6IC3uaj8IEwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9I76Dx9TUrKrHfRnxBMZ4SqpOmv_DbInTk_kFNNLIbwpL88n8lkX3EFlB29elpfWuqe74B_4tEqK6Rd3i_HiW0pR7wGquHh-1ibvIRX7gT7j6EAWiHBTO2dToRqFbnpA7kdepAcc7F1HpH3Wpl3kieXglvMW21vRQCbRiahl4AWZIEayP6897TlxinqTW53GkoOiqN41dbeUfe_KvtodamU3gr1-K1lNvZb5uFSpfEjKTA95raUJiqN0ZBrzVXnRKAPt3p5KCYZ6ykq5kvLSBN2RBL9pj7WbvlKzYx1fQiuBUNnEcsyp0qj-VFG80_IG7rsQz2_LVGuZMWM_zU7jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEspqlsxk8e2jGzXKHMSudLsa2iz_JxaLGjJCb0MoHCCaiCDg069wrIrZU7f-3mFqVz3K7YyOpMi53vHRtza3hM4rin9I6AmRQhJjnuwMLiDGwVULvVOrJxe-vmBiV_8r5VAM3NqRR5Y_MocZ4ypwDfpxij1hh_binR9GubZGauBBkJ-yFTKRF_EUMWm-57NBjqyqqtCIZ5BlAOTM-0JeN8ZPZKF6wD_LBWIxTEMcFIKee5Hhq_aZOurDIUzYGhM64sgMlGZzuWOB01dXfMjclqDzvhGFD8FpaLCSUI_Td5M0mIOwuczL1suCHTioCu3ri7smf5gwZmChDGQjAe30A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcoV0ZGU9jcnrKhF9M6G2WUVvNXnqCSiunFvVsfdFadVnuACPBkq5oL7ot6HAEKISj9l1RNkBONCeN3WRWzsmvOzREggjuthDZvxa-MH9FOC-Z6LB_GFFWwkLlLSsM0mGfdX89EoCDOVW9zQGWO3R0eh45lYUV044X-8DryvtyKLv2jqD-BaJUO9Yq8nFwmfVhfPCBKfK8lG4khWFnD4ZvXaECaeb6Zozm0c-OIz5bRBNRXl8W8thi2knuVEzPoLkqBG5qYQef1xjk5zo67Bqp4zLFGzz5JTA25ZwGES2rl1mofDvNWt4Wa5A3obXg7mE1iVzGWeZkW2wQbzMoiLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXk8R-W4G8fUgZqAtsk21hD6UGFdM8vRY2gM8Vgy_DPYvzJv5mTsiU_zxkXLteLrMYBp0bet-9AW55giLWG8YVYXFLe5YWOqmNfweuiMS8qI3ZanRwq-CWEj73o-yhIwFK8qjq1OLMvn6ffVWdyk4PLW3QjflokZoa0fNgq4a3DU0EqOK3Y7OSFirxB0sLIxKmrm6WO7oZU0d70Wgnvg82myb9LPN_MqN3Yn9inZTia0Ck_mYfGu0_XpJhNHvmmFJLMSngd_11sCvNBtXoa3BOHskAbNNZ4cNWdYRC_eHGYdsI0rJP-triTJpROy3aaSVZ-fvg9x5rGmttKi9OfouA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=nS0qPdglwOS4RI8b8UqB-pOzTcRGRvdJ9dwgJJpJjCk2y2-Ggk2aILZajuf0BIrV2PiqlCa3CnZT-68fWyDJULUvMr1tMf1xNnTfOJVXKGlClvZKXGnPR-owQBPfS3ejJ7OwJvKg2KtQO3DyvlqTltAo1--CwHZWtLnk4TRBq_IxnHdN8RFDJkVPZiDCWN4ZMjiwYPFcM04NMwca_EeXH0ge_APfqu9bNYTcGlvjLKfU1axJ-faq3WjEX3wgiho_gDe8fLqV1VUTptzWwe595_9MtpSVUn4QrExXDbQQSD0W1LRBuUUxXgUo88mTckKDC92veu-ssPVJXpP1-dKsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=nS0qPdglwOS4RI8b8UqB-pOzTcRGRvdJ9dwgJJpJjCk2y2-Ggk2aILZajuf0BIrV2PiqlCa3CnZT-68fWyDJULUvMr1tMf1xNnTfOJVXKGlClvZKXGnPR-owQBPfS3ejJ7OwJvKg2KtQO3DyvlqTltAo1--CwHZWtLnk4TRBq_IxnHdN8RFDJkVPZiDCWN4ZMjiwYPFcM04NMwca_EeXH0ge_APfqu9bNYTcGlvjLKfU1axJ-faq3WjEX3wgiho_gDe8fLqV1VUTptzWwe595_9MtpSVUn4QrExXDbQQSD0W1LRBuUUxXgUo88mTckKDC92veu-ssPVJXpP1-dKsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=DkKg3GA_mC5giC0JIkT6e0EocIR4EyxYm5jiymhJK_d188-0_ZU42utWgZpjRu9nVsx-2GYiXSmWui4nbNGDSoAuzIorTYfzn--6lyhMCiikqhq0bNybVuShk6xjoy0kj2nKieT2qPlZ2dzM7ZvlBwiodulSjaedMDWsb_zbv-9Um05wxzK2F1m2UzZYOUUGtuphWSeDPxMySOxsZS3EuFGaVALjfMlxjVoZqHsQrFtKo4HohErglkCYTRlg8w5dgVJ2eOPXcmatHVs8AeF82gEJdWYR-6MJ07wJ7UrEwF4rbygcPTWTP60BerRG_nSEit5085FC24oW8By8KIYeig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=DkKg3GA_mC5giC0JIkT6e0EocIR4EyxYm5jiymhJK_d188-0_ZU42utWgZpjRu9nVsx-2GYiXSmWui4nbNGDSoAuzIorTYfzn--6lyhMCiikqhq0bNybVuShk6xjoy0kj2nKieT2qPlZ2dzM7ZvlBwiodulSjaedMDWsb_zbv-9Um05wxzK2F1m2UzZYOUUGtuphWSeDPxMySOxsZS3EuFGaVALjfMlxjVoZqHsQrFtKo4HohErglkCYTRlg8w5dgVJ2eOPXcmatHVs8AeF82gEJdWYR-6MJ07wJ7UrEwF4rbygcPTWTP60BerRG_nSEit5085FC24oW8By8KIYeig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Mam5WZ3EkKr4pg-iFhUNmOIlWfdhCv7mWoSDstLilNVO5JjHf-80Dpj0V9y95LHTFImsbBFLQj75s_REPycDQ0KHt7dLxKqffwXuVsXpw_pe5rngDUj_Cg7EUHFWA4qPO8wwPeb1whWnADgy3gZcHMwMBo1RY63tlSOXpupyl6MWhZ92cXKNSPaXHOmvElcNRLdFdipgJdhsOkBYQWgqd_dHsSEnsAOehGsR5PzQ7nvj8r5hWx6DQ76seZD4iodKVgBS55ARyEA02U2WrV-zLLzvjr5weDYn-VQKSnaMY2XL67iUbspTdWQSoOzf7v_JzqaUvHF81Y_thhsOztKuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Mam5WZ3EkKr4pg-iFhUNmOIlWfdhCv7mWoSDstLilNVO5JjHf-80Dpj0V9y95LHTFImsbBFLQj75s_REPycDQ0KHt7dLxKqffwXuVsXpw_pe5rngDUj_Cg7EUHFWA4qPO8wwPeb1whWnADgy3gZcHMwMBo1RY63tlSOXpupyl6MWhZ92cXKNSPaXHOmvElcNRLdFdipgJdhsOkBYQWgqd_dHsSEnsAOehGsR5PzQ7nvj8r5hWx6DQ76seZD4iodKVgBS55ARyEA02U2WrV-zLLzvjr5weDYn-VQKSnaMY2XL67iUbspTdWQSoOzf7v_JzqaUvHF81Y_thhsOztKuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATZeZ9jjWo_lZWVE_hEdAMexxmJ_kqrr1CW39TpK2rGLVJpb1r5efjtlovkRhMD7Xdbb6NGZxJB7dY0zjRXInY8RM4nRiyFJJTl2j1kdQShHYsVhhvBLvO4KwlLPSsHaEE4LkUTEZ26yQBmgv4f-JAX1_Cyc_zY7ba24kXKfaSpdi43uAg5sCR54gpmlxsAa8bgsUYI-f-7Ve687M_mtdUXgmt-POA-Gw4R1k6h_L5oUDBi4-68X7hRtV0hjxTFzUKleEnOSKeesmW61sQ2eQK_bArAMSpYYdNTY7u1alTfo6XYCkGJJbZw6fA1R-Qq2-3VFvkdG1A6ndvjmOQaJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=SL94vK9FDYUKZZs8OBkLpadlZP7M9BrQFbRTPAjwNxppFa-BdPVLJRM3EQIcIxumW_VH4QRUpGkHqNdS-bo2nXGcBxHnoUcaGldClhpPvk-kZTl0idpBF8-DM_RXSzOCJ2T5sUf4YSUESWK6SmExzCaOsHfYrf9GwcHf762dWHehS4axhGcTt_g6-opxKpoISQBKgTXk8N7Csf-TdSmFVs6QeRheN45dyRxsntOQ434dljMm6eV7LnCCL46sOfHovXox0QoHEDamQcP_NaKZ_FJQuy2xFaZ4YdQZf4eIhNuCms_BjQeu1DSaPnAWxHC7uBtcZLc4hqeVKNJ4eFMs0rdU7wuQj1mJ6MqJJ-1VRJXyNnAT70C-h46Hayr3fPN_LL3cV_ylMODN4qQ4Go1bcdIZImQUjjfqPnwg0jse7TyHJj1OiB60j9Brk8Wm5tnfr2AySgdm8FLgmRHUJNITvApehOOLdUcDCD19pJJzSKRlixoHcIMt_Kz_-xMu9mGeLNbadL6GIyrJqxoT2z_i5RMaA8sRE00ORLrHCuLtvwp9ymufTN3bzcO1dQYaGtrzfmSZrGPdDMvxUhIku3bLzvA-dGoZR81RA1a9KeGbOPYFIJG_AJGdJgo8k_jwH6gWJ0vDzUUe12IH06V9uHYGrbf5Go5OjvPK6DiglkTv_oM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=SL94vK9FDYUKZZs8OBkLpadlZP7M9BrQFbRTPAjwNxppFa-BdPVLJRM3EQIcIxumW_VH4QRUpGkHqNdS-bo2nXGcBxHnoUcaGldClhpPvk-kZTl0idpBF8-DM_RXSzOCJ2T5sUf4YSUESWK6SmExzCaOsHfYrf9GwcHf762dWHehS4axhGcTt_g6-opxKpoISQBKgTXk8N7Csf-TdSmFVs6QeRheN45dyRxsntOQ434dljMm6eV7LnCCL46sOfHovXox0QoHEDamQcP_NaKZ_FJQuy2xFaZ4YdQZf4eIhNuCms_BjQeu1DSaPnAWxHC7uBtcZLc4hqeVKNJ4eFMs0rdU7wuQj1mJ6MqJJ-1VRJXyNnAT70C-h46Hayr3fPN_LL3cV_ylMODN4qQ4Go1bcdIZImQUjjfqPnwg0jse7TyHJj1OiB60j9Brk8Wm5tnfr2AySgdm8FLgmRHUJNITvApehOOLdUcDCD19pJJzSKRlixoHcIMt_Kz_-xMu9mGeLNbadL6GIyrJqxoT2z_i5RMaA8sRE00ORLrHCuLtvwp9ymufTN3bzcO1dQYaGtrzfmSZrGPdDMvxUhIku3bLzvA-dGoZR81RA1a9KeGbOPYFIJG_AJGdJgo8k_jwH6gWJ0vDzUUe12IH06V9uHYGrbf5Go5OjvPK6DiglkTv_oM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUDtIp2G8tMZEb0kI_gi4UrPzSROJFYO32J-ZCZVxBjRYIlA7VOzv_UfI1upf6g6dxIXKW3ixPd-3oYlVw74TTSXApPoDPSrN8edPUoF9W7DiSYHHsKgeD__ZXSEfByHNRkJYngytQ4ZS22C0_wH0ODmew4sHdzLIgwfnIib2A9LEmZ0b2-TMtMC-V3Dl4QvbTBsLIeuZalWBZ780BGiZWAHVPFMw-rk1t8z61dVmi1XVIM5cCGTpcDUHwK1BZ4QNobMEhXojgj-RjHklnmbao6-sg90iTb9R0NWLj3hPj0LkrBoG3EGwBnUgKmMNXie5J7YYMNXZqEgDNFvFB3hLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=CSqUaePytlHb2Cyp_x_556s2YEHWo8AssITGXYn7-Y4tzcWbtimHiHuk1rrWsWoiRW9-6NYaycFT70UjEJBCeRPoNdcZzHhY2iCFdlnibRcVHE4sjJ7fbz2g7zvJN0yva2Nr_s98O8uTe8DP92MWtGIHwQ76sBjTfEWUxJ3axqUVJ-e2ZZMRwIk22VlYvn4-3ct-wnIlecU5xLbwqHV2K17aqAIb6Zy67NPCGxv5dLZZEXg8a5rQ1nkBBE0N7e612OGuMCYhkk3GycRtiXztZGRSQgXZAJRkoYzF6uTRgJyBkNH3b6SlVVjgN5u3Hai_Hbure1bgZf1OaeSLpbZa0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=CSqUaePytlHb2Cyp_x_556s2YEHWo8AssITGXYn7-Y4tzcWbtimHiHuk1rrWsWoiRW9-6NYaycFT70UjEJBCeRPoNdcZzHhY2iCFdlnibRcVHE4sjJ7fbz2g7zvJN0yva2Nr_s98O8uTe8DP92MWtGIHwQ76sBjTfEWUxJ3axqUVJ-e2ZZMRwIk22VlYvn4-3ct-wnIlecU5xLbwqHV2K17aqAIb6Zy67NPCGxv5dLZZEXg8a5rQ1nkBBE0N7e612OGuMCYhkk3GycRtiXztZGRSQgXZAJRkoYzF6uTRgJyBkNH3b6SlVVjgN5u3Hai_Hbure1bgZf1OaeSLpbZa0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuPdMCq-qnWh8JSYyhSbnSIaHGzVTyDF8Y2iqcFPKmIfhTxTkm7AtEgQNDI05I3Jt6xRjxWPPSEn0SEbd4GwynqyiI9MsS953WcrfT0QOVQaxcH1g1z0fFVPCHbJRHnR2_U09Yk9xPAJXGl4nUv115XMtGp26TFnBaupXzlFSjy8ydpA2cUtgPZWy8ez9IiJuZftY499Vd_SmFyPfO_panU5fsVUXEnKoqunbQFOBHm7fX0H7bSU60e8PxeUKKZ_3wVc_AhM_H9j2Uqf0LVNlOpuLAlaQ0pKu17utCvIky_sFX60I8eVaZw88DgVvLCdGAUAaDVnIrjWFwexlaPo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7MP6J5QudifcPMVnK_Tv__UAbrbsotDxkPvAz9ouJamrKTthWDxrkOqOpCPZUrRlLY4OwmD1gejaXgIjCYV4US4jU7qRpTWYnRRaoW0I_AjCXXq8IDpJEjoJrce3kcPx5lnJbXX3S5iFcnogPPcqnMhw8GwXY8y5pBodhvKQFWzPRjSOTr6tIBfvzANM_ZlIAAuc8POI25LRwlu5nGyE_nKXKjUF7KEZJXkvUcNhIY-oInRQmqoroHAj59KY-NedWbj80mZbyJ_18ygcr8T-nK-pVpa6GAw9uVujMi5SBs-cqkeZZ-z1pHHCp2BIxhrN9hE-BHPlBP5BrX3eRgS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaGvWEIW64PeaYiTj_AvVY6lEV9jq_GPx5DENTsMlCSr26zS7wW1Ug_p_DW2hTp7BENRKdanRXJb6ZpclLCXnT86VjUT17Ff5tJ36pddpgFl2JkUBszS3p2yppp2h6uGZG7xV5ifIl59yoauNcD22e3NrRmQR42u_VHBTsdBwnIRYnjbhZmfr7vJbnKkr7hpdvPwHZO-LEofSBOLU6CZ099B7EFnVJlN-uLdVd7w35GZcssKCFR_JbDA3sHGbloeBtnuL8PABRGwdejIwChLjkNnpdKldzBAvD6-rDfqHdskidyH0WV8xTI2no2vewLIALjMypfLQfIvsgEGPe2toA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P--IgojVCq2Mnte3D_0DDYgdMElnOSafpRJM8VfEzwU6p46MO4s0oHLFgL-qEmM3m8ID9nkUq6eGpivHmty7uEa5ZjOrf3huPE4STaurE0RRqbxaUrTdNM135249uBlaDRTldjAevFrcMYOW_hRXGsww5S-Nd82vXbbzDmJfovf4_tXNfbB3L5zSvw8YaKzuzaJAeCcHJGoDhpVNj9OqI5kNh8R84RQDqahv5hnFSJUD41TIah_5mBXDwEfD5ddUo_sJIzGIGi9irkFvIxybzdrinRLrZFzS3PqDo5leXFSFBgax727Q3-p4qBnJ6_xzJllO2sytt9cv9EjOUA9IcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiMj9jOOoHYeyAwJI91biXDG-yFbCg1LmebX9mReDt25pIEDSNfbHnlbvz0Fj7fpOnxYmj8sE7q2A4dFbQA8rz_izbxRmmdKq7yR_sq0dcls2rmsyGwMChQTZZfQR_D-LZczUmgHVcF1qvHjJSiLSWDaBNv411pAL1EdvIORIlNZqOFcO-Zx_NYwECHJvpCD_NOC6IDI1mapGRpn9f7SM9k-bVGZfA32dSOpXW5ErvaZe8TbJIXQPTiRUSeHBpR4sXMdN6ePrUgdVwjo74glnDylA4syhN2AIwnX8Hrm4NT0MyEOHup-uXlsOW29M1RTVMXa8VE49xcg_3dj8U3DiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grwmUWHyEtnOAlJgfiw3i3QormxRreqIvacRuknYUNpiUt2_eyDvCD-kPmDjzizZDywnEPp9Yn59oeRsNqXGh1_BoRELJ0ctnchjLqJKO3WgUPk9yNgsb3lRg2lERzlDg0xJyLlcu2D2K13fmDlwrZYJqR16J6sTZi9Dg_hol2WZUfXJPVNDf94_o6xGAv6A3FKdZJQlZ4cuI6nx2XslEbdhv_VwLJQcK96HFAp8tq9pb-cdQYVjxRyNH3oVvkVMBCtTSF90eWfC99OXXgCn4LjrgulmzkitpmLPqeBLkkD2nwMGIi4NycljVwTrw79y6OnDGswB8cNOt1Xzy056Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVOIhuAXu-On0qykWIsg1xRCbjsWRrZHR5WniZLIlauh0ll6-V4cJmtpyXs60cMdhm8_c-HwRbhTr4NcYIW9RWN_ehKwTYGQfJzGB8JHWOMelhQQa0aRxx4cr_gVEkqC6S-1dAkXcll8eXFjOUcjbFTgXpEEyjPDE_m6eoVz0w1z67jj9dO8aG2sT5t7ZG-p-lTE6SR41D8bWLrbCd-5jErxuUiBXW_zycTKnsUjmLknATQNyzxxaKyiKUhI2aYllSEarvLLJwJP9nc0jPb3hIha8zzgY141D4c4QAb0Dcc4ktX8YvPrSkOmsv1ZWGceLUswQb05wGzy1mBANQ58Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=DGi5LEjZre6SvsvVO6uG5eVLBWnnbHvw2dYH5MaNT2tst6ElK95Yd9mb4uQ7q4y7HSi6lkbbMpQJ6Nl7MSM_mUoiU8qy24SAPJBZWafv5uegm4I6VawaMUa3WBkjCKImh2-9O_S1DSxSboTvR4fYsS23Wli7DRxQcdYwsAbIusVbfcyU_mZyjdUSFHFGw65AIxBRb7hxvqKP3fY4zT_qkOk1wwwJIi2rB2NP1ODGzPWU7TrN-Ta7FY4z4DGnOAI8164aKIBLXILitoGiXM5gMCrQJYv-WLnx34t-iDPmF4v_vWOwU2s706fNWNtyOXAuDkmnVI1J7xNU8SZo-tQPZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=DGi5LEjZre6SvsvVO6uG5eVLBWnnbHvw2dYH5MaNT2tst6ElK95Yd9mb4uQ7q4y7HSi6lkbbMpQJ6Nl7MSM_mUoiU8qy24SAPJBZWafv5uegm4I6VawaMUa3WBkjCKImh2-9O_S1DSxSboTvR4fYsS23Wli7DRxQcdYwsAbIusVbfcyU_mZyjdUSFHFGw65AIxBRb7hxvqKP3fY4zT_qkOk1wwwJIi2rB2NP1ODGzPWU7TrN-Ta7FY4z4DGnOAI8164aKIBLXILitoGiXM5gMCrQJYv-WLnx34t-iDPmF4v_vWOwU2s706fNWNtyOXAuDkmnVI1J7xNU8SZo-tQPZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZI_JiOLFdcPniTzaZHQDdsxax2zUvl8TVCH0cEXS59VFG2VFdsU0ixdFHOW3o0sPdya4iUZUZgPRg71LENaI1zk_kcwvxkvnxK55rAgchahsA5DO5-qm9t6Tc95M3CVir7SFeaV4heIgJ-VRDIyc4vkVlXFo7OdGKU0LjBvg_3Cdf-GzCGEta5SH7PFVYNhZt0AthYU5P6Efcy2Y-n_SVIEurS5iFMlBImGfn_BhtSRhBuzDj1Uo29tO6T4kFqge-_Dp7AOoyAfQ6vf6zoFaffAXRNOBF5v_iaGqlsfJ5xUc3egJgZsSkfkq8y-jyYKLRUncGBWXWwBsSOPLMVoxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm7KjYdRs-3M6foECuGE16I9Hie537CyI6rGuorE-VYycd8-nV9b3Fu6nOsoRF_P_tboK3FOrlBMAjuo44nRBe-bvHBNPJh2byXGWYN07kkaSFPr_d5v6XcyFhM2fxAEsIqJ9zrTWBWjSDAW6aBfT05p76aWoU16RlkPVtLRoIp-MplEn88n2kNISYHthUuyfW949JY5tfEBQClhLR-PnmAIuKMVXhVMkl7I5mRSpAnVeAyEb2XTexAiQnbqx26wQH693-wObIwnMYetqxRa1cihr92HbyIaGxH9JSCVdByIFLKygT-n92H4NKiIIfPJDrObfJ7FZRTKyT6ErozJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=A7p6zDPKqJKMd1BK5yovFYVvjUq-Y7bLMm9_zaNDPk5etnV7eR8GkC3ZlmTGmRV423KkUdUYFCt91hkQJhh2xhJzKVPdWThJMdeJA1e-DgBX7r6griSxTNWdiJeovyCoRGqw2x27aLW3_Nzys72n28dFq9RFrWJ_4AtTWTNWiFZwKlXO-GCtMabGAHR9QxnexZ5dGHuVDIUBW6OBRN1ruTRSSmKBFD-5HoYv6tsIItDhwCq8sE1WzAXVX737N2G9hQwcLxkdIu2FxGc467GyS4IWBeKfjt92k-zaoNBxqTTW9-cVlNV8ooUK2XscCwW5ZbGlrSJRsavlrlcQKE-u9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=A7p6zDPKqJKMd1BK5yovFYVvjUq-Y7bLMm9_zaNDPk5etnV7eR8GkC3ZlmTGmRV423KkUdUYFCt91hkQJhh2xhJzKVPdWThJMdeJA1e-DgBX7r6griSxTNWdiJeovyCoRGqw2x27aLW3_Nzys72n28dFq9RFrWJ_4AtTWTNWiFZwKlXO-GCtMabGAHR9QxnexZ5dGHuVDIUBW6OBRN1ruTRSSmKBFD-5HoYv6tsIItDhwCq8sE1WzAXVX737N2G9hQwcLxkdIu2FxGc467GyS4IWBeKfjt92k-zaoNBxqTTW9-cVlNV8ooUK2XscCwW5ZbGlrSJRsavlrlcQKE-u9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=PyIuuZJBgYhbMMaRJ4GEEO65Z0sR0u6YLoMyTXMpy9UUq3BC6uPT5GrZPrWg47wrGQeSM2ZbIyqQke_WinsXEq7C457owX6JqKxDT-0sDi5ltBvsRMJCBINoZT2Hnfyezzu0qruGgX0An5tsujUcooKwrJUcrY9AxinH7Mp8myozKT99pouZZiejtyBcswEdkTD_ACQnK3P-GDZ10k_eV_0tvgra2vXqe-OTGe4eMVrGEQ6Xyp8SG5fi84vz9s9YAEbdKfteqZwfHg7zQ7hFf9cdftH94_RoawXwrL-gpbXx8lHPPe7qEs3u8xm8x1igZxdHZtR-xWdpKa8xYrqd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=PyIuuZJBgYhbMMaRJ4GEEO65Z0sR0u6YLoMyTXMpy9UUq3BC6uPT5GrZPrWg47wrGQeSM2ZbIyqQke_WinsXEq7C457owX6JqKxDT-0sDi5ltBvsRMJCBINoZT2Hnfyezzu0qruGgX0An5tsujUcooKwrJUcrY9AxinH7Mp8myozKT99pouZZiejtyBcswEdkTD_ACQnK3P-GDZ10k_eV_0tvgra2vXqe-OTGe4eMVrGEQ6Xyp8SG5fi84vz9s9YAEbdKfteqZwfHg7zQ7hFf9cdftH94_RoawXwrL-gpbXx8lHPPe7qEs3u8xm8x1igZxdHZtR-xWdpKa8xYrqd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBXKVbGUk1Pi1NE7sp4T7J5CsoZRjeg1yygGh9o_eAskLGpx-NmvErSAXEMGbYQMsUaSTTu7YwGBucs2J0wvsP9EgPoYBelwMDuOhqdszfVQ0Nj8ZkaoYDdqpONDUNLAD3YGWrXprbEEP4meezufyIhNBVRrOdLCpFtWP78BQ1AAMgCUdOpXx-Dz259R7Z96YwXM74BXOhCDgmDPpruYSL0bFPRdxuYuA59X0shrc06vyFWICQl8w3H84eptYfgigw88fX_vNtwObfRT_qKxNW6dfMGkIoPjr8-oTvAw1VLb5FSG6yfSHprR8kzJ0kTdvLlP3AWm6hyzDXO_hu0gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=QqcjzxasaUgm7T1Q2N7GjBGLGNCYnOiSoB549SG5Hc9UxOXVelZwSxj10ie8lJWb7kUxVQWHLh6T-JDj5lomu7w3x7a77R528ZW94hCv1zaraJzZma6UeTV6YFfJEQOzI8i0Nz7km97vPWn_MCCKQI5KIaZsJj5dGbSId8964DyjOIFrRWZN1SIMqNiVe2qhGQ91SnsS1lb6rVQiEaFB-j_UBBMBzZjm1EcCCswPPfNFyUGcuDCODZOmYuGtaHYgu8BKVv94MSoq93MF2AwCQxlzkJaZ0ICLg6jhTyVpGfM7SzyiuDsRKJCHGWQFG6hmN1uysglhu6kXpSj-MGdpSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=QqcjzxasaUgm7T1Q2N7GjBGLGNCYnOiSoB549SG5Hc9UxOXVelZwSxj10ie8lJWb7kUxVQWHLh6T-JDj5lomu7w3x7a77R528ZW94hCv1zaraJzZma6UeTV6YFfJEQOzI8i0Nz7km97vPWn_MCCKQI5KIaZsJj5dGbSId8964DyjOIFrRWZN1SIMqNiVe2qhGQ91SnsS1lb6rVQiEaFB-j_UBBMBzZjm1EcCCswPPfNFyUGcuDCODZOmYuGtaHYgu8BKVv94MSoq93MF2AwCQxlzkJaZ0ICLg6jhTyVpGfM7SzyiuDsRKJCHGWQFG6hmN1uysglhu6kXpSj-MGdpSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=HqMe1Qb4L6MlNzZL_e6whOg5E_RBuu-ceG2fV27fe50Xd13kSmNFtPrPg_8t2s8_r9-8drzUCFlQemNykU0S0ctiuLrrsY5MnbJcvhI6VMJXIZSHXlQQW2SjfuzanGHiXd-QNcdK3YheOVsDwNH4Ny4dIComM51aUaEmRO3mfqNHqMGyd_0IYap09gag0WKNPR4JuuS9N-SzQWiXXVpAoLUhJUDV-QdgXtICCDhZVDCSapmYLlPlO7F6dPC7J6NiGANBt4ZfwRWjgszkxKggrYvJnjrsYEi8ohGlW150yWf7Ue75JMj27mo71A8ef08wMnxAikycvIYBB44j0fKxQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=HqMe1Qb4L6MlNzZL_e6whOg5E_RBuu-ceG2fV27fe50Xd13kSmNFtPrPg_8t2s8_r9-8drzUCFlQemNykU0S0ctiuLrrsY5MnbJcvhI6VMJXIZSHXlQQW2SjfuzanGHiXd-QNcdK3YheOVsDwNH4Ny4dIComM51aUaEmRO3mfqNHqMGyd_0IYap09gag0WKNPR4JuuS9N-SzQWiXXVpAoLUhJUDV-QdgXtICCDhZVDCSapmYLlPlO7F6dPC7J6NiGANBt4ZfwRWjgszkxKggrYvJnjrsYEi8ohGlW150yWf7Ue75JMj27mo71A8ef08wMnxAikycvIYBB44j0fKxQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQjiBQUmLwbMKcCt6eOpMHGazHD-y-ZjFyC1jbQhdngXfuBcvzq71himJsUr12DmwTVdakiJ6RDGiVlQHLxsf7DNFdYZsB-wRDF6qzJ_APGbVoYsnzdPlhWmzOK1onPTazNhsQjWf2oq7fZ2K1SyJo8fIaCnaebSd0SYfqKMHwcRlme4T0I6tsHFO_vUiV-KkXJYhtbBF32IxO-WGNdZiX-PRAfELtvuycvtku9lg_rARNWQRPLD6jjbEz4T1VSeN4iKL5aWhsRndG7q7UwPoq-cfnw6e41_L-Lfv8Bsw48iA54by4A_RTGx5Q2HqHCJ_CqmBIlOH0QmYlzY-Y9qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWTihBanBjUljG54r1ed5icXLqQ4ZIo2lbr7N-Y_lBNiDabI1zaIIjcYLdEeZCs922HsTzUvF1KLY98U4mNTA2cZubD9fKgkj9UqWPUscytLpexC8sYdGiTXN0lgvMYmZmgA-Y1slEv12iNed56jBmLjWkbtyViqaVnlwDwqaCIKXGqLUXdXJyzjDTCmtGlHOv1cW9_ycezY53IizK9sZCDSBB5lHVaLygU6hMu4sqrj92xD4r_0OWNk2NLYx53LQTV6AvqjiwpQ6rtKXg5TKSltA-LP2fNqSiu1BFpC7CdZbgqfXQi-3ugnhJYJvJK2o1WXtn-P0oC7zY_h03wQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqzvrY844fFTOtFHCJ0HS-IL9Zg1f6Etb3VFXyI45bT1FLy4xVTakzm2QFqVJSKt9sxG0hEcyY2otS1izkJhxgeL3aykTTTuB6iQuXgDU0qMWlCUT2g86_1_yuab8v5p0FPQyKZvX6PBjTh2XufLmHdisE5G6_lIwY1SfDHoexnBlTw9BmBVHTckf3Ow91JCpBCY8YbJIrAf9tj92O0tB1Mrq-NHxEZfwOhBLAW_X0C32iWxajAslpPGDk9f7XVSZYnVw6Vraqg-aQFnMQq4k0oILQ5YSoH9UNzRnekFK0-K92jQLTcjUoA4shfF8Cd5xloqrwPOwvYGfXZZ3BtsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OztogntlxrUZVRTLHNlG6Vt5jSo7534_lQt4c6F74Xfeur-9StWtUyJ96bZXSN7Sx13XeT4_hzwoYOICojLIbThIlJp1JEiazKi_pcqCg3RRxG41rfRFaGmMGs1Dck8WBXEOmDA5kpKLuzosZikRyh4_B8GCvL_Hi3Sb2BE7dcF81wupUMlF_OBFoghkBVsrLhAaPG1__HrOGX9Et8z9CJUpg_c5RGsI1eQ547bmxP9uGkfH042Rz4NZSoBtxIAykPf6rzfAbhksVqJMtoPLpDBR3tll7cMHoSgUK3lTxJB9tDdk6IMBvKQqkGH-Qha7gFjMlOMiU_98NjCjnluzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=o4vZ_6JpA-oC7cUNbotHyiTkaiM-OoUAjahnprQ2rE6SsaJDItyf-OxQhwI7kWQ1CthgMm_pOgu-zJdoLg4Xr_B6eW0V0ZWcyh9K8gmLKedDkwTvbqS6hvOCYjEMlLUkc5wd-QRe7TPGvYsYZQy9FJxd0Wpo9P-dtaHD2WMbwYUGKOkrgWRUlL9Odf5IIt00BhdUoJre-JNuuWcr0Sr1qzT5jEvt5XGroHMQSqW59c63qimZ5uVmnqYfzo6aQHZNC9bgIeJoVC3yzssWpXYqSi_RIww4TMMhBJnLmZmYz0i8zmZ_tbn6NR4CBLc7S3DB2UQurxgddU18SGPepEsQfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=o4vZ_6JpA-oC7cUNbotHyiTkaiM-OoUAjahnprQ2rE6SsaJDItyf-OxQhwI7kWQ1CthgMm_pOgu-zJdoLg4Xr_B6eW0V0ZWcyh9K8gmLKedDkwTvbqS6hvOCYjEMlLUkc5wd-QRe7TPGvYsYZQy9FJxd0Wpo9P-dtaHD2WMbwYUGKOkrgWRUlL9Odf5IIt00BhdUoJre-JNuuWcr0Sr1qzT5jEvt5XGroHMQSqW59c63qimZ5uVmnqYfzo6aQHZNC9bgIeJoVC3yzssWpXYqSi_RIww4TMMhBJnLmZmYz0i8zmZ_tbn6NR4CBLc7S3DB2UQurxgddU18SGPepEsQfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDfqs5HIHhgcJXRGffKILYmbWb3yJRnTSvJvx5oYeFVw65HHrBfEzDn0fm_3oUl20bEAktYHMCyq-XQ1DlgM7Q6Wc6bO2j8QlNInqD37ERWfvA0T3sndB7G8aXsyvaD_BJCAdH-11topgbuZ61YfWergCx3F7DK_L3WaKAmUpwozMTWYZEZ6icwzMzEb82gwDtSkZGFAKNFGqKqdKpXuieNg4-0u72cOQkFCWtJFPk_6TnBoFZruC3G5FFmCy1qhe7Fx_IAw2GyKZx5Gb-vVI8UhazkiLRWNCtCoIVEXiHnO1lMOa4nFxSd0uYQLK8anPzA6w5-huvZS4sUNHNhAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFSpE3b3SNeILWhnJv0N70cbFKAmLc4Le_uLNUsY4jDUDifkvktyAg-e3VwbIvwXasBc-GQREizR8z7vBJGx3nfMtMiCjOY45H1nYTUIxvP_GtudnZK_dF2lytAmYvkd9c8uOgTKyxUvXq6xpTYzIT2w9d7m9xqgxk-K980rPe31RO70TIqvGnuS86BAuSWHayBdO12fAg8rj1c3kly17oGGTnD3fphp_j8SIB5xuSxKrBAvlOV8a7fFohPWRWTqeoK80AqCkKv9BYt4-oKdr-ss8hEMmBwFtgtkAgy46eQZqTC-ms0Ed_sp6BCy4Id3bmG7FUtruYZYnAoQ7wXytw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKo9u5uoBBvONZKfXjvgm6IPylTl9hzrtbOwkYpVl3CLIVI51NvxiK1FAtan31jph-xNYjOD9QiATm_7mjQOCDHfpYOIbNqfDXqS7Y5qALM1gn0GO1_l-ZH_J-J5xfkyVjBr7AOe599PGKu4nBiHm_EA8PmbAEBQGqeF4R-4mbpTVoAurknjfeFkhGGYgwxUOzmV-kIFiezbSMCrQ8hO9QG56LAGY0gR_hJ4Jj9ke07yP91vHQbztvfpAZh-BU1wlxTgeaebU0Qr16lowzFhU_G7fFzeuaUbPIgp5GDSDUO6YxLpadaVn--NkqTsxm_qta2fNkWzDzFXkg874HzEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=TcjfL6-g0_hcUQ2SAlkelrNqxyqPt887JbR_jiN7m3tQoQZOgKOhNku600zRnMllMTUDe7ij7GlHwkWzvL0A-dkHHfKopJOyLhISyRvpvVbgkrCGALZbUHI1dVrPLz0zI3HnTwmniy-nggu-cMKOCP3k1nWrEB4kjWld73z4P7ZE2Xk5bhOaxBJauWdp80-HYKSu5sKt00PnT9Dd6h8uGEQB789H_jcev3_TtWENmOwh7lRWJvWMJsVLHuFaL-zG1bnDOtMpwQ8RYtTv7eZB_ALGYNVvFx5kr7AyvhW8B2oQ6wZb9Jwfrp0KoLaEDs0I353NsPfKUQ40zY0AwEHLi3bem3cM3LXYgHDb_wTndaTJS4cxADAmmH8UejMQ2gyq7D7Dayh0QL2UdM9nybxKbOug_BIl6z1Y75u2RzfBjmNMAR5E1GgUDqG4XW3iIClgkJRs1B6yUCV7y2yFMNfwawUl_w6tePiV21a9lq8pCh5qWpJ5t2-L4pOpK8s8bFp6FWLthByaTRK61FDjFWHIFITcUBfXfMGWr6ZrKvGfxo9HKtOHwPWyL7uB39R4sxTUlVz5hDjMAG8wXt0hwHMgjJuNp79z7LH5ALmGdn5gKo7bLD6xnnevPdO9Q48hrSrKHuE0k08mMjTJDV4ng5psXfppWaFgUW9H_KVFJAWnwic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=TcjfL6-g0_hcUQ2SAlkelrNqxyqPt887JbR_jiN7m3tQoQZOgKOhNku600zRnMllMTUDe7ij7GlHwkWzvL0A-dkHHfKopJOyLhISyRvpvVbgkrCGALZbUHI1dVrPLz0zI3HnTwmniy-nggu-cMKOCP3k1nWrEB4kjWld73z4P7ZE2Xk5bhOaxBJauWdp80-HYKSu5sKt00PnT9Dd6h8uGEQB789H_jcev3_TtWENmOwh7lRWJvWMJsVLHuFaL-zG1bnDOtMpwQ8RYtTv7eZB_ALGYNVvFx5kr7AyvhW8B2oQ6wZb9Jwfrp0KoLaEDs0I353NsPfKUQ40zY0AwEHLi3bem3cM3LXYgHDb_wTndaTJS4cxADAmmH8UejMQ2gyq7D7Dayh0QL2UdM9nybxKbOug_BIl6z1Y75u2RzfBjmNMAR5E1GgUDqG4XW3iIClgkJRs1B6yUCV7y2yFMNfwawUl_w6tePiV21a9lq8pCh5qWpJ5t2-L4pOpK8s8bFp6FWLthByaTRK61FDjFWHIFITcUBfXfMGWr6ZrKvGfxo9HKtOHwPWyL7uB39R4sxTUlVz5hDjMAG8wXt0hwHMgjJuNp79z7LH5ALmGdn5gKo7bLD6xnnevPdO9Q48hrSrKHuE0k08mMjTJDV4ng5psXfppWaFgUW9H_KVFJAWnwic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=uQnF6yR-SK6wHR8jR6U6ZIhOspqeRAv_bg0dOOBOTic4xhDbUtGDy_BbxUIysKN99AUX_E21uvvJ40o-nF_hfU-xSxVx9BDX4mmD244K3fmBfIQO0c3OZc8dKz5IPWbbw6NjHjfYlpyWSb7ztiX-UFTM0ZYLd_UG035Und1lKxQFWA0XD9dV5XOc9WI7efdLzwEQPhK7tnCTEswfUATftDpIwr545I60o8a5awwmtLBmbAt-v7hP6XIsPzhaw86rPq-M1s-FTuKF6FCUQ4zpxl3eSh4ZPExkMVQY3LNnIm9xLcZVeN1yj6NnRe2pW9lUomL7uzheu2xyULPtnxj9Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=uQnF6yR-SK6wHR8jR6U6ZIhOspqeRAv_bg0dOOBOTic4xhDbUtGDy_BbxUIysKN99AUX_E21uvvJ40o-nF_hfU-xSxVx9BDX4mmD244K3fmBfIQO0c3OZc8dKz5IPWbbw6NjHjfYlpyWSb7ztiX-UFTM0ZYLd_UG035Und1lKxQFWA0XD9dV5XOc9WI7efdLzwEQPhK7tnCTEswfUATftDpIwr545I60o8a5awwmtLBmbAt-v7hP6XIsPzhaw86rPq-M1s-FTuKF6FCUQ4zpxl3eSh4ZPExkMVQY3LNnIm9xLcZVeN1yj6NnRe2pW9lUomL7uzheu2xyULPtnxj9Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=afg2rg6kh3r_1l6Iet7E3EF10rfIVmOmexUERhDFehKtN042lpFJTk8dxqjA6X_hT9nfeBqPSdCev_TOKa_2yd1dHjITkRpigO0kxS6d0SAnTQkM62fizxYmIgKZPCYYbYONwtlXKmVFY6w-iTMX8KEtpjNwQ_f3uXr5aRVBBIZTRxJBuPX9V9pkvPCG1PIws6l1wjRxVC8999VF3iJ1716FWo9sQf9K-0gf2SM6raqGALzmpxHJqpZDtSr4cWQE9i1Zj40bJd0YdfAu_7325ole2YcJ0GBmtAvUnbjEUZ4KeC2bxtEvKSLN3VN-OtmzuTKRUNMKZIo1fPZOGfcYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=afg2rg6kh3r_1l6Iet7E3EF10rfIVmOmexUERhDFehKtN042lpFJTk8dxqjA6X_hT9nfeBqPSdCev_TOKa_2yd1dHjITkRpigO0kxS6d0SAnTQkM62fizxYmIgKZPCYYbYONwtlXKmVFY6w-iTMX8KEtpjNwQ_f3uXr5aRVBBIZTRxJBuPX9V9pkvPCG1PIws6l1wjRxVC8999VF3iJ1716FWo9sQf9K-0gf2SM6raqGALzmpxHJqpZDtSr4cWQE9i1Zj40bJd0YdfAu_7325ole2YcJ0GBmtAvUnbjEUZ4KeC2bxtEvKSLN3VN-OtmzuTKRUNMKZIo1fPZOGfcYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=S9x99-zlLBYMAyPuzxwoaeVjQxuvoJG1AxWSJwYWUq6txep7NG4nzC8YoAVyl3IDYIuCH1qRFVWPxnwNk8cNRCTPzNQX9Xac8Tf05g6VQrbRp_hVgRvs11yhAE9_DrCtPaONrKv-bY2BoDkdiGaWRxbmeM2NyiMTRIAKrgvbUTkyHMQBN7gojswfL2omItqEgbZbZN1VAWBC-b0tJdIphA59ZAhyr0Um_7dFAnXxD7W2bIgn03vpIR9XQ5ZyG3UG3KG1FYAXAKPTej5iN9AFPBJnchgG6kwjJ4HDxI58U_iUs7xV63qqAi25cauR24BONYJEbKQURphLzwIWUWgUmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=S9x99-zlLBYMAyPuzxwoaeVjQxuvoJG1AxWSJwYWUq6txep7NG4nzC8YoAVyl3IDYIuCH1qRFVWPxnwNk8cNRCTPzNQX9Xac8Tf05g6VQrbRp_hVgRvs11yhAE9_DrCtPaONrKv-bY2BoDkdiGaWRxbmeM2NyiMTRIAKrgvbUTkyHMQBN7gojswfL2omItqEgbZbZN1VAWBC-b0tJdIphA59ZAhyr0Um_7dFAnXxD7W2bIgn03vpIR9XQ5ZyG3UG3KG1FYAXAKPTej5iN9AFPBJnchgG6kwjJ4HDxI58U_iUs7xV63qqAi25cauR24BONYJEbKQURphLzwIWUWgUmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=IJ6Nuvkxf35oSsBUHpJ2_JBjguN5gGgVm_dOd-vZmAG2CbD2D0wJBlMfMS5tRXY68WFIup2GvWg6q1vNEICVYDTZeZTfO_sbQ3dOet8MxIuShdi-KkvOQ8iXvSvdXoNktlIQGwVJrnXeWPmn7z-XsVdiyBFpTBr03maxuUcQV1iBu834GZqslKFMV-CkUzuF1D85__lYJJ1sXW6QTcKkfcTufxaKMdorIwB3LR-vwZlorUZVzM-Nrc0HIssrh8rK5qgIX5AaNKPeZ8jdmaDe3XBdNs61aIPrpCB5Ls8H_Vk0Ez_49Dr8xDpSztD8KJqDDDs1CwfdY0cmBx-VPuD8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=IJ6Nuvkxf35oSsBUHpJ2_JBjguN5gGgVm_dOd-vZmAG2CbD2D0wJBlMfMS5tRXY68WFIup2GvWg6q1vNEICVYDTZeZTfO_sbQ3dOet8MxIuShdi-KkvOQ8iXvSvdXoNktlIQGwVJrnXeWPmn7z-XsVdiyBFpTBr03maxuUcQV1iBu834GZqslKFMV-CkUzuF1D85__lYJJ1sXW6QTcKkfcTufxaKMdorIwB3LR-vwZlorUZVzM-Nrc0HIssrh8rK5qgIX5AaNKPeZ8jdmaDe3XBdNs61aIPrpCB5Ls8H_Vk0Ez_49Dr8xDpSztD8KJqDDDs1CwfdY0cmBx-VPuD8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm4b4lRQio_si2yrQ528HF_3KNwhSjbGmJF8uly4by58iOD-1qeO_T4BOI38cUAkVYEnfw7jHurwga83UshGTMpe2ASugxozYWB5Ha0PqOiARLRKcCX8LZ8dUMq2z5GO9DlH5gMZipC4hNik-VQnCh6py8s8VuR3LsKhLE5GnKrnTfjs1O-LZEYfxzyiY2poX4RdiXPU3HgwCBY2lHjXfbl_oLf7j8lPrqGVVZhJottw-u9X-KULOWgRwifv6kJcWkoKkcwtXM4Ri1M4h2l6K59TUsxOZ5eYAwJarJTS2xFzTjon9kf48x0J37pm01eByi1bUAHhZ2QKzgVjNFSRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC3SXR-ec7aE6C6-RFjR23GDOmO86rAzp2QhbTnFnq70qwHZPca1LHIsxKy5pHk6yE6OiASyZzsXPgRxuInv7Cp1RVRgee_wc7YO-eJXk0udA_quA4L5IzLpX5bJota3GVYhSvcXhPngX8P42B6KzEeyrr7GBDEodI9iRkmpy-C4LMY4A0APYqzTsasP-PIa57sjcE4x_VQvDqy1vLccym2tsirmGauDV5xDKt_UJxB0b8_93SksJsdSvS69RnjmiwH3G6d5LxUwA01SJn-ZdGG30HU3IoDtCQwmiCdpts0Z74ZYbScVyr2mr52hctdHHXslIYj4VeVw9WAqBNowbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8CAg9NDQZS74dEwPObgNrlKgO5K5MoO3cfIVsiFH5i02eNwOk8J6Iac9sXCD_ErY2f9PZPH9XcFADWjAAOYJkqCGgSM9ihj_vAZIsVhXBYlS6ZnFbHCY-7qg7_Apfz5whIdH9tFXa7TPGjwU2vKHPfmCi5L2ZBcbcnYbpdy4ZHyOeJXOy2puroJ4Kkq1vDXEgF_7hKraJ4sd-dPE6u0HZHOUj-MV2ebCvhnNVENXQB3oUiIxzZBEXj4WIQeFrobvpcLRbt3L6qbKT9OKa9LGXhoA_60Htw32VmYwQvsPDNmGUtfBy7TwtAs_62mPR1XGaeK8E1cSBI0HGjhkEHHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OivFOo_IxrCcM_Z_T0VXFZI4raw9NqimfWsjQarlJRntdHfQFtepp_ERrR3-6jYn0frXbei83j-BbLNE_2xP1tSQ_gg9Uk9zNIz4JrMMvlJID71AAj9sIih5oxokOZ8_BQgAroJw8rujQt-_RlqrvLDE7KBeuOCXVGG9Po8WCvB33AlGLK2DnBlUCdoCEx2859w4-FJRvmXhX1YJgl67499CnFnofE_xjzKEg-4Jo5lF9qiyMS-DSrwS5ZWBzu1ESuz3OQg_H9VGbjO8dKRz4PcqVzYe_y_rZk2D2uIAAL7SEjgFUEUgHwIoVKaVHlKwClE4uvpTSzQjGGQz2hc1ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1bmMrvRDYc3arZpfGqrGcLROx1bJHTiTcoO9VsrPEbkDXA0cbXhV1XHXXZ4rBesVe6QWTNIn1Ih0FpYEUFoeoh4OfW0tpUjRCRBll29GdnWg-4Fs7bU3OOTWVxlhKt20rez0hTBlhJZ_dJufUXg2k-qBsOp66lp-4Aftupi6j7ek8eKitlVKeXQ1T7t5QKnbbiiL0lArT9RVzniW1ivvxzdz4xqDcZXsQ_tDCFG5E6kxrsvvYisb6vGZIWJhaWMIOHBrxUFq6Dh3ZLn0KmjYt0UcNFVPsJ_HV3rSvHBzMNlIi9DbH-9RkW_ZyGudUU-S14hk8NAL5Y5M3GM05ADzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rGA39QgOy8-hOni4RbJoktsgrHFU1JIUquZ3zoLglogPVA_qhPrJhJ1K-AuVp1_N4l6EKD3mzlvjVxYD1GYcTPMXC7EBK0Jskeof3gsDtkmjXgKz14X3LBq4MJXs9J6Chhz3pIFEWxAeDpSZZEWFTFLtAKWrsx0PPJ9Gy0BvD10fBj6OKQZxCG3nrEmLhLaasTnXXLFuL_MY64U5OC7eMf1DWSbVDdFlKLXrhJ21ZEJJxl-v9-HGK9yB_WEIxm50Rz8gOWudufOZVEwyLXAjigvMBIVwvW0qBca2hHodbsLYOJxk4J8O3MFPSunpTIzkY_1EzkGV35E5cvahmhWjDJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rGA39QgOy8-hOni4RbJoktsgrHFU1JIUquZ3zoLglogPVA_qhPrJhJ1K-AuVp1_N4l6EKD3mzlvjVxYD1GYcTPMXC7EBK0Jskeof3gsDtkmjXgKz14X3LBq4MJXs9J6Chhz3pIFEWxAeDpSZZEWFTFLtAKWrsx0PPJ9Gy0BvD10fBj6OKQZxCG3nrEmLhLaasTnXXLFuL_MY64U5OC7eMf1DWSbVDdFlKLXrhJ21ZEJJxl-v9-HGK9yB_WEIxm50Rz8gOWudufOZVEwyLXAjigvMBIVwvW0qBca2hHodbsLYOJxk4J8O3MFPSunpTIzkY_1EzkGV35E5cvahmhWjDJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=v3a1-2mzR7PMjNaAuQCfOFHm3QTSbrnLaH-hEViW-qqo8qD_CAaFSuvfsXpIUzH1CMIyNi1vOVn174CQyuXhasFdJRVxh6ZAc5KPHy9L2vUCShPi5HZI_tLV2UX0Z9jHiBT3PnV1twzSLuo8OHmCo68LtOZvKWW91TxTbGcrs4xGAvgP-03nzYqkC-fvUksdotWqw9j4XGBo2Q-mbNSaoyLX2EkbMdyF4uADkGEp1YQzXTRcyBuwtN6sdAo47JDXzTJuhULtbKApRzvfP1xGRPo6sQLLqnn4EgiEm1015iDqEocWr2uIHRzxMNS342D_CvOit8XXhbZnBp6ub_ok4ZrTlx-X1RYgfOCDTwsGNXf_Y-7CPDGnfTl3AQ-i1RIYdUfxWkpllJcAyngHp6NPlT80bQ3r5G7DdzcmYzD6gJXlhgvSOThHR9T1wmIa377rXJK0swt5yBBeprRZfR_NEX5oDI3vWywSeUEOYyDPPwSRY-qB73xMe4KAy9q-PslZutxzS2kD-enLcp471XTjuNL8EsqOaIDTC2t2NCt4WoRAb2lP3svjRux2OklcnunB7Bxh7VNcfdPyS88Bi2Rch36gmsuBHkwDYvlUL__QqZpCm7XNOwdZnX71fcA94OeBSlwux_ZXo2t1R0OPZw2JJSpurz-TSJrSh9BHDbKFqLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=v3a1-2mzR7PMjNaAuQCfOFHm3QTSbrnLaH-hEViW-qqo8qD_CAaFSuvfsXpIUzH1CMIyNi1vOVn174CQyuXhasFdJRVxh6ZAc5KPHy9L2vUCShPi5HZI_tLV2UX0Z9jHiBT3PnV1twzSLuo8OHmCo68LtOZvKWW91TxTbGcrs4xGAvgP-03nzYqkC-fvUksdotWqw9j4XGBo2Q-mbNSaoyLX2EkbMdyF4uADkGEp1YQzXTRcyBuwtN6sdAo47JDXzTJuhULtbKApRzvfP1xGRPo6sQLLqnn4EgiEm1015iDqEocWr2uIHRzxMNS342D_CvOit8XXhbZnBp6ub_ok4ZrTlx-X1RYgfOCDTwsGNXf_Y-7CPDGnfTl3AQ-i1RIYdUfxWkpllJcAyngHp6NPlT80bQ3r5G7DdzcmYzD6gJXlhgvSOThHR9T1wmIa377rXJK0swt5yBBeprRZfR_NEX5oDI3vWywSeUEOYyDPPwSRY-qB73xMe4KAy9q-PslZutxzS2kD-enLcp471XTjuNL8EsqOaIDTC2t2NCt4WoRAb2lP3svjRux2OklcnunB7Bxh7VNcfdPyS88Bi2Rch36gmsuBHkwDYvlUL__QqZpCm7XNOwdZnX71fcA94OeBSlwux_ZXo2t1R0OPZw2JJSpurz-TSJrSh9BHDbKFqLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neejYw0-7I7qrQ5IaGvcFHcE-EJilw4_7ifkTP4qtscNafmsRXuMybMn5x8y7iVqUAZPbG2IESPYeP4cjag6Nz--Koz3NxKDl7z-k43yCRUNL32RLAtsJhgAfDFB8_2GJg_urCYVgb6x0rhWqlNdW0ipUVzzuTyvF2K7iDw2nTAtEWEnCbzRCJHIX4SOWVKPYCIJdG8_c8rkX5b3nekJjt4UDg1Ym5q07iE69Ig68QLsvfjav2BKkaTAjrPS22_SvMYQxg361CADgBRXquPhhPy7aRH6SWBXSGdNR0dz-YbOMyk-bLnwAzlex7g8obWf3bSRuPzFSZSdzc6IxPy0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv6gNs3eaoa3haazRelL3WMzHfLwBDotdj9NZ1iJA2FRFe88olDnpc9mz5flhGKRPvdRu7sVRFljV6lXSgAj9CwuNYbZD2IeT0Lka8bpN7-mGBsnXn9AJFiG7SWzQQgi01y_m9jjB8AMa13hgUtx0RiCh4OFr_wabl58K2RBgMzQJHs2cvUbVbbFZaShhbqB1rNn6oZeX75_a6fnTEQyvyCBKgoZ8eKtRp6-DhxlugDTlfVwxHE0r1hdDNy8MIXihpCHi8gXmpYeqE447c2whZDqVGTogbuKzuBkIJIH_YV6t4gqAxM23YMSTYKUrpQ-dRVlBcOf1DIuym37Tvqmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r94ZCPeQ-o3CsjHQcDhwcMSuytMAO--ZGuyNvonj4YwjqQwg2CJGxD6AMNFgHs5R4GoAnMIaJrnS40wcdG_2MPFrR3zcdH4xVCF6EttxOKe15VaWsv86g7CJTRLqPqUPPd1_TmAuvUlKu6HFfcHdoRVWcqCr0G_Ki352McZ2pfQE-gF1ZRiYEAeq6uENy-MsjZSaJpGOFiXPkxlXGLjXnAgG61qo42LpOC8iSoct8IiDVxeNZaX-vsP-fjinaR3qF4XwRzdRiCmS6nV6Whus8rUqx4hUzMla1sxQB3dDVVbvdVcKYHM8KW8vTOjORupyi5Kuetfz2AVElE20H7fJrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9OoOB-vmpDHIbDkhZJWBHOlaTjXUJw-0j5A3UMEtSJv-N1O3a8Q6URjizIBSy_TA8XzWZkGc3ip-gj3QrqTSFhnWYotvgQcH3fQJy3bwTBbnT55R3L1YjoZLAQncd6aVqbodAguNFJMmVl7zs_00mp_7hyIfwcdnToBSAJlnaD4MhCwYyNQF-40ZZ6O184JwoScF1-5f2oEBpJP4DgtsYxjFMuXzRiI7O9_hDwtXbqYP7iamNeaJr28q3TWloESAnpM8Xeaq-QsAVVK-p4Pd57uiQlj77mMCYHTfzFpG8wtZRj_3JeC1pcEXkSquRFLe4I_cYZRc3yYiEESVdz0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIzASFXwnX5-ltmQe5t2MKsui5F4uJB7YEllsycPMp7RYoVl49_SB6e3diQcD7omK2MhRIRvhWdFeA3tkK44AhLAJhdD24ySVcduQTf9Pww3x0SMCYeCHTITs-GMbux5pY9eldnn-jtdNlw-QjWqkSlapI4Xyul5C4Tn21ZX9kLIVjFMqpOwDhDOJWblj8phBH9ZDf9hrV2VN0eq6EbH51Ln2TjeftsWmE_7F9zR5IM33W8roO05cBaGkbKeTcaLqtlI_rj1q8yzW-CNpone8Z2VAXTtVRSBLQvUKuddpw8h-7fOYnIM_hTMbvBBk7gfVkF7CpoMNFkOsO-ifkS2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECsvuLVmZRgBpX6FXl_cCWgFpR6ICj2MlwvAitF935_WUc7i7b8uS0yq2vEco29qhnlhJT93-PI1qQS7mCGIHdMHFVmbX9d12XOCQNRzleU9oCqGrx6TXgwB-4OYXiMGbfNV3BcKU2HGZGvaLmZc981DgrySbBHvyy1adnYIxMRFZVWGeToCSF1r97kGzLoUvRn5zRIYEad9C69RZ2SYGxuSVjwTAqwslThRckd9GQwr2yZCqmuIPm_9Gg4_Gjca7Isww1Kmlp4RuFq3DTkhpz1OBCS_YwcOGnupP7kPXGQaYybX6psH5A17UhLWWRWRPqgl-nrKWg1F720ueix1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHVzhGhrqJtM0p_CMQdWD8-BgyzfdS344x_5LNF5-2ZOY6FszO2X_CNVrUGdMx7Yjg6ODznRQvJv0NNc79JPuY7kt5tvBh8_w-hzKVrPlQKHf0JnxAyG68tVPPPBTgs_92Vw9ogMw9y0RVtsKtK0tAFkX3PneafVdpbijR-q7pLELnyYBi1xGZ3bQ7fkLm0G9FAPUdESEyjb2VRrBtKGh02P8eQGfT3et0dnfCvwIQU40Lia4Dh5aZ1cizMuChKFSY-a0dWJVRHT9lhR0gH_EYHwqIRV5hFLczh3z0hx9UsvNQygqKh6ntEurQpIPm73dQTYNdZ5u4a3WlGwy_hcWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbiEIQJA8yJyyPJm_x3CRhkOSR2L9TC8pHavisf0YTsNSUDneZiypKla2DjSFHAVwJTLqjWMHivDd0VXv05sgXtgSDwXStrMoaMvtM4PADidn0idZO1mbID9d9wmbvlf2jdvfw82tS6apUWvdnybn0SZN1dq-x2y2SR9eCls3rWLEKsFA6-MTkfmC2UlKM6_LJf7azSKBQCVbbjvmbQjzAQQKHDRyT-bi5aYM5a5calIlAojZ85hKbaNvO1Sr-4S1yRqQUFYTyB288yMWq4uerG-Oq0SP7A9GojBHGGGCDrDYkTU_aInmsgSwbALYLa8nVXRQX0NqT-euKK-pFOHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1felX6rWL4A2v1A91PdiWAmxURQOjEcAoa202HS0oJVX8GCYIg-GmZWuTCj42MSUw6w62JdRMikIoTQ-ewNbmnQcgCgNh5c5UC6GyVgbxUtXezl7vYxshcbylh2Y6WpBBi8ccFjbtJQUb76ihI-Tl477rLZLqcPwwaLjy1E9aAbyeZJuhk8mR-Lku8R6vRsENIj3ecqokQitJYbaBk4_EBNtfHdt0au68GK6WBzKtLFD9zrJdA3sE4GEQQNPvT_2TI7YcSeIfqMFgevfY_mwkA67z4anjOLmUKoelqos9LG3M8kCp3Bb-yZkamyvEamX8fAg5RoeLcj2C-XT1M4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=C6KlKU1F1kviy1bGt2aFtA4I_0R4EN-_UNHnqie58aa0NZG327O8Fp38iKps1KFvRApBdjm7s_HRz2WbVDhMTMWmgco_10NmofhRKBclzfEomLNxL64oLFZwBrGd2uKG-wqcv6fDkeTqEiZAJ_aICWr4L3305mAWVRbU2HIfeL97kif1BdiKV9C-rSPoc6noBA-se1Cez5MNJm50C-ed6o3gg46TXYuPLOm5Vr6KRdoirz2L3H4meO55OdF4oxfNlfbbLntmjsfkQqTQYyQQvH3wPc99pg7Ea_Y1VQgXWcJ1pZnsZnuk1h2lLKT1x4Qng2LywwC9mIHA6qENZVb-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=C6KlKU1F1kviy1bGt2aFtA4I_0R4EN-_UNHnqie58aa0NZG327O8Fp38iKps1KFvRApBdjm7s_HRz2WbVDhMTMWmgco_10NmofhRKBclzfEomLNxL64oLFZwBrGd2uKG-wqcv6fDkeTqEiZAJ_aICWr4L3305mAWVRbU2HIfeL97kif1BdiKV9C-rSPoc6noBA-se1Cez5MNJm50C-ed6o3gg46TXYuPLOm5Vr6KRdoirz2L3H4meO55OdF4oxfNlfbbLntmjsfkQqTQYyQQvH3wPc99pg7Ea_Y1VQgXWcJ1pZnsZnuk1h2lLKT1x4Qng2LywwC9mIHA6qENZVb-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
