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
<img src="https://cdn4.telesco.pe/file/vveoeBcQmTg4aTHwCOBfIIMcGUHqqQA-PDJ6RznmxwynlJsouxtWtsBm_Rxqr3gnx8hrR5xstnxQEINDJ9TZq05l_NMRrC-WCCoxeFbwTr9rNc1rZJAFOSvLg_M8AqFIrI75f9hpxPnw-l7sP_A59dJRoQTeEsXCIJYtjbtan7OcwJU6vtS0vpTt4hNuvYwlpAd9UoTB-ltXcqKaKa1dh7BIzc6_7FJxJQueM4PdYLstDt9n-btoyX63WXFUkMLf22sUIJKkl1qm9tvgxOGiqhw4NUhZf-6paB-BNn0FWUioqKKmTS1jhHizshQvXwvrHvKUiRZw72TtAttv19pXvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 06:13:59</div>
<hr>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Xu-1Sv90oyw714rx6EwCm8pyPA1QzJzkpoobjrS0xEIstln6p6BVQFAWDdNBc0i9vgMbSwNhynf9temTE6hoGPeazJfnoWbNLt9KJuEw2x1kM39CcK08xuRQsKq6A5IL6TmB77y6M4AKJl-Nqk1z8lp3556EP_CXBSlbOHP4kGXI4DP1Lhp0achH3MRLxSRjn97t6PPcv65QeAnQrq9oc9M34Z_3WkRHUyJMouT2glyogky1kN_YhKevps6watjL9NT7pe0wrxUFjh7sxTP_r7MCUCE_3nTuHpKLN-B67sE4T6kG8QSPRIRo37NQdJPoh7X-ZgdkxObB0tRFZWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=t81phrgs0qOYW-tM67kEaGNYb5UBnk3ErzEf9PZKHF5DRn8uAuso2hRnTGFq3OsgsMDBENlLwvbZBZDR1FXL4APlG9QcgEf3CmO3GvIJKTZu7nEn2q3yEi-KggsU_1yKpp-nhRXiDzsllFf3l_4mB05LhOCMvMnOeFlEMMp5z2_1vpStXI-o-gwpc_eY9KN5gmfm-EfxBIgRvcEPJqzucU9ctCB2dNtUWCFRs_c3k-WtMhD8ATE8GyQ40qau2tdbiSzobmJu4mYXS9MH8y5162WWhJ3SBy1KdeS3HX9HuQw98bcodNaloyzu2g_qz64jMnspp0Aqa0RHj6yYycxfRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=t81phrgs0qOYW-tM67kEaGNYb5UBnk3ErzEf9PZKHF5DRn8uAuso2hRnTGFq3OsgsMDBENlLwvbZBZDR1FXL4APlG9QcgEf3CmO3GvIJKTZu7nEn2q3yEi-KggsU_1yKpp-nhRXiDzsllFf3l_4mB05LhOCMvMnOeFlEMMp5z2_1vpStXI-o-gwpc_eY9KN5gmfm-EfxBIgRvcEPJqzucU9ctCB2dNtUWCFRs_c3k-WtMhD8ATE8GyQ40qau2tdbiSzobmJu4mYXS9MH8y5162WWhJ3SBy1KdeS3HX9HuQw98bcodNaloyzu2g_qz64jMnspp0Aqa0RHj6yYycxfRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugMyO6z0lFTERuz4j0r0smhdQ6Nqz1aSLVsO6wOfL8WSRkgvmH3L7QRNHgjOaSSrVnIl-4sYqyWzu-HnbM5xKKP8p2SkvKQntaX_uJfAZ_lQirF4vnBeH7ztcvQihjrq6qGWXi3V1hrZudH4jZKGls7E2X6z6oqXCy9ObMdq1fLC746_OQb2Wf1QN_UCgY9c6rX833w8qWIkaCDaRRVtbAQTsT6yR2MgmBfmgaOQ48r9rPq1kzlDga85XJeh6dYzJHrNTe_uWfo026n9SqbVSoI3iIqUu_sKjsyzDjjoBtkrBITdHHOoZv6oUhehdJoApHVTtGYraYAW3qAxkrB6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=U6ZycOvFuYlPi9N3KWcEOv5k2r7HN9LG27e_ynm1zdbaa8rLwHYHj1qObwC1Z51Mo-vB6QS0zZOMy09XwIQnkw5kPVPFqfSjLOC_22FBF6I2ChFCgfFQnSkvvB11eMr5xEysxReVDtZvmt8MY-kjRIjQi7O-ALFcEnAo751A1W0yXUSvX0etaM6cBRa6W_HEOYEy1_KMLSYYgOOVr-yjxVlEj8_z8UQZAXhy_8toflFTS2O9ilXGX29yxjqtOVpfW2Sw2w8tmD5IC-debB8iDvnMywH704HamO2ozoVSg6QgPi-rdLOxqHHRBfQIRuMa--p2CtS9Oif-iUqANGgBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=U6ZycOvFuYlPi9N3KWcEOv5k2r7HN9LG27e_ynm1zdbaa8rLwHYHj1qObwC1Z51Mo-vB6QS0zZOMy09XwIQnkw5kPVPFqfSjLOC_22FBF6I2ChFCgfFQnSkvvB11eMr5xEysxReVDtZvmt8MY-kjRIjQi7O-ALFcEnAo751A1W0yXUSvX0etaM6cBRa6W_HEOYEy1_KMLSYYgOOVr-yjxVlEj8_z8UQZAXhy_8toflFTS2O9ilXGX29yxjqtOVpfW2Sw2w8tmD5IC-debB8iDvnMywH704HamO2ozoVSg6QgPi-rdLOxqHHRBfQIRuMa--p2CtS9Oif-iUqANGgBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMkz5sX9PTeEjCiNSA9jacT4khR_vwGc8ITb05O1NmZh7rhkjkJHvoNoQryB6BrhMxengYInqgRdd6XFKuN3PogMiLgwKplKWfOZqxQ1M99jWwWHVAk5vJ4221314fnfK8rUOkUg-X5oFtQvLP5uEtV5wgiKp6CkTeCfcbDgiXqwiByVjiS9RORqam2zua0MFQf-F3COKUyGNBN_x8ocr44B-Ln82InY1EmxRwrOM72am1Ef_x0v--j0XYfKg76Ljkb0X3FU73SSkiWRRcN9cTh2JxbcJw99Kspd0LEY4scLajweA6VgAPnV34ThUryrsMZ3kTR45WlZVxRUldKDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1i8nL2018cOSIgcnX6Kq35ow18aHD2JE-6y1OEmJG1JIxqYIWNhu-I_lTo23eQD7ous07OyYNxdbYqAKRWw0ilubNYN9tbU_Xjj9PfFMuSgQNdNHrArPD26b6yD_UpGn2o6zDTY8cbA-rgA1rOQs754QIDu6VvvTBPI0t7-BnbegYSyIwS5Uc3-BQwF0QAr3A1js0ZZoXVpqfd1hCRd3z67qsNajpPATRVj6BnAIUO8ImlSLd_GQybuTxel3bYPFDsgtzNfcYsaaas3LFA8EreZ26mmC3gjTQwIYzLe74_F7qua_bECvL9c1qh_kwutJBferEDzdfKR_fhwK19Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb64PhowCIuvmhDVUkgpJq7v85KlZU66c1nSRk59VKf9iWSKhwlQe9iTl77b25deFa-8DDblAvJJ8jzNlrmYkAgOqyzU1GwbjzeHCZRRQK0o6lrLcp_kn6wdPgu0pIrIRY1jF9i1N0VSuSOD9f2hlS1B5UZ5gObkgiyzyDjq08_sBGqfH9kFNLwEnm832mS43iwiOOYSvD3nNnDDmsc5WShnBPNAhRSnjoGjWWHiMrC-ZlSw-M-GYDyDYTyMPxyQEGyzbQHmfnJ4lWm-YCzOgJJP7R8kaGaZfFJCLSRn33SWYSoGPgycVIkw8RKxFuCe2C3t-AuchO5aYL-jrKjNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOiWX3LizRZsJLS1nKiqK-wq7UAaGVxGexcz1IVt3EUkWWW3Ajhj9BnuwAgXpxTEcYf0ptWSWoYQEDaZgMHYDibQlymuosLE1G9OklXAsLniSXpChG1DrkTHRVJWu55LCgDevrKhZ_qJy5S9UCXTzdgld4f-Z-zm1qfx02gRZHfKQlmnLSzZkX4iJDUqn7ifofK0EKPfqC36xdA_QV8KpHQyKb5OpCCWYh3e7VL7N_114NC7wM5PxyVV0CgLQi3OjYWFPNlTNg3Iwr9dn31oj6KnQCYywpRF6U6Bb-Ma3TW8jYCXkKb0biLAdMarTEPft-bxws0MN4hqWZeHP9Uj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=lnvJZHR0bmis65hz9OgsDVV3WSHO4qu82lQVJGbYS98Xc5dIuKQTR76ERRuHciJck6unCWoL0LEg-98el6TDDi0qclrXIGqHAQOgbYAxwupt4_OGu7B1nGy6C-16AU7CegxVedUK4SPN1nxw9WwGis4lrYImJeWAgOjw3dXAs2ZbF_L8zMT2DQQGj_hkWZyE2qkiMCBs-c-LDoSrfFI75Qdv_hr4vBzyGNZpahoOTE-rPsB_jluYlp9aeTOjJe8BuVn8bGeG6WiJVzgZtuOjy6ugfxOeowmMwqfpU9V418Uj84xfvbvBSaXXUGxslE7FULuzdCgOHFJ-RxEKM685hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=lnvJZHR0bmis65hz9OgsDVV3WSHO4qu82lQVJGbYS98Xc5dIuKQTR76ERRuHciJck6unCWoL0LEg-98el6TDDi0qclrXIGqHAQOgbYAxwupt4_OGu7B1nGy6C-16AU7CegxVedUK4SPN1nxw9WwGis4lrYImJeWAgOjw3dXAs2ZbF_L8zMT2DQQGj_hkWZyE2qkiMCBs-c-LDoSrfFI75Qdv_hr4vBzyGNZpahoOTE-rPsB_jluYlp9aeTOjJe8BuVn8bGeG6WiJVzgZtuOjy6ugfxOeowmMwqfpU9V418Uj84xfvbvBSaXXUGxslE7FULuzdCgOHFJ-RxEKM685hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lo9DY6ZBc8SMrl611AbVHt1hgtqJh9smzOu9ALPfmrMBR6Ci7TkYUEe17RGU_HSaKhRQbSI4evfH81tpr_0iD5p155EuRir3-igbZfc64zxD_tS0LbFNk5kgVO3_o_U-6_kC-Ne1zwuJoVTtFCUdmijF9J4ID9OkQk8kY-PiCxnNJWxXBSEKQ3dp1_LvxtLumWXXlveMXku1DLjsVzb9OSCPqgZc7NbC0pq1CpcCpw--yFy3qUX4DJLsIo2MrtxkFhRUJLLnzlULpAUvNNXthMX83TMLtNnt3iZm1nvsdgCXUvGAGjCQShgzFLdurj5RX71UL99kqSTs_rLZ7RHpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsgVPBCGVFVZ8vz2en1DatjogRCo6aJYcsLiFfJaIqodKQ-SLXCinKhD2QAS7aMZitESYwHBGi6mdG48VBrWWHzU9EK5Y0GDzm48SoW49MycAr41Ecnvjr5jEGdIWYPSHYwId4MrtlQYc0eyPW7LZvf_vs15a72hCu58MpxmFUrLjgHdIOwnyc4uqIyx7odaqkTII-VRk23Z2K6RZRTQmE-VvOv8AN51ZpsJPj1xd4-ywPmG6cU7BtJJWBM2kFacwT8HuVLiC8THLTIG3HnOPdpqAnAv0Exty0Tj_OSwsVfbjVyyhD7z6mnwXQzuhvmM6eehwYuDrEWvjUpU3UFrklzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsgVPBCGVFVZ8vz2en1DatjogRCo6aJYcsLiFfJaIqodKQ-SLXCinKhD2QAS7aMZitESYwHBGi6mdG48VBrWWHzU9EK5Y0GDzm48SoW49MycAr41Ecnvjr5jEGdIWYPSHYwId4MrtlQYc0eyPW7LZvf_vs15a72hCu58MpxmFUrLjgHdIOwnyc4uqIyx7odaqkTII-VRk23Z2K6RZRTQmE-VvOv8AN51ZpsJPj1xd4-ywPmG6cU7BtJJWBM2kFacwT8HuVLiC8THLTIG3HnOPdpqAnAv0Exty0Tj_OSwsVfbjVyyhD7z6mnwXQzuhvmM6eehwYuDrEWvjUpU3UFrklzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gPf8Movw04ov86iyF1SwtPSQrf5gosGpYNEcOlrFhCr-_Ei3li3YYLTKJJX6LTPRmyuFxeq6ZcR4lgcIfUcFhn3NRRRNE4q8tV3RKHDOIy55xFFnOuhyYt3da7jsftIUXAY6oQFhvjLeZUTtSMKTAXVw-RU03_gYaQUGJm5hx7EkmdNt3jbvjUJqtibmsHQ5iRbwuAPEpOz_sOek_Ww_ZXDrUqUzqkz9HR2rtkDJbqPrYcoyaKAQWXiEhvzooClZjA6WWna5gfnMR-LbsNYzTNRxFR0Fr9FFl0hvOBybmmvk5-wJ6ZaqhLedVJkv_h0eCtIygkPvY0tE2hLsH04q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gPf8Movw04ov86iyF1SwtPSQrf5gosGpYNEcOlrFhCr-_Ei3li3YYLTKJJX6LTPRmyuFxeq6ZcR4lgcIfUcFhn3NRRRNE4q8tV3RKHDOIy55xFFnOuhyYt3da7jsftIUXAY6oQFhvjLeZUTtSMKTAXVw-RU03_gYaQUGJm5hx7EkmdNt3jbvjUJqtibmsHQ5iRbwuAPEpOz_sOek_Ww_ZXDrUqUzqkz9HR2rtkDJbqPrYcoyaKAQWXiEhvzooClZjA6WWna5gfnMR-LbsNYzTNRxFR0Fr9FFl0hvOBybmmvk5-wJ6ZaqhLedVJkv_h0eCtIygkPvY0tE2hLsH04q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4gZ0Wb4O9p_JHBWFneXYDQQPv8xeVzxqRKtIRj7GgtXqAESvOZXrHAIYfKLEs0qUEct5fjOnHmocpIzs8bKu1IsFuZXJarkc1WZOg2owwF2KpnoXf1Ej_h69ur0qCtV5049ZzeuUqsqy52ZMd5e6mrXbdQQ66XZcz0xbGuCKBZR2Gs1m0N5cLycguI2HH-dKr4l1-7uNdKQP6oG3dUXayzibOsU47PKS5E1pH2fMQObWYaNI1_7dDl6_XVs7MKR8GIfPCfhgqyjOAwV0C4uV28gO1rHpKbswK3saLihd7tVqugh0nZLBJ-tIO6XZgHjd1aAYuQqcadv5jVcbNZMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ZEPM8pN8PG5kZSzcHB3yiW9VKlY7HqzmGJY5539z2y-1uaCqdDPaV6U5fn7NOX4kEW8UqT9O2uX13_7doRuYE-F6t2_8j6yGxaql1ugW2r57UyTIFLlJblzzMEBnZ1OkU4HkZd8E2CW5UvDXhU4AyR2ab7gj77G_HjXi_BDKSJck1doedbTiRnrHvwRAX1zlMGGv9KqsZpfzk7IJlZEIs33EF80dte_n7s3oUHwm75vgM8yfWHMcqzYN4PRjRO1GotrF0LSPe77bPHZL_ffGZvT8gOJDEH9KdfAT4AvEb4cBJYYuu6OE1IqVDV8wTiFediK2J2WscFzULHqYSvzFyq3E4EkfQFER14wKO5aVQnJFGdfPm8K4B_VEPQmw_0FQcFTVOqKubDuhbnNXCaKx4_1aoGXlm20uwhMZDObexQP17sgMIQItGzO-RYOUCJC0DzkujaKGJyJKZV7DBvpWyS-ViBTiZOMaJmFIahipnXU7EKZowm0l57xgBBxePyErwmk4_gcpqZq-ieADoCFeGgRoAYfGCgGQAtPPxfFgZggWg96P00fi4s8dAdwloQkWCQEh8bkKVgO7FR0GoEaT2xEhCOkvejMJosp4BbuzfSTvHRPIg9NY6z7KZEA2J36BFyWbd5BbMaKMyPmwUaLhwY-yhotV-sJdFmX_0MJEbXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ZEPM8pN8PG5kZSzcHB3yiW9VKlY7HqzmGJY5539z2y-1uaCqdDPaV6U5fn7NOX4kEW8UqT9O2uX13_7doRuYE-F6t2_8j6yGxaql1ugW2r57UyTIFLlJblzzMEBnZ1OkU4HkZd8E2CW5UvDXhU4AyR2ab7gj77G_HjXi_BDKSJck1doedbTiRnrHvwRAX1zlMGGv9KqsZpfzk7IJlZEIs33EF80dte_n7s3oUHwm75vgM8yfWHMcqzYN4PRjRO1GotrF0LSPe77bPHZL_ffGZvT8gOJDEH9KdfAT4AvEb4cBJYYuu6OE1IqVDV8wTiFediK2J2WscFzULHqYSvzFyq3E4EkfQFER14wKO5aVQnJFGdfPm8K4B_VEPQmw_0FQcFTVOqKubDuhbnNXCaKx4_1aoGXlm20uwhMZDObexQP17sgMIQItGzO-RYOUCJC0DzkujaKGJyJKZV7DBvpWyS-ViBTiZOMaJmFIahipnXU7EKZowm0l57xgBBxePyErwmk4_gcpqZq-ieADoCFeGgRoAYfGCgGQAtPPxfFgZggWg96P00fi4s8dAdwloQkWCQEh8bkKVgO7FR0GoEaT2xEhCOkvejMJosp4BbuzfSTvHRPIg9NY6z7KZEA2J36BFyWbd5BbMaKMyPmwUaLhwY-yhotV-sJdFmX_0MJEbXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKq_k99utIzbj-nt2y1WBhIFiLTISVAXHA14FE-l6nAJJO5EQUQ2xwKSy_oFHKhAFfwFDsFjM3tNbeS5OXFFw63I8aadNMHgUYp272vaqpxQboIy-0O1BzoydCtXPUkc4ixLK9vTeX_W3vdyy5wEC2vN7HiotQalRujvxzQtQeGKdFYy1PSlNmttW-mmF80nCF3pan1TKaJtSKh8E4KtShloQ7oRLzrD8xEd8JiVNP6piQ7phw0CHlWkmFH32IHrg6iGi10byEG3_noN9jn_PFp0pMxsD49wJj4EVUw0C5czZEgCCWC7i8i5kDksK0n6SikADE3wUvJHmNMoYgxJOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=aSITL3m9OeviUGFub8n7aynISUwaZ0wiS9lthb8pPfsAgTK84aF2kWmjKk2g3zpW-RQIsvFpL3WF2waPZiPecudLBfBIEOaglqVig-mgIhJN8SGGbfqqsWUk9Lga2Xs7uGbT6qRnTeu0r2dnSL44bAiWPGhjO7IsVMsLVuwZKEsIl6ItCobqX_vrJZ26eWXcEVbNYJOvKrkj0lphIv_lfIeqPzlHxowf1poYxVBjVczzGh24QvhhL3rGHhagX2ly_zjT2vyc6TnT_lVG7t1Fv2b01i_F1zArG2e-zBiQFKCZJWiyxWhHeMAtUamjMw-y4pBo-t33WHIxSyzYWj5upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=aSITL3m9OeviUGFub8n7aynISUwaZ0wiS9lthb8pPfsAgTK84aF2kWmjKk2g3zpW-RQIsvFpL3WF2waPZiPecudLBfBIEOaglqVig-mgIhJN8SGGbfqqsWUk9Lga2Xs7uGbT6qRnTeu0r2dnSL44bAiWPGhjO7IsVMsLVuwZKEsIl6ItCobqX_vrJZ26eWXcEVbNYJOvKrkj0lphIv_lfIeqPzlHxowf1poYxVBjVczzGh24QvhhL3rGHhagX2ly_zjT2vyc6TnT_lVG7t1Fv2b01i_F1zArG2e-zBiQFKCZJWiyxWhHeMAtUamjMw-y4pBo-t33WHIxSyzYWj5upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT_y78rza1ZRWa-1ndWljYOgSqvq_i1eI1RjuR0zygvB7n69CVlhj7dt5NdJuuRrp4Q3QGgYZgGIdWGrubdPjoct1JaiUDucZR6yefpeu4RJ0bT7UMoQogQtb8k0DN-kx3Hq0skIp5jhO04DTwCNbLujCsUY5OFsKpav8kIn9Gp5EgGH_i0U7v5DfNWOPsg6d99fhgNfunfOxDs8sjlnUGAseKCwo6NscAl74bh1_rAMeQW9oCcemhvzED5S-0VL0-0RYJyzzs4kHaE5TFROBgidPt2f-MPplNp-jhCKxExJJNAe60eZIeyo3Za_ciDOLM1f5GmisQ8s9nRofW-eWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfjAlK1X1Gdji8TFBYjeL-7NGimBLQgK9Q0_KNVYE6-YrUvMgkE86TMzXYLryrkeMXAErwYJ-q6boOoLQmmnuf0aBRBEAs7d31V6Tf6L-ZQ7mvrDiLOQGT-xbNn0S5gPS1xCBC8VZgrTtjH5Wv32iscCjy-HaPUVTs1jtqo7t37UfZmB5ewKPCujOl5_OHOBAQQmc8m_b2wZRky4QXcX_-bl79mRTbHeJwUf6AeMSlvTivMN8a2_r5Yj5S0CG0QahciMaD2nReEZdTT8clGDzq5zmdnYuqvBTbUNnNx6n8l1guecwzul9H_krrCTL9LITu_c34WlQ4qbtfHjZtVb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVJwg5KHjyc3HcyR1SeMNDxE5pSsY4OIsfpuOMqAPehMEumq9Gt1xPXjlez3EjpkibV7dAFLkMMxEzRk_vc9wVWuJq_d0HMZZoG3hPfs_K8XKc_NJ5ZnUSprzlnVDbt3ggC_6GYpOeSop6jWv7Gta3J1SWJP9Xga3La9HLMe7iekIuAoo4HnE_7dm0iC8j5qAXp-_aXX7zzaQtJUdspVLnxXiQEotehVy-vAYyilM_WfvRrTW9JxK76WY6G38fTarLXpKmMBg0ya-PdGobd4vBk_bbVj3KVwFlajx1op-ylHLhMLpc7Zt1aX6ThFI_VM5QNLLJzUWmED00-LSXNXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRlr77yulRwanFnQCxh0NIaXzqcHYapascIsHt4gypR7J4D5I_4ApMcYFSNQWUt8RmgoQL9OHbkZZf_6J_MfKBtNhCoXJBQWu61xe_vuxqHsQ496x1cX1Jz1nAevW2GkFM398bRYdhrg-Hl2_TFLFeOzKYk-7iFWSCEBX7smFlHjLbVFhzMcHMNiRXO_p6g-QATyQOEa1_EbV2ETpPpj-nYcI-wSpTD8Ff2kUWXFVlRr5hDNu84ulrdsib2CEC-wywlMWOgCTziWyn5QT6n32no-_Z_C4G7sKbDiKfStiXnOw_9WYBOhImLe4kTq1OMm92nzHW-cl1LikG1ZT96Ngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuz352uXTxdNKBujxIyVE181k6PoJFEyPKWi6dkYF7Slx4UEa6NalE3bg5GLWFIc6BNuABfpic8EDDa7yKsbI6d3DQ7SScRKqlJzWA08gOqQSWoeJhj120Z8EozpAnLrDKzDr4dmjnUhEjkab5aSj1030tHYT_9qswEQNJAaPGC3xnqY43shqV3lt5r3lqoWbpAzdTp6KX0ppoy5gMtszIymK2xlFn5TWRqmZYBHsGnvz674wZUL_B-JdxeeuBO3j4EY0rpydkXgzgvYblGFKb0sOv41701_WQKHA0vYn9PlVXtMMP7BfqpWtLjaTBDT0bM_eUCCEwwktz3tPtWOV1mY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuz352uXTxdNKBujxIyVE181k6PoJFEyPKWi6dkYF7Slx4UEa6NalE3bg5GLWFIc6BNuABfpic8EDDa7yKsbI6d3DQ7SScRKqlJzWA08gOqQSWoeJhj120Z8EozpAnLrDKzDr4dmjnUhEjkab5aSj1030tHYT_9qswEQNJAaPGC3xnqY43shqV3lt5r3lqoWbpAzdTp6KX0ppoy5gMtszIymK2xlFn5TWRqmZYBHsGnvz674wZUL_B-JdxeeuBO3j4EY0rpydkXgzgvYblGFKb0sOv41701_WQKHA0vYn9PlVXtMMP7BfqpWtLjaTBDT0bM_eUCCEwwktz3tPtWOV1mY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=vhWxNHF782HYtwYAA2kAdy0AZkOEKfyi0NNym2uXdNakXr8rHc5kDInQCS4yB0cRhijnozJIe-Uu6sHYFyPp-1x_n1ofQPIZK1JWwG_YT8Y2DkW_zZF-gIb3bLdBxjh7Hm3eaP4uR6x1Vz84r9DX37orrohttOpO9lQrP7AcTcPb-123olbK8UjJpsRtK24TybLuGlhHBvMuNiOfzgseW6NTpLRlQdzps7b1L1IaJCd-GsCWqWiRhxBHQbt2gOkx5rNNkP30OzuNyUCdICK-zdjh_inySJjturtXPk8rB-4ELm58NI9WaJJRAWnwAJdVUz5mM5I_k6nFjJerEXxynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=vhWxNHF782HYtwYAA2kAdy0AZkOEKfyi0NNym2uXdNakXr8rHc5kDInQCS4yB0cRhijnozJIe-Uu6sHYFyPp-1x_n1ofQPIZK1JWwG_YT8Y2DkW_zZF-gIb3bLdBxjh7Hm3eaP4uR6x1Vz84r9DX37orrohttOpO9lQrP7AcTcPb-123olbK8UjJpsRtK24TybLuGlhHBvMuNiOfzgseW6NTpLRlQdzps7b1L1IaJCd-GsCWqWiRhxBHQbt2gOkx5rNNkP30OzuNyUCdICK-zdjh_inySJjturtXPk8rB-4ELm58NI9WaJJRAWnwAJdVUz5mM5I_k6nFjJerEXxynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=UPaUVpShZrC3QL_ozF7TCR_8hbz_OGQrzEkIJCVmAEUxgPNAU2YiNbgopFQlvf57eU3jncwCFJlcQW80dML9V7X-LcfsW0MFIW0mci5G_IIWWnYRuYTPH2PPmB5a8QQkE5P256ZkC3zL162zMRyovn6i1nRf2F-avkybmkysoV5LucgOQ0VZ5YmHuawUc5ZPOzoNei-sKYyeqSH-ZCVZA2Q6llZX8yvO8f_mmEnmAIhB19E6Em3B4Y0QlbNS4ZZEu5efokO4N0MtWnoGri5RHmcDrknRTjyBXi-YEFx-I_-Jwn_JIYcStCI_wVMPeorPSn5OVFFpZORB9SvjBz0ybDe8ONniFRMUTT0jbOavELD514lzBo92CDVLwWfDa6rbnU7Cv_m6TBofW0TG96gBq32QpCDIyFl5bdREvOAwZMuNafZ7hby5oaapl-cObaM9R7WJPyftAq4MtN8BUNpTfudsHXc0LsNqz6-2bmmvmLZvmBt0Wf55zDprPyLf4Ozi1dp0cZvIMiH2bSZejq7iHy-j1-77EhEsLoCiWzMvgpspmbjY7Uu1CtPD1a---fic1-2wbR0QRNc86JUVPnjUfhjfDn39ILTcBKwopLfpglbk2RBjgGV7yeC8PNqRne3QDnahAwS1ZuK9kAgnFEJ2cCSfSFljwjJLtWouCRXfC2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=UPaUVpShZrC3QL_ozF7TCR_8hbz_OGQrzEkIJCVmAEUxgPNAU2YiNbgopFQlvf57eU3jncwCFJlcQW80dML9V7X-LcfsW0MFIW0mci5G_IIWWnYRuYTPH2PPmB5a8QQkE5P256ZkC3zL162zMRyovn6i1nRf2F-avkybmkysoV5LucgOQ0VZ5YmHuawUc5ZPOzoNei-sKYyeqSH-ZCVZA2Q6llZX8yvO8f_mmEnmAIhB19E6Em3B4Y0QlbNS4ZZEu5efokO4N0MtWnoGri5RHmcDrknRTjyBXi-YEFx-I_-Jwn_JIYcStCI_wVMPeorPSn5OVFFpZORB9SvjBz0ybDe8ONniFRMUTT0jbOavELD514lzBo92CDVLwWfDa6rbnU7Cv_m6TBofW0TG96gBq32QpCDIyFl5bdREvOAwZMuNafZ7hby5oaapl-cObaM9R7WJPyftAq4MtN8BUNpTfudsHXc0LsNqz6-2bmmvmLZvmBt0Wf55zDprPyLf4Ozi1dp0cZvIMiH2bSZejq7iHy-j1-77EhEsLoCiWzMvgpspmbjY7Uu1CtPD1a---fic1-2wbR0QRNc86JUVPnjUfhjfDn39ILTcBKwopLfpglbk2RBjgGV7yeC8PNqRne3QDnahAwS1ZuK9kAgnFEJ2cCSfSFljwjJLtWouCRXfC2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=JFB9Nr4dchws0lCCTgEthJjpmvwo3FO1SVWag_Pc-LsviVx8dnGdwAhCbllf5UPaduDnSBnvE1UfaGHUuSXU5l2JZyNVcplEdAO3y5MZOeaZQyD-HGwAXV5LKZBDDnJWw7FTnG2xJlV4iH9SKDO_WfFxFf60SOrN0W0HOqfOFdRXykqKtgTtheT6k2u4_-QcM-blQg_4w23svSE4ylvDOhH7-PPnvjOYNr0K0AjjzFKz8H7GGBYhtF4XqwcQRum3GTzbpcseooo1uxLGvypOmf6IPhua9zKm0na8hmeQkECzFTJWRtYRIjZDrENLn5T2otuW6iOmYZdTxvMyu5YkXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=JFB9Nr4dchws0lCCTgEthJjpmvwo3FO1SVWag_Pc-LsviVx8dnGdwAhCbllf5UPaduDnSBnvE1UfaGHUuSXU5l2JZyNVcplEdAO3y5MZOeaZQyD-HGwAXV5LKZBDDnJWw7FTnG2xJlV4iH9SKDO_WfFxFf60SOrN0W0HOqfOFdRXykqKtgTtheT6k2u4_-QcM-blQg_4w23svSE4ylvDOhH7-PPnvjOYNr0K0AjjzFKz8H7GGBYhtF4XqwcQRum3GTzbpcseooo1uxLGvypOmf6IPhua9zKm0na8hmeQkECzFTJWRtYRIjZDrENLn5T2otuW6iOmYZdTxvMyu5YkXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg35OLNEWPmuwTzVGieHdi08Z5DfhfGOKDLnjaC03Pp1RmR8CWh0XEr6KhPdqqZcYMHDakE03GPfJPProOL5EK3XbqGQUP_r4dD2vz72pOlNwCAJJ7L_6yc9VP6XPujMONyyBAxQROH1hAWzuwKkWlWu0ikDK__gTFmK2DBm5PqgYuFL9KzBdP7ySz7XHVg1vfLBQnyYMBSWuQHlkmrBP9cNGLMIWcix_oFSAuGEtJkPQu2RKog_ExquIAZt56Md74UMw6u_WO_xpGavL8xcG03XAzPsJu9KIygiGpXP9OZi3c_76c-hyopDEhDy2N4U93Yw9fROM_xuvCybwc5sWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=TnI4MLyJ1o6x_EWDr_LR8TsLuHAkdel16izPxNJ-2Cnf1iariCJZMN85C7TlrN5cOVmIUhLr7h2IM6AWWlbeKC63ohCv0dZT7qsPL-1X7U29d3dA8-1G_4kKEm-ri4sWmnGvSPdjdFCWO4IHPAvqN5HTdaZbC2AQ8g83NjePWS5djVTCqzheR5oU5b4A5GKPwClQayRToshh3F8hlg3bTfOmGKnI67SUhbegQchfgx5JWHdSmOn0oiVYDbwzaFIuVMLYE_cHotZkqaLSRTLbe7zl9d5C5-KJsW_zKIh7eqPnwBH4K7E9m7HnZwLWLht77KhIe-ywSRi2RGyIRvA-AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=TnI4MLyJ1o6x_EWDr_LR8TsLuHAkdel16izPxNJ-2Cnf1iariCJZMN85C7TlrN5cOVmIUhLr7h2IM6AWWlbeKC63ohCv0dZT7qsPL-1X7U29d3dA8-1G_4kKEm-ri4sWmnGvSPdjdFCWO4IHPAvqN5HTdaZbC2AQ8g83NjePWS5djVTCqzheR5oU5b4A5GKPwClQayRToshh3F8hlg3bTfOmGKnI67SUhbegQchfgx5JWHdSmOn0oiVYDbwzaFIuVMLYE_cHotZkqaLSRTLbe7zl9d5C5-KJsW_zKIh7eqPnwBH4K7E9m7HnZwLWLht77KhIe-ywSRi2RGyIRvA-AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu901E0bqnnPX98aYmwDLwuRkmC2TYJ5KRnDj5G5Qj5NX4YDm5x3OePuCF63dzKi4JDxqOm8L0cKER4jYdnjkN-4qIRArBUFKOHVOcPLpjJ2RZuYuX3JYdYThu0X1H9yGem1VREIwJ6HYZNtrsaGEXMT5ulFKcf6yNfishXiMBf7Q0a-qf1OyPeHzEdKvLdbXnAwv6q0PwcEU9pUwmIqlVRTjOMr-JnpvIpYVcP7gqjAt0sGjfCUuVy2EA6TSsiFmoXaq6qVf-6ecAuYgSDO-WLKwkibDu7J0EMBOZ1Phc0JeFVP3ZzIyhMvTNH3b30_tbqEhVEYjl_xJ3BBsBGmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=cyGFORnrkluhouVRLVFVB1Z-kkAUhvYPpLyqKMfwwxymW_jtwzQrhuigF8Gn4KdXu4QwEZ64F5V75BzMO_tV2TBc3PVLXbmwqDcVfZuRySI2f5ELuYuMvD5vEnwhJQ94VVRFhP11ax_n6uskODwPENYsqziTFs234wmYDKO4gJg1s-O2Os2qx04aIEddKel3gAfF44rTBIYkgtOC_jpVaqiZxmCWaBO0uywao2GnvvXYIMbCGLmKUtKSN7mWm64XaxURVjSqHlbD_Cdcf8brUTOVBBV_OgAkLsGoDIHQz2LDMI-J4ndqkdT5pHpaC5c74Py3jetWLNTagIF0RKKcMVICD6I_GM8sFExkgurPJPzvPoyuiMWLXJOADnLu3ZCoT9X19ZxqffMWJm1MEdvhniozhjSrYg_ybfsr-MzBUTUKunjkEw-jythXuFCqH_exswRiyQjgoTjObwTooDdScnzez9uhpR-EJEPBlfIj72ZanpuIGcEmzZpJiWbM2_PHi768XxrZ1S66XJ5BA5YDOAv14NJcnTpDDDJTdj_03uaW7WlVZIWRr68gHG4EphKNQVVqIME3aWujCCo6utXB6-zlMnUvgtK3_MIcbIPwH9-4hTB5Q-eRmVPsXVuXnTnnePNdimCziC-Fe9Qwp9aLbrHNRDmMzrZyi8GHGkbiZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=cyGFORnrkluhouVRLVFVB1Z-kkAUhvYPpLyqKMfwwxymW_jtwzQrhuigF8Gn4KdXu4QwEZ64F5V75BzMO_tV2TBc3PVLXbmwqDcVfZuRySI2f5ELuYuMvD5vEnwhJQ94VVRFhP11ax_n6uskODwPENYsqziTFs234wmYDKO4gJg1s-O2Os2qx04aIEddKel3gAfF44rTBIYkgtOC_jpVaqiZxmCWaBO0uywao2GnvvXYIMbCGLmKUtKSN7mWm64XaxURVjSqHlbD_Cdcf8brUTOVBBV_OgAkLsGoDIHQz2LDMI-J4ndqkdT5pHpaC5c74Py3jetWLNTagIF0RKKcMVICD6I_GM8sFExkgurPJPzvPoyuiMWLXJOADnLu3ZCoT9X19ZxqffMWJm1MEdvhniozhjSrYg_ybfsr-MzBUTUKunjkEw-jythXuFCqH_exswRiyQjgoTjObwTooDdScnzez9uhpR-EJEPBlfIj72ZanpuIGcEmzZpJiWbM2_PHi768XxrZ1S66XJ5BA5YDOAv14NJcnTpDDDJTdj_03uaW7WlVZIWRr68gHG4EphKNQVVqIME3aWujCCo6utXB6-zlMnUvgtK3_MIcbIPwH9-4hTB5Q-eRmVPsXVuXnTnnePNdimCziC-Fe9Qwp9aLbrHNRDmMzrZyi8GHGkbiZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=kKmYwcoLnneSKa7bx_IoixAUhg8qpTXZYgoFZbucHtqrb4bOVwQRRL_OHse3BfBxdPuLJ8D4FGKpKd2REMpNR4QkBiRPo3hggKFV5Bdd6D_gtBhBSItu6alHnaFcWRUNGkEcfksYIVgvzeCrd6aIaOSIow8irz3pIobT7af9NifMv3oaBYaPfKg-9ow3GuZWEioIdfgKK2njeUMKOnrJUX_WDInv9yPzUUS16cCNqoE90kf5H66Zu0jnUssAZeDrSrrdj4VGDq05cnzuBfdBz96o82UsWfHDrM_y1qnUdjGP-4XSv5jGA7Xnceyhujz_c9wzMLLwOPNcq2xc1pFuTb8Vu8vFY8ugNc_Kxq9dykbIJoELdRiiAGopmx4fQi-ZHPPc6GJu5ZJjRkXHVGgcI6dlMpwmIBwZmhEhcGXTL8tUHxhsac1TdOXt18ywCnYZE-qvB4iUvoBkZJyuqn8iTRr5MN9KJLHclliM979bXaE6FZMCSHhwWFIGDBVIpV5IUUGCmsE7TnFk8GKpWw85EnuDC90oBPsJtC-3Gs5UOCyCkMeZinLLp2xqzEPv4cS8_lZafDd0MpgYFRYTMZBWveV3HPy-HtHHkGSYEmdU6yrxJ095M7u0TaBu_r587ute8YVrhSmKR7FA1C5BVnZ5nKZZsvbz_qLddeYlcWuL3Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=kKmYwcoLnneSKa7bx_IoixAUhg8qpTXZYgoFZbucHtqrb4bOVwQRRL_OHse3BfBxdPuLJ8D4FGKpKd2REMpNR4QkBiRPo3hggKFV5Bdd6D_gtBhBSItu6alHnaFcWRUNGkEcfksYIVgvzeCrd6aIaOSIow8irz3pIobT7af9NifMv3oaBYaPfKg-9ow3GuZWEioIdfgKK2njeUMKOnrJUX_WDInv9yPzUUS16cCNqoE90kf5H66Zu0jnUssAZeDrSrrdj4VGDq05cnzuBfdBz96o82UsWfHDrM_y1qnUdjGP-4XSv5jGA7Xnceyhujz_c9wzMLLwOPNcq2xc1pFuTb8Vu8vFY8ugNc_Kxq9dykbIJoELdRiiAGopmx4fQi-ZHPPc6GJu5ZJjRkXHVGgcI6dlMpwmIBwZmhEhcGXTL8tUHxhsac1TdOXt18ywCnYZE-qvB4iUvoBkZJyuqn8iTRr5MN9KJLHclliM979bXaE6FZMCSHhwWFIGDBVIpV5IUUGCmsE7TnFk8GKpWw85EnuDC90oBPsJtC-3Gs5UOCyCkMeZinLLp2xqzEPv4cS8_lZafDd0MpgYFRYTMZBWveV3HPy-HtHHkGSYEmdU6yrxJ095M7u0TaBu_r587ute8YVrhSmKR7FA1C5BVnZ5nKZZsvbz_qLddeYlcWuL3Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=RT3PEQQkkZ9mH3UTY9kJC7VRQrEofS4ZJmz6ud7FWZU0VzxeZUIZFakUAymKhqx_EQnkGCyjCmWMQF0vEoFxxOU98ZpWQPgj1Hs7wYFP6vaaRIrPOG9zZp7IFZgo5p4Smc26hF4H2X9TI_vHln9WRuTckUrwjeYcQAfYrgrMf1SHEv44Eo-G5qX8VuchfpAAlGTwrh7QFlT7hY5K4uh_qm0ySvy3up2RXLGDSizrk7AOwpZVv4-a-Rq7r3OOwzhstirVoSdOrG-d7UUx4RYA8UepYtCC8CB0iTKoRG1NKfswN9EEx-vMAHFPl05Uxhn60623aYsoPQnp4uIfxMou8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=RT3PEQQkkZ9mH3UTY9kJC7VRQrEofS4ZJmz6ud7FWZU0VzxeZUIZFakUAymKhqx_EQnkGCyjCmWMQF0vEoFxxOU98ZpWQPgj1Hs7wYFP6vaaRIrPOG9zZp7IFZgo5p4Smc26hF4H2X9TI_vHln9WRuTckUrwjeYcQAfYrgrMf1SHEv44Eo-G5qX8VuchfpAAlGTwrh7QFlT7hY5K4uh_qm0ySvy3up2RXLGDSizrk7AOwpZVv4-a-Rq7r3OOwzhstirVoSdOrG-d7UUx4RYA8UepYtCC8CB0iTKoRG1NKfswN9EEx-vMAHFPl05Uxhn60623aYsoPQnp4uIfxMou8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ZZHH2KA-_KuueVTcRKPGyvlN-EW55qW6uKovJXnu_ZXsJqRMdv2gYzbim2rWTXhR6X9iSEcmUcXan62zVygTlCGmNSyI0ovR4H1yUaTY8w-1aElfOcXZfl-I7r1I7zqexbiuJqhpKhUKcJgOUVIu8lmX0Rh-RYjdAV_zAIu7Ip1gr8oylmonxMPtD9y_j4BngwOvqaVI7--bo_v63T8qg60ZbDHujtz0IVfSdrhsJ3HC4KsrpgL2TOacsgu5ELyuUO3xm3YNQFYJWP9ZwbzEWAqoQDJmgulwUttdi0GZrnpCDmesY-0gl8x-ARxI3pnue1PgaitwQzTogi9XVs4ffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ZZHH2KA-_KuueVTcRKPGyvlN-EW55qW6uKovJXnu_ZXsJqRMdv2gYzbim2rWTXhR6X9iSEcmUcXan62zVygTlCGmNSyI0ovR4H1yUaTY8w-1aElfOcXZfl-I7r1I7zqexbiuJqhpKhUKcJgOUVIu8lmX0Rh-RYjdAV_zAIu7Ip1gr8oylmonxMPtD9y_j4BngwOvqaVI7--bo_v63T8qg60ZbDHujtz0IVfSdrhsJ3HC4KsrpgL2TOacsgu5ELyuUO3xm3YNQFYJWP9ZwbzEWAqoQDJmgulwUttdi0GZrnpCDmesY-0gl8x-ARxI3pnue1PgaitwQzTogi9XVs4ffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=N166U3G23LuQQ-M7Fj3KLgLoZ4N-JpIVzxbN83x9Wa4QG-QTBv1eS_nrfHUxyZebDGRLDfI5fGXc1_nDDQB1ZyfdEFgytpZEiZmF4gl_yg7LEKRSWlXx_pN_sNKogqZtBHDXHSxGSYGzbrRJ7DV_IaMLIzH_o0zychaH1glCZTgLtftJa_U3P7PFMLJFry4Vo5Q9XzM2D_UEQ7b4TjHhAWoXckhkXWaRcOZUGodcLgiz9h61O6WCVvXsWW2bCm7M74Pd0k-PA7Oafb12iYIi6hkxn1jAToFaT0zayU1C4eBS2Qpyjm7cWTmiekTnFnS1rDiMdX028QMlG28M_mj4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=N166U3G23LuQQ-M7Fj3KLgLoZ4N-JpIVzxbN83x9Wa4QG-QTBv1eS_nrfHUxyZebDGRLDfI5fGXc1_nDDQB1ZyfdEFgytpZEiZmF4gl_yg7LEKRSWlXx_pN_sNKogqZtBHDXHSxGSYGzbrRJ7DV_IaMLIzH_o0zychaH1glCZTgLtftJa_U3P7PFMLJFry4Vo5Q9XzM2D_UEQ7b4TjHhAWoXckhkXWaRcOZUGodcLgiz9h61O6WCVvXsWW2bCm7M74Pd0k-PA7Oafb12iYIi6hkxn1jAToFaT0zayU1C4eBS2Qpyjm7cWTmiekTnFnS1rDiMdX028QMlG28M_mj4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PPs2heaIpbaBnhV4NYzAEY4jf_edOj7Tsv6QAOSeEYxaBL1MvG8ZUVVzxXg1kwPUtErx7Izx9QvsH7SoCaQQztU_yTxTD5SZcrTwRCbNuPtgD6CZY72U-0tXJOgQHWQv5I4Vttl_o_l_iR220qxrE2FgP09MRsHzjqvocboMLOqeqgeCagiw3XvsJGZQn3g3XJu3LBy9c6ohFTi943H8D6mafoKE69vGOkxZxgyR7xIuJk4oQPJ-Sk5he3FCvakuWlnJe3PhTA-l_qi-o_YdQ7Km8W3zmgPYqpVRgJc5v_EHSLcjgWmADS0BOFnXr9LAUNR387vkdgetAVJ1yIrcdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PPs2heaIpbaBnhV4NYzAEY4jf_edOj7Tsv6QAOSeEYxaBL1MvG8ZUVVzxXg1kwPUtErx7Izx9QvsH7SoCaQQztU_yTxTD5SZcrTwRCbNuPtgD6CZY72U-0tXJOgQHWQv5I4Vttl_o_l_iR220qxrE2FgP09MRsHzjqvocboMLOqeqgeCagiw3XvsJGZQn3g3XJu3LBy9c6ohFTi943H8D6mafoKE69vGOkxZxgyR7xIuJk4oQPJ-Sk5he3FCvakuWlnJe3PhTA-l_qi-o_YdQ7Km8W3zmgPYqpVRgJc5v_EHSLcjgWmADS0BOFnXr9LAUNR387vkdgetAVJ1yIrcdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Zg287Z0s31N0FjQfdXxnTmC8ddbUW_UZ827-SbLclDkJkUwvZGrsP_L1lb_Cv1Ypmm0AyamGktFEGwTjNRQDwM4nchUDL2bveBIP1j9PKYIfFv_AY9Ox5-Iz85A-4DiAeE5YYh3iA4F9Oc03C3lqOso5r3NO7bv5HlOfTxlXSCC1K9v87-fMz5jylqmPWguT67NZqb9EUrdGh2X36f4lC1oKrG2qdjQcKw8rUklvbulSRQcPt_5s0ZfFk9Kwev12gGl8WWqK-COwrNlntFRR6hF0U_4_Q9IBMpBIt6-_xrWMq5Eo778WLcOuh8LG2Ggm7ZvmthofpmL67fYMmiWEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Zg287Z0s31N0FjQfdXxnTmC8ddbUW_UZ827-SbLclDkJkUwvZGrsP_L1lb_Cv1Ypmm0AyamGktFEGwTjNRQDwM4nchUDL2bveBIP1j9PKYIfFv_AY9Ox5-Iz85A-4DiAeE5YYh3iA4F9Oc03C3lqOso5r3NO7bv5HlOfTxlXSCC1K9v87-fMz5jylqmPWguT67NZqb9EUrdGh2X36f4lC1oKrG2qdjQcKw8rUklvbulSRQcPt_5s0ZfFk9Kwev12gGl8WWqK-COwrNlntFRR6hF0U_4_Q9IBMpBIt6-_xrWMq5Eo778WLcOuh8LG2Ggm7ZvmthofpmL67fYMmiWEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=VYW4jXhmpk45SWRcHNKrgLqoJDArY1d6bQ3I8xWfxX6pwSPWIGRG_-5wERSg-UcbDf80llo1ZondWUoPbplDWmxOSsDMjQG_MPy76210ybUmb0voGp620zmO1xiC0kPH_dsdEi-prV9943OBK2-_Ji-IaxKZS986qdidEoRMFu2NehVyBT6aBWlQzGVmcmy7s7To47Y73g3K1y1g3Pu5iPVZHZf-ho9SgFUNJnUGaFmNuPGOYvQFaH4b3sdvZLZ3-PTDvTcYEtI2AuVG4nBgHokU6XRZlUYRtS2FZlHRWNqubpJCE0pj5_2F7yR2dIqUo6hfN20KSQsK6-oBeJrrfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=VYW4jXhmpk45SWRcHNKrgLqoJDArY1d6bQ3I8xWfxX6pwSPWIGRG_-5wERSg-UcbDf80llo1ZondWUoPbplDWmxOSsDMjQG_MPy76210ybUmb0voGp620zmO1xiC0kPH_dsdEi-prV9943OBK2-_Ji-IaxKZS986qdidEoRMFu2NehVyBT6aBWlQzGVmcmy7s7To47Y73g3K1y1g3Pu5iPVZHZf-ho9SgFUNJnUGaFmNuPGOYvQFaH4b3sdvZLZ3-PTDvTcYEtI2AuVG4nBgHokU6XRZlUYRtS2FZlHRWNqubpJCE0pj5_2F7yR2dIqUo6hfN20KSQsK6-oBeJrrfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=WMStd-amtF_cx6Kvtmqyc2b83IzQaC-3zNQnsL3n-7AbWpZU2wTUYE3FQxpTEID-MS_UTEnmM_BYz4mTYGFWb75JaRE25Chbc_nbm_6oSnDRZ5OPaflwSWPEdD2IvMiHeoIzLEZplHkxQYQpIuscZoSchB1Q2Gq3Wze8iiwYHJJWkwSIYraLhBk6ih70iV4-X3TMUq22UnnUwFu3NS4JeqbHdGYF49FaBtSV05K2-XKu7mYd7HSQVee7PSsCtc6k3595Yv2J2o_mS79rH1zFQAmWIt-HhpU3jfDGiDTTBlE-HM6e89sVV4S2iNHrZcWqQtkPTAx2dAzkd8TzMROlFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=WMStd-amtF_cx6Kvtmqyc2b83IzQaC-3zNQnsL3n-7AbWpZU2wTUYE3FQxpTEID-MS_UTEnmM_BYz4mTYGFWb75JaRE25Chbc_nbm_6oSnDRZ5OPaflwSWPEdD2IvMiHeoIzLEZplHkxQYQpIuscZoSchB1Q2Gq3Wze8iiwYHJJWkwSIYraLhBk6ih70iV4-X3TMUq22UnnUwFu3NS4JeqbHdGYF49FaBtSV05K2-XKu7mYd7HSQVee7PSsCtc6k3595Yv2J2o_mS79rH1zFQAmWIt-HhpU3jfDGiDTTBlE-HM6e89sVV4S2iNHrZcWqQtkPTAx2dAzkd8TzMROlFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=GD_aj1afamU2Ri5tX7mVTK76cyLMLzI_OaHKOuMDhAHjoPf_8_sm0PkYdqNPuv2wzOFZj5dIDTrLSupzJd5ZsYFg4LCDIujdaivs7-K6kWDLuNGHrzVxv-ePE6-_EWAFpZ_q4BrDDt0MrIHecpfzkM8kGRPPfqrhVPeJOViiOhoiAEHvM_TtgKFhsHe19WRpgTh5R9y7W5zuPnjU6GlJQsvz3UBn2kmdASkmkuC0jfZ32cmfdiUT5xkalayxGW_Jo70AMoGCq7NyHfOW-e8EY1l-jBUSOv-CKpZ88rV0WGTEAhrNWsKeJyeVi_3dWLqFnHMKLWZXrPfAPKI0OL04iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=GD_aj1afamU2Ri5tX7mVTK76cyLMLzI_OaHKOuMDhAHjoPf_8_sm0PkYdqNPuv2wzOFZj5dIDTrLSupzJd5ZsYFg4LCDIujdaivs7-K6kWDLuNGHrzVxv-ePE6-_EWAFpZ_q4BrDDt0MrIHecpfzkM8kGRPPfqrhVPeJOViiOhoiAEHvM_TtgKFhsHe19WRpgTh5R9y7W5zuPnjU6GlJQsvz3UBn2kmdASkmkuC0jfZ32cmfdiUT5xkalayxGW_Jo70AMoGCq7NyHfOW-e8EY1l-jBUSOv-CKpZ88rV0WGTEAhrNWsKeJyeVi_3dWLqFnHMKLWZXrPfAPKI0OL04iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=iE4a4nSKRn2QWDoHPp23Wwvxh2za83YbvOVgLKZQUS_bF6SVZ9TsJwp5N-DuKXIiWbu4Qq5D6p4S7IPibD_ZZzcXyJpypEtqruEJ6DdSVrgl5OjpVcfq3xtSilvLzW5kSI0LeG9DvYR7QYl-qeRdbLaZU1ZABHV1Q5gWnpaywWuJ495eodIvuvdmJD7LXDLd6VNG3twOFfWyHwwFSpFy_xq1kjL0DMatSwSltfCibv3QV_soJQaNuNmXf-2NJAUGF3eDEhi4v9O_L1_TaeV5lUrF-v7GIRR6GRw-kUTXJuemRfu-cBqmGldqU2xP5xrkBRAzRXRtSeqgD9HGlqxE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=iE4a4nSKRn2QWDoHPp23Wwvxh2za83YbvOVgLKZQUS_bF6SVZ9TsJwp5N-DuKXIiWbu4Qq5D6p4S7IPibD_ZZzcXyJpypEtqruEJ6DdSVrgl5OjpVcfq3xtSilvLzW5kSI0LeG9DvYR7QYl-qeRdbLaZU1ZABHV1Q5gWnpaywWuJ495eodIvuvdmJD7LXDLd6VNG3twOFfWyHwwFSpFy_xq1kjL0DMatSwSltfCibv3QV_soJQaNuNmXf-2NJAUGF3eDEhi4v9O_L1_TaeV5lUrF-v7GIRR6GRw-kUTXJuemRfu-cBqmGldqU2xP5xrkBRAzRXRtSeqgD9HGlqxE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=stlKqhPJJ24nf2Zm5zHDRP_a07jnh6DjgQa_gg54oXwgMnpQ0vBA5tHRdM-eq2lFRDcDvX3Pz_eBKun1lwgIIoXoC_MinmeECvV8m_MkAJ584t6_s6ttHQ3u0RPVIB7qkhKoITsPACFeQy2E12FGX35P4x4F_qH0BK0i6RpsbBngYkvZ94fYjsykPUcHaWWE69xl6JWPN8gGw7ETl1DFQKTpRoOidPiOHUFplMysv0eiiuqPY-qxQQykgwF9v62TQ1D-jIxLV_-euM0HsCUbrsoURcZkTOigDPXPx5IKYkR-xQ03TEI2-lyA_hi_wzMu8WsHKm32dRRtZe8CyJ1lYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=stlKqhPJJ24nf2Zm5zHDRP_a07jnh6DjgQa_gg54oXwgMnpQ0vBA5tHRdM-eq2lFRDcDvX3Pz_eBKun1lwgIIoXoC_MinmeECvV8m_MkAJ584t6_s6ttHQ3u0RPVIB7qkhKoITsPACFeQy2E12FGX35P4x4F_qH0BK0i6RpsbBngYkvZ94fYjsykPUcHaWWE69xl6JWPN8gGw7ETl1DFQKTpRoOidPiOHUFplMysv0eiiuqPY-qxQQykgwF9v62TQ1D-jIxLV_-euM0HsCUbrsoURcZkTOigDPXPx5IKYkR-xQ03TEI2-lyA_hi_wzMu8WsHKm32dRRtZe8CyJ1lYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=SYW0NlQ_EOFoAntwzahusQFUW6zxkD4-fbx7TcM2L8cbZhy9JuoBoAleu-v5NnKFCYEEEBWKJbl7vICEdYzDfPM317yTrGn3arFi83k5JidfDiCTpTdjPIVLDt-aVy4iM1C_ky9MD0rxnAb4tzzTGXm7Zb_RaGFfL4ZVRsv5Hr8bZMeccgH6OOyBRcBMIz1W-6FEW7NYgz8r1F9S4An8qCgcMxFBP-pDRckVzd7BwshXUw11kzlSUAgx140r2guAwDnnZyg8tv92aLDMLaCH1ee_7aLG1tMK0v_NR__OAY8OyKgZPQ-HAYeBxrT_ul8mq-eXUMHvQLAO9MVvUC76uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=SYW0NlQ_EOFoAntwzahusQFUW6zxkD4-fbx7TcM2L8cbZhy9JuoBoAleu-v5NnKFCYEEEBWKJbl7vICEdYzDfPM317yTrGn3arFi83k5JidfDiCTpTdjPIVLDt-aVy4iM1C_ky9MD0rxnAb4tzzTGXm7Zb_RaGFfL4ZVRsv5Hr8bZMeccgH6OOyBRcBMIz1W-6FEW7NYgz8r1F9S4An8qCgcMxFBP-pDRckVzd7BwshXUw11kzlSUAgx140r2guAwDnnZyg8tv92aLDMLaCH1ee_7aLG1tMK0v_NR__OAY8OyKgZPQ-HAYeBxrT_ul8mq-eXUMHvQLAO9MVvUC76uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxzvYf_ovPDDoeJash6TaEsxO2FaiocWho4p0vBjuqgUqrJmKGd8ZPep3tIrgjMGOYFhecToiekP27aCnMj8gR-0SDifngCIlTgEJxRpt7zJsZaXS887ZlU75WrEBYnYttoPsMJTf4lNYfDwueO3i9D5bofy8aAydN4aQulEdrXuiqZrGkszOH1egP1ATgveeu88IV--Qo9ceZ_84T8ml_ndpKA1ojFjqNNXM5x_Ll9Sv2QxJk7YiDYwSTAsHWJDl16nTCThLN0bgj3GXhH_XlVecHTXxUJIupjciwQ8TZ3j7jjsTV-LaxTEQFJoiOP9kp4zpdP__gnFUwcCF8y32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Ap5ZrZdxSLH2V6KGht0GGVQ7EW5TsKTqTp8JmDIgvwdzw0RZ31XzvHq0Zj0J7AuQEXRmm1utKhPY0MfC0tERc7d29yRnRQi-O9upj2s1xM1-DA61tltW-oKy4XOCXSUxAOoYcWe04960Nhu3bvJyRoKEquyC6AvvoMrK67zYXzpYv7DYSsoPy28zMGoqPf9apQUssRy-BrnFVvMj75odrc_dD7QvtKsUSgxoNVkR8HHtq5xQRQuENTCMkLm0K2hPQdKQiNeXDihe-A0c75sxyMR_8weRATry84kkPbCkIFhYWhC0VN70xDfbaiWvnBVVcXkTF9Xtxc6NLlPUymr97zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Ap5ZrZdxSLH2V6KGht0GGVQ7EW5TsKTqTp8JmDIgvwdzw0RZ31XzvHq0Zj0J7AuQEXRmm1utKhPY0MfC0tERc7d29yRnRQi-O9upj2s1xM1-DA61tltW-oKy4XOCXSUxAOoYcWe04960Nhu3bvJyRoKEquyC6AvvoMrK67zYXzpYv7DYSsoPy28zMGoqPf9apQUssRy-BrnFVvMj75odrc_dD7QvtKsUSgxoNVkR8HHtq5xQRQuENTCMkLm0K2hPQdKQiNeXDihe-A0c75sxyMR_8weRATry84kkPbCkIFhYWhC0VN70xDfbaiWvnBVVcXkTF9Xtxc6NLlPUymr97zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=et2i7FlYnyDobWWLBFENPdzYfadSq3tP7X2a9Y70Xb4axp-t-cLtItgGmYIvLF6LZ3zQaDn5cfTUwwkq8t8DD3P-y8UY7YBs8ebKX4i7iXsEuZFeKjHFvu1Ep4L2Or-kAO5VBe7LYo5yukiqHVh1r1W3nj39C9AoOkslaE4jjq9saMXxowLxmQPunSeDDjLCmdlDKYjJcdKgUD7zTL_s1jrMr_t-Flj--hjVjI_FBQgLMAG22b8YKJGWhhdqS47u8JoGVzAl9ptaKcG4f216fkuBPQ0-cVwu78HciCANMaSA2C-TdCQ3b0p7G-MfWA0gQY-Lw5kthqabbA9ZNooGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=et2i7FlYnyDobWWLBFENPdzYfadSq3tP7X2a9Y70Xb4axp-t-cLtItgGmYIvLF6LZ3zQaDn5cfTUwwkq8t8DD3P-y8UY7YBs8ebKX4i7iXsEuZFeKjHFvu1Ep4L2Or-kAO5VBe7LYo5yukiqHVh1r1W3nj39C9AoOkslaE4jjq9saMXxowLxmQPunSeDDjLCmdlDKYjJcdKgUD7zTL_s1jrMr_t-Flj--hjVjI_FBQgLMAG22b8YKJGWhhdqS47u8JoGVzAl9ptaKcG4f216fkuBPQ0-cVwu78HciCANMaSA2C-TdCQ3b0p7G-MfWA0gQY-Lw5kthqabbA9ZNooGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9cC8ItD3_QvRxxJmixc8SiWkq6ShsYV9g9EnRPn7hFBcnIFsLZu9-4-8Lkr7-fYmjH39JK08oZSBmkWkgA51gRl62yUEJIzovEMDj5z2upV-khpnGA3RvmuBQTzOXRPZxI9eV3Tvdz7DQ_PZVtO03LLGVSbwXaHLKV1O53lZwo-CRv2S0TuzNmw8usotlbXL_YGQJwrBdB-AseatJP46qjp7SD319AMjx50yynqYkRQOPMcOXaOzlEI7UN0iyBqKWIWyXS1JUL3JtP67yLb0Y2FwqzGCHNj7oi-DbW7FelvVrR6Rx0oA35pXu8BF-NxexsFWRqdDqCJzKy0I9rzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pguzRP7cGoUSEyCnU-zi4ymyyMSbrYxbyyESaM3h7xF_v63RvqIfjpN9N6gMdVzr086pQ6kj5bQOkKYcmp3juZwCF_E1t3-rAqvbOJc9Jeh3UrekJLw3X5g95ZPz25LWAabZX9LP2ir1X5nnDuaWmVKZC3ceioK3W6xULXJ8lgGImR_EHPcZHvBMUhFLgIiftWDeL1Ckg3eXpjRuypcYbuRtVwTGfgjWZDCmwzUqYsBWl_olaUuxavW_7YRGU44DC33MSKPO-jPwRLSeyAmLGtmojXwDL1_egSDVB6K4Ep8y7K9Px3SHH5JPuys2u9ZAc_ewcsKI6cMpfhkLEqLUVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=X9mvc3KbWzYNdBnsNJHa7yskNGIZ6iEVBaxF8I59GEMYGkyhvuPvGA-Qq9cYU9ZdSjAJzKIyzzy3y65L1EAHjOwN8oR7hd2NEUPRhYPZYmJc3-G4PrAShcHaHoesaT_mi5ntQsfVD0Ip4X-0rFqWV8zq-G1bnk7mv4fVC7NFke3iHaPSzjP-LWPTm4Q3dNUNfgFhMoZz6MaWFMAcWpVjHZs03EnY-FmicBQ8Xw7YjC6QXibhM4ilia0W4rR8V18jGDZB5MarNrIrnSD2Zqirt1Ibd7t4Y9HM7WR9XAZuvpsQv2JGQ_3kr00qiubS7xrIFEgzoKZjfr2r9KXDxajXTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=X9mvc3KbWzYNdBnsNJHa7yskNGIZ6iEVBaxF8I59GEMYGkyhvuPvGA-Qq9cYU9ZdSjAJzKIyzzy3y65L1EAHjOwN8oR7hd2NEUPRhYPZYmJc3-G4PrAShcHaHoesaT_mi5ntQsfVD0Ip4X-0rFqWV8zq-G1bnk7mv4fVC7NFke3iHaPSzjP-LWPTm4Q3dNUNfgFhMoZz6MaWFMAcWpVjHZs03EnY-FmicBQ8Xw7YjC6QXibhM4ilia0W4rR8V18jGDZB5MarNrIrnSD2Zqirt1Ibd7t4Y9HM7WR9XAZuvpsQv2JGQ_3kr00qiubS7xrIFEgzoKZjfr2r9KXDxajXTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCQwl4iLvD7Igi7pUBaZD4EPrmvLjfnuzXmu-DcjXP-wsPd55pgdaTOPTqlunsr8v179Oqa8DlQNS2TqqK4K9QQ3A7mCDA05Pg-SdsAQZXz_5wpdqnMBsISo7m8z6yZ02y4DOvWQDTJKJkSZFTK2UuN3zQKPinueAkfEsHoX4ap-wAVOj3FuIqAAp5Dlgo7N3zf2DN3UwFyS9rKy15vJdLNd_lrIl_tZL1GKY6ZYSnBohy45qy82mAUrxoepLTyQPudmg-zcxqUsFBFK0OEkKEtc_mDYgOzSwkuXEX9Ye_MNPXBllP-houhzjNH7oQzhe_2foE5HjAefmxRTqk0wJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1rJ1TkpCS9CSRUbCS5ijs8VCZ47jRy7XKBMKO2WphMjLGwJHgQyG6X1odyM-B8vuC18L9maTpg8B4SGzDWBJa02daEA5yndo6VGPjvPCv7evilhbUbXcJCwc5AWa3ZsjcUrJVHICyDSTywja4-DGhYG_ykJWwIYHSmD-fuqQk4DKQRV6onhqLcYrbEHRfjHZSarvz3LNRaSRdPDONqRpHDyEg_dzi3KTcfod86R_ImNteJfkXznZ2HVxp5T_jBKjccHtmc7pqc2VeL62uPJzn3rfX_hcODIMp8Wd2fvJErAOk7Qc1Of24on1uYw58VrnR5vocoIayiFxgKSobkVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcovgiZoMTb_PY2qUqcKK1iTSVIcFWt_QfQ7NqTgDcx0ZaCGPst3Gnl153TvJbvdS4AI-okup5CWDkJLdU_jgZEESt31I3IvccqZ_f6D4Bsq8S1D-7C5PZ9P3VC0nch_txrV4izDBwSFIvdPGeGJGzlf2EoY41q1ywoDjSZQ52tT_KPf5gbCsSVn9d5p2fTQikX5pgvonAm3AW_lNwTGLLTLG-2UG7EMZOFz1QlBpubtwnkr6jnwmD5vMujHlhr-NaNjHK5QmG_Ps4Emjjz7xOHo_0LA7HJby_g__TlIDymTWkje-6bLPh7RelhsJcEHFpJ526nHqFZYHBdo3JUuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=bm3283mYrVJGMW5tqYKrPySOkwaIj5Tyjm18DTFe4ZRdg1x_K6InuCKMzIzKsJGy9eGjWyUmaIgJLdKi0RfoqwuR_E9nWFZ-44CT4uLp0HxaoPW4oTnGEVKL3vIAISSvd-BST26zExj4Nm59lSaPVdlWDgqABiJbhW43vZkJs9SGzyQhc40ZQ9xJUfn24lY7YR_9Tjyu3gll71bSvhdxKsPYGxzKXLy97lJk8HFpxZeQ6q-Du8S7N_XgZlp3DdFXGhlBfyIiHxy4_qUxB-pFKUYWDq2DwPc0iKWvMM0uj3cUoxqQV6Eb_zjxGo5gmygJgB2ioz8vLcT0wrL9jEjLdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=bm3283mYrVJGMW5tqYKrPySOkwaIj5Tyjm18DTFe4ZRdg1x_K6InuCKMzIzKsJGy9eGjWyUmaIgJLdKi0RfoqwuR_E9nWFZ-44CT4uLp0HxaoPW4oTnGEVKL3vIAISSvd-BST26zExj4Nm59lSaPVdlWDgqABiJbhW43vZkJs9SGzyQhc40ZQ9xJUfn24lY7YR_9Tjyu3gll71bSvhdxKsPYGxzKXLy97lJk8HFpxZeQ6q-Du8S7N_XgZlp3DdFXGhlBfyIiHxy4_qUxB-pFKUYWDq2DwPc0iKWvMM0uj3cUoxqQV6Eb_zjxGo5gmygJgB2ioz8vLcT0wrL9jEjLdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=edKuqveSZ6m69I3DkZSSuE40x73odvbuW2FrmSGpEXAScE9coi3XXc1ejvJ25oLWN94gqg-JhyYYLhwOoy9ygnd4CX-Fr0W49-8uYOsAtuq8RXTpvPGmCBtZoKgK9Bu8JpPlq99_WJlEXmJU_KIyjC-2eArwPXSKFYfgsFcSd1avb6kvQ1ChvcMHR41J_ZRPXA7Yu479HaTMB7h6_a_icH4_c0uVcJknhe18Dt2jG71zzuN824hZbY7v0Tiy2jfwcIe7H6zTmqNT97pkqA62CdPVSWvkDF4D37yo5iy8asd27Ta91p3LQ4sW4DwtsbokUct1Zc5bpR7wkWk7qCsMgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=edKuqveSZ6m69I3DkZSSuE40x73odvbuW2FrmSGpEXAScE9coi3XXc1ejvJ25oLWN94gqg-JhyYYLhwOoy9ygnd4CX-Fr0W49-8uYOsAtuq8RXTpvPGmCBtZoKgK9Bu8JpPlq99_WJlEXmJU_KIyjC-2eArwPXSKFYfgsFcSd1avb6kvQ1ChvcMHR41J_ZRPXA7Yu479HaTMB7h6_a_icH4_c0uVcJknhe18Dt2jG71zzuN824hZbY7v0Tiy2jfwcIe7H6zTmqNT97pkqA62CdPVSWvkDF4D37yo5iy8asd27Ta91p3LQ4sW4DwtsbokUct1Zc5bpR7wkWk7qCsMgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=CCwFgh9yayZtWG6yFTJHS0ISlEsNx_AJAJqz4cKr3EH3z0vv-GY1sn_AFt7wvdX6u-Sz8OEwDRi9hhA3VaFzcwPjCWmYzXIkkVnpWE_T935iLBdvpVWLzRiB7QZQUCYzqab4mrKYCgWa5zy-2A1zFeRL4g6gT2Jfg02Hg07foCbNQMSsW-LWgXcb_nIf6uRQ34j70a_TkjKCky2yevMx6DwjZKG11xVLLdz7hY_NdsNXa0nlXoOmUxNV_rN0NDmKrUOt14UzBDYQFnrkIPdFyjmZ8RkGRMqE3IcFcfP59pETvkmK1dI2tdytjorXOEXESR7bGmve88ngwWPuBuO05STgndB7DqVMnvdtlWXisuLnRwI1ZTX6TpZLKJ27oDFgR4v5WdW8_rP7OBAlR9UQq4CU3D3ZfHnHEt1UQTlzQNtVNMfBobSUXJYaPpTeXZIa8qjdnHJV2SG6aDy8fC_oJ5yz0RD-n7sC4uW3wf0307KFJek7GPjf-WJJWk749Ynqm-v29gvVSACQHS1dCwoE0y5p7QkKYMb8HkyeT_mAprTKz1r2LaeA9VtEsMp2308lS0ZAzacG94AuLOh1yNl-V-FziCW3aqHwkNAiQ9NA1t-VoNDYwpXsvf1isxbh0oIclrObleQSLvEZjZBo4q0DRA5ajAxhSEHHNUi6c66OQ94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=CCwFgh9yayZtWG6yFTJHS0ISlEsNx_AJAJqz4cKr3EH3z0vv-GY1sn_AFt7wvdX6u-Sz8OEwDRi9hhA3VaFzcwPjCWmYzXIkkVnpWE_T935iLBdvpVWLzRiB7QZQUCYzqab4mrKYCgWa5zy-2A1zFeRL4g6gT2Jfg02Hg07foCbNQMSsW-LWgXcb_nIf6uRQ34j70a_TkjKCky2yevMx6DwjZKG11xVLLdz7hY_NdsNXa0nlXoOmUxNV_rN0NDmKrUOt14UzBDYQFnrkIPdFyjmZ8RkGRMqE3IcFcfP59pETvkmK1dI2tdytjorXOEXESR7bGmve88ngwWPuBuO05STgndB7DqVMnvdtlWXisuLnRwI1ZTX6TpZLKJ27oDFgR4v5WdW8_rP7OBAlR9UQq4CU3D3ZfHnHEt1UQTlzQNtVNMfBobSUXJYaPpTeXZIa8qjdnHJV2SG6aDy8fC_oJ5yz0RD-n7sC4uW3wf0307KFJek7GPjf-WJJWk749Ynqm-v29gvVSACQHS1dCwoE0y5p7QkKYMb8HkyeT_mAprTKz1r2LaeA9VtEsMp2308lS0ZAzacG94AuLOh1yNl-V-FziCW3aqHwkNAiQ9NA1t-VoNDYwpXsvf1isxbh0oIclrObleQSLvEZjZBo4q0DRA5ajAxhSEHHNUi6c66OQ94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nkOZEUNjuwQV6r-hVylRmo7fN8zBT_5yZwVJeCVkihhyLIaCafPVXcqM5fCdQ8Kq19KO2R_XKujn-ElJUvDiFA8LK0v_d0X0pLvyOXeH0SF_72vE3RV1MTs2GJ_vu_X4XPtiG1paVDjg1_-jQNYG2vOzSD3I3EkJbDIUfHS8LDGb9LKe9V_vfNWn_x2AJfVqBy4-KgtSy-o36TkjJQMACn8ssvkHl8I5HvJxn1WIET_hLIIt23D80yaT71PAsexp1F7NxIVh8C-8NcfdrIQnkclzK7Umh7-Dok-BWL_sC5vPWVAYOmACICipbd17siGc1RAPJqvsAcKI2GykZBv9G4tIPpzQVHtGLLsTS_Zmu1ho3kgPWtYN-TgYrL-NCJ1CyFue_tLq5XTexlxN6Skt5JdyqPKCveA-_6-Ura1PI-TlSuS93Y8GGzMOaH604bYb54-H0K607M_FuN5UPy-2HCnTi7-6KyYCQzZa4yuL38zh8jr_SyRydD5Xxn_PAbxPLnZAi6wxXiynFAkYeKfHjBDkX5gJ4OTxaHXjIK0T3HsRbkFWGqrzwlSIExGz59u2jp1NHHFoTituooDSGSkv3rvL01x_xLCtivFscoOlS8NtTx7Q-9pcp1BtbJPWX-Nes-bGsy_yEekpPBGJKuH3C8PfBK5pggRBrnP-1KnvfRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nkOZEUNjuwQV6r-hVylRmo7fN8zBT_5yZwVJeCVkihhyLIaCafPVXcqM5fCdQ8Kq19KO2R_XKujn-ElJUvDiFA8LK0v_d0X0pLvyOXeH0SF_72vE3RV1MTs2GJ_vu_X4XPtiG1paVDjg1_-jQNYG2vOzSD3I3EkJbDIUfHS8LDGb9LKe9V_vfNWn_x2AJfVqBy4-KgtSy-o36TkjJQMACn8ssvkHl8I5HvJxn1WIET_hLIIt23D80yaT71PAsexp1F7NxIVh8C-8NcfdrIQnkclzK7Umh7-Dok-BWL_sC5vPWVAYOmACICipbd17siGc1RAPJqvsAcKI2GykZBv9G4tIPpzQVHtGLLsTS_Zmu1ho3kgPWtYN-TgYrL-NCJ1CyFue_tLq5XTexlxN6Skt5JdyqPKCveA-_6-Ura1PI-TlSuS93Y8GGzMOaH604bYb54-H0K607M_FuN5UPy-2HCnTi7-6KyYCQzZa4yuL38zh8jr_SyRydD5Xxn_PAbxPLnZAi6wxXiynFAkYeKfHjBDkX5gJ4OTxaHXjIK0T3HsRbkFWGqrzwlSIExGz59u2jp1NHHFoTituooDSGSkv3rvL01x_xLCtivFscoOlS8NtTx7Q-9pcp1BtbJPWX-Nes-bGsy_yEekpPBGJKuH3C8PfBK5pggRBrnP-1KnvfRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vFnVaq0GjHFxbTAqxEJ3a9WbBJG4gmTHv65eViASjYKgsG8mJYQIUntnUIjbz393sfqoGZYeer1VZmF2TDU_GQjllwzQVWGyPT45xPu9uoSdAbdyF74xZwacE80FIkzyfA1mLDJLFXhSTKe89vMaTaCOgaRH5zf53n451gQ33Dmd7XieSAaZwBMAguje7AmZm5o2jjqbRLmbuW-MrqFvb6_LHiggb1H1OadWBqqzYoNzLc4B154ELhY04D-61sHGdeCuAMhREVxgij3R7U73jFgfn2fFUVkS_9KR2sbgdQC_sOcpMww3brWT_eprh6A9dq0AN0SV76mJuU8s58OKFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vFnVaq0GjHFxbTAqxEJ3a9WbBJG4gmTHv65eViASjYKgsG8mJYQIUntnUIjbz393sfqoGZYeer1VZmF2TDU_GQjllwzQVWGyPT45xPu9uoSdAbdyF74xZwacE80FIkzyfA1mLDJLFXhSTKe89vMaTaCOgaRH5zf53n451gQ33Dmd7XieSAaZwBMAguje7AmZm5o2jjqbRLmbuW-MrqFvb6_LHiggb1H1OadWBqqzYoNzLc4B154ELhY04D-61sHGdeCuAMhREVxgij3R7U73jFgfn2fFUVkS_9KR2sbgdQC_sOcpMww3brWT_eprh6A9dq0AN0SV76mJuU8s58OKFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw4olnlX9VKXVfUZcj4maDFeC4u7ehwV4IihegVJD_cci6CVYFTEIa9KJ0GRSBcJrTLy9hIyq0D6T09_TOTOss2CpeOdgcVLP4zp-3eIpaLkgZeVXSPwTlExFAozy4rVFepdfubDp6Y0FsQ6lL_ZdsBiTgFdl28fylWJRSo4bYjV8EsspiXSKhzgF44nAiBRbApgdFVFL6gCw_yDyPvQFwZ6Qd3ZbiPI486JSynfjpj53kYnE5zPptPqjsrXWIiJn26xVCNusCgFP-P4SgTGkmJ16uy7xq0sv0Ny1sEQ2jpEKDc_-WPznCFA9PAGIl-pOIGLM_0eYyHKHLSXBpowOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=py4XL9VYrrlyvGxBp0I76NUaoqgx2dRrWBYCr0i3zcRmWEcR6C-kmTl3w8xNq8JSWWOwmc-7HYV_cS3tHL1W7zBcnnOCn9UOz7e8LlaZ8K7UahBOKa9cB3WxAiFmVVWPbtD6TOHgsN8wL2bQdr1bgkpUd3g6ZphWTGVQT7mt6hXEFT-YGODNcJQFLg0hlXGkhL6osVEQVM1aVmJM7j6RSsxxKVojp2rKVOej_lt-W1kpAUho7nRmPohsWP2NJdEk3bEQiEga42jOzwD5Bm49LQeVDuvy58ARQeLXi-MOFhanQP3q5Cb_jMeZmVly_isN4S9a3Tnjtg9G-9HNpcBaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=py4XL9VYrrlyvGxBp0I76NUaoqgx2dRrWBYCr0i3zcRmWEcR6C-kmTl3w8xNq8JSWWOwmc-7HYV_cS3tHL1W7zBcnnOCn9UOz7e8LlaZ8K7UahBOKa9cB3WxAiFmVVWPbtD6TOHgsN8wL2bQdr1bgkpUd3g6ZphWTGVQT7mt6hXEFT-YGODNcJQFLg0hlXGkhL6osVEQVM1aVmJM7j6RSsxxKVojp2rKVOej_lt-W1kpAUho7nRmPohsWP2NJdEk3bEQiEga42jOzwD5Bm49LQeVDuvy58ARQeLXi-MOFhanQP3q5Cb_jMeZmVly_isN4S9a3Tnjtg9G-9HNpcBaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=W9ggm4pF4p5j82fQUUBsihoxDSyan1gkXCvBv_urjK6YiAtEFJM7EmdFKjZHXSkNe2utCZnyCOl3VG1M0GaRa6joTnhXyG1A8i1k6ULPLahvkO-Sp33zAcYkEQM-o1wqCjCFmO02fR5fWf4Kn3s3SqvbxnQwxlos8auQqjzpUNKXkUbXHnpqSgCcvrYzb6_rDn60oNgUEatR2OfW3xAkB2sEvyCukvzPHfLBFg0uLMCPFkRix1mUpgqnaFntm9tzUkdMQrbLpGAPXeARiS03ihnp_O-WCBwUbzFcixPA9gMJYkacZOd4oPP7EnWjGz_fJnVFZ7jdZv_2jsuykG5yTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=W9ggm4pF4p5j82fQUUBsihoxDSyan1gkXCvBv_urjK6YiAtEFJM7EmdFKjZHXSkNe2utCZnyCOl3VG1M0GaRa6joTnhXyG1A8i1k6ULPLahvkO-Sp33zAcYkEQM-o1wqCjCFmO02fR5fWf4Kn3s3SqvbxnQwxlos8auQqjzpUNKXkUbXHnpqSgCcvrYzb6_rDn60oNgUEatR2OfW3xAkB2sEvyCukvzPHfLBFg0uLMCPFkRix1mUpgqnaFntm9tzUkdMQrbLpGAPXeARiS03ihnp_O-WCBwUbzFcixPA9gMJYkacZOd4oPP7EnWjGz_fJnVFZ7jdZv_2jsuykG5yTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcQ1RxhzmisPt3X9MeXTrJc0oTlLy3cS9Ww3-i1wod8p2I3ZBXuCMPEaYnnPXbebRaaQvc_N_T41r3wffPzL-2lNTQLeKnNvpoAz-_msV8k-ZJOPux1RdN8cHOeJF6u3d2K8fKegv_JWxODkGMOOceJ0JOCI07z4hff27jtgulQ-A8ZSnil_0fuispx3LAs1HoVAhuQf0iqUiJm0LxpG-cmIpCb3NtfjxDnCfa9OOpRNojj6wpY3FFtXkS8UGNiPkhkF8jWuRGajkwlWnACY49A7o3xD3pX_9h49JYk1Oichn7oRcOnUMMD0itR9hsUod3Wjau-sb4NIba02Mkld7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeHWh4bdXEzI1QNwSvF3tC_Eoxy8l6y6-37EUStLDSZoUpFxWfyc52UFhX6fO7-wqKbIYnP1G20Y_CXfPwz8KgkKYqmk8LijjdX2Xa9ln12NxKGGpOGdpVZ60-fAQTPLm15kwONErGV4yMjU-A1fTtXTgLf1Jag9It3bk43te4i2W9csVYjDuBtX-K9j-9k6QIowaWsheM04tMnHHl7tmn_OAdTs3e44V95G1sdF-KpZ25WYWd81BHHQ8kEuUYN5JEnTt3cBJUBtAhJhxKgneB_I5ICkpO7Y2Mpw06oHrpGGc9veQFfG4v8jaEflYoO8DBGXDaHY3YAg5x7iIqF4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFUsDhImeOwKk1QhspeDTZHOXFSFP3cW-vq1SXX3DvPNB5kABCXcEzIo082JmkgI5OXgF4VxTkv5TLHbkU5zxSY9sQGl08GCymbHs1YroR3zJyeqfpxEfE2VQqNujjZZE5PqH2CAZD1oHc26vexYyZ9RYwaVZttql5SLxPbNgw-fwtz04MzrPnlAjULC0Lh1vUHGmP4S4MjP-Zb_oOmo1ad9YxTvz0vu3ay3tt_FjwW2HHbat5QdcdZiXgvB0XBYjrv8vZ8uFdWzlMPe-uqgKH2mZyAgkFvXycvooqGJPTekP07h3ciCsOYDKE7QwyjaePZVRJxUif8WZVLYsx8WrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohOM2eZtLmrVQdGMB3BBi3IbZcSjsZdja4aU5ibbHYtcPlf5frC3b4HpWN2ZjE3Qtt693G3abz8D4mDg83jXuqo3J35ksvg2EndvI1PY8ot-XrbeFK8nG_5L-qGdO0njRMIiPFJG9CW9TYlZWHrKZzVNlnQZdnLJYO2N47g8GG3jnuHiQxdm8PxMwrfkGULmmKvSAuVxMDHlPuf9gc4RmcWZgJDIhWNLo1w0EofEJFEvmMa5E8GvZGq4SAaO2juZQkRREv3YpzME9G8UB_xytEa487blulMlwB6Na_spib5im7I2XDKE_KQD3ZTL_cX9m7MU_YKyTxUgEKhhIBWIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjfcCZrG7-UFTRj4N6fEPUtmoaRfcc3W6B1dWZJY5NVxqCkeebORP-MzrE8-lCWeeVIpsEtLRZoS_jKZM6C2bpaRzLPsyfpe0gaz9SC178m7jK7YmgtJt6SKHtPJkbQeSOksLIT2GJ24p4s_1nUir8ojdOhqZh5kF82vp-uAgR6Inhs4c0AoxWlgktvOXLlObloCPXETpEXSdaOYN1Fx6D15N1Wyq7iUZJKQctuNfowvLGQD6rwYRqookilugt9oS-VgW6e2p523zUgmb9PyqsdGlF5EwgF_GiQ2ujSWa8BjrPfn6oOUQ0o7XHVBCTYwroiUcnG1o3Vo-njkhYDm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_Z98_rAUDwCGM9uAxWe6qphHvJj38MHfplnmlO7OTsWqRXI7nSWlcLA3UnZcqbfxnW1YKNrftGn_-2wuS2k0s3QKEL-XrLhCYkk-kGOWKSERNgL2kZjwe3j8bTHA-4mKQfS-GOWftkAIRH_irQgEi5f53obcV3D3JnUaCt7chgsd6wyppe3sIYxlrP-_lvu0c2X_W2hwGYbw8fglK0Y2yiEZ6nyEcib43dw5PjMh7brC2GdU1_CPJr5VEwtJ7-FrMt4gLNNmQwYK-FTSJT4m_ZBBYqh3-rF60h0dDFXTdr_1XnD-yPeWamDz88AVfbilqg2KaYmPU_PtIytgbdngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1gASTpcnnBR5NS6N3_8dTS40TvdAKXGw2P1_yrCj7qik4LPeZv8FwtUlTiPPrZ447UwmltUNw3bcun1mqNPA7Dq0OzvyuCHymxHqLJA8ylC3_l5debJCKqvuvr0EmwpEv-MeOGHULJDYmzlHPJ-f8frp76sMb-6XqXIYFm3Ap_werhS7Pi0i3aQSNIsrnNAMOaRT7CiRGpCOo_gLSsOaWCGgwS7-Kx5HMwwJ8vsVCyjeYXSq62uSLlYt-_gbIddmRGMKLYB5FoX3HwHDY5FLScYihWtGu1fc491P4SDM4njNwnfYdpaH1BG5675anPh06ZfnYhcaLSsPS190uGNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJHbRPP4gCHu_8iceQi3XRmy9Q03gZpnke45mjEDGbiBhxvYRbqATWyR7ZH9gUFLyeIlLHBujAZFAivBo86uZnqyT40uuCkoLOjSxSwFboLTagl1ZJdT3_6QT6L36FyfHpZgmnnL3zOguFVV6oXjlfX3pGC7TLDiz7HixgaMGS0ynlSnChVLAvS0_uJ5v-5jC60wiMSNtC8c5u--v7JK1rPnYdO4MlZeTV4UeiqsScn9wVYQg0q7onWsyJLwiCMKKGiXa2C3ctOO0pwSSUJesS0dGE24s9qbpV8oaf8hpW472p2tbKIo5UkTEs0YURV5w5I98wtnvP6kNobUvvHz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSVZF7XB83AjbN_FlONsikMxEvN_TpkN448HLW2NFv4NcJZihjt904cbZzziJ8qlXSHuRDvvU1xloINQdm3N6kD4LR3PlKEmg16k120AVjbTyVf5ofhOMtJxn2_WFMzQN9IsiwQXDuyTwG0Zz8xX1jiChJqXwzHDZ0x5dgGEMBK2_BV-SRw_KLswV9bLOgFfBipBnNatZ-I6phDS--5-BkoO4OrK9T3YFD5hNgJ8xQ3TuggzYhAIqnSPV-KCbOBxpWVkIUeAurman-c5hwx3tSStDrhECPz111XXoHlRL-O8p2nEhC7uyFAStmDNJicY2wAeKHb7fc6NHbFvZshCaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkVnDbW1TSVjmPVn34gE63ydg2K31xJBpdadpC_saZhX_WWcWqBRe3oy6Hz0XpbFOpAFfpVPExjmRk5kaj0cAZ3-yeIIBkDbjvgz-HhwCzX8S149p4AGxlOgXZ-UgyIXIOgLuwLpDqEevx0n1n7PTUBbGNeqyo_KYc9gBY2Foe3tu6d-aw3e_87M_IIeZlkCNzeuIzkxMbkNnofOBbUVmFTRrfMb4BNFH42FdYdlhtGRKTsTNg1aSYLZQ31409lYe2sBYmacRo8IaPCpqSM3E83Z1m4icy6Pzvo2nzoc4NPSP86ARJWAIA4kE35nZY1f37-tT6hDPcoCZtZIyavEkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
