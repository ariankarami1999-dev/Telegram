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
<img src="https://cdn4.telesco.pe/file/ajqzmAZyv0eAVO8zOoL9F9vYE-v_k3-ToqIeHmNpSgYkK5cOGMTFYb9zkGJYdbLOSgySvo_NTpOHDJHLM2ct6CTxeltkpxwbuctqfVosjk762n1VR-URHauKY2cCsTDWnpc61gF_MIwHGBR_TZj-Is_pZ-mQwPekyiyripHvLzn7wstOCR-EB7oVqCmoDZuv91Z8LcmwLRnitxxrAbQS4QbGr7Y3G3MI4uUSDjbL6Jm94WfGkB3m3J0j8Wz0dcuNYHDtLqj25NK_Qyvqzhx4lmy_DGq8NOJc5Jnq5_Ia2GRMvsBpBLZYuhUsahgj4WliYVNhEicUxcS8wmYk3YpoYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 15:58:03</div>
<hr>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الاعلام الامريكي:
‏قبل صعودهم على متن طائرة الرئاسة الأمريكية "إير فورس وان" لمغادرة بكين، قام الوفد الأمريكي بأكمله بإلقاء كل ما قدمه لهم المضيفون الصينيون - من هدايا وشارات ودبابيس وأشياء تذكارية - في سلة المهملات الموجودة في الموقع. ‏لم يصعد على متن الطائرة أي شيء من أصل صيني. ‏كان الوفد قد ترك أجهزته الشخصية في المنزل واستخدم هواتف محمولة نظيفة طوال الرحلة.</div>
<div class="tg-footer">👁️ 508 · <a href="https://t.me/naya_foriraq/75438" target="_blank">📅 15:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سوالف الگهوة
وزير ادعوا " انه لم يصوت عليه البارحة سوف يعود بقوة القضاء العراقي المستقل ، العامري الزيدي ورجل معهم حكيم اجتمعوا البارحة عند المالكي ليلاً …</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/naya_foriraq/75437" target="_blank">📅 15:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5ac0cea1.mp4?token=s7D13QZDotFZ0b6cNolg1yQri5ViEg6HL0qZQE0sWk53aANV7wB6t6x5esFOzd0YfQYovPHIeKFRvmr2_YEyW6G1AsniLPW0nlvmJKEO03_m4u3Be0_N9jO5-VD3Fs5uSlb8aPWrY-JDglUm06TBOnO7n5iBq6ipaoST4MT_fLyRwpuXBNyBbk464QkuKSIL0m_IBx1bHa5cZg85887FBxt3BUuahGZKYruh_DuRjHzvRccHF9AGnx9fC5fvEnJ1eUvX3V1LTAvk3pLtboPX3ia9rb231AJyjnq_h3v6O9fDhCYQ18pn_ljey2oYjs1DVCdSHvCH2zyldHIt_C94Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5ac0cea1.mp4?token=s7D13QZDotFZ0b6cNolg1yQri5ViEg6HL0qZQE0sWk53aANV7wB6t6x5esFOzd0YfQYovPHIeKFRvmr2_YEyW6G1AsniLPW0nlvmJKEO03_m4u3Be0_N9jO5-VD3Fs5uSlb8aPWrY-JDglUm06TBOnO7n5iBq6ipaoST4MT_fLyRwpuXBNyBbk464QkuKSIL0m_IBx1bHa5cZg85887FBxt3BUuahGZKYruh_DuRjHzvRccHF9AGnx9fC5fvEnJ1eUvX3V1LTAvk3pLtboPX3ia9rb231AJyjnq_h3v6O9fDhCYQ18pn_ljey2oYjs1DVCdSHvCH2zyldHIt_C94Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يهاجم ‏مراسل بي بي سي بعد ان سأله عن القصف الامريكي الذي استهدف مدرسة ميناب الايرانية
‏
س: سُئل الأدميرال كوبر أمس عن الإضراب الذي استهدف مدرسة البنات--
‏ترامب: حسناً، الأمر قيد التحقيق
‏س: هل يمكنك تأكيد أنه صاروخ أمريكي؟
‏ترامب: مع من أنت؟
‏س: بي بي سي
‏ترامب: بي بي سي مزيفة. هل تقصد أولئك الذين وضعوا الذكاء الاصطناعي في فمي؟</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/naya_foriraq/75436" target="_blank">📅 15:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انسحاب الاسدي والغراوي رسميا من السوداني</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/75435" target="_blank">📅 15:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75434">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8eBLPkhCGJ_KG02S9O6HPOUVI4ijdZkUEalkhh5duwXXUqMsaudifOvT9dl4g5gutStCRxgIbs9jy4TyLqdEqpXzPrUjKBTYS-lsXs_Q9h1MmsN7bY1f4uXZBSISx8M78oTWL_UBJEB57F3BtAGIlz9uAtDqVurAusensA1yW1MLnT3-7U5kbqVVhZ2KjC4rr_vmm7HGTzkc5AI_iUA_indgdnI38r1crRj42dFDces-PErKHzSnATfnR0Xtc28DsvAw46ykS8WnMqDSbAwTyJ_4ew7tfeoxPDTO7zCRYR_2PhfPAJmkE4qkZLLtaWm-qbh6O6OulRegqYvOSzvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة   رسالة من ابو علي بوتين للعراق …</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/naya_foriraq/75434" target="_blank">📅 15:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAmUIuVP_mYZH0yHNcCiXoHvhgL04zJxzguK-klawmZh-lAHXxUjB0Mqp8B9hHFKbzwHEu_iLOJgjIJgerNL-yn1iBf-RHuVcdaKdyIpwranSVktD8fvZ8P3hPo0C_W3__Yy7Rpdo2bqs2xZyLjIGr3cW_AXgY37dfReUP3m8EadFmV_Jq1KkibFq2lf2ggxLd6q13VwA4rZke14kCaQ4-B2Wm_f1pd_4n8g-J92ZnUyVYfBvwmhrGarTOXzSI3tUMsyKKXTRNV_ZE-ZE9dJUvIP3Bsk3OvZFKdXvl18u1NMyqDrM_sh_6QMvki6oPw5pBSjMLvzyK5exuHLKssGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني:
إن مقاومة إيران للتنمر الأمريكي ليست معركة غريبة. فكثير منا يواجه أشكالاً مختلفة من نفس الإكراه البغيض. لقد آن الأوان لنا أن نتكاتف ونعمل معاً على توضيح أن هذه الممارسات يجب أن تُطوى صفحتها إلى الأبد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/naya_foriraq/75433" target="_blank">📅 15:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سوالف الگهوة
رسالة من ابو علي بوتين للعراق …</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/naya_foriraq/75432" target="_blank">📅 15:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏ترامب: لقد أجريت اتصالات مع كيم جونغ أون، زعيم كوريا الشمالية</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/naya_foriraq/75431" target="_blank">📅 14:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏ترامب: سأتخذ قراراً خلال الأيام القليلة المقبلة بشأن رفع العقوبات المفروضة على شركات النفط الصينية التي تشتري النفط الإيراني.</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/75430" target="_blank">📅 14:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏ترامب: "الغبار النووي" الإيراني قد يُسلّم إلى الصين أو الولايات المتحدة</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/75429" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامب: آخر ما نحتاجه الآن هو الحرب.</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/naya_foriraq/75428" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏ترامب: لا امانع في تعليق إيران لبرنامجها النووي لمدة 20 عاماً، لكن يجب أن يكون ذلك التزاماً حقيقياً</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/naya_foriraq/75427" target="_blank">📅 14:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/naya_foriraq/75426" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0nW9BlNazG6KIjgOTRr2xXlFSoOvySL1cjYxgSmtIpZvFxlFTF8q14Br_qAVVrz2fGvOeMuw81r1e9ef5Ii2nO_ZpPrvXTonvarvEw4ZO-VD1YLQwKgJ_dqmKLjLen8d595cZR8gXN2Ng2F_jLfoqUGu72rtED57Phh43aYr7K3D6Db7mEms9DNImeXZKcymfnnyYmJh6pTqxhSui80iVykScCKJCtmBZ0sPHlkLG5bIDIGCQsTiWnlMrMekFLmcewl3B0SifTozIwhcoFrcmFJO6waDh9Uqf-NzlgOEYgwSajk4fk3xgAaIgcSQLfCOusxPvAoFGf_Bt09oLU1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/75425" target="_blank">📅 14:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامب: لم أقدم أي تعهد بشأن تايوان.</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/naya_foriraq/75424" target="_blank">📅 14:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75423">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامب للصحفيين: لا أعتقد أن هناك خلافًا مع الصين بشأن تايوان</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/75423" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75422">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامب بعد اختتام زيارته للصين يقول لفوكس نيوز حول تايوان: لا نتطلع إلى خوض حروب</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/naya_foriraq/75422" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75421">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامب بعد اختتام زيارته للصين يقول لفوكس نيوز حول تايوان: لا نتطلع إلى خوض حروب</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/naya_foriraq/75421" target="_blank">📅 14:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏بيان لقائد الثورة الاسلامية آية الله السيد مجتبى خامنئي بعد قليل</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/75420" target="_blank">📅 14:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75419">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdWlwitBtJG-IdsKZSs0WB9ETNZjpGvVEyW2-Oz56moHJiAS5_RVPbtcefcFCN2Z1brxkGN0JdDQk6Z87YGKKheq95zv94HQ7cKLZM7pUaj1NQ8oTXqVLWRL_axMoApjSHy8FlO3b-5B7lp29q27g3jofWbJD8_y3SrXeYeFhDR8PH2Y02pHWMH-7cRgwPfmbnkakvEFTzHwV1AtRSY3cZQIaADaSU4o4N5KPHupzndVBuU_Mp5Up8Ysa8ZVj_EYLtUymrXxu_le6bdQq421nSpMZH0FXawqAW6s5YKP7CGUZY7lN2mTMe3xWeyd3RXtblAQJBHbdYnTRT_b_HzWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب: ‏الصين لديها قاعة رقص، ويجب أن يكون لدى الولايات المتحدة الأمريكية قاعة مماثلة! إنها قيد الإنشاء، وتسير بوتيرة أسرع من المخطط لها، ‏من المقرر افتتاحها في سبتمبر من عام 2028 تقريباً. الرجل الذي أسير معه هو الرئيس شي جين بينغ، رئيس الصين، أحد أعظم قادة العالم!</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/75419" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75418">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏بيان لقائد الثورة الاسلامية آية الله السيد مجتبى خامنئي بعد قليل</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/75418" target="_blank">📅 13:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75417">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlZdEhmheSIb1FgYwMKQCVSmarWfUu4U9t0z7zzVE6yA0L31fYNp7MB9fZiRksESQ3nhkptWUV4Qjdgq8HpgUkgQg4xQhDWvuPX3oHhXjZPG109iNbcG7WuBn_Bsl5GT30zlkzDEU9L2bS1FC3mDVHdU7AurTlKBr5yzI7K_P-p1BuaBwIV93iD7RJMDIdKTbGQy3v0db1tjVWLQknhLfA7n6OF3d1MtKOYqVLkBSarPmNGowtnElcl4zPF8ldQtW-4W4lMwtEXu5-OAIy1FuLy0gMJzDYv0qtvEf2c1aSAkFE7w3hTnTIsqfBzlJgxJaswG5Al2TG1ANASPxPvsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
الرئيس الايراني مسعود بزشكيان يهنئ رئيس الوزراء العراقي بمناسبة نيل الحكومة ثقة البرلمان</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/75417" target="_blank">📅 13:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني:
- وقف إطلاق النار هش للغاية
- لا يوجد حل عسكري فيما يتعلق بأي شيء له علاقة بإيران
‏- نحن مهتمون بالتفاوض فقط إذا كان الطرف الآخر جاداً
- لا‏ نثق بالأمريكيين
- نحن لا نريد أسلحة نووية، وهذه ليست سياستنا، لدينا برنامج نووي سلمي
‏- يُسمح لجميع السفن بالمرور عبر مضيق هرمز باستثناء السفن التي تخوض حربًا مع الولايات المتحدة
‏- إيران مهتمة بمواصلة أعمال الطاقة والنفط مع الهند
‏- اتفق مع الولايات المتحدة على تأجيل المفاوضات بشأن المواد المخصبة
- الرسائل المتناقضة جعلتنا مترددين بشأن النوايا الحقيقية للأمريكيين في المفاوضات</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/75416" target="_blank">📅 13:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">استهداف دبابة صهيونية في بلدة رشاف جنوب لبنان بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/75415" target="_blank">📅 13:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بلومبرغ:
الإمارات حاولت عبثاً حثّ السعوديين على تنسيق الرد على إيران لكنها شعرت بالإحباط عندما قوبل طلبها بالرفض
في حين سارع محمد بن زايد إلى التعاون مع إدارة ترامب والإسرائيليين أبلغه نظراؤه الخليجيون أن هذه ليست حربهم
الإمارات نفذت هجمات محدودة ضد إيران من دون دعم من دول الخليج بدءاً من أوائل مارس ومرة أخرى في أبريل</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/75414" target="_blank">📅 12:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 تجمّعات لجنود جيش العدو الإسرائيلي في جنوب لبنان بالصواريخ والمسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/75413" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b1df4d5.mp4?token=GDAZXT7ZOe0shwLSImQzqDwdDqwqcyMdWmJ1FQ9RAaBFO1b7hZM8o5W8hrxd4mDYd8TBMmIs1u4ajNLNHq27_HU6BSHip6PVm2G8uWnUt-Kp4dFELmjt2qMOvNrIo0YjoDbPCvjI3coBexieT3ultxT5nXqzZj_dEQRVhwhaouT6ATsSOGr1vcBcWbEF92BCf9czmG7CqbD0XMRwE_tZfpBfHPBqJLU2KL2RjFFIt06hoas1rutWqj1R17L7SexpXfPJJSbRRz1FSpYW_QYxVpdL02SEWTe5fpIajGHR8am9JoKf-E3OTV_vdemjB838yqnvxtKnp3i8ASP7kbu6QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b1df4d5.mp4?token=GDAZXT7ZOe0shwLSImQzqDwdDqwqcyMdWmJ1FQ9RAaBFO1b7hZM8o5W8hrxd4mDYd8TBMmIs1u4ajNLNHq27_HU6BSHip6PVm2G8uWnUt-Kp4dFELmjt2qMOvNrIo0YjoDbPCvjI3coBexieT3ultxT5nXqzZj_dEQRVhwhaouT6ATsSOGr1vcBcWbEF92BCf9czmG7CqbD0XMRwE_tZfpBfHPBqJLU2KL2RjFFIt06hoas1rutWqj1R17L7SexpXfPJJSbRRz1FSpYW_QYxVpdL02SEWTe5fpIajGHR8am9JoKf-E3OTV_vdemjB838yqnvxtKnp3i8ASP7kbu6QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالمسيرات يستهدف مقرات حزب الحرية الإرهابي في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/75411" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e67fea4.mp4?token=LscT4Y7T-tw7tg3dX4YyIqJ7HsPMHqkbYPBrBajZ2bMTxLW4VnoAh5fHDCCwvOzHC34ilx488lCjgiXyF-8XX8pfy4RaZF4OxTi4GMbn_4o4UUR9nCqEB-kIfa14ou4jd0f5LZZPgLwFbQx_V6pXfC96cAplouut9YJMNx_f2jL20j8rw-8mpeB3osB6yYfF3lVzKstZF09fSLWDhLRcMHBGPnbOs4h7Vtqc9IavhuS1j23jQ0WhvDkB6IubMGvoZFUiJzWIYvDDf8qm_CQq3y0LdWoEHtEOKbScrwf79mQkRUxfzb4Dk-KiedAjjZXcGL228uEpQGMClp_-AmEsmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e67fea4.mp4?token=LscT4Y7T-tw7tg3dX4YyIqJ7HsPMHqkbYPBrBajZ2bMTxLW4VnoAh5fHDCCwvOzHC34ilx488lCjgiXyF-8XX8pfy4RaZF4OxTi4GMbn_4o4UUR9nCqEB-kIfa14ou4jd0f5LZZPgLwFbQx_V6pXfC96cAplouut9YJMNx_f2jL20j8rw-8mpeB3osB6yYfF3lVzKstZF09fSLWDhLRcMHBGPnbOs4h7Vtqc9IavhuS1j23jQ0WhvDkB6IubMGvoZFUiJzWIYvDDf8qm_CQq3y0LdWoEHtEOKbScrwf79mQkRUxfzb4Dk-KiedAjjZXcGL228uEpQGMClp_-AmEsmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالمسيرات يستهدف مقرات حزب الحرية الإرهابي في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75410" target="_blank">📅 11:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: هذا هو الوقت الذي يجب فيه على إيران أن تثبت موقعها وتبرز دورها الإقليمي أكثر من أي وقت مضى</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75409" target="_blank">📅 10:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8ecb192c7.mp4?token=ojhIhLfzGXP7G6iqg3oClIyCxh4y9dgozOFzTWzIa_01x1EA4R9fitUVDPZ-Zzp8tmFBvXQVMmeQyv5Zq4wo6X3PQJ-i3ORZ84_2NT8tS-1S8uwq1qE3yMjUGnqdLlXAGQAJ2ve1oz9iiUbdjijbNhgT8B3HwwR8ZAV4ZULg2QD1YZW0M1NjGCFFqC9aoIDFJbv4ROFAIPBEUutIvDIq74HlFpUuzBT2L9r1ZHwVdgoKYP5fRv0m1zzInVTpG_AoOPRgmLltsfUladrqxmw-TcEb2cDwvKWdss5Wzim_YvBPuDXV-g3l6tCX5aThGLo2nXSUr_BAZ6dutsh9oJdxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8ecb192c7.mp4?token=ojhIhLfzGXP7G6iqg3oClIyCxh4y9dgozOFzTWzIa_01x1EA4R9fitUVDPZ-Zzp8tmFBvXQVMmeQyv5Zq4wo6X3PQJ-i3ORZ84_2NT8tS-1S8uwq1qE3yMjUGnqdLlXAGQAJ2ve1oz9iiUbdjijbNhgT8B3HwwR8ZAV4ZULg2QD1YZW0M1NjGCFFqC9aoIDFJbv4ROFAIPBEUutIvDIq74HlFpUuzBT2L9r1ZHwVdgoKYP5fRv0m1zzInVTpG_AoOPRgmLltsfUladrqxmw-TcEb2cDwvKWdss5Wzim_YvBPuDXV-g3l6tCX5aThGLo2nXSUr_BAZ6dutsh9oJdxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
🇮🇷
قائد القيادة المركزية الأمريكية
قال امس في مجلس الشيوخ " رئيس الوزراء العراقي الجديد تعهد لنا بإبعاد نفسه عنّ ايران "</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75408" target="_blank">📅 10:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av34mI9wSoWnf5qRORFOumbDo4LR1PysNsArZyGvfFOP0TCUQrY0jJs0GLFdMN-teVu7xaE9OyeOtIsaJlZi836r1jgbLQTDdhnrvmw600GzAXjS94GB2AcJZTN9nYq7GTBNBZzLuQ3CGt35kp2nZHymFemmZiScMyn1nLi350mi_V1JGhemDjAyLsAscH_tBMdFcsh6LqZiYj5xGYk5JoaQy0XIdPUp_ll7g1X9L1gtg5CKYDoKDfQ8cESYPBR-c_ubJ4SFvAS2UrGF4eoMtMhlEU4tGz8gFi7T1PyycQSEZr9EjbRErJEN9u-mm7qku_C5ynjAW-815--pJnNdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب
عندما أشار الرئيس شي بأناقة شديدة إلى الولايات المتحدة على أنها ربما تكون دولة متراجعة، كان يشير إلى الضرر الهائل الذي عانى منه بلدنا خلال السنوات الأربع لجو بايدن النائم وإدارة بايدن، وعلى هذا الصعيد، كان على حق 100٪. عانى بلدنا بشكل لا يُقاس من حدود مفتوحة، وضرائب مرتفعة، والجنسانية للجميع، والرجال في الرياضات النسائية، وDEI، وصفقات تجارية فظيعة، وجريمة متفشية، وأكثر من ذلك بكثير!
لم يكن يشير الرئيس شي إلى الارتفاع المذهل الذي أظهرته الولايات المتحدة للعالم خلال 16 شهرًا مذهلة من إدارة ترامب، والتي تشمل أسواق الأسهم والـ 401K في أعلى مستوياتها على الإطلاق، والانتصار العسكري في فنزويلا، والتدمير العسكري لإيران (سيستمر!) - أقوى جيش على الأرض إلى حد بعيد، وقوة اقتصادية كبيرة مرة أخرى، مع استثمار 18 تريليون دولارًا أمريكيًا في الولايات المتحدة من قبل الآخرين، وأفضل سوق عمل في التاريخ الأمريكي، مع عدد أكبر من الأشخاص الذين يعملون في الولايات المتحدة الآن من أي وقت مضى، وإنهاء DEI المدمر للبلاد، وأشياء أخرى كثيرة سيكون من المستحيل سردها بسهولة. في الواقع، هنأني الرئيس شي على العديد من النجاحات الهائلة في مثل هذه الفترة القصيرة.
قبل عامين، كنا في الواقع دولةً متراجعة. وعلى هذا، أنا أتفق تمامًا مع الرئيس شي! لكن الآن، الولايات المتحدة هي الدولة الأكثر سخونة في أي مكان في العالم، ونأمل أن تكون علاقتنا مع الصين أقوى وأفضل من أي وقت مضى!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75406" target="_blank">📅 01:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c66844eb9.mp4?token=hGP7Ny632TXm3Ud6ly5keUXxLaRMEKbUKjbp6E97NFPObNXNNcceDIG_3rylVD3zXLj2q1eU2SPaLf6SrEdNC3fYOUTbF56I6bqOA8EczUo7hf0t0h9J32XRnp2Zj9M10Ad7cem6Dk3sljxBz_iFkkObfiT0Ex5aLvY_f0J3TIoOeox2t1LtNc9JyffnUMmyYHgBM9n2ttmtjh2aOBYlF4PXe5R3GixSBeCZjjxYZJT_YPS_tHFCijhDJhmATHDCjNPoSloxayWi9nh4vkV-UONaEoIYn5iYVl9Tqqo8RQFtQmgoFbNP8tO53vF_EAowg6fkpWtxgWk0Yapobyalvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c66844eb9.mp4?token=hGP7Ny632TXm3Ud6ly5keUXxLaRMEKbUKjbp6E97NFPObNXNNcceDIG_3rylVD3zXLj2q1eU2SPaLf6SrEdNC3fYOUTbF56I6bqOA8EczUo7hf0t0h9J32XRnp2Zj9M10Ad7cem6Dk3sljxBz_iFkkObfiT0Ex5aLvY_f0J3TIoOeox2t1LtNc9JyffnUMmyYHgBM9n2ttmtjh2aOBYlF4PXe5R3GixSBeCZjjxYZJT_YPS_tHFCijhDJhmATHDCjNPoSloxayWi9nh4vkV-UONaEoIYn5iYVl9Tqqo8RQFtQmgoFbNP8tO53vF_EAowg6fkpWtxgWk0Yapobyalvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من داخل مقر رئاسة الوزراء في ليبيا، عقب اشتباكات عنيفة بين مشجعي أحد الأندية الرياضية امتدت إلى محيط المقر الحكومي.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75405" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75404" target="_blank">📅 00:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75403">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي يهنئ بتشكيل الحكومة العراقية الجديدة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75403" target="_blank">📅 00:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/75402" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75401">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY_1KfQFVnVPeLuKIBMepibmfyxwRL7Me81jwvwk7mYRLV-hBR9FD6VxVDTp-W_VI_8CXj3ta8H90U1RjKkpzyke74s7yuyIj3LVLpRzapz2jRHp0aBYY5mtpSuu2dZK8Iq3jYqAeQ4p42V0A7pfXxSvZOM9CKr1oCcA0AAapNW0ElM7xdKwGzHRQSj47OiGpiSLurCbE0PE5SJJ8xV0GVnM8bQ1dPAiKw6ijyz_E4gbSOBCIMWzDeGOt_5uGWQIrPyshxzZANOK-d4_JptjhyQm-dYIhDwFdwYJaLlAxVIs89cdfLHxpI0Txq0GyQ4rCZQUqa_DlbzrhF4wu08Wew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75401" target="_blank">📅 23:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75400" target="_blank">📅 23:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROZfHazcKFWN90ZUdZBd47KyoKddor-REkiPdxbxviNS0W9w6HvsBXWcBsiO-GkPDd93kge6jf3g6LexglMiYTzvFV5bcCXxwrI3lIetq-78cS89kpyJ9XRWp1-tMw8a4pCRL51Yp3vCtR5rm8ygQGg0wGf-pSTZiEZhqqOwy5leUDZtcgVlkhgnNFwZ4j-UV4AYCImZt3732M0pYBBYscTarwqG0IarcIN7ED7hVWf1JXWQw26rbTmGhImn_40cAzipoDIW0WGXDbVcsKuZFHmzkpP74k2zbMzMpdKoalwYiY9gY_nURJyPoMRhccEtkmZ2UpB9xYmnuDSI6mczcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
إذن أنت تمول هيغسيث مقدم البرامج التلفزيونية الفاشل، بمعدلات لم يسمع بها أحد منذ عام 2007، حتى يتمكن من تقمص دور وزير الحرب في فناء منزلنا الخلفي في هرمز؟
هل تعلم ما هو أكثر جنوناً من 39 تريليون دولار من الديون ؟ دفع علاوة ما قبل الأزمة المالية العالمية لتمويل لعبة تقمص أدوار حية، وكل ما ستحصل عليه هو أزمة مالية عالمية جديدة تماماً</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75399" target="_blank">📅 23:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75398">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">#سمح_بالنشر
.. مشاهد من إستهداف أبطال المقاومة الإسلامية في العراق
#رجال_البأس_الشديد
أهداف حساسة في عمق
الكيان الصهيوني
الغاصب
بعدد من الطائرات المسيرة حيث حققت إصابات دقيقة ومباشرة .</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75398" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc00397ad.mp4?token=XohqRHHwm_jwyFcOeHDXaho3yL3pCXUGprBUtOARJX7hRJkFzrftKkBJIS9Eb-F0c2FKo2hO6DSl5RY4OwXC3DKyhktl42g5K2kMmpC0JOvsTyLGXuzTiAUXfThhsi51GjkNcnOGYNZTjsGMvpG1MxcD-dyXolzO4xjT0hA1eqKHU0my20QH95Y_zbxESdJgR5sVdJ81dlZW-rJjqAXKGWnT8-7sWIkDlv7Vo7ZM4VAY5RyM4LGdBzQ5DWhxYrlXW_10Zvz3uMRfGRJFwFXaDOkDZoG1eoxLWxVtiwEdX_sTN1-XC2TGkWrj-Ieh0FCCfYAnHbuZsnReRtEtVzmbLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc00397ad.mp4?token=XohqRHHwm_jwyFcOeHDXaho3yL3pCXUGprBUtOARJX7hRJkFzrftKkBJIS9Eb-F0c2FKo2hO6DSl5RY4OwXC3DKyhktl42g5K2kMmpC0JOvsTyLGXuzTiAUXfThhsi51GjkNcnOGYNZTjsGMvpG1MxcD-dyXolzO4xjT0hA1eqKHU0my20QH95Y_zbxESdJgR5sVdJ81dlZW-rJjqAXKGWnT8-7sWIkDlv7Vo7ZM4VAY5RyM4LGdBzQ5DWhxYrlXW_10Zvz3uMRfGRJFwFXaDOkDZoG1eoxLWxVtiwEdX_sTN1-XC2TGkWrj-Ieh0FCCfYAnHbuZsnReRtEtVzmbLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق رشقات صاروخية من لبنان نحو كريات شمونة ومحيطها في الشمال الفلسطيني المحتل والدفاعات الصهيونية تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75396" target="_blank">📅 22:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87449a5631.mp4?token=rnXubakQhk5XFI4ZFJxHFMLHnDHbHoUHiQ9Gbsp8Nw5uEsTXVk3Ow1csTsyD-vyt0BqU2LNnq1HvMnxe77kScxphbb_0MfbLmTJ0xD6H1-_eOJ7WNCRS7k_uA667VJZlBBXFdCjAw61L93zYZK4Zi8umjoeaZ9a9bvn45ZZ3RP4ZdG5INQOMSuK2mVw1Bg4gazZ3i5rL3A2Oz9ZIXU4a2vXWsk-L88Nlg6XEACyhJQVnSh9-rf50Bla19dQ48QkT6hgBSm12ZtjQMQsSV1aS8IyCSHd8EHJpZmmzucAgXptKHtUsVzHxDJqZwM9sKFqXfwQtt6dieoa8GBUW3xkZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87449a5631.mp4?token=rnXubakQhk5XFI4ZFJxHFMLHnDHbHoUHiQ9Gbsp8Nw5uEsTXVk3Ow1csTsyD-vyt0BqU2LNnq1HvMnxe77kScxphbb_0MfbLmTJ0xD6H1-_eOJ7WNCRS7k_uA667VJZlBBXFdCjAw61L93zYZK4Zi8umjoeaZ9a9bvn45ZZ3RP4ZdG5INQOMSuK2mVw1Bg4gazZ3i5rL3A2Oz9ZIXU4a2vXWsk-L88Nlg6XEACyhJQVnSh9-rf50Bla19dQ48QkT6hgBSm12ZtjQMQsSV1aS8IyCSHd8EHJpZmmzucAgXptKHtUsVzHxDJqZwM9sKFqXfwQtt6dieoa8GBUW3xkZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
قصف صهيوني بالقنابل الفسفورية على بلدة على الطاهر في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75395" target="_blank">📅 22:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مصدر لنايا
يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75394" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
عضو لجنة الأمن القومي في البرلمان الإيراني "خضريان":
لا ينبغي للكويت أن تنسى أنها سقطت في يد صدام حسين في غضون 90 دقيقة فقط، وعليها أن تدرك حدودها اليوم، وأن الجمهورية الإسلامية قوية للغاية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75393" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75392">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceda60f73b.mp4?token=pN__PkPTqYNSOESzWBdz9EPQqIN3gCn6xLg4ljmZYio7IT-W9ZKNaTRPCdDoS8pNwHIj_C4H6Gfn0yUrxuhUX2NaG1NPaVma18xY-hjJk4prK4abIq3P1GypTFc-oBQ5HvgGCpz3PExEbAD7eb_oc6wALfXp0-lkvV7QbCAnM1oUM3ACRTtTelMuEeDzA9lbGVsQbysPCOvo7x_P1TELk2iKfu8Hw_ry_MnkS74dLI9v-rtx7xm53Vxtn3ORXZNFCckXk1wZtwRxlqLwpewEhcbVzPxrMHOUKxvyuZwY-xtzDw51eeKK6yjw74aE5fRFDqPPlNeeTY5siGUTtGrdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceda60f73b.mp4?token=pN__PkPTqYNSOESzWBdz9EPQqIN3gCn6xLg4ljmZYio7IT-W9ZKNaTRPCdDoS8pNwHIj_C4H6Gfn0yUrxuhUX2NaG1NPaVma18xY-hjJk4prK4abIq3P1GypTFc-oBQ5HvgGCpz3PExEbAD7eb_oc6wALfXp0-lkvV7QbCAnM1oUM3ACRTtTelMuEeDzA9lbGVsQbysPCOvo7x_P1TELk2iKfu8Hw_ry_MnkS74dLI9v-rtx7xm53Vxtn3ORXZNFCckXk1wZtwRxlqLwpewEhcbVzPxrMHOUKxvyuZwY-xtzDw51eeKK6yjw74aE5fRFDqPPlNeeTY5siGUTtGrdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قيادة العمليات المشتركة:
تم رصد تحركات لعنصر إرهابي خطر ضمن قاطع المسؤولية. و​بعد تحديد الهدف بدقة متناهية، نفذت قيادة طيران الجيش ضربة جوية ناجحة بواسطة الطائرة المسيرة المسلحة (CH5)، مستهدفةً الموقع المرصود في وادي الشاي ضمن قاطع قيادة عمليات كركوك ، إذ تم ​تدمير الوكر الإرهابي بالكامل وقتل العنصر الإرهابي المستهدف.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75392" target="_blank">📅 22:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">يسقط حمد
دعوة لنصرة الشعب البحريني المجاهد .</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75391" target="_blank">📅 22:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سوالف الگهوة   العامري منزعج جدا ؛ ويفكر جديا بسحب وزرائه من الحكومة بسبب مهزلة اليوم في البرلمان …</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75390" target="_blank">📅 21:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سوالف الگهوة
العامري منزعج جدا ؛ ويفكر جديا بسحب وزرائه من الحكومة بسبب مهزلة اليوم في البرلمان …</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75389" target="_blank">📅 21:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287f8d0310.mp4?token=ULs77ergXU3uAt2WoGf7SzAOYFy6fAgthEpO6psJBGyd45PshFDZeI0yezmleldYcS_JObHAyyXeXm1UgFBmCwHeQE2ONllnBYoI2_z-FWLGX5Nc8H8qGE-UF24hwdxPptyFKiXXsPseYME95uA0IvJuVGBSVjsnbhGS0Xa7rWrgbgu8J2RYLwcPEAO5q1URColGZvHpKfAmSu_P_ItL4fcVv07YPlmRrdooTW4hOiJ-yYUKq2dxrfbyzXqx95Sc8Bhc-HQfVibs9dQDL2B17_ur7sQY-WVSytae9-V3Mgo7IRdFdLrgqMxCnGSfdZMsKgWKbc3DfRgJaBWu0wJlQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287f8d0310.mp4?token=ULs77ergXU3uAt2WoGf7SzAOYFy6fAgthEpO6psJBGyd45PshFDZeI0yezmleldYcS_JObHAyyXeXm1UgFBmCwHeQE2ONllnBYoI2_z-FWLGX5Nc8H8qGE-UF24hwdxPptyFKiXXsPseYME95uA0IvJuVGBSVjsnbhGS0Xa7rWrgbgu8J2RYLwcPEAO5q1URColGZvHpKfAmSu_P_ItL4fcVv07YPlmRrdooTW4hOiJ-yYUKq2dxrfbyzXqx95Sc8Bhc-HQfVibs9dQDL2B17_ur7sQY-WVSytae9-V3Mgo7IRdFdLrgqMxCnGSfdZMsKgWKbc3DfRgJaBWu0wJlQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
القناة 12 العبرية عن مصدر: إسرائيل ترفع حالة التأهب إلى الذروة استعدادا لاحتمال تجدد حرب إيران بعد عودة ترمب من الصين.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75388" target="_blank">📅 21:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بولندا تعلن عن تسجيل أول زواج مثلي لها يوم الخميس، بعد أحكام المحاكم الأوروبية والبولندية التي تتطلب الاعتراف بالزواجات المثلية التي تتم في الخارج.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75387" target="_blank">📅 21:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
النتن ياهو: نقول للعالم أجمع إن القدس ستظل عاصمتنا الأبدية والتاريخية.
‏أبعدنا خطرا وجوديا يتمثل في القنابل النووية والصواريخ الباليستية الإيرانية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75386" target="_blank">📅 21:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf0bEVNf6IFY1Zv6OUM0TUQvR96Hxz0l_y7p0Jxr8q8Sv-UHjzQyTuV-q-9j2GeaVFE_OquuudGCWv11bdiAdHzd3XhgrMDa9bpjV-p-9UH7qHY3Nujjruv2lSyEnFhhcJ1xlliIyEJpolQINW9r45CBIfJQrJi5Z9Idr8I705QPCNSwTJih1Ipt_m_L6x9J42joUG9n4g1fTthVhphJpyrLX5ULWwOTgsDcrMNyBmytN_nmgoIpvOX8JPm_vURtdRipE_mWIuektwMmPPlh3EqJGbuE3dUyd3Ct6UmWMF12doAKKFEIp6x0emtb8KX_bxZsb2DJJX76UJjN9-g3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي يهنئ بتشكيل الحكومة العراقية الجديدة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75385" target="_blank">📅 21:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
القناة 12 العبرية عن مصدر:
إسرائيل ترفع حالة التأهب إلى الذروة استعدادا لاحتمال تجدد حرب إيران بعد عودة ترمب من الصين.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75384" target="_blank">📅 20:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال:
إصابة 4 جنود في رأس الناقورة جراء استهدافهم بطائرة مسيرة إطلقت من لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75383" target="_blank">📅 20:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75382">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
بعد عدم نيلهم ثقة مجلس النواب.. توثيق يظهر لحظة إندلاع توتر واشتباك بين عدد من نواب الكتل السياسية في البرلمان العراقي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75382" target="_blank">📅 19:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75381">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b2948510.mp4?token=udSfF-CtgIhMRh_L_I9euqq7kkh7hWMOWELvbkuMQmqL8VfNUoFNxxnEbYttg9L_vZ7JyfFy3LMkAELAvLuzcj6AkumRgbCPKBq6heUXkqPB8VC9E5l9rwwsI-NAAoWv1zIG2UkgqsrEoIx-YGU6ABDmJaMB4PCa5pkWq8wn2cnJMG3zHQTvrjItkG4GinURK9PUdGoJiu2bywY8Ee09dxQJzUwGvA9xKhuW_afsDK7HxKqozLJZCKHCnA7bizHdw9csTb0bUG9S5zBmbDUBbzAyGE3XWtlYcQ6rW2KlNC1YftSTl7XyGVIj8DPHbx-QzViz7HmKwiKdL9NLXu-jFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b2948510.mp4?token=udSfF-CtgIhMRh_L_I9euqq7kkh7hWMOWELvbkuMQmqL8VfNUoFNxxnEbYttg9L_vZ7JyfFy3LMkAELAvLuzcj6AkumRgbCPKBq6heUXkqPB8VC9E5l9rwwsI-NAAoWv1zIG2UkgqsrEoIx-YGU6ABDmJaMB4PCa5pkWq8wn2cnJMG3zHQTvrjItkG4GinURK9PUdGoJiu2bywY8Ee09dxQJzUwGvA9xKhuW_afsDK7HxKqozLJZCKHCnA7bizHdw9csTb0bUG9S5zBmbDUBbzAyGE3XWtlYcQ6rW2KlNC1YftSTl7XyGVIj8DPHbx-QzViz7HmKwiKdL9NLXu-jFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توترات بين الأحزاب السنية بشأن الثقة بأحد الأسم المطروحة لإحدى الوزارات.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75381" target="_blank">📅 19:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75380">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئيس مجلس النواب يدعو رئيس مجلس الوزراء علي فالح الزيدي والوزراء المصوت عليهم لأداء اليمين الدستورية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75380" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75379">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5223d3a624.mp4?token=t_aRgHP2CcyjBHfxJsNZ_M4kJQ4vfFZYqX0HdVEwSWr7OiVcRh_s9bgtqpIO7Ag1JLw6wZKEQgeGRdboqkOvSg6qFd__-aLouqjCBlTm7CcP2fVhTr43gYTmA5znuN0sJLuUvWSMyz2mmy3Pl8aM41BYWzg1FsDjNFN8FYApAmjNF9_Aav8zj1XviX9suZFXQf1SQDGXIHVhz677YSn77DPKunhJimVfwi7M6IAR66YjejfuCGbANgxDYhFvRHAg0FNNvwKEkmMFjc0vCa8FzZz7lumwUCLPSutd8HH5hEaL_BSSI0oArGb0l4h7LHFpzSBaMz1DlPFiEvf7PW4lQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5223d3a624.mp4?token=t_aRgHP2CcyjBHfxJsNZ_M4kJQ4vfFZYqX0HdVEwSWr7OiVcRh_s9bgtqpIO7Ag1JLw6wZKEQgeGRdboqkOvSg6qFd__-aLouqjCBlTm7CcP2fVhTr43gYTmA5znuN0sJLuUvWSMyz2mmy3Pl8aM41BYWzg1FsDjNFN8FYApAmjNF9_Aav8zj1XviX9suZFXQf1SQDGXIHVhz677YSn77DPKunhJimVfwi7M6IAR66YjejfuCGbANgxDYhFvRHAg0FNNvwKEkmMFjc0vCa8FzZz7lumwUCLPSutd8HH5hEaL_BSSI0oArGb0l4h7LHFpzSBaMz1DlPFiEvf7PW4lQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75379" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">توترات بين الأحزاب السنية بشأن الثقة بأحد الأسم المطروحة لإحدى الوزارات.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75378" target="_blank">📅 19:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642dd7275.mp4?token=IyE_Jsm_P7SnXOeZP7S3p8PQnoHUTGh2nmRdcnHKEUEvlW_wGs6-sBZ4Dv2JPiIjQFpHOYoozQZGUFbAIWqosUflN7DqgrpGyx3xYuqZyMRTkv28B-_l9ySDRiwXHmW7DY0iWKfFIZM2B9euMXhPTBcmRChs4wdW15j4CuhsQOmEZzFvShJvFWVJlPuUH2OJnIfcb4O9s3eGpa2tidJ5Vvm2oauBnhiQiPJRd349ea0mg0V80kw1-2mAy05wVE5Z6xvxJ-y4fm8lnCeM1pkYoin4iL5lw9SISJAmot84hUseBrnm1XAkSMZh9nJ1zWTpTaZpfnFI7J6wPgoAcpIeEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642dd7275.mp4?token=IyE_Jsm_P7SnXOeZP7S3p8PQnoHUTGh2nmRdcnHKEUEvlW_wGs6-sBZ4Dv2JPiIjQFpHOYoozQZGUFbAIWqosUflN7DqgrpGyx3xYuqZyMRTkv28B-_l9ySDRiwXHmW7DY0iWKfFIZM2B9euMXhPTBcmRChs4wdW15j4CuhsQOmEZzFvShJvFWVJlPuUH2OJnIfcb4O9s3eGpa2tidJ5Vvm2oauBnhiQiPJRd349ea0mg0V80kw1-2mAy05wVE5Z6xvxJ-y4fm8lnCeM1pkYoin4iL5lw9SISJAmot84hUseBrnm1XAkSMZh9nJ1zWTpTaZpfnFI7J6wPgoAcpIeEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
خلافات داخل مجلس النواب العراقي خلال طرح اسم لأحدى الوزارت.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75377" target="_blank">📅 18:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75376" target="_blank">📅 18:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=KV3FjjoFxMTR7tqUEF87FNIaPzbQDr9pJCSYBVcHk-ukFNkEny9jhNYhqHuNPOb5aENxnSSyad9Fy7xJnKgfKKEV9wJZUpdW6M6jLgEmXESHxoQ_Vnz323YhxLwSNgdGjYpCIE0sIO7Rf4I5YQ3tjL1jR7AmaNP4vRXX9eGUYZtAxqaIeFKpgDs6n7vmqldj_kT_Wpn2p10lp7ubOzJMh2AuPA6qdoM_gb5K5XBt__BQeKr6jLTpYQbzDlxn_B5zy9_THUf7hn9wnkp2DMUz8K5_L2g1YsHUvHhI48Ls06PYWIHk1kbbwojx_2n6Kk8I5TkleMwpSe5d3_es9F31xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=KV3FjjoFxMTR7tqUEF87FNIaPzbQDr9pJCSYBVcHk-ukFNkEny9jhNYhqHuNPOb5aENxnSSyad9Fy7xJnKgfKKEV9wJZUpdW6M6jLgEmXESHxoQ_Vnz323YhxLwSNgdGjYpCIE0sIO7Rf4I5YQ3tjL1jR7AmaNP4vRXX9eGUYZtAxqaIeFKpgDs6n7vmqldj_kT_Wpn2p10lp7ubOzJMh2AuPA6qdoM_gb5K5XBt__BQeKr6jLTpYQbzDlxn_B5zy9_THUf7hn9wnkp2DMUz8K5_L2g1YsHUvHhI48Ls06PYWIHk1kbbwojx_2n6Kk8I5TkleMwpSe5d3_es9F31xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75375" target="_blank">📅 18:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa365d566.mp4?token=rohHujM9py4FB0wylZz6kWvU35WgOGzQlXaUHTkWzuH4BPZvAsxTVT96r2kzg3kWPwDzaTuQTRHGd4GprI0MW20D0rpxkbvrC2md8iT-jmKz9NbCbUiOc2mKSoI9EYjcmbWwLlLbgzzQSqZd-3Nsrv_EVktN7CkkBhDmca41pbo4CgyidhA_7n2YnU-7ZPtdkClcD6swgG3buu2ytcIV-yQ6Jty0PQLUUxYb1tRDmhOEWV4ISJp7sZsju03cemtPsEkY2heHNEpTId6X1uApWUvie-q7kGYlP_flXPHCAfhEtxtUe3Hjc198EwjryO46i3nN1UFdkzyTQPyDmGn24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa365d566.mp4?token=rohHujM9py4FB0wylZz6kWvU35WgOGzQlXaUHTkWzuH4BPZvAsxTVT96r2kzg3kWPwDzaTuQTRHGd4GprI0MW20D0rpxkbvrC2md8iT-jmKz9NbCbUiOc2mKSoI9EYjcmbWwLlLbgzzQSqZd-3Nsrv_EVktN7CkkBhDmca41pbo4CgyidhA_7n2YnU-7ZPtdkClcD6swgG3buu2ytcIV-yQ6Jty0PQLUUxYb1tRDmhOEWV4ISJp7sZsju03cemtPsEkY2heHNEpTId6X1uApWUvie-q7kGYlP_flXPHCAfhEtxtUe3Hjc198EwjryO46i3nN1UFdkzyTQPyDmGn24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75374" target="_blank">📅 18:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">استهداف دبابة ميركافا من قبل حزب الله في بلدة الطيبة جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75373" target="_blank">📅 18:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مجلس النواب يُصوّت على المنهاج الوزاري لرئيس مجلس الوزراء المكلّف علي فالح الزيدي</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75372" target="_blank">📅 18:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4850c33fc2.mp4?token=vuYLZQJW6eqLie_6apxUzgjWjRCugkTfshW-wOa4u--XxXLHVWjQ_YV26pox46k55CPeaRDzG1U83n80h96HDaSUC0P95UcgoKMBSz1xMlgqBOjF2YK8-L2BsH0Y0WRL5tNMEvRUlmAJIKo44MY4HVeBRcSEg5baMc-w79KxSHwUbU7uoev9Zaei9krvoNb5sUxkL7ykLf9mku1r7-e4EjwfWRkV97f_1kCJLoD-LXeRoemwSu0-AdsDHs2lMxB7r8X-1Z9MHax_Sq6URHuSRfjkqecGhpjnFdAc4YtM0stUCbYL5Prtt58VuxBfyUw5jZ5O9doUJN354kNrWaB52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4850c33fc2.mp4?token=vuYLZQJW6eqLie_6apxUzgjWjRCugkTfshW-wOa4u--XxXLHVWjQ_YV26pox46k55CPeaRDzG1U83n80h96HDaSUC0P95UcgoKMBSz1xMlgqBOjF2YK8-L2BsH0Y0WRL5tNMEvRUlmAJIKo44MY4HVeBRcSEg5baMc-w79KxSHwUbU7uoev9Zaei9krvoNb5sUxkL7ykLf9mku1r7-e4EjwfWRkV97f_1kCJLoD-LXeRoemwSu0-AdsDHs2lMxB7r8X-1Z9MHax_Sq6URHuSRfjkqecGhpjnFdAc4YtM0stUCbYL5Prtt58VuxBfyUw5jZ5O9doUJN354kNrWaB52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس مجلس الوزراء المكلّف "علي الزيدي" يبدأ قراءة المنهاج الوزاري للتصويت عليه.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75371" target="_blank">📅 18:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da1de53a6.mp4?token=sdrlQHEGeK4o7mZosI2ntBRGnu9REukj6CRblFA7pT5dMQ6KFzrNbIeNdfp5EkH4KPaRpb2Ahk6kFOVOt-7bJQt6g-uMjPHPh1c3qTSlv__Xq4q_y7plsG3-S33pMMJFAc2YjIxH0usz6h3dofBAOnwV62JtBjG9AxtEIS6K8tlhm-h8f9KT75osIRP6LODxbxUSeEwvOmrfc5gRYzg999GzkTqw6ZZZ943gjhyfJfXTTsscMa6hP_NVVUkRE97G4tiE6O2gjCr1t7DbqIGqK1d3NJEQGQThGdhHY4QiXFtvt79GcP_k439mh6M8tNoeWgV95pMQmRHedBPypJkPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da1de53a6.mp4?token=sdrlQHEGeK4o7mZosI2ntBRGnu9REukj6CRblFA7pT5dMQ6KFzrNbIeNdfp5EkH4KPaRpb2Ahk6kFOVOt-7bJQt6g-uMjPHPh1c3qTSlv__Xq4q_y7plsG3-S33pMMJFAc2YjIxH0usz6h3dofBAOnwV62JtBjG9AxtEIS6K8tlhm-h8f9KT75osIRP6LODxbxUSeEwvOmrfc5gRYzg999GzkTqw6ZZZ943gjhyfJfXTTsscMa6hP_NVVUkRE97G4tiE6O2gjCr1t7DbqIGqK1d3NJEQGQThGdhHY4QiXFtvt79GcP_k439mh6M8tNoeWgV95pMQmRHedBPypJkPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس النواب يعقد جلسته للتصويت على المنهاج الوزاري وحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75370" target="_blank">📅 18:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72718a0f45.mp4?token=BhyzkaAbwmR1QESWq7rj2Buzth-G8et0gIZqBSMttyGjrwvvWYSnzW6flRYwcQThdK-G1YGBRdt2HoztY-_YgKpGjc1zWRa02Sm05SrBXm97hR8lLtMJHuphrfGN5733tcQZNGq5x9J8KqCjAMFgjFNOa9BETl0JfvYnxxQ18QWClXB4Q9Sw1CXkRJOZL-DBCBnZ9HC3Rm830g3Uyd7P-xlH9XVLlW4vxyumMqWm0nXOozIhIT3_-6kgqOKZYlDnoSxizVg9W2Qa34RY7LX85y2TN-do5OXCj0r3EIjjqGvR6WdzPmNK24FsLlCZuyuzK2fDqIgTvnF1VJFCQ6zZvb9oQFI9BeieKzgH9DAnhCsZ26JM--9aG9NR2-9eaUXbcZXt7HHN1mtUo_NkQhT_mXnqcy1UhBtVsJT-RqjqT9FB8JEYkgwf35OFYsvRWugixYKaYUVNsDN3sUlwg7nMrGVe7Aw2w40p3qWfFlxgLgkQR_sO1TnHbo698QKo0Zc_mV3OPkwinSIIRp9keD0yBpStEeV72Yq3XFsEli9iPsDMTZ5ewSwGmBHiy4NL22XMjjPUA-htTmIEmtIKa4FhsSOMecH_Rv0h0RFB5HYTzAt1oTXVUQ3Kk0gh3TnwO3eH7_A2IxpMxiPmM_rLFqoTnsTScjJ5SFR97ivUQPSQXZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72718a0f45.mp4?token=BhyzkaAbwmR1QESWq7rj2Buzth-G8et0gIZqBSMttyGjrwvvWYSnzW6flRYwcQThdK-G1YGBRdt2HoztY-_YgKpGjc1zWRa02Sm05SrBXm97hR8lLtMJHuphrfGN5733tcQZNGq5x9J8KqCjAMFgjFNOa9BETl0JfvYnxxQ18QWClXB4Q9Sw1CXkRJOZL-DBCBnZ9HC3Rm830g3Uyd7P-xlH9XVLlW4vxyumMqWm0nXOozIhIT3_-6kgqOKZYlDnoSxizVg9W2Qa34RY7LX85y2TN-do5OXCj0r3EIjjqGvR6WdzPmNK24FsLlCZuyuzK2fDqIgTvnF1VJFCQ6zZvb9oQFI9BeieKzgH9DAnhCsZ26JM--9aG9NR2-9eaUXbcZXt7HHN1mtUo_NkQhT_mXnqcy1UhBtVsJT-RqjqT9FB8JEYkgwf35OFYsvRWugixYKaYUVNsDN3sUlwg7nMrGVe7Aw2w40p3qWfFlxgLgkQR_sO1TnHbo698QKo0Zc_mV3OPkwinSIIRp9keD0yBpStEeV72Yq3XFsEli9iPsDMTZ5ewSwGmBHiy4NL22XMjjPUA-htTmIEmtIKa4FhsSOMecH_Rv0h0RFB5HYTzAt1oTXVUQ3Kk0gh3TnwO3eH7_A2IxpMxiPmM_rLFqoTnsTScjJ5SFR97ivUQPSQXZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هل ناقشت دعم الصين لإيران مع الرئيس الصيني؟
‏ترامب: لقد ناقشنا الأمر. هممم. أعني، عندما تقول "دعم"، فهم لا يخوضون حربًا معنا أو أي شيء من هذا القبيل. قال إنه لن يقدم معدات عسكرية. هذا تصريحٌ كبير. لكن في الوقت نفسه قال إنهم يشترون الكثير من نفطهم من هناك، ويرغبون في الاستمرار في ذلك.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75369" target="_blank">📅 18:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب: عرض الرئيس الصيني تقديم المساعدة بشأن إيران</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75368" target="_blank">📅 18:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قيادات سياسية ورئاسات في مبنى البرلمان قبل انطلاق جلسة منح الثقة لحكومة الزيدي</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75367" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhrsk4YpLd8FYMwlG3N9sMuXlOgRkFX6ExYMJRVvY4X9sMmQ9cNGnD6LTkZXPaSQ0qnWJA0FZN50Gqgp39MqXeOe30HhXCratPF2w5Cp9Dc_qWMv5YxavpTzLw2VDYDyWeWyJ7ZCdK_2zVjiuzhyTVJovhILuSl60cLBwR00xC8VeukD1BBtTV1Wr1Zsr-IFD0mHu1KcGEos7lc3sLPY6C-m_ZkAHOzlHZNj765lDboYZXIH5fYcSHk339A5HUZC34I5k7VMtXJwyeFlioLJi-EVJWsratuvH8mzsRWUaOJKOxX6yl1f5rS4w-ZmotKyObZ-k3GMIwDlpOEF_jKXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرع جرس البرلمان إيذاناً ببدء جلسة منح الثقة لحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75366" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5hFuEKKzvZCrPH2cbrtGBwVG_SXbOlXMHWsqZ6HJt3SmxpTkhSiUbQAv9QGirHUX6rNC1OV9EXuO4CD_qxDj-vT2N0hyFHK2a4oeXnFh-iu3Uoq5CdwTqUjHPkbCeYLEnqCEuurLMNuN_c0izcQDz8dvPFE4JQQjCt32FjCa_v0FKXW7Gv36euoRDqKQ4PM-GlHk3qRn2G6EZEWjqQ9aqz2u4-naHkoI-YLuyFOV7D5sk9lRJLZkvoFErx6ZwIkUdykyxSl9JIABaG_sXZbt20StWnXoD7PA0NDGN3K0eO5r5fxb0eRK6VXYOMH_PzqsftfVqJzGZ2cSLnhS6Je1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قائد القيادة المركزية الأمريكية:
في الأشهر الثلاثين الماضية فقط قبل بدء عملية الغضب الملحمي، هاجمت جماعات إرهابية مدعومة من إيران القوات والدبلوماسيين الأمريكيين أكثر من 350 مرة - أي ما يعادل هجومًا كل ثلاثة أيام أو أكثر، مما أسفر عن مقتل أربعة من أفراد الخدمة الأمريكية وإصابة ما يقرب من 200 آخرين.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75365" target="_blank">📅 17:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">القيادات السياسية والرئاسات تتوافد لمجلس النواب العراقي للمشاركة في جلسة منح الثقة لحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75364" target="_blank">📅 17:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فايننشال تايمز:
‏السعودية تطرح معاهدة عدم اعتداء في الشرق الأوسط مع إيران.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75363" target="_blank">📅 17:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75362">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة عيناثا جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75362" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75361">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9AgBfOUXV5N0QKg4TFUwvpIu_HczvYYxia3ZX5B6PKQ3mct8COYg3rtfjkN1j5RcT6NlZS8UV2WxZFQ3RoNaLURPBIfusiHToTfE-JYE7JAPzvD2c-kPCU3NexNoMYDIdK_tws7aT3psictsTdbyKG0d7gBqp6yrn7c2JKTLU7c1n1Ts3PqEHJLsl0ZC1VuvrJ9kdeKkU1u2hB8S7d4wsTJrwkzKR4s4OyI74KGrtmyx1kaS8I1M2CgCqwg-8OXOBzrRnmrx51e-AoWxa3yTetJK2vpcLsaM3MptFCceR7JLxwYN7vFNqBpDp20CYuq6cZpgGZAFr6cW0qdMieRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية: ايقاف برنامج (الحق يقال) الذي يقدمه عدنان الطائي لمدة 45 يوم بسبب مخالفة الضوابط والمعايير الاعلامية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75361" target="_blank">📅 17:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75360">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-05-2026 جنود من جيش العدو الإسرائيلي في محيط بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75360" target="_blank">📅 17:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75359">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تأجيل الجلسة نصف ساعة</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75359" target="_blank">📅 16:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الان - العراق   المرشحين للوزارات ورئيس الوزراء يغادرون القصر الرئاسي باتجاه قاعة مجلس النواب</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75358" target="_blank">📅 16:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الان - العراق
المرشحين للوزارات ورئيس الوزراء يغادرون القصر الرئاسي باتجاه قاعة مجلس النواب</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75357" target="_blank">📅 16:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75356">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صندوق النقد الدولي:
العراق سعى للحصول على مساعدات مالية، محادثات جارية مع العراق حول حجم التمويل وهيكلة قرض محتمل.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75356" target="_blank">📅 16:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDR2w02_mdLoRwaEPVIfjWFKLxSwukMpnhWPhngCtWBxBzxpEiOX3CHLFYCYrKS7snQFYBtgJW2jbz2yTD4S38XsZQFu0gNZ4pfrrxop8LG4ASMM8BmWjrPGwfYdGAOtX1dFl9XjufrutTJ_mkj2gS75xNgL3YSHMWSYxTihA1jF2ZN4w-27ExfQXHX5flWox2gkzc-JGpubm4813NKW00iQBASp0lwkhfYNg-ljK5a0Mnblwt2a1n7W-PjeiQLOduy4xf1yDiJ9K3vuaDXGXuiizduJgyaT_Yz0cwwLXbgHGETCY4WPooXkFcvDVSO7PG08rXeJ__jUJX4AK2oaPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غضب جماهيري في مواقع التواصل الاجتماعي بعدما بثت قناة العربية السعودية تقرير خاطئ يتحدث عن العراقيات نقلا عن تقرير أمريكي وبعد البحث تبين انه غير صحيح وغير موجود</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75355" target="_blank">📅 16:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مكتب نتن ياهو:
توجيهات لوزير الخارجية لجدعون ساعر برفع دعوى ضد نيويورك تايمز على خلفية أحد المقالات حول اغتصاب أسرى فلسطينيين في السجون الإسرائيلية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75354" target="_blank">📅 15:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزيى الحرب الصهيوني:
مهمتنا في إيران لم تنتهِ، جاهزون لاحتمال أن نضطر للعمل قريبًا.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75353" target="_blank">📅 15:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75352">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXX1MX2HPTbdKffRBO7F8argSyIbdslbgFcQ0Ndb-tw4zV-HJx_kKVe1VuOF5jMDolYiv1AACgRuL26VZcU2Nm-OloaKihjNxMRATCmsMpVDuAEjzwJZPl3KHtA2a54Cnzro5fXk3UDkKGv8l55oUuZjRlqqTG46h2zO8z8y_-6zVcfBr35Jq3MxYGQyS_qzrCCBHH3hVMa65crijeCSIWwDA3bcllo-3pK7yqvtlMC5DitRWsIGwy98bCr6iHMwUSMP9O2YOAh-F-hJUIgScRM2IljlwYMq2nKMs8UUdtUBnbrw0WvqY4cM9Fm6TOTMWUo5jvtMPOUlvjzj2TPr2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة / نايا   مصطفى جبار سند المرياني وزير مرشح بقوة في حكومة الزيدي …</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75352" target="_blank">📅 15:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75351">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CV حكومة علي الزيدي.pdf</div>
  <div class="tg-doc-extra">8 MB</div>
</div>
<a href="https://t.me/naya_foriraq/75351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">السّير الذاتية لمرشحي الكابينة الوزارية لحكومة رئيس الوزراء المكلف علي الزيدي</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75351" target="_blank">📅 15:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75350">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رئيس حزب
إسرائيل بيتنا
ليبرمان:
أنا قلق جداً ولدي كل الأسباب للقلق، أن رئيس وزراء السابع من أكتوبر (يقصد نتن ياهو) مع تقديم قانون حل الكنيست، سيبدأ عملية عسكرية تهدف فقط لأغراض الانتخابات</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75350" target="_blank">📅 14:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75349">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 08-05-2026 قاعدة شراغا التابعة لجيش العدو الإسرائيلي جنوب مستوطنة نهاريا بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75349" target="_blank">📅 14:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
قائد سلاح الجو الإسرائيلي السابق اللواء عميكام نوركين:
أنا أشعر بالخجل والعار مما حدث لنا في السابع من أكتوبر 2023. من دون الولايات المتحدة، لما كانت إسرائيل قادرة على الصمود خلال الحرب</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75348" target="_blank">📅 14:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75347">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم لحزب الله</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75347" target="_blank">📅 13:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وفاة ضابط برتبة مقدم وجرح ثلاثة مراتب آخرين من جهاز المخابرات العراقي بحادث سير على الطريق الدولي .</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75345" target="_blank">📅 13:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caZOfbVkShwJiWcGVo2ox9xwJdFpsS_NJX1XsGTi3pty1iGriWj5hbkWbWMHA0DeXHAsZMVBrjl-pQ43ApOS8uHBMHm-I6bfbmIqMMB6RVre4SwdE_42hey4DQ1gbzTXtXq3H7hw1s2VMfpZWB07mDLPp-PlLTCC4VeXxOPZoVz3mlt6y5ZXpnGQ11GOQemdsq57JmqPCuKNj6qwCrON-rIjePcGSiIKcKIk5a5sb1xfvfgE-270KAUz2Xa5JrY5oxsRSBG6nvl3i3OWJGQkYnbUGUcBx8eGFmKmOIfbwLrD1PJlx4GVtkm_YoU8GNVo5K7tSVpD2foWKQIZYXVxnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جريمة بحق طفلة شيعية في سوريا..
بعد 45 يوماً من اختطاف الطفلة الشيعية زينب صدام ذات ال 15 عام في قرية الغور الغربية بمدينة حمص، عثر عليها مرمية على جانب الطريق بعد دفع ديتها متعرضة للاغتصاب الوحشي وفاقدة للذاكرة بسبب حقنها بجرعات مكثفة من المخدرات وبعد ذلك قامت حكومة الجولاني الإرهابية بزجها في السجن وترك مرتكبي هذه الجريمة من عصاباتهم دون حساب.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75344" target="_blank">📅 12:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عدد كبير من القتلى والجرحى في صفوف جنود الاحتلال الإسرائيلي بعد كمين من قبل حزب الله في جنوب لبنان</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75343" target="_blank">📅 12:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بلومبرغ عن بيانات ملاحية:
9 سفن محملة بالنفط والغاز عبرت مضيق هرمز منذ يوم الأحد
لا تزال بعض السفن الـ9 داخل خط الحصار الأمريكي في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75342" target="_blank">📅 11:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">إطلاق نار داخل معسكر دبلن في مطار بغداد الجناح العسكري .</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75341" target="_blank">📅 11:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">إطلاق نار داخل معسكر دبلن في مطار بغداد الجناح العسكري .</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75340" target="_blank">📅 10:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حدث بحري شمال شرق الفجيرة</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75339" target="_blank">📅 10:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حدث بحري شمال شرق الفجيرة</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75338" target="_blank">📅 10:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75337">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: مضيق هرمز مفتوح أمام جميع السفن التجارية من وجهة نظرنا لكن يتعين عليها التعاون مع قواتنا البحرية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75337" target="_blank">📅 10:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏وزارة خارجية كوريا الجنوبية: 24 من أفراد الطاقم على متن السفينة الكورية في مضيق هرمز</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75336" target="_blank">📅 06:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8522f3e0a6.mp4?token=Q1KKcFQsnNrJT1OiDKa9k1sLrM9eYK_Mz2ctiML87_RoPz9O17YxhEPnfmajXT-LzICnM1DjVOyIi_uV9A1eCn6QyYGaSuKBN880WIJIeZmRvxIpKNx_X-liL_cFyWA4gntcFqarPNT2nR2kLYE2Ypjm6YCcFh2aZ5ZdifjK_AQ-8dqt3JhVLwF3cadrxzPdezTWA6Ycfn5JRkb1TuKYnimWljRVGrhepBZu9CEr7vqZ7_jky4nwMiwwnJCtwolXzpA4CjXNP7vvlEQMk-Z_JIBjMO0zOj_0-6YPZcW4RQiAjxYHmzqfAxFTdTKZ536N3Ner-ejVR0colvsLw6RcrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8522f3e0a6.mp4?token=Q1KKcFQsnNrJT1OiDKa9k1sLrM9eYK_Mz2ctiML87_RoPz9O17YxhEPnfmajXT-LzICnM1DjVOyIi_uV9A1eCn6QyYGaSuKBN880WIJIeZmRvxIpKNx_X-liL_cFyWA4gntcFqarPNT2nR2kLYE2Ypjm6YCcFh2aZ5ZdifjK_AQ-8dqt3JhVLwF3cadrxzPdezTWA6Ycfn5JRkb1TuKYnimWljRVGrhepBZu9CEr7vqZ7_jky4nwMiwwnJCtwolXzpA4CjXNP7vvlEQMk-Z_JIBjMO0zOj_0-6YPZcW4RQiAjxYHmzqfAxFTdTKZ536N3Ner-ejVR0colvsLw6RcrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الرئيس الصيني يستقبل الرئيس الأميركي في بكين</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75335" target="_blank">📅 06:35 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
