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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugMyO6z0lFTERuz4j0r0smhdQ6Nqz1aSLVsO6wOfL8WSRkgvmH3L7QRNHgjOaSSrVnIl-4sYqyWzu-HnbM5xKKP8p2SkvKQntaX_uJfAZ_lQirF4vnBeH7ztcvQihjrq6qGWXi3V1hrZudH4jZKGls7E2X6z6oqXCy9ObMdq1fLC746_OQb2Wf1QN_UCgY9c6rX833w8qWIkaCDaRRVtbAQTsT6yR2MgmBfmgaOQ48r9rPq1kzlDga85XJeh6dYzJHrNTe_uWfo026n9SqbVSoI3iIqUu_sKjsyzDjjoBtkrBITdHHOoZv6oUhehdJoApHVTtGYraYAW3qAxkrB6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMkz5sX9PTeEjCiNSA9jacT4khR_vwGc8ITb05O1NmZh7rhkjkJHvoNoQryB6BrhMxengYInqgRdd6XFKuN3PogMiLgwKplKWfOZqxQ1M99jWwWHVAk5vJ4221314fnfK8rUOkUg-X5oFtQvLP5uEtV5wgiKp6CkTeCfcbDgiXqwiByVjiS9RORqam2zua0MFQf-F3COKUyGNBN_x8ocr44B-Ln82InY1EmxRwrOM72am1Ef_x0v--j0XYfKg76Ljkb0X3FU73SSkiWRRcN9cTh2JxbcJw99Kspd0LEY4scLajweA6VgAPnV34ThUryrsMZ3kTR45WlZVxRUldKDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1i8nL2018cOSIgcnX6Kq35ow18aHD2JE-6y1OEmJG1JIxqYIWNhu-I_lTo23eQD7ous07OyYNxdbYqAKRWw0ilubNYN9tbU_Xjj9PfFMuSgQNdNHrArPD26b6yD_UpGn2o6zDTY8cbA-rgA1rOQs754QIDu6VvvTBPI0t7-BnbegYSyIwS5Uc3-BQwF0QAr3A1js0ZZoXVpqfd1hCRd3z67qsNajpPATRVj6BnAIUO8ImlSLd_GQybuTxel3bYPFDsgtzNfcYsaaas3LFA8EreZ26mmC3gjTQwIYzLe74_F7qua_bECvL9c1qh_kwutJBferEDzdfKR_fhwK19Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq4v68gu8qZgxyv0x79koN9sXy2NfJgr4zlAPbJoX6sqmqELWbjEQTrbvomHOnxNkcWSuj4Y4tmBXh6xWHmv2-c4UUln_v5nqIwWQ5t-kLuK2HRLPJarh7TO-HWwseVqrFf8qRFH0MYhJ_eeOtKNMZaxnPlvXSWOICRGJG6AQlCxP3cYAWO8Vc2u-mCs_q2i0C51UfNBfmdQL1FBOAT1OCqHUNqj6RQI6wpzZcp-4LYvHpkr_iMaIICbQOuYB2MJ2qcoYHXnRekwaT5Xx9MPUIHzsrS5EMJhyJENDX7YT50y31aHd2LpgYoc6WVj3ft7HTw7hRHklbhC26RpRSIS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOiWX3LizRZsJLS1nKiqK-wq7UAaGVxGexcz1IVt3EUkWWW3Ajhj9BnuwAgXpxTEcYf0ptWSWoYQEDaZgMHYDibQlymuosLE1G9OklXAsLniSXpChG1DrkTHRVJWu55LCgDevrKhZ_qJy5S9UCXTzdgld4f-Z-zm1qfx02gRZHfKQlmnLSzZkX4iJDUqn7ifofK0EKPfqC36xdA_QV8KpHQyKb5OpCCWYh3e7VL7N_114NC7wM5PxyVV0CgLQi3OjYWFPNlTNg3Iwr9dn31oj6KnQCYywpRF6U6Bb-Ma3TW8jYCXkKb0biLAdMarTEPft-bxws0MN4hqWZeHP9Uj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=KwgNNcQ1psnZ57DQ-A1MHPGyNU6JbTKCzL-Yagc-H6WCWZkEedPLuc4k9VkH-FeV3JWDGVoNISZNed5rZUnMUQrkduVCL7QpnM1ClUc6jURUYD3MO5qpSPHZh2ILjGznMghKJ6aczJ4QzlyKLBllbgTYfyFMEqGp-7rauC-mLOoPVovlv5PIfLSlVjwauZpWOJwxBP3oJXKZ6Wy7opf8ROEYknxvvvuzy2B2buwtHw9bCsYk36QLH7EbfZ98fxFCvZb2NO_jDWKzbLyBHL8BDrA1uAgO8_y8XvLVbzV4O2N2LQ8hu8ACQs67Ge0B28sFyI9idGdL7QLPMS7a_vpNNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=KwgNNcQ1psnZ57DQ-A1MHPGyNU6JbTKCzL-Yagc-H6WCWZkEedPLuc4k9VkH-FeV3JWDGVoNISZNed5rZUnMUQrkduVCL7QpnM1ClUc6jURUYD3MO5qpSPHZh2ILjGznMghKJ6aczJ4QzlyKLBllbgTYfyFMEqGp-7rauC-mLOoPVovlv5PIfLSlVjwauZpWOJwxBP3oJXKZ6Wy7opf8ROEYknxvvvuzy2B2buwtHw9bCsYk36QLH7EbfZ98fxFCvZb2NO_jDWKzbLyBHL8BDrA1uAgO8_y8XvLVbzV4O2N2LQ8hu8ACQs67Ge0B28sFyI9idGdL7QLPMS7a_vpNNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEON28MYMWQAJldZ1J7LUiKwqsagDMw9rdx8Nql5qb947Xzl-_NIFD_JRgTjuw1NVyaM2_wZO12t9t-kAR17kgaXURGM-WjVpPjp4H6pB5EHwQwaBYz5NPOBG-m7Y_n8GedGuhsbvD1d44f87jzyC7i8TfgxNQ-Ns0bUyStGnQq0fbm60CUq2_vlIecRukpk3u49tkAvTJrO-NSU_keI5VQkqAclDhm8GGd04rZ0PenZbnFX6DCePfZvA1OfMvvoSV5q7zxFnK2rpAVTUGBNIlCgruTH2t4RI_kZL3uC3VLXmuiM04sRgLh6Mxna0bvUQMIkW3rxayxLtXy4rx6RkQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro1qyuTgsV4KK8Z4E0EgFm5BcAKZBGoM0bp_Q43YuRuECSc8THKixemSE_T97z6L45QFRdYQheaQyHQ5x1SaYcfChmcDTETR23_M__PLBnvEtVcY5AmtcLJOwvMQ7CWU93aM7Sm91dV4Ei6yDVtVgWBN6ywk0KuubEOsnMdOyDJ62npNHlGHZ8J2ddpmQxazr5yiGbiDvO3qiMVhbIgVdmCV97y7-rK4EcDjCg-24mNDGrWI-MWz2Zgz0Q-iSqy6hqbJqS53kdtFq5Jp4rDExh7DmVg9OdOGCwxGgGQCzdJHLKkawLOjWI4moVdhqi962i4oj3fHKHRWNF78ZYl4D2ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro1qyuTgsV4KK8Z4E0EgFm5BcAKZBGoM0bp_Q43YuRuECSc8THKixemSE_T97z6L45QFRdYQheaQyHQ5x1SaYcfChmcDTETR23_M__PLBnvEtVcY5AmtcLJOwvMQ7CWU93aM7Sm91dV4Ei6yDVtVgWBN6ywk0KuubEOsnMdOyDJ62npNHlGHZ8J2ddpmQxazr5yiGbiDvO3qiMVhbIgVdmCV97y7-rK4EcDjCg-24mNDGrWI-MWz2Zgz0Q-iSqy6hqbJqS53kdtFq5Jp4rDExh7DmVg9OdOGCwxGgGQCzdJHLKkawLOjWI4moVdhqi962i4oj3fHKHRWNF78ZYl4D2ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=bHlyDFGNdJc5cQGiwN7fzvzoNEO1FdXgBP62MFn-lnSewlzGcobs957CpLNP5pNiT4JzNJrDPgF3UO9q5wWZly4y88vn50xhYo38o7HXGP7QESkv2zubLHvRKDUyuVQjjCKh-LR3CLQPHxKromF9C6FuZv2KzueoeGpRB8U7gjJEY_b4UGpIALNJ7NToWp87zdNz0h73hScBk8fyJlzPMxHnd4YCZdVABcT8jpV7YQQFTdsvX6cUXEeWR48FdbjtL_qBQpH4w96-Q2orRlmXF6anepDQiSazVjjnBo6l9Zkr7Ocq5iBEB-pquTtSWa9NcdNsoevwF2yRpBK0EnIvcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=bHlyDFGNdJc5cQGiwN7fzvzoNEO1FdXgBP62MFn-lnSewlzGcobs957CpLNP5pNiT4JzNJrDPgF3UO9q5wWZly4y88vn50xhYo38o7HXGP7QESkv2zubLHvRKDUyuVQjjCKh-LR3CLQPHxKromF9C6FuZv2KzueoeGpRB8U7gjJEY_b4UGpIALNJ7NToWp87zdNz0h73hScBk8fyJlzPMxHnd4YCZdVABcT8jpV7YQQFTdsvX6cUXEeWR48FdbjtL_qBQpH4w96-Q2orRlmXF6anepDQiSazVjjnBo6l9Zkr7Ocq5iBEB-pquTtSWa9NcdNsoevwF2yRpBK0EnIvcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7UssQI9Mqa6kpSTds2xrO_dtjvaOzjTA_df0l0OUrTQfaKCrx_cQdjyE3a4UnKVXjqSkxHEfr-LqDIie1CG3XsmjpV5t7uV4c1i5b9Tk0Vx-rDSD5IUVDPcJjxnX0Lxnax9c8_CTVLo9QNFO53EilccT-dk7GcfLIKmJ9BV_tCCKzkwPNBydn9j_oS6vIgXeQ1itxFGm5mEy66fPcyt-brFft4LYOoP2Ax1iNMNHZGonJQdDu-KB2xD-JTRahvV7Sn8kKfIix-CYig0XCIhknAyyq_VLLw_o78U3XEFsgadAJa4wmxwPfkXczP_0cwevvH8s6dhOjilDCk-_6ZHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=paB4axtff2OuE8aCuGxDDp47jatNj9u5a7R-dMIdv2z5rM-3gHpRnwvNkomDlx4l--aNmcMyDcX5OAPCi1vyZ75V1da2lDxnVm_kaevJCAv-WdjPxlRuNCpoGCa8tHPWGMm7b_K6Do51pmZTW0CERsbQOWNlOjIkiaFy1BWnyWFaQQ41QPqILBJokd7b-DnPpMzpdL_tgdI0s-x_0hA7AFohxT5gq0QoAliD3R33sYGIIHevwL9PSf8T-3pFdDLmJ2DvcMfWZIY1sMgGISer1LKQ6XgWuiqViqeUh3oOxZDFps8fvzEHA3t1ncXswqw0aU6NU_ZHITaRKSAEKodTsG823dIz6az0zz1yg2ySsWQSOYph-g6pktBXRu0ecwks2dGcYprsiUfgpOnZGAo8feClrc2TiMMetZdaDabRobybJVd-t4h_8kg-VIbN_IIY5X9R94tY3Ilr6aIEPalG1JZE771c5xS8dSukJecrpApVS-m1wd7Ka2e7kL7QKhuJDOvAZaQeYoBCR8HJlaJ-26GtZli2dYwFc6tbmefByKLT0sBkxT-kzUUZATzBWOmqAJM1FcQ9RKmHzBdLg-x-5M7hQI4wjYXZnMKH9f3rCVpK8nY9V30K0C9GmzeE7qM0C_jrHf1KckZgAJHzdQs1rEYuMF9gvAUOLhYIgpbNnL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=paB4axtff2OuE8aCuGxDDp47jatNj9u5a7R-dMIdv2z5rM-3gHpRnwvNkomDlx4l--aNmcMyDcX5OAPCi1vyZ75V1da2lDxnVm_kaevJCAv-WdjPxlRuNCpoGCa8tHPWGMm7b_K6Do51pmZTW0CERsbQOWNlOjIkiaFy1BWnyWFaQQ41QPqILBJokd7b-DnPpMzpdL_tgdI0s-x_0hA7AFohxT5gq0QoAliD3R33sYGIIHevwL9PSf8T-3pFdDLmJ2DvcMfWZIY1sMgGISer1LKQ6XgWuiqViqeUh3oOxZDFps8fvzEHA3t1ncXswqw0aU6NU_ZHITaRKSAEKodTsG823dIz6az0zz1yg2ySsWQSOYph-g6pktBXRu0ecwks2dGcYprsiUfgpOnZGAo8feClrc2TiMMetZdaDabRobybJVd-t4h_8kg-VIbN_IIY5X9R94tY3Ilr6aIEPalG1JZE771c5xS8dSukJecrpApVS-m1wd7Ka2e7kL7QKhuJDOvAZaQeYoBCR8HJlaJ-26GtZli2dYwFc6tbmefByKLT0sBkxT-kzUUZATzBWOmqAJM1FcQ9RKmHzBdLg-x-5M7hQI4wjYXZnMKH9f3rCVpK8nY9V30K0C9GmzeE7qM0C_jrHf1KckZgAJHzdQs1rEYuMF9gvAUOLhYIgpbNnL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFlqlyNn6PBv7pDzK24jH2ro7bV0W9lakOAI4xlHDIJ3fNlNVRtb-dwo_1N4GnfqzkwFhpxYJm1Bo1KF3cP7SU-shfYSbD0V4eD5PTJzh7FG9utMJA5kinsXlXCSDOs92_Jd--GItt668LuMpoUNvSXiLqYPnGUvBV--bv1ArLe3fXw7iSxe7MBHYccTdZBRRfNRmRX0T-B8H0dqjL-VEdWAgrYSO7MumO0ThJD0obeR8uolh7_EAOPjM1BpirZgHk7H--LG-ehBYPCwyyT6DPwjn61wOF--u3SLY6ds9KQdHor2XQJa3IF0D9_gLeLFp8NNjBZD2R2cA8L1-xjMPQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=aHdSLd1Ddcev6QFMwIifcPvQjYn1Q8vq9vYwKzlnB__mrUNKxe7JREHjhnj_SinuKRv-Fs28PwLQ9xw4WU4k2Xab39qO6pkSAfLj-jjMui-km97JW1_7gm0uigHF6BWGZS06Q32j2j8XP_gvfH2fHL4lZFSB-fb9YpX3IXFCPxwcpuLu7_DIHjeSu87PgmDjCuA07rwwohSxXH9gPe5XTveWSng1Dl_ykS_yCQ0xc1yBsuW5Xt_tPWpbvVLmCgX_bF4yjAFEJYzsu_m417eF_pa53in5X_pb5OesSL2PYPEb6QSRo1IA-otWgnb4W7u967BU4Z3xFyQ8FV4dfZEJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=aHdSLd1Ddcev6QFMwIifcPvQjYn1Q8vq9vYwKzlnB__mrUNKxe7JREHjhnj_SinuKRv-Fs28PwLQ9xw4WU4k2Xab39qO6pkSAfLj-jjMui-km97JW1_7gm0uigHF6BWGZS06Q32j2j8XP_gvfH2fHL4lZFSB-fb9YpX3IXFCPxwcpuLu7_DIHjeSu87PgmDjCuA07rwwohSxXH9gPe5XTveWSng1Dl_ykS_yCQ0xc1yBsuW5Xt_tPWpbvVLmCgX_bF4yjAFEJYzsu_m417eF_pa53in5X_pb5OesSL2PYPEb6QSRo1IA-otWgnb4W7u967BU4Z3xFyQ8FV4dfZEJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn6D869GCKhNTXK96OaATVL9DsKciNZhzFAYtVkmGt9mwP4V14k38coWUArv44ZbdlKS179XE48MD6Q7h_ISvOauw8NrfdN8wgtVMWu3j2d1ax32S2-P0fnHQEXxYgTQWXBHAjDfrxRit1AkX5ybxX5sM-YKvcBaylmLfk-DdT6MYx4Y_wmRiNw51m2wuHg0qYqdLgl-NhME9lSh6Ns_NlKsdrizYveOSoXHOTWoATVtuOjMbAZTT2p2MoWxcqkguLlza30TdNkywvd-tEW46gltAzhV_TXoOMlAXyFN8Th0tBlrNnDd52kgh2IhzSH_2BGt0JwbvwfvIkopt7u4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mztVkgTuT3RXdOFudNaGk5qR1NYxyUQdtTZr41g4H965te8leZM2x7xxq98mOwheEI9vT1psggeK-rfSiIp_Om_roY8va2XNGkMlaiatqn7Vh_80pZyPZkv9oFdpn35Duvqp0ks3kC_nBjGi8rrUUQ4mFcM0fIGurxThi88Pvnmmb_TaoLHUxIpnwCKtLUVI0qZR_TSbefEwKY5pJ930uKAABpiE27O6hn92CcrNRNYmM0PES9TMocJ_uvH26bk6xWl92cuk6xWkXLNFzJte_wy3ZuGvcDSJ0BE9fmOIi5pZ7C0hSNja9BZdn6kYOJBSnv_fQEFFtRneNaySy0gOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngPq4YgUFmWVPGgiJrVfLczzBUjG8J_1nlFFR4mxc4-IkrN3cp4xRMhlq4LP5tK2ra6u_Efib3DTRqkjjrZ0EUpGjEEYvRyptcjQw6XdRIuw5bF5v-JBHAXuwh9Q-5yfRVoYiIBt6EdgStnhDlqT3VsNVTT0w3T8Zm3XfWurpyMhPtM9FgHz70Jlr5-DCMxHbQhHiOEyIV-65j2HPUREJKFVRRPLNZZFWb8_uOueDjkThWFmcud-g_dURKrc4UcCbjX1I9k-lriqfyuwxM-nv9q3yV3Bts-R0Yh0pcN09rf_Whq2ANzxnFnBW_f0G7y59g49Q1EBkATTYmq6NuIlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=EWXD4WfC5YDxFebOOMC-yPUgRlmAyx4-xQ40tFI7yiaWKrl-N7AAmKxFk0bYVPFLxlX1CoTFmSgJKcEipiaVKM5ed99jv7q-OefjufB15V-_y4PDvcCVjBoo2wLcWz_ue1deyCff0XNE-BmSZ0zOl9_MtxP6osOi8zpplnhGMY2k2p8jiuPVPgCCfJ1kTX-TmyBhEiDFwt40fUuEYlvdryoSi5JmYY3IMidAlEN2pBSd0ULVmBYBYP4Nk59fSLNXOpVyA3dy9UIL8QjXR4tDw72SZbQZuu24puH9ZxG6B29rRn2lN65OriPkoC-CTm0QNkB_VRegAUMLiExHTx_yhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=EWXD4WfC5YDxFebOOMC-yPUgRlmAyx4-xQ40tFI7yiaWKrl-N7AAmKxFk0bYVPFLxlX1CoTFmSgJKcEipiaVKM5ed99jv7q-OefjufB15V-_y4PDvcCVjBoo2wLcWz_ue1deyCff0XNE-BmSZ0zOl9_MtxP6osOi8zpplnhGMY2k2p8jiuPVPgCCfJ1kTX-TmyBhEiDFwt40fUuEYlvdryoSi5JmYY3IMidAlEN2pBSd0ULVmBYBYP4Nk59fSLNXOpVyA3dy9UIL8QjXR4tDw72SZbQZuu24puH9ZxG6B29rRn2lN65OriPkoC-CTm0QNkB_VRegAUMLiExHTx_yhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQCNgQWt_9w-Su6qo6l7NRn_vx9tSW8wFkmHvnL8ggPYGm7uoyuEddewbhG7eQQEavRvRK4sGn4ZOq6GcsYfwKzldBteFW89pyTQX76PZCwIdxgm3xXzzJmZ4RvMIiB_-onndKdyw-Qzr60BFTxEKeskzxX-8Uuwjag_LRtasy3OSQS0qwQjDIX_Vx6LRGimt2HH2ejdpDRoS1IeNI9uBLXyifcKjBWPcRHVtICf61AWL1WDV8zZ3eVptjXoqVEXJOeK3x3rJeoLz39VhcKq0glp2By1PM-eiHR68VKZvR-_eVsDoY_FLo61tnVsId_61Ha0UgGwncS6lfz4q1-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4clfM0-TMWViDbWTu_y-pJduCjLsq7clGO_t29sIGK8rQRb3PlBGqIZ7OY7HDUsr9XG6Z2jfMk5nR_dq47LvVX_i8V4CgpZMdWEkGzhjlMTjW1PHSlJIejFrvoV5ZYGLkkf7JqOXk_A2VTbNcSTpfnpqeMIf_ml_FqQ4wNLKRrL5jQhdoycYN0g9kpwD3ZRuppGD2TMPocpwRVeIC_QWUfucXrFtRnmdS5Bv5DkeFMriLS3JFy5p9ypVXJKouJhidi2UBK4bu959IAwSyRI0qO5OxM-4ZT9nhG2MgijNshOTIe6RqxEZXF18ou1wyXLXmZHnbDMsG2YkkJ1LrhAnSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4clfM0-TMWViDbWTu_y-pJduCjLsq7clGO_t29sIGK8rQRb3PlBGqIZ7OY7HDUsr9XG6Z2jfMk5nR_dq47LvVX_i8V4CgpZMdWEkGzhjlMTjW1PHSlJIejFrvoV5ZYGLkkf7JqOXk_A2VTbNcSTpfnpqeMIf_ml_FqQ4wNLKRrL5jQhdoycYN0g9kpwD3ZRuppGD2TMPocpwRVeIC_QWUfucXrFtRnmdS5Bv5DkeFMriLS3JFy5p9ypVXJKouJhidi2UBK4bu959IAwSyRI0qO5OxM-4ZT9nhG2MgijNshOTIe6RqxEZXF18ou1wyXLXmZHnbDMsG2YkkJ1LrhAnSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=vSiaN8_fK-pJRaQ8-5ThX8fbxh5NmdICDEqstgkvBL-YMQOrRLjrpUHjWtaslJfL90NSzcOOAwhCTRTJ8uU1UcordpIVOO7av2KxYOM9mM8jBSypQCE62zCO_iaYIAyLM08cFWokDAz2nRILouJPfeY_fcJXZPzxybDzulSjWLVwUHy9AVPASJcd_WicS_MiJH2jTWXQ6ZQjZPFCGUUl0Lfi-anvUyR07pxKy3Q9OgJcDxqQDi5pPWuaN3VA1cb1fm0ClpyzQ9OKszUNyhQsoldVC7n2t-SMIlEoC8ZwoTXmzZYo994ccG8zE71yIQUnhH1XsWnGT9rlKdVcYmjEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=vSiaN8_fK-pJRaQ8-5ThX8fbxh5NmdICDEqstgkvBL-YMQOrRLjrpUHjWtaslJfL90NSzcOOAwhCTRTJ8uU1UcordpIVOO7av2KxYOM9mM8jBSypQCE62zCO_iaYIAyLM08cFWokDAz2nRILouJPfeY_fcJXZPzxybDzulSjWLVwUHy9AVPASJcd_WicS_MiJH2jTWXQ6ZQjZPFCGUUl0Lfi-anvUyR07pxKy3Q9OgJcDxqQDi5pPWuaN3VA1cb1fm0ClpyzQ9OKszUNyhQsoldVC7n2t-SMIlEoC8ZwoTXmzZYo994ccG8zE71yIQUnhH1XsWnGT9rlKdVcYmjEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=KisPqadyLvvLFN6bISsVW3PipPQifl_fYXYumwz1UqxmjNs9HiuSa3gRljQvPU4WLyMO9p32Qo3F14yOa-JZp41YpO4U0go0qKIuzHrLBZOAwCrOiNYaFs62AR4DTBum4SAmryJjw_hUu8zQD2z2DR97ViWYoziOmvdV9CK7weN7k5heE1N9oIJm5f5jDCaK-kGc_uDGjEUXLMwTINSFWDrvTtboVF9fmL4pa-V7dZExjvzdv023IJF5cxvnLQCYymnt24J86fon1m9zAexEwaaJ4DRh7S3UApZ7_ctfIPYlp3kUXEsEsVVZnxjtcJn8j0cxzQMm-0_T7uFWJRQYxy9X7QeP29QP96TH6Y6jCVJEQ7ltK7i0FQ843VFJeWU6WFA9IN1WuJd4VffJqbkoxfglwsQc7Nq6mF3VBUm5xNYFNtC3C5_ed7uQ9Szg91NHU9xZTVSstMIvLJBZxgr3R47AMqQT7QwdKiImSIP8y7ByR6sdmzE4JUCf1oE1E25zTWIpyUBQ3cwDf2gPb1GFvkUCArCI_NAtsja5U3PRPV8rWDkcxMp8-8IHlfo1d6YJ2nAgT0VgTFKWboJ9FhktqqtMXpX99p5g8koKFNl23RFFll3GECnTBEKJtLmLfePIQ-a_ThSi0ZGVcLrLiW2_lnUKLvkcM8RQx4klVA8mov4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=KisPqadyLvvLFN6bISsVW3PipPQifl_fYXYumwz1UqxmjNs9HiuSa3gRljQvPU4WLyMO9p32Qo3F14yOa-JZp41YpO4U0go0qKIuzHrLBZOAwCrOiNYaFs62AR4DTBum4SAmryJjw_hUu8zQD2z2DR97ViWYoziOmvdV9CK7weN7k5heE1N9oIJm5f5jDCaK-kGc_uDGjEUXLMwTINSFWDrvTtboVF9fmL4pa-V7dZExjvzdv023IJF5cxvnLQCYymnt24J86fon1m9zAexEwaaJ4DRh7S3UApZ7_ctfIPYlp3kUXEsEsVVZnxjtcJn8j0cxzQMm-0_T7uFWJRQYxy9X7QeP29QP96TH6Y6jCVJEQ7ltK7i0FQ843VFJeWU6WFA9IN1WuJd4VffJqbkoxfglwsQc7Nq6mF3VBUm5xNYFNtC3C5_ed7uQ9Szg91NHU9xZTVSstMIvLJBZxgr3R47AMqQT7QwdKiImSIP8y7ByR6sdmzE4JUCf1oE1E25zTWIpyUBQ3cwDf2gPb1GFvkUCArCI_NAtsja5U3PRPV8rWDkcxMp8-8IHlfo1d6YJ2nAgT0VgTFKWboJ9FhktqqtMXpX99p5g8koKFNl23RFFll3GECnTBEKJtLmLfePIQ-a_ThSi0ZGVcLrLiW2_lnUKLvkcM8RQx4klVA8mov4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=c8dSBSlNbWY4TiL61SevlzTWF9izR9VhOexJYr-b0gkoCgdp3_bYwZWBB_xhLU46tCJ_To066esz4XQiKKmjI-yOQzg7bQCC5AODiX4RqCZkTbRnB9f6o6rzoUMLZ1xtDauYfAqqeZIihvGgMdUQTSH7rs2j_8L-QIHsvvOvSTdvGVSDr8A8BWAJtjWSjs46233UGY0aAffh9vHHAGQR07yVCeEK2UbQA6Lardxz8zNlnn0RZYHnLVUQhtyd3c6M-tiYxZrsFzBaL5v2M61L9LeJxKiAuBYylKmjrEdRV-nMQ8OVKMd1SOzS0HCRiwY4lzwws6qeIMcooY9p-PXc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=c8dSBSlNbWY4TiL61SevlzTWF9izR9VhOexJYr-b0gkoCgdp3_bYwZWBB_xhLU46tCJ_To066esz4XQiKKmjI-yOQzg7bQCC5AODiX4RqCZkTbRnB9f6o6rzoUMLZ1xtDauYfAqqeZIihvGgMdUQTSH7rs2j_8L-QIHsvvOvSTdvGVSDr8A8BWAJtjWSjs46233UGY0aAffh9vHHAGQR07yVCeEK2UbQA6Lardxz8zNlnn0RZYHnLVUQhtyd3c6M-tiYxZrsFzBaL5v2M61L9LeJxKiAuBYylKmjrEdRV-nMQ8OVKMd1SOzS0HCRiwY4lzwws6qeIMcooY9p-PXc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6SzF2JPvTMAMu5U4eknp-pKjlk2axY8_GOrzoM6nHr32mE9oW9e2_M9yVyfqaSFpO3FOc-90dku1ZHOXiwcFVhkXSJJyULsymzUVpboPryBVvG-5mkQ4CvVjVJkCu4OyHHJW96GT2pRPoZ013sU_vkvki7lrujesk544o8G60CHQTXmtfs-hB-tcR_06l732WYXWF2EUKVvuscm2e_dacrIAA2tqlV9X0Xp47WYZm72LYUfjihZLpSVfBHTXCzbkfgl2obzDWiDs2H6iVB12RPAFmlDFiFCBgGaq5Su8pu2WvIIrB5Z-F6peSm_SsvMK3PbSdwO7GDrDnHsc7MTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=UJVujfwiCIH8rhWC6PM4pg8QU--kOPHmd7Lc5D_FDCc6o-5iuZEJxtD2rcLTcaiBcf44dxNsMnqkNPkF6zIFmUuo81ODEdtToopl0jEOIJKJR_vraPQiht3ed35CTlBwT-LTtEQ8Qnrk3CGq3SawOFk4W8Dy-n6kyRUylN-nDUCD3a6k51ghxyipW50FRavxMNYxKqzrrfHEz0EamMmuvmxAShVYJk_wPPY5Rc8_nC3mLZn1vmluz3F3EwdLVJKtQjCfaXED6kxxyT3Taf-o7xkcR5GHu08R9YjG1LELisPDdjwF2agykXRXG7fx1NhZT3wF6aGnI2Qn8klk4Y-ShA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=UJVujfwiCIH8rhWC6PM4pg8QU--kOPHmd7Lc5D_FDCc6o-5iuZEJxtD2rcLTcaiBcf44dxNsMnqkNPkF6zIFmUuo81ODEdtToopl0jEOIJKJR_vraPQiht3ed35CTlBwT-LTtEQ8Qnrk3CGq3SawOFk4W8Dy-n6kyRUylN-nDUCD3a6k51ghxyipW50FRavxMNYxKqzrrfHEz0EamMmuvmxAShVYJk_wPPY5Rc8_nC3mLZn1vmluz3F3EwdLVJKtQjCfaXED6kxxyT3Taf-o7xkcR5GHu08R9YjG1LELisPDdjwF2agykXRXG7fx1NhZT3wF6aGnI2Qn8klk4Y-ShA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=vtfAGjM2DAMWFNgV8L3akioMW4w568CMu0zW3lbvl5IM5JfA2AMolWUhqRG1wYQJavB_LOUGtuXTBjS5rvgYFCAXQXYhlER7GfbpyhfsCBO1BsNEZCaMOxeVMHh4jtGZ2dxCdTxpBHQWCabOUOw4qrujI2u__jXVXprZHriaRB94uR4D8b_KpxxEfLMTa60lTli9d5C1dZJpcwyh7hZuu33oKr5JME84Ev8BUfo8Q-Zr0FzPdDdqCNSqaW2ocqplHfnSnQmSQKdgIO2amhW_6KFVvPXLFlaCqqncqvKK5g60TQatThRoSVF3rhbYaHNcm9_2TwKov6OzkyyC93K5WUhYtneOqaQcwiFioxu0HjGHqitKGNiCldVgD3S-ErJDidkrUgRb11lkByie4ZFYqxdRn6MfISsH-pliG06N_oopNsayp4UEe4NviJzmLtGM5BVteSHHz7m2PkAqCGzP-9LVco_NALzAvLsPv8EnJuqOLsnjDcW7uHxwe8bEUBXyhDu93pCIe9Q5OVaOUuHk2JvEkBPwFiarxE5AHhIEIRREBD1nygta1IlRz9ivF_exL8lg6tKb9z863Fx17p7Z3ktxMcadFXKtXQOAEwk389a7l-VUE9w0jws9uB-vJ8gJm7xzQ79Epb-3BJA9jymfn-WGUoiFgdVmsxyrkZXiSVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=vtfAGjM2DAMWFNgV8L3akioMW4w568CMu0zW3lbvl5IM5JfA2AMolWUhqRG1wYQJavB_LOUGtuXTBjS5rvgYFCAXQXYhlER7GfbpyhfsCBO1BsNEZCaMOxeVMHh4jtGZ2dxCdTxpBHQWCabOUOw4qrujI2u__jXVXprZHriaRB94uR4D8b_KpxxEfLMTa60lTli9d5C1dZJpcwyh7hZuu33oKr5JME84Ev8BUfo8Q-Zr0FzPdDdqCNSqaW2ocqplHfnSnQmSQKdgIO2amhW_6KFVvPXLFlaCqqncqvKK5g60TQatThRoSVF3rhbYaHNcm9_2TwKov6OzkyyC93K5WUhYtneOqaQcwiFioxu0HjGHqitKGNiCldVgD3S-ErJDidkrUgRb11lkByie4ZFYqxdRn6MfISsH-pliG06N_oopNsayp4UEe4NviJzmLtGM5BVteSHHz7m2PkAqCGzP-9LVco_NALzAvLsPv8EnJuqOLsnjDcW7uHxwe8bEUBXyhDu93pCIe9Q5OVaOUuHk2JvEkBPwFiarxE5AHhIEIRREBD1nygta1IlRz9ivF_exL8lg6tKb9z863Fx17p7Z3ktxMcadFXKtXQOAEwk389a7l-VUE9w0jws9uB-vJ8gJm7xzQ79Epb-3BJA9jymfn-WGUoiFgdVmsxyrkZXiSVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pT-Q9ANyC7Qlqw2OHWbCrC-QPsExGB6CNAMZtTW4Y0dKO0TsVLDwCx_GluhYXrWYieYo26uSkO21l3jTvPzU9mEDgRt27xTAy_ugc7e0ro11gxLaxSoOLKeK0YBi3ASGk5IMwHfAE2boY5tkWCW4X3cKWgVlyKZLe8gPM5NRdDLo-g4QTpboyhol9sJr5VCasKdksdETnrLNs7AKG4ma1B4lCv3fmzmXV7vXOOQ5cH2z0hZqRScR5IWrNBjPHjnZJXeQk1Kkku9xRsVbVyxPedcny4aFvKHbK7N-bwjpcPkbOq8-F33-nI-3Yt-hHrlT91d_P0ML5TNYdsY9t_5PLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ZyvQw5WvqeocFRNiQqK5-7rT-VHhiejdPQZ3iyEUjemVbbkqn-rT_ZSibTX2JgpYsXw0KEXPr4UAiH7miyaM1upeL4ynuGdE2txS2UKiv4htbKY3ni2D6zf6KpML9yt3HQ3U7CoR1v-EezjCmNnNMCIDZmtVtRR8yx3Um2Bs-5pzYLpsWrkosuyUkpk0ff3Wdqov4KANRZNc_f3bl07XSsIhQHTkPm-Qjb2Ku4sSLenl8Rt7RYevI7-Bj9J5PoNFeHsn7p3OcUJHwakN_1aiTG9kIIjLqF53r2ZbjIcV84z4dheEXzNZUoHjoQa1xfY7lh6Oj2osj2fLnxxp6e-s_0IAb1wgP8IvjRTz407i9UsDvGWMEH9-eEWQbhagXXNP45wZJEQKcY_FVXx3AIA13pTJOLXFcKHnTxcJ0l9S6Q8ypbFHCJ8c9YA34QQrFxxmW9O2UekXLNgysQq_EmPNURY_zrpdG2jWIn3qGhoST8xQImGe_EWyhcVU3RL5WwZp7UDXmgwXzV5g99qRlXe73VqICZ5zczJ5NPcVQvPBzMlkbDkEork56WvWkULHlgzYFaytseNElwGwfRU92N3kT_DmvpW14vrLyrDS2aj8LevapGepCbveGDSfNgp1f4rZFVTOEKMiww6P_S6ICkLKZc6teomsuD333GGi5sXmh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ZyvQw5WvqeocFRNiQqK5-7rT-VHhiejdPQZ3iyEUjemVbbkqn-rT_ZSibTX2JgpYsXw0KEXPr4UAiH7miyaM1upeL4ynuGdE2txS2UKiv4htbKY3ni2D6zf6KpML9yt3HQ3U7CoR1v-EezjCmNnNMCIDZmtVtRR8yx3Um2Bs-5pzYLpsWrkosuyUkpk0ff3Wdqov4KANRZNc_f3bl07XSsIhQHTkPm-Qjb2Ku4sSLenl8Rt7RYevI7-Bj9J5PoNFeHsn7p3OcUJHwakN_1aiTG9kIIjLqF53r2ZbjIcV84z4dheEXzNZUoHjoQa1xfY7lh6Oj2osj2fLnxxp6e-s_0IAb1wgP8IvjRTz407i9UsDvGWMEH9-eEWQbhagXXNP45wZJEQKcY_FVXx3AIA13pTJOLXFcKHnTxcJ0l9S6Q8ypbFHCJ8c9YA34QQrFxxmW9O2UekXLNgysQq_EmPNURY_zrpdG2jWIn3qGhoST8xQImGe_EWyhcVU3RL5WwZp7UDXmgwXzV5g99qRlXe73VqICZ5zczJ5NPcVQvPBzMlkbDkEork56WvWkULHlgzYFaytseNElwGwfRU92N3kT_DmvpW14vrLyrDS2aj8LevapGepCbveGDSfNgp1f4rZFVTOEKMiww6P_S6ICkLKZc6teomsuD333GGi5sXmh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=qb8aNOkAzG5UWTqf2RAyr59fx56yfb5YD3PEsFhE7fQcikL8qynV7fsMhdCQRz1IbO16FKFuO5SwErbe3hpyZsK49tLYlyIHdbAxVzWvrfHuyAhE2lhh3AgezwresFQPZPv9xqxXQ7eBaibPxIZlM9KMWu9roYKqQfEuYSTfvU0DYIPWs528JtgmQTpvCN1mqFAaGNQHFPlXWWth4TqMX0hcl1np1YuBfln7kYIDjNdLfrzX-EUjF2zekKtChFJDb4ypu-pb7iGDOizKyFm5y1q78iF8ibz-_luodAP978qP_BD7XqjD3K5qxEntGZ8yUVvaKbw5etMbgVICUlC4J6PeBYk9ei_3h2gr5LlFfmlE8bzQP0quiidvb3B_26yCm9QUtTAZ-yPRNYE2McXXjnODbBf8IT2rcb0a4HykgNx2s1KVm2U-M7pXSJtC8fShoIZMBDB9HhF0x8caREs5Aq4JP0czko8dp3EDwXV59o-FcWZD3m8bcPhzt_GAtvaibCwln7gtwHXubIEebwFYriJen0T24Dya71mkISGztzVzppUGPNtrF_ydEuLGRwc8d8U-fAwxfafZspuivVI7KFGwgNXoht7ek_5k159UEQxrH3lO4ZNnIF5VyygcaeAr6ncWiXWoYm1zBYxh5AgBDoPM1bmLGdVefT7QpwLZEPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=qb8aNOkAzG5UWTqf2RAyr59fx56yfb5YD3PEsFhE7fQcikL8qynV7fsMhdCQRz1IbO16FKFuO5SwErbe3hpyZsK49tLYlyIHdbAxVzWvrfHuyAhE2lhh3AgezwresFQPZPv9xqxXQ7eBaibPxIZlM9KMWu9roYKqQfEuYSTfvU0DYIPWs528JtgmQTpvCN1mqFAaGNQHFPlXWWth4TqMX0hcl1np1YuBfln7kYIDjNdLfrzX-EUjF2zekKtChFJDb4ypu-pb7iGDOizKyFm5y1q78iF8ibz-_luodAP978qP_BD7XqjD3K5qxEntGZ8yUVvaKbw5etMbgVICUlC4J6PeBYk9ei_3h2gr5LlFfmlE8bzQP0quiidvb3B_26yCm9QUtTAZ-yPRNYE2McXXjnODbBf8IT2rcb0a4HykgNx2s1KVm2U-M7pXSJtC8fShoIZMBDB9HhF0x8caREs5Aq4JP0czko8dp3EDwXV59o-FcWZD3m8bcPhzt_GAtvaibCwln7gtwHXubIEebwFYriJen0T24Dya71mkISGztzVzppUGPNtrF_ydEuLGRwc8d8U-fAwxfafZspuivVI7KFGwgNXoht7ek_5k159UEQxrH3lO4ZNnIF5VyygcaeAr6ncWiXWoYm1zBYxh5AgBDoPM1bmLGdVefT7QpwLZEPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=krRYh43gZXTHFXHk59AN_ANKw79ALgdYHpWEH2jFHSxmZu-29m1PepQJu92YzjzSKProuiLqimeBRIzY63t8Czpe5Ag3ia4_pq4oeVD4hv-3afiigdsT8toJROfGVfSBQ2PQiV1i0uV48yBV7Tx55s2ggSm9sWAyF_GrZreRFZqsnN0t9hlC-JrvLvCU6ygThPKGOoZMT4XebyEheJJb9ipxCCymchkGTY0JxMvgtiMM5NGzM797Qkr690m5zhnbJ_n93bEX0REsY6QeHgj-RY_tfCr-BHV6Y3WHyZbPNsV_AGo_X01zrUhVKSAS2BokkDF7EdfEBt61LBUyMnIR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=krRYh43gZXTHFXHk59AN_ANKw79ALgdYHpWEH2jFHSxmZu-29m1PepQJu92YzjzSKProuiLqimeBRIzY63t8Czpe5Ag3ia4_pq4oeVD4hv-3afiigdsT8toJROfGVfSBQ2PQiV1i0uV48yBV7Tx55s2ggSm9sWAyF_GrZreRFZqsnN0t9hlC-JrvLvCU6ygThPKGOoZMT4XebyEheJJb9ipxCCymchkGTY0JxMvgtiMM5NGzM797Qkr690m5zhnbJ_n93bEX0REsY6QeHgj-RY_tfCr-BHV6Y3WHyZbPNsV_AGo_X01zrUhVKSAS2BokkDF7EdfEBt61LBUyMnIR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=UlOCKP_RbfqGp7t7OBP8xynPYAixL3ZeFdW8r5NpT5l4ZQCgjZqHlm8hYh0_hUBcTXoddMQsNa00ul7USiDPMi8wtFmKrzVYS3QFanI5HKocuUzktIzWDrQIzugobUlYa923X9BQUQE0bLawPmcXIPLD1o4MmFoLdFXQshaNHRDnaFZPRAb0UXZSUnKAi7f5KIEwxVRkfzmjVUFNaPvg4c2f3YmFSsHWdqCCzFj8XwD67lbyVRNA1MwTO-8beHfIKC3fyeUstyGvkTUdO6fMpecmvTV9iFsuM5Ni8VrRhrAfncDl-AlIQ6oAwVgyBNM8bsNl9sTeqlNxiXnQ_0dOLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=UlOCKP_RbfqGp7t7OBP8xynPYAixL3ZeFdW8r5NpT5l4ZQCgjZqHlm8hYh0_hUBcTXoddMQsNa00ul7USiDPMi8wtFmKrzVYS3QFanI5HKocuUzktIzWDrQIzugobUlYa923X9BQUQE0bLawPmcXIPLD1o4MmFoLdFXQshaNHRDnaFZPRAb0UXZSUnKAi7f5KIEwxVRkfzmjVUFNaPvg4c2f3YmFSsHWdqCCzFj8XwD67lbyVRNA1MwTO-8beHfIKC3fyeUstyGvkTUdO6fMpecmvTV9iFsuM5Ni8VrRhrAfncDl-AlIQ6oAwVgyBNM8bsNl9sTeqlNxiXnQ_0dOLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=m4JLhGgCWCjdkkNxm16WNhtU3YsIUM2pno0maUtsvDfU3G88fjdDbN8oK1PL5MIcr6eD6E8Ptt4bxkSp5MMPxfLEC9WKnAiYXSlSB5xy9T6sGxVqPNwViuFmhMlz3EoVSwyzRoqW4x_sTpqI4L-cwEEyX0I6o0YpBQ8e7qs3DfpRK__nqkM-u8nkLuk1XJbjLSi_qb6BZ1gKa-O-ACa3EjhE6KJg1H47dltgln2jA9ndqVyLiuODg3N8R0n-vL8349rH-Yb3fucyWcUxivaXTlhjIKgCfnFvJJ-Ki7uwI3ae5uVJmOBevm71aGnCus39lmXO1IMQH8DfWy9HAm2Frw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=m4JLhGgCWCjdkkNxm16WNhtU3YsIUM2pno0maUtsvDfU3G88fjdDbN8oK1PL5MIcr6eD6E8Ptt4bxkSp5MMPxfLEC9WKnAiYXSlSB5xy9T6sGxVqPNwViuFmhMlz3EoVSwyzRoqW4x_sTpqI4L-cwEEyX0I6o0YpBQ8e7qs3DfpRK__nqkM-u8nkLuk1XJbjLSi_qb6BZ1gKa-O-ACa3EjhE6KJg1H47dltgln2jA9ndqVyLiuODg3N8R0n-vL8349rH-Yb3fucyWcUxivaXTlhjIKgCfnFvJJ-Ki7uwI3ae5uVJmOBevm71aGnCus39lmXO1IMQH8DfWy9HAm2Frw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ABg3G0QZognPLmUZN5MF6PfHelMNkUJV4ztNZdVNH0nbtWtFd6iddou28YaDJuipUVnphKa8Jf2n_hsjmdWNNh-9WActzQmy1BN3l3GBYWnRFDD2Xdyv_Dm2ip2OGDU2h9UdIw_8JrCKgXNlrRzuju0JNHUxu0mJ-RDRDCvHflDKHiVub8LWyv3tBWKJhKniEsZTC3Fbe7Bup416Cpy37Jm9HqENZrkCJyCoOozdI_3kpiKV4ztVU9fBmu1IJfsw7RVLuEgcDeq362-5QQZi9p8GdLLrt5LtjQK2YwJJT8RP595kdbX9d8oUReLp2BL0l873HbJJPkT1CpatxaVCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ABg3G0QZognPLmUZN5MF6PfHelMNkUJV4ztNZdVNH0nbtWtFd6iddou28YaDJuipUVnphKa8Jf2n_hsjmdWNNh-9WActzQmy1BN3l3GBYWnRFDD2Xdyv_Dm2ip2OGDU2h9UdIw_8JrCKgXNlrRzuju0JNHUxu0mJ-RDRDCvHflDKHiVub8LWyv3tBWKJhKniEsZTC3Fbe7Bup416Cpy37Jm9HqENZrkCJyCoOozdI_3kpiKV4ztVU9fBmu1IJfsw7RVLuEgcDeq362-5QQZi9p8GdLLrt5LtjQK2YwJJT8RP595kdbX9d8oUReLp2BL0l873HbJJPkT1CpatxaVCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tdXjndRxSYLBT0mJprejxTfGhzDN8jw6wI8B-F5yzXv4uX9TekROphIvs2AmBeN75iGfr40cUeiT-mKknc8UU856Hkz2WXIvsJqi8nHBDko5o4tuMfSdq3tiAz5d_ElLQFRSnkRbEeDCHP7C_ByATvDl0skr1YUN64O9gG7fI-ZsjyOab9C4HoFytQyy9iFyDSlpV7nOywW-ypii4I0klnRM2_ghqU8YtM-Nhv8llPrmwqZJSqwRmafpnooZmHsUWUyieF0MQmMX7ZubafysbqboDkAEkmvcHQEojhgH42Eyikivb_utfoxrxU2S3Kitj6adHBOaHpaSDpNmjk2hNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tdXjndRxSYLBT0mJprejxTfGhzDN8jw6wI8B-F5yzXv4uX9TekROphIvs2AmBeN75iGfr40cUeiT-mKknc8UU856Hkz2WXIvsJqi8nHBDko5o4tuMfSdq3tiAz5d_ElLQFRSnkRbEeDCHP7C_ByATvDl0skr1YUN64O9gG7fI-ZsjyOab9C4HoFytQyy9iFyDSlpV7nOywW-ypii4I0klnRM2_ghqU8YtM-Nhv8llPrmwqZJSqwRmafpnooZmHsUWUyieF0MQmMX7ZubafysbqboDkAEkmvcHQEojhgH42Eyikivb_utfoxrxU2S3Kitj6adHBOaHpaSDpNmjk2hNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=RnRbXYEYv88SGQgvKEimYtfXlKlK8QWb9XI2Jzcfqw7GIjDIrszUvXMnQ93B7GkNmdbpCgVUUmMdHCI25sP7uMcUR_ilzmezo_z8irSKjnAhol4F3BlaZ7qGhC_-Y7GmLpjIMgjPFX4vgn880DJ5klRlDb3slLMALlRByVoX4C60gR4b76X6InAZNuLECZKXe829JhrZC8CSPxAnpGiKy7ZSGFa4CVVDbok25VZ568aFD3chUtfFtDQySNX6aTvVhajj-ORtXxf-bW_g6Ejdujdm9wbZqU_ClZOM32L7EtfoTDMsv24MveL7Hw3Tg9qo_rLN2WirsNxrs5tcId4EZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=RnRbXYEYv88SGQgvKEimYtfXlKlK8QWb9XI2Jzcfqw7GIjDIrszUvXMnQ93B7GkNmdbpCgVUUmMdHCI25sP7uMcUR_ilzmezo_z8irSKjnAhol4F3BlaZ7qGhC_-Y7GmLpjIMgjPFX4vgn880DJ5klRlDb3slLMALlRByVoX4C60gR4b76X6InAZNuLECZKXe829JhrZC8CSPxAnpGiKy7ZSGFa4CVVDbok25VZ568aFD3chUtfFtDQySNX6aTvVhajj-ORtXxf-bW_g6Ejdujdm9wbZqU_ClZOM32L7EtfoTDMsv24MveL7Hw3Tg9qo_rLN2WirsNxrs5tcId4EZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=JOZ-KB9QgvQr594UBYCJhxUTr9uhiEaVp4nU3S7GzjvKn4RW7oklptAdtmfO4_SyT0E98MwhereFeSDMXOi64vWEhiZpIa6uYcQv07Frh2_Lz7Zr7egtMKTSgj3d2tvzu-VVkisEKwVuSiYr8r8SHUcM5QXzEH5FCBu5w3t773rSal43F3Min6VuKz5VGoxS-xS8Pg4IAuMmdptrjA5hmpA5ewqDDofccrocWJIvd_1UO0YqxbzN4Cz7RRMfFq9utQ9_mSBDohlUuzLJcfr97y7DpLjO2gPelEZO74kDDSBDv98n5fFsCucRKoUk4g3Frh65Il6DzgGTSvQoqEm7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=JOZ-KB9QgvQr594UBYCJhxUTr9uhiEaVp4nU3S7GzjvKn4RW7oklptAdtmfO4_SyT0E98MwhereFeSDMXOi64vWEhiZpIa6uYcQv07Frh2_Lz7Zr7egtMKTSgj3d2tvzu-VVkisEKwVuSiYr8r8SHUcM5QXzEH5FCBu5w3t773rSal43F3Min6VuKz5VGoxS-xS8Pg4IAuMmdptrjA5hmpA5ewqDDofccrocWJIvd_1UO0YqxbzN4Cz7RRMfFq9utQ9_mSBDohlUuzLJcfr97y7DpLjO2gPelEZO74kDDSBDv98n5fFsCucRKoUk4g3Frh65Il6DzgGTSvQoqEm7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt7la8UjU7hoq6w2gIQ6AMPPQWH2gqSFFbnFQoS5uOZhl5uehOhLAwxO1IzrSVLLCfc09koLy_kUz-LwHnEZdutZAfoCk-9f5G7bMCLUmV4nT3Ta-lnhcGzPjpgIObkeMPq6b3DcsEySSo9HudyB0VkXb4DsPfGKZsCLHaS3zoP0PGliNCjM8QRyTBycK956V8RXPPReWcKJPv625dGCd-aUwiQu3OzH-49x8Q0xpayfDfacS1bM9x09do9rOXOV_WEJIOO4I4oEdBwPMoZtYIIyLekdOyzS_ASMk5rYRLjJYuLE6zB0b16AKbsKlSqAtz529DDxXqQb_te100U87A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qRGSHHUGwRcmemnU7nlJ6qjYF-YrL0UJ8HXpPhSq4akUE6ss8TyN9_EvBGWqAkVGvzPH-sPrbMT8ugC8-IDAExsBWXQ5XM1_0UR-SANABaEJ5_a-Qnylrs31Y-En0BfGQHUgXRzpnZ-CBmifXHLtMqZZMmGRXxuv3LcpgZcNZCnbTgfPewk9tifJ715V_BAJbBJXJDz5-O9zWOHwvdrX1nYT9YvecJIATIWprSdzV7qwFqHyth7oQg-lFpJXaMuaZTAqf34UFAfJZvkOPkSM24FroUbl3GToSnDU_nbxT1wGLAf_qL2NeMJBj93L01I1N4Jc1YrRjACqsY1ArareXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qRGSHHUGwRcmemnU7nlJ6qjYF-YrL0UJ8HXpPhSq4akUE6ss8TyN9_EvBGWqAkVGvzPH-sPrbMT8ugC8-IDAExsBWXQ5XM1_0UR-SANABaEJ5_a-Qnylrs31Y-En0BfGQHUgXRzpnZ-CBmifXHLtMqZZMmGRXxuv3LcpgZcNZCnbTgfPewk9tifJ715V_BAJbBJXJDz5-O9zWOHwvdrX1nYT9YvecJIATIWprSdzV7qwFqHyth7oQg-lFpJXaMuaZTAqf34UFAfJZvkOPkSM24FroUbl3GToSnDU_nbxT1wGLAf_qL2NeMJBj93L01I1N4Jc1YrRjACqsY1ArareXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=UdagNMFhZiw6hhxyScsGcO6i44PybpTQUK8G6H6vHUeYR268bPEHvgpWKkeu29MW8xLEUXejEaIdatLvnhDGiAULpGJYs2wl0fCzEYHaflgSDxoF8577PrKzQipNIg7-X7U39AX5FfxlavGuyyyTeVv41miIWirluPRWgr9pgzs8f39LtBFts34Z4IePhRe-VwVMslcgnXtmWF8M08XkLQkUo6WVXunwm7r4gEimzjSU6y5dpS_hZGuiRNMG1Di2DPnwlu9-1rnIY4a32u4BeATwI6QTeg33HZVy72VIVfGcVKzzSSD2_uIqhVGvPqARERl2koTe1qIpoP2yn2W1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=UdagNMFhZiw6hhxyScsGcO6i44PybpTQUK8G6H6vHUeYR268bPEHvgpWKkeu29MW8xLEUXejEaIdatLvnhDGiAULpGJYs2wl0fCzEYHaflgSDxoF8577PrKzQipNIg7-X7U39AX5FfxlavGuyyyTeVv41miIWirluPRWgr9pgzs8f39LtBFts34Z4IePhRe-VwVMslcgnXtmWF8M08XkLQkUo6WVXunwm7r4gEimzjSU6y5dpS_hZGuiRNMG1Di2DPnwlu9-1rnIY4a32u4BeATwI6QTeg33HZVy72VIVfGcVKzzSSD2_uIqhVGvPqARERl2koTe1qIpoP2yn2W1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=BqoqlS5oRm12Qrp1K84XZ70mlZZLxPpjOVfF9D5vgfyH31QT0AS-DRIBO4oIi6TxmGQI862kBbnZmYjUJ2LZDYke85jL7CHqkTb6dmX_R8kp7RcyPZhpoyqx86mO-tz7iR7x9gSsnnblV9YMxl4mjZBGRDmi8hONgl9kyj8a4W0wvF_xtoFaRQICNrbcWrLHOgYQWKv2gebjp6y90PQDPN-vKv5WG_d-5HItaUVm0ON2MKGkvM_D0R64xYm_w9jhp3PTXi_z3yDHjQ891oekW5_ymNv4AAd7heI1KuIYBN02iK5rz_X_ndswD52Qd-Dv-uYkjqA58_Msdwn6z7jsiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=BqoqlS5oRm12Qrp1K84XZ70mlZZLxPpjOVfF9D5vgfyH31QT0AS-DRIBO4oIi6TxmGQI862kBbnZmYjUJ2LZDYke85jL7CHqkTb6dmX_R8kp7RcyPZhpoyqx86mO-tz7iR7x9gSsnnblV9YMxl4mjZBGRDmi8hONgl9kyj8a4W0wvF_xtoFaRQICNrbcWrLHOgYQWKv2gebjp6y90PQDPN-vKv5WG_d-5HItaUVm0ON2MKGkvM_D0R64xYm_w9jhp3PTXi_z3yDHjQ891oekW5_ymNv4AAd7heI1KuIYBN02iK5rz_X_ndswD52Qd-Dv-uYkjqA58_Msdwn6z7jsiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=JfCsVSvGrlx3QdSJxRrIvA_nSUhtD2-PaAsgeN2S-MT1xSAdRpUCs-0H7Y32UfyCgMT607bew5sWO9DTRX2u-d46V0x647a8VYF0P7zKt6kQfLA1ATarSK4wdNhEIpb2dFrGTqZFt-GJdvilmKCmj3jPjO6wUbfR0JreyhGfPxdFB5tSMTqQwK2fE6wgNVutk9FWFwFgKIQTwqubt3DCoSTVF7Fn56wnYlMlVOwNTnZYNyKa704Qecp36BsyeQTVe4-lnYErr9NfENJ9YrH0s-HlDsbd8GahD9dt9Up_opvbW4HgBZ6QMyR3vP3ydkSf5uwHABvlzyQ19p464mtHJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=JfCsVSvGrlx3QdSJxRrIvA_nSUhtD2-PaAsgeN2S-MT1xSAdRpUCs-0H7Y32UfyCgMT607bew5sWO9DTRX2u-d46V0x647a8VYF0P7zKt6kQfLA1ATarSK4wdNhEIpb2dFrGTqZFt-GJdvilmKCmj3jPjO6wUbfR0JreyhGfPxdFB5tSMTqQwK2fE6wgNVutk9FWFwFgKIQTwqubt3DCoSTVF7Fn56wnYlMlVOwNTnZYNyKa704Qecp36BsyeQTVe4-lnYErr9NfENJ9YrH0s-HlDsbd8GahD9dt9Up_opvbW4HgBZ6QMyR3vP3ydkSf5uwHABvlzyQ19p464mtHJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j67DiXgfzzGr-aP-JFmYBaTZhdIN53bvHE1LMESlBCynZLGaOZEN6YdTG5AjUUsddDIR-UEBGeckibp4xNEqfGIU02l-gVk-kf7RXH7ROsFAe9pp5jIxy7YABPqqGwHUSlILV8F7YoVxt2Hj22n5kY0R0SDgxB8htawwWOOWRBhS_lleXU_VD5rPkYIeCLywji3Z4Ehv_NK2PL6Dlrqv9OZbDGA2nwYP0a4uOIiosUrLtyMUW280x7IHS1aNlnwbkaG1AuJHSMR1z_J2X0KDfDPQJTMobMxgwY0OwkEAUO8Qoph5YIFBLlpBpm2qEGhly6eDVEVnqXTAb3cHBnldqQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Qpz3yGWqYDmbroq2hfWSyi5728ic0qVpaXPusqis-n8wIBYvGJJXuQKXy3UasgqhGgYt6SjkyPy96hTrXsr_rmqgUAk1BOZ82PRecfUWYSMQWlYyguPyDs6Ma3dGAx_zTz4sMuAY8a-AIHb2iA474E5rOj2FgIk6cpGuryr2AqZ22X6r7MsQMv_Olfj2k2ZNGxnQ-6FAQZOdHD-F6GjZu8O9OVGezQkhMAqBHedo9FcdeZNQWctbA-qdmKyFWMTjf8pLssc4fqP-yjCoQDoOK9TvMW_AKxKiB11bwqqMg8Ws7pRfDL2_vm0rJwlBPTHcou6eZgVbgk3Wp6zOKlpwvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Qpz3yGWqYDmbroq2hfWSyi5728ic0qVpaXPusqis-n8wIBYvGJJXuQKXy3UasgqhGgYt6SjkyPy96hTrXsr_rmqgUAk1BOZ82PRecfUWYSMQWlYyguPyDs6Ma3dGAx_zTz4sMuAY8a-AIHb2iA474E5rOj2FgIk6cpGuryr2AqZ22X6r7MsQMv_Olfj2k2ZNGxnQ-6FAQZOdHD-F6GjZu8O9OVGezQkhMAqBHedo9FcdeZNQWctbA-qdmKyFWMTjf8pLssc4fqP-yjCoQDoOK9TvMW_AKxKiB11bwqqMg8Ws7pRfDL2_vm0rJwlBPTHcou6eZgVbgk3Wp6zOKlpwvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=rTWTJPAuZPbpaZ1Vnlr_r9mSMKE6KVz3PrMtKk4BLqIb9rT-8cXskIAfsH-ACaHve76ZctaDQ6qp3i4g5JvomFHeLIKotu1E6KztBKIAyYmkMkNxS8xCW8BJhTLKQAj8IUdD_RNxHdVJUBcscQ5EjxfXQGyoQ2qSWy4CbsIzffdLiCxJxNELsNsM3Hw66CMtQv1d0tffsT_saRvIafmy6EYI4b0j32ECTTZD_EBCnZ5n3MTVkDRckdwlH5s1SSNOnQ9FYd21bI7ZpLY_QO-dwmwhVrT5zTKjxPolSWlnurwA7C9jwmTPCZgaxfUVUbgNKgysfQfozwTarDy91c7NGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=rTWTJPAuZPbpaZ1Vnlr_r9mSMKE6KVz3PrMtKk4BLqIb9rT-8cXskIAfsH-ACaHve76ZctaDQ6qp3i4g5JvomFHeLIKotu1E6KztBKIAyYmkMkNxS8xCW8BJhTLKQAj8IUdD_RNxHdVJUBcscQ5EjxfXQGyoQ2qSWy4CbsIzffdLiCxJxNELsNsM3Hw66CMtQv1d0tffsT_saRvIafmy6EYI4b0j32ECTTZD_EBCnZ5n3MTVkDRckdwlH5s1SSNOnQ9FYd21bI7ZpLY_QO-dwmwhVrT5zTKjxPolSWlnurwA7C9jwmTPCZgaxfUVUbgNKgysfQfozwTarDy91c7NGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fckqj7sUD-TFFMisklkdTn5iT9CUyhDFdA7onX2BOr2s-tiJBf-uCiyZE8agBmGWwMNEJcl9eNbswZvC0ir7i8EuFO8e_YvNW9M22iKVjFd--mxB1jfgBBCv3d9BTEp-d3dn5wIQBjH-sdWAQwldstVIWhgMiq7jMmJW2vHLWxC-onB4Qb6t3MHB06xxefhVyyedlpnrrAUBQV-3PzgkPtauZVXR47DrCiLJqXRgxKtrHgxdEaBw2f2o373i9x0-vD_XXaFOR6fNzM6GS7BYT_9ahqRC8PMy1CR42RFXrAjJYpt8a6wWw6rb5RRB-oMSjzdzwt_em6IL0TfN_rrV-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRZ__LcUy-yCt3n0RmiSh14-rQzYBEpA9wy3SjjpvHqc8j874yZWspOWZSg6njHqYlPg-BebYk2lX5jaMnh9-1HJ5NhHCusLJSFMpZupbeDcQTHIFIseKt_JjmkgQ16TSS4M0hPW9UY0SamhGmslQemqiUGFY06nISYISsd_QVkju34cm5NOdDM5NxKNv4BGseiz_s7Fxz4ZqsaZpQxPPj5ZO5qAs4ep-L6M-CaKNqfrc0KwQyAiR_8brS8VAuBRsDOxj2K6jH8EwNTDtSwlZgmIlFMqI6_iKOa3vjTLxj_L8W-UjfFAAly_ZxhBU0YbHTcgRvhumW2J_ARnuGFODQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=lD_0pc-0hzKErpfu1QdaNgNtn5NiTizY5dYA75KMH5Doeyi_xmKOzQoVat-oxr0sQBJqMs13P4J2mA39PhjWb9AdQW1GQQpVy01yFrR0x6I_ct-cMy_FvuLesj6KGPfcVTsM1tY3GAmfNdi_2BGYeak8kdLPr5HpoBL1wXGlM3XM01a_YrnT7iDAIh-B61NJzqkiBGaCh_DQ3T38dZT3dMfd4BkLRnTcnM-KPN1P4GgebszP-Qjjw7TlxDTrzwOQWj4s6fJ3afGy93UuHvLyvkDLIQapj6VvE2S3qhhfWeee0dOJ6PunGXLCKZo4-DN3LcWSDEDuJ7_LQ4CSY3JxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=lD_0pc-0hzKErpfu1QdaNgNtn5NiTizY5dYA75KMH5Doeyi_xmKOzQoVat-oxr0sQBJqMs13P4J2mA39PhjWb9AdQW1GQQpVy01yFrR0x6I_ct-cMy_FvuLesj6KGPfcVTsM1tY3GAmfNdi_2BGYeak8kdLPr5HpoBL1wXGlM3XM01a_YrnT7iDAIh-B61NJzqkiBGaCh_DQ3T38dZT3dMfd4BkLRnTcnM-KPN1P4GgebszP-Qjjw7TlxDTrzwOQWj4s6fJ3afGy93UuHvLyvkDLIQapj6VvE2S3qhhfWeee0dOJ6PunGXLCKZo4-DN3LcWSDEDuJ7_LQ4CSY3JxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNLLEb3ydKG2NEIk6WeBtmHif9EPaN4FnHQ95rO1uqxgUgeQi1vqBKEhIsN6eA1BL8bJltvrVz2i8S7jk2Mw3KsRwyhivOTxQQj69WjYLkkvSzmRrus6A1Str0QOBEPlaNBP9LShAicwlZSorhutZVyhTl14bgXVC1a3RdUf5dtl1a7ChA6xgd3oGzGlC7HwyUNO9OpNWV5plsjl6ixmsLh6Us5Qlrwcpk1C3HpCk6HwCf-EbAd9JKZ1WMbiE5r5_KOLKX9yFp1isoYHQgs5E-ts-Fa5BQYosh_IxM8UrRQp1SZ0Y7Sar24ChGlVVEDBmdpoZaHL8zWkkoVFoB-e0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXwB7fvrqkRcS6Vcm-s6aRe1Rl6se11u5eSCq7wgVM7oc9GEOrclZTC3yzmCnAQVuCMzhoNOr42o3maf_nEqEHHHC-vmx7zpKG-vzKaxMqxYkofeN3U_eSNjNAHSa81Y6RoFJ_aEMdNONrPbnesL5SxwT2C6io5R0HQrgRE1K80db8V7jX4riQ-CyO-f1rhD3JuTPhzwzgMC01pKllEFLlk8qRr7wT4w9RN3aCYcJ9KoDT7TO6OmkiYk1Uyllf-Tuyl4t2eQJ0uzCO8L8KyrJ40tU_X1p5r-JEq0tZ0xY-VY9iwAQ1br533m0lpjCc78hygD7F1WSCCFaDbv9GLPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz2HKRYaiizFq2_B7eE7CZPYqAirEa7jEjRtO5EeAJgA2RBurb0ACnCkF0jL1YX3VSrvAzd5uvClU4bJW43NwtySnWpRW24ntRI4vxTNqBfhHKspZDoTk9I9G92hWEUzd9pvUZsgapJeN4N9RY6IIC8cw4kgTg_75Ru1hzTb2yy8jd_3HSOEP6NvXnqlic76JbZI39VEOC_QCs_zictlsjKxIAFlSw9W-mU1Ko2mkX_bx_DbFllL0UBdEPZ7Cd44btqat52Y2vScn6DMUIAskc6VU647wnCmM1aPTIHpjmYHq9t6ajw5Ha8yZz48g21cXEQNYexJHzSLZSVLpb2aKA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=fsIKOjYSkUBGzG0lqu1yUPMkXqEKyaA6KnsU42cEhPtFkjx6Wb0mQNI-pcqV2FE9PAQ7uiXMKqj6wQ93cbjiWo-DRqjY-icTS0C0bQMER8-0F4kPXAYMYY2NHPgxwy463trUcCQdt8tRNSNBKrnFGrphrkFjl48WfcWNpU-GM4xs-_UPbmzxwNME_XTDwZ_-1fvI8K4XgIJ05LoPnPwc8Qi8Bu7dINFDoPJWB16yBvNTpZ4ZzIBfEnwdeYxBP0KNJ5fZH9sWQoKAKw5OEeYHB7QIAi4KvqoTokahGVP1CARP2aaw4qIE6FKCZjLI3WAkQO3sml6k1Fm3Z2utG5SAuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=fsIKOjYSkUBGzG0lqu1yUPMkXqEKyaA6KnsU42cEhPtFkjx6Wb0mQNI-pcqV2FE9PAQ7uiXMKqj6wQ93cbjiWo-DRqjY-icTS0C0bQMER8-0F4kPXAYMYY2NHPgxwy463trUcCQdt8tRNSNBKrnFGrphrkFjl48WfcWNpU-GM4xs-_UPbmzxwNME_XTDwZ_-1fvI8K4XgIJ05LoPnPwc8Qi8Bu7dINFDoPJWB16yBvNTpZ4ZzIBfEnwdeYxBP0KNJ5fZH9sWQoKAKw5OEeYHB7QIAi4KvqoTokahGVP1CARP2aaw4qIE6FKCZjLI3WAkQO3sml6k1Fm3Z2utG5SAuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=EYvvzTr9qhXrOuadOIjs9Z2NNUioKc8dCdOoHr791yXp_biC0gDPhRhhDJmpORJQX5BjEnJcC9cSHu6lnuDxChhTv3yUKJvJgmEYYu3Tm7BTE_tJlhgOP4KEZQs7ofNOLCK85fAk7y68ci1ca0FmEPR1zLdYchOmxv_PAHxJWWhfaPk9i8ZD8snxMKj3a54tkgPNgucXMcW4CokoyWHFNynzTrhgKZq5d1pcpYlxC5VOTARVYZbd9v3oqk_cfqHx_iAxZxoo_02VwbUDwWaUYLwCJdjetViolXnU8Z7FtfSAPkvpzMo5EM6WUknF3yjBr_ot8rhBgEFhjhzWgmOODA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=EYvvzTr9qhXrOuadOIjs9Z2NNUioKc8dCdOoHr791yXp_biC0gDPhRhhDJmpORJQX5BjEnJcC9cSHu6lnuDxChhTv3yUKJvJgmEYYu3Tm7BTE_tJlhgOP4KEZQs7ofNOLCK85fAk7y68ci1ca0FmEPR1zLdYchOmxv_PAHxJWWhfaPk9i8ZD8snxMKj3a54tkgPNgucXMcW4CokoyWHFNynzTrhgKZq5d1pcpYlxC5VOTARVYZbd9v3oqk_cfqHx_iAxZxoo_02VwbUDwWaUYLwCJdjetViolXnU8Z7FtfSAPkvpzMo5EM6WUknF3yjBr_ot8rhBgEFhjhzWgmOODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Og5YqG3siSWrI5fn50NgCpbuFGUpraKOGRJD4Z7xb9ROnG7yTgTAku9yA_cwWphIWaQ2Ft70hym3Qy28DqbORp-721jUQM7TXbaAgo7BSY7PEjEmz-C5gQ7N3nYzks5WJlV3AWn7HGCAXovkyqiawqVzNkq6njMLxNe51VGT027i-J9TpKs_YD6n5Z2lWghefpeNnWmmN0iMeEkf3rCEpuaxWsZAyS-FhbdtDwUTzuoU88y-F2F-R7sCAubO-UAo6eM0PSxJwKeyYF56TkF2p35J1eK_VA5BtdNo-Pf5n0Y2TebQ03ZudDFnwL2uBO1eywYH2a7E3EF3pl4xiobgkh28Qn8rfwduQWCWGrpyAnBtg2h5eiJIwOyZoLiAEQ8fvtuW2qdBIdOyvtqU-sl-aX5GFWJBK_uC8Xq39Lphea7TxJvRFjRiA1klx6yp00y39FWZX7MonhuUTPTdn92O8BAjjn7eIrE7CbdZZeB-2Rspo_fK3CyKhU9V_xsKpWeMZ-wJO0J8g7qXJO9OlfEaNiSb5qdN7SzXFpz4CLK-4gMhHe3r2q4_a40PFq37w04R5w51C88HCpDMgmZanjzSQHj3VD6lXlMlOCZ05ytJVlin8TW7GbPp49OTC0bREzBDN0qsUz4wez42SxN1Cn0yxPoEJq5Vev_jjkDAQvSqiO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Og5YqG3siSWrI5fn50NgCpbuFGUpraKOGRJD4Z7xb9ROnG7yTgTAku9yA_cwWphIWaQ2Ft70hym3Qy28DqbORp-721jUQM7TXbaAgo7BSY7PEjEmz-C5gQ7N3nYzks5WJlV3AWn7HGCAXovkyqiawqVzNkq6njMLxNe51VGT027i-J9TpKs_YD6n5Z2lWghefpeNnWmmN0iMeEkf3rCEpuaxWsZAyS-FhbdtDwUTzuoU88y-F2F-R7sCAubO-UAo6eM0PSxJwKeyYF56TkF2p35J1eK_VA5BtdNo-Pf5n0Y2TebQ03ZudDFnwL2uBO1eywYH2a7E3EF3pl4xiobgkh28Qn8rfwduQWCWGrpyAnBtg2h5eiJIwOyZoLiAEQ8fvtuW2qdBIdOyvtqU-sl-aX5GFWJBK_uC8Xq39Lphea7TxJvRFjRiA1klx6yp00y39FWZX7MonhuUTPTdn92O8BAjjn7eIrE7CbdZZeB-2Rspo_fK3CyKhU9V_xsKpWeMZ-wJO0J8g7qXJO9OlfEaNiSb5qdN7SzXFpz4CLK-4gMhHe3r2q4_a40PFq37w04R5w51C88HCpDMgmZanjzSQHj3VD6lXlMlOCZ05ytJVlin8TW7GbPp49OTC0bREzBDN0qsUz4wez42SxN1Cn0yxPoEJq5Vev_jjkDAQvSqiO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=q-QXatL_UKpaF7TQMmjbCdE64a_mAuciNFqV59ROdBS9pyG0rKVRsIwD7H_DDHY2gGraGyNxPkQEP_WewYLPQkjXt-qTCApTVaKFPO3QqAnxdZ7hUOHYLIp5czl_JbTEIlCekfnAASouJuPJJ-7EdSqnKqDGqmGuWO-I85fIVJIpcvZFHCLX9Sob-LeixphwvOvs6hIfI3-3fB2x68QOPq3BRDu0eYkK1vCiEff4vXLQS1EayIl6NTqKS1GYDgx9gwiLpwdNcN3VcJwy60zSQLDhmrp0WeCjFb6RQXYxIZiqgA1Mr1xhw2dadz5u7euYRn7SUh6PZv2zSFpIzraf4B0hwYHMJ-tEeMJ-W0v5kfd647JrVy9n1r7ABTvBUvxlZ3hNWN4Bf7xa164-ls-n7xPpmiDZUw5OvP5DBlFO6TbbV-MPiln7o3PIv6aWrLTp6e6RFtnUYQm-bT1UTdFt_YGtBpR-IJbON0yNxtP3rSjJhYfGlTtr2TfjZ-BXO7vvil9Kw01FJn3Bz30vfYtBoFbzbf2GyqikVUqp8od-LqzX9cPlVjLXDQ2QUOHrtXd1uKVcbqd_kL5AXJWkqz6aMOseWDfUpXjOBHKt8YchftA5XFngIMcERdFr3yz_5ebsULSiOvFPnpTCK5zBLRtoE7ShW0FgmuHrL-_2l2BaooE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=q-QXatL_UKpaF7TQMmjbCdE64a_mAuciNFqV59ROdBS9pyG0rKVRsIwD7H_DDHY2gGraGyNxPkQEP_WewYLPQkjXt-qTCApTVaKFPO3QqAnxdZ7hUOHYLIp5czl_JbTEIlCekfnAASouJuPJJ-7EdSqnKqDGqmGuWO-I85fIVJIpcvZFHCLX9Sob-LeixphwvOvs6hIfI3-3fB2x68QOPq3BRDu0eYkK1vCiEff4vXLQS1EayIl6NTqKS1GYDgx9gwiLpwdNcN3VcJwy60zSQLDhmrp0WeCjFb6RQXYxIZiqgA1Mr1xhw2dadz5u7euYRn7SUh6PZv2zSFpIzraf4B0hwYHMJ-tEeMJ-W0v5kfd647JrVy9n1r7ABTvBUvxlZ3hNWN4Bf7xa164-ls-n7xPpmiDZUw5OvP5DBlFO6TbbV-MPiln7o3PIv6aWrLTp6e6RFtnUYQm-bT1UTdFt_YGtBpR-IJbON0yNxtP3rSjJhYfGlTtr2TfjZ-BXO7vvil9Kw01FJn3Bz30vfYtBoFbzbf2GyqikVUqp8od-LqzX9cPlVjLXDQ2QUOHrtXd1uKVcbqd_kL5AXJWkqz6aMOseWDfUpXjOBHKt8YchftA5XFngIMcERdFr3yz_5ebsULSiOvFPnpTCK5zBLRtoE7ShW0FgmuHrL-_2l2BaooE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=saXIbbaPsTyhvuKMgTSXr5xiAUX0m3CvfEYGjuKDRoVKamGhAoxnUd1ieO0LWIe34vthRdhuQTkJdJM2NwDqfw5X9XEIjKfSdr1pMXhtMaY6nLFBmDEjeUROfdReck9Bv0SyIXOohzBA8uHAKDJ5lY-vbef8h-dBmFONCl5i9J87LLjPgjiY1DGnbJbsffCIi9U1rRZss1gRKvP3neZfnh9scPmgQxzW3M8SyOl3lhN1SJDIVWxoEhyaqk-nsy38pKxNzU8jgKbQp9ZxnpEDRxUOlmCd3TAKns7WEV-9LYQf6TQq79GgRPlcnsIKrz4hl8VS-VqLCcaHR1fUGJBWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=saXIbbaPsTyhvuKMgTSXr5xiAUX0m3CvfEYGjuKDRoVKamGhAoxnUd1ieO0LWIe34vthRdhuQTkJdJM2NwDqfw5X9XEIjKfSdr1pMXhtMaY6nLFBmDEjeUROfdReck9Bv0SyIXOohzBA8uHAKDJ5lY-vbef8h-dBmFONCl5i9J87LLjPgjiY1DGnbJbsffCIi9U1rRZss1gRKvP3neZfnh9scPmgQxzW3M8SyOl3lhN1SJDIVWxoEhyaqk-nsy38pKxNzU8jgKbQp9ZxnpEDRxUOlmCd3TAKns7WEV-9LYQf6TQq79GgRPlcnsIKrz4hl8VS-VqLCcaHR1fUGJBWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENI757juxDSRJmTlNcOrYguBSqOB6C5AbGt5kaD_o18bOx7_cmn1s7As5-PPtEMODlvbE1LsUuZVZJhuOzNb7RJND2qj8-UiDt112Je_cWBcF0iya8cwNGHcyZtZdlxsE5Hjsj-V3KyrCSSVYw6x7acQ3PocGnL4doYYbLhP1SK1GJmI27CKrFiRx0K_Zgq4vQf2ewzeRvXo48fXDwNO_LfmsvuqPzMPxFSGxkkp1NtbyjcI4yNF0fNjZUEi5FQIr6JCsxJ8mXSC4D7WjY4c3aaAzAzqWbCa6lt9z4_QFll-1NpNm7lb4FySwRjRA1j1Y84U3xLTzMg7BT8YSDBWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=gbCXApxmVfwM-Jp0lfeWkDsNq0mxDFklH_5DyJwM2BSw6x3UMdR6mWilVqAoKOZBi11x24chSlXkvkfmLH9algUMbXIAfgh6AOs17JzTOEktBE-d1Pfs08YJGl5AfpIDwCjjgsm0fXqHXGFXWwoBQKT7I19uK7zxniQlsOjzVHxfUgxvegtXS4iAN4PC19haFy_V8OT1oKIc08jjVzejA1YsYb-_N0gEyhwLToepez1mhaYwf_-wVgdUzYdXFNlj2x90Q3YvfmnJVam-1F9mu6GpbJDEDQ9SiROTbrGCQFGC1xQpO-Ru4n6K2zWrxX_K-bajnOTJhLkHQLnYVLiwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=gbCXApxmVfwM-Jp0lfeWkDsNq0mxDFklH_5DyJwM2BSw6x3UMdR6mWilVqAoKOZBi11x24chSlXkvkfmLH9algUMbXIAfgh6AOs17JzTOEktBE-d1Pfs08YJGl5AfpIDwCjjgsm0fXqHXGFXWwoBQKT7I19uK7zxniQlsOjzVHxfUgxvegtXS4iAN4PC19haFy_V8OT1oKIc08jjVzejA1YsYb-_N0gEyhwLToepez1mhaYwf_-wVgdUzYdXFNlj2x90Q3YvfmnJVam-1F9mu6GpbJDEDQ9SiROTbrGCQFGC1xQpO-Ru4n6K2zWrxX_K-bajnOTJhLkHQLnYVLiwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=TJbSLXheokaNx2InlsBM-1lgPF34tKqmlxLNUVX0dtjk1-uJvpDRtSz55lLThKmuAYkshmXk6SdWfWOoPhhxeVI5vaf2RPAGJGHASxvOv607GKqDTJqaevOHLjPG4zGg5F-NKy5MvmdJgugdUcwb4x1fc-8-GHM26Y4yXm_9kYmSXwc8MtG9AtxZrJYuhDd-qBCdpjwENV0V6-yvkFttSyqreqaMrnZPlSVNTuxWAWKYB9jpxsAlbEqffzBs0Jv2Bg9aAgvae0SCYDmJ4t3_fYDDN0lx19mGJP0gRIctJc2ox7XgdvZokazjuXEwe3sKBZIfVl2nClOh08NokZjHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=TJbSLXheokaNx2InlsBM-1lgPF34tKqmlxLNUVX0dtjk1-uJvpDRtSz55lLThKmuAYkshmXk6SdWfWOoPhhxeVI5vaf2RPAGJGHASxvOv607GKqDTJqaevOHLjPG4zGg5F-NKy5MvmdJgugdUcwb4x1fc-8-GHM26Y4yXm_9kYmSXwc8MtG9AtxZrJYuhDd-qBCdpjwENV0V6-yvkFttSyqreqaMrnZPlSVNTuxWAWKYB9jpxsAlbEqffzBs0Jv2Bg9aAgvae0SCYDmJ4t3_fYDDN0lx19mGJP0gRIctJc2ox7XgdvZokazjuXEwe3sKBZIfVl2nClOh08NokZjHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9x3b1RT47FKDUXNJtjCcpY5APAOJ1jCpAVPl8Dh9ESR4sy1KAFTcgJhxCEQ5J__5oqkS40kDIcqtenMr_xi3UfEOQtaxQpMI6MV1XBjc-KJbUfenCh_nQd6GpEv1KNgl15u300gP53eOXGeTNB5L_MYIFJUJSxvogou0qhJJTlvKvGIUy9oma-kGYnga0WHGKhiXaNqRpzVQKpYm3x1y-lbXo513THJXHOw2oERhS-npe0u6GL4qrLgcbCcMnhQNOuKCLyJLZxDL5igRQIcREp3yhlj2GekI0n3v-0S_NpXK6b22jAohldJB7U7c0BMEPTx8NbewvbG7tEo1ozazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3VFPCTzsFWIcPMfHhj7PIxeAim3DTPuDTCyFhKeAH2rzRo7Exmuta-LGzoLMnrodMUmxK1vsLeY_i0e0_2pw0fhD2pQalHfafCEtqHtfdy-aRAAzsIgv9IkLHBosDwWoAfcWI3Oz01fP_0CWEYLEhZQbhrFsxfl_M1K5dbrWeknL3wQDgWG75cw0CStTIUhB36cHYlOJ74OPtG2oW1zALXEGaPgkFA4ppPV4WiPX8PPdOkKn5fj41FH_7wx3x_n_quLh2MTAgwhP1MUISR_4m4wsghzK-bOe-uE0rBU_A3sF5Btn0al6FjmydiO1wBS8P7LKCxRh-MAgdysItRXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuDuy7l6mZLs3_aZ4qulEDaBKWZCdJrC_HMX1MibXkWtAQ2_VnNBNx_r4bt78Ut51tx8ijSZuDwyDIrN3uaO636lVii3dCCChbXXzOUbiZBilSrvFAEarxHCovRooCZqzLN9e13M1c1JuvXl-IeVJDG2hhADS8jhT4Txtxe67BBoLKyikyfuehyqAOSWx_aF1qDVfNh8CG1fbq1HlGPqW_fQcY_vGNVWuvHlWIZJkAyNdvf0Ue_9W3RKp64Ll2rc59eFkYtwxfru5o2diDeofbHsjxxRi5UW11Ck8gjpDoKx6EvFqsKQRdfuTL7oTEImFsmOrMlo2P1jD0Jx6hNrvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOmBJYoeIuUqFeXaNUAIIgBEJc4rKdB9rUknCDOQCV_vIIzQ9pnfPrbcra20rCSNr7z8nlyQdAM4fThx-vvAs4Uki_mJni8Ev-V8VZfYp1AhW3WleEmVHnnwMGO7oTs4FgRaaIm38e9ZjNC4HVQ1O7G0MAXJ2pGk3xzJ4aVnQDHCp1g2TgdjVCCg9U14sOwzfWskNy60CjO75DA79yQzFqUIVk6G6JAeThdP7wsS1JU0PTkRLAff2o8ZCRwi1zAcmKLeLKy_GF8WPeIVFzwNruPvt6ChXHhK4rxxJQo11GR4I2lmSCBbnMyIpoIPon6jrdKIP2MadgJrJ5w-FRt0YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5UX9MVhYN5p4PB7INDGdCoxTPd3pOiTY00ohxxaGdC5qfU4G_omHP-1mGn4KaJ4DjYmp0q9WoLqhYiBkLot6z7QmYZ61R_EyZgmDTPCvwO16FhNiMMikkK39_VDdORT4FEUS6FzIae_7JDxNQajiItTaAD60RBZar3yxuoVq8NVRHJeJzwuIksPCTVV2m0pVnXeS1Y9G9CyXmdsEUwmiS-ke4E91jmqbJZjplwLibYWnwVZtyoNFjMbg3QjgNL9oa7aP-ThFlaS5k4FnUlcFgDX9hfLlfC_4tEt3Bsy5BMxU5DKLmTMxxrdw7Q2cl17HucaYnq8gnVxtUJoEc1qWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL31cBWesN8CnSXHOYbJTXaeodi5DXU1DGkLTUpFL8s3vdcRNzjH-y8qbB3-Y0xtT4LZ_y27ayLbjhPCMOXRf6Q7Fld89vhxpLZW10xGJugcvqBa435UeL92zIkLh_Cl0MX0pfKdeXnKlgXa9CMyWTqOjLYymppzONjli-_y5HKsO2KQi_QnqWgMm8DA3Fd0xBMFvctq2kt1tP-Eu46bJpCIAcMXZVTezhgs2QKrVmWEr8e-WAa57pb4CVIKnR02_CWrDtzTaz3F_FgyPLGH662muhQC_yLpKrL7zsISR14Y64i8buBFlxtCkh-tdUPLyAPx8PbLMPKTxblWYYW5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMngEawbe1nIxB7nJwOsCXwgEEooEvnsXngOF2K_ayciXVU1sws1L0boHGJ5J4nq2bsNpKxWElxPgjyZPpyH2M0dkNmRooL4wliDFD7oPpFtLBQsHfrQ2UIek64P1QyBPUn_x1peQlCZqQzEsL0ui2UgWFGXJFxUy-agAzH1k3ciPMQ63fpwMQwAa7n2faHzMOk0A0wf3ePgaBBYHZ2kWdWSvPeYdQjyjj33npqXE73C6q-faqOcknU6Qw7O-Fp1Oo8-8KSISqgha_MQn2VUAX4lAn3S7pPGQnEb3sVH9nvrHm8i_Nc8EN00RKHbHIaz_cXIr6rT1JLZfbdo7RmACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGOat4E-mvoDC64gclUxvJMk2U1-dwbdSb5zToD6vfWZhrOsW5T4wzb-acAbGd0lCICQk7OAnez_44fGE46-d7ODHVWE5iDmoTiLR6X68yeYM9aQx7lCmjzz53TV-aJlnpnMBVzCGQqsrxQAcdkBDG0ZaeUQ0ViUZheLdt4RE3mKWseFPIc20SvKpKiwkTRXjVA2PtFePH4jJLTgUK4a598m53vVn5GDhyRldo2WdZBsirSBnT0owmiQKFpZqvTEGMwCFsEWUGxc6gr17VdhsK7y80jr-keUbd3oNklG4K0AY5MsuHS0j05bHkEpC50eDHYVAsh3Q4KzjpK-GEVoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL5346vdPFwvo8SPmSJ0c9bMHlbND1k08V1S7wpaR5AtXyiIj6_xYZoLf0aC-cf0cV8e6AAD2_e_l2Lj1I-nkTChGUVza0850gHSZZWVKstrUFlaUldjPTmd1qoHKCWetfJ298-F6jBO8PAgbefEaBHHZjiHINGrjwZ8lpkSvkbxvdwYNeK8VqkOQEYa0BwX3I-moYL61szbU8an1OrEjbDEgUBl_zOu9G5_E1bbsNriXkfZCLX1nFqLbu6Ec4re5gqe_kb9ciwOppqBVJVa1tXCT-29ITieV3N5FPEGW6QU_aInrRwhMWMYv5yhEAtn-WAbZHYUue5Wac2TI6IdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEpYlNd3fWpC7J_XiAZrQobmOUmTdFDbKlea5Tec7eIDwdrTnj7e8Ll3a02zXd8I2V-eyyaFZi-ath3p-QtRYjgVi34SdKqR4_nNpiH0C4g7_8Bi-ZjKfgJF2D5fqlnmSmfNnC00JSzLSQMbit8KW-HCjogEbJF1DgN-GKw2VcJkQSX5myssYhBYPchZMdsgKkJxwAdy9p_FAnlEiFVBTetuD_HtREdEcCm1cyid4y3zgVlzZOWSmGN-sZj7quCtycdc5hlQ7BiUkydQLJnKXTDzRCn8-U2sBvkzTwu3AMjPnUVvP0V_xOyHGux3QWDdqGs3hBVQiNACdokcKz86AA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=rIz9BADofdTb3umSQ5tvVjNgzl5X2eCkGERRdaUIc9rsUKVtTSkBG51_jMdjq2dJvsOG1VQ-s7C_54ENTVF2R7481IDvSelFen81erl-EOnL2UzRivVwMFDfMZi9FMqtB7LjQJ_ZQ-zbuUTqWixiKRdA0n7XyulxnHfmTkffDNm2zmRLHo6G6Ym0QrJUxt5-A7jSNUDzZy3h-BMb-RYIHmm4etmBuKfdnom6Ow6brvrYKpHkRiFkFPrH8jrY-pQlU0pSNKruI_wQNc8eID20sPhh1J_TMa79qfB4S_bXo5Te8Pry-dDCs_0Mnpd_wbQIiHRtqNHgoiPUAtmvpnt-NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=rIz9BADofdTb3umSQ5tvVjNgzl5X2eCkGERRdaUIc9rsUKVtTSkBG51_jMdjq2dJvsOG1VQ-s7C_54ENTVF2R7481IDvSelFen81erl-EOnL2UzRivVwMFDfMZi9FMqtB7LjQJ_ZQ-zbuUTqWixiKRdA0n7XyulxnHfmTkffDNm2zmRLHo6G6Ym0QrJUxt5-A7jSNUDzZy3h-BMb-RYIHmm4etmBuKfdnom6Ow6brvrYKpHkRiFkFPrH8jrY-pQlU0pSNKruI_wQNc8eID20sPhh1J_TMa79qfB4S_bXo5Te8Pry-dDCs_0Mnpd_wbQIiHRtqNHgoiPUAtmvpnt-NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
