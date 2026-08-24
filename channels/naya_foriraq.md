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
<img src="https://cdn4.telesco.pe/file/WfflyOeFoEC_r4fdCVtX2DedIAr38HVs14pb2eXzkGqmCIQTfHULbdgL-sjM3Xb4iBf-O88XBGHVY5Xooch7t0WvFChdHjY2EtX9g-ZmjuUl13PWjQ58QsfoKRQlebf2SRGLW1Gv753VCMim8c0WZeAAeI0H6JicDHzi0Igiz8Td2IHnSN5qSQHwit_mpuZeS4uM3W2jQ0F7ymA2pTsq_BR0CpK-xBv2ciApJpELkeuQ6SYRYDHEmR_KCb-p73doKt_XCAyQh_lfKavA5tPIYN0QFlxWnha8OjHeRJWwAVTXazLywH_KSD9pEFS2cU91X-xIcnk5dYd2uUQpMrKebQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 06:58:57</div>
<hr>

<div class="tg-post" id="msg-88406">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
دوي إنفجار عنيف داخل أحد مقرات مرتزقة السعودية في مدينة عدن اليمنية.</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/naya_foriraq/88406" target="_blank">📅 03:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88405">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">إطلاق نيران كثيفة صوب مصفاة لاناز في قضاء خبات بمحافظة أربيل.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/88405" target="_blank">📅 02:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88404">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq3-U5CBxcQ85Yf9WT6l8C2xu_bF01JV-ttnCPzMcj84N-VaK7zcvHBJdw55XzSGgEXoj1ujUD0RqrY1HJxzp7T26tmIO9DXGHSW4ByATf3gR5F4JV0I01Rl2RxQwrfNQB-0__2LSeW8gzwR-1dHSheCBfumamdULUCmQve6z86HEll5NCpNrsOR9WYtBEVuxEvgbqtTxcjb2ugLUR8kWI8qk9Y33b-613HcZrA4NRGYL6rQaFd-VBrRShsECzCfK1QXO-gLxdXiYMR9lSrdH47vBA62X_m9ScrXmTHvM8zGSZ8r6qnyej9byxHjZ4_V58oUm4NFLHbUPNZmeiVHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اربيل امن وامان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88404" target="_blank">📅 01:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88403">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aa2b6b21.mp4?token=Gr7ZOFAc4oDY7Hdr51dfBBul7StY-gQnaRx6NZTMy4d-vqQIhcbF0TkOdWkHQX64IkEoV4Z9-ieEN-tkgCiKCGy96fbKoiY8zThXSekz_lS49j7ZFA0hLwH4289Y5l9DuDLZMoHSOaz5nC4qmaGaO6dArhSXowzzgHuNTBDHt2rhPcrn_yX-NTg11QA5i92bGFgAeKRtyuNpxzLfygJAC9PQVmbiQA6ulECezgGAZJR_0MNlVlfPhRbi6gxF8juEPNpT24XIMMEauOmUr2RgdUG_-bncRfGuBB40NYyNjksJmlY8VipBdcnGvIIkIFvevASuVn409H_9JLuZgcqT9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aa2b6b21.mp4?token=Gr7ZOFAc4oDY7Hdr51dfBBul7StY-gQnaRx6NZTMy4d-vqQIhcbF0TkOdWkHQX64IkEoV4Z9-ieEN-tkgCiKCGy96fbKoiY8zThXSekz_lS49j7ZFA0hLwH4289Y5l9DuDLZMoHSOaz5nC4qmaGaO6dArhSXowzzgHuNTBDHt2rhPcrn_yX-NTg11QA5i92bGFgAeKRtyuNpxzLfygJAC9PQVmbiQA6ulECezgGAZJR_0MNlVlfPhRbi6gxF8juEPNpT24XIMMEauOmUr2RgdUG_-bncRfGuBB40NYyNjksJmlY8VipBdcnGvIIkIFvevASuVn409H_9JLuZgcqT9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العشرات من عشيرة الهركي يتوافدون الى منزل خورشيد الهركي لمواجهة قوات البيشمركة.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/88403" target="_blank">📅 01:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88402">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2921b037ec.mp4?token=Sj5OEeJLOWk3prj7pv9YbuhW_VUfeBKG5fpvOa8Dj1Tm6L8ZAUv2yrhVCXeVyeqKaMWCCbUIw2qLPwckWQhGeJw-iSVxACRYu1nI6wbuaOo69HMZavcUOBAlcT71In5T7_OcttqDSbx4NPqifmA0oyG7DKJITQBgDeo5-WJoyW7QQnbCq0zzHZssa5adNCzwTlO92GL6a_h9UiVnR-cEw7kXcl0JvWCZIjgcfJeuAchLiEXKMS3py5cHJYEsnqYaw6ms8KB80Y3QQi0kIqEXorND1_gxwChVv53AIhIBg0zCFPrkBvV1aWktHz-giR5YNCLdZ9TN-8I7Olugdo_aiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2921b037ec.mp4?token=Sj5OEeJLOWk3prj7pv9YbuhW_VUfeBKG5fpvOa8Dj1Tm6L8ZAUv2yrhVCXeVyeqKaMWCCbUIw2qLPwckWQhGeJw-iSVxACRYu1nI6wbuaOo69HMZavcUOBAlcT71In5T7_OcttqDSbx4NPqifmA0oyG7DKJITQBgDeo5-WJoyW7QQnbCq0zzHZssa5adNCzwTlO92GL6a_h9UiVnR-cEw7kXcl0JvWCZIjgcfJeuAchLiEXKMS3py5cHJYEsnqYaw6ms8KB80Y3QQi0kIqEXorND1_gxwChVv53AIhIBg0zCFPrkBvV1aWktHz-giR5YNCLdZ9TN-8I7Olugdo_aiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وسائل إعلام كردية: خورشيد هركي أبلغ أبناء عشيرته ببدء المعركة ضد البيشمركة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/88402" target="_blank">📅 01:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88400">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ca1f3d6d.mp4?token=fTpJM7GbIDUXjuRggfKwZintVc56je6Dv25vtLHEb-LKVPDatsnIC4mEJ_3vItclQMqRQy9GLPd8JeeDQNEm4N-FgfpgPV3s-gRfxmE9Z1B6buAuhvrIV0B4u8AmqM5ipM41gq-7OHJ2cQ3dUhGVdNzh3K3PUr3vKhnowrJg-Uvq6_hcFpTS2hsbLc1HJ4sV9A_Pg0zqkmb_WXixWp8qCaIJryScgSvz1eSURCsLV2u9R_Kvv5YMqfyEs4DWJ_9diFSR73RN1BJV7zMhnUpgQ1cVdJqjkP9xnnTgcLeQbxch-ZY18PIw0qb2_3gH6mvh53lR0PONO6WChF1Uy9m7JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ca1f3d6d.mp4?token=fTpJM7GbIDUXjuRggfKwZintVc56je6Dv25vtLHEb-LKVPDatsnIC4mEJ_3vItclQMqRQy9GLPd8JeeDQNEm4N-FgfpgPV3s-gRfxmE9Z1B6buAuhvrIV0B4u8AmqM5ipM41gq-7OHJ2cQ3dUhGVdNzh3K3PUr3vKhnowrJg-Uvq6_hcFpTS2hsbLc1HJ4sV9A_Pg0zqkmb_WXixWp8qCaIJryScgSvz1eSURCsLV2u9R_Kvv5YMqfyEs4DWJ_9diFSR73RN1BJV7zMhnUpgQ1cVdJqjkP9xnnTgcLeQbxch-ZY18PIw0qb2_3gH6mvh53lR0PONO6WChF1Uy9m7JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبادل إطلاق النار بين عشيرة الهركي ومليشيات البيشمركة في محيط مصفاة خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/88400" target="_blank">📅 01:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8833d650.mp4?token=WTBjgpbNQ86ALLsVW2f5RqVm2-d7wAQ4DUJ9nNaYpQfpidtRWXE6CSNt0FpDY9TQdwe2UM6bvLm1olOAdZSDVafYDvpqRG9M-aZdVfDJWNJv_Cid4-Hn65_6dYhPCi4DNM5OUJeObVasWbzmK1vp5_XRkFJq2AHNaInsDd-R5kybpc-9RFZ6WgWxlNoXyQdN3GDXofa1CsCexb2At_2eqQVOc2FMSAavSU_8bwhgupEZ0if-pK6i6aXT7olNSxC9mXht-sj38euTb5wd7nkerAj1QoQIVmifIQN3_ApcTONl4eRhOSpbIAZQLb3paPy4JJmLwCJzhn4scMihghDlEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8833d650.mp4?token=WTBjgpbNQ86ALLsVW2f5RqVm2-d7wAQ4DUJ9nNaYpQfpidtRWXE6CSNt0FpDY9TQdwe2UM6bvLm1olOAdZSDVafYDvpqRG9M-aZdVfDJWNJv_Cid4-Hn65_6dYhPCi4DNM5OUJeObVasWbzmK1vp5_XRkFJq2AHNaInsDd-R5kybpc-9RFZ6WgWxlNoXyQdN3GDXofa1CsCexb2At_2eqQVOc2FMSAavSU_8bwhgupEZ0if-pK6i6aXT7olNSxC9mXht-sj38euTb5wd7nkerAj1QoQIVmifIQN3_ApcTONl4eRhOSpbIAZQLb3paPy4JJmLwCJzhn4scMihghDlEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلبية لدعوة خورشيد هركي.. مسلحين تابعين لعشيرة الهركي ينتشرون في محيط مصفاة خبات بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/88399" target="_blank">📅 01:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4890b6251a.mp4?token=HNOegkx_PNJhKmwvdCZWs4ED7fsjn5sXKCmptoDux7vRCzJwKMYHE-RjJwW5PsmBDh64fmFT9DyIc_AZBadt42AmnuGj4E0y6zzf4_PM4hTC3pprbExSh9FDPoFvxT3SP0soA9neJx0G7Z0hfai-83l_KitDCHK1IhVPqKTeXZ_4yxK1oN05FIqYEa4GBOFcGAaW5LtrznPSKAWZZLWs2CL2HkfigIGHi5o5OWUWxCnzDuoO0DwqRsR0jN4W7eXTFafDW2P6mLp4C6doQpqIwwvpLJvMkxlXGckc4F9olNZVGnc_C9urslwaiUH6vg9r-GbuTfTZBvzON4VYm6vpdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4890b6251a.mp4?token=HNOegkx_PNJhKmwvdCZWs4ED7fsjn5sXKCmptoDux7vRCzJwKMYHE-RjJwW5PsmBDh64fmFT9DyIc_AZBadt42AmnuGj4E0y6zzf4_PM4hTC3pprbExSh9FDPoFvxT3SP0soA9neJx0G7Z0hfai-83l_KitDCHK1IhVPqKTeXZ_4yxK1oN05FIqYEa4GBOFcGAaW5LtrznPSKAWZZLWs2CL2HkfigIGHi5o5OWUWxCnzDuoO0DwqRsR0jN4W7eXTFafDW2P6mLp4C6doQpqIwwvpLJvMkxlXGckc4F9olNZVGnc_C9urslwaiUH6vg9r-GbuTfTZBvzON4VYm6vpdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وسائل إعلام كردية: خورشيد هركي أبلغ أبناء عشيرته ببدء المعركة ضد البيشمركة.</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/88398" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
وزير الخزانة الأمريكي:
أي عمل عسكري ضد قواتنا أو ضد دول الخليج سيرد عليه الرئيس ترمب بسرعة وحزم.</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/88397" target="_blank">📅 01:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ارتال إضافية للبيشمركة تتحرك تجاه قضاء خبات بمحافظة أربيل</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/naya_foriraq/88396" target="_blank">📅 01:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88395">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962b98f198.mp4?token=KDDowD2fweewadtRy6gw5FLt3FjMXqC0uDhsOyGUIUWC8AVydkYEfamKy613nzRSshx-WUDi7p2Ovkh11o6I00Rx7XNHEuThWDUSuEQQBD1AfJO3Eiafs86JDTWYaCKO3RWoJ8-frqsOYNHOgd_Riu407IrtD5H_ChfopLMcmFuPAfjq76uM89hUiD6PWMLtQaiMKtdpnwA0B1Mm3ZGC_PmfvaJFhkxZL_3j-QjDW3o5G5fTfGuIPrBupiW6cikN1_cbCqu79YewyBUlKpC7KOA517G2b02BGTppA5W5IlAJ-MagQGN5uP7r_iZXLAoRE1le7MGh9RJ4VIHt-jAHKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962b98f198.mp4?token=KDDowD2fweewadtRy6gw5FLt3FjMXqC0uDhsOyGUIUWC8AVydkYEfamKy613nzRSshx-WUDi7p2Ovkh11o6I00Rx7XNHEuThWDUSuEQQBD1AfJO3Eiafs86JDTWYaCKO3RWoJ8-frqsOYNHOgd_Riu407IrtD5H_ChfopLMcmFuPAfjq76uM89hUiD6PWMLtQaiMKtdpnwA0B1Mm3ZGC_PmfvaJFhkxZL_3j-QjDW3o5G5fTfGuIPrBupiW6cikN1_cbCqu79YewyBUlKpC7KOA517G2b02BGTppA5W5IlAJ-MagQGN5uP7r_iZXLAoRE1le7MGh9RJ4VIHt-jAHKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعزيزات عسكرية كبيرة للبيشمركة تتوجه نحو قضاء خبات بمحافظة أربيل لمواجهة عشيرة الهركي.</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/88395" target="_blank">📅 01:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a0d3bee.mp4?token=vYb5HAZdxjnKIS_ycB9SbHpGIMAj3guqJV0zjIYFm-ZknJ6j-KGiNHRUoGYNV198v85qGIaqKUoe26k0zEfE9VWMGlbmXWXtQc9qqkp50B05S10ljCNpIdY7BtHDXN_TOxdcdqNaTw3HljrgV3lf2nm_2wWWibsAPFeneCsHXfiCbksgzUWHc_EhyznQBbJYvmWb2GqIrljaU76Gb0hFgPh9FPlmG4wMoF79kUuj6BngtI8SzvnvyWWDyWN2AQ8BlGG7JKFkPVS2NOmdOHt512GRWLP93zxCSlND63EkdGSIg1TK2BS0CsR6zStcrAqFz8eJOJZj4DSD4mYSrTCw7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a0d3bee.mp4?token=vYb5HAZdxjnKIS_ycB9SbHpGIMAj3guqJV0zjIYFm-ZknJ6j-KGiNHRUoGYNV198v85qGIaqKUoe26k0zEfE9VWMGlbmXWXtQc9qqkp50B05S10ljCNpIdY7BtHDXN_TOxdcdqNaTw3HljrgV3lf2nm_2wWWibsAPFeneCsHXfiCbksgzUWHc_EhyznQBbJYvmWb2GqIrljaU76Gb0hFgPh9FPlmG4wMoF79kUuj6BngtI8SzvnvyWWDyWN2AQ8BlGG7JKFkPVS2NOmdOHt512GRWLP93zxCSlND63EkdGSIg1TK2BS0CsR6zStcrAqFz8eJOJZj4DSD4mYSrTCw7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة وتعزيزات عسكرية من كلا الطرفين تتجه صوب قضاء خبات.  البيشمركة حاليا: السيطرة تحت الوضع
😆</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/88394" target="_blank">📅 01:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d19f9e5.mp4?token=dYzjNoWbi31zgWVjU5-kEp_3YGk-Lh5bcawnGg2OO6yxFOdd3vYhR_OofQgjAiN4aaa63VDh_37UCTaZPOFZRaBgQhLRpV3y4H6LzP-t8yaV8M0HfJ9W2NdptoTzxwNM8YYuXUDQYBWXSZqDl4RSJNgm9BIVZg9hOgDw0Y3_-wSnu2XBp9cYm0mHgC__qAXnXKF-anRzwv916f-W0Bo95kuRsTWR9uhzDpbgCD6yNiwz0vHY5KLyHzG085FrM8m-fk-2MFpzWUX_LiC2wXaz2_6PFC_lB-Ejq9d4yGU1YVOu8G2UTQXEeEPg-syO8QkqgNMfvv94za9I28D_wFSzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d19f9e5.mp4?token=dYzjNoWbi31zgWVjU5-kEp_3YGk-Lh5bcawnGg2OO6yxFOdd3vYhR_OofQgjAiN4aaa63VDh_37UCTaZPOFZRaBgQhLRpV3y4H6LzP-t8yaV8M0HfJ9W2NdptoTzxwNM8YYuXUDQYBWXSZqDl4RSJNgm9BIVZg9hOgDw0Y3_-wSnu2XBp9cYm0mHgC__qAXnXKF-anRzwv916f-W0Bo95kuRsTWR9uhzDpbgCD6yNiwz0vHY5KLyHzG085FrM8m-fk-2MFpzWUX_LiC2wXaz2_6PFC_lB-Ejq9d4yGU1YVOu8G2UTQXEeEPg-syO8QkqgNMfvv94za9I28D_wFSzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج مسلح كثيف لقبيلة الهركية مع غلق معظم الطرقات المركزية في محافظة اربيل.</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/naya_foriraq/88393" target="_blank">📅 01:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f58106d3.mp4?token=PQhh1v61J5nMNb9niuwfdE9LBQgQHGi8ffYJDkvzMzx7Gm0AHPFbbMuKgFXYQX6DXERqfK8IKdccRqCOXlaTYIr6sFRlNHgi8qbWEOIWJtOncMMhmD0w4dX9hSUHcoDL3vibZWMn83rxag7iowPylCQ29zepcIjoSoUAmty9tFIalXu-3dZ0ECqYljMNsxWZ45zkY31jsCDecO5mSoUcZEt43CuC3OjiVLDk8vIOCIPCSaV4tzWSlzqCUi5yPvyD6RJrgFgMMXBQJPIT8dGokCj9hI2Cz1XFPy22E0Da7Hhl7AOWJ_YDC2tQYFoLxU17061VIC-VSUQkuCwE1AI7pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f58106d3.mp4?token=PQhh1v61J5nMNb9niuwfdE9LBQgQHGi8ffYJDkvzMzx7Gm0AHPFbbMuKgFXYQX6DXERqfK8IKdccRqCOXlaTYIr6sFRlNHgi8qbWEOIWJtOncMMhmD0w4dX9hSUHcoDL3vibZWMn83rxag7iowPylCQ29zepcIjoSoUAmty9tFIalXu-3dZ0ECqYljMNsxWZ45zkY31jsCDecO5mSoUcZEt43CuC3OjiVLDk8vIOCIPCSaV4tzWSlzqCUi5yPvyD6RJrgFgMMXBQJPIT8dGokCj9hI2Cz1XFPy22E0Da7Hhl7AOWJ_YDC2tQYFoLxU17061VIC-VSUQkuCwE1AI7pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عبر نايا   مراقبون أمنيون يتسألون عن دور مدير مكتب القائد العام للقوات المسلحة العراقية الفريق الركن الأول عبد الأمير الشمري والمشروع المكلف به   بنزع السلاح و ان كان يشمل هذا الأمر ايضا اقليم كردستان العراق وسط حالة سقوط المدينة وخروجها عن السيطرة الامنية…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/88392" target="_blank">📅 01:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
عبر نايا
مراقبون أمنيون يتسألون عن دور مدير مكتب القائد العام للقوات المسلحة العراقية الفريق الركن الأول عبد الأمير الشمري والمشروع المكلف به
بنزع السلاح و ان كان يشمل هذا الأمر ايضا اقليم كردستان العراق وسط حالة سقوط المدينة وخروجها عن السيطرة الامنية . ام ان الأمر منوط فقط بسلاح وسط وجنوب العراق .
نعم لحصر السلاح المنفلت</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/88391" target="_blank">📅 01:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bdb6ffa4.mp4?token=CoCZxquhZDrsBpiR5glX-5TZ4sbQfVNS-D__O2rFNccTk72IhkvKazPwXx3NEH9GAV8ZyipYf40MA3PHNa6K20QHgDDGN3XXjnB7KrmcE092jtxTpkvEwNsclfzaxgcnUNs-Ze5vhnPE0JCah5NLC_1s_UVzuaYb0xFPHuu1hCrLt48PxV0POLWqYXd4I0xzFkT_o3HjwKkqviRKhaq_xBPYTYcOn8gCfIR5qyxPyJE54Um8wkK42G1r4UK12XJpmN3L0B4C1qHMiN82rEazbDjwztq_x3pPPXcwP6BzFE_tsl1mRi5mPwLShgL2Bjmwc75clhHvtVx_2ai4VPCK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bdb6ffa4.mp4?token=CoCZxquhZDrsBpiR5glX-5TZ4sbQfVNS-D__O2rFNccTk72IhkvKazPwXx3NEH9GAV8ZyipYf40MA3PHNa6K20QHgDDGN3XXjnB7KrmcE092jtxTpkvEwNsclfzaxgcnUNs-Ze5vhnPE0JCah5NLC_1s_UVzuaYb0xFPHuu1hCrLt48PxV0POLWqYXd4I0xzFkT_o3HjwKkqviRKhaq_xBPYTYcOn8gCfIR5qyxPyJE54Um8wkK42G1r4UK12XJpmN3L0B4C1qHMiN82rEazbDjwztq_x3pPPXcwP6BzFE_tsl1mRi5mPwLShgL2Bjmwc75clhHvtVx_2ai4VPCK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تستمر تحشيدات الهركية في قضاء خبات استعدادا لمواجهات اكبر مع البيشمركة.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/88390" target="_blank">📅 01:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20747c723a.mp4?token=k02v1vOVLexGSpV8jPE3pJqgdigPQYtFUL2M5Lgz-bQ8DMi82WO4EenSKiiG20lQ9LUN9Wf65kzEfzjX-t3mwue1k-rSwwhVSjh6G8pxTy12Pix75rtDuHAieeHVBI9I5kLQcw716dV3kncNFlnsgYxirCbL-7ff_IHmfvM6xdflm_Y4GG0uRtCbW-yAHg6TH-eypz8qmEUGtgL8kbNTpck50a2I8QICOdwFUpOY_QNzJJhvVraLwwFhfJkQgZ68W_tfOmatc0sGEDd58h6ri1m8u0moCCacZL4jfwKbk-mHz3nxLLNZcb2HnUvDYmcDP-C8JM9LKmbI5As-lPcFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20747c723a.mp4?token=k02v1vOVLexGSpV8jPE3pJqgdigPQYtFUL2M5Lgz-bQ8DMi82WO4EenSKiiG20lQ9LUN9Wf65kzEfzjX-t3mwue1k-rSwwhVSjh6G8pxTy12Pix75rtDuHAieeHVBI9I5kLQcw716dV3kncNFlnsgYxirCbL-7ff_IHmfvM6xdflm_Y4GG0uRtCbW-yAHg6TH-eypz8qmEUGtgL8kbNTpck50a2I8QICOdwFUpOY_QNzJJhvVraLwwFhfJkQgZ68W_tfOmatc0sGEDd58h6ri1m8u0moCCacZL4jfwKbk-mHz3nxLLNZcb2HnUvDYmcDP-C8JM9LKmbI5As-lPcFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لمن يتساءل عن أسباب الانفلات الحاصل حالياً في محافظة أربيل... تعود خلفياته إلى خلافات بين زعيم قبيلة الهركية في قضاء خبات والحزب الديمقراطي الكردستاني.  وكان زعيم القبيلة قد انضم إلى حزب بارزاني، إلا أن خلافات نشبت بين الطرفين لاحقاً ما دفعه إلى الانسحاب…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/88389" target="_blank">📅 00:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفلات امني في محافظة اربيل شمالي العراق بسبب اعتقال خورشيد هركي وعدم الافراج عنه.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/88388" target="_blank">📅 00:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88387">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d4806f03.mp4?token=FCJRw03F6rc0ZS75wngjBsERcJ3yYumWGmvlYnPlt4Ueuw_NdLqa0O35LWaKaJ_Gf3z235i3-ibFuX512-vJYeWqDL80yxbXIDAC0TjVvLk_qggZMAgDWrGE_xBz5ozHJ37ljSfBSVqm7LFMlfIruoQLSWRVmrIhcxwge4aJNOwg9tGXSSWE2H4kreL9g9zRENVvmO-L26aMhSciHcSkiFcjdZDatElLZkKySZ3Xp4cL0xB1s0STCuqmBX8wN4JllRC-TxBieWy0dz04Kx0gd0epChJ29Q8FOESiXFPHW8pff-Zaasfd9hFMzf4mh2k-e6QVWc6JEI-UP6EK9rtCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d4806f03.mp4?token=FCJRw03F6rc0ZS75wngjBsERcJ3yYumWGmvlYnPlt4Ueuw_NdLqa0O35LWaKaJ_Gf3z235i3-ibFuX512-vJYeWqDL80yxbXIDAC0TjVvLk_qggZMAgDWrGE_xBz5ozHJ37ljSfBSVqm7LFMlfIruoQLSWRVmrIhcxwge4aJNOwg9tGXSSWE2H4kreL9g9zRENVvmO-L26aMhSciHcSkiFcjdZDatElLZkKySZ3Xp4cL0xB1s0STCuqmBX8wN4JllRC-TxBieWy0dz04Kx0gd0epChJ29Q8FOESiXFPHW8pff-Zaasfd9hFMzf4mh2k-e6QVWc6JEI-UP6EK9rtCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بمختلف انواع الاسلحة المتوسطة والخفيفة تبدأ مواجهات بين الهركية والبيشمركة بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/naya_foriraq/88387" target="_blank">📅 00:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88386">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3162c91ec2.mp4?token=pSF44hxN1-jKzM0BKKbVpoR0igsELhoCWATznY1sYgJIK-QvTCgkM6GGKbe4hjt983zLdiID_st1K7LBnnOO-J8b58egIzHKix4AQ63g9OSkP3qbZcTTMlSufd358HwRgblcjLSWs81VmnpMEJAAN9XeBU-K_UCKhI2pTdd4IBGhkYtuGIa8mi6DNNQzB9o8H5QfBUvjywq6cikSBqMmM2R2HI6-eIgt1YzvNdl6Om11m7U4MMTxQdKyNc2b_se16CG0HuwiFd3B8QxP1wBguXdx7PT3--GB6s_tdoCPXqlL-kbAQEz5vJcAMjNoFdj4bclk6iVUcD55f2XfW3ttMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3162c91ec2.mp4?token=pSF44hxN1-jKzM0BKKbVpoR0igsELhoCWATznY1sYgJIK-QvTCgkM6GGKbe4hjt983zLdiID_st1K7LBnnOO-J8b58egIzHKix4AQ63g9OSkP3qbZcTTMlSufd358HwRgblcjLSWs81VmnpMEJAAN9XeBU-K_UCKhI2pTdd4IBGhkYtuGIa8mi6DNNQzB9o8H5QfBUvjywq6cikSBqMmM2R2HI6-eIgt1YzvNdl6Om11m7U4MMTxQdKyNc2b_se16CG0HuwiFd3B8QxP1wBguXdx7PT3--GB6s_tdoCPXqlL-kbAQEz5vJcAMjNoFdj4bclk6iVUcD55f2XfW3ttMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
البيشمركة ترسل تعزيزات عسكرية ضخمه لصد الجماعات المسلحة التابعة لخورشيد هركي.</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/88386" target="_blank">📅 00:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88385">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ef949d38.mp4?token=kShZA5Xa3thXoPjV5BXCYhxm15gT_A85rZfu1O_hZUX3Ixfq_L2PPFUNM8fBXroMAwmWQPQKrjtBlADLrjGJ1eZjAGrDQWSquNEDTDwDMvD4LLqqDzd2qHUN1DjL_S7_8em4-CBNtCkbhZhAKbceuK5kicxBK7Dwr_D7eM_VCKdmCcfbTeEjCR87fnJmC33RNGh-unGuYVij3qZ3wb769AKKbTXY111nKQs-QaqyVkwSzyI-4nidUFVrYCiJM9xdUA_8Y7W955S7U_HLLyxmkB8_753qVfWqhRP0avk5LwLzqexTECgxo1oSINGaHCEsI-tsvR-9ihmLkbyVw5_FuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ef949d38.mp4?token=kShZA5Xa3thXoPjV5BXCYhxm15gT_A85rZfu1O_hZUX3Ixfq_L2PPFUNM8fBXroMAwmWQPQKrjtBlADLrjGJ1eZjAGrDQWSquNEDTDwDMvD4LLqqDzd2qHUN1DjL_S7_8em4-CBNtCkbhZhAKbceuK5kicxBK7Dwr_D7eM_VCKdmCcfbTeEjCR87fnJmC33RNGh-unGuYVij3qZ3wb769AKKbTXY111nKQs-QaqyVkwSzyI-4nidUFVrYCiJM9xdUA_8Y7W955S7U_HLLyxmkB8_753qVfWqhRP0avk5LwLzqexTECgxo1oSINGaHCEsI-tsvR-9ihmLkbyVw5_FuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة تدور بين الهركية والبيشمركة</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/88385" target="_blank">📅 00:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88384">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
تحشيدات عسكرية ضخمه تابعة للبيشمركة تتجه لقضاء خبات لمواجهة الهركية.</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/88384" target="_blank">📅 00:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba261dcac7.mp4?token=CG6QwsVhh6ppjfCmZTRujMHltwSryakdvJE46YXFXPiCtPWHwHdcLOyxYeIqWFnslzO_ZdmbpNZmHPwnGpqH1nwzw3HuMYFdSvOfFeB0xhQFwMC0qEaQShLmMHZ_RxXMY7px6f7xhxXTuI-DPBtfrLoYx5sJw5NVEpxJ1g5lwEDqApPYZgrGXAomGNxFmu_FbLndb3lQvZIGkzzpVNQ-WLcdKSwuaPnOzfPLqu6e3dhbt_jWwi93lYEiIgqumm5vbJuyRZQ4P_tEFRTYfGb_HojzfYUgbR_iGtXdO-wvFfN-Yl_mhQDVDeKIeBfjKavmC5p6ZZ0smxhqzHTY_-cSzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba261dcac7.mp4?token=CG6QwsVhh6ppjfCmZTRujMHltwSryakdvJE46YXFXPiCtPWHwHdcLOyxYeIqWFnslzO_ZdmbpNZmHPwnGpqH1nwzw3HuMYFdSvOfFeB0xhQFwMC0qEaQShLmMHZ_RxXMY7px6f7xhxXTuI-DPBtfrLoYx5sJw5NVEpxJ1g5lwEDqApPYZgrGXAomGNxFmu_FbLndb3lQvZIGkzzpVNQ-WLcdKSwuaPnOzfPLqu6e3dhbt_jWwi93lYEiIgqumm5vbJuyRZQ4P_tEFRTYfGb_HojzfYUgbR_iGtXdO-wvFfN-Yl_mhQDVDeKIeBfjKavmC5p6ZZ0smxhqzHTY_-cSzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
البيشمركة ترسل تعزيزات عسكرية ضخمه لصد الجماعات المسلحة التابعة لخورشيد هركي.</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/88383" target="_blank">📅 00:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083ed6f065.mp4?token=XR6uxvFRT58WsQ0mko-q0pRtKMuHXin8xqk9xXIi_wn8lP5A4Mb2LmXdMbuvWiFZkTL62NBzVukzXPJFlsrOFgoTzSnZRQL-lxqRIRmOkEvK-lO4afDFyIGc1_Pu35mwCLEgQvC3MC9-MgyIPXXSQKsTlvxM_PxIzN2CmwN1YltCilmejtfVmFT7YsrE4UkqDeU8j3MIlMzTp-zHoCS7WwGMm-lvc5SzwfDt9PEzTVW1wy-IjMFxx6NGfmNKar4U730GnxgijjdWu64AXTY3gUgfwBuBqsLTfNaAo5td-6-tPslL8Jgh2uMW6tRseQabM8JoQpxoJtxNgVtUntNNbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083ed6f065.mp4?token=XR6uxvFRT58WsQ0mko-q0pRtKMuHXin8xqk9xXIi_wn8lP5A4Mb2LmXdMbuvWiFZkTL62NBzVukzXPJFlsrOFgoTzSnZRQL-lxqRIRmOkEvK-lO4afDFyIGc1_Pu35mwCLEgQvC3MC9-MgyIPXXSQKsTlvxM_PxIzN2CmwN1YltCilmejtfVmFT7YsrE4UkqDeU8j3MIlMzTp-zHoCS7WwGMm-lvc5SzwfDt9PEzTVW1wy-IjMFxx6NGfmNKar4U730GnxgijjdWu64AXTY3gUgfwBuBqsLTfNaAo5td-6-tPslL8Jgh2uMW6tRseQabM8JoQpxoJtxNgVtUntNNbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/88382" target="_blank">📅 00:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88381">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/88381" target="_blank">📅 00:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88380">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a009d53.mp4?token=JNSJzqljHlEWuV12FHpnhrBvcfdx4Ecb8vURovdbUlgY61hZu0URTnS9uM1CUJRZ0bUTmG2neevK3PvZx6g8d9vy3MyKjv6qy4409D3i1bdXE4WgCiFAAIPxdh0CstOaEEEtpGeoBmk4LnaKT2wvmi2LqxFyQZRR0FpRZecRP5_uIBozAEDMbbOnjV4-1T-Z5wl3ZQlYy14Q_29dgGzFYUShsIb9G7hh0diz9eHYGfaiPxj72KYyAefywLvq_KR5gNc3Myr7sq52EcFpffwfSVRNhrI1VgAGy0o7BKO5xS3cM1WXrWjntnnfkyalFPpNUKir6yhB4v5DIbZpywJVvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a009d53.mp4?token=JNSJzqljHlEWuV12FHpnhrBvcfdx4Ecb8vURovdbUlgY61hZu0URTnS9uM1CUJRZ0bUTmG2neevK3PvZx6g8d9vy3MyKjv6qy4409D3i1bdXE4WgCiFAAIPxdh0CstOaEEEtpGeoBmk4LnaKT2wvmi2LqxFyQZRR0FpRZecRP5_uIBozAEDMbbOnjV4-1T-Z5wl3ZQlYy14Q_29dgGzFYUShsIb9G7hh0diz9eHYGfaiPxj72KYyAefywLvq_KR5gNc3Myr7sq52EcFpffwfSVRNhrI1VgAGy0o7BKO5xS3cM1WXrWjntnnfkyalFPpNUKir6yhB4v5DIbZpywJVvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماعات المسلحة تحتشد لمواجهات اكثر عنفا مع البيشمركة بعد انتهاء مهلة اطلاق سراح زعيمهم خورشيد هركي.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/88380" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88377">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e7020797.mp4?token=NvphfJbYOoQ5f3XzuU8mvh7bid9aPVs25RzlrC9wooCrkRbDjuv6h2ffI8Jr02QrCsGRtdgcSqqcKyIHyEXPWx3s45ZGvQ8lj6wzndRz5jKkdGl6KpJAT4d1vv8kjSfpq4rSI3gcaXd997Z3_0Gn2Q-EynHAXyPPVyng_4Oln9KWdz51IbSN7acrq6THL4PhvsTVMBGba38gm54DLFolxP1Vvrww2eQsdniThkmVCZCQwInGjsepWIeRemFGh5zjA-CZR4EZ1PzQ2cDKzMflIWqwPPaRTqIfEg1_5yeUe4z7ndavRd2HEaSRtOYV9BXAmgVlsG3FLtE_A-LvKp7NpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e7020797.mp4?token=NvphfJbYOoQ5f3XzuU8mvh7bid9aPVs25RzlrC9wooCrkRbDjuv6h2ffI8Jr02QrCsGRtdgcSqqcKyIHyEXPWx3s45ZGvQ8lj6wzndRz5jKkdGl6KpJAT4d1vv8kjSfpq4rSI3gcaXd997Z3_0Gn2Q-EynHAXyPPVyng_4Oln9KWdz51IbSN7acrq6THL4PhvsTVMBGba38gm54DLFolxP1Vvrww2eQsdniThkmVCZCQwInGjsepWIeRemFGh5zjA-CZR4EZ1PzQ2cDKzMflIWqwPPaRTqIfEg1_5yeUe4z7ndavRd2HEaSRtOYV9BXAmgVlsG3FLtE_A-LvKp7NpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق نار كثيف في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/88377" target="_blank">📅 00:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88376">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇹🇷
🇮🇱
🇸🇾
اجتماع وزير الخارجية السوري مع مدير "الموساد" الإسرائيلي لخص إلى تشكيل لجنة أمنية سورية تركية إسرائيلية لمعالجة المشاكل وتفادي أي صدام.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/88376" target="_blank">📅 00:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88375">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇦🇪
الإعلام الأوروبي:
حذّر مسؤولون إماراتيون من أن "نتيجة سلبية" بشأن التحقيق الجاري مع نادي مانشستر سيتي لكرة القدم المملوك(منصور ال نهيان) بتهمة انتهاك القواعد المالية للدوري الإنجليزي الممتاز "قد تضر بالعلاقات المحسّنة مع المملكة المتحدة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88375" target="_blank">📅 23:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88374">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e86b62545.mp4?token=L3SbcAfzl5Gc2NLJiAa2Zi-9tz5vs7SNQ6wcpTlrEJGtOKOkq1rMz9Gkky_uMB7OM_egToCBquqbr0-BMyUeUH1yg7uZBXaX_2XA_ooVvGT64E63Okjk49BoOJZDEqvFOWlPUUpmviydJWlOHU9rhe11LhGV0XhHvwrqgqKjsFBdpPO0jln7UzyoISvRfI94S3sMK-_JrKGhn8z6eM25PwiYcwy5VhDsXJoj_WtZYvRU0pf0QQFAkpJW_svFO3_tGsTeCCI6uMQ3tJFzNfXPO3MIfjmM4pOgOZerN5pZBKoKa0gfWj6G0MODM0Wio-vxZofe9tckJ5Tmw0m5WYxjCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e86b62545.mp4?token=L3SbcAfzl5Gc2NLJiAa2Zi-9tz5vs7SNQ6wcpTlrEJGtOKOkq1rMz9Gkky_uMB7OM_egToCBquqbr0-BMyUeUH1yg7uZBXaX_2XA_ooVvGT64E63Okjk49BoOJZDEqvFOWlPUUpmviydJWlOHU9rhe11LhGV0XhHvwrqgqKjsFBdpPO0jln7UzyoISvRfI94S3sMK-_JrKGhn8z6eM25PwiYcwy5VhDsXJoj_WtZYvRU0pf0QQFAkpJW_svFO3_tGsTeCCI6uMQ3tJFzNfXPO3MIfjmM4pOgOZerN5pZBKoKa0gfWj6G0MODM0Wio-vxZofe9tckJ5Tmw0m5WYxjCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تسريب غاز سام في حقل خباز النفطي بئر رقم 46 في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88374" target="_blank">📅 23:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88373">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
تسريب غاز سام في حقل خباز النفطي بئر رقم 46 في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88373" target="_blank">📅 23:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88371">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
المستشار الأمني لرئيس مجلس الوزراء العراقي:
الفصائل ليسوا أعداء للدولة بل هم جزء منها،رئيس الوزراء لن يرشح لولاية ثانية وهو رجل المرحلة الحالية، قدمنا مقترحا إلى ايران والسعودية لإنشاء مجلس تنسيقي أمني موحد، ظروف المنطقة وراء عدم موافقة بعض الفصائل على تسليم السلاح حتى الآن، سلاح الفصائل سيكون قوة للدولة ولن يُسلم إلى أي طرف خارجي.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88371" target="_blank">📅 22:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88370">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
هيئة الممرات المائية في خليج فارس:
بسبب انتهاك بعض السفن للوائح الإيرانية المتعلقة بالعبور عبر مضيق هرمز، ستواجه هذه السفن قيودًا مثل الغرامات أو الاحتجاز أو المصادرة في عمليات العبور المستقبلية  .</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88370" target="_blank">📅 21:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88369">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇹🇷
🇮🇱
🇸🇾
اجتماع وزير الخارجية السوري مع مدير "الموساد" الإسرائيلي لخص إلى تشكيل لجنة أمنية سورية تركية إسرائيلية لمعالجة المشاكل وتفادي أي صدام.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88369" target="_blank">📅 21:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88368">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
طلب من سكان المنطقة المحيطة بقطاع غزة الدخول إلى مكان محمي بسبب الاشتباه بوقوع حادث أمني.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88368" target="_blank">📅 20:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id0Qozkqt6QraaeIzPHVFLaHkYCMH_iBHBubazVdcqR8sWb9arepNwORwIalGKCuSTo2kXcrbFwcjUZrIMmZZH2P-7Bd3uK-9EP7S3vBtDdKetqiDa3s7jGVaRca2t_GtAYVJgbJ8qkZU5Qe_jTXni8p8lUXyKGT5fyu07SFGuIj-Fb_4IKnU-jHzS95GVTBaQdE2S5ZxxuhDLCjqwAKdoHAQ_GUsXS8_Mxv4pq0QgOCJPSJpUHS9SBg_ktSLFElRQp6CuJpLdGackGWomPhdDxT93nIXYt513wNULUfRYNEj211Pjty2ezFj4bWlz1FMRPGPLBBBnqISsc6Xm8Mdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ممثل السيد مجتبى الخامنئي:
- نتوجه بالشكر والامتنان والتقدير إلى المرجعية الدينية في النجف الأشرف، ممثلة بالسيد علي السيستاني، وإلى الدولة العراقية
- نثمن دور الأجهزة الأمنية والحشد الشعبي وأصحاب المواكب وجميع المشاركين من الرجال والنساء والأطفال في مراسم التشييع
- الشعب العراقي سطر ملحمة تاريخية في التضامن الشعبي والإسلامي بحضوره الفاعل في التشييع المهيب
- نشيد بأصحاب المواكب وأبناء الحشد الشعبي وبصمتهم في إنجاح المراسم
- حب القيادة العليا في الجمهورية الإسلامية للشعب العراقي لا يخفى
- العلاقة بين الجانبين تختلف عن سائر البلدان، لما يجمعهما، جذور راسخة ومحبة مع العراق
- السيد مجتبى الخامنئي وجه شكره لكل من أسهم في إنجاح مراسم التشييع ومراسم الأربعين، التي قال إنها جسدت عمق التلاحم
- برنامج وفد السيد مجتبى الخامنئي في العراق محكوم باحترام الشعب العراقي ودولته وسيادته ومؤسساته</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88367" target="_blank">📅 18:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
الجمهورية الاسلامية تعلن الموافقة على تكلفة المرور عبر مضيق هرمز في لجنة الأمن القومي</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88366" target="_blank">📅 18:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇱
🇸🇾
إكسيوس:
اجتماع بين مدير الموساد الإسرائيلي ووزير الخارجية السوري.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88365" target="_blank">📅 18:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88363">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXvNw_sZBLR52pTVUHbyveiiP3jP5o4nhk_OldT950yul0xSdOgJVCfJPD1KiqZHQmhr4DEnu6G40CHImDXPNjUMsfU4VVDMKLITV3B-xvqzLs9cD9oKCliF93dpvnlTwrOHRsajQTMF_FgzaJuUQEKuQjkxdvOypddxlzvp4zMTbeGzsdWbLn_NeIznJqzAKz6JkbjfiUGHHDgL8ZCV7RrrW5ZzCvMShejW2copuAAsLN10aVxDD-bh9OlixRTHmOI_zRfAQt2bjrgYHpltAxFj_dGXCqjIDE6Wi44t1DFuLQolX-vxCxWJVi1YJNO0dqdAoC0V-FT6mapTfT8mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkCdu6oP9PA1uJLnesnI9rSd2a6M224kgxMELJ8CeXAQ5ib1le7itl7zy_El6W8FeA0zRPuQmBfJq_A2rCCCS6B2CNZUJVCNO2i0IqV38b-fXrGVJvmyF1whBcBN4_cvJUkO6W6ggcEYEvBlrVrgWRRyU1X1DQoHF3vzTuMShxSCyj7aOEQ1zIf6xLisRDdrocobEyZHPL3iCY4hrEiMJncvAa76zNz2WiNBnxTYJIDTT6kedQFgDTpxw_mUKxrmB5hTYrVaTOCI-0bYOVQUVQsDxh_7QlVxtbklFhDdinM386R6p3EEHWXoCVPL38rMFuykg3rc7Emqe-dcn1s2BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
رئيس هيئة الحشد الشعبي فالح الفياض: هناك من بذل مئات المليارات من الدولارات لمسخ صورة العراقيين وتغيير هويتهم.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88363" target="_blank">📅 18:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88362">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
🔻
رئيس هيئة الحشد الشعبي فالح الفياض:
هناك من بذل مئات المليارات من الدولارات لمسخ صورة العراقيين وتغيير هويتهم.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88362" target="_blank">📅 18:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88361">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_Ny77Lcp2e_Mhh9l8n3Y1XcS40vgvWN0N5j2p1-lLPVWZNrTAtC-7ZGKhiLUEZmpaO49pFsMYlrLwUtZS5EL4_Z3aiNuGSWmAB5mTVf_eTO-sd57ieZspHm1ht27LT5E3sJAwGVVI0W4X_ATRN9TavahdXBrRBu7vCDCFjMqQEaKFjG3P2nnreg-09iUmdctZX2kywPLNdJfQm8WSYO_ChNOlCEvOLA32TFNe67eR8RL3PKeHI5uDE5NSDdL2kp-tzcsPiWJoHH8fKy_4pvG2MFv7qyuLMGPsPRdVI0xSgLL4HrH-fOyIWOaUiPb3CWh-nKW5miOJ3WuxVrCEhFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
:
استيراد اللحوم المجمدة لتحديد أسعار اللحوم. حسناً، قد ينجح ذلك.
‏ما هي الخطة المتعلقة بالسندات وتجميد عوائد الواردات؟
‏هل توقف مشتري المنازل عن شراء المساكن؟
‏تجميد الرواتب كأجور؟
‏تؤدي السياسة الخارجية الجامدة إلى اقتصاد جامد.
‏الشيء الوحيد الذي لا يزال يتحرك؟ البوميرانغ الإيراني.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88361" target="_blank">📅 17:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88360">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اغتيال زعيم المافيا القوقازية يانيس يوشبايف</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88360" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88359">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حدث امني في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88359" target="_blank">📅 17:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88358">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حدث امني في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88358" target="_blank">📅 17:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88357">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇱
نتن ياهو:
هذا هو طائرة الـ F-35. هل لديكم طائرة بدون طيار في المنزل؟ يمكن أن تكون بنفس القدر من الفتك.
إذا جاءت بأعداد كبيرة، يتم تجهيزها بالأسلحة؛ إنها دقيقة للغاية، ومن الصعب اكتشافها. منذ عدة سنوات، نعمل على إيجاد حل لمشكلة الطائرات بدون طيار. نحن الأكثر تقدمًا في العالم، ولكن هذه مشكلة عالمية.
لقد رأينا ذلك في أوكرانيا، ورأينا ذلك في لبنان، ورأينا ذلك في إيران، والآن يحاولون تجديد ذلك وإدخاله إلى غزة.
تعليماتي إلى المؤسسة الأمنية وقوات الدفاع الإسرائيلية هي أن تفعلوا كل ما هو ممكن ضد هذه الأداة الفتاكة: أن تضربوها، وأن تضربوا من يشغلونها، وأن تضربوا المكان الذي يتم إطلاقها منه.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88357" target="_blank">📅 17:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88356">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
من الحريق الذي اندلع داخل مصفى الدورة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88356" target="_blank">📅 15:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88353">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdeeeac9dd.mp4?token=LA7IWE4OFoj2oZreK7g6EBMiOTCywmDIF2M35_cabd-m5_gwW3Ta5r5ojKRWiBWFmdqrDJCgckHO4fz48Vu38ZZW7yf_BselVs1n8cPqo-dHp5rn3V64REE2iCdKczQIzb7S1UzqpBwDfi-GPUJhTVS-hMyAG8VpGp20wqPI6bKfCMgAmh2lP8sNt8hke4s0MPNldyLXfA9doBp-Yno3EyrklwOKBLKYUCF8sD2uBIjd9R5Ik6ltEtQztm3idWJ0wSbLMMvhncSeihl-f8XiYbKd_9dUdq574Q1XmVAGvmAN9mcUgLDMxxyage-8MsqkMSbUOBZKVnWLMDhx0PA1Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdeeeac9dd.mp4?token=LA7IWE4OFoj2oZreK7g6EBMiOTCywmDIF2M35_cabd-m5_gwW3Ta5r5ojKRWiBWFmdqrDJCgckHO4fz48Vu38ZZW7yf_BselVs1n8cPqo-dHp5rn3V64REE2iCdKczQIzb7S1UzqpBwDfi-GPUJhTVS-hMyAG8VpGp20wqPI6bKfCMgAmh2lP8sNt8hke4s0MPNldyLXfA9doBp-Yno3EyrklwOKBLKYUCF8sD2uBIjd9R5Ik6ltEtQztm3idWJ0wSbLMMvhncSeihl-f8XiYbKd_9dUdq574Q1XmVAGvmAN9mcUgLDMxxyage-8MsqkMSbUOBZKVnWLMDhx0PA1Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من تصاعد اعمدة الدخان في العاصمة بغداد بعد الحريق داخل مصفى الدورة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88353" target="_blank">📅 15:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88352">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
مشاهد من الحريق داخل مصفى الدورة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88352" target="_blank">📅 15:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88351">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cb36e6ce.mp4?token=pzaAHkINPQSAc6Mgiv_SDv4YHfx-Z9gJwe1KTjEmmIUKpFw55NLDULwGPl-Z6brEnt6KAFWgfgfqoYN0larQdHq6q9oG0GkV2FxNirVJhw9-JGpkO-lbvlTjBAcScLbamtUoy_ljJP67v9gDstw9pDMh4zDgM6e9bVe5bN7LS29ZEJoB_A-R2bko7D0gFZF2xN8eWkOskfYvvhtFEPOfvugJYIwWoiGdBaX4yWVaa4UaA5MxPcIvGcMUWPHfmX0D_S1oOjkbytyqtikQdzLsb4S8bGzIsLlx9ffEItk7QCq300xPFSFLAi5tyAFkVwYvwnbtKDP0Qy6Gvv6FbQ6FGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cb36e6ce.mp4?token=pzaAHkINPQSAc6Mgiv_SDv4YHfx-Z9gJwe1KTjEmmIUKpFw55NLDULwGPl-Z6brEnt6KAFWgfgfqoYN0larQdHq6q9oG0GkV2FxNirVJhw9-JGpkO-lbvlTjBAcScLbamtUoy_ljJP67v9gDstw9pDMh4zDgM6e9bVe5bN7LS29ZEJoB_A-R2bko7D0gFZF2xN8eWkOskfYvvhtFEPOfvugJYIwWoiGdBaX4yWVaa4UaA5MxPcIvGcMUWPHfmX0D_S1oOjkbytyqtikQdzLsb4S8bGzIsLlx9ffEItk7QCq300xPFSFLAi5tyAFkVwYvwnbtKDP0Qy6Gvv6FbQ6FGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من تصاعد اعمدة الدخان في بغداد وسط انباء عن اندلاع حريق داخل مصفى الدورة</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88351" target="_blank">📅 15:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88350">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEbePPkRfnlvBESf8DQXD6DAxJvfMPwuyaqpwvuRYSzICNPMQDgn8CFTuUjcnbaquQbqolH4SzwvAUXkiKjbBnSQ4R-9Z7ibtntdZTeSo11NpXCaPRJZm7cDkz0Pb-YF5ypF87xBwK0bs4RdoPju5D5hBC48wLVGmipAYhS9EcuzWqEI2iwERr0QsgkoXNmahAi8zDoS6tlVOJdPsK1MkO6B-SNejg60w5-a4mPoopPIQGuHjINhRCfhCekz4SBoNPYXKVwfWadWL8z4NRWPPYvhq_h7hTTysiEQ-N-pnDQuQNh5pgZDdrq-O69hUd48RTQNrnTkp8BgkiW2iXtuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حريق كبير داخل في منطقة الدورة ضمن العاصمة بغداد وانباء اولية على ان الحريق داخل مصفى الدورة</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88350" target="_blank">📅 15:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88349">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية: هيئة الرأي تقر فرصة امتحانية استثنائية لطلبة الثالث المتوسط والسادس الإعدادي
ويؤدي المشمولون الامتحان ضمن دور خاص تعلن اللجنة الدائمة للامتحانات العامة موعده لاحقا، كما حددت الوزارة مبلغ 50 ألف دينار للطالب الراغب بالاستفادة من الفرصة، وتخصص لتغطية أجور الامتحانات ومستلزماتها.
وتكون هذه الفرصة استثنائية ونهائية، ويعد العام الدراسي 2025–2026 آخر عام لتطبيقها، فيما يرفع القرار إلى مجلس الوزراء للمصادقة عليه.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88349" target="_blank">📅 14:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88347">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGTZKheqEs52c5PCtjGH4LSPXRRxCTskhbvy5nqA15Hv8R_95mQdKHkkcQApNEkk1LxdJLrNUhYwWocXqkwlF4OvrKg6aPfDq_TkO08mJiH8QDxIBqmMSUyQM6QxySkq6OAD6c2qbVngbDidSxvt6KwpqfWygKBHXw5RRO9behsQw46-temh0n7vPv0kNAbIL0-5hRJ-nZkYcc8Zm7kzM7k0xQ19-tMY-oPMOFqzN4Jb-8FqE0ZbWJcB0XsYXWQtBvoWKNZ4eok8UwuxgFvtA7-ycilK81o9MiZQf1ehy84JvEdGsmY9YGraxbbRK28BE_RqHFQc9gG2YouR9Xj4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظ على نظافة بلدك من اتباع يزيد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88347" target="_blank">📅 13:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88346">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري اللواء "إسماعيل قاآني":
القضية الفلسطينية، من البحر إلى النهر، أكثر حيوية وقربًا من التحقيق من أي وقت مضى.
توسيع المستوطنات وجرائم الصهاينة هي محاولة للهروب من الأزمة والجمود العميق العسكري والأمني والسياسي والاجتماعي في الأراضي المحتلة، ولا يمكنها إخفاء الهزائم الاستراتيجية التي تكبدها منذ السابع من أكتوبر وحتى الآن.
القضية الفلسطينية هي حلم حيّ ودائم؛ حلم سيبقى قائمًا بمساعدة الله حتى يتحقق نصر الحق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88346" target="_blank">📅 11:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88344">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUfla8ry1M0nLw_wmP_C5UugefUX7JN61LXbbx3ZX2UfOCr9Yt-I0CvEbSrLTesbXa3rMt8jLrkGoXI5O03iar1COIvyK0ZE-rxzjbrc14ZMPt3-DSFbMXBoP18OdpbrphMgSy9PYBi4m1a82vSriVUGxyy5MtfKDF6S0GPHmARElgiuCvYpYqoccE66T18s-bqNkB201SLHTQUSxdmzyjBcGjX6o37kTU7SAUgu16eZuedyRA7Ty9O3CKSfJfBAt-ZBn5NCa35Ct0BlXAT1x2a7EWiPPgbScLLFbcLzj1cUTBew_YMppUwf8jI9icVq0_-wlzdoVMJArahwO-0x-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0xaDTKxzOgWupr0mYzkPmGAVZAV4M_trw37RpuAZF8L_VwzqSiAGktRg9wO-w18lBuabSyLhj0IsLZErNnPzDv5jcRyHhdSOijVfr5Hq7wRtWk4S2CNPWSWj317V5m-lhw0D6sq1pntqjx2dCVqKeKyqplHSUm-ckye2LQMp1yHhqb0t324eryIABroiXAIcnhVJK9Gko7wh4c1sujwTGMum8HN8yXqMKWjJ1IHavnOwhWdnciybOcO2qqvgIpS-kBr66FKzK3HMIXaWl4kXSbu1n79rSfOnQgYn0_rBcdf2RfWQn7MixCOBj3BsAh_19OLqWfnngtTODfu5KHxNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
منتخبنا الوطني للسيدات يخسر ثاني مبارياتهِ الأسيوية في بطولة كرة الطائرة أمام الصين تايبيه بثلاثة أشواط دون مقابل؛
"انتم مال دولمة تخربوا بالطائرة ليش"</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88344" target="_blank">📅 11:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88343">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏
🤡
زيلينسكي: اتفقنا مع ألمانيا على توريد 600 صاروخ اعتراضي من طراز PAC-2 خلال عامي 2027 و2028</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88343" target="_blank">📅 11:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88342">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
الإعلام السعودي:
قائد الجيش الباكستاني سيحمل رسائل أميركية لإيران خلال زيارته غدا.
‏زيارة قائد جيش باكستان لإيران ستحاول كسر حالة الجمود واستئناف المفاوضات.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88342" target="_blank">📅 11:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88341">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇸🇾
🇮🇱
وزير خارجية الجولاني:
نتوقع استئناف المحادثات مع إسرائيل بشأن اتفاق أمني قريبا.
سوريا تمد يدها للدبلوماسية وتحث إسرائيل على اغتنام هذه الفرصة التاريخية.
الاتصالات مع إسرائيل انقطعت بعد هجومها على قاعدة أبو الظهور الجوية في 18 أغسطس.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88341" target="_blank">📅 11:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88340">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165cbecbdc.mp4?token=ZlCcT5N6kHEUgJtoki6WLzc4Md_8sRRIBl1wcIUqWLoe9ZhWBaHwksgSeDMhZBqYFueMGwvtTK_96jL-4EEjD6ecfbeCI0M3A3rxGKvGDWGRP-xm49x70IZYjtVHcpwvf86big0Ga54rqMyepYhxUzm81_pNhmBpbv4EdU5HuEwz-rtLyFzqFRkwC_mnZxs0RYSgUDKpDkXHluJNoB0t0rL44kDA-Y1SySofoZgIsNyjkAq6OdhXAzup_g6q4SbpcCR3INZv6mhLM-Jmq24T2XQ1vDid7pcq48DLhac4lByCNkUZqGyTUv6qISBVpARHFNA1oeJmmzSLwML5JPjY4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165cbecbdc.mp4?token=ZlCcT5N6kHEUgJtoki6WLzc4Md_8sRRIBl1wcIUqWLoe9ZhWBaHwksgSeDMhZBqYFueMGwvtTK_96jL-4EEjD6ecfbeCI0M3A3rxGKvGDWGRP-xm49x70IZYjtVHcpwvf86big0Ga54rqMyepYhxUzm81_pNhmBpbv4EdU5HuEwz-rtLyFzqFRkwC_mnZxs0RYSgUDKpDkXHluJNoB0t0rL44kDA-Y1SySofoZgIsNyjkAq6OdhXAzup_g6q4SbpcCR3INZv6mhLM-Jmq24T2XQ1vDid7pcq48DLhac4lByCNkUZqGyTUv6qISBVpARHFNA1oeJmmzSLwML5JPjY4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
🇮🇱
لحظة إنقضاض البطل الفلسطيني على المستوطن الصهيوني وتنفيذه عملية الطعن.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88340" target="_blank">📅 10:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88339">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7fc53e44.mp4?token=DLMLewwoXmDCYKYir-3z60Dl9JZsEF3o3WA7fhO4V1htp16EP15_btvJszyzgp3hb5XzGoTSYHfazlSfmLX4k2ccU9e8NVJvTUa-ryCN6r4yfGZULKPw3Zuul2BZWVv1uz2ll0BniSVNNy-Hme7hWn4JvxnjNqiDOjm8yzg3VBDbo10u_pVUkjXguf6VoaLnxEF1MUXxMdunilSXWn8V1vo5OvwB3PuvHvONOveCW1DOwnwXL0GwVvp751RDebndYzW_1_T09lknwxyenMFoaJFUSXxwAK_HGElMtinh9o5y6BLI92UqIoi9F_nagbz0vCMY2EiPrSx_vmtmOlDDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7fc53e44.mp4?token=DLMLewwoXmDCYKYir-3z60Dl9JZsEF3o3WA7fhO4V1htp16EP15_btvJszyzgp3hb5XzGoTSYHfazlSfmLX4k2ccU9e8NVJvTUa-ryCN6r4yfGZULKPw3Zuul2BZWVv1uz2ll0BniSVNNy-Hme7hWn4JvxnjNqiDOjm8yzg3VBDbo10u_pVUkjXguf6VoaLnxEF1MUXxMdunilSXWn8V1vo5OvwB3PuvHvONOveCW1DOwnwXL0GwVvp751RDebndYzW_1_T09lknwxyenMFoaJFUSXxwAK_HGElMtinh9o5y6BLI92UqIoi9F_nagbz0vCMY2EiPrSx_vmtmOlDDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
عملية طعن في منطقة الأغوار بفلسطين المحتلة، إصابة صهيوني كحصيلة أولية؛ المنفذ تمكن من الإنسحاب.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88339" target="_blank">📅 10:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88338">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تستهدف مواقع مرتزقة السعودية جنوبي مدينة الحديدة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88338" target="_blank">📅 10:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88337">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vObk_uFV-7XgXvNOdSRPZcC9zFAQw-lw1TJUEn9mPdV6Dg6KHHDdC7b8f3Qs9mK8lZEoc-V3KYjOH41q4f-aSW6Qgmi5dnant5_BUrcSxaplOmGb2JBmd99BP1P45DHqyxk-sK-zmIl-D9GpTebY6HiiZzSfcpa6Jbft3gNIIKsD8-VriQ-nQAv6tGffIlUPddULJWiC4UB2oxHC_JHNYgTTPvedOuI84WiAHBByNNJ4eOFce1UsJLaMb3aKFpPMUFa_KTXDRIXhjv3qeKTxjF7s8ARUyH5y1IfFnOqVAXou3Tujzhib5_w4TD59EM-V_K8-8Pw3xfrB4tkNZuLySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
عملية طعن في منطقة الأغوار بفلسطين المحتلة، إصابة صهيوني كحصيلة أولية؛ المنفذ تمكن من الإنسحاب.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88337" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88336">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReIK4bNR7OAE0vRRy58JIPC7Y90OfGTwNCvMWrsO8gJ4Xk-ZGY6FlB6RZAxPmG2wS1fqJYAdoVVGoqOIan86TJiZsn9fu0ymKLFvMiVZ3SzDceFxXmlpcGV74Ot-mjpC3P7rrVwcaT2MftAsnVGKqW5cIiay4RoLDZWKSBPRBvjJo8pAcy0Ao8H9scgdSTKTa8bop6pQqgRZGVkIflFg5ixNYAeF9_En8e5oGQ6_LiMEaKclPOqHvVzaxGxFGdlkVACJT-wbgy5xDcPcrPptaJdejSTf3yRuV6soD1j3XwY6rgobQOfZ3V5Qo_bjMxtTU9t6cEVZ06aUKlwSqO1uEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يهاجم كندا مجدداً.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88336" target="_blank">📅 08:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88335">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTpaIOspoNNQmyakuefNpxPxslT75yktyT3q3D5QbC9bgjCUpH2N47lgAb9iAIklHRAsmsa8fFq27dMKG6fCrndUM75N97Ld1wBdSCDNXy0pDy5qNim_CvJt3kGfLN6EU8r15ee9yaAvbrpEogzBtyMkrtc4w6eBSgSXp0cdqjkQjkO7Y7SY01iQ25iV4uWRS2oZDrayI1lqdJmgtpDnWbvnxJES-Hi6m82R9iGKf3HqoqKApRObcvna1z7h0pmAHU9AugU92P4NaAC_OGlbmSN9-zCDwxmXY63ynxgrs9s1_9ylBvq4EvWAi0_b22L4AvbV_l1aTuFudj7vh1YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الغربي: ‏
هناك أمر غريب يحدث مع ناقلة النفط "نيو فويج". لم تتحرك بالقرب من مضيق هرمز خلال الساعتين الماضيتين. ويشير موقعها عبر نظام التعرف الآلي (AIS) إلى أنها راسية. كانت متجهة من الإمارات العربية المتحدة، والآن عادت أدراجها دون أن تتحرك.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/88335" target="_blank">📅 00:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88334">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDoWiUPKDP-zhOY0KPSw6x6sfWdlhtItZveR8ZvIaheAxOp451ni1KIdMoiMI98CId2YZbGze8Y_am_YbwHXkR73k3ET8-xtORaGm-3Vu2mrShhehtae76jfxL5hiAI1Qm3zNxAgajcIta6YXcmJ8N_do8mjEeff2iw2BR7e_TqlNj5zBvTtnPqi43LKTq1-lmIZKsgHRCplZVCbFAmIeAbD858rgpy6cBsVZcpPeM1eTr1FyWikbv-TV-fHLtHBFuxV5Fk8rUGCQmVfE6o0B7f9IyHtutTqGMXj3GWKH1s6Ep1jHXf4VNAni5rJZ2H8UwR3RZJYhO8fXAwa5zvdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب يعيد نشر تغريدة بخصوص مضيق هرمز اراضي امريكية
😫</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/88334" target="_blank">📅 00:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88332">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07055ecbb.mp4?token=fVMrOr_ig3ivYXU0zwE6cAIwVcf-MzLtNVA2-rufzKW8FcT-4eTiGpUHWGxmsNF34o2e5A6oxOlEZii20ELHzTC0FZVdfHF_ocRKu-wQmmEHDwugey6uKUefdZskYaSiL_SF4GsOcYZ03YAjXK4VkqLUw3Lop0qJj-1bUg8YrKcIVnU3qJjxvx1WI_PjA6BdgG1O-N1B6EUDsOt6VD6GJD3M0ob4fpAwsjyEQWgs9ev5EmxkePMSFMC91s_NXnunTA2F1Yve7umrJLIcPKL5q-MuLAetkaBJNsvbZQOivEjIJpHlKQ_nRy7bIma7osNSAk8trakjexrtEBwKdL9zQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07055ecbb.mp4?token=fVMrOr_ig3ivYXU0zwE6cAIwVcf-MzLtNVA2-rufzKW8FcT-4eTiGpUHWGxmsNF34o2e5A6oxOlEZii20ELHzTC0FZVdfHF_ocRKu-wQmmEHDwugey6uKUefdZskYaSiL_SF4GsOcYZ03YAjXK4VkqLUw3Lop0qJj-1bUg8YrKcIVnU3qJjxvx1WI_PjA6BdgG1O-N1B6EUDsOt6VD6GJD3M0ob4fpAwsjyEQWgs9ev5EmxkePMSFMC91s_NXnunTA2F1Yve7umrJLIcPKL5q-MuLAetkaBJNsvbZQOivEjIJpHlKQ_nRy7bIma7osNSAk8trakjexrtEBwKdL9zQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الأمين العام للمجلس الأعلى للأمن القومي الإيراني "محسن رضايي":
إذا ما أراد ترامب القيام بأعمال ما، فسوف نردّ عليه بقوة وعزم.
بالتأكيد، سنقوم بإجراء تغييرات في مسألة إدارة أساليب الحرب، وستحدث تحولات في السلوك الدبلوماسي لإيران.
نقول لجميع الدول المجاورة: لا تشاركوا في الحرب الاقتصادية الأمريكة ضدنا، وإلا سنعتبركم أعداء.
نحن لا نسعى لتوسيع نطاق الحرب، ولكن إذا انضمت الدول المجاورة لإيران إلى الحرب الاقتصادية الأمريكية، فسوف نضرّ بمصالحهم.
إذا انضمت الدول المجاورة لإيران إلى الحرب الاقتصادية الأمريكية ضدنا ، فلن تخرج قطرة نفط واحدة من الخليج الفارسي ومضيق هرمز، وسنستهدف أيضًا الطرق الأخرى التي يتم من خلالها تصدير النفط من الخليج الفارسي.
مضيق هرمز مغلق ولن يفتح إلا إذا التزمت الولايات المتحدة بجميع التزاماتها.
أنصح الأمريكيين بعدم إرسال أي قوات إضافية، لأننا سنرد عليهم.
أي حركة تقوم بها الولايات المتحدة في الاتجاه الجنوبي لمضيق هرمز، ستكون هدفًا.
أي اجتماع يعقدونه مع جماعات معارضة للثورة في المنطقة، سنستهدف ذلك المكان أيضًا.
لم نقم حتى الآن بمهاجمة أي من المصالح الاقتصادية الأمريكية.
حتى الآن، استهدفنا فقط القواعد العسكرية، ولكن إذا ما تم تصعيد الحرب الاقتصادية، فنحن مستعدون لاستهداف جميع الشركات النفطية والاقتصادية الأمريكية في المنطقة.
سندافع عن إيران بكل قوة ولن نسمح بعودة الأمريكيين إلى إيران.
نبيع النفط يومياً بكميات تعادل إنتاجنا، خلف السفن البحرية الأمريكية.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/88332" target="_blank">📅 22:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88331">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
رئيس المجلس الأعلى الإسلامي الشيخ همام حمودي:
لن يفلح أي رهان على حرب شيعية- شيعية بوجود المرجعية العليا والالتزام الديني ووعي أبناء شعبنا بحقيقة المؤامرة الخبيثة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88331" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88330">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d826f753.mp4?token=NB9nAAOKE22JmQHQTlr18leMslvTNKJJEkK4GMqZdq5snAABoP5Tz948EVqkqndLRmTWXH4_w2c2j8tRgo81WJRd-uFaZQUr2ClwhzyLrUaYjR2L5sylBC0F1kp893xYtsZgLwt2iEgszVGo5eBFnw8SNfHekjJspfpFnCb1L74Yh1UiIUZfC62Eh3wRFoi3vYxyGb3punc8ELZzkI1Zjh9I0izbGHwUWti9pdyI9VaHeC6BRqXpsHOA1Je5nmPvmpppt6LRqp0q365iEF719t3RVEIU2lAiultPdafJoQpj4KwgaP0xvlmmQz1n5zQTAxGjCe85DoS-772ydB2Efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d826f753.mp4?token=NB9nAAOKE22JmQHQTlr18leMslvTNKJJEkK4GMqZdq5snAABoP5Tz948EVqkqndLRmTWXH4_w2c2j8tRgo81WJRd-uFaZQUr2ClwhzyLrUaYjR2L5sylBC0F1kp893xYtsZgLwt2iEgszVGo5eBFnw8SNfHekjJspfpFnCb1L74Yh1UiIUZfC62Eh3wRFoi3vYxyGb3punc8ELZzkI1Zjh9I0izbGHwUWti9pdyI9VaHeC6BRqXpsHOA1Je5nmPvmpppt6LRqp0q365iEF719t3RVEIU2lAiultPdafJoQpj4KwgaP0xvlmmQz1n5zQTAxGjCe85DoS-772ydB2Efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الإمارات تكمل بناء أقفاص معدنية ضخمة حول خزانات تخزين الوقود في أبو ظبي للحماية من هجمات الطائرات الإيرانية بدون طيار، وذلك بعد نحو أربعة أشهر من العمل.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/88330" target="_blank">📅 21:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88329">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaJbAmg5X03GPkqolKP91JILYvbQjqUKPWbdx4c8ZPoaZqqYaUuYMweIdx-_a2Z2rTJEuI0bllzaqcwOZ0X6Eq2Wz1H2KQQiIHLMb36Qgj5NEf2nrVDBt7HKensPCeavMU6OEb8gb6i3Jhw8KT5VLzuNbf-BdYyKLMZtuZgizD3rY5uem7p5qEb7oFTt8BK4MaK4dmo9Fv4ZIXyOTHeqNe6YaqrZ425pVtDMXGwuANgfU3DNUds8f_BkXsdjFBTzcoubs8VgIMaERrYgtzaZ2SFP8b3NYthMzUbfvBqzPiDv_XpbjKffKWGG4rJLhrqzadT6qEuNf14gtFMobRfQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارات اسرائيلية على الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88329" target="_blank">📅 21:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88328">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇱
‏
نتنياهو
: لن تقوم دولة فلسطينية تسيطر عليها إيران لا في غزة ولا في الضفة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88328" target="_blank">📅 20:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0551d70e8.mp4?token=XDvAC8hiB9iDsb71XSxb3Vsksmf2YRfiyhoUexIlCJsQ136zZ2gzEZRKz2VxSxsmGO3WMEhZw4hUx-1Wozxc6KpFY1HzJwj5woda3af8lEo4onlX84GNp0SqHeB2utyW8e1MXfuhbhJWT83nurJrhxgROJruuIx19fc4FET0BKwb2nCpWZtyuIa-1WmkTWHXNeJPBGuQ2NKXdkfpSJj9OD5b7Q6ZHqDhRKTk322QHnbsRRJyOpkvKlG2O9lRjFKxM3rdcCPWl4M584ro8dtsJCAixy9d2L5yfgrLBYBlU3kzXfjbmHM3KBkby7_GNE08fI-qcu1xxa2WjV8gGFDhxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0551d70e8.mp4?token=XDvAC8hiB9iDsb71XSxb3Vsksmf2YRfiyhoUexIlCJsQ136zZ2gzEZRKz2VxSxsmGO3WMEhZw4hUx-1Wozxc6KpFY1HzJwj5woda3af8lEo4onlX84GNp0SqHeB2utyW8e1MXfuhbhJWT83nurJrhxgROJruuIx19fc4FET0BKwb2nCpWZtyuIa-1WmkTWHXNeJPBGuQ2NKXdkfpSJj9OD5b7Q6ZHqDhRKTk322QHnbsRRJyOpkvKlG2O9lRjFKxM3rdcCPWl4M584ro8dtsJCAixy9d2L5yfgrLBYBlU3kzXfjbmHM3KBkby7_GNE08fI-qcu1xxa2WjV8gGFDhxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد نايا
منصات مقربة من فصائل المقاومة تنشر  مقطع فديو لم يتسنى التأكد من صحته مع عبارة " ستعرفنا ستعرفنا قريبا " المقطع اظهر مسيرات من طراز حديد 110 التي تعمل بنظام المحرك النفاث .. فيما لم يعرف دقة او وقت الفديو او مدى جديته ٌ ..</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88327" target="_blank">📅 20:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrl1C-XJamRQJYcCfyf9hmbZrmaPpFM4zTPV1cSQTwfs6uteHR4SH8dBzHmlCnsx_IJjLRWiY_Br5daW9Hzjj3qwmY8qT-RFdqlBCXVIiOrSPN3GQULZZflkosXtMsYlJjbRfR_VFo7UI_D7wQ7iZoxQpzhkd1VylJMYXwqD20lrk07VLZyadQNesvEU-CQ_G4XGwsgzMcOb-7FDybUFejAWAyJcfX1jkkB-1x6tfoOUi3I6-UdkBp9WceU4iojwjRj2CxFODmoRfLiBnwwlXsqheM274QnVFvreUG94_1XG1bGW038i9zKFs_BfSryD2EuQ5TRPiMRF2SI86GKJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العبوة انفجرت بباص تابع لعصابات الجولاني على طريق معرونة – صيدنايا بريف دمشق</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88326" target="_blank">📅 19:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88325">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجار عبوة ناسفة في ريف دمشق</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88325" target="_blank">📅 19:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88324">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجار عبوة ناسفة في ريف دمشق</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88324" target="_blank">📅 19:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88323">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏
🇮🇶
وزير الاتصالات العراقي:
ملف حصر السلاح بيد الدولة يحتاج إلى واقعية ونقاش عميق ولا يمكن حسم ملف حصر السلاح بيد الدولة بمهل زمنية محددة أو تواريخ ضيقة</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88323" target="_blank">📅 19:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88322">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇨🇦
رئيس الوزراء الكندي:
لا يمكننا قبول عرض الولايات المتحدة، ولن نقبل مطالبها.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88322" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc26914f9.mp4?token=sWzdoqioFpy_bEQ7TReC9WthLnwanMtUs8KhkORdV4_FUcve91k1F2l0zcL-d-9Fm9jtEfZAD4rjmdhgtDf-HLe2YdKDgpom1b4cvmX9Ifrd49QUzbrmmOxD4QTA0ZIpasArXzox30hjErBzF3dDrsNn30fECu5NIOVuSddfDKc96cL_7bXolezXC-INxv5bcG047OKzhmKF2C9hx9mqZX-c5fExonn2eaEZLUDCW1cHyUsGO9fPVBYJPFeTm2BkdBbGYXVP2zX_RBXOQ1P7b8PxsPFo_wqfbioK6C0w7WfEikx7X4DY_9FOS0vQs19ilYv_T7IaN70k2Va-O5SkjJwA0bFWe2vw_3QYpjjoRZgzSjPemXUcHtKDJUc-wvXsdJ0lxWTBQbBYGqy6p1Jgh3RoByQf8o1GeG5B8tfG480cIIRkRN3yy06M9Y9AnCWhYT6XUG4gzGrchMTA9ixoXv_ozDrxFe7mFvSYvQdUmAAaXwi1v46v5oSiEMbVkMQxhEzZrav5JkGZ7WVW9Ik7WhQVC-FbcUpOtrnUmKIxXzbKMLnqd9TCeHLQ1m4_6oMYMfbpcxKuJ6QJ8nMwKu0jjMutnecdr-GVeLuBqkv3Sj-RRYEVRTGQNonzTwTK-uZBSzOjI7pC_Pvzw6wmbCUeNQF6noS9PK4AuyutZFnydOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc26914f9.mp4?token=sWzdoqioFpy_bEQ7TReC9WthLnwanMtUs8KhkORdV4_FUcve91k1F2l0zcL-d-9Fm9jtEfZAD4rjmdhgtDf-HLe2YdKDgpom1b4cvmX9Ifrd49QUzbrmmOxD4QTA0ZIpasArXzox30hjErBzF3dDrsNn30fECu5NIOVuSddfDKc96cL_7bXolezXC-INxv5bcG047OKzhmKF2C9hx9mqZX-c5fExonn2eaEZLUDCW1cHyUsGO9fPVBYJPFeTm2BkdBbGYXVP2zX_RBXOQ1P7b8PxsPFo_wqfbioK6C0w7WfEikx7X4DY_9FOS0vQs19ilYv_T7IaN70k2Va-O5SkjJwA0bFWe2vw_3QYpjjoRZgzSjPemXUcHtKDJUc-wvXsdJ0lxWTBQbBYGqy6p1Jgh3RoByQf8o1GeG5B8tfG480cIIRkRN3yy06M9Y9AnCWhYT6XUG4gzGrchMTA9ixoXv_ozDrxFe7mFvSYvQdUmAAaXwi1v46v5oSiEMbVkMQxhEzZrav5JkGZ7WVW9Ik7WhQVC-FbcUpOtrnUmKIxXzbKMLnqd9TCeHLQ1m4_6oMYMfbpcxKuJ6QJ8nMwKu0jjMutnecdr-GVeLuBqkv3Sj-RRYEVRTGQNonzTwTK-uZBSzOjI7pC_Pvzw6wmbCUeNQF6noS9PK4AuyutZFnydOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇶
مركبة تابعة لجيش الاحتلال التركي تمنع شاحنة لمواطن عراقي كردي من المرور في قضاء شيلادزي ضمن محافظة دهوك باقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88321" target="_blank">📅 17:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انباء اولية عن اختطاف أكثر من 60 مصلياً من مسجد في نيجيريا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88320" target="_blank">📅 17:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2655fd592.mp4?token=p-Ll6oLRYw0rUpCxDjUmRjG1ENM3IP3NRGQG9WmBiLTnGbiepAN0HDcVZsXsCaye3MJm55Dp1zLI-mHSk-4eLPiOe0OyXJKJyPTeOgvF5QQ8j8ne_o_iauQVdrqh7vjmVz8IgizqxbDKpDf__F9ixAQxZZ-5vcthI2nz9LOJR409xajXXk7wS5bPBm8mDw6jzfqd90dh3dveyWbyKLRhjdB7vzCx5ILysCiwKx8A2t8hcwYA8dSi-Ve7ruYG2Ptyhbl-Dcy2JGie9rSi6Qfwr71WYJAsPvdWXjlR5APLmsHNNiAC3q3Pq6Odo520UmjYCb6szwqtKKI6R9YyOmNpAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2655fd592.mp4?token=p-Ll6oLRYw0rUpCxDjUmRjG1ENM3IP3NRGQG9WmBiLTnGbiepAN0HDcVZsXsCaye3MJm55Dp1zLI-mHSk-4eLPiOe0OyXJKJyPTeOgvF5QQ8j8ne_o_iauQVdrqh7vjmVz8IgizqxbDKpDf__F9ixAQxZZ-5vcthI2nz9LOJR409xajXXk7wS5bPBm8mDw6jzfqd90dh3dveyWbyKLRhjdB7vzCx5ILysCiwKx8A2t8hcwYA8dSi-Ve7ruYG2Ptyhbl-Dcy2JGie9rSi6Qfwr71WYJAsPvdWXjlR5APLmsHNNiAC3q3Pq6Odo520UmjYCb6szwqtKKI6R9YyOmNpAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدور مذكرة إلقاء قبض بحق مواطن سوري يقيم في العراق على خلفية امتلاكه عصابة وقيامه بتهديد مواطنين عراقيين بعصابات الجولاني في حال توجههم إلى سوريا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88319" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇱
🇸🇾
‏
وزير الحرب الصهيوني:
وجهنا إنذارًا مباشرًا إلى دمشق قبل تنفيذ الغارة على "مطار أبو الظهور" وتم إبلاغ السلطات الأميركية بالمعلومات الاستخباراتية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88318" target="_blank">📅 16:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCr7hTbXTnPB4jFu3D1k_BCQktIjwVQcLRtOwU3lltq4FAsCDASNVhryhC7uXcwI08KEbplhdWCnjv7j4muywtnFANvqVfaIVUZq4uXoFsjg5Tio8yofUNp_khYGZCIczjizpAnKd-_xOdLFdLjCBrViaGdJ7bhNceUHLrsGD1QMjy84Qdab4AdULpYH-8-2KydmonnC6lMoDq2a5cqTEPn-mYmQRYPlYEW5yZT00B4nSN0WiGPMRfsMUQfBd6sdGSrGe1GDKx9nzr9CElSptsSRier33lYs4NmQNHfNEH2G8DK2P4lg1ZTZO-uwlKlNvxV6iFJIJ_JgBCz1XPvt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
بيانات التتبع:
‏
تستمر صادرات السعودية من ينبع في الانخفاض. شحنة واحدة فقط من ناقلات النفط العملاقة (VLCC) قيد التحميل. ترسو عدة ناقلات من فئة أفراماكس أو أصغر حجماً في رصيف أرامكو. من المرجح أن يكون إجمالي صادرات المنتجات المكررة والنفط الخام أقل من 4 ملايين برميل يومياً. ربما يلجأ السعوديون إلى تحويل مسار النفط للاستهلاك المحلي بعد هجمات الحوثيين المتكررة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88317" target="_blank">📅 16:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لحظة الانفجار داخل احدى المصافي في منطقة دارمان ضمن محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88316" target="_blank">📅 16:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE-D4lbnsm2ftbAC9jBzeZd9RzXGnkDbqcuJ9rD2Ts4Q9GzLMYN-Xt6uf-Zix0rd-UfezWwD1pO_8VE1fg-tuhX5_jAdXo64bAY0BAj8RStfBDRz5VouIh_-YttnEY5U0ROLCJY-JAW_Pps9E5CBbsD0CKmH5FfyG5jym_XI6TkrPijgvf7taSQpqo-Sp8BHYRyXJorucdgL-99YOlzv4lHwTGrwHQNbpjVt3qfe3J-uDaTA_cdI0wtk5tobGPsc2gV5-Pg8K8hAUcgXORH2wm96yYUxJq3cXRPN_jC_KSLWVMYQZf9BBAxIzWkEc5br8ApKDTWRQLnd5k3WBbw9rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
ارتفاع اسعار الحديد في دولة نيكاراغوا
#دنيا_وصفت_ياناس</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88315" target="_blank">📅 15:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDIpXv23Z4n0RfjUjt7exeyFbrOOEEds6or96KF49F-G3dSWLsnJLUsLAqawuoQ_6SewuKtmCyT8vk24ScTFyLb0ZmEE3E8LSKFBDuKmVFXybh078cccxjHy0WG8q4qRu9et86vDDh1_42UxaeRRf1cVXdEt81GfS4g8qvTJXOsWaPUhJjGfmYB98iMaMeXUrYtLFhy-rvwO71P_Hb9XbewQTsDmUfiXnp9Z5r9UFodwOEJI7B0nr_NTOYeaoQGSNBLZHnxRZeQ4J9BAJgoR55FpLfY-YnOFpLyYsMn7Z_l_OZ3nGDI3DyyBH8dT3PqUfWqekye-ab8fiMJlYGOrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZC37AmK13jTr5Ae0bpFDUN7kYd2cO3_q5QcOJkvSRNts7u8altyh_g6uuFzhgW8iSksUuI3tvW3trlvFDqB-iVE_8IYGblqrk9R0dobgo-zOEgrf5lv3ZDJNTyg_Z27VMnnSHOU3iKHJAMunaGP0Fd9HeHmk_vaQuh5lq-OWj36LNR56kSxFlixUqVRs1DozEOz3_OgZdCPRbLS1qbUFu4y2ER1ney_2k3QQMhQW5nkbKARnwcd58eVBNN5c9sUmqz_j5m979TV7fZwLPXe5psy_SKUPbhcxp7l_ZfaJ-6JByebTbxOJhDo4BU0HPVAT_ZVg3jL3SksqU9tMONrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR0tniIj5JXehOh5yccSWgnAVnIe3warhe80Y3UUa7kJ3hHFB6Quni-KiiCjyMAiuMz6noXF_PcAURseBWA96sITHf47T7nERq-ljBqfmGL7nYZM_Bo2_6yfUPgTlm9G8Mk8f4MlvugyEhiG2zUXALLrYNyPAlf6uKMiqAKXcojMPjSuDbWF0oF_2ZpTuts3gk0sL7t8V1u8lynA4XVsQUXsWTI7cHkyg5xkSj0YHnU8wNe5sTIb6BNCUzA8jhK3R37Zz8RchJRja7PNHPCLoxWLfy_2lmADaVZKdcz81LHQCO6cA-H0xtz3lvFeNmC2MpalZJ2_zslafNBjxUNfTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
تمهيداً لمعركة كبيرة في حال لم يسلم لاهور نفسه.. نقل دبابات الى محيط فندق لالازار بمحافظة السليمانية مكان تواجد لاهور شيخ جنكي.  انتقال تانک به اطراف هتل لاله‌زار در السلیمانیه که "لاهور شیخ جنکی" در آن حضور دارد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88312" target="_blank">📅 15:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84232b8c8.mp4?token=KsNqMCR5J1c1-zG3HGNbB6lEGYi2MzphlURRi0AGuhPNVzhGskQl7BdpLUJt4wwcj_wu3keuMhJS-7wR0_HffpRKgnAzNP3vhZ6Wc_5zCmlnq2FT2fBIE2b9ZCsVD3cDeeFwprvIxT8xAmuLEWsdDfcRulrnwgEpP6TCCBmqpwdxNiN68PGBL_1q1WT0OZA3Z1c2fs0wIXyw_dzirZwTE5G_hhZY8_9vuQR8rCjToAxQeghWJyh1uumyqab_OLIokOYja36jpJ_eEQueF9lZoCVxKGWflMT_04ANciR7uL7fl6A-9EztOjF393l610CYAFxhJwXrc7oVdVtW-rRiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84232b8c8.mp4?token=KsNqMCR5J1c1-zG3HGNbB6lEGYi2MzphlURRi0AGuhPNVzhGskQl7BdpLUJt4wwcj_wu3keuMhJS-7wR0_HffpRKgnAzNP3vhZ6Wc_5zCmlnq2FT2fBIE2b9ZCsVD3cDeeFwprvIxT8xAmuLEWsdDfcRulrnwgEpP6TCCBmqpwdxNiN68PGBL_1q1WT0OZA3Z1c2fs0wIXyw_dzirZwTE5G_hhZY8_9vuQR8rCjToAxQeghWJyh1uumyqab_OLIokOYja36jpJ_eEQueF9lZoCVxKGWflMT_04ANciR7uL7fl6A-9EztOjF393l610CYAFxhJwXrc7oVdVtW-rRiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الإمارات تكمل بناء أقفاص معدنية ضخمة حول خزانات تخزين الوقود في أبو ظبي للحماية من هجمات الطائرات الإيرانية بدون طيار، وذلك بعد نحو أربعة أشهر من العمل.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88311" target="_blank">📅 14:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNFPegoyDaPgLY-wvNRHvgDQT4pCOOmedCkVUSp95wQax93ewwsgyWIeHlXorA9JR3Hsv95YG0ihP6TmlIQucF0IEkSXHI_U1d8iQmCznRMWKbVu4rJsCUCvv-doSmiiA68xU8MhTkzGNlDXTdixnxELh4VqAByiTOQEQPWVoI3U38dkV1__oQrDdizcLM-a2cF01zEuxJB-whNF-j6OSc6GKvjwbrT511WN7abHibaET-QWlgSLa2JjdJNQDfAlHeM5K-7SMcBqBlw25rGjIvmH19zdTREUTaLrW9SkYQGF1XxeNTyEvhxa80Csh59W-iXVO_0E_Kv_BwDIh5kN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قاليباف:
لقد تلقينا العديد من الرسائل من الدول المجاورة بشأن صياغة ترتيبات أمنية جديدة وتعاون اقتصادي في المنطقة.
‏لقد عرّضت الولايات المتحدة أمن كل حليف من حلفائها للخطر الشديد من خلال التنمر والتجاهل التام لمصالحهم من أجل إسرائيل لدرجة أنهم رأوا لفترة وجيزة وجودهم كله على المحك.
إن النظام المحلي المستقل هو ما سيحقق السلام والأمن فعلياً.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88310" target="_blank">📅 13:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88309">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaBitrCGN6u8wGTIjvXx3EUwa9FsZqYnBLbN2-rGBuzAbV5EGs9iJibBIyxPF65-aXZkJDUN1-3BPFIVI6w5kNV6oqDf789z7BG3Mk6cq7-5ECacNkw9_j1Wa2TjEaUIKvy7nsrQgo_x00qT9LbSBxn-tKkZ_qPc2-TP7yoiJQDcEEI4_BtatxvNX2i-DYxl7mQ9ySyGJhpCr9n21mqrhxanA4yeBZMGLoj-pdKlAgWfLj4KAvLYoTSgpBe-btf_T0-_qBSO6-LcX5iV2_pTvxvWfj8WpACYuKxS5jeJurGArMosqcnYcqbpkJ79cGi_4n_rQoDhe7uldp0MK1SjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇸🇾
جيش الاحتلال الإسرائيلي يستهدف عجلة بمسيرة في ريف العاصمة السورية دمشق؛ إصابة شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88309" target="_blank">📅 12:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88308">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇾🇪
🇸🇦
مرتزقة السعودية:
الهجمات الحوثية أثرت على ميناء المخا وحركة الملاحة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88308" target="_blank">📅 12:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88307">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
قائد لجنة البحث عن المفقودين الإيرانية:
الوضع الصحي للطيارين الإيرانيين في قطر ليس جيدًا.
مكان احتجاز الطيارين الإيرانيين في البحر لا يوفر الظروف المناسبة للحفاظ على صحتهم.
يجب على الحكومة القطرية نقل الأسرى الإيرانيين إلى اليابسة وإلى مستشفى مجهز في أقرب وقت ممكن.‏
ندعو الكويت إلى إجراء اتصال أولي بين الطيارين الإيرانيين وعائلاتهم.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88307" target="_blank">📅 11:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88305">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
رئيس الجمهورية: هنالك تسهيل لبعض البواخر التي تحمل النفط العراقي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88305" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88304">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
🇮🇷
مصادر إيرانية: إيران تسمح بعبور عدد من ناقلات النفط العراقية من مضيق هرمز بناء على طلب بغداد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88304" target="_blank">📅 11:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88303">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
مراقبون يگولون تغريدة " لخ " أخرى إذا صح التعبير من ابو مجاهد العساف والجماعة حتى باميا للمواطنين بفرحة الزهره يوزعون .
النجباء مسوين شده يا ورد وزيارات وكذا على قادة الإطار التنسيقي مرتاحين لشوفة العامري حتى واحد منهم گال جنه يم هادي الكعبي مو العامري .
خبر " فصيل مسلم أشياء للقوات المسلحة العراقية و الأمريكان كانوا حاضرين للمشاهدة خبر حقيقي  " .</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/88303" target="_blank">📅 11:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88302">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
لا توافق بالآراء حول حرب إيران وحل أزمتها داخل البيت الأبيض.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88302" target="_blank">📅 11:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88301">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
🇮🇷
مصادر إيرانية:
إيران تسمح بعبور عدد من ناقلات النفط العراقية من مضيق هرمز بناء على طلب بغداد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88301" target="_blank">📅 10:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88300">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
"توم باراك" بخصوص الشرق الأوسط:
أُرسل جميع الأنبياء إلى هذه المنطقة. ليس إلى منطقة البحر الكاريبي، ولا إلى أمريكا الجنوبية، ولا إلى أمريكا الشمالية. ‏"إذا لم يستطع الله نفسه حلها، وإذا لم يستطع الأنبياء حلها، فإن فكرة قدرتنا على حلها في العام ونصف العام القادمين تبدو ضئيلة للغاية."
توم باراك صار يكفر بعد فشله بحصر السلاح في لبنان والعراق واليمن وفتح مضيق هرمز
😆</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/88300" target="_blank">📅 01:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88299">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي وإنفجارات كبيرة تهز العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/88299" target="_blank">📅 01:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88298">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwlp1ZVUekuT2ueejpkMAcd3kQElt2yWWKFXMClH2odbQixpo7OSy2gRv1JW_wbDIlG8GpJqp-DHxFi4IUAaGzxFTXxR-1mcz_4jY6Frb5XlZxdOW8-JsMe7qLzzHHGLOQe8-DUoyPocB__yLUPZ-gA7lKbzCKay4BAGsI85E7_NnAg5pDm7v21OfEORJh0iUwMbUbavb5_e7djgmidkQniT-bToIEFst9Iqpr4fMlzsMS2UkA3bA4ChWaP8l6eMcpMIoTuhFfEn7XlhOJQO51LIp_7wt4KTG8EUf7kcIVQdNJTF8O2V_0CXn2l0Glz_O8zJHotIqL4ZVuMZF2vdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
طائرة مقاتلة من طراز إف-35 إيه لايتنينغ 2 تابعة لسلاح الجو الأمريكي تطلق نداء طوارئ على الرقم 7700 فوق الإمارات العربية المتحدة.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/88298" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88297">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e124a7b79c.mp4?token=CvX-Xun8XeUaloPdZnmdBtTkTfp2A4JQlGl7W3IQfQ0ZozpojTAkIUNrjSJ73ccd0dEhmHkMeTYn-2P5iMZKu0d4M0ZIY-iQeM0Qj1Qc63tRnb4iRN0ajiZ5HGB1YsYXTNvwalL4Tu7GvlcnEmqNu1spnb27XjhlBeYcRhLWfBXT1pte6fxvb6P48HnLGCGwOTsFJENQYiNWw23vMFwYHCFKKY6im4tnlhh_9TJGgjMZekJ63n5BOG4dXr8QOPHamuz2Mw54pNZW8RVgoi8I0zCkfmLFJ40ODy5NoBHvV09T6lpPBtkdcx_73TJWZ5XuL2shrAupAXZIIxUOAxS5Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e124a7b79c.mp4?token=CvX-Xun8XeUaloPdZnmdBtTkTfp2A4JQlGl7W3IQfQ0ZozpojTAkIUNrjSJ73ccd0dEhmHkMeTYn-2P5iMZKu0d4M0ZIY-iQeM0Qj1Qc63tRnb4iRN0ajiZ5HGB1YsYXTNvwalL4Tu7GvlcnEmqNu1spnb27XjhlBeYcRhLWfBXT1pte6fxvb6P48HnLGCGwOTsFJENQYiNWw23vMFwYHCFKKY6im4tnlhh_9TJGgjMZekJ63n5BOG4dXr8QOPHamuz2Mw54pNZW8RVgoi8I0zCkfmLFJ40ODy5NoBHvV09T6lpPBtkdcx_73TJWZ5XuL2shrAupAXZIIxUOAxS5Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:  إيران ترغب بشدة في إبرام صفقة لكنهم ليسوا مستعدين لإبرام الصفقة المناسبة.  لدينا سيطرة كاملة على تلك المنطقة بأكملها، وبالأخص فيما يتعلق بمضيق هرمز.  وهذا يعني سيطرتنا تمتد إلى عمق المنطقة، بما في ذلك المناطق البرية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88297" target="_blank">📅 00:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88296">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f648adb9.mp4?token=nzYBgLSyRVrtcaHq9a-HuNNfwfkN6Atnx0_ekSL6RndcQthoA3Sm7pZ7lgP2B4DQJxRTVRScHMnPiIXkzKA5LVrlr3yvSH6u7qLH_gEpThrt5Kxbwyp_KDEBh8-KMitb8qhUWsx1sxFgJVfK88cz4jrSkYAeL13CqOyBR6wFnoYiTYUwlj6b0Cj5w6JniblTS9ro5BRdkjJt_beDJV9KqYge1sfQcUdv-esVmpJSoj-PSH9z9OxgnsbkCyotVuf9-epgacuXrZvtBEvObKVOkNNsAh0smSv-OmcWJUc9YbCMM06PUFrBtjBn0kqPiypL1X-WPYdHKEILzIf0xtX_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f648adb9.mp4?token=nzYBgLSyRVrtcaHq9a-HuNNfwfkN6Atnx0_ekSL6RndcQthoA3Sm7pZ7lgP2B4DQJxRTVRScHMnPiIXkzKA5LVrlr3yvSH6u7qLH_gEpThrt5Kxbwyp_KDEBh8-KMitb8qhUWsx1sxFgJVfK88cz4jrSkYAeL13CqOyBR6wFnoYiTYUwlj6b0Cj5w6JniblTS9ro5BRdkjJt_beDJV9KqYge1sfQcUdv-esVmpJSoj-PSH9z9OxgnsbkCyotVuf9-epgacuXrZvtBEvObKVOkNNsAh0smSv-OmcWJUc9YbCMM06PUFrBtjBn0kqPiypL1X-WPYdHKEILzIf0xtX_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب:
إيران ترغب بشدة في إبرام صفقة لكنهم ليسوا مستعدين لإبرام الصفقة المناسبة.
لدينا سيطرة كاملة على تلك المنطقة بأكملها، وبالأخص فيما يتعلق بمضيق هرمز.
وهذا يعني سيطرتنا تمتد إلى عمق المنطقة، بما في ذلك المناطق البرية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/88296" target="_blank">📅 00:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88295">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyOQfOWsaJFyfzLtHeBGRrybiZ2uv09q3i5sgNr_uBiTJIJPasaMynbYqkrc3W-L6obyQubf4yzsvYtEyL_44CnHx2_KxKeC3OVP8Q5wdeGVZVybvJEFcZhZ4t_kLCzyhM9VN8-BMHXGe9RZ9iSo0-q3k-WbhvA5wLrPYBDM7-PzBis2Ql-w106GKHEXJCVuIYn2dZQ_m8EOzRM16A71pASDDptKyFjgRhPwQ5CrOObxXQd-une4HB6whqT1M-YpWfriDCOU7vPSQWDehXWFHuHHgS_DG7O9NfLstu8i8CFA3CKcBXPIvKYVfeGHuLeMHTOT5r0X8m512B6qeiLfrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
نحن ممتنون لقرار المحكمة العليا الأمريكية.
المجمع العسكري/قاعة الاحتفالات الذي يتم بناؤه على الأراضي المقدسة للبيت الأبيض، وهو أمر بالغ الأهمية للأمن القومي، سيكون الأفضل على الإطلاق!
إنه شيء طالما رغب فيه الرؤساء على مدار 150 عامًا، وهو ما سعى إليه الجيش خلال المئة عام الماضية. قريبًا سيتحقق هذا المطلب!
الأعمال الإنشائية تتم ضمن الميزانية المحددة وبوتيرة أسرع من المخطط. شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88295" target="_blank">📅 23:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88294">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1k0vvsOL04pWE_UvEQcEsvq1GZscMjUZsfnA0cSnnjcDnO6DuTHdYfGfmjmZ15Nsfnllyv-7FvSqp7EERWlUwRk33dx9EGDgG_2TgTXWSbWot_1enEZPLKCVBO2B-F_LITjk8in6wU2HHveL6m5R2D7Ja8vgKfc28Zp467JoWB-VK2chIBChNG8Y38C9nlK4eOlG7sg7eU3lnjAJ9FEkJFNu0FezWO2XFyM6m5shXJ81tVtSPnlL_oKUdWHmBeW9pfofERqUr82xqg2rxumVvpZvZkmLGYQjX816Ee3VKnoSP0Ry_i8-zZp9gQkXaHNympxhqEEvLehDbbS6XicAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
الطيران الحربي الإسرائيلي يشن غارات على مرتفعات علي الطاهر في جنوب لبنان.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88294" target="_blank">📅 23:09 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
