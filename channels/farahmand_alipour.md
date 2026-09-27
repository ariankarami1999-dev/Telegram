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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 00:08:05</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugMyO6z0lFTERuz4j0r0smhdQ6Nqz1aSLVsO6wOfL8WSRkgvmH3L7QRNHgjOaSSrVnIl-4sYqyWzu-HnbM5xKKP8p2SkvKQntaX_uJfAZ_lQirF4vnBeH7ztcvQihjrq6qGWXi3V1hrZudH4jZKGls7E2X6z6oqXCy9ObMdq1fLC746_OQb2Wf1QN_UCgY9c6rX833w8qWIkaCDaRRVtbAQTsT6yR2MgmBfmgaOQ48r9rPq1kzlDga85XJeh6dYzJHrNTe_uWfo026n9SqbVSoI3iIqUu_sKjsyzDjjoBtkrBITdHHOoZv6oUhehdJoApHVTtGYraYAW3qAxkrB6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=U6ZycOvFuYlPi9N3KWcEOv5k2r7HN9LG27e_ynm1zdbaa8rLwHYHj1qObwC1Z51Mo-vB6QS0zZOMy09XwIQnkw5kPVPFqfSjLOC_22FBF6I2ChFCgfFQnSkvvB11eMr5xEysxReVDtZvmt8MY-kjRIjQi7O-ALFcEnAo751A1W0yXUSvX0etaM6cBRa6W_HEOYEy1_KMLSYYgOOVr-yjxVlEj8_z8UQZAXhy_8toflFTS2O9ilXGX29yxjqtOVpfW2Sw2w8tmD5IC-debB8iDvnMywH704HamO2ozoVSg6QgPi-rdLOxqHHRBfQIRuMa--p2CtS9Oif-iUqANGgBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=U6ZycOvFuYlPi9N3KWcEOv5k2r7HN9LG27e_ynm1zdbaa8rLwHYHj1qObwC1Z51Mo-vB6QS0zZOMy09XwIQnkw5kPVPFqfSjLOC_22FBF6I2ChFCgfFQnSkvvB11eMr5xEysxReVDtZvmt8MY-kjRIjQi7O-ALFcEnAo751A1W0yXUSvX0etaM6cBRa6W_HEOYEy1_KMLSYYgOOVr-yjxVlEj8_z8UQZAXhy_8toflFTS2O9ilXGX29yxjqtOVpfW2Sw2w8tmD5IC-debB8iDvnMywH704HamO2ozoVSg6QgPi-rdLOxqHHRBfQIRuMa--p2CtS9Oif-iUqANGgBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMkz5sX9PTeEjCiNSA9jacT4khR_vwGc8ITb05O1NmZh7rhkjkJHvoNoQryB6BrhMxengYInqgRdd6XFKuN3PogMiLgwKplKWfOZqxQ1M99jWwWHVAk5vJ4221314fnfK8rUOkUg-X5oFtQvLP5uEtV5wgiKp6CkTeCfcbDgiXqwiByVjiS9RORqam2zua0MFQf-F3COKUyGNBN_x8ocr44B-Ln82InY1EmxRwrOM72am1Ef_x0v--j0XYfKg76Ljkb0X3FU73SSkiWRRcN9cTh2JxbcJw99Kspd0LEY4scLajweA6VgAPnV34ThUryrsMZ3kTR45WlZVxRUldKDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1i8nL2018cOSIgcnX6Kq35ow18aHD2JE-6y1OEmJG1JIxqYIWNhu-I_lTo23eQD7ous07OyYNxdbYqAKRWw0ilubNYN9tbU_Xjj9PfFMuSgQNdNHrArPD26b6yD_UpGn2o6zDTY8cbA-rgA1rOQs754QIDu6VvvTBPI0t7-BnbegYSyIwS5Uc3-BQwF0QAr3A1js0ZZoXVpqfd1hCRd3z67qsNajpPATRVj6BnAIUO8ImlSLd_GQybuTxel3bYPFDsgtzNfcYsaaas3LFA8EreZ26mmC3gjTQwIYzLe74_F7qua_bECvL9c1qh_kwutJBferEDzdfKR_fhwK19Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb64PhowCIuvmhDVUkgpJq7v85KlZU66c1nSRk59VKf9iWSKhwlQe9iTl77b25deFa-8DDblAvJJ8jzNlrmYkAgOqyzU1GwbjzeHCZRRQK0o6lrLcp_kn6wdPgu0pIrIRY1jF9i1N0VSuSOD9f2hlS1B5UZ5gObkgiyzyDjq08_sBGqfH9kFNLwEnm832mS43iwiOOYSvD3nNnDDmsc5WShnBPNAhRSnjoGjWWHiMrC-ZlSw-M-GYDyDYTyMPxyQEGyzbQHmfnJ4lWm-YCzOgJJP7R8kaGaZfFJCLSRn33SWYSoGPgycVIkw8RKxFuCe2C3t-AuchO5aYL-jrKjNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOiWX3LizRZsJLS1nKiqK-wq7UAaGVxGexcz1IVt3EUkWWW3Ajhj9BnuwAgXpxTEcYf0ptWSWoYQEDaZgMHYDibQlymuosLE1G9OklXAsLniSXpChG1DrkTHRVJWu55LCgDevrKhZ_qJy5S9UCXTzdgld4f-Z-zm1qfx02gRZHfKQlmnLSzZkX4iJDUqn7ifofK0EKPfqC36xdA_QV8KpHQyKb5OpCCWYh3e7VL7N_114NC7wM5PxyVV0CgLQi3OjYWFPNlTNg3Iwr9dn31oj6KnQCYywpRF6U6Bb-Ma3TW8jYCXkKb0biLAdMarTEPft-bxws0MN4hqWZeHP9Uj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=Yg6DubmbSfh8NY6PEodqN6UBnqyyDxV_h-xj4b2Yk7OGxGq9aCAJNjdjENoq6d57chnzsw_cp4JIPvJP4yGJUsU7Q_ByNQmPpwuJQKHAUHyJGlnWSRiThmHrSqlLQPcn2etoglVxAcJfvWDUa-nR9yv6rIx0dgMpQj1krmaqR52NeUqYoVGTyQW-tBGmkAQ5_TlaJL6sprlgAi0R4wo6YriuTvkqlV4lnwVV9I8o2iZfutJQ4ec4HqnC-X23novtE4O-xy1fK0Aau1PQLPBNmrCa4Z9YVguoUJtKm3FF4XzfxTM59nZrNseq6aUrTMWMqsrVd-JGaIN7-oK-1sRQCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=Yg6DubmbSfh8NY6PEodqN6UBnqyyDxV_h-xj4b2Yk7OGxGq9aCAJNjdjENoq6d57chnzsw_cp4JIPvJP4yGJUsU7Q_ByNQmPpwuJQKHAUHyJGlnWSRiThmHrSqlLQPcn2etoglVxAcJfvWDUa-nR9yv6rIx0dgMpQj1krmaqR52NeUqYoVGTyQW-tBGmkAQ5_TlaJL6sprlgAi0R4wo6YriuTvkqlV4lnwVV9I8o2iZfutJQ4ec4HqnC-X23novtE4O-xy1fK0Aau1PQLPBNmrCa4Z9YVguoUJtKm3FF4XzfxTM59nZrNseq6aUrTMWMqsrVd-JGaIN7-oK-1sRQCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lo9DY6ZBc8SMrl611AbVHt1hgtqJh9smzOu9ALPfmrMBR6Ci7TkYUEe17RGU_HSaKhRQbSI4evfH81tpr_0iD5p155EuRir3-igbZfc64zxD_tS0LbFNk5kgVO3_o_U-6_kC-Ne1zwuJoVTtFCUdmijF9J4ID9OkQk8kY-PiCxnNJWxXBSEKQ3dp1_LvxtLumWXXlveMXku1DLjsVzb9OSCPqgZc7NbC0pq1CpcCpw--yFy3qUX4DJLsIo2MrtxkFhRUJLLnzlULpAUvNNXthMX83TMLtNnt3iZm1nvsdgCXUvGAGjCQShgzFLdurj5RX71UL99kqSTs_rLZ7RHpgg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JIk2piI5jgD7wFoC6cC-CEj5yIF2JcNVW_zVC7Ff_yLlNRLx6hnY6w8t1r35Fxn6ShfnYNC5XKhxCMeoWdJIFKfZVJDfMRB6SKuLKw55itSN-4zUj5h4F2IaVsicrzv8y4VjcEULhdR4YaFIVZcAGxVZe-V-b0KAbvc0L4OdrWeq8fJTX2CwJ4oEtFtD4nxuH_07gnQOLVP807oR8DR83EmBmBOB1WLiGuv88Y8lfSiTzic7MGMU2P-3e3jZ8zg9DToWa6h943p-S5F-wGYcmIIQX-bs7py7L4ymhRKg0pq-kJ5MPUcZUYgcBWe09MaQVv6GFbhLqaK3QL0BnFDsFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JIk2piI5jgD7wFoC6cC-CEj5yIF2JcNVW_zVC7Ff_yLlNRLx6hnY6w8t1r35Fxn6ShfnYNC5XKhxCMeoWdJIFKfZVJDfMRB6SKuLKw55itSN-4zUj5h4F2IaVsicrzv8y4VjcEULhdR4YaFIVZcAGxVZe-V-b0KAbvc0L4OdrWeq8fJTX2CwJ4oEtFtD4nxuH_07gnQOLVP807oR8DR83EmBmBOB1WLiGuv88Y8lfSiTzic7MGMU2P-3e3jZ8zg9DToWa6h943p-S5F-wGYcmIIQX-bs7py7L4ymhRKg0pq-kJ5MPUcZUYgcBWe09MaQVv6GFbhLqaK3QL0BnFDsFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gPf8Movw04ov86iyF1SwtPSQrf5gosGpYNEcOlrFhCr-_Ei3li3YYLTKJJX6LTPRmyuFxeq6ZcR4lgcIfUcFhn3NRRRNE4q8tV3RKHDOIy55xFFnOuhyYt3da7jsftIUXAY6oQFhvjLeZUTtSMKTAXVw-RU03_gYaQUGJm5hx7EkmdNt3jbvjUJqtibmsHQ5iRbwuAPEpOz_sOek_Ww_ZXDrUqUzqkz9HR2rtkDJbqPrYcoyaKAQWXiEhvzooClZjA6WWna5gfnMR-LbsNYzTNRxFR0Fr9FFl0hvOBybmmvk5-wJ6ZaqhLedVJkv_h0eCtIygkPvY0tE2hLsH04q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gPf8Movw04ov86iyF1SwtPSQrf5gosGpYNEcOlrFhCr-_Ei3li3YYLTKJJX6LTPRmyuFxeq6ZcR4lgcIfUcFhn3NRRRNE4q8tV3RKHDOIy55xFFnOuhyYt3da7jsftIUXAY6oQFhvjLeZUTtSMKTAXVw-RU03_gYaQUGJm5hx7EkmdNt3jbvjUJqtibmsHQ5iRbwuAPEpOz_sOek_Ww_ZXDrUqUzqkz9HR2rtkDJbqPrYcoyaKAQWXiEhvzooClZjA6WWna5gfnMR-LbsNYzTNRxFR0Fr9FFl0hvOBybmmvk5-wJ6ZaqhLedVJkv_h0eCtIygkPvY0tE2hLsH04q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4gZ0Wb4O9p_JHBWFneXYDQQPv8xeVzxqRKtIRj7GgtXqAESvOZXrHAIYfKLEs0qUEct5fjOnHmocpIzs8bKu1IsFuZXJarkc1WZOg2owwF2KpnoXf1Ej_h69ur0qCtV5049ZzeuUqsqy52ZMd5e6mrXbdQQ66XZcz0xbGuCKBZR2Gs1m0N5cLycguI2HH-dKr4l1-7uNdKQP6oG3dUXayzibOsU47PKS5E1pH2fMQObWYaNI1_7dDl6_XVs7MKR8GIfPCfhgqyjOAwV0C4uV28gO1rHpKbswK3saLihd7tVqugh0nZLBJ-tIO6XZgHjd1aAYuQqcadv5jVcbNZMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=eBPJCv8p1I3osrCAD9ZA4xRnx8rNlAo5ma3yL0xSIJZRKCu8kUes_srz4zM_YOyHHYhVNJHu7xm8ApBB2CJYaZSigsLhmuZmDZ_Kyx4Wak-e1PEE7RU7drgsqJ14i_2Z3_vhgp_eGOQ7F5R8pqLPcdYCsiM-_0F9B-E_ywmSia2TB4EvHtER9a15lX_ufQTTfgxZ0YWaH5uRIYRkr3SqVMa2FKvWK2Dvi2fTDCLlTYjYHICT0yX36B3SVOO_HFKfYEViyuFyn855_LJDaVnwvmFZAJyx-T8Hn-lMpc78_YI04Adw6u4z9qreiCSBZHoX622G1C77TZkd8T9RgT6nZyc1lhgv3kWayPV9onQoucNeLoIVbX2YXBKqyl_b3Ld85ynbhrEd7C7zlk6oVBA4luKRl3Tc8n56kVPhzbyZD6bUZ5gdesWRFHvyaNSV80Zd9iR4lzMxDE3FTLGF66UeKPoSINVQf-bCf1oUixiCkvPmaT78NDlk8Bc_t9_NA3Rzv4OI4KYkDcEQOcfRuRNuhGpuerUU2cmVqRVYwBAdfTdnpxLy4Fe91CrL_PgfBoxRhNI-2CWvJPXYC1InSlOC-KHhZEdijmjt7iCCww13bUfrGPT3BTFc8RtBfEn2YAnIykywjC-gv9jk7-XyjtegumpJRCHOUOfxMGss7O7Vkeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=eBPJCv8p1I3osrCAD9ZA4xRnx8rNlAo5ma3yL0xSIJZRKCu8kUes_srz4zM_YOyHHYhVNJHu7xm8ApBB2CJYaZSigsLhmuZmDZ_Kyx4Wak-e1PEE7RU7drgsqJ14i_2Z3_vhgp_eGOQ7F5R8pqLPcdYCsiM-_0F9B-E_ywmSia2TB4EvHtER9a15lX_ufQTTfgxZ0YWaH5uRIYRkr3SqVMa2FKvWK2Dvi2fTDCLlTYjYHICT0yX36B3SVOO_HFKfYEViyuFyn855_LJDaVnwvmFZAJyx-T8Hn-lMpc78_YI04Adw6u4z9qreiCSBZHoX622G1C77TZkd8T9RgT6nZyc1lhgv3kWayPV9onQoucNeLoIVbX2YXBKqyl_b3Ld85ynbhrEd7C7zlk6oVBA4luKRl3Tc8n56kVPhzbyZD6bUZ5gdesWRFHvyaNSV80Zd9iR4lzMxDE3FTLGF66UeKPoSINVQf-bCf1oUixiCkvPmaT78NDlk8Bc_t9_NA3Rzv4OI4KYkDcEQOcfRuRNuhGpuerUU2cmVqRVYwBAdfTdnpxLy4Fe91CrL_PgfBoxRhNI-2CWvJPXYC1InSlOC-KHhZEdijmjt7iCCww13bUfrGPT3BTFc8RtBfEn2YAnIykywjC-gv9jk7-XyjtegumpJRCHOUOfxMGss7O7Vkeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spQlNG9OyxYv9Vi56tYrRkzNYc7SlBsri5Kjm2w6fzr2dF--Jui2rlCI-AqR51GspAjGeiHdILVlgOl2q6jDLXKvykfDXkImAH3g3u5d7E6Rmt1LM7Rc5cj0Pe6iVjhAscBoSxFbgK-i011nIk6XpS4yo25Tod7cuHyS83Wy5qamDQ65HOPxBol2cud5kO6gTzqAKcZUptClSqAjfFuB5sozLEeMbz4xU3RTfLUDAIj52Bm1MQry7QsTONfyUsZPOc71G528ajjMGpBcLl7QQi33HJHxeJ7wvOasprJ_cBle8oUdZPsv8f4BJZJ5fZp9vsLFYss-bYdZjeKdjgA7CQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=aSITL3m9OeviUGFub8n7aynISUwaZ0wiS9lthb8pPfsAgTK84aF2kWmjKk2g3zpW-RQIsvFpL3WF2waPZiPecudLBfBIEOaglqVig-mgIhJN8SGGbfqqsWUk9Lga2Xs7uGbT6qRnTeu0r2dnSL44bAiWPGhjO7IsVMsLVuwZKEsIl6ItCobqX_vrJZ26eWXcEVbNYJOvKrkj0lphIv_lfIeqPzlHxowf1poYxVBjVczzGh24QvhhL3rGHhagX2ly_zjT2vyc6TnT_lVG7t1Fv2b01i_F1zArG2e-zBiQFKCZJWiyxWhHeMAtUamjMw-y4pBo-t33WHIxSyzYWj5upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=aSITL3m9OeviUGFub8n7aynISUwaZ0wiS9lthb8pPfsAgTK84aF2kWmjKk2g3zpW-RQIsvFpL3WF2waPZiPecudLBfBIEOaglqVig-mgIhJN8SGGbfqqsWUk9Lga2Xs7uGbT6qRnTeu0r2dnSL44bAiWPGhjO7IsVMsLVuwZKEsIl6ItCobqX_vrJZ26eWXcEVbNYJOvKrkj0lphIv_lfIeqPzlHxowf1poYxVBjVczzGh24QvhhL3rGHhagX2ly_zjT2vyc6TnT_lVG7t1Fv2b01i_F1zArG2e-zBiQFKCZJWiyxWhHeMAtUamjMw-y4pBo-t33WHIxSyzYWj5upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTJckJ4FdXzYfoIUHoompf7qsW8bfywPvgOgtiDIEwfO2R3T_DhKik4jHkz3w73k78KDyOcZcLfesnoS1ej1ekdjfqbGQM06erwznzJMucvk3mLnamQUbC4jN3Mp0J4cXvCMPsQcrzXNeHeT-HFnmgXOjPDFDcWi9jgVh3LiXN-iXbh4-LIL8NbuCiEcNdgYB7gi3EI4OtUuhEx-1Rp79RYJiKEYiumfJSjR5al1qf0PSBeo5yCOdzgEo23mB68SKrumNWhUbavP_pnkcFNoCPouo66iZE0HLkLbBRwTi80OyiV2DsjZX1dIYpd1Y9Tjy6QTfxvoswOsn2XGt9E1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK0ql7X3DVw_87da5mhBbwmkyTNQcjHwOywsmpp8HlAIe_ILOs3reR9KAUHMvYxn4VwFHFmdpvoWKqN7uZO9jgA6or0DqDU6eRtvheEckDHJMJ12zTat1QQopCF3tYJyZl_tbsXtw1PW_h5VCgRZ9DzPBDzWBvhTv2V6Oyih4_G6BJKJAxLfJCY7PB4Uv5YP4OFrS9JhMtaLgqclsEU1ae16W2-WSn6GYgIkAuc_HIXRZIJ67je7L9PmEL8zDdenZVXuXcJ9jhLhGCBPMH-yL4vycPTOsPK8H2gcFECDgjgjQAMNuHSgB8yQ3Q_XBfTC1ikckF3LFqio45F3dxySsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNuJfSwaEvg4fL4CrjMK0roFNjaMOKF3fzqwU9-6CRocfSGOm7gyqSTyGOFgqvXfWxWXwEfcNIpXcWAevL87jI3-qowgfKaYeDP28nm42J-ps6IpUzBoTbQegArNCE0lOp7T7ZkmUsLNflDuduSD1SREXFtg-8TkaYH7I88d7cOIiJ0hIGb0UUyrFefypCkOrWDfO-SM8dBLKyq3frrMB5MJfa-pu9-nuR24Fm226JDckpe1pJHHktIcdnwNdw3u5hPKFv7QiR43HzEZLTvq8fUxNXhBSiZMQlhr9w6sgc12iGYGx9TzX_yhAqVXdNuHhVjPxDAXe3MJIP4lP0aqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=rhpAnfvOEJ2E9-L2my9Ee_SBtEXwIzVWzYVYZloNMURYirWxdzk8T0SksPk8s1PFzZZxh53rY03odRMrfH7QjasP5DiP-5j-hJcUUgk-T6inll009sQgvlFIPyN3r23y7IWUTecP9H36i0O3SB934NQkMWSuA4n3TvmVs0F3cRhWjyetJaGUbrFiv6gaQWzVkERrrc7h6FTCL8Sobs7W8wBQnvRaB5Bi9dmV7b7YHRFchttq7gLd8UJp36VtcdOwKok5d3EgSaJ92HtOAo0MgTfBs9PLAVXvcl7NLNVxYP7yjYe917PanEh7VpnEOT9dp6B1796ExcisXQx5LtiSww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=rhpAnfvOEJ2E9-L2my9Ee_SBtEXwIzVWzYVYZloNMURYirWxdzk8T0SksPk8s1PFzZZxh53rY03odRMrfH7QjasP5DiP-5j-hJcUUgk-T6inll009sQgvlFIPyN3r23y7IWUTecP9H36i0O3SB934NQkMWSuA4n3TvmVs0F3cRhWjyetJaGUbrFiv6gaQWzVkERrrc7h6FTCL8Sobs7W8wBQnvRaB5Bi9dmV7b7YHRFchttq7gLd8UJp36VtcdOwKok5d3EgSaJ92HtOAo0MgTfBs9PLAVXvcl7NLNVxYP7yjYe917PanEh7VpnEOT9dp6B1796ExcisXQx5LtiSww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEULEa2tRRzzVaKCQBz_cgpK9OqiGgihth2oI_jN15KTtmn39-ArK62wEKyq_C3qa1sNX4JGRqsOqky15A-BjdNdejGVDSWDH8McnCdN1FH6zepEY-vpmOX4Asj3sWOAhbwgo06TFZ02UM9aoDux2BhWILNx5eQeL1DfIk35ve1gBySZ-zfeM0Q79gsRK0TzgBa2c8qGkqCGnpQwlatjShh6_qzsGzDWWLH9nurdcByAfPVYpyyaHPUH_cOS9Cr1sW6j9ScfoLIDm7tosJetYzCqXieniiwIYWO-iyrTI9BaboA3viVNwxvfWvw0Z8eLJkacZFQu0DKfAaTE7n1Muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuyd0xOEhYVBx4cUX8_ryYtXwfQ8hCu7xeinwVEbGvVJrxsWfeRRElQ4AY3d1e5K1CcvQlQAC7_v44Hs-qs9oneyRj9l_sCp0v9CLFrBZ_2j6pR8mwvVddRxoMVddbAq6DI1UgJHsoa9hUo7-vwccK-GzkMb-qCGzeUui5gybEu_d33Qsmv0QbDIxP1tTwSoRXyIA0TJqf2F9uXiMavlVXC1kXqnyIQwdBM0-VLfk3FGVlTue6_2fNxIncfjfyb2ffOwUc81aFsuTFQCEp3nGakMA0TuEZUgd-m0VxkHghiona95tR-zynykzTusmcrm8rZi20p1P_qDJIN0QWrPWbIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuyd0xOEhYVBx4cUX8_ryYtXwfQ8hCu7xeinwVEbGvVJrxsWfeRRElQ4AY3d1e5K1CcvQlQAC7_v44Hs-qs9oneyRj9l_sCp0v9CLFrBZ_2j6pR8mwvVddRxoMVddbAq6DI1UgJHsoa9hUo7-vwccK-GzkMb-qCGzeUui5gybEu_d33Qsmv0QbDIxP1tTwSoRXyIA0TJqf2F9uXiMavlVXC1kXqnyIQwdBM0-VLfk3FGVlTue6_2fNxIncfjfyb2ffOwUc81aFsuTFQCEp3nGakMA0TuEZUgd-m0VxkHghiona95tR-zynykzTusmcrm8rZi20p1P_qDJIN0QWrPWbIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=KGdNo4973bsqQSMcULzJaEo-n0xOu95BffiiiccxguUco3eYgZ87cAghE9Q-XNDi6Digs_x_GFI3PXrOexMN5c1Y-qgTNc0AiUScVmq9wxjtT-Huu0p5RcIJzO4iipfq3Euii6hxtt0JwMen-zkwGlxYpGcS9AAc_ro-lDbcPfNsNHVwnvUt7ACoI_9tgtNQNXZLwBA-1PqHG-ohNUtPmK7LHUxu3lKr8wnyxuZNI5j-sXhnu5EYn8BWkhD9OUb5h1h7U_8zz73TLhgeVhgYbZTs2mifnducdOXjjA-hXmZE-wxpzCzKr8NDTRcIaCUlHPPZKpKb3nY5cibVSzVqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=KGdNo4973bsqQSMcULzJaEo-n0xOu95BffiiiccxguUco3eYgZ87cAghE9Q-XNDi6Digs_x_GFI3PXrOexMN5c1Y-qgTNc0AiUScVmq9wxjtT-Huu0p5RcIJzO4iipfq3Euii6hxtt0JwMen-zkwGlxYpGcS9AAc_ro-lDbcPfNsNHVwnvUt7ACoI_9tgtNQNXZLwBA-1PqHG-ohNUtPmK7LHUxu3lKr8wnyxuZNI5j-sXhnu5EYn8BWkhD9OUb5h1h7U_8zz73TLhgeVhgYbZTs2mifnducdOXjjA-hXmZE-wxpzCzKr8NDTRcIaCUlHPPZKpKb3nY5cibVSzVqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=H1iCDzK1ScrgCFGh5oTzTcIaNhe0InCtKFFb9-QFZkcRRzqVqbTqV8MDFnoz6cNwhvST2zY5RSu-k96LHdu5dbA04gQDWOFVNiAD9w-_hnxAKpH8gVabUxS_F4minn0fZ7F3Tvde8SzdutBnIXx6Sw3Popm3R2xZRphrLftF8ci8nBODUAXoZ2oBII13h9tKJ32Pe9eNgK2WBwuMrCGoH0pjpNEt2DGoZ0ZAjdPya49KtQKV6W8fqdjMOASgUGNxnVY_kcTDg3AiXcQWkdCVVTZeUkZdBA9Pbsn_yyxLpu7gxql7oUmnwPdrVWtzsrLQ6EE199o6-Micwb5gwRFO54OPKWvXtX573JawaUykkdbzP95A0xfOFNOO6Rh9ZC7PYfjzhv_NAyvlZ2RiVm4Ngy14p-Ox2Ypavt7p22cz436YhAFmIfvMTwENOuo5anLi9RuoXO_dryhf8tpWsTyxUoLMtkLSMxLPZbQXU7zeyUxx2y8GKIbtH36Qr4815NZJPbIhnP1ds5R0cxjAjVJ1B7Fxta3saxIw352dVSA2UEUhKG_rlsJdGfR5vwj_8EPKh66lsjBhCWfCwnQWA5EPUapY3IfWXQbpZ8TiAa09SeT0KEpumJqF_T5eYLAvdFT4Bw0sOesC5Bi2gWYcQK8-6WTu2aTRviSmdvLoS-xBlxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=H1iCDzK1ScrgCFGh5oTzTcIaNhe0InCtKFFb9-QFZkcRRzqVqbTqV8MDFnoz6cNwhvST2zY5RSu-k96LHdu5dbA04gQDWOFVNiAD9w-_hnxAKpH8gVabUxS_F4minn0fZ7F3Tvde8SzdutBnIXx6Sw3Popm3R2xZRphrLftF8ci8nBODUAXoZ2oBII13h9tKJ32Pe9eNgK2WBwuMrCGoH0pjpNEt2DGoZ0ZAjdPya49KtQKV6W8fqdjMOASgUGNxnVY_kcTDg3AiXcQWkdCVVTZeUkZdBA9Pbsn_yyxLpu7gxql7oUmnwPdrVWtzsrLQ6EE199o6-Micwb5gwRFO54OPKWvXtX573JawaUykkdbzP95A0xfOFNOO6Rh9ZC7PYfjzhv_NAyvlZ2RiVm4Ngy14p-Ox2Ypavt7p22cz436YhAFmIfvMTwENOuo5anLi9RuoXO_dryhf8tpWsTyxUoLMtkLSMxLPZbQXU7zeyUxx2y8GKIbtH36Qr4815NZJPbIhnP1ds5R0cxjAjVJ1B7Fxta3saxIw352dVSA2UEUhKG_rlsJdGfR5vwj_8EPKh66lsjBhCWfCwnQWA5EPUapY3IfWXQbpZ8TiAa09SeT0KEpumJqF_T5eYLAvdFT4Bw0sOesC5Bi2gWYcQK8-6WTu2aTRviSmdvLoS-xBlxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=iEDPZyOnn9fge8is67YcqbbigCcp2v-_pf1V-9qchr4AsUCaN45HIG3ZLwNA8x3V8QyOk4xPRt5xUwV2hN9I59PC8xReiM-2Enn3gIuJbVDTm5uZ3BIxz69GNFoVhild2ksZgzXGST64-18FFnxdzRn7VdXJ1Q3jK9WwmQ_U8jeRXvSfRgy9bZ-Z47dPqch_jKvG5IYU8BXS-0ZvjO47GTQEg44OcieKkK_ysiVePjuZtpSoSW0go1KLF2eojwyMU5VSkKIV786NX37I8dxSsOCYIUUOvdAD7wnbb6aR2yielhbB3CD530BHIOYrwbAjtle6Uq9fDXgTgKvt0EJnkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=iEDPZyOnn9fge8is67YcqbbigCcp2v-_pf1V-9qchr4AsUCaN45HIG3ZLwNA8x3V8QyOk4xPRt5xUwV2hN9I59PC8xReiM-2Enn3gIuJbVDTm5uZ3BIxz69GNFoVhild2ksZgzXGST64-18FFnxdzRn7VdXJ1Q3jK9WwmQ_U8jeRXvSfRgy9bZ-Z47dPqch_jKvG5IYU8BXS-0ZvjO47GTQEg44OcieKkK_ysiVePjuZtpSoSW0go1KLF2eojwyMU5VSkKIV786NX37I8dxSsOCYIUUOvdAD7wnbb6aR2yielhbB3CD530BHIOYrwbAjtle6Uq9fDXgTgKvt0EJnkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AafpKbxuSHpMf-x_iKwJ6Q7DOHo9kwyQHq-Ntz-KmI7_O3q31_h3tI0O2Paondy-zT9FRUanBxt7OODV4mW-PmHiqSgU1PFgd_5QqRon7d9mkRMklBBL4pWoQ-kHJ2PJMVJjhJbW3n9aUFm_F_OXjUz6o46l8sAbKRGAU3Pj3VY-178r-alKWNohJx_Blf749pRt_l4OnYYUSTRSFjwzour0qQLXfzXN4V3PYBpvytZdnAr8WKKdXWYBj3f7viMns5mOxyC5nfr0jcPM3FXuA_g84XmDsqFONP9qMHj9xOJK-2Wg7hMuQYK3YeePCwByphNwgIYvSdeJW6pJz_4uIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jfAHZs2BNS5s95kXvCXLeSbA8gVe0o9bpIBVbZ1ucri3almxuiHY3_OobtxMa-anOTGyge60MlAKCTEmCaJ4y_A0bR1vE9He_hqd9pkYrv2ah3f-WNYOrjrz5WloA-4CrnQqN70oFpJp6VuYBBvAhZzGXHENqDwys2M7QLWf-omgKMNz_F43PCN3K2J2APjOkVwuTyZOg5ZwvZLcWaWOXFFFlvhPDe1c9ss5sl3EF1YC5VR4q2sgs6LBiNYcFLY_9f3OqvUIMkoUW8cjyyAe4rE7l1H_ySD-Txtc9y0JlTSlHbs5dqhqbFl8L0B6M3z3LeRhHhgbNtZ3tW4ava4LOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jfAHZs2BNS5s95kXvCXLeSbA8gVe0o9bpIBVbZ1ucri3almxuiHY3_OobtxMa-anOTGyge60MlAKCTEmCaJ4y_A0bR1vE9He_hqd9pkYrv2ah3f-WNYOrjrz5WloA-4CrnQqN70oFpJp6VuYBBvAhZzGXHENqDwys2M7QLWf-omgKMNz_F43PCN3K2J2APjOkVwuTyZOg5ZwvZLcWaWOXFFFlvhPDe1c9ss5sl3EF1YC5VR4q2sgs6LBiNYcFLY_9f3OqvUIMkoUW8cjyyAe4rE7l1H_ySD-Txtc9y0JlTSlHbs5dqhqbFl8L0B6M3z3LeRhHhgbNtZ3tW4ava4LOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=QhK8cHEEJSe65DVUIQYZcXG_jZBRREkogC412I6xYfSHSsQ07X9XlMaQpAPHM2knvVRifqcRDQ1Te4wvfmlecpuEAP_DPaky3xP-JrFAi6SvIgJbr0FH6ZKGpNeKq1bABFVmLNEX_s99w05aFhZ5WM_jg8dR7tGjfu7yn2KGKYW0j3_r-6Pq0OwMT2DM9Nf-ibXGLEnxdp0Zsm6o8Xq2XaDp15MCR1nmSmOWW2C6WQ9tdGxdUKb-se3j4RFrkDy-j3oIXlDjHiH2boqnca1jpVALOQGtprdmqu7EoG7GGg0bKD9LMNSXtVhQ__-ywzybSbcXi3xS7KO0z3pojKE78JSJnOCdXsKPsToFNwyCsh7kSB6D8zUjPsbyBMrW6B8xz6jXsUy7kbFmVqhGDhbRx2x4U5h_eiB70zpXpta_yq0UNGT9C0ufG3LIt18btZ4w6jAp4tFQ-_1BF72WgmZzUFS_hq-yMU7YijLut7vbXOZ46E9LXiQ901HjkNVAz3S67FjSSMNd6lhRN7BZYrBOwGPbSfvmce71DPQ7GCJXpRpJi273IEZOHiutocNkqz_bLwYP0L9vLxYAoa6GgPckiVUw2JAihp7Lwmij6xpvUKA-OPGIul4scP3lqqvjEplXUjph5beIdSO0zePJ7XIMgOBcHg-zCvn6379B5CIGPGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=QhK8cHEEJSe65DVUIQYZcXG_jZBRREkogC412I6xYfSHSsQ07X9XlMaQpAPHM2knvVRifqcRDQ1Te4wvfmlecpuEAP_DPaky3xP-JrFAi6SvIgJbr0FH6ZKGpNeKq1bABFVmLNEX_s99w05aFhZ5WM_jg8dR7tGjfu7yn2KGKYW0j3_r-6Pq0OwMT2DM9Nf-ibXGLEnxdp0Zsm6o8Xq2XaDp15MCR1nmSmOWW2C6WQ9tdGxdUKb-se3j4RFrkDy-j3oIXlDjHiH2boqnca1jpVALOQGtprdmqu7EoG7GGg0bKD9LMNSXtVhQ__-ywzybSbcXi3xS7KO0z3pojKE78JSJnOCdXsKPsToFNwyCsh7kSB6D8zUjPsbyBMrW6B8xz6jXsUy7kbFmVqhGDhbRx2x4U5h_eiB70zpXpta_yq0UNGT9C0ufG3LIt18btZ4w6jAp4tFQ-_1BF72WgmZzUFS_hq-yMU7YijLut7vbXOZ46E9LXiQ901HjkNVAz3S67FjSSMNd6lhRN7BZYrBOwGPbSfvmce71DPQ7GCJXpRpJi273IEZOHiutocNkqz_bLwYP0L9vLxYAoa6GgPckiVUw2JAihp7Lwmij6xpvUKA-OPGIul4scP3lqqvjEplXUjph5beIdSO0zePJ7XIMgOBcHg-zCvn6379B5CIGPGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu901E0bqnnPX98aYmwDLwuRkmC2TYJ5KRnDj5G5Qj5NX4YDm5x3OePuCF63dzKi4JDxqOm8L0cKER4jYdnjkN-4qIRArBUFKOHVOcPLpjJ2RZuYuX3JYdYThu0X1H9yGem1VREIwJ6HYZNtrsaGEXMT5ulFKcf6yNfishXiMBf7Q0a-qf1OyPeHzEdKvLdbXnAwv6q0PwcEU9pUwmIqlVRTjOMr-JnpvIpYVcP7gqjAt0sGjfCUuVy2EA6TSsiFmoXaq6qVf-6ecAuYgSDO-WLKwkibDu7J0EMBOZ1Phc0JeFVP3ZzIyhMvTNH3b30_tbqEhVEYjl_xJ3BBsBGmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Ir5V4NAigj5RiI1f3xI0YPXdKiF8QHQFnFbXtT2DIS1_AX7_-oTWsT3GASVNN15uMaZRu-GlNs4kdaPuoYqenAP0ygV4QK6h19Sd-DsDltr2I2edJcXh-hyuc3p9p9GTupRGqxyN4Nlqdtyr1DRzu72BumsFdoUzhlPn33DlKcAj-dEXR3ZYsfPawiIpJfSA6ixzeU9KAyGMTIbKgeBxylV4oHMXdl1tWeUx0_PHNS1wtai5SY0ZEHdRJv89O0OfmpNRtAAOkotUX8qGIp5TzmURvBatSkc_VioLkjxivbfhuKkP-PQ2wINTHQKvryKK_AvwZ7tAzA3JMSxjWH991bgUglmzXgzzDVblhbi_f12PF7N62VVUHOaVcZYY9dDcW5Z8hCjUNNpyPj_AKrchCUoeix6uJFIBKl5_zM4BEZsOX5qztoCdrIlF3vZmzI5E8eDpChQGu3RIADnfjl_wgXRx48aKs0zMZ-uDvXl9qOwJUHsTsnRp9LwvEft7y3nccFTivI42kKcFPWSrxJHCcJBktN_ESI-Gy3-NpPVG6l5EHFZdKI_muL7FkglpZ_48wf0zgYiN6Y2nf8yrm4qX3pocZhhhMO_Y-jbn_3GInNEIU8i4X4KOvm4Yl_BHz-VpF98_Ltyr8icV2WCHyH73rv9ymv-WEpSndT39a4Txujc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Ir5V4NAigj5RiI1f3xI0YPXdKiF8QHQFnFbXtT2DIS1_AX7_-oTWsT3GASVNN15uMaZRu-GlNs4kdaPuoYqenAP0ygV4QK6h19Sd-DsDltr2I2edJcXh-hyuc3p9p9GTupRGqxyN4Nlqdtyr1DRzu72BumsFdoUzhlPn33DlKcAj-dEXR3ZYsfPawiIpJfSA6ixzeU9KAyGMTIbKgeBxylV4oHMXdl1tWeUx0_PHNS1wtai5SY0ZEHdRJv89O0OfmpNRtAAOkotUX8qGIp5TzmURvBatSkc_VioLkjxivbfhuKkP-PQ2wINTHQKvryKK_AvwZ7tAzA3JMSxjWH991bgUglmzXgzzDVblhbi_f12PF7N62VVUHOaVcZYY9dDcW5Z8hCjUNNpyPj_AKrchCUoeix6uJFIBKl5_zM4BEZsOX5qztoCdrIlF3vZmzI5E8eDpChQGu3RIADnfjl_wgXRx48aKs0zMZ-uDvXl9qOwJUHsTsnRp9LwvEft7y3nccFTivI42kKcFPWSrxJHCcJBktN_ESI-Gy3-NpPVG6l5EHFZdKI_muL7FkglpZ_48wf0zgYiN6Y2nf8yrm4qX3pocZhhhMO_Y-jbn_3GInNEIU8i4X4KOvm4Yl_BHz-VpF98_Ltyr8icV2WCHyH73rv9ymv-WEpSndT39a4Txujc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=nKPNT15boagHMO57EDT--pUOXeNxF0eljhs3dePK-4ozKmn6tyVzdQ2xBAAPNV9ySfzXlMNiZE5UbijBi3O_zjMHYO_DRMs-f6lFNERbke5pK--mirqm88T2MRqYINXUEytssYnNMmFAyp5ca0UHSSqwcpBQBx7QxcQtsYIoEiRjiijI13YX-O6oHP2yp_TvoXt025JwkqkZdmcPNtQjiHT-fJyeFQ-Pk7lsnyqi2D7fRB6E46X7IcS2-pDMRNmmvgcmevEGAoxa3u_UsB41SQafhrQuGL4B0reM2P8AepuojwglMgZihgdp5tv1D-6tDzDGM1wjFAE7HbcjDsg3D6dXe_P8efnhlB2ToRSF3T8BsZT5jeSdar_iQOqG4Zb8oM5rz7y9KqkhjHJStFtcjY63N2BgmGxrYpcPcTtz8OOEpUnekNEtgyFZk9vkvTdR0E8Duv7gN2R0wKrhEaepBQvYFU-gv8kN6L1q6e5K1y9dtFUFd5qahqqKUn5nJg5UOqL8UbFENCgWlNIbVZKHvgVBY2BbJKUf1BpdB-RWlD2mKIClognIuSDSFLuhqOIfqkX5zcQsTl2rqJ4TxJE0ad6p4-0kXcxF4XG5bS18ZaDLMbFWvpSDy3xDVp-XNw7YRg0NTIRbrCJT9EX1SXNw58elJcZYjqm9_yYFNXKqXHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=nKPNT15boagHMO57EDT--pUOXeNxF0eljhs3dePK-4ozKmn6tyVzdQ2xBAAPNV9ySfzXlMNiZE5UbijBi3O_zjMHYO_DRMs-f6lFNERbke5pK--mirqm88T2MRqYINXUEytssYnNMmFAyp5ca0UHSSqwcpBQBx7QxcQtsYIoEiRjiijI13YX-O6oHP2yp_TvoXt025JwkqkZdmcPNtQjiHT-fJyeFQ-Pk7lsnyqi2D7fRB6E46X7IcS2-pDMRNmmvgcmevEGAoxa3u_UsB41SQafhrQuGL4B0reM2P8AepuojwglMgZihgdp5tv1D-6tDzDGM1wjFAE7HbcjDsg3D6dXe_P8efnhlB2ToRSF3T8BsZT5jeSdar_iQOqG4Zb8oM5rz7y9KqkhjHJStFtcjY63N2BgmGxrYpcPcTtz8OOEpUnekNEtgyFZk9vkvTdR0E8Duv7gN2R0wKrhEaepBQvYFU-gv8kN6L1q6e5K1y9dtFUFd5qahqqKUn5nJg5UOqL8UbFENCgWlNIbVZKHvgVBY2BbJKUf1BpdB-RWlD2mKIClognIuSDSFLuhqOIfqkX5zcQsTl2rqJ4TxJE0ad6p4-0kXcxF4XG5bS18ZaDLMbFWvpSDy3xDVp-XNw7YRg0NTIRbrCJT9EX1SXNw58elJcZYjqm9_yYFNXKqXHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ffkED0EWfhvp2bp4AW72q4gKM_p2aTfkWRlnNP0TgGy6hyBVdVK3JN3JJ7Ue0Aw6lOQwPeXkObE8E1SSOMign7eqm9ZbQiceDx5NIAl6ZVPuebFc89DREZYSAe7agxmIgcPiGKarXTF_P8s61tAGcbuwh4SVzOAEhXpDncNL5J3_cJ0QQQ4K1AES9rxBhlwp9_PwARTXiFs2pM3frW5yx7iqpTW2had_SWPhY01YyQAGk4WGbDn0eFIdyfR_IYh9aoFmF1o70sGBGd0duV9Ulz8zoIPjOR2rDTscpc2hdcWn6a6Jzlf574_WjRE7j35DjS7rhSC70O2lVW0oe6yvNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ffkED0EWfhvp2bp4AW72q4gKM_p2aTfkWRlnNP0TgGy6hyBVdVK3JN3JJ7Ue0Aw6lOQwPeXkObE8E1SSOMign7eqm9ZbQiceDx5NIAl6ZVPuebFc89DREZYSAe7agxmIgcPiGKarXTF_P8s61tAGcbuwh4SVzOAEhXpDncNL5J3_cJ0QQQ4K1AES9rxBhlwp9_PwARTXiFs2pM3frW5yx7iqpTW2had_SWPhY01YyQAGk4WGbDn0eFIdyfR_IYh9aoFmF1o70sGBGd0duV9Ulz8zoIPjOR2rDTscpc2hdcWn6a6Jzlf574_WjRE7j35DjS7rhSC70O2lVW0oe6yvNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=NAvON01bwF0mOOhk0XRjNjPp8dvR-ZGec4-yJJ1ik1Mp_5lPQCPxppRfmNMKhuz9PKkboO1o2l0_xxyY00lMBkfqJZ0zkP5lRJVtlZz9zpu3KWzYWG0yRc8TzwnUu839Xhhqq63AGWJeTOKCqm8g7yHtbKuF0eSllpqFvkRRiOC0PvtLLAG8e8dQJTwfaKRv4xuV4QFLYwoQFdeT2PM74iqC8aT5xXQj8VOM2jjkkxKRopqRA0aIcPlWatmi0i4bjuGu1nuiS2YxMvTtgEsLthlWUAxWZRk63N2eNgoAgVOgl6ruwCA1gFKbm8BUELOcWDTVFmLF0OjpqgJBGHadGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=NAvON01bwF0mOOhk0XRjNjPp8dvR-ZGec4-yJJ1ik1Mp_5lPQCPxppRfmNMKhuz9PKkboO1o2l0_xxyY00lMBkfqJZ0zkP5lRJVtlZz9zpu3KWzYWG0yRc8TzwnUu839Xhhqq63AGWJeTOKCqm8g7yHtbKuF0eSllpqFvkRRiOC0PvtLLAG8e8dQJTwfaKRv4xuV4QFLYwoQFdeT2PM74iqC8aT5xXQj8VOM2jjkkxKRopqRA0aIcPlWatmi0i4bjuGu1nuiS2YxMvTtgEsLthlWUAxWZRk63N2eNgoAgVOgl6ruwCA1gFKbm8BUELOcWDTVFmLF0OjpqgJBGHadGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ndcfm6xzAfbMk1PWFTuRiT-ZsIfU0ur1UHVi1slIk5MBIP7NXxmnJ5VMj6vEnHA7JWDZRsHn3SSBdtNvQivBnzThriJnTB7TR8sFQYq8unMAuKzaR6VROvQt07eRByOux4Up1NcnUXz7oTMQmpS_CUk-HO3FqMIepQwsY6734-T1VyTXjSYK-6VOxSrj8X4ul4zMtUO-R4dM5nyIu8wp2x5ipfmH2XZ1CHllcJ81WF8d3mqcm2ALlJVZJMuvsFqpozSlQ7VRS0QIHB0NaUNzrArZ2Nrh7TMwenMca1fUNZJdHT7IGayjn5x8OjsIAwTDOX936lgZM2VOWUHEidzJMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ndcfm6xzAfbMk1PWFTuRiT-ZsIfU0ur1UHVi1slIk5MBIP7NXxmnJ5VMj6vEnHA7JWDZRsHn3SSBdtNvQivBnzThriJnTB7TR8sFQYq8unMAuKzaR6VROvQt07eRByOux4Up1NcnUXz7oTMQmpS_CUk-HO3FqMIepQwsY6734-T1VyTXjSYK-6VOxSrj8X4ul4zMtUO-R4dM5nyIu8wp2x5ipfmH2XZ1CHllcJ81WF8d3mqcm2ALlJVZJMuvsFqpozSlQ7VRS0QIHB0NaUNzrArZ2Nrh7TMwenMca1fUNZJdHT7IGayjn5x8OjsIAwTDOX936lgZM2VOWUHEidzJMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=BDrQKp6xz6G61i30UXCRZp2X5SZK8nHyW6lkAqVPNVwB9RHyVoe8VnTB4MhaYzKt4rOekpDviL7waTWAPcPQoahWcMayEcJ-Quuv-Pdn0A_yNTnsNOWEjfuMQJQJno1-Mosw-HRVe-ClgHDPEkQ1Yv6IC3pncwqCyTMLKJ5k-5zlSgLhXch1nbFftDzpyd-CUkSanDxp4p7z44q56qv1rMsBaGivPMYy0V2KRma2177XeCaZL3hoaMh6DD7yojPQWK9GcwBv6f7Q4TYJKho27Ngtga5k-f0oEs717YrBP9ogvacEkyyaY-hXrpp3QrIp7am6EMboPAi4AxMEw1LycQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=BDrQKp6xz6G61i30UXCRZp2X5SZK8nHyW6lkAqVPNVwB9RHyVoe8VnTB4MhaYzKt4rOekpDviL7waTWAPcPQoahWcMayEcJ-Quuv-Pdn0A_yNTnsNOWEjfuMQJQJno1-Mosw-HRVe-ClgHDPEkQ1Yv6IC3pncwqCyTMLKJ5k-5zlSgLhXch1nbFftDzpyd-CUkSanDxp4p7z44q56qv1rMsBaGivPMYy0V2KRma2177XeCaZL3hoaMh6DD7yojPQWK9GcwBv6f7Q4TYJKho27Ngtga5k-f0oEs717YrBP9ogvacEkyyaY-hXrpp3QrIp7am6EMboPAi4AxMEw1LycQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ecWUkgEMQmoR31nOiSBiq7IU9vy87OxzzZm8ANU0drlV-S1j6nDWkFwN0WLYOXcLSnPaNahsvMcv6vSXX7D1GScugkvbFSvDcuGfirmXBDa-8_M7tgm1beXd3mLZ2uREUJ-qjMN1xTrZsYIs0iITmHrWuULGRlSWuubzJeUsNZINyu5VQgUu_C0eusRI__GYkFA-B-9JxBejQY-wytFcBtfiC-A9mhD7CWNBCRBtHOHWOKk62-zFzkfTF3gdoUKYI9qncE7fpIli3VJn7IhKirKqtDg90IlapFf4qciig8tqLMjO4Cp6nOTjRetgdV40sp_mpT574ivv4I1CeBpxGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ecWUkgEMQmoR31nOiSBiq7IU9vy87OxzzZm8ANU0drlV-S1j6nDWkFwN0WLYOXcLSnPaNahsvMcv6vSXX7D1GScugkvbFSvDcuGfirmXBDa-8_M7tgm1beXd3mLZ2uREUJ-qjMN1xTrZsYIs0iITmHrWuULGRlSWuubzJeUsNZINyu5VQgUu_C0eusRI__GYkFA-B-9JxBejQY-wytFcBtfiC-A9mhD7CWNBCRBtHOHWOKk62-zFzkfTF3gdoUKYI9qncE7fpIli3VJn7IhKirKqtDg90IlapFf4qciig8tqLMjO4Cp6nOTjRetgdV40sp_mpT574ivv4I1CeBpxGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=kQALlcmL26ozj7KsOxf9uV1pwYYz3v0hkJtDStB87q0jr8HMro6OJEtlpkU1xgDVc5X8WGxWijf3mQPQv0UPf4FMg_VIk6lnvCCZT-KYzLwy9FiW0uTQnJoo4u9USwH9Jni33hf1EDC51gtXjaMFoxIEFnz8DKgDBEkQTjES60PHHAEqHLIuJ0VO1ftelJXKNDvFtFLA7akVE34Q152zkAdTncyDQJj5DGCSj0VRZQxej_h110vtkgU1aPnaN1iKmpME59HtZ6HcYtqPFPoaJ7HCiMqSPMLOPYxNwAn39M5WhuE1hHpmeYBQ1u0wGFsGbTJ7nxqMaAKNOit0jonPDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=kQALlcmL26ozj7KsOxf9uV1pwYYz3v0hkJtDStB87q0jr8HMro6OJEtlpkU1xgDVc5X8WGxWijf3mQPQv0UPf4FMg_VIk6lnvCCZT-KYzLwy9FiW0uTQnJoo4u9USwH9Jni33hf1EDC51gtXjaMFoxIEFnz8DKgDBEkQTjES60PHHAEqHLIuJ0VO1ftelJXKNDvFtFLA7akVE34Q152zkAdTncyDQJj5DGCSj0VRZQxej_h110vtkgU1aPnaN1iKmpME59HtZ6HcYtqPFPoaJ7HCiMqSPMLOPYxNwAn39M5WhuE1hHpmeYBQ1u0wGFsGbTJ7nxqMaAKNOit0jonPDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=oQPh9-CHkc73F7rIBrdLCrknSqC2QrC0zVbQ5NtrojRqxJ9YnVAxYPTN0RKVZny4sSkGYBy2yQGZDX5hjTZN4oDNQntJqrMwiJwasluJm8jfWCSKFJlF5GtmnJ8r5JjP3PaeYfcrQWPpG8x_ulinEiNcMxPGaCvPMS2TnU-_D_LnkS2WCNTzYHnvQ_12DUmPfcXpXsgBJpe8Rwvi8MmoWa7OKwaVmxSNxzIjKx538KlkDaVkrLjUgrMkBIM8LxlLaEWm0iv_rx-N8BnEcu9nlmbgg10G5XtkHlKjjuJWL_IKuhVbATgp0n_Pdrvq3dw669I3lT8iMphLT6B-lQu9Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=oQPh9-CHkc73F7rIBrdLCrknSqC2QrC0zVbQ5NtrojRqxJ9YnVAxYPTN0RKVZny4sSkGYBy2yQGZDX5hjTZN4oDNQntJqrMwiJwasluJm8jfWCSKFJlF5GtmnJ8r5JjP3PaeYfcrQWPpG8x_ulinEiNcMxPGaCvPMS2TnU-_D_LnkS2WCNTzYHnvQ_12DUmPfcXpXsgBJpe8Rwvi8MmoWa7OKwaVmxSNxzIjKx538KlkDaVkrLjUgrMkBIM8LxlLaEWm0iv_rx-N8BnEcu9nlmbgg10G5XtkHlKjjuJWL_IKuhVbATgp0n_Pdrvq3dw669I3lT8iMphLT6B-lQu9Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxUrvBDiZXEPpzBZ2UXieFh17vganapc0OAM5gmasodzItab6CVlrsl6rD0FoWOHilQOQ8K-bhRltXk_uMYxxZQTgiw-EUpC2tcO5e3VSIWX8P__kDTEP_RvmdplI1d-6mFO-3i_lvbJyJpOWykBNDkE_wVsd4VOR4dWUUxBU5xa3WevLieLt0nehPA--X0_HfRWG34bHgJxZpT4E9i3Skp7tddg5XUFN8aysrwkMwAGkjZKh5aAFszluR9qUg7RWdVk3YFHuvtwGRa8xw3VpDIyAvWQhA8Hy3dM4WecIHxc4GjZt48jEtRmtmPQlX9bLnY1e-u6jWKOx_WmQUOtnA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=j-8-RaKzIM8bPNEbliO0QpEGzAlhoaycU8bCkNgnNh2zCIpPGWQPZPvvS_1N_PxLmcwMM7v-RTPJJ-VUuqgcvK_svj7wyO35OckFlRVvnUwXg6hilVfieTHtrJLz3F_gdpz_-KuNBv7ocQ0Gpwy--VHFNKsBIxmFr1xLxyW-1EtafATb_RlLeqAZJLvHqT09Z5g0OfDJcAWwNJsxu8Hs-0_IOe3vRcdO-8TIQtlhuAzUMi_vrzD04iJ39qT-c55vAkYptM86bnkALVypweyVNmENeuCoUFlft_I0W7OWuIe4yapeBosviuXo5LuXAqO5MZuhhxIbFkJxm85KJO3_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=j-8-RaKzIM8bPNEbliO0QpEGzAlhoaycU8bCkNgnNh2zCIpPGWQPZPvvS_1N_PxLmcwMM7v-RTPJJ-VUuqgcvK_svj7wyO35OckFlRVvnUwXg6hilVfieTHtrJLz3F_gdpz_-KuNBv7ocQ0Gpwy--VHFNKsBIxmFr1xLxyW-1EtafATb_RlLeqAZJLvHqT09Z5g0OfDJcAWwNJsxu8Hs-0_IOe3vRcdO-8TIQtlhuAzUMi_vrzD04iJ39qT-c55vAkYptM86bnkALVypweyVNmENeuCoUFlft_I0W7OWuIe4yapeBosviuXo5LuXAqO5MZuhhxIbFkJxm85KJO3_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=p_947jF3kjV1JOCizRySdFQexRuneM4xa1X7_7dNYA2MVbVKloqTsfIjSWqRCwV4iGCC26cZWxU3P3oq6b0RrW2yhaz7lT--hZoKNhV_5YJTpF0bxkIwrbNcxOGpOx-VFfB1_IuXyUMCG8Q1egUzohP7FmFvGiFskLeOyowEVu4oHwf-c-X2wxrAYxgwuyUetNCUT4j5OfzgTRK2R7ALeBDq3EkGLDV4VpeD9571upnLcTysBoMVbkEpXkSsGwFSOO-RBZPc9xf-i4AhUhwqfDWiqRKmTXkXi2ujwWSjfjlaUcDduz3jqPJ4_b6iFigKsVhbdtym3eAeG90-TCD_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=p_947jF3kjV1JOCizRySdFQexRuneM4xa1X7_7dNYA2MVbVKloqTsfIjSWqRCwV4iGCC26cZWxU3P3oq6b0RrW2yhaz7lT--hZoKNhV_5YJTpF0bxkIwrbNcxOGpOx-VFfB1_IuXyUMCG8Q1egUzohP7FmFvGiFskLeOyowEVu4oHwf-c-X2wxrAYxgwuyUetNCUT4j5OfzgTRK2R7ALeBDq3EkGLDV4VpeD9571upnLcTysBoMVbkEpXkSsGwFSOO-RBZPc9xf-i4AhUhwqfDWiqRKmTXkXi2ujwWSjfjlaUcDduz3jqPJ4_b6iFigKsVhbdtym3eAeG90-TCD_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=stlKqhPJJ24nf2Zm5zHDRP_a07jnh6DjgQa_gg54oXwgMnpQ0vBA5tHRdM-eq2lFRDcDvX3Pz_eBKun1lwgIIoXoC_MinmeECvV8m_MkAJ584t6_s6ttHQ3u0RPVIB7qkhKoITsPACFeQy2E12FGX35P4x4F_qH0BK0i6RpsbBngYkvZ94fYjsykPUcHaWWE69xl6JWPN8gGw7ETl1DFQKTpRoOidPiOHUFplMysv0eiiuqPY-qxQQykgwF9v62TQ1D-jIxLV_-euM0HsCUbrsoURcZkTOigDPXPx5IKYkR-xQ03TEI2-lyA_hi_wzMu8WsHKm32dRRtZe8CyJ1lYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=stlKqhPJJ24nf2Zm5zHDRP_a07jnh6DjgQa_gg54oXwgMnpQ0vBA5tHRdM-eq2lFRDcDvX3Pz_eBKun1lwgIIoXoC_MinmeECvV8m_MkAJ584t6_s6ttHQ3u0RPVIB7qkhKoITsPACFeQy2E12FGX35P4x4F_qH0BK0i6RpsbBngYkvZ94fYjsykPUcHaWWE69xl6JWPN8gGw7ETl1DFQKTpRoOidPiOHUFplMysv0eiiuqPY-qxQQykgwF9v62TQ1D-jIxLV_-euM0HsCUbrsoURcZkTOigDPXPx5IKYkR-xQ03TEI2-lyA_hi_wzMu8WsHKm32dRRtZe8CyJ1lYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=XxB38FTgOVFt5tlChImlkmlV9qMDfAjKly1Rl30RBxk4YrE4FXq0HGyVI-ApWgTo9M6LmP6qJmRIu2gfgy9rgGPFLd1itoa8k9VhaiJbSvg8wAp6Q-BhSx3q66_vaX8HDTf0uc6asrMB_fBsssVRnz-0670qkrqmH6gjVf7dJJD9xdXG7HRlvB1CilAlZeytZ_lJAsWirMRQUQ3TGaLoLsxfLYfBWxvNGEmEgkt9_g0iXRLGll-rQk9UrhistY_XG8XiMAe_CnmUDktTpkevwkHnwToPF1-RFYkBFsB4CoeHwGs9YC7inS6e3sz_Bk-TJhshR6shlyU4pKvQJgdivg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=XxB38FTgOVFt5tlChImlkmlV9qMDfAjKly1Rl30RBxk4YrE4FXq0HGyVI-ApWgTo9M6LmP6qJmRIu2gfgy9rgGPFLd1itoa8k9VhaiJbSvg8wAp6Q-BhSx3q66_vaX8HDTf0uc6asrMB_fBsssVRnz-0670qkrqmH6gjVf7dJJD9xdXG7HRlvB1CilAlZeytZ_lJAsWirMRQUQ3TGaLoLsxfLYfBWxvNGEmEgkt9_g0iXRLGll-rQk9UrhistY_XG8XiMAe_CnmUDktTpkevwkHnwToPF1-RFYkBFsB4CoeHwGs9YC7inS6e3sz_Bk-TJhshR6shlyU4pKvQJgdivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_w7XhXBGL-2x9VOg7yvkkvm-gnojMirC21cSW_maWlVmSj-1VEX-k71ksG1MpD3wzr1dfmxzatoNo58-Ys9Mp-l6kbJaLn6EfgbljMmw-pgJYqBuZnYhQ8kIz3oA5J-JbiE90AJ7jx7jb6a0nMbS91GPrr7Uk9XhaVWS4Z8KZAo3fF1o6JjICMf17ZIa79mHNifj0z9vw0iP8WoAkLjSeR69cnat3KYV5ojTLJCxfk-VTwElATk7mPYAUl2ycYbSaNhAqgRc26gvehgQ5Z-_q74tAXf_PJt7tF6eDoGE06m_hUgn0QKYJwctLyN5M96ENrXv7Zc7qor0t9T2TSolw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=IjOVYO44CuFbsrw8QsibI1bEg1yLuTvLY7Ua1-bz1JUojG7rONxADKBUXoAdcmMiuA5YJ_mmKk8cwYnOaewb7hmyhYf58zpK8mesGFFdeos91OPjcBommyAHahhJHZhZdKzeaUumv2YGHUVPP94eu-Q77_Z3VU22RhaOSuFyqRIGET-9puXTlhxaBVBLu1-I5D5A9XiLQuFKOxaJdPku3FLMrlQDNn2SsmsKCsfenxD6XlI2sjFFUNPORtmAVvwsiOheNWoie-N0Oscb2ArZJZXI6hF04mO54N6w2XvCGRSaec4xmQmYqP5611rv0u0NhCibcBPcAe-X4QtpS9xCdDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=IjOVYO44CuFbsrw8QsibI1bEg1yLuTvLY7Ua1-bz1JUojG7rONxADKBUXoAdcmMiuA5YJ_mmKk8cwYnOaewb7hmyhYf58zpK8mesGFFdeos91OPjcBommyAHahhJHZhZdKzeaUumv2YGHUVPP94eu-Q77_Z3VU22RhaOSuFyqRIGET-9puXTlhxaBVBLu1-I5D5A9XiLQuFKOxaJdPku3FLMrlQDNn2SsmsKCsfenxD6XlI2sjFFUNPORtmAVvwsiOheNWoie-N0Oscb2ArZJZXI6hF04mO54N6w2XvCGRSaec4xmQmYqP5611rv0u0NhCibcBPcAe-X4QtpS9xCdDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=sZpGJ4ZEVxmAF3uyEZKf4EgAr2zl-P3hukwZEAYND-t-Mgk61VVa3plyvVKIHB2vuw9Y_kjODLpsTG8GR9dMK8VaOhkrDyUox6rExMSR2yVoPeccVQyLv6CBS8O8tA6jRsWISjwjQLt8FEocAJNXfkeZQkF6aOc-fQGPMKT_pidG8wZjsWOZthmeeDThQN_hrlKUCbieOWKaNdxkS57ITHVeZM0KZd92uz7Pt3NOYUEAOfHDEsFnfuPQ1aoFnJXQBDYos30EbGkzw-GgRpj05qkirUNco6RRxDFaZftAh-A9ZIiKUQhww9g9S9o_GWj41bCG_uA64kpn7GXflx5GrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=sZpGJ4ZEVxmAF3uyEZKf4EgAr2zl-P3hukwZEAYND-t-Mgk61VVa3plyvVKIHB2vuw9Y_kjODLpsTG8GR9dMK8VaOhkrDyUox6rExMSR2yVoPeccVQyLv6CBS8O8tA6jRsWISjwjQLt8FEocAJNXfkeZQkF6aOc-fQGPMKT_pidG8wZjsWOZthmeeDThQN_hrlKUCbieOWKaNdxkS57ITHVeZM0KZd92uz7Pt3NOYUEAOfHDEsFnfuPQ1aoFnJXQBDYos30EbGkzw-GgRpj05qkirUNco6RRxDFaZftAh-A9ZIiKUQhww9g9S9o_GWj41bCG_uA64kpn7GXflx5GrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UULMsvSex8JxPNQ2r5pe9_6J7R-Sj-Shbzzr3Ifu1jNs11Dy6fCh_JnuJJBdLVs4x9fLSvK6PapPDLSor9UQtrHosCZdJinydfibpx4iEqvc2R76XIRzlH2qXugM7cIIXXhMQz2c5qjYD-lKoka1MU5I7KSt4cWj8bFb4Ade_eHfRPi3FlF8okULNDdmiF59X1Qi1iwQo6SqP8jciKLT4g_wMQxmiyYMSwiIKj7wwIFzWdhMsBScU8gF3d7HQ1W4EWcrkp6g0w1ng8MaAGtMnmNl1JnZIWeR6bVa2aQYGBURmGvUlBwqx0-tT3aqQsGdd81Bauq4c0Sb6PggQ91dUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1aSTX7qMNA2VOKS8wGz5lQpWAnK0JYGQmu-_Zn2Fkynygi24Y1yC7stIEXkBPl1BCZV9yFdBieQkHoAFBx5ivFqAZNAYEDe59iPp8gyl496k0H6axN8eUwRPrPiMN3LiPpUOBNcZHf-XRTvx0TJqcMA9b7qjiOqvMaYHUz0XNUZ-XjoodtYj5dxZhNLs5ExEa9Nh0HsXko8QkWaqOOgWAvkASIHvuEZXr6xLfpv-X2Vryl83vL8mj_ljPnwRNDFNJ1ksIawfMJr64yb6fxxj7MNe2o4uuy7b94aG1byii3JYS-xfP8n4cd22BLy7nCkVI1qQy1Cfv863abM1RP4tw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Y2HlkVmUKpfT959oqQ86Iak03iAM8vfQ9PyVc0VZJRepLg8KKGbaYv2Z2lB_VCH9dcDuUHh38ASIhfgVtXSlIGlR_guzzYDX0IcYNhidThSYIeYRalSzXsOSbhHIaE8KfKX2-RrrQqW5YAxeFY9u5CNm0865ZDZ4WoYRnuLB4-rmNew_LxDabG8sPTP8HZuW8410d8JqhYB9vm14T6v51Q52u6OwASXlkeLmxq7Lc9uhuM9577Saxb_tF8SNPFgueOqc4UcjkTlxbFFHBVpS_laYzEX3P6_D5YKSxx9jSjeueKQesTPZRd7djtF9udgcobwuLdlkU8RcYEE-IpSGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Y2HlkVmUKpfT959oqQ86Iak03iAM8vfQ9PyVc0VZJRepLg8KKGbaYv2Z2lB_VCH9dcDuUHh38ASIhfgVtXSlIGlR_guzzYDX0IcYNhidThSYIeYRalSzXsOSbhHIaE8KfKX2-RrrQqW5YAxeFY9u5CNm0865ZDZ4WoYRnuLB4-rmNew_LxDabG8sPTP8HZuW8410d8JqhYB9vm14T6v51Q52u6OwASXlkeLmxq7Lc9uhuM9577Saxb_tF8SNPFgueOqc4UcjkTlxbFFHBVpS_laYzEX3P6_D5YKSxx9jSjeueKQesTPZRd7djtF9udgcobwuLdlkU8RcYEE-IpSGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7UuW53f0ZRFV6jW94jQ9T0Akonjd3iKWm1x3NZ32dQIXtGjMVl3EKf_sUVAlGCbCsnlqXZw7eIDHvCXDL1afgUQhDptg_HbUCXqwWnx7r9ml-6A5JDAAxWZ_2rbs11A_KJuVpo2kuNpXRHvB9wiyTQfC_7mul2JX-jfoRq2otUp1y0A32ljl7clkRrxWTthK_UX_KyfVtwOmA9DBfruS7m26xyJ3ZPSQQqiOZNUdUMB5QOdB7DN1tngWx1n2d7eQYNLhQPSlObd9SybvAvMhuN-rb9t7zOLOX1Dskun1uH6VSIFkkeweQncSCPEpacEIgJje21GHaOqHQG42CDsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYwFcPSF5YpUs7xmcv8sa_McXbhUdeTEkAmDyBQeZxgaBqoE_hFDBEAP7zX4SLT5q4mOGZC3re5te1ToV8fnI08KxliZ4jrBwUXr2AoS6n2LRSDE3yJN8DvfVEfTbtxx8fU9cHYJvhKcyqcOIZ18OL_MtNtdOoblYreNn6Ru8qliViqqYIvwjPTxfmjEFzHFo0e_8a6JsX1QcjwBWx1YU5-1SqQZWLCN0Lv7h_1ocAZB4yH7W1e16oVbU1rVFHrFv2xnsb00lzzAyC77naQaIQaRBjggz0Rmq7zzD08avF9BLKiozuF1RSvr8SEF3YVkYIEMQ6pZCU4IrPW_dudesQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPqU4JWgQe9jE6tChagye0gK_LL5vXnmu06-5R2vkfUgOxj4UxAetO1V14NlI8AW3ht96Osb5BA7BBLrdZMe2SBNjrHfihsvBVIjUmRB_pn8kJXTqKGY0_pLNUBd3mNNdclZixt67oKFtOu9ys4pFC1WWZKQZZh84iC4nlbKVAPmS6aeNG99az2EhQM-SmaHa6K1QEr-dUr2eu6JUrZ1Rumb3PgBhVVLgk-PoFCh_Owo5Y3HD5Z7Vpb3rL_pBxsY0tOErjJzKzj91-blHaeB1fWkmmHNf8rzozsd-QSsCBX9zUupx2ITZM1TS92rEwXwj16xPW96j-6H_qiyeKzyQg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ppMCbSsfrFWh7TeaP0wmkK7cBarewxYPBp5wWQH_7yhI-HQTlcSYGjaw_WGrrH2KX0pPVBv-9THhqaXh7TrUAp2d1tiGRoh7vtTtOthyzmQViiM8OQfIXdo_loGhgC3UQbCotwVDqaRlmG7kxTnUvnoAsLrepcwocX_4dv8tyyIRDIAAyPbaV2NR81m0N791Mw9r0kV1xGqcoqqgpILrElgistsjHzyNRoLunC2CbaLks5s_elqUAru3xdJgtgR9UE4dui1LOjlLRA-C_ozEAjPb7juM_PQz9MbuIr1xXdB0je8mJFlw1x6yDsiPvnC82aP5bl6dYeCBL5sSx0oUsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ppMCbSsfrFWh7TeaP0wmkK7cBarewxYPBp5wWQH_7yhI-HQTlcSYGjaw_WGrrH2KX0pPVBv-9THhqaXh7TrUAp2d1tiGRoh7vtTtOthyzmQViiM8OQfIXdo_loGhgC3UQbCotwVDqaRlmG7kxTnUvnoAsLrepcwocX_4dv8tyyIRDIAAyPbaV2NR81m0N791Mw9r0kV1xGqcoqqgpILrElgistsjHzyNRoLunC2CbaLks5s_elqUAru3xdJgtgR9UE4dui1LOjlLRA-C_ozEAjPb7juM_PQz9MbuIr1xXdB0je8mJFlw1x6yDsiPvnC82aP5bl6dYeCBL5sSx0oUsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=duSh7_I6K1kc7rEgMsEzUrXmVukhGGmSCEEBCdjl3uIAPVfJQ83kLVZ_ESnfYjGB58mEnxvp4rS1HkSA39axyhbYZXB2uOuLZyGmLMZUBIcHvSu8P82nKAxXx_6-upvPlVuZ9GNF6OBOqXHutqRAxF8Rc805dRb8kvISizd9QwVdiBqknYMLz9tNQ80l0NOXraCRQgtFtBJ1tQ2YQ_KudywUluTdaEFS9TuinDAVdrORlEN8QJiXwnvvPUI6jTUdy5ykGq4ln3o341f0VRK7BCFeNcEfBeGqST6tDxK8jcK9VVYzwKc-MKgxb7gZbGclcqvrC3E-3r94_0-8TKweXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=duSh7_I6K1kc7rEgMsEzUrXmVukhGGmSCEEBCdjl3uIAPVfJQ83kLVZ_ESnfYjGB58mEnxvp4rS1HkSA39axyhbYZXB2uOuLZyGmLMZUBIcHvSu8P82nKAxXx_6-upvPlVuZ9GNF6OBOqXHutqRAxF8Rc805dRb8kvISizd9QwVdiBqknYMLz9tNQ80l0NOXraCRQgtFtBJ1tQ2YQ_KudywUluTdaEFS9TuinDAVdrORlEN8QJiXwnvvPUI6jTUdy5ykGq4ln3o341f0VRK7BCFeNcEfBeGqST6tDxK8jcK9VVYzwKc-MKgxb7gZbGclcqvrC3E-3r94_0-8TKweXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Go8uHI_JVSswGhgr587Ej2t5bwpubJ1LnSn8FvFBoCa0ReoVBQx-kew1DQpW43bSQuwOi2uWoymrM7j_OvjSjMPWQOjfCPrS4n8NRbWU7L2BwcWqHe4SvI4Ckc6m-YuSeyJmpe751kdy58KzjSz0aM4EC4L_nfM2y5S_uXPFHKdEBuf4DCcUH6UCF7UnzQKkKiJ9JwVOw01uhTSORAvM-HyjntSdTuY4GEGF6DeLxsbAGLqG8ufEQ7imTkAOf3VmVihj5UJ9H3Ol7aFjjCOKi5l17MTm1CIzQyWhWQ1pKB_1kXs84UvqaA6mj_Z6x_k0tZC-m1RvtyCanyJ6DnUu8iRpPB9IbeHWDbTpqCjL8KrYJeLNXkZM4sObWtE2j5zGfLHCFPrNtjpeDLFPZ6XWlBljAMJ9ryzrKzcsnwwu8pmMyofQuqQ8XXepdGus5mORuwd3r2r6-0yRBjq8C9kAlCfKSfkmCLs0J4DdYEu2RcjvgLhvw8P_I2dOFIjpq3wJ_hMDS7sayun0jsu3ELynGm3-RIq_YJZ3pUJQvhRoUa6uIoDSAkiAp-UCNu7HqpNznwL0GZldV_ZUXUIHO4aMbRK18cWgCrsO8c8dyoxvd20xv3tcdRtK-po-xSy8AsWcWprvkaNewFnw1bjynhUdBwFKcTWL8_ylYhnpNXYc5DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Go8uHI_JVSswGhgr587Ej2t5bwpubJ1LnSn8FvFBoCa0ReoVBQx-kew1DQpW43bSQuwOi2uWoymrM7j_OvjSjMPWQOjfCPrS4n8NRbWU7L2BwcWqHe4SvI4Ckc6m-YuSeyJmpe751kdy58KzjSz0aM4EC4L_nfM2y5S_uXPFHKdEBuf4DCcUH6UCF7UnzQKkKiJ9JwVOw01uhTSORAvM-HyjntSdTuY4GEGF6DeLxsbAGLqG8ufEQ7imTkAOf3VmVihj5UJ9H3Ol7aFjjCOKi5l17MTm1CIzQyWhWQ1pKB_1kXs84UvqaA6mj_Z6x_k0tZC-m1RvtyCanyJ6DnUu8iRpPB9IbeHWDbTpqCjL8KrYJeLNXkZM4sObWtE2j5zGfLHCFPrNtjpeDLFPZ6XWlBljAMJ9ryzrKzcsnwwu8pmMyofQuqQ8XXepdGus5mORuwd3r2r6-0yRBjq8C9kAlCfKSfkmCLs0J4DdYEu2RcjvgLhvw8P_I2dOFIjpq3wJ_hMDS7sayun0jsu3ELynGm3-RIq_YJZ3pUJQvhRoUa6uIoDSAkiAp-UCNu7HqpNznwL0GZldV_ZUXUIHO4aMbRK18cWgCrsO8c8dyoxvd20xv3tcdRtK-po-xSy8AsWcWprvkaNewFnw1bjynhUdBwFKcTWL8_ylYhnpNXYc5DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=KMQhRJBy-0ihKwAPldonuO2olrNekr-H0es9ovibNCi1y300kHzAze21bDVkwL0LxKhJ_PYuqVieMfSsRKv43KwySp010IwgVbJdgvkZ46QZs47SzXyecr9y184sH5AURE7CszepBlbwvmoUnJDHal8tYS6HN9anP8W2x_fhxhIcutDBgSlClfa8gM5C_oGowoCcUVUlNKwhCu38QIfp4sLioscppQTd9YZ7CK0nEsleRDcSfAwNEm7yXe03j0FJ4BfSIQas29mN9CS6q40o1kbyOfaTfVkj2jX8LeL-BjjtpGQSAaSr5Tu4fqFeuiHCvsGydct_rtA2-hW0hbbH_I-e4iGUsLdJMgS4uZw6sT_VUEpfbPpHOn_KA3Q58GpKJJo5eGmJbNf84IxBdUoCBK-e1Qs-IgI4WFVWtMPMEZs4xMAPLI7eaPjOl6BFYRdJPrPdq5JiCvJzKBILu3vwEYxbWinWFChz1X2O3qgHfQC5_zQoZbAaVNm7BwO0tbcY7xg9x7Oronu_chKqQwkMAnFVak8pEIBlh7V_HiGceknbRrZysWwYpBCEdmZkNMlxwDvCytC2bl0RgFZ_A2u8OBGeRqzI0QXGayfyL5QSxh6JVLL69CsMfiND64i7VPeQDAsjmEP31WWJYjc6gqy_piugrfudLUuCtjjBWPUUpyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=KMQhRJBy-0ihKwAPldonuO2olrNekr-H0es9ovibNCi1y300kHzAze21bDVkwL0LxKhJ_PYuqVieMfSsRKv43KwySp010IwgVbJdgvkZ46QZs47SzXyecr9y184sH5AURE7CszepBlbwvmoUnJDHal8tYS6HN9anP8W2x_fhxhIcutDBgSlClfa8gM5C_oGowoCcUVUlNKwhCu38QIfp4sLioscppQTd9YZ7CK0nEsleRDcSfAwNEm7yXe03j0FJ4BfSIQas29mN9CS6q40o1kbyOfaTfVkj2jX8LeL-BjjtpGQSAaSr5Tu4fqFeuiHCvsGydct_rtA2-hW0hbbH_I-e4iGUsLdJMgS4uZw6sT_VUEpfbPpHOn_KA3Q58GpKJJo5eGmJbNf84IxBdUoCBK-e1Qs-IgI4WFVWtMPMEZs4xMAPLI7eaPjOl6BFYRdJPrPdq5JiCvJzKBILu3vwEYxbWinWFChz1X2O3qgHfQC5_zQoZbAaVNm7BwO0tbcY7xg9x7Oronu_chKqQwkMAnFVak8pEIBlh7V_HiGceknbRrZysWwYpBCEdmZkNMlxwDvCytC2bl0RgFZ_A2u8OBGeRqzI0QXGayfyL5QSxh6JVLL69CsMfiND64i7VPeQDAsjmEP31WWJYjc6gqy_piugrfudLUuCtjjBWPUUpyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=lu3gUvM1ZOk-JnAMrZotBnxJG4-HRtxsq-ECD1KTn0KxL0K5Bu1FzCKJFwiZbewDNdCJITe18UJzhIx7MJXuYxfM8eW78daOfcM9mxdgqA8t-6I6hWYFtvDqCKDRV_UlTU-ORthZGGOLg0wiQfG9WCYZ5eZFmV-H1am7MDsDPCvwPdkaZ2vYhc9FCcHdkIvnnVrSIhj860nhp43CJATYLDAUKSUf1o6KwVnY6e6V-Vveug7ianiu1G1jvbSlbd9T379QODG_wA8sWkT0fhop8gsu9G5AViGy0d-2y892--ncDWQ7cCKeAI0rc0cp0pW6SpGFryIEO0nMsy4sf_BKNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=lu3gUvM1ZOk-JnAMrZotBnxJG4-HRtxsq-ECD1KTn0KxL0K5Bu1FzCKJFwiZbewDNdCJITe18UJzhIx7MJXuYxfM8eW78daOfcM9mxdgqA8t-6I6hWYFtvDqCKDRV_UlTU-ORthZGGOLg0wiQfG9WCYZ5eZFmV-H1am7MDsDPCvwPdkaZ2vYhc9FCcHdkIvnnVrSIhj860nhp43CJATYLDAUKSUf1o6KwVnY6e6V-Vveug7ianiu1G1jvbSlbd9T379QODG_wA8sWkT0fhop8gsu9G5AViGy0d-2y892--ncDWQ7cCKeAI0rc0cp0pW6SpGFryIEO0nMsy4sf_BKNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgl_J0lVebOcFDukglBEDDNmuyzuNDlV1iPTl53flLU3dICizNXhY0vNSv0028t1loG1W0jIJ0053OnskTTzgvrgxC4dZN4xzmIRtIRCg10g9uvhjilUr39cvfevF4EcoVfxiDqGzuaIcrAE_iZcEheDUvKZzn8aigJci0uMVhgMp3NGpXXfCvQZGaDi14KQOXjezP29RsiP6bMrLvfzzPUlpP1mi_ISXDh9bcP57PCyaq3V_e1M2Xy4ggGwCI_kfXWbhkUzKgy4FUDC6KvsHOpjv4rsnQVS_4p1XXjYtgMPo9eWy_S8-4pvtMR6IpbcxQHfni16UNShWfHVwRZc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=X13thv8UCkAUONTHm16bgCICIfmvW1DIoFy7A9vFWP4ir3AqCbMkGTv3OJCoIHw38OlFu4uWr7hp3B8OepyCM0plr0085L-Dgb__n-VS5_8lD3PLTGHbNfo-Y9HZ0jZfWf2sh7PtZwLeccU43WW51qkmL_vbo4X7Z1C0ikrOZh1TMv2DybLvx2gqgJURT_Rnlq2b3M4dGHRSi6Bj1-chZhI0tcXg0QQY8QHZeSjGpepZRCEcqjZyJ-WOS8L3bSwDK76xxJkY8Lg0V7ksYLQszwqD7SUO8Xpaah3aa5BByD0Im1jFnekRtRWBz5HP63P5FqOo4n0hVjT5dvGiReXnhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=X13thv8UCkAUONTHm16bgCICIfmvW1DIoFy7A9vFWP4ir3AqCbMkGTv3OJCoIHw38OlFu4uWr7hp3B8OepyCM0plr0085L-Dgb__n-VS5_8lD3PLTGHbNfo-Y9HZ0jZfWf2sh7PtZwLeccU43WW51qkmL_vbo4X7Z1C0ikrOZh1TMv2DybLvx2gqgJURT_Rnlq2b3M4dGHRSi6Bj1-chZhI0tcXg0QQY8QHZeSjGpepZRCEcqjZyJ-WOS8L3bSwDK76xxJkY8Lg0V7ksYLQszwqD7SUO8Xpaah3aa5BByD0Im1jFnekRtRWBz5HP63P5FqOo4n0hVjT5dvGiReXnhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=k9K9mbzassspuUzwd-XnJag9TaU9jmHAAaoQBKUix0ltllThjxtDp8e0U6R9yRScWokH6lbjERXAlROfe0aadQPmkTNKpg7375DyUjizWqan0CoBbOia1y4eqAtPmkLcUlI0iJL0DjsV8BJjkNeFfugo6VtlLei0LIYPyJ-eBiZnPz1IxWHlqljXHIp1cv41qP2lX6rIxq5yOKP_DWjYyoU1hwJQKKMYjOI1RjPHsQevM0xyuLJbeALtvYqbKg8BC7Uea8O4chFYBNshEnjnMChy0SkTTqQiZoyUcPD_qDk8TygMq6I7zxLWo9J5qOV_eX9cYn71M7D-dYctF6re2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=k9K9mbzassspuUzwd-XnJag9TaU9jmHAAaoQBKUix0ltllThjxtDp8e0U6R9yRScWokH6lbjERXAlROfe0aadQPmkTNKpg7375DyUjizWqan0CoBbOia1y4eqAtPmkLcUlI0iJL0DjsV8BJjkNeFfugo6VtlLei0LIYPyJ-eBiZnPz1IxWHlqljXHIp1cv41qP2lX6rIxq5yOKP_DWjYyoU1hwJQKKMYjOI1RjPHsQevM0xyuLJbeALtvYqbKg8BC7Uea8O4chFYBNshEnjnMChy0SkTTqQiZoyUcPD_qDk8TygMq6I7zxLWo9J5qOV_eX9cYn71M7D-dYctF6re2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSQPM8Yc2W-MsdrAVE76tmixz4e1k7PZzO8BBEGn1oiWGxZ8lNmZ2eCdQhKw91plW4h4_xDZCPjOaNv18dItlDw-esRlMYHQrQHXP-lCI5hJEvqCxUcIWxhWx77JaodIQA1z10ABg040rRpO65jVpYMALQ5JuUE9-sQNsNJkT3yv2JWweLUbn6amdyMzCfoNfdYme5YZtZsNkZhKFhadF3r2PwaoLzRT6v0Fp_Sp8Cc0pgDISH1jD5_Kn-9_ci0iesrGUMHwkCNblbFsxESiIr3WNEUx1MQksVXba_g9TFqc8_NjJerh1iyoDEGn8D6GHZomZVGTJKLEbF4YB1HIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW0VGs4Nq-9hSTk_u6lZAFRdZ10Bd1Uq3QtTiI3nZWBTt2EUwHe6X00rl8kuHNE1zBgZDE6O9z_kJf2tGpKNudTxO8DFYakyn4t0LXc4r8SBGA9wLK2Gn_KrcXhtNUn1ScDInopuWRw8qSfcpJe1JAFCzr0kBb_xhpdnQ6xGOmmFW7QauJSFStOvuaWpp38_JMGMr2a-S_H-3z4OagGCjY6D4TQIBwHlS0Qbg3ki1q7NvmodjbMBQ4r1aGQ-mw1BW_M0KF_alu0dBToPeDREtb0LAwyj8h3i6BZOZmwZV509J8y9JO-JQkyusUATJa5M6FqSGkkS3lOv4qCiFVIt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFUsDhImeOwKk1QhspeDTZHOXFSFP3cW-vq1SXX3DvPNB5kABCXcEzIo082JmkgI5OXgF4VxTkv5TLHbkU5zxSY9sQGl08GCymbHs1YroR3zJyeqfpxEfE2VQqNujjZZE5PqH2CAZD1oHc26vexYyZ9RYwaVZttql5SLxPbNgw-fwtz04MzrPnlAjULC0Lh1vUHGmP4S4MjP-Zb_oOmo1ad9YxTvz0vu3ay3tt_FjwW2HHbat5QdcdZiXgvB0XBYjrv8vZ8uFdWzlMPe-uqgKH2mZyAgkFvXycvooqGJPTekP07h3ciCsOYDKE7QwyjaePZVRJxUif8WZVLYsx8WrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvOd9aUCWPi3NdyKr7a-oX3UavsEFBe4F9A_A1xApFKSi1Txi8LrZgbrurXHCERcOsnVDDFZ2IidJGZTdwlrTKXkMyb7OrZV6-swkKnsuIR2HWug2Cj9mNEev9dgK6MeiVV2nJirtUHlEV-83-6dppPgpRFnDy2YmwBgcYJzbWniyXqgvIPpGRp32xEwfz2mCZtQjxyE130fbHBWwOCqI1E6kyC4TBKCgmG8Ud62ktCirmbXGT0BcABP6GXZWq7TwQLqKbDZOQW5qup0GV8jLmaXjP1GpPVzJLBkiE8srxuq43b7ksrr59Ex_TFWe1FfKYAzfwicl3HBkiDAltdUgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hoi4KF5H0dn0DZz6ePLouc65mnUlR7IVs17aPD18E7Em_88VnUKFdi-GsXGPr0C8JJkRaSs8qQRqoqwsryRP8U6pr_QPuM13kthm8FxzMZDjDQIp-f2xbfUvb1pZ5JvMUpOsiHXD5i5q-VdWxAKbZIhDFD4N55hlXbz6X-V26hvxjEn7HbCn0iJPlumvTuTHN1ibiwh0RfkWWXCkyblBhBqW5ROZ1O6FPTkde06ueWznArFgYWoohG_NrA33Gqg-Gbyn-QeBL2cAtEPsmOcdT9Kj2odpliVLAPrrdDRYqE0IbsCYichcg6rZXm0OM5l4kpOYacFyKB633X1iYQnPtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_Z98_rAUDwCGM9uAxWe6qphHvJj38MHfplnmlO7OTsWqRXI7nSWlcLA3UnZcqbfxnW1YKNrftGn_-2wuS2k0s3QKEL-XrLhCYkk-kGOWKSERNgL2kZjwe3j8bTHA-4mKQfS-GOWftkAIRH_irQgEi5f53obcV3D3JnUaCt7chgsd6wyppe3sIYxlrP-_lvu0c2X_W2hwGYbw8fglK0Y2yiEZ6nyEcib43dw5PjMh7brC2GdU1_CPJr5VEwtJ7-FrMt4gLNNmQwYK-FTSJT4m_ZBBYqh3-rF60h0dDFXTdr_1XnD-yPeWamDz88AVfbilqg2KaYmPU_PtIytgbdngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T57872GCXtgSc5azuw-8fwSDGBOgQQq4bxJ1R2QH2ra_FuldmaOM8BDzeAu2T1797N57-1hbO-J7A1b0L3SZU7Z1liyhEJCLTQ3sfRTXv2zMmJk9wK9rsIGWVhxyfI6O4msXu_MG8n3XSiz9ml71kshqV1Rq69aW62KACw9Kslmkm4pnAPrsF6SP9_jp4xhRx5Yye5OW8h4Fr-rhRZFLtaa60VtdgfAgZ4w_jS5ApRl4GPkHB0YRyBUsNCAsB3vJopogtNPjcz4yA0z0p62pzQ-3YOTwqbNNHdcArp0NZawHl3OVPItC9S75JseoyJf2pBmR68m0kagIvn1xb4jAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmvCpGCpmsbUg17scRPzUgR6hyJ0R9Kqtk8J6F5QpHexKtwJuZxgslsbFs3dUxGnKK7n-sIH9zCK-1KaNNZzsubKej6vcMIOtzf9lxQ8xGiIJVdViGaZRWk2i88lcZxxsxDjnVYSpvgs5gwtwkfraJfhS5KIzgueudNiict3E_pMhgKPR7yTIWZMxNa34G9t8Wq8-SNeNOMFqDJ4584NdgmGAYqld_NWVI4q9O_ajtWiF_m7pB3cse7mbVG7FNja-JIcvAaUHJYs8iSPXs4zOHdAbbSkvIjx4BPUvM0EJkBm9bHJjskVvRPgHBeJOQAUnNFhPuvGMCTxcwbYq2_nNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UivOZLrhd-ellAYn7cY8LLj5pSzCc3CsIjsUhuoKpFhqjdGfaiyGZzOjGvHwu-ZNVEoL6_mNgy4QuhXaQTlEVspg9um25AYrNI2B6MM5vFwmmZMfXOxdrCnXD_05d1CEkPN8JSHvqWgAcFqKMbaTNzSs1o4q-VoVdl82jKnSMgAflG8KjBqfFNm75JJHYbgRURFkXaDcUfIO3GhNylTKpLHv6u_-tV-PQ2NQw98p1hRnK449inTpG57FzLosg6JyWtoBPHGygh9ref662HoeeYNIfpGKqXn8sSBPDbAJ79JJoaRpvIJE258Sut83s3frNPQwwHINyxyL2rIa-QrGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_3zPi1nu1Lubgb8MjtZHlxRlmqEQozMEtmyg-p05lWc73V_dLZgo9Wa3IswCVBn0OUokGoL-zJOEdDEgwp9p9K5YA-dc8BdEX-Xj67bDJ4eg5S3vcifaVclubUrYKKIzI1k-0znleN_mcsJ7EoxeDGqn9JEJ_0t-5-AuuJpUXINPIvf58DkKdg9TyLUxTFc8N22css5AQQ7XpsNsvK7zFhH7iaa8JvziV_KWoJtKmUYmPgTi_X8kAaLcW6IrTHRnPIVKtMTwoGGxV85RVwVmu34Apjy0BkRMWjBUNS2ur2fPPb6ddWfi3og1xfs9VFans_oNaBKN0WB7cgQgtQKsg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=t4iG9f4dY6xyVnKFeWD3zE5bxPaLX9jeEW6B_iZONSQ7YKh9c1kKOpp6L85eoUktpMBeEEqo9kglqdtCni9Rob1O8h8IdyiYEBQOi3RkRCnM3Lhp4GLvwFw5N_zJH3ye5kepud5RFI31wHrkahMcB0Re4BY__pX4QWyvwf8ZVnkED3O7Q5hbou8XhNbwC9KZQ8r5ST9CKn9NQPIKfb-4E9rhxjZyQi8FYm5-egBVqQvkUsoHHgZ0-yKH0gOa4p7Vjal9c-cSViKvNDgD2jKSTur6Ei_rLXyqdB5avpvnuallCCFZyVtFC2wjQYhizkvUg9UZmozjOk8zapJj2ddCmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=t4iG9f4dY6xyVnKFeWD3zE5bxPaLX9jeEW6B_iZONSQ7YKh9c1kKOpp6L85eoUktpMBeEEqo9kglqdtCni9Rob1O8h8IdyiYEBQOi3RkRCnM3Lhp4GLvwFw5N_zJH3ye5kepud5RFI31wHrkahMcB0Re4BY__pX4QWyvwf8ZVnkED3O7Q5hbou8XhNbwC9KZQ8r5ST9CKn9NQPIKfb-4E9rhxjZyQi8FYm5-egBVqQvkUsoHHgZ0-yKH0gOa4p7Vjal9c-cSViKvNDgD2jKSTur6Ei_rLXyqdB5avpvnuallCCFZyVtFC2wjQYhizkvUg9UZmozjOk8zapJj2ddCmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
