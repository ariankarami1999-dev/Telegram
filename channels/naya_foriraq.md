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
<img src="https://cdn4.telesco.pe/file/UQ0ZApHPQRPVkFLegMYcbsbz9UOoAg1mz9k2UZa8gimmMOewpfsbw9slDlg_4CmKh-Euyk8IZVZpaywLHubeUY_UUDJuOH0J-t-5VsCK4pU5T78kth8D8GZwg0rHhNc8me3uj77t5nZT5iXazWbc1va9dyUg6Z0SVW_mqDFymzypgai3w0vZjvSBWFQPv1BpHRVjHlYNpvbtjYvGfj23xplnTjJWI7SJv5tI7eJvV4d4WoqMKgIML6aF623D-ifTEAG22po0X1wQ6NQofv5KSiZIMO-Tte2lt-EA_7ZteFtEv5dHWzBgXYbX1RSBL0dbzgBdmgrnzbz3XCcpz_g12Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 263K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 23:34:48</div>
<hr>

<div class="tg-post" id="msg-83280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
مكافحة إرهاب إقليم كردستان العراق:
إسقاط 8 طائرات مسيرة في أربيل</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/naya_foriraq/83280" target="_blank">📅 23:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار في كنارك الايرانية</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/naya_foriraq/83279" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eff9938ee.mp4?token=ngcWtcJnyiLNF0PXXu_2K0SfxzcV7qgidg7MHJYRG-nI4dt-fD_Ov9uo5hS4K8yj-0WM9rlO5Bd69NFH6L-zuSXCih2zOMbzgQvp4bLbPDyITQkmYeqYUGwt9o_VqNBHfuLXKc3DoI1MFi7HhnQr7FEgt_mIvaHbzhU9GqFecM4dCrVlh5ltLOBkFWCuxD0T8tWrzAWgx0l49i2z_yIlPV2lpPlrUBSCgq8dI5qkfGMDCh8bLWB7Imd0SMGgWCVO07CG_gUxDCp9MoJNl_abFaclU5-0SLcxoI8NkvkvBMGueLhoH1zAUIsbfP61cv6tNSDtETXDZgUNz4kUsgAndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eff9938ee.mp4?token=ngcWtcJnyiLNF0PXXu_2K0SfxzcV7qgidg7MHJYRG-nI4dt-fD_Ov9uo5hS4K8yj-0WM9rlO5Bd69NFH6L-zuSXCih2zOMbzgQvp4bLbPDyITQkmYeqYUGwt9o_VqNBHfuLXKc3DoI1MFi7HhnQr7FEgt_mIvaHbzhU9GqFecM4dCrVlh5ltLOBkFWCuxD0T8tWrzAWgx0l49i2z_yIlPV2lpPlrUBSCgq8dI5qkfGMDCh8bLWB7Imd0SMGgWCVO07CG_gUxDCp9MoJNl_abFaclU5-0SLcxoI8NkvkvBMGueLhoH1zAUIsbfP61cv6tNSDtETXDZgUNz4kUsgAndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاحياء المدنية في تشابهار وهي ترتفع منها اعمدة الدخان بعد استهدافها من قبل العدو الاميركي</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/naya_foriraq/83278" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618d61e40e.mp4?token=cmjfJnuJ3ALYasCKL4Eej1YUhSWPRVcmNHuYm6y55yIudXQRhlwI2xqMvU5Xd-ccB-6InqRtv6_AlBDqLb4ETQ0RxuWb9VlMInWVPmy6x1BRxb3D0UPGU30qx7XwR9e0zMmpDtmOe1y3e96clNZSB7QelqVsYOg1zm2b2wOeJ2mDeQNdylBT_TMhb8EUSxf_Xj2gmkhqSevue_TcqQ2kSYARQMAvXWh77wgGwKMl-zESZril698KD4iAE7Vib3qZF6Sm10jZQ9xAWT-XStyYCQH7_vU869mrbm_vUbO-oPqYpS8uajCrF1dE5uYW_53y_muC7fP4RwSWABh3XH0PdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618d61e40e.mp4?token=cmjfJnuJ3ALYasCKL4Eej1YUhSWPRVcmNHuYm6y55yIudXQRhlwI2xqMvU5Xd-ccB-6InqRtv6_AlBDqLb4ETQ0RxuWb9VlMInWVPmy6x1BRxb3D0UPGU30qx7XwR9e0zMmpDtmOe1y3e96clNZSB7QelqVsYOg1zm2b2wOeJ2mDeQNdylBT_TMhb8EUSxf_Xj2gmkhqSevue_TcqQ2kSYARQMAvXWh77wgGwKMl-zESZril698KD4iAE7Vib3qZF6Sm10jZQ9xAWT-XStyYCQH7_vU869mrbm_vUbO-oPqYpS8uajCrF1dE5uYW_53y_muC7fP4RwSWABh3XH0PdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار في تشابهار بايران</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/naya_foriraq/83277" target="_blank">📅 23:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجار في بندر عباس</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/naya_foriraq/83276" target="_blank">📅 23:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجار في راسك الايرانية</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/83275" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83274">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60348182c.mp4?token=FKVVeDX9VGXfXNrE7dzJ5mejZ_62YrntnBEo-jGZJOoOOFsCcXzQv8ulQESO1XCuDstb_ZileGrdiU9TVGS4XieWlqCuVYmnGrJIGGl2Ko8qpxUw2yetFhZl1WdwPc_I6gWuo_N4AprsakV6bji4bbbOEVc85u7gSdgPbr3dbuI38_DGlTGAXWjv6gVV7rlOOOTpYp8XmPfV8cVQY0cUNbeR6zIJGjxsPWSSkQmyEawuSbJVGJTfCoJgcRgerSjAOrAteHCF7GNv0Ytk0p6JSpnZMLcG8YClcsePheDEM-pOD7Kw3jeKEC7y8b73fKSlNYMJBoOeIocBn--4powkLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60348182c.mp4?token=FKVVeDX9VGXfXNrE7dzJ5mejZ_62YrntnBEo-jGZJOoOOFsCcXzQv8ulQESO1XCuDstb_ZileGrdiU9TVGS4XieWlqCuVYmnGrJIGGl2Ko8qpxUw2yetFhZl1WdwPc_I6gWuo_N4AprsakV6bji4bbbOEVc85u7gSdgPbr3dbuI38_DGlTGAXWjv6gVV7rlOOOTpYp8XmPfV8cVQY0cUNbeR6zIJGjxsPWSSkQmyEawuSbJVGJTfCoJgcRgerSjAOrAteHCF7GNv0Ytk0p6JSpnZMLcG8YClcsePheDEM-pOD7Kw3jeKEC7y8b73fKSlNYMJBoOeIocBn--4powkLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من الاهواز اثر الاعتدائات الكويتية الاميركية</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/naya_foriraq/83274" target="_blank">📅 23:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83273">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات شديدة في البحرين</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/naya_foriraq/83273" target="_blank">📅 23:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83272">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات تهز قاعدة عيسى الجوية في البحرين</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/83272" target="_blank">📅 23:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83271">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/83271" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83270">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات شديدة في البحرين</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/83270" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83269">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92c1004eec.mp4?token=GXpCbJjgKd5KNfzFhDHPi724l50vdTXjQpgFxiDMxgN5gZwy4d429Qq7MhxzLr1ex09K1GiQZsUMSHib7FKqBpOY2qT5Qu1SjYMV6YaJ9KFGN4KTI2VujQlZvErbulrmsSQFSEtytNmOTwlnZRAevwxfo3WrQVFPe-Ux9UA2mMw6HSIvLQj7Ft9ZPbIvlGWFVDHgfbh5GxlAGura1WfZkdwRJ3fvXuJJIxz_DBC6AuIS27ED7iFegJlmBq0iKwsnYihBN_7gfhPaljdXe1edrK5hh8wODUExfql9pVNReIqk67DxPX-18GnJt6W6thi39I7f77pT6nKRkQLaiX_52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92c1004eec.mp4?token=GXpCbJjgKd5KNfzFhDHPi724l50vdTXjQpgFxiDMxgN5gZwy4d429Qq7MhxzLr1ex09K1GiQZsUMSHib7FKqBpOY2qT5Qu1SjYMV6YaJ9KFGN4KTI2VujQlZvErbulrmsSQFSEtytNmOTwlnZRAevwxfo3WrQVFPe-Ux9UA2mMw6HSIvLQj7Ft9ZPbIvlGWFVDHgfbh5GxlAGura1WfZkdwRJ3fvXuJJIxz_DBC6AuIS27ED7iFegJlmBq0iKwsnYihBN_7gfhPaljdXe1edrK5hh8wODUExfql9pVNReIqk67DxPX-18GnJt6W6thi39I7f77pT6nKRkQLaiX_52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يتحدث عن نفسه:
انظروا إلى هذا الوجه الجميل واللطيف... إنه قاتل. هل تصدقون ذلك؟</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/83269" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83268">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fcebb661.mp4?token=NWYdNnN3ekRMBq7AyCsbBZHtYozyDLBIILyJRjkAVf7wxV4wo11q4ID1rqOvY0k9H89K-D5jqGqW9VF3Yc9LCLwt_eVLbIkMzfIR4AW8xpWMKeHxzLNtn3AIhBB5_W8i9uMqnw6GNHvGCEZ-XpGMTghzkSTxc3e91mfIZDN1h1LmtNy4z0ja7hwv1xLMiWrjAKZ8sgT5CkgKZC7ezGy45qgf60pDg-lZBVa4tkIcPWHIVP_hiSUXFkxZj_bIpGzUopHt-m-ZPD-vOxSurRQ6wI3o4pK16u_XF9Zyz2gWosYaEz7W4-F6SFejSI12ewZfBDz9I_6mQL-T8xQsyZ9Lpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fcebb661.mp4?token=NWYdNnN3ekRMBq7AyCsbBZHtYozyDLBIILyJRjkAVf7wxV4wo11q4ID1rqOvY0k9H89K-D5jqGqW9VF3Yc9LCLwt_eVLbIkMzfIR4AW8xpWMKeHxzLNtn3AIhBB5_W8i9uMqnw6GNHvGCEZ-XpGMTghzkSTxc3e91mfIZDN1h1LmtNy4z0ja7hwv1xLMiWrjAKZ8sgT5CkgKZC7ezGy45qgf60pDg-lZBVa4tkIcPWHIVP_hiSUXFkxZj_bIpGzUopHt-m-ZPD-vOxSurRQ6wI3o4pK16u_XF9Zyz2gWosYaEz7W4-F6SFejSI12ewZfBDz9I_6mQL-T8xQsyZ9Lpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من الاهواز اثر الاعتدائات الكويتية الاميركية</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/83268" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83267">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجار في بندر عباس</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/83267" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83266">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbsENwoJomSeaAJn5I4ZKXcb-44f1svfQU74QntkW7jWDQrzRjsM1slTE5RTIXUvfcx67o-BBRk4jOXRlQyLgwI3ThmlgJvKany8sEmoSKyDohM8sRyR0wEkyk1F5S8e3i31HMwJlW8THMYFaQDDRppD1b23Wm27bQ8ERMUUe3Y7MXq4syFdVloBnLN7y9R2RYKXnyFtFSHRqIm4ERq4fqq_5BDqqhQ_-X75Zk-Q1Z6MdwZzMnRixujDFZ74mxUOLxjrcNA-9rw4PLY_-IaDQn4SCuIs5t9htiZCt-C6XlE6W9nwdyP9dxfoiCPkezso4Aawm5h-hEuW6pDxpEL5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتفاع اعمدة الدخان من الاهواز اثر الاعتدائات الكويتية الاميركية</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/83266" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83264">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0035697f.mp4?token=aNOVdZ3dguXd7WWNUB4rVZIPJ4N8K57rJFnz0w0I3i92AhwgGv4gAVrytanVbHlGSd8VXaHorKP-EUhlHiTiAfAJlyCWZ-FL9i6wFFxKss5V73IPZEp26ZsHKhsonYst03GRKtDnp76Ryw3lTq54uKfokCMjiKP54iZc94O9Qt2I3k_dyK1Je5SkrnXNUNBZcVeIc-JwaFvQNCq_fIQ2m5s8ABnXOsUta2is82rszJCi50Am6jRqp2Liv1qAbCV1pQ7oxq8c7_3LVb9PaVYV4vOel5N2lfRG39VMfCycS9qtvirxyqyFDx_hbkkbPSk60fwdOywPuwrLRJdumOQsJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0035697f.mp4?token=aNOVdZ3dguXd7WWNUB4rVZIPJ4N8K57rJFnz0w0I3i92AhwgGv4gAVrytanVbHlGSd8VXaHorKP-EUhlHiTiAfAJlyCWZ-FL9i6wFFxKss5V73IPZEp26ZsHKhsonYst03GRKtDnp76Ryw3lTq54uKfokCMjiKP54iZc94O9Qt2I3k_dyK1Je5SkrnXNUNBZcVeIc-JwaFvQNCq_fIQ2m5s8ABnXOsUta2is82rszJCi50Am6jRqp2Liv1qAbCV1pQ7oxq8c7_3LVb9PaVYV4vOel5N2lfRG39VMfCycS9qtvirxyqyFDx_hbkkbPSk60fwdOywPuwrLRJdumOQsJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الكويتية تستهدف الاهواز مجددا</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/83264" target="_blank">📅 22:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83263">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوي انفجار في الاهواز</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/83263" target="_blank">📅 22:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83262">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIfaaIgg_3f6hsw1Zzg_mjmWB__3z11-fGe1zisy3ebnhJrutZVFpSQp9_PlEknAckDBbLsgpmgstyCGVyWPF2D2JslgN02TpA9i5BXEiNrtbz8DoXvXURGJEzm7HtCPKEyoDeDoOIeWOJD5SEyapsdweJqjru-BIzinbenm4C7XG43l0ay69fhCqpKAYdH6BYjHL0xnKIrNvf8g4O8G4sqgTNv1A9ObgRSHY8aXbhfijxRRyScXg_oitJpI0cLbBf5nCEJWvP1NuIdIy-T5iYDkH3p8aQGef36gAmyYq6enHlqLmmNcabNMCI_1mGpAhcyyLjc6HF98M5Jc0NVyRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار في تشابهار بايران</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83262" target="_blank">📅 22:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83261">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1ce4ff7e.mp4?token=T1ZAkujcPBidJKVeVpwPLYXS300lKYxpo6q9G6xpjMDcsW8hnzOuAxW1Hyvy_6Htr4F-pF5r4y-SS2vOeKUl5Yd6bFNz8aXzqNSptYPFRLgnobDzPW8P75YRGswf7aqwpVF-IUuhkADCkhCrNv422WSAEh_fXdAaVW_tKYGx5_iMBjtDB7dMqzUYXNi3qcyXyygErQqCXgjBMYdRtZmFHZ7M_u_SjzE0iLZ4wHkuUfUsYhaF7HdNzCRXKSFMESWOgzKTBMOmQabw3EcTsrn7jYBAztSg_QH-aEvD8FExWNFPXFlKP2dqWDV6IkCGkh0l3hZPGaEhtgNJ-xQC9NHvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1ce4ff7e.mp4?token=T1ZAkujcPBidJKVeVpwPLYXS300lKYxpo6q9G6xpjMDcsW8hnzOuAxW1Hyvy_6Htr4F-pF5r4y-SS2vOeKUl5Yd6bFNz8aXzqNSptYPFRLgnobDzPW8P75YRGswf7aqwpVF-IUuhkADCkhCrNv422WSAEh_fXdAaVW_tKYGx5_iMBjtDB7dMqzUYXNi3qcyXyygErQqCXgjBMYdRtZmFHZ7M_u_SjzE0iLZ4wHkuUfUsYhaF7HdNzCRXKSFMESWOgzKTBMOmQabw3EcTsrn7jYBAztSg_QH-aEvD8FExWNFPXFlKP2dqWDV6IkCGkh0l3hZPGaEhtgNJ-xQC9NHvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من اطلاق صواريخ من جانب الكويتي نحو الجمهورية الاسلامية الايرانية</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/83261" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee1c2bc5e.mp4?token=VyBNc971R7rO6fTSBvHZ1r9Vnd2kuFcHCJhi-h214WcObDVc2f912DgR7Yr2eb8fP6734HxpCr5KFtqpups6-NFtPp9Tbldm4W-1jIxQLTMi9HbpouW8ND4ezmo46BryX2bfKF-c1SaeU4sYH6FByghqw6Bqwj9BP3j1Gj21AbsCoyjQFvHNOM4kDg8dyX7Qof8GouZVWh_2KnjfjvEg-qJUirirl1-JetYpXu2OWXG-mn5DD2r03Wemp9svSgEKo1DovNGmvJeVTBI3Vmm2u2CSPSzC_RDwYmHacbNqCUHPI3nH85EmEw60GvseEP9iyIXEEyW07Tfy-U9Rhb8mSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee1c2bc5e.mp4?token=VyBNc971R7rO6fTSBvHZ1r9Vnd2kuFcHCJhi-h214WcObDVc2f912DgR7Yr2eb8fP6734HxpCr5KFtqpups6-NFtPp9Tbldm4W-1jIxQLTMi9HbpouW8ND4ezmo46BryX2bfKF-c1SaeU4sYH6FByghqw6Bqwj9BP3j1Gj21AbsCoyjQFvHNOM4kDg8dyX7Qof8GouZVWh_2KnjfjvEg-qJUirirl1-JetYpXu2OWXG-mn5DD2r03Wemp9svSgEKo1DovNGmvJeVTBI3Vmm2u2CSPSzC_RDwYmHacbNqCUHPI3nH85EmEw60GvseEP9iyIXEEyW07Tfy-U9Rhb8mSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار اطلاق الصواريخ من الكويت نحو ايران</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/83260" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83259">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مشاهد خاصة لنايا توثق لحظة اطلاق الكويت رشقة صاروخية نحو اراضي الايرانية</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/83259" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83258">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مشاهد خاصة لنايا توثق لحظة اطلاق الكويت رشقة صاروخية نحو اراضي الايرانية</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/83258" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83257">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8f71a3ea.mp4?token=qgHyMXJ3DRHNJ_QlqY8DnKTuWd_n1cjabb0X8CeTG1bGL4ESCFtmVXlM8ptPveIBMpLwbEr4kR_v6fwg207-DbIp8xjVi1G0IV_F-kxWdLmCnI6bUDi2UHzrGqv3gfdhKvxx9B4dJTLEl0osUFhLEcUKxUi3t7jRGCrsFn6hboKpAM75T9VrmMiF3MNeucBB4CtU_jb3Izxt7feAuFyJZW9zH5BcB84j3JyaI_o8rx-Y0XfyYCX66ltqk_NbZQouhCHpmLNR43koM99Kp5isxKH7vy7w2VeqU4otUfeAEYobnNg9OLOeSJRi6xH61mjd5e7P11mTePYiseGG4LKaNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8f71a3ea.mp4?token=qgHyMXJ3DRHNJ_QlqY8DnKTuWd_n1cjabb0X8CeTG1bGL4ESCFtmVXlM8ptPveIBMpLwbEr4kR_v6fwg207-DbIp8xjVi1G0IV_F-kxWdLmCnI6bUDi2UHzrGqv3gfdhKvxx9B4dJTLEl0osUFhLEcUKxUi3t7jRGCrsFn6hboKpAM75T9VrmMiF3MNeucBB4CtU_jb3Izxt7feAuFyJZW9zH5BcB84j3JyaI_o8rx-Y0XfyYCX66ltqk_NbZQouhCHpmLNR43koM99Kp5isxKH7vy7w2VeqU4otUfeAEYobnNg9OLOeSJRi6xH61mjd5e7P11mTePYiseGG4LKaNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شظايا صواريخ الباتريوت تتساقط على منازل المدنيين في محافظة اربيل شمالب العراق</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/83257" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83256">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=GY5jNt58MG0CVJYaabZI6_m3c9ENfJfUCHqwAlSDjP3eRbqvzMs04pRpUA_bDxpAZlNcuH_zXIuZ19_Zp4qjOxHaMH-R04JoXhGGzbkbIOS9xYGR0o7L84Di-vZormO4tnQ1IUPtfxVKpCfk3xHKTJKWVSo0vKHm7EB9pOm1E9gxXBTTyU0y5s7BOnJO7xl05jFG7VAGNRKI712RnO66nT-ooy2nspwjhxvXSqylTRx7yAgv80kIM_MNwpUxbcGMHvLuVI4Tu5A1tBUSbn9zPtwYJP_zOW50Rz9ipY2zt6EKF_4PtRRFXT7teu4N-T1KAEhNLXk91562-U-JzTfPxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=GY5jNt58MG0CVJYaabZI6_m3c9ENfJfUCHqwAlSDjP3eRbqvzMs04pRpUA_bDxpAZlNcuH_zXIuZ19_Zp4qjOxHaMH-R04JoXhGGzbkbIOS9xYGR0o7L84Di-vZormO4tnQ1IUPtfxVKpCfk3xHKTJKWVSo0vKHm7EB9pOm1E9gxXBTTyU0y5s7BOnJO7xl05jFG7VAGNRKI712RnO66nT-ooy2nspwjhxvXSqylTRx7yAgv80kIM_MNwpUxbcGMHvLuVI4Tu5A1tBUSbn9zPtwYJP_zOW50Rz9ipY2zt6EKF_4PtRRFXT7teu4N-T1KAEhNLXk91562-U-JzTfPxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انطلاق صواريخ من الكويت</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/83256" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83255">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انطلاق صواريخ من الكويت</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/83255" target="_blank">📅 22:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83254">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوي انفجار في الاهواز</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/83254" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83253">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الكويت تعلن استهداف قواعد الاحتلال  الاميركي اليوم باربعة صواريخ و ٢١ مسيرة.</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/83253" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83252">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نيران تشتعل من مقرات الاحزاب المعارضة في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83252" target="_blank">📅 22:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83251">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTki-4xDKXSqZToKvnNnquho7j2BkbaTyAGDhjXB9VJ1o3MF1P5iP4vfgRYd48MxOqqzrixzwqd9BXVK3yKhM2uWVkjVzzlu9bRrqbNutgnSqcfOiwNw9WzonYWUkffxiM1VqJt0eJe_7MH6TfnKIM85m5pybXqmuYnVVX-lMwTulZ8Gn6uxaTzQ4J31NA8DlYz1u_mnD7jFO7YGL0nG-5vKUZ4lTjiQhXRODvt2VbXR-EKViZm0IunrYgwjLLsvjHEtO431TE0iK53Lc6TL1Ffhgo-NqG31Q3LbmQYShVvB_PCC_btQBai3lF7fcFqJXVrpBJhcnPgAT5IRL_XbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوق امني شديد على مناطق سقوط المسيرات لمنع اي تصوير</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83251" target="_blank">📅 22:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83250">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نيران تشتعل من مقرات الاحزاب المعارضة في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/83250" target="_blank">📅 22:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83249">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a8e8e219.mp4?token=oPH1tfKeKIUBDtO5kFVkzdVfLMj0RcGvjkgmH6oc_QGkp6N7fwnp_Dc5irkCWttRTIN2lVhxzU08Kr_pJTrRtQ3UHBDtPV0rxJXuHl2LbUEpyeopCqNYZyLRES__pR070MaIADWtQE9_VQYB_jkG2noWW1nGDx-RlpCIO1SFwODYAzMcBMxgv9fZcxJs3Ve-gW8k3j8W5fh_yRxuVLsEbD6NV0y3IjFs05NGyfi31x3eIwvBqW8141t2g6eyfsHpwTmGODfjwEa7H21dBc6RCGlb9HKx9w9Fs_PgYOyn9G8LpFyeHZTpikzBQD0s7Dzu6w2VmJ93L47dn_NLBQp7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a8e8e219.mp4?token=oPH1tfKeKIUBDtO5kFVkzdVfLMj0RcGvjkgmH6oc_QGkp6N7fwnp_Dc5irkCWttRTIN2lVhxzU08Kr_pJTrRtQ3UHBDtPV0rxJXuHl2LbUEpyeopCqNYZyLRES__pR070MaIADWtQE9_VQYB_jkG2noWW1nGDx-RlpCIO1SFwODYAzMcBMxgv9fZcxJs3Ve-gW8k3j8W5fh_yRxuVLsEbD6NV0y3IjFs05NGyfi31x3eIwvBqW8141t2g6eyfsHpwTmGODfjwEa7H21dBc6RCGlb9HKx9w9Fs_PgYOyn9G8LpFyeHZTpikzBQD0s7Dzu6w2VmJ93L47dn_NLBQp7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار شديد في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/83249" target="_blank">📅 22:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83248">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجار شديد في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/83248" target="_blank">📅 22:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83247">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac0a37c1.mp4?token=Yyw_Eid9GVXkeBsIz9yfE5sPvFYoD9JnhmD92u-L8I58QzF-E_7ebbSn_KlXX4LzwE6WTQzL1Dlvhz8ABJSHncCLg1YPd2J4RpXQRR5ZZHRv2TH1CusCHgEczh6BposDB4WNmhmN507SAcCDxxQErIWVzGhfPUu1XzFvqiSp2rV71txgcIoDRAfvuE2h8TfP07VbJypGZLNJdW0UavGcccOkB1-uynsNffX4G4hCIr5ZFxqwXIbdrlln0lDehFOBk372f9LUMZsTvhhW_X27aGGzVc0bCIbCDO2H4r-xn8LUQWk856IdWrcNLwnl1Vw3avdAUoNGyRadt4DVwqVSdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac0a37c1.mp4?token=Yyw_Eid9GVXkeBsIz9yfE5sPvFYoD9JnhmD92u-L8I58QzF-E_7ebbSn_KlXX4LzwE6WTQzL1Dlvhz8ABJSHncCLg1YPd2J4RpXQRR5ZZHRv2TH1CusCHgEczh6BposDB4WNmhmN507SAcCDxxQErIWVzGhfPUu1XzFvqiSp2rV71txgcIoDRAfvuE2h8TfP07VbJypGZLNJdW0UavGcccOkB1-uynsNffX4G4hCIr5ZFxqwXIbdrlln0lDehFOBk372f9LUMZsTvhhW_X27aGGzVc0bCIbCDO2H4r-xn8LUQWk856IdWrcNLwnl1Vw3avdAUoNGyRadt4DVwqVSdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83247" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83246">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر... اصابات في صفوف الجيش الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/83246" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83245">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc6f11fe5.mp4?token=TndfTEVZDpSUX-PFErt38x_gk_BzfJEA68WbplcqQyjB56Q3xhMncmn4RJ4oWxojigdJ1kttnsmuWFUau0W2cRThlc2EJPcP0clzhTCv1CQ5RjmkS-jTc9z4xAmZIemcgYPTDKAVF4DHp3M3wdM3ZcYyGy54JAbLH1zdQgTHMqUvtyVqYi4pIzokjBj91OrPXKYsDrzgcPqc3KzCJ_fNcyo_WwpBUVEGLgmcM2KbpOmZvQe-I4Zoksv0K9lsRSSaELtQ85A9iSZzAOXtBReArUFW5IokCrzUJXAjQ3rs_QRPy7LEXPjzZNq6kUG4HLZllMsEXTOtT_L1VRrjsiJJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc6f11fe5.mp4?token=TndfTEVZDpSUX-PFErt38x_gk_BzfJEA68WbplcqQyjB56Q3xhMncmn4RJ4oWxojigdJ1kttnsmuWFUau0W2cRThlc2EJPcP0clzhTCv1CQ5RjmkS-jTc9z4xAmZIemcgYPTDKAVF4DHp3M3wdM3ZcYyGy54JAbLH1zdQgTHMqUvtyVqYi4pIzokjBj91OrPXKYsDrzgcPqc3KzCJ_fNcyo_WwpBUVEGLgmcM2KbpOmZvQe-I4Zoksv0K9lsRSSaELtQ85A9iSZzAOXtBReArUFW5IokCrzUJXAjQ3rs_QRPy7LEXPjzZNq6kUG4HLZllMsEXTOtT_L1VRrjsiJJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/83245" target="_blank">📅 21:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83244">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سيارات الاسعاف تهرع الى مكان سقوط المسيرة</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/83244" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83241">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c94b836aa.mp4?token=JlczbyYgIDfY4Of4vSsScQArI62c0_waIfFuPy0Q3-XZRvKY6rKhKtn9dOOmJMYlOp5F9mjaKbUvjqQ1RUiTksjMbyYxJ0COTr-sP0D19hHgaFARnAArkMKY93FJ_QLc6mGfjg3tPAZYXfZuSjkCVnXYqY5YC7SRkBNi0vimr6gdlVkCuB3n7eJviTYi7uaXRgWSBMgyA0HTAIE3EPX-pzhPFEIL1v_H9WhUu8b78DqkKRxamTFecfX4fSNu_ydop6S2bQ91igh9o0sfblgb4s_Fwu6JyfJ8Yt8nU-OgP0D5S2UlcLMowEJjNFuzDimPKRBZW4VP9de0CEClI6PCGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c94b836aa.mp4?token=JlczbyYgIDfY4Of4vSsScQArI62c0_waIfFuPy0Q3-XZRvKY6rKhKtn9dOOmJMYlOp5F9mjaKbUvjqQ1RUiTksjMbyYxJ0COTr-sP0D19hHgaFARnAArkMKY93FJ_QLc6mGfjg3tPAZYXfZuSjkCVnXYqY5YC7SRkBNi0vimr6gdlVkCuB3n7eJviTYi7uaXRgWSBMgyA0HTAIE3EPX-pzhPFEIL1v_H9WhUu8b78DqkKRxamTFecfX4fSNu_ydop6S2bQ91igh9o0sfblgb4s_Fwu6JyfJ8Yt8nU-OgP0D5S2UlcLMowEJjNFuzDimPKRBZW4VP9de0CEClI6PCGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الانطلاق الباتريوت من قاعدة الاحتلال الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/83241" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83240">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b22f1b7d.mp4?token=JYPS0zRaeEfJ80ah7OmB7M0lF0cPteph6adYJaNastHuau6s8J-PPje03Nak4Eqcgv2v3Le911MFNYBeFcmevXXS_a80jaJvInXAh4fdDlwQCpdq2fo49eVVGT_Sb8L1Q9WRfJohnwdZCYgHurKHsyr_5uzb6LddXRw6mpgG9iywBCetXJ4fRE7PGaim00vZv2J9joZZvbK6hwbcTeyBfD4WIPQxQT-nwjMLZo9pJ2HgEmW8EfrZTQXJEG_zhJg7yJBE2J27_SohhwmCbztNzwfOHYM9cVLAD3tbBKLFCFxn57hc0DNd2Dl4Xgciq0VkCN-SWWLA01_nI7A1Y96qyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b22f1b7d.mp4?token=JYPS0zRaeEfJ80ah7OmB7M0lF0cPteph6adYJaNastHuau6s8J-PPje03Nak4Eqcgv2v3Le911MFNYBeFcmevXXS_a80jaJvInXAh4fdDlwQCpdq2fo49eVVGT_Sb8L1Q9WRfJohnwdZCYgHurKHsyr_5uzb6LddXRw6mpgG9iywBCetXJ4fRE7PGaim00vZv2J9joZZvbK6hwbcTeyBfD4WIPQxQT-nwjMLZo9pJ2HgEmW8EfrZTQXJEG_zhJg7yJBE2J27_SohhwmCbztNzwfOHYM9cVLAD3tbBKLFCFxn57hc0DNd2Dl4Xgciq0VkCN-SWWLA01_nI7A1Y96qyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الانطلاق الباتريوت من قاعدة الاحتلال الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83240" target="_blank">📅 21:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83239">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5eb63bb7.mp4?token=P3eOXOafN4OPWuu7d0nyW6E5FcHt1COEYqUIJboEsCcUhfAWVc9l0s0dwOf0x1kZKRfLVhzoLxsJWAYu-krFgvfC-UVmOeKyFzAMnQ4TS3weSKTe5gIghFwhZZOLwznroNoepGVepc6AThqVeSVl-1hSzq70EKzt_aTD1BiVZ6XqzViU3l65fySF6lVTnDkugynSYi_q6k0TzNKRjRdbj4YAc-9lmdtBNyg-bQXwaJG3qtkGyNGOzniHJ8ql_gAcJZQOzF_pbn1zeR_uFiTcz06WtgYaku6zzbcABKrRHezUZTaz5wPqYdK875nK7FiC2Ey8cp-zq4CP7TXjggKcPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5eb63bb7.mp4?token=P3eOXOafN4OPWuu7d0nyW6E5FcHt1COEYqUIJboEsCcUhfAWVc9l0s0dwOf0x1kZKRfLVhzoLxsJWAYu-krFgvfC-UVmOeKyFzAMnQ4TS3weSKTe5gIghFwhZZOLwznroNoepGVepc6AThqVeSVl-1hSzq70EKzt_aTD1BiVZ6XqzViU3l65fySF6lVTnDkugynSYi_q6k0TzNKRjRdbj4YAc-9lmdtBNyg-bQXwaJG3qtkGyNGOzniHJ8ql_gAcJZQOzF_pbn1zeR_uFiTcz06WtgYaku6zzbcABKrRHezUZTaz5wPqYdK875nK7FiC2Ey8cp-zq4CP7TXjggKcPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من ارتفاع النيران اثر سقوط مباشر لطائرة مسيرة على هدفها في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/83239" target="_blank">📅 21:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83237">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fbce8a46d.mp4?token=qOqAVWj3lIF28vQR9YchK0_11PXwJtE2kdvUn4iTOmnepQ5STNjnai77415PeJOeP3-y1mWuQ4LVGnYNWLWWraTGBs5xVlJuHlrSvQrO73ATfNMyl3rtkoSjoKM0LoJ9g8h4qQp_UeCm6FaASXChkMC9Zpr5QboUqFu4RsHAIHku3vZC-iQaHswXjfN1_Bc5OwR0I9gVIFMaX8LfAUeKDT_pd5YbpJim-KZy9cMgZdFEprHAGXb5qIUM9IVcOHyDqdWlXdl_biEy-nFOspXfPB3iKS8bnmBG88bxo8E1UP2hkoI-wydBC2QROI-3YxSpD1-irTdET7vx6k63jR5EXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fbce8a46d.mp4?token=qOqAVWj3lIF28vQR9YchK0_11PXwJtE2kdvUn4iTOmnepQ5STNjnai77415PeJOeP3-y1mWuQ4LVGnYNWLWWraTGBs5xVlJuHlrSvQrO73ATfNMyl3rtkoSjoKM0LoJ9g8h4qQp_UeCm6FaASXChkMC9Zpr5QboUqFu4RsHAIHku3vZC-iQaHswXjfN1_Bc5OwR0I9gVIFMaX8LfAUeKDT_pd5YbpJim-KZy9cMgZdFEprHAGXb5qIUM9IVcOHyDqdWlXdl_biEy-nFOspXfPB3iKS8bnmBG88bxo8E1UP2hkoI-wydBC2QROI-3YxSpD1-irTdET7vx6k63jR5EXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجاريين مجددا في محافظة اربيل</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/83237" target="_blank">📅 21:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83236">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجار ثالث في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/83236" target="_blank">📅 21:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83235">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30261b70a.mp4?token=vRRzVED8pi91TrpWjV2qfET_pWSxjAvs2X0U7BShVLdrFgdszys4ffBtR9cqWvYhZ-3Pm3hm0lFX1PEUwPgTr_Bfj3sOHDHKo1iDhW7TlQdR4n1bgBpvVM27KN7VdS7qTp7qZ4jon3-mKlbdEVGArAaxjU6yu3AnGXe9fGpLFcmBcP6Aul7UiBNfCvWAjeaOd7xK6BAzSmFl-lydjfOFhVFd89XWISNq_X6pL3YUnURbdBXLACa-Uqo421tnzy6yQAjf5wPa8vZv8QDyoDlt6qcVFlpKGVlT90DKaWWeBcrEQrr8e2rDLfoL4k0dUNEK74ZpyneMLOi2y7aP2Uvriw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30261b70a.mp4?token=vRRzVED8pi91TrpWjV2qfET_pWSxjAvs2X0U7BShVLdrFgdszys4ffBtR9cqWvYhZ-3Pm3hm0lFX1PEUwPgTr_Bfj3sOHDHKo1iDhW7TlQdR4n1bgBpvVM27KN7VdS7qTp7qZ4jon3-mKlbdEVGArAaxjU6yu3AnGXe9fGpLFcmBcP6Aul7UiBNfCvWAjeaOd7xK6BAzSmFl-lydjfOFhVFd89XWISNq_X6pL3YUnURbdBXLACa-Uqo421tnzy6yQAjf5wPa8vZv8QDyoDlt6qcVFlpKGVlT90DKaWWeBcrEQrr8e2rDLfoL4k0dUNEK74ZpyneMLOi2y7aP2Uvriw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ثالث في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/83235" target="_blank">📅 21:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83234">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الدفاعات الجوية تنطلق من قاعدة الاحتلال الاميركي في محافظة اربيل</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/83234" target="_blank">📅 21:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83233">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83233" target="_blank">📅 21:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83232">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اربيل مجددا</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83232" target="_blank">📅 21:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83231">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اربيل مجددا</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83231" target="_blank">📅 21:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83230">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مشاهد من ارتفاع النيران اثر سقوط مباشر لطائرة مسيرة على هدفها في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/83230" target="_blank">📅 21:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83229">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الانذارات ما زالت تدوي في قاعدة الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/83229" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83228">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5d097613.mp4?token=G-AGDEooOPjCJbrLuoMR3DEqxYM7ZHAiCX3dOdZIQ1dGzCUKgffKaKnJoPZg8lG4AwJ7yrfh5oBNA1h7cTWs9YMg60jmcc1-IhD6eusuc5iopjX2I3dG3NbRjsWuGoqIN0U3ycEdrIw3ievtFWy8ViJ_gvhSBaNTSwKw8W43GLVYMA70HLGDGgGgYAsHzJRqC4UQOQ4f8EOu2ut9UqBO3qYP0WTxvELcEywKj2YPGfTVQi420qxmrmqM9WfIjXvdPBoplwHNzmtL4m9Is5UHd9L4u6nlOT8BuNL5gI29Fp6UjBsIIoWSuSEVidqUzGIM_xiluXvXIesS4Wc71PicTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5d097613.mp4?token=G-AGDEooOPjCJbrLuoMR3DEqxYM7ZHAiCX3dOdZIQ1dGzCUKgffKaKnJoPZg8lG4AwJ7yrfh5oBNA1h7cTWs9YMg60jmcc1-IhD6eusuc5iopjX2I3dG3NbRjsWuGoqIN0U3ycEdrIw3ievtFWy8ViJ_gvhSBaNTSwKw8W43GLVYMA70HLGDGgGgYAsHzJRqC4UQOQ4f8EOu2ut9UqBO3qYP0WTxvELcEywKj2YPGfTVQi420qxmrmqM9WfIjXvdPBoplwHNzmtL4m9Is5UHd9L4u6nlOT8BuNL5gI29Fp6UjBsIIoWSuSEVidqUzGIM_xiluXvXIesS4Wc71PicTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع نيران من قاعدة الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/83228" target="_blank">📅 21:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نيران ترتفع الله اكبر</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/83227" target="_blank">📅 21:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83226">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ارتفاع نيران من قاعدة الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/83226" target="_blank">📅 21:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/83225" target="_blank">📅 21:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114a4f57d6.mp4?token=I5AtvBxZmkE1YXuYjYkf8KdjcnmKtPHoP218L27uBQMVpzr4oSIgoD-a2xNaDgCVym-RU1eL0UNJZwVtBHcXcAbwyJXHgZvHKX_eAbLY_5PkiXjBR9o2riaXmhoedbaeMxhLg3Jfls9UKcmc1eh_n6jPps-5OMoTRDtAhRUM0mF5ZvYaMU-QfuruX-4OO2kJP7rtxSJBWXR8zO5Q-q5jf0TMWSX3s18pCh-ID-fXp5704fP81Tp3QrUtcj0djM_RKkpnUyHAWz9mORXmtYUNg_LSy6bDzh1O1tuSBxhFjlrVHVmx9BvIZCYpEV4SCw5hnua56CxrcPUK2LJFg2bt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114a4f57d6.mp4?token=I5AtvBxZmkE1YXuYjYkf8KdjcnmKtPHoP218L27uBQMVpzr4oSIgoD-a2xNaDgCVym-RU1eL0UNJZwVtBHcXcAbwyJXHgZvHKX_eAbLY_5PkiXjBR9o2riaXmhoedbaeMxhLg3Jfls9UKcmc1eh_n6jPps-5OMoTRDtAhRUM0mF5ZvYaMU-QfuruX-4OO2kJP7rtxSJBWXR8zO5Q-q5jf0TMWSX3s18pCh-ID-fXp5704fP81Tp3QrUtcj0djM_RKkpnUyHAWz9mORXmtYUNg_LSy6bDzh1O1tuSBxhFjlrVHVmx9BvIZCYpEV4SCw5hnua56CxrcPUK2LJFg2bt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة اطلاق صاروخ اعتراضي من قاعدة الاحتلال الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83224" target="_blank">📅 21:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddac2c158.mp4?token=CB00Mm_gIXHH7iP3Lo5dPAeSN3Oz43gdP3aMYKu_jWN5s8nUIQqPPf8a0WKURILUyq0lLGqonmmKRXcjqvgOXUuquPfBbcc7e3DxFJXPv88ZRopaZ20NOmKwA_44t-k6r3Pd6cVLWMTtaePow_oLL9dwQOeIOvJZqS0IglwNDcnXycCbg-yPmSMeeKnaJiZ_5KeQ_JV0NGH4hODdXRW9oW5MXTqu5dsGT0Xb3zv7WOaoZHKy83KcgFQuOjQ_UnbCXEfRbPI3iYqh-segCi1iSMVj6h8rftaVCHQGWGB0VMaWh6z0Y6FtsefvZIlM5hh7BJaCNPAZ_90-GNu9imm0eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddac2c158.mp4?token=CB00Mm_gIXHH7iP3Lo5dPAeSN3Oz43gdP3aMYKu_jWN5s8nUIQqPPf8a0WKURILUyq0lLGqonmmKRXcjqvgOXUuquPfBbcc7e3DxFJXPv88ZRopaZ20NOmKwA_44t-k6r3Pd6cVLWMTtaePow_oLL9dwQOeIOvJZqS0IglwNDcnXycCbg-yPmSMeeKnaJiZ_5KeQ_JV0NGH4hODdXRW9oW5MXTqu5dsGT0Xb3zv7WOaoZHKy83KcgFQuOjQ_UnbCXEfRbPI3iYqh-segCi1iSMVj6h8rftaVCHQGWGB0VMaWh6z0Y6FtsefvZIlM5hh7BJaCNPAZ_90-GNu9imm0eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة اطلاق صاروخ اعتراضي من قاعدة الاحتلال الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83223" target="_blank">📅 21:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e16e21dc2.mp4?token=FSyGJaPOEfrzby44x81d1sVQ_eNvxsGMM2TMGTSeVtEhohc-ugCQ3IdTzI5A1s1ZxObfTP9tTXsTsXvzc9BzysrIL0Ma6_R1JjE4jEt94BBe5l9_CP6dO6jzEKmvwJKQUL12zVx0lwLjv1wxd77zy19rAeUvlh7qwKLgNMEMQoOspPEPt77hV8ElFhj2XDHmBMM_ZHwlQkbrpmA4lVlEPNHbUN7gALHtS9F6ezF83JAB13S3eRgYgOW_m8uHErQvjZNXQpc_ybp3fuiIkVGBVsaaW6_4pPLej2NP7a2bGAfE8LGGlQl9TovHiYWh9VbZAUfQ1pocIyn_tIKZ4r4n-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e16e21dc2.mp4?token=FSyGJaPOEfrzby44x81d1sVQ_eNvxsGMM2TMGTSeVtEhohc-ugCQ3IdTzI5A1s1ZxObfTP9tTXsTsXvzc9BzysrIL0Ma6_R1JjE4jEt94BBe5l9_CP6dO6jzEKmvwJKQUL12zVx0lwLjv1wxd77zy19rAeUvlh7qwKLgNMEMQoOspPEPt77hV8ElFhj2XDHmBMM_ZHwlQkbrpmA4lVlEPNHbUN7gALHtS9F6ezF83JAB13S3eRgYgOW_m8uHErQvjZNXQpc_ybp3fuiIkVGBVsaaW6_4pPLej2NP7a2bGAfE8LGGlQl9TovHiYWh9VbZAUfQ1pocIyn_tIKZ4r4n-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ثاني</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83221" target="_blank">📅 21:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83219">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31667cc92.mp4?token=RXlxtABrf1b4n6TSdOwKErMJPjBS08gc5geKBVL7-452jT9kgfYDuKiFyxdKKEFM7XfG2tb4UTwNP6ppdbVe0eaaiHipVQozFenGJsbCVXfhhMncLkot949bq-JTqUX0jYA6xe_6mW6iTJMZtoARFCeVIrpn66l8xpWiKgjs13uWCpxvGQoZlTeVtjdGcXCkpNXNi3nrK6UAVX8bC9J2ByIU7PBmP6ShfiYMhBPnadUsWS-fe-eA61gijsnEp1yuY56t5bAVrA34iO60EHfjjPjdXWu28WTfvwO0KURqNe-pIvouREPtQhu15ZDbvwdfyTPm38blr66ZDwoH9TS1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31667cc92.mp4?token=RXlxtABrf1b4n6TSdOwKErMJPjBS08gc5geKBVL7-452jT9kgfYDuKiFyxdKKEFM7XfG2tb4UTwNP6ppdbVe0eaaiHipVQozFenGJsbCVXfhhMncLkot949bq-JTqUX0jYA6xe_6mW6iTJMZtoARFCeVIrpn66l8xpWiKgjs13uWCpxvGQoZlTeVtjdGcXCkpNXNi3nrK6UAVX8bC9J2ByIU7PBmP6ShfiYMhBPnadUsWS-fe-eA61gijsnEp1yuY56t5bAVrA34iO60EHfjjPjdXWu28WTfvwO0KURqNe-pIvouREPtQhu15ZDbvwdfyTPm38blr66ZDwoH9TS1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاعدة الاحتلال الاميركي تشتعل في محافظة اربيل</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/83219" target="_blank">📅 21:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83218">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قاعدة الاحتلال الاميركي تشتعل في محافظة اربيل</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/83218" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83217">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83217" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83216">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صفارات الانذار تدوي في قاعدة الاحتلال الاميركي في اربيل</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83216" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83215">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صفارات الانذار تدوي في قاعدة الاحتلال الاميركي في اربيل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/83215" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83214">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed09536ad4.mp4?token=rv5tF5wSFWhGElbnKU0AKkrFfTzIspx1CwoRyYH7VEx0CuXCJ-LqdILQ2VhVO6S9MzgCYeuKw463n94kHgN_jlgOkHnYUWR-ktvPPc-0WYh_Fgb4Am5D7an1ZIdPx9ueKd2MsgDfPKTVsRejBsGTfA2q5uU724G62O9w8mXvAWsBova5qTW46oW4uObkBM9UGkwgtgRBUitn5vzvOjHCeUOFF51mBDQ3hS9h4EPt6rvJiKqWfrsMo2-hQ8XPmI44OiAKs2cHTY8XX_hua8dzNSGyuZ0EjICLptkmauLwcxrZ4wPrpxE_ZYnM70Xwznhh3VjBpGwMUZkzJyR61hmUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed09536ad4.mp4?token=rv5tF5wSFWhGElbnKU0AKkrFfTzIspx1CwoRyYH7VEx0CuXCJ-LqdILQ2VhVO6S9MzgCYeuKw463n94kHgN_jlgOkHnYUWR-ktvPPc-0WYh_Fgb4Am5D7an1ZIdPx9ueKd2MsgDfPKTVsRejBsGTfA2q5uU724G62O9w8mXvAWsBova5qTW46oW4uObkBM9UGkwgtgRBUitn5vzvOjHCeUOFF51mBDQ3hS9h4EPt6rvJiKqWfrsMo2-hQ8XPmI44OiAKs2cHTY8XX_hua8dzNSGyuZ0EjICLptkmauLwcxrZ4wPrpxE_ZYnM70Xwznhh3VjBpGwMUZkzJyR61hmUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة اطلاق صاروخ باتريوت من قاعدة الاحتلال الاميركي في محافظة اربيل</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83214" target="_blank">📅 21:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83213">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55edbe3c89.mp4?token=lzinxrZPM1AmyI0XrWe-AAd9mxzADRTM_R5xP9nTGOq5rSa2QHAHLueh7HpWcWgwlLCY_YGwPvx4gBoBRdxiFKV931v09aTj6-z7is90mQDuRns-jp8GJU0bAm9W_LnDRmmSy8MKDHd1VCemhPiq8rROUIOAB70jMpw9Or1Mz_eW_d2DbdqGvs7IWbcaJOxRJiIGawPxRdvfGluUJk4qbdskjgyhVtNSZ5QbApqHmOnhJZmCGnvPUaJ8FRxOfE3aMFx67L7poSpciXZvuTguVggxMH4F4urLyU_IpjTqrB0_-iVz7GG7z2Ta296xadiDsFlTZQjEQYon_SCfXUz0yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55edbe3c89.mp4?token=lzinxrZPM1AmyI0XrWe-AAd9mxzADRTM_R5xP9nTGOq5rSa2QHAHLueh7HpWcWgwlLCY_YGwPvx4gBoBRdxiFKV931v09aTj6-z7is90mQDuRns-jp8GJU0bAm9W_LnDRmmSy8MKDHd1VCemhPiq8rROUIOAB70jMpw9Or1Mz_eW_d2DbdqGvs7IWbcaJOxRJiIGawPxRdvfGluUJk4qbdskjgyhVtNSZ5QbApqHmOnhJZmCGnvPUaJ8FRxOfE3aMFx67L7poSpciXZvuTguVggxMH4F4urLyU_IpjTqrB0_-iVz7GG7z2Ta296xadiDsFlTZQjEQYon_SCfXUz0yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باتريوت يتفعل</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/83213" target="_blank">📅 21:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83212">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417a6060b0.mp4?token=u5QxFunrvECeWKUcJOJLijqg_kouGt9OXyv8xTK6kTyKmIP_HbUlLaYcp_Yf2vKYexQnkSiMXxkUX1hJYkX9WLuWOcpY5ndKqGNQEgUUNRW_V41wH36XNq8g_p_F7sAqnCHSYZt-dTAo6-BL2HVt9A53Ns_hEGvvMMgbwafUvGbFO3h7lNvuXaDHY74HaYzjb33sgZUZsJAbKaIWKTijOoOcXxBw8U1kcICGQKJAJvqShylnutMe1_N2hhYAULslE3C4hpSg4swxlqCVkjBOXsBG5AJo0SmvFyWYjDhylIJ1Tt5U9aK7gz19aYsyWy9i7FwMGAbJVvObkAher8j8_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417a6060b0.mp4?token=u5QxFunrvECeWKUcJOJLijqg_kouGt9OXyv8xTK6kTyKmIP_HbUlLaYcp_Yf2vKYexQnkSiMXxkUX1hJYkX9WLuWOcpY5ndKqGNQEgUUNRW_V41wH36XNq8g_p_F7sAqnCHSYZt-dTAo6-BL2HVt9A53Ns_hEGvvMMgbwafUvGbFO3h7lNvuXaDHY74HaYzjb33sgZUZsJAbKaIWKTijOoOcXxBw8U1kcICGQKJAJvqShylnutMe1_N2hhYAULslE3C4hpSg4swxlqCVkjBOXsBG5AJo0SmvFyWYjDhylIJ1Tt5U9aK7gz19aYsyWy9i7FwMGAbJVvObkAher8j8_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باتريوت يتفعل</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/83212" target="_blank">📅 21:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83211">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ac131c7d.mp4?token=RWZfdKejRcrgMWtwZG4SoFL3Q1u3Mj7j9e1OA-wL_LByibwubuwxHJB7WgUl9Kjxz1AjDXUbSW6m13NC8QVIx5_61Y58C9N06IDwOau-6RY0CfsYjA_qeBe73gagK5c42Dz3GE0bK8Yx9z4sbkz3EClc4y98aANZlHQFzGIH2Qp1RsCLwtyGsCQmYHuUOmaeR4TD7SUW3LhdgYb8WDDEu-v7-S9XTJsUlITOPnmAawJcuqGCJLKAUUUzMhWP4en62oRboQXoBlaZRabjoY3breW8lqwt_fuMEwGlu6Nb-RRB0nV3WNx_Vpw7tB5VdeLwsmvGYXCoC_DPNKDp0UV6Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ac131c7d.mp4?token=RWZfdKejRcrgMWtwZG4SoFL3Q1u3Mj7j9e1OA-wL_LByibwubuwxHJB7WgUl9Kjxz1AjDXUbSW6m13NC8QVIx5_61Y58C9N06IDwOau-6RY0CfsYjA_qeBe73gagK5c42Dz3GE0bK8Yx9z4sbkz3EClc4y98aANZlHQFzGIH2Qp1RsCLwtyGsCQmYHuUOmaeR4TD7SUW3LhdgYb8WDDEu-v7-S9XTJsUlITOPnmAawJcuqGCJLKAUUUzMhWP4en62oRboQXoBlaZRabjoY3breW8lqwt_fuMEwGlu6Nb-RRB0nV3WNx_Vpw7tB5VdeLwsmvGYXCoC_DPNKDp0UV6Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متتالية تستهدف محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/naya_foriraq/83211" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83210">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc330fef5f.mp4?token=nvDze9NwT0zEFXcEswHopGftkvaQKKDSWY2VjOp8F-pnejYevnYg9yAuE5SjaCcDC7ilrSSPhrLCZ2JeIuxDn0bM06h4Bulxnf7tVq7Oo5Sv7W6dBhkdiNKF3JpKee1MO02WU4z07KGjH7bEqURcjMWsInFaJlhgnLnB1JJ1mXHwcaI0aNfVN1G5Vm7OF_CV36F1MDFmsSIpOw78sRXvJkuY4RzyKEgLoygrMG8TRoQYj53jwMvkty81nkkgf8QCFRV40D1J-k2Sj5pH5zmt-svcYdcpwsdRsjPNHVRpKczMny-nf2fBnbOyWmtOwZ8tpMk7uG-Ap65Puey7ox8VKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc330fef5f.mp4?token=nvDze9NwT0zEFXcEswHopGftkvaQKKDSWY2VjOp8F-pnejYevnYg9yAuE5SjaCcDC7ilrSSPhrLCZ2JeIuxDn0bM06h4Bulxnf7tVq7Oo5Sv7W6dBhkdiNKF3JpKee1MO02WU4z07KGjH7bEqURcjMWsInFaJlhgnLnB1JJ1mXHwcaI0aNfVN1G5Vm7OF_CV36F1MDFmsSIpOw78sRXvJkuY4RzyKEgLoygrMG8TRoQYj53jwMvkty81nkkgf8QCFRV40D1J-k2Sj5pH5zmt-svcYdcpwsdRsjPNHVRpKczMny-nf2fBnbOyWmtOwZ8tpMk7uG-Ap65Puey7ox8VKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من سماء محافظة اربيل</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/83210" target="_blank">📅 21:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83209">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBYITVX-6BnCw6plij5JFjROv7ulo3RpscZTFY9XSZ7d6UK1pQuJZR6SMWV3fVzxiRX9UAJDURVFZ_TnvgIS-S2DT5VriKmuDAUpDCDCeEHUQB1rSXF1qCREfCBK9RKhO1PR7IAg_TZPBc4RrI9-4EwJDOiA0PKlJxpa8KxBrZlVCOmsFFdjCWCge4cGbbq0pMWXQDc2liZcFBEXyo3MHgFGiaXnlJCMZGAqqUtxkkf4-zlQO02fr1aRyWUV73ebk5bxA2644g315rptD6XJYg_Qy7V69eJq-Bs_IMLw800Qm9NvoZtwCTX9yKykQ73-tBEAaHHfFm7ggXuA9X7igA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات متتالية تستهدف مقرات المعارضة في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/83209" target="_blank">📅 21:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83208">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1af1dbfa2.mp4?token=lquFwsaPyWXddIFcGS8Nny8m-C_xYPTmE2yNCOBSDkrUM7JPvaaw_CSBQf-7acOH64GsROic6NDgDkpAdHOqzLXpCoWCX9Yaghu83cqhABlHyzRUyND7Jfp2ZyhwbjnLonpGVHLmBnxGHbHMF00V6-fwqcLcxKuBtQyR3rhwFiuyns8xFy0MhtxU8e7z3qKPDqCo7FojqB2xJzCbq2ZzMzs4Q9Ttwx1_jld9H6zdpW7_5KVBZ0d6tCr2iEd09eQt3W5JpCdr7EMFpmXuyeQ-2_eb5Bh_lMUhXZH3_KLzmDugEqfMptSq0lXd0MWK204pOgRQDZMLWzmI6_qeHFGxsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1af1dbfa2.mp4?token=lquFwsaPyWXddIFcGS8Nny8m-C_xYPTmE2yNCOBSDkrUM7JPvaaw_CSBQf-7acOH64GsROic6NDgDkpAdHOqzLXpCoWCX9Yaghu83cqhABlHyzRUyND7Jfp2ZyhwbjnLonpGVHLmBnxGHbHMF00V6-fwqcLcxKuBtQyR3rhwFiuyns8xFy0MhtxU8e7z3qKPDqCo7FojqB2xJzCbq2ZzMzs4Q9Ttwx1_jld9H6zdpW7_5KVBZ0d6tCr2iEd09eQt3W5JpCdr7EMFpmXuyeQ-2_eb5Bh_lMUhXZH3_KLzmDugEqfMptSq0lXd0MWK204pOgRQDZMLWzmI6_qeHFGxsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من سماء محافظة اربيل</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/83208" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83207">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43909b01f7.mp4?token=jhW1IdQAQmZRzKENFN7hweJ4AWUDn38Jw-oZlX5mCEIGrn67zjYraQwm6yWTcMD-yHGQY8rg44KoYV3sYOhQpGX9ViCGDyDh0OuIk1CqDkTrqWHFb2WCQAIgWyAxmG8VjcAZCH92x7m5LAMTJfBTYuXjcHzZhBDv29pwr2fhMOtGdYr3ZCVVADhA6gHSIkpkuhdj7NFOQbBowxubpbgZDlM_GtDEEDrNOEyyo1y6bbCbhZuc6W007eYNcZUiT741LLOrQC8if6vrVSQeQ0dFSiBgKnWt0_ZI9bZPSUic0Aj7ZIE5L2GOTMN_i8fXh7yIpqKIX-Vv302QuC0qcKu11A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43909b01f7.mp4?token=jhW1IdQAQmZRzKENFN7hweJ4AWUDn38Jw-oZlX5mCEIGrn67zjYraQwm6yWTcMD-yHGQY8rg44KoYV3sYOhQpGX9ViCGDyDh0OuIk1CqDkTrqWHFb2WCQAIgWyAxmG8VjcAZCH92x7m5LAMTJfBTYuXjcHzZhBDv29pwr2fhMOtGdYr3ZCVVADhA6gHSIkpkuhdj7NFOQbBowxubpbgZDlM_GtDEEDrNOEyyo1y6bbCbhZuc6W007eYNcZUiT741LLOrQC8if6vrVSQeQ0dFSiBgKnWt0_ZI9bZPSUic0Aj7ZIE5L2GOTMN_i8fXh7yIpqKIX-Vv302QuC0qcKu11A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجار قوي في اربيل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/83207" target="_blank">📅 21:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوي انفجار قوي في اربيل</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83206" target="_blank">📅 21:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏فانس يتراجع عن قرار حكومته
😆
: لن نرسل قوات لإيران لتغيير النظام.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83205" target="_blank">📅 21:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
فانس
يتراجع عن قرار حكومته
😆
: لن نرسل قوات لإيران لتغيير النظام.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83204" target="_blank">📅 21:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
قالليباف
:
يجب أن نكون دائمًا على أهبة الاستعداد للمعركة، وأن ندافع حتى الموت عن أمننا القومي ومصالحنا. لم نرحب بالحرب قط، ولن نفعل، ولكن يجب أن نكون دائمًا على أهبة الاستعداد للمعركة، وأن ندافع حتى الموت عن أمننا القومي ومصالحنا. كما يجب علينا استخدام أدوات الدبلوماسية والتفاوض لتحقيق المصالح الوطنية وتوطيدها.
في هذه الأيام، وقد اشتعلت نيران الحرب من جديد، تُطرح تساؤلات بين مختلف الأفراد والجماعات، ويجيب كلٌّ منهم عنها من منظوره الخاص. هل نسعى إلى الحرب؟ هل ستنتهي الحرب وظلالها؟ هل يمكننا تحقيق أهدافنا عبر التفاوض؟ في ظل مواجهة أمريكا غير الموالية، ما جدوى التفاوض؟ وفي نهاية المطاف، السؤال الأهم هو: كيف نستعيد حقوقنا وننتصر في هذه الحرب؟
إذا نظرنا إلى هذه القضية من منظور المصالح الوطنية والأمن القومي، بعيدًا عن أي منظور حزبي، فسنتمكن من الوصول إلى إجابات واضحة ودقيقة. أولًا، يجب أن ندرك أننا نخوض حربًا وجودية مع أمريكا، هدفها ليس فقط إسقاط النظام المقدس للجمهورية الإسلامية الإيرانية بوصفها المؤسسة الرئيسية للجبهة اليمينية، بل أيضًا تمزيق أوصال وطننا الحبيب إيران. لم تتغير استراتيجية هذا العدو.
ثانيًا، كما ذكرت مرارًا، تسعى أمريكا إلى ضرب إيران وتعزيز مصالحها كلما سنحت لها الفرصة، وهذا لا يقتصر على الحرب أو المفاوضات أو حتى على الرئيس الأمريكي الحالي. لذا، يجب أن تستند نظرتنا إلى الحرب أو المفاوضات على المصالح والأمن القومي، وأن تكون واقعية وطويلة الأمد. لذلك، ليس أمامنا خيار سوى الاعتماد على قوتنا الذاتية وتعزيزها. ثالثًا، لقد أحبطت المقاومة الموحدة للشعب الإيراني وقواتنا المسلحة هذه الخطة الخبيثة للعدو في حرب الأربعين يومًا، وأجبرته على طلب وقف إطلاق النار والتفاوض، لكن هذا بالتأكيد لم يغير استراتيجيته الخاطئة. أمريكا بطبيعتها المتعجرفة، ولن تقبل أبدًا بإيران قوية.
بناءً على هذه الافتراضات، يجب علينا الإجابة على الأسئلة المذكورة أعلاه. لم نرحب بالحرب قط ولن نرحب بها، ولكن يجب أن نكون دائمًا على أهبة الاستعداد للمعركة وأن ندافع عنها حتى الموت حفاظًا على أمننا ومصالحنا الوطنية. إضافةً إلى ذلك، يجب علينا أيضًا استخدام أدوات الدبلوماسية والتفاوض لتحقيق المصالح الوطنية وتوطيدها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83203" target="_blank">📅 20:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83202">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGgQA-ETZWMvRcSnRjLBhxBUbw7tG9VMpP2_H0qP-SyglWXBMCc72HyHMx1yr36Q_IgRQTFyZ6mPZD-LBhwokLBrK7uMO722w6nxOdNTUt01IQyOBYoDCTMS5DxrqkGpYWC1OuOQWp9Kv-O4tr3G4K9BiRwoH3X7IhAA8duAh5GPhYa-C6SnZPQ3NLOAeyL2NKncEBn65jbQETXVG8g1OjeJvgcKXyj5eVkE-RV6k4EQLKn8jcsDH5BLGcF9qHCBchJeqmbYa1ItxN-8Q71Fa8m6geYzfY04D77VUINZZ7qCSRDe1M9b7fdo0skUVR05h7Gug8y55-2zAmjgIbHLQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
حاولت ناقلة الغاز البترولي المسال الإماراتية "مباراز" التابعة لشركة أدنوك الإماراتية أن تدخل ممر ترامب، لكنها توقفت  بعد توجيه انذار لها من قبل بحرية الحرس الثوري الايراني.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83202" target="_blank">📅 20:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83201">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tU_GIDDYQ8K_hC2TXT1CuZC8ifQqLb7EUkgbmtAn1MtHEnFEZ3b3anNj2Y5DQssX7hZi43fEYWLD0I8i6juVD8mpfY2T6YxiZo4ZHQQEVaeg3AwGhXoX0hVFnp_MqZbhK7gkfWZv84FS1ITV0pXJZtABuKrktijdw5iUSpAHpfskg5h78wDxAMTCnq1yr5osoACusKMtGtA7YAdHJ2qsCzVLOWYamw9C0jacMstTQbWouVwHSWsnu-7vIRAi9IpDI0bhlUPnLZnFo_-mABqP7JMbrLjbaz8Oj-EYttlS-xEU1Bmi89gMDjmzVlfJGxXoXJxSzvXz8pPf5tPqjzuWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تدمير واسقاط طائرة مسيرة في بندر عباس  من قبل دفاعات الجوية الايرانية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83201" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الرصد الزلزالي يسجل هزة أرضية بقوة 3.2 درجة شمال غرب البصرة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83200" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83199">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
أعلنَ مكتبُ سماحة السيد السيستاني (دام ظلّه) في النجف الأشرف أن يوم غدٍ الخميس (١٦-٧-٢٠٢٦م) هو الأول من شهر صفر لعام ١٤٤٨ للهجرة ،ونسألكم الدعاء .</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83199" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83198">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da1121f79.mp4?token=rPx9snxm57znkVU4tPRBcYwNPXBpig1rKCjs3LYEk2iQHYB9LDYfH7K-f2SnrT30uqs-8EVMecFBY04oJBBIeQGbjT4CbzzsBChqhNq7qV8pAMFmD2N6MdqBV55JK47tGmoq4DuWpv5yOCrIZc-yZJ0NZN0zrUGzwJXH7cutaz7rV_luCQee6_A5LfhhEmrR9gTw0xVoRqreXQHj0u2p-ikNo4x0VF94nUGsWR85M0xcfHyNXCxb3YFh705RcvaeyJ7b_6lE-Z5k7jC_H8SnMbhebkVJO5xXb3GJe8r1VNuRquKzd4GUNpdcSAUusSidrAS5FC7nHiyks0tJ0hktnIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da1121f79.mp4?token=rPx9snxm57znkVU4tPRBcYwNPXBpig1rKCjs3LYEk2iQHYB9LDYfH7K-f2SnrT30uqs-8EVMecFBY04oJBBIeQGbjT4CbzzsBChqhNq7qV8pAMFmD2N6MdqBV55JK47tGmoq4DuWpv5yOCrIZc-yZJ0NZN0zrUGzwJXH7cutaz7rV_luCQee6_A5LfhhEmrR9gTw0xVoRqreXQHj0u2p-ikNo4x0VF94nUGsWR85M0xcfHyNXCxb3YFh705RcvaeyJ7b_6lE-Z5k7jC_H8SnMbhebkVJO5xXb3GJe8r1VNuRquKzd4GUNpdcSAUusSidrAS5FC7nHiyks0tJ0hktnIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر أضراراً لحقت بحظيرة مروحيات في قاعدة الأمير حسن الجوية بالأردن نتيجة الضربات الإيرانية الأخيرة
😆
الاردن لا يابه صديناها</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83198" target="_blank">📅 20:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83197">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات عنيفة في كويا باربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83197" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83196">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83196" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83195">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">يالثارات الصيادين
بهباد / مسيرة الشهيد نجم عبدالله</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83195" target="_blank">📅 19:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83194">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83194" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/83194" target="_blank">📅 19:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83193">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات عنيفة تهز جزيرة بوبيبان الجانب الكويتي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83193" target="_blank">📅 19:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83192">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83192" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83191">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83191" target="_blank">📅 19:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83190">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مسيرات عدد اثنين تدك جارة السوء الكويت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83190" target="_blank">📅 19:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83189">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">يا أبا الفضل</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83189" target="_blank">📅 19:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83188">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83188" target="_blank">📅 19:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83187">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة هنغام الايرانية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83187" target="_blank">📅 18:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة هنغام الايرانية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83185" target="_blank">📅 18:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامب: أحمد الشرع يرغب في الدخول والتصدي لحزب الله. أنا أفكر في إعطائه الضوء الأخضر.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83184" target="_blank">📅 17:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تصريحات ترامب حول التحقيق في استهداف طلبة مدرسة "ميناب": اعتقد أنه لن يتمكن أحد أبدًا من معرفة ما حدث هناك.
من المحتمل أيضًا أن تكون تلك الصور التي لديكم قد تم إنشاؤها باستخدام الذكاء الاصطناعي.
لا أعتقد أنه يمكن تقديم تقرير نهائي وحاسم حول هذا الموضوع.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83183" target="_blank">📅 17:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad3e88f8a.mp4?token=vYvgwOwIGmG5oBzT9EdW2P0fSlY9l51cntsjUgrmb9MQ-ElQHx5OBWYFXrAY4OAfllczjsvaQnUxMMr_Fa0wurcpUgW1ZoKUox7LAwgqtKQ6PSQyuWEF2avj1qhxClw8desOUeXP3BKw3ZBThLzDsWZmiHyWLvZiv2tcZT5DQBvQqlKCrNCBvWA46f3GZAxOa8ElEKPhJgJHtpxyrH3_mySYA0tWASa9p09BhdSGcMlaVOhjpDo1E_knX-g9SZVTLu1ffNfbMO-NZxEssZ0dxhFGEHKC__2nwwmEQPhG8sn1hsfKHb-9yzcSkmPbYSv_cJWKIGI3tvDTDRP4CXT6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad3e88f8a.mp4?token=vYvgwOwIGmG5oBzT9EdW2P0fSlY9l51cntsjUgrmb9MQ-ElQHx5OBWYFXrAY4OAfllczjsvaQnUxMMr_Fa0wurcpUgW1ZoKUox7LAwgqtKQ6PSQyuWEF2avj1qhxClw8desOUeXP3BKw3ZBThLzDsWZmiHyWLvZiv2tcZT5DQBvQqlKCrNCBvWA46f3GZAxOa8ElEKPhJgJHtpxyrH3_mySYA0tWASa9p09BhdSGcMlaVOhjpDo1E_knX-g9SZVTLu1ffNfbMO-NZxEssZ0dxhFGEHKC__2nwwmEQPhG8sn1hsfKHb-9yzcSkmPbYSv_cJWKIGI3tvDTDRP4CXT6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇷🇺
🙃
تغريدة لترامب حول الحرب بين روسيا وأوكرانيا:
أقول لـ"بوتين" نفس الشيء طوال الوقت.
لا أريد الخوض في تفاصيل كبيرة، ولكن الأمر هو: "فلاديمير، لقد حان الوقت للتوقف. لقد حان الوقت لإنهاء هذه الحرب."
أعتقد أنه مستعد لإبرام صفقة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83182" target="_blank">📅 17:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
‏
ترامب مجددا:
إيران اتصلت بنا منذ فترة؛ إنهم يريدون إبرام صفقة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/83181" target="_blank">📅 17:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇦
🇮🇷
خبير وقود أوكراني :
قد يرتفع سعر البنزين والديزل في أوكرانيا بمقدار 10-12 غريفنا لكل لتر، وذلك بشكل خاص بسبب استئناف الحرب مع إيران وزيادة الطلب الموسمية،</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83180" target="_blank">📅 17:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
وزارة الحرب الأمريكية تزعم:
إنهاء مهمة التحالف الدولي في العراق نهاية أيلول المقبل.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83179" target="_blank">📅 16:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محافظة البصرة: هناك صيادون عراقيون محتجزون في الامارات والسعودية.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83178" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83177">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇷🇺
‏
روسيا:
نشر قوة متعددة الجنسيات في أوكرانيا بعد أي اتفاق سلام أمر غير مقبول، وسيُنظر إليه على أنه تدخل وتهديد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83177" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83176">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🔻
عراق و ایران در حال مذاکره برای اختصاص شماره کوتاه رایگان به زائران ایرانی هستند
@Naya_Press</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83176" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83175">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b34845b8.mp4?token=BvUE3k7RomgCNRakABJ7ddhJkVQxHu_FZZu_-of4adQBVDqha8NZuPIq7VcdMqt860RcCW5UtlwyNMPHUUwKnmoRFos--xGT55rxu6etUA9Z5Vt1iM1EKpbvalQSS-JwPhzGw2i3Nk8KctyUmt_Y5emEMCwIxAtp296pQi6CrFFtYLRcmLShF0OeSeuLYnQCz43lXl8WsNDES8NqXliPzoFgGJYNeUiUCc5JiU6Oj1Qt-BXT0pBXD9tw8zyNlzv-narSK7etDbaqIlqME7xjkVKwloC1-19JXTwgE6rOo5R0jK5V89uEZfXdH7mc21AoHl74qeBermJ4o31coYgmDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b34845b8.mp4?token=BvUE3k7RomgCNRakABJ7ddhJkVQxHu_FZZu_-of4adQBVDqha8NZuPIq7VcdMqt860RcCW5UtlwyNMPHUUwKnmoRFos--xGT55rxu6etUA9Z5Vt1iM1EKpbvalQSS-JwPhzGw2i3Nk8KctyUmt_Y5emEMCwIxAtp296pQi6CrFFtYLRcmLShF0OeSeuLYnQCz43lXl8WsNDES8NqXliPzoFgGJYNeUiUCc5JiU6Oj1Qt-BXT0pBXD9tw8zyNlzv-narSK7etDbaqIlqME7xjkVKwloC1-19JXTwgE6rOo5R0jK5V89uEZfXdH7mc21AoHl74qeBermJ4o31coYgmDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
مقاعد خارج الخدمة..
مسافر على متن الخطوط الجوية العراقية يرصد هذا المشهد خلال احدى الرحلات.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/83175" target="_blank">📅 16:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83174">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
🇮🇷
العراق وايران يناقشان تخصيص رقم مختصر مجاني لخدمة الزائرين الإيرانيين
عراق و ایران در حال مذاکره برای اختصاص یک شماره تلفن رایگان برای خدمت رسانی به زائران ایرانی هستند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/83174" target="_blank">📅 16:06 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
