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
<img src="https://cdn4.telesco.pe/file/No3xGFjt95j0VvoUnPTzrhFudo9OXI0J38ug1HlztX_9xATChG0VOlA43HVyMPDg_uR5Nl2J8u4DBbltoJtaE0VKjBRCtzAwSNq3I_i9XR4qzj-5qn3JPMrqZ26GHPfAVSkmWGfpWGX8BAgskelRAMC18R7d2E5k0G2OdXTv3Xb_qSRc3pVh5zxpKgOwKj_rCItROw0w1Z2ehe0PO8iq_4dnFvgXAAZ80BCo70LiepFyPZm19V_GX3VgburrGViDAfnv6zffRhurDBLKtJU2k0z8e6vxj61wXxQmoKQdjLxXrSSQiUmi38ywKaGUSN_HOXl_pNmircI01DcPDo0ROA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSst-zfn1pTNCF_3W8CENYPwILfNgPAH1yvzW5jVV4tTsAq2oVU7kePzd7VdJDkylbG5CBhaOFu2vqAkfnGlOo5kMBubuzRbRj49nNWOnXQrLZNrFXAUWUIndadao0IbR4twPpYd-cDQNakjf_5yYz9h9Ft-BaeyR1jXaSje3q6Cq3Akeobm9P3yBzCgf0UF6k87GDRoZhyWpGaMmZ1yitSgNeYUNRZgJH88Ag79MOf55Zf4FMHFkCsJX-7QstByh0kdymtZ_EoF6AA4p-g5JsGLaKDbhRup7psbu_Mq8qTlLMC1G1ppxvjC_yWw63rtVnqrNP92IdhDQ3mVmUZYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ1k7dm_GhiESAkJNSxJvmEyIW7HntmC-P8kywaMtdJEub-atDUktxYwqddoqOeRAQNLZpviPRXGd7UVGkfv-D4_Fc2uM7WgbV7mrwl1l8ZbRfPfxNJ16Rec-CszkJaTZam8bSOsya8k4jUhGcXPPKX_Y1adOhp60RTaBJiDmHyHEj4m53iZf4BSVLzXzxc4jOPH6UO-pz9uyzyG30FWPClTe1Yr1iAky0ge9kOQ_PUJI1IbY9uV78lesbhHIICJ1L69SrJ2Z5RGl7AEDbSYP5qdvTLfNuBPGszUuKyYo6b53Mseb5PF2IaIdG_3OjYhKHwB3MOT_Kp4fCYBWvcoYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=IJrlJ80pk48V2nrK6GhvJK2jG4_a5MeKzKlUvcMhBu9GKkQCypxFbLr_7N0VqCt-RRNzQioBZqKUdXxGz3H65BOxjQbMGjT27oTnGVTANc4uvqbonh6DvFhFRWhQc_vbR_Qre4P01lafgsaBkT9A_qUgfHvzuJHo3gMU0hdXVz-k8AwFT6cuWaMgM03iEmYP1kDgAu5IjrUKfCwRFlunTvQFKq2Zjh5hDOctprJ6Yxdxb3x_AxQijfqnFyf31My61pMu48arX2tvCjRQgBaxC-UMelFt5vlAf59icRlToecZ0222-zQq8Uy85kuHKUpAAwbPJl3GdXl-_1sxYdQXZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=IJrlJ80pk48V2nrK6GhvJK2jG4_a5MeKzKlUvcMhBu9GKkQCypxFbLr_7N0VqCt-RRNzQioBZqKUdXxGz3H65BOxjQbMGjT27oTnGVTANc4uvqbonh6DvFhFRWhQc_vbR_Qre4P01lafgsaBkT9A_qUgfHvzuJHo3gMU0hdXVz-k8AwFT6cuWaMgM03iEmYP1kDgAu5IjrUKfCwRFlunTvQFKq2Zjh5hDOctprJ6Yxdxb3x_AxQijfqnFyf31My61pMu48arX2tvCjRQgBaxC-UMelFt5vlAf59icRlToecZ0222-zQq8Uy85kuHKUpAAwbPJl3GdXl-_1sxYdQXZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=t81phrgs0qOYW-tM67kEaGNYb5UBnk3ErzEf9PZKHF5DRn8uAuso2hRnTGFq3OsgsMDBENlLwvbZBZDR1FXL4APlG9QcgEf3CmO3GvIJKTZu7nEn2q3yEi-KggsU_1yKpp-nhRXiDzsllFf3l_4mB05LhOCMvMnOeFlEMMp5z2_1vpStXI-o-gwpc_eY9KN5gmfm-EfxBIgRvcEPJqzucU9ctCB2dNtUWCFRs_c3k-WtMhD8ATE8GyQ40qau2tdbiSzobmJu4mYXS9MH8y5162WWhJ3SBy1KdeS3HX9HuQw98bcodNaloyzu2g_qz64jMnspp0Aqa0RHj6yYycxfRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=t81phrgs0qOYW-tM67kEaGNYb5UBnk3ErzEf9PZKHF5DRn8uAuso2hRnTGFq3OsgsMDBENlLwvbZBZDR1FXL4APlG9QcgEf3CmO3GvIJKTZu7nEn2q3yEi-KggsU_1yKpp-nhRXiDzsllFf3l_4mB05LhOCMvMnOeFlEMMp5z2_1vpStXI-o-gwpc_eY9KN5gmfm-EfxBIgRvcEPJqzucU9ctCB2dNtUWCFRs_c3k-WtMhD8ATE8GyQ40qau2tdbiSzobmJu4mYXS9MH8y5162WWhJ3SBy1KdeS3HX9HuQw98bcodNaloyzu2g_qz64jMnspp0Aqa0RHj6yYycxfRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugMyO6z0lFTERuz4j0r0smhdQ6Nqz1aSLVsO6wOfL8WSRkgvmH3L7QRNHgjOaSSrVnIl-4sYqyWzu-HnbM5xKKP8p2SkvKQntaX_uJfAZ_lQirF4vnBeH7ztcvQihjrq6qGWXi3V1hrZudH4jZKGls7E2X6z6oqXCy9ObMdq1fLC746_OQb2Wf1QN_UCgY9c6rX833w8qWIkaCDaRRVtbAQTsT6yR2MgmBfmgaOQ48r9rPq1kzlDga85XJeh6dYzJHrNTe_uWfo026n9SqbVSoI3iIqUu_sKjsyzDjjoBtkrBITdHHOoZv6oUhehdJoApHVTtGYraYAW3qAxkrB6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=mZ5LcOVoqt_whjTtAU4MWybS_QXfSY7y0IOitj-gZHYCqfYKGXlQPyqDKzRQ1kC5x2Egl4POHaQ2D5p6GCQKADrgqxZAnJTLnp7d8Fs0I5ZrYmvFXyBBMAVKSEuDamrX-_nTFN7SiaWui0vAHirfQqV3wJHbAIAt0gNFRugojOuMet7gdPHaB5YJZsnW1OuYtb37GYHCgbgcJJ8mKuo3Nb6_NYTFiDg5hMNsutbqXKw5siyOjjaSfmcc8ASw0HPFlmY2_IUnzE75ffZcNcKBRMqSyyh5URh6JxmfO5Fq1HLViyq8GgndIBJGaQgVSgOVrXlFORWqSVo3AhbeE8xIczszgOhG4zFe2M8KXCE3poF3lNOC_uT3zk3mAfhYmdYWQEMEAW5bwe5JwaU4ZQE2rWho41IGrvTbtCB0awpn9zJzLJGN9Hwhm9acyIWr1AdA14FcS-BPjxwukfCEoaHsBTiS9UdZ1uT7WqePyIDCt4SHyMBjA8J6CxRYC7bTC5QgxGwhlhQMjOrHXDyWWL0bLE64VxjTZFeeHV3NqenYrLIdLNBBThDxdTVTG7rZr0ku38Xz8CN2GMW3VBAAPp-u1RO7rrS0ei_wf0Nz58mOfM_fz7il5ql1yBWJ__B0T-VuZW8vaEhBSkQLo94GQ0ECmbGRfoMLpDeuCXFnxiBLbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=mZ5LcOVoqt_whjTtAU4MWybS_QXfSY7y0IOitj-gZHYCqfYKGXlQPyqDKzRQ1kC5x2Egl4POHaQ2D5p6GCQKADrgqxZAnJTLnp7d8Fs0I5ZrYmvFXyBBMAVKSEuDamrX-_nTFN7SiaWui0vAHirfQqV3wJHbAIAt0gNFRugojOuMet7gdPHaB5YJZsnW1OuYtb37GYHCgbgcJJ8mKuo3Nb6_NYTFiDg5hMNsutbqXKw5siyOjjaSfmcc8ASw0HPFlmY2_IUnzE75ffZcNcKBRMqSyyh5URh6JxmfO5Fq1HLViyq8GgndIBJGaQgVSgOVrXlFORWqSVo3AhbeE8xIczszgOhG4zFe2M8KXCE3poF3lNOC_uT3zk3mAfhYmdYWQEMEAW5bwe5JwaU4ZQE2rWho41IGrvTbtCB0awpn9zJzLJGN9Hwhm9acyIWr1AdA14FcS-BPjxwukfCEoaHsBTiS9UdZ1uT7WqePyIDCt4SHyMBjA8J6CxRYC7bTC5QgxGwhlhQMjOrHXDyWWL0bLE64VxjTZFeeHV3NqenYrLIdLNBBThDxdTVTG7rZr0ku38Xz8CN2GMW3VBAAPp-u1RO7rrS0ei_wf0Nz58mOfM_fz7il5ql1yBWJ__B0T-VuZW8vaEhBSkQLo94GQ0ECmbGRfoMLpDeuCXFnxiBLbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=adcpW5vlW1UBbJtcDF_Cmcgmm8ubmbcjKsx8gBlplmOHNjqqIOKBdp8VhSn3-I-J67ngWyBZwIr46hR7GBiW5I5WvTC_8B6kTiPaXZ6EFXUX3VZA0wEjUYD-_kQjObHM0R4_r_MSHcx9vCsamGddm72i8TUAEVYsTi93WMoF_gTwURqGYVomNr5gwa-6GAAvazOPNAD33lvBblmC8mkZv6DjD814FzTDmJWG4HsZzoIwAjth_57d4jVFLmJs8D79ad9QAeHK7Xx2Y5mJyyZnO0meybXDnuQSSxgcVxCF-wEACprI3TKrX1106itTEWYMShqUdSipy51rihfmD6lAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=adcpW5vlW1UBbJtcDF_Cmcgmm8ubmbcjKsx8gBlplmOHNjqqIOKBdp8VhSn3-I-J67ngWyBZwIr46hR7GBiW5I5WvTC_8B6kTiPaXZ6EFXUX3VZA0wEjUYD-_kQjObHM0R4_r_MSHcx9vCsamGddm72i8TUAEVYsTi93WMoF_gTwURqGYVomNr5gwa-6GAAvazOPNAD33lvBblmC8mkZv6DjD814FzTDmJWG4HsZzoIwAjth_57d4jVFLmJs8D79ad9QAeHK7Xx2Y5mJyyZnO0meybXDnuQSSxgcVxCF-wEACprI3TKrX1106itTEWYMShqUdSipy51rihfmD6lAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMkz5sX9PTeEjCiNSA9jacT4khR_vwGc8ITb05O1NmZh7rhkjkJHvoNoQryB6BrhMxengYInqgRdd6XFKuN3PogMiLgwKplKWfOZqxQ1M99jWwWHVAk5vJ4221314fnfK8rUOkUg-X5oFtQvLP5uEtV5wgiKp6CkTeCfcbDgiXqwiByVjiS9RORqam2zua0MFQf-F3COKUyGNBN_x8ocr44B-Ln82InY1EmxRwrOM72am1Ef_x0v--j0XYfKg76Ljkb0X3FU73SSkiWRRcN9cTh2JxbcJw99Kspd0LEY4scLajweA6VgAPnV34ThUryrsMZ3kTR45WlZVxRUldKDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=e28JKAmo-C1f02KuZCDZ3FiVvFP7rKcv_KWcgEsa_qnnPs3ckZtMwPC-elMMSrnxWhsOQbI1Rl7ISfW3xfTX_2cWPJvqDDxrd--23T_ahIwHhfdXaJXtHLzK4Ln7eSQP98qxtmt6AY4N5mJIj-M8z0p81NKkvSSMdoDisEAnFcfwxT-Ya4r2LpjVKcMr-bx_yOmTPdWvWADHLdh-rrZwZXEi6W774edvCP3tiV6W062hZPoTuqouvDDffWc-3YBVbMnwIRkCGhQNb2BWV8BltFORgOeOz_8k3WatU0JdRIBTjcmpsQaxsEdDb8cRKlKTVyzGXHf7Dn9dWtaS2Vi_jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=e28JKAmo-C1f02KuZCDZ3FiVvFP7rKcv_KWcgEsa_qnnPs3ckZtMwPC-elMMSrnxWhsOQbI1Rl7ISfW3xfTX_2cWPJvqDDxrd--23T_ahIwHhfdXaJXtHLzK4Ln7eSQP98qxtmt6AY4N5mJIj-M8z0p81NKkvSSMdoDisEAnFcfwxT-Ya4r2LpjVKcMr-bx_yOmTPdWvWADHLdh-rrZwZXEi6W774edvCP3tiV6W062hZPoTuqouvDDffWc-3YBVbMnwIRkCGhQNb2BWV8BltFORgOeOz_8k3WatU0JdRIBTjcmpsQaxsEdDb8cRKlKTVyzGXHf7Dn9dWtaS2Vi_jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1i8nL2018cOSIgcnX6Kq35ow18aHD2JE-6y1OEmJG1JIxqYIWNhu-I_lTo23eQD7ous07OyYNxdbYqAKRWw0ilubNYN9tbU_Xjj9PfFMuSgQNdNHrArPD26b6yD_UpGn2o6zDTY8cbA-rgA1rOQs754QIDu6VvvTBPI0t7-BnbegYSyIwS5Uc3-BQwF0QAr3A1js0ZZoXVpqfd1hCRd3z67qsNajpPATRVj6BnAIUO8ImlSLd_GQybuTxel3bYPFDsgtzNfcYsaaas3LFA8EreZ26mmC3gjTQwIYzLe74_F7qua_bECvL9c1qh_kwutJBferEDzdfKR_fhwK19Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLTniYphpNmFoB37EJxs61PtjfWe2uKoJObnn7MSmNRanI5ZSwCky4CGN5QKDoA2i0mAoAxpoTvFojXatxi-emNB4aEqJqHnnkF-JPwDJDj1GzoYaseAdvXgsfoccpJx4zMbS1pEiFFgkhGFhNcUc0j6Iv294poICVvamhJA1BtHXp-pOfMt7hp4BoxOZoz41OiWvY-iARiREKI0dhPd3aOtXH3Xl7B-hOTWEPbTGt1sS1TIKWHIRNaZlAFQVGvcMDLEgK5LBZMDl6VnW_Edenteeo3QyL4sAhxAMSgJ-83iBhZ3RxjH-smhsS94XzVguH3dzJXN2dfars-oRTrx2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=t2nWC9wSG-7uIAgV6QjgbOxu-HuYqiqtFwtHS_Uw0aeQiVePMr0B2nRUuTe5b_ciRnvowFmJC6QGHEw6UYlFyHFsZKfxwoMUA9QEZLuEwLdJMEyxs-xFbNB1jTdRJERrDQ0DiWm_2TFaffpNEkMUcmRI47sfRkiQumuXZS906x4dnLdzLxK97MdGKr29KAIv-ahFcQMCXBFbFr01utc5eQCokALOqvojEm9yt9-EHdZTYnLlhk-W73kzYF4-wvNh9o_R_QO7DyJ5H-tyvJc_3BeESG_tVkG7oyb4KRTNFiOcnvjJaM71jmDo3NnDbQcA36UATBIpWyv18OwQeqizhE48rFeAj0lsFONQCHOpOW6_zQA6k7raFOsqMprNeChDfrdDtBv1Bkfz8WON7CP2Jr8LcZVm91hLkpz7Ztfm6wGoh9MogItef1SNWgo6IkggTcdwLSk2HXWqdpLXG09qSiUuycMXJJaXrVG17yd4L5uegYe8z7ROABlhiNTsOnNxbGcU5LhaqokMY2jzVIvHtgOJyqKdffuCkOd9x-OiaYvqhq5xXAFthxHI3IFCL5c-8ztrcpd4PXYQTJWzLzU05hLLGY_ZcJ1tzp4ougXDO9Ft_06-Wn_iuD-xpADo-ZMnZ09ptnqLaF9Ps0esYNjmVJk78I9O6YvuJm6pv2oizqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=t2nWC9wSG-7uIAgV6QjgbOxu-HuYqiqtFwtHS_Uw0aeQiVePMr0B2nRUuTe5b_ciRnvowFmJC6QGHEw6UYlFyHFsZKfxwoMUA9QEZLuEwLdJMEyxs-xFbNB1jTdRJERrDQ0DiWm_2TFaffpNEkMUcmRI47sfRkiQumuXZS906x4dnLdzLxK97MdGKr29KAIv-ahFcQMCXBFbFr01utc5eQCokALOqvojEm9yt9-EHdZTYnLlhk-W73kzYF4-wvNh9o_R_QO7DyJ5H-tyvJc_3BeESG_tVkG7oyb4KRTNFiOcnvjJaM71jmDo3NnDbQcA36UATBIpWyv18OwQeqizhE48rFeAj0lsFONQCHOpOW6_zQA6k7raFOsqMprNeChDfrdDtBv1Bkfz8WON7CP2Jr8LcZVm91hLkpz7Ztfm6wGoh9MogItef1SNWgo6IkggTcdwLSk2HXWqdpLXG09qSiUuycMXJJaXrVG17yd4L5uegYe8z7ROABlhiNTsOnNxbGcU5LhaqokMY2jzVIvHtgOJyqKdffuCkOd9x-OiaYvqhq5xXAFthxHI3IFCL5c-8ztrcpd4PXYQTJWzLzU05hLLGY_ZcJ1tzp4ougXDO9Ft_06-Wn_iuD-xpADo-ZMnZ09ptnqLaF9Ps0esYNjmVJk78I9O6YvuJm6pv2oizqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq4v68gu8qZgxyv0x79koN9sXy2NfJgr4zlAPbJoX6sqmqELWbjEQTrbvomHOnxNkcWSuj4Y4tmBXh6xWHmv2-c4UUln_v5nqIwWQ5t-kLuK2HRLPJarh7TO-HWwseVqrFf8qRFH0MYhJ_eeOtKNMZaxnPlvXSWOICRGJG6AQlCxP3cYAWO8Vc2u-mCs_q2i0C51UfNBfmdQL1FBOAT1OCqHUNqj6RQI6wpzZcp-4LYvHpkr_iMaIICbQOuYB2MJ2qcoYHXnRekwaT5Xx9MPUIHzsrS5EMJhyJENDX7YT50y31aHd2LpgYoc6WVj3ft7HTw7hRHklbhC26RpRSIS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcHxkj6C72wV43Bq20KAQFohBCWsH5WAQZo4JJWQY1uB330QcfOqa4ZeZ7YeSWrLZyvUJgUjY7Om89ydf3sRy4PQqtpTOkZWoirgFNBa5YqHQ5-JHyjouO0BIpoeIQ19mIJt9rGbMt5z7V49gonQr4iRjPGx8Cn-YFkMAmlYPN8-pvv-Ry5U5ZweR-bP7YgyBSX_Kcn0-qGwDusUSLjb2IAjyiMb47tIuG6K2ZfyfiLih6t8h9vo3GDoDdtfNW_IKBwkFsg2t1azgDJo4P-wROpHlbYTmc3HG1yhgEu1hnnN9VvoCtoDbWELS50kGt7OZWg2W4zABk0eXfnFXnXAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=MthsD2Zz-2gtjWVPjiVUVp4rRofFqV06icOvyX-coVYOvUnHgFPpq7aqr6h1NzMI__5efdfz31jmOQeHRi8XTz2ym7ZsVS6NYv47Qae8bdoFlQBgRKgLjga0mDpJ519IH49Ph_8VaiNgm_1B-V4iZokoYhFBQuEtctWXKzdA_k-Y6h1wfhBdl8W-NuWeKceNZx8Wi4eTQmSMeNsvmv6CssbcL07lpg2ye8LQhnErRlz_5CWZ0Cyf7p7-6KaoxLavo2RbGZR402veplYicW1knua2Y4ycwCkkPzzCB4k0yPl-g7S-kJPPQhLB1HPtwhyJgyrfDQQNFXUz6HAaFwuLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=MthsD2Zz-2gtjWVPjiVUVp4rRofFqV06icOvyX-coVYOvUnHgFPpq7aqr6h1NzMI__5efdfz31jmOQeHRi8XTz2ym7ZsVS6NYv47Qae8bdoFlQBgRKgLjga0mDpJ519IH49Ph_8VaiNgm_1B-V4iZokoYhFBQuEtctWXKzdA_k-Y6h1wfhBdl8W-NuWeKceNZx8Wi4eTQmSMeNsvmv6CssbcL07lpg2ye8LQhnErRlz_5CWZ0Cyf7p7-6KaoxLavo2RbGZR402veplYicW1knua2Y4ycwCkkPzzCB4k0yPl-g7S-kJPPQhLB1HPtwhyJgyrfDQQNFXUz6HAaFwuLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=oZmgO-rp2SlsHz8g4YmPugjspR9s0elpZN9ud3hCfQZhZbNmarpOsWJTt1w5ytL7e_MxoLNTXwOxCve8Hmf7j9h-kEdnVYLjF6GaHLMjA4L82wneWoVeDM4y9FBaYZza8Pg163QADIaeBh5B6AtpmR02f2ccd36nkY3oAtQON3m9d0Jqpl4eA6DRPYgPgvRxvsKA6q5H-ZBIxt_PusQldRiQd6dXJkJSFwgx17dBIr3aLlsOgYQj1dvELaeNVHvmKxFd2BgI716JAuPuKdApQIJdH-cfIvo8eYlIcgVuMU3rMumyNQlNIcIpsj9sWbEc886uPXB5o2jhntoPIhRZxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=oZmgO-rp2SlsHz8g4YmPugjspR9s0elpZN9ud3hCfQZhZbNmarpOsWJTt1w5ytL7e_MxoLNTXwOxCve8Hmf7j9h-kEdnVYLjF6GaHLMjA4L82wneWoVeDM4y9FBaYZza8Pg163QADIaeBh5B6AtpmR02f2ccd36nkY3oAtQON3m9d0Jqpl4eA6DRPYgPgvRxvsKA6q5H-ZBIxt_PusQldRiQd6dXJkJSFwgx17dBIr3aLlsOgYQj1dvELaeNVHvmKxFd2BgI716JAuPuKdApQIJdH-cfIvo8eYlIcgVuMU3rMumyNQlNIcIpsj9sWbEc886uPXB5o2jhntoPIhRZxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=M7-hjkcKvOo3QmBgOSN0Vgd899CpQyWCqH1VOIDkrwKVfTb-yGH9EKB9l2ctKYyVQZW0lo0qpo7KljiCuIDZwsCp15sFJVHo7LNP4FiepJM_PTF5BdzvJH3KSKA3lT3oaKCJodbpQaozfw1udgTL5lai1FCcnldbY0pOrgjX9_toRJyEu9gw5VrFMUL3RvOBA4xihplwyGc12ncY3OA5Gd-DiN9pt3xM0XcL797EWcGelNu80vFRCwaJ74ED2Hbk94FjEvgHsgNkXLReWEOLCO1MRK8zCiWiFSP74GmZz10uwb1LtPTY6y2HyIkrs4HXXRk2yuwEJihCyNU9pTvXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=M7-hjkcKvOo3QmBgOSN0Vgd899CpQyWCqH1VOIDkrwKVfTb-yGH9EKB9l2ctKYyVQZW0lo0qpo7KljiCuIDZwsCp15sFJVHo7LNP4FiepJM_PTF5BdzvJH3KSKA3lT3oaKCJodbpQaozfw1udgTL5lai1FCcnldbY0pOrgjX9_toRJyEu9gw5VrFMUL3RvOBA4xihplwyGc12ncY3OA5Gd-DiN9pt3xM0XcL797EWcGelNu80vFRCwaJ74ED2Hbk94FjEvgHsgNkXLReWEOLCO1MRK8zCiWiFSP74GmZz10uwb1LtPTY6y2HyIkrs4HXXRk2yuwEJihCyNU9pTvXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe3NUVkfpWWIhSfvtSyKsn3LofXZ2b5i6264gildaE9Fei_tlJJExR2JJ7twgfFelIOxmKV_sNN1kZhOwg-0Cs7Q-dOdA8nNfC9mlvxanMVpEreetYigjpvpeNTSDuf8HT6BrcHpQhZSRMH7r6lz86M2aSuXRzJudaP-l4a3TU1TVO_TPhItrpronMaCWf2Y9qB7Lh7BwCXRP3Dbav119mILhD6TwOPglBNZcCw5vzFj5oUrg7hKmdrDe3GTYKQI91EO1MjR3rJCEU8LgSqpe7L7zfqkonPx6wcrxNwWoI3ALVELCroQSa3dAjcoAy6uMOalo0k_yUrLeGITl2G9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KP0NHGVYngcuEH-NDVRLKj4ssgSWJZ13JXsPr_86g62m2EFwTSoRdWHiiuynfaUrg_5Cr4Wr-l-_MaxEVx9UgzKy-n92ZPdIF4kJs-XQsE_TEmLERZIjqfuXeJQEVF511J0JNbirStM2Acc7oBMcTHiYf7AzjbGjx4da5kYajcdUJ42V3Wjm5LHyG_UQLFQauXnrOdZYfgcSoiZ0DJ4TsDrHqfvaLUfQpizb4q05xEVPgVV4VPErQZk7mUJCaRdil0BcEDo1h8PiXZ8xm17067HV8gOTNYe8A4WwdqqzhifHvsUd3GzqvCvgK9-PtGg9RUTvGY2hBB_f49SEpnzyCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KP0NHGVYngcuEH-NDVRLKj4ssgSWJZ13JXsPr_86g62m2EFwTSoRdWHiiuynfaUrg_5Cr4Wr-l-_MaxEVx9UgzKy-n92ZPdIF4kJs-XQsE_TEmLERZIjqfuXeJQEVF511J0JNbirStM2Acc7oBMcTHiYf7AzjbGjx4da5kYajcdUJ42V3Wjm5LHyG_UQLFQauXnrOdZYfgcSoiZ0DJ4TsDrHqfvaLUfQpizb4q05xEVPgVV4VPErQZk7mUJCaRdil0BcEDo1h8PiXZ8xm17067HV8gOTNYe8A4WwdqqzhifHvsUd3GzqvCvgK9-PtGg9RUTvGY2hBB_f49SEpnzyCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=E5vWO3FBeuuYxZSMlXmax6186lWqpwhFN1d5jDSKDPhKyrXlXRK1YCCjlMMZpi6cgm275qADZUkj8F9rLDcI7dca9SXAXN-sDHqWLPC6U4TaY4x76jTEcOj51UCKIhdpNDE4Ld_V7GikqT5ZDfEMipERPqBTFX9ijUUT3eOAzRRiNi1UZzZe2KloYIk-2d67EL6sH3OOBCgUoqIDfYU-xJz0waxlmyVrytfce-0FmooEqntmqlgSk5JJNzHt1USRrItyB7AMc8APcOIgPEDkcbY6A_PanRf0mtLFCNRS13uJDE8B8yR8rSajXYgKYBPY2XPQ6YibbwdmplS6quLP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=E5vWO3FBeuuYxZSMlXmax6186lWqpwhFN1d5jDSKDPhKyrXlXRK1YCCjlMMZpi6cgm275qADZUkj8F9rLDcI7dca9SXAXN-sDHqWLPC6U4TaY4x76jTEcOj51UCKIhdpNDE4Ld_V7GikqT5ZDfEMipERPqBTFX9ijUUT3eOAzRRiNi1UZzZe2KloYIk-2d67EL6sH3OOBCgUoqIDfYU-xJz0waxlmyVrytfce-0FmooEqntmqlgSk5JJNzHt1USRrItyB7AMc8APcOIgPEDkcbY6A_PanRf0mtLFCNRS13uJDE8B8yR8rSajXYgKYBPY2XPQ6YibbwdmplS6quLP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dvw2UoPq0rjg50hYX-ddBXU7P_guIpOT7uHW_xpQBpLqaVDqcudy6KZkdha6C9JpYPIQp18Qh50_AQrfzsSUMCPlAi86_lRiDdUnAfiVGzl2Q7jwshlRQ2Oql40uBz-kRcS2flRb9ftzKhG-QzSMl0BYcuiuE5gx7spCRrrnPw1i5nffr0h3iv6hOXesCbtvNctm2Mjvr4KXBEs7yQhddKFne07PymJ1cyI4S2Im3AGQq6-833nml4x3pKOc9bAu2Hw987azQIPw-SWxkp6eqPXHjm-LqBOWEHNXZnYGs2TrRkqP5sYuGTg37GUchZTo6f-wXVv5TDkaIVe-8THlKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=is21H4GoVzJOiJwvYsaI8afW5v6sUNaQpsAMIhMFJouN_g30IhZtGlDtIdmRj8jrp-QwesO19bu1ePGr80SCcl9P4l0tm4_V3Vn5qH6zBhcflWPKNtSqQYxpWOZ6BFCJ4GhG3TiwYIhg0gyBE6S63R3o8EkPm8hlcc8nWXIqswYMkIdLn1mSKIJYLsGf0InJQ1ySVbcWkucW2BmtC-_3SVYwhqgZODjNV3GM7bknud9wCcyuGkxWhr4mOwy1QGkymDdQbLYCISZkcgZFBKLpQXE28VUnxoEdA_0wKsyg1Oj9iLpaYf-IzEuKVdQ2TQINSq4G4UJbJNsryD3-xP8EPWX6myoCcOEhWk4JPB8_M7h-h1nuDtqlZpy97JZBk1kSI7dYIT3PnBdzDWUf2FYVFLhvA4M6xe6jWVnv11GSKtOuXKkO2NzmhlCzhCpKgoQlBeytImy9c_iLgK5CH3oSDtSyq_98iNIi4D1ojQM8AH3ezbjsuvZ94WXVyoGdEpJVQazOJQeDhlltehpcAn4xakXPmqlWAx_2n_nRhVTPq_NHFyczxj8APaYCYPcyJbjpcS4fecsYM-Rfja2Znjb64wxhWlA5-yLulKG7ULtQ9OwBXw1Rv8dp_UjNGQYqu78_vEhtTlNU-INh2KEPy9pz76ReOA82f9qv_Ggp8movVtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=is21H4GoVzJOiJwvYsaI8afW5v6sUNaQpsAMIhMFJouN_g30IhZtGlDtIdmRj8jrp-QwesO19bu1ePGr80SCcl9P4l0tm4_V3Vn5qH6zBhcflWPKNtSqQYxpWOZ6BFCJ4GhG3TiwYIhg0gyBE6S63R3o8EkPm8hlcc8nWXIqswYMkIdLn1mSKIJYLsGf0InJQ1ySVbcWkucW2BmtC-_3SVYwhqgZODjNV3GM7bknud9wCcyuGkxWhr4mOwy1QGkymDdQbLYCISZkcgZFBKLpQXE28VUnxoEdA_0wKsyg1Oj9iLpaYf-IzEuKVdQ2TQINSq4G4UJbJNsryD3-xP8EPWX6myoCcOEhWk4JPB8_M7h-h1nuDtqlZpy97JZBk1kSI7dYIT3PnBdzDWUf2FYVFLhvA4M6xe6jWVnv11GSKtOuXKkO2NzmhlCzhCpKgoQlBeytImy9c_iLgK5CH3oSDtSyq_98iNIi4D1ojQM8AH3ezbjsuvZ94WXVyoGdEpJVQazOJQeDhlltehpcAn4xakXPmqlWAx_2n_nRhVTPq_NHFyczxj8APaYCYPcyJbjpcS4fecsYM-Rfja2Znjb64wxhWlA5-yLulKG7ULtQ9OwBXw1Rv8dp_UjNGQYqu78_vEhtTlNU-INh2KEPy9pz76ReOA82f9qv_Ggp8movVtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsz7jrjoIARFsGgiSsQRoL6643r8hC4WUbQkv1lNJZhFxAhRj175ExWUqSUgm2SEhfhG-U9IJCXlBwbH5nS4W5vr2-el2_mhGzW4bxeNgf2IFDlYxHDEkalJsKJJB1qy_aYXwdF13QQsoQbB26fjx_uZREDdsEynlm42bzZL3xOLoIZr3-ZcK5fKy7Kue5GR6Tjv7QW_z-IAZRZkOSDwqY-v-TxewEFuoVGor4xZRt44u_G1eRZaGbe3n3JgFtvnoKHL-nATZvQt6HI-KJeg9t_Nh_vqv4Hgw0Jz2QcBhlqmN1X8-pbehQvGIzYygevOaEg1ee2CG2ouJQGNuKNqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=lF-E4v3_-lptLoPxDhA24uCHM3h8OkQeW_g3QPeAAEX0hjZKX5ASyNODrsYYpc6s2Rci0mE93vy_vmhdM16WnfyOZnOOrMozt3moN5cY4yu9CSatbpzXrZoMc6e93M5W1AuGVV0gPTB9iALEUKOGJ_IbuWqApnRQQo1IsUFyhsnINt6nDbszdZsmkfTlkFhEIYOnezltGAt7MQkkHbxQaddLmHhEdoedaMhyUTCzBWI-akK0Luaq20fuU3ZBEyek7Yg5wbO5hgxfCQqDSLy-bh9dtVamZpyHooVwPyGJ4WtRNGm5LtiBELYu0i0Tbf3bsUJeUL5WOITFDQRyfZVjwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=lF-E4v3_-lptLoPxDhA24uCHM3h8OkQeW_g3QPeAAEX0hjZKX5ASyNODrsYYpc6s2Rci0mE93vy_vmhdM16WnfyOZnOOrMozt3moN5cY4yu9CSatbpzXrZoMc6e93M5W1AuGVV0gPTB9iALEUKOGJ_IbuWqApnRQQo1IsUFyhsnINt6nDbszdZsmkfTlkFhEIYOnezltGAt7MQkkHbxQaddLmHhEdoedaMhyUTCzBWI-akK0Luaq20fuU3ZBEyek7Yg5wbO5hgxfCQqDSLy-bh9dtVamZpyHooVwPyGJ4WtRNGm5LtiBELYu0i0Tbf3bsUJeUL5WOITFDQRyfZVjwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP74cLbkF2fNib6gAnO5McvVczWAiQfYYLLa2RghhUZN5ssmMRD_LHtq05gClKrBmUuVWyIKDg69It9N7bxStm1Ux-c_fNMGK6wslun9NuBa5FjgoKyeqcnN4WXgdBd8vSR1jz0F8vH6Oh-QW3YQF2C_sDnA6kFaLICA-zFBFGT3j2IJH8qzjbwsN4LLDEIqyiwbBIVqpZV_JJT7c_m1r6J20hGLMBenBVUDqhxK0vc-5-EVG12PfltE8c-qDVq8d6orF7jTabT6h7DybuNs5EAnDhVRQpr03aLgkVU_0infKn9Y-Xwug1wfL1XGd9V397klzKdsMzqwnVfrBs5VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmtnXuz7LQR7POeJPe28PD-gtJGJ6eaNsXJiSCw9yhwWBHw1jogSDrLDFKqQUwbiIrQVpeCzSIyBlj2c3pWHI38ozQW3L2dFEl6r5D61yPRh8oC8Dl6pYmYtSLCAjTHG3DxrQCV4iSfWNZ7XbWBc-a4Jiu1FNiDl9A9aOv6_K-W4Itnwt6sj72BbjpS-AY9WGIuh4biyQxs2uK6UyuNL0heX1sy-N37A4-3a9owIjLfx8-1mMnSgsDgKGYpyNo_8WkgFCpeAP9ZdVYmRqFQbkNfinpPukHrbjsecSlREGb3QJ27ZvM0Ot_SA0PZf3dD6XW6d532_LN0i_k0p12v5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrxVbOelBTKzONMC_GatuIqnSEwA0Csho1FlAMVniUefdUr9COTPA05c2_ajUA6KZEZ0Nt7wgx_6yEmrueg9mLH6Yqqg3uIDm9TpRKmrb4U4E4o3WQQscAUTCjLOiVgBsZp_ddxTesH8HZlHwocDTVKFlCYPG38EkskerlZGiL_fVmag8-c77ArpT2_01mlXnYKnKj3niqcV7h4T97swgkv7WLBLN_hfl3hjOY98HfQ-s0tVjEf-HqmWNvHv0mxecxk6YTEkHVX0lsPx_aEmAo9x5FQe9lmqH_buMNZ8y9WS1Hmcdk2QBBCnwrtXDbD9kjX5bRxAjJbzztJnsCNV8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ElI6FfqYiw3sxfS3kp7vIJf0JhC9PGPHHuFbRWsA9b1OGIX6gSEcpGg4ZonbfO8nLZHZmqYiIkP3TOLZsIY-p7YO1uic55dirv92Pjkk-_qWJtRXv8eQWHiTExHLCD7QS5TDNQ90rv-Tw5DZq5kbopRtgoNH5Wqi4V71jpiDpQXU2Jv5Pe0HboUfpAxR8OXuEAI7a78T8otPHghf42CwK1OSSTHEQ1rrna0_2P9_Wk1ytrYP_HwpvNZbeh2abG_4dTOK8bxnjEUx-vj6t_NeG_HwKpb1IG6c6OgC9Pjcl4hzcdLUU-2KGXwvd-awQUrpJntV_o2QupJxZeheeWN6Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ElI6FfqYiw3sxfS3kp7vIJf0JhC9PGPHHuFbRWsA9b1OGIX6gSEcpGg4ZonbfO8nLZHZmqYiIkP3TOLZsIY-p7YO1uic55dirv92Pjkk-_qWJtRXv8eQWHiTExHLCD7QS5TDNQ90rv-Tw5DZq5kbopRtgoNH5Wqi4V71jpiDpQXU2Jv5Pe0HboUfpAxR8OXuEAI7a78T8otPHghf42CwK1OSSTHEQ1rrna0_2P9_Wk1ytrYP_HwpvNZbeh2abG_4dTOK8bxnjEUx-vj6t_NeG_HwKpb1IG6c6OgC9Pjcl4hzcdLUU-2KGXwvd-awQUrpJntV_o2QupJxZeheeWN6Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwZSB0msJ-cexi61t0YbWJWOGvkdF3ZOmnlvZOLXu3e1b6INGr2GUGoNKDGg3iUhdDwCXHmmiFuC26iz0YmiMsZa9Z_XH1OSP7IY4JVIryYbYx2_0fGn_dMgv5UbQjqAZ93mbkr92rynkHxbyL0zDVu7yVKZhFgWiiHxws3PaaJmk1kjESnhxsBDYcdj6IfEC-p2OOzun6umOxBJuB_KAlRJqHsiFQrNRyDWltK_VBE7mbyFazQtj91jNPRwtodHxoSxeKgDa_4Q31ylFl1YAzQU1Tbqtz-x35sbJI5Ip9Mgvdpwejm9nZgvtrLKNV543IZDXY2ajKxO9icfF6b7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1ceyBDBt9JsUdvTCCOBTgkqnoBAgNh8pbpHSeu6PcyNhhnb4m2MKcNULtYlIEzbiLVsNndENYVUkOJ9F5j94RaEHi-sQq-ETqBbwQ23FiSRh9XorvN8wPu8iwfDGpIWPk_9srk4n_73MZIYmEc4j_IksQ_DXC26zd91efXbYNx3B1Zt63YcMyBI15EaK9bTdbTOzcfhGmM6uA_d1fL8nyIMnEXo7x6gLCv-lQWU6OTdehJmIyq3hpWFJtCsCcE9EPfxeTSzYyHLl5jiFdZI6_8gGY1S2MadMnF0A2lgFf4RU-JcTvf12-M9MwOL1ENgRkdSUDaYfcXE8rjFvKM6i5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1ceyBDBt9JsUdvTCCOBTgkqnoBAgNh8pbpHSeu6PcyNhhnb4m2MKcNULtYlIEzbiLVsNndENYVUkOJ9F5j94RaEHi-sQq-ETqBbwQ23FiSRh9XorvN8wPu8iwfDGpIWPk_9srk4n_73MZIYmEc4j_IksQ_DXC26zd91efXbYNx3B1Zt63YcMyBI15EaK9bTdbTOzcfhGmM6uA_d1fL8nyIMnEXo7x6gLCv-lQWU6OTdehJmIyq3hpWFJtCsCcE9EPfxeTSzYyHLl5jiFdZI6_8gGY1S2MadMnF0A2lgFf4RU-JcTvf12-M9MwOL1ENgRkdSUDaYfcXE8rjFvKM6i5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=kVgNdcWiA8Y00_KzNuhRLxUZJ_-xHV3bEr-WnVhJgpJHUHIx-DD4-QIf0tgLxqhrASWjsK2ThTlA-hcSYbkysT9uuwSU0IaKuPxZvQPX4vgPTnqEdcSCAZ9gIu08TmAprHQM_zTRY__AJIeh4u-L5y-AWSLY6ItQJmedK2WoAsQIRHsTUeTnQPwOLkERhU4ZlDRtqPZFyVbRnmBM4zGi9pyDzhccnsoxtHzsbfqqOe1EiLqI5Oq0jAHwLKp_xnB1yD7iZw4vuQORSYs9vGt_CD1_R0VrejxFzUCIXykRs9lNjbpWFQimyiEuUIObbhbRm5azc5ra6I9N3Fgx6_3bng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=kVgNdcWiA8Y00_KzNuhRLxUZJ_-xHV3bEr-WnVhJgpJHUHIx-DD4-QIf0tgLxqhrASWjsK2ThTlA-hcSYbkysT9uuwSU0IaKuPxZvQPX4vgPTnqEdcSCAZ9gIu08TmAprHQM_zTRY__AJIeh4u-L5y-AWSLY6ItQJmedK2WoAsQIRHsTUeTnQPwOLkERhU4ZlDRtqPZFyVbRnmBM4zGi9pyDzhccnsoxtHzsbfqqOe1EiLqI5Oq0jAHwLKp_xnB1yD7iZw4vuQORSYs9vGt_CD1_R0VrejxFzUCIXykRs9lNjbpWFQimyiEuUIObbhbRm5azc5ra6I9N3Fgx6_3bng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=n6brak3gi0zZ1GJZAmXrG-70jHsfBpuSuBJQpCkJwTNZLuRifz05adirctASS6HCKkD0CJfg4RE2Uxljj5a0vOb0nEApBZQIiqNJTJHuFvVT6Gy13gutj2oNnOZfSK0XGk3ymFKAymnYqbc1K6HB-oSNVsOyRBlmZ6_Su8LJUWrA-YN9Yv4zaIEI0dxZhZtTv7xr8DAkLKQrC7U_eON4hQ42jDk2Hjj9bEeWRihQJ5QWQuTYD8Id5vtQyzZNeEf-RKn0p-e9MQyvE6WU_X0wEiv8M2GmpI_DyY3nilClFOYvch_j9wMl-T8ITXHL2NS7pHe7bCa2sqs-mxpcuRC2sblm68B-bHdOib9PqGizi7Vfm6fmdzeCQkunZRdU5sNlarScuhCEWIC2zfTIyK6Vdyx8WyEPaojk4UqPSSekZqrUA37UQb-h8tj2SlLzya46hF7y-GhyB90MxiUNL_pNEfL3e2JLXcoPIMnNfu6eA43MZP4gS6PQZrrZVI5-6rN-3O7Oo8PxbXG5mlU63if8ZUw_fxlygEBUVc0UfPE82kzrj3ANv6wYiskb8tyTu-tiiY7g7Jj-fQVQ1QAvDkWoG3KtCqb0OPDftSY1LIN0cVWAyJOierObMgmUowfsWcgRg5keB2BRsPiEd2rEkrIj_oO9xJxAmm4C0-1_pLCK4VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=n6brak3gi0zZ1GJZAmXrG-70jHsfBpuSuBJQpCkJwTNZLuRifz05adirctASS6HCKkD0CJfg4RE2Uxljj5a0vOb0nEApBZQIiqNJTJHuFvVT6Gy13gutj2oNnOZfSK0XGk3ymFKAymnYqbc1K6HB-oSNVsOyRBlmZ6_Su8LJUWrA-YN9Yv4zaIEI0dxZhZtTv7xr8DAkLKQrC7U_eON4hQ42jDk2Hjj9bEeWRihQJ5QWQuTYD8Id5vtQyzZNeEf-RKn0p-e9MQyvE6WU_X0wEiv8M2GmpI_DyY3nilClFOYvch_j9wMl-T8ITXHL2NS7pHe7bCa2sqs-mxpcuRC2sblm68B-bHdOib9PqGizi7Vfm6fmdzeCQkunZRdU5sNlarScuhCEWIC2zfTIyK6Vdyx8WyEPaojk4UqPSSekZqrUA37UQb-h8tj2SlLzya46hF7y-GhyB90MxiUNL_pNEfL3e2JLXcoPIMnNfu6eA43MZP4gS6PQZrrZVI5-6rN-3O7Oo8PxbXG5mlU63if8ZUw_fxlygEBUVc0UfPE82kzrj3ANv6wYiskb8tyTu-tiiY7g7Jj-fQVQ1QAvDkWoG3KtCqb0OPDftSY1LIN0cVWAyJOierObMgmUowfsWcgRg5keB2BRsPiEd2rEkrIj_oO9xJxAmm4C0-1_pLCK4VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=cM1Mi59bTKhx7ScFzLgKKcYAUuc4PggNz6RDGwbEC7P8vRdrl0rSmbn-LL6T0_i683vX7xYYGYaeBY31nPrLMQ9Eek7oYXYnaRt-rCs603Rke00DJtjPXedaivs0SUH-KQZ2xTT8j3an2EEtjb9vv4Trko5tI_DIIFV2tvj6W6ZwE0v27KpUpYXVMOo9t3pptkjsmWwsjPjiQgrL1JyY3Zl_1G713ROm8c2m1guOdigJ2_bxtXt2Mr0wZT_MQ6UdDSzIQBOswJpK-QFY7kLkypf91Et-f2GlP6fFoZmCudZ0nwUyXo-QuXYmB9wbvt1CBZ17PFGYoVyzb0tXCIt7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=cM1Mi59bTKhx7ScFzLgKKcYAUuc4PggNz6RDGwbEC7P8vRdrl0rSmbn-LL6T0_i683vX7xYYGYaeBY31nPrLMQ9Eek7oYXYnaRt-rCs603Rke00DJtjPXedaivs0SUH-KQZ2xTT8j3an2EEtjb9vv4Trko5tI_DIIFV2tvj6W6ZwE0v27KpUpYXVMOo9t3pptkjsmWwsjPjiQgrL1JyY3Zl_1G713ROm8c2m1guOdigJ2_bxtXt2Mr0wZT_MQ6UdDSzIQBOswJpK-QFY7kLkypf91Et-f2GlP6fFoZmCudZ0nwUyXo-QuXYmB9wbvt1CBZ17PFGYoVyzb0tXCIt7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya6rKufsCmvq-d7-PY4734XbXZQXItG06l05_xcl1Jhna_uAeacdqGxaiS6oNX3HmkOgnVDG9XyXTJGfHMFjvl0hgs0lEa6acgY6TubkF__cAydlr9wl1N7lCplVLszWFlkmNfbgGIHWFmnPcuIRZILgg6nnjAczM_uKApPJslJVeebkBXQe7t_IN4O2A3PNp96eZG7xSM-1csriZs9aM2BKu_IYUwIMqf-KBBuJ7geZP-cN7h_7kAXaNrb7YJalCwVOaD5meHvA0TCwK1q11i-RfKDAGPsgfEREcZLNHWopd80p4eAr3ltcoHHI25hFEqtdMOO4u4DgjI22rZ_tVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=RhnkUIlDDMvqUC-BePOGvPUTyz0QTqlFjoIyDsJM8UJHbkc1P441IUhP-YbetABMsRRecUrtTMlhKRCGRpHd3DGxoNylv0-AIKikwUOIVGe3Me_A6D1HzKxCHYlZ3D9q_ATULEDmNtALt_kBOZFH8140j3MWRMU1GP1hHeA_GPqMihGG7IytQLoOIxreDfAxa2Uex_4TF6wS0SpFOdVtaG4VK09Pr18yJ2mmbyKLAQnF7Jd3_d99pOWNIK6Cl3fgnxemcH6bFwvnlWq8XSt1z2WxOlAiIl5NXef_tDj2yStI75GC7DA4MUve17eOOGX80yMzNJgZD7CQGsNu4WCZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=RhnkUIlDDMvqUC-BePOGvPUTyz0QTqlFjoIyDsJM8UJHbkc1P441IUhP-YbetABMsRRecUrtTMlhKRCGRpHd3DGxoNylv0-AIKikwUOIVGe3Me_A6D1HzKxCHYlZ3D9q_ATULEDmNtALt_kBOZFH8140j3MWRMU1GP1hHeA_GPqMihGG7IytQLoOIxreDfAxa2Uex_4TF6wS0SpFOdVtaG4VK09Pr18yJ2mmbyKLAQnF7Jd3_d99pOWNIK6Cl3fgnxemcH6bFwvnlWq8XSt1z2WxOlAiIl5NXef_tDj2yStI75GC7DA4MUve17eOOGX80yMzNJgZD7CQGsNu4WCZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=F-bFw796jbJN6nloHY4P0nEDbOBmG3Akxuqy4eZD65OUQTT6hwLwqfdARVPu9mFH6wA6ShRYgcf3WTZEkSqlEKVFWua46EbuIj7m4pA_KqvDHM9I3eJowGiCpU2tSHvCFnrFSgR5pSr5vyX5poFnwbNtAiKiTu8s1eccwKJgD8Dm-9DGkHQCsfvmilae9Hh4N5QT9l8JeJZGciZhNPDSx3PTt_5Q0lxwhnz_eTIQzptzLiVwNRpZf3yR7p8oulzsQ6TD3i78DLPiAnhI18XV00GtBKesNjS0yIdPG1SbgfurBNFhJA3PcwbHUqLmAqe4v-MalK-LZGNvo4rPPNcSs5g87G7TadXwefemQmetyUKdZot0e0DGYTlnqzRGtgfoU354_if6--FLluTMI_yIBswcvrEKE1Av7J4SvqZWJpOSuRfK2k9g3tPeg1SC0vCY7knavE_rhy3m5bVbwyGY2mIDseO61sEoCA6BfYLBCOPYHgTFRW0X81vPpzWAXU-PFcFRVzbSMXERRhwFxyoMpAfAqLMYRFMvk0qjcD5maKZ_-MqwnZJQwn0ZQmKiuhfzKHjpWSNLmWMIFhukBUUr0suJbkTn6yBZTS1HqsA3za7CFMYsYbnkfeYga7QU-cmcYao7oGsZxWNzHIrT6tM54egmSrA6AbB7vGF9mJRlteU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=F-bFw796jbJN6nloHY4P0nEDbOBmG3Akxuqy4eZD65OUQTT6hwLwqfdARVPu9mFH6wA6ShRYgcf3WTZEkSqlEKVFWua46EbuIj7m4pA_KqvDHM9I3eJowGiCpU2tSHvCFnrFSgR5pSr5vyX5poFnwbNtAiKiTu8s1eccwKJgD8Dm-9DGkHQCsfvmilae9Hh4N5QT9l8JeJZGciZhNPDSx3PTt_5Q0lxwhnz_eTIQzptzLiVwNRpZf3yR7p8oulzsQ6TD3i78DLPiAnhI18XV00GtBKesNjS0yIdPG1SbgfurBNFhJA3PcwbHUqLmAqe4v-MalK-LZGNvo4rPPNcSs5g87G7TadXwefemQmetyUKdZot0e0DGYTlnqzRGtgfoU354_if6--FLluTMI_yIBswcvrEKE1Av7J4SvqZWJpOSuRfK2k9g3tPeg1SC0vCY7knavE_rhy3m5bVbwyGY2mIDseO61sEoCA6BfYLBCOPYHgTFRW0X81vPpzWAXU-PFcFRVzbSMXERRhwFxyoMpAfAqLMYRFMvk0qjcD5maKZ_-MqwnZJQwn0ZQmKiuhfzKHjpWSNLmWMIFhukBUUr0suJbkTn6yBZTS1HqsA3za7CFMYsYbnkfeYga7QU-cmcYao7oGsZxWNzHIrT6tM54egmSrA6AbB7vGF9mJRlteU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCjqEXDquJZxXUN3I7TMSExs6G_vs1tlnYBtp3FEujLAD5XbDpOdiUKfYbkLwLclDWPa7sAfbOcine4nn733e_22PowO8oazjyETag11DLG0m0dB4QOzc9Kfd059C29BaOI9Mymi4xZAMRsXzuHMRU0X3B2ethWitZ6VDk_xUUc7A2X-UwKRGV4aiQskiH1PBHQznaJOWcJGMITPxKZzgUXe6HC8DMe4Nn_fUp4SFcyHTMm9kR8HPZ6V9fYcCdGeYyrDm5nBwXlWQUIr92PUCd-l3qHVlA21m3UkovIyAOV1eM48K5eHaG9bCvhN-i7rUDwkQyQwb-GyTcdAtvj1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=OqOp4En1wlA_eytgu6oLvpjZFR84q4hlOo3J2j7O7OJPozLH30gre07h7MCKI_mELpmu7BwKVz2zQlcEWr_PnPHBjqPHugK8z4I3Casi2uVoRxzcyOT5wKvCZt6lS82iIprOrmEiWqbPTNZGVJlIy3Z5_2wT5N3GiaHoVu5AE-ltLA9GrSDHCyTs2kmogbaIPmHBqDMu8y60xSoY91ealfq1Jt228ke3xZMJSChpd0gaZ9O9TOnSoN3YrhgGRKb7iLlgLge-KX_sRN2e8hkaln8v_b8ECiDymKsXMZH10IEDtHvgvgP2whkN1AZ7uQRJdz1x-hDiOlPb_wL4GhIEsqDR7IdOcY-S1B2fthjjz8JmA48B05svUXn2eB6H2mK1lDDKn6w-e1DlcpbRizo3ee_w-p7ibVhvxqvQNtE3ZXJdxaGTIUtRlm6ZWKkpittv9Ylc8sdFyPjNKhdohNmhsfi5b22X9_qo0Ce2yRPs0qaHJgl0NFxjI6x6lY3_rdyQ2udK37GFSAkMXeTIexwpMyKpMtGw5rg8d-VXvlisdlO28U6GqUO3Iqwr5U6SlLEkACPHZHm26a3dcbsSOthcgPAkHRKCAYK20bZj5_cvo5QTdhUR4zQEKQ64Z-RD_19NUaau3e-Z6rcB0LQNdoFc9P_SfoAQw6dEmUFP5bOE0YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=OqOp4En1wlA_eytgu6oLvpjZFR84q4hlOo3J2j7O7OJPozLH30gre07h7MCKI_mELpmu7BwKVz2zQlcEWr_PnPHBjqPHugK8z4I3Casi2uVoRxzcyOT5wKvCZt6lS82iIprOrmEiWqbPTNZGVJlIy3Z5_2wT5N3GiaHoVu5AE-ltLA9GrSDHCyTs2kmogbaIPmHBqDMu8y60xSoY91ealfq1Jt228ke3xZMJSChpd0gaZ9O9TOnSoN3YrhgGRKb7iLlgLge-KX_sRN2e8hkaln8v_b8ECiDymKsXMZH10IEDtHvgvgP2whkN1AZ7uQRJdz1x-hDiOlPb_wL4GhIEsqDR7IdOcY-S1B2fthjjz8JmA48B05svUXn2eB6H2mK1lDDKn6w-e1DlcpbRizo3ee_w-p7ibVhvxqvQNtE3ZXJdxaGTIUtRlm6ZWKkpittv9Ylc8sdFyPjNKhdohNmhsfi5b22X9_qo0Ce2yRPs0qaHJgl0NFxjI6x6lY3_rdyQ2udK37GFSAkMXeTIexwpMyKpMtGw5rg8d-VXvlisdlO28U6GqUO3Iqwr5U6SlLEkACPHZHm26a3dcbsSOthcgPAkHRKCAYK20bZj5_cvo5QTdhUR4zQEKQ64Z-RD_19NUaau3e-Z6rcB0LQNdoFc9P_SfoAQw6dEmUFP5bOE0YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OPaORRO_VvsQZur3glNLpoc9MXYlyGowyITiSvOr5GgkUybh7m4AZwAZ4_A7j5F99Vv2W6zSsS_HSMdZQ8EC9NEI20LdV8cNK9_5ATGSZ2wy6KasJ98jFwd97jBYVGLphzvLLWJYdiYUr7PJVSlNaSs25GmusjSfjv1yqdiLgfYDcLdVsCJmcGXBl4tK6rOCLERTl8baxrj9nxb6nCTYSf4hL0WCWB19T3spGm1y9hwojj5N65tDpvPZxxBJcM1p_c4CdV1KsNrwEjZUvDgVevToynizkvXYs1h5Prf7HXo7M1I2sJYHkhEKjj0hd7P3HfQGPgufYA7xo9fNGYu-0aSJS5KNHjtYNiB-eKaG5C2y6WnQQq_XvUgE8Rljmhpa4UKrVpEwB92ZQkgjv9dNrE8aI5YkHtP-Rd2F2eQr_LIdwlPNWVBkXqYEl5coT1RCk_eGxQYbwMFDJ5Iv2I4eUVlVT8PDxSFa9EM45hkezcK-rT479rbHf1w1jb_f8fh6I5uxwlAGLThFwp2IiXlrQVEJ1jUfzWt8xK074Lv-TrGIGR7pLEy4bL5CoRslvKopeLPUvekWnfU6UNtccLxtMVVMYtty6OR4p8DdgBQsHntncg7_MKyg1eiNjDnze1AGQ1kQuDdg7nAFFxpfzE-5N41FuTxGXyr975M3rgfVuAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OPaORRO_VvsQZur3glNLpoc9MXYlyGowyITiSvOr5GgkUybh7m4AZwAZ4_A7j5F99Vv2W6zSsS_HSMdZQ8EC9NEI20LdV8cNK9_5ATGSZ2wy6KasJ98jFwd97jBYVGLphzvLLWJYdiYUr7PJVSlNaSs25GmusjSfjv1yqdiLgfYDcLdVsCJmcGXBl4tK6rOCLERTl8baxrj9nxb6nCTYSf4hL0WCWB19T3spGm1y9hwojj5N65tDpvPZxxBJcM1p_c4CdV1KsNrwEjZUvDgVevToynizkvXYs1h5Prf7HXo7M1I2sJYHkhEKjj0hd7P3HfQGPgufYA7xo9fNGYu-0aSJS5KNHjtYNiB-eKaG5C2y6WnQQq_XvUgE8Rljmhpa4UKrVpEwB92ZQkgjv9dNrE8aI5YkHtP-Rd2F2eQr_LIdwlPNWVBkXqYEl5coT1RCk_eGxQYbwMFDJ5Iv2I4eUVlVT8PDxSFa9EM45hkezcK-rT479rbHf1w1jb_f8fh6I5uxwlAGLThFwp2IiXlrQVEJ1jUfzWt8xK074Lv-TrGIGR7pLEy4bL5CoRslvKopeLPUvekWnfU6UNtccLxtMVVMYtty6OR4p8DdgBQsHntncg7_MKyg1eiNjDnze1AGQ1kQuDdg7nAFFxpfzE-5N41FuTxGXyr975M3rgfVuAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=lmCPk0MJE_lB0T9-p4mr-aql2jepYyhQuI5VHNka68Pqj0M762d79OCsq7C5zbTsyNhQbyVwHB35o4h19FYmrvpqi3aGeTK3PmxhN2p1DSWMnzIPMk6ZZoWD5qOxBwESyOEGMgbp0ioBa_uy7gfsVYGHG5pYRW3qUvAp-1vWxe66HOUhvrGWpx_9wns5A8X2io27lAD6LEMsmcSgoXmfSsKStUOLw8eKJGxABgzeBmxctGqJtPhuY1SO_78kk3XFDa3jXlbPWLn7l6QHyOc-DR_u627qMSv8YYmG3pZTYU9IuVggL2_0Rwtth780r7W4KcWklbeV62Fr52il5BYc0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=lmCPk0MJE_lB0T9-p4mr-aql2jepYyhQuI5VHNka68Pqj0M762d79OCsq7C5zbTsyNhQbyVwHB35o4h19FYmrvpqi3aGeTK3PmxhN2p1DSWMnzIPMk6ZZoWD5qOxBwESyOEGMgbp0ioBa_uy7gfsVYGHG5pYRW3qUvAp-1vWxe66HOUhvrGWpx_9wns5A8X2io27lAD6LEMsmcSgoXmfSsKStUOLw8eKJGxABgzeBmxctGqJtPhuY1SO_78kk3XFDa3jXlbPWLn7l6QHyOc-DR_u627qMSv8YYmG3pZTYU9IuVggL2_0Rwtth780r7W4KcWklbeV62Fr52il5BYc0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=pPGXsbAmZgIBQUOb0YzFmJ9phwkxRCuznbKT1hhk9MBbXcqBhjT9Ban9tQGOM5ZORJEY1A_D40kQQ5eHiRmH1v8lTBz8uK4Xb7mlCwTxOGzd5quK0ziRyIwUR3PPvcjvLHJZlWnI78h8EAlqDsMtEPYGJ7kXDsA1wnkFAo5znShStZbYTYW_fhPLgQaASctC8ly_dZFppPrpqPQE082M0bUItpnEKcKVadSeyDTlSbI56_FbyVdXuM3O5Cssu1Yh0Buhk2sE1HNpPGau3j4TIllJHaUTUH70hTxesWS7AAuhfKuF6Exffu79RoXuJO2_jS2U726VbLZrxWTBUQm2iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=pPGXsbAmZgIBQUOb0YzFmJ9phwkxRCuznbKT1hhk9MBbXcqBhjT9Ban9tQGOM5ZORJEY1A_D40kQQ5eHiRmH1v8lTBz8uK4Xb7mlCwTxOGzd5quK0ziRyIwUR3PPvcjvLHJZlWnI78h8EAlqDsMtEPYGJ7kXDsA1wnkFAo5znShStZbYTYW_fhPLgQaASctC8ly_dZFppPrpqPQE082M0bUItpnEKcKVadSeyDTlSbI56_FbyVdXuM3O5Cssu1Yh0Buhk2sE1HNpPGau3j4TIllJHaUTUH70hTxesWS7AAuhfKuF6Exffu79RoXuJO2_jS2U726VbLZrxWTBUQm2iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=pZt9KCejVs6zQDTTlkkXMoP4xCjyxVmy5rjhkEz7S0EH3AhFOLMz2fiSP4r7yIZqImE-a03ZUWEy7dEOypH80OlrFVxziOJu-EqsiuLqjSzXkJge13TqNKzgkcPg8IwfLkqV-7HNFcYwl4gyv858Z7gPwxX2o74VmHmzInFWQFXZFpNfYHO4wzb-UttAM0cr6W0DczHYaJp02EUadL7RDcDNOnQwya0CXYyJjVasKHx_mdmhkfHS0CX-lVDW8vct1F5jzNhGw8tMwNFkVNZVeOd0uYTdmda1oUdgq_iJnm3EJZPC3UqnGMM5ppXV2EXsEOYAumfx_PkOhAEImElaXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=pZt9KCejVs6zQDTTlkkXMoP4xCjyxVmy5rjhkEz7S0EH3AhFOLMz2fiSP4r7yIZqImE-a03ZUWEy7dEOypH80OlrFVxziOJu-EqsiuLqjSzXkJge13TqNKzgkcPg8IwfLkqV-7HNFcYwl4gyv858Z7gPwxX2o74VmHmzInFWQFXZFpNfYHO4wzb-UttAM0cr6W0DczHYaJp02EUadL7RDcDNOnQwya0CXYyJjVasKHx_mdmhkfHS0CX-lVDW8vct1F5jzNhGw8tMwNFkVNZVeOd0uYTdmda1oUdgq_iJnm3EJZPC3UqnGMM5ppXV2EXsEOYAumfx_PkOhAEImElaXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=UV7fHuPwWRqTEkvtzF1C0Fj5NljzrUKbSp8PGjhQRbfWIni4EaPIHZjRo2ByLSKsZ2SWOKGwO1Zy9aoClMrjvr8y0TNP2iXvndUoq-r15fKZQhABAsNAununC6jgiDuJjvPPXrZK2NeBwGtj54toP5j9mwEfLxscK2JrFDbPvNOthx840WoDUm9Z7bIER0XpwNjxOsIPQ7tJyRDdqaPa90F4Sy5UrAgLA3yRt_P4Ku8hdGTH31e-PrqKr-4_0DnPQj0P6gngu4U1mwgAdTLL3EJWZkNKLB0pjg5qrKjjeQUawC8_05McPilOO-Qmjw7Zd4YF6CF-jMamhYVWUELWyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=UV7fHuPwWRqTEkvtzF1C0Fj5NljzrUKbSp8PGjhQRbfWIni4EaPIHZjRo2ByLSKsZ2SWOKGwO1Zy9aoClMrjvr8y0TNP2iXvndUoq-r15fKZQhABAsNAununC6jgiDuJjvPPXrZK2NeBwGtj54toP5j9mwEfLxscK2JrFDbPvNOthx840WoDUm9Z7bIER0XpwNjxOsIPQ7tJyRDdqaPa90F4Sy5UrAgLA3yRt_P4Ku8hdGTH31e-PrqKr-4_0DnPQj0P6gngu4U1mwgAdTLL3EJWZkNKLB0pjg5qrKjjeQUawC8_05McPilOO-Qmjw7Zd4YF6CF-jMamhYVWUELWyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IHwVbesjc_qxsUDjRgyx-F9pKM6O9Pe_0NhiL8xsZWCyQ96eoLMn1dRltL38cCQXIc6He10IHtGegEcMThcZfZ0Zi0aHPwAjLGfpvCI1qL6zoVpAuIO2QOLziGK_JWSgsopnSh6wsDeaJqCUvz22bI3vFNYynqJRvBo_wSO5hqQxp0xmyxByEI9Ilj6AWpp4mjbbZlXdwk3MMJsho2eu63ynWnWFchYKWDVP8eG37Xgd-b4cvapae1TGGna7xc4dve6HjysY4OPHCTfweFTvNGLZXxJoGILlGuevls4aKJXqKnw77xryGluJdpyvd_OdW_QCc3MNHcz6u8wX3e2i_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IHwVbesjc_qxsUDjRgyx-F9pKM6O9Pe_0NhiL8xsZWCyQ96eoLMn1dRltL38cCQXIc6He10IHtGegEcMThcZfZ0Zi0aHPwAjLGfpvCI1qL6zoVpAuIO2QOLziGK_JWSgsopnSh6wsDeaJqCUvz22bI3vFNYynqJRvBo_wSO5hqQxp0xmyxByEI9Ilj6AWpp4mjbbZlXdwk3MMJsho2eu63ynWnWFchYKWDVP8eG37Xgd-b4cvapae1TGGna7xc4dve6HjysY4OPHCTfweFTvNGLZXxJoGILlGuevls4aKJXqKnw77xryGluJdpyvd_OdW_QCc3MNHcz6u8wX3e2i_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=ktiT2ehHA0i2Gb0OxgNx5gU0dzskNfHTcVhE2Da7NmM3bAhgMvQSltxvPzZY6uy4FbEEPxi4K15j30z6DtUAcgYnD0Ee4Pn4ch3CyrEXhybvIO65wuk51QWvHYwgmsL8Bopwx3nbpViohwf0qySh_1voRoUlnMnlZAmnKgWKdrDYPWWepRIW43ureexrdverqwukPiK8W_rL3toQK5y5205wugSDknU0H7a5PazuyQppJYSewy-2hzPxdCtY6Po784Km-B_siU8Txy1m6rhRfbEMtbYidf8UZmqjAifgrQ6iAPX6LMumy2Z8rXKD-50SXA6yygIoY3_LUFrgj4O5Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=ktiT2ehHA0i2Gb0OxgNx5gU0dzskNfHTcVhE2Da7NmM3bAhgMvQSltxvPzZY6uy4FbEEPxi4K15j30z6DtUAcgYnD0Ee4Pn4ch3CyrEXhybvIO65wuk51QWvHYwgmsL8Bopwx3nbpViohwf0qySh_1voRoUlnMnlZAmnKgWKdrDYPWWepRIW43ureexrdverqwukPiK8W_rL3toQK5y5205wugSDknU0H7a5PazuyQppJYSewy-2hzPxdCtY6Po784Km-B_siU8Txy1m6rhRfbEMtbYidf8UZmqjAifgrQ6iAPX6LMumy2Z8rXKD-50SXA6yygIoY3_LUFrgj4O5Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=rYWtBFMZmsd-tBvuNWxEoUKQEqb7FCsz8F61cQr3vYLusA9Z5BBJUXILvGXLO3Y1WZcAhFoErir5Hz0kPcXmt_XeX-YlgdaCdmRAIUdymy4jnCPZ9MDQcj3CCsOhGLUlD72dL6QaRLw0iuOX3IWaaDT_zI9Hp55_N634enNRobwcjVORyuD4erynUDWbIa_u2iCXvEKLdZIXNU5vcOECkSqG6TUQsqlenyeP3NmcqXa2A38qHTQ_IKU2pHtTrdDCMZJJmYlQoDsq6fw6gd2J554E8iBpI_phKBWHCrIc-_1m1wwtIo8TCgOwYGnQwFZv4qKi66RqtkoGaJKnER880w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=rYWtBFMZmsd-tBvuNWxEoUKQEqb7FCsz8F61cQr3vYLusA9Z5BBJUXILvGXLO3Y1WZcAhFoErir5Hz0kPcXmt_XeX-YlgdaCdmRAIUdymy4jnCPZ9MDQcj3CCsOhGLUlD72dL6QaRLw0iuOX3IWaaDT_zI9Hp55_N634enNRobwcjVORyuD4erynUDWbIa_u2iCXvEKLdZIXNU5vcOECkSqG6TUQsqlenyeP3NmcqXa2A38qHTQ_IKU2pHtTrdDCMZJJmYlQoDsq6fw6gd2J554E8iBpI_phKBWHCrIc-_1m1wwtIo8TCgOwYGnQwFZv4qKi66RqtkoGaJKnER880w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2u1rAmUJr-nP2nYOT56iFr5MPBW_wahTYAGkcIEgS50-btcjNanoVNXpYU0kH8p9VG2sX0JUUjibd72VSixWazTJOIHzvsYssumTnmNjmyC4SJ7iOhL6rhudoEeXli-1eLRI7Zyp5GT2ZQvewiEvzzFlzXUCXnJh9B0VUxkHnCvjgj1vgz3BbGtXNG7w3CntQ6u7__G2zRTyht4HGwCdFFYzNM72K-UAFiMvNTvD8AhZ6tOzQucWTLzzEusenEb6-syENEQ5KSW2EjM8KeVX-XYTOg1Y0yWPCmqmRW_SZwMpETdTTLakW6lQh0PWy-BkCiLnolj7S88PgI4oxL1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Zi8F8UeKD-_1fp2v6BUigw5DwPCgN60Gz2-ojiG0Z9YWH9JR1yPSAlF9O336nMXfpB46911c4CqUYqKYCAEf3svVAp7gFRFg6k-KjWjLOBx_hyFwGSP6p4H6VhUH1a-fsVTVXi_Zwx2KPcFx3rpg3qBIzhWixWLsaZI2nAya7jnjl7Th2FwhYyCkF4HcEuHYu0_b7-oZZ-S_IzmjssBpsLUQyFwrdMDFocTGuUjqovNkkDmXqUAp-JuQ6yFSFNkpEQ3abHml4Gm5ruwKX9GkXfqAfzpxCWjkPOYiMjtEoOVuS9YdxqjzdD3rfmrog_v8meJ8T6Vgnmj8m9VEo2qbag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Zi8F8UeKD-_1fp2v6BUigw5DwPCgN60Gz2-ojiG0Z9YWH9JR1yPSAlF9O336nMXfpB46911c4CqUYqKYCAEf3svVAp7gFRFg6k-KjWjLOBx_hyFwGSP6p4H6VhUH1a-fsVTVXi_Zwx2KPcFx3rpg3qBIzhWixWLsaZI2nAya7jnjl7Th2FwhYyCkF4HcEuHYu0_b7-oZZ-S_IzmjssBpsLUQyFwrdMDFocTGuUjqovNkkDmXqUAp-JuQ6yFSFNkpEQ3abHml4Gm5ruwKX9GkXfqAfzpxCWjkPOYiMjtEoOVuS9YdxqjzdD3rfmrog_v8meJ8T6Vgnmj8m9VEo2qbag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Dtr9pU2TDNXb8jg0RwQMX7aBPTi2AInukfoyqjeVLOPDsuNxsTIYb1oznO6o1LCrmpX0GZMErRXyCVUw0vRhfORcWxDfXa7lmcYU9AJdipeExS8NCc-fka7ecjPX2yYNJicLHonqEUmD4uoP30ftn1ijRyayms0NIBCJDS0PKas88hksHCQ-FK5PB4zQV7Vja7V0ZmDEjnC_I8FZCW1pOXWspAYlLS8TrqWafbsYTUL3n6Dw3YILoIrVkBUMekXY33qrgB70coQPIlLGKz4d9GenaABAhu-WcWNoLj8Is503bqWXIlBqzwWDTrRdqwhgS73PHFy7GRcGxr1QRAw7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Dtr9pU2TDNXb8jg0RwQMX7aBPTi2AInukfoyqjeVLOPDsuNxsTIYb1oznO6o1LCrmpX0GZMErRXyCVUw0vRhfORcWxDfXa7lmcYU9AJdipeExS8NCc-fka7ecjPX2yYNJicLHonqEUmD4uoP30ftn1ijRyayms0NIBCJDS0PKas88hksHCQ-FK5PB4zQV7Vja7V0ZmDEjnC_I8FZCW1pOXWspAYlLS8TrqWafbsYTUL3n6Dw3YILoIrVkBUMekXY33qrgB70coQPIlLGKz4d9GenaABAhu-WcWNoLj8Is503bqWXIlBqzwWDTrRdqwhgS73PHFy7GRcGxr1QRAw7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=izlLMgPM5USD9eVnJJDerIhcjf9QlTBfEWqRqX8x42oJ331sTXuyhJMcG3o4mb5oyj5PG2cIxOk6MhPl2gdOJ65goZdlV2Edd8RqvxmcOcXPK5BDrKmB1Xlsl2NJnSAVBpHPc32e0H_Z01E1Nce38T7y_ZN8mJ3BR3POgN3dYeYLdxSaF-crMtLR9yGVHmI08nqCEjd33CEGhltBgZbyhmWGM8_nyMVKy-_8lI0YoDq-2QeLdKCOdc_JAzRRy8BhGJJNpVDUAOPDliR7dxuD78S_RuwdWwPjHxkpjZCzaW304_rRpqYnQ6fVnI945xclZk1B0-UZrj30Ey937OuJdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=izlLMgPM5USD9eVnJJDerIhcjf9QlTBfEWqRqX8x42oJ331sTXuyhJMcG3o4mb5oyj5PG2cIxOk6MhPl2gdOJ65goZdlV2Edd8RqvxmcOcXPK5BDrKmB1Xlsl2NJnSAVBpHPc32e0H_Z01E1Nce38T7y_ZN8mJ3BR3POgN3dYeYLdxSaF-crMtLR9yGVHmI08nqCEjd33CEGhltBgZbyhmWGM8_nyMVKy-_8lI0YoDq-2QeLdKCOdc_JAzRRy8BhGJJNpVDUAOPDliR7dxuD78S_RuwdWwPjHxkpjZCzaW304_rRpqYnQ6fVnI945xclZk1B0-UZrj30Ey937OuJdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=vjnXN8cT-qIQweUm0sk8RGtiRUI-NyvWzHVoC_p7dFH6uuoFf2Acv8vNumQLP02MvwwI5KpNpjzS_deYaOD0kl38WUE9gGngaJDMkfaNwqquxitBKjY1_kMiQcYMhXEe8eZUIcRPCk-JGuclmpbZwVXITkj4hgscJ7gHo8NHxTrpwtldPc1ZQib5SkqH2xVMIvr8pfxxPgbCFhpsCS7vcsat68psiTYD08psUhvfKLavoe_tW4kbBlmcXgog7TtF9o2J4jZYntf1iH6Cmwqk2uZn7xxmEKDzsoFkYeZUnJ9Ou4ysm_ngVMTzDVMxzjZ3595LxQ0-zDh5gtZJnnGIkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=vjnXN8cT-qIQweUm0sk8RGtiRUI-NyvWzHVoC_p7dFH6uuoFf2Acv8vNumQLP02MvwwI5KpNpjzS_deYaOD0kl38WUE9gGngaJDMkfaNwqquxitBKjY1_kMiQcYMhXEe8eZUIcRPCk-JGuclmpbZwVXITkj4hgscJ7gHo8NHxTrpwtldPc1ZQib5SkqH2xVMIvr8pfxxPgbCFhpsCS7vcsat68psiTYD08psUhvfKLavoe_tW4kbBlmcXgog7TtF9o2J4jZYntf1iH6Cmwqk2uZn7xxmEKDzsoFkYeZUnJ9Ou4ysm_ngVMTzDVMxzjZ3595LxQ0-zDh5gtZJnnGIkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz192obdoOSl89-8lrscVntFg1O0EC8upOlMLEzsD95RVvsW1cewktriPCoP-aY5J9pfxNR7aQ2CY8tR-PvE66HE-0oFsONlqxEck_UNQYUOf3I8hGu1aBMNqVQK-I_EA0waObg601Nj5XCLwzCBE49eQcF1uW02hSouQG0Zo0EWcPOrKssCka-tFo9FT6H6TEu0El9oMHRKZ2gQ7bBkXB9rO-Mz-T9SnKHTTFdMFT0nynIDhOxK4zInyzNl5eH2mH4J2mTPZtk_2EbU_bpcstiTMC1irQBnhp6L0_E2ciXCWDIw_KXt3BGwOIdNHXUAV2JZHK3VVlRDI9fISWmYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YY-sPGLLtm1Jm2hK44FYr_sZPHNai54KBei9TDFg8w8OSopI_Xfj1Y7ee2gSKK108oeDZ11LuGH_i4urnJ-WVGRq7-o8tvidmmobQyajA8e0ahjTDrBfoap_33Tv9F2ov5H_DBszMOzc5j-OBHDRzZVa_nNLw16NAs-ss0hxB2vkMMNLkbvcVncsZ-gu_vsKPhwwnq9x7BaHAWUkeUNyoao9M3dy92FM46G7W0gCoxk9SY6eWxork4TEj1wuhz_K-uJIits2xbDY5g1R_Qlg6LybVJ0q3tGS07CX_AsnFonfXGEoQ239fQ3CUlmAQbWsPHPyfthCVBekx7gEwbLzWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YY-sPGLLtm1Jm2hK44FYr_sZPHNai54KBei9TDFg8w8OSopI_Xfj1Y7ee2gSKK108oeDZ11LuGH_i4urnJ-WVGRq7-o8tvidmmobQyajA8e0ahjTDrBfoap_33Tv9F2ov5H_DBszMOzc5j-OBHDRzZVa_nNLw16NAs-ss0hxB2vkMMNLkbvcVncsZ-gu_vsKPhwwnq9x7BaHAWUkeUNyoao9M3dy92FM46G7W0gCoxk9SY6eWxork4TEj1wuhz_K-uJIits2xbDY5g1R_Qlg6LybVJ0q3tGS07CX_AsnFonfXGEoQ239fQ3CUlmAQbWsPHPyfthCVBekx7gEwbLzWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Q-2esIqEGsR5CbDtXbpmYmYzNJzXSpCRDl3PNrDDQJcdqOSnlOPHCg73wF4QG3WooyzKFSBer7rIoRHHgrTksylegsEn0R7H-QFFx_0XxhUH-elANwThT5LtBsPiE7BLPpa-DADKw4i_bx4Xj7zxOoyiSgo-vUFGTJXCphkNpS_cBXwGn0dY88xnjzbpBT1O5IUOvIXD89YvvKX3q4bpruyg1mA6-p4RtGJFGjzlttu2QGNQcnWnMT0QpCmiuk6YukfJ5OBvWjUUG9dhboB0cWDcivS2FbvcIprgHgTGlX1nsU4bOK4BjvshGQecBgI84G2F9yc9xrGWVyVaWuUD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Q-2esIqEGsR5CbDtXbpmYmYzNJzXSpCRDl3PNrDDQJcdqOSnlOPHCg73wF4QG3WooyzKFSBer7rIoRHHgrTksylegsEn0R7H-QFFx_0XxhUH-elANwThT5LtBsPiE7BLPpa-DADKw4i_bx4Xj7zxOoyiSgo-vUFGTJXCphkNpS_cBXwGn0dY88xnjzbpBT1O5IUOvIXD89YvvKX3q4bpruyg1mA6-p4RtGJFGjzlttu2QGNQcnWnMT0QpCmiuk6YukfJ5OBvWjUUG9dhboB0cWDcivS2FbvcIprgHgTGlX1nsU4bOK4BjvshGQecBgI84G2F9yc9xrGWVyVaWuUD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTyzRYxcG9cen2nhSQzyRP0zXFpAd0Hw3DE0rVbb6IBy3R1oWdOuepJ2xBuHYQIIGtDmW3_-cepK-K7PQo91iKH-izYb1QxpmPQKwU6d-7PbgtDnTYcsp62rey090RxZxv1_NW3nMwp6p4e2eOqNNOh5KGmwaHBlG43MGSrCM_w8N_R1C_ttHOFSzAKNX0mw1SMnzQzurga4NkbtaoEG8UDI6_PLvPc0S6VlIbqXi4jG-I8hTOXYkIlt4qK11cfyNB7cMKLmVStj0JUlsYMjI4GvAP1npsmaG6caGSn6U3PbcNGMHFx5KkA-uVwe05Z9NC5NOPfHJyhurb07iRQVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WBYG4NbsTVSnNKys7-Y89b1nwC7Hafw4QCW0RbLwN5pGIoQ-NvWOjDoq5_wyuRPqje2H2BlnScIp7SAXHHPvR6k15eGjjn4LsofQBxc3DElQPwsXe7QjSjhb1cqnmmydzel8aJhcqy06NsryzoHxrc3MKu-qgQVV1H92QEJNDWkdu5SMq8_jfkHDMhUaP0W31frHuIRoGth4x9CsSWbl6-EhHOgGssQz7UZVpsziOFv0EsI-388HvNq-emFfulQ04gWXn0QgZlBrWp-RXAz6FtfkhHnFCHajR_yKGMzxxLitPZM946CRC7jIeNPFt0qKmNYuBSC5mFiJNPWi7gAvMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Ij1gDF8n-iMoEeUxaMPYqtLYLrTd1tAei0UEpHKV8voe4NRiZRRe9NcBmqeB2wHygg5SYUscuNlpjDF0SG7oOULvxsYOxVql2v1AYABNiWFpk00OakWAui9EprS9YgrCTWu_gZhIz6Bm0ZnMlY_8riVDMLMHUsisnzj3K-1CEIJ2uNF3rUAxSnXZ7Zz4H56Ve59plYT4uCJ-PLEoLMXe6iHLRua72A_2WjNnMe88vxPgvH-P9mJUCM-dEm0c4Nae9QIuWwK_-rpY7kwYpnwPulQOIJ8_RZvLmNZeFCbqgKXHVvnb4tCyEHaQCgeqS2Ku89TsizLeKEC6JFT_JuBBOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Ij1gDF8n-iMoEeUxaMPYqtLYLrTd1tAei0UEpHKV8voe4NRiZRRe9NcBmqeB2wHygg5SYUscuNlpjDF0SG7oOULvxsYOxVql2v1AYABNiWFpk00OakWAui9EprS9YgrCTWu_gZhIz6Bm0ZnMlY_8riVDMLMHUsisnzj3K-1CEIJ2uNF3rUAxSnXZ7Zz4H56Ve59plYT4uCJ-PLEoLMXe6iHLRua72A_2WjNnMe88vxPgvH-P9mJUCM-dEm0c4Nae9QIuWwK_-rpY7kwYpnwPulQOIJ8_RZvLmNZeFCbqgKXHVvnb4tCyEHaQCgeqS2Ku89TsizLeKEC6JFT_JuBBOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz07Di1SJHgnsVTXmima_53iyLeJoLZ7PFY_E0ndWw9cp7ACBaJVHn1LXMuFdq1qwslPQIR4LPqJmVy1Npex-5KeA9SN-3TA0orf18IcCXPxybMhmcKYa0B2bmvP3jv4j2dAcDtmlEOHv8sS5S7D3qN3YJDp33edd7XN-IJJk23I7rwoH2XbPsAJmdSJ2xQi4kJFQE5svyEUF8TwivDA9Tw3jGnxL-lJziywKgA0vJsX5a7YL7AOCPLakgY_S1UJOq6rtIpQf6PNLoTcQcRKvBIWbH-T0Z0MyJ856PuB3jatwWK-cfbj3k7WaZHWjx-VFaU0bLUOHRm8EmTt8kbV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIQLWbMUoENBlHDj6faK3W_gHM4G2-jlQXpYOuUaqFonIX5Yxa9Dx0pyfrq56s8kSfPL4iP6hHPwZyT9-eqbGd70X-xtMHNY9FUsjn1VtEAa8bQfjB_xXC0LqLnSsE8Tu17QCtb79BcyDpvj8lkygP9mK3yniKr3TMsjY4Qw9PH12LBHgqAtOA5ZU_rpcdEHo2W7jiKaDMZpJwB-ILzSX4L4uyI2mJ4-j2bQoaQCYMFA75n9h-dR6M8KcngmXsTTeXNgat9gjsjpFPPtA54pDxHJk36ewqREXTZw0uULgbABhr5oUiJulCYJZ-EQcpeRw2HoF9gFE_3-NXoqQWg9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giEAlBBuY7JpwYQs79adJyH5kG5dfimNi2osTtkPXtKzfGTN5Qif5ih7CIKmv5Sntv8p7c2DD13TSVWrRDrAzI-vN4_kJEdC_sg8JCZCkGC8g15oOY8Y04AhHk7H3HXKkTdGhok1lIoM09x_nov0PSqbL6sp0bAiTpFoQPsoZP1Wbk9SxasXFhdn6A5TzEWi80ZwP6-Qv1QzpVEyU0gsqQ3x-4P8Gq5wLROb3tao84mRGBOyg98BeNQT39DBQnV3EGuhDokg4U62KC0jGWAp-T4toC28rPBWaMT2V2Zyz5KifzdG68NWwMbLT8Wk6y6NQ4a6y0pE5P-HkkNu37GnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=snNfKrX083lWm5LwN_yTeNC-hmnhRw-hKgLNYKR6qqIhWYtUXdLWD66zFqatibEc_w5ER79O456yNGeVw7BZBGRM9Zd6brMEQK-_BYi0ZKcgXyHiO2nQaivdE4CsESQ3UjKmkcKjqlG-16oVmY_CDHilstUkwM20omwQXCGcucd90yqYUBA9mlFwioBozH254HhCWv3of57W5sF1YMnqJ2hT9jCUJjOJ8IWRY4puMgUtZuPQI_L1y9DsRO5OwfaocCDSHQ2oF9McZ8O-_CaPdNirc1600l0WZn4aAq3iRFtifKl6lvlrjFyGhHZ4qajwV6FtoAKAHoX2zsfQLPEpfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=snNfKrX083lWm5LwN_yTeNC-hmnhRw-hKgLNYKR6qqIhWYtUXdLWD66zFqatibEc_w5ER79O456yNGeVw7BZBGRM9Zd6brMEQK-_BYi0ZKcgXyHiO2nQaivdE4CsESQ3UjKmkcKjqlG-16oVmY_CDHilstUkwM20omwQXCGcucd90yqYUBA9mlFwioBozH254HhCWv3of57W5sF1YMnqJ2hT9jCUJjOJ8IWRY4puMgUtZuPQI_L1y9DsRO5OwfaocCDSHQ2oF9McZ8O-_CaPdNirc1600l0WZn4aAq3iRFtifKl6lvlrjFyGhHZ4qajwV6FtoAKAHoX2zsfQLPEpfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=qJJGeF7hEfkiUv9-ndK1JB3cfaQlEAIxyD9NSZQ3gtKu11JwK-sV_SMHpuCDVKcVl8iQmD5v--1HAiBvmrn9sUR_X3iOdRCwSKh_6ZCHKaZA1WSEAUmvHWflhokdCFKWk2h_khhsdzqX9tMhDlBwvJu57O09tZy2pMOMaCU77-DdaaAUyJrZb4d-Zm93tQhiWwTJ-TktAyf2ejIKqm00ySmO0C7tA-1cRsafT3RMcmMS147lkxyUFEN_s0ryJrWw6uix42EeIU5xn8RVUMHw0jaw0A5N-4MS2lZRpky2eXENruBV6aNSV4A7qn2k9uiyTDK4FFQZEFTEcR1iaJHyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=qJJGeF7hEfkiUv9-ndK1JB3cfaQlEAIxyD9NSZQ3gtKu11JwK-sV_SMHpuCDVKcVl8iQmD5v--1HAiBvmrn9sUR_X3iOdRCwSKh_6ZCHKaZA1WSEAUmvHWflhokdCFKWk2h_khhsdzqX9tMhDlBwvJu57O09tZy2pMOMaCU77-DdaaAUyJrZb4d-Zm93tQhiWwTJ-TktAyf2ejIKqm00ySmO0C7tA-1cRsafT3RMcmMS147lkxyUFEN_s0ryJrWw6uix42EeIU5xn8RVUMHw0jaw0A5N-4MS2lZRpky2eXENruBV6aNSV4A7qn2k9uiyTDK4FFQZEFTEcR1iaJHyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Igg1Hhp14Xwu4nHud3pbsgAfZO2ePrANGoGHMrSVFy_5xR5U8jG7OXD1kbULO-iTpGQVxjl1tgJmaFlhIDEeDzzwzoIfazNpXg37Wx07iE-sB4oivDwO5lXou2GzE2EflWt8jvl49pSGXG1-WUlNWdMoYvqVPEuidlPjuTkk22o3VbBC_eZ7GIa5KsXCmyfLVL1yJZ8CwGbl83pkACdkHBhat5GrUhc2-A0dLO9fl2zmaTP9Lku1lYjnvhhHcCjcZw_4o5ogThDrdxGYyceC8hYb-MolQcxql_dd-Sz_Prv05luE6g7lInZ-bIqRePp2hTEh1aOvpmR0iMTquRArxnGGfbVdM7I7uwCvAYw-T3VkhuXGtNWdinUukr0J2UflRt_Pb2eBv2m04d9HFtqOlAp_-yqpcad-ALnmnyR89toFeaY3AVIrO8G68Oa2Obi3EascU9JcvIo91zZ-LeHlxg--Fy1TQtFHnO93Zx5aJLutdZ0o-Eok6dWqmXTfp20NQl843XQ-moxT9Igpv0mCOCFnCv4X9mYvl1LzxF7fKgKVkV1LJkOcp3tDy8YbtHcgt6bjPLGL1hoi89xwrWJqVAIC6HaIyKC6Pe8VV3RvzZ1t9l7upPdBmDQ5YgrW1BJ6vdi5I0co0TLgNPI1hq5b8jc3ZW-MnwFASXnYcN9qd6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Igg1Hhp14Xwu4nHud3pbsgAfZO2ePrANGoGHMrSVFy_5xR5U8jG7OXD1kbULO-iTpGQVxjl1tgJmaFlhIDEeDzzwzoIfazNpXg37Wx07iE-sB4oivDwO5lXou2GzE2EflWt8jvl49pSGXG1-WUlNWdMoYvqVPEuidlPjuTkk22o3VbBC_eZ7GIa5KsXCmyfLVL1yJZ8CwGbl83pkACdkHBhat5GrUhc2-A0dLO9fl2zmaTP9Lku1lYjnvhhHcCjcZw_4o5ogThDrdxGYyceC8hYb-MolQcxql_dd-Sz_Prv05luE6g7lInZ-bIqRePp2hTEh1aOvpmR0iMTquRArxnGGfbVdM7I7uwCvAYw-T3VkhuXGtNWdinUukr0J2UflRt_Pb2eBv2m04d9HFtqOlAp_-yqpcad-ALnmnyR89toFeaY3AVIrO8G68Oa2Obi3EascU9JcvIo91zZ-LeHlxg--Fy1TQtFHnO93Zx5aJLutdZ0o-Eok6dWqmXTfp20NQl843XQ-moxT9Igpv0mCOCFnCv4X9mYvl1LzxF7fKgKVkV1LJkOcp3tDy8YbtHcgt6bjPLGL1hoi89xwrWJqVAIC6HaIyKC6Pe8VV3RvzZ1t9l7upPdBmDQ5YgrW1BJ6vdi5I0co0TLgNPI1hq5b8jc3ZW-MnwFASXnYcN9qd6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=SAOH1WneLNEdAaXhroqgLYO30TjIMlVdtqoguPox7eFzhyZNnExzIokRIl-dDIQn-m3ZONjyJl_Du2XhXtPi97RJDuneRXJ81-aJmwnEDwFjt8OKw16Z_GYElJP7tb450P2ZUVLXs-6z2C2p5GrN9E9sRpTUgPc3WDndumBZGLet4hnwky0gfuqz8r8RSBVXs0M9zB6fLxhIbGaew4pu2qkOV9Hlqas9QfS5aPOVNkVPhyWSGjDCdOeT_DAwfMt_Kg_hdXF-NXegvlUa5Rv08GwGadtfYy3OjtC0eoB_qEykAeURk6rlL8_bz_oBc8R7M-HJV8irlX8i4JBBnooM12FvuD5SYCHBylMCRDxirgqiS-0zJF9beF1glUbanuKnSwF87gxLvKc6fdsm7QyOpldIL-iyX7WmVYdNKfug9hjkfTvm_LpSRIHcFiV4dAyJU7hpgry95a61h2Iy0QMbDDRZvqj8bNCprAr0G7V7MiRDzZpCUckTIn2a2ZovPua8GXfwN9icMYigILzFc2pQqbrSiCFtTOhtHBwnyfz8UL0ZYqCGdpTf3CcJs48ufDP1qTg1AsCSQNWZpEQS6T-pAJU1jUTizr9y91M-CcsnuZMMc6uZjMiBPsf25CPumcl4ftguusyLn-oNwmC1OD9mwUVd7DZNTZeENPsAGRMn2Nk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=SAOH1WneLNEdAaXhroqgLYO30TjIMlVdtqoguPox7eFzhyZNnExzIokRIl-dDIQn-m3ZONjyJl_Du2XhXtPi97RJDuneRXJ81-aJmwnEDwFjt8OKw16Z_GYElJP7tb450P2ZUVLXs-6z2C2p5GrN9E9sRpTUgPc3WDndumBZGLet4hnwky0gfuqz8r8RSBVXs0M9zB6fLxhIbGaew4pu2qkOV9Hlqas9QfS5aPOVNkVPhyWSGjDCdOeT_DAwfMt_Kg_hdXF-NXegvlUa5Rv08GwGadtfYy3OjtC0eoB_qEykAeURk6rlL8_bz_oBc8R7M-HJV8irlX8i4JBBnooM12FvuD5SYCHBylMCRDxirgqiS-0zJF9beF1glUbanuKnSwF87gxLvKc6fdsm7QyOpldIL-iyX7WmVYdNKfug9hjkfTvm_LpSRIHcFiV4dAyJU7hpgry95a61h2Iy0QMbDDRZvqj8bNCprAr0G7V7MiRDzZpCUckTIn2a2ZovPua8GXfwN9icMYigILzFc2pQqbrSiCFtTOhtHBwnyfz8UL0ZYqCGdpTf3CcJs48ufDP1qTg1AsCSQNWZpEQS6T-pAJU1jUTizr9y91M-CcsnuZMMc6uZjMiBPsf25CPumcl4ftguusyLn-oNwmC1OD9mwUVd7DZNTZeENPsAGRMn2Nk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=VDtKuFqDJBxWmDoggggmIZcIOcczrEcPzkEURM9lumfU0j1qV6MXUW8NN7rKHUwhpNi8O9dxwbfV0bmcvwOTuj6okcRWI2VEVEJ-nsqGWtPGisGpsliIrwyNxU6B6lVgptVCaC795evh5u66zcAaoFsImbFlV7cUwsDpD9YNIkHTf7fDNrIED7yw-m9RWBTIPDNiOMjdXMOPi6QE5I3TL3JPyx00ou474q8nxEs2xJ5pkPh4hWGHMkWsdgku3lSxmLg80uUe6PZflMJG8xapFg2zbQbtu89AV6Z9N3u9acKOnQmFbapSCZnNqzo0tTWbOJ0KgvZpem3UCN3-hnZxeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=VDtKuFqDJBxWmDoggggmIZcIOcczrEcPzkEURM9lumfU0j1qV6MXUW8NN7rKHUwhpNi8O9dxwbfV0bmcvwOTuj6okcRWI2VEVEJ-nsqGWtPGisGpsliIrwyNxU6B6lVgptVCaC795evh5u66zcAaoFsImbFlV7cUwsDpD9YNIkHTf7fDNrIED7yw-m9RWBTIPDNiOMjdXMOPi6QE5I3TL3JPyx00ou474q8nxEs2xJ5pkPh4hWGHMkWsdgku3lSxmLg80uUe6PZflMJG8xapFg2zbQbtu89AV6Z9N3u9acKOnQmFbapSCZnNqzo0tTWbOJ0KgvZpem3UCN3-hnZxeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3sUIP34DL7gped1Fa3DAAnsPCCPqlFDi--xay7nxoeK-onnzG9uBTSUTYcb-T2bhepOfWrAc2FJOiHODnVT0DzEpDkO1HbUKEBvPT_fU6cC6orazD0jZdufdZeJMoe2S_SOfUE7E-o_hgN26aPagZNO0I1IZvwvhPqI7pCzLh929hwtxBi5PTdKJhq5YqdUEL8tOKchlTY9eXBsSrDNdacncVGIFPpbDHLK1JJK4jvK82AYZDGAca5s1U7WcDW4n1FPHxzdndbOqU-c74wHWcNFNb5yKQhleaFxKLrrX0IY45Tpp1Y8Kv9LAPy3FuPipUFn_1AfS57-mtgV45brBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Ofpks6K-KzycNJu-cNP2MyEJiUyoNBicIHDCJ2yseLAAsgtKUaeStz5RVdGVNFH-4YhPcbxyVUPK5IR6HPy9SHuIcIycdcRy5UjuEeRb3fdsF7O3voLvwQfnsn_1b9gjndZiZSSJnZBpuOItDlfXrOiuknuCqCNpliGP7qRPmfOPr2GbNmGeDGNAag1_JThVFoUvGBeBFwILG5bPMEey_l9TkPJXhFomTHbElsQVBEcmzTLOuFWG-x4SZ11QkaXz1zale-436a3-w36Ytu_Z-uJ8HNQw9zH0e7lt-m_SnHseV2HxTIUiNdZat3cIYcvtZQQbJ1HwRlsBh52RNflo3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Ofpks6K-KzycNJu-cNP2MyEJiUyoNBicIHDCJ2yseLAAsgtKUaeStz5RVdGVNFH-4YhPcbxyVUPK5IR6HPy9SHuIcIycdcRy5UjuEeRb3fdsF7O3voLvwQfnsn_1b9gjndZiZSSJnZBpuOItDlfXrOiuknuCqCNpliGP7qRPmfOPr2GbNmGeDGNAag1_JThVFoUvGBeBFwILG5bPMEey_l9TkPJXhFomTHbElsQVBEcmzTLOuFWG-x4SZ11QkaXz1zale-436a3-w36Ytu_Z-uJ8HNQw9zH0e7lt-m_SnHseV2HxTIUiNdZat3cIYcvtZQQbJ1HwRlsBh52RNflo3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Jjockj4K4UYJUEK18KXRIW5twOoD7TGsBiAdNObCjEbP1_kt_js3yul1_KTebs7drqTbIswwL3Qu6dhQAwA4M8nWX0zSZk_63iJG4yKfHJtuzH2MLYWjN_apNtk8omoPGJPSgK0RnwTBGxKdGcRcZHbXH7zyUqhOOIAVfHuAO3K3B9AaeKTqxUoBBajpRp46wa0-qx99MCKe6eVA8o7zg0B1iGcm5aKDF0MgkTfFLgPe36s4IwiyRGgVMH40Ey4HNAAQA5tcM_2mHoGOCWdclr4jzYlHPaYTw9MjudPfhLces5_ZCDYP6D-QLnVppFJehF2kZDzG7ca25W_bXbUTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Jjockj4K4UYJUEK18KXRIW5twOoD7TGsBiAdNObCjEbP1_kt_js3yul1_KTebs7drqTbIswwL3Qu6dhQAwA4M8nWX0zSZk_63iJG4yKfHJtuzH2MLYWjN_apNtk8omoPGJPSgK0RnwTBGxKdGcRcZHbXH7zyUqhOOIAVfHuAO3K3B9AaeKTqxUoBBajpRp46wa0-qx99MCKe6eVA8o7zg0B1iGcm5aKDF0MgkTfFLgPe36s4IwiyRGgVMH40Ey4HNAAQA5tcM_2mHoGOCWdclr4jzYlHPaYTw9MjudPfhLces5_ZCDYP6D-QLnVppFJehF2kZDzG7ca25W_bXbUTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJIoA1vPSAOB6AjlCueH3t84vc5haI3j85QCalPOezT9xZcH_kdPOGFvRw2sQQvw_G6l3oRuup7WnTaYinfea6j7DeiM-W2FdHaI7gNJVZKY-cl9ggM-AnGa2QE2of-bqwcAFOsiXUxi_D83dnKRhiLo3IDteLdgTvlra4OcEzpIbBrAyGmZDOPFc7ANh81pxBYOLFRoHTQxem2ZTABTQOkQ24B63RcNJN6Uebr3pfavOhmmhmFRDfcRTrrf7Ew-EKuMu5oQrG3rdpDPVDc6guDE6yhSdstppCcVu67E5dl7G3dBv4JxCcO-y7777LZw6lk5daNHKRRMIWQ6TAr2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXjg6M6SGhnoAXI-TDJBz1plhGZt6NwvH6UxvkK1VdBhPnPKGDHB-cGzqa_2u9zWPIvEiq_VPry_c5t_dRXH3WNmXqymatUHuTXXKcAswLL3QVpgsdHPJik9lmpF_VdVEX0UBBTyQSmDNH81-bDhFeZMuyL6d3N4q8nnqmHljVBK0dj9ASp_bXkMt_y0hg5-MpgxsOjR18oGHevpPYf-NFO_3F_OqrQRZ2yjMdIzHWTiVQ7G_kC4Hhcbghny1FyyllDew_8VOUBkBFFhF1zUOoQc-AQUlZ5AeeE-VvsinkrZa2gHHzBK3kcVZa1lDqs7jAwVAKXZwK_cLjebKvIWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po5fhCBnRAkDwtGm3wpn4NgD-9wk3-R_UFc4QKo99r43ql_SG8eDu0gJIu_5Nhu5jd3wAP0LtHq2tnUemnhgss5e3MnvAZkvl-gz0Wd2Yn4DXKA8be68drocagXmsWOjShu3Q1l85ZuyRFf06GzCLNU3TzkRAmFyZdN2bI8aNNmT_RtOSat8yFEJV2iJIuAZrP5BgrD4fkN6bL3appvCEDFLbl7dBW0QnpCPwj-BkTlxFzsBuIJwNW8dtqLSDNliKT7POo-VPhbRwoS9LMXkY6HeVH322hinQCX0JHc9eiBv64Q1D49FhEWT55jVNXdo85qFKMhbBBAlr4B4OpUzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkg2WGv_UUGkb5KT5iSKgG4qkfUT0ZdOYd1t-BshrnFefXpHaQR9j7fmnkOh5KL7F4mtEzitfzCc15nNNpcPEcgGxJMqBcMMBMByQBmvECZRNjew1CczDM2-1BqfGBYg7NXKdLZne9F_Jiaop-2QIdHJyVFjAbFytE6FLdRB-1hNo-VcEmceh0AQqLnjn0k23ONYS-bu0inK9-7ReyBH71GwGhFnmFzJHoHjoZ-LOJfZ8csYEHUp4NAMUH1wRfIi40XcVbd0JzZK7IBu127UVKRRHBvoHSbPNS8T39RzABHdjhMlzI0niTnZ-CYPtPE5-BfYA7icwHgPdfq5q8p3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIL7Ip71BS9jKgQ4ab2uOTWgqTXPNK6lHr42ampmbYnVHaBENpeZ-97Wdd72fxrs2XOAESxf0p-GK9FxZfa8UFCIfBtQO4ZnhR91cZcKahrL53KLcFbawZq7KDKi10QOMBVpJIezKYL6Rc_K_ODZXtNHZ1R-xIZgi9xJm0gnwIuPnsjQMJcI7iaXpcHGG1VzpPHG7bT93RMP3oo0MWr8PDuN0sOtBj2SYOcDrvNx_J9rpaMqdAOgSkgQ0iSmMdFkIdN0Lf6OOtkFLtgBqGY0-aevkDuxWLji_mmJPK0rHHexM5XynMp3vmIiwfnBjReUAyK8G8VnzS5a1MHkFRcyHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IczEYnF5v8rheXIljrhl-NhMuX-4yQviIiO7x2wvT5876K1Y7MO7ZZwJhtrT38fm1r-WVO12pFB-K6SsLMQq2oKNDtYhfLY82PGrinVK4EbbnPTlKze4KQq-325oW6CmYmXpT5dVhpJxio_Am6ctFv6_9nBIVAoBTUrRmf921QX3_6Q0OXAoQYvdvT0_xFEE08Kimgblqyr-dXF4da4CEwt5e-_Ao2yODb4LjZ6BTHw76LVspFDV50Rhe6chldkaDF5Sfy5SjNBuM0p6tAKOUFLTLXccby_DNJDdNyLvomlrEmcXD_L-wjOyn3SwN8zEl-66Qcphm7QAAX7is51j5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S54dNL9fGySHZ05yeJdcSZfoZ0VkiapMMG_kGKaPc91QxU0cbjwzFGDERlRQLJwGDjUvUgi9QncoO7ZgCY5Ul6z8aLhL3FNqqd06u6vzEBLicPsWSeKF_dVjvBa-wmEXlT6eKFgmph6zELyd4D_gnmCR5E6niWOH0oNOyUOHRfDn0bzULFyH4QVFHZe-xDrjlYBp2wKyV43zvpSB8EPV5i0-cHVlwFOKqJLaixhX7xX98AfwtxxN2sw7pMWjs_Izk_G_0E41yprVjdJPXEMyTqmsVylRc71lRVLZN6rGMYD_8Lo2dxV6RmxfeHDcQgkzmFkTXUzOSVoW5mPT_Zbt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUoH5a0Tw4uvWxBWPOQl6tBR5kpoYknvTvnl4Hi0_SPWxvjG7qwF7zG9wPeWACBPr2iOx1N3_kiQTwiOFhooeaXVLbrK2yOuDFuRxtlNKl6d_2Q5XsRCg1os3xBsacZXRGcGLw4eEZ1a7DqpbAqT-SMaam0i77isSICHDW9TVhtek79qg9Y5AruI3BBj04PH5SrXgqaMGgJ_fMNCVsXJmkwN1cZ2D8ePpCVIrswEGBWucRITqcSQpF6g6UXv7kzQLU30u3iIIyDDDm2Zk9p_T6Dy9cs7OVof3g5hIiK6I17nYPOGtkWUOkSY04QEeWpd0PrMRFjU_iIlxdiWqnBmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntFTwjGW2ZDF_-5TNWx5VAJ1YJHwD5EPURo9ovxpJR0ybZCjUhPdzFSMQK06jZRLck2OouABh7fO_1L3YGX_a_AaNAyECUR3KyDfLP-P7-1b-9rx9m97Hvg-pc6us9RavrZ6S6sqaFGkk6LSEVJRhoKLnnDOGLQuExrVqYhpe7TtQT4fPUxuxmT688puH9o_eyiwpvdfJTd8NRnjj_nMbjxzZBRYHs_5vPpbIRTOf4ME4wYNKcJ6uUZjMvRGCy5FbRv6GdjX2amr-M8QXnWvWqa-mVaMSXqzLLHrZbak2hYWCgBzR9JN6LSZWlOh46dDcd1rBUudsoX2D-rcfSgsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4gDN6h1G9CUst1iiVd9hdkAdmNsfxKloMx5_f2RSs-NLsu899v7uad_eDddzA4fWgWs58ckYK-K-p6zeRj7YteFA5z1HTNEAjlzE5BlQa_aBTwmiUiqRuQsGzT3NElbS-gww925_6SAvTu9_z2bGhEz0KBddVImV_RkaPcUOfr2n1yMJIgP_ZC2wU4-Y9uXuVan8k6prbF4nrI-2MW2IFgJAEiBFUDVfoX4wPIg-LonLPd683LXTgAmsVqEHC4FWwHij8cPEreLTM83YuDq87zr256SNQo-2CpvLK_zznuhz72w9p9qX3XdIr36aNY9V1gMY3oe-SQ8l5RFTeK-jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=H8RqtaEXOT5j-OnA0rAqPszxxeFl-D2yIIEtbJRw2xhVZhjP4y1ntmolhLZqPTMqgH1q3y8W9zScVOtdEDM38nNAYXqaPFtW0jIVDSowpq2raPH-31NBdJJ-8ZwP0xiF8MU1gi3LeSlTxMoLRiuTWiJcYhWd3y1E9iQO97DaVtZWopeT8DmxpTLE8o6i6esc4AbYvRB4PS8BA7KvMDRwqXedZaN9h3U7ISyVtmHqiAvsnTHItvUJjEwzgUg-ZKYd9IWT9XmALZdU1sJA-9Q7YyzBUDn2xC3bfbVQ2psZaHIOdShQrQ3NXzU204OxqBshkeeojDQdjWyKAMqpr13Nqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=H8RqtaEXOT5j-OnA0rAqPszxxeFl-D2yIIEtbJRw2xhVZhjP4y1ntmolhLZqPTMqgH1q3y8W9zScVOtdEDM38nNAYXqaPFtW0jIVDSowpq2raPH-31NBdJJ-8ZwP0xiF8MU1gi3LeSlTxMoLRiuTWiJcYhWd3y1E9iQO97DaVtZWopeT8DmxpTLE8o6i6esc4AbYvRB4PS8BA7KvMDRwqXedZaN9h3U7ISyVtmHqiAvsnTHItvUJjEwzgUg-ZKYd9IWT9XmALZdU1sJA-9Q7YyzBUDn2xC3bfbVQ2psZaHIOdShQrQ3NXzU204OxqBshkeeojDQdjWyKAMqpr13Nqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
